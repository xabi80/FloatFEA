"""Every counter-case is INJECTED, proved by neutering the GATE it guards (BW1).

THE EIGHTH GUARD, MADE GENERIC. `RESULTANT_EXACTNESS` once shipped with
`ceiling < counter` as its only guard -- two literals compared in
`tolerances.py` -- and could be widened a hundredfold with the suite green. BG1
answered that case by injecting the defect. Twice since, a counter was written
that asserts *itself* instead: R163 (`40 * ulp(CD) / ulp(CD) > 4`) and, one round
later in the commit that fixed R163, R173 (`10 > 4`).

**AND THE FIRST VERSION OF THIS FILE COULD NOT CATCH EITHER OF THEM (R182).** It
neutered the ceiling CONSTANT, setting it to `inf`. A degenerate counter is
precisely one shaped `assert value > CEILING` -- so raising the ceiling makes
*that* comparison fail too, and the meta-test read the failure as injection:

    counter body                    ceiling -> inf      gate -> no-op
    R163's, as written              AssertionError      PASSES  <- defect
    R173's, as written              AssertionError      PASSES  <- defect
    the shipped calibration         Failed              Failed
    the shipped exempt-drift        Failed              Failed

Only the right-hand column discriminates. **This file replaces the GATE
FUNCTION with a no-op** and requires the counter to fail: a counter that passes
when the assertion it defends does nothing is measuring itself.

WHAT IT STILL CANNOT DO, said so it is not trusted past its reach: it replaces
the gate by name in the gate's own module, so a counter that reimplements its
gate's comparison inline rather than calling it would pass. That is a narrower
hole than the one it closes, and it is visible in each registration.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests" / "verification" / "rung1"))
sys.path.insert(0, str(ROOT / "tests" / "regression"))

import test_corpus_configurations as CORPUS  # noqa: E402
import test_exempt_pair_responses as GOLDEN  # noqa: E402


class _Capsys:
    """The one fixture the registered gates take, supplied without pytest."""

    @staticmethod
    def disabled():
        import contextlib
        return contextlib.nullcontext()


REGISTERED = [
    ("calibration ULP",
     CORPUS.test_a_LARGER_deviation_fails_the_calibration,
     CORPUS, "test_the_delta_measure_is_CALIBRATED"),
    ("exempt-response drift",
     GOLDEN.test_a_MOVED_response_is_caught,
     GOLDEN, "test_every_recorded_pair_is_still_detected"),
    # `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` -- THE EXEMPTION IS GONE (R183). It
    # was listed as unregisterable "because its gate compares inline across 296
    # parametrised cases", which named the wrong gate: this constant's gate is
    # the headroom assertion, a single test. Registering it found a THIRD
    # instance of R163's defect -- a counter comparing two constants -- which is
    # what this file exists to find.
    ("counter-defect size",
     lambda: CORPUS.test_a_RAISED_counter_defect_breaks_that(_Capsys),
     CORPUS, "test_the_counter_DEFECT_SIZE_cannot_be_raised"),
]


def test_there_is_something_to_check() -> None:
    """Meta-test: an empty registry makes this file a test of nothing."""
    assert REGISTERED, "no counter is registered; this file checks nothing"
    assert len(REGISTERED) >= 3, (
        f"only {[r[0] for r in REGISTERED]} registered -- every counter with a "
        "callable gate belongs here, and an exemption is a hole in the guard "
        "written for exactly this"
    )


@pytest.mark.parametrize("label, counter, module, gate",
                         REGISTERED, ids=[r[0] for r in REGISTERED])
def test_the_counter_fails_when_its_gate_is_neutered(
    label: str, counter, module, gate: str
) -> None:
    """The counter must depend on the assertion it defends.

    With the gate replaced by a no-op nothing it asserts can fail, so a counter
    that measures the gate must fail. One that compares two constants passes --
    which is exactly what R163 and R173 did, and what the ceiling-neutering
    version of this test could not see.
    """
    counter()  # unperturbed it passes: a failure below is the neutering

    original = getattr(module, gate)
    setattr(module, gate, lambda *a, **k: None)
    try:
        # ANY failure, not only `AssertionError`: a counter that runs its gate
        # through `pytest.raises` fails with pytest's own `Failed`, which is not
        # an `AssertionError` subclass.
        with pytest.raises(BaseException):  # noqa: B017, PT011
            counter()
    finally:
        setattr(module, gate, original)

    counter()  # and it passes again, so nothing here is left broken
