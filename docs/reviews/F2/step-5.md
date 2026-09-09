# Review — F2 step 5
Reviewed commit: caa2ec5418e3ca3bc22a3f559fb91f1624e25c37
Verdict: HOLD

Tests: 1578 passed, 0 failed, 0 skipped   (my run at `fba8ace`, `python -m pytest -q`,
138.91 s. With my twenty-sixth-round corpus applied at `caa2ec5`: **1578 passed,
0 failed** -- unchanged, and that is itself the coverage measurement: not one of
my twenty entries is executed by anything in the suite.)

**Reviewed code commit: `fba8ace`** (report), over the step commit `d1fea41`.
The header stamp is `caa2ec5`, my own corpus commit, made immediately before this
verdict and touching no code.

First verdict on step 5. Range `aae355a..HEAD`, six commits. The step is well
built and the two things I was asked to rule on are both ruled in the
implementer's favour. **What holds it is a third thing, which I went looking for
because the entry told me where to look: the invariance that is the entire stated
reason for choosing a ratio does not hold, and both shipped ceilings go red on a
DEFECT-FREE element at ordinary configurations of the same model.**

```
cmd  git diff aae355a..HEAD -- .claude docs/SUPERVISOR.md ; and which commit
out  docs/SUPERVISOR.md +7 lines, in b67163f ALONE -- a standalone `process:`
     commit citing BZ0, touching no floatfea/ and no tests/. Additive: seven
     lines added, none removed, no guard deleted. Reviewed line by line. CLEAN.
cmd  git log --name-only aae355a..HEAD ; any commit touching docs/reviews/
out  none. The plan edit is a standalone `plan:` commit; the step commit touches
     no docs/reviews/ and no .claude/.
cmd  grep "^Answers:" docs/reports/F2/step-5.md ; newest verdict
out  "verdict 25 @ aae355a" ; aae355a IS the newest verdict. Item 1b does not
     trigger.
cmd  python -m pytest -q 2>&1 | tail -1
out  1578 passed, 2 warnings in 138.91s   -- the report's count, reproduced
cmd  python -m pytest tests/verification/rung1/test_rigid_body_modes.py -q
out  8 passed   -- report sec.1 reproduced
cmd  python -m pytest tests/test_counters_are_injected.py -q
out  14 passed  -- report sec.4 reproduced, 5 registered x 2 cells + 3 + 1
cmd  python scripts/regen_figures.py --check
out  up to date, exit 0. And the four new figures are thread-stable: identical at
     OMP_NUM_THREADS = 1, 2, 4, 8.
```

## Carried

Step 4 closed on **PASS** at `4ccd166` (verdict 25, `aae355a`), so **nothing
blocking is carried into step 5.** Every open item is 4a, and each is re-checked
rather than read across.

- **R218 -- ANSWERED, at the line its condition named.** The condition was that
  the next report state the suite counts from its own run and say what moved
  them. `docs/reports/F2/step-5.md:151` states `1578 passed, 0 failed, 0
  skipped`; I reproduced it exactly. The movement `1497 -> 1578` is `+81`, and I
  located it rather than accepting it: `+44` in `tests/test_report_carried.py`
  (122 -> 166 parameters, because verdict 25 names more sites than verdict 24),
  `+8` the new gate file, `+4` the two new registrations x two cells, and the
  remainder in the regenerated corpus parametrisation at `2f92c58`. **The report
  states the count and does not state what moved it**, which is half of the
  condition; recorded as **R227** below rather than re-opened, because the
  arrangement's own answer to it is that I collect both ends, and I did.
- **R220 -- HALF ANSWERED, correctly declared as half.** `docs/closure/F2-step4.md`
  carries 60 distinct R-numbers by name (`grep -oE "R[0-9]+" | sort -u | wc -l`
  -> 60). The other half -- `docs/milestones/F2a.md` carrying the list with the
  verdict each item came from -- is untouched (`grep -oE "R[0-9]+"` over F2a.md is
  still empty). The report says exactly this at `:155-157`. Open at 4a, and it
  remains the item that decides whether the other sixty survive.
- **R221 -- OPEN at 4a, and correctly named first by the report.** Untouched this
  step; the ceiling it concerns (`PATCH_TEST_EXACTNESS`) did not move and the
  figures regenerated to the published digits at `2f92c58`
  (`clean_worst_ratio 0.1261x -> 0.2765x`, `corpus_entries 177 -> 187`,
  `boundary_margin_unbracketed 0: none -> 1: ck_cleanmax_x1e8`). The regeneration
  commit message writes **no cause** for the new unbracketed row and says in terms
  that the cause is mine at R222 and is not restated -- which is exactly what the
  twenty-fifth verdict's second `Next step` item asked for. **Closed as an
  instruction; R222 itself stays open.**
- **R222 -- OPEN at 4a**, unchanged. `scripts/regen_figures.py:205` still carries
  the bare dimensional `1.0e9`. It did not become blocking this round: the
  excluded base is still published by name and the dropped margin still lies
  inside the published range.
- **R216, R217, R219 -- OPEN at 4a**, untouched, correctly declared. R216's
  trigger condition did not fire: `counter_headroom_room` is still `2.18x` in the
  regenerated figures and the two typed copies still agree with it.
- **R200--R204, R206, R210, R215 -- OPEN at 4a**, untouched. R201 is the one I was
  asked to run against the new registrations; see the ruling below -- the shipped
  pair is admitted by both cells and the bound is solved.
- **R198, R199, R181, R189, R190, the R170/R171 remainder, R172, R159, R162,
  R151, R152 -- 4a, unchanged.**
- **R134, R135, R137 -- OPEN, UNTOUCHED**, twenty-first round.
- **R129, R131, R132, R136, R138, R139, R148, R113, R95, R97, R98, R100--R103 --
  as declared in `docs/closure/F2-step4.md`.**
- **R124, R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** Still recorded as a disagreement.
- **R6, R16, R25, R30--R33, R36, R50, R52, R62 -- still open**, 4a or later.
- **R68 standard -- MET, tenth round.**
- **The witness channel -- OPEN FOR THE FIRST TIME, and there is still no witness
  comment.** `docs/SUPERVISOR.md:35-40` records the gap honestly and in the right
  direction: steps 1 to 4 have none and never will, twenty-five consecutive
  reviews of step 4 by one reader, and opening the channel now does not repair
  that. **This is the twenty-sixth consecutive review by the same reader.** Step 5
  is the first that can carry a witness comment and it does not yet. Not a pass --
  an unavailable check, correctly labelled as one by the report at `:169-176`.

## Findings

**Two block. Four are recorded at 4a.** The two that block are stated with the
head they touch and what would close them.

**R223. (BLOCKS -- head 1, the gate's assertion, AND head 3, the truth of a
published sentence) The invariance that is the entire stated reason for choosing
the ratio does not hold in two of the three directions it is claimed in, and both
shipped ceilings go red on a DEFECT-FREE element at ordinary configurations.**
`floatfea/tolerances.py:294`; `tests/verification/rung1/test_rigid_body_modes.py:19`
and `:163-165`; `docs/milestones/F2.md:51` and `:1477`.

```
code  tolerances.py:291-294 "the eigenvalues of `K` carry units and scale with
      `E`, with the section and with the mesh, so a ceiling on them would be a
      ceiling on the model. THE RATIO IS INVARIANT UNDER ALL THREE."
code  test_rigid_body_modes.py:19 "A RATIO, per G2.1, so the assertion is MESH-
      AND UNIT-INDEPENDENT"
code  test_rigid_body_modes.py:163-165 (`mode_ratio`) "both eigenvalues carry the
      same units and the same overall scaling, so the ratio is INVARIANT UNDER A
      CHANGE OF `E`, OF SECTION, AND OF THE LENGTH UNIT."
code  F2.md:51, the G2.1 SCOPE CELL "tested as an eigenvalue *ratio* against the
      first flexible mode SO IT IS MESH- AND UNIT-INDEPENDENT"
code  F2.md:1477 "dimensionless, and INVARIANT UNDER ALL THREE."

cell  ONE VARIABLE MOVED AT A TIME, everything else held, through the SHIPPED
      `mode_ratio` and `subspace_loss` on the SHIPPED frame:

      E alone, over fifteen decades (2.1e5 .. 2.1e20 Pa):
        ratio 1.60e-14 .. 3.16e-14      INVARIANT to within 2x. THE CLAIM HOLDS.

      SECTION alone, circular tubes, the mesh and the frame held:
        D=2.00 t=0.200   ratio 7.23e-15   loss 3.35e-15   both pass
        D=0.60 t=0.012   ratio 1.60e-14   loss 5.31e-15   both pass   (shipped)
        D=0.15 t=0.002   ratio 4.73e-13   loss 1.15e-13   *** LOSS RED ***
        D=0.10 t=0.001   ratio 2.18e-13   loss 1.50e-13   *** LOSS RED ***
        D=0.05 t=0.0005  ratio 1.14e-12   loss 6.62e-13   *** BOTH RED ***
      157x across the range, and it crosses BOTH ceilings. NOT INVARIANT.
      A 100 mm x 1 mm brace is not an exotic member; it is bracing.

      MESH alone, each of the seven members subdivided, section and frame held:
        subdiv 1  ratio 1.60e-14  loss 5.31e-15   pass
        subdiv 4  ratio 7.69e-14  loss 7.84e-14   pass  (loss at 0.78 of ceiling)
        subdiv 6  ratio 3.46e-13  loss 1.19e-13   *** LOSS RED ***
        subdiv 8  ratio 1.34e-13  loss 1.46e-13   *** LOSS RED ***
      NOT INVARIANT, and the direction is the wrong one: refining the mesh
      reddens a gate whose scope cell says it is mesh-independent.

      LENGTH UNIT alone -- and I PROVED IT IS A RE-EXPRESSION BEFORE READING IT,
      because a geometric scaling is not a unit change and I did not want to
      confuse the two:
        cmd  K_mm vs 1e3 * P^-1 K_si P^-1, P = diag(1e3 on translations, 1 on
             rotations)
        out  max|difference| / max|K_mm| = 9.715e-16 -- the mm model IS the SI
             model re-expressed. Nothing physical moved.
        1 m = 1 unit    ratio 1.60e-14  loss 5.31e-15   pass
        1 m = 10        ratio 2.28e-13  loss 6.08e-14   pass
        1 m = 30        ratio 1.45e-12  loss 2.69e-13   *** BOTH RED ***
        1 m = 100 (cm)  ratio 2.27e-11  loss 5.32e-12   *** BOTH RED ***
        1 m = 1000 (mm) ratio 2.00e-09  loss 1.32e-09   *** BOTH RED, 2003x ***
      The SAME PHYSICAL STRUCTURE, the SAME element, in centimetres, fails G2.1.
      NOT UNIT-INDEPENDENT.

judge WHY, stated as the measurement and not as a story. The DOF vector is
      dimensionally inhomogeneous -- metres and radians in the same vector -- so a
      change of length unit is a diagonal CONGRUENCE `K -> s P^-1 K P^-1`, not a
      scalar multiple, and no ratio of two eigenvalues survives a congruence. The
      premise at :164, "both eigenvalues carry ... the same overall scaling", is
      the error, and everything downstream of it inherits it.

cell  AND IT IS THE FRAME, NOT THE ELEMENT -- the control that separates them,
      which nothing in the gate computes. The strain energy of the six ANALYTIC
      rigid-body vectors, max over j of (vKv)/(norm(v)^2 max-abs-K), over all
      twenty corpus configurations:
        min 2.44e-22, max 6.25e-17 -- never once above 6.3e-17.
      The element does not move. Meanwhile the two shipped quantities span
      7.2e-15 .. 7.8e-09, a spread of 1.1e+06. Divided by eps * (lambda_max /
      lambda_7) they COLLAPSE: ratio to 16.5x, loss to 8.7x.
      **Both shipped quantities are, to within one order, `eps` times the frame's
      flexible condition number.** `1e-12` and `1e-13` are ceilings on the
      conditioning of one frame, which is what the entry at :293 says a ceiling
      must not be.

cell  and the ceilings hold BY 62x AND 19x AT EXACTLY ONE OPERATING POINT, which
      the two published headroom figures do not name (F2.md:1491-1492, "~62x",
      "~19x"). At the four points nearest the shipped one in my corpus the loss
      sits at 0.78x (subdiv 4), 0.61x (decimetres), 0.20x (subdiv 2) and 1.50x
      (D=0.1) of its ceiling. **The nearest legitimate configuration that reddens
      is a 100 mm x 1 mm brace at the shipped mesh in SI units.**

judge WHY THIS BLOCKS AND IS NOT 4a. It is not prose about apparatus. `F2.md:51`
      is the GATE'S SCOPE CELL -- what R7 reverted a results figure out of,
      precisely so that cell states what the gate proves -- and it states a
      property measurement refutes. The ratio was chosen OVER the eigenvalues for
      this reason and for no other; with the reason gone, what remains is a
      threshold with an unstated operating point, which is the "a ratio carries
      its operating point" guard verbatim. And 13 of 20 defect-free
      configurations are red.

judge WHY IT IS A HOLD AND NOT A STOP, said so it can be argued with. Rung 1 is
      green at the shipped frame; no element defect is implied and none was found
      (see R228's reach table). The two quantities are still the right two, and
      AP3's ordering is confirmed by my own measurement. What is wrong is the
      claim attached to them and the absence of an operating point. That is
      inside step 5. **If the answer is that G2.1 must assert a different quantity
      -- and the energy control above is one that IS frame-insensitive and is
      asserted nowhere -- that is a plan change and it comes back before code
      lands.**
```

**Closed when** each of the five sites either withdraws the invariance claim or
states it in the direction the measurement supports (`E`: holds; section, mesh and
length unit: does not), **and** the two ceilings carry the operating point they
were measured at -- the frame, the section, the mesh and the unit system -- so
that `~62x` is a headroom at a named point rather than a bare factor. The twenty
entries in `tests/corpus/g21_rigid_body_frames.txt` are on disk and the `energy`
column is the control that separates a frame effect from an element one; how the
shapes are caught, or whether they are, is the implementer's.

**R224. (BLOCKS -- head 3, and head 2 because it is a tolerance's justification)
Two sentences in `floatfea/tolerances.py` are refuted by reading the same
paragraph, and each is a claim about a rule this repository earned by failing.**
`floatfea/tolerances.py:296-298` and `:301-309`.

```
code  :296  "measured at the shipped frame, the clean ratio is `1.601e-14`"
code  :298  "... which is the number this entry is checked against AND IS NOT
            RETYPED HERE (R194)."
cmd   grep -n "1.601e-14" floatfea/tolerances.py
out   296 -- the number the line says is not retyped is on the line before it.
code  :305  "    1e-14 -> 3.03e-13     1e-12 -> 3.06e-11     1e-8 -> 3.06e-07"
code  :308-309 "The sweep is in the step report, which is regenerated by rule; IT
            IS NOT TABULATED HERE (BI3)."
cmd   sed -n '305p;308,309p' floatfea/tolerances.py
out   the sweep is tabulated four lines above the line that says it is not.
cmd   grep -nE "5.306e-15|3.06e-11|7.47e-12|7.59e-14" floatfea/tolerances.py
out   :315 :334 :338 :339 :351 -- with :296, SIX generated live figures retyped
      into this file in one commit. All four figure NAMES exist in
      docs/milestones/F2_figures.md and two of them are cited by name in the same
      paragraph where the value is also typed.
code  and this file's own recorded rule, at :600, written one round ago: "AND THE
      RATIO IS NOT RETYPED HERE EITHER (R194) ... a number that is generated is
      cited by name or it is not written."
judge every one of the six is TRUE at this commit -- I re-measured all six and
      they reproduce to the published digits. That is what kept R212, R206 and
      R216 at 4a and I am not applying a different rule to a new sentence. **What
      is different here is that the META-CLAIM is false at this commit**: two
      sentences say of their own paragraph that it does not do the thing it does,
      four and two lines away. The twenty-fifth verdict's rule was explicit --
      "true at this commit is why this is recorded and not blocking". These two
      are not true at this commit.
judge and the report is the other half of the finding, because it does the right
      thing: `docs/reports/F2/step-5.md:84-85` carries all four as `{{fig:}}`
      names and `:91-93` says "R194's remedy is applied at the start here rather
      than five rounds into it". The remedy is applied in the report and not in
      the file the rule was written for, and that file says it is.
```

**Closed when** `:296-298` and `:301-309` either drop the six typed figures and
keep the citation by name -- which is what `:600` did for `2.537e+07`, and what
the report already does -- or drop the two sentences claiming they are not there.
Either branch, and both sites: half of an item is not the item.

**R225. (recordable, 4a) The plan retypes two of the four generated figures in
the D5 table, forty lines above the table that cites them by name.**
`docs/milestones/F2.md:1456` and `:1457`.

```
code  :1456 "injected through the gate -- `3.061e-11` against a `1e-12` ceiling"
code  :1457 "which must redden both halves of G2.1 -- `7.471e-12` against a
      `1e-13` ceiling"
cmd   grep -c "{{fig:rigid_body_counter_ratio}}" docs/milestones/F2.md
out   1, at :1497 -- the placeholder mechanism was available and was used.
judge true at this commit (I measured 3.0612e-11 and 7.4708e-12) and it is the D5
      counter-case column, which R4 says is rewritten to the shipped counter as
      each row lands. So this is the R194 species and not a false sentence:
      recorded, not blocking, the same ruling as R216.
```

**Closed when** the two rows cite the figure names, or 4a records that the D5
column keeps typed values and why.

**R226. (recordable, 4a) The report's `out` line for its own `AX3` grep does not
match the grep at its own commit.** `docs/reports/F2/step-5.md:26-27`.

```
code  :26  cmd  grep -rni "ax3" over the whole repository, excluding .git
code  :27  out  two hits, both in docs/reports/F2/step-4.md, both mine, both prose
cmd   git grep -in "ax3" fba8ace -- .
out   SIX hits: two in step-4.md and FOUR in step-5.md itself, at :16, :21, :26
      and :164.
judge the SUBSTANTIVE claim is TRUE and I checked it independently: `AX3` names
      nothing in this repository -- no plan row, no README entry, no code, no
      test, no closure artifact. The count is what is stale, and it is stale in
      the self-referential way a grep for a string is stale in the file that
      discusses the string. Not blocking: no ceiling, no gate, no figure.
      Recorded because BF0's `out` field is what the command printed at this
      commit, and this one is not.
```

**Closed when** the `out` field says what the command prints at the commit that
publishes it, or the command excludes the file it is written in and says so.

**R227. (recordable, 4a) R218's condition had two halves; the report answers the
first.** `docs/reports/F2/step-5.md:151`.

```
code  :151 "R218 -- a step report that states no suite count | answered here:
      1578 passed, 0 failed, 0 skipped"
code  R218's condition: "states the suite counts from its own run, and -- because
      the number now moves for reasons that are not the code -- SAYS WHAT MOVED
      THEM."
cmd   python -m pytest --collect-only -q at aae355a and at fba8ace
out   1497 -> 1578, +81. Located: +44 in tests/test_report_carried.py (122 -> 166
      parameters, driven by verdict 25 naming more sites than verdict 24), +8 the
      new gate file, +4 the two new registrations across two cells, and the
      remainder in the regenerated corpus parametrisation at 2f92c58.
judge honest, reproduced, and half. The component that moved MOST is again mine
      and again not a code change, which is the whole reason the second half was
      asked for. Recorded rather than blocking for the reason the twenty-fifth
      verdict gave: its absence hid nothing, because I collected both ends.
```

**Closed when** a report revision states the counts and where the movement came
from, in one line.

**R228. (recorded -- a measurement, and the answer to the first thing I was asked
to try) The gate's measured reach: it is blind to every ORTHOGONAL transformation
error and to any uniform stiffness scaling, by mathematics rather than by
oversight.** No site; this is my adversarial run.

```
cell  eight defects injected into `element_global_stiffness`, upstream of the
      gate, with the SHIPPED assertions then evaluated on the assembled matrix:
        clean control                            ratio 1.60e-14  loss 5.31e-15
        one element's ke TRANSPOSED              1.60e-14  5.31e-15  passes (ke
                                                   is symmetric: a no-op)
        one element's LOCAL FRAME SPUN 37 deg    1.74e-14  4.81e-15  ** PASSES **
        that element's transform made NON-
          orthogonal (5 percent shear)           1.74e-03  3.34e-02  caught
        one element 50 percent too stiff         2.86e-14  9.60e-15  ** PASSES **
        one element's BENDING PLANES SWAPPED     3.31e-01  7.27e-01  caught
        TIP member's GJ -> 0 (seven zero modes)  7.40e-01  7.63e-01  caught
        one element, SIGN FLIP on a coupling     4.47e-01  4.24e-01  caught
        one element DIAGONALISED                 8.48e-01  7.69e-01  caught
judge the two that pass are not defects in the gate. A rigid-body motion mapped
      through ANY orthogonal element frame is still a rigid-body motion in the
      local frame, so the local nullspace is untouched -- no rigid-body test can
      see a wrong-but-orthogonal orientation, and G2.2 is where that lives (R1's
      species). Uniform scaling is likewise exactly annihilated. Recorded so that
      "G2.1 green" is not read as "the transformation is right". Nothing in the
      shipped file claims otherwise; the message at :286-289 is about what a
      FAILURE means and it is accurate.
judge AND THE SEVEN-ZERO-MODE CASE IS CAUGHT BY BOTH HALVES, which answers the
      question AP3 raises: with seven zero modes lambda_7 is round-off, so the
      ratio is a quotient of two round-off numbers and could land anywhere. It
      landed at 0.74 here. The SUBSPACE half landed at 0.76 and does not depend
      on that luck. AP3's ordering -- the span assertion is the real content --
      is confirmed by measurement rather than accepted from the plan.
```

**Closed when** 4a records the reach, or it is left standing as this verdict's
measurement.

## Rulings I was asked for

**1. `AX3`. The implementer's reading is CORRECT, and the frame as built is
adequate -- measured, not conceded.**

```
cmd   git grep -in "ax3" fba8ace -- .
out   six hits, all prose, none a designator: two in the step-4 report, four in
      the step-5 report itself. No plan row, no README entry, no code, no test,
      no closure artifact. AX3 NAMES NOTHING IN THIS REPOSITORY.
code  F2.md:1362, the case table row that governs: "| **V1.1** | constructed |"
judge THE CONSTRUCTED READING IS THE RIGHT ONE. The locked plan's provenance
      column is the authority and it says `constructed`; a directive phrase that
      traces to the implementer's own earlier prose is not a plan. Shipping a
      constructed frame was right, and refusing to invent a platform geometry was
      more right -- that is CLAUDE.md's "when you are stuck" applied correctly.
cell  IS THE FRAME ACCIDENTALLY SYMMETRIC OR DEGENERATE? The docstring at :91-92
      claims not; I measured rather than read.
        singular values of the centred node cloud  3.981 / 2.720 / 2.545
          -- full rank three, genuinely non-planar, no near-planar direction
        member lengths 4.000 4.022 3.712 3.558 3.669 3.567 2.500 -- no duplicates
        smallest RELATIVE gap anywhere in the flexible spectrum: 2.78e-02
        gap lambda_7 -> lambda_8: 5.06e-02
      NO DEGENERACY sits next to the one being measured. The claim holds. Two
      members ARE parallel (0-1 and 3-4, both along global x) and that is by
      construction, not by accident -- the release control needs the second one.
judge ADEQUATE, with one qualification that IS R223: adequacy was measured at one
      section, one mesh and one unit system, and it is exactly those three axes
      the corpus reddens.
```

**2. The dense eigensolver and BZ2's "`v0` pinned". The implementer's reading is
CORRECT and this is NOT a plan change.**

```
code  AP3, F2.md:200-224: "The ARPACK pin makes G2.1 *reproducible*. It does not
      make its eigenvectors *right* ... The `v0` pin still matters and sits
      UNDERNEATH this."
judge AP3 asks for reproducibility of a path that has a starting vector. It does
      not ask the gate to use that path, and `scipy.linalg.eigh` has no starting
      vector, so a pin on the gate would be a guard pointing at nothing --
      precisely the vacuity AP3 was written to name. Choosing ARPACK for the gate
      in order to have a pin to point at would trade accuracy for a citable
      guard. The file's own wording at :27-34 says this, and I agree with it.
cell  and the exercise is real rather than nominal, which is what makes the
      reading legitimate instead of convenient. 300 independent trials of the
      unpinned control's own body:
        unpinned pairs that agreed bit-for-bit: 0 of 300
        pinned pairs bit-identical over 50 trials: True
      The control is not a coin flip and it is not vacuous. NOT A PLAN CHANGE.
```

**3. The release control (asked: is its premise vacuous, and is the seventh mode
the claimed one?). BOTH ANSWERED, BOTH CLEAN.**

```
cell  THE PREMISE CARRIES ITS OWN FAILURE. I rebuilt the frame with node 4 moved
      and ran the SHIPPED control:
        tip (4.4, 1.1,             2.8)  SHIPPED  -> passes, count 7
        tip (4.4, 1.100000000001,  2.8)  +1e-12 m -> PREMISE FIRES
        tip (4.4, 1.100001,        2.8)  +1e-6 m  -> PREMISE FIRES
        tip (4.4, 1.4,             2.8)  +0.3 m   -> PREMISE FIRES
        tip (4.4, 1.1,             3.6)  the FIRST VERSION's shape -> FIRES
      1e-12 m is about the smallest offset the coordinate can express there. NOT
      VACUOUS. The second premise is not vacuous either: BeamElement compares by
      value, so `els[released] == BeamElement(3,4,SEC,S355)` can fail.
cell  THE SEVENTH MODE IS THE ONE CLAIMED, verified independently of the count. I
      built the analytic seven-space myself -- the six rigid modes extended so the
      extra DOF follows node 3's rx, plus the claimed twist (dof30 = dof27 = 1) --
      and projected it onto the computed seven-dimensional nullspace:
        tx 6.9e-15  ty 9.4e-15  tz 3.1e-15  rx 4.5e-15  ry 2.2e-15  rz 3.7e-15
        TWIST 1.3e-14      worst 1.342e-14
      and the claimed twist's strain energy is EXACTLY 0.000e+00.
      It is provable, as the docstring says: the (dof30, dof27) block is fully
      isolated -- max|entry outside the block on either row| = 0.000e+00 -- and it
      is [[GJ/L, -GJ/L], [-GJ/L, GJ/L]], rank one, nullspace exactly span{(1,1)}.
      NOT an artefact of the extra DOF: exactly ONE extra mode, and it is the
      twist the docstring names.
cell  and I INVERTED BOTH COUNTING RULES rather than sampling one side of them:
        pinned control:  largest |lambda_5| / lambda_6 over all 30 pins = 1.73e-13
          against a 1e-12 cutoff -> 5.8x of room below, 1e12x above
        release control: the seventh zero sits at 1.60e-14 of lambda_8, the eighth
          at 9.61e-01 -> 45x of room below, 9.6e+11x above
      Both counts are on a plateau, not near an edge. The 5.8x is the thinnest
      margin in the file, and it inherits R223: the cutoff IS
      `RIGID_BODY_MODE_RATIO`, so it moves with the frame's conditioning too.
```

**4. R201's composed-body attack, run against both new registrations.**

```
cell  the shipped pair, both cells reproduced:
        ratio  widened to 3.0612e-10  gate cell True  ceiling cell True -> ADMITTED
        loss   widened to 7.4708e-11  gate cell True  ceiling cell True -> ADMITTED
cell  THE BOUND, SOLVED rather than argued -- bisection on the shipped ceiling
      with the shipped counter as the predicate:
        RIGID_BODY_MODE_RATIO     green up to 3.0612e-11  =  30.6x
        RIGID_BODY_SUBSPACE_LOSS  green up to 7.4708e-12  =  74.7x
      Each constant can be raised by that factor with the whole suite green. That
      is the reach of the pair for these two entries, and it is EXACTLY the "about
      31x" and "about 75x" the entries already publish, said from the other side.
      The entries are honest about their own bound.
cell  the ceiling cell is not circular even though its widened value derives from
      the same injection: a body injecting 1e-6 in place of the declared 1e-12
      survives the widened 3.06e-10 and is REJECTED. The discrimination holds.
judge R201's generic composed body -- gate half plus arithmetic half -- remains
      admissible in principle here as it is everywhere in this file. That is a 4a
      item about the file, not about these two registrations.
```

## Tolerances touched

**Four added; no value changed, no existing value moved.**

```
cmd  git diff aae355a..HEAD -- floatfea/tolerances.py, non-comment changed lines
out  +4 lines, all four new constants. Not one existing value, name or form moved.
cmd  git diff aae355a..HEAD -- tests/regression/g22_exempt_pair_responses.json
out  54 -> 55 pairs; one added, none removed, none moved. The written explanation
     is in 2f92c58's message ("a corpus round", CLAUDE.md sec. Testing) and it is
     MY corpus round, so the reason is correct and locatable. ACCEPTED.
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `RIGID_BODY_MODE_RATIO` `:311` | (new) | `1e-12` | ratio of two eigenvalues, dimensionless | `RIGID_BODY_MODE_RATIO_COUNTER_DEFECT`, injected through `assembled` and registered in both cells of `tests/test_counters_are_injected.py` | `tolerances.py:289-310` and `F2.md:1468-1500`. The COUNTER is sound and I re-solved it: detection edge **`3.2970e-14`** of max abs K (bisected on the shipped assertion), counter at `1.0e-12` = **30.3x** the edge, response `3.0612e-11` = 30.6x the ceiling. The sweep reproduces to the published digits and is linear over eight decades (`ratio/size` = 3.06e+1 from 1e-14 to 1e-6). **The FORM is where it fails: dimensionless but NOT dimension-invariant, and the justification's central sentence is refuted -- R223.** The paragraph also carries R224. |
| `RIGID_BODY_MODE_RATIO_COUNTER_DEFECT` `:320` | (new) | `1.0e-12` | defect size, a fraction of max abs K, dimensionless | it IS the counter | `tolerances.py:313-319`. Sound. "One decade above the crossing" is 1.48 decades against the solved edge, and one decade above the top of the bracket the entry itself states; loose, not false. |
| `RIGID_BODY_SUBSPACE_LOSS` `:345` | (new) | `1e-13` | normalised projection residual, a fraction in [0,1] | `RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT`, the same injection, registered | `tolerances.py:322-344` and `F2.md:1479-1487`. Detection edge solved at **`1.3093e-14`**; counter at `1.0e-12` = **76.4x** the edge, response `7.4708e-12` = 74.7x the ceiling. The clean value `5.3061e-15` reproduces exactly. **AP3's claim that this is the stronger half is confirmed by measurement** (R228). **Same form defect -- R223 -- and it is the tighter of the two, so it reddens first: 0.78x of its ceiling at `subdiv=4` alone.** |
| `RIGID_BODY_SUBSPACE_LOSS_COUNTER_DEFECT` `:354` | (new) | `1.0e-12` | defect size, dimensionless | it IS the counter | `tolerances.py:347-353`. Sound, and "both counters are ONE injected defect" is not an economy: one diagonal stiffness reddens the loss by 74.7x while reddening the ratio by 30.6x. |

**What held**, reproduced at my run: `1578 passed, 0 failed, 0 skipped`;
`regen_figures.py --check` exit 0; the four new figures identical at four thread
counts; every number in report sec.1, sec.2, sec.3 and sec.4 to the published
digits; both detection edges inside the bracket the entries claim; the frame's
non-degeneracy; the release control's premise and its seventh mode; the pin and
its control over 300 trials; both counters through both cells; every path and
every commit the report cites; the `process:` commit standalone and additive; no
commit touching both code and `docs/reviews/`. **These did not**: the invariance
claim at five sites (R223), the two self-refuting sentences in `tolerances.py`
(R224), the plan's two retyped figures (R225), the report's AX3 count (R226),
R218's second half (R227).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Two items, in this order:

1. **R223** -- the five sites at `floatfea/tolerances.py:294`,
   `tests/verification/rung1/test_rigid_body_modes.py:19` and `:163-165`,
   `docs/milestones/F2.md:51` and `:1477`. **Site by site**, per CLAUDE.md
   "A closing condition that names sites is closed site by site": each named line
   either carries the corrected claim or is declared as left, with the reason. The
   two published headroom figures at `F2.md:1491-1492` cite a rule that moved, so
   BP0 applies to them in the same commit -- they carry their operating point or
   they are withdrawn. **The invariance in `E` HOLDS and should be kept; I
   measured it over fifteen decades. It is the section, the mesh and the length
   unit that do not.**
2. **R224** -- `floatfea/tolerances.py:296-298` and `:301-309`, both sites, one
   branch each: drop the six typed figures, or drop the two sentences saying they
   are not there.

**Not gates on step 5, into the next report's `Carried`:** R225, R226, R227,
R228, and everything already at 4a.

**And the witness.** `docs/SUPERVISOR.md:35-40` now says the channel is live and
that step 5 is the first step that can carry a witness comment. There is none
yet. **If a `[witness F2 step 5]` comment lands before the answering report it is
read first, and a witness HOLD is answered exactly like this one; where the two
disagree the stricter verdict stands and the disagreement goes in the report.**
This is the twenty-sixth consecutive review by one reader, and R223 is exactly the
kind of thing that is found by looking where the previous twenty-five did not.

**Adversarial corpus (BE3): 20 new entries committed at `caa2ec5`, all unseen by
the implementer; every field measured at `fba8ace` before the line was written.**
`tests/corpus/g21_rigid_body_frames.txt` -- a NEW FILE, because G2.1 had no corpus
at all and its coverage claim rested entirely on the one configuration its author
chose.

**The coverage measurement, stated plainly: of my 20 new entries the shipped
checks caught ZERO.** Not one is executed by any shipped test -- `pytest -q` is
`1578 passed` with the corpus on disk, unchanged to the test. **13 of the 20
breach a shipped ceiling with a DEFECT-FREE element**, and the `energy` column is
the control that says so: the analytic vectors' own strain energy never exceeds
`6.3e-17` at any of the twenty while the two gated quantities span `1.1e+06`.

What the entries measure:

* **The nearest legitimate red is a 100 mm x 1 mm brace**, at the shipped mesh, in
  SI units: `loss 1.50e-13`, 1.5x its ceiling. `rb_brace_D0p1_t0p001`.
* **Refining the mesh reddens a gate whose scope cell says it is
  mesh-independent** -- `rb_subdiv6` and `rb_subdiv8`, loss at 1.19x and 1.46x.
* **The same physical structure in centimetres fails both halves by 22.7x and
  53.2x**, and I proved it is a re-expression (residual `9.7e-16`) before reading
  the gate on it. Decimetres still pass; the crossing is between 10 and 30 units
  per metre.
* **Two effects compose**: brace plus `subdiv=4` gives `3.51x` and `10x`.
* **The release control's premise is bracketed on disk**, at `1e-12 m` off-axis
  and at the first version's own tip. Both are caught by the premise assertion.

**Twenty-six consecutive rounds have found no element defect**, and this round
does not either: the element held under eight injected defects and twenty
configurations, and the reading is unchanged -- not yet contradicted, until V5.1
puts CalculiX on the other side. What moved this round is not prose about the
instruments. **It is that the instrument's stated property is not a property it
has, and the ceiling it sets is a ceiling on one frame's condition number.**
