"""V3.1a / G3.1a: the superstructure's mass properties, per body, never on the sum.

`docs/milestones/F3.md` § 5: "Per-body mass, CoG and inertia tensor from the FE mesh
against the model definition. **Reported and asserted PER BODY, never on the sum** — a
global total that matches while individual bodies do not is a failure."

WHY THIS FILE WAS REWRITTEN, AND IT IS THE MOST IMPORTANT THING IN IT (R590). The
first version's mass assertion was `x == approx(x)`. The builder defined
`remainder = deck_mass - member_mass`, and the test asserted
`member_mass + remainder == deck_mass`. Measured: a wall of `0.001 m` instead of
`0.180 m` — a section wrong by 180× — passed all 32 tests, and so did `0.400 m`, at
which three arms outweigh their hub.

So this file now obeys DY1:

* **every deck value is read from `platform12_deck.yaml`**, through the builder's
  `deck_mass`, `deck_cog` and `deck_inertia` fields, which are the YAML's own numbers
  Froude-scaled and nothing else. Never a builder intermediate.
* **`T_G` comes from nodal coordinates only** and is formed against the ASSEMBLED
  global mass matrix, so what is read is the matrix rather than the arithmetic that
  produced it.
* **the member-only mass is asserted to be `f · M_b` from the element matrices**,
  independently of the builder's split, and **the section properties are asserted
  against F1's recorded values** — which is what makes a wrong wall red.
* **no test computes the remainder as a complement.**
"""

from __future__ import annotations

import math

import numpy as np
import pytest

from floatfea import basis
from floatfea.assemble.system import assemble_mass_dense
from floatfea.model.material import Section
from floatfea.model.platform import (
    ARM_OUTER_DIAMETER,
    ARM_WALL,
    MASS_FRACTION_LADDER,
    MAX_LENGTH_OVER_GYRATION,
    MIN_LENGTH_OVER_DIAMETER,
    BodyModel,
    body_mass_matrix,
    build_superstructure,
    check_limits,
    inertia_about,
    rigid_properties,
)
from floatfea.tolerances import MASS_PROPERTY_AGREEMENT

BODIES = 5
MEMBERS = 16
"""not-a-tolerance: the model's own counts — the platform plus four hubs, four hub
arms plus twelve cluster arms. Counts of objects, not thresholds."""

F1_RECORDED_OUTER_DIAMETER = 2.5
F1_RECORDED_WALL = 0.180
"""`docs/milestones/F1.md:389` — the recorded arm section's GEOMETRY, `2.5 m x 180 mm`.

**THE GEOMETRY IS ASSERTED, NOT THE DERIVED PROPERTIES**, and the first version of
this file had it the other way round. DY0a quotes `A 1.311929 m^2`, `I 0.887979 m^4`,
`J 1.775958 m^4`, which are those two numbers put through the exact formulae and
rounded to seven figures. Asserting the computed `A = 1.3119290921390976` against the
seven-figure transcription needs a tolerance of about `1e-7` — a transcription
tolerance, which would then sit in `tolerances.py` bounding nothing physical and
loose enough to hide a real section change.

The diameter and the wall ARE exact decimals, so they are compared exactly, and the
derived properties follow from them through `basis`, which G3.3 already gates. The
transcribed figures are printed for the record rather than asserted.

not-a-tolerance: a recorded geometry, compared exactly."""


@pytest.fixture(scope="module")
def superstructure():
    return build_superstructure()


def deck_properties(body: BodyModel) -> tuple[float, np.ndarray, np.ndarray]:
    """The deck's own mass, CoG and inertia for a body, as the YAML gives them."""
    return body.deck_mass, body.deck_cog, body.deck_inertia


def assembled_properties(body: BodyModel) -> tuple[float, np.ndarray, np.ndarray]:
    """Mass, CoG offset from the deck's CoG, and inertia about the CoG.

    From `body_mass_matrix` — members plus the lumped remainder — projected with
    `T_G` built from nodal coordinates only.
    """
    return rigid_properties(body_mass_matrix(body), body.model.nodes.coords(), body.deck_cog)


def test_the_skeleton_is_FIVE_bodies_and_SIXTEEN_members(superstructure) -> None:
    """The platform and four hubs, four hub arms and twelve cluster arms."""
    assert len(superstructure.bodies) == BODIES
    assert superstructure.n_members == MEMBERS
    assert [b.name for b in superstructure.bodies] == [
        "platform",
        "hub1",
        "hub2",
        "hub3",
        "hub4",
    ]
    assert len(superstructure.bodies[0].members) == 4, "the platform owns the hub arms"
    for hub in superstructure.bodies[1:]:
        assert len(hub.members) == 3, f"{hub.name} is a tripod of three cluster arms"
    labels = [m.label for b in superstructure.bodies for m in b.members]
    assert len(labels) == len(set(labels)) == MEMBERS


def test_every_MEMBER_node_is_in_the_joint_plane(superstructure) -> None:
    """DW1's ruling: the members are planar.

    The REMAINDER node is deliberately not: the platform's sits 20.66 m above the
    plane, because that is where the deck's CoG requires it. So this asserts on the
    member ends rather than on every node, and the distinction is the point — a
    planar frame with an off-plane lumped mass is what DY0 builds.
    """
    z = superstructure.joint_plane_z
    for body in superstructure.bodies:
        for member in body.members:
            for index in (member.node_a, member.node_b):
                node = body.model.nodes[index]
                assert abs(node.z - z) <= MASS_PROPERTY_AGREEMENT * abs(z), (
                    f"{body.name}: member node {node.name!r} is at z = {node.z} and "
                    f"the joint plane is {z}."
                )


# ---------------------------------------------------------------------------
# G3.1a. Three properties, per body, against the deck.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_bodys_MASS_matches_the_deck(superstructure, index: int) -> None:
    """Per body, from the assembled matrix against the YAML's mass."""
    body = superstructure.bodies[index]
    mass, _, _ = assembled_properties(body)
    deck_mass, _, _ = deck_properties(body)
    assert mass == pytest.approx(deck_mass, rel=MASS_PROPERTY_AGREEMENT), (
        f"{body.name}: the assembled matrix gives {mass:.6e} kg against the deck's "
        f"{deck_mass:.6e}."
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_bodys_CoG_matches_the_deck(superstructure, index: int) -> None:
    """Per body: the model's centre of gravity is where the deck says it is.

    THIS IS THE ASSERTION R591 SHOWED WAS MISSING. The old version compared the
    members' centroid to the body's own node, which is a different quantity: it
    caught a dropped member and said nothing about the platform's CoG sitting
    10.3315 m below the point the deck declares. FloatSim's `driver.py:203-209`
    states that the deck's `reference_point` IS the CoG, so that point is the
    referent and this is what compares against it.
    """
    body = superstructure.bodies[index]
    _, offset, _ = assembled_properties(body)
    scale = max(float(np.max(np.abs(body.deck_cog))), body.link_length, 1.0)
    assert float(np.max(np.abs(offset))) <= MASS_PROPERTY_AGREEMENT * scale, (
        f"{body.name}: the model's CoG is {offset} from the deck's "
        f"{body.deck_cog}, which is {float(np.max(np.abs(offset))) / scale:.3e} of "
        f"the {scale:.3f} m scale it is compared against."
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_bodys_full_INERTIA_TENSOR_matches_the_deck(
    superstructure, index: int, capsys
) -> None:
    """Per body: all six independent components, not just `Izz`.

    R592 was that only `Izz` was decremented, so the members' contribution to `Ixx`
    and `Iyy` — 20.9% of the platform's and 51.5% of each hub's — was double-counted,
    and the figure printed as the deck's was `6.250897e9` against a real
    `6.250000e9`. DY2 requires the full tensor, with `J_mem` taken about `G` from the
    assembled matrix.
    """
    body = superstructure.bodies[index]
    _, _, inertia = assembled_properties(body)
    scale = float(np.max(np.abs(body.deck_inertia)))
    worst = float(np.max(np.abs(inertia - body.deck_inertia)))
    with capsys.disabled():
        print(
            f"\n  {body.name:<9} inertia residual {worst:.4e} of {scale:.6e} "
            f"= {worst / scale:.3e} relative"
        )
    assert worst <= MASS_PROPERTY_AGREEMENT * scale, (
        f"{body.name}: the assembled inertia differs from the deck's by "
        f"{worst:.6e} kg.m^2, {worst / scale:.3e} relative.\n"
        f"assembled:\n{inertia}\ndeck:\n{body.deck_inertia}"
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_the_MEMBER_ONLY_mass_is_the_declared_FRACTION(superstructure, index: int) -> None:
    """DY1c. From the element matrices, independently of the builder's split.

    `f · M_b`, where `f` is the body's chosen fraction and `M_b` the deck's mass.
    Neither side is a complement of the other: the left is assembled from element
    matrices, the right is a product of two numbers read from the YAML and the
    ladder.
    """
    body = superstructure.bodies[index]
    member_only = assemble_mass_dense(body.model, body.elements)
    mass = float(rigid_properties(member_only, body.model.nodes.coords(), body.deck_cog)[0])
    expected = body.mass_fraction * body.deck_mass
    assert mass == pytest.approx(expected, rel=MASS_PROPERTY_AGREEMENT), (
        f"{body.name}: the element matrices give {mass:.6e} kg of member mass and "
        f"f = {body.mass_fraction:g} of the deck's {body.deck_mass:.6e} is "
        f"{expected:.6e}."
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_the_chosen_FRACTION_is_asserted_not_inferred(superstructure, index: int) -> None:
    """DY0d. The `f` this body was built at, and the ladder it came from."""
    body = superstructure.bodies[index]
    assert body.mass_fraction in MASS_FRACTION_LADDER
    # not-a-tolerance: DY0c's default MODEL PARAMETER, compared exactly. `f` is an
    # input to the build and not a measured quantity, so there is nothing here to be
    # close about -- the assertion exists so that descending the ladder for a body
    # shows up as a red with a reason rather than as a silent change of model.
    assert body.mass_fraction == 0.5, (  # not-a-tolerance: an input, see above
        f"{body.name} was built at f = {body.mass_fraction:g}, not the default 0.5. "
        "That is admissible and it is a SIZING FINDING, so this assertion is what "
        "makes the change visible rather than silent — update it with the reason."
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_the_section_is_F1s_RECORDED_section(superstructure, index: int, capsys) -> None:
    """DY1b. Every member carries `docs/milestones/F1.md:389`'s section.

    **This is what makes a wrong wall red**, and it is the assertion the first
    version of this file lacked: with the mass split by fraction, an equivalent
    density absorbs any area change and the mass gate cannot see it at all — a wall
    of `0.001 m` instead of `0.180 m` passed every test. The section is the
    stiffness, and the stiffness is what F1 recorded.

    The GEOMETRY is compared exactly; see the constants above for why the derived
    properties are printed instead.
    """
    body = superstructure.bodies[index]
    # not-a-tolerance: F1:389's RECORDED GEOMETRY, compared exactly. `2.5` and `0.180`
    # are exact decimals a designer wrote down, not measurements, so the comparison is
    # equality and a tolerance on it would only let a real section change through.
    assert (
        ARM_OUTER_DIAMETER == F1_RECORDED_OUTER_DIAMETER
    ), (  # not-a-tolerance: a recorded geometry, see above
        f"the builder uses D_o = {ARM_OUTER_DIAMETER}; F1:389 records "
        f"{F1_RECORDED_OUTER_DIAMETER} m"
    )
    # not-a-tolerance: the same, for the wall. This is the line a 180x wall error
    # reddens, and the whole reason DY1b exists.
    assert (
        ARM_WALL == F1_RECORDED_WALL
    ), (  # not-a-tolerance: a recorded geometry
        f"the builder uses t = {ARM_WALL}; F1:389 records {F1_RECORDED_WALL} m"
    )
    expected = Section.circular_tube(F1_RECORDED_OUTER_DIAMETER, F1_RECORDED_WALL)
    for member in body.members:
        assert member.section == expected, (
            f"{member.label} does not carry F1:389's section: it has A = "
            f"{member.section.A:.9f}, I = {member.section.I_y:.9f}, and the recorded "
            f"geometry gives A = {expected.A:.9f}, I = {expected.I_y:.9f}."
        )
    if index == 0:
        with capsys.disabled():
            print(
                "\n  F1:389's 2.5 m x 180 mm gives "
                f"A = {expected.A:.6f} m^2, I = {expected.I_y:.6f} m^4, "
                f"J = {expected.J:.6f} m^4"
                "\n  DY0a transcribes  A = 1.311929, I = 0.887979, J = 1.775958"
            )


def test_the_EQUIVALENT_DENSITIES_are_reported(superstructure, capsys) -> None:
    """DY0e. Every body's `rho_eq`, and a finding above steel.

    The members are stiffness equivalents of a truss with depth, so a density below
    steel is expected — the truss's mass is spread over a larger envelope than the
    equivalent tube. Above steel would mean the body's mass does not fit inside F1's
    section at the chosen fraction.
    """
    with capsys.disabled():
        print()
        for body in superstructure.bodies:
            over = " OVER STEEL" if body.equivalent_density > basis.RHO_STEEL else ""
            print(
                f"  {body.name:<9} f {body.mass_fraction:.1f}  rho_eq "
                f"{body.equivalent_density:8.1f} kg/m^3  "
                f"(steel {basis.RHO_STEEL:g}){over}"
            )
    reported = [f for f in superstructure.findings if "ABOVE steel" in f]
    over_steel = [b.name for b in superstructure.bodies if b.equivalent_density > basis.RHO_STEEL]
    assert len(reported) == len(over_steel), (
        f"{len(over_steel)} bodies are above steel density and {len(reported)} say so. "
        "DY0e requires each one reported."
    )


def test_the_REMAINDER_is_placed_to_match_the_first_MOMENT(superstructure) -> None:
    """The remainder point satisfies `M_b r_G = Σ member first moments + m_r r_r`.

    Checked directly rather than through the CoG gate, so the placement rule itself
    is asserted and not only its consequence.
    """
    for body in superstructure.bodies:
        line_mass = body.member_mass / body.total_member_length
        first_moment = np.zeros(3)
        for member in body.members:
            mid = (
                np.asarray(body.model.nodes[member.node_a].xyz)
                + np.asarray(body.model.nodes[member.node_b].xyz)
            ) / 2.0
            first_moment += (member.length * line_mass) * mid
        combined = first_moment + body.remainder_mass * body.remainder_point
        target = body.deck_mass * body.deck_cog
        scale = max(float(np.max(np.abs(target))), 1.0)
        assert float(np.max(np.abs(combined - target))) <= MASS_PROPERTY_AGREEMENT * scale, (
            f"{body.name}: the combined first moment is {combined} against the deck's " f"{target}."
        )


def test_J_mem_is_taken_ABOUT_G_and_not_about_the_member_centroid(superstructure) -> None:
    """R592's second half, asserted so the reference point cannot drift back.

    The members' own centroid is in the joint plane; `G` is not, for the platform.
    Subtracting an inertia about one from a tensor about the other mixes reference
    points, and it cost a 1.07% error in the platform's inertia before DY2. The two
    differ by the parallel-axis shift, and that difference is what this measures.
    """
    body = superstructure.bodies[0]  # the platform: G is off the member plane
    member_only = assemble_mass_dense(body.model, body.elements)
    coords = body.model.nodes.coords()
    about_g = inertia_about(member_only, coords, body.deck_cog)
    mass, centroid, about_centroid = rigid_properties(member_only, coords, body.deck_cog)
    shift = mass * (float(centroid @ centroid) * np.eye(3) - np.outer(centroid, centroid))
    assert np.allclose(about_g - shift, about_centroid, rtol=MASS_PROPERTY_AGREEMENT), (
        "the two forms do not differ by the parallel-axis shift, so one of them is "
        "not what its name says."
    )
    assert float(np.max(np.abs(shift))) > 0.0, (
        "the shift is zero, so this body's G is on its member centroid and the test "
        "is measuring nothing. Pick a body whose CoG is off the member plane."
    )


# ---------------------------------------------------------------------------
# THE REFUSALS. F3 section 2: not a warning, not a clamp.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("index", range(BODIES))
def test_every_built_member_is_INSIDE_both_limits(superstructure, index: int) -> None:
    """No member in the shipped model is refused, on MEMBER length."""
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
    section = Section.circular_tube(ARM_OUTER_DIAMETER, ARM_WALL)
    check_limits("just inside", 2.0 * ARM_OUTER_DIAMETER, section)
    with pytest.raises(ValueError, match="L/D"):
        check_limits("stubby", 1.99 * ARM_OUTER_DIAMETER, section)


def test_a_SLENDER_member_is_REFUSED() -> None:
    """`L/r > 300`: the slenderness ceiling."""
    section = Section.circular_tube(0.2, 0.004)
    r = math.sqrt(section.I_y / section.A)
    check_limits("just inside", MAX_LENGTH_OVER_GYRATION * r, section)
    with pytest.raises(ValueError, match="L/r"):
        check_limits("slender", 1.01 * MAX_LENGTH_OVER_GYRATION * r, section)


def test_the_BUOY_NODE_MAP_names_its_body(superstructure) -> None:
    """DY4 / R595. Twelve buoys, each mapped to `(body, node)`.

    An index alone does not say which model it indexes, and the twelve buoys land on
    node indices 1, 2 and 3 across four separate hub models. F4 applies loads through
    this map, so the body has to be in it.
    """
    mapping = superstructure.buoy_joint_nodes
    assert len(mapping) == 12
    for buoy, entry in mapping.items():
        assert (
            isinstance(entry, tuple) and len(entry) == 2
        ), f"{buoy} maps to {entry!r}; DY4 requires (body, node)."
        name, node = entry
        body = next(b for b in superstructure.bodies if b.name == name)
        assert 0 <= node < len(body.model.nodes)
    # the collision the bare index invited: three distinct buoys on one index
    by_index: dict[int, list[str]] = {}
    for buoy, (_, node) in mapping.items():
        by_index.setdefault(node, []).append(buoy)
    assert any(len(v) > 1 for v in by_index.values()), (
        "no node index is shared between buoys, so this map would have been "
        "unambiguous without the body and the test is not measuring DY4's reason."
    )
