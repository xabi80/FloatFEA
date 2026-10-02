# F3 step 3 — R624 answered, the ceiling derived, and F3 closed

Answers: verdict 83 @ 580b183

**2026-10-01.**

# Revision 1 — EG0 through EG5, and F3's closure

*The heading above is what `tests/test_report_guard_states.py` anchors on (R632). This report had none, so the harness raised `ValueError: substring not found` and could not PLANT its state at all -- a worse shape than R629, where it planted and could not discriminate.*

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
| R610 | **carried** — §9b | no clause this generator can cut -- see the verdict's Carried section |
| R611 | **withdrawn** — §9c | no clause this generator can cut -- see the verdict's Carried section |
| R612 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R613 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R614 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R615 | **carried** — §9b | no clause this generator can cut -- see the verdict's Carried section |
| R616 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R617 | **withdrawn** — §9c | no clause this generator can cut -- see the verdict's Carried section |
| R618 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R621 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R622 | **later** — §9c | no clause this generator can cut -- see the verdict's Carried section |
| R623 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R624 | **answered** — §2 | ANSWERED at 47daa3d, and I re-derived it rather than accepting it. The |
| R625 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R626 | **carried** — §9b | 's residue -- OPEN, LEDGERED to the same place, same ruling. The two |
| R627 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R628 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R629 | **answered** — §1 | NOT CLOSED. IT CHANGED SHAPE AND IT IS RED ON BOTH MACHINES. R632. The |
| R630 | **answered** — §5 | ANSWERED at 47daa3d, verified line by line, and answered better than I |
| R631 | **carried** — §9b | OPEN, LEDGERED to docs/closure/F3.md section 4, and I ACCEPT the ledger |
| R632 | **open** — blocking, and not answered in this round | ONE OF THE NINE REDS IS NOT THE STEP-BOUNDARY CLASS. THE PLANT ACTION CANNOT BUILD ITS STATE... |
| R633 | **open** — blocking, and not answered in this round | THE NEW ENTRY'S FIRST SENTENCE SAYS ITS THREE COUNTERS ARE REGISTERED IN... |
| R634 | **open** — blocking, and not answered in this round | floatfea/tolerances.py SAYS NOTHING ASSERTS RIGID_MODE_EXACTNESS AND THAT IT BOUNDS NOTHING,... |
| R635 | **open** — blocking, and not answered in this round | THE WINDOW IS GUARDED ASYMMETRICALLY, AND EG0(c)'s 2x CLAUSE FIRES ON ROUTINE LEGAL CHANGES... |
| R636 | **open** — recordable at 4a in the verdict's own classification | What the new ceiling BUYS. The report justifies the change by what the old ceiling could not... |

## 9. Where each carried item stands

**Three subsections, because one was not enough (R632).** `step-3-answers.json` put
14 of 22 rows back at `§9` one commit after R629 was fixed for exactly that --
`§9` named every item, so the planted state and the shipped report were the same
document again. An item now points at the subsection that describes its
DISPOSITION, and the three dispositions are different claims.

### 9a. Answered in an earlier step of F3

* **R612** — carried as step 2's report §9 records it, unchanged by this step.
* **R613** — carried as step 2's report §9 records it, unchanged by this step.
* **R614** — carried as step 2's report §9 records it, unchanged by this step.
* **R616** — carried as step 2's report §9 records it, unchanged by this step.
* **R618** — carried as step 2's report §9 records it, unchanged by this step.
* **R619** — carried as step 2's report §9 records it, unchanged by this step.
* **R620** — carried as step 2's report §9 records it, unchanged by this step.
* **R621** — carried as step 2's report §9 records it, unchanged by this step.
* **R623** — carried as step 2's report §9 records it, unchanged by this step.
* **R624** — answered at `47daa3d` — the gate has its own ceiling, derived from the window the sixteen members leave. §2.
* **R625** — answered at `c4d4817` — the signed PSD clause. Recorded in `docs/closure/F3.md` §2 as the milestone's one real defect.
* **R627** — answered at `8ed0fd4` — the entry declares the third reading.
* **R628** — answered by revision 2 of step 2's report.
* **R629** — answered at `0d911ce` — the pointers discriminate, so the planted state can fail. §1.
* **R630** — answered at `47daa3d` (EG1), and **its own figures withdrawn under BP0**: they were measured against a ceiling this step retires. §5.

### 9b. Ledgered, and carried as a measurement rather than a defect

These are in `docs/closure/F3.md` §4 under DZ7c, and they are margin
characterisation rather than correctness.

* **R610** — carried as step 2's report §9 records it, unchanged by this step.
* **R615** — carried as step 2's report §9 records it, unchanged by this step.
* **R626** — **carried, ledgered.** Its headline is answered; the residual and signed clauses have no solved boundary. `docs/closure/F3.md` §4. §10.
* **R631** — **carried, ledgered.** The figure is right and the operating point does not reproduce. `docs/closure/F3.md` §4. §10.

### 9c. Withdrawn or routed to a later milestone

* **R611** — carried as step 2's report §9 records it, unchanged by this step.
* **R617** — carried as step 2's report §9 records it, unchanged by this step.
* **R622** — carried as step 2's report §9 records it, unchanged by this step.

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

**Two DECLARED, none widened, and the one that changed got `866.3x` tighter, which is `2.94` decades.**

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

# Revision 2 — verdict 84's three items, and four figures of mine

Answers: verdict 84 @ 8368c51

**2026-10-01.**

## 0. CI at `a647492`, the commit verdict 84 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 84 at `a647492` through the report's own `Answers:` line. Run `36900722535`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1044 | 9 | 0 |
| the verification ladder | 1844 | 0 | 0 |
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

## 0a. Runs since the commit verdict 84 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 84 at `a647492` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `36900722535` | push | `a647492` | conclusion **failure** |

**Run `36900722535`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

## 1. R632 — the state could not plant, and the pointers were one section again

```
claim  the harness could not build its state at all
cmd    read tests/test_report_guard_states.py:545
out    head = text.rindex("# Revision ")
out    revision 1 of this report carried NO such heading, so the state raised
out    ValueError: substring not found before planting anything
cmd    python -m pytest "...[guard_state_every_Carried_pointer_names_the_Carried_
         SECTION_ITSELF]" -q, after
out    1 passed
rule   a planted defect that cannot be planted measures nothing
judge  WORSE THAN R629, WHICH I HAD JUST FIXED. There it planted and could not
       discriminate; here it could not plant. And `step-3-answers.json` put 14 of
       22 pointers back at one section ONE COMMIT after R629 -- the same defect,
       in the file written to answer it. Section 9 is split 9a answered / 9b
       ledgered / 9c withdrawn, so a pointer names a DISPOSITION, and the three
       dispositions are different claims rather than one list containing
       everything.
```

## 2. R633 — the counter was asserting itself

```
claim  the registry rows did not exist, and the counter did not depend on the gate
cmd    the reviewer built the row and ran both BX0 cells
out    dropped_flip      gate cell False   ceiling cell True
out    wrong_dof_index   gate cell False   ceiling cell True
out    rotational_block  gate cell False   ceiling cell True
cmd    python -m pytest tests/test_counters_are_injected.py
         tests/verification/rung3/test_platform_rigid_modes.py -q, after
out    37 passed
rule   BX0 cell one: the counter must FAIL with the gate replaced by a no-op
judge  MY COUNTER COMPARED THE RESPONSE WITH THE CEILING INLINE, so neutering the
       gate left it passing. That is R163 and R173 -- a counter asserting itself --
       inside the counter written to defend a gate against exactly that. The three
       bodies call the gate through the module global now. The ceiling cell was
       always true, so the substance was sound and the mechanism was not.
judge  AND THE REGISTRY'S BOUND WAS `>= 4` WITH FOUR ROWS, so a fifth constant
       with a callable gate was invisible to the meta-test. `>= 7` now.
```

## 3. R634 — two sentences, seventy-three lines above my own refusal

```
claim  what the entry said, and what the code does
out    tolerances.py: "AND NOTHING ASSERTS THIS CONSTANT ANY MORE"
out    tolerances.py: "it bounds nothing"
out    platform.py:   check_rigid_modes refuses the production build on it
rule   CW0: prose in the source tree does not claim things about the code
judge  F3 step 2's own commit added the refusal and left both sentences standing,
       seventy-three lines apart in one file. What no longer asserts on it is the
       GATE, which took its own ceiling in step 3; the CLASS line saying ACCURACY
       is right again. `docs/closure/F3.md` section 3 sent a reader to that entry
       under a column headed "the refusal", which is how the reviewer found it.
```

## 4. Four figures of mine, and the mechanism behind all four

```
claim  C101: "`866.3x` tighter, which is `2.94` decades" is wrong
cmd    1e-15 / 1.154338e-18
out    866.3x = 2.94 decades
judge  no reading gives five. It is in docs/closure/F3.md section 7 and in my
       own hand-back. Corrected in both.

claim  C103: "the six design-wave cases have never been run" is wrong
cmd    ls ../HSP-runs/studies/platform-12buoy/floatfea_design_waves/
out    case_T10s, T12.5s, T14s, T15s, T16.2s, T20s -- six CSVs, DJ2(b)'s periods
cmd    the column names of one of them
out    t_s, platform_heave_m, platform_heave_acc_mps2, and surge/sway/heave + acc
out    for buoy1, buoy4 and buoy7 only -- 21 columns, no reaction, no force
judge  I LOOKED ONE DIRECTORY TOO HIGH, at ../HSP-runs/studies/, and concluded
       from its absence that the runner had never run. EG4 IS STILL BLOCKED and
       now for one reason instead of two: the export carries no reactions, which
       is DX1's finding and which I verified myself above. The false ground is
       withdrawn before the escalation reaches Xabier, which is what C103 asked.

claim  C104: a647492's message says `all 5 findings carried`
cmd    python scripts/check_carried.py --verdict <step 3's verdict> --report <this>
out    check_carried: all 8 findings carried
judge  drafted from step 2's figure and not re-read. The commit is pushed, so this
       triple is the repair.

judge  FOUR SLIPS IN ONE SESSION -- "93000x", "1281", "all 5", "five decades" --
       and one mechanism: I draft the triple from the run I remember rather than
       the run that just finished. The reviewer's proposed CP3 names the fix as an
       ORDERING -- the paste is the last edit, and an edit after it voids the
       paste. It is with Xabier; I am not adopting a rule about my own discipline
       on my own authority.
```

## 5. Ledgered, and one that needs a directive

**R635 is not a round's work and I am not treating it as one.** The window is
guarded asymmetrically, and EG0(c)'s own stop clause lands inside its own band at
legal sections:

```
out    the floor is guarded at   2x      the roof at   1x
out    t = 170 mm    1.15x       inside the STOP band
out    t = 185 mm    1.29x       inside the STOP band
out    E = 200 GPa   1.48x       inside the STOP band
rule   EG0(c): if either machine's clean worst comes within 2x of the ceiling,
       STOP and report; do not move it
judge  all three are legal sections and F1's order check brackets that thickness
       range, so the condition fires on a platform nobody has done anything wrong
       to. EG0(c) says do not move the ceiling; the entry says it is re-derived
       rather than re-justified. THOSE TWO DISAGREE and which governs is Xabier's.
       The figures are the reviewer's, taken in verdict 84.
``` R626's residue and R631 stay ledgered in
`docs/closure/F3.md` § 4 under DZ7c.

## 6. EG3(ii), which this revision owes

```
claim  the report-guard files AT the verdict commit, which no verdict had measured
cmd    a clean worktree at 8368c51, then pytest tests/test_report_carried.py
         tests/test_report_numbers_are_sourced.py -q
out    26 failed, 190 passed
rule   EG3(ii): after the verdict commit, measure the report-guard files at that
       commit and paste the counts in the next revision
judge  this is state (2) -- verdict written, answering report not yet -- and it is
       the half CZ1's carve-out could not see, because the reviewer runs at the
       judged commit BEFORE writing. This revision is what clears it.
```

## 7. Findings answered

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R610 | carried | **carried** | §5 | `` | carried from an earlier verdict |
| R611 | carried | **withdrawn** | §10c | `` | carried from an earlier verdict |
| R612 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R613 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R614 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R615 | carried | **carried** | §5 | `` | carried from an earlier verdict |
| R616 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R617 | carried | **withdrawn** | §10c | `` | carried from an earlier verdict |
| R618 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R621 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R622 | carried | **later** | §10c | `` | carried from an earlier verdict |
| R623 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R624 | carried | **answered** | §4 | `` | carried from an earlier verdict |
| R625 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R626 | carried | **carried** | §5 | `` | carried from an earlier verdict |
| R627 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R628 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R629 | carried | **answered** | §10a | `` | carried from an earlier verdict |
| R630 | carried | **answered** | §4 | `` | carried from an earlier verdict |
| R631 | carried | **carried** | §5 | `` | carried from an earlier verdict |
| R632 | recorded | **answered** | §1 | `` | ONE OF THE NINE REDS IS NOT THE STEP-BOUNDARY CLASS. THE PLANT |
| R633 | recorded | **answered** | §2 | `` | THE NEW ENTRY'S FIRST SENTENCE SAYS ITS THREE COUNTERS ARE |
| R634 | recorded | **answered** | §3 | `` | `floatfea/tolerances.py` SAYS NOTHING ASSERTS |
| R635 | recorded | **carried** | §5 | `` | THE WINDOW |
| R636 | recorded | **answered** | §10a | `` | What the new ceiling BUYS. The report justifies the change by what |

## 8. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R632 | `docs/reports/F3/step-2.md` | the file is untouched | TOUCHED at this step for EG1: section 5's withdrawn figures, marked `WITHDRAWN` in place rather than replaced. **No change at that exact line**; step 2 is closed and its report stays the record of what it claimed. |
| R632 | `tests/test_report_guard_states.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:539` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:540` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:541` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:542` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:543` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:544` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:545` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:546` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R632 | `tests/test_report_guard_states.py:777` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R633 | `docs/milestones/F3.md` | the file is untouched | TOUCHED at `47daa3d` -- section 7, F3's own tolerance table -- and at this step for the step marker. **No change at that exact line**; section 5 was re-locked at `3709cc6` and EG1 confirms its figures were right. |
| R633 | `floatfea/tolerances.py:354` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R633 | `floatfea/tolerances.py:355` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |
| R633 | `tests/test_counters_are_injected.py:317` | the file is touched and this line number is the old one | TOUCHED at `95f6293` for R633: three registry rows against `PLATFORM_RIGID_MODE_EXACTNESS` and the bound raised to seven. **No change at that exact line.** |
| R633 | `tests/test_counters_are_injected.py:318` | the file is touched and this line number is the old one | TOUCHED at `95f6293` for R633: three registry rows against `PLATFORM_RIGID_MODE_EXACTNESS` and the bound raised to seven. **No change at that exact line.** |
| R633 | `tests/test_counters_are_injected.py:319` | the file is touched and this line number is the old one | TOUCHED at `95f6293` for R633: three registry rows against `PLATFORM_RIGID_MODE_EXACTNESS` and the bound raised to seven. **No change at that exact line.** |
| R634 | `docs/closure/F3.md` | the file is untouched | TOUCHED at `a647492`, `31cd0db` and `3fdfc79` -- section 4a's R638 record, EH3's backlog ruling, and C101 -- and **no change at that exact line**. |
| R634 | `floatfea/model/platform.py:319` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R634 | `floatfea/model/platform.py:320` | the file is untouched | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R634 | `floatfea/tolerances.py:403` | the file is touched and this line number is the old one | TOUCHED at `8ed0fd4` and `47daa3d` -- the third reading, and two DECLARATIONS, no value widened -- and **no change at that exact line**. |

## 9. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R610 | **carried** — §10b | no clause this generator can cut -- see the verdict's Carried section |
| R611 | **withdrawn** — §10c | no clause this generator can cut -- see the verdict's Carried section |
| R612 | **answered** — §10a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R613 | **answered** — §10a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R614 | **answered** — §10a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R615 | **carried** — §10b | no clause this generator can cut -- see the verdict's Carried section |
| R616 | **answered** — §10a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R617 | **withdrawn** — §10c | no clause this generator can cut -- see the verdict's Carried section |
| R618 | **answered** — §10a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R621 | **answered** — §10a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R622 | **later** — §10c | no clause this generator can cut -- see the verdict's Carried section |
| R623 | **answered** — §10a | no clause this generator can cut -- see the verdict's Carried section |
| R624 | **answered** — §4 | ANSWERED at 47daa3d, and I re-derived it rather than accepting it. The |
| R625 | **answered** — §10a | no clause this generator can cut -- see the verdict's Carried section |
| R626 | **carried** — §10b | 's residue -- OPEN, LEDGERED to the same place, same ruling. The two |
| R627 | **answered** — §10a | no clause this generator can cut -- see the verdict's Carried section |
| R628 | **answered** — §10a | no clause this generator can cut -- see the verdict's Carried section |
| R629 | **answered** — §10a | NOT CLOSED. IT CHANGED SHAPE AND IT IS RED ON BOTH MACHINES. R632. The |
| R630 | **answered** — §4 | ANSWERED at 47daa3d, verified line by line, and answered better than I |
| R631 | **carried** — §10b | OPEN, LEDGERED to docs/closure/F3.md section 4, and I ACCEPT the ledger |
| R632 | **answered** — §1 | ONE OF THE NINE REDS IS NOT THE STEP-BOUNDARY CLASS. THE PLANT ACTION CANNOT BUILD ITS STATE... |
| R633 | **answered** — §2 | THE NEW ENTRY'S FIRST SENTENCE SAYS ITS THREE COUNTERS ARE REGISTERED IN... |
| R634 | **answered** — §3 | floatfea/tolerances.py SAYS NOTHING ASSERTS RIGID_MODE_EXACTNESS AND THAT IT BOUNDS NOTHING,... |
| R635 | **carried** — §10b | THE WINDOW IS GUARDED ASYMMETRICALLY, AND EG0(c)'s 2x CLAUSE FIRES ON ROUTINE LEGAL CHANGES... |
| R636 | **answered** — §10a | What the new ceiling BUYS. The report justifies the change by what the old ceiling could not... |
| R637 | **open** — blocking, and not answered in this round | R632 IS UNCHANGED AT THE REVIEWED COMMIT, AND THE DRAFT THAT WOULD FIX IT MAKES THE STATE... |
| R638 | **open** — blocking, and not answered in this round | RIGID_MODE_EXACTNESS IS THE CEILING THE PRODUCTION BUILDER REFUSES REAL DECKS ON, AND IT CAN BE... |
| R639 | **open** — blocking, and not answered in this round | THE COUNTER INJECTION SIZE CAN BE RAISED EIGHT DECADES WITH THE WHOLE REGISTRY AND BOTH EG0... |
| R640 | **open** — recordable at 4a in the verdict's own classification | Three harness states commit into the parent repository when the suite runs inside a git... |

## 10a. Answered in an earlier step or round of F3

* **R612** — carried as an earlier report records it.
* **R613** — carried as an earlier report records it.
* **R614** — carried as an earlier report records it.
* **R616** — carried as an earlier report records it.
* **R618** — carried as an earlier report records it.
* **R621** — carried as an earlier report records it.
* **R623** — carried as an earlier report records it.
* **R624** — answered at `47daa3d`, verified independently by the reviewer. §4.
* **R625** — carried as an earlier report records it.
* **R627** — carried as an earlier report records it.
* **R628** — carried as an earlier report records it.
* **R629** — carried as an earlier report records it.
* **R630** — answered at `47daa3d`; three labelled sets, the shipped one printed per run.
* **R632** — answered in §1 — the report carries a `# Revision ` heading and §9 is split.
* **R633** — answered in §2 — the three counters are registered and the bodies call the gate.
* **R634** — answered in §3 — both sentences corrected.
* **R636** — carried as an earlier report records it.

## 10b. Ledgered, carried as a measurement rather than a defect

* **R610** — carried as an earlier report records it.
* **R615** — carried as an earlier report records it.
* **R626** — **ledgered.** `docs/closure/F3.md` §4 under DZ7c.
* **R631** — **ledgered.** The figure is right; the operating point does not reproduce.
* **R635** — **ledgered, and it needs a directive.** EG0(c) and the entry disagree. §5.

## 10c. Withdrawn or routed to a later milestone

* **R611** — carried as an earlier report records it.
* **R617** — carried as an earlier report records it.
* **R622** — carried as an earlier report records it.

## 11. The whole suite

SUITE_LINE_PLACEHOLDER

# Revision 3 — verdict 85 answered, and F3 closes

Answers: verdict 86 @ 3b5e36b

**2026-10-01.**

## 0. CI at `b7c05e7`, the commit verdict 86 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 86 at `b7c05e7` through the report's own `Answers:` line. Run `36964000628`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 966 | 17 | 1 |
| the verification ladder | 1848 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 17.**

- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R624->4]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R630->4]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:319]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 86 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 86 at `b7c05e7` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `36964000628` | push | `b7c05e7` | conclusion **failure** |
| `36969962460` | push | `aec96e0` | conclusion **failure** |
| `36997601588` | push | `c9902d3` | **no result** (status `in_progress`) |

**Run `36964000628`, conclusion **failure**: 17 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R624->4]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R630->4]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:319]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `36969962460`, conclusion **failure**: 8 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 1. The reading

**F3 closes with this step, on 1 October** — twelve days inside the 13 October date.
Round 3 of 3, so this verdict closes step 3 whatever it says. EH0 through EH4 are
landed; EH5's items are here; **EH6 is the critical path and is not started**, for
the reason in §8.

## 2. R637 — the state is VACUOUS, and three repairs did not fix it

```
cell   ONE VARIABLE: the plant action writing nothing, everything else held --
       the copy, the commit, the nested invocation, the assertion
out    WITH the plant, as shipped         1 passed
out    WITHOUT the plant (ablated)        1 passed
out    restored                           1 passed
rule   a planted defect whose presence changes nothing measures nothing
judge  IT WOULD READ `passed` WITH THE PLANT DELETED OUTRIGHT. Its only assertion
       is `code != 0`, and EG3's carve-out guarantees a red baseline at exactly the
       moment this state runs, so the vacuity is structural rather than occasional.
       This is R516's recorded failure mode.
```

**Two real defects found on the way, both fixed.** The plant rewrote every pointer
to a hardcoded `§9` while the state is named "names the Carried SECTION ITSELF" —
it now discovers the Carried section's own number the way the guard discovers it.
And **revision 2's headings were letters**, so `## I. Carried` had no numeric id and
the guard's own "do not point at Carried" half could not identify it: the third
instance of the R629/R632 family, and the one that explains the other two.

**The anchoring half is done at both sites.** `rindex("# Revision ")` matched my own
prose quoting it; both now use `^# Revision \d+`, which three other readers already
used.

```
claim  the anchored guard sees the whole revision, not 22 lines of 937
cmd    python -m pytest tests/test_report_numbers_are_sourced.py -q, after anchoring
out    1 failed -- an unsourced figure in the ledger section it had been blind to
rule   BF0's mechanical half reads the newest revision
judge  the repair found a real defect on its first run, which is the repair working.
```

**WHAT I DID NOT DO.** I added a `DIAGNOSIS` entry naming the pointer check as the
cause and removed it again: `_assert_diagnosis` is gated behind
`REQUIREMENT_CHANGED`, which this state is not in, so the entry was **inert** — and
an inert entry that looks like a guard is worse than none. Entering it in
`REQUIREMENT_CHANGED` is a declaration about what the *repaired guard* must do, and
the alternative the reviewer offered is deleting reviewer-authored apparatus under
DR1. Neither is mine to pick. **The ablation is the report and the choice is stated.**

## 3. R639 — the injection size can no longer rise

```
out    binding: rotational_block at 3.088842e-15; the declared size 1e-14 clears
       it by 3.24x
rule   the counter size is the SMALLEST defect the gate must fail
judge  a first version asserted per counter and failed on two of three: the edges
       span five decades, 1.262927e-18 to 3.088842e-15, so no single shared size
       sits within one multiple of all three. 3.24x is the locked plan's own figure,
       now produced by an assertion rather than a comment.
```

## 4. R638 — recorded and ledgered per EH3, and my figure is starker

```
cmd    RIGID_MODE_EXACTNESS 1e-15 -> 1e-13, over tests/verification and tests/unit
out    1802 passed, 0 failed -- nothing in the measuring half of the suite objects
cmd    the boundary, solved
out    every ceiling below 3.783782e-12 is accepted: 3784x of silent headroom
rule   a tolerance is guarded by a counter-case that reddens when it is widened
judge  the gate's own ceiling reddens at 8.7x, so the two are guarded three orders
       apart and the weaker one is on the PRODUCTION path. EH3 rules this recorded
       and ledgered; EJ1 then revised EH3: it is WORKED IN F4 and closed before
       F4 closes (C121 settled), and it does not block F4's opening. The entry and `docs/closure/F3.md` section 4a carry it.
```

## 5. EH2, and one place I wrote text ahead of code

```
out    window (3.528257e-19, 3.776640e-18) width 10.70x; the ceiling sits 3.27x
       above the floor and 3.27x below the roof
rule   EH2(c): guard both edges at 2x
judge  I WROTE "BOTH EDGES GUARDED AT 2x" AND HAD SHIPPED ONLY THE FLOOR. That
       would have been a false claim about the code in the same commit that made
       the claim, which is CW0. The roof assertion is in `3fdfc79` with the text.
       R635's asymmetry was 2x on the floor and 1x on the roof, which let EG0(c)'s
       own clause fire at legal sections.
```

EH2(a) and (b) are stated in the entry and in F3 § 5: the ceiling never moves on
fixed inputs, and a change of input is a re-derivation by the same rule in a
`plan:` commit recording both windows, without which the STOP stands.

## 6. The two figures I owed, as triples

```
claim  C101: "five decades tighter" was wrong
cmd    1e-15 / 1.154338e-18
out    866.3x = 2.94 decades
judge  corrected in `docs/closure/F3.md` and in this report. It was NOT corrected
       when revision 2 said it was, which is the same defect one level out.

claim  C104: a647492's message says `all 5 findings carried`
cmd    python scripts/check_carried.py --verdict <step 3's verdict> --report <this>
out    the run at that commit said `all 8`
judge  drafted from step 2's figure. The commit is pushed, so this triple is the
       repair. CP3 is now adopted for exactly this: the paste is the last edit.
```

## 7. Findings answered

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R610 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R611 | carried | **withdrawn** | §9c | `` | carried from an earlier verdict |
| R612 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R613 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R614 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R615 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R616 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R617 | carried | **withdrawn** | §9c | `` | carried from an earlier verdict |
| R618 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R621 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R622 | carried | **later** | §9c | `` | carried from an earlier verdict |
| R623 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R624 | carried | **answered** | §5 | `` | carried from an earlier verdict |
| R625 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R626 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R627 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R628 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R629 | carried | **answered** | §9a | `` | carried from an earlier verdict |
| R630 | carried | **answered** | §5 | `` | carried from an earlier verdict |
| R631 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R632 | recorded | **answered** | §9a | `` | ONE OF THE NINE REDS IS NOT THE STEP-BOUNDARY CLASS. THE PLANT |
| R633 | recorded | **answered** | §9a | `` | THE NEW ENTRY'S FIRST SENTENCE SAYS ITS THREE COUNTERS ARE |
| R634 | recorded | **answered** | §9a | `` | `floatfea/tolerances.py` SAYS NOTHING ASSERTS |
| R635 | recorded | **carried** | §9b | `` | THE WINDOW |
| R636 | recorded | **answered** | §9a | `` | What the new ceiling BUYS. The report justifies the change by what |
| R637 | recorded | **answered** | §2 | `` | R632 IS UNCHANGED AT THE REVIEWED COMMIT, AND THE |
| R638 | recorded | **carried** | §4 | `` | `RIGID_MODE_EXACTNESS` IS THE CEILING THE PRODUCTION |
| R639 | recorded | **answered** | §3 | `` | THE COUNTER INJECTION SIZE CAN BE RAISED EIGHT DECADES WITH |
| R640 | recorded | **answered** | §9a | `` | Three harness states commit |

## 8. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R632 | `docs/reports/F3/step-2.md` | the file is untouched | **no change.** Step 2 is closed; EG1's withdrawal was marked in place at `a647492` and its report stays the record of what it claimed. |
| R632 | `tests/test_report_guard_states.py` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:539` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:540` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:541` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:542` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:543` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:544` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:545` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:546` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R632 | `tests/test_report_guard_states.py:777` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R633 | `docs/milestones/F3.md` | the file is untouched | **no change.** F3 is CLOSED; its plan is the record. |
| R633 | `floatfea/tolerances.py:354` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R633 | `floatfea/tolerances.py:355` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R633 | `tests/test_counters_are_injected.py` | the file is untouched | TOUCHED at `95f6293` for R633; **no change at that exact line**. |
| R633 | `tests/test_counters_are_injected.py:317` | the file is untouched | TOUCHED at `95f6293` for R633; **no change at that exact line**. |
| R633 | `tests/test_counters_are_injected.py:318` | the file is untouched | TOUCHED at `95f6293` for R633; **no change at that exact line**. |
| R633 | `tests/test_counters_are_injected.py:319` | the file is untouched | TOUCHED at `95f6293` for R633; **no change at that exact line**. |
| R633 | `tests/verification/rung3/test_platform_rigid_modes.py` | the file is untouched | TOUCHED at `95f6293`, `3fdfc79` and `24e8bb2`; **no change at that exact line**. |
| R634 | `floatfea/model/platform.py:319` | the file is untouched | **no change at that exact line.** `check_rigid_modes` is cited as what makes `RIGID_MODE_EXACTNESS` assert again (R634) and as the namespace R638's registry cells must reach. |
| R634 | `floatfea/model/platform.py:320` | the file is untouched | **no change at that exact line.** `check_rigid_modes` is cited as what makes `RIGID_MODE_EXACTNESS` assert again (R634) and as the namespace R638's registry cells must reach. |
| R634 | `floatfea/tolerances.py:330` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R634 | `floatfea/tolerances.py:345` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R634 | `floatfea/tolerances.py:346` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R634 | `floatfea/tolerances.py:347` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R634 | `floatfea/tolerances.py:348` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R634 | `floatfea/tolerances.py:403` | the file is touched and this line number is the old one | TOUCHED at `b7c05e7`, `aec96e0` and `c9902d3`, comments only, no value; **no change at that exact line**. |
| R637 | `R634-docs/closure/F3.md` | the file is untouched | **no change at that exact line** -- and this row is C119 itself: the item prefix `R634-` is parsed as part of the path by `scripts/untouched_sites.py`. EJ3 routes it to F4 step 1's first commit. |
| R637 | `scripts/check_carried.py:51` | the file is untouched | **no change.** One of the three readers already anchoring correctly, cited as the form R637 adopts. |
| R637 | `scripts/ci_section.py:182` | the file is untouched | **no change.** The same, and its `_JUDGED` pattern is what verdict 86's bold line satisfies. |
| R637 | `tests/test_report_carried.py:247` | the file is untouched | TOUCHED at `24e8bb2` for R641; **no change at that exact line**. |
| R637 | `tests/test_report_guard_states.py:545` | the file is untouched | TOUCHED at `3fdfc79` (the anchor, the plant's Carried-number discovery) and `b7c05e7` (EI1's deletion); **no change at that exact line**. |
| R637 | `tests/test_report_numbers_are_sourced.py:102` | the file is untouched | TOUCHED at `3fdfc79` for R637's anchor; **no change at that exact line**. |
| R638 | `F2.md` | the file is untouched | **no change.** A closed milestone's plan; the plan guard reads every locked plan since `47daa3d`, which is why F3's tolerances live in F3.md. |
| R638 | `tests/test_counters_are_injected.py` | the file is untouched | TOUCHED at `95f6293` for R633; **no change at that exact line**. |
| R638 | `tests/test_no_tolerance_literals.py` | the file is untouched | **no change.** Cited as the guard whose domain is comparisons rather than injections, which is why it cannot see the `1.0e-8` literal R638 names. Recorded reach, not a defect. |
| R638 | `tests/verification/rung3/test_platform_rigid_modes.py:260` | the file is untouched | TOUCHED at `95f6293`, `3fdfc79` and `24e8bb2`; **no change at that exact line**. |
| R639 | `docs/milestones/F3.md:668` | the file is untouched | **no change.** F3 is CLOSED; its plan is the record. |
| R639 | `tests/verification/rung1/test_corpus_configurations.py` | the file is untouched | **no change.** Cited as the precedent `test_the_counter_DEFECT_SIZE_cannot_be_raised`, which R639's assertion is modelled on. Rung 1 is F2 apparatus, frozen under DR1. |
| R640 | `scripts/suite_count.py` | the file is untouched | TOUCHED at `b7c05e7` for EI0's two halves; **no change at that exact line**. |
| R643 | `docs/reports/F3/step-3.md:1354` | the file is touched and this line number is the old one | **this report**, and R643's site IS its suite line -- section 12 carries it now, measured in a clean clone outside the synced tree. |
| R643 | `tests/test_report_carried.py` | the file is untouched | TOUCHED at `24e8bb2` for R641; **no change at that exact line**. |

## 9. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R610 | **carried** — §9b | no clause this generator can cut -- see the verdict's Carried section |
| R611 | **withdrawn** — §9c | no clause this generator can cut -- see the verdict's Carried section |
| R612 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R613 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R614 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R615 | **carried** — §9b | no clause this generator can cut -- see the verdict's Carried section |
| R616 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R617 | **withdrawn** — §9c | no clause this generator can cut -- see the verdict's Carried section |
| R618 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R621 | **answered** — §9a | R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621, |
| R622 | **later** — §9c | no clause this generator can cut -- see the verdict's Carried section |
| R623 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R624 | **answered** — §9a | ANSWERED at 47daa3d, and I re-derived it rather than accepting it. The |
| R625 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R626 | **carried** — §9b | 's residue -- OPEN, LEDGERED to the same place, same ruling. The two |
| R627 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R628 | **answered** — §9a | no clause this generator can cut -- see the verdict's Carried section |
| R629 | **answered** — §9a | NOT CLOSED. IT CHANGED SHAPE AND IT IS RED ON BOTH MACHINES. R632. The |
| R630 | **answered** — §9a | ANSWERED at 47daa3d, verified line by line, and answered better than I |
| R631 | **carried** — §9b | OPEN, LEDGERED to docs/closure/F3.md section 4, and I ACCEPT the ledger |
| R632 | **answered** — §9a | ONE OF THE NINE REDS IS NOT THE STEP-BOUNDARY CLASS. THE PLANT ACTION CANNOT BUILD ITS STATE... |
| R633 | **answered** — §9a | THE NEW ENTRY'S FIRST SENTENCE SAYS ITS THREE COUNTERS ARE REGISTERED IN... |
| R634 | **answered** — §9a | floatfea/tolerances.py SAYS NOTHING ASSERTS RIGID_MODE_EXACTNESS AND THAT IT BOUNDS NOTHING,... |
| R635 | **carried** — §9b | THE WINDOW IS GUARDED ASYMMETRICALLY, AND EG0(c)'s 2x CLAUSE FIRES ON ROUTINE LEGAL CHANGES... |
| R636 | **answered** — §9a | What the new ceiling BUYS. The report justifies the change by what the old ceiling could not... |
| R637 | **answered** — §2 | R632 IS UNCHANGED AT THE REVIEWED COMMIT, AND THE DRAFT THAT WOULD FIX IT MAKES THE STATE... |
| R638 | **carried** — §4 | RIGID_MODE_EXACTNESS IS THE CEILING THE PRODUCTION BUILDER REFUSES REAL DECKS ON, AND IT CAN BE... |
| R639 | **answered** — §3 | THE COUNTER INJECTION SIZE CAN BE RAISED EIGHT DECADES WITH THE WHOLE REGISTRY AND BOTH EG0... |
| R640 | **answered** — §9a | Three harness states commit into the parent repository when the suite runs inside a git... |
| R643 | **answered** — §12 | test_the_report_carries_a_WHOLE_SUITE_count IS RED AT THE REVIEWED COMMIT AND STAYS RED WITH... |
| R644 | **answered** — §9a | EH1's two lists are short by one name on the state-(2) side and have one name on the wrong... |

## 9a. Answered in F3

* **R643** — answered by §12's suite line, which IS the finding: the line was the thing missing, and it survived revision 2 landing, which is why verdict 86 ruled it CZ1 (iv) rather than the boundary.
* **R644** — adopted at `66af185` under EJ2: `test_the_answered_verdict_is_the_NEWEST_one` moves to state (2) and `test_a_carried_row_points_at_a_section_that_discusses_it` is added to it.
* **R612** — carried as an earlier report records it.
* **R613** — carried as an earlier report records it.
* **R614** — carried as an earlier report records it.
* **R616** — carried as an earlier report records it.
* **R618** — carried as an earlier report records it.
* **R621** — carried as an earlier report records it.
* **R623** — carried as an earlier report records it.
* **R624** — answered at `47daa3d`, verified independently by the reviewer.
* **R625** — carried as an earlier report records it.
* **R627** — carried as an earlier report records it.
* **R628** — carried as an earlier report records it.
* **R629** — carried as an earlier report records it.
* **R630** — answered at `47daa3d`; three labelled sets, the shipped one printed per run.
* **R632** — answered at `95f6293`, and §2 records what its repair then exposed.
* **R633** — answered at `95f6293` — the three counters are registered and call the gate.
* **R634** — answered at `95f6293` — both sentences corrected.
* **R636** — carried as an earlier report records it.
* **R637** — answered in §2 — both anchors fixed, the plant targets the real Carried section, and the ABLATION shows the state is vacuous regardless.
* **R639** — answered in §3 — the size is bounded against the binding edge.
* **R640** — carried as an earlier report records it.

## 9b. Ledgered — margin characterisation, not correctness

In `docs/closure/F3.md` § 4 and § 4a under DZ7c and EH3.

* **R610** — carried as an earlier report records it.
* **R615** — carried as an earlier report records it.
* **R626** — **ledgered.** `docs/closure/F3.md` §4 under DZ7c.
* **R631** — **ledgered.** The figure is right; the operating point does not reproduce.
* **R635** — **ledgered**, and EH2 rules it: (a) never on fixed inputs, (b) a re-derivation on changed inputs in a `plan:` commit, (c) both edges at 2x. §5.
* **R638** — **ledgered per EH3** — recorded in the entry and in `docs/closure/F3.md` §4a; the registry row is backlog, not an F4 carry. §4.

## 9c. Withdrawn or routed to a later milestone

* **R611** — carried as an earlier report records it.
* **R617** — carried as an earlier report records it.
* **R622** — carried as an earlier report records it.

## 10. EH6 — not started, and the reason is a measurement

```
claim  where DY7's reactions come from, which EH6(a) asks, read from the body
cmd    read scripts/report_joint_reactions.py: solve_one() and main()
out    the script      scripts/report_joint_reactions.py
out    the call        integrate_cummins(lhs, kernel, xi0, xi_dot0, duration, dt,
out                    rho_inf=0.8, constraints=setup.constraints,
out                    external_force=ext, state_force=setup.state_force,
out                    projection_interval=1)
out    the field       `res.lam`, shape (steps, 16 joints x rows); it raises if
out                    `res.lam is None`, "which means `constraints` did not reach
out                    the integrator -- the whole premise of this report"
out    the case        ONE, at --period 10.0 --duration 40.0 --dt 0.01, MODEL
out                    scale, and the snapshot reported is `step = -1`, after the ramp
out    the units       N on translational rows, N.m on rotational, dt-free
rule   EH6(a): state the script, the solve-state fields, and which case
judge  so the reactions are the CONSTRAINT MULTIPLIERS taken from the solve state,
       not a post-processed export -- and extending to six cases means six calls to
       `solve_one` at the six periods, which are declared FULL scale in
       `run_floatsim_design_waves.py` and must be divided by sqrt(lambda) to reach
       the model-scale argument `solve_one` takes. That conversion is the first
       thing EH6(b) has to get right and it is the kind of thing this project
       refuses to assume.
cmd    the column names of the six design-wave CSVs
out    t_s, platform_heave_m, platform_heave_acc_mps2, and surge/sway/heave + acc
out    for buoy1, buoy4 and buoy7 ONLY -- 21 columns, no force of any kind
rule   EH6(b) wants all 16 joints over a steady-state window
judge  THE CSVs CARRY 3 OF 12 BUOYS AND NO FORCES, so the export cannot be
       post-processing: it has to re-run the six cases in `../HSP-runs` and read
       `res.lam` in-process, which is six FloatSim runs. That is what EH6(d)'s
       "work in the HSP-runs worktree" implies, and I will confirm the run cost
       before committing to the 7 October target rather than after.
```

## 11. Tolerances touched

**None this round.** EH2 added ruling text to an entry; no value moved.

```
cmd    git diff f2fa598..HEAD -- floatfea/tolerances.py, the value lines
out    (no output)
```

## 12. The whole suite

**Whole suite at `b7c05e7`: 2901 passed, 18 failed, 1 skipped.** One invocation, no
`--ignore`, in a clean clone — the reviewer's run, because four attempts of mine were
stopped at a thirty-minute limit and the reason was not the suite.

```
claim  the whole-tree figure and its wall time, at this commit
out    18 failed, 2901 passed, 1 skipped, 1245.47s
claim  why my runs stopped and the reviewer's did not
cmd    pytest tests/verification tests/unit -q, clean clone under the LOCAL temp dir
out    1802 passed in 216.86s
cmd    the same selection, same commit, same machine, in the OneDrive-synced tree
out    1802 passed in 399.16s
cell   ONE VARIABLE: the filesystem location
rule   a measurement apparatus that cannot run is not a measurement apparatus
judge  `1.84x`. The working tree is inside a synced folder, so the whole tree is
       ~38 min against a 30-minute limit and `--half main` lands at ~32. THE SPLIT
       WAS NOT THE FIX AND THE SUITE WAS NOT THE PROBLEM: `suite_count.py` is run
       from a clone outside the synced folder. No code change, no apparatus.

claim  the two halves at this commit, and the main half's colour
cmd    the report-guard set, same clean clone
out    18 failed, 221 passed, 1 skipped, 185.64s
cmd    the main set, DERIVED: 2920 collected - 240 in the three parametrised files
out    2680 passed, 0 failed, 0 skipped -- GREEN
rule   R309: one line, not seven subsets, because a subset cannot see a failure in
       an eighth file
judge  every one of the 18 reds is inside one of the three report-parametrised
       files, so the derivation hides nothing -- there is nothing outside them to
       hide. The whole-tree figure above is STRONGER than `--half main` because it
       carries no exclusion at all, which is the property R309 exists to assert.
judge  AND MY OWN GUARDS FIGURE WAS ONE COMMIT STALE: `222 passed` was taken at
       `24e8bb2`; at `b7c05e7` it is `221`, because `b7c05e7` deleted a parametrised
       state. CP3's own subject, caught by the reviewer and not by me.
judge  the line is NOT taken from the CI section's job counts: no CI job is the whole
       suite in one invocation -- two jobs split the work, two are skipped, and the
       lint job's count is a partition. CI stays the cross-check (EI0(b)).
```

**All eighteen named, and traced (EG3(i)).** Measured in a clean clone at `b7c05e7` **outside the synced tree**, which is also the control for the `1.84x` above:

```
cmd    git clone --no-local, checkout b7c05e7, pytest the three files -q
out    18 failed, 221 passed, 1 skipped in 67.49s
rule   EG3(i): every red traces BY NAME, and a red not on the list still blocks
judge  67.49s here against 185.64s in the reviewer's clone and over 13 minutes
       in the synced tree -- the same counts, so the only thing the location
       changes is time. SEVENTEEN are the boundary; ONE is not, and it is the
       first bullet below.
```

```
- **failed** `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R624->4]`  -- state (2), and R644: on NEITHER carve-out list
- **failed** `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R630->4]`  -- state (2), and R644: on NEITHER carve-out list
- **failed** `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:317]`  -- state (2), on the list
- **failed** `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:318]`  -- state (2), on the list
- **failed** `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R633-tests/test_counters_are_injected.py:319]`  -- state (2), on the list
- **failed** `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`  -- a run completed between generating section 0a and the measurement
- **failed** `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit`  -- state (2), on the list
- **failed** `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces`  -- state (2), on the list
- **failed** `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one`  -- state (2), and R644: filed under state (1) in EH1's text
- **failed** `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number`  -- state (2), on the list
- **failed** `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count`  -- R643 -- IT SURVIVES revision 3's landing, so CZ1 (iv) and NOT the boundary
- **failed** `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]`  -- the red BASELINE itself
- **failed** `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`  -- cascade off the red baseline
- **failed** `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]`  -- cascade off the red baseline
- **failed** `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]`  -- cascade off the red baseline
- **failed** `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]`  -- cascade off the red baseline
- **failed** `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`  -- cascade off the red baseline
- **failed** `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]`  -- cascade off the red baseline
```

**The main half's wall time, which EI0(d) asks for.** Two pre-existing figure guards
are essentially the whole cost:

```
cmd    per file, clean clone at b7c05e7 (upper bounds, other work on the machine)
out    tests/test_plan_figures.py              745.81s
out    tests/test_figure_local_check.py        523.42s
out    tests/test_counters_are_injected.py     205.72s
out    tests/test_ci_ladder_gating.py          185.94s
out    tests/test_collected_set_golden.py       38.26s
out    tests/test_ci_determinism_gate.py         1.16s
rule   EI0(d): state what it is now and what remains slow
judge  and the figure I had been citing as a baseline -- `1802 passed in 89.71s` --
       was `tests/verification` and `tests/unit` ONLY, never the main half, so I had
       no before-measurement of the thing that is slow. My claim that I had made the
       suite unrunnable is NOT supported for the main half: R642's cache is a real
       repair (the rung-3 file went 49.94s -> 1.09s) and it was not the cause.
```
