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
