# Working the FloatFEA Milestones with Claude Code

The loop below is the HSP audit-driven workflow adapted to a numerical analysis
codebase. The adaptation is small but it matters: on a simulator you can often
see when an answer is wrong, and on a structural tool you frequently cannot.
So the gating moves earlier and the auditors are read-only and adversarial.

---

## The milestone loop

**1. Skeleton plan.** Ask Claude Code for a skeleton plan for the milestone
against `PLAN.md` — what gets built, which gates it must satisfy, what it
depends on. Short. No implementation detail yet.

**2. Review.** You review. The question at this stage is scope and dependency,
not design.

**3. Lock Q&A.** Claude Code asks its open questions; you answer them; the
answers are written into the milestone plan file. This is the step that prevents
the most rework, because an assumption made here silently becomes a defect
found in week six. Force the questions out — if Claude Code has none, that is
usually a sign it has assumed something rather than that the plan is complete.

**4. Detailed plan.** File-by-file, test-by-test. Every gate in the milestone
maps to a named test.

**5. Review and lock.** Once locked, the plan does not change during
implementation. If it turns out to be wrong, implementation stops and the plan
reopens — that is a finding, not a failure.

**6. Execute.** `fe-implementer` builds against the locked plan. Verification
tests are written alongside the code, not after.

**7. Audit.** `verification-auditor` on every milestone. `loads-auditor`
additionally on F1, F3, F4, F5, and any later change to the load path or the
schema. Both are read-only, and both are told to assume the work is wrong. Run
them before you look at the test output yourself, so their verdict is not
anchored to your impression.

**8. Closure.** `docs/closure/F<n>.md`: what was built, gate-by-gate evidence,
what was deferred and why, and every number that moved with its justification.

**9. Merge.** Rebase, fast-forward only.

## Which agent, when

`fe-implementer` writes code and nothing else — it does not judge its own gates.
`verification-auditor` decides whether a milestone closes. `loads-auditor` owns
the physics of the load path specifically, because that is the failure mode most
likely to survive a generic code review.

Keeping the implementer and the auditors separate is the point of the
arrangement. An agent that both writes the test and rules on it has an obvious
incentive problem, and it shows up exactly as widened tolerances and
regenerated golden files.

## The one habit that matters most

**Never let Claude Code close a gate by changing a number.**

The characteristic failure mode of an automated executor on numerical code is
not writing wrong physics — it is making a red test green by the cheapest
available route. A tolerance widened from 1e-6 to 1e-3, a golden file
regenerated, an assertion relaxed from per-case to mean, a parametrisation
quietly trimmed. Each is a small, reasonable-looking diff. Together they hollow
out the verification suite while every build stays green.

`CLAUDE.md` puts every tolerance in one file so this is visible in a diff, and
`verification-auditor` is explicitly instructed to look for it. Your part is to
treat a tolerance change as a finding that needs a physical explanation, every
time, even when it is obviously fine.

## Session hygiene

Start each session by pointing Claude Code at `CLAUDE.md`, `PLAN.md`, and the
current milestone's locked plan. Do not carry a long session across a milestone
boundary — the locked plan is the context, and a stale one competes with it.

Keep the milestone branch narrow. One milestone, one branch, one closure
artifact. F1 is the exception worth planning for, because part of it lands in
HSP under that repo's own gating.

## Getting started this week

Work F1 before F2. It is tempting to start with the beam solver — it is the fun
part, it is self-contained, and it needs nothing from anyone. Resist that. F1
depends on export work in HSP, it is the item most likely to slip, and its
outcome determines what F4 can do. Starting it first converts the schedule risk
into information early, while there is still room to respond.

In order:

**Tag HSP** at the current known-good state and add a second worktree checked
out at that tag. Ask which commit — it is not necessarily the tip of main or the
latest closed milestone, but whatever the in-flight simulator work is actually
validated against. Production FloatSim runs move to that worktree and are untouched by
everything that follows. This is gate G0.3 and it takes ten minutes; do it
before anything else so there is never a window where the working simulator is
at risk. See `docs/hsp-coupling.md`.

**Test replay determinism.** Run FloatSim twice with the same seed and inputs
and compare output bit-for-bit. This is the assumption the entire strip-load
strategy rests on, and it is a one-hour test. Finding out in week one that it
fails costs a fallback decision; finding out in week six costs the schedule.

**Audit the existing output** — gate G1.0. Which channels the `.flr` schema
needs already exist in FloatSim's output files, which need new export, and which
need the replay hook. This may shrink the HSP work to nothing more than the
strip channels, in which case most of the writer is a converter living in
FloatFEA and HSP barely changes.

**Then lock the schema**, including the screening metric list, since the metrics
determine which channels have to exist. Only after the lock does the reader get
written — and by then the beam solver can proceed in parallel, because it
depends on nothing upstream.

## Decisions already locked

**Strip-resolved distributed loads in v1**, generated by two-pass deterministic
replay rather than stored across the full history. Morison drag dominates the
distributed loading and varies strongly along a member; a per-body resultant
would force an assumed distribution into every downstream bending moment.
Rationale in PLAN.md §4, mechanism in `docs/hsp-coupling.md`.

**API RP 2A-WSD for the code checks.** Working stress design keeps each clause
a closed-form equation that can be hand-verified, which is what G6.1 needs.
ISO 19902's partial factors would require load categorisation the screening pass
does not produce. Note that both are jacket codes — F6 is a sizing screen, not a
compliance calculation, and the reports say so on their face.

**No fork of FloatSim.** Tag, worktree, additive-only export, proven by G1.5.

## Still open, and cheap to defer

Whether geometric stiffness enters F2 or waits. Slender braces under axial load
will want P-delta eventually, but the linear model is the thing to verify first
and the addition is confined to the element.

The tier increment for the G5.2 envelope convergence check — how many additional
snapshots constitute a real second tier. Decide it when the first envelope
exists and you can see the distribution, not before.
