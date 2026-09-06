"""The member-level admission limit: `L/D >= 2` refuses (BH0, Q5).

ONE LIMIT NOW, NOT TWO. `warn_outside_validated_domain` and its
`G22_VALIDATED_MEMBER_LAMBDA` boundary are gone with the quantity they belonged
to (F2.md sec. 5b, Q6): the floor they tracked is the forward error of a linear
solve, which G2.2 reports and no longer asserts, so there is nothing left for a
warning to be about. `member_lambda` survives as a reported diagnostic and is
still tested here for being a DIFFERENT axis from `L/D`.
"""
from __future__ import annotations

import pytest

from floatfea.model.admissibility import (assert_beam_admissible,
                                          member_l_over_d, member_lambda)
from floatfea.model.material import Section
from floatfea.testing import assert_close, assert_differs
from floatfea.tolerances import BEAM_ADMISSION_L_OVER_D, ROUNDOFF_IDENTITY

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


def test_the_two_ratios_are_DIFFERENT_axes() -> None:
    """`L/D` asks whether this is a beam; `L/r` asks how high a SOLVE's floor is.

    Conflating them is what F2.md sec. D7 item 5 had to correct once already.
    Only the first is a limit now; the second is reported.
    """
    assert_differs(member_l_over_d(9.67, SEC), member_lambda(9.67, SEC),
                   by=0.5, floor=1e-12,
                   what="L/D against L/r on the same member")
