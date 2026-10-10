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

    **R763: TWO OF THE FOUR ARMS WERE VACUOUS AND ONE WHOLE FAMILY REACHED NO ASSERTION.**
    No shipped row's `governing_clause` starts with `3.2.1` or `3.2.2` -- the published
    distribution is `3.3.1 interaction` 6, `3.3.2 interaction` 12, `3.2.4 beam shear` 14 --
    so those two `if` arms ran on 0 of 32 rows, and the 14 beam-shear rows fell through
    every branch. The two arms are kept because a future table could land on either clause
    and the sense would still have to agree; what is added is a measured check that the
    clause set is the one this file was written against, so an arm going vacuous is visible
    rather than silent, and an explicit assertion for the shear family.
    """
    rows = _rows()
    seen: dict[str, int] = {}
    for row in rows:
        tension = row["axial_branch"] == "tension"
        clause = row["governing_clause"]
        seen[clause] = seen.get(clause, 0) + 1
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
        if clause.startswith("3.2.4"):
            # The shear family reached no assertion at all. Shear governs when the shear
            # utilisation is the largest of the row's four -- that is what "governing"
            # means -- and it is sense-agnostic, which is why the arms above skip it.
            u = {k: float(row[k]) for k in ("u_axial", "u_bending", "u_shear", "u_torsion")}
            assert u["u_shear"] >= max(u.values()), (
                f"{row['member']} {row['station']} is published as governed by "
                f"{clause!r} and its shear utilisation {u['u_shear']:.6g} is not the "
                f"largest of {u}"
            )

    # R763's own guard: if the clause set changes, the two sense arms above may go vacuous
    # and nothing else in this file would say so.
    assert seen == {"3.3.1 interaction": 6, "3.3.2 interaction": 12, "3.2.4 beam shear": 14}, (
        f"the published clause distribution is {seen}, not the one this test was written "
        "against. Two of its four sense arms are reached by NO shipped row as written "
        "(3.2.1 and 3.2.2, 0 of 32), so a change here can make them vacuous silently -- "
        "re-read R763 before updating this number."
    )


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
# R756 / R757: THE LOCKED PLAN'S REGENERATION GATE, ON THE GATED DOCUMENT
# --------------------------------------------------------------------------
# `docs/milestones/F6.md:261` locks it: "the table regenerates identically from stored
# results (G6.3's shape), and the top-ten list is stable under a re-run." Nothing in
# `tests/` read `results/F6/` at all, and the deliverable was NOT deterministic -- eight
# lines of 457 differed between two runs, every one a pytest wall-clock timing pasted into
# section 5's status block (R756).
#
# **R757: THE FIRST TWO VERSIONS OF THIS GATE WERE BOTH VACUOUS, AND THE SECOND LOOKED LIKE
# A REPAIR.** Version one read only the shipped file, which had already been regenerated
# clean, so reverting the generator left `12 passed`. Version two added a double run -- and
# passed it `--no-gates`, under which `_run_gate` is never called, `gate_runs` is empty, and
# `if gate_runs:` means **the entire "pytest's own summary for each row" block is not
# emitted at all**. R756's eight differing lines lived inside that block. So the
# determinism assertion was green on R756's own state BY CONSTRUCTION: the same shape as
# the version thrown away, one level out, inside the commit repairing a finding about a
# missing gate.
#
# So the comparison is taken on the GATED document, which is the only form that contains
# the column a timing can enter through. It costs two passes of the eight gate node-sets,
# shared by every assertion below through one module-scoped fixture.

RESULTS_REPORT = ROOT / "results" / "F6" / "floatfea_results_report.md"
GENERATOR = ROOT / "scripts" / "measure" / "f6_results_report.py"

# A pytest summary line, with however many clauses stand between the count and the
# duration. The first version of this pattern required the count ADJACENT to `" in "`, so
# `22 passed, 1 warning in 3.45s` and `53 passed, 1 skipped in 9.01s` -- both forms this
# tree emits elsewhere -- did not match it. It reddened only because the eight gate
# node-sets happen to print a bare `N passed` today, and would have stopped doing so the
# day a warning appeared in any of four unrelated rung modules.
_PYTEST_DURATION = re.compile(r"\d+ (?:passed|failed)[^\n]*? in [\d.]+s")


def _first_differences(left: str, right: str) -> list[tuple[int, str, str]]:
    pairs = zip(left.splitlines(), right.splitlines(), strict=False)
    return [(n, a, b) for n, (a, b) in enumerate(pairs, 1) if a != b]


@pytest.fixture(scope="module")
def gated_runs() -> list[str]:
    """Two full regenerations WITH the gates, into a temporary directory."""
    import subprocess
    import sys
    import tempfile

    assert GENERATOR.is_file(), GENERATOR
    out: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        for n in (1, 2):
            path = Path(tmp) / f"run{n}" / "floatfea_results_report.md"
            proc = subprocess.run(
                [sys.executable, str(GENERATOR), "--out", str(path)],
                capture_output=True,
                text=True,
                cwd=ROOT,
            )
            assert proc.returncode == 0, proc.stderr[-2000:]
            out.append(path.read_text(encoding="utf-8"))
    return out


def test_R757_the_gated_regeneration_CONTAINS_the_status_block(
    gated_runs: list[str],
) -> None:
    """The premise every assertion below rests on, asserted rather than assumed.

    Without this, a generator change that stopped emitting section 5 would make the whole
    pair below pass on an absent column -- which is precisely how R757 happened.
    """
    for n, text in enumerate(gated_runs, 1):
        assert "pytest's own summary for each row" in text, (
            f"gated run {n} does not contain section 5's status block, so the comparisons "
            "below cannot see the column R756's timings entered through (R757)."
        )
        assert re.search(
            r"\d+ passed", text
        ), f"gated run {n} carries no `N passed`, so the status column ran no gates."


def test_R756_the_results_report_REGENERATES_IDENTICALLY(gated_runs: list[str]) -> None:
    """The plan's gate: two GATED runs, byte-compared."""
    first, second = gated_runs
    differing = _first_differences(first, second)
    assert not differing, (
        f"the deliverable does not regenerate identically: {len(differing)} line(s) "
        f"differ out of {len(first.splitlines())}. First three: "
        + " | ".join(f"line {n}: {a!r} vs {b!r}" for n, a, b in differing[:3])
        + " -- this is the gate at docs/milestones/F6.md:261 (R756). A figure that changes "
        "between two runs of the same tree is not a measurement of the tree."
    )


def test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree(
    gated_runs: list[str],
) -> None:
    """The plan's other half: the committed file IS what this tree regenerates.

    The tests either side of this one both hold on a deliverable generated from an older
    tree and never refreshed. This compares the SHIPPED bytes against a fresh gated run,
    which is what "regenerates identically from stored results" actually says.
    """
    assert RESULTS_REPORT.is_file(), RESULTS_REPORT
    shipped = RESULTS_REPORT.read_text(encoding="utf-8")
    differing = _first_differences(shipped, gated_runs[0])
    assert not differing and len(shipped.splitlines()) == len(gated_runs[0].splitlines()), (
        f"the committed deliverable is not what this tree regenerates: "
        f"{len(differing)} line(s) differ, shipped has {len(shipped.splitlines())} lines "
        f"against {len(gated_runs[0].splitlines())}. First three: "
        + " | ".join(f"line {n}: shipped {a!r} vs fresh {b!r}" for n, a, b in differing[:3])
        + " -- re-run `python scripts/measure/f6_results_report.py`."
    )


def test_R756_no_WALL_CLOCK_figure_in_the_GATED_or_the_SHIPPED_report(
    gated_runs: list[str],
) -> None:
    """The specific non-determinism R756 found, on both the fresh and the shipped bytes."""
    for label, text in (
        ("the gated regeneration", gated_runs[0]),
        ("the SHIPPED report", RESULTS_REPORT.read_text(encoding="utf-8")),
    ):
        timings = _PYTEST_DURATION.findall(text)
        assert not timings, (
            f"{label} carries {len(timings)} pytest wall-clock figure(s): {timings[:4]}. "
            "The counts are deterministic and the durations are not, so two runs of the "
            "same tree yield different documents (R756)."
        )


@pytest.mark.parametrize(
    "summary",
    [
        "22 passed in 3.45s",
        "1 failed, 11 passed in 14.12s",
        "22 passed, 1 warning in 3.45s",
        "53 passed, 2 warnings in 9.01s",
        "22 passed, 1 skipped in 2.0s",
        "3315 passed, 2 warnings in 698.74s",
    ],
)
def test_R757_the_duration_pattern_matches_EVERY_form_pytest_prints(summary: str) -> None:
    """The pattern's own counter-case, because its first version was narrower than its claim.

    Three of the six forms below did not match the original pattern, which required the
    count adjacent to `" in "`. Two of them are emitted by this repository today -- the
    reviewer's own whole-suite line and the step report's `664 passed, 1 warning in
    260.47s`. The gate reddened only by the accident that the eight gate node-sets print a
    bare count.
    """
    assert _PYTEST_DURATION.search(summary), (
        f"{summary!r} is a form pytest prints and the duration pattern does not match it, "
        "so a timing in that form would pass the gate above."
    )
