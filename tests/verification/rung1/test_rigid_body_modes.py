"""V1.1 — rigid-body modes, gate G2.1 (D2 step 5).

An unconstrained assembly has exactly **six** zero-energy modes: three
translations and three rotations. This file asserts that in TWO HALVES, and
neither of them reads an eigenvector (CT0).

1. THE RESIDUAL. `max_j ||K_hat v_j|| / ||v_j||` over the six ANALYTIC
   rigid-body vectors, on `K_hat = K / max|K|`, against `RIGID_MODE_EXACTNESS`.
   The six exact rigid motions are annihilated by `K`. Dimensionless, and it
   uses no eigensolve at all.
2. THERE IS NO SEVENTH. `lambda_7(K_hat) >= RIGID_MODE_BOUND * ||K_hat|| *
   eps`, a plain ratio against ONE constant (CU0). The first half puts six
   eigenvalues at the arithmetic floor by Courant-Fischer; this certifies that
   nothing else is down there. Where `lambda_7` is not resolvable the outcome
   is UNDECIDABLE -- red, with the ratio reported -- because at that
   conditioning no spectral rule in double precision separates a soft flexible
   mode from a mechanism.

   IT SHIPPED AS TWO CONSTANTS AND THEY WERE ONE THRESHOLD. `RIGID_MODE_FLOOR`
   times `10**RIGID_MODE_GAP` entered the only assertion as a product, nothing
   counted eigenvalues below the floor, and the reviewer moved the pair in
   compensating directions with everything green and the floor at a value its
   own entry called wrong (R415). `RIGID_MODE_BOUND` is that product.

WHY NOT THE SUBSPACE, WHICH IS WHAT THIS FILE USED TO ASSERT. `AP3` is right
that mode SHAPES are an arbitrary basis inside the degenerate block, and the
subspace form was the answer to that. But the subspace form is computed from
the first six eigenVECTORS, so what it measures includes the eigensolver --
and the reviewer's corpus found it exceeding its ceiling on MORE frames than
the ratio it was preferred to, with a defect-free element. The loss's count is
not machine-stable, so no figure carries it and none is typed here; `a large
minority` stood here as a quantifier nothing could check (R405). The ratio's
count is `{{fig:retired_ratio_over_ceiling_on_corpus}}` of
`{{fig:rigid_mode_corpus_frames}}`, and the corpus test prints both when it
runs.

claim: the generated figures file carries a count for the retired subspace
       loss as well as for the retired ratio. It did not, for three rounds
       and three refuted reasons, while four sentences compared the two
       (R454) -- this one among them.
cmd:   count("docs/milestones/F2_figures.md", "retired_loss_over")
ctl:   retired_loss_figure_row
out:   1
Both are retired (CS2) and both are reported by
`test_the_eigenvalue_RATIO_is_a_diagnostic_and_not_a_gate`. The residual
answers AP3's objection without an eigensolve: the analytic vectors are
annihilated or they are not, whatever basis anything computes.

THE EIGENSOLVER, AND WHERE THE `v0` PIN LIVES. The gate uses a DENSE symmetric
eigensolve (`scipy.linalg.eigh`), which is deterministic by construction: it has
no starting vector, so there is nothing to pin and pinning would be vacuous. The
`v0` pin AP3 is about belongs to ARPACK, and it is exercised here rather than
asserted about: `test_the_ARPACK_path_is_REPRODUCIBLE_under_its_pin` runs the
sparse path twice from `determinism.deterministic_v0` and requires bit-identical
eigenvalues. Choosing ARPACK for the gate itself in order to have a pin to point
at would be choosing a less accurate method to satisfy a guard.

NEGATIVE CONTROLS, BOTH DIRECTIONS (the plan's D5 row is rewritten to these, per
R4: a planned counter-case is replaced by the shipped one as the row lands).
The planned counter was "one node's mass omitted", which cannot be built here --
there is no mass matrix until step 7 and this gate does not use one.

  * pin ONE degree of freedom  -> the nullspace must fall to FIVE;
  * release ONE member's torsional continuity -> it must rise to SEVEN.

The second is built by DOF mapping rather than by `releases.py`, which is step 11
and does not exist: the released member's end rotation about its own axis is
assembled into an extra scalar DOF instead of into the shared node's. That member
can then twist rigidly about its own axis at zero strain energy while nothing
else moves, which is exactly one extra mode and is provable rather than measured.
"""

from __future__ import annotations

import contextlib
import math
import sys
from pathlib import Path

import numpy as np
import pytest
import scipy.linalg as sla
import scipy.sparse.linalg as spla

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from floatfea import basis  # noqa: E402
from floatfea.assemble.system import (  # noqa: E402
    BeamElement,
    assemble,
    assemble_dense,
    element_global_stiffness,
    element_length,
)
from floatfea.determinism import deterministic_v0  # noqa: E402
from floatfea.element.beam import local_stiffness  # noqa: E402
from floatfea.model.material import Material, Section  # noqa: E402
from floatfea.model.nodes import Model, Node, element_dofs  # noqa: E402
from floatfea.tolerances import (  # noqa: E402
    RIGID_BODY_MODE_RATIO,
    RIGID_BODY_MODE_RATIO_COUNTER_DEFECT,
    RIGID_BODY_SUBSPACE_LOSS,
    RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT,
    RIGID_MODE_BOUND,
    RIGID_MODE_BOUND_COUNTER_DEFECT,
    RIGID_MODE_EXACTNESS,
    RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
    RIGID_MODE_FLOOR_COUNTER_DEFECT,
    RIGID_MODE_GAP_COUNTER_DEFECT,
)

DOF_PER_NODE = 6
RIGID = 6
"""not-a-tolerance: the dimension of the rigid-body space of a free body in three
dimensions. Three translations and three rotations; a structural constant of the
kinematics, not a threshold anything is compared against."""

S355 = Material(
    E=basis.E_STEEL, nu=basis.NU_STEEL, rho=basis.RHO_STEEL, fy=basis.FY_S355, name="S355"
)
SEC = Section.circular_tube(0.6, 0.012)


def _frame() -> tuple[Model, list[BeamElement]]:
    """A connected, unconstrained, genuinely three-dimensional space frame.

    NOT PLANAR, DELIBERATELY. A planar frame's out-of-plane behaviour is carried
    by a different set of transformation entries, and G2.2's own history is that
    a plane which is never exercised hides half an element's bending stiffness
    (R1). Nothing here is symmetric enough to make two flexible modes coincide,
    which would put a degeneracy next to the one being measured.

    The geometry is CONSTRUCTED, which is what the plan's case table asks for:
    V1.1 needs an unconstrained assembly, not a particular platform. It is not
    the production shape and no number here is a statement about one.

    NODE 4 IS A TIP ON A MEMBER PARALLEL TO GLOBAL X, and that is not decoration.
    The release control needs to cut a member's TORSIONAL continuity, which is a
    rotation about the member's own axis; the assembled matrix is in global
    coordinates, so the two coincide only when the member is axis-parallel. The
    first version of this frame put node 4 off-axis, cut the global rotation
    instead, and the control read SIX -- the mechanism it was built to create did
    not exist. Measured, not reasoned about: see the control's own docstring.
    """
    m = Model()
    for xyz in (
        (0.0, 0.0, 0.0),
        (4.0, 0.0, 0.0),
        (1.7, 3.3, 0.0),
        (1.9, 1.1, 2.8),
        (4.4, 1.1, 2.8),
    ):
        m.nodes.add(Node(*xyz))
    els = [
        BeamElement(a, b, SEC, S355)
        for a, b in ((0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (2, 3), (3, 4))
    ]
    return m, els


def _analytic_rigid_body(model: Model) -> np.ndarray:
    """`(n_dof, 6)` — the exact rigid-body modes of this node set.

    Three unit translations, and three rotations about the **CENTROID**, and
    the choice of that point is LOAD-BEARING rather than cosmetic.

    THE SENTENCE THAT STOOD HERE SAID THE OPPOSITE (R492, R475). It read "the
    centroid is used rather than the origin only so the columns are better
    conditioned as a basis; any point gives the same six-dimensional span,
    which is the thing under test". The span claim is true and it is not what
    the gate reads. The gate reads a residual computed FROM THESE COLUMNS, and
    that quantity is not invariant under the reference point: moving the point
    away from the node set scales every rotation column's translational
    entries by the lever arm, while a defect on a rotational DOF keeps weight
    1, so the defect's share of the quantity falls.

    Measured, span held at 4 m, only the point moved -- the cell that ships as
    the reference-point cell, now retired with the quantity: at the centroid an injected
    rotational defect is detected; at 10^3 and 10^6 spans away the defective
    frame and the clean frame produce the same number. That is why the point
    is fixed here, in one place, and why a caller does not get to choose it.

    It is the centroid rather than any other interior point because the
    centroid is inside the convex hull of the node set by construction, so the
    lever arms are bounded by the model's own span and no choice of origin can
    inflate them.
    """
    xyz = model.nodes.coords()
    centre = xyz.mean(axis=0)
    r = xyz - centre
    n = model.nodes.n_dof
    modes = np.zeros((n, RIGID))
    for d in range(3):
        modes[d::6, d] = 1.0  # translation along d
    for a in range(3):  # rotation about axis a
        axis = np.zeros(3)
        axis[a] = 1.0
        modes[0::6, 3 + a] = np.cross(axis, r)[:, 0]
        modes[1::6, 3 + a] = np.cross(axis, r)[:, 1]
        modes[2::6, 3 + a] = np.cross(axis, r)[:, 2]
        modes[3 + a :: 6, 3 + a] = 1.0
    return modes


def assembled(model: Model, els: list[BeamElement]) -> np.ndarray:
    """The assembled stiffness both gates read, and the ONE injection point.

    Its only job is to be patchable. A counter that builds a defective matrix
    itself and compares the result with the ceiling never runs the assertion it
    defends, which is R163's defect and what
    `tests/test_counters_are_injected.py` exists to find; a counter that patches
    THIS makes the shipped gate compute the defective number and decide on it.
    """
    return assemble_dense(model, els)


def _spectrum(k: np.ndarray) -> np.ndarray:
    """Ascending eigenvalues of a symmetric matrix, dense and deterministic."""
    return np.sort(sla.eigh(k, eigvals_only=True))


def mode_ratio(k: np.ndarray) -> float:
    """`lambda_6 / lambda_7` — the last zero mode against the first flexible one.

    Dimensionless by construction, which is the whole point of G2.1's wording:
    both eigenvalues carry the same units and the same overall scaling, so the
    ratio is invariant under a change of `E`, of section, and of the length unit.
    """
    w = _spectrum(k)
    flexible = w[RIGID]
    if flexible <= 0.0:
        raise ValueError(
            f"the seventh eigenvalue is {flexible:.6e}, not positive. There is "
            "no flexible mode to normalise against, so this model has more "
            "rigid-body freedom than the gate assumes and the ratio would be "
            "meaningless rather than large."
        )
    return float(abs(w[RIGID - 1]) / flexible)


EPS = float(np.finfo(np.float64).eps)
"""not-a-tolerance: the machine's own unit round-off, used to homogenise a
spectrum so two frames can be compared. It is a property of the float format
and nothing is compared against it."""


def residual_exactness(k: np.ndarray, model: Model) -> float:
    """G2.1's first quantity, normalised PER ROW and shared across the six.

        d_i       = max_j ( |K_hat| |v_j| )_i          one denominator per DOF
        residual  = max_j max_i |(K_hat v_j)_i| / d_i

    `K_hat = K / max|K|`, so the quantity is invariant under `E`, the section
    and the length unit. No eigenvalues, no eigenvectors, no solve: it reads
    `K` and the analytic vectors and nothing else.

    WHY PER ROW, AND WHY SHARED (R475). The shipped form was
    `||K v_j|| / (max|K| * ||v_j||)` -- one global normaliser per vector. A
    rotation column carries lever arms O(span) on translational DOFs and
    exactly 1.0 on rotational ones, so `||v_j||` grows with the model while a
    defect on a rotational DOF does not, and the defect's share of the
    quantity falls away. Measured by the reviewer: the same injected defect
    that reddens at 4 m is INVISIBLE at 400 m, the defective frame and the
    clean frame reading the same number to four figures. A defect 40x the
    shipped counter passed the whole gate at a span the corpus already held.

    Dividing each residual COMPONENT by the absolute stiffness available at
    that same DOF removes the mismatch: both sides of the ratio are weighted
    the same way, so a defect is measured against what could have resisted it
    rather than against the whole model. The denominator is shared across the
    six vectors -- `max_j` rather than per-vector -- because a per-vector
    denominator was measured false-reddening a defect-free element on
    near-vertical members, which is R486's finding and now a G3 gate.

    ASSERTED ON THE WORST OF THE SIX, never a mean, per `CLAUDE.md`.
    """
    scale = float(np.max(np.abs(k)))
    khat = k / scale
    absk = np.abs(khat)
    modes = _analytic_rigid_body(model)

    # One denominator per row, the largest any of the six vectors excites there.
    content = np.max(np.stack([absk @ np.abs(modes[:, j]) for j in range(modes.shape[1])]), axis=0)
    live = content > 0.0

    # R487: THE MASKED BRANCH IS UNREACHABLE, AND THAT IS AN ASSERTION RATHER
    # THAN A COMMENT. `content_i >= |(K_hat v_j)_i|` for every i and j by the
    # triangle inequality -- `|sum_k K_ik v_jk| <= sum_k |K_ik||v_jk|` -- so a
    # row with zero content has zero numerator in all six columns, and
    # skipping it cannot hide a residual. A comment saying so is a claim; this
    # is the check.
    for j in range(modes.shape[1]):
        numerator = np.abs(khat @ modes[:, j])
        assert not np.any(numerator[~live] > 0.0), (
            "a DOF with no absolute stiffness content carries a non-zero "
            "residual, which the triangle inequality forbids. Either `K_hat` "
            "has a NaN or the masking below is hiding a real residual."
        )

    worst = 0.0
    for j in range(modes.shape[1]):
        numerator = np.abs(khat @ modes[:, j])
        worst = max(worst, float(np.max(numerator[live] / content[live])))
    return worst


def homogenised(k: np.ndarray) -> np.ndarray:
    """`K_hat = K / max|K|` -- the same homogenisation `residual_exactness` uses.

    Its entries are O(1) whatever the model's units, stiffness or section, so
    the round-off floor of `K_hat` is a property of the arithmetic rather than
    of the structure. Everything CS0 measures is measured on this.
    """
    return k / float(np.max(np.abs(k)))


def epsilon_unit(k: np.ndarray) -> float:
    """`||K_hat|| * eps` -- the arithmetic floor of the homogenised matrix.

    Everything the spectral half measures is measured in these units, which is
    what makes the constant above it a pure number: `K_hat`'s entries are O(1)
    whatever the model's units, stiffness or section, so its round-off floor is
    a property of the arithmetic rather than of the structure.
    """
    kh = homogenised(k)
    return float(np.max(np.abs(sla.eigh(kh, eigvals_only=True)))) * EPS


def zero_modes_under_the_bound(k: np.ndarray) -> int:
    """How many eigenvalues of `K_hat` fall under the bound. DIAGNOSTIC ONLY.

    THE GATE MAY NOT ASSERT AGAINST THIS; A CONTROL MAY (CU0, corrected at
    R425). Under a single constant this count carries no information the gate
    does not already have: `count == 6` is algebraically `lambda_7 > bound AND
    the six rigid eigenvalues are under bound`, so asserting it inside
    `test_there_is_NO_SEVENTH_zero_mode` would be a second name for one
    decision -- which is the defect CU0 removed. The gate prints it instead,
    because the second conjunct is the composition the gate rests on and a
    reader should be able to see it rather than take it.

    A CONTROL IS THE OPPOSITE CASE and R420 is why.
    `test_ONE_RELEASED_CONNECTION_gives_SEVEN` needs a second measurement that
    can disagree with the bound, and counting the spectrum is one: the release
    must put exactly SEVEN under the bound, which also requires `lambda_8`
    above it, and that can fail while the bound assertion passes. A reader who
    takes `nothing may assert this` at its word deletes that assertion, which
    is what the sentence standing here would have cost.

    claim: three lines in this file name this function -- its definition, the
           gate's DIAGNOSTIC print, and the release control's second assertion
    cmd:   count("tests/verification/rung1/test_rigid_body_modes.py", "zero_modes_under_the_bound(")
    ctl:   zero_modes_call_site
    out:   3
    """
    w = np.sort(np.abs(sla.eigh(homogenised(k), eigvals_only=True)))
    return int(np.sum(w <= RIGID_MODE_BOUND * epsilon_unit(k)))


def largest_rigid_eigenvalue(k: np.ndarray) -> float:
    """The largest of the six numerically-zero eigenvalues, in `||K_hat||*eps`.

    THE COURANT-FISCHER COMPOSITION, made visible. The residual half proves the
    six analytic rigid-body vectors are annihilated, which puts six eigenvalues
    at the arithmetic floor; the bound then certifies there is no seventh. That
    argument needs the six to be UNDER the bound, and this is the number that
    says how far under. It is the lower side of `RIGID_MODE_BOUND`'s window and
    it is reported, not asserted here -- `regen_figures` carries it as a
    floor-class row against the bound, which is where it decides something.
    """
    w = np.sort(np.abs(sla.eigh(homogenised(k), eigvals_only=True)))
    return float(w[RIGID - 1] / epsilon_unit(k))


def seventh_over_epsilon(k: np.ndarray) -> float:
    """`lambda_7(K_hat) / (||K_hat|| * eps)` -- where the FIRST FLEXIBLE mode
    sits above the arithmetic floor, as a PLAIN RATIO.

    THIS IS THE WHOLE OF THE COUNT HALF (CT0). The residual half proves the six
    analytic rigid-body vectors are annihilated by `K`, and by Courant-Fischer
    that puts six eigenvalues at the floor; what remains to certify is that
    there is no SEVENTH, which is a statement about `lambda_7` and nothing else.

    TWO EARLIER FORMS WERE REFUTED BY THE REVIEWER'S CORPUS, and both failed
    the same way -- by measuring somewhere other than where the claim lives:

      * "modes below the largest gap" returned EIGHTEEN at a fine length unit,
        because the largest gap in a spectrum can sit anywhere (R397);
      * "the count below tau, validated by the gap after the last one below it"
        let EIGHT modes through with a separation seven times its floor, on two
        composed corpus entries that each hold alone. A gap measured wherever
        the transition happens to be detects being AT a transition, not being
        past one (R403).

    The bound is at the sixth-seventh boundary.

    claim: nothing in this file measures anything at "the last eigenvalue
           below tau", which is where the refuted form measured
    cmd:   count("tests/verification/rung1/test_rigid_body_modes.py", "last_below")
    ctl:   last_below_needle
    out:   0

    A SMALL RESULT IS NOT A FAILED COUNT, it is `lambda_7` at the arithmetic
    floor: the softest flexible mode has sunk into round-off, and no spectral
    rule in double precision can tell that mode from a mechanism. The gate's
    only honest output there is UNDECIDABLE.

    A RATIO AND NOT A LOGARITHM (CU0). It was published in orders, which made
    it the first log-valued figure here and cost two rounds: the staleness
    guard compared a difference of logarithms against a spread declared on
    ratios (R404), and the repair then missed a row that had been renamed out
    of the `_orders` suffix it dispatched on (R418). One constant makes the
    natural quantity a ratio, and the comparison rule is keyed on the row's
    declared class now rather than on its name.
    """
    w = np.sort(np.abs(sla.eigh(homogenised(k), eigvals_only=True)))
    if w.size <= RIGID or w[RIGID] <= 0.0:
        return 0.0
    return float(w[RIGID] / epsilon_unit(k))


def subspace_loss(k: np.ndarray, model: Model) -> float:
    """The largest fraction of an analytic rigid-body vector outside the span.

    The computed nullspace basis is the first six eigenvectors. Each analytic
    vector is projected onto that basis and what is left over is measured
    relative to the vector's own norm, so the quantity is a fraction in `[0, 1]`
    and is invariant under scaling either side.

    ASSERTED ON THE WORST OF THE SIX, never on a mean: a single lost direction
    is exactly the failure this exists to catch, and averaging it against five
    good ones is what `CLAUDE.md` forbids.
    """
    vecs = sla.eigh(k)[1][:, :RIGID]
    q, _ = np.linalg.qr(vecs)
    analytic = _analytic_rigid_body(model)
    worst = 0.0
    for j in range(analytic.shape[1]):
        v = analytic[:, j]
        residual = v - q @ (q.T @ v)
        worst = max(worst, float(np.linalg.norm(residual) / np.linalg.norm(v)))
    return worst


def _assemble_with_torsional_release(
    model: Model, els: list[BeamElement], released: int
) -> np.ndarray:
    """The frame with one member's torsional continuity cut at its first node.

    One EXTRA scalar DOF is appended, and the released element's end rotation
    about the global x axis is assembled into it instead of into the shared
    node's. `released` must therefore be a member whose far end is a free tip,
    so the freed twist moves nothing else.

    WHY THIS IS A MECHANISM AND NOT A DECOUPLING. The released member can rotate
    rigidly about its own axis: its own end rotations move together, its nodes do
    not translate, no other member sees anything. Zero strain energy, and exactly
    one mode, because only the one released component is free.
    """
    n = model.nodes.n_dof
    k = np.zeros((n + 1, n + 1))
    for i, e in enumerate(els):
        dofs = element_dofs(e.node_a, e.node_b).copy()
        if i == released:
            dofs[3] = n  # local end-A rx -> the extra scalar DOF
        ke = element_global_stiffness(model, e)
        k[np.ix_(dofs, dofs)] += ke
    return k


def counter_response(which: str) -> float:
    """What the counter's injected defect actually MEASURES, at this commit.

    Exists so `tests/test_counters_are_injected.py` can widen these ceilings past
    the counter's own injection without typing a measured number into the
    meta-test. The response is a measurement and it moves with the frame; a
    literal there would be stale the first time the frame changes, which is the
    species step 4 spent five rounds on.
    """
    model, els = _frame()
    k = assemble_dense(model, els)
    scale = float(np.abs(k).max())

    # THE BOUND'S COUNTER IS A DIFFERENT INJECTION and is built here rather
    # than by scaling one diagonal entry: a connection that is NEARLY released
    # leaves the seventh mode just under the bound, which is the state the gate
    # exists to refuse. Scaling a diagonal lifts a rigid mode instead, which is
    # the residual half's defect and is already covered above.
    #
    # THE TWO RETIRED SIZES ARE STILL COMPUTED, exactly as the retired ratio's
    # and loss's counters are: a retired constant keeps its record, and the
    # record here is what its defect does under the rule that replaced it.
    # `RIGID_MODE_FLOOR_COUNTER_DEFECT` is the reason one of them is retired
    # rather than kept -- see the counter test below.
    if which in ("bound", "retired_floor", "retired_gap"):
        size = {
            "bound": RIGID_MODE_BOUND_COUNTER_DEFECT,
            "retired_floor": RIGID_MODE_FLOOR_COUNTER_DEFECT,
            "retired_gap": RIGID_MODE_GAP_COUNTER_DEFECT,
        }[which]
        kr = _assemble_with_torsional_release(model, els, released=6)
        kr[-1, -1] += size * float(np.abs(kr).max())
        return seventh_over_epsilon(kr)

    size = {
        "ratio": RIGID_BODY_MODE_RATIO_COUNTER_DEFECT,
        "loss": RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT,
        "residual": RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
    }[which]
    k[0, 0] += size * scale
    if which == "ratio":
        return mode_ratio(k)
    if which == "residual":
        return residual_exactness(k, model)
    return subspace_loss(k, model)


# --------------------------------------------------------------------------
# The gate
# --------------------------------------------------------------------------


# THE CLAIM-A GATE WAS HERE AND IS RETIRED (DI0). Its name is not written out: It asserted claim A
# on
# the assembled matrix. Claim A is a diagnostic now and the quantity it used is retired; see
# `element_rigid_residual` above and F2.md section 5d.


def test_there_is_NO_SEVENTH_zero_mode(capsys) -> None:
    """G2.1's second half: `lambda_7` is resolvably above the floor (CT0).

    ONE ASSERTION, and it is not a count. The residual half supplies the six;
    this certifies there is no seventh. Where `lambda_7` is not resolvable the
    outcome is UNDECIDABLE -- red, with the margin reported -- because the
    question cannot be answered in double precision at that conditioning, and
    a gate that answers anyway is worse than one that refuses.
    """
    model, els = _frame()
    k = assembled(model, els)
    over = seventh_over_epsilon(k)
    with capsys.disabled():
        w = np.sort(np.abs(sla.eigh(homogenised(k), eigvals_only=True)))
        unit = epsilon_unit(k)
        print(
            f"  lambda_7 {w[RIGID]:.4e} is {over:.4e} units of ||K_hat||*eps "
            f"({unit:.4e}), needing {RIGID_MODE_BOUND:g}"
        )
        # THE DIAGNOSTIC, PRINTED AND NOT ASSERTED (CU0). See
        # `zero_modes_under_the_bound`: under one constant this is the
        # assertion plus "the six are under the bound", so asserting it would
        # add a second name for one decision -- which is the defect this
        # round removed.
        print(
            f"  DIAGNOSTIC {zero_modes_under_the_bound(k)} eigenvalues under "
            f"the bound; the largest of the six is "
            f"{w[RIGID - 1] / unit:.4f} units"
        )
    assert over >= RIGID_MODE_BOUND, (
        f"UNDECIDABLE: the first flexible mode sits at {over:.4e} units of "
        f"||K_hat||*eps and G2.1 needs {RIGID_MODE_BOUND:g} to tell it from a "
        "mechanism. Either this model HAS a seventh zero mode, or its softest "
        "flexible mode has sunk into round-off at this conditioning -- and in "
        "double precision no spectral rule separates those two. The gate "
        "refuses rather than reporting a number it cannot defend."
    )


def test_the_eigenvalue_RATIO_is_a_diagnostic_and_not_a_gate(capsys) -> None:
    """`lambda_6 / lambda_7`, RETIRED to a diagnostic by Q7.

    IT WAS THE GATE AND THE REVIEWER'S CORPUS REFUTED IT.
    `{{fig:retired_ratio_over_ceiling_on_corpus}}` of the reviewer's
    `{{fig:rigid_mode_corpus_frames}}` frames exceed its ceiling with a
    defect-free element, because the quantity moves with the frame's
    conditioning -- bracing sections, mesh subdivision, span, and above all
    the length unit. `Sixteen of the twenty-eight frames` stood here and both
    numbers were stale (R405); this test prints the live count when it runs.
    A ceiling that a defect-free element fails at the
    centimetre re-expression of a frame it passes at the metre is a ceiling on
    the frame, and G2.1 is not a statement about the frame.

    It is printed because it is informative about conditioning and it is the
    number three earlier revisions published. THE CEILING DECIDES NOTHING; the
    quantity is asserted to be FINITE, thirty lines below, which is a check on
    the eigensolve and not on the element. `Nothing is asserted against it`
    stood here and was refuted by the function's own body (R436).

    `RIGID_BODY_SUBSPACE_LOSS` IS RETIRED WITH IT (CS2), for the stronger
    reason: it breached at `{{fig:retired_loss_over_ceiling_on_corpus}}` of
    the reviewer's clean frames against the ratio's
    `{{fig:retired_ratio_over_ceiling_on_corpus}}`, so the quantity that had
    been kept was the one the evidence indicted harder. BOTH COUNTS ARE
    FIGURES AND NEITHER IS TYPED. Two were, in words, measured on a 28-frame
    corpus that is now four times that, twelve lines from a docstring in this
    same file saying the loss count is not written here (R423). The dead
    numbers are deliberately not quoted back: writing them would make the
    sentence beside them false, which is how the first version of this repair
    failed its own check.
    `test_the_RETIRED_ratio_is_why_the_form_changed` in the corpus file
    prints both when it runs.

    claim: no count of either retired quantity's breaches is typed in this file
    cmd:   count("tests/verification/rung1/test_rigid_body_modes.py", "seventeen")
    ctl:   seventeen_word
    out:   0
    """
    model, els = _frame()
    k = assembled(model, els)
    ratio = mode_ratio(k)
    loss = subspace_loss(k, model)
    w = _spectrum(k)
    with capsys.disabled():
        print(
            f"  DIAGNOSTIC lambda_6 {w[RIGID - 1]:.4e}  lambda_7 {w[RIGID]:.4e}"
            f"  ratio {ratio:.4e} (retired ceiling {RIGID_BODY_MODE_RATIO:g})"
            f"  subspace loss {loss:.4e} (retired ceiling "
            f"{RIGID_BODY_SUBSPACE_LOSS:g})"
        )
    assert math.isfinite(ratio), (
        "the diagnostic ratio is not finite, which means the seventh "
        "eigenvalue is zero and the model has more freedom than G2.1 assumes."
    )


# --------------------------------------------------------------------------
# The negative controls, in both directions
# --------------------------------------------------------------------------


def test_ONE_PINNED_DOF_leaves_FIVE(capsys) -> None:
    """Downward control. Fixing one DOF must remove exactly one zero mode.

    Without this, a gate that counted six could be counting six of anything. It
    is run at every single DOF rather than at a chosen one, because a DOF that
    happens to be uncoupled would pass a one-sample version silently.

    IT DECIDES BY THE RESIDUAL HALF, which is CT1's point and a correction to
    CS1's. A pin does not add a seventh zero mode -- it REMOVES a rigid one --
    so the `lambda_7` bound is not what catches it and asking that bound to do
    so was asking the wrong half. What a pin breaks is annihilation: a rigid
    vector the pinned structure no longer admits, which the residual measures
    directly.
    """
    model, els = _frame()
    k = assemble_dense(model, els)
    n = k.shape[0]
    analytic = _analytic_rigid_body(model)
    broken = []
    for d in range(n):
        keep = np.setdiff1d(np.arange(n), [d])
        sub = k[np.ix_(keep, keep)]
        av = analytic[keep, :]
        scale = float(np.max(np.abs(sub)))
        broken.append(
            max(
                float(np.linalg.norm(sub @ av[:, j]) / (scale * np.linalg.norm(av[:, j])))
                for j in range(av.shape[1])
            )
        )
    weakest = min(broken)
    with capsys.disabled():
        print(
            f"  one DOF pinned, over all {n}: the WORST analytic vector leaves "
            f"at least {weakest:.4e} at every pin, against a ceiling of "
            f"{RIGID_MODE_EXACTNESS:g}"
        )
    assert weakest > RIGID_MODE_EXACTNESS, (
        f"some pin leaves every analytic rigid vector annihilated to "
        f"{weakest:.4e}, inside the gate's own ceiling. A pinned structure "
        "does not admit all six rigid motions, so the residual half must see "
        "it; if it does not, that half is measuring something else."
    )


def test_ONE_RELEASED_CONNECTION_gives_SEVEN(capsys) -> None:
    """Upward control. A model with a genuine mechanism must not read six.

    The released member is `(3, 4)`: node 4 is a free tip and the member is
    parallel to global x, so its torsion IS a rotation about the global x axis
    and cutting that component cuts the torsional continuity. See
    `_assemble_with_torsional_release`.

    THE FIRST VERSION OF THIS CONTROL READ SIX. The frame put node 4 off-axis, so
    the released component was a global rotation and not the member's twist; no
    mechanism was created and the control passed nothing. That is the reason the
    geometry is what it is, and it is why this control is worth more than the
    gate it guards: it failed first.
    """
    model, els = _frame()
    released = len(els) - 1
    axis = model.nodes[4].xyz - model.nodes[3].xyz
    assert abs(axis[1]) == 0.0 and abs(axis[2]) == 0.0, (
        f"the released member runs {axis}, which is not parallel to global x. "
        "Its torsion is then not the global rx component this control cuts, and "
        "the release would create no mechanism -- which is exactly how the first "
        "version of this control passed while measuring nothing."
    )
    assert els[released] == BeamElement(3, 4, SEC, S355), (
        "the released member is not the tip member this control assumes; the "
        "released twist would then move other members and the extra mode would "
        "not be one."
    )
    k = _assemble_with_torsional_release(model, els, released)
    over = seventh_over_epsilon(k)
    w = _spectrum(k)
    flexible = w[RIGID + 1]
    # BY THE SHIPPED RULE (CT1). A released connection puts a SEVENTH mode at
    # the arithmetic floor, so `lambda_7` cannot clear the bound and the gate
    # must refuse -- which is the same red an over-conditioned frame gets, and
    # deliberately: in double precision the two are the same observation.
    #
    # THE SECOND ASSERTION IS MEASURED SEPARATELY (R420). It read
    # `dim = RIGID + 1 if margin < GAP else RIGID` and then asserted
    # `dim == RIGID + 1` five lines after asserting `margin < GAP`, so it
    # could not fail while the first passed -- a gate carrying its own answer.
    # `zero_modes_under_the_bound` counts the spectrum instead, which is a
    # different measurement and can disagree.
    dim = zero_modes_under_the_bound(k)
    assert over < RIGID_MODE_BOUND, (
        f"a released connection leaves lambda_7 at {over:.4e} units of "
        f"||K_hat||*eps, at or over {RIGID_MODE_BOUND:g}, so the gate would "
        "answer rather than refuse. The seventh mode this control creates is "
        "at zero energy and the bound is supposed to be unable to clear it."
    )
    with capsys.disabled():
        print(
            f"  torsional release: lambda_7 {w[RIGID]:.4e}  lambda_8 "
            f"{flexible:.4e}  nullspace {dim}"
        )
    assert dim == RIGID + 1, (
        f"releasing one member's torsional continuity puts {dim} eigenvalues "
        f"under the bound, not {RIGID + 1}. The mechanism is provable -- that "
        "member can twist rigidly about its own axis at zero energy -- so a "
        "count that does not see exactly one extra is not measuring the "
        "nullspace dimension."
    )


@contextlib.contextmanager
def _nearly_released(size: float, capsys):
    """Patch `assembled` with a connection that is NEARLY released.

    The torsional continuity of the axis-parallel member is cut -- which alone
    puts a SEVENTH mode at the arithmetic floor -- and then given back a
    stiffness of relative `size`. That lifts the seventh clear of round-off
    but leaves it under the bound: a real flexible mode the gate cannot
    certify, which is exactly the state UNDECIDABLE exists for.

    A UNIFORM FOUNDATION WAS THE FIRST ATTEMPT AND IT DOES NOT WORK. It lifts
    all six rigid modes together, so the residual half fails instead --
    measured at every size from `1e-12` to `1e-7`. Nothing brings `lambda_7`
    down towards the floor without touching the six except a defect in the
    connectivity.
    """
    original = globals()["assembled"]

    def defective(model, els):
        k = _assemble_with_torsional_release(model, els, released=6)
        k[-1, -1] += size * float(np.abs(k).max())
        return k

    globals()["assembled"] = defective
    try:
        with capsys.disabled():
            print(f"\n  released one twist and gave back {size:g} of max|K|")
        yield
    finally:
        globals()["assembled"] = original


# CLAIM A'S COUNTER WAS HERE AND IS RETIRED (DI0). Its name is not written out: claim A's counter.
# The
# counter is only meaningful against the assertion it defends, and that assertion is retired.


def test_a_SEVENTH_MODE_UNDER_THE_BOUND_reddens_the_gate(capsys) -> None:
    """`RIGID_MODE_BOUND`'s counter, INJECTED into the assembled matrix.

    A connection NEARLY released leaves `lambda_7` clear of round-off and
    still under the bound: a seventh mode the gate cannot certify as flexible,
    which it must refuse rather than answer about.

    ONE COUNTER, BECAUSE THERE IS ONE CONSTANT (CU0). Two shipped, one per
    retired constant, and the meta-test's cross cell showed each of them
    reddening under EITHER widening -- there was one bound, so there was one
    discrimination to make. The smaller of the two, `2.0e-14`, is also the one
    that sat under the platform spread from the widened bound, so it is the
    larger that carries forward.
    """
    with (
        _nearly_released(RIGID_MODE_BOUND_COUNTER_DEFECT, capsys),
        pytest.raises(AssertionError, match="UNDECIDABLE"),
    ):
        test_there_is_NO_SEVENTH_zero_mode(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_there_is_NO_SEVENTH_zero_mode(capsys)

    # WHY THIS SIZE AND NOT THE OTHER RETIRED ONE, measured here rather than
    # asserted in a comment. Both reddened the two-constant gate. Against one
    # constant the meta-test widens the bound by `WIDEN`, and a counter has to
    # survive that widening by more than the platform spread or it is a
    # counter that could flip on another machine.
    widened = RIGID_MODE_BOUND / 10.0
    with capsys.disabled():
        for label, which in (
            ("shipped  1.0e-13", "bound"),
            ("retired  2.0e-14", "retired_floor"),
        ):
            r = counter_response(which)
            print(
                f"  {label}: lambda_7 {r:.4f} units -- "
                f"{RIGID_MODE_BOUND / r:.4f}x under the bound, "
                f"{r / widened:.4f}x over the widened bound"
            )


# --------------------------------------------------------------------------
# The pin AP3 is about
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# CLAIM A, AS A DIAGNOSTIC (DI0). Computed per element, reported, asserted
# nowhere in F2. In F3 this becomes an assertion on every real platform member
# (R486's gate, F2.md §5e).
# --------------------------------------------------------------------------


def element_rigid_vectors(length: float) -> np.ndarray:
    """`(12, 6)` — the six rigid motions about the ELEMENT'S OWN MIDPOINT.

    Local frame: node A at `-L/2`, node B at `+L/2` along local x. A rotation
    about the midpoint gives each end `cross(axis, r)` of translation and the
    axis itself of rotation. PHYSICALLY RIGID, with no homogenisation applied
    here — dividing the translation by `L/2` while leaving the rotation at 1
    is only a rigid motion when `L/2 == 1`, and that error read `4.3e-02`
    instead of round-off when this was first measured.
    """
    half = length / 2.0
    modes = np.zeros((2 * DOF_PER_NODE, RIGID))
    for d in range(3):
        modes[d, d] = 1.0
        modes[DOF_PER_NODE + d, d] = 1.0
    for a in range(3):
        axis = np.zeros(3)
        axis[a] = 1.0
        for node, x in ((0, -half), (DOF_PER_NODE, +half)):
            arm = np.cross(axis, np.array([x, 0.0, 0.0]))
            modes[node : node + 3, 3 + a] = arm
            modes[node + 3 : node + 6, 3 + a] = axis
    return modes


def element_homogeniser(length: float) -> np.ndarray:
    """`S` as a vector: rotational DOFs scaled by the element length.

    `k_hat = S^-1 k S^-1` and the rigid vector becomes `S r`, so
    `k_hat (S r) = S^-1 (k r)`: a vector annihilated by `k` is annihilated by
    `k_hat`. The transform cannot create or destroy the property under test,
    which is what makes it a homogenisation rather than a second
    normalisation — and `S r`, not `r / S`, which was the second arithmetic
    error in the first measurement of this quantity.
    """
    s = np.ones(2 * DOF_PER_NODE)
    for node in (0, DOF_PER_NODE):
        s[node + 3 : node + 6] = length
    return s


def element_rigid_residual(k_local: np.ndarray, length: float) -> float:
    """`max_j ||k_hat r_hat|| / (||k_hat|| ||r_hat||)` over the six (DI0).

    A DIAGNOSTIC IN F2 AND NOT A GATE, and the reason is measured rather than
    asserted: over the 1592 distinct elements of the reviewer's corpus the
    clean worst is 0.540 eps and frame-independent, but **298 of those 1592
    elements do not redden under at least one of the three counters**. At
    `L/r` of 1e+08 -- or on a member a nanometre long -- the local stiffness
    entries span so many decades that a perturbation of the largest entry
    falls below round-off in the blocks these vectors excite, so the defect is
    invisible for the same reason the clean residual is tiny. Proportions are
    the one axis this form keeps.

    DG2 was pre-registered before the form was measured and it applies: claim
    A is dropped as an F2 gate, no fifth form is proposed, and the platform
    guarantee arrives in F3 on real geometry.
    """
    s = element_homogeniser(length)
    khat = k_local / np.outer(s, s)
    norm = float(np.linalg.norm(khat))
    modes = element_rigid_vectors(length)
    worst = 0.0
    for j in range(RIGID):
        r = modes[:, j] * s
        worst = max(worst, float(np.linalg.norm(khat @ r) / (norm * np.linalg.norm(r))))
    return worst


def test_the_element_local_rigid_residual_is_REPORTED_not_asserted(capsys) -> None:
    """DI0. The diagnostic, over the shipped frame's own elements.

    It prints and it decides nothing. The only assertion here is that the
    quantity is FINITE and frame-independent -- if it ever stopped being
    either, the number in the F3 gate would be meaningless, and that is worth
    catching in F2 even though the value is not gated.
    """
    model, els = _frame()
    seen: dict[tuple, float] = {}
    for el in els:
        length = element_length(model, el)
        k_local = local_stiffness(el.section, el.material, length)
        value = element_rigid_residual(k_local, length)
        assert np.isfinite(value), "the element-local residual is not finite"
        key = (
            length,
            el.section.A,
            el.section.I_y,
            el.section.I_z,
            el.section.J,
            el.material.E,
            el.material.nu,
        )
        if key in seen:
            assert value == seen[key], (
                "the same element read two different values. The quantity is "
                "computed in the element's own frame, so it cannot depend on "
                "anything outside the element -- see "
                "test_the_element_local_residual_is_FRAME_INDEPENDENT."
            )
        seen[key] = value
    with capsys.disabled():
        print(f"\n  element-local rigid residual over {len(seen)} distinct elements:")
        print(f"    worst {max(seen.values()):.4e} = {max(seen.values()) / EPS:.3f} eps")
        print("    DIAGNOSTIC (DI0): reported, asserted nowhere in F2")


def test_the_element_local_residual_is_FRAME_INDEPENDENT(capsys) -> None:
    """The property no assembled form had: the quantity never sees a frame.

    The residual is computed from `k_local` and the element's own length, so
    translating or rotating the model cannot reach it. That is asserted here by
    building the same elements at two different global offsets and requiring
    the values to be identical, not merely close.
    """
    values: dict[tuple, set[float]] = {}
    for offset in ((0.0, 0.0, 0.0), (1.0e3, -4.0e2, 7.0e1)):
        model = Model()
        for xyz in _frame()[0].nodes.coords():
            model.nodes.add(Node(*(xyz + np.array(offset))))
        for el in _frame()[1]:
            length = element_length(model, el)
            value = element_rigid_residual(local_stiffness(el.section, el.material, length), length)
            key = _element_identity(el, length)
            values.setdefault(key, set()).add(value)
    with capsys.disabled():
        print(
            f"\n  {len(values)} distinct elements, both offsets, identical: "
            f"{all(len(v) == 1 for v in values.values())}"
        )
    assert all(len(v) == 1 for v in values.values()), (
        "the same element read different values at two global offsets, which "
        "the quantity's construction forbids -- it is computed in the "
        "element's own frame and never sees a global coordinate."
    )


def _element_identity(el: BeamElement, length: float) -> tuple:
    """What makes two elements the same element, for the check above."""
    return (
        length,
        el.section.A,
        el.section.I_y,
        el.section.I_z,
        el.section.J,
        el.material.E,
        el.material.nu,
    )


def test_a_WEAKER_KEY_reports_a_difference_that_is_not_there(capsys) -> None:
    """The control, and it is my own near-miss turned into a test (DI0).

    Keying element identity on `(length, area)` alone made me report frame
    dependence that did not exist: two circular tubes can carry the SAME area
    and different `I` and `J`, so the weak key grouped two different elements
    and their two different residuals looked like one element disagreeing with
    itself.

    `A = pi * t * (D - t)`, so `(D=0.6, t=0.012)` and `(D=0.318, t=0.024)`
    share an area to round-off while their second moments differ by a factor of
    about three. The weak key must conflate them and the full identity must
    not; if a future change made the weak key adequate, this test says so
    rather than leaving the control quietly vacuous.
    """
    pair = (Section.circular_tube(0.6, 0.012), Section.circular_tube(0.318, 0.024))
    assert abs(pair[0].A - pair[1].A) <= 1e-12 * pair[0].A, (
        f"the two sections no longer share an area ({pair[0].A:.6e} vs "
        f"{pair[1].A:.6e}), so this control is not about a weak key any more."
    )
    assert pair[0].I_y != pair[1].I_y, "the two sections have the same I; pick another pair"

    length = 4.0
    residuals = [element_rigid_residual(local_stiffness(sec, S355, length), length) for sec in pair]
    # A KEY A HUMAN WOULD WRITE, which is the one I wrote: the area compared
    # at the precision a table shows it. The two areas here agree to fifteen
    # digits and differ by a few ulps, so an EXACT float key happens to
    # separate them -- which is luck, not a property, and is why the control
    # keys the way a reader does.
    weak = {(length, float(f"{sec.A:.12e}")) for sec in pair}
    strong = {_element_identity(BeamElement(0, 1, sec, S355), length) for sec in pair}
    with capsys.disabled():
        print(
            f"\n  same area {pair[0].A:.6e}, I_y {pair[0].I_y:.4e} vs "
            f"{pair[1].I_y:.4e} ({pair[1].I_y / pair[0].I_y:.2f}x)"
        )
        print(f"  residuals {residuals[0]:.4e} and {residuals[1]:.4e}")
        print(f"  weak key groups them into {len(weak)}; the full identity into {len(strong)}")
    assert len(weak) == 1, (
        "the weak key did not conflate two different elements, so this control "
        "proves nothing. The two areas agree to twelve decimals by "
        "construction; if that has changed, pick another pair."
    )
    assert pair[0].A != pair[1].A, (
        "the two areas are now bit-identical, which makes the ulp remark above "
        "false -- rewrite it rather than leaving it."
    )
    assert len(strong) == 2, "the full identity conflated two different elements"


# --------------------------------------------------------------------------
# R475's three cells. The residual's normalisation changed at R475, so every
# claim about what it detects is re-measured here rather than inherited.
# --------------------------------------------------------------------------

_SPAN_CELLS = ((1.0, "4 m"), (10.0, "40 m"), (100.0, "400 m"), (1e3, "4 km"), (1e4, "40 km"))
_COUNTER_DOFS = ((0, "translational"), (3, "rotational"))


def _residual_with(k, model, dof: int, size: float) -> float:
    kk = k.copy()
    kk[dof, dof] += size * float(np.abs(k).max())
    return residual_exactness(kk, model)


def _detection_edge(k, model, dof: int) -> float:
    """The defect size at which the gate flips, BISECTED rather than swept.

    Two hundred halvings of a geometric bracket, so the edge is located to
    round-off rather than to the resolution of a sweep -- which is what CO1
    asked for on the other gate's counter and is the same requirement here.
    """
    lo, hi = 1e-18, 1e-6
    for _ in range(200):
        mid = (lo * hi) ** 0.5
        if _residual_with(k, model, dof, mid) > RIGID_MODE_EXACTNESS:
            hi = mid
        else:
            lo = mid
    return hi


# R475'S TEN SPAN CELLS WAS HERE AND IS RETIRED (DI0). Its name is not written out: R475's ten span
# cells. They measured
# the assembled quantity, which R524 then showed crossing the ceiling on defect-free near-vertical
# frames; the span property they proved is real and belongs to a form that is no longer the gate.


# THE REFERENCE-POINT CELL WAS HERE AND IS RETIRED (DI0). Its name is not written out: the reference
# point only enters the
# ASSEMBLED quantity. In the element-local form the vectors are built about the element's own
# midpoint, so there is no global point to depend on -- which is why this cell has nothing left to
# measure.


# ITS STRUCTURAL HALF WAS HERE AND IS RETIRED (DI0). Its name is not written out: the structural
# half
# of the same claim, retired with it.


# THE NEAR-VERTICAL CELL WAS HERE AND IS RETIRED (DI0). Its name is not written out: R525: its
# eleven cells put
# their members at 61.34 down to 55.08 degrees from Z, never near vertical, so it never tested the
# band it was named for. The band is covered by the element-local diagnostic, where it reads 0.007
# to 0.035 eps, and asserted in F3 on real members.


def test_the_ARPACK_path_is_REPRODUCIBLE_under_its_pin(capsys) -> None:
    """AP3. The gate above is dense and has no start vector; ARPACK has one.

    This does not assert that ARPACK's eigenvectors are meaningful inside the
    degenerate block -- AP3 is explicit that they are not, which is why the
    gate reads no eigenvector at all: the subspace form that once answered AP3
    is retired, and the residual answers it without an eigensolve. What this
    asserts is the narrower thing the pin actually buys: two runs of the same
    problem give bit-identical eigenvalues, so a stored result cannot move
    with no code change.
    """
    model, els = _frame()
    k = assemble(model, els).astype(np.float64)
    n = k.shape[0]
    shift = -1.0e-3 * float(abs(k).max())  # not-a-tolerance: a shift off the
    # singular point, so shift-invert is factorisable. Any negative value works;
    # it moves every eigenvalue by a known constant and nothing is compared here
    # against a threshold.
    first = spla.eigsh(
        k, k=RIGID + 2, sigma=shift, which="LM", v0=deterministic_v0(n), return_eigenvectors=False
    )
    second = spla.eigsh(
        k, k=RIGID + 2, sigma=shift, which="LM", v0=deterministic_v0(n), return_eigenvectors=False
    )
    with capsys.disabled():
        print(
            f"  ARPACK under the pin, two runs: max |difference| "
            f"{np.max(np.abs(np.sort(first) - np.sort(second))):.3e}"
        )
    assert np.array_equal(np.sort(first), np.sort(second)), (
        "two ARPACK runs from the same pinned start vector gave different "
        "eigenvalues. The pin is the only thing making this path reproducible, "
        "and it is not doing it."
    )


def test_an_UNPINNED_arpack_start_would_NOT_be_reproducible(capsys) -> None:
    """The control for the pin: without it, the assertion above is vacuous.

    If two unpinned runs happened to agree, the test above would pass whatever
    the pin did. This is the same shape as `test_determinism_pins.py`'s own
    control and it exists for the same reason.
    """
    model, els = _frame()
    k = assemble(model, els).astype(np.float64)
    n = k.shape[0]
    shift = -1.0e-3 * float(abs(k).max())  # not-a-tolerance: see above
    rng = np.random.default_rng()
    runs = [
        np.sort(
            spla.eigsh(
                k,
                k=RIGID + 2,
                sigma=shift,
                which="LM",
                v0=rng.standard_normal(n),
                return_eigenvectors=False,
            )
        )
        for _ in range(2)
    ]
    differs = not np.array_equal(runs[0], runs[1])
    with capsys.disabled():
        print(
            f"  two UNPINNED runs differ: {differs} "
            f"(max |difference| {np.max(np.abs(runs[0] - runs[1])):.3e})"
        )
    if not differs:
        pytest.fail(
            "two unpinned ARPACK runs gave bit-identical eigenvalues, so the "
            "pinned assertion above would pass with the pin removed. This "
            "control is not a skip: it means the reproducibility claim is "
            "currently resting on nothing measurable, and that is a finding."
        )
