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
    match = re.search(
        r"C_m visibly moves the governing U on (\d+) of (\d+) compression rows, at the "
        r"(\d+) significant figures",
        _summary(),
    )
    assert match is not None, (
        "the summary carries no `C_m visibly moves the governing U on N of M compression "
        "rows, at the K significant figures` sentence. R753 deleted the clause that used "
        "to follow it -- `those are the rows where amplified(C_m = 1.0) OVERTAKES simple`, "
        "which holds on 17 of 17 and distinguished nothing -- so this reads the predicate "
        "and the precision it is taken at, and nothing else."
    )
    assert int(match.group(3)) == 6, (
        f"the summary says the count is taken at {match.group(3)} significant figures and "
        "this test compares at 6, which is what the CSV writes"
    )
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


# --------------------------------------------------------------------------
# R756: THE LOCKED PLAN'S REGENERATION GATE, WHICH WAS ASSERTED NOWHERE
# --------------------------------------------------------------------------
# `docs/milestones/F6.md:261` locks it: "the table regenerates identically from stored
# results (G6.3's shape), and the top-ten list is stable under a re-run." Nothing in
# `tests/` read `results/F6/` at all, and the deliverable was NOT deterministic -- the
# reviewer regenerated it and found eight lines of 457 differing, every one a pytest
# wall-clock timing pasted into section 5's status block.
#
# The repair was to publish the COUNTS and not the duration: the counts are what each row
# claims and they are deterministic, the duration was never part of the claim. These two
# tests are what holds that in place, and they are the gate the plan named.

RESULTS_REPORT = ROOT / "results" / "F6" / "floatfea_results_report.md"
GENERATOR = ROOT / "scripts" / "measure" / "f6_results_report.py"


def test_R756_the_results_report_REGENERATES_IDENTICALLY() -> None:
    """Two runs of the generator, byte-compared. The plan's gate, as a test.

    `--no-gates` is passed because the status column's own run is what this file is NOT
    measuring: it would invoke the eight gates twice inside one test, and a difference
    there would be a red gate rather than a non-deterministic document. Everything else --
    the model block, the mass basis, the loads, the envelope, the `f` sweep, the top ten
    and every table -- is compared in full.
    """
    import subprocess
    import sys
    import tempfile

    assert GENERATOR.is_file(), GENERATOR
    with tempfile.TemporaryDirectory() as tmp:
        outs = []
        for n in (1, 2):
            out = Path(tmp) / f"run{n}" / "floatfea_results_report.md"
            proc = subprocess.run(
                [sys.executable, str(GENERATOR), "--no-gates", "--out", str(out)],
                capture_output=True,
                text=True,
                cwd=ROOT,
            )
            assert proc.returncode == 0, proc.stderr[-2000:]
            outs.append(out.read_text(encoding="utf-8"))
    first, second = outs
    if first != second:
        pairs = zip(first.splitlines(), second.splitlines(), strict=False)
        differing = [(n, a, b) for n, (a, b) in enumerate(pairs, 1) if a != b]
        pytest.fail(
            f"the deliverable does not regenerate identically: {len(differing)} line(s) "
            f"differ out of {len(first.splitlines())}. First three:\n"
            + "\n".join(f"  line {n}:\n    {a!r}\n    {b!r}" for n, a, b in differing[:3])
            + "\nThis is the gate at docs/milestones/F6.md:261 (R756). A figure that "
            "changes between two runs of the same tree is not a measurement of the tree."
        )


def test_R756_the_published_report_carries_NO_WALL_CLOCK_figure() -> None:
    """The specific non-determinism R756 found -- and it REGENERATES to look for it.

    **THE FIRST VERSION OF THIS TEST COULD NOT FAIL, which is the defect it was written to
    prevent.** It read only the shipped file, and the shipped file had already been
    regenerated without timings -- so reverting the generator's one line left both R756
    tests green. Measured: `12 passed` with `counts = tail[-1]` restored, which is R756's
    own state.

    So it runs the generator WITH the gates, into a temporary directory, and reads THAT.
    The status column is the only part of the document a timing can enter through, and
    running the gates is the only way to produce one. It costs one pass of the eight gate
    invocations; the shipped file is checked too, because that is what is published.
    """
    import subprocess
    import sys
    import tempfile

    pattern = r"\d+ (?:passed|failed) in [\d.]+s"

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "floatfea_results_report.md"
        proc = subprocess.run(
            [sys.executable, str(GENERATOR), "--out", str(out)],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        assert proc.returncode == 0, proc.stderr[-2000:]
        regenerated = out.read_text(encoding="utf-8")

    assert re.search(r"\d+ passed", regenerated), (
        "a run WITH the gates produced no `N passed` at all, so the assertion below is "
        "vacuous -- either section 5's status block was removed or it stopped running them."
    )
    timings = re.findall(pattern, regenerated)
    assert not timings, (
        f"regenerating with the gates produced {len(timings)} wall-clock figure(s): "
        f"{timings[:4]}. The counts are deterministic and the durations are not, so two "
        "runs of the same tree yield different documents (R756). This is the assertion "
        "that reddens when the generator stops stripping the duration."
    )

    assert RESULTS_REPORT.is_file(), RESULTS_REPORT
    shipped = RESULTS_REPORT.read_text(encoding="utf-8")
    shipped_timings = re.findall(pattern, shipped)
    assert not shipped_timings, (
        f"the PUBLISHED report carries {len(shipped_timings)} wall-clock figure(s): "
        f"{shipped_timings[:4]}. The generator is fixed but the shipped file was not "
        "regenerated after it."
    )
