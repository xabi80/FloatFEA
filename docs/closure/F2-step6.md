# F2 step 6 — G2.1 reduced to the λ₇ bound and G2.2 · CLOSURE

**Status:** closing on the sixty-first verdict. Six verdicts on this step
(56, 58, 59, 60 and the closure verdict), one of them a **STOP**. **The
element formulation was never found to be wrong. What was wrong, four times,
was the measure.**

---

## 1. What changed, in one sentence

G2.1's **claim A** — that the assembled matrix annihilates the six global
rigid-body motions — **is no longer an F2 gate.** It ships as a diagnostic.
G2.1 in F2 is **claim B**, the seventh-mode bound, plus **G2.2's** coverage,
and per frame the corpus now asserts that the six numerically-zero eigenvalues
sit under that bound.

## 2. Why: four forms, four axes

Every assembled-level form measured the residual using rigid vectors built
about a **global point**, so span, position and orientation entered the
quantity through the lever arms, and each normalisation had to cancel all
three.

| form | broke on | evidence |
|---|---|---|
| `λ₆/λ₇` ratio | frame conditioning | over its ceiling on a large fraction of defect-free frames |
| `‖Kv‖/(max|K|·‖v‖)` | **span** | R475: the rotational counter detected at 4 m, invisible from 400 m up |
| per-DOF denominator | **near-vertical members** | R486: `2.9994e-14` on a defect-free element at 2.87° from vertical, 30× the ceiling |
| row-shared denominator | **near-vertical again** | R524: 22 of 130 defect-free frames over the ceiling; `2.4727e-15` at 2.95°, while the element read `3.8709e-17` on the retired form with `1.870e-17` of strain energy |

**The element was fine in every case.** A picometre of tip coordinate doubled
R524's figure.

## 3. The element-local form, and why it is a diagnostic

Per element, in its own frame, six rigid motions about the element's own
midpoint, homogenisation on the matrix (`k̂ = S⁻¹kS⁻¹`, rigid vector `S·r`, so
the transform cannot create or destroy the property under test). **Orientation,
span and reference point leave the quantity by construction** rather than by a
cleverer denominator.

Every figure here is printed by **`python scripts/rigid_counter_response.py`**,
run at the commit that publishes it.

| measurement | at this commit |
|---|---|
| clean worst over every distinct corpus element | `1.4575e-16` = **0.656 ε**, 6.861× clear of `1e-15` |
| frame independence | identical wherever the same element reappears |
| the near-vertical band 2.87°–6° | 0.007–0.035 ε — its quietest region |
| **elements failing at least one counter** | **335 of 1702** |

The counters miss 67 (`dropped_flip`), 32 (`wrong_dof_index`) and 303
(`rotational_block`). At `L/r` of 1e+08, or on a member a nanometre long, a
perturbation of the largest entry falls below round-off in the blocks the rigid
vectors excite — the clean residual is tiny there for the same reason the
defect is invisible. **Proportions are the one axis this form keeps, and this is
its own dilution on that axis.** DG2 was pre-registered before the form was
measured, and it applies. **No fifth form was proposed.**

**The count was `298 of 1592` when first measured and is `335 of 1702` now.**
Both are right at their own commit; the corpus gained two batches. The plan
cites the script rather than the number, which is why the difference is visible
rather than silent.

## 4. What carries the guarantee now

| premise | carried by |
|---|---|
| the six are at the arithmetic floor | `test_G2_1_holds_at_every_frame_in_the_corpus` — **λ₆ < `RIGID_MODE_BOUND`, per frame** |
| there is no seventh | claim B, the `λ₇` bound, unchanged |
| the transform is orthogonal | `test_spectrum_invariance_under_the_transform`, with its non-orthogonal counter-case |
| assembly puts contributions at the right DOFs | G2.2's `test_the_six_constant_strain_states_are_EXACT` |
| each element annihilates its own rigid motions | the diagnostic — **an assertion in F3, on every real platform member** |

### The carrier, measured by the reviewer

`λ₆(K̂)/(‖K̂‖·ε)` against `RIGID_MODE_BOUND = 199.526`: worst **1.6536** over
the 187 corpus frames, and **1.8235** over **1344 unseen frames** the reviewer
built (unit `1e-3`–`1e6`, span `1e-6`–`1e8`, four sections, subdiv 1 and 4,
tips at 2.87/3/6/35°) — **0 over the bound**, 109× clear.

**Its coarseness, stated plainly.** Bisected detection edges: **`2.7202e-13`**
translational and **`1.6809e-12`** rotational, as fractions of `max|K|`. The
retired counter `1.0e-14` is `0.037×` and `0.0059×` of those, so the carrier is
**27×–168× coarser** than claim A was — a ~200-ULP statement where claim A was
~1-ULP. At 200 ULP nothing of structural meaning hides, which is the judgement
this closure rests on and it is recorded as a judgement, not a measurement.

The implementer's control reproduces the translational edge independently:
clean λ₆ `0.4143` units, and the per-frame assertion breaks at a defect of
**`2.7202e-13`** of `max|K|` — the same figure to five digits.

## 5. R531 — the finding that gives this step its lesson

Retiring claim A left the corpus gate asserting `λ₇ > 0.0` and nothing else,
**and the same commit added two comments saying the opposite**, one of them
four lines below the assertion it had just deleted. The reviewer injected a
defect of **`1e+03 × max|K|`** and the gate still passed: there was no defect
size at which it reddened, and every *refused* frame — the frames CT2's whole
argument is about — was asserted on nothing.

**The lesson, and it is the one worth carrying out of this step: a dropped
assertion needs its replacement carrier in the same commit.** Not in the next
one, and not in a comment claiming the old one survives. The replacement here
is λ₆ under the bound, with a bisected edge proving it can fail.

## 6. Deferred, with the reason

* **V1.3 unit scaling** — the corpus re-expresses the same structure in
  decimetres, centimetres, millimetres and kilometres, and G2.2's entries carry
  a `unit` re-expression with `E` scaled by its inverse square.
* **V2.3 torsion**, **V2.4 three-dimensional coupling** — the patch test
  asserts constant twist and curvature in each bending plane over six
  state/plane combinations on an irregular skew mesh, and
  `test_rotation_invariance_of_the_response` covers the coupling AV2 asked for.
  The closed-form torsion case and the out-of-plane portal are what is
  deferred, and F3, F4 and F5 read neither.
* **R486's admissible-domain ceiling** — became a G3 gate on the real platform
  model (DD0), which is a stronger statement about the structure being analysed
  and a weaker one about structures in general.

## 7. Closure items carried out of this step

R526 (the pin control computes a retired quantity), R527 (R487's assertion is a
theorem and a NaN walks past it), R529 and R519/R521/R522/R513 (generator
subject fragments, unchanged), R532 (the citation guard's domain excludes
`floatfea/` — **frozen apparatus, not extended**), R533–R539 as listed in the
sixtieth verdict, and the 48 items already frozen in `docs/milestones/F2a.md`.

**Tolerances: no value moved in this step.** `git diff` over
`floatfea/tolerances.py` across the whole step changes 53 lines and **every one
of them is a comment** -- filtering comment lines out leaves zero. The first
draft of this sentence said "zero changed lines", which the command refuted;
the distinction between the file changing and a VALUE changing is the whole
point of the claim, so it is written the way the command reads. Two entries had
their prose corrected — `RIGID_MODE_EXACTNESS` no longer claims an assertion that was
deleted, and its counter no longer claims an injection that does not happen.
