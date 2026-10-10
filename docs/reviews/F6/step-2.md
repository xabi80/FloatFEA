# Review — F6 step 2
Reviewed commit: ba1527ed20f87b7d258eea460bb48817e90db102
Verdict: HOLD
**Reviewed commit: `5c71cb4`** (branch `F3`, tree clean when I judged it; my corpus batch 47 is
committed on top as `ba1527e`, which is why the plain `Reviewed commit:` stamp below is not the
commit I judged -- R718's subject, and this bold line is the mechanism.)
Tests: 3293 passed, 9 failed, 0 skipped   (MY OWN run, one invocation, no `-k`, no `--ignore`,
no deselection, `-p no:randomly`, tree clean at `5c71cb4`, `661.77s`. All nine trace to verdict
114's own heading format and section 1 is the trace.)

## Round of 2026-10-09 -- F6 STEP 2 REVISION 2. **ROUND 2 OF THREE. HOLD on one item, and it is inside the repair of an item I asked for.** R753 is answered by the right route. Nine closure items land and the figures reproduce to the digit. **What blocks is that C72's funnel fires on the module's own intermediate at two of the six grades the module declares admissible** -- the question the implementer asked me to attack, and it lands.

**WHY HOLD AND NOT PASS.** `allowable_axial_compression(60.0, 2.5, 0.0125, 235e6)` raises
`ValueError: F_y = 182139402.8186804 Pa is outside the plausible range for structural steel`.
That value is `F_xc`, computed by `local_buckling_stress` from an `F_y` that **is** in pascals,
at a section API section 3.2.2 is written for (`D/t = 200 <= 300`) and at a grade the same
commit asserts must be admitted. Solved: the self-fire starts at `D/t = 138.4383` for S235 and
`248.0006` for S275, and every grade below `292.9167 MPa` fires somewhere inside the clause's
own range. **`12.1%` of the domain the `F6_API_CLAUSE_AGREEMENT` entry declares now raises.**
The gate that denies it is asserted at `FY = 355e6` and nothing else; changing that one literal
to `235e6` reddens it with its own message. R754.

**WHAT IS GOOD, AND IT IS MOST OF IT.** R753 is answered by deletion and deletion was the right
route -- argued in section 4 rather than merely accepted. The published line is now a definition
carrying its own precision, `_CSV_FIGURES` names that precision in one place, and the regression
test reads the count AND the precision against the CSV's own column, so the hole batch 46
recorded is closed by removing the thing that sat in it. Nine closure items are answered and
seven of them were false figures of mine or missing refusals -- which is the right call under
CZ0: a wrong number in a tolerance entry is not prose. C73's repair is the shape worth
repeating: the bound is pinned from above at a solved `138.05`, a measured boundary divided by
the window rule's own floor rather than a second declared constant.

**AND THE IMPLEMENTER IS RIGHT AND I WAS WRONG ABOUT ONE FIGURE.** Verdict 114 called
`platform:hub1_arm` TIP at `191%` "the smallest of those seven". It is the LARGEST. I
reproduced the whole ordered list independently and it is the report's: `16.3%` at
`hub3:buoy8_arm` TIP is the smallest. **WITHDRAWN**, and corrected in batch 47 because batch
46's first entry carries the same error.

**No STOP.** No low rung is red. The verification ladder is GREEN in CI at the code-bearing
commit, rung 5 among it, 77 collected and 0 failed.

## 1. THE NINE REDS -- THEY ARE ALL MINE, AND NEITHER EG3 STATE COVERS THEM

```
claim  the whole suite at the reviewed commit, and what is red
cmd    python -m pytest -q -p no:randomly          (whole suite, tree clean at 5c71cb4)
out    9 failed, 3293 passed, 2 warnings in 661.77s      -- NO SKIPS
out    2  tests/test_report_carried.py
out       test_a_blocking_item_is_not_routed_to_4a
out       test_the_generator_would_catch_a_row_under_the_wrong_number
out    7  tests/test_report_guard_states.py::test_the_guard_survives_the_state[...]
out       baseline, non_numeric_step_suffix, superscript_digit_step_number,
out       draft_suffix_beside_a_step_report, step_number_is_the_empty_string,
out       verdict_amended_after_the_commit_the_report_answers, zero_padded_step_number
judge  **NOTHING UNDER tests/verification, tests/unit OR tests/regression IS RED, AND
       test_the_guard_reads_the_step_being_worked_on PASSES** -- EG3 state (1) cleared at
       the verdict and state (2) cleared at the answering report, both as designed. The two
       states the carve-out describes are EMPTY at this commit.
cmd    the baseline state's own log, read rather than matched by name
out    AssertionError: baseline: expected a clean run.
out      FAILED tests/test_report_carried.py::test_a_blocking_item_is_not_routed_to_4a
out      FAILED tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_
out        the_wrong_number
out      2 failed, 113 passed in 1.39s
out    assert 1 == 0
rule   EH1: the cascade is identified by the baseline being red and by each cascading
       state's own failure line, not by its name
judge  **THE SEVEN CASCADE OFF THE TWO AND THE TWO ARE MINE.** I ran the baseline alone to
       get that log rather than ruling seven reds as a family.
```

**THE CZ0 RULING THE IMPLEMENTER ASKED FOR, AND IT IS THE ONE I WOULD HAVE ASKED FOR.**

**The guard does not change.** It is self-protecting in exactly the way the recorded guard list
asks for -- it reddens when its own parse finds nothing rather than reporting a vacuous pass --
and `tests/test_report_carried.py:368` is one of the few places in this repository where a check
says out loud that it has stopped checking. Loosening it to accommodate a verdict's prose is the
cheapest wrong fix available and I will not have it. **The defect is my own heading format**, the
implementer cannot touch it, and recording it with its cause named in section 10 rather than
working around it is correct. **This verdict's findings are written in the parseable form.**

```
claim  the two reds cannot be cleared retroactively, and that is a property of the guard
cmd    tests/test_report_carried.py:288 and :320
out    VERDICT_TEXT = _verdict_text_at(ANSWERED), which runs
out      git show <ANSWERED>:docs/reviews/F6/step-2.md -- the verdict file AS IT STOOD at
out      the commit the report's own header names, bf45e66
judge  so writing a new round into the same file does NOT change what THIS report revision
       is measured against. **The two are red at the reviewed commit and stay red until
       revision 3 answers this verdict.** They are a designed, self-clearing boundary red of
       a THIRD kind -- caused by the reviewer, clearable only by the reviewer -- and EG3's
       two lists do not name them. **I do not hold on them.** A (d) the implementer is
       forbidden to touch and that I have already fixed in this commit is not a finding
       against the work. Section 7 sends the clause out.
```

## 2. CI -- UNAVAILABLE AT THE REVIEWED COMMIT BY DESIGN, AND THE LADDER IS GREEN WHERE IT MATTERS

```
cmd    gh run list --limit 6 --json databaseId,headSha,conclusion,status,workflowName
out    5c71cb4   NO RUN
out    9af9b75   38017640023   completed   failure
rule   CA2: a workflow that did not run on the reviewed commit is an unavailable check
cmd    head -30 .github/workflows/ci.yml
out    on: push: paths-ignore: - "docs/reports/**"
cmd    git diff --stat 9af9b75..5c71cb4
out    docs/reports/F6/step-2.md | 33 +++    (nothing else)
judge  **UNAVAILABLE BY DESIGN, AND THIS IS NOT CK2.** `5c71cb4` is report-only and CO3's
       `paths-ignore` excludes `docs/reports/**` deliberately. It is not the
       allowance-exhausted state either: `38017640023` is a real eleven-minute run on a real
       runner with no spending annotation. `9af9b75` is byte-identical to `5c71cb4` under
       `floatfea/`, `tests/` and `scripts/`, so its result describes the tree I judged for
       everything except the report guards -- which read the report, and are the one thing
       that moved.
cmd    gh run view 38017640023 --json jobs
out    the verification ladder            success     02:37:29 -> 02:40:58
out    lint, unit and guards              failure     02:37:29 -> 02:48:25
out    CI determinism -- leg / ten legs   skipped     (workflow_dispatch only, CK0)
cmd    each rung's own run_rung line
out    ladder 1  1276 collected, 0 failed      ladder 2    66 collected, 0 failed
out    ladder 3   300 collected, 0 failed      ladder 6   144 collected, 0 failed
out    ladder 4   343 collected, 0 failed      ladder 5    77 collected, 0 failed
cmd    the lint job's steps, and the guard step's own summary
out    actionlint, ruff, black --check, mypy, unit tests     all success
out    step 10 "guards and meta-tests"   failure
out    10 failed, 995 passed, 1 skipped, 1 warning in 614.79s (0:10:14)
out    the nine I measured, plus test_the_report_carries_a_WHOLE_SUITE_count
judge  **THE LADDER IS GREEN ON UBUNTU WITH RUNG 5 AMONG IT**, so the new `_require_tube`
       and `_require_plausible_fy` counter-cases and the bit-exact tie equality all hold on
       a second libm. The tenth red is the line `5c71cb4` exists to clear and that cannot be
       measured before the commit carrying it exists -- CZ1's own reusable half, and the
       report says so in those terms in section 11. **The red CI job is my heading format
       plus one CZ1-class line, and nothing else.**
```

## 3. MY OWN INSTRUCTIONS, THE CONFTEST, THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
cmd    git diff --stat bf45e66..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
judge  CH2/CI0: no conftest and no plugin in the range, so rung 5's green is a pytest result
       and not a record rewritten from the rung's own directory.
cmd    git diff --stat bf45e66..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
judge  **NO STOP-CLASS FINDING.** My instructions are untouched in this range. C45 is still
       open and still bites: the agent definition I was invoked with carries the UNAMENDED
       head "(a) a defect in floatfea/", so the criterion I rule under lives in
       `CLAUDE.md:152` and in the invocation, not in my own instructions. Third verdict
       running; section 7.
cmd    git diff bf45e66..HEAD -- floatfea/tolerances.py
out    +21 -7, COMMENTS ONLY
cmd    git diff bf45e66..HEAD -- floatfea/tolerances.py | grep -E "^[+-].*Final\[float\]"
out    (none)
cmd    git diff bf45e66..HEAD | grep -E "^\+.*(xfail|skipif|pytest.skip|deselect|--ignore|addopts)"
out    (none)
cmd    git diff --stat bf45e66..HEAD -- pyproject.toml .github scripts/run_rung.sh
out    (empty)
judge  **NOTHING WAS WIDENED AND NOTHING STOPPED ASSERTING.** No `Final[float]` line is
       touched on either side, no marker, no deselection, no workflow change. So the entries
       that moved are entries whose JUSTIFICATION moved with the value held -- which EU1
       calls the WORST case for an adversarial check and not the safest -- and sections 4 to
       6 are that check, at configurations the diff did not choose.
```

## 4. R753 -- THE DELETION ROUTE WAS THE RIGHT ONE, AND I ARGUE IT RATHER THAN ACCEPT IT

The implementer asks whether the first route was available and the lazy one was taken. **It was
not available in a form I would have accepted, and the reason is in my own closing condition.**

```
claim  the true characterisation coincides with the count only CONTINGENTLY
cmd    recompute both forms on all 17 compression rows from the CSV's own columns
rule   my condition: "governing == 3.3.2 interaction AND the move exceeding six figures
       gives exactly 10 of 17, where the overtake alone gives 17"
out    amplified(C_m = 1.0) > simple                        : 17 of 17
out    ... and amplified(0.85) did NOT                      : 10 of 17
out    C_m moves the governing U at 6 significant figures   : 10 of 17
out    the tightest of the ten overtakes: 0.1153%  (both over-unity platform ROOTs)
judge  **MY OWN CONDITION NAMED A CONJUNCTION AND THE IMPLEMENTER FOUND THE BETTER
       OBJECTION TO IT.** The stricter predicate is `10 of 17` and does coincide with the
       count -- but the coincidence is contingent at one part in a thousand, which verdict
       113 measured and verdict 114 repeated. A published clause computed from a set that
       coincides with the count only while a 0.1153% margin holds is a sentence that will be
       false at the next load case and nothing would say so. **Deletion is not the lazy
       route; it is the one that leaves no claim that can rot.** Both routes were offered
       and the second is the better one.
```

```
claim  the repair is site by site, the deliverable is regenerated in the same commit, and
       what is left is checkable by the file's own reader
cmd    git show 9af9b75 --stat -- docs/F6_utilisation.md scripts/measure/api_wsd_utilisation.py
out    both in ONE commit: docs/F6_utilisation.md | 2 +- ; the generator | 33 +-
cmd    sed -n 70p docs/F6_utilisation.md
out    C_m visibly moves the governing U on 10 of 17 compression rows, at the 6 significant
out      figures this file publishes
cmd    the count, recomputed from the CSV's own two columns at six figures, by me
out    10 of 17        <- and the raw-float count is 12 of 17
cmd    the CSV's own writer format, and the field the count is taken on
out    {:.6g} ; utilisation_K2 is `locked.utilisation`, the GOVERNING U, so "the governing
out      U" is the right name for it and BP0's rule-mismatch is gone
judge  **BP0 SATISFIED: the figure and the sentence now carry the SAME rule.** The clause
       stated a relation between `amplified` and `simple` (which is `u_combined`) beside a
       count measured on the governing `U`; there is no clause left and the sentence names
       the quantity, the set and the precision. `_CSV_FIGURES` is the single place the 6
       lives and both the sentence and the test read it -- C67 discharged where it became
       load-bearing.
cmd    the regression test's new regex, and what it now asserts
out    r"C_m visibly moves the governing U on (\d+) of (\d+) compression rows, at the
out      (\d+) significant figures"  -- three groups
out    assert int(group(3)) == 6 ; assert (group(1), group(2)) == (visible, len(rows))
judge  **THE HOLE IS CLOSED BY REMOVING WHAT SAT IN IT.** My section 7 measurement at
       `02b7daf` was that rewriting everything after the double dash to "the moon is made of
       cheese" left `10 passed`. There is nothing after the double dash now, and the
       precision -- the one part of the sentence a reader could not otherwise check -- is
       asserted against the writer's own format.
```

## 5. C72 -- THE FUNNEL IS RIGHT ABOUT ITS REACH AND WRONG ABOUT ITS DOMAIN. THIS IS R754.

**THE REACH FIRST, BECAUSE IT IS GOOD.** The eight-entry-point funnel is real and it is pinned
per entry point, which is the thing I would have doubted.

```
rule   one edit at a time, whole rung 5 re-run after each, source restored and the
       restoration asserted by re-reading the file and by git status --porcelain;
       baseline 77 passed
out    delete _require_plausible_fy from allowable_shear alone     KILLED  1 failed
out    delete _require_tube from local_buckling_stress alone       KILLED  1 failed
out    MARGIN_MAX 2.0 -> 138.0                                     SURVIVES 77 passed
out    MARGIN_MAX 2.0 -> 139.0                                     KILLED  1 failed
out    swap the two aggregation helpers' bodies                    KILLED  5 failed
out      ... and the EH4 test alone under that swap                KILLED  1 failed
out    delete `not d_outer > 0.0` from _require_tube               SURVIVES 77 passed
judge  the funnels carry their own failure at the individual call site, which is what the
       eight-call dict buys and what a single smoke test would not have.
```

**AND HERE IS WHERE IT BREAKS, WHICH IS THE QUESTION I WAS ASKED.**

```
claim  the refusal fires on a value this module computed, at a grade the module admits
cmd    allowable_axial_compression(60.0, 2.5, D/dt, fy) over SEVEN grades x ELEVEN D/t
       values -- a grid the diff did not choose
rule   the module's own declared admissible set: F_y in [2.0e8, 1.0e9] Pa, and API section
       3.2.2's own D/t <= 300, which this function refuses past by name
out    fy = 235 MPa : REFUSED at D/t = 140, 160, 180, 200, 240, 280, 300
out    fy = 275 MPa : REFUSED at D/t = 280, 300
out    fy = 300/355/420/460/690 MPa : no refusal anywhere in range
out    the raise, verbatim:
out      ValueError: F_y = 182139402.8186804 Pa is outside the plausible range for
out      structural steel [2e+08, 1e+09] Pa. ... this argument's UNIT decides which branch
out      a section lands in -- S355 entered as 355e3 reads a D/t = 100 tube as `compact`.
out      SI throughout: pascals (docs/conventions.md).
cmd    the boundary, SOLVED by bisection on the module's own F_xc rather than sampled
out    S235 : refusal starts at D/t = 138.4383   (54.8% of its declared D/t range)
out    S275 : refusal starts at D/t = 248.0006   (17.6%)
out    the grade boundary: every F_y below 292.9167 MPa fires somewhere inside D/t <= 300
out    over the six grades the agreement entry declares: 12.1% of the grid now RAISES
judge  **THE VALUE THAT TRIPS IT IS `F_xc`, NOT AN `F_y`**, and `F_xc` is a REDUCED stress
       while `F_y` is a GRADE -- so a plausible-grade range is the wrong predicate for it.
       The unit is correct, the input is correct, the computation is correct, and the
       diagnostic a caller reads says the unit is wrong.
```

**AND THE GATE THAT DENIES IT IS ASSERTED AT ONE GRADE. HERE IS THE ABLATION, ONE LITERAL.**

```
claim  test_the_INTERNAL_F_xc_call_stays_inside_the_range_at_every_admissible_section
       cannot contain the fault
cmd    its only grade literal, 355e6 -> 235e6, and nothing else; that test alone
rule   the test's own name: "at EVERY admissible section"
out    1 failed
out    AssertionError: F_xc at the clause's own D/t = 300 limit is 1.604552e+08 Pa, below
out      the plausible-F_y floor 2.000000e+08. The internal substitution would then refuse
out      a value this module computed, which is the refusal firing on itself rather than on
out      a caller's unit error.
out    assert 160455172.11194348 > 200000000.0
judge  **THE GATE'S OWN MESSAGE IS THE FINDING, WORD FOR WORD, AND THE GATE IS RIGHT.** Its
       domain is one grade. That is the recorded assertion-domain-blindness shape: the
       collection the assertion inspects cannot contain the fault.
cmd    the same commit's OTHER new test, at :1452
out    assert F6_API_FY_PLAUSIBLE_MIN < 235e6   # "the low edge may rise only to 2.35e8
out      before S235 is refused"
judge  **TWO TESTS IN ONE COMMIT THAT CANNOT BOTH HOLD**, and the whole rung is 77 passed
       because one of them is evaluated at a grade the other one admits.
cmd    which shipped parametrisation would have caught it
out    the local-buckling and axial parametrisations run at 355e6 and 690e6 only; 275e6
out      appears on the tension and shear clauses, which do not call
out      column_slenderness_parameter
judge  the gate is green and the module is not. The production path is unaffected -- F6
       ships S355 at D/t = 13.9 and no published number moves -- but (a) is a defect in
       `floatfea/` and does not require one to.
```

## 6. C80's FUNNEL -- IT CANNOT REFUSE A SECTION THE CLAUSE ADMITS, AND I CHECKED THE OTHER DIRECTION TOO

The implementer flags this as the one it is least sure of. **It is clean, and the solved
boundary is why.**

```
claim  `_require_tube` removes nothing API section 3.2.3 is written for
cmd    section_class over the admissible D/t range, and either side of the new boundary
rule   the funnel refuses D <= 0, t <= 0, or t >= D/2
out    D/t = 2.0002  ->  compact        D/t = 2.0000  ->  REFUSED "not a tube"
out    D/t = 5.0, 13.8889, 300.0  ->  compact / compact / reduced_2
out    the bending clause's own ceiling: limit_3 = 845.0704 at S355
judge  **THE ONLY GEOMETRIES REMOVED ARE D/t <= 2**, which is a solid or inverted section
       and not a tubular. The agreement sweep starts at `D/t = 5.00` and the shipped section
       is `13.9`, so nothing the clause or the gate uses is near it. `t >= D/2` is a
       judgement rather than a clause requirement and it is the right one: at `t = D/2` the
       annulus closes.
cmd    the C80 cases, through all four functions
out    (2.5, 0.0)   section_class / local_buckling / allowable_bending : ValueError
out    (-2.5, 0.18) all three : ValueError      (0.0, 0.18) all three : ValueError
out    (nan, 0.18)  all three : ValueError      <- was branch 'slender'
judge  the one-sidedness C80 named is gone on those three functions.
```

**TWO RESIDUALS, BOTH CLOSURE CLASS, BOTH NAMED RATHER THAN WAVED THROUGH.**

```
claim  a THIRD divider walks past the funnel
cmd    allowable_axial_compression(60.0, 2.5, 0.0)
out    ZeroDivisionError: float division by zero
rule   the funnel's own docstring: "section_class and local_buckling_stress both divide by
       wall, and a refusal in one of two dividers is a refusal a caller can walk past"
judge  `allowable_axial_compression` computes `d_t = d_outer / wall` BEFORE calling
       `local_buckling_stress`, so it is a third divider and the docstring's list of two is
       complete about two and incomplete about three. `ZeroDivisionError` "rather than a
       named refusal" was C60's own complaint. C84.
cmd    delete `not d_outer > 0.0` from the predicate; whole rung 5
out    77 passed      <- the clause is UNPINNED
cmd    each of the test's five tuples under the weakened predicate
out    (-2.5, 0.18) caught by 0.18 >= -1.25 ; (0.0, 0.18) caught by 0.18 >= 0.0 ;
out      the other three by `not wall > 0` or by `t >= D/2`
out    (nan, 0.18) is NOT caught -- and nan is not in the tuple
judge  three clauses, five cases, and one clause no case distinguishes. The case that would
       pin it is the case C80's own measurement block named and the list leaves out. C85.
```

## 7. ON THE CRITERION -- I WAS ASKED, AND I HAVE TWO THINGS TO SEND OUT

I applied CZ0 as amended by EZ0 and I agree with it. **R754 is inside `(a)` without needing the
EZ0 amendment at all**: it is a defect in `floatfea/checks/api_wsd.py`, in a public clause
function, and it is also `(c)` -- a gate asserting a property on a domain that excludes the
fault. I did not need to reach for a published deliverable and I am saying so, because the last
three rounds all turned on the amendment and this one does not.

**AND I AGREE WITH THE IMPLEMENTER'S ORDERING, WHICH IT ASKS ABOUT DIRECTLY.** Two rounds on
the blocker and nine false figures, with FC2's results report pushed to round 3, is the right
order. A results report built on nine wrong figures is a deliverable that has to be resent, and
EZ0 exists because this project has already sent one. **The cost is real and it has to be said
with a number beside it:** round 3 is the last round, FC2's nine sections do not exist, and
R754 now carries into it. If revision 3 lands both, the step closes on 9-10 October against a
22 October working target. If it lands one, **the choice is slip the working target to the
committed 28 October, or reduce FC2's scope to sections 1 to 7 and send the draft** -- and FC2
already asks for the draft at sections 1 to 7, so the second is the cheaper half of its own
directive. That is the escalation CLAUDE.md asks for when a step is at risk of closing carrying
a blocking item, and it is stated now rather than when the step closes.

**THE TWO THINGS FOR XABIER, and I say each once.**

* **C45, third verdict running.** My own agent definition carries the UNAMENDED head "(a) a
  defect in `floatfea/`", so the criterion I rule under lives in `CLAUDE.md:152` and in the
  invocation's instruction. I ruled under EZ0 because I was told to; the next reviewer may not
  be. One standalone `process:` commit. FC0 routes it past 28 October and I think that is the
  wrong side of the date for it.
* **EG3 NEEDS A THIRD STATE, and this round is its first instance.** The carve-out names state
  (1) (report written, verdict not yet) and state (2) (verdict written, answering report not
  yet). Both are EMPTY at this commit and the tree is still red, because the verdict's own
  prose format broke two guards that read the verdict at the commit the report names. **The
  implementer cannot clear it and I cannot clear it retroactively** -- `_verdict_text_at` reads
  `git show <ANSWERED>:...`, so only the next revision's own header moves it. One sentence:
  *a red whose cause is a verdict's own text, named with the parse that failed, is state (3),
  and it clears at the revision that answers the verdict which fixes the format.* I am not
  asking for apparatus; the guard stays exactly as it is.

## 8. THE EH4 TEST -- I WAS ASKED TO RULE AND IT IS THE NICE PROPERTY, NOT AN OVER-COUPLING

```
claim  the margin bound is now pinned from ABOVE, and the ceiling is SOLVED not sampled
cmd    bisect F6_API_COUNTER_MARGIN_MAX against the new test
rule   EH4: the ceiling falls toward the clean value AND the injection rises until a clean
       case trips -- both directions
out    138.0  ->  77 passed          139.0  ->  1 failed, 76 passed
out    the solved ceiling: strongest/COUNTER = 276.1x divided by F4_WINDOW_RULE_MIN_EDGE
out      = 138.05, and at 300.0 verdict 114 measured 72 passed
judge  **IT IS THE NICE PROPERTY AND HERE IS THE TEST THAT SEPARATES THE TWO READINGS.** An
       over-coupling would be a bound held against another DECLARED constant -- the regress
       the window rule exists to stop. This ceiling is a MEASURED quantity, `strongest /
       COUNTER`, divided by the floor the window's own two edges are already held to. It
       moves when the response moves, which is what a boundary should do, and it is not a
       number anyone chose. C73 is answered in the quantity rather than in the value, which
       is the second time this step that has been the right shape.
cmd    and the obvious attack on it: the ceiling is computed from `_worst_move`, the same
       helper C58's substitutions target
out    swap the two helpers' bodies -> 5 failed over rung 5, and 1 failed with the EH4 test
out      run ALONE
judge  so the EH4 test is an ADDITIONAL killer of that substitution rather than a hole in
       it. A test whose threshold is computed from the helper under attack can still see the
       attack here, and I measured it rather than reasoning about it.
```

## 9. THE REPORT'S OWN FIGURES -- I CHECKED EVERY BLOCK IT NAMES

```
claim  section 2's overtake table
out    17 of 17 / 10 of 17 / 10 of 17, and the ordered seven: 16.3, 16.3, 28.8, 28.8,
out      32.2, 191.0, 191.0 percent        REPRODUCES EXACTLY, mine was the wrong one
claim  section 4's eight-entry-point table and the F_xc row
out    all eight refuse at 355e3 / 355.0 / 355e9 / 0.0 and accept 355e6  REPRODUCES
out    F_xc at D/t = 61 / 100 / 200 / 300 = 354.01 / 324.00 / 275.15 / 242.39 MPa, margin
out      1.2119x at the limit                                            REPRODUCES
out    **and the sentence under it -- "so widening the D/t limit cannot silently make the
out      refusal fire on the module's own intermediate" -- is FALSE at S235. R754.**
claim  section 5's before/after on the geometry refusal
out    reproduced through all four functions; the (nan, 0.18) row is now refused too
claim  section 6's five corrections
out    C71: D/t = 100 -> compact/F_b = 1.205880101 ; D/t = 300 -> 1.761153975  EXACT
out    C75: both halves 1 (hub1:buoy1_arm TIP, f_b = 4.65871e-08 MPa)        EXACT
out    C74: by-assertion attribution reproduced, one at a time                EXACT
out    C83: My = 12633843.95 -> amplified 0.09426368986817012 ; the exact crossing ->
out      simple 0.09426368988411232                                          EXACT
out    C76: the overtake alone on 17 of 17                                   EXACT
claim  section 7's three EH4 boundaries
out    138.05 solved by me (138.0 green, 139.0 red); 3.55e5 and 3.55e11 are verdict 114's
out      own and unchanged                                                   REPRODUCES
claim  section 8's trace and its EG3(ii) count
cmd    at bf45e66, tree clean, in a detached worktree: the three report-guard files
out    26 failed, 134 passed, 1 skipped in 126.31s           REPRODUCES TO THE TEST
claim  section 11's whole-suite line and the ten
out    mine at 5c71cb4 is 9 failed, 3293 passed, 0 skipped; the report's at 9af9b75 is
out      3135 + 154 passed, 10 failed, 1 skipped. The difference is the WHOLE_SUITE line
out      itself plus the parametrisations the added section creates
judge  **EVERY FIGURE IN THE REVISION REPRODUCES EXCEPT ONE SENTENCE, AND THAT SENTENCE IS
       R754.** Two records to correct, neither blocking.
cmd    grep -c "26 failed" docs/reviews/F6/step-2.md
out    0
judge  section 8 says "THE VERDICT'S OWN FIGURE REPRODUCES EXACTLY" of `26 failed, 134
       passed, 1 skipped`. **The number is right -- I reproduced it in a worktree at
       bf45e66 -- and verdict 114 does not contain it**, because EG3(ii) is precisely the
       measurement no verdict can take: I run at the judged commit before writing. The
       attribution is the false half. C86.
cmd    the CX0 repair the implementer flags against itself
out    section 11's block runs `gh run list` and names no run id; `38017640023` appears
out      only in the generated section 0a of the NEXT revision, as CX0 requires
judge  correct, and self-reported. C77's lesson did take on the second try.
```

## Findings

**ONE BLOCKS.**

**R754. (BLOCKING. (a) -- A DEFECT IN `floatfea/`, AND (c) -- A GATE ASSERTION ON A DOMAIN THAT EXCLUDES THE FAULT. NOT EZ0, NOT A DELIVERABLE: PLAIN (a).)**
`floatfea/checks/api_wsd.py:230` (`column_slenderness_parameter`'s new
`_require_plausible_fy(fy)` call) reached through `floatfea/checks/api_wsd.py:293`
(`allowable_axial_compression`'s `F_xc` substitution), with the denying gate at
`tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:1398` and the contradicting
assertion at `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:1452`.
**C72's funnel fires on a value the module computed for itself, at a grade and a section the
module and the locked plan both declare admissible.**

```
cmd    allowable_axial_compression(60.0, 2.5, 0.0125, 235e6)
out    ValueError: F_y = 182139402.8186804 Pa is outside the plausible range for structural
out      steel [2e+08, 1e+09] Pa. ... this argument's UNIT decides which branch a section
out      lands in -- S355 entered as 355e3 reads a D/t = 100 tube as `compact`. SI
out      throughout: pascals (docs/conventions.md).
```

The argument is `F_xc`, which `local_buckling_stress` computed from `fy = 235e6` -- in pascals,
correctly -- at `D/t = 200`, inside API section 3.2.2's own `D/t <= 300`. **Solved rather than
sampled:** the self-fire begins at `D/t = 138.4383` for S235 and `248.0006` for S275, and every
`F_y` below `292.9167 MPa` fires somewhere inside the clause's range. Over the six grades the
`F6_API_CLAUSE_AGREEMENT` entry declares its sweep across, **`12.1%` of the grid now raises.**
`F_xc` is a reduced stress and `F_y` is a grade, so a plausible-grade range is the wrong
predicate for it; the unit is right and the diagnostic says the unit is wrong.

**The gate the commit added to deny this is asserted at one grade.** Its name is
`test_the_INTERNAL_F_xc_call_stays_inside_the_range_at_every_admissible_section`; its only
grade literal is `FY = 355e6`; **replacing that one literal with `235e6` reddens it with its
own message** -- "F_xc at the clause's own D/t = 300 limit is 1.604552e+08 Pa, below the
plausible-F_y floor 2.000000e+08. The internal substitution would then refuse a value this
module computed, which is the refusal firing on itself rather than on a caller's unit error."
The gate is correct and its domain cannot contain the fault. **The same commit asserts at
`:1452` that `F6_API_FY_PLAUSIBLE_MIN < 235e6` because "the low edge may rise only to 2.35e8
before S235 is refused"** -- so two tests added by one commit cannot both hold, and the rung is
`77 passed` because one is evaluated at a grade the other admits. No shipped
G6.1 parametrisation reaches it: the local-buckling and axial branches run at `355e6` and
`690e6` only.

The production path does not move -- F6 ships S355 at `D/t = 13.9`, the deliverables are
byte-identical, and no published number changes -- and `(a)` does not require that it does.
`docs/milestones/F6.md:239` and `floatfea/tolerances.py:3010` both still say the edge admits
S235 and every grade the sweep uses, which is now false downstream of the same constant (BP0).
`floatfea/checks/api_wsd.py:230`'s docstring -- "`F_y` here is `F_xc` ... and is therefore
already inside the range" -- is the only written justification for putting the refusal on that
function, and it is false at S235 (CW0, and the "therefore" is BG0's half with no cell).

**Closed when** the internal substitution no longer passes through a plausible-GRADE predicate
-- either `column_slenderness_parameter` takes the stress it is actually given and the refusal
stays on the public `F_y` entries, or the admissible lower edge for a REDUCED stress is derived
as the function of grade and `D/t` that it is, with a floor beneath every admissible
configuration in the R694 shape -- **and the gate at `:1398` is asserted over the grade set
`:1452` admits**, so the two tests cannot disagree. The refusal's message is corrected where it
now misattributes a unit, and `docs/milestones/F6.md:239` and the `tolerances.py` entry are
re-measured in the same commit (BP0).

**NOTHING ELSE BLOCKS.** I ruled every other candidate against CZ0 (a)-(d):

* **(a)** R753's repair is correct and the deliverable regenerates from the committed
  generator. `_require_tube` refuses nothing API section 3.2.3 is written for -- solved at
  `D/t = 2.0002` admitted, `2.0000` refused -- and it fixes the unsafe direction C80 named: a
  sign slip returned `compact`, the best allowable in the clause. The two residuals are C84
  (`allowable_axial_compression` divides before the funnel and still raises
  `ZeroDivisionError`) and C85 (one of the funnel's three clauses is unpinned), both closure
  class and both measured.
* **(b)** **no tolerance value moved.** `git diff -- floatfea/tolerances.py` is `+21 -7` and
  touches no `Final[float]` line on either side. Two entries' JUSTIFICATIONS moved with their
  values held, which is EU1's worst case, so the adversarial case applies and sections 5, 6 and
  8 are it. `F6_API_COUNTER_MARGIN_MAX = 2.0` is now pinned from above at a solved `138.05` and
  that is the right form for it.
* **(c)** fifteen assertions hold under one-at-a-time edits including the two funnel deletions
  and the helper swap; the one gate whose claim exceeds its domain is `:1398` and it is inside
  R754.
* **(d)** nine reds, all nine traced by name in section 1 to verdict 114's heading format and
  the cascade off it. The ladder is green in CI, rung 5 among it. Neither EG3 state covers
  these nine, they are not clearable by the implementer, and section 7 asks for the clause.

## Closure items

Verdict 114's list ended at C83, so this one starts at C84. **C41 to C70 remain open and FC0
routes C41 to C65 past 28 October.** Of verdict 114's thirteen, **nine are answered in this
revision and I verified each** -- C71, C72 (reach yes, domain no; R754), C73, C74, C75, C76,
C80, C81, C83 -- leaving C77 (answered in section 8 of the report), C78, C79 and C82 for the
step's closure commit. Fixed once in the closure commit, not re-reviewed item by item, and the
step is not held on one.

* **C84.** `floatfea/checks/api_wsd.py:293`. `allowable_axial_compression(60.0, 2.5, 0.0)`
  raises `ZeroDivisionError: float division by zero`, because it computes
  `d_t = d_outer / wall` before calling `local_buckling_stress`. It is a THIRD divider, and
  `_require_tube`'s own docstring names two -- "a refusal in one of two dividers is a refusal a
  caller can walk past" is the right principle with an incomplete list. `ZeroDivisionError`
  rather than a named refusal was C60's own complaint. **Closed when** the funnel reaches that
  divider too, or the docstring's list is the complete one and the omission is stated.
* **C85.** `floatfea/checks/api_wsd.py:181`. Deleting `not d_outer > 0.0` from `_require_tube`
  leaves rung 5 at `77 passed`: each of the five tuples in
  `test_a_GEOMETRY_that_is_not_a_tube_is_REFUSED` is still refused by one of the other two
  clauses -- `(-2.5, 0.18)` by `0.18 >= -1.25` and `(0.0, 0.18)` by `0.18 >= 0.0`. The case
  that distinguishes it is `(nan, 0.18)`, which C60's own measurement block named and the tuple
  omits. **Closed when** the tuple contains a case only that clause refuses, or the reach is
  recorded beside the test.
* **C86.** `docs/reports/F6/step-2.md` section 8. "THE VERDICT'S OWN FIGURE REPRODUCES EXACTLY"
  of `26 failed, 134 passed, 1 skipped`. **The figure is right** -- I reproduced it to the test
  in a worktree at `bf45e66` -- and `grep -c "26 failed" docs/reviews/F6/step-2.md` is `0`,
  because EG3(ii) is the one measurement a verdict structurally cannot take. **Closed when**
  the sentence attributes the figure to the run that produced it rather than to the verdict.
* **C87.** `floatfea/tolerances.py:3010` and `:3015`. C81's closing condition named the ENTRY
  and the repair put `3.55e5`, `3.55e11`, `2.35e8` and `9.6e8` in the EH4 test instead. The
  test is the better place for the assertion and the entry is where the condition pointed, and
  a closing condition that names sites is closed site by site. **Closed when** the two entries
  carry the four numbers or point at the test that does.
* **WITHDRAWN, by me: the top-ten ordering item.** Verdict 114 listed "a top-ten list whose
  order depends on row order among equal values" as still live. Measured over the sixteen
  worst-per-member candidates, rank 10 is `hub4:buoy11_arm` ROOT at `0.788204` and rank 11 is
  `hub2:buoy5_arm` ROOT at `0.776563` -- **a `1.5%` gap, so the published SET is well defined**
  and only the within-pair order of four physically symmetric pairs is arbitrary. Recorded in
  batch 47; it is not a condition on revision 3.
* **R735, R736, R738, C34 to C40, the `0.2240`/`0.2239` item, R712 to R717, C2 to C15, C24 to
  C33, C41 to C70, C77 to C79, C82** -- still open, carried as a list, not re-reviewed item by
  item. **C45 still needs its own standalone `process:` commit** and section 7 is the third
  verdict running to say so.

## Tolerances touched

```
cmd    git diff bf45e66..HEAD -- floatfea/tolerances.py
out    +21 -7, COMMENTS ONLY in two entries; no name added, no name removed
cmd    git diff bf45e66..HEAD -- floatfea/tolerances.py | grep -E "^[+-].*Final\[float\]"
out    (none)
cmd    git diff bf45e66..HEAD | grep -E "^-.*(e-1[0-9]|= [0-9])" | grep -v "^---"
out    the only matches are prose lines inside the two rewritten comments
cmd    git diff bf45e66..HEAD | grep -E "^\+.*(xfail|skipif|pytest.skip|deselect|--ignore)"
out    (none)
judge  **NO VALUE MOVED AND NOTHING STOPPED ASSERTING.** EU1 applies in its hardest form:
       two justifications were re-derived with their values held, which EU1 names as the
       worst case rather than the safest, and the adversarial case is sections 5, 6 and 8 --
       seven one-at-a-time edits and a seven-grade by eleven-slenderness grid, at
       configurations the diff did not choose. **It is the grid that found R754, not the
       diff.**
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F6_API_COUNTER_MARGIN_MAX` | `2.0` | unchanged | dimensionless, STRUCTURAL; a bound on a MARGIN | none, correctly (AO2) | `floatfea/tolerances.py:2963-3002`; `docs/milestones/F6.md:238` | **UNMOVED, AND NOW PINNED FROM ABOVE AT A SOLVED `138.05`.** I bisected it: `138.0` gives `77 passed`, `139.0` gives `1 failed`. The ceiling is `strongest/COUNTER = 276.1x` divided by `F4_WINDOW_RULE_MIN_EDGE`, i.e. a MEASURED boundary over the floor the window's own edges are held to -- not a second declared constant, so it is not the regress the window rule exists to stop. C73 answered in the quantity. The entry's by-assertion attribution table reproduces one edit at a time. |
| `F6_API_FY_PLAUSIBLE_MIN` | `2.0e8` | unchanged | pascals, STRUCTURAL; a refusal threshold on an INPUT | none, correctly (AO2) | `floatfea/tolerances.py:3004-3027` | **UNMOVED, THE `1.76x` IS FIXED, AND THE VALUE IS NOW LOAD-BEARING SOMEWHERE IT WAS NOT.** C71's repair is exact: `1.205880101064237` at the `D/t = 100` the sentence names, and `1.761153975` is the `D/t = 300` figure, both reproduced. **But this constant is now also the lower edge applied to `F_xc`**, a reduced stress, through `column_slenderness_parameter` -- and at S235 and S275 it refuses sections the clause admits. That is R754 and it is a defect in the module, not in the value: `2.0e8` is right for a GRADE and no value of it is right for a reduced stress. C81's four boundaries are in the test and not the entry -- C87. |
| `F6_API_FY_PLAUSIBLE_MAX` | `1.0e9` | unchanged | pascals, STRUCTURAL | none, correctly (AO2) | same entry | **UNMOVED.** Admits S960. Now asserted from below at `9.6e8` by the EH4 test. It is not reachable by `F_xc`, which only falls. |
| `F6_API_CLAUSE_AGREEMENT` | `1.0e-14` | unchanged | dimensionless, RELATIVE | `F6_API_CLAUSE_AGREEMENT_COUNTER` | same block | **UNMOVED.** The entry's declared domain -- `D/t` 5.00 to 300.00 over six grades -- is the set R754 measures against, and `12.1%` of it now raises. C61 still open; the ceiling's `15x` of designed slack is not reopened. |
| `F6_API_CLAUSE_AGREEMENT_COUNTER` | `3.0e-13` | unchanged | dimensionless; a floor beneath the gate's own points | n/a, it IS the counter (AO2) | same block | **UNMOVED.** The helper swap now kills in five places including the EH4 test. C74 answered. |
| `F6_API_CLAUSE_INJECTION_EPS` | `1.0e-10` | unchanged | dimensionless, STRUCTURAL | none (AO2) | same block | **UNMOVED.** C62 still open. |
| `F6_API_UTILISATION_COUNTER_FACTOR` | `1.1` | unchanged | dimensionless, STRUCTURAL | none (AO2) | same block | **UNMOVED.** |
| everything in the F4 block and earlier | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 114 (`bf45e66`, judging `02b7daf`) was a **HOLD** carrying one blocking item, R753, and
thirteen closure items C71 to C83. Status of every one, read from the verdicts rather than from
memory. **The report's header names `verdict 114 @ bf45e66` and that IS the latest verdict** --
one comparison, taken: `git log -1 --format=%H -- docs/reviews/F6/step-2.md` is `bf45e66`.

* **R753 -- ANSWERED AND CLOSED.** By deletion, the second route the condition offered, and
  section 4 argues the route rather than accepting it. Site by site: `docs/F6_utilisation.md:70`
  rewritten, `scripts/measure/api_wsd_utilisation.py:437-438` rewritten, both in the SAME
  commit `9af9b75` (BP0), the deliverable regenerated, and
  `tests/regression/test_f6_deliverable_agrees_with_itself.py:93` now reads the count AND the
  stated precision against the CSV's own column. The figure is in a triple with its rule and
  pasted after the last edit. **It does not carry.**
* **C67 -- DISCHARGED where it became load-bearing.** `_CSV_FIGURES = 6` names the precision in
  one place and both the sentence and the regression test read it. The raw-float count is
  `12 of 17` and the published one `10 of 17`; the entry now says why rather than only that.
* **C71 -- ANSWERED AND EXACT.** `1.205880101064237` at `D/t = 100`; `1.761153975` is the
  `D/t = 300` figure. Both reproduced.
* **C72 -- THE REACH IS ANSWERED AND THE DOMAIN IS NOT. THIS IS R754.** All eight entry points
  refuse `355e3`, `355.0`, `355e9` and `0.0`, and each funnel call is pinned individually
  (deleting one gives `1 failed`). The repair then put a plausible-GRADE predicate in the path
  of the module's own `F_xc`. **C72 is closed and R754 is new**, because the finding is in the
  repair and not in the thing repaired.
* **C73 -- ANSWERED, IN THE QUANTITY.** `276.1x` is in the entry, the by-assertion attribution
  is correct one edit at a time, and the bound is now pinned from above at a solved `138.05`.
  Section 8.
* **C74 -- ANSWERED.** The reach is recorded and the helper swap kills in five places.
* **C75 -- ANSWERED.** `1 of 7`, `hub1:buoy1_arm` TIP, `f_b = 4.65871e-08 MPa`. Reproduced, and
  the implementer's account of why its own classifier mis-binned it is right.
* **C76 -- ANSWERED.** The conjunction is stated and the `17 of 17` is in the comment.
* **C80 -- ANSWERED, with two residuals.** Section 6. The unsafe direction is fixed on three
  functions; C84 and C85 are the residuals and neither reopens the item.
* **C81 -- ANSWERED, at the wrong site.** The four boundaries are in the EH4 test and the
  condition named the entry. C87, and the test is the better place for the assertion.
* **C83 -- ANSWERED AND EXACT.** The docstring now carries `12633843.953476468` and
  `0.09426368988411232`, which is the configuration the gate asserts at, and the paragraph
  records what the rounded neighbour returned. My own number became an input to the tree and
  this is where it is removed.
* **C77 -- ANSWERED in section 8 of the report**, with the cause named (CP3) and the trace
  re-taken. C78, C79 and C82 are stated as outstanding and go to the closure commit. Not
  findings under CZ0.
* **C41 to C66, C68 to C70 -- NOT IN THIS COMMIT, STATED AS OUTSTANDING, ROUTED PAST
  28 OCTOBER BY FC0** except C68, which R753 closed. A closure item does not block and is not
  re-reviewed item by item, so the non-delivery is not a finding. **C45 is the one I will not
  let pass in silence**, and section 7 is where I say so rather than making it a HOLD.
* **THE GENERATED SECTIONS -- LANDED, AND THEY ARE THE GENERATORS' OUTPUT.** Sections 0, 0a and
  9 carry `<!-- generated: scripts/ci_section.py -->` and `scripts/carried_table.py` markers,
  the CI table agrees with `gh` row for row at `02b7daf`, and the `Carried` table's two rows are
  the generator's. Condition 3 of verdict 114 is met.
* **FC1 AND MY OWN INSTRUCTIONS -- UNTOUCHED IN THIS RANGE.** Section 3. No STOP-class finding.
* **THE SCHEDULE -- NO SLIP YET, AND THE CHOICE IS NAMED IN ADVANCE.** Working target
  22 October, committed 28 October, today 9 October. Step 1 closed carrying nothing, so
  CLAUDE.md's two-consecutive-steps trigger has a count of one if step 2 closes carrying R754.
  Section 7 states the choice -- slip to the committed date, or reduce FC2 to sections 1 to 7 --
  with the dates beside it, rather than waiting for the step to close.

## The adversarial corpus (BE3)

**BATCH 47, committed separately as `ba1527e`:
`tests/corpus/f6_the_admissible_domain_a_refusal_declares.txt`, 25 entries, every one new this
round and none of them read by the implementer.** EG4(e)'s pause permits it and the header
claims the exception explicitly: EB6's label-provenance surface, the same one batch 46 claimed
-- API section 3.2.2's branch label, a published CSV column. Batch 46 recorded that the new
`F_y` refusal did not REACH that label; this batch records what happened when it was made to.

**COVERAGE: 6 of 25 caught.**

```
cmd    grep -c "^id=" <the file>                        out  25
cmd    grep "^id=" <the file> | grep -c "expect=catch"  out   6
cmd    every `site=` resolved mechanically against the tree
out    20 distinct sites, all present, all inside the file's line count
cmd    python -m pytest <the 19 files that read tests/corpus> -q -p no:randomly
out    9 failed, 2065 passed -- the same 9, so the batch breaks nothing
```

**THE COMPOSITION, WHICH IS THE PART WORTH READING.** The six catches are controls on what this
commit added and they are real: the funnels pinned per call site, the `t = D/2` boundary solved
both ways, the margin bound's new ceiling, the EH4 test surviving an attack on the helper its
own threshold is computed from, and the regression test reading a precision. **The nineteen
misses are almost all one shape, and it is a shape no previous batch has had:** a refusal
declares an admissible domain by what it rejects, and when the module feeds its own computed
intermediate back through that refusal the two domains must be the same set. Group 1's nine
entries are all that, and one of them is R754.

Against the last eight rounds -- `1 of 16`, `9 of 21`, `4 of 11`, `8 of 13`, `5 of 22`,
`9 of 25`, `9 of 19`, `4 of 22` -- this round is `24%`, above last round and below the series
median. **The number that matters more than the rate is that the batch's largest group is a
shape the corpus has not carried before**, and it was found by running the module at a
configuration grid the diff did not choose rather than by reading the diff. Four consecutive
rounds of "a sentence that characterises a set" ended this round, because R753 was answered by
deleting the sentence rather than by catching it.

**And two entries correct the reviewer's own record**, which is group 4's first line: verdict
114 and batch 46's first entry both call a `191%` overtake "the smallest of those seven" and it
is the largest. A corpus carrying a wrong measurement is worse than no corpus, so the
correction is in the data rather than only in this prose.

## Next step opens when

**STEP 2 STAYS OPEN. THIS IS ROUND 2 OF THREE, so revision 3 is the last one that gets read in
full** -- after it the step closes under CZ0's cap, R754 carries by name into the next step if
it is still open, and the closure items go into the closure artifact as a list. The conditions,
specifically:

1. **R754 is answered at the four sites it names**, site by site, with the diff hunk for each
   or a statement that the site was left and why: `floatfea/checks/api_wsd.py:230` (the
   predicate the internal substitution passes through),
   `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:1398` (the gate, asserted
   over the grade set `:1452` admits), `floatfea/tolerances.py:3010` and
   `docs/milestones/F6.md:239` (both still state an admissible grade set that is now false
   downstream -- BP0, re-measured in the same commit).
2. **The repair's own adversarial case is the grid and not the diff.** Whatever route is taken,
   the figure that closes it is taken over **every grade in [2.0e8, 1.0e9] the module admits
   and every `D/t` in the clause's own range**, not at the configuration the repair chooses.
   `235e6` at `D/t = 138.4383` and `275e6` at `248.0006` are the two the grid found and they
   are the cheap check; the model builds in under a second. If the answer is a floor, it is a
   floor beneath every admissible configuration in the R694 shape, and if it is a function of
   grade and `D/t` then it is written as one.
3. **FC2's results report.** Sections 1 to 7 at least, which is what FC2 asks a draft at. I
   agree with the implementer that two rounds on the blocker and nine false figures was the
   right order and I have said so in section 7 rather than treating it as a finding; what
   follows from it is that the deliverable and R754 land in the same revision or the choice in
   section 7 gets made.
4. **Nothing else from this verdict gates revision 3.** C84 to C87 and the open ledger go into
   the step's closure commit where CZ0 puts them -- fixed once, not re-reviewed item by item.
   The top-ten ordering item is **WITHDRAWN** by my own measurement and is not a condition.
5. **The nine reds are mine and revision 3 clears them by existing.** Its `Answers:` header
   will name this verdict, whose findings are written in the form `_blocking()` parses, so
   `test_a_blocking_item_is_not_routed_to_4a`,
   `test_the_generator_would_catch_a_row_under_the_wrong_number` and the seven planted states
   go green without anyone editing a test. **If they do not, that is a finding and it is mine
   to answer, not the implementer's.**

**WHAT I WILL NOT ACCEPT AT REVISION 3.** Verdict 114's four, minus the withdrawn one, plus
one. A count or a clause attribution in a published table derived from a PROXY rather than from
the quantity. A measurement block in `floatfea/tolerances.py` that no committed script
regenerates (BI3, five rounds on the list). A threshold declared without its boundary in the
direction that weakens it. **And new: a REFUSAL whose admissible domain is asserted at one
point of the parameter space it is applied over.** R754 is that, the gate denying it is that,
and it cost one round. A refusal is a decision rule, so it is solved for its boundary over the
whole domain it guards -- and where that domain is a two-parameter family, the adversarial case
is a grid, not a point.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6 step 2
Reviewed commit: 838e00e776acc0b4f86cea658f0c8d82b64d089b
Verdict: HOLD
**Reviewed commit: `02b7daf`** (`02b7daf6550b83c4bf9aaa316938cbd55ec46f4a`, tree clean when
I judged it; my corpus batch 46 is committed on top, which is why the plain `Reviewed
commit:` stamp below is not the commit I judged -- R718's subject, and this bold line is
the mechanism.)
Tests: 3291 passed, 155 failed, 1 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `02b7daf`, `661.67s`. Every
one of the 155 is EG3 state (1) and the trace is in section 1.)

## Round of 2026-10-09 -- F6 STEP 2 REVISION 1. **ROUND 1 OF THREE. HOLD on one item, and the count beside it is right.** FC0's four gate items are all delivered and all carry their own failure. The one thing that blocks is in the file the milestone exists to produce.

**WHY HOLD AND NOT PASS.** `docs/F6_utilisation.md:70` -- the deliverable Xabier reads --
now says the ten `C_m`-visible rows "are the rows where `amplified(C_m = 1.0)` OVERTAKES
simple". **The overtake holds on 17 of 17 compression rows.** The count `10` is right; the
clause attached to it names a set with seven more members than the count has, and read the
other way it separates no row from any other. It is a defect in a published deliverable and
in the `scripts/measure/` generator that produces it, which is CZ0 (a) as amended by EZ0,
and it is the answer to C68 -- whose closing condition was that the clause be *generated
from the set it describes, or deleted*. One literal was replaced by another literal. R753.

**WHAT IS GOOD, AND IT IS MOST OF IT.** C58's repair is right and it is right in the
quantity rather than in the value: the two aggregations are asserted to BE a minimum and a
maximum, inline, and all four of the substitutions the verdict named die, plus the three I
was asked to try and did not expect to land -- swapping the helpers' bodies, returning the
second-smallest, and skipping the weak-end key. **Eighteen one-at-a-time mutations, fifteen
killed.** C59 is one line and it is the right line. C60's refusal is two-edged, named, and
reaches the production path through `allowable_bending`. C69's tie is reachable, pinned,
bracketed either side, and **our two figures are the same crossing** -- the implementer's
reading of the discrepancy is correct and I verified it.

**No STOP.** No low rung is red. The verification ladder is GREEN in CI at the reviewed
commit, rung 5 among it, so the bit-exact tie equality survives a second libm.

## 1. EG3 STATE (1) -- I CHECKED THE TRACE RATHER THAN ACCEPTING IT, AND IT IS SHORT BY SEVEN

```
claim  every red at this commit is inside three report-guard files and nothing else is
cmd    python -m pytest -q -p no:randomly                      (whole suite, tree clean)
out    155 failed, 3291 passed, 1 skipped, 2 warnings in 661.67s
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py
       tests/test_report_guard_states.py -q -p no:randomly
out    155 failed, 161 passed, 1 skipped in 161.36s
judge  **155 = 155, so the three files account for EVERY red and nothing under
       tests/verification, tests/unit or tests/regression is red.** That is a stronger
       statement than the report's and it is the one the carve-out needs.
cmd    the 155, grouped by test name
out    113 test_every_named_site_is_touched_or_declared
out     23 test_the_report_carries_the_finding
out      7 test_the_guard_survives_the_state          <- tests/test_report_guard_states.py
out      1 test_the_guard_reads_the_step_being_worked_on       (EG3 state (1)'s baseline)
out     11 one each: test_there_are_pointers_to_resolve, test_the_reported_CI_counts_are_
out        not_all_zero, test_the_report_carries_a_WHOLE_SUITE_count, test_the_report_
out        carries_a_CI_SECTION, test_the_generator_would_catch_a_row_under_the_wrong_
out        number, test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph, test_the_
out        Carried_table_is_what_the_generator_produces, test_the_CI_section_is_about_the_
out        REVIEWED_commit, test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW, test_a_report_
out        does_not_say_CLOSED, test_a_carried_row_points_at_a_section_that_discusses_it
out     113 + 23 + 7 + 1 + 11 = 155
```

**AND THE SEVEN I RAN INDIVIDUALLY, WHICH IS THE DISCIPLINE EG3(i) EXISTS TO FORCE.**

```
cmd    pytest "tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]"
out    AssertionError: baseline: expected a clean run.
out      FAILED tests/test_report_carried.py::test_every_named_site_is_touched_or_declared
out        [R752-scripts/measure/api_wsd_utilisation.py:384]   ... and 147 more
out      148 failed, 122 passed, 1 skipped in 3.62s
out    assert 1 == 0
cmd    the other six, each alone
out    each fails at the same assertion site -- the clean-run expectation -- and each
out      names the red baseline run as its cause
judge  **EH1's own words: "the cascade is identified by the baseline being red and by each
       cascading state's own failure line, not by its name."** These seven are on state
       (1)'s list and the report does not enumerate them at all. I matched them by hand.
```

**AND THE REPORT'S OWN FIGURE DOES NOT REPRODUCE AT ITS OWN COMMIT.**

```
claim  the report's section 8 command, run by me, at the report's own commit
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py
       -q -p no:randomly
out    148 failed, 145 passed, 1 skipped in 4.07s
out    by file: tests/test_report_carried.py 148 ; tests/test_report_numbers_are_sourced.py 0
rule   EG3(i): the waiver is conditional on the trace, and each FAILED id is matched
judge  the report publishes `153 failed, 138 passed, 1 skipped` and `149 / 4`. **The four it
       attributes to `test_report_numbers_are_sourced.py` are GREEN**, and the seven in
       `test_report_guard_states.py` are missing. CP3: the paste preceded the last edit to
       the prose the guard reads. The trace holds -- because I took it, not because the
       report did. C77, and it does not block: the reds are the boundary and I proved it.
cmd    the skip
out    SKIPPED [1] tests/test_report_carried.py:2429: reported by
out      test_the_report_carries_a_WHOLE_SUITE_count
judge  a conditional skip keyed on a red FC1-class guard, not a skipped assertion. It was
       1 at `a041574` and 0 at `ececa58`, a closure commit, which is the control.
```

## 2. CI AT THE REVIEWED COMMIT -- THE LADDER IS GREEN, THE GUARD JOB IS THE SAME 155

```
cmd    gh run list --commit 02b7daf6550b83c4bf9aaa316938cbd55ec46f4a --json ...
out    [{"databaseId":38013114860,"workflowName":"CI","status":"completed"}]
cmd    gh run view 38013114860 --json jobs -q '.jobs[] | .name + " :: " + .conclusion'
out    the verification ladder            success
out    lint, unit and guards              failure
out    CI determinism -- leg / ten legs   skipped
cmd    the ladder job's steps
out    ladder 1 / 2 / 3 / 6 / 4 / 5       all success   <- rung 5 among them
cmd    the lint job's steps
out    actionlint, ruff, black --check, mypy, unit tests   all success
out    step 10 "guards and meta-tests"                     failure
cmd    the guard step's own summary line
out    155 failed, 1002 passed, 1 skipped, 1 warning in 678.14s (0:11:18)
judge  **CA2 SATISFIED AND THIS IS NOT CK2** -- a real eleven-minute run, a real runner, no
       allowance annotation. The red is `155 failed, 1 skipped`, which is MY OWN count to
       the test, so the Ubuntu machine and this one agree about which tests are red. **That
       is the state (1) boundary and not a defect**, and the ladder -- the half that
       measures the element -- is green. **Rung 5 passing on Ubuntu is the one measurement
       I most wanted**: `test_G61_a_TIE_between_the_two_forms_is_recorded_as_simple`
       asserts `amplified == simple` BIT-EXACTLY through two `pow` calls, and a second libm
       agrees. I record it as a fragility, not a finding (C82).
```

## 3. MY OWN INSTRUCTIONS, THE CONFTEST, THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
cmd    git diff --stat 2180f16..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
judge  CH2/CI0: no conftest and no plugin in the range, so rung 5's green is a pytest
       result and not a record rewritten from the rung's own directory.
cmd    git diff --stat 2180f16..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 24 ++++++
cmd    git show 7e0d6b4 --stat
out    CLAUDE.md 24+ ; docs/SUPERVISOR.md 24+ ; nothing else
cmd    git diff --name-only 7e0d6b4~1..7e0d6b4 | grep -cE "^(floatfea|tests|scripts)/"
out    0
cmd    the two added blocks, byte for byte
out    CLAUDE.md added 1438 bytes ; docs/SUPERVISOR.md added 1438 bytes ; IDENTICAL: True
cmd    removed lines in either file
out    CLAUDE.md 0 ; docs/SUPERVISOR.md 0
judge  **FC1 IS CLEAN AND IT IS THE SHAPE THE RULE ASKS FOR.** A standalone `process:`
       commit, citing FC1 by name, carrying its own three-cell measurement, purely
       additive, nothing under `floatfea/`, `tests/` or `scripts/`, and `.claude/`
       untouched. **NO STOP-class finding.** C45 is still open and still process class --
       and it still bites me: the agent definition I was invoked with carries the UNAMENDED
       head `(a) a defect in floatfea/`, so the criterion I am asked to rule under lives in
       `CLAUDE.md` and not in my own instructions. I ruled under EZ0 on the invocation's
       instruction and `CLAUDE.md:152`. Section 8 says what I think of leaving that to the
       post-28-October ledger.
```

## 4. C58 -- THE THREE SUBSTITUTIONS I WAS ASKED TO TRY, AND FOUR MORE

**IT IS NOT CIRCULAR, AND THE REASON IS WHAT THE ASSERTION IS ABOUT.** `per_point` at
`:1003` re-derives the per-point relative move from `clean` and `hurt` and asserts that
`_weakest_live_move`'s answer IS `per_point[0]` and `_worst_move`'s IS `per_point[-1]`.
A substitution changes the AGGREGATION, and an aggregation is what this compares. It would
be circular only if it took the ordering from the helper; it takes it from `sorted`.

```
rule   the 18 edits are one at a time, rung 5 re-run after each, source restored and the
       restoration asserted by re-reading the file; baseline 72 passed, 72 passed again
out    counter assertion: _weakest_live_move -> _worst_move    KILLED   3 failed
out    bracket test:      _weakest_live_move -> _worst_move    KILLED   1 failed
out    weak-end point My 1.0e6 -> 1.0e8                        KILLED   1 failed
out    weak-end point KL/r 30.4 -> 90.0                        KILLED   1 failed
out    SWAP the two helpers' bodies                            KILLED   4 failed
out    _weakest_live_move returns the SECOND-smallest           KILLED   4 failed
out    _weakest_live_move SKIPS the weak-end key               KILLED   2 failed
out    the weak-end point DELETED from AMPLIFIED_POINTS        KILLED   2 failed
out    inline per_point denominator max -> min                 KILLED   5 failed
out    MARGIN_MAX 2.0 -> 1.02 (the bound falls to the clean)   KILLED   1 failed
out    C59 counter 3.0e-13 -> 1.0e-15                          KILLED   1 failed
out    C59 injection 1.0e-10 -> 1.0e-8                         KILLED   1 failed
out    C60 the refusal disabled                                KILLED   2 failed
out    C60 only the LOW edge kept                              KILLED   1 failed
out    C60 FY_MIN 2.0e8 -> 4.0e8 (S355 itself refused)         KILLED  45 failed
out    C69 the tie: `>` -> `>=`                                KILLED   1 failed
out    u_combined = amplified only                             KILLED   1 failed
out    MARGIN_MAX 2.0 -> 300.0                                 SURVIVES 72 passed
out    FY_PLAUSIBLE_MIN 2.0e8 -> 3.6e5                         SURVIVES 72 passed
out    FY_PLAUSIBLE_MAX 1.0e9 -> 3.5e11                        SURVIVES 72 passed
judge  **THE THREE THE IMPLEMENTER ASKED ME TO TRY ALL DIE, and two of them die harder
       than the four the verdict named.** The three survivors are all the same shape and it
       is EH4's: slack in the direction that WEAKENS, on the three constants this commit
       declares. They are C73 and C81.
```

**AND THE ONE COMBINATION THAT MATTERS, WHICH IS EH4 RUN PROPERLY.**

```
rule   EH4: the ceiling falls toward the clean value AND the injection rises until a clean
       case trips -- both directions, including the two that weaken a gate
cmd    MARGIN_MAX = 300.0 together with the bracket-test substitution
out    72 passed            <- the substitution C58 was written for is GREEN AGAIN
cmd    MARGIN_MAX = 300.0 together with the weak-end My edit, and with the KL/r edit
out    1 failed in each     <- killed by `weak_point` and `weakest_name`, not by the bound
cmd    MARGIN_MAX = 300.0 together with the counter-assertion substitution
out    3 failed             <- killed by the inline min/max
cmd    the boundary, solved: min-over-COEFFICIENTS of max-over-POINTS
out    8.281906e-11 = 276.1x the counter 3.0e-13
judge  **THE BOUND IS THE SOLE KILLER OF EXACTLY ONE OF THE FOUR SUBSTITUTIONS, and its own
       boundary in the weakening direction is 276.1x.** The entry records `1.024974x` and
       `clears it by 1.95x`, which is the tightening side; the weakening side is not in the
       entry at all, and the entry's "the three substitutions miss it by two decades" reads
       as if the bound catches all three. **The VALUE 2.0 is defensible** -- it sits between
       the clean `1.024974x` and the detection boundary `276.1x`, near the tight end, and
       `F4_WINDOW_RULE_MIN_EDGE` really is `2.0` (`floatfea/tolerances.py:2581`). **I am not
       asking for a bound on the bound**; that regress has no end and the window rule is
       the project's answer to it. I am asking for the number `276.1x` to be in the entry.
       C73.
```

**AND THE REACH OF THE INLINE ASSERTION, WHICH THE REPORT'S OWN TABLE SAYS AND DOES NOT DRAW.**

```
cmd    the per-coefficient live-point count and the max/min ratio, reproduced independently
out    ALLOWABLE_TENSION_FACTOR  live 2  min 1.1475e-12 @3.3.1 U            ratio   87.14
out    ALLOWABLE_SHEAR_FACTOR    live 1  min 1.0000e-10 @3.2.4 F_v          ratio    1.00
out    BEAM_SHEAR_AREA_FACTOR    live 1  min 1.0000e-10 @3.2.4a f_v         ratio    1.00
out    ELASTIC_LOCAL_BUCKLING_C  live 2  min 1.0000e-10 @3.2.2b F_xe D/t=260 ratio   1.00
out    CM_JOINT_TRANSLATION      live 3  min 3.0749e-13 @3.3.2 U KL/r=30.4  ratio  269.34
out    weakest over the family 3.0749226272928885e-13 ; margin 1.0249742090976295 ;
out      counter/ceiling 30.0000x
judge  **EVERY FIGURE IN THE REPORT'S SECTION 3 REPRODUCES EXACTLY.** The implementer is
       right that "more than one live point implies min differs from max" is false and
       could not have been the assertion. The consequence it does not draw: on three of the
       five parametrisations a minimum and a maximum ARE THE SAME NUMBER, so the inline
       assertion distinguishes nothing there and the gate's reach is two of its five cells.
       Not a defect -- the two that matter are the two that carry the declaration -- but it
       belongs in the entry beside the ratios. C74.
```

## 5. C60 -- THE RANGE IS FINE AND THE REACH IS NOT

**THE RANGE FIRST, BECAUSE I WAS ASKED.** `[2.0e8, 1.0e9] Pa` is the right FORM and a
defensible value. It is an absolute threshold on a dimensional quantity, which my own guard
list calls a defect -- and this is the one legitimate exception: the whole purpose of the
threshold is to pin the UNIT, so it cannot be relative to anything, and the entry declares
`pascals` on its face. **"Wide enough to admit a value no steel has" is not a defect
either**: admitting `1000 MPa` costs nothing, because the failure mode is a wrong unit and
not an optimistic grade. I checked the slips that actually happen and every one is refused:
MPa (`355.0`), kPa (`3.55e5`), GPa (`3.55e11`), psi (`5.15e4`), kgf/cm2 (`3.62e3`), `0.0`,
a negative, `nan` and `inf`.

**THE REACH IS THE FINDING.** The report's section 5 says the refusal is "in the one
function every other clause routes through". It is not.

```
claim  four of the six F_y-taking entry points accept an implausible F_y
cmd    each function at fy = 355e6, 355e3 and 355.0, D/t = 100
rule   C60's own statement: the clause's `10340/F_y` form makes the UNIT load-bearing
out    section_class                 REFUSED        allowable_bending   REFUSED
out    local_buckling_stress         3.240000e+05   NO REFUSAL
out    allowable_axial_tension       2.130000e+05   NO REFUSAL
out    allowable_shear               1.420000e+05   NO REFUSAL
out    column_slenderness_parameter  3.417121e+03   NO REFUSAL  (1.080589e+02 at 355e6)
out    allowable_axial_compression(121.5, 2.5, 0.025, 355e3)
out      -> F_a = 1.928148e+05, branch 'inelastic_local'      NO REFUSAL
out    allowable_axial_compression(121.5, 2.5, 0.025, 355e6)
out      -> F_a = 7.325207e+07, branch 'elastic_local'
out    check_member(fy=355e3)        REFUSED -- because it calls allowable_bending FIRST
judge  **THE BRANCH OF SECTION 3.2.2 SILENTLY FLIPS UNDER EXACTLY THE SLIP C60 IS ABOUT**,
       in the function EZ4 Q3 and FA2 make the centre of this milestone -- the branch is a
       published CSV column and the locked plan's whole argument for `K = 2.0` is that it
       moves four members onto a different one. `C_c` moves by `31.6x`. The production path
       is SAFE, because `check_member` refuses upstream and nothing else in `floatfea/` or
       `scripts/` calls the four directly (`grep -rn ... | grep -v def` is empty).
```

**AND THE GATE'S NAME IS UNIVERSAL WHERE THE REFUSAL IS NOT.**
`test_an_F_y_that_is_not_plausibly_in_PASCALS_is_REFUSED` (`:1255`) is read by every later
reader as a property of the module; it exercises two entry points. That is the recorded
assertion-domain-blindness shape: the collection the assertion inspects cannot contain the
fault in the four it does not inspect. **I considered blocking on it under CZ0 (c) and I am
not, and the reason is FC0's own scoping** -- the directive asked for "the `section_class`
unit refusal with a plan row" and that is precisely what was delivered. I will not rule a
directive's own scope a failure. **What I will do is say that C72 should be promoted rather
than ledgered**, and section 8 says why.

```
claim  and the two other refusals the same two lines still do not make
cmd    section_class at the degenerate geometries
out    section_class(2.5, 0.0, 355e6)   -> ZeroDivisionError: float division by zero
out    section_class(-2.5, 0.18, 355e6) -> branch 'compact', d/t = -13.88888888888889
out    allowable_bending then returns 0.75 F_y, the MOST favourable branch
out    section_class(nan, 0.18, 355e6)  -> branch 'slender' (allowable_bending then raises)
rule   FB1/R741: a `D/t` outside the clause's range is REFUSED rather than extrapolated
judge  `fy = 0.0` raising `ZeroDivisionError` "rather than a named refusal" was C60's own
       second sentence. One line later, `wall = 0.0` still does exactly that -- and the
       `D/t` refusal is one-sided: the slender end raises by name, the impossible end
       returns the best allowable in the book. C80.
```

## 6. C69 -- OUR TWO FIGURES ARE THE SAME CROSSING, AND THE IMPLEMENTER'S READING IS RIGHT

```
claim  the tie, at full precision, through the module's own F_a
cmd    solve amplified == simple at KL/r = 60.8, f_a/F_e' = 0.02
out    My = 12633843.953476468 N.m
out    amplified = simple = 0.09426368988411232     equal: True, difference exactly 0.0
out    check_member there: interaction_form = 'simple', u_combined = 0.09426368988411232
judge  **AGREED, AND MINE WAS THE ROUNDED ONE.** Verdict 113's `1.263384395e+07` and
       `...235` came from the deliverable's 4-decimal section modulus, as the report says.
       The last digit is the implementer's and this is the second round running in which a
       figure I handed over as "mine to beat" was the looser of the two.
cmd    the bracket, and how knife-edge the tie is
out    My * 0.999 -> 'amplified' ; My * 1.001 -> 'simple'      (the test's own bracket)
out    My +- 1 and +- 2 ulp -> 'simple' ; My - 5 ulp -> 'amplified'
out    f_a_allow + 1 ulp -> amplified - simple = -1.388e-17, still 'simple'
out    ulp(value) = 1.3877787807814457e-17
rule   the sign of `1 - C_m/(1 - f_a/F_e')` = +0.132653, so amplified - simple DECREASES
       with f_b -- below the crossing amplified governs, above it simple does
judge  **THE DIRECTION CLAIM IN THE DOCSTRING IS CORRECT AND I CHECKED THE SIGN MYSELF.**
       The bracket at 0.1% is four decades clear of the knife edge, so it is not sitting on
       it. The exact equality routes through two `pow` calls and is therefore libm-
       dependent in principle; it is GREEN on Ubuntu at this commit, which is the only
       measurement that settles it. C82, recorded, not a finding.
```

**AND THE ONE THING IN C69's ANSWER THAT IS WRONG, WHICH I FOUND BY CHECKING THE CONVENTION
WHERE ITS OWN DOCSTRING SAYS TO.**

```
claim  the docstring's stated configuration is not the configuration of the tie
cmd    check_member at the `My` the docstring prints, and at the `My` the gate asserts
rule   floatfea/checks/api_wsd.py:367-369 -- "the tie occurs at KL/r = 60.8,
       f_a/F_e' = 0.02, My = 1.263384395e+07 N.m, where both forms are
       0.09426368988411235 bit-identically"
out    My = 1.263384395e+07     -> interaction_form 'amplified',
out      u_combined 0.0942636898681701
out    My = 12633843.953476468  -> interaction_form 'simple',
out      u_combined 0.09426368988411232
judge  **AT THE POINT THE ONLY STATEMENT OF THE CONVENTION NAMES, THE FIELD READS THE
       OPPOSITE LABEL.** The convention itself -- which half, and why -- is correctly stated
       and correctly asserted; the illustrative configuration is verdict 113's ROUNDED pair
       carried into `floatfea/`, and `1.263384395e+07` is `0.0035 N.m` away from the root.
       C83. I considered the carve-out for "a docstring that is the only statement of what
       something means" and did not take it, because the sentence that states the MEANING is
       true and the one that states the LOCATION is the false half -- the same split verdict
       113 made on C66, and I am being consistent with it rather than convenient.
```

## 7. THE STEP-1 CLOSURE COMMIT `9926026`, AND WHY R753 IS IN IT

EQ0 applies: it changes a gate (it adds a test file). The review counts against no step's
rounds (EB4). The new test is a REGRESSION test and the implementer's classification is
right -- it compares two shipped artifacts, asserts no threshold, carries no tolerance, and
"no new apparatus" is about guards and detectors, not about a file under `tests/regression/`
that reads a golden deliverable. **It carries its own failure, measured four ways.**

```
rule   the deliverables regenerate from the committed generator; then one edit at a time
out    clean regeneration reproduces both committed files (modulo the Windows CRLF the
out      checkout applies; content identical line for line)
out    R752 reverted in the generator, deliverables untouched   -> 10 passed   (correctly:
out      the shipped files are still right, so there is nothing to catch)
out    R752 reverted AND the deliverables regenerated           -> 1 failed  KILLED, by
out      test_the_FORM_counts_in_the_prose_are_the_CSV_s_own_counts, republishing
out      "AMPLIFIED governs on 10, SIMPLE on 7"
out    the published counts swapped by hand in the summary      -> 1 failed  KILLED
out    the interaction_form COLUMN deleted from the CSV         -> 3 failed  KILLED
out    the INDICATIVE label removed from the summary            -> 1 failed  KILLED
out    the C_m-visible count moved by one                       -> 1 failed  KILLED
judge  **BOTH WAYS OF REVERTING R752 REDDEN IT, AS CLAIMED.** C70 is answered.
```

**AND HERE IS THE HOLE IT LEAVES, WHICH IS WHERE R753 LIVES.**

```
claim  the regression test reads the COUNT and not the CLAUSE beside it
cmd    the regex at tests/regression/test_f6_deliverable_agrees_with_itself.py:93
out    r"C_m visibly moves U on (\d+) of (\d+)"  -- captures two integers and stops
cmd    rewrite everything after the double dash, three ways, and re-run the file
out    "...those are the rows governed by section 3.2.4 beam shear"   -> 10 passed
out    "...the moon is made of cheese"                                -> 10 passed
out    the clause deleted entirely                                    -> 10 passed
rule   the recorded question: if the thing this sentence asserts were false, would anything
       go red
judge  **NO.** The count is held and the characterisation beside it is not -- which is the
       hole R747, C68 and now R753 all sit in, and the fourth round running in which the
       defect is a sentence about WHICH rows.
```

**THE C66 REPAIR, CHECKED LINE BY LINE.** The three-mechanism account in
`floatfea/checks/api_wsd.py:352-360` is RIGHT: 5 of the 7 misses are rows where
`u_combined` is not the governing channel (beam shear), 2 are `platform:hub1_arm` and
`platform:hub3_arm` TIP where the amplified form IS governing and the bending share is
`0.0000%`. I reproduced all of it. Two sentences in the generator's comment are not:

```
cmd    the seven misses, re-measured, against the old conjunction
out    U is beam shear on 5 of 7 ; f_b < 1e-6 MPa on 3 of 7 ; BOTH on 1 of 7
out      -- hub1:buoy1_arm TIP, f_b = 4.65871e-08 MPa, governing 3.2.4 beam shear
judge  `:393` publishes "0 of the 7 are the both-halves case". It is 1, and verdict 113
       published 1. C75 -- and it is a number introduced in the course of answering a
       finding, which is CP2's exact subject.
cmd    the overtake alone, over all 17 compression rows
out    amplified(C_m = 1.0) > simple on 17 of 17
judge  `:387` says "That is what the predicate detects". The predicate detects the
       conjunction of three things; the overtake alone is true of every compression row in
       the table. C76, and R753 is the same sentence after it reached the deliverable.
```

## 8. ON THE CRITERION -- I WAS ASKED, AND I HAVE ONE THING TO SEND OUT

I applied CZ0 as amended by EZ0 and I agree with it. R753 is inside it: `docs/F6_utilisation.md`
is a published deliverable, `scripts/measure/api_wsd_utilisation.py` produces it, and EZ0's
exclusion is *reports* -- "it covers nothing in a report" -- which this is not. I considered
ruling it a closure item under the retired "truth of a published figure or sentence" head
and I decided against it for one reason: the retired head was retired because six rounds of
REPORT prose moved no gate. This is the summary block of the file that goes out.

**THE ONE THING FOR XABIER, and I say it once.** FC0 routes C41 to C65 past 28 October.
Two items on that list are not prose:

* **C45** makes the reviewer's own agent definition disagree with `CLAUDE.md` about what
  blocks. Every verdict between now and 28 October is written against instructions that
  carry the unamended head. I ruled under EZ0 because the invocation told me to; the next
  reviewer may not be told. It is one standalone `process:` commit.
* **C72** (new, this round) leaves `allowable_axial_compression` reclassifying the branch of
  section 3.2.2 under a wrong-unit `F_y` with no refusal, in the function whose branch label
  is a published column. The production path is protected by `allowable_bending` upstream,
  which is why I did not block; the API surface is not, and "no shipped caller can reach it"
  is a claim about today's callers.

Both are cheap. Neither needs apparatus. I am not making either a HOLD and I am not
spending a round arguing the criterion -- this is the escalation channel and this is the
escalation.

**AND ONE OBSERVATION ABOUT THIS ROUND'S SHAPE, FOR THE RECORD.** The three things that
survived my mutations are all the same thing: slack in the WEAKENING direction on a constant
this commit declared. EH4 is written down, it is three months old, and it was applied to
nothing in this diff -- every boundary in the new entries is solved from the side that makes
the gate look strong. That is one sentence per entry and it is the cheapest finding class
there is.

## Findings

**ONE BLOCKS.**

**R753.** `docs/F6_utilisation.md:70`, generated at
`scripts/measure/api_wsd_utilisation.py:437-438`. The published clause
*"C_m visibly moves U on 10 of 17 -- a DIFFERENT question: those are the rows where
amplified(C_m = 1.0) OVERTAKES simple"* asserts an identity that is false. **Measured from
the deliverable's own columns on all 17 compression rows, `amplified(C_m = 1.0) > simple`
holds on 17 of 17** -- the seven rows where `C_m` is NOT visible are also overtakes, and the
smallest of those seven is `platform:hub1_arm` TIP at `0.095733` against `0.032896`, a
`191%` overtake, where the amplified form IS the governing one. Read as an identity the
clause is false on seven rows; read as an implication it is true of every row and
distinguishes nothing. The count `10` is correct. The clause also states a relation between
`amplified` and `simple` -- that is `u_combined` -- while the count is measured on the
governing `U` at six figures, which is BP0: the figure and the clause carry different rules.
Nothing in the tree reads the clause: replacing it with "those are the rows governed by
section 3.2.4 beam shear", or with "the moon is made of cheese", or deleting it, each leaves
`tests/regression/test_f6_deliverable_agrees_with_itself.py` at `10 passed`.
**This is CZ0 (a) as amended by EZ0** -- a defect in a published deliverable and in the
`scripts/measure/` generator that produces it -- and it is the answer to **C68**, whose
closing condition was that the clause be *generated from the set it describes, or deleted
and the count left to stand on its own.* One f-string literal was replaced by another.
**Closed when** the clause is computed from the set it describes -- the correct
characterisation is in the commit's own comment and is cheap: `governing == "3.3.2
interaction"` AND the move exceeding six figures gives exactly `10` of `17`, where the
overtake alone gives `17` -- or the clause is deleted and the count stands on its own, with
`docs/F6_utilisation.md` regenerated in the same commit (BP0) and the deliverable's
regeneration re-measured.

**NOTHING ELSE BLOCKS.** I ruled every other candidate against CZ0 (a)-(d):

* **(a)** `floatfea/checks/api_wsd.py`'s new refusal is correct and two-edged; no published
  number moved (the CSV is byte-identical across the range and the `.md` changed one line);
  both deliverables regenerate from the committed generator. The missing refusal in
  `allowable_axial_compression` is real, is measured in section 5, and is unreachable from
  any shipped caller -- C72, and section 8 asks for it to be promoted rather than ledgered.
* **(b)** three new values. `F6_API_COUNTER_MARGIN_MAX = 2.0` is the right form and a
  defensible value, sitting between the clean `1.024974x` and the solved detection boundary
  `276.1x`; `F6_API_FY_PLAUSIBLE_MIN/MAX` are the one legitimate case for an absolute
  dimensional threshold, because pinning the unit is the whole point. What is missing from
  all three is the boundary in the weakening direction -- C73, C81, and not blocking.
* **(c)** fifteen of eighteen one-at-a-time mutations die, including the three the
  implementer asked me to try and did not expect to land. The gate's one over-broad claim is
  the F_y test's NAME; FC0 scoped C60 to `section_class` and that is what was delivered.
* **(d)** `155 failed` is EG3 state (1) in full, traced by name in section 1, every red
  inside three report-guard files, confirmed test-for-test by a CI run on another machine,
  and the ladder green at the reviewed commit.

## Closure items

Verdict 113's list ended at C70, so this one starts at C71. **C41 to C70 remain open, are
not re-adjudicated here, and FC0 routes C41 to C65 past 28 October** -- which is the
implementer's and Xabier's call and not a finding. Fixed once in the step's closure commit,
not re-reviewed item by item, and the step is not held on one.

* **C71.** `floatfea/tolerances.py:2998`, the `F6_API_FY_PLAUSIBLE_MIN` entry: "which is the
  wrong allowable by `1.76x` on a section the clause says is slender". Measured at the
  `D/t = 100` the same sentence names: `compact / F_b = 1.205880101064237`, where `F_b =
  220.793 MPa` on `reduced_2` against `0.75 F_y = 266.25 MPa`. `1.7612x` is the ratio at
  `D/t = 300`, the far end of the clause's range. The plan row (`docs/milestones/F6.md:239`),
  the report's section 5 and **this commit's own bit-exact assertion**
  (`tests/verification/rung5/...py:1297`, `assert compact / f_b == 1.205880101064237`) all
  carry `1.2059`. **Closed when** the figure is the one at the section the sentence names.
* **C72.** `floatfea/checks/api_wsd.py:223`. The C60 refusal reaches two of the six
  `F_y`-taking entry points. `allowable_axial_compression(121.5, 2.5, 0.025, 355e3)` returns
  `F_a = 1.928148e+05`, branch `'inelastic_local'`, with no refusal, where the same call at
  `355e6` returns `7.325207e+07`, branch `'elastic_local'`; `column_slenderness_parameter`
  moves `1.080589e+02 -> 3.417121e+03`. The branch is a published CSV column and FA2 makes
  it a reported quantity. `local_buckling_stress`, `allowable_axial_tension` and
  `allowable_shear` also accept it. The production path is protected because `check_member`
  calls `allowable_bending` first, and nothing else in `floatfea/` or `scripts/` calls the
  four directly. **Closed when** the refusal reaches the branch-selecting functions, or
  `test_an_F_y_that_is_not_plausibly_in_PASCALS_is_REFUSED`'s name and `section_class`'s
  docstring are narrowed to what is actually covered and the rest is recorded with the
  "no shipped caller can reach it" reason stated. **Section 8 asks for this one to be
  promoted rather than ledgered.**
* **C73.** `floatfea/tolerances.py:2988`, the `F6_API_COUNTER_MARGIN_MAX` entry. Its own
  boundary in the weakening direction is not recorded: `min`-over-coefficients of
  `max`-over-points is `8.281906e-11` = `276.1x` the counter, and at `MARGIN_MAX = 300.0`
  the bracket-test substitution the bound was written for is green again (`72 passed` for
  the two edits together). The entry also says "the three substitutions miss it by two
  decades", which reads as if this bound catches all three; measured, it is the SOLE killer
  of one (the bracket substitution) and the other two die by `weak_point` and `weakest_name`
  even at `MARGIN_MAX = 300.0`. **Closed when** the entry carries `276.1x` as the solved
  weakening-direction boundary (EH4) and names which assertion kills which substitution.
* **C74.** `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:1003-1017`. The
  inline min/max assertion cannot distinguish a minimum from a maximum on three of its five
  parametrisations: live-point counts are `2, 1, 1, 2, 3` and the `max/min` ratios are
  `87.14, 1.00, 1.00, 1.00, 269.34`. **Closed when** the reach is recorded beside the
  ratios, in the entry or in the test.
* **C75.** `scripts/measure/api_wsd_utilisation.py:393`. "0 of the 7 are the both-halves
  case the old sentence described of all seven." Measured over the seven: `U` is beam shear
  on **5**, `f_b < 1e-6 MPa` on **3**, BOTH on **1** -- `hub1:buoy1_arm` TIP, `f_b =
  4.65871e-08 MPa`, governing `3.2.4 beam shear`. Verdict 113 published `1`. CP2: a number
  introduced in the course of answering a finding. **Closed when** the count is the measured
  one.
* **C76.** `scripts/measure/api_wsd_utilisation.py:387`. "That is what the predicate detects
  -- not which form governs." The predicate detects a conjunction of three things; the
  overtake alone holds on `17 of 17`. BG0: a causal claim with no cell. **Closed when** the
  sentence states the conjunction or is reduced to the bare measurement.
* **C77.** `docs/reports/F6/step-2.md` section 8. The EG3 trace does not reproduce at its
  own commit. The report's own command, run by me at `02b7daf`: `148 failed, 145 passed,
  1 skipped`, all 148 in `test_report_carried.py` and **0** in
  `test_report_numbers_are_sourced.py`, against the published `153 failed, 138 passed` and
  `149 / 4`; and the **7** reds in `tests/test_report_guard_states.py` are absent from the
  enumeration. Whole suite: `155 failed`. EG3(i) makes the trace the load-bearing condition
  and the eighty-third verdict's lesson was a real defect hidden inside a cascade ruled by
  class. **Closed when** the trace is taken over every file that is red, with the per-name
  counts, pasted from the run that follows the last edit (CP3).
* **C78.** `docs/reports/F6/step-2.md` section 9. `grep -c "^\* \*\*C"
  docs/reviews/F6/step-1.md` is published as `26`; the same command at the same commit gives
  `31`. **Closed when** the figure is re-taken.
* **C79.** `docs/reports/F6/step-2.md` section 9. `git diff --stat HEAD -- docs/closure/`
  cannot fail on a clean tree. The claim is TRUE -- `git diff --stat 2180f16..HEAD --
  docs/closure/` is empty -- but the command is not the check. CW0's "a triple whose command
  cannot fail is not a triple". **Closed when** the command names the range.
* **C80.** `floatfea/checks/api_wsd.py:163`. `section_class(2.5, 0.0, 355e6)` raises
  `ZeroDivisionError: float division by zero`, which is verbatim the complaint C60 made one
  line earlier about `fy = 0.0`; and `section_class(-2.5, 0.18, 355e6)` returns branch
  `'compact'` with `d/t = -13.88888888888889`, so `allowable_bending` hands back `0.75 F_y`
  -- the most favourable branch in the clause -- where `D/t > 300` is refused by name.
  **Closed when** the two are refused the way the slender end is, or the asymmetry is
  recorded.
* **C81.** `floatfea/tolerances.py:3010` and `:3015`. The `F_y` range's solved boundaries in
  the weakening direction, which the entry does not carry: `MIN` may fall from `2.0e8` to
  `3.6e5` (`72 passed`; the boundary is `3.55e5`, a factor of `562`) and `MAX` may rise from
  `1.0e9` to `3.5e11` (`72 passed`; the boundary is `3.55e11`, `355x`), because the test
  hardcodes the two slips rather than bounding the range. **Closed when** both numbers are
  in the entry (EH4).
* **C82.** `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:1332`.
  `assert amplified == simple` is a bit-exact equality whose two sides both route through
  `c_c**2` and `r**3`, i.e. through libm `pow`; `ulp` of the value is
  `1.3877787807814457e-17` and a single-ulp move in `f_a_allow` changes the difference.
  **It is GREEN on Ubuntu at this commit** (ladder job success, run `38013114860`), which is
  what settles it. The tie convention is also asserted at one point of a two-parameter
  family. **Closed when** the entry or the docstring records that the equality is exact by
  construction and names the measurement on the second platform, or the absence is accepted.
* **C83.** `floatfea/checks/api_wsd.py:367-369`, which is the ONLY statement of the tie
  convention in the module and therefore the thing C69 was closed against. "the tie occurs
  at `KL/r = 60.8`, `f_a/F_e' = 0.02`, `My = 1.263384395e+07 N.m`, where both forms are
  `0.09426368988411235` bit-identically". Measured through the module at the `My` the
  sentence actually prints: `interaction_form = 'amplified'` and
  `u_combined = 0.0942636898681701`. At the gate's own `My = 12633843.953476468` it is
  `'simple'` and `0.09426368988411232`. **So the docstring names a configuration at which
  the tie does NOT occur and the field reads the opposite label**, which is the one check a
  reader of the convention would run. The figure is verdict 113's rounded pair carried into
  `floatfea/` -- the reviewer's own number became an input to the tree, which is the thing
  that verdict warned about twice about its own output. **Closed when** the docstring carries
  the configuration the gate asserts at, to the precision at which the tie is exact, or
  states the value to the digits that survive rounding.
* **R735, R736, R738, C34 to C40, the `0.2240`/`0.2239` item, R712 to R717, C2 to C15, C24
  to C33, C41 to C70** -- still open, carried as a list, not re-reviewed item by item.
  **C45 still needs its own standalone `process:` commit**, and section 8 says why it is not
  a 28-October item.

## Tolerances touched

```
cmd    git diff 2180f16..HEAD -- floatfea/tolerances.py
out    +51 lines, 0 deletions; three new names, no existing value moved
cmd    git diff 2180f16..HEAD | grep -E "^-.*(Final\[float\]|e-1[0-9]|= [0-9])"
out    (none)
cmd    git diff 2180f16..HEAD | grep -E "^\+.*(xfail|skipif|pytest.skip|deselect|--ignore|addopts)"
out    (none)
cmd    git diff --stat 2180f16..HEAD -- pyproject.toml .github scripts/run_rung.sh
out    (empty)
judge  **NOTHING WAS WIDENED AND NOTHING STOPPED ASSERTING.** Zero deletions in
       `tolerances.py`, no marker, no deselection, no workflow change. Three constants are
       NEW, so EU1's adversarial case applies to them and section 4 is it -- 18 one-at-a-
       time edits and 7 combinations, at configurations the diff did not choose.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F6_API_COUNTER_MARGIN_MAX` | -- | `2.0` | dimensionless, STRUCTURAL; a bound on a MARGIN, not a ceiling on a measured quantity | none, correctly (AO2) -- it is a bound on how loose a counter's floor may be | `floatfea/tolerances.py:2963-2988`; `docs/milestones/F6.md:238` | **ADMISSIBLE, AND IT IS LOAD-BEARING FOR EXACTLY ONE SUBSTITUTION.** The value sits between the clean margin `1.0249742090976295x` (which I reproduce exactly) and the solved detection boundary `276.1x`, near the tight end, and `F4_WINDOW_RULE_MIN_EDGE` really is `2.0` at `:2581`, so the stated derivation checks out. Pinned from below: `1.02` gives `1 failed`. **NOT pinned from above: `300.0` gives `72 passed`, and `300.0` together with the bracket substitution gives `72 passed`** -- C73. I am not asking for a bound on the bound; I am asking for `276.1x` to be in the entry. |
| `F6_API_FY_PLAUSIBLE_MIN` | -- | `2.0e8` | pascals, STRUCTURAL; a refusal threshold on an INPUT | none, correctly (AO2) -- it fires by design on a wrong unit | `floatfea/tolerances.py:2990-3010`; `docs/milestones/F6.md:239` | **ADMISSIBLE, AND THE ABSOLUTE DIMENSIONAL FORM IS CORRECT HERE** -- pinning the unit is the purpose, so it cannot be relative to a response scale, and the entry declares `pascals`. Every slip that happens is refused: MPa, kPa, GPa, psi, kgf/cm2, `0.0`, negative, `nan`, `inf`. Pinned from above by 45 tests (`4.0e8` refuses S355 itself). **NOT pinned from below: `3.6e5` gives `72 passed`**, so the solved weakening boundary is `3.55e5`, a factor of `562` -- C81. The entry's `1.76x` is wrong for the section it names -- C71. |
| `F6_API_FY_PLAUSIBLE_MAX` | -- | `1.0e9` | pascals, STRUCTURAL; the upper edge of the same range | none, correctly (AO2) | same entry | **ADMISSIBLE.** Admits S960. **NOT pinned from above: `3.5e11` gives `72 passed`**, boundary `3.55e11`, `355x` -- C81. |
| `F6_API_CLAUSE_AGREEMENT` | `1.0e-14` | unchanged | dimensionless, RELATIVE | `F6_API_CLAUSE_AGREEMENT_COUNTER` | same block | **UNMOVED.** C59's new line asserts `COUNTER > CEILING`, which pins the counter from below; the ceiling may still RISE `15x` to `1.5375e-13`, which verdict 111 ruled the window rule's designed slack and I am not reopening -- recorded as C82's neighbour in corpus batch 46. C61 still open. |
| `F6_API_CLAUSE_AGREEMENT_COUNTER` | `3.0e-13` | unchanged | dimensionless; a floor beneath the gate's own points, with those points at the weak end | n/a, it IS the counter (AO2) | same block | **UNMOVED, AND NOW HELD IN THE QUANTITY.** `1.0e-15` gives `1 failed` (C59 answered); the min-over-points aggregation is asserted inline and all four substitutions die (C58 answered). C74 records the reach. |
| `F6_API_CLAUSE_INJECTION_EPS` | `1.0e-10` | unchanged | dimensionless, STRUCTURAL | none, correctly (AO2) | same block | **UNMOVED.** `1.0e-8` gives `1 failed`, so the 100x rise is now caught. C62 still open against the "two decades" sentence. |
| `F6_API_UTILISATION_COUNTER_FACTOR` | `1.1` | unchanged | dimensionless, STRUCTURAL | none, correctly (AO2) | same block | **UNMOVED.** |
| everything in the F4 block and earlier | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 113 (`2180f16`, judging `ececa58`) was an EQ0 **PASS** on step 1's closure commit
that carried **nothing blocking** into step 2 and left C66 to C70 plus C41 to C65 as closure
items. Status of every one of them, read from the verdicts and not from memory.

* **R752 -- CLOSED at verdict 113 and NOT reopened.** It does not carry; the report records
  it as closed with that verdict named and does not re-argue it, which is correct. I
  re-measured the half that matters: `interaction_form` over the 32 published rows is
  `tension 15 / simple 10 / amplified 7`, and the two published sentences at
  `docs/F6_utilisation.md:69-70` -- the FORM count and the `C_m`-visible count -- are each
  arithmetically right. **The clause explaining the second is R753.**
* **C66 -- ANSWERED, and the answer is right where it is a mechanism and wrong twice where
  it is a count.** The three-mechanism account in `floatfea/checks/api_wsd.py:352-360` is
  correct and I reproduced all of it: the ten that fire are an overtake by `0.1153%` (both
  over-unity platform ROOTs) to `1.3129%` (`hub2:buoy4_arm`/`hub4:buoy10_arm` ROOT); five
  miss because `u_combined` is not the governing channel; two miss with bending share
  `0.0000%` where the amplified form IS governing. The old false conjunction is deleted from
  both sites -- `grep` over the diff shows `:377-378` and `:333-335` gone. **Two new
  sentences in the replacement are not measured: C75 and C76.** The 5/2 split in verdict
  113's section 5 was right and I confirm the implementer's statement that its quick
  classifier mis-binned two.
* **C67 -- NOT IN THIS RANGE, STILL OPEN.** The six-figure formatting in the `cm_visible`
  predicate still carries no reason, and the measurement is unchanged: a raw float
  comparison gives `12 of 17`, the shipped one `10 of 17`. It is now load-bearing for R753's
  repair, because the correct characterisation has to name the precision.
* **C68 -- ANSWERED AND THE ANSWER DOES NOT MEET THE CONDITION. THIS IS R753.** The
  condition was "the clause is generated from the set it describes, or deleted and the count
  left to stand on its own". The commit replaced the literal "and its answer is the
  bending-dominated ROOTs" with the literal "those are the rows where amplified(C_m = 1.0)
  OVERTAKES simple". Both are f-string literals; neither is derived from the set; and the
  new one is FALSE where the old one was true. Verdict 113's own closing section said in
  terms what it would not accept at this revision: "a sentence characterising WHICH rows a
  published count covers, where the characterisation is not itself computed from the set."
* **C69 -- CLOSED.** The convention is in `MemberCheck.interaction_form`'s docstring
  (`floatfea/checks/api_wsd.py:362-369`), the tie is asserted bit-identically, the bracket
  runs both ways, and `>` to `>=` now gives `1 failed` where it gave `69 passed`. Our two
  figures are the same crossing and the implementer's reading of the difference is right --
  section 6. The residual domain question is C82 and does not reopen it.
* **C70 -- CLOSED.** `tests/regression/test_f6_deliverable_agrees_with_itself.py` is the
  first thing under `tests/` that reads either deliverable. It is a regression test and not
  apparatus -- two shipped artifacts compared with each other, no threshold, no tolerance --
  and I verified its own failure five ways, including both ways of reverting R752. Section 7.
  **Its reach stops at the counts, which is where R753 sits.**
* **C58, C59, C60 -- ALL THREE ANSWERED, and this is the EQ0 commit verdict 113 said they
  would need.** Section 4 and section 5 are the measurements. C58 is answered in the
  quantity rather than the value, which is the shape worth repeating. The residuals are C72,
  C73, C74, C80, C81 and none of them reopens the item.
* **C41 to C57, C61 to C65, C67 -- NOT IN THIS COMMIT, STATED AS OUTSTANDING, ROUTED PAST
  28 OCTOBER BY FC0.** Under CZ0 a closure item does not block and is not re-reviewed item
  by item, so the non-delivery is not a finding. **C45 is the one I will not let pass in
  silence**, and section 8 is where I say so rather than making it a HOLD.
* **FC1 -- DIFFED AS MY OWN INSTRUCTIONS AND CLEAN.** Standalone `process:` commit, cites
  FC1, byte-identical 1438-byte blocks in `CLAUDE.md` and `docs/SUPERVISOR.md`, zero removed
  lines, nothing under `floatfea/`, `tests/` or `scripts/`, `.claude/` untouched. **No
  STOP-class finding.** I agree with the implementer that FC0 does not permit folding C45
  in -- C45 is in C41 to C65 and FC0 routes those to the ledger; it needs its own commit, as
  verdict 113 and verdict 112 both said.
* **THE GENERATED SECTIONS -- THE MECHANICAL REASON IS SOUND AND I WOULD NOT ASK FOR THEM.**
  `VERDICT` resolves to `max(REVIEWED)` over the milestone's review directory, which at a
  step's first revision is the PREVIOUS step's verdict, so `carried_table.py`,
  `answered_table.py` and `ci_section.py` would each emit step 1's content into step 2's
  report, and a `Carried` table would have nothing to be a table of. I verified the
  resolution by reading `tests/test_report_carried.py:68-120`. **Revision 2 carries them**,
  and this verdict is what makes `max(REVIEWED)` equal `2`.
* **THE SCHEDULE -- NO ESCALATION IS DUE AND I AGREE WITH THE REPORT'S READING.** Working
  target 22 October, committed 28 October, today 9 October; step 1 closed on the 9th
  carrying nothing. CLAUDE.md's trigger is two consecutive steps closing with blocking
  items and the count is zero. **This HOLD is round 1 of 3 and the fix is one f-string**, so
  it costs the schedule nothing I can measure. If step 2 closes carrying R753 or C72, the
  choice -- slip the date or reduce scope -- has to be stated with a number beside it.

## The adversarial corpus (BE3)

**BATCH 46, committed separately as `838e00e`:
`tests/corpus/f6_what_a_published_characterisation_is_computed_FROM.txt`, 22 entries, every
one new this round and none of them read by the implementer.** EG4(e)'s pause permits it and
the header claims the exception explicitly: EB6's label-provenance surface, which is where
this commit's two new labels live -- `interaction_form` at a tie, and section 3.2.2's branch
label, which is a published CSV column.

**COVERAGE: 4 of 22 caught.**

```
cmd    grep -c "^id=" <the file>                        out  22
cmd    grep "^id=" <the file> | grep -c "expect=catch"  out   4
cmd    every `site=` resolved mechanically against the tree
out    18 distinct sites, all present, all inside the file's line count
cmd    python -m pytest <the nine files that read tests/corpus> -q -p no:randomly
out    155 failed, 1527 passed, 1 skipped   -- the same 155, so the batch breaks nothing
```

**AND THE COMPOSITION, WHICH IS THE PART WORTH READING.** The four catches are all controls
on what this commit ADDED -- the min-over-points aggregation, the weak-end point's identity,
the two-edged `F_y` refusal, the tie label. **Every one of the eighteen misses is in one of
two places:** a sentence that characterises a set (group 1, seven entries, where R753 lives),
or a boundary solved in only the strengthening direction (groups 2 and 3, six entries). That
is not a scanner gap and I am not asking for a scanner. It is two sentences per entry: say
which set the characterisation is computed from, and say where the boundary is on the side
that weakens.

Against the last seven rounds -- `1 of 16`, `9 of 21`, `4 of 11`, `8 of 13`, `5 of 22`,
`9 of 25`, `9 of 19` -- this round is `18%` and the lowest of the series. **I report it
rather than dressing it up**: the entries I could write this round were almost all about
things nothing in the tree is built to catch, because the things the commit DID build are
caught and I verified that eighteen ways. A low catch rate on a batch aimed at the gap is
the measurement working, not failing -- but it is also the fourth consecutive round in which
the gap is the same sentence, and that is now a number rather than an impression.

## Next step opens when

**STEP 2 STAYS OPEN. THIS IS ROUND 1 OF THREE and revision 2 answers R753 before anything
else, including before any FC2 content.** The conditions, specifically:

1. **R753 is answered at `docs/F6_utilisation.md:70` and at
   `scripts/measure/api_wsd_utilisation.py:437-438`, site by site**, either by computing the
   characterisation from the set -- `governing == "3.3.2 interaction"` and the move exceeding
   the published precision gives exactly `10 of 17`, where the overtake alone gives `17 of
   17` -- or by deleting the clause and letting the count stand. **The deliverable is
   regenerated in the same commit (BP0)** and the regeneration is re-measured, and the
   revision says which of the two routes was taken and why.
2. **The figure that answers it is in a triple with its rule (BF0, BP0, CP3)**: the count,
   the set the characterisation is computed from, the predicate's precision, and the command,
   pasted from the run that follows the last edit. The precision is C67 and it is now
   load-bearing, so C67 comes with it even though FC0 ledgered it.
3. **The generated sections land in revision 2**, which this verdict makes possible --
   `max(REVIEWED)` is now `2`. I would not have asked for them at revision 1 and I agree with
   the mechanical reason the report gives.
4. **The EG3 trace in revision 2 is taken over every file that is red**, with the per-name
   counts and the whole-suite total beside the per-file totals (C77). EG3(ii) also asks for
   the report-guard files run AT this verdict's commit, with the counts pasted.
5. **Nothing else from this verdict gates revision 2.** C71 to C83 go into the step's closure
   commit where CZ0 puts them -- fixed once, not re-reviewed item by item. **C72 and C45 are
   the two I have asked to be promoted rather than ledgered**, in section 8, and that is a
   decision for the directive and not a condition I am imposing.

**WHAT I WILL NOT ACCEPT AT REVISION 2.** Verdict 113's three, unchanged, plus one. A count
or a clause attribution in a published table derived from a PROXY rather than from the
quantity. A top-ten list whose order depends on row order among equal values -- still live,
`hub2:buoy4_arm` ROOT and `hub4:buoy10_arm` ROOT both carry `0.009245` and `sorted` is stable
on input order, and FC2's top ten is about to publish it. A measurement block in
`floatfea/tolerances.py` that no committed script regenerates (BI3, four rounds on the list).
**And new: a THRESHOLD declared without its boundary in the direction that weakens it.** Three
of the three survivors in my mutation battery are that, on three constants declared in one
commit, and EH4 is written down. It is one number per entry.
