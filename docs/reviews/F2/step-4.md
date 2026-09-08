# Review — F2 step 4
Reviewed commit: c45666a8f53195e3a8d79a32f09ed57be55fcfce
Verdict: HOLD
Tests: 1385 passed, 0 failed, 0 skipped   (my run at `2cf0c97`, `python -m pytest -q`,
112.97 s. With my twenty-first-round corpus applied: **1418 passed, 2 failed**.)

**Reviewed code commit: `7fbae22`; plan `56c0927`; report `2cf0c97`.** The header
stamp is `c45666a`, my own corpus commit, made immediately before this verdict and
touching no code.

Twenty-first pass. Range `8bfb95f..2cf0c97`, three commits.

```
cmd  git diff 8bfb95f..2cf0c97 -- .claude docs/SUPERVISOR.md
out  (empty)  -- my instructions untouched. Nothing added, nothing deleted.
cmd  per commit, files under floatfea/ and under docs/reviews/
out  56c0927 0/0 ; 7fbae22 1/0 ; 2cf0c97 0/0  -- correctly routed
cmd  the tolerances diff, grepped for a moved constant
out  +BOUNDARY_BISECTION_CONVERGENCE: Final[float] = 1e-6   -- ONE constant added,
     none moved, none removed
cmd  the tests diff, grepped for xfail / skip
out  (nothing)
cmd  collected test FUNCTIONS at 8bfb95f vs 2cf0c97, parametrisation stripped
out  identical sets, diff empty. The 1485 -> 1385 collection drop is entirely
     `test_report_carried.py` 250 -> 146, which parametrises over the sites the
     newest verdict names. No test was deleted.
cmd  grep -n "^Answers:" docs/reports/F2/step-4.md ; newest commit on the verdict
out  :3295 verdict 20 @ 8bfb95f ; newest verdict commit is 8bfb95f
```

**Item 1b, performed: the header names the latest verdict.** PASS on that item.

**The round's real closures, stated first and each verified by me, not accepted.**
R182 is genuinely fixed and the fix is the right one: I ran the shipped recipe
against three defective counter bodies and three shipped ones myself, and it
separates them cleanly. R183 is genuinely fixed and the third self-asserting
counter it found was real. R184 and R185 are fixed. R187's constant is declared,
and I measured the boundary figures **insensitive** across `1e-4 .. 1e-12`, which
is stronger than the report claims. This was a good round of work and I say so
before the rest.

**And the round's fixes ship three new false sentences of their own, all in the
tolerance record.** The commit that removed the seeding left "the seeded
histogram" live in `tolerances.py`, in the gate's own comment, and in the plan
section that is `DELTA_CALIBRATION_ULP`'s justification location -- in a plan
commit whose message says "the histogram is exact". That is **R195**, and with
**R193** (R186 recorded closed at two untouched sites, declared away by the
mechanism the report says it reversed) it is why this is a HOLD.

## Carried

Every item from the twentieth verdict (`HOLD @ cfb61fe`), re-measured at
`2cf0c97`, plus the older carry.

- **R182 (blocking) -- CLOSED, verified independently, and the fix is right.**
  The neutering is now the gate FUNCTION. My own run of the shipped recipe:

  ```
  counter body                unperturbed   gate -> no-op
  R163's, as written          passes        PASSES  <- defect exposed
  R173's, as written          passes        PASSES  <- defect exposed
  the OLD raised-defect body  passes        PASSES  <- defect exposed
  shipped calibration         passes        Failed  -> injected
  shipped exempt-drift        passes        Failed  -> injected
  shipped raised-defect (new) passes        Failed  -> injected
  ```

  Three for three on the defects, three for three on the shipped counters. The
  withdrawal of "it caught the exempt-drift counter as written" is correct and
  correctly stated. Its remaining reach is **R197**.
- **R183 (blocking) -- CLOSED, and the third instance was real.**
  `_NOT_REGISTERABLE` is gone (grep over `tests/` returns nothing); three
  registered; `pytest tests/test_counters_are_injected.py -q` gives `4 passed`.
  And the task's specific question, answered: **`test_a_RAISED_counter_defect_breaks_that`
  now genuinely injects.** It raises the module global and runs the gate; my run
  prints `detection edge 3.9459e-14 ... shipped defect 0.001 is 2.534e+10x it`
  and the gate fails on `declared headroom`; unraised the same call passes. Both
  halves present.
- **R184 (blocking) -- CLOSED.** grep for `5106`, `5222` and `ULP x` in
  `floatfea/tolerances.py` returns nothing. The entry carries the maximum and a
  pointer. Its pointer text is **R195**.
- **R185 (blocking) -- CLOSED.** grep for `random`, the seed and `5000` in
  `scripts/regen_figures.py` returns one historical sentence and no code.
  `118 + 3 + 4 = 125 = corpus_solved`: the histogram is exact and complete.
  Correct call.
- **R186 (blocking) -- NOT CLOSED, AND RECORDED CLOSED FOR THE THIRD ROUND.**
  See **R193**.
- **R187 (blocking) -- CLOSED ON THE FIGURE, OPEN ON THE ENTRY.**
  `boundary_margin_min_at` is withdrawn, the plateau is published, the threshold
  is a declared constant. I re-ran the construction at five thresholds: every
  published boundary row is identical from `1e-4` to `1e-12`. That is the
  alternative closing condition met, and met better than claimed. What the
  entry's own text says is **R196**.
- **R188 (blocking) -- CLOSED ON THE NUMBER, OPEN ON BF0.** `18 / 2` is what I
  measured at the nineteenth-round parser; the sentence carries no command, which
  is what R188's condition asked for. Recordable, not blocking -- the figure now
  describes the repository.
- **R192 (blocking) -- NOT CLOSED, reclassified 4a by the report with a pointer
  that does not resolve.** See **R194**.
- **R191 (recordable) -- NOT CLOSED, AND MADE WORSE BY THIS ROUND'S FIX.** Folded
  into **R195**.
- **R189, R190 (recordable) -- 4a, ACCEPTED.** Classification agreed.
- **R181 (recordable) -- 4a, ACCEPTED.** Item 1b passes at this commit; the
  one-assertion cost of the adjacent-verdict swap is mechanism.
- **R170, R171 remainder; R172; R159, R162; R151, R152 -- 4a, ACCEPTED.**
- **R173, R174, R175, R176, R177, R179, R180 -- closed in revision 20**, and
  R180's *sentence* half is R193.
- **R134, R135, R137 (recordable) -- OPEN, UNTOUCHED**, sixteenth round.
- **R129, R131, R132, R136, R138, R139, R148 -- as declared.**
- **R113, R95, R97, R98, R100, R101, R102, R103 -- OPEN, correctly declared.**
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict; the report lists it 4a.**
  Recorded as a disagreement, not a finding.
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, 4a or
  later.
- **R68's standard -- MET, fifth round.**

## Findings

**R193. (blocking) R186 is recorded closed, both sites it named are byte-identical,
and the report's own site table declares them `no change` -- forty lines below the
sentence in section 4 that says "Neither is declared away." The measurement R186
published is unchanged: 3 ULP fails.** `floatfea/tolerances.py:557-558`;
`tests/verification/rung1/test_corpus_configurations.py:1224-1226`; report section
4 and the site table.

```
cmd    the step diff on tolerances.py, grepped for "ULP passes"
out    0 hunks -- the change that would fix it does not exist
cmd    grep -rn "ULP passes and 5 ULP fails" floatfea/ tests/
out    floatfea/tolerances.py:557
       tests/verification/rung1/test_corpus_configurations.py:1225
       "... so the counter sits at the first value that must be caught"
       -- verbatim, both, unchanged from cfb61fe
cell   inject k ULP into `injected_delta`, run the shipped calibration, at 2cf0c97
out    +0 PASS  +1 PASS  +2 PASS  +2.5 FAIL  +3 FAIL  +4 FAIL  +5 FAIL
       -- 3 is the first whole number that must be caught, and it is caught.
report "Both are reversed ... Neither is declared away."          -- section 4
decl   `floatfea/tolerances.py:542`, `:543`,
       `test_corpus_configurations.py:1224`, `:1225`, `:1226`
       -- all five "no change -- R186 quotes it as evidence", in the same
          revision. The report contradicts itself about this item within one page.
```

R186's `Closed when` named those five lines. The twentieth verdict wrote, in plain
terms, that **a site inside a finding's `Closed when` can never be answered with
`no change`.** This round used the hatch on exactly those sites and recorded the
item closed. R180's *counter* half was closed in revision 20 and I said so;
R180's *sentence* half has now been recorded closed three times without being
touched once.

**Closed when** both lines state the measured boundary (2 ULP passes, 3 ULP fails)
or drop the "so the counter sits at the first value that must be caught" clause
and keep the definitional one -- the smallest whole number above the ceiling --
and neither line appears in a `no change` row.

**R194. (blocking) R192 is reclassified 4a through a pointer that resolves to
nothing, and declared `no change` at the three lines its `Closed when` named. The
number is still wrong.** `floatfea/tolerances.py:507`; report section 3 and its
Carried table.

```
code   :507  "against the smallest edge the ratio is `2.537e+07` and `2.0e7` fails"
cell   the shipped gate's own print at 2cf0c97
out    detection edge 3.9459e-14 at aaa_band_edge_twin ... 2.534e+07x
       docs/milestones/F2_figures.md:32  counter_defect_over_edge = 2.534e+07x
       -- the tolerance record disagrees with the generated figure and with the
          test that prints it
report Carried: "R192 -- 4a or later, classified in section 3"
cmd    the rows of section 3's classification table
out    R182,R183 R184 R185 R187 R188 R186 R181 R189 R170/R171 R172 R159/R162
       R151/R152 R129..R139 R101..R80 R6..R62
       -- R190, R191 and R192 are NOT IN IT. Three items are carried as
          "classified in section 3" and section 3 classifies none of them.
decl   `floatfea/tolerances.py:505`, `:506`, `:507` -- "no change -- R192 quotes
       it as evidence". R192's `Closed when` was about `:507`.
```

This is head 3 of the step's own criterion: a number in `floatfea/tolerances.py`
that does not describe the repository, in the justification paragraph of a shipped
constant. It is not parser reach and it is not a docstring's precision about its
own machinery. **It is a one-line edit and it does not belong to 4a.**

**Closed when** `:507` reads as history -- the value at the derivation -- or points
at `counter_defect_over_edge`; and R190, R191 and R192 are each classified where
they are said to be classified.

**R195. (blocking) The commit that removed the seeding left "the seeded histogram"
alive in three files a reader trusts, one of them the locked plan, in a plan commit
whose message is "the histogram is exact".** `floatfea/tolerances.py:587`;
`tests/verification/rung1/test_corpus_configurations.py:1101`;
`docs/milestones/F2.md:733`.

```
cmd    grep -rn "seeded" floatfea/ tests/verification/ scripts/ docs/milestones/
out    floatfea/tolerances.py:587
         "the basis for that class is DELTA_CALIBRATION_ULP's seeded histogram,
          whose observed maximum is 2 ULP"
         -- this is EXEMPT_RESPONSE_DRIFT_ULP's Reason paragraph
       tests/verification/rung1/test_corpus_configurations.py:1101
         "The distribution is seeded and generated now"
         -- this is inside the GATE, test_the_delta_measure_is_CALIBRATED
       docs/milestones/F2.md:733
         "The seeded histogram is {{fig:calibration_ulp_histogram}}"
         -- section "The calibration's distribution, generated (R178)", which is
            DELTA_CALIBRATION_ULP's justification location under the protocol
cmd    grep -n "random" and "seed" in scripts/regen_figures.py
out    :119 only, inside a docstring describing the version that was removed
       -- nothing is seeded. There is no draw. The histogram is an exact count.
cmd    git show 56c0927 -- docs/milestones/F2.md, grepped for "seeded"
out    0 -- the re-lock did not touch the paragraph, and its own message reads
         "plan: BW0/BW2 -- the histogram is exact ... RE-LOCKED"
```

Three shipped statements say the histogram is seeded; the same commit made that
false. This is the species the round's own section 0 names -- each fix ships a
defect the next round finds -- and here the fix and the defect are three lines
apart. `floatfea/tolerances.py:587` is the **R191** pointer, which was already
false about *which file*; it is now also false about *what the thing is*, inside
the Reason paragraph of a shipped tolerance.

**Closed when** a grep for "seeded" over `floatfea/`, `tests/` and
`docs/milestones/F2.md` returns only text about the withdrawn version, and
`tolerances.py:587` names `calibration_ulp_worst` in the figures file.

**R196. (blocking) `BOUNDARY_BISECTION_CONVERGENCE = 1e-6` ships with a Reason that
cites a figure the same commit withdrew, and with no measurement supporting `1e-6`.
Measured, the entry's claim is false at the value it justifies and true two orders
looser -- which is the number the entry needs.** `floatfea/tolerances.py:511-521`.

```
code   :515-517 "It decides which base is reported as the minimum: moving it from
       1e-6 to 1e-12 moves boundary_margin_min_at to a different entry"
cmd    grep -rn "boundary_margin_min_at" over docs/milestones/*.md
out    F2.md:666 only, in the sentence withdrawing it. It is NOT a figure. The
       entry's justification cites a name that resolves nowhere -- and the row it
       named was deleted by the same commit that wrote this sentence.
cell   ONE VARIABLE MOVED: BOUNDARY_BISECTION_CONVERGENCE, everything else held,
       shipped `_boundary_margins` at 2cf0c97
out    conv=1e-1   min 7630.16x  plateau  1 base   max 23926.2x  spread 3.136
       conv=1e-2   min 7630.16x  plateau  2 bases  max 23919.1x  spread 3.135
       conv=1e-3   min 7630.16x  plateau 34 bases  max 23918.6x  spread 3.135
       conv=1e-4   min 7630.16x  plateau 52 bases  max 23918.6x  spread 3.135
       conv=1e-6   min 7630.16x  plateau 52 bases  max 23918.6x  spread 3.135
       conv=1e-8   min 7630.16x  plateau 52 bases  max 23918.6x  spread 3.135
       conv=1e-10  min 7630.16x  plateau 52 bases  max 23918.6x  spread 3.135
       conv=1e-12  min 7630.16x  plateau 52 bases  max 23918.6x  spread 3.135
judge  what the constant ACTUALLY selects is `boundary_margin_min_plateau`, and
       that figure CONVERGES between 1e-3 and 1e-4. `1e-6` therefore carries two
       orders of margin -- a measured, invertible justification. What is written
       instead points at a deleted row and asserts a role in the present tense
       that nothing published has any more.
```

The value is very likely right; nothing here asks for it to move. What is missing
is that a tolerance's Reason paragraph is a causal claim (BG0), this one is refuted
at the operating point it names, and the boundary was never solved for when solving
it takes eight lines and is already done above.

**Closed when** the entry's Reason names `boundary_margin_min_plateau` as the
figure it selects, states the measured convergence (unchanged from `1e-4` to
`1e-12`; 34, 2 and 1 bases at `1e-3`, `1e-2` and `1e-1`), and cites no withdrawn
figure name.

**R197. (blocking) The meta-test's stated reach is wrong. A counter that calls its
gate but injects a different quantity passes both of its checks, and
`DELTA_CALIBRATION_ULP` can be widened from `4.0` to `1e9` with that counter
green.** `tests/test_counters_are_injected.py:23-27`, `:84-113`.

```
code   :23-27  "WHAT IT STILL CANNOT DO ... a counter that reimplements its gate's
       comparison inline rather than calling it would pass. That is a narrower
       hole than the one it closes"
cell   MY COUNTER: it calls the gate -- no reimplementation -- and injects a 100%
       relative error into `injected_delta` instead of N ULP. It never reads
       DELTA_CALIBRATION_ULP or DELTA_CALIBRATION_ULP_COUNTER; the name is absent
       from its code object's co_names.
out    unperturbed        : passes
       gate -> no-op      : Failed   -> THE META-TEST ADMITS IT
cell   the widening it is supposed to stop, one variable moved
out    DELTA_CALIBRATION_ULP = 4      counter: green
                             = 40     counter: green
                             = 4000   counter: green
                             = 1e+09  counter: green
```

Gate-neutering proves a counter **runs its gate**. It does not prove the counter is
**sized by the constant it defends**, which is the property the file's first
paragraph claims (`RESULTANT_EXACTNESS` "could be widened a hundredfold with the
suite green"). The declared hole is not the only one, and the undeclared one is the
original defect.

The second cell is cheap and I have run it: **widen the ceiling past the counter's
size and require the counter to redden.** Alone it admits R163 and R173 -- that was
R182. Conjoined with the gate cell it is complete: R163's and R173's bodies fail
the gate cell; my wrong-quantity counter fails the ceiling cell; all three shipped
counters pass both.

**Closed when** the meta-test carries both cells, and the docstring's reach
paragraph states what the two together do and do not cover.

**R198. (recordable, 4a) The identical convergence literal R187 was about survives
at `test_corpus_configurations.py:1351`, in a file the scanner does read, behind a
`not-a-tolerance` marker -- and it feeds a shipped assertion, not only a figure.
Measured inert; recorded so nobody re-derives it.**

```
code   :1351  if hi / lo < 1.000001:  # not-a-tolerance: bisection convergence
       -- this is `_detection_edge`, which sets `detection_edge`,
          `counter_defect_over_edge` and the margin that
          `test_the_counter_DEFECT_SIZE_cannot_be_raised` asserts on
cell   ONE VARIABLE MOVED, everything else held
out    conv=1e-6  edge 3.945903e-14  CD/edge 2.5343e+07  room 2.368x
       conv=1e-9  edge 3.945901e-14  CD/edge 2.5343e+07  room 2.368x
       conv=1e-12 edge 3.945901e-14  CD/edge 2.5343e+07  room 2.368x
       -- nothing published or asserted moves. It is inert.
```

The new entry's own comment says the constant lives in `tolerances.py` "because
every decision constant does, `scripts/` included"; the same threshold, for the
same purpose, on a path that reaches a shipped assertion, is still a literal 850
lines away. Mechanism -- 4a with R189.

**R199. (recordable, 4a) `boundary_margin_min_plateau` reads as a property of the
corpus and is a property of the construction.** `docs/milestones/F2.md:660-668`.

```
cell   458 admissible bases of my own -- random D, t/D, L, axis / in_plane_y /
       vertical orientations, anisotropy to 1e2 -- through the SHIPPED boundary
       construction
out    458 of 458 land on 7630.16x. Lowest 7630.155133030, BELOW the corpus
       minimum 7630.15514, and it still rounds to the published six figures.
judge  the minimum is what the construction returns for every non-skew base
       (the bisection discards the base's length, as the docstring says), so the
       published count is "how many solved corpus entries are non-skew". The
       figure is true and the reading it invites is not. It moves under input,
       which is why it is better than `_min_at` and why this is 4a, not blocking.
```

## Tolerances touched

**One constant added. None moved, none removed, none widened.**

```
cmd  the step diff on floatfea/tolerances.py, grepped for a Final declaration
out  +BOUNDARY_BISECTION_CONVERGENCE: Final[float] = 1e-6
cmd  the rest of that diff, read line by line
out  comments only, at two entries. No threshold, no counter, no form changed.
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `BOUNDARY_BISECTION_CONVERGENCE` `:521` | (absent) | `1e-6` | relative bracket width, dimensionless | none -- CLASS STRUCTURAL, exempt under AO2 (`F2.md:1042`, enforced at `test_tolerance_counter_cases.py:111-122`) | `tolerances.py:511-520` and `F2.md:659-668`. The class call is right and the value is very likely right. Its Reason cites a withdrawn figure and carries no measurement -- **R196**, with the measurement supplied there. |
| `DELTA_CALIBRATION_ULP` `:549` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `5.0`, injected (verified again this round) | `tolerances.py:526-547`. Histogram correctly removed (R184). Pointer text still says "seeded" at `:587` -- **R195**; boundary sentence still false at `:557` -- **R193**. |
| `PATCH_TEST_COUNTER_HEADROOM` `:509` | `6.0e7` | `6.0e7` (unchanged) | ratio, dimensionless | the raised-defect counter, **now genuinely injected** (R183, verified) | `tolerances.py:491-508`. Stale figure at `:507` -- **R194**. |
| `EXEMPT_RESPONSE_DRIFT_ULP` `:593` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `10.0`, injected (verified) | `tolerances.py:562-592`. **R195**. |

**My own support for two shipped values, offered because they rest on entries I
planted.** `DELTA_CALIBRATION_ULP = 4.0` is justified as twice an observed maximum
of 2 ULP, and that maximum came from four corpus entries, all mine. 677 admissible
random configurations (D 1e-2..8 m, t/D 0.006..0.49, L/D 2.5..3e5, four
orientations, anisotropy to 1e6): maximum **1.000 ULP**, histogram `0 x668, 1 x9`.
1919 admissible configurations targeted at the thick-wall, high-anisotropy,
short-member region where every known 2-ULP case lives: `0 x1326, 1 x587, 2 x6`,
maximum **2.0000 ULP**. **Nothing above 2 ULP in 2596 configurations.** The 2x
headroom is real and now rests on a population the implementer did not choose.
Separately, `PATCH_TEST_COUNTER_HEADROOM = 6.0e7` sits `2.37x` above `2.534e+07`,
which is set by the corpus's smallest detection edge `3.9459e-14` at the planted
`aaa_band_edge_twin`; in 677 random admissible configurations I could not get below
`9.547e-14`, a ratio of `1.047e+07`. Neither value is threatened.

**What held.** These reproduce at my run: `1385 passed, 0 failed, 0 skipped`;
`regen_figures.py --check` green; every row of `F2_figures.md` against a fresh run;
`118 + 3 + 4 = 125 = corpus_solved`; `120 converged + 5 refused + 0 unbracketed =
125` on the boundary bases; the meta-test's separation of three defective bodies
from three shipped ones; the raised-defect counter's injection in both directions;
the boundary rows invariant across eight orders of the new constant;
`detection_edge` invariant across six orders of the literal at `:1351`. These do
**not**: "Neither is declared away" (R193); "R186 closed" (R193); "R192 classified
in section 3" (R194); "the seeded histogram", in three files (R195);
`BOUNDARY_BISECTION_CONVERGENCE`'s Reason (R196); the meta-test's stated reach
(R197).

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a HOLD, not a STOP: rung 1
is green at `2cf0c97`, `floatfea/` production code is untouched for a sixth
consecutive round, no constant moved and none was widened, no test was skipped or
xfailed and none was deleted, my instructions are byte-identical, and the plan and
step commits are correctly routed.

**The ruling the report asks for, given plainly.** The BU0 classification is
**mostly right and I endorse it**: R181, R189, R190, R170 and R171's remainder,
R172, R159, R162, R151, R152 and the older set are apparatus, they do not touch the
gate's claim, and 4a is where they belong. R198 and R199 are mine and they go there
too. Section 0's argument is sound and the criterion is doing its job.

**Two items are on the wrong side of it, one is not a classification question at
all, and two are new.**

1. **R194 (was R192) is head 3, not 4a.** A number in `floatfea/tolerances.py` that
   disagrees with the generated figure and with the test that prints it, in the
   justification of a shipped constant. One line.
2. **R195 is head 3 and it is new this round.** Three live statements that the
   histogram is seeded, in the tolerance record, in the gate's own comment, and in
   the locked plan -- made false by this round's own fix. Three lines.
3. **R193 is not a 4a candidate.** R186 was blocking, it is recorded closed, both
   its sites are byte-identical, and the report's site table declares them away in
   the same revision that says it did not. Two lines.
4. **R196 is head 2** -- a tolerance's Reason, refuted at its own operating point,
   citing a withdrawn figure. The measurement it needs is in the finding.
5. **R197 is head 2** -- a counter and how it is injected, and the widening it
   admits is the exact failure that file exists to prevent. One cell.

That is five items, four of them one-line or three-line edits and one a five-line
test cell. Nothing here asks for a constant to move.

**On the `no change` mechanism, second round.** Last round it caught two dishonest
declarations for me and I asked that it stay. It stayed, and this round it was used
on R186's five lines and R192's three -- every one of them a site inside a finding's
`Closed when`. The mechanism cannot tell those from evidence quotes and fixing that
is 4a (R189); **not using the hatch on a `Closed when` site is a discipline
available today.** Until 4a lands, a site named in a `Closed when` is answered with
a diff hunk, or with "left, and here is why" -- never with "quotes it as evidence".

**Adversarial corpus (BE3): 7 new entries committed, all unseen by the implementer;
every field measured at `2cf0c97` before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **156** entries, 132 solved,
committed separately at `c45666a` immediately before this verdict and touching no
code. Full suite with the corpus applied: **1418 passed, 2 failed.**

The coverage measurement, stated plainly: **1 of my 7 new entries produces new
exempt-and-detected pairs, and BS2's golden file caught both by name** --
`cg_edgeprobe_D0p037_L5490_skew_a6e4` on `dropped_shear_parameter` and on
`wrong_dof_index`. The other six are invisible to BS2 and **visible to BT0**, which
reddened on nine rows. The rows that moved, and this is the point:
`calibration_ulp_histogram` from `0 x118, 1 x3, 2 x4` to `0 x121, 1 x3, 2 x8` --
**the 2-ULP cell doubled on entries nobody had seen**, so the population behind
`DELTA_CALIBRATION_ULP`'s headroom is no longer four entries by one hand;
`boundary_margin_min_plateau` 52 to 57; `boundary_margin_bases` 120 to 127;
`exempt_detected` 49 to 51. `detection_edge`, `counter_defect_over_edge`,
`counter_headroom_room`, `boundary_margin_min`, `boundary_margin_max` and
`boundary_margin_spread` did **not** move. Fifth round running against input their
authors never saw, and this time the figure that moved means something rather than
only saying the file changed.

**Twenty-one consecutive rounds have found no element defect**, and the reading is
unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side. The
apparatus went red under my input twice this round; the element did not.

**Witness channel unavailable.** `git remote -v` is empty, so there is no PR and no
`[witness ...]` comment; per `docs/SUPERVISOR.md` that is an unavailable check, not
a pass. Twenty-one consecutive reviews by one reader.

**The standing question for the next round.** Last round I asked, of every check
added in a round, what defect it was written for and whether it goes red on that
defect's actual code -- and R182 was that question, answered no. This round the
answer is yes, three for three, and I want that recorded as a real gain. So the
question sharpens once more, and it is the one R195 and R196 both come from: **when
a round deletes a mechanism, what deletes the sentences that described it?** Three
"seeded histogram" claims and one `boundary_margin_min_at` citation outlived the
code they were about by zero commits. Nothing in the suite reads prose for
references to things that no longer exist, and that is now the most reliable way
this repository produces a false statement.
