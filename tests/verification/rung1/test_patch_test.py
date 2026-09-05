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

What this gate is BLIND to, by design — the general statement (R44, R53)
-----------------------------------------------------------------------
**Every UNIFORM material or section error.** Not just `kappa`: any property error
applied to *every* element is invisible to this gate, and a property error in
*one* element of five is caught at one part in 10^6. Measured, same mesh, same
states:

    uniform, applied to every element          worst err     ceiling 1e-12
      E x 2                                     1.2513e-14   invisible
      nu 0.30 -> 0.45                           3.3044e-14   invisible
      section scaled x 1.5                      4.3564e-15   invisible
      kappa 0.530612 -> 0.5 (a 5.8% error)      8.5848e-15   invisible

    non-uniform, one element of five
      x 1.000001                                1.1743e-07   CAUGHT
      x 1.001                                   1.1734e-04   CAUGHT
      x 2.0                                     6.8860e-02   CAUGHT

**Why, and it is the patch test's definition rather than a hole.** The test is
displacement-driven with ZERO interior load, and the exact field lies in the
element's own solution space. The interior nodes are then fixed by the end
conditions and by the RATIOS of the element stiffnesses; a uniform factor
cancels out of those ratios exactly. So `G2.2 certifies relative consistency
between elements — assembly, connectivity, transformation — and no absolute
property at all.`

This subsumes the earlier statement about `kappa` alone. `_exact_local` does draw
state 4's reference from `SEC.kappa(S355)`, the same source the element uses, per
Q1b's pin -- but even an independent reference would not change the conclusion,
because `E` and the section are drawn independently and are equally invisible.

Absolute properties are gated at **V2.1/V2.2**, the cantilever against a closed
form, where the reference does not come from the model. A reader who takes a
green G2.2 as covering the section properties is reading it wrong.

The gate is NOT blind to the shear FORMULATION: substituting the Euler-Bernoulli
bending block for the shear-flexible one reddens `shear` and `shear_xz` at
`6.198e-03` in the field and `7.687e-02` in the resultants, while the other four
states stay at or below `2.32e-14` — AV4's state-4 argument, measured. So state 4
discriminates the formulation; it is the section CONSTANT feeding both sides that
it cannot see.
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.assemble.system import BeamElement, assemble, solve
from floatfea.element.transform import rotation_matrix
from floatfea.model.material import S355, Section
from floatfea.model.nodes import Model, Node, node_dofs
from floatfea.tolerances import (DETECTION_THRESHOLD_BAND, PATCH_TEST_COND_FACTOR,
                                 PATCH_TEST_COND_FACTOR_COUNTER_DEFECT,
                                 PATCH_TEST_EXACTNESS,
                                 PATCH_TEST_EXACTNESS_COUNTER, RESULTANT_EXACTNESS,
                                 RESULTANT_EXACTNESS_COUNTER,
                                 SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT,
                                 SOLVE_BACKWARD_ERROR_FACTOR)
from floatfea.testing import assert_close, assert_differs
from floatfea.tolerances import (COND_UNIT_INVARIANCE,
                                 COND_UNIT_INVARIANCE_COUNTER,
                                 DETECTION_THRESHOLD_BAND_COUNTER,
                                 ROUNDOFF_IDENTITY)

SEC = Section.circular_tube(0.6, 0.012)
STATES = ["axial", "curvature", "twist", "shear",
          "curvature_xz", "shear_xz"]

# The four state amplitudes, in ONE place. `_exact_local` poses the field from
# them and `_exact_resultants` poses the internal forces from them, so the two
# cannot drift apart into a comparison of one state against another.
EPS_AXIAL = 1.0e-4        # axial strain, dimensionless
CURVATURE = 2.0e-4        # 1/m
TWIST_RATE = 3.0e-5       # rad/m
SHEAR_LOAD = 1.0e5        # N, constant shear with its linear moment
# Irregular: no pair of element lengths in a SMALL-INTEGER RATIO. Lengths
# [3.27, 3.00, 0.90, 0.79, 1.71]; the closest pairwise ratio to p/q with p,q <= 5
# is 0.0877. Kept as standard practice -- a controlled measurement found the
# property itself worth nothing for this gate (R3, docs/instrumentation.md).
STATIONS = np.array([0.0, 3.27, 6.27, 7.17, 7.96, 9.67])
AXIS_ALIGNED = np.array([1.0, 0.0, 0.0])
SKEW = np.array([1.0, 0.35, 0.22]) / np.linalg.norm(np.array([1.0, 0.35, 0.22]))


def _section_material(scale: float):
    """The same physical section and material posed at length-unit factor `scale`.

    `scale == 1.0` returns the module's own SEC/S355 objects, so every figure
    measured before the sweep existed is reproduced bit-for-bit rather than
    recomputed through a scaling path.
    """
    if scale == 1.0:
        return SEC, S355
    from floatfea import basis
    from floatfea.model.material import Material

    mat = Material(E=basis.E_STEEL / scale**2, nu=basis.NU_STEEL,
                   rho=basis.RHO_STEEL, fy=basis.FY_S355, name="scaled")
    return Section.circular_tube(0.6 * scale, 0.012 * scale), mat


def _model(direction: np.ndarray, scale: float = 1.0):
    sec, mat = _section_material(scale)
    m = Model()
    for s in STATIONS * scale:
        m.nodes.add(Node(*(s * direction)))
    els = [BeamElement(i, i + 1, sec, mat) for i in range(len(STATIONS) - 1)]
    a, b = m.nodes[0].xyz, m.nodes[1].xyz
    return m, els, rotation_matrix(a, b)


def _exact_local(state: str, x: np.ndarray, scale: float = 1.0) -> np.ndarray:
    """(n_nodes, 6) exact LOCAL displacement for a constant-strain state.

    Under a length-unit factor `scale` the amplitudes carrying 1/length scale as
    1/scale, and the shear load `P` is invariant: `EI ~ scale^2` and
    `kappa G A ~ scale^0`, so `u ~ scale` and `phi ~ scale^0` with `P` fixed.
    """
    sec, mat = _section_material(scale)
    ei = mat.E * sec.I_z
    kga = sec.kappa(mat) * mat.G * sec.A
    u = np.zeros((x.size, 6))
    if state == "axial":
        u[:, 0] = EPS_AXIAL * x
    elif state == "curvature":
        c = CURVATURE / scale
        u[:, 1] = c * x**2 / 2.0
        u[:, 5] = c * x
    elif state == "twist":
        u[:, 3] = (TWIST_RATE / scale) * x
    elif state == "shear":
        p, ll = SHEAR_LOAD, STATIONS[-1] * scale
        u[:, 1] = p * (ll * x**2 / 2.0 - x**3 / 6.0) / ei + p * x / kga
        u[:, 5] = p * (ll * x - x**2 / 2.0) / ei
    elif state == "curvature_xz":
        # x-z plane. `w' = -phi_y`, so a positive curvature about +y bends the
        # member the other way in w -- the sign the x-y states cannot see.
        c = CURVATURE / scale
        u[:, 2] = -c * x**2 / 2.0
        u[:, 4] = c * x
    elif state == "shear_xz":
        # Constant shear in x-z, with its linear moment. Same field as `shear`
        # with the rotation negated, per `w' = -phi_y`; EI uses I_y.
        p, ll = SHEAR_LOAD, STATIONS[-1] * scale
        ei_y = mat.E * sec.I_y
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


def _element_resultants(model, elements, u_global: np.ndarray) -> np.ndarray:
    """(n_el, 12) LOCAL end forces, ``k_loc (T u_e)``, from a solved global field.

    The standard recovery: rotate the element's two nodal DOF into local axes and
    push them through the element stiffness. F5's stress recovery supersedes this;
    it lives here because G2.2 needs a quantity that is not the displacement it
    already checks.
    """
    from floatfea.assemble.system import element_length
    from floatfea.element.beam import local_stiffness
    from floatfea.element.transform import rotation_matrix, transformation
    from floatfea.model.nodes import element_dofs

    out = np.empty((len(elements), 12))
    for i, e in enumerate(elements):
        k = local_stiffness(e.section, e.material, element_length(model, e))
        r = rotation_matrix(model.nodes[e.node_a].xyz, model.nodes[e.node_b].xyz,
                            orientation_node=e.orientation_node, roll_rad=e.roll_rad)
        out[i] = k @ (transformation(r) @ u_global[element_dofs(e.node_a, e.node_b)])
    return out


def _exact_resultants(state: str, x_a: float, x_b: float,
                      scale: float = 1.0) -> np.ndarray:
    """(12,) analytic LOCAL end forces for one element of a constant-strain state.

    From STATICS AND SECTION PROPERTIES, not from the solve: ``EA eps``,
    ``EI kappa`` in each plane, ``GJ phi'``, and for state 4 the constant shear
    ``P`` with its linear moment ``P(L - x)``. Sign convention is the element's
    own -- ``f = k u`` is the force the stiffness applies at each end -- so end
    `a` carries the negative of a tension, and it is VERIFIED rather than
    asserted by `test_the_resultant_recovery_is_EXACT_on_the_exact_field`.

    Note what this does and does not exercise. `kappa G A` does not appear: the
    resultants of state 4 are fixed by equilibrium, so a wrong shear coefficient
    moves the FIELD (which `_exact_local` poses and the gate checks) and not
    these. What it adds over the displacement check is a stiffness-weighted
    derivative of the field, which is why a stiffness defect moves it by more
    than it moves the displacement -- measured 0.41-0.48 against 0.064-0.069 at
    a 2x defect.
    """
    sec, mat = _section_material(scale)
    ea = mat.E * sec.A
    gj = mat.G * sec.J
    ei_z = mat.E * sec.I_z
    ei_y = mat.E * sec.I_y
    ll = STATIONS[-1] * scale
    curv = CURVATURE / scale
    f = np.zeros(12)
    if state == "axial":
        f[0], f[6] = -ea * EPS_AXIAL, ea * EPS_AXIAL
    elif state == "twist":
        f[3], f[9] = -gj * (TWIST_RATE / scale), gj * (TWIST_RATE / scale)
    elif state == "curvature":
        f[5], f[11] = -ei_z * curv, ei_z * curv
    elif state == "curvature_xz":
        f[4], f[10] = -ei_y * curv, ei_y * curv
    elif state == "shear":
        f[1], f[7] = -SHEAR_LOAD, SHEAR_LOAD
        f[5], f[11] = -SHEAR_LOAD * (ll - x_a), SHEAR_LOAD * (ll - x_b)
    elif state == "shear_xz":
        # w' = -phi_y, so the moments carry the opposite sign to the x-y pair.
        f[2], f[8] = -SHEAR_LOAD, SHEAR_LOAD
        f[4], f[10] = SHEAR_LOAD * (ll - x_a), -SHEAR_LOAD * (ll - x_b)
    else:  # pragma: no cover
        raise ValueError(state)
    return f


def _worst_resultant_error(model, elements, u_global: np.ndarray, state: str,
                           scale: float = 1.0) -> float:
    """Worst relative resultant error over the elements, scaled per element."""
    got = _element_resultants(model, elements, u_global)
    worst = 0.0
    for i, e in enumerate(elements):
        ex = _exact_resultants(state, float(STATIONS[e.node_a] * scale),
                               float(STATIONS[e.node_b] * scale), scale)
        worst = max(worst, float(np.abs(got[i] - ex).max() / np.abs(ex).max()))
    return worst


def _free_conditioning(model, elements) -> float:
    """`cond(D^-1/2 K_ff D^-1/2)` -- the EQUILIBRATED conditioning of the patch
    system, which is what the floor is built on (BH1/R55).

    NOT `cond(K_ff)`. That was the first form and it fails the property a floor
    most needs: it is not unit-invariant, and the gate runs three unit systems.
    Measured, same six states, same two orientations:

        S        cond(K_ff)     cond(K~)    worst err   err/(c~.eps)
        1e-3     5.9831e+08   3.8491e+02   1.6029e-13       1.8754
        1        9.2096e+02   3.8491e+02   1.2513e-14       0.1464
        1e+3     4.0490e+07   3.8491e+02   4.9240e-14       0.5761

    `cond(K~)` is the SAME NUMBER at all three -- spread `1.000000x` -- because
    `diag(SKS) = S diag(K) S` makes the equilibrated matrix algebraically
    invariant under a diagonal rescaling. `cond(K_ff)` spans six orders over the
    same three, so a ceiling built on it was 5.4e5x weaker at millimetres than at
    metres: it moved with the unit system rather than with the problem.

    It keeps the other property too -- it still tracks slenderness, `121.7x` over
    `D = 0.6 .. 0.05` -- so it is not a constant wearing a floor's clothes.

    `equilibrate` is a tested utility and is still NOT on the solve path (BD2).
    Estimating this floor is what it is for.

    Dense, because the free block is 24x24 and the number is wanted exactly.
    """
    from floatfea.assemble.system import equilibrate

    ends = np.concatenate([node_dofs(0), node_dofs(len(STATIONS) - 1)])
    free = np.setdiff1d(np.arange(model.n_dof), ends)
    kff = assemble(model, elements)[free][:, free].tocsc()
    return float(np.linalg.cond(equilibrate(kff)[0].toarray()))


def floor_aware_ceiling(model, elements) -> float:
    """`PATCH_TEST_COND_FACTOR * cond(K~) * eps` -- the ceiling that scales.

    `PATCH_TEST_EXACTNESS`, a constant, is what breaks on slender members: its
    ratio spans 141x over element L/r = 15.7 .. 117.9 and crosses 1 three times,
    non-monotonically. Against the equilibrated conditioning the same errors span
    7.9x and never reach 1.

    **Both are asserted**, and the constant is the CAP that bounds this one's
    self-reference (BH2): a floor computed from `K` moves when `K` is defective,
    so the loosening any defect can buy is bounded by
    `PATCH_TEST_EXACTNESS / floor_aware_ceiling`.
    """
    return PATCH_TEST_COND_FACTOR * _free_conditioning(model, elements) * float(
        np.finfo(float).eps)


def _run(
    state: str,
    direction: np.ndarray,
    stiffness_scale: float = 1.0,
    block: str | None = None,
    scale: float = 1.0,
    transpose_transform: bool = False,
):
    """Solve the patch test. `stiffness_scale` perturbs element 1 -- the whole
    element by default, or only `block`'s local entries when named. `scale` poses
    the same physical problem in a different length unit (R40)."""
    m, els, r = _model(direction, scale)
    u_ex = _to_global(_exact_local(state, STATIONS * scale, scale), r)

    k = assemble(m, els)
    if transpose_transform:
        # The plan's named counter-case for this gate, made executable (R4): ONE
        # element's rotation used transposed. R is orthogonal so R.T is a valid
        # rotation -- the element is not corrupted, it is oriented wrongly, which
        # is what a transform bug actually looks like.
        from floatfea.assemble.system import element_length
        from floatfea.element.beam import local_stiffness
        from floatfea.element.transform import rotation_matrix, to_global

        e = els[1]
        k_loc = local_stiffness(e.section, e.material, element_length(m, e))
        rot = rotation_matrix(m.nodes[e.node_a].xyz, m.nodes[e.node_b].xyz,
                              orientation_node=e.orientation_node,
                              roll_rad=e.roll_rad)
        delta = to_global(k_loc, rot.T) - to_global(k_loc, rot)
        k = k.tolil()
        dd = np.concatenate([node_dofs(1), node_dofs(2)])
        for i in range(12):
            for j in range(12):
                k[dd[i], dd[j]] += delta[i, j]
        k = k.tocsr()

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

    err = relative_error(got, u_ex, STATIONS[-1] * scale)
    res_err = _worst_resultant_error(m, els, u, state, scale)
    return err, res, res_err


# The length units the gate is asserted in (R40). `PATCH_TEST_EXACTNESS`'s comment
# justifies 1e-12 by invariance across unit systems, and until this parametrisation
# existed that justification was produced by a scratch harness -- the number that
# decided whether the ceiling was defensible had exactly the status `_MEASURED`
# was deleted for. Three decades is what covers the worst measured cell (S = 1e-3)
# at 36 nodes rather than 108; G2.5/V1.3 remains its own gate and is not closed
# early by this.
GATE_UNIT_SCALES = [1e-3, 1.0, 1e3]


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
@pytest.mark.parametrize("orientation", ["axis_aligned", "skew"])
@pytest.mark.parametrize("scale", GATE_UNIT_SCALES, ids=lambda s: f"S={s:g}")
def test_the_six_constant_strain_states_are_EXACT(
    state: str, orientation: str, scale: float
) -> None:
    """G2.2. Exactness at ULP scale, not convergence -- in three length units."""
    d = AXIS_ALIGNED if orientation == "axis_aligned" else SKEW
    err, res, res_err = _run(state, d, scale=scale)
    assert err <= PATCH_TEST_EXACTNESS, (
        f"{state}/{orientation}/S={scale:g}: interior nodes deviate from the "
        f"exact field by "
        f"{err:.3e}, above {PATCH_TEST_EXACTNESS:.0e}. This is a patch-test "
        "failure -- every accuracy comparison above rung 1 is uninterpretable "
        "until it is fixed, and refinement is not the response."
    )
    # The floor-aware bound (R46). A constant ceiling is what breaks on slender
    # members; this one scales with the achievable accuracy of the solve. At the
    # posed geometry it is TIGHTER than the constant above, so it binds here too.
    m_c, els_c, _ = _model(d, scale)
    ceiling = floor_aware_ceiling(m_c, els_c)
    assert err <= ceiling, (
        f"{state}/{orientation}/S={scale:g}: {err:.3e} exceeds "
        f"{PATCH_TEST_COND_FACTOR:g} * cond(K_ff) * eps = {ceiling:.3e}. The "
        "error is above the accuracy this solve can achieve, which is a "
        "formulation or assembly defect rather than round-off."
    )

    # The SECOND quantity, and the one that moves under a stiffness defect (R41).
    # `res.residual` used to sit here; it measures the SOLVE, not the element, and
    # it does not move under a defect the line above fails by eleven orders -- it
    # moved DOWN for two of three states at a 2x defect. It is now
    # `test_the_solve_residual_is_a_SOLVE_check`, out of the G2.2 evidence.
    assert res_err <= RESULTANT_EXACTNESS, (
        f"{state}/{orientation}/S={scale:g}: recovered element resultants "
        f"deviate from the "
        f"analytic EA*eps / EI*kappa / GJ*phi' / P values by {res_err:.3e}, above "
        f"{RESULTANT_EXACTNESS:.0e}. The nodal field can be right while the "
        "internal forces are wrong -- that is what this line is for."
    )


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

    R38: THE COMPARISON IS ON THE O(1) RATIO, NOT ON TWO 1e-12 NUMBERS.
    The previous form was

        assert err == pytest.approx(PATCH_TEST_EXACTNESS, rel=DETECTION_THRESHOLD_BAND)

    where `rel * |expected| = 0.05 * 1e-12 = 5e-14` but `pytest.approx`'s
    UNDECLARED default `abs = 1e-12` is twenty times larger and therefore
    decided. The band in force was `0 .. 2e-12` rather than the declared
    `9.5e-13 .. 1.05e-12`, so `err = 0.0` passed: with the perturbation dropped
    from `_run` -- the gate's sensitivity exactly zero -- all six of these nodes
    stayed green. This was G2.2's ONLY guard against widening
    `PATCH_TEST_EXACTNESS`, so the ceiling had no live guard at all.

    Dividing by the ceiling puts both operands at O(1), where a 5% relative band
    is the only thing that can decide. `assert_close` is relative-only and
    carries no defaults, which is the same move BD3 made for R9.

    WHAT THE BAND BUYS, measured by bisection on the shipped predicate rather
    than derived (the inverted number the verdict asked for). The smallest
    sensitivity change this assertion detects, per state::

        state          ratio at f=1   detected above   detected below
        axial              0.997640          +5.24%           -5.01%
        curvature          1.003067          +4.88%           -5.54%
        twist              0.999703          +5.25%           -5.02%
        shear              1.009952          +4.50%           -5.95%
        curvature_xz       0.999730          +5.27%           -5.08%
        shear_xz           1.000443          +5.47%           -5.07%

    So a formulation change that moved any state's sensitivity by **+5.5% or
    -6.0% is caught in every state**, and by +4.5% / -5.0% in the tightest. Not
    a symmetric +/-5%: the band is relative to the LARGER operand, and each
    state already sits a little off 1.000.
    """
    eps = DETECTION_THRESHOLD[state]
    err, _, _ = _run(state, SKEW, stiffness_scale=1.0 + eps)
    ratio = err / PATCH_TEST_EXACTNESS
    assert_close(
        ratio, 1.0, DETECTION_THRESHOLD_BAND, floor=np.finfo(float).eps,
        what=(
            f"{state}: perturbing by the recorded threshold {eps:.3e} gave "
            f"{err:.4e} against the ceiling {PATCH_TEST_EXACTNESS:.0e}, a ratio "
            f"of {ratio:.6f}. The gate's sensitivity has changed and the "
            "recorded thresholds are stale"
        ),
    )


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
def test_a_perturbed_element_BREAKS_the_patch_test(state: str) -> None:
    """Negative control, per state.

    A patch test that cannot fail certifies connectivity rather than testing it.
    One interior element's stiffness is perturbed -- the defect a wrong length or
    a wrong section produces -- and every state must detect it.

    THE MARGIN, written down because a counter-case without one says nothing
    about how close the gate is to losing the case (R15): the smallest response
    is `1.0764e-07` against a counter of `1.0e-07` -- **7.6%**. That is tight by
    design. The counter was moved to the smallest of the six measured responses
    (R2), so it sits just under the weakest state rather than comfortably under
    the strongest, and a formulation change that cost any state 8% of its
    sensitivity would fail here rather than quietly reducing the gate to five
    working states.
    """
    err, _, _ = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-6)
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
@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
@pytest.mark.parametrize("orientation", ["axis_aligned", "skew"])
def test_the_resultant_recovery_is_EXACT_on_the_exact_field(
    state: str, orientation: str
) -> None:
    """The analytic table is verified, not asserted -- eighth guard.

    `_exact_resultants` writes down a sign convention: `f = k u` is the force the
    stiffness applies at each end, so end `a` carries the negative of a tension,
    and the x-z moments carry the opposite sign to the x-y pair because
    `w' = -phi_y`. If any of that is wrong the error is O(1), not O(eps) -- a
    flipped sign doubles the discrepancy. Pushing the EXACT field through the
    recovery isolates the table from the solve: no factorisation is involved, so
    a failure here is the table or the element, never the solve.

    Measured on the exact field: 7.5e-16 (axial) to 1.19e-13 (shear, skew). That
    is the cancellation floor of `k @ u`, and it is why the resultant channel
    cannot share the displacement ceiling.
    """
    d = AXIS_ALIGNED if orientation == "axis_aligned" else SKEW
    m, els, r = _model(d)
    u_exact_global = _to_global(_exact_local(state, STATIONS), r).reshape(-1)
    err = _worst_resultant_error(m, els, u_exact_global, state)
    assert err <= RESULTANT_EXACTNESS, (
        f"{state}/{orientation}: k_loc @ u_exact disagrees with the analytic "
        f"resultants by {err:.3e}. No solve is involved, so this is the analytic "
        "table's signs and magnitudes, or the element."
    )


# The resultant channel's DECISION thresholds -- the defect each shipped
# predicate actually detects, by bisection on the predicate itself (R47). These
# are what a reader comparing the two channels needs; the raw responses to one
# arbitrary 1e-6 defect are not, and quoting them as "6.4x the more sensitive"
# said the opposite of what the code does.
#
#   state            via field  via resultants    ratio
#   axial           9.1808e-12      1.4498e-09   157.9x
#   curvature       9.2518e-12      1.4422e-09   155.9x
#   twist           9.1708e-12      1.4498e-09   158.1x
#   shear           8.4540e-12      1.2527e-09   148.2x
#   curvature_xz    9.2976e-12      1.4422e-09   155.1x
#   shear_xz        8.4953e-12      1.2527e-09   147.5x
#
# As a GATE the resultant channel is ~150x weaker. It is kept for what it sees,
# not for sensitivity: it is a different quantity, verified against statics, and
# four of five planted sign defects in its analytic table are caught by it.
RESULTANT_DETECTION_THRESHOLD = {
    "axial": 1.4498e-09,
    "curvature": 1.4422e-09,
    "twist": 1.4498e-09,
    "shear": 1.2527e-09,
    "curvature_xz": 1.4422e-09,
    "shear_xz": 1.2527e-09,
}


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
def test_the_RESULTANT_detection_threshold_still_holds(state: str) -> None:
    """BG1/R48: the guard that makes `RESULTANT_EXACTNESS` un-widenable.

    Measured: the entry could be moved `1e-9 -> 1e-7` with the whole suite green.
    Its only guard was `ceiling < counter`, a comparison between two literals in
    `tolerances.py`, plus a control asserting a response exceeded the counter --
    neither of which mentions the ceiling's magnitude. 680x of free travel.

    This is `test_the_measured_detection_threshold_still_holds` with `res_err` in
    place of `err`, which is what the sixth verdict named as the cheapest form.
    Perturbing by the recorded threshold must land the resultant error ON the
    ceiling, within the declared band, so any move of the ceiling in either
    direction fails here.
    """
    eps = RESULTANT_DETECTION_THRESHOLD[state]
    _, _, res_err = _run(state, SKEW, stiffness_scale=1.0 + eps)
    ratio = res_err / RESULTANT_EXACTNESS
    assert_close(
        ratio, 1.0, DETECTION_THRESHOLD_BAND, floor=np.finfo(float).eps,
        what=(
            f"{state}: perturbing by the recorded resultant threshold {eps:.3e} "
            f"gave {res_err:.4e} against the ceiling {RESULTANT_EXACTNESS:.0e}, "
            f"a ratio of {ratio:.6f}"
        ),
    )


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
def test_a_perturbed_element_BREAKS_the_recovered_RESULTANTS(state: str) -> None:
    """Negative control for the resultant channel, per state.

    The line this channel replaced could not do this: a solve residual does not
    move under a stiffness defect, and at a 2x defect it moved DOWN for two of
    three states. Here a 1e-6 defect in one interior element must show, in every
    state.
    """
    _, _, res_err = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-6)
    assert res_err > RESULTANT_EXACTNESS, (
        f"{state}: a 1e-6 stiffness error left the recovered resultants at "
        f"{res_err:.3e}, at or below the ceiling {RESULTANT_EXACTNESS:.0e}. The "
        "assertion does not trip on the defect it is required to catch."
    )
    assert res_err >= RESULTANT_EXACTNESS_COUNTER, (
        f"{state}: a 1e-6 stiffness error in one element moved the recovered "
        f"resultants by only {res_err:.3e}, below the counter-case "
        f"{RESULTANT_EXACTNESS_COUNTER:.3e}. The channel has lost sensitivity "
        "and the ceiling above it is no longer defensible."
    )


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
@pytest.mark.parametrize("orientation", ["axis_aligned", "skew"])
@pytest.mark.parametrize("scale", GATE_UNIT_SCALES, ids=lambda s: f"S={s:g}")
def test_the_solve_is_BACKWARD_STABLE(state: str, orientation: str,
                                      scale: float) -> None:
    """The solve check, in the normalisation that does not depend on the load.

    OUTSIDE the G2.2 evidence (R41): it says the factorisation solved the system
    it was handed, not that the system was the right one. Kept because a silently
    bad solve makes every number above it meaningless.

    IT RUNS AT ALL THREE SCALES NOW (R45). The version this replaces asserted
    `||r||/||f||` and had to be restricted to metres, on the recorded ground that
    "the residual is conditioning-limited". The cell refutes that: cond(K_ff) is
    a property of the matrix and is identical for all six states at a scale, and
    holding it fixed while varying the state puts five of six at round-off. The
    whole excursion was the `twist` cell, whose `||K||.||u||/||f||` is 1.4e+08
    against 4.7 for axial -- a collapsing LOAD norm. Backward error has no such
    denominator: worst over the eighteen cells is 1.0343e-16, or 0.47 eps.
    """
    d = AXIS_ALIGNED if orientation == "axis_aligned" else SKEW
    _, res, _ = _run(state, d, scale=scale)
    ceiling = SOLVE_BACKWARD_ERROR_FACTOR * float(np.finfo(float).eps)
    assert res.backward_error <= ceiling, (
        f"{state}/{orientation}/S={scale:g}: backward error "
        f"{res.backward_error:.3e} exceeds {SOLVE_BACKWARD_ERROR_FACTOR:g} eps = "
        f"{ceiling:.3e}. The factorisation did not solve the system it was "
        "given; nothing above this line is interpretable."
    )


def test_a_WRONG_SOLUTION_is_caught_by_the_backward_error() -> None:
    """BG1: the counter, injected, at the cell where it is hardest.

    STATED LIMITATION, unchanged from the version this replaces: there is no way
    to make the shipped `solve` return a large residual without breaking the
    factorisation, so this perturbs the solved field and recomputes the measure
    **by the same definition `solve` uses**. It exercises the measure's
    discriminating power, not the code path that computes it.

    THE COST OF THIS NORMALISATION, measured and stated rather than left to be
    found: `||r||/||f||` detected a wrong solve at ~1e-12. Backward error is
    weaker at exactly the cells where `||f||` collapses -- it is the right
    measure of STABILITY and a weaker detector of a WRONG ANSWER. The counter is
    set at the worst cell, so every cell catches it, and `SolveResult` reports
    both numbers so the other one is still available to a caller.
    """
    worst_missed: list[str] = []
    ceiling = SOLVE_BACKWARD_ERROR_FACTOR * float(np.finfo(float).eps)
    for scale in GATE_UNIT_SCALES:
        for state in STATES:
            m, els, r = _model(SKEW, scale)
            u_ex = _to_global(_exact_local(state, STATIONS * scale, scale), r)
            k = assemble(m, els)
            n_nodes = len(STATIONS)
            ends = np.concatenate([node_dofs(0), node_dofs(n_nodes - 1)])
            free = np.setdiff1d(np.arange(m.n_dof), ends)
            u_pres = np.zeros(m.n_dof)
            u_pres[node_dofs(0)] = u_ex[0]
            u_pres[node_dofs(n_nodes - 1)] = u_ex[-1]
            f = -(k @ u_pres)
            f[ends] = 0.0

            clean = solve(k, f, ends)
            kff = k[free][:, free].tocsc()
            ff = f[free]
            wrong = clean.u[free] * (1.0 + SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT)
            bwd = float(np.linalg.norm(kff @ wrong - ff)
                        / (abs(kff).max() * np.linalg.norm(wrong)
                           + np.linalg.norm(ff)))
            if bwd <= ceiling:
                worst_missed.append(f"{state}/S={scale:g} at {bwd:.3e}")
            assert clean.backward_error <= ceiling, (
                f"{state}/S={scale:g}: the CLEAN solve is already at "
                f"{clean.backward_error:.3e}, so the counter below is vacuous"
            )

    assert not worst_missed, (
        f"a solved field wrong by {SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT:.3e} "
        f"relative stayed below the ceiling {ceiling:.3e} in: "
        f"{', '.join(worst_missed)}. The check would pass a wrong solve."
    )


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
def test_a_TRANSPOSED_TRANSFORM_on_one_element_breaks_every_state(state: str) -> None:
    """The counter-case `F2.md` sec. D5 names for this gate, executed (R4).

    The plan promised "one element's transformation transposed" and nothing ran
    it, so the row was prose where every other counter-case in this file is a
    number a test consumes. It is a good case: `R.T` is itself a valid rotation,
    so the element stays a legitimate beam and only its ORIENTATION is wrong --
    which is what a transform bug looks like, and is not reachable by scaling a
    stiffness.

    Measured response, six states, skew orientation:
    axial 1.53e+00, curvature 2.01e-01, twist 1.57e-01, shear 3.02e-01,
    curvature_xz 1.01e-01, shear_xz 1.49e-01 -- every state, at O(1).
    """
    err, _, res_err = _run(state, SKEW, transpose_transform=True)
    assert err >= PATCH_TEST_EXACTNESS_COUNTER, (
        f"{state}: one element's transform transposed moved the interior field "
        f"by only {err:.3e}, below the counter-case "
        f"{PATCH_TEST_EXACTNESS_COUNTER:.3e}. A wrongly oriented element is "
        "invisible to this gate."
    )
    assert res_err >= RESULTANT_EXACTNESS_COUNTER, (
        f"{state}: the recovered resultants moved by only {res_err:.3e} under a "
        "transposed transform."
    )


# Sections for the floor-aware counter test: the posed geometry and three slender
# ones the constant ceiling cannot cover. D/t = 50 throughout, which holds the
# section's proportions so the sweep isolates slenderness.
COND_FACTOR_SECTIONS = [0.600, 0.120, 0.100, 0.080]


@pytest.mark.parametrize("d_outer", COND_FACTOR_SECTIONS, ids=lambda d: f"D={d:g}")
def test_the_floor_aware_ceiling_CATCHES_its_counter_defect(d_outer: float) -> None:
    """BG1: the counter is a MUTATION, not a value sitting in a file.

    `RESULTANT_EXACTNESS` could be widened 680x in silence because nothing
    injected a defect and asserted the assertion tripped -- its only guard was
    `ceiling < counter`, which is a comparison between two literals. This test
    injects `PATCH_TEST_COND_FACTOR_COUNTER_DEFECT` and requires the floor-aware
    assertion to FIRE, on four sections spanning element L/r = 15.7 .. 117.9.

    Widening the factor raises the ceiling and the detection threshold together,
    so a factor much above 4 pushes the threshold past the counter and this test
    goes red. That is what makes silent widening structurally impossible rather
    than something review has to catch.
    """
    global SEC
    original = SEC
    try:
        SEC = Section.circular_tube(d_outer, d_outer / 50.0)
        m, els, _ = _model(SKEW)
        ceiling = floor_aware_ceiling(m, els)

        clean = max(_run(st, SKEW)[0] for st in STATES)
        assert clean <= ceiling, (
            f"D={d_outer:g}: the CLEAN configuration is already at {clean:.3e} "
            f"against a ceiling of {ceiling:.3e}; the counter below would be "
            "vacuous because the assertion is already tripped."
        )

        worst_missed = 0.0
        for st in STATES:
            err, _, _ = _run(st, SKEW, stiffness_scale=1.0 + PATCH_TEST_COND_FACTOR_COUNTER_DEFECT)
            if err <= ceiling:
                worst_missed = max(worst_missed, err)
        assert worst_missed == 0.0, (
            f"D={d_outer:g}: a single-element stiffness defect of "
            f"{PATCH_TEST_COND_FACTOR_COUNTER_DEFECT:.3e} left at least one state at "
            f"{worst_missed:.3e}, below the ceiling {ceiling:.3e}. The ceiling "
            "has been widened past the defect it is required to catch."
        )
    finally:
        SEC = original


def test_a_SENSITIVITY_CHANGE_breaks_the_threshold_band() -> None:
    """BG1: `DETECTION_THRESHOLD_BAND`'s counter, injected.

    The entry says a 25% change in any state's sensitivity must be caught. That
    was never run: `DETECTION_THRESHOLD_BAND_COUNTER = 0.25` sat beside the
    ceiling with nothing perturbing anything.

    A sensitivity change by factor `f` is posed by perturbing by `f x` the
    recorded threshold -- the error is linear in the perturbation over this
    range, which is the property the band measures in the first place. Both
    directions, because the band is relative to the larger operand and is not
    symmetric.
    """
    for direction, factor in (("up", 1.0 + DETECTION_THRESHOLD_BAND_COUNTER),
                              ("down", 1.0 - DETECTION_THRESHOLD_BAND_COUNTER)):
        missed = []
        for state in STATES:
            eps = DETECTION_THRESHOLD[state] * factor
            err, _, _ = _run(state, SKEW, stiffness_scale=1.0 + eps)
            ratio = err / PATCH_TEST_EXACTNESS
            try:
                assert_close(ratio, 1.0, DETECTION_THRESHOLD_BAND,
                             floor=np.finfo(float).eps, what="")
            except AssertionError:
                continue
            missed.append(f"{state} {ratio:.4f}")
        assert not missed, (
            f"a {DETECTION_THRESHOLD_BAND_COUNTER:.0%} sensitivity change "
            f"({direction}) was NOT caught in: {', '.join(missed)}. The band is "
            "wider than the change it is declared to detect."
        )


def test_a_STIFFNESS_DEFECT_moves_the_equilibrated_conditioning() -> None:
    """BG1: `COND_UNIT_INVARIANCE`'s counter, injected.

    `COND_UNIT_INVARIANCE_COUNTER = 1e-3` is "the smallest drift worth
    investigating" in `cond(K~)` between unit systems. Nothing produced a drift,
    so the ceiling above it was unguarded.

    The injection is a stiffness defect in one element rather than a unit change,
    because a unit change CANNOT move this quantity -- that is the property under
    test. What must be true is that the assertion can resolve a drift of the
    declared size at all, and a 10% single-element error is the cheapest defect
    that produces one.

    NOTE, measured: the response is not monotone in the defect. A 10% error moves
    cond(K~) by 7.05e-03 and a 100% error by 5.05e-03. The counter is set below
    both, and the non-monotonicity is recorded rather than smoothed.
    """
    from floatfea.assemble.system import element_global_stiffness, equilibrate

    ends = np.concatenate([node_dofs(0), node_dofs(len(STATIONS) - 1)])

    def cond_eq(stiffness_scale: float) -> float:
        m, els = _scaled_model(1.0)
        k = assemble(m, els)
        if stiffness_scale != 1.0:
            delta = (stiffness_scale - 1.0) * element_global_stiffness(m, els[1])
            k = k.tolil()
            d = np.concatenate([node_dofs(1), node_dofs(2)])
            for i in range(12):
                for j in range(12):
                    k[d[i], d[j]] += delta[i, j]
            k = k.tocsr()
        free = np.setdiff1d(np.arange(m.n_dof), ends)
        return float(np.linalg.cond(equilibrate(k[free][:, free].tocsc())[0].toarray()))

    base = cond_eq(1.0)
    drift = abs(cond_eq(1.1) - base) / base
    assert drift >= COND_UNIT_INVARIANCE_COUNTER, (
        f"a 10% stiffness error in one element moved cond(K~) by only "
        f"{drift:.3e}, below the declared counter-case "
        f"{COND_UNIT_INVARIANCE_COUNTER:.3e}. The invariance assertion cannot "
        "resolve a drift of the size it claims to catch."
    )
    assert drift > COND_UNIT_INVARIANCE, "the counter must exceed the ceiling"


UNIFORM_ERRORS = [
    ("E x 2", "material", 2.0),
    ("nu 0.30 -> 0.45", "nu", 0.45),
    ("section x 1.5", "section", 1.5),
]


@pytest.mark.parametrize("label, kind, value", UNIFORM_ERRORS,
                         ids=[u[0] for u in UNIFORM_ERRORS])
def test_a_UNIFORM_property_error_is_invisible_to_this_gate(
    label: str, kind: str, value: float
) -> None:
    """The boundary of what G2.2 certifies, asserted so it stays true (R44/R53).

    This asserts a BLINDNESS, deliberately. The gate is displacement-driven with
    zero interior load and the exact field lies in the element's solution space,
    so the interior nodes depend on the RATIOS of element stiffnesses and a
    uniform factor cancels exactly. Recording it stops a later reader treating a
    green G2.2 as evidence about `E`, `nu`, `kappa` or the section -- and if a
    change ever makes the gate sensitive to a uniform error, this goes red and
    the docstring above it gets revisited rather than quietly ceasing to be true.

    Its partner is `test_a_perturbed_element_BREAKS_the_patch_test`: the same
    magnitude of error in ONE element of five is caught at 1e-6.
    """
    from dataclasses import replace

    global SEC, S355
    sec_before, mat_before = SEC, S355
    try:
        if kind == "material":
            S355 = replace(mat_before, E=mat_before.E * value)
        elif kind == "nu":
            S355 = replace(mat_before, nu=value)
        else:
            SEC = Section.circular_tube(0.6 * value, 0.012 * value)
        worst = max(_run(st, SKEW)[0] for st in STATES)
    finally:
        SEC, S355 = sec_before, mat_before

    assert worst <= PATCH_TEST_EXACTNESS, (
        f"{label} was DETECTED at {worst:.4e}. That contradicts the gate's own "
        "docstring, which says a uniform property error cancels out of the "
        "stiffness ratios. Either the docstring or the formulation is wrong, and "
        "this is not a case of tightening a tolerance."
    )


PLANE_STATES = {
    "bending_xy": ("curvature", "shear"),
    "bending_xz": ("curvature_xz", "shear_xz"),
}


@pytest.mark.parametrize("block", ["bending_xy", "bending_xz"])
def test_a_defect_in_ONE_bending_plane_is_caught_by_THAT_plane(block: str) -> None:
    """Each plane's states detect a defect confined to their own block.

    THE MARGIN (R15): at a `1e-3` defect confined to `bending_xz` the smallest
    detecting state is `1.0756e-04` and the largest blind state is `1.3881e-14`
    -- a separation of **7.7e+09**. Nearly ten orders, and it is not a coincidence to be relied
    on: it is the difference between a state that contains the defective block
    and one whose exact field has no content in it at all, so the blind states
    sit at round-off rather than at a small response.
    """
    for state in PLANE_STATES[block]:
        err, _, _ = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-3, block=block)
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
        err, _, _ = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-3, block=block)
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
    """The same physical beam posed with lengths x `scale`, skew orientation.

    One scaling path, not two: this delegates to `_model`, so the conditioning
    tests below and the gate's own unit sweep cannot drift apart.
    """
    m, els, _ = _model(SKEW, scale)
    return m, els


@pytest.mark.parametrize("scale", UNIT_SCALES)
def test_the_equilibrated_conditioning_is_unit_INVARIANT(scale: float) -> None:
    """`cond(D^-1/2 K D^-1/2)` is the same number in every length unit.

    A PROPERTY OF `equilibrate` THE UTILITY, NOT OF `solve` (R37a). An earlier
    version of this line called it "the algebraic fact the equilibrated solve
    rests on". `solve` does not equilibrate -- it factorises `K_ff` directly
    (BD2, `system.py`) -- so there is no equilibrated solve for anything to rest
    on, and the sentence survived two commits after the path it described was
    deleted.

    What the property is: for diagonal `S`, `diag(SKS) = S diag(K) S`, so the
    scaled matrix is algebraically invariant. Measured, `cond(K~) = 3.85e2` at
    every unit system while `cond(K_ff)` runs 9.2e2 to 6.0e8 over these scales.
    It is asserted because it is the reason `equilibrate` is kept as a candidate
    for F3, and it would be removed with the utility.
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
        "the equilibrated conditioning moved with the length unit, so "
        "`equilibrate` does not do the one thing it is retained for. This says "
        "NOTHING about the solve, which does not use it: the gate's own unit "
        "invariance is asserted by test_the_six_constant_strain_states_are_EXACT"
    )


def test_the_UNequilibrated_conditioning_DOES_move() -> None:
    """Negative control for the test above: the invariance is not automatic.

    Says what it is a control FOR, which is the utility's property. It used to
    say that without this, "equilibration would be ceremony" -- but on the
    production path equilibration IS absent, and `system.py` says so in the
    honest words ("retained as a utility"). A control cannot argue for a
    production choice that was not made.
    """
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
