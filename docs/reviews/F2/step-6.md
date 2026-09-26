# Review � F2 step 6
Reviewed commit: 4064897d2c36f8c5fb9c640b51afb486e2261213
Verdict: STOP

**Reviewed commit: `acbbd0a`.** Fifty-ninth verdict, and the **third verdict on
step 6**. The `Reviewed commit:` line at the top of this file is stamped `HEAD`
by `scripts/write_verdict.py` and is my corpus commit, not the commit judged
(R513, unchanged).

Tests: **1 failed, 2544 passed, 0 skipped** -- my run, clean tree at `acbbd0a`,
`python -m pytest -q`, 617.27 s, Python 3.13 on Windows.

```
out  FAILED tests/test_plan_figures.py::test_every_floor_class_row_clears_its_
     tolerance_on_THIS_tree
       rigid_mode_residual_worst_over_corpus clears RIGID_MODE_EXACTNESS by
       1.347x, under the declared spread 1.5x
judge REPRODUCED. That is the red the report declares rather than clears, and
     declaring it was the right call.
```

**AND THEN I WENT LOOKING FOR THE BAND IT COMES FROM, WHICH IS THE QUESTION YOU
PUT TO ME, AND IT IS WORSE THAN 1.347x.** At my corpus commit `4064897`, rung 1
is red at **six** frames:

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py -q -k G2_1_holds
out  6 failed, 181 passed, 7 deselected
     rb_tip_2p95deg_from_global_Z         1.2497e-15   1.250x the ceiling
     rb_tip_2p95deg_from_Z_tip_1pm_moved  2.4727e-15   2.473x
     rb_tip_4p4deg_from_global_Z          1.3905e-15   1.391x
     rb_tip_3deg_from_Z_span_x10          1.0818e-15   1.082x
     rb_tip_2p9deg_from_Z_span_x30_12dp   1.5796e-15   1.580x
     rb_tip_2p95deg_from_Z_brace          1.2435e-15   1.244x
judge SIX DEFECT-FREE FRAMES OVER THE GATE'S OWN CEILING, every one in the
     family the corpus already holds, not one of them a new kind of structure.
     That is the STOP, and R524 is where it is measured.
```

## Item 1b -- CHECKED, AND CLEAN

```
cmd  the newest Answers line in the report under review
out  docs/reports/F2/step-6.md:1801 -- Answers: verdict 58 @ 8a681b2
cmd  the newest verdict in the repository before this one
out  verdict 58, committed at 8a681b2, in docs/reviews/F2/step-6.md
judge THE HEADER NAMES THE LATEST. One comparison, made, and it matches. Every
     Carried claim below is about the right list.
```

## CI at the reviewed commit (3b) -- RED on identical code, and not CK2

```
cmd  gh run list --commit acbbd0a --json name,conclusion,workflowName
out  []
cmd  the same for 44757be
out  36218676882, event push, conclusion FAILURE
cmd  git diff 44757be acbbd0a -- floatfea tests scripts .github
out  (empty)
judge SO THE LAST RUN THAT EXECUTED RAN THE CODE UNDER REVIEW, BYTE FOR BYTE;
     acbbd0a touches only docs/reports/**, which paths-ignore skips. NOT CK2 --
     no job was created and cancelled for payment; none was created at all. The
     result still describes this tree and it is FAILURE.
cmd  gh run view 36218676882 --json jobs
out  the verification ladder            | success
     lint, unit and guards              | FAILURE | 13 named failures
     CI determinism -- leg / ten agree  | skipped
judge THE LADDER IS GREEN ON LINUX ON THIS CODE, at the corpus as committed.
     test_every_floor_class_row_clears_its_tolerance_on_THIS_tree is among the
     thirteen, so the 1.347x decision is reproduced on a machine neither of us
     controls -- your determinism claim is confirmed, and I confirmed it a
     second way by re-summing both matvecs in reverse order (R524). The other
     twelve are the report-parametrised guards, measured before revision 4
     existed, and they are green in my run at acbbd0a.
judge A RED CI IS A HOLD ON ITS OWN (CA2). It is subsumed here by the STOP.
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, tenth round.
```

## My own instructions (4b), conftest (4c), tolerance values (4)

```
cmd  git diff 8e64f22..acbbd0a -- .claude docs/SUPERVISOR.md
out  .claude/hooks/require-verdict.sh +19, docs/SUPERVISOR.md +36
cmd  which commits, and what else is in them
out  531d106 -- .claude/hooks/require-verdict.sh ONLY, "process: ... (DE1)"
     44757be -- docs/SUPERVISOR.md ONLY, "process: ... (DE2)"
judge BOTH ARE STANDALONE process: COMMITS CITING THEIR DIRECTIVE, and neither
     touches floatfea/ or tests/. NOT A STOP on this head. I read both
     additions line by line. DE1 adds closed_by_a_pass() and skips a review
     file containing any "^Verdict: *PASS", which is DD1's ruling mechanised
     and deletes no guard. DE2 is scope, it is Xabier's to set, and I hold it
     rather than argue it here.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction's own expectation, met
cmd  git diff 8e64f22..acbbd0a -- tests/conftest.py "tests/**/conftest.py"
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set, so no rung's green is written by
     code in its own directory and no plugin was added this round
cmd  every NAME: Final[...] = value at 8e64f22 and at acbbd0a
out  48 and 48; added [] removed [] changed []. NOT ONE VALUE MOVED.
judge AND THAT IS THE RIGHT ANSWER TO THE RED, not a tolerance edit. You
     reported the failure instead, which is what CLAUDE.md asks for.
```

## Carried

Verdict 58 carried **R514, R515, R516, R517, R518** as blocking, R519 to R523 as
closure items, and R475 / R487 / R488 / R492 / R493 / R500 / R501 as open on top.
Its `Next step opens when` conditions 6 and 7 are carried here too.

- **R514 -- ANSWERED, site by site, and the withdrawal is better than I asked
  for.** `floatfea/tolerances.py:392` now reads "TWO CANDIDATES, BOTH
  RENDERED AND BOTH ENFORCED AGAIN (CV1/CW2, R426/R438; R503 then R514)";
  `:413` turns "WITHDRAWN AND NOT REPLACED" into "WAS WITHDRAWN AND IS NOW
  REPLACED"; `:422-441` names the test that enforces it and then records, in the
  file, why the five sentences went stale and that this is BP0 turned on the
  entry that cites BP0. All three named sites closed. **The same entry now
  carries a new sentence that is false in the same reassuring direction -- R524
  -- so the head does not clear.**
- **R515 -- ANSWERED and the ablation is closed.**
  `tests/test_plan_figures.py:173-188` requires
  `{"rigid_mode_largest_rigid_eigenvalue", "rigid_mode_mechanism_ceiling"}` to be
  in `checked` before `assert checked` runs, so flipping the two `_floor(...)`
  marks in `scripts/regen_figures.py` to `"derived"` now reddens instead of
  passing. Membership, not non-emptiness, which is what the finding asked for.
- **R516 -- ANSWERED.** `test_the_Carried_table_is_what_the_generator_produces`
  is in the tuple at `tests/test_report_guard_states.py:659-668`, and
  `two_digit_step_number_discriminating` is green in my run with nothing else in
  that file red.
- **R517 -- ANSWERED, AND THE CHOICE YOU MADE IS THE RIGHT ONE.**
  `_seed_older_verdict()` at `tests/test_report_guard_states.py:253-276`
  constructs the precondition inside the scratch copy instead of skipping the
  three states; `:356` and `:462` both check the length and assert a diagnosis
  rather than indexing `[1]` bare. All three states are green in my run.
- **R518 -- ANSWERED.** `_is_a_site()` at `tests/test_report_carried.py:2626` is
  `"/" in path or _tracked_at_reviewed(path)`; `frames.txt` still dies and
  `tests/verification/rung1/test_new_thing.py` is a control in `_R507_CONTROLS`
  asserting that a path naming a file to be created is a site.
- **Condition 6 (`0 failed` locally, completed SUCCESS on CI) -- NOT MET**, and
  not met for the reason that is the most useful output of this step. R524.
- **Condition 7 / R475 -- LANDED at `aa5ccf3`, and the form is not what fails.**
  The three cells ship as tests; the ten span cells and the reference-point cell
  are green in my run and I reproduced the reference-point numbers. The
  row-shared denominator is a real improvement on the per-DOF candidate: the
  corpus's own `perdof_clean` field reads `1.2425e-14` at 2.87 degrees where
  `rowshared_clean` reads `4.2293e-16`. **What R475 did not do is re-derive the
  ceiling, and the ceiling is where the gate fails.**
- **R487 -- LANDED as an assertion at
  `tests/verification/rung1/test_rigid_body_modes.py:285-298`, and the assertion
  cannot fail.** R527, a closure item, with its measurement attached so nobody
  spends a round rediscovering it.
- **R486 -- OUT OF F2 BY DD0, not reopened by me.** I want to be explicit that
  R524 is not R486 coming back through the window. DD0 moved the
  *admissible-domain* claim to a G3 gate on the real platform model. R524 is
  inside the corpus family the F2 gate already asserts over: this file has held
  `rb_tip_2p87deg`, `rb_tip_4deg`, `rb_tip_6deg`, `rb_tip_10deg` and
  `rb_tip_20deg` since batch 4, and which angles are in it is an accident of
  which ones I picked then.
- **R488, R492, R493, R500, R501 -- OPEN,** unchanged, none re-reviewed.
- **R519 -- OPEN closure item.** The section-3 rows still read "the sentences the
  finding names are restored by reverting the DB1 prose commit"; `365ae5b` edited
  them.
- **R520 (R505) -- ANSWERED as recorded in the answers file; not re-measured.**
- **R521 (R509), R522 (R510) -- OPEN closure items,** unchanged. R522 still
  carries R476's `ZeroDivisionError` on a coincident tip node, R477, R478, R480.
- **R523 -- CLOSED, the honest way.** A temporary ref at `8e64f22`, dispatch
  `36234584744`, the FAILURE taken, the ref deleted; `gh run list` shows it. That
  ends the question the finding was about.
- **R513 -- OPEN and live in this file's own header line,** as in the last two.
- **The 48 items frozen in `docs/milestones/F2a.md` section 7 -- OPEN on the
  frozen list,** not re-reviewed item by item. DE2 adds the apparatus corpora and
  REPAIR-STALE's 0-of-13 to that list; I have not transcribed them.

## Findings

**First, what is right, and it is most of the diff.** `aa5ccf3` is the best
commit of this step: the normalisation is derived rather than tried, the three
cells ship as tests rather than as report sections, both counters are injected on
both DOF classes at five spans with bisected edges, the reference-point cell
publishes both sides instead of a saturated ratio, and the structural half is
asserted on the shipped columns against a bound derived from `n_nodes * EPS`
rather than typed. `365ae5b` closes five findings at their named sites, and
`_seed_older_verdict` refuses the skip that was available. **And the red was
reported rather than cleared, with `RIGID_MODE_EXACTNESS` untouched, after a
directed cell refuted its own hypothesis.** That is the behaviour this apparatus
exists to produce, and it is why the STOP below is a statement about the plan
rather than about the work.

---

**R524. (STOP-class -- (b), (c) and (d).) THE ROW-SHARED RESIDUAL'S CLEAN
SCATTER CROSSES `RIGID_MODE_EXACTNESS` ON DEFECT-FREE FRAMES IN THE CORPUS'S OWN
FAMILY. THE CEILING IS NOT 1.347x THIN; OVER THE NEAR-VERTICAL BAND IT IS
EXCEEDED, UP TO 2.473x, AND THE ELEMENT IS FINE AT EVERY ONE OF THEM BY TWO
WITNESSES THAT DO NOT SHARE THE NEW NORMALISATION.**

```
cell  ONE VARIABLE. The shipped frame, the shipped section, metres, subdiv 1,
      node 4 at node 3 plus 2.5 m -- the construction the corpus's own
      rb_tip_*deg_from_global_Z entries use, with the tip written to TWELVE
      decimal places throughout this cell and the next two. Only the angle of
      member (3,4) from global Z moves. (The precision is stated because it
      matters: see the smoothness cell below. My corpus entries record which
      precision each one used, and the same angle at eleven places is a
      DIFFERENT number -- 3.00 deg reads 3.6831e-16 there and 1.3484e-15 here.)
out    2.87 deg  2.5835e-16  0.258x     <- corpus entry since batch 4
       2.90      1.3487e-16  0.135x
       2.95      2.4727e-15  2.473x  *** OVER ***
       3.00      1.3484e-15  1.348x  *** OVER ***
       3.05      1.4403e-15  1.440x  *** OVER ***
       3.10      1.3809e-16  0.138x
       3.20      1.1949e-15  1.195x  *** OVER ***
       3.50      1.2116e-15  1.212x  *** OVER ***
       4.00      1.3581e-16  0.136x
       5.00      1.0515e-15  1.051x  *** OVER ***
       6.00      7.3569e-16  0.736x     <- corpus entry, and your worst
cmd   the same sweep widened, metres only: 13 angles x 10 spans, base section,
      subdiv 1, every frame through C._build and RB.residual_exactness
out   22 of 130 defect-free frames OVER the ceiling. Worst 1.5796e-15 at 2.90
      deg with a 159 m span.
cell  THE ELEMENT, HELD, MEASURED BY TWO QUANTITIES THAT DO NOT SHARE THE NEW
      DENOMINATOR, at that 159 m frame
out   retired global-norm residual   3.8709e-17   (0.039x the same ceiling)
      strain energy, max_j |v'Kv| / (||v||^2 max|K|)   1.870e-17
      -- both the same order as at the shipped frame, and the energy field is
      the corpus's own frame-versus-element control.
judge SO IT IS THE MEASURE, NOT THE ELEMENT. Fifty-nine rounds have found no
      element defect and this is not one.
```

```
cell  AND THE QUANTITY IS NOT SMOOTH IN THE GEOMETRY. One variable: the twelfth
      decimal place of one coordinate.
out   2.95 deg, tip written to 11 dp: 1.2497e-15. The same tip to 12 dp:
      2.4727e-15. The two frames differ by about a picometre on a 4 m member and
      the gate's number doubles. The same pair at 2.90 deg, span x30:
      4.2740e-16 and 1.5796e-15 -- one green, one red.
cmd   both matvecs re-summed in reverse order, as a stand-in for another BLAS
out   1.2497e-15 -> 1.2501e-15; 2.4727e-15 -> 2.4721e-15; 7.4255e-16 ->
      7.4369e-16. Under 0.1 percent.
judge NOT A SUMMATION-ORDER ARTEFACT AND NOT A PLATFORM ARTEFACT. The scatter is
      in the geometry, and the ceiling sits inside it.
cell  WHERE THE MAXIMUM COMES FROM -- the cell you asked me for, rows 25 and 27,
      one orientation step apart, both 4-term. IT IS NOT THE ROW.
out   6 deg:    max at row 25 (dof 1, node 4), vector j=5, 4 terms
                content from j=5            1.3519e-02
                shared max_j content        1.8981e-01   (from j=3)
                inflation                   14.04x
                numerator / its own content  46.95 eps
      2.87 deg: max at row 27 (dof 3, node 4), vector j=5, 4 terms
                content from j=5            8.0566e-03
                shared max_j content        2.3669e-01   (from j=3)
                inflation                   29.38x
                numerator / its own content  56.24 eps
judge THE TWO ROWS ARE THE SAME SHAPE AND THE SAME VECTOR. What differs is the
      DENOMINATOR: the shared max_j at that row is 14.04x the content the
      maximising vector itself excites at 6 deg and 29.38x at 2.87 deg -- a
      lever-arm ratio between two DIFFERENT rigid vectors at the same DOF. In the
      per-vector quantity THE ORDER REVERSES (56.24 eps at 2.87 deg against
      46.95 eps at 6 deg), so the published 1.75x gap is entirely the sharing,
      and the sharing is what stopped R486's false reds. The measure is
      eps x (the row's own assembly error) / (a geometric ratio the frame
      chooses), and nothing bounds the second factor.
judge WHICH IS WHY DF0 FOUND NOTHING, AND YOUR REPORT OF IT IS CORRECT. The term
      count cannot explain it, the cancellation cannot explain it, and a c*m*eps
      bound is not the shape of this quantity. The hypothesis was worth one cell
      and the cell answered it.
```

```
judge WHY THIS IS (b) AND (c) AND (d) AT ONCE. (b): 1e-15 is not a ceiling on the
      quantity it now bounds, and the entry at floatfea/tolerances.py:328
      says in the same commit that the value "is a decade boundary above the
      measured worst" -- it is 1.347x above the committed corpus's worst and
      BELOW the measurement at the frames above. (c): the gate's decision over
      this band carries no information, because a defect-free frame reads
      2.4727e-15 while the counter's own bisected detection edge on k[0,0] is
      1.1656e-15 to 1.4745e-15 -- clean and defective are the same number there.
      (d): six parametrised cases of test_G2_1_holds_at_every_frame_in_the_corpus
      in tests/verification/rung1/test_rigid_body_corpus.py are red at my corpus
      commit.
judge AND WHY IT IS A STOP RATHER THAN A FOURTH ROUND. docs/milestones/F2.md LINE
      1849 STILL DECLARES THE RETIRED FORM -- max_j ||K_hat v_j|| / ||v_j|| -- as
      what RIGID_MODE_EXACTNESS bounds, one commit after the code stopped
      computing it. Line 1462 authorises the row-shared form and asks for
      RIGID_MODE_EXACTNESS "re-measured on CI", and the re-measurement is what
      has come back negative. The locked plan and the shipped gate do not
      describe the same quantity, and no value chosen inside a step repairs that:
      either the form changes again or the ceiling is derived from something, and
      both are Q7, which is locked. A rung-1 gate that false-reds makes every
      rung above it uninterpretable.
```

  **Reopens** `docs/milestones/F2.md` § Q7: the residual row at `:1849`, the
  `RIGID_MODE_EXACTNESS` row at `:1331`, and the sentence at
  `floatfea/tolerances.py:328` that calls the value a decade above the measured
  worst, inside the re-measured Reason block at `:316-331`. **No tolerance value moves in the meantime, and nothing is
  widened to clear the six reds** -- `1e-15 -> 3e-15` would pass my corpus and
  would be a number chosen to fit a scatter nobody has bounded, which is the
  shape DB1 and DC0 spent two rounds deleting. What the reopened plan has to say
  is which of these it is: **(i)** the quantity is bounded by something derivable
  -- then derive it, and let the ceiling be that bound times a stated factor,
  with the near-vertical band inside the measurement; **(ii)** it is not bounded
  and the gate needs a different quantity -- the strain-energy field is the
  obvious candidate and this corpus has carried it at or below 6.3e-17 over every
  entry for thirty rounds; or **(iii)** G2.1's residual half is asserted only over
  a declared, enumerated set of frames and says so, in which case the corpus is
  that set and it is now red. I have no vote on which. The measurement is what I
  owe.

---

**R525. (BLOCKS -- (c).) `test_a_NEAR_VERTICAL_member_is_not_false_reddened` DOES
NOT BUILD A NEAR-VERTICAL MEMBER. ITS ELEVEN CELLS PUT MEMBER (3,4) AT 61.3 DOWN
TO 55.1 DEGREES FROM GLOBAL Z, THE CLOSEST MEMBER TO VERTICAL IS 38.1 DEGREES IN
EVERY CELL, AND THE BAND IT NAMES IS WHERE R524 LIVES.**

```
cmd  build each of the eleven cells exactly as the test does --
     tip = f"{4*sin(d)},0.0,{4*cos(d)}" -- and measure the angle of member (3,4)
     from global Z on the assembled model
out   deg | member(3,4) from Z | min member from Z | clean residual
       0  |       61.340       |      38.100       | 1.3370e-16
       1  |       60.677       |      38.100       | 1.7955e-16
       2  |       60.019       |      38.100       | 1.6042e-16
       5  |       58.078       |      38.100       | 1.4753e-16
      10  |       55.081       |      38.100       | 1.7076e-16
judge THE PARAMETER IS THE ANGLE OF NODE 4's POSITION VECTOR FROM THE ORIGIN, AND
     NO MEMBER RUNS FROM THE ORIGIN TO NODE 4. CONN has (0,3), (1,3), (2,3),
     (3,4); node 4's neighbour is node 3 at (1.9, 1.1, 2.8). So `degrees` moves
     the tip along a circle about the origin while the member sweeps 61 to 55
     degrees, which is neither near-vertical nor a band.
judge AND THREE OF THE CELLS COULD NOT HAVE BEEN BUILT AS NAMED.
     MEMBER_ORIENTATION_DEGENERACY refuses a member within 2.866 degrees of
     global Z -- DegenerateMemberOrientation, raised, I hit it -- so 0, 1 and 2
     degrees from vertical do not exist without an orientation node. The test
     reads green at those ids because it is measuring something constructible
     instead.
judge THIS IS THE RECORDED GUARD ABOUT ASSERTION DOMAIN, word for word: check
     that the collection the assertion inspects can contain the failure. The real
     band reads 2.5835e-16 at 2.87 deg, 2.4727e-15 at 2.95 deg and 7.3569e-16 at
     6 deg -- 2x to 18x the figures this cell publishes -- and six of my fifteen
     new corpus entries inside it are red. The one cell shipped to protect the
     operating point certifies nothing about it, which is how R524 could land in
     the same commit as "the near-vertical band shows no false red".
judge IT IS (c) AND NOT PROSE. The docstring is wrong, but so is the
     PARAMETRISATION: the quantity is asserted at a geometry the test does not
     name, so what the gate claims is not what it checks.
```

  **Closed when** the cell's geometry is the angle it parametrises -- member (3,4)
  swept from global Z, over the part of the band the tool admits, which begins at
  `MEMBER_ORIENTATION_DEGENERACY` and not at zero -- and the figures in
  `docs/reports/F2/step-6.md` § 1 that were measured against the old geometry are
  regenerated or withdrawn in the same commit (BP0). **An inadmissible orientation
  raises and is not a cell.** This is a change to an existing test's domain, not
  new apparatus.

## Closure items (CZ0). None of these is (a), (b), (c) or (d).

**R526. The downward negative control for the residual half decides by the
RETIRED quantity.** `tests/verification/rung1/test_rigid_body_modes.py:694` and
its twin at `tests/verification/rung1/test_rigid_body_corpus.py:302` compute
`max_j ||K v_j|| / (max|K| ||v_j||)` inline and compare it with
`RIGID_MODE_EXACTNESS`, whose quantity changed at `aa5ccf3`. **I measured it under
the shipped form before writing this, so that nobody spends a round on it:** over
all 30 pins the weakest is `4.4205e-02` under the shipped form against
`4.9378e-03` under the retired one, and 0 of 30 pins land inside the ceiling. The
decision does not move. What is wrong is that a control on the residual half is
not computed by the residual half. Closed by routing both through
`residual_exactness` on the reduced system, or by stating in the file that the
control is deliberately in the retired quantity and why.

**R527. R487's assertion cannot fail, and the one cause its own message names
walks past it.** `tests/verification/rung1/test_rigid_body_modes.py:285-298`
asserts `not any(numerator[~live] > 0)`. `content_i` is a sum of non-negative
terms, so `content_i == 0` implies every term is zero and the numerator is exactly
zero: the assertion is a theorem of IEEE arithmetic, not a check. Its message says
"either `K_hat` has a NaN or the masking below is hiding a real residual" -- with
`K[7,7] = nan`, `scale` is NaN, every `content_i` is NaN, `NaN > 0.0` is False, the
assertion passes, and the function then raises `ValueError: zero-size array to
reduction operation maximum` out of line 302. Measured. The retired form returned
NaN and reddened the gate, so the masking lost that diagnosis. Closed by asserting
something that can be false -- a finite `K_hat`, and `content` non-empty -- or by
deleting the assertion and keeping the comment; a check that cannot fail is the one
thing worse than the comment it replaced.

**R528. `docs/reports/F2/step-6.md` § 1 says "the near-vertical band shows no false
red".** The figures under it are correct for the geometry the test builds; the
sentence is about a band the test does not build (R525). Closed by regenerating
both when R525 lands.

**R529. R519, R521, R522 and R513 unchanged**, and not re-measured here.

## Tolerances touched

**NONE. No constant was created, retired, moved or renamed.**

```
cmd  every NAME: Final[...] = value at 8e64f22 and at acbbd0a
out  48 and 48. added [] removed [] changed []
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance value touched this round** | -- | -- |

**But `RIGID_MODE_EXACTNESS` is the subject of the STOP, and this is where a
summary of it belongs.** Form: relative and dimensionless by construction under
the new normalisation, which is right. Counter:
`RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1.0e-14`, now injected on a translational
and a rotational DOF at five spans each with bisected edges -- what R475 asked
for, delivered. Basis: the Reason block at `floatfea/tolerances.py:316-331`, above the value at
`:332`, and the basis is what fails. The counter's bisected detection edge on `k[0,0]` is `1.1656e-15` to
`1.4745e-15` at the shipped tip direction, and a **defect-free** frame 2.95
degrees from vertical reads `2.4727e-15` -- so over that band the clean value is
past the edge at which the counter is declared detected. **A counter that clears
its edge by 6.78x at one orientation and a clean frame that clears the ceiling
from the wrong side at another are the same measurement seen twice, and the entry
records only the first.**

## Adversarial corpus (BE3, scoped by DE2 to the element and the gates)

**15 new entries, all unseen by the implementer, committed separately at
`4064897`. `tests/corpus/g21_rigid_body_frames.txt`, batch 8, entries 173 to
187.** The near-vertical band of the gate's own frame under the row-shared
residual: 2.87 to 5 degrees from global Z, crossed with section, span, length unit
and subdivision, plus two pairs differing only in the twelfth decimal place of one
coordinate.

```
cmd  grep -c "^id=" tests/corpus/g21_rigid_body_frames.txt
out  187   (172 before this batch)
```

**Coverage measurement. 15 new entries, 6 of them live -- defect-free frames over
the shipped ceiling -- and the implementer's checks caught 0 of 6.** The mechanism,
so the zero is not taken on trust: the only shipped check aimed at this shape is
`test_a_NEAR_VERTICAL_member_is_not_false_reddened`, and R525 is the measurement
that its eleven cells sit at 55 to 61 degrees from vertical, where the quantity
reads 1.34e-16 to 1.80e-16 and nothing crosses. The ten span cells hold the tip
direction fixed at `3.1,2.2,4.4` -- 35 degrees from Z -- and sweep the span, which
is the axis this quantity IS flat along. **6 of 6 found by sweeping the axis the
tolerance entry claims to be about; 0 of 6 by any check in the repository.** The
per-entry corpus assertion reddens on all six now, and that is the corpus doing its
job rather than a check catching an unseen shape.

**And the recheck on batch 4, because a corpus that is not re-measured is a list.**
The five `rb_tip_*deg_from_global_Z` entries that have been in this file since batch
4 read 0.258x, 0.136x, 0.736x, 0.116x and 0.162x of the ceiling today -- all green
-- and the nearest new neighbour of the first, 0.08 degrees away, is red at
1.250x or at 2.473x depending on the twelfth decimal place of one coordinate. **Which
angles are in the file is an accident of which ones I picked in an earlier round**,
and that is the sharpest thing this round measured about the corpus method itself: a
corpus sampled on a smoothness assumption, over a quantity that is not smooth,
certifies its samples and nothing between them.

**And the counterweight, because right-every-time is not allowed to become a prior:
fifty-nine rounds have found no element defect and this round found none either.**
`floatfea/` received no executable change; the element annihilates the analytic
rigid-body vectors to `3.8709e-17` in the retired form and `1.870e-17` in energy at
the worst frame I could build. R524 is about the instrument. Ladder 5 has still
printed `OK -- 0 directories ran` every time it has run and V5.1 against CalculiX
has still not spoken, so "not yet contradicted" remains the strongest statement
available about the element itself.

## On the criterion, said once

**CZ0's three-verdict clock closes HOLDs. It does not convert a STOP, and I have
not let it.** This is the third verdict on step 6, and under CZ0 I would write PASS
and carry R524 and R525 by name into step 7. I am not doing that, and the reason is
the one the criterion gives for its own existence: the clock is there so that rounds
of correct findings which move no gate stop consuming schedule. R524 moves a gate --
it is the gate -- and the repair is not available inside a step, because
`docs/milestones/F2.md` § Q7 is locked and the plan row and the code now describe
different quantities. Carrying it would mean step 7 measured against a rung-1 gate
that reads 2.473x on a defect-free brace three degrees off vertical, which is the
orientation a platform is mostly made of. **If Xabier reads the clock as ruling even
here, the disposition is his to write into this file by hand, as verdict 57 was, and
I will not spend a round arguing it.** What I would ask in exchange is one sentence
in the reopened Q7 naming which of R524's three exits is taken, because the
difference between "derive the bound" and "enumerate the domain" decides whether the
corpus is evidence or is the gate.

**And the schedule.** The 2-3 October slip, reported the day it is known, is the
rule working. I have no basis to hold a date against this step: a gate that
false-reds, found on 26 September, is worth more to 31 October than a green step 6 on
30 September, and F3's G3 gate on the platform model -- DD0's destination for R486 --
cannot be built on a residual whose ceiling is inside its own scatter.

## Next step opens when

**Step 6 does not close and step 7 does not open. Implementation halts.**
`docs/milestones/F2.md` § Q7 reopens, and the gate is not touched until it is
re-locked.

1. **Q7 reopens and states which quantity `RIGID_MODE_EXACTNESS` bounds**, at
   `docs/milestones/F2.md:1849`, and what bounds the value, at `:1331` and at
   `floatfea/tolerances.py:328`, inside the Reason block at `:316-331`. One of
   R524's three exits, named. **No value
   moves before the plan is re-locked, and no value is chosen to clear my six
   entries.**
2. **The re-derivation, whatever it is, is measured over the near-vertical band** --
   from `MEMBER_ORIENTATION_DEGENERACY` upward -- and not only along the span axis,
   which is the axis this quantity is flat along.
3. **R525:** the band cell's geometry is the angle it parametrises, and § 1's figures
   are regenerated or withdrawn in the same commit.
4. **The six red entries in `tests/corpus/g21_rigid_body_frames.txt` are answered by
   the re-lock, not by a corpus edit.** The file is mine, I will not remove them, and
   an entry the re-locked gate legitimately refuses is marked refused in the plan's
   own words rather than deleted.
5. **`python -m pytest -q` is `0 failed` and `gh run list --commit <sha>` is a
   completed SUCCESS** at whatever commit answers this, on a push that touches
   `floatfea/` or `tests/` so `paths-ignore` does not skip it.
6. **R526, R527, R528 and R529 are closure items** and go into one closure commit
   with the rest of the list. Do not re-review them item by item, and do not hold
   anything on them.
