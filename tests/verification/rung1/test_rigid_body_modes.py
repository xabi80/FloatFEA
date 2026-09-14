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


def homogenised_spectrum(k: np.ndarray) -> np.ndarray:
    """`|lambda|` in units of the matrix's own round-off floor, `eps * max|lambda|`.

    Below one means "indistinguishable from zero for this matrix". That is
    what makes two frames comparable: the six rigid modes of the shipped frame
    and of its kilometre re-expression both land under one, while their raw
    eigenvalues differ by twelve orders.
    """
    w = np.sort(sla.eigh(k, eigvals_only=True))
    floor = EPS * float(np.max(np.abs(w)))
    return np.abs(w) / floor


def zero_modes_by_gap(k: np.ndarray) -> tuple[int, float]:
    """`(how many modes sit below the largest gap, that gap's ratio)` (Q7).

    THE COUNT COMES FROM THE SPECTRUM'S OWN SHAPE, not from a threshold. A
    threshold on an eigenvalue is a statement about the model's units and
    stiffness; the largest gap is where the nullspace ends, and it is what a
    reader of a nullspace dimension relies on anyway.

    Everything below the round-off floor is clamped TO the floor before the
    ratios are taken: the six zero modes differ from each other only by
    round-off, and dividing two round-off numbers would put the largest gap
    inside the nullspace rather than at its edge.
    """
    h = np.maximum(homogenised_spectrum(k), 1.0)
    ratios = h[1:] / h[:-1]
    i = int(np.argmax(ratios))
    return i + 1, float(ratios[i])


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
    size = (
        RIGID_BODY_MODE_RATIO_COUNTER_DEFECT
        if which == "ratio"
        else RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT
    )
    k[0, 0] += size * float(np.abs(k).max())
    return mode_ratio(k) if which == "ratio" else subspace_loss(k, model)


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


def test_the_ZERO_MODES_NUMBER_SIX_by_the_spectral_gap(capsys) -> None:
    """G2.1's second half: how many, from the spectrum's own shape.

    The count and the gap are two claims and both are asserted. The count is
    what G2.1 is about; the gap is whether the count is worth reading, and a
    count taken across a narrow gap is a coin toss dressed as a measurement.
    """
    model, els = _frame()
    k = assembled(model, els)
    count, gap = zero_modes_by_gap(k)
    with capsys.disabled():
        h = homogenised_spectrum(k)
        print(
            f"  {count} modes below a gap of {gap:.4e} against "
            f"{RIGID_MODE_GAP:g}; homogenised lambda_6 {h[RIGID - 1]:.4e}, "
            f"lambda_7 {h[RIGID]:.4e}"
        )
    assert count == RIGID, (
        f"the largest gap in the homogenised spectrum puts {count} modes below "
        f"it and G2.1 requires {RIGID}. Fewer means a rigid motion is being "
        "resisted; more means the model has a mechanism in it."
    )
    assert gap >= RIGID_MODE_GAP, (
        f"the gap separating the nullspace from the first flexible mode is "
        f"{gap:.4e}, under {RIGID_MODE_GAP:g}. The count above is then being "
        "read across a boundary that is not there."
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
    number three earlier revisions published. Nothing is asserted against it
    and `RIGID_BODY_MODE_RATIO` is now referenced only here.
    """
    model, els = _frame()
    k = assembled(model, els)
    ratio = mode_ratio(k)
    w = _spectrum(k)
    with capsys.disabled():
        print(
            f"  DIAGNOSTIC lambda_6 {w[RIGID - 1]:.4e}  lambda_7 {w[RIGID]:.4e}"
            f"  ratio {ratio:.4e}; the retired ceiling was "
            f"{RIGID_BODY_MODE_RATIO:g}"
        )
    assert math.isfinite(ratio), (
        "the diagnostic ratio is not finite, which means the seventh "
        "eigenvalue is zero and the model has more freedom than G2.1 assumes."
    )


def test_the_analytic_rigid_body_vectors_are_SPANNED(capsys) -> None:
    """G2.1, second half, and the one AP3 says is the real content."""
    model, els = _frame()
    loss = subspace_loss(assembled(model, els), model)
    with capsys.disabled():
        print(
            f"  worst analytic vector outside the computed span: {loss:.4e} "
            f"against {RIGID_BODY_SUBSPACE_LOSS:g}"
        )
    assert loss <= RIGID_BODY_SUBSPACE_LOSS, (
        f"an analytic rigid-body vector has {loss:.4e} of its norm outside the "
        f"computed nullspace, above {RIGID_BODY_SUBSPACE_LOSS:g}. The six "
        "computed modes are at zero energy but they do not span the rigid-body "
        "space, so something else is at zero energy in place of a rigid motion."
    )


# --------------------------------------------------------------------------
# The negative controls, in both directions
# --------------------------------------------------------------------------


def test_ONE_PINNED_DOF_leaves_FIVE(capsys) -> None:
    """Downward control. Fixing one DOF must remove exactly one zero mode.

    Without this, a gate that counted six could be counting six of anything. It
    is run at every single DOF rather than at a chosen one, because a DOF that
    happens to be uncoupled would pass a one-sample version silently.
    """
    model, els = _frame()
    k = assemble_dense(model, els)
    n = k.shape[0]
    counts = []
    for d in range(n):
        keep = np.setdiff1d(np.arange(n), [d])
        w = _spectrum(k[np.ix_(keep, keep)])
        counts.append(int(np.sum(np.abs(w) <= RIGID_BODY_MODE_RATIO * w[RIGID - 1])))
    with capsys.disabled():
        print(f"  one DOF pinned, over all {n}: nullspace dimensions " f"{sorted(set(counts))}")
    assert set(counts) == {RIGID - 1}, (
        f"pinning one DOF gives nullspace dimensions {sorted(set(counts))}, not "
        f"{{{RIGID - 1}}}. A pinned DOF that leaves six means the gate above is "
        "not counting rigid-body modes; one that leaves fewer than five means "
        "the pin removed more freedom than it has."
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
    w = _spectrum(k)
    flexible = w[RIGID + 1]
    dim = int(np.sum(np.abs(w) <= RIGID_BODY_MODE_RATIO * flexible))
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


def test_a_RIGID_BODY_MODE_that_carries_ENERGY_is_caught(capsys) -> None:
    """`RIGID_BODY_MODE_RATIO`'s counter, INJECTED into the assembled matrix.

    A defect of relative size `RIGID_BODY_MODE_RATIO_COUNTER_DEFECT` is added to
    the diagonal of one translational DOF. That is the shape of a real defect --
    a stiffness that resists a rigid translation -- and it lifts the sixth
    eigenvalue off zero. The gate above must redden.

    INJECTED INTO THE MEASURED QUANTITY AND RUN THROUGH THE GATE (BV1/BX0), not
    compared with the constant: a counter that computes a ratio and checks it
    against the ceiling asserts arithmetic on two constants and passes with the
    gate neutered. `tests/test_counters_are_injected.py` registers this pair and
    runs both cells against it.
    """
    with (
        _defect(RIGID_BODY_MODE_RATIO_COUNTER_DEFECT, capsys),
        pytest.raises(AssertionError, match="leaves"),
    ):
        test_the_rigid_body_vectors_are_EXACT_in_the_residual(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_the_rigid_body_vectors_are_EXACT_in_the_residual(capsys)


@contextlib.contextmanager
def _foundation(size: float, capsys):
    """Patch `assembled` with a UNIFORM elastic foundation of relative `size`.

    `size * max|K|` on every diagonal entry: every mode is lifted by the same
    amount, so the six rigid ones rise together and the gap between them and
    the seventh closes without the COUNT changing. That is what makes it the
    gap's counter rather than the count's.

    IT REDDENS THE RESIDUAL TOO, necessarily: anything that lifts a zero mode
    makes that motion carry energy. Said rather than hidden -- what makes this
    the gap's counter is that it is sized on the gap, and the count's own
    controls are the release and the pin, which move the answer instead.
    """
    original = globals()["assembled"]

    def defective(model, els):
        k = original(model, els)
        return k + size * float(np.abs(k).max()) * np.eye(k.shape[0])

    globals()["assembled"] = defective
    try:
        with capsys.disabled():
            print(f"\n  injected a uniform foundation of {size:g} of max|K|")
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


def test_a_CLOSED_GAP_reddens_the_COUNT_assertion(capsys) -> None:
    """`RIGID_MODE_GAP`'s counter, INJECTED into the assembled matrix.

    A uniform foundation lifts all six rigid modes together, so the count
    stays at six and the GAP is what degrades. The gate must redden on the
    gap, which is the half of that test this counter is declared against.
    """
    with (
        _foundation(RIGID_MODE_GAP_COUNTER_DEFECT, capsys),
        pytest.raises(AssertionError, match="separating the nullspace"),
    ):
        test_the_ZERO_MODES_NUMBER_SIX_by_the_spectral_gap(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_the_ZERO_MODES_NUMBER_SIX_by_the_spectral_gap(capsys)


def test_a_LOST_rigid_body_DIRECTION_is_caught(capsys) -> None:
    """`RIGID_BODY_SUBSPACE_LOSS`'s counter, INJECTED into the same matrix.

    The same defect removes a rigid translation from the zero-energy space and
    puts something else there, so the analytic vector for that translation is no
    longer spanned. Measured on the worst of the six, never on a mean.
    """
    with (
        _defect(RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT, capsys),
        pytest.raises(AssertionError, match="outside the computed"),
    ):
        test_the_analytic_rigid_body_vectors_are_SPANNED(capsys)

    # And undefected it passes, so the failure above is the injection.
    test_the_analytic_rigid_body_vectors_are_SPANNED(capsys)


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
