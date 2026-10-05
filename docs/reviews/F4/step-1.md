# Review — F4 step 1
Reviewed commit: 3d6fdb606f454608f7b2418d9e16f3bd78199677
Verdict: HOLD
**Reviewed commit: `7c8e4ae7c57d48f51a5e955a42fceb1d25a117ac`** (HEAD of F3 at invocation,
pushed). My corpus commit `3d6fdb6` lands first, so the script's `Reviewed commit:` stamp
and the judged commit differ; DU1 says restate the judged one and this is it.
Tests: 2844 passed, 39 failed, 3 skipped   (MY OWN run, ONE invocation, no `--ignore`, no
deselection, fresh clone outside the OneDrive tree, 604.75s. I did not accept a count from
the report, and the report publishes none -- its section 17 is the literal token
`SUITE2_PLACEHOLDER`.)
**CI at the reviewed commit: run `37349836460`, conclusion FAILURE, and the red is
`ladder 4 -- the loads are the loads`.**

## Round of 2026-10-05 -- NINETY-FOURTH verdict. F4 step 1, SECOND round of three.

**HOLD.** R663 is genuinely fixed and I verified it independently; EB6's first side is
real, correct, and catches the smallest of all 66 label transpositions; R664 moved from an
identity to a comparison against an independently formed weight and now reddens on the
injection that defeated it. That is three of seven answered with work I could not break.

**What holds the step is this: the one red in CI is rung 4, and it is red because this
step's own gate skips.** `scripts/run_rung.sh:274-276` fails a rung on ANY skip, by a rule
this repository already wrote down. The implementer hands me EB6's `skipif` as a routing
question; the ladder script had already ruled on it, and rung 5 is skipped behind the red.
Then four of verdict 93's seven items are untouched or half-answered at their named sites,
and the machine says so by name before I do. And one new ceiling can be widened nineteen
decades -- past the exact error the defect it exists to catch produces -- with every one of
its ten gates green.

## 1. THE DIFFS, EACH ONE SEPARATELY, AS MY INSTRUCTIONS ORDER THEM

```
cmd    git diff --stat 3a908fa..7c8e4ae -- floatfea tests docs scripts
out    F4.md 18, preview 78, step-1.md 158/8, member_forces.py 63, tolerances.py 84,
out    rung4/test_f4_static_and_mapping.py 354.  SIX files.
cmd    git diff --stat 3a908fa..7c8e4ae -- floatfea/tolerances.py      [instruction 4]
out    84 insertions, 0 deletions -- SIX new constants, read line by line in section 6
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"        [instruction 4c]
out    tests/conftest.py                                  -- the instruction is intact
cmd    git diff 3a908fa..7c8e4ae -- tests/conftest.py "tests/**/conftest.py"
out    (no output) -- nothing the ladder gate reads was rewritten from a rung, and I
out    checked it rather than inferring it from the rung own green
cmd    git diff 3a908fa..7c8e4ae -- .claude docs/SUPERVISOR.md         [instruction 4b]
out    (no output) -- NO STOP-CLASS FINDING. My own instructions are untouched across the
out    whole range and I diffed them; nothing in the suite reads that file.
cmd    grep -n "^Answers:" docs/reports/F4/step-1.md                   [instruction 1b]
out    363: Answers: verdict 93 @ 3a908fa
judge  `3a908fa` IS the newest verdict commit. The header names the LATEST verdict and not
       a superseded one, so every `Carried` claim in the report is about the right list.
       That is the one comparison a machine cannot make and I made it first.
```

## 2. CI AT THE REVIEWED COMMIT (CA2), AND THE RED IS A LADDER RUNG

```
cmd    gh run list --commit 7c8e4ae7c57d48f51a5e955a42fceb1d25a117ac --json ...
out    [{"conclusion":"failure","databaseId":37349836460,"status":"completed"}]
cmd    gh run view 37349836460 --json jobs -- job AND step level
out    lint, unit and guards     FAILURE
out      actionlint / ruff / black --check / mypy / unit tests   ALL success
out      **guards and meta-tests  FAILURE**
out    the verification ladder   FAILURE
out      ladder 1 success / ladder 2 success / ladder 3 success / ladder 6 success
out      **ladder 4 -- the loads are the loads   FAILURE**
out      ladder 5 -- independent confirmation    skipped
out    CI determinism (two jobs) skipped
out    lint job ran 17:37:53 to 17:48:47 ; ladder job 17:37:41 to 17:41:09
rule   CK2: the third state is runner_name empty, NO steps, a two-second duration and the
       spending-limit annotation
judge  **IT IS NOT CK2.** Both failing jobs carry full step lists with real conclusions and
       ten- and three-minute durations. `guards and meta-tests` is SEEN TO HAVE RUN rather
       than skipped behind an earlier red step, which is what CZ1 (iii) exists to make
       visible. Two real reds.
judge  I used the full sha throughout; the short form returns an empty list silently.
```

**AND THE LADDER RED IS THE SENTENCE THAT DECIDES THIS ROUND:**

```
cmd    gh run view 37349836460 --log-failed, the ladder job only
out    run_rung: FAIL -- 2 skipped in tests/verification/rung4. CLAUDE.md: never skip a
out    test to get a green build. Report the failure instead.
out    run_rung: 137 collected, 0 failed, 0 errored, 2 skipped
out      skipped  test_f4_static_and_mapping::test_EB6_every_buoy_label_sits_where_HSP_STABLE_says
out      skipped  test_f4_static_and_mapping::test_EB6_a_PERMUTED_export_reddens_the_gate
rule   scripts/run_rung.sh:274-276 -- a rung with any skipped case exits FAIL
judge  **ZERO FAILED, ZERO ERRORED, AND THE RUNG IS RED ANYWAY, BY DESIGN.** The step own
       gate turns its own rung red on the machine that gates the merge, and rung 5 is
       skipped behind it. Filed as R670, and it is also my ROUTING of the question the
       report hands me: a `skipif` inside `tests/verification/` is not an option this
       repository leaves open, and the decision was taken before I was asked.
```

## 3. R663 -- FIXED, AND I VERIFIED IT RATHER THAN ACCEPTING IT

```
cmd    build_superstructure + solve_superstructure_static, full scale; over all 16 members
         form `k u - T f_eq` and compare the tip shear with the solve own reaction vector
out    tip shear vs support reaction, worst relative over 16 members: 3.143e-16
out    assertions executed: 16 of 16 ; members skipped by the `continue`: 0
out    conservation |Vz_A + Vz_B - weight| / weight, worst over 16 members: 5.696e-16
out    the same with the element equivalent load omitted: 7.931e-01 on the tip shear
rule   element nodal force recovery with distributed loads, `f_end = k u^e - f^e_eq`
judge  **FIXED, AND THE REPORT FIGURES REPRODUCE ON MY INSTRUMENT TO EVERY DIGIT.** The
       preview is reissued as issue 2 in the SAME commit as the fix (`9ebbec1`), which is
       what BP0 asks, and its static table now reads `3.0656e+06` and `5.9269e+06` for the
       platform and hub tip shears -- the corrected values, matching my own solve.
judge  And section 5 confession is the best paragraph in the report. The implementer
       recorded against itself that its "independent arithmetic check" WAS the defective
       formula identity and would have reddened on the fix. That is the finding I made and
       the wording is the implementer own.
```

## 4. EB6 -- THE FIRST SIDE IS REAL, AND I TRIED TO BREAK IT

```
cmd    parse CLUSTER_ARM_RADIUS and CLUSTER_ANGLES_DEG from HSP-stable, rebuild the 12
         centres, scale by froude_lambda, compare with the built FE nodes
out    clean worst = 0.000000e+00 m
cmd    permute the EXPORT and not the expectation: buoy_joint_nodes buoy2 <-> buoy4
out    worst = 30.982842 m -> REDDENS the 1.0e-6 m ceiling
cmd    all 66 label transpositions in turn, the genuinely permuted export each time
out    MINIMUM 30.982842 m, on buoy2-buoy4, with 4 pairs at that value
rule   DQ9: at least 1e3x below the smallest transposition displacement, both edges solved
judge  **THE DECLARED COUNTER IS THE TRUE MINIMUM OVER ALL 66, AND I CHECKED ALL 66 RATHER
       THAN THE ONE THE TEST PICKS.** 4 pairs at 0.619657 m model scale is verdict 91 own
       figure, reproduced. The permuted EXPORT reddens the gate -- the form the plan
       section 2.2 asks for, and stronger than the permuted expectation the test uses. The
       two are equivalent here and I measured that they are.
judge  The UPPER edge binds: the ceiling may rise to 30.9 with all ten green and reddens at
       31.0. The LOWER edge is set by how many decimal places `30.982842` was written to,
       not by the clean worst, which is exactly `0.0` -- so DQ9 "1e3x above the clean worst"
       edge cannot bind, and the entry own comment says so. Honest.
judge  Two of the four constants are LITERALS in the test (`[0.0, 120.0, 240.0]` and `0.5`)
       and only two are parsed. A change in HSP-stable would redden rather than pass, so it
       fails safe, but the docstring sentence "a change there reaches this gate" is false
       for half the expected side. C146.
```

## 5. R664 -- ANSWERED, AND THE INJECTION I RAN IS NOT THE ONE THE COUNTER-CASE RUNS

```
cmd    the shipped gate arithmetic, five bodies, CLEAN
out    platform rel 0.000e+00 ; hub1 2.095e-16 ; hub2 0.000e+00 ; hub3 2.095e-16 ; hub4 0
cmd    PHYSICAL INJECTION 1: subtract the remainder diagonal from body_mass_matrix
out    platform applied 6.131250e+06 against expected 1.226250e+07, rel 5.000e-01  RED
out    all five rows RED
cmd    PHYSICAL INJECTION 2: negate selfweight.GRAVITY_VECTOR -- gravity points UP
out    platform  applied 1.226250e+07  expected 1.226250e+07  rel 0.000e+00  **PASS**
out    hub1-4    applied 1.778063e+07  expected 1.164937e+07  rel 5.263e-01   RED
out    sum_error on all five bodies: 0, 0, 0, 2.095e-16, 2.095e-16 -- still blind
rule   DQ8 static: `abs(sum reactions - weight) / weight` against the FE mass own weight
judge  **THE MOVE IS REAL AND IT WORKS: `weight_N` now enters a comparison and the half-mass
       injection that read `3.038e-16` last round reads `5.000e-01`.** That is R664 answered
       on its principal direction.
judge  **BUT THE GATE TAKES `abs(case.applied_N)`, SO IT DISCARDS THE SIGN**, and gravity
       reversed PASSES on the platform row -- the row the verdict measured it on. The whole
       gate reddens only through the four hub rows, i.e. through the handed-down term; a
       body with no upstream body is sign-blind. And the declared counter-case injects into
       the EXPECTED side (`corrupt = -case.weight_N`) rather than into the model, so it
       never ran the injection it names. R674.
```

## 6. THE SIX NEW TOLERANCES, BOTH DIRECTIONS (EH4), AND ONE CEILING IS UNBOUNDED

Every sweep below restores `floatfea/tolerances.py` afterwards and I verified
`git status --short` clean at the end of each.

```
cmd    sweep F4_MEMBER_FORCE_CONSERVATION, rung4 + rung3 counter-case guard + literal guard
out    5.0e-16  -> 1 failed  test_G4_member_end_shears_sum_to_the_load_the_member_carries
out    1.0e-13  -> 150 passed   (shipped)
out    1.0      -> 150 passed
out    2.0      -> 150 passed
out    1.0e+6   -> 150 passed
cmd    rename ONLY the counter: F4_MEMBER_FORCE_CONSERVATION_COUNTER_DEFECT -> _COUNTER
out    ceiling 1.0e-13 -> 150 passed
out    ceiling 2.0     -> 1 failed
out                       test_the_ceiling_sits_below_its_counter_case[F4_MEMBER_FORCE_CONSERVATION]
rule   EH4: a boundary is solved in BOTH directions, including the two that WEAKEN a gate
rule   tests/verification/rung3/test_tolerance_counter_cases.py:89-94 returns EARLY for any
       entry whose counter is named `_COUNTER_DEFECT`, because "a defect SIZE is not in the
       ceiling quantity, so no ordering between them exists to assert"
judge  **THE CEILING MAY RISE NINETEEN DECADES WITH EVERY ONE OF THE TEN GATES GREEN, PAST
       THE 1.0 ERROR R663 ITSELF PRODUCES.** At 2.0 the gate the plan credits with catching
       R663 would accept R663. Nothing bounds it, because the counter test compares
       `abs(carried)/weight < CEILING` -- and the defective formula end shears cancel at
       1e-16, so THAT assertion gets EASIER as the ceiling rises -- while the second half
       compares against the counter CONSTANT and never against the ceiling.
judge  **AND THE CARVE-OUT PREMISE IS FALSE FOR ALL THREE OF F4 ENTRIES.** The counter is in
       the ceiling own quantity in every case: dimensionless relative conservation error
       against dimensionless relative conservation error; metres against metres;
       dimensionless relative against dimensionless relative. The `_COUNTER_DEFECT` suffix
       -- which report section 16 says the guard "pairs on" -- is the suffix that switches
       the ordering assertion OFF, and `_COUNTER` satisfies BOTH guards the report says
       refused it while also binding the ceiling. Measured above, one rename, nothing else.
       R671.
cmd    sweep F4_STATIC_REACTION_AGREEMENT
out    1.0e-16 -> 2 failed ; 3.0e-16 -> 1 failed (tip shear, clean worst 3.143e-16)
out    1.0e-12 -> 10 passed (shipped) ; 1.0e-6 / 1.0e-2 / 0.2 / 0.249 -> 10 passed
out    0.3     -> 1 failed  test_G4_the_defective_formula_misses_the_reaction_by_a_quarter
judge  bound above at 0.25 by its own counter, but only through an `approx(..., rel=)` and
       not by a declared ordering. A 24.9 percent tip-shear error reads green.
cmd    sweep F4_EB6_POSITION_M
out    1.0e-15 / 1.0e-14 -> 1 failed ; 1.0e-6 (shipped) / 1.0e-3 / 1.0 / 30.9 -> 10 passed
out    31.0 -> 1 failed  test_EB6_a_PERMUTED_export_reddens_the_gate
judge  bound above at 30.982842, the same way.
```

## 7. WHAT THE TEN GATES ACTUALLY READ. TRY TO BREAK IT.

```
cmd    the conservation gate with the displacement field replaced, one variable at a time
out    u_full -> zeros        worst 3.797e-16   GREEN
out    u_full * 1000          worst 0.000e+00   GREEN
out    u_full -> N(0, 1e-2)   worst 7.595e-16   GREEN
cmd    the same gate with the element equivalent load doubled
out    worst 1.000e+00   RED
judge  **R663 GATE READS NOTHING FROM THE SOLVE.** `k u` end shears cancel identically, so
       after the subtraction `carried` is minus the element equivalent load z-sum and the
       assertion is an identity of the element mass ROW SUMS against `member_mass / n`. It
       catches the omission -- which is what it was built for -- and it catches a wrong
       element mass. It cannot see a wrong displacement, a wrong stiffness or a wrong
       support scheme, and the report table calls it "the gate" for R663 without saying so.
cmd    and the body average it compares against
out    all four platform members are 50.000 m and all three of each hub 25.000 m, so
out    `member_mass / len(members)` happens to equal each element mass; NOTHING in the file
out    asserts the members are equal length, and on an unequal frame the gate FALSE-REDDENS
cmd    the tip-shear gate with the reaction map emptied on every body
out    assertions executed = 0, and pytest reports `1 passed`
rule   an empty parameter set is an error, not a skip; a vacuous pass certifies nothing
judge  the `continue` at :123 is silent. At this commit 16 of 16 members assert, which I
       measured rather than assumed -- but the count is not asserted, so the gate can go
       vacuous without a word. R675.
cmd    the duality gate, and what it is a property of
out    the Jacobian is a 3x12 matrix of 0s, 1s and -1s WRITTEN IN THE TEST
out    grep -rn map_joint_reactions over tests: ONE hit, and it is inside a docstring
out    duality_residual(zeros, zeros) = 0.0 ; duality_residual(a, -a) = 0.0 -- IDENTICAL
rule   R668 closing condition: read the shares from the Jacobian, AND the both-zero case is
       excluded from the window or raises
judge  **HALF OF R668.** The first half is done honestly: the property is asserted on a
       Jacobian and the both-blocks-plus-I mutant reads exactly 2.0, with no epsilon, which
       is the right call. The second half is untouched -- `joint_reactions.py` is not in the
       diff at all -- so a ramp start and a satisfied law still print the same number. And
       `map_joint_reactions`, the mapper this step is named for, is still called by no test.
cmd    the horizontal restraint, re-measured at THIS commit in the WEAKENING direction
out    shipped scheme            worst_horizontal 0.0 on all five bodies
out    ux,uy fixed at ALL FOUR joints -- eight DOF for three rigid motions
out                              worst_horizontal 0.0 on all five bodies
out                              platform reactions BIT-IDENTICAL: 3065625.000000 each
rule   R665 closing condition: the quantity says what it measures with a relative threshold
       and a counter, OR a check a redundant restraint reddens; either way the claim that
       the zero proves the scheme right is WITHDRAWN from static.py:21-23 and the report
judge  **NOTHING IN THE RANGE TOUCHES `floatfea/solve/static.py` OR
       `floatfea/loads/selfweight.py`.** The claim at static.py:21-23 is verbatim what it
       was, report section 3 CHECK 2 still says the zero "proves ... the right scheme
       rather than a convenient one", no threshold is declared, and no test under `tests/`
       reads `worst_horizontal_N` at all. R672.
```

## 8. THE 39 REDS, TRACED BY NAME. NOT ONE OF THEM IS A BOUNDARY RED.

EG3 state (2) is cleared BY THE ANSWERING REPORT, and the answering report is in the tree
at this commit. So its carve-out does not apply and every red below is CZ1 (iv) unchanged.
I ran the off-list ids individually rather than ruling a 39-red group by class, which is
the discipline EG3(i) exists to force and the discipline the eighty-third verdict earned.

```
cmd    python -m pytest -q, fresh clone outside OneDrive, origin resolving
out    39 failed, 2844 passed, 3 skipped, 604.75s
cmd    test_the_report_carries_the_finding, 13 parametrisations, run alone
out    "R622 is in the newest verdict ... and the newest report revision Carried section
out    does not mention it"; same for R626 R631 R635 R637 R654 R655 R657 R658 R659 R660
out    R661 R662. The parsed table is ['R663','R664','R665','R666','R668','R669',...]
judge  **THIRTEEN ITEMS VERDICT 93 CARRIES ARE ABSENT FROM THE ANSWERING REVISION Carried
       SECTION.** Revision 1 section 9 mentions some; the guard reads the NEWEST revision
       section 16, and that table has four rows. This is the precise failure CLAUDE.md
       names as the reason step gating exists -- the dependency list is what gets re-read.
cmd    test_a_report_does_not_say_CLOSED, run alone
out    ['R638'] are recorded with a word only a verdict may use
out    assert not [('R638', '**open** under EJ1, closed before F4 closes')]
out    6 status cells parsed, 1 say `closed`
cmd    the two test_report_vocabulary_corpus rows, run alone
out    legitimate_open_row and two_spaces_before_the_item_number: "the corpus requires
out    allowed and the shipped guard says refused, REPORTED BY test_a_report_does_not_say_CLOSED"
judge  R666 WAS NOT FULLY ANSWERED. The two `**CLOSED**` cells became `**answered**` -- I
       read the diff hunk -- but the R638 row carries the word `closed` in its free text,
       and the two vocabulary rows cascade off it exactly as verdict 93 predicted: one
       change into two more. Three reds, one word.
cmd    test_the_report_carries_a_WHOLE_SUITE_count, run alone
out    "the newest revision carries no whole-suite line ... Generate it with
out    `python scripts/suite_count.py`, run AFTER every other edit"
judge  section 17 is `SUITE2_PLACEHOLDER`. The implementer says so plainly and asks me to
       take the figure, which I did -- but the report is required to carry its own and the
       mechanism to produce it is committed and was not run.
cmd    the five CI-section ids, run alone
out    "the newest report revision has no `## ... CI ...` section"
judge  Verdict 93 now EXISTS under docs/reviews/F4, so section 1a reason -- "no numbered
       verdict under docs/reviews/F4" -- is no longer true at this commit, and
       `scripts/ci_section.py` would now produce the section. Revision 2 did not re-run it.
cmd    test_every_named_site_is_touched_or_declared, the 8 red parametrisations
out    R664-floatfea/solve/static.py:92
out    R665-floatfea/loads/selfweight.py:86
out    R665-floatfea/solve/static.py:21, :22, :23
out    R667-docs/closure/F3.md:179
out    R667-tests/verification/rung3/test_platform_skeleton.py:711
out    R668-joint_reactions.py:89
judge  **THE MACHINE NAMES THE UNTOUCHED SITES BEFORE I DO, AND IT NAMES THE SAME ONES.**
       Every one of these is a site a verdict-93 closing condition named; none is touched
       and none is declared. "A closing condition that names sites is closed site by site."
cmd    the 7 test_report_guard_states rows, baseline first
out    baseline RED, then non_numeric_step_suffix, superscript_digit_step_number,
out    draft_suffix_beside_a_step_report, step_number_is_the_empty_string,
out    verdict_amended_after_the_commit_the_report_answers, zero_padded_step_number
judge  identified as a cascade by the baseline being red and by each row own failure line,
       not by its name -- EH1 wording. They clear with the baseline.
judge  **SO: 39 reds, 0 on the EG3 lists, and 2793 -> 2844 passed means the step added 51
       green cases while the red set went 43 -> 39.** R673.
```

## 9. R669 -- THREE OF ITS FOUR ROWS STILL HAVE NO ASSERTION, AND THE REPORT SAYS SO

```
cmd    grep -rn over tests/ for an assertion on the four hub reactions being equal
out    no test reads `vertical_reactions_N` for a spread. EK0(d) SYMMETRY -- the only one
out    of the three the FE stiffness participates in, and the only one of batch 32 three
out    that CAUGHT anything -- is a prose row in report section 3 and nothing else.
cmd    grep -rn for G4.4 / mapping conservation / map_joint_reactions over tests/
out    one hit, inside a docstring. **G4.4 HAS NO ASSERTION.**
cmd    grep -rni for EK0(a) / premise over tests/
out    no hit under rung4. The premise check that can STOP the step is a report figure.
cmd    grep -rn for Z_HUB_REF, hub positions, or line 157 over tests/verification/rung4
out    (no output) -- DQ9 required EXTENSION to the 4 hub-platform joints is absent
rule   F4.md section 5 marks G4.4, EK0(d) symmetry, EK0(e) duality and EK0(a) "to be
       measured at step 1"; DQ9 says "Extend it to the 4 hub-platform joints against
       HSP-stable hub positions (cite file and line)"
judge  one of the four rows is now asserted (duality, on a hand-built Jacobian). Report
       section 16 says "R669 -- answered in part", which is accurate and is why I am not
       arguing about it: an item answered in part is open. R676.
judge  And this is still not apparatus. DR1 freezes guards, scanners, meta-tests, detectors
       and report generators. A gate row the locked plan prescribes for THIS step is the
       milestone work.
```

## The adversarial corpus (BE3)

**Batch 33, committed separately at `3d6fdb6`:**
`tests/corpus/f4_step1_gate_mutations.txt`, **37 entries, all new**, on F4 load-mapping
gate and EB6 label-provenance gate -- EG4(e) two standing exceptions to the corpus pause,
and the two surfaces where a miss reaches a member force. Every `measured=` field was taken
by me at `7c8e4ae`.

**COVERAGE, MEASURED AND NOT CLAIMED: of 37 new entries the step ten shipped gates plus the
two tolerance guards CATCH 10, catch 2 ONLY AFTER a named repair, leave 1 UNAVAILABLE in
CI, and MISS 24.**

```
cmd    a Counter of the expect field over the committed file
out    37 entries -- catch 10, catch_only_after_repair 2, unavailable 1, miss 24
judge  Previous batches: 4 of 11, 8 of 13, 5 of 10, then 5 of 17 last round. **10 of 37 is
       the strongest absolute count of the milestone and the step earned it** -- five of the
       ten catches are ceiling boundaries that reddened in BOTH directions, which last round
       had nothing to measure at all.
judge  The misses are not exotic and they are not spread out. **Seven of the 24 are plan rows
       with no assertion** (EK0(d) symmetry, G4.4, EK0(a), EB6 hubs, the mapper sign, the
       duality both-zero, the Jacobian provenance). **Four more are one ceiling moved
       upward.** Three are the conservation gate not reading the solve. One is the vacuous
       `continue`. One is the production signature defaulting.
judge  The entry I would put in front of the implementer is `eb6_both_tests_removed_entirely`:
       at this commit the rung fails ONLY on the two skips, so DELETING the gate turns the
       rung green. A ladder script that rewards removing a gate is the shape worth seeing.
```

## Findings

**R670. (BLOCKING -- (d), CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4.)
`tests/verification/rung4/test_f4_static_and_mapping.py:265-272` SKIPS EB6 BOTH TESTS WHEN
HSP-stable IS ABSENT, AND `scripts/run_rung.sh:274-276` FAILS A RUNG ON ANY SKIP.** Section
2 carries the log: `run_rung: FAIL -- 2 skipped in tests/verification/rung4`, with
`137 collected, 0 failed, 0 errored`, and `ladder 5` skipped behind it. **This is also my
routing of the question report section 14 hands me, and the answer is that the repository
had already taken the decision**: a `skipif` is not available inside `tests/verification/`.
Of the two alternatives the report offers I take NEITHER as stated -- vendoring the four
constants puts the expected side where a permutation can reach it, and "a gate that runs in
one place only" is the state that is red.
**Closed when** EB6 gate runs in CI without a skip. The shape that does it without
vendoring: the gate reads HSP-stable when present and otherwise reads a committed
`# expected:` fixture whose PROVENANCE is a checked-in hash of
`platform_common.py:33-36,51-58`, so the expected side is the HSP-stable value, a change
there reddens, and the export cannot reach it -- OR the EB6 gate moves out of
`tests/verification/` to a path the ladder script does not gate, with the plan row saying
which machine runs it and the closure artifact carrying its result. Either way `ladder 4`
is green at the answering commit and the `gh run view` step list is pasted.

**R671. (BLOCKING -- (b), A TOLERANCE WHOSE CEILING NOTHING BOUNDS ABOVE.)
`floatfea/tolerances.py:1888` `F4_MEMBER_FORCE_CONSERVATION` RISES FROM `1.0e-13` TO
`1.0e+6` WITH 150 TESTS GREEN -- PAST THE `1.0` ERROR R663 ITSELF PRODUCES.** Section 6
carries the sweep and the one-rename cell. The cause is the counter suffix:
`tests/verification/rung3/test_tolerance_counter_cases.py:89-94` returns early for any
`_COUNTER_DEFECT`, on the stated premise that a defect size is not in the ceiling quantity
-- and for all three of F4 entries it IS the same quantity. Renaming
`F4_MEMBER_FORCE_CONSERVATION_COUNTER_DEFECT` to `..._COUNTER`, nothing else, reddens
`test_the_ceiling_sits_below_its_counter_case` at `2.0` and stays green at `1.0e-13`.
**Closed when** the three F4 counters are declared under the suffix that brackets them --
`_COUNTER` -- so `ceiling < counter` is asserted for each, with the sweep in both directions
pasted at the answering commit; and the counter-case test second assertion compares the
defect size against the CEILING rather than against the counter constant, so that raising
the ceiling makes that assertion HARDER and not easier. Do not answer this by widening,
by exempting an entry, or by extending the rung3 guard -- the suffix that already works is
the whole repair.

**R672. (BLOCKING -- (c), CARRIED FROM VERDICT 93 AND UNANSWERED.) R665 IS UNTOUCHED AT
EVERY SITE ITS CLOSING CONDITION NAMED.** `git diff 3a908fa..7c8e4ae -- floatfea/solve/static.py
floatfea/loads/selfweight.py` is empty; `static.py:21-23` still says the zero proves the
support scheme right; report section 3 CHECK 2 still says it "proves ... the right scheme
rather than a convenient one"; no threshold is declared for `worst_horizontal_N`, which is an
absolute figure on a dimensional quantity; and no test under `tests/` reads it. Re-measured
at THIS commit: an eight-DOF restraint -- `ux, uy` at all four joints, for three rigid
motions -- gives `0.0` on all five bodies with the platform reactions bit-identical.
Report section 13 table claims the static-weight gate answers "R664, R665"; it answers R664.
**Closed when** verdict 93 condition is met at its own sites: EITHER `static.py:21-23` and
the plan EK0(d)-supports row say the quantity measures that the applied load is purely
vertical, with a RELATIVE threshold against a stated response scale and a counter; OR a
check a redundant in-plane DOF reddens, which section 7 shows today does not exist. Either
way the determinacy claim is withdrawn from `static.py:21-23` AND from report section 3.

**R673. (BLOCKING -- (d), 39 RED TESTS AT THE REVIEWED COMMIT AND NOT ONE IS A BOUNDARY
RED.)** Section 8 traces all 39 individually. The three groups that are not cascade:
**(i)** thirteen `test_the_report_carries_the_finding` rows -- R622, R626, R631, R635, R637,
R654, R655, R657, R658, R659, R660, R661, R662 -- items verdict 93 carries that the newest
revision section 16 `Carried` table does not mention; **(ii)** `test_a_report_does_not_say_CLOSED`
on `| R638 | **open** under EJ1, closed before F4 closes |`, with the two
`test_report_vocabulary_corpus` rows cascading off it, which is R666 remaining third;
**(iii)** eight `test_every_named_site_is_touched_or_declared` rows naming R664, R665, R667
and R668 untouched and undeclared sites, plus the missing CI section (five ids) and the
missing whole-suite line (`SUITE2_PLACEHOLDER`). EG3 state (2) is cleared BY the answering
report and the answering report is in the tree, so the carve-out does not apply.
**Closed when** all 39 are green at the answering commit with the `FAILED` list pasted, or
each remaining red traces by name to a state EG3 actually lists; section 16 `Carried` names
every item verdict 93 and this verdict carry; the R638 row drops the word `closed`; section
17 carries `python scripts/suite_count.py` output taken AFTER the last edit (CP3); and the
CI section is generated now that a numbered F4 verdict exists.

**R674. (BLOCKING -- (b) and (c), THE COUNTER-CASE DOES NOT RUN THE INJECTION IT NAMES, AND
THE GATE IS SIGN-BLIND ON THE ROW THE VERDICT MEASURED.)**
`tests/verification/rung4/test_f4_static_and_mapping.py:161` compares `abs(case.applied_N)`
with `case.weight_N + handed`. Measured in section 5: with `GRAVITY_VECTOR` negated the
platform row reads `applied 1.226250e+07` against `expected 1.226250e+07`, `rel 0.000e+00`,
**PASS**; the gate reddens only through the four hub rows, i.e. only through the handed-down
term, so a body with no upstream body is sign-blind. And
`test_G4_1_static_the_weight_check_REDDENS_on_the_two_worst_misses[gravity_reversed]`
corrupts the EXPECTED side (`corrupt = -case.weight_N`) instead of the model, so the
declared counter-case never ran the injection it is named for. `static.py:86-91` own
docstring says the sign is "the one error this check exists for".
**Closed when** the gate compares the SIGNED applied load against the signed expected load,
so a reversed field reddens on every body including the platform; and the two counter-cases
are injected into the MODEL -- `GRAVITY_VECTOR` negated, the remainder diagonal dropped --
and re-solved, with the measured relative error pasted per body. My figures to beat:
`5.000e-01` for the dropped remainder on the platform and a platform row that must stop
reading `0.000e+00` under reversal.

**R675. (BLOCKING -- (c), TWO GATES WHOSE REACH IS NARROWER THAN THE TABLE CLAIMS, ONE OF
THEM VACUOUSLY PASSABLE.)** Section 7. **(a)**
`test_G4_the_tip_shear_equals_the_support_reaction:123` skips a member with a silent
`continue`; with the reaction map empty, 0 assertions execute and pytest reports `1 passed`.
**(b)** `test_G4_member_end_shears_sum_to_the_load_the_member_carries` reads nothing from the
solve -- `u_full` zeroed gives `3.797e-16`, times 1000 gives `0.000e+00`, randomised gives
`7.595e-16`, all GREEN -- because after the subtraction the assertion is an identity of the
element mass row sums against `member_mass / len(members)`; and that body AVERAGE equals each
element mass only because all four platform members are `50.000 m` and all three of each hub
`25.000 m`, which nothing in the file asserts.
**Closed when** the tip-shear gate asserts the number of comparisons it made (16 at this
commit) and RAISES on an empty set rather than passing; and the conservation gate compares
against each ELEMENT own mass rather than a body average, or states in its docstring that it
is an identity of the mass row sums with no reach into the solve and names the test that does
have that reach.

**R676. (BLOCKING -- (c), CARRIED FROM VERDICT 93 AND ANSWERED FOR ONE ROW OF FOUR.) THREE
OF R669 FOUR GATE ROWS STILL HAVE NO ASSERTION, AND DQ9 REQUIRED HUB EXTENSION IS ABSENT.**
Section 9 carries the greps. **EK0(d) platform symmetry** -- the only one of EK0(d) three
checks the FE stiffness participates in, and the only one batch 32 measured as catching
anything -- is a prose row in report section 3 and nothing reads `vertical_reactions_N` for a
spread. **G4.4** mapping conservation has no assertion and `map_joint_reactions` is called
by no test. **EK0(a)** the premise that can STOP the step is a report figure. **EB6 hub
extension** at `platform_common.py:157` with `:130` and `:102` does not exist; nothing under
`tests/verification/rung4` mentions `Z_HUB_REF`. Report section 16 records this as "answered
in part", which is accurate.
**Closed when** each of the three rows is an assertion under `tests/` with a counter that
reddens it and an expected value read from something other than the object under test (EA4);
the EB6 hub side ships against `:157`; and every `cmd` line reporting them in the revised
report is a command I can run. For EK0(d) symmetry the discriminator is already measured and
free: one arm `I_y`, `I_z`, `J` reduced `100x` gives reactions `671905.5` and `5459344.5`,
spread `1.5617` against a clean `9.11e-16`.

**R677. (BLOCKING -- (a) and (b), R663 CLOSING CONDITION SECOND BRANCH IS NOT MET: IT
DEFAULTS.)** `floatfea/post/member_forces.py:95` declares
`f_eq_global: NDArray[np.float64] | None = None` and the docstring says "that default is
correct only for a member carrying nothing but its end actions. R663 is what omitting it
costs." Verdict 93 condition was "forms the element nodal force MINUS the element equivalent
load, OR takes that load as an argument and RAISES when it is not supplied -- it raises, it
never defaults." Neither branch holds: the subtraction is conditional on an argument that
defaults to the defect. Measured: `member_forces(body, member, u)` returns silently with tip
`Vz = 2.299219e+06`, the R663 value, and no production module calls this function at all, so
the first caller written after this step inherits the defect by omission.
**Closed when** omission raises. The cheap form: a module-level sentinel the caller must pass
to assert there is no distributed load -- `member_forces(body, member, u, NO_DISTRIBUTED_LOAD)`
-- so the three counter-case call sites that NEED the defective path say so explicitly and a
future production caller cannot reach it by forgetting. "An unsupported case raises, it never
defaults" is the recorded guard and this is the clearest instance of it in the step.

**R678. (BLOCKING -- (c), R668 SECOND CLAUSE, UNTOUCHED.) `duality_residual` STILL RETURNS
`0.0` FOR A BOTH-ZERO SHARE, WHICH IS THE SAME NUMBER A SATISFIED LAW RETURNS.** Measured:
`duality_residual(zeros, zeros) = 0.0` and `duality_residual(a, -a) = 0.0`, identical.
`floatfea/loads/joint_reactions.py` is not in the diff. The published `0.000e+00` over all six
cases cannot distinguish a satisfied law from an absent load, which is what verdict 93 asked
to be fixed alongside the Jacobian half -- and the Jacobian half WAS done well, including the
exact `2.0` mutant with no epsilon.
**Closed when** the both-zero case is excluded from the window or raises, so the window figure
is a statement about a law rather than a value an absent load also prints.

## Closure items

Not re-reviewed item by item. Fixed once, in the step closure commit (CZ0). **C135 to C143
from verdict 93 are still open and go into the same list.**

* **C144.** Report section 13: "`tests/verification/rung4/test_f4_static_and_mapping.py`,
  9 tests" and "out 9 passed". Measured: **10 passed** where HSP-stable exists and
  **8 passed, 2 skipped** where it does not. No tree produces 9. CP3 -- the figure was taken
  before the last edit. Closes when it is re-taken after the final edit, with the machine
  named, both states reported.
* **C145.** Report section 13: "widen EB6_POSITION_CEILING from 1.0e-6 to 1.0e+3" names a
  constant that does not exist at this commit (`F4_EB6_POSITION_M` does), and the pasted
  "1 failed, 8 passed" is 9 of 10. My own re-take: widening to `1.0e+3` gives
  `1 failed, 9 passed`, and the one failure is the counter-case. The conclusion is right and
  the figure and the name are stale.
* **C146.** `test_f4_static_and_mapping.py:285` -- "The constants are read from the file, so a
  change there reaches this gate." Two of the four are LITERALS in the test:
  `buoy = [0.0, 120.0, 240.0]` at :294 and `radius = 0.5` at :295. It fails safe (a change
  reddens) and the sentence is false for half the expected side. CW0.
* **C147.** Report section 16: "the four constants F4 step 1 declares", and the block lists
  four. **Six** are declared and `docs/milestones/F4.md` section 5a lists six. The same
  section says the guard "REFUSED ME THREE TIMES" where the invocation says six.
* **C148.** Report section 13 table: the static-sum gate row answers "R664, R665". It answers
  R664. R672 is the blocking half.
* **C149.** `floatfea/tolerances.py:1942-1947`, the `F4_STATIC_REACTION_AGREEMENT_COUNTER_DEFECT`
  entry: "The hub arms are 20.69%, so the platform value is the TIGHTER of the two and is the
  one declared." `0.2069 < 0.25`, so the hub value is the tighter one. The declared `0.25` is
  correct for what the test does with it -- an equality check on one platform member -- and the
  word is wrong. Closes when the sentence says the platform value is the one the test injects
  and the hub value is the smaller of the two.
* **C150.** `docs/milestones/F4.md` section 5a row for `F4_EB6_POSITION_M`: "both edges
  solved". Measured: the clean worst is exactly `0.000000e+00 m`, so DQ9 lower edge is
  vacuous and only the upper one binds. The tolerance entry itself says this correctly; the
  plan row does not.
* **C151.** Report section 1a is now false at this commit -- a numbered verdict DOES exist
  under `docs/reviews/F4` -- and it is revision 1 prose kept unchanged. EK3 governs: it is
  fixed in the next report or in `docs/closure/**`, and it does not open a round. Related
  red is in R673 (iii).

## Carried

Verdict 93 named **seven blocking items**, nine closure items, and a nine-item
`Next step opens when`. Every one, with its status and where.

* **R663 -- ANSWERED on its principal claim, OPEN on its second branch.** The subtraction
  is made at `member_forces.py:124-128`, verified independently in section 3: tip shear
  equals the support reaction to `3.143e-16` over 16 of 16 members, conservation worst
  `5.696e-16`, the preview reissued as issue 2 in the SAME commit (BP0 respected). **The
  "it raises, it never defaults" half is NOT met -- R677.** The gate the condition named --
  the tip moment at a roller, true value `0`, defective value minus `mu L^2 / 12` -- was not
  built; two other gates that redden on the omission were, and I accept the substitution on
  substance while recording that the named site was not the one used.
* **R664 -- ANSWERED on its principal direction, OPEN on its sign and its injection.**
  `weight_N` now enters a comparison and the half-mass injection reads `5.000e-01` where it
  read `3.038e-16`. Section 5 carries both physical injections. **R674** is the remainder.
  The causal sentence at `static.py:86-91` the condition also named is untouched.
* **R665 -- OPEN AND UNANSWERED AT EVERY NAMED SITE. R672.** `static.py` and `selfweight.py`
  are not in the diff; re-measured at this commit, an eight-DOF restraint still reads `0.0`
  with bit-identical reactions. The machine names four of the sites itself in R673 (iii).
* **R666 -- ANSWERED TWO THIRDS.** The two `**CLOSED**` cells became `**answered**` and the
  `**ledgered**` cell became `**open**` -- I read the diff hunks. The R638 row free text
  still carries the word `closed`, `test_a_report_does_not_say_CLOSED` is red, and the two
  vocabulary rows cascade off it. Section 1b "ONE CAUSE" is corrected in section 15, which
  the condition asked for and which was done. Remainder inside R673 (ii).
* **R667 -- ANSWERED on the first side, OPEN on the hub extension and ROUTED on the skip.**
  The first side ships reading `platform_common.py` and I verified it against all 66
  transpositions. DQ9 extension to the four hub-platform joints is absent (R676). The skip
  is not a routing question any more: it is R670, a red rung, and the routing is written
  there.
* **R668 -- ANSWERED on the Jacobian half, OPEN on the both-zero half. R678.** The mutant
  reading exactly `2.0` with no epsilon is the right call and I say so. The Jacobian is
  hand-built, which is honest for a unit property and does not reach FloatSim own; recorded
  as a corpus miss rather than a finding.
* **R669 -- ANSWERED FOR ONE ROW OF FOUR. R676.** The report says "in part" and that is
  correct.
* **C135 to C143 -- OPEN, absorbed in the closure commit, not re-reviewed (CZ0).** Nothing
  in the range touches their sites and the report routes them correctly.
* **R656 -- OPEN WITH XABIER, unchanged.** `scripts/ci_section.py` is not in the range. The
  milestone-boundary gap verdict 93 raised alongside it is now MOOT in one direction -- the
  answering report exists, state (2) has cleared, and the reds at this commit are the
  report own incompleteness rather than the boundary -- which is itself the answer to
  whether the boundary needed a new state: it did not.
* **R653 -- OPEN, carried, becomes (c) at step 2.** A grep for `RHO_INF` over `tests` and
  `floatfea` still gives no output. Carries by name into step 2.
* **R638 -- OPEN, unchanged, EJ1 governs, closed before F4 closes.** The six new F4 entries
  do not touch it. Note that its Carried ROW is what reddens
  `test_a_report_does_not_say_CLOSED`.
* **R637 clause (iii) -- NOT ANSWERED THIS ROUND.** The whole-suite line is
  `SUITE2_PLACEHOLDER`, so the one figure this clause exists to pin does not exist at the
  commit it describes. Its new object is R673.
* **R657, R658, C119, R659, R660, R661, R662, R654, R655 -- CLOSED at verdict 93, not
  reopened.** Nothing in this range touches their sites. **They are still named in verdict
  93 Carried section, which is why their absence from report section 16 is red (R673 i).**
* **R622, R626, R631, R635 -- carried on the EJ3 ledger at `docs/closure/F3.md` section 8,
  unchanged and not re-reviewed (CZ0).** Also absent from section 16 and part of R673 (i).
* **The EJ4 residual-location hand-over -- unchanged, live at step 2** where `3.96e-06` is
  the reference.
* **Verdict 93 `Next step opens when`, item by item.** (1) R663 -- **ANSWERED, second branch
  open (R677)**. (2) R664 -- **ANSWERED, sign and injection open (R674)**. (3) R665 --
  **NOT ANSWERED (R672)**. (4) R666 -- **TWO THIRDS (R673 ii)**. (5) R667 -- **first side
  ANSWERED, hub extension open, skip is R670**. (6) R668 -- **Jacobian half ANSWERED,
  both-zero open (R678)**. (7) the four gate rows -- **ONE OF FOUR (R676)**; I said I would
  run them and I did. (8) the schedule paragraph -- **KEPT AND NOT UPDATED**: report section
  1 is revision 1 text and reads "no slippage to report today" at a commit three items
  further on. See the schedule note below. (9) "nothing here is new apparatus" -- I say it
  again for every item above.
* **What I said I would not accept, and whether it was offered.** A tolerance making R663
  figures agree with the old ones -- **NOT OFFERED**; the figures moved and the preview was
  reissued. "Zero by construction" offered as a reason a check needs no counter -- **NOT
  OFFERED**. A `cmd` line that describes a command instead of being one -- **STILL PRESENT
  in revision 1 sections 2, 3, 4, 6 and 7**, which revision 2 did not regenerate; the
  revision-2 sections 12 to 16 are mostly real commands and that is the improvement.

## Tolerances touched

**SIX DECLARED, NONE MOVED. All six are new; no existing value, form, counter or injection
changed.** I diffed the file separately per my instruction 4, because that is where the
cheapest wrong fix lands, and I read all 84 lines.

| constant | old | new | form | counter | injected by | my judgement |
|---|---|---|---|---|---|---|
| `F4_MEMBER_FORCE_CONSERVATION` | none | `1.0e-13` | dimensionless, relative -- correct form | `..._COUNTER_DEFECT = 0.5` | `test_G4_the_conservation_gate_REDDENS_without_the_equivalent_load` | **ceiling UNBOUNDED ABOVE -- R671** |
| `F4_MEMBER_FORCE_CONSERVATION_COUNTER_DEFECT` | none | `0.5` | dimensionless | is the counter | the same test | value fine; the SUFFIX disables the bracket -- R671 |
| `F4_EB6_POSITION_M` | none | `1.0e-6` | metres, full scale, absolute on a dimensional quantity | `..._COUNTER_DEFECT = 30.982842` | `test_EB6_a_PERMUTED_export_reddens_the_gate` | **ACCEPTED.** A position tolerance on a geometry gate is a length, not a response ratio; the counter is the true minimum over all 66 transpositions and it binds the ceiling at `31.0`. Lower edge vacuous and the entry says so. |
| `F4_EB6_POSITION_M_COUNTER_DEFECT` | none | `30.982842` | metres | is the counter | the same test | **ACCEPTED**, verified `30.982841873` over all 66 |
| `F4_STATIC_REACTION_AGREEMENT` | none | `1.0e-12` | dimensionless, relative | `..._COUNTER_DEFECT = 0.25` | `test_G4_the_defective_formula_misses_the_reaction_by_a_quarter` | bound at `0.25` by an `approx` rel and not by a declared ordering -- R671. Second use, the weight gate, is NOT what the plan section 5a row says it bounds. |
| `F4_STATIC_REACTION_AGREEMENT_COUNTER_DEFECT` | none | `0.25` | dimensionless | is the counter | the same test | value correct for the platform member it injects; the "TIGHTER of the two" sentence is wrong -- C149 |

```
cmd    git diff 3a908fa..7c8e4ae -- floatfea/tolerances.py      [separately, instruction 4]
out    84 insertions, 0 deletions
cmd    pytest tests/test_plan_matches_tolerances.py tests/test_no_tolerance_literals.py
         tests/verification/rung3/test_tolerance_counter_cases.py -q
out    273 passed with the rung4 file ; and EVERY perturbation of the three ceilings
out    reddens test_plan_matches_tolerances, so the plan table and the file agree
rule   every numerical tolerance lives in floatfea/tolerances.py and moves with a plan edit
judge  **THE PLAN EDIT IS REAL AND CORRECTLY PAIRED.** `docs/milestones/F4.md` section 5a
       moves all six and the guard pins each value, which I verified by moving each and
       watching it redden. The machinery that refused six times was right six times and
       the report says so; what the report does not say is that the SIXTH refusal -- the
       suffix -- was answered with the one name that switches the bracket off.
judge  And `F4_EB6_POSITION_M` is an ABSOLUTE tolerance on a dimensional quantity, which
       the recorded guard normally calls a defect. It is not one here and I want the reason
       on the record: the subject is a POSITION against a fixed geometry, the response
       scale is the geometry itself, and the counter is a length in the same units. A
       relative form would divide by a radius that is `0.0` for a centre node. Accepted.

## On the schedule, because nobody raised it this round

Report section 1 is revision 1 prose and still reads "Measured against EK4 preview target
of 8 Oct: HELD, three days early ... No slippage to report today." That was true on 5
October at revision 1. **Revision 2 did not update it, and CZ0 says slippage is reported THE
DAY IT IS KNOWN.** I am not making this a blocking finding -- it is report prose -- but I am
putting the arithmetic on the record so the next revision writes it rather than discovers it:
F4 is committed for **19 Oct** with a working target of 14 Oct; this is **round 2 of 3** on
step 1 of three steps; nine items are open above, of which R670 needs a CI-visible design
decision and R676 needs three gate rows built. **Two steps remain after this one and the
member-force table is committed for 23 Oct.** If step 1 consumes its third round, the choice
CZ0 names -- slip the date or reduce scope -- is live and the report paragraph is where it
gets stated.

## Next step opens when

Step 2 does not open. These are answered first and the step is re-invoked. **Round 2 of 3 on
F4 step 1. The next round is the LAST (CZ0, and DK0 means no re-lock buys more).**

1. **R670 -- `ladder 4` is GREEN in CI at the answering commit**, with the `gh run view` step
   list pasted, and EB6 gate runs rather than skips. This is the one item that cannot be
   answered by prose and the one I would fix first.
2. **R671 -- the three F4 counters are declared under `_COUNTER`** so `ceiling < counter` is
   asserted, and the conservation counter-case second assertion compares against the CEILING.
   Paste the sweep in both directions. `1.0e+6` with 150 green is the number it has to stop
   printing.
3. **R672 -- R665 at its own sites**, or the determinacy claim withdrawn from
   `static.py:21-23` and report section 3. The eight-DOF cell is the discriminator and it is
   already measured.
4. **R673 -- all 39 reds green, or each remaining red matched by name to a state EG3 lists.**
   Section 16 `Carried` names every item verdict 93 and verdict 94 carry; the R638 row drops
   the word; section 17 carries `scripts/suite_count.py` run AFTER the last edit; the CI
   section is generated.
5. **R674 -- the weight gate compares SIGNED quantities**, and both counter-cases are
   injected into the model and re-solved.
6. **R675 -- the tip-shear gate asserts its comparison count and raises on an empty set**;
   the conservation gate compares per element or says what it is an identity of.
7. **R676 -- EK0(d) symmetry, G4.4 and EK0(a) are assertions**, and EB6 hub side ships
   against `platform_common.py:157`. Every `cmd` line reporting them is a command. **I will
   run them.**
8. **R677 -- omission raises.** A sentinel the caller must pass is the cheap form.
9. **R678 -- the both-zero duality case is excluded or raises.**
10. **The schedule paragraph is REWRITTEN at revision 3**, not carried from revision 1, with
    the 19 Oct and 23 Oct dates measured against two remaining steps and one remaining round.

**What I will not accept as an answer:** widening any of the three new ceilings; exempting an
F4 entry from the counter bracket, or extending the rung3 guard instead of using the suffix
that already works; "it fails safe" offered as a reason a gate needs no counter; a
counter-case that injects into the expected side when the model is the thing under test; or
a skip reason, however well worded, standing in for a gate that runs.

**And what I want on the record for the implementer rather than against them.** Three things
in this round are genuinely good and two of them are the hardest kind. **R663 is fixed, and
the implementer wrote down against itself that its own published hand-check was the bug
restated and would have reddened on the correct answer** -- that is the sentence a reviewer
cannot extract and an author has to volunteer. **The EB6 first side is correct and I attacked
it from four directions** -- the permuted export rather than the permuted expectation, all 66
transpositions, both ceiling edges, and the provenance of each of the four constants -- and it
survived all four. **And the Jacobian mutant asserting exactly `2.0` with no epsilon, on the
ground that `x + (-x)` is exact in binary floating point, is the right instinct about when a
tolerance is not wanted**; two literals went away instead of being exempted. What the round
shows is the mirror of last round: the step now has instruments, and six of my nine findings
came from moving the instruments own thresholds rather than from reading its code.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 1
Reviewed commit: 80e24df8d801e349b22a47e96b95063179636258
Verdict: HOLD
**Reviewed commit: `a7fefba1eb55e69a0cab8a9c640396229a1548bd`** (HEAD of F3 at invocation,
pushed). My corpus commit `80e24df` lands first, so the script's `Reviewed commit:` stamp
and the judged commit differ; DU1 says restate the judged one and this is it.
Tests: 2793 passed, 43 failed, 1 skipped   (MY OWN run, ONE invocation, no `--ignore`, no
deselection, in a fresh clone outside the OneDrive tree, 504.12s. The 43 FAILED ids are
IDENTICAL to the report's section 1b list -- `diff` over the two sorted sets is empty.)
**CI at the reviewed commit: run `37337908921`, conclusion FAILURE.**

## Round of 2026-10-05 -- NINETY-THIRD verdict. F4 step 1, first round of three.

**HOLD.** Six blocking findings: one defect in `floatfea/` measured against an independent
recovery, four gate assertions that cannot fail, and two red tests that do not trace to the
milestone boundary. Nine closure items. The largest single fact about this step is that
**nothing in the repository imports any of the 669 lines it shipped**, so not one figure in
the report can be regenerated by running the shipped tests at the report's own commit --
and I reproduced section 3's table myself, to every digit, by writing the driver that does
not exist.

Two things I owe you up front. **R657, R658 and C119 are CLOSED and the word is mine, not
yours** -- see `## Carried`, and see R666 for why your report may not say it. And **verdict
92's `Next step opens when` item 5 is WITHDRAWN: you were right to refuse it**, for the
reason section 1a of your report gives, in those words.

## 1. THE PREMISE CHECK, THE DIFFS, AND MY OWN INSTRUCTIONS

```
cmd    git diff --stat 6426ca4..a7fefba -- floatfea
out    5 files, 669 insertions, 0 deletions -- joint_reactions.py, selfweight.py,
out    member_forces.py, inertia_relief.py, static.py
cmd    git diff 6426ca4..a7fefba -- floatfea/tolerances.py        [instruction 4, separate]
out    (no output) -- NO TOLERANCE DECLARED OR MOVED, your section 10 holds
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"   [instruction 4c]
out    tests/conftest.py                                 -- the instruction is intact
cmd    git diff 6426ca4..a7fefba -- tests/conftest.py "tests/**/conftest.py"
out    (no output) -- nothing the ladder's gate reads was rewritten from a rung
cmd    git diff 6426ca4..a7fefba -- .claude docs/SUPERVISOR.md     [instruction 4b]
out    (no output) -- NO STOP-CLASS FINDING. My own instructions are untouched in the
out    whole range, and I diffed them rather than inferring it from a green suite.
cmd    git diff --stat 6426ca4..a7fefba -- tests
out    test_report_carried.py 21, test_report_guard_states.py 42 -- both in standalone
out    `process:` commits citing EK2, both read line by line below
```

**EK0(a) -- the premise that could have stopped the step. NO STOP, and I accept it on its
mechanism rather than on its figure.** Your `0.000000e+00 N` over 24006 steps I cannot
re-take; the pinned FloatSim state is not on my instrument this round. What I CAN check is
the mechanism you name, and it is checkable: the five FE bodies carry no `hydro_body_label`,
so no excitation channel addresses their rows, and `docs/closure/F3.md` section 6a already
measured that the balance of those five bodies is `|M a| ~ |G^T lam|` with `|applied| = 0`.
**Zero by construction is a stronger result than zero by measurement and you said so,
including the part against yourself** -- that the check cannot catch a body acquiring a
label later. That sentence is why EK0(a) is a per-step gate and not a one-off, and it is the
best-reasoned paragraph in the report.

## 2. CI AT THE REVIEWED COMMIT (CA2), FROM `gh` AND NOT FROM A PASTE

```
cmd    gh run list --commit a7fefba1eb55e69a0cab8a9c640396229a1548bd --json ...
out    [{"conclusion":"failure","databaseId":37337908921,"status":"completed"}]
cmd    gh run view 37337908921 --json jobs -- job and STEP level
out    lint, unit and guards        FAILURE
out      actionlint success / ruff success / black --check success / mypy success
out      unit tests success / **guards and meta-tests FAILURE**
out    the verification ladder      SUCCESS -- all six rungs
out    CI determinism (two jobs)    skipped
rule   CA2: a red CI is a HOLD regardless of what the local run says; an unfinished run
       is not a pass; CK2's third state is `runner_name: ""`, no steps, two seconds
judge  **IT IS NOT CK2.** The run executed, the jobs carry steps with real durations, and
       `guards and meta-tests` is SEEN TO HAVE RUN rather than skipped behind an earlier
       red step -- which is the one thing CZ1 (iii) exists to make visible. So this is a
       real red. The ladder is green on all six rungs and lint/mypy/black/ruff are green,
       which localises the red exactly where my local run puts it.
judge  I also record that your short-sha warning is right: `gh run list --commit a7fefba8`
       returns `[]` silently. I used the full sha throughout.
```

## 3. THE 43 REDS -- TRACED BY NAME, THEN CELLED. **THREE OF THEM ARE NOT THE BOUNDARY.**

Your section 1b does the hard half honestly: you declined EG3's carve-out because the state
is wider than its named list, and you pasted all 43 so "only those" is checkable. It is.

```
cmd    my FAILED set, sorted, against your section 1b list, sorted
out    diff empty -- 43 ids, IDENTICAL SETS
judge  the "only those" claim is VERIFIED, and that is EG3(i) satisfied on its face.
```

**But EG3(i) asks for the trace, and a trace is one variable away from being a guess. I
celled it, and the single-cause claim is REFUTED.** Four states, one variable each, in a
scratch clone at `a7fefba`:

```
cmd    (i) commit a stub verdict to docs/reviews/F4/step-1.md, nothing else
out    43 failed -> 33 failed.  10 CLEAR.  0 NEW.
cmd    (ii) then change `**CLOSED**` to `**answered**` in section 9, ONE WORD
out    33 -> 32.  `test_a_report_does_not_say_CLOSED` clears.
cmd    (iii) then change `**ledgered**` to `**open**` for R656, ONE WORD
out    32 -> 29.  `test_every_carried_item_carries_one_of_the_report_words` clears, and
out    the TWO `test_report_vocabulary_corpus` rows clear with it
cmd    (iv) the remaining 29, each failure line read
out    EG3 state (2)'s named list plus the cascade off a still-red baseline
cell   ONE VARIABLE PER STEP, nothing else moved, each measured on its own
rule   EG3(i): a red that does not match the state's own list is CZ1 (iv) unchanged
judge  **THREE OF THE 43 ARE THE REPORT'S OWN CARRIED-TABLE VOCABULARY, NOT THE MILESTONE
       BOUNDARY.** One of them cascades into two more. They would be red at any commit with
       this table in it, verdict or no verdict. Filed as R666.
judge  AND THE BOUNDARY HALF OF YOUR CLAIM IS CONFIRMED STRONGER THAN YOU PUT IT: the
       verdict clears 10 and introduces NOTHING. The remaining set is a strict subset. That
       is the self-clearing property EG3 describes, arriving at a milestone boundary where
       its two lists do not reach.
judge  This is exactly the shape the eighty-third verdict earned EG3(i) on -- eight planted
       states ruled as one cascade by class, and the eighth was R629, a real defect sitting
       inside a group nobody read individually. Forty-three is a larger group and the same
       trap. **I nearly fell into it: your list is complete and your cause is wrong for
       three of its entries, and nothing but the cell separates those two statements.**
```

## 4. TRY TO BREAK IT -- THE MEMBER-FORCE RECOVERY IS WRONG, AND THE PUBLISHED HAND-CHECK REDDENS ON THE CORRECT ANSWER

I could not break the step with a stubby beam or a skew rotation, because the step ships no
assertion to break. So I built the driver it does not have, reproduced section 3 to every
digit, and then injected.

```
claim  `member_forces` returns the element nodal force `k u` and OMITS the element's own
         equivalent load, so it is not the member internal action EK1 asks for
cmd    for platform:hub1_arm: form `f^e_eq = M_e (T a_g)` from `local_mass` and compare
         `k u` against `k u - f^e_eq`, full scale, static case
out    station          shipped `k u`        `k u - f^e_eq`    truth
out    tip  Vz        2.299219e+06        3.065625e+06    = the tip support reaction
out                                                        3065625.000000002, EXACTLY
out    tip  My       -6.386719e+06       -3.73e-09        = 0, a vertical roller carries
out                                                        no moment
out    root Vz       -2.299219e+06       -1.532813e+06
out    root My        1.213477e+08        1.149609e+08
out    Vz_A + Vz_B            0.0         1.532813e+06    = the member's own weight
out                                                        1532812.5 N
out    shipped tip My = -6386718.75 = -mu L^2 / 12 EXACTLY -- the fixed-end moment that
out    should have been subtracted
rule   element nodal force recovery with distributed loads, `f_end = k u^e - f^e_eq`
       (Cook, Concepts and Applications of FEA); the module's own docstring at :3-5
       asserts the opposite and calls it "the element's own equilibrium"
judge  **`k u` lies in the space with the rigid null vectors, so its two end shears sum to
       zero IDENTICALLY -- measured 0.0 -- and the member's own weight can therefore never
       appear in it, whatever the member carries.** That is the mechanism, and it is not a
       convention one could adopt: there is no reading under which a roller support carries
       6.39e+06 N.m.
cmd    the same over all 16 members, shipped against corrected
out    platform arms: Vz ratio 0.7500 on all four, My ratio 1.0556 on all four
out    hub arms:      Vz ratio 0.7931 on all twelve, My ratio 1.0435 on all twelve
out    worst: shear 25.0 percent LOW, root moment 5.56 percent HIGH, tip moment infinite
out    relative error on a true zero
```

**AND THE PUBLISHED CHECK IS THE SAME IDENTITY, WHICH IS WHY IT AGREED.**

```
claim  section 5's "independent arithmetic check" cannot fail for the shipped code and
         DOES fail for the correct code
cmd    the hand value as section 5 forms it: `R - half the member weight`
out    3065625.0 - 766406.25 = 2299218.75 -- IDENTICAL to the computed 2.299219e+06, to
out    every digit, not to the 4 digits the report claims
cmd    the same hand value against three mutations
out    shipped        k u          tip Vz 2.299219e+06   MATCHES the hand value
out    `k u - 2 f^e`               tip Vz 3.832031e+06   fails it
out    `k u + f^e`                 tip Vz 1.532813e+06   fails it
out    CORRECT `k u - f^e`         tip Vz 3.065625e+06   FAILS IT
rule   a gate carries its own failure: if the thing it claims were false, would this go red
judge  **IT GOES RED IF THE THING IT CLAIMS IS TRUE.** Nodal equilibrium makes
       `k u = R - f_applied_at_node` an identity the solve enforces to round-off, so the
       hand value and the computed value are the same number arrived at twice. The check
       certifies the defect. It is the strongest instance of the instrument-defect shape
       this milestone has produced, and four of this milestone's defective instruments were
       written while the element was fine -- this time the instrument and the element are
       wrong together and the instrument says so.
judge  Published reach: EVERY `Vz` and `My` cell in BOTH tables of
       `docs/reports/F4/preview-PRELIMINARY.md`, and section 5 of the report.
```

## 5. THE THREE EK0(d) CHECKS, INJECTED. **TWO OF THEM CANNOT FAIL.**

Six injections, one variable each, full scale, platform unless stated.

```
cmd    where `gravity_load` is nonzero, by component
out    ux 0.000000e+00   uy 0.000000e+00   rz 0.000000e+00
out    uz 6.131250e+06   rx 6.386719e+06   ry 6.386719e+06
judge  THE IN-PLANE SUBPROBLEM IS HOMOGENEOUS. The horizontal restraint fixes only
       in-plane translational DOF, so its reactions are exactly 0.0 for ANY restraint.
cmd    WEAKENING DIRECTION, EH4: `ux, uy` fixed at ALL FOUR joints -- eight DOF for three
         rigid motions, grossly redundant, the opposite of minimal-determinate
out    worst_horizontal = 0.000e+00 ; reactions unchanged at 3065625.000000 each
cmd    the same with `ux, uy, rz` at joint 0 plus `ux, uy` at joint 1
out    worst_horizontal = 0.000e+00
cmd    STRENGTHENING DIRECTION: tilt GRAVITY_VECTOR and solve for the boundary
out    tilt 1e-16 -> 1.226e-09 N ; 1e-12 -> 1.226e-05 ; 1e-06 -> 1.226e+01 ;
out    1e-03 -> 1.226e+04 N
rule   EH4: both directions, including the two that WEAKEN a gate
judge  **THE QUANTITY MEASURES WHETHER THE APPLIED LOAD IS PURELY VERTICAL. IT SAYS NOTHING
       ABOUT THE RESTRAINT.** The locked plan's own row says "zero by construction"; your
       section 3 and `static.py:21-23` then upgrade it to proof that the scheme is right
       rather than convenient, and that upgrade is what I block on. **And no threshold is
       declared anywhere**, so `worst_horizontal_N` -- an ABSOLUTE figure on a dimensional
       quantity -- has no injection size that counts as caught.
cmd    the remainder mass dropped from the mass matrix: HALF the platform's mass gone
out    sum_err 3.038e-16 ; worst_horizontal 0.000e+00 ; four reactions EQUAL at 1532812.5
out    weight_N 12262500 against applied_N -6131250 -- a factor of two, never compared
cmd    GRAVITY_VECTOR sign reversed: gravity pointing UP
out    sum_err 0.000e+00 ; worst_horizontal 0.000e+00 ; four reactions equal at -3065625
cmd    the handed-down platform reaction sign-flipped, on hub1
out    sum_err 1.599e-16 ; hub reactions 3883125.0 against a correct 5926875.0
cmd    the handed-down platform reaction omitted, on hub1
out    sum_err 3.797e-16 ; hub reactions 4905000.0
judge  **ALL THREE EK0(d) CHECKS READ CLEAN ON FOUR SEPARATE WRONG LOADS, ONE OF WHICH IS
       HALF THE STRUCTURE'S MASS AND ANOTHER OF WHICH IS GRAVITY POINTING UP.** `sum_error`
       at `static.py:92` compares `sum_vertical` against `applied` -- both derived from the
       same `f` -- so it is an identity the solve enforces. `weight_N`, the one
       independently formed number in the dataclass, enters NO comparison.
judge  AND THE DOCSTRING'S REASON IS REFUTED BY ITS OWN CELL. `static.py:86-91` says
       writing it as a difference "would read as satisfied when the reactions had the wrong
       sign, which is the one error this check exists for." Measured: the SUM form reads
       satisfied too, when the whole load has the wrong sign. BG0.
cmd    AND WHAT DOES WORK, so the finding is not a blanket one
out    one arm's `I_y`, `I_z` and `J` reduced 100x: reactions 671905.5 and 5459344.5,
out    spread 1.5617 against a clean 9.11e-16 -- **the symmetry check CAUGHT it**
out    `_retained` order reversed: sum_err 4.959, worst_horizontal 2.077e+08 -- CAUGHT,
out    but NOT by the width assertion `static.py:111-113` credits, since a permutation
out    preserves width; it is the reported reactions that go loud
judge  So EK0(d)'s symmetry check has real content and is the only one of the three that
       the FE stiffness participates in -- which is what your section 3 says about it, and
       that part is correct.
```

## 6. THE DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE CODE THE REPORT DESCRIBES IS NOT IN THE TREE

```
claim  section 4: "The shipped check forms `g[rows].T @ lam[rows]` and compares the 6-DOF
         blocks the two bodies actually receive"
cmd    git diff --stat 6426ca4..a7fefba -- scripts
out    (no output) -- NOT ONE LINE OF `scripts/` CHANGED IN THE WHOLE RANGE
cmd    grep -rn jacobian --include=*.py floatfea
out    io/reader.py:75 and :378 only -- two validator strings. NO MODULE UNDER `floatfea/`
out    FORMS OR READS A CONSTRAINT JACOBIAN.
cmd    `scripts/report_joint_reactions.py:278` as shipped, unchanged in the range
out    `g = setup.constraints.jacobian ...` then `reaction = g.T @ lam`, a PER-BODY
out    6-vector; there is no per-joint duality comparison anywhere in that file
cmd    duality_residual on what the shipped mapper produces
out    a = 1,2,3,0,0,4    b = -1,-2,-3,0,0,-4    duality = 0.0
cmd    the mutation it CAN see -- body B given the same sign as A
out    duality = 2.0
cmd    a lam row of zeros
out    duality = 0.0, by the documented both-zero branch
rule   EK0(e): equal and opposite on the two bodies of each joint, ASSERTED rather than
       assumed, and `joint_reactions.py:10-13` names the state it catches as "a Jacobian
       whose two blocks are not negatives"
judge  **`map_joint_reactions` IMPOSES the opposite sign at `:89`.** So the figure is `0.0`
       by construction, and the Jacobian state the docstring and section 4 both name is
       invisible -- not because the check is weak but because nothing in `floatfea/` ever
       sees a Jacobian. **THIS IS THE VACUITY YOU SAY YOU FIXED, STILL IN THE TREE**: the
       old form was `duality_residual` of a block and its negative; the new form is
       `duality_residual` applied to a mapper that constructs the negative. Same assertion.
judge  And `0.000e+00` on all six cases is also what an absent load prints. A figure that
       cannot distinguish a satisfied law from nothing at all is not evidence of the law.
```

## 7. NOTHING IMPORTS THE 669 LINES, SO NO FIGURE IN THE REPORT IS REGENERABLE

```
cmd    grep -rn for the five module paths and every public symbol they export, over the
         whole tree, excluding the five files themselves
out    (no match outside .git, .mypy_cache, .pytest_cache and .ruff_cache)
cmd    git ls-files tests/verification/rung5 tests/verification/rung6
out    __init__.py only -- both rungs are empty
cmd    the EB6 gate: grep -rn for buoy_centers, platform_common and 0.619657 over tests
         and floatfea
out    (no match) -- and the shipped buoy-node gate,
out    tests/verification/rung3/test_platform_skeleton.py:711, reads
out    `superstructure.deck_joint_points[buoy]` -- THE EXPORT, which is the side DQ9
out    section 2.2 says a permutation corrupts
cmd    grep -n EB6 docs/closure/F3.md
out    :179 -- "F4's load-mapping step adds a gate whose expected side is ... read-only
out    from FloatSim's own platform definition in HSP-stable"
rule   CLAUDE.md section Step gating item 1: every figure is regenerated by running the
       SHIPPED TESTS at the report's own commit
judge  **NOT ONE FIGURE IN SECTIONS 2, 3, 4, 5, 6 OR 7 IS PRODUCED BY ANYTHING IN THE
       REPOSITORY.** Every `cmd` line in those sections is a prose description of a command
       -- "solve_superstructure_static, full scale, load path platform then hubs" -- and
       not a command a reader can run. I reproduced section 3's table to every digit and
       section 5's `2.299219e+06` by writing the driver myself, so THE NUMBERS ARE RIGHT
       FOR THE SHIPPED CODE. The finding is that the four gate rows the locked plan marks
       "to be measured at step 1" -- G4.4, EK0(d) symmetry, EK0(e) duality, EK0(a) -- have
       no assertion anywhere, and EB6's gate does not exist.
judge  **ASKING FOR THESE IS NOT ASKING FOR APPARATUS.** DR1 freezes guards, scanners,
       meta-tests, detectors and report generators. A gate row prescribed by the locked
       plan's own section 5 is the milestone's work, not new apparatus, and I would be
       wrong to let DR1 stand in front of it.
```

## 8. THE TWO `process:` COMMITS, READ LINE BY LINE

Both are standalone, both cite EK2, neither touches `floatfea/` or anything else.

```
cmd    git show e505f28 -- read in full
out    `_ANSWERS_HEADER = re.compile` of a MULTILINE pattern anchored at `^Answers:`,
out    plus `_newest_answers_header`, LAST match, ONE constant, BOTH call sites
cmd    grep -n for rindex and for a bare .index call over tests/test_report_guard_states.py
out    328, 337 -- two COMMENT lines describing the old defect. NO UNANCHORED LOCATOR
out    REMAINS IN EITHER GUARD FILE.
cmd    the two states run individually at 1cfaa66, before the marker moved
out    2 passed
judge  It raises rather than returning a sentinel, which is the right call: a plant that
       silently writes nothing is R657's whole defect. **Anchored, not widened, no name
       added to a list, no state declared green. R657 and R658 CLOSED.**
cmd    git show 9020c6c -- read in full
out    a negative lookbehind, then `R<digits>-` prefixes consumed OUTSIDE the capture,
out    then the original path group unchanged
judge  No real site is lost -- which is the one direction C119's own comments say must
       never be silent -- and the lookbehind stops a mid-token start. The residual case, a
       genuine first path segment of the form `R<digits>-`, is DECLARED rather than hidden.
       **C119 CLOSED.**
```

## 9. THE DISCRIMINATION FIGURES IN SECTION 9 ARE VOID AT THIS COMMIT (CP3)

Verdict 92's item 6 said: before any restored control is believed green, suppress its plant
and paste both directions. You did paste both directions. **The paste cannot have come from
this commit, and I measured that it cannot be re-taken here.**

```
cmd    suppress BOTH plants at `a7fefba` -- each write puts back exactly what it read --
         and compare the red set with the shipped one
out    shipped 13 red ; suppressed 13 red ; THE SETS ARE IDENTICAL
judge  **THE SUPPRESSION CHANGES NOTHING AT `a7fefba`**, because the two states are already
       red for the boundary reason. So no discrimination can be measured at the commit that
       publishes the figure. CP3: generate, edit, re-run, paste -- and if an edit follows
       the paste, the paste is void. The edit that followed was the marker move, in this
       same commit.
cmd    the two states individually at 1cfaa66, where the marker was still on F3
out    2 passed
judge  So your figures were taken before the marker moved and they were true then. **I am
       closing R657 and R658 on my own reading of the regex and on this 1cfaa66 run, NOT on
       section 9's paste**, and the paste itself is a closure item (C141).
```

## The adversarial corpus (BE3)

**Batch 32, committed separately at `80e24df`:**
`tests/corpus/f4_static_case_and_member_force_recovery.txt`, **17 entries, all new**, on
F4's load-mapping surface -- which is one of the two exceptions EG4(e) leaves open to the
corpus pause, and the one where a miss reaches a member force. Every `measured=` field was
taken by me at `a7fefba` against the shipped modules.

**COVERAGE, MEASURED AND NOT CLAIMED: of 17 new entries the step's own four published
quantities CATCH 5, leave 1 UNDECIDABLE for want of a declared threshold, and MISS 11.**

```
cmd    a Counter of the expect field over the committed file
out    17 entries -- MISS 11, catch 5, declare_a_threshold 1
judge  The five catches are: two member-force mutations the section-5 identity does
       discriminate against, the one-arm stiffness asymmetry, the retained-DOF permutation,
       and the mapper's own sign constant. **The eleven misses include half the platform's
       mass and gravity pointing up.** The two worst are both closed by one move: compare
       `StaticCase.weight_N` with `StaticCase.applied_N`, two fields the shipped dataclass
       already carries and never puts on the same line of arithmetic.
judge  Previous batches on other surfaces ran 4 of 11, 8 of 13, 5 of 10. 5 of 17 is the
       weakest round of the milestone, and the reason is not that the entries are exotic:
       it is that a surface with no assertion on it has nothing to catch with.
```

## Findings

**R663. (BLOCKING -- (a), A DEFECT IN `floatfea/`.) `floatfea/post/member_forces.py:78`
RETURNS THE ELEMENT NODAL FORCE AND OMITS THE ELEMENT'S OWN EQUIVALENT LOAD, SO EVERY
PUBLISHED `Vz` AND `My` IS WRONG.** Section 4 above carries the measurement. Tip shear
25.0 percent low on the platform arms and 20.69 percent low on the hub arms; root moment
5.56 and 4.35 percent high; tip moment `-6.386719e+06 N.m` against a true `0`, which is
exactly minus `mu L^2 / 12`. `Vz_A + Vz_B = 0.0` where the member's own weight
`1532812.5 N` must appear. Reach: both tables of
`docs/reports/F4/preview-PRELIMINARY.md`, and report section 5.
**Closed when** `member_forces` forms the element nodal force MINUS the element's
equivalent load, or takes that load as an argument and RAISES when it is not supplied --
it raises, it never defaults; and the gate that reddens on the omission is the tip moment
at a roller, whose true value is `0` and whose defective value is minus `mu L^2 / 12`; and
both preview tables are regenerated or withdrawn IN THE SAME COMMIT (BP0), with report
section 5 regenerated with them.

**R664. (BLOCKING -- (c), A GATE ASSERTION THAT CANNOT FAIL.)
`floatfea/solve/static.py:92`: `StaticCase.sum_error` IS AN IDENTITY THE SOLVE ENFORCES,
AND THE INDEPENDENT SIDE IT COMPUTES IS NEVER USED.** It names DQ8 and forms
`|sum_vertical + applied| / |applied|` with both terms derived from the same `f`.
`weight_N`, which is `deck_mass` times gravity, is reported in the table and compared with
nothing. Counters measured in section 5: half the platform's mass gone reads `3.038e-16`;
gravity reversed reads `0.000e+00`; the handed-down reaction sign-flipped reads
`1.599e-16`. The locked plan's own form is the difference against "the FE mass
distribution's own weight".
**Closed when** the static conservation quantity is normalised against an independently
formed weight -- for a hub that is `deck_mass` times gravity PLUS the handed-down term
NAMED, which is the arithmetic report section 3 writes in prose as
`14715000 + 3065625 = 17780625` and asserts nowhere -- with the counter stated as the
smallest defect in the same quantity the same assertion detects; and the causal sentence at
`:86-91` carries the cell that isolates it or is cut to the bare measurement.

**R665. (BLOCKING -- (c).) THE EK0(d) SUPPORT-SCHEME CHECK CANNOT FAIL, AND NO THRESHOLD IS
DECLARED FOR IT.** `floatfea/loads/selfweight.py:86`, `floatfea/solve/static.py:21-23`,
report section 3's CHECK 2. Measured both directions in section 5: an eight-DOF redundant
restraint and a restraint that clamps yaw both give `0.000e+00`; a `1e-16` tilt of gravity
gives `1.226e-09 N` and a `1e-3` tilt gives `1.226e+04 N`. The quantity is a statement
about the load's verticality, not about the restraint's determinacy, and
`worst_horizontal_N` is an absolute dimensional figure with no stated scale.
**Closed when** EITHER the plan's EK0(d)-supports row and the module docstring say what the
quantity measures -- that the applied load is purely vertical -- with a relative threshold
against a stated response scale and a counter; OR the determinacy claim is carried by a
check that can fail, for which the discriminator is already measured: a restraint with a
redundant in-plane DOF must redden it, and today it does not.

**R666. (BLOCKING -- (d), THREE RED TESTS THAT ARE NOT THE MILESTONE BOUNDARY, AND CI IS
RED AT THE REVIEWED COMMIT.)** Section 3 carries the four cells. `**CLOSED**` in report
section 9's Carried table reddens `test_a_report_does_not_say_CLOSED` -- CC1, only a
verdict closes an item -- and `**ledgered**` for R656 reddens
`test_every_carried_item_carries_one_of_the_report_words`, which in turn is the reporter
for both `test_report_vocabulary_corpus` rows. Each is cleared by changing ONE WORD and
nothing else. They are red at any commit carrying this table. CZ1 (iv) unchanged.
**Closed when** section 9's status cells use the report's own vocabulary -- `answered`,
`open`, `withdrawn`, `4a`, `later`, `carried` -- and the three ids are green at the
answering commit with the `FAILED` list pasted; and section 1b's "ONE CAUSE" is corrected
to name the two causes it actually has.

**R667. (BLOCKING -- (c).) EB6's GATE DOES NOT EXIST, AND REPORT SECTION 7 REPORTS A SECOND
SIDE TO A FIRST SIDE THAT IS NOT IN THE TREE.** Section 7 above carries the greps.
`docs/closure/F3.md:179` assigns the gate to "F4's load-mapping step"; the locked plan's
section 2.2 and its section 5 row specify the expected source, the `1e3x` band and the
permuted export as counter-case; the only shipped buoy-node gate,
`tests/verification/rung3/test_platform_skeleton.py:711`, reads the export on BOTH sides.
The plan's DQ9 sentence "EB6 ships on the first side" is false.
**Closed when** EITHER the first side ships reading `platform_common.py:51-58` with the
permuted export CONSTRUCTED as its counter-case and the hub extension at `:157`, OR the
plan row and report section 7 state that the gate does not exist yet and name the step that
builds it. **I will not take the second option as free**: the second-side measurement in
section 7 is good work and it is currently a measurement about nothing.

**R668. (BLOCKING -- (c).) THE EK0(e) DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE STATE
THE DOCSTRING NAMES IS INVISIBLE.** Section 6 above. `map_joint_reactions` imposes body
B's share as the negative at `joint_reactions.py:89`, so `duality_residual` on its output
is `0.0` whatever any Jacobian does, and no module under `floatfea/` reads a Jacobian. The
both-zero branch returns `0.0` as well, so the published `0.000e+00` cannot distinguish a
satisfied law from an absent load.
**Closed when** the duality assertion reads the two bodies' shares from the Jacobian rather
than from a mapper that imposes the sign, with a Jacobian whose two blocks are not mutual
negatives CONSTRUCTED as the counter-case; and the both-zero case is excluded from the
window or raises, rather than returning a value indistinguishable from a pass.

**R669. (BLOCKING -- (c).) FOUR GATE ROWS THE LOCKED PLAN MARKS "TO BE MEASURED AT STEP 1"
HAVE NO ASSERTION ANYWHERE, AND NOTHING IN THE TREE IMPORTS THE 669 LINES.** Section 7
above. G4.4, EK0(d) symmetry, EK0(e) duality and EK0(a) exist as prose figures only; the
`cmd` lines that carry them are descriptions rather than commands;
`tests/verification/rung5` and `rung6` are empty. This is not a prose finding and it is not
apparatus: it is the gate assertions the plan's section 5 prescribes for this step.
**Closed when** each of those four rows is an assertion under `tests/`, each with the
counter that reddens it, each reading its expected value from a source that is not the
object under test (EA4); and each `cmd` line in the report is the command that runs it.

## Closure items

Not re-reviewed item by item. Fixed once, in the step's closure commit (CZ0).

* **C135.** `docs/milestones/F4.md:8-13` says "NO `step-under-execution` MARKER IN THIS FILE
  YET, DELIBERATELY" while `:3` carries it. I checked the mechanism rather than assuming:
  `_STEP_LINE` resolves to F4 step 1 correctly and the stale comment does not match it, so
  there is no second marker and no blinding. False prose in a locked plan (CW0). What closes
  it: delete or rewrite the comment.
* **C136.** The marker move landed in `a7fefba`, the REPORT commit. Plan section 2.4 says
  "in the FIRST commit", together with C119 and R661. Closes when the plan row or the
  practice agrees with the other.
* **C137.** Report section 5's hand arithmetic: `156250 x 9.81` is `1532812.5`, not the
  `1533000` published, and the hand value is `2299218.75` -- IDENTICAL to the computed
  `2.299219e+06`. The `2.2996e+06` and the implied agreement "to within 4e+02" do not exist;
  they are an artifact of the report's own rounding. Closes with R663's regeneration.
* **C138.** `floatfea/solve/static.py:12`: "On the platform the link is `20.66 m` long, so
  the remainder's moment arm is load-bearing rather than incidental." Measured: the offset is
  `[4.0e-16, -7.5e-16, 20.663]`, PURELY VERTICAL, so `r x F` is zero under vertical gravity;
  ablating the offset to zero leaves the reactions bit-identical and `u_full` different by
  `4.542e-17`. BG0 -- the causal sentence has no cell. **The other half of that paragraph is
  correct and important**: the slave node's six DOF really are unconnected and the
  factorisation really is exactly singular without the reduction. Closes when the sentence
  says the reduction is needed because the node is unconnected, full stop.
* **C139.** `floatfea/solve/static.py:111-113`: "an assert on the width is what makes a drift
  loud instead of a silently permuted reaction vector." A permutation preserves width.
  Measured: reversing `_retained` IS caught, but by `sum_err 4.959` and
  `worst_horizontal 2.077e+08`. Closes when the comment names the mechanism that actually
  catches it.
* **C140.** `floatfea/loads/selfweight.py:92-93`: "Picking the furthest ... is the only
  choice that cannot accidentally be degenerate on a frame whose joints are nearly aligned."
  The degeneracy test at `:102` is `max(separations) == 0.0`, an exact float comparison, so a
  nearly-aligned frame passes it and the solve is near-singular rather than refused. Closes
  when the sentence matches the test, or the test matches the sentence.
* **C141.** Report section 9's three `cmd` lines are prose, and its `3 passed / 3 passed /
  3 failed` cannot be re-taken at `a7fefba` -- section 9 of this verdict measures that
  suppressing both plants there changes nothing, 13 red either way, identical sets. CP3.
  Closes when the figure is re-taken at a commit where the two states are otherwise green,
  with the commit named.
* **C142.** `_links` is the same eight lines in `floatfea/solve/static.py:95-105` and
  `floatfea/solve/inertia_relief.py:68-74`. C131's shape: a rule written twice drifts.
* **C143.** `floatfea/loads/joint_reactions.py:50-56`: the both-zero branch returning `0.0`
  is correctly declared as "a real state at the start of a ramped run". What the docstring
  does not say is that it is also indistinguishable from a satisfied law, which is R668.

## On the criterion, once, and it leaves the loop

**EG3's two lists do not reach a MILESTONE boundary, and nothing in the repository says what
happens there.** Your section 1b is right that state (1) presumes a verdict in the same
review directory, and right to decline a carve-out you do not have. I measured the state and
it behaves exactly like EG3 describes -- a verdict clears 10 of the 43 and introduces nothing
-- but the list is 43 and EG3 names one. **Two consequences I cannot resolve from inside the
loop:**

1. **Verdict 92's item 5 is withdrawn and I was wrong to write it.** I asked F4 step 1's
   first report to carry `Answers: verdict 92 @ 5049151`. Verdict 92 is F3 step 3's. My own
   instruction 1b exists so that one unverifiable-by-machine comparison -- does the header
   name the LATEST verdict -- is made by a reader; a header pointing into another milestone
   would make that comparison false while reading true. **Your refusal is the correct call
   and the reasoning in your section 1a is the reasoning I should have used.**
2. **Which leaves a boundary with no clean state.** Either EG3's state (1) list is extended
   to cover "the newest report is the first in its milestone and no verdict exists under
   `docs/reviews/F<n>`", or something must make the section generable without a false
   header. `scripts/ci_section.py` already declines in words, correctly, which is why I am
   not treating its absence as a finding. **This is a criterion question, it goes to Xabier
   through you, and it does not become another round.**

**And one planted state is this condition's own control.** You named it and I confirm it:
`newest_report_has_no_verdict_yet` plants the situation the tree is actually in, so the plant
changes nothing and the state cannot discriminate. That is R657's vacuous-control shape from
the other side -- not a locator that misses its target but a target the tree already occupies
-- and you were right that EK2 does not cover it, because it is not a locator. **It is the
clearest thing in your report and it is the kind of finding only the person who built the
state can make.** To Xabier with the above.

## Carried

Verdict 92 named **two blocking items**, three closure items, a ledger, two hand-overs, and
a seven-item `Next step opens when`. Every one, with its status.

* **R657 -- ANSWERED AND CLOSED at `e505f28`. The word is mine.** Section 8 carries the
  reading: anchored at line start, MULTILINE, last match, one constant serving both call
  sites, and `_newest_answers_header` RAISES rather than returning a sentinel. No unanchored
  locator remains in either guard file. Not answered by widening, not by declaring a state
  green, not by adding a name to a list -- verdict 92's three prohibitions, all respected.
  Closed on my reading plus the `1cfaa66` run, NOT on section 9's paste (C141).
* **R658 -- ANSWERED AND CLOSED at `e505f28`**, same constant, same commit, same reading.
  Verdict 92's "same unanchored locator, two sites" is now zero sites.
* **C119 -- ANSWERED AND CLOSED at `9020c6c`.** Section 8. The id prefix is consumed outside
  the capture so no real site is lost, the lookbehind stops a mid-token start, and the
  residual case is declared rather than hidden. Landed AFTER the lock, as verdict 92 item 1
  required.
* **The DR1 / CZ0 wording conflict -- RESOLVED by EK2 and applied twice, correctly.** Both
  repairs are locator or parser repairs in standalone `process:` commits citing the clause;
  neither touches an assertion. This had been open with Xabier for three rounds and it is
  now shut.
* **R656 -- OPEN WITH XABIER, unchanged, correctly not repaired.** `scripts/ci_section.py` is
  untouched in the range. **It now has a second instance:** the criterion section above is
  the same class of problem -- CA2's and EG3's declared states not covering a real tree
  state. Ledgered after 28 Oct per EK2.
* **R653 -- OPEN, carried, and about to become (c).** A grep for RHO_INF over tests and
  floatfea gives no output; the constant still reaches no assertion. **F4 step 2 is where a
  G4.x gate cites this residual, which is the condition verdict 92 set for it to become
  blocking.** Carries by name into step 2.
* **R638 -- OPEN, unchanged, EJ1 governs, closed before F4 closes.** `floatfea/tolerances.py`
  is not in this range's diff at all.
* **R637 clause (iii) -- ANSWERED FOR THIS ROUND.** The whole-suite line IS pasted at the
  committed sha and it reproduces on my instrument exactly -- `43 failed, 2793 passed,
  1 skipped` -- and the 43 ids are set-identical. Its standing object was R662, now closed;
  it has no new object.
* **R659, R654, R655 -- CLOSED, not reopened, nothing in this range touches their sites.**
* **R660 -- ANSWERED at `0c490bf`**, the standalone closure commit verdict 92 said was worth
  making. It is the only commit in the range touching `docs/closure/F3.md`.
* **R661 -- ANSWERED in report section 8**, where EK3 puts it, and the cause is correctly
  identified as the fill-in default rather than the generator.
* **R662 -- ANSWERED in F3's closure artifact, not reopened.**
* **The EJ4 residual-location hand-over -- unchanged, carried into F4's gate.** It becomes
  live at step 2, where `3.96e-06` is the reference.
* **Verdict 92's `Next step opens when`, item by item.** (1) the plan locked before
  implementation -- **RESPECTED**, `2e32b41` precedes `1cfaa66`. (2) R657 and R658 not
  answered by widening, declaration or a list entry -- **RESPECTED**, verified line by line.
  (3) push ordering -- **RESPECTED**, `a7fefba` reached CI at run `37337908921`.
  (4) section 0 producible -- **WITHDRAWN WITH ITEM 5.** (5) name verdict 92 at my verdict
  commit -- **WITHDRAWN BY ME, and the refusal in your section 1a was right.** (6) a red
  traced by name, and a state that passes is not a state that discriminates -- **ANSWERED IN
  FORM AND REFUTED IN SUBSTANCE**: the trace is complete and the cause is wrong for three
  entries (R666), and the discrimination paste cannot be re-taken at this commit (C141).
  (7) the `Carried` list -- answered; `check_carried` is still run by nothing, which verdict
  92 recorded as the reason the list has to be exact, and it was.
* **The EJ3 ledger at `docs/closure/F3.md` section 8 -- unchanged and not re-reviewed**, per
  CZ0. C113, C115 to C117, C120, C122, C123, R631, R626's residue, R635 and the long closed
  list stay as they are. **C119 moves off it, closed.**
* **R622 -- F4's own, not yet reached.**

## Tolerances touched

**NONE.**

```
cmd    git diff 6426ca4..a7fefba -- floatfea/tolerances.py
out    (no output) -- diffed SEPARATELY, per my instruction 4, because that file is where
out    the cheapest wrong fix lands
judge  No value, no form, no counter and no injection changed. Your section 10 is correct,
       and the locked plan's gate table is correct that F4 declares none until step 2
       measures one. **But note what that means for R664 and R665**: a quantity reported
       with no threshold is not a tolerance-free gate, it is a gate with an UNDECLARED
       threshold, and `worst_horizontal_N` is published today as an absolute dimensional
       number. When step 2 declares it, it is relative to a stated response scale and it
       arrives with a counter.
```

## Next step opens when

Step 2 does not open. These are answered first and the step is re-invoked. **Round 1 of 3 on
F4 step 1.**

1. **R663 -- the member-force recovery.** The element's equivalent load is subtracted, or
   demanded and refused when absent. The tip moment at a roller is the assertion: true value
   `0`, defective value minus `mu L^2 / 12`. Both preview tables and report section 5 are
   regenerated or withdrawn in the SAME commit as the fix, not the next one (BP0).
2. **R664 -- the static conservation quantity is normalised against an independent weight**,
   with the handed-down term named, and the counter is the measured defect size at which it
   trips. `3.038e-16` on half the platform's mass is the number it has to stop printing.
3. **R665 -- the support-scheme check either states what it measures, with a threshold and a
   counter, or is replaced by one a redundant restraint reddens.** Either way the claim that
   the zero proves the scheme right is withdrawn from `static.py:21-23` and from the report.
4. **R666 -- section 9's status cells use the report's own vocabulary, and the three ids are
   green at the answering commit with the `FAILED` list pasted.** Section 1b says two causes.
5. **R667 -- EB6's first side ships against `platform_common.py`, or the plan row and
   section 7 say it does not exist and name the step that builds it.**
6. **R668 -- the duality assertion reads the Jacobian, with non-mutual-negative blocks
   constructed as its counter-case.**
7. **R669 -- the four step-1 gate rows are assertions under `tests/`**, each with its
   counter, each reading its expected value from something other than the object under test.
   Every `cmd` line in the revised report is a command. **I will run them.**
8. **The schedule paragraph is kept and updated.** EK4's preview is delivered three days
   early and I credit that; R663 means its figures are wrong, so it is reissued with the fix
   and the 8 Oct delivery stands as the delivery of a corrected table. **F4 is committed for
   19 Oct. If answering items 1 to 7 puts that at risk, CZ0 says the slippage is reported
   THE DAY IT IS KNOWN, with the choice stated -- slip the date or reduce scope -- and not
   when the step closes.**
9. **Nothing in items 1 to 7 is new apparatus, and I say so explicitly** so that DR1 is not
   an answer to any of them. Each is either a defect in `floatfea/` or a gate row the locked
   plan already prescribes for step 1.

**What I will not accept as an answer:** a tolerance that makes R663's regenerated figures
agree with the old ones; "zero by construction" offered as a reason a check needs no
counter; or a `cmd` line that describes a command instead of being one.

**And what I want on the record for you rather than against you.** The three best things in
this round are yours: the premise check argued on its mechanism instead of its figure, the
vacuous-control finding on `newest_report_has_no_verdict_yet`, and the refusal to write a
header that would read true and be false. The 43 reds are listed completely and honestly and
you declined a carve-out you could have claimed. **What the round shows is that a step whose
only instruments are its own published numbers cannot be audited by reading them, and six of
my seven findings came from running the code rather than from reading the report.**
