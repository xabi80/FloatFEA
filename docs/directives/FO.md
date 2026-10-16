# DIRECTIVE FO — revision 3 (last for step 1)

**Provenance: verbatim from the directive message.**

---

FO0 — R814: your proposal is accepted. No density floor. `run` refuses
  exactly two cases:
  (a) any body that admissible() rejects (PSD);
  (b) any member group whose equivalent mass is exactly 0.0 (f = 0),
      without study_only.
  No comparison against DENSITY or any other range bound on a computed value.
  Small f such as 0.0106 is a legitimate input and runs normally; its mass
  table shows the split. Counter-cases: f = 1.0 and 0.999999 refuse (PSD);
  f = 0.0 refuses (degenerate); f = 0.0106 runs and publishes unlabelled;
  patching any removed threshold changes nothing (proves none remains).
  Correct the refusal message so it is true of every value it refuses.
FO1 — FN0's npz half: re-export with λ recorded in the npz, run `--check`
  to completion, and paste both. The golden must still pass byte-identically.
FO2 — R815: all nine caveats in the header; R816: a test that reads the
  published .md and .csv files, not a stub. Each must redden when one caveat
  is removed from the generator.
FO3 — If revision 3's verdict closes step 1 carrying anything, the items go
  into step 2's first commit (no slip). Then step 2 opens immediately.
  Target 28 Oct; report the date the moment it is at risk.

---

## Note on FO0's counter-case, superseded by FP2

FO0's last counter-case — "patching any removed threshold changes nothing (proves none
remains)" — was implemented as a test that reads the guard's own SOURCE TEXT. That became
blocking finding **R820**: reintroducing the same floor through a local binding left the
test green, so the proof did not hold the absence. **FP2 replaced it**: the test must be
able to fail when the floor returns by any route, and it tests the BEHAVIOUR rather than
the source. See `FP.md`.
