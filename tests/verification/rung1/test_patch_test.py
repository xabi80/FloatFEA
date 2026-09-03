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

**Unequal element lengths.** A uniform mesh cannot distinguish an element that is
exact from one that is merely consistent, because the errors cancel by symmetry.
The mesh here is deliberately irregular.

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

SEC = Section.circular_tube(0.6, 0.012)
# Deliberately irregular: no pair of element lengths in a SMALL-INTEGER RATIO.
# Lengths [3.27, 3.00, 0.90, 0.79, 1.71]; the closest any pairwise ratio comes to
# p/q with p,q <= 5 is 0.0877. Two earlier meshes failed this: one ended at 9.4,
# making the last element exactly 2x the first, and its replacement contained
# 0.9/0.6 = 3/2 exactly and 2.8/1.7 within 0.02 of 5/3.
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
    else:  # pragma: no cover
        raise ValueError(state)
    return u


def _to_global(u_local: np.ndarray, r: np.ndarray) -> np.ndarray:
    """Rotate each node's (translation, rotation) pair into global axes."""
    out = np.empty_like(u_local)
    out[:, :3] = u_local[:, :3] @ r
    out[:, 3:] = u_local[:, 3:] @ r
    return out


def _run(state: str, direction: np.ndarray, stiffness_scale: float = 1.0):
    m, els, r = _model(direction)
    u_ex = _to_global(_exact_local(state, STATIONS), r)

    k = assemble(m, els)
    if stiffness_scale != 1.0:
        from floatfea.assemble.system import element_global_stiffness

        k = k.tolil()
        kb = element_global_stiffness(m, els[1])
        d = np.concatenate([node_dofs(1), node_dofs(2)])
        for i in range(12):
            for j in range(12):
                k[d[i], d[j]] += (stiffness_scale - 1.0) * kb[i, j]
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
    scale = np.abs(u_ex).max()
    err = np.abs(got - u_ex).max() / scale
    return err, res


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear"])
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
    """Meta-test: a uniform mesh lets errors cancel by symmetry, so the states
    above would pass on an element that is merely consistent."""
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
    assert worst > 0.05, (
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
    assert shear / (bending + shear) > 1e-4, "shear term is negligible in state 4"


# Detection thresholds, MEASURED (AX1). A counter-case is one perturbation; the
# threshold is where the state stops seeing one at all, and it is the number a
# later reader needs to judge whether a tolerance change has cost detection.
#
#   state       sensitivity (err/eps)   smallest eps detected at 1e-12
#   axial              1.0908e-01              9.17e-12
#   curvature          3.7161e-02              2.69e-11
#   twist              1.0908e-01              9.17e-12
#   shear              3.0170e-02              3.31e-11   <- weakest
#
# Verified rather than extrapolated: perturbing by the threshold eps lands the
# error on 1e-12 to within 0.3% in every state. So the patch test stops seeing a
# single-element stiffness error below ~3.3e-11 relative. Widening
# PATCH_TEST_EXACTNESS by an order moves that to ~3.3e-10.
#
# These numbers are FROM THE INCOMMENSURATE MESH. On the previous mesh -- which
# contained 0.9/0.6 = 3/2 exactly -- the weakest state's threshold was 1.51e-10,
# so removing the symmetry cancellation improved detection about FIVEFOLD. The
# assertion below caught the old numbers going stale the moment the mesh changed.
DETECTION_THRESHOLD = {
    "axial": 9.17e-12,
    "curvature": 2.69e-11,
    "twist": 9.17e-12,
    "shear": 3.31e-11,
}


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear"])
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


@pytest.mark.parametrize("state", ["axial", "curvature", "twist", "shear"])
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
