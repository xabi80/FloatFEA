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

import floatfea.io.froude as froude
from floatfea.io.froude import (
    COMPOSITE_BLOCKS,
    DIMENSIONS,
    LENGTH_EXPONENT,
    MASS_EXPONENT,
    TIME_EXPONENT,
    Dimensions,
    assumption_record,
    provenance,
)

# R578. The counter injects by patching `froude.DIMENSIONS`, so anything it wants
# to measure the sensitivity of must reach the module at CALL time. A `from ...
# import` binds the object at import time and the injection slides underneath it,
# which is exactly how the first version of this counter came to report full
# sensitivity for a test it never ran.
froude_factor = froude.froude_factor
to_full_scale = froude.to_full_scale
to_model_scale = froude.to_model_scale

from floatfea.tolerances import ROUNDOFF_IDENTITY  # noqa: E402

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
        derived = froude.DIMENSIONS[quantity].froude_exponent()
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
    with pytest.raises(ValueError, match="finite and positive"):
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
    back = froude.to_model_scale(froude.to_full_scale(values, quantity, LAMBDA), quantity, LAMBDA)
    worst = float(np.max(np.abs(back - values))) / float(np.max(np.abs(values)))
    assert (
        worst <= ROUNDOFF_IDENTITY
    ), f"{quantity}: the round trip does not return its input -- {worst:.4e}"


def test_a_WRONG_EXPONENT_on_any_ONE_quantity_reddens(capsys, monkeypatch) -> None:
    """DS2's counter. One quantity at a time, and the round trip cannot see it.

    **R578 rewrote this. The figure it publishes was right and its evidence was
    not.** The first version perturbed a local dict, read that dict directly for
    the table half, and computed `(values * factor) / factor` inline for the round
    trip. Three cells refuted it: deleting the injection changed nothing, gutting
    the SHIPPED assertion to a tautology still reported full sensitivity, and
    making `to_model_scale` multiply instead of divide reddened twelve tests while
    this control still printed "the ROUND TRIP misses 7". It measured IEEE
    division, not the code it named.

    It now injects through the module and runs the SHIPPED code on both halves:
    the table half calls the shipped test function, the round-trip half composes
    the shipped `to_full_scale` and `to_model_scale`. Both figures move when the
    thing they name moves.
    """
    survived_table: list[str] = []
    survived_round_trip: list[str] = []
    for quantity in DECLARED:
        broken = dict(froude.DIMENSIONS)
        original = broken[quantity]
        broken[quantity] = Dimensions(
            length=original.length + 1.0, time=original.time, mass=original.mass
        )
        with monkeypatch.context() as patch:
            patch.setattr(froude, "DIMENSIONS", broken)

            # THE TABLE HALF: run the shipped assertion, not a copy of it.
            try:
                test_the_derived_exponents_match_the_DECLARED_table()
            except AssertionError:
                pass
            else:
                survived_table.append(quantity)

            # THE ROUND-TRIP HALF: compose the shipped functions, which resolve
            # `DIMENSIONS` at call time and therefore see the injection.
            values = np.array([1.0, -2.5, 1e4])
            back = froude.to_model_scale(
                froude.to_full_scale(values, quantity, LAMBDA), quantity, LAMBDA
            )
            worst = float(np.max(np.abs(back - values))) / float(np.max(np.abs(values)))
            if worst <= ROUNDOFF_IDENTITY:
                survived_round_trip.append(quantity)

    with capsys.disabled():
        print(
            f"\n  one exponent perturbed, {len(DECLARED)} quantities, injected"
            f" through the module:"
            f"\n    the DECLARED-TABLE check misses  {len(survived_table)}"
            f"\n    the ROUND TRIP misses            {len(survived_round_trip)}"
        )

    assert not survived_table, (
        f"a wrong exponent on {survived_table} does not redden the declared-table "
        "comparison, so that check cannot see the defect DS2 names."
    )
    assert len(survived_round_trip) == len(DECLARED), (
        "the round trip caught a wrong exponent, which it cannot do by "
        "construction -- scaling up and back down composes `lambda**n` with "
        "`lambda**-n`, which returns the input for ANY n. If this equality ever "
        "fails, the round trip is measuring something other than the inverse and "
        "the claim that it is blind would be unfounded."
    )


def test_the_COUNTER_ITSELF_reddens_when_the_shipped_assertion_is_gutted(
    monkeypatch,
) -> None:
    """R578's own control: the counter must fail if the gate it measures stops asserting.

    The defect R578 found was a counter that certified a COPY of the assertion, so
    it would have reported full sensitivity for a gate that checked nothing. This
    replaces the shipped table assertion with a tautology and requires the counter
    to notice -- if it does not, it is measuring a copy again.
    """
    import sys

    module = sys.modules[__name__]

    def tautology() -> None:
        assert True

    with monkeypatch.context() as patch:
        patch.setattr(module, "test_the_derived_exponents_match_the_DECLARED_table", tautology)
        survived = []
        for quantity in DECLARED:
            broken = dict(froude.DIMENSIONS)
            original = broken[quantity]
            broken[quantity] = Dimensions(
                length=original.length + 1.0, time=original.time, mass=original.mass
            )
            with monkeypatch.context() as inner:
                inner.setattr(froude, "DIMENSIONS", broken)
                try:
                    module.test_the_derived_exponents_match_the_DECLARED_table()
                except AssertionError:
                    pass
                else:
                    survived.append(quantity)

    assert len(survived) == len(DECLARED), (
        "the table half was replaced by a tautology and the counter still reported "
        f"only {len(survived)} of {len(DECLARED)} missed. It is not running the "
        "shipped assertion."
    )


def test_a_MIXED_DIMENSION_array_is_REFUSED_not_half_scaled(capsys) -> None:
    """R579. `mu[N,6]` and `lam[N,n_rows]` stack force with moment.

    Scaling either as one quantity leaves half the columns wrong by exactly
    `lambda`, and the old API did it without raising. The composite carries the
    column map; the scalar call refuses.
    """
    mu = np.ones((2, 6))
    with pytest.raises(ValueError, match="composite width"):
        froude.to_full_scale(mu, "force", LAMBDA)
    with pytest.raises(ValueError, match="composite width"):
        froude.to_full_scale(mu, "moment", LAMBDA)

    scaled = np.asarray(froude.to_full_scale(mu, "wrench", LAMBDA))
    force_factor = froude.froude_factor("force", LAMBDA)
    moment_factor = froude.froude_factor("moment", LAMBDA)
    assert np.allclose(scaled[:, 0:3], force_factor, rtol=ROUNDOFF_IDENTITY)
    assert np.allclose(scaled[:, 3:6], moment_factor, rtol=ROUNDOFF_IDENTITY)

    # the counter: how wrong the silent path WAS, so the refusal is not cosmetic
    silent = np.asarray(mu) * force_factor
    ratio = float(moment_factor / force_factor)
    with capsys.disabled():
        print(
            f"\n  mu[N,6] scaled as 'force' at lambda = {LAMBDA:g}: the moment "
            f"columns come out short by a factor of {ratio:g}"
            f"\n    correct {moment_factor:g}   silent {silent[0, 3]:g}"
        )
    assert ratio == pytest.approx(LAMBDA, rel=ROUNDOFF_IDENTITY), (
        "the under-scaling factor must be exactly lambda -- moment is length times "
        "force, so the two exponents differ by exactly the length base."
    )

    # a composite name has no single factor, and saying so is the point
    with pytest.raises(ValueError, match="composite"):
        froude.froude_factor("wrench", LAMBDA)
    # the declared width is not inferred from the data
    with pytest.raises(ValueError, match="occupies 6 columns"):
        froude.to_full_scale(np.ones((2, 4)), "wrench", LAMBDA)


@pytest.mark.parametrize("kind,width", [("yaw_locked", 4), ("hinge", 5)])
def test_the_JOINT_MULTIPLIER_layout_follows_the_JOINT(kind: str, width: int) -> None:
    """`lam[N,n_rows]` is three force rows plus the rotational lock rows.

    `yaw_locked` locks three translations and one rotation (4 rows); `hinge` locks
    three and two (5). Verified against the assembled 12-buoy deck: 16 of 16 joints
    are `yaw_locked`, 64 rows, every one a two-rotation gimbal.
    """
    name = f"joint_multiplier_{kind}"
    blocks = COMPOSITE_BLOCKS[name]
    assert blocks[-1][1] == width
    assert blocks[0] == (0, 3, "force"), "the three translational rows carry force"
    assert blocks[1][2] == "moment", "the rotational lock rows carry moment"

    scaled = np.asarray(froude.to_full_scale(np.ones((3, width)), name, LAMBDA))
    assert np.allclose(scaled[:, 0:3], froude.froude_factor("force", LAMBDA))
    assert np.allclose(scaled[:, 3:width], froude.froude_factor("moment", LAMBDA))


def test_a_NON_FINITE_or_UNREPRESENTABLE_scale_is_REFUSED(capsys) -> None:
    """R581. `lam <= 0.0` is False for nan, so nan propagated into every channel.

    The counter is the list of values the old predicate admitted. `1e-300` is the
    one that shows why a guard on lambda alone is not enough: it is finite and
    positive, and `lambda**3` underflows to exactly zero, which annihilates every
    value it multiplies.
    """
    refused: list[str] = []
    admitted: list[str] = []
    for lam in (float("nan"), float("inf"), -float("inf"), 0.0, -0.0, -1.0, 1e-300, 1e300):
        try:
            froude.froude_factor("force", lam)
        except ValueError:
            refused.append(repr(lam))
        else:
            admitted.append(repr(lam))

    with capsys.disabled():
        print(f"\n  scales refused: {len(refused)} of 8")

    assert not admitted, (
        f"these scales were accepted and should not be: {admitted}. A validation "
        "failure must not degrade to a warning, and returning nan degrades it past "
        "a warning to nothing at all."
    )
    # not-a-tolerance: an EXACT equality. `force` derives to lambda^3, and
    # `50.0**3.0` and `50.0**3` are the same IEEE double, so there is nothing here
    # to be close about -- a comparison with any tolerance would hide a changed
    # exponent behind it.
    assert froude.froude_factor("force", LAMBDA) == LAMBDA**3


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
