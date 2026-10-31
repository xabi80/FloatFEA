# FY — rulings on FW2 (R885, R895, R1072 Q1/Q2) and FX acceptance

*Recorded under FP0, verbatim, as the first commit of the turn that received it. Issued by
Xabier, 2026-10-31.*

## The directive, verbatim

```
DIRECTIVE FY — rulings on FW2 (R885, R895, R1072 Q1/Q2) and FX acceptance
Record: docs/directives/FY.md (FP0). Order: FY1–FY4 in one cycle, then the
step-3 report (revision 1 of 3), then FL3. R1 target stays 10 Nov.

FY1 — R885 (ledgered): REFUSE, do not normalise.
  - A heading outside [0, 360) is refused. The message names the value
    received, the accepted range and the remedy ("normalise mod 360 under
    the convention in docs/conventions.md:150").
  - Record the decision and its reason in the _validated_wave_basis
    docstring, citing conventions.md:150.
  - Add the signed −10° recording as a test row (refused, exit ≠ 0).
  - Close the ledger entry as "decided: refuse (FY1)".

FY2 — R895 (blocking): CHECK the pair against λ, with a declared tolerance.
  - The 100 m ceiling applies to FULL-scale height. The model ceiling is not
    a separate constant: it is derived as 100/λ.
  - If both model and full heights are recorded:
    |full − model·λ| ≤ tol·full, with tol a named entry in tolerances.py
    (its justification and counter, as for every tolerance). On mismatch,
    refuse at exit ≠ 0.
  - If only one is recorded, derive the other.
  - Add as rows:
      case C: mismatched pair → refused
      case D: "24.2 m full (100.0 m model)" → refused
  - Re-lock R1 §4 if published text changes. Usual caller cycle.
  - Confirm the golden example still gives U = 1.71167.

FY3 — R1072 Q1 + Q2 (blocking, published deliverable per EZ0): FIX BOTH.
  - Q1 allocation: each inclined face carries its in-plane share of shear,
    (V/2)·Lf/h with Lf = √(h² + (b/2)²), not the vertical projection.
    Add a closure assertion across the full grid: the sum of the faces'
    vertical components = V to tolerance (closure 1.000, not 0.447–0.98).
  - Q2 length: brace the inclined face over Lf, not h.
  - Box section must be unchanged. Assert it against the current box
    regression (test_ft25_truss_sizing.py :497, :657).
  - Add the absolute triangle cell at h ≠ b (h = 2, b = 8) as a regression
    row with a hand calculation in the test docstring.
  - Published F6b: mark the triangle tables and figures SUPERSEDED with a
    dated note pointing to the corrected values. Regenerate figures in the
    same commit (BP0, figures pasted last per CP3).
  - In your report, give a table of old vs new triangle diagonal area per
    grid cell (ratio column) so it can be relayed to Xabier.
  - Xabier may override this ruling. If he does, a separate directive
    will say so.

FY4 — FX: ACCEPTED, both parts.
  - The protect-reviews.sh narrowing and the fail-closed guard stay.
  - FX was not issued by the supervisor in this channel. Make sure
    docs/directives/FX.md exists and names its issuer and date. If it
    doesn't, write it now from the record you have.

Standing rules unchanged: FR1/FS1, FV1–FV4, FM1, no force-push, no tolerance
widened, no skip/xfail, docs/reviews/ only via write_verdict.py --judged.
```

## What is already true at the commit that records this

Recorded so the cycle is measured against a known state rather than against an assumption.

* **FY4's second bullet is satisfied as to existence**: `docs/directives/FX.md` exists, at
  `026c9c3`, and names Xabier as issuer. It did **not** carry a date, and the FY4 cycle adds
  one. FX arrived as a selection among three options rather than as a message, which that
  file records and the `README.md` provenance list distinguishes.
* **FY1's outcome is already the behaviour**; what is missing is the three things FY1 asks
  for around it — a message naming value, range and remedy; the recorded reason in the
  docstring; and the signed test row. R885 was ledgered, not blocking, for exactly that
  reason: the outcome is right and only the record is thin.
* **FY2 and FY3 are both open and blocking**, carried by name for many rounds.
* **R1072's defect is in `floatfea/run/truss.py` and inherited verbatim** from
  `scripts/measure/f6b_truss_sizing.py`, already published in
  `results/F6b/truss_sizing.md`. FY3's SUPERSEDED bullet is what addresses the published
  copy.

## One reading FY1 settles and one it leaves to be flagged

`[0, 360)` is half-open as written, so a recorded heading of exactly `360.0` is refused.
`HEADING`'s declared domain today is `0.0..360.0` **inclusive**, and R1100 established that
a *declared* `headings: [360.0]` is accepted and compared modulo 360 — so implementing FY1
as written makes the recorded side stricter than the declared side at exactly one value.

That asymmetry may be intended: a recorded `360.0` is an exporter writing a direction it
could have written as `0.0`, which is the same class of thing as a recorded `-10.0`. It is
implemented as the directive words it, and the commit reports what the change newly
refuses, so that if `[0, 360]` was meant the correction is one character.
