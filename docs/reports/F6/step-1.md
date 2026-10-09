# F6 step 1 — API RP 2A-WSD tubular member checks

# Revision 1 — the six clauses, the first full pass, and FA2's answer

Answers: FA3 opens the step

**2026-10-09.**

## 1. The schedule, and what this revision is

**F6 step 1's working target is 22 October and it holds.** Today is 9 October. The
committed date is 28 October.

**The deliverable went first, per FA3 and EY0's ordering.** `docs/F6_utilisation.csv`
(256 rows) and `docs/F6_utilisation.md` were sent before any of this report's guard work
existed. What this revision records is what was built and what it measured; **G6.1's
documented hand calculations are not in it** and are named in § 6 as the step's remaining
work.

**The step marker moved in this commit and not in the one before it.** FA3 says "the marker
moves in its first commit"; `test_the_plan_names_the_step_under_execution` says it is
"advanced in the commit that adds the next step's report, never before it". That is C27's
unresolved conflict, and it has now been directed one way and enforced the other. Both are
satisfied here because this commit carries both — stated rather than left as a silent
choice. **C27 still needs ruling for the general case.**

## 2. What step 1 built

`floatfea/checks/api_wsd.py` — six closed-form clauses, one function each, SI throughout.

```
claim  every allowable reproduces hand arithmetic
cmd    python -c "from floatfea.checks.api_wsd import *; ..."
out    F_t = 0.6 Fy            = 213.00 MPa   (hand: 213.00)
out    F_b, D/t=13.9           = 266.25 MPa  branch=compact   (hand: 266.25, compact)
out    F_v = 0.4 Fy            = 142.00 MPa   (hand: 142.00)
out    C_c = sqrt(2 pi^2 E/Fy) = 108.059            (hand: 108.059)
out    F_a at KL/r=  60.8      =  161.05 MPa  branch=inelastic
out    F_a at KL/r= 121.5      =   73.25 MPa  branch=elastic
out    F_e at KL/r=121.5       = 73.25 MPa   (hand: 73.25)
rule   API RP 2A-WSD sections 3.2.1, 3.2.2, 3.2.3, 3.2.4
judge  spot checks, not G6.1. **G6.1 asks for each check against an INDEPENDENT hand
       calculation documented in `docs/verification/`, and that does not exist yet** (§ 6).
       These seven lines catch a gross error and nothing subtler.
```

**The SI coefficients are the ones that matter and they are named in the module.**
§ 3.2.3's branch limits are `10340/F_y` and `20680/F_y` with `F_y` in **MPa**; writing the
US forms against a pascal `F_y` would misplace every branch boundary by about `145x`. The
two conversions happen in one place each.

**`D/t > 300` is refused rather than extrapolated.** The clause's third branch is written
only that far; beyond it local buckling governs and a beam-level allowable would be an
invented clause.

## 3. FA1 — the allowable F4's table was comparing against was the wrong one

```
claim  the 213.0 MPa reference is generic 0.6 Fy, not the API bending allowable
cmd    python -c "Fy=355.0; print(10340/Fy, 20680/Fy, 0.75*Fy, 0.6*Fy)"
out    10340/Fy = 29.13   20680/Fy = 58.25
out    D/t = 13.9 <= 29.13  ->  section 3.2.3 first branch
out    F_b = 0.75 Fy = 266.25 MPa     against the generic 0.6 Fy = 213.00 MPa
rule   API RP 2A-WSD section 3.2.3
judge  the generic reference is **1.25x conservative on bending** for this section. F4's
       table, summary and closure artifact are relabelled -- a published-deliverable
       correction under EZ0, folded into issue 5 rather than resent for itself.
```

## 4. FA2 — and the answer is that the axial term contributes almost nothing

This is the finding of the pass and it was not what I expected when EZ4 locked `K = 2.0`.

```
claim  the K lock moves four members onto a different formula and barely moves a number
cmd    python scripts/measure/api_wsd_utilisation.py
out    axial branch over 256 rows : elastic 32; inelastic 96; tension 128
out    largest |U(K=2) - U(K=1)|  : 0.024114  at platform:hub1_arm TIP (elastic)
out    worst compression station  : U = 1.70984  with U(K=1) identical
out    at the worst station: u_axial = 0.0004  against  u_bending = 1.815
rule   API sections 3.3.1 and 3.3.2; EZ4 Q3's K = 2.0 with FA2's K = 1.0 column
judge  **both halves are true and the second is the one that matters.** At `K = 2.0` the
       50 m platform arms do cross `C_c = 108.06` into the elastic branch while the 25 m
       hub arms stay inelastic -- the branch split § 0 of the plan predicted. But bending
       governs by three orders of magnitude, so § 3.3's interaction is bending plus a
       rounding error, the `C_m / (1 - f_a/F_e')` amplification never bites, and on the
       compression rows the simple `0.6 F_y` form of § 3.3.2 governs over the amplified one
       -- which contains no `K` at all. **The choice that looked like the biggest modelling
       decision in the check changes the governing number by at most `0.024`.**
```

It would matter on a member carrying real axial load. None of these does, and a reader who
was told only "K is the biggest sensitivity" would have mis-weighted the whole check.

## 5. The result

```
claim  four member-stations exceed unity and the governing clause is the same for all four
cmd    python scripts/measure/api_wsd_utilisation.py
out    4 of 32 member-stations exceed U = 1.0, the worst at 1.815
out    1  platform:hub2_arm ROOT  T = 12.5 s  3.3.1 interaction  U = 1.815
out    2  platform:hub4_arm ROOT  T = 12.5 s  3.3.1 interaction  U = 1.814
out    3  platform:hub3_arm ROOT  T = 16.2 s  3.3.1 interaction  U = 1.202
out    4  platform:hub1_arm ROOT  T = 12.5 s  3.3.1 interaction  U = 1.188
rule   EZ2's governing basis: T = 12.5, 14, 15, 16.2 s; ROOT and TIP only (FA3)
judge  all four are platform arm ROOTs, all § 3.3.1, all on bending, and three of the four
       are at `T = 12.5 s` -- the band's lower edge, which FA0 ruled stays and which
       governs because the response rises as `T` falls across the band.
```

**This is a finding about the section and the plan said so in advance.** The tube is a
stiffness equivalent for a truss of undecided depth, and F4 already had the static root at
`269.7 MPa` against a `213.0 MPa` reference under self-weight alone. `U = 1.815` on an
indicative screen of a stand-in section is the expected outcome, not news, and nothing was
tuned to bring it under unity.

## 6. What step 1 has NOT done

* **G6.1 is not met.** Each check needs an independent hand calculation documented in
  `docs/verification/api_wsd/`. § 2's seven lines are spot checks against arithmetic I did
  in the same sitting, which is not an independent path.
* **No counter-case per clause.** A check that cannot redden certifies nothing; each needs
  an injected input that pushes the utilisation past unity, with the injection size
  declared.
* **No tolerance is declared yet**, and none should be until the hand calculations measure
  what the closed forms agree to.
* **MID is excluded** (FA3) until R730's conditions are discharged — the closed-form
  midspan is a measured `4.0%` approximation on bending, unverified against a refined mesh.
  The exclusion is in the code, not in a note.
* **No circumferential stress recovery, no CalculiX cross-check, no VTK.** G6.2 and F7.

## 7. Carried

R730, R731 and R732 carry from F4's ledger, R730 and R731 blocking. C27 needs ruling for
the general case (§ 1). Nothing from F4's closure items is discharged here.

# Revision 2 — G6.1 first (FB0), and the deliverable behind it

Answers: verdict 110 @ 2cf33b0

**2026-10-09.**

## 0. CI at `0b9ea0d`, the commit verdict 110 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 110 at `0b9ea0d` through the report's own `Answers:` line. Run `37883813296`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 927 | 43 | 1 |
| the verification ladder | 2110 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 36.**

- `tests/test_report_carried.py::test_the_report_names_the_verdict_it_answers` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_blocking_item_is_not_routed_to_4a` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_parse_found_something_to_check` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_report_does_not_say_CLOSED` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_there_are_pointers_to_resolve` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_diff_the_site_check_needs_is_available` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[reviews_directory_renamed_away]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1_reports_one_diagnosis_not_sixteen]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)

## 0a. Runs since the commit verdict 110 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 110 at `0b9ea0d` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37883813296` | push | `0b9ea0d` | conclusion **failure** |

**Run `37883813296`, conclusion **failure**: 36 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_names_the_verdict_it_answers` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_blocking_item_is_not_routed_to_4a` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_parse_found_something_to_check` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_report_does_not_say_CLOSED` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_there_are_pointers_to_resolve` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_diff_the_site_check_needs_is_available` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[reviews_directory_renamed_away]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1_reports_one_diagnosis_not_sixteen]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)

## 1. The schedule, and what this revision is

**F6 step 1's working target holds.** Verdict 110 asked that if revision 2 closes still
carrying any of R739 to R746, the choice — slip the date or reduce scope — be stated rather
than restated. It does not: every one of the eight is answered below, R737 is decided, and
the verdict's closure list goes to the closure commit where CZ0 puts it. **Nothing is
carried forward blocking.**

```
claim  the dates this step is measured against, and today's
cmd    grep -n "October" docs/milestones/F6.md | tail -2
out    290:Drafted under EY4, **locked by EZ4**. Working target **22 October**, committed
out    291:**28 October**. F4 closed **9 October** against a committed 19 October, and the
cmd    date +%Y-%m-%d
out    2026-10-09
rule   CLAUDE.md section Step gating: the report's one hand-written paragraph carries the
       schedule -- which date the step is measured against, and whether it holds
judge  nineteen days of slack on the committed date and thirteen on the working target,
       with the step's locked content now built. Slippage is reported the day it is known
       and there is none to report.
```

**What this revision is, in one sentence: the ordering was inverted.** Verdict 110's
`On FA3 versus G6.1` section went to Xabier and came back as FB0 — G6.1 lands before the
next deliverable send — so the gate is the subject of this revision and the regenerated
table rides behind it, carrying the G6.1 line on its face.

## 2. G6.1 — the gate the step was locked to build

`tests/verification/rung5/test_g61_api_wsd_hand_calculations.py`. Every clause against the
clause arithmetic worked by hand in the test, in SI, with the clause cited — never the
module's own function (FB0, EA4).

```
claim  G6.1 exists, is green, and reads both new files
cmd    python -m pytest tests/verification/rung5/ -q
out    65 passed in 0.44s
cmd    grep -c "def test_" tests/verification/rung5/test_g61_api_wsd_hand_calculations.py
out    37
cmd    grep -c "# expected:" tests/verification/rung5/test_g61_api_wsd_hand_calculations.py
out    22
cmd    grep -rl api_wsd tests/ | grep -v corpus
out    tests/verification/rung5/test_g61_api_wsd_hand_calculations.py
rule   FB0: each clause function, two or more points per branch, either side of every
       boundary; the clause formula worked by hand, never the module's own function
judge  the verdict's `grep -rl api_wsd tests/` was EMPTY. The points are four per
       compression branch either side of `C_c`, two compact and four on each reduced
       bending branch either side of the two `D/t` limits, both sides of the
       local-buckling limit, both forms of section 3.3.2, and both refusals.
```

**AND IT IS RUNG 5, NOT RUNG 6, WHICH I HAD TO BE TOLD BY A GUARD.**

```
claim  G6.1 is V5.3 and belongs to rung 5; it was written into rung 6
cmd    grep -n "V5.3\|Gate G6.1\|Rung 6" docs/verification/README.md
out    177:**V5.3 Code check hand calculations.** Each API RP 2A-WSD utilisation term
out    180:and the code result. *Gate G6.1.*
out    186:## Rung 6 — It stays fixed
cmd    python -m pytest tests/test_ci_runs_the_whole_suite.py -q
out    65 of 3358 collected tests are run by no CI job   (before the move)
out    74 passed                                         (after)
rule   docs/verification/README.md orders the ladder by DEPENDENCY, and
       floatfea/tolerances.py's own section headers already put G6.1 under
       "Rung 5 -- Independent confirmation" and rung 6 under golden-file regression
judge  **THE TEST WAS GREEN IN THE WRONG RUNG AND NOTHING ABOUT ITS OWN RESULT SAID SO.**
       What said so was `test_every_test_in_the_suite_is_run_by_some_ci_job`: rung 6 is
       declared `empty:` in the workflow and carries a `.empty-by-design` marker, so the
       65 tests ran on my machine and in no CI job at all. The file is now in
       `tests/verification/rung5`, that rung is `full:` and its marker is deleted in the
       same commit, and `scripts/run_rung.sh` reports `65 collected, 0 failed, 0 errored,
       0 skipped`. **I had declared the tolerances under the rung-5 header while putting
       the test in rung 6**, which is the contradiction the guard caught.
```

**R742 is answered — the cap, and the cause is the clause's own continuity point.**

```
claim  F_b can no longer exceed 0.75 F_y at any admissible D/t
cmd    tests/.../test_G61_bending_never_exceeds_the_compact_value -- the whole domain,
       D/t from 0.1 to 845.9 in steps of 0.1, every value the clause returns for
rule   F_b <= 0.75 F_y everywhere (FB1)
out    65 passed  -- the sweep asserts `checked > 7000` so a narrowed domain fails loudly
out    before the cap: F_b = 267.785587 MPa at D/t = 29.1268 against the 266.25 cap,
out      staying above it to D/t = 30.5974
judge  the fix is in the CLAUSE TRANSCRIPTION and not in `E_STEEL`, which is what the
       verdict's closing condition required: `1500/F_y[ksi]` is continuous at
       `E = 29000 ksi = 199948 MPa` and this module runs at `210000 MPa`, so the converted
       limit sits below the continuity point and the reduced branch pokes above the cap on
       the interval between them. `E_STEEL` is a locked material constant and is untouched.
```

**R741 is answered — section 3.2.2(b) is implemented, and the refusal is exercised.**

```
claim  a slender tube is reduced, and one outside the clause is refused
cmd    tests/.../test_G61_local_buckling_reduces_a_slender_tube (D/t = 61, 100, 200, 300)
cmd    tests/.../test_G61_a_section_outside_the_clause_is_REFUSED_not_extrapolated
out    65 passed
out    before the repair: allowable_axial_compression at D/t = 100 returned
out      1.3610e+08 Pa, branch `inelastic`, no refusal and no reduction
rule   API RP 2A-WSD section 3.2.2(b): F_xc = F_y for D/t <= 60; above it
       F_xc = F_y[1.64 - 0.23 (D/t)^(1/4)] <= F_xe = 2 C E t / D, C = 0.3
judge  `allowable_axial_compression` now takes `D` and `t`, substitutes `F_xc` for `F_y`
       in the column form, names the branch `*_local` when it is reduced, and refuses
       above `D/t = 300`. The limit it uses is the clause's own `60`, not the bending
       clause's `300`, which is what the verdict's closing condition named.
```

**AND HALF OF SECTION 3.2.2(b) IS UNREACHABLE AT THE GRADE F6 LOCKS.** This is the finding
of the revision and it was found by running the model at a configuration nothing in the
diff chose.

```
claim  F_xe never governs min(F_xc, F_xe) at F_y = 355 MPa, at any D/t the clause admits
cmd    scratch sweep: F_xc and F_xe at F_y = 355, 460, 690, 960 MPa over D/t, then the
       crossing solved for each grade
rule   section 3.2.2(b) takes the MINIMUM of the two
out    F_y = 355 MPa: F_xe first governs at D/t = nan      -- never, at any D/t
out    F_y = 460 MPa: F_xe first governs at D/t = 491.94   -- OUTSIDE D/t <= 300
out    F_y = 690 MPa: F_xe first governs at D/t = 252.53   -- inside
out    F_y = 960 MPa: F_xe first governs at D/t = 159.57   -- inside
out    at D/t = 300, F_y = 355: F_xc = 242.39 MPa against F_xe = 420.00 MPa
judge  **`ELASTIC_LOCAL_BUCKLING_C` AND THE WHOLE ELASTIC HALF OF THE CLAUSE ARE INERT AT
       S355**, so a G6.1 that checked only the shipped material would have certified
       nothing about them -- the measured response to scaling that coefficient was exactly
       `0.000000e+00`. The hand calculation takes it at `F_y = 690 MPa`, `D/t = 260` and
       `300`, where `F_xe` is the minimum, and asserts that the same `D/t` at S355 is
       governed by the other half. **Flagged for Xabier**: nothing on the platform is
       remotely this slender, so this is about the function being right rather than about
       the structure.
```

**The tolerance the comparison needs, declared by the window rule over the whole counter
family.**

```
claim  the ceiling is measured, not invented, and both edges clear the window rule's floor
cmd    tests/.../test_the_ceiling_and_its_counter_BRACKET_the_family_BOTH_ways
cmd    scratch: the 32 points by hand against the module, then each clause coefficient
       scaled by 1 + F6_API_CLAUSE_INJECTION_EPS one at a time
rule   the window rule: the ceiling sits between the clean worst and the weakest live
       response, both edges above F4_WINDOW_RULE_MIN_EDGE = 2.0
out    POINTS                 : 32
out    CLEAN WORST            : 1.683679572698748e-16   at 3.2.2b F_xc D/t=61.0
out    points bit-identical   : 31 of 32
out    WEAKEST LIVE           : 8.283918449512958e-13   (CM_JOINT_TRANSLATION)
out    geometric centre       : 1.180993830438892e-14
out    F6_API_CLAUSE_AGREEMENT = 1.0e-14   edges 59.3937x and 82.8392x
out    F6_API_CLAUSE_AGREEMENT_COUNTER = 8.0e-13   margin below the weakest live 1.0355x
out    EH4 injection falling  : eps may FALL to 1.207158e-14 (82.84x) before its weakest
out                             response reaches the ceiling
judge  **31 OF 32 POINTS AGREE TO THE BIT.** The one that does not is `(D/t)^(1/4)`, the
       only FRACTIONAL power in the six clauses, and the headroom exists because `pow` is not
       required to be correctly rounded and CI runs ubuntu where this was measured on
       Windows. The injection is deliberately at round-off scale: the clause coefficients
       are exact decimals, so a real transcription error is percent-scale and is caught ten
       decades over -- what the counter-case measures is that the comparison is not vacuous.
```

**THE COUNTER-CASE FAMILY HAD TO BE REPAIRED BEFORE IT MEASURED ANYTHING, and that is the
part worth reading.** Four of its seven members responded exactly zero, each for a
different reason.

```
claim  four of seven family members were vacuous, and the three live ones all sat at
       sensitivity 1.0 -- which is what a family looks like when it only tests the
       comparison
cmd    scratch: each coefficient scaled by 1 + 1e-12, one at a time, worst relative move
       over the 32 points
out    FIRST ATTEMPT -- LIVE 3 of 7, dead: ELASTIC_LOCAL_BUCKLING_C, CM_JOINT_TRANSLATION,
out      LOCAL_BUCKLING_DT, BENDING_THIRD_BRANCH_NUMERATOR
out    AFTER THE REPAIR -- LIVE 5 of 5:
out      CM_JOINT_TRANSLATION       8.283918e-13   sens 0.828392
out      ALLOWABLE_SHEAR_FACTOR     1.000057e-12   sens 1.000057
out      ELASTIC_LOCAL_BUCKLING_C   1.000062e-12   sens 1.000062
out      BEAM_SHEAR_AREA_FACTOR     1.000067e-12   sens 1.000067
out      ALLOWABLE_TENSION_FACTOR   1.000127e-12   sens 1.000127
cell   one coefficient moved per run, everything else held, same 32 points
judge  **THREE DIFFERENT CAUSES AND NONE OF THEM IS ARITHMETIC.** `F_xe` is unreachable at
       S355 (above). `check_member`'s `cm` default is bound AT IMPORT, so perturbing the
       module global is inert and the injection has to go through the parameter -- which
       also means nothing otherwise asserted that the default IS the declared constant, and
       now something does. And the two THRESHOLDS respond to a relative nudge only where a
       point sits within `eps` of one, so they are not in this family at all: their
       counter-cases MOVE THE LIMIT PAST A POINT and assert the branch changes.
```

```
claim  the two threshold counter-cases redden, and are undone
cmd    tests/.../test_G61_the_local_buckling_LIMIT_is_what_decides_the_reduction
cmd    tests/.../test_G61_the_third_branch_LIMIT_is_what_decides_the_refusal
out    65 passed
out    LOCAL_BUCKLING_DT 60 -> 62: D/t = 61 goes 'inelastic_local' -> 'inelastic'
out    BENDING_THIRD_BRANCH_NUMERATOR 300000 -> 200000: D/t = 700 goes 'reduced_2' ->
out      REFUSED, "where API section 3.2.3 is not written"
judge  each asserts the original value is restored afterwards, so a test that left the
       module perturbed would fail in its own body rather than poisoning the next one.
```

**And `C_m`'s sensitivity is itself a measurement about where the point was taken.**

```
claim  the gate resolves a C_m error to 0.828392 of its relative size, and the first point
       tried resolved it to 0.151897
cmd    scratch: the C_m sensitivity of u_combined over axial load, bending moment and both
       branches of section 3.2.2, with max(amplified, simple) as the module computes it
rule   C_m appears ONLY in section 3.3.2's amplified form, so its sensitivity is zero
       wherever the simple form governs
out    KL/r = 121.5, N = -1e6, My = 5e7, Mz = 3e7  : sens 0.151897, SIMPLE governs
out    KL/r = 121.5, N = -1e7, My = 1e8            : sens 0.828392, AMPLIFIED governs
out    KL/r =  60.8, N = -1e8, My = 1e8            : sens 0.562374, AMPLIFIED governs
judge  **AT THE OBVIOUS POINT THE AMPLIFIED FORM DOES NOT GOVERN AT ALL.** `u_combined` is
       `max(amplified, simple)` and the simple form carries no `F_a`, no `F_e'` and no
       `C_m`, so a hand calculation taken there is correct and measures nothing -- the
       entire amplified branch could be wrong and it would still agree. The gate's two
       amplified points are the high-axial ones, each asserts `amplified > simple` in its
       own body, and `C_m` is still the family's weakest member by `1.21x`.
```

## 3. R744 — the sag control now reads the published value, and R734 is its subject

```
claim  the control was on the two lines that DEFINE the sags and had no reach on the two
       that APPLY them; it now reads `mid - chord`, which is what the station publishes
cmd    python <scratch>/r744_cell.py   -- one variable moved per run: the control, against
       the same four one-character reversions
rule   the published MID carries `mid - chord`, so that difference is the subject
out    === the HEAD control ===
out      definition, My     -> CAUGHT         exit 1
out      definition, Mz     -> CAUGHT         exit 1
out      APPLICATION, My    -> *** MISSED *** exit 0
out      APPLICATION, Mz    -> *** MISSED *** exit 0
out      unperturbed        -> exit 0
out    === the repaired control ===
out      definition, My     -> CAUGHT         exit 1
out      definition, Mz     -> CAUGHT         exit 1
out      APPLICATION, My    -> CAUGHT         exit 1
out      APPLICATION, Mz    -> CAUGHT         exit 1
out      unperturbed        -> exit 0
out    the working tree is restored: True
cell   the control is the only thing that changes between the two halves; the four
       reversions, the fixture, the window and the section are identical
judge  **`exit 0` ON THE TWO MISSED ROWS IS THE WHOLE FINDING**: the table was written, the
       script succeeded, and the published `Mz` was wrong. The repair captures the chord
       mean before the sags are applied and signs the difference, so a flip in either half
       reddens. No threshold, no constant, no new file.
```

**And the first version of that cell was wrong in two ways, which is worth recording
because both made it print the answer I expected.**

```
claim  the cell's first version measured HEAD twice and exited 1 on every run
cmd    the first version's own output
out    === the repaired control ===
out      definition, My     -> CAUGHT
out      APPLICATION, My    -> *** MISSED ***
out      unperturbed        -> exit 1
judge  it read the "repaired" source back off disk AFTER the HEAD loop had overwritten the
       file, so both halves were HEAD -- and it wrote the table's output to a tempdir
       outside the repository, where the script's own final `relative_to(ROOT)` raises, so
       `unperturbed -> exit 1` on a clean tree. **Two identical halves and a failing
       control are the tells**, and the second version captures the source once and writes
       inside the repository.
```

```
claim  R744 moved no published value
cmd    python scripts/measure/member_forces_table.py  then  diff against the pre-R744 output
out    wrote docs/F4_member_forces.csv (1248 rows)
out    (no diff)
rule   BP0: a figure is regenerated by the code that ships
judge  the change captures a chord that was already being computed; the arithmetic is
       untouched, and this is the command that says so rather than an argument that it must be.
```

## 4. R739 and R740 — confirmed, and the one figure that does not reproduce

Both were answered in the commit the verdict judged the predecessor of, and the verdict
re-derived the figures independently. Four of its five reproduce exactly. **The fifth does
not, and the disagreement is R740 rather than an error in either of us.**

```
claim  the verdict's figures to beat, measured on the shipped table
cmd    python scripts/measure/api_wsd_utilisation.py  then read docs/F6_utilisation.csv
rule   verdict 110's "my figures to beat" list
out    F_a on the four platform ROOTs : 73.1922 MPa   (verdict: 73.25, elastic)
out    F_a on the hub ROOTs           : 161.078 MPa   (verdict: 161.02, inelastic)
out    all four over-unity rows       : section 3.3.2 / 3.3.1 by sign -- two and two
out    governing U                    : 1.71167   (verdict's per-instant figure: 1.7115)
out    largest |U(K=2) - U(K=1)|      : 0.034238  (verdict: 0.034926)
judge  **THE LAST ONE IS THE DISAGREEMENT AND IT IS THE DIFFERENCE BETWEEN THE TWO BASES.**
       The verdict measured `0.034926` with the sign corrected on the `total_max`/
       `total_min` rows, which is what the file then carried; the shipped table is
       `total_instant`, which is R740's own repair, so the K sensitivity is measured on a
       different set of six components. `73.1922` against `73.25` and `161.078` against
       `161.02` are the same quantity to three figures -- the verdict computed them at
       `KL/r` of exactly `121.5` and `60.8`, the table at the section's own
       `r = sqrt(I_y/A)`.
```

```
claim  the governing number MOVED when R740 was answered, and the direction is down
cmd    read the governing row of docs/F6_utilisation.csv, against what was published
rule   R740: the per-instant value is the physical one; the envelope is an upper bound
       whose six components do not occur together
out    published before : U = 1.815  at platform:hub2_arm ROOT, section 3.3.1, F_a = 213.00
out    shipped now      : U = 1.71167 at platform:hub2_arm ROOT, section 3.3.2, F_a = 73.1922
out    f_b = 455.7 MPa against F_b = 266.25 MPa, so u_bending = 1.7114
out    rows 32   over unity 4
judge  **TWO CORRECTIONS IN OPPOSITE PARTS OF THE CALCULATION, AND THE BASIS IS THE BIGGER
       ONE.** R740 takes the station from the envelope to the per-instant components, which
       lowers `f_b` from `483.2` to `455.7 MPa`; R739's sign moves the member from tension
       to compression, which changes the clause and drops `F_a` from `213.00` to `73.19` --
       and because the simple form of section 3.3.2 governs on this row, that `F_a` change
       does not reach `U`. The number a reader cares about fell `5.7%` and the clause it is
       computed under changed.
```

## 5. R743 and FB2 — `C_m`, and the column beside it

```
claim  the constant is named for the category it is, its direction is stated as measured,
       and the C_m = 1.0 column is published
cmd    grep -n "CM_JOINT_TRANSLATION" floatfea/checks/api_wsd.py scripts/measure/api_wsd_utilisation.py
cmd    tests/.../test_G61_a_LARGER_Cm_RAISES_the_compression_utilisation
cmd    read the C_m column of docs/F6_utilisation.csv
rule   section 3.3.1 case (a): members in frames subject to joint translation, C_m = 0.85
out    the constant is CM_JOINT_TRANSLATION; "no transverse load" appears nowhere
out    65 passed  -- the direction is asserted at an AMPLIFIED-governing point, because at
out      a simple-governing point C_m has no effect and the assertion would be vacuous
out    largest |U(C_m=1) - U(C_m=0.85)| : 0.009245  at hub2:buoy4_arm ROOT (inelastic)
out    at the governing station          : 1.71365 against 1.71167
judge  **THE DIRECTION IS NOW THE MEASURED ONE AND THE DELIVERABLE'S LABEL SAYS SO**:
       `C_m = 1.0` raises the compression utilisation and `0.85` is the LESS onerous of the
       two, which is the opposite of what the module claimed. The category now matches
       `K = 2.0`'s own sidesway assumption instead of contradicting it.
```

**And the verdict's ranking of the two levers does not survive the per-instant basis,
which is worth saying plainly because it was the verdict's own correction of my headline.**

```
claim  on the shipped basis C_m and K are both small, and C_m is the larger of the two
cmd    read both sensitivity columns of docs/F6_utilisation.csv over all 32 rows
rule   the levers are compared on the number that is published, not on a prior basis
out    largest |U(K=2) - U(K=1)|        : 0.034238   at platform:hub1_arm TIP (elastic)
out    largest |U(C_m=1) - U(C_m=0.85)| : 0.009245   at hub2:buoy4_arm ROOT (inelastic)
out    at the four over-unity stations, K moves U by 0.000000 on every one
out    the verdict's own ratio, on the envelope basis it measured: 0.128855 / 0.024114
out      = 5.343576345691299x, which is where its `5.3x` came from
judge  **K IS NOW THE LARGER OF THE TWO, AND BOTH ARE SMALL, AND NEITHER MOVES THE
       GOVERNING NUMBER.** The verdict measured `C_m` at `0.128855` against `K` at
       `0.034926` on the envelope basis; on the per-instant basis they are `0.009245` and
       `0.034238`. The reason is the same one in both directions: `C_m` lives only in
       section 3.3.2's amplified form, the simple form governs every over-unity row, and
       `K` reaches `U` only through `F_a` -- which the simple form does not contain. So
       `0.0` at all four stations is not a coincidence, it is the clause. **The conclusion
       that survives both bases is the one the verdict said survives: the axial term
       contributes almost nothing** -- `u_axial = 0.0008` against `u_bending = 1.7114` at
       the governing station.
```

## 6. R737 — decided, and the verdict's framing needed one correction first

Verdict 110 carried R737 as blocking: "`HSP_COMMIT` declared and compared nowhere". **That
is not quite right, and finding out why is what decided the item.**

```
claim  HSP_COMMIT IS compared -- in the geometry exporter, against the live worktree
cmd    grep -rn HSP_COMMIT floatfea scripts tests --include=*.py
out    floatfea/hsp_pin.py:19:HSP_COMMIT: Final[str] = "25de7ce"
out    scripts/export_platform_deck.py:86: if not head.startswith(hsp_pin.HSP_COMMIT) and
out      not hsp_pin.HSP_COMMIT.startswith(head):
out    scripts/export_platform_deck.py:87:     raise SystemExit(...)
out    tests/verification/rung3/test_platform_deck_export.py:166: the deck text names it
rule   docs/hsp-coupling.md: every FE result is traceable to an exact simulator state
out    export_platform_deck.py refuses THREE WAYS before writing: the worktree must
out      describe as HSP_TAG, its HEAD must be HSP_COMMIT, and `status --porcelain` must
out      be empty (R584)
judge  **SO THE GEOMETRY SIDE IS PINNED AT COMMIT LEVEL ALREADY**, and the pattern the
       finding asks for exists in this repository, three lines, with its own test.
```

```
claim  what is NOT pinned at commit level is the dynamic-inputs npz
cmd    read data/f4/dynamic_inputs.provenance.json's HSP fields, and the deck's header
out    npz provenance : hsp_tag: 'floatfea-ref-1  (HSP-runs)'      -- the tag, and only it
out    deck header    : HSP tag    floatfea-ref-1
out    deck header    : HSP commit 25de7ce
rule   a tag is movable and a sha is not
judge  **BOTH CAME FROM THE SAME WORKTREE, `HSP-runs`, AT THE SAME PIN.** So the npz's
       warrant is the tag in its own provenance PLUS the deck exporter's commit-level and
       dirty refusals, which prove that worktree was at `25de7ce` and clean. That is
       indirect but it is not nothing, and it is narrower than "compared nowhere".
```

**Why the fix is scheduled rather than applied, and the reason is a gate rather than a
preference.**

```
claim  adding the refusal to the dynamic export forces a re-export of the npz
cmd    grep -n "generating_script\|import_closure" tests/verification/rung4/test_f4_g41_dynamic.py
out    :265  expected = dict(declared.get("import_closure", {}))
out    :266  for key in ("generating_script", "measurement_module"):
rule   EX0(c): the gate asserts the provenance's recorded blob shas against the tree, so
       the code that wrote the file cannot move without the file being rewritten
judge  `scripts/export_f4_dynamic_inputs.py`'s own blob sha is on that list, so editing it
       to add three lines reddens G4.1 until the npz is regenerated -- six FloatSim runs
       over the DQ6 window. The gate is right to do that; it is R726's whole point.
```

**The decision: `export_f4_dynamic_inputs.py` adopts `export_platform_deck.py`'s three
refusals and records `hsp_commit` in the provenance AT THE NEXT EXPORT**, whenever the npz
is next regenerated for any reason. Until then the npz's HSP state rests on the tag plus the
deck's indirect commit-level warrant above, which is stated here and in the results label
rather than discharged. **This is Xabier's to overrule if a re-export is wanted sooner** —
it costs six FloatSim runs and moves no number.

## 7. R745 — the suite, and EG3's trace

```
claim  nothing outside the report guards is red, and every red traces by name to EG3's
       state (1) -- report written, verdict not yet
cmd    python -m pytest -q   (one invocation, no -k, no --ignore, no deselection)
out    <the whole-suite line is below, generated by scripts/suite_count.py and run LAST>
rule   EG3(i): the pre-invocation green requirement is waived only if EVERY red traces by
       name to the step-boundary cause, and the trace is pasted
out    by file: tests/test_report_carried.py, tests/test_report_guard_states.py and
out      tests/test_report_numbers_are_sourced.py -- and nothing else
out    the baseline, test_the_guard_reads_the_step_being_worked_on, is on state (1)'s own
out      list (EH1), and test_report_guard_states.py's planted states cascade off it:
out      each cascading state's failure line pastes the baseline's reds
judge  **STATE (1), AND IT CLEARS AT THE VERDICT COMMIT.** The reviewer measures that half;
       EG3 says so explicitly, because the reviewer runs at the judged commit before
       writing. What revision 1 could not do was paste the trace at all -- it carried no
       suite count, so there was no claim to hold to. That is the part R745 was about.
```

**And one piece of R745 is not the report's to fix, which verdict 110 said and I agree
with.** `VERDICT` resolves to the newest file under the milestone's review directory and
falls back to `step-0.md` when there is none, so at the **first step of a new milestone** a
dozen assertions are keyed on a file that cannot exist yet. That is EG3's boundary one level
up — a milestone boundary rather than a step boundary — and EG3's two lists do not name it.
It needs a third state in `CLAUDE.md`'s list, which is Xabier's; until then the honest
reading is the one EG3 already gives, and this section is it.

## 8. The F4 ledger, and the list R746 was about

Verdict 110's first finding against revision 1 was its `Carried` section: it answered
verdict 108's list, named **R731** as blocking when verdict 109 had closed it, and did not
name **R734**, **R735**, **R736**, **R737** or **R738** at all. The header now names verdict
110 and the table in § 9 is the generator's.

**R730 and R731 are closed, and the closing was verdict 110's own measurement.** R730 was
the MID station computed as the mean of the two RAW ends, which is a load and not an
internal action, and it reached a sent deliverable. R734 was my first repair of it giving
both bending planes the same sag sign. Verdict 110 verified all four parts of its own
condition on R734 and found the residue, which is R744 and is § 3.

**R732 is closed by verdict 109** and is not re-raised here.

**R735, R736 and R738 remain open as closure items**, carried in `docs/closure/F4.md` as a
list. R735 is the one-sign-for-two-planes sentence at the top of
`scripts/measure/member_forces_table.py`; it is C47 in verdict 110's closure list and it
goes in the closure commit with the rest.

```
claim  R735 has not regressed further, and it is at THREE sites and not one
cmd    grep -n "w L\^2 / 8" scripts/measure/member_forces_table.py
out    65:shear linear, moment parabolic, so the midspan moment is the chord mean plus
out       `w L^2 / 8`.
out    372:    so its mid value is the chord mean plus `w L^2 / 8` with `w` the local
out       transverse
out    861:        "`w L^2 / 8` on the two bending components. A refined mesh would give it
out       directly.",
rule   the derivation in the code gives `- w_z L^2/8` on My and `+ w_y L^2/8` on Mz --
       the two planes carry OPPOSITE signs
judge  **ONE SIGN FOR TWO PLANES, AT THREE SITES, AND THE THIRD IS IN THE PUBLISHED
       LABEL** (`:861`). Verdict 110's C47 named `:65`; the grep names two more, and one
       of them is in a deliverable, so under EZ0 the published one is not purely prose.
       **It is still a closure item** -- the CODE carries the two signs and has since
       R734's repair, so no number is wrong -- but it goes in the closure commit as three
       sites rather than one.
```

**R712 to R717 and the C-items of F4's closure list** remain open in `docs/closure/F4.md`,
not re-adjudicated here, per CZ0.

```
claim  the F4 ledger is a list in the closure artifact and this revision does not touch it
cmd    git diff --stat HEAD -- docs/closure/F4.md
out    (empty)
rule   CZ0: a finding that is not (a) to (d) is a closure item, listed once and fixed in
       the step's closure commit, not re-reviewed item by item
judge  the carried names are read from the verdict rather than from my memory of them,
       which is what the generated table in section 9 is for and what R746 was about.
```

## 8a. Every site the verdict named, site by site

**A closing condition that names sites is closed site by site, and half of an item is not
the item.** The verdict named 40 sites across eight findings. The ones the diff touches are
in the sections above. These are the ones it does **not** touch, each with what was done
instead — the escape hatch is deliberate and each row is a claim a reviewer can check.

```
claim  the sites below are untouched by this step's diff, and the rest are touched
cmd    git diff -U0 0b9ea0d -- . ":(exclude)docs/reviews" ":(exclude)tests/corpus"
rule   tests/test_report_carried.py's site check: a named site is in the diff, or the
       newest revision says `no change` beside that exact site
out    the table below is the untouched set, 37 of 40
judge  three sites are touched and need no row: `floatfea/checks/api_wsd.py:133` (the
       signature), `:148` and `:150-153` (the branch guards and the inelastic form).
```

| site | status | what was done instead |
|---|---|---|
| `docs/conventions.md:320` | no change — **by design** | it is the AUTHORITY, locked at F0. "Positive axial force: tension positive" is what the publishing boundary was corrected to agree with; changing it would be reopening the F0 gate (CLAUDE.md § Conventions) |
| `floatfea/checks/api_wsd.py:254` | no change | old `in_tension = axial_n >= 0.0` is CORRECT given a tension-positive column. R739's defect was the column, not the reader, so the fix is at the publishing boundary in `scripts/measure/member_forces_table.py` and this line is right as written |
| `floatfea/post/member_forces.py:23` | no change — **already correct** | the attribution sentence already says "the forces the ELEMENT exerts on its nodes at each end", which is the true sense and is what R739 measured. The verdict's condition asked for it to be corrected; it did not need correcting |
| `scripts/measure/api_wsd_utilisation.py:138` | no change | `axial_n=float(r["N"])` is correct once the column it reads is tension-positive. Negating here as well would double the fix |
| `scripts/measure/member_forces_table.py:415` | no change | the `0.5 * (a + b) -> Vz = +2299218.75` cell is R730's measurement and is still true; it is the evidence for the convention, not a statement of it |
| `scripts/measure/api_wsd_utilisation.py:81` | no change | a bare `)` closing the label tuple at the reviewed commit. The label block above it is rewritten and two labels are added; this line is punctuation |
| `floatfea/basis.py:46` | no change — **the verdict forbade it** | `E_STEEL = 210e9` is a locked material constant and R742's closing condition says explicitly "**Not** by changing `E_STEEL`". The fix is in the clause transcription |
| `floatfea/checks/api_wsd.py:102` | no change | `limit_1 = 10340.0 / fy_mpa` is the standard's own SI rounding and R742's option (i) keeps it. What changed is the cap below it, not the limit |
| `floatfea/checks/api_wsd.py:73` | no change | a blank line inside the `C_m` docstring at the reviewed commit. The docstring around it is rewritten for R743 |
| `floatfea/checks/api_wsd.py:77` | no change | the docstring's closing `"""`. Same rewrite |
| `floatfea/checks/api_wsd.py:134` | no change | `allowable_axial_compression`'s docstring, FA2 paragraph — kept verbatim because it is still true and still the reason the branch is reported |
| `floatfea/checks/api_wsd.py:135` | no change | same docstring |
| `floatfea/checks/api_wsd.py:136` | no change | same docstring |
| `floatfea/checks/api_wsd.py:137` | no change | same docstring |
| `floatfea/checks/api_wsd.py:138` | no change | same docstring |
| `floatfea/checks/api_wsd.py:139` | no change | same docstring |
| `floatfea/checks/api_wsd.py:140` | no change | same docstring |
| `floatfea/checks/api_wsd.py:141` | no change | the blank line before the branch table |
| `floatfea/checks/api_wsd.py:142` | no change | the branch table's `inelastic` row — the formula verdict 110 verified to the fifteenth digit |
| `floatfea/checks/api_wsd.py:143` | no change | the branch table's `CSF` row, same verification |
| `floatfea/checks/api_wsd.py:144` | no change | the branch table's `elastic` row, same verification |
| `floatfea/checks/api_wsd.py:145` | no change | the docstring's closing `"""` |
| `floatfea/checks/api_wsd.py:146` | no change | `if k_l_over_r <= 0.0:` — the positivity guard, still correct |
| `floatfea/checks/api_wsd.py:147` | no change | its `raise ValueError`, still correct |
| `floatfea/checks/api_wsd.py:149` | no change | `c_c = column_slenderness_parameter(...)` — now called with `f_xc` in place of `fy`, which is the line below it; the call itself is unchanged in form |
| `scripts/measure/member_forces_table.py:446` | no change | the R734 measurement cell (`w_y = -7.1836e+03`, the two forms). It is the evidence for the two signs and is still true |
| `scripts/measure/member_forces_table.py:449` | no change | `sag_z = +w_local[1] * span * span / 8.0` is CORRECT and stays. R744 is not that line — it is that the control read it instead of reading the published value |
| `CLAUDE.md` | no change — **and it is Xabier's** | R745's own last paragraph says the milestone-boundary state needs a third state in EG3's list, which is prose in `CLAUDE.md` and not the implementer's to write (the reviewer's instructions and the process rules change only in a standalone `process:` commit citing the directive) |
| `docs/reviews/F6/step-1.md` | no change — **forbidden** | the implementer never writes, edits or deletes a verdict; a `PreToolUse` hook refuses it, Bash included |
| `scripts/ci_section.py` | no change | it is RUN, not edited: § 0 and § 0a are its output, anchored on this revision's own `Answers:` line |
| `scripts/suite_count.py` | no change | it is RUN last, after every other edit (CP3), and its line is at the end of this revision |
| `tests/test_report_carried.py` | no change | it is the guard R745 is measured by. An existing guard that fails false is fixed or deleted and never extended (CZ0); this one does not fail false — it was right that revision 1 carried no suite count, no CI section and no answers file |
| `tests/test_report_carried.py:211` | no change | `VERDICT = REVIEWS / f"step-{max(REVIEWED)}.md" if REVIEWED else ...` is the milestone-boundary line, and it is the subject of the paragraph above that goes to Xabier rather than something to edit here |
| `tests/test_report_guard_states.py` | no change | the planted-state guard, unedited; its reds cascade off the baseline and are traced by name in § 7 |
| `tests/test_report_numbers_are_sourced.py` | no change | unedited; five of its sections were red against revision 1 and all are green against this one |
| `docs/reports/F6/step-1.md:5` | no change — **deliberately** | line 5 is REVISION 1's `Answers: FA3 opens the step`, and EK3 forbids touching a step report after that report's final verdict. The correction R746 asks for is revision 2's own header, which reads `Answers: verdict 110 @ 2cf33b0` |

## 9. Carried

**The row set, the class and the subject are the verdict's; the state and the pointer are
`docs/reports/F6/step-1-answers.json`'s. Neither is retyped here.**

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R712 | **open** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R717 | **open** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R730 | **answered** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R731 | **answered** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R732 | **answered** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R734 | **answered** — §3 | (blocking, carried into F6's ledger) -- CLOSED, and I measured all four |
| R735 | **open** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R736 | **open** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R737 | **answered** — §6 | (blocking, carried into F6's ledger) -- STILL OPEN, AND NOTHING IN THIS STEP |
| R738 | **open** — §8 | no clause this generator can cut -- see the verdict's Carried section |
| R739 | **answered** — §4 | AS AMENDED BY EZ0, AND ALSO (a) ON THE UNAMENDED HEAD, BECAUSE THE DEFECT IS IN floatfea/.) THE... |
| R740 | **answered** — §4 | UNDER EZ0.) U = 1.815 IS THE PER-COMPONENT ENVELOPE BOUND, THE DELIVERABLE'S LABEL SAYS IT IS... |
| R741 | **answered** — §2 | , AND THE LOCKED PLAN REQUIRES IT IN ITS OWN WORDS.) Â§ 3.2.2's LOCAL-BUCKLING CHECK IS NOT... |
| R742 | **answered** — §2 | .) allowable_bending RETURNS MORE THAN 0.75 F_y, WHICH NO READING OF Â§ 3.2.3 PERMITS, FOR D/t... |
| R743 | **answered** — §5 | .) CM_NO_TRANSVERSE_LOAD = 0.85 IS DECLARED UNDER THE WRONG CLAUSE CATEGORY AND ITS... |
| R744 | **answered** — §3 | -- ASSERTION DOMAIN BLINDNESS, AND IT IS THE CONTROL THAT ANSWERED VERDICT 109's BLOCKING... |
| R745 | **answered** — §7 | .) 43 RED TESTS AT THE REVIEWED COMMIT AND A RED CI JOB, AND THE EG3(i) TRACE IS NOT PASTED... |
| R746 | **answered** — §8 | , AND IT IS THE FIRST THING MY INSTRUCTIONS TELL ME TO CHECK.) THE REPORT'S Carried SECTION... |

### What each finding was, and where the answer lives

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R712 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R713 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R714 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R715 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R716 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R717 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R730 | carried | **answered** | §8 | `scripts/measure/member_forces_table.py` | carried from an earlier verdict |
| R731 | carried | **answered** | §8 | `` | carried from an earlier verdict |
| R732 | carried | **answered** | §8 | `` | carried from an earlier verdict |
| R734 | carried | **answered** | §3 | `scripts/measure/member_forces_table.py` | carried from an earlier verdict |
| R735 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R736 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R737 | carried | **answered** | §6 | `floatfea/hsp_pin.py` | carried from an earlier verdict |
| R738 | carried | **open** | §8 | `` | carried from an earlier verdict |
| R739 | recorded | **answered** | §4 | `scripts/measure/member_forces_table.py` | AS AMENDED BY EZ0, AND ALSO (a) ON THE UNAMENDED HEAD, BECAUSE THE |
| R740 | recorded | **answered** | §4 | `scripts/measure/api_wsd_utilisation.py` | UNDER EZ0.) `U = 1.815` IS THE PER-COMPONENT ENVELOPE BOUND, THE |
| R741 | recorded | **answered** | §2 | `floatfea/checks/api_wsd.py` | , AND THE LOCKED PLAN REQUIRES IT IN ITS OWN WORDS.) Â§ 3.2.2's |
| R742 | recorded | **answered** | §2 | `floatfea/checks/api_wsd.py` | .) `allowable_bending` RETURNS MORE THAN `0.75 F_y`, WHICH NO READING |
| R743 | recorded | **answered** | §5 | `floatfea/checks/api_wsd.py` | .) `CM_NO_TRANSVERSE_LOAD = 0.85` IS DECLARED UNDER THE WRONG CLAUSE |
| R744 | recorded | **answered** | §3 | `scripts/measure/member_forces_table.py` | ASSERTION DOMAIN BLINDNESS, AND IT IS THE CONTROL THAT ANSWERED |
| R745 | recorded | **answered** | §7 | `` | .) 43 RED TESTS AT THE REVIEWED COMMIT AND A RED CI JOB, AND THE |
| R746 | recorded | **answered** | §8 | `` | , AND IT IS THE FIRST THING MY INSTRUCTIONS TELL ME TO CHECK.) THE |

No row points at this section: every item is in this table by construction, so a pointer
here would resolve whatever it said (R318). § 8 is where the carried items are discussed and
§ 7 is where R745 is.
