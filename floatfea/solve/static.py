"""EK0(d): the static load path, platform -> hubs, and the three checks it must pass.

THE ORDER IS THE LOAD PATH AND IT IS NOT A CHOICE. The platform's self-weight is carried
at its four hub joints; each hub then carries its own weight PLUS what the platform hands
it, supported at its three buoy joints. Solving a hub first would need a reaction that
does not exist yet.

THE REMAINDER IS A SLAVE, NOT A FREE NODE, AND THE FIRST VERSION OF THIS MODULE WAS
SINGULAR BECAUSE OF IT. DY0 puts half of each body's mass at a `remainder_node` joined to
the centre by a RIGID LINK, which is a kinematic constraint and not an element -- so
`assemble()` leaves that node's six DOF unconnected and the factorisation is exactly
singular. On the platform the link is `20.66 m` long, so the remainder's moment arm is
load-bearing rather than incidental. The system is reduced through
`constraint_transform` before it is solved, and expanded back afterwards. Every hub has a
ZERO-length link (DW1: a hub's mass reference already sits on the joint plane), so for a
hub the reduction is the identity and the code path is the same.

WHAT EK0(d) ASSERTS, and each is a different kind of statement:
  * `Sum of reactions = applied` per body -- conservation, and the one a wrong mass
    distribution breaks.
  * the horizontal restraint's reactions are ZERO -- that the support scheme is right. A
    vertical load system can induce no horizontal reaction in a determinate restraint, so
    a nonzero value means the restraint is carrying load it should not.
  * the platform's four hub reactions are EQUAL -- by the frame's four-fold symmetry.
    This is the only one of the three the FE stiffness participates in, because the fourth
    vertical support is redundant and the split between the four is a stiffness answer
    rather than a statics one.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp
from numpy.typing import NDArray

from floatfea.assemble.system import assemble_dense, solve
from floatfea.element.constraints import constraint_transform, reduce_matrix
from floatfea.io.frames import GRAVITY_MAGNITUDE
from floatfea.loads.selfweight import (
    SupportScheme,
    gravity_load,
    horizontal_restraint,
    vertical_supports,
)
from floatfea.model.nodes import DOF_PER_NODE, node_dofs
from floatfea.model.platform import BodyModel, Superstructure

__all__ = ["StaticCase", "joint_nodes_of", "solve_body_static", "solve_superstructure_static"]


@dataclass(frozen=True)
class StaticCase:
    """One body's static solve, with the quantities EK0(d) asks to be reported."""

    body: str
    weight_N: float
    """`mass * g` from the body's own deck mass -- the independent side of the sum."""

    vertical_reactions_N: dict[int, float]
    """Node index -> reaction. The answer, and what the next body down is loaded by."""

    sum_vertical_N: float
    horizontal_reactions_N: dict[int, float]
    """Global DOF -> reaction. Zero, or the support scheme is wrong."""

    worst_horizontal_N: float
    applied_N: float
    """Sum of applied vertical, including what an upstream body handed down."""

    residual: float
    backward_error: float
    scheme: SupportScheme
    u_full: NDArray[np.float64]
    """Displacement in the body's FULL DOF numbering, slave node included.

    Expanded back through the constraint transform here rather than at the call site:
    `member_forces` needs full DOF and a reduced vector passed to it would read the
    wrong ones silently.
    """

    @property
    def sum_error(self) -> float:
        """`|sum(reactions) + applied| / |applied|` -- DQ8's static normalisation.

        A reaction opposes its load, so conservation is a SUM to zero and not a
        difference: writing it as `sum - applied` would read as satisfied when the
        reactions had the wrong sign, which is the one error this check exists for.
        """
        return abs(self.sum_vertical_N + self.applied_N) / abs(self.applied_N)


def _links(body: BodyModel) -> dict[int, tuple[int, NDArray[np.floating]]]:
    """The body's rigid links, slave -> (master, offset). Empty when none.

    A hub's remainder sits ON its centre node, so there is no link and no reduction.
    The platform's does not, and the offset is the vector master -> slave.
    """
    if body.remainder_node == body.centre_node:
        return {}
    coords = body.model.nodes.coords()
    offset: NDArray[np.floating] = coords[body.remainder_node] - coords[body.centre_node]
    return {body.remainder_node: (body.centre_node, offset)}


def _retained(n_dof: int, links: Mapping[int, object]) -> list[int]:
    """The DOF `constraint_transform` keeps, in its own column order.

    THE RULE IS RESTATED HERE AND CHECKED AGAINST THE TRANSFORM'S WIDTH, rather than
    trusted. Two copies of an ordering rule that drift are C131's defect; an assert on
    the width is what makes a drift loud instead of a silently permuted reaction vector.
    """
    slave_dofs = {d for s in links for d in range(DOF_PER_NODE * s, DOF_PER_NODE * (s + 1))}
    return [i for i in range(n_dof) if i not in slave_dofs]


def joint_nodes_of(s: Superstructure, body: BodyModel) -> tuple[int, ...]:
    """The nodes a body is supported AT, read from the deck's joint table.

    For a hub those are its three buoy joints; `buoy_joint_nodes` maps each buoy label to
    `(body, node)` and the selection is by BODY NAME, not by member label -- a permutation
    corrupts the labels, so selecting with them would put the label on both sides of the
    comparison, which is R600's defect.
    """
    if body.name == "platform":
        tips = tuple(
            body.model.nodes.index(f"platform:{hub}_arm_tip")
            for hub in sorted(k for k, v in s.deck_joint_owner.items() if v == "platform")
        )
        if len(tips) != 4:
            raise ValueError(f"expected 4 hub joints on the platform, found {len(tips)}")
        return tips
    nodes = tuple(
        sorted(node for _buoy, (owner, node) in s.buoy_joint_nodes.items() if owner == body.name)
    )
    if len(nodes) != 3:
        raise ValueError(f"expected 3 buoy joints on {body.name!r}, found {len(nodes)}")
    return nodes


def solve_body_static(
    s: Superstructure,
    body: BodyModel,
    handed_down: Mapping[int, float] | None = None,
) -> StaticCase:
    """One body under self-weight plus whatever an upstream body hands it.

    `handed_down` is node index -> vertical force applied TO this body, signed in the
    global frame. For a hub that is the platform's reaction acting downward on the hub
    centre; the platform itself gets nothing.
    """
    joints = joint_nodes_of(s, body)
    scheme = SupportScheme(
        vertical=vertical_supports(joints),
        horizontal=horizontal_restraint(body, joints),
    )

    n_dof = body.model.n_dof
    f = gravity_load(body)
    for node, fz in (handed_down or {}).items():
        f[node_dofs(node)[2]] += fz
    applied = float(sum(f[node_dofs(n)[2]] for n in range(n_dof // DOF_PER_NODE)))

    k_full = assemble_dense(body.model, body.elements)
    links = _links(body)
    if links:
        t = constraint_transform(n_dof, links)
        retained = _retained(n_dof, links)
        if t.shape[1] != len(retained):
            raise AssertionError(
                f"the retained rule here keeps {len(retained)} DOF and "
                f"constraint_transform keeps {t.shape[1]}; the two orderings have "
                "drifted and every reaction below would be silently permuted."
            )
        k_red = reduce_matrix(k_full, t)
        f_red = t.T @ f
    else:
        retained = list(range(n_dof))
        k_red, f_red = k_full, f

    column_of = {dof: j for j, dof in enumerate(retained)}
    fixed_red = np.array(sorted(column_of[int(d)] for d in scheme.fixed), dtype=np.int64)
    res = solve(sp.csr_matrix(k_red), f_red, fixed_red)
    u_full = t @ res.u if links else res.u

    vertical = {
        int(d // DOF_PER_NODE): float(res.reactions[column_of[int(d)]]) for d in scheme.vertical
    }
    horizontal = {int(d): float(res.reactions[column_of[int(d)]]) for d in scheme.horizontal}

    return StaticCase(
        body=body.name,
        weight_N=float(body.deck_mass * GRAVITY_MAGNITUDE),
        vertical_reactions_N=vertical,
        sum_vertical_N=float(sum(vertical.values())),
        horizontal_reactions_N=horizontal,
        worst_horizontal_N=max((abs(v) for v in horizontal.values()), default=0.0),
        applied_N=applied,
        residual=res.residual,
        backward_error=res.backward_error,
        scheme=scheme,
        u_full=np.asarray(u_full, dtype=np.float64),
    )


def solve_superstructure_static(s: Superstructure) -> dict[str, StaticCase]:
    """The whole static path in load order: platform first, then each hub it feeds.

    The platform's reaction at `platform:<hub>_arm_tip` is what that joint pushes up on
    the platform with, so the force the platform exerts on the hub is its NEGATIVE,
    applied at the hub's own centre node -- which is where the deck puts the
    hub-platform joint (`attach_a_body = [0, 0, 0]`).
    """
    bodies = {b.name: b for b in s.bodies}
    platform = bodies["platform"]
    out: dict[str, StaticCase] = {"platform": solve_body_static(s, platform)}

    for hub in sorted(k for k, v in s.deck_joint_owner.items() if v == "platform"):
        tip = platform.model.nodes.index(f"platform:{hub}_arm_tip")
        reaction = out["platform"].vertical_reactions_N[tip]
        body = bodies[hub]
        out[hub] = solve_body_static(s, body, handed_down={body.centre_node: -reaction})
    return out
