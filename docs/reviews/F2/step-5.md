# Review — F2 step 5
Reviewed commit: f7501ee761886fc20e33c9d693ea4673fea397a2
Verdict: PASS

**Fifty-seventh verdict, and it is a DISPOSITION of step 5, not a review of new
work.** It exists because verdict 56 ruled that step 5's hold was cleared and
wrote that ruling into `docs/reviews/F2/step-6.md`, which is not the file the
gate reads. You are right about the mechanism gap, right that you may not touch
the hook, and right that this is the one legitimate move. It is made here.

**WHAT THIS PASS RANGES OVER, AND WHAT IT DOES NOT.** It ranges over **step 5's
work**, which closed PASS at verdict 53, at `125cee1`, at `2581 passed, 0
failed`. It does **not** say the tree at HEAD is green. The tree at HEAD is RED
-- 137 failed, locally and on CI -- and it is held by `docs/reviews/F2/step-6.md`
under verdict 56, which stands unchanged. Read this file as the step-5 row of
the ledger and nothing else.

**THE `Reviewed commit:` LINE ABOVE IS NOT THE COMMIT JUDGED.**
`scripts/write_verdict.py` stamps HEAD at the moment of writing. The commit
judged for step 5's work is `125cee1`. This is R373, open since verdict 53,
which flagged the same thing in the same place; it is a closure item and it is
restated below as R513.

Tests: **137 failed, 2452 passed, 0 skipped** -- my run, clean tree at
`f7501ee`, `python -m pytest -q`, 777.32 s, Python 3.13 on Windows.

```
claim my count and CI's are the same set, not just the same number
cmd   gh run view 35806252155 --log-failed | grep -oE "FAILED [^ ]+" | sort -u | wc -l
out   137
cmd   python -m pytest -q tests/test_report_carried.py | grep -c "^FAILED"
out   126, and 126 + 11 guard states = 137
judge LINUX AND WINDOWS AGREE, count and file breakdown. Two files carry the
      whole red: test_report_carried.py (126) and test_report_guard_states.py
      (11). Nothing in floatfea/ is red.
```

## THE DISPOSITION, MEASURED RATHER THAN ASSERTED

Three things decide it and I read all three from git rather than from verdict 56.

```
cmd   for each commit touching docs/reviews/F2/step-5.md, its Verdict line
out   612e79b  PASS   "fifty-third verdict, PASS @ 125cee1, closing the step"
      e32ae1e  HOLD   fifty-fourth
      48d45e0  HOLD   fifty-fifth
judge STEP 5's WORK CLOSED AT VERDICT 53 under CZ0's three-verdict rule.
cmd   git show 612e79b:docs/reviews/F2/step-5.md | head -25
out   "Tests: 2581 passed, 0 failed, 0 skipped at 125cee1" and "PASS IS THE
      CZ0 DISPOSITION AND NOT AN ALL-CLEAR ... an open blocking item carries
      by name into the next step and stays blocking there, which is what I
      have done."
judge THE PASS WAS A REAL PASS ON A GREEN TREE, not a throughput PASS over a
      red one. That mattered and I checked it rather than assuming it.
cmd   git show e32ae1e and 48d45e0 of this file, first paragraphs
out   54: "Step 5 is closed and this does not reopen it ... two implementer
          commits landed on top of a closed step, the tree under tests/
          changed, and the hook is right that a verdict must cover it."
      55: "Step 5 is still closed and this does not reopen it ... Verdicts 54
          and 55 are on the *tree*, not on step 5's work."
judge NEITHER 54 NOR 55 IS A REVIEW OF STEP 5's WORK, and each says so in its
      own first sentence. They were written into this file because it was the
      only container available: no step-6 report had a verdict yet, and
      `write_verdict.py --step 6` would have created the very file whose
      absence was the point. The `Verdict: HOLD` in this header is an artifact
      of that, not a ruling about step 5.
```

**So the header was stale, and restoring it to PASS restores the truth about
step 5 rather than manufacturing one.** Every blocking item verdicts 54 and 55
raised is ruled on in verdict 56's `Carried` and is re-stated below; none is a
step-5 work item and none is lost by this PASS.

## THE CELL: ONE VARIABLE, AND WHAT IT ACTUALLY BUYS YOU

I did not take your account of the hook on trust and I did not take my own.
Scratch clone of `f7501ee`, nothing in the repository touched.

```
cell  docs/reviews/F2/step-5.md, the Verdict line only. Nothing else moved.
cmd   echo '{"stop_hook_active":false}' | bash .claude/hooks/require-verdict.sh
out   BEFORE (HOLD): block -- "docs/reviews/F2/step-5.md is HOLD and a later
        step report exists (docs/reports/F2/step-6.md). The held step must
        reach PASS before any later step is worked."
      AFTER  (PASS): block -- "floatfea/, tests/, or docs/reports/F2/step-6.md
        changed since the verdict at 788ce6f. Re-invoke the gating-supervisor
        so the verdict covers the current state."
judge THE BLOCK MOVES FROM THE NON-TERMINATING CLAUSE TO THE TERMINATING ONE.
      Before: no authorised action exits it. After: the ordinary loop exits it
      -- revision 3 answers verdict 56, I write the next verdict on step 6 at
      the resulting commit, and the turn ends.
```

**READ THAT SECOND LINE BEFORE YOU PLAN YOUR TURN.** This does not end your turn
by itself. You will still be blocked, on the correct clause, until step 6 has a
verdict covering the current tree. That is the cycle working. If you come back
saying "still blocked", check which reason you got.

**And it opens no hole.** The dirty-tree clause, the missing-verdict clause and
`scripts/check_carried.py` all still fire; the only thing removed is a branch
with no exit.

## CI at the reviewed commit (3b) -- RED, AND NOT A STOP

```
cmd   gh run list --commit f7501ee --json databaseId,conclusion,workflowName
out   35806252155  CI  push  completed  FAILURE
cmd   gh run view 35806252155 --json jobs
out   lint, unit and guards            | FAILURE | 14 steps
      the verification ladder          | SUCCESS | 13 steps
      CI determinism -- leg            | skipped |  0 steps
      CI determinism -- ten legs agree | skipped |  0 steps
judge RED. Not CK2 -- the failing job ran 14 real steps, so this is a build
      that happened, not an exhausted allowance. THE LADDER IS GREEN: no low
      rung is red, nothing in floatfea/ is implicated, and this is NOT A STOP.
      It is (d) against STEP 6, where verdict 56 already holds it.
cmd   the failing names, deduplicated
out   126 from test_report_carried.py (33 distinct tests) and 11 from
      test_the_guard_survives_the_state[baseline, two_digit_step_number,
      non_numeric_step_suffix, superscript_digit_step_number,
      draft_suffix_beside_a_step_report, step_number_is_the_empty_string,
      verdict_amended_after_the_commit_the_report_answers,
      zero_padded_step_number, answers_header_names_an_older_verdict_commit,
      guard_state_declared_GREEN_in_REQUIREMENT_CHANGED...,
      guard_state_the_whole_suite_line_names_an_ANCESTOR...]
judge THE GUARD-STATE SET GREW FROM 8 TO 11 AND I DO NOT WANT YOU TO REPORT
      THAT AS A REGRESSION WITHOUT LOOKING. Verdict 56's circularity cell
      predicted exactly this: with a step-6 verdict present the boundary
      assertion goes silent and the nested runs get FURTHER, into the
      "report has not answered verdict 56" diagnoses. Three states that used
      to die at the boundary now reach those. That is the prediction coming
      true, not a new defect -- but it IS a prediction. I have not re-measured
      each of the three at this commit and I am not claiming it as measured.
      Revision 3 is where it is confirmed or contradicted; name any that
      survives it.
cmd   gh pr view 1 --json comments --jq ".comments | length"
out   0 -- no outside-witness comment. Unavailable check, ninth round.
```

## My own instructions (4b), conftest (4c), tolerances (4)

```
cmd   git diff 9e02cb5..f7501ee -- .claude docs/SUPERVISOR.md
out   (empty).  NOT A STOP.
cmd   git ls-files -- tests/conftest.py "tests/**/conftest.py"
out   tests/conftest.py            -- the instruction's own expectation, met
cmd   git diff 9e02cb5..f7501ee -- tests/conftest.py "tests/**/conftest.py"
out   (empty)
cmd   git ls-files "*conftest.py"
out   tests/conftest.py -- still the whole set. No plugin was added, so no
      rung's green is written by code in its own directory.
cmd   count of the `NAME: Final[...] = value` lines in tolerances.py, both ends
out   48 at 9e02cb5, 48 at f7501ee, and the extracted lines hash identically
      (md5 f7bf915f0c67cae063dd523561d52e94 on both sides).
      NOT ONE VALUE MOVED.
cmd   git show --name-only f7501ee
out   floatfea/tolerances.py, tests/test_report_guard_states.py. TWO FILES.
      The `tests/corpus/tree_prose_claims.txt` change in the same range is
      788ce6f, mine. The implementer did not write the reviewer's trees.
```

## Carried

This file's previous verdict is 55. It carried R494, R495 and R496 as blocking,
R497 to R501 as closure items, and R475 / R486 / R487 / R492 / R493 on top.
Every one was ruled on in verdict 56; the statuses below are that ruling plus
what `f7501ee` did to it. Nothing here is a fourth review of step 5's work.

- **R494(A), R494(B) -- ANSWERED**, verdict 56 `Carried`, measured there.
- **R494(C) -- ANSWERED IN THE GUARD at `3aa804c`, THEN LIVE A THIRD TIME at
  `tests/test_report_guard_states.py:138` (R502), AND REPAIRED AT `f7501ee`.**
  ```
  cmd   git diff 9e02cb5..f7501ee -- tests/test_report_guard_states.py
  out   ("append_finding", str(STEP)) -> ("append_finding", str(VERDICT_STEP)),
        with six lines of comment naming R502 and R494(C).
  judge THE ONE-TOKEN REPAIR IS THE ONE I NAMED. `append_finding` edits the
        VERDICT file and `VERDICT_STEP` is the step the verdict is in. Whether
        the state now MEASURES anything is step 6's question, and it is
        condition 2 below rather than something I close from this file.
  ```
- **R494 as a whole -- NOT CLOSED, and it is STEP 6's item.** Its closing
  condition was `0 failed` locally AND a completed SUCCESS on CI. Neither holds
  at `f7501ee`. It carries in `docs/reviews/F2/step-6.md`, not here.
- **R495 -- half died with the revert, half re-raised as R503, and `f7501ee`
  answers it by the second of the two routes I offered.** The entry now says
  what brackets the value, and what it says is: nothing.
  ```
  cmd   git diff 9e02cb5..f7501ee -- floatfea/tolerances.py
  out   "BOTH ENFORCED" becomes "AND NEITHER ENFORCED SINCE DC0 (R503)"; the
        `--check` sentence is explicitly WITHDRAWN AND NOT REPLACED; the entry
        now reads "NOTHING IN THE SUITE WOULD NOTICE IF THEY STOPPED HOLDING"
        and records that `largest_rigid_eigenvalue` has one caller, the
        generator itself. Comment only. No value moved.
  judge THIS IS THE HONEST ROUTE AND IT IS THE HARDER ONE TO WRITE. An entry
        that records its own guard as absent is worth more than one that
        quietly stops mentioning it. YOU DID NOT RESTORE THE ENFORCEMENT AND
        YOU WERE RIGHT NOT TO: that is apparatus under the F6 freeze and it
        goes to Xabier, which is where you sent it. Whether R503 is CLOSED is
        step 6's ruling, because R503 is a step-6 finding.
  ```
- **R496, R497, R498, R499 -- CLOSED in verdicts 55 and 56.** Not reopened.
- **R500, R501 -- OPEN closure items,** restated as R509 / R510 in verdict 56.
- **R475 -- OPEN AND STILL BLOCKING F2-rung2's FIRST COMMIT**, with **R486**'s
  admissible-domain ceiling and **R487**'s one-line assertion in the same
  commit. THIS IS THE ITEM THAT MUST NOT BE LOST BY THIS PASS. It is named
  again in condition 3 below and it lives in step 6's file.
- **R488 -- ADOPTED, not closed.** R504 is advice against it, not a gate.
- **R489, R490, R491 -- CLOSED in verdict 55.** Not reopened.
- **R492 -- OPEN**, and R504 changes what replaces it.
- **R493, R471 to R474, and the 48 items frozen in `docs/milestones/F2a.md`
  section 7 -- OPEN on the frozen list,** not re-reviewed item by item.
- **R479 -- CLOSED in verdict 56.** Ten determinism legs ran and agreed.
- **R482 -- carried into R494, not separately live.**
- **R373 -- OPEN since verdict 53.** This verdict is a fresh instance of it.
  Restated as R513.

## Findings

**Two, and I found the first by checking whether my own write was inert.** I did
not want this verdict to move a test, so I measured it. It moves one, and the
reason it moves one is a defect in a gate.

**R511. (BLOCKS -- (c).) `test_every_named_site_is_touched_or_declared` CLOSES A
NAMED SITE WHEN THE REVIEWER TOUCHES IT, AND IT MANUFACTURES SITES THE
IMPLEMENTER IS FORBIDDEN TO TOUCH. `tests/test_report_carried.py:2519` and
`:2576`.**

```
cell  scratch clone of f7501ee; docs/reviews/F2/step-5.md Verdict line only,
      HOLD then PASS. Nothing else moved -- and the FIRST attempt at this cell
      was wrong: `git revert -q` is not an option, the revert silently did not
      happen, and the two sides were the same side. Redone with an explicit
      checkout of the old blob. The numbers below are the redone run.
cmd   python -m pytest -q tests/test_report_carried.py, both sides
out   HOLD: 127 failed, 158 passed
      PASS: 126 failed, 159 passed
      diff of the failing sets, exactly one name:
      test_every_named_site_is_touched_or_declared[R502-docs/reviews/F2/step-5.md]
judge WRITING A VERDICT INTO step-5.md CLOSES A SITE CHECK. Nothing was
      answered. I edited the reviewer's own file and an item went green.
```

Two separate defects produce that and both are in the same file.

*(i) `TOUCHED` has no reviewer-tree exclusion, and the same file knows better.*
`_changed_lines()` runs a bare `git diff -U0 <reviewed>` with no pathspec.
Three hundred lines up, `_implementer_commits_after()` excludes
`REVIEWER_TREES = ("tests/corpus", "docs/" + "re" + "views")`, and its comment
says why: ".claude/hooks/ refuses both of these to the implementer, so a commit
touching nothing else is the reviewer's by construction." The reasoning was
written down and then not applied to the sibling function. Consequence: **any
site a verdict names inside `docs/reviews/` or `tests/corpus/` is closed by the
reviewer's own next write**, and `scripts/write_verdict.py` rewrites the whole
verdict file every round, so it is closed automatically, every round, for ever.

*(ii) `_sites_by_finding()` cannot tell a NAMED SITE from a path that is
measured OUTPUT.* R502 names exactly one site,
`tests/test_report_guard_states.py:138`. The string `docs/reviews/F2/step-5.md`
appears in its block as the printed value of `REVIEW_PATH` inside a `cmd`/`out`
cell: it is data, not an instruction. The guard parsed it as a site and demanded
the implementer touch it or write `no change` beside it, and a `PreToolUse` hook
forbids the first of those. The same shape is live at HEAD in three more cells I
can see from my own run -- `[R507-frames.txt]`,
`[R507-g22_model_configurations.txt]`, `[R507-tree_prose_claims.txt]` -- three
corpus filenames that R507 quotes as the EVIDENCE FOR its mechanism, turned into
three red parametrisations against files the implementer may not open.
`[R507-frames.txt]` is not even a path: it is the tail of
`g21_rigid_body_frames.txt`, broken across a line in my own prose.

**Why this is (c) and not prose.** It is what a gate claims, on which quantity.
In one direction it reports an item answered that nobody answered; in the other
it reddens on items nobody raised, in a tree the implementer cannot write. Both
directions are wrong and both are load-bearing: this guard is the mechanism that
CLAUDE.md's "half of an item is not the item" rule runs on, and four of the
thirty-three red parametrisations at HEAD are its own artifacts.

**Closed when** `_changed_lines()` takes the same `REVIEWER_TREES` pathspec its
sibling takes, AND a site inside a reviewer-owned tree is either not generated
as a parametrisation at all or is generated with a status saying the implementer
cannot touch it. I am naming the property, not the implementation, and this is
not new apparatus: both halves are edits to a guard that exists. If you conclude
the right answer is that the guard should not parse paths out of `cmd`/`out`
blocks at all, that is within (c) and I will rule on it.

**R512. (Closure item, and it is MINE.) SIX OF MY FOURTEEN CORPUS FILES HAVE NO
READER IN THE REPOSITORY, AND THE COVERAGE NUMBERS I PUBLISHED FOR THEM WERE
NOT RE-TAKEN WHEN THAT BECAME TRUE.**

```
cmd   for each file in tests/corpus, git grep -l <stem> with tests/corpus and
      docs excluded
out   carried_item_routing    NO READER   (last written at verdict 32)
      carried_row_subject     NO READER   (verdict 35)
      ci_determinism          NO READER   (verdict 35 -- the ci.yml hit is
                                           test_ci_determinism_gate.py, a
                                           substring, not this file)
      pinned_interpreter      NO READER   (verdict 31)
      prose_triple_shapes     NO READER   (verdict 51)
      report_numbers_sourced  NO READER   (verdict 36)
      The other eight ARE read: ci_ladder_gating, tolerance_marker_exemptions,
      report_ci_section, report_guard_states, report_status_vocabulary,
      tree_prose_claims, g21_rigid_body_frames, g22_model_configurations.
judge THIS IS BP0 TURNED ON ME. "When a decision rule changes, every figure
      citing the old rule is regenerated or withdrawn in the same commit."
      Each of those six batches shipped with a caught-over-total coverage
      number. For `prose_triple_shapes.txt` the rule demonstrably changed by
      directive -- CLAUDE.md records that the prose detectors were DELETED --
      so its coverage figure describes a check that no longer exists and I
      never withdrew it. Whether the other five are retired-guard residue or
      genuine orphans I do not know, and the honest statement is that I have
      not looked.
```

**Closed when** each of the six is either deleted with one line naming the guard
it measured and when that guard went, or its reader is named. **This is not
yours to fix** -- `tests/corpus/` is mine and the hook refuses it to you. I
carry it and I do it in a corpus commit. It is recorded here because the rule I
have been applying to your figures applies to mine, and because a reader six
months from now should not find six files that look like live gates.

**R513. (Closure item.) R373, unchanged, now in its third instance.** The
`Reviewed commit:` line at the top of this file says `f7501ee`, which is HEAD
when I typed; the commit whose work this PASS is about is `125cee1`.
`scripts/write_verdict.py` stamps `sha()` unconditionally. Verdict 53 flagged
it; verdict 56's header says `788ce6f`, my own corpus commit, while its body
judges `9e02cb5`; and now this. It has never misled anyone because every verdict
says so in its first paragraph, which is exactly why it has survived three
rounds. **Closed when** the script takes the judged commit as an argument, or
the field is renamed to what it is. Apparatus under freeze: it goes on the
frozen `docs/milestones/F2a.md` list, not into a step commit.

## Tolerances touched

**One entry's comment. No value, no form, no counter, no injection.**

| entry | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `RIGID_MODE_BOUND` | 199.53 | 199.53 -- UNCHANGED | unchanged | unchanged | `floatfea/tolerances.py:360-403`; the finding is R503 in `docs/reviews/F2/step-6.md` |

```
cmd   extract every `NAME: Final[...] = value` line from floatfea/tolerances.py
      at 9e02cb5 and at f7501ee and compare
out   48 and 48; added [], removed [], changed []; identical md5.
judge NO TOLERANCE VALUE MOVED. What changed is the entry's account of what
      enforces it, from a claim that was true before DC0 to a statement that
      nothing enforces it now. Under "never widen" that is the correct
      direction: it makes the gap louder, not quieter. Under BI3 it is also
      the right home -- the entry carries the statement and a pointer to where
      the decision goes, rather than a table that nothing regenerates.
```

## Adversarial corpus (BE3)

**No batch this round, and this is a statement rather than a silence.** Two
reasons and both are measured.

1. The corpus relevant to the work in front of you is
   `tests/corpus/report_guard_states.txt`, and verdict 56 told you in writing
   not to edit it while you repair the states that read it. Adding entries now
   would move the target underneath a repair I asked for. It gets its batch at
   the verdict that judges revision 3.
2. R512. Six of my files have no reader. Adding a fifteenth, or entries to an
   orphan, would be adding data that measures nothing -- the exact defect I
   have charged you with under "empty parameter set is an error, not a skip".
   I am not doing it to make a section look full.

**New entries this round: 0. Caught by the implementer's checks: not
applicable.** The last real measurement stands: batch 6, 14 unseen RUNNER-claim
shapes, at `788ce6f`.

## On the criterion itself, once

**The gap you hit is real, this verdict does not fix it, and it will recur at
every step boundary where a tree round lands on a closed step.** What I did here
is write the true disposition into the file the gate reads. What I did NOT do is
remove the mechanism that made the file false: `scripts/write_verdict.py` has no
way to say "this verdict is about the tree at step k+1", so the next time two
commits land on a closed step before the next step's report is reviewed, the
same HOLD goes into the same header and the same dead end reappears.

The cheapest fix is still one sentence in `CLAUDE.md` section Step gating: *a
verdict written into step k's file about work at step k+1 does not hold step k,
and the reviewer restores the header to the step's own disposition.* That is
Xabier's sentence. It needs no code, no hook change and no apparatus, and this
verdict is the worked example of what it would have authorised. Said twice now,
verdict 56 and here, and I will not say it a third time inside the loop.

## Next step opens when

**Step 5 is closed and PASSED, and this is the last verdict this file gets.**
Nothing from step 5 survives as a step-5 item. What follows are conditions that
live in `docs/reviews/F2/step-6.md`, restated here only so this PASS cannot be
read as clearing them.

1. **Revision 3 of `docs/reports/F2/step-6.md` answers verdict 56**, carrying
   R502 and R503 with their statuses and adding the four nested-run lines R505
   asked for. That is the next thing you write, as you said.
2. **`python -m pytest -q` is `0 failed` at the resulting commit and
   `gh run list --commit <that sha>` is a completed SUCCESS.** 137 is the number
   to beat. **One of the 137 --
   `test_every_named_site_is_touched_or_declared[R502-docs/reviews/F2/step-5.md]`
   -- GOES GREEN THE MOMENT THIS VERDICT IS COMMITTED, AND NOT BECAUSE YOU DID
   ANYTHING.** Do not report it as a repair. Report it as R511.
3. **R511 is answered**, at `tests/test_report_carried.py:2519` and `:2576`. It
   is (c) and it blocks step 6.
4. **R475 is answered in the FIRST commit of F2-rung2**, unchanged and still
   blocking, with **R486**'s admissible-domain ceiling and **R487**'s one-line
   assertion in the same commit. This PASS does not touch it.
5. **R512 and R513 are closure items and neither is yours.** R512 is mine and I
   do it in a corpus commit. R513 goes on the frozen 4a list.

**On the schedule, one paragraph, and it is the escalation CLAUDE.md asks for.**
Step 6 is measured against 31 October. Two verdicts, 56 and 57, have now gone on
a boundary rather than on the work, and that cost is not recoverable by working
harder inside the loop. **Two consecutive steps have closed carrying a blocking
item**: step 5 closed at verdict 53 carrying R475, and it closes again here with
R475 still unanswered four verdicts later. CLAUDE.md says that is escalated with
the choice stated. The choice is: **slip the date, or drop R486's
admissible-domain ceiling from F2-rung2's first commit and take the gate on
R475's row-shared form alone.** I recommend the second. I am not authorised to
choose it, so it goes to Xabier together with the criterion paragraph above, in
one message, today -- not when step 6 closes.
