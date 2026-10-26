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


def test_R896_the_GENERATOR_refuses_a_sidecar_the_run_reader_refuses(tmp_path) -> None:
    """The deliverable's generator is the CALL SITE, and it is held here (FT2's rule).

    **R896: ONE INPUT, TWO READERS, ONE OF THEM VALIDATING.** `main` read `prov["run"]`
    straight out of the JSON and published `heading_deg` and both wave heights from it, so
    a sidecar `floatfea run` refuses by name was accepted here at exit 0. One variable
    moved, the committed sidecar with its two heights negated:

        HEAD's generator  -> EXIT=0, "wave height, full scale  : -24.2 m (-0.484 m model,
                             Froude lambda = 50.0)"
        repaired          -> EXIT=1, ConfigError, nothing published

    A unit test on `wave_basis_from_sidecar` is green with the call removed from this
    generator, which is the hole R866, R877 and R881 each shipped through -- so this test
    runs the real script as a subprocess.
    """
    import json as _json
    import subprocess
    import sys

    good = ROOT / "data" / "f4" / "dynamic_inputs.provenance.json"
    recorded = _json.loads(good.read_text(encoding="utf-8"))
    recorded["run"]["wave_height_full_m"] = -24.2
    recorded["run"]["wave_height_model_m"] = -0.484
    bad = tmp_path / "bad.provenance.json"
    bad.write_text(_json.dumps(recorded, indent=1), encoding="utf-8")

    proc = subprocess.run(
        [
            sys.executable,
            str(GENERATOR),
            "--out",
            str(tmp_path / "out.md"),
            "--provenance",
            str(bad),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert proc.returncode != 0, (
        "the generator accepted a sidecar the `floatfea run` reader refuses by name, and "
        "a negative wave height reached a published deliverable at exit 0: "
        + (tmp_path / "out.md").read_text(encoding="utf-8")[:400]
    )
    combined = proc.stdout + proc.stderr
    assert "wave_height_full_m" in combined, combined[-600:]

    # AND THE GOOD SIDECAR STILL GOES THROUGH -- the door refuses the wrong thing only.
    ok = subprocess.run(
        [sys.executable, str(GENERATOR), "--out", str(tmp_path / "ok.md")],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert ok.returncode == 0, (ok.stdout + ok.stderr)[-600:]
    assert "24.2 m (0.484 m model" in (tmp_path / "ok.md").read_text(encoding="utf-8")


def test_R902_the_BAND_is_computed_at_the_RECORDED_height(tmp_path) -> None:
    """The generator validated the recorded height and then ignored it.

    `WAVE_HEIGHT_FULL_M = 24.2` was a module literal, and the band, the steepness ratio
    and the BREAKING verdict all came from it while the HEADER printed the recorded value.
    They agree at `24.2` today, so no shipped artifact was wrong -- the control for that is
    that both deliverables still regenerate byte-identical. The defect needs a sidecar at
    a different H, which is FT2.6's own work in this step.

    One variable moved, at `model=1.0, full=50.0` -- inside `WAVE_HEIGHT`'s domain and
    consistent with the recorded lambda, so R895's relation check would pass it too:

        HEAD      "the associated-period band for H = 24.2 m"   12.5  0.0992  ok
                                                                      0.334% short
        repaired  "the associated-period band for H = 50.0 m"   12.5  0.2050  BREAKING
                                                                      30.662% short

    A breaking, out-of-band sea state published as admissible, at exit 0.
    """
    import json as _json
    import subprocess
    import sys

    recorded = _json.loads(
        (ROOT / "data" / "f4" / "dynamic_inputs.provenance.json").read_text(encoding="utf-8")
    )
    recorded["run"]["wave_height_full_m"] = 50.0
    recorded["run"]["wave_height_model_m"] = 1.0
    side = tmp_path / "h50.provenance.json"
    side.write_text(_json.dumps(recorded, indent=1), encoding="utf-8")

    out = tmp_path / "h50.md"
    # **AND THE FORCES TABLE MUST BE AT THIS SEA STATE TOO -- R946's shape, here.** This
    # cell passed `--provenance` alone, so it ran at H = 50 m against the committed
    # `docs/F4_member_forces.csv`, whose own caveats say H = 24.2 m. Nothing noticed until
    # R938's height join refused it: the join turned a silent mismatch into a red test,
    # which is what it is for, and this cell was one of the things relying on the silence.
    # UNDER `ROOT`, because `member_forces_table.py` prints
    # `args.out.relative_to(ROOT)` AFTER writing both files, so a path outside the
    # repository raises `ValueError` once the work is already done (R918, now with a
    # third witness; `scratch/` is gitignored).
    # R918 is repaired, so this no longer needs a directory inside the repository
    # (R956: those were gitignored and accumulated one per cell per run).
    forces = tmp_path / "forces_at_this_sea_state.csv"
    made = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "measure" / "member_forces_table.py"),
            "--out",
            str(forces),
            "--summary",
            str(tmp_path / "forces_at_this_sea_state.md"),
            "--provenance",
            str(side),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert made.returncode == 0, (made.stdout + made.stderr)[-700:]

    proc = subprocess.run(
        [
            sys.executable,
            str(GENERATOR),
            "--out",
            str(out),
            "--provenance",
            str(side),
            "--forces",
            str(forces),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-600:]
    text = out.read_text(encoding="utf-8")

    assert "band for H = 50.0 m" in text, (
        "the band was computed at a height the sidecar does not record. That is R902: a "
        "module literal deciding the breaking verdict while the header printed the "
        "recorded value."
    )
    assert "band for H = 24.2 m" not in text, "the literal is still deciding the band"
    assert "BREAKING" in text, (
        "H = 50 m at T = 12.5 s is H/L = 0.2050, past the 1/7 breaking limit. A "
        "deliverable that does not say so is the silently wrong result R902 names."
    )


def test_R902_NEITHER_generator_carries_a_module_wave_height_literal() -> None:
    """`grep -rn WAVE_HEIGHT_FULL_M tests/` was empty while two generators defined it.

    The shape, not the two instances: a module constant in a `scripts/measure/` generator
    standing in for a recorded input is R805/FN0, which `member_forces_table.py`'s own
    comment records seven lines above where it was doing it again. This is the assertion
    that was missing, and it names the symbol so the grep is no longer empty.
    """
    import re

    for name in ("f6_results_report.py", "member_forces_table.py"):
        src = (ROOT / "scripts" / "measure" / name).read_text(encoding="utf-8")
        for symbol in ("WAVE_HEIGHT_FULL_M", "FROUDE_LAMBDA"):
            assigned = re.search(rf"(?m)^{symbol}\s*=", src)
            assert assigned is None, (
                f"{name} defines a module-level {symbol}. The scale and the height are "
                f"recorded in the provenance sidecar and read through "
                f"`wave_basis_from_sidecar`; a constant here overrides the record "
                f"silently, which is R902 and, before it, R805/FN0."
            )


def test_R926_every_SCRIPT_THAT_TOUCHES_A_RECORDED_SCALE_resolves_it() -> None:
    """The domain is DERIVED from the tree, not typed (R926, and the repair for its class).

    **THE LIST WAS TWO FILENAMES AND THAT IS WHY R926 EXISTED.** The R919 version of this
    test named `f6a_premise_check.py` and `member_forces_table.py` by hand, so
    `f6_results_report.py` -- which printed `Froude lambda = {run['lambda']}` from the
    sidecar, cross-checked by nothing -- was outside its domain and published `25.0`
    beside an npz recording `50.0` at exit 0, while the other generator refused the
    identical pair. Same quantity, same file pair, two readers, opposite outcomes.

    That is the shape of R919, R925, R926 and R927 alike: **a check applied to the sites
    its author was looking at rather than to the site list the repository has.** Three
    hand lists did it at three levels -- a commit message's claim, this test's filenames,
    and the caveat tuple -- so the repair is a derived list and not more attention.

    Three properties, each over every `.py` under `scripts/`:

    **(i) Nothing READS a recorded scale by subscript.** A scale is RESOLVED, not echoed.
    The load/store distinction is what separates a consumer from the export that writes
    the record, so no filename has to be exempted: `export_f4_dynamic_inputs.py` writes
    `run["lambda"]` and reads none.

    **(ii) Nothing calls `exported_froude_lambda`.** It reports where it read a value and
    validates nothing about it -- the FN0 reader, library-internal, and R919's defect was
    a publisher being routed onto it.

    **(iii) A file that converts with `froude_factor` resolves a scale first.** A
    conversion is only as good as the number it is given, which is R925: two factors
    published as `lambda = 50` literals, 8x and 16x wrong at a legitimate `lambda = 25`.
    """
    import ast

    read_sites: list[str] = []
    reader_sites: list[str] = []
    unresolved_converters: list[str] = []

    for path in sorted((ROOT / "scripts").rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        calls = {
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        }
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Constant)
                and node.slice.value in ("lambda", "froude_lambda")
                and isinstance(node.ctx, ast.Load)
            ):
                read_sites.append(f"{path.name}:{node.lineno}")
        if "exported_froude_lambda" in calls:
            reader_sites.append(path.name)
        if "froude_factor" in calls and "validated_export_scale" not in calls:
            unresolved_converters.append(path.name)

    assert not read_sites, (
        f"these sites READ a recorded scale instead of resolving one: {read_sites}. A "
        f"scale echoed out of a sidecar is cross-checked by nothing -- that is R926, and "
        f"it published `Froude lambda = 25.0` above forces computed at 50."
    )
    assert not reader_sites, (
        f"{reader_sites} call `exported_froude_lambda`, which validates nothing about the "
        f"value it returns (R919). Publishers go through `validated_export_scale`."
    )
    assert not unresolved_converters, (
        f"{unresolved_converters} convert with `froude_factor` without resolving a scale "
        f"first, so the factor is whatever was lying around (R925)."
    )

    # AND THE DOMAIN IS NOT EMPTY, so none of the three can pass by finding nothing.
    resolvers = [
        path.name
        for path in sorted((ROOT / "scripts").rglob("*.py"))
        if "validated_export_scale"
        in {
            node.func.id
            for node in ast.walk(ast.parse(path.read_text(encoding="utf-8", errors="replace")))
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        }
    ]
    assert len(resolvers) >= 3, (
        f"only {resolvers} resolve a scale. Three generators publish one; a sweep that "
        f"finds fewer is measuring nothing, which is how two typed filenames passed."
    )
