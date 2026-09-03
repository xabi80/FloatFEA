"""AV2 -- the transformation, over-determined by invariance.

In local axes the element is block-diagonal (asserted in `test_beam_element.py`),
so **every coupling entry it has lives in `T^T K T`**. The transformation owns all
of them, and three invariances pin it against expectations already trusted:

* **Rotation invariance** — build the member along `R e_x`, apply `R f`, and the
  response must be `R u_local` with `u_local` the closed form from AU1. One test
  exercises every coupling entry at once.
* **Spectrum invariance** — an orthogonal transform cannot move an eigenvalue.
  A non-orthogonal `T` (the `I + [theta x]` first-order trap in
  `conventions.md`, arriving through a different door) shows up here and nowhere
  else.
* **Roll invariance** — for a circular section the response cannot depend on the
  reference vector that fixes local *y*. A defect in `local_axes.py` is otherwise
  invisible until a member happens to lie near the reference direction.

The rotation is deliberately **not axis-aligned**: a 90 degree rotation about z
permutes entries and passes with a sign error that a skew 37 degree rotation
exposes.
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.element.beam import local_stiffness
from floatfea.element.transform import rotation_matrix, to_global, transformation
from floatfea.model.material import S355, Section
from floatfea.tolerances import (
    TRANSFORM_INVARIANCE,
    TRANSFORM_INVARIANCE_COUNTER,
)

SEC = Section.circular_tube(0.8, 0.020)
L = 2.4
LOAD = 1.0e6


def rodrigues(axis: np.ndarray, angle: float) -> np.ndarray:
    """Rotation by `angle` about `axis`, per `docs/conventions.md`."""
    a = np.asarray(axis, dtype=np.float64)
    a = a / np.linalg.norm(a)
    kx = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(angle) * kx + (1 - np.cos(angle)) * (kx @ kx)


SKEW = rodrigues(np.array([0.3, -0.7, 0.65]), np.radians(37.0))


def _triad_from(rot: np.ndarray):
    """Nodes and orientation node that force the member triad to equal `rot`."""
    a = np.array([1.3, -0.4, 2.2])
    b = a + L * rot[0]
    return a, b, a + rot[2]


def test_the_fixture_rotation_is_not_axis_aligned() -> None:
    """Meta-test: an axis-aligned rotation would only permute entries."""
    for col in SKEW.T:
        assert np.abs(col).min() > 0.05, "rotation is too close to axis-aligned"
    assert np.allclose(SKEW @ SKEW.T, np.eye(3), atol=1e-14)


def test_the_member_triad_equals_the_intended_rotation() -> None:
    a, b, o = _triad_from(SKEW)
    assert np.allclose(rotation_matrix(a, b, orientation_node=o), SKEW, atol=1e-12)


@pytest.mark.parametrize("dof", [0, 1, 2, 3, 4, 5])
def test_rotation_invariance_of_the_response(dof: int) -> None:
    """AV2: response in global == R^T (response in local), for every load DOF.

    Exercises every coupling entry of `T^T K T` at once, against the local
    closed-form behaviour already pinned at step 2.
    """
    a, b, o = _triad_from(SKEW)
    k_loc = local_stiffness(SEC, S355, L)
    k_glo = to_global(k_loc, rotation_matrix(a, b, orientation_node=o))

    free = [6, 7, 8, 9, 10, 11]
    f_loc = np.zeros(6)
    f_loc[dof] = LOAD
    u_loc = np.linalg.solve(k_loc[np.ix_(free, free)], f_loc)

    # The same physical load and response, expressed globally.
    r6 = np.zeros((6, 6))
    r6[:3, :3] = SKEW
    r6[3:, 3:] = SKEW
    f_glo = r6.T @ f_loc
    u_glo = np.linalg.solve(k_glo[np.ix_(free, free)], f_glo)

    # Scaled by the response magnitude. An absolute floor below the round-off of
    # the solve fails on components whose exact value is zero -- which a first
    # draft of this test did, at 1e-18 against a measured 1.07e-18.
    scale = np.abs(u_loc).max()
    assert np.allclose(
        u_glo, r6.T @ u_loc, rtol=TRANSFORM_INVARIANCE,
        atol=TRANSFORM_INVARIANCE * scale,
    ), "global response is not the rotated local response; a coupling entry in T^T K T is wrong"


def test_spectrum_invariance_under_the_transform() -> None:
    """An orthogonal transform cannot move an eigenvalue.

    This is the only test here that would catch a non-orthogonal `T` -- the
    `I + [theta x]` first-order trap. A first-order rotation passes a
    small-angle response check and fails this one.
    """
    k_loc = local_stiffness(SEC, S355, L)
    k_glo = to_global(k_loc, SKEW)
    ev_loc = np.sort(np.linalg.eigvalsh(k_loc))
    ev_glo = np.sort(np.linalg.eigvalsh(k_glo))
    scale = np.abs(ev_loc).max()
    assert np.allclose(ev_loc, ev_glo, rtol=0, atol=TRANSFORM_INVARIANCE * scale)


def test_a_NON_orthogonal_transform_moves_the_spectrum() -> None:
    """Negative control for the test above.

    Without it, spectrum invariance could hold trivially -- and the check would
    certify rather than test.
    """
    k_loc = local_stiffness(SEC, S355, L)
    theta = np.array([0.05, -0.03, 0.02])
    kx = np.array([[0, -theta[2], theta[1]], [theta[2], 0, -theta[0]],
                   [-theta[1], theta[0], 0]])
    first_order = np.eye(3) + kx                     # NOT orthogonal
    assert not np.allclose(first_order @ first_order.T, np.eye(3), atol=1e-6)

    t = transformation(first_order)
    bad = t.T @ k_loc @ t
    ev_loc = np.sort(np.linalg.eigvalsh(k_loc))
    ev_bad = np.sort(np.linalg.eigvalsh(bad))
    scale = np.abs(ev_loc).max()
    shift = np.abs(ev_bad - ev_loc).max() / scale
    # Consumes the COUNTER value: the defect must reach the declared magnitude,
    # so the ceiling cannot be widened toward it without breaking the pairing.
    assert shift >= TRANSFORM_INVARIANCE_COUNTER, (
        f"a non-orthogonal transform shifted the spectrum by only {shift:.3e}, "
        f"below the declared counter-case {TRANSFORM_INVARIANCE_COUNTER:.3e}"
    )


@pytest.mark.parametrize("roll_deg", [0.0, 17.0, 90.0, 231.0])
def test_roll_invariance_for_a_circular_section(roll_deg: float) -> None:
    """For a circular section the global response cannot depend on local y.

    The sharpest single test of `local_axes.py`: a defect there is otherwise
    invisible until a member happens to lie near the orientation reference.
    """
    a = np.array([0.0, 0.0, 0.0])
    b = a + L * SKEW[0]
    k_ref = to_global(
        local_stiffness(SEC, S355, L), rotation_matrix(a, b, roll_rad=0.0)
    )
    k_rolled = to_global(
        local_stiffness(SEC, S355, L),
        rotation_matrix(a, b, roll_rad=np.radians(roll_deg)),
    )
    scale = np.abs(k_ref).max()
    assert np.allclose(k_ref, k_rolled, rtol=0, atol=TRANSFORM_INVARIANCE * scale), (
        f"roll of {roll_deg} deg changed the global stiffness of a circular "
        "section; either the triad or the transform is wrong"
    )


def test_roll_invariance_would_FAIL_for_an_unequal_section() -> None:
    """Negative control: the invariance must be a property of the SECTION.

    If it held for I_y != I_z as well, the test above would be insensitive to the
    triad entirely.
    """
    unequal = Section(A=SEC.A, I_y=SEC.I_y, I_z=3.0 * SEC.I_z, J=SEC.J,
                      shape="thin_tube")
    a = np.array([0.0, 0.0, 0.0])
    b = a + L * SKEW[0]
    k_ref = to_global(local_stiffness(unequal, S355, L), rotation_matrix(a, b))
    k_rolled = to_global(
        local_stiffness(unequal, S355, L),
        rotation_matrix(a, b, roll_rad=np.radians(37.0)),
    )
    assert not np.allclose(
        k_ref, k_rolled, rtol=0, atol=TRANSFORM_INVARIANCE * np.abs(k_ref).max()
    )
