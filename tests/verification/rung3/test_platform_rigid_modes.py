"""G2.1 ON REAL MEMBERS (F3 § 5, R486, DD0, DI1).

Two assertions, per member of the real platform, on the member's OWN local
stiffness:

  * the six rigid motions about its midpoint are annihilated, to
    `RIGID_MODE_EXACTNESS`;
  * there is no SEVENTH mode at the arithmetic floor -- the first flexible mode
    sits at least `RIGID_MODE_BOUND` units of `||k_hat|| * eps` above it.

**WHAT THIS REPLACES.** R486 asked for the rigid-mode ceiling shown valid across
the whole admissible domain. DD0 moved that out of F2: "every admissible
configuration" is an open-ended domain and each round found one more axis of it.
Asserting the ceiling on the platform's own members is a stronger statement about
the structure being analysed and a weaker one about structures in general, and
the trade is deliberate.

**AND THERE IS NO NEAR-VERTICAL BAND TO MEASURE IN.** § 5 instructed that this
gate be measured first in that band, on the reasoning that a platform frame is
mostly near-vertical members. It is not: the frame is planar, `max |dz|` is `0.0`
exactly and every member is at 90 degrees from vertical. § 5 was re-locked under
EB0 to say so, and R486's original finding -- a defect-free element reading
`2.9994e-14` on a retired ASSEMBLED form at 2.87 degrees -- is not reachable on
this frame. This gate does not pretend to reach it.

**THE BUILDER REFUSES TOO**, in `floatfea.model.platform.check_rigid_modes`, and
the two are not redundant: this file says the sixteen members this deck produces
are sound, and the refusal says no other deck can produce one that is not.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

from floatfea.element.beam import local_stiffness
from floatfea.element.rigid import element_rigid_residual, seventh_over_epsilon
from floatfea.model.platform import build_superstructure
from floatfea.tolerances import RIGID_MODE_BOUND, RIGID_MODE_EXACTNESS

MEMBERS = 16
"""What the deck produces, asserted by `test_the_skeleton_is_FIVE_bodies_and_SIXTEEN_members`
in the sibling module. Named here so an empty parametrisation cannot pass."""


def member_stiffnesses() -> list[tuple[str, np.ndarray, float]]:
    """`(label, k_local, length)` for every member of the real platform.

    A MODULE-LEVEL FUNCTION, AND NOT A FIXTURE, so the counters below can replace
    it. The two cells in `tests/test_counters_are_injected.py` patch a module
    attribute; a fixture is resolved by pytest and cannot be reached that way.
    """
    s = build_superstructure()
    return [
        (m.label, local_stiffness(m.section, b.material, m.length), m.length)
        for b in s.bodies
        for m in b.members
    ]


def test_there_are_SIXTEEN_members_to_check() -> None:
    """A parse that finds nothing agrees with everything."""
    rows = member_stiffnesses()
    # expected: the member count the deck implies, asserted independently by
    # `test_platform_skeleton.py::test_the_skeleton_is_FIVE_bodies_and_SIXTEEN_members`
    # against data/platform/platform12_deck.yaml's joint list. Not counted from
    # the rows under test.
    assert len(rows) == MEMBERS, f"{len(rows)} members, not {MEMBERS}"
    assert len({r[0] for r in rows}) == MEMBERS, "two members share a label"


def test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions(capsys) -> None:
    """G2.1's first half, per member, element-local.

    ONE TEST OVER THE SIXTEEN rather than a parametrisation, because the counters
    registered against it inject into every member at once and the registry's
    cells call one function.
    """
    rows = member_stiffnesses()
    worst = 0.0
    worst_label = ""
    for label, k, length in rows:
        residual = element_rigid_residual(k, length)
        if residual > worst:
            worst, worst_label = residual, label
    with capsys.disabled():
        print(
            f"  worst element rigid residual {worst:.4e} on {worst_label}, "
            f"ceiling {RIGID_MODE_EXACTNESS:g}, margin "
            f"{RIGID_MODE_EXACTNESS / worst if worst else float('inf'):.2f}x"
        )
    # expected: RIGID_MODE_EXACTNESS, floatfea/tolerances.py, which is a pure
    # number because the residual is dimensionless and relative to the quantity
    # compared. The left side is the shipped `element_rigid_residual`, tied to
    # rung 1's independent copy by `test_G2_1_the_SHIPPED_residual_agrees_with_RUNG_ONEs`
    # below -- not to itself.
    assert worst <= RIGID_MODE_EXACTNESS, (
        f"{worst_label}: the element-local rigid residual is {worst:.6e}, above "
        f"{RIGID_MODE_EXACTNESS:g}. The member's own stiffness does not annihilate the "
        "six rigid motions about its midpoint."
    )


def test_G2_1_every_MEMBER_has_NO_SEVENTH_zero_mode(capsys) -> None:
    """G2.1's second half: the first FLEXIBLE mode is resolvably above the floor.

    Where it is not resolvable the outcome is UNDECIDABLE -- red, with the margin
    reported -- because the question cannot be answered in double precision at
    that conditioning, and a gate that answers anyway is worse than one that
    refuses.
    """
    rows = member_stiffnesses()
    over = [(seventh_over_epsilon(k, length), label) for label, k, length in rows]
    smallest, label = min(over)
    with capsys.disabled():
        print(
            f"  smallest seventh/eps {smallest:.4e} on {label}, needing "
            f"{RIGID_MODE_BOUND:g}, margin {smallest / RIGID_MODE_BOUND:.3e}x"
        )
    # expected: RIGID_MODE_BOUND, floatfea/tolerances.py, a pure number for the
    # same reason -- the ratio is measured in units of `||k_hat|| * eps`, which is
    # a property of the arithmetic and not of the structure.
    assert smallest >= RIGID_MODE_BOUND, (
        f"{label}: the first flexible mode sits at {smallest:.6e} units of "
        f"||k_hat||*eps, below {RIGID_MODE_BOUND:g}. Either there is a seventh mode "
        "at the floor, or the conditioning makes the question UNDECIDABLE."
    )


def test_G2_1_the_SHIPPED_residual_agrees_with_RUNG_ONEs() -> None:
    """Two implementations of one formula, compared, so neither can drift.

    `floatfea/element/rigid.py` exists because the builder's refusal cannot import
    from `tests/`. Rung 1 keeps its own copy: it is F2 apparatus and frozen under
    DR1, so it is not re-pointed here. What stops the two diverging is this.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "rung1"))
    try:
        import test_rigid_body_modes as rung1
    finally:
        sys.path.pop(0)

    worst = 0.0
    for _label, k, length in member_stiffnesses():
        # expected: rung 1's own `element_rigid_residual`, a separate
        # implementation of the same formula in
        # tests/verification/rung1/test_rigid_body_modes.py. Not the shipped one
        # under test.
        worst = max(
            worst, abs(element_rigid_residual(k, length) - rung1.element_rigid_residual(k, length))
        )
    assert worst == 0.0, (
        f"the shipped residual and rung 1's disagree by {worst:.6e} on the real "
        "platform's members. One formula, two implementations, and they have drifted."
    )


def test_G3_1b_the_DECK_the_model_reads_IS_the_one_G3_2_GATES() -> None:
    """G3.1b, and its COINCIDENCE with G3.1a stated rather than implied (DV0).

    G3.1b asks for the mass properties against the FloatSim body definitions. On
    this model those are the same numbers G3.1a B compares against, because the
    deck YAML IS the exported FloatSim definition -- so there is ONE comparison,
    not two independent ones, and the row is kept with the coincidence written
    down rather than left to imply a second witness.

    **AND THIS DOES NOT RE-HASH THE DECK.** A first version did, and it was two
    defects in one: it duplicated
    `test_platform_deck_export.py::test_the_committed_deck_matches_its_digest`,
    which already asserts `content_sha(raw) == golden["content_sha256"]`, and it
    hashed the RAW BYTES where that test hashes canonical JSON -- so it failed on
    a correct tree, because the committed file is CRLF on this platform and the
    digest is deliberately blind to that.

    What is left unasserted by G3.2 is the other end of the chain: that the file
    the MODEL reads is the file the exporter writes and G3.2 gates. Two modules
    each hold their own `data/platform/platform12_deck.yaml`, and nothing compared
    them.
    """
    from floatfea.model.platform import DECK_YAML as MODELS_DECK

    from . import test_platform_deck_export as export_gate

    # expected: `DECK_YAML` in tests/verification/rung3/test_platform_deck_export.py,
    # which is the path `test_the_committed_deck_matches_its_digest` hashes against
    # the golden, and which `scripts/export_platform_deck.py` writes as `OUT`. Not
    # read from the model's own constant.
    assert MODELS_DECK.resolve() == export_gate.DECK_YAML.resolve(), (
        f"the model reads {MODELS_DECK} and G3.2 gates {export_gate.DECK_YAML}. "
        "G3.1b's properties are then compared against a file whose provenance "
        "nothing checks."
    )


# --------------------------------------------------------------------------
# THE THREE COUNTERS ARE NOT REGISTERED HERE, AND THE REASON IS A MEASUREMENT.
#
# F3 § 5 asks for `dropped_flip`, `wrong_dof_index` and `rotational_block`
# registered against this gate. At the size the F2 constant declares --
# `RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1e-14` of `max|k_e|` -- TWO OF THE THREE
# DO NOT REDDEN IT on the real platform's members:
#
#     dropped_flip      worst response 3.6563e-16  = 0.366x the ceiling   NO
#     wrong_dof_index   worst response 9.4595e-15  = 9.459x the ceiling   yes
#     rotational_block  worst response 1.4644e-17  = 0.0146x the ceiling  NO
#
# That constant's own entry pre-registered this: "that counter's size will be
# bisected against THAT gate rather than assumed from this one." Bisected here,
# the detection edges are `2.735459e-14`, `1.057143e-15` and `6.837686e-13`, so
# the inherited size sits BELOW two of them.
#
# Registering them needs an injection size this gate can see, and declaring one
# is a decision rather than a repair: `CLAUDE.md` puts every numerical tolerance
# in `floatfea/tolerances.py`, and
# `tests/test_report_carried.py`'s sibling `test_every_declared_tolerance_appears_
# in_the_plan` then requires a row in `docs/milestones/F2.md` -- a CLOSED
# milestone's locked plan. The alternative is a derived not-a-tolerance factor in
# the manner of `WIDEN`. The step report puts both to Xabier; neither is taken
# here, and nothing is registered under a size that cannot see the defect.
#
# WHAT IS NOT IN DOUBT: the gate itself reddens under all three shapes at a size
# it can see, and `floatfea.model.platform.check_rigid_modes` refuses the build
# under all three plus a nearly-released seventh mode. Both measurements are in
# the step report.
# --------------------------------------------------------------------------
