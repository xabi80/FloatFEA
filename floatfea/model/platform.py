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

WHAT IT REPORTS RATHER THAN REFUSING. A body whose members outweigh it. F3 § 3.3:
"report it as a sizing finding, not a clamp to zero. A negative remainder is
information about the section, and clamping it would make G3.1a pass on a body whose
steel does not fit inside its own mass."
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Final

import numpy as np
from numpy.typing import NDArray

from floatfea import basis
from floatfea.assemble.system import BeamElement
from floatfea.io.froude import to_full_scale
from floatfea.model.material import S355, Section
from floatfea.model.nodes import Model, Node

DECK_YAML: Final[Path] = (
    Path(__file__).resolve().parents[2] / "data" / "platform" / "platform12_deck.yaml"
)

MIN_LENGTH_OVER_DIAMETER: Final[float] = 2.0
MAX_LENGTH_OVER_GYRATION: Final[float] = 300.0
_NEGLIGIBLE_FRACTION: Final[float] = 1e-12
"""not-a-tolerance: the fraction of a body's own mass or inertia below which a
remainder is reported as zero. It is a REPORTING threshold on a quantity that is
zero by construction when a member is mass-sized -- nothing is judged close enough
to anything -- and the finding it gates is a sentence, not a pass or a fail."""
"""F3 § 2's builder limits, verbatim, and neither is a tolerance.

not-a-tolerance: they are properties of the model the tool ACCEPTS, declared in the
plan and asserted here. Nothing is compared against them to decide whether a computed
number is close enough to another, which is why they are not in
`floatfea.tolerances`. `L/D >= 2` keeps a member in the range a beam element
describes at all; `L/r <= 300` is the slenderness ceiling.
"""

CLUSTER_ARM_OUTER_DIAMETER: Final[float] = 2.5
CLUSTER_ARM_WALL: Final[float] = 0.180
"""`docs/milestones/F1.md:389` — the one RECORDED section, and its basis is at
`F1.md:425-433`: the joint delivers 5.93 MN at the rod tip, over 25 m that is
M = 148.2 MN·m, demand W = 0.696 m³ against 0.710 supplied. F1's own caveat travels
with it: the order check makes the section "plausible rather than comfortable".

not-a-tolerance: a designed geometry, cited to its source. Nothing is compared
against it.
"""

HUB_ARM_OUTER_DIAMETER: Final[float] = 2.5
"""The outer diameter assumed when sizing a hub arm to its body's mass.

`docs/milestones/F1.md:390` records the platform cross-truss arm as "50 m span,
TRIANGULATED, depth undecided" — so there is no recorded tubular section for it, and
DJ1's rule applies: sized to reproduce the body's mass and marked `preliminary`. The
diameter is carried over from the cluster arm so that one number is assumed rather
than two; the wall follows from the mass.
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
    """One FloatSim body as a free-free structural model."""

    name: str
    model: Model
    members: tuple[Member, ...]
    remainder_mass: float
    remainder_inertia: NDArray[np.float64]
    remainder_node: int
    link_length: float
    deck_mass: float
    member_mass: float
    findings: tuple[str, ...] = field(default_factory=tuple)

    @property
    def elements(self) -> list[BeamElement]:
        """The members as assembler input."""
        return [
            BeamElement(node_a=m.node_a, node_b=m.node_b, section=m.section, material=S355)
            for m in self.members
        ]

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
    buoy_joint_nodes: dict[str, int]
    assumptions: tuple[str, ...]
    label: str

    @property
    def n_members(self) -> int:
        return sum(len(b.members) for b in self.bodies)

    @property
    def findings(self) -> tuple[str, ...]:
        return tuple(f for b in self.bodies for f in b.findings)


def size_to_mass(target_mass: float, count: int, length: float, d_outer: float) -> Section:
    """A circular tube of `d_outer` whose `count` members of `length` weigh `target_mass`.

    DJ1: "any member without a recorded section is sized to reproduce its body's
    mass and marked `preliminary`". This is that sizing, and it is exact rather than
    iterated: the area follows from the mass, and the wall from the area.

    Raises rather than returning a degenerate tube, because a target mass that needs
    a wall thicker than the radius is a statement about the body, not a section to
    build.
    """
    if target_mass <= 0.0 or count <= 0 or length <= 0.0:
        raise ValueError(f"cannot size to mass {target_mass} over {count} members of {length} m")
    area = target_mass / (count * length * basis.RHO_STEEL)
    # A = pi/4 (D_o^2 - D_i^2)  =>  D_i = sqrt(D_o^2 - 4A/pi)
    inner_sq = d_outer**2 - 4.0 * area / math.pi
    if inner_sq <= 0.0:
        raise ValueError(
            f"a tube of outer diameter {d_outer} m cannot reach area {area:.6f} m^2 "
            f"without a solid section; the body mass {target_mass:.3e} kg over "
            f"{count} members of {length} m needs a larger diameter. Sizing is "
            "refused rather than clamped to solid, because a solid rod is a "
            "different member and would be reported as a tube."
        )
    thickness = (d_outer - math.sqrt(inner_sq)) / 2.0
    return Section.circular_tube(d_outer, thickness)


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


def build_superstructure(path: Path | None = None, froude_lambda: float = 50.0) -> Superstructure:
    """The five-body superstructure at full scale, or a refusal.

    Every coordinate comes from the deck's own joint points. Nothing is typed, and
    no nominal radius is used — DJ1's rule, and the reason the deck export exists.
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
    # a discrepancy invented by the check rather than present in the deck.
    elevations = {j["point"][2] for j in joints}
    if len(elevations) != 1:
        raise ValueError(
            f"the joint points span {len(elevations)} elevations {sorted(elevations)}; "
            "this builder makes a PLANAR frame and DW1's ruling rests on them being "
            "coplanar. A non-planar deck is refused rather than flattened."
        )
    z = elevations.pop()

    built: list[BodyModel] = []
    buoy_nodes: dict[str, int] = {}

    # ---------------------------------------------------------------- platform
    model = Model()
    centre = model.nodes.add(Node(0.0, 0.0, z, name="centre"))
    hub_nodes: dict[str, int] = {}
    for joint in sorted(hub_joints, key=lambda j: j["body_a"]):
        px, py, _pz = joint["point"]
        hub_nodes[joint["body_a"]] = model.nodes.add(
            Node(px, py, z, name=f"{joint['body_a']}_node")
        )
    platform_mass = bodies["platform"]["mass"]
    hub_arm_length = min(math.dist((0.0, 0.0), (j["point"][0], j["point"][1])) for j in hub_joints)
    hub_arm_section = size_to_mass(
        platform_mass, len(hub_joints), hub_arm_length, HUB_ARM_OUTER_DIAMETER
    )
    members: list[Member] = []
    for name, node in hub_nodes.items():
        length = math.dist(model.nodes[centre].xyz.tolist(), model.nodes[node].xyz.tolist())
        label = f"platform:{name}_arm"
        check_limits(label, length, hub_arm_section)
        members.append(
            Member(
                node_a=centre,
                node_b=node,
                section=hub_arm_section,
                label=label,
                length=length,
                preliminary=True,
                section_basis=(
                    "sized to reproduce the platform body's deck mass (DJ1); "
                    "F1.md:390 records this arm as a TRIANGULATED truss of undecided "
                    "depth, so no tubular section is on record"
                ),
            )
        )
    built.append(_finish("platform", model, members, bodies["platform"], centre, z))

    # ---------------------------------------------------------------- the hubs
    for hub in sorted(hub_nodes):
        model = Model()
        node = model.nodes.add(Node(*_point_of(hub_joints, hub), name=f"{hub}_node"))
        cluster = sorted((j for j in buoy_joints if j["body_b"] == hub), key=lambda j: j["body_a"])
        if len(cluster) != 3:
            raise ValueError(
                f"{hub} carries {len(cluster)} cluster arms; the platform is four "
                "tripods of three, and a hub with another count is not this model."
            )
        section = Section.circular_tube(CLUSTER_ARM_OUTER_DIAMETER, CLUSTER_ARM_WALL)
        members = []
        for joint in cluster:
            tip = model.nodes.add(
                Node(joint["point"][0], joint["point"][1], z, name=f"{joint['body_a']}_joint")
            )
            buoy_nodes[joint["body_a"]] = tip
            length = math.dist(model.nodes[node].xyz.tolist(), model.nodes[tip].xyz.tolist())
            label = f"{hub}:{joint['body_a']}_arm"
            check_limits(label, length, section)
            members.append(
                Member(
                    node_a=node,
                    node_b=tip,
                    section=section,
                    label=label,
                    length=length,
                    preliminary=False,
                    section_basis="docs/milestones/F1.md:389, basis at F1.md:425-433",
                )
            )
        built.append(_finish(hub, model, members, bodies[hub], node, z))

    return Superstructure(
        bodies=tuple(built),
        froude_lambda=froude_lambda,
        joint_plane_z=z,
        buoy_joint_nodes=buoy_nodes,
        label=(
            "buoy spar columns not assessed as members; " "buoy loads applied as joint reactions"
        ),
        assumptions=(
            "body mass and inertia are taken at the deck's `reference_point`; the "
            "deck declares no `cog` and no `inertia_reference_point`, and the schema "
            "enumerates both, so this is the only consistent reading rather than a "
            "chosen convention.",
            f"FROUDE-SCALED from model scale to full scale at lambda = "
            f"{froude_lambda:g} by floatfea.io.froude.",
            "no buoy mass is in the model: each buoy's inertia reaches the arm tip "
            "through its gimbal reaction, and a lumped buoy mass beside it would "
            "double-count.",
            "the frame is a tree -- nothing joins adjacent hubs or adjacent buoy "
            "joints -- so each body is statically determinate and there is no "
            "redundancy. This is an observation about the platform.",
        ),
    )


def _point_of(joints: list[dict[str, Any]], body: str) -> tuple[float, float, float]:
    for joint in joints:
        if joint["body_a"] == body:
            return (joint["point"][0], joint["point"][1], joint["point"][2])
    raise KeyError(body)


def _finish(
    name: str,
    model: Model,
    members: list[Member],
    body: dict[str, Any],
    node: int,
    plane_z: float,
) -> BodyModel:
    """Attach the remainder mass, and report a body its members outweigh."""
    member_mass = sum(m.section.A * m.length * basis.RHO_STEEL for m in members)
    deck_mass = body["mass"]
    remainder = deck_mass - member_mass

    findings: list[str] = []
    if remainder < 0.0:
        findings.append(
            f"{name}: its members weigh {member_mass:.6e} kg and the deck gives the "
            f"body {deck_mass:.6e} kg, so the remainder is {remainder:.6e} kg -- "
            f"NEGATIVE by {abs(remainder) / deck_mass:.1%}. Reported rather than "
            "clamped to zero (F3 section 3.3): clamping would make G3.1a pass on a "
            "body whose steel does not fit inside its own mass."
        )

    # The remainder sits at the deck's reference point, on a rigid link from `node`.
    reference = body["reference_point"]
    link = math.dist(reference, model.nodes[node].xyz.tolist())

    # n members radiating from `node` in the plane, each a uniform rod: about the
    # vertical axis through the node, sum of m_i L_i^2 / 3.
    member_izz = sum(
        (m.section.A * m.length * basis.RHO_STEEL) * m.length**2 / 3.0 for m in members
    )
    remaining = body["inertia"].copy()
    remaining[2][2] -= member_izz
    deck_izz = float(body["inertia"][2][2])
    if remaining[2][2] < 0.0:
        findings.append(
            f"{name}: its members' Izz about the body node is {member_izz:.6e} "
            f"kg.m^2 and the deck gives {deck_izz:.6e}, so the remaining Izz is "
            "negative. Reported, not clamped."
        )

    # A REMAINDER OF ZERO MASS CARRYING ROTARY INERTIA IS NOT A POINT MASS, and it is
    # what mass-sizing a member to its body produces. Representable in a mass matrix,
    # but it says the sized TUBE does not represent the body's real mass
    # distribution -- F1.md:390 records the platform arm as a TRIANGULATED truss,
    # whose mass sits in chords far from the centroid and therefore delivers more Izz
    # for the same mass.
    if abs(remainder) <= _NEGLIGIBLE_FRACTION * deck_mass and remaining[2][2] > 0.0:
        findings.append(
            f"{name}: the remainder mass is {remainder:.3e} kg -- zero to within "
            f"{_NEGLIGIBLE_FRACTION:g} of the deck mass -- while the remaining Izz is "
            f"{remaining[2][2]:.6e} kg.m^2. Matching both the deck's mass and its Izz "
            "therefore needs rotary inertia with no mass attached. The members "
            f"deliver {member_izz:.6e} against the deck's {deck_izz:.6e}, a factor of "
            f"{deck_izz / member_izz:.4f}, so a mass-sized tube under-represents this "
            "body's mass distribution by that factor."
        )

    # AND THE DECK'S OWN INERTIA FOR THIS BODY MAY BE A PLACEHOLDER, which G3.1a has
    # to know before it asserts against it.
    ixx, iyy = float(body["inertia"][0][0]), float(body["inertia"][1][1])
    if ixx > 0.0 and abs(ixx + iyy - deck_izz) <= _NEGLIGIBLE_FRACTION * deck_izz:
        findings.append(
            f"{name}: the deck's inertia satisfies Ixx + Iyy = Izz exactly "
            f"({ixx:.6e} + {iyy:.6e} = {deck_izz:.6e}), the perpendicular-axis "
            "identity for a LAMINA. A real three-dimensional body does not satisfy "
            "it -- the buoys in this same deck do not -- so this body's inertia is a "
            "typed placeholder rather than a derived figure "
            "(`platform_common.py:159,178`; HSP's own `platform-geometry.md:46` flags "
            "the hub value as Q2). G3.1a's MASS and CoG halves assert against real "
            "design figures; its INERTIA half would assert against this."
        )

    return BodyModel(
        name=name,
        model=model,
        members=tuple(members),
        remainder_mass=remainder,
        remainder_inertia=remaining,
        remainder_node=node,
        link_length=link,
        deck_mass=deck_mass,
        member_mass=member_mass,
        findings=tuple(findings),
    )
