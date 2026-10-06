"""EK1: member end forces in the member's own local frame.

`f_local = k_local @ T @ u - f_eq_local`, which is the element's own equilibrium: the
same `local_stiffness` and `rotation_matrix` the assembler used, MINUS the element's own
equivalent nodal load.

R663. THE SUBTRACTION WAS MISSING AND IT IS NOT A REFINEMENT. `k u` carries the rigid
null space, so its two end shears self-equilibrate IDENTICALLY -- `Vz_A + Vz_B = 0`
exactly -- and a member's own distributed weight can therefore never appear in them. On
the platform arms that put every shear 25.0000% low, every root moment 5.56% high, and
the tip moment at exactly `-mu L^2 / 12` where a roller support carries none at all.
Measured: with the subtraction, the tip shear is `3065625.000000 N`, the support reaction
to every digit, and `Vz_A + Vz_B` is the member's weight `1532812.5 N`.

The check that should have caught it did the opposite: "reaction minus half the member
weight" is the DEFECTIVE formula's own identity, so it agreed with the bug and would have
reddened on the fix. The test that catches this is conservation -- the end shears must sum
to the load the member carries -- not a comparison with a hand-computed end value.

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

from floatfea.assemble.system import element_global_mass
from floatfea.element.beam import local_stiffness
from floatfea.element.transform import rotation_matrix, transformation
from floatfea.model.nodes import element_dofs
from floatfea.model.platform import BodyModel, Member

__all__ = ["COMPONENTS", "MemberForces", "element_equivalent_load", "member_forces"]

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


def element_equivalent_load(
    body: BodyModel, member: Member, accel_full: NDArray[np.float64]
) -> NDArray[np.float64]:
    """The element's 12-DOF equivalent nodal load under a FULL-DOF acceleration field.

    `M_e @ a_e`, consistent with the element mass the assembler used. The caller supplies
    the field, because what loads an element differs by case and this module must not
    guess: for the static case it is gravity on every translation; for an inertia-relief
    case it is MINUS the rigid acceleration field, the d'Alembert body force.
    """
    n_dof = body.model.n_dof
    accel_full = np.asarray(accel_full, dtype=np.float64)
    if accel_full.shape != (n_dof,):
        raise ValueError(f"accel_full must have shape ({n_dof},); got {accel_full.shape}")
    e = next(
        el for el in body.elements if el.node_a == member.node_a and el.node_b == member.node_b
    )
    dofs = element_dofs(member.node_a, member.node_b)
    return np.asarray(element_global_mass(body.model, e) @ accel_full[dofs], dtype=np.float64)


def member_forces(
    body: BodyModel,
    member: Member,
    u_global: NDArray[np.float64],
    f_eq_global: NDArray[np.float64],
) -> MemberForces:
    """End forces for one member from a FULL-DOF global displacement vector.

    `f_eq_global` is the element's equivalent nodal load in the GLOBAL frame, 12
    components, from `element_equivalent_load`. **IT IS REQUIRED AND HAS NO DEFAULT
    (R677).** It defaulted to `None` once, meaning "no distributed load", and R663 is
    what that default cost: every caller that forgot it got a self-consistent wrong
    answer instead of an error. A member genuinely carrying nothing but its end actions
    passes an explicit zero vector, which is a statement rather than an omission.

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

    dofs = element_dofs(member.node_a, member.node_b)
    f_local = k_local @ (t @ u_global[dofs])
    f_eq = np.asarray(f_eq_global, dtype=np.float64)
    if f_eq.shape != (12,):
        raise ValueError(f"f_eq_global must have shape (12,); got {f_eq.shape}")
    f_local = f_local - t @ f_eq
    return MemberForces(
        label=member.label,
        body=body.name,
        end_a=np.array(f_local[0:6], dtype=np.float64),
        end_b=np.array(f_local[6:12], dtype=np.float64),
    )
