# DIRECTIVE GJ — rulings on R2 step 0; start step 1

*Recorded verbatim under FP0, 18 November 2026, as the first commit of the turn that acts on
it. The text below is the directive as received, unaltered. Provenance: pasted directive
message from Xabier. See `docs/directives/README.md`.*

**What it answers.** `docs/reports/R2/step-0.md` closed carrying three decisions for Xabier
(§7) — the FQ3 toolchain escalation, the D1-against-GI5-step-2(iii) collision, and D1–D4
confirmation. GJ1 rules the first, GJ2 the second, GJ3 the third. GJ4 opens step 1, GJ5
tightens GI2's review discipline.

---

DIRECTIVE GJ — rulings on R2 step 0; start step 1
Record: docs/directives/GJ.md.

GJ1 — FQ3 toolchain: RESTORE THE LOCK. Do not re-base.
  - Build the FloatSim run environment from
    HSP-runs/requirements-lock.txt exactly (a separate venv is fine).
    Every FloatSim invocation by FloatFEA uses that environment, and
    FloatFEA records its path and lock hash in each run's provenance.
  - Acceptance: the committed dynamic_inputs.npz regenerates
    bit-identically, which clears the FQ3 reds.
  - If a locked version cannot be installed for this Python/OS,
    escalate with the exact pip error. Do not substitute a version.

GJ2 — D1 vs GI5 step 2(iii): the supervisor's error. Corrected
  bookkeeping:
  - Superstructure bodies (platform, hubs):
      m_body = m_nonstruct + k·m_steel
    No ballast term.
  - Buoys:
      m_buoy = m_buoy_dry + m_ballast
    Ballast is solved per buoy so every buoy's static equilibrium
    (draft and trim) stays at the BEM reference within the declared
    tolerance (D2).
  - System check:
      Σ all bodies = displaced mass at design draft
    within the same tolerance, every iteration.
  - Ballast inertia: ballast is a solid at the buoy's lowest admissible
    level. State the assumption in the report.
  - Bookkeeping test = the three identities above, exact at the
    declared tolerance.

GJ3 — D1–D4 confirmed, with changes:
  D1: CONFIRMED. m_nonstruct = 625 t platform, 375 t per hub (full
      scale). k = 1.0, as a marked placeholder.
  D2: CONFIRMED, with ballast in the buoys only (per GJ2).
  D3: Cap raised to 20 iterations. Tolerances unchanged: mass < 0.5%,
      sections unchanged, governing U moves < 0.01. The 2-cycle
      relaxation guard stays as a cheap safety net. Aitken Δ²
      acceleration on body masses is allowed in step 3 behind
      `--accelerate`, default OFF until the acceptance case converges to
      the same design (same sections, U within 0.01) with and without
      it. Report the iteration counts both ways.
  D4: CONFIRMED. Every heading and sea state every iteration. About 26
      min per iteration is acceptable, so no working set.

GJ4 — Step 1 (export) starts now. It never depended on D1–D4. R1243
  carries in as blocking, as recorded.

GJ5 — Review discipline for R2 (tightens GI2):
  a. 3 reviewed revisions per step is a HARD cap. After the third, only
     FR1 items block. Everything else goes to the ledger, and the step
     closes or escalates.
  b. FR1 for R2 means a wrong tool output, a wrong published engineering
     number, or a wrong statement inside a decision item addressed to
     Xabier. Wrong prose elsewhere in a report is a ledger row.
  c. No commits on the work branch while a review is open (GG2). Work
     done meanwhile goes on a local side branch and is merged after the
     verdict. Step 0 broke this twice. A third time gets escalated to
     Xabier.
  d. Step reports: decision items and measured results first, one
     screen. The evidence goes in an appendix.

Report at step 1 close, then continue to step 2 without waiting unless
something escalates.
