"""EK0(e): FloatSim's joint multipliers mapped onto the FE joint nodes.

WHAT `res.lam` IS. DX1 measured it: 16 joints x 4 rows -- `Fx`, `Fy`, `Fz` and the
locked-axis moment -- in N and N*m, dt-free, the PHYSICAL constraint force. The study
discards it; `scripts/report_joint_reactions.py` reads it from the solve.

THE SIGN IS THE WHOLE DIFFICULTY AND IT IS NOT A CONVENTION TO PICK. FloatSim's
constraint Jacobian `G` enters the equations as `-G^T lam`, so `G^T lam` is the force the
constraint applies to the bodies, and the two bodies of one joint receive equal and
opposite shares BY CONSTRUCTION. EK0(e) asks that to be asserted rather than assumed,
because the thing it would catch -- a Jacobian whose two blocks are not negatives -- would
put the same force into both bodies and leave every member force wrong in the same
direction on both sides of a joint, which no per-body equilibrium check would see.

`docs/conventions.md` is authoritative for frames and signs and this module assumes
nothing beyond what it declares: FloatSim's global frame and FloatFEA's are the same,
and the only conversion anywhere is at the I/O boundary.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from floatfea.model.nodes import node_dofs

__all__ = ["JointShare", "duality_residual", "map_joint_reactions"]

ROWS_PER_JOINT = 4
"""`Fx`, `Fy`, `Fz`, locked-axis moment -- DX1's measured layout, not an assumption."""


@dataclass(frozen=True)
class JointShare:
    """What one joint applies to one body at one timestep, in the global frame."""

    joint: str
    body: str
    node: int
    force: NDArray[np.float64]
    """`(3,)` N."""

    moment: NDArray[np.float64]
    """`(3,)` N*m -- only the locked axis is nonzero for a `yaw_locked` joint."""


def duality_residual(share_a: NDArray[np.float64], share_b: NDArray[np.float64]) -> float:
    """`max|f_a + f_b| / max(|f_a|, |f_b|)` -- EK0(e)'s equal-and-opposite check.

    Relative, because the absolute size spans the whole run; and a SUM rather than a
    difference, because equal and opposite means they cancel.

    **RAISES when both shares are zero (R678).** It returned `0.0` there, which reads as
    perfect agreement and cannot be told from a correct Jacobian -- so a run whose
    multipliers had collapsed to zero would report the strongest possible result. A
    caller with legitimately zero shares excludes those steps itself.
    """
    scale = max(float(np.max(np.abs(share_a))), float(np.max(np.abs(share_b))))
    if scale == 0.0:
        raise ValueError(
            "both shares are identically zero, so there is no duality to measure and "
            "no scale to measure it against. R678: this returned 0.0, which reads as "
            "PERFECT AGREEMENT and is indistinguishable from a correct Jacobian -- so "
            "a run whose multipliers had collapsed to zero reported the strongest "
            "possible result. A caller that expects zero shares (before the ramp, say) "
            "excludes those steps itself, which is a statement rather than a silence."
        )
    return float(np.max(np.abs(share_a + share_b)) / scale)


def map_joint_reactions(
    lam_row: NDArray[np.float64],
    joint_order: list[tuple[str, str, str]],
    nodes: dict[tuple[str, str], int],
    n_dof_of: dict[str, int],
) -> dict[str, NDArray[np.float64]]:
    """One timestep's multipliers as a nodal load vector per body.

    `joint_order` is `(joint name, body_a, body_b)` in the SAME order as the blocks of
    `lam_row`; `nodes` maps `(joint, body)` to that body's node for the joint. Both are
    passed in rather than derived here: the deck is the authority for the order and the
    builder for the nodes, and a module that guessed either would be asserting its guess.

    Body A receives `+(F, M)` and body B receives `-(F, M)`. Which of the two is "A" is
    the deck's `body_a`, so a reader checking a sign has one place to look.
    """
    if lam_row.shape != (ROWS_PER_JOINT * len(joint_order),):
        raise ValueError(
            f"lam row has shape {lam_row.shape}; expected "
            f"({ROWS_PER_JOINT * len(joint_order)},) for {len(joint_order)} joints"
        )
    out = {body: np.zeros(n, dtype=np.float64) for body, n in n_dof_of.items()}
    for i, (joint, body_a, body_b) in enumerate(joint_order):
        block = lam_row[ROWS_PER_JOINT * i : ROWS_PER_JOINT * (i + 1)]
        force = np.array(block[0:3], dtype=np.float64)
        moment = np.array([0.0, 0.0, float(block[3])], dtype=np.float64)
        for body, sign in ((body_a, 1.0), (body_b, -1.0)):
            if body not in out:
                continue  # a buoy: a load on the superstructure, not a modelled body
            dofs = node_dofs(nodes[(joint, body)])
            out[body][dofs[0:3]] += sign * force
            out[body][dofs[3:6]] += sign * moment
    return out
