# DIRECTIVE FW

Recorded verbatim on receipt, as the first commit of the turn, under FP0. The text below
is the directive exactly as given; nothing in it is paraphrased, reordered or summarised.

```
DIRECTIVE FW — date, FT2.6 design, the open questions

FW0 — DATE AND SCOPE: Xabier's standing rule is "do not trim" (FQ4). R1 = 10 Nov,
  full scope, FT2.7 included. Record it in R1.md (plan: commit citing FW0).
  Report against it at each reviewed revision.
FW1 — FT2.6 DESIGN RULED: the file and heading go ON Row (self-describing).
  The published CSV gains those two columns. That is a deliberate schema
  change: regenerate every affected deliverable and the golden in the same
  commit (BP0), state the column change in the cover note, and check that no
  numeric cell moved (the golden comparison stays exact on every pre-existing
  column). The rename and atomic conversion are as ruled. Land FT2.6 whole.
FW2 — The FIRST thing in your next message to Xabier: the full text of R885,
  R895 and R1072's two physics questions, each followed by a one-paragraph
  plain-language summary of what is being decided and what each option
  changes in the results. Asked for at FV5 and still not shown. Then carry on.
FW3 — R1084 left open is accepted (no third rewrite of that sentence this
  turn). R1083's lesson stands: an arm's mutation reverts only the repair's
  own clauses. Continue FT2.6 → FT2.7 → the step-3 report → FL3, without
  stopping between items.
```

## What this settles, for a reader reconstructing the decisions

**FW0 answers the escalation CLAUDE.md required and it answers it against trimming.**
The choice was put as *slip to 10 November with full scope, or hold 5-6 November by
moving FT2.7 to R2*. FQ4's standing rule decides it: **do not trim.** R1 is 10 November,
full scope, FT2.7 in. The date goes in `docs/milestones/R1.md` and every reviewed
revision reports against it.

**FW1 rules the one design question FT2.6 could not answer from inside the loop.** The
file and heading ride **on `Row`**, not alongside it, so every row is self-describing and
the report's attribution cannot be forged by a parallel-array slip -- which is the
`npz_files[0]` failure mode the reviewer named. The cost is accepted explicitly: the
published `member_forces.csv` gains two columns, which is a schema change, so every
affected deliverable and its golden are regenerated in the SAME commit under BP0, the
cover note states the column change, and the golden comparison stays EXACT on every
pre-existing column so that no numeric cell is allowed to move behind the schema change.

**FW2 is the third request for the same thing** -- FV5 asked for R885 and R895 in full
text, and the R1072 physics has been escalated since verdict 31. It is not enough to
relay the findings: each gets a plain-language paragraph saying what is being decided and
what each option changes in the results, because the decision is an engineering one and
the person making it should not have to reconstruct it from review prose.

**FW3 accepts R1084 staying open** -- a third rewrite of that one sentence inside a single
turn is the pattern the last five rounds were made of -- and keeps R1083's lesson as a
standing rule on arms: **the mutation reverts only the repair's own clauses**, or the arm
is measuring a neighbour and proves nothing about the repair.
