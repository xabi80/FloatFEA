# DIRECTIVE GE — finish R1: witness and closure

Received 8 November 2026. Recorded verbatim on receipt, as the first commit of the turn,
under FP0. The text below is the directive exactly as given; nothing in it is paraphrased,
reordered or summarised.

```
DIRECTIVE GE — finish R1: witness and closure
Record: docs/directives/GE.md.

GE1 — R1173 is the work. In revision 2, nothing else of substance:
  - Run the fresh-agent witness per GC6. It gets ONLY docs/USER_GUIDE.md
    and the repo, with no directives, SR log or digests.
  - It must reproduce the golden example (U = 1.71167) and the other
    fixtures FR4 names, plus one modified config of its own choosing,
    without help.
  - Record the transcript, each fixture's result vs expected, and every
    place it got stuck.
  - Each stuck point is a guide defect: fix the guide, and re-run the
    witness on the fixed guide until a run completes with no help. All
    runs go in the record, not only the last.
  - Write docs/closure/R1.md as FR4 requires, with the transcript(s).
  Then revision 2 to the reviewer.

GE2 — R1168, R1169, R1170: one line each.
  - R1168: give the caveat the guide's qualifier ("with a bending term
    to multiply"), and add the zero-moment member as a row so both
    deliverables are checked against it.
  - R1169: correct SR-48 in place. `git show` is ALLOW, `cp` is DENY,
    and the figure was reproducible.
  - R1170: correct which assertion the ablation reddens.
  No essays. The lesson goes in one line of the digest.

GE3 — R835/R861 (a red count that depends on the newest verdict's
  text): R2 under GA1. It has not hidden a blocking finding since R1117
  was fixed. From now on the reviewer records it as "R835: unchanged,
  R2" in one line and does not re-measure it each round.

GE4 — docs/SUPERVISOR.md's false sentence: fix it in a standalone
  `process:` commit, before revision 2. State what actually happens:
    - write_verdict.py writes the verdict file
    - the reviewer commits it in ITS OWN worktree (FV2)
    - the implementer fast-forwards it in
  Nothing in the main tree is written by the reviewer. If that is not
  what happens today, describe what does happen and escalate rather
  than inventing a procedure.

GE5 — Slow suite: noted. If it costs time again, sample the child, per
  the reviewer. No investigation now.

Target: revision 2 to the reviewer on 10 Nov.
```

## The revision number, resolved rather than asked (FZ rule 7)

**GE says "revision 2" in GE1, GE4 and the target line. The next revision of
`docs/reports/R1/step-4.md` is REVISION 3.** Revision 2 was pushed at `6876854` on
7 November, two days inside GD2's date, and the reviewer passed it at `c88b0c0`; step 4
stands at 1 of 3 reviewed revisions under ES0. GE was written against the state GD2
described, where revision 2 was still owed.

FZ rule 7 resolves ambiguous wording toward existing conventions without asking, and the
convention here is not in doubt: revisions are numbered sequentially within a step and a
reviewed one is not renumbered. **This is not FZ (f)** — no published number differs
between the two readings; the heading on one report section does. So the work GE1 names is
done as revision 3, the target date is read as 10 November for that revision, and the
substance of every clause is taken exactly as written.

## What GE changes about what the previous verdicts asked for

* **R1173 becomes the step's work rather than its closing condition.** Verdict 51 ruled it
  non-blocking under FR1 and the step's closing condition. GE1 puts it first and says
  "nothing else of substance", which also settles what revision 3 is allowed to spend a
  round on.
* **R1168, R1169 and R1170 are capped at one line each** by GE2, against the three rounds
  the `C_m` sentence has already taken. GE2 also adds one thing that is not a line of
  prose: *the zero-moment member as a row*, so the claim is checked rather than reworded.
* **R835/R861 goes to R2 and stops being re-measured** (GE3), ending eleven measurements.
* **`docs/SUPERVISOR.md` is corrected in a standalone `process:` commit** (GE4), which is
  what CLAUDE.md § "The reviewer's own instructions are not edited inside a step" requires
  of any change to that file.
