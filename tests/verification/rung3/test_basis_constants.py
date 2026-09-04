"""The project basis: values, and the identities that pin them (AP2/AS1/AS2).

`sigma_allow` and `kappa` have each appeared with two values in two documents.
These tests pin the values against their stated sources so a second value cannot
be introduced silently.
"""
from __future__ import annotations

import math

import pytest

from floatfea import basis as sec
from floatfea.tolerances import ROUNDOFF_IDENTITY


def test_sigma_allow_is_the_project_basis_not_a_safety_factor() -> None:
    """0.6 f_y, per docs/milestones/F1.md sec. 8 -- NOT f_y/1.5.

    The two differ by 11.11% exactly, and F2's first brace sweep used the wrong
    one. This asserts which basis is in force, and that the other is measurably
    different rather than an equivalent rounding.
    """
    assert sec.SIGMA_ALLOW_S355 == pytest.approx(213.0e6)
    assert sec.ALLOWABLE_FACTOR == 0.6
    wrong = sec.FY_S355 / 1.5
    assert wrong / sec.SIGMA_ALLOW_S355 == pytest.approx(1.1111, abs=1e-4)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged


def test_kappa_matches_cowper() -> None:
    """Cowper (1966) Table 1 at nu = 0.3."""
    assert sec.kappa("thin_tube", 0.3) == pytest.approx(0.5305, abs=5e-4)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged
    assert sec.kappa("solid_circular", 0.3) == pytest.approx(0.8864, abs=5e-4)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged


def test_kappa_depends_on_BOTH_shape_and_nu() -> None:
    """AS1: kappa belongs to neither container alone, so it cannot be a field.

    If it varied with only one of the two, storing it on that one would be
    defensible and the computed-not-stored rule would be ceremony.
    """
    assert sec.kappa("thin_tube", 0.3) != sec.kappa("solid_circular", 0.3)
    assert sec.kappa("thin_tube", 0.0) != sec.kappa("thin_tube", 0.5)


def test_an_unknown_shape_RAISES_rather_than_defaulting() -> None:
    """A silent fallback to a tube value on a non-tube section is the
    two-different-beams failure this module exists to prevent."""
    with pytest.raises(ValueError, match="no shear coefficient"):
        sec.kappa("i_beam", 0.3)


def test_the_shear_geometric_bound_is_invariant_in_slenderness() -> None:
    """Phi * (P/P_E) <= 12 sigma_allow / (kappa G pi^2), lambda cancelling.

    Asserted against the closed form AND a direct evaluation at several
    slendernesses: the invariance is the whole argument for not refining k_g, and
    if it held only approximately the deferral would be a judgement, not a proof.
    """
    import math

    b = sec.shear_geometric_bound()
    assert b == pytest.approx(0.006043, abs=5e-6)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged
    g = sec.E_STEEL / (2 * (1 + sec.NU_STEEL))
    c_phi = 12 * sec.E_STEEL / (sec.kappa("thin_tube") * g)
    c_pe = sec.SIGMA_ALLOW_S355 / (math.pi**2 * sec.E_STEEL)
    for lam in (15.0, 30.0, 46.4, 70.0, 140.0):
        assert (c_phi / lam**2) * (c_pe * lam**2) == pytest.approx(b, rel=ROUNDOFF_IDENTITY)


def test_it_is_a_BOUND_understressed_members_sit_below_it() -> None:
    """AT1: the identity is at sigma_actual; the BOUND is at sigma_allow.

    A member carrying half its allowable stress has half the product, so the
    bound covers the whole model rather than the strength-sized subset. Asserting
    this is what makes it a bound rather than an identity quoted as one.
    """
    import math

    g = sec.E_STEEL / (2 * (1 + sec.NU_STEEL))
    bound = sec.shear_geometric_bound()
    for util in (1.0, 0.5, 0.1):
        sigma_actual = util * sec.SIGMA_ALLOW_S355
        actual = 12 * sigma_actual / (sec.kappa("thin_tube") * g * math.pi**2)
        assert actual <= bound + 1e-15
        if util < 1.0:
            assert actual < bound


@pytest.mark.parametrize(
    "fy, expected", [(235e6, 0.00400), (355e6, 0.00604), (460e6, 0.00783)]
)
def test_the_bound_scales_with_the_material_and_survives_all_of_them(
    fy: float, expected: float
) -> None:
    """If it ever breaks it will be the material or the allowable basis, never
    the geometry -- so the scaling is pinned across the structural steels."""
    assert sec.shear_geometric_bound(fy=fy) == pytest.approx(expected, abs=5e-5)  # not-a-tolerance: reference pin -- the recorded per-material bound
    assert sec.shear_geometric_bound(fy=fy) < 0.01  # not-a-tolerance: fixture property -- bounds an input, not a computed discrepancy


def test_kappa_is_distinguishable_from_the_simple_argument() -> None:
    """The 6% gap is the whole reason kappa is pinned.

    If Cowper's thin-tube value happened to equal the shear-flow 0.5, the pin
    would be ceremony -- a verification test could use either and never notice.
    """
    simple = 0.5
    assert abs(sec.kappa("thin_tube", 0.3) - simple) / simple > 0.05  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small


def test_chs_class_limits_follow_the_code_formula() -> None:
    c1, c2, c3 = sec.chs_class_limits(sec.FY_S355)
    eps2 = 235e6 / sec.FY_S355
    assert (c1, c2, c3) == pytest.approx((50 * eps2, 70 * eps2, 90 * eps2))
    assert c3 == pytest.approx(59.6, abs=0.1)  # not-a-tolerance: reference pin, not a ceiling -- asserts a RECORDED measurement is unchanged


def test_shear_modulus_is_derived_not_declared() -> None:
    """G must follow from E and nu, or the three can drift apart."""
    assert sec.G_STEEL == pytest.approx(sec.E_STEEL / (2 * (1 + sec.NU_STEEL)))


@pytest.mark.parametrize("d,t", [(0.6, 0.012), (2.5, 0.18), (0.9, 0.015)])
def test_tube_properties_are_exact_not_thin_walled(d: float, t: float) -> None:
    """G3.3 asks for EXACT section properties.

    The thin-wall approximations (A = pi D t, I = pi D^3 t / 8) are close but not
    equal; asserting the difference is visible stops an approximation being
    substituted later without notice.
    """
    a_exact = sec.tube_area(d, t)
    i_exact = sec.tube_second_moment(d, t)
    a_thin = math.pi * d * t
    i_thin = math.pi * d**3 * t / 8.0
    assert a_exact == pytest.approx(math.pi * (d**2 - (d - 2 * t) ** 2) / 4)
    assert a_exact < a_thin          # thin-wall over-states area
    assert i_exact < i_thin
    assert abs(i_exact - i_thin) / i_exact > 1e-3, "difference too small to detect a swap"  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small


def test_radius_of_gyration_is_consistent_with_area_and_inertia() -> None:
    r = sec.tube_radius_of_gyration(0.9, 0.015)
    assert r == pytest.approx(
        math.sqrt(sec.tube_second_moment(0.9, 0.015) / sec.tube_area(0.9, 0.015))
    )
    # Thin tube: r -> D / (2 sqrt 2) = 0.3536 D. Exact is slightly below.
    assert 0.34 < r / 0.9 < 0.3536  # not-a-tolerance: fixture property -- asserts the fixture is in a usable range
