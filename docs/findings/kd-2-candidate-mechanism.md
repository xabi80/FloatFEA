# KD-2 — candidate mechanism, with the magnitude that rules it out at buoy scale

**For:** whoever owns KD-2-revised in `docs/openfast-cross-check-report.md` (HSP)
**From:** FloatFEA F0 audit, 2026-08-10
**Status:** hypothesis with its magnitude analysis attached. **The class matches;
the magnitude at buoy scale does not, by 277×.**

---

## Why this document exists

FloatFEA's F0 audit found a CoG/reference-point defect in the FloatSim deck. It
is the same *class* of defect KD-2 is attributed to — "combined-deck
mass-aggregation discrepancy". Handing that over as a bare hypothesis would be
worse than useless, because the found defect is real but **two orders of
magnitude too small**, and the predictable failure mode is that someone confirms
the 0.16%, records it as a partial explanation, and stops looking.

So the magnitude analysis travels with the hypothesis, and the useful output is
not the defect — it is the **lever length the mechanism would need**, which
points somewhere specific.

## What KD-2 requires

FloatSim pitch natural period 32.34 s against OpenFAST 26.83 s.

```
period ratio      32.34 / 26.83  = 1.2054        (+20.54%)
T = 2*pi*sqrt(I/K)  =>  the discrepancy is a factor 1.4530 in I/K
```

**That 1.4530 can sit in either term**, and this is the first thing to settle:

| branch | required error |
|---|---|
| inertia high | **I high by +45.3%** |
| stiffness low | **K low by −31.2%** |

"Mass-aggregation" is the *attributed* cause, and **the attribution may itself be
the error.** The pitch restoring `K` depends on `KG` through the `−m·g·z_G` term
(`floatsim/hydro/hydrostatics.py`), and the platform carries a **placeholder**
structural mass (C4-c, "10 kg platform", flagged as an assumption in
`platform-geometry.md`) which sets `KG`. A placeholder mass in the restoring
term is at least as plausible a source as an inertia error, and nothing in the
current record discriminates between them. **Settle which branch before hunting
in either.**

## What the found defect delivers

The buoy body reference point and the CoG are not coincident, and FloatSim
assumes they are (`driver.py:222` passes `cog_offset_body=None`; `driver.py:208-209`
records that the deck has no CoG-offset field).

```
m = 28.67 kg          I_xx = 24.0 kg.m2
d = Z_BUOY_REF - CoG_global = -1.1956674 - (-1.23268) = +0.03701 m   (37.0 mm)

omitted parallel-axis term      m*d^2 / I        = 0.164%
coupling ratio                  m*d / sqrt(m*I)  = 4.05%
coupling, second order          eps^2            = 0.164%
```

The 4.05% coupling ratio is the eye-catching number and it is **not** the one
that matters here. It enters the pitch period at second order — `eps^2` = 0.164%
— and would only amplify if surge and pitch were near-degenerate in frequency.
**On a spar they are not**, by a wide margin: that separation is the defining
property of the hull form.

So both available terms deliver **~0.16%** against a required **45.3%**.

## The lead: same defect class, deck scale

Inverting the mechanism gives the useful result. To produce KD-2 by this
mechanism at this mass:

```
required   m*d^2 = 0.4530 * I = 10.87 kg.m2
           d_need = sqrt(10.87 / 28.67) = 0.6157 m   MODEL SCALE
                                        = 30.8 m     FULL SCALE

found      d      = 0.03701 m
ratio             = 16.6x in LENGTH,  277x in EFFECT
```

**30.8 m full scale is a plausible deck-to-waterline distance.** The search
target is therefore **the same defect class at deck scale, where the lever is
metres rather than millimetres** — a combined-deck aggregation in which a
superstructure or deck mass is referenced to the wrong point, not the buoy-level
37 mm offset found here.

That is a much better-posed search than "look for a mass-aggregation error",
because it comes with a length scale: any candidate whose lever is not of order
tens of metres full scale cannot produce KD-2, whatever else is wrong with it.

## What FloatFEA does about it meanwhile

Nothing that depends on KD-2 being resolved. The deviation is recorded in
`floatfea/hsp_pin.py` and inherited by every FE result computed from tag
`floatfea-ref-1`, and it is named on the face of any report rather than left to
be discovered downstream.

The buoy-scale offset is handled separately and on its own merits: the `.flr`
record must declare the inertia tensor's reference point, and the validator
rejects a record that omits it. **G3.1a cannot catch a wrong reference point**,
because FloatFEA would compute its own tensor about its own point and be
internally consistent — both sides consistently wrong. See `docs/conventions.md`
§ Body frames.

## Reproducing every number here

```
python - <<'PY'
import sys; sys.path.insert(0,'studies/cluster-3buoy-rigid')
sys.path.insert(0,'studies/platform-12buoy')
import cluster_common as cc, platform_common as pc
r = 32.34/26.83
m, I = cc.M_BUOY, cc.I_XX_BUOY
d = pc.Z_BUOY_REF - (cc.CoG_Z_SINGLE - pc.PLATFORM_DZ)
print(f"I high by {100*(r*r-1):+.1f}%  or  K low by {100*(1-1/r/r):+.1f}%")
print(f"m d^2/I = {100*m*d*d/I:.3f}%   eps^2 = {100*(m*d/(m*I)**.5)**2:.3f}%")
print(f"d_need  = {((r*r-1)*I/m)**.5:.4f} m model = {((r*r-1)*I/m)**.5*50:.1f} m full")
PY
```

Run from the HSP repository root at tag `floatfea-ref-1`.
