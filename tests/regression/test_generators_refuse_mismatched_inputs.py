"""The deliverable generators, driven as real processes (R933).

**NOTHING IN `tests/` INVOKED ANY OF THEM, AND NOTHING NAMED R907 OR R909.** Measured at
`e645e38`: `grep -rl R907 tests/` and `grep -rl R909 tests/` were both empty, and the only
references to the three generators were corpus prose and two tests that import one of them
for its symbols. Every finding from R896 onward was a check one publisher did not use, and
the reason the same shape recurred eight times is that the publishers were never run.

The cells are cheap because every refusal fires before `build_superstructure()`:

    f6_results_report.py       exit=1    0.63 s
    member_forces_table.py     exit=1    0.49 s

**But the ACCEPTANCE cells are not cheap, and an earlier revision of this docstring said
otherwise (R954).** It claimed "the whole file is seconds" and cited "the twenty minutes a
full generator run costs". Both were false once the acceptance cells arrived: every cell
that requires a generator to SUCCEED runs the full solve, several now do, and the file
takes minutes. A full `member_forces_table.py` solve is about a minute -- the twenty-minute
figure belongs to `f6a_premise_check.py --dynamic`, which this file does not drive.

**The mutations are all SIDECAR-side on purpose.** `f4_dynamic_residual.load()` checks the
npz's sha256 against the sha the provenance declares, so a modified npz needs its declared
sha rewritten to reach anything downstream -- which is how my first R908 caller cell came
to prove nothing (an older guard fired first). The npz-side domain and agreement cells live
in `tests/unit/test_headings_and_bem_coverage.py`, where they drive the resolver directly.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]
MEASURE = ROOT / "scripts" / "measure"
SIDECAR = ROOT / "data" / "f4" / "dynamic_inputs.provenance.json"
FORCES = ROOT / "docs" / "F4_member_forces.csv"
UTIL = ROOT / "docs" / "F6_utilisation.csv"


def _sidecar(tmp: Path, **run_fields: Any) -> Path:
    """The committed sidecar with `run` fields overridden, written beside nothing."""
    recorded = json.loads(SIDECAR.read_text(encoding="utf-8"))
    recorded["run"].update(run_fields)
    out = tmp / "mutated.provenance.json"
    out.write_text(json.dumps(recorded, indent=1), encoding="utf-8")
    return out


def _out_dir(tmp: Path) -> Path:
    """Pytest's own tmp directory, now that a generator can be pointed outside the repo.

    **THIS USED TO RETURN A DIRECTORY UNDER `ROOT` AND THAT WAS A WORKAROUND (R956).**
    `member_forces_table.py` ended with `args.out.relative_to(ROOT)` in a print, so a
    path outside the repository raised AFTER both files were written -- R918, worked
    around here, then again in `test_f6_deliverable_agrees_with_itself.py`, with a third
    witness from the reviewer. The directories it made were gitignored, so they were
    invisible to `git status` and accumulated one per cell per run: 15 of them and 1.9 MB
    by the time anyone looked.

    R918 is repaired at its two lines now, so the workaround and the rubbish both go. The
    cause is removed rather than cleaned up after.
    """
    return tmp


def _run(script: str, tmp: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    """One generator, as a real process, writing only into a scratch directory."""
    tmp = _out_dir(tmp)
    args: list[str] = [sys.executable, str(MEASURE / script)]
    if script == "member_forces_table.py":
        args += ["--out", str(tmp / "o.csv"), "--summary", str(tmp / "o.md")]
    else:
        args += ["--out", str(tmp / "o.md")]
    args += list(extra)
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT)


def _wrote_nothing(tmp: Path) -> bool:
    """R878's shape: a refusal that leaves a zero-byte artifact behind is not a refusal."""
    out = _out_dir(tmp)
    return not any((out / name).exists() for name in ("o.md", "o.csv"))


GENERATORS = ("f6_results_report.py", "member_forces_table.py")


@pytest.mark.parametrize("script", GENERATORS)
def test_R933_the_control_runs_clean(script: str, tmp_path: Path) -> None:
    """Every refusal below is only evidence if the unmutated run succeeds."""
    proc = _run(script, tmp_path)
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]


@pytest.mark.parametrize("script", GENERATORS)
def test_R933_a_NEGATIVE_wave_height_is_refused_by_both(script: str, tmp_path: Path) -> None:
    """R881, at the publishers rather than at the reader.

    A negative recorded height reached `report.md` and both CSV headers at exit 0 before
    the validator existed. These are the processes that write the files.
    """
    side = _sidecar(tmp_path, wave_height_full_m=-24.2, wave_height_model_m=-0.484)
    proc = _run(script, tmp_path, "--provenance", str(side))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "wave_height_full_m" in proc.stdout + proc.stderr
    assert _wrote_nothing(tmp_path)


@pytest.mark.parametrize("script", GENERATORS)
def test_R933_a_DISAGREEING_scale_is_refused_by_both(script: str, tmp_path: Path) -> None:
    """R908 and R927 at the two publishers that resolve a scale.

    The npz key says 50.0; this sidecar says 25.0. FN0's PREFERENCE decides which to read
    and was never a licence to publish from one while the other says something else --
    `f6_results_report.py` published `Froude lambda = 25.0` above forces at 50 (R926),
    and `member_forces_table.py` took the height from one record and the scale from
    another (R927).
    """
    side = _sidecar(tmp_path, **{"lambda": 25.0})
    proc = _run(script, tmp_path, "--provenance", str(side))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "scale disagreement" in proc.stdout + proc.stderr
    assert _wrote_nothing(tmp_path)


def test_R933_an_ORPHAN_PERIOD_is_refused(tmp_path: Path) -> None:
    """R909: the band table is per recorded period, the response table per solved case.

    A seventh recorded period published a full sea-state row above a six-row response
    table -- a sea state that was never analysed.
    """
    recorded = json.loads(SIDECAR.read_text(encoding="utf-8"))
    side = _sidecar(tmp_path, periods_full_s=[*recorded["run"]["periods_full_s"], 25.0])
    proc = _run("f6_results_report.py", tmp_path, "--provenance", str(side))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    # R958 made the join two-directional and rewrote this refusal, so the needle moved
    # with it. The property is unchanged: a RECORDED period with no solved case behind it
    # is refused, and the message names which.
    assert "Recorded with no solved case" in proc.stdout + proc.stderr
    assert _wrote_nothing(tmp_path)


def test_R933_a_FORCES_TABLE_AT_ANOTHER_SCALE_is_refused(tmp_path: Path) -> None:
    """R938: the three inputs are joined through the CSV's own SCALE line.

    This reader resolves the scale from `--npz`, the basis from `--provenance` and every
    force from `--forces`, and joined none of them -- so a forces table generated at a
    different sea state published the reference basis over it at exit 0.
    """
    text = FORCES.read_text(encoding="utf-8")
    other = text.replace(
        "force x 125000; locked moment x 6250000", "force x 15625; locked moment x 390625"
    )
    assert other != text, "the SCALE line this cell mutates is not in the committed CSV"
    csv = tmp_path / "other_scale.csv"
    csv.write_text(other, encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--forces", str(csv))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "different Froude scale" in proc.stdout + proc.stderr
    assert _wrote_nothing(tmp_path)


@pytest.mark.parametrize("script", GENERATORS)
def test_R933_ANOTHER_SEA_STATE_RUNS_rather_than_refusing(script: str, tmp_path: Path) -> None:
    """R907, and the measurement that refusing was the wrong repair.

    My first R907 repair asserted the narrative's premises and raised when they failed,
    which made both generators unable to run at any sea state but one -- destroying the
    property R902 establishes and blocking FT2.6, whose whole job is producing other sea
    states. This is the cell that would have caught it directly.

    **R946: AND THIS CELL USED TO ASSERT R938's DEFECT.** It did not override `--forces`,
    so the `f6_results_report.py` arm ran at `H = 50 m` against the committed
    `docs/F4_member_forces.csv`, whose own caveats say `H = 24.2 m` -- and PASSED at exit
    0, because nothing joined the two. The cell's intent was right and its inputs were
    not. It now generates a forces table AT that sea state first, with the sibling
    generator, which is what the report must be pointed at.
    """
    side = _sidecar(tmp_path, wave_height_full_m=50.0, wave_height_model_m=1.0)
    out = _out_dir(tmp_path)
    extra: list[str] = []

    if script == "f6_results_report.py":
        # The forces table for THIS sea state, written by the generator that owns it.
        made = subprocess.run(
            [
                sys.executable,
                str(MEASURE / "member_forces_table.py"),
                "--out",
                str(out / "forces.csv"),
                "--summary",
                str(out / "forces.md"),
                "--provenance",
                str(side),
            ],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        assert made.returncode == 0, (made.stdout + made.stderr)[-700:]
        extra = ["--forces", str(out / "forces.csv")]

    proc = _run(script, tmp_path, "--provenance", str(side), *extra)
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]

    written = (out / "o.md").read_text(encoding="utf-8")
    assert "H = 50.0 m" in written or "H = 50 m" in written, written[:400]
    # The clauses that were true only at the reference sea state must be GONE, not
    # restated with a different number beside them (R907, R936).
    assert "too long for this height" not in written
    assert "associated-period range for H = 24.2" not in written
    assert "is within the guidance's own precision, and the case was CHOSEN" not in written


def test_R946_the_REPORT_refuses_a_forces_table_from_another_sea_state(tmp_path: Path) -> None:
    """The inverse of the cell above, which is the defect R946 named.

    A forces table at one sea state and a sidecar at another is exactly the state that
    published `24.2 m` over an H = 30 m table at exit 0. The join is on the `H = ... m`
    the caveats write and on the SCALE line's parsed factors (R938, R945).
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, wave_height_full_m=50.0, wave_height_model_m=1.0)
    made = subprocess.run(
        [
            sys.executable,
            str(MEASURE / "member_forces_table.py"),
            "--out",
            str(out / "other.csv"),
            "--summary",
            str(out / "other.md"),
            "--provenance",
            str(side),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert made.returncode == 0, (made.stdout + made.stderr)[-700:]

    # The forces table at H = 50 m, the sidecar left at the committed H = 24.2 m.
    proc = _run("f6_results_report.py", tmp_path, "--forces", str(out / "other.csv"))
    assert proc.returncode != 0, (
        "the report accepted a forces table from another sea state. That is R938: the "
        "basis, the scale and every force came from three inputs nobody joined: "
        + (out / "o.md").read_text(encoding="utf-8")[:300]
    )
    assert "different wave height" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R936_the_TWO_PREDICATES_cannot_disagree(tmp_path: Path) -> None:
    """At H = 30 m, where the membership predicate and `stale` used to differ (R936 iii).

    **THE CELL ABOVE IS VACUOUS FOR THIS.** The reviewer solved the two predicates over
    `WAVE_HEIGHT` on 100,001 points: they disagreed on exactly `H in [24.039, 30.153] m`
    -- 6114 points -- and AGREE at `H = 50 m`, so reverting `_reference = not stale`
    leaves the H = 50 cell green. H = 30 m is inside the window and is where the summary
    carried both branches at once:

        line 20  "... kept only if a rule like FA0 is stated for THIS height, WHICH NONE IS."
        line 67  "... and FA0 RULES THAT IT STAYS.** `10.5%` below the bound is within
                  the guidance's own precision"
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, wave_height_full_m=30.0, wave_height_model_m=0.6)
    proc = _run("member_forces_table.py", tmp_path, "--provenance", str(side))
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]

    written = (out / "o.md").read_text(encoding="utf-8")
    withheld = "a rule like FA0 is stated for THIS height" in written
    asserted = "is within the guidance's own precision, and the case was CHOSEN" in written
    assert not (withheld and asserted), (
        "the summary states both that no FA0 ruling exists for this height and that FA0 "
        "rules the case stays. Two predicates deciding one question is R936, and this "
        "height is where they differed."
    )
    assert withheld, "the computed branch should be the one taken at H = 30 m"


def test_R937_a_NON_INTEGER_scale_publishes_its_real_factor() -> None:
    """R937 (ii): nothing exercised a non-integer scale, so `:.0f` could come back green.

    The reviewer measured that no file outside `member_forces_table.py` mentions
    `_factor_text` and no test drove a fractional lambda, so reverting the format left
    the whole suite passing. At `lambda = 1.1447` the force composite is `1.499944` and
    `:.0f` published `force x 1` -- 33.33% low, inside the declared `FROUDE_LAMBDA`.
    """
    import importlib.util

    from floatfea.io.froude import froude_factor

    spec = importlib.util.spec_from_file_location(
        "_mft_for_R937", MEASURE / "member_forces_table.py"
    )
    assert spec is not None and spec.loader is not None
    mft = importlib.util.module_from_spec(spec)
    sys.modules["member_forces_table"] = mft
    spec.loader.exec_module(mft)

    assert mft._factor_text(froude_factor("force", 1.1447)) == "1.49994"
    assert mft._factor_text(froude_factor("moment", 1.1067)) == "1.5001"
    # And the committed scale still prints as the deliverables carry it -- an integer with
    # no decimal part, which is why `:.0f` was exact there and nowhere else.
    assert mft._factor_text(froude_factor("force", 50.0)) == "125000"
    assert mft._factor_text(froude_factor("moment", 50.0)) == "6250000"


@pytest.mark.parametrize(("height", "expect"), [(10.0, "ABOVE"), (14.21, "INSIDE")])
def test_R944_the_PROSE_agrees_with_the_TABLE_about_T_12_5(
    tmp_path: Path, height: float, expect: str
) -> None:
    """A height where the band's two edges give different answers (R944).

    **AND THIS CELL EXISTS BECAUSE THE FIX WAS UNHELD WITHOUT IT.** I repaired R944 and
    then reverted the repair: `11 passed`. The one-edged guard
    `math.sqrt(6.5 * h_full) <= 12.5` is wrong only where the band's UPPER edge has
    fallen past 12.5 s, which happens at `H = 156.25/11 = 14.2045 m` -- and every other
    cell in this file uses 24.2, 30 or 50 m, all above it. A repair whose defect shows at
    no tested configuration is not held, which is the same vacuity the reviewer measured
    for R936 (iii) and R937 (ii), committed by me in the act of fixing it.

    At `H = 10 m` the band is 8.062-10.488 s, so `T = 12.5 s` is ABOVE it; the prose had
    said "INSIDE the band" over a row reading "above the band ... by 2.012 s". At
    `H = 14.21 m` it is genuinely inside, 0.0055 m past the boundary.
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, wave_height_full_m=height, wave_height_model_m=height / 50.0)
    proc = _run("member_forces_table.py", tmp_path, "--provenance", str(side))
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    written = (out / "o.md").read_text(encoding="utf-8")

    assert f"is {expect} the band at this height" in written, (
        f"at H = {height} m the prose does not place `T = 12.5 s` {expect} the band. "
        f"The table's own row is what it must agree with."
    )
    # The row and the sentence are the two readers R944 was about: whatever the row says,
    # the prose says the same thing.
    row = next(ln for ln in written.splitlines() if ln.startswith("| 12.5 "))
    assert (
        expect.lower().replace("above", "above the band").replace("inside", "in the band") in row
    ), (row, expect)


@pytest.mark.parametrize("height", [40.0, 50.0, 100.0])
def test_R950_the_FA0_WARNING_survives_where_the_offset_is_LARGEST(
    tmp_path: Path, height: float
) -> None:
    """`breaking` is a SUBSET of below-the-lower-edge, and R944's guard missed it.

    My R944 repair guarded on `_cat_12_5 != "below"`, and the breaking category's own
    string says "and below the band". So above
    `lambda(12.5)/7 = 34.8506694583 m` the document took the "no such question arises"
    branch for a case that is 30.7% below the edge at H = 50 m and sets nine of the ten
    most loaded stations at 455.7 MPa. **The code R944 replaced was right there**, so the
    repair was a regression: wrong on 65150 of 100000 points where the old one was wrong
    on none.

    The guard now asks the question the clause answers -- is `T = 12.5 s` below the lower
    edge -- while the WORD still comes from the table's four-outcome classification.
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, wave_height_full_m=height, wave_height_model_m=height / 50.0)
    proc = _run("member_forces_table.py", tmp_path, "--provenance", str(side))
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    written = (out / "o.md").read_text(encoding="utf-8")

    assert "That ruling is NOT asserted here" in written, (
        f"at H = {height} m `T = 12.5 s` is below the band's lower edge and FA0's ruling "
        f"is not asserted for this height, so the warning must be published. R944's "
        f"guard sent the breaking category down the no-question branch instead."
    )
    assert "no such question arises here" not in written


def test_R951_the_TWO_GENERATORS_agree_about_FA0_on_one_sidecar(tmp_path: Path) -> None:
    """The membership predicate R936 condemned survived in the twin file.

    R936 replaced it in `member_forces_table.py` and I measured the file the finding was
    raised in, not its sibling. On one matched H = 30 m pair the report published
    "... and is kept as the band's lower edge" while the forces table from the SAME
    sidecar published "That ruling is NOT asserted here". The reviewer's grid: true on
    `[24.0385, 30.1538] m` against exactly `24.2 m`, disagreeing on 61153 of 1e6 points.
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, wave_height_full_m=30.0, wave_height_model_m=0.6)

    made = subprocess.run(
        [
            sys.executable,
            str(MEASURE / "member_forces_table.py"),
            "--out",
            str(out / "forces.csv"),
            "--summary",
            str(out / "forces.md"),
            "--provenance",
            str(side),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert made.returncode == 0, (made.stdout + made.stderr)[-700:]

    proc = _run(
        "f6_results_report.py",
        tmp_path,
        "--provenance",
        str(side),
        "--forces",
        str(out / "forces.csv"),
    )
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]

    table = (out / "forces.md").read_text(encoding="utf-8")
    report = (out / "o.md").read_text(encoding="utf-8")
    withheld = "That ruling is NOT asserted here" in table
    # **THE NEEDLE MUST NOT SPAN A LINE BREAK, AND MY FIRST ONE DID.** The generator
    # emits that sentence as two `w(...)` lines, so "is kept as the band's lower edge"
    # appears in the document across lines 128/129 and matched nothing -- the cell passed
    # whatever the code did, which is the vacuity I had just been shown twice. The
    # reference branch's own marker is the sentence it opens with, on one line.
    claimed = "The governing basis is the four periods EZ2 admits" in report
    assert not (withheld and claimed), (
        "the two generators disagree about whether FA0's ruling applies at this height: "
        "the forces table withholds it and the report asserts it, from one sidecar."
    )
    assert withheld, "at H = 30 m the forces table should withhold the ruling"


def test_R952_a_FORCES_TABLE_WITH_NO_HEIGHT_is_refused(tmp_path: Path) -> None:
    """`if _seen_h and ...` skipped the join whenever the header carried no height.

    Measured by the reviewer: the real H = 50 m CSV with its three height tokens
    rewritten and everything else byte-identical -- SCALE line, 1248 rows -- gave exit 0
    and published `24.2 m`. Nine lines above, a missing SCALE line refuses. No current
    generator writes a heightless header, so the admitted class is the LEGACY one, which
    is the stale input the join exists to reject.
    """
    import re as _re

    out = _out_dir(tmp_path)
    stripped = _re.sub(r"H = [0-9.]+ m", "H = (not stated)", FORCES.read_text(encoding="utf-8"))
    csv = tmp_path / "no_height.csv"
    csv.write_text(stripped, encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--forces", str(csv))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "states no wave height" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R945_a_COLLIDING_SCALE_is_refused_not_substring_matched(tmp_path: Path) -> None:
    """R945's own condition (i): nothing drove the collision the parse exists for.

    `"force x 125000"` sits inside `"force x 125000000"`, so a forces table carrying
    lambda = 500's factors passed the old substring test at exit 0 over forces 1000x out.
    The existing mismatch cell uses 15625/390625, which the SUBSTRING test also refused
    -- so reverting the parse left the suite green, which the reviewer measured.
    """
    out = _out_dir(tmp_path)
    collided = FORCES.read_text(encoding="utf-8").replace(
        "force x 125000; locked moment x 6250000",
        "force x 125000000; locked moment x 62500000000",
    )
    csv = tmp_path / "lambda_500.csv"
    csv.write_text(collided, encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--forces", str(csv))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "different Froude scale" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R918_a_GENERATOR_can_be_pointed_outside_the_repository(tmp_path: Path) -> None:
    """Three cells were routed around this before it was two lines (R918, R949, R955).

    `args.out.relative_to(ROOT)` sat in a `print` after both files were written, so an
    `--out` outside the repository produced correct artifacts and then exited 1. A
    generator that cannot be pointed at a scratch path cannot be checked for determinism,
    which is part of why the regeneration gates went unasserted.

    `tmp_path` is deliberately NOT under `ROOT` here -- that is the whole property.
    """
    proc = subprocess.run(
        [
            sys.executable,
            str(MEASURE / "member_forces_table.py"),
            "--out",
            str(tmp_path / "outside.csv"),
            "--summary",
            str(tmp_path / "outside.md"),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    assert (tmp_path / "outside.csv").is_file() and (tmp_path / "outside.md").is_file()
    assert (tmp_path / "outside.csv").read_bytes() == FORCES.read_bytes()


def test_R958_the_PERIOD_JOIN_is_two_directional(tmp_path: Path) -> None:
    """A solved case with no declaration was silent, and that is what built R957.

    `set(_recorded) - _solved` refused a declared period with no case; the other
    direction was unchecked. At H = 24.1 m with a declared subset the report published
    "Breaking ...: none. Past the band's long edge: none" above a response table printing
    `T = 10 s` at 762.151 MPa -- breaking at that height -- and `T = 20 s` at
    338.226 MPa.

    **AND IT IS WHY R957's INPUT EXISTED.** The R951 repair keys the reference branch on
    the height alone, so a sidecar at the committed height declaring a SUBSET published
    the hand-written paragraph -- "the four periods EZ2 admits: the three in band" -- over
    a three-row table with two in band, naming two periods the run does not record. With
    both directions joined that input cannot be built, which is what makes the height
    comparison sufficient rather than merely narrow.
    """
    out = _out_dir(tmp_path)
    recorded = json.loads(SIDECAR.read_text(encoding="utf-8"))["run"]["periods_full_s"]

    # (a) a SOLVED case with no declaration -- R957's input, previously accepted
    subset = _sidecar(tmp_path, periods_full_s=[12.5, 14.0, 15.0])
    proc = _run("f6_results_report.py", tmp_path, "--provenance", str(subset))
    assert proc.returncode != 0, (
        "a declared SUBSET was accepted: the hand-written membership paragraph is then "
        "published over a table that does not match it (R957)."
    )
    assert "Solved with no declaration" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()

    # (b) a RECORDED period with no case -- R909's direction, still refused
    extra = _sidecar(tmp_path, periods_full_s=[*recorded, 25.0])
    proc = _run("f6_results_report.py", tmp_path, "--provenance", str(extra))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "Recorded with no solved case" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R959_the_COMMITTED_CSVs_are_byte_identical_to_their_own_BLOBS() -> None:
    """The deliverables are stored as their generators write them (R959).

    **THIS IS WHAT MADE FOUR ROUNDS OF "0 DIFF" MACHINE-DEPENDENT**, on both sides of the
    review. `csv.writer` terminates rows CRLF and the comment header is written LF; with
    `core.autocrlf=true` and no `.gitattributes` rule, git normalised every CRLF away, so
    the blob carried 0 CRLF where the generator writes 1249. The committed file could not
    equal its own generator's output on ANY platform -- on Windows a checkout re-added
    CRLF to all 1266 lines, matching neither; on Linux it matched the blob and so not the
    generator. It surfaced as a RED LADDER RUNG in CI, which skipped rungs 4 and 5.

    `*.csv -text` stores the bytes. This asserts the property directly, rather than
    leaving it to a cell that happens to compare bytes on one machine.
    """
    import subprocess

    tracked = subprocess.run(
        ["git", "ls-files", "*.csv"], capture_output=True, text=True, cwd=ROOT, check=True
    ).stdout.split()
    assert tracked, "no tracked CSVs found, so this check is measuring nothing"

    mismatched = []
    for rel in tracked:
        blob = subprocess.run(["git", "show", f"HEAD:{rel}"], capture_output=True, cwd=ROOT).stdout
        if blob != (ROOT / rel).read_bytes():
            mismatched.append(rel)
    assert not mismatched, (
        f"these committed CSVs differ from their own blobs: {mismatched}. Line endings "
        f"are being normalised on commit, so no regeneration check comparing a generator "
        f"against a checkout can be trusted on any platform (R959). `.gitattributes` "
        f"carries `*.csv -text` for this reason."
    )


def _subset_forces(tmp: Path, keep: set[str]) -> Path:
    """The committed forces table restricted to `keep` periods, header intact."""
    lines = FORCES.read_text(encoding="utf-8").splitlines(keepends=True)
    comments = [ln for ln in lines if ln.startswith("#")]
    body = [ln for ln in lines if not ln.startswith("#")]
    head, rows = body[0], body[1:]
    kept = [r for r in rows if r.split(",")[3] in keep | {""}]
    out = tmp / "subset_forces.csv"
    out.write_text("".join(comments) + head + "".join(kept), encoding="utf-8")
    return out


def test_R967_a_STALE_UTILISATION_TABLE_is_refused(tmp_path: Path) -> None:
    """`--util` was joined to nothing, and it is the one with a wrong number in it.

    One variable moved -- the 16.2 s rows deleted from the utilisation CSV, sidecar and
    forces table untouched:

        CONTROL     EXIT 0  member-stations 32  over unity 4 of 32
                            #3 = hub3_arm ROOT 16.2  **1.182**
        STALE UTIL  EXIT 0  member-stations 30  over unity 3 of 30
                            #3 = hub1_arm ROOT 12.5  **1.177**

    **A station over unity disappeared from the published count and the ranked table**
    at exit 0, with every other join green. `api_wsd_utilisation.py` reads the forces CSV
    and writes the utilisation CSV, so "regenerate one, forget the other" is two commands.
    """
    out = _out_dir(tmp_path)
    lines = UTIL.read_text(encoding="utf-8").splitlines(keepends=True)
    stale = [ln for ln in lines if ln.startswith("#") or ",16.2," not in ln]
    assert len(stale) < len(lines), "the rows this cell deletes are not in the committed CSV"
    csv = tmp_path / "stale_util.csv"
    csv.write_text("".join(stale), encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--util", str(csv))
    assert proc.returncode != 0, (
        "a utilisation table missing member-stations was accepted; the over-unity count "
        "and the ranked top ten are read from it (R967)."
    )
    assert "absent from the utilisations" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R968_an_AGREEING_SUBSET_does_not_publish_the_reference_paragraph(
    tmp_path: Path,
) -> None:
    """The height gate is satisfied by every npz this pipeline produces, so it gated nothing.

    `h_full` is a module-constant product here, so `h_full == _ref_h` is always true, and
    the branch had no reference to the period sets -- all 63 non-empty subsets reached the
    hand-written paragraph. Measured at two agreeing pairs at the committed height, both
    passing every join, both publishing "the largest of THE SIX" and "the FOUR periods
    EZ2 admits: the THREE in band".

    This pair agrees on both joins -- the sidecar and the forces table carry the same four
    periods, and dropping only the two sensitivity-only cases leaves all 32 utilisation
    member-stations intact -- so the predicate is the only thing under test.
    """
    out = _out_dir(tmp_path)
    keep = {"12.5", "14", "15", "16.2"}
    side = _sidecar(tmp_path, periods_full_s=[12.5, 14.0, 15.0, 16.2])
    forces = _subset_forces(tmp_path, keep)

    proc = _run(
        "f6_results_report.py", tmp_path, "--provenance", str(side), "--forces", str(forces)
    )
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    written = (out / "o.md").read_text(encoding="utf-8")

    assert "not the reference sea state" in written, (
        "a four-period run published the paragraph written for the six-period reference "
        "set. The paragraph is a set of claims about a height AND a case list (R968)."
    )
    assert "largest of the six" not in written
    assert "four periods EZ2 admits" not in written


def test_R969_a_DUPLICATED_period_is_refused(tmp_path: Path) -> None:
    """Sets were compared and a list was iterated, so one duplicate passed both directions.

    `set(_recorded)` equals `_solved` while `_recorded` has seven entries, giving a
    seven-row band table with `T = 10 s` twice above a six-row response table, and
    `Inside the band: [12.5, 14.0, 14.0, 15.0, 16.2]` on the computed branch.
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, periods_full_s=[10.0, 10.0, 12.5, 14.0, 15.0, 16.2, 20.0])
    proc = _run("f6_results_report.py", tmp_path, "--provenance", str(side))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "Declared more than once" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()
