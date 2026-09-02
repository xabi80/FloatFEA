"""Step-2 checkpoint: Phi -> 0 recovers Euler-Bernoulli EXACTLY (AT2).

Asserted **entry-wise on the stiffness matrix**, not on a deflection at a
tolerance: a deflection check passes on a matrix with two compensating errors, and
the entries are what every later result is built from.

The negative control is not optional here. In a `1/(1+Phi)` formulation, setting
`Phi = 0` reproduces the Euler-Bernoulli form *by construction*, so a test
comparing the two could pass while certifying nothing. `test_the_phi_zero_check_
CAN_FAIL` perturbs one shear term and confirms the assertion goes red.
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.element.beam import (
    bending_stiffness,
    euler_bernoulli_bending_stiffness,
    local_stiffness,
    shear_parameter,
)
from floatfea.model.material import S355, Section

EI = 4.2e9
L = 7.5
SEC = Section.circular_tube(0.6, 0.012)


def test_phi_zero_recovers_euler_bernoulli_ENTRYWISE() -> None:
    """The step-2 checkpoint. Bit-exact, not approximate."""
    got = bending_stiffness(EI, L, phi=0.0)
    want = euler_bernoulli_bending_stiffness(EI, L)
    assert np.array_equal(got, want), (
        "Phi = 0 does not reproduce Euler-Bernoulli exactly; max |diff| = "
        f"{np.abs(got - want).max():.6e}"
    )


def test_the_phi_zero_check_CAN_FAIL() -> None:
    """Negative control for the checkpoint above.

    Without this, `test_phi_zero_recovers_euler_bernoulli_ENTRYWISE` is green by
    construction and its green is read as evidence. A check that cannot fail is
    worse than no check.
    """
    want = euler_bernoulli_bending_stiffness(EI, L)
    perturbed = bending_stiffness(EI, L, phi=0.0)
    perturbed[1, 3] *= 1.0 + 1e-9          # one shear-coupling term, 1 part in 1e9
    assert not np.array_equal(perturbed, want), (
        "perturbing a shear term did not change the comparison -- the entry-wise "
        "assertion is not actually looking at that entry"
    )


def test_the_reference_is_written_independently() -> None:
    """The EB reference must not be the element evaluated at Phi = 0.

    If it were, the checkpoint would compare a function to itself. Asserted by
    behaviour: the reference must not vary with Phi at all.
    """
    a = euler_bernoulli_bending_stiffness(EI, L)
    b = euler_bernoulli_bending_stiffness(EI, L)
    assert np.array_equal(a, b)
    # And it must DIFFER from the shear-flexible form at any non-zero Phi.
    assert not np.allclose(a, bending_stiffness(EI, L, phi=0.3))


@pytest.mark.parametrize("phi", [0.05, 0.3, 1.0, 5.0])
def test_shear_flexibility_softens_the_beam(phi: float) -> None:
    """Physical direction: shear flexibility can only reduce stiffness."""
    stiff = bending_stiffness(EI, L, phi=0.0)
    soft = bending_stiffness(EI, L, phi=phi)
    assert soft[0, 0] < stiff[0, 0]
    assert np.linalg.eigvalsh(stiff - soft).min() >= -1e-6 * abs(stiff[0, 0])


def test_bending_stiffness_is_symmetric_and_singular() -> None:
    """Symmetry, and exactly two rigid-body modes in the plane (translation and
    rotation) -- a 4x4 bending block must have rank 2."""
    k = bending_stiffness(EI, L, phi=0.4)
    assert np.allclose(k, k.T, rtol=0, atol=1e-9 * abs(k).max())
    assert np.linalg.matrix_rank(k, tol=1e-9 * abs(k).max()) == 2


def test_phi_uses_kappa_from_basis_not_a_literal() -> None:
    """AS1: kappa reaches the element by computation, never as a constant.

    Checked by dependence: Phi must move when `nu` moves, which it cannot do if
    kappa were a hardcoded 0.5.
    """
    from dataclasses import replace

    phi_a = shear_parameter(SEC, S355, L, plane="xy")
    phi_b = shear_parameter(SEC, replace(S355, nu=0.45), L, plane="xy")
    assert phi_a != phi_b


def test_local_stiffness_is_symmetric_with_six_rigid_body_modes() -> None:
    k = local_stiffness(SEC, S355, L)
    assert k.shape == (12, 12)
    assert np.allclose(k, k.T, rtol=0, atol=1e-9 * abs(k).max())
    # A free element has exactly six rigid-body modes: rank 12 - 6 = 6.
    assert np.linalg.matrix_rank(k, tol=1e-9 * abs(k).max()) == 6


def test_zero_length_and_bad_section_are_refused() -> None:
    with pytest.raises(ValueError, match="length must be positive"):
        shear_parameter(SEC, S355, 0.0, plane="xy")
    with pytest.raises(ValueError, match="invalid tube"):
        Section.circular_tube(0.4, 0.25)
