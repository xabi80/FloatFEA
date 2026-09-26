"""An interpolated reference carries a flag, and a round-off comparison refuses it (AK3).

Written to the eighth guard: the fixture is asserted to contain the failing case
before anything is asserted about catching it.
"""

from __future__ import annotations

import numpy as np
import pytest

from floatfea.io.frames import (
    Reference,
    assert_reference_supports,
    interpolated_reference,
)
from floatfea.tolerances import INTERPOLATED_REFERENCE_TOLERANCE_FLOOR, ROUNDOFF_IDENTITY

# The measured AF3 case: the case frequency sits near dead centre of its gap
# because case frequencies are chosen for physics, not grid alignment.
GRID = np.array([1.930166, 2.074677])
W_CASE = 2.000377
B_VALUES = np.array([[1.0, 1.6]])  # B varies ~60% across this gap


def test_fixture_really_is_a_mid_gap_case() -> None:
    """Without this the guard tests could pass on a reference that is nearly exact."""
    f = (W_CASE - GRID[0]) / (GRID[1] - GRID[0])
    assert (
        0.3  # not-a-tolerance: fixture property -- the lower bracket
        < f
        < 0.7
        # not-a-tolerance: fixture property -- asserts the fixture is in a usable range
    ), f"fixture is not mid-gap (f={f:.3f}); it cannot exercise the guard"


def test_interpolation_is_flagged_with_its_gap_fraction() -> None:
    ref = interpolated_reference(GRID, B_VALUES, W_CASE, source="hdb.B")
    assert ref.interpolated
    assert ref.gap_fraction == pytest.approx(
        0.486,
        abs=5e-3,
        # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is
        # unchanged
    )


def test_a_solved_frequency_is_not_flagged() -> None:
    """Landing on a grid point must not be penalised, or callers route around."""
    ref = interpolated_reference(GRID, B_VALUES, float(GRID[1]), source="hdb.B")
    assert not ref.interpolated
    assert ref.value == pytest.approx(B_VALUES[..., 1], rel=ROUNDOFF_IDENTITY)


def test_round_off_comparison_refuses_an_interpolated_reference() -> None:
    ref = interpolated_reference(GRID, B_VALUES, W_CASE, source="hdb.B")
    with pytest.raises(ValueError, match="INTERPOLATED"):
        assert_reference_supports(ref, tolerance=1e-12, what="G1.6 radiation")


def test_a_loose_comparison_still_accepts_one() -> None:
    """The guard must not forbid interpolation everywhere -- only where it hides."""
    ref = interpolated_reference(GRID, B_VALUES, W_CASE, source="hdb.B")
    assert_reference_supports(ref, tolerance=1e-2, what="a loose check")


def test_the_floor_is_the_boundary_it_claims_to_be() -> None:
    ref = interpolated_reference(GRID, B_VALUES, W_CASE, source="hdb.B")
    assert_reference_supports(
        ref, tolerance=INTERPOLATED_REFERENCE_TOLERANCE_FLOOR * 1.01, what="just above"
    )
    with pytest.raises(ValueError):
        assert_reference_supports(
            ref, tolerance=INTERPOLATED_REFERENCE_TOLERANCE_FLOOR, what="at the floor"
        )


def test_an_exact_reference_passes_at_any_tolerance() -> None:
    ref = Reference(np.ones(3), omega=W_CASE, interpolated=False, source="same solve")
    assert_reference_supports(ref, tolerance=1e-15, what="AF3 same-solve")


def test_interpolated_without_gap_fraction_is_rejected_at_construction() -> None:
    with pytest.raises(ValueError, match="gap_fraction"):
        Reference(np.ones(3), omega=1.0, interpolated=True, source="unlabelled")
