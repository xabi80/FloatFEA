# Review — F2 step 6
Reviewed commit: b546aaa9ed7934c4b18cce75661db009e47fc57a
Verdict: PASS

**Reviewed commit: `792c44e`. Sixty-first verdict, and the verdict that CLOSES step 6
under DK0.** This is a disposition, not another round: what is still open under
(a)-(d) is named and carried into step 7, everything else goes to the closure list
and is not re-reviewed. The `Reviewed commit:` line stamped at the top of this file
by `scripts/write_verdict.py` is my corpus commit, not the commit judged (R513,
unchanged).

**Five verdicts on step 6, not six: 56, 58, 59, 60 and this one.** Verdict 57 wrote
step 5's disposition by hand (DD1) and was not about step 6. `docs/closure/F2-step6.md:3-4`
says "Six verdicts on this step (56, 58, 59, 60 and the closure verdict)" -- the
parenthesis lists five and the count says six. Closure item.

Tests: **2549 passed, 0 failed, 0 skipped** -- my run, clean tree at `792c44e`,
`python -m pytest -q`, 622.42 s, Python 3.13 on Windows. 2 warnings, both
pre-existing (the `orient_norm_overflow` g22 corpus entry).

## Item 1b -- CHECKED, AND CLEAN

```
cmd  the newest Answers line in the report under review
out  docs/reports/F2/step-6.md:2740 -- "Answers: verdict 60 @ aa67cc2"
cmd  git log --oneline --follow -- docs/reviews/F2/step-6.md | head -1
out  aa67cc2 review: F2 step 6 -- sixtieth verdict, HOLD @ 6cc6b07
judge THE HEADER NAMES THE LATEST. One comparison, made, it matches, so every
     Carried claim in the revision is about the right list.
```

## CI (3b) -- GREEN AT THE REVIEWED COMMIT, and I did not take it on your word

```
cmd  gh run view 36261451332 --json status,conclusion,headSha,event,jobs
out  completed success 792c44ee push
     the verification ladder  success  13 steps
     lint, unit and guards    success  14 steps
     CI determinism -- leg            skipped  0 steps
     CI determinism -- ten legs agree skipped  0 steps
judge COMPLETED SUCCESS AT `792c44e`, real step counts, not CK2. NO RED TEST AT
     THE REVIEWED COMMIT -- (d) is clean.
cmd  gh run view 36258311635 --log-failed  (at 061bb70)
out  tests/test_report_carried.py:2341 -- "1 commit(s) touching code follow the
     report's own commit 6cc6b07 ... 061bb70" plus the ten
     test_report_guard_states states that wrap it. 13 names, all in
     "lint, unit and guards"; the verification ladder was SUCCESS in both
     failing runs.
judge THE TWO INTERMEDIATE FAILURES ARE THE REPORT-PARAMETRISED GUARDS AND
     NOTHING ELSE, verified in the log rather than accepted from the invocation.
     They are the guard doing its job while a code commit sat after the report's
     own commit, and revision 6 regenerates the line at `3c83650`.
cmd  gh run list --commit 792c44e --json name,conclusion,workflowName
out  []  -- the commit filter returns nothing while `gh run view 36261451332`
     reports headSha 792c44ee. Recorded so the next reader does not read the
     empty list as an absent run.
cmd  the last run in which the determinism legs EXECUTED
out  36253615495 at acbbd0a, workflow_dispatch: ten legs success, 13 steps
     each, "ten legs agree" success
cmd  git diff --stat acbbd0a..792c44e -- tests/verification scripts .github
out  4 files, 496 insertions, 282 deletions -- including the 500-line rewrite of
     test_rigid_body_modes.py and the 111 lines of test_rigid_body_corpus.py
     that carry the new per-frame assertion
judge THE DETERMINISM LEGS ARE AN UNAVAILABLE CHECK AT THIS COMMIT, not a pass
     and not a red, and their last execution no longer describes the tree. That
     is not (d) and I am not holding on it. **I am taking your offer: dispatch a
     `workflow_dispatch` run at `792c44e` or at step 7's first commit.** The
     quantity that just became a per-frame assertion at 213 frames is an
     EIGENVALUE, and agreement across ten legs is the only measurement in this
     repository that would notice `eigh` disagreeing with itself.
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, twelfth round.
```

## My own instructions (4b), conftest (4c), tolerance values (4)

```
cmd  git diff 6cc6b07..792c44e -- .claude docs/SUPERVISOR.md
out  (empty). NOT A STOP on this head.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py   -- the instruction's own expectation, met
cmd  git diff 6cc6b07..792c44e -- tests/conftest.py "tests/**/conftest.py"
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set; no plugin was added, so the
     CH2/CI0 channel is closed by inspection this round
cmd  git diff 6cc6b07..792c44e -- CLAUDE.md
out  one hunk, DK0, committed alone at 0a7423a as `process:` and touching
     nothing else. That is the form the directive requires.
cmd  git diff 6cc6b07..792c44e -- floatfea/tolerances.py, non-comment +/- lines
out  (empty). 53 changed lines, every one a comment -- the closure artifact's
     claim, checked.
cmd  every NAME: Final[...] = value at 6cc6b07 and at 792c44e
out  48 and 48; added [] removed [] changed []. NOT ONE VALUE MOVED.
cmd  git log --format="%h %s" 6cc6b07..792c44e, checked for a commit touching
     both floatfea/ or tests/ AND docs/reviews/
out  none. aa67cc2 is the verdict, alone.
```

## Carried

Verdict 60 was a HOLD carrying **R530** and **R531** as blocking, R532 to R539 as
closure items, R475 / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 /
R522 / R526 / R527 / R529 as open on top, the 48 frozen 4a items, and four closing
conditions.

- **R530 -- ANSWERED, at four of its five sites, and I checked each.** (1) The
  phantom citation is gone: `grep -rn test_BOTH_counters_redden_at_EVERY_span
  floatfea tests scripts` now returns only `docs/milestones/F2a.md:156`, which is
  the record of the finding. (2) `:328-331` no longer claims a per-frame
  enforcement -- the sentence is cut to "`1e-15` is a decade boundary above the
  measured worst." (3) The entry says what the constant is today, including that
  its CLASS line is "now wrong in spirit". (4) The counter entry says "nothing
  injects it" and that F3 will bisect a counter of that shape against its own
  gate. (5) The two false half-sentences at `tests/test_counters_are_injected.py:142-144`
  are the ones that went. **No value moved to close it**, which was the condition.
  What the repair introduced is a new stale figure -- closure item C1.
- **R531 -- ANSWERED on the half that blocks, and better than I expected.** The
  per-entry test now asserts `six = largest_rigid_eigenvalue(k) < RIGID_MODE_BOUND`
  at `tests/verification/rung1/test_rigid_body_corpus.py:230`, before the
  `lambda_7 > 0.0` line, with no early return and no skip between the
  parametrisation and the assertion, so it is evaluated at every one of the
  entries including every refused one. I reproduced the control's edge
  independently and on both DOF classes: clean `lambda_6` **0.4143** units at
  `rb_shipped_frame`, translational edge **2.7202e-13** of `max|K|` (the report's
  figure to five digits), rotational edge **1.6807e-12**. The bisection measures
  what it says: `lifted(hi)` reads 199.60 and `lifted(hi/10)` 19.50, and if
  nothing in `[1e-20, 1e-2]` broke the assertion the final `lifted(hi*10)` line
  would go red rather than pass. **The sentence half of the condition is NOT
  closed** -- R540 below is the part of it that is (b), and C5 to C7 the part
  that is prose.
- **R532 -- RECORDED AS ANSWERED AND IT IS NOT, for three directives.** Closure
  item C8; not re-reviewed further.
- **R533 -- FROZEN, correctly.** `docs/milestones/F2a.md:153-160` records the
  one-tuple domain fix without applying it, which is what CZ0's freeze requires,
  and `3c83650` corrects the finding number in place and says that it did.
- **R534 -- PARTIALLY ANSWERED.** `_stretched` and `_defect` are deleted. Closure
  item C9 for the remainder.
- **R535, R538, R539 -- OPEN closure items**, not re-measured here, and closure
  items rather than blocking: none of them is a value, a form, a counter, a gate
  assertion or a red test. They go to the closure artifact list.
- **R536 -- ANSWERED, and the answer is a real one.** `python scripts/rigid_counter_response.py`
  prints, at this commit, `1702 distinct elements`, `clean worst 1.4575e-16 = 0.656
  eps at rb9_brace_shrunk_1e3_2p87_subdiv4`, `clean clears 1e-15 by 6.861x`,
  `dropped_flip 67 / wrong_dof_index 32 / rotational_block 303`, and `ELEMENTS
  FAILING AT LEAST ONE COUNTER: 335 of 1702`. Every figure in `docs/milestones/F2.md:1493-1508`
  and in `docs/closure/F2-step6.md:48-53` matches that output exactly. **The one
  place that does not is `floatfea/tolerances.py:331` and
  `tests/verification/rung1/test_rigid_body_modes.py:875-876`** -- closure item C1.
- **R537 -- ANSWERED.** Section 0 of revision 6 records run 36256042985 at
  `6cc6b07` as SUCCESS.
- **R475 / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 /
  R526 / R527 / R529 -- OPEN, unchanged, none re-reviewed.** They carry into the
  closure list.
- **The 48 items frozen in `docs/milestones/F2a.md` section 7 -- OPEN on the frozen
  list**, not re-reviewed item by item. `grep -c "^| R" docs/milestones/F2a.md` = 48.
- **Verdict 60's four conditions:** (1) R530 -- met. (2) R531 -- met on the
  assertion, not on the sites; the unmet part is R540. (3) R532-R539 treated as
  closure items and not re-reviewed -- met. (4) `0 failed` locally and a completed
  SUCCESS on CI at a commit whose push touched code -- met at `792c44e`.

## Findings

**The thing I tried hardest to break is R531's new assertion, because it is the (c),
and it survived more than the report claims for it.** Four cells, all at `792c44e`,
all run from a scratch directory outside the repository and none of them in the tree.

```
cell ONE VARIABLE: the element's own local stiffness, patched at the assembly
     site (`floatfea.assemble.system.local_stiffness`, which is where
     `assemble_dense` resolves it -- patching `floatfea.element.beam` changes
     nothing, and a cell that patches the wrong name reads "no defect detected"
     on a defect it never injected; my first run did exactly that). The three
     counter shapes from `scripts/rigid_counter_response.py`, injected into EVERY
     element at 1e-8 of `max|k_e|`, measured through the shipped
     `largest_rigid_eigenvalue` over the 161 spectrally-decided entries of the
     shipped corpus
out  dropped_flip      148 of 161 frames redden
     wrong_dof_index   161 of 161
     rotational_block  126 of 161
judge THE NEW ASSERTION DETECTS THE THREE DEFECT SHAPES THE PLAN NAMES, at the
     size DG2 measured the element-local form at -- where that form leaves 335 of
     1702 elements undetected. The suite reddens under each of the three. Nobody
     had measured this and it is the strongest argument for the replacement that
     exists; it is not in the plan, the report or the closure artifact.
cell SAME VARIABLE, a genuinely unstable element: the sign of `k[1,1]` and
     `k[7,7]` flipped, so `K_hat` has six negative modes at `-1.995e+14` units of
     the arithmetic floor
out  lambda_6 = 9.2588e+13 -> the per-frame assertion is RED
     lambda_7(abs) = 1.2744e+14 -> the shipped single-frame gate at
     test_rigid_body_modes.py:558 PASSES
judge THE INDEFINITE CASE THAT THE RETIRED RESIDUAL CAUGHT IS STILL CAUGHT, and
     by the new assertion rather than by the spectral half, which reads
     |lambda_7| and cannot see the sign at all. That is a real hole in the
     spectral half and the new per-frame assertion is what closes it -- which
     means R531's repair bought more than it was asked for. Closure item C10 for
     the docstring that names `lambda_7` where the code computes `|lambda_7|`.
cell THE SAME CELL ON THE OTHER HALF OF THE DOMAIN: the 41 entries of the shipped
     corpus whose `lambda_7` is under the bound, where the spectral half refuses
     and `lambda_6 < RIGID_MODE_BOUND` is the only assertion left
out  at 1e-8 of max|k_e|:  dropped_flip 3 of 41, wrong_dof_index 34 of 41,
                           rotational_block 0 of 41
     at 1e-4, four decades up: rotational_block STILL 0 of 41
judge THIS IS R540's SECOND HALF. See the finding.
cell AND THE FALSE-RED QUESTION, on 960 frames I built rather than on the
     corpus: four sections x six length units (1e-6..1e9) x five stretches
     (1e-9..1e9) x four tips x subdiv 1 and 4
out  480 built, 480 refused by the builder with `DegenerateMemberOrientation`
     (every exactly-Z-aligned tip member -- an unsupported case that RAISES and
     does not default, which is the behaviour the guard asks for). Of the 480
     built: worst lambda_6 = 1.2768 at base_u1e+06_s1e-09, 156.3x clear,
     **0 over the bound**.
judge NO DEFECT-FREE FALSE RED, on axes two decades wider than any batch in the
     corpus. After four normalisations that this corpus false-reddened, the
     replacement has now held on 187 + 1344 + 480 + 11 frames.
```

---

**R540. (BLOCKS -- (b). CARRIES BY NAME INTO STEP 7.) `floatfea/tolerances.py`'s
`RIGID_MODE_BOUND` ENTRY STILL SAYS THE GATE ASSERTS ONE THING AND THAT THE
RESIDUAL HALF PROVES ITS PREMISE. THE GATE ASSERTS TWO THINGS PER FRAME AS OF
`061bb70`, AND THE RESIDUAL HALF WAS RETIRED BY THIS STEP. THE SENSITIVITY OF THE
NEW ASSERTION ON THE REFUSED HALF OF THE CORPUS IS UNPUBLISHED AND, FOR ONE OF THE
THREE COUNTER SHAPES, ZERO.**

```
cmd  floatfea/tolerances.py:383-390, read today
out  "the gate asserts ONE thing about the spectrum, and it is not a count:
         lambda_7(K_hat) >= RIGID_MODE_BOUND * ||K_hat|| * eps
     The residual half already proves the six analytic rigid-body vectors are
     annihilated by `K`, and by Courant-Fischer that puts six eigenvalues at the
     arithmetic floor."
cmd  grep -rn "RIGID_MODE_BOUND" tests/verification/rung1/test_rigid_body_corpus.py
out  :230  assert six < RIGID_MODE_BOUND   -- added 061bb70, per frame, 213 frames
     :457  assert over >= RIGID_MODE_BOUND -- the decided-set control
cmd  the same entry's own supersession: is the residual half still a proof?
out  no. DI0 retired it in this step; `test_rigid_body_corpus.py:199` prints it.
     The premise is now carried by :230 -- by THIS constant, used in the opposite
     direction, which the entry does not say.
cmd  verdict 59's condition 1 and verdict 60's R531 both named this site
out  verdict 60 named `floatfea/tolerances.py:359-366`; revision 6's section 3
     declares all eight lines "no change -- the sentences the finding names are
     restored by reverting the DB1 prose commit, not edited", which is the R519
     boilerplate and is not a reason for these lines.
judge (b) BY THE LETTER, and it is the R530 shape on the next constant down: the
     value is right, the form is right, and the entry describes a gate that no
     longer has that shape. One constant now serves as a FLOOR for lambda_7 and a
     CEILING for lambda_6 per frame, and only one of those two roles is written
     down in the file `CLAUDE.md` makes the sole home of every tolerance. **No
     value moves to close this.** Third verdict in a row in which a condition
     naming this file was answered at some sites and declared-left at others.
cell AND THE FIGURE THE ENTRY OWES: the new role's sensitivity, split by the
     domain the gate itself splits on. One variable, the three counter shapes at
     1e-8 of max|k_e| into every element's local stiffness
out  decided set (161 entries): 148 / 161 / 126 of 161 redden
     refused set (41 entries):    3 /  34 /   0 of 41 redden
     rotational_block at 1e-4, four decades up: still 0 of 41
judge SO "it holds at EVERY frame including every refused one, so the element is
     under test everywhere" (`test_rigid_body_corpus.py:216-219`, written in this
     commit) IS AN OVERSTATEMENT ON 41 OF THE 213 ENTRIES. The assertion is
     EVALUATED there; for one of the three named defect shapes it cannot fail
     there at any size I reached. That is the sentence R531 was about, in the
     other direction, and the refused set is exactly the set CT2's "undecidable
     is an outcome and not a skip" argument is about.
```

  **Closed when**, site by site: (1) `floatfea/tolerances.py:383-390` says what
  the constant bounds today -- both directions, with `:230` named -- and stops
  citing the retired residual half as the premise's proof; (2) the split above,
  or the implementer's own re-measurement of it, is published where the gate's
  claim is stated, and the sentence at `test_rigid_body_corpus.py:216-219` is
  reduced to what is measured -- OR an assertion reaches the refused frames.
  Either exit is acceptable and I have no vote on which. **No value moves, and
  neither exit is new apparatus**: (1) is a comment, (2) is a sentence plus a
  figure or a change to an existing assertion.

## Closure items (CZ0). None of these is (a), (b), (c) or (d).

**C1. The repair wrote a stale figure into the file it was repairing (CP2 + BI3 +
BP0).** `floatfea/tolerances.py:331` says "298 of the corpus's 1592 distinct
elements did not redden", and `tests/verification/rung1/test_rigid_body_modes.py:875-876`
says "over the 1592 distinct elements ... clean worst is 0.540 eps ... 298 of those
1592". `python scripts/rigid_counter_response.py` prints 335 of 1702 and 0.656 eps at
this commit, and the plan and the closure artifact both carry the new numbers.
`061bb70` wrote `298 of 1592` on top of a corpus that was already 202 entries, so the
figure was stale in the commit that published it; `3fe6cfa` fixed the plan and not
these two. Closed by citing the script instead of the numbers, as BI3 says.

**C2. `docs/closure/F2-step6.md:3-4` counts six verdicts and lists five.** The five
are 56, 58, 59, 60, 61.

**C3. `docs/closure/F2-step6.md:128` calls the citation-guard item R532.** `3c83650`
established that it is R533 and that a frozen item naming the wrong finding is the
species R533 is about. The artifact also records nothing of R532's own answer.

**C4. `docs/closure/F2-step6.md:59` says "No fifth form was proposed."** Verdict 60
proposed `lambda_6 < RIGID_MODE_BOUND` per entry, measured it green at 109x over all
202 entries, and the same artifact ships it in section 4 as what carries the premise.
Closed by "no fifth assembled-residual normalisation was proposed", which is true.

**C5. `tests/verification/rung1/test_rigid_body_corpus.py:166-175` still opens "The
residual form and the spectral gap ... Asserted on EVERY entry", and the module
docstring at `:25` still says "THE RESIDUAL FORM AND THE SPECTRAL GAP HOLD AT EVERY
ONE. That is the claim this file makes."** The residual form is printed.

**C6. The comment at `:195-199` is half-edited.** It now reads "Claim B, the
`lambda_6` under the bound is what is asserted per frame now (R531). Computed and
printed as a diagnostic; nothing decides on it." Claim B is the `lambda_7` bound,
`lambda_6` is not claim B, and the second sentence belongs to the residual on the
line below. At the one site R531 was about.

**C7. `test_rigid_body_modes.py:363-369` and `:379-382` still name the residual half
as the proof of the premise**, and `:367-369` says `largest_rigid_eigenvalue` is
"reported, not asserted here -- `regen_figures` carries it", while
`test_rigid_body_corpus.py:230` asserts it at 213 frames.

**C8. R532 is recorded as answered and is not, for three directives.**
`git log -S DH1 -- docs CLAUDE.md` returns only report and review commits -- no
`plan:` or `process:` commit cites DH1 -- and `grep -rn DH1 docs/milestones docs/closure
CLAUDE.md` returns nothing. **DK2** (step 7's scope) and **DK4** (the schedule) appear
nowhere in `docs/milestones/`, `docs/closure/` or `CLAUDE.md` either, and revision 6
cites both. `docs/milestones/F2a.md`'s "every directive that moved anything now has a
`plan:` or `process:` commit citing it" is refuted by one command, in the locked plan,
which is CW0's own shape.

**C9. R534's remainder.** `_SPAN_CELLS` (`test_rigid_body_modes.py:1035`),
`_COUNTER_DOFS` (`:1036`) and the `"residual"` branch of `counter_response` (`:497`)
still have no caller; `grep -rn _SPAN_CELLS tests scripts` returns one line, its own.

**C10. `seventh_over_epsilon` is documented as `lambda_7` and computes `|lambda_7|`.**
`test_rigid_body_modes.py:371` and `:376` -- `np.sort(np.abs(...))`. On four of my
fifteen candidate frames the defect-free `K_hat` is indefinite at round-off and the
abs hides it: `lambda_7(K) = -2.620e+09` reads as `5.455e-03` units and passes
`over > 0.0`. It does not block because the sign-flip cell above shows the sibling
`lambda_6` assertion catches the case where the negative matters, and at round-off the
frame is genuinely undecidable. Closed by naming the quantity as `|lambda_7|` where it
is stated, or by reporting the sign -- a residual destroys information.

**C11. `test_the_RETIRED_ratio_is_why_the_form_changed` scans every corpus entry
through `mode_ratio`, which raises on a frame class the corpus's own axes reach.**
Four of my fifteen candidates raise `ValueError`. The raise is correct behaviour; the
scan has no handling, so the reviewer's corpus cannot carry those frames. They are
recorded in the batch-10 header instead.

**C12. The determinism legs are unavailable at this commit** and their last execution
(`36253615495` at `acbbd0a`) predates a 496-line change under `tests/verification` and
`scripts`. Closed by one `workflow_dispatch`.

**C13. R535, R538, R539, R519, R521, R522, R526, R527, R529, R500, R501, R513, R475,
R487, R488, R492, R493 and the 48 frozen 4a items** carry into the closure artifact as
a list, unchanged and not re-reviewed.

## Tolerances touched

**NONE. No constant was created, retired, moved, renamed or revalued.**

```
cmd  every NAME: Final[...] = value at 6cc6b07 and at 792c44e
out  48 and 48. added [] removed [] changed []
cmd  git diff 6cc6b07..792c44e -- floatfea/tolerances.py | non-comment +/- lines
out  (empty) -- 53 changed lines, every one a comment
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance value touched this round** | -- | -- |

`RIGID_MODE_EXACTNESS` -- form relative and dimensionless, still correct as
arithmetic; CLASS line still reads ACCURACY and the entry now says so itself;
asserted by nothing; counter `1.0e-14` injected nowhere and stated as such. The
entry's remaining defect is a figure, not a value: C1.

`RIGID_MODE_BOUND` -- value `199.526231496888` unchanged, form a pure number in
units of `||K_hat||*eps`, counter `RIGID_MODE_BOUND_COUNTER_DEFECT` injected
against the `lambda_7` assertion at `test_rigid_body_modes.py:791`. **As of this
step it also serves as a per-frame CEILING on `lambda_6` at 213 frames, and its
entry does not say so: R540.** The new role's detection edge is bisected rather
than declared -- `2.7202e-13` translational, `1.6807e-12` rotational, reproduced
independently -- which is the better form of a counter and is worth saying.

## Adversarial corpus (BE3, scoped by DE2 to the element and the gates)

**11 new entries, all unseen by the implementer, committed separately at `b546aaa`.
`tests/corpus/g21_rigid_body_frames.txt`, batch 10, entries 203 to 213.** The target
is the REFUSED half of the new carrier -- the frames where `lambda_6 <
RIGID_MODE_BOUND` is the only assertion left -- on axes no earlier batch reached:
unit `1e-06` and `1e+09` (earlier: `1e-03` to `1e+06`), stretch `1e-09` and `1e+10`
(earlier: `1e-06` to `1e+08`), subdiv 8 and 16 (earlier: 1, 2, 4, 6, 8 at unit 1).

```
cmd  grep -c "^id=" tests/corpus/g21_rigid_body_frames.txt
out  213   (202 before this batch)
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py
     tests/test_plan_figures.py tests/test_collected_set_golden.py -q
out  469 passed -- the batch reddens nothing, including
     test_every_floor_class_row_clears_its_tolerance_on_THIS_tree, which
     re-renders the lambda_6 row and asserts it against the bound
```

**Coverage measurement.** 15 candidates built, 11 committed. **0 of 11 false-red the
shipped carrier** -- worst `0.8882` units against `199.526` -- and 0 of the 480 frames
in the sweep behind them. That is the second batch in a row that argues FOR a shipped
decision. **The live shape is again the refused set: 9 of the 11 are spectrally
refused, and the new `l6_counters_detected` field records the shipped assertion
detecting 0 of 3 counter shapes on five of them and 3 of 3 on both decided entries.
The checks in the tree caught 0 of 9.** Four of the fifteen candidates cannot be
carried by the corpus at all (C11) and are recorded in the header with their
measurements.

**The counterweight, because right-every-time is not allowed to become a prior:
sixty-one rounds have found no element defect and this round found none either.** The
element annihilates its own rigid motions to `0.656 eps` worst over 1702 distinct
corpus elements, `0.000 eps` on the indefinite frames of C10, and the three counter
shapes are detected on 126 to 161 of 161 decided frames by the assertion that replaced
claim A. Ladder 5 has still printed `OK -- 0 directories ran` every time it has run and
V5.1 against CalculiX has still not spoken, so **"not yet contradicted" remains the
strongest statement available about the element** -- and this week it is a slightly
stronger statement than last week, because the per-frame assertion that was missing is
back and I have measured what it detects.

## On the criterion, said once

**I accept DK0 and the disposition, and I have one thing to say that is not an
argument with CZ0.** Three verdicts in a row -- 59, 60 and this one -- have named
`floatfea/tolerances.py` in a closing condition, and three times the answering report
fixed some of the named sites and declared the rest left with a reason copied from a
different finding. That is the "closed site by site" rule failing in the same place
each time, and the pattern says the file is read entry by entry while the change under
review crosses two entries. **It is not a request for apparatus** -- R533 is frozen
and I am not asking for a scanner. It is the reason R540 is blocking rather than a
closure item: the fourth occurrence should not be discovered by a reader.

## Next step opens when

**Step 6 is CLOSED at `792c44e`, PASS.** Step 7 (V2.5, V2.6 and the V6.1 golden) may
open now, carrying:

1. **R540 -- BLOCKING in step 7's `Carried` section, by name.** The `RIGID_MODE_BOUND`
   entry says what it bounds today at both ends, and the refused/decided sensitivity
   split is published where the gate's claim is stated -- or the sentence at
   `test_rigid_body_corpus.py:216-219` is reduced to what is measured. No value moves.
   **Answered before step 7's first measurement, not alongside it**, because a rung-1
   constant whose entry describes the wrong gate is what the last three verdicts have
   been about.
2. **C1 to C13 are closure items** and go into one closure commit with the rest of the
   list. Do not re-review them item by item and do not hold anything on them.
3. **One `workflow_dispatch` run at `792c44e` or at step 7's first commit** (C12), so
   the ten determinism legs describe a tree that contains the new per-frame eigenvalue
   assertion. Not blocking; report the result in step 7's section 0.
4. **`python -m pytest -q` is `0 failed` and `gh run list --commit <sha>` is a
   completed SUCCESS** on a push that touches `floatfea/` or `tests/`. Note that my
   corpus commit `b546aaa` and this verdict commit follow revision 6's own commit, so
   `test_the_whole_suite_line_is_about_a_commit_that_exists` will redden at them by
   construction until step 7's report regenerates that line -- which is the guard
   working, and is what the two intermediate failures in this round were.

**And the schedule.** F2 on **4 October** holds on this evidence: CI green at the
reviewed commit, `floatfea/` unchanged for the whole step, no value moved, and the one
blocking item is a comment and a figure. Nothing in this verdict slips a date, and
R540 needs no measurement that is not already in this file.
