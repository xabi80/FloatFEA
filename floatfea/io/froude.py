"""Froude scaling at the I/O boundary: model-scale FloatSim output to full scale.

WHY THIS IS AT THE BOUNDARY AND NOWHERE ELSE. `CLAUDE.md` § Conventions: "No unit
conversion happens anywhere except at the I/O boundary." A Froude scale change is a
unit change, so it happens here, once, on the way in — and never again.

**What ENFORCES that is `floatfea.io.reader._validate_scale`, not this sentence
(R577).** The first version of this docstring said "nothing downstream of the reader
multiplies anything by `lambda`", which was true only because nothing called this
module at all — an unenforced property stated as a design guarantee. The reader now
refuses a record whose `scale` is absent, unrecognised, or `"model"`, and refuses a
converted record that does not carry `froude_lambda` and the FROUDE-SCALED sentence.
A model-scale record therefore cannot reach anything downstream.

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
at all for a derived quantity. The derivation is pinned to the table DR4(c)
declared, in `tests/verification/rung4/test_froude_scaling.py`, so neither is
trusted on its own — and the counter there injects a wrong exponent through THIS
module, which is what makes the pinning load-bearing rather than decorative.

WHAT THIS MODULE DOES NOT DO. It does not decide which channels a record carries,
it does not read or write the file format, and it does not know what a `.flr`
record is. It answers one question — *given a quantity's dimensions, what is its
Froude factor* — and applies it to arrays.
"""

from __future__ import annotations

import math
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
"""The SCALAR quantities declared so far, by dimensions.

**It is not every quantity the schema carries, and the first version of this
sentence said it was (C5).** The schema carries `area[P]` on panels and on plate
patches, and `froude_factor("area", 50)` raises. The raise is correct — an
undeclared quantity must not be silently scaled by `lambda**0` — but a sentence
claiming completeness is the sentence that stops someone checking. This table is
DR4(c)'s seven rows plus the ones the work has needed since; it grows by addition,
not by assumption.

`angle` and `density` have exponent zero and are listed rather than omitted,
because silence about them would read as an oversight instead of a decision.

Quantities whose columns do NOT share one dimension are not here. They are in
`COMPOSITE_BLOCKS`, with the column map declared.
"""


COMPOSITE_BLOCKS: Final[dict[str, tuple[tuple[int, int, str], ...]]] = {
    "wrench": ((0, 3, "force"), (3, 6, "moment")),
    "body_dof": ((0, 3, "length"), (3, 6, "angle")),
    "body_dof_velocity": ((0, 3, "velocity"), (3, 6, "angular_velocity")),
    "body_dof_acceleration": ((0, 3, "acceleration"), (3, 6, "angular_acceleration")),
    "joint_multiplier_yaw_locked": ((0, 3, "force"), (3, 4, "moment")),
    "joint_multiplier_hinge": ((0, 3, "force"), (3, 5, "moment")),
}
"""Arrays whose columns do NOT share one dimension, with the column map declared.

R579. The schema marks `/loads/<body>/radiation/mu[N,6]` and
`/joints/<id>/lam[N,n_rows]` REQUIRED, and both stack force with moment. Scaling
either as `"force"` leaves the moment columns short by exactly `lambda`; scaling
it as `"moment"` leaves the force columns long by the same factor. Neither raised.
Both results look like numbers.

The joint rows follow the joint's own constraint structure, which
`floatsim/bodies/joints.py` fixes: `yaw_locked` is three translational rows plus
one rotational lock (4), `hinge` is three plus two (5). Verified against the
assembled 12-buoy deck: 16 of 16 joints are `yaw_locked` at 4 rows, 64 rows total.
"""

COMPOSITE_WIDTHS: Final[frozenset[int]] = frozenset(
    blocks[-1][1] for blocks in COMPOSITE_BLOCKS.values()
)
"""The trailing-axis widths a composite occupies: 4, 5 and 6."""


def _checked_lambda(lam: float) -> float:
    """The scale factor, or a refusal.

    R581: `lam <= 0.0` is False for nan, so the original guard let a nan scale
    through into every quantity in a record and `inf` and `1e-300` with it. A
    validation failure must not degrade to a warning, and returning nan is a
    degradation past a warning to nothing at all.
    """
    value = float(lam)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(
            f"the Froude scale must be finite and positive; got {lam!r}. nan, inf "
            "and a subnormal all pass an unguarded `lam <= 0` and then propagate "
            "silently into every scaled channel."
        )
    return value


def froude_factor(quantity: str, lam: float) -> float:
    """`lambda ** n` for a SCALAR `quantity`. Raises on anything else."""
    value = _checked_lambda(lam)
    if quantity in COMPOSITE_BLOCKS:
        raise ValueError(
            f"{quantity!r} is a composite: its columns do not share one exponent, "
            "so there is no single factor to return. Scale the array with "
            "to_full_scale/to_model_scale, which applies each block's own factor."
        )
    try:
        dims = DIMENSIONS[quantity]
    except KeyError:
        raise ValueError(
            f"unknown quantity {quantity!r}; add it to DIMENSIONS with its "
            "dimensions rather than with a factor. A quantity whose dimensions "
            "nobody wrote down is a quantity nobody checked."
        ) from None
    exponent = dims.froude_exponent()
    try:
        factor = float(value**exponent)
    except OverflowError:
        factor = math.inf
    # A finite positive `lam` is not enough: `lam = 1e-300` is finite and positive
    # and `lam**3` UNDERFLOWS to 0.0, which annihilates every value it multiplies.
    # This is not a threshold on a measurement -- it asks whether the factor is
    # representable at all, which is why no tolerance is involved.
    if not math.isfinite(factor) or factor == 0.0:
        raise ValueError(
            f"lambda**{exponent:g} is not representable for lambda = {value!r} "
            f"(it evaluates to {factor!r}). A factor that underflows to zero "
            f"annihilates every value it scales and one that overflows to inf "
            f"poisons them; neither is caught by a guard on lambda alone."
        )
    return factor


def _refuse_uncovered(values: NDArray[np.float64], quantity: str) -> None:
    """Refuse a SCALAR quantity declared over an array it does not cover (R579).

    An array whose trailing axis is a declared composite width is a stacked
    mixed-dimension channel in this schema -- `mu[N,6]`, `lam[N,4]`, `lam[N,5]` --
    and applying one exponent to it under-scales half of it silently. A wrong
    answer that looks right is worse than a crash, so this is a refusal.

    WHAT THIS DOES NOT COVER, said plainly rather than implied away: a ONE-
    dimensional array of exactly 4, 5 or 6 samples of a genuinely scalar channel is
    indistinguishable from a single unstacked wrench, and this guard lets it
    through. The schema puts time on the leading axis, so a 1-D array is a scalar
    channel over time and a composite is always 2-D; refusing 1-D on width alone
    would refuse correct calls. The residual case is a single wrench passed without
    its time axis, and nothing in the schema has that shape.
    """
    if values.ndim >= 2 and values.shape[-1] in COMPOSITE_WIDTHS:
        raise ValueError(
            f"{quantity!r} is one exponent and this array's trailing axis is "
            f"{values.shape[-1]}, a declared composite width. In this schema an "
            f"array of that shape stacks channels of different dimensions -- "
            f"mu[N,6] is force in columns 0:3 and moment in 3:6, lam[N,n_rows] is "
            f"three force rows and one or two moment rows. Name the composite "
            f"instead: {sorted(COMPOSITE_BLOCKS)}. Scaling it as a single quantity "
            f"would leave half the columns wrong by a factor of lambda, silently."
        )


def _scale(
    values: NDArray[np.floating] | float, quantity: str, lam: float, *, up: bool
) -> NDArray[np.float64] | float:
    """Shared body of `to_full_scale` and `to_model_scale`."""
    _checked_lambda(lam)
    if quantity in COMPOSITE_BLOCKS:
        blocks = COMPOSITE_BLOCKS[quantity]
        array = np.asarray(values, dtype=np.float64)
        width = blocks[-1][1]
        if array.ndim < 1 or array.shape[-1] != width:
            raise ValueError(
                f"{quantity!r} occupies {width} columns; got an array of shape "
                f"{array.shape}. The column map is declared and is not inferred "
                "from the data."
            )
        out = array.copy()
        for start, stop, part in blocks:
            factor = froude_factor(part, lam)
            out[..., start:stop] = (
                array[..., start:stop] * factor if up else array[..., start:stop] / factor
            )
        return out

    factor = froude_factor(quantity, lam)
    if isinstance(values, (int, float)) and not isinstance(values, bool):
        return float(values) * factor if up else float(values) / factor
    array = np.asarray(values, dtype=np.float64)
    _refuse_uncovered(array, quantity)
    return array * factor if up else array / factor


def to_full_scale(
    values: NDArray[np.floating] | float, quantity: str, lam: float
) -> NDArray[np.float64] | float:
    """Scale model-scale `values` of `quantity` to full scale.

    `quantity` is either a scalar entry in `DIMENSIONS` or a composite in
    `COMPOSITE_BLOCKS`, in which case each declared column block gets its own
    factor.
    """
    return _scale(values, quantity, lam, up=True)


def to_model_scale(
    values: NDArray[np.floating] | float, quantity: str, lam: float
) -> NDArray[np.float64] | float:
    """The inverse. Present so the round-trip test has a real inverse to compose."""
    return _scale(values, quantity, lam, up=False)


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
