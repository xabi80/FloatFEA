# F3 step 1 — the platform superstructure

Answers: verdict 73 @ 52de940

**2026-09-30.**

F2 step 7 closed at verdict 73 carrying four items by name. This step opens with them,
and this is its first revision — the generated tables arrive with revision 2, once a
verdict exists in this milestone's review tree for the generators to read.

## 1. The reading

**Schedule: F3 13 October, F4 19 October, the member-force table 23 October, the
code-check screen 28 October — unchanged.** The 6–8 October figure was withdrawn last
round and is not reinstated. **All four carried items are answered** and the step
opens with nothing blocking: R599 first, for a green suite, then R596, R597 and R598
site by site, then the closure list, then this report and the marker move.

**DZ7c is recorded in the plan so the next escalation does not cost a round:** if this
step closes carrying, the answer is *reduce scope, do not slip* — carried items that
cannot change member forces or the G4.1 equilibrium check are ledgered; items that can
keep blocking, at F4's G4.1.

## 2. R596 — the gate was circular, and I published the signature of that as precision

```
claim  the platform's inertia comparison was `deck == deck`, by construction
cmd    the assembled tensor against the deck's, component by component
out    [0][0] +3.12500000000000000e+09 vs +3.12500000000000000e+09  identical: True
out    [1][1] +3.12500000000000000e+09 vs +3.12500000000000000e+09  identical: True
out    [2][2] +6.25000000000000000e+09 vs +6.25000000000000000e+09  identical: True
out    off-diagonals ~1e-26 against an exact 0
judge  the DIAGONAL -- the part carrying the physics -- differed by exactly nothing.
       The builder set `remainder = deck - member - parallel` and the gate added the
       same two terms back, from the same matrix.
```

**ERRATUM (DZ1d).** Revision 7 of `docs/reports/F2/step-7.md` published
`3.375e-36` as the platform's inertia residual and read it as an accuracy result. It
is withdrawn. `numpy.spacing(6.25e9) = 9.5367e-07`, so that figure is thirty orders
of magnitude below one bit of the quantity being differenced: it was the maximum over
the whole tensor normalised by `6.25e9`, and it came entirely from round-off on the
off-diagonal **zeros** while the diagonal was algebraically identical. A residual that
small is evidence that nothing was compared. **From now a residual below one ULP of
its scale is reported as `≤ 1 ULP`, never as a number.**

### What replaces it: an independent path (DZ1)

`analytic_properties` computes mass, CoG and inertia from node coordinates, the line
mass and the section. It never touches the assembled matrix, and it reads the
remainder off the model's lumped-mass input rather than recomputing it.

The rotary terms are **cited, not assumed**. `floatfea/element/beam.py:332-336,351`
says the torsional rotary inertia is `rho (I_y + I_z)` — the polar second moment — and
not `rho J`, with its reason; `bending_mass` carries `rho I`. So a member contributes,
about its own centre,

    J = m (L²/12) (1 − eeᵀ) + ρ_eq L [ J_p eeᵀ + I (1 − eeᵀ) ],   J_p = I_y + I_z

**If the element ever omits one of these, the residual is a finding and the reference
is not tuned to match.**

```
rule   (A) analytic == assembled, (B) analytic == deck, both at MASS_PROPERTY_AGREEMENT,
       mass normalised by M_b, CoG by l_b, inertia by M_b l_b^2 (DZ1c)
out    body       (A) mass     (A) CoG   (A) inertia   (B) inertia
out    platform  0.000e+00   3.648e-18     1.522e-18     1.522e-18
out    hub1      0.000e+00   1.421e-16     6.358e-17     6.358e-17
out    hub2      1.552e-16   1.421e-16     1.272e-16     6.358e-17
out    hub3      0.000e+00   1.421e-16     6.358e-17     6.358e-17
out    hub4      1.552e-16   1.421e-16     6.358e-17     6.358e-17
judge  worst 1.5522e-16 at hub2's mass, against a floor of 1e-13 -- 644x of headroom
```

## 3. DZ6 — four mutations, each with the code line, the red, and the restore

```
baseline  48 passed

(i) the element ROTARY-MASS term scaled -> (A) reddens
    file  floatfea/element/beam.py
    -     rho_ip_l = rho * (section.I_y + section.I_z) * ll
    +     rho_ip_l = rho * (section.I_y + section.I_z) * ll * 2.0
    out   10 failed, 38 passed
    out   AssertionError: platform: the analytic inertia and the assembled one
          disagree by 4.230312e+05 kg.m^2
    restored  48 passed

(ii) a member TIP moved +3 m -> DZ2 reddens
    file  floatfea/model/platform.py
    -     b = node(end, f"{label}_tip")
    +     b = node((end[0] + 3.0, end[1], end[2]), f"{label}_tip")
    out   20 failed, 28 passed
    restored  48 passed

(iii) a DUPLICATED member, COUNT PRESERVED -> DZ2 reddens
    file  floatfea/model/platform.py
    -     total_length = sum(m.length for m in members)
    +     members[-1] = <a copy of members[0]'s endpoints, keeping its own label>
    out   5 failed, 43 passed
    out   AssertionError: platform has duplicate members: 4 members occupy 3 distinct
          endpoint pairs, so at least one line is drawn twice and its mass is counted
          twice
    restored  48 passed

(iv) a 180x WALL error -> the section gate reddens
    file  floatfea/model/platform.py
    -     ARM_WALL: Final[float] = 0.180
    +     ARM_WALL: Final[float] = 0.001
    out   5 failed, 43 passed
    out   AssertionError: the builder uses t = 0.001; F1:389 records 0.18 m
    restored  48 passed
```

**The previous round's cell hit a docstring and measured nothing.** These mutate the
code line and each shows its diff, which is what DZ6 asked for.

## 4. R597 — the geometry was not gated at all

The reviewer measured four tips moved +3 m and four of sixteen members duplicated,
both **1765 passed**. A dropped member was caught by the count alone — a detection the
pre-DY1 CoG test had and my rewrite lost. DZ2 asserts the member count, the undirected
endpoint-pair set against the **deck's own** joint coordinates, no duplicate pairs,
and that each body is a star from its centre. Cells (ii) and (iii) above are the
evidence.

## 5. R598 — a phantom counter and two wrong figures

The entry cited `test_G3_1a_a_MISPLACED_remainder_reddens`. `git grep` found that name
in exactly one place: the comment itself. **I named a test I never wrote, in the file
whose purpose is that a value is not taken on trust.** It is deleted and replaced by a
pointer to §3 above, per DZ3 — demonstrations live in the report.

And the entry's own figures were wrong. It claimed a worst residual of `2.2119e-15`
and ~45× headroom; that divided a CoG offset by `1.0 m` instead of the body's extent.
Under `l_b` normalisation the worst at this commit is **`1.5522e-16`**, giving 644×.
The directive's correction, `1.9073e-16`, was measured against the pre-DZ1 gate; the
figure above is re-measured here, on the path that replaced it.

**`MASS_PROPERTY_AGREEMENT = 1e-13` is unchanged**, set from `36·eps = 7.993606e-15`
rather than from any measurement.

## 6. R599 — a guard that failed false, deleted rather than extended

The `named` whitelist required the nested failure to arrive through one of eleven
listed test names. The planted defect was detected three times over, by reporters that
name the commit and the file, and the assertion's message was false about those
states. **The list was unsound in both directions** — an unlisted reporter gives a
false red, a listed one firing for an unrelated reason gives a false green, which is
R516 recorded three lines below it. Adding a name had been the repair three times.
Deleted; `assert code != 0` and `_assert_diagnosis` are kept.

## 7. DZ5 — the deck's body inertias are physically inconsistent

**Report only. The FE keeps FloatSim's values, because inertia-relief equilibrium with
FloatSim's loads requires it.**

```
claim  the platform's deck inertia is M * 50^2 * (1, 1, 2) exactly
out    np.diag(J_G) = [3.125e+09 3.125e+09 6.250e+09]; M*2500*(1,1,2) identical: True
rule   a rigid body's principal moments satisfy I_i + I_j >= I_k

out    body        M t    k_z m   extent m   deck J_G slack     J_r slack
out    platform 1250.0   70.711     51.056       0.0000e+00   -2.6770e+08
out    hub1     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
out    hub2     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
out    hub3     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
out    hub4     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
judge  every body's J_G is planar at G -- the lamina identity, slack exactly zero --
       which no real three-dimensional body satisfies, and the buoys in the same deck
       do not. The platform's radius of gyration about z is 70.711 m against 50 m arms
       and a 51.056 m extent: the mass gyrates beyond the structure carrying it.
judge  J_r is PSD for every body and violates the triangle inequality for every body.
       The directive predicted about -2.67e8 for the platform; it is -2.6770e+08. The
       hubs were not predicted and are -1.0153e+06 each.

cmd    grep -rn "Inertia(Ixx=10.0\|Inertia(Ixx=0.5" ../HSP-stable/studies/platform-12buoy/
out    platform_common.py:159   inertia=Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)
out    platform_common.py:178   inertia=Inertia(Ixx=10.0, Iyy=10.0, Izz=20.0)
out    platform_rao_pilot.py:172 and :191 carry the same two literals
judge  typed into the study, not derived. HSP's `docs/platform-geometry.md:46` flags
       the hub value as Q2.
```

**The results label now reads** `buoy spar columns not assessed as members; buoy loads
applied as joint reactions; platform mass properties as in FloatSim; see DZ5 finding`,
and the assumptions block carries the figures. Xabier decides on FloatSim.

## 8. Corrections to the previous report (C33, C36, C37)

**C36 — the DY7 symmetry pairing was wrong.** I wrote that joints 5/15, 6/14 and 7/13
mirror. They do not: the pairs are **(5, 13), (6, 15), (7, 14)**. The reviewer
re-measured and got my exact figures for joints 2 and 3, so the observation that the
reactions are symmetric stands; the pairing I published for it does not.

**C37 — the command row did not produce the output row.** It read `--duration 30.0`
while the printed snapshot was at the script's default. The command is stated with its
arguments in §9.

**C33 — the whole-suite figure was two commits early**, published before the commits
it described. The line in §10 is taken at this report's own commit.

**C38 and C39, found in the same reading, were code and are fixed** (`3621b35`):
`range(12)` is not the twelve buoy joints — the joint order interleaves three buoy
joints with a hub-platform joint, so it took in joints 3, 7 and 11 and left out
buoy10–12 — and the buoy weight was typed rather than read from the deck. **The
published `0.6581 N` and `2.34e-03` do not move**; what is fixed is a latent error.

## 9. DY7 — the joint reactions, restated with the command that produced them

```
cmd    python scripts/report_joint_reactions.py --period 10.0 --duration 30.0
out    6 case files, 21 columns; columns naming a multiplier, reaction or joint: 0
out    buoys represented: 3 of 12 -- ['buoy1', 'buoy4', 'buoy7']
out    16 joints x 4 rows = 64 multipliers, read from res.lam
out    the largest buoy-joint Fz is 0.6581 N against a buoy weight of
       28.67 * 9.81 = 281.3 N, a ratio of 2.34e-03
rule   the study builds with `solve_equilibrium=False` and `xi` is displacement from
       the reference, so `lam` is the reaction ABOUT the equilibrium state
judge  a member-force table built from these alone would understate every arm by three
       orders of magnitude. F4's export must carry the equilibrium reaction as well as
       the history, and it is an ADDITIVE writer on the HSP side rather than a
       reconstruction.
```

The equilibrium identity does not close from what is exported: the inertia term is the
Cummins operator, and neither the per-body added mass nor the memory state is in the
file. That is DX1's gap one level deeper, and the script prints `|R + A|` labelled as
the part that is available rather than a residual that would look like the answer.

## 10. The whole suite

**Whole suite at `9cba81c`: 2628 passed, 0 failed, 0 skipped.** **The excluded set: 309 passed, 1 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 310 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]`
```

**Zero failed and zero skipped in the main set.** The excluded set is one, down from
two: `test_the_answered_verdict_is_the_NEWEST_one` through the nested harness, which is
the ordinary interval red while this report waits for the verdict that judges it. The
other one cleared when R599's whitelist went.

**THE STEP MARKER MOVES IN THIS COMMIT (DY8c), and the consequence is stated rather
than discovered.** `REPORTS` and `REVIEWS` follow the plan carrying
`<!-- step-under-execution -->` since DX2, so from this commit they resolve to
`docs/reports/F3` and `docs/reviews/F3`. **There is no verdict in that tree yet** --
`scripts/write_verdict.py` refuses a step with no report, so this report has to exist
before the reviewer can write one. The report-parametrised guards are therefore red
between this commit and that verdict, and the generated tables arrive with revision 2.
The forced order is the reviewer's own: report and marker first, verdict second.


# Revision 2 — verdict 74's two findings

Answers: verdict 74 @ 8ac9ce8

**2026-09-30.**

## 0. CI, for the commit under review

## 0. CI at `228bdfb`, the commit verdict 74 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 74 at `228bdfb` through the report's own `Answers:` line. Run `36743792702`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 835 | 37 | 0 |
| the verification ladder | 1816 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 35.**

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
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_diff_the_site_check_needs_is_available` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_reports_ahead_of_the_newest_verdict]` (lint, unit and guards)
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
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_a_report_commit_messaged_docs_that_also_edits_the_guards_measuring_it]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

## 0a. Runs since the commit verdict 74 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 74 at `228bdfb` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `36743792702` | push | `228bdfb` | conclusion **failure** |
| `36743819045` | workflow_dispatch | `228bdfb` | conclusion **failure** |

**Run `36743792702`, conclusion **failure**: 35 failing test name(s) in the log.**
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
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_diff_the_site_check_needs_is_available` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_reports_ahead_of_the_newest_verdict]` (lint, unit and guards)
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
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_a_report_commit_messaged_docs_that_also_edits_the_guards_measuring_it]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

**Run `36743819045`, conclusion **failure**: 35 failing test name(s) in the log.**
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
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_diff_the_site_check_needs_is_available` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_reports_ahead_of_the_newest_verdict]` (lint, unit and guards)
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
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_a_report_commit_messaged_docs_that_also_edits_the_guards_measuring_it]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]` (lint, unit and guards)

## 1. The reading

**Schedule unchanged: F3 13 October, F4 19 October, the member-force table 23 October,
the code-check screen 28 October.** Both findings are answered. **R600 is the third
round running in which I shipped a gate that compares something with itself**, and the
third in which the cell I published appeared to prove otherwise — R590 was the mass,
R596 the inertia, R600 the geometry. The pattern is not that these comparisons are
hard. It is that I build the expected side out of whatever is nearest, and what is
nearest is the thing under test.

```
claim  the geometry gate was blind to every geometric defect the reviewer tried
out    every tip +3 m, the plan centre +3 m, all coordinates x1.02, the arm labels
       permuted, the frame rotated 30 degrees -- all 48 passed
judge  `expected_pairs` read `body.model.nodes[...]` for both sides. Its docstring
       said "from the DECK's joints"; `BodyModel` carried no deck coordinate, so it
       could not have read one.

claim  the gate reads the deck now, and each mutation reddens
cmd    ONE VARIABLE each, baseline 52 passed
out    every tip +3 m, the node moved WITH the length   -> 5 failed
out    the plan centre moved to (3, 0, z)               -> 1 failed, and it is DZ2
out    every in-plane coordinate x1.02, a typed radius  -> 1 failed, and it is DZ2
out    the arm labels permuted onto each other's joints -> 4 failed
out    restored                                          -> 52 passed
rule   the expected set comes from `deck_joint_points` and `deck_joint_owner`, both
       filled from the deck and untouchable by the model construction
```

**And my previous cell (ii) was mis-attributed**, which the reviewer caught and I
reproduced: the edit sat *after* `length = math.dist(start, end)`, so what reddened
was `member.length` disagreeing with the coordinates, not the geometry. The table
above moves the tip before the node is built, which is the honest form.

**The label permutation needed its own assertion and it is the one that matters
most.** A permutation leaves the endpoint-pair set unchanged — the frame really does
join the same points — so the pair check passes and should. What it corrupts is which
buoy each node belongs to, and `buoy_joint_nodes` is keyed off those labels. **F4
applies each buoy's gimbal reaction through that map**, so a permutation would put
buoy1's reaction at buoy2's node and every member force downstream would be wrong in
silence.

**R601(a) was C40's shape, and C40 was ledgered rather than fixed on a reading that
the marker move falsified.** The harness hardcoded `docs/milestones/F2.md`; the marker
moving made the regex miss, `_step()` returned 0, and all twenty-four states died on
`FileNotFoundError` before planting anything — 24 of the 37 reds. It reads the active
plan now, the same way `test_report_carried.py` has since DX2.

## 2. The measurement the reviewer added, and what it settles

**DZ5's slack against `f`, one variable**, which DZ5 did not ask for and which is the
most useful thing in the round after R600:

```
out    f      0.5          0.4          0.3          0.2          0.1          0
out    slack  -2.6770e+08  -1.7858e+08  -1.1487e+08  -6.7051e+07  -2.9819e+07  0.0
rule   a rigid body's principal moments satisfy I_i + I_j >= I_k
judge  THE SPLIT DOES NOT CREATE THE VIOLATION, IT INHERITS IT. The deck's J_G sits
       exactly ON the lamina boundary -- slack 0.0000e+00 -- so any mass moved off
       the plane pushes it over, the slack is linear in `f`, and no admissible `f`
       removes it. f = 0 is the only value with zero slack and it is the value that
       puts no mass on the members at all.
judge  `admissible()` is True at every `f`, so DY0d's ladder never descends: it tests
       PSD, which is a weaker condition than realisability. That is a real gap in
       DY0d and it is recorded rather than patched, because changing what `admissible`
       means is a decision about the model, not a repair.
```

## 3. Findings

Generated: `python scripts/answered_table.py <the newest verdict> <the answers file>`.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R600 | recorded | **answered** | §1 | `tests/verification/rung3/test_platform_skeleton.py` | DZ2's geometry gate builds its expected endpoint-pair set from the |
| R601 | recorded | **answered** | §1 | `tests/test_report_guard_states.py` | CI is RED at the reviewed commit -- `37 failed, 835 passed` in |

## 4. Sites named by findings and not touched

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R600 | `CLAUDE.md` | the file is untouched | **no change.** Quoted as the rule the finding is measured against. The governing file is not edited to answer a finding it governs. |
| R600 | `floatfea/model/platform.py:551` | the file is touched and this line number is the old one | TOUCHED at `1c0785e`, and **no change at that exact line**: `Superstructure` now carries `deck_joint_points` and `deck_joint_owner`, so a gate has something to read that the model construction cannot influence. |
| R600 | `floatfea/model/platform.py:552` | the file is touched and this line number is the old one | TOUCHED at `1c0785e`, and **no change at that exact line**: `Superstructure` now carries `deck_joint_points` and `deck_joint_owner`, so a gate has something to read that the model construction cannot influence. |
| R600 | `floatfea/model/platform.py:553` | the file is touched and this line number is the old one | TOUCHED at `1c0785e`, and **no change at that exact line**: `Superstructure` now carries `deck_joint_points` and `deck_joint_owner`, so a gate has something to read that the model construction cannot influence. |
| R600 | `platform.py:551` | the file is touched and this line number is the old one | **no change** -- the same site as above, cited by bare name in the verdict's prose. See the `floatfea/model/platform.py` row. |
| R600 | `platform.py:552` | the file is touched and this line number is the old one | **no change** -- the same site as above, cited by bare name in the verdict's prose. See the `floatfea/model/platform.py` row. |
| R600 | `platform.py:553` | the file is touched and this line number is the old one | **no change** -- the same site as above, cited by bare name in the verdict's prose. See the `floatfea/model/platform.py` row. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:326` | the file is touched and this line number is the old one | TOUCHED at `8df625a`, and **no change at that exact line**: `expected_pairs` reads the deck rather than the model, and a new assertion ties each buoy to the node the deck puts it at -- which is what the label permutation reddens. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:334` | the file is touched and this line number is the old one | TOUCHED at `8df625a`, and **no change at that exact line**: `expected_pairs` reads the deck rather than the model, and a new assertion ties each buoy to the node the deck puts it at -- which is what the label permutation reddens. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:335` | the file is touched and this line number is the old one | TOUCHED at `8df625a`, and **no change at that exact line**: `expected_pairs` reads the deck rather than the model, and a new assertion ties each buoy to the node the deck puts it at -- which is what the label permutation reddens. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:339` | the file is touched and this line number is the old one | TOUCHED at `8df625a`, and **no change at that exact line**: `expected_pairs` reads the deck rather than the model, and a new assertion ties each buoy to the node the deck puts it at -- which is what the label permutation reddens. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:340` | the file is touched and this line number is the old one | TOUCHED at `8df625a`, and **no change at that exact line**: `expected_pairs` reads the deck rather than the model, and a new assertion ties each buoy to the node the deck puts it at -- which is what the label permutation reddens. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:343` | the file is touched and this line number is the old one | TOUCHED at `8df625a`, and **no change at that exact line**: `expected_pairs` reads the deck rather than the model, and a new assertion ties each buoy to the node the deck puts it at -- which is what the label permutation reddens. |
| R601 | `F2.md` | the file is untouched | **no change, and deliberately.** The marker is GONE from it, which is the whole point of DY8c: exactly one plan carries `<!-- step-under-execution -->` and F2 is closed. What was wrong was four files reading this path regardless. |
| R601 | `docs/reports/F2/step-0.md` | the file is untouched | **no change -- this file has never existed.** It is the path the broken harness constructed when `_step()` returned 0, and the `FileNotFoundError` it raised is the symptom the finding names, not a file to create. |
| R601 | `test_report_carried.py` | the file is untouched | **no change** -- cited by bare name as the file DX2 already fixed, and it is the template the other three now follow. See the `tests/test_report_carried.py` row. |
| R601 | `tests/test_plan_matches_tolerances.py:34` | the file is untouched | **no change, and it is the one of the four still hardcoded.** It does not fail false: it reads `docs/milestones/F2.md` for the tolerance TABLE, which is a real file that really holds the table, so nothing breaks. The reviewer ruled leave it and I ledgered it as C40; the F3 tolerance sitting in a closed milestone's table is the visible cost and the heading says so. |
| R601 | `tests/test_report_carried.py` | the file is untouched | **no change.** DX2 re-pointed it at the plan carrying the step marker, so it followed the marker to F3 without an edit -- which is why it is the only one of the four that did not break. |

## 5. Carried

Generated: `python scripts/carried_table.py <the newest verdict> <the answers file>`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R596 | **open** — carried from an earlier verdict | and R599 are closed. Closure items C12, C14, C18 to C32, the open |
| R598 | **open** — carried from an earlier verdict | and R599 are closed. Closure items C12, C14, C18 to C32, the open |
| R599 | **open** — carried from an earlier verdict | are closed. Closure items C12, C14, C18 to C32, the open |
| R600 | **answered** — §1 | DZ2's geometry gate builds its expected endpoint-pair set from the BUILT MODEL, not from the... |
| R601 | **answered** — §1 | CI is RED at the reviewed commit -- 37 failed, 835 passed in lint, unit and guards -- and it... |

## 6. The whole suite

**Whole suite at `8df625a`: 2632 passed, 0 failed, 0 skipped.** **The excluded set: 136 passed, 47 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 183 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_parse_found_something_to_check`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R596]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R598]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R599]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R600]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R601]`
- **failed, in the excluded set** `tests.test_report_carried::test_a_report_does_not_say_CLOSED`
- **failed, in the excluded set** `tests.test_report_carried::test_the_Carried_table_is_what_the_generator_produces`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_carried::test_there_are_pointers_to_resolve`
- **failed, in the excluded set** `tests.test_report_carried::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_a_CI_SECTION`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`
- **failed, in the excluded set** `tests.test_report_carried::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_section_is_about_the_REVIEWED_commit`
- **failed, in the excluded set** `tests.test_report_carried::test_the_reported_CI_counts_are_not_all_zero`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-CLAUDE.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-docs/reports/F3/step-1.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-floatfea/model/platform.py:551]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-floatfea/model/platform.py:552]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-floatfea/model/platform.py:553]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-platform.py:551]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-platform.py:552]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-platform.py:553]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-tests/verification/rung3/test_platform_skeleton.py:326]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-tests/verification/rung3/test_platform_skeleton.py:334]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-tests/verification/rung3/test_platform_skeleton.py:335]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-tests/verification/rung3/test_platform_skeleton.py:339]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-tests/verification/rung3/test_platform_skeleton.py:340]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R600-tests/verification/rung3/test_platform_skeleton.py:343]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R601-F2.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R601-docs/reports/F2/step-0.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R601-test_report_carried.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R601-tests/test_plan_matches_tolerances.py:34]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R601-tests/test_report_carried.py]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]`
```

**Zero failed and zero skipped in the MAIN set.** The excluded set is 47, and every
one is the interval state this revision closes: the line is taken at `8df625a`, where
the report still answered verdict 73 while verdict 74 existed, so
`_verdict_text_at("52de940")` found no F3 verdict at that sha and fell back to the
working copy — comparing a report against a verdict it predates. The reviewer predicted
that exact number's cause in its hand-back.

**AND A FOURTH FILE WAS FOUND HARDCODED TO `F2` WHILE BUILDING THIS REVISION.**
`scripts/ci_section.py` carried the milestone in FOUR places — the plan path, the report
path, the reviews directory and the verdict path used by `git show` — and each had to be
found by the generator failing differently:

```
cmd    python scripts/ci_section.py, four times, after each repair
out    F2.md carries no `<!-- step-under-execution: N -->` line
out    the newest revision of the report has no `Answers: verdict N @ <sha>` line
out    the verdict file cannot be read at that commit
out    ## 0. CI at `228bdfb`, the commit verdict 74 judged -- conclusion FAILURE
judge  a hardcoded milestone is not one constant; it is however many the file has. That
       makes five files in the family: `test_report_carried.py` (DX2),
       `test_plan_matches_tolerances.py` and `test_report_guard_states.py` (C40, R601a),
       and this one. C40 ledgered the pattern on the reading that none failed false;
       the marker move falsified that for three of them within one commit.
```
