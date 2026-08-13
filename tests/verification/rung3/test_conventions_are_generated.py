"""`docs/conventions.md`'s frame section must match what `frames.py` renders.

Gate **G0.2**. The machine-readable definitions are the **single source**; the
prose is generated from them. This test is what makes that true rather than
aspirational.

Note what it is *not*. It is not two artifacts held together by a comparison —
that arrangement works until someone edits the prose and updates the test to
match, at which point the test certifies the drift it was meant to catch. Here
there is one place a value can be stated, and the document is a rendering of it.
Editing the prose fails this test with a diff and a pointer to the source.
"""

from __future__ import annotations

import re
from pathlib import Path

from floatfea.io.frames import (
    GRAVITY_MAGNITUDE,
    N_DOF_FREE,
    N_DOF_HYDRO,
    N_DOF_TOTAL,
    ROTATION_BY_PRODUCER,
    buoy_body_index,
    render_markdown,
)

_CONVENTIONS = Path(__file__).resolve().parents[3] / "docs" / "conventions.md"
_BEGIN = "<!-- GENERATED FROM floatfea/io/frames.py -- DO NOT EDIT BY HAND -->"
_END = "<!-- END GENERATED -->"


def _embedded_block() -> str:
    text = _CONVENTIONS.read_text(encoding="utf-8")
    match = re.search(re.escape(_BEGIN) + r".*?" + re.escape(_END), text, re.DOTALL)
    assert match is not None, (
        "docs/conventions.md has no generated frame block. It must contain the "
        f"section delimited by\n  {_BEGIN}\n  {_END}\n"
        "Regenerate it from floatfea.io.frames.render_markdown()."
    )
    return match.group(0)


def test_conventions_document_matches_the_source() -> None:
    """The committed prose is exactly what the source renders."""
    rendered = render_markdown()
    embedded = _embedded_block()
    assert embedded == rendered, (
        "docs/conventions.md's frame section has diverged from "
        "floatfea/io/frames.py.\n\n"
        "The MODULE is the source. Edit it and regenerate; do not edit the "
        "document.\n\n--- committed ---\n"
        f"{embedded}\n\n--- rendered ---\n{rendered}"
    )


def test_gravity_is_floatsim_not_standard() -> None:
    """9.81, not 9.80665.

    Small as physics and not small as a discrepancy: a mismatch appears
    downstream as an unexplained mass error and gets hunted in the wrong place.
    """
    assert GRAVITY_MAGNITUDE == 9.81
    assert GRAVITY_MAGNITUDE != 9.80665


def test_the_dof_arithmetic_closes() -> None:
    """102 total, 64 constrained, 38 free — the figure PLAN.md §1 quotes."""
    assert N_DOF_TOTAL == 102
    assert N_DOF_HYDRO == 72
    assert N_DOF_FREE == 38
    assert N_DOF_TOTAL - 16 * 4 == N_DOF_FREE


def test_hydro_dof_is_a_strict_subset_of_the_state_vector() -> None:
    """72 of 102. Summing radiation over 102 would index past the BEM data."""
    assert N_DOF_HYDRO < N_DOF_TOTAL


def test_body_index_follows_the_deck_ordering() -> None:
    """Clusters occupy four slots as [3 buoys, 1 hub], so buoy k is at 4c + b."""
    assert buoy_body_index(0) == 0
    assert buoy_body_index(2) == 2
    assert buoy_body_index(3) == 4   # first buoy of cluster 1, after hub 0
    assert buoy_body_index(11) == 14


def test_every_producer_declares_a_rotation_parameterisation() -> None:
    """FloatSim reads xi[3:6] three ways; no producer may be left implicit."""
    assert ROTATION_BY_PRODUCER
    assert set(ROTATION_BY_PRODUCER.values()) <= {
        "zyx_intrinsic_euler",
        "rotation_vector",
        "linearised",
    }
    # The two that matter most, and that differ from each other.
    assert ROTATION_BY_PRODUCER["strips"] == "zyx_intrinsic_euler"
    assert ROTATION_BY_PRODUCER["joints"] == "rotation_vector"
