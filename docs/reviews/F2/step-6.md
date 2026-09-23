# Review — F2 step 6
Reviewed commit: be1d9e2db8c3c82ff3830bed25dd10cf2b49821c
Verdict: HOLD

**Reviewed commit: `8e64f22`.** Fifty-eighth verdict, and the **second verdict
on step 6** -- one more is available under CZ0 before the step closes.

Tests: **4 failed, 2592 passed, 0 skipped** -- my run, clean tree at `8e64f22`,
`python -m pytest -q`, 611.20 s, Python 3.13 on Windows.

```
out  tests/test_report_guard_states.py::test_the_guard_survives_the_state
       [two_digit_step_number_discriminating]                         :606
       [answers_header_names_an_older_verdict_commit]                 :333
       [guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_
        state_actually_REDDENS_CONTROL]                               :333
       [guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_
        THE_SUITE_WAS_RED]                                            :414
judge NOTHING IN floatfea/ IS RED. Nothing in tests/verification/ is red.
     test_report_carried.py is entirely green at this commit, which is the
     collapse you predicted for the excluded set and it happened.
     ALL FOUR ARE IN THE HARNESS, and three of them never reach the guard.
```

**Commits judged: `f7501ee`, `53cfeee`, `7115410`, `8945a4e`, `60999c9`,
`5755de8`, `028ac59`, `8e64f22`.** (`18f51fc`, `3b5d6eb` and `788ce6f` in the
range are mine.)

## Item 1b -- CHECKED, AND IT IS NOT CLEAN, AND IT DOES NOT HOLD

```
cmd  the newest Answers line in the report under review
out  docs/reports/F2/step-6.md:912 -- Answers: verdict 56 @ 18f51fc
cmd  the newest verdict in the repository before this one
out  verdict 57, committed at 3b5d6eb, in docs/reviews/F2/step-5.md
judge THE HEADER NAMES 56 AND THE NEWEST IS 57. One comparison, made, and it
     does not match. I am NOT holding on it, and the reason is measured
     rather than argued: verdict 57 is a DISPOSITION of step 5, it says so in
     its own first paragraph, and the one finding it raised for step 6 --
     R511 -- is in the report by name and is answered at 60999c9. The Carried
     list the report is written against is therefore the right list. 1b
     exists so that no Carried claim is about a superseded round; nothing
     here is. Recorded, not charged, and R513 already owns the underlying
     shape.
```

## CI at the reviewed commit (3b) -- UNAVAILABLE, and not for the CK2 reason

```
cmd  gh run list --commit 8e64f22 --json name,conclusion,workflowName
out  []
cmd  the same for 028ac59 and 5755de8
out  [] and []
judge NO WORKFLOW RAN ON THE REVIEWED COMMIT. .github/workflows/ci.yml
     paths-ignore carries docs/reports/** and 8e64f22 touches nothing else,
     so the push was skipped by design. NOT CK2 -- no job was started and
     cancelled for payment; none was created. Recorded as an unavailable
     check, and it does NOT hold on its own.
cmd  gh run list, newest entry, and where its head sits
out  35882767142, head 8a88bf2, event push, conclusion FAILURE.
     git log -1 --format=%p 8a88bf2 -> 028ac59, so it is the FORCE-PUSHED-OUT
     revision 3, sitting on the same parent as the one in history.
cmd  git diff 8a88bf2 8e64f22 -- floatfea tests scripts .github
out  (empty)
judge SO THE LAST RUN THAT EXECUTED RAN THE CODE UNDER REVIEW, BYTE FOR BYTE.
     Only docs/reports/F2/step-6.md differs. Its result still describes this
     tree and it is FAILURE.
cmd  gh run view 35882767142 --json jobs
out  the verification ladder            | success
     lint, unit and guards              | FAILURE | 12 named failures
     CI determinism -- leg / ten agree  | skipped
judge THE LADDER IS GREEN ON LINUX ON THIS CODE. No low rung is red. THIS IS
     NOT A STOP.
cmd  the 12 names, against my 4
out  11 guard states + test_the_whole_suite_line_is_about_a_commit_that_
     exists. Eight of the eleven are the baseline cascade and they are GREEN
     at 8e64f22 -- 028ac59 fixed the line they hang off. Three survive into
     my run. ONE OF MY FOUR IS NOT IN CI'S TWELVE, and that is R516.
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, ninth round.
```

## My own instructions (4b), conftest (4c), tolerance values (4)

```
cmd  git diff 9e02cb5..8e64f22 -- .claude docs/SUPERVISOR.md
out  (empty).  NOT A STOP.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction's own expectation, met
cmd  git diff 9e02cb5..8e64f22 -- tests/conftest.py "tests/**/conftest.py"
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is written by code in its own directory.
cmd  53cfeee touched what
out  CLAUDE.md only. A standalone process: commit citing DD1. CORRECT under
     the rule, and it deletes no guard -- I read the added paragraph line by
     line. 7115410 touched docs/milestones/F2.md only, a standalone plan:
     commit citing DD0.
cmd  every NAME: Final[...] = value at 9e02cb5 and at 8e64f22
out  48 and 48; added [] removed [] changed []. NOT ONE VALUE MOVED.
```

## Carried

Verdict 56 carried **R502** and **R503** as blocking, R504 as advisory, R505 to
R510 as closure items, and R475 / R486 / R487 / R488 / R492 / R493 / R500 /
R501 as open on top. Verdict 57 added **R511** (blocking), R512 and R513
(closure).

- **R502 -- ANSWERED, and the repair is the right one.**
  `tests/test_report_guard_states.py:144` now reads
  `[("append_finding", str(VERDICT_STEP))]`. The state is GREEN in my run at
  `8e64f22`, and green because the guard ran: `require=green` for that entry
  means the nested run must be clean, and a `FileNotFoundError` in the builder
  can no longer be mistaken for it. Your paragraph withdrawing "the other six
  cascade from baseline" is accurate and I accept it. The report half of the
  condition -- naming the nested run's own line for that state -- is still not
  done; that is R505 and it stays a closure item.
- **R503 -- NOT CLOSED, and it is now false in the other direction. R514.**
  You took the first branch of the condition (the assertion) and left the
  entry saying the second branch was impossible. Details below.
- **R504 -- ADVICE, unchanged, not a condition.** DB0 is not in this diff.
- **R505 -- OPEN closure item.** `docs/reports/F2/step-6.md` line 1319 carries
  a paragraph naming the four states and no nested-run line for any of them.
  A reader still cannot tell "green because the guard reported" from "green
  because the harness stopped asking", which is the whole content of R494.
- **R506, R507 -- CLOSED, and closed the way I asked.** `5755de8` keeps what
  was measured and deletes what was not. "It ran four times" and "every time"
  are gone from `tests/test_plan_figures.py`. I verified the survivor
  sentence: the two corpus files that feed rendered rows are named, in the
  past tense, against a named commit -- which is the one shape in this family
  a later commit cannot falsify, and it is the control in my batch 7.
- **R508 -- CLOSED as recorded.** You recorded it rather than rewriting the
  commit message, which is the right handling of a pushed message.
- **R509, R510 -- OPEN closure items,** unchanged.
- **R511 -- ANSWERED IN BOTH HALVES, and the second half is answered better
  than DD3 asked.** `_changed_lines()` takes the `REVIEWER_TREES` pathspec at
  `tests/test_report_carried.py:2500-2515`, so my own write can no longer
  close a site. `_tracked_at_reviewed` kills `frames.txt` and keeps the other
  two, and `_R507_CONTROLS` says so in the file with the outcome each
  ACTUALLY produces rather than the one the directive predicted. I ran the
  three controls myself and they are green. **That is the correct handling of
  a directive that was wrong about its own reach, and it is the best thing in
  this diff.** It also opened one hole -- R518.
- **R512, R513 -- OPEN closure items,** unchanged. R513 is live in this very
  file: the `Reviewed commit:` line at the top is stamped HEAD by
  `scripts/write_verdict.py` and is not the commit judged. The commit judged
  is `8e64f22`.
- **R475 -- OPEN AND STILL BLOCKING F2-rung2's first commit.** DB0 is measured
  and not written; correct.
- **R486 -- MOVED OUT OF F2 BY DD0 and recorded at `7115410`.** I read the
  plan section. It states what is given up. **I do not reopen it and I agree
  with the ruling, which was mine to argue and Xabier's to make.** It is
  carried out of this milestone, not closed.
- **R487 -- OPEN, stays with R475,** and DD0's explicit call is right: the
  triangle-inequality assertion is a property of the residual form, not of a
  domain, so it does not follow R486 to F3.
- **R488, R492, R493, R500, R501 -- OPEN,** unchanged, none re-reviewed.
- **R479 -- CLOSED in verdict 56; not reopened.**
- **The 48 items frozen in `docs/milestones/F2a.md` section 7 -- OPEN on the
  frozen list,** not re-reviewed item by item.

## Findings

**First, what is right, and it is most of the diff.** `f7501ee`'s one-token
repair is correct and I confirmed it by running the entry that found the
defect. `60999c9` is the best work in this round: it answers a directive,
finds that the directive was wrong about its own reach, says so in the file
with parametrised controls asserting what actually happens, and does not
quietly claim the third case. `5755de8` deletes rather than defends. `028ac59`
regenerates the line at the commit the report sits on and states the rewrite
in the message, which is R461 handled correctly the second time. `8945a4e`
restores a real enforcement without restoring the false failure -- the idea is
right, and two of the three findings below are about how it was recorded and
how far it reaches, not about whether it should exist.

---

**R514. (BLOCKS -- (b).) R503 IS NOT CLOSED. YOU TOOK THE FIRST BRANCH OF THE
CONDITION AND LEFT THE ENTRY ASSERTING THE SECOND BRANCH WAS IMPOSSIBLE.
`floatfea/tolerances.py` NOW TELLS ITS READER THAT NOTHING GUARDS
`RIGID_MODE_BOUND`, ONE COMMIT AFTER SOMETHING STARTED TO.**

```
cmd  git show --stat 8945a4e
out  tests/test_plan_figures.py | 78 ++++++  -- ONE FILE. floatfea/
     tolerances.py is not in it.
cmd  what the entry says at HEAD, floatfea/tolerances.py:363 and :394-403
out  :363  "TWO CANDIDATES, BOTH RENDERED, AND NEITHER ENFORCED SINCE DC0"
     :395  "NOTHING IN THE SUITE WOULD NOTICE IF THEY STOPPED HOLDING"
     :397  "`largest_rigid_eigenvalue` has one caller in the tree, the
            generator itself, and no assertion anywhere compares it with this
            constant. The same is true of the mechanism ceiling."
     :401  "closing it is a decision about apparatus under a freeze -- so it
            goes to the technical supervisor, not into the next commit I
            happen to be writing."
     :388  "THE SECOND HALF OF THAT SENTENCE IS WITHDRAWN AND NOT REPLACED"
cmd  what the tree does at HEAD
out  tests/test_plan_figures.py:103 test_every_floor_class_row_clears_its_
     tolerance_on_THIS_tree renders on the tree, resolves each floor-class
     row's ceiling through R._ceiling(), and asserts the margin. `_ceiling`
     at scripts/regen_figures.py:744 returns getattr(T, "RIGID_MODE_BOUND")
     for both rows. The test is GREEN in my run.
judge EVERY ONE OF THOSE FIVE SENTENCES IS FALSE AT THE COMMIT THAT SHIPS
     THEM. They were all true at f7501ee. 8945a4e -- the NEXT commit -- made
     them false and did not touch the entry. The last one is the sharpest:
     it says the repair will not go into the next commit, and the next commit
     is exactly where it went.
judge WHY THIS IS (b) AND NOT PROSE, and it is the same reason verdict 56
     gave for the same site, pointing the other way. CLAUDE.md section
     Tolerances makes the written justification part of what a tolerance is;
     the entry is the ONLY statement of what 199.526231496888 means and what
     brackets it; and the criterion's carve-out names exactly this case. A
     reader in six months is told nothing guards the bound, and something
     does. The direction of the error does not change its class -- an
     understated guarantee is the one a reader stops reading, which is why it
     survives longer than an overstated one.
judge AND THE CONDITION ITSELF. R503's Closed when offered two branches:
     assert the two brackets where the entry says they are, OR have the entry
     stop claiming enforcement and say what does bracket the value. You did
     the first and wrote the second. Neither branch is met, site by site:
       floatfea/tolerances.py:363   OPEN -- now false the other way
       floatfea/tolerances.py:388   OPEN -- "NOT REPLACED" was replaced
       floatfea/tolerances.py:394-403 OPEN -- three sentences, all false
       the assertion itself          DONE and correct
judge BP0 IS THE RULE THIS BREAKS, in its own words: when a decision rule
     changes, every figure citing the old rule is regenerated or withdrawn IN
     THE SAME COMMIT, not the next one and not when someone notices.
```

  **Closed when** the entry says what the tree does: both brackets are
  asserted, by name, in `tests/test_plan_figures.py::test_every_floor_class_
  row_clears_its_tolerance_on_THIS_tree`, and the withdrawal note at `:388`
  either goes or says what replaced it. Site by site: `floatfea/
  tolerances.py:363`, `:388`, `:394-403`. **No tolerance value moves.** This
  is deletion and one sentence, not apparatus.

---

**R515. (BLOCKS -- (c).) THE ENFORCEMENT 8945a4e RESTORED HAS NO NAMED DOMAIN.
FLIPPING TWO TOKENS IN THE GENERATOR REMOVES BOTH BRACKETS FROM IT AND THE
TEST STAYS GREEN. `assert checked` PROVES THE COLLECTION IS NOT EMPTY AND SAYS
NOTHING ABOUT WHETHER THE TWO ROWS THE TOLERANCE ENTRY NAMES ARE IN IT.**

```
cell ABLATION, one variable, in a scratch clone of 8e64f22. In
     scripts/regen_figures.py, _floor("rigid_mode_largest_rigid_eigenvalue",
     "below", "RIGID_MODE_BOUND") -> _floor(..., "derived"), and the same for
     rigid_mode_mechanism_ceiling. Nothing else touched.
cmd  python -m pytest tests/test_plan_figures.py -q -k clears
out  1 passed, 192 deselected, 162.33 s
judge SO THE ONE ASSERTION THAT NOW BRACKETS RIGID_MODE_BOUND CAN BE REMOVED
     FROM BOTH ITS QUANTITIES BY TWO TOKENS IN A FILE THAT IS NOT A TEST, AND
     THE SUITE STAYS GREEN. The loop iterates whatever floor_class() returns
     and `continue`s on any other kind; the only guard is that the set is
     non-empty, and 6 other rows keep it non-empty.
judge THIS IS THE RECORDED GUARD ABOUT ASSERTION DOMAIN, word for word: check
     that the collection the assertion inspects can actually contain the
     failure. A row removed from the class before the list is built never
     reaches the assertion that checks the class.
judge IT IS ALSO THE EXACT DEFECT DC0 WAS CLEANING UP. --check's ceiling job
     had the same shape, and what made its loss invisible was that no
     assertion named a quantity. The replacement inherits that.
judge WHAT I AM NOT SAYING. The test is good and the counter-case in 8945a4e's
     message is a real one -- ceil/1e6 is arithmetically the same perturbation
     as value*1e6, so it is measured in the right quantity. The gap is the
     domain, not the decision.
```

  **Closed when** the two quantities the `RIGID_MODE_BOUND` entry names are
  named by the assertion -- the cheapest form is that the test requires
  `rigid_mode_largest_rigid_eigenvalue` and `rigid_mode_mechanism_ceiling` to
  be present in `checked`, which is one line and no new apparatus. **This is a
  fix to an existing guard that passes false, which CZ0 permits explicitly.**

---

**R516. (BLOCKS -- (c) and (d).) `two_digit_step_number_discriminating` IS RED
AT `8e64f22`, IT IS THE ONE RED THAT MY VERDICT DOES NOT CLEAR, AND IT WAS
GREEN ON CI ONE COMMIT AGO ONLY BECAUSE AN UNRELATED TEST WAS ALSO FAILING.**

```
cmd  python -m pytest tests/test_report_guard_states.py -q -k
       two_digit_step_number_discriminating
out  1 failed. tests/test_report_guard_states.py:606 --
     "the guard failed through ['test_the_Carried_table_is_what_the_
      generator_produces'], none of which is a named reporter"
cmd  read the nested run's own output out of that failure
out  1 failed, 290 passed. The single failure names R999 in its message:
     "| R999 | **open** - blocking, and not answered in this round | planted
      by the harness. |"
judge THE GUARD DID EXACTLY WHAT THE CORPUS ENTRY ASKS. It parsed `10` as ten,
     it found the planted finding, it named it. The state fails because
     `named` at tests/test_report_guard_states.py:587-601 does not contain
     `test_the_Carried_table_is_what_the_generator_produces`, so the last
     assertion at :606 reports "nobody can locate it" about a failure that
     names the item, the file and the regeneration command.
cell WHY IT WAS GREEN BEFORE AND IS RED NOW. ONE VARIABLE: the whole-suite
     line. At 8a88bf2 the nested run ALSO failed
     test_the_whole_suite_line_is_about_a_commit_that_exists, which IS in
     `named`, so `any(...)` was satisfied and the state passed. 028ac59 fixed
     that line. Same code, one docs line moved, and the state's pass
     disappeared with it.
cmd  gh run view 35882767142 --log-failed, the twelve names
out  two_digit_step_number_discriminating is NOT among them; two_digit_step_
     number (the non-discriminating twin) is.
judge SO THE STATE HAS BEEN CERTIFYING NOTHING. It passed on the presence of
     an unrelated red. That is the recorded guard about a gate carrying its
     own failure -- ask of every test whether it would go red if the thing it
     claims were false, and here the inverse happened: it went GREEN on a
     failure it was not about.
judge THIS IS (c) BEFORE IT IS (d). The threshold is the `named` allow-list,
     and it decides whether a real, located, item-naming failure counts as a
     report. It is stale by one test name, and the test it is missing is the
     one this state's whole purpose depends on.
```

  **Closed when** `test_the_Carried_table_is_what_the_generator_produces` is
  in the tuple at `tests/test_report_guard_states.py:587-601` and the state is
  green with that as the nested run's only failure -- or the corpus entry's
  `require=` is shown to be wrong, which I do not think it is. **Do not edit
  `tests/corpus/report_guard_states.txt`.** One line, no new apparatus.

---

**R517. (BLOCKS -- (c) and (d).) THREE NEGATIVE CONTROLS CANNOT BE BUILT AT A
STEP'S FIRST VERDICT, AND ONE OF THEM RAISES A BARE `IndexError` IN ITS
BUILDER -- R502'S SHAPE AGAIN, AT `tests/test_report_guard_states.py:414`.**

```
cmd  the three failures and their lines
out  answers_header_names_an_older_verdict_commit                     :333
     guard_state_declared_GREEN_in_REQUIREMENT_CHANGED...             :333
     guard_state_the_whole_suite_line_names_an_ANCESTOR...            :414
cmd  what :333 says
out  AssertionError: the verdict file has one commit, so there is no older
     verdict to name and this state cannot be built
     assert 1 > 1  where 1 = len(['18f51fc'])
cmd  what :414 does
out  subprocess.run(["git","log","--format=%h","--",REVIEW_PATH]).stdout
       .split()[1]   ->  IndexError: list index out of range
judge THE CAUSE IS STRUCTURAL AND IT WILL RECUR EVERY TIME. `VERDICT_STEP` is
     6 now, `REVIEW_PATH` is docs/reviews/F2/step-6.md, and that file has ONE
     commit because verdict 56 was its first. Both builders assume the
     verdict file has a history two deep. At the first verdict of any step it
     does not.
cell ABLATION, one variable, scratch clone of 8e64f22: one extra commit
     appending a line to docs/reviews/F2/step-6.md, nothing else.
out  BEFORE 4 failed. AFTER 3 passed, 1 failed -- and the one is R516.
judge SO THREE OF THE FOUR REDS ARE CLEARED BY THE ACT OF WRITING THIS
     VERDICT, WHICH IS NOT A REPAIR. Next step's first verdict reproduces
     them exactly. R502 was "a control that raises in its builder measures
     nothing"; :414 is the same sentence with a different index, and :333 is
     the honest version of it -- it at least says what happened.
judge I AM RECORDING THE ONE THING IN MY FAVOUR AND AGAINST ME BOTH: these
     three were green in your run and on CI, and they were green because the
     verdict file happened to be deep enough. The condition is on MY writing,
     not on your code, which is precisely why neither of us saw it until the
     step boundary moved.
```

  **Closed when** the two builders state what they need and produce a
  diagnosis rather than an index error: `:414` must not index `[1]` without
  the same `len(history) > 1` check that `:333` already has, and a state that
  cannot be built must be reported as unbuildable rather than as a failed
  guard. **A state that cannot be built is not a state that failed**, and the
  distinction is the entire content of R494 and R502. Delete no state.

---

**R518. (BLOCKS -- (c).) `_tracked_at_reviewed` SILENTLY DROPS A SITE WHOSE
PATH DID NOT EXIST AT THE REVIEWED COMMIT, SO A CLOSING CONDITION THAT ASKS
FOR A FILE TO BE CREATED PRODUCES NO ASSERTION AT ALL.**

```
cmd  import tests/test_report_carried.py and ask it
out  _tracked_at_reviewed("tests/verification/rung1/test_new_thing.py")
       -> False
     _tracked_at_reviewed("frames.txt")                    -> False
     _tracked_at_reviewed("g22_model_configurations.txt")  -> True
judge THE COMMENT AT :2650 THOUGHT ABOUT DELETION -- "a file the step deletes
     was a real site when the verdict named it" -- AND NOT ABOUT CREATION. A
     verdict whose Closed when names a file the step must ADD is dropped by
     `continue` at :2652, so no parametrised case is generated for it and the
     guard is green while checking nothing. That is the empty-parameter-set
     shape at row granularity: an entry that vanishes reads as agreement.
judge IT IS NOT LIVE AT THIS COMMIT -- every path verdict 56 named exists, and
     every path this verdict names exists. It is (c) because it is a change
     to what the gate claims, made this round, and the guard's own
     parametrisation is where a silent narrowing is least visible.
judge AND IT IS NOT WHAT DD3 ASKED FOR. DD3's target was a bare fragment,
     `frames.txt`, broken across a line. Your own `_R507_CONTROLS` docstring
     says existence cannot separate `named` from `printed`. The narrower rule
     does the same job: drop a string only when it has NO path separator AND
     is not tracked. `frames.txt` still dies; the two survivors still survive;
     a path naming a file to be created survives too.
```

  **Closed when** a path with a separator that the repository does not have is
  still a site -- it can be declared in the report's untouched-sites section
  like any other -- or the guard reports the strings it dropped. The first is
  one condition on the `if` at `tests/test_report_carried.py:2652` and adds no
  apparatus.

## Closure items (CZ0). None of these is (a), (b), (c) or (d).

**R519. `docs/reports/F2/step-6.md` section 3 declares the R503 sites with a
reason that belongs to the previous round.** Every `floatfea/tolerances.py`
row reads "**no change** -- the sentences the finding names are restored by
reverting the DB1 prose commit, not edited". They WERE edited, at `f7501ee`,
in this round, which is what R514 is about. The generated column beside it
("the file is touched and this line number is the old one") is correct; the
hand-written reason is stale. Closed by rewriting the reason or by the R514
edit making the row moot.

**R520. R505, unchanged.** The four nested-run lines are still not in the
report. I took the measurement in verdict 56 and again here; it remains a
thing the report should carry rather than the verdict.

**R521. R509, unchanged.** `scripts/answered_table.py` still takes the
fragment after the item number as the subject: `R502 | and (d).) THE EIGHTH
RED IS NOT A CASCADE.`, `R504 | -(d). You asked for my read...`. Harmless to
the status column, misleading in the subject one.

**R522. R510, unchanged.** R476 (`ZeroDivisionError` on a coincident tip
node), R477, R478, R480.

**R523. No CI run exists at the reviewed commit, and that is now the second
round in which the tree under review has never been on a machine neither of us
controls at its own sha.** The last executed run covers the same code byte for
byte, which is why this is not a finding under (d) -- but the coincidence is
doing work it was not designed to do, and one `workflow_dispatch` at the head
would end the question. Closed by dispatching one.

## Tolerances touched

**NONE. No constant was created, retired, moved or renamed.**

```
cmd  every NAME: Final[...] = value at 9e02cb5 and at 8e64f22
out  48 and 48. added [] removed [] changed []
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance value touched this round** | -- | -- |

**But 28 lines of `floatfea/tolerances.py` changed and they are the record of
why `RIGID_MODE_BOUND` is what it is, and the record is now wrong.** That is
R514 and it is the reason this is a HOLD rather than a PASS with a list. The
value is right; the sentence a reader is given about what guards it is false
in five places, in the safe-looking direction.

The shape R475 asks for is unchanged and still owed with DB0's form: relative
and dimensionless by construction; the counter injected on a rotational dof at
more than one span; and **R487's one-line assertion replacing the
`content > 0` comment in the same commit.** R486's admissible-domain ceiling
has left F2 by DD0 and is not owed here.

## Adversarial corpus (BE3)

**13 new entries, all unseen by the implementer, committed separately at
`be1d9e2`. `tests/corpus/tree_prose_claims.txt`, entries 70 to 82.** New part
6: the **REPAIR-STALE claim**.

Batch 5 was the POINTER claim (part 4) and batch 6 the RUNNER claim (part 5): a sentence that
was ALWAYS false. This round produced the other half and it is harder. A
REPAIR-STALE claim was **TRUE at the commit that wrote it** and was made false
by a **later commit in the same round** -- usually the commit that closes the
gap the sentence records. It is false in the reassuring direction, so it reads
as candour and a reader who agrees with it stops.

```
cmd  grep -c "^id=" tests/corpus/tree_prose_claims.txt
out  82   (69 before this batch)
```

**Coverage measurement. 13 new entries; the implementer's checks caught 0 of
13.** The mechanism, so the zero is not taken on trust:
`tests/test_tree_prose_consistent.py` rules only on explicit `claim:` /
`cmd:` / `out:` triples -- the absence and retired-alias keyword lists were
deleted, and `CLAUDE.md` records why. Every sentence in batch 7 is plain
comment prose and carries no triple. And the vocabulary
`{count, lines, files, defined}` at `:235` **has no term for time**: a triple
can ask whether something is true now, never whether it is STILL true, and a
triple written at `f7501ee` and never re-run is precisely the defect.

**Four of the thirteen are LIVE at `8e64f22`** and each is refuted by one
command; they are the cells inside R514. **4 of 4 live repair-stale claims
found by reading the diff, 0 of 4 by any check in the repository.** One entry
is a **control that must be ALLOWED and is**: the `tests/test_plan_figures.py`
deletion note's surviving sentence, which names a commit in the past tense and
therefore cannot be falsified by a later one. That is the shape the repair
should take everywhere.

**And the recheck on batch 6, because a corpus that is not re-measured
is a list.** Three of batch 6's fourteen were live at `9e02cb5`. All three are
**closed at `8e64f22`** -- `runner_claim_whose_only_caller_was_deleted_in_the_
same_round` and `runner_claim_with_a_wherever_it_runs_escape_clause` by the
`f7501ee` rewrite, and the third by `8945a4e` adding the assertion. **Not one
of them closed by a check; all three closed by a directive, and two of the
three closed into the new species this batch is about.** That is the number
and it is still not a good one.

**And the counterweight, because right-every-time is not allowed to become a
prior: fifty-seven rounds have found no element defect and this round found
none either.** `floatfea/` received no executable change for the thirteenth
round running -- 28 comment lines and nothing else. The ladder was green on
Linux on this exact code. Ladder 5 has still printed `OK -- 0 directories ran`
every time it has run, and V5.1 against CalculiX has still not spoken. R475
and R487 are the open questions about the element's gate and neither moved,
which is the right call with the boundary work unfinished.

## On the criterion, and on the one question you put to me

**The hook.** You asked whether `.claude/hooks/require-verdict.sh` must follow
DD1 in the same breath, and my answer is **yes, and it goes to Xabier as a
`process:` item, not as a HOLD.** DD1 wrote the rule and left the mechanism
reading the last line, and the text says which resolves the disagreement --
that is enough to get out of a deadlock by hand, which is what verdict 57 did.
It is not enough to stop the deadlock recurring: the next time a tree round
lands in a closed step's file, the hook refuses turns again and the exit is
again a hand-written verdict. One reader, two rules, and the cheaper one wins
until someone notices. **I am not proposing a mechanism and this is not
apparatus**; it is the observation that DD1 fixed the ruling and not the
refusal, said once.

**And one sentence about R517, which is mine as much as yours.** Three of the
four reds at this commit exist because the verdict file for step 6 has one
commit in it, and it has one commit in it because I wrote the first one. A
harness that depends on how many times the reviewer has written is a harness
whose green depends on the reviewer, which is the coupling DC0 and DD3 have
both been about. It is worth naming as a class rather than as a third
instance.

## Next step opens when

**F2-rung2 does not proceed past its present commit.** Step 6 is open; this is
its **second verdict**, and one more is available under CZ0, after which the
step closes and anything still blocking carries by name into the next step.

1. **`floatfea/tolerances.py` says what the tree does** (R514), site by site
   at `:363`, `:388`, `:394-403`. No value moves.
2. **The clearance test names its two quantities** (R515) -- one line, so that
   two tokens in `scripts/regen_figures.py` can no longer remove both brackets
   from the gate in silence.
3. **`test_the_Carried_table_is_what_the_generator_produces` is in the
   reporter allow-list** at `tests/test_report_guard_states.py:587-601`
   (R516), and the state is green with it as the nested run's only failure.
4. **`:414` does not index `[1]` unguarded, and an unbuildable state says so**
   (R517). A state that cannot be built is not a state that failed.
5. **A path with a separator that the repository does not have is still a
   site** (R518), at `tests/test_report_carried.py:2652`.
6. **`python -m pytest -q` is `0 failed` at the resulting commit, and
   `gh run list --commit <that sha>` is a completed SUCCESS.** The push that
   carries (1)-(5) touches `floatfea/`, `tests/` and `scripts/`, so
   `paths-ignore` will not skip it and no dispatch is needed. If the run is
   skipped anyway, dispatch one and say so.
7. **R475 is answered in the FIRST commit of F2-rung2**, unchanged and still
   blocking, with **R487** in the same commit. **R486 is out of F2 by DD0 and
   is not a condition here.** R504 is advice on how DB0 gets written, not a
   condition on it.
