"""Comparison helpers that refuse to compare things they cannot see (BD0).

Why this exists
---------------
Two negative controls for the *same* property were malformed in two attempts, and
both failed the same way: they compared quantities smaller than the comparison
could resolve.

The second was the sharper case. `pytest.approx(mm, rel=1e-12)` carries an
**undeclared default** `abs=1e-12`, so comparing `4.15e-12` against `4.15e-16`
passes -- and the control that was supposed to detect a 1000x unit drift detected
nothing. The construction was fixed after the first attempt; the *assertion* was
not, and nothing in the test could say so.

The rule
--------
**A comparison asserts its operands are above its floor before it compares them.**
`assert_close` raises on construction when `max(|a|, |b|)` is within `100 x floor`
of the resolution the comparison actually has, so a vacuous control fails loudly
instead of passing quietly.

This is the eighth guard -- a gate carries its own failure -- made executable at
the operand level, which is where it kept failing. `pytest.approx`,
`np.allclose` and friends are not called directly under `tests/`; the scanner
enforces that.
"""
from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike

DEFAULT_FLOOR_FACTOR = 100.0
"""How far above the floor the operands must sit. 100x is two decades of headroom
-- enough that a comparison is resolving a real difference rather than the floor,
and small enough not to reject legitimately tiny quantities that were measured."""


def assert_close(
    a: ArrayLike,
    b: ArrayLike,
    tol: float,
    *,
    floor: float,
    what: str = "",
) -> None:
    """Assert ``|a - b| <= tol * max(|a|, |b|)``, refusing a vacuous comparison.

    Parameters
    ----------
    tol
        Relative tolerance. Must come from `floatfea.tolerances`.
    floor
        The smallest magnitude this comparison can resolve -- the round-off floor
        of whatever produced `a` and `b`. If both operands sit within
        ``DEFAULT_FLOOR_FACTOR * floor`` of it, the comparison cannot distinguish
        agreement from noise and this raises rather than passing.
    """
    av = np.asarray(a, dtype=np.float64)
    bv = np.asarray(b, dtype=np.float64)
    scale = float(max(np.abs(av).max(initial=0.0), np.abs(bv).max(initial=0.0)))

    if scale < DEFAULT_FLOOR_FACTOR * floor:
        raise AssertionError(
            f"{what or 'comparison'} is VACUOUS: both operands are at most "
            f"{scale:.3e}, within {DEFAULT_FLOOR_FACTOR:.0f}x of the stated floor "
            f"{floor:.3e}. A comparison at this magnitude cannot distinguish "
            "agreement from noise -- it would pass whatever the code did. Compare "
            "a quantity the measurement can actually resolve, or state a lower "
            "floor and justify it."
        )

    diff = float(np.abs(av - bv).max(initial=0.0))
    if diff > tol * scale:
        raise AssertionError(
            f"{what or 'comparison'} failed: max |a - b| = {diff:.6e} exceeds "
            f"{tol:.3e} x {scale:.6e} = {tol * scale:.6e}"
        )


def assert_differs(
    a: ArrayLike,
    b: ArrayLike,
    by: float,
    *,
    floor: float,
    what: str = "",
) -> None:
    """Assert two quantities differ by at least `by` (relative). For controls.

    A negative control is a comparison too, and it fails the same way: asserting
    that two indistinguishable numbers differ proves nothing about the defect it
    claims to detect.
    """
    av = np.asarray(a, dtype=np.float64)
    bv = np.asarray(b, dtype=np.float64)
    scale = float(max(np.abs(av).max(initial=0.0), np.abs(bv).max(initial=0.0)))

    if scale < DEFAULT_FLOOR_FACTOR * floor:
        raise AssertionError(
            f"{what or 'control'} is VACUOUS: both operands are at most "
            f"{scale:.3e}, within {DEFAULT_FLOOR_FACTOR:.0f}x of the floor "
            f"{floor:.3e}. It cannot demonstrate a difference it could not see."
        )

    diff = float(np.abs(av - bv).max(initial=0.0))
    if diff < by * scale:
        raise AssertionError(
            f"{what or 'control'} did not separate: max |a - b| = {diff:.6e} is "
            f"below {by:.3e} x {scale:.6e} = {by * scale:.6e}. The control does "
            "not demonstrate what it claims."
        )
