# Review — F6 step 1
Reviewed commit: 24fad0492733f50ad2921041ca53145387ead6e0
Verdict: PASS
**Reviewed commit: `54ff15c`** (`54ff15ccc899ffd1f9f8c996d048c816a7e652c0`, tree clean when I
judged it; my corpus batch 44 is committed on top at `24fad04`, which is why the plain
`Reviewed commit:` stamp below is not the commit I judged -- R718's subject, and this bold
line is the mechanism.)
Tests: 3433 passed, 0 failed, 0 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `54ff15c`, `648.19s`.)

## Round of 2026-10-09 -- ROUND 3 OF THREE, F6 step 1. **PASS, AND THE STEP CLOSES CARRYING ONE.** Four of the five are closed and I ran each. The fifth is closed in form and its repair published an inverted count.

**WHY PASS.** This is the third reviewed revision, so under CZ0 as amended by ES0 the step
closes whatever its state. It closes in good order: **R748, R749, R750 and R751 are CLOSED**,
each measured rather than read, and R747's four sentences are now generated from their sets --
three of them correctly. **One blocking item is open and carries by name into step 2: R752**,
the fourth generated sentence, which publishes "the AMPLIFIED form governs on 10 of 17
compression rows" where the amplified form governs on **7 of 17** and the ten rows it counts
are **exactly the ten where the SIMPLE form governs**. The predicate is right about a
different question. **My own verdict-111 inference is the proximate cause and I withdraw it.**

**WHAT I RAN RATHER THAN READ.** Twenty-six one-at-a-time mutations of
`floatfea/checks/api_wsd.py`, source restored byte-identical after each: **26 of 26 killed**,
including all three R749 survivors, the `>=`/`>` switch and the nine coefficients the report
asked me to try. Thirteen mutations of the gate's own aggregation, point set and three
constants. The clause module at 1792 `(KL/r, f_a/F_e, My)` configurations the diff did not
choose. An independent hand side for section 3.2.2 over six grades and `D/t` from 5 to 300,
in two spellings. A consistent change of unit system. A 1 mm prescribed stretch. The
deliverable regenerated and diffed byte for byte.

**No STOP.** No low rung is red: `the verification ladder` is SUCCESS at `a041574` with
`ladder 5 -- independent confirmation` success and `run_rung: 68 collected, 0 failed`. The
locked plan is not wrong.

## 0. CI -- UNAVAILABLE AT THE REVIEWED COMMIT BY DESIGN, RED AT THE ROUND'S CODE COMMIT, AND I TRACED ALL NINE BY NAME

```
cmd    gh run list --commit 54ff15ccc899ffd1f9f8c996d048c816a7e652c0 --json ...
out    []
cmd    git show --stat 54ff15c
out    docs/reports/F6/step-1.md   one file, and it is under the workflow's paths-ignore
judge  **UNAVAILABLE BY DESIGN. NOT CK2 AND NOT CA2's RED.** No run exists at the reviewed
       commit because that commit touches only `docs/reports/**`.
cmd    gh run list --commit a041574e59f9cb61b6ab58e1bce7706e2bf76d32 --json ...
out    [{"conclusion":"failure","databaseId":37951958409,"event":"push","name":"CI"}]
cmd    gh run view 37951958409 --json jobs -q '.jobs[] | .name + " :: " + .conclusion'
out    lint, unit and guards             failure     (step 10, guards and meta-tests)
out    the verification ladder           success
out    CI determinism -- leg             skipped
out    CI determinism -- ten legs agree  skipped
cmd    gh run view 37951958409   (the ladder job, step level)
out    ladder 1 / 2 / 3 / 6 / 4 / 5     all success
cmd    gh run view 37951958409 --log | grep "run_rung:"
out    1276 / 66 / 297 / 134 / 343 / 68 collected, 0 failed, 0 errored, 0 skipped
judge  **THE 68 RUNG-5 TESTS RAN ON UBUNTU AND ARE GREEN THERE**, which is the one
       measurement an exactness ceiling's own justification cannot take on one machine. The
       three new assertions and the new weak-end point are inside that 68.
cmd    gh run view 37951958409 --log | grep -oE "FAILED tests/[^ ]*" | sort -u
out    FAILED tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
out    FAILED tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count
out    FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
out      + [non_numeric_step_suffix] [superscript_digit_step_number]
out        [draft_suffix_beside_a_step_report] [step_number_is_the_empty_string]
out        [verdict_amended_after_the_commit_the_report_answers] [zero_padded_step_number]
out    9 failed, 1149 passed, 1 skipped, 1 warning in 660.77s
cmd    python -m pytest -q -p no:randomly tests/test_report_carried.py
       tests/test_report_guard_states.py tests/test_report_numbers_are_sourced.py
       -- AT THE REVIEWED COMMIT
out    327 passed in 139.56s
judge  **NINE REDS, TWO CAUSES, EVERY ONE MATCHED BY NAME, AND NOTHING OUTSIDE THOSE TWO
       FILES.** I checked the claim rather than took it: each of the seven planted states
       pastes the SAME two reds in its own failure line, which is how EH1 says a cascade is
       identified. Both causes are CZ1's class -- a check whose input is the commit itself:
       `scripts/suite_count.py` measures a clean worktree AT a commit, and the `0a` table
       needs a RUN, which cannot exist before a push. **Both clear at the reviewed commit
       and I measured the clearing**; my own whole-suite run at `54ff15c` is `3433 passed,
       0 failed, 0 skipped`. CZ0 (d) asks about a red test at the reviewed commit and there
       is none.
```

**AND THE STRUCTURAL PROBLEM UNDER IT IS NOW TWO ROUNDS OLD -- see the criterion section.**
Neither of those two guards is on either of EG3/EH1's lists, so on a literal reading of "any
red not on the list still blocks" both would block, and for the second consecutive round a
reviewer has admitted them by hand. That is a criterion question and it goes to Xabier.

## 1. MY OWN INSTRUCTIONS, THE CONFTEST AND THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
cmd    git diff fdb4ecd..54ff15c -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git diff --name-status fdb4ecd..54ff15c -- '*conftest*' '*plugin*'
out    (empty)
judge  CH2/CI0: no conftest and no plugin anywhere in the range, so no rung's green is
       written from its own directory and I did not have to read a hookwrapper. Rung 5's
       green is a pytest result and not a rewritten record.
cmd    git diff --stat fdb4ecd..54ff15c -- .claude docs/SUPERVISOR.md
out    (empty)
judge  **CLEAN.** My own instructions are untouched in this range. C45 is still open and is
       still process class rather than step work.
cmd    git diff fdb4ecd..54ff15c -- floatfea/tolerances.py | grep -E "^[-+][A-Z0-9_]+: Final"
out    -F6_API_CLAUSE_AGREEMENT_COUNTER: Final[float] = 8.0e-13
out    +F6_API_CLAUSE_AGREEMENT_COUNTER: Final[float] = 3.0e-13
out    -F6_API_CLAUSE_INJECTION_EPS: Final[float] = 1.0e-12
out    +F6_API_CLAUSE_INJECTION_EPS: Final[float] = 1.0e-10
judge  **TWO VALUES MOVED AND `F6_API_CLAUSE_AGREEMENT` DID NOT.** The counter FELL by
       `2.67x` and the injection ROSE by `100x`; nothing else in the file moved. EU1 fires
       and section 5 is the adversarial case.
```

## 2. THE ORDER THE VALUES MOVED IN -- THE THING THE REPORT ASKED ME TO BE MOST SUSPICIOUS OF

```
claim  the assertion moved first and went red on the shipped values, so the values were
       re-derived rather than fitted
cmd    in a clean `git archive HEAD` copy: COUNTER 3.0e-13 -> 8.0e-13 and EPS 1.0e-10 ->
       6.5e-12 and -> 5.0e-11, one at a time, whole of rung 5 re-run, both files restored
       byte-identical and asserted
rule   the gate's own two assertions: weakest live > COUNTER, and weakest/CEILING > 2.0
out    EPS -> 6.5e-12  (the entry's own boundary)     3 failed, 65 passed
out    EPS -> 5.0e-11                                 2 failed, 66 passed
out    COUNTER -> 3.1e-13                             2 failed, 66 passed
cmd    git diff --stat fdb4ecd..54ff15c -- floatfea/checks/api_wsd.py
out    (empty)
judge  **THE ORDER IS AS CLAIMED AND THE MODULE THE TOLERANCES MEASURE IS BYTE-IDENTICAL
       ACROSS THE RANGE.** There is no code change in this commit for either value to
       rescue, which is the strongest available form of "the tolerance was not moved to make
       a failure pass". The aggregation is what makes the old values red; the values follow.
```

**And the question behind it -- is `1.0e-10` simply large enough to make a weak gate look
adequate.** Solved in both directions.

```
rule   the response is linear in the injection and the minimum resolution is 3.074923e-03
out    the gate reddens below eps = 9.757e-11 -- the counter is a function of eps, so at the
out      SHIPPED counter there is 2.5% of headroom beneath the injection, not two decades
out    eps may rise to 1.0e-8 with 68 passed -- unbounded and unasserted
out    the entry's 6.504229e-12 is the CEILING-based boundary and is correct as stated
judge  **NOT A FINDING, AND THE READING MATTERS.** `1.0e-10` is eight decades below a real
       transcription error (the coefficients are exact decimals) and three decades above the
       point where the comparison goes vacuous. What the entry does not say is that the two
       constants are locked together: lowering `eps` without lowering the counter reddens
       the gate, so "two decades above the boundary" is a statement about what `eps` COULD
       be if the counter were re-derived, not about headroom in the shipped gate. C62.
```

## Findings

**R752. (BLOCKING. (a) AS AMENDED BY EZ0 -- A DEFECT IN A PUBLISHED DELIVERABLE AND IN THE
`scripts/measure/` GENERATOR THAT PRODUCES IT.) THE REPAIR OF R747's FOURTH SENTENCE
PUBLISHES AN INVERTED COUNT: SECTION 3.3.2's AMPLIFIED FORM GOVERNS ON 7 OF 17 COMPRESSION
ROWS, NOT 10, AND THE TEN ROWS THE SENTENCE COUNTS ARE EXACTLY THE TEN WHERE THE SIMPLE FORM
GOVERNS. MY OWN `10 of 17` IS WITHDRAWN -- THE COUNT WAS RIGHT AND THE INFERENCE I ATTACHED
TO IT WAS NOT.**
`scripts/measure/api_wsd_utilisation.py:374-386` (the `amplified_rows` predicate and the
comment above it), published at `docs/F6_utilisation.md:69`.

```
claim  "section 3.3.2's AMPLIFIED form governs on 10 of 17 compression rows", generated
cmd    per published compression row, recompute the two forms section 3.3.2 takes the larger
       of, from the deliverable's own columns:
         amplified = f_a/F_a + cm*u_bending/(1 - f_a/F_e)
         simple    = f_a/(0.6 F_y) + u_bending
       with F_e at the body's own KL/r -- 121.5 platform, 60.8 hubs
rule   floatfea/checks/api_wsd.py:401-403, `u_combined = max(amplified, simple)`
out    AMPLIFIED governs on  7 of 17
out    SIMPLE    governs on 10 of 17
out    and the 10 rows the published sentence counts are the 10 SIMPLE-governing rows,
out      one for one
out    platform:hub2_arm ROOT  u_bending 1.71138  amplified 1.456719  simple 1.711666
out    platform:hub4_arm ROOT  u_bending 1.71138  amplified 1.456719  simple 1.711666
out    hub1:buoy2_arm   ROOT   u_bending 0.78429  amplified 0.677880  simple 0.790490
out    ... seven more, all SIMPLE, every one bending-dominated at a share above 98.4%
out    hub3:buoy8_arm   TIP    u_bending 0.00384  amplified 0.008400  simple 0.007720
out    ... six more, all AMPLIFIED, every one with a bending share under 46%
judge  **THE PREDICATE IS RIGHT ABOUT A DIFFERENT QUESTION.** `amplified_rows` is the rows
       where `utilisation_Cm1 != utilisation_K2` at the CSV's `{:.6g}`. That detects `C_m`
       changing the GOVERNING utilisation, which happens where the amplified form governs AT
       THE PERTURBED `C_m = 1.0` -- not at the shipped `0.85`. Measured at
       platform:hub2_arm ROOT: at `C_m = 0.85` amplified is `1.456719` against simple
       `1.711666`, so SIMPLE governs by `17.5%`; at `C_m = 1.0` amplified rises to
       `1.713640` and TAKES OVER, which is the published `utilisation_Cm1 = 1.71365`. The
       column differs precisely BECAUSE the simple form was governing and stopped.
```
```
cmd    the comment the predicate is derived from, api_wsd_utilisation.py:374
out    "The amplified form of 3.3.2 governs exactly where `C_m` reaches `U`, because `C_m`
out     appears nowhere else in the calculation."
judge  **A CAUSAL CLAIM (BG0) WITH NO CELL, AND ONE ROW REFUTES IT.** `C_m` appearing
       nowhere else is true and does not license the inference, because `C_m` can flip which
       half of the `max` is taken.
cmd    sed -n '69,72p' docs/F6_utilisation.md
out    :69  section 3.3.2's AMPLIFIED form governs on 10 of 17 compression rows
out    :72  ... the simple form carries no `F_a` and no `C_m`, and it is the one that
out         governs wherever bending dominates
judge  **THE DELIVERABLE NOW SAYS BOTH, AND THE HAND-WRITTEN HALF IS THE TRUE ONE.** `:72`
       is correct -- the simple form governs on exactly the ten bending-dominated rows,
       including both over-unity platform ROOTs at a 99.98% bending share. This is R747's
       class for the third round running, a summary line contradicting the table it sits
       beside, inverted, with the generated half now the wrong one. Verdict 109's single
       blocking finding was a defect in the repair of the previous finding in this class.
cmd    the fields of MemberCheck
out    no field records which half of `max(amplified, simple)` was taken, so any caller
out    that wants it must re-derive it -- which is what the proxy was
```

**Closed when** the count is computed from the two forms themselves -- either `check_member`
returns which half of `max(amplified, simple)` governed, or the generator forms both from the
row it already has -- the sentence is regenerated, and `docs/F6_utilisation.csv` and
`docs/F6_utilisation.md` are regenerated in the same commit (BP0). **My figures to beat:
AMPLIFIED on 7 of 17, SIMPLE on 10 of 17; at `platform:hub2_arm` ROOT amplified `1.456719`
against simple `1.711666` at `C_m = 0.85`, and `1.713640` at `C_m = 1.0`, which is the
published `utilisation_Cm1`.** If a regeneration disagrees I want the disagreement, not a
reconciliation. **And the comment at `:374` is deleted or given its cell**, because it is the
sentence that produced the predicate.

**I AM WITHDRAWING MY OWN FIGURE AND SAYING WHY, BECAUSE IT IS THE CAUSE.** Verdict 111
wrote: "10 of 17 compression rows have `utilisation_Cm1 != utilisation_K2`, **which can only
happen where the amplified form governs, because `C_m` appears nowhere else in the
calculation**". The count is correct; the clause after the comma is wrong, for the reason
above. The implementer generated the sentence from the set *my verdict named* instead of from
the set the sentence describes, and that is the right instinct applied to a defective input.
**A figure I hand over as "mine to beat" is an input to a generator, and this is the second
consecutive round in which one of my inferences rather than my arithmetic was the defect** --
the first was the `5.3x` ranking I withdrew in verdict 111.

## 3. WHAT I CLOSED, EACH MEASURED RATHER THAN READ

```
R749 -- THE THREE SURVIVORS, RE-RUN BY ME, PLUS TWENTY-THREE MORE
cmd    26 one-at-a-time edits of floatfea/checks/api_wsd.py in a clean `git archive HEAD`
       copy, whole of rung 5 re-run after each, source restored byte-identical and asserted
out    limit_1 10340 -> 10430 (digit swap)   2 failed, 66 passed   KILLED
out    limit_1 -> 10443.4 (+1%)              2 failed, 66 passed   KILLED
out    limit_1 -> 10236.6 (-1%)              2 failed, 66 passed   KILLED
out    limit_2 20680 -> 20860 (digit swap)   3 failed, 65 passed   KILLED
out    limit_2 -> 20886.8 (+1%)              3 failed, 65 passed   KILLED
out    limit_2 -> 20473.2 (-1%)              4 failed, 64 passed   KILLED
out    d_t > 300.0 -> 303.0                  1 failed, 67 passed   KILLED
out    d_t > 300.0 -> 299.0                  1 failed, 67 passed   KILLED
out    in_tension >= 0.0 -> > 0.0            1 failed, 67 passed   KILLED
out    CONTROL PASCAL_PER_MPA 1.0e6 -> 1.1e6 6 failed, 62 passed   KILLED
out    the nine the report asked me to try: 0.84 -> 0.48 (5 failed); 1.74 -> 1.47 (4);
out      0.72 -> 0.27 (15); 0.58 -> 0.85 (15); 1.64 -> 1.46 (8); 0.23 -> 0.32 (8);
out      F_e 12.0 -> 21.0 (12); 23.0 -> 32.0 (11); (1 - 0.5 r^2) 0.5 -> 0.05 (8)
out    and seven more I chose: 5/3 -> 5/3.1 (8); 3/8 -> 3/8.8 (8); r^3/8 -> /8.8 (8);
out      CM_JOINT_TRANSLATION 0.85 -> 0.58 (4); LOCAL_BUCKLING_DT 60 -> 90 (4);
out      BEAM_SHEAR_AREA_FACTOR 0.5 -> 0.6 (4); third numerator 300000 -> 30000 (14)
out    **26 of 26 KILLED. Nothing survives.**
judge  **R749 IS CLOSED AND THE CONDITION WAS MET BOTH WAYS INSTEAD OF ONE.** `limit_1` and
       `limit_2` are exact equalities against `section_class(D_OUTER, WALL, FY)` -- which is
       the one function `allowable_bending` itself calls, so one literal serves both and
       pinning it pins the branch -- AND `29.2`/`58.3` sit inside each limit's own
       neighbourhood AND in `_FB_POINTS`. The `300` refusal is bracketed at `300`/`300.1`
       and I confirmed it reddens on `299` too, which is the direction nobody asked for.
       The tension switch is bracketed at `0.0` and `-5e-324`.

R748 -- THE FOUR CITATIONS
cmd    grep -rn "rung6" docs/F6_utilisation.md docs/F6_utilisation.csv
       scripts/measure/api_wsd_utilisation.py ; ls tests/verification/rung5/
out    (no match in any of the three files)
out    rung5:  __init__.py  test_g61_api_wsd_hand_calculations.py
cmd    python scripts/measure/api_wsd_utilisation.py --out <tmp> --summary <tmp> ; diff
out    CSV identical; MD identical
judge  **CLOSED, AND THE REGENERATION IS BYTE-IDENTICAL**, which is more than the condition
       asked and is the shape step 2's own gate will need.

R751 -- THE ATTRIBUTION, AND THE HONEST STATEMENT OF ITS TEST's REACH
cmd    in a clean copy: invert `member_forces`' returned vector; then separately delete
       `root[0] = -root[0]`, then `tip_internal[0] = -tip_internal[0]`, from
       scripts/measure/member_forces_table.py. Whole of rung 4 each time.
out    baseline                                 343 passed in 3.17s
out    the attribution INVERTED                 4 failed, 339 passed   REDDENS
out      -- test_a_member_in_pure_TENSION_returns_a_NEGATIVE_end_a_axial plus the two
out         conservation tests and the defective-formula control
out    `root[0] = -root[0]` reverted            343 passed             still green
out    `tip_internal[0]` reverted               343 passed             still green
cmd    grep -rl member_forces_table tests/
out    tests/verification/rung4/test_f4_static_and_mapping.py + three corpus DATA files
judge  **CLOSED FOR THE `floatfea/` HALF, AND THE REPORT STATES THE OTHER HALF's ABSENCE
       RATHER THAN CLAIMING IT.** The paragraph is now the measured attribution with a
       triple `tests/test_tree_prose_consistent.py` runs, and the measurement is a rung-4
       test on a prescribed sense -- `end_a[0] = -5.51010219e+06` where Hooke gives
       `+5.51010219e+06`, verdict 110's and verdict 111's figure to every digit.
       **Self-reporting that the test does not reach the publishing boundary is worth more
       than the test**: it is C52's other half, it is named as open, and nothing in the
       report pretends otherwise. I found the second negation unguarded too.
```

## 4. R750 -- I ACCEPT THE READING, I WITHDRAW MY OWN WORDING, AND HERE IS WHY

The implementer asked me to attack this hardest. I will do the opposite, because the
measurement supports it, and I will say exactly which of my sentences was wrong.

```
claim  (mine, verdict 111) "the counter is a floor beneath every admissible configuration
       rather than a constant at one"
cmd    the resolution's closed form, cm*u_bending/((1 - f_a/F_e)*u_combined), tends to 0
       with the bending term. Does the amplified form still govern there?
rule   u_combined = max(amplified, simple); at u_bending = 0 these are f_a/F_a and
       f_a/(0.6 F_y), so the amplified form governs iff F_a < 0.6 F_y
out    F_a(KL/r = 30.4) = 1.926954e+08  <  0.6 F_y = 2.130000e+08   -> TRUE
out    and down that path at eps = 1.0e-10, measured through `check_member`:
out      My = 1e6 -> 3.074923e-13   1e5 -> 3.088937e-14   1e4 -> 3.108077e-15
out      My = 1e3 -> 1.828331e-16   1e2 -> 0.000000e+00
judge  **THE INFIMUM IS 0 AND IT IS ATTAINED WHILE THE AMPLIFIED BRANCH IS STILL THE
       GOVERNING ONE, SO NO CONSTANT CAN SATISFY MY CONDITION AS I WROTE IT.** I reproduced
       the entry's five-row table to every digit, from the module rather than from the
       closed form, and I checked the branch inequality rather than taking it. **My wording
       is WITHDRAWN.** The second option my own condition offered -- points chosen at the
       weak end, margin restated from there -- is the only one available and it is the one
       taken.
cmd    the whole family, through the gate's own helpers, at the shipped values
out    35 points. CM_JOINT_TRANSLATION live at 3 of them:
out      3.074923e-13 (KL/r=30.4)   5.621925e-11 (60.8)   8.281906e-11 (121.5)
out    ALLOWABLE_TENSION_FACTOR 1.147542e-12 and 9.999994e-11; ALLOWABLE_SHEAR_FACTOR
out      1.000000e-10; BEAM_SHEAR_AREA_FACTOR 9.999985e-11; ELASTIC_LOCAL_BUCKLING_C
out      9.999979e-11 and 9.999985e-11
out    WEAKEST LIVE over the family = 3.0749226272928885e-13; margin over 3.0e-13 =
out      1.024974x
judge  **THE DECLARED FIGURES ARE THE SAME DOUBLES I GET AND THE WEAK POINT IS WHERE IT IS
       SAID TO BE.** The new point is 183x weaker than the next weakest, so which point wins
       is not marginal; the margin to the counter is 2.5%, tighter than the 1.0355x the old
       value had, and pinned from above -- COUNTER -> 3.1e-13 gives 2 failed.
cmd    an independent hand side for section 3.2.2, written in my own sweep, in two
       spellings, against the module at the two exact decimals the entry names
out    6.50115566720729e-16   at F_y = 355 MPa, D/t = 106.76, KL/r = 108.1
out    6.538410439539509e-16  at F_y = 420 MPa, D/t = 240.85, KL/r = 108.0
out    identical under both spellings of the same hand arithmetic
judge  **BOTH PUBLISHED FIGURES REPRODUCE TO ALL SIXTEEN DIGITS AGAINST A HAND SIDE WRITTEN
       INDEPENDENTLY OF BOTH THE TEST FILE AND THE REPORT's SWEEP.** The lower edge
       `15.2942x` is sound as a magnitude and clears `F4_WINDOW_RULE_MIN_EDGE = 2.0` by
       7.6x, so the ceiling does not move.
cmd    and on the 0.2% disagreement between our two sweeps, which the report asked me to
       rule on
out    my own 0.01-step scan over D/t 100..120 at the locked grade has a MAXIMUM of
out      4.885e-16 and reaches 6.4e-16 at NONE of 2001 points -- because `dt += 0.01`
out      accumulates, so my grid never lands on the exact decimal 106.76
out    every worst either of us found sits at KL/r = 108.0 or 108.1, against C_c between
out      113.86 and 115.96
judge  **THE IMPLEMENTER's READING IS RIGHT AND IF ANYTHING UNDERSTATED.** The quantity is
       pure round-off: it is not flat in that neighbourhood so much as NOISY, and its argmax
       is a function of the last bits of `D/t` and of how the hand side is spelled. The
       magnitude is reproducible; the location is not. **No finding.** The over-precision on
       the location is C61, with the mechanism: every worst is at the inelastic branch's
       safety polynomial near `C_c`, not at `F_xc`'s fractional power, which is what the OLD
       entry attributed it to.
```

**So R750 is CLOSED on all three of its conditions.** The counter is a floor beneath the
gate's own points with those points placed at the weak end; the window entry states the edge
over the domain the ceiling defends with the `(F_y, D/t, KL/r)` it was taken at; and EH4's
weakening direction is formed, asserted, and reported beside the maximum.

## 5. THE ADVERSARIAL CASE (EU1) -- WHAT I RAN AT CONFIGURATIONS THE DIFF DID NOT CHOOSE

Two tolerance values moved, so EU1 fires. Six probes. Two found something.

```
1  THE TWO FORMS OF SECTION 3.3.2, RECOMPUTED PER PUBLISHED ROW, against what the
   deliverable says about them.  -> R752. 7 of 17, not 10, and the ten are the other set.
2  1792 (KL/r, f_a/F_e, My) CONFIGURATIONS instead of the three the gate has. 1595 live,
   762 below the shipped counter, minimum 1.112868e-16 -- and that is NOT a finding, because
   the entry now scopes its claim to the gate's own points and proves the infimum is 0. The
   measurement that matters is the other direction: the minimum where bending is at least
   1% of u_combined is 8.647182e-13, ABOVE the gate's chosen point at 3.074923e-13, whose
   own bending share is 0.217%. The chosen point is at the weak end in the only sense
   available.
3  AN INDEPENDENT HAND SIDE FOR SECTION 3.2.2 over six grades and D/t from 5 to 300, in two
   spellings.  -> both published clean worsts reproduce to 16 digits; the argmax does not
   survive a change of grid.  -> C61, not a finding.
4  THIRTEEN MUTATIONS OF THE GATE ITSELF -- its aggregation, its point set, its three
   constants.  -> reverting `_weakest_live_move` to `_worst_move` leaves 68 passed; moving
   the weak-end point's My or KL/r leaves 68 passed; the counter may fall BELOW its own
   ceiling and the injection may rise without bound, both with 68 passed.  -> C58 and C59,
   and I say under them why they are not blocking.
5  A CONSISTENT CHANGE OF UNIT SYSTEM -- the same physical state in (Pa, N) and (kPa, kN).
   U = 1.0810699109478443 against 1.0810699109478445, relative 2.054e-16, so the utilisation
   is unit-invariant. The section 3.2.3 BRANCH SELECTION is not: `section_class` at
   `fy = 355e3` reads D/t = 100 as `compact`, so `F_b` would be `0.75 F_y` instead of the
   second reduced branch -- unconservative by `1/0.72` -- and `fy = 0.0` raises a bare
   `ZeroDivisionError`. Unreachable from any shipped caller.  -> C60.
6  26 CLAUSE MUTATIONS. 26 killed. Nothing survives. Section 3.
```

**And two things that did NOT break, recorded because an absence is a measurement.** The
deliverable regenerates byte-identically from the committed generator, both files. And the
`K = 1.0` and `C_m = 1.0` sensitivity columns each move exactly one variable:
`check_member(k_l_over_r=kl1, ...)` recomputes `F_a` AND `F_e` at the same `KL/r`, so neither
column is a mixture of two configurations -- which is the defect I went looking for in the
generator and did not find.

## Closure items

Named with their site and what would close each. The implementer fixes the whole list once,
in the step's closure commit; they are not re-reviewed item by item and the step is not held
on one. Verdict 111's list ended at C57, so this one starts at C58. **C41 to C57 remain open
and are not re-adjudicated here.**

* **C58.** `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:654`, `:990` and
  `:1014`. **R750's repair is not self-protecting.** Reverting `_weakest_live_move` to
  `_worst_move` in the counter assertion gives `68 passed`; the same substitution in the
  bracket test gives `68 passed`; changing the weak-end point's `My` from `1.0e6` to `1.0e8`
  gives `68 passed`, and its `KL/r` from `30.4` to `90.0` gives `68 passed`. The declared
  basis -- margin `1.024974x`, points placed AT the weak end -- would become false in
  silence and the gate would return to the state R750 found. The `35`-point count catches a
  DELETED point (`1 failed, 66 passed`) and a key COLLISION (`1 failed, 67 passed`) and no
  replacement that keeps a distinct key. **Not blocking: everything the gate asserts today
  is true and I verified every shipped figure.** **Closed when** the weak-end point's
  identity is asserted -- the simplest form is an assert that the minimum over live points
  is attained at the `KL/r = 30.4` key -- or the absence is recorded as accepted.
* **C59.** `floatfea/tolerances.py`, the three F6 window constants. Each has unasserted slack
  in the direction that weakens it: the counter may FALL to `1.0e-15`, a tenth of its own
  ceiling, with `68 passed`; the injection may RISE to `1.0e-8` with `68 passed`; the ceiling
  may RISE `15x` with `68 passed`, the solved bound being
  `weakest / F4_WINDOW_RULE_MIN_EDGE = 1.5375e-13`. The third is the window rule's designed
  slack at `MIN_EDGE = 2.0` and I am not reopening that; the first is the one worth a line,
  because nothing asserts `COUNTER > CEILING` and the line that used to compare a response
  with the ceiling was moved onto the STRONGEST point in the same commit. **Closed when**
  `COUNTER > CEILING` is asserted once, or the three slacks are recorded as accepted with
  these numbers beside them.
* **C60.** `floatfea/checks/api_wsd.py:146`. `section_class` divides by `PASCAL_PER_MPA` and
  nothing refuses an `F_y` that is not in pascals: at `fy = 355e3`, `D/t = 100` reads
  `compact` with `limit_1 = 29126.7606` where the same section at `355e6` reads `reduced_2`;
  `fy = 0.0` raises `ZeroDivisionError` rather than a named refusal. FB1 had the module
  refuse a `D/t` outside the clause's range rather than extrapolate, and the clause's own
  `10340/F_y` form is what makes `F_y`'s unit load-bearing. **Closed when** an implausible
  `F_y` is refused the way an out-of-range `D/t` is, or the absence is recorded with the
  reason that no shipped caller can reach it.
* **C61.** `floatfea/tolerances.py`'s `F6_API_CLAUSE_AGREEMENT` entry. The location
  `(420 MPa, D/t = 240.85, KL/r = 108.0)` is published to five figures for a quantity that is
  round-off: my own 0.01-step scan at the locked grade peaks at `4.885e-16` and reaches
  `6.4e-16` at none of 2001 points, because accumulated `+= 0.01` changes the last bits. The
  magnitude and the `15.2942x` edge are sound. Two further things in the same entry: every
  worst either of us found is at `KL/r = 108.0`/`108.1` against `C_c` between `113.86` and
  `115.96`, so the mechanism is the inelastic branch's safety polynomial near `C_c` and not
  `F_xc`'s fractional power the old entry named (BP0); and no committed script regenerates
  that block (BI3). **Closed when** the location is given as a neighbourhood, the mechanism
  is restated, and the block either gets its generator or moves to the step report with a
  pointer.
* **C62.** `floatfea/tolerances.py`'s `F6_API_CLAUSE_INJECTION_EPS` entry. "`1.0e-10` is two
  decades above [`6.504229e-12`]" is true of the ceiling-based boundary and reads as
  headroom; at the shipped counter the injection may fall only `2.5%`, to `9.757e-11`, before
  the gate reddens, because the counter is a function of it. **Closed when** the entry says
  which boundary the two decades are above.
* **C63.** `docs/reports/F6/step-1.md` section 9a, the `R741 | floatfea/checks/api_wsd.py:147`
  row, which gives R749's `limit_1` reason. At verdict 110's own commit `0b9ea0d`, line 147 is
  the closing `"""` of `allowable_axial_compression`'s docstring, not `limit_1`. **I checked
  the rest of that group at `0b9ea0d` rather than at HEAD and the other twenty-one rows are
  correct**: lines 132-153 there really are that function's `def`, docstring, guards and
  body, and R742's `:102`/`:103` really are the two branch limits. **One row of eighty-seven
  is wrong and the reasons are not boilerplate.** **Closed when** that row reads what line
  147 was.
* **C64.** `scripts/measure/api_wsd_utilisation.py:234`. `args.out.relative_to(ROOT)` raises
  `ValueError` when `--out` points outside the repository, AFTER both files are written, so
  the script exits non-zero having succeeded. **Closed when** the print is
  relative-or-absolute.
* **C65.** The published whole-suite line describes `a041574` (`3106 + 315 + 9 + 1 = 3431`)
  while the reviewed commit `54ff15c` has `3433` passing in my run -- two extra
  parametrisations over the longer revision. The fixed point is real and the resolution is
  right; the consequence is that no published whole-suite figure ever describes the commit
  under review. **Closed when** the two-test difference is explained or deliberately ignored
  in one sentence. This one may well close by saying so.
* **R735, R736, R738, C34 to C40, and the `0.2240`/`0.2239` item** -- still open from verdict
  109, carried in `docs/closure/F4.md`, not re-adjudicated.
* **R712 to R717, C2 to C15, C24 to C33, C41 to C57** -- still open, carried, not re-reviewed
  item by item, per CZ0. **C45 still needs its own standalone `process:` commit**, and C52's
  publishing-boundary half is still open -- I measured both negations unguarded at rung 4.

## Tolerances touched

```
cmd    git diff fdb4ecd..54ff15c -- floatfea/tolerances.py | grep -E "^[-+][A-Z0-9_]+: Final"
out    -F6_API_CLAUSE_AGREEMENT_COUNTER: Final[float] = 8.0e-13
out    +F6_API_CLAUSE_AGREEMENT_COUNTER: Final[float] = 3.0e-13
out    -F6_API_CLAUSE_INJECTION_EPS: Final[float] = 1.0e-12
out    +F6_API_CLAUSE_INJECTION_EPS: Final[float] = 1.0e-10
cmd    git diff --stat fdb4ecd..54ff15c -- floatfea/checks/api_wsd.py
out    (empty)
judge  **TWO VALUES MOVED, THE MODULE THEY MEASURE IS BYTE-IDENTICAL, AND THE ASSERTION
       MOVED FIRST.** Neither value rescues a code change because there is no code change in
       the range for it to rescue. EU1 fires and section 5 is the adversarial case.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F6_API_CLAUSE_AGREEMENT` | `1.0e-14` | unchanged | dimensionless, RELATIVE; exactness at a small multiple of round-off | `F6_API_CLAUSE_AGREEMENT_COUNTER` | `floatfea/tolerances.py` entry; `docs/milestones/F6.md` section 3a | **ADMISSIBLE, AND THE BASIS R750 ASKED FOR IS NOW THE RIGHT ONE.** The value did not move; its stated lower edge did, from `59.3937x` over the gate's own points to `15.2942x` over the domain the ceiling defends, with the `(F_y, D/t, KL/r)` given. Both dense figures reproduce to all sixteen digits against a hand side I wrote independently, in two spellings. The edge clears `F4_WINDOW_RULE_MIN_EDGE = 2.0` by `7.6x`. The over-precision on the LOCATION and the stale mechanism sentence are C61; that the ceiling may rise `15x` with the gate green is C59 and is the window rule's own design. |
| `F6_API_CLAUSE_AGREEMENT_COUNTER` | `8.0e-13` | `3.0e-13` | dimensionless; a floor beneath the gate's own points, with those points at the weak end | n/a, it IS the counter (AO2) | same entry | **ADMISSIBLE, AND THE FORM IS NOW DEFENSIBLE.** It FELL by `2.67x` while the injection rose `100x`, which is a tightening in the quantity that matters: the counter is asserted against the MINIMUM over live `(coefficient, point)` pairs -- EH4's weakening direction, which this file never formed. Margin `1.024974x` below `3.0749226272928885e-13`, which I reproduce exactly; pinned from above (`3.1e-13` gives `2 failed`); `30x` above the ceiling. That no constant can be a floor beneath EVERY admissible configuration is proved rather than asserted -- the infimum is `0` and attained while the amplified branch still governs, and I verified the branch inequality `F_a = 1.926954e+08 < 0.6 F_y = 2.130000e+08` myself. **My own closing wording is withdrawn.** What nothing holds in place is C58; that it may fall below its own ceiling is C59. |
| `F6_API_CLAUSE_INJECTION_EPS` | `1.0e-12` | `1.0e-10` | dimensionless, STRUCTURAL; an input to a counter-case | none, correctly (AO2) | same entry | **ADMISSIBLE, AND THE RISE IS THE ONLY COHERENT REPAIR.** At `1.0e-12` the weakest live point responded `3.098618e-15`, `0.3099x` the ceiling, so the gate could not resolve a `C_m` defect of the declared size at that configuration at all -- and the alternative repair, holding `eps` and dropping the counter to about `3e-15`, would put the counter BENEATH its own ceiling, which is incoherent. I solved both directions: the gate reddens below `9.757e-11` and survives to `1.0e-8` unasserted. `1.0e-10` is still eight decades below a percent-scale transcription error. The sentence that reads as two decades of headroom is C62. |
| `F6_API_UTILISATION_COUNTER_FACTOR` | `1.1` | unchanged | dimensionless, STRUCTURAL; a load multiplier | none, correctly (AO2) | same entry | **UNMOVED AND STILL ADMISSIBLE.** Re-checked at this commit: the compression case recomputes `F_a*A` from the clause's own branch rather than carrying a literal, asserts the branch, and the elastic-branch exclusion is asserted as `F_a / F_e == 1.0` exactly rather than stated. |
| everything in the F4 block and earlier | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 111 (`fdb4ecd`, judging `dd90505`) was a **HOLD** carrying five names and a closure
list. Every one, with status.

* **R747 (blocking) -- ANSWERED IN FORM, AND ITS REPAIR CARRIES R752.** The structural half
  is done and done well: `_write_summary` no longer interleaves hand-written sentences with
  generated ones about the same quantities, the sets are formed first, and three of my four
  figures reproduce exactly -- the `2/2` split between section 3.3.1 and section 3.3.2 on the
  four over-unity rows, `0.034238` at `platform:hub1_arm` TIP, and `u_axial = 0.000833389`
  against `u_bending = 1.71138` at `platform:hub2_arm` ROOT. Both files regenerate
  byte-identically. **The fourth sentence is generated from the wrong set and is now R752**,
  which blocks and carries into step 2.
* **R748 (blocking) -- CLOSED.** The four citations read `tests/verification/rung5/`, `grep`
  for `rung6` finds nothing in any of them, `ls tests/verification/rung5/` shows the gate, and
  the CSV and summary regenerate byte-identically in the same commit.
* **R749 (blocking) -- CLOSED, and closed better than the condition.** Both limits are exact
  equalities against `section_class(D_OUTER, WALL, FY)` -- which `allowable_bending` itself
  calls, so the pin reaches the branch -- AND `29.2`/`58.3` are inside each limit's own
  neighbourhood AND in `_FB_POINTS`. The `300` refusal is bracketed at `300`/`300.1`, the
  tension switch at `0.0` and `-5e-324`. **26 of 26 mutations killed in my own run**,
  including all six the verdict found surviving, both `-1%` directions nobody asked for, and
  the `PASCAL_PER_MPA` control.
* **R750 (blocking) -- CLOSED on all three conditions, and I withdrew one of my own sentences
  to close it.** Section 4. The measurement that decided it is the branch inequality at zero
  bending, which I took independently.
* **R751 (blocking) -- CLOSED for the `floatfea/` half.** The paragraph states the measured
  attribution, carries a triple `tests/test_tree_prose_consistent.py` runs, and the
  measurement is a rung-4 test on a prescribed sense. Inverting the attribution gives
  `4 failed, 339 passed`; reverting either publishing-boundary negation leaves rung 4 at
  `343 passed`, which the report states rather than papers over. That half stays as C52.
* **R735, R736, R738, C34 to C40, the `0.2240`/`0.2239` item, R712 to R717, C2 to C15,
  C24 to C33, C41 to C57 (closure) -- STILL OPEN**, carried as a list, not re-adjudicated.
* **THE MID EXCLUSION -- still excluded on R736's grounds and still labelled R730 (C50).**
* **THE SCHEDULE -- the escalation verdict 111 anticipated is NOT due, and I agree with the
  report's reading.** Working target 22 October, committed 28 October, today 9 October. Step 1
  closes with one blocking item, which is one generated sentence and one predicate in a file
  the step already ships; it needs no FloatSim run, no new apparatus and no plan change.
  **On today's evidence the 22 October target holds and I would not slip it.** CLAUDE.md's
  escalation trigger is two consecutive steps closing with blocking items. This is the first.
  If step 2 closes carrying anything, the choice -- slip the date or reduce scope -- has to be
  stated with a number beside it rather than restated.

## Carried for the next step

**R752 (blocking) carries by name into step 2's `Carried` section and stays blocking there.**
`scripts/measure/api_wsd_utilisation.py:374-386`, published at `docs/F6_utilisation.md:69`.
Closed when the amplified/simple count is computed from the two forms themselves, the sentence
regenerated, both files regenerated in the same commit, and the causal comment at `:374`
deleted or given its cell. My figures: AMPLIFIED on `7 of 17`, SIMPLE on `10 of 17`;
`1.456719` against `1.711666` at `C_m = 0.85` and `1.713640` at `C_m = 1.0` at
`platform:hub2_arm` ROOT. **Step 2 regenerates this deliverable anyway**, so the fix lands
inside work already planned rather than beside it.

Nothing else carries blocking. The closure list C58 to C65, and the open C41 to C57, go into
the step's closure commit where CZ0 puts them; **CZ1 applies to that commit and EQ0 applies if
it moves a gate or a tolerance** -- which, if C58 or C59 are answered there rather than in
step 2, it will.

## The adversarial corpus (BE3)

**BATCH 44, committed separately at `24fad04`:
`tests/corpus/f6_which_clause_form_governs_and_what_holds_the_counter_in_place.txt`, 25
entries, every one new this round and none of them read by the implementer.**

EG4(e)'s pause to 28 October permits it and the file header claims the exception explicitly:
the surface is **EB6's label-provenance** one -- which clause, and which FORM of it, is
attributed to a published utilisation in `docs/F6_utilisation.md` and `.csv`. A wrong
attribution is what R739 was, what R747 was, and what R752 is.

**COVERAGE: the shipped checks catch 9 of 25.**

```
cmd    grep -c "^id=" <the file>
out    25
cmd    grep "^id=" <the file> | grep -c "expect=catch"
out    9
cmd    python -m pytest -q -p no:randomly <the 8 files that read tests/corpus or the tree
       prose>
out    1458 passed, 2 warnings in 160.26s
```

Against the last six rounds -- 1 of 16, 9 of 21, 4 of 11, 8 of 13, 5 of 22, 8 of 29 -- this is
`36%` against `28%`, and the composition is what moved: **all six misses in group 1 are one
defect and one missing field.** `MemberCheck` does not record which half of
`max(amplified, simple)` was taken, so every caller that wants it re-derives it, and the one
caller that did got it wrong. One field closes six entries.

**And the number that matters beside 9 of 25 is 26 of 26.** Of the twenty-six clause
mutations I ran this round, G6.1 kills all twenty-six; last round it killed thirty of
thirty-four and the four survivors were R749. **The gate is now complete over the clause
arithmetic and over its branch boundaries.** What the corpus still catches is one level up:
not the clause, but the sentence that says which clause governed.

## On the criterion -- I was asked, and I agree with it, and my one disagreement is not about the work

CZ0 as amended by EZ0 is right and I applied it. My single blocking finding is squarely in (a)
without argument: `docs/F6_utilisation.md` is a file sent to Xabier, `scripts/measure/` is
named in EZ0's own definition, and the defect is a false statement about which clause form
governs a published utilisation. **I used no carve-out this round.** Eight items went into the
closure list, including three -- C58, C59, C60 -- that under the retired "truth of a published
figure or sentence" head I would have had to argue about; under CZ0 they are listed once and
cost nobody a round.

**THE ONE DISAGREEMENT, AND IT IS WITH THE MECHANISM RATHER THAN THE WORK.** For the second
consecutive round, the two guards that are red BY CONSTRUCTION at the commit a round's code
lands in -- `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` and
`test_the_report_carries_a_WHOLE_SUITE_count` -- are on NEITHER of EG3/EH1's two lists, and
EH1 says in terms that any red not on the list still blocks. Verdict 111 admitted the second
by hand on the ground that it is green at the reviewed commit; I have now admitted both the
same way. **That is a reviewer exercising discretion twice about a state the rule says blocks,
which is exactly what EG3(i) exists to stop.** The fix is one of two sentences and neither is
mine to write: either EG3's state (1) list gains those two names, or the two guards read the
previous commit so that they can be measured before a push. **This goes to Xabier through the
implementer and it does not become another round.** I record it because the alternative is a
third reviewer making the same undocumented call.

**And one thing on the record for the implementer rather than against them.** Four of five
blocking items closed, each one I ran rather than read, and three of them closed better than
the condition asked: R749 took both options instead of one, R748's regeneration is
byte-identical, R751 states the limit of its own test instead of claiming the item.
**R750 is the best work in this milestone.** It refused the condition I wrote, proved the
refusal (`F_a = 1.926954e+08 < 0.6 F_y` with the amplified branch still governing at zero
bending), took the option that remained, moved the assertion before the values and showed the
red, and published the disagreement between our two sweeps as a disagreement rather than
reconciling it. I checked every digit and every digit holds. **The one thing that went wrong
went wrong in the same place it has gone wrong three rounds running**: not in the arithmetic,
which is now pinned twenty-six ways, but in a sentence about which clause governs -- and this
time the sentence was generated, which is what we both asked for, from a predicate I handed
over in a verdict. Generating a sentence from a set is only as good as the set, and the set is
the thing to review next time.

## Next step opens when

**STEP 1 IS CLOSED. THIS WAS THE THIRD REVIEWED REVISION AND CZ0 CLOSES THE STEP.** Step 2
may open now. The conditions on it, specifically:

1. **Step 2's report answers R752 by name in its `Carried` section**, with the count computed
   from the two forms and both deliverable files regenerated in the same commit (BP0). It
   stays blocking until then.
2. **The closure commit carries C58 to C65 and the open C41 to C57**, fixed once, not
   re-reviewed item by item. **C45 needs its own standalone `process:` commit.** CZ1 (i) to
   (iv) applies to that commit, and EQ0 applies -- so it is REVIEWED, and that review counts
   against no step's rounds -- if it answers C58 or C59, because both move a gate assertion.
3. **Step 2's own gate is that the table regenerates identically from stored results and the
   top-ten list is stable under a re-run.** I measured the first half for step 1's deliverable
   today and it holds byte for byte. The stability of a top-ten list under TIES is the part
   that does not: `hub2:buoy4_arm` ROOT and `hub4:buoy10_arm` ROOT carry `0.009245` to every
   published digit and `max` returns whichever comes first, which is the shape to design
   against before the list is published rather than after.
4. **The MID column stays excluded** on R736's grounds, and the published label still says
   R730 (C50).

**What I will not accept at step 2's first revision.** A count or a clause attribution in a
published table that is derived from a PROXY for the quantity rather than from the quantity --
that is R752, and it is the third round in a row that the arithmetic was right and the
sentence about which clause governed was wrong. A top-ten list whose order depends on row
order among equal values. And a measurement block in `floatfea/tolerances.py` that no
committed script regenerates, now that BI3 has been on the closure list for two rounds. The
question for all three is the recorded one: if the thing this claim asserts were false, would
anything go red. For R752 I measured the answer and it is no.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6 step 1
Reviewed commit: a0482e2a03525f72ab64c9137de1a9b4a65b616b
Verdict: HOLD
**Reviewed commit: `dd90505`** (`dd905051ff75f9506a6c383906fb62bec24cd0a6`, tree clean when I
judged it; my corpus batch 43 is committed on top at `a0482e2`, which is why the plain
`Reviewed commit:` stamp is not the commit I judged -- R718's subject, and this bold line is
the mechanism.)
Tests: 3358 passed, 0 failed, 0 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `dd90505`, `661.48s`. The
report's whole-suite line is `3100 passed` plus an excluded set of `249 passed, 8 failed,
1 skipped` AT `1f8f61a`; `3100 + 249 + 8 + 1 = 3358`, and at `dd90505` all of it is green.)

## Round of 2026-10-09 -- ROUND 2 OF THREE, F6 step 1. **HOLD.** Five blocking items. The gate was built, it is good work, and the two Â§ 3.2.3 branch limits it was built to pin survive a digit swap.

**WHY HOLD, IN SIX SENTENCES.** G6.1 exists, it is 65 tests at 32 points, it runs in CI on
ubuntu at rung 5, and I mutated every numeric literal on an executable line of
`floatfea/checks/api_wsd.py` one at a time -- **30 of them redden it**, including the
`0.75 F_y` cap, both halves of Â§ 3.3.2's `max`, the bending resultant, `C_c`'s `2`, the
safety-factor polynomial and `F_xc`'s fractional power. **Four survive, and two of the four
are `10340` and `20680`** -- the two numbers R742 was about: `10340 -> 10430` and
`20680 -> 20860`, the classic transcription slip, each leaving `65 passed`. The third
survivor is Â§ 3.2.2's `D/t = 300` refusal at `303`. **The published deliverable's summary
prose contradicts its own published table on four counts**, and one of them is R739's own
subject -- "All four are platform arm ROOTs, all governed by Â§ 3.3.1" where the CSV and the
top-ten table three inches above it both say two are Â§ 3.3.2. **The deliverable's G6.1
warrant cites `tests/verification/rung6/`**, which holds `__init__.py` and
`.empty-by-design` and is run as `empty:` in CI -- the gate moved to rung 5 at `1f8f61a`
and the four citations of it did not. And **the counter is a constant pinned to one of two
chosen points at a `1.0355x` margin**: over 350 live amplified-governing configurations the
diff did not choose, 266 sit at or below it and the weakest is `267x` below.

**No STOP.** No low rung is red: `the verification ladder` is SUCCESS at `1f8f61a` with
rung 5 `full:` and `run_rung: 65 collected, 0 failed`. The locked plan is not wrong; FB0
inverted FA3 for F6 and the step did what FB0 asked.

**WHAT THE IMPLEMENTER ASKED ME TO CHECK, AND WHAT THE ANSWER WAS.** Nine items were named.
Items 4 (R744), 5 (the rung placement), 6 (R737) and 8 (R743/FB2) hold, and I measured each
rather than reading it. Item 1's claim that no `# expected:` is a module call holds, with
one caveat in the closure list. Item 2(b) -- changing the material to make Â§ 3.2.2(b)'s
elastic half reachable -- is the **right** call and I say so in Â§ 4. Item 3 is where the
finding is. Item 7's fifth figure disagreed for a reason neither of us had: **I am
withdrawing my own `0.034926`**, and the cause is not only the basis.

## 0. CI -- UNAVAILABLE AT THE REVIEWED COMMIT BY DESIGN, AND THE LAST RUN DESCRIBES THIS TREE

```
cmd    gh run list --commit dd905051ff75f9506a6c383906fb62bec24cd0a6 --json conclusion,status
out    []
cmd    gh run list --commit acfc5df5e6940ca7e1232d1097296c7bce9aa987 --json conclusion,status
out    []
cmd    sed -n '22,26p' .github/workflows/ci.yml
out    on: push: branches ["**"] paths-ignore: - "docs/reports/**"
cmd    git diff --stat 1f8f61a..dd90505
out    docs/reports/F6/step-1.md | 82 ++++++---     one file, and it is the ignored path
judge  **THIS IS NOT CK2 AND IT IS NOT CA2's RED.** No run exists at the reviewed commit
       because that commit touches only `docs/reports/**`, which CK0 ignores by its own
       recorded decision. It is UNAVAILABLE and is recorded as that. The last run that
       executed is at `1f8f61a`, and the only difference between that tree and this one is
       a report file, so its result still describes the code under review. `acfc5df` has no
       run of its own because it was pushed together with `1f8f61a`.
cmd    gh run list --commit 1f8f61a4f5fd9b374c4e7e92f6a428485c4c1622 --json ...
out    [{"conclusion":"failure","databaseId":37939206345,"event":"push","status":"completed"}]
cmd    gh run view 37939206345 --json jobs -q '.jobs[] | .name + " " + .conclusion'
out    the verification ladder            success
out    lint, unit and guards              failure
out    CI determinism -- leg              skipped
out    CI determinism -- ten legs agree   skipped
cmd    gh run view 37939206345 --json jobs    (the ladder job, step level)
out    ladder 1 / 2 / 3 / 6 / 4 / 5           all success
cmd    gh run view 37939206345 --log | grep "ladder 5"
out    run_rung: 65 collected, 0 failed, 0 errored, 0 skipped
out    run_rung: OK -- 1 director(y|ies) ran
judge  **THE 65 TESTS RAN ON UBUNTU AND ARE GREEN THERE**, and rung 5 really is `full:`
       with the marker deleted in the same commit. That is the one measurement the
       tolerance's own justification could not take on one machine, and it is the answer to
       the implementer's item 3: the `1.0e-14` headroom for a `pow` that is not correctly
       rounded is now an ubuntu measurement and not only an argument.
cmd    gh run view 37939206345 --log | grep -E "^FAILED|failed," | sort -u
out    8 failed, 1081 passed, 1 skipped, 1 warning in 310.57s
out    FAILED tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count
out    FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
out      + 6 more planted states, each pasting that one red in its own failure line
judge  **THE CLAIM IS EXACTLY RIGHT AND I CHECKED IT RATHER THAN TOOK IT.** Eight reds, one
       cause, each traced by name. `test_the_report_carries_a_WHOLE_SUITE_count` is on
       NEITHER of EG3's two lists, so under EH1 it would block -- except that it is red at
       `1f8f61a` and GREEN at the reviewed commit, which my own full run measures. The
       fixed point is real: `scripts/suite_count.py` measures a clean worktree AT a commit,
       so a line naming `1f8f61a` cannot be inside `1f8f61a`. Landing it in a report-only
       follow-on that creates no run is the right resolution and it is self-clearing.
       **Nothing outside those three files was red at `1f8f61a`, and nothing at all is red
       at `dd90505`.**
```

## 1. MY OWN INSTRUCTIONS, THE CONFTEST AND THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
cmd    git diff 2cf33b0..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git diff --name-status 2cf33b0..HEAD -- '*conftest*' '*plugin*' tests/
out    D  tests/verification/rung5/.empty-by-design
out    A  tests/verification/rung5/test_g61_api_wsd_hand_calculations.py
judge  CH2/CI0: no conftest and no plugin anywhere in the range, so no rung's green is
       written from its own directory and I did not have to read a hookwrapper. The one
       `tests/` addition is the gate itself, and I read all 1012 lines of it.
cmd    git diff --stat 2cf33b0..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
judge  **CLEAN.** My own instructions are untouched in this range. C45 is still open and is
       still process class rather than step work.
cmd    git diff 2cf33b0..HEAD -- floatfea/tolerances.py | grep -cE "^-[^-]"
out    1       the single line `# (no entries yet -- F6/F7)`
judge  **NOTHING WAS WIDENED AND NO EXISTING VALUE MOVED.** Four entries are new. EU1
       FIRES -- tolerance values moved -- so Â§ 5 is the adversarial case, run at
       configurations the diff did not choose. That is what found R750.
```

## 2. WHAT G6.1 CATCHES -- MEASURED, NOT READ

I mutated every numeric literal on a code line of `floatfea/checks/api_wsd.py` by `+1%`,
one at a time, restoring the source byte-identical after each, and re-ran the whole of
rung 5 each time. This is the measurement the gate deserved and the one no planted-shape
count can substitute for.

```
cmd    56 literals, one 1% edit each, `pytest -q -p no:randomly tests/verification/rung5`
out    30 KILLED on executable lines; 4 SURVIVED; the rest were inside docstrings or f-strings
out    KILLED: C_c's 2.0; F_e's 12.0 and 23.0; F_xe's 2.0; F_xc's 1.64, 0.23 and 0.25;
out            the safety polynomial's 5.0/3.0/3.0/8.0/3/8.0; (1.0 - 0.5 r^2); the 0.75 cap;
out            0.84, 1.74, 0.72, 0.58; the amplification's 1.0
out    KILLED: PASCAL_PER_MPA, LOCAL_BUCKLING_DT, BENDING_THIRD_BRANCH_NUMERATOR,
out            CM_JOINT_TRANSLATION, ALLOWABLE_TENSION_FACTOR, ALLOWABLE_SHEAR_FACTOR,
out            BEAM_SHEAR_AREA_FACTOR, ELASTIC_LOCAL_BUCKLING_C
out    KILLED: u_combined = amplified alone (1 failed); = simple alone (5 failed);
out            the 0.75 cap disabled (3 failed); hypot -> max (4 failed)
judge  **THIS IS A REAL GATE.** Eight module constants and twenty-two in-line clause
       coefficients each redden it, both halves of Â§ 3.3.2's `max` are live, and R742's own
       cap has a control that fires when it is removed. Verdict 110 said G6.1 was the next
       thing to build and six of eight findings were inside its scope; it was built and it
       would have caught them. The four survivors are R749.
```

## Findings

**R747. (BLOCKING. (a) AS AMENDED BY EZ0 -- A DEFECT IN A PUBLISHED DELIVERABLE AND IN THE
`scripts/measure/` GENERATOR THAT PRODUCES IT.) THE DELIVERABLE'S SUMMARY PROSE CONTRADICTS
ITS OWN PUBLISHED TABLE ON FOUR COUNTS, AND ONE OF THEM IS R739's OWN SUBJECT -- THE
GOVERNING CLAUSE ON THE OVER-UNITY STATIONS.**
`scripts/measure/api_wsd_utilisation.py:363-375` (the hand-written block inside
`_write_summary`), published at `docs/F6_utilisation.md:81-83`.

```
claim  the four sentences in the summary block, against the CSV the same run wrote
cmd    python -I -c "read docs/F6_utilisation.csv; group the 4 rows with U > 1.0 by
       governing_clause; read u_axial/u_bending at the worst station; max |U(K2)-U(K1)|;
       count compression rows where utilisation_Cm1 != utilisation_K2"
rule   the published table and CSV in the same file, written by the same run
out    PUBLISHED  "All four are platform arm ROOTs, all governed by section 3.3.1"
out    MEASURED   hub1_arm ROOT 3.3.1 (1.17709); hub2_arm ROOT 3.3.2 (1.71167);
out               hub3_arm ROOT 3.3.1 (1.18223); hub4_arm ROOT 3.3.2 (1.71167)
out               Counter({'3.3.1 interaction': 2, '3.3.2 interaction': 2})
out    PUBLISHED  "changes the governing number by at most `0.024`"
out    MEASURED   0.034238 -- and the GENERATED code block at :77 prints that figure
out               three lines above the sentence
out    PUBLISHED  "u_axial = 0.0004 against u_bending = 1.815"
out    MEASURED   worst station platform:hub2_arm ROOT: u_axial 0.000833389,
out               u_bending 1.71138.  `1.815` is the total_max/total_min figure R740 was
out               about, which the label at :16 says is NOT used here
out    PUBLISHED  "the amplification never bites, and on the compression rows the simple
out               0.6 F_y form governs over the amplified one"
out    MEASURED   10 of 17 compression rows have utilisation_Cm1 != utilisation_K2, which
out               can only happen where the amplified form governs, because C_m appears
out               nowhere else in the calculation
judge  **THE FIRST ONE IS THE FINDING AND THE OTHER THREE ARE THE SAME MECHANISM.** R739's
       whole subject was that the published clause attribution on the over-unity stations
       was wrong; the CSV and the top-ten table are now right and the sentence a reader
       reads last is the pre-repair one. The fourth is a causal claim (BG0) refuted by the
       `U (C_m=1)` column this same commit added. Verdict 109's single blocking finding was
       a defect in the repair of the previous finding in this class; this is that again,
       and the class is why EZ0 exists.
```

**Closed when** the four sentences are generated from the sets they describe or deleted,
and `docs/F6_utilisation.csv` and `docs/F6_utilisation.md` are regenerated in the same
commit (BP0). The 2/2 split, `0.034238`, `u_bending = 1.71138` and `10 of 17` are my
figures to beat; if the regeneration disagrees I want the disagreement, not a
reconciliation. The structural half of it is that `_write_summary` interleaves generated
f-strings with hand-written sentences about the same quantities, and the hand-written ones
are the four that are wrong.

**R748. (BLOCKING. (a) UNDER EZ0.) THE DELIVERABLE'S G6.1 WARRANT CITES A DIRECTORY THAT
CONTAINS NO TESTS AND THAT CI RUNS AS `empty:`. THE GATE MOVED AT `1f8f61a` AND ITS FOUR
CITATIONS DID NOT.**
`docs/F6_utilisation.md:9`, `docs/F6_utilisation.csv:5`,
`scripts/measure/api_wsd_utilisation.py:36` and `:92`.

```
claim  "G6.1 is GREEN: every clause is verified against an independent hand calculation in
       tests/verification/rung6/, at two or more points per branch, either side of every
       boundary (FB0)."
cmd    ls -a tests/verification/rung6/ ; ls tests/verification/rung5/
out    rung6:  .  ..  .empty-by-design  __init__.py
out    rung5:  __init__.py  test_g61_api_wsd_hand_calculations.py
cmd    grep -n "rung6" .github/workflows/ci.yml
out    run: sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression
cmd    git show 1f8f61a --name-only
out    .github/workflows/ci.yml  docs/milestones/F6.md  docs/reports/F6/step-1.md
out    floatfea/tolerances.py  tests/verification/rung5/.empty-by-design
out    tests/verification/rung5/test_g61_api_wsd_hand_calculations.py
judge  **THE CITATION DOES NOT RESOLVE, AND IT NAMES THE ONE DIRECTORY CI ASSERTS IS
       EMPTY.** The commit that moved the gate out of rung 6 did not touch the deliverable,
       the CSV or the generator, so the published warrant now points at exactly the state
       `1f8f61a` was written to escape -- a rung whose own green result could not say that
       nothing in it runs. "Every citation resolves" is one of the recorded guards and this
       is the shape it names: a reader checking the deliverable's own evidence finds
       nothing at the path given. BP0 is the mechanical half: the gate's location is the
       rule the sentence cites, it moved, and the artifact citing it was not regenerated in
       the same commit.
```

**Closed when** the four sites read `tests/verification/rung5/` and the CSV and the
summary are regenerated in the same commit, with `ls tests/verification/rung5/` pasted. One
string and one run. I am naming the classification rather than smuggling it: this is a
sentence, and under the retired head it would have been a closure item -- it blocks because
`docs/F6_utilisation.md` is a file sent to Xabier and `scripts/measure/` is named in EZ0's
own definition, and because the sentence IS the deliverable's warrant rather than a remark
inside it.

**R749. (BLOCKING. (c) -- A GATE ASSERTION: WHAT THE GATE CLAIMS, ON WHICH QUANTITY, AT
WHAT THRESHOLD.) G6.1 DOES NOT PIN Â§ 3.2.3's TWO BRANCH LIMITS OR Â§ 3.2.2's REFUSAL
THRESHOLD. `10340 -> 10430` AND `20680 -> 20860` EACH LEAVE ALL 65 TESTS GREEN, AND THOSE
ARE THE TWO NUMBERS R742 WAS ABOUT.**
`floatfea/checks/api_wsd.py:147`, `:148`, `:226`, against
`tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:368` and `:472` and
`docs/milestones/F6.md` Â§ 3a.

```
rule   docs/milestones/F6.md section 3a: the agreement is measured "over 32 points either
       side of every branch boundary"; the test file's own docstring: "the points sit
       EITHER SIDE OF EVERY BOUNDARY rather than in the middle of a range -- C_c, the three
       D/t limits, the local-buckling limit, the tension/compression switch. A point taken
       only in a branch's interior cannot see a misplaced boundary, which is R742's whole
       mechanism."
cmd    one edit each, source restored byte-identical, whole of rung 5 re-run
out    limit_1 = 10340.0 -> 10430.0   (a digit swap)       65 passed in 0.40s
out    limit_1 = 10340.0 -> 10443.4   (+1%)                65 passed in 0.40s
out    limit_2 = 20680.0 -> 20860.0   (a digit swap)       65 passed in 0.41s
out    limit_2 = 20680.0 -> 20886.8   (+1%)                65 passed in 0.41s
out    if d_t > 300.0  ->  if d_t > 303.0                  65 passed in 0.39s
out    in_tension = axial_n >= 0.0  ->  > 0.0              65 passed in 0.40s
cmd    the bracket each boundary actually has, from _FB_POINTS and _FXC_POINTS
out    limit_1 = 29.1268 : nearest points 29.0 and 30.0  -- 0.44% below, 3.0% above
out    limit_2 = 58.2535 : nearest points 58.0 and 60.0  -- 0.44% below, 3.0% above
out    the 300 refusal   : admitted at 300 and 100, refused at 500 and 700
out    LOCAL_BUCKLING_DT : bracketed at D/t = 60 exactly and 60.5 -- and it IS killed
out    limit_3           : `assert limit_3 == 845.0704225352113` at test:472 -- KILLED,
out                        and it is what kills PASCAL_PER_MPA and the third numerator too
judge  **THE GATE ALREADY CONTAINS THE TECHNIQUE THAT WOULD CLOSE THIS AND APPLIES IT TO
       ONE OF THE THREE LIMITS.** `limit_3` is pinned by an exact equality against
       `section_class(...)`; `limit_1` and `limit_2` are not pinned at all. test:368's
       `assert 10340.0 / 355.0 == 29.12676056338028` looks like the missing assertion and
       is not one: both sides are written in the test and neither reads the module, so it
       holds byte for byte under every mutation above -- CW0's triple-whose-command-cannot-
       fail shape, in an assertion rather than a comment. And this is not a hypothetical
       class of defect: R742 was a question about exactly these two numbers one round ago.
```

**Closed when** `limit_1` and `limit_2` are pinned the way `limit_3` already is -- one
exact equality each against `section_class(D_OUTER, WALL, FY)`, which is a one-character
change to test:368 -- or a point is added inside each boundary's own neighbourhood
(`29.2` and `58.3` would do it), and the `300` refusal is bracketed at `300` and `300.1`
the way `LOCAL_BUCKLING_DT` is bracketed at `60` and `60.5`. Re-run the three mutations and
paste both outcomes. No new apparatus: this is inside the file the step already shipped.

**R750. (BLOCKING. (b) -- A COUNTER VALUE AND THE FORM OF ONE, WHICH IS WHAT EU1 ASKS THE
ADVERSARIAL CASE ABOUT.) `F6_API_CLAUSE_AGREEMENT_COUNTER = 8.0e-13` IS A CONSTANT PINNED
TO ONE OF TWO CHOSEN POINTS AT A `1.0355x` MARGIN. AT 266 OF 350 LIVE
AMPLIFIED-GOVERNING CONFIGURATIONS THE DIFF DID NOT CHOOSE IT SITS AT OR ABOVE THE
RESPONSE, AND THE WEAKEST IS `267x` BELOW IT. THE DECLARED WINDOW'S LOWER EDGE IS `15.35x`
AND NOT `59.3937x`.**
`floatfea/tolerances.py` (`F6_API_CLAUSE_AGREEMENT`, `F6_API_CLAUSE_AGREEMENT_COUNTER`),
`tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:888-908`, and
`docs/milestones/F6.md` Â§ 3a's two rows.

```
claim  "`C_m` is the weakest member and stays the weakest by `1.21x` ... so the gate
       resolves a `C_m` error to `0.828392` of its relative size", and
       "margin `1.0355x`" below "the weakest live response over the whole family
       `8.283918449512958e-13`"
cmd    run check_member at 432 admissible configurations -- KL/r in {30.4, 45, 60.8, 80,
       100, 108.1, 121.5, 150, 200}, f_a/F_e' in {0.02 ... 0.95}, My in {1e6 ... 5e8} --
       and scale `cm` by 1 + F6_API_CLAUSE_INJECTION_EPS at each, one variable moved
rule   the gate's own decision rule: the response must exceed
       F6_API_CLAUSE_AGREEMENT_COUNTER
out    configurations with 3.3.2 interaction governing : 432
out    of those, response EXACTLY 0.000000e+00         : 82
out    live                                            : 350
out    at or BELOW the declared counter 8.0e-13        : 266 of 350
out    WEAKEST live                                    : 3.098618e-15  at KL/r = 30.4,
out                                                       f_a/F_e' = 0.4, My = 1e6
out                                                       -- 267x below the counter
out    strongest live                                  : 9.794854e-13
out    the two points the diff chose                   : 0.56 and 0.828392 of eps
judge  **R694's SHAPE EXACTLY, AND THE PLAN RECORDS IT AS SUCH.** "A counter that depends
       on a model parameter is not a number, it is a function, and the question an
       adversarial case asks is which." The resolution has a closed form --
       `cm * u_bending / ((1 - f_a/F_e') * u_combined)` -- and the declared `0.828392` is
       that function evaluated at the better of two chosen points, with a 3.5% margin
       beneath it. The gate passes because `_worst_move` is a MAX over the 32 quantities,
       which is a defensible aggregation for non-vacuity; the sentence declaring what the
       gate RESOLVES is not defensible, and the margin is quoted in the direction that
       makes it look strong.
cmd    test:888-908 -- which direction the declared "weakest" is taken in
out    `weakest = min(responses)` where each response is itself `_worst_move`, a MAX over
out    the 32 points. So `weakest` is min-over-5-coefficients of max-over-32-points, and
out    the min over points is never formed anywhere in the file.
judge  **EH4's WEAKENING DIRECTION WAS NOT SOLVED.** "A boundary is solved in both
       directions, including the two that WEAKEN a gate." The direction that weakens this
       one is the minimum over points, and it is the direction the declared margin is
       quoted in.
cmd    a dense sweep of the clause module's own admissible domain -- D/t <= 300 in steps of
       0.01, at the gate's own two grades, KL/r at seven values -- module against a hand
       side written independently of the test file. 97681 points.
rule   the window rule's lower edge: F6_API_CLAUSE_AGREEMENT / the clean worst
out    declared clean worst   1.683679572698748e-16  -> lower edge 59.3937x
out    DENSE clean worst      6.515863e-16 at F_y = 355 MPa, D/t = 113.43, KL/r = 108.1
out                                                  -> lower edge 15.35x
out    six grades             6.587053e-16 at F_y = 420 MPa, D/t = 260.97, KL/r = 108.1
judge  **THE CONFIGURATION IS ONE THE GATE NEARLY CHOSE** -- the locked grade, a `KL/r`
       already in `_FA_POINTS`, and a `D/t` between the `100` and `200` of `_FXC_POINTS`.
       `15.35x` still clears `F4_WINDOW_RULE_MIN_EDGE = 2.0`, so the ceiling is not wrong;
       the published edge is wrong by `3.87x` as a statement about the module the ceiling
       defends. The gate's own `_quantities` docstring names this hazard in its own words
       -- "a family measured on a narrower domain than the ceiling it defends reports the
       strongest member as the quantity's, which is what R708 and R710 both were" -- and
       the sentence applies to the gate that contains it.
```

**Closed when** the counter is a floor beneath every admissible configuration rather than a
constant at one, which R694's repair shape already demonstrates: either `C_m`'s resolution
is written as the closed form above and the counter derived from its minimum over the
family's own points, or the family's points are chosen at the WEAK end instead of the
strong one and the margin restated from there. **And** `F6_API_CLAUSE_AGREEMENT`'s window
entry states the edge over the domain the ceiling defends (`15.35x`, or whatever a rerun
gives) rather than over the 32 points, with the `(F_y, D/t, KL/r)` it was taken at. **And**
EH4's weakening direction is taken at least once: the minimum over points, reported beside
the maximum. `3.098618e-15`, `266 of 350`, `82 of 432` and `6.515863e-16` are my figures.
I am not ruling that `8.0e-13` is the wrong number -- I am ruling that its stated basis is a
figure about one point and that the gate's own assertion never looks in the direction that
would refute it.

**R751. (BLOCKING. (a) -- AND I AM NAMING THE CLASSIFICATION RATHER THAN SMUGGLING IT.)
`floatfea/post/member_forces.py:23`'s ATTRIBUTION IS STILL INVERTED, AND Â§ 8a RECORDS IT AS
"ALREADY CORRECT". IT IS THE ONLY STATEMENT OF THE AXIAL SENSE IN `floatfea/`, AND R739's
WHOLE REPAIR IS A NEGATION THAT IS CORRECT ONLY IF THAT SENTENCE IS FALSE.**
`floatfea/post/member_forces.py:23`, against `docs/reports/F6/step-1.md` Â§ 8a row 3.

```
claim  (section 8a) "the attribution sentence already says `the forces the ELEMENT exerts
       on its nodes at each end`, which is the true sense and is what R739 measured. The
       verdict's condition asked for it to be corrected; it did not need correcting"
cmd    move node_b of platform:hub1_arm 1 mm OUTWARD along the member axis -- an
       unambiguous stretch -- and read member_forces(body, member, u, zeros(12))
rule   a force the ELEMENT exerts ON node A under TENSION points from A toward B, i.e.
       along +local x, so end_a[0] would be POSITIVE if the sentence held
out    EA/L * 1e-3   true internal N, tension positive (Hooke)  = +5.51010219e+06
out    member_forces end_a[0]                                   = -5.51010219e+06
out    member_forces end_b[0]                                   = +5.51010219e+06
judge  **THE SENTENCE IS BACKWARDS AND THE REPORT'S CLAIM ABOUT IT IS FALSE.** `end_a[0]`
       is negative for a stretch, so the returned vector is the force the NODES exert ON
       THE ELEMENT (`k u`), which is the opposite attribution. The sentence's second half
       -- "end B's axial has the opposite sign to end A's under pure tension" -- is true
       under either attribution, which is exactly why reading it does not refute it and
       only a prescribed-sense measurement does. This reproduces verdict 110's figure to
       every digit, so it is not a question of which of us measured.
cmd    grep -rn "forces the ELEMENT exerts\|force the NODES exert" floatfea/
out    floatfea/post/member_forces.py:23 only
judge  it is the ONLY statement of the sense in the library, and the repair R739 landed is
       `root[0] = -root[0]` at the publishing boundary. A reader who trusts :23 concludes
       the negation is a double correction and deletes it. That is R739 shipped again.
```

**Closed when** the sentence states the sense as measured -- `k u` is the force applied TO
the element, so `end_a[0]` is minus the internal axial action -- with the 1 mm cell above
pasted beside it, and Â§ 8a's row corrected. **The classification, said once:** this is a
sentence, and under the retired "truth of a published figure or sentence" head it would be a
closure item. I block on it because (i) it is the only statement in `floatfea/` of a
convention a published column's sign now depends on, which is the carve-out my instructions
name for a docstring that is the only statement of what something means, and (ii) verdict
110 made it a named site of R739's closing condition and the report recorded that half of
the item as answered on a claim that one command refutes -- "half of an item is not the
item". If Xabier reads the criterion more narrowly, this becomes closure item C56 and
nothing else in this verdict changes.

## 3. WHAT I MEASURED AND FOUND SOUND -- the four the implementer asked about, each run rather than read

```
R744 -- THE SAG CONTROL, mutated at all four sites on a fixture with a_y = 3 and a_z = 2
cmd    four separate one-character mutations of _station_values, each on its own copy
out    HEAD, unperturbed                       OK, exit 0   MID Mz = +2.92968750e+06
out    DEFINITION  sag_z = +w -> -w            REFUSED
out    DEFINITION  sag_y = -w -> +w            REFUSED
out    APPLICATION mid[5] = mid[5] - sag_z     REFUSED
out    APPLICATION mid[4] = mid[4] - sag_y     REFUSED
judge  **R744 IS ANSWERED, BOTH PLANES AND BOTH HALVES.** The subject is now `mid - chord`,
       the delta the station publishes, which is what the condition named. Taken on my own
       fixture, not the report's cell. It is the third round on those two lines and it is
       the first time all four mutations redden.

THE RUNG PLACEMENT (item 5) -- and the guard that caught it is the right guard
out    ladder 5 in CI: run_rung: 65 collected, 0 failed; rung 5 `full:`; marker deleted in
out    the same commit; `run_rung.sh`'s full:/empty: contract satisfied in one commit
judge  SOUND, and self-reported before I could find it. `test_every_test_in_the_suite_is_
       run_by_some_ci_job` earned its keep: 65 green tests running in no job is precisely
       the state no test's own result can report.

R737 (item 6) -- the framing correction is CORRECT and I withdraw my wording
cmd    sed -n '80,95p' scripts/export_platform_deck.py
out    HSP_COMMIT is compared against the live worktree HEAD, with a tag check and a dirty
out    check beside it
judge  **THE IMPLEMENTER IS RIGHT AND MY FINDING WAS LOOSELY WORDED.** "Declared and
       compared nowhere" was wrong: it is compared. What is unpinned at commit level is the
       dynamic-inputs npz, whose provenance records the tag alone. The decision -- the
       provenance gains `hsp_commit` at the next export, the npz resting meanwhile on the
       tag plus the deck's indirect commit-level warrant -- is one of the two branches my
       condition offered and it is recorded. **R737 is CLOSED.** The reading of the
       `import_closure` consequence is also right: the G4.1 staleness assertion reads the
       export script's own blob sha, so touching that script reddens the gate until the npz
       is regenerated, and six FloatSim runs to pin a commit nobody has moved is the wrong
       trade this week. Recording the decision is the whole of what I asked for.

R743 / FB2 (item 8) -- the direction, and my own 5.3x ranking
out    largest |U(Cm=1) - U(K=2)| = 0.009245  against  largest |U(K=2) - U(K=1)| = 0.034238
judge  **MY `5.3x` RANKING DOES NOT SURVIVE THE PER-INSTANT BASIS AND I WITHDRAW IT.** On
       the shipped basis `K` is the larger lever by 3.7x, not the smaller by 5.3x. The
       constant is renamed, the category is Â§ 3.3.1 case (a), the direction is stated as
       measured, and a `C_m = 1.0` column is published. R743 is ANSWERED. The conclusion
       that survives is the one I said survives: u_axial 0.0008 against u_bending 1.7114.
```

## 4. ON ITEM 2(b) -- CHANGING THE MATERIAL TO MAKE A GATE NON-VACUOUS IS THE RIGHT CALL

The implementer asked me to attack this hardest and I will say the opposite instead, because
the measurement supports it.

```
rule   API RP 2A-WSD section 3.2.2(b): F_xc = F_y [1.64 - 0.23 (D/t)^(1/4)], capped at
       F_xe = 2 C E t / D with C = 0.3
cmd    solve min(F_xc, F_xe) = F_xe for D/t, at each grade
out    S355  F_xe never governs at any D/t the clause admits
out    S460  first governs at D/t = 491.94  -- outside D/t <= 300
out    S690  first governs at D/t = 252.53  -- inside
judge  **THE CLAUSE HALF IS INERT AT THE LOCKED GRADE, AND THAT IS A PROPERTY OF THE CLAUSE
       AND NOT A CHOICE OF THE TEST.** A gate that exercised only S355 would have certified
       `ELASTIC_LOCAL_BUCKLING_C` against nothing -- which is what the implementer measured
       as a `0.000000e+00` response before the repair. Taking that one assertion at S690 is
       not relaxing the model; it is the only configuration in which the expression is
       reachable, and the test says so in its own name and docstring and asserts
       `f_xe < f_xc` first so the point cannot drift off the governing side. My own
       mutation sweep confirms it is live: `ELASTIC_LOCAL_BUCKLING_C` 0.3 -> 0.303 gives
       `3 failed`.
judge  **AND THE SAME TEST KEEPS THE S355 COMPARISON AT THE SAME D/t, one variable moved**
       (test:315-321), so a reader sees which half governs where. That is the right shape.
       **No finding.** The one thing I would add is in the closure list: the plan row says
       "the hand calculation takes it at S690" and the plan's own Â§ 0 locks F_y = 355 MPa,
       so the two should name each other explicitly rather than leaving a reader to
       reconcile them.
```

**And the third measured point -- the pure-compression counter-case on the elastic branch --
is right for the reason given.** `F_a` and `F_e'` are the same expression there, so
`F_a/F_e' = 1.000000` and `u_axial = 1` is the singularity of the amplification. I verified
`f_a_allow / euler_stress(121.5, E) == 1.0` exactly and `0.5505390764073391` at `60.8`, and
the test asserts both rather than asserting the conclusion. Taking it on the inelastic
branch is the clause's answer, not the test's.

## 5. THE ADVERSARIAL CASE (EU1) -- what I ran at configurations the diff did not choose

Tolerance values moved, so EU1 fires. Seven probes, none of them chosen by the diff. Four
found something.

```
1  EVERY NUMERIC LITERAL ON A CODE LINE, perturbed 1% one at a time, rung 5 re-run after
   each, source restored byte-identical. 56 literals, 30 killed, 4 survived.
   -> R749. Two of the four are the numbers R742 was about.
2  432 ADMISSIBLE AMPLIFIED-GOVERNING CONFIGURATIONS instead of the two the diff chose.
   266 of 350 live responses at or below the declared counter; weakest 267x below; 82
   respond exactly 0.0.  -> R750, and it is R694's shape.
3  A DENSE 97681-POINT SWEEP of the clause module's admissible domain, module against a
   hand side I wrote rather than the test's. Clean worst 6.515863e-16 at F_y = 355,
   D/t = 113.43, KL/r = 108.1, against the declared 1.683679572698748e-16.  -> R750.
4  THE PUBLISHED DELIVERABLE AGAINST ITS OWN PUBLISHED CSV, four sentences at a time.
   -> R747, and the first of the four is R739's own subject.
5  THE FOUR SAG SITES, mutated separately on a fixture reaching both planes.
   -> nothing. R744 is answered.
6  THE 1 mm PRESCRIBED STRETCH, re-run independently. end_a[0] = -5.51010219e+06.
   -> R751, in the docstring rather than in the arithmetic.
7  REVERTING R739's TWO NEGATION LINES. `_station_values` returns at exit 0 and nothing
   under `tests/` imports the module, so the revert is invisible to all 3358 tests.
   -> closure item C52; the two sag planes carry a refusal and the axial line does not.
```

**And two things that did NOT break, recorded because an absence is a measurement.** Both
halves of Â§ 3.3.2's `max` are live -- dropping either reddens -- so the two amplified points
are doing work. And `allowable_bending`'s cap cannot be removed silently: disabling
`if f_b > cap` gives `3 failed`, which is R742's repair carrying its own failure, the
property R744 was the absence of.

## Closure items

Named with their site and what would close each. The implementer fixes the whole list once,
in the step's closure commit; they are not re-reviewed item by item and the step is not held
on one. Verdict 110's list ended at C49, so this one starts at C50. **C41 to C49 remain
open and are not re-adjudicated here.**

* **C50.** `docs/F6_utilisation.md:14` and `scripts/measure/api_wsd_utilisation.py`'s MID
  label: "the MID column waits on R730's discharge". Verdict 110 ruled R730/R734 discharged
  and named R736 as the live reason; the label gives R736's substance ("a measured 4.0%
  approximation on bending, unverified against a refined mesh") under R730's number, so a
  reader tracing the exclusion arrives at a closed item. The hand-back says the exclusion
  now rests on R736; the published label does not. **Closed when** the label names R736.
* **C51.** `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:573`.
  `assert_close(one_plane, two_planes, ...)` is module against module -- an invariance
  assertion, not a hand calculation. It is hand-pinned two lines later through `summed`, so
  the claim in the file docstring survives; the first assertion on its own does not. **Closed
  when** the docstring notes which assertions are invariances rather than hand values, or
  the magnitude is asserted against `summed / sqrt(2)` directly.
* **C52.** `scripts/measure/member_forces_table.py:433`. The axial negation has no control
  beside it, where the two sag planes each have one. Measured: replacing both lines with
  `pass` leaves `_station_values` at exit 0, and `grep -rl member_forces_table tests/`
  returns only two corpus data files, so the revert is invisible to all 3358 tests. **Closed
  when** the sign of the published `N` is refused the way the sag signs are -- one
  `copysign` comparison against a prescribed-sense reference -- or the absence is recorded
  as accepted with the reason.
* **C53.** `scripts/measure/member_forces_table.py:493`. The repaired guard skips when
  `applied == 0.0`, and the subject is now a difference rather than a product, so a sag
  below half an ULP of the chord mean is skipped where the old subject could only be zero if
  the load was. The ratio needed is about `1e16` and no shipped row is near it. **Closed
  when** the skip reads the load alone, as it did before, with the difference asserted
  nonzero rather than used as the skip condition.
* **C54.** `docs/milestones/F6.md` Â§ 3a's `F6_API_CLAUSE_AGREEMENT_COUNTER` row says "the
  hand calculation takes it at S690" while Â§ 0 locks `F_y = 355 MPa`. Both are right and
  neither names the other. **Closed when** the Â§ 3a row cites Â§ 0's lock and says why the
  one assertion departs from it.
* **C55.** `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:748`.
  `_quantities`' docstring says the 32 points are "the domain of the ceiling" and warns that
  "a family measured on a narrower domain than the ceiling it defends reports the strongest
  member as the quantity's". The warning is correct and applies to this file: the ceiling
  defends a module in `__all__` that accepts every `D/t` up to 300 at every grade. **Closed
  when** R750's repair lands and the sentence is restated against the domain that results.
* **C56.** `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:370` and the file
  docstring's "either side of every boundary": the tension/compression switch is exercised on
  both sides but not bracketed at it, and `in_tension >= 0.0 -> > 0.0` leaves 65 green.
  Harmless today -- the two differ only at exactly zero -- but the docstring names the switch
  as one of the bracketed boundaries. **Closed when** the claim is narrowed or a point sits
  at `axial_n = 0.0` and `-0.0`.
* **C57.** `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py:623` and `:820`
  import `CM_JOINT_TRANSLATION` into the hand side, so the VALUE is pinned by the single
  exact assert at `:677` and by nothing else -- the hand arithmetic cannot see it. The assert
  exists and kills a 1% edit, so this is a note about where the warrant lives, not a gap.
  **Closed when** the two hand sides write `0.85` out, as they do for every other
  coefficient.
* **R735, R736, R738, C34 to C40, and the `0.2240`/`0.2239` item** -- still open from verdict
  109, carried in `docs/closure/F4.md:147`, not re-adjudicated. R735's third site and the
  published label the report's Â§ 8 greps are part of that list.
* **R712 to R717, C2 to C15, C24 to C33, C41 to C49** -- still open, carried, not re-reviewed
  item by item, per CZ0.

## Tolerances touched

```
cmd    git diff 2cf33b0..HEAD -- floatfea/tolerances.py | grep -E "^\+[A-Z0-9_]+: Final"
out    +F6_API_CLAUSE_AGREEMENT: Final[float] = 1.0e-14
out    +F6_API_CLAUSE_AGREEMENT_COUNTER: Final[float] = 8.0e-13
out    +F6_API_CLAUSE_INJECTION_EPS: Final[float] = 1.0e-12
out    +F6_API_UTILISATION_COUNTER_FACTOR: Final[float] = 1.1
cmd    git diff 2cf33b0..HEAD -- floatfea/tolerances.py | grep -cE "^-[^-]"
out    1    the single line `# (no entries yet -- F6/F7)`
judge  **FOUR NEW ENTRIES, NOTHING EXISTING MOVED, NOTHING WIDENED.** All four are declared
       under the "Rung 5 -- Independent confirmation" header and the gate is now in rung 5,
       which `1f8f61a` fixed. EU1 fires and Â§ 5 is the adversarial case.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F6_API_CLAUSE_AGREEMENT` | -- | `1.0e-14` | dimensionless, RELATIVE | `F6_API_CLAUSE_AGREEMENT_COUNTER` | `floatfea/tolerances.py` entry, window rule; `docs/milestones/F6.md` Â§ 3a | **FORM ADMISSIBLE, THE DECLARED WINDOW IS NOT. R750.** Relative and dimensionless, correctly; an exactness tolerance at a small multiple of round-off with the measurements recorded, correctly; and the ubuntu run at `1f8f61a` is the independent-platform measurement the argument needed. What is wrong is the lower edge: `59.3937x` is the edge over the 32 chosen points, `15.35x` is the edge over the domain the ceiling defends, at `F_y = 355`, `D/t = 113.43`, `KL/r = 108.1`. Still above `F4_WINDOW_RULE_MIN_EDGE = 2.0`, so the VALUE stands; the published edge does not. |
| `F6_API_CLAUSE_AGREEMENT_COUNTER` | -- | `8.0e-13` | dimensionless, a floor beneath the family response | n/a, it IS the counter (AO2) | same entry | **BLOCKED, R750.** A constant at `1.0355x` below a response measured at one of two chosen points, where 266 of 350 live amplified-governing configurations sit at or below it and the weakest is `3.098618e-15`. The resolution has a closed form; the declared `0.828392` is that function at the strong end. EH4's weakening direction -- the minimum over points -- is never formed in the file. |
| `F6_API_CLAUSE_INJECTION_EPS` | -- | `1.0e-12` | dimensionless, STRUCTURAL, an input to a counter-case | none, correctly (AO2) | same entry | **ADMISSIBLE, and solved in both directions as the entry claims.** I reproduced the linearity: the response scales with it, so it may fall to `1.207158e-14` before `C_m`'s response at the chosen point reaches the ceiling. The reason given -- that a real transcription error is percent-scale and this measures non-vacuity -- is right, and my mutation sweep is the evidence (a 1% edit gives `1 failed` to `7 failed`, ten decades over). Its consequence is R750's, not its own. |
| `F6_API_UTILISATION_COUNTER_FACTOR` | -- | `1.1` | dimensionless, STRUCTURAL, a load multiplier | none, correctly (AO2) | same entry | **ADMISSIBLE, and the entry's hardest claim is true.** All six channels reach exactly `1.0` by a closed form, redden at `1.1x`, `governing` names the injected clause in all six, and neither branch moves under the injection -- which the test asserts rather than states. The elastic-branch exclusion is a property of the clause (`F_a/F_e' = 1.000000` exactly, verified) and not of the test, and the test asserts the ratio rather than the conclusion. |
| everything in the F4 block and earlier | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 110 (`2cf33b0`, judging `0b9ea0d`) was a **HOLD** carrying eight names and a closure
list. Every one, with status.

* **R739 (blocking) -- ANSWERED IN SUBSTANCE, TWO NAMED SITES STILL OPEN.** The negation is
  at the publishing boundary (`scripts/measure/member_forces_table.py:433`), the derivation
  is recorded there, both tables are regenerated in the same commit, and `F_a = 73.19` /
  `161.08` and the 2/2 clause split are published. The sense is read once, from
  `docs/conventions.md:320`. **Two residues, each blocking under its own number:**
  `floatfea/post/member_forces.py:23` is still inverted and Â§ 8a records it as correct
  (**R751**), and the published summary still says all four over-unity rows are Â§ 3.3.1
  (**R747**). The 1 mm cell is recorded in the source comment rather than in the report;
  that half of the condition I let stand, because the measurement is where the fix is.
* **R740 (blocking) -- CLOSED.** `total_instant` rows exist, one per station, on EZ2's
  governing basis, with a refusal if any station lacks a governing-basis peak; the filter
  reads only those; the label states which quantity the column is and why the envelope is
  not used. `U = 1.71167` against the old `1.81496` is published. The "ONLY WITHIN THE
  GOVERNING BASIS" note -- that tracking the global peak emitted 2 rows instead of 32 -- is
  the kind of self-reported near-miss that makes the rest believable.
* **R741 (blocking) -- CLOSED.** `local_buckling_stress` implements Â§ 3.2.2(b),
  `allowable_axial_compression` takes `D` and `t`, refuses above `D/t = 300`, reports
  `*_local` branches, and the refusal is exercised. `C_c` is recomputed from `F_xc`, which
  is the clause's own substitution. My mutation sweep confirms both the limit and the
  coefficient are live.
* **R742 (blocking) -- CLOSED, by option (i).** The limits stay at `10340`/`20680`, the
  modulus the clause's limits were derived at is stated, and the reduced branch is capped at
  `0.75 F_y`. The sweep test asserts `checked > 7000` so a narrowed domain fails loudly, and
  the cap carries its own failure: disabling it gives `3 failed`. **The residue is R749** --
  the cap is now what the first boundary's correctness rests on, and the boundary's own
  location is unpinned.
* **R743 (blocking) -- CLOSED.** Renamed `CM_JOINT_TRANSLATION`, category Â§ 3.3.1 case (a),
  direction stated as measured, `C_m = 1.0` column published, and the direction asserted at
  an amplified-governing point rather than a vacuous one. **My own `5.3x` ranking is
  WITHDRAWN**: on the shipped basis `K` is the larger lever by `3.7x`.
* **R744 (blocking) -- CLOSED, measured at all four sites.** Â§ 3 above. The report's account
  of the two ways its first cell was wrong -- reading the repaired source back after the
  HEAD loop had overwritten it, and writing outside the repository so the unperturbed
  control failed -- is the most useful paragraph in the revision, and both tells it names
  were the right tells.
* **R745 (blocking) -- CLOSED.** `Answers: verdict 110 @ 2cf33b0`, `step-1-answers.json`
  committed, `## 0` and `## 0a` generated, the whole-suite line present, the five sections
  sourced, and the eight-red trace pasted and checkable. I verified the trace by name in CI
  and verified the clearing by my own full run at `dd90505`: 3358 passed.
* **R746 (blocking) -- CLOSED.** The header names verdict 110, the `Carried` table is the
  generator's, R731 and R732 are marked answered-by-109 rather than carried, and R737 is
  named with a decision.
* **R737 (blocking, carried from verdict 109) -- CLOSED, and my framing was the loose half.**
  Â§ 3 above.
* **R735, R736, R738, C34 to C40, the `0.2240`/`0.2239` item, R712 to R717, C2 to C15,
  C24 to C33, C41 to C49 (closure) -- STILL OPEN**, carried as a list, not re-adjudicated.
  C46 -- the guard that was failing false on its own fixture -- is green in my run, so it
  was either fixed or it was conditional; it stays on the list until the closure commit says
  which. R735's third site and the published label the report's Â§ 8 greps belong to that
  list too.
* **THE MID EXCLUSION -- correctly excluded, wrongly attributed.** The hand-back says it now
  rests on R736; the published label still says R730. C50.
* **THE SCHEDULE -- and this is the escalation verdict 110 said would be due.** The report
  states the 22 October working target, the 28 October committed date, and that the target
  holds. Step 1 is two rounds in and carries five blocking items into round three. Four of
  the five are a string, a regeneration, two exact equalities and a sentence; the fifth
  (R750) is a derivation the implementer has already done once and has to redo at the weak
  end. **None of them needs a FloatSim run and none needs new apparatus.** On today's
  evidence the 22 October working target still holds and I would not slip it yet. If round 3
  closes still carrying any of R747 to R751, the choice -- slip the date or reduce scope --
  has to be stated with a number beside it rather than restated.

## The adversarial corpus (BE3)

**BATCH 43, committed separately at `a0482e2`:
`tests/corpus/f6_g61_gate_reach_and_the_counter_at_other_configurations.txt`, 29 entries,
every one new this round and none of them read by the implementer.**

EG4(e)'s pause to 28 October permits it and the file header claims the exception explicitly:
the surface is F4's load-mapping gate -- the `N` column, the generator that writes it, and
the clause module that reads it and branches on its sign. The clause-boundary entries are on
the same surface one step downstream: a `D/t` limit one digit wrong picks a different
allowable for the same member force.

**COVERAGE: the shipped checks catch 8 of 29.**

```
cmd    grep "^id=" <the file> | grep -c "expect=catch"
out    8
cmd    grep "^id=" <the file> | grep -c "expect=miss"
out    21
cmd    python -m pytest -q -p no:randomly <the 10 files that read tests/corpus>
out    1765 passed, 2 warnings in 377.84s
```

Against the last five rounds -- 1 of 16, 9 of 21, 4 of 11, 8 of 13, 5 of 22 -- this is the
second highest, and the reason is the thing that changed: **last round the surface had no
gate at all and now it has one.** All eight catches are in the clause module, and every one
of them is a mutation G6.1 kills. Batch 42's five catches were all controls.

**And the number that matters more than 8 of 29 is 30 of 34.** Of the thirty-four
executable-line literals and expressions I mutated in `floatfea/checks/api_wsd.py`, G6.1
kills thirty. The four it does not are R749, and two of them are the numbers the previous
round's finding was about. That is the measurement on FB0's ordering: the gate was worth
building, it works, and the holes in it are at the boundaries rather than in the arithmetic.

## On the criterion -- I was asked, and I agree with it, and I used its carve-out twice

CZ0 as amended by EZ0 is right and I applied it. Of my five findings, three are squarely in
(a), (b) or (c) without argument: R749 is a gate assertion, R750 is a counter value and the
form of one, R747 is a defect in a published deliverable and in the `scripts/measure/`
generator named in EZ0's own definition.

**Two needed the carve-out and I am naming both rather than smuggling them.** R748 and R751
are sentences. R748 blocks because the sentence IS the deliverable's warrant and its cited
path contains nothing -- "every citation resolves" is a recorded guard and this is its
shape. R751 blocks because it is the only statement in `floatfea/` of a convention a
published column's sign now depends on, and because it is a named site of R739's closing
condition that the report recorded as answered on a claim one command refutes. **If Xabier
reads the criterion more narrowly, both become closure items and the other three findings
hold the step on their own.** I would rather be told the line is in the wrong place than
guess at it.

**Nothing in this verdict is held against a figure in a report.** Eight prose items went
into the closure list, including C50 and C54, which under the retired head would each have
been a finding and would each have moved nothing. **And I want to record what the mutation
sweep bought, because it is the first time this project has had one.** Four of my five
findings came from running something the diff did not choose, and three of the four came
from two loops that each took under a minute per case -- a per-literal mutation of one
module, and the same model at 432 configurations instead of 2. The diff read nothing like as
well. `grep` over a diff finds a changed line; it cannot find a line that should have
changed, and it cannot find a constant that is right at the point its author picked.

## Next step opens when

**STEP 1 STAYS OPEN. THIS WAS ROUND 2 OF THREE AND ONE REVIEWED REVISION REMAINS.** After
the third revision the step closes under CZ0 whatever its state, and any blocking item still
open carries by name into step 2 and stays blocking there. In order, cheapest first:

1. **R748 is answered** -- the four citations read `tests/verification/rung5/`, and
   `docs/F6_utilisation.csv` and `docs/F6_utilisation.md` are regenerated in the same commit
   (BP0), with `ls tests/verification/rung5/` pasted. One string and one run.
2. **R747 is answered in that same commit, because it is the same regeneration** -- the four
   summary sentences are generated from the sets they describe or deleted. My figures to
   beat: the 2/2 split between Â§ 3.3.1 and Â§ 3.3.2 on the four over-unity rows, `0.034238`,
   `u_bending = 1.71138` at `platform:hub2_arm` ROOT, and the amplified form governing on
   `10 of 17` compression rows. If the regeneration disagrees with those I want the
   disagreement rather than a reconciliation.
3. **R751 is answered** -- one clause in `floatfea/post/member_forces.py:23`, the 1 mm cell
   beside it, and Â§ 8a's row corrected. `end_a[0] = -5.51010219e+06` for a stretch where
   `EA/L x 1e-3 = +5.51010219e+06` is the measurement, and it is the same one verdict 110
   took.
4. **R749 is answered** -- `limit_1` and `limit_2` are pinned the way `limit_3` already is,
   or a point sits inside each boundary's own neighbourhood, and the `300` refusal is
   bracketed the way `LOCAL_BUCKLING_DT` is at `60`/`60.5`. Re-run `10340 -> 10430`,
   `20680 -> 20860` and `300 -> 303` and paste both outcomes for each. Three assertions
   inside a file the step already shipped; no new apparatus.
5. **R750 is answered** -- the counter is a floor beneath every admissible configuration
   rather than a constant at one, the window entry states the edge over the domain the
   ceiling defends, and EH4's weakening direction is taken at least once. `3.098618e-15`,
   `266 of 350`, `82 of 432` and `6.515863e-16 at (355 MPa, 113.43, 108.1)` are my figures.
6. **The closure list C50 to C57** goes in the step's closure commit, where CZ0 puts it, and
   C45 still needs its own standalone `process:` commit. CZ1 applies to that commit and EQ0
   applies if it moves a gate or a tolerance -- which, if R749 and R750 are answered in it
   rather than in the revision, it will.

**What I will not accept at revision 3.** A deliverable whose summary paragraph still
contradicts the table above it, because that is R739's own subject for the second round
running and it is the paragraph a reader reaches last. A G6.1 warrant citing a directory CI
declares empty. A branch limit that a digit swap leaves green, when the file already
contains the exact assertion that would catch it and applies it to one limit of three. A
counter whose declared basis is the strongest member of its family when the rule it is
declared under asks for a floor beneath the weakest. And a sentence in `floatfea/` that
says the opposite of what a prescribed-sense measurement says, two rounds after that
measurement was first taken. The question for all five is the recorded one: if the thing
this claim asserts were false, would anything go red. For R749 and R750 I measured the
answer and it is no.

**And one thing on the record for the implementer rather than against them.** This revision
built the step's locked content from nothing in one round, and the gate it built is real: I
mutated thirty-four things in the module and it killed thirty. It found and reported three
vacuous counter-cases that nobody asked it about, it reported its own first cell being wrong
in two ways before I could find it, it reported the rung placement before I could find that
either, and it corrected my framing of R737 with a command. Four of the eight items verdict
110 raised are closed outright and two more are closed in substance. **The pattern in what
remains is one thing, and it is worth saying plainly: every one of the five is at a boundary
or in a sentence, and none is in the arithmetic.** The clause transcription is correct --
I checked thirty coefficients by mutation this round after checking eight by hand last
round. What keeps going wrong is the edge of the domain and the prose a reader reads
instead of the table. Those are the two places a correct calculation gets published wrong,
and the fix for both is the same one: generate the sentence from the set, and bracket the
boundary at the boundary.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F6 step 1
Reviewed commit: 517f8e201a1860142277d155b03b221458f482bb
Verdict: HOLD
**Reviewed commit: `0b9ea0d`** (`0b9ea0dd5cec0a6382c26fafae31be6f488a7d0b`, tree clean when
I judged it; my corpus batch 42 is committed on top at `517f8e2`, which is why the plain
`Reviewed commit:` stamp above is not the commit I judged -- R718's subject, and this bold
line is the mechanism.)
Tests: 3125 passed, 43 failed, 1 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `0b9ea0d`, `589.90s`. The
report states no suite count at all, so there is no figure of its to compare with.)

## Round of 2026-10-09 -- ROUND 1 OF THREE, F6 step 1. **HOLD.** Eight blocking items -- six on the code and the deliverable, two on a red suite and a red CI -- and the one that matters is a sign.

**WHY HOLD, IN FIVE SENTENCES.** I was asked to check the six clauses' coefficients
independently and I did: `10340`/`20680` with `F_y` in MPa, `0.5 A` beam shear,
`W_t = 2J/D`, `C_m` as a declared input, the `3.3.2` max-of-two, `C_c`, the `F_e'`
expression and the `3.2.2` branch boundary are **all correct**, and the branch boundary is
continuous to the fifteenth digit. **What is wrong is upstream of all of them: the column
the check reads publishes compression as positive, and `check_member` reads it as
tension.** Measured from a displacement whose sense cannot be argued with -- a member
stretched 1 mm publishes `N = -5510102.18698421` at both stations -- against
`docs/conventions.md:320`, which locks tension positive. Every `axial branch`, every `F_a`,
every `u_axial` and every `governing_clause` in `docs/F6_utilisation.csv` and
`docs/F6_utilisation.md` is wrong on every row; the four over-unity rows are Â§ 3.3.2 and not
Â§ 3.3.1; `F_a` is published as `213.00 MPa` -- the exact figure the same file's FA1 label
calls superseded -- where the clause gives `73.25`; and the **FA2 headline `0.024114` that
the report uses to invert its own advice to Xabier about `K` becomes `0.151293`** once the
sign and `C_m` are each corrected one at a time. **The governing `U = 1.815` is also not the
quantity its label names**: it is the per-component envelope bound, where the per-instant
value is `1.7115`.

**No STOP.** No low rung is red: `the verification ladder` is SUCCESS in CI at the reviewed
commit, all six rungs, and every one of my 43 local reds is in three report-guard files.
The locked plan is not wrong -- on the contrary, Â§ 3 item 2 of it is one of the things the
code does not do -- so nothing needs reopening.

**AND THE STEP IS OUT OF SCOPE AGAINST ITS OWN LOCKED PLAN, which I rule on rather than
block on.** `docs/milestones/F6.md` Â§ 3 is step 1 and it is the six clauses *plus* G6.1's
documented hand calculations *plus* a counter-case per check. Â§ 4 is step 2 and it is
`scripts/measure/`, the utilisation table and the top ten. This commit shipped Â§ 4's
deliverable and none of Â§ 3's gate, which is the two halves of the plan swapped. FA3
directed the send, so I am not treating it as a silent adaptation -- but the consequence is
exactly what CZ0 (a) was amended for: **a utilisation table a structural engineer sizes
steel against went to Xabier with no gate, no counter-case, no tolerance and nothing under
`tests/` reading either new file.** `grep -rl api_wsd tests/` is empty. Six of my eight
findings are things G6.1 would have caught, and that is the measurement on the ordering, not
an opinion about it. See Â§ *On FA3 versus G6.1* -- that one goes to Xabier.

## 0. CI AT THE REVIEWED COMMIT -- RED, AND THE LADDER IS THE HALF THAT IS GREEN

```
cmd    gh run list --commit 0b9ea0dd5cec0a6382c26fafae31be6f488a7d0b --json databaseId,conclusion,status
out    [{"conclusion":"failure","databaseId":37883813296,"status":"completed"}]
cmd    gh run view 37883813296 --json jobs -q '.jobs[] | "\(.name)\t\(.conclusion)"'
out    lint, unit and guards              failure    (11m26s)
out    the verification ladder            success    (3m34s)
out    CI determinism -- leg              skipped
out    CI determinism -- ten legs agree   skipped
cmd    gh run view 37883813296 --json jobs   (step level, the failing job)
out    1..9  checkout / setup / install / actionlint / ruff / black --check / mypy /
out          unit tests                                              all success
out    10    guards and meta-tests                                   FAILURE
judge  **CA2: A RED CI IS A HOLD REGARDLESS OF WHAT THE LOCAL RUN SAYS, and here the local
       run agrees.** This is not CK2: the jobs ran on a real runner for eleven minutes,
       there is no payment annotation and no two-second zero-step job. It is not CA2's
       unavailable state either -- the run completed at the reviewed commit's own sha.
       `guards and meta-tests` is the step that fails, which is the same family as my 43,
       and `the verification ladder` passing is why this is a HOLD and not a STOP.
```

## 1. MY OWN INSTRUCTIONS, THE CONFTEST AND THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
cmd    git diff cdbbf79..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
judge  CH2/CI0: the one conftest in the tree is untouched in this range, so no rung's
       green is forged from its own directory and I did not have to read a hookwrapper.
cmd    git diff cdbbf79..HEAD -- floatfea/tolerances.py
out    (empty)
judge  NOT ONE VALUE, COUNTER, FORM OR COMMENT MOVED. EU1 does not fire on this diff -- and
       I ran the adversarial case anyway, at every `D/t` and `KL/r` boundary the clause
       module has, because the diff introduced two decision rules with no tolerance behind
       them at all. That is what found R742.
cmd    git diff --stat cdbbf79..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 6 ++++--
cmd    git log --oneline cdbbf79..HEAD -- docs/SUPERVISOR.md
out    767fb86 process: EZ0 -- CZ0 (a) gains "or in a published deliverable"
cmd    git show --stat 767fb86
out    CLAUDE.md | 15 ++++++++++++++-     docs/SUPERVISOR.md | 6 ++++--
judge  **CORRECT AND CLEAN.** A standalone `process:` commit citing EZ0 by name, touching
       nothing under `floatfea/`, `tests/` or `scripts/`. I read the diff line by line: it
       is purely additive, it deletes no guard, and the amended head and its definition
       are byte-identical with `CLAUDE.md`'s. `.claude/agents/gating-supervisor.md` is
       untouched -- which is itself a problem, and it is C45 below rather than a finding,
       because the file that governs what I read now disagrees with the two files that
       say it is the single home of the list.
```

## 2. THE SIX CLAUSES, CHECKED AGAINST THE STANDARD INDEPENDENTLY -- WHAT IS RIGHT

The hand-back asked for this specifically and named three of the four things it was least
sure of. I re-derived each from the clause rather than from the module, and from the US
forms and their conversion rather than from the SI numbers the module carries.

```
rule   API RP 2A-WSD section 3.2.3: the US branch limits are `1500/F_y` and `3000/F_y` with
       `F_y` in ksi; `1 ksi = 6.894757 MPa`
out    1500 x 6.894757 = 10342.1    3000 x 6.894757 = 20684.3
out    the module carries 10340 and 20680, which is the standard's own SI rounding
out    10340/355 = 29.1268    20680/355 = 58.2535    D/t shipped = 13.8889
judge  **THE CONVERSION IS RIGHT AND IT IS DONE IN ONE PLACE** (`PASCAL_PER_MPA`, read only
       at `:101`). The 145x risk the module's docstring names is real and is not realised.
rule   section 3.2.4(a): the beam shear stress for a cylinder is `V / (0.5 A)`, `F_v = 0.4 F_y`
out    `V/(0.5 A)` is `2 V/A`, so using `A` reads 2x LOW -- the direction the comment claims
judge  CORRECT, including the direction, which is the half a comment usually gets wrong.
rule   section 3.2.4(b): `f_vt = M_t D / (2 I_p)`, `F_vt = 0.4 F_y`
out    `M_t D / (2 I_p)` is `M_t / (2 J / D)`, and the script passes `2 J / D`
judge  CORRECT.
rule   section 3.3.2 requires BOTH (3.3.2-1) with the `C_m/(1 - f_a/F_e')` amplification AND
       (3.3.2-2) `f_a/(0.6 F_y) + f_b/F_b`, and permits the single in-lieu form only at
       `f_a/F_a <= 0.15`
out    the module evaluates both and takes `max`, and omits the in-lieu relaxation
judge  **CORRECT AND CONSERVATIVE IN THE RIGHT DIRECTION.** `max` of two utilisations is
       the right expression of "both must be <= 1", and dropping a permission cannot
       under-report. `F_e' = 12 pi^2 E / (23 (KL/r)^2)` is the same expression as the
       elastic `F_a`, which is why the report's two `73.25` lines agree -- that is the
       standard, not a copy-paste.
rule   section 3.2.2: inelastic below `C_c`, elastic at and above, `C_c = sqrt(2 pi^2 E/F_y)`
out    C_c                                   = 108.05885001274791
out    inelastic form as the ratio -> 1      = 92608695.65217389 Pa
out    elastic form at KL/r = C_c            = 92608695.65217392 Pa
out    KL/r = C_c - 1e-12                    -> inelastic;  = C_c -> elastic
judge  **CONTINUOUS TO THE FIFTEENTH DIGIT AND THE `>=` IS ON THE CORRECT SIDE.** `12/46`
       is identically the inelastic limit, so the whole safety-factor polynomial
       `5/3 + 3x/8 - x^3/8` is transcribed right. This was the coefficient the hand-back
       was least sure of and it is correct.
```

**So four of the five things I was asked to attack in Â§ 1 of the hand-back hold.** The
fifth, `C_m = 0.85`, does not, and it does not for a reason the module states backwards --
R743.

## Findings

**R739. (BLOCKING. (a) AS AMENDED BY EZ0, AND ALSO (a) ON THE UNAMENDED HEAD, BECAUSE THE
DEFECT IS IN `floatfea/`.) THE PUBLISHED `N` COLUMN IS COMPRESSION-POSITIVE AND
`check_member` READS IT AS TENSION-POSITIVE. 128 OF 256 ROWS ARE CLASSIFIED IN THE WRONG
SENSE, AND SO IS EVERY ROW OF BOTH PUBLISHED TABLES.**
`floatfea/checks/api_wsd.py:254` (`in_tension = axial_n >= 0.0`),
`scripts/measure/api_wsd_utilisation.py:138` (`axial_n=float(r["N"])`), against
`docs/conventions.md:320`. Published in `docs/F6_utilisation.csv` (`axial_branch`,
`F_a_MPa`, `u_axial`, `governing_clause`) and `docs/F6_utilisation.md`.

```
claim  a positive `N` in docs/F4_member_forces.csv is a tension force
cmd    move node_b of platform:hub1_arm OUTWARD along the member axis by 1 mm -- an
       unambiguous stretch -- and read what member_forces publishes at each station
rule   docs/conventions.md:320, locked at F0: "Positive axial force: tension positive."
out    end_a = [-5510102.187, 0, 0, 0, 0, 0]      end_b = [+5510102.187, 0, 0, 0, 0, 0]
out    EA/L x 1e-3 (the true internal N, tension positive) = +5510102.18698421
out    published ROOT N  =  end_a[0] = -5510102.18698421
out    published TIP  N  = -end_b[0] = -5510102.18698421
judge  **BOTH STATIONS PUBLISH COMPRESSION-POSITIVE.** `k_local @ (t @ u)` is the force the
       NODES exert on the ELEMENT, not the force the element exerts on the nodes, and the
       module's own equilibrium note confirms the sense: `Vz_A + Vz_B` equals the member's
       weight `+1532812.5 N`, which only holds for forces applied TO the element.
```

**THE REACH, each cell with one variable moved and everything else held -- same CSV, same
filter, same section, same `C_m`:**

```
rule   the shipped decision rule, `in_tension = axial_n >= 0.0`, against the same rule
       reading `-axial_n`
out    branch assignment    : 128 rows published `tension` are in COMPRESSION, and all 128
out                           published `elastic`/`inelastic` are in TENSION
out    branch HISTOGRAM     : elastic 32; inelastic 96; tension 128 -- IDENTICAL EITHER WAY
out    governing clause     : all four over-unity rows go 3.3.1 -> 3.3.2; all ten published
out                           top-ten rows read `3.3.1 interaction`
out    F_a on the 4 platform ROOTs : published 213.00 MPa, clause gives 73.25 MPa (elastic
out                           at KL/r = 121.5) -- u_axial low by 2.9079x
out    F_a on the hub ROOTs : published 213.00 MPa, clause gives 161.02 MPa (inelastic at
out                           60.8) -- u_axial low by 1.3228x
out    u_axial, worst station : 0.000358 published, 0.001043 corrected
out    u_axial, platform:hub1_arm ROOT : 0.033966 published, 0.098847 corrected
out    largest |U(K=2)-U(K=1)| : 0.024114 published, 0.034926 corrected
out    worst compression station : U = 1.70984 published, 1.81496 corrected -- the worst
out                           station in the whole table IS a compression station
judge  **THE HISTOGRAM BEING IDENTICAL IS WHY NOTHING LOOKED WRONG.** The split is 128/128
       because every station contributes one `total_max` row and one `total_min` row of
       opposite axial sign, so the one summary number a reader would sanity-check is
       invariant under the inversion. The report publishes that number as the FA2 answer.
```

**AND IT PUTS `213.00 MPa` BACK INTO A DELIVERABLE THAT SPENDS A LABEL SAYING IT IS
SUPERSEDED.** `docs/F6_utilisation.md:35`'s FA2 table publishes `F_a = 213.00` on all ten
rows; the same file's FA1 inheritance says the `213.0 MPa` generic `0.6 F_y` reference "is
SUPERSEDED by F6's API RP 2A-WSD clauses and it is NOT the API bending allowable". Both
sentences are in one published file and they contradict each other, and the reason is this
sign: with the sign corrected, no governing row's `F_a` is `0.6 F_y` at all.

**Closed when** the sign convention is stated once and read once: `docs/conventions.md:320`
is the authority, so either `member_forces` returns the internal action (and the five other
components are re-derived with it, not just negated) or the consumer negates at the one
boundary where it reads the CSV, with the convention named in `check_member`'s docstring and
in `MemberCheck.in_tension`; **plus** the two attribution sentences at
`floatfea/post/member_forces.py:23` and `scripts/measure/member_forces_table.py:415`
corrected, **plus** `docs/F6_utilisation.csv` and `docs/F6_utilisation.md` regenerated in
the same commit (BP0), **plus** the 1 mm prescribed-stretch cell above pasted as the
control -- it costs four lines, needs no npz, and is the one route that cannot share an
assumption with either file. My figures to beat are in the two blocks above.

**R740. (BLOCKING. (a) UNDER EZ0.) `U = 1.815` IS THE PER-COMPONENT ENVELOPE BOUND, THE
DELIVERABLE'S LABEL SAYS IT IS THE PER-INSTANT VALUE, AND IT IS NOT EXACTLY EITHER.**
`scripts/measure/api_wsd_utilisation.py:79-81` (the label), `:126` (the `total*` filter) and
`:209` (the max over rows), published at `docs/F6_utilisation.md:13` and in every row of
`docs/F6_utilisation.csv`.

```
claim  "The utilisations are computed from F4's PER-INSTANT stresses where available; the
       per-component envelope is an upper bound and is reported separately in F4's table."
cmd    the basis values F4's CSV actually carries, and which of them the filter keeps
out    dynamic_max 288   dynamic_min 288   static 48   total_max 288   total_min 288
out    the filter keeps `basis.startswith("total")`, i.e. total_max and total_min ONLY
out    F4's per-instant figure is computed in memory and published in docs/F4_member_forces.md
out      alone; THE CSV CARRIES NO PER-INSTANT ROW, so "where available" is nowhere
rule   docs/milestones/F6.md section 4: "Both of F4's stress columns carry through -- per-instant and
       envelope upper bound -- and the utilisation is computed from each, labelled.
       Collapsing them would be the one thing this milestone could do that makes F4's
       table less honest than it is."
out    platform:hub2_arm ROOT, T = 12.5 s:  per-instant 455.7 MPa   envelope 483.2 MPa
out    U from the envelope   = 1.81496   <- what is published
out    U from the per-instant = 455.7/266.25 = 1.7115
out    the gap, 0.103 in U, is 4.3x the K sensitivity the report leads with
judge  **AND IT IS NOT THE PER-COMPONENT BOUND EITHER.** The bending resultant is formed
       INSIDE each `total` row before the max over rows is taken, so a station whose `My`
       peaks on `total_max` and whose `Mz` peaks on `total_min` is published BELOW the true
       per-component bound. The published number is a third quantity -- the worse of two
       per-component rows -- and it has no stated provenance that is true.
```

**Closed when** the label states which quantity the column is, measured rather than
asserted, and the two columns Â§ 4 requires exist -- or, if the per-instant column genuinely
cannot be formed without re-running F4's driver, the label says exactly that and the one
number above (`1.81496` against `1.7115` at the governing station) is published beside it so
a reader knows the size of what is missing. The deliverable's own labels are the half of it
Xabier reads first.

**R741. (BLOCKING. (a), AND THE LOCKED PLAN REQUIRES IT IN ITS OWN WORDS.) Â§ 3.2.2's
LOCAL-BUCKLING CHECK IS NOT IMPLEMENTED AND A SLENDER SECTION IS NOT REFUSED -- IT PASSES
SILENTLY, WHICH IS THE EXACT PHRASE THE PLAN FORBIDS.**
`floatfea/checks/api_wsd.py:132-153` (`allowable_axial_compression`), against
`docs/milestones/F6.md` Â§ 3 item 2.

```
rule   docs/milestones/F6.md section 3 item 2, LOCKED: "D/t is checked against the
       local-buckling limit first, because beyond it the global check is not the binding
       one ... so local buckling does not govern *this* section and the check must still
       refuse rather than pass silently on one that is slender."
cmd    inspect.signature(allowable_axial_compression)
out    (k_l_over_r: float, fy: float = 355000000.0, e: float = 210000000000.0)
judge  it takes no `D` and no `t`, so it cannot check `D/t` at all.
cmd    allowable_axial_compression(80.0) with the section at D/t = 100
out    (136098611.12499207, 'inelastic')   -- no refusal, no reduction, no flag
rule   API RP 2A-WSD section 3.2.2(b): `F_xc = F_y` only for `D/t <= 60`; above it the local
       buckling stress replaces `F_y` in the column formula
cmd    grep -n "60|Fxc|local buckling" floatfea/checks/api_wsd.py
out    one comment line, at :97, and it is about `D/t = 300` in the BENDING clause
judge  **THE ONLY REFUSAL IN THE MODULE IS `allowable_bending`'s at `D/t > 300`, which is a
       different clause and a different limit.** A caller asking for the axial allowable
       alone -- which is the public API, it is in `__all__` -- gets a number computed on the
       full `F_y` at any slenderness. It is vacuous at the shipped `D/t = 13.8889`, which is
       precisely EU1's shape: the configuration the commit chose cannot see it.
```

**Closed when** `allowable_axial_compression` either implements Â§ 3.2.2(b) or refuses above
its limit, and the limit it uses is the clause's (`D/t = 60`) rather than the bending
clause's `300` -- with the refusal exercised, because a refusal nothing reaches is not a
refusal. `basis.chs_class_limits()` is named in the plan row and already exists.

**R742. (BLOCKING. (a).) `allowable_bending` RETURNS MORE THAN `0.75 F_y`, WHICH NO READING
OF Â§ 3.2.3 PERMITS, FOR `D/t` IN `(29.1268, 30.5974)`. THE CAUSE IS THAT `10340` ENCODES
`E = 200 GPa` AND THE MODULE COMPUTES WITH `E_STEEL = 210e9`.**
`floatfea/checks/api_wsd.py:102-103` (the limits) against `:174` (the first reduced branch),
and `floatfea/basis.py:46`.

```
claim  section 3.2.3's branches are monotone and capped at 0.75 F_y
cmd    allowable_bending at and just above the first branch limit
out    F_b at D/t = 29.1268            = 267.7855873914286 MPa
out    0.75 F_y                        = 266.25 MPa
out    ratio                           = 1.0057674643809524   (+1.5356 MPa)
out    the reduced_1 branch crosses 0.75 F_y at D/t = 30.59737736765419
cmd    the D/t at which [0.84 - 1.74 F_y D/(E t)] F_y equals 0.75 F_y
out    0.051724 x E / F_y = 30.597295774647886  -- the crossing, to five figures
out    0.051724 x 29000 ksi = 1500.0  -- which is the US form of the same limit
cmd    the second boundary, D/t = 58.2535
out    reduced_1 gives 237.37 MPa and reduced_2 gives 235.32 MPa -- a step DOWN of 0.87%
judge  **ONE CAUSE, TWO DISCONTINUITIES IN OPPOSITE DIRECTIONS, WHICH IS WHAT RULES OUT A
       TRANSCRIPTION SLIP IN ONE COEFFICIENT.** `1500/F_y[ksi]` is exactly the continuity
       point at `E = 29000 ksi = 199948 MPa`, and `10340/F_y[MPa]` is its conversion. The
       module runs at `210000 MPa`, 5.0% higher, so the branch limit sits 5.0% below the
       continuity point and the reduced branch pokes above the cap on the interval between
       them. Vacuous at `D/t = 13.8889` and not vacuous as a clause: the module is in
       `__all__` and is the one the next section will be checked with.
```

**Closed when** the module either (i) states the modulus the clause's own limits were derived
at, keeps `10340`/`20680`, and caps the reduced branch at `0.75 F_y` so the function cannot
return above the clause's own ceiling, or (ii) derives both limits from `E` so the branches
are continuous by construction -- with the chosen reading stated and the
`1.0057674643809524` above reproduced or refuted. **Not** by changing `E_STEEL`: that is a
locked material constant and this is a clause-transcription question.

**R743. (BLOCKING. (a).) `CM_NO_TRANSVERSE_LOAD = 0.85` IS DECLARED UNDER THE WRONG CLAUSE
CATEGORY AND ITS CONSERVATISM IS STATED BACKWARDS. MEASURED, IT IS A LARGER LEVER ON THE
GOVERNING NUMBER THAN `K` IS, AND THE REPORT'S HEADLINE SAYS `K` WAS THE LARGEST.**
`floatfea/checks/api_wsd.py:71-77`, published at `docs/F6_utilisation.md` in "The section and
the slenderness" as `C_m = 0.85` (Â§ 3.3.2, no transverse load -- a declared input).

```
claim  "0.85 is the conservative reading of a clause whose alternatives need an end-moment
       ratio the screen does not resolve"
rule   section 3.3.2's amplified form is f_a/F_a + C_m f_b / [(1 - f_a/F_e') F_b], so C_m
       MULTIPLIES the bending term: a smaller C_m gives a SMALLER utilisation
cmd    four cells, one variable each, same CSV, same filter, same section
out    shipped (C_m = 0.85, sign as shipped) : worst U 1.81496   largest |dU over K| 0.024114
out    sign fixed alone                      : worst U 1.81496   largest |dU over K| 0.034926
out    C_m = 1.0 alone                       : worst U 1.81496   largest |dU over K| 0.128855
out    both                                  : worst U 1.81754   largest |dU over K| 0.151293
out    platform:hub1_arm ROOT, both corrected: 1.18820 -> 1.37969
out    platform:hub3_arm ROOT, both corrected: 1.20215 -> 1.37951
judge  **"CONSERVATIVE" IS THE WRONG DIRECTION, MEASURED: C_m = 1.0 RAISES EVERY
       COMPRESSION UTILISATION.** And the category is wrong twice over. API's
       no-transverse-loading case is C_m = 0.6 - 0.4 M_1/M_2, not 0.85; 0.85 is the
       sidesway case, which is the reading K = 2.0 itself rests on ("no reliable lateral
       restraint"), and the docstring's own next sentence says these arms DO carry a
       distributed body force. So the constant is plausibly the right NUMBER under a
       category its name, its docstring and the deliverable's label all deny.
```

**This is the one place I disagree with the report's headline rather than with a number in
it.** The hand-back asked me to attack the claim that `K` is not the largest modelling
choice. It is not -- but on the report's own metric `C_m` moves the governing number
`5.3x` further than `K` does, and with both corrected the amplified form of Â§ 3.3.2 begins
to govern, which puts `K` back inside the number through `F_e'`. The conclusion "the axial
term contributes almost nothing" **survives** -- `u_axial = 0.001043` against
`u_bending = 1.81460` at the governing station -- and that half of the advice to Xabier is
sound. What does not survive is `0.024114` as the measure of how much the modelling choices
move the answer.

**Closed when** the constant is named for the category it is, the docstring states the
direction as measured (`C_m = 1.0` raises `U`, here from `1.18820` to `1.37969` at
`platform:hub1_arm` ROOT with the sign also corrected) rather than asserting conservatism,
the published label stops saying "no transverse load" in a deliverable whose own load basis
is a distributed body force, and the choice between API's sidesway category and its
transverse-loading-with-unrestrained-ends category is stated with its reason -- or `1.0` is
adopted. I am not ruling which; I am ruling that the three current statements of it cannot
all be true.

**R744. (BLOCKING. (c) -- ASSERTION DOMAIN BLINDNESS, AND IT IS THE CONTROL THAT ANSWERED
VERDICT 109's BLOCKING FINDING.) THE SAG-SIGN GUARD READS THE INTERMEDIATE AND NOT THE LINE
THAT SETS THE PUBLISHED VALUE. R734's EXACT DEFECT RETURNS ON A ONE-CHARACTER CHANGE WITH
THE GUARD SILENT.**
`scripts/measure/member_forces_table.py:446-449` (the two assignments) against `:452-462`
(the guard), published in `docs/F4_member_forces.csv`'s MID rows.

```
claim  "the check is a sign comparison and needs no constant. It catches exactly the defect
       that shipped, and it cannot be satisfied by a configuration that happens to sit at
       zero because it skips those."
cmd    three copies of the module, one variable moved in each, `_station_values` called on
       platform:hub1_arm with a uniform a_y = 3 m/s^2 so that w_local[1] is nonzero
rule   the guard at :452-462 compares copysign(sag_z) against copysign(want * load)
out    base                                  OK        mid Mz = +2.92968750e+06
out    `sag_z = +w_local[1]...` -> `-w_local[1]...`    REFUSED (the guard fires)
out    `mid[5] = mid[5] + sag_z` -> `- sag_z`          OK, SILENT, mid Mz = -1.46484375e+07
out    the fixture is not degenerate: w_local[1] = 28125.0, so the `load == 0: continue`
out      branch is not taken
judge  **THE GUARD RESTATES THE LINE ABOVE IT.** `sag_z` is assigned `+w_local[1] * span^2
       / 8` and the guard then asserts that `sag_z` has the sign of `+w_local[1]`, with
       `span^2/8 > 0` always -- so for the quantity that is PUBLISHED, `mid[5]`, the guard
       has no reach at all. The defect that shipped as R734 was a wrong sign on the
       published MID `Mz`; the repair split that one line into two, and the half the guard
       reads is not the half that publishes. One character, factor of 5 and a sign change,
       suite green.
```

**I am blocking on a guard, which CZ0 classes as a closure item, and I am naming that rather
than smuggling it.** My instructions' carve-out is for a closure item that touches (c), and
this is that: it is the ONLY check in the tree on the sign of a published column -- `grep
-rl member_forces_table tests/` is still empty -- so what it claims, on which quantity, is a
gate assertion in substance even though it is a runtime refusal in form. It is also the
third round running on the same two lines, and the reason it recurs is not carelessness: it
is that the repair's own control was written to the shape of the previous defect rather than
to the published quantity.

**Closed when** the comparison is on `mid[5]` -- the delta the station actually publishes,
against the sign of its own load component -- so that a flip in either half reddens, with
the mutation above re-run and both outcomes pasted. One expression, no new file, no
threshold, and no new apparatus.

**R745. (BLOCKING. (d).) 43 RED TESTS AT THE REVIEWED COMMIT AND A RED CI JOB, AND THE
EG3(i) TRACE IS NOT PASTED BECAUSE THE REPORT CARRIES NO TEST COUNT AT ALL. AT LEAST 16 OF
THE REDS ARE OUTSIDE BOTH OF EG3's LISTS AND ARE THE REPORT'S OWN MISSING SECTIONS.**
`docs/reports/F6/step-1.md` (the whole file), `docs/reports/F6/step-1-answers.json` (absent).

```
cmd    python -m pytest -q -p no:randomly   (my own run, tree clean at 0b9ea0d)
out    43 failed, 3125 passed, 1 skipped in 589.90s
out    by file: tests/test_report_carried.py 19; tests/test_report_guard_states.py 19;
out            tests/test_report_numbers_are_sourced.py 5
out    NOTHING under tests/verification, tests/unit or tests/regression is red
cmd    EG3(i)'s trace -- each FAILED id matched to state (1)'s own list
out    on the list    : test_the_guard_reads_the_step_being_worked_on
out    the cascade    : test_report_guard_states.py[baseline] is red and its own failure
out                     line pastes the test_report_carried.py reds, so the other 18 states
out                     cascade off it
out    OUTSIDE BOTH LISTS, each one an omission of the report itself:
out      test_the_report_names_the_verdict_it_answers   -- no `Answers: verdict <n> @ <sha>`
out      test_the_report_carries_a_WHOLE_SUITE_count    -- no suite count anywhere
out      test_the_report_carries_a_CI_SECTION           -- no CI section
out      test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW -- no 0a table
out      test_the_ROUNDS_SECTION_is_the_GENERATORS...   -- no 0a table
out      test_the_reported_CI_counts_are_not_all_zero   -- no CI rows
out      test_the_Carried_table_is_what_the_generator_produces  -- step-1-answers.json
out      test_the_generator_would_catch_a_row_under_the_wrong_number  -- same file absent
out      test_there_are_pointers_to_resolve             -- no Carried row names a section
out      test_a_report_does_not_say_CLOSED              -- no Carried table to parse
out      test_every_number_in_prose_is_sourced... x 5   -- sections 1, 2, 5, 6, 7
judge  **EG3's WAIVER IS CONDITIONAL ON THE TRACE AND THE TRACE IS NOT PASTED.** The report
       states no test count, so there is no claim for me to check and no "only those"
       sentence to hold it to. CZ1 (iv) is therefore unchanged for every red above.
```

**I MEASURED WHICH OF THEM MY OWN VERDICT CLEARS, because that is the half no verdict can
take after the fact.** In a detached worktree at `0b9ea0d` with a placeholder verdict
committed at `docs/reviews/F6/step-1.md`, the three files go from **43 red to 31 red**: 12
clear at the verdict commit, and the 31 that remain are the report's own omissions plus the
cascade plus state (2)'s named five. So writing this verdict does not fix it, and the
answering revision must.

**AND ONE PART OF THIS IS NOT THE REPORT'S FAULT AND GOES TO XABIER.** `VERDICT` resolves to
`docs/reviews/F6/step-{max(REVIEWED)}.md` and falls back to `step-0.md` when `REVIEWED` is
empty (`tests/test_report_carried.py:211`). At the **first step of a new milestone** that
directory is empty, so a dozen assertions are keyed on a file that cannot exist yet. This is
EG3's boundary one level up -- a MILESTONE boundary rather than a step boundary -- and
EG3's two lists do not name it. I am not asking for new apparatus; the fix is a third state
in EG3's list, which is prose in `CLAUDE.md`. Until it exists, the honest reading is the one
EG3 already gives: record the red with its cause named, and name it in the report.

**Closed when** the report carries, generated rather than written: an
`Answers: verdict 110 @ <this verdict's sha>` header, `docs/reports/F6/step-1-answers.json`
committed, the `## 0`/`## 0a` CI sections from `scripts/ci_section.py`, the whole-suite line
from `scripts/suite_count.py` run AFTER every other edit (CP3), and the five unsourced
sections' numbers inside a command block or table of their own section -- with the resulting
`FAILED` list pasted and every id in it matched by name to EG3's state (2).

**R746. (BLOCKING. (d), AND IT IS THE FIRST THING MY INSTRUCTIONS TELL ME TO CHECK.) THE
REPORT'S `Carried` SECTION ANSWERS VERDICT 108's LIST, NOT VERDICT 109's. R731 IS NAMED AS
BLOCKING WHEN IT WAS CLOSED, AND R734, R735, R736, R737 AND R738 ARE NOT NAMED AT ALL.**
`docs/reports/F6/step-1.md:5` (`Answers: FA3 opens the step`) and `:134-135`.

```
claim  "R730, R731 and R732 carry from F4's ledger, R730 and R731 blocking."
cmd    the newest verdict's own Carried and `Carried for F5's ledger` sections
rule   my instruction 1b: the `Answers: verdict <n> @ <sha>` header names the LATEST
       verdict, and a report answering a superseded round has every `Carried` claim about
       the wrong list
out    verdict 109 (`cdbbf79`, judging `3305473`): R731 CLOSED as to every condition;
out      R732 CLOSED and its warrant stronger than written; R730 NOT CLOSED and renamed
out      R734; R735, R736, R737, R738 raised
out    verdict 109's "the names that stay blocking": R730/R734, and R737
out    the report names: R730 blocking, R731 blocking, R732 carrying
judge  **TWO OF THE THREE DISPOSITIONS ARE WRONG AND THE TWO NEW NAMES ARE ABSENT.** This
       is exactly the failure 1b exists to prevent, and it is not academic: R737 is a
       blocking carry that nothing in this step mentions, and R734's fourth condition --
       the corrected CSV going to Xabier with a sentence saying which column moved -- is
       unevidenced anywhere.
```

**The substance is better than the list.** R734's repair at `029cce5` is correct and I
verified it myself, below. The finding is the ledger, not the work -- and the ledger is what
the whole arrangement exists to re-read.

**Closed when** the header reads `Answers: verdict 110 @ <sha>` and the `Carried` section is
the generator's table over verdict 109's and this verdict's items, with R731 and R732 marked
closed by verdict 109 rather than carried, and R737 named.

## Closure items

Named with their site and what would close each. The implementer fixes the whole list once,
in the step's closure commit; they are not re-reviewed item by item and the step is not held
on one. F4's numbering ended at C40, so this list starts at C41.

* **C41.** `scripts/measure/api_wsd_utilisation.py:264`. The published `branch at K=2`
  column is computed as `kl2 >= 108.059` -- a literal -- while the utilisation on the same
  row used `column_slenderness_parameter() = 108.05885001274791`, and `locked.axial_branch`
  was available per row. Two rules for one decision inside one file, disagreeing on
  `KL/r` in `[108.05885, 108.059)`. **Closed when** the column reads the branch the check
  returned, or the literal is deleted in favour of the function.
* **C42.** `scripts/measure/api_wsd_utilisation.py:84-91`. `_section()` reads
  `built.bodies[0].members[0]` and the result is applied to all sixteen members, while
  `_kl_over_r()` four lines later reads each member's own body. Measured: all sixteen share
  `A = 1.31192909`, `I_y = 0.88797921`, `J = 1.77595841`, `D = 2.5`, so it is vacuous today.
  **Closed when** one `assert` states the equality the first function assumes, or `_section`
  takes the body.
* **C43.** `floatfea/checks/api_wsd.py:101`. `section_class(2.5, 0.18, fy=355.0)` returns
  `compact` with `limit_1 = 29126760.56` and `allowable_bending` returns `266.25 Pa`. The
  module's own docstring names this exact failure as the reason the SI forms matter, and
  nothing refuses it. **Closed when** an `F_y` that is not plausibly in pascals raises, or
  the docstring stops claiming the risk is handled.
* **C44.** `scripts/measure/api_wsd_utilisation.py:314-316`. "**{len(over)} of
  {len(all_stations)} member-stations exceed U = 1.0** ... All four are platform arm ROOTs"
  -- a computed count beside a hand-written "four". **Closed when** the sentence is
  generated from the same set, or the count is removed from the prose.
* **C45.** `.claude/agents/gating-supervisor.md:219` still reads `(a) a defect in
  `floatfea/`;` while `CLAUDE.md:152` and `docs/SUPERVISOR.md:27` carry EZ0's amendment --
  and `docs/SUPERVISOR.md:24-26` says the list "lives there, once". So the file that
  governs what the reviewer reads disagrees with the two files that point at it, and the
  reviewer reads the unamended head. **Closed when** a standalone `process:` commit citing
  EZ0 brings the agent file into line. Process class, not step work.
* **C46.** `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]`
  is red on its own fixture: "`frames.txt` now counts as a site: True, expected False". A
  guard failing false. **Closed when** it is fixed or deleted (CZ0), never accommodated.
* **C47.** `scripts/measure/member_forces_table.py:65` still reads "the midspan moment is
  the chord mean plus `w L^2 / 8`", one sign for two planes, against `:448` (`-w_z`) and
  `:449` (`+w_y`). That is R735 unchanged and still open. **Closed when** both sentences
  carry the two signs separately or point at the derivation.
* **C48.** `docs/milestones/F6.md` Â§ 3 item 3 names the branch limit as `1500/F_y`, the ksi
  form, where the code correctly uses `10340/F_y` with `F_y` in MPa. **Closed when** the
  plan row names the SI form the code implements.
* **C49.** `floatfea/checks/api_wsd.py:220-246`. `check_member`'s docstring says the
  arguments are keyword-only and why, and says nothing about the sign convention of
  `axial_n` -- which is the one argument whose sign changes a decision. R739's repair
  should land here too. **Closed when** the docstring and `MemberCheck.in_tension` name
  `docs/conventions.md:320`.
* **R735, R736, R738, C34 to C40, and the `0.2240`/`0.2239` item** -- all still open from
  verdict 109, carried in `docs/closure/F4.md:147` as a list, and not re-adjudicated here.
* **R712 to R717, C2 to C15, C24 to C33** -- still open, carried in the F4 closure
  artifact, not re-reviewed item by item, per CZ0.

## Tolerances touched

```
cmd    git diff cdbbf79..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff cdbbf79..HEAD -- floatfea/ | grep -E "^\+[A-Z_]+: Final"
out    +PASCAL_PER_MPA: Final[float] = 1.0e6
out    +ALLOWABLE_TENSION_FACTOR: Final[float] = 0.6
out    +ALLOWABLE_SHEAR_FACTOR: Final[float] = 0.4
out    +BEAM_SHEAR_AREA_FACTOR: Final[float] = 0.5
out    +CM_NO_TRANSVERSE_LOAD: Final[float] = 0.85
judge  **NO TOLERANCE VALUE OR COUNTER MOVED ANYWHERE IN THE TREE, AND NOTHING WAS
       WIDENED.** EU1 does not fire on this diff; I ran its adversarial case anyway,
       because the diff introduced two DECISION RULES with no tolerance behind either --
       Â§ 3.2.2's branch and Â§ 3.2.3's three branches -- and a branch boundary is a
       threshold whether or not it is called one. Running the clauses at the boundaries the
       commit did not choose is what found R742 and R741.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `PASCAL_PER_MPA` | -- | `1.0e6` | a unit conversion, not a tolerance | none, correctly | `floatfea/checks/api_wsd.py:55-56` | **ADMISSIBLE and correctly NOT in `tolerances.py`.** It is a unit, read in exactly one place (`:101`), and I verified the branch limits it feeds against the ksi forms and their conversion: `1500 x 6.894757 = 10342.1`, `3000 x 6.894757 = 20684.3`. |
| `ALLOWABLE_TENSION_FACTOR` `0.6`, `ALLOWABLE_SHEAR_FACTOR` `0.4` | -- | as shown | clause coefficients | none, correctly | `:58-62` | **ADMISSIBLE.** Â§ 3.2.1 and Â§ 3.2.4 give exactly these. They are the clause, not a threshold anything is compared against, and the module's docstring says so -- which is the right reading of `CLAUDE.md`'s rule. |
| `BEAM_SHEAR_AREA_FACTOR` `0.5` | -- | `0.5` | the clause's own idealisation | none, correctly | `:64-69` | **ADMISSIBLE, and the direction in the comment is right** -- `V/(0.5 A)` is `2 V/A`, so using `A` reads 2x low, which is what it claims. |
| `CM_NO_TRANSVERSE_LOAD` `0.85` | -- | `0.85` | a declared modelling input that MULTIPLIES a published utilisation | none, and it needs one | `:71-77` and `docs/F6_utilisation.md` | **BLOCKED, R743.** Not because `0.85` is necessarily the wrong number -- it may be right under API's sidesway category -- but because the name, the docstring and the published label all attribute it to the no-transverse-load category, which is a different formula, and the stated direction is backwards: measured, `C_m = 1.0` moves the governing metric from `0.024114` to `0.128855`. A value that scales a published utilisation and has no counter is a tolerance in all but name. |
| the two Â§ 3.2.3 branch limits `10340`/`20680` | -- | as shown | dimensionless, `F_y` in MPa | none, and R742 is what a counter would have found | `:102-103`, `:86-88` | **BLOCKED, R742.** The numbers are the standard's. They are inconsistent with `E_STEEL = 210e9` by construction, and the consequence is an allowable above the clause's own cap on an interval of `D/t`. |
| the Â§ 3.2.2 branch at `C_c` | -- | `>=` | dimensionless | none needed -- the branches are continuous there | `:149` | **CLEAN, and I solved the boundary in both directions.** `C_c - 1e-12` takes the inelastic branch, `C_c` takes the elastic, and the two forms agree to `92608695.65217389` against `92608695.65217392`. Nothing to declare. |
| everything else in the F4 block | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 109 (`cdbbf79`, judging `3305473`, an EQ0 review of the F4 closure commit counting
against no step's rounds) was a **HOLD** carrying two names and a closure list. Every one,
with status. **The report's own `Carried` section is about verdict 108's list instead, which
is R746.**

* **R730 / R734 (blocking, carried into F6's ledger) -- CLOSED, and I measured all four
  parts of my own condition rather than three.** Answered at `029cce5`.
  **(1)** `scripts/measure/member_forces_table.py:449` now reads
  `mid[5] = mid[5] + sag_z` with `sag_z = +w_local[1] * span * span / 8.0`, and the
  calibration sentence is replaced by the derivation -- `e_x x F = (0, -F_z, +F_y)` giving
  `M_z'' = -w_y` and `M_y'' = +w_z` -- which is the route I asked for and not a
  recalibration. **(2)** BP0's regeneration is in the same commit:
  `docs/F4_member_forces.csv` (768 lines changed) and `docs/F4_member_forces.md`, and **the
  two top-ten figures I predicted independently reproduce exactly** -- `384.6 / 396.7` and
  `384.6 / 396.1` are what the regenerated table carries. **(3)** The control runs where
  `w_local[1]` is nonzero. **(4)** The sentence saying which column moved and by how much is
  in the commit message. **Does not carry as written. Its residue is R744** -- the control
  from part (3) is on the wrong half of the expression, which I measured rather than read.
* **R737 (blocking, carried into F6's ledger) -- STILL OPEN, AND NOTHING IN THIS STEP
  MENTIONS IT.** `grep -rn HSP_COMMIT tests/` returns my own corpus entry and
  `tests/verification/rung3/test_platform_deck_export.py:166`, which asserts the pin file
  names the commit -- not that the recorded provenance is compared against it, which is what
  the finding was. My condition offered two branches and either is one line: F6 decides
  whether `HSP_COMMIT` goes into the provenance at the next export, or records that the tag
  alone is the warrant and a moved tag is out of scope. **Carries, still blocking.**
* **R731, R732 -- remain closed by verdict 109** and are not re-raised. The report lists
  R731 as blocking; it is not. R746.
* **R735, R736, R738 and the `0.2240`/`0.2239` item (closure) -- STILL OPEN**, correctly, and
  carried as a list rather than landed. I verified only that R735 has not regressed further:
  `:65` still gives one sign for two planes. C47 above.
* **C34 to C40, R712 to R717, C2 to C15, C24 to C33 (closure) -- STILL OPEN**, carried in
  `docs/closure/F4.md:147` and not re-adjudicated.
* **The MID exclusion -- RULED, and the report's reason is the wrong one.** `docs/milestones/F6.md`
  Â§ 0 requires the step-1 report to state R730's discharge. R730/R734 **is** discharged (above),
  so the live reason to exclude MID is **R736's unmeasured-direction bending approximation**,
  not R730. Excluding MID is the right call and I am not reopening it; the report should say
  it rests on R736 and on the absence of a refined-mesh comparison, which is true, rather
  than on R730, which is not.
* **The schedule.** The report states the 22 October working target and the 28 October
  committed date and says the working target holds. I am recording rather than escalating:
  R739 is a sign and a regeneration, R741 to R743 are each a few lines, and G6.1 is the
  step's actual locked content and is unstarted. **If revision 2 closes still carrying any
  of R739 to R746, that is the second consecutive step boundary carrying blocking items in
  this milestone's first step, and the choice -- slip the date or reduce scope -- has to be
  stated rather than restated.**

## Try to break it -- what I ran and what it said

Six adversarial configurations, none of them chosen by the diff. Four found something.

```
1  A MEMBER IN PURE TENSION, sense prescribed rather than inferred -- node B moved 1 mm
   outward along the member axis. Published N = -5510102.18698421 at both stations.
   -> R739. This is the one that outranks everything in the report.
2  THE SAME TABLE WITH THE AXIAL SIGN INVERTED, one variable moved: branch histogram
   IDENTICAL (128/128), governing clause flips on every row, F_a wrong by 2.9079x on the
   four governing stations, FA2 headline 0.024114 -> 0.034926.  -> R739's reach.
3  A SLENDER TUBE, D/t = 100 -- admissible input, past API 3.2.2.b's limit of 60.
   allowable_axial_compression returns 136098611.12 Pa, branch inelastic, no refusal.
   -> R741, and the locked plan requires the refusal in its own words.
4  THE BRANCH BOUNDARIES THEMSELVES, solved rather than sampled. D/t = 29.1268 gives
   F_b = 267.79 MPa against a 0.75 F_y cap of 266.25, and the reduced branch stays above
   the cap to D/t = 30.5974.  -> R742.
5  C_m AT API's OTHER CATEGORY, 1.0 -- one variable moved. The governing metric goes
   0.024114 -> 0.128855, and with the sign also corrected two stations go 1.188 -> 1.380
   and 1.202 -> 1.380.  -> R743, and it inverts the report's own ranking of its levers.
6  THE SAG GUARD, MUTATED ON EACH HALF OF ITS EXPRESSION SEPARATELY, on a fixture where
   w_y = 28125.0 rather than zero. The intermediate reddens; the published line does not,
   and MID Mz goes +2.93e+06 -> -1.46e+07.  -> R744.
```

**And two things I tried that did NOT break, recorded because an absence of a finding is
also a measurement.** `MemberCheck.utilisation` cannot under-report the interaction --
`u_combined >= u_bending` holds identically in both clauses, because Â§ 3.3.2's simple form
is `f_a/(0.6 F_y) + u_bending` and `f_a >= 0`. And the empty-parameter-set shape is handled:
if the `GOVERNING_PERIODS` filter matched nothing, `:178` raises rather than writing a
zero-row CSV that would read green.

## The adversarial corpus (BE3)

**BATCH 42, committed separately at `517f8e2`:
`tests/corpus/f6_api_wsd_sign_convention_and_clause_boundaries.txt`, 22 entries, every one
new this round and none of them read by the implementer.**

EG4(e)'s pause to 28 October permits it and the file header claims the exception explicitly:
every entry is on F4's load-mapping surface -- the `N` column of
`docs/F4_member_forces.csv`, the generator that writes it, and, new this round, the code
that READS that column and BRANCHES ON ITS SIGN to pick an allowable. A miss here reaches a
published allowable and a published clause number, not only a member force.

**COVERAGE: the shipped checks catch 5 of 22.**

```
cmd    grep "^id=" <the file> | grep -c "expect=catch"
out    5
cmd    grep "^id=" <the file> | grep -c "expect=miss"
out    17
```

Against the last four rounds -- 1 of 16, 9 of 21, 4 of 11, 8 of 13 -- this is the second
lowest, and for the same reason batch 41's was the lowest: **the surface has no gate.**
`grep -rl api_wsd tests/` is empty, so nothing under `tests/` reads either new file, and
seventeen of the twenty-two misses are on code that no test imports. The five catches are
all controls, and two of them are the measurements the hand-back asked for and did not have
(the branch-boundary continuity, and the sag guard's reach on each half separately).

**The useful number for the plan is not 5 of 22; it is that six of my eight blocking
findings are things G6.1's hand calculations and counter-cases would have caught.** That is
the measurement on the ordering, and it is in the section below.

## On FA3 versus G6.1 -- this one is Xabier's, not the implementer's

I was asked to rule on whether shipping a utilisation table before G6.1 is acceptable under
FA3's ordering, or whether FA3 and G6.1 conflict. **They conflict, and the measurement is
this round.**

FA3 says send it as soon as the first full pass exists. G6.1 says every one of the six
clauses is verified against an independent hand calculation before the milestone has a
result. Both are reasonable and they cannot both be honoured in one commit, because the
thing FA3 asks to be sent is the output of the thing G6.1 asks to be verified first.

**What the conflict cost, measured rather than argued.** Of my eight blocking findings,
**six are inside the scope of G6.1's own gate**: the sign convention (an independent hand
calculation of a member in tension finds it immediately), the local-buckling refusal (a
counter-case per clause is literally the missing refusal), the bending-branch cap (a hand
calculation at the branch limit is the first thing one does), `C_m`'s category and
direction (a hand calculation states the category it used), the provenance label (a hand
calculation names its input), and the sag guard's reach (a counter-case per check). Only
R745/R746, the report guards, are outside it. **And the table has already been sent.** The
correction that now has to go out is the second correction to a deliverable in eight days.

**My recommendation, offered once and not as a HOLD.** Keep FA3's ordering but bind it:
a published deliverable may go before its gate **if** the send carries, on its face, the
sentence that its clause implementations are unverified and that the numbers may move --
and if the gate lands in the next commit rather than the next revision. That is one
sentence in the label block and it is cheaper than a second correction. The alternative is
to invert the ordering for F6 step 2, which costs the send date.

**It is not a HOLD and it does not become another round.** I am ruling the step HOLD on
(a) and (d) items that stand on their own. This paragraph leaves the loop.

## On C27, for the third time -- also Xabier's

The report is right that the two directives disagree and right that this commit satisfies
both only by carrying the marker and the report together.

```
cmd    git log --oneline -2 -- docs/milestones/F6.md
out    0b9ea0d F6 step 1: the six API RP 2A-WSD clauses ...
out    da0e472 plan: EZ2 the envelope basis, EZ3 the numbering, EZ4 the F6 lock
cmd    git show --stat 0b9ea0d | grep -E "milestones/F6|reports/F6"
out    docs/milestones/F6.md       | 34 +++-
out    docs/reports/F6/step-1.md   | 135 ++++++++++++++
judge  marker and report in ONE commit, so FA3's "first commit" and the guard's "the commit
       that adds the report" coincide. They coincide only because this step took one
       commit. At `4344495` they did not and the guard refused.
```

**My ruling, and it is a ruling on the mechanism rather than a preference.** The guard's
rule is the one that can be enforced and the directive's is not: a marker moved in a
commit with no report leaves the tree in a state where `STEP` resolves to a step with no
report, which is the state `test_the_plan_names_the_step_under_execution` exists to refuse.
**So the guard is right and FA3's wording should change**, not the guard -- "the marker
moves in the commit that adds the step's report" is one phrase, it is enforceable, and it
costs nothing because a step's first commit can simply carry the report stub. If Xabier
prefers the directive's wording, the guard has to be deleted rather than extended (CZ0),
and then nothing checks the marker at all. **That is the choice, stated once.** It needs a
decision because luck of ordering has now resolved it twice and will not a third time.

## On the criterion -- I was asked, and I agree with it, and EZ0 is why this round is cheap

CZ0 as amended by EZ0 is right and I applied it. **All eight of my findings are (a), (c) or
(d)**: four defects in `floatfea/`, two in a published deliverable and its generator, and
two on a red suite with a red CI. **Nothing in this verdict is held against
a figure or a sentence** -- nine prose items went into the closure list, including C44 and
C48 which under the retired head would each have been a finding and would each have moved
nothing.

**AND I WANT TO RECORD WHAT EZ0 BOUGHT, because I asked for it twice and it is now
measurable.** R739 and R740 are both in the class the amendment added. Under the unamended
head R740 would be a closure item -- `scripts/` is not `floatfea/`, a label is not a
tolerance, the generator asserts nothing, and no test was red on it -- and `U = 1.815` would
have gone to Xabier labelled as a per-instant stress for a second round. R739 happens to sit
in `floatfea/` as well, so it would have blocked either way; R740 would not have. **One of
my two highest-value findings this round is blocking only because of EZ0.** That is the
third consecutive round in which the amendment's class carried the highest-value finding,
and it is the last time I will say so.

**One note on what EZ0 does NOT reach, said once.** `docs/F6_utilisation.csv` and
`docs/F6_utilisation.md` are generated by `scripts/measure/`, so they are squarely inside
the amendment. `floatfea/post/member_forces.py:23`'s inverted attribution sentence is in
`floatfea/` but is prose, and I have filed its substance under R739 as a site of the sign
defect rather than as a sentence -- which I think is the right reading, because the sentence
is the only statement of the convention anywhere and the next reader will take it as
authoritative. If that reading is too wide, say so and I will file it as closure class.

## Next step opens when

**STEP 1 STAYS OPEN. THIS WAS ROUND 1 OF THREE AND TWO REVIEWED REVISIONS REMAIN.** In
order, cheapest first, and the first one is one character plus a regeneration:

1. **R739 is answered** -- the sign convention is read once, from `docs/conventions.md:320`,
   with the 1 mm prescribed-stretch cell pasted as the control, both attribution sentences
   corrected, and `docs/F6_utilisation.csv` and `docs/F6_utilisation.md` regenerated in the
   **same** commit (BP0). My figures to beat: `F_a = 73.25` on the four platform ROOTs and
   `161.02` on the hub ROOTs, `u_axial = 0.001043` at the governing station, all four
   over-unity rows at Â§ 3.3.2, and `largest |U(K=2)-U(K=1)| = 0.034926`. If the regeneration
   disagrees with those, the disagreement is the finding and I want to see it rather than a
   reconciliation.
2. **R740 is answered** in the same commit, because it is the same label block and the same
   regeneration: the published column says which quantity it is, and `1.81496` against
   `1.7115` at the governing station is published beside it.
3. **R746 is answered** -- the `Answers:` header names this verdict, and the `Carried`
   section is the generator's table over verdict 109's list with R731 and R732 closed and
   **R737 named**.
4. **R745 is answered** -- the report's generated sections exist: `step-1-answers.json`
   committed, `## 0` and `## 0a` from `scripts/ci_section.py`, the whole-suite line from
   `scripts/suite_count.py` run AFTER every other edit, the five sections' numbers sourced,
   and the resulting `FAILED` list pasted with every id matched by name to EG3's state (2).
   **CI must be green at the revision's own commit**, or red with its cause named and
   traced.
5. **R741, R742, R743 and R744 are answered** -- each is a few lines and none needs a run.
6. **R737 is answered or recorded**, per verdict 109's two branches. One line either way.
7. **G6.1 is the step's locked content and is unstarted.** `docs/verification/api_wsd/`,
   six hand calculations not derived from the code, a counter-case per clause with a
   declared injection size and a plan row, and the tolerance the comparison needs -- which
   `docs/milestones/F6.md` Â§ 3 says must reflect float arithmetic and nothing else. **Six of
   my eight findings are inside that gate's scope.** It is not optional and it is not step 2.

**What I will not accept at revision 2.** A sign fix without the prescribed-sense control
pasted, because this project has now twice calibrated a sign against a cell that could not
see it. A regenerated table whose provenance label still names a column it does not read. A
clause function that returns an allowable above its own clause's cap. A `C_m` whose stated
direction is still the opposite of its measured one. And a control that reads the
intermediate rather than the published quantity -- that is R744, it is the third round on
those two lines, and the question for all five is the same one: if the thing this assertion
claims were false, would it go red. Today the measured answer is no for each.

**And one thing on the record for the implementer rather than against them.** The hand-back
named the five things to attack in priority order, and the order was right: item 1 was where
the defect was, item 3 asked me to attack a conclusion that turned out to be half wrong in
the direction the hand-back itself suspected, and item 4 self-reported the missing gate
before I could find it. The clause arithmetic the hand-back was least sure of -- `C_c`, the
safety-factor polynomial, the `3.3.2` max-of-two, the two shear forms, the SI conversion --
is correct in every case, and I checked each from the US forms rather than from the module.
**Three of the four numbers you have sent Xabier in this project were wrong, and the reason
is not the arithmetic: it is that nothing between the arithmetic and the send reads either
file.** That is G6.1, and it is the next thing to build.
