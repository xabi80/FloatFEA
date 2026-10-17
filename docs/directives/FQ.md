# DIRECTIVE FQ — FP2 repairs; full R1 scope (Xabier: do not trim)

**Provenance: verbatim from the directive message.**

---

FQ0 — R827 RULED: API RP 2A-WSD § 3.2.3's third range ends at D/t ≤ 300 (a flat
  value; the ksi form is 1,500/Fy, 3,000/Fy, 300). § 3.2.2(b) applies for
  60 < D/t ≤ 300. "300000/Fy" in FB1 was my error. Refuse D/t > 300 at every
  site, including api_wsd.py:228 and :73–92, and close that open question
  there, citing FQ0. The caveat in the artifact states D/t ≤ 300. A test
  asserts that D/t = 300 is accepted and 300.01 is refused, through the public
  entry points. R819 closes with it.
FQ1 — R825: name-keyed mappings (line_masses, sections.groups, and any other
  mapping whose keys are names) REQUIRE string keys. A non-string constructed
  key (bool, int, float, None) is REFUSED with "quote the name" in the
  message. Delete the str(g) coercion.
FQ2 — R826 / R828: every repair is held by a test that fails when the repair
  is reverted. Show the revert-red-restore cycle for R822, R823, R825, R817
  and R818 (the generator, not the committed file). Paste the cycle.
FQ3 — R829: an empty-basis branch in the CSV path (no contradictory
  sentences). R830: pin numpy and scipy (and every package whose version
  can move a number) in constraints-dev.txt. If the golden moves under the
  pin, STOP and report; do not re-baseline silently.
FQ4 — FULL SCOPE (Xabier, 17 Oct: do not trim). FL2 stays complete: member
  topology from config; required_section and truss_sizing integrated into
  `floatfea run` with FM0's re-solve loop; headings (refusing those the BEM
  database does not cover); the period-band check. Then FL3 (the guide and
  the witness).
FQ5 — DATE: 28 Oct is at risk. In the report carrying FQ0–FQ3, give a
  realistic finish date for R1, with the remaining items and the estimate
  per item. Do not cut verification to meet a date; report the date instead.
  Keep working through items without stopping.

---

## Note on FQ0, which corrects an earlier instruction

FQ0 overrules **FB1's `300000/Fy`**, which Xabier records here as his own error, and with
it the figure this implementer published in three artifacts (`845.1` at Fy = 355) and the
reviewer's bisection finding R827 (`734.3`, measured against the code as it then stood).

**The ceiling is a FLAT `D/t ≤ 300`.** The ksi form of § 3.2.3's ranges is `1,500/Fy`,
`3,000/Fy`, `300` — the first two scale with grade and the third does not, which is the
reading that was lost. `§ 3.2.2(b)` applies for `60 < D/t ≤ 300`.

So the repair is in the CODE and not only in the caveat: every site must refuse above 300,
and the open question `api_wsd.py:73-92` recorded for Xabier is closed by this directive.
