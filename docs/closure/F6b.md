# F6b — TRUSS SIZING FROM THE BEAM FORCES · INCREMENT CLOSURE

**Status: CLOSED.** One step, two reviewed revisions under FG1's lighter process. Revision 1
was held on one item — **R801**, a real geometry defect of mine that moved the headline —
and revision 2 **PASSED** at `d509e44`, with the reviewer re-deriving all 168 cells from its
own CSV read, its own FI1 formulas, its own tube algebra and its own clause calls, with no
import of the sizing script: **336 (cell, reading) pairs at zero relative disagreement.**

Opened by **DIRECTIVE FI**. Committed date: **FI5 asked for 3 days, i.e. 14 October. The
deliverable existed on 11 October and was corrected the same day.** The date held.

**EQ0 DOES NOT REACH THIS COMMIT AND I AM SAYING SO RATHER THAN IMPLYING A REVIEW THAT WILL
NOT HAPPEN.** EQ0 reviews a closure commit that changes a gate or a tolerance; this one
changes neither — it adds this artifact, moves the chord's buckling length into its own
function (no number moves, measured below), and carries CZ1's outputs. So **items C1 and C2
below are answered on my own record and nobody checks them.**

---

## 0. Verification at closure (CZ1)

{{SECTION_0}}

---

## 1. What F6b ships

**The deliverable**: `results/F6b/truss_sizing.md` and `.csv`, labelled INDICATIVE —
idealised pin-jointed truss, no joint or connection checks, no secondary bending,
placeholder masses, one heading, `F_y` assumed. **Sent to Xabier twice: the first version on
11 October and the corrected version the same day, with the first explicitly superseded**,
because its headline cell is mass-inconsistent and he was holding it.

**The sizing**: `scripts/measure/f6b_truss_sizing.py`. FI1's two cross-sections, FI2's
sizing by bisection on `D` at the declared `D/t`, FI3's sweep over `h × b × section ×
group`, FI4(i)/(iii)/(v)'s measurements. Reuses `floatfea/checks/api_wsd.py`'s clause
functions rather than transcribing them a second time.

**The generator**: `scripts/measure/f6b_report.py`, typing no measured figure.

**Nothing in `floatfea/` or `tests/` changed across the whole increment** — FI0 said
post-processing only and that is literal.

### The answer

| group | section | shallowest, consistent under BOTH readings | chord `A` [m²] | line mass [t/m] | `μ` [t/m] | `per_face_45` | `uniform_panel` |
|---|---|---|---|---|---|---|---|
| platform (4), L = 50 m | box | `h = 4 m`, `b = 6 m` | 0.2186 | 9.097 | 9.375 | **0.970** | **0.963** |
| platform (4), L = 50 m | triangle | `h = 4 m`, `b = 8 m` | 0.2753 | 8.649 | 9.375 | **0.923** | **0.917** |
| hubs (12), L = 25 m | box | `h = 2 m`, `b = 2 m` | 0.2454 | 9.778 | 15.000 | **0.652** | **0.652** |
| hubs (12), L = 25 m | triangle | `h = 2 m`, `b = 2 m` | 0.3332 | 9.932 | 15.000 | **0.662** | **0.662** |

## 2. The tolerances F6b declares

**None.** No value was added to `floatfea/tolerances.py` and none was moved.

```
claim  no tolerance moved across the whole increment
cmd    git diff --stat 4862f6e..HEAD -- floatfea/tolerances.py floatfea tests
out    (empty)
rule   FI's `D/t = 24`, the `1.15` joint allowance, the 45° diagonals, the sweep grids and
       `F_y = 355 MPa` are declared inputs, carried in the deliverable's label
judge  no counter is declared, so **EU1 does not arise** -- there is no configuration axis
       for an adversarial case to range over. The reviewer's caution is recorded in § 5:
       `D/t` and the joint allowance are the two inputs the answer scales most directly
       with, and a reader sizing steel should treat both as dials even though neither was
       chosen to make two numbers agree.
```

## 3. R801 — the blocking item, and why it is the increment's most useful output

**What was wrong.** The sizing took the chord's buckling length as `min(h, b)` while its own
comment said *"panel length = the face dimension"*. A box of depth `h` and width `b` has
**two** face dimensions, so FI1's "diagonals at 45° (panel length = the face dimension)" has
two self-consistent readings — and I took **the shorter buckling length from one and the
shorter diagonal from the other**. That is the favourable half of each and it is not a
reading of FI1 at all.

**Where it landed.** The published headline, at the grid's most extreme aspect ratio, 8:3 —
which is exactly where `min(h, b)` is most wrong. `h = 3, b = 8` was published at `0.979`
and is `1.023` / `1.027`: **mass-inconsistent under either reading.**

**The repair is structural.** The geometry is stated once, in a `GEOMETRIES` constant, a
`chord_buckling_length()` and a single `panel_and_diagonal()` — so the chord's length and
the diagonal's length can no longer be taken from different readings, which is what R801
was. **Both readings are swept and published**, because which one FI means is a plan
question rather than a generator question, and the recommendation is the shallowest cell
consistent under both.

**Three consequences came with it**, and the reviewer ruled the first of them a second
defect it had not found: each face's diagonals are sized for **that face's own** shear (FI1
gives the two kinds of face different shears and FI2 asks for each member's governing
station — one worst-shear-everywhere satisfied neither); a diagonal buckles over its own
length; and `mass_ratio` is replaced by the two readings plus `mass_ratio_worst`, with the
headline keyed on `consistent_under_both`. Per BP0 the areas, the line masses and both ratio
tables were regenerated end to end.

## 4. What the reviewer established that I had not

**The `h = b` control cannot fail, and that is its limit rather than its reassurance.** I
leaned on it as evidence; the reviewer showed it is an *identity*.

```
claim  at h = b the two readings are the same geometry, not two computations that agree
cmd    the reviewer's own probe over every h = b cell
out    per_face_45  returns (max(h,b)=s, s√2, √2)
       uniform_panel returns (s, hypot(s,s)=s√2, √2)   -- identical in all three components
       24 cells, max |ratio_A - ratio_B| = 2.220e-16   -- round-off
rule   a control that cannot fail detects nothing
judge  **it does establish what I claimed** -- that the divergence at `h ≠ b` is geometry
       and not a bug in one path -- **and it cannot detect an error shared by both.**
       Correctness has to come from outside the pair, and the 168-cell independent
       re-derivation is what supplies it. I was treating an identity as a measurement.
```

**Monotonicity, which I flagged as unproven, holds.** 7.54M evaluations, zero non-monotone
pairs — plus a proof: at fixed `D/t`, `r ∝ D` so `F_a` rises to `0.6 F_y` while `|F|/A`
falls as `D²`, and § 3.2.2(b)'s local reduction depends on `D/t` alone, which is held. The
bisection's root is the root.

**FI5's hand recomputation passes**: the chord force exact, the area to five figures.
**FI1(b)'s triangle** was derived independently from first principles and is correct — and
the warning I gave was right, that both equilibrium checks close for a wrong `I` with
consistent levers, so the derivation and not the checks is what had to be read.
**FI4(iii)'s hand table** confirmed. **FI4(v)'s narrow answer** ruled acceptable with no
cell required, and the CoG closed form reproduced independently.

**The 1-of-168 disagreement is right, and the reviewer's clause is better than mine:** the
cell disagrees because it **straddles** the line — both values within `0.33%` of `1.0`, a
spread of `0.43%` — not because the readings diverge there. "Robust to the reading" is the
stronger way to say it.

## 5. The ledger — what is open, by name

**Nothing blocking.** Two closure items, both from the PASS verdict, both about the trace
rather than the tree, and **both answered here on my own record because EQ0 does not reach
this commit**.

**C1 — § 6 of the report asserted the boundary classes in prose, and EG3(i) requires the
trace pasted.** No ids, no counts, no `FAILED` list. The measured number is **nine, not
one**:

```
claim  the boundary set at the reviewed commit, by id
cmd    python -m pytest -q tests/test_report_carried.py tests/test_report_guard_states.py
       tests/test_report_numbers_are_sourced.py -p no:randomly
out    9 failed, 157 passed, 1 skipped in 432.11s
       tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
       tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]
rule   EG3(i): the waiver is conditional on the trace, and the trace is pasted -- each
       `FAILED` id matched to the state's own list, not "the failures look like the
       boundary set"
judge  2 are FC1's pair, which cannot pass in the commit they describe; 7 are the planted
       states cascading off a red `[baseline]`, whose nested run sees that same pair.
       **`tests/test_report_numbers_are_sourced.py` is 0 failed, which is the control.**
       The tree is fine -- and **R629 was the eighth member of exactly such a group**, so a
       class assertion cannot tell nine designed reds from eight designed and one real.
       That is why the ids are here and not a sentence.
```

**C2 — and this one is sharper, because my reasoning was inverted for exactly the tests that
were red.** I wrote that the suite needed no re-run because `git diff -- floatfea tests` is
empty, so "no test's subject changed".

```
claim  the diff shows no test CODE changed; it does not show no test SUBJECT changed
cmd    git diff --stat 6e32716..6ebe4c0 -- docs/reports/F6b/step-1.md
out    revision 2 rewrote it (+341) and 6ebe4c0 extended it (+103)
rule   the three report-guard files READ `docs/reports/F6b/step-1.md`
judge  **their subject changed more than anything else in the tree**, and the proof is that
       their red count moved 37 -> 9 across those commits. The reason I gave is sound for
       the ~3300 tests whose subject is `floatfea/` and **exactly inverted for the nine that
       are red.** The correct statement is: no test of `floatfea/` had its subject changed,
       and the report guards had theirs rewritten, which is why their count moved.
```

**The latent fragility, fixed here.** `chord_L` was taken as
`panel_and_diagonal(geometry, h, b, faces(...)[0])[0]` — a non-per-face quantity out of a
per-face call, correct only because both readings happen to return a face-independent first
element. A reading that made it face-dependent would have been silently resolved by
whichever face sorted first. It is now `chord_buckling_length(geometry, h, b)`.

```
claim  the refactor moves no number
cmd    regenerate both artefacts and diff the results tree
out    (empty)
rule   BP0: a figure whose rule moved is regenerated or withdrawn -- here the rule did not
       move, and the empty diff is what says so
```

**Disposed of, not ledgered:** the `1 skipped` — my correction was accepted and the
verdict's claim withdrawn. It is `test_a_RED_suite_is_named_in_the_report` deferring to the
whole-suite guard when that line is absent, state-dependent rather than new, and F6's own
step-2 verdict records it at the then line 2429. The `D/t = 24` / `1.15` caution is recorded
in § 2.

**F6a's ledger stays on `docs/closure/F6a.md`** — R788, R789, R790, R791 — and nothing in it
was touched by this increment.

## 6. The limitations every F6b number carries

1. **The truss is a pin-jointed idealisation** with no joint or connection design and no
   secondary bending. Joints are where a truss of this scale is actually decided.
2. **No system buckling of the bracing**, only member-level § 3.2.2 at the panel length.
3. **The masses are placeholders** — platform `9.375 t/m`, hubs `15.0 t/m`, and § 7 is about
   exactly this.
4. **One heading, 0°**, which § 7's first finding shows is load-bearing in a way a tube
   never exposed.
5. **`F_y = 355 MPa` is assumed**, not specified.
6. **Which reading of FI1 is meant is undecided.** Both are published; the recommendation
   survives both; picking one is a design decision rather than a measurement.
7. **The frame model was not re-solved.** The stiffness note is a pointer to a future F4
   run, not a result.

## 7. What reaches increment 2 and increment 3

**FOR INCREMENT 3 (the heading plan): `b` MAY NOT BE SIZED FROM ONE ARM.** `Mz` is
`2.689e+08` on two platform arms and round-off on the other two, and the four arms are
geometrically identical — the split is which way the wave comes, not the steel. At heading
0° the along-wave arms take the demand as `My` and the transverse arms take the same demand
as `Mz`. **A tube never exposed this because it is axisymmetric; a truss with `h ≠ b` does.**
One section per group has to carry the larger moment in both planes, and width buys more
than depth on the platform arms because `max|Mz|` exceeds `max|My|`.

**FOR INCREMENT 2 (the mass budget): the deck CoG is unreachable by any truss in the grid,
and the remainder's height is not a modelling choice.**

```
claim  the remainder's height is forced by the CoG, in closed form
cmd    `_build_body`'s placement rule, inverted, against the built model
out    z_remainder(f) = (z_cog - f z_joint) / (1 - f)
       joints 24.668 m ; deck CoG 35.000 m (10.33 above) ; remainder 65.995 m (41.33 above)
       closed form 65.995 m, error 1.42e-14 m
       a truss of depth h reaches a CoG of at most z_joint + h/2
       -> the deck CoG needs h = 20.66 m, against a sweep stopping at 10 m
rule   every arm midpoint lies in the joint plane, so the arms' first moment is
       `f·deck_mass·z_joint` and the remainder's height follows exactly
judge  **the inconsistency is not between the truss and the remainder's HEIGHT -- it is
       between the truss and the deck CoG itself**, at every depth in the sweep and whatever
       `f` is, because the closed form puts the leftover mass HIGHER as `f` falls. And
       `h/2` is the generous ceiling: a box reaches it only with chords at the very top,
       and a triangle's centroid is at `h/3`.
```

And the narrow answer to what FI4(v) literally asked: **none** of the governing *horizontal*
moment comes from the remainder's height. It sits on the centreline, so its weight produces
no horizontal-plane moment, and a horizontal acceleration at `41.33 m` produces an
overturning couple about a *horizontal* axis, which the arms carry as `My`. The height's
consequence is in `My` and in the arithmetic above.

## 8. One finding of my own, and what caught it

The torsion share was first computed by **differencing** two resolutions and returned
**exactly zero** — at the governing row `T = -1.411678e-09 N·m` against a face shear of
`2.956708e+06 N`, so the two agree to 16 significant figures and the subtraction underflows.
Formed from its own terms it is `2.984057271793956e-17`, matching a hand value exactly.
Publishing `0.000e+00` would have been publishing a cancellation as a result. G4.1's rule in
another guise: a small quantity is formed from its own terms, never by subtracting two large
ones.

**And the repair was live for one run while the document still said zero**, because two
stale differencing lines survived three rows below the new assignment and overwrote it. A
replacement that leaves the thing it replaced still executing is not a replacement.

**What caught it was a hand calculation**, and the reviewer's note on that is the one worth
keeping: nothing in this repository would have caught `0.000e+00` for a quantity whose true
value is `1e-17`, because both read as zero to any threshold anyone would write. **That is
the reason FI5 asks for a hand recomputation at all.**
