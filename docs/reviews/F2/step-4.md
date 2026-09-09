# Review — F2 step 4
Reviewed commit: 45550a3cee7f52bfcd27eaf890e3627c87cedaf7
Verdict: HOLD
Tests: 1518 passed, 0 failed, 0 skipped   (my run at `3e225c5`, `python -m pytest -q`,
157.73 s. With my twenty-fourth-round corpus applied: **1540 passed, 1 failed**.)

**Reviewed code commit: `3e225c5`.** The header stamp is `45550a3`, my own corpus
commit, made immediately before this verdict and touching no code.

Twenty-fourth pass. Range `dfcee3a..HEAD`, three commits. **All three blocking
items are answered at their named sites and I verified each one by running it,
not by reading it.** R207's new generated figure is the best piece of work in
this round and I tried three ways to make it lie; it did not. R208 is closed at
both sites. R209 is closed in `tolerances.py`.

**And the paragraph R207 was about acquired a new defect in the commit that
fixed it.** The bold sentence leading the withdrawal -- declared *left
deliberately* -- is a causal claim about what consumes this tolerance's margin,
its supporting measurement was deleted three lines below it in this same commit,
and the replacement measurement points the other way. That is R211, and it is
the one thing I hold on.

```
cmd  git diff dfcee3a..HEAD -- .claude docs/SUPERVISOR.md
out  (empty)  -- my instructions untouched. Nothing added, nothing deleted.
cmd  git diff dfcee3a..HEAD -- floatfea/ --stat
out  floatfea/tolerances.py | 35 +++++++++--------- AND NOTHING ELSE
cmd  git diff dfcee3a..HEAD -- floatfea/tolerances.py, non-comment changed lines
out  (empty)  -- every changed line is a comment. No value moved.
cmd  git diff dfcee3a..HEAD -- tests/
out  (empty)  -- no test, no golden file, no fixture
cmd  git log --format='%h %s' dfcee3a..HEAD ; any commit touching docs/reviews/
out  d89dfee plan / 6eed45e step / 3e225c5 report -- none touches docs/reviews/
cmd  grep -n "^Answers:" docs/reports/F2/step-4.md | tail -1 ; newest verdict
out  :3823 verdict 23 @ dfcee3a ; newest verdict IS 23 @ dfcee3a
cmd  python -m pytest -q 2>&1 | tail -1
out  1518 passed, 2 warnings in 157.73s
cmd  python scripts/regen_figures.py --check
out  regen_figures: up to date  -- exit 0
```

**Item 1b, performed, and it does not trigger.** The report's header names verdict
23 and verdict 23 is the newest. One comparison, made.

## Carried

Every item from the twenty-third verdict (`HOLD @ fc30b71`, committed `dfcee3a`),
re-measured at `3e225c5`.

- **R207 -- ANSWERED, at all five sites, and the fifth is better than what I asked
  for.** I asked for four `{{fig:}}` references and a boundary sentence either
  re-solved or rewritten so it does not quote a moving absolute. What landed is a
  fifth generated figure that runs the shipped assertion.

  ```
  cmd   sed -n '579,586p' docs/milestones/F2.md
  out   {{fig:detection_edge}}, {{fig:detection_edge_at}},
        {{fig:counter_defect_over_edge}}, {{fig:counter_headroom_room}},
        {{fig:counter_defect_boundary}} -- five references, zero typed values
  cmd   the three things I was asked to check, run rather than read:
  out   (a) IT INVOKES THE SHIPPED TEST. scripts/regen_figures.py:113 calls
            C.test_the_counter_DEFECT_SIZE_cannot_be_raised(_Silent) with
            C.PATCH_TEST_EXACTNESS_COUNTER_DEFECT rebound. The test reads that
            name out of its own module globals (:1379), which is the same route
            the shipped counter meta-test uses at :1420, so the rebinding
            reaches the assertion. The shipped test's own capsys line appears
            in the script's output, which is how I know it ran.
        (b) A WRONG VALUE REDDENS. test_the_generated_figures_are_not_stale
            shells regen_figures.py --check and compares the whole table, so
            any row that stops reproducing fails the suite. Measured on this row
            specifically, two negative controls, one variable moved each:
              headroom x10 in the module the test reads -> row becomes
                "2.174e-06 passes, 2.179e-06 PASSES"     (differs -> red)
              headroom /10                               -> row becomes
                "2.174e-06 FAILS, 2.179e-06 fails"       (differs -> red)
            So the two words are load-bearing, not decoration.
        (c) THE 1e-3 OFFSETS DO NOTHING A READER WOULD NOT EXPECT. I solved the
            flip rather than sampling it: CD = boundary x 1.0 PASSES and
            x 1.0000001 FAILS. The predicate is exact at H x edge, so +/-0.1%
            is a true bracket with 1e4 of slack, not a tuned pair.
  cell  and the caching cannot mask a dependence, because there is none:
        _detection_edge bisects on PATCH_TEST_EXACTNESS and never reads the
        counter-defect size. With CD x 1e3 and _EDGE_CACHE cleared the edge
        is bit-identical, 3.6275172611048466e-14. R124 holds by construction.
  judge closed. The one nuance is R214 below, recorded at 4a and not a block.
  ```
- **R208 -- ANSWERED, both sites, as the condition demanded.**

  ```
  cmd   sed -n '400,422p' floatfea/tolerances.py
  out   :405 now ends "4.47e-15 rounded up. It is a TIGHTENING by 200x." --
        26.8x and 21.5x are gone from the present tense and appear in a
        paragraph headed "THOSE ARE THE DERIVATION'S NUMBERS AND THEY ARE
        HISTORY (R208)", dated.
        :420-422 "The worst clean value over the corpus is clean_worst_ratio
        there, and it is cited rather than typed" -- 0.0887x is gone.
  cmd   the live condition the entry now points at, checked against the figures
  out   clean_worst_ratio 0.1142x < 1; margin_dropped_flip 6.264e+05x,
        margin_wrong_dof_index 1486x, margin_one_element_scaled 8.698e+06x, all
        > 1. dropped_shear_parameter is 0.0006932x and is correctly NOT in
        UNCONDITIONALLY_RED, so "the asserted defects" is the right qualifier.
  judge closed. Both sites, not one.
  ```
- **R209 -- ANSWERED in `tolerances.py`, which is the branch the condition
  offered.** `:507-515` now reads "THE MARGIN IS EATEN FROM ONE SIDE ONLY", names
  the minimum-over-a-growing-set construction, and says a corpus round can only
  tighten. The plan withdrawal stands. The two files no longer disagree -- except
  in the lead sentence, which is R211.
- **R210 -- ACCEPTED at 4a**, as I classed it. Unchanged.
- **R206 -- 4a, unchanged.** `tolerances.py:511` still retypes `2.534e+07` as
  history. R212 below is its sibling and lands the same way.
- **R200, R201, R202, R203, R204 -- OPEN at 4a, correctly.** Untouched, as
  expected.
- **R198, R199 -- 4a, accepted, unchanged.**
- **R181, R189, R190, the R170/R171 remainder, R172, R159, R162, R151, R152 --
  4a, unchanged from my endorsement.**
- **R205 -- CLOSED.** The report revision covering `fc30b71`'s golden-file change
  landed (section 3), which is what I asked for at the end of the last verdict.
- **R134, R135, R137 -- OPEN, UNTOUCHED**, nineteenth round.
- **R129, R131, R132, R136, R138, R139, R148 -- as declared.**
- **R113, R95, R97, R98, R100, R101, R102, R103 -- OPEN.**
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** Recorded as a disagreement.
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, 4a or
  later.
- **R68 standard -- MET, eighth round.**
- **The witness channel -- STILL UNAVAILABLE, and the blocker has changed.**
  `git remote -v` now names `xabi80/FloatFEA` and `master` is pushed; what is
  missing is a base branch to open the PR against. Twenty-four consecutive
  reviews by one reader. Not a pass, and correctly not decided inside a step.

## Findings

**R211. (BLOCKING) The sentence declared "left deliberately" is not only the
withdrawal. It is a withdrawal clause bolted to a causal claim about what
consumes `PATCH_TEST_COUNTER_HEADROOM`'s margin -- and this commit deleted that
claim's supporting measurement and replaced it with one that points the other
way.** `docs/milestones/F2.md:598-603`.

```
code  :598-599 (UNTOUCHED, blame d920a8d) "**The reason for 6.0e7 is the
      improvement side only, and the sentence claiming otherwise is withdrawn.**"
code  :601-603 (WRITTEN THIS COMMIT, blame d89dfee) "So the guard is loosened by
      nothing and tightened both by a harder corpus entry and by any formulation
      change that improves sensitivity anywhere."
code  DELETED THIS COMMIT, from the same paragraph: "adding nine corpus entries
      moved the minimum by 0%" -- the measurement that supported "improvement
      side only" when it was written, and the only one there ever was.
cmd   counter_headroom_room over every commit that has touched the figures file
out   ba4c21a 2.37x (133 entries) ... f1b226b 2.37x (156), fc30b71 2.19x (163),
      6eed45e 2.18x (170)
cell  what moved it, one variable at a time: git diff f1b226b..6eed45e --
      floatfea/ with comment lines removed is EMPTY. Both tightenings happened
      with the formulation byte-identical. Two of two were corpus rounds; zero of
      two were sensitivity improvements.
judge the paragraph now answers "what eats this margin?" twice, incompatibly, in
      four lines. The answer it LEADS with is the one no measurement supports and
      whose measurement this commit removed; the answer three lines below it is
      the one all of the data supports. Under BG0 a Reason is a causal claim that
      carries the cell that isolates it, and the cell here contradicts the lead.
```

**Why this is not a reading quibble, and why it is not R209 re-litigated.** R209
was about `tolerances.py` contradicting the plan, and that is genuinely closed --
the code side now states one direction and states it correctly. R211 is the plan
contradicting *itself*, in a hunk written this round. Whatever "the improvement
side" is taken to name -- a cause or a direction -- the paragraph asserts "only"
in one sentence and "both ... and" three lines later about the same quantity, and
a reader consulting why `6.0e7` is the right number cannot tell which governs.
The practical content is not decorative: a reader is told the room is reserved
for a formulation improvement, when in fact it is being consumed by reviewer
corpus rounds at 0.01x-0.18x each, with 2.18x left.

**And the declaration is the hatch, narrowly.** The site table at report
`:4082-4086` declares `F2.md:586` (old numbering) untouched because "this is the
plan's withdrawal sentence itself, and R209's closing condition is that it
stands". That is true of the *second half* of the line and false of the first.
R209's condition protects the withdrawal -- "a harder corpus entry raises the edge
and loosens the guard" must stay withdrawn, and it does. It does not protect a
separate positive claim that happens to share the line. This is R193's shape at
reduced scale: a site declared untouched under a reason that covers part of what
is on it. I am ruling on it as asked: **the declaration is honest in intent and
incomplete in fact, and it is not a defence of the clause it does not mention.**

**Closed when** `F2.md:598-599` either drops "the improvement side only" or names
the direction rather than the cause, so that it agrees with `:601-603` and with
`tolerances.py:507-515`; **or** the lead is kept and the measurement that
supports it is restored -- which would require a corpus round that moved the room
by 0%, and the two most recent did not. One line. The withdrawal clause stays
either way.

**R212. (recordable, 4a) The paragraph that stops retyping two figures types a
third, and dates the derivation to the wrong day.** `floatfea/tolerances.py:407-411`
against `:438`.

```
code  :408-411 "At the derivation, 2026-09-05, ... the clean side alone moved to
      10.2x."
cmd   git log --date=short -S on the 5e-15 assignment line in tolerances.py
out   fdade28 2026-09-06 -- and the same entry's own footer at :438 says
      "Quantity and value REPLACED 2026-09-06, F2". The entry dates itself twice,
      one day apart.
cmd   the generated table at this commit
out   clean_worst_ratio 0.1142x, i.e. 8.76x -- so 10.2x is already two rounds
      behind, and with my corpus applied it is three: 0.1261x, i.e. 7.93x.
judge tensed as history and bounded ("within two corpus rounds"), so it is true
      as history and I am NOT re-raising R208. It is the fourth typed figure in
      this file and it went one round further from the present the day it was
      written. The date is a plain miss.
```

**Closed when** the date matches the entry's own footer, and `10.2x` either
carries the commit it was measured at or goes, as `0.0887x` did.

**R213. (recordable, 4a) The plan and `tolerances.py` count the same three
numbers as three rounds and as two, in the same commit -- and neither phrasing
survives contact with the trajectory.** `F2.md:603-605` against
`tolerances.py:512-513`.

```
code  F2.md "Measured across three consecutive reviewer rounds the room went
      2.37x, 2.19x, 2.18x -- one direction, three times."
code  tolerances.py "two consecutive reviewer rounds measured it: the room went
      2.37x, 2.19x, 2.18x."
cmd   counter_headroom_room at every figures-file commit, with corpus_entries
out   133:2.37 139:2.37 145:2.37 149:2.37 156:2.37 163:2.19 170:2.18
judge BOTH are defensible readings of the same three published values (three
      rounds each publishing one; two rounds each moving one), which is why this
      is not R211's species. What neither supports is "one direction, three
      times": across SIX corpus rounds the room moved TWICE and held at 2.37x
      four times. The direction claim is right; the count of occurrences is not.
```

**Closed when** the two files state the same count, and the count is of
something the trajectory shows -- two movements in six rounds, or three published
values, but not three movements.

**R214. (recordable, 4a) `counter_defect_boundary` brackets the boundary; it does
not search for it, and the plan's word is "SOLVED".**
`scripts/regen_figures.py:108-123`.

```
code  boundary = PATCH_TEST_COUNTER_HEADROOM * edge; probes at boundary*(1-1e-3)
      and boundary*(1+1e-3)
judge the probe centre is the assertion's own predicate rearranged, so the pair
      CONFIRMS the boundary rather than locating it. That is still a real
      measurement -- I showed both words flip under a 10x change of the effective
      threshold -- but it cannot detect a discrepancy smaller than 0.1%, and it
      cannot detect one that moves edge and the threshold together.
cmd   the flip, solved: CD = boundary x 1.0 PASSES, x 1.0000001 FAILS
judge a bisection to the flip costs the same one cached comparison per step and
      would make the published pair a located boundary rather than a checked
      guess. The gap between what the figure does and what "SOLVED" says is
      small, and it is the kind of gap this milestone has spent six rounds on.
```

**Closed when** either the figure bisects to the flip, or the plan says
"bracketed at plus or minus 0.1%" rather than "SOLVED".

**R215. (recordable, 4a) `_Silent` is a hand-rolled stand-in for a pytest fixture,
in a script the suite depends on, with nothing asserting the two agree.**
`scripts/regen_figures.py:37-44`.

```
code  class _Silent, whose disabled() returns contextlib.nullcontext()
judge if the shipped test's use of capsys ever grows past .disabled(), the
      script raises AttributeError and --check reddens -- which is the safe
      direction, and is why this is not a block. The unsafe direction is quieter:
      the script now prints the shipped test's capsys line into --check's
      stdout twice, so the one place a reader looks for "up to date" is
      interleaved with test output. Cosmetic, and it belongs with 4a's apparatus.
```

**Closed when** the script suppresses the invoked test's output, or 4a records
that it does not.

## Tolerances touched

**None. Every changed line in `floatfea/tolerances.py` is a comment.**

```
cmd  the diff of floatfea/tolerances.py over the range, with comment lines and
     diff headers removed
out  (empty)  -- not one value, not one name, not one form
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COUNTER_HEADROOM` `:521` | `6.0e7` | `6.0e7` (unchanged) | ratio, dimensionless | the raised-defect counter, injected via module globals and registered in both cells | `tolerances.py:497-520` and `F2.md:561-611`. **HOLDS**, and I re-solved rather than read it: the flip is exactly at `6.0e7 x 3.6275e-14 = 2.17651e-06` (PASS at `x1.0`, FAIL at `x1.0000001`), `2.18x` of room. Under my corpus round the edge does **not** move and the room stays `2.18x`. The tolerances-file half is clean; the plan's lead sentence is **R211**. |
| `PATCH_TEST_EXACTNESS` `:439` | `5e-15` | `5e-15` (unchanged) | relative field error, dimensionless | `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`, injected | `tolerances.py:396-438`. **HOLDS** at `8.76x` above the worst clean entry, `7.93x` under my corpus. The two figures that misstated that margin are **closed (R208)**; the third typed one is **R212**. |
| `DELTA_CALIBRATION_ULP` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `DELTA_CALIBRATION_ULP_COUNTER = 5.0`, injected | `calibration_ulp_worst` is `2.000 ULP` at this commit and `2.000 ULP` under my corpus; my four new solved entries all land at 0 ULP (histogram `x129 -> x133`). The `2x` headroom is not threatened. |
| `EXEMPT_RESPONSE_DRIFT_ULP` `:632` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `10.0`, injected | unchanged; the golden file did not move this round and does not move under my corpus. |

**The golden file, checked as its own question (CLAUDE.md, section Testing).**

```
cmd  git diff dfcee3a..HEAD -- tests/regression/g22_exempt_pair_responses.json
out  (empty) -- and git diff dfcee3a..HEAD -- tests/ is empty entirely
judge nothing to explain. The explanation owed for fc30b71's three insertions
     landed in this report's section 3, which closes R205.
```

**What held.** These reproduce at my run: `1518 passed, 0 failed, 0 skipped`;
`regen_figures.py --check` exit 0; `tests/test_plan_figures.py` green; `floatfea/`
byte-identical outside comments; `tests/` byte-identical; my instructions
byte-identical; the report's section 1 and section 3 figure movements to the
published digits; the `139 -> 145` self-correction, which is right and which I
checked (`corpus_solved` is 145). These do **not**: the plan's lead sentence
(R211), the derivation date and the third typed figure (R212), the round count
(R213).

## Next step opens when

**Not now. Step 4 re-opens on R211 alone; step 5 does not begin.**

The BU0 head, named as asked: **R211 falls under the truth-of-a-published-sentence
head**, and secondarily under the tolerance head, because the sentence is inside
the located justification for a shipped tolerance. It is not apparatus: it is not
a parser's reach, not a generator's plumbing, and not a docstring's precision
about its own machinery. It is the paragraph a reader consults to decide whether
`6.0e7` is defensible, and this commit left it stating two incompatible answers
to the question the paragraph exists to answer, having deleted the measurement
behind the one it leads with.

**The condition is one line.** `F2.md:598-599` agrees with `:601-603`, or the
lead's measurement is restored. R212, R213, R214 and R215 are **recorded at 4a**
with the ten already there; none of them needs to move for step 4 to close.

**I want to be explicit that this is a narrower hold than the last three.** The
three named items are genuinely closed and I checked each by running it. R207's
answer is better than the condition asked for: the boundary is now re-solved by
the run that publishes it, and I could not make the figure lie in three attempts.
What I will not do is pass a paragraph whose lead sentence this commit orphaned,
in the round whose whole subject is sentences that outlive their measurements --
and doing so would ratify the reasoning that a finding's protection of one clause
makes the whole line untouchable.

**Adversarial corpus (BE3): 7 new entries committed, all unseen by the
implementer; every field measured at `3e225c5` before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **177** entries, 149 solved,
committed separately at `45550a3` and touching no code. Full suite with the
corpus applied: **1540 passed, 1 failed** -- `test_the_generated_figures_are_not_stale`,
and only that.

The coverage measurement, stated plainly: **0 of my 7 new entries produce a new
exempt-and-detected pair, so BS2's golden file is untouched and caught 0 of 7.
BT0's staleness check reddens on ten rows.** What the entries measure:

* **A new worst clean entry, from a region three rounds of search did not enter.**
  `clean_worst_ratio` `0.1142x -> 0.1261x`; the margin on `PATCH_TEST_EXACTNESS`
  falls `8.76x -> 7.93x`. The incumbent had `I_y/I_z = 9.6e5` and a wall 1.4% of
  `D`; mine has `I_y/I_z = 206` and a wall **19.7%** of `D` -- 4700x less
  anisotropic and 14x thicker. The ceiling **holds**. What is worth recording is
  that this is the third consecutive round in which an outside search lowers it,
  and none of the three found the region the previous one used.
* **The clean ratio is NOT scale-invariant; the detection edge is.** The same
  shape at `x1`, `x1e+4` and `x1e-4` -- identical member lambda to four figures --
  gives `0.1261x / 0.0642x / 0.0442x`, a **2.85x** spread over eight orders,
  while the edge gives `6.2171e-14 / 6.2978e-14 / 6.1796e-14`, a **1.9%** spread.
  Sensitivity is scale-free here and the round-off floor is not. Any future
  unit-invariance claim on this quantity is bounded at **2.9x**, never an
  identity -- and the spread is entirely on the safe side, metre scale worst.
* **`PATCH_TEST_COUNTER_HEADROOM = 6.0e7` holds, third round running against a
  reviewer trying to break it.** Breaking it needs an edge below `1.6667e-14`.
  1180 candidates over four searches -- thick-wall, thin-wall, mixed, and a
  400-candidate refinement around the best -- reached `4.0274e-14`, 2.42x short,
  and **above** the corpus minimum already published. Seven hand-chosen extremes
  (near-solid wall, kilometre scale, micrometre scale, inverted anisotropy at the
  range floor, a member one part in `1e7` above the admission limit) all landed
  between `9.86e-14` and `1.0126e-13` -- within 2.7% of each other. The plateau is
  near `1e-13` and the minimum is only reachable by search.
* **The section constructor refuses a wall that is not thinner than the radius,
  including the exact equality.** `t = D/2` (a solid rod, the limit of the tube
  family) and `t = 0.6 D` both raise at construction. The equality case is the one
  an inclusive comparison lets through, and the one that yields a zero bore with
  no other symptom.
* **The anisotropy range is closed at its top, measured rather than declared.**
  `1e6 + 1e-6` is refused by the parser and `1000000.0` is accepted, so the two
  bracket the edge.

**Twenty-four consecutive rounds have found no element defect**, and the reading
is unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side.
The element did not move under my input this round either -- 1180 candidates, and
the worst thing I could do to it was raise a round-off floor from 11% of its
ceiling to 13%. What moved, for the fifth round running, is prose about the
element's instruments.

**The standing question, answered mechanically at last, and one line short.**
Verdict 23 said the fix for stale figures already exists in the repository and is
called `{{fig:}}`. It is now used in the section that justifies a tolerance, and
the boundary is generated. The residue is what `{{fig:}}` cannot reach: a sentence
with no number in it. `tests/test_plan_figures.py` checks that every reference
resolves and that the table is fresh; nothing checks that the prose around a
reference still says what the reference now means. R211 is that gap with a name.
