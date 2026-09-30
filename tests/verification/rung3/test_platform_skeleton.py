"""V3.1a / G3.1a: the superstructure's mass properties, per body, never on the sum.

**WHAT THIS GATE IS FOR (DZ0), and the row it used to quote said something else.**
`docs/milestones/F3.md` § 5 previously read "G3.1a's per-body mass check is the gate
that proves the sizing". It does not and cannot: the model is CONSTRUCTED to carry the
deck's properties, so reproducing them proves nothing about the sizing. The row now
states the two things the gate does establish, and this module is organised around
them:

* **(1)** the assembled model reproduces FloatSim's rigid-body mass properties per
  body — the precondition for inertia-relief equilibrium with FloatSim's loads. That
  is `..._B_the_ANALYTIC_path_agrees_with_the_DECK`.
* **(2)** the element mass matrices, the geometry and the assembly agree with an
  INDEPENDENT analytic path. That is `..._A_the_ANALYTIC_path_agrees_with_the_ASSEMBLED_matrix`,
  and it is the half with content.

Per body, never on the sum — a global total that matches while individual bodies do
not is a failure, so there is deliberately no test that adds the five bodies up.

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


def body_extent(body: BodyModel) -> float:
    """`l_b`: the largest node distance from the deck's CoG (DZ1c).

    The normalising length for the CoG and inertia comparisons. Using it rather
    than 1.0 m is what R598 was about: a CoG offset divided by one metre reported
    11.6x worse agreement than the body's own scale gives.
    """
    coords = body.model.nodes.coords()
    return float(np.max(np.linalg.norm(coords - body.deck_cog, axis=1)))


def analytic_properties(body: BodyModel) -> tuple[float, np.ndarray, np.ndarray]:
    """Mass, CoG offset from the deck's CoG, and inertia about the CoG — BY HAND.

    **THE INDEPENDENT PATH (DZ1). It never touches the assembled mass matrix.** Its
    inputs are the node coordinates and connectivity, the line mass and section, and
    the remainder's mass, position and `J_r` read off the model's lumped-mass input.
    It does not recompute the remainder, because recomputing it is what made the old
    comparison circular: the builder set `remainder = deck - member - parallel` and
    the gate added the same two terms back, so the assertion was `deck == deck` and
    the platform's diagonal came out BIT-IDENTICAL (R596).

    WHICH ROTARY TERMS, CITED RATHER THAN ASSUMED. `floatfea/element/beam.py`'s
    `local_mass` carries, per unit length:

    * axial and transverse translation at `rho * A` (`:346`);
    * torsion at `rho * (I_y + I_z)` — the POLAR second moment, and its docstring
      says why it is not `rho * J`: "`J` is the St-Venant torsion CONSTANT, which is
      a stiffness property; the rotary inertia of the cross-section about the member
      axis is its polar second moment" (`:332-336`, `:351`);
    * bending rotary inertia at `rho * I` through `bending_mass`'s `rho_i`.

    So a member of length `L` about its own centre carries

        J = m (L^2/12) (1 - e e^T)  +  rho_eq L [ J_p e e^T + I (1 - e e^T) ]

    with `J_p = I_y + I_z`. The first term is the line mass; the second is the
    section's own rotary inertia. **If the element ever omits one of these the
    residual is a FINDING, not a reason to tune this reference.**
    """
    section = body.members[0].section
    line_mass = body.member_mass / body.total_member_length
    polar = section.I_y + section.I_z

    parts: list[tuple[float, np.ndarray, np.ndarray]] = []
    for member in body.members:
        start = np.asarray(body.model.nodes[member.node_a].xyz, dtype=np.float64)
        end = np.asarray(body.model.nodes[member.node_b].xyz, dtype=np.float64)
        length = member.length
        axis = (end - start) / length
        along = np.outer(axis, axis)
        across = np.eye(3) - along
        mass = line_mass * length
        own = mass * (length**2 / 12.0) * across + body.equivalent_density * length * (
            polar * along + section.I_y * across
        )
        parts.append((mass, (start + end) / 2.0, own))

    # the remainder, READ OFF the model's lumped-mass input and not recomputed
    parts.append((body.remainder_mass, body.remainder_point, body.remainder_inertia))

    total = sum(m for m, _, _ in parts)
    centroid = sum(m * c for m, c, _ in parts) / total
    inertia = np.zeros((3, 3), dtype=np.float64)
    for mass, centre, own in parts:
        d = centre - centroid
        inertia += own + mass * (float(d @ d) * np.eye(3) - np.outer(d, d))
    return total, centroid - body.deck_cog, inertia


def _report_residual(label: str, residual: float, scale: float) -> str:
    """DZ1d: below one ULP of the scale, say so rather than printing a number.

    R596's `3.375e-36` was published as an accuracy result. It was the signature of
    exact cancellation -- thirty orders below `numpy.spacing(6.25e9)` -- and a number
    that small is evidence that nothing was compared, not that the comparison was
    tight.
    """
    ulp = float(np.spacing(scale))
    if residual <= ulp:
        return f"{label}: <= 1 ULP of {scale:.4e}"
    return f"{label}: {residual / scale:.4e} relative"


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
def test_G3_1a_A_the_ANALYTIC_path_agrees_with_the_ASSEMBLED_matrix(
    superstructure, index: int, capsys
) -> None:
    """(A). The gate's real content: two independent routes to the same properties.

    `analytic_properties` computes mass, CoG and inertia from node coordinates, the
    line mass and the section, never touching the assembled matrix.
    `assembled_properties` projects the assembled matrix. **A disagreement is a
    defect in the element mass matrix, the geometry or the assembly** — which is what
    DZ0 says G3.1a is for, and what the version this replaces could not see:

    ```
    cell   ONE VARIABLE: `rho_ip_l = rho * (I_y + I_z) * ll` scaled by 2 in beam.py
    out    unmutated           (A) inertia residual 1.5225e-18
    out    torsional rotary x2 (A) inertia residual 1.2983e-04
    out    restored            (A) inertia residual 1.5225e-18
    ```

    Fourteen orders, against a tolerance of `1e-13`.
    """
    body = superstructure.bodies[index]
    analytic_m, analytic_c, analytic_j = analytic_properties(body)
    assembled_m, assembled_c, assembled_j = assembled_properties(body)
    extent = body_extent(body)
    mass_scale = body.deck_mass
    inertia_scale = body.deck_mass * extent**2

    with capsys.disabled():
        print(
            f"\n  {body.name:<9} (A) "
            + _report_residual("mass", abs(analytic_m - assembled_m), mass_scale)
            + "; "
            + _report_residual("CoG", float(np.max(np.abs(analytic_c - assembled_c))), extent)
            + "; "
            + _report_residual(
                "inertia", float(np.max(np.abs(analytic_j - assembled_j))), inertia_scale
            )
        )

    assert abs(analytic_m - assembled_m) <= MASS_PROPERTY_AGREEMENT * mass_scale
    assert float(np.max(np.abs(analytic_c - assembled_c))) <= MASS_PROPERTY_AGREEMENT * extent
    assert (
        float(np.max(np.abs(analytic_j - assembled_j))) <= MASS_PROPERTY_AGREEMENT * inertia_scale
    ), (
        f"{body.name}: the analytic inertia and the assembled one disagree by "
        f"{float(np.max(np.abs(analytic_j - assembled_j))):.6e} kg.m^2. One of the "
        "element mass matrix, the geometry or the assembly is wrong -- the reference "
        "is not tuned to match (DZ1b)."
    )


@pytest.mark.parametrize("index", range(BODIES))
def test_G3_1a_B_the_ANALYTIC_path_agrees_with_the_DECK(superstructure, index: int) -> None:
    """(B). The model carries FloatSim's rigid-body properties, per body.

    DZ0(1): this is the precondition for inertia-relief equilibrium with FloatSim's
    loads, and it is what the results depend on. It is largely closed by
    construction -- the remainder is placed to close it -- and it is asserted anyway,
    because the placement rule could be wrong and this is where that shows.
    """
    body = superstructure.bodies[index]
    analytic_m, analytic_c, analytic_j = analytic_properties(body)
    extent = body_extent(body)
    assert abs(analytic_m - body.deck_mass) <= MASS_PROPERTY_AGREEMENT * body.deck_mass
    assert float(np.max(np.abs(analytic_c))) <= MASS_PROPERTY_AGREEMENT * extent, (
        f"{body.name}: the model's CoG is {analytic_c} from the deck's "
        f"{body.deck_cog}, which is {float(np.max(np.abs(analytic_c))) / extent:.3e} "
        f"of the body's {extent:.3f} m extent."
    )
    scale = body.deck_mass * extent**2
    assert float(np.max(np.abs(analytic_j - body.deck_inertia))) <= MASS_PROPERTY_AGREEMENT * scale


# ---------------------------------------------------------------------------
# DZ2 / R597. The geometry, which the properties gate does not see.
# ---------------------------------------------------------------------------


def expected_pairs(superstructure, body: BodyModel) -> set[frozenset[tuple[float, ...]]]:
    """The undirected endpoint pairs this body must have, FROM THE DECK.

    **THE FIRST VERSION OF THIS READ THE MODEL'S OWN NODES FOR BOTH SIDES (R600).**
    Its docstring said "from the DECK's joints" and "independent of what the builder
    actually made"; it read `body.model.nodes[...]` for the centre and every tip, it
    never used its `superstructure` argument, and `BodyModel` carried no deck
    coordinate, so it could not have read one. The assertion was `X == X`. Measured
    against it, all at `48 passed`: every tip moved 3 m, the plan centre moved 3 m,
    every in-plane coordinate scaled by 1.02, the arm labels permuted onto each
    other's joints, and the whole frame rotated 30 degrees about z.

    **The label permutation is the one that matters most**, because
    `buoy_joint_nodes` is keyed off those labels: F4 would have applied each buoy's
    reaction at its neighbour's node, and nothing would have said so.

    What it reads now is `superstructure.deck_joint_points` and `deck_joint_owner`,
    both filled from the deck's joints, and `test_C56_the_DECK_POINTS_really_come_from_the_DECK`
    asserts that what they carry equals an independent read of the deck file (C62, R608:
    this said construction CANNOT reach them, which is an absolute the tree does not
    support -- rebuilding them from the built nodes leaves the module green whenever no
    value also moves). The OWNERSHIP comes from the deck too, and not from
    `buoy_joint_nodes`, because that map is keyed off the member labels -- which is
    exactly what a permutation corrupts, so reading it would put the label back on
    both sides of the comparison.
    The platform's centre is the only point not taken from there, because it is not a
    joint: it is the plan centre `(0, 0, joint_plane_z)`.
    """
    extent = body_extent(body)
    grid = MASS_PROPERTY_AGREEMENT * extent
    deck = superstructure.deck_joint_points

    def cell(point) -> tuple[float, ...]:
        return tuple(round(float(c) / grid) * grid for c in point)

    if body.name == "platform":
        centre = (0.0, 0.0, superstructure.joint_plane_z)
        tips = [deck[name] for name in sorted(deck) if name.startswith("hub")]
    else:
        centre = deck[body.name]
        owner = superstructure.deck_joint_owner
        tips = [deck[name] for name in sorted(deck) if owner[name] == body.name]
    return {frozenset({cell(centre), cell(tip)}) for tip in tips}


def test_C56_the_DECK_POINTS_really_come_from_the_DECK(superstructure) -> None:
    """**PROVENANCE, which is the shape this step has produced three times.**

    R590, R596 and R600 were all one defect wearing three faces: the expected side of
    a comparison built out of the thing under test. Each was found by a reviewer, not
    by a test, and the reviewer measured that the shape is still REACHABLE: with
    `deck_joint_points` overwritten from the built nodes, the whole module passed.

    NO COUNT HERE (C58, R604). This docstring published `52 passed` in the very commit
    that made the baseline `53` by adding this test, so the figure was falsified by the
    change that shipped it -- BP0 in a docstring, and nothing regenerates a docstring.
    The counts live in the step report, which is regenerated by rule.

    So this reads the deck again and compares. **IT READS THE FILE, NOT THE BUILDER'S
    READER (C59, R605).** The first version called `_full_scale_deck`, which is the same
    function the builder called, because that is what the closing condition asked for --
    and the reviewer measured the hole: give that function a module-level cache and shift
    every joint point 3 m inside the cached object, and the whole frame is 3 m wrong with
    the module green, C56 included. A provenance check that re-reads through the builder's
    own function is circular the moment that function returns a shared object. Nothing
    memoises it today, so that was reach and not a defect; the assertion should not depend
    on it staying that way.

    The path here is: the YAML bytes, `yaml.safe_load`, the body's own reference point plus
    the joint's body-fixed attachment, scaled by the length basis. It shares the constant
    `DECK_YAML` with the builder and nothing else.

    It is a rung-3 assertion about the model, not a guard about a report, so DR1's
    apparatus freeze does not reach it.
    """
    import yaml

    from floatfea.io.froude import to_full_scale
    from floatfea.model.platform import DECK_YAML

    lam = superstructure.froude_lambda
    # THE LENGTH BASIS IS lambda^1, `docs/conventions.md`, and the scale below is
    # written out rather than delegated so this path does not route through
    # `floatfea.model.platform` at all. One assertion holds the two together, so a
    # change to the basis cannot leave this test quietly scaling by the wrong power.
    assert float(to_full_scale(1.0, "length", lam)) == lam

    raw = yaml.safe_load(DECK_YAML.read_bytes().decode("utf-8"))
    reference = {body["name"]: [float(c) for c in body["reference_point"]] for body in raw["bodies"]}
    fresh = {
        joint["body_a"]: (
            [
                (r + float(a)) * lam
                for r, a in zip(reference[joint["body_a"]], joint["attach_a_body"], strict=True)
            ],
            joint["body_b"],
        )
        for joint in raw["joints"]
    }

    carried = superstructure.deck_joint_points
    owners = superstructure.deck_joint_owner
    assert len(carried) == len(fresh) == 16

    for name, (point, owner) in fresh.items():
        assert name in carried, f"{name} is not in the carried deck points"
        offset = float(np.max(np.abs(np.asarray(carried[name]) - np.asarray(point))))
        assert offset == 0.0, (
            f"{name}'s carried point is {carried[name]} and an independent read of "
            f"{DECK_YAML.name} gives {point} -- {offset:.4e} m apart. The points a gate "
            "compares against are not the deck's."
        )
        assert owners[name] == owner, (
            f"{name} is recorded as attaching to {owners[name]!r} and the deck says "
            f"{owner!r}."
        )


@pytest.mark.parametrize("index", range(BODIES))
def test_DZ2_the_bodys_MEMBER_GEOMETRY_is_what_the_deck_implies(superstructure, index: int) -> None:
    """R597. Member count, the endpoint-pair set, no duplicates, and a tree.

    **The properties gate does not see any of this.** Measured before DZ2 existed:
    four member tips moved +3 m gave `1765 passed` across `tests/unit` and
    `tests/verification`, and four of sixteen members duplicated onto another line
    gave `1765 passed` too. A dropped member was caught by the count alone -- a
    detection the pre-DY1 CoG test had and the rewrite lost.
    """
    body = superstructure.bodies[index]
    expected_count = 4 if body.name == "platform" else 3
    assert len(body.members) == expected_count

    extent = body_extent(body)
    grid = MASS_PROPERTY_AGREEMENT * extent

    def cell(index_: int) -> tuple[float, ...]:
        point = np.asarray(body.model.nodes[index_].xyz, dtype=np.float64)
        return tuple(round(float(c) / grid) * grid for c in point)

    pairs = [frozenset({cell(m.node_a), cell(m.node_b)}) for m in body.members]

    assert len(set(pairs)) == len(pairs), (
        f"{body.name} has duplicate members: {len(pairs)} members occupy "
        f"{len(set(pairs))} distinct endpoint pairs, so at least one line is drawn "
        "twice and its mass is counted twice."
    )
    assert set(pairs) == expected_pairs(superstructure, body), (
        f"{body.name}'s members do not join the points the deck's joints imply. "
        "A moved tip lands here."
    )

    # a tree: every member touches the centre, and the tips are all distinct
    centre = cell(body.centre_node)
    assert all(centre in pair for pair in pairs), (
        f"{body.name} has a member not touching its centre node, so the body is not "
        "the star the frame requires."
    )
    tips = {next(iter(pair - {centre})) for pair in pairs}
    assert (
        len(tips) == expected_count
    ), f"{body.name} has {len(tips)} distinct tips for {expected_count} members."


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


@pytest.mark.parametrize("index", range(1, BODIES))
def test_DZ2_each_BUOY_lands_on_the_node_the_DECK_puts_it_at(superstructure, index: int) -> None:
    """R600's hardest case: the arm LABELS permuted onto each other's joints.

    A permutation leaves the endpoint-pair SET unchanged, so the pair check passes
    and should -- the frame really does join the same points. What it corrupts is
    WHICH BUOY each node belongs to, and `buoy_joint_nodes` is keyed off exactly
    those labels. **F4 applies each buoy's gimbal reaction through that map**, so a
    permutation would put buoy1's reaction at buoy2's node and every member force
    downstream would be wrong with nothing saying so.

    This is the assertion that ties the two together: the node `buoy_joint_nodes`
    gives for a buoy must sit at the coordinate the DECK gives for that buoy.
    """
    body = superstructure.bodies[index]
    extent = body_extent(body)
    for buoy, (owner, node_index) in superstructure.buoy_joint_nodes.items():
        if owner != body.name:
            continue
        built = np.asarray(body.model.nodes[node_index].xyz, dtype=np.float64)
        expected = np.asarray(superstructure.deck_joint_points[buoy], dtype=np.float64)
        offset = float(np.max(np.abs(built - expected)))
        assert offset <= MASS_PROPERTY_AGREEMENT * extent, (
            f"{buoy} is mapped to a node at {built} and the deck puts that buoy's "
            f"joint at {expected} -- {offset:.4f} m apart. F4 applies this buoy's "
            "reaction through that map, so the load would land on the wrong node."
        )
        assert superstructure.deck_joint_owner[buoy] == owner, (
            f"{buoy} is mapped to body {owner!r} and the deck attaches it to "
            f"{superstructure.deck_joint_owner[buoy]!r}."
        )


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
