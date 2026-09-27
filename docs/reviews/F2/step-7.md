# Review — F2 step 7
Reviewed commit: e663a886b37722a693de50573db090537ea3c341
Verdict: PASS
Tests: 2757 passed, 15 failed, 0 skipped   (my run, `python -m pytest -q`, 689.86s)

**Sixty-fifth verdict on F2; the second written into this file after step 7's closure
verdict (DD1).** It rules on one commit, `c9a8736`, and on nothing else. **Step 7 stays
closed, F2 stays closed, and this verdict does not disturb verdict 63 at `2c48a4f`.**

The narrow question and its answer:

- **`c9a8736` is comment-only, and I checked it rather than took it.** Nine added lines,
  every one a `#` comment, and the parsed module is byte-identical.
- **Its content is correct. I reproduced every figure independently**, and the withdrawal
  in `docs/closure/F2.md` is earned.
- **The `M.a` gap is NOT (c) against F2. V4.2's specification IS (c), live now, and it
  carries by name into F4.** Finding R550.

```
cmd  git diff 675da6a..HEAD -- floatfea/ | grep -E "^[-+]" | grep -vE "^[-+]\s*#"
out  (no output) -- zero non-comment changed lines
cmd  compare ast.dump(ast.parse(beam.py)) at 675da6a and at HEAD
out  AST identical: True   old 64275d8273f6258f   new 64275d8273f6258f
cmd  git diff 675da6a..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 675da6a..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py     -- CI0: the pathspec resolves, the instruction is not broken
cmd  git diff 675da6a..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)    -- my own instructions are untouched. Not a STOP-class finding.
cmd  git log --oneline 675da6a..HEAD
out  c9a8736 docs: the artifact's inertia-relief reason was FALSE and is withdrawn
     626d168 review: F2 step 7 -- sixty-fourth verdict, PASS @ fdf4fb0
```

**The AST comparison is the check the invocation's grep cannot make.** A grep over
`^[-+]` would pass a line moved *into* a docstring, or a `#` inside a triple-quoted
string that closes it. The parse says no executable line, no assertion, no default
argument and no tolerance moved. **`c9a8736` is inert, and it is acceptable.**

## Carried

From verdict 64 at `fdf4fb0`. **Nothing was answered, and nothing was expected to be --
`c9a8736` is a comment, not a repair.** All six remain open, and all six are in the red
measured at R553.

1. **R546 -- still open.** Three parts of R544 at one commit with `pytest -q` at
   `0 failed` and `lint, unit and guards` SUCCESS. Still red in both places.
   `tests/test_report_guard_states.py:195-211` and the one `print` in the failure path
   are untouched: `git diff 675da6a..HEAD -- tests/` is empty.
2. **R547 -- still open, and now demonstrated rather than argued.** See R554.
3. **R548 -- still open.** The distance-zero hole and the reviewer-tree exemption.
4. **R549 -- still open**, closed by R547.
5. **R545 -- still open**, and correctly not started; DP2 reclassifies it against a
   closed form, which is the right order.
6. **Batch 13's five states -- still open.** `test_the_corpus_and_the_states_agree` is
   red with `built and not in the corpus: []`, and the five unbuilt states plus that
   test are six of the fifteen failures.

**On 1b, checked and recorded rather than applied.** `docs/reports/F2/step-7.md` reads
`Answers: verdict 61 @ 52941f7`, three verdicts behind the latest. That is **not** the
superseded-report state 1b exists to catch: step 7 closed at verdict 63 and has received
tree-verdicts since, so the report legitimately predates them, and no `Carried` list is
being validated against the wrong round. **Applying 1b mechanically here would HOLD a
closed step over a report nobody submitted, which is the DD1 trap verbatim.**

**`c9a8736` has no report at all.** It changed `floatfea/` with no `docs/reports/` entry;
its claim/cmd/out triples arrived in the invocation instead. Same shape as R544's fix.
Not blocking -- a comment is not work a report exists for -- but it is the second
post-closure `floatfea/` touch to arrive without one, and it is why this file keeps
receiving verdicts.

## Findings

**R550. (c) -- V4.2's specification asserts a property I refuted by measurement.
`docs/verification/README.md:102-106`. BLOCKING, against F4, carried by name.**

The row reads: *"A load case built from pure rigid-body acceleration with no external load
produces near-zero internal stress. The sharpest single test of the load path: it fails if
the inertial distribution, the mass matrix, or the inertia relief constraint is wrong, and
it cannot be passed by a broken implementation that happens to balance."*

**The last clause is false, and false by construction rather than by degree.** I did not
take the witness's `1.6e-22`. I measured it through the shipped assembly, and it is not a
small number -- it is exactly zero:

```
rule  V4.2's own words: "it fails if ... the mass matrix ... is wrong"
cell  ONE VARIABLE: one diagonal entry of M. Same K, same a, same assembly, same solve.
cmd   4-element free-free tube, D=0.6 m / t=0.012 m, 4.8 m; rigid rotation about z;
      the load case f = -M.a and the relief term +M.a drawn from the SAME M
out   shipped M               |rhs|inf = 0.000e+00   |u|inf = 0.000e+00
      M +30%   on one dof     |rhs|inf = 0.000e+00   |u|inf = 0.000e+00
      M +1000% on one dof     |rhs|inf = 0.000e+00   |u|inf = 0.000e+00
cmd   the same gate with the load case from an INDEPENDENT body force
out   shipped M               |rhs|inf = 0.000e+00   |u|inf = 0.000e+00
      M +30%   on one dof     |rhs|inf = 5.273e+01   |u|inf = 1.484e-07
      M +1000% on one dof     |rhs|inf = 1.758e+03   |u|inf = 4.947e-06
```

**A mass matrix wrong by a factor of eleven moves the right-hand side by not one bit.**
This is the "a gate carries its own failure" guard: V4.2 as specified passes while
certifying nothing, and a sentence claiming it *cannot* be passed by a broken
implementation is the strongest available form of that error.

**The measurement also supplies what the artifact only prescribes.** `docs/closure/F2.md`
says the load case must come from an independently computed body force. The second cell is
what that buys: the same 30% defect becomes `5.273e+01` N of unbalanced force and
`1.484e-07` m of response. **The remedy is sufficient to make the gate fail, and that is
now a measured number rather than a plan.**

**Closed when** V4.2's row states the provenance of its load case -- that the d'Alembert
load and the relief term may not be drawn from the same `M` -- and either drops the
"cannot be passed by a broken implementation" clause or restates it against the
independent-load-case form. **The ladder is a locked document, so this goes through the
plan and not through a step commit.** It is **not** a STOP today: nothing is implementing
rung 4, and halting F3 step 1 over an F4 row would buy nothing.

---

**R551. The `M.a` gap is NOT (c) against F2 -- answering the invocation's question
directly.**

**F2's own gates are sound.** G2.1 to G2.5 claim what they claim, on quadratic forms and
on eigenproblems, and every one of those claims is true at its threshold. **None of them
claimed to cover `M.a`.** A coverage gap is not a false assertion, and (c) is "what a gate
claims, on which quantity, at what threshold" -- not "what a gate omitted". **F2's closure
is not disturbed and no F2 verdict is withdrawn.**

```
cmd  every use of the shipped mass matrix anywhere in tests/
out  tests/verification/rung2/test_consistent_mass.py    bending_mass x12,
       assemble_mass_dense x5, local_mass x3
     tests/verification/rung2/test_releases_and_links.py local_mass x3
cmd  the form each one reads M through
out  float(v @ m @ v) at :352        phi.T @ m @ phi at :385 and :416
     float(v @ m_global @ v) at releases:439     sla.eigh(k, m) at :497 and :747
     -- a quadratic form or an eigenproblem, every one. NOTHING forms M @ vector.
```

So the new comment's claim `No gate in F2 reads that product` is **true** as measured.
**The gap carries for F3/F4 by name at R550** -- the coverage gap and the false gate row
are one hole seen from two sides, and R550 is the end of it that blocks.

---

**R552. The withdrawal is correct, and my reproduction is sharper than the artifact's on
one point that changes what DP3 must do.** Not blocking.

I transcribed the shape functions by hand from `beam.py`'s module comment and integrated
at 10 Gauss points rather than the code's 4, so the comparison matrix shares no line with
the element under test:

```
cmd   transcription control: my corrected 4x4 against the shipped bending_mass
out   rel = 1.940e-16  -- the reference is verified before anything is compared to it
out      L    L/D      Phi     centre     rel M.a rot   rel M.a trans   rel aTMa
      1.20   2.00   1.7655     node A        22.238%         2.7e-16    1.3e-16
      1.20   2.00   1.7655   10 m away        1.939%         2.7e-16    2.0e-16
      2.00   3.33   0.6356     node A        16.735%         3.7e-16    7.1e-16
      4.00   6.67   0.1589     node A         3.608%         8.2e-16    4.9e-16
     30.00  50.00   0.0028     node A         0.094%         5.6e-16    5.9e-16
cell  one variable, the sign; same section, same spans, same quadrature
```

**Every published figure reproduces to the digit**, including the `10 m away` row, and
every `Phi` matches. The withdrawal stands on its own measurement, not on the witness's.

**Where the artifact is narrower than the truth.** It says the term vanishes "on rigid
vectors". **The blind subspace is `{c3 = 0}`, and it is wider than the rigid one.** My
corpus entry `ma12` -- a non-rigid field `a(x) = x^2` -- is **29.18% wrong in `M.a` and
`2.7e-16` in `aTMa`**, while `ma11`, which leaves that subspace, is `2.5e-02` in the
quadratic form. So `beam.py`'s **pre-existing** paragraph, "the rigid-body inertias and
`Phi^T M Phi` are quadratic forms of vectors whose `c3` is zero", was the correct statement
all along, and the artifact's rigid-vector rendering of it was the narrower wrong one.
**That is the actual mechanism of the mis-borrowing**, and it matters because the blindness
is wider than the fix assumes.

---

**R553. (d) -- the tree is RED at the reviewed commit. Pre-existing, already carried by
name, and NOT caused by `c9a8736`.**

```
cmd   python -m pytest -q 2>&1 | tail -40
out   15 failed, 2757 passed, 2 warnings in 689.86s
cmd   gh run list --commit c9a87361fa7ce81f8fa1fe241d4be676329ab253
out   CI / CI   conclusion=failure   status=completed
cmd   gh run view 36330759278 --json jobs
out   lint, unit and guards         FAILURE   14 steps, 15:46:02 -> 15:57:29
      the verification ladder       SUCCESS   13 steps
      CI determinism -- leg         skipped,  0 steps
      CI determinism -- ten legs    skipped,  0 steps
```

**This is not CK2's allowance-exhausted state.** The job ran eleven minutes and executed
fourteen steps, with a real assertion in the log. It is a real red, and under CA2 a real
red is (d).

**It did not arrive with this commit, and the LADDER IS GREEN.** The failing job is the
guards job. No verification rung is red, so nothing above is uninterpretable.

```
cmd   gh run list --commit fdf4fb0   (the commit verdict 64 reviewed and PASSed)
out   CI / CI   conclusion=failure
```

**Already red one commit earlier.** The fifteen decompose entirely into carried items: one
root (`test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists`),
eight inherited `test_the_guard_survives_the_state[...]` states that fail because the root
leaks into every state's run, five of my batch-13 states that raise `KeyError` because they
are in the corpus and not built, and `test_the_corpus_and_the_states_agree`. **Six of the
fifteen are caused by my own corpus batch 13 and are the coverage measurement working as
designed. Not one of the fifteen is attributable to `c9a8736`'s content.**

**Why this is PASS and not HOLD, stated rather than assumed.** What CA2's HOLD protects is
a step closing on a red. **Step 7 did not close on this red** -- it closed at verdict 63 on
a tree measured green at `2c48a4f`, and the red arrived afterwards, in apparatus items I
raised. A HOLD now would reopen a closed step, which DD1 forbids and which has already cost
this project two verdicts. **So the red is recorded as a blocking carry against the next
step's CLOSURE, which is where it bites, and not as a HOLD on a step that is shut.** I am
not softening a HOLD: there is no open step to hold.

---

**R554. R547 is no longer an argument -- `c9a8736` is its demonstration, and the
demonstrating commit is nine lines of comment.** Not separately blocking; it is R547. This
is the measurement R547 was missing.

```
cmd   git log --format="%h %s" 36b5899..HEAD -- . ":(exclude)tests/corpus" ":(exclude)docs/reviews"
out   c9a8736 docs: the artifact's inertia-relief reason was FALSE and is withdrawn
      fdf4fb0 process: a milestone witness, because the PR witness never ran (DO3)
      efaee67 docs: F2's milestone closure artifact (DO2)
      80735cf R544: the ancestor state plants a real ancestor, selected not fabricated
      901c634 plan: the schedule dates actually move to 5 and 10 October (C22)
```

**A comment-only commit under `floatfea/` is an "implementer commit touching code" to this
guard** -- and so is the milestone closure artifact, and so is a `process:` commit, and so
is a plan re-lock. **Four of the five intruders changed no executable line anywhere in the
repository.** `REVIEWER_TREES = ("tests/corpus", "docs/reviews")` and nothing else is
exempt, so R546's condition -- `pytest -q` at `0 failed` -- cannot be met by any tree that
has had a closure artifact written on it. DP1's `docs/closure/**` exemption is the right
route and it is a guard-fails-false fix, not new apparatus.

**My own corpus commit is correctly excluded**, which I checked rather than assumed,
because a reviewer round that reddens the suite it is measuring would be the worst version
of this:

```
cmd   the same pathspec at HEAD, after e663a88 (corpus batch 14)
out   the same five commits. e663a88 is absent.
```

## Closure items

Not blocking under CZ0. Not to be re-reviewed item by item. Fixed once, in the closure
commit.

- **C28. `floatfea/element/beam.py:214` -- `No gate in F2 reads that product` is an absence
  claim with no triple and no test (CW0).** It is *true* today; I measured it at R551. The
  defect is the form, and its staleness has a date on it: **DP3, F3 step 2, is the `M.a`
  test.** The commit that lands it makes this sentence false inside `floatfea/`, and
  nothing in this tree regenerates a comment. Closed when it is a triple with a registered
  needle in `tests/prose_triple_controls.txt`, or is reduced to the prescription it already
  carries -- "F4's G4.2 has to load its case from an independently computed body force" --
  which claims nothing about the tree and cannot rot.
- **C29. `floatfea/element/beam.py:211-213` -- `22.2% at L/D = 2, 0.09% still at L/D = 50`
  are measurements published in a comment with no rule and no regenerating script (BI3).**
  Both are correct at this commit; I reproduced them. Closed per BI3's own remedy: the
  comment carries the single number it needs plus a pointer to the artifact that
  regenerates it.
- **C30. `scripts/write_verdict.py:11-12` claims a check the 62-line file does not contain
  (CW0).** The docstring says it *"refuses to overwrite a PASS with anything but a fresh
  review of a changed report."*
  ```
  cmd  grep -n "PASS|overwrite|changed|exists()" scripts/write_verdict.py
  out  11,12 the docstring; 25 the VERDICTS tuple; 41 the body-prefix check;
       50 `if not report.exists()` -- "no step report at". No PASS check exists at all.
  ```
  This is in the one script that writes this gate's output, and it is the exact CW0 shape.
  Closed when the sentence is deleted or the refusal is implemented. **I raise it as a
  closure item rather than a block**, while noting it is the borderline CZ0 names: this
  docstring is the only statement anywhere of what the verdict path guarantees.

## Corpus

**`tests/corpus/g42_inertia_relief_ma_products.txt`, batch 14, committed separately at
`e663a88`. Twelve entries, all twelve unseen.**

**Coverage: the shipped F2 gates catch 0 of 12 on the `M.a` product.** The one entry marked
`f2_gate_catches=yes`, `ma10`, is caught **for the wrong reason** -- arithmetic blow-up
within `1e-7` of `Phi = 1`, where the *defective* coefficient matrix has determinant
`L(1 - Phi)/6` and is singular -- and not by the sign it claims to detect. That is the same
false-reason catch `g24_consistent_mass_members.txt` already records. **So the honest number
is 0 of 12.**

**Two holes the entries were written for, both of them warnings for DP3:**

- **`ma08` is a counter that cannot fail.** Rigid translation, `ma_sign_rel = 2.7e-16`. DP3
  plans R541's sign flip as its counter; **on a translation that counter is round-off.** If
  DP3 injects it anywhere but a rotation, the counter passes vacuously and certifies
  nothing -- which is exactly how R541 survived fifteen rounds.
- **The counter carries an operating point, and I solved for the boundary rather than
  sampling one side of it.** D = 0.6 m, t = 12 mm, rotation about node A: the R541 defect in
  `M.a` falls below **10% at L/D = 3.860, 5% at 5.367, 1% at 15.612, 0.1% at 48.604, and
  0.01% at 153.454.** A threshold quoted without its `L/D` is not a number, and a test
  parametrised over slender platform members alone cannot see R541 at all (`ma07`,
  L/D = 200, `5.8861e-05`).

`ma12` is the entry that corrected the mechanism at R552.

## Tolerances touched

**None.** `git diff 675da6a..HEAD -- floatfea/tolerances.py` is empty, and the AST
comparison in the header rules out a tolerance entering as a bare literal or as a default
argument instead. No counter changed, no injection site changed, no golden file changed, no
parametrisation changed, no assertion changed.

## On the criterion rather than on the work -- this goes to Xabier, and I say it once

**Three consecutive verdicts in a closed step's file, none of them about engineering, all
three produced by the apparatus.** Verdict 64 reviewed R544's fix; this one reviews a
comment. Both were required, because a `floatfea/` touch is (a) territory and the `Stop`
hook is right to refuse a turn over it. Both were consumed mostly by guard bookkeeping.

**The specific thing I want ruled on is R546's condition, because I wrote it and it cannot
be met.** `pytest -q` at `0 failed` requires that no commit touching anything outside
`tests/corpus` and `docs/reviews` follow the report's commit -- and a milestone closure
artifact, a `process:` commit, a plan re-lock and a nine-line comment each violate it while
changing no executable line. **The condition I placed on F3 step 1 is unsatisfiable for
reasons that have nothing to do with F3.** DP1 fixes the `docs/closure/**` half; the
comment-only `floatfea/` half and the `process:` half are not yet covered. A rule that goes
red on a comment is a rule that will be worked around, and that is worse than not having it.

**Second, and I am not asking for apparatus: six of the fifteen failures are my own
batch-13 entries the implementer has not built yet.** BE3 makes my corpus red until it is
built, which means **"the suite is green" and "the reviewer has stopped finding shapes" are
currently the same statement.** They should not be. A corpus commit is a measurement; it
should not be able to fail a CI job. The coupling makes the one number that says whether any
of this works cost a red build, and someone above me should make that trade knowingly rather
than inherit it.

**On DP0, which I did not verify and am not ruling on.** The report that FloatSim's pinned
tag has no irregular-sea capability, so DJ2(b)'s twelve JONSWAP runs and its two-run reduced
set are both unreachable, is a scope finding, and sending it to Xabier before starting was
the right call. I note only this: `docs/closure/F1.md:29` already recorded "irregular seas
are Phase 2", and the load-case answer was written past it by everyone who read it, me
included. **That is the carried-dependency failure this entire mechanism exists to prevent,
and it happened in the one class of document the mechanism never re-reads.** The milestone
witness found its sibling in the same class. Both point the same way, and it is the
strongest argument in this verdict for keeping the witness (DO3).

## Next step opens when

**`c9a8736` is ACCEPTED: comment-only, inert, and correct. Step 7 stays closed, F2 stays
closed, verdict 63 at `2c48a4f` remains the closure verdict, and F3 step 1 remains open and
may proceed.** Verdict 64's list is unchanged, with two additions. **F3 step 1 closes
when:**

1. **R546, R547, R548 and R549** -- unchanged from verdict 64, site by site per CLAUDE.md,
   including any site left and why. R547 now has its demonstration (R554): the exemption
   must reach the comment-only and `process:` cases as well as `docs/closure/**`, or the
   condition stays unmeetable and `0 failed` is theatre.
2. **R545** -- unchanged, before any F3 test parametrises G2.4 over a platform member.
3. **Batch 13's five states built, or each refused by name with a reason.** Two of them are
   R548 and stay red until R548 moves.
4. **R550 carried by name into F4 and not lost.** V4.2's row re-specified through the plan
   before G4.2 is written, and **no step report may cite G4.2 as a check on the mass matrix
   until it is.**
5. **DP3's counter registered at a stated operating point, and not injected on a rigid
   translation.** `ma08` and the solved boundary above are the reasons; `2.7e-16` and
   `L/D = 15.612` are the numbers.

**And one condition on the report rather than on the work.** F3 step 1's report states, in
its one hand-written paragraph and on the day it is written, that the tree is red at fifteen
and names the guards job. **A step report written on a red tree that does not say so is the
failure this gate exists for** -- and the whole-suite line cannot carry that message while
the guard producing it is itself the thing that is red.

**Not in this verdict and not reviewed here:** step 7's work, DM0, DM2, DP1 through DP5, and
the `../HSP-stable` pin. The FloatSim wave-capability finding is Xabier's to rule on, not
mine.
