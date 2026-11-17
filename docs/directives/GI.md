# DIRECTIVE GI — open R2: closed-loop mass/structure optimisation with FloatSim

*Recorded verbatim under FP0, 17 November 2026, as the first commit of the turn that acts on
it. The text below is the directive as received, unaltered. Provenance: pasted directive
message from Xabier. See `docs/directives/README.md`.*

---

DIRECTIVE GI — open R2: closed-loop mass/structure optimisation with FloatSim
Record: docs/directives/GI.md. This opens R2 and supersedes GG4's park
and GH's ban on running FloatSim.

GI0 — Goal (Xabier, 17 Nov): FloatFEA runs FloatSim itself and sizes the
  platform and hub arms in a closed loop:
    sections → steel mass → body mass and inertia → FloatSim → export
    → FE + sizing → sections
  The loop repeats until it converges.

GI1 — Standing constraints, as changed by Xabier:
  - AUTHORISED: running FloatSim time-domain simulations from the pinned
    HSP worktree (tag floatfea-ref-1). It is read-only on HSP source.
    Every output goes to FloatFEA's own run folder, never into the
    worktree.
  - STILL FORBIDDEN: running platform_bem.py, writing to HSP-stable, and
    editing FloatSim source. If the loop needs a FloatSim change (e.g. a
    way to accept mass/inertia overrides), escalate with the minimal
    proposed diff. That is a conversation with Xabier.
  - The deck stays DO-NOT-HAND-EDIT. Mass changes go through HSP's deck
    builder with a declared override file, as ER0 did.
  - Unchanged: no force-push, no tolerance widening, no skip/xfail, FM1,
    and the docs/reviews/ write rule.

GI2 — Process for R2 (lighter than R1):
  - GA1–GA5 carry over (apparatus freeze, push batching, short verdicts,
    one-screen daily digest, tool function first).
  - The reviewer is invoked once per step close, with at most 3
    revisions. No per-commit review.
  - Blocking stays FR1: a silently wrong result.
  - First commit: docs/milestones/R2.md written from this directive. The
    reviewer locks it in one round before any step-1 code.
  - R2's first report answers the newest verdict BY SHA (63affd1 or
    later) and carries verdicts 55 onward (R1202).

GI3 — Step 0: measure only, no tool code. Report in one screen:
  a. Per member, the share of the governing load that is inertial
     (from the body's own mass × acceleration) versus joint reaction. The
     npz carries m_xddot and accel. This says how sensitive sizing is to
     mass.
  b. Wall time of ONE FloatSim run at the R1 config, and the projected
     cost of one loop iteration over all headings and sea states.
  c. How mass and inertia enter HSP's deck builder, and whether an
     override path exists without editing FloatSim source. If none does,
     escalate per GI1 with the minimal diff.
  d. Which bodies carry buoyancy and where ballast could sit, so draft
     can be held (GI4 D2).
  e. Fix hsp_pin.HSP_WORKTREE. It does not resolve from C:\dev\floatfea.
     Make it a config key with an env-var fallback, pointing at the
     existing floatfea-ref-1 worktree. This is the only code allowed in
     step 0.

GI4 — Decisions. Provisional defaults; Xabier may override before step 2:
  D1 Body mass = m_nonstruct + k × m_steel(sized sections × length ×
     7850 kg/m³). m_nonstruct is fixed at (1 − f) × today's deck mass:
     625 t platform, 375 t per hub (full scale). k = 1.0, a placeholder
     marked like the R1 placeholders. Inertia is computed from the
     member steel's geometry plus a fixed non-structural part. It is not
     scaled.
  D2 Draft is held. Every floating body (or the buoy carrying a changed
     body) gets compensating ballast, so its equilibrium draft and trim
     stay at the BEM reference. Each iteration checks the static
     equilibrium against the BEM reference with a declared tolerance in
     tolerances.py, and REFUSES on drift: a BEM used off its draft is a
     silently wrong result. Report the ballast mass and position per
     iteration.
  D3 Convergence:
       - every body's mass changes by < 0.5% between iterations
       - the sized section of every group is unchanged
       - the governing U moves by < 0.01
     At most 8 iterations. If it oscillates (2-cycle), apply 0.5
     under-relaxation to the mass update and say so. If it still fails,
     stop and report. Never report a non-converged result as a design.
  D4 Each iteration uses every heading and sea state in the R1 config.
     If step 0's timing makes that impractical, propose a working set
     (the governing headings from the previous iteration) with a final
     verification pass on the full set, and escalate the choice.
  D5 Sizing rules are unchanged from R1: API RP 2A-WSD, D/t ≤ 300, the
     candidate grid, and the re-solve loop.

GI5 — Steps (the plan in R2.md follows this order):
  Step 1 — Export (FL2(c)). `floatfea export` produces the
    dynamic-inputs file from a FloatSim npz. Acceptance: exporting the
    reference run reproduces the golden dynamic-inputs file, and
    `floatfea run` on it gives U = 1.71167.
  Step 2 — Mass model and FloatSim invocation.
    - Implement D1 and D2. FloatFEA writes the override file, builds the
      deck and runs FloatSim.
    - Zero-change test: feeding today's masses reproduces the reference
      run within FloatSim's own determinism (bit-identical on one
      platform, per Q8).
    - Bookkeeping test: the sum of member steel + non-structural +
      ballast = body mass, exactly.
    - Draft check: a deliberately un-ballasted case is refused.
  Step 3 — `floatfea optimize`.
    - Runs the loop to D3, with an iteration table: masses, ballast,
      governing member/U/heading, sections changed, FloatSim run ids,
      wall time.
    - Output is the converged design plus the full history.
    - Acceptance: a small case converges, and an artificially oscillating
      case triggers relaxation and is reported.
  Step 4 — USER_GUIDE.md section for the loop, plus a fresh-agent witness
    that runs `floatfea optimize` from the guide alone.

GI6 — Report after step 0 and stop. Xabier confirms or overrides D1–D4
  before step 2 code.
