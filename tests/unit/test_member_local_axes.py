"""The degeneracy guard must FIRE on a vertical member.

`MEMBER_ORIENTATION_DEGENERACY` is a threshold designed to be tripped: the spars
in this platform are vertical, so it fires on the real model by construction.
That creates standing pressure to raise it — the first time someone adds a spar
and the build refuses, the cheapest fix on offer is a bigger number, and the
justification comment in `tolerances.py` will not stop that.

These tests convert a silent bump into a broken test, which is the only reliable
guard for a deliberately-firing threshold. If the value is raised far enough to
admit a vertical member, `test_guard_fires_on_a_vertical_member` goes red and
says why.

Convention under test: `docs/conventions.md` § "Member local axes".
"""

from __future__ import annotations

import numpy as np
import pytest

from floatfea.model.local_axes import DegenerateMemberOrientation, member_local_axes
from floatfea.tolerances import MEMBER_ORIENTATION_DEGENERACY

# The real spar: vertical, full-scale submerged length (docs/milestones/F1.md sec.8).
_SPAR_BOTTOM = np.array([0.0, 0.0, -72.87])
_SPAR_TOP = np.array([0.0, 0.0, 0.0])


def test_guard_fires_on_a_vertical_member() -> None:
    """A vertical member with no explicit orientation must be REFUSED.

    This is the test that protects the threshold. It fails if
    MEMBER_ORIENTATION_DEGENERACY is raised to a value that admits a vertical
    member, which is the specific silent change it exists to catch.
    """
    with pytest.raises(DegenerateMemberOrientation) as exc:
        member_local_axes(_SPAR_BOTTOM, _SPAR_TOP)
    message = str(exc.value)
    assert "MEMBER_ORIENTATION_DEGENERACY" in message
    assert "no silent fallback" in message


def test_guard_fires_just_inside_the_threshold() -> None:
    """A member just inside the floor is refused; just outside is admitted.

    Pins the threshold's location, not merely its existence -- a test that only
    checked the exactly-vertical case would still pass if the value were raised
    to admit a member 30 degrees off vertical.
    """
    eps = MEMBER_ORIENTATION_DEGENERACY
    length = 100.0
    inside = np.array([0.5 * eps * length, 0.0, np.sqrt(1.0 - (0.5 * eps) ** 2) * length])
    outside = np.array([2.0 * eps * length, 0.0, np.sqrt(1.0 - (2.0 * eps) ** 2) * length])

    with pytest.raises(DegenerateMemberOrientation):
        member_local_axes(np.zeros(3), inside)

    x, y, z = member_local_axes(np.zeros(3), outside)
    assert np.isclose(np.linalg.norm(x), 1.0)
    assert np.isclose(np.linalg.norm(y), 1.0)
    assert np.isclose(np.linalg.norm(z), 1.0)


def test_orientation_node_admits_the_vertical_spar() -> None:
    """The documented remedy works: an explicit orientation node."""
    x, y, z = member_local_axes(
        _SPAR_BOTTOM, _SPAR_TOP, orientation_node=np.array([1.0, 0.0, -72.87])
    )
    np.testing.assert_allclose(x, [0.0, 0.0, 1.0], atol=1e-12)
    np.testing.assert_allclose(z, [1.0, 0.0, 0.0], atol=1e-12)
    np.testing.assert_allclose(y, np.cross(z, x), atol=1e-12)


def test_triad_is_right_handed_and_orthonormal() -> None:
    """y = z x x, all unit, all mutually orthogonal -- for a horizontal member."""
    x, y, z = member_local_axes(np.zeros(3), np.array([50.0, 0.0, 0.0]))
    for v in (x, y, z):
        assert np.isclose(np.linalg.norm(v), 1.0)
    assert np.isclose(np.dot(x, y), 0.0, atol=1e-12)
    assert np.isclose(np.dot(y, z), 0.0, atol=1e-12)
    assert np.isclose(np.dot(z, x), 0.0, atol=1e-12)
    np.testing.assert_allclose(np.cross(z, x), y, atol=1e-12)


def test_collinear_orientation_node_is_refused() -> None:
    """An orientation node on the member axis is degenerate however it arrived."""
    with pytest.raises(DegenerateMemberOrientation):
        member_local_axes(
            _SPAR_BOTTOM, _SPAR_TOP, orientation_node=np.array([0.0, 0.0, -10.0])
        )


def test_roll_does_not_rescue_a_vertical_member() -> None:
    """Roll is measured FROM the global-Z reference, so it cannot save a member
    for which that reference does not exist. Documented in local_axes."""
    with pytest.raises(DegenerateMemberOrientation):
        member_local_axes(_SPAR_BOTTOM, _SPAR_TOP, roll_rad=np.pi / 4)
