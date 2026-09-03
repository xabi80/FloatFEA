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
    TRANSFORM_SPECTRUM_INVARIANCE_COUNTER,
    TRANSFORM_SPECTRUM_INVARIANCE,
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

    # RELATIVE AND DIMENSIONLESS, scaled by the response (AW1). An absolute
    # tolerance on a displacement is what V1.3 exists to catch: the same problem
    # posed in millimetres moves the round-off floor three orders while the
    # tolerance stays put. Scaling also handles the components whose exact value
    # is zero, where no absolute floor is meaningful.
    scale = np.abs(u_loc).max()
    residual = np.abs(u_glo - r6.T @ u_loc).max() / scale
    assert residual <= TRANSFORM_INVARIANCE, (
        f"scaled response residual {residual:.3e} exceeds "
        f"{TRANSFORM_INVARIANCE:.0e}; a coupling entry in T^T K T is wrong"
    )


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
    assert np.allclose(
        ev_loc, ev_glo, rtol=0, atol=TRANSFORM_SPECTRUM_INVARIANCE * scale
    )


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
    assert shift >= TRANSFORM_SPECTRUM_INVARIANCE_COUNTER, (
        f"a non-orthogonal transform shifted the spectrum by only {shift:.3e}, "
        f"below the declared counter-case {TRANSFORM_SPECTRUM_INVARIANCE_COUNTER:.3e}"
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

    If roll-invariance held for `I_y != I_z` too, the test above would be
    insensitive to the triad entirely and would certify rather than test.

    **This control builds the local matrix BY HAND, and that is a deliberate
    weakening that has to be stated.** `Section` refuses to represent `I_y !=
    I_z` -- correctly, since the only shapes it supports are circular -- so there
    is no production route to an unequal section, and this control therefore
    reaches the element by a path production code cannot take. It demonstrates
    that the *transformation* is roll-sensitive when the bending stiffnesses
    differ; it does not exercise the section machinery.

    The earlier version of this control was worse: it constructed `I_y != I_z`
    while labelling the shape `thin_tube`, which drew the circular `kappa` and
    the circular `J` for a section that was neither. That object is now refused
    at construction (AW3), which is what surfaced the guard being on the
    classmethod rather than on the type.
    """
    from floatfea.element.beam import bending_stiffness

    ei_z, ei_y = 3.0e9, 1.0e9          # deliberately unequal
    k_loc = np.zeros((12, 12))
    kz = bending_stiffness(ei_z, L, 0.1)
    ky = bending_stiffness(ei_y, L, 0.1)
    flip = np.diag([1.0, -1.0, 1.0, -1.0])
    k_loc[np.ix_([1, 5, 7, 11], [1, 5, 7, 11])] = kz
    k_loc[np.ix_([2, 4, 8, 10], [2, 4, 8, 10])] = flip @ ky @ flip

    a = np.array([0.0, 0.0, 0.0])
    b = a + L * SKEW[0]
    k_ref = to_global(k_loc, rotation_matrix(a, b))
    k_rolled = to_global(k_loc, rotation_matrix(a, b, roll_rad=np.radians(37.0)))
    assert not np.allclose(
        k_ref, k_rolled, rtol=0, atol=TRANSFORM_INVARIANCE * np.abs(k_ref).max()
    ), "roll did not change an unequal-section member; the test is triad-blind"


def test_an_incoherent_section_is_REFUSED_at_construction() -> None:
    """AW3: the guard is on the TYPE, not on one construction path.

    `Section(...)` previously accepted any `J` and any `shape` with no check --
    so `basis.torsion_constant` guarded only `circular_tube`, and the claim that
    a non-circular section fails loudly at construction was false for any caller
    using the plain constructor.
    """
    from floatfea.model.material import Section as S

    with pytest.raises(ValueError, match="circular but I_y"):
        S(A=1.0, I_y=1.0, I_z=3.0, J=2.0, shape="thin_tube")
    with pytest.raises(ValueError, match="no shear coefficient"):
        S(A=1.0, I_y=1.0, I_z=1.0, J=2.0, shape="i_beam")
    with pytest.raises(ValueError, match=r"requires J = I_y \+ I_z"):
        S(A=1.0, I_y=1.0, I_z=1.0, J=99.0, shape="thin_tube")
    with pytest.raises(ValueError, match="must be positive"):
        S(A=-1.0, I_y=1.0, I_z=1.0, J=2.0, shape="thin_tube")


def test_the_supported_section_still_constructs() -> None:
    """Meta-test: a guard that refuses everything would pass every test above."""
    s = Section.circular_tube(0.6, 0.012)
    assert s.I_y == s.I_z and s.J == pytest.approx(s.I_y + s.I_z)


def test_the_displacement_counter_case_is_reachable() -> None:
    """AW1: the counter must be measured in the SAME quantity as the assertion.

    The assertion is on a scaled displacement residual, so the counter is too --
    perturbing the CORRECT rotation by the non-orthogonal `I + [theta x]` map,
    rather than substituting an unrelated rotation.

    A first version substituted `I + [theta x]` for the rotation entirely and
    measured ~12.6 at every theta, because it was comparing a response under one
    rotation against an expectation under a different one. That number was not a
    counter-case; it was a mismatch.
    """
    a, b, o = _triad_from(SKEW)
    r = rotation_matrix(a, b, orientation_node=o)
    k_loc = local_stiffness(SEC, S355, L)
    free = [6, 7, 8, 9, 10, 11]
    r6 = np.zeros((6, 6))
    r6[:3, :3] = SKEW
    r6[3:, 3:] = SKEW

    theta = 1.0e-8
    th = np.array([theta, -0.6 * theta, 0.4 * theta])
    kx = np.array([[0, -th[2], th[1]], [th[2], 0, -th[0]], [-th[1], th[0], 0]])
    bad = transformation((np.eye(3) + kx) @ r)
    k_bad = bad.T @ k_loc @ bad

    worst = 0.0
    for dof in range(6):
        f = np.zeros(6)
        f[dof] = LOAD
        u_loc = np.linalg.solve(k_loc[np.ix_(free, free)], f)
        u_bad = np.linalg.solve(k_bad[np.ix_(free, free)], r6.T @ f)
        worst = max(worst, np.abs(u_bad - r6.T @ u_loc).max() / np.abs(u_loc).max())

    assert worst >= TRANSFORM_INVARIANCE_COUNTER, (
        f"a non-orthogonality of {theta:.0e} rad produced a residual of only "
        f"{worst:.3e}, below the declared counter-case "
        f"{TRANSFORM_INVARIANCE_COUNTER:.3e}"
    )
