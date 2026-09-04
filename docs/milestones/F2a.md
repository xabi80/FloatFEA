# F2 step 4a — verification apparatus

**SKELETON PLAN. Not locked. Nothing here is built.**

Written 2026-09-04 under BE1. This is stage one of the loop in `CLAUDE.md`
§ Working agreement: skeleton plan → review → lock Q&A → detailed plan → review
→ build. The next thing that happens to this file is a review, not a commit
under `tests/`.

---

## 1. Why this is a step of its own

The tolerance-literal scanner, `floatfea/testing.py`, the `# not-a-tolerance:`
exemption scheme and the `_MEASURED` registry were built inside step 4, whose
gate is a patch test. They were built in one session, under review pressure, by
the hand that then verified them — with no skeleton plan and no lock Q&A.

Three review rounds of defects came out of that apparatus and none out of the
element. The specific shapes: a scanner measured against fifteen shapes its own
author wrote; a registry of "measured" values that no run produced; ~22 declared
tolerances placed in the argument slot that does not decide the comparison; an
exemption marker that clears a line from inside a string.

They are not element defects and they were never part of what step 4 was for.
Hence a step, hence a plan.

## 2. What this step would build

**A. One comparison, no defaults.** `assert_close(a, b, *, rel, abs, floor)` is
the only comparison permitted in `tests/`. `pytest.approx`, `assert_allclose`,
`allclose`, `isclose`, `assert_array_almost_equal` are banned **by presence**.

The reason is R33 and it is a design decision, not a fix: the scanner failed
because it tried to decide *which slot governs* a comparison. `pytest.approx(x,
rel=1e-14)` is governed by its undeclared `abs=1e-12`; `assert_allclose(a, b,
atol=1e-14)` is governed by numpy's undeclared `rtol=1e-7`. A checker that
reasons about precedence will be wrong again. **Remove the question instead of
answering it.**

**B. A scanner with nothing to reason about.** Flagged by presence:

* any banned comparison name;
* any `tol`/`atol`/`rtol`/`abs`/`rel` keyword outside `assert_close`;
* any numeric constant below 1 in a `Compare`.

Its coverage claim then becomes checkable by enumeration — every construct in
the language that reaches a comparison — rather than by a corpus of examples.

**C. The corpus is the reviewer's.** `tests/corpus/` (BE3, already in force at
`8ba62d3`): test data written by the gating-supervisor, unseen entries added at
every review, and the coverage number is *the reviewer's count of new entries
caught*, never the implementer's planted-shape count.

**D. The exemption, reconsidered from scratch.** The present marker is a bare
substring test on the line. Whether an exemption should exist at all is an open
question below; if it does, it is not a substring.

**E. The ~22 decorative conversions, re-done under A.** They currently declare a
name in a slot that does not decide. Each becomes an `assert_close` call, or is
recorded as not being a tolerance comparison at all.

## 3. Pre-registered, not open

These were settled in BE2 and are not reopened by the lock Q&A:

* **Ban, do not resolve.** No precedence reasoning anywhere in the scanner.
* **`_MEASURED` is dead** (removed at `ab23181`). Measured values live in step
  reports, produced by the run at the report's commit. `tolerances.py` carries
  the ceiling, the counter-case, and where the justification is written.
* **The corpus is authored by the reviewer**, and the implementer's editing
  tools are blocked from `tests/corpus/`.

## 4. Open questions for the lock Q&A

**Q1.** Does `assert_close` take `rel` *and* `abs`, or does a caller pick one?
Two arguments with no defaults is honest but invites `abs=0` as a way to mean
"relative", which is a default wearing a disguise.

**Q2.** What is `floor` for, precisely, and who supplies it? It is what made
R9's control the first negative control this milestone that bites, so it earns
its place — but a floor the caller chooses is another undeclared tolerance.
Candidate: `floor` is always `eps` times a named scale, and the scale is the
argument.

**Q3.** Is any exemption permitted? A scanner with no escape hatch is a scanner
people route around (the mesh-station comparison, the "is this quantity large"
discrimination check). A scanner with a substring hatch is the present defect.
Third option: those comparisons get their own named helper — `assert_exceeds`,
`assert_in_range` — and there is no hatch.

**Q4.** Does the ban extend to `floatfea/` or only `tests/`? Production code has
its own comparisons (`np.allclose` in a validator is not a test tolerance).

**Q5.** What is the enumeration in B checked *against*? "Every construct that
reaches a comparison" is a claim about Python's grammar, and the honest form is
a list of `ast` node types with a stated boundary, not a sentence.

**Q6.** Does the scanner have a `_COUNTER`-shaped obligation of its own — a
mutation that must make it go red — and where does that live?

## 5. What is NOT in this step

* Nothing about the element, the assembly, or the solve.
* No new tolerance values.
* `floatfea/io/reader.py:157,208,225` and `frames.py:358` (R36) are F1 code with
  undeclared thresholds. They are `Carried` into this step, but they are fixed
  **after** the rule is locked, not under the rule that is about to change.

## 6. Exit criteria (draft)

1. Every comparison in `tests/` is an `assert_close` or a named helper from Q3.
2. The scanner's coverage claim is an enumeration with a stated boundary.
3. The reviewer's corpus has been added to at least twice, and the last round's
   new entries were caught by a scanner that did not see them coming.
4. No file in `tests/` or `floatfea/` carries a numeric comparison threshold
   that is not a name from `floatfea/tolerances.py`.
