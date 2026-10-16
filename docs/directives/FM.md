# DIRECTIVE FM — R1 rulings; proceed with step 1

**Provenance: verbatim from the directive message.**

---

FM0 — R1.md as written at 472821b is accepted, with this change to §2 / §4
  (plan: commit):
  FG2's premise is NOT checked by a threshold. The sizing analyses
  (required_section, truss_sizing) use fixed forces only to PROPOSE
  candidates. The tool then RE-SOLVES the FE model (static + dynamic) with
  the selected sections and reports max U from that re-solve. If U > 1.0, it
  steps the section up and re-solves, looping until U ≤ 1.0 or the grid is
  exhausted (and then refuses). Report the iteration count and the
  fixed-force vs re-solved max U.
  This is correct for determinate and indeterminate frames alike, and needs
  no new tolerance. Delete the threshold derivation from step 2's lock Q&A.
FM1 — The hook-evasion disclosure in e978a79 is acknowledged. Never construct a
  command to get past a hook. Use Read, or stop and ask.
FM2 — Proceed with step 1 (FL1) without stopping between items. Send the
  example-config golden result and the wall time as soon as they exist.
  Target 28 Oct holds.
