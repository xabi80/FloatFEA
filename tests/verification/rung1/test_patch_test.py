"""V1.2 / G2.2 — the patch test. FOUR constant-strain states, all EXACT (AW4).

Form
----
**Displacement-driven, per Irons.** The exact field is imposed on the two end
nodes; the interior nodes are free and carry **zero load**; the interior response
must reproduce the exact field.

The load-driven alternative is an equilibrium test wearing the patch test's name.
It does not exercise connectivity the way the displacement-driven form does, and
connectivity is the whole reason V1.2 sits at rung 1: a patch-test failure makes
every accuracy comparison above it uninterpretable.

**Unequal element lengths**, as standard practice for patch tests. Note that the
benefit is *not* demonstrated for this gate: a controlled measurement holding the
perturbed element's length and position fixed found commensurability worth
nothing: across draws the ratio to a UNIFORM mesh spans roughly 0.85-1.09, i.e.
both sides of 1. See `docs/instrumentation.md` on what was withdrawn. The mesh
stays irregular because it costs nothing, not because it was measured to help.

**Straight member only.** A non-collinear assembly is a frame test and belongs at
V2.4. Both an axis-aligned and a skew-but-straight orientation are run, so the
transform is in the loop without the test becoming a frame test.

The four states
---------------
For a Timoshenko beam with ``V = kappa G A (v' - phi)`` and ``M = EI phi'``:

1. **constant axial strain**   ``u = eps x``
2. **constant curvature**      ``phi = c x``, ``v = c x^2 / 2``, zero shear
3. **constant twist**          ``rx = tau x``
4. **constant shear, linear moment**
   ``phi = P(Lx - x^2/2)/EI``, ``v = P(Lx^2/2 - x^3/6)/EI + Px/(kappa G A)``

States 2 and 4 are required **in each bending plane** (locked plan, AV4 item 2),
so there are six in total. The x-z versions carry the sign flip ``w' = -phi_y``:
``phi_y = c x`` with ``w = -c x^2 / 2``, and the shear analogue with the rotation
negated.

**The x-z pair was missing until R1.** All four original states lived in local DOF
``{0}``, ``{3}`` and ``{1,5}``; local DOF ``{2,4,8,10}`` -- the block ``beam.py``
builds as ``flip @ ky @ flip`` -- was identically zero in every state and in both
orientations, because the skew direction rotates the *global* field without giving
the *local* field any x-z content. G2.2 was passing on half the element's bending
stiffness. That is assertion-domain blindness: the collection the assertion
inspected could not contain the failure.

State 4 is the one that matters. It is the only state whose exact solution
contains the shear term, so it is where an element that is *convergent* rather
than *nodally exact* leaves a non-zero interior residual. **That residual is the
test.** The other three states are satisfied by formulations that fail state 4.

Exactness is asserted at ULP scale, per AU4 — not convergence. An element that
reproduces constant curvature only in the limit is passing a convergence test
wearing the patch test's clothes.
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.assemble.system import BeamElement, assemble, solve
from floatfea.element.transform import rotation_matrix
from floatfea.model.material import S355, Section
from floatfea.model.nodes import Model, Node, node_dofs
from floatfea.tolerances import PATCH_TEST_EXACTNESS, PATCH_TEST_EXACTNESS_COUNTER
from floatfea.testing import assert_close, assert_differs
from floatfea.tolerances import COND_UNIT_INVARIANCE, ROUNDOFF_IDENTITY

SEC = Section.circular_tube(0.6, 0.012)
# Irregular: no pair of element lengths in a SMALL-INTEGER RATIO. Lengths
# [3.27, 3.00, 0.90, 0.79, 1.71]; the closest pairwise ratio to p/q with p,q <= 5
# is 0.0877. Kept as standard practice -- a controlled measurement found the
# property itself worth nothing for this gate (R3, docs/instrumentation.md).
STATIONS = np.array([0.0, 3.27, 6.27, 7.17, 7.96, 9.67])
AXIS_ALIGNED = np.array([1.0, 0.0, 0.0])
SKEW = np.array([1.0, 0.35, 0.22]) / np.linalg.norm(np.array([1.0, 0.35, 0.22]))


def _model(direction: np.ndarray) -> tuple[Model, list[BeamElement], np.ndarray]:
    m = Model()
    for s in STATIONS:
        m.nodes.add(Node(*(s * direction)))
    els = [BeamElement(i, i + 1, SEC, S355) for i in range(len(STATIONS) - 1)]
    a, b = m.nodes[0].xyz, m.nodes[1].xyz
    return m, els, rotation_matrix(a, b)


def _exact_local(state: str, x: np.ndarray) -> np.ndarray:
    """(n_nodes, 6) exact LOCAL displacement for a constant-strain state."""
    ei = S355.E * SEC.I_z
    kga = SEC.kappa(S355) * S355.G * SEC.A
    u = np.zeros((x.size, 6))
    if state == "axial":
        u[:, 0] = 1.0e-4 * x
    elif state == "curvature":
        c = 2.0e-4
        u[:, 1] = c * x**2 / 2.0
        u[:, 5] = c * x
    elif state == "twist":
        u[:, 3] = 3.0e-5 * x
    elif state == "shear":
        p, ll = 1.0e5, STATIONS[-1]
        u[:, 1] = p * (ll * x**2 / 2.0 - x**3 / 6.0) / ei + p * x / kga
        u[:, 5] = p * (ll * x - x**2 / 2.0) / ei
    elif state == "curvature_xz":
        # x-z plane. `w' = -phi_y`, so a positive curvature about +y bends the
        # member the other way in w -- the sign the x-y states cannot see.
        c = 2.0e-4
        u[:, 2] = -c * x**2 / 2.0
        u[:, 4] = c * x
    elif state == "shear_xz":
        # Constant shear in x-z, with its linear moment. Same field as `shear`
        # with the rotation negated, per `w' = -phi_y`; EI uses I_y.
        p, ll = 1.0e5, STATIONS[-1]
        ei_y = S355.E * SEC.I_y
        u[:, 2] = p * (ll * x**2 / 2.0 - x**3 / 6.0) / ei_y + p * x / kga
        u[:, 4] = -p * (ll * x - x**2 / 2.0) / ei_y
    else:  # pragma: no cover
        raise ValueError(state)
    return u


def _to_global(u_local: np.ndarray, r: np.ndarray) -> np.ndarray:
    """Rotate each node's (translation, rotation) pair into global axes."""
    out = np.empty_like(u_local)
    out[:, :3] = u_local[:, :3] @ r
    out[:, 3:] = u_local[:, 3:] @ r
    return out


# Local DOF owned by each independent block of the element. In local axes the
# 12x12 is block-diagonal (asserted in tests/unit/test_beam_element.py), so a
# perturbation confined to one block is a defect confined to one physical
# behaviour -- which is what a negative control for a single plane needs.
LOCAL_BLOCKS = {
    "axial": (0, 6),
    "torsion": (3, 9),
    "bending_xy": (1, 5, 7, 11),
    "bending_xz": (2, 4, 8, 10),
}


def relative_error(got, exact, char_length: float) -> float:
    """Dimensionally homogeneous relative error over a (n_nodes, 6) field.

    Taking `max()` across all six DOF mixes metres with radians, which makes the
    measure itself unit-dependent: under a length-unit factor S the translations
    scale by S and the rotations do not, so a spurious rotation divided by a
    translational scale grows with S while the solve is untouched. Measured, the
    axial state -- whose exact rotations are exactly zero -- breached the ceiling
    by 2.8x in kilometres for precisely this reason.

    Rotations are converted to equivalent translations through `char_length`
    before the norm is taken. Extracted as a function so the property can be
    tested by BEHAVIOUR rather than by inspecting how the weighting is spelled
    (R9): a structural check for `w[3:]` is satisfied by `w[3:] = 0.0 * L`.
    """
    import numpy as _np

    w = _np.ones(6)
    w[3:] = char_length
    return float((_np.abs(got - exact) * w).max() / (_np.abs(exact) * w).max())


def _run(
    state: str,
    direction: np.ndarray,
    stiffness_scale: float = 1.0,
    block: str | None = None,
):
    """Solve the patch test. `stiffness_scale` perturbs element 1 -- the whole
    element by default, or only `block`'s local entries when named."""
    m, els, r = _model(direction)
    u_ex = _to_global(_exact_local(state, STATIONS), r)

    k = assemble(m, els)
    if stiffness_scale != 1.0:
        from floatfea.assemble.system import element_global_stiffness, element_length
        from floatfea.element.beam import local_stiffness
        from floatfea.element.transform import rotation_matrix, to_global

        if block is None:
            kb = element_global_stiffness(m, els[1])
            delta = (stiffness_scale - 1.0) * kb
        else:
            # Scale one LOCAL block, then transform -- so the defect stays in the
            # physical behaviour named, not spread across the global matrix.
            e = els[1]
            k_loc = local_stiffness(e.section, e.material, element_length(m, e))
            idx = list(LOCAL_BLOCKS[block])
            pert = np.zeros_like(k_loc)
            pert[np.ix_(idx, idx)] = (stiffness_scale - 1.0) * k_loc[np.ix_(idx, idx)]
            rot = rotation_matrix(m.nodes[e.node_a].xyz, m.nodes[e.node_b].xyz,
                                  orientation_node=e.orientation_node,
                                  roll_rad=e.roll_rad)
            delta = to_global(pert, rot)

        k = k.tolil()
        d = np.concatenate([node_dofs(1), node_dofs(2)])
        for i in range(12):
            for j in range(12):
                k[d[i], d[j]] += delta[i, j]
        k = k.tocsr()

    n_nodes = len(STATIONS)
    ends = np.concatenate([node_dofs(0), node_dofs(n_nodes - 1)])
    # Prescribed end displacements enter as an equivalent load on the free DOF.
    u_pres = np.zeros(m.n_dof)
    u_pres[node_dofs(0)] = u_ex[0]
    u_pres[node_dofs(n_nodes - 1)] = u_ex[-1]
    f = -(k @ u_pres)
    f[ends] = 0.0

    res = solve(k, f, ends)
    u = res.u + u_pres
    got = u.reshape(n_nodes, 6)

    err = relative_error(got, u_ex, STATIONS[-1])
    return err, res


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
@pytest.mark.parametrize("orientation", ["axis_aligned", "skew"])
def test_the_four_constant_strain_states_are_EXACT(state: str, orientation: str) -> None:
    """G2.2. Exactness at ULP scale, not convergence."""
    d = AXIS_ALIGNED if orientation == "axis_aligned" else SKEW
    err, res = _run(state, d)
    assert err <= PATCH_TEST_EXACTNESS, (
        f"{state}/{orientation}: interior nodes deviate from the exact field by "
        f"{err:.3e}, above {PATCH_TEST_EXACTNESS:.0e}. This is a patch-test "
        "failure -- every accuracy comparison above rung 1 is uninterpretable "
        "until it is fixed, and refinement is not the response."
    )
    assert res.residual <= PATCH_TEST_EXACTNESS


def test_the_mesh_is_actually_irregular() -> None:
    """The mesh has the property the module claims for it.

    Kept, but note what it does NOT establish: controlled measurement found
    commensurability worth nothing for this gate, the ratio to a uniform mesh
    straddling 1 across draws. This asserts the stated property holds, not that
    the property buys sensitivity.
    """
    lengths = np.diff(STATIONS)
    assert len(set(np.round(lengths, 9))) == len(lengths), "element lengths repeat"

    # IRREGULAR MEANS NO SMALL-INTEGER RATIO, not merely no equal pair and no 2:1
    # (AX1). A 3:2 pair cancels by symmetry in some node patterns just as a 2:1
    # pair does, so checking only the ratios previously met would make this a test
    # of two known defects rather than of the property. Both earlier meshes passed
    # the narrower check and failed this one.
    worst = 1e9
    for i, a in enumerate(lengths):
        for j, b in enumerate(lengths):
            if i == j or a < b:
                continue
            ratio = a / b
            for q in range(1, 6):
                for pp in range(1, 6):
                    worst = min(worst, abs(ratio - pp / q))
    assert worst > 0.05, (  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small
        f"some pair of element lengths sits {worst:.4f} from a small-integer "
        "ratio; errors can cancel by symmetry on such a mesh"
    )


def test_the_shear_state_actually_contains_shear() -> None:
    """State 4 is the discriminating one only if its shear term is non-trivial.

    If `P x / (kappa G A)` were negligible against the bending term, state 4
    would degenerate into state 2 and the patch test would lose the state that
    distinguishes a nodally exact element from a merely convergent one.
    """
    ei = S355.E * SEC.I_z
    kga = SEC.kappa(S355) * S355.G * SEC.A
    p, ll = 1.0e5, STATIONS[-1]
    bending = p * (ll * ll**2 / 2.0 - ll**3 / 6.0) / ei
    shear = p * ll / kga
    assert shear / (bending + shear) > 1e-4, "shear term is negligible in state 4"  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small


# Detection thresholds, MEASURED (AX1). A counter-case is one perturbation; the
# threshold is where the state stops seeing one at all, and it is the number a
# later reader needs to judge whether a tolerance change has cost detection.
#
#   state         sensitivity (err/eps)   smallest eps detected at 1e-12
#   axial                1.0908e-01              9.17e-12
#   curvature            1.0764e-01              9.29e-12   <- weakest
#   twist                1.0908e-01              9.17e-12
#   shear                1.1743e-01              8.52e-12
#   curvature_xz         1.0764e-01              9.29e-12
#   shear_xz             1.1743e-01              8.52e-12
#
# All six regenerated by running the shipped tests (R14). The bending states'
# sensitivities were previously understated at 3.72e-02 / 3.02e-02 because their
# rotational error was divided by a translational scale; under the homogeneous
# measure all six respond at ~1.1e-01 and the weakest threshold is 8.52e-12.
#
# NOTE what is NOT claimed here. An earlier version of this block said removing
# mesh commensurability improved detection "about FIVEFOLD". That is WITHDRAWN --
# see docs/instrumentation.md. The comparison was uncontrolled.
DETECTION_THRESHOLD = {
    "axial": 9.17e-12,
    "curvature": 9.29e-12,
    "twist": 9.17e-12,
    "shear": 8.52e-12,
    "curvature_xz": 9.29e-12,
    "shear_xz": 8.52e-12,
}


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
def test_the_measured_detection_threshold_still_holds(state: str) -> None:
    """The threshold is a recorded property of the gate, so it is asserted.

    If a formulation change alters sensitivity, this fails and the recorded
    numbers get revisited -- rather than silently ceasing to describe the gate.
    """
    eps = DETECTION_THRESHOLD[state]
    err, _ = _run(state, SKEW, stiffness_scale=1.0 + eps)
    assert err == pytest.approx(PATCH_TEST_EXACTNESS, rel=0.05), (
        f"{state}: perturbing by the recorded threshold {eps:.3e} gave {err:.3e}, "
        f"not the declared ceiling {PATCH_TEST_EXACTNESS:.0e}. The gate's "
        "sensitivity has changed and the recorded thresholds are stale."
    )


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
def test_a_perturbed_element_BREAKS_the_patch_test(state: str) -> None:
    """Negative control, per state.

    A patch test that cannot fail certifies connectivity rather than testing it.
    One interior element's stiffness is perturbed -- the defect a wrong length or
    a wrong section produces -- and every state must detect it.
    """
    err, _ = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-6)
    assert err >= PATCH_TEST_EXACTNESS_COUNTER, (
        f"{state}: a 1e-6 stiffness error in one element moved the interior "
        f"field by only {err:.3e}, below the counter-case "
        f"{PATCH_TEST_EXACTNESS_COUNTER:.3e}"
    )


# ---------------------------------------------------------------------------
# R1's negative control: a defect confined to ONE bending plane.
#
# The whole-element control above cannot show that a plane is covered, because
# every state responds to a whole-element scaling. Confining the perturbation to
# one local block is what demonstrates that the x-z states are actually loading
# the x-z stiffness -- and that they were needed.
# ---------------------------------------------------------------------------
PLANE_STATES = {
    "bending_xy": ("curvature", "shear"),
    "bending_xz": ("curvature_xz", "shear_xz"),
}


@pytest.mark.parametrize("block", ["bending_xy", "bending_xz"])
def test_a_defect_in_ONE_bending_plane_is_caught_by_THAT_plane(block: str) -> None:
    """Each plane's states detect a defect confined to their own block."""
    for state in PLANE_STATES[block]:
        err, _ = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-3, block=block)
        assert err >= PATCH_TEST_EXACTNESS_COUNTER, (
            f"{state} did not detect a 1e-3 defect confined to {block}: "
            f"{err:.3e} < {PATCH_TEST_EXACTNESS_COUNTER:.3e}"
        )


@pytest.mark.parametrize("block", ["bending_xy", "bending_xz"])
def test_the_OTHER_plane_is_blind_to_it(block: str) -> None:
    """The mirror, and the reason R1 was possible.

    A defect confined to one bending plane is invisible to every state outside
    it. That is not a flaw -- it is why both planes need their own states, and
    it is the property that made the x-z block untested while four states passed.
    Asserted so the coverage argument rests on a measurement.
    """
    other = "bending_xz" if block == "bending_xy" else "bending_xy"
    for state in PLANE_STATES[other] + ("axial", "twist"):
        err, _ = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-3, block=block)
        assert err <= PATCH_TEST_EXACTNESS, (
            f"{state} responded to a defect confined to {block} ({err:.3e}); the "
            "blocks are not independent and the local matrix is not block-diagonal"
        )


# ---------------------------------------------------------------------------
# R2: unit invariance. Not V1.3 -- that gate poses a scaled problem and checks
# the RESULTS scale correctly. This checks the weaker property V1.3 depends on:
# that the achievable accuracy, and therefore this gate's ceiling, does not move
# with the length unit.
#
# WHAT CLOSED IT: the ERROR MEASURE alone, necessary and sufficient by ablation.
# Equilibration was briefly added to the solve on a claim that two fixes were
# required; that claim is refuted and the change is reverted (BD2). The
# conditioning tests below exercise `equilibrate` as a utility, which is what it
# now is.
# ---------------------------------------------------------------------------
UNIT_SCALES = [1.0, 10.0, 1000.0, 0.001]      # metres, decimetres, mm, km


def _scaled_model(scale: float):
    """The same physical beam posed with lengths x `scale`."""
    from floatfea import basis
    from floatfea.model.material import Material

    mat = Material(E=basis.E_STEEL / scale**2, nu=basis.NU_STEEL,
                   rho=basis.RHO_STEEL, fy=basis.FY_S355, name="scaled")
    sec = Section.circular_tube(0.6 * scale, 0.012 * scale)
    m = Model()
    for st in STATIONS * scale:
        m.nodes.add(Node(*(st * SKEW)))
    els = [BeamElement(i, i + 1, sec, mat) for i in range(len(STATIONS) - 1)]
    return m, els


@pytest.mark.parametrize("scale", UNIT_SCALES)
def test_the_equilibrated_conditioning_is_unit_INVARIANT(scale: float) -> None:
    """`cond(D^-1/2 K D^-1/2)` is the same number in every length unit.

    This is the algebraic fact the equilibrated solve rests on: for diagonal `S`,
    `diag(SKS) = S diag(K) S`, so the scaled matrix is invariant. Without it the
    conditioning is a property of the unit system rather than of the problem --
    measured, `cond(K_ff)` runs 9.2e2 to 6.0e8 over these scales.
    """
    from floatfea.assemble.system import equilibrate

    ref_m, ref_els = _scaled_model(1.0)
    m, els = _scaled_model(scale)
    ends = np.concatenate([node_dofs(0), node_dofs(len(STATIONS) - 1)])
    free = np.setdiff1d(np.arange(m.n_dof), ends)

    def cond_eq(model, elements):
        kff = assemble(model, elements)[free][:, free].tocsc()
        return float(np.linalg.cond(equilibrate(kff)[0].toarray()))

    assert cond_eq(m, els) == pytest.approx(cond_eq(ref_m, ref_els), rel=COND_UNIT_INVARIANCE), (
        "the equilibrated conditioning moved with the length unit; the solve is "
        "not unit-robust and every exactness ceiling above it is unit-dependent"
    )


def test_the_UNequilibrated_conditioning_DOES_move() -> None:
    """Negative control: if it did not, equilibration would be ceremony."""
    ends = np.concatenate([node_dofs(0), node_dofs(len(STATIONS) - 1)])
    conds = []
    for scale in UNIT_SCALES:
        m, els = _scaled_model(scale)
        free = np.setdiff1d(np.arange(m.n_dof), ends)
        conds.append(np.linalg.cond(assemble(m, els)[free][:, free].toarray()))
    assert max(conds) / min(conds) > 1e4, (  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small
        f"cond(K_ff) spans only {max(conds) / min(conds):.1e} across "
        "these unit systems; this test cannot demonstrate what equilibration is for"
    )


def _synthetic(scale: float):
    """A field and an error posed at length-unit factor `scale`.

    Faithful to how the real failure arises, which a first version of this was
    not. The ERROR is solve round-off concentrated in the rotational DOF, and
    round-off does NOT scale with the unit system -- it is set by the
    conditioning. The FIELD's translations do scale. Scaling the error along with
    the field, as the first version did, makes even the mixed measure invariant
    and the control demonstrates nothing.
    """
    rng = np.random.default_rng(4)
    exact = np.abs(rng.standard_normal((6, 6))) + 0.5
    exact[:, 3:] *= 1.0e-3                 # rotations are small, in radians
    exact[:, :3] *= scale                  # translations carry the length unit
    err = np.zeros((6, 6))
    err[:, 3:] = 1.0e-12                   # round-off, absolute, unit-independent
    return exact + err, exact


def test_the_error_measure_is_UNIT_INVARIANT() -> None:
    """R9/BD3: the property, by behaviour, on an O(1) quantity.

    **The comparison is the RATIO between unit systems against 1**, not two 1e-12
    numbers against each other. Both earlier attempts compared quantities the
    comparison could not resolve: the second used `pytest.approx(mm, rel=1e-12)`,
    whose undeclared default `abs=1e-12` is larger than the operands, so the
    pre-R2 mixed measure passed it while drifting 1000x.

    `assert_close` refuses operands within 100x of the stated floor, so that
    failure mode raises on construction instead of passing.
    """
    lc = 9.67
    m = relative_error(*_synthetic(1.0), lc)
    mm = relative_error(*_synthetic(1000.0), lc * 1000.0)
    assert m > 0.0 and mm > 0.0, f"degenerate operands: {m:.3e}, {mm:.3e}"

    ratio = mm / m
    assert_close(
        ratio, 1.0, ROUNDOFF_IDENTITY, floor=np.finfo(float).eps,
        what=f"unit-invariance ratio (m={m:.4e}, mm={mm:.4e})",
    )


@pytest.mark.parametrize(
    "name, measure",
    [
        # The measure that shipped before R2.
        ("mixed max()", lambda got, ex, _lc: float(
            np.abs(got - ex).max() / np.abs(ex).max())),
        # The sabotage the docstring names: weighting that discards rotations.
        ("w[3:] = 0", lambda got, ex, lc: float(
            (np.abs(got - ex) * np.r_[np.ones(3), np.zeros(3)]).max()
            / (np.abs(ex) * np.r_[np.ones(3), np.zeros(3)]).max())),
    ],
)
def test_a_DEFECTIVE_measure_fails_that(name: str, measure) -> None:
    """Both controls must fail the invariance, and the operands are reported.

    `w[3:] = 0` produces 0/0 on a rotation-only error, which is itself a failure
    to resolve -- reported rather than silently passing.
    """
    lc = 9.67
    m = measure(*_synthetic(1.0), lc)
    mm = measure(*_synthetic(1000.0), lc * 1000.0)

    if m == 0.0 or mm == 0.0:
        # Degenerate rather than drifting: this measure cannot see the error at
        # all. That IS the defect, so it is asserted rather than returned -- an
        # early `return` here is a test that passes while checking nothing, which
        # is the failure this whole family of controls exists to prevent.
        assert m == 0.0 and mm == 0.0, (
            f"{name} was degenerate in one unit system only ({m:.3e}, {mm:.3e}); "
            "that is neither blindness nor drift and needs explaining"
        )
        return

    assert_differs(
        mm / m, 1.0, by=0.5, floor=np.finfo(float).eps,
        what=f"{name} unit drift (m={m:.4e}, mm={mm:.4e})",
    )
