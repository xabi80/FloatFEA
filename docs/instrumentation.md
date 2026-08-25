# Instrumentation practice for scratch diagnostics

**Status:** adopted 2026-08-11, from three defects that shared a shape.

---

## The pattern

Three instrumentation defects occurred during the F1 drift investigation. All
three were caught, and all three were caught by *us*, which is the system
working. But three points is a pattern rather than three accidents:

| defect | where |
|---|---|
| `pk[-6]` reached a partial first window in a six-element series | growth **rate** |
| `"+11.10% STILL GROWING"` contradicting its own flat table | growth **percentage** |
| `log(1.0)` denominator after a script was derived by `sed` | scaling **exponent** |

**Every one was in a derived column. The primary measurements were sound every
time.** Mean surge, per-cycle peaks and per-case forces were correct in all three
runs; only the ratios, percentages and exponents computed *from* them were wrong.

That asymmetry is not luck. A raw measurement is a number the code obtained
directly and that a reader can sanity-check against physical intuition. A derived
ratio hides its denominator, its window, and its sign convention inside an
expression nobody reads once the script has printed something plausible — and a
plausible derived number is *more* dangerous than a wrong raw one, because it
arrives pre-interpreted.

## The rule

**Scratch diagnostics print raw quantities only.**

Ratios, exponents, growth rates, percentages and normalised comparisons are
derived **in the write-up**, where they are reviewed, not in the script, where
they are trusted.

The write-up is read adversarially by someone asking "is that right?". The script
output is read as data. Putting a derivation in the script moves it from the
first regime to the second, which is exactly backwards for the part most likely
to be wrong.

**Where a script must derive** — because the derivation is the measurement, as in
an envelope fit — it **asserts its denominator**:

```python
assert abs(np.log(scale)) > 1e-12, f"degenerate scale {scale}: exponent undefined"
assert len(series) > n, f"need >{n} points for an n-back difference, have {len(series)}"
```

An assertion that fires is a defect found in one second. A silent `inf`, or a
ratio taken against a partial window, is a defect found by a reviewer three
rounds later — if at all.

## Third guard: localise before you judge

**A failing tolerance is tested for localisation — boundary, edge, degenerate
region — before it is either widened or the code is blamed.**

The C2 differentiation check failed at 19.7% and looked like a broken estimator.
Split by region it was:

```
first 3 samples   13.1%      one-sided stencil
last 3 samples    19.7%      one-sided stencil
interior max       0.23%     clean
```

Both available responses to the bare 19.7% were wrong. Widening 5% -> 20% goes
green and **hides a field that was fine to 0.2%**. Blaming the estimator
discards a method that worked. Only localisation gives the actual answer, and it
is cheaper than either.

This guard catches the case **without needing the tightening to be tried first**.
In C2 the tightened bound happened to be tried and happened to pass, which was
luck; the rule should not depend on that.

Sits alongside the two standing rules — **never widen to pass**
(`CLAUDE.md`) and **raw columns only** (above).

## Fifth guard: only a convention-free anchor detects a convention error

**A frequency-domain / time-domain comparison detects implementation errors. It
does not detect convention errors, because both sides can share the convention
and agree perfectly while both are flipped.**

DR2 was built with this weakness and it is now demonstrated rather than
hypothetical. The TD/FD comparison passed to <2°, and it *had* to — both sides
read the same BEM data through the same convention. What actually established
the excitation sign was the **physical anchor**: heave rides long waves in phase
with `eta`, where a flip would read anti-phase. That anchor uses no BEM
convention on either side, which is the only reason it can see the thing the
comparison cannot.

The same structure appeared immediately afterwards in the panel extraction,
where the radiation damping sign turned out to be the conjugate of the assumed
form (schema §5.0.3).

**So every such comparison is built with an anchor, named alongside it:**

| quantity | convention-free anchor |
|---|---|
| Excitation | heave in phase with `eta` in long waves |
| Radiation | **stability** — positive dissipation; a flipped `B` diverges rather than drifts |

The radiation anchor is worth dwelling on, because it is the one that settles
scope. It is why the Capytaine finding is a property of the *new extraction
path* and not a latent simulator defect: FloatSim's runs are stable, therefore
its `B` sign is right, and no further argument is needed.

When neither anchor exists for a quantity, that is itself the finding — say so
rather than presenting an FD/TD agreement as if it closed the question.

## The general pattern: every reconstructed quantity carries its validity window

The guard below started as a fact about `run_case`. It has since applied three
times, to three unrelated quantities, which makes it a pattern rather than a
rule about one function:

| quantity | reconstructed from | valid only where |
|---|---|---|
| `mu` | replayed convolution | one kernel memory after real history begins |
| drift, second differences | a returned window | the window actually covers |
| panel pressure field | BEM at the hull's **reference position** | displacement from that reference stays small |

> **Every reconstructed quantity is exported with the window over which it is
> valid, and the validator refuses to use it outside that window.**

The third row is the one still ahead of us and the reason to state the pattern
now rather than after. Panel pressures are computed by the BEM for a hull *at its
reference position*, and linear theory assumes small motion about that position.
The platform translates **~2.3 spar diameters** over a run
(`docs/findings/mean-drift-and-screening.md`), so the field becomes progressively
less applicable to where the hull actually is. Same class as G4.6, but attached
to the panel field rather than the waterline — and free to build in, expensive to
retrofit once the exporter and its records exist.

What that requires of module 3, decided before it is written:

- record the **body pose at every exported instant**, not just the reference;
- the validator **rejects or flags** any screened snapshot whose displacement
  from the BEM reference exceeds a stated bound;
- **the bound and its basis live in the schema**, not in a comment — a
  threshold whose justification is a code comment is a number nobody can
  re-check, which is the failure mode `docs/closure/F0.md` records under a
  different heading.

## Fourth guard: a window is not a history

**Any export or diagnostic records the window it covers, and every derived
quantity that needs pre-history is marked invalid over its warm-up length.**

`run_case` returns only the final `window_periods` window, not the run. That one
fact has now produced three separate defects:

| consequence | how it showed up |
|---|---|
| Second differences inconclusive | only 6 cycles available, leakage at the signal's own order |
| Drift magnitude wrong by ~16x | the 75 s window's accumulated drift read as the drift generally |
| `mu` head invalid | zero-padded buffer where the solver had real history |

Three instances of one cause is systemic. The first two were caught after being
written down; the third was caught before, only because the pattern had been
named by then.

**The `mu` case is the sharpest, because the invalid region can exceed the data.**
`mu[0] = 0` is correct at a true run start and simply wrong at the start of a
window with prior history, and it stays wrong until the convolution buffer
refills — one full kernel memory. On the 12-buoy platform that is a 60 s kernel,
**6000 lag samples against ~1955 returned**, so a naive export of a truncated
window would be invalid over its *entire* length while looking perfectly
well-formed.

The defences, in order of preference:

1. **Export from the full run**, so the question does not arise.
2. **Carry at least one kernel length of pre-history** into the window.
3. **Mark the warm-up invalid and refuse to screen inside it** — the exporter
   records `valid_from`, and the reader rejects any case selected before it.

And the parameter that decides which case you are in gets **no default**.
`recompute_mu(..., from_run_start=...)` is keyword-only and required, because a
wrong default there produces plausible numbers rather than an error — the worst
available failure mode, and the one the other three guards exist to prevent.

## Corollary: persist the raw history

Two of the three defects could not be re-derived from stored output because the
script had printed a *filtered* view and persisted nothing. Both required a
re-run to close, at ~8 minutes each.

**Scratch diagnostics persist their raw series** (`npz` is sufficient), so a
questioned derivation can be recomputed offline instead of re-simulated. This is
cheap at write time and repeatedly expensive to omit.

## Scope

This governs scratch and investigation scripts. Committed code is covered by the
verification ladder and the tolerances rule, which are stricter. The point of
writing it down is that scratch scripts are *not* covered by those, are trusted
anyway, and feed conclusions into documents that outlive them.

## Sixth guard: when mechanisms fall in sequence, suspect the inference

**Six refutations in a row is evidence about the frame, not about the physics.**

The G1.6 radiation investigation refuted, in order: harmonic content, my own
frequency lookup, the free-decay transient, the driven build-up, a phase
convention, a diagonal `B` error, an off-diagonal `B` error, and a comparison-
window mismatch. Each refutation was sound. The sequence was the signal, and it
was missed for six rounds.

**The tell:** every refuted mechanism was *a way for `dB` to be large* — and
`dB` being large was **never measured**. It was *derived*, from a bridge that
said "the residual is purely quadrature, therefore the error is in `B`".

That bridge assumes an **uncoupled** system:

```
mu_j = -w^2 * sum_k (A - A_inf)_jk X_k   -   i w * sum_k B_jk X_k
```

The two sums run over **different matrices**, so they carry different complex
phases. The 90° relationship the bridge needs holds only when
`arg(sum A_jk X_k) == arg(sum B_jk X_k)` — true for a single uncoupled DOF,
false in general. With **96.8% of `B`'s energy off-diagonal**, it fails severely.

So the contradiction between the residual decomposition and the kernel transform
was **manufactured by the inference**. Both measurements stand. There was never
a `dB` to explain.

> **When several mechanisms are refuted in sequence, suspect the inference that
> generated them, not the next mechanism.**

The practical form: ask *which quantity in this chain was measured, and which was
derived?* A derived quantity that has survived six rounds of mechanism-hunting
without ever being measured directly is the thing to doubt.

## Corollary to the persist rule: persist somewhere durable

The rule above says scratch diagnostics persist their raw series. This
investigation persisted to a **session-temporary scratchpad**, which was then
wiped — losing a 20-minute record and every analysis script mid-diagnosis.

**"Persisted" means persisted where the next session can reach it.** Analysis
inputs that cost minutes to regenerate belong under `artifacts/`, not in a temp
directory. Persisting to volatile storage is the same failure as not persisting,
one level up, and it cost this investigation its data at the exact moment two
decisive tests were queued.
