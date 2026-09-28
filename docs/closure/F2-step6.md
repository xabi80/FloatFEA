# F2 step 6 — G2.1 reduced to the λ₇ bound and G2.2 · CLOSURE

**Status:** CLOSED at the sixty-first verdict, PASS, at `792c44e`. **Five
verdicts on this step: 56, 58, 59, 60 and 61**, one of them a **STOP**. This
line said "six verdicts" and then listed five (C2); verdict 57 wrote step 5's
disposition by hand under DD1 and was not about step 6 at all. **The element
formulation was never found to be wrong. What was wrong, four times, was the
measure.**

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
| **elements failing at least one counter** | see the command — the count moves with the corpus |

Every one of the three shapes misses some element. At `L/r` of 1e+08, or on a
member a nanometre long, a
perturbation of the largest entry falls below round-off in the blocks the rigid
vectors excite — the clean residual is tiny there for the same reason the
defect is invisible. **Proportions are the one axis this form keeps, and this is
its own dilution on that axis.** DG2 was pre-registered before the form was
measured, and it applies. **No fifth ASSEMBLED-RESIDUAL NORMALISATION was
proposed.** This sentence read "no fifth form was proposed" (C4), and verdict
60 did propose a form — the `lambda_6` ceiling that §4 below ships as what
carries the premise. What DG2 forbade was a fifth attempt to normalise the
assembled residual, and there was none.

**THE COUNT HAS TAKEN THREE VALUES IN THREE COMMITS AND THE CODE DID NOT MOVE
BETWEEN ANY OF THEM.** `298 of 1592`, then `335 of 1702`, then, at the closure
commit `d147f25`:

```
cmd    python scripts/rigid_counter_response.py
out    1851 distinct elements over the rigid-body corpus
       clean worst 1.4575e-16 = 0.656 eps at rb9_brace_shrunk_1e3_2p87_subdiv4
       clean clears 1e-15 by 6.861x
       ELEMENTS FAILING AT LEAST ONE COUNTER: 427 of 1851
rule   each of the three counters must redden every element, which is what
       DG2 tested this form against
```

Each value was right at its own commit and stale at the next, because the
corpus grows and nothing in this repository re-takes a figure when it does.
**So the plan, the tolerance entry and the diagnostic's docstring now carry the
command and no count (C1).** The first two carried `298 of 1592` for two
commits after the plan had moved on, which is the same staleness DB1, DC0 and
R514 were each about, arriving in the commit that was repairing it.

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
the corpus **as it stood at 187 frames**, and **1.8235** over **1344 unseen
frames** the reviewer built (unit `1e-3`–`1e6`, span `1e-6`–`1e8`, four
sections, subdiv 1 and 4, tips at 2.87/3/6/35°) — **0 over the bound**,
109× clear. A further **960 frames** at the closure verdict, on axes two
decades wider, put the worst at **1.2768** with **0 over** and 480 of them
refused by the builder rather than defaulted; and the reviewer's batch 10 added
**11 frames aimed at the refused half**, worst `0.8882`, **0 false-red**.

**The frame counts are stamped because the corpus grows.** It is 213 entries at
the closure commit and was 187 when the first figure above was taken; the
figures are not re-taken here, they are dated.

```
cmd    grep -n rigid_mode_largest_rigid_eigenvalue docs/milestones/F2_figures.md
out    | `rigid_mode_largest_rigid_eigenvalue` | 1.2727 |
rule   the row is a floor-class figure, compared below `RIGID_MODE_BOUND` by
       `test_every_floor_class_row_clears_its_tolerance_on_THIS_tree`
```

That row is produced by `python scripts/regen_figures.py` on the canonical
machine and is the number a later reader should take, rather than any figure
dated above (C1's lesson, applied to figures that were still correct).

**Its coarseness, stated plainly.** Bisected detection edges: **`2.7202e-13`**
translational and **`1.6809e-12`** rotational, as fractions of `max|K|`. The
retired counter `1.0e-14` is `0.037×` and `0.0059×` of those, so the carrier is
**27×–168× coarser** than claim A was — a ~200-ULP statement where claim A was
~1-ULP. At 200 ULP nothing of structural meaning hides, which is the judgement
this closure rests on and it is recorded as a judgement, not a measurement.

The implementer's control reproduces the translational edge independently:
clean λ₆ `0.4143` units, and the per-frame assertion breaks at a defect of
**`2.7202e-13`** of `max|K|` — the same figure to five digits.

### What the replacement detects, which no document held until the closure

The reviewer measured this at the sixty-first verdict and it is the strongest
argument for the replacement that exists. It was in neither the plan, the
report nor the first draft of this artifact, and it is here because a gate's
**sensitivity** is not established by its clean margin.

The three element-defect shapes from `scripts/rigid_counter_response.py`,
injected into **every element's local stiffness at the assembly site**, then
measured through the per-frame `lambda_6` ceiling and split by the gate's own
decided/refused classification:

```
cmd    python scripts/rigid_counter_response.py
out    (clean worktree at d147f25)
       the spectral half decides 163 frames and refuses 50; the ceiling is
       evaluated at all 213
       at 1e-08 of max|k_e|, into EVERY element:
         dropped_flip      decided 150 of 163    refused  4 of 50
         wrong_dof_index   decided 163 of 163    refused 38 of 50
         rotational_block  decided 128 of 163    refused  0 of 50
       at 1e-04, four decades up:
         dropped_flip      decided 163 of 163    refused 36 of 50
         wrong_dof_index   decided 163 of 163    refused 39 of 50
         rotational_block  decided 147 of 163    refused  0 of 50
rule   a comment claiming the element is "under test everywhere" is measured
       against whether each named defect shape can redden the assertion there
cell   one variable: the element's own local stiffness, patched at
       `floatfea.assemble.system.local_stiffness` — the name `assemble_dense`
       resolves. Patching the definition's home module injects nothing and
       reads "no defect" on a defect never applied; the reviewer's first cell
       did that and the second corrected it. Everything else held: same
       frames, same builder, same eigensolver, classification taken clean
       before injection.
```

**Two things follow, and they point in opposite directions.**

On the frames the gate decides, the per-frame ceiling reddens under all three
shapes at a size where the **element-local** diagnostic leaves a large minority
of elements undetected. The assembled assertion is the more sensitive of the
two on the domain the gate certifies — which nobody had measured when claim A
was dropped, and which makes the replacement a better trade than it was argued
to be.

On the frames it **refuses**, one shape reddens nothing at either size. That is
**R540**, the one blocking item this verdict raised, and it is answered in the
closure commit `d147f25`: the tolerance entry states both directions of the
constant and names the assertion's line, and the comment that said "the element
is under test everywhere" now says **evaluated** everywhere and points at this
command for what is sensitive where. No value moved.

**And the indefinite element.** The reviewer flipped the sign of two diagonal
entries — six negative modes at `-1.995e+14` units — and found the per-frame
`lambda_6` assertion **red** while the shipped single-frame `lambda_7` gate
**passed**, because that gate reads `|lambda_7|` and cannot see a sign. The
replacement closes a hole in the spectral half that it was not asked to close.
`seventh_over_epsilon` is documented as `|lambda_7|` now, and says which
information the absolute value destroys (C10).

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

**R533** is the citation guard's domain excluding `floatfea/` — **frozen
apparatus, not extended**, with the one-tuple fix recorded in
`docs/milestones/F2a.md` for whoever unfreezes 4a. This sentence called it
**R532** (C3), repeating in the artifact the error `3c83650` had just corrected
in the plan; a frozen item naming the wrong finding is a pointer to nothing,
which is the species R533 is itself about.

**R532** is a different finding — that no directive from DG1 to DI2 was
recorded anywhere in the repository — and it is answered rather than frozen, by
`docs/milestones/F2.md` §5g, a ledger of every directive with what was acted on
and where it is recorded. The sentence that first answered it claimed every
directive had a commit citing it by name and one grep refuted that for three of
them (C8); a record that can be read replaced a sentence that had to be
believed.

**Answered in the closure commit `d147f25`:** R540 (blocking — the constant's
two directions and the refused half's sensitivity), C1 (the stale count at two
sites), C5, C6, C7 (four sentences describing the deleted gate), C9 (the
stranded span table, counter-DOF table, injection helper and bisection helper
deleted; the `"residual"` branch of `counter_response` deliberately left, with
the reason at the site), C10 (`|lambda_7|` named as what is computed), C11 (the
retired-ratio scan handles a correct raise instead of propagating it). **In
`7d7175d`:** C8 and the plan's own stale figure. **C12:** the determinism legs
were dispatched by hand at `52941f7` — run `36264799173`, **ten legs and the
agreement job all success**, the first execution since a 496-line change under
`tests/verification` and `scripts`.

**Carried as a list, unchanged and not re-reviewed:** R526 (the pin control
computes a retired quantity), R527 (R487's assertion is a theorem and a NaN
walks past it), R529, R519, R521, R522, R513 (generator subject fragments),
R535, R538, R539, R500, R501, R475, R487, R488, R492, R493, and the 48 items
already frozen in `docs/milestones/F2a.md`.

**Tolerances: no value moved in this step.** `git diff` over
`floatfea/tolerances.py` across the whole step changes 53 lines and **every one
of them is a comment** -- filtering comment lines out leaves zero. The first
draft of this sentence said "zero changed lines", which the command refuted;
the distinction between the file changing and a VALUE changing is the whole
point of the claim, so it is written the way the command reads. Two entries had
their prose corrected — `RIGID_MODE_EXACTNESS` no longer claims an assertion that was
deleted, and its counter no longer claims an injection that does not happen.
