"""EK1: member end forces in the member's own local frame.

`f_local = k_local @ T @ u_global`, which is the element's own equilibrium rather than a
post-processing formula: the same `local_stiffness` and the same `rotation_matrix` the
assembler used, so a member force cannot disagree with the solve that produced it.

SIGN AND COMPONENT ORDER ARE `docs/conventions.md`'s, not this module's. The local axes
come from `member_local_axes`, so `N` is along the member from A to B, `Vy`/`Vz` are the
two local shears, `T` is torsion about the member axis and `My`/`Mz` the two bending
moments. The returned values are the forces the ELEMENT exerts on its nodes at each end,
which is why end B's axial has the opposite sign to end A's under pure tension -- a
reader comparing the two ends is looking at an action and a reaction, not at a
discrepancy.

ONE ELEMENT PER MEMBER, at F3's mesh. EK1 asks for every element node along a member and
asks the report to state the count; `BodyModel.elements` builds exactly one
`BeamElement` per `Member`, so the stations are the member's two ends. A refined mesh
would give more and this function does not care how many there are.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from floatfea.element.beam import local_stiffness
from floatfea.element.transform import rotation_matrix, transformation
from floatfea.model.nodes import element_dofs
from floatfea.model.platform import BodyModel, Member

__all__ = ["COMPONENTS", "MemberForces", "member_forces"]

COMPONENTS = ("N", "Vy", "Vz", "T", "My", "Mz")
"""EK1's six, in the order the local 6-vector carries them."""


@dataclass(frozen=True)
class MemberForces:
    """One member's end forces at one timestep, local frame."""

    label: str
    body: str
    end_a: NDArray[np.float64]
    """`(6,)` -- N, Vy, Vz, T, My, Mz at end A."""

    end_b: NDArray[np.float64]
    """`(6,)` at end B."""

    @property
    def stations(self) -> tuple[NDArray[np.float64], ...]:
        """Both ends, so a caller can take a max over stations without naming them."""
        return (self.end_a, self.end_b)


def member_forces(body: BodyModel, member: Member, u_global: NDArray[np.float64]) -> MemberForces:
    """End forces for one member from a FULL-DOF global displacement vector.

    `u_global` must be in the body's full DOF numbering. A caller that solved a reduced
    system expands first: passing a reduced vector would silently read the wrong DOF,
    which is why this takes no `retained` argument to get confused about.
    """
    n_dof = body.model.n_dof
    u_global = np.asarray(u_global, dtype=np.float64)
    if u_global.shape != (n_dof,):
        raise ValueError(
            f"u_global must have shape ({n_dof},) for {body.name!r}; got {u_global.shape}. "
            "A reduced vector has to be expanded through the constraint transform first."
        )

    coords = body.model.nodes.coords()
    a, b = coords[member.node_a], coords[member.node_b]
    r = rotation_matrix(a, b)
    t = transformation(r)
    k_local = local_stiffness(member.section, body.material, member.length)

    f_local = k_local @ (t @ u_global[element_dofs(member.node_a, member.node_b)])
    return MemberForces(
        label=member.label,
        body=body.name,
        end_a=np.array(f_local[0:6], dtype=np.float64),
        end_b=np.array(f_local[6:12], dtype=np.float64),
    )
