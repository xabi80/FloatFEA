"""Local-to-global transformation for the 12-DOF beam element (D2 step 3).

Every coupling entry the element has lives here. In local axes a straight
prismatic member is **block-diagonal** — axial, torsion, and the two bending
planes are independent, and `tests/unit/test_beam_element.py` asserts the
off-block entries are identically zero. `T^T K T` is what creates couplings, so
the transformation owns all of them.

The rotation matrix has the local axes as **rows**, so it maps global components
to local ones::

    u_local = R @ u_global          R = [x_hat; y_hat; z_hat]

and `T = blkdiag(R, R, R, R)` applies that to the four (translation, rotation)
triples of a two-node element.

`R` is **orthogonal by construction** because `member_local_axes` returns an
orthonormal right-handed triad. That is worth asserting rather than assuming: a
non-orthogonal `T` moves eigenvalues, and it is exactly the `I + [theta x]`
first-order trap `docs/conventions.md` warns about arriving through a different
door.
"""
from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from floatfea.model.local_axes import member_local_axes


def rotation_matrix(
    node_a: NDArray[np.floating],
    node_b: NDArray[np.floating],
    *,
    orientation_node: NDArray[np.floating] | None = None,
    roll_rad: float = 0.0,
) -> NDArray[np.float64]:
    """3x3 with the member's local axes as rows."""
    x, y, z = member_local_axes(
        node_a, node_b, orientation_node=orientation_node, roll_rad=roll_rad
    )
    return np.array([x, y, z], dtype=np.float64)


def transformation(r: NDArray[np.floating]) -> NDArray[np.float64]:
    """12x12 block-diagonal transformation from a 3x3 rotation."""
    r = np.asarray(r, dtype=np.float64)
    if r.shape != (3, 3):
        raise ValueError(f"rotation must be 3x3; got {r.shape}")
    t = np.zeros((12, 12), dtype=np.float64)
    for b in range(4):
        t[3 * b : 3 * b + 3, 3 * b : 3 * b + 3] = r
    return t


def to_global(
    k_local: NDArray[np.floating], r: NDArray[np.floating]
) -> NDArray[np.float64]:
    """``T^T K_local T``."""
    t = transformation(r)
    return t.T @ np.asarray(k_local, dtype=np.float64) @ t
