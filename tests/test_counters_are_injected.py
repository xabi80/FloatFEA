"""Every counter-case is INJECTED, proved by neutering the gate it guards (BV1).

THE EIGHTH GUARD, MADE GENERIC. `RESULTANT_EXACTNESS` once shipped with
`ceiling < counter` as its only guard -- two literals compared in
`tolerances.py` -- and could be widened a hundredfold with the suite green. BG1
answered that case by injecting the defect. Twice since, a counter has been
written that asserts *itself* instead:

* R163 -- the calibration's counter computed `40 * ulp(CD) / ulp(CD)` and checked
  `40 > 4`. Arithmetic on two constants. It passed with the assertion it guards
  neutered.
* R173 -- the exempt-drift counter, one round later, in the commit that fixed
  R163: neuter the shipped comparison and the counter still passed. It bound only
  "the ceiling may not exceed 10 ULP".

Two instances of one defect, a round apart, each found by a reviewer. **This
makes it a build failure.** Every counter registers the pair

    (gate, counter)

where `gate` is the test whose assertion the counter exists to defend, and the
meta-test below runs the counter with the gate's comparison replaced by
always-true. A counter that still passes is not injecting anything.

WHAT THIS CANNOT DO, said so it is not trusted past its reach: it neuters by
monkey-patching the module-level name the gate compares through, so a gate that
inlines its comparison cannot be registered here. Those are listed as
`_NOT_REGISTERABLE` with the reason, which is a smaller surface than the defect
it replaces and a visible one.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests" / "verification" / "rung1"))

import test_corpus_configurations as CORPUS  # noqa: E402
sys.path.insert(0, str(ROOT / "tests" / "regression"))
import test_exempt_pair_responses as GOLDEN  # noqa: E402


def _neuter_ulp(module, name: str):
    """Replace a module-level ULP ceiling with one nothing can exceed."""
    original = getattr(module, name)
    setattr(module, name, float("inf"))
    return lambda: setattr(module, name, original)


REGISTERED = [
    # (label, counter test, neuter, restore-maker)
    ("calibration ULP",
     CORPUS.test_a_LARGER_deviation_fails_the_calibration,
     CORPUS, "DELTA_CALIBRATION_ULP"),
    ("exempt-response drift",
     GOLDEN.test_a_MOVED_response_is_caught,
     GOLDEN, "EXEMPT_RESPONSE_DRIFT_ULP"),
]

_NOT_REGISTERABLE = {
    # counter -> why the gate's comparison cannot be neutered from outside
    "PATCH_TEST_EXACTNESS_COUNTER_DEFECT":
        "its gate is the red-on-defect assertion, which compares against "
        "PATCH_TEST_EXACTNESS inline in 296 parametrised cases rather than "
        "through a module-level name",
}


def test_there_is_something_to_check() -> None:
    """Meta-test: an empty registry makes this file a test of nothing."""
    assert REGISTERED, "no counter is registered; this file checks nothing"


@pytest.mark.parametrize("label, counter, module, ceiling",
                         REGISTERED, ids=[r[0] for r in REGISTERED])
def test_the_counter_fails_when_its_gate_is_neutered(
    label: str, counter, module, ceiling: str
) -> None:
    """The counter must depend on the assertion it defends.

    With the gate's ceiling raised to infinity nothing can exceed it, so a
    counter that measures the gate must fail. One that compares two constants
    passes -- which is exactly what R163 and R173 did.
    """
    counter()  # unperturbed, it passes: a failure below is the neutering

    restore = _neuter_ulp(module, ceiling)
    try:
        # ANY failure, not only `AssertionError`: a counter that runs its gate
        # through `pytest.raises` fails with pytest's own `Failed`, which is not
        # an `AssertionError` subclass. Requiring the narrower type would have
        # made this meta-test itself the thing that passes for the wrong reason.
        with pytest.raises(BaseException):  # noqa: B017, PT011
            counter()
    finally:
        restore()

    counter()  # and it passes again, so nothing here is left broken
