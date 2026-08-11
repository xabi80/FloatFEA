"""Member local-axis construction, and the degeneracy guard that protects it.

This enforces the convention decided at F0 and locked in `docs/conventions.md`
§ "Member local axes". It is convention enforcement, not element formulation —
the element library is F2 and depends on this, not the other way round.

    local x  =  unit(node_b - node_a)         member axis, A to B
    local z  =  unit(r - (r . x) x)           r = orientation reference
    local y  =  z  x  x                       right-handed

**There is no implicit default for a vertical member.** The reference defaults
to global Z, which is degenerate for exactly the members this platform is mostly
made of. Rather than silently switching to another global axis — which changes
the sign convention of every recovered moment on that member, untraceably — the
construction refuses and demands an explicit orientation node.

A roll angle does not rescue a vertical member: roll is measured *from* the
global-Z-derived reference, so if that reference is degenerate the datum the
roll is measured from does not exist either. Only an orientation node works
there, and that is the point — it forces the choice to be written down.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from floatfea.tolerances import MEMBER_ORIENTATION_DEGENERACY

_GLOBAL_Z: NDArray[np.float64] = np.array([0.0, 0.0, 1.0], dtype=np.float64)


class DegenerateMemberOrientation(ValueError):
    """The orientation reference is too near-parallel to the member axis.

    Raised rather than falling back to another reference axis. See
    `docs/conventions.md` § "Member local axes" for why the fallback is refused.
    """


def member_local_axes(
    node_a: NDArray[np.floating],
    node_b: NDArray[np.floating],
    *,
    orientation_node: NDArray[np.floating] | None = None,
    roll_rad: float = 0.0,
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """Return the right-handed local triad ``(x, y, z)`` for a member.

    Parameters
    ----------
    node_a, node_b
        Member end coordinates, global frame, metres. Must be distinct.
    orientation_node
        Optional third point. When given, local z lies in the plane of
        (A, B, orientation_node) on the side of that point, and the global-Z
        default is not consulted. **Required for near-vertical members.**
    roll_rad
        Rotation of the triad about local x, measured from the reference
        derived above. Applies to either reference.

    Raises
    ------
    ValueError
        If the nodes coincide.
    DegenerateMemberOrientation
        If the orientation reference in use is within
        :data:`floatfea.tolerances.MEMBER_ORIENTATION_DEGENERACY` of parallel to
        the member axis.
    """
    a = np.asarray(node_a, dtype=np.float64)
    b = np.asarray(node_b, dtype=np.float64)
    for name, arr in (("node_a", a), ("node_b", b)):
        if arr.shape != (3,):
            raise ValueError(f"{name} must have shape (3,); got {arr.shape}")

    axis = b - a
    length = float(np.linalg.norm(axis))
    if length == 0.0:
        raise ValueError("node_a and node_b must be distinct; got zero-length member")
    x_hat = axis / length

    if orientation_node is None:
        reference = _GLOBAL_Z
        source = "the default global-Z reference"
        remedy = "supply an orientation_node for this member"
    else:
        ref_pt = np.asarray(orientation_node, dtype=np.float64)
        if ref_pt.shape != (3,):
            raise ValueError(f"orientation_node must have shape (3,); got {ref_pt.shape}")
        reference = ref_pt - a
        norm = float(np.linalg.norm(reference))
        if norm == 0.0:
            raise ValueError("orientation_node must not coincide with node_a")
        reference = reference / norm
        source = "the supplied orientation_node"
        remedy = "move the orientation_node off the member axis"

    # |r_hat x x_hat| is the sine of the angle between reference and member axis.
    # It is exactly the quantity whose reciprocal amplifies any perturbation in
    # the member axis into the local-y direction, which is why it is the guard.
    perpendicularity = float(np.linalg.norm(np.cross(reference, x_hat)))
    if perpendicularity < MEMBER_ORIENTATION_DEGENERACY:
        raise DegenerateMemberOrientation(
            f"member ({a} -> {b}) is {np.degrees(np.arcsin(min(perpendicularity, 1.0))):.3f} deg "
            f"from {source}, below the "
            f"MEMBER_ORIENTATION_DEGENERACY floor of {MEMBER_ORIENTATION_DEGENERACY} "
            f"({np.degrees(np.arcsin(MEMBER_ORIENTATION_DEGENERACY)):.3f} deg). "
            f"The local-axis construction is ill-conditioned here and there is no "
            f"silent fallback: {remedy}."
        )

    z_raw = reference - float(np.dot(reference, x_hat)) * x_hat
    z_hat = z_raw / float(np.linalg.norm(z_raw))
    y_hat: NDArray[np.float64] = np.cross(z_hat, x_hat)

    if roll_rad != 0.0:
        c, s = float(np.cos(roll_rad)), float(np.sin(roll_rad))
        y_rot = c * y_hat + s * z_hat
        z_rot = -s * y_hat + c * z_hat
        y_hat, z_hat = y_rot, z_rot

    return x_hat, y_hat, z_hat
