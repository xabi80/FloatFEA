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
