"""V3.2 / G3.2: the model definition round-trips through YAML without loss.

DV0 re-locked F3's layout source to a GENERATED YAML, `data/platform/platform12_deck.yaml`,
written only by `scripts/export_platform_deck.py`.

WHY THERE IS NO `skipif` IN THIS MODULE. The strongest statement about this file is
that it still reproduces a deck built from HSP. That comparison needs `../HSP-runs`,
which exists on the implementer's machine and not in CI — so the first version marked
it `skipif` and the gate silently did not run where a gate is most needed.
`CLAUDE.md` names `skip` in the same sentence as `xfail`.

SO THE GATE IS SPLIT BY WHAT CAN BE ASSERTED WHERE, and neither half is conditional:

* **Here, always** — the committed file matches a committed digest of its content AND
  its order, its header agrees with what it contains, every coordinate is finite, and
  the four arms are on the axes.
* **In the generator** — `python scripts/export_platform_deck.py --check` rebuilds the
  deck from HSP at the pin and compares. It needs a second repository at a specific
  tag, which is not a thing a unit test can require, so it is a procedure with a
  command and its output goes in the step report as a triple.

AND THE FIRST VERSION OF THIS HALF CERTIFIED NOTHING (R583). It carried the gate id
on a parse-and-re-emit comparison: parse the file, re-emit, re-parse, compare.
That is green on ANY file that parses. The reviewer measured it
green on 11 of 11 injected mutations — a buoy moved to 99.0, every mass times ten, a
`.nan` coordinate, the header falsified, a file parsing to `None`, and the document
re-emitted with `sort_keys=True`, which is the case its own docstring claimed. The
split was right and the label went on the one assertion that said nothing;
`test_the_file_PARSES_and_re_emits_stably` keeps that assertion under a name
that describes what it actually checks, and the digests carry the gate.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import pytest

from floatfea.tolerances import ROUNDOFF_IDENTITY

yaml = pytest.importorskip("yaml")

ROOT = Path(__file__).resolve().parents[3]
DECK_YAML = ROOT / "data" / "platform" / "platform12_deck.yaml"
DIGEST = ROOT / "tests" / "goldens" / "platform_deck_digest.txt"

BODIES = 17
JOINTS = 16
JOINT_ROWS = 4
"""not-a-tolerance: the platform's own topology, from
`../HSP-runs/docs/platform-geometry.md:65-67` — 12 buoys, 4 cluster hubs, 1 platform
cross; 16 identical `yaw_locked` joints at 4 constraint rows each. Counts of objects,
not thresholds on a measurement."""


def _split(text: str) -> tuple[str, str]:
    """Header comment block, then the document body.

    ANCHORED ON THE COMMENT BLOCK, not on a key name. The first version anchored on
    `text.index("bodies:")`, and the document's first top-level key is `simulation:`
    -- so it silently cut the header AND the simulation block, and then compared a
    truncated body against a full canonical dump. A structural anchor that happens
    to match a key in the middle of a file is not an anchor.
    """
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines) and (lines[i].startswith("#") or not lines[i].strip()):
        i += 1
    return "".join(lines[:i]), "".join(lines[i:])


def _text() -> str:
    assert DECK_YAML.is_file(), (
        f"{DECK_YAML.relative_to(ROOT)} is missing. Generate it with "
        "`python scripts/export_platform_deck.py`; F3's layout has no other source."
    )
    return DECK_YAML.read_text(encoding="utf-8")


def _loaded() -> dict:
    raw = yaml.safe_load(_text())
    assert isinstance(raw, dict), (
        f"{DECK_YAML.relative_to(ROOT)} does not parse to a mapping (got "
        f"{type(raw).__name__}). Every check below would be vacuous on that."
    )
    return raw


def _golden() -> dict[str, str]:
    assert DIGEST.is_file(), (
        f"{DIGEST.relative_to(ROOT)} is missing. It is written by "
        "`python scripts/export_platform_deck.py`, and without it the deck's "
        "content is unguarded."
    )
    out = {}
    for line in DIGEST.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        out[key.strip()] = value.strip()
    return out


def content_sha(raw: dict) -> str:
    """The canonical hash the digest records. Blind to order, by construction."""
    return hashlib.sha256(
        json.dumps(raw, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def order_of(raw: dict) -> tuple[str, str]:
    """The sequences as the FILE carries them. This is what the hash cannot see."""
    return (
        ",".join(b["name"] for b in raw["bodies"]),
        ",".join(f"{j['body_a']}>{j['body_b']}" for j in raw["joints"]),
    )


def test_G3_2_the_committed_deck_matches_its_CONTENT_digest() -> None:
    """Any changed value reddens: a coordinate, a mass, an inertia, a `.nan`.

    A golden under `CLAUDE.md` § Testing. If this fails, the deck moved, and moving
    it requires a written explanation of why — regenerating the digest to match new
    output without one is the same error as widening a tolerance.
    """
    raw = _loaded()
    golden = _golden()
    assert content_sha(raw) == golden["content_sha256"], (
        "the committed deck's content no longer hashes to the recorded digest. "
        "Some value in it changed: a coordinate, a mass, an inertia tensor. "
        "Regenerate with scripts/export_platform_deck.py and say in the commit "
        "why the deck moved."
    )
    assert (
        str(len(json.dumps(raw, sort_keys=True, separators=(",", ":"))))
        == golden["canonical_bytes"]
    )


def test_G3_2_the_committed_deck_matches_its_ORDER_digest() -> None:
    """Reordering reddens, which the content hash cannot see.

    `sort_keys=True` on re-emission leaves every value identical and changes the
    document. The first version of this gate passed on exactly that.
    """
    bodies, joints = order_of(_loaded())
    golden = _golden()
    assert bodies == golden["body_order"], "the body order in the file changed"
    assert joints == golden["joint_order"], "the joint order in the file changed"


def test_the_HEADER_agrees_with_what_the_file_CONTAINS() -> None:
    """A falsified header reddens. It is provenance, so it is not decoration.

    The header states the body and joint counts; if it can disagree with the
    document beneath it, a reader who trusts it is misled about the model.
    """
    from floatfea import hsp_pin

    text, raw = _text(), _loaded()
    assert "DO NOT HAND-EDIT" in text
    assert hsp_pin.HSP_TAG in text, "the file does not name the HSP tag it came from"
    assert hsp_pin.HSP_COMMIT in text, "the file does not name the HSP commit"
    assert "MODEL scale" in text, "the file does not declare its scale"
    for label, count in (("bodies", len(raw["bodies"])), ("joints", len(raw["joints"]))):
        assert f"#   {label}         {count}\n" in text, (
            f"the header does not state {label} = {count}, which is what the "
            f"document actually contains. A header that can disagree with its own "
            f"file is provenance nobody can rely on."
        )


def test_every_COORDINATE_in_the_deck_is_FINITE() -> None:
    """A `.nan` anywhere reddens here with a message naming where.

    The digest already catches it, but as an opaque hash mismatch. A structural
    model with a nan coordinate assembles a stiffness matrix of nans and the solve
    fails far from the cause.
    """
    raw = _loaded()
    bad: list[str] = []

    def walk(node: object, path: str) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{path}/{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")
        elif isinstance(node, float) and not math.isfinite(node):
            bad.append(f"{path} = {node}")

    walk(raw, "")
    assert not bad, f"non-finite values in the deck: {bad}"


def test_the_deck_YAML_has_the_platforms_OWN_topology() -> None:
    """17 bodies and 16 joints, every joint `yaw_locked`, every one 4 rows."""
    raw = _loaded()
    assert len(raw["bodies"]) == BODIES
    assert len(raw["joints"]) == JOINTS
    kinds = {j["type"] for j in raw["joints"]}
    assert kinds == {"yaw_locked"}, f"expected 16 identical yaw_locked joints; got {kinds}"


def test_the_file_PARSES_and_re_emits_stably() -> None:
    """A parse-and-re-emit cycle returns the same structure.

    **This is the assertion R583 found vacuous, under a name that says what it
    does.** It is green on any file that parses, so it does not carry the gate id.
    It is kept because a file that is NOT stable under a parse-and-re-emit cycle is
    worth knowing about, and deleting it would lose that for nothing.
    """
    raw = _loaded()
    assert yaml.safe_load(yaml.safe_dump(raw, sort_keys=False)) == raw


def test_G3_2_the_file_matches_its_RECORDED_BYTE_digest() -> None:
    """The file as emitted, hashed. This is what catches REORDERING.

    A YAML mapping is unordered, so re-emitting with `sort_keys=True` leaves the
    CONTENT identical — every value the same, the same canonical hash, the same list
    order — while changing the document. The reviewer counted that among the eleven
    mutations the old gate missed, and it is right to count it: the file is
    generated, and a generated file not in its generator's form was written by
    something else.

    **TWO EARLIER ATTEMPTS AT THIS COULD NOT SEE IT, and the reason is worth the
    space.** The content hash is order-blind by construction. And a test that
    re-emits the file's own parsed content and compares is self-referential:
    `safe_load` hands the keys back in the order the file listed them, so the
    comparison reproduces whatever the file says, sorted or not. **A recorded hash
    is the only side of the comparison the file cannot supply itself**, which is the
    same reason `--check` against HSP is the strongest half of this gate.
    """
    # the BODY, not the whole file: the header carries a date and would make this
    # digest change on a re-export that altered nothing about the model.
    _, body = _split(_text())
    assert hashlib.sha256(body.encode()).hexdigest() == _golden()["body_sha256"], (
        "the deck YAML's bytes do not match the recorded digest. If the content "
        "digest still matches, then no VALUE changed and only the file's form did -- "
        "a re-emission with different settings, or a hand-edit that round-trips. "
        "The generator is the only sanctioned writer."
    )


def test_the_arms_are_AXIAL_which_is_what_R576_turned_on() -> None:
    """The four cluster hubs lie on ±x and ±y, not on the diagonals.

    DJ1 said "two diagonal arms" until DV1 withdrew it, and the sentence had already
    produced a false claim about which wave heading governs. Asserted here because a
    sentence in a plan is checked by nothing.

    The comparison is RELATIVE, against the arm's own radius: the hub positions come
    from `cos` and `sin` of multiples of pi/2, so the off-axis coordinate is a
    round-off residue and not an exact zero — `cos(pi/2)` is 6.1e-17.
    """
    by_name = {b["name"]: b for b in _loaded()["bodies"]}
    radii = []
    for i in range(1, 5):
        x, y, _z = by_name[f"hub{i}"]["reference_point"]
        radius = math.hypot(x, y)
        radii.append(radius)
        off_axis = min(abs(x), abs(y)) / radius
        assert off_axis <= ROUNDOFF_IDENTITY, (
            f"hub{i} sits at ({x}, {y}); its smaller coordinate is {off_axis:.3e} of "
            "the arm radius, so it is off-axis by more than round-off. A hub "
            "genuinely off both axes would mean the diagonal layout DJ1 described, "
            "which the deck does not have."
        )
    spread = (max(radii) - min(radii)) / max(radii)
    assert spread <= ROUNDOFF_IDENTITY, f"the four hub arms are not equal length: {radii}"


def test_the_JOINT_POINTS_are_COPLANAR_which_the_planar_frame_rests_on() -> None:
    """All 16 joints at one elevation, which is why DW1's frame is planar.

    If this ever fails, the superstructure is not a planar frame and F3 §3's work
    list is describing a structure the deck does not have. It is the single
    measurement DW1's ruling turns on, so it is a test and not a paragraph.
    """
    raw = _loaded()
    ref = {b["name"]: b["reference_point"] for b in raw["bodies"]}
    zs = []
    for j in raw["joints"]:
        a = [ref[j["body_a"]][k] + j["attach_a_body"][k] for k in range(3)]
        b = [ref[j["body_b"]][k] + j["attach_b_body"][k] for k in range(3)]
        assert math.dist(a, b) <= ROUNDOFF_IDENTITY * max(
            1.0, math.dist(a, [0, 0, 0])
        ), f"joint {j['body_a']}-{j['body_b']}'s two attach points do not coincide"
        zs.append(a[2])
    spread = max(zs) - min(zs)
    assert spread <= ROUNDOFF_IDENTITY * max(abs(z) for z in zs), (
        f"the 16 joint points span {spread:.3e} m in z and are not coplanar. The "
        "planar frame DW1 rules for does not describe this deck."
    )


# ---------------------------------------------------------------------------
# THE COUNTER. A gate carries its own failure or it is not a gate.
# ---------------------------------------------------------------------------

MUTATIONS: dict[str, object] = {
    "a_buoy_moved_to_99": ("move", None),
    "every_mass_times_ten": ("mass", None),
    "a_nan_coordinate": ("nan", None),
    "header_says_bodies_99": ("header", None),
    "the_file_parses_to_None": ("none", None),
    "re_emitted_with_sort_keys_True": ("sort", None),
    "a_joint_retyped_to_hinge": ("hinge", None),
    "a_body_dropped": ("drop_body", None),
    "a_joint_dropped": ("drop_joint", None),
    "two_bodies_swapped_in_order": ("swap", None),
    "a_hub_moved_onto_the_diagonal": ("diagonal", None),
    "one_joint_lifted_off_the_plane": ("unplanar", None),
}
"""The reviewer's eleven, plus the coplanarity case DW1's ruling rests on.

Every one of these was GREEN against the gate as first written."""


def _mutate(kind: str, text: str) -> str:
    raw = yaml.safe_load(text)
    if kind == "move":
        raw["bodies"][0]["reference_point"][0] = 99.0
    elif kind == "mass":
        for b in raw["bodies"]:
            b["mass"] = float(b["mass"]) * 10.0
    elif kind == "nan":
        raw["bodies"][0]["reference_point"][2] = float("nan")
    elif kind == "header":
        return text.replace("#   bodies         17", "#   bodies         99", 1)
    elif kind == "none":
        return "# only a comment\n"
    elif kind == "sort":
        return _split(text)[0] + yaml.safe_dump(raw, sort_keys=True)
    elif kind == "hinge":
        raw["joints"][0]["type"] = "hinge"
    elif kind == "drop_body":
        raw["bodies"].pop()
    elif kind == "drop_joint":
        raw["joints"].pop()
    elif kind == "swap":
        raw["bodies"][0], raw["bodies"][1] = raw["bodies"][1], raw["bodies"][0]
    elif kind == "diagonal":
        hub = next(b for b in raw["bodies"] if b["name"] == "hub1")
        r = math.hypot(*hub["reference_point"][:2])
        hub["reference_point"][0] = hub["reference_point"][1] = r / math.sqrt(2.0)
    elif kind == "unplanar":
        raw["joints"][0]["attach_a_body"][2] += 0.05
    else:  # pragma: no cover - the table and this dispatch are one unit
        raise AssertionError(f"no mutation named {kind!r}")
    return _split(text)[0] + yaml.safe_dump(raw, sort_keys=False, default_flow_style=False)


@pytest.mark.parametrize("name", sorted(MUTATIONS))
def test_a_MUTATED_deck_reddens_at_least_one_assertion(name: str, monkeypatch, tmp_path) -> None:
    """Each mutation must fail at least one check in this module.

    R583's finding was a gate green on 11 of 11 of these. The counter is
    parametrised so a mutation that stops being caught names itself, rather than
    being absorbed into a count.
    """
    kind = MUTATIONS[name][0]  # type: ignore[index]
    mutated = tmp_path / "platform12_deck.yaml"
    mutated.write_text(_mutate(kind, _text()), encoding="utf-8")

    checks = [
        test_G3_2_the_committed_deck_matches_its_CONTENT_digest,
        test_G3_2_the_committed_deck_matches_its_ORDER_digest,
        test_the_HEADER_agrees_with_what_the_file_CONTAINS,
        test_every_COORDINATE_in_the_deck_is_FINITE,
        test_the_deck_YAML_has_the_platforms_OWN_topology,
        test_the_arms_are_AXIAL_which_is_what_R576_turned_on,
        test_the_JOINT_POINTS_are_COPLANAR_which_the_planar_frame_rests_on,
        test_G3_2_the_file_matches_its_RECORDED_BYTE_digest,
    ]
    import sys

    # Point this module's own reader at the mutated copy. The checks are the SHIPPED
    # functions, called directly, so the counter measures the gate rather than a
    # re-implementation of it.
    monkeypatch.setattr(sys.modules[__name__], "DECK_YAML", mutated)

    caught = []
    for check in checks:
        try:
            check()
        except (AssertionError, KeyError, TypeError, ValueError):
            caught.append(check.__name__)

    assert caught, (
        f"the mutation {name!r} was not caught by ANY assertion in this module. "
        "That is R583's defect exactly: a gate that cannot see a wrong deck."
    )
