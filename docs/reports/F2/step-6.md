# Revision 1 — F2-rung2 opens, and DB0 is not in it

Answers: verdict 54 @ e32ae1e

**2026-09-22.**

## 0. CI at `7d6a94e`, the commit verdict 54 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 54 at `7d6a94e` through the report's own `Answers:` line. Run `35682754448`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1073 | 9 | 0 |
| the verification ladder | 1430 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 12.**

- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R481-tests/test_report_carried.py:1402]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R481-tests/test_report_carried.py:1403]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R481-tests/test_report_carried.py:1404]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 54 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 54 at `7d6a94e` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `35682754448` | push | `7d6a94e` | conclusion **failure** |
| `35742557389` | workflow_dispatch | `c2e2ddc` | **no result** (`cancelled`) |
| `35742558572` | push | `c2e2ddc` | **no result** (`cancelled`) |
| `35743308312` | push | `e884dbc` | **no result** (`cancelled`) |
| `35743513831` | workflow_dispatch | `e884dbc` | conclusion **failure** |

**Run `35682754448`, conclusion **failure**: 12 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R481-tests/test_report_carried.py:1402]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R481-tests/test_report_carried.py:1403]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R481-tests/test_report_carried.py:1404]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `35743513831`, conclusion **failure**: 11 failing test name(s) in the log.**
- `tests/test_plan_figures.py::test_the_generated_figures_are_not_stale` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0b. History since the commit verdict 54 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --history`, anchored on verdict 54 at `7d6a94e` through the report's own `Answers:` line. Commits this branch held and no longer holds, from `git reflog`. A rewrite is the right answer to some findings and it is never a silent one (CY0, R461). The reflog is LOCAL: a fresh clone has none, so this table is what was generated at the report's own commit and cannot be reproduced from the clone alone.

| commit | left history at | subject |
|---|---|---|
| `277c127` | 2026-09-22 14:37Z | DB2: the generator and the carry guard take the step from the pl |

## 0c. Commits since the commit verdict 54 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --commits`, anchored on verdict 54 at `7d6a94e` through the report's own `Answers:` line. `git log --oneline <judged>..HEAD`, run at the report's own commit. This revision's own commit is not in it, because it does not exist yet when the section is generated.

```
3e2417f corpus: 27 unseen frames at the orientation-degeneracy floor (batch 
e32ae1e review: F2 step 5 -- fifty-fourth verdict, HOLD @ 7d6a94e, on the ta
7f13c93 plan: the plan names the step under execution (DB2)
422d608 DB2: the generator and the carry guard take the step from the plan
c2e2ddc DB1: a corpus-derived count stops being a published figure
e884dbc DB1: the plan, the tolerance entries and the closure artifact cite t
4333fb2 DB2: the step under execution is the LATER of the plan line and the 
a697a53 DB1: the canonical render, and a withdrawn row is a words row
```

## 1. The reading

**Schedule: F2-rung2 by 30 September, F2 closed with it, F3 opening 1 October
with the two lock questions. It holds; the date moved from 28 to 30 September
at DB4 and nothing since has moved it.** This step opens with rulings, not with
element work. **DB2** takes the step number out of two literals and into one
line of the plan, which is what made the boundary permanently red: the
generator could only produce a section for step 5, so step 6 could not have a
report, so nothing could answer step 5's closing verdict. The first version of
it took the plan's line whenever that step had a report, and your own
`two_digit_step_number` state caught it — an injected step-10 pair with the
plan left at 5 — so the step is now the **later** of the plan line and the
newest complete pair, which is right in both directions. **DB1** stops
publishing any figure that moves when the corpus grows, verified two ways, and
the citations in the plan and in `tolerances.py` now name the test
that asserts the claim instead of quoting a count. **DB0 is not in this commit
and that is the point of R484 through R488**: the prescribed energy form is
refuted, my candidate is refuted by your near-vertical cell, and the row-shared
form you measured is the one being adopted — with your reference-point cell as
its own test, which is R485's finding turned into a gate. **R491 is answered by
deleting the row rather than correcting it** (DB1 reaches it too), and **R492's
sentence in `_analytic_rigid_body` is left standing until DB0 lands**, because
the reason the point matters is exactly what that commit measures. **Open and
not claimed:** R487's `content > 0` guard, R489's citation convention, R493's
four earlier closure items, and the 48 frozen 4a items.

```
cmd   the AST walk of _figures(), tainting every local assigned from a corpus
out   0 published rows still read a corpus (41 tainted locals)
cmd   diff the two CI renders either side of the corpus going 126 -> 145
out   8 rows moved; of those, still published under DB1: 0
cmd   python -m pytest tests/test_report_guard_states.py -q
out   8 failed, 18 passed at the previous commit -- every one of the eight is
      the same root cause, the whole-suite line with six code commits after
      revision 27, which this report is what closes
cmd   git diff -- floatfea/ over the DB1 prose commit, comments stripped
out   0 changed lines
cmd   the schedule DB4 set, quoted and not measured
out   F2-rung2 and F2 closed by 30 September, moved there from 28 September;
      F3 opens 1 October; CZ3 moves from 5 to 7 October; F4 and the first
      result on 26 October hold
cmd   grep -c "^| R" docs/milestones/F2a.md
out   48
cmd   count the rows of the CI render whose value is a DB1 withdrawal
out   51 -- and `49` stood in this paragraph, taken from a laptop render
      before the last two rows were withdrawn
cmd   count withdrawn {{fig:}} citations at e884dbc^ in the two live files
out   65 in the plan and 20 in tolerances.py, 85 in all
```

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py docs/reviews/F2/step-5.md docs/reports/F2/step-6-answers.json`. The class and the subject are read from the verdict; the state and the site come from the answers file.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R223 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R224 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R230 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R231 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R244 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R245 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R275 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R323 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R324 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R325 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R330 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R331 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R332 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R333 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R334 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R335 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R336 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R337 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R338 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R339 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R340 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R341 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R342 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R343 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R344 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R345 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R346 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R347 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R348 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R349 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R350 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R351 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R352 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R353 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R354 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R355 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R356 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R357 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R358 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R359 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R360 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R361 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R362 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R363 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R364 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R365 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R366 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R367 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R368 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R369 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R370 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R371 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R372 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R373 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R374 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R375 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R376 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R377 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R378 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R379 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R380 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R381 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R382 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R383 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R384 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R385 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R386 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R387 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R388 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R389 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R390 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R391 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R392 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R393 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R394 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R395 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R396 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R397 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R398 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R399 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R400 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R401 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R402 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R403 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R404 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R405 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R406 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R407 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R408 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R409 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R410 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R411 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R412 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R413 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R414 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R415 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R416 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R417 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R418 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R419 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R420 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R421 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R422 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R423 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R424 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R425 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R426 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R427 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R428 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R429 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R430 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R431 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R432 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R433 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R434 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R435 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R436 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R437 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R438 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R439 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R440 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R441 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R442 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R443 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R444 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R445 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R446 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R447 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R448 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R449 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R450 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R451 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R452 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R453 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R454 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R455 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R456 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R457 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R458 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R459 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R460 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R461 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R462 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R463 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R464 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R465 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R466 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R467 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R468 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R469 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R470 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R471 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R472 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R473 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R474 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R482 | blocks | **answered** | §2 | `tests/test_report_carried.py` | , and it is the whole reason this is a HOLD.) The suite |
| R483 | recorded | **answered** | §2 | `tests/test_report_carried.py` | THE ANSWER TO THE QUESTION YOU ASKED: the guard is NOT failing false, |
| R484 | recorded | **answered** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | DA0's FORM IS REFUTED, I REPRODUCED YOUR NEGATIVE RESULT, AND THERE |
| R485 | recorded | **answered** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | YOUR DIAGNOSIS IS RIGHT ABOUT THE MECHANISM AND WRONG ABOUT THE |
| R486 | blocks | **answered** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | , the form of a tolerance and the ceiling it would |
| R487 | recorded | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | THE `content > 0` GUARD IS NOT AN IMPLEMENTATION DETAIL AND YOU WERE |
| R488 | recorded | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | YOUR THIRD QUESTION -- would a third form be better than either |
| R489 | recorded | **open** | §2 | `tests/test_report_carried.py` | My own citation convention caused three of the twelve CI reds, and |
| R490 | recorded | **answered** | §2 | `scripts/regen_figures.py` | The tail exists because a reviewer corpus commit invalidates a |
| R491 | recorded | **answered** | §2 | `docs/closure/F2-step5.md` | `docs/closure/F2-step5.md` sections 1 and 4 still publish the row |
| R492 | recorded | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | `_analytic_rigid_body():161-164` -- any point gives the same |
| R493 | recorded | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | The four earlier closure items, unchanged.** R476 |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R482 | `test_report_guard_states.py` | the file is untouched | **no change** -- the harness is named as the thing that CAUGHT the defect, not as a site to edit. The repair is in `tests/test_report_carried.py` |
| R483 | `CLAUDE.md` | the file is untouched | **no change** -- the finding cites the rule, and the rule is what the repair follows rather than something to rewrite |
| R483 | `docs/milestones/F2a.md` | the file is untouched | **no change** -- the frozen list. The item is recorded there already and CZ0 freezes what would be added to it |
| R489 | `tests/test_report_carried.py:1385` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1386` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1387` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1388` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1389` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1390` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1391` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1392` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1393` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1394` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1395` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1396` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1397` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1398` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1399` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1400` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1401` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1402` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1403` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:1404` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |
| R489 | `tests/test_report_carried.py:2451` | the file is touched and this line number is the old one | **no change** at these line numbers -- the file is touched and the block moved; the repair is in the commit this item's row names |

## 4. Carried

Generated: `python scripts/carried_table.py docs/reviews/F2/step-5.md docs/reports/F2/step-6-answers.json`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R383 | **open** — §2 | ), R480 -- OPEN, closure items, correctly not |
| R459 | **carried** — §2 | to R470 -- closed in verdicts 52 and 53, not reopened. |
| R470 | **carried** — §2 | closed in verdicts 52 and 53, not reopened. |
| R471 | **open** — §2 | to R474 and the 48 items frozen in docs/milestones/F2a.md section |
| R474 | **open** — §2 | and the 48 items frozen in docs/milestones/F2a.md section |
| R475 | **open** — carried from an earlier verdict | OPEN, AND THIS ROUND IS WORK ON IT, NOT AN ANSWER TO IT. |
| R476 | **open** — carried from an earlier verdict | (R383), R480 -- OPEN, closure items, correctly not |
| R477 | **open** — carried from an earlier verdict | (R383), R480 -- OPEN, closure items, correctly not |
| R478 | **open** — carried from an earlier verdict | (R383), R480 -- OPEN, closure items, correctly not |
| R479 | **open** — carried from an earlier verdict | (R383), R480 -- OPEN, closure items, correctly not |
| R480 | **open** — carried from an earlier verdict | OPEN, closure items, correctly not |
| R481 | **open** — carried from an earlier verdict | ANSWERED AT THE SITE, AND ITS CONDITION IS ONLY PARTLY CLOSED. |
| R482 | **answered** — §2 | , and it is the whole reason this is a HOLD.) The suite is not red on one test. It is red on... |
| R483 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R484 | **answered** — §2 | to R488 are my answers to the three |
| R485 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R486 | **answered** — §2 | , the form of a tolerance and the ceiling it would carry.) THE CANDIDATE HAS A DEFECT YOU HAVE... |
| R487 | **open** — §2 | carried, and the verdict says nothing further about it here |
| R488 | **open** — §2 | are my answers to the three |
| R489 | **open** — §2 | , which is my fault and not yours. |
| R490 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R491 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R492 | **open** — §2 | carried, and the verdict says nothing further about it here |
| R493 | **open** — §2 | carried, and the verdict says nothing further about it here |

## 5. The whole suite

**Whole suite at `82cadeb`: 2127 passed, 0 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit, excluding 373 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py) -- which the supervisor runs at the commit that carries it. R339: the count of what is excluded is part of the line, so a reader can size it without running anything.


# Revision 2 — DB1's second half reversed, and the boundary is the last red

Answers: verdict 55 @ 48d45e0

**2026-09-22.**

## 0. CI at `ccb5346`, the commit verdict 55 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 55 at `ccb5346` through the report's own `Answers:` line. Run `35751444035`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 791 | 8 | 0 |
| the verification ladder | 1457 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 13.**

- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R489-tests/test_report_carried.py:1403]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R489-tests/test_report_carried.py:1404]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R489-tests/test_report_carried.py:2451]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

## 0a. Runs since the commit verdict 55 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 55 at `ccb5346` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `35751444035` | push | `ccb5346` | conclusion **failure** |
| `35757030579` | push | `3aa804c` | conclusion **failure** |
| `35798434072` | workflow_dispatch | `dae3b6c` | conclusion **failure** |
| `35798434217` | push | `dae3b6c` | **no result** (`cancelled`) |
| `35800434872` | push | `c58810d` | conclusion **failure** |

**Run `35751444035`, conclusion **failure**: 13 failing test name(s) in the log.**
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R489-tests/test_report_carried.py:1403]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R489-tests/test_report_carried.py:1404]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R489-tests/test_report_carried.py:2451]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

**Run `35757030579`, conclusion **failure**: 15 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

**Run `35798434072`, conclusion **failure**: 18 failing test name(s) in the log.**
- `tests/test_collected_set_golden.py::test_every_test_name_cited_in_prose_exists[tests/test_plan_figures.py:test_the_generated_figures_are_not_stale]` (lint, unit and guards)
- `tests/test_figure_local_check.py::test_the_spread_bound_is_bracketed_by_its_own_measurements` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R491-docs/closure/F2-step5.md]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

**Run `35800434872`, conclusion **failure**: 14 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R491-docs/closure/F2-step5.md]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R498-ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R498-docs/SUPERVISOR.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R498-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R500-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0b. History since the commit verdict 55 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --history`, anchored on verdict 55 at `ccb5346` through the report's own `Answers:` line. Commits this branch held and no longer holds, from `git reflog`. A rewrite is the right answer to some findings and it is never a silent one (CY0, R461). The reflog is LOCAL: a fresh clone has none, so this table is what was generated at the report's own commit and cannot be reproduced from the clone alone.

**No commit has left this branch's history since then.**

## 0c. Commits since the commit verdict 55 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --commits`, anchored on verdict 55 at `ccb5346` through the report's own `Answers:` line. `git log --oneline <judged>..HEAD`, run at the report's own commit. This revision's own commit is not in it, because it does not exist yet when the section is generated.

```
cbf8520 corpus: 16 unseen POINTER-claim shapes, the sentence DB1 put where a
48d45e0 review: F2 step 5 -- fifty-fifth verdict, HOLD @ ccb5346
3aa804c R494: the verdict path, and the harness that plants at a path DB2 mo
3861d89 DC0: DB1's second half is reversed, and the staleness guard is delet
dae3b6c golden: the collected set loses test_the_generated_figures_are_not_s
c58810d DC1: the harness copies the verdict that exists, and the render is r
f79b017 R497: the whole-suite line says whether the EXCLUDED set is red
decee6d R499: the boundary assertion asks the pair, not the plan line
```

## 1. The reading

**Schedule: F2-rung2 and F2 closed by 30 September, F3 opening 1 October. It
holds.** The technical supervisor reversed DB1's second half on reading verdict
55 — both of its non-live findings were consequences of emptying the figures
rather than of the work — so **DC0** restores every corpus-derived value and
**deletes** `test_the_generated_figures_are_not_stale`, with the golden
regenerated in its own commit and the reason recorded: *a staleness check whose
domain includes reviewer-owned data reports the reviewer's work as the
implementer's defect.* R495 dies with the revert and R496 with the deletion;
neither is patched. **R494 is answered in all three mechanisms** — the harness
now resolves both the report and the verdict the way the guard does, which is
R494(C) one level out and the same confusion I fixed in the guard last round
and left here. **R497 is answered in the line itself**: the whole-suite line
carries the excluded set's own result, because "0 failed" while all eight
failures sat inside the excluded files is a false impression of the tree, and
my own message to the reviewer said so in words the line did not. **R499 is a
regression DB2 caused and it is fixed**: the boundary assertion asks the newest
complete pair again, so it fires at the state it was written for. **DB0 is
measured but not written** — the row-shared form closes all ten span cells at
the centroid and **fails the reference-point cell**, which puts it on DC3's
contingency branch. **The last red is the boundary itself** and it does not
clear without a verdict on step 6.

```
cmd   the reference-point cell, span HELD at 4 m, the point moved
out   centroid 259.28x red; 10^3 spans away 1.00x; 10^6 spans away 1.00x;
      and the same on all three axes -- so the form is blind away from the
      centroid and the centroid is load-bearing
cmd   the ten span cells at the centroid, defect 1e-14 of max|K|
out   k[0,0] 38.61x to 58.16x and k[3,3] 159.48x to 259.28x, red at every
      span, which is R475 closed on the axis it was found on
cmd   grep -c "_withdrawn\|_WITHDRAWN" scripts/regen_figures.py
out   0
cmd   sha256 of the CI render on legs 1 and 4, ten-legs-agree green
out   01d5080eea240f54f4f28c0e75ba80adb476267a87bea11beef601a69a46a364
cmd   the schedule DB4 set and DC4 holds, quoted and not measured
out   F2-rung2 and F2 closed by 30 September; F3 opens 1 October
cmd   the verdict this revision answers, from its own Answers: line
out   verdict 55, at 48d45e0
cmd   python -m pytest tests/test_report_carried.py -q
out   3 failed -- two are this report being older than the code, which this
      revision is, and the third is the R499 assertion correctly saying that
      step 6 has a report and no verdict yet
```

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py docs/reviews/F2/step-5.md docs/reports/F2/step-6-answers.json`. The class and the subject are read from the verdict; the state and the site come from the answers file.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R223 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R224 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R230 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R231 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R244 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R245 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R275 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R323 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R324 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R325 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R330 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R331 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R332 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R333 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R334 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R335 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R336 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R337 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R338 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R339 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R340 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R341 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R342 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R343 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R344 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R345 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R346 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R347 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R348 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R349 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R350 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R351 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R352 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R353 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R354 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R355 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R356 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R357 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R358 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R359 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R360 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R361 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R362 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R363 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R364 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R365 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R366 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R367 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R368 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R369 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R370 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R371 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R372 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R373 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R374 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R375 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R376 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R377 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R378 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R379 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R380 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R381 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R382 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R383 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R384 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R385 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R386 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R387 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R388 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R389 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R390 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R391 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R392 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R393 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R394 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R395 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R396 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R397 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R398 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R399 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R400 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R401 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R402 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R403 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R404 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R405 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R406 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R407 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R408 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R409 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R410 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R411 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R412 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R413 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R414 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R415 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R416 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R417 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R418 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R419 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R420 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R421 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R422 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R423 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R424 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R425 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R426 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R427 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R428 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R429 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R430 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R431 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R432 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R433 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R434 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R435 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R436 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R437 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R438 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R439 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R440 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R441 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R442 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R443 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R444 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R445 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R446 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R447 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R448 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R449 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R450 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R451 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R452 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R453 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R454 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R455 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R456 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R457 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R458 | carried | **open** | §2 | `` | carried from an earlier verdict |
| R459 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R460 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R461 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R462 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R463 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R464 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R465 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R466 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R467 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R468 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R469 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R470 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R471 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R472 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R473 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R474 | carried | **open** | §2 | `docs/milestones/F2a.md` | carried from an earlier verdict |
| R482 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R483 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R484 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R485 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R486 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R487 | carried | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | carried from an earlier verdict |
| R488 | carried | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | carried from an earlier verdict |
| R489 | carried | **open** | §2 | `tests/test_report_carried.py` | carried from an earlier verdict |
| R490 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R491 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R492 | carried | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | carried from an earlier verdict |
| R493 | carried | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | carried from an earlier verdict |
| R494 | blocks | **answered** | §2 | `tests/test_report_guard_states.py` | and (c).) THE EIGHT ARE NOT ONE ROOT CAUSE AND NONE OF |
| R495 | blocks | **answered** | §2 | `floatfea/tolerances.py` | .) DB1 DELETED THE ONLY TWO MACHINE-CHECKED BRACKETS ON |
| R496 | blocks | **answered** | §2 | `scripts/regen_figures.py` | .) FIFTY-ONE OF THE SIXTY-FOUR ROWS OF THE CANONICAL |
| R497 | recorded | **answered** | §2 | `scripts/suite_count.py` | The whole-suite line is green by excluding the file that holds every |
| R498 | recorded | **answered** | §2 | `docs/reports/F2/step-6.md` | The two process errors you put in front of me, ruled on. |
| R499 | recorded | **answered** | §2 | `tests/test_report_carried.py` | DB2 made `test_the_guard_reads_the_step_being_worked_on` silent on the |
| R500 | recorded | **open** | §2 | `scripts/answered_table.py` | The generated tables in `docs/reports/F2/step-6.md` sections 2 and 4 |
| R501 | recorded | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | The four earlier closure items, unchanged.** R476 (`ZeroDivisionError` |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R494 | `docs/re-views/F2/step-6.md` | the file is untouched | **no change** -- a verdict file for step 6 does not exist yet, which is the finding, not a site I may write |
| R494 | `docs/reports/F2/step-5.md` | the file is untouched | **no change** -- step 5's report is closed; this step's report is where the answer goes |
| R494 | `step-10.md` | the file is untouched | **no change** -- a file the guard-state harness creates inside a copy of the repository; it does not exist in the tree |
| R494 | `test_report_guard_states.py:207` | the file is touched and this line number is the old one | **no change** -- the verdict's short spelling of a file named above |
| R494 | `tests/corpus/report_guard_states.txt` | the file is untouched | **no change** -- the reviewer's corpus, refused to me |
| R494 | `tests/test_report_carried.py:146` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:147` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:148` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:149` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:150` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:151` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:152` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:235` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:237` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:238` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:239` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:241` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:242` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:243` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R494 | `tests/test_report_carried.py:244` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R495 | `floatfea/tolerances.py:365` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R495 | `floatfea/tolerances.py:384` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R495 | `floatfea/tolerances.py:385` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R495 | `floatfea/tolerances.py:386` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R495 | `scripts/regen_figures.py:228` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R495 | `scripts/regen_figures.py:921` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R495 | `test_corpus_configurations.py` | the file is untouched | **no change** -- the verdict's short spelling of a file named above |
| R495 | `test_rigid_body_modes.py:308` | the file is untouched | **no change** -- the verdict's short spelling of a file named above |
| R495 | `tests/verification/rung1/test_rigid_body_corpus.py` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R495 | `tolerances.py:369` | the file is touched and this line number is the old one | **no change** -- the verdict's short spelling of a file named above |
| R496 | `scripts/regen_figures.py:921` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:922` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:923` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:924` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:925` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:926` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:927` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:928` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:929` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:930` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:931` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:932` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:933` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:934` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:935` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:936` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:937` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:938` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:939` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:940` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:941` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:942` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:943` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:944` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:945` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:946` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:947` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:948` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:949` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:950` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R496 | `scripts/regen_figures.py:951` | the file is touched and this line number is the old one | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R498 | `CLAUDE.md` | the file is untouched | **no change** -- the finding cites the rule, not a site to edit |
| R498 | `ci_section.py` | the file is untouched | **no change** -- the verdict's short spelling of a file named above |
| R498 | `docs/SUPERVISOR.md` | the file is untouched | **no change** -- the witness's own instructions; they change only in a standalone process: commit, and no directive this round asked for one |
| R498 | `scripts/ci_section.py` | the file is untouched | **no change** at this line -- touched by DB2; the line number is the old one |
| R499 | `.claude/hooks/require-verdict.sh` | the file is untouched | **no change** -- named as the reader the protection had fallen back onto; the repair is in the guard |

## 4. Carried

Generated: `python scripts/carried_table.py docs/reviews/F2/step-5.md docs/reports/F2/step-6-answers.json`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R29 | **open** — carried from an earlier verdict | 's half-of-an-item rule asks. |
| R459 | **carried** — §2 | to R470 -- closed in verdicts 52 and 53, not reopened. |
| R470 | **carried** — §2 | closed in verdicts 52 and 53, not reopened. |
| R471 | **open** — §2 | to R474 and the 48 items frozen in docs/milestones/F2a.md |
| R474 | **open** — §2 | and the 48 items frozen in docs/milestones/F2a.md |
| R475 | **open** — carried from an earlier verdict | as blocking and listed R489 to R493 as closure items, |
| R476 | **open** — carried from an earlier verdict | ) -- OPEN closure items, correctly untouched. |
| R477 | **open** — carried from an earlier verdict | ) -- OPEN closure items, correctly untouched. |
| R478 | **open** — carried from an earlier verdict | ) -- OPEN closure items, correctly untouched. |
| R480 | **open** — carried from an earlier verdict | ) -- OPEN closure items, correctly untouched. |
| R482 | **carried** — §2 | NOT ANSWERED. Same item, one round on. Its closing condition |
| R483 | **carried** — §2 | answered in verdict 54; not reopened. |
| R484 | **carried** — §2 | answered in verdict 54; not reopened. |
| R485 | **carried** — §2 | answered in verdict 54; not reopened. |
| R486 | **carried** — §2 | OPEN, carried into that same commit. Correctly not touched. |
| R487 | **open** — §2 | OPEN. The content > 0 one-line assertion is not in this |
| R488 | **open** — §2 | ADOPTED, not closed. The directive takes the row-shared form. I |
| R489 | **open** — §2 | to R493 as closure items, |
| R490 | **carried** — §2 | ANSWERED BY DB1, AND THE RULING IS THE ONE I WOULD HAVE CHOSEN. |
| R491 | **carried** — §2 | ANSWERED by deleting the row. Correct: condition (ii) of R475 |
| R492 | **open** — §2 | OPEN, deliberately, until DB0 lands. Agreed; I said so. |
| R493 | **open** — §2 | as closure items, |
| R494 | **answered** — §2 | and (c).) THE EIGHT ARE NOT ONE ROOT CAUSE AND NONE OF THEM IS THE WHOLE-SUITE LINE. I isolated... |
| R495 | **answered** — §2 | .) DB1 DELETED THE ONLY TWO MACHINE-CHECKED BRACKETS ON RIGID_MODE_BOUND AND LEFT THE SENTENCE... |
| R496 | **answered** — §2 | .) FIFTY-ONE OF THE SIXTY-FOUR ROWS OF THE CANONICAL RENDER ARE NOW A STRING COMPUTED FROM THE... |
| R497 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R498 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R499 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R500 | **open** — §2 | carried, and the verdict says nothing further about it here |
| R501 | **open** — §2 | carried, and the verdict says nothing further about it here |

## 5. The whole suite

**Whole suite at `decee6d`: 2257 passed, 0 failed, 0 skipped.** **The excluded set: 203 passed, 14 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 217 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

- **failed, in the excluded set** `tests.test_report_carried::test_the_guard_reads_the_step_being_worked_on`
- **failed, in the excluded set** `tests.test_report_carried::test_the_whole_suite_line_is_about_a_commit_that_exists`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R491-docs/closure/F2-step5.md]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[two_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[shallow_clone_depth_1]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[shallow_clone_depth_1_reports_one_diagnosis_not_sixteen]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]`
