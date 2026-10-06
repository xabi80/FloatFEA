"""FloatSim's time integrator, as the FE side has to know it (R653).

WHY THIS MODULE EXISTS. The replay driver reconstructs the generalized-alpha step
FloatSim took, so that `res.lam` can be read back as joint reactions. Every coefficient
of that step follows from one number, the spectral radius at infinity `rho_inf`, and that
number lived as a bare constant in `scripts/report_joint_reactions.py` where nothing
asserted it:

    cmd: grep -rn RHO_INF tests/ floatfea/
    out: (no output) -- nothing asserted this value

R653 carried that gap from F3, on the condition that it becomes blocking "if a G4.x gate
ever cites this residual as evidence that FloatSim's scheme is reproduced". F4 step 2's
G4.1 does exactly that: it reports a per-body equilibrium residual computed from the
reconstructed step. So the parameter moves here, where the FE side declares it, and the
derivation that follows from it is written once.

WHAT THIS IS NOT. It is not a tolerance -- no comparison is made against it -- so it does
not belong in `floatfea/tolerances.py`. It is not apparatus either: it is one closed-form
formula and the constant it is evaluated at, both of which the step's own gate needs.
"""

from __future__ import annotations

from typing import Final, NamedTuple

FLOATSIM_RHO_INF: Final[float] = 0.8
"""The spectral radius at infinity the replay driver reconstructs with.

It is FloatSim's value, not a choice made here, and the driver imports it from this module
so that there is exactly one copy. C131's finding is that a rule written twice drifts, and
an earlier version of the driver held two copies of this number: a `0.05` drift between
them made the residual "429x louder", which is the measurement that collapsed them into
one. Varying the single value moves the residual by about `1.0005x`, so this constant is
not what the residual is sensitive to -- a wrong RECONSTRUCTION is, by two to three
decades, and that sensitivity is the point of reconstructing at all.
"""


class GeneralizedAlpha(NamedTuple):
    """The four coefficients of one generalized-alpha step."""

    alpha_m: float
    alpha_f: float
    beta: float
    gamma: float


def generalized_alpha_coefficients(rho_inf: float) -> GeneralizedAlpha:
    """`(alpha_m, alpha_f, beta, gamma)` from the spectral radius at infinity.

    Chung & Hulbert (1993), "A time integration algorithm for structural dynamics with
    improved numerical dissipation: the generalized-alpha method", eqs. (25)-(27):

        alpha_m = (2 rho_inf - 1) / (rho_inf + 1)
        alpha_f = rho_inf / (rho_inf + 1)
        beta    = (1 - alpha_m + alpha_f)^2 / 4
        gamma   = 1/2 - alpha_m + alpha_f

    `rho_inf` in `[0, 1]`: 1 is no dissipation, 0 is asymptotic annihilation. The
    enumeration is not checked here because this is a formula, not a validator -- the
    interchange reader is what refuses a record whose `integrator` block is wrong, and
    `docs/load-interchange-v1.md` sec.2 is where the field is specified.
    """
    alpha_m = (2.0 * rho_inf - 1.0) / (rho_inf + 1.0)
    alpha_f = rho_inf / (rho_inf + 1.0)
    return GeneralizedAlpha(
        alpha_m=alpha_m,
        alpha_f=alpha_f,
        beta=0.25 * (1.0 - alpha_m + alpha_f) ** 2,
        gamma=0.5 - alpha_m + alpha_f,
    )
