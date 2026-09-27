"""End-release condensation for the 12-DOF beam element (D1, D2 step 11).

Reference
---------
Przemieniecki, J.S., *Theory of Matrix Structural Analysis*, McGraw-Hill 1968
(Dover reprint 1985), §6.4 -- static condensation of a released end force
component. Cross-checked against Cook, Malkus, Plesha & Witt, *Concepts and
Applications of Finite Element Analysis*, 4th ed., §8.9.

WHAT A RELEASE IS
-----------------
A released DOF is one at which the element transmits **no force**. The element
still has that displacement -- it is free to take whatever value makes the force
zero -- so it is eliminated from the element's contribution rather than
restrained. Partitioning the local matrix into retained ``r`` and released ``c``::

    [ k_rr  k_rc ] [ d_r ]   [ f_r ]
    [ k_cr  k_cc ] [ d_c ] = [  0  ]

gives ``d_c = -k_cc^-1 k_cr d_r`` and the condensed stiffness::

    k~ = k_rr - k_rc k_cc^-1 k_cr

with the released rows and columns zeroed in the 12x12 so the DOF numbering
never changes. **A release is not a restraint and it is not a deleted DOF**, and
the difference is observable: a restraint would hold the rotation at zero and
transmit the moment, which is the opposite of what a pin does.

THE SAME RECOVERY MATRIX APPLIES TO THE MASS
--------------------------------------------
``d_c`` is a linear function of ``d_r``, so the released element's kinematics are
``d = R d_r`` with ``R`` the recovery matrix below, and the consistent mass
condenses as ``m~ = R^T m R``. **It is not ``m_rr``.** Dropping the coupling
would give a released member the wrong inertia, and a free-free frequency is the
quantity that would notice.

WHY THE RELEASED SET IS CHECKED FOR SOLVABILITY
-----------------------------------------------
``k_cc`` is singular when the released set contains a rigid-body freedom of the
element -- release both end rotations *and* both end translations in one plane
and there is nothing left to invert. That **raises**; it does not fall back to a
pseudo-inverse. A silently pseudo-inverted release is a member that transmits
something nobody chose.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from floatfea.element.beam import DOF_PER_ELEMENT

# Local DOF indices, A then B, matching `model/nodes.py` and `element/beam.py`.
MOMENT_DOFS: dict[str, tuple[int, int]] = {
    "x": (3, 9),
    "y": (4, 10),
    "z": (5, 11),
}
"""The rotational DOF at each end, by the local axis the moment is about.

`MOMENT_DOFS["y"][0]` is node A's rotation about local y, and releasing it
releases the moment in the x-z bending plane at that end.
"""


def recovery_matrix(
    k_local: NDArray[np.floating], released: tuple[int, ...]
) -> NDArray[np.float64]:
    """``R`` such that ``d = R d_r``, shaped ``(12, 12)``.

    Columns of the released DOFs are zero -- those displacements are not
    independent -- and the released rows carry ``-k_cc^-1 k_cr``. Applying ``R``
    to a retained displacement vector reconstructs the released rotations, which
    is what the post-processor needs to recover the member's real end
    displacements after a solve.
    """
    k = np.asarray(k_local, dtype=np.float64)
    if k.shape != (DOF_PER_ELEMENT, DOF_PER_ELEMENT):
        raise ValueError(
            f"expected a {DOF_PER_ELEMENT}x{DOF_PER_ELEMENT} local matrix; got {k.shape}"
        )
    if len(set(released)) != len(released):
        raise ValueError(f"a DOF is released twice: {released}")
    for dof in released:
        if not 0 <= dof < DOF_PER_ELEMENT:
            raise ValueError(f"released DOF {dof} is outside 0..{DOF_PER_ELEMENT - 1}")

    c = np.array(sorted(released), dtype=np.int64)
    r = np.array([i for i in range(DOF_PER_ELEMENT) if i not in set(released)], dtype=np.int64)

    k_cc = k[np.ix_(c, c)]
    # A rigid-body freedom inside the released set makes this singular. It RAISES
    # rather than falling back to a pseudo-inverse, per the module docstring.
    if np.linalg.matrix_rank(k_cc) < k_cc.shape[0]:
        raise ValueError(
            f"the released set {tuple(int(i) for i in c)} makes k_cc singular, so "
            "the released displacements are not determined by the retained ones. "
            "That is a released rigid-body freedom of the element, not a pin: "
            "releasing it leaves the member with nothing to transmit and the "
            "condensation has no solution."
        )

    recovery = np.zeros((DOF_PER_ELEMENT, DOF_PER_ELEMENT), dtype=np.float64)
    recovery[r, r] = 1.0
    recovery[np.ix_(c, r)] = -np.linalg.solve(k_cc, k[np.ix_(c, r)])
    return recovery


def condense(matrix: NDArray[np.floating], recovery: NDArray[np.floating]) -> NDArray[np.float64]:
    """``R^T A R`` -- the condensed stiffness or the condensed mass.

    ONE FUNCTION FOR BOTH ON PURPOSE. The recovery matrix is a statement about
    the element's kinematics, and stiffness and mass are both quadratic forms on
    those kinematics. Two functions would let the mass be condensed by a
    different rule than the stiffness, which is the defect `RIGID_LINK`'s dropped
    lever arm is the other instance of.
    """
    a = np.asarray(matrix, dtype=np.float64)
    r = np.asarray(recovery, dtype=np.float64)
    out = r.T @ a @ r
    return 0.5 * (out + out.T)


def released_local_stiffness(
    k_local: NDArray[np.floating], released: tuple[int, ...]
) -> NDArray[np.float64]:
    """The 12x12 local stiffness with `released` transmitting no force."""
    return condense(k_local, recovery_matrix(k_local, released))


def gimbal_release(end: str, locked_axis: str) -> tuple[int, ...]:
    """DJ0's joint model: the two free moments released, the locked one transmitted.

    A two-rotation gimbal transmits the moment about the axis it is locked
    against and neither of the other two. `end` is ``"a"`` or ``"b"``;
    `locked_axis` is the LOCAL axis whose moment is carried.

    THE PATTERN IS TWO RELEASES AND NOT THREE. Releasing all three is a ball
    joint, which is a different connection and which leaves the member's
    torsional freedom undetermined when both ends are so released -- the
    singularity `recovery_matrix` raises on.
    """
    if end not in ("a", "b"):
        raise ValueError(f"end must be 'a' or 'b'; got {end!r}")
    if locked_axis not in MOMENT_DOFS:
        raise ValueError(f"locked_axis must be one of {sorted(MOMENT_DOFS)}; got {locked_axis!r}")
    which = 0 if end == "a" else 1
    return tuple(MOMENT_DOFS[axis][which] for axis in sorted(MOMENT_DOFS) if axis != locked_axis)
