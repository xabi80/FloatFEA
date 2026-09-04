"""Sparse assembly, boundary conditions, and the direct solve (D2 step 3).

Diagnostics are **per solve, never averaged** (`CLAUDE.md` § Non-negotiables).
`SolveResult` carries the equilibrium residual and the reaction check for the
single case it describes; there is deliberately no aggregate, because an outlier
hidden in a mean is the specific thing these numbers exist to catch. This is
where V4.1's discipline starts, and it costs one line.

`equilibrate` is a tested utility and is **not** on the solve path -- see its
docstring, and BD2 in `docs/milestones/F2.md`.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from numpy.typing import NDArray

from floatfea.determinism import SPARSE_PERMC_SPEC
from floatfea.element.beam import local_stiffness
from floatfea.element.transform import rotation_matrix, to_global
from floatfea.model.material import Material, Section
from floatfea.model.nodes import Model, element_dofs


@dataclass(frozen=True)
class BeamElement:
    """A two-node member. Orientation is explicit or defaulted per `local_axes`."""

    node_a: int
    node_b: int
    section: Section
    material: Material
    orientation_node: NDArray[np.float64] | None = None
    roll_rad: float = 0.0


def equilibrate(k: sp.spmatrix) -> tuple[sp.csc_matrix, NDArray[np.float64]]:
    """Symmetric diagonal equilibration: ``(D^-1/2 K D^-1/2, sqrt(diag K))``.

    **A tested utility, NOT on the solve path (BD2).** `solve` factorises the
    original matrix.

    What it does. A beam stiffness mixes translational and rotational DOF, whose
    diagonal entries scale **oppositely** under a change of length unit: with
    lengths x S, translational entries go as ``S^-1`` (``EA/L``, ``12EI/L^3``) and
    rotational as ``S^+1`` (``4EI/L``), coupling (``6EI/L^2``) unchanged --
    measured on this element to four digits. Since ``diag(SKS) = S diag(K) S``,
    the scaled matrix is algebraically invariant, so ``cond(K~) = 3.85e2`` at
    every unit system where ``cond(K_ff)`` runs ``9.2e2 .. 6.0e8``.

    Why it is not on the solve path. It was put there on a claim that the
    unit-invariance of the patch test "required two fixes". The ablation refutes
    that: **the error measure alone is necessary and sufficient**. All four
    cells, worst error over the six patch-test states at each length-unit factor
    ``S``, ceiling ``1e-12``::

        S           1e-4    1e-3    1e-2     0.1       1      10     100     1e3     1e4 | worst  breach
        eq + wtd  2.0e-14 2.7e-14 2.0e-14 2.5e-14 7.9e-15 1.1e-14 3.1e-14 2.5e-14 3.2e-14| 3.2e-14  none
        -- + wtd  2.0e-13 1.6e-13 7.6e-14 1.3e-13 1.3e-14 1.2e-14 2.4e-14 4.9e-14 5.4e-14| 2.0e-13  none
        eq + mix  2.1e-11 2.8e-12 2.0e-13 2.5e-14 1.9e-15 9.9e-15 3.5e-14 5.8e-13 7.8e-12| 2.1e-11  1e-4
        -- + mix  2.1e-10 1.7e-11 4.2e-13 1.3e-13 4.2e-15 4.2e-14 1.5e-13 1.9e-11 1.3e-10| 2.1e-10  1e-4

    The measure alone (row 2) breaches at no scale; that is the whole of the fix.

    **CORRECTION (R34).** An earlier version of this docstring added "and
    equilibration alone leaves the kilometre breach exactly where it was". Row 3
    refutes it: equilibration alone is precisely what removes the kilometre
    breach, ``1.9e-11 -> 5.8e-13``. What it does not do is remove the other
    three (``S = 1e-4``, ``1e-3``, ``1e4``), which is why it is not sufficient
    and the measure is. The conclusion stands; the mechanism as stated was
    false, and it was written one commit after BC1 named exactly this shape of
    claim. See `docs/milestones/F2.md` sec. R8, "The fourth cell".

    The replacement justification -- a "6x" improvement -- was a ratio of
    extremes; per scale the benefit runs

        S      1e-4  1e-3  1e-2   0.1     1    10   100  1e3   1e4
        ratio  9.93  5.84  3.87  5.10  1.58  1.08  0.77 1.97  1.69

    median 1.97 and **below 1 at S = 100**. A production solve-path change with no
    gate, no test through the solve, and a benefit that is sometimes negative does
    not stay. Deleting it left 289 tests passing, which is the measurement that
    settled it.

    Retained as a utility because the conditioning property is real and tested,
    and it is a candidate for F3 if conditioning bites on the full model.
    """
    d = np.sqrt(np.abs(k.diagonal()))
    if not np.all(d > 0.0):
        raise ValueError(
            "a free DOF has zero diagonal stiffness; the system is singular "
            "before equilibration and the caller has an unconstrained mechanism."
        )
    dinv = sp.diags(1.0 / d)
    return (dinv @ k @ dinv).tocsc(), d


@dataclass(frozen=True)
class SolveResult:
    """One solve. Every diagnostic here describes THIS case only."""

    u: NDArray[np.float64]
    reactions: NDArray[np.float64]
    residual: float
    """``||K u - f|| / ||f||`` over the free DOF, for this case."""
    reaction_imbalance: float
    """``||sum(reactions) + sum(applied)|| / ||applied||``, translations only."""


def element_length(model: Model, e: BeamElement) -> float:
    a = model.nodes[e.node_a].xyz
    b = model.nodes[e.node_b].xyz
    return float(np.linalg.norm(b - a))


def element_global_stiffness(model: Model, e: BeamElement) -> NDArray[np.float64]:
    a = model.nodes[e.node_a].xyz
    b = model.nodes[e.node_b].xyz
    k_loc = local_stiffness(e.section, e.material, element_length(model, e))
    r = rotation_matrix(a, b, orientation_node=e.orientation_node, roll_rad=e.roll_rad)
    return to_global(k_loc, r)


def assemble(model: Model, elements: list[BeamElement]) -> sp.csr_matrix:
    """Sparse global stiffness, COO triplets to CSR.

    Element order and DOF order are both insertion order, so the triplet list is
    deterministic; `scipy` sums duplicates on conversion, which is the assembly.
    """
    n = model.n_dof
    rows: list[NDArray[np.int64]] = []
    cols: list[NDArray[np.int64]] = []
    vals: list[NDArray[np.float64]] = []
    for e in elements:
        dofs = element_dofs(e.node_a, e.node_b)
        kg = element_global_stiffness(model, e)
        rr, cc = np.meshgrid(dofs, dofs, indexing="ij")
        rows.append(rr.ravel())
        cols.append(cc.ravel())
        vals.append(kg.ravel())
    if not elements:
        return sp.csr_matrix((n, n))
    return sp.coo_matrix(
        (np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
        shape=(n, n),
    ).tocsr()


def assemble_dense(model: Model, elements: list[BeamElement]) -> NDArray[np.float64]:
    """Dense assembly by explicit scatter-add, for the AV3 cross-check.

    Deliberately a different code path -- an index loop rather than COO triplets
    and duplicate summation -- so that agreeing bit-exactly is evidence rather
    than tautology.
    """
    n = model.n_dof
    k = np.zeros((n, n), dtype=np.float64)
    for e in elements:
        dofs = element_dofs(e.node_a, e.node_b)
        kg = element_global_stiffness(model, e)
        for i, gi in enumerate(dofs):
            for j, gj in enumerate(dofs):
                k[gi, gj] += kg[i, j]
    return k


def solve(
    k: sp.csr_matrix,
    f: NDArray[np.floating],
    fixed: NDArray[np.integer],
) -> SolveResult:
    """Direct solve with the fixed DOF eliminated, and its own diagnostics.

    The factorisation's fill-reducing ordering is pinned via
    `determinism.SPARSE_PERMC_SPEC`: a permutation chosen by a heuristic that
    varies with library version would move stored results with no code change.
    """
    n = k.shape[0]
    f = np.asarray(f, dtype=np.float64)
    fixed = np.unique(np.asarray(fixed, dtype=np.int64))
    free = np.setdiff1d(np.arange(n, dtype=np.int64), fixed)
    if free.size == 0:
        raise ValueError("every DOF is fixed; there is nothing to solve")

    kff = k[free][:, free].tocsc()
    lu = spla.splu(kff, permc_spec=SPARSE_PERMC_SPEC)
    uf = lu.solve(f[free])

    u = np.zeros(n, dtype=np.float64)
    u[free] = uf

    # Per-case equilibrium residual. Never averaged across cases.
    # Residual on the ORIGINAL system, not the equilibrated one: the equilibrated
    # residual would be small by construction and would not describe the solve the
    # caller asked for.
    ff = f[free]
    denom = np.linalg.norm(ff)
    residual = float(np.linalg.norm(kff @ uf - ff) / denom) if denom > 0 else 0.0

    # Reactions at the fixed DOF, and the equilibrium they must satisfy.
    reactions = np.zeros(n, dtype=np.float64)
    reactions[fixed] = (k @ u)[fixed] - f[fixed]

    applied_t = np.array([f[i::6][:].sum() for i in range(3)])
    react_t = np.array([reactions[i::6][:].sum() for i in range(3)])
    scale = np.linalg.norm(applied_t)
    imbalance = (
        float(np.linalg.norm(react_t + applied_t) / scale) if scale > 0 else 0.0
    )
    return SolveResult(u=u, reactions=reactions, residual=residual,
                       reaction_imbalance=imbalance)
