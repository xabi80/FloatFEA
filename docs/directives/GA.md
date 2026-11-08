# DIRECTIVE GA — apparatus freeze, push discipline, verdict length, reporting, priority

**Received 4 November 2026, inside directive GC, as GC0.** Recorded verbatim on receipt, as
the first commit of the turn, under FP0. **GA was issued earlier in the supervisor channel
and never delivered to this session** — GC0 says so in its own heading, "as originally
issued", and reissues the text so that the record exists. The text below is that text
exactly as given in GC0; nothing in it is paraphrased, reordered or summarised.

**`GA6` is not reproduced here because GC0 does not reproduce it.** GC0's heading states
`GA6 replaced by GC5`, and GC5 is recorded in `GC.md`. No wording for GA6 is invented.

```
GC0 — DIRECTIVE GA (as originally issued; GA6 replaced by GC5)
  GA1 — Apparatus freeze. No new guards, generators, matrix harnesses or
    hook clauses on the review/report apparatus until R1 is tagged. An
    apparatus defect is fixed ONLY if it could hide a blocking finding or
    make a wrong engineering result look green (the R1117 class).
    Otherwise it gets one ledger line, with no investigation and no
    census of sibling sites.
  GA2 — Pushes. Push only immediately before invoking the reviewer (FP1)
    or at end of day. One push per answered round.
  GA3 — Reviewer invocation. For the remaining R1 rounds, the invocation
    asks for:
      - blocking findings in full
      - non-blocking findings as one ledger line each
      - apparatus findings only under the GA1 test
    Target verdict length: 150 lines or fewer. This does not limit what
    the reviewer may rule blocking.
  GA4 — Reporting. FZ digest only, one screen. No running narrative.
    Self-found defects: a count plus one line each. Corrections to your
    own earlier claims: one line each.
  GA5 — Priority is tool function. Any R1 item not yet started that is
    apparatus, or documentation beyond USER_GUIDE.md, goes to R2.
```

## What this file replaces

`GB.md` carried a section headed **"GA IS MISSING FROM THIS RECORD, AND I CANNOT
RECONSTRUCT IT"**, because GB cited `GA4` and `GA5` and no file in the repository held
their text. That was C25 — the defect FP0 was adopted for — one directive letter after
FP0. **It is answered by this file and not by a reconstruction**: the text above came from
Xabier in GC0, not from my memory of what GA might have said.

**One thing in the record does not line up, and I am not resolving it.** GB1 wrote
*"my GA5 said 'step 4, then FL3'. That was my wording, not a ruling."* The `GA5` reissued
above says something else entirely — priority is tool function, apparatus and
documentation beyond `USER_GUIDE.md` go to R2. Those are two different texts under one
number. I do not know whether GA5 carried both, whether GB1's reference was to a sentence
elsewhere in the GA message, or whether the numbering slipped; **GC0 is what Xabier
reissued, so GC0's GA5 is what this file records**, and the discrepancy is noted rather
than silently reconciled.

---

## Both gaps closed, 7 November 2026 (directive GD1)

**The section above is left standing and is answered here.** GD1 supplied both missing
texts from the supervisor's own record, so neither is a reconstruction of mine.

### GA6, verbatim — superseded by GC5, recorded for completeness

```
GA6 — Environment. Xabier will move the repo off OneDrive. When
suite_count.py finishes, apply the append patch, commit, push (GA2), and
state in the digest that everything is pushed and no worktree holds
unpushed work. Then stop for the move. Do not clean up the 33 stale
worktrees; the move makes that moot.
```

**It is spent.** GC5 replaced it, and what it asked for happened: the push state was
confirmed, the digest for 4 November carried the sentence, and the stale worktrees were
left alone — they lived under `%TEMP%` and are simply absent from this clone.

### GA5 — one text, two dates

GD1: *"GA5 as originally issued had two sentences: an order (\"finish step 3, then step 4,
then FL3\") and the R2 rule. GB1 superseded the order sentence (the plan's renumbering
governs). GC0 reissued only the surviving R2 rule. One text, two dates. Nothing to
reconcile."*

**So the discrepancy the section above declined to resolve was not a discrepancy.** GB1's
"my GA5" and GC0's GA5 are the same clause at two points in its life: GB1 quoted the
sentence it was withdrawing, GC0 reissued the sentence that survived. Neither reading I
offered — GA5 carrying both, GB1 pointing elsewhere, the numbering slipping — was right,
and the one I did not offer is that a clause can lose a sentence and keep its number.

**SR-35 is closed in `docs/directives/FZ.md`.** The ruling it recorded was to invent
nothing and say so; that held, and the gap was closed by the author, which is the second
time in four days that declining to guess was what made the correction cheap.
