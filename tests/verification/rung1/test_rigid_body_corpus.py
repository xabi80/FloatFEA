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
    _assemble_with_torsional_release,
    _frame,
    mode_ratio,
    residual_exactness,
    subspace_loss,
    zero_modes_below_floor,
)

from floatfea import basis  # noqa: E402
from floatfea.assemble.system import BeamElement, assemble_dense  # noqa: E402
from floatfea.model.material import Material, Section  # noqa: E402
from floatfea.model.nodes import Model, Node  # noqa: E402
from floatfea.tolerances import (  # noqa: E402
    RIGID_MODE_EXACTNESS,
    RIGID_MODE_GAP,
)

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

    Asserted on EVERY entry, including the ones the retired pair breaches.
    HOW MANY IS NOT WRITTEN HERE -- `sixteen` was, and the same round's own
    canonical render said ten (R395). `{{fig:retired_ratio_over_ceiling_on_corpus}}`
    carries it, and `test_the_RETIRED_ratio_is_why_the_form_changed` prints
    both counts at the commit it runs at.

    That is the whole claim: the new form measures the element, so a frame
    that is merely badly conditioned does not move it.
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

    count, gap = zero_modes_below_floor(k)
    assert count == RIGID, (
        f"{entry['id']}: {count} eigenvalues are below tau, not {RIGID}. "
        "The frame is connected and unconstrained, so it has six."
    )
    assert gap >= RIGID_MODE_GAP, (
        f"{entry['id']}: the count is UNTRUSTWORTHY here -- the separation "
        f"after the last mode below tau is {gap:.3f} orders, under "
        f"{RIGID_MODE_GAP:g}."
    )


def test_the_RETIRED_ratio_is_why_the_form_changed(capsys) -> None:
    """The contrast, measured rather than asserted (Q7).

    The retired quantity is recomputed here at every entry and reported. It is
    not asserted against anything -- that is what "retired" means -- and it is
    kept because a reader is owed the evidence for why a gate changed shape.
    """
    from floatfea.tolerances import RIGID_BODY_MODE_RATIO, RIGID_BODY_SUBSPACE_LOSS

    over, loss_over = [], 0
    for entry in ENTRIES:
        model, els = _build(entry)
        k = assemble_dense(model, els)
        ratio = mode_ratio(k)
        if ratio > RIGID_BODY_MODE_RATIO:
            over.append((entry["id"], ratio))
        if subspace_loss(k, model) > RIGID_BODY_SUBSPACE_LOSS:
            loss_over += 1
    with capsys.disabled():
        print(
            f"\n  the retired ratio exceeds its ceiling at {len(over)} of "
            f"{len(ENTRIES)} frames and the retired subspace loss at "
            f"{loss_over}, every one a defect-free element"
        )
        for name, ratio in over[:4]:
            print(f"    {name}: {ratio:.4e} against {RIGID_BODY_MODE_RATIO:g}")
    assert over, (
        "the retired ratio now holds at every corpus frame. That is not a "
        "failure, but it removes the evidence this file cites for retiring "
        "it, and the report says the opposite. Re-read both."
    )


# --------------------------------------------------------------------------
# The four controls CS1 names, each deciding by the shipped rule
# --------------------------------------------------------------------------


def test_a_PINNED_DOF_leaves_FIVE_below_the_floor(capsys) -> None:
    """Downward, at every DOF, by the rule the gate uses (CS1)."""
    model, els = _frame()
    k = assemble_dense(model, els)
    n = k.shape[0]
    seen = set()
    narrowest = float("inf")
    for d in range(n):
        keep = np.setdiff1d(np.arange(n), [d])
        count, gap = zero_modes_below_floor(k[np.ix_(keep, keep)])
        seen.add(count)
        narrowest = min(narrowest, gap)
    with capsys.disabled():
        print(
            f"\n  one DOF pinned, over all {n}: counts {sorted(seen)}, "
            f"narrowest gap {narrowest:.3f} orders"
        )
    assert seen == {RIGID - 1}, f"pinning one DOF gives {sorted(seen)}, not {RIGID - 1}"
    assert narrowest >= RIGID_MODE_GAP, (
        f"the narrowest gap under a pin is {narrowest:.3f} orders, under "
        f"{RIGID_MODE_GAP:g}, so this control is reading a count it cannot trust."
    )


def test_a_RELEASED_CONNECTION_leaves_SEVEN_below_the_floor(capsys) -> None:
    """Upward, by the same rule (CS1)."""
    model, els = _frame()
    count, gap = zero_modes_below_floor(_assemble_with_torsional_release(model, els, released=6))
    with capsys.disabled():
        print(f"  one released connection: {count} below tau, gap {gap:.3f} orders")
    assert count == RIGID + 1, f"a released twist gives {count}, not {RIGID + 1}"
    assert (
        gap >= RIGID_MODE_GAP
    ), f"the released frame's gap is {gap:.3f} orders, under {RIGID_MODE_GAP:g}."


def test_the_COMPOSED_ill_conditioned_frame_is_still_six(capsys) -> None:
    """The reviewer's composed case: a bracing section AND a kilometre unit.

    Under the retired rule the two effects together put the gap under its
    floor (R397). Under CS0's rule the count is six and the separation holds,
    because `tau` is a property of the homogenised matrix rather than of the
    spectrum's shape.
    """
    entry = {
        "id": "composed_brace_kilometre",
        "section": "circular_tube,D=0.1,t=0.001",
        "subdiv": "1",
        "unit": "1000.0",
        "stretch": "1.0",
        "tip": "4.4,1.1,2.8",
    }
    model, els = _build(entry)
    count, gap = zero_modes_below_floor(assemble_dense(model, els))
    with capsys.disabled():
        print(f"  brace at a kilometre unit: {count} below tau, gap {gap:.3f} orders")
    assert count == RIGID, f"the composed frame gives {count}, not {RIGID}"
    assert (
        gap >= RIGID_MODE_GAP
    ), f"the composed frame's gap is {gap:.3f} orders, under {RIGID_MODE_GAP:g}."


def test_a_FINER_UNIT_than_the_corpus_is_still_six(capsys) -> None:
    """The configuration that returned EIGHTEEN under the retired rule (R397).

    One decade finer than the corpus's kilometre entry. The largest gap in
    that spectrum sits after the eighteenth mode, which is why counting below
    the largest gap returned eighteen with nothing warning. Counting below
    `tau` returns six.
    """
    entry = {
        "id": "finer_than_the_corpus",
        "section": "circular_tube,D=0.6,t=0.012",
        "subdiv": "1",
        "unit": "1e-4",
        "stretch": "1.0",
        "tip": "4.4,1.1,2.8",
    }
    model, els = _build(entry)
    count, gap = zero_modes_below_floor(assemble_dense(model, els))
    with capsys.disabled():
        print(f"  unit 1e-4: {count} below tau, gap {gap:.3f} orders")
    assert count == RIGID, (
        f"the finer-unit frame gives {count}, not {RIGID}. This is R397's own "
        "configuration and it is the reason the rule counts below a threshold."
    )
    assert (
        gap >= RIGID_MODE_GAP
    ), f"the finer-unit frame's gap is {gap:.3f} orders, under {RIGID_MODE_GAP:g}."
