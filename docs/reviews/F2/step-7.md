# Review — F2 step 7
Reviewed commit: 0a660cede5b9a7031508ad517bfb908a7f4e7983
Verdict: PASS
Tests: 2759 passed, 1 failed, 0 skipped   (my run at `0a660ce`, `python -m pytest -q`, 699.17s)

**Sixty-eighth verdict on F2; the fifth written into this file after step 7's closure
verdict (DD1). STEP 7 IS AND STAYS CLOSED. F2 IS AND STAYS CLOSED. Verdict 63 at
`2c48a4f` remains the closure verdict and nothing here withdraws it.** No later step has
been started: `docs/milestones/F2.md:10` still reads `step-under-execution: 7` and the
reports tree holds only F2. This verdict rules on four commits, `d877c91..HEAD`, and on
nothing else. It is NOT the engineering verdict -- DR1 defers that until DP2 and DQ4
land -- and it exists because the `Stop` hook requires a verdict when `tests/` moves,
which it should.

**WHY PASS ON A RED TREE, said once and plainly.** The tree IS red at `0a660ce` -- one
test, and CI agrees -- so by CZ0 (d) alone this is a HOLD. Two written rules collide and
one has to yield:

* CA2 / CZ0 (d): a red test or a red CI at the reviewed commit blocks.
* the `CLAUDE.md` three-verdict cap: after the third round a step closes, and a
  still-open blocking item **carries by name** into the next step rather than buying a
  fourth round. DR1 adds that post-closure verdicts count against the next step's cap.

This is the FIFTH post-closure round against a cap of THREE; the red is the same red
verdict 67 already ruled on (R566); it is measured BELOW where it was; and it is not
caused by anything in this diff. Holding again would also reproduce the exact deadlock
`CLAUDE.md` DD1 records: a HOLD on step 7 freezes DP2 and DQ4 at the hook, while DR1
withholds the next verdict until DP2 and DQ4 land, and the only exit is a hand-written
disposition. So I apply the cap, PASS the round, and **carry the red by name as a
blocking item.** It is not softened and it is not forgiven: `## Next step opens when`
states the condition, and green does not mean green in this repository until it clears.
The collision itself goes to Xabier under its own heading below.

## The one question: is the retirement clean or over-broad?

**CLEAN IN EXTENT. ONE ITEM WIDER THAN DR0'S REASON. AND THE LOSS STATEMENT IS
INCOMPLETE BY EXACTLY THAT ITEM.** Nothing was deleted that DR0 and DR1 did not
authorise, nothing survived that carries the retired rule, and no tolerance, no
`floatfea/` line and no conftest moved.

```
claim  six test functions and five helpers were deleted across the range, and they are
       the ones the invocation lists
cmd    git diff d877c91..HEAD -- tests | grep -E "^-\s*def "
out    _report_anchor, _implementer_commits_after, _changes_the_parse, _is_ignored,
       test_the_pathspec_names_every_executable_tree,
       test_a_COMMENT_ONLY_commit_is_exempt_and_a_CODE_commit_is_NOT,
       test_the_whole_suite_line_is_about_a_commit_that_exists,
       test_a_code_commit_after_the_report_reddens_and_a_corpus_commit_does_not,
       test_the_anchor_fallback_cannot_be_taken_in_this_repository,
       _older_ancestor, test_every_reviewer_entry_is_BUILT_before_a_step_CLOSES
       (plus two nested `def`s inside deleted bodies)
judge  the rule, its two controls, the two controls from the failed repair, four
       helpers, one build action, one state, and the backstop. That is the invocation's
       list with nothing extra and nothing missing.
```

```
claim  nothing outside the reviewer's own trees still names any deleted object
cmd    grep -rn <each of the fourteen names> .   (excluding .git and the reviews tree)
out    live code: NONE. Live prose: two dangling HELPER citations (R571).
       docs/closure/F2.md: one dangling TEST citation (R573). The step-5 and step-6
       reports: historical records, correct as records. tests/corpus/
       report_guard_states.txt: mine, and a record of what was measured.
```

```
claim  REVIEWER_TREES has exactly one remaining consumer and it is the site-check diff
cmd    grep -rn "REVIEWER_TREES" tests scripts .github
out    tests/test_report_carried.py:2154 (the definition), :2272 (the site-check
       `git diff` pathspec), :2255 (a COMMENT naming a deleted function -- R571)
judge  the claim holds for code. One comment beside it does not.
```

```
claim  the three kept tests are about the LINE'S CONTENT, not about commit distance
cmd    read tests/test_report_carried.py:2116-2130, :2205-2221, :2224-2232
out    WHOLE_SUITE_count: the line exists and `passed > 100`. RED_suite_is_named:
       every failure the line reports is named with a node id. CI_counts_not_all_zero:
       the CI table is not all zeros. None of the three reads git history.
judge  kept correctly. That judgement in the invocation is right.
```

**Where it goes wider than DR0's REASON, and this is the answer to question 2.** The
deleted test carried TWO assertions under one name. DR0's reason -- R546, R548, R563,
R564 -- is about the second only: the distance and the pathspec. The first was "a count
stamped with a sha nobody can check is a count": the sha must be an ancestor of `HEAD`.
That went with it, and the note at the site does not say so.

```
rule   (retired) the whole-suite line names a commit that is an ancestor of HEAD
cell   ONE VARIABLE: the newest revision's suite-line sha, set to `deadbee`, a commit
       that exists nowhere in this repository. Scratch worktree at 0a660ce, nothing
       else moved.
cmd    python -m pytest tests/test_report_carried.py -q
out    203 passed        -- identical to the unmutated tree
cmd    grep -rn "is-ancestor\|merge-base" tests scripts --include=*.py
out    tests/test_report_carried.py:364 (report vs verdict ordering),
       scripts/ci_section.py:527,:657 (CI run shas). Nothing reads the suite line.
judge  a fabricated sha in a published count is now invisible. That is a SECOND loss
       and it is not in the note.
```

**And the staleness loss is not hypothetical. It is already realised at this commit, in
the dangerous direction:**

```
claim  the newest published whole-suite figure is stale and wrong in the failed count
cmd    grep -n "Whole suite at" docs/reports/F2/step-7.md | tail -1
out    **Whole suite at `41a200c`: 2509 passed, 0 failed, 0 skipped.**
cmd    git rev-list --count 41a200c..HEAD
out    23
cmd    python -m pytest -q 2>&1 | tail -1
out    1 failed, 2759 passed in 699.17s
judge  the report publishes `0 failed` measured at a tree 23 commits behind a tree that
       is RED. Under the retired rule this was the red F2 closed with; it is now green
       and silent. That is the trade DR0 made, stated so nobody discovers it later.
```

**Deleting the backstop was within DR1 (question 3).** DR1 as recorded authorises it by
name and for the same reason the invocation gives:

```
cmd  sed -n '292,296p' docs/SUPERVISOR.md
out  "the backstop that asserted it zero at a step close is deleted, because it was
      failing *true* against a decision already taken. It returns when the freeze lifts."
cmd  git show --stat 0a660ce
out  docs/SUPERVISOR.md | 33 +++ -- one file, a standalone `process:` commit citing DR1
cmd  git diff d877c91..HEAD -- .claude docs/SUPERVISOR.md | grep -c "^-[^-]"
out  0        -- additive only. No guard removed from my own instructions. NOT a STOP.
```

The failing-true / failing-false distinction the invocation is least sure of does not
decide it: DR1 names this case explicitly. What is missing is not the deletion; it is
the ledger (R574) -- and the reason recorded at the site carries the wrong number (R570).

## Carried

Verdict 67's open items were R561, R562, R563, R564, R565 and R566. DR0 additionally
named R546 and R548.

* **R561 -- ANSWERED at `77d55c6`.** `cmd git show 77d55c6 -- tests/test_report_guard_states.py`;
  `out` the citation was corrected to
  `test_every_reviewer_entry_is_BUILT_before_a_step_CLOSES`, and `85541e1` then removed
  the name entirely with the test it named. The check is that the citation guard is green
  over the whole tree at `0a660ce`: no `test_*` name in prose under `tests/` or `scripts/`
  is dangling.
* **R562 -- CLOSED AS MOOT, but NOT for the reason the invocation gives.** It was a
  finding against the TRANSCRIPTION BACKSTOP (`tests/test_report_guard_states.py:695-697`
  at `0f26f03`), not against the retired rule's helpers; it closes under DR1's deletion,
  not under DR0. The distinction is load-bearing exactly once: DR1 says the backstop
  RETURNS when the freeze lifts, and R562's constraint must return with it -- the trigger
  must be a file the implementer cannot write, for example a `Verdict: PASS` line in the
  protected reviews tree, which is the property the closure artifacts do not have.
  Nothing in the repository records that constraint now. See R574.
* **R563 -- CLOSED with the rule.** Its site, the `assert distance == 1` at
  `tests/test_report_carried.py:2527` of that commit, no longer exists.
* **R564 -- CLOSED with the rule.** The `REPORTS`-is-F2 milestone trap dies with the
  anchor.
* **R565 -- CLOSED with the rule, and here the invocation's reasoning is right.** Its
  site was `test_the_pathspec_names_every_executable_tree`, one of the two controls of
  the retired rule; verified deleted in the `def` list above.
* **R546 and R548 -- CLOSED with the rule** (DR0 names both).
* **R566 -- STILL OPEN, reduced from eleven reds to one, CARRIED BY NAME as blocking
  into the next step.** Restated as R567 with the ablation.

## Findings

**R567. (d) -- BLOCKING, CARRIED. The tree is red at `0a660ce`, locally and in CI, and the
retirement did not cause it: it reduced it.
`tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]`.**

```
cmd  python -m pytest -q 2>&1 | tail -3
out  FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number]
     1 failed, 2759 passed, 2 warnings in 699.17s
cmd  gh api repos/xabi80/FloatFEA/actions/runs/36374615479/jobs
out  "lint, unit and guards"   failure -- runner "GitHub Actions 1000001366", 14 steps,
     11m46s: a run that EXECUTED, so this is not CK2's allowance state
     "the verification ladder" success -- no rung is red, so this is not a STOP
cmd  gh run view 36374615479 --log-failed | tail -5
out  1 failed, 963 passed -- the same single failure, the same assertion, on Linux. CI
     and my machine agree, so it is not platform-dependent.
```

```
claim  the red predates the retirement; the retirement removed eleven of twelve
cell   ONE VARIABLE: the commit. Same test, same machine. A worktree at 5bfdf3e --
       verdict 67 landed, retirement not yet made -- against 0a660ce.
cmd    python -m pytest tests/test_report_guard_states.py -q -k two_digit_step_number
out    at 5bfdf3e: 1 failed -- nested run 36 failed, 128 passed
out    at 0a660ce: 1 failed -- nested run 25 failed, 134 passed
judge  same assertion, same cause class, eleven fewer nested failures. The retirement is
       neither the cause nor an aggravation of it.
```

**The cause, measured rather than taken from the invocation. The invocation's reading is
RIGHT about the mechanism and INCOMPLETE about the consequence.**

```
claim  the nested run demands the NEWEST verdict while the outer run is held to the
       verdict the report CLAIMS to answer, so the state is red for the whole interval
       between any verdict and its answering report
cmd    grep -n "Answers: verdict" docs/reports/F2/step-7.md | tail -1
out    278:Answers: verdict 62 @ b52b370
cmd    the nested failure names, from the CI log above
out    test_the_report_carries_the_finding[R562] through [R566] -- verdict 67's findings
judge  the `Answers:` header rule -- my own instructions, item 1b -- is what makes "green
       mean green" at the outer level. The nested harness has no such rule, and this state
       COPIES the verdict to step 10, so the comparison lands on 67 and reds. It clears
       when a report revision answers the newest verdict, which is the invocation's
       reading and is correct, and it reds again at the NEXT verdict. It has now been red
       for five rounds.
```

**Closed when** a report revision answers the newest verdict and this state is green in CI
at that commit -- or, if that price is judged wrong, when the state is DELETED under DR1
with the reason at the site. Those are the only two DR1-compliant moves; a repair is a
guard edit and the freeze forbids it. I am naming the choice, not asking for one, and I
will not treat another round on this harness as available. **Do not repair it.**

**R568. (closure) The loss statement is incomplete by one item -- the sha-existence half.
`tests/test_report_carried.py:2190-2199`.** Measured under "The one question" above: a
fabricated sha gives `203 passed`. **Closed when** the note names both losses -- a stale
figure AND a sha that names nothing -- and `docs/milestones/F2a.md` carries the row.

**R569. (closure) "WHAT CARRIES THE PROPERTY NOW" is refuted by the same two cells.
`tests/test_report_carried.py:2185-2188`.** The collected-set golden records test NAMES;
the suite line is a COUNT and a SHA. They share no quantity.

```
cell   the two mutations above: the 23-commit-stale figure, and the fabricated sha
cmd    python -m pytest tests/test_collected_set_golden.py -q
out    green in both        -- it can see neither
claim  and it could not see this commit's own deletions either
cmd    git diff d877c91..HEAD -- tests/goldens/collected_tests.txt | grep -c "^-tests/"
out    3        -- while six test functions were deleted
cmd    git log --all -S the backstop's name -- tests/goldens/collected_tests.txt
out    (no output)   -- three of the six were added after the previous regen, and the
       golden is one-directional by design, so it never recorded them
judge  the golden is a good guard for the defect it was written for. It carries none of
       the retired rule's property, and it cannot be used to enumerate deletions -- the
       `def` diff is what I had to use above.
```

**Closed when** the sentence is reduced to what was measured: nothing carries the retired
property, and the golden carries a different one.

**R570. (closure) "it was true -- twelve are unbuilt" is 22 at the commit that publishes
it. `tests/test_report_guard_states.py:616-624`.** CP2's species exactly: the number sits
in the prose written AROUND the fix.

```
cmd  python -m pytest tests/test_report_guard_states.py -q -s -k corpus_and_the_states
out  22 entries awaiting transcription
cmd  the same module imported at 5bfdf3e
out  46 entries, 25 built, 21 awaiting
judge  twelve was verdict 67's figure, taken before my batch 16 (nine entries) and before
       this commit's own state deletion (one). 12 + 9 + 1 = 22. Correct when taken, wrong
       when published, which is BI3's shape inside a comment.
```

**R571. (closure) Two dangling HELPER citations, which the citation guard cannot see
because it reads `test_*` names only.**

* `tests/test_report_guard_states.py:271` -- "`_older_ancestor` below is what that state
  uses instead. This function stays because..." -- and `_older_ancestor` is deleted twenty
  lines below it, in the same commit.
* `tests/test_report_carried.py:2255` -- "`_implementer_commits_after()` excludes
  `REVIEWER_TREES` and explains why" -- present tense, and both the function and the
  explanation are gone. The measured cell beside it, 126 failed to 125, survives, so the
  substance of DD3 and R511 is not lost; only the pointer is.

**This is the answer to "is the citation guard the right replacement".** It is a good
guard; it caught three of the implementer's own dangling names inside the commit that
named it; that is worth the line and I agree with it. It is NOT a replacement for the
retired rule -- a different property entirely -- and its reach is exactly where this
retirement left two dangling pointers. **Closed when** both sentences say what is true.

**R572. (closure) Dead code: `_last_commit_touching` at
`tests/test_report_carried.py:2133` has no caller.** `cmd grep -rn "_last_commit_touching"
tests scripts`; `out` one line, the definition. It outlived `_report_anchor` and
`test_the_anchor_fallback_cannot_be_taken_in_this_repository`, its only two consumers.
**Closed when** it is deleted or a caller exists.

**R573. (closure, and the one a later reader meets first) `docs/closure/F2.md:206-214` now
misattributes the red CI job and publishes a `cmd` that collects nothing.** Section 3 says
the nested cause of the red `lint, unit and guards` job is
`test_the_whole_suite_line_is_about_a_commit_that_exists`, gives the command to reproduce
it, and quotes the retired rule on its `rule` line. At `0a660ce` that test does not exist
and the red is `two_digit_step_number`. BP0 is explicit: when a decision rule changes,
every figure citing it is regenerated or withdrawn in the same commit. **Closed when**
section 3 states the red as it is at the current head, or records that its account is as
of `2c48a4f` and names what the red is now.

**R574. (closure) `docs/milestones/F2a.md` carries no row for anything DR1 defers, so the
freeze has no ledger.** `cmd grep -n "batch 15" docs/milestones/F2a.md`, and the same for
"backstop", "whole-suite", "untranscribed", "DR0" and "DR1"; `out` (no output) for every
one of the six. Three rows are needed: (i) the 22 untranscribed reviewer entries, batches
15 and 16, with the corpus-agreement test named as the reporter; (ii) the transcription
backstop's return, carrying R562's constraint; (iii) the suite-line existence check from
R568. **Closed when** the three rows exist. A freeze without a ledger is a deletion.

**R575. (closure) `scripts/run_floatsim_design_waves.py:22-27` gives an incomplete reason
for skipping heading 45, and the constraint that actually binds is the expensive one.** The
hardcoded-argument claim is TRUE: the pilot study script in the pinned HSP worktree
constructs its wave at heading zero, at line 262. But lines 25-31 of that same file record
that `platform12_bem.nc` was solved at heading 0 ONLY, and that the other case needs the
BEM re-solved at about 190 minutes. A heading parameter alone does not buy heading 45; a
database does. **Closed when** the docstring says which constraint binds. Recorded because
DQ0's scope depends on it, not because of the prose.

**Not a finding, recorded so it is not re-litigated:** `290ffbd` adds a script, not
apparatus. It is not a guard, scanner, meta-test, detector or report generator, so DR1 does
not reach it, and its refusal to run in the production worktree plus the `git hash-object`
check is the right shape for the incident it follows.

## Closure items

R568, R569, R570, R571, R572, R573, R574, R575. Eight: prose, dead code, a stale artifact
section and a ledger row. None of them is (a), (b) or (c). Fix them once in one closure
commit and do not re-review them item by item. **R574 is the one I would not let slide
into F3** -- it is what makes the freeze reversible rather than a deletion.

## Tolerances touched

**None.**

```
cmd  git diff d877c91..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff d877c91..HEAD -- floatfea
out  (no output)
cmd  git diff d877c91..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        -- CI0: the pathspec resolves; the instruction is not broken
cmd  git diff d877c91..HEAD -- .github
out  (no output)
cmd  git show --stat for each of the four commits
out  77d55c6 and 85541e1 touch tests/ only; 290ffbd touches docs/ and scripts/ only;
     0a660ce touches docs/SUPERVISOR.md alone. No commit touches both the reviews tree and
     tests/ or floatfea/, and the one commit that edits my own instructions is standalone
     and cites its directive.
```

## Corpus this round

**No new entries, deliberately, and the reason is written down rather than left as an
omission.** DE2 forbids new corpus files for apparatus species and freezes the existing
apparatus corpora as a list; DR1 sends batch 15 and later apparatus entries to
`docs/milestones/F2a.md` untranscribed. This diff touches no element, no gate on a physical
quantity and no platform model, so an element batch taken here would measure nothing about
it. **The element batch is deferred to the DP2/DQ4 verdict, where it can be measured
against the new mode pairing instead of the old one.**

**The standing measurement, which is the only number that says whether any of this works:**
46 corpus entries, 24 built, **22 unbuilt** -- twelve from before verdict 67, nine from
batch 16, and one created by this commit's own state deletion. New entries put in front of
the implementer's checks this round: **zero, so no coverage was measured.** That is a gap in
this round's record, not a clean bill.

## A criterion collision, once, for Xabier and not for another round

**CA2 -- a red CI is a HOLD -- and the three-verdict cap cannot both be obeyed in a
post-closure tree loop, and this is the fifth round where they meet.** The red is a
process-harness state whose green depends on a condition outside itself: a report answering
the newest verdict. So CI is red for the whole interval between any verdict and its
answering report. Obeying CA2 there means the gate is red by construction during exactly the
interval it exists to cover -- the same defect the `Answers:` header rule was introduced to
fix at the outer level -- and obeying the cap means a reviewer writes PASS on a red tree,
which is what CA2 exists to prevent. I resolved it by the cap, with the item carried by
name, and I think that is right for THIS round only: the red is pre-existing, measured,
falling, and fully attributed. **It is not a precedent I can keep applying.** One of two
things should be decided above me -- either the nested harness gets the `Answers:` rule the
outer level has, which is a guard edit and therefore post-freeze, or the state is deleted
now under DR1 and the property goes on the frozen list. Either is cheap. Doing neither means
the next verdict inherits the same collision with one more round of precedent behind it.

## Next step opens when

Step 7 is closed and stays closed. Nothing here reopens it, and nothing here gates DP2 or
DQ4.

1. **R567 is BLOCKING and carried by name.** The post-DP2/DQ4 report carries it in its
   `Carried` section and either shows
   `test_the_guard_survives_the_state[two_digit_step_number]` green in CI at its own commit
   -- which a revision answering the newest verdict should produce on its own -- or records
   that the state was deleted under DR1 with the reason at the site. Repairing it is refused
   by the freeze.
2. **The eight closure items land in one commit**, R574 included, and are not re-reviewed
   individually.
3. **The next verdict is requested after DP2 and DQ4 land** (DR1): not per commit and not
   per directive. Under DR1 this verdict counts against that step's cap, so two rounds
   remain before the cap closes it. Spend them on the element.
4. **`Answers: verdict 68 @ 0a660ce`** is the header the next report carries. This is the
   latest verdict as of this commit.
