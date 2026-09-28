
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

**Whole suite at `9bc35bc`: 2499 passed, 0 failed, 0 skipped.** **The excluded set: 213 passed, 13 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 226 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```

**Zero failed in the main set.** The count is RE-TAKEN at `9bc35bc` and the
reason is in the commit that moved it: CI at `eff9fc8` was red on three mypy
errors in the new element modules, which my local lint command does not run.
The first version of this line was taken at `eff9fc8` and read
`2499 passed, 0 failed` with 12 in the excluded set; the main count is the same
number at both commits because mypy is not a test.

**The excluded set is 13 and was 12**, and the thirteenth is
`test_the_guard_reads_the_step_being_worked_on`: step 7 has a report and no
verdict, which is the state that guard exists to report and the reason this
round is being invoked. The other twelve are the report-parametrised guards
measured before this revision was committed, exactly as in step 6's revision 6.


# Revision 2 — the corrected element

Answers: verdict 62 @ b52b370

**2026-09-27.**

## 0. CI at `acb5e8c`, the commit verdict 62 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 62 at `acb5e8c` through the report's own `Answers:` line. Run `36292692101`, event `workflow_dispatch`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1694 | 0 | 0 |
| CI determinism -- leg (1) | 134 | 0 | 0 |
| CI determinism -- leg (7) | 134 | 0 | 0 |
| CI determinism -- leg (5) | 134 | 0 | 0 |
| CI determinism -- leg (2) | 134 | 0 | 0 |
| lint, unit and guards | 935 | 8 | 0 |
| CI determinism -- leg (8) | 134 | 0 | 0 |
| CI determinism -- leg (4) | 134 | 0 | 0 |
| CI determinism -- leg (3) | 134 | 0 | 0 |
| CI determinism -- leg (9) | 134 | 0 | 0 |
| CI determinism -- leg (6) | 134 | 0 | 0 |
| CI determinism -- leg (10) | 134 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 13 jobs, 1 not green.**

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

## 0a. Runs since the commit verdict 62 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 62 at `acb5e8c` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `36292692101` | workflow_dispatch | `acb5e8c` | conclusion **failure** |
| `36294387943` | push | `968435a` | conclusion **failure** |
| `36312140561` | push | `e0ab508` | **no result** (`cancelled`) |
| `36312442705` | push | `fab11d0` | **no result** (`cancelled`) |
| `36312618782` | push | `6b39b78` | **no result** (`cancelled`) |
| `36312788571` | push | `41a200c` | conclusion **failure** |

**Run `36292692101`, conclusion **failure**: 8 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `36294387943`, conclusion **failure**: 63 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R541]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R542]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R543]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R541-beam.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R541-beam.py:276]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:865]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:866]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:867]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:868]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:869]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:870]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:871]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R542-tests/verification/rung2/test_consistent_mass.py:872]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:299]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:300]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:301]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:302]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:303]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:304]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:305]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:306]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:307]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:308]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-docs/conventions.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:170]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:171]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:172]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:173]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:174]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1375]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1376]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1377]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1378]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1379]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1380]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1381]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/tolerances.py:1382]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:16]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:17]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:18]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:19]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:20]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:21]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:22]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:24]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:25]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/verification/rung2/test_releases_and_links.py]` (lint, unit and guards)
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

**Run `36312788571`, conclusion **failure**: 43 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R541]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R542]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R543]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R541-beam.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R541-beam.py:276]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:299]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:300]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:301]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:302]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:303]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:304]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:305]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:306]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:307]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-beam.py:308]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-docs/conventions.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:170]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:171]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:172]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:173]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:174]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:16]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:17]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:18]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:19]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:20]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:25]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R543-tests/verification/rung2/test_releases_and_links.py]` (lint, unit and guards)
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

## 0b. History since the commit verdict 62 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --history`, anchored on verdict 62 at `acb5e8c` through the report's own `Answers:` line. Commits this branch held and no longer holds, from `git reflog`. A rewrite is the right answer to some findings and it is never a silent one (CY0, R461). The reflog is LOCAL: a fresh clone has none, so this table is what was generated at the report's own commit and cannot be reproduced from the clone alone.

| commit | left history at | subject |
|---|---|---|
| `0c410c4` | 2026-09-27 10:24Z | docs: step 7's closure artifact -- R541's blast radius, measured |
| `3f94d79` | 2026-09-27 10:18Z | R543: ROUNDOFF_IDENTITY's recorded basis, re-taken. No value mov |

## 0c. Commits since the commit verdict 62 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --commits`, anchored on verdict 62 at `acb5e8c` through the report's own `Answers:` line. `git log --oneline <judged>..HEAD`, run at the report's own commit. This revision's own commit is not in it, because it does not exist yet when the section is generated.

```
7d47828 corpus: 15 unseen stubby members on the axis V2.5's four checks cann
b52b370 review: F2 step 7 -- sixty-second verdict, HOLD @ acb5e8c
968435a R541: the shear term's SIGN in the interpolation was wrong, and the 
2048ad9 R542 + DN1: the assertion covers what it prints, and the shear coeff
e0ab508 R543: ROUNDOFF_IDENTITY's recorded basis, re-taken. No value moves.
87606e7 plan: AO4 -- the non-nesting claim is withdrawn, DN0's branch 2 reco
fab11d0 docs: step 7's closure artifact -- R541's blast radius, measured (DN
6b39b78 plan: G2.4's order band and the eigh-drift note join the frozen list
41a200c C15, C16, C17: the closure items with a site in the tree
```

## 1. The reading

**Schedule: F2 closes 5 October, F3 10 October, F4 and F5-prep 17 October, the
member-force table 20 October, the code-check screen 25 October. DM's revision
moved F2 and F3 one day right and that is the slip this step cost; it holds.**
**R541 is the first real element defect in sixty-three verdicts, and it is
answered at `968435a`** — the shear term's sign in `bending_interpolation` was
`+Φξ/6` and should have been `−Φξ/6`, which made the interpolation matrix
**singular at Φ=1 — a member well inside F3's own `L/D ≥ 2` limit**. **The step's
published headline finding was its artefact and is withdrawn**: the spaces are
nested, the two rises the earlier revision published are both `0.000e+00`
corrected, and §141 of the plan now quotes the withdrawn sentences rather than
deleting them. **R542 is answered at `2048ad9`** —
the assertion covers the whole range it prints and asserts the sign half of
DL0's band — and **R543 at `e0ab508`**, with no value moved. **DN0's second
branch applies**: the round-off-floor hypothesis is refuted where it matters and
so is rotary inertia, so the order question goes to F3 with both cells.
**DN1 ships the check that would have caught it**, and its counter is the shipped
sign flip. **C14–C19 are answered or recorded**; the stiffness is **bit-identical**
across the fix, so rung 1, `ΦᵀMΦ` and F4's inertia relief were never affected.

```
cmd   det of the interpolation matrix at L = 4
out   shipped   Phi=0 +6.667e-01  Phi=0.5 +3.333e-01  Phi=1 +0.000e+00  Phi=2 -6.667e-01
      corrected Phi=0 +6.667e-01  Phi=0.5 +1.000e+00  Phi=1 +1.333e+00  Phi=2 +2.000e+00
rule  the determinant must be positive for the interpolation to be solvable;
      corrected it is L(1+Phi)/6, the classical shear-flexible denominator
cmd   python -m pytest tests/verification/rung2 -q -s -k ENERGY
out   Phi=1e-3 1.4e-15, 1e-2 1.2e-15, 0.1 2.0e-15, 1 1.3e-15, 10 1.1e-15
rule  ROUNDOFF_IDENTITY = 1e-14, against the field's own strain energy
cmd   python -m pytest tests/verification/rung2 -q -s -k SIGN_FLIP
out   the shipped sign: 3.8957e-03, 3.8730e-02, 3.2971e-01, LinAlgError, 3.3041e-01
cmd   python -m pytest tests/verification/rung2 -q -s -k MONOTONE
out   free-free Phi=0: 0.000e+00  shipped: 0.000e+00
      pinned-pinned Phi=0: 0.000e+00  shipped: 0.000e+00
cmd   python -m pytest tests/verification/rung2 -q -s -k OWN_continuum
out   n=4 +2.7397e-04, n=8 +2.0096e-05, n=16 +1.9494e-06, n=32 +2.9424e-07,
      n=64 +6.0988e-08, n=128 +1.4059e-08 -- positive and falling, both planes
cmd   local_stiffness at L = 1, 4, 60 m in worktrees at 968435a~1 and HEAD, as bytes
out   bit-identical at all three spans
cmd   the round-off floor beside the discretisation error, planar bending only
out   n=16 error 1.9494e-06 floor 1.9340e-10 ratio 10.31;
      n=128 error 1.4059e-08 floor 1.2785e-08 ratio 4.34
cmd   rotary inertia off, against its own closed form
out   ratios 13.63, 10.31, 6.62, 4.47 -- identical to four figures
cmd   the five spans of the Phi->0 limit, in ULP
out   0.54, 0.54, 4.07, 2.02, 4.93 -- worst 1.0952e-15, headroom 9.13x not 45x
cmd   git log --format=%s -1 6b39b78 ; grep -n "5 October\|10 October" docs/milestones/F2.md
out   DM's schedule: F2 5 October, F3 10 October, F4 and F5-prep 17 October, the
      member-force table 20 October, the code-check screen 25 October. F2 and F3
      each moved one day right from DK4's dates, which is the slip this step cost.
cmd   local_mass at Phi = 1 on the SHIPPED sign, D = 0.6 m, t = 0.012 m
out   Phi = 1 falls at L = 1.5945 m, L/D = 2.66, a member of 277.5 kg:
      LinAlgError, Singular matrix. Corrected, max|m| = 9.885445e+01.
out   THESE ARE MINE AND THEY ARE NOT THE REVIEWER'S. Its verdict reports
      max|m| = 1.62e+30 for a 46 kg member and a LinAlgError on D = 3.0,
      t = 0.001 -- a different section. I carried its figures into a draft of
      this paragraph without re-measuring, which is the one thing a figure in a
      report may not be, and they are replaced by the run above.
cmd   git show 87606e7^:docs/milestones/F2.md, the withdrawn AO4 paragraph
out   it published 1.476e-04 free-free and 7.924e-05 pinned-pinned as the
      largest rises under refinement; both are 0.000e+00 on the corrected sign
cmd   git log --oneline b52b370..HEAD
out   the seven commits of this revision: 968435a R541, 2048ad9 R542 and DN1,
      e0ab508 R543, 87606e7 the plan, fab11d0 the closure artifact, 6b39b78 the
      frozen list, 41a200c C15 to C17
```

**C14 is answered here rather than in a table**: my invocation said "the two
report guards" and there are **three** — `tests/test_report_carried.py`,
`tests/test_report_numbers_are_sourced.py` and `tests/test_report_guard_states.py`
— and the third contributed seven of the eight failures the reviewer measured.
§5's line is taken over all three.

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`.

**R541, R542 and R543** are answered at `968435a`, `2048ad9` and `e0ab508`, each
with its own commit and its own measurements; §1 carries them. **R540** stays
answered from revision 1, at `d147f25`. **R533** stays frozen. **R475**, **R487**,
**R488**, **R492**, **R493**, **R500**, **R501**, **R513**, **R519**, **R521**,
**R522**, **R523**, **R524**, **R525**, **R526**, **R527**, **R528**, **R529**,
**R535**, **R538** and **R539** carry unchanged as the closure list, not
re-measured here.

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
| R533 | carried | **later** | §2 | `` | carried from an earlier verdict |
| R535 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R538 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R539 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R540 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R541 | blocks | **answered** | §1 | `` | , and it is the step's substance.) THE SHEAR TERM IN |
| R542 | blocks | **answered** | §1 | `` | .) `test_the_SHIPPED_element_approaches_its_OWN_continuum` |
| R543 | blocks | **answered** | §1 | `` | .) `ROUNDOFF_IDENTITY`'s RECORDED BASIS IS FALSIFIED BY THE |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R541 | `beam.py:232` | the file is touched and this line number is the old one | ANSWERED at `968435a` and the block MOVED -- the interpolation and its derivation were rewritten; not `no change` |
| R541 | `beam.py:276` | the file is touched and this line number is the old one | ANSWERED at `968435a` and the block MOVED -- the interpolation and its derivation were rewritten; not `no change` |
| R543 | `beam.py:299` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:300` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:301` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:302` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:303` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:304` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:305` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:306` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:307` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `beam.py:308` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `docs/conventions.md` | the file is untouched | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `floatfea/element/beam.py:170` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `floatfea/element/beam.py:171` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `floatfea/element/beam.py:172` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `floatfea/element/beam.py:173` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `floatfea/element/beam.py:174` | the file is touched and this line number is the old one | ANSWERED at `e0ab508` and the block MOVED -- the Reason paragraph carries the re-taken worst and headroom; not `no change`, and no value moved |
| R543 | `tests/regression/test_f2_shipped_matrices.py:16` | the file is touched and this line number is the old one | no change. The site expansion reaches these lines; R543 is about `ROUNDOFF_IDENTITY`'s recorded basis and these files only USE the constant |
| R543 | `tests/regression/test_f2_shipped_matrices.py:17` | the file is touched and this line number is the old one | no change. The site expansion reaches these lines; R543 is about `ROUNDOFF_IDENTITY`'s recorded basis and these files only USE the constant |
| R543 | `tests/regression/test_f2_shipped_matrices.py:18` | the file is touched and this line number is the old one | no change. The site expansion reaches these lines; R543 is about `ROUNDOFF_IDENTITY`'s recorded basis and these files only USE the constant |
| R543 | `tests/regression/test_f2_shipped_matrices.py:19` | the file is touched and this line number is the old one | no change. The site expansion reaches these lines; R543 is about `ROUNDOFF_IDENTITY`'s recorded basis and these files only USE the constant |
| R543 | `tests/regression/test_f2_shipped_matrices.py:20` | the file is touched and this line number is the old one | no change. The site expansion reaches these lines; R543 is about `ROUNDOFF_IDENTITY`'s recorded basis and these files only USE the constant |
| R543 | `tests/regression/test_f2_shipped_matrices.py:25` | the file is touched and this line number is the old one | no change. The site expansion reaches these lines; R543 is about `ROUNDOFF_IDENTITY`'s recorded basis and these files only USE the constant |
| R543 | `tests/verification/rung2/test_releases_and_links.py` | the file is untouched | no change. The site expansion reaches these lines; R543 is about `ROUNDOFF_IDENTITY`'s recorded basis and these files only USE the constant |

## 4. Carried

Generated: `python scripts/carried_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`.

**C15 is why this section also names items the table does not carry.** The
generator's row set and the guard's differ, which is now written into
`scripts/carried_table.py`'s own docstring rather than claimed away: **R523**,
**R524**, **R525** and **R528** are mentioned in the verdict as history rather
than as live items, and none is open or blocking.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R475 | **carried** — §2 | / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 / |
| R487 | **carried** — §2 | / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 / |
| R488 | **carried** — §2 | / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 / |
| R492 | **carried** — §2 | / R493 / R500 / R501 / R513 / R519 / R521 / R522 / |
| R493 | **carried** — §2 | / R500 / R501 / R513 / R519 / R521 / R522 / |
| R500 | **carried** — §2 | / R501 / R513 / R519 / R521 / R522 / |
| R501 | **carried** — §2 | / R513 / R519 / R521 / R522 / |
| R513 | **carried** — §2 | / R519 / R521 / R522 / |
| R519 | **carried** — §2 | / R521 / R522 / |
| R521 | **carried** — §2 | / R522 / |
| R522 | **carried** — §2 | - R475 / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 / |
| R523 | **carried** — §2 | / R524 / R525 / R526 / R527 / R528 / R529 / R533 / R535 / R538 / R539 and |
| R524 | **carried** — §2 | / R525 / R526 / R527 / R528 / R529 / R533 / R535 / R538 / R539 and |
| R525 | **carried** — §2 | / R526 / R527 / R528 / R529 / R533 / R535 / R538 / R539 and |
| R526 | **carried** — §2 | / R527 / R528 / R529 / R533 / R535 / R538 / R539 and |
| R527 | **carried** — §2 | / R528 / R529 / R533 / R535 / R538 / R539 and |
| R528 | **carried** — §2 | / R529 / R533 / R535 / R538 / R539 and |
| R529 | **carried** — §2 | / R533 / R535 / R538 / R539 and |
| R533 | **later** — §2 | / R535 / R538 / R539 and |
| R535 | **carried** — §2 | / R538 / R539 and |
| R538 | **carried** — §2 | / R539 and |
| R539 | **carried** — §2 | R523 / R524 / R525 / R526 / R527 / R528 / R529 / R533 / R535 / R538 / R539 and |
| R540 | **answered** — §2 | as blocking by name, |
| R541 | **answered** — §1 | , and it is the step's substance.) THE SHEAR TERM IN... |
| R542 | **answered** — §1 | .) test_the_SHIPPED_element_approaches_its_OWN_continuum ASSERTS OVER n = 4, 8, 16 AND REPORTS... |
| R543 | **answered** — §1 | .) ROUNDOFF_IDENTITY's RECORDED BASIS IS FALSIFIED BY THE SITES THIS STEP ADDED TO IT, IN THE... |

## 5. The whole suite

**Whole suite at `41a200c`: 2509 passed, 0 failed, 0 skipped.** **The excluded set: 210 passed, 42 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 252 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R541]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R542]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R543]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_Carried_table_is_what_the_generator_produces`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_section_is_about_the_REVIEWED_commit`
- **failed, in the excluded set** `tests.test_report_carried::test_the_whole_suite_line_is_about_a_commit_that_exists`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R541-beam.py:232]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R541-beam.py:276]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:299]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:300]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:301]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:302]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:303]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:304]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:305]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:306]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:307]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-beam.py:308]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-docs/conventions.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:170]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:171]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:172]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:173]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-floatfea/element/beam.py:174]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:16]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:17]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:18]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:19]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:20]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-tests/regression/test_f2_shipped_matrices.py:25]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R543-tests/verification/rung2/test_releases_and_links.py]`
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
```

**THIS FIGURE IS STALE AND IS STAMPED RATHER THAN RE-TAKEN (R568).** It was
measured at `41a200c`, which is now **24 commits behind HEAD**, and it reports
`0 failed` while the tree at HEAD reports `1 failed`. The rule that used to refuse
a line in this condition is retired under DR0, and the retirement note in
`tests/test_report_carried.py` records that this exact loss is realised here. Step
7 is closed, so the line is marked rather than regenerated.

**Zero failed in the main set.** The excluded set is **42** and was 13 at
revision 1's commit, and the jump is this revision: at `41a200c` the newest
report revision still answered verdict 61 while verdict 62 existed, so every
per-item guard for verdict 62's carry list was red. That is the guard asking for
this revision, and C14's correction is why the count now names all three files
rather than two.


# Revision 3 — verdict 68's carry list, and the load basis

Answers: verdict 68 @ 83c7ba5

**2026-09-28.**

## 0. NO CI SECTION, AND THE GENERATOR IS WHY

`python scripts/ci_section.py` refuses at this revision:

```
cmd   python scripts/ci_section.py
out   verdict 68 at `83c7ba5` does not name the commit it judged in its header,
      so there is no commit to report CI for.
cmd   git show 83c7ba5:<the verdict> | grep -n "Reviewed commit"
out   2:Reviewed commit: 0a660cede5b9a7031508ad517bfb908a7f4e7983
```

**The verdict does name it — in the header's plain form.** The generator reads the
BOLDED, backticked form in the body (`_JUDGED` at `scripts/ci_section.py:120`),
which is the R513 convention: the stamped header is normally the reviewer's corpus
commit and therefore not the commit judged, so the body carries the truth. **This
round the reviewer wrote no corpus commit** — deliberately, with the reason
recorded — so the header IS the judged commit and the body never restates it.

**Nothing here is hand-written in its place.** CX0 and R449 make a run's outcome
generated or absent, never typed, and DR1 freezes report apparatus so the
generator is not edited to accept the header. The consequence is stated rather
than worked around: **this revision reports no CI, and the run at `0a660ce` is
recorded in verdict 68 itself** — `lint, unit and guards` failure, `the
verification ladder` success, one failure on both platforms. That is the
reviewer's measurement, not mine.

## 1. The reading

**Schedule: DS2 and DQ2 by 2 October, F3 by 9 October, F4 by 16 October, the
member-force table 20 October, the code-check screen 25 October. DS2 has landed
early and 2 October holds. F3 on 9 October is the one I will not promise from
here** — the platform model is the largest piece left, nothing of it has started,
and DT4 requires the slip to be reported the day it is known rather than when the
step closes. **This revision exists because the `Carried` section owed verdict 68
its nine findings and BS0 makes that a build failure**, not because a review round
was requested: DT3 defers the next verdict until F3's platform model lands.
**R568 to R575 are answered at `e500ea0` and `ca6959a`**; **R567 carries by name**
and blocks at the next step. The load basis for the first result is the six DS1
design-wave cases at heading 0, and every output will carry that on its face.

```
cmd   the six DS1 cases, in ../HSP-runs at the pinned tag
out   T_full 10.0 12.5 14.0 15.0 16.2 20.0 s -> T_model 1.4142 1.7678 1.9799
      2.1213 2.2910 2.8284 s at H_model 0.4840 m; every case settled=True and
      exported; 1481.7 s total = 24.69 min for six
rule  DQ0's design-wave method at H = 1.86 * Hs = 24.2 m full scale, Froude-mapped
cmd   python -m pytest tests/verification/rung4/test_froude_scaling.py -q -s
out   20 passed; one exponent perturbed over seven quantities -- the
      declared-table check misses 0, the ROUND TRIP misses 7
cmd   git rev-list --count 41a200c..HEAD
out   the revision-2 suite line is that many commits stale and is stamped, not
      re-taken; the rule that would have refused it is retired under DR0
```

**Heading 45 degrees is not in the basis, and the reason is upstream.** The BEM
database is solved at a single wave heading, so no change to a study script
produces a 45-degree result — it needs a second BEM solve, measured at 3.66 h and
40.6 GB, ending in a commit that carries PR8 STEP 4's hydrostatic correction. That
is an HSP task pending Xabier's go-ahead, recorded in `docs/milestones/F2a.md`.
**THIS SENTENCE IS STRUCK (C8). It said the X-brace arms run along the diagonals,
so a 45-degree wave travels along one arm and puts its two end clusters most out of
phase. The arms are AXIAL, not diagonal**, and the reviewer confirmed it
independently: `CLUSTER_ANGLES_DEG = [0, 90, 180, 270]`, hubs at (+/-50, 0) and
(0, +/-50) m full scale. So it is the ZERO-degree heading that runs along an arm --
the heading the basis already contains -- and the causal clause was reasoning from
a geometry the repository does not have. A BG0 failure: a "so" with no cell.

**No replacement claim about which heading governs is written here**, because none
has been measured. Six periods at 0 degrees shows the frame's response; whether it
contains the worst arm load is open, and the member-force table will say which
heading it was computed at rather than which heading governs. The same false belief
is in `docs/milestones/F3.md:25` ("two diagonal arms") and is R576's third strand.

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`.

**R568** — the retirement note described one of the deleted test's two assertions;
the sha-exists half went unremarked and the loss is already realised, with the
revision-2 suite line naming a commit 24 behind HEAD. **R569** — I claimed
`test_collected_set_golden.py` carries the retired property and it does not.
**R570** — "twelve unbuilt" is 22. **R571, R572** — two dangling helper citations
the citation guard cannot see, and dead code. **R573** — the closure artifact cited
the retired test by name as the reason CI is red. **R574** — the freeze had no
ledger. **R575** — the heading-45 reason named the hardcoded argument and not the
single-heading database. All eight answered at `e500ea0`; **R567 carries**.

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
| R533 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R535 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R538 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R539 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R540 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R541 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R542 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R543 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R544 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R545 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R546 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R548 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R555 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R556 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R557 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R558 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R561 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R562 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R563 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R564 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R565 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R567 | recorded | **carried** | §2 | `` | BLOCKING, CARRIED. The tree is red at `0a660ce`, locally and in CI, and the |
| R568 | recorded | **answered** | §2 | `` | The loss statement is incomplete by one item -- the sha-existence half. |
| R569 | recorded | **answered** | §2 | `` | "WHAT CARRIES THE PROPERTY NOW" is refuted by the same two cells. |
| R570 | recorded | **answered** | §2 | `` | "it was true -- twelve are unbuilt" is 22 at the commit that publishes |
| R571 | recorded | **answered** | §2 | `` | Two dangling HELPER citations, which the citation guard cannot see |
| R572 | recorded | **answered** | §2 | `` | Dead code: `_last_commit_touching` at |
| R573 | recorded | **answered** | §2 | `` | `docs/closure/F2.md:206-214` now |
| R574 | recorded | **answered** | §2 | `` | `docs/milestones/F2a.md` carries no row for anything DR1 defers, so the |
| R575 | recorded | **answered** | §2 | `` | `scripts/run_floatsim_design_waves.py:22-27` gives an incomplete reason |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R568 | `tests/test_report_carried.py:2195` | the file is touched and this line number is the old one | ANSWERED at `e500ea0` and the block MOVED -- the retirement note was rewritten to carry both lost assertions and to withdraw the replacement claim; not `no change` |
| R568 | `tests/test_report_carried.py:2196` | the file is touched and this line number is the old one | ANSWERED at `e500ea0` and the block MOVED -- the retirement note was rewritten to carry both lost assertions and to withdraw the replacement claim; not `no change` |
| R568 | `tests/test_report_carried.py:2197` | the file is touched and this line number is the old one | ANSWERED at `e500ea0` and the block MOVED -- the retirement note was rewritten to carry both lost assertions and to withdraw the replacement claim; not `no change` |
| R568 | `tests/test_report_carried.py:2198` | the file is touched and this line number is the old one | ANSWERED at `e500ea0` and the block MOVED -- the retirement note was rewritten to carry both lost assertions and to withdraw the replacement claim; not `no change` |
| R568 | `tests/test_report_carried.py:2199` | the file is touched and this line number is the old one | ANSWERED at `e500ea0` and the block MOVED -- the retirement note was rewritten to carry both lost assertions and to withdraw the replacement claim; not `no change` |
| R569 | `tests/test_collected_set_golden.py` | the file is untouched | ANSWERED at `e500ea0` and the block MOVED -- the retirement note was rewritten to carry both lost assertions and to withdraw the replacement claim; not `no change` |
| R570 | `tests/test_report_guard_states.py:616` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:617` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:618` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:619` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:620` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:621` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:622` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:623` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R570 | `tests/test_report_guard_states.py:624` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The count moved from twelve to 22 in the F2a ledger; these line numbers are the verdict's and the text moved with the rewrite |
| R575 | `scripts/run_floatsim_design_waves.py:27` | the file is touched and this line number is the old one | ANSWERED at `e500ea0`. The docstring now names the single-heading BEM database as the binding constraint; the line moved with the rewrite |

## 4. Carried

Generated: `python scripts/carried_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R546 | **carried** — §2 | and R548. |
| R548 | **carried** — §2 | named R546 and R548. |
| R561 | **carried** — §2 | and R566. DR0 additionally |
| R562 | **carried** — §2 | and R566. DR0 additionally |
| R563 | **carried** — §2 | and R566. DR0 additionally |
| R564 | **carried** — §2 | and R566. DR0 additionally |
| R565 | **carried** — §2 | and R566. DR0 additionally |
| R566 | **open** — carried from an earlier verdict | . DR0 additionally |
| R567 | **carried** — §2 | -- BLOCKING, CARRIED. The tree is red at 0a660ce, locally and in CI, and the retirement did not... |
| R568 | **answered** — §2 | The loss statement is incomplete by one item -- the sha-existence half.... |
| R569 | **answered** — §2 | "WHAT CARRIES THE PROPERTY NOW" is refuted by the same two cells.... |
| R570 | **answered** — §2 | "it was true -- twelve are unbuilt" is 22 at the commit that publishes it.... |
| R571 | **answered** — §2 | Two dangling HELPER citations, which the citation guard cannot see because it reads test_ names... |
| R572 | **answered** — §2 | Dead code: _last_commit_touching at tests/test_report_carried.py:2133 has no caller. cmd grep... |
| R573 | **answered** — §2 | docs/closure/F2.md:206-214 now misattributes the red CI job and publishes a cmd that collects... |
| R574 | **answered** — §2 | docs/milestones/F2a.md carries no row for anything DR1 defers, so the freeze has no ledger. cmd... |
| R575 | **answered** — §2 | scripts/run_floatsim_design_waves.py:22-27 gives an incomplete reason for skipping heading 45,... |

## 5. The whole suite

**Whole suite at `ca6959a`: 2532 passed, 0 failed, 0 skipped.** **The excluded set: 236 passed, 12 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 248 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_answered_verdict_is_the_NEWEST_one`
- **failed, in the excluded set** `tests.test_report_numbers_are_sourced::test_every_number_in_prose_is_sourced_in_its_own_section[5. The whole suite]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
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

**Zero failed in the main set, and the excluded set is 12.** The twelve are the
report-parametrised guards measured at `ca6959a`, where the newest revision still
answered verdict 62 while verdict 68 existed -- the `Answers:` shape DT2's commit
recorded and this revision closes. They are not the retired commit-distance rule,
which no longer exists to fail.


# Revision 4 — verdict 69's STOP, and the four code findings answered

Answers: verdict 69 @ 4ff1008

**2026-09-28.**

## 0. CI, for the commit under review

```
cmd   python scripts/ci_section.py
out   no CI run at 2dc6a99dcaf8f48fd5fc0201284c688cd8af501e. A commit that was never pushed has no run, and a report cannot publish a table for it.
```

**The generator is right and nothing is hand-written in its place.** The chain it
walks now resolves -- this revision's `Answers:` header names verdict 69, and the
format correction at `4ff1008` made the verdict's bolded judged-commit line
parseable, which is what DU1 was for. What it resolves TO is a commit with no run,
because `2dc6a99` was never pushed: the F3 branch was rebased onto F2's head this
turn and `origin/F3` still stands at `6186eb4`, so publishing a run for it would
need a force-push of a branch that has already been pushed.

**That decision is not mine to take and the consequence is stated rather than
worked around.** CX0 and R449 make a run's outcome generated or absent, never
typed, so this revision reports no CI and the four CI guards stay red until the
branch reaches the remote. The reviewer had already recorded the same absence for
verdict 69 itself -- `origin/F3` is `6186eb4`, not CK2 -- and measured the tree
instead at the code-identical `c78d895`.

## 1. The reading

**The schedule first, because it moved. F3's plan puts its close at 10 October and
that date is gone**, and not because the work slipped: verdict 69 is a STOP at the
plan's *first executable step*, so nothing of the platform model can begin until
DJ1 reopens and re-locks. DT4 requires slippage to be reported the day it is known
and this is that day. Two consecutive steps have not closed carrying blocking
items, so the escalation CZ0 describes is not yet triggered, but the choice it
names is already visible and it is the supervisor's: **slip the date, or reduce
scope.** What is unblocked meanwhile is the section module — G3.3's exact
hollow-section formulae need no layout — and it is what I will build while DJ1 is
open. **R576 carries and is the only open blocking item**; R577, R578, R579, R581
and R570 are answered below, R567 was withdrawn by the verdict itself, and the
remaining reds at verdict 69 were the report-parametrised guards waiting on this
revision.

```
claim  the platform's four cluster arms are AXIAL, not diagonal, which is R576's
       second strand and is also the sentence struck from section 1 of revision 3
cmd    grep -n "CLUSTER_ANGLES_DEG =" ../HSP-runs/studies/platform-12buoy/platform_common.py
out    34:CLUSTER_ANGLES_DEG = np.array([0.0, 90.0, 180.0, 270.0])  # C4-a
rule   two crossing arms along +/-x and +/-y, so the ZERO-degree heading runs
       along one arm and 45 degrees runs between them
claim  DJ1's source does not exist, which is R576's first strand
cmd    find ../HSP-runs ../HSP-stable -name "*.yaml" -o -name "*.yml"
out    two 3-buoy-cluster decks, one semisub example, one orcaflex fixture --
       none of them the 12-buoy platform, whose deck is built in Python
claim  all 16 joints are two-rotation gimbals, so DJ0's assumption holds and F3's
       builder has no model to refuse on that ground
cmd    python scripts/measure_platform_joints.py
out    two-rotation gimbals: 16 of 16
out    worst released-moment leak at the joint point : 2.753e-15
rule   DJ0 -- two free moments released, the locked-axis moment transmitted,
       measured on the REACTION at the joint point rather than on the joint's name
cell   ONE VARIABLE, |attach_a|: at 0.0000 m (4 joints) the rank over all four
       constraint rows is 1; at 1.6890 m (12 joints) it is 3; the rank over the
       lock row is 1 in both. The first moves with the offset and is therefore the
       moment of the constraint FORCE about the reference point, not a joint moment
```

## 2. Findings, and every item carried

Generated: `python scripts/answered_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`.

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
| R533 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R535 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R538 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R539 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R540 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R541 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R542 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R543 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R544 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R545 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R546 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R548 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R555 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R556 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R557 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R558 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R561 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R562 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R563 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R564 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R565 | carried | **carried** | §2 | `` | carried from an earlier verdict |
| R567 | carried | **withdrawn** | §2 | `` | carried from an earlier verdict |
| R568 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R569 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R570 | carried | **answered** | §2 | `tests/test_report_guard_states.py:616-624` | carried from an earlier verdict |
| R571 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R572 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R573 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R574 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R575 | carried | **answered** | §2 | `` | carried from an earlier verdict |
| R576 | recorded | **carried** | §1 | `docs/milestones/F3.md` | F3's locked plan is wrong at its first executable step, in three |
| R577 | recorded | **answered** | §2 | `floatfea/io/reader.py` | `floatfea/io/reader.py::validate` enforces nothing from `scale`. |
| R578 | recorded | **answered** | §2 | `tests/verification/rung4/test_froude_scaling.py` | The DS2 counter's injection is inert, and its round-trip control |
| R579 | recorded | **answered** | §2 | `floatfea/io/froude.py` | The converter cannot express the two composite channels the schema |
| R580 | recorded | **answered** | §3 | `tests/test_report_guard_states.py` | 25 tests are red at `2dc6a99`, locally and in CI, up from one at |
| R581 | recorded | **answered** | §2 | `floatfea/io/froude.py` | `floatfea/io/froude.py:98` -- the lambda guard is defeated |

## 3. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R576 | `../HSP-runs/studies/platform-12buoy/platform_common.py` | the file is untouched | **no change** -- it is the evidence, not the defect, and `../HSP-runs` is read-only from FloatFEA under DS0. It is the file whose `CLUSTER_ANGLES_DEG = [0, 90, 180, 270]` refutes DJ1's "two diagonal arms". |
| R576 | `docs/milestones/F3.md` | the file is untouched | **no change, and deliberately.** R576 is the STOP and it is a PLAN finding. A plan changes only in a standalone `plan:` commit citing the directive that asked for it, and no directive has. Editing the locked plan to answer a finding against it is the implementer re-locking its own plan. |
| R576 | `docs/milestones/F3.md:24` | the file is untouched | **no change, and deliberately.** R576 is the STOP and it is a PLAN finding. A plan changes only in a standalone `plan:` commit citing the directive that asked for it, and no directive has. Editing the locked plan to answer a finding against it is the implementer re-locking its own plan. |
| R576 | `docs/milestones/F3.md:25` | the file is untouched | **no change, and deliberately.** R576 is the STOP and it is a PLAN finding. A plan changes only in a standalone `plan:` commit citing the directive that asked for it, and no directive has. Editing the locked plan to answer a finding against it is the implementer re-locking its own plan. |
| R576 | `docs/milestones/F3.md:26` | the file is untouched | **no change, and deliberately.** R576 is the STOP and it is a PLAN finding. A plan changes only in a standalone `plan:` commit citing the directive that asked for it, and no directive has. Editing the locked plan to answer a finding against it is the implementer re-locking its own plan. |
| R576 | `scripts/run_floatsim_design_waves.py` | the file is untouched | **no change.** The script is correct; what it records -- a single-heading BEM database -- is what makes DJ2's 45-degree heading unreachable. The finding is against the plan that locked the heading, not against the script that reports the constraint. |
| R577 | `docs/load-interchange-v1.md` | the file is untouched | **no change.** The schema sentence is right and DU0 re-locked it one commit before this verdict. The defect was that nothing enforced it, which is fixed in `floatfea/io/reader.py`, not here. |
| R577 | `scripts/run_floatsim_design_waves.py:57` | the file is untouched | **no change.** Line 57 is a docstring naming the study's Froude scale, and it is accurate. The verdict cites it as evidence that the converter had no caller in `floatfea/`, which is answered by `_validate_scale` rather than by editing the citation. |
| R578 | `docs/load-interchange-v1.md` | the file is untouched | **no change, and this is the site I looked at hardest.** Its sentence -- "measured, 7 of 7 planted exponent errors survived it" -- is TRUE; the verdict re-measured it through the shipped functions and got the same 7 of 7. The defect was the counter's evidence, not the schema's claim, so correcting the sentence would have replaced a true statement with a different true statement and left the counter blind. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:95` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:96` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:97` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:107` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:108` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:110` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:111` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:112` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:113` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:114` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:115` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:122` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:123` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:124` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:125` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:126` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:127` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:129` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:130` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:131` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:132` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:133` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:134` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:135` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:136` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:137` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R578 | `tests/verification/rung4/test_froude_scaling.py:138` | the file is touched and this line number is the old one | TOUCHED -- the whole counter is rewritten at `902301b`. The line numbers the verdict cites (95-141) are the old ones and do not survive the rewrite; this is `no change` only in the sense that those exact lines no longer exist. |
| R579 | `CLAUDE.md` | the file is untouched | **no change.** It is quoted -- "a wrong answer that looks right is worse than a crash" -- as the reason the silent half-scaling is (a) rather than latent. The governing file is not edited to answer a finding it governs. |
| R579 | `floatfea/io/froude.py:100` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:101` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:102` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:103` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:104` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:105` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:106` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:107` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:109` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:110` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:111` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:112` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:113` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:119` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:120` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:121` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:122` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:123` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R579 | `floatfea/io/froude.py:124` | the file is touched and this line number is the old one | TOUCHED at `902301b`: `COMPOSITE_BLOCKS`, `_refuse_uncovered` and the shared `_scale` body. `no change` does not apply. |
| R580 | `docs/reports/F2/step-7.md:887` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:888` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:889` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:890` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:891` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:892` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:893` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:894` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |
| R580 | `docs/reports/F2/step-7.md:895` | the file is touched and this line number is the old one | **no change at those exact lines.** 892-895 are revision 3's answer-table rows, which are generated output for a round that has closed. They are superseded by this revision's own generated tables rather than edited in place -- rewriting a past round's generated table would make the report disagree with the commit that produced it. |

## 4. Carried

Generated: `python scripts/carried_table.py <the newest verdict> docs/reports/F2/step-7-answers.json`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R562 | **carried** — §2 | 's constraint travelling with the backstop. This was the one verdict 68 would not |
| R567 | **withdrawn** — §2 | blocking by name and listed R568-R575 as closure items. The |
| R568 | **answered** — §2 | as closure items. The |
| R569 | **answered** — §2 | ANSWERED. The claim that test_collected_set_golden.py carries the retired |
| R570 | **answered** — §2 | NOT ANSWERED. The site was never touched. This is the one the report gets |
| R571 | **answered** — §2 | ANSWERED, both sites. tests/test_report_guard_states.py:268-273 no longer |
| R572 | **answered** — §2 | ANSWERED. cmd grep -rn "_last_commit_touching" tests scripts; out (no |
| R573 | **answered** — §2 | ANSWERED, AND RE-BROKEN BY THE NEXT COMMIT. docs/closure/F2.md:206-224 was |
| R574 | **answered** — §2 | ANSWERED. The four-row ledger is in docs/milestones/F2a.md, including |
| R575 | **answered** — §2 | as closure items. The |
| R576 | **carried** — §1 | F3's locked plan is wrong at its first executable step, in three independent places.... |
| R577 | **answered** — §2 | floatfea/io/reader.py::validate enforces nothing from scale. This is the direct answer to the... |
| R578 | **answered** — §2 | The DS2 counter's injection is inert, and its round-trip control cannot fail.... |
| R579 | **answered** — §2 | The converter cannot express the two composite channels the schema marks REQUIRED, and scaling... |
| R580 | **answered** — §3 | 25 tests are red at 2dc6a99, locally and in CI, up from one at verdict 68. R570 is not answered... |
| R581 | **answered** — §2 | floatfea/io/froude.py:98 -- the lambda guard is defeated by nan, inf and subnormals. cmd... |

## 5. The whole suite

**Whole suite at `4ff1008`: 2552 passed, 0 failed, 0 skipped.** **The excluded set: 200 passed, 22 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 222 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_a_blocking_item_is_not_routed_to_4a`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_a_CI_SECTION`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`
- **failed, in the excluded set** `tests.test_report_carried::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_section_is_about_the_REVIEWED_commit`
- **failed, in the excluded set** `tests.test_report_carried::test_the_reported_CI_counts_are_not_all_zero`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R570-tests/test_report_guard_states.py:616]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R570-tests/test_report_guard_states.py:617]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R573-docs/closure/F2.md:206]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R575-scripts/run_floatsim_design_waves.py:27]`
- **failed, in the excluded set** `tests.test_report_numbers_are_sourced::test_every_number_in_prose_is_sourced_in_its_own_section[0. NO CI SECTION, AND THE GENERATOR IS W]`
- **failed, in the excluded set** `tests.test_report_numbers_are_sourced::test_every_number_in_prose_is_sourced_in_its_own_section[1. The reading]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
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
