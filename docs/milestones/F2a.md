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

## 7. The frozen list (CZ0)

**This list is closed.** CZ0 stops new apparatus through F6, so nothing is
added to 4a from here: an item found after this commit is recorded in a verdict
and in the milestone's closure artifact, and it does not enter this plan. The
48 items below are every item open at the fifty-second verdict on step 5,
plus the four recorded there.

The description in each row is the subject its own verdict gave it. Verdict
files are rotated by `scripts/write_verdict.py`, so for the older items the
verdict text no longer exists in the tree and the description is the longest
cell naming the item in `docs/reports/F2/step-4.md` or `step-5.md`. It was
assembled once, by a script in the session scratchpad that is deliberately not
committed -- a frozen list is a list nothing regenerates.

**What this list is worth, measured rather than asserted.** The apparatus these
items would extend was measured twice by the reviewer against defect shapes it
had not seen: 2 of 22 caught at the fifty-first verdict, 1 of 19 at the
fifty-second, and at the second of those, 0 of 19 by the check written for the
shape's own class. That is the number to read before spending a day here. The
ten `False` rows in `_REPORT_SHAPES` in `tests/test_report_carried.py` are the
same fact in the suite: shapes the CI guards do not catch, asserted as not
caught, so that closing one is a deliberate act.

**The control rule has its own number, and CZ1 asks for it here.** The
equality rule in `tests/test_tree_prose_consistent.py` REGISTERS a needle;
it does not demonstrate the needle can be found. Measured at the
fifty-second verdict (R469) against nine unseen defect shapes, each with
its needle registered: **six ship green**, and **zero of the nine** are
refused by `control_defect`, the function the rule lives in. The direction
is still right -- it refuses every re-admission through a plausible-looking
fake control line -- and the mechanism that would close the gap is an item
on this frozen list rather than work to be done now.

**R532 joins this list as frozen apparatus (DK1).** The citation guard
`test_every_test_name_cited_in_prose_exists` walks `("tests", "scripts")` and
therefore cannot see `floatfea/` — which is how `floatfea/tolerances.py` went
on naming `test_BOTH_counters_redden_at_EVERY_span` for two commits after that
test was deleted, and why a human reader caught it rather than the guard. The
fix is one tuple. It is **not applied**, because CZ0 freezes apparatus through
F6 and widening a guard's domain is extending it; the finding is here so that
whoever unfreezes 4a has the one-line change waiting.

The same list already holds the coverage measurements that argue for spending
nothing here: 2 of 22 unseen shapes caught, then 1 of 19, then 0 of 16, then
0 of 13, and REPAIR-STALE at 0 of 13 recorded under DE2 without transcription.

| item | what it is |
|---|---|
| R230 | open — REOPENED BY NAME.** Revision 3 gave it a status only a verdict may give, against that verdict's own words; §0 |
| R231 | open** — a Q8 value, and no Q8 value is written before the canonical render (R293) |
| R244 | open** — Q8 is locked; the drift tolerance is measured on CI under it before any value is written |
| R245 | OPEN, and now UNBLOCKED for the first time. The report says |
| R275 | the alternating measurement. CF1's job must reach ten of ten first |
| R330 | R320's repair added a whole-line exemption on a weaker predicate than the one it replaced.... |
| R331 | A commit message's count, and an unrecorded CI red inside the range. 265b32f's subject says... |
| R332 | R281 is seven files, not three, and the largest is the corpus for this step's own gate. cmd... |
| R347 | no change** — this is `tests/regression/test_exempt_pair_responses.py`, wrapped across a line in the verdict. It is the guard the finding names as the one that  |
| R348 | no change** at this line — the file is touched by R342's repair and the substring assertion is not. Parsing the condition rather than searching it is 4a |
| R349 | no change** — 4a, and narrowed rather than left: §8 is generated now, and by importing the guard's own site list rather than re-deriving it |
| R350 | no change** — the reviewer's file and refused to me. What I could do is §5: the field is decoded rather than compared, so `measured=clean` reads as the synonym  |
| R354 | The cheap-first comment prices a lint red in seconds and not in evidence.... |
| R355 | no change** — 4a. The name promises orders and the body asserts greater-than; the docstring is right that a threshold would re-introduce R326's literal, so the  |
| R356 | no change** — 4a, and it is R351's species in a fourth reader. The fix is one line each and they go together, not one at a time in whichever round notices |
| R357 | no change** — this is the finding's own EXAMPLE of what a suffix match would wrongly hit, not a file in the tree. It is quoted here because the generator reads  |
| R362 | no change** — 4a, and it is the hook's own documented limitation rather than a defect in it. Changing anything under `.claude/` is a standalone `process:` commi |
| R363 | no change** — 4a. Anchoring on the judged commit is the choice the finding calls defensible; what is owed is one docstring sentence saying it is a choice, and i |
| R364 | The scanner's coverage is still two thirds unseen axes, four batches running. My 22 entries... |
| R370 | no change** — 4a. The closure artifact for a CLOSED step is the record of what was published then; regenerating it is a decision about how closure artifacts age |
| R371 | no change** — the content is right and the finding says so; what was wrong was reformatting in the same commit as the content. Reformatting it again now would r |
| R372 | "The dispatch run at this round's head" names a run at the report parent. Report section 4,... |
| R373 | no change** — the reviewer's own tool, and the finding says it is not a path I may write. Recorded at 4a with the fix named there |
| R374 | The scanner coverage is two thirds unseen axes for the fifth consecutive batch, and the shape... |
| R381 | CP4 second species has no magnitude bound, so float("inf") is reported as a tolerance.... |
| R382 | no change** — `.claude/hooks/` changes only in a standalone `process:` commit citing a directive, and the finding quotes the hook's own statement of its limits  |
| R383 | no change** — 4a. A shipped test for the leg predicate goes with the other three 4a items about that same job rather than one per round |
| R384 | no change** — the finding quotes the rule; CQ3 closes the species itself and §5 carries the measurement |
| R390 | The CQ3 species does not reach a tolerance keyword. assert np.isclose(a, b,... |
| R391 | Section 10's out is still not the command's output. git log --oneline 7fd7155..4e79873 prints... |
| R392 | no change** — 4a. It goes with the other items about that generator rather than one per round |
| R393 | no change** — step 6 has not opened and the file does not exist. The finding is about what this log will need when it does |
| R400 | no change** — 4a. The corpus reader raising before its own meta-test can speak is R234's species and goes with the other readers that share it |
| R401 | no change** — 4a. The escaped dot in the citation regex skips a cited test FILE; one character, and it goes with the other 4a items in that file |
| R402 | no change** — the finding quotes the rule about what section 10's output block must be; the omission it names is in the report and is fixed there |
| R410 | no change** — 4a, and it goes with the other items about the report generators rather than one per round |
| R411 | Section 9's git log --oneline block drops a commit that touches floatfea/tolerances.py. git log... |
| R414 | The pin and release controls now exist twice. test_ONE_PINNED_DOF_leaves_FIVE and... |
| R419 | no change** — 4a. The per-entry assertion in this file moved from `isfinite` to `> 0.0` when the quantity changed, which is stronger, but the domain is still as |
| R431 | OPEN, and I can now name the fourth file. The suite line says |
| R432 | carried, and the verdict says nothing further about it here |
| R433 | carried, and the verdict says nothing further about it here |
| R447 | carried, and the verdict says nothing further about it here |
| R458 | no change** — R458 is OPEN and §6 says so. These are the paths the reading's declared scope excludes and does not declare excluded; widening it is not in this r |
| R471 | The generated/hand-written split now keys on a string the implementer types, so R463 moved house rather than closing. |
| R472 | `ci_table_defects()` reads the outcome cell and nothing else, and asks for non-emptiness rather than completeness. |
| R473 | The suite now requires an authenticated `gh` to pass anywhere. |
| R474 | The section 0c out block is not what its cmd prints. |
