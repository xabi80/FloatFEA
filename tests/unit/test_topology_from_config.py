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
