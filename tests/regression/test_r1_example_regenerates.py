"""The three published R1 deliverables ARE what this tree regenerates (R845).

**NOTHING IN THIS REPOSITORY COMPARED A SINGLE NUMBER IN THOSE THREE FILES.** Measured by
editing the committed artifacts and running `tests/regression tests/unit`, five runs, one
injection at a time:

    baseline                                    400 passed, 0 failed
    report.md  **U = 1.71167** -> 0.99999       400 passed, 0 failed
    utilisation.csv  0.701035 -> 0.0701035      400 passed, 0 failed
    member_forces.csv  4.992194e+06 -> e+07     400 passed, 0 failed
    restored                                    400 passed, 0 failed

The first of those is the one that matters: **the governing utilisation went from over
unity to under unity** -- from a member that fails its code check to one that passes -- in
a file that goes to Xabier, and the whole suite stayed green.

The reason the existing gates could not see it, which is the part worth keeping: it was
covered twice and by neither. `test_r1_example_golden.py` compares a FRESH run against
`docs/F4_member_forces.csv` and `docs/F6_utilisation.csv`, so it checks the TOOL and never
reads `results/R1/example/`. `test_r1_published_artifacts.py` reads those three files and
asserts constants and strings -- the caveats, the disclaimer, the clause limits, the
commented header -- which is the published FORM and no number in it. **A file can be
covered by two test files and have none of its numbers compared.**

`results/F6/` has had this shape since R756
(`test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`), and it is what
caught FQ0's limit moving. This is that gate for `results/R1/example/`. Verdicts 7 and 8
both named it as R838's proper repair and two narrower needles shipped instead.

**THE RUN IS REDIRECTED, NOT RE-PUBLISHED.** The fixture points `outputs.directory` at a
temporary directory, so the committed files are read and never written by this test. A gate
that regenerated in place would overwrite the evidence it is checking.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"
PUBLISHED = ROOT / "results" / "R1" / "example"

NAMES = ("report.md", "member_forces.csv", "utilisation.csv")

# TWO DECLARED CLASSES OF LINE ARE EXCLUDED FROM THE BYTE COMPARISON, AND BOTH ARE CHECKED
# SEPARATELY. An excluded line is a line nothing checks unless something else checks it.
#
# (1) THE WALL CLOCK. FL1(d) asks for the run time, so the report carries a
#     `| stage | seconds |` table whose three rows cannot agree between two runs. Measured
#     across three machine states: total 65.97, 97.27 and 126.26 s.
_TIMING_ROW = re.compile(r"^\|\s*(build|solve|total)\s*\|\s*[0-9.]+\s*\|\s*$")

# (2) THE PROVENANCE PATHS, which the first run of this gate found rather than assumed. The
#     fixture writes its configuration to a temporary directory with ABSOLUTE deck and npz
#     paths, because a configuration's relative paths resolve against its own directory. So
#     three provenance lines name this machine's paths where the shipped ones name
#     repository-relative paths. Those three lines and the timing rows were the ONLY
#     differences across all three files: 102, 1289 and 73 comparable lines agreed
#     otherwise, which is the measurement that says the numbers are reproduced.
#
#     Their CONTENT is compared by `test_R845_the_PROVENANCE_values_agree_by_BASENAME`.
_PROVENANCE_PATH = re.compile(
    r"^(?:#\s*|\*\s+\*\*)(config|deck|load_cases)(?:\*\*)?\s*[:—-]\s*(.+?)\s*$"
)


@pytest.fixture(scope="module")
def regenerated(tmp_path_factory: Any) -> dict[str, str]:
    """`floatfea run` on the shipped example, written to a temporary directory.

    Only `outputs.directory` changes in substance. The deck and npz paths are absolutised
    for the same reason `tests/unit/test_run_config.py` absolutises -- a configuration's
    relative paths resolve against ITS OWN directory, so a copy written elsewhere cannot
    keep them.
    """
    from floatfea.cli import main

    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    out = tmp_path_factory.mktemp("r1_regen")
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    if data["load_cases"].get("npz"):
        data["load_cases"]["npz"] = str((EXAMPLE.parent / data["load_cases"]["npz"]).resolve())
    data["outputs"]["directory"] = str(out)

    cfg = out / "config.yaml"
    cfg.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    assert main(["run", str(cfg)]) == 0, "`floatfea run` did not exit 0 on the example"
    return {n: (out / n).read_text(encoding="utf-8") for n in NAMES}


def _excluded(line: str) -> bool:
    """The two declared classes, and nothing else."""
    return bool(_TIMING_ROW.match(line) or _PROVENANCE_PATH.match(line))


def _lines(text: str) -> list[str]:
    return [ln.rstrip("\r") for ln in text.splitlines() if not _excluded(ln.rstrip("\r"))]


def _provenance(text: str) -> dict[str, str]:
    """`{key: the last path component}` for the three environment-dependent lines."""
    out: dict[str, str] = {}
    for raw in text.splitlines():
        m = _PROVENANCE_PATH.match(raw.rstrip("\r"))
        if m:
            out[m.group(1)] = m.group(2).replace("\\", "/").rsplit("/", 1)[-1]
    return out


@pytest.mark.parametrize("name", NAMES)
def test_R845_the_PUBLISHED_deliverable_is_what_this_tree_REGENERATES(
    name: str, regenerated: dict[str, str]
) -> None:
    """Every number in the committed file is compared against a fresh run.

    This is the gate that would have caught a governing utilisation edited from `1.71167`
    to `0.99999`, which three existing test files did not.
    """
    shipped_path = PUBLISHED / name
    assert shipped_path.is_file(), f"{shipped_path.relative_to(ROOT)} is not committed"

    shipped = _lines(shipped_path.read_text(encoding="utf-8"))
    fresh = _lines(regenerated[name])
    # `strict=False` DELIBERATELY. `strict=True` raises on a length mismatch, and a length
    # mismatch is one of the two things this test REPORTS -- the assertion below names both
    # counts, which a `ValueError` from the zip would replace with a traceback.
    differing = [
        (i + 1, a, b) for i, (a, b) in enumerate(zip(shipped, fresh, strict=False)) if a != b
    ]
    assert not differing and len(shipped) == len(fresh), (
        f"{name} is not what this tree regenerates: {len(differing)} line(s) differ, "
        f"shipped has {len(shipped)} comparable lines against {len(fresh)}. First three: "
        + " | ".join(f"line {n}: shipped {a!r} vs fresh {b!r}" for n, a, b in differing[:3])
        + " -- re-run `python -m floatfea.cli run examples/platform12_placeholder.yaml` "
        "AFTER the last edit to the code it publishes (CP3)."
    )


def test_R845_the_CSVs_carry_NO_excluded_timing_row(regenerated: dict[str, str]) -> None:
    """The wall-clock exclusion applies to the report alone, and the CSVs say so.

    If a wall clock ever reaches a CSV this reddens, rather than the exclusion quietly
    starting to cover it.
    """
    for name in ("member_forces.csv", "utilisation.csv"):
        for label, text in (
            ("shipped", (PUBLISHED / name).read_text(encoding="utf-8")),
            ("fresh", regenerated[name]),
        ):
            hits = [ln for ln in text.splitlines() if _TIMING_ROW.match(ln.rstrip("\r"))]
            assert not hits, f"{label} {name} carries a timing row: {hits[:2]}"


def test_R845_the_EXCLUSION_is_exactly_the_DECLARED_lines(
    regenerated: dict[str, str],
) -> None:
    """The exclusion cannot widen into "whatever differs".

    **A gate that drops the lines that disagree asserts nothing.** This pins the excluded
    set by KEY in both the shipped and the fresh report, so a fourth non-deterministic line
    reaching the deliverable reddens here instead of being absorbed.
    """
    for label, text in (
        ("the SHIPPED report", (PUBLISHED / "report.md").read_text(encoding="utf-8")),
        ("the fresh report", regenerated["report.md"]),
    ):
        stages = sorted(
            m.group(1) for ln in text.splitlines() if (m := _TIMING_ROW.match(ln.rstrip("\r")))
        )
        assert stages == ["build", "solve", "total"], (label, stages)
        keys = sorted(_provenance(text))
        assert keys == ["config", "deck", "load_cases"], (label, keys)


@pytest.mark.parametrize("name", NAMES)
def test_R845_the_PROVENANCE_values_agree_by_BASENAME(
    name: str, regenerated: dict[str, str]
) -> None:
    """The excluded provenance lines are CHECKED, not merely dropped.

    Only the directory prefix differs between a repository-relative path and this machine's
    absolute one, so the last component is the part that carries meaning -- and a
    deliverable naming a different deck or npz than the tree regenerates is exactly the
    class R845 is about.
    """
    shipped = _provenance((PUBLISHED / name).read_text(encoding="utf-8"))
    fresh = _provenance(regenerated[name])
    assert shipped, f"{name} carries no provenance line at all"
    for key in ("deck", "load_cases"):
        assert shipped.get(key) == fresh.get(key), (
            f"{name}: the {key} provenance names {shipped.get(key)!r} in the committed "
            f"file and {fresh.get(key)!r} in a fresh run of this tree."
        )
    # `config` is the one value that legitimately differs: the fixture's copy is named
    # `config.yaml` and the shipped run used the example's own name.
    assert shipped.get("config") == "platform12_placeholder.yaml", shipped
