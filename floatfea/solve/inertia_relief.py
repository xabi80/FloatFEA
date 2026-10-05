"""EK0(e) and DQ8: the dynamic case -- joint reactions, inertia relief, per body.

WHAT INERTIA RELIEF IS DOING HERE. A dry superstructure body under its joint reactions
is not in equilibrium: the reactions are what accelerates it. So the body is solved free,
with the rigid-body acceleration the load implies subtracted as a d'Alembert field. The
six Lagrange multipliers on the rigid modes ARE the residual reactions
(`PLAN.md:305-307`), which is why they double as the diagnostic DQ8 reads.

THE ACCELERATION IS A PREDICTION, NOT AN INPUT. `a = (R^T M R)^-1 R^T f` is computed from
the FE mass matrix and the applied joint reactions alone. FloatSim's own `xi_ddot` for
that body never enters the solve -- which is what lets DQ8 assert the two agree. If the
acceleration were taken from the export the assertion would compare a number with itself,
which is R600's defect.

THE RIGID MODES COME FROM NODAL COORDINATES ONLY (`rigid_projection`, DY1a). Nothing the
builder computed enters them, so `R^T M R` reads the assembled mass matrix rather than an
intermediate.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from floatfea.assemble.system import assemble_dense
from floatfea.element.constraints import constraint_transform, reduce_matrix
from floatfea.model.nodes import DOF_PER_NODE
from floatfea.model.platform import BodyModel, body_mass_matrix, rigid_projection

__all__ = ["ReliefResult", "solve_inertia_relief"]


@dataclass(frozen=True)
class ReliefResult:
    """One body, one timestep: the relief solve and the quantities DQ8 reads."""

    body: str
    acceleration: NDArray[np.float64]
    """The 6-component rigid acceleration the applied load implies, about the body's CoG.

    Translations in m/s^2, rotations in rad/s^2. This is the FE's PREDICTION and the
    quantity DQ8 compares against FloatSim's.
    """

    residual: NDArray[np.float64]
    """`R^T (f - M R a)`, the 6-component imbalance left after relief.

    Zero to round-off by construction -- it is the equation `a` solves -- so it measures
    the solve rather than the physics, and DQ8's own residual is formed separately from
    the joint reactions and `M a`.
    """

    applied_resultant: NDArray[np.float64]
    """`R^T f`: the 6-component resultant of the applied joint reactions about the CoG."""

    reference_point: NDArray[np.float64]
    mass: float
    u: NDArray[np.float64]
    """Deformation in the RETAINED DOF space, rigid motion removed."""

    retained: list[int]
    u_full: NDArray[np.float64]
    """Deformation in the body's FULL DOF numbering, expanded through the link."""


def _links(body: BodyModel) -> dict[int, tuple[int, NDArray[np.floating]]]:
    """The body's rigid links, slave -> (master, offset); empty when the link is zero."""
    if body.remainder_node == body.centre_node:
        return {}
    coords = body.model.nodes.coords()
    offset: NDArray[np.floating] = coords[body.remainder_node] - coords[body.centre_node]
    return {body.remainder_node: (body.centre_node, offset)}


def solve_inertia_relief(body: BodyModel, applied: NDArray[np.float64]) -> ReliefResult:
    """Solve one body free under `applied`, with the implied rigid acceleration relieved.

    `applied` is the full-DOF nodal load vector -- the joint reactions mapped onto the
    body's joint nodes. The remainder's rigid link is reduced out first, exactly as in the
    static case, because the slave node carries half the body's mass and is attached by a
    constraint rather than an element.
    """
    n_dof = body.model.n_dof
    applied = np.asarray(applied, dtype=np.float64)
    if applied.shape != (n_dof,):
        raise ValueError(f"applied must have shape ({n_dof},); got {applied.shape}")

    k_full = assemble_dense(body.model, body.elements)
    m_full = body_mass_matrix(body)

    links = _links(body)
    if links:
        t_c = constraint_transform(n_dof, links)
        # Whole NODES are removed, never part of one, so the retained node list is
        # what the coordinates must be indexed by -- deriving it from a stride over
        # the DOF list would be correct only while the slave is the last node.
        retained_nodes = [i for i in range(n_dof // DOF_PER_NODE) if i not in links]
        retained = [
            d for i in retained_nodes for d in range(DOF_PER_NODE * i, DOF_PER_NODE * (i + 1))
        ]
        if t_c.shape[1] != len(retained):
            raise AssertionError(
                f"the retained rule here keeps {len(retained)} DOF and "
                f"constraint_transform keeps {t_c.shape[1]}; the orderings have drifted."
            )
        k = reduce_matrix(k_full, t_c)
        m = reduce_matrix(m_full, t_c)
        f = t_c.T @ applied
        coords = body.model.nodes.coords()[retained_nodes]
    else:
        retained = list(range(n_dof))
        k, m, f = k_full, m_full, applied
        coords = body.model.nodes.coords()

    # The CoG of the REDUCED system, so the rigid modes are about the point the
    # acceleration is reported at. `rigid_properties` would re-read the full matrix.
    t0 = rigid_projection(coords, np.zeros(3))
    m6_0 = t0.T @ m @ t0
    mass = float(m6_0[0, 0])
    if mass <= 0.0:
        raise ValueError(f"{body.name!r} has non-positive reduced mass {mass!r}")
    cog = np.array([m6_0[1, 5], m6_0[2, 3], m6_0[0, 4]], dtype=np.float64) / mass

    r = rigid_projection(coords, cog)
    m6 = r.T @ m @ r
    accel = np.asarray(np.linalg.solve(m6, r.T @ f), dtype=np.float64)

    f_relief = f - m @ (r @ accel)
    residual = r.T @ f_relief

    # Constrain the six rigid modes out with Lagrange multipliers rather than fixing
    # arbitrary DOF: fixing DOF would put a support reaction into the answer, and the
    # whole point is that no support exists.
    n = k.shape[0]
    kkt = np.zeros((n + 6, n + 6), dtype=np.float64)
    kkt[:n, :n] = k
    kkt[:n, n:] = r
    kkt[n:, :n] = r.T
    rhs = np.concatenate([f_relief, np.zeros(6)])
    sol = np.linalg.solve(kkt, rhs)

    u_red = sol[:n]
    u_full = (t_c @ u_red) if links else u_red
    return ReliefResult(
        body=body.name,
        acceleration=accel,
        residual=residual,
        applied_resultant=r.T @ f,
        reference_point=cog,
        mass=mass,
        u=u_red,
        retained=retained,
        u_full=np.asarray(u_full, dtype=np.float64),
    )
