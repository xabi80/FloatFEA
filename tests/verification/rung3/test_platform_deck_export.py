"""V3.2 / G3.2: the model definition round-trips through YAML without loss.

DV0 re-locked F3's layout source to a GENERATED YAML, `data/platform/platform12_deck.yaml`,
written only by `scripts/export_platform_deck.py`. Two things have to be true of it
and neither is true by construction:

1. **It re-validates to its source.** A YAML that does not reproduce the deck it
   was dumped from is a lossy copy, not a model definition. This is G3.2.
2. **It still matches the deck.** A generated file is only stronger than a
   hand-written one while something re-generates and compares it. Nothing does that
   on its own, so this module does.

WHY THE COMPARISON IS AGAINST THE SHIPPED FILE AND NOT AGAINST A FRESH DUMP ALONE.
A test that dumps the deck twice and compares the two dumps passes whatever the
committed file says, which is the failure mode of every golden that regenerates
itself. The committed bytes are one side of the comparison.
"""

from __future__ import annotations

from pathlib import Path

import pytest

yaml = pytest.importorskip("yaml")

ROOT = Path(__file__).resolve().parents[3]
DECK_YAML = ROOT / "data" / "platform" / "platform12_deck.yaml"
HSP_RUNS = ROOT.parent / "HSP-runs"

BODIES = 17
JOINTS = 16
"""not-a-tolerance: the platform's own topology, from
`../HSP-runs/docs/platform-geometry.md:65-67` -- 12 buoys, 4 cluster hubs, 1
platform cross; 16 identical `yaw_locked` joints. These are counts of objects, not
thresholds on a measurement, and a deck that disagrees is a different platform."""


def _loaded() -> dict:
    assert DECK_YAML.is_file(), (
        f"{DECK_YAML.relative_to(ROOT)} is missing. Generate it with "
        "`python scripts/export_platform_deck.py`; F3's layout has no other source."
    )
    return yaml.safe_load(DECK_YAML.read_text(encoding="utf-8"))


def test_the_exported_deck_exists_and_declares_its_provenance() -> None:
    """The file says which HSP it came from, on its face.

    A model definition whose provenance is in a commit message is a model
    definition nobody can trace from the file they are reading.
    """
    from floatfea import hsp_pin

    text = DECK_YAML.read_text(encoding="utf-8")
    assert "DO NOT HAND-EDIT" in text
    assert hsp_pin.HSP_TAG in text, "the file does not name the HSP tag it came from"
    assert hsp_pin.HSP_COMMIT in text, "the file does not name the HSP commit"
    assert "MODEL scale" in text, (
        "the file does not declare its scale. Every coordinate in it is model "
        "scale, and a layout read as metres would be wrong by a factor of 50."
    )


def test_the_deck_YAML_has_the_platforms_OWN_topology() -> None:
    """17 bodies and 16 joints, every joint `yaw_locked` at 4 rows."""
    raw = _loaded()
    assert len(raw["bodies"]) == BODIES
    assert len(raw["joints"]) == JOINTS
    kinds = {j["type"] for j in raw["joints"]}
    assert kinds == {"yaw_locked"}, f"expected 16 identical yaw_locked joints; got {kinds}"


def test_the_arms_are_AXIAL_which_is_what_R576_turned_on() -> None:
    """The four cluster hubs lie on +/-x and +/-y, not on the diagonals.

    DJ1 said "two diagonal arms" until DV1 withdrew it, and the sentence had
    already produced a false claim about which wave heading governs. It is asserted
    here rather than left in prose, because a sentence in a plan is not checked by
    anything and this is.
    """
    raw = _loaded()
    by_name = {b["name"]: b for b in raw["bodies"]}
    hubs = [by_name[f"hub{i}"]["reference_point"] for i in range(1, 5)]
    for x, y, _z in hubs:
        on_axis = (abs(x) < 1e-12) != (abs(y) < 1e-12)
        assert on_axis, (
            f"hub at ({x}, {y}) is on neither axis. The arms run along +/-x and "
            "+/-y; a hub off both axes would mean the diagonal layout DJ1 "
            "described, which the deck does not have."
        )
    radii = sorted(round((x**2 + y**2) ** 0.5, 9) for x, y, _z in hubs)
    assert radii[0] == radii[-1], f"the four hub arms are not equal length: {radii}"


@pytest.mark.skipif(not HSP_RUNS.is_dir(), reason="the HSP runs worktree is absent")
def test_G3_2_the_shipped_YAML_still_REPRODUCES_the_deck() -> None:
    """The gate. The committed bytes against a deck built from HSP right now.

    This is the half a self-regenerating golden cannot do: if the study changes
    under the pin, or if someone hand-edits the YAML, the two sides stop agreeing.
    """
    import subprocess
    import sys

    out = subprocess.run(
        [sys.executable, "scripts/export_platform_deck.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert out.returncode == 0, (
        "the shipped deck YAML no longer reproduces the deck HSP builds:\n"
        f"{out.stdout}\n{out.stderr}"
    )
    assert "round trip: re-validated dump equals the source dump" in out.stdout, (
        "the generator did not report its round-trip check, so this test would "
        "pass on a run that never performed it."
    )
