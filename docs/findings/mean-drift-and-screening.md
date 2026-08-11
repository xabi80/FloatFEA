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
   linearisation was taken about is not where the body is. At −1.19 m full scale
   and growing, this is not negligible against a 8.41 m diameter spar.

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
2. **A residual force-convention sign error.** The repository carries a
   post-mortem (`docs/post-mortems/m6-epilogue-wave-force-convention-bug.md`) and
   a branch `fix-make-regular-wave-force-convention`, so this class of error has
   occurred here before and been fixed at least once.

**Distinguishing them is one cheap experiment**: run the same case at two ramp
durations, or two initial phases. If the drift changes sign or magnitude, it is
mechanism 1. If it is invariant and downstream-negative, it is mechanism 2 and a
FloatSim defect.

This must be settled before drift is characterised any further — the two
mechanisms imply completely different treatments, and the screening consequences
in the previous section hold either way but their magnitude does not.

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

