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

## Two classes, and the counter-case rule binds on only one (AO2)

Every entry is **STRUCTURAL** or **ACCURACY**, and the distinction is declared in
its comment because a rule applied where it does not fit gets weakened to
accommodate.

**STRUCTURAL** — a threshold on a physical or numerical *condition*, which fires
by design when the condition holds. `MEMBER_ORIENTATION_DEGENERACY` fires on the
platform's vertical spars on purpose; it exists to force an explicit choice, not
to be tuned until it stops firing. Demanding a "smallest defect it must still
catch" of such an entry would force an artificial number.

**ACCURACY** — a ceiling on a residual or error that is *supposed* to be small.
These are the ones "the test fails, widen the tolerance" can reach, and they carry
a **paired counter-case**:

    X          = <ceiling the check asserts>
    X_COUNTER  = <smallest defect that must still fail>

The pairing is what makes the ceiling an execution result rather than a
reviewer's judgement:

* **existence is mechanically checkable** — every `X` has an `X_COUNTER`;
* **it cannot be satisfied by prose**, because `X_COUNTER` is a number an
  executable test consumes;
* **widening `X` toward `X_COUNTER` eventually breaks the counter-test.**

That last property is the point. A tolerance with a floor but no ceiling can
always be widened one more order and still look principled.


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

# CLASS: STRUCTURAL -- fires by design on vertical members; no counter-case.
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


# CLASS: STRUCTURAL -- a condition (is this DOF alive?), not an error ceiling.
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


# CLASS: STRUCTURAL -- a condition (is this reference admissible here?).
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


# CLASS: ACCURACY -- carries PANEL_RECONSTRUCTION_RESIDUAL_COUNTER below.
# G1.6 / V4.6 -- ceiling on the panel-reconstruction residual
# ||R - T||_F / ||T||_F, where R integrates the exported per-panel radiation
# pressure over each body's panels and T is w^2*A + i*w*B from the same BEM solve.
# Relative, Frobenius, dimensionless.
#
# Reason: the identity is EXACT in exact arithmetic -- both sides are the same
# surface integral, one evaluated panel-wise and one by the solver -- so the only
# admissible residual is floating-point accumulation. Measured 1.308e-15 on the
# 12-buoy platform (10,560 panels, 72 DOF) and 1.518e-16 on the committed
# 64-panel fixture. 1e-12 sits ~3 orders above the larger of those, which covers
# BLAS/platform variation in the einsum reduction without admitting anything
# physical: the smallest deliberate defect measured -- ONE panel of 10,560 with
# its area perturbed by 1% -- produced 1.082e-05, seven orders ABOVE this ceiling.
# Raising it toward 1e-5 would begin admitting real geometry errors; lowering it
# to ~1e-15 would make the gate sensitive to summation order.
# Set: 2026-08-28, F1
PANEL_RECONSTRUCTION_RESIDUAL: Final[float] = 1e-12

# COUNTER-CASE for the above -- the smallest defect the gate must still fail.
# Measured, not chosen: ONE panel of the 10,560-panel platform mesh with its
# area perturbed by 1% produces a residual of 1.082e-05. The counter-test
# asserts a perturbed fixture exceeds this value, so widening
# PANEL_RECONSTRUCTION_RESIDUAL toward it eventually makes that test fail --
# which is the property that makes the ceiling defensible by execution rather
# than by argument. Seven orders separate the two.
# Set: 2026-08-30, F1
PANEL_RECONSTRUCTION_RESIDUAL_COUNTER: Final[float] = 1.0e-5


# ---------------------------------------------------------------------------
# Rung 1 -- The solver is a solver
# Rigid-body modes (G2.1/V1.1), patch test (G2.2/V1.2), unit scaling (G2.5/V1.3).
# These compare against exact algebraic results, so tolerances here are set by
# floating-point accumulation and conditioning, never by physical judgement.
# ---------------------------------------------------------------------------

# CLASS: ACCURACY -- carries TRANSFORM_INVARIANCE_COUNTER below.
# G2.5 / V2.4 -- agreement between the rotated response and the rotated local
# response. RELATIVE AND DIMENSIONLESS, scaled by the response itself:
#
#     |u_global - R u_local|  <=  TRANSFORM_INVARIANCE * ||u_local||_inf
#
# Reason: an orthogonal transform cannot change the response, so this is exact in
# exact arithmetic and the only admissible discrepancy is accumulation through a
# 12x12 triple product and a 6x6 solve. Measured worst-case over all six load
# DOF: 3.836e-15. 1e-11 sits ~4 orders above that floor.
#
# THE FORM MATTERS AS MUCH AS THE VALUE (AW1). An earlier draft used an ABSOLUTE
# atol on a displacement, which is a dimensional quantity: posing the same problem
# in millimetres moves the round-off floor by three orders while the tolerance
# stays put, so V1.3 (unit scaling) would either fail on this assertion or pass it
# vacuously. The offending component's exact value is also ZERO, where no absolute
# floor is meaningful at all -- which is why the first draft's 1e-18 failed against
# a measured 1.07e-18 for reasons unrelated to the transform. Scaling to
# ||u_local||_inf handles the zero components by the scale rather than by a floor.
# Set: 2026-09-02, F2
TRANSFORM_INVARIANCE: Final[float] = 1e-11

# COUNTER-CASE, measured IN THE SAME QUANTITY as the assertion (AW1).
# A _COUNTER is the smallest defect the SAME assertion detects, so it is measured
# on the displacement residual, not on the spectrum. Perturbing the correct
# rotation by the non-orthogonal I + [theta x] map gives a residual linear in
# theta: 1.227e-02 at 1e-3 rad, 1.228e-05 at 1e-6, 1.228e-07 at 1e-8. The
# counter is set at the last of these, so the gate must catch a non-orthogonality
# of TEN NANORADIANS -- four orders above the ceiling, and far below any
# first-order-rotation bug a real model could contain.
# Set: 2026-09-02, F2
TRANSFORM_INVARIANCE_COUNTER: Final[float] = 1.2e-7


# CLASS: ACCURACY -- carries TRANSFORM_SPECTRUM_INVARIANCE_COUNTER below.
# G2.5 / V2.4 -- relative agreement between eig(T^T K T) and eig(K), scaled by the
# largest eigenvalue. A separate entry from TRANSFORM_INVARIANCE because it is a
# DIFFERENT QUANTITY: the spectrum test is the only one that detects a
# non-orthogonal T without reference to any particular load case.
#
# Reason: an orthogonal similarity preserves eigenvalues identically. Measured
# shift under the real transform: 2.71e-16. 1e-11 sits ~5 orders above it.
# Set: 2026-09-02, F2
TRANSFORM_SPECTRUM_INVARIANCE: Final[float] = 1e-11

# COUNTER-CASE for the spectrum test, measured on the spectrum.
# The I + [theta x] trap shifts the spectrum by 1.30e-03 at theta = 0.05 rad,
# 5.20e-05 at 0.01, and 5.20e-07 at 0.001 -- so the gate must catch a first-order
# rotation of a milliradian.
# Set: 2026-09-02, F2
TRANSFORM_SPECTRUM_INVARIANCE_COUNTER: Final[float] = 5.0e-7


# CLASS: ACCURACY -- carries SUBDIVISION_INVARIANCE_COUNTER below.
# G2.2 / V1.2 -- relative agreement of a fixed-length cantilever's tip response
# across element counts. Dimensionless (a ratio of like quantities).
#
# Reason: the element is NODALLY EXACT for constant section and load, so
# subdividing changes nothing but round-off. Measured deviation from the
# one-element result: 9.99e-15 at n=2, 1.16e-14 at n=5, 4.58e-13 at n=11 -- and
# the per-solve equilibrium residual grows with it, 1.38e-14 to 8.79e-13 over the
# same range. That growth is a CONDITIONING signature, not a formulation error:
# more DOF means a longer factorisation chain. 1e-11 sits ~20x above the worst
# measured deviation, which leaves room for that growth at the mesh sizes F3 will
# use without admitting anything structural.
#
# DECLARED LATE (AW2). This value existed as an undeclared `rtol=1e-10` literal
# inside the test before it was measured, which is the local-literal failure this
# file exists to prevent.
# Set: 2026-09-02, F2
SUBDIVISION_INVARIANCE: Final[float] = 1e-11

# COUNTER-CASE, measured on the same quantity.
# A relative stiffness error in ONE member of the chain produces a tip deviation
# linear in it: 4.84e-04 at 1e-3, 4.85e-06 at 1e-5, 4.85e-08 at 1e-7. The counter
# is set at the last, so the gate must catch a one-part-in-10^7 error in a single
# element -- three orders above the ceiling.
# Set: 2026-09-02, F2
SUBDIVISION_INVARIANCE_COUNTER: Final[float] = 4.8e-8


# CLASS: ACCURACY -- carries PATCH_TEST_EXACTNESS_COUNTER below.
# G2.2 / V1.2 -- deviation of the interior nodal displacements from the exact
# constant-strain field, in a DISPLACEMENT-DRIVEN patch test on an irregular
# mesh. Relative, scaled by the largest component of the exact field, so it is
# dimensionless and survives V1.3's unit rescaling.
#
# Reason: the four constant-strain states -- axial, curvature, twist, and
# constant shear with linear moment -- are reproduced EXACTLY by this element,
# not in the limit, so the only admissible deviation is round-off. Measured over
# all four states:
#
#   axis-aligned   2.88e-17 .. 2.00e-16
#   skew straight  1.41e-15 .. 4.19e-15   (transform accumulation)
#
# 1e-12 sits ~240x above the worst measured value, which covers the transform
# path and longer chains, and ~30000x below the counter-case.
#
# UNIT SYSTEM AND FLOOR (R2). Declared in SI metres, and VERIFIED invariant
# across length-unit factors S = 1e-3 .. 1e+3 (kilometres to millimetres): worst
# error 3.12e-14, no breach at any scale. That invariance is not automatic and was
# not present when this entry was written -- it required two fixes, neither of
# them a tolerance change:
#
#   1. the solve equilibrates (assemble.system.equilibrate), because translational
#      and rotational diagonal entries scale as S^-1 and S^+1, so their ratio moves
#      by S^2 and cond(K_ff) went 9.2e2 -> 4.0e7 over that range. Equilibrated,
#      cond(K~) = 3.85e2 at EVERY scale.
#   2. the error measure weights rotations by a characteristic length, because
#      taking max() across all six DOF mixes metres with radians and is therefore
#      unit-dependent on its own.
#
# Floor, as a multiple of the equilibrated conditioning: cond(K~) * eps =
# 3.85e2 * 2.22e-16 = 8.5e-14. The worst measured error is 0.37x that floor and
# this ceiling is ~12x it.
#
# THIS IS AN EXACTNESS TOLERANCE, NOT A CONVERGENCE ONE. An element that
# reproduces constant curvature only in the limit is passing a convergence test
# wearing the patch test's clothes; there is nothing between exact and wrong here,
# which is why the value sits at ULP scale rather than at an engineering one.
# Set: 2026-09-02, F2
PATCH_TEST_EXACTNESS: Final[float] = 1e-12

# COUNTER-CASE, measured on the same quantity and in the WORST state.
# A relative stiffness error in ONE interior element perturbs the interior field
# linearly: at 1e-6 the four states move by 1.09e-07 (axial), 1.09e-07 (twist),
# 3.72e-08 (curvature) and 3.02e-08 (shear). The counter is set at the SMALLEST
# of those, so every state must catch a one-part-in-10^6 stiffness error, not
# merely the most sensitive one.
#
# TIGHTENED 2026-09-03, from 3.0e-8, under the dimensionally homogeneous error
# measure (R2). The assertion is `err >= COUNTER`, so raising it makes the negative
# control STRICTER, not weaker. Under the old mixed-unit measure the bending
# states' rotational error was divided by a translational scale and thereby
# understated at 3.72e-08 and 3.02e-08; measured coherently all six states respond
# at 1.08e-07 .. 1.17e-07 and the counter moves to the smallest of those.
#
# Its earlier history: 6.0e-9 came from a mesh containing 0.9/0.6 = 3/2 exactly.
# The claim that changing that mesh bought a fivefold improvement is WITHDRAWN --
# controlled measurement puts commensurability at 0.848x, i.e. nothing. The value
# moved because the perturbed element's length and position changed with it. See
# docs/instrumentation.md, seventeenth guard.
# Set: 2026-09-03, F2
PATCH_TEST_EXACTNESS_COUNTER: Final[float] = 1.0e-7


# CLASS: ACCURACY -- carries MATRIX_SYMMETRY_COUNTER below.
# G2.1 / V1.1 -- symmetry of an assembled or element stiffness matrix, relative,
# scaled by the largest entry. Dimensionless.
#
# Reason: K is symmetric in exact arithmetic (Maxwell-Betti), so the only
# admissible asymmetry is accumulation through the 12x12 triple product and the
# scatter-add. Measured on the element and on a 5-member assembly: max |K - K^T|
# / max |K| is 0.0 exactly for a single element and 2.4e-16 assembled. 1e-9 sits
# ~7 orders above that, which covers longer chains without admitting a
# transposed block (which shows at O(1)).
# Set: 2026-09-03, F2
MATRIX_SYMMETRY: Final[float] = 1e-9

# COUNTER-CASE: one transposed element block, the defect this shape of error
# actually takes. Measured: transposing one 12x12 element contribution makes
# max |K - K^T| / max |K| = 3.1e-01, eight orders above the ceiling.
# Set: 2026-09-03, F2
MATRIX_SYMMETRY_COUNTER: Final[float] = 1.0e-2


# CLASS: ACCURACY -- carries ROUNDOFF_IDENTITY_COUNTER below.
# Rung 1 -- relative agreement for a property that is EXACT in exact arithmetic
# and is asserted at round-off: triad orthonormality, reciprocity of a
# flexibility matrix, the equality of two algebraically identical expressions.
# Dimensionless in every use.
#
# Reason: these have no discretisation error to bound, only floating-point
# accumulation. Measured across the sites that use it, the worst is 4.9e-15.
# 1e-12 sits ~200x above that. It is deliberately ONE value shared by several
# assertions of the same kind rather than a literal at each site -- which is what
# it replaced, and what AW2 and R13 were both about.
# Set: 2026-09-03, F2
ROUNDOFF_IDENTITY: Final[float] = 1e-12

# COUNTER-CASE: the smallest defect these assertions must still catch. A single
# sign error or a swapped index in any of the quantities involved is O(1); the
# subtlest real case measured is the non-orthogonal I + [theta x] map at
# theta = 1e-8, which perturbs orthonormality by 1.0e-08.
# Set: 2026-09-03, F2
ROUNDOFF_IDENTITY_COUNTER: Final[float] = 1.0e-8


# CLASS: ACCURACY -- carries COND_UNIT_INVARIANCE_COUNTER below.
# G2.5 / V1.3 -- relative agreement of cond(D^-1/2 K D^-1/2) between two unit
# systems. Dimensionless.
#
# Reason: equilibration makes the conditioning algebraically invariant under a
# diagonal rescaling, so this is exact in exact arithmetic; measured agreement
# across S = 1e-3 .. 1e+3 is within 1e-11. 1e-6 leaves room for the eigenvalue
# computation on an ill-conditioned unequilibrated input without admitting a real
# drift.
#
# DECLARED LATE (R13). This was a bare `rel=1e-6` inside the test, written two
# commits after AW2 closed on exactly that defect.
# Set: 2026-09-03, F2
COND_UNIT_INVARIANCE: Final[float] = 1e-6

# COUNTER-CASE: without equilibration cond(K_ff) spans 6.5e5 across the same unit
# systems, so the assertion must catch anything at or above that ratio; the
# counter is set far below it, at the smallest drift worth investigating.
# Set: 2026-09-03, F2
COND_UNIT_INVARIANCE_COUNTER: Final[float] = 1.0e-3


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
