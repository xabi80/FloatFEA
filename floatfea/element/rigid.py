"""The element-local rigid-mode diagnostic, as a shipped function (F3 § 5, G2.1).

Two quantities about one 12x12 local stiffness matrix:

  * `element_rigid_residual` -- how far the element is from annihilating the six
    rigid motions about its OWN midpoint, homogenised on the matrix, so
    orientation, span and reference point leave the quantity by construction;
  * `seventh_over_epsilon` -- where the first FLEXIBLE mode sits above the
    arithmetic floor of the homogenised matrix, as a plain ratio.

WHY THESE LIVE IN `floatfea/` AND NOT ONLY IN `tests/`. F3 § 5 requires that the
builder REFUSE a platform whose members fail the ceiling, and a refusal in
`floatfea/model/platform.py` cannot import from `tests/`. Until F3 the
element-local form existed only as rung-1 apparatus, which is why it could be a
diagnostic there and an assertion here without either moving.

`tests/verification/rung1/test_rigid_body_modes.py` keeps its own copy. It is F2
apparatus and is frozen under DR1, so it is not re-pointed at this module; what
ties the two is `test_G2_1_the_SHIPPED_residual_agrees_with_RUNG_ONEs`, which
runs both over the real platform's members and requires equality. Two
implementations of one formula that nothing compares is the drift this repository
keeps rediscovering.

Reference: the rigid-motion construction is Cook, Malkus, Plesha & Witt,
*Concepts and Applications of Finite Element Analysis*, 4th ed., § 3.7 -- a
correct element stiffness annihilates every rigid-body motion of its own
geometry, and the six here are three translations plus three rotations about the
element midpoint.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

RIGID = 6
"""Rigid-body modes of a free three-dimensional element: three translations and
three rotations."""


def element_rigid_vectors(length: float) -> NDArray[np.float64]:
    """`(12, 6)` -- the six rigid motions about the ELEMENT'S OWN midpoint.

    Local frame: node A at `-L/2`, node B at `+L/2` along local x. A rotation
    about the midpoint gives each end `cross(axis, r)` of translation and the
    axis itself of rotation. PHYSICALLY RIGID, with no homogenisation applied
    here -- dividing the translation by `L/2` while leaving the rotation at 1 is
    a rigid motion only when `L/2 == 1`, and that error reads `4.3e-02` instead
    of round-off.
    """
    half = length / 2.0
    out = np.zeros((12, RIGID), dtype=np.float64)
    for node, x in ((0, -half), (1, +half)):
        base = 6 * node
        for axis in range(3):
            out[base + axis, axis] = 1.0
        r = np.array([x, 0.0, 0.0], dtype=np.float64)
        for axis in range(3):
            e = np.zeros(3, dtype=np.float64)
            e[axis] = 1.0
            out[base : base + 3, 3 + axis] = np.cross(e, r)
            out[base + 3 : base + 6, 3 + axis] = e
    return out


def element_homogeniser(length: float) -> NDArray[np.float64]:
    """`S` as a vector: rotational DOFs scaled by the element length.

    `k_hat = S^-1 k S^-1` and the rigid vector becomes `S r`, so
    `k_hat (S r) = S^-1 (k r)`: a vector annihilated by `k` is annihilated by
    `k_hat`. The transform cannot create or destroy the property under test,
    which is what makes it a homogenisation rather than a second normalisation
    -- and `S r`, not `r / S`.
    """
    s = np.ones(12, dtype=np.float64)
    for node in range(2):
        s[6 * node + 3 : 6 * node + 6] = length
    return s


def element_rigid_residual(k_local: NDArray[np.float64], length: float) -> float:
    """`max_j ||k_hat r_hat|| / (||k_hat|| ||r_hat||)` over the six.

    Dimensionless and relative to the quantity compared, so the ceiling it is
    measured against is a pure number.
    """
    s = element_homogeniser(length)
    khat = k_local / np.outer(s, s)
    norm = float(np.linalg.norm(khat))
    modes = element_rigid_vectors(length)
    worst = 0.0
    for j in range(RIGID):
        r = modes[:, j] * s
        worst = max(worst, float(np.linalg.norm(khat @ r) / (norm * np.linalg.norm(r))))
    return worst


def seventh_over_epsilon(k_local: NDArray[np.float64], length: float) -> float:
    """`|lambda_7(k_hat)| / (||k_hat|| * eps)` -- the first FLEXIBLE mode's margin.

    THE ABSOLUTE VALUE IS IN THE NAME BECAUSE IT IS IN THE BODY. The spectrum is
    sorted by magnitude, so a negative seventh is reported by its size and its
    sign is lost here.

    **AND NOTHING ELSE CAUGHT THAT, WHICH IS R625.** A sentence here used to say
    the residual half catches a structural sign flip. It does not: negating a
    symmetric sub-block leaves every rigid motion annihilated, so on
    `platform:hub1_arm` the residual stays `8.7211e-20` and this ratio stays
    `9.3791e+11` with the torsion block negated, with the axial block negated,
    and with THE WHOLE MATRIX negated -- seven negative eigenvalues, accepted by
    both halves. `element_lambda_min_over_epsilon` below is the half that reads
    the sign.

    Homogenised with `S` rather than by `max|k|`, which is the whole difference
    between the element-local form and the assembled one: with the rotational
    DOFs unscaled the six vectors are not rigid motions of `k_hat` at all.
    """
    s = element_homogeniser(length)
    khat = k_local / np.outer(s, s)
    khat = (khat + khat.T) / 2.0
    w = np.sort(np.abs(np.linalg.eigvalsh(khat)))
    unit = float(np.linalg.norm(khat)) * float(np.finfo(np.float64).eps)
    return float(w[RIGID] / unit)


def element_lambda_min_over_epsilon(k_local: NDArray[np.float64], length: float) -> float:
    """`lambda_min(k_hat) / (||k_hat|| * eps)` -- SIGNED, which is the whole point.

    A correct element stiffness is positive semi-definite: it stores energy, it
    does not release it. Neither `element_rigid_residual` nor
    `seventh_over_epsilon` can see a violation, because both are blind to sign --
    the first by construction, since a negated symmetric sub-block still
    annihilates every rigid motion, and the second because it sorts `|lambda|`.

    So this is reported signed and compared against `-RIGID_MODE_BOUND`: at
    round-off a defect-free element reads a small negative number, and anything
    structural is decades below it. Measured over the real platform's members the
    clean reading is `-2.1425e-03` to `-7.1e-02` units, and the three negation
    shapes read `-9.3791e+11` and `-4.5035e+15`.

    NO NEW CONSTANT. `RIGID_MODE_BOUND` already says how far from the arithmetic
    floor a mode has to be before its position is a statement about the structure
    rather than about double precision, and that is exactly the question here with
    the sign kept.
    """
    s = element_homogeniser(length)
    khat = k_local / np.outer(s, s)
    khat = (khat + khat.T) / 2.0
    smallest = float(np.linalg.eigvalsh(khat).min())
    unit = float(np.linalg.norm(khat)) * float(np.finfo(np.float64).eps)
    return smallest / unit
