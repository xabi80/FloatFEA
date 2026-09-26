# Review — F2 step 6
Reviewed commit: df594651e6f818b935e8ae1601c5040b9a908972
Verdict: HOLD

**Reviewed commit: `6cc6b07`.** Sixtieth verdict, and the **first round against the
re-locked plan** -- see *On the criterion* below for why I read the clock that way,
and how to convert this verdict without spending a round if Xabier reads it the
other way. The `Reviewed commit:` line stamped at the top of this file by
`scripts/write_verdict.py` is my corpus commit, not the commit judged (R513,
unchanged).

Tests: **2511 passed, 0 failed, 0 skipped** -- my run, clean tree at `6cc6b07`,
`python -m pytest -q`, 608.56 s, Python 3.13 on Windows. 2 warnings, both
pre-existing: the overflow is raised by `orient_norm_overflow`, a deliberate g22
corpus entry.

**THE SIX RED FRAMES: CHECKED THE WAY YOU ASKED.** They are green because the
assertion is gone, and nothing was tuned.

```
cmd  git diff 136e77d..6cc6b07 -- floatfea/tolerances.py
out  (empty) -- not one line, so not one value
cmd  git diff 136e77d..6cc6b07 --stat -- floatfea
out  (empty) -- floatfea/ received no change of any kind this round
cmd  the hunk that clears them, 96c5607 in test_rigid_body_corpus.py
out  -    assert worst <= RIGID_MODE_EXACTNESS, (...)
     +    print(f"  {entry['id']}: retired assembled residual {worst:.4e}")
judge THE RIGHT MECHANISM FOR THE RULING YOU WERE GIVEN, and the wrong one would
     have been a ceiling edit. You reported the failure and then removed the
     claim by ruling instead of moving the number. I have no vote on the ruling
     and I am not re-litigating it.
```

## Item 1b -- CHECKED, AND CLEAN

```
cmd  the newest Answers line in the report under review
out  docs/reports/F2/step-6.md:2281 -- Answers: verdict 59 @ 136e77d
cmd  the newest verdict in the repository before this one
out  verdict 59, committed at 136e77d, STOP @ acbbd0a
judge THE HEADER NAMES THE LATEST. One comparison, made, it matches, and every
     Carried claim below is about the right list.
```

## CI at the reviewed commit (3b) -- GREEN, and the report says there is none

```
cmd  gh run list --commit 6cc6b07 --json name,conclusion,workflowName
out  [] at the moment the report was written; A RUN EXISTS NOW
cmd  gh run list --limit 8 --json databaseId,headSha,conclusion,status
out  36256042985  head 6cc6b07  event push  status completed  conclusion SUCCESS
cmd  gh run view 36256042985 --json jobs
out  the verification ladder    success  13 steps  16:36:16Z -> 16:39:13Z
     lint, unit and guards      success  14 steps  16:36:16Z -> 16:47:27Z
     CI determinism -- leg      skipped  (workflow_dispatch only, by design)
judge COMPLETED SUCCESS AT THE COMMIT I AM JUDGING, on a machine neither of us
     controls, with real runners and real step counts -- not CK2, not a
     two-second empty job. This is the first green CI in this step and it is the
     strongest single fact in the round. `paths-ignore` did not skip it because
     the push carried b047dc2 (tests/) as well as 6cc6b07 (docs/reports only).
judge THE REPORT'S OWN CI SENTENCE IS THEREFORE FALSE IN THE PESSIMISTIC
     DIRECTION -- "no run at 6cc6b07 (docs-only, paths-ignore)". It was true
     when written, three seconds before the push created 36256042985. Closure
     item, recorded because the CI line is the one report figure I never take on
     trust.
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, eleventh round.
```

## My own instructions (4b), conftest (4c), tolerance values (4)

```
cmd  git diff 136e77d..6cc6b07 -- .claude docs/SUPERVISOR.md
out  (empty). NOT A STOP on this head.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction's own expectation, met
cmd  git diff 136e77d..6cc6b07 -- tests/conftest.py "tests/**/conftest.py"
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No rung's green is written by code
     in its own directory and no plugin was added this round, so the CH2/CI0
     channel is closed by inspection rather than by a gate.
cmd  every NAME: Final[...] = value at 136e77d and at 6cc6b07
out  48 and 48; added [] removed [] changed []. NOT ONE VALUE MOVED.
```

## Carried

Verdict 59 was a STOP carrying **R524** (STOP-class) and **R525** (blocking),
R526 to R529 as closure items, R475 / R487 / R488 / R492 / R493 / R500 / R501 /
R513 / R519 to R523 as open on top, and six closing conditions.

- **R524 -- ANSWERED, and by the exit I did not list.** I named three exits
  (derive the bound, change the quantity, enumerate the domain); Xabier took a
  fourth, which is to drop the claim. `docs/milestones/F2.md` section 5d states
  it, names section D2 and line 1849 as superseded, tabulates the four assembled
  forms with the axis each broke on, and records the element-local measurements.
  **I reproduced the element-local figures independently**: 1592 distinct corpus
  elements, clean worst `1.1999e-16` = `0.540 eps`, and `1e-15 / worst = 8.334`.
  Your numbers are right to four figures. The three sites the condition named --
  `F2.md:1849`, `:1331` and `floatfea/tolerances.py:328` -- are all untouched;
  the first two are explicitly superseded by section 5d and I accept that,
  **the third is not superseded anywhere in its own file and is R530.**
- **R525 -- ANSWERED by retirement.** The near-vertical cell is gone from
  `tests/verification/rung1/test_rigid_body_modes.py` and from
  `tests/goldens/collected_tests.txt`, and the band it was named for is now
  covered by the element-local diagnostic at `0.007` to `0.035 eps`. The report's
  section 1 figures for it are withdrawn with it. Correct disposition.
- **R526 -- OPEN closure item, and now worse than when I wrote it.** Both controls
  still decide by the retired quantity against `RIGID_MODE_EXACTNESS`
  (`test_rigid_body_modes.py:695`, `test_rigid_body_corpus.py:322`), and the gate
  they control no longer exists at all. Not re-reviewed; it appears in R530's site
  list only because that is where the stranded constant is still read.
- **R527 -- OPEN closure item**, unchanged: the `not any(numerator[~live] > 0)`
  assertion at `test_rigid_body_modes.py:285-298` still cannot fail. The report's
  section 3 declares all fourteen named lines as left, so the site-by-site rule
  is met.
- **R528 -- ANSWERED**, withdrawn with R525's cell.
- **R529, R519, R521, R522, R513 -- OPEN**, unchanged, none re-reviewed. R519's
  shape is live again: section 3's row for `floatfea/tolerances.py:328` reads "the
  sentences the finding names are restored by reverting the DB1 prose commit",
  which is boilerplate from a different finding and is not a reason.
- **R475 and R487's subjects were DELETED this round** -- the ten span cells, the
  reference-point cell and the structural-half cell. R475's span property is no
  longer a property of any shipped quantity, so that item closes by the quantity
  leaving rather than by being answered. R487's assertion survives as R527.
  **R488, R492, R493, R500, R501 -- OPEN**, unchanged.
- **Condition 1 (Q7 reopens, three named sites) -- TWO OF THREE.** R524 above and
  R530 below.
- **Condition 2 (the re-derivation measured over the near-vertical band) -- MET**,
  and I widened it to 1344 unseen defect-free frames, 0 over the bound.
- **Condition 3 (R525) -- MET** by retirement.
- **Condition 4 (the six red entries answered by the re-lock, not by a corpus
  edit) -- MET.** `tests/corpus/g21_rigid_body_frames.txt` is untouched by the
  implementer; the entries stand and their `shipped_gate=false_red` fields now
  describe a retired quantity, which is the honest outcome.
- **Condition 5 (`0 failed` locally, completed SUCCESS on CI) -- MET.** 2511
  passed locally; run 36256042985 is SUCCESS at `6cc6b07`.
- **Condition 6 (R526 to R529 are closure items, not re-reviewed) -- MET.**
- **The 48 items frozen in `docs/milestones/F2a.md` section 7 -- OPEN on the
  frozen list**, not re-reviewed item by item.

## Findings

**First, the question you asked me, because it is the one that matters, and the
answer is mostly in your favour.** I went looking for the hole and measured three
things.

```
cell  ONE VARIABLE: the carrier. Over every corpus frame, defect-free, the
      quantity that still decides anything about rigid-body annihilation --
      lambda_6(K_hat)/(||K_hat||*eps), floor-class against RIGID_MODE_BOUND
out   187 frames: worst 1.6536 units against a bound of 199.526 -- 120.7x clear,
      0 over. Worst three: rb_tip_3deg_from_Z_span_x10 1.6536, rb_span_x1000
      1.4614, rb_solid_D13_mm_unit_span_x1e4 1.3295.
cmd   the same over 1344 UNSEEN frames: 4 sections x 6 length units (1e-3..1e6)
      x 7 spans (1e-6..1e8) x 4 orientations (2.87, 3, 6, 35 deg) x subdiv 1,4
out   1344 built, 1344 finite, worst 1.8235 units. 0 OVER THE BOUND. The
      element-local diagnostic over the same set: worst 0.656 eps.
judge SO THE REPLACEMENT IS FLAT ON EVERY AXIS THAT BROKE THE FOUR RESIDUAL
      FORMS -- unit, span, section, subdivision, near-vertical. That is the
      measurement the disposition needed and nobody had taken it. It is not in
      the plan, in the report, or in tolerances.py.
cell  AND THE PRICE, solved rather than sampled. The shipped frame, k[0,0] and
      k[3,3] bisected against lambda_6 > RIGID_MODE_BOUND
out   translational edge 2.7202e-13 of max|K|; rotational edge 1.6809e-12.
      RIGID_MODE_EXACTNESS_COUNTER_DEFECT (1.0e-14) is 0.037x and 0.0059x of
      those, so THE RETIRED COUNTER IS NOW INVISIBLE: lambda_6 reads 6.88 units
      under it, against a bound of 199.526.
judge THE SPECTRAL CARRIER IS 27x TO 168x COARSER THAN THE GATE IT REPLACED for
      this defect shape: a ~200-ULP statement where claim A was a ~1-ULP one. At
      200 ULP of max|K| nothing that matters to a platform is hiding, so I do not
      call that a hole. I call it the number the plan should have published
      instead of a premise carried by nothing.
cell  AND PREMISE 3 IS REAL, which I checked rather than assumed
out   tests/verification/rung1/test_corpus_configurations.py: 203 entries, each
      asserted `worst <= PATCH_TEST_EXACTNESS` at :767 AND reddened per entry
      under every injected defect at :1050-1087. G2.2's corpus IS per-entry gated
      with counters.
judge SO "G2.1 in F2 is the lambda_7 bound plus G2.2's coverage" is a defensible
      sentence about G2.2's half. It is not a true one about the lambda_7 half --
      R531.
```

---

**R530. (BLOCKS -- (b).) `floatfea/tolerances.py` STILL DESCRIBES THE GATE THIS
COMMIT DELETED. `RIGID_MODE_EXACTNESS` IS AN ACCURACY CEILING NO ASSERTION
COMPARES AGAINST, ITS COUNTER IS INJECTED NOWHERE, AND ITS ENTRY NAMES A TEST
THIS COMMIT DELETED.**

```
cmd  git diff 136e77d..6cc6b07 -- floatfea/tolerances.py
out  (empty). The file is exactly as it was under the retired gate.
cmd  floatfea/tolerances.py:338, read today
out  "# at five spans each -- `test_BOTH_counters_redden_at_EVERY_span`, ten
     cells."
cmd  grep -rn test_BOTH_counters_redden_at_EVERY_span floatfea tests scripts
out  floatfea/tolerances.py:338 -- THE ONLY HIT. The test was deleted at 96c5607.
cmd  where the guard for exactly this looks
out  tests/test_collected_set_golden.py:203, _citations(), walks ("tests",
     "scripts"). `floatfea/` IS NOT IN ITS DOMAIN -- which is why CI flagged the
     same name six times from tests/ at run 36253525659 and cannot see this one.
cmd  every remaining reader of RIGID_MODE_EXACTNESS_COUNTER_DEFECT
out  tolerances.py (its own entry), the import at test_rigid_body_modes.py:109,
     and the dict at :509 inside counter_response(), which is called only at :838
     and only with "bound" and "retired_floor". NOTHING INJECTS IT.
cmd  tests/test_counters_are_injected.py:142-144, the sentence that authorises
     keeping it
out  "The counter constant ... stays in `tolerances.py` with its entry marked,
     because the diagnostic still injects it when it prints"
out  the diagnostic is test_the_element_local_rigid_residual_is_REPORTED_not_
     asserted; it computes clean values only and names no counter. The entry is
     not marked either. BOTH HALVES OF THAT SENTENCE ARE FALSE.
cmd  tolerances.py:328-331, the reason given for not re-tuning the value
out  "`1e-15` is a decade boundary above the measured worst, and the margin is
     asserted per frame by the corpus test rather than declared here." -- that
     per-frame assertion was deleted in the same commit that left this sentence
     standing.
cmd  the two assertions that DO still read the constant
out  test_rigid_body_modes.py:695 and test_rigid_body_corpus.py:322, both
     `assert weakest > RIGID_MODE_EXACTNESS` -- so the surviving role is a
     discrimination FLOOR two controls must exceed, not an accuracy ceiling. The
     CLASS line at :288 still reads ACCURACY.
judge THIS IS (b) BY THE LETTER -- a tolerance form, its counter, and how the
     counter is injected -- in the one file CLAUDE.md makes the sole home of every
     tolerance in the repository. It is the mirror image of widening: the value
     did not move, the thing it bounds was deleted from under it, and the entry
     reads as reassuringly as it did the day it was true. Condition 1 of verdict
     59 named `:328` and the Reason block at `:316-331` explicitly, and section 3
     of the report declares the site unchanged with a reason copied from another
     finding.
```

  **Closed when**, site by site: (1) the citation at `floatfea/tolerances.py:338`
  resolves or goes; (2) `:328-331` no longer claims a per-frame enforcement that
  does not exist; (3) the entry says what the constant is today -- either
  retired-and-marked in the style the file already uses for `RIGID_BODY_MODE_RATIO`
  and `RIGID_BODY_SUBSPACE_LOSS`, whose records `counter_response` still computes,
  or an explicitly floor-class constant two controls must exceed, with the CLASS
  line matching; (4) the counter entry says where it is injected, or that it is
  injected nowhere in F2 and returns in F3 under section 5e; (5) the two false
  half-sentences at `tests/test_counters_are_injected.py:142-144` are the ones that
  go, not the ones that acquire a new number. **No value moves to close this.**

---

**R531. (BLOCKS -- (c).) `test_G2_1_holds_at_every_frame_in_the_corpus` NOW
ASSERTS `lambda_7 > 0.0` AND NOTHING ELSE. IT PASSES ON THE CORPUS FRAMES WITH A
DEFECT OF `1e+03 x max|K|` RESISTING A RIGID TRANSLATION. THE lambda_7 BOUND IS
NOT ASSERTED PER FRAME ANYWHERE, AND TWO COMMENTS WRITTEN IN THIS COMMIT SAY IT
IS.**

```
cmd  the whole body of the test after 96c5607
out  worst = residual_exactness(k, model); print(...)
     over  = seventh_over_epsilon(k); assert over > 0.0; DECIDED[id] = over
cell A GATE CARRIES ITS OWN FAILURE. One variable: the size of a diagonal
     stiffness on a translational DOF, injected into the assembled matrix, with
     the SHIPPED test function called on three corpus entries
out   defect of max|K|   outcome of the shipped test    lambda_6 units
      0                  PASS                           1.06 - 1.65
      1.0e-14            PASS                           6.87 - 10.9
      1.0e-08            PASS                           7.5e+06 - 1.1e+07
      1.0e-02            PASS                           3.5e+07 - 1.0e+13
      1.0e+00            PASS                           2.9e+07 - 2.5e+13
      1.0e+03            PASS  retired residual 0.998   6.5e+04 - 4.2e+10
judge THERE IS NO DEFECT SIZE AT WHICH IT REDDENS. A rigid motion the matrix
     resists almost completely leaves it green, because lambda_7 > 0 is true of
     any matrix with a seventh eigenvalue. 187 parametrised cases of a rung-1 test
     named "G2_1 holds at every frame" now certify that the model builds.
cmd  test_rigid_body_corpus.py:196-197, added in 96c5607
out  "Claim B, the `lambda_7` bound below, is unchanged and still asserted at
     every frame." -- the assertion below it is `over > 0.0`.
cmd  test_rigid_body_corpus.py:205-209, edited in 96c5607
out  "What is asserted per entry is the RESIDUAL, above, which holds at every
     frame in the corpus including every refused one: the element is under test
     everywhere." -- the residual assertion was deleted eight lines above it, in
     the same commit.
judge AND THAT SECOND SENTENCE IS THE JUSTIFICATION CT2 RESTS ON. The bound is
     not asserted per entry on purpose, because some frames are legitimately
     undecidable -- and what made that acceptable was the residual covering those
     frames anyway. It does not. A refused frame is now asserted on nothing at all.
cmd  how many frames that is, by the shipped split in
     test_the_gate_REFUSES_rather_than_guesses_and_says_how_often
out  refused = lambda_7 < 199.526: 3 of my 15 new entries, and 536 of the 1344
     frames in the wider sweep. Both sets non-empty is all that test asserts.
cmd  the docstring of the same function, untouched
out  "The residual form and the spectral gap, at each of the reviewer frames.
     Asserted on EVERY entry" ... "That is the whole claim: the new form measures
     the element"
judge IT IS (c) AND NOT PROSE: what the gate claims and what it checks are
     different, measured, on the quantity and at the threshold. It is also the
     honest answer to the sufficiency question. The hole is not in the mathematics
     -- it is that section 5d names "the lambda_7 bound" as an assertion the tree
     does not make over the corpus, while the aggregate that DOES carry a 200-ULP
     version of claim A -- the max lambda_6 over the corpus, published as
     `{{fig:rigid_mode_largest_rigid_eigenvalue}}` and floor-class against
     RIGID_MODE_BOUND -- is not named in section 5d at all.
```

  **Closed when** the per-entry corpus test makes an assertion a defect can
  falsify, on a named quantity at a named threshold, over every entry including the
  refused ones. `lambda_6 < RIGID_MODE_BOUND` per entry is available and I have
  measured it green at 109x over all 202 entries; `lambda_7 >= RIGID_MODE_BOUND` on
  the decided set with the refused set enumerated is the other shape; I have no
  vote on which. **And the sentences that describe it are corrected at their
  sites**: `test_rigid_body_corpus.py:196-197`, `:205-209` and the docstring at
  `:164-175`; `floatfea/tolerances.py:359-366`, and the docstrings at
  `test_rigid_body_modes.py:361-370`, `:376-383` and `:556-561`, each of which
  still states that the residual half already proves the six analytic rigid-body
  vectors are annihilated, as the premise the lambda_7 bound stands on. Those six
  sites are one claim, they are the first thing a reader of the F3 gate in section
  5e will read, and they are inside this item rather than in the closure list for
  that reason. **This is a change to an existing test assertion, not new
  apparatus.**

## Closure items (CZ0). None of these is (a), (b), (c) or (d).

**R532. Not one of DG1, DG2, DG4, DH0, DH1, DI0, DI1 or DI2 is recorded anywhere in
this repository before the commit that acts on it, and DG1 and DH1 are not recorded
at all.** `git log -S DG2 -- docs/` returns `11e563e` and `6cc6b07` only. The
load-bearing sentence of the round -- "DG2 was pre-registered before any of this was
measured", at `F2.md:1511` -- is a claim about the process that the repository
cannot check, and the thing it authorises is the removal of a gate that had just
gone red. I believe it; the point is that a reader in F3 cannot. Closed by quoting
the text and date of DG2 in section 5d, and of DG1 and DH1 where they are cited.
The precedent is DD0, which is at least summarised in section 5c.

**R533. The citation guard domain excludes `floatfea/`.**
`tests/test_collected_set_golden.py:203` walks `("tests", "scripts")`. The one file
CLAUDE.md names as the home of every tolerance is outside the reach of the guard
whose whole job is that a named test exists -- which is how the phantom in R530
survived a commit whose message is about fixing exactly that species. Closed by
adding `"floatfea"` to that tuple: a one-word domain fix to an existing guard, not
new apparatus.

**R534. Six helpers and one branch are now unreachable** in
`tests/verification/rung1/test_rigid_body_modes.py`: `_stretched` (:1067), `_defect`
(:520), `_residual_with` (:1093), `_detection_edge` (:1099), `_SPAN_CELLS` (:1063),
`_COUNTER_DOFS` (:1064), and the `"residual"` branch of `counter_response` (:509).
Closed by deleting them or by a caller.

**R535. The retirement comments read as though a linter wrote them.** "THE CLAIM-A
GATE WAS HERE AND IS RETIRED (DI0). Its name is not written out: It asserted claim A
on the assembled matrix." -- six sites in `test_rigid_body_modes.py` at `:551`,
`:799`, `:1116`, `:1121`, `:1128` and `:1135`. Dodging the citation guard is
legitimate; the sentence it produced is not a sentence. Closed by naming the
quantity instead of the name being avoided.

**R536. The two largest numbers in the report are produced by no shipped command.**
"1592 distinct elements" and "298 of 1592 fail at least one counter" sit in a
cmd/out block whose cmd is a description -- "the minimum response per counter over
all 1592 elements" -- and the shipped diagnostic prints over the elements of the
shipped frame only. I reproduced the 1592 and the `0.540 eps` myself and they are
right; **the 298 I could not reproduce, because the three counters it counts against
are not in the tree.** The figure that decides the disposition is the one figure
nothing regenerates. Closed by naming the script, or by moving the count into a form
the tree can re-take.

**R537. The CI section of the report says there is no run at `6cc6b07`.** There is,
and it is SUCCESS. Closed by regenerating section 0.

**R538. R519, R521, R522, R526, R527, R529 and R513 are unchanged**, and not
re-measured here. The shape of R519 recurs in the section 3 row for
`floatfea/tolerances.py:328`.

**R539. `F2.md:1849`, `:1331`, `:1617` and `:2002` still declare the retired
residual as what `RIGID_MODE_EXACTNESS` bounds and as the quantity of G2.1.**
Section 5d supersedes the first two by name, which is enough for a reader who
reaches section 5d; the table row at `:2002` and the "re-measured on CI" at `:1617`
are named by nothing. Closed by editing the four rows, or by naming them in the
supersession list in section 5d.

## Tolerances touched

**NONE. No constant was created, retired, moved, renamed or revalued.**

```
cmd  every NAME: Final[...] = value at 136e77d and at 6cc6b07
out  48 and 48. added [] removed [] changed []
cmd  git diff 136e77d..6cc6b07 -- floatfea/tolerances.py
out  (empty)
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance value touched this round** | -- | -- |

**But `RIGID_MODE_EXACTNESS` is a stranded constant now, and that is R530.** Form:
relative and dimensionless, still correct as arithmetic. Class: declared ACCURACY at
`:288`, used as a discrimination floor by two controls and as a ceiling by nothing.
Counter: `RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1.0e-14`, **injected nowhere**, and
`0.037x` of the bisected detection edge of the quantity that replaced it -- so it
would certify nothing even if something did inject it. Basis: the Reason block at
`:316-331`, which asserts a per-frame enforcement deleted in the commit under review.

## Adversarial corpus (BE3, scoped by DE2 to the element and the gates)

**15 new entries, all unseen by the implementer, committed separately at `df59465`.
`tests/corpus/g21_rigid_body_frames.txt`, batch 9, entries 188 to 202.** The target
is deliberately the NEW carrier rather than the retired one:
`lambda_6(K_hat)/(||K_hat||*eps)`, floor-class against `RIGID_MODE_BOUND`, across
1e-3 to 1e6 in length unit, 1e-6 to 1e8 in span, four sections, subdiv 1 and 4, and
tips at 2.87, 3 and 6 degrees.

```
cmd  grep -c "^id=" tests/corpus/g21_rigid_body_frames.txt
out  202   (187 before this batch)
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py
     tests/test_plan_figures.py tests/test_collected_set_golden.py -q
out  455 passed -- the batch reddens nothing
```

**Coverage measurement, and this round it cuts in your favour on one axis and against
the suite on the other.** 15 new entries. **0 of 15 false-red the surviving carrier**
-- worst `1.8235` units against `199.526`, and 0 of 1344 in the wider sweep behind
the batch. After four normalisations that this file false-reddened, that is a real
result, and it is the first thing I have measured this milestone that argues FOR a
shipped decision rather than against one. **The live shape in the batch is the
refused set: 3 entries whose lambda_7 is under the bound, on which the shipped suite
asserts nothing about the element at all, and the checks in the tree caught 0 of 3.**
The mechanism is not taken on trust: the cell in R531 runs the shipped per-entry test
at defect sizes up to `1e+03 x max|K|` and it passes at every one. The batch moves one
published figure -- `rigid_mode_largest_rigid_eigenvalue` from `1.6536` to `1.8235`
units, still floor-class and still `109x` clear -- which is that figure doing its job.

**And the recheck, because a corpus that is not re-measured is a list.** The six batch
8 entries that were red at `acbbd0a` are green at `6cc6b07`, and I verified it is the
absence of the assertion and not a number: `residual_exactness` still returns
`1.2497e-15` to `2.4727e-15` at those frames, and the test now prints them. Their
`shipped_gate=false_red` fields describe a retired quantity from today; I am leaving
the entries and the fields as the record of why the form changed, per condition 4.

**The counterweight, because right-every-time is not allowed to become a prior: sixty
rounds have found no element defect and this round found none either.** `floatfea/`
received no executable change at all; the element annihilates its own rigid motions to
`0.540 eps` worst over 1592 distinct corpus elements and `0.656 eps` over 1344 unseen
frames. Ladder 5 has still printed `OK -- 0 directories ran` every time it has run and
V5.1 against CalculiX has still not spoken, so **"not yet contradicted" remains the
strongest statement available about the element** -- and it is a weaker statement this
week than last, because the per-frame corpus assertion that was part of "not
contradicted" is the thing R531 is about.

## On the criterion, said once

**I am treating the three-verdict clock as restarted by the re-lock, and this as the
first round against the re-locked plan.** Verdict 59 was the third on step 6 and it
was a STOP: it reopened Q7, and CLAUDE.md section Working agreement says a reopened
plan is reviewed and locked before implementation resumes. Sections 5d, 5e and 5f are
a new locked scope -- claim A dropped, the R486 gate moved to F3, rung 2 narrowed --
and the two items above are findings about THAT scope rather than a fourth pass over
the old one. Both were introduced or left standing by the commits under review.

**If Xabier reads the clock as unbroken, the conversion needs no round and I will not
spend one arguing it:** step 6 closes as PASS at `6cc6b07`, **R530 and R531 carry by
name into the Carried section of step 7 and stay blocking there**, R532 to R539 go
into the closure list, and the disposition is written into this file by hand as
verdict 57 was. What I would ask in exchange is that R531 is answered before the
first measurement of step 7 rather than alongside it, because a step measured against
a rung-1 corpus gate that cannot fail is a step measured against nothing.

**And the schedule.** F2 on 4 October holds on this evidence: CI is green at the
reviewed commit, `floatfea/` is unchanged, and the two open items are one commit of
prose and one assertion between them. V2.5 and V2.6 being explicitly absent rather
than quietly missing is the report doing what DI2 asked.

## Next step opens when

1. **R530 -- `floatfea/tolerances.py` says what its two constants are today**, at the
   five sites named in the item. No value moves.
2. **R531 -- the per-entry corpus gate makes an assertion a defect can falsify**, over
   every entry including the refused ones, and the six sentences describing the old
   premise are corrected at their sites.
3. **R532 to R539 are closure items** and go into one closure commit with the rest of
   the list. Do not re-review them item by item and do not hold anything on them.
4. **`python -m pytest -q` is `0 failed` and `gh run list --commit <sha>` is a
   completed SUCCESS**, on a push that touches `floatfea/` or `tests/` so
   `paths-ignore` does not skip it -- as it was this round.
