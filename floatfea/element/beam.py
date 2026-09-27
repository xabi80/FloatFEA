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


# --------------------------------------------------------------------------
# Consistent mass (D3, Przemieniecki §11.4) -- step 7, V2.5
# --------------------------------------------------------------------------
#
# WHAT IS IMPLEMENTED AND WHAT IS TRANSCRIBED, said plainly because they are not
# the same thing and `CLAUDE.md` § Style asks for a reference that can be
# checked rather than re-derived.
#
# The plan names Przemieniecki §11.4 for the shear-flexible consistent mass and
# does NOT print the matrix, as it prints eq. 5.36 for the stiffness. Rather
# than write Phi-dependent coefficients from memory -- which is the "plausible
# number to fill a gap" `CLAUDE.md` § When you are stuck forbids -- the
# interpolation is derived here from the governing equations and integrated
# exactly. The two routes give the same matrix, because Przemieniecki's closed
# form IS that integral, and the derivation is checkable line by line while a
# half-remembered table is not.
#
# THE DERIVATION, in one plane, with no distributed load:
#
#     V' = 0                 =>  V  constant
#     M' = V,  M = EI th'    =>  th  quadratic in x
#     w' = th + V/(kappa G A) =>  w   cubic in x
#
# so with xi = x/L and free coefficients (w_A, th_A, c2, c3):
#
#     th(xi) = th_A + c2 xi + c3 xi^2
#     w(xi)  = w_A + th_A L xi + L [ c2 xi^2/2 + c3 (xi^3/3 + Phi xi/6) ]
#
# The `Phi xi / 6` term is the shear part: V = 2 EI c3 / L^2 and
# V/(kappa G A) = c3 Phi / 6 by the definition of Phi, so the shear strain is
# CONSTANT over the element, which is what the exact Timoshenko solution says.
#
# WHY THIS PAIRING AND NOT A DIFFERENT ONE. The interpolation above spans
# exactly the space the exact stiffness eq. 5.36 is built from, so stiffness and
# mass are a conforming Rayleigh-Ritz pair. **That is what makes G2.4's band
# one-sided (AO4).** A Euler-Bernoulli consistent mass bolted to a Timoshenko
# stiffness is not such a pair, and the upper-bound theorem the band is
# pre-registered on would not apply to it.
#
# Phi -> 0 recovers the classical Euler-Bernoulli consistent mass, and that is
# asserted against an independently transcribed matrix rather than claimed here.


def euler_bernoulli_bending_mass(rho_a: float, length: float) -> NDArray[np.float64]:
    """The classical Euler-Bernoulli consistent mass 4x4, TRANSLATION ONLY.

    **Not** ``bending_mass(rho_a, 0.0, L, phi=0.0)``. Written independently for
    the same reason `euler_bernoulli_bending_stiffness` is: a reference derived
    from the thing under test certifies nothing.

    Przemieniecki eq. 11.31 / Cook eq. 11.3-8, transcribed from the source.
    DOF order ``(w_A, theta_A, w_B, theta_B)``.
    """
    ll = length
    f = rho_a * ll / 420.0
    return f * np.array(
        [
            [156.0, 22.0 * ll, 54.0, -13.0 * ll],
            [22.0 * ll, 4.0 * ll**2, 13.0 * ll, -3.0 * ll**2],
            [54.0, 13.0 * ll, 156.0, -22.0 * ll],
            [-13.0 * ll, -3.0 * ll**2, -22.0 * ll, 4.0 * ll**2],
        ],
        dtype=np.float64,
    )


_GAUSS_NODES, _GAUSS_WEIGHTS = np.polynomial.legendre.leggauss(4)
"""Four-point Gauss-Legendre on [-1, 1].

not-a-tolerance: a quadrature rule, not a threshold. Four points integrate a
degree-7 polynomial exactly and the integrand here is degree 6 -- ``N_w`` is
cubic -- so the integration is EXACT to round-off and there is no quadrature
error to bound. Raising the count would change nothing; lowering it would make
the mass matrix wrong rather than approximate."""


def bending_interpolation(
    length: float, phi: float, xi: float
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """``N_w`` and ``N_theta`` at ``xi = x/L``, for DOF ``(w_A, th_A, w_B, th_B)``.

    The derivation is in the module comment above. ``T`` maps the free
    coefficients ``(w_A, th_A, c2, c3)`` onto the four nodal DOF; inverting it
    gives the shape functions. ``T`` carries only ``L`` and ``Phi``, so it is
    well conditioned for any section and any unit.
    """
    ll = length
    t = np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [1.0, ll, ll / 2.0, ll * (1.0 / 3.0 + phi / 6.0)],
            [0.0, 1.0, 1.0, 1.0],
        ],
        dtype=np.float64,
    )
    p_w = np.array(
        [1.0, ll * xi, ll * xi**2 / 2.0, ll * (xi**3 / 3.0 + phi * xi / 6.0)],
        dtype=np.float64,
    )
    p_t = np.array([0.0, 1.0, xi, xi**2], dtype=np.float64)
    t_inv = np.linalg.inv(t)
    return p_w @ t_inv, p_t @ t_inv


def bending_mass(rho_a: float, rho_i: float, length: float, phi: float) -> NDArray[np.float64]:
    """4x4 consistent mass in one bending plane, translation plus rotary.

    ``rho_a = rho * A`` is mass per length; ``rho_i = rho * I`` is rotary
    inertia per length about the bending axis of THIS plane. Passing
    ``rho_i = 0`` gives the translational part alone, which is what the
    Euler-Bernoulli checkpoint compares against.

        m = integral_0^L rho ( A N_w^T N_w + I N_theta^T N_theta ) dx
    """
    if length <= 0.0:
        raise ValueError(f"element length must be positive; got {length}")
    m = np.zeros((4, 4), dtype=np.float64)
    for node, weight in zip(_GAUSS_NODES, _GAUSS_WEIGHTS, strict=True):
        xi = 0.5 * (node + 1.0)
        n_w, n_t = bending_interpolation(length, phi, xi)
        m += 0.5 * weight * length * (rho_a * np.outer(n_w, n_w) + rho_i * np.outer(n_t, n_t))
    return m


def local_mass(section: Section, material: Material, length: float) -> NDArray[np.float64]:
    """12x12 local consistent mass: axial, torsional, and bending in both planes.

    THE TORSIONAL INERTIA IS ``rho (I_y + I_z)`` AND NOT ``rho J``. ``J`` is the
    St-Venant torsion CONSTANT, which is a stiffness property; the rotary
    inertia of the cross-section about the member axis is its polar second
    moment of area. The two coincide for a circular tube and do not in general,
    and using ``J`` would put the error only on the sections F3 introduces --
    where it would look like a modelling difference rather than a bug. This is
    physics, not a convention, so it is not in `docs/conventions.md`.
    """
    m = np.zeros((DOF_PER_ELEMENT, DOF_PER_ELEMENT), dtype=np.float64)
    ll = length
    rho = material.rho

    # Axial, linear interpolation: rho A L / 6 * [[2, 1], [1, 2]].
    # Przemieniecki eq. 11.30.
    rho_a_l = rho * section.A * ll
    m[np.ix_([0, 6], [0, 6])] = (rho_a_l / 6.0) * np.array([[2.0, 1.0], [1.0, 2.0]])

    # Torsion, linear interpolation in the twist angle, with the POLAR second
    # moment as the rotary inertia per length. Przemieniecki eq. 11.30.
    rho_ip_l = rho * (section.I_y + section.I_z) * ll
    m[np.ix_([3, 9], [3, 9])] = (rho_ip_l / 6.0) * np.array([[2.0, 1.0], [1.0, 2.0]])

    # Bending in x-y (about local z): (v_A, rz_A, v_B, rz_B).
    phi_z = shear_parameter(section, material, ll, plane="xy")
    mz = bending_mass(rho * section.A, rho * section.I_z, ll, phi_z)
    m[np.ix_([1, 5, 7, 11], [1, 5, 7, 11])] = mz

    # Bending in x-z (about local y): the same sign flip the stiffness uses, and
    # for the same reason. A mass matrix is a quadratic form, so the flip is
    # applied on both sides; `flip` is its own inverse.
    phi_y = shear_parameter(section, material, ll, plane="xz")
    my = bending_mass(rho * section.A, rho * section.I_y, ll, phi_y)
    flip = np.diag([1.0, -1.0, 1.0, -1.0])
    m[np.ix_([2, 4, 8, 10], [2, 4, 8, 10])] = flip @ my @ flip

    return m
