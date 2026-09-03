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
# Deliberately irregular: no two elements the same length, and no length a simple
# multiple of another. A uniform mesh lets errors cancel by symmetry.
STATIONS = np.array([0.0, 1.7, 2.3, 5.1, 6.0, 9.1])
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
    # No length an integer multiple of another. The first draft compared every
    # length against the FIRST one, which trivially includes the self-ratio of
    # 1.0 -- and it also caught a real defect: the mesh then ended at 9.4, making
    # the last element exactly 2x the first.
    for i, a in enumerate(lengths):
        for j, b in enumerate(lengths):
            if i == j:
                continue
            ratio = a / b
            if ratio < 1.0:
                continue
            assert abs(ratio - round(ratio)) > 0.05, (
                f"lengths {a} and {b} are commensurate (ratio {ratio:.3f}); "
                "errors can cancel by symmetry on such a mesh"
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
