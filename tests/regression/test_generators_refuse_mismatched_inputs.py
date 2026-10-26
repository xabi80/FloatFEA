"""The deliverable generators, driven as real processes (R933).

**NOTHING IN `tests/` INVOKED ANY OF THEM, AND NOTHING NAMED R907 OR R909.** Measured at
`e645e38`: `grep -rl R907 tests/` and `grep -rl R909 tests/` were both empty, and the only
references to the three generators were corpus prose and two tests that import one of them
for its symbols. Every finding from R896 onward was a check one publisher did not use, and
the reason the same shape recurred eight times is that the publishers were never run.

The cells are cheap because every refusal fires before `build_superstructure()`:

    f6_results_report.py       exit=1    0.63 s
    member_forces_table.py     exit=1    0.49 s

against the twenty minutes a full generator run costs. So each mutation gets its own
subprocess and the whole file is seconds.

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


def _sidecar(tmp: Path, **run_fields: Any) -> Path:
    """The committed sidecar with `run` fields overridden, written beside nothing."""
    recorded = json.loads(SIDECAR.read_text(encoding="utf-8"))
    recorded["run"].update(run_fields)
    out = tmp / "mutated.provenance.json"
    out.write_text(json.dumps(recorded, indent=1), encoding="utf-8")
    return out


def _out_dir(tmp: Path) -> Path:
    """A writable output directory UNDER `ROOT`, because one generator insists on it.

    `member_forces_table.py` ends with `args.out.relative_to(ROOT)`, so a path outside the
    repository raises AFTER both files are written (R918, ledger). `scratch/` is
    gitignored, and each cell gets its own subdirectory named for the pytest tmp it
    shadows, so concurrent cells cannot collide.
    """
    out = ROOT / "scratch" / f"r933_{tmp.name}"
    out.mkdir(parents=True, exist_ok=True)
    return out


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
    assert "has no solved case for" in proc.stdout + proc.stderr
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
