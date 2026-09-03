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

## Seventh guard: reproduce the solver's discretisation, not the textbook rule

Checking a solver's numerics against *the correct rule for the same integral*
answers a different question than the one asked.

The G1.6 residual was chased for eight rounds and briefly **withdrawn as
refuted** because the retardation kernel, transformed back with **trapezoid**
weights, reproduced the tabulated `A(ω)` and `B(ω)` to ~5%. That measurement was
sound. It was also irrelevant: `RadiationConvolution.evaluate()` is a **plain
rectangular sum**, and the `dt·K[0]/2` difference between the two rules was
`5.82×` the entire tabulated `B`.

Recomputed with the solver's own weights, the quadrature rule alone predicted the
measured residual — `0.2258` against `0.2085`, phase within 1.6°.

> **A faithful kernel and an unfaithful sum over it are different findings, and
> only the second one was ever applied to the platform.**

The tell: a check that exonerates a component while the discrepancy persists.
Before concluding a component is faithful, confirm the check used *its* arithmetic
and not the arithmetic it should have used.

## Eighth guard: a gate should carry the failure it detects, not only the success it asserts

The general form of the vacuous-negative-control rule, which has now appeared in
**four disguises**:

| disguise | how it passes without testing anything |
|---|---|
| vacuous negative control | the control never had the property it was controlling for |
| fixture-pose meta-test | the fixture's pose is near zero, so a pose-sensitive check cannot discriminate |
| rename-detection test | `"nothing imports X"` passes **trivially** once `X` has been renamed away |
| FloatSim's in-test rectangular rule | the gate cannot fail against a stub, because the stub is what it compares to |

In every case the check is green and **certifies rather than tests**.

> **A check that cannot demonstrate its own failure mode certifies rather than
> tests. Build the failure into the gate, not just the pass.**

Concretely, a gate should be able to answer: *what would make this red?* If the
answer is "nothing available in this fixture", the gate is decoration. The
remedies are cheap and specific — a meta-test that asserts the negative control
*can* fail; a rename-detection test asserting the symbol still exists before
asserting nothing imports it; a deliberately wrong rule checked in alongside the
right one so the comparison has something to reject.

This is why G1.6's move to a **round-off** target (AH2) is paired with AG5's
per-DOF fingerprint. Under the old design a zero residual was self-evidently
broken. Under a round-off target zero is the *expected* answer, so that alarm is
gone and something must replace it: a *shape* — heave barely moving, pitch and
surge collapsing, the change tracking `K(0)` — that a stub cannot fake.

## Ninth guard: a ratio against a varying denominator carries its operating point

> **Reduction, frequency and configuration travel with the number, or the number
> means nothing.**

This resembles the unstated-input rule — the tube diameter, the lever arm — but it
is sharper. Those were inputs someone forgot to write down; the value was fixed
and recoverable. Here the **denominator itself varies by orders of magnitude**, so
the *same computation, honestly performed and honestly reported*, gives:

```
dt*K(0)/2 against ||B(w)||_F, whole-matrix Frobenius:

  w = 4.0     0.23x        w = 2.0     5.82x        w = 1.0    63.27x
  and as a mean pitch diagonal at w = 1.0:        4605.93x
```

`0.23` and `4606` are both correct. Neither is wrong, and no amount of care in
computing either one makes it interpretable alone.

The failure this prevents is not a wrong number but a **wrongly-scoped** one: a
reader who takes `43×` as "the size of the defect" concludes something false about
a defect whose actual character is that it is **constant** while the thing it is
compared against is not. That framing — see
`docs/findings/radiation-convolution-endpoint.md` §1 — only becomes visible once
the operating point is attached.

It applied immediately and twice: the document's own title carried a bare `6×`,
and a `278×` range figure differed from a measured `9059×` purely by the band it
was taken over.

## Why the dead-DOF rule is enforced in code (AJ3)

The eighth guard was recorded, and violated one commit later. That alone argues
for enforcement over memory. **The measured behaviour argues for it far more
strongly.**

The dead yaw DOF (`mu = 1.2e-17`) entered an AG5 correlation in two successive
revisions of one script, and corrupted it in **opposite directions**:

```
revision 1   yaw's round-off read as a real -4.1% change    ->   +0.1246
revision 2   yaw's nan mapped to zero                       ->   +0.6523
truth        live DOF only                                  ->   +0.5256
```

The two contaminated values **bracket** the true one. The **sign of the error was
set by an incidental choice about how the dead DOF's noise happened to be
handled** — a detail neither revision considered a decision at all.

> **A defect that can land on either side of the truth cannot be caught by
> noticing that the answer looks wrong.**

Every other guard here has a tell: a number too large, a residual that will not
close, a mechanism that keeps not being found. This one has none. Plausibility
review — the reviewer's last line of defence — is blind to it by construction,
because the error has no characteristic direction to be suspicious of.

That is the case for `frames.live_dof()` / `over_live()` being structural rather
than remembered, and it generalises: **when a defect's sign is set by an
incidental implementation choice, the only available defence is making the choice
impossible to take.**

## Tenth guard: evidence provenance, not just existence

Distinct from the eighth, and the distinction is the point:

| guard | asks |
|---|---|
| **eighth** | *can this check fail?* |
| **tenth** | *does this check point at the claim?* |

A test can be fully capable of failing, exercise a real code path, and still be
testing something **adjacent**.

> **"A test exists and passes" is not "the right test exists and passes."**

The case: gate **G1.1** (writer/reader round-trip, bit-exact) was recorded PASS
citing a test that did not exist. It survived because something adjacent did —
G1.2's positive control, a well-formed record the validator accepts. Both are "a
valid record that passes validation". The difference is **provenance**: one was
hand-built in Python, the other produced by the writer. **Provenance is invisible
in a pass/fail**, so the substitution left no trace.

When the real test was finally written, it found two defects within minutes — a
fixture the validator correctly rejected, and an exception class that destroyed
its own message on propagation. Neither was reachable from the adjacent test.

The audit form, two questions per claim:

1. **Does the cited evidence exist?** Mechanical — now enforced by
   `tests/verification/rung3/test_closure_evidence_exists.py`.
2. **Does it test what the claim says?** **Not mechanical.** It needs reading, and
   it is where the failures live. Across the F1 gate table, (a) caught one row and
   (b) caught three more: a half-tested claim (G1.3), a mischaracterised artifact
   (G1.4), and unreproducible counts (G1.5).

Coverage of a *fault* is not coverage of the *conditions that raise it*. G1.3's
`PROVENANCE_MISSING` had three raise paths and one mutation, and the matrix's own
coverage assertion reported it covered.

## Eleventh: a rejection test that catches at the raise site never exercises propagation

`FlrValidationError` was a frozen dataclass. Python assigns `__traceback__` to an
exception as it propagates; a frozen dataclass forbids the assignment. So a real
rejection travelling up through a context manager arrived as

```
FrozenInstanceError: cannot assign to field '__traceback__'
```

— **the named fault replaced by an unrelated error at the moment it was needed.**

Thirty-nine rejection tests never saw it, because every one of them catches the
exception **at the raise site**, where no propagation happens:

```python
with pytest.raises(FlrValidationError):
    validate(mutated)          # raised and caught in the same frame
```

**Any exception-based suite has this blind spot**, and a validation error is the
worst place for it to live: the class exists to deliver a specific diagnostic, and
it destroyed that diagnostic under exactly the conditions it is raised in.

> **Test the exception's journey, not only its birth.** At least one test should
> let a real error propagate through an intervening frame and assert the fault
> survives.

Corollary, general: **an error type is part of the interface.** Making one a
frozen dataclass, a `NamedTuple`, or anything else with restricted attribute
assignment breaks a Python protocol that only shows up in transit.


## Twelfth: an empty parameter set is an error, not a skip

A parametrized test whose parameters are **discovered** — a glob, a directory
walk, an enum, a registry — becomes a silent no-op the moment discovery returns
nothing. pytest's default for this is `skip`, so the run stays green.

It happened in the module written to prevent exactly this class of failure:
`test_closure_evidence_exists.py` resolved the repo root one directory too
shallow, its glob found no closure artifacts, and **four parametrized tests
reported SKIPPED while checking nothing**. Only its own meta-test caught it.

```toml
empty_parameter_set_mark = "fail_at_collect"
```

is set in `pyproject.toml`. It is the backstop; a discovering test should also
assert non-emptiness directly, because the backstop cannot say *what* should have
been found.

## Thirteenth: verify a claim by mutation, not by re-reading

Reading asks the reviewer to re-form the judgement the author already formed, and
they will usually re-form it the same way. **A mutation is a measurement.**

> **Break exactly what the claim asserts — derived from the CLAIM TEXT, never
> from the test — and confirm the check goes red.**

Deriving from the claim rather than the test is what makes it independent. If you
have to read the test to invent the mutation, that *is* the finding: the claim and
its evidence have drifted, and the search for the mutation surfaced it.

The F1 gate-table audit ran this over seven rows. Six behaved as their claim text
predicted. **G1.2 did not, and reading had cleared it twice** — its
message-distinctness assertion iterated `list(Fault)`, which yields only canonical
enum members, so two faults declared with the same message became an *alias* and
the duplicate never appeared. The assertion was structurally incapable of failing.
One mutation found what two readings missed.

Mutation choice remains judgement, so this is not a complete answer. It converts
most of a reading exercise into execution, which is the part that was unreliable.

## Fourteenth: an assertion over a collection derived from the thing it checks can be blind by construction

The U2 family — *verify the reference* — moved up from the reference's **value** to
the assertion's **domain**.

G1.2's message-distinctness check:

```python
messages = [f.value for f in Fault]
assert len(set(messages)) == len(messages), "two faults share a message"
```

This is **structurally incapable of failing**. `list(Fault)` is built *after*
Python collapses equal-valued enum members into aliases, so a duplicated message
can never reach the list the assertion inspects — the member count silently drops
from 18 to 17 instead. The collection the assertion iterates is derived from the
very property it is checking, and the derivation removes the fault.

**Reading could not have found this**, and did not — twice, by someone actively
hunting for exactly this class of defect. The test *looks* correct, and it *is*
correct: about a domain that excludes the fault. A mutation found it in one run
(thirteenth guard).

The general form:

> **When an assertion iterates a collection produced by the same machinery it is
> testing, ask what that machinery removes before the assertion sees it.**

Instances to expect:

- an enum, dict, or set keyed by the value under test — duplicates vanish into
  aliases or key collisions;
- a registry that de-duplicates on insert, checked for duplicates after insert;
- a filesystem glob checked for the file the glob's own pattern would exclude;
- any `set()` built from the property being asserted unique.

The fix is to assert over a view that **retains** the fault — here
`Fault.__members__`, which includes aliases — and, separately, to assert the
collapse itself has not happened (`len(__members__) == len(list(Fault))`).

## What these guards are, and what they are not (AO5)

The AN3 script asserted that `newmark` was **actually instrumented** before
trusting a zero — without it, the run compares `recompute_mu` against itself and
reports a perfect result, which is precisely the shape that cost six rounds on
G1.6. That guard fired *prospectively*: written before being bitten, rather than
after.

**It is worth being exact about why, because the flattering reading is wrong.**

That guard was cheap only because six rounds of G1.6 had already made its failure
shape recognisable. It is not foresight. **These guards are compressed
hindsight** — each one is a defect that was paid for once, written down so the
next instance costs a line instead of a week.

The expectation this sets, and it should be held to for F2:

> **They fire prospectively for shapes already seen, and not at all for new ones.**

A guard list is not protection against being wrong; it is protection against being
wrong *the same way twice*. F2 will be wrong in ways this document does not
describe, and the list will grow by exactly those.

The corollary matters for how a new milestone is planned: **do not treat the
guard list as coverage.** Ask what F2's failure modes are on their own terms —
references, convergence rates, tolerance pressure — and expect the list to be
silent on most of them until after the fact.

## Fifteenth: ask what would flip the decision, not how confident you are

> **When a decision looks sensitive to an uncertain input, compute the value of
> that input that would REVERSE it. Do not estimate your confidence in the value
> you have.**

The two questions feel similar and are not:

| question | what it produces |
|---|---|
| *how confident am I in this input?* | a judgement, defended |
| *what value would flip the decision?* | **a number, computed** |

The second has an answer. The first invites **margin-defending** — which is
exactly what "the margin is large, so the conclusion is not delicate" was, and why
it had to be withdrawn from F2's lock. A margin is a property of the current
estimate; a flip threshold is a property of the decision.

**Q1 answered itself twice this way inside one lock question.**

*Load uncertainty.* The design moment is 150–300 MN·m and only the FE model can
pin it — the dominant uncertainty in the project. Asking what moment would flip
the decision produced the **invariance**:

```
P/P_E = sigma_allow * lambda^2 / (pi^2 E)
```

The load cancels against the area it sized. **No value of the moment flips it**,
because the moment does not enter. That is a far stronger statement than any
confidence interval in the moment could have been.

*Geometry uncertainty.* The margin over the threshold was 11%, which looks
fragile. Asking what geometry would flip it produced **braces 33% shorter than
assumed** — a 6.7 m truss depth at 45°, a layout that makes geometric stiffness
pointless rather than marginal. **A large move, not a nudge.**

Neither uncertainty could reach the decision, and neither fact was visible from
the margin. Both fell straight out of asking for the flip threshold.

**Distinct from the sixth guard.** That one aims at a **stuck investigation** —
when mechanisms keep falling, suspect the inference. This one aims at a **live
decision** — before committing, find what would reverse it. They share only the
move of stepping back from the object to the frame around it.

**Practical form:** invert the decision rule and solve. If the answer is "no value
of this input reverses it", record *that*, not the margin — it is stronger and it
does not decay as estimates change. If the answer is a reachable value, the
decision is genuinely open and should be recorded as undecided rather than taken
on a preference.


## Sixteenth: a guard on one construction path is not a guard on the type

`basis.torsion_constant` was added to refuse `J` for any non-circular shape, and
reported as making "the first non-circular section fail loudly at construction".
**It did not.** The call sat inside `Section.circular_tube`, a convenience
classmethod, while the dataclass constructor accepted anything:

```python
Section(A=1.0, I_y=1.0, I_z=3.0, J=99.0, shape="i_beam")   # constructed fine
```

Found because a negative control built `I_y != I_z` while labelling the shape
`thin_tube` — which additionally drew the **circular** `kappa` for a non-circular
section. The control was reaching the element by a route production code could
also take, so it was not merely a weak control; it was evidence the guard was
misplaced.

> **Ask which construction paths reach the invariant, not whether the check
> exists.** A validator on the happy path leaves every other path unguarded, and
> the code that finds the gap is usually a test doing something slightly unusual.

Moved into `__post_init__`, so it binds on the type. The related discipline for
tests: **a negative control that bypasses production paths must say so**, because
its scope is then smaller than it appears — the rewritten control builds a local
matrix by hand and records that it demonstrates transformation behaviour, not
section machinery.

## Also seen this turn: an absolute tolerance on a dimensional quantity

`atol` on a displacement is what V1.3 (unit scaling) exists to catch: the same
problem posed in millimetres moves the round-off floor three orders while the
tolerance stays put, so the unit-scaling gate either fails on the assertion or
passes it vacuously.

The tell was already visible in *why* the first draft failed — the offending
component's exact value was **zero**, and no absolute floor is meaningful there.

> **Scale the tolerance to the quantity being compared, and let the scale handle
> the components whose exact value is zero.**

A `_COUNTER` must be measured **in the same quantity as its assertion**. A
displacement-residual assertion paired with a spectrum-shift counter is two
different measurements wearing one name — and the first attempt at it substituted
an unrelated rotation and produced a constant `12.6` at every perturbation size,
which was not a counter-case but a mismatch.


## Seventeenth: a check written from the defects you met tests those defects, not the property

The patch-test mesh must be **irregular**, because commensurate element lengths
let errors cancel by symmetry — which is exactly what an exactness test must not
allow.

The first mesh ended at 9.4, making the last element `2x` the first. Caught. The
replacement was checked against *that* defect — "no length an integer multiple of
another" — and passed, while containing **`0.9/0.6 = 3/2` exactly** and
`2.8/1.7` within 0.02 of `5/3`. A 3:2 pair cancels by symmetry in some node
patterns just as a 2:1 pair does.

> **A check written from the defects already met is a test of those defects. Write
> it from the PROPERTY.**

The property is "no pair in a small-integer ratio", so the check sweeps `p/q` for
`p, q <= 5` rather than enumerating the ratios that have bitten. The third mesh
was chosen by searching for one whose closest approach to any such ratio is
`0.0877`.

**It was not a cosmetic fix.** Removing the symmetry improved the weakest state's
detection threshold about **fivefold**, from `1.51e-10` to `3.31e-11`. The
narrower check had left real sensitivity on the table, not merely a theoretical
gap.

## Corollary: record the DETECTION THRESHOLD, not only the counter-case

A counter-case is one perturbation the gate must catch. The **threshold** is where
the gate stops catching anything, and it is the number that says what a tolerance
change would cost:

```
state        sensitivity   smallest defect detected at the ceiling
axial         1.0908e-01              9.17e-12
curvature     3.7161e-02              2.69e-11
twist         1.0908e-01              9.17e-12
shear         3.0170e-02              3.31e-11   <- weakest
```

Measured by verification, not extrapolation: perturbing by the threshold lands the
error on the declared ceiling to within 0.3%.

The thresholds are **asserted**, not merely recorded — so a formulation or mesh
change that alters sensitivity fails a test rather than silently leaving the
recorded numbers describing a gate that no longer exists. That assertion earned
itself immediately: it went red the moment the mesh changed, which is how the
stale counter-case was found.
