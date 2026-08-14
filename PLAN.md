# FloatFEA — Structural Analysis of the Floating Platform from FloatSim Loads

**Status:** skeleton plan, awaiting review
**Owner:** Xabier
**Companion project:** FloatSim / HSP (`github.com/xabi80/HSP`)
**Target:** verified global structural capability by **2026-10-04** (8 weeks)

---

## 1. Purpose

FloatSim answers *how does the platform move*. It does not answer *does the
structure survive*. FloatFEA closes that gap: it takes the load and motion
histories FloatSim produces for the 12-buoy platform (4 clusters × 3 buoys,
38 DOFs) and turns them into member forces, stresses, and code utilisations
for the physical parts of the structure.

The two codebases stay separate. They meet at one place only: a versioned load
interchange file. That boundary is deliberate. It keeps FloatSim's audit history
clean, it lets FloatFEA be verified against textbook problems with no
hydrodynamics anywhere in the loop, and it means a change to either side is
forced to declare itself at the schema.

## 2. Solver strategy

The solver is split along a real difficulty cliff rather than along a
convenience line.

The **global model is solved by our own Python code**. A three-dimensional
two-node Timoshenko beam element is a closed-form, fully bounded problem: the
stiffness matrix is analytic, the verification cases are in textbooks, and the
whole element library needed for a space frame — beam, rigid link, spring,
point mass — is a few thousand lines. Owning it means the load-transfer chain
from FloatSim to member force is inspectable end to end, with no black box in
the middle of the only part of the calculation that is genuinely novel here.
This is also the part where a commercial tool would be least helpful, because
the difficulty is in the load mapping, not in the linear algebra.

The **detailed sub-models are solved by CalculiX**. Writing a shell and solid
solver with buckling, contact, and plasticity is a multi-year effort that would
consume the schedule and still fall short of a mature free solver. CalculiX
reads Abaqus `.inp` syntax, which is already familiar, so the work reduces to
deck generation and result extraction — pre- and post-processing we own anyway.

CalculiX earns its place a second time as an **independent check on our own
solver**. It has B31 beam elements, so the identical global model can be run
both ways from week one and the results compared. That cross-check is worth
more than any amount of internal unit testing, because it is the only test in
the suite that a shared misconception cannot pass.

Long term this does not foreclose replacing CalculiX with our own shell
capability. It sequences that ambition behind a working tool instead of in
front of it.

## 3. Architecture

```
HSP / FloatSim                    FloatFEA
──────────────                    ────────
time-domain solve
      │
      ├─ load export ──►  .flr file  ──►  reader + validator
      │  (additive, @tag)  (versioned)         │
                                               ├─ screening → load case set
  model definition (YAML) ──────────────────►  ├─ model builder
                                               ├─ mass reconciliation
                                               ├─ load mapping + inertia relief
                                               ├─ linear static solve
                                               ├─ force / stress recovery
                                               ├─ code checks (API RP 2A / ISO 19902)
                                               │
                                               ├─► envelope report + VTK
                                               └─► CalculiX .inp  ──► sub-models
```

Package layout:

```
floatfea/
  io/          reader, validator, schema versioning
  screen/      response metrics, snapshot selection, envelope convergence
  model/       nodes, elements, sections, materials, model builder
  solve/       assembly, constraints, inertia relief, linear solve
  loads/       mapping FloatSim loads onto the FE mesh, equilibrium check
  post/        force and stress recovery, envelopes, VTK output
  checks/      API RP 2A / ISO 19902 member and joint utilisation
  export/      CalculiX deck generation, sub-model cut-boundary extraction
docs/
  conventions.md, load-interchange-v1.md, verification/
tests/
  unit/, verification/, regression/
```

## 4. Load fidelity, and the dependency it creates on HSP

The fidelity ceiling of the whole tool is set by what FloatSim writes out, not
by anything in FloatFEA. This is the single most important finding in this plan
and it changes what the first work item is.

A net six-component load on a rigid body cannot be correctly distributed onto a
flexible frame. If FloatSim exports only a resultant force and moment per buoy,
FloatFEA has to invent a distribution, and every member force downstream
inherits that invention. What is needed instead is loads **decomposed by
physical origin, each with its point or line of application**: gravity and
inertia are body forces distributed by mass; hydrostatic and Froude-Krylov are
surface pressures distributed by wetted geometry; Morison drag is a line load
along the member; connector and mooring loads are point loads at known
attachment nodes. Each distributes differently, so each must arrive separately.

### Locked decision: strip-resolved loads in v1

Distributed loads are exported **per strip, not as per-body resultants.**

Morison drag is the dominant distributed load on this structure and it varies
as `u|u|` with wave kinematics that decay exponentially with depth. On a member
spanning the splash zone to depth, assuming a distribution misplaces the
resultant along the member axis, and bending moment scales directly with that
lever arm. The resulting error lands in the tens of percent, in the quantity
that usually governs tubular utilisation. Members would be sized against an
artifact of our own assumption.

This is affordable because **FloatSim already computes the strip loads.**
Morison is evaluated strip by strip and integrated up to the body resultant, so
the values exist at every timestep and are currently discarded. Exporting them
retains an intermediate; it is not new physics and not new computation.

Storage is the real objection and it is handled by not storing the full history.
Twelve buoys at roughly twenty strips, across all load sources, over a
three-hour sea state runs to a few gigabytes. Instead the export runs in two
passes: **a screening pass writing only the small body-level channels, then a
deterministic replay writing strip-resolved output for the selected snapshots
only.** Forty snapshots with a short window around each — enough to confirm a
peak is physical and not a numerical spike — is tens of megabytes.

The consequence is that **deterministic replay becomes a hard requirement on
FloatSim**: same seed and same inputs must reproduce the run bit-identically.
That is a capability worth having independently, but it is now on the critical
path and is gated at G1.4.

### The first task is an audit, not an implementation

Before designing any HSP change, **audit what FloatSim already writes to disk.**
If the per-body load decomposition is already present in the existing output
files, the v1 writer can live entirely inside FloatFEA as a converter and HSP
need not change at all for that part. Only the strip channels and the replay
hook are likely to require touching HSP. Establishing which is which, first,
is the cheapest hour in the project.

Where HSP does change, it changes **additively and against a tag** — see
`docs/hsp-coupling.md`. No fork.

## 5. Load cases: screening

Full transient FE over the time history is not planned. The structure is stiff
relative to wave periods, so a quasi-static treatment of screened snapshots
captures what sizes members, at a fraction of the cost.

Screening runs in two passes, because the honest answer to "did I screen enough
cases?" is a measurement, not a judgement.

**First pass** ranks the time history by proxy response metrics: per-connector
axial, shear and moment; per-cluster interface resultants; global base shear and
overturning moment; platform pitch and roll extremes; vertical acceleration
extremes; mooring line tensions; and relative motion between adjacent buoys,
which is what actually drives connector load. The timestep of each maximum and
each minimum becomes a candidate snapshot. Many metrics peak at the same instant,
so after de-duplication expect roughly twenty to sixty unique snapshots per sea
state.

**Second pass** runs the candidates through the FE model, builds member force
envelopes, then adds the next tier of candidates and measures how much the
envelope grows. If adding tier two moves any governing utilisation by less than
a stated threshold, screening has converged and the number is defensible. If it
does not, widen and repeat. That convergence measurement is gate G5.2 and it is
the difference between a screened load set and a guessed one.

## 6. Milestones and gates

Every gate is an automated test in CI. A gate that lives only in a document is
not a gate.

### F0 — Repo bootstrap and conventions lock · *Week 1, first half*

Repo created, CI running, test harness in place. `docs/conventions.md` written
and locked: coordinate frames, sign conventions, units, rotation representation,
node and element numbering. It must explicitly reference and reconcile with
FloatSim's `docs/multibody-conventions.md` — where the two differ, the
transformation is written down here, once.

- **G0.1** CI green on an empty test suite; lint and type-check configured.
- **G0.2** Conventions document reviewed and merged; a machine-readable copy of
  the frame definitions exists for the validator to check against.
- **G0.3** HSP reference tag created at the current known-good state, and a
  second worktree checked out at that tag so production FloatSim runs continue
  undisturbed while export development proceeds on main. FloatFEA records the
  tag it is pinned to. Which commit to tag is a question for Xabier, not an
  assumption — it is not necessarily the tip of main. See `docs/hsp-coupling.md`.

### F1 — Load interchange schema v1 · *Week 1–2*

Begins with the output audit of §4. Schema then specified and versioned. Writer
implemented wherever the audit says it belongs — in FloatFEA as a converter
where existing output suffices, additively in HSP where it does not. Reader and
validator in FloatFEA. See `docs/load-interchange-v1.md` and
`docs/hsp-coupling.md`.

- **G1.0** Existing FloatSim output audited and documented: which required
  channels already exist, which need new export, and which need the replay hook.
  This gate is a written finding, not code, and it blocks the schema lock.
- **G1.1** Round-trip test: a synthetic load record written by the writer and
  read by FloatFEA reproduces every channel bit-exact.
- **G1.2** The validator rejects, with a specific message, each of: unknown
  schema version, missing units declaration, unit mismatch, undeclared frame,
  non-normalised quaternion, NaN or inf in any channel, and a body whose inertia
  tensor is not positive definite.
- **G1.3** Every record carries the HSP git SHA and FloatSim run ID. A record
  without provenance is rejected, not warned about.
- **G1.4** Deterministic replay: the same seed and inputs reproduce the
  screening run bit-identically, and the replay that generates strip output
  reproduces the screening run's body-level resultants within tolerance.
  Without this the two-pass strip export is unsound.
- **G1.5** Additive-only proof: HSP's existing regression suite produces
  bit-identical results on the export branch and at the reference tag. Any
  difference means the solve path was touched and the change is rejected.
- **G1.6 — reconstruction integrity.** Per-panel pressures and per-strip loads,
  integrated over each hull, reproduce the body-level force FloatSim actually
  applied — excitation, radiation, drag — **per body and per source**, per
  timestep, within tolerance. Never as a single global residual: harmonic
  content concentrates near the free surface and on the heave plate, so a bad
  heave plate averages away against clean spar panels.

  Report the residual's **spectral content** alongside its magnitude. Linear
  hydro responds at whatever frequencies the motion contains, and the motion is
  periodic but not sinusoidal because drag and the joint constraints are
  nonlinear. Reconstructing at the fundamental is cheap and probably
  sufficient; the general answer is a per-panel retardation convolution and is
  expensive. Residual energy at 2ω and 3ω is the signal that the convolution is
  needed, and roughly at what order — which turns the decision into a
  measurement rather than a judgement call.

### F2 — Beam solver core · *Week 2–3*

Nodes, 3D Timoshenko beam elements with shear deformation, end releases, rigid
links via multi-point constraints, springs, point masses. Sparse assembly,
direct linear solve. Geometric stiffness is designed for but may be deferred.

- **G2.1** Six rigid-body modes with zero strain energy, to machine precision
  relative to the first flexible mode.
- **G2.2** Patch test: a constant strain state is recovered exactly.
- **G2.3** Cantilever tip deflection matches closed form, including the shear
  term verified on a deliberately stubby beam where Euler-Bernoulli would fail.
- **G2.4** Free-free beam natural frequencies match analytic values.
- **G2.5** Unit-scaling test: the same model in a scaled unit system produces
  correctly scaled results, catching hardcoded constants.

### F3 — Model builder and mass reconciliation · *Week 4*

**Precondition — full-scale deck and BEM re-run.** Deferred out of F1 by decision
(2026-08-13) and binding here. G3.1b compares FE mass properties against the
FloatSim body properties that generated the loads, and the FE model is inherently
full scale — S355, an 8.41 m spar, 180 mm walls, full-scale allowables. Comparing
that against a model-scale record requires exactly the conversion the
full-scale decision forbids, not as a convenience but as the only way to make the
comparison at all. F4 is where loads reach the structure; **F3 is where the scales
must already agree.**

Riding with it: re-characterisation of the surge drift at full-scale Reynolds
(the spar carries almost all of the drift brake, and Cd = 1.2 is a subcritical
value), and the carried G1.6 obligation from F1 — re-run on the first full-scale
record and record the result.

Parametric platform model generated from a YAML model definition. Body mass,
centre of gravity, and inertia tensor computed from the FE mesh and reconciled
against the values FloatSim used.

Mass reconciliation is **two gates, not one**. The original single gate assumed
the FE mass could be checked against a fixed FloatSim mass. It cannot: the buoys
carry the entire floating mass, so structural weight sets draft, which sets the
hydrostatics and the BEM, which sets the loads that size the structure. That is
a design loop, and a single pass/fail gate placed across it would never close.

- **G3.1a — correctness.** The FE model reproduces the mass, CoG, and inertia
  tensor of its own model-definition YAML. A pure code gate, always passable,
  and it blocks F4.
- **G3.1b — consistency.** FE mass properties match the FloatSim body properties
  **used to generate the loads being analysed**. This is the convergence
  criterion of the design loop, not a code gate. It does not block building the
  pipeline; it blocks *trusting a result*. Every report states which iteration
  it belongs to and whether G3.1b held for it.
- **G3.2** Model definition round-trips through YAML without loss.
- **G3.3** Section properties are computed from exact hollow-section formulae.
  Thin-wall approximations are permitted for order-checks only, must be labelled
  as such, and must use mean diameter — `πD²t/4` on outer diameter overstates
  section modulus by 20% and is unconservative.

**For the eight-week window, freeze the mass.** Adopt a structural mass estimate,
put it into FloatSim, run, and analyse against it. Converge the *pipeline* in
this window and the *design* in Phase 2. Iterating the loop inside the eight
weeks means BEM re-runs on the critical path, which the schedule does not carry.

### F4 — Load mapping and inertia relief · *Week 5–6*

FloatSim loads mapped onto FE nodes by physical origin. Inertial loads
distributed by the FE mass matrix. Self-equilibrium verified. Inertia relief
solve implemented via Lagrange multipliers on six rigid-body constraints, which
has the useful property that the multipliers *are* the residual reactions and so
double as a diagnostic.

- **G4.1** Residual imbalance, as a fraction of total applied load magnitude,
  below tolerance for every load case. Reported per case in the run log, never
  aggregated into a single number that can hide an outlier.
- **G4.2** A pure rigid-body acceleration case produces near-zero internal
  stress — the sharpest single test of the whole load path.
- **G4.3** A pure hydrostatic case reproduces the analytically known buoyancy
  distribution.
- **G4.4 — mapping conservation.** Distributed loads mapped from the hydro
  discretisation onto the FE mesh preserve total force **and moment about a
  common point**, per body and per source. This is a distinct failure mode from
  G1.6: G1.6 tests that the *exported* field reproduces what FloatSim applied,
  G4.4 tests that *transferring* it onto a non-matching mesh loses nothing. A
  panel field can pass G1.6 and still be mapped wrongly.
- **G4.6 — hydrostatic reconciliation.** FloatFEA's recomputed buoyancy,
  linearised about ξ=0, reproduces FloatSim's hydrostatic restoring matrix `C`
  per body, 6×6, within tolerance.

  Gravity and hydrostatic cancel inside `C` at ξ=0 upstream, so neither can be
  extracted from it — `C` is a restoring derivative, not a load. Both are
  therefore reconstructed independently in FloatFEA: gravity from the FE mass
  distribution, buoyancy from the hull geometry. This gate is what confirms the
  reconstruction matches the model that generated the motions. Disagreement
  means the hull geometry or the waterplane differs between the two models, and
  it must surface here rather than as an unexplained G4.1 residual.

  Buoyancy is evaluated on the **mean** wetted surface, matching FloatSim's
  linearisation. Evaluating on the instantaneous surface introduces a
  nonlinearity FloatSim never had, which appears as a G4.1 residual with no
  obvious cause. This is a deliberate consistency choice, not an approximation
  to be improved later without reopening the gate.
- **G4.5 — residual convergence rate.** With the exporter's timestamp alignment
  in place, the equilibrium residual must fall at the expected order under
  timestep refinement. Run at Δt and Δt/2 and check the *rate*, not just the
  magnitude. A re-introduced one-step lag reverts the rate to first order while
  the absolute residual may still look acceptable, so the rate is the property
  that actually guards the fix.

### F5 — Screening and load case generation · *Week 6*

Response metric extraction, snapshot selection, envelope convergence check.
Implementation lands here, but the metric list must be **specified during F1**,
because it determines which channels the schema has to carry.

- **G5.1** The case list is reproducible: same input record and same criteria
  produce a byte-identical case list.
- **G5.2** Envelope convergence: adding the next tier of candidate snapshots
  changes no governing utilisation by more than the stated threshold.

### F6 — Post-processing and code checks · *Week 7–8*

Member force recovery, stress recovery at circumferential points on tubulars,
member utilisation, envelope reporting, VTK output.

**Locked decision: API RP 2A-WSD.** Working stress design means the clauses are
compact closed-form equations, so each check can be verified against an
independent hand calculation — exactly what G6.1 requires when the checks are
being implemented from scratch. ISO 19902 is LRFD, and its partial factors
depend on load category, which would require categorisation metadata that the
screening pass does not produce and the schema does not carry. That is scope
creep into F5 and F1 for no benefit at this stage. Migration to ISO later is a
bounded change confined to `checks/`.

**These checks are a sizing screen, not a compliance calculation.** Both API RP
2A and ISO 19902 are written for fixed jackets; neither is a certification basis
for a floating platform. Actual certification lives in the DNV series, and shell
buckling of the buoy cans specifically is DNV-RP-C202 territory, which is
sub-model work in F7 and not a beam-level check. F6 exists to find the governing
members and their approximate utilisations. The reports it generates must say so
on their face, so that a result read twelve months from now is not mistaken for
a code case.

- **G6.1** Each individual code check verified against an independent hand
  calculation, documented in `docs/verification/`.
- **G6.2** Stress recovery cross-checked against CalculiX on the same section.
- **G6.3** Envelope report regenerates identically from stored results.

### F7 — CalculiX cross-check and sub-model export · *Week 8 onward*

The global model exported as a CalculiX B31 deck and compared. Then sub-model
export: cut-boundary forces from the global model driving shell models of
critical joints and cans.

- **G7.1** Global displacements agree with CalculiX within 0.5%; member forces
  within 1%. Any exceedance is explained in writing before proceeding.
- **G7.2** Sub-model cut boundaries are in equilibrium with the global member
  forces they were extracted from.

**F7 deliberately straddles the two-month line.** The staged global-then-detail
scope is more than eight weeks of work. What fits is the global capability,
fully verified, with the sub-model path opened rather than finished.

## 7. Definition of done at eight weeks

A verified global space-frame model of the platform, loaded from screened
FloatSim extreme cases with strip-resolved distributed loads, producing member
forces and API RP 2A-WSD utilisations, with every gate F0 through F6 passing in
CI and the CalculiX cross-check of G7.1 complete. Fatigue, shell sub-models,
geometric nonlinearity, and any DNV code basis are explicitly out of scope for
this window and are the natural F8 onward.

## 8. Risk register

The two schedule risks are F1 and F4, and they are the same risk wearing
different clothes: both are about whether the loads arriving at the structure
are physically right.

F1 is at risk because it depends on new work in a *different* repository, under
that repo's own review gating, and because the strip export and the replay hook
may be more invasive than they look. Mitigation is to start F1 first, before any
FloatFEA solver code exists, and to open it with the G1.0 audit — which either
shrinks the HSP work to nothing or tells you in week one exactly how big it is.
The beam solver depends on nothing upstream and can proceed in parallel, so an
F1 slip does not idle the schedule.

Deterministic replay (G1.4) is the specific piece most likely to surprise. If
FloatSim turns out not to replay bit-identically — an accumulated floating-point
path, an unseeded random draw, a wall-clock dependency — the two-pass strip
export is unsound and the fallback is decimated strip output over the full
history, at higher storage cost. Test replay determinism in week one, before
building anything on top of it.

F4 is at risk because equilibrium bugs are quiet. A model with a 3% load
imbalance still solves, still produces plausible contour plots, and is still
wrong. Mitigation is G4.1 reported per case rather than averaged, plus G4.2,
which is designed so that a broken load path cannot produce a passing result.

That 3% is not hypothetical. A one-step misalignment between force and state
channels produces a residual of order `ωΔt`, which at ω = 0.45 rad/s and
Δt = 0.0707 s is 3.2% — the exact magnitude described above as quiet and wrong.
The fix is to align each exported force to the index of the state it was
evaluated from, rather than to declare a floor and set G4.1's tolerance above
it. Declaring the floor would set the tolerance at precisely the level that
hides a real load-path defect. Guard the fix with G4.5, not with a tolerance.

A third risk is now visible in F3: mass reconciliation is a design loop rather
than a check. It is mitigated by freezing the mass for this window, and the
residual risk is that the frozen estimate is far enough off that the analysed
loads are not representative. G3.1b makes that visible rather than silent.

A third, non-schedule risk deserves naming: **tolerance drift**. The
characteristic failure mode when an automated executor is asked to make a
numerical test pass is to quietly widen the tolerance. The workflow in
`CLAUDE.md` addresses this structurally by keeping every tolerance in one
reviewed file.

## 9. Schedule

| Week | Dates | Milestone |
|---|---|---|
| 1 | Aug 10–16 | F0 complete incl. HSP tag; G1.0 audit and replay-determinism test |
| 2 | Aug 17–23 | F1 complete; F2 started |
| 3 | Aug 24–30 | F2 complete |
| 4 | Aug 31–Sep 6 | F3 complete |
| 5 | Sep 7–13 | F4 load mapping |
| 6 | Sep 14–20 | F4 complete; F5 complete |
| 7 | Sep 21–27 | F6 recovery and checks |
| 8 | Sep 28–Oct 4 | F6 complete; G7.1 cross-check |
