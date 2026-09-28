# The radiation convolution's `k=0` endpoint replaced `B(ω)` with a near-constant dashpot

*(Earlier title: "adds damping worth ~6× `B(ω)`". Retitled under AJ1 — that
headline was a ratio with no operating point attached, which is the failure AJ2
names, in the title of the document reporting it. The `6×` is one point on a
curve spanning `0.23×` to `4606×`; the constant-dashpot statement holds
everywhere.)*

**For:** FloatSim / HSP — **this one does go upstream**
**From:** FloatFEA, G1.6 closure, 2026-08-25
**Status:** measured from the kernel alone, no simulation, then confirmed against
an exported record. One line of code.

---

## 1. What it is — a constant dashpot in place of a frequency-dependent B(ω)

**This is the framing that matters, and it is qualitative, not a magnitude.**

`dt·K(0)/2` does **not depend on ω**. `B(ω)` does, by orders of magnitude. So the
defect added a frequency-**independent** damping on top of a frequency-**dependent**
one, and wherever the constant dominates, the model no longer possessed the
property that radiation damping varies with frequency.

```
spurious  ||dt*K(0)/2||_F = 11.4464      CONSTANT at every omega
physical  ||B(w)||_F      = 3.86e-02 .. 3.50e+02   over 0.5 < w < 8

CROSSOVER (spurious == physical)   w = 2.8554 rad/s   T = 2.2005 s
platform operating point           w = 2.0004 rad/s   T = 3.1410 s   <- INSIDE, by 1.43x
```

The effective damping the solver actually applied:

```
  omega   T (s)    |B(w)|_F     |B+E|_F  spurious frac
 0.8000   7.854  1.1193e-01  1.1558e+01          99.0%
 1.2000   5.236  2.5507e-01  1.1702e+01          97.8%
 1.6000   3.927  5.9977e-01  1.2046e+01          95.0%
 2.0004   3.141  1.9667e+00  1.3413e+01          85.3%   <- operating point
 2.4000   2.618  5.0961e+00  1.6543e+01          69.2%
 2.8554   2.200  1.1446e+01  2.2893e+01          50.0%   <- crossover
 3.4000   1.848  2.4749e+01  3.6196e+01          31.6%
 6.0000   1.047  2.0006e+02  2.1150e+02           5.4%
```

**At the platform's operating point, 85.3% of the applied radiation damping was
spurious.** Below the crossover it is the majority of the damping, reaching 99%.

The decisive comparison is not any single ratio but how the two **vary**. From
ω=0.8 to ω=2.4:

| | variation across that range |
|---|---|
| physical `‖B(ω)‖_F` | **45.5×** |
| what the solver applied | **1.43×** |

> **Physics says the damping varies 45× across the operating band. The model
> varied it 1.4×.** That is a near-constant dashpot, not a radiation model.

### What this invalidates, beyond magnitudes

Anything that depended on radiation damping **varying with frequency** was
computed under a model that did not have that property:

- **mode selectivity** — which modes are damped and which ring;
- **relative damping between modes**, including the rotational mode's `Q ≈ 134`;
- the finding that the response is **radiation-damping-controlled rather than
  drag-controlled** (5× `Cd_n` moving `max‖θ‖` by 1.3%) — a near-constant dashpot
  85% larger than physical is a very good reason for drag not to matter, and it
  was not the physical one.

These are **suspended**, on the same footing as the drift work under AI3: not
disproven, but computed on a model that lacked a property they assumed.

### A note on the range figure

I measure the `‖B(ω)‖_F` span as **9059×** over `0.5 < ω < 8`, against the 278×
in the directive. The difference is almost certainly the band — over `2 < ω < 8`
it is 178×. **Which is exactly AJ2's point arriving unprompted:** a range quoted
without its band is the same failure as a ratio quoted without its operating
point. The band travels with the number above.

## 2. The arithmetic

`RadiationConvolution.evaluate()` is a plain rectangular sum:

```python
mu = self._dt * np.einsum("ijk,kj->i", self._K, self._buffer)
```

Weight `dt` on **every** lag, `k=0` included. The trapezoid rule weights the
endpoints `dt/2`, so the two differ by `dt·K[0]/2`.

`K(0)` is the largest value in the kernel — `K(0) = (2/π)∫B(ω)dω`, an integral
over the *whole* band, while `B(ω)` at any one frequency is a single sample of it.
So this endpoint is not a small correction:

```
||K[0]||_F                 2.2893e+03
dt*K[0]/2   (dt = 0.01)    1.1446e+01
||B_tab||_F at w=2.0004    1.9667e+00

the endpoint term alone is 5.82x the entire tabulated B
```

## 3. It accounts for the G1.6 residual, quantitatively

The effective transfer function is `H(ω) = B_eff(ω) + iω[A_eff(ω) − A_inf]`.
`dt·K[0]/2` is real and positive, so it adds to `B_eff` — and because
`iω(A−A_inf)` dominates, an addition to the real part shows up mostly as a
**phase rotation toward the real axis**, with a small gain increase.

Computed from the kernel with each quadrature, against the tabulated
coefficients — no simulation involved:

```
                            |H|/|H_tab|      arg        ||H-H_tab||_F/||H_tab||_F
trapezoid                      0.9889     -0.01 deg              0.0490
RECTANGULAR (the solver's)     1.0164    -12.67 deg              0.2258

measured on an exported record 1.0223    -11.07 deg              0.2085
```

**The prediction from the quadrature rule alone matches the measured residual** —
0.2258 against 0.2085, phase within 1.6°, gain within 0.6%. Trapezoid lands on
0.049, which is exactly the kernel's own approximation error measured
independently (AD2).

The G1.6 residual of 0.209 is this endpoint. Nothing else is left.

## 4. Why it matters more than a first-order quadrature error usually would

The error is `O(dt)` as a first-order rule implies, and its coefficient is
`K(0)/2`, which is large. Scaling is exact and linear:

```
dt = 0.01     excess  1.14e+01     5.8 x B_tab
dt = 0.005    excess  5.72e+00     2.9 x B_tab
dt = 0.001    excess  1.14e+00     0.58 x B_tab
```

**Even at a ten-times finer timestep the excess damping is still comparable to
`B` itself.** This is not a convergence problem that goes away at practical `dt`.

### It likely explains an unrelated FloatFEA measurement

FloatFEA measured the platform response as **radiation-damping-controlled, not
drag-controlled**: a **5×** change in the plate `Cd_n` moved `max‖θ‖` by **1.3%**,
where quadratic-drag-limited resonance predicts ~200%. That was recorded as an
open puzzle.

If the applied radiation damping is ~6× the BEM's, the puzzle resolves: the
response is held down by a quadrature artifact, and drag cannot compete with it.
**This is a hypothesis, not a measurement** — testing it means re-running the `Cd`
sweep with the endpoint halved.

## 5. The fix

Halve the `k=0` term (and the last lag, negligible). One line. It changes results,
so it is FloatSim's call and its regression baselines will move — which is the
point: they are currently baselined on the artifact.

## 6. What this does to FloatFEA's earlier note

`docs/findings/kernel-vs-tabulated-damping.md` claimed the applied damping differs
from the BEM's "by more than the size of `B`", then **withdrew** it when the
kernel transform came back faithful.

The withdrawal was correct on its evidence and wrong in its conclusion: the
transform was computed with **trapezoid** weights, which is not what the solver
does. The kernel is faithful; the *sum over it* is not. The original claim was
right, understated at "more than the size of `B`" when the true figure is ~6×, and
was withdrawn because the check used the wrong quadrature.

**Guard, seventh:** when checking a solver's numerics, reproduce the solver's own
discretisation — not the textbook rule for the same integral. A faithful kernel
and an unfaithful convolution over it are different findings, and only the second
one was ever applied to the platform.

---

## 7. AI2 — reconciling `6.73×` against `43.51×`

Two independent measurements of the pitch excess, 6.5× apart, both in permanent
records. Measured across every reduction of the *same* underlying quantity
(`dt·K(0)/2` against `B`) on the 12-buoy platform:

```
  omega   whole-F  pitchblk-F  pitch-diag   |B|_F
 1.0000     63.27     1340.87     4605.93   1.809e-01
 1.5000     25.09       86.49      289.29   4.561e-01
 2.0004      5.82       13.87       43.52   1.967e+00
 2.5000      1.84        3.91       10.69   6.218e+00
 3.0000      0.80        1.53        3.39   1.436e+01
 4.0000      0.23        0.39        0.71   5.023e+01
```

**The gap is the reduction.** FloatFEA's `43.51×` is the **mean pitch diagonal**
at ω=2.0004; FloatSim's figure is a **whole-matrix Frobenius**, which `9fb5b33`'s
own note states as "~7× ‖B‖ in Frobenius". At ω=2.0004 the two reductions differ
by **7.48×**, against the 6.5× to be explained. Neither measurement is wrong.

A **16% remainder** is left (`5.82×` here against `6.73×` there) and is almost
certainly configuration — 12-buoy against the 16-buoy `pin_vs_rigid` case — or a
slightly different ω. **That one point is worth confirming with FloatSim**; the
6.5× is settled without an exchange.

### The larger point: neither number means anything without its ω

The ratio spans **four orders of magnitude across the band** — `4606×` at ω=1.0,
`0.71×` at ω=4.0 — because `dt·K(0)/2` is a **constant** while `B(ω)` varies by
three orders. The excess is not large *because the defect is large at low
frequency*; it is large because **`B` is small there**.

> **Quoting "the pitch excess is 43×" without naming the reduction, the frequency
> and the configuration is quoting one point on a very steep curve.** Both figures
> in the record now carry all three.

This also sharpens §3: the defect is worst exactly where radiation damping is
weakest, which is where a lightly-damped resonance would otherwise live.
