"""The single home for every numerical tolerance in FloatFEA.

**This file is deliberately empty of values.** It exists before the first
tolerance does, because a guardrail that arrives after the thing it guards
never takes: by then tolerances have already been scattered into call sites and
default arguments, and consolidating them becomes a refactor nobody schedules.

---

## The rule

Every numerical tolerance in this repository lives here. No exceptions, no
local literals, no default arguments carrying a tolerance. This includes
anything that functions as a tolerance under another name -- convergence
thresholds, comparison epsilons, "small number" guards, tier cutoffs in
screening, and any factor introduced to make two numbers agree.

Do not modify this file to make a failing test pass. If a test fails, the
default hypothesis is that the code is wrong, not that the tolerance is tight.

Changing a value requires a written justification in the milestone closure
artifact (`docs/closure/F<n>.md`) naming the physical or numerical reason the
previous value was incorrect. A tolerance change in the same commit as the code
change it rescues will be rejected in review.

See `CLAUDE.md` sec. Tolerances and `WORKFLOW.md` sec. "The one habit that
matters most".

---

## The comment convention

Every entry carries four things, and a reviewer should be able to check the
value without reading any other file:

1. the **gate** it serves (G2.1, G4.1, ...) and the verification case (V1.1,
   V4.5, ...) from `docs/verification/README.md`;
2. **what is being compared** -- absolute or relative, and to what reference;
3. the **physical or numerical reason** the value is what it is, not merely that
   it passes;
4. the **date and milestone** it was last changed under.

Template::

    # G<n.n> / V<n.n> -- <what is compared, absolute or relative>
    # Reason: <physical or numerical basis for this magnitude>
    # Set: <YYYY-MM-DD>, <milestone>
    NAME: Final[float] = <value>

A value whose comment says only "empirically determined" or "matches the
reference" is not documented; it is a fudge factor with better manners.

---

## Layout

Entries are grouped by verification-ladder rung, so that a reviewer reading a
red test at rung 1 sees rung 1's tolerances together and is not invited to
compare them against rung 5's, which answer a different kind of question.

Rungs are defined in `docs/verification/README.md`.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Model construction -- geometric degeneracy guards
#
# Not tied to a verification rung: these guard the construction of the model
# itself, and they fail loudly at build time rather than producing a wrong
# number at solve time.
# ---------------------------------------------------------------------------

# G0.2 / docs/conventions.md sec. "Member local axes" -- minimum |z_hat x x_hat|
# for the DEFAULT global-Z orientation reference to be admissible on a member.
# Dimensionless; equals the sine of the member's angle from vertical.
#
# Compared: the magnitude of the cross product used to build local y, against
# this floor. Below it the model builder RAISES and demands an explicit
# orientation node or roll angle. It does not fall back to another axis.
#
# Reason: local y is built from z_hat x x_hat, so its direction error amplifies
# any perturbation in the member axis by 1/|z_hat x x_hat|. The construction is
# exactly singular at vertical and ill-conditioned near it. 0.05 corresponds to
# 2.87 deg from vertical and bounds that amplification at 20x. The spars in this
# platform are vertical, so this guard fires on the real model by design -- it
# exists to force an explicit choice, not to be tuned until it stops firing.
# Raising it excludes valid members; lowering it admits members whose section
# axes are not reliably oriented.
# Set: 2026-08-10, F0
MEMBER_ORIENTATION_DEGENERACY: Final[float] = 0.05


# G1.6 / diagnostics -- floor below which a DOF carries no signal and MUST NOT
# enter any aggregate statistic. Relative, against the largest reference
# magnitude across the DOF being aggregated.
#
# Compared: each DOF's reference magnitude (|mu|, |B|, whatever the statistic is
# formed over) divided by the maximum over that same set, against this floor.
# Below it the DOF is structurally dead and `frames.live_dof` excludes it.
#
# Reason: a body of revolution has no yaw radiation, so yaw `mu` on this platform
# is 1.2e-17 against 4.2e-01 in surge -- a ratio of 3e-17, which is round-off, not
# a small physical quantity. Including such a DOF in a correlation or a norm
# computes a statistic over noise and reports it as a measurement; it did exactly
# that once, moving an AG5 correlation from +0.53 to +0.65. The floor sits at
# 1e-12 because double precision gives ~1e-16 relative and four orders of headroom
# separates "accumulated round-off" from "small but real": the smallest genuinely
# physical ratio measured on this platform is heave's 0.01x, twelve orders above.
# Raising it would begin discarding real DOF; lowering it re-admits round-off.
# Set: 2026-08-26, F1
DEAD_DOF_RELATIVE_FLOOR: Final[float] = 1e-12


# G1.6 / diagnostics -- tolerance at or below which an INTERPOLATED reference is
# inadmissible and `frames.assert_reference_supports` refuses the comparison.
# Relative, same units as the comparison tolerance it is checked against.
#
# Compared: the tolerance a comparison intends to assert at, against this floor.
# At or below it the reference must come from a solved/exact point, not from
# interpolation between grid points.
#
# Reason: interpolating a reference across a grid gap injects an error set by how
# much the quantity varies over that gap, and it is invisible in the result. The
# measured case: omega = 2.000377 sits at 48.6% of the gap 1.930166 -> 2.074677 --
# dead centre, because case frequencies are chosen for physics, not grid alignment
# -- and B varies ~60% across it. That produced a residual of 5.914e-04 against a
# true reconstruction error of 1.359e-15: ELEVEN orders, entirely from the
# interpolation. 1e-3 sits just above the measured 5.9e-4 artifact, so a
# comparison asserting at or below it cannot distinguish its own interpolation
# from the thing it is measuring. Raising it would admit interpolated references
# into comparisons the artifact dominates; lowering it below ~6e-4 would admit the
# exact case already measured to fail.
# Set: 2026-08-27, F1
INTERPOLATED_REFERENCE_TOLERANCE_FLOOR: Final[float] = 1e-3


# ---------------------------------------------------------------------------
# Rung 1 -- The solver is a solver
# Rigid-body modes (G2.1/V1.1), patch test (G2.2/V1.2), unit scaling (G2.5/V1.3).
# These compare against exact algebraic results, so tolerances here are set by
# floating-point accumulation and conditioning, never by physical judgement.
# ---------------------------------------------------------------------------

# (no entries yet -- F2)


# ---------------------------------------------------------------------------
# Rung 2 -- The element is the element it claims to be
# Cantilever slender/stubby (G2.3/V2.1-2.2), torsion (V2.3), 3D coupling (V2.4),
# free-free frequencies (G2.4/V2.5), releases and rigid links (V2.6).
# Compared against closed-form textbook solutions.
# ---------------------------------------------------------------------------

# (no entries yet -- F2)


# ---------------------------------------------------------------------------
# Rung 3 -- The model is the platform
# Mass correctness (G3.1a/V3.1a), mass consistency (G3.1b/V3.1b), YAML
# round-trip (G3.2/V3.2), exact section properties (G3.3/V3.3).
#
# Note G3.1b is the convergence criterion of a design loop, not a code gate --
# see PLAN.md sec.6 F3. Its tolerance expresses "close enough that the analysed
# loads are representative", which is a different kind of claim from every other
# entry in this file and must say so in its comment.
# ---------------------------------------------------------------------------

# (no entries yet -- F3)


# ---------------------------------------------------------------------------
# Rung 4 -- The loads are the loads
# Equilibrium residual (G4.1/V4.1), rigid-body acceleration (G4.2/V4.2),
# hydrostatic (G4.3/V4.3), mapping conservation (G4.4), residual convergence
# rate (G4.5), hydrostatic reconciliation (G4.6), frame round-trip (V4.4),
# strip integration (V4.5), reconstruction integrity (G1.6).
#
# G4.1's tolerance must NOT be set above the timestamp-alignment floor. The
# exporter aligns each force to the index of the state it was evaluated from,
# which removes an O(omega*dt) ~ 3.2% residual at full scale; declaring that
# floor instead would put the tolerance at precisely the level that hides a real
# load-path defect. G4.5 guards the alignment by convergence RATE, not by
# magnitude. See docs/milestones/F1.md sec.6 and PLAN.md sec.8.
# ---------------------------------------------------------------------------

# (no entries yet -- F1/F4)


# ---------------------------------------------------------------------------
# Rung 5 -- Independent confirmation
# CalculiX global cross-check (G7.1/V5.1), stress recovery (G6.2/V5.2), code
# check hand calculations (G6.1/V5.3).
#
# G7.1's values are stated in PLAN.md sec.6 F7 (0.5% displacement, 1% member
# force). An exceedance is explained in writing before the milestone closes --
# never absorbed here.
# ---------------------------------------------------------------------------

# (no entries yet -- F6/F7)


# ---------------------------------------------------------------------------
# Rung 6 -- It stays fixed
# Golden-file regression (V6.1). A golden-file change requires a written
# explanation of why the numbers moved, in the milestone closure artifact.
# ---------------------------------------------------------------------------

# (no entries yet -- F6)
