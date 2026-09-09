# Review — F2 step 4
Reviewed commit: 5554f0d0ccc331ec6085fe64a8b26a3b9a3974fd
Verdict: PASS
Tests: 1398 passed, 0 failed, 0 skipped   (my run at `9d70483`, `python -m pytest -q`,
124.25 s. With my twenty-second-round corpus applied: **1431 passed, 2 failed**.)

**Reviewed code commit: `f1b226b`; plan `3d91954`; report `9d70483`.** The header
stamp is `5554f0d`, my own corpus commit, made immediately before this verdict and
touching no code.

Twenty-second pass. Range `ec09ea6..9d70483`, three commits.

```
cmd  git diff ec09ea6..HEAD -- .claude docs/SUPERVISOR.md
out  (empty)  -- my instructions untouched. Nothing added, nothing deleted.
cmd  per commit, files under floatfea/ | tests/ | docs/reviews/ | .claude/
out  3d91954  0|0|0|0    f1b226b  1|3|0|0    9d70483  0|0|0|0   -- correctly routed
cmd  the tolerances diff, comment lines stripped
out  (empty)  -- NO value changed. Three entries, comment text only.
cmd  the tests diff, grepped for xfail / skip
out  (nothing)
cmd  collected test FUNCTIONS at ec09ea6 vs 9d70483, parametrisation stripped
out  223 -> 225. Two ADDED (`test_the_counter_fails_when_its_ceiling_is_widened`,
     `test_a_DEFECTIVE_counter_is_rejected_by_its_cell_and_admitted_by_the_other`),
     none removed. Per file: meta-test 4->10, plan-figures 30->31,
     report_carried 146->117 (parametrised over the newest verdict's named
     sites). Nothing else moved.
cmd  grep -n "^Answers:" docs/reports/F2/step-4.md | tail -1 ; newest verdict commit
out  :3523 verdict 21 @ ec09ea6 ; newest verdict commit is ec09ea6
```

**Item 1b, performed: the header names the latest verdict.** PASS on that item.

**The ruling, first, because the report asks for one.** All five blocking items of
the twenty-first verdict are answered at the sites they named, and I verified each
by my own measurement rather than accepting the report's. This step closes. What
follows is six recordables under the BU0 criterion, one of them a measurement of
mine that moves nine generated figures, and none of them touching the gate's claim.

## Carried

Every item from the twenty-first verdict (`HOLD @ 2cf0c97`, committed `ec09ea6`),
re-measured at `9d70483`, plus the older carry.

- **R193 (blocking) -- CLOSED, and the measurement reproduces exactly.** Both
  named lines are rewritten (`tolerances.py:583-590` and the docstring at
  `test_corpus_configurations.py:1225-1232`); the extremal clause is gone from
  `floatfea/` and `tests/`. My own cell, not the report's:

  ```
  cell  inject k ULP into `injected_delta`, run the shipped calibration, at 9d70483
  out   +0 PASS  +1 PASS  +2 PASS  +2.5 FAIL  +3 FAIL  +4 FAIL  +5 FAIL
  out   unperturbed worst over 132 solved entries: 2.0000 ULP at
        `bt_calib_2ulp_thick_aniso5e4_L68` -- one of MY entries, which is what
        makes the "because the worst entry already sits 2 ULP" clause a cell and
        not a story
  ```

  The reason for `5.0` is now stated as definitional and the extremal claim is
  withdrawn. Correct, and correctly separated.
- **R194 (blocking) -- CLOSED.** `2.537e+07` survives once, inside the past-tense
  sentence recording the correction; `2.5e+07`, `2.4x` and `2.37x` are gone;
  `counter_defect_over_edge` and `counter_headroom_room` are cited by name at
  `:496`, `:498`, `:510`. The other half is closed too: R190, R191 and R192 are
  each classified in report section 4, which is where the Carried table says they
  are.
- **R195 (blocking) -- CLOSED.** No live statement says the histogram is seeded.
  Both pointers name `calibration_ulp_worst`. The counts pasted beside the grep do
  not reproduce -- **R203**, recordable, and the claim they support is true.
- **R196 (blocking) -- CLOSED, and the sweep reproduces to the digit.** My own
  run of the shipped construction, one variable moved:

  ```
  conv     1e-1     1e-2     1e-3     1e-4     1e-6     1e-8    1e-10    1e-12
  plateau     1        2       36       57       57       57       57       57
  min   7630.23  7630.16  7630.16  7630.16  7630.16  7630.16  7630.16  7630.16
  max   23926.2  23919.1  23918.6  23918.6  23918.6  23918.6  23918.6  23918.6
  ```

  Identical to report section 3. The entry names `boundary_margin_min_plateau`,
  states the convergence between `1e-3` and `1e-4`, cites no withdrawn figure as
  live, and tabulates nothing (BI3). This is the item done properly.
- **R197 (blocking) -- CLOSED on both clauses of its condition; the reach
  paragraph is answered but not exact.** Two cells ship, three defective bodies
  ship as negative controls, and I ran my own harness over all six bodies rather
  than reading the table:

  ```
  body                                    gate cell   ceiling cell
  shipped: calibration ULP                admits      admits
  shipped: exempt-response drift          admits      admits
  shipped: counter-defect size            admits      admits
  control: R163's body                    REJECTS     admits
  control: R173's body                    REJECTS     admits
  control: R197's wrong-quantity body     admits      REJECTS
  ```

  Three for three both ways. The wrong-quantity body I built last round is
  reproduced faithfully and is now rejected. Its residue is **R200** and **R201**,
  both recordable.
- **R198 (recordable, 4a) -- ACCEPTED as 4a by the report, agreed.**
- **R199 (recordable, 4a) -- ACCEPTED, and taken anyway.** The paragraph inserted
  below the sentence at `F2.md:672-678` says what my 458-base run measured. Good
  call to answer it beside the sentence rather than edit a true sentence.
- **R186, R191, R192 -- closed inside R193/R194/R195**, and this time at the
  sites, not by declaration. The `no change` table now says which line of each
  `Closed when` range was rewritten and where the hunk is. That is the discipline
  the twenty-first verdict asked for and it was applied.
- **R181, R189, R190, R170/R171 remainder, R172, R159, R162, R151, R152 -- 4a,
  ACCEPTED**, unchanged from my endorsement last round.
- **R182, R183, R184, R185, R187, R188 -- closed in revision 21**, verified then.
- **R173 to R180 -- closed in revisions 20 and 21.** R163's and R173's bodies now
  ship as negative controls, which is the right place for them.
- **R134, R135, R137 (recordable) -- OPEN, UNTOUCHED**, seventeenth round.
- **R129, R131, R132, R136, R138, R139, R148 -- as declared.**
- **R113, R95, R97, R98, R100, R101, R102, R103 -- OPEN, correctly declared.**
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict; the report lists it 4a.**
  Recorded as a disagreement, not a finding, for the fourth round.
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, 4a or
  later.
- **R68's standard -- MET, sixth round.**

## Findings

All six are **recordable and go to 4a**. None touches the gate's assertion, none
touches a tolerance value or the form of one, and the two that touch a published
number are numbers that understate a claim I verified independently.

**R200. (recordable, 4a) The meta-test's reach paragraph has the direction of its
own first limitation backwards. A correct counter written the long way is
REJECTED by the gate cell, and the file goes red on it -- the pair over-rejects
where the docstring says it under-covers.** `tests/test_counters_are_injected.py:36-39`.

```
code  :36-39 "a counter that reimplements its gate's comparison inline rather
      than calling it would pass that cell -- it is then the ceiling cell's job,
      and a body that does both (reimplements the comparison AND is sized by the
      constant) is a correct counter written the long way, not a defect"
cell  MY BODY H2: it does exactly both. It reimplements the calibration's
      comparison inline -- perturb `injected_delta` by
      `DELTA_CALIBRATION_ULP_COUNTER * ulp(CD)`, compute the ULP measure, assert
      it exceeds `CORPUS.DELTA_CALIBRATION_ULP` -- and it reads the module
      constant, so it IS sized by it.
out   clean=passes   gate cell = REJECTS   ceiling cell = admits
judge `_gate_cell` returns False, so the assertion on it FAILS and
      `test_the_counter_fails_when_its_gate_is_neutered` is RED, with a message
      that calls the body R163 and R173. There is no ceiling cell's job left to
      do: the pair has already failed. The limitation is real and it is a
      FALSE POSITIVE, not the false negative the bullet describes.
```

Conservative, so nothing bad gets in. Recorded because the paragraph is what a
reader consults when the meta-test reddens on a counter they believe is correct,
and what it tells them is that the file is fine with such a body.

**Closed when** the bullet states the measured direction: a counter that does not
call its gate by name fails the gate cell whether or not it is correctly sized, so
counters registered here call their gate.

**R201. (recordable, 4a) The two cells are conjoined but not required to fire on
the same mechanism, so a COMPOSED body passes both and is not a counter. The
guarantee the pair actually delivers is bounded, and the bound is measurable.**
`tests/test_counters_are_injected.py:28-31`, `:40-43`.

```
cell  MY BODY H1 = the shipped `_control_wrong_quantity` (calls the gate,
      injects a 100 percent relative error where the constant says N ULP) with
      R163's shape bolted on: assert DELTA_CALIBRATION_ULP is below
      DELTA_CALIBRATION_ULP_COUNTER.
out   clean=passes   gate cell = admits   ceiling cell = admits   -- BOTH PASS
judge the gate cell is satisfied by the injection half, the ceiling cell by the
      arithmetic half, and nothing requires them to be the same half. Nothing in
      H1 ever measures whether a 5-ULP perturbation is detected, which is the
      property `DELTA_CALIBRATION_ULP_COUNTER` exists to assert.
cell  and the BOUND, solved rather than argued: widen the constant with H1 and
      with a looser bolt (H3, whose bolt compares against 1e3 times the counter)
out   ceiling  4.0   4.9    6.0    40    400    4000   1e6   1e9
      shipped  GREEN GREEN  GREEN  red   red    red    red   red
      H1       GREEN GREEN  red    red   red    red    red   red
      H3       red   red    red    red   red    red    red   red
judge H3 is rejected by the ceiling cell at the SHIPPED value: a bolt must fire
      at WIDEN times the declared injection to be admitted, so the widening any
      both-cells-green body can hide is capped at WIDEN times that injection --
      50 ULP here, 12.5x the ceiling. The pair is doing real work. What it does
      NOT prove is that the injection is in the constant's quantity.
```

**Closed when** the reach paragraph states what the conjunction proves -- that the
constant cannot move past WIDEN times its declared injection without something
reddening -- rather than that the counter is sized by it.

**R202. (recordable, 4a) Report section 1's "6 failed" cell carries no `cmd`, and
does not reproduce under the obvious one: 11, not 6.**
`docs/reports/F2/step-4.md:3583-3588`.

```
report cell: DELTA_CALIBRATION_ULP = 1e9 at this commit, one variable moved
       out:  6 failed -- both cells on calibration ULP and on exempt-response
             drift, R163's control, and the plan test.
       There is no cmd line at all.
cmd    clone at 9d70483, `DELTA_CALIBRATION_ULP` 4.0 -> 1e9, python -m pytest -q
out    11 failed, 1387 passed. The six named, PLUS
       test_exempt_pair_responses.py::test_every_recorded_pair_is_still_detected
       test_exempt_pair_responses.py::test_a_MOVED_response_is_caught
       test_plan_figures.py::test_the_generated_figures_are_not_stale
       test_corpus_configurations.py::test_a_LARGER_deviation_fails_the_calibration
       test_tolerance_counter_cases.py::test_the_ceiling_sits_below_its_counter_case
judge  6 is what the meta-test file plus the plan test alone produce. The claim
       the cell supports -- that the widening was never silent repo-wide -- is
       TRUE and stronger than stated. BF0 asks for the command precisely so a
       reader does not have to guess which subset a number came from; here I had
       to.
```

**Closed when** the cell carries its `cmd` and the count is the count that command
prints.

**R203. (recordable, 4a) Report section 2's grep counts contradict the command
beside them and contradict each other in one line.**
`docs/reports/F2/step-4.md:3620-3626`.

```
report cmd: grep -rn seeded over docs/milestones/F2.md floatfea/ tests/ scripts/
       out: "9 hits. Eight are the word unseeded ..." followed by NINE
            enumerated locations, then "The ninth is tolerances.py:619-620"
cmd    that command, binaries excluded
out    11 matching lines, of which 9 contain "unseeded"; the remaining two are
       tolerances.py:619 and :620, the record sentence
judge  eight / nine / eleven: the sentence is inconsistent with its own list
       before it is inconsistent with the command. The substance is right and I
       checked it independently -- a case-insensitive grep for the three live
       phrasings over floatfea/, tests/, scripts/ and docs/milestones/ returns
       only the record sentence.
```

**Closed when** the two counts are what the pasted command prints.

**R204. (recordable, 4a) `RAISED_COUNTER_DEFECT_FACTOR`'s marker carries a causal
"because" and not the boundary that makes the choice invertible. Solved, the
boundary is 2.3 -- 2.4, which is `counter_headroom_room`, and `1e3` sits 422x
above it.** `tests/verification/rung1/test_corpus_configurations.py:1394-1399`.

```
code  :1396-1398 "Three orders is used because that is inside the range the
      suite tolerated before the guard existed."
cell  INVERT THE DECISION RULE AND SOLVE. One variable moved, the shipped
      `test_a_RAISED_counter_defect_breaks_that` run at each value:
out   factor 1.0 RED   2.0 RED   2.3 RED   2.4 GREEN   3 GREEN   1e3 GREEN
      1e6 GREEN
judge the boundary is between 2.3 and 2.4 -- it is `counter_headroom_room`,
      published as 2.37x, and it is the same number twice. Below it the guard
      goes RED rather than vacuous, which is the property that matters and which
      nothing states. The shipped 1e3 sits 422x above the boundary.
```

**Closed when** the marker states the boundary (`counter_headroom_room`, and that
below it the test reddens rather than passing) instead of, or beside, the causal
sentence.

**R205. (recordable, 4a -- and delivered as corpus rather than as a demand) The
published detection edge is beatable from outside the corpus.
`counter_headroom_room` falls from 2.368x to 2.185x.
`PATCH_TEST_COUNTER_HEADROOM = 6.0e7` still holds.**

```
cell  about 10,000 admissible holding bases of my own through the SHIPPED
      `_detection_edge`, at 9d70483
out   random axis / skew / vertical / in_plane_y bases with NO roll floor at
      about 9.77e-14 -- a plateau hit to four digits by shapes spanning
      D 0.03..4.5 m and L/D 3..1e4, so it is not a minimum over those either.
      The band below is reached only by RAW DIRECTION VECTORS WITH A ROLL, which
      is what `aaa_band_edge_twin` carries. In that family:
        3.642482e-14   CD/edge 2.7454e+07x   room 2.185x
        3.725032e-14   CD/edge 2.6845e+07x   room 2.235x
        3.804467e-14   CD/edge 2.6285e+07x   room 2.283x
      against the published 3.945903e-14 / 2.534e+07x / 2.368x
judge THE HEADROOM HOLDS. Breaking `6.0e7` needs an edge below 1.6667e-14 and I
      could not get within a factor of two of it. What moves is the published
      room, by 8 percent, and `detection_edge_at`, which has named the same
      planted entry for five rounds.
```

Nothing here asks for a constant to move. The three entries are in
`tests/corpus/`; regenerating is the next report's work, and the reason is a
corpus round.

**R206. (recordable, 4a) The sentence that says a generated number is cited by name
or not written retypes one on its next line, and my corpus round moves it this
round.** `floatfea/tolerances.py:509-513`.

```
code  :509-511 "This line read 2.537e+07 while counter_defect_over_edge and the
      test that prints it both read 2.534e+07"
      :512-513 "a number that is generated is cited by name or it is not written"
cmd   regenerate the figures with my corpus applied
out   counter_defect_over_edge  2.534e+07x -> 2.745e+07x
judge tensed as history, so it stays true as history, and that is why this is
      not blocking. It is recorded because the species is exactly the one the
      sentence records, one line apart, and because it is no longer hypothetical.
```

**Closed when** the record sentence names the figure or drops the second number.

## Tolerances touched

**None. No value changed, none moved, none removed, none widened.**

```
cmd  git diff ec09ea6..HEAD -- floatfea/tolerances.py, comment lines stripped
out  (empty) -- every changed line in that file is a comment
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COUNTER_HEADROOM` `:515` | `6.0e7` | `6.0e7` (unchanged) | ratio, dimensionless | the raised-defect counter, injected and registered in both cells (verified) | `tolerances.py:491-514`. Retyped figures removed, R194 closed. Room falls to `2.185x` under my corpus -- **R205**; the record sentence retypes a live figure -- **R206**. |
| `BOUNDARY_BISECTION_CONVERGENCE` `:539` | `1e-6` | `1e-6` (unchanged) | relative bracket width, dimensionless | none -- CLASS STRUCTURAL, exempt under AO2 | `tolerances.py:517-538` and `F2.md:680-686`. Reason now MEASURED and I reproduced the sweep to the digit. **This entry is now the model for the others.** |
| `DELTA_CALIBRATION_ULP_COUNTER` `:590` | `5.0` | `5.0` (unchanged) | ULP multiple, dimensionless | is itself the injection; injected through the gate (verified) | `tolerances.py:571-589`. Boundary corrected and reproduced by me: `+2` passes, `+3` fails. Reason is definitional and says so. |
| `EXEMPT_RESPONSE_DRIFT_ULP` `:626` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `10.0`, injected (verified) | `tolerances.py:595-625`. Pointer now names `calibration_ulp_worst`, R195 closed. |

**The ruling on `RAISED_COUNTER_DEFECT_FACTOR`, asked for explicitly: it is NOT a
tolerance, the `not-a-tolerance` marking stands, and it does not move to
`floatfea/tolerances.py`.** Three reasons, the first measured rather than argued:

```
cell  add PATCH_TEST_COUNTER_HEADROOM_COUNTER = 1.0e3 to tolerances.py in a
      clone at 9d70483, run the counter-cases rung
out   1 failed --
      test_structural_tolerances_do_NOT_carry_a_counter_case[PATCH_TEST_COUNTER_HEADROOM]
      "is STRUCTURAL but carries a counter-case. Either it is really an ACCURACY
      tolerance and the CLASS is wrong, or the counter-case is invented."
judge the repository's own locked taxonomy (AO2) FORBIDS the move under the
      obvious name. Moving it in under any other name pulls in
      `test_every_float_tolerance_declares_a_class` and a CLASS for a multiplier.
```

Second: nothing is accepted or rejected by comparison with it -- it appears only
as the shipped defect times the factor, and inside the widened ceiling. Third, and
the reason I am comfortable: it cannot go vacuous silently. Solved above (R204),
the guard goes **RED** at 2.3 and green at 2.4, so a value too small to exercise
the assertion fails loudly rather than passing. What is missing is that number in
the comment, which is R204 and is 4a.

**My own support for two shipped values, offered because they rest on entries I
planted.** `DELTA_CALIBRATION_ULP = 4.0` is twice an observed maximum of 2 ULP.
I measured 11,000 further admissible holding configurations this round from a new
seed: 2,000 broad (histogram 0 x1589, 1 x411; maximum **1.0000 ULP**) and 9,000
targeted at the thick-wall / high-anisotropy / short-member region (0 x6308,
1 x2680, 2 x12; maximum **2.0000 ULP**). With last round's 2,596 that is **13,596
configurations and nothing above 2.0000 ULP**. The `2x` headroom is not
threatened, and neither is the `+2 passes / +3 fails` boundary the round
publishes, since that rests on the worst entry sitting at 2.

**What held.** These reproduce at my run: `1398 passed, 0 failed, 0 skipped`;
`regen_figures.py --check` green; the ULP injection boundary; the
`BOUNDARY_BISECTION_CONVERGENCE` sweep to the digit; the two cells' separation of
three defective bodies from three shipped ones, run from my own harness; the
raise-factor boundary at 2.3 / 2.4; 121 + 3 + 8 = 132 = `corpus_solved`;
127 converged + 5 refused + 0 unbracketed = 132. These do **not**: the reach
paragraph's first bullet (R200); the "6 failed" cell (R202); the "9 hits, eight
unseeded" cell (R203).

## Next step opens when

**Now. Step 4 closes and step 5 (V1.1, rigid-body modes) opens.**

The five blocking items are answered at their named sites and I verified each by
my own measurement: the ULP boundary, the convergence sweep, the seeded grep, the
retyped ratio, and the two cells with my own adversarial bodies run through them.
Rung 1 is green at `9d70483`, `floatfea/` production code is untouched for a
seventh consecutive round, no constant moved and none was widened, no test was
skipped, xfailed or deleted, my instructions are byte-identical, and the plan,
step and report commits are correctly routed.

**The BU0 classification, endorsed again.** R181, R189, R190, the R170/R171
remainder, R172, R159, R162, R151, R152 and the older set are apparatus; so are
R198 and R199; so are R200 through R206 above. The criterion held this round in
the direction that matters: it did not stop me finding anything, and it stopped
the findings from becoming a twenty-third round about a docstring bullet and two
grep counts. **Six items open at 4a's lock, each with a closing condition written
above.**

**Carried into step 5 as the two things I want re-read.** First, R200 and R201 are
about the guard that will police every counter step 5 writes; the rigid-body modes
gate will need one, and the reach paragraph is what its author will read. Second,
`counter_headroom_room` is `2.185x` once my corpus is regenerated, not `2.37x`,
and that entry's own Reason says the margin is eaten from both sides. Neither is a
reason to hold step 4.

**Adversarial corpus (BE3): 7 new entries committed, all unseen by the
implementer; every field measured at `9d70483` before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **163** entries, 139 solved,
committed separately at `5554f0d` immediately before this verdict and touching no
code. Full suite with the corpus applied: **1431 passed, 2 failed.**

The coverage measurement, stated plainly: **1 of my 7 new entries produces new
exempt-and-detected pairs, and BS2's golden file caught all three by name** --
`ch_edgefloor_D0p068_L387_skew` on `dropped_flip`, `dropped_shear_parameter` and
`wrong_dof_index`. The other six are invisible to BS2 and **visible to BT0**,
which reddens on nine rows. The rows that moved, and this is the point: for the
first time in five rounds **`detection_edge` 3.9459e-14 to 3.6425e-14**,
`detection_edge_at` from `aaa_band_edge_twin` to
`ch_edgemin_D0p0758_roll1p05_aniso9p4e5`, `counter_defect_over_edge` 2.534e+07x to
2.745e+07x and `counter_headroom_room` 2.37x to 2.19x -- four figures that had not
moved since they were first published, and the one shipped margin in this
milestone that a reviewer's input can eat. `clean_worst_ratio` 0.0887x to 0.0982x
at `ch_edgemin_D0p391_rollm0p73_aniso1p4e5`; `calibration_ulp_histogram` from
0 x121, 1 x3, 2 x8 to 0 x124, 1 x4, 2 x11; `boundary_margin_min_plateau` 57 to 60;
`exempt_detected` 51 to 54. `boundary_margin_min`, `boundary_margin_max`,
`boundary_margin_spread`, `calibration_ulp_worst` and every margin row did **not**
move. Sixth round running against input their authors never saw.

**Twenty-two consecutive rounds have found no element defect**, and the reading is
unchanged and is the one thing about this milestone I would not soften: not yet
contradicted, until V5.1 puts CalculiX on the other side. The apparatus went red
under my input twice this round; the element did not. Four defective counter
bodies of my own were correctly separated by the file written to separate them,
and two more that it does not separate are recorded above rather than fixed by me.

**Witness channel unavailable.** `git remote -v` is empty, so there is no PR and no
witness comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass.
Twenty-two consecutive reviews by one reader, and step 5 should open the remote
before it opens anything else -- the report says it will.

**The standing question, carried forward.** Last round I asked: when a round
deletes a mechanism, what deletes the sentences that described it? This round
answered it by hand at four sites and the answer held. The question for step 5 is
narrower and it comes from R200, R202 and R203 together: **every one of this
round's three misstatements is a claim about the repository that a reader could
check in one line, in a document whose own rule is that such claims carry their
command.** The rule is written; nothing runs it. Step 5 writes a gate that must
fail, and the sentences describing it will be written the same way.
