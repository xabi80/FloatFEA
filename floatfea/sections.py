"""Material and section constants — one source, consumed everywhere.

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
E_STEEL: Final[float] = 210e9        # Pa
NU_STEEL: Final[float] = 0.3
RHO_STEEL: Final[float] = 7850.0     # kg/m^3
FY_S355: Final[float] = 355e6        # Pa

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
SIGMA_ALLOW_S355: Final[float] = ALLOWABLE_FACTOR * FY_S355   # 213.0 MPa

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
# Shear correction factor. SECTION-DEPENDENT AND SOURCE-DEPENDENT -- the whole
# reason this module exists.
#
# The element and every verification reference MUST take kappa from here. A
# Timoshenko tip-deflection formula evaluated with a different kappa than the
# element uses is a comparison between two different beams.
#
# Values and their sources:
#   thin-walled circular tube, simple shear-flow argument   0.5
#   thin-walled circular tube, Cowper (1966) at nu = 0.3    0.53
#   solid circular, Cowper (1966) at nu = 0.3               0.886
#   rectangular, Cowper (1966) at nu = 0.3                  0.850
#
# Cowper, G.R., "The Shear Coefficient in Timoshenko's Beam Theory", J. Appl.
# Mech. 33(2), 1966, pp. 335-340 -- Table 1.
#
# THE PROJECT USES COWPER THROUGHOUT, because it is a single consistent source
# across section types rather than a mix of conventions.
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
