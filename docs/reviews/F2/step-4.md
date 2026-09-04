# Review � F2 step 4
Reviewed commit: 15bbc3bfaa902303d849d8abcb9ba41b58f7ca5d
Verdict: HOLD
Tests: 366 passed, 0 failed, 0 skipped   (my run, `python -m pytest -q`, 0.92s)

Sixth pass. Reviewed range `1103d20..15bbc3b`, fifteen commits, two of them
`process:` commits touching no code. My own adversarial corpus
(`tests/corpus/`, 17 entries) is committed separately, immediately before this
verdict, and is described at the end.

**All five gated items are answered, and I verified each by re-running the check
rather than reading it.** R38's `if False:` mutation reddens the six threshold
nodes at HEAD (it did not before); `1e-12 -> 1e-13` now reddens, where the fifth
verdict measured it green; R39's replacement count is exact to the unit
(`70 in 12 files -- approx 42, allclose 17, isclose 7, assert_allclose 4`); the
gate is parametrised over three unit systems and the `6.2x` is an execution
result; the analytic resultant table is correct -- I re-derived all six states
from statics independently of `k u`, and four of five sign mutations I planted
redden eight nodes each. The element itself survived every adversarial case I
could build: a vertical member on an orientation node, `roll = pi/4` and
`1.0 rad`, a section with `I_y = 2 I_z` that the type cannot construct, two
stubby tubes, and a member along global y. None of the four blocking findings
below is an element defect.

It is a HOLD because **two new ACCURACY entries landed this step and both carry a
justification the measurement refutes**, and because the R43 answer wrote a
boundary into the locked plan as an F3 obligation that does not exist. All four
are cheap; none requires a value to move.

## Carried

Every item from the fifth verdict (`HOLD @ 44f4e14`, committed `1103d20`), traced
through `1103d20..15bbc3b` and re-measured. The report lists all fifteen, which
is the first time in six rounds that the dependency list is complete; recorded as
answered on its own terms.

- **1. R37a (gated) -- ANSWERED.** `6f321a9`. All three named sites are rewritten:
  `:818-821` now reads "A PROPERTY OF `equilibrate` THE UTILITY, NOT OF `solve`",
  `:843-847`'s failure message ends "This says NOTHING about the solve, which
  does not use it", and `:854-857` no longer argues that the control rescues a
  production choice. `grep -n equilibrat` on that file gives 15 hits and I read
  every one: three are the old claim quoted inside the withdrawal, the rest name
  the utility, the import or the call. Closed site by site, which is what the
  condition asked for. Two notes in R50 concern how the answer is cited, not the
  answer.

- **2. R38 (gated) -- ANSWERED, and I reproduced the mutation.** `9f9537f`. The
  assertion is now `assert_close(err / PATCH_TEST_EXACTNESS, 1.0,
  DETECTION_THRESHOLD_BAND, floor=eps)` -- O(1) operands, no defaults, the
  declared band deciding. My own runs at HEAD: `if stiffness_scale != 1.0:` ->
  `if False:` gives **20 failed, 79 passed** in that file and **all six**
  `test_the_measured_detection_threshold_still_holds` nodes are among them;
  `PATCH_TEST_EXACTNESS 1e-12 -> 1e-11` gives 6 failed; `-> 1e-13` gives **7**
  failed (the six, plus the gate node `[S=0.001-skew-axial]`). Inverting the rule
  myself: the ceiling can be widened by **+5.0%** or tightened by **-4.1%**
  before the weakest state reddens, which is the same band the report reports per
  state from the other direction. This is now the tightest guard in the file, and
  it is the model the two new entries should have been given (R48).

- **3. R39 (gated) -- ANSWERED, and the replacement is exact.** `d87cb1c`. I
  walked the AST of every file under `tests/` except the scanner's own corpus and
  got `total 70 in 12 files; approx 42, allclose 17, isclose 7, assert_allclose
  4` -- the docstring's four numbers and both totals, to the unit.
  `assert_close`/`assert_differs` at 3 sites in the patch test plus 10 in
  `tests/unit/test_testing_helpers.py`, also exact. The ban is now stated as
  `F2a.md`'s proposal rather than as the state of the tree.

- **4. R40 (gated) -- ANSWERED.** `0c66241`. `GATE_UNIT_SCALES = [1e-3, 1, 1e3]`,
  36 gate nodes. I re-measured all six cells through my own harness and every
  figure in the entry reproduces: `S=1e-3` axis `1.1500e-14` skew `1.6029e-13`,
  `S=1` `3.8831e-15` / `1.2513e-14`, `S=1e3` `8.8575e-15` / `4.9240e-14`. Worst
  `1.6029e-13`, headroom `6.24x`, and the out-of-band figures are labelled
  unasserted, which is the honest form. The `+24` node accounting checks out: 336
  at `24cf582`, 360 at `0c66241`.

- **5. R41 (gated) -- ANSWERED in both halves, and the reference is verified.**
  `6612280`, `24cf582`. `test_patch_test.py:235` is gone; the residual lives in
  its own labelled test against its own entry, outside the gate assertion, and
  the gate's second quantity is the recovered end forces.
  **I verified the analytic table independently of the implementation**, which is
  the eighth guard's requirement and the one thing the shipped
  `test_the_resultant_recovery_is_EXACT_on_the_exact_field` cannot do for itself.
  From statics, in the element convention `f = k u`: end `a` carries `-EA*eps`; a
  constant-curvature element gives `f[5] = -EI c`, `f[11] = +EI c` and zero shear
  (evaluated on the residual field after removing the rigid part, which is what
  makes the station offset drop out); the shear state's `f[1] = -P`, `f[7] = +P`
  follow from moment equilibrium about node `a` given `f[5] = -P(L-x_a)`,
  `f[11] = +P(L-x_b)`; and the x-z pair carries the opposite moment sign because
  `M_y = EI_y phi_y'` while `w' = -phi_y`. **Every entry in `_exact_resultants`
  is right.** Its discriminating power is real too -- I planted five mutations
  and four redden eight nodes each (x-z moment sign flipped, the shear taper
  dropped, the axial signs swapped, `J -> I_z`). The fifth, `ei_y -> ei_z`, is
  green, which is R53.
  - **R4's plan half -- answered.** The plan names the shipped entry, the
    transposed transform is now a test that runs, and the general rule ("a
    planned name is rewritten to the shipped one as each lands") is a better
    answer than correcting the single row.
  - **R5 -- answered.** Superseded by `SOLVE_RESIDUAL`.

- **6. R42 (recordable) -- ANSWERED, and I performed the diff it asks for.**
  `153b208` is a standalone `process:` commit touching only `.claude/` and
  `CLAUDE.md`; `e9dfa5b` touches only `CLAUDE.md`. Neither touches `floatfea/` or
  `tests/`. **`git diff 1103d20..HEAD -- .claude docs/SUPERVISOR.md` is 8
  insertions, 0 deletions** -- reading-order item 4b, purely additive, no guard
  removed, no instruction weakened, and it constrains rather than relaxes me.
  `docs/SUPERVISOR.md` is unchanged. The change to my own instructions is
  **additive and accepted**, and I have carried out item 4b this round as its
  first exercise. Recorded for the next reviewer: the new `CLAUDE.md` clause
  makes a mixed edit a STOP-class finding; there was none this round.

- **7. R43 (recordable) -- ANSWERED IN PART. The operating point is written down;
  the boundary is wrong. Carried as R46, blocking.** The sweep table reproduces
  to four digits through my own harness (`1.251e-14 / 3.807e-14 / 1.571e-13 /
  1.762e-12 / 4.415e-12 / 1.844e-11` at `D = 0.60 .. 0.02`), the fixed-wall
  control reproduces (`6.418e-13` at `D = 0.10`, and `D = 0.05` does breach, at
  `3.006e-12`), and the localisation is right -- skew, axial, rotational DOF,
  which I confirmed per state at both `D = 0.10` and `D = 0.12`.

- **8. R44 (recordable) -- ANSWERED, and it reproduces exactly.** `08ca53c`. I
  substituted `kappa = 0.5` for the Cowper `0.530612` and measured worst field
  `8.5848e-15`, worst resultants `2.0022e-13` -- the docstring's two figures to
  five digits. The blindness section is the right addition and names V2.2 as
  `kappa`'s real gate. It is now the register a reader consults for what G2.2
  does not see, which is why R53 belongs in it.

- **9. R15 (recordable) -- ANSWERED, and I withdraw its remaining evidence by
  measurement.** `73f4edc`. The rename is done and both margins are written down
  (`+7.6%` on the field counter, `7.7e+09` plane separation). R15 had also said
  the counter "is a property of this mesh and this section and should say so", on
  the evidence that a stubby `D = 2.0 m` tube responded at `8.898e-08 ..
  1.018e-07`, below the counter. **I re-ran that case at HEAD and it no longer
  holds**: under the post-R2 homogeneous measure the stubby responses are
  `1.0839e-07 .. 1.4062e-07` (`t = 0.040`) and `1.0836e-07 .. 1.4370e-07`
  (`t = 0.100`), all above `1.0e-7`, with the posed geometry still the worst at
  `1.0764e-07`. **Withdrawn on measurement, not on argument.** What is left of
  R15 is R52.

- **10. R26 (recordable) -- ANSWERED.** `3e793f9`. "So only commensurability
  varies" is withdrawn with the reason -- element 1's position is confounded at
  index 1 of a five-element mesh and cannot be held fixed -- and the conclusion
  is left as a spread straddling 1 rather than re-attributed. That is the right
  handling of a control that cannot be made clean.

- **11. R27 (recordable) -- ANSWERED.** `f09c2b9`. The detailed plan stops saying
  "DRAFT, awaiting review" after six reviews and four executed steps, and the new
  §D0 records the two post-lock amendments with the commits they entered at.
  `170cb52` exists and is an ancestor of HEAD.

- **12. R37 (recordable) -- ANSWERED.** `3e793f9`. `instrumentation.md:727` now
  reads `0.995%` with the six per-state deviations, replacing the `0.3%` that
  stood for three verdicts, and records that `DETECTION_THRESHOLD_BAND = 0.05`
  sits 5x above the worst of it. It reconciles with my own fifth-verdict
  measurement (`-0.24 / +0.31 / -0.03 / +1.00 / -0.03 / +0.04 %`).

- **13. R6 -- still open**, correctly listed. `pin_threads` is called only from
  `tests/verification/rung3/test_determinism_pins.py`. Inherited from an ungated
  step 3; step 5's.

- **14. R16 -- still open**, correctly listed. `equilibrate` takes `abs()` of the
  diagonal; a note for step 12, when `k_g` can make a diagonal negative.
  Unchanged, and correctly unchanged.

- **15. R25, R30, R31, R32, R33 (outside G2.2), R36 -- still open, in step 4a.**
  Accepted on the same reasoning the fifth verdict accepted the narrowing.
  `F2a.md` is unchanged this step, which is right: nothing in it is built.

## Findings

**R45. (blocking) `SOLVE_RESIDUAL`'s recorded reason for restricting its own
domain is a causal claim, and a controlled measurement refutes it. The wrong
diagnosis is written as a standing instruction to the next reader.**
`floatfea/tolerances.py:449-458`, repeated at
`tests/verification/rung1/test_patch_test.py:655-659`. The entry says the
residual "is conditioning-limited, and `cond(K_ff)` is a property of the unit
system, so this ceiling is a metre-scale number", publishes `S=1e-3 ->
2.3036e-13` against `S=1 -> 1.7295e-15`, restricts the test to `S = 1` on that
basis, and instructs: "**Do not parametrise it over `GATE_UNIT_SCALES` without
first deciding what the ceiling means at `S = 1e-3`**, where `cond(K_ff) =
5.98e8` against `9.21e2` at metres -- six orders of conditioning buying two and a
half orders of residual is the expected behaviour of a direct solve, not a
defect."

The ablation is one loop and it is not in the diff. `cond(K_ff)` is a property of
the *matrix*, so it is identical for all six states at a given scale. Hold it
fixed and vary the state:

```
state           S=1e-3 resid   (||K||.||u||/||f||)    S=1 resid    S=1e3 resid
axial            3.538e-16     ( 8.53e+00 )           5.931e-16    6.914e-15
curvature        1.935e-15     ( 2.26e+04 )           1.056e-15    1.307e-16
twist            2.304e-13     ( 2.57e+08 )           1.468e-15    9.341e-16
shear            2.494e-15     ( 2.04e+04 )           1.729e-15    2.826e-16
curvature_xz     2.123e-15     ( 2.26e+04 )           7.471e-16    1.537e-16
shear_xz         1.964e-15     ( 2.04e+04 )           1.137e-15    2.919e-16
cond(K_ff)          5.983e+08                          9.210e+02    4.049e+07
```

**Five of the six states at `S = 1e-3` sit at ~2e-15, at the very conditioning
that is blamed.** The whole effect is the `twist` cell, whose right-hand side
norm collapses: `||K||.||u||/||f||` is `2.57e+08` there against `2.57e+02` at
metres. The entry's own second data point refutes it as well: `S = 1e3` carries
`cond = 4.05e7`, four orders above metres, and its worst residual is `6.9e-15`,
4x metres rather than two and a half orders.

Measured with the standard backward-error normalisation instead,
`||Ku-f|| / (||K||.||u|| + ||f||)`, **all eighteen cells are at or below
`6.76e-17`**. The solve is backward-stable at every scale in every state, so
there is no conditioning story to tell. What there is: `SOLVE_RESIDUAL` is
relative to `||f||`, a denominator that varies by **eight orders** across the
twelve cells the gate runs. That is the ninth guard, inside the entry written in
this step to answer the ninth guard.

It matters beyond wording. The gate asserts the field at `S = 1e-3`; the
diagnostic whose stated purpose is that "nothing above this line is
interpretable" is absent at exactly that scale, and the recorded reason tells the
next reader the absence is physics rather than a normalisation choice.
**Closed when** the entry and the test docstring say what was measured -- one
state, at one scale, through a collapsing `||f||`, not the conditioning -- or the
ceiling moves to a quantity that does not vary with the unit system, in which
case the test runs at all three scales. The loop above is the whole cost.

**R46. (blocking) The slenderness boundary R43 asked for does not exist, it
contradicts the table three lines above it, and `F2.md` §D7 item 5 has already
turned it into an obligation on F3.**
`floatfea/tolerances.py:336-337`: "Bisected, the boundary is `D = 0.0791 m`,
element `L/r = 119`." Three lines above, the same block records `D = 0.10`,
`L/r = 94.4` as a **BREACH**. A boundary at `D = 0.0791` and a breach at
`D = 0.10` cannot both hold. The number was carried across from the fifth
verdict's `D = 0.078 / L/r ~ 121` -- which was mine, and wrong for the same
reason -- rather than regenerated, which is what `CLAUDE.md` §Step gating
requires; and bisection is not applicable to this quantity in any case.

The error is **not monotone in slenderness**. Sweeping `D` finely at `D/t = 50`,
worst over six states and both orientations:

```
   D      L/r      worst           D      L/r      worst
 0.0750  125.8  8.967e-13        0.1050   89.9  8.076e-13
 0.0800  117.9  1.028e-12  B     0.1100   85.8  2.273e-13
 0.0850  111.0  5.662e-13        0.1150   82.0  1.127e-13
 0.0900  104.8  8.342e-13        0.1200   78.6  1.010e-12  B
 0.0950   99.3  4.638e-13        0.1250   75.5  1.733e-13
 0.1000   94.4  1.762e-12  B     0.1300   72.6  2.071e-13
```

Three breaches with clean points between them. My own bisection on the same
predicate returns `D = 0.1011`, `L/r = 93.3`; the implementer's returns
`D = 0.0791`, `L/r = 119`; neither is a property of the code, because the
quantity is round-off scatter riding a slow trend.

**The consequence runs in the unsafe direction and it is now in the locked plan.**
`F2.md` §D7 item 5 writes "the ceiling is breached at `L/r ~ 119` (bisected;
`1.76e-12` at `L/r = 94.4`)" -- self-contradictory in one sentence -- and then
hands F3 a named dependency: "assert that every member's element slenderness lies
inside the range G2.2's tolerance was validated over, and fail the build if it
does not." A builder coding that rule from this text admits `L/r = 78.6`, which I
measure at `1.010e-12`, localised exactly where the entry says it would be: skew,
axial, rotational DOF, with the axis-aligned value at the same section at
`3.364e-16`.

Two further operating-point problems in the same paragraph, conservative in
effect but wrong as written:

- `lambda = 46.4` from `F2.md` §5 is a **member** slenderness, `L/r` of a whole
  brace at `D_max = 0.877 m`. The sweep's axis is **element** `L/r`, at fixed
  element lengths `0.79-3.27 m`. Different quantities. A `D = 0.877 m` brace has
  element `L/r ~ 11`, stockier than the posed geometry, so the true margin is
  better than claimed and "no F2 gate is affected" stands -- but not for the
  reason given, and F3's assertion has to be in the quantity F3 computes.
- The quoted `1.57e-13, 6x of margin` is the `D = 0.20 / L/r = 47.2` row read
  across to `lambda = 46.4`. At element `L/r = 46.40` I measure `3.345e-13`,
  **3.0x**, and neighbouring samples move by 3x. One draw of a scattering
  quantity, quoted as a margin.

**Closed when** `tolerances.py` and `F2.md` §D7 item 5 state what was measured --
a region over which the ceiling is *not* reliably held, with the breaching
samples listed -- instead of a boundary, and the F3 obligation is written against
a limit no measured sample breaches (from my sweep, element `L/r <= 50` is clean
at `<= 1.6e-13`) in the quantity F3 will actually compute.
`tests/corpus/g22_model_configurations.txt` carries seven slenderness entries,
three of them measured breaches, as the data for that.

**R47. (blocking) "The resultant channel is 6.4x the more sensitive" is a
response ratio standing where a decision ratio is meant, and inverting the rule
turns it upside down.**
`floatfea/tolerances.py:530-533` and `docs/milestones/F2.md:848-852`. `F2.md`
draws the conclusion explicitly: "The resultant channel is **6.4x the more
sensitive**, which is why it is added beside the field check rather than instead
of it."

`6.4x` is the ratio of raw responses to one `1e-6` defect (`6.90e-7` against
`1.08e-7`). It is arithmetically right and it decides nothing, because the two
channels are compared against ceilings a **thousand times** apart. Solving for
the boundary instead of sampling one side of it -- bisection on each shipped
predicate for the smallest single-element relative stiffness defect it detects:

```
state           via field (err <= 1e-12)   via resultants (err <= 1e-9)   ratio
axial                    9.175e-12                    1.450e-09          158.0x
curvature                9.260e-12                    1.442e-09          155.7x
twist                    9.170e-12                    1.450e-09          158.1x
shear                    8.452e-12                    1.253e-09          148.2x
curvature_xz             9.287e-12                    1.442e-09          155.3x
shear_xz                 8.497e-12                    1.253e-09          147.4x
```

**As a gate the resultant channel is ~150x weaker, not 6.4x stronger.** The entry
is worth keeping -- it is a different quantity, and the sign mutations show it
catches defects the field check cannot -- but that is the argument, and it is not
the one written. A reader deciding which channel to trust, or which ceiling to
tighten first, is being told the opposite of what the code does.
**Closed when** both sites carry the measured detection thresholds beside the
response figures, and the reason for keeping the channel is the one the
measurements support -- a distinct quantity, verified against statics, four of
five planted table defects caught -- rather than sensitivity.

**R48. (blocking) `RESULTANT_EXACTNESS` can be widened a hundredfold in silence.
The new entry shipped without the guard R38 was gated for, one entry over.**
I ran the mutation: `RESULTANT_EXACTNESS: 1e-9 -> 1e-7` gives **`366 passed`**.
Its only live guard is `test_the_ceiling_sits_below_its_counter_case`, at
`6.8e-7` -- **680x** of free widening. For contrast `PATCH_TEST_EXACTNESS` now
reddens at `+5.0%`, and `SOLVE_RESIDUAL` at `10x` (`1e-13 -> 1e-12` gives 2
failed). Tightening: `1e-10` is silent, `1e-11` reddens; the worst measured is
`4.558e-11`. The live band on this ceiling is therefore `[4.6e-11, 6.8e-7]`, four
orders wide, and `1e-9` is pinned nowhere inside it.

This is the defect R38 was gated for, in a value created in the same step that
fixed R38. The `_COUNTER` protocol asks for "the smallest defect the same
assertion detects"; `6.8e-7` is the response to one arbitrary `1e-6`
perturbation, and the smallest defect the assertion actually detects is
`1.45e-9`, from R47's table.
**Closed when** the entry carries that inverted number and something in the suite
reddens when the ceiling moves by a factor that matters. The cheapest form is
already in the file: a per-state recorded response asserted through
`assert_close` against a declared band, i.e.
`test_the_measured_detection_threshold_still_holds` with `res_err` in place of
`err`.

**R49. (recordable) `SOLVE_RESIDUAL_COUNTER = 9.9e-13` is 9.9x above the defect
its own assertion detects, and it is a perturbation size rather than a
threshold.**
`floatfea/tolerances.py:474-485`. The entry says the counter is "set just under
the last" of a four-decade table -- i.e. just under `1e-12` -- and calls the pair
"7.7x above the ceiling, the tightest pair in this file". Bisecting the shipped
predicate: the smallest relative solution error that puts the residual above
`1e-13` is **`1.0025e-13`**, so the assertion is about 10x sharper than its
counter declares. Separately, the constant is consumed as the *size of the
perturbation* (`test_patch_test.py:701`) while the threshold in the assertion is
`SOLVE_RESIDUAL` itself -- a different contract from every other `_COUNTER` in
the file, where the constant is the value a response must exceed. Both are in the
conservative direction; neither is what the suffix means.
**Closed when** the entry records `1.0e-13` as the measured detection threshold
beside `9.9e-13`, or the constant is renamed to say it is a perturbation.

**R50. (recordable) The report's opening claim about itself is false in three
places, and each is checkable in one line.**
`docs/reports/F2/step-4.md:623-625` -- "Every figure below was regenerated by one
run of the shipped harness at the final commit; none is carried from a working
note or from the verdict." Under BF0 that is a sentence stating a fact about the
repository, so it takes the same treatment as the others:

- `:731` gives "all six ... FAILED (`14 failed, 24 passed`)" and `:733-734`
  "`1e-12 -> 1e-11: 6 failed, 295 passed` and `1e-12 -> 1e-13: 6 failed, 295
  passed`". At HEAD I measure **20 failed / 79 passed** (file scope), **6 failed
  / 360 passed**, and **7 failed / 359 passed**. `295 + 6 = 301` is the test
  count at `9f9537f`, not at `15bbc3b`. The `1e-13` case gains a seventh failure
  at HEAD -- the gate node itself -- which is a *stronger* result than the one
  reported.
- `:722` cites the surviving `equilibrat` hits at `:721, :723, :756`. At HEAD
  they are at `:819-821` and `:854`.
- `:715` cites `726550a` for R37a. `git merge-base --is-ancestor 726550a HEAD` is
  false: it is a pre-rebase twin of `6f321a9` with identical content, so the
  citation resolves to an object but not to the history. The seventh guard says
  every citation resolves; this one resolves to a dangling commit.

All three are consistent with the prose having been written mid-step and not
re-run at `15bbc3b`. Nothing is wrong with the underlying work, and every
property they claim does hold.
**Closed when** the three figures are what the commands print at the report's own
commit, or the sentence is narrowed to say each figure was taken at the commit
that made its change.

**R51. (recordable) The module a reader opens still says FOUR in its first line.**
`tests/verification/rung1/test_patch_test.py:1` -- "the patch test. FOUR
constant-strain states, all EXACT (AW4)" -- against `:35` "so there are six in
total" and the function correctly renamed to
`test_the_six_constant_strain_states_are_EXACT`. R15's content was that "four"
was stale where a closure evidence row would cite it; the title line is where a
reader looks first. One word.

**R52. (recordable) `PATCH_TEST_EXACTNESS_COUNTER`'s entry opens with a paragraph
its own next paragraph refutes.**
`floatfea/tolerances.py:409-414`: "at 1e-6 the four states move by 1.09e-07
(axial), 1.09e-07 (twist), 3.72e-08 (curvature) and 3.02e-08 (shear). The counter
is set at the SMALLEST of those" -- the smallest listed is `3.02e-08` and the
value is `1.0e-7`. The paragraph five lines below says those two figures were
understated by the pre-R2 measure and that all six now respond at `1.08e-07 ..
1.17e-07`. Read top-down the first paragraph is false, and it is the paragraph a
hurried reader stops at. Same species as the four the fifth verdict found. Also
still absent here, though R43 got it for the ceiling: the operating point. I
withdrew R15's stubby evidence for it by measurement (Carried 9), so what is left
is that `1.0764e-07` belongs to one mesh and one section and should say so in one
clause.

**R53. (recordable) `section.I_y` can be deleted from the element formulation and
all 366 tests pass. The blindness register added at R44 is the place that should
say so.**
Mutation, run and restored: replacing `section.I_y` with `section.I_z` at
`floatfea/element/beam.py:73` and `:152` gives **`366 passed`**. The reason is
structural rather than accidental -- `basis._KAPPA_BY_SHAPE` knows only
`thin_tube` and `solid_circular`, and `Section.__post_init__` refuses
`I_y != I_z` for both -- so no section the repository can construct distinguishes
the two bending inertias. It shows up inside this step too: of my five planted
mutations of `_exact_resultants`, the only one that stays green is
`ei_y -> ei_z`. The limitation is recorded honestly at
`tests/unit/test_transform_invariance.py:179-190`, for roll invariance. It is not
recorded in the patch test's new "What this gate is BLIND to" section, which
after `08ca53c` is where a reader goes for exactly this question and which names
only `kappa`.
I confirmed the element is not at fault: forcing an `I_y = 2 I_z` section past
the type guard and running all twelve cases gives worst field `3.037e-14` and
worst resultants `5.882e-13`, both green.
**Closed when** the blindness section names the `I_y == I_z` restriction and the
mutation result alongside `kappa`.

**R54. (recordable) The gate never poses the orientation the platform is made
of.** `AXIS_ALIGNED` and `SKEW` are the only two directions, neither needs an
`orientation_node`, and `roll_rad` is never non-zero. The platform's spars are
vertical. I ran what the gate does not, and the news is good in both directions:
a member along `+z` or `-z` with no orientation node **raises**
`DegenerateMemberOrientation` rather than defaulting, which is correct and is the
tenth guard satisfied; with `orientation_node = (5,0,0)` all six states hold at
worst field `4.630e-15` and worst resultants `1.525e-13`, and both negative
controls still fire (`1.0764e-07`, `6.8976e-07`); `roll = 0.3, 1.0, pi/4` hold at
`8.75e-15 .. 2.46e-14`. Recorded as coverage, not as a defect, and seeded into
`tests/corpus/` so it is scored rather than re-derived next time.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `RESULTANT_EXACTNESS` | -- | `1e-9` | relative, scaled per element by that element's largest analytic resultant; dimensionless | `6.8e-7`, consumed by `test_a_perturbed_element_BREAKS_the_recovered_RESULTANTS` and `test_a_TRANSPOSED_TRANSFORM_on_one_element_breaks_every_state` | `tolerances.py:489-521`, `F2.md:812-857`. Form correct. Worst measured reproduces exactly through my harness (`2.892e-11 / 4.558e-11 / 1.525e-13 / 3.921e-13 / 2.900e-13 / 1.484e-12`), so `21.9x` is right. Two defects: the counter is a response to one perturbation rather than the detection threshold, which I measure at `1.45e-9` (**R47**), and the ceiling admits a 100x silent widening (**R48**). The reference the channel compares against is CORRECT -- I re-derived all six states from statics -- and its sign convention is guarded: four of five planted table mutations redden 8 nodes each. |
| `RESULTANT_EXACTNESS_COUNTER` | -- | `6.8e-7` | relative, dimensionless, same quantity as the assertion | -- | Consumed. Margin re-measured at HEAD: smallest of six responses `6.8976e-07` against `6.8e-7`, **+1.4%**. Thinner than the field counter's `+7.6%` and stated nowhere as a margin. |
| `SOLVE_RESIDUAL` | -- | `1e-13` | relative to the load norm, dimensionless -- but that denominator varies by eight orders across the twelve cells the gate runs, which is why the entry had to restrict its own domain (**R45**) | `9.9e-13`, consumed as a PERTURBATION SIZE at `test_patch_test.py:701`; the assertion's threshold is the ceiling itself | `tolerances.py:434-471`. Guard bites at `1e-12` (2 failed); `1e-14` is silent, so `58x` of claimed headroom is `5.8x` of used headroom. The stated reason for the domain restriction is refuted by a one-loop ablation (**R45**) and the counter sits 9.9x above the measured detection threshold (**R49**). |
| `SOLVE_RESIDUAL_COUNTER` | -- | `9.9e-13` | relative, dimensionless | -- | See R49. |
| `PATCH_TEST_EXACTNESS` | `1e-12` | `1e-12` (unchanged) | relative, dimensionless | `1.0e-7` | `tolerances.py:305-407`, rewritten for the operating point. The unit-scale table and the slenderness table both reproduce through my own harness. The `L/r = 119` boundary does not (**R46**). Now genuinely guarded in both directions: `+5.0% / -4.1%`, measured by inversion. |
| `PATCH_TEST_EXACTNESS_COUNTER` | `1.0e-7` | `1.0e-7` (unchanged) | relative, dimensionless | -- | Margin `+7.6%` now written down, so R15 is answered. Opening paragraph stale (**R52**). Survives the stubby case R15 predicted it would fail. |
| `DETECTION_THRESHOLD_BAND` | `0.05` | `0.05` (unchanged) | relative, dimensionless | `0.25`, still unused (4a) | `tolerances.py:600-631`. **It now decides its assertion**, which is R38. The fifth verdict's withdrawal of "margin 5x" is superseded: measured band `+4.50 .. +5.47%` above and `-5.01 .. -5.95%` below, per state. |
| everything else | -- | unchanged | -- | -- | Four `+` lines declaring `Final[float]`, zero `-` lines, in `1103d20..HEAD`. Confirmed independently by parsing both revisions with `ast` and diffing the name-to-value maps: four names added, none removed, **no value moved**. |

No tolerance was widened. No golden file moved. No test is skipped or `xfail`ed;
the suite has zero skips, and the ACCURACY parametrisation resolves to real
entries -- both new ones are collected
(`test_accuracy_tolerances_have_a_counter_case[SOLVE_RESIDUAL]` and
`[RESULTANT_EXACTNESS]`), so the empty-parameter-set guard holds.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin until:

1. **R45** -- `SOLVE_RESIDUAL`'s entry and
   `test_the_solve_residual_is_a_SOLVE_check`'s docstring say what the controlled
   measurement shows: the `S = 1e-3` excursion is one state, through a collapsing
   load norm, not the conditioning, and every cell is backward-stable at
   `<= 6.8e-17`. Or the ceiling moves to a quantity that does not vary with the
   unit system and the test runs at all three scales.
2. **R46** -- the `L/r = 119` boundary is withdrawn from `tolerances.py` and from
   `F2.md` §D7 item 5, replaced by the measured samples, and the F3 dependency is
   written against a limit no measured sample breaches, in the quantity F3 will
   compute. The three breaching entries are in
   `tests/corpus/g22_model_configurations.txt`.
3. **R47** -- the `6.4x` sensitivity claim, in both `tolerances.py` and `F2.md`
   §D5, is replaced by the measured detection thresholds for the two channels.
4. **R48** -- `RESULTANT_EXACTNESS` has a guard that reddens when it is widened by
   less than 680x, and its entry carries the inverted number.

R49, R50, R51, R52, R53 and R54 -- together with R6, R16, R25, R30, R31, R32,
R33 (outside G2.2) and R36 -- may be answered in step 5's `Carried` section,
**and that section must list every one of them, open or answered.** This step's
report listed all fifteen carried items for the first time in six rounds. Keep
that.

**Not a STOP.** No rung is red, and no finding this round is an element defect.
The four blocking items are all statements about numbers: a causal diagnosis
refuted by holding conditioning fixed and varying the state, a boundary that
contradicts the table above it, a sensitivity ratio quoted at the wrong operating
point, and a ceiling with no guard. Everything I could think to break, I broke
and it held -- the analytic resultant table re-derived from statics and correct
in all six states; four of five planted sign defects in it caught at eight nodes
each; a vertical member refusing to build without an orientation node and exact
with one; `roll = pi/4`; a section with `I_y = 2 I_z` forced past its own type
guard; two stubby tubes where R15 predicted the counter would fail and it does
not; `PATCH_TEST_EXACTNESS` tightened until it reddens, at `-4.1%`.

The pattern is narrower again and it has moved up one level. Last round it was
sentences about the code that a one-line command refutes; the report has adopted
BF0 and that class is largely gone -- the R39 counts are exact to the unit, the
R44 figures to five digits, the R43 tables to four. What has replaced it is
this: **the numbers are right and the sentences explaining them are the reasoning
that was never measured.** `cond(K_ff)` is quoted correctly and does not cause
what it is said to cause. `6.898e-07 / 1.076e-07` is measured correctly and does
not mean what it is said to mean. The sweep table is exact and the boundary read
off it is not a property of the code. Each is refuted by a controlled cell
costing one loop. The standing question for step 5: *for every "because", "so"
and "therefore" in this diff, what is the cell that holds everything else
fixed?*

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Six
consecutive reviews by one reader. `366 passed` means "not yet contradicted"
until V5.1 puts CalculiX on the other side -- and this round it means slightly
more than last round, because `test_the_measured_detection_threshold_still_holds`
has stopped being an assertion inside the green count that cannot fail.

**Adversarial corpus (BE3): opened this round.**
`tests/corpus/g22_model_configurations.txt`, committed separately in the commit
immediately preceding this one, touching no code. The fifth verdict declined the corpus
on the ground that the one it had in mind scored 4a's undesigned checker; that
reasoning still holds for the scanner, and I have written none of those entries.
What changed is that this step's own gate has a corpus-shaped question -- which
model configurations `1e-12` is claimed over -- and it is answerable now.

**17 entries, all new, all unseen by the implementer. 2 are executed by a shipped
test; 15 are not.** That 2-of-17 is the coverage measurement for G2.2's
configuration space, and it is the number to quote rather than the twelve green
cases. I ran all 15 unrun entries by hand for this verdict: one must raise and
does (`vertical_no_onode`); three are measured breaches inside the region
`tolerances.py` declares valid (`slender_L_r_79`, `_94`, `_118` -- that is R46);
eleven hold. The file is data only -- no imports, one candidate per line, a
header stating what a passing scan means -- and how any entry is exercised
remains the implementer's to design.
