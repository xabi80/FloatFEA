# Review — F2 step 5
Reviewed commit: 8874a7472325876ef39cbb0008fd16da53fbe8ab
Verdict: HOLD

**Reviewed commit: `2337624`.** Report revision 19, `Answers: verdict 44 @
ab3b50c`. The `Reviewed commit:` line stamped above this one by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus commit
`8874a74` -- not the commit judged. That is R373, still open; read `2337624`.

Tests: **2265 passed, 0 failed, 0 skipped** at `2337624` (my run, clean tree,
`python -m pytest -q`, 472.82 s, Python 3.13.15 on Windows).

**AT MY OWN CORPUS COMMIT `8874a74`: 11 failed, 2282 passed.** Every one of the
eleven is `test_G2_1_holds_at_every_frame_in_the_corpus` at a frame I added this
round, and that is the corpus doing the job BE3 gives it rather than a
pre-existing red. The eleven are named in the adversarial-corpus section below
and the next report must name them under `test_a_RED_suite_is_named_in_the_report`.

**Commits: `6215afb`, `477f324`, `79c885d`, `d045bff`, `d875bd6`, `ea4731b`;
plan `ac20398`, `fa96dcc`. Report `2337624`.**

**Item 1b.** Revision 19's header at line 6734 reads `Answers: verdict 44 @
ab3b50c`; `git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`ab3b50c873ceddc7331c1cad2df2cdb475bf2f17`. It is the latest. **Passes.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT, AND THE DETERMINISM LEGS RAN

```
cmd  gh run list --commit 2337624
out  [] -- the short sha finds nothing through that flag. Recorded, then
     resolved by full sha rather than treated as an unavailable check.
cmd  gh run list --limit 15 --json headSha,conclusion,databaseId
out  run 34811100727 -- headSha 233762438ab..., event push, SUCCESS
cmd  gh api .../runs/34811100727/jobs
out  "the verification ladder"   success, runner "GitHub Actions 1000000967", 13 steps
     "lint, unit and guards"     success, runner "GitHub Actions 1000000968", 14 steps
     "CI determinism -- leg"          skipped, runner null, 0 steps
     "CI determinism -- ten legs"     skipped, runner null, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I AM JUDGING,
     WITH Q7'S NEW GATE IN THE LADDER. Not CK2: runners were assigned and
     steps executed. The determinism pair is dispatch-only and is recorded as
     an UNAVAILABLE check rather than skipped over.
cmd  gh api .../runs/34809090965/jobs   -- the dispatch at `fa96dcc`
out  ten "CI determinism -- leg (n)" jobs, ALL success, real runners, 13 steps
     each; "CI determinism -- ten legs agree" success, 4 steps
judge R383 MOVED FOR THE FIRST TIME IN MANY ROUNDS: CP3's predicate executed.
     It is not closed at the reviewed commit --
     `git diff --stat fa96dcc..2337624 -- tests/verification scripts .github`
     is one file, `tests/verification/rung1/test_rigid_body_modes.py`, 21
     insertions, and that file is in the rung the legs run. The result
     describes a tree one commit-shaped change away from the one under review.
cmd  gh run view 34809090965 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  the golden pair, the two retired counter cells, and sixteen
     `test_plan_figures.py` rows for the eight unrendered Q7 names -- exactly
     the set `d045bff`, `d875bd6` and `ea4731b` then fixed. The report's
     account of that failure in sec.4 is accurate.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff ab3b50c..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- no STOP-class finding. Nothing under `.claude/` moved.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                  -- the instruction's own expectation
cmd  git diff ab3b50c..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set, and no plugin was added
cmd  git diff --stat ab3b50c..HEAD -- floatfea
out  floatfea/tolerances.py | 62 ++++++ -- ONE FILE, 62 INSERTIONS, 0 DELETIONS
judge THE TWENTY-ROUND RUN OF A BYTE-IDENTICAL `floatfea/` ENDS HERE, and
     correctly: Q7 needed four new entries. NO EXISTING VALUE MOVED -- the
     diff has no deletions at all, so nothing was widened, retyped or
     retargeted. `79c885d` carries the four entries together with the gate
     they serve; that is an ADDITION for a new assertion, not a tolerance
     changed in the same commit as the code it rescues, and the F2 precedent
     is `RESULTANT_EXACTNESS` and `SOLVE_RESIDUAL` at step 4.
cmd  git show --name-only on each of the nine commits
out  `ac20398` and `fa96dcc` touch docs/milestones/F2.md ALONE and both say
     RE-LOCKED. No commit mixes process with code.
```

## Carried

Verdict 44 held on R385, R386, R387, R388 and R389. **Four are answered; R388
is answered at one of the two sites its condition named and carries.**

- **R385 -- ANSWERED, at the site.** Â§D5a's "The scanner's domain" now reads
  "`floatfea/` and `scripts/`" and strikes `floatsim/io/` with the check in the
  plan itself. `git ls-files -- floatsim` is empty here and the row now says so
  and says why, citing `docs/hsp-coupling.md`. The tree the round's own cell
  scanned, `scripts/`, is in the row with the reason it is there. A standalone
  plan commit, `ac20398`, RE-LOCKED. **Closed.**

- **R386 -- ANSWERED, and both limbs of the condition are met.** R1's gate is
  now provenance plus an injected `_COUNTER` that "reddens the reader's DECISION
  on a named record", and decision-invariance is demoted in writing to "a
  REGRESSION CHECK and labelled as one ... it cannot fail while the values are
  identical". R2 now solves for the `|g|` at which accept flips, sets the
  relative form to preserve that boundary, publishes it as a figure and has V1.3
  assert unit-invariance. That is invert-the-rule-and-solve, written into the
  plan. **Closed.**

- **R387 -- ANSWERED, at the line.**

```
cmd  grep -rn "test_the_report_this_guard_measures" . --include=*.py
out  (nothing under tests/ or scripts/ -- only this verdict and the answers
     table quoting the finding)
cmd  sed -n '1262p' tests/test_report_carried.py
out  `test_the_anchor_fallback_cannot_be_taken_in_this_repository`
cmd  grep "def test_the_anchor_fallback" tests/test_report_carried.py
out  :1342 -- the citation resolves
judge AND CR2 TURNED THE FINDING INTO A MECHANISM:
     `tests/test_collected_set_golden.py::test_every_test_name_cited_in_prose_exists`,
     30 citations collected, so it is not an empty parameter set.
```

- **R388 -- HALF ANSWERED, AND THE HALF THAT IS NOT IS THE ONE THE CONDITION
  NAMED SECOND. This carries.** The condition was: "the table's third row says
  what actually returns the empty string ... **and the comment at `:1249` names
  the same condition**".

```
cmd  git diff ab3b50c..HEAD -- tests/test_report_carried.py
out  the docstring table gains the UNTRACKED row and corrects the empty-string
     row to "nothing under `docs/reports/` has any history at all" -- THE
     FIRST SITE IS DONE
out  at the second site, ONE LINE CHANGED, and it is the phantom citation from
     R387. The condition sentence is untouched:
       :1257  # NO HISTORY FOR THIS REPORT PATH (R377). There is no commit to
       :1258  # measure a distance to, ...
cmd  sed -n '1266,1269p' tests/test_report_carried.py
out  the assertion message under it repeats it: "and this report path has no
     history to anchor a distance to"
judge THE BRANCH IS STILL LABELLED WITH THE CONDITION ITS OWN TABLE NOW SAYS
     IS WRONG, eight lines above it, and the failure message a reader sees
     says it too. This is the CLAUDE.md rule "A closing condition that names
     sites is closed site by site", and sec.2 of the report records R388 as
     answered without mentioning the second site.
```

**Closed when** the comment at `:1257` and the assertion message at `:1268`
name the condition the table names -- nothing under `docs/reports/` has any
history, or git failed -- rather than "this report path". Two lines.

- **R389 -- ANSWERED AT BOTH AXES, AND I MEASURED IT ON MY OWN DATA RATHER
  THAN ON THEIRS.** The condition offered the rule or the sentences; they took
  the rule, and the rule reaches.

```
cmd  python scripts/corpus_figures.py, at 2337624
out  260 260 106 154 54   -- against 260 260 106 154 40 at `d273acf`
judge FOURTEEN OF MY EIGHTEEN MISSES MOVED FROM ESCAPING TO CAUGHT, and
     fourteen is exactly the number R389 attributed to the two axes. The
     identity table has a side and `_const_value` folds recursively through
     brackets, powers and the numeric calls, and the other operand must carry
     the declared name.
cmd  the false-positive control the condition required
out  `RIGID_BODY_MODE_RATIO * w[RIGID - 1]` still clean -- the subscript side
     folds to None, so the constant is never read. It is live at
     `test_rigid_body_modes.py:493` and green in my whole-suite run.
```

- **R390, R391, R392, R393 -- OPEN at 4a, correctly listed in sec.6.** R391
  recurs and is worse this round; recorded below as R402 rather than silently
  re-carried.

- **R383 -- ADVANCED, NOT CLOSED.** See the CI block: the ten legs executed at
  `fa96dcc` and agreed on one hash. One rung-1 file moved after that dispatch.

- **R370, R371, R372, R373, R374 -- OPEN at 4a**, correctly listed. R373 bites
  again in this verdict's own header.

- **R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350's second
  half, R330, R331 -- OPEN at 4a, correctly listed.**

- **R332 -- ANSWERED BY EVENTS, and I want it recorded.** It was "nothing reads
  `g21_rigid_body_frames.txt`". `tests/verification/rung1/test_rigid_body_corpus.py`
  reads it, asserts on every entry, and has a meta-test that compares the parsed
  count with the file's own `id=` lines. Eighteen rounds late and it is the
  thing that settled Q7. **Closed.**

- **R223, R224 -- ANSWERED. Q7 is executed.** See the findings below.

- **R231, R244, R245, R275 -- OPEN, unblocked, and the report correctly does
  not claim them.**

- **R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.** R302 accepted at verdict 37, not reopened.

- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement is unchanged and
  stays at 4a.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** R250, R251,
  R226, R227, R264 and R266 still have no row; R348 territory, unmoved.

- **R365, R366, R367, R368, R369, R375-R382, R384 -- carried in
  `step-5-answers.json`.** Checked the diff; the bookkeeping is right.

## Findings

**First, what is right, because it is the largest thing that has happened in
this step and it should not be buried under six holds.**

**THE RESIDUAL HALF OF Q7 IS A REAL IMPROVEMENT AND I MEASURED IT MYSELF.**

```
cell my own instrument, built from the shipped `residual_exactness`, over the
     28 frames in my corpus and over ten decades of length unit
out  residual worst 9.2375e-17 over the corpus (ceiling 1e-15), and
     1.13e-17 .. 9.74e-17 over unit = 1e-6 .. 1e+6. It does not move.
out  the SAME counter injected at every one of the 28 frames is CAUGHT at all
     28, margins 1.36x .. 4.50x. There is no frame in the file where the
     residual gate is blind.
out  a defect on a ROTATIONAL dof at 1e-6 of the rotation block's own scale
     takes the residual to 5.871e-08, 5.9e+07 times the ceiling. The single
     global `max|K|` normalisation does NOT make it blind to the softer block,
     which was my first hypothesis and the measurement refuted it.
judge THE RETIRED RATIO BREACHES AT 10 OF 28 AND THE SUBSPACE LOSS AT 17 OF 28
     WITH A DEFECT-FREE ELEMENT -- I reproduce both counts exactly. Replacing
     the ratio with the residual is correct and the corpus is why. Good.
```

---

**R394. (BLOCKS -- a tolerance's counter justification publishes a number its
own shipped function refutes by 11x, and the wrong number is the one that makes
the margin look safe.)** `floatfea/tolerances.py:311-315`, in `79c885d`.

```
code :312 "a diagonal stiffness resisting a rigid translation at this size
     :314  takes the residual to about `5e-14`, which is well past the ceiling
           without sitting on its own detection edge"
cmd  the shipped `counter_response("residual")`, imported from
     tests/verification/rung1/test_rigid_body_modes.py at 2337624
out  4.4841e-15
judge 4.4841e-15 IS 4.48x PAST THE CEILING, NOT ~50x. The published figure is
     the response to a defect of `1e-13`, one decade above the value the entry
     declares -- my sweep gives 1e-13 -> 4.4679e-14. This is BI3's species
     exactly: a number correct for the factor it was first written against,
     left behind when the factor moved, and nothing regenerates it.
cmd  invert the decision rule and solve, by bisection on the defect size
out  detection edge 2.2038e-15; the declared counter is 4.54x above its own
     edge
judge SO THE SECOND CLAUSE IS ALSO WEAKER THAN IT READS.
     `RIGID_BODY_MODE_RATIO_COUNTER_DEFECT` next door sets the house standard
     and states it: "31x past the ceiling", "deliberately NOT the smallest
     size that reddens". 4.48x and 4.54x are defensible; they are not what the
     entry says, and at the worst corpus frame the margin is 1.36x.
```

**Closed when** `:314` carries the number the shipped `counter_response("residual")`
returns at the commit that publishes it, and the "not on its own detection
edge" clause carries the solved edge or is struck. One command produces both.

**R395. (BLOCKS -- the same round publishes "10 of 28" in the report and in the
canonical render, and "sixteen" in the tolerance entry and in the test docstring
that is the reader's account of why the gate changed.)**
`floatfea/tolerances.py:294` and
`tests/verification/rung1/test_rigid_body_modes.py:430`.

```
code tolerances.py:293 "the reviewer's corpus of twenty-eight frames showed
     :294              what that measures: sixteen of them exceed its ceiling
                       with a DEFECT-FREE element"
code test_rigid_body_modes.py:429 "IT WAS THE GATE AND THE REVIEWER'S CORPUS
     :430               REFUTED IT. Sixteen of the twenty-eight frames ...
                        exceed its ceiling"
cmd  mode_ratio(K) > RIGID_BODY_MODE_RATIO over every corpus entry, my own
     instrument
out  10 of 28
cmd  grep retired_ratio_over_ceiling_on_corpus docs/milestones/F2_figures.md
out  | `retired_ratio_over_ceiling_on_corpus` | 10 of 28 |   -- the canonical
     render, produced on the runner
cmd  the report's own sec.4
out  "the ratio exceeds its ceiling at 10 of 28 frames"
judge SIXTEEN IS NOT ANY QUANTITY IN THIS FILE. I checked the neighbours: the
     loss breaches 17, the union of the two is 17, `expect=breach` marks 18.
     It is not a machine disagreement either -- the canonical render says ten.
     BP0's rule is that a figure carries the rule it was measured against and
     is regenerated when the rule moves; here the correct figure was generated
     into `F2_figures.md` in the same round and two prose sites kept an older
     one. A reader of the entry is told the evidence is 60% stronger than it is.
```

**Closed when** both sites carry the rendered figure by name -- the entry has
`{{fig:retired_ratio_over_ceiling_on_corpus}}` available and the neighbouring
entries already cite figures rather than retyping them (R194) -- or carry ten.

**R396. (BLOCKS -- a RE-LOCKED plan says two ceilings are "asserted against
nothing" and one of them is asserted, in the rung the plan is about; and the
evidence the plan cites for retiring the first applies with more force to the
one it kept.)** `docs/milestones/F2.md`, section "G2.1 in the residual form",
in `fa96dcc`; `tests/verification/rung1/test_rigid_body_modes.py:439`.

```
code plan "The two quantities below were the gate for fourteen rounds and
          neither is one now. `RIGID_BODY_MODE_RATIO` and
          `RIGID_BODY_SUBSPACE_LOSS` are kept, still generated, and asserted
          against nothing."
cmd  grep -rn "RIGID_BODY_SUBSPACE_LOSS" tests/ --include=*.py | grep -v COUNTER
out  tests/verification/rung1/test_rigid_body_modes.py:466:
       assert loss <= RIGID_BODY_SUBSPACE_LOSS, (
cmd  my own whole-suite run, captured output
out  "worst analytic vector outside the computed span: 5.3061e-15 against
     1e-13" -- `test_the_analytic_rigid_body_vectors_are_SPANNED` runs and
     decides, and `test_a_LOST_rigid_body_DIRECTION_is_caught` is still its
     registered counter in `tests/test_counters_are_injected.py:155`.
judge THE SENTENCE IS FALSE FOR HALF ITS SUBJECT, in a RE-LOCKED plan.
code test_rigid_body_modes.py:439 "and `RIGID_BODY_MODE_RATIO` is now
                                   referenced only here"
cmd  grep -rn "RIGID_BODY_MODE_RATIO" tests/ --include=*.py | grep -v COUNTER
out  :449 (here), :493, :535, plus test_rigid_body_corpus.py:188
judge FALSE, AND IT MATTERS RATHER THAN BEING A COUNTING SLIP. At `:493` and
     `:535` the retired ceiling is the ZERO-MODE THRESHOLD the two count
     controls decide by: `np.sum(np.abs(w) <= RIGID_BODY_MODE_RATIO * flexible)`.
     Q7's stated reason for the gap is that "a threshold on an eigenvalue is a
     statement about the model's units and stiffness"; the controls that
     establish 5 and 7 still use exactly that threshold.
judge AND THE SUBSTANTIVE HALF. The corpus evidence the plan cites is that the
     ratio breaches at 10 of 28 defect-free frames. I measured the loss on the
     same 28: IT BREACHES AT 17. The measure the round kept as a gate is the
     one the round's own evidence indicts more heavily, and neither the plan
     nor the report says so.
```

**Closed when** (i) the plan sentence says which of the two still asserts, or
`RIGID_BODY_SUBSPACE_LOSS` is retired on the same evidence and the plan records
17 of 28; (ii) `:439` says where the name is referenced; and (iii) whichever
limb is chosen, the 17-of-28 measurement appears somewhere a reader of the plan
meets it. One grep and one loop over the corpus.

**R397. (BLOCKS -- the COUNT half of the new gate is a statement about the
frame's conditioning in the same way the retired ratio was, the gap does not
warn when it fails, and eleven of twenty-eight unseen frames break it.)**
`tests/verification/rung1/test_rigid_body_modes.py:243-256` `zero_modes_by_gap`;
`floatfea/tolerances.py:331-345` `RIGID_MODE_GAP`.

```
code tolerances.py:340 "Homogenising by the round-off floor is what makes it
                        comparable between frames: the six zero modes sit
                        BELOW that floor and the seventh is orders above it."
cell the shipped `zero_modes_by_gap` at `unit=1e-4` -- ten kilometres, ONE
     DECADE past the kilometre entry already in the corpus, same defect-free
     element, my own instrument
out  homogenised spectrum [0.35 0.21 0.045 0.035 0.040 0.094 | 6.0e5 7.3e5
     7.5e5 2.3e6 ... 4.4e6 | 8.1e13 ...]
     count = 18        <- the assertion wants 6
     gap   = 1.8203e+07 >= 1e+06  -> THE GATE CERTIFIES THE WRONG COUNT AS
                                     WORTH READING, 18x above its own floor
     residual = 3.7337e-17  -> green
judge EIGHTEEN MODES SIT BELOW THE FLOOR, NOT SIX. K's translation block
     scales as 1/u and its rotation block as u, so twelve rotational modes
     sink under `eps*max|lambda|`. `argmax` over the whole spectrum then finds
     the bending/axial split instead of the nullspace edge. The gap assertion
     cannot protect against this: it is the ratio AT the largest gap, wherever
     that is, so it is large precisely when the count is most wrong.
cell invert the decision rule and solve, by bisection on `unit`
out  the count leaves 6 at u = 2.3456e-04 and again at u = 1.1736e+04 -- a
     WINDOW of about 7.7 decades, not an invariance. Pinned from both sides in
     my corpus: `rb_unit_count_hold_small` (2.4e-4, holds) against
     `rb_unit_count_edge_small` (2.3e-4, count 18), and `rb_unit_0p1mm`
     (1e4, holds at gap 2.0496e+06) against `rb_unit_count_edge_large`
     (1.2e4, count 15).
cell TWO EFFECTS ALREADY IN THE CORPUS, COMPOSED -- and this one needs no
     exotic unit at all
out  `rb_brace_D0p05_t0p0005` holds. `rb_unit_kilometre` holds.
     `rb_brace_kilometre` is the two together: count 6, GAP 4.3408e+05, UNDER
     the 1e+06 floor. The crossing in D at kilometre units is solved at
     D = 0.0759 m and is on disk as `rb_brace_D0p0759_kilometre` (gap
     9.9999e+05).
     `rb_subdiv8_kilometre` holds at 1.1045e+06 -- 1.10x of the floor.
     `rb_span_x100_centimetre` holds at 1.8774e+06 -- 1.88x.
judge THE FLOOR WAS SET FROM THE MINIMUM OVER THE FRAMES THAT HAPPENED TO BE
     IN THE FILE. The entry says so -- "the smallest gap over the reviewer's
     twenty-eight frames is about sixty times this" -- and I reproduce
     6.0131e+07 exactly. That is a statement about twenty-eight frames, not
     about the class of frames the gate claims. Compose two of them and the
     headroom is gone.
judge THIS IS THE SAME FINDING THAT RETIRED THE RATIO, ONE AXIS OVER, and the
     round's own reasoning is what makes it blocking rather than interesting.
judge WHAT IS NOT WRONG, so the repair is not over-scoped: the count and the
     gap are honest about the MATRIX. At u = 1e-4 twelve rotational modes
     really are indistinguishable from zero in double precision. What is
     refuted is the claim that the quantity is comparable between frames, and
     the eleven reds are false reds on a defect-free element -- which is the
     defect, not a discovery about the element.
```

**Closed when** either the count is made scale-aware -- the obvious candidates
are a gap sought at the expected nullspace edge, or a spectrum homogenised per
DOF block rather than by a single largest eigenvalue, and neither is my call --
**or** the claim is narrowed to the domain that was measured: the
`RIGID_MODE_GAP` entry and the plan section state the solved window, say the
count is conditioned, and `rb_brace_kilometre` and the two boundary pairs are
given an expectation one way or the other. **Either answer is fine. What is not
fine is the entry's present sentence, which one decade of extension refutes.**

**R398. (BLOCKS -- the new COUNT assertion has nothing in the repository that
makes it fail. Both of Q7's counters leave the count at six by design, and the
two controls that would move it were not converted.)**
`tests/verification/rung1/test_rigid_body_modes.py:414`, `:479`, `:504`, `:620`.

```
code :414  assert count == RIGID, ...
judge ASK THE QUESTION THIS REPOSITORY ASKS OF EVERY CHECK: if the thing it
     claims were false, would this go red? Nothing shipped demonstrates that
     `zero_modes_by_gap` can return anything but 6.
cmd  the gap counter, `_foundation`, through the shipped gate
out  "6 modes below a gap of 9.6534e+04" -- it reddens the GAP assertion and
     leaves the count at six. The entry says so: "it degrades the gap rather
     than changing the answer."
cmd  the residual counter, `_defect`
out  reddens the residual. Does not touch the count.
cmd  the two controls that DO move a nullspace dimension:
     test_ONE_PINNED_DOF_leaves_FIVE:493 and
     test_ONE_RELEASED_CONNECTION_gives_SEVEN:535
out  both still count with the RETIRED threshold, through `_spectrum`:
     `np.sum(np.abs(w) <= RIGID_BODY_MODE_RATIO * flexible)`. Neither calls
     `zero_modes_by_gap`.
cell I ran the new rule through both controls myself, because the cheap
     measurement exists and an argument is not a measurement
out  pinning each of the 30 DOFs in turn: zero_modes_by_gap gives 5 at all 30
     torsional release on member (3,4): gives (7, 2.4255e+13)
judge SO THE NEW RULE WOULD PASS BOTH, AND THE REPAIR IS TWO LINES. That is
     why this is a gap rather than a defect -- and it is still a gap: the only
     evidence the count can read 5 or 7 is in this verdict, not in the suite.
     The upward control is the one that failed first in this file's history
     and its own docstring says it "is worth more than the gate it guards". It
     now guards the retired gate.
code :620 `def test_a_CLOSED_GAP_reddens_the_COUNT_assertion` -- the name says
     COUNT; the body matches on "separating the nullspace", which is the GAP
     assertion, and its own docstring says "the count stays at six".
```

**Closed when** the two controls decide through `zero_modes_by_gap`, so the new
count assertion has a downward control at five and an upward control at seven;
and `:620` is named for the assertion it reddens.

**R399. (BLOCKS -- the retired pair's tolerance entries still read as live
gates, and the retired ratio's counter now defends a different assertion in a
different quantity.)** `floatfea/tolerances.py:350-389`;
`tests/verification/rung1/test_rigid_body_modes.py:549-568`.

```
code :357 "That leaves about 83x of headroom ON THE CANONICAL MACHINE."
code :371 "so this ceiling is crossed by a defect somewhere between `1e-14`
          and `1e-13` of the largest entry"
code :382 "COUNTER-CASE, INJECTED into the assembled matrix and run through
          the gate ... about 31x past the ceiling"
cmd  git diff ab3b50c..HEAD -- floatfea/tolerances.py
out  0 deletions -- not one word of the retired pair's entries was touched
judge THE WORDS "HEADROOM", "CEILING ... CROSSED" AND "RUN THROUGH THE GATE"
     DESCRIBE A GATE, and the only assertion left on that quantity is
     `assert math.isfinite(ratio)`. There is no ceiling to have headroom
     against.
cmd  what uses RIGID_BODY_MODE_RATIO_COUNTER_DEFECT now
out  test_a_RIGID_BODY_MODE_that_carries_ENERGY_is_caught:564, which injects
     it and then calls `test_the_rigid_body_vectors_are_EXACT_in_the_residual`
     -- a different assertion, against RIGID_MODE_EXACTNESS, in a different
     quantity. Its own docstring still says "`RIGID_BODY_MODE_RATIO`'s counter"
     and "it lifts the sixth eigenvalue off zero. The gate above must redden."
judge CLAUDE.md: "A counter measured in a different quantity ... is evidence
     for a different test." That is this, and `tests/test_counters_are_injected.py`
     cannot see it -- the ratio pair LEFT the registry, so the one guard that
     asks "does this counter defend the gate it is declared against" no longer
     looks at this counter at all. The meta-test caught the registry change,
     which is to its credit; nothing catches the orphan it left behind.
judge SAME SPECIES IN THE RENDER: `scripts/regen_figures.py:138` still marks
     `rigid_body_counter_ratio` as
     `_floor(..., "above", "RIGID_BODY_MODE_RATIO")`, a pass/fail against a
     rule that no longer decides anything.
```

**Closed when** the two retired entries say they are diagnostics and what the
retirement was -- one sentence each, with the "headroom" and "run through the
gate" wording struck -- and `test_a_RIGID_BODY_MODE_that_carries_ENERGY_is_caught`
is either the residual's second counter, described as such and sized on the
residual, or removed because `test_a_RESISTED_rigid_motion_reddens_the_RESIDUAL`
is already that test.

**R400. (recordable, 4a) The corpus reader in the new rung-1 file raises before
its own meta-test can speak.** `tests/verification/rung1/test_rigid_body_corpus.py:73-78`.
`_entries()` does `dict(f.split("=", 1) for f in line.split())` at import time
and raises `ValueError` on any `id=` line carrying a token without an `=`. The
direction is right -- it refuses rather than dropping -- but
`test_the_corpus_is_read_at_all` then never runs, and what a reader sees is a
collection error rather than the meta-test's message. I hit this while
generating my own entries.

**R401. (recordable, 4a) CR2's citation rule cannot see a cited test FILE.**
In `tests/test_collected_set_golden.py`, `_CITED` is compiled from a raw string
in which the optional `.py` group is written with a DOUBLED backslash, so the
group matches a literal backslash and a backticked `test_foo.py` is silently
skipped -- the one suffix the group was written to allow. Measured at 2337624:
the pattern matches `test_foo` and does not match `test_foo.py`. 30 citations
are collected, so this is a reach gap and not an empty parameter set.

**R402. (recordable, 4a) Section 10's `out` block omits two commits, one of
them the golden.** `git log --oneline ab3b50c..HEAD` prints nine rows at the
report's own commit and eight at `ea4731b`; the block labelled with that command
lists six, dropping `d875bd6` and `ea4731b`. R391 was the same label carrying
truncated text; this one drops rows, and one of the dropped rows is a
golden-file change, which `CLAUDE.md` gates specifically under Testing. The
substance is elsewhere -- sec.7 explains the golden -- so it does not block, but
it is the third round running for this block.

## Tolerances touched

**Four new entries in `floatfea/tolerances.py`. No existing value moved:**
`git diff ab3b50c..HEAD -- floatfea/tolerances.py` is `+62, -0`, and the whole
of `floatfea/` is that one file.

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| `RIGID_MODE_EXACTNESS` | -- | `1e-15` | **relative and dimensionless** -- the worst over six analytic vectors of the residual norm over `max-abs-K` times the vector norm, so numerator and denominator carry the same units | `RIGID_MODE_EXACTNESS_COUNTER_DEFECT`, injected through `assembled` and decided by the shipped assertion. I confirmed it reaches the assertion, and that it is caught at all 28 pre-existing corpus frames, margins 1.36x to 4.50x | `:305-308` plus `{{fig:rigid_mode_residual_worst_over_corpus}}` = 9.2375e-17, which I reproduce exactly. **The ceiling itself is sound and I could not break it.** |
| `RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | -- | `1.0e-14` | relative defect, a fraction of `max-abs-K` on one translational diagonal | n/a | `:311-315`. **R394: the published response `5e-14` is measurably `4.4841e-15`, and the solved detection edge is `2.2038e-15`, so the counter is 4.54x above its own edge rather than clear of it.** |
| `RIGID_MODE_GAP` | -- | `1.0e06` | dimensionless ratio between adjacent homogenised eigenvalues | `RIGID_MODE_GAP_COUNTER_DEFECT`, a uniform foundation injected through `assembled`; reddens the gap assertion, pinned by a `match` on its message. Declared against the gap while also reddening the residual, **and the entry says so** | `:342-345`, "sixty times this ... at the kilometre re-expression" -- I reproduce 6.0131e+07. **R397: that is the minimum over the 28 frames that were in the file, and a composition of two of them, `rb_brace_kilometre`, sits at 4.3408e+05, under the floor.** |
| `RIGID_MODE_GAP_COUNTER_DEFECT` | -- | `1.0e-07` | relative, a fraction of `max-abs-K` on every diagonal | n/a | `:337-346`. I reproduce `9.6534e+04` exactly against the entry's `9.7e+04`, and the solved edge is `9.6533e-09`, so the counter is 10.36x above it -- **this one's arithmetic is right.** |

```
judge ON THE INVOCATION'S SECOND QUESTION -- IS DECLARING A COUNTER AGAINST ONE
     ASSERTION WHILE IT TRIPS TWO THE WRONG SHAPE? NO, AND THE ENTRY'S
     HANDLING IS RIGHT. A uniform foundation must lift a zero mode, and a
     lifted zero mode must carry energy; refusing the counter for that would
     demand a defect that closes a spectral gap without touching the
     nullspace, which does not exist. What makes a counter a counter is that
     it is SIZED ON and DECLARED AGAINST one assertion and that that assertion
     reddens on it, and both hold -- the `match` argument pins which half.
     Stating the side effect instead of hiding it is the standard the rest of
     the file should follow, and I want that recorded as a positive.
     The complaint is R398's and not this one's: the side effect is recorded,
     and the half this counter does NOT reach -- the count -- has none at all.
judge NO OTHER NUMBER IN THE NINE COMMITS FUNCTIONS AS A TOLERANCE. CR1's
     `_IDENTITY` table is a classification boundary inside a scanner; I pinned
     it from both sides on my own corpus last round and fourteen of those
     entries moved this round, in the direction claimed.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2265 passed at 2337624 -- no undeclared literal entered tests/ this round.
     The four in `floatfea/io/` remain outside that scan and are step R's.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**What moved this round is the most substantive work in this step, and it goes
before the holds.** Q7 is executed. **The corpus I wrote eighteen rounds ago was
read, and it changed a gate** -- the arrangement working as designed, and the
implementer found the answer in it rather than arguing with it. **The residual
form is right**: I attacked it over ten decades of length unit, at both section
extremes, at four mesh densities, with a one-micrometre member, and with a
defect placed in the rotational block where I expected the single global
normalisation to be blind -- it was not, by seven orders. Four of the five gated
items closed. `RIGID_BODY_MODE_RATIO`'s ceiling deserved to go and the evidence
for going is measured, not argued. CI is green on Linux at the reviewed commit
with the new gate in the ladder, the ten determinism legs executed and agreed
for the first time in many rounds, and commit hygiene is clean -- two standalone
RE-LOCKED plan commits and nothing near `.claude/`.

**What holds is six items. Two are in the half of Q7 that was not attacked, and
four are prose written around work that is correct.**

1. **R394 -- `5e-14` is `4.4841e-15`.** The counter's published response is the
   number for a defect one decade larger, and the margin it advertises is
   eleven times the margin it has.
2. **R395 -- "sixteen of them" is ten**, in the tolerance entry and in the test
   docstring, while the report and the canonical render both say ten, in this
   same round.
3. **R396 -- the RE-LOCKED plan says the subspace loss is "asserted against
   nothing" and it is asserted at `:466`**; and the corpus indicts it at 17 of
   28 against the ratio's 10, so the gate that was kept is the one the round's
   own evidence indicts harder.
4. **R397 -- the COUNT half is conditioned, and the gap does not warn.** One
   decade past the corpus's own kilometre entry the count reads eighteen with a
   gap eighteen times above its floor; two effects already in the file,
   composed, put the gap under it. The window is solved -- 7.7 decades of
   length unit -- and pinned from both sides on disk.
5. **R398 -- nothing in the repository can make the count assertion fail.**
   Both counters hold the count at six by design and the five-and-seven
   controls still decide by the retired threshold. I ran the new rule through
   both and it gives 5 and 7, so the repair is two lines -- but the measurement
   is in this verdict and not in the suite.
6. **R388's second site** -- the branch comment and its failure message still
   name the condition the table eight lines above now says is wrong.

**Adversarial corpus (BE3): 28 new entries in
`tests/corpus/g21_rigid_body_frames.txt`, all unseen by the implementer,
committed separately at `8874a74`.** Every `residual`, `count` and `gap` field
was measured by importing the shipped functions at `2337624`, and every one
round-trips: parsing the line back, rebuilding the frame and re-running the
shipped functions reproduces all four published fields, **zero mismatches on
twenty-eight**.

**The coverage measurement, stated plainly: of my 28 new frames the shipped Q7
gate holds at 17 and fails at 11.** Every entry is the same defect-free element,
so all eleven are misses.

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py -q
out  11 failed, 47 passed
     rb_unit_10km  rb_unit_100km  rb_unit_1000km  rb_unit_count_edge_small
     rb_unit_count_edge_large  rb_unit_10um  rb_span_x10000  rb_span_x100000
     rb_brace_kilometre  rb_brace_10km  rb_brace_D0p0759_kilometre
```

* **The split is clean and that is the finding.** All eleven are the count or
  the gap. **The residual half holds at all twenty-eight**, worst 9.7420e-17
  against a ceiling of 1e-15.
* **Both boundaries are solved and pinned from both sides rather than sampled.**
  The count's unit window at 2.3456e-04 and 1.1736e+04, bracketed by two pairs;
  the gap's crossing in brace diameter at kilometre units at D = 0.0759 m, on
  disk as an entry whose gap is 9.9999e+05 against a floor of 1.0e+06.
* **Seventeen controls that must not move do not move**: thick and thin walls
  at D = 3 m, a 10 mm hairline, subdiv 16 and 24, a tip member one centimetre,
  one millimetre and one micrometre long, span x1000, and the heavy section at
  kilometre units. A corpus in which everything breached would measure nothing.
* **One case is not a line because the code refuses, and it is right to.**
  A tip at `4.4,1.1,280` puts the tip member 0.517 deg from global Z and
  `member_local_axes` raises `DegenerateMemberOrientation` rather than picking a
  reference silently. Recorded in the file's header so it is not re-tried as a
  gap.
* **Nothing was added to `tolerance_marker_exemptions.txt` this round.** R389
  closed both axes it named, the four remaining misses there are R390's family
  and already at 4a, and the frames file is where this round's leverage was.

**Not gates on step 5, into the next report's Carried section:** R400, R401,
R402, R390, R391, R392, R393, R383, R370, R371, R372, R373, R374, R362, R363,
R364, R354, R355, R356, R357, R347, R348, R349, R350's second half, R330, R331,
the section 9 status-versus-subject disagreement, R321, R322, R300, R291, R292,
R281, R231, R244, R245, R275, R230, R261, the underlying gap in R276, R277,
R262, R264, R266, the two R248 residues, R249-R252, R225-R228, R232, R233, and
everything already at 4a. R332, R223 and R224 are closed.

**Forty-five rounds have found no element defect, and this round does not
either.** Every one of the eleven corpus breaches is a MEASURE failing on a
defect-free element, which is the same thing the round itself discovered about
the ratio. `floatfea/` changed for the first time in twenty rounds and changed
only by addition. It still means "not yet contradicted": ladder 5 has printed
`OK -- 0 directories ran` every time it has run, and V5.1 against CalculiX is
the witness that has not spoken.
