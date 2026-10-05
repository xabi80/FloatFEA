"""EK0(d): the static case -- self-weight from the FE mass, carried at the joints.

WHY THIS IS A SEPARATE CASE FROM THE DYNAMIC ONE. `docs/closure/F3.md` section 6a
measures that FloatSim's equilibrium reaction is identically zero: `xi = 0` solves a
model with no gravity term, so the exported multipliers are perturbations about an
equilibrium that carries no weight. The static part is FloatFEA's to build, from the FE
mass distribution, by a decision taken at Q1 and `PLAN.md:303`. DQ8 then forbids mixing
the two residuals, because their denominators are different quantities.

THE SUPPORT SCHEME IS EK0(d)'s AND IT IS NOT THE OBVIOUS ONE. A joint restrains the
VERTICAL only: the buoys float, so nothing at a joint resists horizontal motion. Three
vertical restraints at three non-collinear joints remove `uz`, `rx` and `ry`; the
remaining three rigid motions -- `ux`, `uy`, `rz` -- are removed by a minimal
statically determinate restraint whose reactions MUST COME OUT ZERO, because a
vertical load system can induce no horizontal reaction in a determinate restraint.
That zero is the check that the scheme is right, and it is the reason the restraint is
minimal rather than convenient.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from floatfea.io.frames import GRAVITY_VECTOR
from floatfea.model.nodes import node_dofs
from floatfea.model.platform import BodyModel, body_mass_matrix

__all__ = [
    "SupportScheme",
    "gravity_load",
    "horizontal_restraint",
    "vertical_supports",
]


@dataclass(frozen=True)
class SupportScheme:
    """The DOF a static case fixes, split by what each group is there for.

    `vertical` carries the load path and its reactions are the answer. `horizontal`
    removes rigid motion only, and its reactions are a CHECK: they are zero or the
    scheme is wrong.
    """

    vertical: NDArray[np.int64]
    horizontal: NDArray[np.int64]

    @property
    def fixed(self) -> NDArray[np.int64]:
        return np.unique(np.concatenate([self.vertical, self.horizontal]))


def gravity_load(body: BodyModel) -> NDArray[np.float64]:
    """Nodal self-weight, `M @ a_g`, consistent with the body's own mass matrix.

    `a_g` is the rigid-body acceleration field of gravity: `GRAVITY_VECTOR` on every
    translational triple and zero on every rotation. Going through `M` is correct HERE
    and is exactly what DQ5 forbids for ITS check -- DQ5 needs a route that does not
    share this one's mass matrix, or a mass matrix wrong in the same way on both sides
    would cancel. This function is the dependent route and says so.
    """
    mass = body_mass_matrix(body)
    n_dof = mass.shape[0]
    accel = np.zeros(n_dof, dtype=np.float64)
    for node in range(n_dof // 6):
        dofs = node_dofs(node)
        accel[dofs[0:3]] = GRAVITY_VECTOR
    return mass @ accel


def vertical_supports(nodes: tuple[int, ...]) -> NDArray[np.int64]:
    """The `uz` DOF of each joint node: the only direction a joint restrains."""
    if len(nodes) < 3:
        raise ValueError(
            f"a vertical support set needs at least three joints to remove uz, rx "
            f"and ry; got {len(nodes)}. Fewer leaves a rigid rotation free and the "
            "solve would be singular rather than wrong, which is the better failure "
            "but still a failure."
        )
    return np.array([node_dofs(n)[2] for n in nodes], dtype=np.int64)


def horizontal_restraint(body: BodyModel, nodes: tuple[int, ...]) -> NDArray[np.int64]:
    """`ux, uy` at one joint and `uy` at a second: three DOF, three rigid motions.

    The second node is chosen as the one FURTHEST from the first in `x`, because the
    pair's `x` separation is the lever that removes `rz`: two joints at the same `x`
    would leave yaw free and the stiffness matrix singular. Picking the furthest is
    not an optimisation, it is the only choice that cannot accidentally be degenerate
    on a frame whose joints are nearly aligned.
    """
    coords = body.model.nodes.coords()
    first = nodes[0]
    rest = nodes[1:]
    if not rest:
        raise ValueError("a horizontal restraint needs two distinct joints")
    separations = [abs(float(coords[n][0] - coords[first][0])) for n in rest]
    second = rest[int(np.argmax(separations))]
    if max(separations) == 0.0:
        raise ValueError(
            f"every joint of {body.name!r} shares the first joint's x coordinate, so "
            "no pair of them can remove yaw; the restraint would be degenerate and "
            "the solve singular."
        )
    a, b = node_dofs(first), node_dofs(second)
    return np.array([a[0], a[1], b[1]], dtype=np.int64)
