"""The determinism job's own assertions, run off GitHub (R304, R307).

Two of this workflow's steps are gates rather than diagnostics: the one that
decides whether a leg's golden comparison passed, and the one that decides
whether the ten legs agree. Both were written as inline YAML, and inline YAML is
executed nowhere but on GitHub -- which is how `bad` came to be computed,
written into `regression.txt`, printed by the verdict job and **asserted
nowhere**. A leg reporting `4 collected, 3 failed` exited 0, ten times, inside a
green job.

`scripts/run_rung.sh` exists because of the same lesson one level up: a claim
about a gate that can only run on GitHub has a corpus of zero. These steps are
still inline, because they are five lines each and belong beside the artifact
they read -- so this file lifts the two `python - <<'PY'` bodies out of the
workflow and runs them against fabricated inputs.

WHAT IS FABRICATED AND WHY. A junit report with three failing cases out of four
is what a real red golden run produces, and no other input reaches that branch:
`tests/regression` is green here, so a test that waited for a real failure would
never run the assertion. The controls are the shapes that must stay green.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"

_JUNIT = """<?xml version="1.0" encoding="utf-8"?>
<testsuites><testsuite name="pytest" tests="{n}">
{cases}
</testsuite></testsuites>
"""


def _body(after: str) -> str:
    """The first `python - <<'PY' ... PY` heredoc following `after`.

    Read out of the workflow rather than copied into this file: a copy would
    pass for ever while the workflow drifted, which is the shape this whole
    file exists to refuse.
    """
    text = WORKFLOW.read_text(encoding="utf-8")
    start = text.index(after)
    open_at = text.index("python - <<'PY'", start)
    lines = text[open_at:].splitlines()[1:]
    out: list[str] = []
    for line in lines:
        if line.strip() == "PY":
            break
        out.append(line)
    body = textwrap.dedent("\n".join(out))
    assert body.strip(), f"no heredoc body found after {after!r}"
    return body


def _junit(total: int, failures: int) -> str:
    cases = []
    for i in range(total):
        inner = "<failure message='golden moved'/>" if i < failures else ""
        cases.append(f"<testcase classname='c' name='t{i}'>{inner}</testcase>")
    return _JUNIT.format(n=total, cases="\n".join(cases))


def _run(body: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-"],
        input=body,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


# ---------------------------------------------------------------- the leg


@pytest.mark.parametrize(
    "total, failures, must_fail, why",
    [
        (4, 0, False, "the shape every leg has produced so far: the control"),
        (4, 3, True, "R304 exactly: the goldens moved and the leg said nothing"),
        (4, 4, True, "every golden moved"),
        (1, 1, True, "one case, one failure -- the smallest red there is"),
        (0, 0, True, "collected nothing, which the step already caught"),
    ],
)
def test_the_leg_reports_its_golden_run(
    total: int, failures: int, must_fail: bool, why: str, tmp_path: Path
) -> None:
    (tmp_path / "leg").mkdir()
    (tmp_path / "leg" / "regression.xml").write_text(_junit(total, failures), encoding="utf-8")
    out = _run(_body('name: "measure: the regression rung'), tmp_path)
    failed = out.returncode != 0
    assert failed == must_fail, (
        f"{total} cases, {failures} failing: the leg exited {out.returncode} and "
        f"must{'' if must_fail else ' not'} fail. {why}\n"
        f"{out.stdout}\n{out.stderr}"
    )


def test_the_leg_step_writes_the_row_the_verdict_job_reads() -> None:
    """The two steps are coupled by a filename, and nothing else says so."""
    body = _body('name: "measure: the regression rung')
    verdict = _body("all ten hashes equal")
    assert "regression.txt" in body and "regression.txt" in verdict, (
        "the leg writes a file the verdict job does not read, or the other way "
        "round. The coupling is a filename in two places and this is what "
        "notices when one of them moves."
    )


# ------------------------------------------------------------ the verdict


def _legs(tmp_path: Path, n: int = 10, **odd: object) -> Path:
    """Ten leg directories as `download-artifact` lays them out."""
    root = tmp_path / "legs"
    root.mkdir()
    for i in range(1, n + 1):
        d = root / f"determinism-leg-{i}"
        d.mkdir()
        figures = f"# figures\ncontent for leg {i}\n" if odd.get("split") == i else "# figures\n"
        # BYTES, not `write_text`. On Windows the default newline translation
        # rewrites every newline on the way out, so the file stops hashing to
        # what was hashed here and the CONTROL fails for a reason that has
        # nothing to do with the gate under test.
        (d / "F2_figures.md").write_bytes(figures.encode())
        claimed = hashlib.sha256(figures.encode()).hexdigest()
        if odd.get("lies") == i:
            claimed = "0" * 64
        (d / "figures.sha256").write_text(claimed + "\n", encoding="utf-8")
        (d / "cpu.txt").write_text("AMD EPYC 7763\n", encoding="utf-8")
        core = "unset" if odd.get("unpinned") else "Haswell"
        (d / "coretype.txt").write_text(core + "\n", encoding="utf-8")
        (d / "regression.txt").write_text("4 collected, 0 failed\n", encoding="utf-8")
        if odd.get("no_artifact") == i:
            (d / "F2_figures.md").unlink()
    return root


@pytest.mark.parametrize(
    "kwargs, must_fail, why",
    [
        ({}, False, "ten legs, one hash, one kernel: the control, and the CG1 result"),
        ({"split": 3}, True, "one leg renders different bytes -- the vendor split"),
        ({"lies": 5}, True, "R307: the uploaded file is not what the leg claims"),
        ({"no_artifact": 7}, True, "R307: a leg with no artifact to commit"),
        ({"unpinned": True}, True, "ten agreeing legs with the kernel unpinned"),
        ({"n": 9}, True, "a leg that never reported"),
    ],
)
def test_the_verdict_job_rules_on_the_ten_legs(
    kwargs: dict, must_fail: bool, why: str, tmp_path: Path
) -> None:
    _legs(tmp_path, **kwargs)
    out = _run(_body("all ten hashes equal"), tmp_path)
    failed = out.returncode != 0
    assert failed == must_fail, (
        f"{kwargs}: the verdict job exited {out.returncode} and must"
        f"{'' if must_fail else ' not'} fail. {why}\n{out.stdout}\n{out.stderr}"
    )


def test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8() -> None:
    """CH3, re-expressed for the collapsed ladder (CK0).

    Ladder 4 has been red under Q8 for eleven rounds; while ladder 6 was
    `needs:`-chained behind it the goldens ran on ten determinism legs and
    were gated on none of them. The ladder's ordering rule is about
    interpretability, and "do today's bytes equal yesterday's" stays
    interpretable whatever ladder 4 says.

    THE SHAPE CHANGED AND THE PROPERTY DID NOT. Six jobs became six steps of
    one job, and steps stop at the first failure -- so the chain is now the
    ORDER, and rung 6 is not behind rung 4 exactly when its step comes first.
    It still comes after rungs 1 to 3, which are what make a golden's inputs
    mean anything.
    """
    text = WORKFLOW.read_text(encoding="utf-8")
    ladder = text[text.index("  ladder:") :]
    order = [
        line.split("run_rung.sh", 1)[1].strip()
        for line in ladder.splitlines()
        if "run_rung.sh" in line
    ]
    assert len(order) >= 6, f"the ladder job runs {len(order)} rungs: {order}"
    where = {n: i for i, step in enumerate(order) for n in ("rung3", "rung4", "rung6") if n in step}
    assert {"rung3", "rung4", "rung6"} <= set(where), f"rungs missing from {order}"
    assert where["rung6"] < where["rung4"], (
        "the goldens run after ladder 4, so a red ladder 4 stops them -- which "
        "is where they were for eleven rounds, gated nowhere while running on "
        "ten determinism legs."
    )
    assert where["rung3"] < where["rung6"], (
        "the goldens run before rung 3, whose tests are what make a golden's "
        "inputs mean anything."
    )
