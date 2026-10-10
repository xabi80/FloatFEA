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

## 11. The whole suite, and the ten

```
claim  nothing outside the three report-guard files is red, and the ten divide into three
       causes
cmd    python scripts/suite_count.py        (one invocation over the whole suite)
out    Whole suite at `9af9b75`: 3135 passed, 0 failed, 0 skipped.
out    The excluded set: 154 passed, 10 failed, 1 skipped.
out    test_a_blocking_item_is_not_routed_to_4a                     <- the verdict's
out    test_the_generator_would_catch_a_row_under_the_wrong_number   <- heading format
out    test_the_report_carries_a_WHOLE_SUITE_count                   <- this line
out    test_the_guard_survives_the_state[baseline]                   <- cascade
out    ...[non_numeric_step_suffix]      ...[superscript_digit_step_number]
out    ...[draft_suffix_beside_a_step_report]   ...[step_number_is_the_empty_string]
out    ...[verdict_amended_after_the_commit_the_report_answers]
out    ...[zero_padded_step_number]
cmd    gh run list --limit 1 --json headSha,status,conclusion   then its jobs
out    9af9b75 completed failure
out    the verification ladder            success
out    lint, unit and guards              failure
out    CI determinism -- leg / ten legs   skipped
out    the run's own id is NOT written here: CX0 keeps it to the generated sections, and
out      section 0a of the next revision is where it lands
rule   EG3 state (2) as amended by FC1, which added the whole-suite and CI-table guards
judge  **THREE CAUSES, AND TWO OF THEM ARE NOT MINE TO CLEAR.** The suite-count line is
       CZ1's class and the commit carrying this section clears it. The seven planted
       states cascade off the baseline, which is how EH1 identifies a cascade. The other
       two are the verdict's heading format, named in § 10, and the implementer cannot
       edit a verdict. **Nothing under `tests/verification`, `tests/unit` or
       `tests/regression` is red** and the ladder is SUCCESS at this commit.
```

**Whole suite at `9af9b75`: 3135 passed, 0 failed, 0 skipped.** **The excluded set: 154 passed, 10 failed, 1 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 165 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_a_blocking_item_is_not_routed_to_4a`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_a_WHOLE_SUITE_count`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
```

# Revision 3 — R754 by a second predicate, and FC2's deliverable

Answers: verdict 115 @ a16eb28
Answers file: `docs/reports/F6/step-2-answers.json`

**2026-10-09.**

## 0. CI at `5c71cb4`, the commit verdict 115 judged — **report-only; no run by design** — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 115 at `5c71cb4` through the report's own `Answers:` line. The judged commit touches only paths the workflow ignores (`docs/reports/**`, `docs/reviews/**`), so no run was created for it. **Code-identical run at `9af9b75c11c1a35b5a413cc92a80faf9381cf92b`**: run `38017640023`, event `push`, conclusion **failure**.

```
cmd  gh run list --commit 5c71cb4d72854fd1bf2b27116da57fabe1620a80
out  (no output)
cmd  git diff --name-only 9af9b75 5c71cb4
out  only paths under the workflow's paths-ignore
judge NO RUN BY DESIGN, not CK2 and not a red. The run below measures the same
     code, because every path that differs is one the workflow ignores.
```

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 995 | 10 | 1 |
| the verification ladder | 2206 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 10.**

- `tests/test_report_carried.py::test_a_blocking_item_is_not_routed_to_4a` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 115 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 115 at `5c71cb4` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| (none) | | | no run at any commit in this round |

## 1. The schedule, and what this revision is

**F6 step 2's working target is 22 October and it holds.** Today is 9 October. This is
**round 3 of 3** under CZ0's cap, so it is the last revision of this step that gets read in
full; after it the step closes, a blocking item still open carries by name into step 3, and
the closure items go into the closure artifact as a list. Verdict 115 held on one item,
R754, and set three conditions beyond it: the grid as the adversarial case, FC2's results
report at sections 1 to 7 at least, and that the nine reds clear by this revision existing.
**All three are here, and the deliverable and R754 land in the same revision**, which is the
first of the two choices the verdict's section 7 offered.

```
claim  the dates this step is measured against, and today's
cmd    grep -n "October" docs/milestones/F6.md | tail -2
out    294:Drafted under EY4, **locked by EZ4**. Working target **22 October**, committed
out    295:**28 October**. F4 closed **9 October** against a committed 19 October, and the
cmd    date +%Y-%m-%d
out    2026-10-09
rule   CLAUDE.md section Step gating: the report's one hand-written paragraph carries the
       schedule -- which date the step is measured against, and whether it holds
judge  thirteen days to the working target, and FC2's own deliverable date is 22 October
       with the draft asked for "as soon as sections 1-7 exist". All nine sections exist.
       No slippage to report.
```

## 2. R754 — the refusal stays on the public entries, site by site

**R754 is answered.** Verdict 115's condition offered two routes and I took the first:
`column_slenderness_parameter` takes the STRESS it is actually given, through a predicate
of its own with a floor beneath every admissible configuration, and the plausible-GRADE
range is untouched at `[2.0e8, 1.0e9]` on the public `F_y` entries. The second route —
deriving the admissible lower edge for a reduced stress as the function of grade and `D/t`
that it is — is what the floor now stands beneath rather than what replaces it, and
section 3 is why a constant is defensible here where R694 said it was not.

```
every figure this section quotes, and where it comes from. The four SITE numbers are
verdict 115's own, read off its Findings section; the rest are the constants and literals
the sites are about.

  2.0e8, 1.0e9      floatfea/tolerances.py: F6_API_FY_PLAUSIBLE_MIN and _MAX, unmoved
  355, 355e6        the grade my C72 docstring was correct at (S355)
  235e6             the grade the verdict substituted to redden the one-grade gate
  2.35e8            the same grade, as the :1452 assertion spells it
  1398, 1452        verdict 115's line numbers for the gate and for the assertion it
                    contradicted -- its text, not a measurement of mine
  3010, 239         verdict 115's line numbers for the two BP0 sites
  230, 273          the funnel call before and after, measured by the grep in site 1
```

### The cell: one variable, the grid held

```
claim  the grade predicate refused an eighth of the declared six-grade sweep on the
       module's own intermediate; the stress predicate refuses none of it
cmd    python scripts/measure/r754_stress_vs_grade.py
out    grid: 6 declared grades x D/t in [5.00, 300.00] step 0.01
       held: the module, the grid, E = 2.100e+11 Pa, D = 2.5 m
       moved: the predicate in front of column_slenderness_parameter's argument

       predicate                           floor [MPa]   refused      of  fraction      binding F_xc [Pa]
       _require_plausible_fy   (GRADE)           200.0     21357  177006  12.066%       2.0000015687e+08
       _require_plausible_stress (STRESS)        100.0         0  177006   0.000%       1.6045517211e+08
cell   the ONE variable is which funnel stands in front of that argument. NOTHING IS
       PATCHED: both predicates are asked about the same `F_xc` the module itself computes,
       over the same grid, the same six grades and the same `D/t` range. The script is
       committed under `scripts/measure/`, so the command is one the reviewer can run.
rule   the reviewer's own figures, reproduced: the self-fire begins at `D/t = 138.4383` for
       S235 and `248.0006` for S275, and `12.1%` of the grid raised. TABLE 1 of the same
       run carries both numbers to the digit, and the fraction exactly as `12.066%`.
judge  the third column MOVED, `2.000e+08` to `1.605e+08`. That is the tell and not a
       detail: under the grade predicate the points below 200 MPa were the ones being
       refused, so its binding figure measured the defect rather than the clause.
```

### The four sites the verdict named

**Site 1 — `floatfea/checks/api_wsd.py:230`, the predicate the internal substitution passes
through. CHANGED.** The call is now `_require_plausible_stress`, a second predicate whose
message says in its own clause that the argument is a stress and not a grade.

```
claim  the funnel in front of that argument is the stress predicate, and the grade
       predicate still guards the five public F_y entries
cmd    grep -n "_require_plausible_stress\|_require_plausible_fy" floatfea/checks/api_wsd.py
out    143:def _require_plausible_fy(fy: float) -> None:
out    170:def _require_plausible_stress(stress: float) -> None:
out    237:    _require_plausible_fy(fy)
out    259:    _require_plausible_fy(fy)
out    273:    _require_plausible_stress(fy)
out    301:    _require_plausible_fy(fy)
out    334:    _require_plausible_fy(fy)
out    413:    _require_plausible_fy(fy)
judge  one site moved and five did not, which is the shape the condition asked for: the
       refusal stays on the public entries and the internal call stops passing through
       a grade range. The line moved from 230 to 273 because the new predicate, and
       a BI3 triple inside it, are both defined above it.
```

**And the docstring the verdict called out by name is replaced, not softened.** The sentence
"`F_y` here is `F_xc` ... and is therefore already inside the range" was CW0's half with
BG0's missing cell: true at S355 and false at the two grades below it. It now says the
opposite, with the figure.

```
claim  the false justification is gone from the tree, and the correction names the grades
cmd    git diff 1e19f7f^..HEAD -- floatfea/checks/api_wsd.py | grep "^-.*already inside"
out    -    `F_y` here is `F_xc` on a slender tube, which is `local_buckling_stress`'s output and is
```

**Site 2 — `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:1398`, the
denying gate. REPLACED, NOT WIDENED.**
`test_the_INTERNAL_F_xc_call_stays_inside_the_range_at_every_admissible_section` asserted
at one grade literal, `FY = 355e6`, and the verdict reddened it by substituting `235e6`.
The gate in its place is asserted over the whole grade x slenderness grid, so there is no
literal left to substitute.

```
claim  the new gate sweeps every admissible grade against every slenderness the clause
       admits, and the old one-grade gate is gone from the file
cmd    grep -n "def test_the_INTERNAL_F_xc_call" \
         tests/verification/rung5/test_g61_api_wsd_hand_calculations.py
out    1400:def test_the_INTERNAL_F_xc_call_cannot_REFUSE_over_the_WHOLE_grade_x_SLENDERNESS_GRID() -> None:
cmd    grep -n "checked == len(grades)\|assert binding ==" \
         tests/verification/rung5/test_g61_api_wsd_hand_calculations.py
out    1434:    assert checked == len(grades) * 2951, checked
out    1446:    assert binding == 1.365575932867604e08  # not-a-tolerance: the hand value, exact
rule   7 grades -- the six declared plus the plausible floor itself -- x 2951 slendernesses
       = 20657 calls. The binding `F_xc` is asserted as an exact hand value rather than as
       a bound, so a drift in either direction reddens it.
```

**Site 3 — `tests/verification/rung5/...:1452`, the assertion the gate contradicted.
UNCHANGED BY DESIGN, and now consistent.** It asserts `F6_API_FY_PLAUSIBLE_MIN < 235e6`
because the low edge may rise only to `2.35e8` before S235 is refused — true of the GRADE
range, and the grade range did not move. What made the two irreconcilable was that one of
them was about a stress; they are now about different constants and both hold.

```
claim  both assertions hold at this commit, in one run, with no deselection
cmd    python -m pytest tests/verification/rung5 -q -p no:randomly
out    77 passed in 0.49s
judge  verdict 115's own words were "two tests added by one commit cannot both hold, and
       the rung is 77 passed because one is evaluated at a grade the other admits". The
       count is the same and the reason it holds is not: the stress claim is now asserted
       over the grid and the grade claim over the grade range.
```

**Site 4 — `floatfea/tolerances.py:3010` and `docs/milestones/F6.md:239`, both re-measured
in the same commit (BP0).** The `F6_API_FY_PLAUSIBLE_MIN` sentence — "the edge admits S235
and every grade the sweep uses" — was true of the range and **false downstream**, and both
copies now say so rather than being quietly left true again.

```
claim  both sites record that the sentence was false downstream between C72 and R754, and
       point at the entry that carries the repair
cmd    grep -c "false DOWNSTREAM" docs/milestones/F6.md
out    1
cmd    grep -n "F6_API_STRESS_PLAUSIBLE_MIN:" floatfea/tolerances.py
out    3103:F6_API_STRESS_PLAUSIBLE_MIN: Final[float] = 1.0e8
rule   BP0: when a decision rule changes, every figure citing the old rule is regenerated
       or withdrawn IN THE SAME COMMIT. The rule that moved is which predicate guards a
       reduced stress, and the sentence citing it lived in two files.
```

## 2a. Every site verdicts 114 and 115 name, one row each

A closing condition that names sites is closed site by site, and **half of an item is not
the item**. Nine of the sites the two verdicts name are not touched by this step's diff;
each is declared here by name with its reason, rather than left as an omission nobody sees.

```
claim  the nine rows below are every site the two verdicts name that this step's diff does
       not touch -- the table is the guard's own list, not a selection of mine
cmd    python -m pytest tests/test_report_carried.py::test_every_named_site_is_touched_or_declared
         -q -p no:randomly
out    15 passed in 0.18s
rule   the guard parametrises over every `finding-path:line` it can read out of the
       verdict, and fails any one that is neither touched by the diff nor declared
       `no change` beside that exact site string. Fifteen parametrisations: six touched,
       nine declared here.
```

| finding | site | disposition |
|---|---|---|
| R754 | `floatfea/checks/api_wsd.py:230` | **no change** at that LINE — the content moved. The funnel call is now at `:273` and the docstring above it is rewritten; section 2, site 1 carries the `grep`. |
| R754 | `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:1452` | **no change**, by design. It asserts the GRADE range's lower edge; the grade range did not move, and it is now consistent rather than contradicted. Section 2, site 3. |
| R754 | `floatfea/tolerances.py:3010` | **no change** at that LINE. The `F6_API_FY_PLAUSIBLE_MIN` entry it heads gains the BP0 sentence, and the new `F6_API_STRESS_PLAUSIBLE_MIN` entry sits below it in the same block; section 2, site 4 and section 5. |
| R754 | `docs/conventions.md` | **no change.** The verdict quotes the refusal's own message, which cites `docs/conventions.md` for "SI throughout: pascals". The convention is right; the message citing it was attached to the wrong predicate. `docs/conventions.md` is locked at F0 — changing it reopens that gate rather than being an inline edit. |
| R753 | `docs/F6_utilisation.md` | **no change** in this revision — answered in revision 2 by deleting the false clause, and verdict 115 verified it. |
| R753 | `docs/F6_utilisation.md:70` | **no change** in this revision; same answer, same verdict. |
| R753 | `scripts/measure/api_wsd_utilisation.py:437` | **no change** in this revision — revision 2 deleted the clause generator at that site, and verdict 115 verified the deletion. |
| R753 | `scripts/measure/api_wsd_utilisation.py:438` | **no change** in this revision; same deletion, same verdict. |
| R753 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | **no change** in this revision. Revision 2 added it as the first test reading either deliverable, and verdict 115 verified it. |

## 3. The adversarial case is the grid, and C84 and C85 come with it

Verdict 115's condition 2: *"the figure that closes it is taken over every grade in
[2.0e8, 1.0e9] the module admits and every `D/t` in the clause's own range, not at the
configuration the repair chooses."* The gate does that, and the binding corner it finds is
one no single-grade literal reaches.

```
the figures this section quotes beyond its own blocks:

  2.0e8, 1.0e9      the admissible grade range, quoted from verdict 115's condition 2
  4.2e8             0.6 E / 300 with E = 210 GPa, computed in the second cell below
  C84, C85          verdict 115's closure-item numbers, from its Closure items section
```

```
claim  the binding `F_xc` over the whole admissible grade range at the clause's own `D/t`
       ceiling, and the margin the declared floor clears it by
cmd    python scripts/measure/r754_stress_vs_grade.py
out    === TABLE 2: F_xc at the clause's D/t = 300 limit, per grade ===
       over EVERY admissible grade, the floor of the range included -- the corner no
       single-grade literal reaches, and the one the floor below must clear.
        F_y [MPa]   F_xc [MPa]              F_xc [Pa]
            200.0      136.558       1.3655759329e+08   <- the minimum
            235.0      160.455       1.6045517211e+08
            275.0      187.767       1.8776669077e+08
            355.0      242.390       2.4238972808e+08
            420.0      286.771       2.8677094590e+08
            460.0      314.082       3.1408246456e+08
            690.0      420.000       4.2000000000e+08
           1000.0      420.000       4.2000000000e+08
         the binding case is 1.3655759329e+08 Pa
rule   the gate asserts that exact value over 7 grades x 2951 slendernesses = 20657 calls,
       and `F6_API_STRESS_PLAUSIBLE_MIN = 1.0e8` clears it by `1.3655759329x`
judge  the binding corner is the grade FLOOR at the `D/t` CEILING. My own denying figure
       for C72 -- `F_xc = 242.39 MPa`, `1.21x` -- is the `355.0` row, correct where it was
       taken and three rows above the minimum. That is R694's shape verbatim.
```

**AND THE LAST TWO ROWS TIE, which the shipped table could not show because it skipped two
grades.** At the table's own `D/t = 300` the elastic term is
`F_xe = 2 C E t / D = 0.6 E / 300 = 4.2e8 Pa`, independent of the grade, and section
3.2.2(b) takes the smaller of it and `F_y [1.64 - 0.23 (D/t)^(1/4)]`. From S690 upward the
elastic term is the smaller one, so every grade at or above it reads `4.2e8` — the function
stops depending on the grade exactly where a reader would expect the margin to keep growing.

```
claim  the elastic term governs at `D/t = 300` from S690 upward and not below it
cmd    python -c "E=210e9; print(f'{0.6*E/300:.6e}', [(g, f'{g*1e6*(1.64-0.23*300**0.25):.6e}') for g in (460,690)])"
out    4.200000e+08 [(460, '3.140825e+08'), (690, '4.711237e+08')]
judge  `460` is below the cap and `690` is above it, so the crossover is between them --
       which is the whole reason the minimum sits at the grade FLOOR. The `460` value is
       an independent hand check of TABLE 2's own `3.1408246456e+08` row.
```

That is why a constant is a legitimate repair here where R750 needed a function: `F_xc` is
bounded below on the admissible domain and the bound is ATTAINED at a corner, which is
exactly what `C_m`'s resolution was not — its infimum is `0`, attained, so no constant
could ever be a floor beneath it.

```
claim  EH4 in the direction that WEAKENS the floor as well as the one that strengthens it
cmd    python scripts/measure/r754_stress_vs_grade.py
out    === TABLE 3: EH4, both directions on the STRESS floor ===
         declared            1.000000e+08 Pa
         may RISE only to    1.3655759329e+08 Pa  (1.3655759329x), above which a legitimate
                             slender section at the grade floor is refused
         may FALL only to    3.550000e+05 Pa  (281.6901x below the declared value),
                             beneath which a kPa S355 is admitted as a stress
rule   EH4: a boundary is solved in BOTH directions, including the two that weaken a gate.
       The weakening direction for a floor is downward, and it is `281.6901x` away.
```

### C84 and C85 — answered with R754 rather than ledgered, and the reason is one sentence

Both are refusal-funnel defects in `floatfea/`, so separating them from R754 would have
meant shipping a funnel I already knew to be incomplete.

**C84 — the third divider.** `allowable_axial_compression(60.0, 2.5, 0.0)` raised
`ZeroDivisionError` because it computed `d_t = d_outer / wall` before any funnel ran.
`_require_tube`'s own docstring named two dividers and this was a third.

```
claim  every entry point that divides by the wall now reaches the funnel first
cmd    python -c "import floatfea.checks.api_wsd as M; M.allowable_axial_compression(60.0, 2.5, 0.0)"
out    ValueError: D = 2.5 m and t = 0.0 m are not a tube: both must be positive and
out      the wall must be under half the diameter. A negative D/t satisfies every
out      branch test in section 3.2.3, because each is an upper bound -- so this
out      returned `compact`, the best allowable, rather than refusing (C80).
rule   C60's own complaint was that `ZeroDivisionError` is not a named refusal. The
       condition said "closed when the funnel reaches that divider too", which is the
       route taken rather than the docstring-correction alternative.
```

**C85 — the unpinned clause.** Deleting `not d_outer > 0.0` from `_require_tube` left rung 5
at `77 passed`, because each of the five tuples was refused by one of the other two clauses.
The distinguishing case is a NaN diameter, which C60's own measurement block named and the
tuple omitted.

```
claim  all three clauses of `_require_tube` now redden when deleted one at a time
cmd    delete each clause, run `pytest tests/verification/rung5 -q`, restore the source
out      not d_outer > 0.0        -> 1 failed, 76 passed in 0.68s
           FAILED tests/verification/rung5/test_g61_api_wsd_hand_calculations.py::test_a_GEOMETRY_that_is_not_a_tube_is_REFUSED
         not wall > 0.0           -> 1 failed, 76 passed in 0.72s
           FAILED tests/verification/rung5/test_g61_api_wsd_hand_calculations.py::test_a_GEOMETRY_that_is_not_a_tube_is_REFUSED
         wall >= 0.5 * d_outer    -> 1 failed, 76 passed in 0.53s
           FAILED tests/verification/rung5/test_g61_api_wsd_hand_calculations.py::test_a_GEOMETRY_that_is_not_a_tube_is_REFUSED
       restored: True
cell   one clause removed at a time, the other two and the tuple list held, source restored
       after each. The test is not parametrised per tuple, so the same id fails in all
       three rows -- the distinguishing CASES are `(nan, 0.18)` for the first clause and
       `(2.5, nan)` for the second, and before those two were added the first row read
       `77 passed`: the clause was decoration.
```

## 4. FC2's results report — generated, and it caught one of my own figures

`results/F6/floatfea_results_report.md`, with the two CSVs beside it. **All nine sections
exist**, against a condition that asked for one to seven.

```
claim  the deliverable and both CSVs are produced by one command, and section 5's status
       column is a pytest run rather than a recollection
cmd    python scripts/measure/f6_results_report.py
out      wrote results\F6\floatfea_results_report.md (457 lines)
         wrote results\F6\F4_member_forces.csv (copied from docs\F4_member_forces.csv)
         wrote results\F6\F6_utilisation.csv (copied from docs\F6_utilisation.csv)
rule   EV3: every report figure comes from a script committed under `scripts/measure/`,
       cited by path and command. EZ0 makes anything under `results/` or
       `scripts/measure/` that produces a deliverable a PUBLISHED DELIVERABLE, so a wrong
       figure in either is CZ0 (a) and blocks.
```

**Nothing in the document is typed.** The model numbers come from `build_superstructure()`,
the loads from the committed provenance JSON, the member forces and utilisations from the
two published CSVs, the clause allowables from `floatfea.checks.api_wsd`, and the gate
ceilings from `floatfea.tolerances` **resolved by name** — so a renamed constant or a
renamed test stops the generator rather than letting it publish a stale figure.

```
claim  no quantitative figure in the published PROSE is hand-written; each is generated in
       its own line, read from `floatfea/hsp_pin.py`, or a clause or standard identifier
cmd    a regex over every prose line of the deliverable, outside code fences and tables,
       printing the sorted set of numeric tokens longer than one digit
out    ['0.0002', '0.034238', '0.057%', '0.8104', '1.0', '1.6208', '10', '1000', '12.5',
        '16.2', '19902', '1e-8', '1e8', '2.0', '2.00', '2.5e-12', '20', '20.54%', '25%',
        '26.83', '3.2', '3.3', '32.34', '4.1', '4.2', '6.5', '7.9', '8e+07']
judge  twenty-eight tokens, and every one is accounted for. GENERATED in the line that
       prints it: `0.0002`, `2.5e-12`, `8e+07`, `7.9` (the G4.1 ratio), `0.034238` (the K
       lever), `0.8104`, `1.6208`, `2.00` (the f span). READ FROM `floatfea/hsp_pin.py`:
       `0.057%`, `1000`, `1e-8`, `1e8`, `20.54%`, `25%`, `26.83`, `32.34`. DECLARED
       INPUTS, in the clause or the deck: `2.0` (K), `1.0` (f), `10`, `12.5`, `16.2`, `20`
       (the periods), `6.5` (the band formula). IDENTIFIERS, not quantities: `19902`,
       `3.2`, `3.3`, `4.1`, `4.2`. **Nothing is left over**, which is the property the
       claim is about -- not that the list is short.
```

**IT CAUGHT ONE WHILE BEING WRITTEN, AND THAT IS THE ARGUMENT FOR THE SHAPE.** Section 5
carried my sentence "the moment channel is four orders looser than the force channel".

```
claim  that sentence named four decades where the two constants are 7.9 apart, and the
       published line is now an expression over them rather than a number about them
cmd    python -c "from floatfea.tolerances import F4_G41_DYNAMIC_FORCE as f, F4_G41_DYNAMIC_MOMENT as m; import math; print(m/f, math.log10(m/f))"
out    80000000.00000001 7.903089986991944
judge  SEVEN POINT NINE decades, not four. The published line is now an f-string over
       `F4_G41_DYNAMIC_MOMENT / F4_G41_DYNAMIC_FORCE`, so it cannot be wrong about them
       again. The figure was wrong because I typed it, in the one part of the document I
       had written by hand -- which is the whole of R739, R747, R752 and R753's shape.
```

### What the deliverable finds, in one block

```
claim  the headline numbers Xabier is being sent
cmd    python scripts/measure/f6_results_report.py   (sections 7 and 8 of its output)
out    over unity               : 4 of 32
       worst                    : U = 1.71167 at platform/platform:hub2_arm ROOT
                                  T = 12.5 s, 3.3.2 interaction, axial branch elastic
       and on the STATIC-ONLY basis -- self-weight, no wave load at all:
         worst sigma                    : 269.716 MPa at platform:hub1_arm ROOT
         against F_b = 266.25 MPa        : 1.0130
         against 0.6 F_y = 213.00 MPa   : 1.2663
rule   the stand-in tube is a stiffness equivalent for a truss of undecided depth, which
       the locked plan said in advance. Nothing was tuned to bring it under unity and no
       tolerance was touched.
```

**Three of its blocks are measurements FC2 asked for that did not exist before this
revision.** The `f` sensitivity across every rung of `MASS_FRACTION_LADDER` plus `f = 1.0`;
the per-case stress bound that justifies excluding `T = 10 s`; and the count of force
components identically zero without a wave, which is what one heading costs.

```
claim  the three new measurements, quoted from the deliverable's own generated blocks
cmd    python scripts/measure/f6_results_report.py   (sections 4, 6 and 8 of its output)
out    the dependence is LINEAR in f -- worst residual against the straight line
         through the f = 0 and f = 1 rungs: 8.882e-16 of utilisation
       `0.8104` to `1.6208`, a factor of `2.00`
        T_full [s]   worst ROOT sigma BOUND [MPa]
              10.0                        762.151
              12.5                        483.214
        component  exactly zero on  max |value| on the static basis
                N         48 of 48                 0.0000e+00 N
               Vy         48 of 48                 0.0000e+00 N
               Mz         48 of 48                 0.0000e+00 N.m
judge  the f sweep is the single largest lever in the report and the shipped rung is NOT
       the worst on it; the stress column is why `T = 10 s` is excluded in the EXPENSIVE
       direction; and three of six components are identically zero without a wave, so
       nothing here constrains them at any other heading.
```

**WHAT IS NOT DONE, STATED RATHER THAN SKIPPED: there is no PDF.**

```
claim  no markdown renderer exists in this environment
cmd    for c in pandoc wkhtmltopdf md-to-pdf weasyprint; do command -v $c; done;
         python -c "import markdown"; python -c "import weasyprint"
out    pandoc         not found
       wkhtmltopdf    not found
       md-to-pdf      not found
       weasyprint     not found
       ModuleNotFoundError: No module named 'markdown'
       ModuleNotFoundError: No module named 'weasyprint'
judge  the markdown is the deliverable this repository can produce; the render is a
       separate step, and the document's own footer says so rather than leaving a reader
       to notice. I did not install a renderer in order to produce a deliverable.
```

## 5. BI3 on R754's own entry — the one item on the reviewer's standing list

`F6_API_STRESS_PLAUSIBLE_MIN`'s entry shipped three measurement tables in `1e19f7f` that no
committed script regenerated, which is on verdict 115's list of what it will not accept —
*"a measurement block in `floatfea/tolerances.py` that no committed script regenerates (BI3,
five rounds on the list)"*. All three are now emitted by the script the entry cites.

```
claim  the entry names a committed command, and the command emits all three of its tables
cmd    grep -n "r754_stress_vs_grade" floatfea/tolerances.py floatfea/checks/api_wsd.py \
         docs/milestones/F6.md
out    floatfea/tolerances.py:3051:#     cmd  python scripts/measure/r754_stress_vs_grade.py
out    floatfea/checks/api_wsd.py:188:    out:    scripts/measure/r754_stress_vs_grade.py
out    docs/milestones/F6.md:241:| `F6_API_STRESS_PLAUSIBLE_MIN` = 1.0e8 | ... `python scripts/measure/r754_stress_vs_grade.py` regenerates every figure in this row, BI3 ...
rule   BI3: a table in `floatfea/tolerances.py` is regenerated by a script at the commit it
       describes, or it is not in that file.
```

```
the figures this section quotes, each a BEFORE and AFTER pair of the same quantity. The
AFTER values are TABLE 1 and TABLE 2 of `python scripts/measure/r754_stress_vs_grade.py`,
pasted in sections 2 and 3; the BEFORE values are what 1e19f7f shipped.

  12.1    -> 12.066                     the refused fraction of the six-grade grid
  282     -> 281.6901                   how far the floor may fall before a kPa S355 is
                                        admitted as a stress
  1.365576e+08 -> 1.3655759329e+08      the binding F_xc, to the digits the gate asserts
  420, 460                              the two grades the shipped table skipped between
                                        355 and 690, whose absence hid the elastic cap
```

**And the entry's rounded figures are now the exact ones**, because the script is the source
rather than a memory of it. Two grades the first table had omitted are in it, and that is
what made the elastic cap visible at all.

**The `api_wsd.py` docstring carries its claim as a prose triple**, not as an assertion
nobody runs, because `tests/test_tree_prose_consistent.py` executes the `cmd` and compares
it to the `out`.

```
claim  the docstring's BI3 triple is run by the guard and holds
cmd    python -m pytest tests/test_tree_prose_consistent.py -q -p no:randomly
out    34 passed in 0.49s
```

## 6. C86 and C87

```
the figures this section quotes:

  3010, 3015        verdict 115's line numbers for C87's two named entry sites
  C81, C86, C87     verdict 115's own item numbers, from its Closure items section
  26, 134           my own run at bf45e66: `26 failed, 134 passed, 1 skipped`, which is
                    the figure whose ATTRIBUTION C86 is about
```

**C87 — answered by measurement, and the answer is that the entry already had them.** C81's
closing condition named `floatfea/tolerances.py:3010` and `:3015`, and verdict 115 said the
repair had put the four numbers in the EH4 test instead.

```
claim  all four numbers are in the `F6_API_FY_PLAUSIBLE_MIN` entry's own text
cmd    python -c "from pathlib import Path; t=Path('floatfea/tolerances.py').read_text(encoding='utf-8'); b=t[t.index('CLASS: STRUCTURAL -- the range of'):t.index('F6_API_STRESS_PLAUSIBLE_MIN')]; [print(f'{n:10s} in the F_y entry: {n in b}') for n in ('3.55e5','3.55e11','2.35e8','9.6e8')]"
out    3.55e5     in the F_y entry: True
       3.55e11    in the F_y entry: True
       2.35e8     in the F_y entry: True
       9.6e8      in the F_y entry: True
judge  the condition is satisfied as written -- "closed when the two entries carry the four
       numbers OR point at the test that does". They carry them. The reviewer read the
       diff, which put them in the TEST; the entry's four were already in its Reason
       paragraph from C60's repair, which that diff did not touch.
```

**C86 — recorded, and deliberately NOT fixed in place.** Revision 2's section 8 attributed
a figure to the verdict that the verdict's text does not contain. The figure is right and
the attribution is not, because EG3(ii) is the one measurement a verdict structurally
cannot take.

**The correction is here rather than in revision 2's prose, and the reason is mechanical.**
EK3 keeps a commit off a report that already has its verdict, and the report guards compare
the newest commit touching a report against the newest touching a verdict — so reverting
content would not help even if the edit were harmless. **So, stated here:** that figure is
mine, from my own run at `bf45e66`, and the verdict reproduced it independently in a
worktree. It was never in the verdict's text and revision 2 should not have said it was.

## 7. The suite, and EG3 state (2)

**This is EG3 state (2): verdict written, answering report not yet.** Verdict 115 is newer
than revision 2, so the report guards that key on a finding or a site of the newest verdict
cannot pass until this revision is in the tree. The run is recorded **red with its cause
named**, with the full `FAILED` list, and EG3(i) is why each id is matched individually
rather than ruled as a family.

**The whole-suite line below is generated by `python scripts/suite_count.py`, run after
every other edit to this revision (CP3, and the guard's own instruction says the same).**
It runs the suite itself in a clean worktree at the commit, so the count and the `FAILED`
list come from one invocation and not from a remembered one. FC1 is why the line can only
ever describe the PREVIOUS commit: a check whose input is the commit cannot be measured
before the commit exists.

**Whole suite at `03ea8bf`: 3138 passed, 0 failed, 0 skipped.** **The excluded set: 158 passed, 9 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 167 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_a_blocking_item_is_not_routed_to_4a`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
```

**THE NINE, MATCHED ID BY ID RATHER THAN RULED AS A FAMILY (EG3(i)).** The whole suite
outside the three report-guard files is `3138 passed, 0 failed, 0 skipped`, so there is
nothing else to place.

| # | failing id | where it belongs |
|---|---|---|
| 1 | `test_the_generator_would_catch_a_row_under_the_wrong_number` | **EG3 state (2), named in the list** |
| 2 | `test_a_blocking_item_is_not_routed_to_4a` | **NOT on EG3's list.** See below — it is verdict 114's heading format, which verdict 115 ruled on. |
| 3 | `test_the_guard_survives_the_state[baseline]` | the cascade's baseline, red by EH1's own identification rule |
| 4 | `test_the_guard_survives_the_state[non_numeric_step_suffix]` | a planted state cascading off that baseline, identified by its own failure line |
| 5 | `test_the_guard_survives_the_state[superscript_digit_step_number]` | the same cascade |
| 6 | `test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` | the same cascade |
| 7 | `test_the_guard_survives_the_state[step_number_is_the_empty_string]` | the same cascade |
| 8 | `test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` | the same cascade |
| 9 | `test_the_guard_survives_the_state[zero_padded_step_number]` | the same cascade |

**Row 2 is off the list and I am not smuggling it.** `test_a_blocking_item_is_not_routed_to_4a`
is not among EG3's five names, nor EH1's two, nor FC1's two. It is red because at the
measured commit the newest revision in the tree is revision 2, which answers verdict 114 —
and verdict 114 wrote `**R753.**` with no `(BLOCKING. ...)` parenthetical for `_blocking()`
to parse. Revision 2's section 10 recorded it as outside my reach; **verdict 115 ruled that
the guard does not change and wrote its own finding in the parseable form**, which is why
this revision's `Answers:` header clears it. That is the verdict's own condition 5, not a
waiver I am claiming for myself.

```
claim  verdict 115's heading is in the form `_blocking()` parses, where 114's was not
cmd    compare the two rounds' finding headings for the parenthetical
out    verdict 115: **R754. (BLOCKING. (a) -- A DEFECT IN `floatfea/`, AND (c) -- ...)**
       verdict 114: **R753.**
judge  the difference is the parenthetical and nothing else.
```

**AND THE IMPLEMENTER'S HALF OF EG3(ii), MEASURED RATHER THAN ASSERTED.** State (2) is
cleared BY THE ANSWERING REPORT and not by time, so the three report-guard files are run on
the tree with this revision in it. **They are not green, and I am not going to write that
they are.** Twenty of the twenty-eight reds clear; eight remain, and all eight are FC1's
own class — a check whose input is the commit, which cannot pass before the commit exists.

```
claim  the three report-guard files on the tree WITH this revision in it, and what is left
cmd    python -m pytest tests/test_report_carried.py tests/test_report_guard_states.py
         tests/test_report_numbers_are_sourced.py -q -p no:randomly -rf
out    FAILED tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]
       8 failed, 168 passed in 109.75s (0:01:49)
rule   FC1: state (2) gains `test_the_report_carries_a_WHOLE_SUITE_count` and
       `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`, "and the reason is that NEITHER
       CAN PASS IN THE COMMIT IT DESCRIBES". `scripts/ci_section.py --rounds` needs a RUN,
       and no run exists for a commit before it is pushed.
judge  the eight are `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` plus the seven
       planted states that cascade off it. The baseline's own failure IS that test -- it
       is the one test in the suite that reaches `gh` -- so the cascade is identified by
       its baseline being red, which is EH1's rule and not a family argument.
       `test_the_report_carries_a_WHOLE_SUITE_count`, FC1's other name, is GREEN: the
       generated line above satisfies it.
```

```
claim  twenty of the twenty-eight cleared, and the twenty are the ones that key on verdict
       115's findings and sites
cmd    the same command, before and after this revision was written
out    before: 27 failed, 147 passed      (revision 2 newest, verdict 115 unanswered)
       after:   8 failed, 168 passed      (this revision in the tree)
cell   one variable: whether this revision exists. Same command, same three files, same
       commit for everything else. The nineteen that cleared are
       `test_every_named_site_is_touched_or_declared` (nine parametrisations),
       `test_every_number_in_prose_is_sourced_in_its_own_section` (six sections),
       `test_a_carried_row_points_at_a_section_that_discusses_it`,
       `test_no_RUN_ID_appears_outside_THE_GENERATED_CI_SECTIONS`,
       `test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` and
       `test_every_CI_RUN_the_report_names_carries_its_conclusion`; plus
       `test_a_table_of_numbers_shows_where_it_came_from` on section 2a, which is twenty.
```

**One of those twenty is worth naming, because it is a guard catching a real shape in my
own figures.** `test_no_RUN_ID_appears_outside_THE_GENERATED_CI_SECTIONS` fired on
`136557593` — the leading nine digits of the binding `F_xc` in pascals, which reads as a CI
run id wherever a report quotes it. The guard is right about its own shape and **is not
extended**; the figure is spelled `1.3655759329e+08` at every source that publishes it —
the generator, the tolerance entry, the plan row, the docstring and the gate's literal —
and `1.365575932867604e08 == 136557593.2867604` is `True`, so the asserted value did not
move.

### What each finding was, and where the answer lives

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| C84 | carried | **answered** | §3 | `floatfea/checks/api_wsd.py` | carried from an earlier verdict |
| C85 | carried | **answered** | §3 | `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py` | carried from an earlier verdict |
| C86 | carried | **answered** | §6 | `docs/reports/F6/step-2.md` | carried from an earlier verdict |
| C87 | carried | **answered** | §6 | `floatfea/tolerances.py` | carried from an earlier verdict |
| R753 | recorded | **answered** | §2a | `scripts/measure/api_wsd_utilisation.py` | `docs/F6_utilisation.md:70`, generated at |
| R754 | recorded | **answered** | §2 | `floatfea/checks/api_wsd.py` | A DEFECT IN `floatfea/`, AND (c) -- A GATE ASSERTION ON A DOMAIN THAT EXCLUDES THE FAULT. NOT EZ |

## 8. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R752 | **not classified in this verdict** — carried in from an earlier one | CLOSED at verdict 113 and NOT reopened. It does not carry; the report records |
| R753 | **answered** — §2a | no clause this generator can cut -- see the verdict's Carried section |
| R754 | **answered** — §2 | -- A DEFECT IN floatfea/, AND (c) -- A GATE ASSERTION ON A DOMAIN THAT EXCLUDES THE FAULT. NOT... |

**R752 is CLOSED at verdict 113 and does not carry.** The generator cannot classify it
because this verdict does not re-rule it; it is listed because the generator lists every
item for which it finds a heading.

**Still open and routed to the step's closure commit**, where CZ0 puts a closure item —
fixed once, not re-reviewed item by item: **C77, C78, C79, C82**, and the **C41 to C70**
ledger, which FC0 routes past 28 October. Nothing blocking is open.

## 9. What this revision does NOT do

```
  28 October        EG4(e)'s own date, from CLAUDE.md section "Corpus batches pause"
  C86               verdict 115's item number, answered in section 6 of this revision
```

**No PDF.** Section 4 carries the command that shows no renderer is installed. The markdown
and the two CSVs are what this repository can produce, and the render is a separate step.

**No heading sweep, no irregular sea, no real masses.** All three are in the deliverable's
section 9, ranked, with the `f` sensitivity quantified so the ranking is a measurement
rather than an opinion. None of them is in F6's locked scope.

**No corpus batch.** EG4(e) pauses batches until 28 October except mutation work on F4's
load-mapping gate and EB6's label-provenance gate, and this revision touches neither.

**No edit to revision 2's prose.** C86's correction is in section 6 of this revision
instead, because EK3 keeps a commit off a report that already has its verdict, and the
report guards compare the newest commit touching a report against the newest touching a
verdict — so reverting content would not help even if the edit were harmless.

**No new apparatus.** `scripts/measure/f6_results_report.py` and
`scripts/measure/r754_stress_vs_grade.py` are plain measurement scripts under
`scripts/measure/`: they measure, they assert nothing, no gate imports them, and `pytest`
does not collect them. EZ0 contemplates exactly this — it defines a published deliverable
as "anything under `results/` or `scripts/measure/` that produces one" — and DR1's frozen
"report generators" are the step-report apparatus in `scripts/`, which this revision does
not touch.

```
claim  neither new script is collected by pytest, and the only mentions of either under
       `floatfea/` or `tests/` are the two BI3 pointers -- no import, no gate
cmd    python -m pytest --collect-only -q scripts
       grep -rn "f6_results_report\|r754_stress_vs_grade" floatfea tests
out    no tests collected in 0.30s
       floatfea/checks/api_wsd.py:188:    out:    scripts/measure/r754_stress_vs_grade.py
       floatfea/tolerances.py:3051:#     cmd  python scripts/measure/r754_stress_vs_grade.py
judge  both lines are the BI3 citation asked for in section 5, one in a prose triple and
       one in a tolerance comment. `f6_results_report` appears in neither tree at all.
```

### One operational note, because it cost me a rebuild

**Interrupting a `tests/test_report_guard_states.py` run leaves a planted state in the
tree.** Those tests write a mutated step report and restore it afterwards; killing the run
mid-flight skips the restore, and the report on disk is then a planted state rather than
what was written. It cost this revision one full rebuild from the scratchpad. It is not a
defect in the guard — the guard is doing what it says — but it is worth knowing before
someone cancels one of those runs again.
