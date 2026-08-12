# Mean surge drift — a finding for screening design, not a defect

**Measured:** 2026-08-10, from the committed cache
`studies/platform-12buoy/fin_study/timeseries/ts_0215_Cd5_H0p04_T3p141.npz`
(fin 0215, Cd_n = 5.0, H = 0.04 m, T = 3.141 s). No re-run required.
**Affects:** F5 screening design, G4.3/G4.6 hydrostatic linearisation.

---

## What was measured

The platform is drifting in surge while the study reports `settled=True`.

```
window returned            18.84 s = 6.00 periods
mean surge                 -0.02371 m   = 40% of the surge amplitude (0.0598 m)
mean sway                   0.00000 m
linear trend               -0.001266 m/s  =  -0.003976 m per wave period

cycle-mean surge, successive periods:
  -0.02061  -0.02170  -0.02288  -0.02420  -0.02566  -0.02723   (m)
```

The cycle means march monotonically and the increments *grow* (1.09, 1.18, 1.32,
1.46, 1.57 mm per period). This is an **active drift**, not a static offset.
Identical to five decimal places across all thirteen tracked bodies, so it is
rigid-body motion of the whole platform, not a relative effect.

**Magnitude — corrected, and the earlier figure was wrong by ~16x.**

An earlier version of this document recorded the drift as **−1.19 m full
scale**. That was the accumulated drift of the *cached 75.4 s case*, presented
as if it were the drift magnitude generally. `run_case` returns only the final
six periods, and the same truncation that made the second differences
inconclusive also truncated this figure.

```
terminal drift rate    1.27 mm/s model (our linear fit)
                       1.15 mm/s model (FloatSim, independent)
                    =  0.20 m per wave period, full scale

over the full 309.1 s integration   16 - 20 m full scale
                                 =  ~2.3 spar diameters (D = 8.41 m)
```

**Not 0.14 of a diameter — roughly two diameters.** The spread is whether you
integrate from t = 0 or from the end of the 20 s ramp; either way the conclusion
is the same and the regime is different from the one previously recorded.

**Cross-validation.** FloatSim's own instrumentation measured **1.153 mm/s**
model drift velocity; our independent measurement, from a different harness and
a different case, gives **1.266 mm/s** — **9.8% agreement**. Two independent
measurements on two harnesses agreeing to within 10% is the strongest evidence
in this investigation that the phenomenon is real and correctly characterised,
rather than an artifact of either measurement chain.

## Mechanism

Exactly as expected, and both halves are confirmed in the model:

1. **No restraint in surge, sway or yaw.** `_deck_with_drag()` returns
   `connections = 0` — no mooring, no catenaries. The sixteen `yaw_locked`
   joints constrain *relative* motion between bodies; nothing restrains the
   assembly as a whole. Hydrostatic `C` has no surge/sway/yaw restoring for a
   free-floating body.
2. **Morison drag is nonlinear.** `F ∝ u|u|` rectifies, producing a non-zero
   mean force over a wave cycle — with nothing to react it.

So the platform accelerates downstream until nothing stops it. Bounded only by
the run length.

## Why `settled=True` did not catch it

`run_case`'s settle criterion is **platform-heave amplitude** agreement between
consecutive windows (`platform_rao_pilot.py:281`). It is silent about mean
position, and about every other degree of freedom.

This is the second time that criterion has been narrower than it reads. The
envelope check (`docs/milestones/F1.md` §9) established steady state in
**rotation** — flat to 0.004% over the final cycles — and this measurement shows
mean **position** moving 3.2% per period over the same window. Both were true
simultaneously. "Settled" means one specific thing here, and it should be quoted
with its qualifier wherever it is relied on.

## Consequences for FloatFEA

**This is a finding for screening design, not a defect in FloatSim.** An
unmoored platform in waves drifts; that is physics. What it changes is how
screened snapshots may be compared.

1. **Snapshots at different mean positions are not strictly comparable.** Over a
   screening window spanning many periods, candidate snapshots sit at different
   mean offsets. An envelope built across them mixes load cases that differ by a
   rigid-body translation nobody declared. F5 must either screen within a window
   short enough that the mean is common, or record each snapshot's mean offset so
   the comparison is explicit.

2. **It degrades the hydrostatic linearisation across exactly the screening
   window.** Q1 and G4.6 lock buoyancy to the **mean wetted surface**, matching
   FloatSim's linearisation about ξ = 0. A mean position that moves means "the
   mean wetted surface" is itself a moving target, and the reference the
   linearisation was taken about is not where the body is.

   **This is not a perturbation, and that is a change of regime.** At ~19 m —
   **2.3 spar diameters** — by the end of the integration, the body is not near
   the configuration the linearisation was taken about; it is somewhere else.
   G4.6 locks buoyancy to the *mean* wetted surface to match FloatSim's
   linearisation about ξ = 0, and that match is what degrades. A reviewer who
   reads "the mean surface moves" without "by two spar diameters" will price it
   as negligible, and would be wrong by more than an order of magnitude.

   **Add an unvalidated band on top.** If the drift is tangential-plate-driven
   (below), its magnitude is unvalidated *by construction*: `Cd_t = 1.5` is the
   midpoint of a tank-pending [1, 2] range, so G4.6 and F5 inherit at least
   **±33%** on everything above.

3. **G4.1's residual inherits it.** A drifting rigid-body mode is precisely what
   inertia relief absorbs, so the residual should stay small — but the
   *inertia-relief multipliers* will carry the drift, and they are a diagnostic
   (`PLAN.md` §6 F4). They should be read with this in mind rather than as
   evidence of a load-path error.

## The drift is UPSTREAM, and that changes the diagnosis

An earlier draft of this document inferred from the −x drift that
`heading_deg = 0` must propagate along −x. **That inference was wrong, and
reading the source is what caught it.**

`waves/regular.py:56-59` and `excitation.py:50` both state that heading 0
propagates along **+X**. So the platform is drifting **upstream, against the
waves.**

Mean Morison drag rectification pushes *downstream*. Upstream drift is therefore
not explained by drag rectification, and the two candidate mechanisms are:

1. **Startup transient with zero restoring — the more likely.** The run applies
   `HalfCosineRamp(duration=20 s)`. With no surge stiffness whatever, *any* net
   impulse delivered during ramp-up leaves a **permanent velocity offset**,
   whose sign is set by the wave phase at ramp start rather than by the
   propagation direction. Nothing subsequently removes it: drag opposes the
   motion but the mean force balance is about a drifting state, not about zero.
   If this is the mechanism, the drift is a **startup artifact** whose magnitude
   and sign vary case by case with ramp duration and initial phase.
2. **A residual force-convention sign error, in the EXCITATION path only.** The repository carries a
   post-mortem (`docs/post-mortems/m6-epilogue-wave-force-convention-bug.md`) and
   a branch `fix-make-regular-wave-force-convention`, so this class of error has
   occurred here before and been fixed at least once.

### The ramp-to-period ratio shifts the prior — and is a full-scale trap

`ramp_s = 20.0 s` against `T = 3.141 s` is **6.4 periods**. Over that many
cycles the ramp's residual net impulse largely cancels, which argues *against*
mechanism 1 being large — the prior should sit nearer mechanism 2 than the bare
description suggests.

**But the ratio is what matters, not the 20 s.** At full scale `T = 23.03 s`,
and a ramp left at 20 s is **0.87 periods** — the impulse then barely cancels at
all and the startup transient becomes large. **The ramp duration must be
Froude-scaled with everything else**, to `20 × √50 = 141.4 s`, or the full-scale
re-run acquires a startup artifact the model-scale runs never had. This is a
concrete trap for the full-scale deck (F1 §3) and is recorded here because it
would otherwise be discovered as an unexplained drift difference between scales.

### The phase sweep settles it: NOT a startup artifact

Ran the identical case at initial phases 0/90/180/270° and phase-averaged.
Phase 0 reproduces the committed cache exactly (−0.02371 m), which validates the
harness before the other three points are read.

```
phase     mean surge      amp    mean/amp
    0       -0.02371   0.05981     -0.396
   90       -0.02449   0.06026     -0.406
  180       -0.02538   0.05898     -0.430
  270       -0.02460   0.05942     -0.414

phase-average           = -0.024548 m
spread across phases    =  0.000592 m   (2.4% of the mean)
|phase-avg| / |mean individual| = 1.000
```

**The drift is phase-independent.** A startup transient's sign is set by the
phase at ramp start and would average toward zero; this does not move at all.
**Mechanism 1 is eliminated.** The drift is sustained rectification.

### But "therefore a convention error" does not follow

The sweep's binary verdict rules mechanism 1 *out*; it does not establish that
the remainder is a defect. But **mechanism 2 is not eliminated either, and
nothing so far has tested it.**

> **A sub-argument in an earlier draft of this document was wrong and is
> struck.** It claimed that "a first-order excitation sign error cannot produce
> a mean force, because a harmonic force has zero mean". That is true of the
> excitation force *directly* and **false of the drift**. The drift comes from
> drag rectification, which depends on the **relative phase between body motion
> and fluid kinematics** — exactly what the depth-decay and clipping asymmetries
> sample. Flipping the excitation sign shifts body motion 180° against an
> unchanged fluid field, changing that correlation and potentially reversing the
> rectified force. Zero mean of its own; can still set the sign of someone
> else's.

What *has* been tested is narrower than it looked: **W1 tested the wave
kinematics sign** and **D3 tested the heading metadata**. **The BEM excitation
force sign convention itself — the subject of
`docs/post-mortems/m6-epilogue-wave-force-convention-bug.md` — is untested.**
That is now the leading candidate, not an excluded one.

A physically legitimate mechanism also remains in play. At this case the platform surges
**2.99× the fluid orbital amplitude**:

```
wave amplitude A                    0.0200 m      (H/2)
fluid orbital displacement at z=0   0.0200 m      = A, deep water
body surge amplitude                0.0598 m      -> 2.99x
fluid orbital velocity              0.0400 m/s
body surge velocity                 0.1196 m/s    -> 2.99x
```

So `u_rel = u_fluid − v_body` is **dominated by body motion, not by the wave** —
the platform is being dragged through relatively still water rather than pushed
by it. A pure sinusoid gives exactly zero mean for `u|u|`, so the mean force must
come from the couplings that break that symmetry: the exponential depth decay
`e^{kz}` sampled by a heaving and pitching body, and the MWL clipping documented
at `kinematics.py:16-22` (`z > 0` clamped to `z = 0`, which "overestimates
kinematics in the crest and underestimates in the trough" — an explicitly
asymmetric treatment). Both are real, both are documented Phase-1 modelling
choices, and both rectify.

**Status: sustained rectification confirmed, mechanism not yet identified.** It
is not a startup artifact. It is *not* excluded from being the excitation sign
convention, which remains untested.
Whether it is legitimate physics of the linear-Airy-plus-clipping model or a
defect deeper in the drag path is the open question, and it should not be
labelled a FloatSim defect until someone has separated those. The screening
consequences hold regardless, because they follow from the drift existing rather
than from its cause.

### DR3 / DR4 — first reading WITHDRAWN, and what the data actually says

```
case                    T      sparCd   mean surge   surge amp   max|theta|
baseline              3.141     1.2      -0.02371     0.05981     0.0378
DR3 off-resonance     2.500     1.2      +0.00158     0.02390     0.0131
DR4 half spar Cd      3.141     0.6      -0.04044     0.06161     0.0394
DR4 tenth spar Cd     3.141     0.12     -0.07681     0.06464     0.0422
```

**An earlier reading of this table is withdrawn in full.** It claimed the two
periods straddled the rotational mode and that Cd set the resonant response.
Both are false:

- **They do not straddle.** `T_rot = 3.257 s` is `omega = 1.9291 rad/s`;
  `T = 3.141 s` is `2.0004` and `T = 2.500 s` is `2.5133`. **Both sit above the
  mode, on the same side.** The 180-degree phase-sweep explanation cannot apply.
- **Reconciliation of 3.141 against 3.257.** The max||theta|| measurements (§9)
  used T = 3.257 s, *at* the mode, giving 0.159 rad. The drift work used
  T = 3.141 s to match the committed cache, where max||theta|| = 0.038 rad — four
  times smaller. **Every drift measurement was taken off the rotational mode.**
  Labelling T = 3.141 s "on-resonance" was wrong.
- **The response is not drag-limited.** A quadratic-drag-limited resonance gives
  response ~ `Cd^-0.5`: +41% at half Cd and +216% at a tenth. Observed: **+3.0%
  and +8.1%.** Morison drag is not what limits this response — radiation damping
  `B(omega)` most likely is, which would make the mode frequency-selective and
  Cd-insensitive at the same time.
- **The withdrawn explanation was quantitatively impossible.** Drift x1.7 from a
  +3.0% response change requires `drift ~ response^18`. No rectification
  mechanism scales that way.

**What the exponents say instead.** Fitting drift against spar Cd:

```
Cd x0.50 -> drift x1.706   exponent -0.770
Cd x0.10 -> drift x3.240   exponent -0.510
```

Signatures: drag as **driver** would give **+1.0**; a constant mean force braked
by **quadratic** damping gives **-0.5**; braked by **linear** damping, **-1.0**.
Observed -0.77 and -0.51.

> **Spar drag is the BRAKE, not the driver.** A genuine mean force exists
> elsewhere, and spar drag only limits the drift velocity it produces. The
> exponent sitting between -0.5 and -1.0 is mixed quadratic drag plus linear
> radiation damping — corroborating the response finding from entirely
> independent data.

### The plate drag is the source, and it sets the upstream sign

The Morison **inertia** term was the natural next hypothesis — MWL clipping and
`e^{kz}` bias fluid *acceleration* as well as velocity, so a `Cm` term would
rectify independently of `Cd`, exactly the shape the exponents require. **It does
not exist in this model.** `distributed_cylinder_drag` builds drag-only members,
and `driver.py:447-452` **raises** on `include_inertia=True`, forcing it `False`
at `:462`. `Cm` is not a knob here; the term is absent.

But the previous sweep varied only the **spar** Cd — the **plate** was held at
`Cd_n = 5.0` throughout. Within this model the only nonlinear terms are the two
drag families, so if the spar is the brake, the plate is the remaining candidate
driver. Sweeping it, with spar Cd fixed at 1.2:

```
plate Cd_n=5.00 Cd_t=1.50 -> mean surge -0.02371   amp 0.05981
plate Cd_n=2.50 Cd_t=0.75 -> mean surge -0.01482   amp 0.06028
plate Cd_n=0.50 Cd_t=0.15 -> mean surge +0.01327   amp 0.06533
```

**The drift passes through zero and reverses.** At a tenth of the plate drag it
is **+0.01327 m — downstream**, the direction drag rectification normally gives.

That is stronger evidence than a scaling exponent, and the exponent is in fact
meaningless once the sign changes. It shows **two competing mean-force
contributions of opposite sign**: one carried by the plate drag (upstream), one
independent of it (downstream). At the deck's `Cd_n = 5.0` the plate term
dominates and the platform drifts upstream.

**Limitation of this sweep, stated so it is not over-read.** It scaled `Cd_n`
and `Cd_t` **together**, so it localises the drift to the plate drag *as a whole*
and does **not** isolate which of the two plate terms drives it. Separating them
needs a `Cd_t`-only sweep — the natural knob, and unlike `Cm` it exists.

A prior reconciliation that fitted a scaling exponent across these points is
**void**: the sign flip means they are not points on one curve, so no exponent
can be fitted through them. Readings derived from that fit — including
"`Cd_n` is the brake" — are withdrawn. `Cd_n` is net-*driving*.

**The heave-plate drag model is what produces the upstream drift.** Two features
of that model make it the natural suspect, both already documented:

- The **tangential (edge-on) term is lumped at the disc centre**, not
  patch-resolved (`morison.py:589-595`) — flagged in the G1.0 audit as the one
  part of the plate load that is *not* distribution-resolved.
- `Cd_t = 1.5` is recorded at `platform_rao_pilot.py:104` as **"mid of the [1,2]
  tank-pending sensitivity"** — an unvalidated parameter awaiting tank data. If
  the tangential term is the driver, **the drift magnitude is unvalidated by
  construction**, carrying at least ±33% before any other uncertainty.

**Why the lumping is physically suspect, not merely inelegant.** Lumping a
*quadratic* load at the disc centre puts it exactly where the **rotational**
velocity contribution vanishes: the rim carries the pitch contribution, the
centre carries none. So the model runs at a rotational mode while discarding the
pitch contribution to the dominant damping surface's tangential drag. The drift
localising to precisely that term is not a coincidence worth betting against.

**This makes patch-resolving the tangential term the decisive experiment — and
it is required work regardless.** The G1.0 audit already flagged it as the one
part of the plate load that is not distribution-resolved, and FloatFEA needs it
distributed for the export. Sequencing the strip/patch export module first
resolves an open investigation as a side effect of scheduled work.

### N2 result — the TANGENTIAL term is NOT the driver; the NORMAL term is

`Cd_n` held at 5.0, `Cd_t` swept over a factor of ten, spar Cd fixed:

```
Cd_n=5.00  Cd_t=1.50 -> mean surge -0.02371   amp 0.05981
Cd_n=5.00  Cd_t=0.75 -> mean surge -0.02380   amp 0.05982
Cd_n=5.00  Cd_t=0.15 -> mean surge -0.02387   amp 0.05983
```

**A tenfold reduction in `Cd_t` moves the drift by 0.7%.** The tangential term is
not the driver.

Differencing against the earlier sweep, which scaled `Cd_n` and `Cd_t` *together*
and produced the sign reversal, the reversal is attributable to `Cd_n` alone:

> **The plate NORMAL (broadside) drag drives the upstream drift.**

*(Instrumentation note: the exponent column in this run's output is garbage —
the scaling denominator was not updated when the script was derived from the
previous sweep, so it divides by log(1.0). The mean-surge values are unaffected
and are what the conclusion rests on. Recorded rather than quietly dropped.)*

### Independently converged — the second time in this investigation

FloatSim's own force decomposition isolated the plate-**normal** term at
**−0.432 N** mean. Our `Cd_t` sweep reached the same conclusion by elimination —
a tenfold reduction in the tangential coefficient moving the drift by 0.7% —
from a different harness, by a different method, with no shared intermediate.

That is the **second independent convergence** here, after the drift-velocity
cross-validation (FloatSim 1.153 mm/s against our 1.266 mm/s, 9.8%).

Recorded deliberately: **two methods agreeing is stronger evidence than either
standing alone**, and in an investigation where several confident readings have
already been withdrawn, agreement reached without a shared path is the only kind
that carries weight. Both convergences should be cited whenever the drift
characterisation is relied on downstream.

### This inverts the sequencing rationale for the strip/patch module

The physical argument for expecting the tangential term — that lumping a
quadratic load at the disc centre discards the rotational contribution, since the
rim carries pitch and the centre carries none — was a good argument and it is
**not what the data says**. The driver is the **normal** term, which is *already*
patch-resolved by the polar quadrature (`_disc_patches`, `df_n` per patch at
`morison.py:583`). The lumped term is the one that does nothing here.

**Consequence: patch-resolving the tangential term will NOT resolve the drift.**
It remains required work — the G1.0 audit flagged it as the one part of the plate
load that is not distribution-resolved, and FloatFEA needs it distributed for the
export — but it must not be scheduled on the expectation that it settles this
investigation as a side effect. That rationale is withdrawn; the export
justification stands on its own.

### Candidate mechanism for a normal term producing horizontal drift

The plate normal is `+z` in the body frame, so its drag responds to the *normal*
component of relative velocity — largely heave. A horizontal mean force arises
because `f_normal = n_hat * Σ df_n` with `n_hat = R · n_hat_body`
(`morison.py:568-580`): **when the body pitches, `n_hat` tilts away from vertical
and the normal force acquires a horizontal component.** The magnitude is
quadratic in the normal relative velocity, so the product of a quadratic
heave-driven magnitude with an oscillating pitch tilt rectifies into a mean
horizontal force.

This depends on the **correlation between heave velocity and pitch angle** — a
phase relationship, therefore response-dependent, which is consistent with the
off-resonance collapse and sign change already measured. It is a testable
prediction rather than a restatement: it implies the drift should track the
heave-pitch phase, and should be insensitive to `Cd_t` — which is what was just
observed.

### C2 — the mechanism is confirmed in FORM; its magnitude is not reconciled

Re-evaluated `plate_element_force` offline over the stored history, using
FloatSim's own code rather than a reimplementation, and formed the first-order
prediction alongside the full force:

```
samples                                1885   (t = 56.56 to 75.40 s)
mean plate horizontal force, 12 buoys      -0.079995 N
mean of n_hat_x * f_n, 12 buoys            -0.080336 N
peak-to-peak plate horizontal force         0.509298 N
rms pitch angle, buoy 0                     0.02385096 rad
```

**The first-order decomposition reproduces the full plate horizontal force to
0.4%.** That is the C2 test, and it passes: the mean horizontal force *is*
`<n_hat_x · f_n>`, i.e. the quadratic normal force projected through the
pitch-tilted normal. The rectification is **first order in theta**, not second.

Two consequences follow, and neither depends on the magnitude:

- **It is leading-order**, so it appears in *any* model that tilts a plate normal
  with pitch and uses quadratic drag. It is not a numerical artifact of this
  implementation, and it will not go away with mesh or timestep refinement.
- **All three `xi[3:6]` interpretations agree to first order**, so the
  representation ambiguity perturbs this only at second order (~0.4%). The
  mechanism is **representation-insensitive** — it can be neither blamed on nor
  fixed by the interpretation split.

**The magnitude does NOT reconcile, and the comparison as run is invalid.**
−0.080 N against FloatSim's reported −0.432 N is a factor of 5.4. The leading
explanation is in this script's own setup: it evaluated with
**`fluid_velocity = 0`, i.e. calm water**. The plate sits 1.4574 m below the
waterline, where `e^{kz}` at `k = omega^2/g = 0.4078 /m` gives **0.552** — the
orbital velocity there is 55% of its surface value, not negligible. Omitting it
changes the relative velocity that the quadratic term acts on.

So the −0.432 N comparison is **not** evidence of disagreement; it is a
comparison between two different quantities. Recorded that way rather than as a
5.4x discrepancy, which would be a false finding. Closing it needs the offline
evaluation repeated with wave kinematics at the plate depth — cheap, since the
history is now persisted (`c2_history.npz`) and no re-simulation is required.

**Status: mechanism established, magnitude open.** The form is confirmed by
measurement rather than plausibility, which was C2's purpose. The remaining gap
is a known omission in the check, not an unexplained result.

**Overall status: driver isolated, mechanism established in form, magnitude open.** It is not a startup artifact
(phase sweep), not the wave kinematics sign (W1), not the heading metadata (D3),
and not spar-drag rectification (spar Cd is the brake). It is carried by the
plate **normal** drag term specifically (N2). Whether that is legitimate model physics or a defect in the
lumped tangential treatment is the remaining question — and **the excitation
sign convention is still formally untested**, which is DR2's job.

### The three discriminating experiments

**DR2 — closed-form frequency-domain response.** Same pattern as the `mu`
identity, and the data is already held. Solve the constrained response at the
fundamental from `A(ω)`, `B(ω)`, `C` and Capytaine's excitation force, then
compare against time-domain surge in **amplitude and phase**. A response 180°
off the frequency-domain prediction isolates the sign error directly. It also
independently cross-validates the 2.99× amplification.

**DR3 — does the off-resonance case drift?** A free body has no surge restoring
and therefore no surge resonance, so the 2.99× surge amplification is almost
certainly the **rotational mode's horizontal component** at Q ≈ 134. If the
drift is response-driven rectification it should largely collapse off-resonance;
a convention error drifts regardless. The T = 2.5 s case (max‖θ‖ = 0.039 rad,
0.39× the bound) is the natural comparison.

**DR4 — run, and it inverted its own premise.** It was meant to show whether
the drift was drag-mediated. It showed the opposite of the assumed sign: drag is
the brake, and the driver is the plate term. Recorded above.

## Wave kinematics sign — checked independently of the heading metadata, and CLEAN

The heading check (D3) confirmed the *metadata*: FloatSim's wave module and
Capytaine's reader agree that heading 0 is +X. It did **not** confirm that
`u_fluid` carries the sign that heading claims — excitation (a BEM force) and
Morison drag (`u_fluid` sampled at a position) are separate code paths, and a
sign error in horizontal orbital velocity would rectify drag in −X while
excitation still acted +X. That is exactly what is observed, and it would have
survived D3.

**Checked, and it is correct.** For a wave travelling +X the horizontal orbital
velocity is in phase with elevation, so `u_x` under a crest must be positive.
Evaluated directly from `airy_velocity` at heading 0, A = 1, ω = 2:

```
t = 0 (crest)   eta = +1.0000   u_x = +2.0000 = +A*omega
u_x over a cycle:  +2.000  +1.414   0.000  -2.000  -0.000   =  A*omega*cos(omega t)
```

In phase with elevation, positive under the crest. **This candidate is
eliminated**, and with it the only mechanism that explained a *sustained* −X
drift while D3 passed. Mechanism 1 gives a constant velocity offset, not
sustained rectification — so if the phase sweep does not collapse the drift, the
remaining explanation is confined to the excitation force path.

## The drag hypothesis is disproved

The proposal that the drag term might drop or linearise away the mean relative
velocity — leaving nothing to arrest the drift — **is false.**
`morison.py:_body_velocity_at` returns `v_ref + ω × arm` with
`v_ref = xi_dot_body[0:3]`, the *full* inertial translational velocity of the
reference point, mean component included. `morison_element_force` then forms
`u_rel = u_fluid − v_body` with `u_fluid` sampled at the body's **drifted**
position. Nothing is dropped and nothing is linearised. The arresting mechanism
is present and correct.

## Second differences: inconclusive, and the window is why

The stored record returns only the final 6 periods (`run_case` returns one
`window_periods` window). A one-period moving average isolates the slow
component over 15.7 s, and it does not support an asymptote fit:

```
slow displacement  -0.02066 -> -0.02723 m
slow velocity      +0.000690 -> -0.000560 m/s     (not monotonic)
d|v|/dt            +0.000002 m/s2                 (at the leakage floor)
```

Fitting `dv/dt = a0 + c2 v²` — the saturating quadratic-drag signature — returns
`a0 < 0, c2 > 0`, which is not that signature. But the moving-average leakage
from the incommensurate period (314.1 samples binned at 314) is of the same
order as the slow velocity itself, so **the estimator is at its noise floor and
the result is inconclusive rather than negative.**

The mean displacement moved 32% over five periods, which is far larger than any
leak and is real. Everything beyond that fact needs a longer record than the
stored window contains.

