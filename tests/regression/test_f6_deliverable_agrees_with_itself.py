"""C70: the published code-check table agrees with its own data.

**NOTHING UNDER `tests/` READ EITHER DELIVERABLE, AND THREE PUBLISHED SENTENCES HAVE NOW
BEEN WRONG.** R739's clause attribution, R747's four summary sentences, and R752's
form-governing count were each a statement in `docs/F6_utilisation.md` contradicted by the
CSV written beside it by the same run. The reviewer measured the hole directly: reverting
R752's two comprehensions republishes `AMPLIFIED on 10, SIMPLE on 7` -- still carrying its
own `(read from interaction_form, not inferred -- R752)` parenthesis -- with the whole suite
green.

So this file reads the two published files and asserts the summary's counts against the
CSV's own columns. It is a REGRESSION test and not a guard: it compares two shipped
artifacts with each other, it asserts no threshold, and it carries no tolerance.

WHAT IT CANNOT DO, said so it is not trusted past its reach. It cannot tell whether the
CSV is right -- that is G6.1's job, and G6.1 pins `interaction_form` against both forms of
section 3.3.2 worked by hand at 120 configurations. What it can tell is whether the PROSE
agrees with the TABLE, which is the question all three of those findings turned on.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "docs" / "F6_utilisation.md"
TABLE = ROOT / "docs" / "F6_utilisation.csv"


def _rows() -> list[dict[str, str]]:
    lines = [ln for ln in TABLE.read_text(encoding="utf-8").splitlines() if ln[:1] != "#"]
    return list(csv.DictReader(lines))


def _summary() -> str:
    return SUMMARY.read_text(encoding="utf-8")


def test_both_deliverables_are_present_and_non_empty() -> None:
    """Meta: an absent or empty file makes every assertion below vacuous."""
    assert TABLE.is_file() and SUMMARY.is_file()
    rows = _rows()
    assert len(rows) == 32, f"the CSV carries {len(rows)} rows; the table is 32 member-stations"
    assert "interaction_form" in rows[0], sorted(rows[0])


def test_the_FORM_counts_in_the_prose_are_the_CSV_s_own_counts() -> None:
    """R752's repair, held in place.

    The sentence names two counts and the CSV carries the column they are counts of.
    Reverting the generator's two comprehensions republishes them swapped, and before this
    test nothing noticed.
    """
    rows = [r for r in _rows() if r["axial_branch"] != "tension"]
    amplified = sum(1 for r in rows if r["interaction_form"] == "amplified")
    simple = sum(1 for r in rows if r["interaction_form"] == "simple")
    assert amplified + simple == len(rows), {r["interaction_form"] for r in rows}

    match = re.search(
        r"section 3\.3\.2 over (\d+) compression rows: AMPLIFIED governs on (\d+), "
        r"SIMPLE on (\d+)",
        _summary(),
    )
    assert match is not None, (
        "the summary carries no `AMPLIFIED governs on N, SIMPLE on M` sentence. Either it "
        "was reworded or it was removed, and this test is what reads it."
    )
    published = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    assert published == (len(rows), amplified, simple), (
        f"the summary publishes {published} (rows, amplified, simple) and the CSV's own "
        f"interaction_form column gives {(len(rows), amplified, simple)}. This is R752: the "
        "sentence and the table in one file, disagreeing."
    )


def test_the_Cm_VISIBILITY_count_is_the_CSV_s_own_count() -> None:
    """The second sentence, which answers a different question and must stay separate.

    It is a count of rows where `C_m` visibly moves the station's governing utilisation --
    at the precision the CSV publishes, because that is the only precision a reader can
    reproduce from the file the sentence sits beside.
    """
    rows = [r for r in _rows() if r["axial_branch"] != "tension"]
    visible = sum(
        1
        for r in rows
        if f"{float(r['utilisation_Cm1']):.6g}" != f"{float(r['utilisation_K2']):.6g}"
    )
    match = re.search(r"C_m visibly moves U on (\d+) of (\d+)", _summary())
    assert match is not None, "the summary carries no `C_m visibly moves U on N of M` sentence"
    assert (int(match.group(1)), int(match.group(2))) == (visible, len(rows)), (
        f"the summary publishes {match.group(1)} of {match.group(2)} and the CSV gives "
        f"{visible} of {len(rows)}"
    )


def test_the_two_counts_are_DIFFERENT_so_neither_can_stand_for_the_other() -> None:
    """R752's whole mechanism: one was read off the other and came out backwards.

    If the two ever coincide, the sentence that distinguishes them stops being checkable by
    the reader -- so the divergence is asserted rather than assumed. On the shipped table
    the overtake margin that separates them is as tight as `0.1153%`, which is why the
    coincidence is contingent and why both counts are published.
    """
    rows = [r for r in _rows() if r["axial_branch"] != "tension"]
    amplified = sum(1 for r in rows if r["interaction_form"] == "amplified")
    visible = sum(
        1
        for r in rows
        if f"{float(r['utilisation_Cm1']):.6g}" != f"{float(r['utilisation_K2']):.6g}"
    )
    assert amplified != visible, (
        f"both counts are {amplified}. They answer different questions and on this table "
        "they happened to agree -- which is the state in which reading one off the other "
        "looks correct. Re-read the explanation in scripts/measure/api_wsd_utilisation.py "
        "before changing this assertion."
    )


def test_the_governing_clause_agrees_with_the_axial_branch_on_every_row() -> None:
    """R739's class: a tension-positive column read as compression put every over-unity
    station on the wrong clause. Here the two published columns must agree about the sense.
    """
    for row in _rows():
        tension = row["axial_branch"] == "tension"
        clause = row["governing_clause"]
        if clause.startswith("3.3."):
            want = "3.3.1 interaction" if tension else "3.3.2 interaction"
            assert clause == want, (
                f"{row['member']} {row['station']} is {row['axial_branch']} and the "
                f"governing clause reads {clause!r}; the clause for that sense is {want!r}"
            )
        if clause.startswith("3.2.1"):
            assert tension, f"{row['member']} {row['station']}: section 3.2.1 on compression"
        if clause.startswith("3.2.2"):
            assert not tension, f"{row['member']} {row['station']}: section 3.2.2 on tension"


@pytest.mark.parametrize(
    "label",
    [
        "INDICATIVE SIZING SCREEN -- NOT A CODE CASE",
        "tests/verification/rung5/",
        "heading 0 degrees",
        "total_instant",
        "tension-positive",
    ],
)
def test_the_label_the_milestone_requires_is_on_the_face_of_both_files(label: str) -> None:
    """F6.md section 1: every report this milestone generates carries the label on its face.

    `tests/verification/rung5/` is in the list because R748 was that citation pointing at a
    directory CI runs as `empty:` -- the warrant naming the wrong place is the same defect
    as the warrant being absent.
    """
    assert label in _summary(), f"the summary does not carry {label!r}"
    assert label.replace(";", ",") in TABLE.read_text(encoding="utf-8").replace(
        ";", ","
    ), f"the CSV's label block does not carry {label!r}"
