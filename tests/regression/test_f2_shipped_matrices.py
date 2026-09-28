"""V6.1 -- the golden for what F2 ships (D2 step 11, DK2).

`docs/verification/README.md`: "Reference results stored for the full
verification set and the platform model. Any change in any stored result fails
the build. A legitimate change is accompanied by a regenerated golden file and a
written explanation of why the numbers moved, recorded in the milestone closure
artifact."

WHAT IS RECORDED. Scalar invariants of the matrices F2 ships -- a trace, a
Frobenius norm and the extreme entry of each, plus the six rigid-body quadratic
forms of every element mass matrix. Three summaries per matrix and not one,
because each misses something the others catch: a trace misses an off-diagonal
sign flip, a Frobenius norm misses a transposition, and the extreme entry catches
a change of scale the other two average away.

WHAT IS DELIBERATELY NOT RECORDED, and this is the honest limit of the guard.
**Frequencies.** They come from `eigh`, whose last bits differ between LAPACK
builds, and this golden is checked on two platforms -- Windows locally, Linux on
CI. A tolerance loose enough to survive that difference would record almost
nothing; a tighter one would redden on a platform difference rather than on a
defect. **What a frequency golden needs first is a bound on that drift**, and
`docs/milestones/F2a.md` records it as the missing measurement with what it would
take. Until then V6.1 covers the matrices and `tests/verification/rung2` covers
the frequencies with assertions of its own.

The sentence here used to say the measurement was one "nobody has taken", which
is a claim about the repository in source-tree prose with nothing to check it
against (CW0, C16). What replaces it is a pointer to where the requirement is
recorded.

WHY THE COMPARISON IS RELATIVE AT `ROUNDOFF_IDENTITY` AND NOT IN ULP. The
neighbouring golden, `test_exempt_pair_responses.py`, compares in ULP with its
own declared drift constant, and that is the stronger form. It can afford to be:
its quantity is produced by the same arithmetic on both platforms. These
quantities pass through `np.linalg.solve` and `np.linalg.inv` in the
condensation and the interpolation, so their last bits are LAPACK's. At `1e-14`
relative this guard catches **a change in a formulation**, which is what a
regression is for, and does not claim to catch a last-bit drift. Saying which of
the two it is matters more than the number.

REGENERATING IT. `python scripts/regen_f2_golden.py`, and then the explanation of
why the numbers moved goes in the closure artifact. No exception for "the element
changed": that IS the case the explanation is for.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from regen_f2_golden import collect  # noqa: E402

from floatfea.tolerances import ROUNDOFF_IDENTITY  # noqa: E402

GOLDEN = ROOT / "tests" / "regression" / "f2_shipped_matrices.json"
RECORDED: dict[str, float] = json.loads(GOLDEN.read_text(encoding="utf-8"))
MEASURED: dict[str, float] = collect()


def test_the_golden_exists_and_records_something() -> None:
    """Meta-test: an empty golden makes every comparison below vacuous."""
    assert RECORDED, f"{GOLDEN} is empty, so this file asserts nothing"
    assert len(RECORDED) >= 100, (
        f"only {len(RECORDED)} quantities recorded. F2 ships two element matrices "
        "at three spans and two sections, four release patterns, two link offsets "
        "and an assembled frame with and without a link; a short file means the "
        "generator stopped collecting rather than that there is little to record."
    )


def test_every_recorded_quantity_is_still_produced() -> None:
    """A recorded name that the generator no longer emits is a DELETION.

    Asserted separately from the values, because a deleted quantity and a moved
    one need different responses: a move needs an explanation, a disappearance
    needs to be intended.
    """
    missing = sorted(set(RECORDED) - set(MEASURED))
    assert not missing, (
        f"{len(missing)} recorded quantities are no longer produced, first few "
        f"{missing[:5]}. Either something was deleted or the generator was "
        "narrowed; regenerate deliberately and say why in the closure artifact."
    )


def test_the_generator_produces_nothing_UNRECORDED() -> None:
    """The other direction: a new quantity has to enter the golden deliberately.

    Without this the golden silently covers less and less of what ships, which is
    the failure mode a deletion detector alone does not have.
    """
    extra = sorted(set(MEASURED) - set(RECORDED))
    assert not extra, (
        f"{len(extra)} produced quantities are not in the golden, first few "
        f"{extra[:5]}. Run `python scripts/regen_f2_golden.py` so the new "
        "quantities are protected too."
    )


@pytest.mark.parametrize("name", sorted(RECORDED), ids=sorted(RECORDED))
def test_the_recorded_value_has_not_moved(name: str) -> None:
    """The regression itself, one case per quantity so a failure names it."""
    want = RECORDED[name]
    got = MEASURED[name]
    scale = abs(want) if want != 0.0 else 1.0
    moved = abs(got - want) / scale
    assert moved <= ROUNDOFF_IDENTITY, (
        f"{name} moved from {want!r} to {got!r}, relative {moved:.4e} against "
        f"{ROUNDOFF_IDENTITY:g}. `CLAUDE.md` § Testing: regenerating this file to "
        "match new output, without a written explanation of why the number moved "
        "in the closure artifact, is the same error as widening a tolerance."
    )


def test_the_golden_would_notice_a_CHANGED_FORMULATION(capsys) -> None:
    """The control: a golden nothing can break is a file, not a guard.

    Every recorded quantity is perturbed by a relative amount one decade above
    the comparison threshold, and the least-moved of them still has to redden.

    **THE MAGNITUDE OF A QUANTITY IS IRRELEVANT HERE, and the first version of
    this docstring said the opposite** -- it picked the smallest recorded value
    and called it "where that is hardest", which is false for a RELATIVE
    comparison: the ratio is identical at every scale, and the number printed was
    1.0. What genuinely has no room is a quantity recorded as exactly zero, which
    no relative perturbation moves at all. Those are counted, named, and asserted
    absent rather than claimed to be covered.
    """
    zeros = sorted(k for k, v in RECORDED.items() if v == 0.0)
    nonzero = {k: v for k, v in RECORDED.items() if v != 0.0}
    assert nonzero, "every recorded quantity is zero, so no perturbation can be relative"
    worst_name, worst_moved = "", float("inf")
    for name, want in nonzero.items():
        moved = abs(want * (1.0 + 10.0 * ROUNDOFF_IDENTITY) - want) / abs(want)
        if moved < worst_moved:
            worst_name, worst_moved = name, moved
    with capsys.disabled():
        print(
            f"\n  {len(nonzero)} quantities perturbed by {10 * ROUNDOFF_IDENTITY:g} "
            f"relative; least-moved {worst_name} at {worst_moved:.4e}. "
            f"Recorded as exactly zero, so uncovered by a relative test: {len(zeros)}"
        )
    assert worst_moved > ROUNDOFF_IDENTITY, (
        f"a relative change of {10 * ROUNDOFF_IDENTITY:g} in {worst_name} does "
        f"not exceed {ROUNDOFF_IDENTITY:g}, so this golden cannot see a change "
        "of that size."
    )
    assert not zeros, (
        f"{len(zeros)} quantities are recorded as exactly zero ({zeros[:5]}), and "
        "a relative comparison cannot detect any change in them. They need an "
        "absolute companion or they do not belong in the golden."
    )
