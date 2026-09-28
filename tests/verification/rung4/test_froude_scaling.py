"""DS2: the Froude converter, and the round-trip that a wrong exponent reddens.

DR4(c) declared the exponent table. `floatfea/io/froude.py` does not carry that
table — it carries three bases and derives everything dimensionally — so the two
are pinned to each other here rather than one being trusted.

**The round-trip is not the whole test and would be vacuous alone.** Scaling up
and back down composes `lambda**n` with `lambda**-n`, which returns the input for
*any* `n`, right or wrong. So the round-trip proves the inverse is an inverse, and
the DECLARED TABLE proves the exponents; the counter perturbs one exponent at a
time and requires the table comparison to redden.
"""

from __future__ import annotations

import numpy as np
import pytest

from floatfea.io.froude import (
    DIMENSIONS,
    LENGTH_EXPONENT,
    MASS_EXPONENT,
    TIME_EXPONENT,
    Dimensions,
    assumption_record,
    froude_factor,
    provenance,
    to_full_scale,
    to_model_scale,
)
from floatfea.tolerances import ROUNDOFF_IDENTITY

DECLARED = {
    "length": 1.0,
    "time": 0.5,
    "force": 3.0,
    "moment": 4.0,
    "acceleration": 0.0,
    "mass": 3.0,
    "inertia": 5.0,
}
"""DR4(c)'s table, transcribed. Every row is checked against the derivation."""

LAMBDA = 50.0
"""not-a-tolerance: the model's Froude scale, an INPUT to every call below.
It appears in an equality against the provenance field that must echo it, which
is a comparison of a recorded value against the value recorded -- not a threshold
on a measurement."""


def test_the_derived_exponents_match_the_DECLARED_table() -> None:
    """The directive's seven rows against the dimensional derivation.

    This is the assertion that carries the physics. If a base is wrong, or a
    quantity's dimensions are wrong, a row here disagrees.
    """
    for quantity, declared in DECLARED.items():
        derived = DIMENSIONS[quantity].froude_exponent()
        assert derived == pytest.approx(declared, abs=ROUNDOFF_IDENTITY), (
            f"{quantity}: DR4(c) declares lambda^{declared:g} and the dimensional "
            f"derivation gives lambda^{derived:g}. One of the three bases or this "
            "quantity's dimensions is wrong."
        )


def test_every_quantity_the_SCHEMA_carries_has_dimensions() -> None:
    """A quantity with no dimensions recorded must RAISE, not default.

    `CLAUDE.md`: never assume a unit. An unknown quantity silently scaled by
    `lambda**0` would be the assumption this table exists to prevent.
    """
    with pytest.raises(ValueError, match="unknown quantity"):
        froude_factor("bending_stiffness_nobody_declared", LAMBDA)
    with pytest.raises(ValueError, match="must be positive"):
        froude_factor("length", 0.0)


@pytest.mark.parametrize("quantity", sorted(DIMENSIONS))
def test_the_ROUND_TRIP_returns_the_input(quantity: str) -> None:
    """Up then down is the identity, for every quantity the schema carries.

    Proves the inverse is an inverse. It does NOT prove the exponent, which is
    what the declared-table test above is for, and the next test measures exactly
    how blind this one is.
    """
    rng = np.random.default_rng(20260928)
    values = rng.standard_normal(64) * 1e3
    back = to_model_scale(to_full_scale(values, quantity, LAMBDA), quantity, LAMBDA)
    worst = float(np.max(np.abs(back - values))) / float(np.max(np.abs(values)))
    assert (
        worst <= ROUNDOFF_IDENTITY
    ), f"{quantity}: the round trip does not return its input -- {worst:.4e}"


def test_a_WRONG_EXPONENT_on_any_ONE_quantity_reddens(capsys, monkeypatch) -> None:
    """DS2's counter. One quantity at a time, and the round trip cannot see it.

    Each of DR4(c)'s seven rows is perturbed by one in the length dimension --
    the smallest change that alters an exponent -- and the declared-table
    comparison must redden for that row. The round-trip test is run against the
    same perturbation to measure how blind it is: it passes every time, because
    `lambda**n` composed with `lambda**-n` is the identity for any `n`.
    """
    import floatfea.io.froude as froude

    survived_table: list[str] = []
    survived_round_trip: list[str] = []
    for quantity in DECLARED:
        broken = dict(DIMENSIONS)
        original = broken[quantity]
        broken[quantity] = Dimensions(
            length=original.length + 1.0, time=original.time, mass=original.mass
        )
        with monkeypatch.context() as patch:
            patch.setattr(froude, "DIMENSIONS", broken)
            derived = broken[quantity].froude_exponent()
            if derived == pytest.approx(DECLARED[quantity], abs=ROUNDOFF_IDENTITY):
                survived_table.append(quantity)
            values = np.array([1.0, -2.5, 1e4])
            factor = froude.froude_factor(quantity, LAMBDA)
            back = (values * factor) / factor
            worst = float(np.max(np.abs(back - values))) / float(np.max(np.abs(values)))
            if worst <= ROUNDOFF_IDENTITY:
                survived_round_trip.append(quantity)

    with capsys.disabled():
        print(
            f"\n  one exponent perturbed, {len(DECLARED)} quantities:"
            f"\n    the DECLARED-TABLE check misses  {len(survived_table)}"
            f"\n    the ROUND TRIP misses            {len(survived_round_trip)}"
        )

    assert not survived_table, (
        f"a wrong exponent on {survived_table} does not redden the declared-table "
        "comparison, so that check cannot see the defect DS2 names."
    )
    assert len(survived_round_trip) == len(DECLARED), (
        "the round trip caught a wrong exponent, which it cannot do by "
        "construction -- so this control is measuring something other than what "
        "it says, and the claim that the round trip is blind would be unfounded."
    )


def test_the_ASSUMPTIONS_record_names_the_scale_and_the_bases() -> None:
    """`CLAUDE.md`: a transformation in use is recorded so a result computed under
    it can never be mistaken for one measured directly."""
    text = assumption_record(LAMBDA)
    assert "lambda = 50" in text
    assert "MODEL scale" in text
    for base in ("length lambda^1", "time lambda^0.5", "mass lambda^3"):
        assert base in text, f"the assumptions record does not state {base!r}"

    fields = provenance(LAMBDA)
    assert fields["scale"] == "full", (
        "a scaled record must DECLARE full scale. The schema's `scale` field is "
        "'declared, never a factor to apply', and after this conversion the "
        "declaration is true: no consumer applies anything further."
    )
    assert fields["source_scale"] == "model"
    # An identity on a DECLARATION: the provenance field must echo the scale the
    # caller passed in. Both sides are the same recorded input, so there is no
    # measurement here to set a threshold on.
    echoed = fields["froude_lambda"]
    assert echoed == LAMBDA  # not-a-tolerance: the input, echoed back
    assert fields["froude_exponents"]["moment"] == pytest.approx(4.0, abs=ROUNDOFF_IDENTITY)


def test_the_BASES_are_the_three_Froude_similitude_says_they_are() -> None:
    """A guard on the bases themselves, since everything else derives from them.

    Froude number equality `v / sqrt(gL)` invariant with `g` unchanged gives
    `v ~ lambda^(1/2)`, hence time `~ lambda^(1/2)` for length `~ lambda`. Mass
    `~ lambda^3` is geometric scaling at constant density. If any of the three
    moves, every derived exponent moves with it and the declared-table test is
    what would catch it -- this names the reason so a reader does not have to
    reconstruct it.
    """
    assert (LENGTH_EXPONENT, TIME_EXPONENT, MASS_EXPONENT) == (1.0, 0.5, 3.0)
    velocity = DIMENSIONS["velocity"].froude_exponent()
    assert velocity == pytest.approx(0.5, abs=ROUNDOFF_IDENTITY), (
        f"velocity scales as lambda^{velocity:g}; Froude similitude requires "
        "lambda^0.5, and that is the equality the whole law rests on."
    )
    assert DIMENSIONS["acceleration"].froude_exponent() == pytest.approx(
        0.0, abs=ROUNDOFF_IDENTITY
    ), (
        "acceleration must be lambda^0 -- gravity is the same at both scales, "
        "which is what makes Froude scaling applicable at all."
    )
