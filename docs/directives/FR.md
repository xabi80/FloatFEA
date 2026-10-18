# DIRECTIVE FR — escalation answered: slip, full scope; sharpen the blocking criterion

Received 18 October 2026. Verbatim, recorded before any of it is acted on (FP0).

```
DIRECTIVE FR — escalation answered: slip, full scope; sharpen the blocking
criterion

FR0 — CZ0 ESCALATION (two consecutive steps carrying): Xabier's answer is SLIP,
  NOT TRIM (FQ4). The new R1 target is 5 Nov. Record it in R1.md (plan:
  commit citing FR0).
FR1 — BLOCKING CRITERION FOR THE REST OF R1 (CLAUDE.md, standalone process:
  commit citing FR1):
  A finding BLOCKS only if it can cause a SILENTLY WRONG result: a wrong
  number in a gate, a CSV, a report or any published deliverable (EZ0), or
  an input accepted and used other than as declared. All of these go to the
  R1 ledger and are listed in the closure, but do not block:
  - a refusal whose message is unclear but whose outcome is right;
  - a census, needle or grep that is too narrow where no wrong result follows;
  - report prose and figure wording;
  - closure items.
  The reviewer states, for each blocking finding, the silently wrong result
  it produces.
FR2 — STEP 2 CLOSES at revision 3, with R841 (if it meets FR1) and whatever of
  R838 / R839 / R842 meets FR1. The rest is ledgered, C26–C42 included.
  C42 (U+FFFD in historical verdict headers) is ledgered for the reviewer;
  you do not touch verdict content.
FR3 — STEP 3 = FL2, complete, as FQ4: member topology from config;
  required_section and truss_sizing in `floatfea run` with FM0's re-solve
  loop; headings with the BEM refusal; the period-band check. Build ALL of it
  before the first reviewed revision. Interim checks run as the hook requires
  and count against no round. Fix only FR1-blocking items from them, and
  ledger the rest.
FR4 — STEP 4 = FL3 (the guide and the witness).
FR5 — The reviewer commits its own verdict file, path-limited; you push. No
  hook workarounds (FM1). Report progress against 5 Nov at each reviewed
  revision.
```

## Provenance

Verbatim from Xabier's message of 18 October 2026, pasted without alteration.
Nothing in this file is reconstructed; compare `FL.md`, whose own provenance note
records that it was rebuilt from a session summary rather than from the directive
text.

## What it changes, for a reader who finds this file first

**FR0 answers the escalation CLAUDE.md § Step gating requires** when two consecutive
steps close carrying blocking items. The choice was stated as *slip 5 November, or
reduce FL2's scope*; the answer is slip, and FQ4's "do not trim" stands. The target
moves from 28 October to **5 November** and is recorded in `docs/milestones/R1.md`.

**FR1 narrows what may consume a round for the rest of R1.** CZ0's four heads stay in
CLAUDE.md as the general rule; FR1 is the R1-specific sharpening, and the operative
test is whether a finding **can cause a silently wrong result**. The four named
non-blocking classes are the ones the preceding rounds actually spent themselves on —
a message's wording, a census needle, report prose, and closure items — and each of
those findings was real. The reviewer now states, per blocking finding, which
silently wrong result it produces, which is the sentence that makes the criterion
checkable rather than a matter of taste.

**FR2 renumbers the remaining steps.** Step 2 closes at revision 3. FL2 becomes
step 3 and FL3 becomes step 4, where the locked plan's §3 had FL2 as step 2's gate
and FL3 as step 3. The plan is amended accordingly, citing FR3 and FR4.

**FR3 changes the order of work inside a step.** All of FL2 is built before the first
reviewed revision, with interim checks absorbing the turn boundaries under ES0. Only
FR1-blocking items from those checks are fixed in flight; the rest are ledgered. That
is the direct consequence of the measurement both reviewers reached independently —
that the repairs were one line each and the rounds were the cost.
