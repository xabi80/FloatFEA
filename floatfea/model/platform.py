"""DX3: the platform superstructure, built from the exported deck.

WHAT THIS BUILDS, and it is five structural models rather than one.
`docs/milestones/F3.md` § 3.4: each FloatSim body is its own free-free structural
model, balanced by its own inertia relief. So this returns one `BodyModel` per
modelled body — the platform and the four hubs — and the members are PARTITIONED
between them:

    platform   4 hub arms, centre -> hub, 50 m               + its remainder mass
    hub1..4    3 cluster arms each, hub -> buoy joint, 25 m   + its remainder mass

16 members, no member in two bodies, and nothing joining adjacent hubs or adjacent
buoy joints. That last is a **design observation about the platform** and not a
modelling choice: the frame is a tree, each body is statically determinate, and the
absence of cross-bracing belongs in the member-force table's commentary.

THE BUOYS ARE LOADS, NOT MASS, AND GETTING THIS WRONG WOULD DOUBLE-COUNT (DX0).
Each buoy is its own FloatSim body joined to its hub by a gimbal, so everything the
buoy experiences — weight, buoyancy, wave force, its own inertia — reaches the
cluster-arm tip as the force and locked-axis moment that joint transmits. The
reaction ALREADY CONTAINS the buoy's inertia. No buoy mass enters this model; the
twelve buoy-joint nodes exist so the reactions have somewhere to be applied.

THE FRAME IS PLANAR AND THAT WAS MEASURED, NOT ASSUMED (DW1). All 16 joint points
are coplanar to machine zero, so every node here is at the joint plane and every
member is horizontal. `tests/verification/rung3/test_platform_deck_export.py`
asserts the coplanarity, so if it ever stops being true this module's premise fails
loudly rather than silently producing a frame the deck does not have.

WHAT IT REFUSES. A member outside `L/D >= 2` or `L/r <= 300` (F3 § 2), on MEMBER
length. Not a warning and not a clamp.

THE MEMBERS ARE STIFFNESS EQUIVALENTS, NOT MASS MODELS (DY0). This is the ruling
that replaced "size the members to reproduce the body's mass", and the arithmetic is
why:

    claim  four 50 m platform arms at F1's section, in steel, outweigh their body
    out    4 x 50 m x 1.311929 m^2 x 7850 kg/m^3 = 2059.7 t
    out    the platform body's deck mass is 1250.0 t -- the members are 1.65x it
    judge  so a member carrying its own steel mass cannot be right, and sizing the
           SECTION to the mass cannot be right either: it made the members consume
           the entire body and left nothing at the CoG, which put the model's centre
           of gravity 10.3315 m below the one the deck declares (R591).

So each member takes F1's recorded section for its STIFFNESS, and the mass splits:

    members    f * M_b as a uniform line mass, through an equivalent density
               rho_eq = f * M_b / (L_b * A). Rotary inertia follows as rho_eq * I,
               which keeps the two consistent by construction.
    remainder  (1 - f) * M_b at the point that makes the combined first moment equal
               the deck's, on a rigid link to the body's centre node.

`f = 0.5` by default, descended per body if the remainder mass or its inertia tensor
comes out negative.

WHAT IT REPORTS RATHER THAN REFUSING. An equivalent density above steel, and an `f`
below the default. Both are sizing findings under F3 § 3.3 -- reported, not clamped,
because a body whose members cannot be made light enough is information about the
section rather than a number to force.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Final

import numpy as np
from numpy.typing import NDArray

from floatfea import basis
from floatfea.assemble.system import BeamElement, assemble_mass_dense
from floatfea.element.beam import local_stiffness
from floatfea.element.rigid import (
    element_lambda_min_over_epsilon,
    element_rigid_residual,
    seventh_over_epsilon,
)
from floatfea.io.froude import to_full_scale
from floatfea.model.material import S355, Material, Section
from floatfea.model.nodes import Model, Node
from floatfea.tolerances import (
    MASS_PROPERTY_AGREEMENT,
    RIGID_MODE_BOUND,
    RIGID_MODE_EXACTNESS,
)

DECK_YAML: Final[Path] = (
    Path(__file__).resolve().parents[2] / "data" / "platform" / "platform12_deck.yaml"
)

MIN_LENGTH_OVER_DIAMETER: Final[float] = 2.0
MAX_LENGTH_OVER_GYRATION: Final[float] = 300.0
"""F3 § 2's builder limits, verbatim, and neither is a tolerance.

not-a-tolerance: they are properties of the model the tool ACCEPTS, declared in the
plan and asserted here. Nothing is compared against them to decide whether a computed
number is close enough to another, which is why they are not in
`floatfea.tolerances`. `L/D >= 2` keeps a member in the range a beam element
describes at all; `L/r <= 300` is the slenderness ceiling.
"""

ARM_OUTER_DIAMETER: Final[float] = 2.5
ARM_WALL: Final[float] = 0.180
"""`docs/milestones/F1.md:389` — the one RECORDED section, used for BOTH member
types (DY0a). Its basis is at `F1.md:425-433`: the joint delivers 5.93 MN at the rod
tip, over 25 m that is M = 148.2 MN·m, demand W = 0.696 m³ against 0.710 supplied.
F1's own caveat travels with it: the order check makes the section "plausible rather
than comfortable".

not-a-tolerance: a designed geometry, cited to its source. Nothing is compared
against it.
"""

MASS_FRACTION_LADDER: Final[tuple[float, ...]] = (0.5, 0.4, 0.3, 0.2, 0.1, 0.0)
"""The fractions of a body's mass the members may carry, most first (DY0c, DY0d).

**0.5 is the default and its reason is physical:** a truss with its bottom chord in
the joint plane carries about half its mass there, and the in-plane members are the
STIFFNESS equivalent of that truss rather than a model of its steel.

The ladder is descended per body when `f` is inadmissible — a negative remainder, or
a remainder inertia tensor with a negative eigenvalue — and `f = 0` is always
admissible because it puts the whole body mass at the remainder and asks the members
to carry none.

not-a-tolerance: a set of candidate model parameters, and the chosen value is
asserted per body rather than compared against anything.
"""


@dataclass(frozen=True)
class Member:
    """One structural member, with where its section came from."""

    node_a: int
    node_b: int
    section: Section
    label: str
    length: float
    preliminary: bool
    section_basis: str


@dataclass(frozen=True)
class BodyModel:
    """One FloatSim body as a free-free structural model.

    `centre_node` is the body's own structural node; `remainder_node` is where the
    lumped remainder sits, joined to the centre by a rigid link. They coincide when
    the link is zero-length, which is the case for every hub (DW1: a hub's mass
    reference is already on the joint plane).
    """

    name: str
    model: Model
    members: tuple[Member, ...]
    material: Material
    mass_fraction: float
    equivalent_density: float
    remainder_mass: float
    remainder_inertia: NDArray[np.float64]
    remainder_point: NDArray[np.float64]
    centre_node: int
    remainder_node: int
    link_length: float
    deck_mass: float
    deck_cog: NDArray[np.float64]
    deck_inertia: NDArray[np.float64]
    member_mass: float
    findings: tuple[str, ...] = field(default_factory=tuple)

    @property
    def elements(self) -> list[BeamElement]:
        """The members as assembler input, with the body's EQUIVALENT density."""
        return [
            BeamElement(node_a=m.node_a, node_b=m.node_b, section=m.section, material=self.material)
            for m in self.members
        ]

    @property
    def total_member_length(self) -> float:
        return sum(m.length for m in self.members)

    @property
    def preliminary(self) -> tuple[str, ...]:
        """Members whose section was sized rather than recorded (DJ1's mark)."""
        return tuple(m.label for m in self.members if m.preliminary)


@dataclass(frozen=True)
class Superstructure:
    """The five modelled bodies, and what has to travel with any result from them."""

    bodies: tuple[BodyModel, ...]
    froude_lambda: float
    joint_plane_z: float
    buoy_joint_nodes: dict[str, tuple[str, int]]
    deck_joint_owner: dict[str, str]
    """Which body each joint attaches TO, from the deck (`body_a` -> `body_b`).

    Carried beside the points so a gate can work out which tips belong to which body
    WITHOUT reading the builder's member labels -- those labels are what a permutation
    corrupts, and `buoy_joint_nodes` is keyed off them, so using them to select the
    expected set would put the label on both sides of the comparison again.
    """

    deck_joint_points: dict[str, tuple[float, float, float]]
    """Every joint's point at FULL SCALE, keyed by the joint's own body_a.

    **Carried so a gate can check the built geometry against something that is not
    the built geometry (R600).** The first DZ2 gate read the model's own nodes for
    both sides of its comparison and asserted `X == X`: its docstring said "from the
    DECK's joints", its `superstructure` argument was unused, and `BodyModel` carried
    no deck coordinate at all, so it could not have read one. Measured: every tip
    moved 3 m, the plan centre moved 3 m, every coordinate scaled by 1.02, the arm
    labels permuted onto each other's joints, and the whole frame rotated 30 degrees
    -- all `48 passed`.

    The keys are `body_a` of each joint, so `hub1` is the hub-platform joint at hub1
    and `buoy1` is the buoy-hub joint at buoy1. The platform's own centre is not a
    joint and is not in here; it is the plan centre `(0, 0, z)` and the gate builds
    it from `joint_plane_z`.
    """
    assumptions: tuple[str, ...]
    label: str

    @property
    def n_members(self) -> int:
        return sum(len(b.members) for b in self.bodies)

    @property
    def findings(self) -> tuple[str, ...]:
        return tuple(f for b in self.bodies for f in b.findings)


def rigid_projection(
    coords: NDArray[np.float64], about: NDArray[np.float64]
) -> NDArray[np.float64]:
    """`T_G`: the six rigid motions about `about`, from NODAL COORDINATES ONLY.

    DY1a. Nothing from the builder enters this matrix -- it is a function of the node
    positions and the reference point, so `T_G.T @ M @ T_G` reads the ASSEMBLED matrix
    rather than any intermediate the builder computed.
    """
    n = len(coords)
    t = np.zeros((6 * n, 6), dtype=np.float64)
    for i, point in enumerate(coords):
        d = point - about
        t[6 * i : 6 * i + 3, 0:3] = np.eye(3)
        t[6 * i : 6 * i + 3, 3:6] = np.array(
            [[0.0, d[2], -d[1]], [-d[2], 0.0, d[0]], [d[1], -d[0], 0.0]]
        )
        t[6 * i + 3 : 6 * i + 6, 3:6] = np.eye(3)
    return t


def inertia_about(
    mass_matrix: NDArray[np.float64], coords: NDArray[np.float64], about: NDArray[np.float64]
) -> NDArray[np.float64]:
    """The inertia tensor about `about`, with NO shift to the centroid.

    This is what DY0c's `J_mem(G)` means and it is not what `rigid_properties`
    returns. The distinction cost a 1.07% error in the platform's inertia: the
    members' own centroid is in the joint plane, 10.33 m below G, so an inertia
    reported about the member centroid is not an inertia about G, and subtracting it
    from `J_b(G)` mixes two reference points.
    """
    t = rigid_projection(coords, about)
    return np.array((t.T @ mass_matrix @ t)[3:6, 3:6], dtype=np.float64)


def rigid_properties(
    mass_matrix: NDArray[np.float64], coords: NDArray[np.float64], about: NDArray[np.float64]
) -> tuple[float, NDArray[np.float64], NDArray[np.float64]]:
    """`(mass, CoG offset from `about`, inertia tensor about the CoG)`.

    Read off the 6x6 rigid projection: `[0:3, 0:3]` is `m I`, the coupling block is
    `-m skew(c)`, and `[3:6, 3:6]` is the inertia about `about`. The inertia is then
    shifted to the centroid by the parallel-axis theorem so the returned tensor is
    about the CoG, which is what the deck declares its own about.
    """
    t = rigid_projection(coords, about)
    m6 = t.T @ mass_matrix @ t
    mass = float(m6[0, 0])
    if mass <= 0.0:
        return 0.0, np.zeros(3), np.zeros((3, 3))
    centroid = np.array([m6[1, 5], m6[2, 3], m6[0, 4]], dtype=np.float64) / mass
    about_ref = np.array(m6[3:6, 3:6], dtype=np.float64)
    shift = mass * (float(centroid @ centroid) * np.eye(3) - np.outer(centroid, centroid))
    return mass, centroid, about_ref - shift


def check_rigid_modes(label: str, k_local: NDArray[np.float64], length: float) -> None:
    """F3 § 5's G2.1 refusal, on the MEMBER'S OWN stiffness. Not a warning.

    Two halves, both element-local, both dimensionless:

      * the six rigid motions about the member's midpoint are annihilated, to
        `RIGID_MODE_EXACTNESS`;
      * there is no SEVENTH mode down at the arithmetic floor -- the first
        flexible mode sits at least `RIGID_MODE_BOUND` units of
        `||k_hat|| * eps` above it;
      * and the matrix is POSITIVE SEMI-DEFINITE, which neither of the other two
        can see (R625).

    WHY THE BUILDER AND NOT ONLY THE GATE. F3 § 5 asks for both, and they answer
    different questions. The gate says the sixteen members this deck produces are
    sound; the refusal says that no OTHER deck can produce a member that is not,
    because `build_superstructure` will not return one. A gate alone would leave
    the guarantee attached to one input file.

    An UNRESOLVABLE seventh mode is refused, not passed: at that conditioning the
    question cannot be answered in double precision, and a builder that answers
    anyway is worse than one that stops.
    """
    residual = element_rigid_residual(k_local, length)
    if residual > RIGID_MODE_EXACTNESS:
        raise ValueError(
            f"{label}: the element-local rigid residual is {residual:.6e}, above "
            f"{RIGID_MODE_EXACTNESS:g}. The member's own stiffness does not annihilate "
            "the six rigid motions about its midpoint, so every force this model "
            "reports from it carries that error. The platform is refused rather than "
            "analysed (F3 § 5, G2.1)."
        )
    over = seventh_over_epsilon(k_local, length)
    if over < RIGID_MODE_BOUND:
        raise ValueError(
            f"{label}: the first flexible mode sits at {over:.6e} units of "
            f"||k_hat||*eps, below {RIGID_MODE_BOUND:g}. Either the element has a "
            "SEVENTH mode at the arithmetic floor -- one rigid motion too many, which "
            "is a defect -- or the conditioning makes the question unanswerable in "
            "double precision. Both are refusals (F3 § 5, G2.1)."
        )
    # THE THIRD HALF, AND THE TWO ABOVE WERE BLIND TO IT (R625). Negating a
    # symmetric sub-block leaves every rigid motion annihilated and leaves
    # `|lambda_7|` where it was, so the residual and the seventh-mode ratio both
    # read EXACTLY their clean values with the whole matrix negated -- seven
    # negative eigenvalues, accepted by both. A stiffness that releases energy is
    # not a stiffness, and nothing in this repository rejected one: every spectral
    # read takes an absolute value or clips at zero.
    smallest = element_lambda_min_over_epsilon(k_local, length)
    if smallest < -RIGID_MODE_BOUND:
        raise ValueError(
            f"{label}: the smallest eigenvalue of the homogenised stiffness is "
            f"{smallest:.6e} units of ||k_hat||*eps, below -{RIGID_MODE_BOUND:g}. The "
            "element is INDEFINITE -- it releases energy under some displacement -- "
            "which the rigid residual and the seventh-mode ratio cannot see because "
            "both are blind to sign. The platform is refused (F3 section 5, G2.1, R625)."
        )


def check_limits(label: str, length: float, section: Section) -> None:
    """F3 § 2's two refusals, on MEMBER length. Not a warning, not a clamp."""
    # D_o is recovered from the area and the second moment rather than passed in, so
    # the check cannot be fed a diameter that disagrees with the section it checks.
    d_outer = _outer_diameter(section)
    radius_of_gyration = math.sqrt(section.I_y / section.A)
    over_d = length / d_outer
    over_r = length / radius_of_gyration
    if over_d < MIN_LENGTH_OVER_DIAMETER:
        raise ValueError(
            f"{label}: L/D = {over_d:.3f} is below {MIN_LENGTH_OVER_DIAMETER:g}. "
            "Below it the cross-section is not slender against the span and a space "
            "frame is the wrong model, so the member is refused rather than analysed."
        )
    if over_r > MAX_LENGTH_OVER_GYRATION:
        raise ValueError(
            f"{label}: L/r = {over_r:.1f} exceeds {MAX_LENGTH_OVER_GYRATION:g}, the "
            "slenderness ceiling. Refused rather than analysed."
        )


def _outer_diameter(section: Section) -> float:
    """Recover `D_o` for a circular tube from `A` and `I`.

    For a hollow circle, `I/A = (D_o^2 + D_i^2)/16`, and `A = pi/4 (D_o^2 - D_i^2)`,
    so `D_o^2 = 8 I/A + 2A/pi` after eliminating `D_i`. Derived rather than stored
    because a stored diameter can disagree with the properties beside it.
    """
    return math.sqrt(8.0 * section.I_y / section.A + 2.0 * section.A / math.pi)


def _full_scale_deck(path: Path, lam: float) -> dict[str, Any]:
    """Read the generated deck YAML and Froude-scale what this module uses.

    Only lengths, masses and inertias are scaled, through `floatfea.io.froude`, which
    is the one place a scale change happens (`CLAUDE.md` § Conventions).
    """
    import yaml

    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    bodies: dict[str, Any] = {}
    for body in raw["bodies"]:
        inertia = body["inertia"]
        bodies[body["name"]] = {
            "reference_point": [
                float(to_full_scale(c, "length", lam)) for c in body["reference_point"]
            ],
            "mass": float(to_full_scale(float(body["mass"]), "mass", lam)),
            "inertia": np.array(
                [
                    [inertia["Ixx"], inertia["Ixy"], inertia["Ixz"]],
                    [inertia["Ixy"], inertia["Iyy"], inertia["Iyz"]],
                    [inertia["Ixz"], inertia["Iyz"], inertia["Izz"]],
                ],
                dtype=np.float64,
            )
            * to_full_scale(1.0, "inertia", lam),
        }
    joints = []
    for joint in raw["joints"]:
        joints.append(
            {
                "type": joint["type"],
                "body_a": joint["body_a"],
                "body_b": joint["body_b"],
                "point": [
                    float(to_full_scale(r + a, "length", lam))
                    for r, a in zip(
                        raw_reference(raw, joint["body_a"]), joint["attach_a_body"], strict=True
                    )
                ],
            }
        )
    return {"bodies": bodies, "joints": joints}


def raw_reference(raw: dict[str, Any], name: str) -> list[float]:
    """A body's model-scale reference point, by name."""
    for body in raw["bodies"]:
        if body["name"] == name:
            return [float(c) for c in body["reference_point"]]
    raise KeyError(f"no body named {name!r} in the deck")


def _member_geometry(
    joints: list[dict[str, Any]], hub_joints: list[dict[str, Any]], z: float
) -> dict[str, list[tuple[str, tuple[float, float, float], tuple[float, float, float]]]]:
    """Per body, its members as `(label, start, end)` in the joint plane.

    Separated from the mass work so the geometry is decided once and the `f` ladder
    can rebuild a body without re-deriving where its members are.
    """
    buoy_joints = [j for j in joints if j["body_a"].startswith("buoy")]
    out: dict[str, list[tuple[str, tuple[float, float, float], tuple[float, float, float]]]] = {}
    centre = (0.0, 0.0, z)
    out["platform"] = [
        (
            f"platform:{j['body_a']}_arm",
            centre,
            (j["point"][0], j["point"][1], z),
        )
        for j in sorted(hub_joints, key=lambda j: j["body_a"])
    ]
    for hub in sorted(j["body_a"] for j in hub_joints):
        node = next((j["point"][0], j["point"][1], z) for j in hub_joints if j["body_a"] == hub)
        cluster = sorted((j for j in buoy_joints if j["body_b"] == hub), key=lambda j: j["body_a"])
        if len(cluster) != 3:
            raise ValueError(
                f"{hub} carries {len(cluster)} cluster arms; the platform is four "
                "tripods of three, and a hub with another count is not this model."
            )
        out[hub] = [
            (
                f"{hub}:{j['body_a']}_arm",
                node,
                (j["point"][0], j["point"][1], z),
            )
            for j in cluster
        ]
    return out


def _build_body(
    name: str,
    geometry: list[tuple[str, tuple[float, float, float], tuple[float, float, float]]],
    body: dict[str, Any],
    fraction: float,
    section: Section,
    preliminary: bool,
    basis_note: str,
    laddered: bool = True,
) -> BodyModel:
    """One body at one `f`, with its remainder placed to match the deck's CoG.

    No admissibility decision is taken here: this builds the body and reports what it
    came to, and `build_superstructure` descends the ladder on the result. Keeping the
    two apart is what lets the chosen `f` be asserted rather than inferred.
    """
    deck_mass = float(body["mass"])
    deck_cog = np.asarray(body["reference_point"], dtype=np.float64)
    deck_inertia = np.asarray(body["inertia"], dtype=np.float64)

    model = Model()
    node_of: dict[tuple[float, ...], int] = {}

    def node(point: tuple[float, ...], label: str) -> int:
        key = tuple(round(c, 9) for c in point)
        if key not in node_of:
            node_of[key] = model.nodes.add(Node(point[0], point[1], point[2], name=label))
        return node_of[key]

    centre_node = node(geometry[0][1], f"{name}_centre")
    members: list[Member] = []
    for label, start, end in geometry:
        a = node(start, f"{name}_centre" if start == geometry[0][1] else f"{label}_a")
        b = node(end, f"{label}_tip")
        length = math.dist(start, end)
        check_limits(label, length, section)
        members.append(
            Member(
                node_a=a,
                node_b=b,
                section=section,
                label=label,
                length=length,
                preliminary=preliminary,
                section_basis=basis_note,
            )
        )

    total_length = sum(m.length for m in members)
    member_mass = fraction * deck_mass
    line_mass = member_mass / total_length if total_length > 0.0 else 0.0
    density = line_mass / section.A
    material = Material(
        E=S355.E, nu=S355.nu, rho=density, fy=S355.fy, name=f"{S355.name}-equivalent"
    )

    # G2.1 ON EVERY MEMBER THIS BODY OWNS, HERE AND NOT IN THE LOOP ABOVE, because
    # the body's equivalent material is what the member is finally built with and it
    # is not known until the total length is. Only `rho` differs from S355 and the
    # rigid-mode quantities do not read it, so the refusal would land identically in
    # the loop -- it is placed here so that what is checked is what is shipped.
    for member in members:
        check_rigid_modes(
            member.label,
            local_stiffness(member.section, material, member.length),
            member.length,
        )

    # The remainder goes where it makes the combined first moment equal the deck's.
    first_moment = np.zeros(3, dtype=np.float64)
    for member in members:
        midpoint = (
            np.asarray(model.nodes[member.node_a].xyz) + np.asarray(model.nodes[member.node_b].xyz)
        ) / 2.0
        first_moment += (member.length * line_mass) * midpoint
    remainder_mass = (1.0 - fraction) * deck_mass
    if remainder_mass > 0.0:
        remainder_point = (deck_mass * deck_cog - first_moment) / remainder_mass
    else:
        # f = 1 leaves nothing to place; the point is the CoG so the link is defined.
        remainder_point = deck_cog.copy()

    remainder_node = node(tuple(float(c) for c in remainder_point), f"{name}_remainder")
    link_length = math.dist(
        np.asarray(model.nodes[centre_node].xyz).tolist(), remainder_point.tolist()
    )

    # J_mem ABOUT G, FROM THE ASSEMBLED MATRIX (DY2). Not a rod formula: the element
    # mass matrix carries rotary inertia as `rho_eq * I`, which a line-mass formula
    # omits, and R592 was exactly the discrepancy that omission produced.
    provisional = BodyModel(
        name=name,
        model=model,
        members=tuple(members),
        material=material,
        mass_fraction=fraction,
        equivalent_density=density,
        remainder_mass=remainder_mass,
        remainder_inertia=np.zeros((3, 3)),
        remainder_point=remainder_point,
        centre_node=centre_node,
        remainder_node=remainder_node,
        link_length=link_length,
        deck_mass=deck_mass,
        deck_cog=deck_cog,
        deck_inertia=deck_inertia,
        member_mass=member_mass,
    )
    member_only = assemble_mass_dense(model, provisional.elements)
    inertia_member = inertia_about(member_only, model.nodes.coords(), deck_cog)

    offset = remainder_point - deck_cog
    parallel = remainder_mass * (float(offset @ offset) * np.eye(3) - np.outer(offset, offset))
    remainder_inertia = deck_inertia - inertia_member - parallel

    findings: list[str] = []
    if density > basis.RHO_STEEL:
        findings.append(
            f"{name}: the equivalent density is {density:.1f} kg/m^3, ABOVE steel at "
            f"{basis.RHO_STEEL:g}. The members are stiffness equivalents so a density "
            "above steel is not impossible, but it means this body's mass does not fit "
            "inside F1's section at the chosen fraction and the section or the fraction "
            "is the thing to look at."
        )
    if not laddered:
        # The CAUSAL clause below is true only of a fraction the ladder descended to:
        # it names what `admissible()` rejected at the rung above. A fraction handed in
        # by a caller was not rejected by anything, so the cause is dropped and the
        # finding states the fact (BG0). It is a finding at ANY off-ladder fraction,
        # above the default as much as below, because what makes the value reportable
        # is that nothing admitted it.
        findings.append(
            f"{name}: the mass fraction is {fraction:g}, handed in by the caller rather "
            f"than taken from {MASS_FRACTION_LADDER}, so `admissible()` was never "
            "consulted for it. This body is a MEASUREMENT, not one to ship."
        )
    elif fraction < MASS_FRACTION_LADDER[0]:
        findings.append(
            f"{name}: the mass fraction is {fraction:g} rather than the default "
            f"{MASS_FRACTION_LADDER[0]:g}, because the default left a negative "
            "remainder mass or a remainder inertia with a negative eigenvalue. "
            "Reported as a sizing finding (DY0d), not a clamp."
        )

    return BodyModel(
        name=name,
        model=model,
        members=tuple(members),
        material=material,
        mass_fraction=fraction,
        equivalent_density=density,
        remainder_mass=remainder_mass,
        remainder_inertia=remainder_inertia,
        remainder_point=remainder_point,
        centre_node=centre_node,
        remainder_node=remainder_node,
        link_length=link_length,
        deck_mass=deck_mass,
        deck_cog=deck_cog,
        deck_inertia=deck_inertia,
        member_mass=member_mass,
        findings=tuple(findings),
    )


def admissible(body: BodyModel) -> bool:
    """`m_r >= 0` and no eigenvalue of `J_r` below `-tol` (DY0d).

    **PSD, AND NOT REALISABILITY, BY DECISION (EA3).** The remainder's `J_r` is
    PSD at every `f` on the ladder and violates the triangle inequality at every
    `f > 0`, reaching zero slack only at `f = 0`, which puts no mass on the
    members at all. That is inherited from the deck, whose own `J_G` sits exactly
    on the lamina boundary, not created by the split (DZ5).

    **IT IS NOT LINEAR IN `f` ON THE PLATFORM (C80, R618).** This said it was.
    `slack/f` runs `-5.354e+08, -4.464e+08, -3.829e+08, -3.353e+08, -2.982e+08`
    over `f = 0.5 ... 0.1` -- a `1.80x` spread -- so the quantity is not
    proportional to `f` there. It is exactly linear on the four hubs, at
    `-2.03055e+06` per unit `f`, which is probably where the claim came from. The
    RULING is unaffected: slack is negative at every rung with `f > 0` and
    exactly zero at `f = 0` on all five bodies, which is the whole of what
    "requiring realisability would force `f = 0`" needs.

    Every figure in this docstring is produced by the sweep in F3 step 2's report
    (C83, R620), which rebuilds each body at each rung of `MASS_FRACTION_LADDER`
    through `_build_body` and takes the slack from `remainder_inertia`. A figure
    in a docstring is a report nothing regenerates, so the derivation lives where
    rule regenerates it and this entry carries the numbers it needs and a pointer.

    So requiring realisability here would force `f = 0`, which is worse for member
    forces than an unrealisable remainder: it would leave the arms massless. The
    weaker test is the intended one, and this docstring claims PSD only, which is
    what the two lines below compute.

    **THE SLACK IS REPORTED IN `assumptions`, NOT `findings` (C81, R619).** This
    said `findings`, and `Superstructure.findings` and every body's `findings` are
    `()` at the shipped configuration -- so the sentence pointed a reader at an
    empty tuple. The entry carrying both figures is the last one in
    `Superstructure.assumptions`.
    """
    if body.remainder_mass < 0.0:
        return False
    if body.remainder_mass == 0.0 and not np.any(body.remainder_inertia):
        return True
    scale = max(float(np.max(np.abs(body.deck_inertia))), 1.0)
    eigenvalues = np.linalg.eigvalsh((body.remainder_inertia + body.remainder_inertia.T) / 2.0)
    return bool(np.min(eigenvalues) >= -MASS_PROPERTY_AGREEMENT * scale)


def body_mass_matrix(body: BodyModel) -> NDArray[np.float64]:
    """The ASSEMBLED global mass matrix: members plus the lumped remainder.

    The remainder is a 6x6 block at its own node -- translational mass on the
    diagonal and `J_r` in the rotational block. The rigid link to the centre node is
    a KINEMATIC constraint and does not change the rigid-body mass properties, which
    is why it does not appear here and why `rigid_properties` on this matrix is the
    right thing for G3.1a to read.
    """
    mass = assemble_mass_dense(body.model, body.elements)
    base = 6 * body.remainder_node
    for i in range(3):
        mass[base + i, base + i] += body.remainder_mass
    mass[base + 3 : base + 6, base + 3 : base + 6] += body.remainder_inertia
    return mass


def build_superstructure(
    path: Path | None = None,
    froude_lambda: float = 50.0,
    mass_fraction: float | None = None,
) -> Superstructure:
    """The five-body superstructure at full scale, or a refusal.

    Every coordinate comes from the deck's own joint points. Nothing is typed, and no
    nominal radius is used -- DJ1's rule, and the reason the deck export exists.
    """
    deck = _full_scale_deck(path or DECK_YAML, froude_lambda)
    bodies, joints = deck["bodies"], deck["joints"]

    hub_joints = [j for j in joints if j["body_b"] == "platform"]
    buoy_joints = [j for j in joints if j["body_a"].startswith("buoy")]
    if len(hub_joints) != 4 or len(buoy_joints) != 12:
        raise ValueError(
            f"expected 4 hub-platform joints and 12 buoy-hub joints; got "
            f"{len(hub_joints)} and {len(buoy_joints)}. The topology is not the "
            "platform this builder describes."
        )

    # THE PLANE IS THE EXACT VALUE, NOT A ROUNDED ONE. A first version took
    # `round(z, 9)` for the set-membership check and then used the ROUNDED number as
    # the plane, so every node was up to 5e-10 m off the joint points it came from --
    # a discrepancy invented by the check rather than present in the deck, and the
    # CoG gate caught it.
    elevations = {j["point"][2] for j in joints}
    if len(elevations) != 1:
        raise ValueError(
            f"the joint points span {len(elevations)} elevations {sorted(elevations)}; "
            "this builder makes a PLANAR frame and DW1's ruling rests on them being "
            "coplanar. A non-planar deck is refused rather than flattened."
        )
    z = elevations.pop()

    section = Section.circular_tube(ARM_OUTER_DIAMETER, ARM_WALL)
    geometry = _member_geometry(joints, hub_joints, z)

    built: list[BodyModel] = []
    for name in ["platform", *sorted(j["body_a"] for j in hub_joints)]:
        preliminary = name == "platform"
        note = (
            "docs/milestones/F1.md:389 for the SECTION (stiffness); F1.md:390 records "
            "this arm as a TRIANGULATED truss of undecided depth, so the tube is a "
            "stiffness equivalent and the member is marked preliminary"
            if preliminary
            else "docs/milestones/F1.md:389, basis at F1.md:425-433"
        )
        if mass_fraction is not None:
            # EK1's f SENSITIVITY. The ladder is bypassed on purpose: EK1 asks for
            # f = 0.25 and 0.75, neither of which is on it, and 0.75 is ABOVE the
            # default. `_build_body` accepts any fraction and reports findings rather
            # than refusing, so an off-ladder build carries its own warnings and
            # `admissible()` is NOT consulted -- the point of the sensitivity is to see
            # what the member forces do, including at a fraction the ladder would have
            # rejected. A caller passing this gets a model to MEASURE, not one to ship.
            built.append(
                _build_body(
                    name,
                    geometry[name],
                    bodies[name],
                    mass_fraction,
                    section,
                    preliminary,
                    note,
                    laddered=False,
                )
            )
            continue
        for fraction in MASS_FRACTION_LADDER:
            candidate = _build_body(
                name, geometry[name], bodies[name], fraction, section, preliminary, note
            )
            if admissible(candidate):
                built.append(candidate)
                break
        else:  # pragma: no cover - f = 0 is always admissible
            raise ValueError(
                f"{name}: no fraction in {MASS_FRACTION_LADDER} is admissible, which "
                "cannot happen because f = 0 puts the whole body mass at the "
                "remainder and asks the members to carry none."
            )

    # DY4: keyed by (body, node), because twelve buoys map onto node indices 1, 2, 3
    # across five separate models and an index alone does not say which model.
    buoy_nodes: dict[str, tuple[str, int]] = {}
    for hub_body in built[1:]:
        for member in hub_body.members:
            buoy = member.label.split(":")[1].removesuffix("_arm")
            buoy_nodes[buoy] = (hub_body.name, member.node_b)

    return Superstructure(
        bodies=tuple(built),
        froude_lambda=froude_lambda,
        joint_plane_z=z,
        buoy_joint_nodes=buoy_nodes,
        deck_joint_points={
            j["body_a"]: (j["point"][0], j["point"][1], j["point"][2]) for j in joints
        },
        deck_joint_owner={j["body_a"]: j["body_b"] for j in joints},
        label=(
            "buoy spar columns not assessed as members; "
            "buoy loads applied as joint reactions; "
            "platform mass properties as in FloatSim; see DZ5 finding"
        ),
        assumptions=(
            "the deck's `reference_point` IS the body's CoG. FloatSim's own "
            "`driver.py:203-209` states it -- \"the deck's reference_point IS the body "
            'frame origin and the CoG (no explicit CoG-offset field in the deck)" -- '
            "so the referent is declared upstream rather than in the deck, and G3.1a "
            "compares against it on that basis.",
            f"FROUDE-SCALED from model scale to full scale at lambda = "
            f"{froude_lambda:g} by floatfea.io.froude.",
            "the in-plane members are STIFFNESS equivalents of a truss with depth, not "
            "mass models (DY0). Steel density is not used for member mass: four 50 m "
            "platform arms at F1's section in steel weigh 2059.7 t against a 1250.0 t "
            "body. The mass splits by fraction instead, and the members carry it as a "
            "uniform line mass through an equivalent density.",
            "no buoy mass is in the model: each buoy's inertia reaches the arm tip "
            "through its gimbal reaction, and a lumped buoy mass beside it would "
            "double-count.",
            "the frame is a tree -- nothing joins adjacent hubs or adjacent buoy "
            "joints -- so each body is statically determinate and there is no "
            "redundancy. This is an observation about the platform.",
            "the deck's body inertias are kept AS FLOATSIM HAS THEM, because "
            "inertia-relief equilibrium with FloatSim's loads requires it, and they "
            "are physically inconsistent: every body's J_G satisfies the LAMINA "
            "identity exactly -- triangle-inequality slack 0.0000e+00 -- and the "
            "platform's is M * 50^2 * (1, 1, 2) exactly, giving a radius of gyration "
            "about z of 70.711 m against 50 m arms and a 51.056 m extent. The "
            "remainder inertia the split leaves is PSD but violates the triangle "
            "inequality by -2.6770e+08 kg.m^2 on the platform and -1.0153e+06 on "
            "each hub. See the DZ5 finding.",
        ),
    )
