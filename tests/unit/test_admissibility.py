"""The two member-level limits: one refuses, one warns (BH0, Q5/Q6)."""
from __future__ import annotations

import pytest

from floatfea.model.admissibility import (OutsideValidatedDomain,
                                          assert_beam_admissible,
                                          member_l_over_d, member_lambda,
                                          warn_outside_validated_domain)
from floatfea.model.material import Section
from floatfea.testing import assert_close, assert_differs
from floatfea.tolerances import (BEAM_ADMISSION_L_OVER_D,
                                 G22_VALIDATED_MEMBER_LAMBDA,
                                 ROUNDOFF_IDENTITY)

SEC = Section.circular_tube(0.6, 0.012)


def test_the_outer_diameter_is_recovered_exactly() -> None:
    """`D` comes from `A` and `I`, so a section built any way reports the same."""
    for d, t in ((0.6, 0.012), (2.0, 0.04), (0.1, 0.002), (0.6, 0.29)):
        sec = Section.circular_tube(d, t)
        # L/D with L = D is 1/D, so multiplying back recovers D exactly.
        got = float(d * member_l_over_d(d, sec))
        assert_close(got, d, ROUNDOFF_IDENTITY, floor=1e-16,
                     what=f"recovered outer diameter for D={d}, t={t}")


def test_a_stubby_member_is_REFUSED() -> None:
    """`L/D < 2` is not a beam. Raises, never warns -- it is a modelling error."""
    with pytest.raises(ValueError, match="admission limit"):
        assert_beam_admissible(1.0, Section.circular_tube(2.0, 0.04), what="stub")


def test_an_admissible_member_passes_silently() -> None:
    """The meta-test: a guard that refuses everything is not a guard."""
    assert_beam_admissible(9.67, SEC, what="the gate's own member")
    assert member_l_over_d(9.67, SEC) > BEAM_ADMISSION_L_OVER_D


def test_a_slender_member_WARNS_and_does_not_raise() -> None:
    """Past G2.2's validated domain the element is right and the floor is higher.

    A warning, not a refusal, and not CLAUDE.md's forbidden warning: nothing is
    invalid here. The distinction is written out in the function's docstring.
    """
    long_enough = (G22_VALIDATED_MEMBER_LAMBDA + 40.0) * (SEC.I_z / SEC.A) ** 0.5
    with pytest.warns(OutsideValidatedDomain, match="validated domain"):
        ratio = warn_outside_validated_domain(long_enough, SEC, what="slender")
    assert ratio > G22_VALIDATED_MEMBER_LAMBDA


def test_a_member_INSIDE_the_domain_does_not_warn() -> None:
    """The other half: it must be silent where the claim holds."""
    import warnings

    inside = (G22_VALIDATED_MEMBER_LAMBDA - 20.0) * (SEC.I_z / SEC.A) ** 0.5
    with warnings.catch_warnings():
        warnings.simplefilter("error", OutsideValidatedDomain)
        warn_outside_validated_domain(inside, SEC, what="inside")


def test_the_two_limits_are_DIFFERENT_axes() -> None:
    """`L/D` asks whether this is a beam; `L/r` asks how high the floor has risen.

    Conflating them is what F2.md sec. D7 item 5 had to correct once already.
    """
    assert_differs(member_l_over_d(9.67, SEC), member_lambda(9.67, SEC),
                   by=0.5, floor=1e-12,
                   what="L/D against L/r on the same member")
