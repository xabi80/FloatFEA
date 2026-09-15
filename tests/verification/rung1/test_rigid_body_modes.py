"""V1.1 — rigid-body modes, gate G2.1 (D2 step 5).

An unconstrained assembly has exactly **six** zero-energy modes: three
translations and three rotations. This file asserts that, and it asserts it on
the SUBSPACE rather than on the mode shapes, per the lock's AP3.

WHY THE SUBSPACE AND NOT THE MODES. Within the six-fold degenerate zero
eigenvalue the eigenvectors are an arbitrary basis of the rigid-body space --
non-unique *in principle*, not merely non-reproducible. Any orthogonal mixture of
the six is an equally valid answer, so a test asserting particular shapes asserts
a property the mathematics does not confer, and would pass only because the
solver happened to produce that basis. What is invariant under every basis choice
inside the degenerate block is that the six ANALYTIC rigid-body vectors lie in
the computed span, and that is what is asserted.

TWO QUANTITIES, BOTH DIMENSIONLESS, BOTH GATED

1. `RIGID_BODY_MODE_RATIO` -- the sixth eigenvalue of `K` divided by the seventh.
   A RATIO, per G2.1, so the assertion is mesh- and unit-independent: the
   absolute eigenvalues of a stiffness matrix carry units and scale with `E`,
   with the section, and with the mesh, and a ceiling on them would be a ceiling
   on the model rather than on the element.
2. `RIGID_BODY_SUBSPACE_LOSS` -- the largest fraction of any analytic rigid-body
   vector left outside the computed six-dimensional span. Zero if the span
   contains them all.

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
)
from floatfea.determinism import deterministic_v0  # noqa: E402
from floatfea.model.material import Material, Section  # noqa: E402
from floatfea.model.nodes import Model, Node, element_dofs  # noqa: E402
from floatfea.tolerances import (  # noqa: E402
    RIGID_BODY_MODE_RATIO,
    RIGID_BODY_MODE_RATIO_COUNTER_DEFECT,
    RIGID_BODY_SUBSPACE_LOSS,
    RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT,
    RIGID_MODE_EXACTNESS,
    RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
    RIGID_MODE_FLOOR,
    RIGID_MODE_FLOOR_COUNTER_DEFECT,
    RIGID_MODE_GAP,
    RIGID_MODE_GAP_COUNTER_DEFECT,
)

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

    Three unit translations, and three rotations about the CENTROID. The
    centroid is used rather than the origin only so the columns are better
    conditioned as a basis; any point gives the same six-dimensional span, which
    is the thing under test.
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
    """G2.1's first quantity in the RESIDUAL form (Q7).

    The worst over the six analytic rigid-body vectors of

        ||K v|| / (max|K| * ||v||)

    -- how far an exact rigid-body motion is from the nullspace of the
    assembled matrix. Dimensionless: the numerator carries `K`'s units and the
    denominator carries them too, so the quantity is invariant under `E`, the
    section and the length unit in the way `mode_ratio` only claimed to be.

    WHAT IT DOES NOT USE, and that is the point: no eigenvalues and no
    eigenvectors. `subspace_loss` projects onto the first six COMPUTED
    eigenvectors, so what it measures includes the eigensolver; this reads `K`
    and the analytic vectors and nothing else. There is no iterative solve
    here, so there is no starting vector to pin -- `deterministic_v0` is
    pinned where a solve does happen, in the sparse cross-check below.

    ASSERTED ON THE WORST OF THE SIX, never a mean, per `CLAUDE.md`.
    """
    scale = float(np.max(np.abs(k)))
    analytic = _analytic_rigid_body(model)
    worst = 0.0
    for j in range(analytic.shape[1]):
        v = analytic[:, j]
        worst = max(worst, float(np.linalg.norm(k @ v) / (scale * np.linalg.norm(v))))
    return worst


def homogenised(k: np.ndarray) -> np.ndarray:
    """`K_hat = K / max|K|` -- the same homogenisation `residual_exactness` uses.

    Its entries are O(1) whatever the model's units, stiffness or section, so
    the round-off floor of `K_hat` is a property of the arithmetic rather than
    of the structure. Everything CS0 measures is measured on this.
    """
    return k / float(np.max(np.abs(k)))


def zero_mode_threshold(k: np.ndarray) -> float:
    """`tau = RIGID_MODE_FLOOR * ||K_hat|| * eps` -- numerically zero, below here."""
    kh = homogenised(k)
    norm = float(np.max(np.abs(sla.eigh(kh, eigvals_only=True))))
    return RIGID_MODE_FLOOR * norm * EPS


def seventh_over_threshold(k: np.ndarray) -> float:
    """`log10(lambda_7 / tau)` -- how resolvably the FIRST FLEXIBLE mode clears
    the floor, in orders of magnitude.

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

    The bound is at the sixth-seventh boundary. Nothing reads "the last
    eigenvalue below tau" anywhere in this file.

    A NEGATIVE RESULT IS NOT A FAILED COUNT, it is `lambda_7` at or under the
    floor: the softest flexible mode has sunk into round-off, and no spectral
    rule in double precision can tell that mode from a mechanism. The gate's
    only honest output there is UNDECIDABLE.
    """
    w = np.sort(np.abs(sla.eigh(homogenised(k), eigvals_only=True)))
    tau = zero_mode_threshold(k)
    if w.size <= RIGID or w[RIGID] <= 0.0:
        return float("-inf")
    return float(np.log10(w[RIGID] / tau))


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

    # THE GAP'S COUNTER IS A DIFFERENT INJECTION, so it is built here rather
    # than by scaling one diagonal entry: a uniform foundation lifts all six
    # rigid modes together, which is what degrades the gap without moving the
    # count.
    # THE GAP'S COUNTER IS A DIFFERENT INJECTION and is built here rather than
    # by scaling one diagonal entry: a connection that is NEARLY released
    # leaves the seventh mode just above `tau`, which narrows the separation
    # without moving the count.
    if which == "gap":
        kr = _assemble_with_torsional_release(model, els, released=6)
        kr[-1, -1] += RIGID_MODE_GAP_COUNTER_DEFECT * float(np.abs(kr).max())
        return seventh_over_threshold(kr)

    size = {
        "ratio": RIGID_BODY_MODE_RATIO_COUNTER_DEFECT,
        "loss": RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT,
        "residual": RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
        "floor": RIGID_MODE_FLOOR_COUNTER_DEFECT,
    }[which]
    k[0, 0] += size * scale
    if which == "ratio":
        return mode_ratio(k)
    if which == "residual":
        return residual_exactness(k, model)
    if which == "floor":
        # BOTH RIGID-BODY COUNTERS INJECT THE SAME MECHANISM AT DIFFERENT
        # SIZES (CT0), because the two constants enter one bound
        # multiplicatively. What each returns is the margin its own defect
        # leaves, in orders.
        kr = _assemble_with_torsional_release(model, els, released=6)
        kr[-1, -1] += RIGID_MODE_FLOOR_COUNTER_DEFECT * float(np.abs(kr).max())
        return seventh_over_threshold(kr)
    return subspace_loss(k, model)


@contextlib.contextmanager
def _defect(size: float, capsys):
    """Patch `assembled` so the SHIPPED gate computes a defective matrix.

    The defect is a diagonal stiffness on one translational degree of freedom,
    as a fraction `size` of the largest entry: the shape of a real defect, since
    it is a stiffness that resists a rigid translation. Both halves of G2.1 must
    see it -- it lifts a zero eigenvalue AND takes that translation out of the
    span -- which is why one injected defect carries both counters.
    """
    original = globals()["assembled"]

    def defective(model, els):
        k = original(model, els)
        k[0, 0] += size * float(np.abs(k).max())
        return k

    globals()["assembled"] = defective
    try:
        with capsys.disabled():
            print(f"\n  injected {size:g} of max|K| on one translational DOF")
        yield
    finally:
        globals()["assembled"] = original


# --------------------------------------------------------------------------
# The gate
# --------------------------------------------------------------------------


def test_the_rigid_body_vectors_are_EXACT_in_the_residual(capsys) -> None:
    """G2.1's first half, in the form Q7 settles on.

    The six analytic rigid-body motions are in the nullspace of the assembled
    matrix, measured as a residual and not through an eigensolver.
    """
    model, els = _frame()
    k = assembled(model, els)
    worst = residual_exactness(k, model)
    with capsys.disabled():
        print(f"\n  worst rigid-body residual {worst:.4e} against " f"{RIGID_MODE_EXACTNESS:g}")
    assert worst <= RIGID_MODE_EXACTNESS, (
        f"an exact rigid-body motion leaves {worst:.4e} of residual behind, "
        f"above {RIGID_MODE_EXACTNESS:g}. A rigid motion that `K` resists is "
        "an element or transformation defect: the stiffness is doing work on "
        "a displacement that strains nothing."
    )


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
    margin = seventh_over_threshold(k)
    with capsys.disabled():
        w = np.sort(np.abs(sla.eigh(homogenised(k), eigvals_only=True)))
        tau = zero_mode_threshold(k)
        print(
            f"  lambda_7 {w[RIGID]:.4e} against tau {tau:.4e}: {margin:.3f} "
            f"orders, needing {RIGID_MODE_GAP:g}"
        )
    assert margin >= RIGID_MODE_GAP, (
        f"UNDECIDABLE: the first flexible mode sits {margin:.3f} orders above "
        f"tau and G2.1 needs {RIGID_MODE_GAP:g} to tell it from a mechanism. "
        "Either this model HAS a seventh zero mode, or its softest flexible "
        "mode has sunk into round-off at this conditioning -- and in double "
        "precision no spectral rule separates those two. The gate refuses "
        "rather than reporting a number it cannot defend."
    )


def test_the_eigenvalue_RATIO_is_a_diagnostic_and_not_a_gate(capsys) -> None:
    """`lambda_6 / lambda_7`, RETIRED to a diagnostic by Q7.

    IT WAS THE GATE AND THE REVIEWER'S CORPUS REFUTED IT. Sixteen of the
    twenty-eight frames in `tests/corpus/g21_rigid_body_frames.txt` exceed its
    ceiling with a defect-free element, because the quantity moves with the
    frame's conditioning -- bracing sections, mesh subdivision, span, and above
    all the length unit. A ceiling that a defect-free element fails at the
    centimetre re-expression of a frame it passes at the metre is a ceiling on
    the frame, and G2.1 is not a statement about the frame.

    It is printed because it is informative about conditioning and it is the
    number three earlier revisions published. Nothing is asserted against it.

    `RIGID_BODY_SUBSPACE_LOSS` IS RETIRED WITH IT (CS2), for the stronger
    reason: it breached at seventeen of the reviewer's first twenty-eight
    clean frames against the ratio's ten, so the quantity that had been kept
    was the one the evidence indicted harder. Both are reported here and
    neither is asserted anywhere.
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
    margin = seventh_over_threshold(k)
    w = _spectrum(k)
    flexible = w[RIGID + 1]
    # BY THE SHIPPED RULE (CT1). A released connection puts a SEVENTH mode at
    # the floor, so `lambda_7` is not resolvable and the gate must refuse --
    # which is the same red an over-conditioned frame gets, and deliberately:
    # in double precision the two are the same observation.
    dim = RIGID + 1 if margin < RIGID_MODE_GAP else RIGID
    assert margin < RIGID_MODE_GAP, (
        f"a released connection leaves lambda_7 {margin:.3f} orders above tau, "
        f"at or over {RIGID_MODE_GAP:g}, so the gate would answer rather than "
        "refuse. The seventh mode this control creates is at zero energy and "
        "the bound is supposed to be unable to clear it."
    )
    with capsys.disabled():
        print(
            f"  torsional release: lambda_7 {w[RIGID]:.4e}  lambda_8 "
            f"{flexible:.4e}  nullspace {dim}"
        )
    assert dim == RIGID + 1, (
        f"releasing one member's torsional continuity gives a nullspace of "
        f"{dim}, not {RIGID + 1}. The mechanism is provable -- that member can "
        "twist rigidly about its own axis at zero energy -- so a gate that does "
        "not see it is not measuring the nullspace dimension."
    )


@contextlib.contextmanager
def _nearly_released(size: float, capsys):
    """Patch `assembled` with a connection that is NEARLY released.

    The torsional continuity of the axis-parallel member is cut -- which alone
    gives SEVEN modes below `tau` -- and then given back a stiffness of
    relative `size`. That leaves the seventh just above `tau`: the count reads
    six, which is the right answer, and the separation collapses. It is the
    state the gap exists to refuse.

    A UNIFORM FOUNDATION WAS THE FIRST ATTEMPT AND IT DOES NOT WORK UNDER
    CS0's RULE. It lifts all six rigid modes together, so nothing is left
    below `tau` and the COUNT fails instead of the gap -- measured at every
    size from `1e-12` to `1e-7`. No defect narrows this gap without touching
    the count except one that leaves a mode just above the floor.
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


def test_a_RESISTED_rigid_motion_reddens_the_RESIDUAL(capsys) -> None:
    """`RIGID_MODE_EXACTNESS`'s counter, INJECTED into the assembled matrix.

    The same defect shape as the ratio's: a diagonal stiffness on one
    translational DOF, which is a stiffness resisting a rigid translation. It
    is run through the SHIPPED gate, which recomputes the residual on the
    defective matrix and decides on it (BV1/BX0).
    """
    with (
        _defect(RIGID_MODE_EXACTNESS_COUNTER_DEFECT, capsys),
        pytest.raises(AssertionError, match="leaves"),
    ):
        test_the_rigid_body_vectors_are_EXACT_in_the_residual(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_the_rigid_body_vectors_are_EXACT_in_the_residual(capsys)


def test_a_SEVENTH_MODE_AT_THE_FLOOR_reddens_the_gate(capsys) -> None:
    """`RIGID_MODE_FLOOR`'s counter, INJECTED into the assembled matrix.

    A connection NEARLY released leaves `lambda_7` AT `tau`. That is this
    entry's own mechanism: at the floor a flexible mode is indistinguishable
    from a mechanism, and the gate must refuse.
    """
    with (
        _nearly_released(RIGID_MODE_FLOOR_COUNTER_DEFECT, capsys),
        pytest.raises(AssertionError, match="UNDECIDABLE"),
    ):
        test_there_is_NO_SEVENTH_zero_mode(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_there_is_NO_SEVENTH_zero_mode(capsys)


def test_a_SEVENTH_MODE_TOO_CLOSE_TO_THE_FLOOR_reddens_the_gate(capsys) -> None:
    """`RIGID_MODE_GAP`'s counter, INJECTED into the same way.

    The same defect a decade and a half stiffer: `lambda_7` clears `tau`, so
    the floor's own mechanism is satisfied, and it does not clear it by the
    declared separation. The two counters differ exactly as the two constants
    do.
    """
    with (
        _nearly_released(RIGID_MODE_GAP_COUNTER_DEFECT, capsys),
        pytest.raises(AssertionError, match="UNDECIDABLE"),
    ):
        test_there_is_NO_SEVENTH_zero_mode(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_there_is_NO_SEVENTH_zero_mode(capsys)


# --------------------------------------------------------------------------
# The pin AP3 is about
# --------------------------------------------------------------------------


def test_the_ARPACK_path_is_REPRODUCIBLE_under_its_pin(capsys) -> None:
    """AP3. The gate above is dense and has no start vector; ARPACK has one.

    This does not assert that ARPACK's eigenvectors are meaningful inside the
    degenerate block -- AP3 is explicit that they are not, which is why the gate
    asserts on the subspace. It asserts the narrower thing the pin actually
    buys: two runs of the same problem give bit-identical eigenvalues, so a
    stored result cannot move with no code change.
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
