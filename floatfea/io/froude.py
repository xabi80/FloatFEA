"""Froude scaling at the I/O boundary: model-scale FloatSim output to full scale.

WHY THIS IS AT THE BOUNDARY AND NOWHERE ELSE. `CLAUDE.md` § Conventions: "No unit
conversion happens anywhere except at the I/O boundary." A Froude scale change is a
unit change, so it happens here, once, on the way in — and never again. Nothing
downstream of the reader multiplies anything by `lambda`.

RECONCILED WITH THE LOCKED SCHEMA, because a reader will notice the tension.
`docs/load-interchange-v1.md` § 2 says of `scale`::

    scale    "full" | "model" -- declared, never a factor to apply

That constrains the **reader**: a record declaring `model` must not be silently
multiplied by whatever the consumer assumes. It does not forbid a converter from
producing a record that genuinely IS full scale and declares itself so. After this
module runs, `scale` is `"full"` and it is true — no consumer applies anything.
**The `lambda` that was applied is recorded in `assumptions` and in provenance**, so
a result computed at model scale can never be mistaken for one measured at full
scale, which is the property that line exists to protect.

THE EXPONENTS ARE DERIVED, NOT LISTED, and that is the whole design. Froude
similitude fixes three base exponents::

    length   lambda^1
    time     lambda^(1/2)      (Froude number equality: v/sqrt(gL) invariant)
    mass     lambda^3          (geometric scaling at constant density)

Everything else follows from its dimensions. A table of nine numbers can be
mistyped in nine places; three bases and a dimensional product cannot be mistyped
at all for a derived quantity. `test_the_derived_exponents_match_the_DECLARED_table`
checks the derivation against the table DR4(c) declared, so the two are pinned to
each other rather than one being trusted.

WHAT THIS MODULE DOES NOT DO. It does not decide which channels a record carries,
it does not read or write the file format, and it does not know what a `.flr`
record is. It answers one question — *given a quantity's dimensions, what is its
Froude factor* — and applies it to arrays.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import numpy as np
from numpy.typing import NDArray

LENGTH_EXPONENT: Final[float] = 1.0
TIME_EXPONENT: Final[float] = 0.5
MASS_EXPONENT: Final[float] = 3.0
"""The three Froude bases.

not-a-tolerance: exponents of an exact similitude law, not thresholds. Nothing is
compared against them. They are `Final` because a scale law is not configuration.
"""


@dataclass(frozen=True)
class Dimensions:
    """A quantity's dimensions as powers of length, time and mass."""

    length: float = 0.0
    time: float = 0.0
    mass: float = 0.0

    def froude_exponent(self) -> float:
        """The power of `lambda` this quantity scales by."""
        return self.length * LENGTH_EXPONENT + self.time * TIME_EXPONENT + self.mass * MASS_EXPONENT


DIMENSIONS: Final[dict[str, Dimensions]] = {
    "length": Dimensions(length=1),
    "time": Dimensions(time=1),
    "mass": Dimensions(mass=1),
    "angle": Dimensions(),
    "velocity": Dimensions(length=1, time=-1),
    "acceleration": Dimensions(length=1, time=-2),
    "angular_velocity": Dimensions(time=-1),
    "angular_acceleration": Dimensions(time=-2),
    "force": Dimensions(length=1, time=-2, mass=1),
    "moment": Dimensions(length=2, time=-2, mass=1),
    "inertia": Dimensions(length=2, mass=1),
    "pressure": Dimensions(length=-1, time=-2, mass=1),
    "force_per_length": Dimensions(time=-2, mass=1),
    "density": Dimensions(length=-3, mass=1),
    "frequency": Dimensions(time=-1),
}
"""Every quantity the interchange schema carries, by dimensions.

`angle` and `density` have exponent zero and are listed rather than omitted: a
quantity absent from this table raises, and silence about angle would read as an
oversight instead of a decision.
"""


def froude_factor(quantity: str, lam: float) -> float:
    """`lambda ** n` for `quantity`. Raises on an unknown quantity."""
    if lam <= 0.0:
        raise ValueError(f"the Froude scale must be positive; got {lam}")
    try:
        dims = DIMENSIONS[quantity]
    except KeyError:
        raise ValueError(
            f"unknown quantity {quantity!r}; add it to DIMENSIONS with its "
            "dimensions rather than with a factor. A quantity whose dimensions "
            "nobody wrote down is a quantity nobody checked."
        ) from None
    return float(lam ** dims.froude_exponent())


def to_full_scale(
    values: NDArray[np.floating] | float, quantity: str, lam: float
) -> NDArray[np.float64] | float:
    """Scale model-scale `values` of `quantity` to full scale."""
    factor = froude_factor(quantity, lam)
    if isinstance(values, (int, float)):
        return float(values) * factor
    return np.asarray(values, dtype=np.float64) * factor


def to_model_scale(
    values: NDArray[np.floating] | float, quantity: str, lam: float
) -> NDArray[np.float64] | float:
    """The inverse. Present so the round-trip test has a real inverse to compose."""
    factor = froude_factor(quantity, lam)
    if isinstance(values, (int, float)):
        return float(values) / factor
    return np.asarray(values, dtype=np.float64) / factor


def assumption_record(lam: float) -> str:
    """The sentence that goes in the record's `assumptions` block.

    `CLAUDE.md` § Non-negotiables requires any fallback or transformation in use to
    be recorded in `assumptions` and surfaced in the run log, "so that a result
    computed under a fallback can never be mistaken for one computed under full
    data". A scale change is exactly that kind of transformation.
    """
    return (
        f"FROUDE-SCALED from model scale to full scale at lambda = {lam:g}. "
        f"Bases: length lambda^{LENGTH_EXPONENT:g}, time lambda^{TIME_EXPONENT:g}, "
        f"mass lambda^{MASS_EXPONENT:g}; every other quantity's exponent is derived "
        "from its dimensions by floatfea.io.froude. The underlying FloatSim run was "
        "executed at MODEL scale and no quantity in this record was measured at full "
        "scale."
    )


def provenance(lam: float) -> dict[str, object]:
    """The provenance fields a scaled record carries beside `assumptions`."""
    return {
        "scale": "full",
        "froude_lambda": lam,
        "froude_bases": {
            "length": LENGTH_EXPONENT,
            "time": TIME_EXPONENT,
            "mass": MASS_EXPONENT,
        },
        "froude_exponents": {
            name: dims.froude_exponent() for name, dims in sorted(DIMENSIONS.items())
        },
        "source_scale": "model",
    }
