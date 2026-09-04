"""The dead-DOF exclusion is structural (AI4).

The eighth guard says a gate should carry the failure it detects. These tests are
written to that rule: the fixture below is asserted to *contain* a dead DOF before
anything is asserted about excluding one, because a test that yaw is excluded
passes trivially on a fixture where every DOF is live.
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.io.frames import live_dof, over_live
from floatfea.tolerances import DEAD_DOF_RELATIVE_FLOOR

DOF_NAME = ("surge", "sway", "heave", "roll", "pitch", "yaw")

# The measured AG5 case: max |mu| per DOF on the 12-buoy platform, trapezoid
# convolution, last 8 periods. Yaw is 1.2e-17 because a body of revolution has no
# yaw radiation -- round-off, not a small physical quantity.
MU_MEASURED = np.array(
    [4.2485e-01, 3.1213e-02, 1.7728e-02, 2.8032e-02, 4.0844e-01, 1.1788e-17]
)


def test_fixture_actually_contains_a_dead_dof() -> None:
    """Meta-test: without this, every assertion below could pass vacuously.

    This is the fixture-pose failure in its general form -- a check for exclusion
    proves nothing on data with nothing to exclude.
    """
    ratios = MU_MEASURED / MU_MEASURED.max()
    assert (ratios < DEAD_DOF_RELATIVE_FLOOR).any(), (
        "the fixture has no dead DOF, so the exclusion tests below cannot fail "
        "and therefore cannot pass meaningfully"
    )
    assert (ratios >= DEAD_DOF_RELATIVE_FLOOR).any(), "the fixture has no live DOF"


def test_yaw_is_excluded_and_the_other_five_are_not() -> None:
    mask = live_dof(MU_MEASURED)
    assert [n for n, m in zip(DOF_NAME, mask) if not m] == ["yaw"]
    assert mask.sum() == 5


K0_MEASURED = np.array(
    [2.0389e02, 2.0455e02, 3.5363e-02, 2.6278e02, 2.6207e02, 1.2830e-30]
)
CHANGE_LIVE = [0.041, 0.016, 0.0024, 0.007, 0.044]


@pytest.mark.parametrize(
    "yaw_change, contaminated",
    [
        # The dead DOF's noise reached the statistic two different ways in two
        # successive versions of the AG5 script, and corrupted it in OPPOSITE
        # directions -- which is the argument for excluding it structurally
        # rather than remembering to handle it.
        (0.0, 0.6523),      # second version: yaw's nan mapped to zero
        (0.041, 0.1246),    # first version: yaw's round-off read as a real -4.1%
    ],
)
def test_exclusion_changes_the_statistic_it_guards(
    yaw_change: float, contaminated: float
) -> None:
    """The guard must be load-bearing, not decorative.

    The guarded value is the SAME for both handlings of the dead DOF; the naive
    value swings from +0.12 to +0.65 on a choice that is arbitrary. Truth is
    +0.53.
    """
    change = np.array([*CHANGE_LIVE, yaw_change])

    naive = np.corrcoef(K0_MEASURED, change)[0, 1]
    guarded = np.corrcoef(
        over_live(K0_MEASURED, MU_MEASURED, what="K(0)"),
        over_live(change, MU_MEASURED, what="d|mu|"),
    )[0, 1]

    assert naive == pytest.approx(contaminated, abs=5e-3)  # not-a-tolerance: reference pin -- the recorded contaminated values
    assert guarded == pytest.approx(0.5256, abs=5e-3)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged
    assert abs(naive - guarded) > 0.05, "the guard would be decorative on this data"  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small


def test_a_uniformly_dead_set_is_NOT_caught() -> None:
    """The documented limitation, asserted so it cannot be forgotten.

    A relative floor makes the largest entry live by construction, so a set that
    is round-off in every DOF passes through untouched. Saying so in a test is
    the eighth guard applied to the guard itself.
    """
    uniformly_tiny = np.array([1e-30, 2e-30, 1e-30])
    assert live_dof(uniformly_tiny).all(), (
        "if this ever starts excluding, the floor gained an absolute component "
        "and the docstring's stated limitation is now wrong"
    )


def test_all_zero_reference_raises() -> None:
    with pytest.raises(ValueError, match="no signal"):
        live_dof(np.zeros(6))


def test_mismatched_length_raises() -> None:
    with pytest.raises(ValueError, match="same DOF in the same order"):
        over_live(np.ones(5), MU_MEASURED, what="mismatched")


def test_reference_must_be_per_dof() -> None:
    with pytest.raises(ValueError, match="1-D"):
        live_dof(np.ones((6, 6)))
