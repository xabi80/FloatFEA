"""G2.1 ON REAL MEMBERS (F3 § 5, R486, DD0, DI1).

Two assertions, per member of the real platform, on the member's OWN local
stiffness:

  * the six rigid motions about its midpoint are annihilated, to
    `RIGID_MODE_EXACTNESS`;
  * there is no SEVENTH mode at the arithmetic floor -- the first flexible mode
    sits at least `RIGID_MODE_BOUND` units of `||k_hat|| * eps` above it.

**WHAT THIS REPLACES.** R486 asked for the rigid-mode ceiling shown valid across
the whole admissible domain. DD0 moved that out of F2: "every admissible
configuration" is an open-ended domain and each round found one more axis of it.
Asserting the ceiling on the platform's own members is a stronger statement about
the structure being analysed and a weaker one about structures in general, and
the trade is deliberate.

**AND THERE IS NO NEAR-VERTICAL BAND TO MEASURE IN.** § 5 instructed that this
gate be measured first in that band, on the reasoning that a platform frame is
mostly near-vertical members. It is not: the frame is planar, `max |dz|` is `0.0`
exactly and every member is at 90 degrees from vertical. § 5 was re-locked under
EB0 to say so, and R486's original finding -- a defect-free element reading
`2.9994e-14` on a retired ASSEMBLED form at 2.87 degrees -- is not reachable on
this frame. This gate does not pretend to reach it.

**THE BUILDER REFUSES TOO**, in `floatfea.model.platform.check_rigid_modes`, and
the two are not redundant: this file says the sixteen members this deck produces
are sound, and the refusal says no other deck can produce one that is not.
"""

from __future__ import annotations

import contextlib
import sys
from pathlib import Path

import numpy as np
import pytest

from floatfea.element.beam import local_stiffness
from floatfea.element.rigid import (
    element_lambda_min_over_epsilon,
    element_rigid_residual,
    seventh_over_epsilon,
)
from floatfea.model.platform import build_superstructure, check_rigid_modes
from floatfea.tolerances import (
    PLATFORM_RIGID_MODE_EXACTNESS,
    PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
    RIGID_MODE_BOUND,
    RIGID_MODE_EXACTNESS,
)

MEMBERS = 16
"""What the deck produces, asserted by `test_the_skeleton_is_FIVE_bodies_and_SIXTEEN_members`
in the sibling module. Named here so an empty parametrisation cannot pass."""


def member_stiffnesses() -> list[tuple[str, np.ndarray, float]]:
    """`(label, k_local, length)` for every member of the real platform.

    A MODULE-LEVEL FUNCTION, AND NOT A FIXTURE, so the counters below can replace
    it. The two cells in `tests/test_counters_are_injected.py` patch a module
    attribute; a fixture is resolved by pytest and cannot be reached that way.
    """
    s = build_superstructure()
    return [
        (m.label, local_stiffness(m.section, b.material, m.length), m.length)
        for b in s.bodies
        for m in b.members
    ]


def test_there_are_SIXTEEN_members_to_check() -> None:
    """A parse that finds nothing agrees with everything."""
    rows = member_stiffnesses()
    # expected: the member count the deck implies, asserted independently by
    # `test_platform_skeleton.py::test_the_skeleton_is_FIVE_bodies_and_SIXTEEN_members`
    # against data/platform/platform12_deck.yaml's joint list. Not counted from
    # the rows under test.
    assert len(rows) == MEMBERS, f"{len(rows)} members, not {MEMBERS}"
    assert len({r[0] for r in rows}) == MEMBERS, "two members share a label"


def test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions(capsys) -> None:
    """G2.1's first half, per member, element-local.

    ONE TEST OVER THE SIXTEEN rather than a parametrisation, because the counters
    registered against it inject into every member at once and the registry's
    cells call one function.
    """
    rows = member_stiffnesses()
    worst = 0.0
    worst_label = ""
    for label, k, length in rows:
        residual = element_rigid_residual(k, length)
        if residual > worst:
            worst, worst_label = residual, label
    with capsys.disabled():
        print(
            f"  worst element rigid residual {worst:.4e} on {worst_label}, "
            f"ceiling {PLATFORM_RIGID_MODE_EXACTNESS:g}, margin "
            f"{PLATFORM_RIGID_MODE_EXACTNESS / worst if worst else float('inf'):.2f}x"
        )
    # expected: PLATFORM_RIGID_MODE_EXACTNESS, floatfea/tolerances.py, a pure
    # number because the residual is dimensionless and relative to the quantity
    # compared. NOT `RIGID_MODE_EXACTNESS`, which was measured on the retired
    # assembled form and which two of the three counters cannot cross (R624, EG0):
    # the two ceilings have different subjects and F3 section 7 states both. The
    # left side is the shipped `element_rigid_residual`, tied to rung 1's
    # independent copy by `test_G2_1_the_SHIPPED_residual_agrees_with_RUNG_ONEs`.
    assert worst <= PLATFORM_RIGID_MODE_EXACTNESS, (
        f"{worst_label}: the element-local rigid residual is {worst:.6e}, above "
        f"{PLATFORM_RIGID_MODE_EXACTNESS:g}. The member's own stiffness does not "
        "annihilate the six rigid motions about its midpoint."
    )


def test_G2_1_every_MEMBER_has_NO_SEVENTH_zero_mode(capsys) -> None:
    """G2.1's second half: the first FLEXIBLE mode is resolvably above the floor.

    Where it is not resolvable the outcome is UNDECIDABLE -- red, with the margin
    reported -- because the question cannot be answered in double precision at
    that conditioning, and a gate that answers anyway is worse than one that
    refuses.
    """
    rows = member_stiffnesses()
    over = [(seventh_over_epsilon(k, length), label) for label, k, length in rows]
    smallest, label = min(over)
    with capsys.disabled():
        print(
            f"  smallest seventh/eps {smallest:.4e} on {label}, needing "
            f"{RIGID_MODE_BOUND:g}, margin {smallest / RIGID_MODE_BOUND:.3e}x"
        )
    # expected: RIGID_MODE_BOUND, floatfea/tolerances.py, a pure number for the
    # same reason -- the ratio is measured in units of `||k_hat|| * eps`, which is
    # a property of the arithmetic and not of the structure.
    assert smallest >= RIGID_MODE_BOUND, (
        f"{label}: the first flexible mode sits at {smallest:.6e} units of "
        f"||k_hat||*eps, below {RIGID_MODE_BOUND:g}. Either there is a seventh mode "
        "at the floor, or the conditioning makes the question UNDECIDABLE."
    )


def test_G2_1_the_SHIPPED_residual_agrees_with_RUNG_ONEs() -> None:
    """Two implementations of one formula, compared, so neither can drift.

    `floatfea/element/rigid.py` exists because the builder's refusal cannot import
    from `tests/`. Rung 1 keeps its own copy: it is F2 apparatus and frozen under
    DR1, so it is not re-pointed here. What stops the two diverging is this.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "rung1"))
    try:
        import test_rigid_body_modes as rung1
    finally:
        sys.path.pop(0)

    worst = 0.0
    for _label, k, length in member_stiffnesses():
        # expected: rung 1's own `element_rigid_residual`, a separate
        # implementation of the same formula in
        # tests/verification/rung1/test_rigid_body_modes.py. Not the shipped one
        # under test.
        worst = max(
            worst, abs(element_rigid_residual(k, length) - rung1.element_rigid_residual(k, length))
        )
    assert worst == 0.0, (
        f"the shipped residual and rung 1's disagree by {worst:.6e} on the real "
        "platform's members. One formula, two implementations, and they have drifted."
    )


def test_G2_1_every_MEMBER_is_POSITIVE_SEMI_DEFINITE(capsys) -> None:
    """G2.1's third half (R625), and the one the other two are blind to.

    A correct element stiffness stores energy. Negating a symmetric sub-block
    leaves every rigid motion annihilated and leaves `|lambda_7|` exactly where it
    was, so the residual and the seventh-mode ratio accept an INDEFINITE matrix --
    including the whole matrix negated. This reads the sign.
    """
    rows = member_stiffnesses()
    over = [(element_lambda_min_over_epsilon(k, length), label) for label, k, length in rows]
    smallest, label = min(over)
    with capsys.disabled():
        print(
            f"  smallest lambda_min/eps {smallest:.4e} on {label}, floor "
            f"-{RIGID_MODE_BOUND:g}, margin {abs(RIGID_MODE_BOUND / smallest):.3e}x"
        )
    # expected: -RIGID_MODE_BOUND, floatfea/tolerances.py, reused and not a new
    # constant: it already says how far from the arithmetic floor a mode must sit
    # before its position is a statement about the structure. The left side is
    # SIGNED, which is the entire difference from `seventh_over_epsilon`.
    assert smallest >= -RIGID_MODE_BOUND, (
        f"{label}: the smallest eigenvalue of the homogenised stiffness is "
        f"{smallest:.6e} units of ||k_hat||*eps, below -{RIGID_MODE_BOUND:g}. The "
        "element is indefinite."
    )


# --------------------------------------------------------------------------
# THE BUILDER'S REFUSAL, SOLVED FROM BOTH SIDES (R626).
#
# `check_rigid_modes` is half of what F3 section 5 asserts and NO COMMITTED TEST
# SHOWED IT RAISING -- a grep over `tests/` returned two comment lines, no import
# and no `pytest.raises`. Its sibling `check_limits`, eight lines away in the same
# module, is solved at both boundaries from both sides, which is the standard this
# meets now.
# --------------------------------------------------------------------------

_NEGATED = {
    "the torsion sub-block": (3, 9),
    "the axial sub-block": (0, 6),
    "the WHOLE matrix": tuple(range(12)),
}


def _negate(k: np.ndarray, rows: tuple[int, ...]) -> np.ndarray:
    out = k.copy()
    idx = np.array(rows)
    out[np.ix_(idx, idx)] = -out[np.ix_(idx, idx)]
    return out


def test_the_REFUSAL_accepts_every_real_member() -> None:
    """The other side: on the platform as built, nothing is refused."""
    for label, k, length in member_stiffnesses():
        check_rigid_modes(label, k, length)


@pytest.mark.parametrize("what", sorted(_NEGATED))
def test_the_REFUSAL_rejects_an_INDEFINITE_member(what: str, capsys) -> None:
    """R625's three shapes, each refused by name, at the builder's own boundary."""
    label, k, length = member_stiffnesses()[0]
    bad = _negate(k, _NEGATED[what])
    with capsys.disabled():
        print(
            f"  {what} negated: residual {element_rigid_residual(bad, length):.4e}, "
            f"seventh/eps {seventh_over_epsilon(bad, length):.4e}, "
            f"lambda_min/eps {element_lambda_min_over_epsilon(bad, length):.4e}"
        )
    # expected: RIGID_MODE_EXACTNESS and RIGID_MODE_BOUND, the two ceilings the
    # OTHER halves assert against -- and the claim is that this shape PASSES both
    # of them, so a refusal can only have come from the signed half. Asserted as
    # "still passes", not as "bit-identical": the eigensolver returns the last bits
    # differently on a negated matrix (`937911510493.677` against
    # `...493.6768` for two of the three shapes), and R625 is about detection, not
    # about reproducing a double.
    assert element_rigid_residual(bad, length) <= RIGID_MODE_EXACTNESS
    assert seventh_over_epsilon(bad, length) >= RIGID_MODE_BOUND
    with pytest.raises(ValueError, match="INDEFINITE"):
        check_rigid_modes(label, bad, length)


def test_the_REFUSAL_rejects_a_LIFTED_rigid_mode(capsys) -> None:
    """The residual half's own boundary, from both sides, at the refusal."""
    label, k, length = member_stiffnesses()[0]
    check_rigid_modes(label, k, length)
    bad = k.copy()
    big = float(np.abs(k).max())
    bad[3, 3] += 1.0e-8 * big
    with capsys.disabled():
        print(
            f"  a torsional diagonal +1e-8 of max|k_e|: residual "
            f"{element_rigid_residual(bad, length):.4e}"
        )
    # expected: RIGID_MODE_EXACTNESS, the ceiling the residual half asserts
    # against. The injection site is `scripts/rigid_counter_response.py`'s
    # `rotational_block`, so this is that script's shape and not a new one.
    with pytest.raises(ValueError, match="rigid residual"):
        check_rigid_modes(label, bad, length)


def _retained_torsion(k: np.ndarray, fraction: float) -> np.ndarray:
    """The torsional sub-block scaled down: a NEARLY RELEASED connection.

    The shape the seventh-mode clause exists for, and it is not a perturbation of
    a size: scaling the torsion stiffness toward zero sinks the first flexible
    mode into the round-off band while leaving every rigid motion annihilated and
    the matrix positive semi-definite. The other two clauses are silent on it.
    """
    out = k.copy()
    idx = np.array([3, 9])
    out[np.ix_(idx, idx)] = out[np.ix_(idx, idx)] * fraction
    return out


def test_the_REFUSAL_rejects_a_SUNK_seventh_mode(capsys) -> None:
    """The seventh-mode clause, raising, at its own boundary from both sides (R626).

    **THE OTHER TWO CLAUSES ARE SILENT HERE**, which is why this clause exists and
    why no counter shape reaches it: the residual stays at its clean value and
    `lambda_min` stays at round-off, so a refusal can only have come from the
    seventh-mode comparison.

    THE BOUNDARY IS SOLVED, not stepped past by decades. The report's first
    version claimed this shape at `1e-8 of max|k_e|`, which is wrong twice: it is
    a retained FRACTION rather than an added perturbation, and the edge is
    `2.127342e-10`, 9.67 decades below `1e-8`.
    """
    label, k, length = member_stiffnesses()[0]
    edge = 2.127342e-10
    below, above = _retained_torsion(k, edge * 0.5), _retained_torsion(k, edge * 2.0)
    with capsys.disabled():
        for tag, kk in (("half the edge", below), ("twice the edge", above)):
            print(
                f"  {tag:<15} 7th/eps {seventh_over_epsilon(kk, length):.4e}  "
                f"residual {element_rigid_residual(kk, length):.3e}  "
                f"lambda_min/eps {element_lambda_min_over_epsilon(kk, length):.3e}"
            )

    # expected: RIGID_MODE_BOUND, and the OTHER two ceilings, which this shape
    # leaves satisfied on both sides of the edge -- asserted, not described.
    for kk in (below, above):
        assert element_rigid_residual(kk, length) <= RIGID_MODE_EXACTNESS
        assert element_lambda_min_over_epsilon(kk, length) >= -RIGID_MODE_BOUND

    assert seventh_over_epsilon(below, length) < RIGID_MODE_BOUND
    with pytest.raises(ValueError, match="first flexible mode"):
        check_rigid_modes(label, below, length)

    # And above the edge it is accepted, so the refusal is the position of the
    # mode and not the shape of the mutation.
    assert seventh_over_epsilon(above, length) >= RIGID_MODE_BOUND
    check_rigid_modes(label, above, length)


def _injected(k: np.ndarray, kind: str, size: float) -> np.ndarray:
    """The three counter shapes, at `scripts/rigid_counter_response.py`'s sites."""
    out = k.copy()
    big = float(np.abs(k).max())
    if kind == "dropped_flip":
        out[1, 5] -= size * big
        out[5, 1] = out[1, 5]
    elif kind == "wrong_dof_index":
        out[0, 7] += size * big
        out[7, 0] = out[0, 7]
    elif kind == "rotational_block":
        out[3, 3] += size * big
    else:  # pragma: no cover - a typo in a parametrisation, not a state
        raise AssertionError(f"unknown counter {kind!r}")
    return out


COUNTERS = ("dropped_flip", "wrong_dof_index", "rotational_block")


@pytest.mark.parametrize("kind", COUNTERS)
def test_EG0_the_THREE_COUNTERS_redden_every_member(kind: str, capsys) -> None:
    """EG0(b): 16 of 16, per counter. Not "some member".

    The ceiling exists so that these three can cross it on EVERY member, which is
    what makes the gate a gate rather than a statement about the luckiest element.
    `RIGID_MODE_EXACTNESS` could not do that: two of the three sit below it at the
    declared injection, which is R624.
    """
    rows = member_stiffnesses()
    responses = [
        (
            element_rigid_residual(
                _injected(k, kind, PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT), length
            ),
            lab,
        )
        for lab, k, length in rows
    ]
    weakest, weakest_at = min(responses)
    reddened = sum(1 for r, _ in responses if r > PLATFORM_RIGID_MODE_EXACTNESS)

    # The detection edge, per member, so the figure is the WORST and not the best.
    edges = []
    for lab, k, length in rows:
        lo, hi = 0.0, 1.0e-6
        for _ in range(200):
            mid = (lo + hi) / 2
            if (
                element_rigid_residual(_injected(k, kind, mid), length)
                > PLATFORM_RIGID_MODE_EXACTNESS
            ):
                hi = mid
            else:
                lo = mid
        edges.append((hi, lab))
    worst_edge, worst_edge_at = max(edges)
    best_edge, _ = min(edges)

    with capsys.disabled():
        print(
            f"  {kind}: {reddened}/{len(rows)} reddened, weakest {weakest:.4e} "
            f"= {weakest / PLATFORM_RIGID_MODE_EXACTNESS:.1f}x the ceiling; "
            f"edge worst {worst_edge:.6e} on {worst_edge_at}, best {best_edge:.6e}, "
            f"spread {worst_edge / best_edge:.2f}x"
        )

    # expected: PLATFORM_RIGID_MODE_EXACTNESS, and the injection size
    # PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT, both from floatfea/tolerances.py. The
    # count is the thing asserted: EVERY member, because a counter that reddens one
    # of sixteen leaves fifteen ungated.
    assert reddened == len(rows), (
        f"{kind} at {PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT:g} reddens {reddened} of "
        f"{len(rows)} members; the weakest is {weakest:.6e} on {weakest_at}, against "
        f"a ceiling of {PLATFORM_RIGID_MODE_EXACTNESS:g}. A counter that does not "
        "reach every member leaves the rest of them ungated (EG0(b))."
    )


def test_EG0_the_CEILING_is_the_window_it_claims_to_be(capsys) -> None:
    """The derivation, re-run: the ceiling is inside the window on both sides.

    EG0(c) asks that this be measured on both machines and that the step STOP if
    either clean worst comes within `2x` of the ceiling. This is the assertion that
    makes CI the second machine.
    """
    rows = member_stiffnesses()
    clean = max(element_rigid_residual(k, length) for _, k, length in rows)
    weakest = min(
        element_rigid_residual(
            _injected(k, kind, PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT), length
        )
        for kind in COUNTERS
        for _, k, length in rows
    )
    with capsys.disabled():
        print(
            f"  window ({clean:.6e}, {weakest:.6e}) width "
            f"{weakest / clean:.2f}x; ceiling {PLATFORM_RIGID_MODE_EXACTNESS:g} sits "
            f"{PLATFORM_RIGID_MODE_EXACTNESS / clean:.2f}x above the floor and "
            f"{weakest / PLATFORM_RIGID_MODE_EXACTNESS:.2f}x below the roof"
        )
    # expected: the two edges, measured here, and the shipped constant between
    # them. The constant is NOT re-derived and compared with itself: the assertion
    # is that it lies inside a window whose edges are measured from the members.
    assert clean < PLATFORM_RIGID_MODE_EXACTNESS < weakest, (
        f"the ceiling {PLATFORM_RIGID_MODE_EXACTNESS:g} is not inside the window "
        f"({clean:.6e}, {weakest:.6e}) the sixteen members leave."
    )
    assert PLATFORM_RIGID_MODE_EXACTNESS / clean >= 2.0, (
        # not-a-tolerance: EG0(c)'s REPORTING condition, not a comparison the
        # model depends on. The directive asks that the step STOP and report if
        # either machine's clean worst comes within a factor of two of the
        # ceiling; nothing is accepted or rejected by this number -- the ceiling
        # is, and it is declared -- and widening this would widen no gate.
        f"EG0(c): the clean worst {clean:.6e} is within 2x of the ceiling "
        f"{PLATFORM_RIGID_MODE_EXACTNESS:g} -- {PLATFORM_RIGID_MODE_EXACTNESS / clean:.2f}x. "
        "STOP and report; do not move the ceiling."
    )


@contextlib.contextmanager
def injected_members(kind: str, size: float):
    """Replace `member_stiffnesses` with one that perturbs every member.

    A module-level swap, because `tests/test_counters_are_injected.py`'s two cells
    patch module attributes and a fixture is resolved by pytest.
    """
    clean = member_stiffnesses

    def perturbed() -> list[tuple[str, np.ndarray, float]]:
        return [(lab, _injected(k, kind, size), L) for lab, k, L in clean()]

    globals()["member_stiffnesses"] = perturbed
    try:
        yield
    finally:
        globals()["member_stiffnesses"] = clean


def _counter_reddens_the_gate(kind: str, capsys) -> None:
    """Inject `kind` and require THE GATE FUNCTION to redden; then that it passes.

    **IT CALLS THE GATE (R633).** The first version of this file measured the
    response itself and compared it with the ceiling inline, so BX0's gate cell --
    which replaces the gate with a no-op and requires the counter to fail --
    passed on all three: the counter was asserting itself, which is R163 and R173.
    Resolved at call time through the module global, so the no-op substitution
    reaches it.
    """
    with (
        injected_members(kind, PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT),
        pytest.raises(AssertionError, match="rigid residual"),
    ):
        test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions(capsys)


def test_a_DROPPED_FLIP_reddens_the_gate(capsys) -> None:
    """A sign dropped from the shear-moment coupling `k[1, 5]`."""
    _counter_reddens_the_gate("dropped_flip", capsys)


def test_a_WRONG_DOF_INDEX_reddens_the_gate(capsys) -> None:
    """A coupling written to `k[0, 7]`, across nodes and across DOF kinds."""
    _counter_reddens_the_gate("wrong_dof_index", capsys)


def test_a_ROTATIONAL_BLOCK_reddens_the_gate(capsys) -> None:
    """A torsional diagonal `k[3, 3]` inflated, which lifts a rigid rotation."""
    _counter_reddens_the_gate("rotational_block", capsys)


def counter_response(kind: str) -> float:
    """The worst response at this commit, so the meta-test's widened ceiling is
    measured rather than typed. A literal there would be stale the first time the
    platform's sections or lengths moved."""
    worst = 0.0
    for _, k, length in member_stiffnesses():
        worst = max(
            worst,
            element_rigid_residual(
                _injected(k, kind, PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT), length
            ),
        )
    return worst


def test_G3_1b_the_DECK_the_model_reads_IS_the_one_G3_2_GATES() -> None:
    """G3.1b, and its COINCIDENCE with G3.1a stated rather than implied (DV0).

    G3.1b asks for the mass properties against the FloatSim body definitions. On
    this model those are the same numbers G3.1a B compares against, because the
    deck YAML IS the exported FloatSim definition -- so there is ONE comparison,
    not two independent ones, and the row is kept with the coincidence written
    down rather than left to imply a second witness.

    **AND THIS DOES NOT RE-HASH THE DECK.** A first version did, and it was two
    defects in one: it duplicated
    `test_platform_deck_export.py::test_G3_2_the_committed_deck_matches_its_CONTENT_digest`,
    which already asserts `content_sha(raw) == golden["content_sha256"]`, and it
    hashed the RAW BYTES where that test hashes canonical JSON -- so it failed on
    a correct tree, because the committed file is CRLF on this platform and the
    digest is deliberately blind to that.

    What is left unasserted by G3.2 is the other end of the chain: that the file
    the MODEL reads is the file the exporter writes and G3.2 gates. Two modules
    each hold their own `data/platform/platform12_deck.yaml`, and nothing compared
    them.
    """
    from floatfea.model.platform import DECK_YAML as MODELS_DECK

    from . import test_platform_deck_export as export_gate

    # expected: `DECK_YAML` in tests/verification/rung3/test_platform_deck_export.py,
    # which is the path `test_G3_2_the_committed_deck_matches_its_CONTENT_digest` hashes against
    # the golden, and which `scripts/export_platform_deck.py` writes as `OUT`. Not
    # read from the model's own constant.
    assert MODELS_DECK.resolve() == export_gate.DECK_YAML.resolve(), (
        f"the model reads {MODELS_DECK} and G3.2 gates {export_gate.DECK_YAML}. "
        "G3.1b's properties are then compared against a file whose provenance "
        "nothing checks."
    )


# --------------------------------------------------------------------------
# THE THREE COUNTERS ARE NOT REGISTERED HERE, AND THE REASON IS A MEASUREMENT.
#
# F3 § 5 asks for `dropped_flip`, `wrong_dof_index` and `rotational_block`
# registered against this gate. At the size the F2 constant declares --
# `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1e-14` of `max|k_e|` -- TWO OF THE THREE
# DO NOT REDDEN IT on the real platform's members:
#
#     dropped_flip      worst response 3.6563e-16  = 0.366x that ceiling   NO
#     wrong_dof_index   worst response 9.4595e-15  = 9.459x that ceiling   yes
#     rotational_block  worst response 1.4644e-17  = 0.0146x that ceiling  NO
#
# That constant's own entry pre-registered it: "that counter's size will be
# bisected against THAT gate rather than assumed from this one."
#
# THE EDGES PUBLISHED HERE WERE THE BEST MEMBER, NOT THE WORST (EG1, R630).
# `2.735459e-14 / 1.057143e-15 / 6.837686e-13` are the edges of the member that
# reddens FIRST; a size just above the first of them reddens one member and not
# the worst, which needs 1.93x more. Against the retired `1e-15` ceiling the worst
# over the sixteen is `5.285599e-14 / 1.094071e-15 / 2.642868e-12`, which is what
# the locked plan's section 5 states -- right to the digit. I reported the plan as
# wrong and it was my own figures that were.
#
# AND BOTH SETS ARE MEASURED AGAINST A CEILING THIS COMMIT RETIRED (BP0). An edge
# is a property of the RULE as much as of the member, and the rule moved from
# `RIGID_MODE_EXACTNESS = 1e-15` to `PLATFORM_RIGID_MODE_EXACTNESS = 1.154338e-18`.
# Against the ceiling that now ships, the worst edge over the sixteen is
#
#     dropped_flip      6.266629e-17   on platform:hub4_arm   (spread 2.14x)
#     wrong_dof_index   1.262927e-18   on hub4:buoy12_arm     (spread 1.03x)
#     rotational_block  3.088842e-15   on platform:hub4_arm   (spread 3.93x)
#
# produced by `test_EG0_the_THREE_COUNTERS_redden_every_member` below, which
# bisects per member and prints the worst, the best and the spread at every run --
# so no figure here has to be re-taken by hand when the platform moves. The two
# older sets are kept as the record of what was published under the old rule, each
# labelled with the rule it was measured against, which is what BP0 asks instead
# of a silent replacement.
#
# EG0 ANSWERED R624: the gate has its own ceiling now,
# `PLATFORM_RIGID_MODE_EXACTNESS`, and the three counters are registered against
# it below. The refusal keeps `RIGID_MODE_EXACTNESS` and hosts no counter, because
# over the admissible band the window is empty.
#
# Registering them needs an injection size this gate can see, and declaring one
# is a decision rather than a repair: `CLAUDE.md` puts every numerical tolerance
# in `floatfea/tolerances.py`, and
# `tests/test_report_carried.py`'s sibling `test_every_declared_tolerance_appears_
# in_the_plan` then requires a row in `docs/milestones/F2.md` -- a CLOSED
# milestone's locked plan. The alternative is a derived not-a-tolerance factor in
# the manner of `WIDEN`. The step report puts both to Xabier; neither is taken
# here, and nothing is registered under a size that cannot see the defect.
#
# WHAT IS NOT IN DOUBT: the gate itself reddens under all three shapes at a size
# it can see, and `floatfea.model.platform.check_rigid_modes` refuses the build
# under all three plus a nearly-released seventh mode. Both measurements are in
# the step report.
# --------------------------------------------------------------------------
