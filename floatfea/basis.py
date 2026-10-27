"""The project basis: material constants, allowables, and section formulae.

**Named `basis.py`, not `sections.py` (AS2).** The earlier name described half the
contents, and *a file called `sections.py` holding material constants will
eventually attract a `materials.py` with its own `E`*. That is the duplication
this module exists to prevent, arriving through **naming** rather than
carelessness. `docs/milestones/F1.md` §8 already calls `0.6 f_y` "the project
basis"; the module takes the phrase.

**Not tolerances.** These are physical and code-derived constants, so they do not
belong in `tolerances.py`. What they share with it is the single-source rule, and
for the same reason: a constant that exists in two places will eventually differ
in two places.

Why this module exists
----------------------
Two constants have already appeared with two values in two documents:

* **`kappa`**, the shear correction factor, is genuinely source-dependent —
  ~0.5 for a thin-walled tube by the simple argument, ~0.53 by Cowper at
  `nu = 0.3`, 0.886 for solid circular. If the ELEMENT uses one value and a
  REFERENCE FORMULA uses another, a verification test compares two different
  beams and passes or fails for the wrong reason, while looking like a clean
  closed-form check. Pinned at F2's lock before it could bite.

* **`sigma_allow`** bit immediately afterwards, one constant over. F1.md §8 states
  the basis as `0.6 f_y = 213.0 MPa`; F2's brace sweep used `f_y / 1.5 =
  236.7 MPa`. Consistently **11.11% high** — exactly `(1/1.5) / 0.6` — across every
  row. The conclusion survived, but an 11% difference between a lock document and
  the project's stated basis will eventually be a member passing instead of
  failing.

The rule, therefore: **anything that could reasonably be written down twice is
written down here once**, and both the code and the verification reference consume
it from here.
"""

from __future__ import annotations

import math
from typing import Final

# ---------------------------------------------------------------------------
# Material -- S355, the project standard (docs/milestones/F1.md sec. 8).
# ---------------------------------------------------------------------------
E_STEEL: Final[float] = 210e9  # Pa
NU_STEEL: Final[float] = 0.3
RHO_STEEL: Final[float] = 7850.0  # kg/m^3
FY_S355: Final[float] = 355e6  # Pa

G_STEEL: Final[float] = E_STEEL / (2.0 * (1.0 + NU_STEEL))

# ---------------------------------------------------------------------------
# Allowable stress basis.
#
# THE PROJECT BASIS IS 0.6 f_y, stated in docs/milestones/F1.md sec. 8. It is the
# working-stress allowable for members in tension/compression and is what every
# sizing figure in that section was computed against.
#
# `f_y / 1.5` is NOT the same number (it is 0.667 f_y, 11.11% higher) and must not
# be substituted for it. F2's first brace sweep did exactly that.
# ---------------------------------------------------------------------------
ALLOWABLE_FACTOR: Final[float] = 0.6
SIGMA_ALLOW_S355: Final[float] = ALLOWABLE_FACTOR * FY_S355  # 213.0 MPa


# ---------------------------------------------------------------------------
# Sea-state admissibility -- the associated-period band and the breaking limit.
#
# THE ASSOCIATED-PERIOD BAND, as DNV practice and as this project has used it
# since F4:
#
#     sqrt(ASSOCIATED_PERIOD_LOW_COEFF * H)  <=  T  <=  sqrt(ASSOCIATED_PERIOD_HIGH_COEFF * H)
#
# with H the full-scale wave height in metres and T the full-scale period in
# seconds. For H = 24.2 m that is 12.542 .. 16.316 s.
#
# THE BREAKING LIMIT is the classical deep-water limiting steepness of a
# progressive wave, H / lambda = 1/7, with the deep-water dispersion relation
# lambda = g T^2 / (2 pi). A sea state above it cannot exist at that height and
# period, so it cannot set a design envelope.
#
# Both are PHYSICAL / CODE-DERIVED CONSTANTS and not tolerances: nothing here is
# an error ceiling, a convergence threshold or a factor introduced to make two
# numbers agree. Their placement in this module rather than in `tolerances.py`
# is directive FU1 (`docs/directives/FU.md`).
#
# `g` IS NOT DECLARED HERE. It is `floatfea.io.frames.GRAVITY_MAGNITUDE`, the one
# source. Directive FU0 is why: two measure scripts had declared their own
# `GRAVITY = 9.80665` against the library's 9.81, and two more carried 9.81 as a
# bare literal.
#
# A sentence naming this module's consumers stood here and was wrong by one (R1027). It
# is deleted rather than corrected: a list of callers in a comment goes stale on the next
# import and nothing in this repository re-reads it. The replacement is not a corrected
# list and not a claim about how many declarations of these constants exist -- that would
# be the same shape again.
# ---------------------------------------------------------------------------
ASSOCIATED_PERIOD_LOW_COEFF: Final[float] = 6.5  # s^2/m
ASSOCIATED_PERIOD_HIGH_COEFF: Final[float] = 11.0  # s^2/m
BREAKING_STEEPNESS_LIMIT: Final[float] = 1.0 / 7.0  # -   H / lambda, deep water


# ---------------------------------------------------------------------------
# EN 1993-1-1 Table 5.2 -- circular hollow section class limits in compression,
# as D/t, with eps^2 = 235/f_y. Beyond class 3 the section is slender: local
# buckling governs and a global (Euler) check is not the binding one.
# ---------------------------------------------------------------------------
def chs_class_limits(fy: float = FY_S355) -> tuple[float, float, float]:
    """(class 1, class 2, class 3) D/t limits for a CHS in compression."""
    eps2 = 235e6 / fy
    return 50.0 * eps2, 70.0 * eps2, 90.0 * eps2


# ---------------------------------------------------------------------------
# Shear correction factor -- COMPUTED, NEVER STORED (AS1).
#
# kappa depends on BOTH the section geometry AND Poisson's ratio: 0.5306 for a
# thin-walled tube at nu = 0.3, 0.8864 for solid circular, and both vary with nu.
# It therefore belongs to NEITHER a Material nor a Section alone -- it is a
# property of the pair.
#
# THE RULE: kappa is obtained by calling `kappa(section, material)`. It is never a
# field on Material, never a field on Section, and never a default argument.
#
# This is a stronger rule than "single source", and it outlives the reason for it:
# a stored kappa is wrong as soon as the section or nu changes, so the physics
# forbids the field even for someone who has forgotten why duplication is banned.
#
# Values, all Cowper (1966) J. Appl. Mech. 33(2) 335-340 Table 1, at nu = 0.3:
#   thin-walled circular tube    0.5306   (simple shear-flow argument gives 0.5)
#   solid circular               0.8864
#   rectangular                  0.8497
#
# THE PROJECT USES COWPER THROUGHOUT -- one consistent source across section
# types rather than a mix of conventions.
# ---------------------------------------------------------------------------
KAPPA_SOURCE: Final[str] = "Cowper (1966), J. Appl. Mech. 33(2) 335-340, Table 1"


def kappa_thin_tube(nu: float = NU_STEEL) -> float:
    """Cowper's shear coefficient for a thin-walled circular tube.

    ``kappa = 2(1 + nu) / (4 + 3 nu)`` -- Cowper Table 1, hollow circular in the
    thin-wall limit. Gives 0.5305 at nu = 0.3, against 0.5 from the simple
    shear-flow argument; the 6% difference is exactly the kind that makes a
    closed-form check pass or fail for the wrong reason.
    """
    return 2.0 * (1.0 + nu) / (4.0 + 3.0 * nu)


def kappa_solid_circular(nu: float = NU_STEEL) -> float:
    """Cowper's shear coefficient for a solid circular section.

    ``kappa = 6(1 + nu) / (7 + 6 nu)`` -- 0.8864 at nu = 0.3.
    """
    return 6.0 * (1.0 + nu) / (7.0 + 6.0 * nu)


# ---------------------------------------------------------------------------
# Thin-walled circular tube properties. Exact forms, not thin-wall
# approximations, so G3.3 (exact section properties) has something to check.
# ---------------------------------------------------------------------------
def tube_area(d_outer: float, t: float) -> float:
    d_i = d_outer - 2.0 * t
    return math.pi * (d_outer**2 - d_i**2) / 4.0


def tube_second_moment(d_outer: float, t: float) -> float:
    d_i = d_outer - 2.0 * t
    return math.pi * (d_outer**4 - d_i**4) / 64.0


def tube_radius_of_gyration(d_outer: float, t: float) -> float:
    return math.sqrt(tube_second_moment(d_outer, t) / tube_area(d_outer, t))


# ---------------------------------------------------------------------------
# The dispatcher. `Section` carries a SHAPE, not a kappa.
# ---------------------------------------------------------------------------
_KAPPA_BY_SHAPE = {
    "thin_tube": kappa_thin_tube,
    "solid_circular": kappa_solid_circular,
}


def kappa(shape: str, nu: float = NU_STEEL) -> float:
    """Shear correction factor for ``shape`` at Poisson's ratio ``nu``.

    The only sanctioned way to obtain kappa. Raises on an unknown shape rather
    than defaulting: a silent fallback to a tube value on a section that is not a
    tube is precisely the two-different-beams failure this module prevents.
    """
    try:
        return _KAPPA_BY_SHAPE[shape](nu)
    except KeyError:
        raise ValueError(
            f"no shear coefficient for shape {shape!r}; known: "
            f"{sorted(_KAPPA_BY_SHAPE)}. Add it from {KAPPA_SOURCE} rather than "
            "defaulting -- a wrong kappa makes an element and its verification "
            "reference two different beams."
        ) from None


# ---------------------------------------------------------------------------
# Why the cubic geometric stiffness needs no shear-flexible refinement.
#
# STATED AS A BOUND, NOT AN IDENTITY (AT1). The identity
#
#     Phi * (P/P_E) = 12 sigma_actual / (kappa G pi^2)
#
# holds at whatever stress a member happens to carry, so on its own it is a
# statement about strength-sized members and nothing else. The useful form is the
# INEQUALITY: any member passing its strength check has sigma_actual <= sigma_allow,
# therefore
#
#     Phi * (P/P_E)  <=  12 sigma_allow / (kappa G pi^2)
#
# Under-stressed members satisfy it with room to spare, so the bound covers the
# WHOLE MODEL rather than the sized subset -- which is what the self-limiting
# argument for the cubic k_g actually needs.
#
# lambda cancels identically (I = A r^2 for any section), so the bound is
# independent of slenderness, section and load. It scales with sigma_allow / G:
#
#     S235 at 0.6 f_y   0.400%
#     S355 at 0.6 f_y   0.604%
#     S460 at 0.6 f_y   0.783%
#
# The claim survives any structural steel. If it ever breaks it will be the
# material pair or the allowable basis that breaks it, NEVER the geometry -- which
# is why the bound is computed from the basis rather than quoted as a constant.
# ---------------------------------------------------------------------------
def shear_geometric_bound(
    fy: float = FY_S355, nu: float = NU_STEEL, shape: str = "thin_tube"
) -> float:
    """Upper bound on ``Phi * (P/P_E)`` for any member passing its strength check.

    Returns ``12 sigma_allow / (kappa G pi^2)``. This bounds the worth of a
    shear-flexible refinement to the geometric stiffness: 0.604% for S355, i.e.
    0.17% on the moment at a 28% amplification.

    **Do not quote the number without recomputing it.** It moves with the
    allowable basis and the material, and a bare constant in a document silently
    stops being a bound the first time either changes.
    """
    g = E_STEEL / (2.0 * (1.0 + nu))
    return 12.0 * (ALLOWABLE_FACTOR * fy) / (kappa(shape, nu) * g * math.pi**2)


# ---------------------------------------------------------------------------
# Torsion constant. RAISES on shapes it cannot handle (AU3).
#
# J = I_y + I_z is the polar second moment, and it is the torsion constant ONLY
# for circular sections, where the cross-section does not warp. For any other
# shape the polar moment OVERSTATES torsional stiffness -- badly for open
# sections -- and the member comes out torsionally over-stiff with nothing in the
# suite looking for it.
#
# A docstring caveat documents the trap; it does not guard against it. So the
# unsupported case is an ERROR, never a default -- the same discipline as
# rejecting an empty parameter set, and as kappa refusing an unknown shape.
# ---------------------------------------------------------------------------
_CIRCULAR_SHAPES = frozenset({"thin_tube", "solid_circular"})


def torsion_constant(shape: str, i_y: float, i_z: float) -> float:
    """St Venant torsion constant ``J``.

    For circular sections ``J = I_y + I_z`` exactly. Raises for every other
    shape rather than returning the polar moment.
    """
    if shape not in _CIRCULAR_SHAPES:
        raise ValueError(
            f"no torsion constant for shape {shape!r}. J = I_y + I_z holds ONLY "
            "for circular sections, which do not warp; using it elsewhere makes "
            "the member torsionally over-stiff and nothing downstream checks it. "
            "Add the shape's St Venant constant here, and revisit the "
            "no-warping assumption in docs/verification/README.md before doing so."
        )
    return i_y + i_z
