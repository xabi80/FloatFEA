# R2 step 0 — closure

**Closed by verdict 65 (PASS) at `0fb8c93`, with one blocking item carried.** Step 0 was
GI3's measure-only step: five measurements, one permitted code change, and GI6's
instruction to report and stop. It consumed all three ES0 revisions and **six** reviewer
rounds -- three interim checks, which count against none, plus three reviewed revisions --
and then two further reviews of the closure commit itself under EQ0, which cost no round
either. **This sentence read "five" and 3 + 3 is six** (R1252).

## What was built

GI3's five items, all answered in `docs/reports/R2/step-0.md`:

* **(a)** the inertial/joint-reaction split, and the loop gain it implies. At the body the
  split is 1:1 by construction; at the governing member the stress is 59.2 % static /
  40.8 % dynamic. Loop gain `g = k·m_steel/m_body` is 0.53–0.77, so the loop converges
  **monotonically**. **The group matters and this line dropped it:** the PLATFORM needs
  11–14 iterations to reach D3's 0.5 % band; each HUB needs 5.7–9.0. Published without
  the group it reads as a whole-model figure, and it errs on the slow side rather than the
  safe one.
* **(b)** one D4 iteration is **25 min 56 s** with threads pinned. D3's cap of 8 is ≈ 3.5 h.
* **(c)** the in-memory mass/inertia override already exists and HSP's deck builder takes
  **no file input at all**, so the returned Deck object is the only override point and
  **GI3(c) raises no escalation**.
* **(d)** only the 12 buoys carry buoyancy; the five bodies R2 resizes have no draft of
  their own. The system gets **lighter** on iteration one, so ballast is **added**.
* **(e)** the two-key worktree resolver, seven assignments across six files, with tests.

## Which gates pass, AND AT WHICH COMMIT

**R1249: the table that stood here published five rows as green, and two were red at the
commit publishing them.** One of those two was red *about R1243* -- the step's only open
blocking item, which is to say the one thing the carry mechanism exists to stop anyone
dropping. The rows now carry their own operating point, because a gate result without one
is a figure whose rule can move underneath it (BP0), and `docs/closure/**` sits outside
every prose guard in this repository, so nothing would have said so.

**AND ONE OF THE TWO WAS WORSE THAN STALE, WHICH I HAD UNDERSTATED.** The row read
`468 + 24 passed`, and `pytest --collect-only` gives **468 and 24 at that commit** -- so
the figure was the COLLECTED ID COUNT PUBLISHED AS A PASS COUNT. A number taken that way
is green by construction whatever the suite does; the actual result there was 484 passed,
8 failed. The other row was true at the previous commit and voided by the next, which is
ordinary staleness. These are different defects and lumping them together would have lost
the one that cannot fail.

<!-- cz1-closure-outputs -->
**CZ1 (ii)-(iv) at `ce5a84f`, the previous closure commit, with the tree clean.** These are
the outputs CZ1 owes and that `e71ecd5` put in a commit message instead -- which R1250 is
the mechanical reason for: this artifact was invisible to the router, and the report is
sealed by EK3, so there was nowhere legal left.

```
cmd    ruff check floatfea tests
out    All checks passed!
cmd    black --check floatfea tests
out    129 files would be left unchanged
cmd    mypy floatfea
out    Success: no issues found in 45 source files
cmd    pytest -q
out    10 failed, 4456 passed, 2 warnings in 3552.86s
```

**Whole suite at `ce5a84f`: 4456 passed, 10 failed, 0 skipped.**

*Generated, and generated AFTER every run of the round concluded, which is R1237's
ordering. The hand-written one-row table that stood here would have been the same
defect a third time.*

## 0a. Runs since the commit verdict 64 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 64 at `e87b2c0` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that reached no conclusion ABOUT THE CODE -- cancelled, or still running -- has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it. A cancelled run IS `completed`, which is why the test is the conclusion and not the status (CX0, R449, R1130).

| run | event | head | outcome |
|---|---|---|---|
| `44164723945` | push | `a3a30d2` | conclusion **failure** |
| `44180156206` | push | `772f616` | conclusion **failure** |
| `44186415061` | push | `e511161` | conclusion **failure** |
| `44187721362` | push | `e71ecd5` | conclusion **failure** |
| `44196001239` | push | `ce5a84f` | conclusion **failure** |
| `44205027019` | push | `3e34953` | conclusion **failure** |

**Run `44164723945`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` (the verification ladder)

**Run `44180156206`, conclusion **failure**: 18 failing test name(s) in the log.**
- `tests/test_ci_determinism_gate.py::test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:387]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:388]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:389]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:390]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1242-tests/test_report_carried.py:387]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1242-tests/test_report_carried.py:388]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1242-tests/test_report_carried.py:389]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1242-tests/test_report_carried.py:390]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[19. R1239, R1240, R1241, R1242]` (lint, unit and guards)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` (the verification ladder)

**Run `44186415061`, conclusion **failure**: 2 failing test name(s) in the log.**
- `tests/test_ci_determinism_gate.py::test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8` (lint, unit and guards)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` (the verification ladder)

**Run `44187721362`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` (the verification ladder)

**Run `44196001239`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` (the verification ladder)

**Run `44205027019`, conclusion **failure**: 1 failing test name(s) in the log.**
- `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` (the verification ladder)

**The ten, traced per id and not by family (EG3 i), because two of them are not the
escalation and saying "ten reds, two are the escalation" would be the cascade EG3 forbids:**

- **failed** `tests.verification.rung4.test_f4_g41_dynamic::test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` -- the FQ3 escalation
- **failed** `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` -- downstream of it (R1223)
- **failed** `tests.test_report_carried::test_the_answered_verdict_is_the_NEWEST_one` -- EK3's timing guard: `ce5a84f` touches a report sealed at its final verdict and no newer verdict existed yet. Cleared at verdict 66, measured.
- **failed** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]` -- the outer harness reporting the id above; four occurrences in its own output
- **failed** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]` -- the outer harness reporting the id above; four occurrences in its own output
- **failed** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]` -- the outer harness reporting the id above; four occurrences in its own output
- **failed** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` -- the outer harness reporting the id above; four occurrences in its own output
- **failed** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]` -- the outer harness reporting the id above; four occurrences in its own output
- **failed** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` -- the outer harness reporting the id above; four occurrences in its own output
- **failed** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]` -- the outer harness reporting the id above; four occurrences in its own output

**EVERY ONE IS NAMED WITH ITS NODE ID AND THAT IS NOT COSMETIC.** This block first wrote
the seven planted states as `seven x test_the_guard_survives_the_state[...]` with the
parameters in one line -- **a cascade collapsed by family, in a paragraph claiming to
trace per id.** `test_a_RED_suite_is_named_in_the_report` caught it: *"the whole-suite line
reports 10 failing tests and the report names 2."* EG3 (i) exists because eight planted
states were once ruled as one cascade and the eighth was a real defect (R629), and the
collapsed form is precisely the shape that hid it.

**Two of those ten were green at the commit BEFORE and red here, and that is the finding
R1249 is about rather than a detail**: reverting the report to satisfy EK3 removed R1243's
only mention, which turned `check_carried` red about the step's one open blocking item.
<!-- /cz1-closure-outputs -->

## Carried out of step 0

*`scripts/check_carried.py` and `tests/test_report_carried.py` both read this section once
the step is closed, because EK3 seals the report and the artifact is the only place a
closed step's list can still gain a row (R1250).*

| item | state | where it goes |
|---|---|---|
| R1243 | **open, blocking** | **step 1.** R1239's observation stands -- chaining rungs in one job hides every rung after a red one whichever order they sit in -- and its repair does not. The fix is to stop the chaining: separate jobs, or `if: always()` per step, with a CI section that names skipped STEPS. CH3's order is restored meanwhile and the gate is green |
| R1223, R1225 | **open, escalated** | **Xabier.** One item: the committed npz does not regenerate from this tree, FQ3 ruled the case in advance, and the deliverable red is downstream of the same cause |
| R1232 | open | **the write run**, not this step: `pin_threads()` cannot be called below the module's own numpy import, so the environment is recorded in the provenance and not held |
| R1248 | open | **step 2.** `scripts/export_buoy_centers_ref.py` checks the stable tree's NAME and never its TAG |
| R1249, R1250 | **answered in this commit** | the table above, and the router in both of its readers |
| R1251, R1252, R1253, R1254, R1255 | ledger | figure and needle corrections in this artifact, below |
| R1244, R1245, R1246, R1247 | answered | in this artifact, above |
| R1212, R1217, R1218, R1222, R1224, R1234, R1242 | reviewer-side or ledger | carried as the verdict routed them; none is a step-0 matter |
| R1205, R1206, R1207, R1208 | answered in revision 1 | `docs/reports/R2/step-0.md` §6 -- the marker, exit (iii), step 2's gates, the two keys |
| R1213, R1214, R1215, R1226, R1227, R1229 | answered in revision 1 | §6a -- the DS0 name test, the set-and-wrong refusal, the marker comment, the stable-key refusal, the STEP condition, the vacuous assertion |
| R1221, R1228, R1233, R1235, R1236 | answered in revision 2 | §6a and §7 -- the mention filter at both sites, the regenerated quotation, the narrowed magnitude sentence, the two stale figures |
| R1230, R1231, R1237, R1238, R1240, R1241 | answered in revision 3 | §11, §13, §14, §17, §18, §19 -- the header naming the newest verdict, the three generated sections, the rounds table, the red list, the oldest-round scoping, the two refuted sentences |
| R1186, R1188, R1189, R1190, R1191, R1193, R1196, R1197, R1198, R1199, R1200, R1201, R1203, R1204, R835 | open, from verdict 58 | **step 1.** None is a step-0 matter; R1188 and R1193 are discharged from the reviewer's side |

## R1245 and R1246 -- two closure items with nowhere to go but here (EK3)

**R1245 -- the R1240 gain is FOUR items, not five, and the correction exists in no file
until this one.** `docs/reports/R2/step-0.md:1629` and `step-0-answers.json` both read
*"R1212, R1217, R1218, R1219, R1224 -- five items"*. Measured: `R1219 in EXPECTED` is
`False` (35 ids), and it has no row in §19b. **It is four.** The figure was wrong in
verdict 64 and I restated it without checking it against `EXPECTED` itself, which is the
same failure as every other restated figure in this step.

The correction was made in `e71ecd5` **and the byte-for-byte restore in `ce5a84f` reverted
it** -- `git show e71ecd5:docs/reports/R2/step-0.md | grep -c "four items"` is `0`, so it
never existed in a file at all. It lived in a commit message, which no guard and no reader
of the record reads.

**R1246 -- the same thing happened to the `<!-- generated: scripts/untouched_sites.py -->`
marker.** It was at `e71ecd5` and is absent now, reverted by the same restore.

**AND THAT COLLISION IS THE REUSABLE PART.** EK3 seals a step report at its final verdict;
CZ0 requires the whole closure list fixed in the closure commit. **For any closure item
whose SITE is inside the closed report, those two instructions cannot both be obeyed** --
the repair must touch the report, and touching it is forbidden. The restore that satisfied
EK3 necessarily reverted every closure-item repair sited there. Both items now have only
this artifact as a home, and `docs/reports/R2/step-0.md:1616` and `:1629` are
**declare-only** from here: step 1's report records them `**no change** -- EK3`, which is
the one form of answer still available.

**`:1616` is the other one**: it still reads the refuted "ONE red to TWO" prediction, and
the verdict that asked for its replacement named a site inside the report it was closing.
The reviewer withdrew that half of its own condition for exactly this reason.

## What is escalated, and it is the substance of this step

**The committed `data/f4/dynamic_inputs.npz` does not regenerate from this tree.** numpy
and scipy sit off `requirements-lock.txt` (2.5.4 / 1.18.1 against 2.4.4 / 1.17.1), the
difference is round-off — ~197 eps relative to each array's own scale, on the one case
measured — and FQ3 already ruled this case in advance: *"if the golden moves under these
pins, STOP and report rather than re-baselining."* Two options, both costed in the
report's §7, and the choice is Xabier's.

**And GI's own D1 and GI5 step 2 (iii) contradict each other** — consistent only if
ballast is identically zero, and then D2's draft cannot be held when steel moves.

## What was deferred and why

* **R1243 — carried into step 1 by name and still blocking.** R1239's observation stands
  (chaining rungs in one job means a red rung hides every rung after it) and its repair
  does not. The fix is to stop the chaining — separate jobs, or `if: always()` per step,
  with a CI section that names skipped STEPS — which is apparatus work and not step 0's.
* **R1248 — carried to step 2.** `scripts/export_buoy_centers_ref.py` checks the stable
  tree's NAME and never its TAG, so a tree merely *named* `HSP-stable` regenerates EB6's
  input while the file declares the pinned tag. Documented rather than hidden, and the
  committed snapshot is untouched.
* **R1232** stands for the write run: `pin_threads()` cannot be called below the module's
  own numpy import, so the environment is **recorded** in the provenance and not held.
* **Rungs 4 and 5 are unmeasurable in CI while the escalation stands.** Rung 6 is red, so
  the rungs after it do not execute. Written down rather than fixed wrongly — which is
  exactly what R1243 was.

## R1243, and the two records the report must not carry (EK3)

**R1243 is the closure commit's first item (FF0) and it is a defect introduced while
repairing another.** R1239's observation was right -- CI had never measured rung 4 -- and
the repair chosen for it was wrong in a way the file already said.

```
claim  the rungs should run in the ladder's own order, and CI's ladder job would go from
       one red to two, the second being the escalation becoming visible
cmd    sed -n '496,503p' .github/workflows/ci.yml       (UNCHANGED by that diff)
out    "AND RUNG 6 RUNS BEFORE RUNG 4 (CH3). The goldens ask whether today's bytes equal
        yesterday's, which stays interpretable whatever ladder 4 says; chained behind it
        they were skipped for eleven rounds while running on ten determinism legs ...
        `tests/test_ci_determinism_gate.py` asserts that position."
cmd    pytest -q tests/test_ci_determinism_gate.py      (at the reordered commit)
out    1 failed, 12 passed -- test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8
cell   ONE VARIABLE, the step order, from the two runs rather than from reasoning:
         rungs 1,2,3,6   ladder row  2143 passed, 1 failed, 0 skipped
         rungs 1,2,3,4   ladder row  2011 passed, 1 failed, 0 skipped
       -477 (rung 6 AND the whole of tests/regression), +345 (rung 4), SAME `1 failed`
rule   CH3, and `tests/test_ci_determinism_gate.py`, which asserts the position
judge  **THE PREDICTION IS REFUTED BY ITS OWN COMMIT'S RUN: one red, not two.** Rung 4
       fails while the escalation stands, so rungs 5 AND 6 skip -- the very mechanism
       R1239 identified, applied to R1239's repair. The escalation did not become
       visible; it MOVED, from the rung-6 deliverable red to the rung-4 staleness red,
       and the rung-6 one went invisible, taking the whole of `tests/regression` out of
       CI with it -- which FV1 assigns to CI in so many words, and which holds
       `test_f6_deliverable_agrees_with_itself.py`, the only automated check that a
       published deliverable still regenerates.
       Nothing would have said so: `ci_section.py` reads a JOB's conclusion and parses
       `run_rung:` lines, and a skipped STEP emits no such line.
       **A general principle was appealed to over a specific, measured, gated ruling
       recorded TWENTY-FIVE lines from the edit** -- `ci.yml:528` against the edit, measured,
       and "eight" was wrong at every commit in play. The distance is not the point and
       getting it wrong twice in the same sentence is: a figure in `.github/` and one in
       `docs/closure/` are both outside `test_tree_prose_consistent.py`'s ROOTS, so
       nothing in the tree checks either. That is the whole error.
```

**Reverted; `tests/test_ci_determinism_gate.py` is green again (13 passed).** R1239's
observation stands and its repair does not: chaining rungs in one job hides every rung
after a red one whichever order they sit in, so the fix is to stop the chaining -- separate
jobs, or `if: always()` per step, with a CI section that names skipped STEPS. That is step
1's and **R1243 carries into it by name, still blocking.** Meanwhile R1239's second exit is
taken as the honest record: **rungs 4 and 5 are unmeasurable in CI while the escalation
stands.**

**R1244 -- revision 2's rounds table has a wrong row, and it is corrected HERE rather than
there.** The row for the run at `0c5c864` reads `**no result** (status in_progress)`; that
run concluded `failure` at 18:58:00Z, thirty minutes before the commit carrying the table
was written. That is R1237, and the report's §17 states the defect without naming the run
or the row. **The table is left as it shipped.** Silently rewriting a reviewed generated
record so it no longer shows what was published would remove the evidence of the finding.

**AND EK3 IS WHY THESE TWO SIT HERE AND NOT IN THE REPORT.** The closure commit first put
them into `docs/reports/R2/step-0.md`, which EK3 forbids -- *"a closure commit NEVER touches
a step report after that report's final verdict"* -- and the guard said so immediately:

```
cmd    pytest -q tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one
out    the report at `e71ecd5` is newer than the verdict at `e511161` and names `a3a30d2`.
       Written with the newest verdict available, it must answer that one.
rule   EK3, measured three ways in CLAUDE.md: "any commit that touches a closed report
       before a newer verdict exists reddens it"
judge  **FOURTH TIME IN THIS STEP THAT THE `Answers:` HEADER TRAILED THE NEWEST VERDICT**,
       and the first three were R1230, which this report answered two revisions ago. The
       report is restored byte-for-byte to its final-verdict state at `0fb8c93` and every
       post-closure word is in this file instead, which is exactly where EK3 routes it.
       The reviewer's own list said "closure artifact: R1243, R1244-R1247" and the report
       was never the right home for them.
```

## No number moved

No tolerance was added, widened or removed: `git diff` over `floatfea/tolerances.py` is
empty across every commit of this step, and no declared counter moved. §4 of
`docs/milestones/R2.md` lists the five values step 2 will need and classifies two of them
as **not** tolerances, with the reason.

## The one reusable rule this step produced

**Use the committed generator. Where one exists, a second implementation is the defect —
and the one you write will be the lenient one.**

Measured three times, each time by running the pair against each other rather than reading
either:

| | the two implementations | mine was |
|---|---|---|
| R1221 | the `MENTION` filter, guard and generator | present in one site only |
| R1240 | the Carried-section scoping | fixed in one site, pair unsatisfiable |
| the eight under-declared sites | the touched-line predicate | **lenient** — `range(380,405)` where the gate reads `{379,380}` |

And the fourth fact is what turns it from an observation into a rule:
**`scripts/untouched_sites.py` was committed the whole time**, its docstring already
saying *"IT IS THE GUARD'S OWN LIST, NOT A SECOND OPINION … a generator with its own regex
is a second implementation of the thing being satisfied, and the two drift — which is how
the first version of this script produced 68 rows against the guard's 87."* An ad-hoc
script was written beside it and drifted by the same mechanism, in the same direction.

**Both halves are measured.** Lenient: eight reds shipped. Already-solved: the committed
generator refuses on the unavailable-diff case the ad-hoc one would have read as "nothing
touched".

## The honest account of the round

Six reviewer rounds -- three interim checks, which count against no round, and three
reviewed revisions -- produced **ten findings carrying the blocking marker, and every one
was real.** The "five rounds" and "nineteen blocking findings" this paragraph used to
carry were both wrong: 3 + 3 is six, and nineteen was a count of RED TEST IDS rather than
of findings. Two arithmetic errors in one sentence about the step's own cost. The
implementer's own, recorded because the pattern matters more than any single instance:

* two wrong diagnoses of the `--check` refusal, the second with the refuting ablation
  already in git history;
* an escalation whose premise was never run (`.claude/hooks/` named as a blocking site; it
  has no such collision);
* a false claim in a reviewer brief about the implementer's own file contents;
* a figure attributing a red to a test that had not run, with the right answer printed
  twenty lines above;
* **a repair that broke the gate existing to prevent it**, with the reason recorded eight
  lines from the edit, and shipping a prediction its own run refuted;
* U+FFFD written into a published report by a script missing an `encoding` argument;
* a splice that deleted two sections by replacing a range instead of a token;
* a generator output pasted from a truncated console capture, publishing two red tests as
  green;
* three checks that could not fail, one of them eleven lines below a docstring warning
  about exactly that.

The common cause in nearly all of them is **asserting from reading rather than running**.
Every one was caught by something that ran, and none reached a number in front of Xabier.

**The two decisions that could have put a wrong number in front of him were both
declined**: pushing through the `--check` refusal, and regenerating the F6 deliverable to
agree with a red gate. Four rounds of not taking the cheap wrong repair is the best
evidence this step produced.
