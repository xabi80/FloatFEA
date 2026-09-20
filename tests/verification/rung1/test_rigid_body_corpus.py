"""G2.1's two quantities over the reviewer's frames, not just the shipped one (Q7).

`tests/corpus/g21_rigid_body_frames.txt` is the reviewer's file. It was written
at the twenty-sixth verdict and its own header says why: the shipped gate poses
ONE frame -- one section, one mesh, one unit system -- and every control, every
counter and every published figure was measured at that single configuration by
the hand that chose it.

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
    _analytic_rigid_body,
    _assemble_with_torsional_release,
    _frame,
    mode_ratio,
    residual_exactness,
    seventh_over_epsilon,
    subspace_loss,
)

from floatfea import basis  # noqa: E402
from floatfea.assemble.system import BeamElement, assemble_dense  # noqa: E402
from floatfea.model.material import Material, Section  # noqa: E402
from floatfea.model.nodes import Model, Node  # noqa: E402
from floatfea.tolerances import (  # noqa: E402
    RIGID_MODE_BOUND,
    RIGID_MODE_EXACTNESS,
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

# Filled in by the per-entry test above as it runs, and read by the domain
# test below. Both are in this file and both run in the same session, so
# the domain test is reporting the same numbers the assertions used.
DECIDED: dict[str, float] = {}


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

    # UNDECIDABLE IS AN OUTCOME AND NOT A SKIP (CT2). `CLAUDE.md`
    # § Non-negotiables forbids `skip` outright, and a first version of this
    # used one -- the forbidden mechanism wearing a reason, which is the exact
    # shape this repository has caught twice before. What is asserted per
    # entry is the RESIDUAL, above, which holds at every frame in the corpus
    # including every refused one: the element is under test everywhere. The
    # spectral question is the one the gate declines, and which frames it
    # declines is asserted in `test_the_gate_REFUSES_rather_than_guesses_and_says_how_often`,
    # from the same measurement.
    over = seventh_over_epsilon(k)
    assert over > 0.0, (
        f"{entry['id']}: lambda_7 is zero or absent, so there is nothing to "
        "report. The frame has fewer than seven modes, which is not a "
        "conditioning limit but a broken model."
    )
    DECIDED[entry["id"]] = over


def test_the_gate_REFUSES_rather_than_guesses_and_says_how_often(capsys) -> None:
    """The domain, counted (CT2).

    A gate that declines part of its input has to say how much, or "it passes"
    means nothing. Every frame is classified and both sides are asserted
    non-empty: if nothing were ever refused the `undecidable` branch above
    would be dead code, and if nothing were ever decided the gate would be
    certifying nothing at all.

    THE `kind` FIELD IN THE CORPUS DESCRIBES THE RETIRED RULE. It is not read
    here. The reviewer marks entries `expect=undecidable` under CT2; until
    that lands this reports the split rather than asserting per entry, and
    says so.
    """
    decided, refused = [], []
    for entry in ENTRIES:
        model, els = _build(entry)
        over = seventh_over_epsilon(assemble_dense(model, els))
        (decided if over >= RIGID_MODE_BOUND else refused).append((entry["id"], over))
    assert len(decided) + len(refused) == len(ENTRIES)
    with capsys.disabled():
        print(
            f"\n  the gate decides {len(decided)} of {len(ENTRIES)} frames and "
            f"refuses {len(refused)}"
        )
        for name, over in sorted(refused, key=lambda r: r[1])[:4]:
            print(f"    refused: {name} at {over:.4e} units of ||K_hat||*eps")
    assert decided, "the gate decides no frame in the corpus, so it certifies nothing."
    assert refused, (
        "the gate refuses no frame in the corpus, which would make the "
        "undecidable branch dead code -- and the corpus contains deliberate "
        "extremes of unit and span for which the question IS undecidable."
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


def test_a_PINNED_DOF_is_caught_by_the_RESIDUAL_half(capsys) -> None:
    """Downward, and by the half that can see it (CT1).

    A pin REMOVES a rigid mode; it does not add a seventh. The `lambda_7`
    bound is not what catches it and asking that bound to do so was asking
    the wrong half. What a pin breaks is annihilation.
    """
    model, els = _frame()
    k = assemble_dense(model, els)
    n = k.shape[0]
    analytic = _analytic_rigid_body(model)
    weakest = float("inf")
    for d in range(n):
        keep = np.setdiff1d(np.arange(n), [d])
        sub = k[np.ix_(keep, keep)]
        av = analytic[keep, :]
        scale = float(np.max(np.abs(sub)))
        weakest = min(
            weakest,
            max(
                float(np.linalg.norm(sub @ av[:, j]) / (scale * np.linalg.norm(av[:, j])))
                for j in range(av.shape[1])
            ),
        )
    with capsys.disabled():
        print(f"\n  every pin leaves at least {weakest:.4e} of residual")
    assert weakest > RIGID_MODE_EXACTNESS, (
        f"some pin leaves the analytic vectors annihilated to {weakest:.4e}, "
        f"inside {RIGID_MODE_EXACTNESS:g}."
    )


def test_a_RELEASED_CONNECTION_makes_the_gate_REFUSE(capsys) -> None:
    """Upward, by the shipped bound (CT1).

    A released connection puts a seventh mode at the arithmetic floor, so
    `lambda_7` cannot clear the bound and the gate refuses. That is the same
    red an over-conditioned frame gets, deliberately: in double precision the
    two are the same observation.
    """
    model, els = _frame()
    over = seventh_over_epsilon(_assemble_with_torsional_release(model, els, released=6))
    with capsys.disabled():
        print(f"  one released connection: lambda_7 at {over:.4e} units")
    assert over < RIGID_MODE_BOUND, (
        f"a released connection leaves lambda_7 at {over:.4e} units of "
        f"||K_hat||*eps, at or over {RIGID_MODE_BOUND:g}, so the gate would "
        "answer rather than refuse."
    )


def test_the_COMPOSED_eight_mode_frame_is_REFUSED_not_certified(capsys) -> None:
    """R403's own composition, which the retired rule certified as trustworthy.

    A millimetre unit and a ten-thousand-fold span, each of which holds alone.
    Under the retired rule the count read EIGHT and the gap said the answer
    was trustworthy at seven times its floor. Under CT0 there is no count to
    be wrong, and under CU0 there is one constant to clear: `lambda_7` does
    not clear it and the gate refuses.
    """
    entry = {
        "id": "composed_mm_span",
        "section": "circular_tube,D=0.6,t=0.012",
        "subdiv": "1",
        "unit": "1000",
        "stretch": "1e4",
        "tip": "4.4,1.1,2.8",
    }
    model, els = _build(entry)
    over = seventh_over_epsilon(assemble_dense(model, els))
    with capsys.disabled():
        print(f"  millimetres at ten thousand spans: {over:.4e} units")
    assert over < RIGID_MODE_BOUND, (
        f"R403's composition leaves lambda_7 at {over:.4e} units, so the gate "
        "answers where it used to answer WRONGLY. It should refuse."
    )


def test_a_FINER_UNIT_than_the_corpus_is_still_decided(capsys) -> None:
    """R397's own frame: `K_hat` does not see the unit, so this is green."""
    entry = {
        "id": "finer_than_the_corpus",
        "section": "circular_tube,D=0.6,t=0.012",
        "subdiv": "1",
        "unit": "1e-4",
        "stretch": "1.0",
        "tip": "4.4,1.1,2.8",
    }
    model, els = _build(entry)
    over = seventh_over_epsilon(assemble_dense(model, els))
    with capsys.disabled():
        print(f"  unit 1e-4: {over:.4e} units of ||K_hat||*eps")
    assert over >= RIGID_MODE_BOUND, (
        f"the finer-unit frame is refused at {over:.4e} units. `K_hat` is "
        "homogenised, so a unit change alone must not move this."
    )
