# Verification Ladder

Every case here is an automated test with a numeric pass/fail criterion. The
ladder is ordered so that a failure at rung *n* makes rungs above it
uninterpretable — which means a red test low on the ladder is never worked
around by looking at a green test higher up.

Tolerances are not stated in this document. They live in `floatfea/tolerances.py`
so there is exactly one place to review when one changes. See `CLAUDE.md` §
Tolerances.

---

## Rung 1 — The solver is a solver

**V1.1 Rigid-body modes.** An unconstrained model has exactly six zero-energy
modes. Test the eigenvalue ratio against the first flexible mode, not an
absolute value, so the test is mesh- and unit-independent. *Gate G2.1.*

**V1.2 Patch test.** A small irregular assembly under boundary conditions
corresponding to a constant strain state recovers that state exactly. This is
the test that catches assembly, transformation, and connectivity errors, and it
is the reason it sits below every accuracy comparison. *Gate G2.2.*

**V1.3 Unit scaling.** The same physical problem posed in a scaled unit system
produces correctly scaled results. Catches hardcoded constants and implicit unit
assumptions — cheap to write, and it finds a class of bug that no amount of
comparison against a single reference case will. *Gate G2.5.*

## Rung 2 — The element is the element it claims to be

**V2.1 Cantilever, slender.** Tip deflection under end load against `PL³/3EI`,
and under end moment against `ML²/2EI`.

**V2.2 Cantilever, stubby.** Same, on a beam short enough that the Timoshenko
shear term is a significant fraction of total deflection. A Euler-Bernoulli
implementation mislabelled as Timoshenko passes V2.1 and fails here. *Gate G2.3.*

**V2.3 Torsion and warping.** Circular hollow section under pure torque against
`TL/GJ`. Tubulars make this the well-behaved case; note in the results whether
any non-circular section is ever introduced, because warping restraint then
stops being negligible.

**V2.4 Three-dimensional coupling.** A curved or helical member, or a portal
frame out of plane, where axial, bending, and torsion couple through the
transformation. Catches sign and axis errors in the local-to-global transform
that planar cases cannot see.

**V2.5 Free-free frequencies.** Natural frequencies of a free-free beam against
analytic values. Exercises the mass matrix, which none of the static cases
touch. *Gate G2.4.*

**V2.6 End releases and rigid links.** A pinned-end member carries no end
moment; a rigid link reproduces exact kinematic transfer. Both are constraint-
handling tests disguised as element tests.

## Rung 3 — The model is the platform

**V3.1a Mass correctness.** Per-body mass, CoG, and inertia tensor computed from
the FE mesh against the model-definition YAML. Reported per body. A global total
that matches while individual bodies do not is a failure, not a pass — so the
test asserts per body and never on the sum. *Gate G3.1a.*

**V3.1b Mass consistency.** The same properties against the FloatSim body
properties used to generate the loads under analysis. This one is the
convergence criterion of a design loop, not a code test: it is expected to fail
on early iterations and its failure means the loads are not representative, not
that the code is wrong. *Gate G3.1b.*

**V3.3 Exact section properties.** Section modulus and area from exact hollow-
section formulae, cross-checked against an independent calculation. Thin-wall
approximations are order-check tools only. `πD²t/4` on outer diameter overstates
section modulus by 20% — unconservative on strength, conservative on weight, so
a paired mass-and-strength check made from both looks self-consistent while
being wrong in the direction that matters. *Gate G3.3.*

**V3.2 Model definition round-trip.** YAML in, model built, YAML out, no loss.
*Gate G3.2.*

## Rung 4 — The loads are the loads

This rung is where the project's real risk lives. An equilibrium error does not
crash anything; it produces a plausible answer that is wrong.

**V4.1 Self-equilibrium residual.** For every load case, the sum of applied
loads including d'Alembert inertia, as a fraction of total applied load
magnitude, below tolerance. Reported per case in the run log. Never averaged
across cases, because the average of one bad case and forty good ones passes.
*Gate G4.1.*

**V4.2 Rigid-body acceleration.** A load case built from pure rigid-body
acceleration with no external load produces near-zero internal stress. The
sharpest single test of the load path: it fails if the inertial distribution,
the mass matrix, or the inertia relief constraint is wrong, and it cannot be
passed by a broken implementation that happens to balance. *Gate G4.2.*

**V4.3 Hydrostatic.** A still-water case reproduces the analytically known
buoyancy distribution and zero net force against weight. *Gate G4.3.*

**V4.4 Frame round-trip.** A load defined in a body frame, transformed to
global and back, returns to itself. Trivial to write, and it is the test that
catches the FloatSim-to-FloatFEA convention mismatch that `docs/conventions.md`
exists to prevent.

**V4.5 Strip integration.** Strip-resolved loads integrate along each member
back to the body resultant for the same source and timestep, within tolerance.
This is the only test that catches a strip export which is internally consistent
but does not correspond to the loads FloatSim actually applied — the strip data
would look perfectly reasonable, and the structure would be loaded with
something the simulator never computed. *Numerical half of gate G1.4.*

**V4.6 Replay consistency.** The second-pass replay that generates strip data
reproduces the screening run's body-level channels bit-identically. If it drifts,
the strip loads belong to a slightly different trajectory than the snapshot they
are attached to. *Gate G1.4.*

## Rung 5 — Independent confirmation

**V5.1 CalculiX global cross-check.** The identical global model exported as a
CalculiX B31 deck. Displacements and member forces compared. This is the only
test in the suite that a shared misconception cannot pass, which is why it runs
against the real platform model and not a toy. Any exceedance is explained in
writing before the milestone closes — never absorbed by widening the tolerance.
*Gate G7.1.*

**V5.2 Stress recovery cross-check.** Section stresses at circumferential
recovery points against CalculiX on the same section. *Gate G6.2.*

**V5.3 Code check hand calculations.** Each API RP 2A-WSD utilisation term
verified against an independent hand calculation, worked and stored in this
directory. One document per check, showing the input, the clause, the arithmetic,
and the code result. *Gate G6.1.*

Note the standard is a locked decision (PLAN.md F6) and these hand calculations
are written against it. A later migration to ISO 19902 invalidates every
document in this set, which is the main reason the choice was made up front.

## Rung 6 — It stays fixed

**V6.1 Golden-file regression.** Reference results stored for the full
verification set and the platform model. Any change in any stored result fails
the build. A legitimate change is accompanied by a regenerated golden file and a
written explanation of why the numbers moved, recorded in the milestone closure
artifact.
