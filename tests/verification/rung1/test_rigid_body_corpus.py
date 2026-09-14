"""G2.1's two quantities over the reviewer's frames, not just the shipped one (Q7).

`tests/corpus/g21_rigid_body_frames.txt` is the reviewer's file. It was written
at the twenty-sixth verdict and its own header says why: the shipped gate poses
ONE frame -- one section, one mesh, one unit system -- and both controls, both
counters and both published figures were measured at that single configuration
by the hand that chose it.

**Nothing read it for eighteen rounds.** This does.

WHAT IT FOUND, and it is the reason Q7 changed the gate rather than widening a
ceiling. Frames in this file exceed one or both of the two retired ceilings
with a DEFECT-FREE element, and the corpus's own `expect` field marks more of
them than either measure finds today. HOW MANY IS NOT WRITTEN HERE: a count in
a docstring is a figure nothing regenerates, and three findings this milestone
were exactly that. `test_the_RETIRED_ratio_is_why_the_form_changed` below
prints it at the commit it runs at, and the step report publishes it.

The corpus is explicit that this is a statement about conditioning: bracing
sections, mesh subdivision, span, and above all the length unit. The same
physical structure re-expressed in centimetres breaches a ceiling it passes in
metres, and an element does not know what unit anybody wrote its coordinates
in.

THE RESIDUAL FORM AND THE SPECTRAL GAP HOLD AT EVERY ONE. That is the claim
this file makes, and it is the claim Q7 rests on: G2.1 is a statement about the
element and the transformation, so its measure has to be one too.

THE `expect` FIELD IN THE CORPUS IS ABOUT THE RETIRED QUANTITIES and is read
here only to report the contrast. It is not an expectation on the new form, and
the new form is asserted on every entry whatever that field says.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from test_rigid_body_modes import (  # noqa: E402
    RIGID,
    mode_ratio,
    residual_exactness,
    zero_modes_by_gap,
)

from floatfea import basis  # noqa: E402
from floatfea.assemble.system import BeamElement, assemble_dense  # noqa: E402
from floatfea.model.material import Material, Section  # noqa: E402
from floatfea.model.nodes import Model, Node  # noqa: E402
from floatfea.tolerances import RIGID_MODE_EXACTNESS, RIGID_MODE_GAP  # noqa: E402

CORPUS = ROOT / "tests" / "corpus" / "g21_rigid_body_frames.txt"

# The frame the shipped gate poses, from `_frame()`. The corpus varies the
# section, the subdivision, the unit and the span around THIS geometry, and its
# `tip` field replaces the last node.
BASE = (
    (0.0, 0.0, 0.0),
    (4.0, 0.0, 0.0),
    (1.7, 3.3, 0.0),
    (1.9, 1.1, 2.8),
)
CONN = ((0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (2, 3), (3, 4))


def _entries() -> list[dict[str, str]]:
    out = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if line.startswith("id="):
            out.append(dict(f.split("=", 1) for f in line.split()))
    return out


ENTRIES = _entries()


def _build(entry: dict[str, str]) -> tuple[Model, list[BeamElement]]:
    """The frame one corpus line describes.

    `unit` is a RE-EXPRESSION and not a new structure: coordinates and section
    scale with it and `E` scales with its inverse square, which is what the
    corpus header says it verified to a relative residual of 9.7e-16. `stretch`
    is a longer frame at the same section, which is a different structure.
    """
    diameter, thickness = (float(x.split("=")[1]) for x in entry["section"].split(",")[1:])
    unit = float(entry["unit"])
    stretch = float(entry["stretch"])
    tip = tuple(float(v) for v in entry["tip"].split(","))
    subdiv = int(entry["subdiv"])

    coords = [tuple(c * stretch * unit for c in p) for p in BASE]
    coords.append(tuple(c * stretch * unit for c in tip))
    section = Section.circular_tube(diameter * unit, thickness * unit)
    steel = Material(
        E=basis.E_STEEL / unit**2,
        nu=basis.NU_STEEL,
        rho=basis.RHO_STEEL,
        fy=basis.FY_S355,
        name="S355",
    )

    model = Model()
    for point in coords:
        model.nodes.add(Node(*point))
    els: list[BeamElement] = []
    for a, b in CONN:
        if subdiv == 1:
            els.append(BeamElement(a, b, section, steel))
            continue
        start, finish = np.array(coords[a]), np.array(coords[b])
        previous = a
        for step in range(1, subdiv):
            model.nodes.add(Node(*(start + (finish - start) * step / subdiv)))
            fresh = len(model.nodes.coords()) - 1
            els.append(BeamElement(previous, fresh, section, steel))
            previous = fresh
        els.append(BeamElement(previous, b, section, steel))
    return model, els


def test_the_corpus_is_read_at_all() -> None:
    """Meta-test: an unread corpus makes every case below vacuous.

    The count is compared to the file's own `id=` lines by a reader that does
    no field splitting, for the reason set out at length in
    `tests/test_marker_exemption_corpus.py`: a parser that drops entries takes
    every assertion built on them with it.
    """
    on_file = sum(
        1 for line in CORPUS.read_text(encoding="utf-8").splitlines() if line.startswith("id=")
    )
    assert ENTRIES, f"{CORPUS} parsed to no entries; the format changed"
    assert len(ENTRIES) == on_file, (
        f"{on_file} entries in the file and {len(ENTRIES)} reached the " "assertions."
    )


@pytest.mark.parametrize("entry", ENTRIES, ids=[e["id"] for e in ENTRIES])
def test_G2_1_holds_at_every_frame_in_the_corpus(entry: dict[str, str]) -> None:
    """The residual form and the spectral gap, at each of the reviewer's frames.

    Asserted on EVERY entry, including the sixteen the retired ratio breaches.
    That is the whole claim: the new form measures the element, so a frame that
    is merely badly conditioned does not move it.
    """
    model, els = _build(entry)
    k = assemble_dense(model, els)

    worst = residual_exactness(k, model)
    assert worst <= RIGID_MODE_EXACTNESS, (
        f"{entry['id']}: the worst rigid-body residual is {worst:.4e}, above "
        f"{RIGID_MODE_EXACTNESS:g}. This frame is the same defect-free element "
        "as every other, so a residual here is a conditioning effect the "
        "ceiling does not cover -- or the element is wrong."
    )

    count, gap = zero_modes_by_gap(k)
    assert count == RIGID, (
        f"{entry['id']}: the largest gap puts {count} modes below it, not "
        f"{RIGID}. The frame is connected and unconstrained, so it has six."
    )
    assert gap >= RIGID_MODE_GAP, (
        f"{entry['id']}: the gap is {gap:.4e}, under {RIGID_MODE_GAP:g}, so "
        "the count above is read across a boundary that is not there."
    )


def test_the_RETIRED_ratio_is_why_the_form_changed(capsys) -> None:
    """The contrast, measured rather than asserted (Q7).

    The retired quantity is recomputed here at every entry and reported. It is
    not asserted against anything -- that is what "retired" means -- and it is
    kept because a reader is owed the evidence for why a gate changed shape.
    """
    from floatfea.tolerances import RIGID_BODY_MODE_RATIO

    over = []
    for entry in ENTRIES:
        model, els = _build(entry)
        ratio = mode_ratio(assemble_dense(model, els))
        if ratio > RIGID_BODY_MODE_RATIO:
            over.append((entry["id"], ratio))
    with capsys.disabled():
        print(
            f"\n  the retired ratio exceeds its ceiling at {len(over)} of "
            f"{len(ENTRIES)} frames, every one a defect-free element"
        )
        for name, ratio in over[:4]:
            print(f"    {name}: {ratio:.4e} against {RIGID_BODY_MODE_RATIO:g}")
    assert over, (
        "the retired ratio now holds at every corpus frame. That is not a "
        "failure, but it removes the evidence this file cites for retiring "
        "it, and the report says the opposite. Re-read both."
    )
