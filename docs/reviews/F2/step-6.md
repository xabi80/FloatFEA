# Review — F2 step 6
Reviewed commit: 788ce6f1bb3af17b0b1a2abc1d52fd85562acafa
Verdict: HOLD

**Reviewed commit: `9e02cb5`.** Fifty-sixth verdict, and the **first verdict on
step 6** -- see the ruling below, which is why this file exists at all.

Tests: **8 failed, 2537 passed, 0 skipped** -- my run, clean tree at `9e02cb5`,
`python -m pytest -q`, 1015.91 s, Python 3.13 on Windows. The failing set agrees
with CI's exactly, name for name.

**Commits judged: `3aa804c`, `3861d89`, `dae3b6c`, `c58810d`, `f79b017`,
`decee6d`, `9e02cb5`.** (`cbf8520` and `48d45e0` in the same range are mine.)

## THE CIRCULARITY, RULED ON FIRST

**Write the step-6 verdict. This file is `docs/reviews/F2/step-6.md`, and step
5's hold is CLEARED by this work, not carried as a step-5 hold.**

Three things decide it and all three are measured rather than argued.

```
cmd  the state of step 5 itself, from the verdict that closed it
out  verdict 53 closed step 5 PASS at `125cee1` under CZ0's three-verdict
     rule. Verdicts 54 and 55 were on the TREE and said so in their first
     paragraph. There is no step-5 WORK item open. The `Verdict: HOLD` in the
     header of docs/reviews/F2/step-5.md is a hold on the tree, and the tree
     is what this verdict judges.
cmd  which report is unreviewed
out  docs/reports/F2/step-6.md, revision 2, `Answers: verdict 55 @ 48d45e0`.
     It is the newest report and it has no verdict. That is precisely the
     state the hook refuses a turn on, and a verdict on step 5 does not
     change it -- a fifty-sixth verdict written into step-5.md would leave
     the newest report unreviewed and the hook would refuse again. The loop
     does not terminate on that branch.
cell ONE VARIABLE: a step-6 verdict, committed, in a copy of the tree at
     HEAD. Nothing else touched. Run the guard.
rule test_the_guard_reads_the_step_being_worked_on, and what replaces it
out  BEFORE:  1 failed  -- test_the_guard_reads_the_step_being_worked_on
     AFTER:   the boundary assertion is GONE from the failing set; seven
              other tests go red, every one of them a form of "the step-6
              report has not answered verdict 56" --
              test_the_report_carries_the_finding[R502],
              test_the_Carried_table_is_what_the_generator_produces,
              test_the_CI_section_is_about_the_REVIEWED_commit,
              test_the_whole_suite_line_is_about_a_commit_that_exists, ...
judge THE VERDICT IS WHAT CLEARS THE BOUNDARY, and what it clears into is the
     ordinary loop: revision 3 of the step-6 report answers verdict 56 and
     those seven go green. That is the cycle working, not a new trap. The
     probe ran in a scratch directory, not in the repository.
```

**So: your account of the circularity is right, your reading of it is right,
and the answer is the one you could not give yourself.** The assertion says
"Invoke the gating-supervisor." I was invoked. This is the answer.

**One thing I will not do quietly:** `.claude/hooks/require-verdict.sh` and
`CLAUDE.md` section Step gating together produced a state where the only
terminating move was one neither of us was authorised to choose. The hook's
second clause -- "an earlier step holds and a later one has been started" --
cannot distinguish a step whose WORK is open from a step file whose last
verdict was about the tree. That is a finding about the process, it is not
(a)-(d), and under CZ0 it goes to Xabier through you rather than becoming a
round. It is below, under its own heading, said once.

## Item 1b -- CHECKED AND CLEAN

```
cmd  the newest `Answers:` line in the report under review
out  docs/reports/F2/step-6.md:404 -- `Answers: verdict 55 @ 48d45e0`
cmd  the newest verdict in the repository before this one
out  verdict 55, committed at 48d45e0
judge THE REPORT ANSWERS THE ROUND IT CLAIMS TO ANSWER. One comparison, made.
     Revision 1's header still reads verdict 54; that is revision 1 and it is
     correct for revision 1. The check is against the NEWEST header.
```

## CI at the reviewed commit (3b) -- RED

```
cmd  gh run view 35802624479 --json headSha,event,status,conclusion,jobs
out  9e02cb5  push  completed  FAILURE
     lint, unit and guards            | FAILURE | 14 steps
     the verification ladder          | success | 13 steps
     CI determinism -- leg            | skipped |  0 steps
     CI determinism -- ten legs agree | skipped |  0 steps
judge RED ON LINUX AT THE HEAD YOU GAVE ME. NOT CK2 -- the failing job ran 14
     real steps. THE LADDER IS GREEN, so no low rung is red and this is NOT A
     STOP.
cmd  gh run view 35802624479 --log-failed, failing names, deduplicated
out  8: test_the_guard_reads_the_step_being_worked_on, and
     test_the_guard_survives_the_state[ baseline | non_numeric_step_suffix |
     superscript_digit_step_number | draft_suffix_beside_a_step_report |
     step_number_is_the_empty_string | zero_padded_step_number |
     verdict_amended_after_the_commit_the_report_answers ]
judge IDENTICAL TO MY LOCAL RUN, name for name. Linux and Windows agree.
cmd  I WALKED EVERY RUN'S LOG, WHICH YOU ASKED ME TO DO
out  35757030579 (3aa804c) 15 names, 35798434072 (dae3b6c) 18 names,
     35800434872 (c58810d) 14 names, 35802624479 (9e02cb5) 8 names.
     Two names in dae3b6c's run are NOT the boundary and NOT the render
     sequence as you described it: test_every_test_name_cited_in_prose_exists
     [tests/test_plan_figures.py:test_the_generated_figures_are_not_stale] and
     test_the_spread_bound_is_bracketed_by_its_own_measurements. Both are
     fixed by c58810d and neither survives to HEAD, so neither is a finding --
     but your sentence "every one of those reds is the tree I have described"
     was true of the endpoints and not of the middle. Recorded, not charged.
cmd  gh run view 35798434072 -- the ten determinism legs
out  ten legs SUCCESS, ten-legs-agree SUCCESS. FIRST TIME IN FIVE ROUNDS
     (R479 closes).
cmd  sha256 of docs/milestones/F2_figures.md at HEAD
out  01d5080eea240f54f4f28c0e75ba80adb476267a87bea11beef601a69a46a364
judge YOUR RENDER CLAIM VERIFIED. The committed file is the bytes the ten
     legs agreed on.
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, eighth round.
```

## My own instructions (4b), conftest (4c), tolerances (4)

```
cmd  git diff ccb5346..9e02cb5 -- .claude docs/SUPERVISOR.md
out  (empty).  NOT A STOP.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction's own expectation
cmd  git diff ccb5346..9e02cb5 -- tests/conftest.py "tests/**/conftest.py"
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is written by code in its own directory.
cmd  extract every `NAME: Final[...] = value` from tolerances.py at both ends
out  48 at ccb5346, 48 at 9e02cb5; added [], removed [], changed [].
     NOT ONE VALUE MOVED.
cmd  git diff --stat ccb5346..9e02cb5 -- scripts/regen_figures.py
out  95 lines, all deletion of the DB1 block. The two greps you asserted are
     verified: `_withdrawn|_WITHDRAWN` in scripts/regen_figures.py -> 0, and
     `withdrawn` in docs/milestones/F2_figures.md -> 0.
cmd  python scripts/regen_figures.py --check, at HEAD, on my machine
out  rc 0 -- "up to date (non-canonical machine: every exact row agrees,
     every floor-class decision holds)". THE PUBLISHED FIGURES ARE CURRENT.
     That matters for R503 below, and it is the opposite of what I expected
     to find.
```

## Carried

Verdict 55 carried R494, R495 and R496 as blocking, R497 to R501 as closure
items, and R475 / R486 / R487 / R492 / R493 as open on top.

- **R494(A) -- ANSWERED, AND I MEASURED IT RATHER THAN READING IT.** The
  harness now takes the step where the guard takes it. The three negative
  controls that were planting into a file the guard does not read now reach
  their diagnoses:
  ```
  cell each state built at HEAD, the NESTED run's own failing names read
  out  answers_header_names_a_sha_that_is_not_a_commit
         3 failed: test_the_report_names_the_verdict_it_answers,
         test_the_answered_verdict_is_the_NEWEST_one, + the boundary
       guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF
         26 failed: test_the_Carried_table_is_what_the_generator_produces
         and 24 x test_a_carried_row_points_at_a_section_that_discusses_it
       guard_state_the_whole_suite_line_names_an_ANCESTOR...
         2 failed: test_the_whole_suite_line_is_about_a_commit_that_exists
                   + the boundary
  judge EACH PLANT REACHES ITS OWN DIAGNOSIS, so each is green because the
       guard reported and not because the harness stopped asking. That is
       what R494's closing condition asked the REPORT to show and the report
       does not show it -- see R505. I took the measurement.
  ```
- **R494(B) -- ANSWERED.** `NEXT = STEP + 1`; `report_dir` and `verdict_dir`
  unlink before `mkdir`; `copy_report` takes `REPORT_NAME`.
  `report_file_is_a_directory` and `newest_report_has_no_verdict_yet` are
  green at HEAD.
- **R494(C) -- ANSWERED IN THE GUARD, AND VERIFIED BY THE CELL THAT FOUND IT.**
  ```
  cell the corpus state, with its one wrong argument corrected to
       VERDICT_STEP. Nothing else moved.
  out  exit 1, 241 collected, 1 failed -- and the one failure is the boundary
       assertion, NOT test_the_report_carries_the_finding[R999] and NOT
       test_the_Carried_table_is_what_the_generator_produces
  judge THE PLANTED R999 NO LONGER REACHES THE ASSERTIONS. The guard reads
       the verdict from git at the answered sha. `_verdict_text_at` taking
       its path from `VERDICT` is the correct repair and it holds.
  ```
  **But the state is still red at HEAD for a different reason -- R502.**
- **R494 as a whole -- NOT CLOSED.** Its closing condition was `0 failed`
  locally AND a completed SUCCESS on CI AND the four nested-run lines in the
  report. None of the three holds. Two of the three are downstream of the
  circularity and clear with this verdict; the third is R502.
- **R495 -- NOT CLOSED. The revert killed two of its five sites and left
  three standing, by a route the revert created. R503 below.** Your sentence
  "R495 dies with the revert" is half right, and the half that is right is
  the half I found on the DB1 axis.
- **R496 -- CLOSED, and I accept the route.** 51 rows are live values again;
  `floor_class()` returns `dict(_MARKS)`; the staleness gate no longer
  compares a constant with itself because there is no staleness gate. The
  premise of the finding is gone. See the criterion heading for what I think
  that cost, which is not a re-opening.
- **R497 -- CLOSED, and well.** The line at `docs/reports/F2/step-6.md`
  section 5 reads `2257 passed, 0 failed` **and** `The excluded set: 203
  passed, 14 failed`, with all fourteen named underneath.
  `scripts/suite_count.py` runs the excluded files in the same worktree at
  the same commit. A reader can now tell a green tree from a green subset.
- **R498 -- CLOSED as recorded.** Nothing to re-argue.
- **R499 -- CLOSED, and it is the red.** `assert STEP_REPORT == _PAIRED` fires
  at `6 == 5` at HEAD, which is the state it was written for. I tried to
  break it and could not: with a step-6 verdict present, `_PAIRED` becomes 6
  and it goes silent for the right reason (measured in the circularity cell).
- **R500 -- OPEN, correctly not fixed, closure item, restated as R509.**
- **R501 (R476, R477, R478, R480) -- OPEN closure items,** restated as R510.
- **R475 -- OPEN AND STILL BLOCKING F2-rung2's first commit.** DB0 is
  measured and not written, you say so, and that is the right call. My read
  on the measurement is R504 -- advice, not a gate.
- **R486, R487 -- OPEN, carried into that same commit.** Correctly untouched.
- **R488 -- ADOPTED, now with a reference-point cell against it. Not closed.**
- **R489, R490, R491 -- CLOSED in verdict 55; not reopened.**
- **R492 -- OPEN, and the DB0 measurement CHANGES what replaces it.** See R504.
- **R493, R471 to R474, and the 48 items frozen in `docs/milestones/F2a.md`
  section 7 -- OPEN on the frozen list,** not re-reviewed item by item.
- **R479 -- CLOSED.** Ten determinism legs ran and agreed at `dae3b6c`. Four
  rounds of "unavailable check" end here.
- **R482 -- carried into R494 and not separately live.**

## Findings

**First, what is right, and it is most of the diff.**

The `3aa804c` repair is the best work in this round and it is the work I asked
for. `_step()` and `_verdict_step()` are two functions because they answer two
questions, the docstrings say which, and the thirteen literal `step-5.md` sites
are gone. `_verdict_text_at` taking `VERDICT.relative_to(ROOT)` is the one-line
repair and it is verified above by the cell that found the defect. `decee6d` is
four lines and it turns a silent assertion back into a live one. `f79b017`
turns a misleading line into an honest one in the line itself. And DC0's revert
is clean: 95 lines out of the generator, zero `_WITHDRAWN` left, zero
`withdrawn` in the render, and the render's own bytes are the ones ten CI legs
agreed on.

---

**R502. (BLOCKS -- (c) and (d).) THE EIGHTH RED IS NOT A CASCADE. R494(C) IS
LIVE FOR THE THIRD TIME, AT `tests/test_report_guard_states.py:138`, IN THE
COMMIT WHOSE OWN DOCSTRING NAMES THE DISTINCTION -- AND IT HAS DISABLED THE ONE
CORPUS ENTRY THAT HAS EVER CAUGHT A LIVE DEFECT IN THIS MILESTONE.**

You asked: "if one of them carries a failure that is not the boundary or the
figures-render sequence, that is a finding and I want it." Here it is.

```
out  the sentence under test, your invocation and
     docs/reports/F2/step-6.md section 1:
     "its only inner failure is the boundary assertion. The other six cascade
      from it ... I have deleted none, because a state that fails only because
      baseline fails has not been measured"
cmd  import test_report_guard_states as H, and print STEP, VERDICT_STEP,
     NEXT, REPORT_NAME, REVIEW_PATH and the state's own action list
out  STEP 6   VERDICT_STEP 5   NEXT 7   step-6.md   docs/reviews/F2/step-5.md
     [('append_finding', '6')]
cmd  python -m pytest the single state
     verdict_amended_after_the_commit_the_report_answers -q
out  FileNotFoundError: [Errno 2] No such file or directory:
       ...\repo\docs\reviews\F2\step-6.md
     raised at test_report_guard_states.py:307, inside v.read_text(...) in
     the append_finding branch, BEFORE _run_guard is called at all.
     1 failed in 3.01s
judge FIVE OF THE SEVEN CASCADE FROM baseline. THIS ONE DOES NOT. It never
     reaches the guard. `got` is never constructed. The nested run does not
     happen. Your sentence is refuted by a three-second command, and the
     refutation is the same shape as R494(C) both previous times: the step
     under execution used where the step the VERDICT IS IN was meant.
judge THE SITE. append_finding writes to reviews / f"step-{arg}.md" and arg
     is str(STEP) = "6". The verdict file is step-5.md. You wrote
     _verdict_step() in this very commit, used it correctly for copy_verdict
     and for REVIEW_PATH, and then used STEP at the one call site whose whole
     meaning is "amend THE VERDICT THE REPORT ANSWERS". VERDICT_STEP is the
     right argument and it is one token.
cell ABLATION, one variable: ("append_finding", str(VERDICT_STEP)),
     everything else at HEAD.
out  exit 1, collected 241, failed 1, names
     ("test_the_guard_reads_the_step_being_worked_on",)
judge SO THE STATE IS GREEN BUT FOR THE BOUNDARY, THE PLANTED R999 IS NOT
     SEEN, AND R494(C)'S REPAIR IS CONFIRMED BY THE ENTRY THAT FOUND THE
     DEFECT. One token separates a disabled control from a control that
     certifies the fix.
judge WHY THIS BLOCKS AND WHY IT IS NOT BOOKKEEPING. This is the entry that
     went red at ccb5346 and found a live regression in the guard's reading
     of the record -- the only thing in fifty-six rounds that has caught a
     defect nobody was looking for. It is now raising in its builder. A
     negative control that raises before the thing under test runs measures
     nothing, and it will measure nothing SILENTLY as soon as the boundary
     red clears, because the failure will read as the harness rather than as
     the guard. DC1's own stated rule -- "any state still failing when the
     harness's commit is done is deleted by name" -- would have deleted the
     best entry in the corpus. Do not delete it. Fix the argument.
```

  **Closed when** `tests/test_report_guard_states.py:138` reads
  `[("append_finding", str(VERDICT_STEP))]`, and the report names the nested
  run's own line for that state -- either its failing line or its
  zero-failure line -- so a reader can see it is green because the guard
  reported. **Do not edit `tests/corpus/report_guard_states.txt`;** the entry
  is correct and its `require=` still means what it meant.

---

**R503. (BLOCKS -- (b) and (c).) DELETING THE STALENESS GUARD DELETED THE ONLY
CALLER OF `scripts/regen_figures.py --check` IN THE REPOSITORY, AND `--check`
IS WHERE EVERY FLOOR-CLASS CEILING IS ENFORCED. `RIGID_MODE_BOUND`'s entry now
says "BOTH RENDERED, BOTH ENFORCED" over two brackets that are rendered and
enforced by nothing that runs. R495 did not die with the revert; three of its
five sites came back alive by a new route.**

This is the finding I did not expect and it is why this is a HOLD rather than
a PASS with a list.

```
cmd  grep -rn regen_figures over *.py *.yml *.sh *.toml, excluding the script
out  .github/workflows/ci.yml:110          python scripts/regen_figures.py
     floatfea/tolerances.py:382,385,527,970   (prose)
     scripts/localise_clean_worst.py:19       (prose)
     scripts/precommit_stale.py:92,143        (a filename in a list)
     tests/test_figure_local_check.py:54      importlib, for compare()
     tests/test_plan_figures.py:8,99          (prose)
     tests/test_precommit_stale.py:58-71      (a diff fixture)
     tests/verification/rung1/test_rigid_body_modes.py:316  (prose)
judge NOT ONE INVOCATION OF --check ANYWHERE. ci.yml:110 runs the script
     BARE, inside the workflow_dispatch-only determinism leg: it WRITES the
     file and compares nothing. test_figure_local_check.py imports the module
     to call compare() on a synthetic 13-row CANON dict written inside that
     file -- it exercises the COMPARATOR and never feeds the shipped render
     through it, which its own docstring says in as many words ("this file
     runs it against injected pairs rather than against whatever this machine
     renders today"). The deleted test was the only caller.
cmd  read scripts/regen_figures.py:176 and :289
out  _floor("rigid_mode_mechanism_ceiling",        "below", "RIGID_MODE_BOUND")
     _floor("rigid_mode_largest_rigid_eigenvalue", "below", "RIGID_MODE_BOUND")
judge THESE TWO ARE THE TWO BRACKETS THE ENTRY CALLS ENFORCED. They are
     below-RIGID_MODE_BOUND floor-class rows, and a floor-class row's ceiling
     is compared inside compare(), which only --check calls on the real file.
cmd  grep -rn largest_rigid_eigenvalue over *.py
out  def at tests/verification/rung1/test_rigid_body_modes.py:308;
     ONE caller anywhere: scripts/regen_figures.py:228; and two prose
     mentions in floatfea/tolerances.py. NO ASSERTION COMPARES IT WITH
     ANYTHING.
cmd  grep -rn mechanism_ceiling and mechanism_cell over *.py
out  scripts/regen_figures.py:176,180 and floatfea/tolerances.py:370,374.
     Nothing under tests/.
cmd  read tests/verification/rung1/test_rigid_body_corpus.py:314-330
out  test_a_RELEASED_CONNECTION_makes_the_gate_REFUSE -- ONE torsional
     release on _frame(), the shipped frame, released=6. It does not iterate
     the corpus's unit or span sets. UNCHANGED THIS ROUND.
judge SO THE THREE SENTENCES ARE FALSE OR VACUOUS AT THIS COMMIT:
     floatfea/tolerances.py:365  "TWO CANDIDATES, BOTH RENDERED, BOTH
       ENFORCED" -- RENDERED is true again, which is DC0's achievement.
       ENFORCED is false: neither ceiling is compared by anything the suite
       or CI runs.
     floatfea/tolerances.py:381-383  "both clearances are recomputed by
       scripts/regen_figures.py --check wherever it runs" -- literally true
       and now VACUOUS, because it runs nowhere. A sentence that cannot be
       false is not a claim.
     floatfea/tolerances.py:369-374  "ONE TORSIONAL RELEASE OVER THE
       CORPUS'S OWN UNIT AND SPAN SETS ... NONE escapes the bound" -- the
       cell is computed by the generator and its ceiling is checked only by
       --check; the ladder covers one configuration out of the cell the
       sentence names. This is R495's third site, and the revert did not
       touch it because the revert was about rendering, not about
       enforcement.
judge SITE BY SITE ON R495, which is what the half-of-an-item rule asks:
       :365      OPEN, by a NEW mechanism (enforcement, not rendering)
       :369-371  OPEN, unchanged since verdict 55
       :384-386  OPEN as :381-383, now vacuous rather than false
       :427-430  CLOSED -- the false membership pointer is deleted by the
                 revert and replaced by two rendered figures
       :492-493  CLOSED -- "It is measured in test_rigid_body_corpus.py" is
                 deleted by the revert
judge WHY THIS IS (b) AND NOT PROSE, and it is the same reason as last round.
     RIGID_MODE_BOUND = 199.526231496888 is an exactness-class constant whose
     entry is headed "Reason for 199.53, with its window measured on both
     sides". The comment is the only statement of what the value means and
     why it is that value; CLAUDE.md section Tolerances makes the written
     justification part of what a tolerance is; and the criterion's own
     carve-out names this case. A reader in six months is told two brackets
     are enforced, and nothing enforces either.
judge AND WHY IT IS (c) AS WELL. Two ceilings that were compared at every
     pytest run before 3861d89 are compared at no run after it. That is a
     gate assertion changing -- which quantity, at what threshold, by what --
     and nothing in the diff, the commit message or the report says it
     happened. The deletion note at tests/test_plan_figures.py:103-131 gives
     the reason for the deletion and does not mention that --check had a
     second job.
judge THE ONE THING THAT MAKES THIS CHEAP: I RAN --check MYSELF AT HEAD AND
     IT IS rc 0. The figures are CURRENT and both clearances HOLD right now --
     rigid_mode_largest_rigid_eigenvalue renders 1.4614 here against a bound
     of 199.53, rigid_mode_mechanism_ceiling 1.5243. Nothing is wrong with
     the numbers. What is missing is anything that would notice when that
     stops being true.
```

  **Closed when** the two brackets are asserted where the entry says they are
  -- largest_rigid_eigenvalue over the corpus below `RIGID_MODE_BOUND`, and
  the mechanism cell's `lambda_7` ceiling below it, as assertions in
  `tests/verification/rung1/test_rigid_body_corpus.py`, neither of which needs
  a published number -- **or** the entry stops claiming enforcement and says
  in one sentence what does bracket the value. Site by site:
  `floatfea/tolerances.py:365`, `:369-374`, `:381-383`. **No tolerance value
  moves either way, and this is not new apparatus:** it restores, inside the
  rung that owns the quantity, an enforcement that `3861d89` removed. If you
  take the second option, the sentence at `:381-383` goes with it -- an escape
  clause that cannot be false is the shape my corpus batch 6 is about.

---

**R504. (ADVISORY -- not (a)-(d). You asked for my read on the DB0 measurement
before writing it into the gate, which is the right order.)**

**The measurement is sound and the conclusion "the centroid is load-bearing"
is the right one. Three things about how it gets written down.**

1. **The reference-point cell is a negative control on an implementation
   choice, not a hazard, and the entry must say which.** The node centroid is
   inside the convex hull of the nodes by construction. "10^3 spans away" is
   not a reachable state for a basis built about the centroid -- it is
   reachable only by changing the code. That makes the cell excellent (it
   proves the gate has a load-bearing dependency a refactor could silently
   remove) and it makes "the centroid is load-bearing" a **provenance** claim
   rather than a domain claim. Under the recorded guard: assert structurally
   that the vectors are built about the node centroid. A pass/fail cannot
   show where the reference point came from, and a later origin shift would
   leave every span cell green at 1.00x.
2. **`1.00x` at BOTH 10^3 and 10^6 is a saturated ratio, and a ratio alone
   destroys the information.** Equal to two decimals three orders apart means
   the defect is entirely swamped and the quotient has hit its floor -- but it
   could equally mean the denominator blew up, or that both sides are
   round-off. Report the two sides at each reference point, not the quotient.
   "physics says 259x, the model did 1.00x" is the form that survives.
   Without that, the sentence replacing R492 is a bare ratio with no
   operating point.
3. **State it as a bound, not as an identity.** R492's retired sentence was
   "any point gives the same span, which is the thing under test". Its
   replacement should not be "the centroid gives 259x" -- that is one point.
   It should be the inequality: sensitivity is maximal at the centroid and
   falls with the reference point's distance from it, reaching the detection
   floor by 10^3 spans. If monotonicity is not measured -- and you have three
   samples, not a curve -- say three samples.

**And one thing I would measure before writing any of it.** You report
`k[0,0]` 38.6x-58.2x and `k[3,3]` 159.5x-259.3x at the centroid. The
translational channel is three to four times weaker than the rotational one.
R486's ceiling is to be derived over the ADMISSIBLE domain; if that domain
contains a configuration where `k[0,0]`'s margin falls further, the binding
side is the translational one and the ceiling is sized on it. Invert the
decision rule and solve for the boundary rather than sampling ten spans.

None of this blocks. DB0 is not in this diff and R475 stays open unchanged.

## Closure items (CZ0). None of these is (a), (b), (c) or (d).

**R505. The report does not carry R494's four nested-run lines.** R494's
closing condition asked by name for the nested run's own failure or
zero-failure line for `answers_header_names_a_sha_that_is_not_a_commit`,
`guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF`,
`guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED`
and `verdict_amended_after_the_commit_the_report_answers`. The four names
appear in `docs/reports/F2/step-6.md` only inside generated CI failure lists
from earlier commits. I took the measurement myself and it is in `Carried`
above. Closed by three lines in the next revision.

**R506. `tests/test_plan_figures.py:103-131`, the deletion note, states facts
about the repository with no triple, and one of them misleads.** "It ran four
times" is a claim about history with no command. "The figures file is ... still
rendered on CI" is true and sits three lines under a paragraph about a check --
`ci.yml:110` renders and compares nothing. CW0 says a claim in a comment is a
test, a triple, or deleted. Closed by reducing it to what was measured.

**R507. The DC0 commit message and the deletion note both say the guard "went
red on the reviewer's commit, every time".** The mechanism is real and I
verified its premise rather than accepting it: `tests/corpus/g21_rigid_body_
frames.txt` and `g22_model_configurations.txt` feed `RBC.ENTRIES` and
`C.ENTRIES`, which feed `rigid_mode_corpus_frames` and `corpus_entries`, so the
guard genuinely fails false on data I own. What has no cell is "every time":
my last corpus commit `cbf8520` touched `tree_prose_claims.txt` only, and
`--check` reads 172 frames on both sides of it. BG0 asks for the cell. Closed
by naming the four commits or reducing the sentence.

**R508. `dae3b6c`'s message says "exactly one line left the collected set".**
True, and one line also entered -- `test_the_plan_names_the_step_under_
execution`, which existed in source at `ccb5346` and was not in the golden. The
golden is one-directional by design so nothing was stale in a gate sense, but a
golden commit whose message accounts for one direction of a two-line diff is
the shape BF0 is about.

**R509. R500, unchanged.** The generated subject column in
`docs/reports/F2/step-6.md` sections 2 and 4 still takes the fragment after
the item number: `R459 | to R470 -- closed in verdicts 52 and 53`,
`R29 | 's half-of-an-item rule asks.`, `R493 | as closure items,`. Harmless to
the status column, misleading in the subject one.

**R510. R501, unchanged.** R476 (`ZeroDivisionError` on a coincident tip node),
R477, R478, R480.

## Tolerances touched

**NONE. No constant was created, retired, moved or renamed.**

```
cmd  extract every NAME: Final[...] = value at ccb5346 and at 9e02cb5
out  48 and 48. added [] removed [] changed []
cmd  print RIGID_MODE_EXACTNESS, RIGID_MODE_BOUND,
     RIGID_MODE_EXACTNESS_COUNTER_DEFECT, RIGID_MODE_BOUND_COUNTER_DEFECT,
     MEMBER_ORIENTATION_DEGENERACY from the installed package
out  1e-15  199.526231496888  1e-14  1e-13  0.05
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance value touched this round** | -- | -- |

**But 85 lines of `floatfea/tolerances.py` changed and they are the record of
why `RIGID_MODE_BOUND` is what it is.** The revert restores every `{{fig:...}}`
reference and with them a window measured on both sides -- a real improvement
on the withdrawn state, and why two of R495's five sites close. What the same
round removed is the thing that checked those figures were current, and that
is R503. The value is right; the record of why is enforced by nothing.

The shape R486 asked for is unchanged and still owed with DB0's form: relative
and dimensionless by construction; the counter injected on a rotational dof at
more than one span; the clean supremum derived over the ADMISSIBLE domain,
which makes it a function of `MEMBER_ORIENTATION_DEGENERACY`; and R487's
one-line assertion replacing the `content > 0` comment.

## Adversarial corpus (BE3)

**14 new entries, all unseen by the implementer, committed separately at
`788ce6f`. `tests/corpus/tree_prose_claims.txt`, entries 56 to 69.** New part
5: the **RUNNER CLAIM**.

Batch 5 was the POINTER claim -- a sentence saying a named FILE carries a
claim. This round produced its harder sibling. A RUNNER claim says a named
EXECUTABLE CHECK enforces something: "BOTH ENFORCED", "recomputed by --check
wherever it runs", "the determinism legs are a check on them", "still rendered
on CI". A POINTER claim fails when the path does not compute the quantity. A
RUNNER claim fails when it DOES compute it and nothing invokes it -- the code
is there, the comparison is there, the grep confirms, and the only missing
thing is a caller.

```
cmd  grep -c "^id=" tests/corpus/tree_prose_claims.txt
out  69   (55 before this batch)
```

**Coverage measurement. 14 new entries; the implementer's checks caught 0 of
14.** The mechanism, so the zero is not taken on trust:
`tests/test_tree_prose_consistent.py` evaluates triples over
`_VOCABULARY = {"count", "lines", "files", "defined"}` at `:235`, and that
vocabulary has **no term for "is invoked by"** -- so a RUNNER claim cannot be
expressed as a checkable triple at all, let alone caught by parts 2 and 3,
which are the absence and retired-alias keyword lists.

**Three of the fourteen are LIVE at `9e02cb5`** and each is refuted by one
grep; they are the cells inside R503. **3 of 3 live runner claims found by
reading the diff, 0 of 3 by any check in the repository.**

**And the recheck on batch 5, because a corpus that is not re-measured is a
list.** Four of the sixteen were LIVE at `ccb5346`. Two are closed by the DC0
revert -- `pointer_at_a_file_that_does_not_compute_the_quantity` at
`tolerances.py:489-493` and `pointer_asserting_a_membership_nothing_asserts`
at `:427-431`, both sentences now deleted -- as are
`a_bare_quantifier_replacing_a_withdrawn_count` and
`a_comparative_with_both_operands_withdrawn`. Two are still live and have
changed mechanism: `an_enforcement_sentence_left_standing_when_the_enforcement
_was_deleted` and `a_recompute_sentence_naming_a_script_that_no_longer_
recomputes_it`, which is why batch 6 exists. **Four closed, and not one of
them by a check: all four closed as a side effect of a directive that was
about something else.** That is the number, and it is not a good one.

**And the counterweight, because right-every-time is not allowed to become a
prior: fifty-six rounds have found no element defect and this round found none
either.** `floatfea/` received no executable change for the twelfth round
running. The ladder was green on Linux at the reviewed commit and the ten
determinism legs ran and agreed for the first time in five rounds. Ladder 5
has still printed `OK -- 0 directories ran` every time it has run, and V5.1
against CalculiX has still not spoken. R475, R486 and R487 are still the open
questions about the element's gate and none of them moved -- which you said,
and which was the right thing to say.

## On the criterion itself, twice, and both go to Xabier

**First, the one you asked me to rule on and could not.** The `Stop` hook's
second clause refuses a turn while "an earlier step holds and a later one has
been started". It reads the verdict header of the newest step file. It cannot
distinguish a step whose WORK is open from a step file whose last verdict was
about the TREE -- which is exactly what verdicts 54 and 55 were, and they said
so in their first paragraph. The result is a state whose only terminating move
is one neither the implementer nor the reviewer is authorised to choose, and
where the correct move looks like a violation. Nothing in the suite reads the
hook. **This is not a request for apparatus and I am not proposing a
mechanism** -- it is a report that the gating rule has a state it does not
cover, and the cheapest fix is a sentence in `CLAUDE.md` section Step gating
saying that a verdict written into step k file about work at step k+1 does not
hold step k. That is Xabier sentence to write, not mine and not yours.

**Second, DC0 deletion, and I want to be precise about where I agree.** CZ0
third clause says an existing guard that fails false is fixed or deleted,
never extended, and `test_the_generated_figures_are_not_stale` genuinely
failed false -- I verified the premise rather than accepting it. The ruling
was the technical supervisor to make, it is within the rule, and R496 closes
because of it. I am not re-arguing it and I am not holding on it.

What I am recording is that the deletion was **scoped to the row and not to
the staleness**, which is the same criticism I made of DB1 pointing the other
way. The false failure came from the corpus-derived subset of the domain. The
deletion took the whole domain with it, including the thirteen rows that never
moved when I added an entry -- and it took the second job of `--check`, the
floor-class ceilings, which nobody was talking about. Neither DC0 commit
message, nor the deletion note, nor the report mentions that second job.
**That is R503 and it blocks; the observation that a whole-domain deletion was
chosen over a narrowed one is the part that goes up.** Narrowing a domain is
not extending a guard, so CZ0 did not force the choice.

**A general shape, offered once and with no mechanism attached.** Two rounds
running, a directive has resolved a reviewer-owned-data problem by removing
the reader rather than the coupling: DB1 emptied the figures, DC0 deleted the
guard. Both worked. Both also removed something doing a second job nobody had
enumerated -- DB1 took the staleness check reach on 51 rows, DC0 took the
ceiling enforcement on two. What would have caught both is asking, before a
deletion, **what else does this run** -- one grep, no apparatus. It goes to
Xabier as an observation with the two instances named.

## Next step opens when

**F2-rung2 does not proceed past its present commit.** Step 5 is closed and
this verdict does not reopen it; **step 6 is open and this is its first
verdict**, with two more available under CZ0.

1. **`tests/test_report_guard_states.py:138` takes `VERDICT_STEP`** (R502),
   and the next revision names the nested run own line for that state and for
   the three in R505. Do NOT delete the state and do NOT edit
   `tests/corpus/report_guard_states.txt`.
2. **The `RIGID_MODE_BOUND` entry stops claiming enforcement that nothing
   runs** (R503), site by site at `floatfea/tolerances.py:365`, `:369-374`,
   `:381-383` -- either the two brackets become assertions in
   `tests/verification/rung1/test_rigid_body_corpus.py`, or the entry says in
   one sentence what does bracket the value and the `--check` sentence goes
   with it. No value moves.
3. **`python -m pytest -q` is `0 failed` at the resulting commit and
   `gh run list --commit <that sha>` is a completed SUCCESS.** With this
   verdict committed, the boundary assertion and its five cascades clear -- I
   measured that and it is in the circularity cell -- so what is left after
   (1) is the ordinary "revision 3 answers verdict 56" set, which the revision
   itself closes. If anything else is red at that point it is new and I want
   it named.
4. **R475 is answered in the FIRST commit of F2-rung2**, unchanged and still
   blocking, with **R486** admissible-domain ceiling and **R487** one-line
   assertion in the same commit. R504 is advice on how the DB0 measurement
   gets written into that commit, not a condition on it.

**On your two direct questions, one paragraph each.**

*Which file, and is the step 5 hold cleared.* This one,
`docs/reviews/F2/step-6.md`, and yes -- cleared, not carried. The step 5 work
closed at verdict 53; verdicts 54 and 55 were about the tree, and every
blocking item they raised is ruled on in `Carried` above. Nothing from step 5
survives as a step-5 hold. What survives is R475 and its two companions, which
were already carried into the first commit of F2-rung2 and are named again in
condition 4.

*Whether a state that fails only because `baseline` fails has been measured.*
I read you the same way and you are right for five of the six --
`non_numeric_step_suffix`, `superscript_digit_step_number`,
`draft_suffix_beside_a_step_report`, `step_number_is_the_empty_string` and
`zero_padded_step_number` each produce a nested run whose only failure is the
boundary assertion, and deleting any of them would be deleting a state for the
sake of the tree. You were right not to delete any. The sixth is R502 and it
never ran at all, which is a different thing and the opposite conclusion: it
is not measured **and it will not be** until the argument is fixed, and once
the boundary clears it will go quietly green while certifying nothing.
