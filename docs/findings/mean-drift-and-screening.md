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

At full scale: mean offset **−1.19 m** and growing at **≈0.0090 m/s**, i.e.
**0.20 m per wave period**.

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
   linearisation was taken about is not where the body is. **Magnitude, not just
   mechanism: −1.19 m is 14% of a spar diameter (8.41 m), reaching 38% after ten
   more wave periods.** G4.6's write-up must carry that number, not only the
   mechanism — a reviewer who reads "the mean surface moves" without "by 14% of a
   diameter and rising" will price it as negligible.

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

### DR3 and DR4 results — the drift is response-driven

```
case                        T      sparCd   mean surge   surge amp   max|theta|
baseline                  3.141     1.2      -0.02371     0.05981     0.0378
DR3 off-resonance         2.500     1.2      +0.00158     0.02390     0.0131
DR4 half Cd               3.141     0.6      -0.04044     0.06161     0.0394
DR4 tenth Cd              3.141     0.12     -0.07681     0.06464     0.0422
```

**DR3 — it collapses AND reverses sign.** Off-resonance the drift is
**+0.00158 m, i.e. DOWNSTREAM** and 15× smaller; on-resonance it is −0.02371 m,
upstream. Ratio off/on = −0.067.

That reversal is the most informative number in the set. **A fixed excitation
sign error is not amplitude-dependent** — it would shift phase by 180° at every
frequency and flip the drift sign everywhere, not between one period and
another. What *does* reverse across these two cases is the **response phase**:
T = 3.141 s and T = 2.500 s straddle the rotational mode at T_rot = 3.257 s, and
response phase relative to excitation sweeps through ~180° across a resonance.
The rectified mean depends on exactly that relative phase, so it flips. This is
ordinary resonant behaviour, not a convention.

The amplitude ratio tracks it: off-resonance the body surges 0.0239 m against a
0.0200 m fluid orbit (**1.2×**, comparable, drift downstream as drag
rectification normally gives); on-resonance 0.0598 m against 0.0200 m
(**2.99×**, body-dominated, drift upstream).

**DR4 — the drift scales INVERSELY with Cd, and the experiment is confounded.**
Halving spar Cd multiplies the drift by 1.7×; reducing it to a tenth multiplies
it by 3.2×. Not the "scales with Cd" signature at all.

The reason is visible in the same table: **Cd also sets the resonant response.**
Lower Cd → less damping → larger response (surge amp 0.0598 → 0.0646, max‖θ‖
0.0378 → 0.0422) → stronger rectification. The two effects oppose, and the
response effect wins.

So DR4 is weaker than "necessary but not sufficient" — as designed it **cannot
discriminate**, because Cd is not an independent knob. What it does establish is
that drag is *involved* (changing Cd changes the drift substantially) and that
the drift is **response-driven rather than directly Cd-driven**, which is the
same conclusion DR3 reaches by a different route.

**Weight of evidence: legitimate physics, not a convention error.** Both
experiments show the drift tracking response amplitude and phase. Recorded as a
finding about the model's nonlinear behaviour near resonance.

**DR2 remains worth running** — it would confirm the time-domain response phase
matches the frequency-domain prediction and close the loop directly, rather than
by inference from two sign observations. It is the only test that isolates the
excitation sign convention, which is still formally untested.

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

**DR4 — Cd sweep, with its limit stated.** It establishes that the drift is
**drag-mediated**, not that the phase driving the drag is correct. Scaling with
Cd is consistent with legitimate rectification *and* with a phase error feeding
the same drag term. **Necessary, not sufficient** — and it must not be reported
as though it settled the question.

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

