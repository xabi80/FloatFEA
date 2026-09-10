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
`.claude/agents/gating-supervisor.md` — the list lives there, once.

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
4c. `git diff <prev>..<this> -- 'tests/**/conftest.py'` separately (CH2).
   **Everything the ladder's gate reads is writable from a rung's own
   conftest.** `scripts/run_rung.sh` reads pytest's junit report and pytest's
   exit code, which is the right pair and is what killed four text channels --
   and a `pytest_runtest_makereport` hookwrapper in the rung's directory turns a
   failing report into a passing one, while `pytest_ignore_collect` and
   `pytest_collection_modifyitems` delete the failing test before anything
   records it. All three were measured reaching `run_rung: OK`, exit 0, on a
   genuinely red rung.
   No gate closes this, because a gate reading a record cannot outrank code that
   writes the record. **Review is the bound**: a conftest under `tests/` changed
   inside a step commit is inspected line by line, every step, exactly as
   `tolerances.py` is.
5. Open the *previous* inside review and the previous witness comment. List
   every item either marked as blocking. For each, find the answer in this
   step's diff or report. An unanswered blocking item is a HOLD on its own.
6. Now read the diff for the step, then the inside verdict, then the report —
   in that order. Every claim in the report is located in the diff or the test
   output; a claim that cannot be located is recorded as unverified.
7. Construct one adversarial case for the step and run it. The inside
   supervisor is asked to do the same; do not assume it did.
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

## What the witness does not do

It does not merge. It does not edit tests, tolerances, or reviews. It does not
soften a HOLD because the inside verdict was PASS. And it does not accept "the
supervisor already checked this" as evidence — that sentence is the reason the
witness exists.
