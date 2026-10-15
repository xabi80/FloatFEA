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
checked here is the published FORM, and reading the committed files also catches a
regeneration that was never committed -- which a test that regenerates cannot.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PUBLISHED = ROOT / "results" / "R1" / "example"
REPORT = PUBLISHED / "report.md"
FORCES = PUBLISHED / "member_forces.csv"
UTILISATION = PUBLISHED / "utilisation.csv"

# The nine caveats FO2 requires, by the marker each one is identified by in the tree.
# `EX3/R724` and `R741/R742` are single caveats naming two findings each, which is how the
# committed deliverables write them.
CAVEAT_MARKERS = ("R739", "R740", "FA3", "EZ2", "EX3", "R724", "FA0", "FA1", "R741", "R742", "R743")

ARTIFACTS = (REPORT, FORCES, UTILISATION)


@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_the_artifact_was_published_at_all(path: Path) -> None:
    """The file exists and is not empty. Everything below is vacuous without it."""
    assert path.is_file(), (
        f"{path.relative_to(ROOT)} is not committed. `floatfea run "
        f"examples/platform12_placeholder.yaml` produces it, and `results/` is tracked."
    )
    assert path.stat().st_size > 0, path


@pytest.mark.parametrize("marker", CAVEAT_MARKERS)
@pytest.mark.parametrize("path", ARTIFACTS, ids=lambda p: p.name)
def test_every_caveat_reaches_EVERY_published_artifact(path: Path, marker: str) -> None:
    """All nine caveats, in all three files, one case per (file, marker).

    **R815 IS WHY THIS IS PARAMETRISED THIS WAY.** The previous gate asserted four markers
    in one `for` loop over a single stub, and the other five grepped `0 0 0` across the
    report and both CSVs while it passed. One case per pair means a missing caveat names
    both the file and the marker.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    assert marker in text, (
        f"{path.name} does not mention {marker}. The caveats say what the COLUMNS mean; a "
        f"reader without them can take an envelope bound for a stress (R740) or read the "
        f"axial column with the wrong sign (R739)."
    )


@pytest.mark.parametrize("path", (FORCES, UTILISATION), ids=lambda p: p.name)
def test_the_csv_header_is_COMMENTED_and_the_data_is_parseable(path: Path) -> None:
    """The header must be `#` lines, and the rows must still read as a CSV.

    A header written without the comment prefix would make every consumer's first data row
    a label, and `csv.DictReader` would take it as the field names.
    """
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    head = [line for line in lines if line.startswith("#")]
    assert len(head) >= 20, (
        f"{path.name} carries {len(head)} comment lines. The header is the label, the "
        f"provenance, the build's assumptions, its findings and the column caveats; a "
        f"short header means one of those is missing (R806)."
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
