"""The sea-state admissibility screen (FL2(d), `floatfea/loads/period_band.py`).

Every figure here is one the project has already PUBLISHED, so the module is checked
against the deliverables rather than against itself:

* the band at `H = 24.2 m` is `12.542 .. 16.316 s` -- `docs/closure/F4.md:180`;
* `T = 12.5 s` sits `0.042 s` below the lower edge -- FA0, `docs/F4_member_forces.md:68`;
* `T = 10 s` and `T = 20 s` are the two cases outside, `T = 10 s` by breaking steepness
  -- EZ2(b), `docs/F4_member_forces.md:40`.

A module that reproduced none of those would be a new screen wearing the old one's name.
"""

from __future__ import annotations

import math

import pytest

from floatfea.basis import (
    ASSOCIATED_PERIOD_HIGH_COEFF,
    ASSOCIATED_PERIOD_LOW_COEFF,
    BREAKING_STEEPNESS_LIMIT,
)
from floatfea.loads.period_band import (
    Admissibility,
    associated_period_band,
    classify_case,
    deep_water_wavelength,
    steepness,
)

# The shipped sea state. Not a module constant in `floatfea/` -- R902 is what one of
# those cost -- but the fixture this project's published figures were computed at.
H_PUBLISHED = 24.2

# The npz's six cases, and the verdict each is published under.
PUBLISHED_VERDICTS = {
    10.0: Admissibility.BREAKING,
    12.5: Admissibility.TOO_SHORT,
    14.0: Admissibility.IN_BAND,
    15.0: Admissibility.IN_BAND,
    16.2: Admissibility.IN_BAND,
    20.0: Admissibility.TOO_LONG,
}


def test_the_band_reproduces_the_PUBLISHED_edges_to_three_decimals() -> None:
    """`docs/closure/F4.md:180`: 12.542 .. 16.316 s at H = 24.2 m."""
    low, high = associated_period_band(H_PUBLISHED)
    assert f"{low:.3f}" == "12.542"
    assert f"{high:.3f}" == "16.316"


@pytest.mark.parametrize(("period", "expected"), sorted(PUBLISHED_VERDICTS.items()))
def test_every_published_case_gets_its_PUBLISHED_verdict(
    period: float, expected: Admissibility
) -> None:
    """EZ2(b) and FA0, case by case rather than as a set."""
    assert classify_case(period, H_PUBLISHED).verdict is expected


def test_FA0s_case_is_short_by_the_PUBLISHED_margin() -> None:
    """`0.042 s` below the lower edge -- the figure FA0's ruling turns on."""
    case = classify_case(12.5, H_PUBLISHED)
    assert f"{case.margin_s:.3f}" == "-0.042"
    # And it cannot govern on the band alone, which is WHY FA0 had to rule.
    assert not case.may_govern


def test_only_IN_BAND_may_govern() -> None:
    """The one place `may_govern` is decided, over every outcome rather than one."""
    for verdict in Admissibility:
        assert verdict.may_govern is (verdict is Admissibility.IN_BAND)


def test_BREAKING_is_reported_in_preference_to_the_band_when_BOTH_apply() -> None:
    """`T = 10 s` at `H = 24.2 m` is breaking AND below the band; breaking is published.

    Not a style choice: a wave that cannot exist is a stronger statement than a wave of
    the wrong period, and a reader told only "too short" would look for a longer period
    at the same height -- which at `T = 12.5 s` is still breaking at `H = 30 m`.
    """
    case = classify_case(10.0, H_PUBLISHED)
    low, _high = associated_period_band(H_PUBLISHED)
    assert low > 10.0, "the premise moved: T = 10 s is no longer below the band"
    assert case.steepness > BREAKING_STEEPNESS_LIMIT
    assert case.verdict is Admissibility.BREAKING


def test_the_wavelength_and_the_steepness_agree_with_the_CLOSED_FORM() -> None:
    """`lambda = g T^2 / (2 pi)` and `H/lambda`, bit-exact against the expression."""
    from floatfea.io.frames import GRAVITY_MAGNITUDE

    for period in sorted(PUBLISHED_VERDICTS):
        lam = GRAVITY_MAGNITUDE * period * period / (2.0 * math.pi)
        assert deep_water_wavelength(period) == lam
        assert steepness(period, H_PUBLISHED) == H_PUBLISHED / lam
        case = classify_case(period, H_PUBLISHED)
        assert case.wavelength_m == lam
        assert case.steepness == H_PUBLISHED / lam


# ---------------------------------------------------------------------------
# EH4: every boundary solved in BOTH directions, including the ones that WEAKEN
# the screen.
# ---------------------------------------------------------------------------
def test_EH4_the_band_edges_are_INCLUSIVE_at_exactly_the_edge() -> None:
    """A case AT the edge is in band. Solved at the edge itself, not near it."""
    low, high = associated_period_band(H_PUBLISHED)
    assert classify_case(low, H_PUBLISHED).verdict is Admissibility.IN_BAND
    assert classify_case(high, H_PUBLISHED).verdict is Admissibility.IN_BAND
    assert classify_case(low, H_PUBLISHED).margin_s == 0.0
    assert classify_case(high, H_PUBLISHED).margin_s == 0.0


def test_EH4_the_WEAKENING_direction_on_the_band_the_period_rises_until_it_trips() -> None:
    """How far may a period rise past the upper edge before the screen notices?

    The strengthening question is "does a clearly-out case trip", and it does. The
    weakening one is the next representable float: `nextafter(high, inf)` must already
    be TOO_LONG, or the screen has a blind sliver above its own edge.
    """
    _low, high = associated_period_band(H_PUBLISHED)
    just_over = math.nextafter(high, math.inf)
    assert just_over > high
    assert classify_case(just_over, H_PUBLISHED).verdict is Admissibility.TOO_LONG
    assert classify_case(just_over, H_PUBLISHED).margin_s > 0.0


def test_EH4_the_WEAKENING_direction_on_the_band_the_period_falls_until_it_trips() -> None:
    """The same at the lower edge: one float below must already be TOO_SHORT."""
    low, _high = associated_period_band(H_PUBLISHED)
    just_under = math.nextafter(low, -math.inf)
    assert just_under < low
    assert classify_case(just_under, H_PUBLISHED).verdict is Admissibility.TOO_SHORT
    assert classify_case(just_under, H_PUBLISHED).margin_s < 0.0


def test_EH4_the_WEAKENING_direction_on_BREAKING_the_steepness_falls_to_the_limit() -> None:
    """At EXACTLY the limit the wave is admissible; one float above it is breaking.

    The limit is `>`, not `>=`, so the height that puts `H/lambda` exactly on `1/7` is
    NOT breaking. Both sides are solved here because the direction that weakens the
    screen -- the limit rising, so a breaking wave passes -- is the one no round had run.
    """
    period = 10.0
    lam = deep_water_wavelength(period)
    at_limit = BREAKING_STEEPNESS_LIMIT * lam
    assert steepness(period, at_limit) == pytest.approx(BREAKING_STEEPNESS_LIMIT)
    assert classify_case(period, at_limit).verdict is not Admissibility.BREAKING

    # And a height that is unambiguously above it, so the test does not rest on which
    # side of the limit a rounded product lands.
    assert classify_case(period, at_limit * 1.01).verdict is Admissibility.BREAKING


def test_EH4_a_LOWER_sea_state_moves_the_band_DOWN_and_a_published_case_changes_side() -> None:
    """The band depends on `H`, so a verdict is not a property of `T` alone.

    `T = 20 s` is TOO_LONG at `H = 24.2 m`. At `H = 36.4 m` the upper edge is
    `sqrt(11 * 36.4) = 20.01 s` and the same period is IN BAND. This is the measurement
    that makes "the verdict travels with the height" checkable rather than asserted --
    and it is the class R902 found, where a module constant height decided a band while
    the header printed a recorded one.
    """
    assert classify_case(20.0, H_PUBLISHED).verdict is Admissibility.TOO_LONG
    taller = 36.4
    _low, high = associated_period_band(taller)
    assert high > 20.0
    assert classify_case(20.0, taller).verdict is Admissibility.IN_BAND


# ---------------------------------------------------------------------------
# The refusals. Not tolerances: there is no epsilon and no value here that could
# be loosened to make a test pass.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("period", [0.0, -1.0, -0.0, float("nan"), float("inf")])
def test_a_NONPOSITIVE_or_nonfinite_period_is_REFUSED_not_divided_by(period: float) -> None:
    """`lambda` is zero at `T = 0`, so the steepness would be a division by zero."""
    with pytest.raises(ValueError, match="period"):
        deep_water_wavelength(period)
    with pytest.raises(ValueError):
        classify_case(period, H_PUBLISHED)


@pytest.mark.parametrize("height", [-1.0, -24.2, float("nan"), float("-inf")])
def test_a_NEGATIVE_or_nonfinite_height_is_REFUSED_rather_than_square_rooted(
    height: float,
) -> None:
    """A negative height is not a wave (R881), and `sqrt` of one is a `ValueError`
    whose message says nothing about waves."""
    with pytest.raises(ValueError, match="height"):
        associated_period_band(height)
    with pytest.raises(ValueError, match="height"):
        steepness(10.0, height)
    with pytest.raises(ValueError, match="height"):
        classify_case(10.0, height)


def test_a_ZERO_height_is_admitted_and_collapses_the_band_to_a_POINT() -> None:
    """`H = 0` is calm water, not an error: the band is `0 .. 0` and nothing is in it.

    Reported rather than refused, because the refusal belongs to the configuration
    reader -- `WAVE_HEIGHT`'s declared domain is `0.0 .. 100.0` m, so zero is a legal
    recorded value and this module must say something true about it rather than raise.
    """
    assert associated_period_band(0.0) == (0.0, 0.0)
    assert steepness(10.0, 0.0) == 0.0
    case = classify_case(10.0, 0.0)
    assert case.verdict is Admissibility.TOO_LONG
    assert not case.may_govern


def test_the_three_COEFFICIENTS_come_from_basis_and_not_from_this_module() -> None:
    """FU1: the coefficients live in `floatfea/basis.py`, cited, and are consumed here.

    Checked by VALUE through the published band rather than by import, so moving a
    coefficient in `basis.py` and leaving a copy here would fail.
    """
    low, high = associated_period_band(H_PUBLISHED)
    assert low == math.sqrt(ASSOCIATED_PERIOD_LOW_COEFF * H_PUBLISHED)
    assert high == math.sqrt(ASSOCIATED_PERIOD_HIGH_COEFF * H_PUBLISHED)
    assert (ASSOCIATED_PERIOD_LOW_COEFF, ASSOCIATED_PERIOD_HIGH_COEFF) == (6.5, 11.0)
    assert BREAKING_STEEPNESS_LIMIT == 1.0 / 7.0


def test_describe_names_the_verdict_the_band_and_the_steepness() -> None:
    """The one line a report row or a refusal message is built from."""
    text = classify_case(12.5, H_PUBLISHED).describe()
    assert "T = 12.5 s" in text
    assert "H = 24.2 m" in text
    assert "too short for this height" in text
    assert "12.542 .. 16.316 s" in text
    assert "outside by -0.042 s" in text
