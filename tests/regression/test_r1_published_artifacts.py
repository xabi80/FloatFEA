"""The PUBLISHED artifacts are read as files, not as a stub (R816, FO2).

**WHY THIS FILE EXISTS.** Verdict 2 measured that no test in `tests/` touched
`results/R1/example/`, `_write_report`, `_write_member_forces`, `_write_utilisations` or
`_cmd_run`. The header test asserted `_header_lines()` on a hand-built `RunResult`, which
checks the function and not the file: everything between that function and the bytes on
disk -- the `#` prefixing, the comma stripping, the writer's column list, the report's
section order -- was unexercised.

That is not hypothetical. R808 was a duplicated body prefix IN THE PUBLISHED REPORT that
survived a round because I verified the console line and not the file, and asserted the
fix in a commit message. A test over `_header_lines` would not have caught it either.

**THE ARTIFACTS ARE COMMITTED, SO THIS READS THEM RATHER THAN REGENERATING THEM.** A full
run is 67 s and `test_r1_example_golden.py` already pays it to check the NUMBERS. What is
checked here is the published FORM.

**AND THE CLAIM THAT USED TO FOLLOW THAT SENTENCE WAS FALSE, WHICH R831 MEASURED.** It read
"reading the committed files also catches a regeneration that was never committed -- which a
test that regenerates cannot". It did not: the caveat gate's needle was the MARKER, and
`EX3` appears in the stale sentence as well as the repaired one, so all three deliverables
published the pre-R829 wording with 33 of 33 cases green. A needle that matches both sides
of the change it is meant to detect catches nothing. The needle is now the caveat TEXT, out
of `floatfea.cli.TABLE_CAVEATS`, so a reworded caveat reddens until the files are
regenerated.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from floatfea.cli import TABLE_CAVEATS

ROOT = Path(__file__).resolve().parents[2]
PUBLISHED = ROOT / "results" / "R1" / "example"
REPORT = PUBLISHED / "report.md"
FORCES = PUBLISHED / "member_forces.csv"
UTILISATION = PUBLISHED / "utilisation.csv"

# **THE NEEDLE IS THE CAVEAT TEXT, NOT ITS MARKER (R831).** This was
# `CAVEAT_MARKERS = ("R739", "R740", ... "R743")` -- eleven markers for nine caveats,
# `EX3/R724` and `R741/R742` each naming two findings. The marker is present in a REWORDED
# caveat too, so when R829's repair changed `TABLE_CAVEATS[4]` in `cli.py` and the files
# were not regenerated afterwards, all 33 (file, marker) cases stayed green while all three
# deliverables published the sentence R829 had named false.
#
# Reading the source of truth makes the comparison one that can fail.


def _normalised(text: str) -> str:
    """`_write_header` writes `line.replace(",", ";")` so a CSV reader is safe.

    Both sides are normalised the same way, so one needle serves the markdown report and
    the two CSVs without a per-file branch that could pass for the wrong reason.
    """
    return text.replace(",", ";")


ARTIFACTS = (REPORT, FORCES, UTILISATION)


@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_the_artifact_was_published_at_all(path: Path) -> None:
    """The file exists and is not empty. Everything below is vacuous without it."""
    assert path.is_file(), (
        f"{path.relative_to(ROOT)} is not committed. `floatfea run "
        f"examples/platform12_placeholder.yaml` produces it, and `results/` is tracked."
    )
    assert path.stat().st_size > 0, path


@pytest.mark.parametrize("index", range(len(TABLE_CAVEATS)), ids=lambda i: f"caveat{i}")
@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_every_caveat_reaches_EVERY_published_artifact(path: Path, index: int) -> None:
    """All nine caveats, VERBATIM, in all three files, one case per (file, caveat).

    **R815 IS WHY THIS IS PARAMETRISED THIS WAY.** The previous gate asserted four markers
    in one `for` loop over a single stub, and the other five grepped `0 0 0` across the
    report and both CSVs while it passed. One case per pair means a missing caveat names
    both the file and the caveat.

    **R831 IS WHY THE NEEDLE IS THE TEXT.** With the marker as the needle this was green on
    three deliverables publishing the pre-R829 wording, because `EX3` is in both wordings.
    Measured at that commit:

        results/R1/example/report.md          caveats: 9   NOT PRESENT verbatim: [4]
        results/R1/example/member_forces.csv  caveats: 9   NOT PRESENT verbatim: [4]
        results/R1/example/utilisation.csv    caveats: 9   NOT PRESENT verbatim: [4]

    The counter is a rewording: change one element of `TABLE_CAVEATS` and leave the files
    alone, and this reddens on three cases rather than staying green on 33.
    """
    caveat = TABLE_CAVEATS[index]
    text = _normalised(path.read_text(encoding="utf-8", errors="replace"))
    assert _normalised(caveat) in text, (
        f"{path.name} does not carry caveat {index} VERBATIM. A caveat reworded in "
        f"`floatfea/cli.py` and not regenerated into the files is R831, and the fix is to "
        f"re-run `floatfea run` AFTER the last edit to `cli.py` (CP3). Missing: "
        f"{caveat[:160]}"
    )


@pytest.mark.parametrize("path", (FORCES, UTILISATION), ids=lambda p: p.name)
def test_the_csv_header_is_COMMENTED_and_the_data_is_parseable(path: Path) -> None:
    """The header must be `#` lines, and the rows must still read as a CSV.

    A header written without the comment prefix would make every consumer's first data row
    a label, and `csv.DictReader` would take it as the field names.
    """
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    head = [line for line in lines if line.startswith("#")]
    # C23: NO MAGIC COUNT. This read `len(head) >= 20` against 40 actual lines, so it
    # would have passed with half the header missing -- a floor with 2x slack is not a
    # check, and "20" was a number nothing derived.
    #
    # Every PROVENANCE KEY instead, taken from the schema rather than counted: the key set
    # comes from `RunConfig.provenance()`, so adding a provenance field extends this check
    # automatically and dropping one from the writer fails it by name.
    from floatfea.run.config import load_config

    expected_keys = sorted(
        load_config(ROOT / "examples" / "platform12_placeholder.yaml").provenance()
    )
    blob = "\n".join(head)
    missing = [key for key in expected_keys if key not in blob]
    assert not missing, (
        f"{path.name}'s header is missing provenance key(s) {missing}. The header is the "
        f"label, the provenance, the build's assumptions, its findings and the column "
        f"caveats; a reader who cannot see what was configured cannot audit the run "
        f"(R806)."
    )
    rows = list(csv.DictReader([line for line in lines if not line.startswith("#")]))
    assert rows, f"{path.name} has a header and no data rows"
    for field in ("body", "member", "station", "basis"):
        assert field in rows[0], (field, sorted(rows[0]))


def test_the_published_report_does_not_DOUBLE_PREFIX_the_member() -> None:
    """R808, as a property of the FILE this time.

    The member label already carries its body, so `platform:platform:hub4_arm` is the
    defect. It survived a round because the fix was claimed in a commit message and
    verified on the console line only.
    """
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    for body in ("platform", "hub1", "hub2", "hub3", "hub4"):
        doubled = f"{body}:{body}:"
        assert doubled not in text, (
            f"{REPORT.name} publishes `{doubled}...`: the member label already carries its "
            f"body, so prefixing it again doubles it (R808)."
        )


def test_the_published_report_names_the_governing_station_in_full() -> None:
    """The governing row is NAMED, never summarised (`CLAUDE.md` forbids averaging).

    Member, station, period and clause, so an outlier cannot hide in a statistic.
    """
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "## The governing utilisation" in text, text[:200]
    line = next(line for line in text.splitlines() if line.startswith("**U = "))
    for part in ("ROOT", "T_full", "basis", "governing clause"):
        assert part in line, (part, line)


def test_the_published_report_carries_the_mass_table_PER_BODY() -> None:
    """Five rows, one per body, with the residual formed from its own terms (G4.1)."""
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "## Mass, per body" in text
    for body in ("platform", "hub1", "hub2", "hub3", "hub4"):
        assert f"| `{body}` |" in text, f"the mass table has no row for {body}"


def test_the_published_report_carries_the_BUILDS_OWN_findings() -> None:
    """R807: nine findings were computed and discarded. They are in the file now."""
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "## Findings the build raised, per body" in text
    assert "MEASUREMENT" in text, (
        "five of the nine findings say the body is a MEASUREMENT and not one to ship; that "
        "is the half a reader of a published artifact most needs."
    )
    assert "11433" in text, "the equivalent densities must be reported (DZ5 / ER1(e))"


def test_a_NON_STUDY_run_carries_no_STUDY_label_anywhere() -> None:
    """The control for the study label: the shipped example is not a study.

    Without this, a generator that stamped every run would pass the study test and nobody
    would notice that the label had stopped meaning anything.
    """
    for path in ARTIFACTS:
        text = path.read_text(encoding="utf-8", errors="replace")
        assert "STUDY -- NOT FOR DESIGN" not in text, (
            f"{path.name} carries the study label and the example declares "
            f"`study_only: false`. A label on everything distinguishes nothing."
        )


@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_R817_every_artifact_states_the_HEADING_and_the_WAVE_HEIGHT(path: Path) -> None:
    """The two facts the caveats are ABOUT (R817).

    The EX3/R724 caveat is about the heading and the EZ2/FA0 caveat is about the wave
    height's associated-period band, and neither value appeared in any artifact. The
    committed deliverables these replaced said "all cases are heading 0 degrees" and
    "H = 24.2 m" outright; the reworded caveat said "every case carries the heading its
    load cases declare", which in a file declaring no heading says nothing.

    Asserted per artifact, because carrying it in the report and not in the CSVs is the
    same defect one file over.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    assert "heading" in text.lower(), f"{path.name} does not state a heading"
    assert "0.0 deg" in text or "heading 0.0" in text, (
        f"{path.name} states no heading VALUE. The caveat about heading dependence is "
        f"unreadable without it."
    )
    assert "24.2" in text, (
        f"{path.name} states no wave height. EZ2's associated-period band is derived from "
        f"H, so a reader cannot check which periods may govern without it."
    )


def test_R818_the_report_states_the_SENSITIVITY_OPERATING_POINTS() -> None:
    """Two published columns had no operating point anywhere (R818).

    `utilisation_K_sens` and `utilisation_Cm_sens` are published per station. Run at a
    configuration the diff did not choose -- `K_sensitivity` equal to `K`,
    `Cm_sensitivity = 0.1` -- the two columns collapse onto the base on 32 of 32 rows and
    the header differed from the shipped run by ONE line, the config filename. A column
    whose operating point is unpublished cannot be read, and R743's caveat delegates the
    Cm direction to exactly that column.
    """
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    assert "K_sensitivity" in text, "the report states no K sensitivity operating point"
    assert "Cm_sensitivity" in text, "the report states no Cm sensitivity operating point"


def test_R819_FQ0_the_artifacts_state_the_FLAT_D_over_t_ceiling() -> None:
    """The clause limits as FQ0 rules them, in all three artifacts.

    **THIS GATE PINNED THE WRONG NUMBER AND IS THE REASON TO DISTRUST A GATE WRITTEN
    BESIDE ITS OWN REPAIR.** R819 said the artifacts misstated two things, and I corrected
    them to `0.75*Fy IS compact` (right) and `300000/Fy[MPa] = 845.1` (wrong), then wrote
    this test to assert the wrong one. The reviewer's bisection found the code's first
    refusal at `734.3`, which matched neither, and FQ0 then ruled the ceiling is a FLAT
    `300` and named `300000/Fy` as FB1's own error.

    So three figures were published for one limit -- `845.1`, `734.3`, `300` -- and the
    gate asserted the first. What it checks now is the ruling, and it checks the CODE's
    boundary too, so a caveat and a clause cannot drift apart again.
    """
    from floatfea.basis import FY_S355
    from floatfea.checks.api_wsd import BENDING_THIRD_BRANCH_MAX_D_OVER_T, allowable_bending

    for path in ARTIFACTS:
        text = path.read_text(encoding="utf-8", errors="replace")
        assert "D/t <= 300" in text, f"{path.name} does not state FQ0's flat D/t <= 300 ceiling."
        assert (
            "300000/Fy" not in text
        ), f"{path.name} still carries FB1's grade-dependent reading, which FQ0 overruled."
        assert "845.1" not in text, f"{path.name} still carries the 845.1 figure."
        assert (
            "first reduction below the compact branch" not in text
        ), f"{path.name} still calls 0.75*Fy a reduction below compact; it IS compact."

    # AND THE CODE AGREES WITH THE CAVEAT, at the boundary and on both sides of it.
    # not-a-tolerance: FQ0's flat clause ceiling. API RP 2A-WSD section 3.2.3's third
    # range ends at a D/t of 300 in the standard's own text, so this pins a CLAUSE
    # CONSTANT against the caveat the artifacts publish -- not a comparison epsilon.
    assert BENDING_THIRD_BRANCH_MAX_D_OVER_T == 300.0  # not-a-tolerance: a clause constant
    allowable_bending(d_outer=2.5, wall=2.5 / 300.0, fy=FY_S355)  # must not raise
    with pytest.raises(ValueError, match="the flat upper limit"):
        allowable_bending(d_outer=2.5, wall=2.5 / 300.01, fy=FY_S355)
    # FLAT: the ceiling does not move with grade, which is the whole content of FQ0.
    for fy in (235e6, 355e6, 460e6, 690e6):
        with pytest.raises(ValueError, match="the flat upper limit"):
            allowable_bending(d_outer=2.5, wall=2.5 / 300.01, fy=fy)
