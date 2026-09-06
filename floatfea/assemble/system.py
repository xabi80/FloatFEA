"""Sparse assembly, boundary conditions, and the direct solve (D2 step 3).

Diagnostics are **per solve, never averaged** (`CLAUDE.md` § Non-negotiables).
`SolveResult` carries the equilibrium residual and the reaction check for the
single case it describes; there is deliberately no aggregate, because an outlier
hidden in a mean is the specific thing these numbers exist to catch. This is
where V4.1's discipline starts, and it costs one line.

`equilibrate` used to live here. BD2 took it off the solve path
(`docs/milestones/F2.md` sec. R8 has that measurement) and BH1 gave it a second
life estimating a conditioning-scaled floor for G2.2's ceiling. That floor was
withdrawn after a STOP (sec. D7 item 6), which left the function with no caller,
so it is gone: dead code with a test around it reads like coverage.
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


@dataclass(frozen=True)
class SolveResult:
    """One solve. Every diagnostic here describes THIS case only."""

    u: NDArray[np.float64]
    reactions: NDArray[np.float64]
    residual: float
    """``||K u - f|| / ||f||`` over the free DOF, for this case.

    Its denominator is a property of the LOAD, and across the cases G2.2 runs it
    varies by eight orders, so a ceiling on it is a ceiling on the load case
    rather than on the solve (R45). `backward_error` is what G2.2 gates.

    **It is still gated in two places**, and this docstring said "Reported, not
    gated" while they existed: `tests/unit/test_assembly_and_solve.py:133` and
    `:197`, both against `TRANSFORM_INVARIANCE` -- a tolerance borrowed from
    another quantity entirely. That reuse is R33's species and belongs to step
    4a's sweep; it is named here rather than left to contradict the sentence
    above it.
    """
    backward_error: float
    """``||K u - f|| / (||K||_max ||u||_2 + ||f||_2)`` -- the standard
    normalisation, and the one that is gated.

    Dimensionless, bounded by a small multiple of eps for a backward-stable
    factorisation whatever the scaling of the problem. ``||K||_max`` is the
    largest-magnitude entry: a norm choice, so it is named here rather than left
    for a reader to infer.
    """
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
    resid_abs = float(np.linalg.norm(kff @ uf - ff))
    denom = np.linalg.norm(ff)
    residual = float(resid_abs / denom) if denom > 0 else 0.0

    # Backward error: how large a perturbation of THIS system the computed
    # solution solves exactly. The denominator cannot collapse the way ||f||
    # alone does, which is what made the residual a ceiling on the load case.
    scale = float(abs(kff).max() * np.linalg.norm(uf) + denom)
    backward_error = float(resid_abs / scale) if scale > 0 else 0.0

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
                       backward_error=backward_error,
                       reaction_imbalance=imbalance)
