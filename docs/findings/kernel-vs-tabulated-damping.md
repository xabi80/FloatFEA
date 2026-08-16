# The retardation kernel's damping differs materially from the tabulated `B(ω)`

**For:** FloatSim / HSP
**From:** FloatFEA, G1.6 first pass, 2026-08-15
**Status:** measured at one frequency on one case. **Not a defect claim** — see
§4 — but an unexamined dependency on a quantity now measured to be approximate.

---

## 1. What was measured

Comparing the exported `mu` against a frequency-domain prediction built from the
**tabulated** `A(ω)`, `B(ω)`, at the case frequency, on the 12-buoy platform:

```
magnitude-weighted |R-T|/|T| = 0.2085
magnitude-weighted |R|/|T|   = 1.0223
```

A **purely quadrature** missing term predicts `|R-T|/|T| = sqrt(|R|/|T|² - 1)`:

```
sqrt(1.0223² - 1) = 0.2124    observed 0.2085    agreement 1.85%
```

That is a **fit**, not an inequality. A pure phase rotation would instead give
`|R|/|T| = 1` exactly, and the rotation implied by 0.209 would be **12.0°** —
which no convention produces. So the discrepancy is a missing term, in
quadrature, at 21% of `|mu|`.

## 2. The quadrature direction identifies which term, independently

In `F_rad = A(ω)·ξ̈ + B(ω)·ξ̇` the two terms are **90° apart**. With `A`
dominating, an error in `B` lands **exactly in quadrature** — which is where the
discrepancy is. Two independent lines of evidence, from the same two numbers.

And the kernel is what carries `B`: `K(t)` and `B(ω)` are a Fourier pair, so a
truncated, resampled kernel is precisely an approximation of `B`.

## 3. The size, relative to `B` itself

This is the number that matters, and it is larger than "21%" suggests:

```
max |[A - A_inf]·ξ̈|  = 4.689e-01
max |B·ξ̇|            = 5.043e-02      (10.3% of |mu|)
max |mu|             = 4.884e-01

quadrature discrepancy = 0.2124 × |mu| = 1.037e-01
   as a fraction of the B term         = 206%
```

**The quadrature discrepancy is roughly twice the entire tabulated `B`
contribution.** `B` is small relative to `A` here, so a 21% error on the total is
a large error on the damping specifically.

Sources, each individually small: truncation at **60 s** (6001 lags), a
**79-point** ω grid with contaminated slices excluded, and a **left-endpoint**
convolution sum whose convergence to the continuous result FloatFEA measured at
**first order** in `dt`.

## 4. Why this is not a defect claim

The kernel is a legitimate, documented approximation, and **`mu` is exactly what
the solver applied** — verified bit-identical against an instrumented run. The
simulation is self-consistent. Nothing here says a FloatSim result is wrong.

What it says is that **the damping actually applied is the kernel's, not the
BEM's**, and the two differ by more than the size of `B`.

## 5. Why it matters beyond the gate

FloatFEA's earlier measurement established that the platform response is
**radiation-damping-controlled, not drag-controlled**: a **5×** change in the
plate `Cd_n` moved `max‖θ‖` by **1.3%**, where quadratic-drag-limited resonance
would have predicted ~200%. Something other than drag limits that response, and
radiation damping is the candidate.

If the damping controlling the response is the kernel's rather than the BEM's,
then **response amplitudes inherit the kernel's error** — including
**`max‖θ‖ = 8.97°`**, which is the number FloatFEA's Q2 (rotation validity) turns
on, and which was measured at 1.6× the stated small-angle bound.

Not necessarily large in effect. But it is a dependency nobody was looking for,
on a quantity now measured to be approximate at the 200%-of-`B` level.

## 6. Caveats, stated plainly

- **One frequency, one case.** The measurement is at `ω = 2.0004 rad/s` on the
  12-buoy platform. The error is frequency-dependent by construction — truncation
  bites hardest where `K(t)` has not decayed.
- **The attribution to `B` is inference.** The quadrature *direction* is
  consistent with a `B` error given `A` dominance; another quadrature-direction
  error would look identical.
- **"206% of `B`" is a ratio to a small number.** It is 21% of the total
  radiation force, which is the figure to quote for effect size.

## 7. Cheapest next step

Compare the kernel's own `B_eff(ω)` — recovered by transforming `K(t)` back —
against the tabulated `B(ω)` across the swept grid. That is a direct measurement
of the approximation, needs no simulation, and would show whether the error is
localised in frequency or broad. FloatFEA cannot do it authoritatively because
the kernel construction is FloatSim's.
