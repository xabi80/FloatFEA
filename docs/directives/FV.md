# DIRECTIVE FV — pace, isolation, the open process items

Received 28 October 2026. Verbatim, recorded before any of it is acted on (FP0).

```
DIRECTIVE FV — pace, isolation, the open process items

FV0 — DATE FIRST: open your next message to Xabier with the remaining items
  (FT2.3 close, FT2.4–FT2.7, the step-3 report, FL3's guide and witness), an
  estimate per item, and the R1 finish date. Asked for at FT3 and FU2 and
  still not given.
FV1 — LOCAL TEST SCOPE (replaces R1047's local requirement; CLAUDE.md, a
  standalone process: commit citing FV1). Before a commit, run locally:
  - the tests of every module the diff touches;
  - tests/unit;
  - the four root guards;
  - any regression test that reads a deliverable the diff regenerates.
  The WHOLE of tests/regression is CI's job at the pushed sha (CZ1 already
  requires it green). A CI-only red is fixed in the next commit (FF0 class)
  before any other work. State the local selection in the commit, as now.
FV2 — ISOLATION: the gating-supervisor works in its own git worktree or clone,
  never in the implementer's working tree. It never runs checkout, reset or
  any write in the implementer's tree. Put it in its definition and in
  docs/SUPERVISOR.md (a standalone process: commit citing FV2).
FV3 — R1049 (FF0): write_verdict.py takes a REQUIRED --judged <sha>, stamps
  that, and refuses if the sha is not an ancestor of HEAD. It never stamps
  HEAD implicitly. Correct verdict 26's anchor by an addendum entry written
  with the tool (no edit of verdict content). A standalone process: commit
  citing FV3.
FV4 — R1039: the gating-supervisor's definition and docs/SUPERVISOR.md cite
  FR1's blocking criterion and FS1's predicate; the superseded CZ0 head and
  EG3 lists are removed (cite, don't copy, as FE1). A standalone process:
  commit citing FV4. The reviewer confirms it by diff.
FV5 — R885 and R895: paste each one's full text in your next message, so I can
  rule on them. Then continue FT2.4 → FT2.7 without stopping between items.
```

## What each clause settles

**FV0** is the third request for the same thing — FT3 asked for it, FU2 asked again, and
neither was answered in a message to Xabier. It is answered in the message this commit's
turn produces, not here and not in a report.

**FV1 REPLACES R1047's local requirement**, which was "any diff touching `floatfea/` runs
the WHOLE of `tests/regression`". That rule came out of a stale published count shipping,
and it has cost roughly thirty minutes of wall time per commit since. FV1 keeps the
coverage where it is cheap — CI at the pushed sha, which CZ1 already requires green — and
narrows the local run to the modules the diff touches plus the standing guards. **A CI-only
red is an FF0-class item: fixed in the next commit before any other work.**

**FV2** answers the hazard this session measured twice from both sides. The reviewer runs
in the implementer's checkout today: it ran `git checkout --` there once, reverting work in
flight, and the addendum to verdict 29 recorded the reviewer reading a WORKING file to check
a claim about a COMMIT — which is R1050 committed from the reviewer's side. A separate
worktree makes both impossible by construction rather than by discipline.

**FV3** closes R1049, which has been open and escalated for several rounds:
`scripts/write_verdict.py` stamps `HEAD` at the moment of writing rather than the commit the
verdict judges, so every verdict's anchor line is correct only by coincidence. The reviewer
has been writing the judged sha into the body by hand as a stopgap and saying so.

**FV4** closes R1039. `grep -c FR1` is 0 in both `docs/SUPERVISOR.md` and the
gating-supervisor's own definition, so the criterion the reviewer is required to rule under
is absent from the files that tell it what to read; it has been ruling under `CLAUDE.md`
instead, as that file instructs, and relaying the gap for three consecutive rounds.

**FV5** unblocks the two findings that have been escalated longest. Neither is the
implementer's to decide: R885 asks what FloatSim actually exports, and R895 asks which of
two conventions a published column follows.
