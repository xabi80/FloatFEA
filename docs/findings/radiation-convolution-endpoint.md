# The radiation convolution's `k=0` endpoint adds damping worth ~6× `B(ω)`

**For:** FloatSim / HSP — **this one does go upstream**
**From:** FloatFEA, G1.6 closure, 2026-08-25
**Status:** measured from the kernel alone, no simulation, then confirmed against
an exported record. One line of code.

---

## 1. What it is

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

## 2. It accounts for the G1.6 residual, quantitatively

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

## 3. Why it matters more than a first-order quadrature error usually would

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

## 4. The fix

Halve the `k=0` term (and the last lag, negligible). One line. It changes results,
so it is FloatSim's call and its regression baselines will move — which is the
point: they are currently baselined on the artifact.

## 5. What this does to FloatFEA's earlier note

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
