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

## Incidental evidence on an UNRESOLVED convention

Mean drift under Morison drag is in the **wave propagation direction**. The
measured drift is in **−x**, which is evidence that `heading_deg = 0` propagates
along **−x**.

Recorded as evidence, **not** as settled. `docs/conventions.md` leaves the
heading-zero direction UNRESOLVED pending a reading of
`floatsim/waves/regular.py` and `make_regular_wave_force`, and that reading is
still the thing that closes it. A single inference from a drift sign is a good
lead and a poor convention.
