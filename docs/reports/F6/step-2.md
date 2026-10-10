# F6 step 2 — the FloatFEA results report

# Revision 1 — FC0's first commit: the four gate items, before any report work

Answers: verdict 113 @ 2180f16

**2026-10-09.**

## 1. The schedule, and what this revision is

**F6 step 2's working target is 22 October and it holds.** Today is 9 October; the committed
date is 28 October. Step 1 closed on the 9th, thirteen days inside its own target.

**FC0 orders this commit and this is it.** The directive opens step 2 now, carrying only
what blocks — four closure items the directive promoted, named in the block below — plus
the two repair holes and the `section_class` unit refusal with its plan row. The rest of
the closure ledger goes past 28 October. **No report content is in this revision**; FC2's
nine sections follow, and a draft goes out as soon as sections 1 to 7 exist.

```
claim  the dates this step is measured against, and today's
cmd    grep -n "October" docs/milestones/F6.md | tail -2
out    293:Drafted under EY4, **locked by EZ4**. Working target **22 October**, committed
out    294:**28 October**. F4 closed **9 October** against a committed 19 October, and the
cmd    date +%Y-%m-%d
out    2026-10-09
rule   CLAUDE.md section Step gating: the report's one hand-written paragraph carries the
       schedule -- which date the step is measured against, and whether it holds
judge  thirteen days to the working target with the deliverable's inputs already built --
       the member-force table, the utilisation table and six of the nine sections' content
       exist as generated artifacts. No slippage to report.
```

## 2. What this revision built

Four closure items the directive promoted to blocking, and each was a hole in a gate rather
than a defect in a number. The figures each one is answered against are in § 3 to § 6.

## 3. C58 — R750's repair was not self-protecting

```
claim  the gate asserted the FLOOR and not that the floor is TIGHT, and a floor is
       satisfied by any larger response
rule   the declaration: the counter is a round bound just BENEATH the weakest live
       response, with the family's points placed AT the weak end
out    under `_worst_move` the reported weakest becomes min-over-COEFFICIENTS of
out      max-over-POINTS: 8.281906e-11, which is 276.1x the counter and 269.3x the
out      true weakest 3.074922627292889e-13
judge  so `weakest > COUNTER` passed under every substitution that destroyed the basis.
```

Three things now hold it, and the second is the one that matters:

* the floor is now asserted to be TIGHT as well as a floor;
* **the two aggregations ARE a minimum and a maximum, computed inline in the test rather
  than taken from the helpers.** The value is not what a substitution changes; the
  aggregation is — which is why an assertion about the value alone could not see it;
* the weakest member and its weakest point are asserted to be the ones the counter was
  derived at.

```
claim  the margin, the bound, and the spread each aggregation reads
cmd    the per-coefficient min and max over live points, at the declared injection
rule   the counter is a round bound just BENEATH the weakest live response
out    shipped margin                   1.024974x   bound F6_API_COUNTER_MARGIN_MAX 2.0
out    ALLOWABLE_TENSION_FACTOR  live 2  min 1.1475e-12  max 1.0000e-10  ratio    87.14
out    ALLOWABLE_SHEAR_FACTOR    live 1  min 1.0000e-10  max 1.0000e-10  ratio     1.00
out    BEAM_SHEAR_AREA_FACTOR    live 1  min 1.0000e-10  max 1.0000e-10  ratio     1.00
out    ELASTIC_LOCAL_BUCKLING_C  live 2  min 1.0000e-10  max 1.0000e-10  ratio     1.00
out    CM_JOINT_TRANSLATION      live 3  min 3.0749e-13  max 8.2819e-11  ratio   269.34
out    C_m's weakest point: `3.3.2 U KL/r=30.4`
judge  **THREE OF THE FIVE HAVE A RATIO OF 1.00**, so "more than one live point implies the
       min differs from the max" is false and could not have been the assertion. What holds
       it is the inline computation of both aggregations.
```

## 4. C59 — the ordering nothing asserted

```
claim  nothing asserted that the counter exceeds its own ceiling
out    the counter could fall to 1.0e-15, a TENTH of its ceiling 1.0e-14, with 68 passed
rule   a gate cannot be required to catch a defect it is also permitted to accept
judge  one line. The injection rising 100x is caught by the tight-margin bound in section 3
       rather than by a bound of its own, and the ceiling's own 15x of slack is the window
       rule's designed slack at MIN_EDGE = 2.0, which is not reopened here.
```

## 5. C60 — the clause's `10340/F_y` form makes the unit load-bearing

```
claim  an F_y in the wrong unit silently reclassified a slender section
cmd    section_class(2.5, 0.025, fy) at the shipped grade and at a kPa slip
rule   API RP 2A-WSD section 3.2.3: the branch limits are 10340/F_y and 20680/F_y with
       F_y in MPa
out    fy = 355e6 : D/t = 100 -> `reduced_2`, F_b = 220.79 MPa
out    fy = 355e3 : D/t = 100 -> `compact`,   F_b = 266.25 MPa, limit_1 = 29126.7606
out    the wrong allowable by 1.2059x, in the UNSAFE direction
out    fy = 0.0   : ZeroDivisionError rather than a named refusal
judge  FB1 had the module refuse a `D/t` outside the clause's range rather than
       extrapolate. This is that rule applied to the other load-bearing input, in the one
       function every other clause routes through.
```

```
claim  the declared range, what it admits, and what it refuses
cmd    the two constants, against every grade this milestone's gates use
rule   structural steel yield, generously bracketed
out    F6_API_FY_PLAUSIBLE_MIN = 2.0e8 Pa   F6_API_FY_PLAUSIBLE_MAX = 1.0e9 Pa
out    admitted: 235e6, 275e6, 355e6, 420e6, 460e6, 690e6 -- every grade G6.1 and the
out      dense agreement sweep use, plus S960 at 960e6 at the high edge
out    refused : 355e3 (kPa, three decades low), 355.0 (a bare number), 355e9 (GPa, two
out      decades high), 0.0, and a negative
judge  the low edge admits S235 and the high edge S960, so the range is wider than any
       grade this project will use and still three decades clear of a kPa slip.
```

## 6. C69 — the tie convention, stated and reachable

```
claim  the tie is reachable and the convention was unasserted
cmd    solve amplified == simple for My from the module's own F_a
rule   f_b = F_b (f_a/F_a - f_a/(0.6 F_y)) / (1 - C_m/(1 - f_a/F_e'))
out    KL/r = 60.8, f_a/F_e' = 0.02, My = 12633843.953476468 N.m
out    amplified = simple = 0.09426368988411232   -- bit-identically
out    below the crossing the AMPLIFIED form governs; above it the SIMPLE one does,
out      because 1 - C_m/(1 - f_a/F_e') is positive at 0.132653
judge  `max` returns the amplified operand at a tie and the field records `simple` -- the
       label that does not claim the amplification is doing anything. No published figure
       depends on the choice, but `>` to `>=` left the whole gate green, so the convention
       is now in the field's own docstring and bracketed either side of the crossing.
       **Verdict 113's figure was `1.263384395e+07` and `0.09426368988411235`**, the same
       crossing computed at the 4-decimal section modulus.
```

## 7. The control FC0 asks for

```
claim  every hole the verdict named now reddens, and the tree is restored after each
cmd    one edit at a time, source restored byte-identical, the whole of rung 5 re-run
rule   the verdict's figure to beat is `68 passed` on each
out    unperturbed                                                 -> exit 0  72 passed
out    C58 the counter assertion: _weakest_live_move -> _worst_move -> KILLED  3 failed
out    C58 the bracket test:      _weakest_live_move -> _worst_move -> KILLED  1 failed
out    C58 the weak-end point's My:  1.0e6 -> 1.0e8                 -> KILLED  1 failed
out    C58 the weak-end point's KL/r: 30.4 -> 90.0                  -> KILLED  1 failed
out    C59 the counter falls to a tenth of its own ceiling          -> KILLED  1 failed
out    C59 the injection rises 100x                                -> KILLED  1 failed
out    C60 the F_y refusal removed                                 -> KILLED  2 failed
out    C69 the tie convention: > -> >=                             -> KILLED  1 failed
out    unperturbed again                                           -> exit 0  72 passed
judge  **EIGHT OF EIGHT, where the first pass killed seven.** The survivor was the
       per-coefficient counter assertion, and it survived for C58's own reason: it asserted
       the floor and the substitution raises the response. What kills it is the inline
       min/max assertion rather than any bound on the value.
```

## 8. The suite, and EG3 state (1) — a NEW STEP whose review directory has no file yet

```
claim  153 report-guard tests are red, all of them state (1), and nothing else is
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py -q
out    153 failed, 138 passed, 1 skipped
out    by file: tests/test_report_carried.py 149; tests/test_report_numbers_are_sourced.py 4
out    and NOTHING under tests/verification, tests/unit or tests/regression
cmd    python -m pytest tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on -q
out    "step 2 has a report and no verdict yet. That is the legitimate boundary -- the
out     verdict is written after the report is committed -- and until it lands this guard
out     checks step 2, so step 2's carry list is UNCHECKED. Invoke the gating-supervisor."
out    assert 2 == 1
rule   EG3 state (1): report written, verdict not yet. The baseline is
       `test_the_guard_reads_the_step_being_worked_on` and the planted states cascade off it
out    the cascade, by test name: 113 test_every_named_site_is_touched_or_declared,
out      24 test_the_report_carries_the_finding, 4 test_every_number_in_prose_is_sourced,
out      and one each of the eleven generated-section guards
judge  **THE BASELINE SAYS THE CAUSE IN ITS OWN WORDS AND THE CASCADE IS KEYED ON IT.**
       `VERDICT` resolves to the newest file in the milestone's review directory, and
       `REVIEWED` is still `{1}` because step 2 has no verdict -- so every parametrisation
       is keyed on STEP 1's findings and sites while `STEP` is `2`. That is not step 2's
       carry list being wrong; it is step 2's carry list being UNREADABLE until a verdict
       for step 2 exists. **This is the same state F6 step 1's own revision 1 was in**, at
       43 reds, and it is self-clearing: the verdict creates the step-2 file,
       `max(REVIEWED)` becomes `2`, and revision 2 carries the generated sections.
```

**The generated sections are NOT in this revision and the reason is mechanical, not a
choice.** `scripts/carried_table.py`, `scripts/answered_table.py` and
`scripts/ci_section.py` all read `VERDICT`. At a step's first revision that resolves to the
PREVIOUS step's verdict, so every one of them would emit step 1's content into step 2's
report — the four findings above answer step 1's closure ledger, not a step-2 verdict, and
there is nothing for a `Carried` table to be a table OF. Revision 2 carries them.

## 9. Carried

**Nothing carries into step 2 blocking**, and the names are read from the verdicts rather
than from memory.

```
claim  what step 1 closed with, and what this revision answers
cmd    grep -c "^\* \*\*C" docs/reviews/F6/step-1.md   (run without naming the path)
out    26 C-items across the four verdicts in that file
rule   CZ0 as amended by EZ0: a closure item does not block; FC0 promoted four of them
out    verdict 112: step 1 PASS, carrying R752
out    verdict 113: R752 CLOSED; C66, C68, C70 raised and answered in the closure commit
out    this revision answers the four FC0 names, all previously closure class
judge  the rest of the ledger is past 28 October by FC0's own words -- "Everything else
       goes to the ledger, after 28 Oct." -- and no item on it blocks.
```

```
claim  this revision does not touch the ledger or any verdict
cmd    git diff --stat HEAD -- docs/closure/
out    (empty)
rule   CZ0 as amended by EZ0: a finding that is not (a) to (d) is a closure item, fixed
       once in the step's closure commit and not re-reviewed item by item
judge  FC0's own words -- "Everything else goes to the ledger, after 28 Oct." A verdict is
       not writable by the implementer at all: a `PreToolUse` hook refuses it, Bash
       included, which is a stronger statement than a clean diff.
```

## 10. What this revision does NOT do

* **No report content.** FC2's sections are the step's deliverable and none of them is
  written yet. The inputs exist and are listed in the block below; the first batch goes out
  as a draft as soon as it exists.
* **No PDF.** FC2 asks for one; nothing in the repository renders markdown yet, and that is
  part of the deliverable's own work rather than of this commit.
* **The ledger is untouched** and is past its date by FC0, as § 9 records.

```
claim  the deliverable's inputs already exist, which is why the date holds
cmd    ls -1 docs/F4_member_forces.csv docs/F6_utilisation.csv docs/F6_utilisation.md
out    docs/F4_member_forces.csv
out    docs/F6_utilisation.csv
out    docs/F6_utilisation.md
cmd    wc -l docs/F4_member_forces.csv docs/F6_utilisation.csv
out    1266 docs/F4_member_forces.csv
out      45 docs/F6_utilisation.csv
out    1311 total
rule   FC2's nine sections: scope, model, mass basis, loads, verification summary, member
       forces, code check, findings, what would change the answer most
judge  the member forces, the utilisations and the gate summaries are generated artifacts
       already in the tree, so what remains is the writing and the render rather than the
       measuring.
```


# Revision 2 — R753 answered by deletion, and seven false figures with it

Answers: verdict 114 @ bf45e66
Answers file: `docs/reports/F6/step-2-answers.json`

**2026-10-09.**

## 0. CI at `02b7daf`, the commit verdict 114 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 114 at `02b7daf` through the report's own `Answers:` line. Run `38013114860`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 2201 | 0 | 0 |
| lint, unit and guards | 1002 | 155 | 1 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 155.**

- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R712]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R717]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R730]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R731]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R732]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R734]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R735]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R736]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R737]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R738]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R739]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R740]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R741]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R742]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R743]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R744]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R745]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R746]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R747]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R748]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R749]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R750]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R751]` (lint, unit and guards)
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
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-docs/F6_utilisation.md:35]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-docs/conventions.md:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-floatfea/checks/api_wsd.py:254]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-floatfea/post/member_forces.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-scripts/measure/api_wsd_utilisation.py:138]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-scripts/measure/member_forces_table.py:415]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-docs/F4_member_forces.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-docs/F6_utilisation.md:13]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-scripts/measure/api_wsd_utilisation.py:79]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-scripts/measure/api_wsd_utilisation.py:80]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-scripts/measure/api_wsd_utilisation.py:81]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:132]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:133]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:134]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:135]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:136]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:137]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:138]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:139]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:140]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:141]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:142]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:146]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:150]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:151]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:152]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:153]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R742-floatfea/basis.py:46]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R742-floatfea/checks/api_wsd.py:102]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R742-floatfea/checks/api_wsd.py:103]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:71]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:72]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:73]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:74]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:75]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:76]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:77]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:446]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:447]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:448]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:449]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-docs/reports/F6/step-1-answers.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-docs/reports/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-docs/reviews/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-scripts/suite_count.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-step-1-answers.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-test_report_guard_states.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_carried.py:211]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_guard_states.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_numbers_are_sourced.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R746-docs/reports/F6/step-1.md:5]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-docs/F6_utilisation.md:81]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-docs/F6_utilisation.md:82]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-docs/F6_utilisation.md:83]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:363]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:364]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:365]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:366]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:367]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:368]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:369]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:370]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:371]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:372]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:373]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:375]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-__init__.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-docs/F6_utilisation.md:9]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-docs/reports/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-scripts/measure/api_wsd_utilisation.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-scripts/run_rung.sh]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R749-floatfea/checks/api_wsd.py:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R749-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:368]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:888]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:889]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:890]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:891]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:892]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:893]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:894]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:895]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:896]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:897]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:898]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:899]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:900]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:901]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:902]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:903]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:904]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:905]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:906]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:907]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:908]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R751-docs/reports/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R751-floatfea/post/member_forces.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-api_wsd_utilisation.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-docs/F6_utilisation.md:69]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-floatfea/checks/api_wsd.py:401]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-floatfea/checks/api_wsd.py:402]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-floatfea/checks/api_wsd.py:403]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:375]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:376]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:383]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:384]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 114 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 114 at `02b7daf` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `38013114860` | push | `02b7daf` | conclusion **failure** |

**Run `38013114860`, conclusion **failure**: 155 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R712]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R717]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R730]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R731]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R732]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R734]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R735]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R736]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R737]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R738]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R739]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R740]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R741]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R742]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R743]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R744]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R745]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R746]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R747]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R748]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R749]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R750]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R751]` (lint, unit and guards)
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
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-docs/F6_utilisation.md:35]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-docs/conventions.md:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-floatfea/checks/api_wsd.py:254]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-floatfea/post/member_forces.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-scripts/measure/api_wsd_utilisation.py:138]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R739-scripts/measure/member_forces_table.py:415]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-docs/F4_member_forces.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-docs/F6_utilisation.md:13]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-scripts/measure/api_wsd_utilisation.py:79]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-scripts/measure/api_wsd_utilisation.py:80]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R740-scripts/measure/api_wsd_utilisation.py:81]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:132]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:133]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:134]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:135]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:136]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:137]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:138]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:139]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:140]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:141]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:142]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:146]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:150]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:151]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:152]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R741-floatfea/checks/api_wsd.py:153]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R742-floatfea/basis.py:46]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R742-floatfea/checks/api_wsd.py:102]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R742-floatfea/checks/api_wsd.py:103]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:71]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:72]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:73]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:74]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:75]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:76]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R743-floatfea/checks/api_wsd.py:77]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:446]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:447]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:448]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R744-scripts/measure/member_forces_table.py:449]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-docs/reports/F6/step-1-answers.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-docs/reports/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-docs/reviews/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-scripts/suite_count.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-step-1-answers.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-test_report_guard_states.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_carried.py:211]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_guard_states.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R745-tests/test_report_numbers_are_sourced.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R746-docs/reports/F6/step-1.md:5]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-docs/F6_utilisation.md:81]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-docs/F6_utilisation.md:82]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-docs/F6_utilisation.md:83]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:363]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:364]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:365]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:366]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:367]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:368]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:369]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:370]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:371]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:372]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:373]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R747-scripts/measure/api_wsd_utilisation.py:375]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-__init__.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-docs/F6_utilisation.md:9]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-docs/reports/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-scripts/measure/api_wsd_utilisation.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R748-scripts/run_rung.sh]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R749-floatfea/checks/api_wsd.py:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R749-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:368]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:888]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:889]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:890]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:891]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:892]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:893]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:894]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:895]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:896]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:897]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:898]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:899]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:900]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:901]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:902]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:903]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:904]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:905]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:906]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:907]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R750-tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:908]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R751-docs/reports/F6/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R751-floatfea/post/member_forces.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-api_wsd_utilisation.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-docs/F6_utilisation.md:69]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-floatfea/checks/api_wsd.py:401]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-floatfea/checks/api_wsd.py:402]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-floatfea/checks/api_wsd.py:403]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:374]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:375]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:376]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:383]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R752-scripts/measure/api_wsd_utilisation.py:384]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 1. The schedule, and what this revision is

**F6 step 2's working target is 22 October and it holds.** Today is 9 October. Verdict 114
held on one item, R753, and listed thirteen closure items; **seven of those are false
figures or missing refusals that I wrote, so they are answered here rather than ledgered** —
a wrong number in a tolerance entry or a docstring is not prose. FC2's results report is
still ahead of me, and this revision buys it a tree with no known false figure in it.

```
claim  the dates this step is measured against, and today's
cmd    grep -n "October" docs/milestones/F6.md | tail -2
out    293:Drafted under EY4, **locked by EZ4**. Working target **22 October**, committed
out    294:**28 October**. F4 closed **9 October** against a committed 19 October, and the
cmd    date +%Y-%m-%d
out    2026-10-09
rule   CLAUDE.md section Step gating: the report's one hand-written paragraph carries the
       schedule -- which date the step is measured against, and whether it holds
judge  thirteen days to the working target. No slippage, and the verdict agrees -- it put
       no schedule item on the list.
```

## 2. R753 — the clause is deleted, which is the second route its condition offered

```
claim  the published clause was false as an identity and empty as an implication
cmd    recompute both forms of section 3.3.2 at C_m = 0.85 and C_m = 1.0 from the
       deliverable's own columns, on all 17 compression rows
rule   the clause: "those are the rows where amplified(C_m = 1.0) OVERTAKES simple"
out    amplified(C_m = 1.0) > simple                     : 17 of 17
out    ... and amplified(0.85) did NOT                   : 10 of 17
out    C_m visibly moves U at 6 significant figures      : 10 of 17
out    smallest non-firing overtake: hub3:buoy8_arm TIP, 0.008977 against 0.007717 = 16%
judge  **THE VERDICT IS RIGHT AND THE DIAGNOSIS IS SHARPER THAN MINE WAS.** What I MEASURED
       was the stricter predicate -- overtakes at `1.0` and did not at `0.85` -- which is
       `10 of 17` and does coincide with the count. What I WROTE was the loose one, which
       holds everywhere. **This is C68 for the second time: one f-string literal replaced
       another.** So the clause goes, by the second of the two routes the condition named.
```

The published line is now the predicate and nothing else:

```
claim  the deliverable states what is counted and makes no claim about why
cmd    python scripts/measure/api_wsd_utilisation.py  then read docs/F6_utilisation.md:70
rule   a definition is not an inference
out    C_m visibly moves the governing U on 10 of 17 compression rows, at the 6
out      significant figures this file publishes
judge  the precision is in the sentence, which is C67 and is load-bearing now: two
       utilisations differing in the seventh figure are EQUAL in the published file, so a
       count taken in memory is `12 of 17` and is not reproducible by the file's reader.
       `_CSV_FIGURES` names it in one place and the sentence reads it.
```

**And the verdict's own figure differs from mine on one point, which I record rather than
reconcile.**

```
claim  which of the seven non-firing rows carries the SMALLEST overtake
cmd    the overtake ratio at C_m = 1.0 over the seven rows where C_m is not visible
rule   the verdict names platform:hub1_arm TIP as the smallest of the seven
out    hub3:buoy8_arm    TIP  0.008977 against 0.007717  -> 16% over   <- smallest
out    hub3:buoy9_arm    TIP  0.008977 against 0.007717  -> 16% over
out    hub1:buoy2_arm    TIP  0.008054 against 0.006252  -> 29% over
out    hub1:buoy3_arm    TIP  0.008054 against 0.006252  -> 29% over
out    hub1:buoy1_arm    TIP  0.015702 against 0.011874  -> 32% over
out    platform:hub3_arm TIP  0.093110 against 0.031995  -> 191% over
out    platform:hub1_arm TIP  0.095733 against 0.032896  -> 191% over  <- the verdict's
judge  **THE SUBSTANCE IS IDENTICAL AND IS THE FINDING: ALL SEVEN ARE OVERTAKES.** The
       verdict's two numbers are right and its row is the LARGEST of the seven rather than
       the smallest. Recorded, not reconciled -- the claim it supports is unaffected.
```

## 3. Nothing under `tests/` held the clause, and now something does

```
claim  the clause could be replaced by anything and the suite stayed green
rule   the verdict's own measurement: "the moon is made of cheese" leaves
       tests/regression/test_f6_deliverable_agrees_with_itself.py at 10 passed
out    that file now parses the sentence's COUNT and its stated PRECISION, and asserts
out      both against the CSV's own column
cmd    python -m pytest tests/regression -q
out    144 passed
judge  it reads the predicate and the precision and nothing else, so there is no clause
       left for it to be unable to check. What it still cannot do is say the CSV is right;
       that is G6.1's job.
```

## 4. C72 — the refusal reached two of six entry points

```
claim  the F_y refusal covers every public entry that takes F_y, not the production path only
cmd    call all eight at 355e6 and at 355e3
rule   C60 put the refusal inside `section_class`; `allowable_bending` routes through it,
       which is why production was safe and the API surface was not
out    section_class / allowable_axial_tension / allowable_shear /
out      column_slenderness_parameter / local_buckling_stress / allowable_bending /
out      allowable_axial_compression / check_member
out    at 355e6: ok on all eight.  at 355e3: REFUSED on all eight
out    before: allowable_axial_compression(121.5, 2.5, 0.025, 355e3) returned
out      F_a = 1.928148e+05 on branch 'inelastic_local' where 355e6 gives 'elastic_local'
judge  **THE BRANCH IS A PUBLISHED CSV COLUMN AND FA2 MAKES IT A REPORTED QUANTITY**, so a
       caller reaching section 3.2.2 directly got a label the table publishes. It is a
       funnel now -- `_require_plausible_fy` -- because a refusal in one of several entry
       points is a refusal a caller walks past.
```

```
claim  and the funnel does not fire on a value this module computed for itself
cmd    F_xc over the clause's own admissible range, against the declared floor
rule   allowable_axial_compression substitutes F_xc for F_y and passes it on
out    D/t =  61 -> F_xc = 354.01 MPa      D/t = 200 -> 275.15 MPa
out    D/t = 100 -> F_xc = 324.00 MPa      D/t = 300 -> 242.39 MPa
out    the floor is 200 MPa, so the margin at the clause's own D/t = 300 limit is 1.21x
out    past D/t = 300 the AXIAL refusal fires first, not the F_y one
judge  asserted, so widening the `D/t` limit cannot silently make the refusal fire on the
       module's own intermediate.
```

## 5. C80 — a negative diameter returned the BEST allowable

```
claim  a sign slip on either geometry input returned `compact`
cmd    section_class and local_buckling_stress at zero and negative geometry
rule   every branch test in section 3.2.3 is an UPPER bound, so a negative D/t satisfies
       the first one
out    before: D = -2.5 -> branch 'compact', D/t = -13.88888888888889
out    before: t = -0.18 -> branch 'compact'; D = 0.0 -> 'compact'; t = 0.0 ->
out      ZeroDivisionError
out    after : all five refused, on BOTH dividers, with "not a tube"
judge  **THE DIRECTION IS WHAT MAKES IT WORTH A REFUSAL RATHER THAN A NOTE.** `compact` is
       the top of the three branches, so the defect returned `F_b = 0.75 F_y` -- the
       highest allowable the clause has -- on a nonsense section. A second funnel,
       `_require_tube`, for C72's reason: two functions divide by `wall`.
```

## 6. Five figures I wrote that were wrong

Each is a measurement, each was refuted by one command, and none is prose.

```
claim  C71: the ratio named at the section the sentence names
cmd    allowable_bending at D/t = 100 and at D/t = 300
rule   the entry says "the wrong allowable by Nx on a section the clause says is slender",
       and names D/t = 100
out    D/t = 100  reduced_2  F_b = 220.793 MPa  compact/F_b = 1.205880
out    D/t = 300  reduced_2  F_b = 151.179 MPa  compact/F_b = 1.761154
judge  the entry carried `1.76x`, which is the `D/t = 300` figure -- the far end of the
       clause's range. The plan row, the step report and this commit's own bit-exact
       assertion all carried `1.2059`, so the entry disagreed with three places that
       agreed with each other.
```

```
claim  C75: how many of the seven are the both-halves case
cmd    classify the seven non-firing rows by governing channel and by bending share
rule   the comment said "0 of the 7 are the both-halves case"
out    BOTH halves : 1   (hub1:buoy1_arm TIP, beam shear AND f_b = 4.659e-08 MPa)
out    shear only  : 4   (f_b of 0.1779, 0.1779, 1.023, 1.023 MPa)
out    negligible only : 2   (platform:hub1_arm and hub3_arm TIP)
judge  `1`, and verdict 113 had published `1`. My own classifier mis-binned it because it
       compared a reconstructed `u_combined` against the published `U` at a relative
       tolerance, and at a bending share of `0.0000%` that comparison cannot resolve.
```

```
claim  C74: the margin bound is the sole killer of ONE of the four substitutions
cmd    each substitution one at a time, by which assertion reddens
rule   the entry said "the three substitutions miss it by two decades"
out    counter assertion -> _worst_move : the INLINE min/max assertion
out    bracket test      -> _worst_move : THE MARGIN BOUND
out    weak-end My moved               : the weakest-name and weakest-point assertions
out    weak-end KL/r moved            : the same two
judge  the bound covers one; three assertions that do not read it cover the rest. **And
       EH4's weakening test now pins the bound from above** -- it must sit below
       `strongest / COUNTER = 276.1x`, so raising it to `300.0` reddens that test instead
       of admitting the substitution it was raised to admit.
```

```
claim  C83: the tie docstring carried the ROUNDED My, at which the field returns the
       OPPOSITE label
cmd    check_member at the docstring's My and at the exact crossing
rule   the docstring states that a tie is recorded as `simple`
out    My = 12633843.95            -> amplified   U = 0.09426368986817012
out    My = 12633843.953476468     -> simple      U = 0.09426368988411232
judge  **THE ONLY PLACE THE CONVENTION IS WRITTEN DOWN CARRIED AN EXAMPLE THAT CONTRADICTS
       IT.** The tie is a single double; a rounded neighbour of it is not a tie. The
       rounded pair came from verdict 113's own figure, which that verdict has since
       withdrawn as the looser of the two -- and I copied it into `floatfea/` instead of
       the value I had solved.
```

```
claim  C76: the overtake sentence in the generator's comment, R753's own class
out    "That is what the predicate detects" -- the overtake alone holds on 17 of 17
judge  corrected in the same comment, in the same commit as the published clause. It is
       the same false sentence in two places and only one of them was published.
```

## 7. C73 and C81 — EH4's weakening direction, which I applied to nothing

The verdict's observation is the one I would keep: *"EH4 is written down, it is three
months old, and it was applied to nothing in this diff — every boundary in the new entries
is solved from the side that makes the gate look strong."* That is right, and it is now a
test rather than a sentence.

```
claim  each of the three new constants has its weakening boundary SOLVED, not sampled
cmd    tests/.../test_EH4_the_weakening_boundary_of_each_new_constant_is_SOLVED
rule   EH4: a boundary is solved in BOTH directions, including the two that WEAKEN a gate
out    F6_API_COUNTER_MARGIN_MAX  weakens by RISING: admitted at 276.1x, the margin the
out      max-over-points aggregation produces. Declared 2.0, so 138x of room, and the
out      clean margin 1.024974x bounds it from below
out    F6_API_FY_PLAUSIBLE_MIN    weakens by FALLING: a kPa S355 is admitted at 3.55e5.
out      Declared 2.0e8. It may RISE only to 2.35e8 before S235 is refused
out    F6_API_FY_PLAUSIBLE_MAX    weakens by RISING: a GPa S355 is admitted at 3.55e11.
out      Declared 1.0e9. It may FALL only to 9.6e8 before S960 is refused
judge  the two `F_y` edges are bounded on BOTH sides by real grades, which is why the range
       is wide: narrowing it toward the measurement would refuse a steel someone may use.
```

## 8. The suite, CI, and EG3 state (2)

```
claim  every red is EG3 state (2) -- verdict written, answering report not yet -- and the
       trace is by name
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py -q
out    13 failed, 124 passed, 1 skipped
out    test_a_blocking_item_is_not_routed_to_4a
out    test_a_carried_row_points_at_a_section_that_discusses_it[(none)]
out    test_a_report_does_not_say_CLOSED
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
out    test_the_CI_section_is_about_the_REVIEWED_commit
out    test_the_Carried_table_is_what_the_generator_produces
out    test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph
out    test_the_generator_would_catch_a_row_under_the_wrong_number
out    test_the_report_carries_a_CI_SECTION
out    test_the_report_carries_a_WHOLE_SUITE_count
out    test_the_report_carries_the_finding[R753]
out    test_the_reported_CI_counts_are_not_all_zero
out    test_there_are_pointers_to_resolve
cmd    python -m pytest ... tests/test_report_guard_states.py -q   (the three files)
out    20 failed, 140 passed, 1 skipped
rule   EG3 state (2) plus FC1's two additions, which are now on the list by directive
judge  **EVERY ONE OF THE THIRTEEN IS SOMETHING THIS REVISION SUPPLIES** -- the CI
       sections, the whole-suite line, the Carried table, the pointers and the finding row.
       The seven further reds in `test_report_guard_states.py` are the planted states
       cascading off the baseline, which is how EH1 identifies the cascade. Nothing outside
       the three files.
```

**EG3(ii), measured at the verdict commit, which is the half no verdict can take after the
fact.**

```
claim  state (1) cleared at the verdict commit and what remained was state (2)
cmd    at bf45e66, tree clean: the three report-guard files
out    26 failed, 134 passed, 1 skipped
rule   EG3(ii): after the verdict commit exists, the report-guard files are run AT that
       commit and the counts pasted in the next revision
judge  **THE VERDICT'S OWN FIGURE REPRODUCES EXACTLY.** Down from `155` at `02b7daf`, and
       `test_the_guard_reads_the_step_being_worked_on` passes there -- state (1) cleared at
       the verdict, as designed. The verdict also records that six of state (2)'s names are
       not on EG3/EH1's list; that is the same shortness EH1 and R644 corrected twice and
       it is a directive candidate, not mine to write. FC1 added two of them.
```

**AND MY REVISION-1 TRACE DID NOT REPRODUCE**, which the verdict files under its own
number and which is CP3.

```
claim  revision 1's published trace does not reproduce at its own commit
rule   CP3: the `out` line is copied from a run executed AFTER the final edit to the thing
       it describes, and if an edit follows the paste, the paste is void
out    revision 1 published : 153 failed, 149 in test_report_carried.py, 4 in
out      test_report_numbers_are_sourced.py
out    the reviewer's run of that same command, at that same commit:
out      148 failed, 145 passed, 1 skipped -- all 148 in test_report_carried.py, ZERO in
out      test_report_numbers_are_sourced.py
judge  I pasted the count and then edited the prose the guard reads, so the paste described
       a tree that had moved -- and the four I attributed to the prose guard were the four
       my own later edits removed. The figures in this section are taken after the last
       edit to this revision.
```

## 9. Carried

**The row set, the class and the subject are the verdict's; the state and the pointer are
`docs/reports/F6/step-2-answers.json`'s. Neither is retyped here.**

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R752 | **not classified in this verdict** — carried in from an earlier one | CLOSED at verdict 113 and NOT reopened. It does not carry; the report records |
| R753 | **answered** — §2 | no clause this generator can cut -- see the verdict's Carried section |

### What each finding was, and where the answer lives

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R753 | recorded | **answered** | §2 | `scripts/measure/api_wsd_utilisation.py` | `docs/F6_utilisation.md:70`, generated at |

**R752 is closed at verdict 113 and does not carry.** The generator cannot classify it
because this verdict does not declare it; the row above records that, and § 2 of step 1's
closure commit is where it was answered.

**The closure ledger: C41 to C70 stay on it and FC0 routes C41 to C65 past 28 October.**
Of verdict 114's thirteen, **seven are answered in this revision** -- C71, C72, C73, C74,
C75, C76, C80, C81 and C83, which is nine by count, because each is a false figure or a
missing refusal rather than prose. What remains of this verdict's list is C77, C78 and C79
(revision 1's report figures, one of which § 8 answers), and C82 (this revision's own
prose), which go to the step's closure commit.

No row points at this section: every item is in this table by construction, so a pointer
here would resolve whatever it said (R318).

## 10. Two reds whose cause is the verdict's heading format, not this report

```
claim  two guards cannot parse a blocking class from verdict 114 and say so
cmd    python -m pytest tests/test_report_carried.py -k "blocking or wrong_number" -q
out    test_a_blocking_item_is_not_routed_to_4a  -- "no blocking finding parsed from
out      step-2.md. The heading format changed and this check passes on anything."
out    test_the_generator_would_catch_a_row_under_the_wrong_number  -- StopIteration
rule   the guard reads `^\*\*(R\d+)\.?\s*\(([^)]*)\)` and looks for "block" inside the
       parenthetical
out    verdict 114  : `**R753.** \`docs/F6_utilisation.md:70\`, generated at`
out    verdicts 110-113: `**R750. (BLOCKING. (b) -- A COUNTER VALUE AND THE FORM OF ONE...`
out    `**R751. (BLOCKING. (a) -- AND I AM NAMING THE CLASSIFICATION...`
out    `**R752. (BLOCKING. (a) AS AMENDED BY EZ0 -- A DEFECT IN A PUBLISHED DELIVERABLE...`
judge  **THE GUARD IS WORKING AND IT IS NOT FAILING FALSE.** Every verdict before this one
       put the class in a parenthetical after the number; verdict 114 states it as a
       heading above the finding (`**ONE BLOCKS.**`) instead, so `_blocking()` returns the
       empty set and the guard correctly reports that it would pass on anything. **I cannot
       fix this**: a `PreToolUse` hook refuses any write under the review directory, and
       the implementer never edits a verdict. It is one line in the reviewer's own
       convention, and it is raised in the next invocation rather than worked around here.
       Recorded as RED WITH ITS CAUSE NAMED, which is what EG3 asks of a boundary red --
       and this one is not on either of EG3's lists, so it is named rather than waived.
```
