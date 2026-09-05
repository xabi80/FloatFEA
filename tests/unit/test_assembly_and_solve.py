"""AV3 -- step-3 hygiene: per-case residual, reaction equilibrium, sparse vs dense.

Three items, none negotiable:

* the direct solve reports ``||Ku - f|| / ||f||`` **per solve, never averaged** --
  this is where V4.1's discipline starts, and an outlier hidden in a mean is the
  specific thing it exists to catch;
* the constrained-DOF reactions **sum to the applied load**, per case, as an
  assertion -- the cheapest check on the boundary-condition path and the one most
  often skipped;
* the sparse assembly agrees with a **dense assembly of the same model,
  bit-exact**, built by a different code path so agreement is evidence rather
  than tautology.
"""
from __future__ import annotations

import numpy as np
import pytest

from floatfea.assemble.system import (
    BeamElement,
    assemble,
    assemble_dense,
    element_global_stiffness,
    solve,
)
from floatfea.model.material import S355, Section
from floatfea.model.nodes import Model, Node, element_dofs, node_dofs
from floatfea.tolerances import (
    MATRIX_SYMMETRY,
    MATRIX_SYMMETRY_COUNTER,
    ROUNDOFF_IDENTITY,
    SUBDIVISION_INVARIANCE,
    SUBDIVISION_INVARIANCE_COUNTER,
    TRANSFORM_INVARIANCE,
)

SEC = Section.circular_tube(0.6, 0.012)


TOTAL_LENGTH = 10.0


def _frame(n_el: int = 4, skew: bool = True) -> tuple[Model, list[BeamElement]]:
    """A chain spanning a FIXED total length, subdivided into ``n_el`` members.

    Total length is held constant so that subdivision is the only thing varying.
    An earlier version gave every element the same length, which made the three
    cases three DIFFERENT cantilevers -- and no scaling recovers that, because
    the shear term scales as L while the bending term scales as L^3.
    """
    m = Model()
    d = np.array([1.0, 0.35, 0.22]) if skew else np.array([1.0, 0.0, 0.0])
    d = d / np.linalg.norm(d) * (TOTAL_LENGTH / n_el)
    for i in range(n_el + 1):
        m.nodes.add(Node(*(i * d)))
    els = [BeamElement(i, i + 1, SEC, S355) for i in range(n_el)]
    return m, els


def test_sparse_and_dense_assembly_agree_BIT_EXACT() -> None:
    """Different code paths -- COO triplets with duplicate summation, against an
    explicit scatter-add loop -- so agreement is evidence, not tautology."""
    m, els = _frame()
    k_sp = assemble(m, els).toarray()
    k_de = assemble_dense(m, els)
    assert np.array_equal(k_sp, k_de), (
        f"sparse and dense assembly differ; max |diff| = "
        f"{np.abs(k_sp - k_de).max():.6e}"
    )


def test_the_two_assemblies_are_not_trivially_equal() -> None:
    """Meta-test: two zero matrices are also bit-equal."""
    m, els = _frame()
    k = assemble(m, els).toarray()
    assert np.abs(k).max() > 0.0  # not-a-tolerance: discrimination floor -- asserts a quantity is LARGE, not that an error is small
    assert (k != 0).sum() > 12 * 12, "assembly did not overlap any elements"


def test_assembly_is_symmetric() -> None:
    m, els = _frame()
    k = assemble(m, els).toarray()
    assert np.allclose(k, k.T, rtol=0, atol=TRANSFORM_INVARIANCE * np.abs(k).max())


def test_a_MISINDEXED_scatter_BREAKS_the_symmetry() -> None:
    """BG1: MATRIX_SYMMETRY's counter, injected -- and the injection refuted the
    defect the entry named.

    `MATRIX_SYMMETRY_COUNTER = 1e-2` said it came from "one transposed element
    block ... 3.1e-01". Running it: **an element contribution is symmetric**
    (`max|kg - kg^T| / max|kg| = 3.7e-17`), so transposing one is a no-op and the
    assembly's asymmetry stays at `3.711e-17` -- which is the CLEAN value. The
    named defect could never have been caught because it is not a defect.

    The defect that is real, and that this injects, is a **mis-indexed scatter**:
    the element's columns landing on the wrong node's DOF while its rows land
    correctly. Every entry is still present and only the pattern is wrong, which
    is what a wrong `element_dofs` ordering produces. Measured on this frame:

        transpose the block (the named defect)   3.7107e-17   <- no-op
        columns scattered to the wrong node      7.9020e-02
        upper triangle only                      5.0000e-01
        one off-diagonal entry, 5%               2.5000e-02

    The VALUE 1e-2 survives -- the realistic defect is 8x above it and even a 5%
    single-entry error is 2.5x above it. The sentence explaining it did not.
    """
    m, els = _frame()
    k = assemble(m, els).toarray()
    dofs = element_dofs(els[0].node_a, els[0].node_b)
    kg = element_global_stiffness(m, els[0])
    # Columns scattered to the other node's block; rows correct.
    wrong_columns = list(range(6, 12)) + list(range(6))
    k[np.ix_(dofs, dofs)] += kg[:, wrong_columns] - kg

    asym = float(np.abs(k - k.T).max() / np.abs(k).max())
    assert asym >= MATRIX_SYMMETRY_COUNTER, (
        f"a mis-indexed scatter left max|K - K^T| / max|K| = {asym:.3e}, "
        f"below the declared counter-case {MATRIX_SYMMETRY_COUNTER:.3e}. The "
        "symmetry check cannot see the defect its counter names."
    )
    assert asym > MATRIX_SYMMETRY, "the counter must exceed the ceiling"


def test_the_solve_reports_a_PER_CASE_residual() -> None:
    m, els = _frame()
    k = assemble(m, els)
    f = np.zeros(m.n_dof)
    f[node_dofs(len(m.nodes) - 1)[1]] = 1.0e5
    r = solve(k, f, node_dofs(0))
    assert r.residual < TRANSFORM_INVARIANCE, f"residual {r.residual:.3e}"
    assert isinstance(r.residual, float), "residual must be per-case, not aggregated"


@pytest.mark.parametrize("direction", [0, 1, 2])
def test_reactions_balance_the_applied_load(direction: int) -> None:
    """Equilibrium on the boundary-condition path, asserted per case."""
    m, els = _frame()
    k = assemble(m, els)
    f = np.zeros(m.n_dof)
    f[node_dofs(len(m.nodes) - 1)[direction]] = 1.0e5
    r = solve(k, f, node_dofs(0))

    applied = np.array([f[i::6].sum() for i in range(3)])
    react = np.array([r.reactions[i::6].sum() for i in range(3)])
    assert np.allclose(react + applied, 0.0, atol=TRANSFORM_INVARIANCE * abs(applied).max())
    assert r.reaction_imbalance < TRANSFORM_INVARIANCE


def test_reaction_equilibrium_CAN_FAIL() -> None:
    """Negative control: a reaction computed on the wrong DOF set must show up.

    Without this the equilibrium assertion could pass on any model whose
    reactions happen to be small.
    """
    m, els = _frame()
    k = assemble(m, els)
    f = np.zeros(m.n_dof)
    f[node_dofs(len(m.nodes) - 1)[1]] = 1.0e5
    r = solve(k, f, node_dofs(0))
    # Drop one component of the reaction -- the defect a wrong fixed-set produces.
    broken = r.reactions.copy()
    broken[node_dofs(0)[1]] = 0.0
    applied = np.array([f[i::6].sum() for i in range(3)])
    react = np.array([broken[i::6].sum() for i in range(3)])
    assert not np.allclose(react + applied, 0.0, atol=1e-6 * abs(applied).max())  # not-a-tolerance: negative control -- asserts the BROKEN reaction FAILS equilibrium


def test_a_fully_fixed_model_is_refused() -> None:
    m, els = _frame(n_el=1)
    k = assemble(m, els)
    allof = np.arange(m.n_dof)
    with pytest.raises(ValueError, match="nothing to solve"):
        solve(k, np.zeros(m.n_dof), allof)


def test_SUBDIVISION_changes_nothing_under_an_end_load() -> None:
    """Nodal exactness survives assembly.

    The element is exact for constant section and constant load, so a cantilever
    of fixed total length must give the SAME tip response whether it is one
    element or five. This is the assembled form of the AU1 checkpoint, and it is
    the statement that makes refinement the wrong response to a bad answer.
    """
    tips = []
    for n_el in (1, 2, 5, 11):
        m, els = _frame(n_el=n_el)
        total = float(np.linalg.norm(m.nodes[len(m.nodes) - 1].xyz))
        assert total == pytest.approx(TOTAL_LENGTH, rel=ROUNDOFF_IDENTITY)
        k = assemble(m, els)
        f = np.zeros(m.n_dof)
        last = node_dofs(len(m.nodes) - 1)
        f[last[1]] = 1.0e5
        r = solve(k, f, node_dofs(0))
        assert r.residual < TRANSFORM_INVARIANCE
        tips.append(r.u[last[1]])
    dev = max(abs(t / tips[0] - 1.0) for t in tips)
    assert dev <= SUBDIVISION_INVARIANCE, (
        f"subdivision changed the tip response by {dev:.3e}: {tips}. The element "
        "is nodally exact, so this is a formulation or assembly error -- "
        "refinement is not the response."
    )


def test_the_subdivision_counter_case_is_reachable() -> None:
    """AW2: a one-part-in-10^7 stiffness error in ONE member must be caught.

    Measured linear in the perturbation: 4.84e-04 at 1e-3, 4.85e-08 at 1e-7. The
    counter consumes that value, so widening SUBDIVISION_INVARIANCE toward it
    breaks this test.
    """
    eps = 1.0e-7
    tips = []
    for scale in (1.0, 1.0 + eps):
        m, els = _frame(n_el=5)
        k = assemble(m, els).tolil()
        d = np.arange(12)
        kb = element_global_stiffness(m, els[0])
        for i in range(12):
            for j in range(12):
                k[d[i], d[j]] += (scale - 1.0) * kb[i, j]
        f = np.zeros(m.n_dof)
        last = node_dofs(len(m.nodes) - 1)
        f[last[1]] = 1.0e5
        tips.append(solve(k.tocsr(), f, node_dofs(0)).u[last[1]])

    dev = abs(tips[1] / tips[0] - 1.0)
    assert dev >= SUBDIVISION_INVARIANCE_COUNTER, (
        f"a {eps:.0e} stiffness error in one member moved the tip by only "
        f"{dev:.3e}, below the counter-case {SUBDIVISION_INVARIANCE_COUNTER:.3e}"
    )
