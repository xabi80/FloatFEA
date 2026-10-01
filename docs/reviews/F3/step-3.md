# Review — F3 step 3
Reviewed commit: 6c4e6516f5a07c0f75db67c897c9258b60b3288d
Verdict: HOLD
Judged commit: a647492e99b59eec16b0b3faf2489867d2aab596  (HEAD of F3 and pushed; the stamp above is HEAD at write time, which is corpus batch 31 at 6c4e651 -- the tool records that limitation in its own docstring)
Tests: 2976 passed, 9 failed, 0 skipped   (my own run, ONE invocation, clean tree, no exclusion, 641.69s -- not the report's 2664, and not its 270/20 excluded-set split)

## Round of 2026-10-01 -- EIGHTY-FOURTH verdict, ROUND 1 OF 3 ON STEP 3.

**THE ELEMENT WORK IS RIGHT AND I COULD NOT BREAK IT.** R624 is answered, and I
re-derived the answer rather than accepting it: the window, the emptiness of the band
window, the 16/16 counts, the three detection edges and the counter-size boundary all
reproduce on my machine, and the one figure the step needed that nobody had taken --
what the new ceiling BUYS -- is a **843x to 866x gain in the smallest defect the gate
detects.** That is the strongest result in F3 and the report does not state it.

**I HOLD ON THREE THINGS AND NONE OF THEM IS THE ELEMENT.** One is a red at the
judged commit that is NOT the step-boundary class, on both machines, at the exact
site verdict 83 named -- R629 is not closed, it changed shape. Two are sentences in
`floatfea/tolerances.py`: the new entry says its three counters are registered in a
file that does not name them, and the entry 60 lines above says nothing asserts a
constant that the production builder refuses on. Both are (b) rather than prose,
because `tolerances.py` is the one file `CLAUDE.md` makes authoritative for a
tolerance and both sentences are the only statement of what their constant is for.

## THE TREE AT a647492, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    a647492e99b59eec16b0b3faf2489867d2aab596   both -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    (no output, before any work of mine)
cmd    git log --oneline 580b183..HEAD --name-only
out    0d911ce  docs/reports/F3/step-2-answers.json, step-2.md
out    47daa3d  docs/milestones/F3.md, floatfea/tolerances.py,
out             tests/test_plan_matches_tolerances.py,
out             tests/verification/rung3/test_platform_rigid_modes.py
out    f942b83  CLAUDE.md, docs/SUPERVISOR.md
out    7e86d2a  docs/milestones/F3.md
out    a647492  docs/closure/F3.md, docs/reports/F3/step-3.md and -answers.json,
out             docs/reports/F3/step-2.md
cmd    git diff 580b183..HEAD --stat -- floatfea tests docs scripts .github .claude CLAUDE.md
out    11 files, 1310 insertions, 58 deletions
judge  FIVE COMMITS AND THE PROCESS CHANGE IS STANDALONE. f942b83 touches CLAUDE.md
       and docs/SUPERVISOR.md and NOTHING ELSE, cites EG3 and EG4e in its subject,
       and is purely additive. NO STOP-CLASS PROCESS FINDING. Verified by the diff
       rather than by the subject line -- see `## My own instructions` below.
cmd    python -m pytest -q
out    9 failed, 2976 passed, 2 warnings in 641.69s (0:10:41)
cmd    python -m pytest tests/verification/rung3/test_platform_rigid_modes.py -q -s
out    16 passed in 2.33s, and every printed figure is reproduced in R636 below
cmd    the Answers header, and the newest verdict commit
out    docs/reports/F3/step-3.md:3   Answers: verdict 83 @ 580b183
out    git log --oneline -1 580b183 -> "review: F3 step 2 -- eighty-third verdict"
judge  ITEM 1b PASSES, in one comparison. The report answers the NEWEST verdict by
       that verdict's own commit. No HOLD on this head.
```

Lint and types: not re-run by me, because CI ran them at this exact commit and that is
the stronger witness -- `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests`
are five SUCCESS steps in run 36900722535, none skipped, and `guards and meta-tests`
is seen to have RUN rather than been skipped behind an earlier red (CZ1 iii).

## CI, AT THE JUDGED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit a647492... --json conclusion,status,databaseId
out    36900722535  completed  FAILURE
cmd    gh run view 36900722535 --json jobs, job by job
out    the verification ladder            SUCCESS   13 steps
out    lint, unit and guards              FAILURE   14 steps
out    CI determinism -- leg              skipped    0 steps
out    CI determinism -- ten legs agree   skipped    0 steps
cmd    the ladder job's steps
out    ladder 1, 2, 3, 6, 4, 5 -- ALL SUCCESS. "ladder 3 -- the model is the
out    platform" is green, which is where the new ceiling and the three new cells
out    live.
judge  NOT CK2: no two-second duration, no runner-never-started, no spending
       annotation. The two skipped jobs are the workflow_dispatch gate under CK0,
       unavailable BY DECLARATION, as at verdicts 79 to 83.
cmd    gh run view 36900722535 --log-failed, the FAILED ids
out    test_the_guard_reads_the_step_being_worked_on
out    test_the_guard_survives_the_state[baseline]
out    test_the_guard_survives_the_state[non_numeric_step_suffix]
out    test_the_guard_survives_the_state[superscript_digit_step_number]
out    test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]
out    test_the_guard_survives_the_state[step_number_is_the_empty_string]
out    test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
out    test_the_guard_survives_the_state[zero_padded_step_number]
out    test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]
judge  NINE, AND CI AND MY RUN AGREE BY NAME ON ALL NINE. CI is RED at the judged
       commit and I record it as red (CA2). Eight of the nine are EG3's state (1).
       The ninth is not, and it is R632.
```

**EG0(c)'S SECOND MACHINE IS MEASURED AND THERE IS NO STOP.** The directive's stop
condition is a shipped assertion, so the question is whether the ladder passed on a
machine neither of us controls:

```
cmd    the ladder job at 47daa3d, the commit that introduced the ceiling
out    run 36898482589, "the verification ladder" SUCCESS, 13 steps, ladder 3 green
cmd    git diff 47daa3d..HEAD --stat -- floatfea tests scripts .github
out    (no output) -- the code has not moved since that run
judge  `test_EG0_the_CEILING_is_the_window_it_claims_to_be` asserts
       `clean < CEILING < weakest` AND `CEILING / clean >= 2.0`, and it passed on
       Linux at the commit that ships the code, and the code is byte-identical at
       HEAD. My own reading is 3.27x. NO STOP ON EITHER MACHINE, and the directive's
       condition is satisfied by a test result rather than by a promise, which is
       exactly how it should have been written.
```

## THE SEVEN RULINGS THE HAND-BACK ASKED FOR, SO THEY ARE ON THE PAGE

**1. a647492's message says `check_carried: all 5 findings carried` and the run says
`all 8`. The self-report is right and the repair is owed.** It is pushed, history stays
linear, and it cannot be amended. **The repair is a claim/cmd/out triple in the next
revision naming the commit, the false figure and the true one** -- and under CP2 that
triple is the whole repair: no number enters the sentence explaining it without its own
command. Closure item C104, not a block: nothing downstream reads that message.

**2. Amending f942b83 from `1281` to `1237` while unpushed was RIGHT, and I want that
said without hedging.** The rule against amending protects PUBLISHED history. An
unpushed commit has none, and a commit whose body is a claim/cmd/out triple carrying a
false `out` line is a commit that would have shipped a measurement nobody could
reproduce. Amending it is the repair; leaving it and correcting it later would have put
two numbers in history where one is right. **The part that matters more than the amend
is that section 6 records it rather than fixing it quietly** -- that is CP2 applied to
the commit that adopts a rule about pasted output, and it is the correct instinct.

**3. Three pasted-figure slips in one session is worth a rule, and here is the wording.**
The diagnosis in the hand-back is right and it is not about arithmetic: all three
figures -- 93000x, 1281, 5 -- were correct when first measured and described a tree
that had moved underneath them. BF0 says the figure carries its command; BP0 says it
carries its rule; CP2 says a repair's numbers carry theirs. **None of them says WHEN
the output is taken.** My proposed sentence, for a directive, in one paragraph:

> **A figure is pasted from the run that produced the artifact it is pasted into, and
> the pasting is the LAST edit (CP3).** Where a commit message, a report section or a
> tolerance comment carries an `out` line, that line is copied from a run executed
> after the final edit to the thing it describes -- not from a remembered run and not
> from a previous round. The consequence is an ordering and not a new check: generate,
> edit, re-run, paste, commit -- **and if an edit follows the paste, the paste is void.**
> Earned three times in one session on figures that were each correct when taken.

This is not apparatus and asks for no new guard, so CZ0 does not bar it. It goes to
Xabier through the implementer; I am not treating it as a HOLD.

**4. FOLLOWING EG0(a)'s DEFINITION OVER ITS PARENTHETICAL WAS RIGHT, and I would have
held on the parenthetical.** A parenthetical that says "approximately" is an
expectation; the definition is the specification, and where they disagree the
expectation is the thing that was wrong. The measurement settles it beyond the balance
argument: **with the WEAKEST counter response as the roof, 16/16 is true by
construction; with the WORST member's response as the roof it is not.** At 2.27e-18 the
roof is 1.464442e-17, which is rotational_block's BEST member, and the weakest member's
3.776640e-18 is then only 1.66x clear -- so the directive's own 16/16 requirement would
rest on 1.66x of a round-off quantity instead of 3.27x. Publishing both windows and
naming the disagreement is the right way to record it.

**5. EG2 TO THE CLOSURE ARTIFACT RATHER THAN TO F2a WAS YOURS TO DECIDE AND YOU DECIDED
IT CORRECTLY.** I checked the ground rather than the argument:

```
cmd    head -4 docs/milestones/F2a.md
out    "# F2 step 4a - verification apparatus"
out    "**SKELETON PLAN. Not locked. Nothing here is built.**"
rule   DZ7c says a ledgered item goes to docs/milestones/F2a.md; F2a section 7 says an
       item found after that commit "is recorded in a verdict and in the milestone's
       closure artifact, and it does not enter this plan"
judge  F2a IS NOT A LOCKED PLAN AND SAYS SO IN ITS SECOND LINE, so ledgering a measured
       finding into it would have been WEAKER than the closure artifact, not
       equivalent. DZ7c's sentence and F2a's own first line conflict; the implementer
       followed the more specific one, which is the file's own statement about itself,
       and recorded the deviation in section 10 rather than taking it. That is the
       behaviour the arrangement is for. NOT A FINDING, and I am not asking for them
       to move.
```

**6. EG4's PREVIEW IS CORRECTLY BLOCKED -- AND ONE OF ITS TWO STATED GROUNDS IS FALSE.**
I checked it rather than taking it, and the conclusion survives while the reason does
not:

```
claim  the floatfea_design_waves directory "does not exist -- the six cases have never
       been run" (report section 7, and the hand-back)
cmd    ls -la ../HSP-runs/studies/platform-12buoy/floatfea_design_waves/
out    IT EXISTS and holds SIX files, dated 27 September:
out      case_T10s_full_H24.2m_head0.csv      626250 bytes
out      case_T12.5s_full_H24.2m_head0.csv    781661
out      case_T14s_full_H24.2m_head0.csv      871739
out      case_T15s_full_H24.2m_head0.csv      931141
out      case_T16.2s_full_H24.2m_head0.csv    993608
out      case_T20s_full_H24.2m_head0.csv     1220383
judge  REFUTED BY ONE ls, and it contradicts the LOCKED PLAN's own DV2 -- "the six
       cases are run, settled and exported ... 1481.7 s total". The six periods are
       exactly DJ2(b)'s: 10.0, 12.5, 14.0, 15.0, 16.2, 20.0 s at H = 24.2 m, head 0.
claim  the export cannot supply gimbal reactions
cmd    head -1 on case_T10s..., columns counted, header grepped for
       lam reaction constraint multiplier force moment
out    21 columns: t_s, platform_heave_m, platform_heave_acc_mps2, and surge/sway/
out    heave plus acceleration for buoy1_clusterA, buoy4_clusterB, buoy7_clusterC
out    ZERO matches for any reaction-like name
rule   CLAUDE.md section Non-negotiables: never invent a load distribution
judge  THE BLOCKER STANDS, ON THIS GROUND. Nine of twelve buoys are absent, the
       platform has one DOF of six, no external force is exported, so neither the
       multipliers nor F_ext minus M a is available for any body. Refusing to invent a
       load and escalating is the right call. **But the escalation must not reach
       Xabier saying the cases were never run**, because that is the one sentence in
       it he can check in five seconds and it is false. C103.
```

**7. "NO TOLERANCE WAS WIDENED IN F3" IS TRUE AND I VERIFIED IT. "FIVE DECADES TIGHTER"
IS FALSE.**

```
cmd    git diff 580b183..HEAD -- floatfea/tolerances.py, the value lines only
out    + PLATFORM_RIGID_MODE_EXACTNESS: Final[float] = 1.154338e-18
out    + PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT: Final[float] = 1.0e-14
out    no existing NAME = value line changed, in either direction
cmd    1e-15 / 1.154338e-18
out    866.3x, which is 2.94 decades
cmd    where the claim is written
out    docs/closure/F3.md:154 and docs/reports/F3/step-3.md:512 -- "five decades"
rule   a tolerance change requires a written justification naming the physical or
       numerical reason the previous value was incorrect (CLAUDE.md section Tolerances)
judge  THE DIRECTION IS RIGHT AND THE JUSTIFICATION IS SOUND: the gate's threshold
       moved from 1e-15 to 1.154338e-18, which is strictly stronger, the reason is in
       the entry, and the previous value's own entry pre-registered the re-derivation
       in words I quote in R634. THE MAGNITUDE IS WRONG BY TWO ORDERS AND NO READING
       GIVES FIVE: 1e-14/1.154338e-18 is 3.94 decades and 1e-15/1.154338e-18 is 2.94.
       It is a figure, so C101 and not a block -- but it is the fourth pasted figure of
       the session and it is in the closure artifact, which is the document a later
       reader trusts most.
```

## Carried

Verdict 83 carried five items by name and listed them as blocking in step 3.

* **R624 -- ANSWERED at 47daa3d, and I re-derived it rather than accepting it.** The
  substance is in R636 below. Both halves land: the gate gets its own ceiling, and the
  refusal keeps `1e-15` with the emptiness of the band window stated as the reason.
  **My independent sweep confirms the emptiness, which is the load-bearing half:**

```
cmd    40000 admissible (D_o, t/D_o, L) points, L constrained to L/D >= 2 and
       L/r <= 300, S355-equivalent; worst clean element_rigid_residual and weakest
       response over the three counters at the declared 1e-14
out    clean worst     1.872454e-17  at D_o 1.1791, t/D_o 0.011654, L 2.4762
out    weakest counter 1.569787e-19  rotational_block at D_o 4.0845, t/D_o 0.17689,
out                                  L 364.51
rule   a single ceiling would have to sit above every clean reading and below every
       counter response
judge  THE FLOOR IS ABOVE THE ROOF BY 119.3x, ON A GRID NEITHER OF US DESIGNED
       TOGETHER. The decision is sound and R624 is CLOSED. My counter figure agrees
       with the plan's 1.571633e-19 to three figures; my clean worst is 3.54x WORSE
       than the published 5.287607e-18 and consistent with verdict 83's own
       1.956747e-17, which is C102 and not a change to the ruling.
```

* **R629 -- NOT CLOSED. IT CHANGED SHAPE AND IT IS RED ON BOTH MACHINES. R632.** The
  fix at 0d911ce took the data half of the closing condition and neither of the two
  alternatives the condition required. The vacuity is gone from step 2's report and
  the guard is unchanged -- and step 3's own answers file puts fourteen of twenty-two
  rows back at section 9, which is again a bulleted list naming every item. The state
  now fails earlier than it used to: it cannot be BUILT.
* **R630 -- ANSWERED at 47daa3d, verified line by line, and answered better than I
  asked.** The condition was that the test comment name which end of the sixteen its
  three edges are. It does more: it carries THREE labelled sets -- the best member,
  the worst against the retired ceiling, the worst against the ceiling that ships --
  each with its rule, and the third is printed per run by the new cell rather than
  typed. I re-bisected all three sets and every figure reproduces:
  `6.266629e-17` on platform:hub4_arm, `1.262927e-18` on hub4:buoy12_arm,
  `3.088842e-15` on platform:hub4_arm, spreads 2.14x, 1.03x, 3.93x. **And no injection
  size was chosen against the best member:** the declared `1.0e-14` clears the WORST
  edge `3.088842e-15` by 3.24x, which is the condition's second half.
* **R631 -- OPEN, LEDGERED to `docs/closure/F3.md` section 4, and I ACCEPT the ledger
  under DZ7c.** No value moves, nothing it touches can change a member force or the
  G4.1 equilibrium check, and DZ7c's standing answer is reduce scope rather than slip.
  Element (iii) of its condition -- the insensitivity window -- is still unmeasured and
  the ledger says so. **It does not carry as blocking into F4; it carries as a
  recorded item in the closure artifact**, which is what DZ7c asks for this class.
* **R626's residue -- OPEN, LEDGERED to the same place, same ruling.** The two
  boundaries are written in verdict 83 and quoted in the ledger, so nothing has to be
  re-derived by whoever picks it up.
* **C88 -- STILL OPEN and its one condition WAS NOT MET.** Verdict 83 ruled that it
  waits for the closure commit with one condition: "it lands BEFORE step 3 chooses an
  injection size, because step 3 reads those rows." Step 3 chose `1.0e-14` and the
  plan block's citation is untouched at this commit. **The choice turned out right
  anyway -- I verified it against the worst member -- so this is a closure item and not
  a block**, but the condition was a condition and it was missed, and I am recording
  that rather than quietly re-ruling it.
* **C97, C98, C99, C100 -- C99 is CLOSED at f942b83**, in my own wording, unparaphrased,
  with EG3's two conditions beside it. C97, C98 and C100 are untouched and still
  closure.
* **C86, C90, C91, C92, C93, C94, C95, C96 -- STILL OPEN, closure, not re-reviewed.**
  Nothing on that list has become blocking in my reading this round.
* **C74, C76, C78, C82, C85, R610, R615 -- carried unchanged, no work asked.**
* **C40 -- CLOSED at 47daa3d, and I checked the repair rather than the claim.** The
  plan guard reads every `docs/milestones/F*.md` now and names the file it read in its
  failure message. One residue, C107: the glob reaches two files that are not locked
  plans.
* **C75, C75b -- closed and still closed.** `ruff`, `black --check` and `mypy` all
  SUCCEEDED on CI at this commit.
* **R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621,
  R623, R625, R627, R628 closed as ruled at 79, 81, 82 and 83. R622 is F4. C89 stays
  withdrawn.**
* **C58 to C64, C65 to C73, C56(iii), C56(iv), C57 -- as ruled at verdicts 77 to 83.**
  This step's diff touches none of them.

## Findings

**R632. (d, BLOCKING) ONE OF THE NINE REDS IS NOT THE STEP-BOUNDARY CLASS. THE PLANT
ACTION CANNOT BUILD ITS STATE AGAINST A FIRST-REVISION REPORT, SO IT RAISES BEFORE
ANYTHING IS MEASURED -- AND THIS WILL RECUR AT EVERY FIRST REVISION OF EVERY STEP.**
EG3(i) requires each FAILED id matched by name to the state's own list. I matched all
nine by CAUSE and not by family, which is the lesson R629 was:

```
cmd    python -m pytest tests/test_report_guard_states.py -q --tb=line
out    8 failed, 16 passed in 165.97s
out    tests/test_report_guard_states.py:777: AssertionError:
out      zero_padded_step_number: a file that is not a numbered step must be stepped
out      over, not reacted to.   assert 1 == 0
out    tests/test_report_guard_states.py:545: ValueError: substring not found
cmd    the baseline's own nested failure
out    "step 3 has a report and no verdict yet. That is the legitimate boundary ...
out     Invoke the gating-supervisor."    assert 3 == 2
cmd    tests/test_report_guard_states.py:539-546, the pointers_all_at_carried action
out    head = text.rindex(the literal hash-Revision-space)
cmd    count that heading in the two reports
out    docs/reports/F3/step-2.md   1
out    docs/reports/F3/step-3.md   0
rule   EG3(i): the waiver applies only if EVERY red traces BY NAME to the
       step-boundary cause, and a red that does not match is CZ1 (iv) unchanged
judge  EIGHT OF NINE ARE STATE (1): the baseline fails because step 3 has a report and
       no verdict, and seven planted states cascade off it with assert 1 == 0. THE
       NINTH FAILS INSIDE THE HARNESS, with a ValueError in the plant action, and its
       cause has NOTHING TO DO WITH WHETHER A VERDICT EXISTS -- step-3.md is revision
       1 and carries no revision heading, so rindex raises and the state is never
       built. The verdict I am writing will clear the other eight. It will not clear
       this one.
```

**This is R629 in a second shape and the shape is worse**: before, the state planted and
could not discriminate; now it cannot plant at all, so a guard that is supposed to prove
the pointer check can fail instead reports a Python error. CZ0 is explicit that an
existing guard that fails false is fixed or deleted, never extended, and a guard that
raises on a legitimate tree state is failing false.

**Closed when** one of two things, both inside CZ0: **(i)** the plant action handles a
report with no revision heading -- plant into the whole file when there is no revision
boundary -- and the state then REDDENS, demonstrated by the nested run's own failure
line rather than by the state merely passing; or **(ii)** the state is deleted under DR1
and its vacuity is recorded in the closure artifact, standing in my corpus row as what
was measured. **And in either case**, `docs/reports/F3/step-3-answers.json` points
fourteen of its twenty-two rows at section 9 of step-3.md, which is "Where each carried
item stands" -- a bulleted list naming every item. That is the same pointer-that-cannot-
discriminate the original R629 was about, reproduced in the file written one commit
after it was fixed. **At the answering commit `python -m pytest -q` reads `0 failed`
apart from EG3 state (1), and a pushed CI run at that sha shows the same.**

**R633. (b, BLOCKING) THE NEW ENTRY'S FIRST SENTENCE SAYS ITS THREE COUNTERS ARE
REGISTERED IN `tests/test_counters_are_injected.py`. THEY ARE NOT, THE LOCKED PLAN
REQUIRES THEM TO BE, AND I MEASURED THAT THE COUNTER AS WRITTEN CANNOT BE REGISTERED --
IT FAILS THE GATE CELL ON ALL THREE KINDS.** This is not a missing table row.

```
cmd    grep -rn "PLATFORM_RIGID_MODE_EXACTNESS" tests/test_counters_are_injected.py
out    (no output)
cmd    git diff 580b183..HEAD --stat -- tests/test_counters_are_injected.py
out    (no output) -- the file is untouched by this step
cmd    floatfea/tolerances.py:354-355, the new entry's opening
out    "CLASS: ACCURACY -- hosts the three element-local counters registered in
out     tests/test_counters_are_injected.py against G2.1's gate on the real platform."
cmd    docs/milestones/F3.md section 5, the locked requirement
out    "And its three counters go back into the injection guard. ... here it is an
out    assertion again, so dropped_flip, wrong_dof_index and rotational_block are
out    registered against it."
cmd    tests/test_counters_are_injected.py:317-319, the guard's own promise
out    "It goes back UP in F3, where the element-local check becomes an assertion on
out    every real platform member and its three counters are registered against that
out    gate."
cmd    the registry, and what the completeness meta-test asserts
out    REGISTERED holds FOUR rows; test_there_is_something_to_check asserts
out    len(REGISTERED) >= 4 -- so a fifth constant with no row is invisible to the one
out    meta-test whose docstring says "A constant with no counter registered here is
out    not covered at all"
rule   (b): a tolerance's counter and HOW IT IS INJECTED. BX0's two cells are what
       prove a counter is not self-asserting; a constant absent from the registry has
       neither cell run against it.
judge  FOUR PLACES IN THE TREE SAY THIS HAPPENED OR WILL HAPPEN IN F3, F3 IS BEING
       CLOSED, AND IT DID NOT HAPPEN. And the omission is not clerical:
```

```
cmd    build the REGISTERED row by hand for test_EG0_the_THREE_COUNTERS_redden_every_
       member and run both BX0 cells per kind -- gate cell neuters
       test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions, ceiling cell widens
       PLATFORM_RIGID_MODE_EXACTNESS to 10 x 1e-14
out    dropped_flip      gate cell False   ceiling cell True
out    wrong_dof_index   gate cell False   ceiling cell True
out    rotational_block  gate cell False   ceiling cell True
rule   test_the_counter_fails_when_its_gate_is_neutered asserts the gate cell is True;
       test_the_counter_fails_when_its_ceiling_is_widened asserts the ceiling cell is
judge  THE CEILING CELL PASSES ON ALL THREE -- the counter IS sized by the constant, so
       the substance is sound and I am not claiming the counter is defective. THE GATE
       CELL FAILS ON ALL THREE, because the counter reimplements the comparison
       `r > PLATFORM_RIGID_MODE_EXACTNESS` inline instead of calling the gate it
       defends: neuter the gate and the counter still passes, which is precisely what
       that cell reports as self-asserting. Registering it is therefore a CODE CHANGE
       with a design decision in it, not a one-line addition a closure commit absorbs,
       and that is why this is (b) and blocks rather than going on the closure list.
```

**Closed when** one of three, and the choice is the implementer's: **(i)** the counter
runs the gate -- call `test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions` under
`pytest.raises` with `member_stiffnesses` patched to return the injected rows, which is
why that function is module-level and not a fixture -- and a row is added to
`REGISTERED`, with both cells green and the `>= 4` in `test_there_is_something_to_check`
moved to `>= 5` so the registry cannot silently lose it again; or **(ii)** all four
sentences are corrected to say what is true -- that the counters are asserted 16/16 by
`tests/verification/rung3/test_platform_rigid_modes.py` and are NOT in the BX0 registry,
with the reason -- in `floatfea/tolerances.py:354-355`, `docs/milestones/F3.md` section 5
and section 7, and `tests/test_counters_are_injected.py:317-319`; or **(iii)** the
registration is ruled out of scope by directive, in which case all four sentences change
anyway. **What may not stand is the present state: a tolerance entry naming a guard that
does not read it.** No new apparatus in any branch -- (i) adds a row to an existing list,
(ii) deletes four sentences.

**R634. (b, BLOCKING) `floatfea/tolerances.py` SAYS NOTHING ASSERTS
`RIGID_MODE_EXACTNESS` AND THAT IT BOUNDS NOTHING, SEVENTY-THREE LINES ABOVE A SENTENCE
THIS STEP'S OWN COMMIT WROTE SAYING THE PRODUCTION BUILDER KEEPS IT. ONE FILE, TWO
ANSWERS, AND THE LIVE ONE IS A REFUSAL ON THE PRODUCTION PATH.**

```
cmd    floatfea/tolerances.py:330
out    "AND NOTHING ASSERTS THIS CONSTANT ANY MORE (DI0, R530)."
cmd    floatfea/tolerances.py:345-348
out    "The constant is kept because the diagnostic and the closure artifact both read
out    it as the scale the retired quantity was measured against. Its CLASS line above
out    still says ACCURACY and that is now wrong in spirit: it bounds nothing."
cmd    grep -rn "RIGID_MODE_EXACTNESS" floatfea/ | grep -v PLATFORM
out    floatfea/model/platform.py:319    if residual > RIGID_MODE_EXACTNESS:
out    floatfea/model/platform.py:320    raise ValueError(... "The platform is refused
out      rather than analysed (F3 section 5, G2.1).")
cmd    floatfea/tolerances.py:403, written by THIS STEP at 47daa3d
out    "floatfea.model.platform.check_rigid_modes keeps RIGID_MODE_EXACTNESS, because
out    the refusal's subject is every deck a reader could write"
rule   CW0: a claim about this repository written in a comment is a test, a triple, or
       deleted -- and (b), because this paragraph is the ONLY statement of what this
       constant is for and the constant is the threshold the builder refuses on
judge  THE SENTENCE WAS TRUE WHEN WRITTEN AND THE REFUSAL LANDED AFTER IT, so it is
       pre-existing and I am not pretending otherwise. But THIS STEP is the commit that
       split the two ceilings and made this entry the record of the REFUSAL's ceiling,
       and it is the commit that wrote the contradicting sentence into the same file.
       docs/closure/F3.md section 3 now publishes RIGID_MODE_EXACTNESS in a column
       headed "the refusal", so a reader sent there arrives at an entry saying the value
       bounds nothing. A reader deciding whether 1e-15 may move would be told by its own
       Reason paragraph that nothing depends on it, and the production builder would
       stop refusing a defective deck.
```

**Closed when** lines 330 and 345-348 say what is true at the commit that publishes them:
that `RIGID_MODE_EXACTNESS` is asserted by `check_rigid_modes` at
`floatfea/model/platform.py:319` as the G2.1 REFUSAL's ceiling, that its subject is every
deck a reader could write, that no counter is registered against it and why -- the band
window is empty, which I confirmed independently at 119.3x -- and that what DI0 and R530
retired is the F2 claim-A assertion rather than every use of the constant. The
`CLASS: ACCURACY` line is then correct rather than "wrong in spirit". **The
pre-registration sentence at lines 348-352 is kept exactly as written, because EG0
fulfilled it to the letter and that is worth a later reader seeing.** No value moves.

**R635. (c, NOT BLOCKING, recorded with its measurement because it will fire) THE WINDOW
IS GUARDED ASYMMETRICALLY, AND EG0(c)'s 2x CLAUSE FIRES ON ROUTINE LEGAL CHANGES WHILE
THE DIRECTIVE AND THE TOLERANCE ENTRY GIVE OPPOSITE INSTRUCTIONS FOR WHAT TO DO THEN.**
The gate is correct today; this is about the next section change.

```
cmd    which assertion binds each side of the window, and at what factor
out    floor  PLATFORM_RIGID_MODE_EXACTNESS / clean >= 2.0, in
out           test_EG0_the_CEILING_is_the_window_it_claims_to_be         2x
out    roof   reddened == 16, in test_EG0_the_THREE_COUNTERS_redden_every_member   1x
judge  A SYMMETRIC WINDOW GUARDED ASYMMETRICALLY. Both margins read 3.27x today; a
       3.27x drift of the rotational_block response reddens the roof with no warning
       band first, while the same drift on the clean side is caught at 2x. That is the
       directive's design rather than a defect, and it is worth knowing which side has
       no margin clause.
cmd    hold the sixteen-member geometry and move the arm wall through the legal range,
       reading the clean worst as a fraction of the ceiling
out    t = 150 mm  0.35x     t = 160 mm  0.19x     t = 170 mm  0.87x
out    t = 175 mm  0.12x     t = 180 mm  0.08x     t = 185 mm  0.78x
out    t = 190 mm  0.34x     t = 200 mm  0.23x     t = 220 mm  0.37x
out    t = 250 mm  0.29x
cmd    the same with E at 200 GPa instead of 210, section and lengths held
out    clean worst 7.786002e-19 = 0.67x the ceiling, so 1.48x inside
rule   EG0(c): if either machine's clean worst comes within 2x of the ceiling, STOP and
       report; do not move the ceiling
judge  TWO OF TEN LEGAL WALL THICKNESSES AND ONE ROUTINE GRADE CHANGE LAND INSIDE THE
       STOP BAND -- 170 mm at 1.15x, 185 mm at 1.29x, 200 GPa at 1.48x -- and F1's own
       order check brackets exactly that thickness range ("t ~ 175 mm closes it, so
       180 mm is the buildable number"), with DV0 recording that the section "should be
       re-examined, not treated as settled". The clean worst is round-off scatter and
       not a trend: it moves between 0.08x and 0.87x across neighbouring thicknesses.
       So the first time the arm is re-sized the shipped gate STOPs, and EG0(c) says do
       not move the ceiling while the entry says "this value is re-derived rather than
       re-justified". Those are two instructions and they disagree.
```

**My reading, offered so the next round does not spend itself on it:** the entry is right
and EG0(c) means "do not WIDEN the ceiling to rescue a red", not "never re-derive it". A
re-derivation at a changed section is a new measurement of the same rule, and BP0 already
requires every figure citing the old ceiling to move with it. **That needs a sentence
where a later reader finds it, and it is a directive rather than a round.** Not blocking:
no assertion is wrong today, every figure reproduces, and the risk is dated rather than
present.

**R636. (NOT A FINDING -- THE RESULT, RECORDED BECAUSE NOBODY MEASURED IT AND IT IS THE
BEST THING IN F3.)** What the new ceiling BUYS. The report justifies the change by what
the old ceiling could not do; the stronger statement is what the new one can:

```
cmd    per member, bisect the injection size at which the residual crosses the ceiling;
       take the LARGEST over the sixteen; against 1e-15 and against 1.154338e-18
out    dropped_flip      5.285599e-14 -> 6.266629e-17    843.5x smaller
out    wrong_dof_index   1.094071e-15 -> 1.262927e-18    866.3x smaller
out    rotational_block  2.642868e-12 -> 3.088842e-15    855.6x smaller
rule   element_rigid_residual(k_local, L) <= the ceiling, per member, worst over the
       sixteen
judge  THE GATE NOW DETECTS DEFECTS ABOUT 850x SMALLER ON EVERY MEMBER. That is what
       makes this a tightening rather than a renaming, and it is the sentence I would
       have put in the closure artifact instead of "five decades".
cmd    the window as a decision rule, inverted and solved on both edges
out    lowest ceiling the shipped assertions accept   7.056514e-19 (the 2x clause)
out    highest ceiling they accept                    just under 3.776640e-18
out    so the constant is pinned inside a 5.35x interval, 1.64x and 3.27x from its edges
cmd    invert the COUNTER-SIZE rule and bisect
out    at 3.100e-15 all three counters read 16/16; at 3.050e-15 the worst reads 12/16
out    so the declared 1.0e-14 clears a SOLVED boundary by 3.24x
cmd    the same platform expressed in millimetres, a thousand-fold unit change
out    clean worst 0.33x the ceiling, weakest counter 3.28x -- STILL INSIDE
judge  FOUR THINGS A CEILING USUALLY DOES NOT HAVE: both edges solved rather than
       sampled, a counter size measured against a bisected boundary, a pinning interval
       narrower than one decade, and survival of the unit-scaling case that moved the
       RIGID_MODE_BOUND band figure by 24x. I tried to break this and could not.
cmd    and one reach boundary, so the tightening is not over-read
out    the WHOLE MATRIX negated: residual 8.7211e-20 clean, 8.7211e-20 negated, against
out    a ceiling of 1.154338e-18
judge  866x of extra sensitivity buys NOTHING against a sign error. R625's signed clause
       is still the only thing that sees one, and that deserves a sentence beside a
       ceiling advertised as a sensitivity gain.
```

## Closure items

Named, not re-reviewed, none of them holding anything. Fix the list once in the step
closure commit and verify it AFTER it exists (CZ1).

* **C101.** "five decades tighter" at `docs/closure/F3.md:154` and
  `docs/reports/F3/step-3.md:512`. The ratio is `866.3x`, which is 2.94 decades; the
  direction is right and verified. **Closes when** both places carry the measured ratio,
  and R636's `843.5x / 866.3x / 855.6x` detection gain is the figure that replaces it,
  since that is what the reader wants from the sentence.
* **C102.** `docs/closure/F3.md:69` and `docs/milestones/F3.md:677` pair the refusal's
  clean worst `5.287607e-18` with the margin `51.1x` in the same cell. `1e-15` over
  `5.287607e-18` is `189x`; `51.1x` belongs to verdict 83's `1.956747e-17`, and my own
  40000-point grid this round found `1.872454e-17`. The plan's phrasing "sits 51.1x inside
  the clean worst" also reads backwards. **Closes when** the cell carries one sweep's
  worst and that sweep's margin, with the worst of every grid tried -- `1.956747e-17` is
  the number today.
* **C103.** `docs/reports/F3/step-3.md` section 7 and the escalation it feeds say the six
  design-wave cases have never been run and the export directory does not exist. Six CSVs
  dated 27 September are there, which is what the locked plan's own DV2 records.
  **Closes when** the escalation reaches Xabier on the ground that holds -- 21 columns, no
  reaction, no external force, nine of twelve buoys absent -- and the false ground is
  struck in place.
* **C104.** `a647492`'s message says `check_carried: all 5 findings carried`; the run says
  `all 8`. Pushed and unamendable. **Closes when** the next revision carries a
  claim/cmd/out triple naming the commit, the false figure and the true one, with every
  number in the explanation inside its own triple (CP2).
* **C105.** The report's section 0 is headed "CI at `29570e1`, the commit verdict 83
  judged". Verdict 83 judged `b105de1` and its own stamp reads `5a2ff21`; `29570e1` is
  verdict 81's. `scripts/ci_section.py` is resolving the OLDEST `Reviewed commit:` line in
  the verdict file rather than the newest, which is the DX2 append-ordering trap one file
  over. Section 0a does cover this round's commits, so nothing is hidden -- but the table
  is labelled with the wrong commit. **Closes when** the anchor is the newest round's
  judged commit, or the heading says which round it is about.
* **C106.** `tests/verification/rung3/test_platform_rigid_modes.py:326-340` duplicates
  `scripts/rigid_counter_response.py:82-92`. The two are equivalent today -- I compared
  them -- and the only statement that the gate and the published sweep inject the same
  defect is the docstring. Nothing imports, nothing compares. **Closes when** the test
  imports the script's shape or the docstring stops claiming provenance it cannot carry.
* **C107.** `tests/test_plan_matches_tolerances.py:40` globs `docs/milestones/F*.md`, which
  returns `F2a.md` ("SKELETON PLAN. Not locked.") and `F2_figures.md` ("GENERATED, do not
  edit") beside the three locked plans. A tolerance value written into either would satisfy
  `test_every_declared_tolerance_appears_in_the_plan`. Latent, not live: 56 rows come from
  F2.md, 3 from F3.md, zero from the other three. **Closes when** the list is the locked
  plans or the set of files read is asserted.
* **C108.** `docs/closure/F3.md` section 5, "What is red at the closing commit", states a
  pointer and no content. **Closes when** it names the nine FAILED ids at the closing
  commit and the cause of each, which after R632 is eight in one class and one in another.
* **C109.** `docs/milestones/F3.md` now runs 0,1,2,3,4,5,7,8 -- the new section 7 was
  inserted and the old section 6 renumbered to 8, so there is no section 6.
  **Closes when** the numbering is contiguous or the gap is stated.
* **C88** -- still open, its one timing condition missed; ruled in `## Carried`.
* **C97, C98, C100, C86, C90, C91, C92, C93, C94, C95, C96** -- carried unchanged.
* **C74, C76, C78, C82, C85, R610, R615** -- ledger lines, carried unchanged.
* **C89** -- withdrawn and staying withdrawn. **C99, C40** -- CLOSED this round.

## Tolerances touched

```
cmd  git diff 580b183..HEAD --numstat -- floatfea/tolerances.py
out  80  0
cmd  the same diff, lines matching a NAME = value declaration
out  + PLATFORM_RIGID_MODE_EXACTNESS: Final[float] = 1.154338e-18
out  + PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT: Final[float] = 1.0e-14
out  no existing NAME = value line changed, in either direction
cmd  git diff 580b183..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep -i conftest
out  tests/conftest.py and tests/test_supervisor_conftest_pathspec.py -- one conftest
out  in the tree; no rung carries its own, and no plugin is loaded from tests/
cmd  tests/conftest.py, read line by line (CH2), unchanged this round and read anyway
out  it registers a hypothesis profile, adds a rung marker from the directory and SORTS
out  items by rung. No pytest_runtest_makereport, no pytest_ignore_collect, no
out  pytest_collection_modifyitems that removes an item, no outcome written.
judge  TWO VALUES DECLARED, NONE WIDENED, NO GOLDEN AND NO PARAMETRISATION LOOSENED.
       The one ASSERTION that moved -- the G2.1 gate's ceiling -- moved DOWN by 866.3x,
       which I verified by bisecting the detection edge before and after (R636). A
       tolerance declared in the same commit as the code that reads it is normally the
       finding; here the code is a new gate and the value is derived from a window the
       same commit measures, with both edges solved. That is the admissible form of it.
```

| constant | value | form | counter | justification located |
|---|---|---|---|---|
| `PLATFORM_RIGID_MODE_EXACTNESS` | `1.154338e-18`, NEW | relative and dimensionless -- the element-local residual is homogenised by `S^-1 k S^-1`, so span, orientation and reference point leave the quantity; correct form | `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1.0e-14`, three shapes, 16/16 each, binding edge `3.088842e-15` cleared by `3.24x`. **The counter is a detection THRESHOLD and not one perturbation** -- I re-bisected it and found `12/16` at `3.050e-15` | `floatfea/tolerances.py:354-409`, the table in `docs/milestones/F3.md:667`, and the derivation re-run by `test_EG0_the_CEILING_is_the_window_it_claims_to_be` at every run rather than typed (BI3 satisfied). **The one false sentence in it is R633.** |
| `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | `1.0e-14`, NEW | a fraction of `max abs k_e`, dimensionless; correct form | it IS the counter | `floatfea/tolerances.py:411-434`. The reuse of `RIGID_MODE_EXACTNESS_COUNTER_DEFECT`'s value is argued rather than assumed, and the entry says what would separate them. **R633 applies here too: nothing in the BX0 registry reads this name.** |
| `RIGID_MODE_EXACTNESS` | `1e-15`, UNCHANGED | unchanged | **none, and none is possible** -- the band window is empty, which I confirmed independently at `119.3x` | its own entry, and that entry is **R634**: it says nothing asserts the constant while `floatfea/model/platform.py:319` refuses on it. |
| `RIGID_MODE_BOUND` | `199.526231496888`, UNCHANGED | unchanged | unchanged | unchanged. **R631** is its open residue, ledgered. |

## My own instructions (4b), read line by line

```
cmd  git diff 580b183..HEAD --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out  CLAUDE.md 43 +, docs/SUPERVISOR.md 42 +, 0 deletions
cmd  git show --stat f942b83
out  CLAUDE.md and docs/SUPERVISOR.md ONLY. No floatfea/, no tests/, no scripts/.
cmd  git log --oneline 580b183..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out  f942b83 only -- one commit, and its subject cites EG3 and EG4e
judge  NO STOP-CLASS PROCESS FINDING, and I verified it the way the rule requires:
       by the diff, not by the subject. The change is a standalone `process:` commit
       citing the directives that asked for it, it is PURELY ADDITIVE -- 85 insertions,
       zero deletions, measured -- and no guard is removed, weakened or narrowed.
       Both files receive the same two blocks. The CZ1 carve-out block is MY verdict-83
       wording with the sharpening quoted verbatim, which is what C99 asked for, and
       EG3's two conditions are added beside it rather than inside it. `.claude/` is
       untouched. C99 is CLOSED.
cmd  and the one thing I checked that the diff does not show: does the carve-out
     NARROW what I must read or carry?
out  No. It waives a PRE-INVOCATION green requirement on the implementer's side and
out  adds condition (i) requiring the trace pasted per id and condition (ii) requiring
out  the verdict commit measured. Both increase what is measured. Nothing in it
out  changes what I diff, what I carry, or what I may write.
```

## THE EXCLUSION: DID IT HIDE ANYTHING? YES, AND IT IS R632

```
cmd    the report's own whole-suite line, section 12
out    "Whole suite at 7e86d2a: 2664 passed, 0 failed, 0 skipped" and "the excluded
out    set: 270 passed, 20 failed", measured at 7e86d2a -- the commit BEFORE the report
cmd    my own run, whole tree, no exclusion, at the committed revision a647492
out    9 failed, 2976 passed
judge  THE TWO ARE NOT COMPARABLE AND NEITHER IS WRONG. The report's is the tree minus
       three files at the commit before the report existed; mine is the whole tree at
       the commit that ships it. CZ1's reusable half is exactly this: the plant action
       reads the NEWEST report, and at 7e86d2a the newest report was step-2.md, which
       HAS a revision heading. The ValueError cannot exist until step-3.md is committed,
       so no run the implementer could have taken before committing would have shown it.
       THE NUMBER THAT DECIDES ANYTHING IS MINE, AND IT IS 9 FAILED.
cmd    the report's EG3(i) trace, section 12
out    "THE EXCLUDED SET'S 20 ARE THAT CASCADE" -- asserted for the family, with three
out    ids traced individually and seventeen by class
rule   EG3(i): each FAILED id is matched to the state's own list, not "the failures look
       like the boundary set"
judge  THE TRACE IS THE RIGHT SHAPE AND IT IS NOT FINISHED. The report is right that the
       condition caught two gaps in the clause's state-(2) list on CI, and right to
       record them as unlisted rather than waived -- that is the condition working. What
       it did not do is give each of the twenty a cause, and the one that needed it is
       the one that is not the boundary. EG3(i) earned itself on its first use, twice
       over: once the way the report describes, and once the way it did not.
```

**On the two UNLISTED ids the report flags for a directive, my ruling:**
`test_the_answered_verdict_is_the_NEWEST_one` and the `the_guard_survives_the_state`
cascade at `47daa3d` ARE state (2) by cause -- the report in the tree answered verdict 82
while 83 existed, and the baseline cascade follows -- and the clause's list does not name
them. **Recording them as unlisted rather than waived was the correct call and I would
have found a widened list a worse answer.** The list was written from one observation; it
is short by two names on each side. **My wording, so the channel is a verdict and not an
agent message:** *state (1)'s list is `test_the_guard_reads_the_step_being_worked_on` and
`test_the_answered_verdict_is_the_NEWEST_one`, plus the planted states that cascade off a
red baseline; state (2)'s is the five named plus the same cascade. In both states the
cascade is identified by the baseline being red and by each cascading state's own failure
line, not by its name.* That is four lines and it narrows nothing.

## The adversarial corpus (BE3)

`tests/corpus/platform_ceiling_and_counter_registration.txt`, batch 31, committed
separately from this verdict at `6c4e651`. **TWENTY-SIX ENTRIES, ALL TWENTY-SIX UNSEEN.**
In scope under DE2: the element, the gates, the platform model; section E is the
report-guard harness, in scope because it holds the only red here that is not the step
boundary.

**FOURTEEN ROWS PREDICT `caught`. ONE READS CAUGHT.** That is the worst coverage of the
milestone -- batch 29 was 8 of 13, batch 30 was 5 of 10 -- and the shape of the miss is
again the finding: **not one of the thirteen misses is the element.** Eight are sentences
in `floatfea/`, `tests/` and the artifacts that no check reads (R633, R634, C101, C102,
C103, C106, and the two record rows); five are reach boundaries of the new ceiling and of
two guards that nothing was asked to measure (R635, C107, and the registry's `>= 4`).
**The one that reads CAUGHT is R632**, and it is caught as a hard error rather than as a
reported defect, which is the finding rather than the coverage.

**Two rows are `expect=blind` and both matter.** The millimetre unit system: the ceiling
stays inside the window under a thousand-fold change of length unit, which is the first
figure in this family that survives that case -- batch 30 measured the `RIGID_MODE_BOUND`
band reading moving `24x`. And the whole matrix negated: `866x` of extra residual
sensitivity buys nothing against a sign error.

```
cmd  grep -c "^id=" tests/corpus/platform_ceiling_and_counter_registration.txt
out  26
cmd  grep -rn "platform_ceiling_and_counter_registration" tests/ scripts/ --include=*.py
out  (no output) -- named by no .py
cmd  python -m pytest tests/test_collected_set_golden.py
       tests/test_marker_exemption_corpus.py tests/test_report_vocabulary_corpus.py
       tests/test_tree_prose_consistent.py tests/test_ci_ladder_gating.py -q
out  300 passed in 132.51s        exit 0
judge  THE CORPUS COMMIT REDDENS NOTHING, measured and not reasoned.
```

**EG4(e) notes that batches pause AFTER this step, so this is the last general batch.**
F4's load-mapping gate and EB6's label-provenance gate continue, and on the measurement
above that is the right place to spend: thirteen of fourteen misses this round were
records rather than reachable defects, and the two surfaces EG4(e) keeps open are the two
where a miss reaches a member force.

Every mutation was applied in a scratch harness under the session scratch directory,
importing the shipped functions; nothing in the working tree was written.
`git status --porcelain --untracked-files=all` was empty before I began, and the only
paths I have written in this repository are that corpus file and this verdict.

## On the criterion

**I ruled under CZ0 and I have no complaint about the criterion this round.** Of my six
numbered items, one is (d) measured on two machines, two are (b) in `floatfea/tolerances.py`,
one is (c) recorded and explicitly not blocking, one is a result rather than a finding, and
nine are closure items I have named and will not re-review. **No round was spent on prose
and no round was spent re-reading the closure list**, which is what CZ0 is for.

**One thing I want on the record about the shape of this HOLD, because it is unusual.**
Two of my three blocking items are SENTENCES, which CZ0 retires as a blocking head, and I
am blocking on them anyway on the ground my own instructions give: *a docstring that is
the only statement of what a tolerance means*. Both qualify exactly. R633's sentence names
a guard as the thing that proves a counter is not self-asserting, and I measured that the
guard does not read it and cannot as written -- that is not "a figure is wrong", it is
"the mechanism named does not exist". R634's paragraph tells a reader that a constant the
production builder refuses on bounds nothing. **If either had been a sentence about a
measurement rather than about a mechanism, I would have put it on the closure list, and
verdict 83's sharpening is the test I used: does moving the sentence move a decision?**
For both, yes.

**And the cap.** This is round 1 of 3 on step 3. The three blocking items are one guard
repair, one registry decision, and one paragraph rewrite; none of them is a day of work,
and none of them touches a number. If they land, step 3 closes at round 2 and F3 closes
with it.

## Next step opens when

**Step 3 is HELD. These are answered before anything else, and F3 does not close until
they are.** The specific conditions, so that "address the above" is not what this says:

1. **R632.** `python -m pytest -q` at the answering commit reads `0 failed` apart from
   EG3 state (1), and the pushed CI run at that sha reads the same. The
   `pointers_all_at_carried` state either plants against a first-revision report and is
   shown to REDDEN by the nested run's own failure line, or is deleted under DR1 with its
   vacuity recorded. `docs/reports/F3/step-3-answers.json` points each item at the section
   that does its work rather than at the one that lists them all.
2. **R633.** Either a row for `PLATFORM_RIGID_MODE_EXACTNESS` in
   `tests/test_counters_are_injected.py`'s `REGISTERED` with both BX0 cells green and the
   completeness assertion moved to `>= 5`, or all four sentences corrected -- 
   `floatfea/tolerances.py:354-355`, `docs/milestones/F3.md` section 5 and section 7,
   `tests/test_counters_are_injected.py:317-319` -- site by site, each with its hunk.
3. **R634.** `floatfea/tolerances.py:330` and `:345-348` say what is true: the constant is
   asserted by `check_rigid_modes` at `floatfea/model/platform.py:319`, its subject is
   every deck a reader could write, no counter is registered against it and why. No value
   moves.
4. **The closure list absorbed in one commit**, with CZ1's four outputs pasted AFTER that
   commit exists: `ruff check`, `black --check`, `mypy`, `pytest -q` at the commit, then
   `gh run list` at its own sha with the job-level conclusions.

**What does NOT hold this step, stated so no round is spent asking:** R631 and R626's
residue are LEDGERED under DZ7c and I accept the ledger; R635 is recorded and not
blocking; C88's missed timing condition is a closure item because the choice it would have
affected turned out right and I verified it against the worst member; the EG4 preview stays
BLOCKED and that is correct -- fix its stated ground, do not work around it.

**Schedule.** F3 closes **13 October**; F4 19 October; the member-force table 23 October;
the code-check screen 28 October. **I have no measurement that contradicts any of them**,
and the ladder is green on CI at this commit, which is the measurement that would. The
report proposes pulling F4 to **16 October** under EG5(b): **I do not endorse that from
here.** Not because the reasoning is wrong -- the export-not-a-derivation argument is
sound and DX1 measured it -- but because the step report names the one unknown it rests on
(whether HSP-stable carries the buoy positions where a gate can cite them by file and
line) and that unknown is unmeasured, and because section 7's other factual claim about
`../HSP-runs` was refuted by one `ls`. **Measure the EB6 expected side first, then propose
the date.** Three days is not worth buying on an unread file.

**One sentence for the implementer.** The ceiling is the best-derived constant in this
repository -- both edges solved, the counter size bisected, the unit-scaling case survived,
and it buys `850x` of detection that nobody had measured. Everything I am holding on is a
sentence about a mechanism or a guard that cannot fail, and all three are in files you can
fix in one commit without touching a number.
