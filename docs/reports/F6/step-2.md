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
