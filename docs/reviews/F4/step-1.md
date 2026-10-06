# Review — F4 step 1
Reviewed commit: 6e3915152c0dc6936943855a4e5fc966e5695fa5
Verdict: PASS
**Reviewed commit: `84de436c35f3c736c22ac56ff36f7735613b4d29`** (HEAD of F3 at invocation,
pushed). My corpus commit `6e39151` lands first, so the script's `Reviewed commit:` stamp
and the judged commit differ; DU1 says restate the judged one and this is it. The range is
`9f75cd5..84de436` -- two commits: the closure commit `ecace4a` and the standalone
`process:` commit `84de436`.
Tests: 3022 passed, 0 failed, 0 skipped   (MY OWN run, ONE invocation, no `--ignore`, no
deselection, no `-k`, in the repository itself with its GitHub origin, 655.89s. `grep -c
"^FAILED"` over the log gives 0. I did not accept a count from the report.)
**CI at the reviewed commit: run `37424376028` at `84de436`, conclusion SUCCESS -- every
job AND every step, `ladder 4 -- the loads are the loads: success`, `ladder 5: success`,
`guards and meta-tests: success`.**

## Round of 2026-10-06 -- NINETY-SIXTH verdict. F4 step 1's CLOSURE COMMIT, not a fourth round.

**PASS, and PASS here means a specific thing: the closure commit stands, and step 1's PASS
at the ninety-fifth verdict is undisturbed (DD1).** It does NOT mean nothing is open. Four
blocking-class items are open and they **CARRY INTO STEP 2 BY NAME** on top of R679's
remainder, R682, R683, R684, R685 and R653. I am not reopening a closed step to hold them
and I am not softening them to fit a PASS: the step is closed by CZ0's cap, so by-name
carry is the only container the mechanism has, and it is the one verdict 95 already used.

**The three carried items are substantively fixed and I reproduced each rather than
accepting it.** R679's per-body residual reads `1.778481e+00` and `1.635665e+00` on the two
dropped-joint shapes against a `1.0e-12` ceiling, matching the implementer's figures to
seven digits. R680's `rho A L` is the right pair -- `material` is per body, `section` is per
member. R681's form is now relative and dimensionless.

**And three of the four new findings are INSIDE those three repairs.** That is CP2's
recorded shape stated as a measurement rather than a worry: a counter declared above the
worst defect it must catch (R682), a decision rule changed with nothing in the tree holding
it there (R683), and four tolerance figures republished against the rule the same commit
deleted (R685). The fourth, R684, is MINE -- C158's closing condition asserted a premise I
did not measure, the implementer implemented it faithfully, and it is false.

**On the implementer's own question -- was fixing the three blocking items in the closure
commit the wrong call under CZ0? NO, IT WAS THE RIGHT CALL, and I say so at the top because
I was asked directly.** CZ0's carry-by-name governs what may consume a review ROUND; it
does not forbid a fix. Two of the three left a gate actively wrong for the step that builds
on it, and R680 left a gate that false-reddens on a correct solve -- shipping that into
step 2 to protect a round budget would be the wrong trade. **But the cost was real and this
verdict is what it cost**: three new blocking items shipped unmeasured, which is precisely
the gap CZ1 names in its own words, and CZ1 (ii)/(iii) is why there was a measurement to
make at all.

## 1. THE DIFFS, EACH ONE SEPARATELY, AS MY INSTRUCTIONS ORDER THEM

```
cmd    git log --oneline 9f75cd5..HEAD
out    84de436 process: C154 -- `_build` read `.git` as a directory ... (EK2)
out    ecace4a F4 step 1 closure: C135 to C160, and the three items verdict 95 carries
cmd    git diff --stat 9f75cd5..HEAD
out    F4.md 31, selfweight.py 13, platform.py 18, inertia_relief.py 18, static.py 38,
out    tolerances.py 61, export_buoy_centers_ref.py 32, test_report_guard_states.py 47,
out    rung4/test_f4_static_and_mapping.py 230.  NINE files, 366 insertions, 122 deletions.
cmd    git diff --name-only 9f75cd5..HEAD -- docs/reports
out    (no output) -- **the closure commit does NOT touch the step report.** The
out    implementer's first finding is confirmed at the level that matters.
cmd    git diff 9f75cd5..HEAD -- .claude docs/SUPERVISOR.md         [instruction 4b]
out    (no output) -- **NO STOP-CLASS FINDING.** My own instructions are untouched across
out    the whole range and I diffed them myself; nothing in the suite reads them. And
out    `84de436` IS a standalone `process:` commit citing EK2 that touches ONE file and
out    nothing in `floatfea/`, which is the form Â§ "The reviewer's own instructions" asks
out    for applied to a harness rather than to an instruction.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"      [instruction 4c]
out    tests/conftest.py                                  -- the instruction is intact
cmd    git diff 9f75cd5..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (no output) -- nothing the ladder gate reads was rewritten from a rung, and the
out    rung4 file adds no hookwrapper, no `pytest_ignore_collect` and no
out    `pytest_collection_modifyitems`. I read all 230 changed lines of it.
cmd    git diff --stat 9f75cd5..HEAD -- floatfea/tolerances.py       [instruction 4]
out    43 insertions, 18 deletions -- ONE rename-with-form-change pair and three comment
out    corrections, read line by line in Â§ Tolerances touched. NO EXISTING VALUE MOVED.
cmd    grep -rn "F4_STATIC_TIP_MOMENT_N_M" over floatfea tests scripts docs/milestones
out    (no output) -- the old absolute constant leaves no stale reference behind.
```

**INSTRUCTION 1b, and its subject does not exist in this range.** The newest report is
`docs/reports/F4/step-1.md` revision 3, whose `Answers:` header names verdict 94 @
`de9a448` while verdict 95 exists -- which read mechanically is the HOLD 1b describes. It
is not one here, and the reason is that **there is no report in this range at all**: the
step closed PASS at verdict 95 and verdict 95 routed its three open items into STEP 2's
`Carried`, not into a step-1 revision 4. 1b exists so that a report's `Carried` is about
the right list; the right list for these items is step 2's. I state the comparison rather
than skipping it, which is what 1b asks.

## 2. CI AT THE REVIEWED COMMIT (CA2), AND IT IS GREEN AT JOB AND STEP LEVEL

```
cmd    gh run list --commit 84de436c35f3c736c22ac56ff36f7735613b4d29 --json ...
out    [{"conclusion":"success","databaseId":37424376028,"event":"push","name":"CI",
out      "status":"completed","workflowName":"CI"}]
cmd    gh run view 37424376028 --json jobs -- job AND step level, with runnerName
out    JOB the verification ladder: success   [06:33:16Z -> 06:36:41Z]
out      ladder 1 / 2 / 3 / 6 success
out      **ladder 4 -- the loads are the loads: success**
out      **ladder 5 -- independent confirmation: success**  (not skipped behind a red)
out    JOB lint, unit and guards: success    [06:33:16Z -> 06:44:18Z]
out      actionlint / ruff / black --check / mypy / unit tests  ALL success
out      **guards and meta-tests: success** -- SEEN TO HAVE RUN, which is CZ1 (iii)
out    JOB CI determinism -- leg: skipped ; ten legs agree: skipped
rule   CK2: the third state is `runner_name: ""`, NO steps, a two-second duration and the
       spending-limit annotation
judge  **NOT CK2 AND NOT A RED.** Both real jobs carry full step lists with real
       conclusions and three- and eleven-minute durations. `runnerName` reads null on
       every job in this account's API responses, including ones that plainly ran for
       eleven minutes, so I ruled on the step lists and durations rather than that field,
       as I did last round.
cmd    gh run list --commit ecace4a --json ...
out    []
judge  `ecace4a` has no run of its own because the push that carried it also carried
       `84de436`. I checked the consequence rather than assuming it away:
       `git diff --stat ecace4a..84de436` is ONE file, `tests/test_report_guard_states.py`,
       so the whole of `floatfea/`, `scripts/`, `docs/milestones/` and the rung-4 gate at
       `ecace4a` is BYTE-IDENTICAL to the tree the green run measured. CZ1 (iv) is
       satisfied by the follow-on's own green sha, which is what CZ1 (iv) provides for.
cmd    ruff check floatfea tests ; black --check floatfea tests ; mypy floatfea
out    All checks passed! / 97 files unchanged / no issues found in 35 source files
judge  run by me at `84de436`, not taken from the report.
cmd    bash scripts/run_rung.sh full:tests/verification/rung4      [my own run]
out    run_rung: 153 collected, 0 failed, 0 errored, 0 skipped
out    run_rung: OK -- 1 director(y|ies) ran
rule   scripts/run_rung.sh -- a rung with any skipped case exits FAIL
```

## 3. R679 IS FIXED, I REPRODUCED IT EXACTLY, AND NOTHING IN THE TREE HOLDS IT THERE

The fix is real and it is the plan's own wording. `_resultants` and `_expected_resultants`
return a dict keyed per body and `_body_errors` normalises each separately.

```
cmd    the mapper mutated per shape, lam row (seed 4), `nodes` and the expected side all
         held, then BOTH `_mapping_error` as shipped AND the aggregate it replaced
out    case                     | PER BODY (shipped)     | AGGREGATE (reverted)
out    clean                    | 2.196224e-16 GREEN     | 1.872582e-16 GREEN
out    sign_not_flipped         | 3.556962e+00 RED       | 9.202049e-01 RED
out    wrong_node_same_body     | 9.597086e-01 RED       | 2.437483e-01 RED
out    drop_one_internal        | **1.778481e+00 RED**   | 1.872582e-16 GREEN
out    drop_all_four_internal   | **1.635665e+00 RED**   | 9.362910e-17 GREEN
out    drop_one_buoy            | 5.190127e-01 RED       | 4.425295e-01 RED
out    per body, drop_one : platform 1.778e+00 hub1 3.897e-01 hub2 1.795e-16
out                         hub3 2.093e-16 hub4 1.635e-16
out    per body, drop_four: platform 1.000e+00 hub1 3.897e-01 hub2 3.674e-01
out                         hub3 1.636e+00 hub4 3.799e-01
cell   ONE VARIABLE MOVED between the two columns: the normalisation scope. Same mapper,
       same lam, same nodes, same expected side, same ceiling.
rule   `error < F4_MAPPING_CONSERVATION` = 1.0e-12
judge  **R679'S SUBSTANCE IS ANSWERED and my figures to beat are beaten to seven digits**
       -- I asked for `1.778500e+00` and `1.635700e+00` to stop reading as round-off and
       they read `1.778481e+00` and `1.635665e+00`. The small differences from verdict 95
       are my removal shape (both sides of the joint, four-component block) against the
       mutation I wrote last round, not a disagreement.
judge  **AND THE SECOND HALF OF R679'S CLOSING CONDITION IS NOT MET.** It asked for "both
       counter-cases plus the two dropped-joint shapes above re-measured and pasted per
       body". The two dropped-joint shapes are not in the file. R683.
```

## 4. TRY TO BREAK IT -- THE REPAIR IS UNPROTECTED, AND I SOLVED THAT BOUNDARY

```
cmd    grep -n "internal_joint_dropped\|parametrize" tests/verification/rung4/test_f4_static_and_mapping.py
out    233:@pytest.mark.parametrize("injection", ["remainder_dropped", "gravity_reversed"])
out    830:@pytest.mark.parametrize("injection", ["sign_not_flipped", "wrong_node_same_body"])
out    958:@pytest.mark.parametrize(   -- the EK0(a) sites
cmd    grep -rn "internal_joint_dropped" --include=*.py .
out    (no output)
judge  **THE INVOCATION'S CLAIM "a new counter-case parametrisation `internal_joint_dropped`
       is in the file so the aggregate cannot return" IS FALSE.** The parametrisation list
       at `:830` is the one that shipped last round, unchanged. BF0: this is a sentence
       that states a fact about the code, and one grep refutes it.
judge  And it matters rather than being a slip of the pen, because Â§ 3's right-hand column
       is the measurement: **both shipped counter-cases are RED under the aggregate too**,
       so reverting `_resultants`, `_expected_resultants` and `_mapping_error` to the
       six-vector form leaves the ENTIRE suite green. "A gate carries its own failure" --
       break the claimed property and confirm the assertion goes red. The claimed property
       is now *per body*, and breaking it goes nowhere. R683.
```

## 5. R681's FORM IS RIGHT AND ITS COUNTER IS DECLARED ABOVE THE DEFECT IT MUST CATCH

This is the finding I would put in front of the implementer first. The form change is
correct and answers R681. The counter that came with it does not describe the quantity the
assertion measures, and the direction of the error is the unsafe one.

```
cmd    solve the clean and defect tip/root ratios for ALL SIXTEEN members, which is the
         loop the ceiling runs, rather than for the one member the counter-case injects into
out    CLEAN, worst over 16: platform:hub4_arm  root 1.149609375e+08  tip 6.053597e-08
out      ratio 5.265785810941744e-16   -- 1899x below the 1.0e-12 ceiling
out    DEFECT (R663's formula), all sixteen:
out      platform:hub1_arm      5.263157894736842e-02  = exactly 1/19   counter HOLDS
out      platform:hub2/3/4_arm  5.263157894736891e-02  = 1/19           counter HOLDS
out      hub1:buoy1_arm .. hub4:buoy12_arm, TWELVE members
out                             4.166666666666627e-02  = exactly 1/24   **counter FAILS**
out    members whose defect ratio is BELOW the declared counter 0.05: **12 of 16**
cmd    the gate's own denominator under the defect, printed
out    DEFECT root My 121347656.25000013   where the CORRECT root is 114960937.50000009
out    and the difference is exactly `mu L^2 / 12` = 6386718.750000007, the tip moment
rule   `tip_ratio = abs(mf.end_b[4]) / abs(mf.end_a[4])`, and under R663's formula
       `mf.end_a[4]` is the correct root PLUS `mu L^2/12` -- the defect moves the
       denominator too
judge  **THE ENTRY AND THE PLAN ROW QUOTE A RATIO THE ASSERTION NEVER COMPUTES.** Both say
       "the measured worst over all 16 members is 5.555556e-02", derived as
       `6386718.75 / 114960937.5`. That arithmetic is right and it is the ratio to the
       CORRECT root. The assertion divides by the DEFECT'S root, giving `1/19` on a
       platform arm and `1/24` on a hub arm. **No member reads 5.555556e-02.**
cmd    solve the counter boundary in the weakening direction (EH4), by substitution
out    counter 0.05 -> 437 passed (shipped) ; 0.04 -> 1 failed, the plan pin only
out    counter 0.06 -> 2 failed, + test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula
judge  so the measured margin is `5.263158e-02 / 0.05` = **5.26%**, not the 11.1% the
       quoted `5.555556e-02` implies, and the bracket in the plan row (`1.0550e+14x`) is
       computed from the wrong numerator -- measured it is `9.9950e+13` against the member
       injected and `7.9127e+13` against the worst member.
judge  **AND THE DIRECTION IS THE UNSAFE ONE.** A counter is "the smallest defect the same
       assertion, in the same quantity, detects". Declared at `0.05` it is ABOVE the
       smallest defect R663's formula actually produces on the members the ceiling covers,
       so a gate whose sensitivity degraded to anywhere in `[0.0417, 0.05)` would still
       pass its own bracket while missing this defect on twelve of sixteen members. The
       counter-case passes only because it injects into `body.members[0]` of the platform,
       which is the EASIEST of the sixteen and not the hardest. R682.
cmd    and the ceiling itself, both directions
out    1.0e-11 / 1.0e-13 / 1.0e-15 -> 1 failed, the plan pin ONLY (clean worst 5.27e-16
out      passes at 1e-15); the clean case trips at a ceiling of 5.265785810941744e-16
out    the ceiling may RISE to 5.263157894736842e-02 before the counter-case's
out      `tip_ratio > CEILING` stops holding -- a factor of 5.3e+10
judge  **THE CEILING'S VALUE AND FORM ARE ACCEPTED.** `1.0e-12` is a round-off ceiling
       1899x above the measurement, dimensionless, against a stated response scale that is
       two lines above the assertion. R681's own closing condition is met on the form, and
       the entry's "nothing to be relative to" sentence is deleted rather than rephrased,
       which is what I asked for. The entry's "tightened, the clean case trips below
       1e-15" brackets the boundary without solving it; that is a closure item, not this.
```

## 6. C158'S CLOSING CONDITION WAS MINE AND ITS PREMISE IS FALSE

I asked for the `max(..., 1.0)` floor to be removed and said the thing it guarded against
was assertable. The implementer did exactly that. The premise I handed over is wrong and
the gate now raises on a legal input.

```
cmd    hand the gate a multiplier row with ONE nonzero joint block and nothing else
out    only ('buoy1','buoy1','hub1') nonzero, ||lam|| = 1.912540e+06 (NONZERO)
out      bodies with a zero force- or moment-scale: ['platform','hub2','hub3','hub4']
out      _mapping_error -> AssertionError: "hub2's expected resultants are
out      array([0.,0.,0.,0.,0.,0.]), so there is no scale to normalise by."
out    only ('hub4','hub4','platform') nonzero, ||lam|| = 1.518610e+06
out      bodies with a zero scale: ['hub1','hub2','hub3']  -> AssertionError
out    only the FOUR internal blocks nonzero, ||lam|| = 3.535757e+06
out      -> measures 0.000000e+00 GREEN and does NOT raise (all five bodies are reached)
rule   `_one_body_error` asserts `f_scale > 0.0 and m_scale > 0.0` with the message "For a
       nonzero multiplier row no body can have a zero resultant -- every one of the five
       carries at least one joint"
judge  **THE MESSAGE'S SENTENCE IS REFUTED BY ONE ROW.** Every body carries at least one
       joint, which is true; it does not follow that every body's BLOCK is nonzero in an
       arbitrary nonzero row, and a load case in which only some joints carry reaction is
       physically ordinary. The gate errors rather than measuring. R684.
judge  **LATENT TODAY and I say so rather than overstating it**: the gate is only ever
       handed `_synthetic_lam`, which I measured dense in all 16 of 16 blocks, so nothing
       in the suite reaches this -- `run_rung: 153 collected, 0 failed, 0 errored`. The
       floor's REMOVAL is otherwise a strengthening and I checked the direction: the
       per-body scales measure `1.157232e+06` to `5.281836e+06` (force) and `4.182033e+07`
       to `3.182e+08` (moment), so the floor never bound, and removing it can only make
       the normalised error larger. Nothing was widened here.
judge  The finding is MINE before it is the implementer's. C158 said "the quantity cannot
       be zero for a nonzero lam row, which is assertable" -- I wrote that from reasoning
       and did not take the measurement, which is the one guard on my own list I broke.
       "Convert arguments into measurements."
```

## 7. BP0 -- FOUR TOLERANCE FIGURES CROSSED A RULE CHANGE IN THE SAME COMMIT

R679's fix IS a change to a decision rule. `F4_MAPPING_CONSERVATION` and its counter sit
twenty lines away in the same file and the same commit, and none of their figures moved.

```
cmd    re-take every figure in the mapping entries under the SHIPPED per-body rule
out    figure as published                 | measured at 84de436 under the shipped rule
out    clean 1.8726e-16, "5341x above"     | 2.196224e-16, 4553x
out    wrong node: force 5.2050529737194385e-17, moment 0.24374825705420716
out                                        | platform force EXACTLY 0.000000e+00,
out                                          moment 9.597086e-01
out    "Reason for 0.2 ... MEASURES 0.24374825705420716"   | 9.597086e-01
out    "the other injection ... reads 0.9202048893902944"  | 3.556962e+00, and its FORCE
out                                          channel is 3.556962e+00, not round-off
out    "the wrong-node defect is the smaller of the two"   | STILL TRUE, 0.96 < 3.56
rule   BP0: "when a decision rule changes, every figure citing the old rule is regenerated
       or withdrawn in the same commit. Not the next one, and not when someone notices."
cmd    and the consequence for the counter, solved rather than asserted (EH4)
out    wrong-node injection scaled: 1.00 -> 9.597086e-01 HOLDS ; 0.25 -> 2.399271e-01
out      HOLDS ; 0.21 -> 2.015388e-01 HOLDS ; 0.208 -> 1.996194e-01 FAILS
judge  the injection may now weaken **79%** before `error > 0.2` fails, where verdict 95
       measured **18%** under the aggregate. The counter errs SAFE in that direction, so I
       am NOT asking the value to move -- `0.2` demands less of the gate than the gate
       delivers, which is the harmless side. What I am asking is that the justification
       describe the rule that shipped. R685.
judge  The one figure that got STRONGER is worth naming because the entry under-states its
       own case: "THE MOMENT IS IN THE QUANTITY ... because a resultant force is blind to
       WHICH node a block landed on" is more true per body than the `5.2e-17` beside it
       says -- the platform's force channel is EXACTLY zero. A correct causal sentence with
       a stale number attached is still BP0's case.
judge  I class this as (b) rather than as a figure, and the instruction I am applying is
       the one that says to: these comments are the ONLY statement of what the counter is a
       bound below, and a reader solving the boundary from the entry as published would
       conclude 18% where the tree gives 79%.
```

## 8. R680, AND THE FIGURE THE IMPLEMENTER ASKED ME TO ADJUDICATE

```
cmd    read the line, then check the pair it uses is the right pair
out    `own_weight = body.material.rho * member.section.A * span * GRAVITY_MAGNITUDE`
out    platform.py:159 `material: Material` is per BODY; `member.section` is per MEMBER
judge  **R680 IS ANSWERED and the pair is correct** -- `material` is a body attribute and
       every element is built with it (`platform.py:178`), while `section` varies per
       member, so `rho * A_member * L_member` is this member's own prismatic mass and the
       analytic side is right on an unequal frame. The false-redden I measured is gone.
cmd    the old form against the new, every member, so the fix's size is on the record
out    worst gap 1.898721e-16 relative, on five hub arms; identical on the platform's four
judge  so the fix changes nothing measurable today and that is the point: it removes a
       wrong answer that was waiting for an unequal frame, not a wrong number now.
```

**THE `5.1513e-16` vs `5.265786e-16` QUESTION, RULED: THE IMPLEMENTER'S FIGURE IS RIGHT AND
ITS STATED CAUSE IS WRONG.**

```
cmd    print the tip/root ratio for all sixteen members, sorted
out    platform:hub4_arm  5.265785810941744e-16   <- the MAX, the implementer's figure
out    hub2:buoy5_arm     5.151312e-16            <- the SECOND, my figure from verdict 95
out    hub3:buoy9_arm     4.596556e-16 ; hub4:buoy11_arm 3.883297e-16 ; ...
cell   ONE VARIABLE MOVED: `_analytic_static` reverted to the body average, everything
       else held. The sixteen tip/root ratios are BIT-IDENTICAL either way.
judge  **`5.265786e-16` IS THE CORRECT WORST OVER ALL SIXTEEN and mine was the second
       largest** -- I took the max over a subset last round and the entry should carry the
       implementer's number, which it does. But the reason offered for the difference ("I
       measured after R680's change, which moves the expected side") is REFUTED by the
       cell: `tip_ratio` is `abs(mf.end_b[4]) / abs(mf.end_a[4])`, both from
       `member_forces`, and `_analytic_static` enters neither. R680 cannot have moved this
       figure. BG0 -- a causal sentence carries the cell that isolates it, and the cell
       here says the cause is which members were in the maximum. Reduced to the
       measurement: the two numbers are the first and second of the same sixteen.
```

## 9. THE FOUR CLOSURE ITEMS THAT CHANGED GATE BEHAVIOUR, ATTACKED AS ASKED

```
cmd    C157 -- the hub gate: re-measure the exchange it was blind to, and solve the Z edge
out    clean                   worst 0.000000e+00 m  checked 8   GREEN
out    hub1 <-> hub2 exchanged worst 7.071068e+01 m  checked 8   RED  (was 0.0, checked 4)
out    hub1 <-> hub3 exchanged worst 1.000000e+02 m  checked 8   RED
out    hub1 platform arm tip z +1.0e-06 -> 1.000000e-06 m RED ; +1.0e-07 -> GREEN
out    hub1 BODY centre node z +1.0e-06 -> 1.000000e-06 m RED ; +1.0e-07 -> GREEN
judge  **ACCEPTED AND IT IS A REAL STRENGTHENING.** `checked == 8` is asserted, both sides
       of each joint are compared, the three-component norm makes Z live, and the detection
       boundary is EXACTLY the declared `1.0e-06 m` because the quantity IS the offset norm
       -- solved from both sides, not sampled. The hub body's own node was previously never
       read at all, so a Z error there was a miss at any size.
cmd    C160 -- the anchored label check, on fourteen spellings its author did not write
out    CAUGHT (11): buoys{k} / buoy_{k} / buoy-{k} / b{k}uoy / xbuoy{k} / buoy{k}_hub1 /
out      buoy{k}_HUB2 / "buoy" / platform_buoy{k} / hUb{k} / "PLATFORM"
out    PASSES, correctly (3): BuOy{k} / BUOY{k+1} / buoy{idx}   -- these ARE buoy labels
out    MISS (1): f"{prefix}buoy{k}" -- a closing brace is a word boundary, so an arbitrary
out      runtime prefix satisfies the anchor
out    and my three misses from verdict 95 all CATCH now
judge  **ACCEPTED.** All three named misses are closed and the FE-body half folding case is
       a genuine tightening. One direction is worth recording and no sentence does:
       `f"BUOY{k+1}"` REDDENED under the old bare-substring form and PASSES now, because
       the buoy half got case-insensitive in the same commit the FE half did. The new
       semantics are right -- a buoy in another case is a buoy -- but it is the weakening
       direction of the same edit and EH4's spirit is that it gets said. Closure item.
cmd    C158 -- see Â§ 6. C152 -- read the docstring and the message against Â§ 3's figures
judge  C152 ACCEPTED: the docstring now names the reach the per-body form has and names
       `joint_order` and `nodes` as outside it with my own numbers, and the assertion
       message prints the per-body dict, which is "a residual destroys information"
       answered -- a reader sees WHICH body, not a norm.
cmd    C142 -- `rigid_links` moved to platform.py; is it behaviour-preserving?
judge  **YES, AND READING IS ENOUGH HERE, so I am answering the implementer's question
       directly: the ladder's green is not the only evidence and does not need to be.** I
       diffed the two deleted copies against the new function: the four-line body is
       BYTE-IDENTICAL to both, both call sites now pass the same `body`, and `mypy` types
       it the same. There is no behaviour to test that the two deleted copies did not
       already have tested. A test here would assert that a move is a move.
```

## 10. C154 -- THE HARNESS REPAIR IS RIGHT, AND I MEASURED IT IN THE ENVIRONMENT IT IS ABOUT

The implementer asked me to check I had not been handed a harness that lies somewhere else.
It is my instrument, so I built the environment and ran it, in a worktree registered against
a SCRATCH CLONE so that nothing lands on this repository.

```
cmd    git clone --local <repo> <scratch>/clone ; git -C clone worktree add --detach
         <scratch>/wt 84de436 ; ls -la wt/.git
out    -rw-r--r-- 169 bytes, `gitdir: .../clone/.git/worktrees/wt`
out    python: is_dir False  is_file True       -- the environment is reproduced
cmd    cd <scratch>/wt ; python -m pytest tests/test_report_guard_states.py -q
out    **23 passed in 156.80s** ; HEAD unmoved at 84de436 ; `git status --porcelain` clean
out    `git log --oneline -4` shows 84de436/ecace4a/9f75cd5/9285a9f -- NO seeding commit
cmd    THE ABLATION: the SAME worktree at `ecace4a`, one variable moved -- the 46-line
         `_real_git_dir_into` and nothing else
out    **1 failed, 22 passed** ; FAILED ..._REDDENS_CONTROL -- the state the implementer
out      named, and only that one
out    `git status --porcelain` -> ` M docs/reports/F4/step-1.md` and
out      ` M tests/test_report_carried.py`, `git diff --stat` 4 deletions
cell   ONE VARIABLE MOVED. Same worktree, same clone, same interpreter, same origin URL.
judge  **THE REPAIR IS CORRECT AND THE SEVERITY CLAIM IS CONFIRMED, INDEPENDENTLY.** The
       pre-repair harness wrote into the tree it was measuring -- it deleted lines from
       `docs/reports/F4/step-1.md` and `tests/test_report_carried.py` in the checkout
       under test -- which is a stronger statement than "one state failed". After the
       repair the tree is clean and HEAD has not moved.
judge  **AND I CHECKED THE OTHER ENVIRONMENTS RATHER THAN TRUSTING THE SHAPE.** The
       `src.is_dir()` arm is byte-identical to what the loop did, so a normal checkout and
       CI take the unchanged path -- confirmed by my own full run (3022 passed) and by the
       green `guards and meta-tests` step in run `37424376028`. The only behavioural
       difference in the new arm is that the copy is DETACHED where the old one inherited
       `ROOT`'s branch symref; nothing in the module reads a branch name, `git commit`
       works detached, and `reset --mixed` clears any staged state the copied common
       `index` carried. `--path-format=absolute` is the right call: a relative `commondir`
       copied one level down would resolve to the wrong place, which is the trap.
judge  Routing: standalone `process:` commit, cites EK2, one file, nothing in `floatfea/`
       or in the rung. That is the form. **C154 CLOSED.**
```

**AND THE EK3 ROUTING IS JUSTIFIED -- I reproduced the mechanism rather than accepting the
three-run account.**

```
cmd    in the scratch worktree, a commit on top of 84de436 whose ONLY change is one
         trailing newline in docs/reports/F4/step-1.md, then the two report-guard files
out    **8 failed, 224 passed**
out    FAILED tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one
out    FAILED test_the_guard_survives_the_state[baseline]
out    FAILED [non_numeric_step_suffix] [superscript_digit_step_number]
out           [draft_suffix_beside_a_step_report] [step_number_is_the_empty_string]
out           [verdict_amended_after_the_commit_the_report_answers]
out           [zero_padded_step_number]
judge  **THE GUARD READS THE COMMIT GRAPH and the content of the edit is irrelevant**, so
       a closure commit genuinely cannot carry a step-report edit after the step's final
       verdict. I measure 8 where the implementer reported 7; the extra one is in the
       other file, `test_report_carried.py`, and the seven in `test_report_guard_states.py`
       are exactly the implementer's count. EK3's routing of C137/C141/C144/C145/C147/
       C148/C151 into step 2's first report is correct and I am not asking for it back.
judge  The one part of the account I could NOT reproduce as stated is the middle run --
       "content byte-identical to `b0824d5` but the file still in the commit". Git drops a
       path with no diff from a commit, so that state is not constructible; I take the
       claim as describing the first and third runs. Recorded as unverified-as-worded, not
       as a finding, because the conclusion it supports is the one I measured myself.
```

## 11. THE LOCKED PLAN -- NOTHING HERE NEEDED A RE-LOCK, AND I CHECKED Â§ 0 BY HASH

```
cmd    git diff -U0 9f75cd5..HEAD -- docs/milestones/F4.md | grep "^@@"
out    @@ -8,6 +8,11 @@  @@ -240 +245,7 @@  @@ -330 +341 @@  @@ -334,2 +345,2 @@
cmd    grep -n "^## " docs/milestones/F4.md | head
out    28: ## 0. THE LOCKED ANSWERS (EK) ... 142: ## 1. SCOPE ... 311: ## 5. GATES ...
cmd    md5sum of section 0 at 9f75cd5 (lines 23-136) and at HEAD (lines 28-141)
out    a2d499fff42e1ed6a0207a5fdb1885bf  ==  a2d499fff42e1ed6a0207a5fdb1885bf
judge  **EK'S UNPARAPHRASED ANSWERS ARE BYTE-IDENTICAL. NO RE-LOCK IS NEEDED** and I rule
       on each of the four hunks rather than on the file: (i) line 8 is the preamble HTML
       comment, OUTSIDE Â§ 0, and C135 corrects a sentence that went false when the marker
       moved -- a correction of false prose, which is what CW0 requires; (ii) line 245 is
       Â§ 2's known-deviations list and C136 RECORDS a deviation that EL0 accepted, with
       the row "left as written rather than relaxed", which is the honest form and not a
       scope change; (iii) line 341 is C150 narrowing `F4_EB6_POSITION_M`'s row from "both
       edges solved" to "only the UPPER edge binds", which I measured myself last round as
       true -- it narrows the plan's DESCRIPTION to the truth and the gate's assertion is
       untouched; (iv) lines 345-346 are BR0's REQUIRED edit, the paired plan rows for the
       constant R681 forced to change form. A tolerance that moves without its plan row is
       the thing `test_plan_matches_tolerances` refuses.
cmd    perturb each new constant and run tests/test_plan_matches_tolerances.py
out    ceiling 1.0e-11 / 1.0e-13 / 1.0e-15 -> FAILED [F4.md-345-F4_STATIC_TIP_MOMENT_
out      RELATIVE-1.0e-12]  ; counter 0.04 / 0.06 -> FAILED [F4.md-346-..._COUNTER-0.05]
judge  the pin is live in BOTH directions on both new rows. I moved each rather than
       reading the table. **No value was widened anywhere in this range** -- the only
       numeric change in `tolerances.py` is the rename-with-form-change pair, and I read
       all 43 inserted lines.
```

## The adversarial corpus (BE3)

**Batch 35, committed separately at `6e39151`:**
`tests/corpus/f4_closure_counter_and_label_anchor_reach.txt`, **36 entries, all new**, on
F4's load-mapping gate and EB6's label-provenance gate -- EG4(e)'s two standing exceptions
to the corpus pause. Every `measured=` field was taken by me at `84de436`.

**COVERAGE, MEASURED AND NOT CLAIMED: of 36 new entries the step's shipped gates CATCH 19
and MISS 8; one produces a FALSE RED on a correct tree; 8 contradict a sentence shipped
beside the gate or inside a tolerance entry.**

```
cmd    a Counter of the expect field over the committed file
out    {'catch': 19, 'miss': 8, 'explain': 8, 'false_red': 1}  total 36
judge  Previous batches: 4 of 11, 8 of 13, 5 of 10, 5 of 17, 10 of 37, 11 of 31. **19 of
       36 is the best rate of the milestone**, and the reason is visible in the entries
       rather than in the rate: eight shapes batch 34 recorded as MISSES now CATCH -- the
       two hub-platform omissions (R679's fix), the hub-body exchanges and the Z component
       (C157), and three label spellings (C160). An entry that starts catching is updated
       and not deleted, which is what makes the two batches comparable.
judge  **AND THE MISSES MOVED TO A NEW SURFACE AGAIN: THE REPAIRS THEMSELVES.** Batch 33's
       misses were thresholds. Batch 34's were the wiring. Of this batch's eight misses,
       THREE are a repair that nothing holds in place or whose counter is declared on the
       wrong side (`mapping_per_body_rule_REVERTED_to_the_aggregate_6_vector`,
       `tipmoment_counter_0.05_exceeds_the_defect_ratio_on_TWELVE_of_SIXTEEN_members`,
       `mapping_wrong_node_INJECTION_weakened_to_scale_0.21`), and all eight of the
       `explain` entries are a figure or a sentence measured against a rule the same
       commit deleted. That is a different failure mode from either previous batch and it
       is the one CZ1 exists to catch, which is why this round was worth its spend.
judge  The entry I would put in front of the implementer is
       `mapping_per_body_rule_REVERTED_to_the_aggregate_6_vector`: undo R679's entire fix
       and the suite stays green, 3022 passed, because both shipped counter-cases were
       already red under the aggregate. That is R683 and the corpus is where I found it.
judge  The one entry I expect NOT to be closed is `premise_site_f_prefix_buoy_k`. A
       template whose prefix is a runtime value cannot be decided by reading, and
       accepting it is the defensible choice; I record it so a later tightening is a
       decision rather than a surprise.
```

## Findings

**R682. (BLOCKING -- (b), AND IT CARRIES INTO STEP 2 BY NAME.)
`F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05` IS DECLARED ABOVE THE SMALLEST DEFECT THE
GATE'S OWN INJECTION PRODUCES, AND THE MEASUREMENT QUOTED FOR IT IS IN A QUANTITY THE
ASSERTION NEVER COMPUTES.** `floatfea/tolerances.py` (the
`F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` entry) and `docs/milestones/F4.md:346` both state
"the measured worst over all 16 members is 5.555556e-02", derived as
`(mu L^2 / 12) / (R L - w L^2 / 2)` = `6386718.75 / 114960937.5` = `1/18`; the assertion
message at `test_f4_static_and_mapping.py:552` repeats "which is 1/18 of the root moment on
a platform arm". The assertion divides by `abs(mf.end_a[4])`, and under R663's formula that
is the correct root PLUS `mu L^2/12` -- measured `121347656.25000013` against a correct
`114960937.50000009` -- so the ratio is exactly `1/19` on a platform arm and exactly `1/24`
on a hub arm. Measured over all sixteen members the ceiling covers: four platform arms at
`5.263157894736891e-02`, **twelve hub arms at `4.166666666666627e-02`, which is BELOW the
declared counter**. No member reads `5.555556e-02`. The counter-case passes only because it
injects into `body.members[0]` of the platform, the easiest of the sixteen. Counter boundary
solved by substitution: `0.06` reddens
`test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula`, `0.05` holds, `0.04` leaves only
the plan pin -- so the measured margin is **5.26%**, not the 11.1% the quoted figure
implies, and the plan row's bracket `1.0550e+14x` measures `9.9950e+13` against the member
injected and `7.9127e+13` against the worst member. The recorded guard is explicit: a
counter is "the smallest defect the same assertion, in the same quantity, detects", and a
gate whose sensitivity degraded into `[0.0417, 0.05)` would pass its own bracket while
missing this defect on twelve of sixteen members. **THE CEILING IS NOT THE FINDING** --
`1.0e-12` is accepted, R681's form question is answered, and I say so.
**Closed when** the counter is declared below `4.166666666666627e-02`, the smallest ratio
R663's formula produces over the sixteen members the ceiling loops over, with that figure
and the `1/19` and `1/24` derivations pasted and the denominator named (the defect's own
root moment, not the correct one); AND the three sites that carry `5.555556e-02` or `1/18`
are each closed site by site -- the tolerance entry, `F4.md:346` including its
`1.0550e+14x`, and the assertion message at `:552` -- or the site is named and the reason
it was left is given. If the counter is instead kept at `0.05` with the counter-case still
injecting into one platform arm, the entry says that it is a bound about that one member
and not about the sixteen, which is a different claim from the one written now.

**R683. (BLOCKING -- (c), AND IT CARRIES INTO STEP 2 BY NAME.) NOTHING IN THE TREE HOLDS
R679'S PER-BODY RESIDUAL IN PLACE: REVERT THE WHOLE FIX AND THE SUITE STAYS GREEN.**
`grep -rn "internal_joint_dropped"` over the repository returns nothing, and the
parametrisation at `test_f4_static_and_mapping.py:830` is still
`["sign_not_flipped", "wrong_node_same_body"]`, unchanged from the commit R679 was raised
against -- so the invocation's claim that "a new counter-case parametrisation
`internal_joint_dropped` is in the file so the aggregate cannot return" is false. Measured,
with the lam row, the `nodes` map and the expected side held and only the normalisation
scope moved: both shipped counter-cases are RED under the aggregate form as well
(`9.202049e-01` and `2.437483e-01`) as under the per-body form (`3.556962e+00` and
`9.597086e-01`), and the clean case is green under both (`1.872582e-16` / `2.196224e-16`).
The two shapes that distinguish the forms are the ones not in the file: a mapper dropping
one hub-platform joint reads `1.778481e+00` per body and `1.872582e-16` aggregate, and
dropping all four reads `1.635665e+00` per body and `9.362910e-17` aggregate. This is the
second half of R679's own closing condition, which asked for "both counter-cases plus the
two dropped-joint shapes above re-measured and pasted per body". "A gate carries its own
failure": break the claimed property and confirm the assertion goes red -- the claimed
property is now per body, and breaking it goes nowhere.
**Closed when** an injection that omits a hub-platform joint from the mapper is
parametrised into the G4.4 counter-case (or stands as its own test), asserting
`> F4_MAPPING_CONSERVATION` on the per-body error, with `1.778481e+00` and `1.635665e+00`
reproduced and the aggregate's `1.872582e-16` and `9.362910e-17` recorded beside them as
what the case exists to prevent; and the per-body breakdown pasted, because
`hub2 1.795e-16 hub3 2.093e-16 hub4 1.635e-16` on the one-joint shape is the evidence that
the residual localises to the two bodies the joint touches.

**R684. (BLOCKING -- (c), AND IT CARRIES INTO STEP 2 BY NAME. THE PREMISE IT RESTS ON WAS
MINE AND I WITHDRAW IT.) `_one_body_error`'S NEW ASSERTION MAKES THE MAPPING GATE RAISE ON
A LEGAL SPARSE MULTIPLIER ROW, AND ITS MESSAGE'S STATED REASON IS FALSE.**
`test_f4_static_and_mapping.py` `_one_body_error` replaces the `max(..., 1.0)` floor with
`assert f_scale > 0.0 and m_scale > 0.0`, whose message reads "For a nonzero multiplier row
no body can have a zero resultant -- every one of the five carries at least one joint".
Measured: a multiplier row whose only nonzero block is the joint `('buoy1','buoy1','hub1')`
has `||lam|| = 1.912540e+06` and leaves `platform`, `hub2`, `hub3` and `hub4` with
identically zero expected resultants, so the gate raises `AssertionError` instead of
measuring; a row carrying only `('hub4','hub4','platform')` does the same to `hub1`, `hub2`
and `hub3`. The second half of the premise is true -- every body does carry at least one
joint -- and the conclusion does not follow from it, because a row may be nonzero overall
and zero in a given body's blocks, which is what a load case with reaction at some joints
and not others looks like. **LATENT TODAY**: the gate is only ever handed `_synthetic_lam`,
which I measured nonzero in all 16 of 16 blocks, and the rung reads `153 collected, 0
failed, 0 errored, 0 skipped`. The floor's REMOVAL is a strengthening and is not the
finding -- the per-body scales measure `1.157232e+06` to `5.281836e+06` (force) and
`4.182033e+07` to `3.182e+08` (moment), so it never bound.
**C158's closing condition said "the quantity cannot be zero for a nonzero lam row, which
is assertable". That sentence is mine, I wrote it from reasoning without taking the
measurement, and it is wrong** -- "convert arguments into measurements", and this is the
round where my own argument was the one that had not been.
**Closed when** a body whose expected resultant is identically zero no longer makes the
gate raise -- the natural form is an absolute comparison against zero for that body plus an
assertion on the COUNT of bodies compared, which is the four-gates pattern this file already
uses, so a sparse row reduces coverage visibly rather than erroring -- and the false
sentence in the message is deleted rather than rephrased. **OR**, equally acceptable to me:
`_mapping_error` declares that its domain is a dense row, asserts that, and says so -- but
then the assertion is about the INPUT and the message must not claim it is about the
physics.

**R685. (BLOCKING -- (b), AND IT CARRIES INTO STEP 2 BY NAME.) THE `F4_MAPPING_CONSERVATION`
ENTRIES REPUBLISH FOUR FIGURES MEASURED AGAINST THE AGGREGATE RESIDUAL THAT THE SAME COMMIT
DELETED.** `floatfea/tolerances.py`, the `F4_MAPPING_CONSERVATION` and
`F4_MAPPING_CONSERVATION_COUNTER` entries, in `ecace4a` -- the commit that replaced the
aggregate six-vector residual with the per-body one. Measured at `84de436` under the rule
that shipped: the clean value is `2.196224e-16` and the margin `4553x`, where the entry says
`1.8726e-16` and `5341x`; the wrong-node injection's force channel is EXACTLY
`0.000000e+00` and its moment channel `9.597086e-01`, where the entry says
`5.2050529737194385e-17` and `0.24374825705420716`; "Reason for 0.2 ... which MEASURES
0.24374825705420716" measures `9.597086e-01`; "the other injection ... reads
0.9202048893902944" measures `3.556962e+00`, and that injection's force channel is
`3.556962e+00` rather than round-off. The ordering claim the counter rests on -- "the
wrong-node defect is the smaller of the two" -- SURVIVES, `0.96 < 3.56`, and I say so. The
consequence, solved rather than asserted: the wrong-node injection may now be scaled down
to `0.209` before `error > F4_MAPPING_CONSERVATION_COUNTER` fails (`0.21` reads
`2.015388e-01` and holds, `0.208` reads `1.996194e-01` and fails), a **79%** weakening
window where verdict 95 measured **18%** on the aggregate. `CLAUDE.md` BP0: "when a decision
rule changes, every figure citing the old rule is regenerated or withdrawn in the same
commit. Not the next one, and not when someone notices." **I am NOT asking the value `0.2`
to move** -- a counter below its measurement demands less of the gate than the gate
delivers, which is the harmless direction -- and I class this as (b) rather than as a figure
under the instruction that says to: these comments are the only statement of what the
counter is a bound below, and a reader solving the boundary from the entry as published
would conclude 18% where the tree gives 79%.
**Closed when** the four figures are re-taken under the per-body rule or withdrawn, the
`5341x` recomputed, and the weakening window stated as the measured `79%`; and the sentence
"a block moved to the wrong node of the right body leaves the force at
5.2050529737194385e-17" is replaced by the per-body figure, which makes its own causal point
more strongly.

## Closure items

Not re-reviewed item by item (CZ0). **C135, C136, C138, C139, C140, C142, C149, C150, C152,
C153, C155, C156, C157, C159 and C160 are CLOSED by `ecace4a`** -- I read each diff hunk and
each is what it claims to be. **C154 is CLOSED by `84de436` and I measured it (Â§ 10).**
**C137, C141, C144, C145, C147, C148 and C151 are DEFERRED into step 2's first report under
EK3, and the mechanism that forced the deferral is verified (Â§ 10), so I am not asking for
them back.** New this round:

* **C161.** `tests/verification/rung4/test_f4_static_and_mapping.py:817` -- a dead
  assignment: `error = _mapping_error(built, loads, want)` is immediately overwritten by
  `error = max(per_body.values())` two lines later, so the gate computes its residual twice
  and discards one. Harmless, and `ruff` does not see it. Closes when the first line goes.
* **C162.** `floatfea/tolerances.py`, the `F4_STATIC_TIP_MOMENT_RELATIVE` entry -- "BOTH
  EDGES SOLVED (EH4): tightened, the clean case trips below 1e-15" BRACKETS the boundary
  rather than solving it. Measured: at ceilings of `1.0e-15`, `1.0e-14` and `1.0e-13` the
  clean case PASSES and only the plan pin objects; it trips at `5.265785810941744e-16` or
  below, which is the clean worst itself. Closes when the sentence carries the solved
  boundary. EH4 asks for the boundary, not a sample on one side of it.
* **C163.** `test_f4_static_and_mapping.py`, `_premise_violations` and `_BUOY_LABEL` --
  C160's edit moved one half in the WEAKENING direction and no sentence records it:
  `f"BUOY{k+1}"` reddened under the pre-C160 bare-substring form (verdict 95 measured it
  among "ALL REDDEN -- fails safe") and PASSES now, because `re.IGNORECASE` applies to the
  buoy half as well as to the FE-body half. The new semantics are RIGHT -- a buoy label in
  another case is a buoy label -- so this is a disclosure item and not a defect. Closes
  when the docstring says the buoy half is case-insensitive and therefore accepts
  spellings the old form refused.
* **C164.** `test_f4_static_and_mapping.py`, `_BUOY_LABEL` -- `f"{prefix}buoy{k}"` passes
  `_premise_violations` (measured, 0 violations), because a closing brace is a word
  boundary, so an arbitrary runtime prefix satisfies the anchor. I expect this one NOT to
  be closed and I record it so a later tightening is a decision rather than a surprise: a
  template whose prefix is a runtime value cannot be decided by reading. Closes when the
  docstring says the check is about literal label SHAPES and that a computed prefix is
  outside it.
* **C165.** `test_f4_static_and_mapping.py:552`, the assertion message's "which is 1/18 of
  the root moment on a platform arm" -- measured `1/19`, for the reason in R682. Listed
  separately because R682's closing condition names three sites and this is the one a
  reader of a FAILING run sees. CW0.
* **C166.** Seven stale `suite-count-*` worktree registrations, flagged in the invocation.
  Not a code finding and I agree it is not one. `git worktree prune` cannot remove them
  because of a Windows permission on pack files; `git worktree remove --force` on each, or
  deleting `.git/worktrees/<name>` by hand, is the usual way out. They are registered
  against this repository and `_real_git_dir_into` now copies them into every scratch build
  of the guard harness, which is harmless but is a reason to clear them. Closes when
  `git worktree list` shows only the real checkouts.

## Carried

Verdict 95 named **three blocking items carrying into step 2**, nine new closure items on
top of C135-C151, and a `Next step opens when` list. Every one, with its status and where.

* **R679 -- ANSWERED ON ITS SUBSTANCE, AND HALF-ANSWERED ON ITS CLOSING CONDITION. R683 IS
  THE REMAINDER AND IT CARRIES INTO STEP 2 BY NAME.** `_resultants` and
  `_expected_resultants` return per-body dicts, `_body_errors` normalises each separately,
  the assertion prints the per-body breakdown, and the plan's own "per body and per source"
  is the quantity. I reproduced `1.778481e+00` and `1.635665e+00` against my `1.778500e+00`
  and `1.635700e+00` -- my figures to beat are beaten (Â§ 3). What is NOT done is the second
  clause: "both counter-cases plus the two dropped-joint shapes above re-measured and
  pasted per body". The dropped-joint shapes are absent and the fix is unprotected (Â§ 4).
* **R680 -- ANSWERED, and I checked the pair rather than the line.** `body.material.rho *
  member.section.A * span * GRAVITY_MAGNITUDE`; `material` is per body and `section` per
  member, so this is the member's own prismatic mass. The false-redden I measured
  (`1.532812e+06 N` against `1.686094e+06 N` with one member 10% longer) is gone. The
  worst old-against-new gap today is `1.898721e-16` on five hub arms, so the fix removes a
  wrong answer that was waiting for an unequal frame rather than a wrong number now. The
  docstring clause of the condition -- "say which of the three it actually reads" -- is in
  the rewritten comment.
* **R681 -- ANSWERED ON THE FORM, WHICH IS WHAT IT WAS ABOUT. R682 IS NEW AND IT CARRIES
  INTO STEP 2 BY NAME.** `F4_STATIC_TIP_MOMENT_N_M = 1.0` is gone with no stale reference
  anywhere, replaced by `F4_STATIC_TIP_MOMENT_RELATIVE = 1.0e-12`, dimensionless, against
  the member's own root moment -- which is the denominator I said was two lines above the
  assertion, and it is. The "nothing to be relative to" sentence is DELETED rather than
  rephrased, which the condition asked for in those words. The counter that came with it is
  R682 (Â§ 5), and the entry's EH4 sentence is C162.
* **C135, C136, C138, C139, C140, C142, C149, C150, C152, C153, C155, C156, C157, C159,
  C160 -- CLOSED by `ecace4a`; C154 -- CLOSED by `84de436`.** Read hunk by hunk, not
  re-reviewed item by item (CZ0). Four of them changed gate behaviour and I attacked those
  four as asked: C152 and C157 accepted (Â§ 9), C160 accepted with C163 and C164 recorded,
  C158 is R684. C153's routing -- the figures move to the step report and the entry keeps a
  pointer -- **DOES satisfy BI3 and I answer the implementer's question directly**: BI3's
  two permitted forms are "a committed script produces the table at the commit that
  publishes it" or "the table belongs in the step report, which is regenerated by rule, and
  the entry carries the single number it needs and a pointer". This is the second form
  exactly. It does not merely move unpinned prose, because the step report IS regenerated
  and a tolerance comment is not.
* **C137, C141, C144, C145, C147, C148, C151 -- DEFERRED to step 2's first report (EK3),
  and the deferral is justified.** I reproduced the mechanism myself: a commit touching
  `docs/reports/F4/step-1.md` after the step's final verdict reddens 8 states, content
  irrelevant (Â§ 10). **They carry into step 2 as closure items, not as blocking items.**
* **R653 -- OPEN, UNCHANGED, AND IT BECOMES (c) AT STEP 2.** `grep -rn RHO_INF` over
  `tests` and `floatfea` still returns nothing at `84de436`. **Carries by name.**
* **R656 -- OPEN WITH XABIER, unchanged.** Nothing in this range touches the ledger
  question. `scripts/ci_section.py` is untouched in the range.
* **R638 -- OPEN, unchanged, EJ1 governs, closed before F4 closes.** `docs/closure/F3.md`
  carries it at Â§ 4a and Â§ 391. Nothing in this range touches its site.
* **R637 clause (iii) -- ANSWERED at verdict 95 and NOT reopened**, and the environment
  that made its figure disagree is now repaired (C154 closed), so the next
  `scripts/suite_count.py` run will not reproduce the `1 failed` the report explained.
* **R622, R626, R631, R635 -- carried on the EJ3 ledger at `docs/closure/F3.md` Â§ 8,
  unchanged and not re-reviewed (CZ0).**
* **The EJ4 residual-location hand-over -- unchanged, live at step 2**, where `3.96e-06`
  is the reference.
* **R657, R658, C119, R659, R660, R661, R662, R654, R655 -- CLOSED at verdict 93, not
  reopened.** Nothing in this range touches their sites.
* **Verdict 95's `Next step opens when`, item by item.** R679 -- **ANSWERED on substance,
  remainder R683**. R680 -- **ANSWERED**. R681 -- **ANSWERED on form, counter is R682**.
  The closure list -- **ABSORBED**, fifteen closed plus C154, seven deferred under EK3 with
  the mechanism measured. R653 -- **STILL OPEN and still carried**.
* **What I said I would not accept, and whether it was offered.** A ceiling widened to
  rescue anything -- **NOT OFFERED**; no existing value moved and I swept the two new ones
  in both directions. A counter in a different quantity from its ceiling -- **OFFERED, and
  it is R682**: the ceiling is a ratio to the member's own root moment and the counter's
  stated measurement is a ratio to a different root moment. A gate exempted or a guard
  extended -- **NOT OFFERED**; `test_tolerance_counter_cases.py` and
  `test_no_tolerance_literals.py` are both untouched across the range. A skip standing in
  for a gate -- **NOT OFFERED**; `0 skipped` in the rung and in my full run. An edit to my
  own instructions -- **NOT OFFERED**; `git diff` over `.claude` and `docs/SUPERVISOR.md`
  is empty and I ran it myself.

## Tolerances touched

**ONE PAIR RENAMED WITH ITS FORM CHANGED, THREE COMMENTS CORRECTED, NO EXISTING VALUE
MOVED.** I diffed the file separately per my instruction 4, because that is where the
cheapest wrong fix lands, and I read all 43 inserted lines.

| constant | old | new | form | counter | injected by | my judgement |
|---|---|---|---|---|---|---|
| `F4_STATIC_TIP_MOMENT_N_M` | `1.0` | **DELETED** | was N*m, absolute on a dimensional quantity | was `..._COUNTER = 6386718.75` | was `test_EO1_...` | **R681 ANSWERED.** Gone with no stale reference: `grep -rn F4_STATIC_TIP_MOMENT_N_M` over `floatfea tests scripts docs/milestones` is empty. |
| `F4_STATIC_TIP_MOMENT_RELATIVE` | none | `1.0e-12` | **dimensionless, relative to the member's own root moment** | `..._COUNTER = 0.05` | `test_EO1_static_member_forces_match_STATICS_not_the_model` / `..._REDDENS_on_the_R663_formula` | **VALUE AND FORM ACCEPTED.** Clean worst over all 16 members `5.265785810941744e-16` on `platform:hub4_arm`, `1899x` of room, which I re-measured rather than carrying. Boundary solved both ways: clean trips at a ceiling of `5.265785810941744e-16`; the ceiling may rise to `5.263157894736842e-02` before the counter-case stops holding. The EH4 sentence is C162. |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | none | `0.05` | dimensionless | is the counter | the same test | **R682 -- THE DECLARED VALUE SITS ABOVE THE DEFECT ON TWELVE OF SIXTEEN MEMBERS AND THE MEASUREMENT QUOTED FOR IT IS IN THE WRONG QUANTITY.** Measured `1/19` = `5.263157894736842e-02` on the four platform arms and `1/24` = `4.166666666666627e-02` on the twelve hub arms, against a quoted `5.555556e-02` that no member reads. Margin 5.26%, not 11.1%. Boundary: `0.06` reddens the counter-case, `0.04` leaves the plan pin alone. |
| `F4_STATIC_REACTION_AGREEMENT_COUNTER` | `0.25` | `0.25` | dimensionless | is the counter | `test_G4_the_defective_formula_misses_the_reaction_by_a_quarter` | **UNCHANGED IN VALUE; C149's comment correction ACCEPTED.** "the platform value is the TIGHTER of the two" was wrong -- `0.2069 < 0.25` -- and the replacement says the platform value is declared because it is the member the counter-case injects into, which is the reason that actually holds. I checked the inequality direction myself. |
| `F4_STATIC_SYMMETRY_SPREAD_COUNTER` | `1.5` | `1.5` | dimensionless | is the counter | `test_EK0d_the_symmetry_gate_REDDENS_on_an_unsymmetric_frame` | **UNCHANGED IN VALUE; C153's pointer ACCEPTED and it satisfies BI3** (see `Carried`). The figures move to the report, which is regenerated by rule; the entry keeps the one value plus the pointer, which is BI3's second permitted form verbatim. |
| `F4_MAPPING_CONSERVATION` | `1.0e-12` | `1.0e-12` | dimensionless, relative, force and moment normalised separately, **now PER BODY** | `..._COUNTER = 0.2` | `test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node` | **VALUE AND FORM ACCEPTED, AND THE QUANTITY IS NOW RIGHT (R679).** Clean per body `2.196224e-16`, `4553x` of room. **R685: the entry's four figures are the AGGREGATE's and were republished unchanged in the commit that deleted the aggregate.** |
| `F4_MAPPING_CONSERVATION_COUNTER` | `0.2` | `0.2` | dimensionless | is the counter | the same test | **VALUE ACCEPTED, and I say explicitly that I am not asking it to move.** Under the per-body rule the wrong-node injection measures `9.597086e-01`, so `0.2` demands LESS than the gate delivers -- the safe direction. Its justification is R685: the weakening window is a measured 79%, not the 18% the entry's figures imply. |

```
cmd    git diff 9f75cd5..HEAD -- floatfea/tolerances.py      [separately, instruction 4]
out    43 insertions, 18 deletions. Every deletion is a comment line or one of the two
out    deleted declarations. NO SURVIVING VALUE MOVED.
cmd    grep -n "^F4_" floatfea/tolerances.py | wc -l ; and the plan's section 5a rows
out    12 constants, and `docs/milestones/F4.md` section 5a lists 12 rows
cmd    perturb each of the two new constants and run tests/test_plan_matches_tolerances.py
out    ceiling 1.0e-11 / 1.0e-13 / 1.0e-15 -> FAILED [F4.md-345-F4_STATIC_TIP_MOMENT_
out      RELATIVE-1.0e-12] ; counter 0.04 / 0.06 -> FAILED [F4.md-346-..._COUNTER-0.05]
rule   every numerical tolerance lives in floatfea/tolerances.py and moves with a plan edit
judge  **THE PLAN EDIT IS REAL AND CORRECTLY PAIRED IN THE SAME COMMIT**, the pin is live
       in both directions on both new rows, and I moved each rather than reading the table.
       The one thing I would not have accepted -- a value moved to make something agree --
       was not offered, and the rename is a form correction forced by my own finding.
```

## On the criterion, and on being asked whether the fix belonged here

I was asked to say if I disagree with *the criterion* rather than with the work. **I do
not, and I want one observation on the record rather than as a round.**

Reviewing a closure commit is not a fourth round and I have not treated it as one: step 1's
disposition is read from its closure verdict (DD1), that verdict is PASS, and nothing here
reopens it. The four findings are blocking-class items about the TREE and they carry by name
into step 2, which is the container CZ0 provides and the one verdict 95 already used.

**The observation is that this round found four blocking items in a commit the process does
not review, and three of them are inside repairs made to answer blocking items.** That is
CZ1's own thesis measured a second time, and it suggests the gap CZ1 names is not fully
closed by CZ1's four steps: (ii) and (iii) measure whether the closure commit is GREEN, and
all four findings here are in a tree that is green on three machines. A green suite cannot
see a counter declared on the wrong side of its own defect, a decision rule nothing holds in
place, or a figure whose rule moved underneath it. **I am not asking for new apparatus --
"no new apparatus through F6" and I agree with it.** What I am recording is that the reading
is the mechanism, and that a closure commit which fixes blocking items has now twice been
the highest-yield thing I read this milestone. If Xabier wants a rule out of it, the cheap
one is: a closure commit that changes a GATE or a TOLERANCE, as opposed to prose, is
reviewed; one that changes only prose is not. That is a question for him and not a round.

## On the schedule

No report in this range, so there is no hand-written schedule paragraph to read and I am not
asking for one retroactively. The dates stand as revision 3 left them: EK4's preview held
three days early, step 1 closed on verdict 95, no slippage reported. **What I record for
CZ0's escalation clause is the exposure, because it has grown**: step 2 now opens carrying
**six items -- R682, R683, R684, R685, R653 and R679's remainder** (R683 IS that remainder,
so five distinct), four of which are blocking and none of which needs new apparatus or a
design decision. That is four blocking items to answer before step 2's own work is read.
CZ0's clause is "if two consecutive steps close carrying blocking items, that is escalated
with the choice stated -- slip the date, or reduce scope." Step 1 closed carrying three. If
step 2 closes carrying any, the clause fires, and the report paragraph is where it gets
stated the day it is known rather than when the step closes.

## Next step opens when

**IT IS ALREADY OPEN.** Step 1 closed PASS at verdict 95 and this verdict does not reopen
it (DD1). The closure commit stands: CI green at job and step level at its own sha, my own
single-invocation run 3022 passed / 0 failed / 0 skipped, lint green, rung 4 `153 collected,
0 failed, 0 errored, 0 skipped`, my own instructions untouched, no conftest touched, no
value widened. **Step 2 may be worked now.** What follows is what step 2's FIRST report
answers before its own work is read, and each is specific:

1. **R682** -- the tip-moment counter declared below `4.166666666666627e-02`, or the entry
   stating that it is a bound about one platform arm and not about the sixteen; and all
   three sites carrying `5.555556e-02` or `1/18` closed site by site (the tolerance entry,
   `F4.md:346` with its `1.0550e+14x`, the assertion message at `:552`), or each named with
   the reason it was left. My figures to beat: `1/19` and `1/24`, exactly.
2. **R683** -- a dropped-internal-joint injection parametrised into the G4.4 counter-case,
   asserting on the per-body error, with `1.778481e+00` and `1.635665e+00` reproduced and
   the aggregate's `1.872582e-16` and `9.362910e-17` beside them. The test I would write is
   described; I do not write it.
3. **R684** -- the sparse-row raise removed or the gate's domain declared and asserted, and
   the false sentence in the message deleted rather than rephrased. **The premise was mine
   and the withdrawal is on the record above**, so an answer that says "the reviewer's
   closing condition was wrong" is a correct answer and I will accept it in those words.
4. **R685** -- the four mapping figures re-taken under the per-body rule or withdrawn, the
   `5341x` recomputed, and the weakening window stated as the measured `79%`.
5. **R653** -- unchanged, and it becomes (c) at step 2 as verdict 95 said it would.
6. **C161 to C166, plus C137/C141/C144/C145/C147/C148/C151** -- the closure list step 2
   absorbs once. Not re-reviewed item by item, and none of them holds step 2.
7. **CZ1 (ii), the half no verdict in this milestone had measured until now** -- this
   verdict commit creates EG3 state (2): a verdict written, no answering report yet. The
   expected reds at the verdict commit are the eight EH1 names
   (`test_every_named_site_is_touched_or_declared`, `test_the_report_carries_the_finding`,
   `test_the_CI_section_is_about_the_REVIEWED_commit`,
   `test_the_Carried_table_is_what_the_generator_produces`,
   `test_the_generator_would_catch_a_row_under_the_wrong_number`,
   `test_the_answered_verdict_is_the_NEWEST_one`,
   `test_a_carried_row_points_at_a_section_that_discusses_it`) plus the cascade off a red
   baseline, **and nothing else**. I measure it at this commit and paste it; step 2's report
   clears it, and EG3's sharpening is that it clears BY THE ANSWERING REPORT and not by
   time. Any red outside that list at this commit is CZ1 (iv) unchanged and I will say so.

**What I will not accept at step 2 on these five.** The tip-moment counter left at `0.05`
with the entry still claiming a measurement over sixteen members -- the counter-case injects
into one and the entry must say which claim it is making. A counter-case for R683 that
injects into the EXPECTED side rather than into the mapper, because the mapper is what is
under test here. "It fails safe" offered as the reason R684 needs no change: a gate that
raises is not failing safe, it is failing uninterpretably, and a rung that errors is
indistinguishable from a rung that is broken. And a figure in any of the four answers that
is not in a `claim/cmd/out` triple taken AFTER the final edit (CP3) -- three of this round's
four findings are numbers that were correct when taken and described a tree that had moved,
which is the whole of why that rule exists.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 1
Reviewed commit: 9285a9fb5907ff6b31638877d0de687b7e4a83b0
Verdict: PASS
**Reviewed commit: `b0824d515fa702e3349bfff8f7864e87a8458b6e`** (HEAD of F3 at invocation,
pushed). My corpus commit `9285a9f` lands first, so the script's `Reviewed commit:` stamp
and the judged commit differ; DU1 says restate the judged one and this is it.
Tests: 3018 passed, 0 failed, 0 skipped   (MY OWN run, ONE invocation, no `--ignore`, no
deselection, no `-k`, in the repository itself with its GitHub origin, 670.45s. `grep -c
"^FAILED"` over the log gives 0. I did not accept a count from the report.)
**CI at the code commit: run `37412585625` at `a3b914d`, conclusion SUCCESS -- every job
and every step, `ladder 4 -- the loads are the loads: success`, `ladder 5: success`.**

## Round of 2026-10-05 -- NINETY-FIFTH verdict. F4 step 1, THIRD round of three.

**PASS, and the step closes here by CZ0.** All nine of the ninety-fourth verdict's blocking
items are answered and I verified each rather than accepting it: the rung is green on the
machine that gates the merge with no skip, the conservation ceiling is bracketed twice over,
the determinacy claim is withdrawn at both named sites, the weight gate is signed, three
plan gate rows and EB6's hub side ship with counter-cases, omission raises, and the
both-zero duality case raises. The suite I ran is 3018 passed, 0 failed -- from 39 failed.

**Three blocking items are open and they CARRY INTO STEP 2 BY NAME**, which is what CZ0
prescribes on the third round rather than a fourth. Two of them came from one question:
*every gate in this step is handed its wiring -- what happens when the wiring is wrong?*

* **R679** -- G4.4's residual is summed over all five bodies where the plan's own row says
  "per body and per source", and that aggregation makes it **identically blind to all four
  hub-platform joints being dropped from the mapper**: `3.745164e-16` against a `1.0e-12`
  ceiling. The per-body form reads `1.6357e+00` on the same mutation.
* **R680** -- R675's second half was fixed in one of its two places. `_analytic_static:474`
  still divides `member_mass` by `len(members)`, on the same premise the report itself
  measured to be FALSE, and on an unequal frame that gate **FALSE-REDDENS on a correct
  solve** by `9.0909e-02` against a `1.0e-12` ceiling.
* **R681** -- `F4_STATIC_TIP_MOMENT_N_M` is an absolute tolerance on a dimensional quantity
  and its stated reason is refuted by its own comment.

**The four things I was asked to attack first, ruled.** EK0(a)'s substitution is legitimate
and honestly stated (ruling 1). G4.4's builder-derived `joint_order` is not the whole of
what it misses, and the part that is not stated is R679 (ruling 2). The round-bound counter
form is RIGHT and I say why (ruling 3). The Â§ 16a four-way disagreement is **resolved, not
carried**: I reproduced it and the cause is the harness, not the tree (ruling 4).

## 1. THE DIFFS, EACH ONE SEPARATELY, AS MY INSTRUCTIONS ORDER THEM

```
cmd    git diff --stat de9a448..b0824d5 -- floatfea tests docs scripts data .github
out    buoy_centers_ref.json 86 (new), F4.md 12, preview 333, step-1-answers.json 150
out    (new), step-1.md 1178, joint_reactions.py 18, platform.py 42, member_forces.py 19,
out    static.py 12, tolerances.py 97, export_buoy_centers_ref.py 219 (new),
out    rung4/test_f4_static_and_mapping.py 699.  TWELVE files.
cmd    git diff --stat de9a448..b0824d5 -- floatfea/tolerances.py      [instruction 4]
out    93 insertions, 4 deletions -- three RENAMES and six NEW constants, read line by
out    line below. NO existing value moved.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"        [instruction 4c]
out    tests/conftest.py                                  -- the instruction is intact
cmd    git diff de9a448..b0824d5 -- tests/conftest.py "tests/**/conftest.py"
out    (no output) -- nothing the ladder gate reads was rewritten from a rung, and the
out    rung4 file adds no hookwrapper, no `pytest_ignore_collect` and no
out    `pytest_collection_modifyitems`. I read all 861 lines of it.
cmd    git diff de9a448..b0824d5 -- .claude docs/SUPERVISOR.md         [instruction 4b]
out    (no output) -- NO STOP-CLASS FINDING. My own instructions are untouched across the
out    whole range and I diffed them; nothing in the suite reads them.
cmd    grep -n "^Answers:" docs/reports/F4/step-1.md                   [instruction 1b]
out    367: Answers: verdict 93 @ 3a908fa      (revision 2, historical)
out    508: Answers: verdict 94 @ de9a448      (revision 3, the NEWEST)
judge  `de9a448` IS the newest verdict commit and `git log --oneline` puts it immediately
       before this round's range. The newest revision's header names the LATEST verdict,
       not a superseded one, so every `Carried` claim in it is about the right list. One
       comparison, made first.
cmd    git diff --stat a3b914d..b0824d5 -- floatfea tests scripts data .github docs/milestones
out    (no output) -- the code at `b0824d5` is BYTE-IDENTICAL to `a3b914d`, which is why
out    the green run at `a3b914d` describes the tree I am judging.
```

## 2. CI AT THE REVIEWED COMMIT (CA2), AND IT IS GREEN

```
cmd    gh run list --commit a3b914d73cc1b3ff38078f1fa2c6a32bb5269c91 --json ...
out    [{"conclusion":"success","databaseId":37412585625,"event":"push","status":"completed"}]
cmd    gh run view 37412585625 --json jobs -- job AND step level, with runnerName
out    JOB the verification ladder: success   [04:12:18Z -> 04:15:13Z]
out      ladder 1 success / 2 success / 3 success / 6 success
out      **ladder 4 -- the loads are the loads: success**
out      **ladder 5 -- independent confirmation: success**  (not skipped behind a red)
out    JOB lint, unit and guards: success    [04:12:18Z -> 04:23:26Z]
out      actionlint / ruff / black --check / mypy / unit tests  ALL success
out      **guards and meta-tests: success** -- SEEN TO HAVE RUN, which is CZ1 (iii)
out    JOB CI determinism -- leg: skipped ; ten legs agree: skipped
rule   CK2: the third state is `runner_name: ""`, NO steps, a two-second duration and the
       spending-limit annotation
judge  **NOT CK2 AND NOT A RED.** Both real jobs carry full step lists with real
       conclusions and three- and eleven-minute durations. `runnerName` reads null on
       every job in this account's API responses, including ones that plainly ran for
       eleven minutes, so I ruled on the step lists and durations rather than that field.
cmd    gh run list --commit b0824d515fa702e3349bfff8f7864e87a8458b6e --json ...
out    []
judge  `b0824d5` touches `docs/reports/**` only, which `.github/workflows/ci.yml`
       paths-ignores by design, and its code is byte-identical to `a3b914d` (section 1).
       Verdict 90's push-union ruling applies and the green run stands for this tree. I
       used full shas throughout; the short form returns `[]` silently for anything.
cmd    ruff check floatfea tests ; black --check floatfea tests ; mypy floatfea
out    All checks passed! / 97 files unchanged / no issues found in 35 source files
judge  run by me at `b0824d5`, not taken from the report.
```

## 3. R670 -- THE RUNG RUNS WITH NO SKIP, AND I CHECKED THE REFERENCE'S OWN DERIVATION

```
cmd    bash scripts/run_rung.sh full:tests/verification/rung4      [my own run, b0824d5]
out    run_rung: 150 collected, 0 failed, 0 errored, 0 skipped
out    run_rung: OK -- 1 director(y|ies) ran
rule   scripts/run_rung.sh:274-276 -- a rung with any skipped case exits FAIL
judge  the ninety-fourth verdict read `FAIL -- 2 skipped`, `137 collected`. It is 150 and
       0. **The shape I named is the shape that shipped**: the gate reads a committed
       fixture whose provenance is a checked-in blob sha, the export cannot reach it, and
       `_eb6_reference()` ASSERTS the file exists rather than skipping.
cmd    cd ../HSP-stable && git rev-parse HEAD:studies/platform-12buoy/platform_common.py
out    b8b8123904aff2b79785043255cb28fcc6527ab5   == the snapshot's recorded blob
cmd    git describe --tags
out    floatfea-ref-1                             == the snapshot's recorded tag
cmd    rebuild the 12 centres and the 4 hub positions BY HAND from CLUSTER_ARM_RADIUS=1.0
         (:33), CLUSTER_ANGLES_DEG=[0,90,180,270] (:34), cc.BUOY_ANGLES_DEG=[0,120,240]
         (cluster_common.py:47), cc.CLUSTER_RADIUS=0.5 (:44), Z_HUB_REF=0.4933695679797303
         (:102) and compare with data/platform/buoy_centers_ref.json
out    identical; hub z at full scale 24.668478398986515 == the built arm-tip z
judge  **THE REFERENCE IS RIGHT AND I CHECKED ITS DERIVATION INDEPENDENTLY OF THE
       IMPLEMENTATION**, which is the recorded guard. Two provenance weaknesses go to
       closure (C155, C156); neither makes the value wrong today.
cmd    permute the EXPORT -- `buoy_joint_nodes` -- once for each of the 66 label
         transpositions, against the PINNED SNAPSHOT this time
out    ALL 66 RED. minimum 30.982841873186896 m on buoy2-buoy4, 4 pairs at the minimum
rule   DQ9: at least 1e3x below the smallest transposition displacement, both edges
judge  the declared counter `30.982842` is STILL the true minimum over all 66 after the
       snapshot substitution, and I re-measured rather than carrying last round's figure.
       The ceiling binds at `31.0`; the clean worst is `0.0`, so DQ9's lower edge stays
       vacuous and the entry says so.
```

## 4. R671 -- THE CEILING IS BRACKETED, AND I SWEPT ALL SIX IN BOTH DIRECTIONS (EH4)

Every sweep below was run in a clone outside the OneDrive tree and restores
`floatfea/tolerances.py` afterwards; the shipped value is re-run first and last.

```
cmd    for v in ...; do substitute the constant, then pytest tests/verification/rung4
         tests/verification/rung3/test_tolerance_counter_cases.py
         tests/test_no_tolerance_literals.py tests/test_plan_matches_tolerances.py; done
out    F4_MEMBER_FORCE_CONSERVATION   1.0e-13 -> 434 passed (shipped)
out       5.0e-16 -> 2 failed  + test_G4_member_end_shears_sum_to_the_load_...  (clean trips)
out       1.0e-6  -> 1 failed  the plan pin only
out       0.4     -> 1 failed  the plan pin only
out       0.6     -> 2 failed  + test_the_ceiling_sits_below_its_counter_case[...]
out       1.0     -> 3 failed  + test_G4_the_conservation_gate_REDDENS_without_the_...
out       2.0     -> 3 failed  ; 1.0e+6 -> 3 failed
out    F4_STATIC_REACTION_AGREEMENT   1.0e-12 -> 434 ; 3.0e-16 -> 4 failed ; 0.249 -> plan
out       pin only ; 0.3 -> 3 failed (+ bracket + the quarter counter-case)
out    F4_EB6_POSITION_M              1.0e-6  -> 434 ; 1.0e-14 -> 2 failed ; 30.9 -> plan
out       pin only ; 31.0 -> 3 failed (+ bracket + the permuted counter-case)
out    F4_STATIC_TIP_MOMENT_N_M       1.0     -> 434 ; 1.0e-8 -> 2 failed ; 1.0e+6 -> plan
out       pin only ; 6386719.0 -> 3 failed (+ bracket + the analytic counter-case)
out    F4_STATIC_SYMMETRY_SPREAD      1.0e-12 -> 434 ; 9.0e-16 -> 2 failed ; 1.4 -> plan
out       pin only ; 1.6 -> 3 failed (+ bracket + the unsymmetric counter-case)
out    F4_MAPPING_CONSERVATION        1.0e-12 -> 434 ; 2.0e-16 -> 2 failed ; 0.19 -> plan
out       pin only ; 0.21 -> 2 failed (bracket) ; 0.3 -> 3 failed (+ the wrong-node case)
rule   EH4: a boundary is solved in BOTH directions, including the two that WEAKEN a gate
judge  **R671 IS ANSWERED AND I BROKE NOTHING TRYING.** `1.0e+6` now gives 3 failed, the
       number the report claims, reproduced exactly. The conservation ceiling is bounded
       twice: at `0.5` by the `_COUNTER` bracket the rename restored, and at `1.0` by the
       counter-case's new `relative > F4_MEMBER_FORCE_CONSERVATION`, which gets HARDER as
       the ceiling rises. **The carve-out premise is now correct for all six**: each
       counter is in its ceiling's own quantity and the ordering is asserted.
judge  The band between each ceiling and its counter is held by the plan pin alone --
       e.g. `F4_STATIC_SYMMETRY_SPREAD` reaches `1.4` with only
       `test_plan_matches_tolerances` objecting. That is the recorded discipline working
       as designed (a widening needs a plan edit in the same commit and that edit is what
       I read), and it is the same shape verdict 94 accepted. Not a finding.
judge  Nothing was widened, no entry was exempted, and `test_tolerance_counter_cases.py`
       was NOT extended -- `git diff` over it is empty across the whole range. The suffix
       that already works was the whole repair, exactly as I said it had to be.
```

## 5. TRY TO BREAK IT -- THE MAPPING GATE IS BLIND TO THE FOUR HUB JOINTS IT NAMES

This is the attack the implementer asked for and it went further than the report's own
statement of the limitation. The gate forms `_resultants` by summing force and moment
about the origin over **all five bodies into one 6-vector**, and compares with
`_expected_resultants` over the same `joint_order` and the same `nodes`.

```
cmd    a mapper variant that SKIPS joints, with the lam row, the nodes and the expected
         side all held, then `_mapping_error` exactly as the gate computes it
out    clean                                  1.872582e-16   GREEN
out    mapper drops ONE hub-platform joint    1.872582e-16   GREEN   (identical to clean)
out    mapper drops ALL FOUR hub-platform     3.745164e-16   GREEN
out    mapper drops ONE buoy joint            4.425295e-01   RED
out    mapper drops all 12 buoy joints        1.000000e+00   RED
cell   ONE VARIABLE MOVED: which joints the mapper iterates. Same lam row (seed 4), same
       `nodes`, same `_expected_resultants` over the full 16-entry `joint_order`.
rule   the gate asserts `error < F4_MAPPING_CONSERVATION` = 1.0e-12 and its own failure
       message says "Either a block was dropped, or a sign is on the wrong side, or a
       block landed on the wrong node"
judge  **A HUB-PLATFORM JOINT IS INTERNAL TO THE MODELLED SET, SO IT CONTRIBUTES
       IDENTICALLY ZERO TO A RESULTANT SUMMED OVER ALL FIVE BODIES.** The force cancels,
       and the hub centre and the platform arm tip are the SAME point -- I measured the
       gap as `0.000e+00` at all four -- so the moment cancels too. Four of the sixteen
       joints are outside this gate's reach, and they are DQ9's extension and half of
       EK0(e)'s subject.
cmd    the SAME residual normalised PER BODY, which is what F4.md section 5's G4.4 row
         says ("mapped total force and moment about a common point, PER BODY and per
         source"), with everything else held
out    clean                                  2.196e-16      GREEN
out    mapper drops ONE hub-platform joint    1.778500e+00   RED
out    mapper drops ALL FOUR                  1.635700e+00   RED
cell   ONE VARIABLE MOVED: the normalisation scope. Same mapper, same lam, same nodes.
judge  **THE AGGREGATION IS THE WHOLE DEFECT AND THE FIX IS THE PLAN'S OWN WORDING.**
       R679. And it is the shape `CLAUDE.md` names outright: "Never average a per-case
       diagnostic. An outlier hidden in a mean is the specific thing these diagnostics
       exist to catch."
cmd    and the mutations that ARE caught, so the finding is bounded
out    mapper omits the sign flip on the four hub joints ONLY   5.174e-01   RED
out    mapper writes force and leaves every moment row zero     9.513e-03   RED
out    mapper uses `nodes[(joint, body_a)]` for both sides      1.643e-01   RED
judge  so the blindness is specific to OMISSION of an internal joint, not to sign and not
       to an internal indexing slip. I say that rather than overstating it.
```

## 6. AND THE WIRING THE GATE IS HANDED IS OUTSIDE ITS REACH ENTIRELY

```
cmd    corrupt the `nodes` dict -- the driver's input -- and hand the SAME dict to both
         the mapper and the expected side, which is how a driver would do it
out    hub1 and hub2 arm tips transposed in `nodes`     3.224193e-16   GREEN
out    nodes[(hub1,"platform")] -> the platform CENTRE  1.791338e-16   GREEN
cmd    permute `joint_order` instead
out    hub1-platform and hub2-platform transposed      3.745164e-16   GREEN
out    two BUOY labels transposed in `joint_order`     2.922619e-16   GREEN
judge  The report states ONE of these -- "what this gate does NOT check: that
       `joint_order` matches the deck's". It does not state that the `nodes` map is
       equally outside the reach, and `nodes` is the only place the "which node" answer
       lives. I am NOT blocking on this half: the expected side is built from the lam
       blocks and the node coordinates, both independent of the mapper (EA4), and a gate
       cannot audit an input it must be told. What I am blocking on is the aggregation
       (R679), because that one hides a defect INSIDE the mapper. The input half goes to
       the corpus with its number, where it belongs.
judge  The honest statement of the gate's reach is: *a property of `map_joint_reactions`
       relative to the wiring it is handed, for the twelve joints with an unmodelled
       side.* The docstring says more than that today and the assertion message says more
       still. C152.
```

## 7. R675 WAS FIXED IN ONE OF ITS TWO PLACES

The report's Â§ 7 is the best section of this round: the implementer asserted the premise
I objected to, found it FALSE, and reported that the gate would have given a wrong answer
rather than a missed one. I verified the premise myself and it is false.

```
cmd    for each body, print every member's length and `rho A L`
out    platform  50.0, 50.0, 50.0, 50.0            rho A L  156250.0 x4
out    hub1      25.0, 25.0, 25.000000000000004    250000.0, 250000.0, 250000.00000000003
out    hub2      25.000000000000004, 25.000000000000007, 25.0
out    body average `member_mass / len(members)` = 250000.0 exactly
judge  one and two ulp out of the 120-degree geometry. The report's figures reproduce.
cmd    grep -rn "member_mass / len(" --include=*.py .
out    tests/verification/rung4/test_f4_static_and_mapping.py:95   (a comment, the fix)
out    tests/verification/rung4/test_f4_static_and_mapping.py:474  **STILL LIVE**
judge  **`_analytic_static:474` IS THE SAME DEFECT, IN THE GATE SHIPPED IN THE SAME
       COMMIT RANGE TO ANSWER R675.** `own_weight = body.member_mass / len(body.members)
       * GRAVITY_MAGNITUDE` is the expected side of
       `test_EO1_static_member_forces_match_STATICS_not_the_model` -- the gate the report
       calls "the one that reads the solve".
cmd    the discrepancy between that average and `rho A L`, and the ceiling it sits under
out    worst 2.328306e-16 on hub2:buoy6_arm against F4_STATIC_REACTION_AGREEMENT 1.0e-12
out    margin 4295x -- so it PASSES today
cmd    one platform member's length raised 10%, everything else held, same arithmetic
out    expected own weight 1.532812e+06 N where rho A L g is 1.686094e+06 N
out    relative error 9.0909e-02 against a 1.0e-12 ceiling
cell   ONE VARIABLE MOVED: one member's length. Sections, material, geometry, reactions
       and the solve all held.
judge  **FALSE-REDDENS ON A CORRECT SOLVE.** R680. "A closing condition that names sites
       is closed site by site" and "half of an item is not the item" -- and here the
       second site did not exist when the condition was written, which is why I state it
       as a new finding rather than as R675 unanswered. The fix is the same one line the
       other gate already took.
cmd    the other half of R675: the vacuous `continue`
out    `assert checked == 16` at :190, and `assert checked == 16` at :508, and
out    `assert checked == 12` / `== 4` on the two EB6 sides
judge  ANSWERED, and better than the condition asked -- four gates now assert their own
       comparison count, not one.
```

## 8. THE FOUR THINGS I WAS ASKED TO ATTACK, RULED ONE BY ONE

**RULING 1 -- EK0(a)'s substitution is LEGITIMATE and the limitation is stated honestly.**

```
cmd    read the gate, then feed `_premise_violations` thirteen site spellings it has
         never seen, including four designed to slip past it
out    'f"buoy{k+1}"'            0 violations  PASSES   (the real input -- correct)
out    'f"hub{c+1}"' '"platform"' '"HUB1"' '"Platform"' 'label' 'BODY_NAMES[k]'
out    'f"spar{k}"' 'f"BUOY{k+1}"' 'f"{name}"'          ALL REDDEN -- fails safe
out    'f"buoy{k+1}_PLATFORM"'   0 violations  PASSES   **MISS**
out    'f"buoyancy_body{k}"'     0 violations  PASSES   **MISS**
out    'f"deck_buoy{k}"'         0 violations  PASSES   **MISS**
rule   EK0(a): the per-body external hydrodynamic force on the 5 FE bodies is identically
       zero; report the max; STOP if nonzero
judge  **THE SUBSTITUTION IS SOUND.** EK0(a)'s own words ask for a sample and the report
       gives it (24,006 steps, `0.000000e+00 N`). The gate asserts the STRUCTURAL reason
       -- no excitation channel addresses a body that carries no `hydro_body_label` -- and
       a structural reason is STRONGER than a sample, not weaker, because a sample cannot
       exclude cancellation and this can. It runs in CI where the sample cannot, which is
       R670's lesson applied. The docstring states both what it asserts and what it does
       not catch, in those words, which is what I would have asked for.
judge  The three misses are the containment test, not the substitution: the FE-body check
       is case-sensitive while the buoy check is a bare substring, so
       `f"buoy{k+1}_PLATFORM"` -- the same shape as the counter-case's fourth entry,
       `"buoy1_and_platform"` -- passes on case alone. The gate's input today is
       `f"buoy{k + 1}"` from a pinned blob and is correct; the misses go to the corpus.
       Not blocking: a gate whose subject is one pinned blob is right about that blob.
```

**RULING 2 -- G4.4's builder-derived `joint_order` is ACCEPTABLE; what is not is the
aggregation, and that is R679.** Sections 5 and 6 carry the measurements. Building the
wiring from the builder so the gate needs no HSP worktree is the right call and is the
direct consequence of R670. Stating that it does not check the deck's order is the right
disclosure. But it is **not R675's defect in a new place** -- R675 was a false premise
hidden inside an expected value, and this is a stated boundary. R679 is a different
finding: the gate cannot see a defect INSIDE the subject it does claim.

**RULING 3 -- THE ROUND-BOUND COUNTER FORM IS RIGHT, AND `approx(rel=1.0e-9)` WAS WRONG.**

```
cmd    weaken the INJECTION rather than the ceiling (EH4's second direction), both new
         counters, and solve for where the counter assertion stops holding
out    symmetry: factor 0.01 -> 1.561652e+00 (>1.5 OK) ; 0.1 -> 1.123624e+00 (FAILS the
out      counter) ; so the injection may weaken from factor 0.01 to about 0.0106, no more
out    mapping:  scale 1.00 -> 2.437483e-01 (>0.2 OK) ; 0.82 -> 1.998736e-01 (FAILS the
out      counter) ; so the injection may weaken by 18%, no more
out    and in BOTH cases the CEILING assertion still reddens over the whole range, by
out      twelve decades
rule   the counter is the smallest defect the gate must still fail; the rung3 bracket
       asserts `ceiling < counter`
judge  **THE BOUND IS THE RIGHT FORM AND THE EQUALITY WAS THE WRONG ONE.** A counter is a
       statement about what the gate must still catch, and `>` is that statement; `==`
       pins a number the solve produces, which is a portability claim nobody wants to
       make about a BLAS summation order. `test_no_tolerance_literals` refusing
       `rel=1.0e-9` was right for a second reason: the window would itself have been an
       undeclared tolerance. The two places where equality IS used -- the EB6 counter
       (`approx(abs=F4_EB6_POSITION_M)`, a geometric length) and the tip-moment counter
       (`mu L^2/12 * g`, exact arithmetic) -- are the two where the number is NOT
       solve-derived, and that distinction is correct.
judge  What the bound loses, with its size: the measured figures in the two comments
       (`1.5616518375226505`, `0.24374825705420716`, and the four reactions) are now
       unpinned prose, and the windows are 4% and 18%. That is BI3's class and it goes to
       closure (C153), not to a block -- the alternative costs two more declared
       constants to pin two comments.
```

**RULING 4 -- THE Â§ 16a DISAGREEMENT IS RESOLVED. IT IS THE HARNESS, AND I FOUND THE
LINE.** The report says "I have not diagnosed it" and asks whether it may be carried. It
does not need to be carried, because it took one reproduction and one `ls`.

```
cmd    git worktree add --detach <scratch>/wt b0824d5, in a clone whose `origin` URL is
         the real GitHub one, then pytest tests/test_report_guard_states.py -q
out    1 failed, 22 passed in 80.11s (0:01:20)
out    FAILED test_the_guard_survives_the_state[guard_state_declared_GREEN_in_
out      REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]
out    E  subprocess.CalledProcessError: Command '[... 'commit', '-m', 'harness: the
out       report, re-committed with an older Answers sha']' returned non-zero exit 1
cmd    the same file in the clone WITHOUT a worktree, GitHub origin restored
out    23 passed in 141.85s        -- ONE VARIABLE MOVED: the origin URL
cmd    ls -la <scratch>/wt/.git ; cat it
out    -rw-r--r-- 169 bytes ; `gitdir: C:/.../sweep/.git/worktrees/wt`
out    python: Path(".git").is_dir() False   is_file() True
rule   tests/test_report_guard_states.py:434-440 -- `_build` loops over (".git", "tests",
       "docs", ...) and does `copytree` when `src.is_dir()` and `copy2` otherwise
judge  **IN A `git worktree`, `.git` IS A FILE HOLDING AN ABSOLUTE `gitdir:` POINTER**, so
       `_build` copies the pointer and every `git -C <scratch>/repo ...` in the harness
       operates on the ORIGINAL tree, where the plant was never written. Nothing is
       staged, `git commit` exits 1, and the ONE state that commits is the one that
       fails. The assertion never ran: the direction is "the harness could not build the
       plant", not "the tree is wrong".
judge  **So the four environments do not disagree about the tree.** The clone's seven are
       the remote (confirmed: 23 passed with the URL restored). The worktree's one is
       this. The repository and CI are green and so is my own full run. The implementer's
       instinct -- "the direction of its failure is the control did not behave" -- was
       right, and its caution about publishing a figure from the environment that
       disagrees was right too: `scripts/suite_count.py` builds exactly such a worktree,
       so the "excluded set: 270 passed, 1 failed" line IS this and nothing else.
judge  Routing: a harness whose LOCATOR misreads its input is EK2's explicit case and is
       repairable in a standalone `process:` commit -- resolve through
       `git rev-parse --git-common-dir`, or build the scratch repo with `git clone
       --local`. C154. **Not blocking**: it is a guard (CZ0), it is not red in the
       repository or in CI, and I have named the line.
```

## 9. THE REMAINING SIX ITEMS, EACH VERIFIED RATHER THAN ACCEPTED

```
cmd    R672: read floatfea/solve/static.py:20-30 at b0824d5
out    "the horizontal restraint's reactions are ZERO. **THIS MEASURES THAT THE APPLIED
out    LOAD IS PURELY VERTICAL, AND NOTHING ABOUT THE RESTRAINT.** The claim that stood
out    here ... is WITHDRAWN (R672)" and "no threshold is declared for it, so it is
out    reported and not asserted on"
judge  ANSWERED AT BOTH NAMED SITES. `static.py:21-23` is withdrawn in the words the
       measurement supports, report Â§ 3 CHECK 2 is amended IN PLACE (which is the right
       choice -- a reader who stops at Â§ 3 is the reader the claim misled), and the
       eight-DOF cell is published. I re-measured the clean platform reactions:
       `3065624.999999999, 3065625.0, 3065625.0, 3065625.000000002`. The withdrawal was
       the honest branch of the two I offered and the measurement is why.
cmd    R673: python -m pytest -q, one invocation, my own machine, b0824d5
out    3018 passed, 2 warnings in 670.45s ; grep -c "^FAILED" = 0
judge  ANSWERED. 39 -> 0, and the collected count rose by 174, so nothing was deselected
       to get there. No EG3 carve-out is needed because there is nothing to carve out.
cmd    R674: read the gate, then check the counter-case computes what the gate reads
out    gate: `expected = -(case.weight_N + handed)` ; `case.applied_N == approx(expected)`
out    counter: `applied = sum((body_mass_matrix(corrupt) @ accel)[uz])`
out    and selfweight.py:56-71 `gravity_load` IS `body_mass_matrix(body) @ accel`
judge  ANSWERED. The `abs()` is gone, the comparison is signed, and the counter-case's
       left-hand side is the SAME formula `solve_body_static` uses for `applied_N` --
       which I checked rather than assuming, because a counter-case that reimplements the
       quantity differently would be testing its own arithmetic. Both injections now
       corrupt the model (`replace(platform, remainder_mass=0.0)`; `accel = -accel`).
cmd    R676: python -m pytest tests/verification/rung4 -q -k "EK0d or G4_4 or EK0a"
out    10 passed, 140 deselected -- and I ran each gate's counter-case against my own
out    independent injection rather than the shipped one, in sections 5, 6 and 8
judge  ANSWERED for all four rows, with the reach qualifications in R679 and C152. The
       symmetry gate is the strongest of the three: clean `9.113860057399177e-16` against
       a `1.0e-12` ceiling, and a softening of one part in `1e9` still reads `4.0464e-10`
       -- 404x above the ceiling. I also injected a shape its author did not: one arm's
       `A` scaled by 0.99 and by 1.01, which moves mass AND stiffness, reads
       `2.503129e-03` and `2.496879e-03`, both RED.
cmd    R677: grep the signature
out    `f_eq_global: NDArray[np.float64]` -- no default; omission is a TypeError
judge  ANSWERED. "An unsupported case raises, it never defaults." The three counter-case
       call sites now pass `np.zeros(12)` explicitly, which is the statement I asked for.
cmd    R678: duality_residual(zeros, zeros)
out    ValueError -- "both shares are identically zero, so there is no duality to measure"
cmd    grep -rn duality_residual over floatfea and scripts
out    only its own module and the rung4 test -- no production caller to break
judge  ANSWERED. A satisfied law and an absent load can no longer print the same number.
```

## The adversarial corpus (BE3)

**Batch 34, committed separately at `9285a9f`:**
`tests/corpus/f4_mapping_wiring_and_premise_reach.txt`, **31 entries, all new**, on F4's
load-mapping gate and EB6's label-provenance gate -- EG4(e)'s two standing exceptions to
the corpus pause. Every `measured=` field was taken by me at `b0824d5`.

**COVERAGE, MEASURED AND NOT CLAIMED: of 31 new entries the step's shipped gates CATCH 11
and MISS 12; one produces a FALSE RED on a correct tree; 7 contradict a sentence shipped
beside the gate.**

```
cmd    a Counter of the expect field over the committed file
out    {'miss': 12, 'catch': 11, 'explain': 7, 'false_red': 1}  total 31
judge  Previous batches: 4 of 11, 8 of 13, 5 of 10, 5 of 17, 10 of 37. **11 of 31 is the
       best RATE of the milestone and it was earned by the step**, not by easier entries:
       every threshold mutation I could write now catches, which is what batch 33's 24
       misses were mostly about, so this batch had to find a new surface to attack.
judge  **THE NEW SURFACE IS THE WIRING AND IT IS WHERE THE MISSES CLUSTER.** Four of the
       twelve misses are the `nodes` map and `joint_order` handed to the mapper; two more
       are the two hub-platform omission shapes that became R679; two are the EB6 hub
       gate reading one side of the joint and dropping Z; three are the premise gate's
       string containment. Not one of the twelve is a threshold.
judge  The entry I would put in front of the implementer is
       `mapping_mapper_DROPS_ALL_FOUR_hub_platform_joints`: a mapper that injects nothing
       at all for the four joints EK0(e) and DQ9 are both about reads `3.745164e-16`
       against a `1.0e-12` ceiling, and the gate's own message says it catches a dropped
       block. The per-body form reads `1.6357e+00` on the same mutation. That is R679 and
       the corpus is where I found it.
judge  Last round I wrote that the step "now has instruments" and that six of nine
       findings came from moving their thresholds. This round every threshold held, so
       all three findings came from the inputs instead. That is the apparatus paying.
```

## Findings

**R679. (BLOCKING -- (c), AND IT CARRIES INTO STEP 2 BY NAME.) G4.4's GATE SUMS ITS
RESIDUAL OVER ALL FIVE BODIES, SO IT IS IDENTICALLY BLIND TO THE FOUR HUB-PLATFORM JOINTS
BEING DROPPED FROM THE MAPPER.** `tests/verification/rung4/test_f4_static_and_mapping.py`
`_resultants:642-654` accumulates one 6-vector over every body; `_mapping_error:686-698`
normalises that one vector. Measured in section 5, with the lam row, the `nodes` map and
the expected side held: a mapper that skips every joint whose `body_b` is `platform`
reads **`3.745164e-16`** against a `1.0e-12` ceiling, GREEN, and skipping one reads
`1.872582e-16` -- the clean value to every digit. The cause is physical and not a slip: a
hub-platform joint is internal to the modelled set, the force cancels, and the hub centre
and the platform arm tip are the SAME point (gap `0.000e+00` at all four), so the moment
cancels too. `docs/milestones/F4.md:310` specifies the quantity as "mapped total force and
moment about a common point, **per body** and per source", and the per-body form -- one
variable moved -- reads **`1.778500e+00`** for one dropped joint and `1.635700e+00` for all
four. `CLAUDE.md`: "Never average a per-case diagnostic."
**Closed when** `_mapping_error` is formed and normalised per body, with the plan's own
wording as the quantity, and both counter-cases plus the two dropped-joint shapes above
re-measured and pasted per body; and the gate's assertion message and docstring claim only
what the per-body form actually catches. My figures to beat: `1.778500e+00` and
`1.635700e+00` must stop reading as round-off.

**R680. (BLOCKING -- (c), AND IT CARRIES INTO STEP 2 BY NAME.) R675's BODY AVERAGE IS
STILL LIVE IN `_analytic_static:474`, WHICH IS THE EXPECTED SIDE OF THE GATE THE REPORT
CALLS "THE ONE THAT READS THE SOLVE".** `own_weight = body.member_mass /
len(body.members) * GRAVITY_MAGNITUDE`. The premise is exactly the one Â§ 7 of the report
measured and found FALSE -- `hub1`'s members are `25.0`, `25.0` and `25.000000000000004` m
-- and `grep -rn "member_mass / len("` over the tree returns this line and one comment and
nothing else. Measured: the average departs from `rho A L` by `2.328306e-16` at worst
today, which clears the `1.0e-12` ceiling by `4295x` and passes; with one platform member
10% longer and everything else held, the expected own weight is `1.532812e+06 N` where
`rho A L g` is `1.686094e+06 N`, a `9.0909e-02` relative error against a `1.0e-12` ceiling,
so `test_EO1_static_member_forces_match_STATICS_not_the_model` **FALSE-REDDENS on a correct
solve.** That is a wrong answer, not a missed one, which is the implementer's own wording
for why the other site had to change.
**Closed when** `_analytic_static` takes each element's own `rho * A * member.length`, the
same closed form line 105 already uses, with the clean worst re-measured; and the
docstring's "deck masses, `f`, geometry" says which of the three it actually reads.

**R681. (BLOCKING -- (b), AND IT CARRIES INTO STEP 2 BY NAME.) `F4_STATIC_TIP_MOMENT_N_M =
1.0` IS AN ABSOLUTE TOLERANCE ON A DIMENSIONAL QUANTITY AND ITS OWN COMMENT REFUTES THE
REASON GIVEN FOR IT.** `floatfea/tolerances.py:1966-1973` says "an absolute ceiling rather
than a relative one: the exact answer is zero and **there is nothing to be relative to**",
and the next sentence names "root moments of 1.15e+08 and 1.18e+08", which is the response
scale. The assertion at `test_f4_static_and_mapping.py:504` already computes
`mf.end_a[4]`, the same member's root moment, two lines above. Measured: the relative form
reads `5.1513e-16` clean and `5.5556e-02` for R663's defect -- a `1e14` bracket, wider than
the absolute form's `6.4e+06x`. And the unit-scaling test cannot be run to defend the
absolute form either way: `build_superstructure(froude_lambda=1.0)` RAISES
(`platform:hub1_arm: L/D = 0.400 is below 2`), so the quantity exists at exactly one scale
and the ceiling is a number about that one scale. The recorded guard is explicit -- "an
absolute tolerance on a dimensional quantity is a defect; accuracy tolerances are relative
to a stated response scale and dimensionless" -- and unlike `F4_EB6_POSITION_M`, which I
accepted last round because its natural denominator is `0.0` at a centre node, this one's
denominator is in the same loop. **The VALUE is not loose** (`1.0` N*m is `3.6e+07x` above
the measurement) and I say so; it is the form and the stated reason that fail.
**Closed when** the tip-moment ceiling is dimensionless against a stated response scale --
the member's own root moment is the obvious one -- with the clean worst, the defect and
both edges re-measured in that quantity, and the entry's "nothing to be relative to"
sentence deleted rather than rephrased. If the absolute form is kept instead, the entry
says which single scale it is a number about and why no relative form was available, and
that is a different claim from the one written now.

## Closure items

Not re-reviewed item by item. **C135 to C151 from verdicts 93 and 94 are still open and go
into the same list**, which the closure commit absorbs once (CZ0).

* **C152.** `test_f4_static_and_mapping.py:720` and `:734-735` -- the G4.4 docstring says
  the gate "catches a dropped joint, a sign on the wrong side, and a block on the wrong
  node" and the assertion message repeats it. Measured (sections 5 and 6): a dropped
  hub-platform joint reads `1.872582e-16`; a wrong node arriving through the `nodes` map
  reads `3.224193e-16`; a wrong `joint_order` reads `3.745164e-16`. Closes when both
  sentences name the reach the per-body fix (R679) actually has, and say that the wiring
  it is handed is outside it. CW0.
* **C153.** `floatfea/tolerances.py:2000-2012` and `:2033-2043` -- the measured figures
  `1.5616518375226505`, `0.24374825705420716`, `0.9202048893902944` and the four reactions
  `671905.5 / 5459344.5` are now unpinned prose: the ordering assertions admit a 4% and an
  18% weakening of the injections they describe (section 8, ruling 3). BI3's class. Closes
  when each figure is either regenerated by a committed script at the commit that
  publishes it, or moved to the step report with the entry carrying a pointer.
* **C154.** `tests/test_report_guard_states.py:434-440` -- `_build` treats `.git` as a
  directory, and in a `git worktree` it is a 169-byte file holding an absolute `gitdir:`
  pointer, so every `git -C <scratch>` in the harness operates on the original tree. One
  state (`..._REDDENS_CONTROL`) fails there for that reason and no other; reproduced in
  section 8 ruling 4. This is the environment `scripts/suite_count.py` uses to produce the
  excluded-set figure the report publishes. EK2's explicit case -- a LOCATOR misreading
  its input -- so repair it in a standalone `process:` commit citing EK2
  (`git rev-parse --git-common-dir`, or `git clone --local` for the scratch repo), or
  delete the state. Not an extension of the guard.
* **C155.** `scripts/export_buoy_centers_ref.py:43-48` -- `BUOY_ANGLES_DEG` is a module
  LITERAL and its docstring says it is "checked by `--check` like everything else". It is
  not: `check()` compares `build()` with the stored snapshot and `build()` uses the same
  literal, and the recorded blob sha is `platform_common.py`'s, so a move in
  `cluster-3buoy-rigid/cluster_common.py:47` changes neither side and `--check` prints
  "current". Verified the value is right today (`np.array([0.0, 120.0, 240.0])`). CW0.
  Closes when the sentence says which constants `--check` covers, or the fourth is parsed.
* **C156.** `scripts/export_buoy_centers_ref.py:80` -- `BUOY_RADIUS` is parsed from the
  trailing COMMENT on `platform_common.py:36` (`BUOY_RADIUS = cc.CLUSTER_RADIUS  # 0.5 m`),
  not from `cc.CLUSTER_RADIUS`. The comment and the constant agree today
  (`cluster_common.py:44`, `CLUSTER_RADIUS = 0.5`) and I checked. A comment that fell out
  of step would become the expected side of two gates with the blob sha unmoved. Closes
  when the value is parsed from where it is defined, or the limitation is stated where a
  reader of the snapshot will see it. Supersedes C146, which has moved here from the test.
* **C157.** `test_f4_static_and_mapping.py:399-424` -- the EB6 hub extension reads the
  PLATFORM's `platform:<hub>_arm_tip` node only, never the hub body's own node, and
  compares `got[:2]` against `expected[index][:2]`, dropping Z. Measured: exchanging the
  `hub1` and `hub2` body models leaves the hub gate at worst `0.0`, checked 4, GREEN (the
  buoy gate catches it incidentally at `70.71067811865476 m`); and the Z check is free --
  the snapshot's `24.668478398986515` equals the built arm-tip z to every digit. Closes
  when the norm is three-component and the hub body's own node is on one side of the
  comparison, or the docstring says which side of the joint the gate is about.
* **C158.** `test_f4_static_and_mapping.py:693-694` -- `_mapping_error` normalises by
  `max(float(np.max(np.abs(want[...]))), 1.0)`, a small-number guard written as a literal
  in a gate. `CLAUDE.md` names "small number guards" as tolerances under another name and
  `test_no_tolerance_literals` does not see this one. Measured: it never binds -- the
  scales are `4473165.687831473` and `318301929.1018349`. Closes when the floor is removed
  (the quantity cannot be zero for a nonzero lam row, which is assertable) or declared.
* **C159.** `test_f4_static_and_mapping.py:816-834` -- the EK0(a) docstring and the
  report's Â§ 8 claim "no body outside the twelve buoys carries a `hydro_body_label` in
  HSP-stable". The snapshot scans ONE file; `grep -rn` over HSP-stable finds assignments
  at `studies/platform-12buoy/platform_rao_pilot.py:152`,
  `studies/cluster-3buoy-rigid/cluster_rao.py:118` and `cluster_fin_fan.py:86`, none of
  them scanned. All three read `buoy{k + 1}`, so the SUBSTANCE holds; the sentence is
  about one file. Closes when it says so. CW0.
* **C160.** The three premise-gate misses in section 8 ruling 1: `f"buoy{k+1}_PLATFORM"`,
  `f"buoyancy_body{k}"` and `f"deck_buoy{k}"` all pass `_premise_violations`, the first
  because the FE-body check is case-sensitive while the buoy check is a bare substring --
  the same shape the counter-case's `"buoy1_and_platform"` entry exists to catch. Closes
  when both halves fold case, or when the docstring says the check is literal and
  case-sensitive about a pinned blob.

## Carried

Verdict 94 named **nine blocking items**, eight closure items (C144-C151), and a ten-item
`Next step opens when`. Every one, with its status and where.

* **R670 -- ANSWERED AND VERIFIED ON THE MACHINE THAT RAISED IT.** `ladder 4: success` and
  `ladder 5: success` in run `37412585625`; my own `bash scripts/run_rung.sh
  full:tests/verification/rung4` gives `150 collected, 0 failed, 0 errored, 0 skipped`,
  `OK`. The shape is the pinned snapshot with a checked-in blob sha, which is the first
  alternative I named; the export cannot reach it; `_eb6_reference()` asserts rather than
  skips. I verified the snapshot's derivation against HSP-stable by hand (section 3).
* **R671 -- ANSWERED.** Three counters renamed to `_COUNTER`, so `ceiling < counter` is
  asserted for each; the conservation counter-case's signature assertion now reads against
  the COUNTER and a new assertion compares the defect's error (`1.0` exactly) against the
  CEILING. My own sweep of all six ceilings, both directions, is in section 4: `1.0e+6`
  gives 3 failed. The rung3 guard was not extended -- `git diff` over it is empty.
* **R672 -- ANSWERED AT BOTH NAMED SITES, BY WITHDRAWAL.** `static.py:21-30` and report
  Â§ 3 CHECK 2, with the eight-DOF cell published. I re-measured the clean reactions.
* **R673 -- ANSWERED.** My own run: 3018 passed, 0 failed, 0 skipped, one invocation.
* **R674 -- ANSWERED.** Signed comparison; both counter-cases corrupt the model; and I
  checked that the counter-case's left-hand side is the same formula `applied_N` uses
  (`gravity_load` is `body_mass_matrix @ accel`), which is what makes it a test of the
  gate rather than of its own arithmetic.
* **R675 -- ANSWERED ON (a), AND ON (b) IN ONE OF TWO PLACES. R680 IS THE REMAINDER.** The
  count is asserted at four gates, not one. The conservation gate takes `rho A L`. The
  report found the premise FALSE by asserting it, which is better than the condition asked
  for and I say so. `_analytic_static:474` still divides by `len(members)`.
* **R676 -- ANSWERED FOR ALL FOUR ROWS**, with reach qualifications: R679 (blocking) and
  C152, C157. I ran each of the three new gates against injections its author did not
  write, in sections 5, 6 and 9.
* **R677 -- ANSWERED.** `f_eq_global` has no default; omission is a `TypeError`.
* **R678 -- ANSWERED.** `duality_residual` raises on a both-zero share; no production
  caller to break, which I checked.
* **C135 to C151 -- OPEN, absorbed in the closure commit, not re-reviewed (CZ0).** C146
  is superseded by C156, which is the same defect at its new site. C144, C145 and C147's
  figures are in revision 2 sections the implementer deliberately left standing and
  corrected in revision 3 instead; that is the right call for a reader following the
  verdict and I am not reopening it.
* **R656 -- OPEN WITH XABIER, unchanged.** `scripts/ci_section.py` IS in the range in the
  sense that it finally ran -- report sections 0 and 0a are generated and the five
  CI-section guards are green -- which is the practical half. The ledger question is
  Xabier's.
* **R653 -- OPEN, carried, becomes (c) at step 2.** `grep -rn RHO_INF` over `tests` and
  `floatfea` still gives no output. **Carries by name into step 2.**
* **R638 -- OPEN, unchanged, EJ1 governs, closed before F4 closes.** None of the six new
  entries touches it.
* **R637 clause (iii) -- ANSWERED.** Report Â§ 16 carries `scripts/suite_count.py`'s output
  and Â§ 16a re-takes it AT the revision's own commit, which is the half CZ1 (ii) asks for
  and which no revision in this milestone had done before. The figure it publishes from
  the worktree is explained by C154.
* **R622, R626, R631, R635 -- carried on the EJ3 ledger at `docs/closure/F3.md` Â§ 8,
  unchanged and not re-reviewed (CZ0).** They are in the report's Â§ 12 and Â§ 14 tables
  now, which is why the thirteen `test_the_report_carries_the_finding` reds are gone.
* **R657, R658, C119, R659, R660, R661, R662, R654, R655 -- CLOSED at verdict 93, not
  reopened.** Nothing in this range touches their sites.
* **The EJ4 residual-location hand-over -- unchanged, live at step 2**, where `3.96e-06`
  is the reference.
* **Verdict 94's `Next step opens when`, item by item.** (1) R670 -- **ANSWERED**, CI
  green, step list pasted. (2) R671 -- **ANSWERED**, sweep both ways pasted, `1.0e+6`
  gives 3 failed. (3) R672 -- **ANSWERED** by withdrawal at both sites. (4) R673 --
  **ANSWERED**, 0 reds. (5) R674 -- **ANSWERED**, signed, both injections into the model.
  (6) R675 -- **ANSWERED on the count, HALF-ANSWERED on the average (R680)**. (7) R676 --
  **ANSWERED**, all four rows, and I ran them as I said I would. (8) R677 -- **ANSWERED**,
  omission raises. (9) R678 -- **ANSWERED**, raises. (10) the schedule paragraph --
  **REWRITTEN at revision 3**, not carried, with the 19 Oct and 23 Oct dates and the
  arithmetic CZ0 asks for. All ten addressed; two with a named remainder.
* **What I said I would not accept, and whether it was offered.** Widening any of the
  three ceilings -- **NOT OFFERED**; none moved and I swept all six. Exempting an entry or
  extending the rung3 guard -- **NOT OFFERED**; the diff over that file is empty. "It
  fails safe" offered as a reason a gate needs no counter -- **NOT OFFERED**; all ten
  gates ship with one. A counter-case injecting into the expected side when the model is
  under test -- **OFFERED ONCE AND CORRECTLY**: `test_EK0a_the_premise_gate_REDDENS_on_a_
  LABELLED_FE_BODY` injects into the expected side, and the docstring argues that the
  source's value IS the thing under test. I accept that: the gate's whole content is a
  statement about HSP-stable's source. A skip standing in for a gate that runs -- **NOT
  OFFERED**; the skip is gone.

## Tolerances touched

**SIX DECLARED, THREE RENAMED, NONE MOVED.** I diffed the file separately per my
instruction 4, because that is where the cheapest wrong fix lands, and I read all 97
changed lines.

| constant | old | new | form | counter | injected by | my judgement |
|---|---|---|---|---|---|---|
| `F4_MEMBER_FORCE_CONSERVATION` | `1.0e-13` | `1.0e-13` | dimensionless, relative | `..._COUNTER = 0.5` (renamed from `_COUNTER_DEFECT`) | `test_G4_the_conservation_gate_REDDENS_without_the_equivalent_load` | **R671 ANSWERED.** Bracketed at `0.5` by the suffix and at `1.0` by the new `relative > CEILING`. Swept both ways, section 4. |
| `F4_EB6_POSITION_M` | `1.0e-6` | `1.0e-6` | metres, full scale, absolute on a dimensional quantity | `..._COUNTER = 30.982842` (renamed) | `test_EB6_a_PERMUTED_export_reddens_the_gate` | **ACCEPTED**, as last round and for the same stated reason. I re-verified the counter is the true minimum over all 66 transpositions against the NEW snapshot: `30.982841873186896`. |
| `F4_STATIC_REACTION_AGREEMENT` | `1.0e-12` | `1.0e-12` | dimensionless, relative | `..._COUNTER = 0.25` (renamed) | `test_G4_the_defective_formula_misses_the_reaction_by_a_quarter` | **ACCEPTED** and now bracketed: `0.3` reddens the rung3 ordering, where last round only an `approx` rel bound it. |
| `F4_STATIC_TIP_MOMENT_N_M` | none | `1.0` | **N*m, full scale -- ABSOLUTE on a dimensional quantity** | `..._COUNTER = 6386718.75` | `test_EO1_static_member_forces_match_STATICS_not_the_model` / `..._REDDENS_on_the_R663_formula` | **R681 -- THE FORM IS A DEFECT AND THE STATED REASON IS REFUTED BY ITS OWN COMMENT.** Value not loose; bracket works; the denominator is two lines above the assertion. |
| `F4_STATIC_TIP_MOMENT_N_M_COUNTER` | none | `6386718.75` | N*m | is the counter | the same test | **ACCEPTED.** Exact `mu L^2/12 * g`; measured defect `6386718.750000007`, ratio `1.000000`; the bracket reddens at a ceiling of `6386719.0`. The entry's note that rounding to `6386719.0` broke it once is the right thing to have written down. |
| `F4_STATIC_SYMMETRY_SPREAD` | none | `1.0e-12` | dimensionless, relative, `(max-min)/mean` | `..._COUNTER = 1.5` | `test_EK0d_the_symmetry_gate_REDDENS_on_an_unsymmetric_frame` | **ACCEPTED, and it is the strongest of the six.** Clean `9.113860057399177e-16`, `1097x` of room; one part in `1e9` of softening still reads `4.0464e-10`, `404x` above; clean trips at `9.0e-16`, bracket at `1.6`. |
| `F4_STATIC_SYMMETRY_SPREAD_COUNTER` | none | `1.5` | dimensionless | is the counter | the same test | **ACCEPTED, bound form, and ruling 3 says why.** The injection may weaken from factor `0.01` to about `0.0106` and no further -- a 4% window, measured. |
| `F4_MAPPING_CONSERVATION` | none | `1.0e-12` | dimensionless, relative, force and moment normalised separately | `..._COUNTER = 0.2` | `test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node` | **VALUE AND FORM ACCEPTED** -- clean `1.8726e-16`, `5341x` of room, clean trips at `2.0e-16`, bracket at `0.21`. **The QUANTITY it is a ceiling on is R679:** aggregated over bodies where the plan says per body. |
| `F4_MAPPING_CONSERVATION_COUNTER` | none | `0.2` | dimensionless | is the counter | the same test | **ACCEPTED, bound form.** The injection may weaken 18% before the counter assertion goes green, measured; the ceiling assertion holds throughout. Taking the counter from the SMALLER of the two injections is the right choice and the report measures both (`0.2437` and `0.9202`). |

```
cmd    git diff de9a448..b0824d5 -- floatfea/tolerances.py      [separately, instruction 4]
out    93 insertions, 4 deletions. The four deletions are the three `_COUNTER_DEFECT`
out    declaration lines and one comment line that pointed at one of them. NO VALUE MOVED.
cmd    grep -n "^F4_" floatfea/tolerances.py
out    twelve constants at :1893 :1909 :1927 :1938 :1953 :1963 :1973 :1983 :1998 :2012
out    :2030 :2043 -- and `docs/milestones/F4.md` section 5a lists twelve rows
cmd    perturb each of the six ceilings in turn and run tests/test_plan_matches_tolerances.py
out    EVERY perturbation reddens `test_the_plan_and_the_code_agree[F4.md-<line>-<name>-
out    <value>]`, so the plan table and the file are pinned to each other in both
out    directions. I moved each rather than reading the table.
rule   every numerical tolerance lives in floatfea/tolerances.py and moves with a plan edit
judge  **THE PLAN EDIT IS REAL AND CORRECTLY PAIRED, AND THE SIXTH REFUSAL IS ANSWERED
       WITH THE SUFFIX THAT BINDS RATHER THAN THE ONE THAT DOES NOT.** The one thing I
       would not have accepted -- a value moved to make something agree -- was not
       offered, and I checked rather than assuming.
```

## On the schedule

The report's one hand-written paragraph carries it and I read it rather than restating the
dates: EK4's preview held at three days early, step 1 closes on this verdict, and the
arithmetic for what slippage would look like is written out. **No slippage to report
today, and I agree with that reading** -- step 1 consumed exactly its three rounds and
closes green. The exposure CZ0 cares about is now step 2's round budget: three blocking
items arrive there by name on top of R653, which is four items before step 2's own work is
read. If step 2 then needs three rounds of its own, the choice CZ0 names -- slip the date
or reduce scope -- is live, and the report paragraph is where it gets stated the day it is
known. None of the three carried items needs new apparatus and none needs a design
decision: R679 is a normalisation scope, R680 is one line, R681 is one denominator.

## On the criterion -- not a HOLD, and it goes to Xabier through the implementer

Nothing to add this round. CZ0 did what it was written to do: I spent this round on three
gate-reach questions and a tolerance form instead of on prose, and the closure list below
is nine items I did not argue about. **One observation for the record rather than a
disagreement.** Two of my three blocking findings are cases where a gate's PROSE and its
REACH disagree, and under CZ0 the prose half is a closure item while the reach half blocks.
That split is the right one and I am not asking to change it -- but it means the same
defect is written down twice, in two lists, with two different dispositions (R679 and C152;
R680 and the `_analytic_static` docstring). I have kept them paired by name so the closure
commit and the step-2 fix cannot drift apart.

## Next step opens when

**STEP 2 OPENS NOW.** Step 1 is CLOSED at PASS: the tree is green on my own run and in CI,
the rung runs with no skip, and all nine of the previous round's blocking items are
answered. This was round 3 of 3 (CZ0; DK0 means no re-lock buys more), so the step closes
on this verdict and the remainder carries rather than consuming a fourth round.

## Carried for the next step -- THESE BLOCK AT STEP 2

1. **R679 -- G4.4's residual is formed and normalised PER BODY**, as `F4.md:310` says, with
   the two dropped-joint shapes re-measured per body and the docstring and assertion
   message claiming only the reach the fix has. `3.745164e-16` is the number that has to
   stop printing.
2. **R680 -- `_analytic_static:474` takes each element's own `rho * A * L`**, the same
   closed form line 105 already uses, with the clean worst re-measured.
3. **R681 -- the tip-moment ceiling is dimensionless against a stated response scale**, or
   the entry says which single scale it is a number about; the "nothing to be relative to"
   sentence is deleted either way.
4. **R653 -- carried again.** `grep -rn RHO_INF` over `tests` and `floatfea` still returns
   nothing, and at step 2 the integrator's own parameter becomes a gate assertion. It
   becomes (c) there, as verdict 94 said it would.

**What I will not accept as an answer at step 2:** widening any of the twelve F4 ceilings
or the counter that brackets it; a per-body form whose expected side is re-derived from the
mapper's output; "the wiring is the driver's business" offered a second time for something
inside the gate's own subject rather than at its boundary; a figure in `tolerances.py` that
is not regenerated at the commit that publishes it; or `_analytic_static` keeping the
average with an assertion that the members are equal in length -- the premise is false and
asserting it is how this was found.

**And what I want on the record for the implementer rather than against them.** Three
things in this round are the hardest kind. **The implementer asserted the premise I
objected to, found it FALSE, and reported that its own gate would have given a WRONG
ANSWER rather than a missed one** -- that is R675 going further than my condition asked,
volunteered, and it is the second round running that the report has recorded something
against itself that I could not have extracted. **R670 was answered with the design I
named and then with a provenance I could check independently**: a blob sha, a tag, and
twelve centres I rebuilt by hand from four constants in HSP-stable, all of which agreed.
**And Â§ 16a reported a four-way disagreement it could not resolve instead of quoting the
environment that suited it**, which is the only reason I knew to go and look -- the cause
turned out to be nine lines away and the honest "I have not diagnosed it" is what made it
findable. Measured against last round: every threshold I could move held, so all three of
my findings came from the inputs instead, and 11 of 31 unseen corpus entries is the best
rate of the milestone.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

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
