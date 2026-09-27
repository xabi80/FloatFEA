# Review — F2 step 7
Reviewed commit: b9a985999972a4738671a66e9cd8dcc1585a6dfb
Verdict: HOLD
Tests: 2762 passed, 15 failed, 0 skipped   (my run at `9682bcc`, `python -m pytest -q`, 750.49s)

**Sixty-sixth verdict on F2; the third written into this file after step 7's closure
verdict (DD1), and it rules on one commit, `9682bcc`, and on nothing else.**

**STEP 7 IS AND STAYS CLOSED. F2 IS AND STAYS CLOSED. Verdict 63 at `2c48a4f` remains
the closure verdict and nothing here withdraws it.** The three-verdicts-per-step cap is
not in play: this is not a fourth round on step 7's *work*, it is the same
post-closure tree loop verdicts 64 and 65 ran, and the reason it exists is that
`9682bcc` changed `tests/` after a verdict. The `Stop` hook is right to refuse.

**The HOLD is on the TREE, not on step 7's work, and the exit exists.** No later step
has been started -- `docs/milestones/F2.md:10` still reads `step-under-execution: 7`
and F3 step 1 has no commits -- so the DD1 deadlock (a verdict on step 7 that cannot
clear a step-6 report) cannot form here. The exit is: fix the four blocking items in
`tests/`, re-invoke, and a PASS-on-the-tree verdict is written into this file.

**The direct answer to the invocation's two questions.**

1. **YES. `9682bcc` relaxes more than DQ3 ruled, in three separate ways, each
   measured.** `pyproject.toml` is exempt and is neither `docs/` nor `CLAUDE.md`
   (R555). The `_changes_the_parse` exemption rests on a premise this repository
   refutes -- a comment-only commit under `floatfea/` turns the suite into a
   collection error (R556). And the BE3 backstop, which is the whole of what makes
   ruling 2 safe, is disarmed by a one-line edit to a document the same commit just
   exempted (R557).
2. **YES, `pyproject.toml`'s absence is a hole and it carries.** It is the largest one
   measured here: `2777` collected becomes `88`, and the rule reports no intruder.

**And one thing that is worse than a hole: ruling 2 is NOT IMPLEMENTED (R558).** An
untranscribed reviewer entry still reddens CI, one failure per entry. My own corpus
batch this round took the tree from 15 failures to 22 -- seven entries, seven new
reds -- which is exactly the coupling BE3 was ruled to break.

```
cmd  git log --oneline e663a88..HEAD
out  9682bcc process: R546, BE3 and write_verdict.py -- three rulings (DQ3)
     303d203 docs: the blind subspace is {c3 = 0}, not the rigid subspace
     (303d203 was reviewed at verdict 65; 9682bcc is the only commit ruled on here)
cmd  git diff e663a88..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff e663a88..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py      -- CI0: the pathspec resolves; the instruction is not broken
cmd  git diff e663a88..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)   -- my own instructions are untouched. NOT a STOP-class edit.
cmd  git diff 9682bcc~1..9682bcc --stat
out  scripts/write_verdict.py 20+, tests/test_report_carried.py 172+,
     tests/test_report_guard_states.py 60+  -- no floatfea/, and the process: commit
     is standalone as CLAUDE.md requires
```

## Carried

From verdict 65 at `e663a88`. **Five of six are untouched by `9682bcc`; the sixth is
answered in form and reintroduced in substance.**

1. **R546 -- ATTEMPTED, NOT ANSWERED.** This is the commit under review and it is the
   subject of R555, R556 and R557. The condition verdict 65 set -- `pytest -q` at
   `0 failed` at one commit -- is still unmet (15 failures at `9682bcc`, 22 at
   `b9a9859`), and the rule that was unsatisfiable is now satisfiable by four commit
   shapes that move the suite count. **Still open.**
2. **R547 -- ANSWERED IN PART.** The comment-only and `process:` halves are now
   exempt, which is what R547 asked for. The `docs/closure/**` half is exempt too and
   that is the one I can now show is wrong by measurement rather than by argument
   (R557, and the corpus ruling in batch 15). **Still open, narrowed.**
3. **R548 -- STILL OPEN, BOTH HALVES, AND NEITHER WAS TOUCHED.**
   ```
   cmd  sed -n '2489p' tests/test_report_carried.py
   out  assert distance <= 1,
   ```
   **Distance zero is still accepted.** The invocation asks and this is the answer:
   it was never rejected, `9682bcc` did not change it, and `0 <= 1` is the whole
   measurement. `git diff 9682bcc~1..9682bcc -- tests/test_report_carried.py` touches
   `_implementer_commits_after`, `_changes_the_parse` and two new tests, and not that
   line. The reviewer-tree half is also unchanged -- **and for `tests/corpus` I now
   record it as checked rather than carried: `git ls-files tests/corpus | grep -c
   '\.py$'` is `0`, the tree is data-only, and the `PreToolUse` hook blocks the
   implementer from writing it, so the exemption is sound for a reason the file does
   not give.** The `docs/reviews` half stands as R548 wrote it.
4. **R549 -- still open**, closed by R547.
5. **R545 -- still open**, correctly not started.
6. **Batch 13's five states -- STILL OPEN, and the direction of travel is wrong.**
   None was built. The claim that they "now produce one named work item" is false:
   they produce five `KeyError`s plus one named work item. See R558.
7. **R550 -- still open and unchanged**, carried against F4. **`git diff
   e663a88..HEAD -- docs/verification/README.md` is empty**, so V4.2's row is
   untouched, which is correct: the ladder is a locked document and DQ5 is the route.
   Note for the record that naming those sites has a cost I created: the nested
   `two_digit_step_number` state now reds on
   `test_every_named_site_is_touched_or_declared[R550-docs/verification/README.md:105]`
   and two siblings, and the only thing that clears them is F3 step 1's report saying
   `no change` beside each site by name.
8. **C28, C29, C30 (closure items from verdict 65)** -- C28 and C29 untouched, which
   is correct; they belong to the closure commit. **C30 was answered and a new
   instance of the same defect was written in its place.** See the closure items.

**On 1b: there is no report to check.** `docs/reports/F2/step-7.md` is unchanged since
`36b5899` and still reads `Answers: verdict 61 @ 52941f7`; `9682bcc` arrived with no
report at all, its triples in the invocation instead. As at verdict 65, applying 1b
mechanically here would HOLD a closed step over a report nobody submitted. **But this
is now the third consecutive `tests/`-or-`floatfea/`-touching commit to arrive with no
report, and the invocation's own prose is the only place the numbers live.** One of the
four numbers in it is wrong at the commit it describes (C34). That is the cost of the
arrangement, stated once.

## Findings

**R555. (c) -- BLOCKING. `pyproject.toml` is exempt from the whole-suite rule, and a
commit touching only it moves the collected count from 2777 to 88.
`tests/test_report_carried.py:2230` and `:2369-2377`.**

```
rule   _implementer_commits_after(anchor) must be non-empty for a commit that
       makes the report's whole-suite count stale
cell   ONE VARIABLE: one commit, pyproject.toml only, in a scratch clone at 9682bcc.
       testpaths ["tests"] -> ["tests/unit"], xfail_strict true -> false.
       Nothing else moved.
cmd    python -m pytest --collect-only -q   before and after
out    2777 tests collected  ->  88 tests collected
cmd    _implementer_commits_after("HEAD~1") and _changes_the_parse(HEAD), imported
       from the clone's own tests/test_report_carried.py
out    []      and    False
judge  HOLE. The rule is silent about a commit that deleted 2689 tests from the
       suite the report's count describes.
```

**The proximate cause is that the guard meant to keep the include list honest cannot
see files.** `test_the_pathspec_names_every_executable_tree` iterates
`ROOT.iterdir()` and skips everything that is `not entry.is_dir()`, so no
top-level file can ever be named by it -- `pyproject.toml`, `CLAUDE.md`, `PLAN.md`,
`WORKFLOW.md`, `.gitignore`. An include list guarded by a check blind to half the
things it must include is not guarded.

**And the same commit contains the counter-evidence, thirty lines from the list.**
`tests/test_report_guard_states.py:351` enumerates what a nested pytest run needs
copied into a work tree:

```
cmd  sed -n '351p' tests/test_report_guard_states.py
out  for rel in (".git", "tests", "docs", "floatfea", "scripts", "pyproject.toml"):
```

**`docs` and `pyproject.toml` are both there, because without them the nested suite
does not reproduce.** Two files in the same guard family give two different answers to
"what can change a suite outcome", and the one written this commit is the narrower.

**Closed when** `pyproject.toml` is inside the rule's domain, *and*
`test_the_pathspec_names_every_executable_tree` can fail on a top-level file that is
missing from the list -- break it by removing one entry and confirm it reds. A guard
that cannot see the class of thing it checks is the "gate carries its own failure"
defect, not a gap in a list.

---

**R556. (c) -- BLOCKING. `_changes_the_parse` exempts a commit class that this
repository has three tests reading as data. `tests/test_report_carried.py:2296-2318`
says a comment-only edit under `floatfea/` "cannot move a suite count". It can, and
the result is a collection error, not a changed number.**

```
rule   _changes_the_parse(sha) is False only for a commit that cannot change a test
       outcome -- the docstring's own words
cell   ONE VARIABLE: one commit appending ONE hash-comment line to
       floatfea/element/beam.py, `# claim: this probe comment asserts something
       about the repository`, with no `cmd:` after it. Parse identical; nothing
       else moved.
cmd    _changes_the_parse(HEAD) ; _implementer_commits_after("HEAD~1")
out    False ; []          -- exempt
cmd    python -m pytest tests/test_tree_prose_consistent.py -q   before and after
out    30 passed  ->  AssertionError: floatfea/element/beam.py:369 opens `claim:`
       and no `cmd:` follows it ;  1 error in 0.45s, Interrupted: 1 error during
       collection
judge  HOLE, and the worst-shaped one available: the state the rule calls inert is a
       state in which NOTHING RUNS. The corpus header at
       tests/corpus/report_guard_states.txt:43 already rules that a collection error
       is never an agreement with any expected outcome.
```

**Comments in this tree are executable content, and this was knowable by reading.**
`tests/test_tree_prose_consistent.py:99` scans `ROOTS = ("floatfea", "tests",
"scripts", "docs/milestones", "docs/verification")` and `:100`
`EXTRA_FILES = ("CLAUDE.md",)` for claim/cmd/out triples, which live in
comments by construction -- CW0 requires it. `tests/test_plan_figures.py:52` sweeps
`("floatfea", "tests", "scripts", "docs")` for figure names in `.py`, `.md` and `.sh`.
`tests/test_no_tolerance_literals.py:92` reads `tokenize.COMMENT` tokens for the
`not-a-tolerance:` exemption. **The AST is the wrong invariant for this repository**,
because CW0 deliberately made comments load-bearing.

**One honest negative, recorded because I measured it and it did not fire.** I also
deleted the `not-a-tolerance:` marker line at
`tests/test_counters_are_injected.py:64` as a second instance of the same class:
`_changes_the_parse` returned `False` and `tests/test_no_tolerance_literals.py` stayed
`50 passed`. That channel did not redden. The `beam.py` one did, and one measured
counter-example is what the claim needs to be false.

**What `c9a8736` and `303d203` prove, precisely.** They are two commits that happened
to be inert. `test_a_COMMENT_ONLY_commit_is_exempt_and_a_CODE_commit_is_NOT` asserts a
property of those two shas, not of the class, and the docstring generalises from them.

**Closed when** the exemption stops applying to a file whose comments a shipped test
reads -- measured, by naming the readers above, not asserted -- or the docstring's
claim is reduced to what was measured ("these two commits are inert") and the rule's
promise is restated to match. **DQ3 ruled that comment-only edits must not redden the
rule. It did not rule that a comment-only edit which reddens the SUITE must be exempt,
and those are different sentences.**

---

**R557. (c) -- BLOCKING. The BE3 backstop is disarmed by one line in a document, and
that line is exempt from the rule that would notice it.
`tests/test_report_guard_states.py:664-690`.**

The safety of ruling 2 rests entirely on "each step closure commit asserts N = 0". The
assertion is conditional on `docs/closure/F2-step{STEP}.md` existing, and `STEP` is read
from a regex over `docs/milestones/F2.md`.

```
rule   test_every_reviewer_entry_is_BUILT_at_a_closure_commit asserts
       AWAITING_TRANSCRIPTION is empty once the step has closed
cell   ONE VARIABLE: one commit changing the marker step-under-execution: 7 to
       8 in docs/milestones/F2.md. Nothing else moved; no entry transcribed.
cmd    python -m pytest tests/test_report_guard_states.py -q -k
         every_reviewer_entry_is_BUILT
out    BEFORE: 1 failed -- assert not [the five batch-13 names, listed verbatim in
       the CI log of run 36345404842]
out    AFTER:  1 passed in 0.01s
cmd    _implementer_commits_after(HEAD~1) on that same commit
out    []      -- and the rule that reads suite counts is silent about it too
judge  HOLE. One line in a document takes the backstop from red to green with all
       five reviewer shapes still unbuilt, and the commit that does it is exempt.
```

**There is a second silencer and it is structural rather than adversarial.** The path
is hardcoded `F2-step{STEP}.md` while `STEP` comes from `docs/milestones/F2.md`, a
frozen file for a closed milestone. Every F3 step will look for an F2 artifact. The
backstop is live today only because that marker still reads 7 -- it does not survive
the milestone boundary, which is where carried items are lost.

**Third: a gate whose precondition is a file the constrained party writes.** The body
returns early when the closure artifact is absent. Closing a step without writing the
per-step artifact is enough, and nothing asserts the artifact exists.

**Closed when** the assertion trigger is not a document the implementer edits in a
commit the whole-suite rule exempts. Two forms satisfy DQ3 without a new mechanism:
assert whenever a closure artifact exists for **any** step whose review file carries a
PASS, or assert unconditionally and let the report carry N -- the ruling says the
count is reported, and reporting it does not require the assertion to be skippable.
**Ask of it what CLAUDE.md asks of every gate: if the thing it claims were false,
would this go red? Today: only while one integer in one markdown file holds still.**

---

**R558. (c) -- BLOCKING, and this is the one I would fix first. Ruling 2 of DQ3 is NOT
IMPLEMENTED. An untranscribed reviewer entry still reddens CI, one failure per entry.
`tests/test_report_guard_states.py:693` with `:359`.**

```
cmd  sed -n 359p and sed -n 693p on tests/test_report_guard_states.py
out  359:     for action, arg in STATES[state]:
     693: @pytest.mark.parametrize("state, require", ENTRIES, ids=...)
```

`ENTRIES` is the corpus. `STATES` is what is built. An entry in the first and not the
second raises `KeyError` inside `_build`, before any assertion runs.
`test_the_corpus_and_the_states_agree` was softened; the thing that actually failed was
not.

```
rule   DQ3 ruling 2: an untranscribed reviewer corpus entry stops failing CI
out    AT 9682bcc, failures attributable to untranscribed entries: 5 KeyErrors in
       test_the_guard_survives_the_state cases plus 1 named work item = 6
out    AT e663a88, the same count was 5 KeyErrors plus
       test_the_corpus_and_the_states_agree = 6      (verdict 65, R553)
cell   ONE VARIABLE: my corpus batch 15, seven entries, committed at b9a9859.
       No test code changed.
cmd    python -m pytest tests/test_report_guard_states.py -q
out    14 failed -> 21 failed. Seven entries, seven new reds, one per entry.
judge  NOT IMPLEMENTED. The count is unchanged at six and the coupling is intact:
       a reviewer round still costs a red build, one for one.
```

**This is the finding the invocation asked me to look for and it points the other
way.** I was asked whether the relaxation lets a reviewer finding be ignored. The
measurement says the relaxation did not happen: "the suite is green" and "the reviewer
has stopped finding shapes" are still the same statement, and my batch 15 above is
seven more reds on a tree that is already red. **That is a bad trade for the one
number in this process that says whether any of it works.**

**Closed when** a corpus entry with no build action produces no failure -- parametrise
over the built intersection, or make the unbuilt path report -- and the count is
asserted by the repaired backstop of R557 and nowhere else. Break it to check: add one
entry, confirm the delta is zero failures.

---

**R559. (d) -- the tree is RED at the reviewed commit. 15 failures, CI red, carried
rather than new.**

```
cmd  python -m pytest -q 2>&1 | tail -40
out  15 failed, 2762 passed, 2 warnings in 750.49s
cmd  gh run list --commit 9682bcc37ed708625020fb0ee2e1ff0c776b754e --json name,
       conclusion,workflowName,status
out  CI / CI   status=completed   conclusion=failure     (run 36345404842)
cmd  gh run view 36345404842 --json jobs
out  lint, unit and guards     FAILURE   14 steps, 19:43:38 -> 19:54:20 (11 min)
     the verification ladder   SUCCESS   13 steps
     CI determinism -- leg / ten legs   skipped, 0 steps
cmd  gh run view 36345404842 --log-failed
out  the same fifteen, same roots, same messages as my local run
```

**Not CK2.** The job ran eleven minutes over fourteen steps with real assertions in the
log; it is a real red and under CA2 a real red is (d). **The LADDER IS SUCCESS**, so no
rung is red and nothing above is uninterpretable -- this is a HOLD, not a STOP.

**Composition, the same fifteen as at `e663a88` with one substitution:**
`test_the_whole_suite_line_is_about_a_commit_that_exists` (the genuine stale line, now
naming **two** commits, not one -- see C34), `baseline` and eight inherited states, the
five untranscribed entries, and
`test_every_reviewer_entry_is_BUILT_at_a_closure_commit` in place of
`test_the_corpus_and_the_states_agree`. **Both new tests pass**, locally and on CI.

---

**R560. Checked and NOT a hole -- recorded because the invocation asked, and because a
negative result measured is worth more than a suspicion carried.**

* **Merge commits.** `git show --name-only --format=` prints nothing for a merge
  TREESAME to a parent, so `_changes_the_parse` returns False for the merge itself --
  but git history simplification reports the *side* commit instead, and that one is
  caught. Measured: `_implementer_commits_after(9682bcc)` on a no-ff merge of a branch
  editing `floatfea/tolerances.py` returned the side commit
  `4cf55ba a real code change on a side branch`. **An evil merge is also caught**:
  amended to add a line present in neither parent, git show falls back to the
  conflicted-file list, `_changes_the_parse` returned True, and both the merge and the
  side commit were reported. Both are corpus entries in batch 15. History here is
  rebase-then-ff-only, so this was the cheap check, not the likely one.
* **A commit that reverts and re-applies within itself** is correctly exempt: the net
  parse is unchanged and the net suite outcome is too. Not a hole.
* **Python files under `tests/corpus` are skipped for the right reason**, which I
  checked rather than accepted: `git ls-files tests/corpus` matches zero names ending
  in .py, the header declares the file test data only, and the PreToolUse hook blocks
  the implementer from that tree. The *reason given in the docstring* is the R361
  collected-count one, which is true and is why the exemption is necessary; the reason
  it is **safe** is the hook, and the file does not say so.
* **A shallow clone would make the new control vacuous** -- it skips when the sha is
  absent -- but it cannot happen here: all three `actions/checkout@v4` steps in
  `.github/workflows/ci.yml` carry fetch-depth 0, at lines 97, 355 and 467, for exactly
  this reason (CC3).
* **`artifacts/` -- the classification survives, and by a route the check in the
  invocation did not cover.** `grep -rn artifacts tests scripts floatfea` does not read
  `.github/`, and `.github/` is in `EXECUTABLE_PATHS` precisely because CI content moves
  outcomes; if a workflow ran a script from `artifacts/`, the tree would be
  CI-executable. It does not: `grep -rn artifacts .github/ scripts/ docs/verification/`
  returns one prose mention at `scripts/ci_section.py:351`. The other route is a
  repo-wide sweep, and every sweep is rooted: `tests/test_collected_set_golden.py:206`
  at tests and scripts, `tests/test_plan_figures.py:52` at floatfea, tests, scripts and
  docs, `tests/test_no_tolerance_literals.py:630` at TESTS, and every globbing triple in
  the tree is over `tests/**/*.py`. **`artifacts/` is reachable by none of them.** The
  classification is right; the evidence given for it was incomplete.

## On the criterion rather than on the work -- this goes to Xabier, and I say it once

**Ruling 1 of DQ3 rests on a premise this repository refutes, and I am not treating that
as a HOLD because the premise is for Xabier to re-make, not for me to overrule.** The
ruling is that `docs/` and `CLAUDE.md` are exempt by pathspec because they cannot move a
suite count. Measured at `9682bcc`:

```
cell   ONE VARIABLE: one commit adding docs/closure/F3-step1.md, nothing else
cmd    python -m pytest --collect-only -q   before and after
out    2777 -> 2781, and tests/verification/rung3/test_closure_evidence_exists.py
       gained one failure (test_the_artifact_cites_evidence_at_all)
cmd    sed -n 38p and sed -n 53p on that file
out    CLOSURE = sorted((REPO / "docs" / "closure").glob("F*.md"))
       @pytest.mark.parametrize("doc", CLOSURE, ids=lambda d: d.stem)
cmd    sed -n 99,100p tests/test_tree_prose_consistent.py
out    ROOTS = ("floatfea","tests","scripts","docs/milestones","docs/verification")
       EXTRA_FILES = ("CLAUDE.md",)
```

**A closure artifact adds four parametrised cases to the collected count -- the same
shape as R361, which is the measurement that withdrew the justification of the last
pathspec exemption. `CLAUDE.md` is scanned by the prose guard. `docs/milestones/F2.md`
carries the integer that selects the entire input of the guard-state harness.** So the
exempted set is not inert, and what the rule claims after `9682bcc` is narrower than the
sentence written beside it.

**The real problem is that no pathspec can express this rule**, and that is worth saying
plainly rather than iterating on the list. The rule wants "the suite count in the report
still describes the head". What it checks is "no commit of a certain shape followed the
report". Those diverge in both directions, and R546 was the divergence becoming
unsatisfiable. **The satisfiable form needs no new apparatus: either the count is
re-taken by the last commit before the reviewer is invoked, or the rule is retired and
`tests/test_collected_set_golden.py` -- which already exists and already compares the
collected set against a golden -- is what carries the property.** I am not asking for
either; the F2a list is frozen and this is a choice about a rule, which is for Xabier.

**What I am asking for is that the four blocking items be fixed before the report for F3
step 1 is written**, because that report whole-suite line is the first artifact measured
by the relaxed rule, and verdict 65 already predicted the failure mode in those words: a
rule that goes red on a comment is a rule that will be worked around, and that is worse
than not having it. The worked-around version is what `9682bcc` produced, and I would
rather say so now than certify it.

## Tolerances touched

**None.**

```
cmd  git diff e663a88..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 9682bcc~1..9682bcc -- floatfea
out  (no output)
```

No counter changed, no injection site changed, no golden file changed, no assertion
threshold changed. **One not-a-tolerance declaration was added and it is correctly
formed**: `EXECUTABLE_PATHS` at `tests/test_report_carried.py:2230` carries
"not-a-tolerance: a pathspec. Nothing is compared against it", which is true -- it is a
domain, and R555 is about the domain being wrong, not about it being a threshold.

## Closure items

Not blocking under CZ0. Not to be re-reviewed item by item. Fixed once, in the closure
commit. **C28 and C29 from verdict 65 stand unchanged and are not repeated here.**

- **C31. `scripts/write_verdict.py:14-19` -- C30 was answered and the same defect was
  written in its place. The file has FOUR refusals and the new docstring says two.**
  ```
  cmd  grep -n "sys.exit" scripts/write_verdict.py
  out  53: the Verdict: line;  56: the missing-sections list;
       58: the empty Carried section;  63: no step report at ...
  cmd  grep -n "the two refusals" scripts/write_verdict.py
  out  17: "No such check exists in this file -- the two refusals are"
  ```
  The false clause **was** deleted and only the false clause -- I read the hunk, and the
  only other words lost were the hedge "by accident or", which claimed nothing. But the
  replacement is a new false claim about refusals, in the same file, in the same
  sentence shape, introduced while fixing a false claim about refusals. **That is CP2
  verbatim: the prose written around the fix inherits none of the discipline applied to
  the fix.** Closed when the docstring names four, or names none and points at the code.
- **C32. `scripts/write_verdict.py:16` -- the PLACEHOLDER token makes the quoted false
  claim unreadable, and nothing requires it.** A grep for PLACEHOLDER over `tests/`,
  `scripts/` and `floatfea/` returns only that line; no test reads the text of this
  file. A reader cannot see what was wrong with the old sentence, which is the one thing
  a withdrawal is for. Closed when the withdrawn words are quoted or the quotation is
  dropped.
- **C33. The `EXECUTABLE_PATHS` and `_changes_the_parse` docstrings state a property
  that is false, and the false sentence is the justification for the domain of a gate.**
  `tests/test_report_carried.py:2236` (docs and CLAUDE.md "cannot move a suite count"),
  `:2273` (everything else "cannot change a test outcome") and `:2299` (a comment-only
  edit "cannot move a suite count"). All three are refuted above by measurement. **I
  class these as closure items and not as blocks only because R555, R556 and R557
  already block on the domain itself**; if the domain is repaired and these sentences
  are left, they become the only statement of what the rule covers and they are wrong.
  Closed when each is either a CW0 triple with a registered needle or reduced to the
  measurement that was taken.
- **C34. The out line "1 commit: 80735cf" in the commit message and in the invocation is
  wrong at the commit it describes.** It was measured before committing.
  ```
  cmd  python -m pytest tests/test_report_carried.py -q -k whole_suite_line_is_about
  out  2 commit(s) touching code follow the report own commit 36b5899:
       9682bcc process: R546, BE3 and write_verdict.py -- three rulings (DQ3)
       80735cf R544: the ancestor state plants a real ancestor (DO0)
  ```
  The implementing commit of the rule is itself an intruder, which is not a defect but
  is the number. BP0 -- when the decision rule changes, every figure citing it is
  regenerated in the same commit -- applies to a figure measured at HEAD~1 and published
  at HEAD.
- **C35. `test_the_pathspec_names_every_executable_tree` fails false on a working copy
  that git status calls clean.** It walks `ROOT.iterdir()` rather than tracked files, so
  a gitignored tree counts.
  ```
  cell   ONE VARIABLE: mkdir -p build/lib/floatfea and one .py inside it
  cmd    git status --porcelain
  out    (empty)
  cmd    python -m pytest tests/test_report_carried.py -q -k pathspec_names_every
  out    1 failed -- AssertionError: [build] contain executable content and are not
         in EXECUTABLE_PATHS
  ```
  `.gitignore` lists build/, dist/ and egg-info. It did **not** fire on CI at `9682bcc`,
  so the editable install did not leave a build tree with .py in it there -- but it is
  one `python -m build` away on any developer machine, and the CLAUDE.md rule is that a
  guard which fails false is fixed or deleted. Corpus entry
  `gitignored_build_tree_present_in_the_working_copy`, batch 15. Closed when the walk is
  over tracked files.

## Corpus

**`tests/corpus/report_guard_states.txt`, batch 15, committed separately at `b9a9859`.
Seven entries, all seven unseen, plus one ruling on an existing entry.**

**Coverage: the rule under review catches 2 of 7.** Four are holes -- pyproject only,
the comment-only `floatfea/` commit, the docs/closure artifact, and the plan marker --
and each is R555, R556, R557 or the Xabier item above. Two are caught, both merge
shapes, and one of those, `plain_no_ff_merge_of_a_code_branch`, is caught **by a
different route than the rule describes**: the merge itself is exempt and git history
simplification reports the side commit instead. The seventh is the only require=green
row and the rule reds on it (C35).

**The old measurement protocol is still unavailable and this is its second round of
cost.** Building each state and running `tests/test_report_carried.py -q` requires a
green baseline; baseline is red at `9682bcc`, so no outcome would be attributable to the
variable moved. I measured instead as controlled pairs -- the rule own
`_implementer_commits_after` and `_changes_the_parse` called on each state commit in a
scratch clone, plus `--collect-only` before and after -- and the batch header records
that deviation. **A corpus round on this rule has not been available at the rule own
commit for three verdicts.**

**The ruling.** `closure_artifact_is_the_only_commit_after_the_report` keeps
require=fail. Its measurement flips from CAUGHT to HOLE because DQ3 exempted `docs/`,
and **I did not change require to match the new behaviour**: the state is a stale count
by measurement (2777 -> 2781, plus a rung-3 failure), so the corpus records the property
and the disagreement of the implementation with it. The invocation asked whether
building these five would change what R546 should have been. **For this one, yes**: it
stops being a negative control the moment `docs/` is exempt, and the shape it was
written for is still live. For `suite_line_names_the_report_commit_ITSELF` and
`only_a_REVIEWER_corpus_commit_follows_the_report`, no -- R546 touched neither mechanism
and they are R548 unchanged.

**And a warning about transcribing them.** Every entry built adds a
`test_the_guard_survives_the_state` case; every entry *not* built adds a `KeyError`.
Until R558 is fixed the corpus cannot grow without reddening the build, and it grew by
seven this round: `tests/test_report_guard_states.py` went from 14 failed to 21 failed
at `b9a9859`, and the tree from 15 failures to 22.

## Next step opens when

**`9682bcc` is NOT accepted as it stands. Step 7 stays closed, F2 stays closed, verdict
63 at `2c48a4f` remains the closure verdict, and F3 step 1 does NOT open** until the four
items below are answered in `tests/`. They are all apparatus in the (c) sense -- what a
gate claims -- and none of them requires new apparatus or a plan change.

1. **R558 first**, because it is the cheapest and it is the ruling that was directed and
   not delivered. A corpus entry with no build action produces no failure, demonstrated
   by adding one and measuring zero new reds.
2. **R555.** `pyproject.toml` inside the domain, and
   `test_the_pathspec_names_every_executable_tree` able to fail on a top-level file that
   is missing from the list -- broken once to show it reds.
3. **R556.** The parse exemption stops covering files whose comments a shipped test
   reads, with the readers named by path and line, or the docstring claim is reduced to
   the two commits actually measured.
4. **R557.** The trigger of the transcription backstop is not a document the implementer
   edits in a commit the whole-suite rule exempts, and it survives the milestone
   boundary. Break it to check: leave one entry untranscribed and confirm red.
5. **Each of R546, R547, R548 and R549 answered site by site per CLAUDE.md**, including
   any site left and why. The distance-zero half of R548 is one line, `:2489`, and has
   now been carried through four verdicts untouched.
6. **R545 and R550 unchanged**, carried by name -- R545 before any F3 test parametrises
   G2.4 over a platform member, R550 into F4 through DQ5, with **no step report citing
   G4.2 as a check on the mass matrix until the V4.2 row is re-specified**.
7. **The DP3 counter registered at a stated operating point and not injected on a rigid
   translation** -- the 2.7e-16 of ma08 and L/D = 15.612, from verdict 65.
8. **The commit that answers this carries a report**, or its numbers carry their commands
   at the commit they describe. Three commits in a row have now arrived without one and
   C34 is what that costs.

**On the schedule, because it is a requirement and nobody else is measuring it here.**
Three of the last four verdicts on this file have been consumed by the guard apparatus
rather than by the platform, and F3 step 1 has not started. **That is slippage against 5
and 10 October and it is reportable today, not when a step closes.** The choice CLAUDE.md
asks for is stated rather than made: slip the date, or reduce scope -- and I note that of
the four blocking items here, R558 is a two-line change and R557 a handful, so the cost
of clearing this HOLD is hours, not a round. **The 12-buoy BEM solve at 19.69 GB resident
against a 12.71 GB documented estimate, with 20.68 GB free of 63.7, is not mine to rule
on and I have not measured it; it is here only so that it is in a document.**

**Not in this verdict and not reviewed here:** the work of step 7, DM0, DM2, DP1 through
DP5, DQ4, DQ5, DQ2, the ../HSP-stable pin, and the design-wave load-case answer.
