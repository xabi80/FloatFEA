"""V3.2 / G3.2: the model definition round-trips through YAML without loss.

DV0 re-locked F3's layout source to a GENERATED YAML, `data/platform/platform12_deck.yaml`,
written only by `scripts/export_platform_deck.py`.

WHY THERE IS NO `skipif` IN THIS MODULE, AND THE FIRST VERSION HAD ONE.
The strongest statement about this file is that it still reproduces a deck built
from HSP. That comparison needs `../HSP-runs`, which exists on the implementer's
machine and does not exist in CI — so the first version of this module marked it
`skipif` and the gate silently did not run in the one place a gate most needs to.
`CLAUDE.md` names `skip` in the same sentence as `xfail`, and a conditional skip on
the half that carries the gate is that sentence's shape even when the condition is
honest.

SO THE GATE IS SPLIT BY WHAT CAN BE ASSERTED WHERE, and neither half is conditional:

* **Here, always, everywhere** — the committed YAML parses, re-serialises and
  re-parses to an equal structure, and carries the platform's own topology, its
  provenance and its scale. This is a property of the file, and the file is in the
  repository, so nothing about the environment can excuse not checking it.
* **In the generator, by the implementer** — `python scripts/export_platform_deck.py
  --check` rebuilds the deck from HSP at the pin and compares. It needs a second
  repository at a specific tag, which is not a thing a unit test can require, so it
  is a procedure with a command and its output goes in the step report as a triple.

Calling that second half a test and letting it skip would have read, in every CI
summary, as a gate that passed.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from floatfea.tolerances import ROUNDOFF_IDENTITY

yaml = pytest.importorskip("yaml")

ROOT = Path(__file__).resolve().parents[3]
DECK_YAML = ROOT / "data" / "platform" / "platform12_deck.yaml"

BODIES = 17
JOINTS = 16
JOINT_ROWS = 4
"""not-a-tolerance: the platform's own topology, from
`../HSP-runs/docs/platform-geometry.md:65-67` — 12 buoys, 4 cluster hubs, 1 platform
cross; 16 identical `yaw_locked` joints at 4 constraint rows each. These are counts
of objects, not thresholds on a measurement, and a deck that disagrees is a
different platform."""


def _loaded() -> dict:
    assert DECK_YAML.is_file(), (
        f"{DECK_YAML.relative_to(ROOT)} is missing. Generate it with "
        "`python scripts/export_platform_deck.py`; F3's layout has no other source."
    )
    return yaml.safe_load(DECK_YAML.read_text(encoding="utf-8"))


def test_the_exported_deck_declares_its_provenance_and_its_scale() -> None:
    """The file says which HSP it came from and what scale it is in, on its face.

    A model definition whose provenance is in a commit message is a model
    definition nobody can trace from the file they are reading. The scale matters
    more: every coordinate here is model scale, and a layout read as metres is
    wrong by a factor of fifty in length and a hundred and twenty-five thousand in
    force.
    """
    from floatfea import hsp_pin

    text = DECK_YAML.read_text(encoding="utf-8")
    assert "DO NOT HAND-EDIT" in text
    assert hsp_pin.HSP_TAG in text, "the file does not name the HSP tag it came from"
    assert hsp_pin.HSP_COMMIT in text, "the file does not name the HSP commit"
    assert "MODEL scale" in text, "the file does not declare its scale"


def test_G3_2_the_committed_YAML_ROUND_TRIPS_without_loss() -> None:
    """The gate's environment-independent half. YAML out, parsed, re-emitted, equal.

    This is weaker than `Deck.model_validate`, which is the generator's check, and
    it is what can be asserted without a second repository: nothing in the file is
    lost or reordered by a parse-and-re-emit cycle, so the file is a faithful
    serialisation of the structure it represents rather than something a parser
    silently normalises.
    """
    raw = _loaded()
    again = yaml.safe_load(yaml.safe_dump(raw, sort_keys=False))
    assert again == raw, (
        "the committed deck YAML does not survive a parse-and-re-emit cycle, so it "
        "is not a lossless serialisation of the model definition."
    )


def test_the_deck_YAML_has_the_platforms_OWN_topology() -> None:
    """17 bodies and 16 joints, every joint `yaw_locked`, every one 4 rows."""
    raw = _loaded()
    assert len(raw["bodies"]) == BODIES
    assert len(raw["joints"]) == JOINTS
    kinds = {j["type"] for j in raw["joints"]}
    assert kinds == {"yaw_locked"}, f"expected 16 identical yaw_locked joints; got {kinds}"
    assert BODIES * 6 - JOINTS * JOINT_ROWS == 38, (
        "the free-DOF arithmetic in docs/platform-geometry.md no longer follows "
        "from the counts this module asserts"
    )


def test_the_arms_are_AXIAL_which_is_what_R576_turned_on() -> None:
    """The four cluster hubs lie on ±x and ±y, not on the diagonals.

    DJ1 said "two diagonal arms" until DV1 withdrew it, and the sentence had
    already produced a false claim about which wave heading governs. It is asserted
    here rather than left in prose, because a sentence in a plan is checked by
    nothing and this is.

    The comparison is RELATIVE, against the arm's own radius. The hub positions come
    from `cos` and `sin` of multiples of pi/2, so the off-axis coordinate is a
    round-off residue rather than an exact zero -- `cos(pi/2)` is 6.1e-17, not 0.
    `ROUNDOFF_IDENTITY` is the declared entry for a dimensionless relative agreement
    on a quantity exact in exact arithmetic, which is what this is.
    """
    raw = _loaded()
    by_name = {b["name"]: b for b in raw["bodies"]}
    radii = []
    for i in range(1, 5):
        x, y, _z = by_name[f"hub{i}"]["reference_point"]
        radius = (x**2 + y**2) ** 0.5
        radii.append(radius)
        off_axis = min(abs(x), abs(y)) / radius
        assert off_axis <= ROUNDOFF_IDENTITY, (
            f"hub{i} sits at ({x}, {y}); its smaller coordinate is {off_axis:.3e} of "
            "the arm radius, so it is off-axis by more than round-off. The arms run "
            "along +/-x and +/-y; a hub genuinely off both axes would mean the "
            "diagonal layout DJ1 described, which the deck does not have."
        )
    spread = (max(radii) - min(radii)) / max(radii)
    assert spread <= ROUNDOFF_IDENTITY, f"the four hub arms are not equal length: {radii}"
