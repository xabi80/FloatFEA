"""Rigid links as master-slave constraints (D1, D2 step 11).

Reference
---------
Cook, Malkus, Plesha & Witt, *Concepts and Applications of Finite Element
Analysis*, 4th ed., Wiley 2002, §13.2 -- multipoint constraints by
transformation. Przemieniecki §6.5 for the same algebra in the displacement
method.

WHAT A RIGID LINK IS
--------------------
Two nodes that move as one rigid body. The slave's six DOF are determined by the
master's six and the vector ``d`` from master to slave::

    u_s     = u_m + theta_m x d
    theta_s = theta_m

which is EXACT kinematics, not an approximation: a rigid body's velocity field
is linear in the rotation with the lever arm as the coefficient. In matrix form,
with the 3x3 skew of ``d``::

    [ u_s     ]   [ I   -[d]_x ] [ u_m     ]
    [ theta_s ] = [ 0      I   ] [ theta_m ]

**THE LEVER ARM IS THE WHOLE CONTENT.** Drop ``-[d]_x`` and the link becomes a
translation-only tie: the slave follows the master's displacement and ignores its
rotation, so a moment applied at the master produces no force at the slave. That
is `RIGID_LINK_CONSTRAINT`'s named counter-case, and it is the reason this module
has one function that builds the block and nothing that builds it a second way.

SIGN OF THE SKEW, AND WHY IT IS WRITTEN OUT
-------------------------------------------
``theta x d`` with ``theta`` the rotation vector and ``d`` the master-to-slave
offset. Written as a matrix that is ``-[d]_x``, because ``theta x d = -d x
theta`` and ``[d]_x theta = d x theta``. Getting this backwards transposes the
coupling and produces a link that is exactly as wrong in the opposite direction,
which a symmetric test cannot see -- so the test applies a rigid rotation and
checks the DISPLACEMENT it produces at the slave, not only that the energy is
zero.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

DOF_PER_NODE = 6


def skew(vector: NDArray[np.floating]) -> NDArray[np.float64]:
    """``[v]_x`` such that ``[v]_x w = v x w``."""
    v = np.asarray(vector, dtype=np.float64).ravel()
    if v.shape != (3,):
        raise ValueError(f"expected a 3-vector; got shape {v.shape}")
    return np.array(
        [[0.0, -v[2], v[1]], [v[2], 0.0, -v[0]], [-v[1], v[0], 0.0]],
        dtype=np.float64,
    )


def rigid_link_block(offset: NDArray[np.floating]) -> NDArray[np.float64]:
    """The 6x6 mapping master DOF -> slave DOF for an offset master-to-slave.

    ``u_s = u_m + theta_m x d`` and ``theta_s = theta_m``, so the upper-right
    block is ``-[d]_x``.
    """
    d = np.asarray(offset, dtype=np.float64).ravel()
    block = np.eye(DOF_PER_NODE, dtype=np.float64)
    block[:3, 3:] = -skew(d)
    return block


def slave_motion(
    master_motion: NDArray[np.floating], offset: NDArray[np.floating]
) -> NDArray[np.float64]:
    """The slave's six DOF given the master's six, by exact rigid kinematics."""
    motion = np.asarray(master_motion, dtype=np.float64).ravel()
    if motion.shape != (DOF_PER_NODE,):
        raise ValueError(f"expected 6 master DOF; got {motion.shape}")
    return rigid_link_block(offset) @ motion


def constraint_transform(
    n_dof: int, links: dict[int, tuple[int, NDArray[np.floating]]]
) -> NDArray[np.float64]:
    """``T`` mapping the retained DOF onto all DOF, for `links` slave -> (master, d).

    The retained set is every DOF except the slaves'. Reducing a system is then
    ``T^T K T``, and a solved retained vector is expanded back by ``T``.

    A slave that is itself a master is rejected rather than resolved. Chained
    links are a legitimate modelling wish and resolving them takes an ordering
    rule; a rule guessed here would silently pick one, and F3's joints are all
    single-level.
    """
    slaves = set(links)
    masters = {master for master, _ in links.values()}
    chained = slaves & masters
    if chained:
        raise ValueError(
            f"nodes {sorted(chained)} are both a master and a slave. Chained rigid "
            "links need an ordering rule to resolve, and this builds none rather "
            "than guessing one."
        )

    slave_dofs: set[int] = set()
    for slave in links:
        slave_dofs.update(range(DOF_PER_NODE * slave, DOF_PER_NODE * (slave + 1)))
    retained = [i for i in range(n_dof) if i not in slave_dofs]

    t = np.zeros((n_dof, len(retained)), dtype=np.float64)
    column_of = {dof: j for j, dof in enumerate(retained)}
    for dof, j in column_of.items():
        t[dof, j] = 1.0
    for slave, (master, offset) in links.items():
        block = rigid_link_block(offset)
        rows = range(DOF_PER_NODE * slave, DOF_PER_NODE * (slave + 1))
        cols = [column_of[DOF_PER_NODE * master + k] for k in range(DOF_PER_NODE)]
        for local_row, row in enumerate(rows):
            for local_col, col in enumerate(cols):
                t[row, col] = block[local_row, local_col]
    return t


def reduce_matrix(
    matrix: NDArray[np.floating], transform: NDArray[np.floating]
) -> NDArray[np.float64]:
    """``T^T A T``, symmetrised. Used for both stiffness and mass, deliberately."""
    a = np.asarray(matrix, dtype=np.float64)
    t = np.asarray(transform, dtype=np.float64)
    out = t.T @ a @ t
    symmetric: NDArray[np.float64] = 0.5 * (out + out.T)
    return symmetric
