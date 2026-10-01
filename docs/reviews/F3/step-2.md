# Review — F3 step 2
Reviewed commit: cb03e0a14f5a6d57b0289778c46cfcff16a5020c
Verdict: HOLD
Tests: 3100 passed, 9 failed, 0 skipped   (my own run at the reviewed commit, `python -m pytest -q`, ONE invocation, no split, no exclusion, clean tree, 629.76s -- and NOT the report's subset count)

## Round of 2026-10-01 -- EIGHTY-FIRST verdict, and the FIRST on step 2 (EB4). THE PLAN STOP IS CLEARED. THE GATE IS WHERE THE WORK IS.

**Reviewed commit: `29570e1`.**

**R616 IS ANSWERED AND THE STOP IS LIFTED.** `docs/milestones/F3.md` section 5 is re-locked at `3709cc6`: the near-vertical band sentence is struck in place with the measurement that empties it, and the G2.1 row says what it is measured on. That was the one thing holding step 2 shut and it is shut no longer. Under EB4 the five post-closure rounds count against nothing and step 2 opens with three. **This is round 1 of 3.**

**WHAT I RULED THIS ROUND.** Eight commits, one path class each. I read every line of the diff before opening the report, ran the whole suite myself in one invocation, took CI from `gh` rather than from the paste, reproduced every figure in sections 2, 3, 4 and 5 of the report independently, and then attacked the new gate and the new refusal twenty-two ways. **The report is ACCURATE: every number in it that I re-took, I got.** The findings below are not corrections to its arithmetic. They are what the arithmetic it stopped short of says.

**THE ONE-LINE ANSWER TO THE HAND-BACK'S FIVE.** (1) Holding section 5 was RIGHT, and all three of its options move the wrong variable -- the CEILING is the variable and I have solved for it. (2) The second implementation is the right trade and the agreement test is sound, but it ties ONE of the two quantities and the untied one is where the defect is. (3) Four shapes is not the right set; the placement is correct and I measured it, `0.000000e+00`. (4) CZ1 needs a carve-out for a first report and my wording is below; the red is my own absence and it holds nothing. (5) You have item 5 the right way round -- the four lengths are real at full precision and I confirmed the bijection.

## THE TREE AT 29570e1, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    29570e121d129ee9b0dadfb5ea748e7695ffa678   both -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    (no output, before any work of mine)
cmd    git log --oneline 7e5f3fb..HEAD --name-only
out    3709cc6  docs/milestones/F3.md                EB0, the re-lock
out    9c26ffe  CLAUDE.md + docs/SUPERVISOR.md       EB1/EB4, process:
out    6246fbd  scripts/write_verdict.py             EB2, process:
out    ccbd38b  .github/workflows/ci.yml             EB3
out    5d93e6c  .claude/hooks/require-verdict.sh     EC0, process:
out    d0fb2a6  floatfea/ + tests/                   the gate and the refusal
out    d8ea3a3  docs/milestones/F3.md                the step marker
out    a772128  tests/ + docs/reports/               the cited test name
out    29570e1  docs/reports/                        this report
judge  one path class per commit, as stated. No commit touches both floatfea/ and
       docs/reviews/. The three commits touching my own instructions are each a
       standalone process: commit citing its directive -- read line by line below.
cmd    python -m pytest -q
out    9 failed, 3100 passed, 2 warnings in 629.76s (0:10:29)
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests scripts
out    112 files would be left unchanged
cmd    python -m mypy floatfea
out    Success: no issues found in 30 source files
cmd    python -m mypy scripts
out    Found 56 errors in 16 files (checked 21 source files)
judge  the ledgered count in ccbd38b's comment is RIGHT at this commit.
cmd    python scripts/check_carried.py --verdict docs/reviews/F3/step-1.md
         --report docs/reports/F3/step-2.md
out    check_carried: all 24 findings carried          exit 0
judge  ED1(c) confirmed by MY run, not accepted from the paste.
cmd    grep -n "'Answers:" docs/reports/F3/step-2.md
out    3:Answers: verdict 80 @ 7e5f3fb
cmd    git log --oneline -1 7e5f3fb ; git log --oneline -3 -- docs/reviews/F3/
out    7e5f3fb IS the eightieth verdict's own commit AND the newest verdict commit
judge  ITEM 1b SATISFIED. The header names the latest verdict, by the verdict's own
       commit rather than the commit it judged (DX2, C13). One comparison; it passes.
```

## CI, AT THE REVIEWED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit 29570e121d129ee9b0dadfb5ea748e7695ffa678 --json name,conclusion,status,workflowName,databaseId,event,headSha
out    CI  36861000264  push  completed  FAILURE   headSha 29570e1...
cmd    gh run view 36861000264 --json jobs, every job and every step
out    the verification ladder     success   13 steps, all success
out    lint, unit and guards       FAILURE   14 steps: actionlint, ruff,
out                                black --check, mypy and unit tests all SUCCESS,
out                                none skipped; "guards and meta-tests" FAILURE
out    CI determinism -- leg              skipped   0 steps
out    CI determinism -- ten legs agree   skipped   0 steps
judge  THE JOBS RAN -- runner present, 14 steps, 11m40s. NOT CK2: no job here has
       an empty runner_name with a two-second duration and a spending annotation.
       The two skipped jobs are the workflow_dispatch gate under CK0, unavailable
       BY DECLARATION, the same state verdicts 79 and 80 recorded.
cmd    gh run view 36861000264 --log-failed, the FAILED names
out    tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
out    ... and seven more planted states, each carrying either "baseline: expected
out    a clean run" or "a file that is not a numbered step must be stepped over"
cmd    my own whole-suite run at the same commit, one invocation
out    THE SAME NINE, BY NAME. 9 failed, 3100 passed.
```

**AND IT IS ONE CAUSE, WHICH IS MY OWN ABSENCE.** `tests/test_report_carried.py:450-456` asserts `STEP_REPORT == _PAIRED` and fails with "step 2 has a report and no verdict yet ... Invoke the gating-supervisor." Its own docstring at :418-422 names the state: "CB2 made it follow the newest report and that took the suite down whenever a report had no verdict yet, **which is every legitimate boundary**." The eight planted states cascade off it because the harness plants into a tree whose baseline is already red -- the cascade verdict 78 already ruled on.

**SO THE RED IS NOT THE HOLD, AND I SAY SO EXPLICITLY RATHER THAN LETTING CA2 DO IT SILENTLY.** CA2 exists because CI runs on a machine neither party controls and can contradict a local green. Here CI and my own run AGREE, by name, on nine failures whose assertion is that the verdict for this report does not exist. Reading that as (d) makes every step's first report unreviewable -- the no-exit the DD1 entry in `CLAUDE.md` records as costing two verdicts, neither about the work. **The HOLD below rests on three findings that are (a), (b) and (c), and a green CI would change none of them.**

**AND I MEASURED WHAT THIS VERDICT DOES TO THE SUITE, which is not what I expected and is worth more than the ruling.** Taken with `docs/reviews/F3/step-2.md` written into the tree, before it was committed:

```
cmd    python -m pytest "tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on" -q
out    1 passed in 0.15s
judge  CONFIRMED -- the verdict is what clears the nine. The summons is answered.
cmd    python -m pytest tests/test_report_carried.py -q, same tree
out    63 failed, 142 passed in 4.77s
out    57 x test_every_named_site_is_touched_or_declared[R616..R626-<site>]
out     3 x test_the_report_carries_the_finding
out     1 x test_the_CI_section_is_about_the_REVIEWED_commit
out     1 x test_the_Carried_table_is_what_the_generator_produces
out     1 x test_the_generator_would_catch_a_row_under_the_wrong_number
judge  THE PAIRING GUARD CLEARS AND SIXTY-THREE OTHERS OPEN. The suite is red on
       BOTH SIDES of a step boundary: before the verdict because the verdict does
       not exist, after it because the report answering it does not. The green
       window is only after the ANSWERING report lands.
judge  AND THE SECOND HALF HAS NEVER APPEARED IN A VERDICT, because the reviewer
       runs the suite at the JUDGED commit, before writing -- verdict 80's
       `2868 passed, 0 failed` was taken at `ec713d2`, which precedes `7e5f3fb`. So
       this state has existed at every step boundary in this milestone and nobody
       has measured it. It is the other half of R615's window, and it is why my
       ruling-4 clause below covers both sides rather than only the first.
```

The planted-state half needs the commit -- `tests/test_report_guard_states.py` clones the repository, so it cannot see an uncommitted verdict. That one measurement, and only that one, is taken after this file exists and goes in the hand-back.

## Carried

* **R616 / R613 -- ANSWERED at `3709cc6`, and the STOP IS LIFTED.** Verified line by line rather than taken from the report: section 5 now carries "WHAT THIS GATE IS MEASURED ON -- RE-LOCKED (EB0)", the band sentence is struck in place with `max abs dz = 0.0` and `within 15 deg of vertical  0` beside it, the gate row reads "Those orientations are all one orientation (EB0)", and the rigid link is named as outside the gate's subject. That is exactly verdict 80's condition 1. **R616 closes here and carries no further.**
* **R612 -- closed at verdict 79, still closed.** `ruff`, `black --check` and `mypy floatfea` clean at this commit, and CI's `ruff` and `black --check` steps both SUCCEEDED in run 36861000264.
* **R611, R617 -- withdrawn, and they stay withdrawn.** Nothing this round reopens either.
* **R614 -- closed by being on the page.**
* **R610, R615 -- ledger lines, unchanged, no work asked.** Third and second instance; I spend no more than this line on either.
* **R618 / C80 -- ANSWERED at `d0fb2a6`.** The word "linear" is gone from `floatfea/model/platform.py` and the entry reads "IT IS NOT LINEAR IN f ON THE PLATFORM (C80, R618)" with the `slack/f` row and the `1.80x` spread, naming the hubs as the exactly-linear case. The ruling it supports is untouched, as I said it would be.
* **R619 / C81 -- ANSWERED at `d0fb2a6`.** The sentence reads "THE SLACK IS REPORTED IN assumptions, NOT findings (C81, R619)" and says both tuples are empty at the shipped configuration.
* **R620 / C83 -- ANSWERED at `d0fb2a6`**, by the route BI3 prescribes: the docstring carries the numbers it needs and points at the report section rule regenerates, instead of carrying a table nothing regenerates.
* **R623 / C84 -- ANSWERED at `d0fb2a6`.** `tests/verification/rung3/test_platform_skeleton.py:488-497`: the DZ2 comment names the typed plan centre as the third source and says `joint_plane_z` is the deck's own joint elevation. More than the four words I asked for, and correctly more.
* **R621 / C79 -- ANSWERED in prose at `29570e1`**, section 9: `1 failed, 2 passed` replaces "twenty-two others".
* **R622 -- LATER, and correctly so.** It was written as F4's to answer and the report routes it there. Nothing owed inside this step.
* **C75 -- CLOSED. C75b -- ANSWERED at `ccbd38b`, both halves measured.** The workflow runs `ruff check floatfea tests scripts` and `black --check floatfea tests scripts` and both steps succeeded on CI at the reviewed commit. The `mypy` half is ledgered AT THE SITE WITH ITS REASON AND ITS COUNT, and the count is right: `Found 56 errors in 16 files`. `run_rung.sh` ledgered too. **That is the right shape -- the item asked for the pathspec or the exclusion written down with its reason, and this is the second.**
* **C74 -- STILL OPEN, closure.** Step 1's generated CI section stays anchored on verdict 74 at a failed run, by CO1's design, and step 1 is closed at PASS so its report is not edited. Ledgered.
* **C76 -- STILL OPEN, closure.** The marker-count clause counts plans, not markers per plan. Unchanged, holding nothing.
* **C77 answered with C79 as its correction. C78 ledger line. C82 wording, recorded in section 9. C85 recorded as asked** -- and I re-ran both uncollected resolvers by hand this round; `scripts/check_carried.py` is the one I used for ED1(c) above.
* **C58 to C64, C65 to C73, C40, C56(iii), C56(iv), C57** -- as ruled at verdicts 77, 79 and 80. Nothing in these eight commits touches any of them.

## THE FIVE RULINGS THE HAND-BACK ASKED FOR

**1. SECTION 5 -- HOLDING IT WAS RIGHT, AND ALL THREE OPTIONS MOVE THE WRONG VARIABLE.** Holding was right twice over: a tolerance decision is not the implementer's to take mid-step, and declining to register a counter under a size that cannot see the defect is exactly the restraint `CLAUDE.md` asks for. But all three options assume the INJECTION SIZE is the variable and the ceiling is fixed. It is the other way round, and the constant's own entry says so:

```
cmd    sed -n 347,353p floatfea/tolerances.py
out    "It is left rather than retired-with-a-marker because F3 asserts the
out     element-local check on every real platform member, and that gate needs a
out     ceiling of this shape -- which will be DERIVED FROM THAT QUANTITY'S OWN
out     MEASUREMENTS, NOT INHERITED FROM HERE."
judge  it was inherited. 1e-15 was measured under the PER-ROW ASSEMBLED form at
       R475, over the corpus of assembled frames. The gate and the refusal shipped
       at d0fb2a6 assert the GLOBAL-NORM ELEMENT-LOCAL form against it. Different
       quantity, same number, no new measurement taken.
```

**And the solve all three options skip. One loop each, at this commit:**

```
cmd    over the SIXTEEN members: solve for the ceilings C that pass the
       defect-free case AND redden all three counters at the declared 1e-14
out    clean worst            3.528257e-19    (C must be ABOVE)
out    dropped_flip           3.656327e-16    (C must be BELOW)
out    wrong_dof_index        9.459456e-15    (C must be BELOW)
out    rotational_block       1.464442e-17    (C must be BELOW)
out    => A WINDOW EXISTS: (3.5283e-19, 1.4644e-17), 41.51x wide
judge  SO NO NEW CONSTANT AND NO NEW INJECTION SIZE IS NEEDED. Option (a)'s row in
       a closed plan and option (b)'s new table in F3.md both answer a question
       nobody has to ask: the declared 1e-14 registers all three counters as soon
       as the ceiling sits inside that window.
cmd    the same solve over the WHOLE admissible band, L/D >= 2 to L/r <= 300, on
       F1:389's recorded section, 194 points
out    worst clean                        5.287607e-18   (C must be ABOVE)
out    weakest rotational_block response  1.571633e-19   (C must be BELOW)
out    => THE WINDOW IS EMPTY
judge  AND THIS IS WHAT SECTION 5 HAS TO SAY. The GATE'S subject is the sixteen
       members (EB0 narrowed it); the REFUSAL'S subject is every deck. One constant
       cannot carry a counter guarantee on the second, because the clean response
       and the counter response move in OPPOSITE directions with slenderness. That
       is a statement about scope, not a number to tune.
```

**Option (c) is the one I would refuse on its face.** An injection size derived at runtime from the bisected edge is a counter sized by the very ceiling it is supposed to be independent of. `tests/test_counters_are_injected.py` cell two exists to require the opposite -- "the counter must be SIZED BY the constant it defends" -- and a runtime-derived size passes that cell vacuously. `WIDEN = 10.0` is not a precedent: `WIDEN` is a fixed factor nothing compares against, not a quantity read back out of the measurement it governs.

**2. THE SECOND IMPLEMENTATION IS THE RIGHT TRADE, AND THE TIE COVERS ONE OF THE TWO QUANTITIES.** Shipping `floatfea/element/rigid.py` rather than re-pointing frozen rung-1 apparatus is correct under DR1 and I would have ruled the same way. The agreement test is sound and the `0.000e+00` is real -- I reproduced it on all sixteen. But:

```
cmd    compare the four function bodies in the two files, name by name, docstrings
       stripped
out    element_rigid_vectors    NOT textually identical -- a different loop form
out    element_homogeniser      NOT textually identical -- a different loop form
out    element_rigid_residual   identical below the docstring
out    seventh_over_epsilon     A DIFFERENT FUNCTION. rung 1 takes (k) and
out                             homogenises by max|K|; the shipped one takes
out                             (k_local, length) and homogenises by S
cmd    read what the gate compares
out    test_G2_1_the_SHIPPED_residual_agrees_with_RUNG_ONEs compares
       element_rigid_residual ONLY
judge  so the module docstring's "rung 1 keeps its own copy ... what ties the two is
       [that test]" is true of the residual and false of the spectral half, and the
       UNTIED half is the one R625 below is about. The trade is right; the tie is
       half a tie; and the half that is loose is the half that is new.
```

**3. FOUR SHAPES IS NOT THE RIGHT SET. THE PLACEMENT IS CORRECT AND I MEASURED IT.**

```
claim  the refusal would land identically in the member loop
cmd    max |local_stiffness(section, body.material, L) - local_stiffness(section,
       S355, L)| over the sixteen members
out    0.000000e+00
cmd    read floatfea/element/beam.py:127-152 for what local_stiffness consumes
out    E, G, A, J, I_z, I_y and kappa. rho appears nowhere in the function.
judge  CONFIRMED, and the placement chosen is the better of the two for the reason
       the comment gives: what is checked is what is shipped. No finding here.
```

The SET is where it falls short, and the missing class is SIGN -- R625. Four shapes that all perturb a magnitude cannot reach a defect that preserves every magnitude.

**4. CZ1 NEEDS A CARVE-OUT FOR A FIRST REPORT. HERE IS MY WORDING, TO CARRY AS THE ORIGINAL WAS CARRIED.** The circularity is real and measured above: step (iii) asks for a green pushed run before the invocation, and at a step's first report the guard that is red is the one asserting that this verdict does not exist.

> **CZ1 step (iii) does not apply to the boundary red a step's own report creates, on EITHER side of the verdict.** Two states, both designed, both self-clearing, and neither is a defect:
>
> **(1) Report written, verdict not yet.** The only failures are `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` and the planted states that cascade off its baseline. The verdict clears them.
>
> **(2) Verdict written, answering report not yet.** The only failures are `test_every_named_site_is_touched_or_declared`, `test_the_report_carries_the_finding`, `test_the_CI_section_is_about_the_REVIEWED_commit`, `test_the_Carried_table_is_what_the_generator_produces` and `test_the_generator_would_catch_a_row_under_the_wrong_number`, each naming a finding or a site of the newest verdict. The answering report clears them.
>
> In either state the run is recorded as RED WITH ITS CAUSE NAMED -- the full `FAILED` list pasted, and the sentence saying which of the two states it is -- and work proceeds. **Any failure outside the state's own list is CZ1 (iv) unchanged**, and "only those" is a claim that carries the `FAILED` list as its command. The reviewer measures state (1) clearing at its verdict commit; the implementer measures state (2) clearing at the report commit.

I have done the reviewer half this round. **I am not editing CZ1 and this is not a HOLD on it** -- it is the disagreement-with-the-criterion channel, said once, leaving the loop.

**5. ITEM 5 IS THE RIGHT WAY ROUND AND I CONFIRMED THE BIJECTION.**

```
cmd    repr(length) and element_rigid_residual, per member, grouped
out    L=50.0                 8.721078e-20   n=4
out    L=25.0                 9.673052e-20   n=7
out    L=25.000000000000004   1.988390e-19   n=4
out    L=25.000000000000007   3.528257e-19   n=1
judge  four lengths, four residuals, one to one, counts 4+7+4+1 = 16. EB0's sentence
       is TRUE at full precision and withdrawing it would have been the error. You
       caught yourself; recorded because the check that looked like a refutation is
       the one that confirmed it.
```

## Findings

**R624. (b, blocking) THE CEILING THE NEW GATE AND THE NEW REFUSAL ASSERT AGAINST IS INHERITED FROM A DIFFERENT QUANTITY, AND THAT CONSTANT'S OWN ENTRY FORBIDS IT. THE CONSEQUENCE IS MEASURED, NOT PREDICTED.** `tests/verification/rung3/test_platform_rigid_modes.py:99` and `floatfea/model/platform.py:311-319` both compare the element-local global-norm residual with `RIGID_MODE_EXACTNESS = 1e-15`, whose "Reason for 1e-15" at `floatfea/tolerances.py:316-328` is measured under the per-ROW assembled form (R475), over assembled corpus frames. `tolerances.py:347-352` pre-registered that F3's gate "needs a ceiling of this shape -- which will be derived from THAT quantity's own measurements, not inherited from here."

```
cmd    the whole admissible section-and-length space: D_o 0.2..6 m, t/D_o
       0.005..0.2, L constrained to L/D >= 2 and L/r <= 300; 1680 points
out    WORST clean residual   1.620063e-17   at D_o 0.20, t 0.0010, L 0.400
out    the ceiling            1e-15          => 61.73x headroom EVERYWHERE
out    SMALLEST seventh/eps   3.849230e+10   at D_o 0.50, t 0.0250, L/r 300.0
out    the bound              199.526        => 1.929e+08x inside
rule   the two shipped assertions, read as refusals over every member a deck can
       describe
judge  so NEITHER HALF OF THE REFUSAL CAN FIRE ON ANY ADMISSIBLE DECK. The only
       thing that can move the residual is a CODE defect in local_stiffness -- which
       makes the counter sizes the whole specification of what this gate is for, and
       two of the three declared ones are blind:
out    dropped_flip      at 1e-14  3.656327e-16 = 0.3656x the ceiling    BLIND
out    rotational_block  at 1e-14  1.464442e-17 = 0.01464x               BLIND
out    wrong_dof_index   at 1e-14  9.459456e-15 = 9.459x                 reddens
cmd    invert and bisect each edge, worst over the sixteen
out    2.735459e-14   1.057143e-15   6.837686e-13
judge  I reproduced the report's figures exactly. What it did not take is the solve in
       ruling 1: over the SIXTEEN the ceiling window is (3.5283e-19, 1.4644e-17),
       41.51x wide; over the ADMISSIBLE BAND it is EMPTY.
```

**Closed when** one of two things, and either is a decision rather than work: **(i)** `RIGID_MODE_EXACTNESS` is derived from the element-local quantity's own measurements and lands inside the 41.51x window, at which point all three counters register at the declared `1e-14` with no new constant and no new table -- the value moves in an existing `F2.md` row, not a new one; or **(ii)** the gate's subject and the refusal's subject are separated in writing, the gate keeping a derived ceiling and the refusal declaring that it carries no counter guarantee across the admissible band with the EMPTY-window measurement beside it. **Either way the three counters F3 section 5 asks for are registered or section 5 is amended to say they cannot be** -- what may not stand is an assertion whose declared counters are two-thirds blind and whose ceiling nobody measured for it.

**R625. (a and c, blocking) THE SHIPPED REFUSAL ACCEPTS AN INDEFINITE ELEMENT STIFFNESS. THREE SIGN ERRORS, EACH INJECTED ALONE, EACH PASSING BOTH HALVES.** `floatfea/element/rigid.py:106-119`: `seventh_over_epsilon` sorts `np.abs(np.linalg.eigvalsh(khat))`, so a large NEGATIVE seventh eigenvalue reads as a large positive one. And a symmetric sub-block negated still annihilates every rigid motion -- a rigid rotation has `theta_A == theta_B`, so the torsion block cancels whatever its sign -- so the residual half does not see it either.

```
cell   one shape at a time into k_local for platform:hub1_arm, L = 50 m, nothing
       else touched, then floatfea.model.platform.check_rigid_modes called
out    clean                        residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    torsion sub-block negated    residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    axial sub-block negated      residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    whole matrix negated         residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    torsion DIAGONALS only       residual 2.083e-04                          REFUSED
out    signed eigenvalues, homogenised: clean has 0 negatives; the three accepted
out    cases have 1, 1 and 6, the largest at -2.2951e+06 on a matrix of norm 1.1e10
rule   the two shipped assertions, and the check_rigid_modes docstring's claim that
       "no OTHER deck can produce a member that is not [sound]"
judge  an element with negative axial or torsional stiffness RELEASES energy under
       deformation. "The whole matrix negated" is the sign-convention inversion
       CLAUDE.md non-negotiables name by name. Three of four pass, and the one that
       is caught is caught by the residual, not by the half that exists for this.
cmd    does anything else in the repository reject an indefinite element stiffness
out    NO. Every spectral read in rung 1 and rung 3 takes np.abs; rung 2's
       test_consistent_mass.py:497 and :747 use np.clip(..., 0.0, None), which
       DISCARDS the sign; the only eigenvalue sign test in floatfea/ is on INERTIA,
       at io/reader.py:314.
judge  AND THE DOCSTRING SENTENCE THAT WOULD HAVE REASSURED A READER IS THE ONE THIS
       REFUTES: "why the residual half is the thing that catches a structural sign
       flip, is in rung 1's copy" (rigid.py:100-103). It does not catch these three.
```

**Closed when** the refusal rejects an indefinite element, and the measurement below says it needs NO new constant -- `RIGID_MODE_BOUND` read as a floor on the SIGNED minimum separates clean from defect by twelve to fifteen decades:

```
cmd    lambda_min(k_hat) / (||k_hat|| * eps), the same unit the bound is already in
out    the sixteen members          -0.0715 .. -0.0021
out    the whole admissible band    -0.7908 .. +0.0001     (194 points)
out    torsion sub-block negated    -9.379115e+11
out    axial sub-block negated      -4.503527e+15
out    whole matrix negated         -4.503527e+15
rule   lambda_min / (||k_hat|| * eps) >= -RIGID_MODE_BOUND
judge  every clean case passes by 252x; all three defects are refused by 4.70e+09x
       or more. One comparison, inside the assertion that is already there, on the
       constant that is already there. NOT a new gate and NOT new apparatus.
```

The alternative close is narrower and I will take it: the two docstring sentences are reduced to what was measured and the gate's own comment says the pair is blind to sign. **What may not stand is a shipped refusal that accepts negative stiffness while its docstring says no other deck can produce an unsound member.**

**R626. (c, blocking) THE REFUSAL IS A GATE HALF AND NOTHING COMMITTED SHOWS IT EVER REFUSES. ITS SIBLING IN THE SAME MODULE IS TESTED ON BOTH SIDES OF BOTH BOUNDARIES.** F3 section 5 makes "the builder refuses a platform that fails it" half of what G2.1 asserts, so this is a gate assertion and not apparatus.

```
cmd    grep -rn "check_rigid_modes" tests/
out    tests/verification/rung3/test_platform_rigid_modes.py:26   a docstring line
out    tests/verification/rung3/test_platform_rigid_modes.py:224  a comment line
out    no import, no call, no pytest.raises, anywhere in tests/
cmd    grep -rn "check_limits" tests/
out    test_platform_skeleton.py:696  check_limits("just inside", 2.0 * D)
out    test_platform_skeleton.py:698  pytest.raises ... ("stubby", 1.99 * D)
out    test_platform_skeleton.py:705  check_limits("just inside", 300 * r)
out    test_platform_skeleton.py:707  pytest.raises ... ("slender", 1.01 * 300 * r)
rule   a gate carries its own failure -- break the claimed property and confirm the
       assertion goes red
judge  check_limits, the refusal shipped in the SAME module for F3 section 2, is
       solved at both boundaries from both sides. check_rigid_modes, shipped in the
       same step, has nothing. The only evidence the refusal fires is the report's
       section 3 cell, and that cell is a scratch measurement no committed code
       reproduces.
cmd    and one row of that cell does not reproduce: the fourth shape, "seventh_mode
       REFUSED, injected alone at 1e-8 of max|k_e|"
out    NO SUCH SHAPE EXISTS IN THE REPOSITORY -- scripts/rigid_counter_response.py
out    injected() raises SystemExit on anything but the three
out    AND NO 1e-8-of-max|k_e| PERTURBATION AT THE TORSIONAL BLOCK CAN REACH THE
out    BOUND: rotational_block at 1e-8 reads 9.3791e+11 against 199.526, green, and
out    the retained-torsion fraction at the boundary, bisected, is 2.127342e-10 --
out    9.67 DECADES below 1e-8
judge  so the one row offered as evidence that the SEVENTH-MODE half of the refusal
       fires is UNVERIFIED, and the size attached to it is refuted. The half does
       fire -- I made it, by removing the torsion entirely, 4.8647e-02 -- but that is
       my measurement and not the report's.
```

**Closed when** `tests/verification/rung3/` carries a cell that calls `check_rigid_modes` and asserts it RAISES, in the shape `check_limits` already uses beside it: for each half, one input just inside and one just outside, with the boundary solved rather than sampled. **Not new apparatus** -- it is a verification test of shipped `floatfea/` behaviour, in the file class that already holds exactly this, and DR1 freezes guards and meta-tests, not rung tests. And the `seventh_mode` row either names a shape that exists in the tree with its real size, or goes.

## Closure items

Named, not re-reviewed, none of them holding anything. Fix the list once in the step's closure commit and verify it AFTER it exists (CZ1), with my ruling-4 carve-out applied to the pairing guard if it is the only red.

* **C86.** `floatfea/element/rigid.py:18-23` -- the module docstring says rung 1 "keeps its own copy" and that the agreement test "ties the two". It ties `element_rigid_residual` and not `seventh_over_epsilon`, which is a different function in the two files. **Closes when** the sentence names the quantity it covers.
* **C87.** `floatfea/element/rigid.py:100-103` -- "why the residual half is the thing that catches a structural sign flip, is in rung 1's copy". Refuted by R625's three shapes. Folded into R625's close; listed here so the wording is not forgotten if R625 is closed by the signed read alone.
* **C88.** `docs/milestones/F3.md` section 5, mine under EB0, two provenance defects I am recording against myself. **(i)** "Every figure below is produced by `PYTHONPATH=. python scripts/rigid_counter_response.py` and the geometry and residual sweep in `tests/verification/rung3/`" -- that script reads the rigid-body CORPUS and prints counts at `SIZE = 1e-8`; it never builds the platform, and no sweep in `tests/verification/rung3/` prints the per-member table. **(ii)** the bisected edges published there, `5.286e-14 / 1.094e-15 / 2.643e-12`, are not reproducible as "worst over the sixteen members": at this commit that solve gives `2.735459e-14 / 1.057143e-15 / 6.837686e-13`, which is what the report prints and what I measured. The published triple looks like the WEAKEST member's edge rather than the worst. **Closes when** section 5 either names the command that produces its table or carries the figures the report's own run gives. Not the implementer's file; recorded for whoever next edits it.
* **C89.** `docs/milestones/F3.md` section 5's judgement "SIZE sits four to seven decades past every boundary" is measured at `1e-8`, which is `scripts/rigid_counter_response.py`'s not-a-tolerance probe size and NOT `RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1e-14`, the repository's declared counter size. At the declared size two of three are blind. The sentence that follows -- "what make a correction sufficient here and a new gate unnecessary" -- is the conclusion R624 holds on. Same file, same owner.
* **C90.** `tests/verification/rung3/test_platform_rigid_modes.py:94-96` and `:122-124` -- "a pure number because the residual is dimensionless and relative to the quantity compared". Dimensionless, yes; unit-INVARIANT, no. The same member in millimetres, consistently scaled, moves the residual by `1.1110x`, `3.9264x` and `2.5417x` at `L = 50`, `25` and `5` m. `seventh_over_epsilon` is exactly invariant, `1.000000`. It passes the unit-scaling test vacuously today on a `2834x` margin; inside R624's `41.51x` window a `3.93x` sensitivity is a tenth of the room. **Closes when** the comment says dimensionless rather than implying invariant, and R624's derivation accounts for it.
* **C91.** `tests/verification/rung3/test_platform_rigid_modes.py:217-218` -- "`tests/test_report_carried.py`'s sibling `test_every_declared_tolerance_appears_in_the_plan`". That test is in `tests/test_plan_matches_tolerances.py:98`. Same directory, different file; a reader following the name goes to the wrong one.
* **C74, C76, C78, C82, C85, R610, R615** -- carried unchanged, see `## Carried`.

## Tolerances touched

```
cmd  git diff 7e5f3fb..HEAD -- floatfea/tolerances.py
out  no output
cmd  git diff 7e5f3fb..HEAD --stat -- floatfea
out  floatfea/element/rigid.py     115 +     a new module
out  floatfea/model/platform.py     91 +, 8 -
cmd  git diff 7e5f3fb..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  no output
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep conftest
out  tests/conftest.py            one conftest in the tree; no rung carries its own
```

**NO VALUE MOVED, AND THAT IS THE FINDING RATHER THAN THE CLEARANCE.** No tolerance, no golden, no parametrisation and no `_COUNTER` changed, and no counter was registered -- which is correct restraint and is why R624 is a HOLD on a DECISION rather than on an edit. No conftest and no plugin changed, so nothing new can rewrite what `scripts/run_rung.sh` reads and the CH2/CI0 reading has nothing to read this round.

**TWO CONSTANTS CHANGED THEIR SUBJECT WITHOUT CHANGING THEIR VALUE**, which is the case this section exists to notice and the one a diff of the file cannot show:

| constant | value | what asserted it before | what asserts it now | justification located |
|---|---|---|---|---|
| `RIGID_MODE_EXACTNESS` | `1e-15`, unchanged | nothing -- a diagnostic since DI0/R530 | the rung-3 gate at :99 AND the shipped refusal at platform.py:312 | `F3.md` section 5's residual sweep -- a measurement of the clean response, NOT a derivation of the ceiling, and `tolerances.py:347-352` asks for the derivation. **R624.** |
| `RIGID_MODE_BOUND` | `199.526231496888`, unchanged | rung 1, on the ASSEMBLED `K / max abs K` | the rung-3 gate at :125 AND platform.py:325, on the ELEMENT-LOCAL `S`-homogenised quantity | `F3.md` section 5 gives the margin `4.70e+09x` and no counter in the new quantity. The registered `rigid-body seventh under the bound` counter in `tests/test_counters_are_injected.py` defends rung 1's gate, not this one -- and I measured that no perturbation at the three counter sites, at any size up to `1.0`, can redden the new half. **R624, and the signed read in R625 is what gives this constant a sensitive direction.** |

## My own instructions (4b), read line by line

```
cmd  git diff 7e5f3fb..HEAD --stat -- .claude docs/SUPERVISOR.md
out  .claude/hooks/require-verdict.sh | 40 +++++++++++++++++++++++++++++++++++----
out  docs/SUPERVISOR.md               | 41 ++++++++++++++++++++++++++++++++++++++++
cmd  git log --oneline 7e5f3fb..HEAD --name-only, the two commits that touch them
out  9c26ffe  CLAUDE.md + docs/SUPERVISOR.md only      process:, cites EB1 and EB4
out  5d93e6c  .claude/hooks/require-verdict.sh only    process:, cites EC0
judge  BOTH ARE STANDALONE process: COMMITS CITING THEIR DIRECTIVE, and neither also
       touches floatfea/ or tests/. NO STOP-CLASS PROCESS FINDING.
judge  CONTENT, read line by line rather than by stat. docs/SUPERVISOR.md gains CZ1
       and EB4 and loses nothing -- 41 inserted, 0 deleted, and the CZ1 text is the
       wording I proposed, unparaphrased. require-verdict.sh changes the milestone
       field from $2 to $3 and makes a path it cannot read a milestone from BLOCK
       rather than rank at zero. That is STRICTER, not looser: before, every report
       ranked at milestone 000 and docs/reports/F2/step-7.md beat
       docs/reports/F3/step-1.md on 7 > 1, so the hook read none of F3's seven
       verdicts. NO GUARD IS REMOVED BY EITHER COMMIT. Verified by reading both
       diffs in full, not by counting lines.
cmd  and the byte-identity EB1 claims between the two copies of the CZ1 text:
     slice each file from the CZ1 heading to the next heading and compare
out  CLAUDE.md 1817 bytes ; docs/SUPERVISOR.md 1817 bytes ; identical True
judge  CONFIRMED. The hand-back says 1527, which is a different slice of the same
       block -- my boundaries include the heading line and the italic attribution.
       Identity is what EB1 claimed and identity is what I measured.
```

## The adversarial corpus (BE3)

`tests/corpus/element_local_g21_refusal_reach.txt`, batch 28, committed separately from this verdict at `cb03e0a`. **THIRTY ENTRIES, ALL THIRTY UNSEEN -- a new file on a surface no corpus has touched.** In scope under DE2: the element, the gates and the platform model, and nothing about apparatus.

**Ten entries carry a mutation. FOUR CAUGHT, SIX NOT CAUGHT.** The six are not reach -- they are the subject the gate names: three sign errors that leave the element indefinite, one torsion loss of nine decades, and two of the three counters F3 section 5 asks for at the size this repository declares. `expect=` is the prediction written before each run; `measured=` is what the shipped pair did. Against four of eleven caught in batch 27, ten of eleven in batch 26, twelve of thirteen in batch 25.

**This is the first corpus round in five whose misses are inside the gate's own stated subject rather than outside it**, and that is why R625 and R624 block where batch 27's eight invisible deck mutations did not.

Every mutation was applied in a scratch harness under the session scratch directory, importing the shipped functions; nothing in the working tree was written. `git status --porcelain --untracked-files=all` was empty before I began and the only paths I have written in this repository are the two corpus files and this verdict.

**AND THE CORPUS COMMIT REDDENS NOTHING, measured rather than reasoned.**

```
cmd  grep -rn for a glob over tests/corpus in tests/ and scripts/
out  none -- every corpus reader names one file by name, as verdict 80 recorded
cmd  grep -rn "element_local_g21_refusal_reach" tests/ scripts/ --include=*.py
out  named by no .py
cmd  python -m pytest tests/test_collected_set_golden.py tests/test_marker_exemption_corpus.py
       tests/test_report_vocabulary_corpus.py tests/test_tree_prose_consistent.py
       tests/test_ci_ladder_gating.py -q        with batch 28 in the tree
out  298 passed in 131.28s          exit 0
judge  a .txt file adds no parametrised case -- the citation guard scans .py prose
       inside backticks only -- so batch 28 moves no collected count and no assertion.
```

**EC4 IS DONE, in the same commit.** `tests/corpus/platform_skeleton_builder.txt:136` recorded the smallest of the four distinct residuals as `7.18521e-20`; re-measured at this commit it is `8.721078e-20`, the other three and the worst agree exactly, and the `2834.26x` margin is set by the worst and is unaffected. The row now carries the corrected figure and says it was corrected here and why. The file is mine under DE2 and DR1; the request was the right way to raise it.

## On the criterion, and the one thing above me

I was asked to rule under CZ0 and I did. **Three findings are blocking and each is squarely inside (a), (b) or (c):** R624 is a tolerance value and the form of one, including a counter and how it is injected; R625 is a defect in `floatfea/` and a gate assertion's quantity; R626 is what a gate half claims and whether it can fail. Six more findings are closure items and I have put them in a list instead of spending a round on them -- including two against my OWN section 5, which I am recording rather than re-litigating.

**NOTHING HERE IS A COMPLAINT ABOUT THE CRITERION.** CZ0 worked this round exactly as intended: six prose findings that would have consumed a round under the old head are a list, and the round went to the element instead. That is the first time this milestone it has paid out that way, and it is worth saying so.

**The one thing I want recorded for Xabier, and I say it once: CZ1 needs the first-report carve-out in ruling 4.** It is a four-line clause, it narrows nothing, and without it every step's first report arrives with an unsatisfiable precondition -- which is the species of defect DR1's own record says produced a finding against itself in four consecutive rounds. I have not edited CZ1; it is the implementer's to carry, as the original was.

## Next step opens when

**Step 2 stays OPEN. R616 is answered, the STOP is lifted, and the plan is no longer what blocks -- the gate is.** Three items, and two of them are decisions rather than code.

1. **R624 -- the ceiling is derived for the quantity it bounds, or the two subjects are separated in writing.** Either close is acceptable and both are measured above. If the derivation route is taken, the 41.51x window `(3.5283e-19, 1.4644e-17)` is where the value lands and the declared `1e-14` then registers all three counters with no new constant and no new plan table -- **which retires all three of section 5's options, so do not spend a round choosing between them.** If the separation route is taken, the EMPTY-window measurement goes beside the refusal. **Either way, F3 section 5's request for three registered counters is satisfied or section 5 says why it cannot be.**
2. **R625 -- the refusal rejects an indefinite element stiffness.** The signed `lambda_min / (||k_hat|| * eps) >= -RIGID_MODE_BOUND` read is measured, needs no new constant and no new gate, and separates clean from defect by twelve to fifteen decades. Whatever form is chosen, the three shapes in R625's cell are the acceptance test and the two docstring sentences are reduced to what holds.
3. **R626 -- `check_rigid_modes` gets a committed cell that shows it RAISING**, in the shape `check_limits` already uses eight lines away, with each boundary solved rather than sampled; and the report's `seventh_mode` row names a shape that exists with its real size, or goes.

**Do NOT spend a round on anything under `## Closure items`**, including C88 and C89 which are against my own section 5. Fix the list once in the closure commit.

**CZ1, as I have ruled it.** Verify the closure commit after it exists. If the only red at that commit is the step-pairing guard and the states that cascade off it, record it with the `FAILED` list pasted and proceed -- that is ruling 4 and it applies to you now, not after Xabier answers. Any other red is CZ1 (iv) unchanged.

**Schedule.** F3 closes 13 October; F4 19 October; the member-force table 23 October; the code-check screen 28 October. **I have no measurement that contradicts any of them.** The report says step 3 is "the counter registration and F3's closure artifact, 7 October" and that is where R624 and R625 land naturally; what I have added to that step is the derivation and one assertion, not a new gate, and R626 is a test in a file that already has its template. **DZ7c is not triggered and I am not asking for a slip.** The one thing that could move the date is R624 answered by inventing a new constant and a new plan table instead of deriving the one that exists -- and if that is the choice, say so the day it is made.

**This is round 1 of 3 on step 2 (EB4).** Two rounds remain. I would rather spend the second on R625's acceptance cell than on anything in the closure list, and I will not re-review the closure list item by item.
