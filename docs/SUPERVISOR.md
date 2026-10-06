# The Outside Witness

How a reviewer that is *not* the implementing session, and *not* invoked by
it, reviews FloatFEA steps through the pull request — so that review does not
depend on a person pasting output between two chat windows.

There are two reviewers in this repository and they are not redundant.

The **gating-supervisor** (`.claude/agents/gating-supervisor.md`) runs inside
Claude Code, invoked by the implementer at every step boundary, and its verdict
in `docs/reviews/` gates the next step through a hook. It is fast and it is
always there. Its limitation is structural: it is invoked by the thing it
judges, and it sees the repository through the same tools on the same machine.

The **outside witness** is any session that reads the PR from outside — a
Cowork session watching the PR, or a scheduled task that wakes on its own
clock. It has no conversation with the implementer, is not invoked by it, and
reviews the diff and the test run rather than the report. Its job is the class
of failure the inside reviewer cannot see: a step executed on top of an
unanswered gate, a verdict written in the same commit as the code it approves,
a report that is accurate about what it covers and silent about what it skips.

Both read this file. The witness applies exactly the guards in
`.claude/agents/gating-supervisor.md` — the list lives there, once — and
**both rule under the same blocking criterion (CZ0)**, in that file's
§ *What blocks, and what is a closure item*: a finding blocks only if it is a
defect in `floatfea/`, a tolerance value or form, a gate assertion, or a red
test at the reviewed commit. Everything else is recorded as a closure item and
does not hold a step. A witness HOLD on something outside (a)–(d) is not a
stricter verdict; it is a verdict under a criterion this repository retired.

---

## The channel

One PR per milestone, branch `F<n>`, opened at the milestone's first commit and
kept open until closure. Each step lands as one or more commits; the step
report `docs/reports/F<n>/step-<k>.md` is committed with the step; the inside
verdict `docs/reviews/F<n>/step-<k>.md` is committed **separately**, after.

**F2's channel is live: `xabi80/FloatFEA`, private, PR #1, `F2 -> master`.**
Opened late — at the close of step 4 rather than at the milestone's first commit
— because the repository did not exist until then. **Steps 1 to 4 therefore have
no witness comment and never will**, and that is a gap in the record rather than
a clean bill: twenty-five consecutive reviews of step 4 were written by one
reader. The first witness comment this milestone can carry is on step 5.

The witness posts as a PR comment prefixed `[witness F<n> step <k>]`, in the
same block format the reviews use (`Verdict`, `Carried`, `Findings`,
`Tolerances touched`, `Next step opens when`). The implementer's standing
instruction (`CLAUDE.md` § Step gating) is to read the latest witness comment
before opening any step, and to treat a witness HOLD exactly like an inside
HOLD: it is answered before anything else, and the answer goes in the next
report's `Carried` section.

The witness and the inside supervisor may disagree. When they do, the stricter
verdict stands, and the disagreement itself goes into the next report.

## The witness protocol

Run these in order. Do not skip to the report.

```
gh pr list --state open --json number,headRefName,title
gh pr view <n> --comments --json comments,commits,headRefOid
gh run list --commit <sha> --json name,conclusion,workflowName
```

**A red CI is a HOLD regardless of what a local run says** (CA2), and the reason
is measured: the first time this project's CI reached the verification ladder it
found thirteen failures in a rung that had been green locally for weeks. CI is a
machine neither reviewer controls. A run that has not finished is not a pass, and
a workflow that did not run on the reviewed commit is an unavailable check --
recorded as unavailable, never skipped over.

**THREE STATES, NOT TWO (CK2).** `red`, `green`, and **`unavailable --
allowance exhausted`**, which is neither and does not HOLD on its own:

```
cmd  gh api repos/<owner>/<repo>/actions/runs/<id>/jobs
out  every job: runner_name "", steps [], a two-second duration, and the
     annotation "The job was not started because recent account payments have
     failed or your spending limit needs to be increased"
```

A job that was never started measured nothing. Reading it as red would HOLD a
step on a billing account, and reading it as green would be worse. Record the
state, name the last run that DID execute, and say whether the code has moved
since -- `git diff <that run's commit>..HEAD -- tests/verification scripts
.github` empty means the ladder result still describes the tree. Then judge the
step on everything else.

1. Identify the newest `docs/reports/F<n>/step-<k>.md` on the branch and the
   newest `[witness ...]` comment. Every step report newer than the last
   witness comment is unreviewed by the witness. Review them oldest first.
2. Check out the branch at the commit being reviewed. Run the tests yourself:
   `python -m pytest -q`. Record the counts. A count that differs from the
   report's is a finding before anything else is read.
3. `git log --format='%h %s' <prev>..<this>` — and check that no commit touches
   both `floatfea/` and `docs/reviews/`. A verdict committed with the code it
   judges is a finding regardless of the verdict's content.
4. `git diff <prev>..<this> -- floatfea/tolerances.py`. Every changed line has
   a form (relative, dimensionless, or ULP-scaled with recorded measurements),
   a `_COUNTER` in the assertion's own quantity, and a justification located in
   `docs/milestones/F<n>.md` or the closure artifact. Missing any one is a
   HOLD.
4c. `git diff <prev>..<this> -- tests/conftest.py 'tests/**/conftest.py'`
   separately (CH2, corrected by CI0).

   **BOTH PATHS, AND THE FIRST ONE IS THE FILE THAT EXISTS.** The pattern
   `tests/**/conftest.py` alone matched NOTHING in this repository: git's
   default pathspec glob will not let a double star stand for zero
   directories, so it means "depth two or more", and the only conftest here is
   `tests/conftest.py` at depth one. The instruction read as "every conftest
   under tests/" and returned the empty set for a full round while that file
   implemented `pytest_collection_modifyitems` -- one of the channels this
   item exists for -- for every rung at once.

       $ git ls-files -- tests/conftest.py 'tests/**/conftest.py'
       tests/conftest.py

   `tests/test_supervisor_conftest_pathspec.py` asserts that the pathspec in
   this file matches every conftest in the repository, and reddens when one
   appears outside it.
   **Everything the ladder's gate reads is writable from a rung's own
   conftest.** `scripts/run_rung.sh` reads pytest's junit report and pytest's
   exit code, which is the right pair and is what killed four text channels --
   and a `pytest_runtest_makereport` hookwrapper in the rung's directory turns a
   failing report into a passing one, while `pytest_ignore_collect` and
   `pytest_collection_modifyitems` delete the failing test before anything
   records it. All three were measured reaching `run_rung: OK`, exit 0, on a
   genuinely red rung.
   No gate closes this, because a gate reading a record cannot outrank code
   that writes the record. **REVIEW IS THE BOUND** (CJ0). The claim that a
   forgery must now be consistent across two places is WITHDRAWN: the
   cross-check in `scripts/run_rung.sh` closes two of the six channels that
   have been measured, and the sixth defeats it with one keyword argument --
   a `pytest_runtest_call` wrapper with `trylast=True` calling
   `outcome.force_result(None)`, which the tally cannot see because the tally
   is taken inside the hook it wraps.
   The plan states the boundary: in-tree code is trusted under review, and
   resistance to forgery BY in-tree code is out of scope for F2. The
   cross-check stays as a consistency guard against ACCIDENT. What you are
   reading this diff for is the intent of a change to code that runs inside
   the measurement -- line by line, every step, exactly as `tolerances.py`.
5. Open the *previous* inside review and the previous witness comment. List
   every item either marked as blocking. For each, find the answer in this
   step's diff or report. An unanswered blocking item is a HOLD on its own.
6. Now read the diff for the step, then the inside verdict, then the report —
   in that order. Every claim in the report is located in the diff or the test
   output; a claim that cannot be located is recorded as unverified.

   **And the same reading runs over the DIFF's prose, not only the report's
   (CW1).** Any sentence in a comment, a docstring or a locked plan that
   asserts what the code does or does not do, and carries no
   `claim:`/`cmd:`/`out:` triple beside it, is a finding. This is a reading
   and not a pattern on purpose: two rounds were spent on keyword detectors
   for it and they measured **0 of 20** and **3 of 8** against unseen
   phrasings, while the reviewer reading the diff found eight such sentences
   in one round and five more in the next. `tests/test_tree_prose_consistent.py`
   checks the triples that exist and says in its own docstring that the rest
   is this step.

   A triple whose command cannot fail is the same finding: the reviewer runs
   the `cmd:` with the needle changed and confirms the answer moves.
7. Construct one adversarial case for the step and run it. The inside
   supervisor is asked to do the same; do not assume it did.
7b. Rule under CZ0. Sort every finding into blocking (a)–(d) or closure, and
   count the verdicts this step already has — on the third the step closes
   with its open items carried by name, and the witness says so rather than
   asking for a fourth.
8. Post the comment. If the verdict is STOP, also say so in the PR title
   (`[STOP]` prefix) so it is visible without opening the thread.

## Running the witness

**From a Cowork session** (same-day, interactive): the session polls the PR
with a persistent monitor — new commits or comments wake it — and runs the
protocol on each wake. This keeps a human-readable audit trail in the chat, and
it dies with the session. Good while a milestone is moving quickly and someone
is around.

**As a scheduled task** (standing): a task that fires every two hours in a
fresh session with the prompt below. It has no memory of any conversation,
which is the intended property — everything it needs is in this repository, and
if it is not, the repository is what gets fixed. Requires the task's
environment to have `gh` authenticated against the FloatFEA repo.

Scheduled-task prompt, verbatim:

> You are the outside witness for the FloatFEA repository
> (`github.com/<owner>/FloatFEA`). Clone or update the repo, read
> `docs/SUPERVISOR.md` and `.claude/agents/gating-supervisor.md`, and run the
> witness protocol on every step report that has no `[witness ...]` comment
> yet, oldest first. Run the tests yourself. Post one comment per step in the
> block format. If there is nothing unreviewed, post nothing and end. Do not
> edit any file in the repository; you review, you do not fix.

## Corpus scope through F6 (DE2)

**Corpus rounds target the element, the gates, and — from F3 — the platform
model. Not the apparatus.**

This is a scope instruction to the reviewer, from the technical supervisor. It
is **not** a guard change and nothing in `tests/` enforces it; the reviewer is
asked to hold it.

**No new corpus files for apparatus species** — prose staleness, pointer
claims, report shapes, guard shapes, runner claims, repair-staleness. The
existing apparatus corpus files stay exactly as they are, and they **join the
frozen 4a list** rather than growing.

**REPAIR-STALE is recorded on that list with its coverage, 0 of 13, and is not
transcribed.** A coverage number is a measurement, not a work item.

**The reasoning, stated so it can be argued with.** Each new apparatus corpus
is a new species of prose or process defect, and each one forces transcription
work on the implementer before the gate can move. Measured over the rounds
that produced them: the apparatus corpora caught 2 of 22 unseen shapes, then 1
of 19, then 0 of 16, then 0 of 13 — while four days of rounds went into
apparatus and R475, the one finding that touched the gate, did not land. The
corpus rounds that found something about the *element* are the ones worth the
implementer's time: R475 itself came from a corpus-adjacent span ladder, and
R486 from a near-vertical orientation nobody had built.

**What does not change.** BE3 is unchanged in every other respect: the corpus
is the reviewer's, the implementer's tools are blocked from it, entries are
unseen, the old ones stay, and the coverage measurement the reviewer reports
is still the number that decides whether a check is worth anything. What
changed is only what the entries are *about*.

Apparatus defects are still findings. The reviewer reads for them, reports
them, and — under CZ0 — most of them are closure items.

## What the witness does not do

It does not merge. It does not edit tests, tolerances, or reviews. It does not
soften a HOLD because the inside verdict was PASS. And it does not accept "the
supervisor already checked this" as evidence — that sentence is the reason the
witness exists.

## The milestone witness (DO3)

**The PR witness above never ran.** Fourteen rounds, no outside comment on any F2
step, and F2 closed with twenty-eight consecutive reviews by one reader. A channel
that is available and unused is not a second reader; recording that here is the
first half of the fix.

**The second half is cheaper and it runs. At each MILESTONE close, one independent
pass:**

* a **fresh reader**, not the gating supervisor, with **no conversation history** —
  it is given the repository, `PLAN.md`, `CLAUDE.md`, `docs/conventions.md`, the
  ladder, the milestone plan and the milestone closure artifact, and nothing about
  how the milestone went;
* asked **one question in two halves**: *does this milestone's physics do what the
  closure artifact says, and what would you test that nobody did?*
* **one pass, not a round.** It writes no verdict, it does not gate, and it does
  not enter the three-verdict count. Its findings go to Xabier.
* it may not modify a tracked file. If it needs a tree it takes a `git worktree`
  outside the repository and removes it.

**Once per milestone rather than once per step**, which is what makes it
affordable: seven steps of F2 would have been seven passes, and the weakness the
witness exists to catch is a milestone-level one — a physics claim that has been
read so many times by the same reader that it stops being read.

**Why it is asked about the ARTIFACT and not the diff.** The closure artifact is
what a later milestone builds on and what F4 will cite when its inertia relief
reads this element. If the artifact's physics claims do not hold, nothing
downstream of it is safe, and that is a different question from whether any step's
diff was correct.

**It is not a substitute for the PR witness.** If the PR channel ever runs, both
apply and the stricter finding stands, exactly as the step-level rule says.

## The `Answers:` sha is the VERDICT'S OWN COMMIT (DX2, C13)

**The next report's header names the commit the verdict TEXT is final at -- the
reviewer's own verdict commit -- and never the commit the verdict judged.**

`VERDICT_TEXT` is read AT the commit the header names. Naming the judged commit makes
every generator read the PREVIOUS verdict: the carried table comes out with the wrong
round's rows, the answered table with the wrong subjects, the sites table with the
wrong sites. Two consecutive hand-backs proposed the judged commit, and the second
cost three rebuilds of one revision before the cause was found.

So a closing instruction reads `Answers: verdict <n> @ <the verdict's own commit>`.
The commit the verdict judged is stated separately, in the body, bolded and backticked
per DU1 -- it is what CI is reported for, and the two are different commits.

## The apparatus freeze (DR1)

**Absolute, until the member-force table ships.** No new guard, no guard edit, and
no guard fix except deletion. **A guard that fails false is DELETED, with the
reason recorded at the site — not repaired.**

Earned by measurement, not by impatience. Four of the last five verdicts on F2
step 7 went to the report-carry apparatus rather than to the platform, and the
rule at the centre of them produced a finding against *itself* in four consecutive
rounds: no satisfiable state at a milestone close (R546), a hardcoded milestone
path that no F3 report could clear (R564), three anchor states needing different
distance rules from each other (R563), and distance zero never rejected at all
(R548). Each repair moved the defect instead of closing it. It is retired under
DR0 and `tests/test_collected_set_golden.py` carries what remains checkable.

**Reviewer corpus.** Batch 15 and any later apparatus corpus go to
`docs/milestones/F2a.md` **untranscribed**. The count is reported by the
corpus-agreement meta-test so the debt stays visible; the backstop that asserted
it zero at a step close is deleted, because it was failing *true* against a
decision already taken. It returns when the freeze lifts.

**When the next verdict is requested.** Post-closure verdicts count against the
next step's cap. **The next verdict is requested only after DP2 and DQ4 have
landed** — the `f0` mode pairing and the `M.a` test. Not after each apparatus
commit, and not per directive.

**Why this is worth the risk, said plainly.** The freeze trades away the chance of
catching a new apparatus defect for the certainty of reaching a first result. F2's
one real element defect was found by the reviewer reading physics, and the
milestone witness found its blast radius by reading physics. Neither came from the
report-carry apparatus. What that apparatus has produced lately is findings about
itself.

## The verdict file ACCUMULATES (DX2)

**Each round is appended under a dated heading. No prior round is ever rewritten or
removed.**

This is not housekeeping. `tests/test_report_carried.py::test_no_status_claims_more_than_the_verdict_allows`
states its premise in its own docstring -- *"the WHOLE review file, every round of it,
because a withdrawal ruled two verdicts ago is still a withdrawal"* -- and that premise
was false of the file:

```
claim  the verdict file held ONE ROUND, not an accumulating record
out    83c7ba5  397 lines  R567 x3
out    4314118  508 lines  R567 x2
out    4ff1008  508 lines  R567 x2
out    1b895db  538 lines  R567 x0
judge  verdict 69 withdrew R567 explicitly and the text was gone two rounds later,
       so the guard could not see any withdrawal older than the current round, and
       a report reporting the withdrawal truthfully went red. Twelve reds traced to
       that one status cell.
```

**The rule is here rather than in the guard deliberately.** Making the file accumulate
makes the guard's premise true; loosening the guard would remove the one check that
stops a report retiring its own findings. The mechanical cause is
`scripts/write_verdict.py`, which uses `write_text` rather than appending -- **that is
the reviewer's tool to change, and this entry is the requirement, not the patch.**

## How a verdict is written so the parsers can read it (DU1)

Two rules about the reviewer's own output. **No parser changes; this is the format
side of a mismatch that cost six red guards.**

**One: always restate the judged commit in the body, bolded and backticked, even
when it equals the header.**

```
**Reviewed commit: `0a660ce`.**
```

`scripts/ci_section.py` reads that form and not the header's plain
`Reviewed commit: <40 chars>`, because under R513 the stamped header is normally
the reviewer's *corpus* commit and therefore not the commit judged. **Verdict 68
wrote no corpus commit — deliberately — so its header was the judged commit and
its body never restated it, and the generator refused to produce a CI section at
all.** The convention that makes the header untrustworthy is exactly what made it
trustworthy that round, and no parser can tell the difference. Restating it always
costs one line and removes the case.

**Two: a blocking finding's class and its blocking status go INSIDE the
parentheses.**

```
**R567. (d, blocking) ...**          not    **R567. (d) -- BLOCKING, ...**
```

`tests/test_report_carried.py`'s `_blocking()` matches
`^\*\*(R\d+)\.?\s*\(([^)]*)\)` and requires `block` within the captured group.
Verdict 68 put `BLOCKING` outside the parentheses, so the guard parsed no blocking
finding and reported — correctly — that the heading format had changed and the
check would pass on anything.

**Neither of these is a judgement about content**, and neither narrows what the
reviewer may find or say. They are the shape the existing readers expect, recorded
here because the alternative was editing two parsers during an apparatus freeze.

### A closure commit is verified after it exists (CZ1)

*Adopted by directive EB1, in the reviewer's wording, unparaphrased. It was
proposed in the seventy-ninth verdict after the closure commit `8e4238d` shipped
two reds that the implementer's loop could not see.*

**A closure commit is verified AFTER it exists (CZ1).** A closure commit is written
after the last reviewed round and is not reviewed by rule, so nothing between it and the
next step's report measures it. Two classes of red shipped in 8e4238d for that reason: the
lint gate, which `pytest` does not run, and the report guards, whose answer is a function of
the commit graph and therefore cannot be taken before the commit exists.

So, for every closure commit, in this order: **(i)** make the commit; **(ii)** at that
commit, tree clean, run and paste `ruff check floatfea tests`, `black --check floatfea
tests`, `mypy floatfea` and `pytest -q`; **(iii)** push it and paste `gh run list --commit
<sha>` with the job-level conclusions, so that the lint job's `guards and meta-tests` step
is seen to have RUN rather than been skipped behind an earlier red step; **(iv)** any red is
answered in a follow-on commit that repeats (ii) and (iii). A closure commit is not finished
until a pushed CI run at its own sha, or at the follow-on's, is green.

The four outputs are `claim / cmd / out` triples (BF0, CP2) in the step report's closure
section, or -- where that report is already closed -- in the next report's `Carried`.

**The reusable half of it:** a check whose input is the commit itself cannot be measured
before the commit exists. That class includes `tests/test_report_carried.py`,
`tests/test_report_guard_states.py`, and anything reading `git log`, `git diff` or
`git merge-base`. For those, "I ran it before committing" is not a measurement.

### A closure commit that changes a gate or a tolerance is REVIEWED (EQ0)

*Adopted by directive EQ0 in the reviewer's wording, unparaphrased. Proposed in the
ninety-sixth verdict, which reviewed a closure commit for the first time and found four
blocking items in it -- three of them inside repairs made to answer blocking items -- in a
tree that was green on three machines.*

> **A closure commit that changes a gate or a tolerance is reviewed; one that changes only
> prose is not.**

**That review counts against no step's rounds (EB4).** It judges a commit written after the
last reviewed round, so it is not implementer work done for the next step.

**Why green was not enough, which is the whole reason for the rule.** CZ1 (ii) and (iii)
measure whether a closure commit is GREEN. A green suite cannot see:

* a counter declared on the wrong side of its own defect -- `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER`
  shipped at `0.05` above the defect on 12 of 16 members, because the figure was derived
  against the CORRECT root moment while the gate divides by the DEFECTIVE one (`1/19` on
  the platform arms, `1/24` on the hubs; no member read the published `5.555556e-02`);
* a decision rule that nothing holds in place -- the per-body mapping residual shipped with
  both of its counter-cases red under the aggregate it replaced, so reverting the fix left
  the whole suite green, and the counter-case the commit message SAID was added was not in
  the file at all;
* a figure whose rule moved underneath it (BP0) -- four figures in a tolerance entry,
  measured against the aggregate the same commit deleted.

Each of those is `(b)` or `(c)` under CZ0 and each was invisible to `pytest -q`, to `ruff`,
`black` and `mypy`, and to a green CI run at the commit's own sha.

**And a closure commit NEVER touches a step report after that report's final verdict
(EK3).** Measured three ways, one variable moved: the report-prose edits in place gave
`7 failed, 16 passed`; the same commit with the report's CONTENT reverted to byte-identical
gave `7 failed, 16 passed` again; the commit with the report left out entirely gave
`23 passed`. The guard compares the newest commit touching the report against the newest
touching the verdict, so reverting content cannot help -- **any** commit that touches a
closed report before a newer verdict exists reddens it. EK3 already routed post-closure
prose to "the next report or `docs/closure/**`"; this is the mechanical reason for that
wording rather than a preference.

### Round counting across a step boundary (EB4)

*Recorded by directive EB4, answering the question raised in the eightieth
verdict: five verdicts were spent after F3 step 1 closed at PASS, on a STOP
against the locked plan, and under the rule as it stood step 2 would have opened
with its three rounds already spent before its first line.*

**A verdict spent on a STOP or blocker whose resolution belongs to the supervisor
or to the user counts against NO step.** Post-closure verdicts count against the
next step only when they judge implementer work done for that step. A step
therefore opens with its full three rounds, counted from its first report.

**ROUNDS ARE COUNTED PER REPORT REVISION, AND AN INTERIM CHECK COUNTS AGAINST NONE
(ES0).** Adopted by directive ES0, which took exit (i) of the two the ninety-seventh
verdict named. **The `Stop` hook is not edited.**

* **At most THREE REVIEWED REVISIONS per step.** The count is of revisions, not of
  verdicts.
* **A verdict the hook forces at a turn boundary mid-step, on a tree with NO new report
  revision, is an INTERIM CHECK and counts against no round.**
* **An interim check is light:** the suite and CI at the commit, plus a CZ0 (a)-(d) scan
  of the diff since the last verdict. **No corpus batch, no closure list.**
* **Its findings join the step's list** and are answered in the next revision.

Why the clause exists, which is the part a later reader needs: EQ3's "one reviewer
invocation, at the report" and the hook's "nothing past the newest verdict" cannot both be
satisfied by a step that takes more than one commit, and F4 step 2's ER1(b) alone is six
FloatSim re-runs. Without this clause the implementer's choices were to spend a round on a
third of the work, to revert verified work to silence a hook, or to write a verdict -- and
the third is forbidden outright.

The ninety-seventh verdict ruled, correctly under EB4 as it then stood, that a
hook-forced round counted: EB4 keys on the SUBJECT of a verdict and that verdict's subject
was implementer work. This clause keys the exemption on whether a new report revision
exists, which is what distinguishes "the work has reached a reviewable state" from "a turn
ended".

**It is not a free round.** An interim check still rules under CZ0 (a)-(d) and its findings
still block; what it does not do is consume one of the three rounds in which the step's
work gets read in full. DK0's concern -- that a mechanism which buys rounds makes the cap
meaningless -- is answered by the revision count: three revisions is three revisions
however many interim checks fall between them.

### CZ1's carve-out for a step's own boundary red (EG3)

*Adopted by directive EG3 in the reviewer's wording, unparaphrased. Proposed in the
eighty-first verdict's ruling 4 and sharpened in the eighty-third; the reviewer
applied it by hand three times before it was written down.*

> **CZ1 step (iii) does not apply to the boundary red a step's own report creates, on EITHER side of the verdict.** Two states, both designed, both self-clearing, and neither is a defect:
>
> **(1) Report written, verdict not yet.** The only failures are `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` and the planted states that cascade off its baseline. The verdict clears them.
>
> **(2) Verdict written, answering report not yet.** The only failures are `test_every_named_site_is_touched_or_declared`, `test_the_report_carries_the_finding`, `test_the_CI_section_is_about_the_REVIEWED_commit`, `test_the_Carried_table_is_what_the_generator_produces` and `test_the_generator_would_catch_a_row_under_the_wrong_number`, each naming a finding or a site of the newest verdict. The answering report clears them.
>
> In either state the run is recorded as RED WITH ITS CAUSE NAMED -- the full `FAILED` list pasted, and the sentence saying which of the two states it is -- and work proceeds. **Any failure outside the state's own list is CZ1 (iv) unchanged**, and "only those" is a claim that carries the `FAILED` list as its command. The reviewer measures state (1) clearing at its verdict commit; the implementer measures state (2) clearing at the report commit.

**And the sharpening, which is the eighty-third verdict's own sentence:**

> the first-report carve-out should say that state (2) is cleared BY THE ANSWERING REPORT and not by time -- if no answering report is written the state does not clear, and a tree red with no revision in sight must read as what it is.

**The two lists, corrected (EH1).** The clause above was written from one observation
and was short by two names on each side. The reviewer's wording, adopted
unparaphrased:

> *state (1)'s list is `test_the_guard_reads_the_step_being_worked_on`, plus the
> planted states that cascade off a red baseline; state (2)'s is the five named, plus
> `test_the_answered_verdict_is_the_NEWEST_one`, plus
> `test_a_carried_row_points_at_a_section_that_discusses_it`, plus the same cascade.
> In both states the cascade is identified by the baseline being red and by each
> cascading state's own failure line, not by its name.*

**R644, adopted by directive EJ2 — the reviewer withdrew two placements of its own,
and the measurement is why.** At `b7c05e7`, with eighteen reds traced individually
rather than by family:

* `test_the_answered_verdict_is_the_NEWEST_one` was filed under **state (1)** and is
  a state (2) failure. It fires when a verdict is newer than the report, which is
  state (2) by definition.
* `test_a_carried_row_points_at_a_section_that_discusses_it` was on **neither** list
  and is a state (2) failure — red on two rows at that commit, and all twenty-eight
  parametrisations green with the answering revision in the tree.

Both were found by running the two off-list ids on their own instead of ruling them
as part of a sixteen-red cascade, which is the discipline EG3(i) exists to force.

**Any red not on the list still blocks** — EH1 restates that, and it is CZ1 (iv)
unchanged.

**Two conditions on it, from EG3:**

**(i) The waiver is conditional on the trace, and the trace is pasted.** The
pre-invocation green requirement is waived only if EVERY red traces by name to the
step-boundary cause. Not "the failures look like the boundary set" -- each `FAILED`
id is matched to the state's own list, and a red that does not match is CZ1 (iv)
unchanged. The eighty-third verdict is why the condition is worded that way: eight
planted states were ruled as one cascade by class across two verdicts, and the
eighth was a real defect (R629) sitting inside a group nobody was reading
individually.

**(ii) The verdict commit is measured too.** After the verdict commit exists, the
report-guard files are run AT that commit and the counts pasted in the next
revision. State (2) is the half no verdict in this milestone had ever measured,
because the reviewer runs at the judged commit before writing.

### Corpus batches pause until 28 October (EG4(e))

Recorded here because it changes what a round may spend. Batches pause after F3
step 3, except mutation work on **F4's load-mapping gate** and **EB6's
label-provenance gate** -- the two surfaces where a miss would reach a member
force. The coverage measurements that justified the spend are in the verdicts:
4 of 11, then 8 of 13, then 5 of 10, with the last round's misses all outside the
element.

### Every boundary is solved in BOTH directions (EH4)

**A boundary is solved in both directions, including the two that WEAKEN a gate: the
ceiling falls toward the clean value, and the injection rises until a clean case
trips.** This applies from F4's load-mapping gates on; the corpus pause above
otherwise stands.

Earned on one measurement. Corpus batch 31 solved every boundary from the side that
makes a gate look strong -- how far the gate's ceiling may RISE, how far the
injection may FALL -- and never the two that weaken it. Two of the next round's
three blocking findings came from inverting the direction and nothing else: a
production ceiling that widens `100x` with the measuring half of the suite green,
and an injection size that rises eight decades with every assertion getting easier.

**A figure is pasted from the run that produced the artifact it is pasted into, and
the pasting is the LAST edit (CP3).** Where a commit message, a report section or a
tolerance comment carries an `out` line, that line is copied from a run executed
after the final edit to the thing it describes -- not from a remembered run and not
from a previous round. The consequence is an ordering and not a new check: generate,
edit, re-run, paste, commit -- **and if an edit follows the paste, the paste is void.**
Earned three times in one session on figures that were each correct when taken.

*Adopted by directive EH0 in the reviewer's wording, unparaphrased, proposed in the
eighty-fifth verdict. BF0 says the figure carries its command; BP0 says it carries
its rule; CP2 says a repair's numbers carry theirs. **None of them says WHEN the
output is taken**, and the four figures that went wrong in one session -- `93000x`,
`1281`, `all 5`, `five decades` -- were each correct when first measured and
described a tree that had moved underneath them.*
