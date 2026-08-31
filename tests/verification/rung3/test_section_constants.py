"""Single-source constants: the values, and the identities that pin them (AP2).

`sigma_allow` and `kappa` have each appeared with two values in two documents.
These tests pin the values against their stated sources so a second value cannot
be introduced silently.
"""
from __future__ import annotations

import math

import pytest

from floatfea import sections as sec


def test_sigma_allow_is_the_project_basis_not_a_safety_factor() -> None:
    """0.6 f_y, per docs/milestones/F1.md sec. 8 -- NOT f_y/1.5.

    The two differ by 11.11% exactly, and F2's first brace sweep used the wrong
    one. This asserts which basis is in force, and that the other is measurably
    different rather than an equivalent rounding.
    """
    assert sec.SIGMA_ALLOW_S355 == pytest.approx(213.0e6)
    assert sec.ALLOWABLE_FACTOR == 0.6
    wrong = sec.FY_S355 / 1.5
    assert wrong / sec.SIGMA_ALLOW_S355 == pytest.approx(1.1111, abs=1e-4)


def test_kappa_matches_cowper() -> None:
    """Cowper (1966) Table 1 at nu = 0.3."""
    assert sec.kappa_thin_tube(0.3) == pytest.approx(0.5305, abs=5e-4)
    assert sec.kappa_solid_circular(0.3) == pytest.approx(0.8864, abs=5e-4)


def test_kappa_is_distinguishable_from_the_simple_argument() -> None:
    """The 6% gap is the whole reason kappa is pinned.

    If Cowper's thin-tube value happened to equal the shear-flow 0.5, the pin
    would be ceremony -- a verification test could use either and never notice.
    """
    simple = 0.5
    assert abs(sec.kappa_thin_tube(0.3) - simple) / simple > 0.05


def test_chs_class_limits_follow_the_code_formula() -> None:
    c1, c2, c3 = sec.chs_class_limits(sec.FY_S355)
    eps2 = 235e6 / sec.FY_S355
    assert (c1, c2, c3) == pytest.approx((50 * eps2, 70 * eps2, 90 * eps2))
    assert c3 == pytest.approx(59.6, abs=0.1)


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
    assert abs(i_exact - i_thin) / i_exact > 1e-3, "difference too small to detect a swap"


def test_radius_of_gyration_is_consistent_with_area_and_inertia() -> None:
    r = sec.tube_radius_of_gyration(0.9, 0.015)
    assert r == pytest.approx(
        math.sqrt(sec.tube_second_moment(0.9, 0.015) / sec.tube_area(0.9, 0.015))
    )
    # Thin tube: r -> D / (2 sqrt 2) = 0.3536 D. Exact is slightly below.
    assert 0.34 < r / 0.9 < 0.3536
