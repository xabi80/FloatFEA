# DIRECTIVE GH — acceptance test on the newest FloatSim run (not R2)

*Recorded verbatim under FP0, 10 November 2026, as the first commit of the turn that acts on
it. The text below is the directive as received, unaltered. Provenance: pasted directive
message from Xabier. See `docs/directives/README.md`.*

---

DIRECTIVE GH — acceptance test on the newest FloatSim run (not R2)
Record: docs/directives/GH.md. This is a user test of the R1 tool:
no reviewer, no step report, and no changes to floatfea/, tests/ or
scripts/. R2 stays closed.

GH1 — Find the run.
  - Search Xabier's machine for FloatSim output files (.npz) outside
    this repo, including the HSP/FloatSim folders.
  - List the 5 newest with: path, date, λ, sea state (H, T), headings,
    duration, and whether the bodies match FloatFEA's 5-body layout
    (platform + 4 hubs).
  - Choose the newest one that matches the layout, and say why.
  - Read only. Do not run FloatSim or platform_bem.py, and do not touch
    HSP-stable.

GH2 — Run it the way a user would, following docs/USER_GUIDE.md only.
  - Write the config in an untracked folder, acceptance/GH/ (add it to
    .git/info/exclude, not .gitignore).
  - Structural inputs stay at the R1 placeholders (platform 20 kg,
    hub 12 kg at model scale, f = 0.75, golden-example geometry), unless
    the run itself states different masses. If it does, report the
    mismatch and use the run's values.
  - Run `floatfea run`, then `floatfea export`.

GH3 — If FloatFEA refuses the run: quote the refusal verbatim, say
  whether the refusal is correct, then try the next-newest matching run
  (at most 3 in total). Never edit inputs to get past a refusal, and
  never change tool code.

GH4 — Report, one screen:
  - run used (path, date, λ, H, T, headings)
  - governing member, its U, governing heading and load case
  - top 5 members by U
  - the wave-band check result
  - the required-section and truss-sizing outcomes, with re-solve
    iteration count
  - sanity check: peak loads vs the golden example's run (ratio), and
    whether the masses are consistent between FloatSim and the config
  - guide gaps: every place USER_GUIDE.md was not enough, one line each
    (R2 items, do not fix now)
  - suspected tool bugs: report with evidence, do not fix
  Then stop.
