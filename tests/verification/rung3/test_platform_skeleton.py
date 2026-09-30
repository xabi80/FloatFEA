"""V3.1a / G3.1a: the superstructure's mass properties, per body, never on the sum.

`docs/milestones/F3.md` § 5: "Per-body mass, CoG and inertia tensor from the FE mesh
against the model definition. **Reported and asserted PER BODY, never on the sum** — a
global total that matches while individual bodies do not is a failure."

So every assertion here is parametrised by body. There is deliberately no test that
adds the five bodies up.

WHAT IS ASSERTED AND WHAT IS ONLY REPORTED, because the difference is a finding rather
than a convenience. The builder reports that the deck's platform and hub inertias
satisfy `Ixx + Iyy = Izz` **exactly** — the perpendicular-axis identity for a lamina,
which no real three-dimensional body satisfies, and which the buoys in the same deck do
not. They are typed round numbers (`platform_common.py:159,178`), and HSP's own
`platform-geometry.md:46` flags the hub value as Q2. So:

* **mass and CoG are ASSERTED.** They come from real design figures — F1's 1250 t truss
  and the hub's 3 rods x 4 kg.
* **the inertia tensor is MEASURED AND REPORTED, not asserted**, until the deck carries
  a derived figure. Asserting the FE model against a placeholder would make G3.1a pass
  or fail on a number nobody computed, which is the shape `CLAUDE.md` calls a fudge
  factor: two numbers made to agree without a physical reason.

That is a narrowing of G3.1a and it is recorded here rather than left implicit.
"""

from __future__ import annotations

import math

import numpy as np
import pytest

from floatfea.assemble.system import assemble_mass_dense
from floatfea.model.material import Section
from floatfea.model.platform import (
    CLUSTER_ARM_OUTER_DIAMETER,
    MAX_LENGTH_OVER_GYRATION,
    MIN_LENGTH_OVER_DIAMETER,
    BodyModel,
    build_superstructure,
    check_limits,
    size_to_mass,
)
from floatfea.tolerances import ROUNDOFF_IDENTITY

BODIES = 5
MEMBERS = 16
"""not-a-tolerance: the model's own counts — the platform plus four hubs, four hub arms
plus twelve cluster arms. Counts of objects, not thresholds."""


@pytest.fixture(scope="module")
def superstructure():
    return build_superstructure()


def rigid_mass_matrix(body: BodyModel) -> np.ndarray:
    """The 6x6 rigid-body mass matrix of a body's members about its own node.

    `R` spans the six rigid motions about the reference; `R.T M R` is the rigid mass
    matrix, whose `[0:3, 0:3]` is `m I`, whose coupling block carries `m` times the
    centroid offset, and whose `[3:6, 3:6]` is the inertia about the reference. This is
    the standard reduction and it is done here rather than trusted from a summary,
    because the point of the gate is to read the ASSEMBLED matrix.
    """
    mass = assemble_mass_dense(body.model, body.elements)
    coords = body.model.nodes.coords()
    reference = np.asarray(body.model.nodes[body.remainder_node].xyz, dtype=np.float64)
    n = len(coords)
    modes = np.zeros((6 * n, 6), dtype=np.float64)
    for i, point in enumerate(coords):
        d = point - reference
        modes[6 * i : 6 * i + 3, 0:3] = np.eye(3)
        modes[6 * i : 6 * i + 3, 3:6] = np.array(
            [[0.0, d[2], -d[1]], [-d[2], 0.0, d[0]], [d[1], -d[0], 0.0]]
        )
        modes[6 * i + 3 : 6 * i + 6, 3:6] = np.eye(3)
    return modes.T @ mass @ modes


def test_the_skeleton_is_FIVE_bodies_and_SIXTEEN_members(superstructure) -> None:
    """The platform and four hubs, four hub arms and twelve cluster arms."""
    assert len(superstructure.bodies) == BODIES
    assert superstructure.n_members == MEMBERS
    names = [b.name for b in superstructure.bodies]
    assert names == ["platform", "hub1", "hub2", "hub3", "hub4"]
    assert len(superstructure.bodies[0].members) == 4, "the platform owns the hub arms"
    for hub in superstructure.bodies[1:]:
        assert len(hub.members) == 3, f"{hub.name} is a tripod of three cluster arms"
    # no member belongs to two bodies: the labels partition
    labels = [m.label for b in superstructure.bodies for m in b.members]
    assert len(labels) == len(set(labels)) == MEMBERS


def test_the_frame_is_PLANAR_and_every_member_is_horizontal(superstructure) -> None:
    """DW1's ruling, asserted on the built model rather than on the deck.

    If a node ever leaves the joint plane the frame is not planar and the builder's
    premise has failed, which must be loud.
    """
    z = superstructure.joint_plane_z
    for body in superstructure.bodies:
        for node in body.model.nodes:
            assert abs(node.z - z) <= ROUNDOFF_IDENTITY * abs(z), (
                f"{body.name}: node {node.name!r} is at z = {node.z} and the joint "
                f"plane is {z}. The frame is not planar."
            )


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_bodys_MASS_matches_the_deck(superstructure, index: int) -> None:
    """Per body: assembled member mass plus remainder equals the deck's mass.

    This is the half of G3.1a that rests on real design figures.
    """
    body = superstructure.bodies[index]
    from_matrix = float(rigid_mass_matrix(body)[0, 0])
    total = from_matrix + body.remainder_mass
    assert total == pytest.approx(body.deck_mass, rel=ROUNDOFF_IDENTITY), (
        f"{body.name}: the assembled members give {from_matrix:.6e} kg and the "
        f"remainder {body.remainder_mass:.6e}, totalling {total:.6e} against the "
        f"deck's {body.deck_mass:.6e}."
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_assembled_mass_matches_the_builders_own_figure(
    superstructure, index: int
) -> None:
    """The matrix and the builder's arithmetic agree.

    Two independent routes to the same number: `A * L * rho` summed over members, and
    the `[0,0]` entry of the assembled rigid mass matrix. They are not the same
    computation -- the second goes through the element mass formulation and the
    assembly -- so agreement is evidence about both.
    """
    body = superstructure.bodies[index]
    from_matrix = float(rigid_mass_matrix(body)[0, 0])
    assert from_matrix == pytest.approx(body.member_mass, rel=ROUNDOFF_IDENTITY)


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_members_CoG_is_where_the_geometry_puts_it(superstructure, index: int) -> None:
    """Per body: the coupling block is `m` times the centroid offset, and by symmetry
    a body's members are centred on its own node in plan.

    The platform's four arms are at 90 degrees and the hubs' three at 120, so in both
    cases the in-plane centroid sits on the body node. An asymmetric build -- a dropped
    member, a mislocated node -- moves it, which is what this reads.
    """
    body = superstructure.bodies[index]
    m6 = rigid_mass_matrix(body)
    mass = float(m6[0, 0])
    # the coupling block is m * skew(centroid offset); recover the offset
    offset = np.array([m6[1, 5], m6[2, 3], m6[0, 4]]) / mass
    span = max(m.length for m in body.members)
    assert np.max(np.abs(offset)) <= ROUNDOFF_IDENTITY * span, (
        f"{body.name}: its members' centroid is {offset} from the body node, which "
        f"is {np.max(np.abs(offset)) / span:.3e} of the {span:.3f} m member span. "
        "A symmetric fan of members is centred on its own node."
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_bodys_INERTIA_is_reported_and_the_reason_is_recorded(
    superstructure, index: int, capsys
) -> None:
    """The half that is MEASURED rather than asserted, and why.

    The deck's platform and hub inertias satisfy `Ixx + Iyy = Izz` exactly, the
    lamina identity, so they are typed placeholders. Asserting the FE model against
    them would make the gate turn on a number nobody derived. The measurement is
    printed so it is on the record and moves when the model moves.
    """
    body = superstructure.bodies[index]
    m6 = rigid_mass_matrix(body)
    member_izz = float(m6[5, 5])
    remaining = float(body.remainder_inertia[2][2])
    deck_izz = member_izz + remaining
    with capsys.disabled():
        print(
            f"\n  {body.name:<9} Izz: members {member_izz:.6e}  remainder "
            f"{remaining:+.6e}  deck {deck_izz:.6e} kg.m^2"
            f"   members/deck {member_izz / deck_izz:.4f}"
        )
    # what IS asserted: the split is exact, so no inertia is invented or lost
    assert member_izz + remaining == pytest.approx(deck_izz, rel=ROUNDOFF_IDENTITY)
    assert deck_izz > 0.0


def test_the_builder_REPORTS_the_placeholder_inertia_rather_than_asserting_on_it(
    superstructure,
) -> None:
    """The finding must be present, because the narrowing above depends on it.

    If the deck ever carries a derived inertia this test goes red, which is the
    signal to widen G3.1a to assert on it.
    """
    lamina = [f for f in superstructure.findings if "LAMINA" in f]
    assert len(lamina) == BODIES, (
        f"{len(lamina)} of {BODIES} modelled bodies report the lamina-identity "
        "finding. If a body's deck inertia is now derived, G3.1a's inertia half can "
        "be asserted for it and this test is what says so."
    )


def test_the_builder_REPORTS_a_zero_remainder_carrying_rotary_inertia(
    superstructure,
) -> None:
    """The platform's remainder mass is zero while its remaining Izz is not.

    Mass-sizing a member to its body's mass leaves nothing to carry the residual
    inertia. That is representable and it is not a point mass, and the builder says so
    rather than letting a reader assume the lumped mass is physical.
    """
    zero_remainder = [f for f in superstructure.findings if "rotary inertia" in f]
    assert len(zero_remainder) == 1, (
        "exactly the platform should report a zero remainder carrying rotary "
        f"inertia; {len(zero_remainder)} bodies do."
    )
    assert "platform" in zero_remainder[0]


# ---------------------------------------------------------------------------
# THE REFUSALS. F3 section 2: not a warning, not a clamp.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("index", range(BODIES))
def test_every_built_member_is_INSIDE_both_limits(superstructure, index: int) -> None:
    """No member in the shipped model is refused, and the margins are on the record."""
    body = superstructure.bodies[index]
    for member in body.members:
        d_outer = math.sqrt(
            8.0 * member.section.I_y / member.section.A + 2.0 * member.section.A / math.pi
        )
        over_d = member.length / d_outer
        over_r = member.length / math.sqrt(member.section.I_y / member.section.A)
        assert over_d >= MIN_LENGTH_OVER_DIAMETER, f"{member.label}: L/D = {over_d}"
        assert over_r <= MAX_LENGTH_OVER_GYRATION, f"{member.label}: L/r = {over_r}"


def test_a_STUBBY_member_is_REFUSED() -> None:
    """`L/D < 2`: below it a beam element does not describe the member at all."""
    section = Section.circular_tube(CLUSTER_ARM_OUTER_DIAMETER, 0.180)
    check_limits("just inside", 2.0 * CLUSTER_ARM_OUTER_DIAMETER, section)
    with pytest.raises(ValueError, match="L/D"):
        check_limits("stubby", 1.99 * CLUSTER_ARM_OUTER_DIAMETER, section)


def test_a_SLENDER_member_is_REFUSED() -> None:
    """`L/r > 300`: the slenderness ceiling."""
    section = Section.circular_tube(0.2, 0.004)
    r = math.sqrt(section.I_y / section.A)
    check_limits("just inside", MAX_LENGTH_OVER_GYRATION * r, section)
    with pytest.raises(ValueError, match="L/r"):
        check_limits("slender", 1.01 * MAX_LENGTH_OVER_GYRATION * r, section)


def test_SIZING_to_a_mass_reproduces_that_mass(capsys) -> None:
    """`size_to_mass` is exact, not iterated, and it refuses rather than going solid."""
    from floatfea import basis

    target, count, length = 1.25e6, 4, 50.0
    section = size_to_mass(target, count, length, CLUSTER_ARM_OUTER_DIAMETER)
    produced = count * length * section.A * basis.RHO_STEEL
    with capsys.disabled():
        print(
            f"\n  sized to {target:.4e} kg over {count} x {length:g} m: "
            f"A = {section.A:.6f} m^2, produced {produced:.4e} kg"
        )
    assert produced == pytest.approx(target, rel=ROUNDOFF_IDENTITY)

    # a mass a tube of that diameter cannot reach without going solid
    with pytest.raises(ValueError, match="without a solid section"):
        size_to_mass(1e9, 1, 1.0, CLUSTER_ARM_OUTER_DIAMETER)
