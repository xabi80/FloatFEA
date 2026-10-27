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
import re
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


def test_R976_a_DUPLICATED_utilisation_row_is_refused(tmp_path: Path) -> None:
    """The R967 join compared a set; every published count reads the list.

    R969's defect, one function away, inside the repair for R967. One committed row
    repeated, forces and sidecar untouched:

        member-stations checked : 33   (true 32)
        in tension              : 16   (true 15)
        over unity              : 5 of 33   (true 4 of 32)

    numerator and denominator wrong in opposite directions, with
    `platform:hub3_arm ROOT 16.2` ranked at BOTH #3 and #4 and `hub4:buoy11_arm ROOT`
    pushed out of the published top ten, at exit 0.
    """
    out = _out_dir(tmp_path)
    lines = UTIL.read_text(encoding="utf-8").splitlines(keepends=True)
    body = [ln for ln in lines if not ln.startswith("#")]
    assert len(body) > 2, "the utilisation CSV has no data rows to duplicate"
    csv = tmp_path / "duplicated_util.csv"
    csv.write_text("".join([*lines, body[3]]), encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--util", str(csv))
    assert proc.returncode != 0, (
        "a repeated member-station was accepted; it inflates both halves of "
        "`over unity : N of M` and ranks one station twice (R976)."
    )
    assert "carries more than one row for" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R976_a_UTILISATION_ROW_WITH_NO_FORCES_ROW_is_refused(tmp_path: Path) -> None:
    """R967's condition (i) named EACH direction, and only one was held.

    `_util_extra` -- a utilisation row for a member-station the forces table does not
    screen -- was asserted by nothing.
    """
    out = _out_dir(tmp_path)
    lines = UTIL.read_text(encoding="utf-8").splitlines(keepends=True)
    body = [ln for ln in lines if not ln.startswith("#")]
    invented = body[3].split(",")
    invented[1] = "platform:not_a_member_arm"
    csv = tmp_path / "extra_util.csv"
    csv.write_text("".join([*lines, ",".join(invented)]), encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--util", str(csv))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "no forces row" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R976_a_UTILISATION_ROW_AT_A_WRONG_PERIOD_is_refused(tmp_path: Path) -> None:
    """R967's `_wrong_period` arm, which was also held by nothing."""
    out = _out_dir(tmp_path)
    lines = UTIL.read_text(encoding="utf-8").splitlines(keepends=True)
    rebased = []
    for ln in lines:
        if ln.startswith("#"):
            rebased.append(ln)
            continue
        cols = ln.split(",")
        if cols[3] not in ("period_full_s", ""):
            cols[3] = "99"
        rebased.append(",".join(cols))
    csv = tmp_path / "wrong_period_util.csv"
    csv.write_text("".join(rebased), encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--util", str(csv))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "no `total_instant` row for" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R977_a_SHIFTED_PERIOD_SET_does_not_publish_the_reference_paragraph(
    tmp_path: Path,
) -> None:
    """Both sides of the old predicate came from one argument's own default.

    `_reference` compared `args.provenance`'s height and periods against that argument's
    DEFAULT, re-read from a hard-coded path -- so on the default invocation it was
    `x == x`, and the reviewer ablated it to a byte-identical document. The consequence it
    let through, measured through the real generator: the sidecar regenerated to
    `[10, 12.5, 14, 15, 16.2, 25]` with one shipped `export_f4_dynamic_inputs.py --period`,
    an agreeing forces table and the height unchanged, published the hand-written
    paragraph naming `T = 20 s` TWICE over tables that both print `25.0`.

    **Which sea state a directive ruled on is a property of the directive**, so the
    reference is declared and cited rather than read from an input that cannot answer the
    question about itself.
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, periods_full_s=[10.0, 12.5, 14.0, 15.0, 16.2, 25.0])

    # the forces table relabelled to agree, so both joins pass and the predicate is the
    # only thing under test
    lines = FORCES.read_text(encoding="utf-8").splitlines(keepends=True)
    comments = [ln for ln in lines if ln.startswith("#")]
    body = [ln for ln in lines if not ln.startswith("#")]
    head, rows = body[0], body[1:]
    shifted = []
    for r in rows:
        cols = r.split(",")
        if cols[3] == "20":
            cols[3] = "25"
            r = ",".join(cols)
        shifted.append(r)
    forces = tmp_path / "shifted_forces.csv"
    forces.write_text("".join(comments) + head + "".join(shifted), encoding="utf-8")

    proc = _run(
        "f6_results_report.py", tmp_path, "--provenance", str(side), "--forces", str(forces)
    )
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    written = (out / "o.md").read_text(encoding="utf-8")

    assert "not the reference sea state" in written, (
        "a run whose period set is not the one FA0 and EZ2 ruled on published the "
        "paragraph written for that set (R977)."
    )
    assert (
        "T = 20 s" not in written
    ), "the hand-written paragraph names a period this run does not record."


def _flat(document: str) -> str:
    """The document with every whitespace run collapsed, so a needle cannot miss a WRAP.

    **R951's trap, closed rather than worked around.** A cell asserted
    `"is kept as the band's lower edge" in report` and the generator emitted that sentence
    across two lines, so the needle matched nothing and the cell passed whatever the code
    did. R986 and R987 turn hand-wrapped paragraphs into interpolated ones, which moves
    every line break in them, and a needle anchored on a break would be the same defect
    with a new cause. Markdown joins a paragraph's soft breaks, so this is the form a
    READER sees and the form an assertion should be taken in.
    """
    return " ".join(document.split())


# The forces table's own 0-based column indices, read off its header rather than typed
# twice: `body, member, station, period_full_s, basis, N, Vy, Vz, T, My, Mz, sigma_Pa,
# tau_Pa`. `COMPONENTS` is the six a stress is a function of, and scaling all six by one
# factor scales sigma EXACTLY by that factor, because both of `_stresses`' terms are
# homogeneous of degree one in the components.
_HEADER = [
    c
    for ln in FORCES.read_text(encoding="utf-8").splitlines()
    if not ln.startswith("#")
    for c in [ln.split(",")]
][0]
COMPONENTS = tuple(_HEADER.index(c) for c in ("N", "Vy", "Vz", "T", "My", "Mz"))
SIGMA_PA = _HEADER.index("sigma_Pa")
AXIAL = _HEADER.index("N")


def _scaled_forces(
    tmp: Path,
    basis: str | None,
    station: str | None,
    column: int | tuple[int, ...],
    factor: Any,
) -> Path:
    """The committed forces table with one or more columns scaled, everything else held.

    `basis` and `station` select the rows and `None` means every row; `column` is one
    0-based index or a tuple of them; `factor` is a number or a callable taking the row's
    period string. Body, member, station, period and basis are untouched, so every key and
    period join in the report stays green and the only thing that moves is a value.

    **R993: THE COLUMN SET IS A PARAMETER BECAUSE A DOCSTRING TABLE BELOW WAS MEASURED ON
    ALL SIX COMPONENTS WHILE THE CELL SCALED `N` ALONE.** Every row of that table belonged
    to a configuration the cell did not run -- BP0's shape one layer in: the figures were
    each correct against a rule, and the rule was not the one the code applied.
    """
    touch = (column,) if isinstance(column, int) else tuple(column)
    lines = FORCES.read_text(encoding="utf-8").splitlines(keepends=True)
    comments = [ln for ln in lines if ln.startswith("#")]
    body = [ln for ln in lines if not ln.startswith("#")]
    head, rows = body[0], body[1:]
    touched = 0
    out_rows: list[str] = []
    for ln in rows:
        cols = ln.rstrip("\r\n").split(",")
        if (basis is None or cols[4] == basis) and (station is None or cols[2] == station):
            f = factor(cols[3]) if callable(factor) else factor
            for c in touch:
                cols[c] = f"{float(cols[c]) * f:.6e}"
            touched += 1
            out_rows.append(",".join(cols) + chr(10))
        else:
            out_rows.append(ln)
    assert touched, f"no {basis} row at station {station} was scaled; the cell is vacuous"
    out = tmp / f"scaled_{basis}_{'_'.join(str(c) for c in touch)}.csv"
    out.write_text("".join(comments) + head + "".join(out_rows), encoding="utf-8")
    return out


def _bound_table(document: str) -> dict[float, float]:
    """The per-case stress bound AS PUBLISHED, parsed out of section 4's own block.

    The assertions below compare the document's sentences against the document's own
    table, not against the numbers the cell planted -- so they hold at any ordering rather
    than at the one ordering this cell happens to construct.
    """
    rows: dict[float, float] = {}
    inside = False
    for line in document.splitlines():
        if "worst ROOT sigma BOUND" in line:
            inside = True
            continue
        if inside:
            parts = line.split()
            if len(parts) != 2:
                break
            rows[float(parts[0])] = float(parts[1])
    assert rows, "section 4 publishes no stress-bound table"
    return rows


def _against_f_b(document: str) -> float:
    """Section 8(i)'s static-basis ratio AS PUBLISHED, out of its own block.

    Read rather than restated, for `_bound_table`'s reason: it is a function of the forces
    table this run was handed, so a cell that types it measures one table and silently
    stops tracking the run.
    """
    found = re.search(r"against F_b = [0-9.]+ MPa\s+: ([0-9.]+)", document)
    assert found, "section 8(i) publishes no `against F_b` ratio"
    return float(found.group(1))


def _band_edges(document: str) -> tuple[float, float]:
    """The associated-period band AS PUBLISHED, from section 4's own line.

    Read rather than restated: the band is a function of the recorded height (R902), so a
    cell that types its edges measures one sea state and silently stops tracking the run.
    """
    found = re.search(r"sqrt\(6\.5 H\) = ([0-9.]+) s\s+sqrt\(11 H\) = ([0-9.]+) s", document)
    assert found, "section 4 publishes no associated-period band line"
    return float(found.group(1)), float(found.group(2))


def test_R978_a_FORCES_TABLE_WHOSE_VALUES_DISAGREE_is_refused(tmp_path: Path) -> None:
    """The two tables were joined on keys and on periods, and never on a VALUE.

    s.6 publishes forces-derived stresses and s.7 publishes utilisation-derived counts with
    no comparison between them, so a forces table whose AXIAL column is scaled by 1.5 moved
    s.6 and left s.7 identical: `over unity : 4 of 32` and `worst U = 1.71167` published for
    a structure whose stresses are half again as large, at exit 0, every key and period
    join green.

    **R992: that sentence used to say "a forces table scaled by 1.5", which was false of
    the column this cell scales and exactly true of `sigma_Pa`** -- the one column the join
    cannot reach, because `utilisation_row` never reads it. Scaling `N` moves s.7 and IS
    refused here; the `sigma_Pa` channel is `test_R992_...` below.

    The join recomputes each published row through `api_wsd_utilisation.utilisation_row`
    and compares that module's own `csv_text` rendering, over the whole row dict rather
    than a column list written at the join -- so a column added to the producer and not
    joined here is impossible by construction.

    **NOT the sum of two independently rounded columns**, which cannot be made exact at
    any precision -- `2.25161 + 186.6500 = 188.9016` against a published `188.9022` -- and
    which is why this was escalated once as a choice between a comparison epsilon and a new
    CSV column. Neither arm was ever necessary.
    """
    out = _out_dir(tmp_path)
    forces = _scaled_forces(tmp_path, "total_instant", None, 5, 1.5)

    proc = _run("f6_results_report.py", tmp_path, "--forces", str(forces))
    assert proc.returncode != 0, (
        "a forces table whose axial column was scaled by 1.5 was accepted; s.7's "
        "over-unity count, worst station and ranked top ten would be published for forces "
        "that are not s.6's (R978)."
    )
    assert "does not carry the values" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R978_a_DUPLICATED_FORCES_ROW_is_refused(tmp_path: Path) -> None:
    """R976 from the other side: the expectation is read per key, so a repeat is ambiguous.

    The committed table carries exactly one `total_instant` row per
    `(member, station, period)` -- 48 keys, multiplicity 1 -- so no legitimately-produced
    table trips this.
    """
    out = _out_dir(tmp_path)
    lines = FORCES.read_text(encoding="utf-8").splitlines(keepends=True)
    instant = [ln for ln in lines if not ln.startswith("#") and ln.split(",")[4] == "total_instant"]
    assert instant, "the committed forces table carries no total_instant rows"
    csv = tmp_path / "duplicated_forces.csv"
    csv.write_text("".join([*lines, instant[0]]), encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--forces", str(csv))
    assert proc.returncode != 0, (proc.stdout + proc.stderr)[-700:]
    assert "more than one `total_instant` row for" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def test_R978_a_CHANGE_BELOW_THE_PUBLISHED_PRECISION_is_accepted(tmp_path: Path) -> None:
    """EH4's weakening direction: how far may a value move with this join still green?

    Solved rather than sampled, over the six components this cell itself scales --
    `_scaled_forces(..., COMPONENTS, ...)`, which writes each component back at the CSV's
    own `.6e`, with the join's own refusal line read for the count:

        x (1 + 1e-8)  ->   0 of 736 cells differ   <- accepted here
        x (1 + 1e-7)  ->   8 of 736
        x (1 + 1e-5)  -> 384 of 736, and it SATURATES there

    `384` is every cell that is a function of the forces row; the other `352` are the five
    key columns, the three branch/clause labels and the two allowables, none of which a
    forces value can move. **The blind band below `1e-8` is not a tolerance and no number
    was introduced for it:** it is `_CSV_FIGURES`, which the producer's own docstring
    declares as the precision any count taken from that file is measured at. A join at a
    precision the publication does not carry would not be checkable by its reader.

    **R993: THE TABLE USED TO BE MEASURED ON ALL SIX AND THE CELL USED TO SCALE `N`
    ALONE**, which gives `0 / 0 / 82` -- every published row belonging to a configuration
    this cell did not run, and the saturation claim wrong by a factor of 4.7 for it. The
    cell now runs the configuration the table describes.

    **AND THE CHANNEL IS NAMED BECAUSE THE 1e-7 ROW DEPENDS ON IT.** The reviewer measured
    `13 of 736` for all six and `8` is what this path gives, because writing a component
    back at `.6e` truncates part of a perturbation that small. Neither figure is wrong;
    `8` is the one this cell's own injection produces, and R993 is exactly the defect of
    publishing the other one here.
    """
    out = _out_dir(tmp_path)
    forces = _scaled_forces(tmp_path, "total_instant", None, COMPONENTS, 1.0 + 1e-8)
    proc = _run("f6_results_report.py", tmp_path, "--forces", str(forces))
    assert proc.returncode == 0, (
        "a change below the precision the CSV publishes was refused, which would make the "
        "join a comparison at a precision no reader of the file can take (R978)."
    )
    assert (out / "o.md").exists()


def test_R986_the_BOUND_SENTENCES_follow_the_BOUND_TABLE(tmp_path: Path) -> None:
    """Three of the paragraph's seven claims are about a quantity the gate does not read.

    `_reference` compares the height and the recorded period set; the per-case stress bound
    comes from `--forces`, an independent input it does not touch. One variable moved --
    the `total_max` ROOT `sigma_Pa` values scaled per period, every key, period, basis and
    other column identical, so every join stays green and the argmax MEMBER at each period
    is unchanged -- and the document published, at exit 0, on the REFERENCE branch:

        10.0  299.983   <- the SMALLEST     "it is also the largest of the six"
        16.2  599.991   <- the LARGEST      "the bound falls monotonically as `T` rises"
        20.0  400.021   <- BELOW 16.2       "`T = 20 s` ticks back up above `T = 16.2 s`"

    three false sentences directly above the table that contradicts them. There is NO value
    of the bound that trips `_reference`, so a fourth conjunct is not the repair -- and the
    same claim had a duplicate in s.8(iv) at four-space indent, outside both branches of
    that gate, which a conjunct could not have reached at all.

    Every assertion is taken against the table THE SAME RUN PUBLISHED, so the cell holds at
    any ordering rather than at the one it plants.
    """
    # **THE CHANNEL MOVED WITH R992's REPAIR, AND THIS CELL WOULD OTHERWISE HAVE GONE
    # VACUOUS WHILE STAYING GREEN.** It used to plant the bound by scaling the `sigma_Pa`
    # COLUMN -- the column R992 took out of this generator's hands. Section 4's bound is
    # derived from each row's own six components now, so scaling that column moves nothing
    # and the cell would have measured the SHIPPED ordering while asserting against a
    # planted one. It plants the six components, which scales the bound by exactly their
    # factor, and the pre-planting figures come from a CONTROL RUN rather than from a
    # recomputation here.
    before = _bound_table(_control(tmp_path))
    assert len(before) >= 3, before

    # Targets that RISE with T across the band and do NOT tick back up past the long edge
    # -- the inverse of all three sentences.
    order = sorted(before)
    targets = {p: 300.0 + 50.0 * n for n, p in enumerate(order)}
    targets[order[-1]] = 400.0
    raw, written = _planted_report(tmp_path, targets)
    published = _bound_table(raw)
    # **THE ARGMAX AND THE BAND EDGES ARE BOTH READ, NOT TYPED.** The first version of
    # this cell compared against `10.0` and against `12.542 .. 16.316`, and
    # `test_no_undeclared_tolerance_reaches_a_comparison` was red on all three -- correctly,
    # because they are sea-state quantities and a cell that restates them stops tracking
    # the run the moment the height moves, which is R902's defect inside a test. The
    # pre-planting argmax comes from the CONTROL RUN's own published table, and the band
    # comes from the planted run's OWN published edges.
    argmax_before = max(before, key=lambda T: before[T])
    top = max(published, key=lambda T: published[T])
    assert top != argmax_before, (
        f"the planted bound did not move the argmax off T = {argmax_before:g} s, so this "
        f"cell is measuring the shipped ordering and not a reordering."
    )
    lo, hi = _band_edges(raw)
    band = [published[T] for T in sorted(published) if lo <= T <= hi]
    assert len(band) >= 2 and band == sorted(band) and band[0] < band[-1], (band, lo, hi)

    # (1) the argmax, as the sentence states it -- and at BOTH sites, which is why the
    # count is taken over the whole document rather than over section 4.
    assert "largest of the six" not in written, (
        f"the document calls the breaking case the largest of the six while its own table "
        f"puts the largest at T = {top:g} s ({published[top]:.3f} MPa) (R986)."
    )
    assert (
        f"MPa at `T = {top:g} s`" in written
    ), "the published rank does not name the period the table's own argmax is at."
    assert written.count("ranks 6 of 6") == 2, (
        "the rank is published at section 4 AND at section 8(iv); 8(iv) sits outside both "
        "branches of `_reference`, which is R986's condition (iii)."
    )

    # (2) the monotonicity, in the direction the table shows.
    assert "falls monotonically" not in written, (
        f"the document states the bound falls across the band while its own table rises: "
        f"{band} (R986)."
    )
    assert "rises monotonically" in written
    assert "the lower edge is NOT what governs on this bound" in written

    # (3) the comparison past the long edge.
    assert "does not tick back up" in written
    assert "The trend reverses past the long edge" not in written

    # s.8(iv): the direction word is gone and the measured relation is what is published.
    assert "expensive direction" not in written
    assert "retains the largest bound in the recorded set" in written


def test_R987_the_LIMITATIONS_BLOCK_names_the_RECORDED_heading(tmp_path: Path) -> None:
    """The heading was a literal in the block a reader consults for what the run covers.

    One field moved, `heading_deg` 0.0 -> 90.0, every other input committed: EXIT 0, the
    reference branch -- because `_reference` does not read the heading -- and one document
    publishing `heading : 90.0 deg` in s.4 and "one heading, 0 deg" in s.2, seventy-five
    lines apart. Every member force, stress and utilisation in s.6 and s.7 is a function of
    the heading that was run, which s.8(iii) says in as many words.
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, heading_deg=90.0)
    proc = _run("f6_results_report.py", tmp_path, "--provenance", str(side))
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    written = _flat((out / "o.md").read_text(encoding="utf-8"))

    assert "one heading, 0" + chr(176) not in written, (
        "s.2 states heading 0 deg for a run whose s.4 publishes 90.0 deg from the same "
        "sidecar (R987)."
    )
    assert "one heading, 90" + chr(176) in written
    assert "heading : 90.0 deg" in written
    assert "Only heading 90" + chr(176) + " has been run" in written
    assert "Only 90" + chr(176) + " is run" in written


def test_R987_the_CASE_COUNT_in_prose_follows_the_RECORDED_set(tmp_path: Path) -> None:
    """A count in prose was a literal UPSTREAM of the R977 branch, at three sites.

    The recorded set trimmed to five with the forces table agreeing: EXIT 0, s.4 correctly
    takes the NON-reference branch -- the R977 repair working exactly as built -- while the
    counts in s.2 and s.9 sat above the document's own five-row band table.
    """
    out = _out_dir(tmp_path)
    side = _sidecar(tmp_path, periods_full_s=[10.0, 12.5, 14.0, 15.0, 16.2])
    forces = _subset_forces(tmp_path, {"10", "12.5", "14", "15", "16.2"})
    proc = _run(
        "f6_results_report.py", tmp_path, "--provenance", str(side), "--forces", str(forces)
    )
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    raw = (out / "o.md").read_text(encoding="utf-8")
    written = _flat(raw)

    assert "not the reference sea state" in written
    assert "Six periods" not in written, "a five-period run published a count of six (R987)."
    assert "Six regular waves" not in written
    assert "Five periods at a single wave height" in written
    assert "Five regular waves with no return period" in written
    assert len(_bound_table(raw)) == 5


def test_R986_a_RECORDED_PERIOD_WITH_NO_BOUND_ROW_is_refused(tmp_path: Path) -> None:
    """The denominator the bound sentences count is the bound table's, not the sidecar's.

    A `total_max` ROOT row missing for one recorded period leaves every other join green --
    the period is still SOLVED, because the other five bases carry it -- and shrinks
    `len(_bound_mpa)` by one. The paragraph beneath then counts the bound table while the
    band table above it counts the sidecar: "the largest of the five" over a six-row table.
    The same wrong-denominator shape as R976, one table along, and found while repairing
    R986 rather than by a cell that existed.
    """
    out = _out_dir(tmp_path)
    lines = FORCES.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, dropped = [], 0
    for ln in lines:
        cols = ln.split(",")
        if (
            not ln.startswith("#")
            and len(cols) > 4
            and cols[4] == "total_max"
            and cols[2] == "ROOT"
            and cols[3] == "16.2"
        ):
            dropped += 1
            continue
        kept.append(ln)
    assert dropped, "no total_max ROOT rows at 16.2 s in the committed table"
    csv = tmp_path / "no_bound_row.csv"
    csv.write_text("".join(kept), encoding="utf-8")

    proc = _run("f6_results_report.py", tmp_path, "--forces", str(csv))
    assert proc.returncode != 0, (
        "a recorded period with no stress-bound row was accepted; the paragraph counts "
        "the bound table and the band table above it counts the sidecar (R986)."
    )
    assert "carries no `total_max` ROOT row for" in proc.stdout + proc.stderr
    assert not (out / "o.md").exists()


def _control(tmp: Path) -> str:
    """The report as the COMMITTED inputs produce it, run here rather than read.

    Every assertion that compares a planted run against the unplanted one needs the
    unplanted figures, and reading them out of `results/F6/` would make the cell a
    comparison against a file the same commit can edit. A real process, in its own
    directory so it cannot collide with the planted run's `o.md`.
    """
    here = tmp / "control"
    here.mkdir(exist_ok=True)
    if not (here / "o.md").exists():
        proc = _run("f6_results_report.py", here)
        assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    return (here / "o.md").read_text(encoding="utf-8")


def _band_rows(document: str) -> dict[float, list[str]]:
    """Section 4's associated-period band table, one split row per recorded period.

    The membership and breaking claims below are about sets this document publishes, so the
    cells read the published rows rather than restating `GOVERNING_PERIODS` or re-running
    the steepness test -- either would compare one source against itself (R977).
    """
    rows: dict[float, list[str]] = {}
    inside = False
    for line in document.splitlines():
        if "edge offset" in line and "basis" in line:
            inside = True
            continue
        if inside:
            parts = line.split()
            if len(parts) < 6:
                break
            rows[float(parts[0])] = parts
    assert rows, "section 4 publishes no associated-period band table"
    return rows


def _published_basis(document: str) -> dict[float, str]:
    """Which periods THIS DOCUMENT marks `GOVERNING`, from its own band table."""
    return {T: parts[-1] for T, parts in _band_rows(document).items()}


def _published_breaking(document: str) -> list[float]:
    """Which periods THIS DOCUMENT marks `BREAKING`, from its own band table."""
    return sorted(T for T, parts in _band_rows(document).items() if "BREAKING" in parts)


def _planted_bound(tmp: Path, targets_mpa: dict[float, float], control: str) -> Path:
    """A forces table whose per-case stress BOUND is the given per-period MPa values.

    The factor per period is `target / published`, where `published` is the CONTROL run's
    own bound table -- not a recomputation here, which would be a second copy of
    `_stresses` (R983), and not the `sigma_Pa` column, which R992 takes out of this
    generator's hands entirely. All six components are scaled by one factor, which scales
    the bound by exactly that factor, so the argmax MEMBER within each period is unchanged
    and the only thing that moves is the ordering the sentences are about.
    """
    published = _bound_table(control)
    assert set(published) == set(targets_mpa), (sorted(published), sorted(targets_mpa))
    return _scaled_forces(
        tmp,
        "total_max",
        "ROOT",
        COMPONENTS,
        lambda p: targets_mpa[float(p)] / published[float(p)],
    )


def _planted_report(tmp: Path, targets_mpa: dict[float, float]) -> tuple[str, str]:
    """`(raw, flattened)` for a run at a planted bound ordering, on the REFERENCE branch."""
    out = _out_dir(tmp)
    control = _control(tmp)
    forces = _planted_bound(tmp, targets_mpa, control)
    proc = _run("f6_results_report.py", tmp, "--forces", str(forces))
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    raw = (out / "o.md").read_text(encoding="utf-8")
    assert "not the reference sea state" not in raw, (
        "these cells hold the sea state and move only the bound, so the REFERENCE branch "
        "is the one that must be under test."
    )
    # **WHAT IS ASSERTED IS THE ORDERING, NOT THE TARGET VALUE, AND THAT IS NOT AN
    # EPSILON IN DISGUISE.** The targets are a construction device: the components are
    # written back at the CSV's own `.6e`, so a factor of 2.66 lands the bound on
    # `900.001` where `900.000` was asked for. Every assertion in these cells reads the
    # table the run PUBLISHED, and what each one is about is which period carries which
    # rank -- so the ordering is the postcondition the planting has to meet, and the
    # targets are 100 MPa apart, which no rounding at the sixth figure can cross.
    published = _bound_table(raw)
    assert sorted(published, key=lambda T: published[T]) == sorted(
        targets_mpa, key=lambda T: targets_mpa[T]
    ), (published, targets_mpa)
    return raw, _flat(raw)


def test_R991_the_LOWER_EDGE_CONCLUSION_follows_the_GOVERNING_BOUNDS(tmp_path: Path) -> None:
    """`_band_dir` was measured over `_in_band` and decided a sentence about `T = 12.5 s`.

    **The series the premise is measured over EXCLUDES the case the conclusion is about.**
    `_in_band` is `[14, 15, 16.2]` on the reference branch by construction and the kept
    lower edge is `12.5`, so "across the band the bound falls monotonically as `T` rises,
    so the lower edge is what governs and this case is the one that represents it" drew a
    claim about one period from a direction measured over three others.

    One variable moved -- the per-case bound, every key, period, basis and station held --
    and at this ordering the document published that sentence over its own table, in which
    `T = 12.5 s` at 100.000 MPa is the SMALLEST of the four the same document marks
    GOVERNING. The direction word was correctly measured. The conclusion was not.

    The conclusion is read off the governing periods' own bounds from here on, which is
    ONE claim covering all four of `_monotonic_word`'s return values rather than a branch
    on one of them -- so this cell asserts the premise and the conclusion DISAGREE, which
    the repaired generator can say and the old one could not.
    """
    raw, written = _planted_report(
        tmp_path, {10.0: 900.0, 12.5: 100.0, 14.0: 500.0, 15.0: 400.0, 16.2: 300.0, 20.0: 200.0}
    )
    published = _bound_table(raw)
    lo, hi = _band_edges(raw)
    interior = [T for T in sorted(published) if lo <= T <= hi]
    band = [published[T] for T in interior]
    governing = {T: published[T] for T, b in _published_basis(raw).items() if b == "GOVERNING"}
    lower = min(governing)

    # The premise, as the table shows it: the band's interior falls.
    assert len(band) >= 2 and band == sorted(band, reverse=True) and band[0] > band[-1], band
    assert "falls monotonically" in written

    # The conclusion, about the kept lower edge: it is the SMALLEST governing bound, so it
    # is not what governs -- and the premise above would have said the opposite.
    assert lower not in interior, (
        f"T = {lower:g} s is inside the published band, so this cell is not measuring the "
        f"case the conclusion is about."
    )
    assert governing[lower] == min(governing.values()), governing
    assert "the lower edge is NOT what governs on this bound" in written, (
        f"the document says the lower edge governs while its own table puts "
        f"T = {lower:g} s at {governing[lower]:.3f} MPa, the smallest of the governing "
        f"{sorted(governing.values())} (R991)."
    )
    # And the series the direction word is measured over is NAMED, so a reader can tell
    # that it excludes the case the next clause is about.
    assert f"in-band rows alone, which do not include `T = {lower:g} s`" in written


def test_R991_the_MEMBERSHIP_CONCLUSION_follows_the_GOVERNING_SET(tmp_path: Path) -> None:
    """`_ex_rank == 1` decided whether the governing SET contains the recorded argmax.

    The rank of the EXCLUDED breaking case and the membership of the argmax coincide only
    when that argmax is either the breaking case or a governing period. `_past_long` is a
    third possibility and neither branch covered it: at this ordering the largest bound
    belongs to `T = 20 s`, which the same document marks `sensitivity`, and section 8(iv)
    published "so the governing basis RETAINS the largest bound in the recorded set".

    **That states the conservatism of the governing basis backwards**, which is the defect
    R986 named at this exact site, with the direction word removed and the error kept. It
    is the second of EH4's two directions on this sentence: the first cell makes the
    premise and the conclusion disagree, this one puts the argmax where neither old branch
    could describe it.
    """
    raw, written = _planted_report(
        tmp_path, {10.0: 400.0, 12.5: 380.0, 14.0: 360.0, 15.0: 350.0, 16.2: 340.0, 20.0: 900.0}
    )
    published = _bound_table(raw)
    basis = _published_basis(raw)
    top = max(published, key=lambda T: published[T])
    breaking = _published_breaking(raw)

    # The state: the argmax is neither the breaking case nor a governing period.
    assert basis[top] != "GOVERNING", (top, basis)
    assert breaking and top not in breaking, (top, breaking)

    assert "retains the largest bound in the recorded set" not in written, (
        f"the document calls the governing basis conservative while its own band table "
        f"marks the argmax T = {top:g} s ({published[top]:.3f} MPa) as {basis[top]} "
        f"(R991)."
    )
    assert (
        f"leaves out the largest bound in the recorded set, which is at `T = {top:g} s`" in written
    )
    # The rank clause is still read off the whole recorded set, and it is NOT the clause
    # that decides membership: the breaking case is second here, not first. The rank is
    # counted over the PUBLISHED table, so the assertion reads the artifact.
    assert published[breaking[0]] < published[top], (published, breaking, top)
    rank = 1 + sum(1 for v in published.values() if v > published[breaking[0]])
    assert f"it ranks {rank} of {len(published)} —" in written


def test_R991_a_NON_MONOTONIC_BAND_can_still_have_the_LOWER_EDGE_GOVERNING(
    tmp_path: Path,
) -> None:
    """EH4's weakening direction on the same sentence, and the third of four words.

    `_monotonic_word` returns four strings and the old `_governs_text` branched on one of
    them, so "is not monotonic" and "has too few cases to be monotonic" both routed to the
    strong negative claim -- "the lower edge is NOT what governs on this bound, and FA0's
    reason for keeping this case is not reproduced at it." At this ordering the band's
    interior is not monotonic AND the kept lower edge carries the largest governing bound,
    so the negative claim is false in the opposite direction from the first cell's.

    This is the cell that shows the two are decoupled: the word is published as a
    measurement over the band's interior and the conclusion comes from the governing
    bounds, so all four words route to a claim that follows from them.
    """
    raw, written = _planted_report(
        tmp_path, {10.0: 900.0, 12.5: 600.0, 14.0: 300.0, 15.0: 500.0, 16.2: 200.0, 20.0: 100.0}
    )
    published = _bound_table(raw)
    lo, hi = _band_edges(raw)
    band = [published[T] for T in sorted(published) if lo <= T <= hi]
    governing = {T: published[T] for T, b in _published_basis(raw).items() if b == "GOVERNING"}
    lower = min(governing)

    # The premise: not monotonic in either direction, and measured over at least two rows,
    # so the fourth word ("has too few cases") is not what is under test here.
    assert len(band) >= 2 and band != sorted(band) and band != sorted(band, reverse=True), band
    assert "is not monotonic" in written
    assert "has too few cases to be monotonic" not in written

    # The conclusion, the other way from the first cell: the lower edge IS the governing
    # argmax, so the negative claim the old branch would have published is refused.
    assert governing[lower] == max(governing.values()), governing
    assert "the lower edge is NOT what governs on this bound" not in written, (
        f"a non-monotonic band published the negative claim while its own table puts the "
        f"kept lower edge T = {lower:g} s at {governing[lower]:.3f} MPa, the largest of "
        f"the governing {sorted(governing.values())} (R991)."
    )
    assert "so the lower edge is what governs on this bound" in written


def test_R992_the_BOUND_and_the_STATIC_FIGURE_follow_the_COMPONENTS(tmp_path: Path) -> None:
    """`sigma_Pa` was the one input to two published figures and was joined to nothing.

    R978's join recomputes all 23 utilisation columns through the producer's own row dict
    and `sigma_Pa` is in none of them, because `api_wsd_utilisation.py` reads the six
    components and never that column. `grep -rn sigma_Pa tests/` found one hit and it was
    prose in a docstring. So: scaled by 1.5 with the six components, every key, period and
    basis held, the generator exited 0 and published section 4's six-row bound table 50%
    high and `against F_b : 1.5195` where the components give `1.0130`; at 0.6 the same
    figure read `0.6078`, UNDER UNITY, beneath "**(i) The stand-in section governs**".
    Section 7 was byte-identical both ways, and re-running the utilisation producer on the
    doctored table gives a byte-identical CSV, so the 736-cell join is green BY
    CONSTRUCTION there rather than by luck.

    **Both directions, and both halves.** The two `sigma_Pa` arms assert the published
    figures do NOT follow that column; the two component arms assert they DO -- without
    which the first two would be satisfied by a generator that published a constant. The
    repair is one definition and NOT an epsilon: recomputing the column and comparing
    strings at the forces table's own `.6e` differs on 303 of 1248 rows, so the
    exact-string route R978 took is measured unavailable on this channel.
    """
    control = _control(tmp_path)
    before_bound = _bound_table(control)
    before_ratio = _against_f_b(control)

    for n, factor in enumerate((1.5, 0.6)):
        here = tmp_path / f"sigma_{n}"
        here.mkdir()
        forces = _scaled_forces(here, None, None, SIGMA_PA, factor)
        proc = _run("f6_results_report.py", here, "--forces", str(forces))
        assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
        raw = (here / "o.md").read_text(encoding="utf-8")
        assert _bound_table(raw) == before_bound, (
            f"section 4's stress bound followed `sigma_Pa` x {factor}, a column nothing in "
            f"this repository compares against anything (R992)."
        )
        assert _against_f_b(raw) == before_ratio, (
            f"section 8(i)'s static-basis utilisation followed `sigma_Pa` x {factor}; at "
            f"0.6 that figure goes under unity beneath a heading that says the section "
            f"governs (R992)."
        )

    # And the other direction: a COMPONENT moving must move both figures, or the two
    # assertions above would hold for a generator that published a constant.
    bound_dir = tmp_path / "components_bound"
    bound_dir.mkdir()
    forces = _scaled_forces(bound_dir, "total_max", "ROOT", COMPONENTS, 1.5)
    proc = _run("f6_results_report.py", bound_dir, "--forces", str(forces))
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    moved = _bound_table((bound_dir / "o.md").read_text(encoding="utf-8"))
    assert all(moved[T] > before_bound[T] for T in before_bound), (moved, before_bound)

    static_dir = tmp_path / "components_static"
    static_dir.mkdir()
    forces = _scaled_forces(static_dir, "static", "ROOT", COMPONENTS, 1.5)
    proc = _run("f6_results_report.py", static_dir, "--forces", str(forces))
    assert proc.returncode == 0, (proc.stdout + proc.stderr)[-700:]
    assert _against_f_b((static_dir / "o.md").read_text(encoding="utf-8")) > before_ratio


def test_R994_a_UNION_OF_HEADINGS_is_refused_rather_than_published_as_ONE(
    tmp_path: Path,
) -> None:
    """Five sentences in this document state ONE heading, and the count was a literal.

    The header block's "-- ONE heading only", s.2's "Regular design waves at one heading",
    s.8(iii)'s "Only heading 0 degrees has been run", s.9 item 3's "Only 0 degrees is run"
    and the limitations block all assert the same count, and four of them reach the value
    through `float(run['heading_deg'])`, which raises on a sequence. **So interpolating the
    count at the header alone would have been a branch no configuration the rest of the
    file survives can reach**, and writing a refusal into the generator for it would have
    been dead code of a second kind: `floatfea/run/pipeline.py:793-806` ALREADY refuses a
    non-scalar `run.heading_deg`, by name, at `main()`'s `wave_basis_from_sidecar` call 262
    lines above the header block -- and for this exact reason, in its own words, "Coercing
    either would publish `[0.0, 45.0] deg` or `[0.0, 45.0] m` in all three artifacts, which
    is what this refusal replaces."

    **So the count was already correct by construction, and what was missing was this
    cell.** Nothing in the repository connected that refusal to the five sentences it is
    what makes true -- which is why two repairs got written for a defect that had a guard:
    the guard was cited by nothing a reader of those sentences would find.

    FT2.6's union of headings is the configuration that makes all five false at once, and
    it is two steps away. What it needs is an envelope definition, not a prose edit.
    """
    side = _sidecar(tmp_path, heading_deg=[0.0, 45.0])
    proc = _run("f6_results_report.py", tmp_path, "--provenance", str(side))
    assert proc.returncode != 0, (
        "a sidecar recording two headings was accepted; the document would state ONE "
        "heading at five sites for a run that covered two, with every force, stress and "
        "utilisation in s.6 and s.7 a function of which (R994)."
    )
    blob = proc.stdout + proc.stderr
    assert "`run.heading_deg` is [0.0, 45.0] (list), not a number" in blob, blob[-700:]
    assert "in all three artifacts" in blob, blob[-700:]
    assert _wrote_nothing(tmp_path)
