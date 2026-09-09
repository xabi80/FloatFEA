"""Two-node Timoshenko beam element, 12 DOF (D2 step 2).

Reference
---------
Przemieniecki, J.S., *Theory of Matrix Structural Analysis*, McGraw-Hill 1968
(Dover reprint 1985). Bending §5.6, axial and torsion §5.2-5.3, consistent mass
§11.4, geometric stiffness §12.3. Cross-checked against Cook, Malkus, Plesha &
Witt, *Concepts and Applications of Finite Element Analysis*, 4th ed., §2.

Local DOF ordering, A then B, matching `model/nodes.py`::

    0..5   u_x  u_y  u_z  r_x  r_y  r_z    at node A
    6..11  u_x  u_y  u_z  r_x  r_y  r_z    at node B

Nodal exactness
---------------
The shear-flexible stiffness below is the **exact** solution of the governing
Timoshenko ODEs for constant section and constant load, so it is **nodally
exact**: an end-loaded cantilever is reproduced by **one element** to round-off.

That is pre-registered deliberately, and as *nodally exact* rather than
*locking-free*, because it removes the mesh reflex categorically. **If a one-element
end-loaded case is wrong, the formulation is wrong and refinement cannot fix it** --
there is nothing for refinement to fix. "Locking-free" still leaves "try a finer
mesh" available as a response; this does not.

Distributed-load cases are a different matter: there the element is not nodally
exact, and the convergence *order* is the assertable quantity.

Geometric stiffness (step 12), and why the cubic form suffices
---------------------------------------------------------------
``k_g`` will be the cubic-interpolation form (Przemieniecki §12.3), **not** the
consistent geometric stiffness for a shear-flexible beam. That is a bounded
non-issue rather than a limitation, and the bound is an **inequality**::

    Phi * (P/P_E)  <=  12 sigma_allow / (kappa G pi^2)

The identity holds at ``sigma_actual``; the bound follows because any member
passing its strength check has ``sigma_actual <= sigma_allow``. Under-stressed
members sit below it with room to spare, so **the bound covers the whole model,
not just the strength-sized subset** -- which is what the argument needs.

``lambda`` cancels identically (``I = A r^2`` for any section), so the bound is
independent of slenderness, section and load. It scales with ``sigma_allow / G``:
0.400% for S235, 0.604% for S355, 0.783% for S460 at ``0.6 f_y``. The claim
survives any structural steel; if it ever breaks it will be the material or the
allowable basis, never the geometry.

**Compute it with `basis.shear_geometric_bound()`; do not quote the number.** A
bare constant in a comment stops being a bound the first time the basis moves.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from floatfea.model.material import Material, Section

DOF_PER_ELEMENT = 12


def shear_parameter(section: Section, material: Material, length: float, *, plane: str) -> float:
    """``Phi = 12 E I / (kappa G A L^2)`` for one bending plane.

    ``Phi`` is the ratio of bending to shear flexibility. ``Phi -> 0`` recovers
    Euler-Bernoulli exactly; large ``Phi`` is a stubby beam. `kappa` is computed
    from the section shape and the material's `nu`, never stored.
    """
    if length <= 0.0:
        raise ValueError(f"element length must be positive; got {length}")
    inertia = section.I_z if plane == "xy" else section.I_y
    kappa = section.kappa(material)
    return 12.0 * material.E * inertia / (kappa * material.G * section.A * length**2)


def bending_stiffness(ei: float, length: float, phi: float) -> NDArray[np.float64]:
    """4x4 shear-flexible bending stiffness in one plane.

    Przemieniecki eq. 5.36. DOF order ``(w_A, theta_A, w_B, theta_B)``::

                      EI          [  12      6L     -12      6L     ]
        k = ------------------    [  6L  (4+Phi)L^2  -6L  (2-Phi)L^2]
             L^3 (1 + Phi)        [ -12     -6L      12     -6L     ]
                                  [  6L  (2-Phi)L^2  -6L  (4+Phi)L^2]

    At ``Phi = 0`` this is the Euler-Bernoulli matrix **exactly**, entry for entry
    -- not approximately, and not in a limit. That exactness is what the step-2
    checkpoint asserts.
    """
    ll = length
    f = ei / (ll**3 * (1.0 + phi))
    return f * np.array(
        [
            [12.0, 6.0 * ll, -12.0, 6.0 * ll],
            [6.0 * ll, (4.0 + phi) * ll**2, -6.0 * ll, (2.0 - phi) * ll**2],
            [-12.0, -6.0 * ll, 12.0, -6.0 * ll],
            [6.0 * ll, (2.0 - phi) * ll**2, -6.0 * ll, (4.0 + phi) * ll**2],
        ],
        dtype=np.float64,
    )


def euler_bernoulli_bending_stiffness(ei: float, length: float) -> NDArray[np.float64]:
    """The classical Euler-Bernoulli 4x4, written INDEPENDENTLY.

    **Not** `bending_stiffness(ei, L, phi=0.0)`. Deriving the reference from the
    thing under test would make the step-2 checkpoint pass by construction and
    certify nothing -- the failure recorded as the fourteenth guard, where an
    assertion iterates a collection produced by the machinery it is testing.

    Przemieniecki eq. 5.20 / Cook eq. 2.3-8, transcribed from the source.
    """
    ll = length
    f = ei / ll**3
    return f * np.array(
        [
            [12.0, 6.0 * ll, -12.0, 6.0 * ll],
            [6.0 * ll, 4.0 * ll**2, -6.0 * ll, 2.0 * ll**2],
            [-12.0, -6.0 * ll, 12.0, -6.0 * ll],
            [6.0 * ll, 2.0 * ll**2, -6.0 * ll, 4.0 * ll**2],
        ],
        dtype=np.float64,
    )


def local_stiffness(section: Section, material: Material, length: float) -> NDArray[np.float64]:
    """12x12 local stiffness: axial, torsion, and bending in both planes."""
    k = np.zeros((DOF_PER_ELEMENT, DOF_PER_ELEMENT), dtype=np.float64)
    ll = length

    # Axial, Przemieniecki eq. 5.2.
    ea_l = material.E * section.A / ll
    k[np.ix_([0, 6], [0, 6])] = ea_l * np.array([[1.0, -1.0], [-1.0, 1.0]])

    # Torsion, Przemieniecki eq. 5.3.
    gj_l = material.G * section.J / ll
    k[np.ix_([3, 9], [3, 9])] = gj_l * np.array([[1.0, -1.0], [-1.0, 1.0]])

    # Bending in x-y (about local z): (v_A, rz_A, v_B, rz_B).
    phi_z = shear_parameter(section, material, ll, plane="xy")
    kz = bending_stiffness(material.E * section.I_z, ll, phi_z)
    k[np.ix_([1, 5, 7, 11], [1, 5, 7, 11])] = kz

    # Bending in x-z (about local y): (w_A, ry_A, w_B, ry_B). The sign pattern
    # differs because a positive rotation about +y produces NEGATIVE w-slope --
    # this is the sign that planar test cases cannot see (V2.4 exists for it).
    phi_y = shear_parameter(section, material, ll, plane="xz")
    ky = bending_stiffness(material.E * section.I_y, ll, phi_y)
    flip = np.diag([1.0, -1.0, 1.0, -1.0])
    k[np.ix_([2, 4, 8, 10], [2, 4, 8, 10])] = flip @ ky @ flip

    return k
