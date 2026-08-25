# The retardation kernel reproduces BOTH tabulated channels; it is not the source of the G1.6 residual

**For:** FloatSim / HSP
**From:** FloatFEA, G1.6, 2026-08-15, **superseded 2026-08-25**
**Status:** **the upstream claim is WITHDRAWN.** Both channels of the kernel are
now measured directly against the tabulated coefficients, and both are faithful.
Retained because the *route* to the withdrawn claim is the finding.

---

## -2. THE KERNEL IS EXONERATED IN BOTH CHANNELS (AD1, AD2)

### AD1 — the bridge that generated this whole document is invalid

Everything from §-1 down rests on one inferential step: *the residual is purely
quadrature, therefore the error is in `B`*. That step assumes an **uncoupled**
system. In general

```
mu_j = -w^2 * sum_k (A - A_inf)_jk X_k   -   i w * sum_k B_jk X_k
```

and the two sums run over **different matrices**, so they carry different complex
phases. The 90° separation the bridge needs holds only when
`arg(sum A_jk X_k) == arg(sum B_jk X_k)` — exact for a single uncoupled DOF,
false in general. Measured: **+90.0° exactly** for one uncoupled DOF, versus
**+3.2°, −178.4°, −3.7°, −44.8°** on coupled trials. With **96.8% of `B`'s energy
off-diagonal**, the failure is severe.

**Consequence:** the residual (a measurement) and the kernel transform (a
measurement) **both stand**. The 2.09× and the 42–56× "contradiction" were
manufactured by the inference sitting between them. **There was never a `dB` to
explain**, and no seventh mechanism is needed. §-1 below is superseded entire.

### AD2 — the A channel, measured rather than inferred

AA1 held that a purely quadrature residual *is* the statement that `A` is
faithful, so the sine transform need not be run. AD1 removes that argument's
foundation, so `A` is measured the same way `B` was — from the other half of the
same Ogilvie pair, needing no simulation:

```
B(w) =        integral K(t) cos(w t) dt
A(w) = A_inf - integral K(t) sin(w t) dt / w
```

At the case frequency `ω = 2.0004 rad/s`, Frobenius over the full 72×72:

```
||A_tab - A_inf||_F   2.5957e+01     <- the quantity mu actually multiplies
||A_eff - A_tab||_F   1.2731e+00     ratio  0.0490
||B_tab||_F           1.9667e+00
||B_eff - B_tab||_F   3.9915e-02     ratio  0.0203

dominant diagonals, (A_eff-A_inf)/(A_tab-A_inf):  0.982 .. 0.990
median over 37 in-band frequencies:  dA 0.0507   dB 0.0258
```

`dB/B` reaches 1.09 at the low end, but `|B|_F` is `4.7e-02` there against
`1.4e+02` at ω=5.3 — negligible in absolute terms, the same pattern the earlier
diagonal comparison showed.

**How much of the 20.9% residual can the kernel account for?** Since
`||dA·x|| <= ||dA||_F·||x||`, these ratios bound it:

```
A-term share of |mu|   4.689e-01 / 4.884e-01 = 96.0%   x 0.0490 = 4.71%
B-term share of |mu|   5.043e-02 / 4.884e-01 = 10.3%   x 0.0203 = 0.21%
                                            bound on kernel error  ~4.9% of |mu|
                                                 observed residual  20.9% of |mu|
```

**At most about a quarter, and that is an upper bound assuming worst-case
alignment.** The kernel is faithful in both channels and cannot be the source.
This is the first time the quantity has been *bounded* rather than inferred.

**Withdrawn upstream:** the §5 claim that response amplitudes — including
`max‖θ‖ = 8.97°` — inherit a kernel damping error at the "200%-of-`B`" level.
`dB/B = 0.020`. Nothing goes to FloatSim on this.

**Still open:** the residual itself. AD3 (broadband spectral) is the remaining
candidate and the one never tested.

---

## -1. SUPERSEDED BY AD1 — the "contradiction" was an artifact of the bridge

> Retained verbatim to show what was inferred. AD1 shows the 2.79× and the
> kernel transform were never in conflict; the inference between them was.

Two measurements of the same quantity disagree by ~56×, and both cannot be right:

```
residual decomposition (same denominator, AA3)  dB = 2.79 x B_tab
kernel transform, full 72x72 (Frobenius)        dB < 0.05 x B_tab
```

**AA3: not a denominator artifact.** Recomputed per-DOF at the fundamental on a
common basis, `|Bterm|/|T| = 0.0986` against the earlier global-max `0.1032` —
the two reductions agree, so the 2.09 (now 2.79) factor is real arithmetic, not a
mismatched ratio. The AA3 suspicion was reasonable given precedent but does not
hold here.

**AA1 accepted: the A channel needs no test.** A purely quadrature residual *is*
the statement that `A` is faithful — the in-phase component works out to 0.07% of
the A-share. The sine transform would confirm what the data already says, and is
not run.

**AA4 is structurally unavailable on this record.** At a *single* frequency
`ξ̈ = iω·ξ̇` in phasor terms, so `dA` and `dB` are **perfectly confounded** — no
regression can separate them. The attempted fit returns `dB/B_tab` of 46.9, 44.6,
39.2 and 6233 across DOF: not a measurement, a degenerate fit. It is also
misspecified per-DOF, since `dA` and `dB` are 72×72 matrices and off-diagonal
energy is 96.8% of `B_tab`. The in-phase/quadrature split is the *only*
separation single-frequency data admits, and the phasor method already performs
it. A third independent measurement needs **multi-frequency** data.

### The resolution that fits every measurement

The identity `mu = [A(ω)−A_inf]·ξ̈ + B(ω)·ξ̇` holds for a sinusoid extending back
to `t = −∞`. `mu(t)` convolves **60 s of history** — the full kernel memory —
whereas every check that excluded a transient (V1, W1) operated on an **8-cycle,
25 s comparison window**.

Those are different windows, and the response amplitude is *not* stationary over
the longer one: the envelope was measured falling ×0.90 across 100 s. The
convolution weights that varying history, so `mu` cannot equal a steady-state
prediction built from a single instantaneous amplitude — while the kernel itself
remains faithful, `A` remains faithful, and `B` remains faithful.

**This reconciles all three measurements** rather than refuting a fourth
mechanism. It is a property of the comparison window, not of FloatSim.

**Test:** repeat on a record stationary over a full 60 s kernel memory — which
the ~84-cycle re-run (W3) provides anyway. If the residual collapses, closed.

---

## 0. HEADLINE CORRECTION — the direct measurement refutes the inference

**Everything below §1 was written from an inference. The direct measurement
contradicts it, and the inference is withdrawn.**

`B(ω) = ∫ K(t) cos(ωt) dt`, and the kernel actually used is in hand, so
`B_eff(ω)` is directly computable — no simulation, no argument. Doing it:

```
hydro[40] = g52   w=2.0004   B_tab 3.072e-02   B_eff 3.229e-02   ratio 1.051
hydro[46] = g58   w=2.0004   B_tab 2.928e-02   B_eff 3.053e-02   ratio 1.043
hydro[ 2] = g2    w=2.0004   B_tab 1.962e-02   B_eff 1.961e-02   ratio 1.000

frequency-resolved, median ratio across 0.5 < w < 8:  1.003
  w > 2:   1.000 - 1.005   (excellent)
  w < 1.5: wild ratios, but B_tab is 1e-6..1e-4 there -- negligible absolutely
```

**The kernel reproduces the tabulated diagonal damping to within 5% at the case
frequency, and to 0.3% in the median across the band.** Neither proposed branch
survives: it is not `+3.09 B_tab`, and it is not `-1.09 B_tab`. There is no
factor of three and no sign reversal.

**So the 206%-of-`B` figure cannot be attributed to a diagonal `B` error.** The
residual itself is real and purely quadrature — that part stands — but its origin
is not what §2–§3 infer. The remaining candidate is the **off-diagonal** kernel:
the comparison above is diagonal-only, while `mu` is a full 72×72 matrix–vector
product, and the database is a genuine multi-body solve with cross-body coupling
already measured at 2.7% of own-body added mass.

**Nothing goes upstream on the strength of §2–§3.** They are retained below only
to show what was inferred and how the measurement overturned it.

### An indexing error, caught in the same step

The first run of this comparison indexed the **102-DOF global** kernel with a
**72-DOF hydro-subset** index and compared it against `B_tab[j,j]` — two
conventions inside one comparison. It put global DOF 46, which lies in hub2 and
is *structural*, opposite a hydro DOF, and returned `B_eff = 0.000000e+00` with
ratio 0.000. Read uncritically, that would have looked like a spectacular
confirmation of "the kernel destroys the damping".

The 72-vs-102 trap is one this project has already recorded twice
(`docs/conventions.md` § Numbering, and the L1 radiation-DOF correction). It bit
anyway, in the script written to resolve the question it bears on.

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
