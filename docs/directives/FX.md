# FX — the Carried-table generator may read the verdict file

*Recorded under FP0: a directive is committed verbatim before it is acted on. This one
arrived as the answer to a question rather than as free text, so what is verbatim is the
question and the option selected. Both are reproduced exactly; nothing is paraphrased.*

## Provenance

**Issuer: Xabier. Date: 2026-10-30.** Asked in the session that then made the change; he
selected the first of three options. There is no additional free-text instruction, and this
file does not invent one.

**The issuer and date are stated because FY4 asked for them and this file did not carry
them.** FY4's wording is "FX was not issued by the supervisor in this channel. Make sure
`docs/directives/FX.md` exists and names its issuer and date" — the file existed and named
the issuer; the date was missing, and a directive record whose date a later reader has to
infer from `git log` is the same defect as one whose text they have to infer from a commit
message. **Accepted at FY4** (`docs/directives/FY.md`), both parts: the
`protect-reviews.sh` narrowing and the fail-closed guard that I flagged as going beyond
FX1's letter.

## FX0 — the question, verbatim

> The Carried-table generator needs `docs/reviews/R1/step-3.md` as a command-line argument,
> which the PreToolUse hook refuses. How should I proceed?

## FX1 — the option selected, verbatim

> **Narrow the hook in a process: commit**
>
> I write a standalone `process:` commit citing this as the directive, changing
> `.claude/hooks/` so the refusal keys on writes to docs/reviews/ rather than on the path
> appearing anywhere. It touches nothing in floatfea/ or tests/, as CLAUDE.md requires of a
> reviewer-instruction change — but it is me editing the guard that constrains me, which is
> why I will not do it unasked.

## FX2 — the two options NOT selected, recorded so the ruling's alternatives are legible

> **You run the one command** — You run
> `python scripts/carried_table.py docs/reviews/R1/step-3.md docs/reports/R1/step-3-answers.json > /tmp/carried.md`
> yourself and paste the output, or tell me the path you wrote it to. I build the answers
> JSON first so the command is ready. Nothing in my permissions changes.

> **Ship revision 1 without the table** — I write the report with every other generated
> section, and the Carried table as an explicit gap naming the blocked command and the
> reason. `tests/test_report_carried.py` will be red on it, and I state that as a known red
> with its cause rather than a surprise — the reviewer then rules whether the hook or the
> report is what moves.

## What the ruling authorises, and what it does not

**Authorises:** one standalone `process:` commit changing `.claude/hooks/protect-reviews.sh`
so that the Bash clause keys on WRITE INTENT AT A PROTECTED TARGET rather than on a
protected path appearing anywhere in a command that also contains any redirect.

**Does not authorise:** any change to `docs/SUPERVISOR.md`, to `.claude/agents/`, to the
`require-verdict.sh` Stop hook, to `settings.json`'s matcher list, or to what the hook does
on `Write`/`Edit`/`MultiEdit`/`NotebookEdit` — those paths are untouched. It does not
authorise the implementer to write, edit or delete a verdict, which remains refused by the
same hook on exactly the same terms.

## Why the question was asked rather than answered

`CLAUDE.md` § "The reviewer's own instructions are not edited inside a step" makes a change
to `.claude/hooks/` inside a step commit a STOP-class finding, on the stated ground that
*"a reviewer cannot be relied on to notice an instruction that is no longer there."* FM1
forbids constructing a command to get past a hook. The implementer editing the guard that
constrains it is the one move those two rules are built to prevent, so it is not a move the
implementer makes on its own judgement — even when the refusal is plainly an over-refusal
and the fix is plainly small.

## The hook's own record of this failure mode

`protect-reviews.sh` already carries the pattern, in its own words, after three instances:

> THE PATTERN, recorded because it is the third instance: every widening of this rule has
> cost a read and bought nothing, because the implementer's writes here are already caught
> by the narrow forms.

> Over-blocking a WRITE costs nothing; over-blocking a READ costs the ability to work.

This is the fourth instance. The refused command was a read whose output went to the
scratchpad:

    python scripts/carried_table.py docs/reviews/R1/step-3.md <answers.json> > <scratchpad>

and `tests/test_report_carried.py` re-runs that generator and compares its output with what
the report committed, so the table cannot be written by hand instead.

## The condition the hook itself imposes on the change

> THE MATRIX IS RUN IN BOTH DIRECTIONS on every change to this clause, and the run is pasted
> into the commit that makes the change. Four of the four defects in this hook were found by
> someone hitting them, not by the hook being exercised; a guard whose only evidence is that
> it has not fired is not evidence.

The `process:` commit carries that matrix.
