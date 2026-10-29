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
    height_full: float | None = None,
    sidecar: bool = True,
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
    if not sidecar:
        # **NO PROVENANCE SIDECAR AT ALL, WHICH FL1(a) ADMITS.** Such a file records no
        # heading and no height, so it cannot be screened -- and R1095 is what the report
        # did with that beside a file that could be.
        return dest
    side = json.loads(src.with_suffix(".provenance.json").read_text(encoding="utf-8"))
    for block in ("run", "wave", "basis"):
        if not isinstance(side.get(block), dict):
            continue
        if heading is not None and "heading_deg" in side[block]:
            side[block]["heading_deg"] = heading
        if height_full is not None and "wave_height_full_m" in side[block]:
            # The MODEL height moves with it, from the sidecar's own declared lambda --
            # not from a constant here, which would be R895 written into a fixture.
            lam = float(side[block]["lambda"])
            side[block]["wave_height_full_m"] = height_full
            side[block]["wave_height_model_m"] = height_full / lam
    dest.with_suffix(".provenance.json").write_text(json.dumps(side), encoding="utf-8")
    return dest


def _section(text: str, heading: str) -> str:
    """One `## ` section of a report, whole.

    **THE ASSERTION DOMAIN IS THE POINT (R1093 to R1096).** Every cell in this file read
    `report.md` at the `**U = ` line and nothing else, and the four blocking findings of
    verdict 40 were all in the ELEVEN OTHER sections -- a basis section stating the first
    file's heading, a band sentence stating the first file's band over every file's rows,
    a per-case table silently omitting an unscreened file, and two counts multiplied by
    the number of declared files. A green suite was furthest from all four.
    """
    lines = text.splitlines()
    starts = [k for k, ln in enumerate(lines) if ln.startswith(f"## {heading}")]
    assert len(starts) == 1, f"{heading}: {starts}"
    i = starts[0]
    j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
    return chr(10).join(lines[i:j]).rstrip()


def _utilisation_rows(out: Path) -> list[dict[str, str]]:
    import csv

    text = (out / "utilisation.csv").read_text(encoding="utf-8")
    body = [ln for ln in text.splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(body))


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


def test_R1093_the_BASIS_SECTION_states_EVERY_declared_file_and_not_the_FIRST(
    tmp_path, source_npz
) -> None:
    """`report.md`'s basis section read WHOLE, at two files recording different headings.

    **THE SECTION PUBLISHED FILE ONE'S HEADING AS THE RUN'S, IN A DOCUMENT THAT NAMED
    FILE TWO AS GOVERNING TWENTY LINES BELOW (R1093).** `* **heading** -- 0.0 deg` under
    "the wave basis these loads were exported at", with `from `p045.npz` at heading 45
    deg` as the governing row. One document contradicting itself, and the half a reader
    sizes steel against was the wrong half.

    The assertion is on BOTH names and on the agreement between the two sections, not on
    a needle: a repair that named the second file and kept the first file's heading
    against it would pass a name check and fail this.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "p000.npz", scale=1.0, heading=0.0)
    two = _write_npz(source_npz, local / "p045.npz", scale=4.0, heading=45.0)
    cfg, out = _config(tmp_path, [str(one), str(two)])
    assert cli.main(["run", str(cfg)]) == 0

    text = (out / "report.md").read_text(encoding="utf-8")
    basis = _section(text, "The wave basis")
    assert "p000.npz" in basis, basis
    assert "p045.npz" in basis, basis
    # Each file's own heading sits inside that file's own block, and nowhere else.
    blocks = basis.split("### ")
    by_name = {b.splitlines()[0].strip("`"): b for b in blocks[1:]}
    assert set(by_name) == {"p000.npz", "p045.npz"}, sorted(by_name)
    assert "0.0 deg" in by_name["p000.npz"], by_name["p000.npz"]
    assert "45.0 deg" in by_name["p045.npz"], by_name["p045.npz"]
    assert "45.0 deg" not in by_name["p000.npz"], by_name["p000.npz"]
    assert "0.0 deg" not in by_name["p045.npz"], by_name["p045.npz"]

    # AND THE GOVERNING SENTENCE AGREES WITH THE BLOCK THAT NAMES ITS FILE.
    governing = next(ln for ln in text.splitlines() if ln.startswith("**U = "))
    assert "from `p045.npz` at heading 45 deg" in governing, governing
    assert "45.0 deg" in by_name["p045.npz"], by_name["p045.npz"]

    # **AND THE PUBLISHED RULE FOR READING AN EMPTY `source` IS TRUE OF EVERY ROW.**
    # `cli.py` tells a reader that an empty `source` means gravity, which is the sentence
    # a defaulted `Row.source` would have falsified for a dynamic row (R1102). Asserted
    # over the deliverable rather than inside a fixture.
    rows = _rows(out)
    head = rows[0]
    src, bas = head.index("source"), head.index("basis")
    pairs = [(r[src] == "", r[bas] == "static") for r in rows[1:]]
    assert all(empty == static for empty, static in pairs), [
        r for r in rows[1:] if (r[src] == "") != (r[bas] == "static")
    ][:3]
    assert any(static for _e, static in pairs), "no static row reached the check"
    assert any(not static for _e, static in pairs), "no dynamic row reached the check"


def test_R1094_EVERY_band_row_is_DERIVABLE_from_the_band_printed_above_it(
    tmp_path, source_npz
) -> None:
    """Two files recording DIFFERENT heights, and `outside by` checked against its band.

    **ONE STATED BAND OVER TWELVE ROWS FROM TWO HEIGHTS (R1094).** The section said
    `12.542 .. 16.316 s` and a row said `outside by -0.654`, which that band gives as
    `-0.042`. A reader who checks the arithmetic -- the only reason the column exists --
    concludes the table is wrong rather than that the band is one of two.

    This does not look for a sentence. It re-derives every row's margin from the band
    printed in that row's own block, so a repair that prints two bands and puts the rows
    under the wrong one fails.
    """
    import re

    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "r242.npz", scale=1.0, heading=0.0, height_full=24.2)
    two = _write_npz(source_npz, local / "r266.npz", scale=2.0, heading=45.0, height_full=26.62)
    cfg, out = _config(tmp_path, [str(one), str(two)])
    assert cli.main(["run", str(cfg)]) == 0

    section = _section((out / "report.md").read_text(encoding="utf-8"), "Sea-state")
    bands = re.findall(r"`([0-9.]+) \.\. ([0-9.]+) s`", section)
    assert len(bands) == 2, section
    assert bands[0] != bands[1], bands

    blocks = section.split("### ")[1:]
    assert len(blocks) == 2, section
    checked = 0
    for block in blocks:
        low, high = (float(v) for v in re.findall(r"`([0-9.]+) \.\. ([0-9.]+) s`", block)[0])
        for row in re.findall(r"^\| ([0-9.]+) \|.*\| ([-+0-9.]+|—) \|", block, re.M):
            period, margin = float(row[0]), row[1]
            # **NO EPSILON HERE, AND THE GUARD IS WHY.** My first version compared
            # `abs(got - want) < 5e-4`, which is a comparison tolerance in a test and
            # `CLAUDE.md` forbids one outright --
            # `test_no_undeclared_tolerance_reaches_a_comparison` caught it, on the sixth
            # consecutive commit where that guard has caught a literal in a repair rather
            # than in original work. The published cell is a STRING the report formats
            # `{:+.3f}` from the band printed above it, so the exact question is whether
            # that string is the one THIS block's own band gives.
            want = (
                "—"
                if low <= period <= high
                else f"{period - low:+.3f}" if period < low else f"{period - high:+.3f}"
            )
            assert margin == want, (block, period, margin, want, low, high)
            checked += 1
    assert checked == 12, checked


def test_R1095_a_file_that_was_NOT_SCREENED_is_NAMED_beside_one_that_was(
    tmp_path, source_npz
) -> None:
    """The mixed pair: one file with a sidecar, one without, carrying the larger loads.

    **R1007's MEASURED FAILURE, REACHABLE AGAIN THROUGH A NEW DOOR (R1095).** A file with
    no recorded height screens to nothing. Concatenated, it vanished -- so beside a
    screened file the aggregate was non-empty, the "the screen was NOT performed"
    disclosure the single-file path owns was skipped, the six-row table read as complete,
    and the governing utilisation came from the file the table never mentioned. R1007
    measured that same skip at 63% high on the governing utilisation at exit 0.

    The control is the same unscreened file ALONE, which must still make the disclosure
    the pair lost. One variable: whether a second, screened file is declared beside it.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    screened = _write_npz(source_npz, local / "q000.npz", scale=1.0, heading=0.0)
    bare = _write_npz(source_npz, local / "qNONE.npz", scale=4.0, heading=None, sidecar=False)

    pair_dir = tmp_path / "pair"
    pair_dir.mkdir()
    cfg, out = _config(pair_dir, [str(screened), str(bare)])
    assert cli.main(["run", str(cfg)]) == 0
    text = (out / "report.md").read_text(encoding="utf-8")
    section = _section(text, "Sea-state")
    assert "qNONE.npz" in section, section
    assert "was NOT screened" in section, section
    # The governing row IS the unscreened file's, which is what makes the omission matter.
    governing = next(ln for ln in text.splitlines() if ln.startswith("**U = "))
    assert "qNONE.npz" in governing, governing

    # THE CONTROL: the same file alone still says the screen was not performed.
    solo_dir = tmp_path / "solo"
    solo_dir.mkdir()
    solo_cfg, solo_out = _config(solo_dir, [str(bare)])
    assert cli.main(["run", str(solo_cfg)]) == 0
    solo = _section((solo_out / "report.md").read_text(encoding="utf-8"), "Sea-state")
    assert "the screen was NOT performed" in solo, solo
    assert "###" not in solo, solo


def test_R1096_the_CHECKED_STATION_counts_are_over_DISTINCT_stations(tmp_path, source_npz) -> None:
    """`Checked stations: 64. Over unity: 16.` on a platform with 32 stations.

    **THE COUNTS MULTIPLIED BY THE NUMBER OF DECLARED FILES (R1096).** The records are
    one per (station, FILE) since FT2.6 and the two published counts were written when
    they were one per station. The over-unity count is the number a reader acts on, and
    counting a station twice because it fails under two headings is a wrong census of the
    failures rather than conservatism.

    Both counts are re-derived from `utilisation.csv`, so this cannot be satisfied by a
    sentence: the published numbers must equal the distinct counts in the deliverable.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "c000.npz", scale=1.0, heading=0.0)
    two = _write_npz(source_npz, local / "c045.npz", scale=4.0, heading=45.0)
    cfg, out = _config(tmp_path, [str(one), str(two)])
    assert cli.main(["run", str(cfg)]) == 0

    rows = _utilisation_rows(out)
    key = ("body", "member", "station")
    stations = {tuple(r[k] for k in key) for r in rows}
    over = {tuple(r[k] for k in key) for r in rows if float(r["utilisation"]) > 1.0}
    assert len(rows) == 2 * len(stations), (len(rows), len(stations))

    text = (out / "report.md").read_text(encoding="utf-8")
    line = next(ln for ln in text.splitlines() if ln.startswith("Checked stations:"))
    assert f"Checked stations: {len(stations)}." in line, (line, len(stations))
    assert f"Over unity: {len(over)}." in line, (line, len(over))
    # And the station-case count is stated rather than dropped, so a reader comparing
    # the report with the CSV's row count does not have to discover the difference.
    assert f"{len(rows)} station-cases over 2 declared files" in line, line


def test_R1099_the_UTILISATION_CSV_rows_are_UNIQUELY_KEYED_at_two_files(
    tmp_path, source_npz
) -> None:
    """The two provenance columns, appended, and the duplicate keys they resolve.

    **THE UNION MADE THIS DELIVERABLE AMBIGUOUS (R1099).** Without them every station
    appears once per declared file under an IDENTICAL published key with a DIFFERENT
    utilisation -- `U = 0.7115` and `0.819965` under one key -- and a code check is read
    from this file. FW1's conditions are asserted in the direction that weakens the
    change: the two names are LAST, so no pre-existing column moved.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "u000.npz", scale=1.0, heading=0.0)
    two = _write_npz(source_npz, local / "u045.npz", scale=4.0, heading=45.0)
    cfg, out = _config(tmp_path, [str(one), str(two)])
    assert cli.main(["run", str(cfg)]) == 0

    rows = _utilisation_rows(out)
    assert list(rows[0])[-2:] == ["source", "heading_deg"], list(rows[0])
    keys = {tuple(r[k] for k in list(rows[0])[:5]) for r in rows}
    assert len(keys) * 2 == len(rows), (len(keys), len(rows))
    with_source = {tuple(r[k] for k in [*list(rows[0])[:5], "source"]) for r in rows}
    assert len(with_source) == len(rows), (len(with_source), len(rows))
    assert {r["source"] for r in rows} == {"u000.npz", "u045.npz"}
    assert {r["heading_deg"] for r in rows} == {"0", "45"}
    # No utilisation row is ever gravity, so none may carry an empty provenance.
    assert all(r["source"] and r["heading_deg"] for r in rows), rows[0]


def test_R1098_a_utilisation_key_the_COLUMN_LIST_does_not_name_is_REFUSED(
    tmp_path, source_npz
) -> None:
    """A new key in the record is refused, not silently published and not dropped.

    **"THE FIELDNAMES ARE STATED EXPLICITLY" WAS FALSE (R1098).** It was a denylist over
    an inferred list -- two names denied, every other key admitted -- so the property the
    comment claimed, that a future column is an edit someone makes on purpose, was
    precisely the one it did not have. Measured then: `body,member,station,utilisation,
    A_BRAND_NEW_FIELD`.
    """
    from floatfea import cli
    from floatfea.run.pipeline import RunResult

    # **A REAL `RunResult` AND THE REAL WRITER, because the CALLER is what FT2 asks to be
    # held.** My first version of this cell passed a stub carrying only `utilisations` and
    # `wave_bases`, and `_write_header` -- which every artifact goes through -- raised
    # `AttributeError: '_R' object has no attribute 'config'`. A stub thin enough to pass
    # would have been a stub that does not reach the writer under test.
    cfg_path, _ = _config(tmp_path, str(source_npz))
    built = type("_B", (), {"label": "", "assumptions": (), "bodies": ()})()
    record: dict[str, Any] = {name: "x" for name in cli.UTILISATION_COLUMNS}
    record["utilisation"] = 0.5
    record["source"] = "a.npz"
    record["heading_deg"] = 0.0

    def _result(rows: list[dict[str, Any]]) -> RunResult:
        return RunResult(
            config=load_config(cfg_path),
            built=built,
            rows=[],
            utilisations=rows,
            mass=(),
            timings={},
            wave_bases=(("a.npz", {}),),
        )

    # The named set writes, with the two provenance columns last.
    clean = tmp_path / "clean.csv"
    cli._write_utilisations(clean, _result([dict(record)]))
    header = next(
        ln for ln in clean.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")
    )
    assert header.endswith(",source,heading_deg"), header
    assert header.split(",")[: len(cli.UTILISATION_COLUMNS)] == list(cli.UTILISATION_COLUMNS)

    # And one extra key is a refusal naming it, with no file written.
    record["A_BRAND_NEW_FIELD"] = 1.0
    with pytest.raises(ConfigError) as caught:
        cli._write_utilisations(tmp_path / "dirty.csv", _result([dict(record)]))
    assert "A_BRAND_NEW_FIELD" in str(caught.value), str(caught.value)
    assert not (tmp_path / "dirty.csv").exists()


def test_R1100_the_WRAP_VALUE_360_is_accepted_at_ONE_file_AND_at_TWO(
    tmp_path, source_npz, capsys
) -> None:
    """`headings: [360.0]` against exports at 0, at one declared file and at two.

    **THE SAME DECLARATION FLIPPED FROM ACCEPTED TO REFUSED WHEN A SECOND FILE WAS ADDED
    (R1100).** The one-file path asks `uncovered_headings`, which is modulo 360 and whose
    own comment says so; the multi-file path asked a plain `==`. 360 is inside `HEADING`'s
    declared domain and names the direction 0 names, so the modulo is the correct rule and
    the second implementation was the defect.

    Both directions. The declared heading no file covers must STILL be refused at two
    files, which is the half a modulo could have broken.
    """
    from floatfea import cli

    local = tmp_path / "data"
    local.mkdir()
    one = _write_npz(source_npz, local / "w000.npz", scale=1.0, heading=0.0)
    two = _write_npz(source_npz, local / "w045.npz", scale=4.0, heading=45.0)

    solo_dir = tmp_path / "solo"
    solo_dir.mkdir()
    solo_cfg, _ = _config(solo_dir, [str(one)], headings=[360.0])
    assert cli.main(["run", str(solo_cfg)]) == 0

    both_dir = tmp_path / "both"
    both_dir.mkdir()
    both_cfg, _ = _config(both_dir, [str(one), str(two)], headings=[360.0])
    assert cli.main(["run", str(both_cfg)]) == 0

    # AND THE OTHER DIRECTION: a heading genuinely uncovered is still refused at two.
    bad_dir = tmp_path / "bad"
    bad_dir.mkdir()
    bad_cfg, bad_out = _config(bad_dir, [str(one), str(two)], headings=[90.0])
    # `cli.main` CATCHES `ConfigError` and returns 2, with the message on stderr.
    assert cli.main(["run", str(bad_cfg)]) == 2
    message = capsys.readouterr().err
    assert "90" in message, message
    assert not bad_out.exists() or not list(bad_out.glob("*"))


def test_R1101_the_UNRECORDED_clause_agrees_in_BOTH_numbers(tmp_path, source_npz) -> None:
    """`records no heading at all` for one file, `record` for two.

    **THE FOURTH INSTANCE OF THIS CLASS IN THIS STEP (L36, R1085, R1089, R1101).** One
    branch of an agreement pair, never emitted by any cell. Both are emitted here, and
    the branch is reached through the real refusal rather than by calling the helper.
    """
    from floatfea.run.config import ConfigError
    from floatfea.run.pipeline import refuse_headings_no_file_covers

    local = tmp_path / "data"
    local.mkdir()
    has = _write_npz(source_npz, local / "has.npz", scale=1.0, heading=0.0)
    bare_a = local / "barea.npz"
    bare_b = local / "bareb.npz"

    from floatfea.run.pipeline import exported_wave_basis

    basis = exported_wave_basis(has)
    with pytest.raises(ConfigError) as one:
        refuse_headings_no_file_covers((45.0,), [(has, basis), (bare_a, {})])
    assert "barea.npz records no heading at all" in str(one.value), str(one.value)

    with pytest.raises(ConfigError) as two:
        refuse_headings_no_file_covers((45.0,), [(has, basis), (bare_a, {}), (bare_b, {})])
    assert "barea.npz, bareb.npz record no heading at all" in str(two.value), str(two.value)


def test_R1102_the_PROVENANCE_fields_carry_NO_DEFAULT() -> None:
    """`Row.source` and `Row.heading_deg` have no default, so an omission will not compile.

    **THE APPEND WAS THE DANGEROUS HALF AND IT WAS HONOURED; THIS IS THE CHEAP HALF THAT
    WAS NOT (R1102).** With defaults, all four `Row(` constructions stayed legal and
    `mypy` named none of them, so a FUTURE construction that forgot the provenance would
    publish a dynamic row with an empty `source` -- and `cli.py`'s published rule says an
    empty `source` means gravity. The row would be attributed to the static case.

    The `static` construction passes the empty string and the `nan` explicitly, which is a
    statement about those rows rather than a default nobody chose.
    """
    import dataclasses

    from floatfea.post.forces_table import Row

    fields = {f.name: f for f in dataclasses.fields(Row)}
    for name in ("source", "heading_deg"):
        assert fields[name].default is dataclasses.MISSING, name
        assert fields[name].default_factory is dataclasses.MISSING, name
    # And they are LAST, so nothing positional shifted when they were added.
    assert [f.name for f in dataclasses.fields(Row)][-2:] == ["source", "heading_deg"]
