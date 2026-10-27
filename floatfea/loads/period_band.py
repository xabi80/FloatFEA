"""The sea-state admissibility screen: the associated-period band and the breaking limit.

**THE ONE DEFINITION (FL2(d), directives FU0 and FU1).** Before this module the
relation was written three times -- `scripts/measure/f6_results_report.py` twice and
`scripts/measure/member_forces_table.py` twice -- each with its own copy of `6.5`,
`11.0` and `1/7`, and each with its own gravity: two scripts declared
`GRAVITY = 9.80665` while the library declares `GRAVITY_MAGNITUDE = 9.81` and every
force in the model consumes it. Two more sites carried `9.81` as a bare literal, which
is the same defect wearing the right value.

The three coefficients are in `floatfea/basis.py` as cited physical constants; `g` is
`floatfea.io.frames.GRAVITY_MAGNITUDE`, the single source. Nothing in this module
declares a number.

What the screen decides, and what it does NOT
---------------------------------------------
It decides, per case, whether a `(T, H)` pair is an ADMISSIBLE sea state:

* **breaking** -- `H / lambda` exceeds the deep-water limiting steepness. The wave
  cannot exist at that height and period.
* **too short** / **too long** -- outside the associated-period band for that height.
* **in band** -- admissible.

It does **not** decide which case governs. That is a result of the run and is read from
the period column of the output (the FA0 caveat in `floatfea/cli.py` says so, and it is
still true). This module answers only "may this case set an envelope at all".

Why it exists: the measurement
------------------------------
The caveat `EZ2` has been published on every artifact since F4 -- *"only the declared
governing periods may set the envelope. Cases outside the associated-period range for
this wave height -- and any exceeding the deep-water breaking steepness -- are reported
as SENSITIVITY ONLY and cannot govern"* -- and until FL2(d) nothing in `floatfea/`
checked that the declared set was inside the range. One variable moved on the shipped
example, the breaking wave added to `load_cases.governing_periods` and everything else
held:

    governing_periods: [12.5, 14.0, 15.0, 16.2]          EXIT=0   U = 1.71167
    governing_periods: [10.0, 12.5, 14.0, 15.0, 16.2]    EXIT=0   U = 2.78942

`T = 10 s` at `H = 24.2 m` has `H / lambda = 0.155`, above `1/7`. It set the governing
utilisation 63% high, at exit 0, in a `utilisation.csv` that carried the caveat denying
it could. That is the state this module is built to refuse.

FA0 and the override
--------------------
`T = 12.5 s` at `H = 24.2 m` sits `0.042 s` (`0.3%`) BELOW `sqrt(6.5 H) = 12.542 s` and
FA0 rules that it governs anyway: it was chosen as the band's lower edge, the response
rises as `T` falls across the band, so the lower edge is what governs and `12.5 s`
represents it. So an out-of-band case that governs is a REAL, SHIPPED configuration and
not a corner -- which is why FL2(d)'s "unless the config says otherwise" is a declared
override (`load_cases.out_of_band_governing`) and not a tolerance on the band edge.

A tolerance would have been the wrong mechanism and it is worth saying why: a band edge
widened by `0.3%` to admit `12.5 s` would silently admit every other case within `0.3%`
of an edge, at every height, forever. The override admits ONE declared period and names
it in every artifact.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Final

from floatfea.basis import (
    ASSOCIATED_PERIOD_HIGH_COEFF,
    ASSOCIATED_PERIOD_LOW_COEFF,
    BREAKING_STEEPNESS_LIMIT,
)
from floatfea.io.frames import GRAVITY_MAGNITUDE

__all__ = [
    "Admissibility",
    "CaseBand",
    "associated_period_band",
    "classify_case",
    "deep_water_wavelength",
    "steepness",
]


class Admissibility(Enum):
    """Why a case may or may not set an envelope.

    Four outcomes decided ONCE (R944's lesson: the prose below one table decided the
    same question with `sqrt(6.5 * H) <= 12.5`, one edge of a two-edged interval, and
    published "INSIDE" for a case the band's upper edge had moved past).

    `BREAKING` is tested FIRST and reported in preference to a band verdict, because a
    wave that cannot exist is a stronger statement than a wave of the wrong period --
    and because the two are not exclusive: at `H = 24.2 m`, `T = 10 s` is both breaking
    and below the band.
    """

    IN_BAND = "in band"
    BREAKING = "breaking"
    TOO_SHORT = "too short for this height"
    TOO_LONG = "too long for this height"

    @property
    def may_govern(self) -> bool:
        """Whether this outcome admits the case to the envelope with no declaration."""
        return self is Admissibility.IN_BAND


@dataclass(frozen=True)
class CaseBand:
    """One case's screen result, with every figure the report needs.

    Every field is carried rather than recomputed by the consumer, because a consumer
    that recomputes `lambda` from its own `g` is the defect FU0 exists to remove.
    """

    period_full_s: float
    height_full_m: float
    wavelength_m: float
    steepness: float
    band_low_s: float
    band_high_s: float
    verdict: Admissibility

    @property
    def may_govern(self) -> bool:
        return self.verdict.may_govern

    @property
    def margin_s(self) -> float:
        """Signed distance OUTSIDE the band, in seconds; 0.0 when inside.

        Negative below the lower edge, positive above the upper. FA0's case is
        `-0.042`. A reader of a refusal needs to know whether a case missed by a
        rounding's worth or by four seconds, and this is that number.
        """
        if self.period_full_s < self.band_low_s:
            return self.period_full_s - self.band_low_s
        if self.period_full_s > self.band_high_s:
            return self.period_full_s - self.band_high_s
        return 0.0

    def describe(self) -> str:
        """One line, for a report row or a refusal message."""
        core = (
            f"T = {self.period_full_s:g} s at H = {self.height_full_m:g} m: "
            f"{self.verdict.value}; band {self.band_low_s:.3f} .. "
            f"{self.band_high_s:.3f} s, H/lambda = {self.steepness:.4f} "
            f"(limit {BREAKING_STEEPNESS_LIMIT:.4f})"
        )
        if self.margin_s:
            core += f", outside by {self.margin_s:+.3f} s"
        return core


# The screen's inputs are physical quantities and both have a floor that is a FACT
# rather than a threshold: a period of zero has no wavelength, and a negative height is
# not a wave. Neither is a tolerance -- there is no epsilon here and no value that could
# be loosened to make a test pass. `WAVE_HEIGHT`'s declared domain in
# `floatfea/run/config.py` already refuses a negative height at the reader (R881); this
# refuses it again at the one place that takes its square root, because a module that
# can be called from a test or a script does not get to assume its caller validated.
_POSITIVE: Final[str] = "must be positive"


def deep_water_wavelength(period_full_s: float) -> float:
    """`lambda = g T^2 / (2 pi)`, the deep-water dispersion relation.

    `g` is `floatfea.io.frames.GRAVITY_MAGNITUDE` -- FloatSim's 9.81, which every force
    in the model is computed with. See FU0: using the standard 9.80665 here instead put
    the screen and the loads in two different worlds and moved six published figures.
    """
    if not math.isfinite(period_full_s) or period_full_s <= 0.0:
        raise ValueError(f"period {period_full_s!r} s {_POSITIVE} and finite")
    lam = GRAVITY_MAGNITUDE * period_full_s * period_full_s / (2.0 * math.pi)
    # **R1020: THE PERIOD BEING POSITIVE DOES NOT MAKE THE WAVELENGTH POSITIVE.** `T^2`
    # underflows for a `T` this function's own check admits: at `T = 1e-170` the product
    # is exactly `0.0`, so `steepness` raised `ZeroDivisionError` out of the screen, and
    # at `T = 1e-160` it is `1.56e-320` and `H/lambda` is `inf` -- which the screen then
    # reads as BREAKING, a verdict from an infinity. This is the function's OWN invariant
    # and not a second copy of the reader's domain check (R1019): R994 forbids a refusal
    # that CANNOT fire, and this one fires on an input the check above lets through.
    if lam <= 0.0:
        raise ValueError(
            f"period {period_full_s!r} s gives a wavelength that underflows to {lam!r} m; "
            f"`g T^2 / (2 pi)` is not representable at this period, so no steepness can "
            f"be formed from it"
        )
    return lam


def steepness(period_full_s: float, height_full_m: float) -> float:
    """`H / lambda` in deep water."""
    if not math.isfinite(height_full_m) or height_full_m < 0.0:
        raise ValueError(f"wave height {height_full_m!r} m must be finite and >= 0")
    lam = deep_water_wavelength(period_full_s)
    s = height_full_m / lam
    # **R1020, the other half: a POSITIVE wavelength does not make a FINITE steepness.**
    # At `T = 1e-160` the wavelength is `1.56e-320` -- denormal but positive, so the check
    # inside `deep_water_wavelength` admits it -- and `H/lambda` is `inf`. `classify_case`
    # then compares `inf > BREAKING_STEEPNESS_LIMIT` and returns BREAKING: a verdict about
    # a sea state, formed from an infinity, with nothing saying so. Refused by name here
    # because this is the one place the quotient exists.
    if not math.isfinite(s):
        raise ValueError(
            f"period {period_full_s!r} s and height {height_full_m!r} m give a steepness "
            f"of {s!r} (wavelength {lam!r} m); no admissibility verdict can be formed "
            f"from it"
        )
    return s


def associated_period_band(height_full_m: float) -> tuple[float, float]:
    """`(sqrt(6.5 H), sqrt(11 H))` in seconds -- DNV practice; see `floatfea.basis`."""
    if not math.isfinite(height_full_m) or height_full_m < 0.0:
        raise ValueError(f"wave height {height_full_m!r} m must be finite and >= 0")
    return (
        math.sqrt(ASSOCIATED_PERIOD_LOW_COEFF * height_full_m),
        math.sqrt(ASSOCIATED_PERIOD_HIGH_COEFF * height_full_m),
    )


def classify_case(period_full_s: float, height_full_m: float) -> CaseBand:
    """The screen, for one case. The ONE place the four outcomes are decided."""
    low, high = associated_period_band(height_full_m)
    s = steepness(period_full_s, height_full_m)
    if s > BREAKING_STEEPNESS_LIMIT:
        verdict = Admissibility.BREAKING
    elif period_full_s < low:
        verdict = Admissibility.TOO_SHORT
    elif period_full_s > high:
        verdict = Admissibility.TOO_LONG
    else:
        verdict = Admissibility.IN_BAND
    return CaseBand(
        period_full_s=float(period_full_s),
        height_full_m=float(height_full_m),
        wavelength_m=deep_water_wavelength(period_full_s),
        steepness=s,
        band_low_s=low,
        band_high_s=high,
        verdict=verdict,
    )
