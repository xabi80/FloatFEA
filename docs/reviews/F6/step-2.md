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
