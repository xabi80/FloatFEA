# Review — F2 step 7
Reviewed commit: d877c91005c9b7ef211c439f05f3c7dea95ea9b3
Verdict: HOLD
Tests: 2761 passed, 11 failed, 0 skipped   (my run at `0f26f03`, `python -m pytest -q`, 761.79s)

**Sixty-seventh verdict on F2; the fourth written into this file after step 7's closure
verdict (DD1), and it rules on one commit, `0f26f03`, and on nothing else.**

**STEP 7 IS AND STAYS CLOSED. F2 IS AND STAYS CLOSED. Verdict 63 at `2c48a4f` remains the
closure verdict and nothing here withdraws it.** No later step has been started:
`docs/milestones/F2.md:10` still reads `step-under-execution: 7` and the reports tree holds
only F2. This is the same post-closure tree loop as verdicts 64, 65 and 66.

**The invocation is IN ORDER and its three direct questions are answered here.**

1. **The four items: three answered, one answered in part.** R558 ANSWERED and measured.
   R556 ANSWERED. R555 ANSWERED at both halves I named, with a residual hole of the same
   class (R565). **R557 ANSWERED AT TWO OF ITS THREE SILENCERS** -- the third was
   relocated, not closed, and one `git rm` of four markdown files takes the backstop from
   red to green (R562).
2. **The ten remaining reds are ELEVEN, and none of them is a false red.** The eleventh is
   new, it is caused by this commit, and the five-file subset the commit message measured
   is the one subset that cannot see it (R561).
3. **R548's fix is correct in one anchor state of three and INVERTS THE RULE in the other
   two.** With the report tracked-and-modified or untracked, `assert distance == 1` rejects
   a count taken at the head and accepts a count one commit stale. Measured as a controlled
   pair both ways (R563). **That condition was mine and it was underspecified; the finding
   is not that the implementer misread it.**

```
cmd  git log --oneline b9a9859..HEAD
out  d877c91 corpus: batch 16 (mine, committed after this review's measurements)
     0f26f03 fix: the HOLD exit -- R555, R556, R557, R558, R548, C31, C32
     53c4908 review: F2 step 7 -- sixty-sixth verdict, HOLD @ 9682bcc
cmd  git diff b9a9859..0f26f03 -- floatfea/tolerances.py
out  (no output)
cmd  git diff b9a9859..0f26f03 -- floatfea
out  (no output)
cmd  git diff b9a9859..0f26f03 -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py      -- CI0: the pathspec resolves; the instruction is not broken
cmd  git diff b9a9859..0f26f03 -- .claude docs/SUPERVISOR.md
out  (no output)   -- my own instructions are untouched. NOT a STOP-class edit.
cmd  git diff b9a9859..0f26f03 -- .github
out  (no output)
cmd  git diff 0f26f03~1..0f26f03 --stat
out  scripts/write_verdict.py 28, tests/test_report_carried.py 52,
     tests/test_report_guard_states.py 67 -- no floatfea/
cmd  the same diff of scripts/write_verdict.py, filtered to added or removed lines
       matching "sys.exit", "def " or "import "
out  one line, and it is inside the docstring. That file is the reviewer's one
     sanctioned write path and no executable line of it moved.
cmd  python -m ruff check tests scripts ; python -m black --check tests scripts floatfea
out  All checks passed! ; 101 files would be left unchanged
     -- the two lint claims in the commit message hold at this commit
```

**CI, for the reviewed commit (CA2).**

```
cmd  gh run list --commit 0f26f0383f2ba221364013c6aa6b675ce83d44ac
       --json name,conclusion,workflowName,status
out  CI / CI   status=completed   conclusion=failure     (run 36349346875)
cmd  gh run view 36349346875 --json jobs
out  the verification ladder      SUCCESS   13 steps   20:48:05 -> 20:51:00
     lint, unit and guards        FAILURE   14 steps   20:48:06 -> 21:00:08 (12 min)
     CI determinism -- leg / ten legs agree   skipped, 0 steps
cmd  gh run view 36349346875 --log-failed, unique FAILED names
out  eleven names, identical to my local eleven
```

**Not CK2.** Twelve minutes over fourteen steps with real assertion text in the log: a real
red, and under CA2 a real red is (d). **The LADDER IS SUCCESS**, so no rung is red and
nothing above is uninterpretable -- HOLD, not STOP. The tree moved from 22 failures at
`b9a9859` to 11 at `0f26f03`.

**On 1b: there is no report, for the fourth consecutive commit that touches `tests/`.**
`docs/reports/F2/step-7.md` is unchanged since `36b5899` and still reads
`Answers: verdict 61 @ 52941f7`; `0f26f03` arrived with its triples in the commit message
and in the invocation. Applying 1b mechanically would HOLD a closed step over a report
nobody submitted, so I apply it as verdicts 65 and 66 did. **The cost is measured again
this round and it is the same cost: the commit message's one numeric claim about the suite
is short by one, and the guard that catches the miss was outside the subset it was measured
on.**

## Carried

From verdict 66 at `b9a9859`.

1. **R555 -- ANSWERED, at both halves the condition named, and a residual of the same
   class is R565.** The one filename is in the include list; the control can now fail on a
   top-level file.
   ```
   cell  ONE VARIABLE: remove that one filename from the include list at 0f26f03
   cmd   python -m pytest tests/test_report_carried.py -q -k pathspec_names_every
   out   1 failed -- it is named as executable content missing from the list.
         The negative control fires.
   ```
2. **R556 -- ANSWERED, and the withdrawn helper is reachable nowhere from the rule.**
   ```
   cmd   grep -rn "_changes_the_parse" --include=*.py .
   out   three lines: the definition, and the two controls that read it. The
         intruder helper no longer calls it.
   ```
   The consequence is real and I record it rather than complain about it: `c9a8736` and
   `303d203`, two commits I accepted as inert at verdict 65, are intruders again and are
   two of the five names in today's whole-suite failure. The rule is still satisfiable -- a
   report committed on top of the commit it names clears it -- so this is a cost, not R546.
   **It does put the code and DQ3's first ruling in disagreement**, and see the criterion
   section.
3. **R557 -- ANSWERED AT TWO OF THREE. Still open at the third; see R562.** Measured, one
   variable each, in a scratch clone at `0f26f03`:
   ```
   cell  bump `step-under-execution: 7` to `8`, nothing else
   out   BEFORE 1 failed -> AFTER 1 failed    (it PASSED before this commit) FIXED
   cell  set the marker to 1 and add a closure artifact for the next milestone
   out   1 failed                              FIXED -- it survives the boundary
   cell  git rm the four per-step closure artifacts, entries still untranscribed
   out   1 passed, and the rule reported no intruder for it   NOT FIXED
   ```
4. **R548 -- ANSWERED IN THE LETTER AT ITS ONE NAMED SITE, AND THE ANSWER INVERTS THE RULE
   IN TWO ANCHOR STATES.** See R563. The reviews-tree half of R548 is untouched and stays
   open; the corpus half stays checked-not-carried for the reason verdict 66 gave.
5. **R546 -- OPEN, WITH XABIER, AND CORRECTLY NOT ATTEMPTED.** The implementer did not
   argue with the measurement and did not act on it; no pathspec moved beyond the one
   filename. This is the criterion item, not a work item.
6. **R547 and R549 -- STILL OPEN.** The exemption of the documentation tree is the
   mechanism R562 now measures from the other side: it is what makes the closure-artifact
   deletion invisible to the whole-suite rule.
7. **Batch 13's five and batch 15's seven -- STILL UNTRANSCRIBED, and the direction of
   travel is now RIGHT while the count grew.** Twelve at `0f26f03`, twenty-one after my
   batch 16. The per-entry cost is gone (R558) and the backstop names them in one failure.
   **A reasoned refusal has a channel and it is not a new mechanism**: the
   requirement-changed table in the guard-states file exists to record a state whose
   required outcome changed, with the reason. The entry the implementer says needs a ruling
   can be built and recorded there; it does not need the ruling first.
8. **R550 -- still open, carried against F4.** `git diff b9a9859..HEAD --
   docs/verification/README.md` is empty, which is correct: the ladder is locked and DQ5
   is the route.
9. **R545 -- still open**, correctly not started.
10. **C30, C31, C32 -- C32 ANSWERED; C31's count is right and its line numbers are not.**
    C33 open at all three sites. C34 superseded. **C35 ANSWERED, by a different remedy
    than the one its condition named** -- the walk is still over the filesystem, with a
    git-ignore check and a hard skip of the build trees, rather than over tracked files.
    Measured: a gitignored build tree present with `git status --porcelain` empty gives
    `1 passed`; a new untracked tree is still named. The defect is gone and the named
    remedy was not taken, which under CLAUDE.md's site rule is a thing to state rather
    than to re-litigate. See the closure items.
11. **The DP3 counter condition -- carried unchanged.** It is a condition on F3 step 2,
    not on this commit; `floatfea/tolerances.py` is untouched, which is correct.

## Findings

**R561. (d) -- BLOCKING, NEW, AND CAUSED BY THIS COMMIT. The rename left a phantom
citation and the repository's own citation guard catches it.
`tests/test_report_guard_states.py:652`.**

```
cmd  python -m pytest -q, unique FAILED names
out  test_every_test_name_cited_in_prose_exists reds on the pair
     (tests/test_report_guard_states.py, the OLD test name)
out  "cites `test_every_reviewer_entry_is_BUILT_at_a_closure_commit` in prose and nothing
     by that name exists"
```

The test was renamed to one ending `_BUILT_before_a_step_CLOSES`; the sibling docstring at
`:652` still points at the old name. **The five-file subset the commit message measured
(`10 failed, 326 passed`) is the one subset that excludes the guard that catches the
commit's own edit**, which is why the tree has eleven failures and the message says ten.
One line. **Closed when** the citation names the test that exists.

---

**R562. (c) -- BLOCKING. R557's third silencer was relocated, not closed: the backstop's
precondition is still a set of files the constrained party writes, and deleting them is a
documentation commit the whole-suite rule exempts.
`tests/test_report_guard_states.py:695`, `:696`, `:697`.**

```
rule   the backstop asserts the awaiting-transcription set is empty once any step
       has closed
cell   ONE VARIABLE: one commit removing the four per-step closure artifacts, in a
       scratch clone at 0f26f03. No entry transcribed, no test code touched.
cmd    python -m pytest tests/test_report_guard_states.py -q -k BUILT_before_a_step
out    BEFORE: 1 failed, naming twelve untranscribed entries
out    AFTER:  1 passed in 0.01s
cmd    the rule's own intruder helper on that commit
out    []        -- the whole-suite rule is silent about it too
judge  HOLE. `if not closed: return` is the same early return as the single-path
       version it replaced, over a glob instead of one path.
```

**And nothing else in the repository requires those artifacts to exist.**

```
cmd  grep -rn "F2-step\|F\*-step" tests/ scripts/ --include=*.py
out  two lines, both inside this one test: its docstring and its own glob
```

So the four PASS verdicts recorded in the reviews tree would still record four closed steps
while the assertion about them did not run. **Closed when** the trigger is a file the
implementer cannot write. The form I named at R557 is still available and costs one line:
glob the reviews tree for a `Verdict: PASS` line -- the `PreToolUse` hook blocks the
implementer from that tree, which is the property the closure artifacts do not have. Break
it to check: delete the artifacts and confirm it still reds.

---

**R563. (c) -- BLOCKING, AND THIS IS THE ONE THAT MATTERS MOST. `assert distance == 1` is
correct in one of the three anchor states and requires a STALE count in the other two.
`tests/test_report_carried.py:2527`.**

The anchor helper has three live states and its own docstring names them: a sha when the
report is tracked and clean, the literal string `"HEAD"` when it is tracked and MODIFIED --
"HEAD is the commit it will sit on" -- and the reports-tree sha when it is UNTRACKED. The
distance the rule wants is one in the first state and **zero** in the other two, because in
those two the correct measurement is the one taken at the head itself.

```
rule   the whole-suite line names the commit the count was taken at, and that
       commit is the tree the report describes
cell   ONE VARIABLE: the sha in the report's whole-suite line. Scratch clone at
       0f26f03, report tracked and MODIFIED (not committed), nothing else moved.
cmd    python -m pytest tests/test_report_carried.py -q -k whole_suite_line_is_about
out    names HEAD    (0f26f03, the FRESH count) -> 1 failed:
       "names `0f26f03`, which is 0 commit(s) behind `HEAD`"
out    names HEAD~1  (53c4908, one commit STALE) -> 1 passed
cell   SAME VARIABLE, report UNTRACKED via git rm --cached, nothing else moved
out    names HEAD -> 1 failed, "0 commit(s) behind `36b5899`"
out    names HEAD~1 -> 1 passed
judge  INVERTED. In both states the fresh count reds and the stale count greens.
       And in the MODIFIED state the intruder half returns [] by early return, so
       this is the ONLY assertion covering that state.
```

**The old `<= 1` was loose and included the correct value; `== 1` excludes it.** This is the
guard-fails-false case in its worst form -- the assertion fires on the state whose claim is
true -- and it will bite on the first report written after this commit, because a report is
modified-or-untracked at the moment its count is taken.

**I own the shape of this.** R548 said `<= 1` must become `== 1` and named one line. It did
not distinguish the three anchor states, the implementer implemented it literally, and the
literal version is wrong. **Closed when** the threshold is per-state -- one where the anchor
is a sha, zero where it is the `"HEAD"` or reports-tree fallback -- with both directions
broken once and shown to red.

---

**R564. (c) -- BLOCKING. The whole-suite rule cannot see a report for the next milestone, so
F3 step 1's report cannot clear it and the rule is red from F3's first commit onward.
`tests/test_report_carried.py:69`, `:70`; `scripts/ci_section.py:100`, `:108`;
`tests/test_report_guard_states.py:80`.**

```
cell   ONE VARIABLE: commit a step-1 report for the next milestone with a
       whole-suite line naming HEAD, in a scratch clone at 0f26f03. Nothing else
       moved.
cmd    import the guard module and print its reports directory, its step and its
       report path
out    the directory is docs/reports/F2, the step is 7, and the report is
       docs/reports/F2/step-7.md
cmd    python -m pytest tests/test_report_carried.py -q -k whole_suite_line_is_about
out    1 failed -- "5 commit(s) touching code follow the report's own commit `36b5899`"
judge  The new report is invisible. The only tree state that clears this rule is one
       in which a CLOSED step's report is re-stamped and re-committed on top of the
       newest commit, at every commit, forever.
```

This is R546's unsatisfiability in its original form, re-earned at the milestone boundary,
and it is the same defect class R557's second silencer was: a path hardcoded to a milestone
that has closed. It predates `0f26f03`; I block on it here rather than in F3 step 1's first
round because **it is directly on the throughput path and it is one substitution in five
places.** **Closed when** the five sites read the milestone under execution instead of the
literal name, and a committed report for the next milestone is measured clearing the rule.

---

**R565. (c) -- BLOCKING. R555's repair reads top-level FILES from a four-name whitelist, so
the domain is still blind to every other one -- including a root `conftest.py`, which can
empty the collection. `tests/test_report_carried.py:2400`, `:2401`, `:2402`.**

```
rule   the include-list control must name anything a commit can touch that moves a
       suite outcome
cell   ONE VARIABLE: one commit adding a top-level conftest.py whose collection hook
       empties the item list, in a scratch clone at 0f26f03. Nothing else moved.
cmd    python -m pytest tests/test_report_carried.py -q -k pathspec_names_every
out    no tests ran in 0.24s        -- the conftest emptied the collection
cell   the SAME commit with a benign one-line conftest.py, plus a noxfile and a
       Makefile whose default target runs pytest
cmd    python -m pytest tests/test_report_carried.py -q -k pathspec_names_every
out    1 passed
cmd    the rule's own intruder helper on that commit
out    []
judge  HOLE, same class as R555. The branch adds a name only when it is one of four
       hardcoded filenames and otherwise skips the file.
```

A root `conftest.py` is the channel my own instructions single out (CH2 and CI0): everything
a gate reads is writable from a conftest. **Closed when** a top-level file that can move a
suite outcome cannot be silently outside the domain -- the cheap form is that any top-level
`.py`, and any tracked top-level file pytest or CI reads, must be named or explicitly
classed -- and the control is broken once on a file that is not the one already listed.

---

**R566. (d) -- the tree is RED at the reviewed commit: 11 failures, CI red, and ten of the
eleven are carried rather than new.**

```
cmd  python -m pytest -q 2>&1 | tail -40
out  11 failed, 2761 passed, 2 warnings in 761.79s
```

**Composition, and none of the eleven is a false red as a test outcome:**

* **1 -- the whole-suite-line rule.** TRUE: five code-touching commits follow the report's
  own commit and no report has been written. Two of the five named intruders cannot move a
  count; see carried item 2.
* **8 -- the guard-state cases**, `baseline` and seven step-number states. All eight have the
  SAME root cause: the nested guard run reads the stale suite line above. **`baseline` red
  means the harness has no valid control**, so the other seven carry no independent
  information until the first item is green.
* **1 -- the transcription backstop.** TRUE, and this one is the new backstop doing its job:
  twelve reviewer entries untranscribed with four steps closed. It is a work item, not a
  defect.
* **1 -- R561**, new and caused by this commit.

**What IS false here is not a red, it is three guard BEHAVIOURS, and they are R562, R563 and
R565.** The distinction is the whole of this verdict: the failures are honest and three of
the passes are not.

## Tolerances touched

**None.**

```
cmd  git diff b9a9859..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 0f26f03~1..0f26f03 -- floatfea
out  (no output)
```

No counter changed, no injection site changed, no golden file changed. **One threshold in a
gate assertion did change and it is not a tolerance**: `assert distance <= 1` became
`assert distance == 1`. It is a discrete commit count, not a numerical tolerance, it lives
in `tests/` by design, and it is R563.

## Closure items

Not blocking under CZ0. Not to be re-reviewed item by item. Fixed once, in the closure
commit. **C28, C29 and C33 from the previous two verdicts stand unchanged and are not
restated.**

- **C36. The repair of a false count wrote a third false figure, in the same docstring, in
  the same sentence shape. The count of four is now right and every line number cited is
  wrong.**
  ```
  cmd  grep -n "sys.exit" scripts/write_verdict.py
  out  18 (the cmd line itself), 63, 66, 68, 73
  out  the docstring names :53, :56, :58, :63 -- the pre-edit numbers, shifted by the
       ten lines the edit added, so the `out:` line "the four lines above" is refuted
       by the `cmd:` printed directly above it
  ```
  This is the third consecutive round in which the prose written *around* a fix inherits
  none of the discipline applied *to* it, which is CP2 verbatim. It is also a CW0 triple
  whose `cmd:` refutes its own `out:` at the commit that publishes it, and
  `tests/test_tree_prose_consistent.py` is green -- the pair has no `claim:` line, so
  nothing executes it. **Closed when** the line numbers are dropped and the grep is left as
  the source, which is what C31's second option said.
- **C37. C35 was closed by a remedy other than the one its condition named.** The walk is
  over the filesystem with a git-ignore call per file and a hard skip of the build trees;
  the condition said "the walk is over tracked files". The measured defect is gone. Recorded
  so that a later reader does not find the condition and think it was met literally.
- **C38. DQ3 exists nowhere in this repository.** A grep for it across `docs/` returns only
  this review file -- my own verdict. The ruling that authorises the entire relaxation of the
  whole-suite rule, and that two commits now implement, is not a locked decision anywhere:
  not in the plan's amendment table, not in the closure artifacts. **I have judged
  conformance to DQ3 from my own paraphrase of it**, which is the thing CLAUDE.md's working
  agreement exists to prevent. Closed when the ruling is written into the amendment table
  with the commit that entered it.
- **C39. The backstop's docstring claims more than was measured.** "There is nothing an
  implementer can write that makes the set empty except transcribing the entries" is true of
  the SET and false of the GATE, and the sentence above it -- "If any step anywhere has
  closed, every reviewer entry must be built" -- is refuted by R562's cell. Closed when the
  sentence states the trigger it actually has.

## Corpus

**`tests/corpus/report_guard_states.txt`, batch 16, committed separately at `d877c91`. Nine
entries, all nine unseen, plus two rulings on existing entries.**

**Coverage: the apparatus under review catches 2 of 9.** Seven are holes and each is a
finding above -- the root `conftest.py` and the top-level whitelist (R565), the closure
artifact deletion (R562), the three anchor-state rows (R563), and the next-milestone report
row (R564). The two that hold are the three-entries-with-no-build-action row, which is the
positive control for R558, and the emptied-parametrisation row, which does not read silently
green because `pyproject.toml` sets `empty_parameter_set_mark = "fail_at_collect"` -- one
more reason that file belongs inside the include list, which this commit put it in.

**R558 is verified by the corpus rather than by the implementer's count**, and this is the
measurement the previous verdict asked for:

```
cell  ONE VARIABLE: three corpus entries with no build action, appended in a scratch
      clone at 0f26f03. No test code touched.
cmd   python -m pytest tests/test_report_guard_states.py -q
out   9 failed, 18 passed   ->   9 failed, 18 passed
out   zero new reds for three entries, and the collected count did not move
cell  the same, nine entries, in the live tree at d877c91
cmd   python -m pytest tests/test_report_guard_states.py -q -k
        "corpus_and_the_states_agree or BUILT_before_a_step"
out   1 failed, 1 passed -- ONE failure naming twenty-one entries, not twenty-one
      failures
judge DQ3 RULING 2 IS IMPLEMENTED. A reviewer round no longer costs a red per entry.
```

**The measurement-protocol deviation is in its third round.** `baseline` is red, so no
whole-file outcome is attributable to the variable moved, and every row is measured as a
controlled pair on the named test plus the rule's own helpers in a scratch clone. The batch
header records the deviation. **This is the third consecutive verdict at which a corpus round
on this rule has not been available at the rule's own commit**, and R563 plus R564 are why it
will not be available at the next one either.

## On the criterion rather than on the work -- this goes to Xabier, and I say it once

**The post-closure tree loop has no verdict cap and it has now run four rounds.** CZ0 caps a
step at three verdicts precisely so that a loop cannot consume the schedule; this loop is not
a step, so the cap does not reach it, and verdicts 64, 65, 66 and 67 have all been about the
same guard apparatus. Each round has been correct and each round has produced the next one.
**That is a structural gap in CZ0, not a failure of any one verdict, and it is for Xabier to
close.**

**The single highest-value thing available is to retire the whole-suite-line rule.** Nine of
the eleven failures at `0f26f03` are that one rule and its nested harness. R563 and R564 are
both in it. R546's unsatisfiability was in it. `tests/test_collected_set_golden.py` already
exists, already compares the collected set against a golden, and already carries the property
the whole-suite line is a proxy for -- **it is the thing that caught R561 in this very diff.**
Retiring the line rule and letting the golden carry it would delete R563, R564, the first item
of R566 and its eight dependents in one commit. I am not asking for it; the F2a list is frozen
and this is a choice about a rule.

**And DQ3 and the code now disagree.** DQ3's first ruling, as I have it, is that a
comment-only edit must not redden this rule. `0f26f03` withdrew the exemption that delivered
that, for a reason I measured and stand behind, and two comment-only commits are intruders
again today. One of those two sentences has to give and it is not mine to choose. See C38: the
ruling is not written down anywhere, which is why this has to be asked rather than looked up.

## Next step opens when

**`0f26f03` is a real improvement and it is not accepted as it stands. Step 7 stays closed, F2
stays closed, verdict 63 at `2c48a4f` remains the closure verdict, and F3 step 1 does NOT
open** until the items below are answered. They are all (c) or (d), none needs new apparatus,
and none needs a plan change.

1. **R563 first.** The anchor-state threshold, broken once in each direction and shown to red.
   It is the item that makes the next report writable at all.
2. **R564.** The five hardcoded milestone sites, with a committed next-milestone report
   measured clearing the rule.
3. **R561.** One line, the phantom citation.
4. **R562.** The backstop trigger is a file the implementer cannot write, demonstrated by
   deleting the closure artifacts and confirming it still reds.
5. **R565.** A top-level file outside the four-name whitelist cannot be silently outside the
   domain, with the control broken on a file that is not the one already listed.
6. **The twenty-one corpus entries built, or each refused BY NAME through the
   requirement-changed table with its reason.** The backstop is red until this is done and that
   is the backstop working. No ruling is needed first; the refusal channel exists.
7. **Each of R546, R547, R548 and R549 answered site by site per CLAUDE.md**, including any
   site left and why. R548's reviews-tree half has now been carried through five verdicts
   untouched.
8. **R545 and R550 unchanged**, carried by name -- R545 before any F3 test parametrises G2.4
   over a platform member, R550 into F4 through DQ5, with **no step report citing G4.2 as a
   check on the mass matrix until the V4.2 row is re-specified**.
9. **The DP3 counter registered at a stated operating point and not injected on a rigid
   translation** -- the `2.7e-16` of `ma08` and `L/D = 15.612`, from verdict 65. A condition on
   F3 step 2.
10. **The commit that answers this carries a report.** Four in a row have not, and R561 is what
    that cost this round: a subset-measured count that missed the commit's own new red.

**On the schedule, because it is a requirement and nobody else is measuring it here.** Four of
the last five verdicts on this file have been consumed by the report-carry apparatus rather
than by the platform, and F3 step 1 has not started. **That is slippage against 5 and 10
October, it was reportable at verdict 66, and it is worse today.** The choice CLAUDE.md asks
for is stated rather than made: **slip the date, or reduce scope** -- and I add the third
option above, which is to retire one rule and recover nine of the eleven failures in a single
commit. Of the items here, R561 is one line, R562 and R564 are substitutions, and R563 is the
only one that needs thought.

**The FloatSim finding in the invocation is Xabier's and I have not measured it.** Recorded so
that it is in a document: the BEM solve completed at the pinned tag in 13191.1 s at 40.64 GB
peak resident against a documented estimate of about 42 minutes and 12.71 GB, and the timed
design-wave run was stopped by FloatSim's own restoring-PSD gate with 24 negative generalized
eigenvalues, so no per-run wall time exists for the twelve-against-two decision. **That is
upstream of this repository and CLAUDE.md makes it a conversation. It is not in scope for this
verdict and nothing here depends on it.**

**Not in this verdict and not reviewed here:** the work of step 7, DM0, DM2, DP1 through DP5,
DQ2, DQ4, DQ5, the `../HSP-stable` pin, and the design-wave load-case answer.
