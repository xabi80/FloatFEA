"""Every counter-case is INJECTED, proved by TWO cells that must both fire (BX0).

THE EIGHTH GUARD, MADE GENERIC. `RESULTANT_EXACTNESS` once shipped with
`ceiling < counter` as its only guard -- two literals compared in
`tolerances.py` -- and could be widened a hundredfold with the suite green. BG1
answered that case by injecting the defect. Twice since, a counter was written
that asserts *itself* instead: R163 (`40 * ulp(CD) / ulp(CD) > 4`) and, one round
later in the commit that fixed R163, R173 (`10 > 4`).

A counter has to have two properties, and each cell here tests exactly one:

    GATE CELL      it RUNS the assertion it defends -- replace that assertion
                   with a no-op and the counter must fail;
    CEILING CELL   it is SIZED BY the constant it defends -- widen the ceiling
                   past the counter's declared injection and the counter must
                   fail.

**NEITHER CELL ALONE IS THE GUARD, and both mistakes are in this repository's
history.** The first version of this file had only the ceiling cell, set to
`inf` (R182): a degenerate counter is precisely one shaped `assert value >
CEILING`, so raising the ceiling made *that* comparison fail too and the cell
read the failure as injection -- R163's and R173's bodies were admitted. The
second version had only the gate cell (R197): a counter that calls its gate but
injects a 100% relative error where the constant says N ULP runs the gate
faithfully and is sized by nothing, so it passed, and `DELTA_CALIBRATION_ULP`
could be widened from `4.0` to `1e9` with it green.

Conjoined, each defect is rejected by the cell the other admits, and that is not
a claim here -- it is `CONTROLS` below, three defective bodies carried as
negative controls, each asserted to be rejected by ITS cell and admitted by the
other. Delete either cell and a control turns green.

WHAT THE PAIR STILL DOES NOT COVER, said so it is not trusted past its reach:

* the gate cell replaces the gate by name in the gate's own module, so a counter
  that reimplements its gate's comparison inline rather than calling it would
  pass that cell -- it is then the ceiling cell's job, and a body that does both
  (reimplements the comparison AND is sized by the constant) is a correct
  counter written the long way, not a defect;
* the ceiling cell proves the counter's injection is above the ceiling and no
  more than `WIDEN` times it. It does not prove the injection is the SMALLEST
  such value; that is what each constant's own Reason paragraph states, with the
  measured boundary beside it;
* both cells are per-counter. A constant with no counter registered here is not
  covered at all, which is what `test_there_is_something_to_check` is for.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests" / "verification" / "rung1"))
sys.path.insert(0, str(ROOT / "tests" / "regression"))

import test_corpus_configurations as CORPUS  # noqa: E402
import test_exempt_pair_responses as GOLDEN  # noqa: E402
import test_rigid_body_modes as RIGID  # noqa: E402

# not-a-tolerance: how far past the counter's own declared injection the ceiling
# cell widens. Nothing is accepted or rejected by comparison with it -- it is a
# deliberate over-widening, and any factor above one exercises the cell. Ten is
# used so the widened ceiling is unmistakably clear of the injection.
WIDEN = 10.0


class _Capsys:
    """The one fixture the registered gates take, supplied without pytest."""

    @staticmethod
    def disabled():
        import contextlib

        return contextlib.nullcontext()


REGISTERED = [
    (
        "calibration ULP",
        CORPUS.test_a_LARGER_deviation_fails_the_calibration,
        CORPUS,
        "test_the_delta_measure_is_CALIBRATED",
        "DELTA_CALIBRATION_ULP",
        WIDEN * CORPUS.DELTA_CALIBRATION_ULP_COUNTER,
    ),
    (
        "exempt-response drift",
        GOLDEN.test_a_MOVED_response_is_caught,
        GOLDEN,
        "test_every_recorded_pair_is_still_detected",
        "EXEMPT_RESPONSE_DRIFT_ULP",
        WIDEN * GOLDEN.EXEMPT_RESPONSE_DRIFT_ULP_COUNTER,
    ),
    # `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` -- THE EXEMPTION IS GONE (R183). It
    # was listed as unregisterable "because its gate compares inline across 296
    # parametrised cases", which named the wrong gate: this constant's gate is
    # the headroom assertion, a single test. Registering it found a THIRD
    # instance of R163's defect -- a counter comparing two constants -- which is
    # what this file exists to find.
    #
    # Its injection is a FACTOR on the measured ratio, not an offset in the
    # ceiling's units, so the widened ceiling is that factor times the ceiling:
    # the counter multiplies the shipped defect by `RAISED_COUNTER_DEFECT_FACTOR`
    # and a headroom that many times wider absorbs the raised ratio whatever the
    # clean ratio is.
    (
        "counter-defect size",
        lambda: CORPUS.test_a_RAISED_counter_defect_breaks_that(_Capsys),
        CORPUS,
        "test_the_counter_DEFECT_SIZE_cannot_be_raised",
        "PATCH_TEST_COUNTER_HEADROOM",
        WIDEN * CORPUS.RAISED_COUNTER_DEFECT_FACTOR * CORPUS.PATCH_TEST_COUNTER_HEADROOM,
    ),
    # G2.1 / V1.1, both halves. These two counters inject ONE defect -- a
    # diagonal stiffness resisting a rigid translation -- because that single
    # defect must redden both halves of the gate: it lifts a zero eigenvalue and
    # it takes that translation out of the computed span.
    #
    # Their widened ceilings are MEASURED rather than typed. The injection is a
    # defect SIZE, not an offset in the ceiling's units, so how far it lifts the
    # measured quantity is a property of the frame; `counter_response` returns it
    # at this commit. A literal here would be stale the first time the frame
    # moved, which is the species step 4 spent five rounds on.
    # THE RATIO PAIR IS GONE FROM THIS REGISTRY (Q7). Its gate is a diagnostic
    # now -- printed, asserted against nothing -- and a counter registered
    # against a gate that does not assert cannot redden it. Both cells here
    # failed at the commit that retired it, which is this meta-test doing
    # exactly its job: it noticed that a counter had lost the assertion it
    # defended before any reader did.
    (
        "rigid-body residual exactness",
        lambda: RIGID.test_a_RESISTED_rigid_motion_reddens_the_RESIDUAL(_Capsys),
        RIGID,
        "test_the_rigid_body_vectors_are_EXACT_in_the_residual",
        "RIGID_MODE_EXACTNESS",
        WIDEN * RIGID.counter_response("residual"),
    ),
    # BOTH RIGID-BODY SPECTRAL COUNTERS REDDEN ONE ASSERTION (CT0), because
    # `RIGID_MODE_FLOOR` and `RIGID_MODE_GAP` enter one bound
    # multiplicatively: `lambda_7 >= tau * 10**GAP`. Each is sized on its own
    # constant's meaning -- the first puts `lambda_7` AT the floor, the second
    # leaves it above the floor but under the separation -- and each widened
    # value is what that constant would have to become for its own defect to
    # go unnoticed.
    #
    # THE GAP'S WIDENED VALUE IS A LOGARITHM, so widening it means SUBTRACTING
    # rather than dividing. `WIDEN` is a ratio; `log10(WIDEN)` is the same
    # move in orders. Dividing a value in orders by a ratio is the R404
    # mistake one file over.
    (
        "rigid-body seventh at the floor",
        lambda: RIGID.test_a_SEVENTH_MODE_AT_THE_FLOOR_reddens_the_gate(_Capsys),
        RIGID,
        "test_there_is_NO_SEVENTH_zero_mode",
        "RIGID_MODE_FLOOR",
        RIGID.RIGID_MODE_FLOOR / WIDEN,
    ),
    (
        "rigid-body seventh too close",
        lambda: RIGID.test_a_SEVENTH_MODE_TOO_CLOSE_TO_THE_FLOOR_reddens_the_gate(_Capsys),
        RIGID,
        "test_there_is_NO_SEVENTH_zero_mode",
        "RIGID_MODE_GAP",
        RIGID.counter_response("gap") - math.log10(WIDEN),
    ),
    # AND THE SUBSPACE LOSS LEAVES WITH THE RATIO (CS2). Its gate is a
    # diagnostic now, for the stronger reason of the two: it breached at more
    # of the reviewer's clean frames than the quantity already retired. A
    # counter registered against a gate that does not assert cannot redden it,
    # and both cells here failed at the commit that retired it -- which is
    # this meta-test doing its job for the second round running.
]


# --------------------------------------------------------------------------
# THE NEGATIVE CONTROLS (BX0). Three defective counter bodies, carried so the
# discrimination this file claims is measured rather than asserted. Two of them
# shipped in this repository; the third is the one the twenty-first review built
# against it. Each is rejected by exactly one of the two cells.
# --------------------------------------------------------------------------


def _control_R163() -> None:
    """R163, as written: `40 * ulp(CD) / ulp(CD) > 4`, arithmetic on constants.

    It reads the ceiling, so widening the ceiling makes this comparison fail and
    the ceiling cell reads that failure as injection -- it admits it. It never
    runs the calibration, so the gate cell rejects it.
    """
    cd = CORPUS.PATCH_TEST_EXACTNESS_COUNTER_DEFECT
    ulp = (40.0 * math.ulp(cd)) / math.ulp(cd)
    assert ulp > CORPUS.DELTA_CALIBRATION_ULP, "the injection is below the ceiling"


def _control_R173() -> None:
    """R173, as written: `10 > 4`, two constants, in the commit that fixed R163."""
    assert (
        GOLDEN.EXEMPT_RESPONSE_DRIFT_ULP_COUNTER > GOLDEN.EXEMPT_RESPONSE_DRIFT_ULP
    ), "the injection is below the ceiling"


def _control_wrong_quantity() -> None:
    """R197's body: it CALLS its gate, and injects a quantity the ceiling does
    not describe -- a 100% relative error where the constant says N ULP.

    `DELTA_CALIBRATION_ULP` is absent from it: it is sized by nothing, and the
    constant could move from `4.0` to `1e9` with this green. The gate cell
    admits it, because it does run the gate. The ceiling cell rejects it,
    because a 100% error survives a ceiling widened to `WIDEN` times 5 ULP.
    """
    original = CORPUS.injected_delta
    CORPUS.injected_delta = lambda e, k, _o=original: (
        _o(e, k) * 2.0 if k == "one_element_scaled" else _o(e, k)
    )
    try:
        with pytest.raises(AssertionError, match="ULP"):
            CORPUS.test_the_delta_measure_is_CALIBRATED()
    finally:
        CORPUS.injected_delta = original

    CORPUS.test_the_delta_measure_is_CALIBRATED()


CONTROLS = [
    (
        "R163's body",
        _control_R163,
        "gate",
        CORPUS,
        "test_the_delta_measure_is_CALIBRATED",
        "DELTA_CALIBRATION_ULP",
        WIDEN * CORPUS.DELTA_CALIBRATION_ULP_COUNTER,
    ),
    (
        "R173's body",
        _control_R173,
        "gate",
        GOLDEN,
        "test_every_recorded_pair_is_still_detected",
        "EXEMPT_RESPONSE_DRIFT_ULP",
        WIDEN * GOLDEN.EXEMPT_RESPONSE_DRIFT_ULP_COUNTER,
    ),
    (
        "R197's wrong-quantity body",
        _control_wrong_quantity,
        "ceiling",
        CORPUS,
        "test_the_delta_measure_is_CALIBRATED",
        "DELTA_CALIBRATION_ULP",
        WIDEN * CORPUS.DELTA_CALIBRATION_ULP_COUNTER,
    ),
]


def _fails(counter) -> bool:
    """True if the counter fails.

    ANY failure, not only `AssertionError`: a counter that runs its gate through
    `pytest.raises` fails with pytest's own `Failed`, which is not an
    `AssertionError` subclass.
    """
    try:
        counter()
    except BaseException:  # noqa: BLE001 -- the outcome IS the measurement
        return True
    return False


def _gate_cell(counter, module, gate: str) -> bool:
    """Replace the assertion the counter defends with a no-op.

    A counter that measures the gate must fail; one that compares two constants
    passes.
    """
    original = getattr(module, gate)
    setattr(module, gate, lambda *a, **k: None)
    try:
        return _fails(counter)
    finally:
        setattr(module, gate, original)


def _ceiling_cell(counter, module, ceiling: str, widened: float) -> bool:
    """Widen the ceiling past the counter's declared injection.

    A counter sized by that constant must fail; one sized by something else
    passes.
    """
    original = getattr(module, ceiling)
    setattr(module, ceiling, widened)
    try:
        return _fails(counter)
    finally:
        setattr(module, ceiling, original)


def test_there_is_something_to_check() -> None:
    """Meta-test: an empty registry makes this file a test of nothing, and a
    control set that exercises only one cell makes the other one vacuous."""
    assert REGISTERED, "no counter is registered; this file checks nothing"
    assert len(REGISTERED) >= 5, (
        f"only {[r[0] for r in REGISTERED]} registered -- every counter with a "
        "callable gate belongs here, and an exemption is a hole in the guard "
        "written for exactly this"
    )
    rejecting = {c[2] for c in CONTROLS}
    assert rejecting == {"gate", "ceiling"}, (
        f"the controls exercise {sorted(rejecting)}. A cell with no control "
        "that only it rejects is a cell nothing shows to be necessary."
    )


@pytest.mark.parametrize(
    "label, counter, module, gate, ceiling, widened", REGISTERED, ids=[r[0] for r in REGISTERED]
)
def test_the_counter_fails_when_its_gate_is_neutered(
    label: str, counter, module, gate: str, ceiling: str, widened: float
) -> None:
    """CELL ONE (R182). The counter must depend on the assertion it defends."""
    counter()  # unperturbed it passes: a failure below is the neutering
    assert _gate_cell(counter, module, gate), (
        f"the {label} counter passes with `{gate}` replaced by a no-op. It is "
        "not running the assertion it defends -- it is asserting itself, which "
        "is R163 and R173."
    )
    counter()  # and it passes again, so nothing here is left broken


@pytest.mark.parametrize(
    "label, counter, module, gate, ceiling, widened", REGISTERED, ids=[r[0] for r in REGISTERED]
)
def test_the_counter_fails_when_its_ceiling_is_widened(
    label: str, counter, module, gate: str, ceiling: str, widened: float
) -> None:
    """CELL TWO (R197). The counter must be SIZED BY the constant it defends.

    Running the gate is not enough. R197's body ran the gate faithfully and
    injected a 100% error where the constant says N ULP, so the constant could
    be widened by nine orders with it green -- the original defect, alive inside
    the guard written to stop it.
    """
    counter()  # unperturbed it passes: a failure below is the widening
    assert _ceiling_cell(counter, module, ceiling, widened), (
        f"the {label} counter passes with `{ceiling}` widened to {widened:g}, "
        "past its own declared injection. Its injection is therefore not sized "
        "by that constant, so the constant can move without this counter "
        "noticing -- which is the whole failure this file exists for."
    )
    counter()  # and it passes again, so nothing here is left broken


@pytest.mark.parametrize(
    "label, body, rejected_by, module, gate, ceiling, widened",
    CONTROLS,
    ids=[c[0] for c in CONTROLS],
)
def test_a_DEFECTIVE_counter_is_rejected_by_its_cell_and_admitted_by_the_other(
    label: str, body, rejected_by: str, module, gate: str, ceiling: str, widened: float
) -> None:
    """The controls: both cells are necessary, measured rather than argued.

    A defective body is REJECTED by a cell when it PASSES that cell's
    perturbation -- the cell then reports it as self-asserting. It is ADMITTED
    when it fails, which is what a genuine counter does. Each control is
    asserted in BOTH directions, so deleting either cell turns a control green
    and this test red.
    """
    body()  # every control passes on a clean tree -- that is what makes it a defect
    outcome = {
        "gate": _gate_cell(body, module, gate),
        "ceiling": _ceiling_cell(body, module, ceiling, widened),
    }
    other = "ceiling" if rejected_by == "gate" else "gate"

    assert outcome[rejected_by] is False, (
        f"{label} FAILS the {rejected_by} cell, so that cell reads it as a "
        "genuine counter. It is a defective body, and this file's "
        "discrimination is not what its docstring says."
    )
    assert outcome[other] is True, (
        f"{label} passes the {other} cell too, so the {rejected_by} cell is not "
        f"shown to be necessary by this control. Find a body only the "
        f"{rejected_by} cell rejects, or the pair is one cell wearing two names."
    )
