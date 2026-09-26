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


# Revision 3 — the escalation resolved, and three of my sentences withdrawn

Answers: verdict 56 @ 18f51fc

**2026-09-23.**

## 0. CI at `9e02cb5`, the commit verdict 56 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 56 at `9e02cb5` through the report's own `Answers:` line. Run `35802624479`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 992 | 8 | 0 |
| the verification ladder | 1457 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 8.**

- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 56 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 56 at `9e02cb5` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `35802624479` | push | `9e02cb5` | conclusion **failure** |
| `35806252155` | push | `f7501ee` | conclusion **failure** |
| `35880641506` | push | `60999c9` | conclusion **failure** |

**Run `35802624479`, conclusion **failure**: 8 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `35806252155`, conclusion **failure**: 137 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R479]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R502]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R503]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R504]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R505]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R506]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R507]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R508]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R509]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R510]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R999]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R502-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R502-docs/reviews/F2/step-5.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R502-test_report_guard_states.py:307]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:369]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:370]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:371]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:372]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:373]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-scripts/localise_clean_worst.py:19]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-scripts/precommit_stale.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-scripts/regen_figures.py:176]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-test_figure_local_check.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_figure_local_check.py:54]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:8]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:103]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:115]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:118]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:119]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:122]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:123]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:124]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:125]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:126]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:127]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:128]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:129]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:130]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:58]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:59]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:60]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:61]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:62]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:63]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:64]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:65]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:66]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:67]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:68]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:69]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:70]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:71]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:314]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:319]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:324]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:325]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:326]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:327]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:328]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:329]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:330]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_modes.py:308]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_modes.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R505-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:103]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:115]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:118]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:119]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:122]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:123]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:124]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:125]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:126]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:127]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:128]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:129]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:130]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R507-frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R507-g22_model_configurations.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R507-tree_prose_claims.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R509-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

**Run `35880641506`, conclusion **failure**: 134 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R479]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R502]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R503]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R504]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R505]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R506]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R507]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R508]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R509]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R510]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R999]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R502-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R502-docs/reviews/F2/step-5.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R502-test_report_guard_states.py:307]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:369]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:370]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:371]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:372]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:373]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-scripts/localise_clean_worst.py:19]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-scripts/precommit_stale.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-scripts/regen_figures.py:176]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-test_figure_local_check.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_figure_local_check.py:54]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:8]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:115]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:118]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:119]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:122]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:123]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:124]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:125]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:126]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:127]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:128]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:129]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:130]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:58]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:59]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:60]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:61]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:62]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:63]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:64]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:65]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:66]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:67]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:68]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:69]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:70]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:71]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:314]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:319]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:324]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:325]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:326]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:327]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:328]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:329]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:330]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_modes.py:308]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_modes.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R505-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:115]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:118]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:119]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:122]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:123]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:124]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:125]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:126]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:127]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:128]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:129]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:130]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R507-g22_model_configurations.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R507-tree_prose_claims.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R509-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

## 0b. History since the commit verdict 56 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --history`, anchored on verdict 56 at `9e02cb5` through the report's own `Answers:` line. Commits this branch held and no longer holds, from `git reflog`. A rewrite is the right answer to some findings and it is never a silent one (CY0, R461). The reflog is LOCAL: a fresh clone has none, so this table is what was generated at the report's own commit and cannot be reproduced from the clone alone.

**No commit has left this branch's history since then.**

## 0c. Commits since the commit verdict 56 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --commits`, anchored on verdict 56 at `9e02cb5` through the report's own `Answers:` line. `git log --oneline <judged>..HEAD`, run at the report's own commit. This revision's own commit is not in it, because it does not exist yet when the section is generated.

```
788ce6f corpus: 14 unseen RUNNER-claim shapes (batch 6)
18f51fc review: F2 step 6 -- fifty-sixth verdict, HOLD @ 9e02cb5
f7501ee R502 and R503: the third R494(C), and an enforcement DC0 removed unm
3b5d6eb review: F2 step 5 -- fifty-seventh verdict, PASS @ f7501ee, the disp
53cfeee process: a step's disposition is its closure verdict, not the file's
7115410 plan: R486 leaves F2 and becomes a G3 gate (DD0, Xabier's ruling)
8945a4e DD2: the clearance comes back; the staleness comparison does not
60999c9 DD3: a reviewer's own write cannot close a site, and a fragment is n
5755de8 R506, R507: the deletion note keeps only what was measured
```

## 1. The reading

**Schedule: F2 closes 30 September if the next two verdicts hold nothing under
(a)–(d); F3 opens 1 October. It holds, and 31 October holds with it.** The
escalation went to Xabier and came back as **DD0**: R486 leaves F2 and becomes
a **G3 gate** — G2.1's residual and seventh-mode bound asserted on every member
of the *real* platform model at its real orientation, with the builder refusing
a platform that fails. What is given up is a claim about structures this
project is not building; what is bought is that the near-vertical members R486
exists to protect are checked on the platform itself, as a finite set. **R487
stays with R475** and does not follow R486: it is the one-line assertion
replacing the `content > 0` comment, a property of the residual form rather
than of a domain. **R502 was mine and my account of it was wrong** — I told the
reviewer "the other six cascade from baseline"; five do, and the eighth was
R494(C) a third time, in the commit that defined `_verdict_step()` to fix the
other two. **R503 is answered by restoring the clearance and not the
staleness** (DD2): eight floor-class rows are recomputed on the tree and
asserted against their own constants, never against the committed render.
**R511 is fixed in both halves** (DD3), and **the second half closes one of the
three live cases rather than three** — which is in the controls, not in a
sentence. **R506 and R507 withdrew three of my own sentences**: "it ran four
times", "every time", and a claim about CI that sat under a paragraph about a
check which compares nothing. **DB0 is next and it is the only substantive work
left before the rest of CZ2.**

```
cmd   the schedule DD4 sets, quoted and not measured
out   F2 closes 30 September if the next two verdicts hold nothing under
      (a)-(d); F3 opens 1 October; the first result 26 October; 31 October
      holds, which is what DD0 bought by moving R486
cmd   the eight floor-class rows, recomputed and compared with their ceilings
out   clean_worst_ratio 3.617x, counter_headroom_room 2.18x,
      rigid_mode_counter_seventh 1.603x, largest_rigid_eigenvalue 136.5x,
      mechanism_ceiling 130.9x, rigid_mode_residual 12.71x,
      residual_worst_over_corpus 6.916x, seventh_over_epsilon 1.204e+11x
cmd   the same test with one ceiling divided by 1e6
out   that row's margin becomes 3.617e-06x and the test reports THE DECISION
      MOVED -- so it is not vacuous
cmd   _tracked_at_reviewed on the three live R507 cases
out   frames.txt False; g22_model_configurations.txt True;
      tree_prose_claims.txt True -- one of three, and the other two are real
      files that are also printed output
cmd   git show cbf8520 --stat
out   one file, the prose-claims corpus, which moves no rendered row -- which
      is why "every time" is withdrawn
cmd   git show dae3b6c --stat, and the golden's diff in both directions
out   one line left the collected set AND one entered
      (test_the_plan_names_the_step_under_execution, in source at ccb5346 and
      not in the golden). My message accounted for one direction of a
      two-line diff, which is R508 and is recorded rather than rewritten.
```

**R494's four nested-run lines, which revision 2 did not carry (R505).** The
three negative controls that had been planting into a file the guard does not
read — `answers_header_names_a_sha_that_is_not_a_commit`,
`guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF`,
`guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED`
— reach the guard again; and `verdict_amended_after_the_commit_the_report_answers`
reaches it for the first time since DB2, which is R502.

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py docs/reviews/F2/step-6.md docs/reports/F2/step-6-answers.json`. The class and the subject are read from the verdict; the state and the site come from the answers file.

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
| R494 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R495 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R496 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R497 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R498 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R499 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R500 | carried | **open** | §2 | `scripts/answered_table.py` | carried from an earlier verdict |
| R501 | carried | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | carried from an earlier verdict |
| R502 | blocks | **answered** | §2 | `tests/test_report_guard_states.py` | and (d).) THE EIGHTH RED IS NOT A CASCADE. R494(C) IS |
| R503 | blocks | **answered** | §2 | `tests/test_plan_figures.py` | and (c).) DELETING THE STALENESS GUARD DELETED THE ONLY |
| R504 | recorded | **open** | §2 | `tests/verification/rung1/test_rigid_body_corpus.py` | (d). You asked for my read on the DB0 measurement |
| R505 | recorded | **answered** | §2 | `docs/reports/F2/step-6.md` | The report does not carry R494's four nested-run lines.** R494's |
| R506 | recorded | **answered** | §2 | `tests/test_plan_figures.py` | `tests/test_plan_figures.py:103-131`, the deletion note, states facts |
| R507 | recorded | **answered** | §2 | `tests/test_plan_figures.py` | The DC0 commit message and the deletion note both say the guard "went |
| R508 | recorded | **answered** | §2 | `docs/reports/F2/step-6.md` | `dae3b6c`'s message says "exactly one line left the collected set". |
| R509 | recorded | **open** | §2 | `scripts/answered_table.py` | R500, unchanged.** The generated subject column in |
| R510 | recorded | **open** | §2 | `floatfea/tolerances.py` | R501, unchanged.** R476 (`ZeroDivisionError` on a coincident tip node), |
| R511 | carried | **answered** | §2 | `tests/test_report_carried.py` | carried from an earlier verdict |
| R512 | carried | **open** | §2 | `tests/test_report_guard_states.py` | carried from an earlier verdict |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R502 | `docs/reviews/F2/step-5.md` | the file is untouched | **no change** -- a verdict file, which I never write; it is named as printed output inside a finding |
| R502 | `step-5.md` | the file is untouched | **no change** -- the verdict's short spelling of a file named above |
| R502 | `test_report_guard_states.py:307` | the file is touched and this line number is the old one | **no change** -- the verdict's short spelling of a file named above |
| R502 | `tests/corpus/report_guard_states.txt` | the file is untouched | **no change** -- the reviewer's corpus, refused to me |
| R503 | `floatfea/tolerances.py:365` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R503 | `floatfea/tolerances.py:369` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R503 | `floatfea/tolerances.py:370` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R503 | `floatfea/tolerances.py:371` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R503 | `floatfea/tolerances.py:372` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R503 | `floatfea/tolerances.py:373` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R503 | `floatfea/tolerances.py:374` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R503 | `scripts/localise_clean_worst.py:19` | the file is untouched | **no change** -- named in a carried item from an earlier verdict |
| R503 | `scripts/precommit_stale.py:92` | the file is untouched | **no change** -- named in a carried item from an earlier verdict |
| R503 | `scripts/regen_figures.py` | the file is untouched | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R503 | `scripts/regen_figures.py:176` | the file is untouched | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R503 | `scripts/regen_figures.py:228` | the file is untouched | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R503 | `test_figure_local_check.py` | the file is untouched | **no change** -- the verdict's short spelling of a file named above |
| R503 | `test_rigid_body_corpus.py` | the file is untouched | **no change** -- the verdict's short spelling of a file named above |
| R503 | `tests/test_figure_local_check.py:54` | the file is untouched | **no change** -- the vehicle changes there were REVERTED by DC0, since restoring the values restored the rows they used |
| R503 | `tests/test_plan_figures.py:8` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:104` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:105` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:106` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:107` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:108` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:116` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:117` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:118` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:119` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:120` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:121` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:122` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:123` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:124` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:125` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:126` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:127` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_plan_figures.py:128` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R503 | `tests/test_precommit_stale.py:58` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:59` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:60` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:61` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:62` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:63` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:64` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:65` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:66` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:67` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:68` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:69` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:70` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/test_precommit_stale.py:71` | the file is untouched | **no change** -- named in a carried item from an earlier verdict, not by anything this round asks for |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:314` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:315` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:316` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:317` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:318` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:319` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:320` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:321` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:322` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:323` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:324` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:325` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:326` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:327` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:328` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:329` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_corpus.py:330` | the file is untouched | **no change** -- named as where a claim is asserted, not as a site |
| R503 | `tests/verification/rung1/test_rigid_body_modes.py:308` | the file is untouched | **no change** -- this is DB0's site; the form is measured and not yet written, and the reference-point cell is why |
| R503 | `tests/verification/rung1/test_rigid_body_modes.py:316` | the file is untouched | **no change** -- this is DB0's site; the form is measured and not yet written, and the reference-point cell is why |
| R506 | `tests/test_plan_figures.py:104` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:105` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:106` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:107` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:108` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:116` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:117` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:118` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:119` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:120` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:121` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:122` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:123` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:124` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:125` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:126` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:127` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R506 | `tests/test_plan_figures.py:128` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R507 | `g22_model_configurations.txt` | the file is untouched | **no change** -- the reviewer's corpus, refused to me; it is named as a file that FEEDS a rendered row, not as a site |
| R507 | `tree_prose_claims.txt` | the file is untouched | **no change** -- the reviewer's corpus, refused to me. It reads as untouched now because DD3 excluded the reviewer's trees from the diff, which is the point of DD3 |

## 4. Carried

Generated: `python scripts/carried_table.py docs/reviews/F2/step-6.md docs/reports/F2/step-6-answers.json`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R471 | **open** — §2 | to R474, and the 48 items frozen in docs/milestones/F2a.md |
| R474 | **open** — §2 | , and the 48 items frozen in docs/milestones/F2a.md |
| R475 | **open** — carried from an earlier verdict | / R486 / R487 / R492 / R493 as open on top. |
| R476 | **open** — carried from an earlier verdict | ) -- OPEN closure items, restated as R510. |
| R477 | **open** — carried from an earlier verdict | ) -- OPEN closure items, restated as R510. |
| R478 | **open** — carried from an earlier verdict | ) -- OPEN closure items, restated as R510. |
| R479 | **open** — carried from an earlier verdict | CLOSED. Ten determinism legs ran and agreed at dae3b6c. Four |
| R480 | **open** — carried from an earlier verdict | ) -- OPEN closure items, restated as R510. |
| R482 | **carried** — §2 | carried into R494 and not separately live. |
| R486 | **carried** — §2 | / R487 / R492 / R493 as open on top. |
| R487 | **open** — §2 | / R492 / R493 as open on top. |
| R488 | **open** — §2 | ADOPTED, now with a reference-point cell against it. Not closed. |
| R489 | **open** — §2 | CLOSED in verdict 55; not reopened. |
| R490 | **carried** — §2 | CLOSED in verdict 55; not reopened. |
| R491 | **carried** — §2 | CLOSED in verdict 55; not reopened. |
| R492 | **open** — §2 | / R493 as open on top. |
| R493 | **open** — §2 | as open on top. |
| R494 | **carried** — §2 | and R496 as blocking, R497 to R501 as closure |
| R495 | **carried** — §2 | and R496 as blocking, R497 to R501 as closure |
| R496 | **carried** — §2 | as blocking, R497 to R501 as closure |
| R497 | **carried** — §2 | to R501 as closure |
| R498 | **carried** — §2 | CLOSED as recorded. Nothing to re-argue. |
| R499 | **carried** — §2 | CLOSED, and it is the red. assert STEP_REPORT == _PAIRED fires |
| R500 | **open** — §2 | OPEN, correctly not fixed, closure item, restated as R509. |
| R501 | **open** — §2 | as closure |
| R502 | **answered** — §2 | and (d).) THE EIGHTH RED IS NOT A CASCADE. R494(C) IS LIVE FOR THE THIRD TIME, AT... |
| R503 | **answered** — §2 | and (c).) DELETING THE STALENESS GUARD DELETED THE ONLY CALLER OF scripts/regen_figures.py... |
| R504 | **open** — §2 | -(d). You asked for my read on the DB0 measurement before writing it into the gate, which is... |
| R505 | **answered** — §2 | . I took the measurement. |
| R506 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R507 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R508 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R509 | **open** — §2 | OPEN, correctly not fixed, closure item, restated as R509. |
| R510 | **open** — §2 | OPEN closure items, restated as R510. |
| R999 | **open** — carried from an earlier verdict | ] and NOT |

## 5. The whole suite

**Whole suite at `028ac59`: 2258 passed, 0 failed, 0 skipped.** **The excluded set: 218 passed, 116 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 334 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R479]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R502]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R503]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R504]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R505]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R506]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R507]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R508]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R509]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R510]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R999]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_Carried_table_is_what_the_generator_produces`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_section_is_about_the_REVIEWED_commit`
- **failed, in the excluded set** `tests.test_report_carried::test_the_whole_suite_line_is_about_a_commit_that_exists`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R502-docs/reports/F2/step-6.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R502-docs/reviews/F2/step-5.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R502-test_report_guard_states.py:307]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:369]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:370]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:371]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:372]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:373]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-floatfea/tolerances.py:374]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-scripts/localise_clean_worst.py:19]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-scripts/precommit_stale.py:92]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-scripts/regen_figures.py:176]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-test_figure_local_check.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_figure_local_check.py:54]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:8]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:104]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:105]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:106]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:107]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:108]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:116]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:117]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:118]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:119]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:120]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:121]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:122]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:123]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:124]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:125]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:126]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:127]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_plan_figures.py:128]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:58]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:59]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:60]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:61]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:62]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:63]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:64]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:65]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:66]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:67]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:68]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:69]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:70]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/test_precommit_stale.py:71]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:314]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:315]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:316]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:317]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:318]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:319]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:320]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:321]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:322]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:323]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:324]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:325]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:326]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:327]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:328]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:329]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_corpus.py:330]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_modes.py:308]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R503-tests/verification/rung1/test_rigid_body_modes.py:316]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R505-docs/reports/F2/step-6.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:104]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:105]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:106]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:107]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:108]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:116]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:117]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:118]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:119]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:120]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:121]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:122]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:123]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:124]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:125]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:126]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:127]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R506-tests/test_plan_figures.py:128]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R507-g22_model_configurations.txt]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R507-tree_prose_claims.txt]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R509-docs/reports/F2/step-6.md]`
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
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]`
```

**What the excluded set's failures are, and why the number is what it is.**
They are the report-parametrised guards, measured in a clean worktree at the
commit this revision is committed ON TOP OF -- so they are judging a report
that does not yet carry verdict 56's findings, which is what this revision
is. `test_the_report_carries_the_finding[R479]` through `[R512]` are that
set. The line is taken before the edit it describes by rule (R309: run it
last, at the commit the report is committed from), so this is structural
rather than a defect, and the supervisor's own run at the commit that carries
this revision is what settles it.


# Revision 4 — R475 lands, and DF0 refutes the ceiling's hypothesis

Answers: verdict 58 @ 8a681b2

**2026-09-26.**

## 0. CI at `8e64f22`, the commit verdict 58 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 58 at `8e64f22` through the report's own `Answers:` line. Run `36234584744`, event `workflow_dispatch`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1047 | 4 | 0 |
| CI determinism -- leg (6) | 4 | 0 | 0 |
| CI determinism -- leg (10) | 4 | 0 | 0 |
| CI determinism -- leg (9) | 4 | 0 | 0 |
| the verification ladder | 1457 | 0 | 0 |
| CI determinism -- leg (8) | 4 | 0 | 0 |
| CI determinism -- leg (1) | 4 | 0 | 0 |
| CI determinism -- leg (4) | 4 | 0 | 0 |
| CI determinism -- leg (3) | 4 | 0 | 0 |
| CI determinism -- leg (2) | 4 | 0 | 0 |
| CI determinism -- leg (5) | 4 | 0 | 0 |
| CI determinism -- leg (7) | 4 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 13 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 5.**

- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

## 0a. Runs since the commit verdict 58 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 58 at `8e64f22` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `35890289681` | push | `365ae5b` | conclusion **failure** |
| `36218676882` | push | `44757be` | conclusion **failure** |
| `36234584744` | workflow_dispatch | `8e64f22` | conclusion **failure** |

**Run `35890289681`, conclusion **failure**: 12 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R518-tests/verification/rung1/test_new_thing.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R519-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R521-scripts/answered_table.py]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `36218676882`, conclusion **failure**: 13 failing test name(s) in the log.**
- `tests/test_plan_figures.py::test_every_floor_class_row_clears_its_tolerance_on_THIS_tree` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R518-tests/verification/rung1/test_new_thing.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R519-docs/reports/F2/step-6.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R521-scripts/answered_table.py]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `36234584744`, conclusion **failure**: 5 failing test name(s) in the log.**
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]` (lint, unit and guards)

## 0b. History since the commit verdict 58 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --history`, anchored on verdict 58 at `8e64f22` through the report's own `Answers:` line. Commits this branch held and no longer holds, from `git reflog`. A rewrite is the right answer to some findings and it is never a silent one (CY0, R461). The reflog is LOCAL: a fresh clone has none, so this table is what was generated at the report's own commit and cannot be reproduced from the clone alone.

**No commit has left this branch's history since then.**

## 0c. Commits since the commit verdict 58 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --commits`, anchored on verdict 58 at `8e64f22` through the report's own `Answers:` line. `git log --oneline <judged>..HEAD`, run at the report's own commit. This revision's own commit is not in it, because it does not exist yet when the section is generated.

```
be1d9e2 corpus: 13 unseen REPAIR-STALE shapes (batch 7)
8a681b2 review: F2 step 6 -- fifty-eighth verdict, HOLD @ 8e64f22
365ae5b R514-R518: five repairs, and the first one is BP0 turned on the entr
aa5ccf3 R475: the residual is normalised per row, shared across the six vect
531d106 process: the hook reads a step's disposition from its closure verdic
44757be process: corpus rounds target the element, the gates and the model (
```

## 1. The reading

**Schedule: F2 closes 2–3 October, not 30 September, and that slip is reported
the day it is known. F3 opens 1 October as planned and absorbs the
difference; 31 October holds.** **R475 has landed** (`aa5ccf3`): the residual
is normalised per row and shared across the six vectors, both counters redden
at every span on both DOF classes, the near-vertical band shows no false red,
and R487 is an assertion rather than a comment. **The ceiling did not move and
one thing about it is now red on CI**: `rigid_mode_residual_worst_over_corpus`
clears `RIGID_MODE_EXACTNESS` by **1.347x**, inside the declared platform
spread of 1.5x — found by DD2's own clearance test, which is the check R503
asked for doing its job on the commit that follows it. **DF0 was the cell that
would have justified re-deriving that ceiling as a round-off bound, and it
refutes its own hypothesis**: the term count does not track the residual and
does not explain why 6° is worse than 2.87°, so DF1 does not apply and nothing
about the tolerance has been touched. **Verdict 58's five blocking items are
answered** (`365ae5b`), including R514, which is BP0 turned on the entry that
cites BP0 — DD2 restored an enforcement in the test file and I never came back
to the tolerance entry, so five sentences described a closed gap for two
commits. **DE1 fixed the hook** and **DE2 scoped the corpus to the element,
the gates and the model through F6.** **Open and blocking:** the 1.347x
clearance, R521 and R522.

```
cmd   the ten span cells, bisected edges, both counters
out   k[0,0] edge 1.4745e-15 / 1.2871e-15 / 1.1656e-15 / 1.3529e-15 /
      1.2575e-15 at 4 m, 40 m, 400 m, 4 km, 40 km; counter 6.78x to 8.58x
      past it. k[3,3] edge 2.8290e-16 / 2.7739e-16 / 3.5384e-16 / 3.2089e-16 /
      3.3606e-16; counter 28.3x to 36.1x past it. Flat on both classes.
rule  the shipped assertion, residual > RIGID_MODE_EXACTNESS = 1e-15
out   under the OLD form the rotational defect read 1.00x of clean from 400 m
      up -- defective and clean frames the same number
cmd   the reference-point cell, span held at 4 m, both sides published
out   centroid clean 1.4462e-16, defective 3.7497e-14, RED; 10^3 spans away
      1.4319e-16 and 1.4319e-16, blind; 10^6 spans away 2.0449e-16 and
      2.0449e-16, blind
cmd   the near-vertical band, one cell per degree 0 to 10
out   clean 1.34e-16 to 1.80e-16, 0.124x to 0.180x of the ceiling
cmd   DD2's clearance test on CI, run 36218676882, conclusion **failure**
out   rigid_mode_residual_worst_over_corpus clears RIGID_MODE_EXACTNESS by
      1.347x, under the declared spread 1.5x -- and my laptop reproduces
      1.347x, so it is not a platform artefact
cmd   the corpus worst under the new form, top four
out   7.4255e-16 rb_tip_6deg_from_global_Z; 4.2508e-16, 4.2358e-16,
      4.1918e-16 the three 2.87-degree frames. The old form's worst was
      1.4459e-16.
cmd   DF0 over all 172 frames: residual/eps against the term count of the row
      the maximum occurs in
out   6 degrees 3.344 eps on a 4-term row; 2.87 degrees 1.914 eps on a 4-term
      row -- THE SAME COUNT, 1.75x apart. corr(residual/eps, terms) = -0.030.
      A 14-term row reads 1.080 eps and a 5-term row 0.363 eps.
out   worst structural row over the corpus 30 terms, max of
      residual/eps / terms 0.836, so a c*m*eps bound would be about 25 eps =
      5.6e-15, which LOOSENS the ceiling 5.6x rather than confirming it
out   cancellation is anti-correlated too, -0.467, and enormous on every
      frame: 9.59e+13 at the worst, 4.97e+16 at the mildest
```

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py docs/reviews/F2/step-6.md docs/reports/F2/step-6-answers.json`. The class and the subject are read from the verdict; the state and the site come from the answers file.

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
| R494 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R495 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R496 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R497 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R498 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R499 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R500 | carried | **open** | §2 | `scripts/answered_table.py` | carried from an earlier verdict |
| R501 | carried | **open** | §2 | `tests/verification/rung1/test_rigid_body_modes.py` | carried from an earlier verdict |
| R502 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R503 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R504 | carried | **open** | §2 | `tests/verification/rung1/test_rigid_body_corpus.py` | carried from an earlier verdict |
| R505 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R506 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R507 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R508 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R509 | carried | **open** | §2 | `scripts/answered_table.py` | carried from an earlier verdict |
| R510 | carried | **open** | §2 | `floatfea/tolerances.py` | carried from an earlier verdict |
| R511 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R512 | carried | **open** | §2 | `tests/test_report_guard_states.py` | carried from an earlier verdict |
| R514 | blocks | **answered** | §2 | `floatfea/tolerances.py` | .) R503 IS NOT CLOSED. YOU TOOK THE FIRST BRANCH OF THE |
| R515 | blocks | **answered** | §2 | `tests/test_plan_figures.py` | .) THE ENFORCEMENT 8945a4e RESTORED HAS NO NAMED DOMAIN. |
| R516 | blocks | **answered** | §2 | `tests/test_report_guard_states.py` | and (d).) `two_digit_step_number_discriminating` IS RED |
| R517 | blocks | **answered** | §2 | `tests/test_report_guard_states.py` | and (d).) THREE NEGATIVE CONTROLS CANNOT BE BUILT AT A |
| R518 | blocks | **answered** | §2 | `tests/test_report_carried.py` | .) `_tracked_at_reviewed` SILENTLY DROPS A SITE WHOSE |
| R519 | recorded | **answered** | §2 | `docs/reports/F2/step-6.md` | `docs/reports/F2/step-6.md` section 3 declares the R503 sites with a |
| R520 | recorded | **answered** | §2 | `docs/reports/F2/step-6.md` | R505, unchanged.** The four nested-run lines are still not in the |
| R521 | recorded | **open** | §2 | `scripts/answered_table.py` | R509, unchanged.** `scripts/answered_table.py` still takes the |
| R522 | recorded | **open** | §2 | `floatfea/tolerances.py` | R510, unchanged.** R476 (`ZeroDivisionError` on a coincident tip |
| R523 | recorded | **answered** | §2 | `docs/reports/F2/step-6.md` | No CI run exists at the reviewed commit, and that is now the second |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R514 | `CLAUDE.md` | the file is untouched | **no change** -- the finding cites the rule, not a site to edit |
| R514 | `floatfea/tolerances.py:388` | the file is touched and this line number is the old one | **no change** -- the sentences the finding names are restored by reverting the DB1 prose commit, not edited |
| R514 | `scripts/regen_figures.py:744` | the file is untouched | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R514 | `tests/test_plan_figures.py:103` | the file is touched and this line number is the old one | **no change** at this line -- the guard that stood here is deleted |
| R515 | `scripts/regen_figures.py` | the file is untouched | **no change** at this line -- the withdrawal mechanism that stood here is deleted, so there is no line to point at |
| R516 | `tests/corpus/report_guard_states.txt` | the file is untouched | **no change** -- the reviewer's corpus, refused to me |
| R516 | `tests/test_report_guard_states.py:587` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:588` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:589` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:590` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:591` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:592` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:593` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:594` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:595` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:596` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:597` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:598` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:599` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R516 | `tests/test_report_guard_states.py:606` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R517 | `docs/reviews/F2/step-6.md` | the file is untouched | **no change** -- a verdict file, which I never write |
| R517 | `tests/test_report_guard_states.py:414` | the file is touched and this line number is the old one | **no change** at this line -- the file is touched by DC1 and the line number is the old one |
| R518 | `g22_model_configurations.txt` | the file is untouched | **no change** -- the reviewer's corpus, refused to me; it is named as a file that FEEDS a rendered row, not as a site |
| R518 | `tests/test_report_carried.py:2652` | the file is touched and this line number is the old one | **no change** at this line -- touched by R494(C) and R499; the line number is the old one |
| R518 | `tests/verification/rung1/test_new_thing.py` | the file is untouched | **no change** -- this file does not exist and is not meant to. R518 names it as the example of a site a closing condition asks to be CREATED, which the rule used to drop silently; it is a control in test_the_R507_cases_rule_as_measured, not a file to write |
| R521 | `scripts/answered_table.py` | the file is untouched | **no change** -- R500 is a closure item and is not fixed in this step |

## 4. Carried

Generated: `python scripts/carried_table.py docs/reviews/F2/step-6.md docs/reports/F2/step-6-answers.json`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R475 | **open** — carried from an earlier verdict | / R486 / R487 / R488 / R492 / R493 / R500 / |
| R479 | **open** — carried from an earlier verdict | CLOSED in verdict 56; not reopened. |
| R486 | **carried** — §2 | / R487 / R488 / R492 / R493 / R500 / |
| R487 | **open** — §2 | / R488 / R492 / R493 / R500 / |
| R488 | **open** — §2 | / R492 / R493 / R500 / |
| R492 | **open** — §2 | / R493 / R500 / |
| R493 | **open** — §2 | / R500 / |
| R494 | **carried** — §2 | because the harness stopped asking", which is the whole content of R494. |
| R500 | **open** — §2 | R510 as closure items, and R475 / R486 / R487 / R488 / R492 / R493 / R500 / |
| R501 | **open** — §2 | as open on top. Verdict 57 added R511 (blocking), R512 and R513 |
| R502 | **carried** — §2 | and R503 as blocking, R504 as advisory, R505 to |
| R503 | **carried** — §2 | as blocking, R504 as advisory, R505 to |
| R504 | **open** — §2 | as advisory, R505 to |
| R505 | **carried** — §2 | Verdict 56 carried R502 and R503 as blocking, R504 as advisory, R505 to |
| R506 | **carried** — §2 | CLOSED, and closed the way I asked. 5755de8 keeps what |
| R507 | **carried** — §2 | CLOSED, and closed the way I asked. 5755de8 keeps what |
| R508 | **carried** — §2 | CLOSED as recorded. You recorded it rather than rewriting the |
| R509 | **open** — §2 | OPEN closure items, unchanged. |
| R510 | **open** — §2 | as closure items, and R475 / R486 / R487 / R488 / R492 / R493 / R500 / |
| R511 | **carried** — §2 | (blocking), R512 and R513 |
| R512 | **open** — §2 | and R513 |
| R513 | **open** — carried from an earlier verdict | R501 as open on top. Verdict 57 added R511 (blocking), R512 and R513 |
| R514 | **answered** — §2 | .) R503 IS NOT CLOSED. YOU TOOK THE FIRST BRANCH OF THE CONDITION AND LEFT THE ENTRY ASSERTING... |
| R515 | **answered** — §2 | .) THE ENFORCEMENT 8945a4e RESTORED HAS NO NAMED DOMAIN. FLIPPING TWO TOKENS IN THE GENERATOR... |
| R516 | **answered** — §2 | and (d).) two_digit_step_number_discriminating IS RED AT 8e64f22, IT IS THE ONE RED THAT MY... |
| R517 | **answered** — §2 | and (d).) THREE NEGATIVE CONTROLS CANNOT BE BUILT AT A STEP'S FIRST VERDICT, AND ONE OF THEM... |
| R518 | **answered** — §2 | .) _tracked_at_reviewed SILENTLY DROPS A SITE WHOSE PATH DID NOT EXIST AT THE REVIEWED COMMIT,... |
| R519 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R520 | **answered** — §2 | carried, and the verdict says nothing further about it here |
| R521 | **open** — §2 | carried, and the verdict says nothing further about it here |
| R522 | **open** — §2 | carried, and the verdict says nothing further about it here |
| R523 | **answered** — §2 | carried, and the verdict says nothing further about it here |

## 5. The whole suite

**Whole suite at `44757be`: 2283 passed, 1 failed, 0 skipped.** **The excluded set: 327 passed, 12 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 339 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed** `tests.test_plan_figures::test_every_floor_class_row_clears_its_tolerance_on_THIS_tree`
- **failed, in the excluded set** `tests.test_report_carried::test_the_whole_suite_line_is_about_a_commit_that_exists`
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
```

**The one failure in the main set is the finding, not an obstacle.**
`test_every_floor_class_row_clears_its_tolerance_on_THIS_tree` is DD2's check,
restored at R503, and it reddens on the clearance described in section 1. It fails identically on this laptop and on CI, so the decision is
deterministic rather than platform-carried. Neither `RIGID_MODE_EXACTNESS`
nor `FIGURE_FLOOR_CLASS_SPREAD` has been touched: DF0 was the cell that would
have justified re-deriving the ceiling and it refuted its own hypothesis, so
DF1 does not apply and the red stands as reported. The twelve in the excluded
set are the report-parametrised guards measured at the commit this revision
sits on, judging a report that does not yet carry verdict 58's findings --
which is what this revision is.
