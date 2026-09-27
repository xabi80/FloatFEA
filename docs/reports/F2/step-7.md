
# Revision 1 — step 7: V2.5, V2.6 and the V6.1 golden

Answers: verdict 61 @ 52941f7

**2026-09-26.**

## 0. CI at `792c44e`, the commit verdict 61 judged — conclusion **SUCCESS**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 61 at `792c44e` through the report's own `Answers:` line. Run `36261451332`, event `push`, conclusion **success**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1493 | 0 | 0 |
| lint, unit and guards | 968 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 0 not green.**

**Failing tests named in the log: 0.**

## 0a. Runs since the commit verdict 61 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 61 at `792c44e` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `36261451332` | push | `792c44e` | conclusion **success** |
| `36264799088` | push | `52941f7` | **no result** (`cancelled`) |
| `36264799173` | workflow_dispatch | `52941f7` | conclusion **failure** |
| `36266335541` | push | `83bc146` | conclusion **failure** |
| `36267622049` | push | `0ffd6bd` | conclusion **failure** |
| `36289838984` | push | `258e26e` | conclusion **failure** |
| `36290218710` | push | `e28193e` | conclusion **failure** |
| `36290459980` | push | `a0f0f32` — **head not in current history** | conclusion **failure** |
| `36290472434` | push | `901a146` — **head not in current history** | conclusion **failure** |
| `36291053032` | push | `eff9fc8` | conclusion **failure** |

**Run `36264799173`, conclusion **failure**: 4 failing test name(s) in the log.**
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R540-test_rigid_body_corpus.py:218]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R540-test_rigid_body_corpus.py:219]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R540-tests/verification/rung1/test_rigid_body_corpus.py]` (lint, unit and guards)

**Run `36266335541`, conclusion **failure**: 12 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R540-test_rigid_body_corpus.py:199]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R540-test_rigid_body_corpus.py:216]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R540-test_rigid_body_corpus.py:219]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `36267622049`, conclusion **failure**: 0 failing test name(s) in the log.**

**Run `36289838984`, conclusion **failure**: 0 failing test name(s) in the log.**

**Run `36290218710`, conclusion **failure**: 0 failing test name(s) in the log.**

**Run `36290459980`, conclusion **failure**: 0 failing test name(s) in the log.**

**Run `36290472434`, conclusion **failure**: 0 failing test name(s) in the log.**

**Run `36291053032`, conclusion **failure**: 0 failing test name(s) in the log.**

## 0b. History since the commit verdict 61 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --history`, anchored on verdict 61 at `792c44e` through the report's own `Answers:` line. Commits this branch held and no longer holds, from `git reflog`. A rewrite is the right answer to some findings and it is never a silent one (CY0, R461). The reflog is LOCAL: a fresh clone has none, so this table is what was generated at the report's own commit and cannot be reproduced from the clone alone.

| commit | left history at | subject |
|---|---|---|
| `bd84ae8` | 2026-09-26 19:22Z | plan: the directive ledger, step 7's scope, the schedule -- C8 - |

## 0c. Commits since the commit verdict 61 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --commits`, anchored on verdict 61 at `792c44e` through the report's own `Answers:` line. `git log --oneline <judged>..HEAD`, run at the report's own commit. This revision's own commit is not in it, because it does not exist yet when the section is generated.

```
b546aaa corpus: 11 unseen frames on the REFUSED half of the new lambda_6 car
52941f7 review: F2 step 6 -- sixty-first verdict, PASS @ 792c44e (the step c
d147f25 closure: R540 and the code half of step 6's closure list
7d7175d plan: the directive ledger, step 7's scope, the schedule -- C8 -- RE
83bc146 docs: the closure artifact answers C2, C3, C4, C12 and C13
0ffd6bd V2.5: the consistent mass matrix, and G2.4's band is HELD with a fin
07f975c DL0: the Timoshenko pinned-pinned reference ships. DL1: FALLBACK TAK
258e26e plan: AO4 rewritten -- each assertion names its reference (DL0) -- R
e28193e V2.6: end releases and rigid links, with DJ0's gimbal (DL2)
add3beb ci: rung 2 is declared FULL, and its empty marker is deleted with it
eff9fc8 V6.1: the golden for what F2 ships, and what it deliberately does no
```

## 1. The reading

**Schedule: F2 closes 4 October, F3 9 October, F4 and F5-prep 17 October, the
member-force table 20 October, the code-check screen 25 October. It holds, and
both parallel tracks are open as of today rather than pending.** Step 7 is
DK2's whole scope and nothing else: **V2.5**, **V2.6**, the **V6.1 golden**.
**R540 is answered rather than carried** — verdict 61's one blocking item, the
`RIGID_MODE_BOUND` entry that described one direction of a constant used in two
— and it is answered at `d147f25` with no value moved, so step 7 opens carrying
no blocking item. **G2.4's band is the finding of this step.** AO4 pre-registered
a one-sided band against a cited closed form, and the reference described a
continuum the element does not discretise; DL0 replaced it with the exact
Timoshenko pinned-pinned frequency, which is shipped and verified by its two
limits, and **DL1's pre-registered fallback was then taken** because one cell
found a second obstacle DL0 could not have known: `Phi` is computed from the
element length, so the interpolation spaces are not nested and this element has
no monotone approach from above to **any** reference. **No tolerance was created
in this step** — not `FREE_FREE_FREQUENCY`, not `RIGID_LINK_CONSTRAINT`, both of
which §D5 anticipated — and every assertion added uses `ROUNDOFF_IDENTITY` or a
strict inequality. **One guard caught a real defect of mine**: rung 2 was still
declared empty in the ladder job, so 60 new tests ran in the suite and in no CI
job.

```
cmd   python -m pytest tests/verification/rung2 -q
out   60 passed
cmd   sh scripts/run_rung.sh full:tests/verification/rung2
out   run_rung: 60 collected, 0 failed, 0 errored, 0 skipped
rule  the ladder job's own declaration, which must name a populated rung as full
out   at e28193e it read `empty:` and test_every_test_in_the_suite_is_run_by_some_ci_job
      reported "60 of 2752 collected tests are run by no CI job"
cmd   python scripts/regen_f2_golden.py
out   tests/regression/f2_shipped_matrices.json: 126 recorded quantities
cmd   python -m pytest tests/regression/test_f2_shipped_matrices.py -q
out   130 passed
cmd   grep -n "4 October\|9 October\|17 October\|20 October\|25 October" docs/milestones/F2.md
out   the five dates above are DK4's, recorded in the plan at F2.md section 5i
      by commit 7d7175d: F2 4 October, F3 9 October, F4 and F5-prep 17 October,
      the member-force table 20 October, the code-check screen 25 October
cmd   git branch -a --format="%(refname:short)"
out   F2, F3, F5-prep, master and their remotes -- DL3's two parallel tracks are
      branches with a plan commit each, a0f0f32 and 901a146, not intentions
```

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`. The class and the subject are read from the verdict; the state and the site come from the answers file.

**R540** is answered at `d147f25`, both halves of its closing condition, and §1 carries the diff. **R530**, **R531**, **R532**, **R534**, **R536** and **R537** were step 6's and are closed by its closure commits `d147f25`, `7d7175d` and `83bc146`. **R533** stays frozen in `docs/milestones/F2a.md` as apparatus that is not extended. **R535**, **R538**, **R539**, and **R475**, **R487**, **R488**, **R492**, **R493**, **R500**, **R501**, **R513**, **R519**, **R521**, **R522**, **R523**, **R524**, **R525**, **R526**, **R527**, **R528**, **R529** carry unchanged as the closure list recorded in `docs/closure/F2-step6.md` §7, not re-measured here.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R475 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R487 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R488 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R492 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R493 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R500 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R501 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R513 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R519 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R521 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R522 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R523 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R524 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R525 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R526 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R527 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R528 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R529 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R530 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R531 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R532 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R533 | carried | **later** | §2 | `` | carried from an earlier verdict |
| R534 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R535 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R536 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R537 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R538 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R539 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R540 | blocks | **answered** | §1 | `` | . CARRIES BY NAME INTO STEP 7.) `floatfea/tolerances.py`'s |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R540 | `CLAUDE.md` | the file is untouched | no change. The verdict cites `CLAUDE.md` as the authority for where a tolerance lives, not as a site to edit; changing it would need a standalone `process:` commit citing a directive, and no directive asked for one |
| R540 | `floatfea/tolerances.py:359` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `floatfea/tolerances.py:360` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `floatfea/tolerances.py:361` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `floatfea/tolerances.py:362` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `floatfea/tolerances.py:363` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `floatfea/tolerances.py:364` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `floatfea/tolerances.py:365` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `floatfea/tolerances.py:366` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The entry was rewritten at `d147f25`; these line numbers are the verdict's and the text is now at `tolerances.py:381-424`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `test_rigid_body_corpus.py:199` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The comment was rewritten at `d147f25` and is now at `test_rigid_body_corpus.py:212-231`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `test_rigid_body_corpus.py:216` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The comment was rewritten at `d147f25` and is now at `test_rigid_body_corpus.py:212-231`. Not `no change`, because the lines did change -- see section 1 |
| R540 | `test_rigid_body_corpus.py:219` | the file is touched and this line number is the old one | ANSWERED AND THE BLOCK MOVED. The comment was rewritten at `d147f25` and is now at `test_rigid_body_corpus.py:212-231`. Not `no change`, because the lines did change -- see section 1 |

## 4. Carried

Generated: `python scripts/carried_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`.

**Four items the generator's row set does not carry, named here because the
guard reads this section and the generator and the guard disagree about them.**
`scripts/carried_table.py` builds its rows from the verdict's finding headings
and its own Carried section; `tests/test_report_carried.py` also counts every
`R<n>` the verdict MENTIONS. **R523**, **R524**, **R525** and **R528** are
mentioned in the sixty-first verdict as history rather than as live items --
R523 and R528 in its account of how step 6 went, R524 as the near-vertical
refutation that retired the row-shared form, R525 as the shape of a figure I
misread. None of them is open, none is blocking, and none was re-measured in
this step. The disagreement is itself recorded rather than papered over: the
generator's docstring claims it uses the same rule as the guard, and for these
four it does not.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R475 | **carried** — §2 | / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / |
| R487 | **carried** — §2 | / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / |
| R488 | **carried** — §2 | / R492 / R493 / R500 / R501 / R513 / R519 / R521 / |
| R492 | **carried** — §2 | / R493 / R500 / R501 / R513 / R519 / R521 / |
| R493 | **carried** — §2 | / R500 / R501 / R513 / R519 / R521 / |
| R500 | **carried** — §2 | / R501 / R513 / R519 / R521 / |
| R501 | **carried** — §2 | / R513 / R519 / R521 / |
| R513 | **carried** — §2 | / R519 / R521 / |
| R519 | **carried** — §2 | / R521 / |
| R521 | **carried** — §2 | closure items, R475 / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / |
| R522 | **carried** — §2 | / R526 / R527 / R529 as open on top, the 48 frozen 4a items, and four closing |
| R526 | **carried** — §2 | / R527 / R529 as open on top, the 48 frozen 4a items, and four closing |
| R527 | **carried** — §2 | / R529 as open on top, the 48 frozen 4a items, and four closing |
| R529 | **carried** — §2 | as open on top, the 48 frozen 4a items, and four closing |
| R530 | **answered** — §2 | and R531 as blocking, R532 to R539 as |
| R531 | **answered** — §2 | as blocking, R532 to R539 as |
| R532 | **answered** — §2 | to R539 as |
| R533 | **later** — §2 | FROZEN, correctly. docs/milestones/F2a.md:153-160 records the |
| R534 | **answered** — §2 | PARTIALLY ANSWERED. _stretched and _defect are deleted. Closure |
| R535 | **carried** — §2 | OPEN closure items, not re-measured here, and closure |
| R536 | **answered** — §2 | ANSWERED, and the answer is a real one. python scripts/rigid_counter_response.py |
| R537 | **answered** — §2 | ANSWERED. Section 0 of revision 6 records run 36256042985 at |
| R538 | **carried** — §2 | OPEN closure items, not re-measured here, and closure |
| R539 | **carried** — §2 | Verdict 60 was a HOLD carrying R530 and R531 as blocking, R532 to R539 as |
| R540 | **answered** — §1 | . CARRIES BY NAME INTO STEP 7.) floatfea/tolerances.py's RIGID_MODE_BOUND ENTRY STILL SAYS THE... |

## 5. The whole suite

**Whole suite at `eff9fc8`: 2499 passed, 0 failed, 0 skipped.** **The excluded set: 241 passed, 12 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 253 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
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

**Zero failed in the main set.** The twelve in the excluded set are the
report-parametrised guards, measured at `eff9fc8` -- the commit this revision
sits on, where no step-7 report existed yet -- so they were judging step 6's
report with two implementer commits after it, which is the condition they exist
to report. The same twelve stood in step 6's revision 6 for the same reason.

