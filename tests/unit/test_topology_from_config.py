"""FL2(a): the platform's member topology comes from the configuration.

The star is the DEFAULT and it is GENERATED, which is what every run before FL2(a) did
unconditionally. Two properties carry this item:

1. **The declared star is the generated star**, labels and node identities included. The
   labels are published in all three R1 deliverables and step 1's gate fixtures name
   `platform:hub4_arm`, so a topology identical to the default must not rename a row.
2. **A non-star topology places the body centre correctly.** `_build_body` read the FIRST
   member's start point as the body centre, which is the centre for a star and a HUB for
   any topology whose first member does not touch the centre. `centre_node` is what the
   remainder mass is rigidly linked to, so that inference would have attached the
   platform's entire remainder -- and the loads reaching it -- at a hub while the
   configuration said otherwise.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.model.platform import build_superstructure
from floatfea.run.config import ConfigError, load_config
from floatfea.solve.static import joint_nodes_of
from floatfea.tolerances import NODE_COINCIDENCE_DECIMALS

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"

HUBS = ("hub1", "hub2", "hub3", "hub4")
STAR = tuple(("centre", h) for h in HUBS)


def _platform(ss: Any) -> list[Any]:
    return [m for b in ss.bodies if b.name == "platform" for m in b.members]


def _body(ss: Any) -> Any:
    return next(b for b in ss.bodies if b.name == "platform")


@pytest.fixture(scope="module")
def generated() -> Any:
    """The star, generated -- the behaviour every run had before FL2(a)."""
    return build_superstructure()


@pytest.fixture(scope="module")
def declared() -> Any:
    """The same star, declared member by member in the configuration's own form."""
    return build_superstructure(platform_members=STAR)


def test_FL2a_the_DECLARED_star_is_the_GENERATED_star(generated: Any, declared: Any) -> None:
    """Member for member, including the labels and the node identities.

    The labels reach three published deliverables and step 1's gate names
    `platform:hub4_arm` ROOT, so this is what stops a declared default from renaming a
    published row. `_platform_label` is the part that makes it hold: a declared member
    touching the centre takes the generated star's `platform:<hub>_arm` form.
    """
    gen, dec = _platform(generated), _platform(declared)
    assert len(gen) == len(dec) == 4
    for a, b in zip(gen, dec, strict=True):
        assert a.label == b.label, (a.label, b.label)
        assert (a.node_a, a.node_b) == (b.node_a, b.node_b), a.label
        assert a.length == b.length, a.label  # not-a-tolerance: the same two points


def test_FL2a_the_declared_star_puts_the_SAME_MASS_on_the_members(
    generated: Any, declared: Any
) -> None:
    """The mass follows the total length, so identical geometry is identical mass."""
    assert _body(generated).member_mass == _body(declared).member_mass
    assert _body(generated).centre_node == _body(declared).centre_node


def test_FL2a_a_NON_STAR_topology_centres_the_body_at_its_OWN_CENTRE() -> None:
    """The defect the passed centre prevents, asserted on the consequence.

    The first declared member here is hub-to-hub, so the old inference
    (`geometry[0][1]`, the first member's start) would have named `hub1` the body centre.
    `rigid_links` ties `remainder_node` to `centre_node` and measures the offset between
    them, so the platform's whole remainder mass would have hung off a hub.

    This asserts the centre is the ORIGIN of the joint plane rather than asserting which
    expression computed it, so the property survives a different implementation.
    """
    braced = (("hub1", "hub2"), *STAR)
    ss = build_superstructure(platform_members=braced)
    body = _body(ss)
    assert [m.label for m in body.members][0] == "platform:hub1_hub2"
    centre = body.model.nodes[body.centre_node]
    assert centre.name == "platform_centre"
    assert np.allclose(centre.xyz[:2], [0.0, 0.0]), centre.xyz
    # and the braced member is a real fifth member, not a silently dropped one
    assert len(body.members) == 5


def test_FL2a_a_hub_to_hub_member_takes_the_PAIR_label() -> None:
    """A member with no centre end has no `_arm` form to match, so it names both ends."""
    ss = build_superstructure(platform_members=(("hub1", "hub2"), *STAR))
    labels = [m.label for m in _platform(ss)]
    assert "platform:hub1_hub2" in labels
    assert sum(1 for x in labels if x.endswith("_arm")) == 4


def test_FL2a_an_UNKNOWN_node_name_is_refused_against_the_DECKs_own_list() -> None:
    """The deck is the authority for which hubs exist (DJ1).

    Building the rest without the unknown member would publish a frame the configuration
    did not describe, which is why this refuses rather than skipping.
    """
    with pytest.raises(ValueError) as caught:
        build_superstructure(platform_members=(("centre", "hub9"),))
    message = str(caught.value)
    assert "hub9" in message and "not a node of this deck" in message, message
    assert "hub1" in message, "the refusal does not name the nodes that DO exist"


# ---------------------------------------------------------------------------
# The schema's own refusals, through the real `load_config`
# ---------------------------------------------------------------------------


@pytest.fixture
def cfg_with(tmp_path: Path) -> Any:
    """The shipped example with a `topology` block, paths absolutised."""

    def make(topology: Any) -> Path:
        data = copy.deepcopy(yaml.safe_load(EXAMPLE.read_text(encoding="utf-8")))
        for block, key in (("floatsim", "deck"), ("load_cases", "npz"), ("outputs", "directory")):
            value = data.get(block, {}).get(key)
            if isinstance(value, str) and value.strip():
                data[block][key] = str((EXAMPLE.parent / value).resolve())
        if topology is not None:
            data["topology"] = topology
        path = tmp_path / "config.yaml"
        path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
        return path

    return make


@pytest.mark.parametrize(
    ("label", "topology", "needle"),
    [
        ("a self-loop", {"platform": {"members": [["hub1", "hub1"]]}}, "both ends are"),
        (
            "a duplicate pair, reversed",
            {"platform": {"members": [["centre", "hub1"], ["hub1", "centre"]]}},
            "already declared",
        ),
        ("an empty list", {"platform": {"members": []}}, "the list is EMPTY"),
        ("a named topology that is not star", {"platform": "ring"}, "not a topology"),
        (
            "a three-element member",
            {"platform": {"members": [["centre", "hub1", "hub2"]]}},
            "expected a [from, to] pair",
        ),
        (
            "an unquoted bool as a node name",
            {"platform": {"members": [[True, "hub1"]]}},
            "is not a string",
        ),
        ("an unknown key", {"platform": "star", "hubs": "star"}, "unrecognised field"),
        ("a scalar where a mapping belongs", 7, "expected a mapping"),
    ],
)
def test_FL2a_the_schema_refuses(cfg_with: Any, label: str, topology: Any, needle: str) -> None:
    """One case per way a declared topology can be wrong, refused by the schema.

    The bool case reuses `_require_string` from R834/R837 rather than adding a second
    rule for the same defect: a node name is a NAME, and `[no, hub1]` arrives as `False`.
    """
    with pytest.raises(ConfigError) as caught:
        load_config(cfg_with(topology))
    assert needle in str(caught.value), (label, str(caught.value))


@pytest.mark.parametrize(
    ("label", "topology"),
    [
        ("absent", None),
        ("platform: star", {"platform": "star"}),
        ("platform with no members key", {"platform": {}}),
        ("the star declared explicitly", {"platform": {"members": [list(p) for p in STAR]}}),
        (
            "a braced star",
            {"platform": {"members": [["hub1", "hub2"], *[list(p) for p in STAR]]}},
        ),
    ],
)
def test_FL2a_these_configurations_LOAD(cfg_with: Any, label: str, topology: Any) -> None:
    """The controls, so the refusals above are not refusing everything."""
    cfg = load_config(cfg_with(topology))
    declared = cfg.topology.members
    assert cfg.topology.is_star == (not declared), label


def test_FL2a_an_ABSENT_block_is_the_star_and_says_so(cfg_with: Any) -> None:
    """`is_star` is the schema's own word for "nothing declared, generate the star"."""
    cfg = load_config(cfg_with(None))
    assert cfg.topology.members == ()
    assert cfg.topology.is_star is True


# --------------------------------------------------------------------------
# R869: every hub the deck owns is reachable from the centre.
#
# THE EIGHT TOPOLOGIES ARE `docs/milestones/R1.md`'s FT2.7 TABLE, not a set invented here,
# and the two halves below are its two halves. #8 is already refused by the deck-name check
# (`test_FL2a_an_UNKNOWN_node_name_is_refused_against_the_DECKs_own_list`), so it is not
# repeated.
# --------------------------------------------------------------------------

BRACE = ("hub1", "hub2")
T1_ARMS_FIRST = (*STAR, BRACE)
T2_BRACE_FIRST = (BRACE, *STAR)
T3_REVERSED_ARM = (("hub1", "centre"), *STAR[1:])
T4_HUB4_VIA_BRACE = (*STAR[:3], ("hub3", "hub4"))
T5_RING = (("hub1", "hub2"), ("hub2", "hub3"), ("hub3", "hub4"), ("hub4", "hub1"))
T6_THREE_ARMS = STAR[:3]
T7_ONE_MEMBER = STAR[:1]


@pytest.mark.parametrize(
    ("label", "topology", "absent", "stranded"),
    [
        ("5 a ring with no centre member", T5_RING, [], ["hub1", "hub2", "hub3", "hub4"]),
        ("6 three arms only", T6_THREE_ARMS, ["hub4"], []),
        ("7 a single member", T7_ONE_MEMBER, ["hub2", "hub3", "hub4"], []),
    ],
)
def test_R869_a_hub_the_centre_cannot_reach_is_REFUSED(
    label: str,
    topology: Any,
    absent: list[str],
    stranded: list[str],
) -> None:
    """The refusal, with the hub names and WHICH KIND of failure each one is.

    **WHAT THIS CLOSES, AND IT IS NOT A CONNECTIVITY CHECK ON THE STRUCTURE.** All three
    of these built without complaint, and `rigid_links` then ties the body's whole
    remainder to a `centre` that is an endpoint of no member -- so the remainder's mass
    appears in the mass report and contributes no stiffness to the frame. The enumeration
    of all eight topologies with the command that measured each one is in the plan.

    **#6 AND #7 ARE WHY THE CHECK IS OVER THE DECK'S HUBS AND NOT THE MODEL'S NODES.**
    Neither has a disconnected node: the missing hub has no node in the frame at all, so a
    component walk over BUILT nodes finds nothing wrong and would accept a platform
    missing a quarter or three quarters of its support. Only #5 is disconnected in that
    sense, and the two are different mistakes -- a hub no member names is a topology that
    forgot it; a hub named but unreachable is a topology that is disconnected -- so the
    message says which, and this cell asserts which.
    """
    with pytest.raises(ValueError) as caught:
        build_superstructure(platform_members=topology)
    message = str(caught.value)
    assert "topology.platform.members leaves" in message, message
    for hub in absent + stranded:
        assert hub in message, (hub, message)
    if absent:
        assert f"{absent} appear in no declared member" in message, message
    else:
        assert "appear in no declared member" not in message, message
    if stranded:
        assert f"{stranded} are declared but not reachable" in message, message
    else:
        assert "not reachable" not in message, message
    # The reader is told what the deck DOES own, so the refusal is actionable.
    assert "The deck's hubs are ['hub1', 'hub2', 'hub3', 'hub4']" in message, message


@pytest.mark.parametrize(
    ("label", "topology", "members"),
    [
        ("the default star", STAR, 4),
        ("1 braced star, arms first", T1_ARMS_FIRST, 5),
        ("2 braced star, brace first", T2_BRACE_FIRST, 5),
        ("3 one arm written [hub1, centre]", T3_REVERSED_ARM, 4),
        ("4 hub4 reached only by a brace", T4_HUB4_VIA_BRACE, 4),
    ],
)
def test_R869_does_NOT_refuse_a_topology_that_reaches_every_hub(
    label: str, topology: Any, members: int
) -> None:
    """EH4's other direction: the injection rises until a CLEAN case trips.

    **#4 IS THE ONE THIS CELL EXISTS FOR.** hub4 is joined to hub3 by a brace and hub3 to
    the centre by its arm, so hub4 IS in the centre's component and the structure is
    connected. Verdict 42 ruled it RUN: its joint node is at distance 0.0 from the node
    #1 calls `platform:hub4_arm_tip`, and the support scheme uses only the node INDEX, so
    refusing it would refuse a structure the configuration declares and the solver can
    solve. A reachability check written one notch too wide catches it, and nothing else
    in this file would notice.

    **AND `platform_remainder` IS WHY THE CHECK IS NOT OVER "EVERY NODE IN THE MODEL".**
    It is rigid-linked rather than a member endpoint, so it is unreached in the healthy
    star too -- a check written that way would refuse the default, which is the first row
    here.
    """
    ss = build_superstructure(platform_members=topology)
    body = _body(ss)
    assert len(body.members) == members, [m.label for m in body.members]


# --------------------------------------------------------------------------
# R867: a node's NAME is the joint's, never the member's that reached it first.
# --------------------------------------------------------------------------

ALL_TIPS = tuple(f"platform:{h}_arm_tip" for h in HUBS)
R867_RUNS = (
    ("the default star", STAR),
    ("1 braced star, arms first", T1_ARMS_FIRST),
    ("2 braced star, brace first", T2_BRACE_FIRST),
    ("3 one arm written [hub1, centre]", T3_REVERSED_ARM),
    ("4 hub4 reached only by a brace", T4_HUB4_VIA_BRACE),
)


@pytest.mark.parametrize(("label", "topology"), R867_RUNS)
def test_R867_every_hub_JOINT_carries_its_OWN_name_whatever_the_order(
    label: str, topology: Any
) -> None:
    """All four tip names exist, and the MEMBER labels are untouched.

    **THE DEFECT WAS THAT A NODE'S NAME DEPENDED ON DECLARATION ORDER (R867).** `node()`
    deduplicates by coordinate and names on CREATION, and the two lines below it derived
    each end's name from the MEMBER -- `f"{label}_a"` / `f"{label}_tip"` -- so a brace
    declared before the arm sharing its hub took the node as `platform:hub1_hub2_a` and
    `platform:hub1_arm_tip` was never created, while `config.py`'s duplicate-member check
    keys on `frozenset((a, b))`, which is the schema stating that order does NOT identify
    a member. Three readers of the tip name then raised three layers downstream, in a
    `KeyError` rather than a refusal.

    **BOTH HALVES ARE ASSERTED, and the second is the one a renaming repair breaks.** The
    node names must be the joints' -- and the member LABELS must be exactly what they
    were, because those DO reach three published deliverables and step 1's gate names
    `platform:hub4_arm` ROOT. A repair that fixed the names and renamed a published row
    would pass a name check and fail this.
    """
    ss = build_superstructure(platform_members=topology)
    body = _body(ss)
    names = {n.name for n in body.model.nodes}
    assert set(ALL_TIPS) <= names, sorted(names)
    assert "platform_centre" in names, sorted(names)
    # No member-derived END name survives anywhere: `_a` was the other half of the old rule.
    assert not [n for n in names if n.endswith("_a")], sorted(names)
    # And the published member labels are the declared ones, unchanged by the renaming.
    labels = [m.label for m in body.members]
    assert all(lbl.startswith("platform:") for lbl in labels), labels
    assert len(set(labels)) == len(labels), labels


@pytest.mark.parametrize(("label", "topology"), R867_RUNS)
def test_R867_joint_nodes_of_resolves_to_the_SAME_nodes_on_ALL_of_them(
    label: str, topology: Any
) -> None:
    """Verdict 42's ruling 1, asserted through the reader rather than quoted.

    **THE SUPPORT SCHEME IS ALREADY TOPOLOGY-AGNOSTIC ONCE THE NAME IS THE JOINT'S.**
    `joint_nodes_of` looks up `f"platform:{hub}_arm_tip"` and then uses only the node
    INDEX -- `vertical_reactions_N[tip]` -- so a reaction is a property of the NODE and not
    of which member reached it. #4 is the row this matters for: hub4's joint node is at
    distance 0.0 from the node the star calls `platform:hub4_arm_tip`, measured at verdict
    42, which is why it RUNS rather than being refused or needing a topology-aware scheme.

    The four indices are asserted to be IDENTICAL across all five topologies, which is
    stronger than asserting the lookup succeeds: a repair that created the name on some
    other node would resolve and support the wrong point.
    """
    ss = build_superstructure(platform_members=topology)
    tips = joint_nodes_of(ss, _body(ss))
    assert len(tips) == 4, tips
    assert tips == (1, 2, 3, 4), tips
    by_index = {n_i: n.name for n_i, n in enumerate(_body(ss).model.nodes)}
    assert [by_index[i] for i in tips] == list(ALL_TIPS), [by_index[i] for i in tips]


def test_R867_the_PARAMETERISED_reader_is_UNCHANGED_on_the_tripods() -> None:
    """L60: three reader sites, TWO shapes, and the third generalises over bodies.

    `floatfea/post/forces_table.py` reads `f"{parent}:{child}_arm_tip"` rather than the
    fixed `platform:` of the two sites in `floatfea/solve/static.py`. **A repair keyed on
    the literal `platform:` would have changed two sites and left the third reading a name
    that no longer exists**, which is why R867's rule is applied to the PLATFORM's declared
    members only: a hub's tripod is three cluster arms to its own buoys, a count this
    builder refuses to vary, so no declaration order exists there to disagree with.

    This asserts the tripod names are the member-derived ones they have always been, at
    the shape that reader uses.
    """
    ss = build_superstructure(platform_members=T2_BRACE_FIRST)
    hub = next(b for b in ss.bodies if b.name == "hub1")
    names = {n.name for n in hub.model.nodes}
    tips = sorted(n for n in names if n.endswith("_arm_tip"))
    assert len(tips) == 3, sorted(names)
    for tip in tips:
        assert tip.startswith("hub1:"), tip
        # the exact shape the parameterised reader composes
        child = tip[len("hub1:") : -len("_arm_tip")]
        assert f"hub1:{child}_arm_tip" in names, (tip, sorted(names))


def test_R867_the_COINCIDENCE_rule_is_declared_and_its_boundary_is_BOTH_WAYS() -> None:
    """`NODE_COINCIDENCE_DECIMALS`, solved from both sides (EH4) rather than asserted.

    **WHY THIS CELL EXISTS.** `round(c, 9)` was an undeclared comparison epsilon on the
    production path, green under `tests/test_no_tolerance_literals.py` because that guard
    treats integers as counts. Verdict 42's L57 ruled it CZ0 (b) in shape and said it goes
    live the moment R867's repair touches the helper. R867 touches it AND deletes the
    adjacent exact comparison that was L57's reason the epsilon was harmless -- so the
    harmlessness is measured here instead of inherited.

    **THE RISING DIRECTION DOES NOTHING AND THE FALLING DIRECTION IS LOUD.** The default
    star's closest two nodes are 41.3 m apart, so no admissible value of this constant can
    merge them: the build is unchanged from d = 9 up and from d = 9 down to d = -1, which
    is ten decades of margin. At d = -2 -- 100 m buckets -- the centre and a hub do merge,
    and the failure is a REFUSAL from the element rather than a silently shorter frame.
    That is the loudness L57 relied on, and it is a property of the element and not of the
    naming rule that used to provide it.
    """
    from floatfea.model import platform as pf

    clean = {n.name for n in _body(build_superstructure(platform_members=STAR)).model.nodes}
    assert len(clean) == 6, sorted(clean)

    original = pf.NODE_COINCIDENCE_DECIMALS
    try:
        # RISING, and FALLING as far as it may fall with no effect.
        for decimals in (18, 12, 9, 0, -1):
            pf.NODE_COINCIDENCE_DECIMALS = decimals
            got = {n.name for n in _body(build_superstructure(platform_members=STAR)).model.nodes}
            assert got == clean, (decimals, sorted(got))
        # FALLING past the boundary: LOUD, and it names the state.
        pf.NODE_COINCIDENCE_DECIMALS = -2
        with pytest.raises(ValueError) as caught:
            build_superstructure(platform_members=STAR)
        assert "node 0 to itself" in str(caught.value), str(caught.value)
    finally:
        pf.NODE_COINCIDENCE_DECIMALS = original
        assert pf.NODE_COINCIDENCE_DECIMALS == NODE_COINCIDENCE_DECIMALS
