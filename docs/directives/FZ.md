# FZ — standing rulings and escalation (reduce round trips)

*Recorded under FP0, verbatim, as the first commit of the turn that received it. Issued by
Xabier, 2026-10-31.*

## The directive, verbatim

```
DIRECTIVE FZ — standing rulings and escalation (reduce round trips)
Record: docs/directives/FZ.md, and link it from CLAUDE.md and
docs/SUPERVISOR.md so every session and the reviewer read it.

PURPOSE: decide covered questions yourself under the rulings below. Do not
stop to ask. Record each self-ruling in the active directive record as
"SR-<n>: question / ruling applied (FZ rule #) / why", then continue.

STANDING RULINGS (apply without asking)
 1. Blocking: FR1 only. A silently wrong published result blocks;
    everything else goes in the ledger, and is fixed in-cycle if cheap.
 2. Inputs: refuse rather than silently adjust. An exact, documented
    equivalence (e.g. 360 ≡ 0) is accepted on both the recorded and the
    declared side, so the two are never asymmetric.
 3. Every new numeric comparison gets a named tolerance in tolerances.py,
    with its justification and a counter-test showing a just-outside
    value is refused. Never widen an existing tolerance.
 4. Physics found wrong in the UNCONSERVATIVE direction: fix it, mark the
    affected published tables/figures SUPERSEDED with a dated note, give
    an old/new ratio table, and report it in the digest. Do not wait for
    approval. CONSERVATIVE-direction errors: ledger, fix if cheap.
 5. Self-found defects: fix, and add a named test row so they can't
    regress. No ruling needed.
 6. Provenance: derived or stand-in values are marked in human-readable
    outputs (report.md, user guide), never by adding keys to
    machine-readable outputs.
 7. Ambiguous directive wording: take the reading consistent with
    existing conventions and tests, record it as an SR, continue. If both
    readings give the same published numbers, pick the simpler one.
 8. Scope: never trim R1. Work outside R1 → ledger for R2.

ESCALATE (stop that item, keep working on others) ONLY for:
 a. Any change to FloatSim/HSP-stable, or running platform_bem.py.
 b. New physical inputs or design assumptions (masses, truss depth,
    materials, geometry).
 c. Changes to the code-check basis (API RP 2A parameters, Fy, K, C_m,
    allowable increases).
 d. Anything requiring a standing constraint to be broken (tolerance
    widened, test skipped/xfailed, force-push, hook bypass, writing to
    docs/reviews/ outside write_verdict.py).
 e. A forecast that R1 slips past 10 Nov.
 f. Two defensible readings that give DIFFERENT published numbers, where
    no convention or test picks one.

DIGEST (replaces per-item reports to the supervisor)
  Once per working day, or at each step completion if sooner, write
  docs/digests/<date>.md and print it. Contents:
    - done (commits, CI state)
    - SRs taken (one line each)
    - superseded published results (rule 4)
    - escalations (a–f), each with your recommended option first
    - next
  Keep it under one screen. Escalations are the only part needing a reply.

Continue the current queue under FZ: FY1/FY2/FY5 test rows and
docstring, golden check, FY3, the step-3 report revision 1, then FL3.
```

## What FZ changes about how this repository is worked

**It replaces asking with deciding, for everything its eight rulings cover**, and it
replaces the per-item report to the supervisor with a once-a-day digest. What it does not
change is the gate: `CLAUDE.md`'s step gating, the reviewer's verdicts and the ES0 revision
cap are untouched, and FZ (d) makes breaking any standing constraint an escalation rather
than a self-ruling.

**The three questions this session had already stopped to ask would now be decided, not
asked** — and recording that is the honest measure of what FZ costs and buys:

* **FX** (the Carried-table generator blocked by a hook) would still be an escalation,
  under FZ (d): a hook bypass is named there explicitly. Asking was right.
* **FY1's `[0, 360)`** would be decided under rule 2's second sentence, which settles the
  recorded/declared asymmetry directly — and would have reached FY5.1's answer without a
  round trip.
* **FY2's derived-height disclosure**, which the FY1/FY2 work named and declined to build,
  is rule 6 exactly: marked in `report.md`, never by a key in a machine-readable output.
  That is FY5.2's answer, reached without asking.

So two of the three round trips this cycle spent were avoidable under FZ and one was not.

## Where self-rulings are recorded, and the first one

FZ says "the active directive record". **This file is that record for FZ-era rulings**, in
a running log below, rather than each SR going into whichever directive file happens to be
newest. The reading and the reason are themselves SR-1.

### SR log

**SR-1: where does an SR get written?**
*Ruling applied:* FZ rule 7 (ambiguous wording → the reading consistent with existing
conventions, recorded as an SR).
*Why:* "the active directive record" has two readings — this file, or the newest directive
file at the time of each ruling. The second scatters a running log across `FY.md`, `FZ.md`
and every later file, so a reader looking for "what did this session decide on its own"
would have to know the directive sequence first. `docs/directives/README.md` is already the
index of the record and points at one file per directive; one SR log in the file that
created the mechanism is the reading consistent with that. No published number depends on
either reading, so rule 7's tie-break — pick the simpler one — also selects this.
