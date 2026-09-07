"""V1.2 / G2.2 — the patch test. FOUR KINDS of constant-strain state, SIX in
total, all EXACT (AW4).

WHAT IS ASSERTED, AND IT IS NOT THE SOLVED FIELD (F2.md sec. 5b, Q6)
--------------------------------------------------------------------
The gate asserts the **interior out-of-balance of the EXACT field**: impose the
constant-strain field on every node, form `K u_exact` in homogeneous units, and
the interior rows must vanish to round-off. There is **no solve in the gate**.

The solved nodal field error is the FORWARD error of a linear solve -- `cond` x
backward error -- and five successive attempts to bound it with a constant
(1e-12), a conditioning-scaled ceiling, an equilibrated floor and a validated
slenderness domain were each refuted by one more axis the envelope had not
spanned. It is now REPORTED per corpus entry and asserted nowhere; the solve is
gated by its BACKWARD error, which is cond-independent by construction.

PROVENANCE, PER BLOCK, BECAUSE A BLANKET CLAIM IS THE CHEAPEST KIND TO REFUTE
(R93). A previous version of this paragraph said "every figure below this line
was re-measured at this commit". Three blocks below it had not been, and two of
them were contradicted by measurements elsewhere in this same file. Each block of
figures now states which quantity it was measured on and when. Where a block
carries a table that no shipped test produces, it says so.

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

What this gate is BLIND to, by design (R44, R53, narrowed by BH4/R59)
---------------------------------------------------------------------
**A uniform SCALAR factor on K, and nothing wider.** Multiplying every element's
stiffness by the same number leaves the displacement-imposed patch test exactly
where it was: the interior nodes solve `K u = 0` with the ends prescribed, and a
scalar factor cancels out of that. `E x 2` is such a factor and is invisible.
Absolute properties are gated at **V2.1/V2.2**, against a closed form, where the
reference does not come from the model.

**THE WIDER CLAIM WAS WRONG AND IS WITHDRAWN.** An earlier version of this
docstring said *every* uniform material or section error was invisible, listing
`nu` and a scaled section as evidence. Both were artefacts of the measurement:
the test moved the REFERENCE with the element, so it was comparing a beam
against itself. Holding the reference fixed and moving only the element:

    defect                  both moved   reference HELD
    E x 2                   8.0516e-17   8.0516e-17   invisible
    nu 0.30 -> 0.45         9.4103e-17   2.1581e-06   CAUGHT
    section x 1.5           1.7827e-16   2.8875e-05   CAUGHT

(`E x 2` reference-held is 8.0516e-17, the CLEAN value to every digit -- a
uniform scalar is not merely small here, it is exactly cancelled.)

`nu` moves `G/E`, hence `Phi`, hence the SHAPE of K; a scaled section moves `A`
as `D` and `I` as `D^3`. Neither is a scalar multiple, and the gate sees both at
1e-7 and 1e-6, the floors the shipped test asserts. Only `E` scales K uniformly.

`kappa` behaves like `nu` for the same reason, and the gate is blind to it only
because Q1b pins state 4's reference to `SEC.kappa(S355)` -- the same source the
element uses. That is a property of the reference, deliberately chosen, not of
the gate.

The gate is NOT blind to the shear FORMULATION. Substituting the
Euler-Bernoulli bending block for the shear-flexible one, with the reference
field held:

    axial 9.79e-17   curvature 3.46e-17   twist 6.33e-18   curvature_xz 9.41e-17
    shear 1.2913e-04                      shear_xz 1.3895e-04

Only the two shear states move, and they move by twelve orders — AV4's state-4
argument, measured on the shipped quantity. So state 4 discriminates the
formulation; it is the section CONSTANT feeding both sides that it cannot see.
(The resultant channel's response to the same substitution is not restated here:
it was measured on the solved recovery and has not been regenerated at this
commit, and a figure that is not regenerated does not belong in a docstring.)
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.assemble.system import BeamElement, assemble, solve
from floatfea.element.transform import rotation_matrix
from floatfea.model.material import S355, Section
from floatfea.model.nodes import Model, Node, node_dofs
from floatfea.tolerances import (DETECTION_THRESHOLD_BAND,
                                 PATCH_TEST_EXACTNESS,
                                 RESULTANT_EXACTNESS,
                                 RESULTANT_EXACTNESS_COUNTER,
                                 SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT,
                                 SOLVE_BACKWARD_ERROR_FACTOR)
from floatfea.testing import assert_close, assert_differs
from floatfea.tolerances import (DETECTION_THRESHOLD_BAND_COUNTER,
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


def interior_out_of_balance(model, elements, u_exact: np.ndarray,
                            char_length: float, k=None) -> float:
    """G2.2's quantity: how far the EXACT field is from satisfying `K u = 0`.

    Irons' test says a constant-strain field satisfies the discrete equations.
    That is checkable without solving anything: impose the field on every node,
    form `K u_exact`, and the interior out-of-balance must be zero.

    HOMOGENEOUS UNITS, so the comparison is dimensionless and does not mix
    metres with radians (the R2 lesson, applied to the matrix as well as the
    field). With `D = diag(I3, l I3)` per node,

        w      = D u_exact          translations, and l x rotations
        K_hat  = D^-1 K D^-1        forces, and moments / l
        r_hat  = K_hat w            = D^-1 K u_exact

    and the residual is `max |r_hat[interior]| / (max|K_hat| max|w|)`.

    WHY THIS AND NOT THE SOLVED FIELD (F2.md sec. 5b, Q6). The solved field's
    error is the FORWARD error of a linear solve -- `cond` x backward error --
    and `cond` moves with the unit system, the frame, the slenderness, the mesh
    and the section size. Five successive attempts to bound it with a constant,
    a conditioning-scaled ceiling and a validated domain were each refuted by one
    more axis the envelope had not spanned. This quantity has no factorisation in
    it at all: numerator and denominator both carry the largest stiffness, so the
    `lambda^2` amplification that comes from measuring a bending displacement
    against axial round-off cannot arise. Measured, it sits at 0.13-0.49 eps
    across six orders of length unit, 12x of slenderness, and the configuration
    that refuted the domain.

    THE COST, recorded because it decides the counter's operating point: a
    bending-block defect's residual falls as `1/lambda^2` -- measured slope -2.0
    over `lambda = 15.7 .. 188.7`. The counter is therefore recorded at the
    corpus's most slender entry, not at the posed geometry.
    """
    n_nodes = len(u_exact) // 6
    ends = np.concatenate([node_dofs(0), node_dofs(n_nodes - 1)])
    interior = np.setdiff1d(np.arange(len(u_exact)), ends)

    dw = np.ones(len(u_exact))
    for n in range(n_nodes):
        dw[node_dofs(n)[3:]] = char_length

    # `k` IS PASSED IN BY EVERY CALLER THAT PERTURBS. Re-assembling here would
    # silently discard the caller's defect and make every mutation test green --
    # the quantity would then be measuring a matrix nobody was testing.
    kd = assemble(model, elements).toarray() if k is None else np.asarray(
        k.toarray() if hasattr(k, "toarray") else k, dtype=float)
    k_hat = (kd / dw[:, None]) / dw[None, :]
    w = dw * u_exact
    r_hat = k_hat @ w

    denom = float(np.abs(k_hat).max() * np.abs(w).max())
    return float(np.abs(r_hat[interior]).max() / denom)


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
    oob = interior_out_of_balance(m, els, u_ex.reshape(-1),
                                  float(STATIONS[-1] * scale), k=k)
    return err, res, res_err, oob


# The length units the gate is asserted in (R40). Until this parametrisation
# existed, the unit-invariance justification for the ceiling was produced by a
# scratch harness -- the number that decided whether the ceiling was defensible
# had exactly the status `_MEASURED` was deleted for. Three decades is run here;
# G2.5/V1.3 remains its own gate and is not closed early by this.
#
# THE PARAMETRISATION MATTERS LESS TO THE CEILING THAN IT DID, and that is worth
# stating rather than leaving as an unexplained survival: the shipped quantity is
# a ratio of two quantities that both carry the largest stiffness, so a change of
# length unit cannot move it the way it moved the solved field error.
#
# MEASURED OVER THE 36 CELLS THIS PARAMETRISATION ACTUALLY RUNS (R93). The
# sentence here previously quoted "3.8x (0.13-0.49 eps)", which came from a
# scratch sweep over different configurations, not from these cells:
#
#   S = 1e-3   worst 1.4761e-16 (0.665 eps)
#   S = 1      worst 8.7042e-17 (0.392 eps)
#   S = 1e+3   worst 8.7042e-17 (0.392 eps)
#
# The per-scale worst spans 1.70x across six orders of length unit, and the
# individual cells run 0.0001 to 0.665 eps. The three scales stay because a claim
# of unit-invariance should be asserted, not derived.
GATE_UNIT_SCALES = [1e-3, 1.0, 1e3]


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear", "curvature_xz", "shear_xz"])
@pytest.mark.parametrize("orientation", ["axis_aligned", "skew"])
@pytest.mark.parametrize("scale", GATE_UNIT_SCALES, ids=lambda s: f"S={s:g}")
def test_the_six_constant_strain_states_are_EXACT(
    state: str, orientation: str, scale: float
) -> None:
    """G2.2. Exactness at ULP scale, not convergence -- in three length units."""
    d = AXIS_ALIGNED if orientation == "axis_aligned" else SKEW
    _, _, res_err, oob = _run(state, d, scale=scale)

    # THE GATE, and there is no solve in it. Irons' test: the exact field either
    # satisfies the discrete equations or it does not.
    assert oob <= PATCH_TEST_EXACTNESS, (
        f"{state}/{orientation}/S={scale:g}: the exact constant-strain field "
        f"leaves an interior out-of-balance of {oob:.3e}, above "
        f"{PATCH_TEST_EXACTNESS:.0e}. The field does not satisfy the discrete "
        "equations, which is an assembly, transformation or connectivity "
        "defect. Refinement is not the response."
    )

    # THE SOLVED FIELD IS NOT ASSERTED HERE AT ALL (F2.md sec. 5b Q6). Its error
    # is the forward error of a linear solve -- `cond` x backward error -- and
    # five successive attempts to bound it with a constant, a
    # conditioning-scaled ceiling and a validated domain were each refuted by one
    # more axis the envelope had not spanned. It is reported per corpus entry as
    # a diagnostic, and the solve is gated by its BACKWARD error, in
    # test_the_solve_is_BACKWARD_STABLE.

    # The SECOND quantity, and the one that moves under a stiffness defect (R41).
    # `res.residual` used to sit here; it measures the SOLVE, not the element, and
    # it does not move under a defect the line above fails by eleven orders -- it
    # moved DOWN for two of three states at a 2x defect. It is now
    # `test_the_solve_is_BACKWARD_STABLE`, out of the G2.2 evidence.
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
#   state       out-of-balance per 1e-6   smallest eps detected at 5e-15
#   axial              4.9589e-08                 1.01e-13   <- most sensitive
#   curvature          2.2929e-11                 2.18e-10
#   twist              1.7638e-11                 2.83e-10   <- weakest
#   shear              4.4206e-11                 1.13e-10
#   curvature_xz       2.2929e-11                 2.18e-10
#   shear_xz           4.7570e-11                 1.05e-10
#
# All six regenerated by running the shipped tests (R14). The table above is on
# the SHIPPED quantity; the previous one (sensitivities ~1.1e-01, thresholds
# ~9e-12) described the solved nodal field error and does not transfer.
#
# NOTE what is NOT claimed here. An earlier version of this block said removing
# mesh commensurability improved detection "about FIVEFOLD". That is WITHDRAWN --
# see docs/instrumentation.md. The comparison was uncontrolled.
# RE-DERIVED 2026-09-06 WITH THE QUANTITY (F2.md sec. 5b, Q6). The values above
# this line describe the SOLVED nodal field error, which the gate no longer
# asserts; these describe the interior out-of-balance against 5e-15. Linearity
# was checked before inverting, not assumed: the response at 1e-9 is 1.0000 of
# the response at 1e-6 scaled, in all six states.
#
# THE SPREAD IS NEW AND IT IS THE POINT. Under the retired quantity all six
# thresholds sat within 9% of each other; here they span 2800x, because this
# quantity is far more sensitive in AXIAL (4.96e-08 per 1e-6) than in the
# bending and twist states (1.8e-11 .. 4.8e-11 per 1e-6). A single flat
# threshold would have been describing the axial state and nothing else.
DETECTION_THRESHOLD = {
    "axial": 1.01e-13,
    "curvature": 2.18e-10,
    "twist": 2.83e-10,
    "shear": 1.13e-10,
    "curvature_xz": 2.18e-10,
    "shear_xz": 1.05e-10,
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
        axial              0.996385          +5.44%           -4.92%
        curvature          0.999760          +5.34%           -5.02%
        twist              0.998301          +5.49%           -4.88%
        shear              0.999578          +5.28%           -4.97%
        curvature_xz       0.999695          +5.34%           -5.02%
        shear_xz           0.999133          +5.39%           -4.92%

    REGENERATED 2026-09-06 ON THE SHIPPED PREDICATE (R93). The previous table was
    byte-identical to the one at `620ec96`, i.e. it survived the quantity change
    unmeasured; two of its six ratios crossed 1.000 where none does now.

    So a formulation change that moved any state's sensitivity by **+5.5% or
    -5.0% is caught in every state**, and by +5.3% / -4.9% in the tightest. Not
    a symmetric +/-5%: the band is relative to the LARGER operand, and each
    state already sits a little off 1.000.
    """
    eps = DETECTION_THRESHOLD[state]
    _, _, _, err = _run(state, SKEW, stiffness_scale=1.0 + eps)
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

    THE THRESHOLD IS THE GATE'S OWN, AND THERE IS NO SECOND NUMBER HERE. A fixed
    counter on a small defect is a universal the physics forbids: the response
    falls as `1/lambda_weak^2`, so any constant is wrong at some slenderness, and
    six review rounds were spent bounding a domain around that. What this test
    asserts is that at THIS geometry every state detects, i.e. exceeds the ceiling
    the gate decides on. The QUANTITATIVE claim -- that the response follows
    `3.327e-08 * (L/r_min)^(-1.964)` within a declared band -- is asserted per
    corpus entry in `test_corpus_configurations.py`, where it can be measured
    across three decades of slenderness instead of at one point.

    THE MARGIN (R15): the smallest of the six responses here is `1.7638e-11`
    against a ceiling of `5e-15`, i.e. `3528x`. Loose, and saying so is the point;
    the binding measurement is the curve, not this line.
    """
    _, _, _, err = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-6)
    assert err > PATCH_TEST_EXACTNESS, (
        f"{state}: a 1e-6 stiffness error in one element left an interior "
        f"out-of-balance of only {err:.3e}, at or below the ceiling "
        f"{PATCH_TEST_EXACTNESS:.0e}. This state does not detect the defect at "
        "all, and a gate that holds here cannot fail here."
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
# REGENERATED 2026-09-06 ON THE SHIPPED PREDICATES (R93). The `via field` column
# used to hold the RETIRED quantity's thresholds -- reproducible to three digits
# by bisecting `fwd > 1e-12`, and contradicted by `DETECTION_THRESHOLD` 130 lines
# above in this same file. Both columns below come from bisecting the predicate
# each channel actually asserts:
#
#   state            via field  via resultants      ratio
#   axial           1.0136e-13      1.4498e-09   14302.8x
#   curvature       2.1805e-10      1.4422e-09       6.6x
#   twist           2.8348e-10      1.4498e-09       5.1x
#   shear           1.1300e-10      1.2527e-09      11.1x
#   curvature_xz    2.1806e-10      1.4422e-09       6.6x
#   shear_xz        1.0509e-10      1.2527e-09      11.9x
#
# THE SINGLE NUMBER IS WITHDRAWN WITH THE OLD COLUMN. This block used to conclude
# "as a GATE the resultant channel is ~150x weaker", which was true of the two
# retired columns and is not true of these: the ratio spans 5.1x to 14303x, three
# orders, and no single figure describes it. What the spread says is that the two
# channels are sensitive to DIFFERENT things -- the field channel is 14000x the
# sharper in axial and only 5x in twist -- which is the argument for keeping both
# and is stronger than the number it replaces. The resultant channel is kept for
# what it sees: a different quantity, verified against statics, with four of five
# planted sign defects in its analytic table caught by it.
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
    _, _, res_err, _ = _run(state, SKEW, stiffness_scale=1.0 + eps)
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
    _, _, res_err, _ = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-6)
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
    _, res, _, _ = _run(state, d, scale=scale)
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

    THE SKEW ORIENTATION IS PART OF THE CASE, AND IT IS WHY THIS IS NOT A
    CORPUS-WIDE CONTROL (BO1). `R.T` differs from `R` only when `R` is not
    symmetric, and an axis-aligned member with no roll has `R = I` -- so
    transposing it injects NOTHING. Measured over the corpus, `|R - R.T| = 0`
    exactly on 8 entries and the response there equals the clean value.

    THE OTHER TWO ENTRIES WERE DESCRIBED WRONGLY AND THE SENTENCE IS CORRECTED
    (R120). They were called "near-axis, below the ceiling"; the count was right
    and the cause was not. `onode_just_outside` has `|R - R.T| = 2.000` -- as
    far from symmetric as a rotation gets -- and an injected `to_global` delta of
    **exactly zero**; `straddle_above_lam61_axis` has `|R - R.T| = 1.197` and a
    relative delta of `3.09e-18`. In both the difference is ABSENT from the
    assembled matrix, not present and too small to see. Neither is near-axis, and
    "below the ceiling" describes a response that was never injected.

    The defect is real and this gate sees it, on a member whose frame is actually
    rotated, which is the case the defect describes.

    MEASURED RESPONSE ON THE QUANTITIES THIS TEST ASSERTS, regenerated
    2026-09-06 (R93). The figures here were the retired field error and read
    "every state, at O(1)"; none of these is O(1) and the smallest is 2000x below
    the smallest of those:

        state          field (oob)   resultants
        axial           2.8565e-02   1.7621e+00
        curvature       1.4356e-02   1.1156e+01
        twist           7.1889e-04   5.6707e+00
        shear           2.1497e-02   2.1081e+01
        curvature_xz    8.2813e-03   6.2014e+00
        shear_xz        1.2401e-02   1.1719e+01

    Every state still detects it by nine orders or more against its counter, and
    the resultant channel is the one that is O(1) here. `twist` is the weakest
    field response and is the number to watch if the transform changes.
    """
    _, _, res_err, err = _run(state, SKEW, transpose_transform=True)
    # AGAINST THE CEILING (BO0). The counter-case is the DEFECT; the assertion is
    # that injecting it turns the gate red, and the margin lives in the docstring
    # rather than in a constant.
    assert err > PATCH_TEST_EXACTNESS, (
        f"{state}: one element's transform transposed left the interior "
        f"out-of-balance at {err:.3e}, at or below the ceiling "
        f"{PATCH_TEST_EXACTNESS:.0e}. A wrongly oriented element is invisible "
        "to this gate."
    )
    assert res_err >= RESULTANT_EXACTNESS_COUNTER, (
        f"{state}: the recovered resultants moved by only {res_err:.3e} under a "
        "transposed transform."
    )


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
            _, _, _, err = _run(state, SKEW, stiffness_scale=1.0 + eps)
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


def _run_with_independent_reference(state: str, sec_el, mat_el) -> float:
    """Solve with `sec_el`/`mat_el` while the exact field comes from the MODULE's
    own section and material.

    This is what separates a property of the ELEMENT from a property of the
    measurement. `_run` builds both sides from the same globals, so a change to
    them moves the reference too and the comparison is a beam against itself.
    """
    m_ref, _, _ = _model(SKEW)
    u_ex_local = _exact_local(state, STATIONS)

    global SEC, S355
    sec_before, mat_before = SEC, S355
    try:
        SEC, S355 = sec_el, mat_el
        m, els, r = _model(SKEW)
    finally:
        SEC, S355 = sec_before, mat_before

    u_ex = _to_global(u_ex_local, r)
    k = assemble(m, els)
    n_nodes = len(STATIONS)
    ends = np.concatenate([node_dofs(0), node_dofs(n_nodes - 1)])
    u_pres = np.zeros(m.n_dof)
    u_pres[node_dofs(0)] = u_ex[0]
    u_pres[node_dofs(n_nodes - 1)] = u_ex[-1]
    f = -(k @ u_pres)
    f[ends] = 0.0
    solve(k, f, ends)
    # THE GATE'S QUANTITY, from the INDEPENDENT reference field: `u_ex` is built
    # from the unmodified module state above, so a property error that moves the
    # reference too cannot hide in it.
    return interior_out_of_balance(m, els, u_ex.reshape(-1),
                                   float(STATIONS[-1]), k=k)


@pytest.mark.parametrize("factor", [2.0, 0.5], ids=lambda f: f"E x {f:g}")
def test_a_uniform_SCALAR_factor_on_K_is_invisible(factor: float) -> None:
    """The boundary of what G2.2 certifies, narrowed to what was measured (BH4).

    A scalar factor on every element cancels out of `K u = 0` with the ends
    prescribed, so it cannot move an interior node. `E` is the only property in
    this model that scales K uniformly.

    This asserts a BLINDNESS deliberately, and it is asserted with an INDEPENDENT
    reference -- so it is a property of the gate, not of the harness. The earlier
    version of this test moved the reference too and therefore also reported
    `nu` and a scaled section as invisible; both are caught, see below.
    """
    from dataclasses import replace

    worst = max(_run_with_independent_reference(st, SEC, replace(S355, E=S355.E * factor))
                for st in STATES)
    assert worst <= PATCH_TEST_EXACTNESS, (
        f"E x {factor:g} was DETECTED at {worst:.4e}. A scalar factor on K cannot "
        "move an interior node of a displacement-imposed patch test, so either "
        "the formulation or this docstring is wrong."
    )


# THE FLOORS ARE RE-DERIVED WITH THE QUANTITY (F2.md sec. 5b, Q6), not carried:
# the worst response is 2.1581e-06 for `nu` and 2.8875e-05 for the section, so
# each floor sits an order below its own measurement -- 21.6x and 28.9x. They are
# discrimination floors, asserted from BELOW, so setting them low weakens the
# claim rather than propping it up.
NON_SCALAR_ERRORS = [
    ("nu 0.30 -> 0.45", "nu", 0.45, 1.0e-7),
    ("section x 1.5", "section", 1.5, 1.0e-6),
]


@pytest.mark.parametrize("label, kind, value, floor",
                         NON_SCALAR_ERRORS, ids=[e[0] for e in NON_SCALAR_ERRORS])
def test_a_uniform_NON_scalar_property_error_IS_caught(
    label: str, kind: str, value: float, floor: float
) -> None:
    """The half of the old claim that was false, now asserted the right way round.

    `nu` moves `G/E` and hence `Phi`; a scaled section moves `A` as `D` and `I`
    as `D^3`. Neither is a scalar multiple of K, and with an independent
    reference the gate sees both -- `5.5281e-04` and `7.3011e-03` at this commit,
    eight and nine orders above the ceiling.

    The `floor` here is a discrimination floor, not a tolerance: it asserts the
    response is LARGE, and it is set an order below the measured value so a
    formulation change has to lose an order of sensitivity before it passes.
    """
    from dataclasses import replace

    if kind == "nu":
        sec_el, mat_el = SEC, replace(S355, nu=value)
    else:
        sec_el, mat_el = Section.circular_tube(0.6 * value, 0.012 * value), S355

    worst = max(_run_with_independent_reference(st, sec_el, mat_el)
                for st in STATES)
    assert worst > floor, (  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE
        f"{label} moved the interior field by only {worst:.4e}. The gate is "
        "supposed to see a non-scalar uniform property error; if it no longer "
        "does, the blindness docstring above is wider than the code."
    )


PLANE_STATES = {
    "bending_xy": ("curvature", "shear"),
    "bending_xz": ("curvature_xz", "shear_xz"),
}


@pytest.mark.parametrize("block", ["bending_xy", "bending_xz"])
def test_a_defect_in_ONE_bending_plane_is_caught_by_THAT_plane(block: str) -> None:
    """Each plane's states detect a defect confined to their own block.

    THE MARGIN (R15), re-measured on the shipped quantity: at a `1e-3` defect
    confined to `bending_xz` the smallest detecting state is `2.2929e-08` and the
    largest blind state is `1.2077e-16` -- a separation of **1.90e+08**. Eight
    orders, and it is not a coincidence to be relied on: it is the difference
    between a state that contains the defective block and one whose exact field
    has no content in it at all, so the blind states sit at round-off rather than
    at a small response. (`bending_xy` gives 2.2929e-08 against 1.0064e-16,
    2.28e+08.)
    """
    for state in PLANE_STATES[block]:
        _, _, _, err = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-3, block=block)
        # AGAINST THE CEILING, WHICH IS THE GATE'S OWN DECISION, and not against
        # a response floor. A counter-case is the DEFECT, and the check that it
        # is caught is a comparison with the gate's own ceiling (BO0). The
        # separation this test is about is in the docstring and is nine orders
        # wide; a second constant here would be a threshold outside
        # `tolerances.py` (R80/R85).
        assert err > PATCH_TEST_EXACTNESS, (
            f"{state} did not detect a 1e-3 defect confined to {block}: "
            f"{err:.3e} <= {PATCH_TEST_EXACTNESS:.0e}"
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
        _, _, _, err = _run(state, SKEW, stiffness_scale=1.0 + 1.0e-3, block=block)
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
# `equilibrate` was later used to estimate a conditioning-scaled floor for this
# gate's ceiling; that form was withdrawn after a STOP (F2.md sec. D7 item 6) and
# the function went with it, having no other caller.
# ---------------------------------------------------------------------------
UNIT_SCALES = [1.0, 10.0, 1000.0, 0.001]      # metres, decimetres, mm, km


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
