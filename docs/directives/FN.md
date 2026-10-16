# DIRECTIVE FN — rulings on R1 step 1's HOLD

**Provenance: verbatim from the directive message.**

---

FN0 — R805 (λ): one source for λ. It reaches the deck build, every Froude
  conversion and the provenance, with no module constant on the run path.
  The dynamic-inputs npz records the λ it was exported at; `run` REFUSES if
  the config's λ differs, naming both. The golden test gains a λ counter-case
  (λ = 25 with a λ = 50 npz must refuse; a λ = 25 synthetic export must scale
  forces by λ³ and the locked moment by λ⁴).
FN1 — R810 (f): `run` REFUSES any body whose distribution fails admissible()
  (PSD), or whose equivalent density falls below the declared floor (f = 0).
  The measurement path stays available only behind an explicit config flag,
  `study_only: true`. With that flag, every output carries "STUDY — NOT FOR
  DESIGN" in its label and header. Counter-cases: f = 1.0, f = 0.999999 and
  f = 0.0 refuse without the flag.
FN2 — R813 AUTHORISED (FF0 class): add the three verdict-dependent names to
  EG3's state (1) list in CLAUDE.md, byte-identical where mirrored, in one
  standalone process: commit citing FN2. Cite bd315a1 (0 failed with a
  verdict present) as the control that establishes the cause.
FN3 — write_verdict.py (FF0 class): generalise the milestone identifier to any
  locked plan in docs/milestones/ (F6, F6a, R1, …). It REFUSES an identifier
  with no locked plan (so `--milestone 1` must refuse, not write into F1/).
  One standalone process: commit citing FN3, with counter-cases. Fix all
  F-assumption sites found, and paste the grep that shows none remain. The
  reviewer writes subsequent R1 verdicts with the tool, not by hand.
FN4 — Then revision 2 on the remaining items, one reviewed revision. Target
  28 Oct holds.

---

## Note on FN1, superseded by FO0

FN1's second condition — "whose equivalent density falls below the declared floor" — was
implemented as a comparison against `config.py`'s `DENSITY` bound on the declared nominal.
That became blocking finding **R814**, because a range bound used as a comparison on a
computed value is a tolerance under another name. **FO0 replaced it**: refuse only an
equivalent mass of exactly `0.0`, with no comparison against any range bound. See
`FO.md`.
