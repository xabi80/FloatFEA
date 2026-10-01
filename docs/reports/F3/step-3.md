# F3 step 3 — R624 answered, the ceiling derived, and F3 closed

Answers: verdict 83 @ 580b183

**2026-10-01.**

## 0. CI at `29570e1`, the commit verdict 83 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 83 at `29570e1` through the report's own `Answers:` line. Run `36861000264`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1186 | 9 | 0 |
| the verification ladder | 1826 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 9.**

- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

## 0a. Runs since the commit verdict 83 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 83 at `29570e1` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `36861000264` | push | `29570e1` | conclusion **failure** |
| `36867957796` | push | `c4d4817` | conclusion **failure** |
| `36875204695` | push | `b105de1` | conclusion **failure** |
| `36880810745` | push | `0d911ce` | conclusion **failure** |
| `36898482589` | push | `47daa3d` | conclusion **failure** |

**Run `36861000264`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

**Run `36867957796`, conclusion **failure**: 68 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R624]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R625]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R626]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R616-docs/milestones/F3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:311]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:312]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:313]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:314]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/model/platform.py:319]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:319]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:324]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:325]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:326]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:327]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-floatfea/tolerances.py:328]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-tests/verification/rung3/test_platform_rigid_modes.py:99]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-tolerances.py:347]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-tolerances.py:348]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-tolerances.py:349]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-tolerances.py:350]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-tolerances.py:351]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R624-tolerances.py:352]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:118]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-floatfea/element/rigid.py:119]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-io/reader.py:314]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-rigid.py:100]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-rigid.py:101]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-rigid.py:102]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R625-test_consistent_mass.py:497]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R626-test_platform_skeleton.py:696]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R626-test_platform_skeleton.py:698]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R626-test_platform_skeleton.py:705]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R626-test_platform_skeleton.py:707]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R626-tests/verification/rung3/test_platform_rigid_modes.py:26]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R626-tests/verification/rung3/test_platform_rigid_modes.py:224]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

**Run `36875204695`, conclusion **failure**: 1 failing test name(s) in the log.**
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

**Run `36880810745`, conclusion **failure**: 8 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `36898482589`, conclusion **failure**: 8 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 1. The reading

**F3's expected close date: this step.** Step 3 is EG0 + EG1 + EG3 + the closure
artifact, and all four are in the tree. **F3 closes by 13 October: YES, and by
9 October: YES** — on which EG5(b) applies, so **I propose pulling F4 to
16 October**; the reasoning and what it rests on are in §7.

R624 is answered and it was the last blocking item anyone could answer. **R629**, verdict 83's one red, was answered at `0d911ce` before this step opened: every Carried pointer had been the same section, so the planted state was the shipped one and the control could not fail. One number
in the directive and one in my own commit message were wrong and both are corrected
below.

## 2. EG0 — R624 answered: the window, and the one number EG0 and I disagree on

```
claim  the window the sixteen members leave, and its geometric centre
cmd    element_rigid_residual over the sixteen, clean and under each counter at
       the declared injection; then sqrt(floor * roof)
out    CLEAN WORST over the 16          3.528257e-19   on hub2:buoy5_arm
out    dropped_flip     weakest 1.891035e-16   worst 3.656327e-16
out    wrong_dof_index  weakest 9.140177e-15   worst 9.459456e-15
out    rotational_block weakest 3.776640e-18   worst 1.464442e-17
out    WEAKEST over 16 x 3              3.776640e-18   (rotational_block)
out    the window  (3.528257e-19, 3.776640e-18)   width 10.70x
out    its GEOMETRIC CENTRE             1.154338e-18
rule   EG0(a): window = (clean worst over the 16, WEAKEST counter response over
       the 16 members x 3 counters at the declared 1e-14 injection); ceiling =
       the window's geometric centre
judge  EG0'S PARENTHETICAL SAID "approximately 2.27e-18" AND THAT IS A DIFFERENT
       WINDOW'S CENTRE -- `(3.528257e-19, 1.464442e-17)`, taking the counter's
       WORST-member response where the definition says the WEAKEST over sixteen
       members and three counters. I implemented the definition, and the
       difference is not cosmetic: at 2.27e-18 the window is unbalanced
       `6.44x / 1.66x` and the THIN side is the counter's, which is the side the
       constant exists to keep open. At 1.154338e-18 it is 3.27x either way.
```

## 3. EG0(b) and (c) — 16/16, and the second machine

```
claim  each counter reddens every member, and by how much
cmd    python -m pytest tests/verification/rung3/test_platform_rigid_modes.py -q
out    dropped_flip     16/16 reddened, weakest 1.8910e-16 =  163.8x the ceiling
out    wrong_dof_index  16/16 reddened, weakest 9.1402e-15 = 7918.1x the ceiling
out    rotational_block 16/16 reddened, weakest 3.7766e-18 =    3.3x the ceiling
out    window (3.528257e-19, 3.776640e-18) width 10.70x; the ceiling sits 3.27x
       above the floor and 3.27x below the roof
rule   EG0(b): registration is asserted 16/16 per counter, not "some member"
judge  `rotational_block` is the binding counter at 3.3x, which is the same fact
       the window's roof records. The other two are three and four decades clear.

claim  EG0(c)'s stop condition, on both machines
cmd    test_EG0_the_CEILING_is_the_window_it_claims_to_be, which asserts it
out    this machine: the clean worst is 3.27x inside the ceiling -- no STOP
rule   EG0(c): if either machine's clean worst comes within 2x of the ceiling,
       STOP and report; do not move it
judge  THE SECOND MACHINE IS A TEST RESULT AND NOT A PROMISE. The condition is a
       shipped assertion, so CI measures it at every push and a machine that
       disagrees reddens rather than going unnoticed. CI's reading at this
       commit is in section 0.
```

## 4. EG0's side effect — C40 closed, carried since F2

```
claim  which plans state which tolerances, before and after
cmd    for each plan, count the declared tolerances it states a value for
out    F2.md: states 49 of 49 declared        F3.md: states 0    (before)
out    F2.md: states 49                      F3.md: states 2     (after)
rule   a tolerance is fixed by SOME locked plan, not by F2 specifically
judge  `test_plan_matches_tolerances.py` read `docs/milestones/F2.md` hardcoded,
       so EG0's two constants would have had to be written into a CLOSED
       milestone's table to satisfy `test_every_declared_tolerance_appears_in_
       the_plan`. It reads every locked plan now and names the one it read in its
       failure message. That is C40, ledgered since F2 on the reading that this
       guard did not fail false -- true until a later milestone declared a
       tolerance, which is the one event it was ledgered for.
```

## 5. EG1, R630 — and the figures were mine, not the plan's

```
claim  the three detection edges, and the rule each set belongs to
out    WITHDRAWN: 2.735459e-14 / 1.057143e-15 / 6.837686e-13 are the BEST
out    member's edges. A size just above the first reddens ONE member, not the
out    worst, which needs 1.93x more.
out    the worst over the sixteen, against the RETIRED 1e-15 ceiling:
out    5.285599e-14 / 1.094071e-15 / 2.642868e-12
out    the worst over the sixteen, against the ceiling that now SHIPS:
out    6.266629e-17 / 1.262927e-18 / 3.088842e-15
rule   BP0: when a decision rule changes, every figure citing the old rule is
       regenerated or withdrawn in the same commit
judge  TWO CORRECTIONS, both mine. The second set is what `docs/milestones/F3.md`
       section 5 states -- right to the digit -- and I reported the plan as wrong
       when my own figures were. And both older sets were measured against a
       ceiling this step RETIRES, so the third set is the one that describes the
       code; all three are kept, each labelled with its rule, which is what BP0
       asks instead of a silent replacement. The third set is printed per run by
       `test_EG0_the_THREE_COUNTERS_redden_every_member`, so no figure here needs
       re-taking by hand.
```

## 6. EG3, and one figure I pasted without re-reading

The carve-out is in `CLAUDE.md` and `docs/SUPERVISOR.md` in the reviewer's wording,
with EG3's two conditions and EG4(e)'s corpus pause.

```
claim  the clause is byte-identical in both files
cmd    slice the block out of each file and compare
out    identical: True   length 1237
rule   EG3: the reviewer's verdict-83 wording, unparaphrased
judge  I FIRST WROTE `1281` INTO THAT COMMIT MESSAGE, from the run before the
       final edit, and caught it on re-reading the output rather than the message.
       The commit was unpushed and I corrected it in place rather than leave a
       false figure in history -- which is the one case where amending is the
       repair and not a convenience. It is CP2's shape in the commit that adopts
       a rule about pasted output, which is worth recording rather than fixing
       quietly.
```

## 7. F3's close, and EG5(b)

```
rule   the dates this milestone is measured against (EG5(c), unchanged)
out    F3                       13 October   -- closing with this step
out    F4                       19 October   -- EG5(b): propose 16 October
out    the member-force table   23 October
out    the code-check screen    28 October, or 26 October if the preview runs clean
judge  **F3 CLOSES BY 9 OCTOBER: YES**, so EG5(b) applies and I propose pulling F4
       to 16 October. What it rests on: F4's first item is an additive HSP writer
       for `res.lam` plus the per-body external force and the equilibrium
       reaction, and DX1 already measured that those reactions exist in the solve
       and are discarded -- so the work is an export, not a derivation. What it
       does NOT rest on is the preview in EG4, which is unverified by
       construction and cannot be evidence for a date.
judge  AND THE RISK I WOULD NOT HIDE BEHIND THE YES: F4 adds the EB6
       label-provenance gate, whose expected side has to come from HSP-stable
       read-only. I have not yet read that file, so the one unknown in pulling F4
       forward is whether the buoy positions are there in a form a gate can cite
       by file and line. If they are not, 16 October is the wrong date and 19 is
       the right one.
```

## 8. Findings answered

Generated: `python scripts/answered_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R610 | carried | **carried** | §9 | `` | carried from an earlier verdict |
| R611 | carried | **withdrawn** | §9 | `` | carried from an earlier verdict |
| R612 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R613 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R614 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R615 | carried | **carried** | §9 | `` | carried from an earlier verdict |
| R616 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R617 | carried | **withdrawn** | §9 | `` | carried from an earlier verdict |
| R618 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R619 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R620 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R621 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R622 | carried | **later** | §9 | `` | carried from an earlier verdict |
| R623 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R624 | recorded | **answered** | §2 | `` | THE CEILING THE NEW GATE AND THE NEW REFUSAL ASSERT AGAINST IS INHERITED FROM A DIFFERENT QUANTI |
| R625 | recorded | **answered** | §9 | `` | THE SHIPPED REFUSAL ACCEPTS AN INDEFINITE ELEMENT STIFFNESS. THREE SIGN ERRORS, EACH INJECTED AL |
| R626 | recorded | **carried** | §10 | `` | THE REFUSAL IS A GATE HALF AND NOTHING COMMITTED SHOWS IT EVER REFUSES. ITS SIBLING IN THE SAME  |
| R627 | recorded | **answered** | §9 | `` | A THIRD READING OF `RIGID_MODE_BOUND` SHIPS IN TWO ASSERTIONS AND ITS OWN ENTRY STILL SAYS TWO - |
| R628 | recorded | **answered** | §9 | `` | THE REPORT IN THE TREE ANSWERS VERDICT 80. THIS ROUND HAD NO REPORT, AND ITS FIGURES LIVED IN AN |
| R629 | recorded | **answered** | §1 | `` | ONE TEST IS RED AT THE JUDGED COMMIT ON BOTH MACHINES, IT IS NOT THE STEP-BOUNDARY CLASS, AND WH |
| R630 | recorded | **answered** | §5 | `` | THE THREE DETECTION EDGES PUBLISHED IN THE SOURCE TREE AS "THE DETECTION EDGES" ARE THE BEST OF  |
| R631 | recorded | **carried** | §10 | `` | THE `RIGID_MODE_BOUND` ENTRY'S NEW MARGIN IS PUBLISHED WITH AN OPERATING POINT THAT DOES NOT PRO |

## 8a. Sites named by findings and not touched

Generated: `python scripts/untouched_sites.py`.

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R624 | `F2.md` | the file is untouched | **no change.** A closed milestone's plan, and EG0 is precisely about not writing an F3 tolerance into it. |
| R624 | `floatfea/model/platform.py:311` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:312` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:313` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:314` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:315` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:316` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:317` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:318` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/model/platform.py:319` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R624 | `floatfea/tolerances.py:316` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:317` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:318` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:319` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:320` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:321` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:322` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:323` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:324` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:325` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:326` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:327` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `floatfea/tolerances.py:328` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R624 | `scripts/write_verdict.py` | the file is untouched | **no change in step 2.** C72 was answered at `6246fbd` under EB2. |
| R624 | `tolerances.py:347` | the file is touched and this line number is the old one | **no change** -- the bare-name form of `floatfea/tolerances.py`. |
| R624 | `tolerances.py:348` | the file is touched and this line number is the old one | **no change** -- the bare-name form of `floatfea/tolerances.py`. |
| R624 | `tolerances.py:349` | the file is touched and this line number is the old one | **no change** -- the bare-name form of `floatfea/tolerances.py`. |
| R624 | `tolerances.py:350` | the file is touched and this line number is the old one | **no change** -- the bare-name form of `floatfea/tolerances.py`. |
| R624 | `tolerances.py:351` | the file is touched and this line number is the old one | **no change** -- the bare-name form of `floatfea/tolerances.py`. |
| R624 | `tolerances.py:352` | the file is touched and this line number is the old one | **no change** -- the bare-name form of `floatfea/tolerances.py`. |
| R625 | `floatfea/element/rigid.py:106` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:107` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:108` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:109` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:110` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:111` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:112` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:113` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:114` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:115` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:116` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:117` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:118` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `floatfea/element/rigid.py:119` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R625 | `io/reader.py:314` | the file is untouched | **no change.** Cited as the one place in `floatfea/` that already tested an eigenvalue sign; the contrast R625 was framed against. |
| R625 | `rigid.py:100` | the file is untouched | **no change** -- the bare-name form of `floatfea/element/rigid.py`. |
| R625 | `rigid.py:101` | the file is untouched | **no change** -- the bare-name form of `floatfea/element/rigid.py`. |
| R625 | `rigid.py:102` | the file is untouched | **no change** -- the bare-name form of `floatfea/element/rigid.py`. |
| R625 | `rigid.py:103` | the file is untouched | **no change** -- the bare-name form of `floatfea/element/rigid.py`. |
| R625 | `test_consistent_mass.py:497` | the file is untouched | **no change.** Cited as a site that clips a spectrum at zero, the class R625 belongs to. Rung 2 is not in this step's scope. |
| R626 | `scripts/rigid_counter_response.py` | the file is untouched | **no change.** The script this step's injection sites come from; it measures and does not assert. |
| R626 | `test_platform_skeleton.py:696` | the file is untouched | **no change** -- the bare-name form. See the `tests/` row. |
| R626 | `test_platform_skeleton.py:698` | the file is untouched | **no change** -- the bare-name form. See the `tests/` row. |
| R626 | `test_platform_skeleton.py:705` | the file is untouched | **no change** -- the bare-name form. See the `tests/` row. |
| R626 | `test_platform_skeleton.py:707` | the file is untouched | **no change** -- the bare-name form. See the `tests/` row. |
| R626 | `tests/verification/rung3/test_platform_rigid_modes.py:26` | the file is touched and this line number is the old one | TOUCHED at `47daa3d` -- the new ceiling, the 16/16 assertions and the window check -- and **no change at that exact line**. |
| R626 | `tests/verification/rung3/test_platform_rigid_modes.py:131` | the file is touched and this line number is the old one | TOUCHED at `47daa3d` -- the new ceiling, the 16/16 assertions and the window check -- and **no change at that exact line**. |
| R626 | `tests/verification/rung3/test_platform_rigid_modes.py:224` | the file is touched and this line number is the old one | TOUCHED at `47daa3d` -- the new ceiling, the 16/16 assertions and the window check -- and **no change at that exact line**. |
| R627 | `floatfea/element/rigid.py:135` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R627 | `floatfea/element/rigid.py:136` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R627 | `floatfea/element/rigid.py:137` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R627 | `floatfea/element/rigid.py:138` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R627 | `floatfea/element/rigid.py:139` | the file is untouched | TOUCHED at `c4d4817` and `8ed0fd4`; **no change at that exact line**. |
| R627 | `floatfea/model/platform.py:328` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R627 | `floatfea/model/platform.py:344` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R627 | `floatfea/tolerances.py:389` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:390` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:391` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:392` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:393` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:394` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:395` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:396` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:397` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:398` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:399` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:400` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:401` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:402` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:403` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:404` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `floatfea/tolerances.py:405` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R627 | `rigid.py` | the file is untouched | **no change** -- the bare-name form of `floatfea/element/rigid.py`. |
| R628 | `docs/reports/F3/step-2.md:3` | the file is touched and this line number is the old one | TOUCHED at this step for EG1: section 5's withdrawn figures, marked `WITHDRAWN` in place rather than replaced. **No change at that exact line**; step 2 is closed and its report stays the record of what it claimed. |
| R629 | `tests/test_report_carried.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:539` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:540` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:541` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:542` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:543` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:544` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:545` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:546` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R629 | `tests/test_report_guard_states.py:547` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R630 | `scripts/rigid_counter_response.py` | the file is untouched | **no change.** The script this step's injection sites come from; it measures and does not assert. |

## 8b. Carried

Generated: `python scripts/carried_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R610 | **carried** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R611 | **withdrawn** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R612 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R613 | **answered** — §9 | ANSWERED at 3709cc6, and the STOP IS LIFTED. Verified line by line rather than taken from the... |
| R614 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R615 | **carried** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R616 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R617 | **withdrawn** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R618 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R619 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R620 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R621 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R622 | **later** — §9 | LATER, and correctly so. It was written as F4's to answer and the report routes it there.... |
| R623 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R624 | **answered** — §2 | THE CEILING THE NEW GATE AND THE NEW REFUSAL ASSERT AGAINST IS INHERITED FROM A DIFFERENT... |
| R625 | **answered** — §9 | THE SHIPPED REFUSAL ACCEPTS AN INDEFINITE ELEMENT STIFFNESS. THREE SIGN ERRORS, EACH INJECTED... |
| R626 | **carried** — §10 | THE REFUSAL IS A GATE HALF AND NOTHING COMMITTED SHOWS IT EVER REFUSES. ITS SIBLING IN THE SAME... |
| R627 | **answered** — §9 | A THIRD READING OF RIGID_MODE_BOUND SHIPS IN TWO ASSERTIONS AND ITS OWN ENTRY STILL SAYS TWO --... |
| R628 | **answered** — §9 | THE REPORT IN THE TREE ANSWERS VERDICT 80. THIS ROUND HAD NO REPORT, AND ITS FIGURES LIVED IN... |
| R629 | **answered** — §1 | ONE TEST IS RED AT THE JUDGED COMMIT ON BOTH MACHINES, IT IS NOT THE STEP-BOUNDARY CLASS, AND... |
| R630 | **answered** — §5 | THE THREE DETECTION EDGES PUBLISHED IN THE SOURCE TREE AS "THE DETECTION EDGES" ARE THE BEST OF... |
| R631 | **carried** — §10 | THE RIGID_MODE_BOUND ENTRY'S NEW MARGIN IS PUBLISHED WITH AN OPERATING POINT THAT DOES NOT... |

## 9. Where each carried item stands

Every row of §8b points at the section that does its work.

* **R610** — carried as step 2's report §9 records it, unchanged by this step.
* **R611** — carried as step 2's report §9 records it, unchanged by this step.
* **R612** — carried as step 2's report §9 records it, unchanged by this step.
* **R613** — carried as step 2's report §9 records it, unchanged by this step.
* **R614** — carried as step 2's report §9 records it, unchanged by this step.
* **R615** — carried as step 2's report §9 records it, unchanged by this step.
* **R616** — carried as step 2's report §9 records it, unchanged by this step.
* **R617** — carried as step 2's report §9 records it, unchanged by this step.
* **R618** — carried as step 2's report §9 records it, unchanged by this step.
* **R619** — carried as step 2's report §9 records it, unchanged by this step.
* **R620** — carried as step 2's report §9 records it, unchanged by this step.
* **R621** — carried as step 2's report §9 records it, unchanged by this step.
* **R622** — carried as step 2's report §9 records it, unchanged by this step.
* **R623** — carried as step 2's report §9 records it, unchanged by this step.
* **R624** — answered at `47daa3d` — the gate has its own ceiling, derived from the window the sixteen members leave. §2.
* **R625** — answered at `c4d4817` — the signed PSD clause. Recorded in `docs/closure/F3.md` §2 as the milestone's one real defect.
* **R626** — **carried, ledgered.** Its headline is answered; the residual and signed clauses have no solved boundary. `docs/closure/F3.md` §4. §10.
* **R627** — answered at `8ed0fd4` — the entry declares the third reading.
* **R628** — answered by revision 2 of step 2's report.
* **R629** — answered at `0d911ce` — the pointers discriminate, so the planted state can fail. §1.
* **R630** — answered at `47daa3d` (EG1), and **its own figures withdrawn under BP0**: they were measured against a ceiling this step retires. §5.
* **R631** — **carried, ledgered.** The figure is right and the operating point does not reproduce. `docs/closure/F3.md` §4. §10.

## 10. EG2 — and the one place I did not put it

R626's residue and R631 are ledgered in **`docs/closure/F3.md` § 4**, not in
`docs/milestones/F2a.md`.

```
claim  what F2a's own frozen list says about additions
cmd    read docs/milestones/F2a.md, section 7's opening
out    "This list is closed. CZ0 stops new apparatus through F6, so nothing is
out    added to 4a from here: an item found after this commit is recorded in a
out    verdict and in the milestone's closure artifact, and it does not enter
out    this plan."
rule   EG2: "Ledger both in F2a, quoting verdict 83's edges and grid values"
judge  THE DIRECTIVE AND THAT SENTENCE DISAGREE, and I followed the sentence,
       because the closure artifact is the home it names. Both items are there
       with the verdict's edges and grid values. Adding rows to a list whose
       first line says it is closed is the deviation I was not willing to make
       quietly: say so and I will move them.
```

## 11. Tolerances touched

**Two DECLARED, none widened, and the one that changed got five decades tighter.**

```
cmd    git diff 580b183..HEAD -- floatfea/tolerances.py, the value lines
out    + PLATFORM_RIGID_MODE_EXACTNESS: Final[float] = 1.154338e-18
out    + PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT: Final[float] = 1.0e-14
out    no existing value line changed
rule   a tolerance change requires a written justification naming the physical or
       numerical reason the previous value was incorrect
judge  G2.1's gate moved from `1e-15` to `1.154338e-18`, which is TIGHTER by five
       decades and is not a widening in any direction. The reason is in the
       entry: `1e-15` was measured on the retired per-row assembled form, its own
       entry pre-registered the re-derivation, and at that value two of the three
       counters could not cross it. The builder's `RIGID_MODE_EXACTNESS` is
       untouched.
```

## 12. The whole suite

**Whole suite at `7e86d2a`: 2664 passed, 0 failed, 0 skipped.** **The excluded set: 270 passed, 20 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 290 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_answered_verdict_is_the_NEWEST_one`
- **failed, in the excluded set** `tests.test_report_carried::test_the_plan_names_the_step_under_execution`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[two_reports_ahead_of_the_newest_verdict]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_file_is_a_directory]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[two_digit_step_number_discriminating]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_a_report_commit_messaged_docs_that_also_edits_the_guards_measuring_it]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]`
```

**EG3(i) — THE TRACE, because the waiver is conditional on it.** Every red is
matched by name to the state's own list; a red that does not match is CZ1 (iv)
unchanged, and none is unmatched.

```
cmd    python -m pytest tests/test_report_carried.py
         tests/test_report_numbers_are_sourced.py -q, in place at this commit
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  -> UNMATCHED: CZ1 (iv) unchanged
out    test_the_guard_reads_the_step_being_worked_on  -> state (1), cleared by the verdict
out    test_the_report_carries_a_WHOLE_SUITE_count  -> this line, which did not exist when the count ran
rule   CZ1's carve-out, state (1): report written, verdict not yet. The only
       failures are `test_the_guard_reads_the_step_being_worked_on` and the
       planted states that cascade off its baseline.
judge  THE EXCLUDED SET'S 20 ARE THAT CASCADE, and the lesson of R629 is that
       "cascade" is a claim and not a category: eight planted states were ruled as
       one by class across two verdicts and the eighth was a real defect. So the
       count above is matched name by name rather than by family, and the harness
       is run in full -- `tests/test_report_guard_states.py` cannot be run in
       place, which is exactly where R629 hid.
```

**EG3(i) ON CI, AND IT FOUND TWO GAPS IN THE CLAUSE'S OWN LIST.** The condition is
that every red traces *by name* to the state's list, so a red that is obviously the
same cause but is not on the list is a gap in the list rather than a pass.

```
cmd    the FAILED ids of run 36898482589 at 47daa3d, conclusion failure
out    tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one
out    tests/test_report_guard_states.py::test_the_guard_survives_the_state[...]
cmd    the same trace against the carve-out's state (2) list
out    test_every_named_site_is_touched_or_declared          not seen
out    test_the_report_carries_the_finding                   not seen
out    test_the_CI_section_is_about_the_REVIEWED_commit      not seen
out    test_the_Carried_table_is_what_the_generator_produces not seen
out    test_the_generator_would_catch_a_row_under_the_wrong_number  not seen
out    test_the_answered_verdict_is_the_NEWEST_one           UNLISTED
out    the_guard_survives_the_state cascade                  UNLISTED
rule   EG3(i): the waiver applies only if EVERY red traces BY NAME to the
       step-boundary cause
judge  BOTH ARE STATE (2) BY THEIR OWN MESSAGES -- the report answered verdict 82
       while 83 existed, and the harness plants into a tree whose baseline is that
       failure -- and NEITHER IS ON THE CLAUSE'S LIST. The list was written from
       one observation of the state; these two are the same cause under different
       names. I am not editing the clause: it is the reviewer's wording adopted by
       directive EG3, and widening a waiver's own list is the last thing an
       implementer should do unilaterally. **Flagged for a directive**, and until
       then this red is recorded as unlisted rather than waived.
judge  THIS IS WHAT EG3(i) IS FOR, on its first use. The condition caught a stale
       CI table in the local run as well -- `test_the_CI_TABLE_agrees_with_gh_FOR_
       EVERY_ROW`, a run that had completed between generating section 0 and
       running the guards -- which a "the failures look like the boundary set"
       reading would have waved through.
```

**And EG3(ii) is owed at the next revision**, not here: the report-guard files are
measured AT the verdict commit once it exists, and those counts go into the
revision that answers it.

