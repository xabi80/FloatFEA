# Review � F2 step 5
Reviewed commit: 67486dfb11504e58fdacae3b3ac3bac62e292ce0
Verdict: HOLD

**Reviewed commit: `44f28e8`.** Report revision 20, `Answers: verdict 45 @
f19eef5`. The `Reviewed commit:` line stamped above this one by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus commit
`67486df` -- not the commit judged. That is R373, still open; read `44f28e8`.

Tests: **2343 passed, 0 failed, 0 skipped** at `44f28e8` (my run, clean tree,
`python -m pytest -q`, 479.59 s, Python 3.13.15 on Windows).

**AT MY OWN CORPUS COMMIT `67486df`: 13 failed** in
`tests/verification/rung1/test_rigid_body_corpus.py`, every one a frame I added
this round. That is the corpus doing the job BE3 gives it, not a pre-existing
red. The thirteen are named below and the next report must name them under
`test_a_RED_suite_is_named_in_the_report`.

**Commits: `7a5445a`, `45ab8ca`, `1b87e03`, `12223c2`, `c149c3e`, `2ffb4b9`;
plan `2698e5c`. Report `44f28e8`.**

**Item 1b.** Revision 20's header at line 7156 reads `Answers: verdict 45 @
f19eef5`; `git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`f19eef598d9586872e69ca4e69865970deb928b7`. It is the latest. **Passes.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT

```
cmd  gh run list --commit 44f28e800ec19aba06c42be0760e89c7d518130f
out  run 34857334208, event push, conclusion SUCCESS
cmd  gh api .../runs/34857334208/jobs
out  "the verification ladder"      success, runner "GitHub Actions 1000001014", 13 steps
     "lint, unit and guards"        success, runner "GitHub Actions 1000001015", 14 steps
     "CI determinism -- leg"        skipped, runner null, 0 steps
     "CI determinism -- ten legs"   skipped, runner null, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I AM JUDGING,
     with the rewritten count in the ladder. Not CK2: runners were assigned
     and steps executed. The determinism pair is dispatch-only and is recorded
     as an UNAVAILABLE check at this commit rather than skipped over.
cmd  gh api .../runs/34852760507/jobs   -- this round's dispatch at `1b87e03`
out  ten "CI determinism -- leg (n)" jobs ALL success with real runners and 13
     steps each; "CI determinism -- ten legs agree" success
     AND: "lint, unit and guards"  FAILURE
cmd  gh run view 34852760507 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  test_the_whole_suite_line_is_about_a_commit_that_exists, the eight
     test_report_guard_states cells that wrap it, and three
     test_every_named_site_is_touched_or_declared rows -- all report-staleness
     guards, red by construction because the answering revision had not landed
     yet. Nothing in `floatfea/` or rung 1.
judge R383 ADVANCED AGAIN AND IS AGAIN NOT CLOSED:
     `git diff --stat 1b87e03..HEAD -- tests/verification scripts .github` is
     one file, `tests/verification/rung1/test_rigid_body_modes.py`, 24
     deletions, and that file is in the rung the legs run. Same shape as last
     round.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff f19eef5..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- no STOP-class finding. Nothing under `.claude/` moved.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                  -- the instruction's own expectation
cmd  git diff f19eef5..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set; no plugin was added, so no
     rung's green is being written by code in its own directory.
cmd  git diff --stat f19eef5..HEAD -- floatfea
out  floatfea/tolerances.py | 164 ++++++--- -- ONE FILE
cmd  git show --name-only on each of the eight commits
out  `2698e5c` touches docs/milestones/F2.md ALONE and says RE-LOCKED. No
     commit mixes process with code.
judge THE TOLERANCE DIFF IS NOT ADDITIVE THIS ROUND and it should not be: Q7's
     count rule changed shape, `RIGID_MODE_GAP` changed both VALUE and
     QUANTITY, and two entries were retired. The value changes arrive in
     `7a5445a` and `1b87e03` together with the rule they serve, which is the
     right place for them -- what `CLAUDE.md` forbids is a tolerance moved to
     rescue a failing test, and no test was failing. The retune of
     `RIGID_MODE_GAP` from `1.5` to `1.3` is the one I do not accept, and the
     reason is measured in R404, not stylistic.
```

## Carried

Verdict 45 held on R394, R395, R396, R397, R398, R399 and carried R388's second
site. **Five are answered. R399 carries. R397's rule is gone and its FINDING
recurs against the replacement, as R403.**

- **R394 -- ANSWERED, at the line, and I reproduce both numbers.**

```
cmd  RB.counter_response("residual"), imported at 44f28e8
out  4.4841e-15  -- and `tolerances.py:315` now says `4.4841e-15`
cmd  bisection on the defect size through the shipped assertion
out  edge 2.2038e-15; 1.0e-14 / 2.2038e-15 = 4.54x, which is what :317 says
judge `about 5e-14` IS GONE AND THE ENTRY SAYS WHY IT WAS WRONG. Closed.
```

- **R395 -- ANSWERED AT BOTH SITES ITS CONDITION NAMED.** `tolerances.py` and
  `test_rigid_body_corpus.py` both carry
  `{{fig:retired_ratio_over_ceiling_on_corpus}}` instead of the word, and
  `grep -rn sixteen` over both files is empty. **Closed.** The sentence the
  figure now sits inside is a new finding, R405, not a re-carry of this one.

- **R396 -- ANSWERED.** (i) The loss is retired, so the plan's "asserted
  against nothing" is true of both -- `grep -rn "RIGID_BODY_SUBSPACE_LOSS"
  tests/ | grep -v COUNTER` finds no `assert`. (ii) `:439`'s "referenced only
  here" is struck. (iii) The count is in the report at §2 (41 of 56 canonical,
  42 here; I measure 42 of 56) and not in the plan. **I accept that:** the
  round measured the figure disagreeing between machines and Q8 forbids
  publishing an exact row that does, so withdrawing it is the rule working
  rather than an omission. **Closed.**

- **R397 -- THE RULE IT INDICTED IS GONE, AND ITS TWO FRAMES BOTH GIVE SIX.**
  I ran both through the shipped gate: `unit=1e-4` gives 6 with a gap of 6.379
  orders, `rb_brace_kilometre` gives 6 at 8.548. Both are now shipped tests.
  **Closed as stated.** The finding recurs one axis over against the
  replacement and is opened fresh as R403 rather than silently re-carried.

- **R398 -- ANSWERED, AND I MEASURED THE THING THAT WAS MISSING.**

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_modes.py -q -s
out  one DOF pinned, over all 30: nullspace dimensions [5], narrowest gap 12.641
     torsional release: nullspace 7, gap 13.627
     _defect(RIGID_MODE_FLOOR_COUNTER_DEFECT): 5 eigenvalues below tau
judge THE COUNT ASSERTION CAN NOW FAIL, which is exactly what R398 said nothing
     in the repository demonstrated. `test_a_LIFTED_rigid_mode_reddens_the_COUNT`
     pins the half it reddens with `match="below tau and G2.1 requires"` and
     `test_a_NARROW_GAP_reddens_the_VALIDITY_assertion` with `match="UNTRUSTWORTHY"`,
     so the two counters cannot be swapped without the meta-test noticing.
     Both controls decide by `zero_modes_below_floor` and both check the gap.
     `:620`'s name matches the assertion it reddens. Closed.
```

- **R399 -- HALF ANSWERED, AND THE HALF THAT IS NOT IS THE SAME SPECIES THE
  ITEM WAS ABOUT. This carries.**

```
judge DONE: both ceilings carry `RETIRED` and a reason;
     `test_a_RIGID_BODY_MODE_that_carries_ENERGY_is_caught` is deleted, so the
     orphan counter that ran a different assertion in a different quantity is
     gone; `tests/test_counters_are_injected.py` no longer registers either.
cmd  sed -n '459,466p;502,509p' floatfea/tolerances.py
out  RIGID_BODY_MODE_RATIO_COUNTER_DEFECT and
     RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT still open with
     "COUNTER-CASE, INJECTED into the assembled matrix and run through the
     gate", and still say "about 31x past the ceiling" and "about 75x past the
     ceiling". Neither carries the retirement note their own ceilings got.
judge THE TWO CEILINGS WERE FIXED AND THE TWO COUNTERS BESIDE THEM WERE NOT.
     There is no gate for either to be injected through and no ceiling to be
     past. This is the condition's "the two retired entries say they are
     diagnostics" applied to the wrong two of the four.
cmd  scripts/regen_figures.py:148 and :154
out  `_floor("rigid_body_counter_ratio", "above", "RIGID_BODY_MODE_RATIO")`
     and the same for the loss -- `--check` still computes a pass/fail margin
     against two ceilings that decide nothing. That was R399's third paragraph
     and is untouched.
```

  **Closed when** the two `_COUNTER_DEFECT` entries carry the same retirement
  note their ceilings carry, and the two `_floor(..., "above", <retired>)`
  marks in `scripts/regen_figures.py` are dropped to `"derived"` or removed.

- **R388 -- ANSWERED, at both lines the condition named.**

```
cmd  git diff f19eef5..HEAD -- tests/test_report_carried.py
out  :1257 now reads "NOTHING UNDER `docs/reports/` HAS ANY HISTORY (R377, and
     R388's second site)" and distinguishes the three states explicitly
out  the assertion message reads "nothing under the reports tree has any
     history to anchor a distance to"
judge BOTH LINES, AND THE TABLE EIGHT LINES ABOVE NOW AGREES WITH THEM. Closed.
```

- **R383 -- ADVANCED, NOT CLOSED.** See the CI block. Ten legs executed and
  agreed at `1b87e03`; one rung-1 file moved after that dispatch.

- **R400, R401, R402 -- OPEN at 4a**, correctly listed in §5. R402 recurs and
  is recorded again below as R411 rather than silently re-carried.

- **R390, R391, R392, R393 -- OPEN at 4a**, correctly listed.

- **R370, R371, R372, R373, R374 -- OPEN at 4a**, correctly listed. R373 bites
  again in this verdict's own header.

- **R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350's second
  half, R330, R331 -- OPEN at 4a, correctly listed.**

- **R231, R244, R245, R275 -- OPEN, unblocked, and the report correctly does
  not claim them.** Step R has not run.

- **R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.** R302 accepted at verdict 37, not reopened.

- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement is unchanged and
  stays at 4a.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** R250, R251,
  R226, R227, R264 and R266 still have no row; R348 territory, unmoved.

- **R365-R369, R375-R382, R384 -- carried in `step-5-answers.json`.** Checked
  the diff; the bookkeeping is right except for R399, which is R410.

- **R332, R223, R224 -- closed at verdict 45**, not reopened.

## Findings

**First, what is right, because it is the larger part of this round.**

**THE COUNT RULE IS A REAL IMPROVEMENT AND R397 IS GENUINELY DEAD.** I put my
own instrument on it. Counting below `tau` instead of below the largest gap
fixes exactly what R397 found, and it fixes it for the right reason -- at
`unit=1e-4` the twelve rotational modes that fooled `argmax` sit at `6e5` to
`4.4e6` units of round-off, hundreds of thousands of times ABOVE the floor, so
a threshold sees them and a gap-finder does not. Over 56 frames the count is
six at every one, and the floor's bracket is real: solved, it is
`(1.461, 60.15)` and `10.0` has `6.84x` below and `6.01x` above. R398 is
answered with measurements rather than argument -- the count assertion can now
go red, at five and at seven, and all four controls decide by the shipped rule.
The residual half I could not break last round I could not break this round
either: worst `1.0589e-16` over my 26 new frames against a ceiling of `1e-15`,
including at `unit=1e8`.

---

**R403. (BLOCKS -- the gap is not the validity condition on the count. On
frames composed from two entries already in the corpus, each of which holds
alone, the count is wrong and the gap certifies it at up to 7.2x its floor; and
on the same one-parameter sweep the gap goes red where the count is RIGHT.)**
`floatfea/tolerances.py:341-342`, `tests/verification/rung1/test_rigid_body_modes.py:250-256`,
`docs/milestones/F2.md` "THE COUNT IS BELOW A THRESHOLD..." in `2698e5c`.

```
code tolerances.py:341 "the gap is the validity condition ON that count and is
                        asserted separately."
code zero_modes_below_floor docstring: "an untrustworthy count fails loudly
                        instead of returning a wrong number."
code plan "when it fails the test reports the count as untrustworthy and goes
          red rather than returning a number it does not believe."
cell THE FORTY-FIFTH VERDICT'S OWN TECHNIQUE, UNCHANGED: take two effects
     already in the file, each holding alone, and pose them together. My own
     instrument, shipped `zero_modes_below_floor` and `residual_exactness`.
out  rb_unit_millimetre (unit=1000, holds, count 6)
     x rb_span_x10000   (stretch=1e4, holds, count 6)
     ->  count 8,  gap 9.359 orders against a floor of 1.3  (7.2x the floor)
         residual 2.6077e-22 -- THE ELEMENT IS CLEAN BY THE GATE'S OWN
         OTHER HALF, five orders below its ceiling
out  rb_unit_10um x rb_span_x100000  -> count 8, gap 5.962   (4.6x)
     rb_unit_0p1mm x rb_span_x1000   -> count 8, gap 7.366   (5.7x)
     rb_heavy_D2p0_t0p2 at mm x1e4   -> count 8, gap 8.367   (6.4x)
     unit=1e8, no composition at all -> count 15, gap 14.025 (10.8x)
judge MILLIMETRES IS NOT AN EXOTIC UNIT. The mildest of these is the metric
     unit an engineer types without thinking, composed with a span factor that
     is already in the file with `expect=hold`.
cell AND THE OTHER DIRECTION, WHICH I DID NOT EXPECT AND WHICH IS THE CLEANER
     REFUTATION. One parameter, stretch, at unit=1000, laddered:
out  stretch  3600 -> count 6 (RIGHT), gap 1.270  -> THE GATE GOES RED
             4000 -> count 6 (RIGHT), gap 1.061  -> THE GATE GOES RED
             4300 -> count 6 (RIGHT), gap 1.187  -> THE GATE GOES RED
             4340 -> count 7 (wrong), gap 0.017  -> gap warns, correctly
             4400 -> count 8 (wrong), gap 8.648  -> gap says TRUSTWORTHY
judge SO THE GAP DETECTS BEING **AT** A TRANSITION, NOT BEING **PAST** ONE.
     That is a true and useful thing for it to detect and it is not what any
     of the three sentences above says it does. A validity condition that is
     wide precisely once the count has finished going wrong is the same
     structure R397 found in the old rule -- "it is the ratio AT the largest
     gap, wherever that is, so it is large precisely when the count is most
     wrong" -- and the round's own reasoning is what makes this blocking
     rather than interesting.
judge WHAT IS NOT WRONG, so the repair is not over-scoped. The count and the
     gap are honest about the MATRIX: at `unit=1e8` two flexible modes really
     are indistinguishable from zero in double precision. What is refuted is
     the claim that the gap guards the count. The thirteen reds are a MEASURE
     failing on a defect-free element, which is the same thing this round
     itself discovered about the largest-gap rule.
```

**Closed when** either the count is made scale-aware -- a per-DOF-block
homogenisation and a nullspace-edge search are the obvious candidates and
neither is my call -- **or** the claim is narrowed to what was measured: the
entry, the docstring and the plan say the gap detects a marginal boundary and
NOT a wrong count, the domain the count is claimed over is stated, and the
thirteen frames I added are given an expectation one way or the other. **Either
answer is fine. What is not fine is three sentences that one composition of two
corpus entries refutes.**

**R404. (BLOCKS -- `RIGID_MODE_GAP` is a LOGARITHM judged by a MULTIPLICATIVE
rule, and the retune that rule forced moved the binding margin from 2.371x to
1.496x, under the repository's own declared platform spread of 1.5x.)**
`floatfea/tolerances.py:375-392` and `scripts/regen_figures.py:99`, `:130`, `:636`.

```
code tolerances.py:377 "Q8's floor class requires a floor-class decision to
     :378              survive the declared platform spread of `1.5x`, and
     :379              `2.071 / 1.3` is `1.59x`."
code regen_figures.py:636  margin = ceil / b if kind == "below" else b / ceil
code tolerances.py:1227, the FIGURE_FLOOR_CLASS_SPREAD entry: "A dimensionless
     FACTOR between two renders of the same figure: max/min ... THE VALUE IS
     INVARIANT UNDER THE FIGURE'S UNITS."
judge IT IS NOT INVARIANT UNDER A LOGARITHM, AND log10 IS NOT A UNIT CHANGE.
     `rigid_mode_gap_orders` is the first log-valued figure in this file. A
     platform factor f on the underlying ratio shifts an ORDERS figure by
     log10(f) -- an ADDITIVE 0.176 for f = 1.5 -- so dividing two orders and
     comparing the quotient with 1.5 compares a ratio of logarithms with a
     spread of ratios.
cmd  the margins computed consistently, in the quantity the platform perturbs
out  floor 1.50 : clean 10^(2.071-1.50) = 3.724x  counter 10^(1.50-1.125) = 2.371x
     floor 1.30 : clean 10^(2.071-1.30) = 5.902x  counter 10^(1.30-1.125) = 1.496x
judge THE FIRST VALUE WAS THE BETTER ONE AND THE CHECK REFUSED IT ON A UNIT
     ERROR. At 1.5 both sides clear the declared spread. At 1.3 the clean side
     gains room it did not need and the COUNTER side drops to 1.496x -- under
     1.5, which is the exact sentence the checker prints when it refuses
     something: "the platform alone could carry this decision across its
     ceiling". The entry publishes this margin as `1.50` at :399 ("a factor of
     `1.50` narrower than the floor allows"), rounded up across the boundary.
judge AND THE STALENESS HALF, SAME CAUSE. The spread column for
     `rigid_mode_gap_orders` read `13.655 vs 13.763 -> 1.0079x` in my run; the
     underlying ratios are 4.52e13 and 5.79e13, a 1.28x spread. The guard's
     sensitivity on a log-valued row is reduced by roughly the row's own
     magnitude. Nothing tripped this round; the guard is nonetheless not doing
     on this row what its own entry says it does.
judge THE INVOCATION ASKS ME TO PUT THE CHECKER'S REFUSAL ON THE RECORD AS THE
     THING WORKING. I cannot, as stated. The refusal was real, the response to
     it was conscientious, and the rule it applied was the wrong rule for the
     quantity -- which is why the value moved in the direction that weakens
     the counter. That IS the arrangement working, one level up: a mechanical
     check that cannot see its own units is exactly what a reviewer is for.
```

**Closed when** the floor-class comparison for a log-valued figure is done in
the quantity the spread is declared on -- either `_floor` gains a kind that
compares `10**value`, or the two gap-in-orders rows are published as ratios and
the tolerance stays an orders threshold -- **and** `RIGID_MODE_GAP` is
re-chosen with both margins computed the same way, with the counter's margin
stated against `FIGURE_FLOOR_CLASS_SPREAD` rather than rounded to it. One
function and one number.

**R405. (BLOCKS -- the sentence R395 repaired now carries a corpus size and a
quantifier that the figure inside it refutes: "twenty-eight frames" and "a
large minority" against a rendered `34 of 56`, which is a majority.)**
`floatfea/tolerances.py:293-297` and `:424-427`.

```
code :294 "the reviewer's corpus of twenty-eight frames showed what that
     :295  measures: a large minority of them exceed its ceiling ... the count
     :297  is `{{fig:retired_ratio_over_ceiling_on_corpus}}`"
code :424 "it exceeds this ceiling on a large minority of the reviewer's
     :425  fifty-six frames"
cmd  grep -c "^id=" tests/corpus/g21_rigid_body_frames.txt   (at 44f28e8)
out  56
cmd  grep retired_ratio_over_ceiling_on_corpus docs/milestones/F2_figures.md
out  | `retired_ratio_over_ceiling_on_corpus` | 34 of 56 |
cmd  my own loop over the corpus with the shipped mode_ratio
out  34 of 56 -- I reproduce it exactly
judge 34/56 IS 61 PER CENT. "A large minority" is false of the number the same
     sentence renders, and "twenty-eight frames" is false of the file. R395's
     condition was "carry the rendered figure by name", which was met -- and
     the prose written AROUND the repair inherited none of the discipline
     applied to it, which is CP2's species named in `CLAUDE.md` almost
     verbatim. The plan has the same pair: `docs/milestones/F2.md` still says
     the corpus "poses twenty-eight frames" and "a large minority of those
     frames", in a section re-locked at `2698e5c`.
```

**Closed when** the three sites say sixty-one per cent, or "most", or nothing
quantitative at all beside the figure, and the corpus size is read from the
file rather than typed. `{{fig:rigid_mode_corpus_frames}}` already exists.

**R406. (BLOCKS -- the RE-LOCKED plan describes the gap's counter as a uniform
elastic foundation; the shipped counter is a nearly-released connection, and
the shipped code's own docstring says the foundation DOES NOT WORK under this
rule.)** `docs/milestones/F2.md`, last paragraph of "G2.1 in the residual
form", in `2698e5c`.

```
code plan "The gap's counter is a uniform elastic foundation: it lifts all six
          rigid modes together, so the COUNT does not move and the gap is what
          degrades ... What makes it the gap's counter is that it is sized on
          the gap."
code the docstring of `_nearly_released`, which replaced it: "A UNIFORM
          FOUNDATION WAS THE FIRST ATTEMPT AND IT DOES NOT WORK UNDER CS0's
          RULE. It lifts all six rigid modes together, so nothing is left
          below `tau` and the COUNT fails instead of the gap -- measured at
          every size from `1e-12` to `1e-7`."
cmd  grep -n "_foundation" tests/verification/rung1/test_rigid_body_modes.py
out  (nothing -- the function is deleted)
judge THE PLAN AND THE CODE CONTRADICT EACH OTHER IN THE SAME ROUND, and the
     plan's version is the one the code went out of its way to record as
     refuted. `2698e5c` edited the paragraph four above this one and left this
     one. This is R396 exactly -- a false sentence in a RE-LOCKED plan,
     refuted by one grep -- one round later.
judge AND THE SECTION BELOW IT IS WORSE. "G2.1's two quantities, added at step
     5 (V1.1)" is untouched and still presents the two RETIRED ceilings as the
     gate: a headroom table ("~83x", "~18x"), "Both counters are ONE injected
     defect", and "Both are registered in `tests/test_counters_are_injected.py`
     and pass its two cells". Neither is registered -- `7a5445a` removed both
     cells and the file says so in a comment.
```

**Closed when** the counter paragraph describes the counter that ships, and
the "G2.1's two quantities" section either says at its head that everything in
it is the retired form, or is cut to the record the retired entries already
keep. The figures in it (`~83x`, `~18x`, "two cells") are regenerated or
withdrawn in the same commit, per BP0.

**R407. (BLOCKS -- the gate file's own header says it asserts the thing this
round deleted, and calls both retired quantities "BOTH GATED".)**
`tests/verification/rung1/test_rigid_body_modes.py:3-25`.

```
code :4  "This file asserts that, and it asserts it on the SUBSPACE rather
     :5   than on the mode shapes, per the lock's AP3."
code :13 "the six ANALYTIC rigid-body vectors lie in the computed span, and
     :14  that is what is asserted."
code :16 "TWO QUANTITIES, BOTH DIMENSIONLESS, BOTH GATED"
     :18   1. `RIGID_BODY_MODE_RATIO` ...
     :23   2. `RIGID_BODY_SUBSPACE_LOSS` ...
cmd  grep -n "assert" over the file, for either name
out  neither appears in any assertion.
     `test_the_analytic_rigid_body_vectors_are_SPANNED` was deleted in
     `7a5445a`.
judge THE FIRST TWENTY-FIVE LINES A READER OF THIS GATE MEETS DESCRIBE A GATE
     THAT WAS REPLACED IN THE SAME COMMIT. `CLAUDE.md` records this exact
     species -- "a module docstring describing a `tests/` tree it did not
     match" -- as one of the five findings that earned BF0. The tolerance
     entries were carefully repaired; the file header they belong to was not
     read.
```

**Closed when** the header names the three quantities that are gated -- the
residual, the count, the gap -- and says the ratio and the loss are retired
diagnostics, with AP3's argument attached to the residual, which is where it
now lives and is a stronger form of it.

**R408. (BLOCKS -- a sentence added THIS ROUND to answer R399 is refuted by one
grep, and it is the sentence that licenses leaving the counter entry alone.)**
`floatfea/tolerances.py:420-422`.

```
code :420 "The quantity is computed and printed by
     :421  `test_the_eigenvalue_RATIO_is_a_diagnostic_and_not_a_gate`, and its
     :422  counter constant is referenced by nothing."
cmd  grep -rn "RIGID_BODY_MODE_RATIO_COUNTER_DEFECT" --include=*.py .
out  floatfea/tolerances.py:466                       (the definition)
     tests/verification/rung1/test_rigid_body_modes.py:78    (imported)
     tests/verification/rung1/test_rigid_body_modes.py:358   (the size dict in
                                                              counter_response)
judge REFERENCED AT TWO SITES, ONE OF THEM A LIVE DISPATCH TABLE.
     `counter_response("ratio")` still injects it and returns `mode_ratio(k)`,
     and `scripts/regen_figures.py:148` still renders that response as
     `rigid_body_counter_ratio` with a pass/fail against the retired ceiling.
     The claim is one `grep` from being checked and it was not run.
```

**Closed when** `:422` says where the constant is referenced, or the two
references go with it. This is the same command R399 asked for, run.

**R409. (BLOCKS -- two test functions were deleted and the golden regenerated
with no golden-change explanation, and one of them is the assertion the plan
still calls the one AP3 asks for.)** `tests/goldens/collected_tests.txt` in
`7a5445a` and `12223c2`; `docs/reports/F2/step-5.md` revision 20.

```
cmd  git diff f19eef5..HEAD -- tests/goldens/collected_tests.txt
out  -test_a_RIGID_BODY_MODE_that_carries_ENERGY_is_caught
     -test_the_analytic_rigid_body_vectors_are_SPANNED
     -test_a_CLOSED_GAP_reddens_the_COUNT_assertion      (renamed)
     -test_a_LOST_rigid_body_DIRECTION_is_caught         (renamed)
     -test_the_ZERO_MODES_NUMBER_SIX_by_the_spectral_gap (renamed)
     plus four new corpus controls, [tests] 322 -> 324
code the golden's own header: "A FUNCTION disappearing is what this file
     exists to catch."
cmd  grep -in "golden" over revision 20
out  three hits, all inside the generated tables of sections 7 and 8, about
     R401 and R402. There is no golden-change section.
judge CLAUDE.md, Testing: "Golden-file changes require a written explanation
     of why the numbers moved. Regenerating a golden file to match new output,
     without that explanation, is the same error as widening a tolerance."
     Three of the five removals are renames and are benign. Two are DELETIONS
     OF ASSERTIONS and one of those is G2.1's subspace half. Section 2
     disposes of the first in a subordinate clause ("that test is deleted")
     and never mentions the second at all.
judge THE SUBSTANCE IS DEFENSIBLE AND I WANT THAT RECORDED: the residual
     assertion is a STRONGER form of the subspace claim -- basis-free,
     eigenvector-free, and it says the analytic vectors are in the numerical
     nullspace rather than merely in a computed span. AP3 is better served
     after the deletion than before. What is missing is anyone SAYING so, and
     `docs/milestones/F2.md` still says the opposite: "without it G2.1 would be
     six numbers near zero with nothing said about what they are modes *of*."
```

**Closed when** the report carries a golden-change section naming both deleted
functions and why each went, and the plan sentence that requires the subspace
assertion is rewritten onto the residual. The argument is already made in the
tolerance entry; it is not made where the golden rule and the plan need it.

**R410. (recordable, 4a) The report says R399 is answered in section 9 and its
own generated Carried table says it is not.** `docs/reports/F2/step-5.md`
section 8 carries the row `| R399 | **open** -- blocking, and not answered in
this round |` against section 9's "R396, R399 -- ... both entries say they are
retired, and the orphaned counter is gone". `step-5-answers.json` has no `R399`
key, so `carried_table.py` defaulted it. The table is the mechanism that exists
so the dependency list is not skipped; a blocking item with two statuses in one
document is the one thing it must not produce.

**R411. (recordable, 4a) Section 9's `git log --oneline` block drops a commit
that touches `floatfea/tolerances.py`.** `git log --oneline f19eef5..HEAD`
prints eight rows at the report's own commit; the block lists six and accounts
for a seventh ("this revision's own commit follows"). The missing row is
`2ffb4b9`, whose diff is `floatfea/tolerances.py | 9 +++++++--`. Section 6
names that same commit two sections earlier, so the omission is in the block
and not in the knowledge. **Fourth round running for this block** (R391, R402).

**R412. (recordable, 4a) Section 0a names this round's dispatch and reports
three green jobs from a run whose conclusion is `failure`.** `gh run list`
gives run `34852760507` at `1b87e03` conclusion **failure**: "lint, unit and
guards" failed. Every sentence in 0a is true and the failures are
report-staleness guards red by construction mid-step -- but a CI section that
names a run by id under a green table and does not give its conclusion is
under-reporting the one check neither of us controls. One line.

**R413. (recordable, 4a) `RIGID_MODE_FLOOR`'s window is sampled, not solved,
and the sampled claim overstates it by about 1.5x.** `floatfea/tolerances.py:349`
says "The window is a decade wide on each side and this sits in it", from
readings at 1 and at 100. Solved over the same 56 frames -- the max of the
sixth homogenised eigenvalue and the min of the seventh, one loop -- the window
is `(1.461, 60.15)`: `6.84x` below and `6.01x` above. The value is well inside
it and nothing about the choice is wrong; the published margin is. "Invert the
decision rule and solve" is the rule and the loop is three lines.

**R414. (recordable, 4a) The pin and release controls now exist twice.**
`test_ONE_PINNED_DOF_leaves_FIVE` and
`test_a_PINNED_DOF_leaves_FIVE_below_the_floor` pin the same 30 DOFs by the
same rule in two files, and the release pair does the same. Duplication, not a
defect; but the second pair carries none of the first pair's premise assertions
about its own geometry, which is the half that made the release control worth
more than the gate it guards.

## Tolerances touched

**One file, `floatfea/tolerances.py`, `+164 -270` across `7a5445a`, `1b87e03`
and `2ffb4b9`. Two values retired, one renamed and requantified, two added.**

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| `RIGID_MODE_FLOOR` | -- | `10.0` | **dimensionless multiplier** on the matrix's own round-off floor; `tau = FLOOR * norm(K_hat) * eps` on `K_hat = K/max-abs-K`, so the threshold carries the matrix's units and the comparison does not | `RIGID_MODE_FLOOR_COUNTER_DEFECT = 1.0e-12`, injected through `assembled`, decided by the shipped count assertion, pinned by `match="below tau and G2.1 requires"`. **I confirmed it takes the count to five**, and that `counter_response("floor")` returns a SOLVED widened floor, `735.2`, not a typed one | `:344-349` plus my own loop. **The value is sound and I could not break it: solved window `(1.461, 60.15)` over 56 frames. R413: the entry says "a decade on each side", which is `6.84x` and `6.01x`.** |
| `RIGID_MODE_FLOOR_COUNTER_DEFECT` | -- | `1.0e-12` | relative defect, a fraction of `max-abs-K` on one translational diagonal | n/a | `:354-358`. The entry says the crossing is "between `1e-14` and `1e-12`"; I measure it between `1e-14` and `3.16e-14`, so the statement is true and loose. The solved margin is the registry's `735.2 / 10 = 73.5x`, which is the right form. |
| `RIGID_MODE_GAP` | `1.0e06` (a RATIO) | `1.3` (ORDERS) | **the quantity changed, not only the value**: `log10(first_above / last_below)` | `RIGID_MODE_GAP_COUNTER_DEFECT`, a nearly-released connection, injected through `assembled`, pinned by `match="UNTRUSTWORTHY"` so the count half cannot be what reddens. **Its arithmetic I reproduce exactly: `1.125070` orders.** | `:372-392`. **R404: the bracket's upper end is a ratio of logarithms compared with a spread declared on ratios, and the retune it forced leaves the counter at `1.496x` against a declared `1.5x`. R403: the quantity does not do what the entry says it does.** |
| `RIGID_MODE_GAP_COUNTER_DEFECT` | `1.0e-07` | `8.318e-15` | relative, on the released member's extra rotational DOF | n/a | `:394-408`. **The claim that no injection reaches a narrower separation at count six survived my own 200-point scan** -- my coarser grid bottoms out at `1.1465` and the shipped value gives `1.1251`. The reasoning for a counter near its own edge is correct and well argued; the MARGIN it has is the finding, not the placement. |
| `RIGID_BODY_MODE_RATIO` | `1e-12` | `1e-12` (**retired**) | unchanged; nothing asserts against it | -- | `:410-427`. Retirement recorded. **R405** on the quantifier, **R408** on "referenced by nothing". |
| `RIGID_BODY_SUBSPACE_LOSS` | `1e-13` | `1e-13` (**retired**) | unchanged; nothing asserts against it | -- | `:468-477`. Retirement recorded, and the evidence for it -- 41 of 56 canonical, 42 here -- I reproduce at 42 of 56. |

```
judge NO VALUE WAS WIDENED TO RESCUE A TEST. No test was failing before any of
     these moved, the retirements are backed by a measurement over a corpus
     the implementer did not write, and the two new entries arrive with the
     assertion they serve, which is the `RESULTANT_EXACTNESS` precedent from
     step 4.
judge THE ONE MOVE I REFUSE IS `RIGID_MODE_GAP` 1.5 -> 1.3, and not because
     1.3 is loose. It is TIGHTER on the clean side. It is the COUNTER side
     that the move put under the declared platform spread, and the reason the
     move happened at all is a margin computed in the wrong units (R404).
judge NO OTHER NUMBER IN THE EIGHT COMMITS FUNCTIONS AS A TOLERANCE. `RIGID`
     is still a kinematic constant with a not-a-tolerance docstring; `EPS` is
     `np.finfo(float).eps`; the `1.0, 1e12` bracket inside
     `counter_response("floor")` is a bisection domain and is solved out of.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2343 passed at 44f28e8 -- no undeclared literal entered tests/ this round,
     and nothing was added to `tolerance_marker_exemptions.txt`.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**What moved is substantial and goes before the holds.** The count rule is
right in shape and R397 is genuinely answered: counting below a threshold
instead of below the largest gap is the correct fix, the floor has a real
bracket, R398's missing controls exist and I watched them go to five and to
seven, R394's decade error is corrected with the shipped function's own
numbers, R388's second site is closed at both lines, and the subspace loss was
retired on evidence rather than defended. The residual half is still the
strongest thing in this gate -- I attacked it at `unit=1e8` and it read
`8.1e-25`. CI is green on Linux at the reviewed commit, ten determinism legs
executed and agreed at `1b87e03`, and commit hygiene is clean: a standalone
RE-LOCKED plan commit and nothing near `.claude/`.

**What holds is seven items. One is the gate's claim; one is a tolerance the
repository's own check pushed the wrong way; five are sentences that one
command refutes, four of them written or re-locked this round.**

1. **R403 -- the gap does not guard the count.** Millimetres composed with a
   span factor already in the file gives count 8 with the gap at 7.2x its
   floor, and the same one-parameter ladder reddens the gap three times where
   the count is right. The gap detects a boundary, not a wrong answer, and
   three sentences say otherwise.
2. **R404 -- a logarithm judged by a multiplicative rule.** `2.071/1.3` is a
   ratio of orders compared with a spread of ratios; computed consistently,
   `1.5` cleared both sides and `1.3` leaves the counter at `1.496x` against a
   declared `1.5x`.
3. **R405 -- "twenty-eight frames" and "a large minority" against `34 of 56`,**
   in the sentence R395 repaired and in the plan beside it.
4. **R406 -- the RE-LOCKED plan describes a counter the code deleted** and
   whose docstring records that it does not work; and the section under it
   still presents the two retired ceilings as the gate, with headroom.
5. **R407 -- the gate file's first twenty-five lines describe the gate that was
   replaced in the same commit.**
6. **R408 -- "its counter constant is referenced by nothing"**, two references.
7. **R409 -- a golden lost two assertions with no golden-change explanation,**
   and the plan still says one of them is required.

**Adversarial corpus (BE3): 26 new entries in
`tests/corpus/g21_rigid_body_frames.txt`, all unseen by the implementer,
committed separately at `67486df`.** Every `residual`, `count`, `gap_orders`,
`ratio` and `loss` field was measured by importing the shipped functions at
`44f28e8`, and every one round-trips: re-parsing the line, rebuilding the frame
and re-running the shipped functions reproduces all five published fields,
**zero mismatches on twenty-six**.

**The coverage measurement, stated plainly: of my 26 new frames the shipped Q7
gate holds at 13 and fails at 13.** Every entry is the same defect-free
element, so all thirteen are misses.

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py -q
out  13 failed, 75 passed
     rb_mm_span_x4400  rb_mm_span_x10000  rb_0p1mm_span_x1000
     rb_10um_span_x100000  rb_heavy_mm_span_x10000  rb_span_x10000000
     rb_unit_0p1um  rb_unit_10nm  rb_mm_span_x4340  rb_subdiv8_span_x1000000
     rb_subdiv16_span_x1000000  rb_mm_span_x3600  rb_mm_span_x4000
```

* **The split is the finding and the file carries it in a `kind=` field.**
  Eight are `count_wrong_gap_wide` -- the count is not six and the gap is over
  its floor. Three are `count_wrong_gap_warns`, where the gap does its job.
  **Two are `count_right_gap_red`: the count is SIX, which is correct, and the
  gate refuses it.** Those two are the ones I did not expect.
* **The residual half holds at all twenty-six**, worst `1.0589e-16` against a
  ceiling of `1e-15`, including at a length unit of `1e8`. Every breach is the
  count or the gap; none is the element.
* **Nothing exotic is needed.** The mildest breach is `unit=1000` --
  millimetres -- composed with `stretch=10000`, and both components are already
  in this file with the shipped rule holding on each alone.
* **Thirteen controls that must not move do not move**: centimetres and
  millimetres at two span factors each, a micrometre unit, span x1e6, subdiv 4,
  8, 16 and 24 composed with fine units and long spans, and the brace and heavy
  sections at a micrometre unit. A corpus in which everything breached would
  measure nothing.
* **The transition is laddered rather than sampled**: `rb_mm_span_x3600`,
  `x4000`, `x4340` and `x4400` walk the count from six to seven to eight and
  show the gap falling below its floor and coming back above it while the count
  stays wrong.
* **The older `gap=` fields in this file are the retired largest-gap RATIO and
  are not comparable with `gap_orders=`.** The new block's header says so, and
  the `count=` fields above it were measured under the retired rule.

**Not gates on step 5, into the next report's Carried section:** R410, R411,
R412, R413, R414, R400, R401, R402, R390, R391, R392, R393, R383, R370, R371,
R372, R373, R374, R362, R363, R364, R354, R355, R356, R357, R347, R348, R349,
R350's second half, R330, R331, the section 9 status-versus-subject
disagreement, R321, R322, R300, R291, R292, R281, R231, R244, R245, R275, R230,
R261, the underlying gap in R276, R277, R262, R264, R266, the two R248
residues, R249-R252, R225-R228, R232, R233, and everything already at 4a.
R394, R395, R396, R397, R398 and R388 are closed. R399 carries.

**Forty-six rounds have found no element defect, and this round does not
either.** All thirteen of my corpus breaches are a MEASURE failing on a
defect-free element, which is the third round running that the corpus has said
the same thing about a different measure. It still means "not yet
contradicted": ladder 5 has printed `OK -- 0 directories ran` every time it has
run, and V5.1 against CalculiX is the witness that has not spoken.
