"""FT2.6: the envelope over the UNION of several dynamic-inputs files.

**THE CELL THIS FILE EXISTS FOR IS THE ONE `npz_files[0]` CANNOT PASS.** The reviewer's
staging ruling named the hazard the rename cannot catch: `cfg.load_cases.npz_files[0]`
type-checks, the suite stays green, and the pipeline silently uses the first file. The
locked plan requires the envelope over the union and the report to name the governing
heading AND file (`docs/milestones/R1.md`, step 3's FT2.6 bullet), so a first-file run
publishes a deliverable attributing file one's answer to a union it never took.

The only thing that holds that is a case whose correct answer DIFFERS FROM THE FIRST
FILE'S ALONE. That is `test_the_union_is_not_either_file_alone` below: two files, the
second carrying the larger loads, and the envelope strictly above what file one gives.

The other three cells are EH4's boundaries, each solved in the direction that WEAKENS the
new behaviour rather than the one that flatters it:

* a tuple of ONE reproduces the single-file answer exactly -- not approximately;
* the EMPTY list is REFUSED, not defaulted and not silently skipped;
* the SAME file twice is refused rather than double-counted.

The second file is built by ROTATING the first, which the plan's own row allows ("tested
on synthetic or rotated npz data; the real multi-heading data waits on `export`").
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.run.config import ConfigError, load_config

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"
TRIMMED_STEPS = 40
"""FT2.4's trimmed window. Reproduces the governing `U` to six digits in seconds."""


def _write_npz(
    src: Path,
    dest: Path,
    *,
    scale: float,
    heading: float | None,
    froude_lambda: float | None = None,
) -> Path:
    """A copy of `src` with its reactions scaled and its recorded heading replaced.

    `scale` multiplies every `case*/lam`, which is what makes one file's loads larger than
    another's without inventing a load distribution: the same distribution, scaled, which
    is a rotation of the same sea state in the only sense this fixture needs.
    """
    raw = np.load(src, allow_pickle=False)
    out: dict[str, Any] = {}
    for key in raw.files:
        value = raw[key]
        if key.endswith(("/lam", "/times")):
            value = value[:TRIMMED_STEPS]
        if key.endswith("/lam"):
            value = value * scale
        # **THE SCALE LIVES IN THE NPZ, NOT IN THE SIDECAR, AND I MEASURED THAT RATHER
        # THAN ASSUMING IT.** My first version of the scale-disagreement cell retuned
        # `run/lambda` in the provenance JSON and the run exited 0 -- which looked like a
        # missing per-file check and was not: `exported_froude_lambda` reported `the npz`
        # as its source for both files, so the two genuinely agreed and the check was
        # right to pass. Editing the sidecar changes a value nothing reads here.
        if froude_lambda is not None and key == "froude_lambda":
            value = np.asarray(froude_lambda, dtype=value.dtype)
        out[key] = value
    np.savez(dest, **out)
    side = json.loads(src.with_suffix(".provenance.json").read_text(encoding="utf-8"))
    if heading is not None:
        for block in ("run", "wave", "basis"):
            if isinstance(side.get(block), dict) and "heading_deg" in side[block]:
                side[block]["heading_deg"] = heading
    dest.with_suffix(".provenance.json").write_text(json.dumps(side), encoding="utf-8")
    return dest


def _example_froude_lambda() -> float:
    """The scale the shipped example declares, read rather than restated.

    A test that hard-codes the number here goes stale the day the example changes, and the
    staleness is silent: the fixture would build a file at a scale the configuration no
    longer declares, and the cell would pass for the wrong reason.
    """
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    return float(data["floatsim"]["froude_lambda"])


def _config(tmp_path: Path, npz_entry: Any, **overrides: Any) -> tuple[Path, Path]:
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    data["load_cases"]["npz"] = npz_entry
    data["load_cases"].pop("headings", None)
    out = tmp_path / "out"
    data["outputs"]["directory"] = str(out)
    data["outputs"]["truss_sizing"] = False
    data["outputs"]["required_section"] = False
    for key, value in overrides.items():
        data["load_cases"][key] = value
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path, out


@pytest.fixture(scope="module")
def source_npz() -> Path:
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    return (EXAMPLE.parent / data["load_cases"]["npz"]).resolve()


def _rows(out: Path) -> list[list[str]]:
    import csv

    text = (out / "member_forces.csv").read_text(encoding="utf-8")
    body = [line for line in text.splitlines() if not line.startswith("#")]
    return list(csv.reader(body))


def test_the_union_is_not_either_file_alone(tmp_path, source_npz) -> None:
    """Two files, and the envelope is strictly above what the FIRST file gives.

    **THIS IS THE CELL AN `npz_files[0]` FAILS.** File two carries the same load
    distribution at four times the magnitude, so the union's worst force is file two's and
    a run that read only the first would publish file one's. The assertion is a strict
    inequality against a single-file run of the SAME first file, so it cannot be satisfied
    by reading either file alone.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "h000.npz", scale=1.0, heading=0.0)
    two = _write_npz(source_npz, local / "h045.npz", scale=4.0, heading=45.0)

    solo_dir = tmp_path / "solo"
    solo_dir.mkdir()
    solo_cfg, solo_out = _config(solo_dir, [str(one)])
    assert cli.main(["run", str(solo_cfg)]) == 0
    both_dir = tmp_path / "both"
    both_dir.mkdir()
    both_cfg, both_out = _config(both_dir, [str(one), str(two)])
    assert cli.main(["run", str(both_cfg)]) == 0

    def worst_axial(rows: list[list[str]]) -> float:
        return max(abs(float(r[5])) for r in rows[1:] if r[4].startswith("total_"))

    solo_worst = worst_axial(_rows(solo_out))
    both_worst = worst_axial(_rows(both_out))
    assert both_worst > solo_worst, (solo_worst, both_worst)

    # And every row says which file it came from, so the attribution is on the row.
    rows = _rows(both_out)
    head = rows[0]
    src = head.index("source")
    names = {r[src] for r in rows[1:]}
    assert names == {"h000.npz", "h045.npz", ""}, names
    # The empty one is the static rows and nothing else.
    assert all(r[4] == "static" for r in rows[1:] if r[src] == "")
    # Both headings reach the table, which is what "over the union" means.
    deg = head.index("heading_deg")
    assert {r[deg] for r in rows[1:]} == {"0", "45", ""}


def test_a_ONE_file_list_reproduces_the_SCALAR_declaration_exactly(tmp_path, source_npz) -> None:
    """EH4: a one-element list and a bare string give byte-identical artifacts.

    The direction that weakens the change: if the plural path diverged from the scalar one
    at a single file, every committed deliverable would be a different number tomorrow.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "only.npz", scale=1.0, heading=0.0)

    scalar_dir = tmp_path / "scalar"
    scalar_dir.mkdir()
    scalar_cfg, scalar_out = _config(scalar_dir, str(one))
    assert cli.main(["run", str(scalar_cfg)]) == 0

    list_dir = tmp_path / "listed"
    list_dir.mkdir()
    list_cfg, list_out = _config(list_dir, [str(one)])
    assert cli.main(["run", str(list_cfg)]) == 0

    for name in ("member_forces.csv", "utilisation.csv"):
        a = (scalar_out / name).read_text(encoding="utf-8")
        b = (list_out / name).read_text(encoding="utf-8")
        # The config NAME differs between the two directories, so the header line that
        # records it is excluded; every other line, including every number, is identical.
        a_lines = [line for line in a.splitlines() if not line.startswith("# config:")]
        b_lines = [line for line in b.splitlines() if not line.startswith("# config:")]
        assert a_lines == b_lines, name


def test_an_EMPTY_npz_list_is_REFUSED_and_not_defaulted(tmp_path) -> None:
    """EH4: the empty set is an error, not a run with no dynamic loads.

    `CLAUDE.md` is explicit that an empty parameter set is an error and not a skip. The
    failure this forbids is concrete: gravity alone, solved and published as an envelope.
    """
    path, out = _config(tmp_path, [])
    with pytest.raises(ConfigError) as caught:
        load_config(path)
    message = str(caught.value)
    assert "the list is EMPTY" in message, message
    assert "error and not a skip" in message, message
    assert not out.exists() or not list(out.glob("*"))


def test_the_SAME_file_twice_is_REFUSED_rather_than_double_counted(tmp_path, source_npz) -> None:
    """EH4: a repeat covers no extra heading and would be named twice in every artifact."""
    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "twice.npz", scale=1.0, heading=0.0)
    path, _out = _config(tmp_path, [str(one), str(one)])
    with pytest.raises(ConfigError) as caught:
        load_config(path)
    assert "already declared at index 0" in str(caught.value), str(caught.value)


def test_a_DECLARED_heading_NO_file_covers_is_refused_by_name(tmp_path, source_npz, capsys) -> None:
    """R809's rule over the union: refused only when NO declared file covers it.

    Both halves in one cell, because the interesting property is the pair: a heading the
    SECOND file covers must be ACCEPTED (which a first-file-only check would refuse), and
    a heading no file covers must be REFUSED.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "a000.npz", scale=1.0, heading=0.0)
    two = _write_npz(source_npz, local / "a045.npz", scale=1.0, heading=45.0)

    # 45 is covered by the SECOND file. A check that asked only the first would refuse it.
    ok_dir = tmp_path / "ok"
    ok_dir.mkdir()
    ok_cfg, _ = _config(ok_dir, [str(one), str(two)], headings=[0.0, 45.0])
    assert cli.main(["run", str(ok_cfg)]) == 0

    # 90 is covered by neither, and the refusal names what the files DO carry.
    bad_dir = tmp_path / "bad"
    bad_dir.mkdir()
    bad_cfg, bad_out = _config(bad_dir, [str(one), str(two)], headings=[0.0, 90.0])
    # **`cli.main` CATCHES `ConfigError` AND RETURNS 2**, with the message on stderr --
    # it does not propagate. My first version of this cell expected a raise and got
    # `DID NOT RAISE`, which is the CLI behaving as designed and the cell being wrong
    # about the boundary it was testing.
    assert cli.main(["run", str(bad_cfg)]) == 2
    message = capsys.readouterr().err
    assert "90" in message, message
    assert "a000.npz" in message and "a045.npz" in message, message
    assert not bad_out.exists() or not list(bad_out.glob("*"))


def test_a_SCALE_disagreement_in_the_SECOND_file_is_refused_naming_THAT_file(
    tmp_path, source_npz, capsys
) -> None:
    """The per-file hazard FT2.6 creates, and the one the recon called out first.

    Two files at different scales would mix forces at `lambda^3` with a locked moment at
    `lambda^4` against one deck. Asking only the first file is exactly the shape that
    would let it through, so the second file's disagreement must refuse and must NAME the
    second file.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    # The two scales are NAMED and the controls compare against the names rather than
    # against repeated literals: the tolerance guard reads a bare `== 25.0` as a threshold
    # and it is right to -- a number with no visible provenance inside a comparison is
    # one. The second value is also the one handed to the fixture, so the control cannot
    # drift from what was actually written.
    declared = _example_froude_lambda()
    disagreeing = declared / 2.0
    assert disagreeing != declared
    one = _write_npz(source_npz, local / "s000.npz", scale=1.0, heading=0.0)
    two = _write_npz(
        source_npz,
        local / "s045.npz",
        scale=1.0,
        heading=45.0,
        froude_lambda=disagreeing,
    )

    # The control that makes the assertion below mean something: the two files really do
    # disagree, as the reader this run uses reports them.
    from floatfea.run.pipeline import exported_froude_lambda

    assert exported_froude_lambda(one)[0] == declared
    assert exported_froude_lambda(two)[0] == disagreeing

    path, out = _config(tmp_path, [str(one), str(two)])
    assert cli.main(["run", str(path)]) == 2
    message = capsys.readouterr().err
    assert "s045.npz" in message, message
    assert "scale mismatch" in message, message
    assert not out.exists() or not list(out.glob("*"))


def test_the_REPORT_names_the_governing_HEADING_and_FILE(tmp_path, source_npz) -> None:
    """The plan's own requirement: "the report names the governing heading AND file".

    **AND IT IS LOOKED UP ON THE GOVERNING ROW, NOT TAKEN FROM THE FIRST FILE.** The
    second file carries the larger loads here, so it is the one that governs -- a sentence
    built from `npz_files[0]` would name the first file beside the second file's number,
    which is the exact shape FW1 put the provenance on `Row` to prevent.

    The one-file half is asserted too, in the direction that weakens the change: a single
    declared file must NOT gain the clause, because the file and heading are already in
    every artifact's header and appending them would move a committed deliverable's line
    for no new information.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "g000.npz", scale=1.0, heading=0.0)
    two = _write_npz(source_npz, local / "g045.npz", scale=4.0, heading=45.0)

    both_dir = tmp_path / "both"
    both_dir.mkdir()
    both_cfg, both_out = _config(both_dir, [str(one), str(two)])
    assert cli.main(["run", str(both_cfg)]) == 0
    report = (both_out / "report.md").read_text(encoding="utf-8")
    governing = [ln for ln in report.splitlines() if ln.startswith("**U = ")]
    assert len(governing) == 1, governing
    # The SECOND file governs, because it carries the larger loads.
    assert "from `g045.npz` at heading 45 deg" in governing[0], governing[0]
    assert "g000.npz" not in governing[0], governing[0]

    # And one file does not gain the clause at all.
    solo_dir = tmp_path / "solo"
    solo_dir.mkdir()
    solo_cfg, solo_out = _config(solo_dir, [str(one)])
    assert cli.main(["run", str(solo_cfg)]) == 0
    solo_report = (solo_out / "report.md").read_text(encoding="utf-8")
    solo_governing = [ln for ln in solo_report.splitlines() if ln.startswith("**U = ")]
    assert len(solo_governing) == 1, solo_governing
    assert "from `" not in solo_governing[0], solo_governing[0]
