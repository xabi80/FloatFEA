# Review — F2 step 4
Reviewed commit: eb5e1a8437c903bd4d3d0374ebb822bb7cba271c
Verdict: HOLD
Tests: 1266 passed, 0 failed, 0 skipped   (my run at `f963b3d`, `python -m pytest -q`,
74.5 s. With my nineteenth-round corpus applied: **1294 passed, 2 failed**.)

**Reviewed code commit: `98b5747`; process `6c6ff3c`; plan `864b716`; report `f963b3d`.**
The header stamp is `eb5e1a8`, my own corpus commit, made immediately before this
verdict and touching no code.

Nineteenth pass. Range `7e6df21..f963b3d`, four commits.

```
cmd  git diff 7e6df21..f963b3d -- .claude docs/SUPERVISOR.md
out  one file, .claude/agents/gating-supervisor.md, +38 -0. Reading-order item 1b
     and the BU0 criterion. NOTHING DELETED, no guard weakened -- I read every
     added line.
cmd  git show --stat 6c6ff3c
out  .claude/agents/gating-supervisor.md | 38 +   (only file; cites BU0 and BU1)
cmd  per commit, files under floatfea/ and under docs/reviews/
out  6c6ff3c 0/0 ; 864b716 0/0 ; 98b5747 1/0 ; f963b3d 0/0   -- correctly routed
cmd  git diff 7e6df21..f963b3d -- tests/ | grep "xfail|pytest.skip|mark.skip"
out  (nothing)
cmd  git log --format=%h -1 -- docs/reviews/F2/step-4.md ; grep -n "^Answers:" report
out  7e6df21 ; one line, ":2860  Answers: verdict 18 @ 7e6df21"
```

**Item 1b, performed: the header names the latest verdict.** One `Answers:` line,
naming `7e6df21`, which is the newest commit touching the verdict file. PASS on
that item.

**Both changes to my instructions are ACCEPTED**, with the reach of each measured
below (R181) and one qualification on the second.

*BU1 (item 1b) is a real closure of my operational note, and I verified the claim
rather than reading it.* I committed a simulated verdict 19 on top of `f963b3d`
in a clone, leaving the report at revision 19, and ran the suite: **1266 passed**.
Before this change that boundary was red by construction. Section 0 is true.

*BU0 (the blocking criterion) I accept as a default, and applying it does not
shorten this round.* Six of the nine findings below fall inside its own three
bullets -- two are counters and their justifications, one is the truth of the
headline published figure, three are the truth of published sentences in
`tolerances.py`, in a shipped test comment and in the report itself. **R170 and
R171 as classified are correct and I take them to 4a**, with one exception: R170
has a live instance at this commit, `Generated at 7e6df21` is false, and that is
R179. The classification is otherwise sound and I say so plainly -- parser reach
is not this gate.

## Carried

Every item from the eighteenth verdict (`HOLD @ b21b520`), re-measured at
`f963b3d`, plus the older carry. The report carries every expected identifier;
`test_report_carried.py` asserts it and I confirmed it fails for the right reason.

- **R163 (blocking) -- CLOSED AT ONE HALF OF TWO.** The calibration counter is a
  genuine injection now and I broke it to prove it: replacing the shipped
  `assert ulp <= DELTA_CALIBRATION_ULP` with `assert True or ...` gives
  `FAILED test_a_LARGER_deviation_fails_the_calibration`. That is the best move in
  the round. The second half -- `test_a_MOVED_response_is_caught`, which my
  condition named -- is unchanged in substance and its docstring now makes exactly
  the claim my condition said it must abandon. See **R173**.
- **R164 (blocking) -- CLOSED ON THE FORM, NOT ON THE REASON.** The band is in ULP
  and is no longer `SUBDIVISION_INVARIANCE`'s number. Its justification cites, as
  "the same argument", the sentence the same commit withdrew forty lines above.
  See **R174**.
- **R165 (blocking) -- CLOSED, both sites.** `test_exempt_pair_responses.py:102-107`
  and `test_corpus_configurations.py:1469-1473` both moved, and the new sentence is
  true: `UNCONDITIONALLY_RED = ("dropped_flip", "wrong_dof_index",
  "one_element_scaled")` at `:1001`, and only `dropped_shear_parameter` reaches the
  early `return` at `:1048-1056`.
- **R166 (blocking) -- CLOSED, and the provenance is structural.** `floor` at
  `:975-977` is literally `PATCH_TEST_EXACTNESS_COUNTER_DEFECT -
  DELTA_CALIBRATION_ULP * math.ulp(...)`, with `DELTA_CALIBRATION_ULP` imported at
  `:80`. Ablated, not inferred: exempt pairs go 49 / 47 / 47 / 44 at
  `DELTA_CALIBRATION_ULP` = 0 / 4 / 1e6 / 1e10, so the constant is live in the
  decision rule.
- **R167 (blocking) -- CLOSED AT FOUR SITES OF EIGHT, FIFTH ROUND RUNNING, and the
  report says "every named site".** The four plan lines are figure references and
  the withdrawal at `:521` is right. `test_corpus_configurations.py:993-1000` and
  `tolerances.py:411`, `:459`, `:492-493` are untouched. See **R176**.
- **R168 (blocking) -- CLOSED AT THE NAMED SITE.** `tolerances.py:517-527` states
  the distribution and withdraws "four times the only value ever observed". Two
  consequences the condition did not reach: the withdrawn sentence survives verbatim
  in the shipped calibration (**R177**), and the histogram is an unseeded one-off
  draw (**R178**).
- **R169 (blocking) -- THE RANGE REPRODUCES AND THE MINIMUM IS NOT AT A BOUNDARY.**
  I re-ran the shipped construction over all 115 solved bases: min `7616.18x` at
  `boundary_kilo_L414p6`, max `23918.6x` at `band_edge_thickwall_free_dir`, spread
  `3.14x` -- the published figures to every digit. Then I asked where each base
  landed. See **R175**. **Both of us were wrong twice**: I withdrew "7630.2x to five
  digits across nine" last round, and I now withdraw my "TIGHTEST 7616.2x" as well.
- **R170 (recordable) -- ACCEPTED AS A 4a ITEM, with one live instance.** The
  `--check` cut is apparatus. `Generated at 7e6df21` is a figure that does not
  describe the repository, which is not: **R179**.
- **R171 (recordable) -- ACCEPTED AS A 4a ITEM.** One further reach measured, in
  **R181**; the docstring at `:34-37` already declares that a file touched at the
  wrong line passes, which is precisely how R167 and R148 were recorded closed.
- **R172 (recordable) -- OPEN, declared.** `:1477-1481` unchanged.
- **R148 (recordable) -- CLOSED AT ONE SITE OF TWO.** `F2.md:699-702` is correct.
  `test_corpus_configurations.py:996` still states `K_bend/K_max ~ 12/lambda_elem^2`
  as the mechanism. Folded into **R176**.
- **R159, R162, R151, R152 (recordable) -- OPEN, declared, unchanged.**
- **R131, R138 -- CLOSED at my sixteenth verdict; the report still says open.**
  Recorded as a disagreement for the third round, not a finding.
- **R132, R136 (blocking) -- OPEN, UNTOUCHED, third round.** `tolerances.py:492-493`
  still `3.9413e-14 at band_edge_isotropic_bracing` / `2.537e+07x` against generated
  `3.9459e-14 at aaa_band_edge_twin` / `2.534e+07x`; `:459` still `8.701e+06x at
  L/r_min = 558` against generated `8.698e+06x at L/r_min 991`; `:411` still
  "90-entry" against generated `139`. Folded into **R176**.
- **R134, R135, R137 (recordable) -- OPEN.** `:1025` "nine orders"; the solved count
  is now 115; `:1055` still asserts `delta < CD` inside a branch requiring
  `delta < CD - 4*ulp(CD)`, so the tautology survives the R166 rewrite.
- **R129 -- folded into R176. R130, R133, R139 -- CLOSED.**
- **R113, R95, R97, R98, R100, R101, R102, R103 -- OPEN, correctly declared.**
  `grep -n "revision 1" floatfea/tolerances.py` still gives `:189` and `:624`, both
  "revision 10".
- **R115 through R128 -- closed at the fourteenth and fifteenth verdicts.**
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.**
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, 4a or later.
- **R68's standard -- MET, third round.** Section 2 records the round's own three
  defects inside its own fix, by name, without being asked.

## Findings

**R173. (blocking) The exempt-drift counter is still not injected, and its docstring
now claims to be the control it is not. Delete the shipped comparison entirely and
all four tests pass.** `tests/regression/test_exempt_pair_responses.py:126-143`.

```
code   b = recorded[key] / PATCH_TEST_EXACTNESS
       a = b + EXEMPT_RESPONSE_DRIFT_ULP_COUNTER * math.ulp(b)
       moved = abs(a - b) / math.ulp(b)
       assert moved > EXEMPT_RESPONSE_DRIFT_ULP
       -- no _measured(), no golden read back through the shipped path. It is
          10.0 > 4.0 with three float operations in between: the same shape as
          the 40 > 4 that R163 named, in the file R163 named.
cell   replace the shipped "assert moved <= EXEMPT_RESPONSE_DRIFT_ULP" with
       "assert True or ...", one variable moved
out    4 passed   -- the regression AND its counter green with the regression's
                     assertion gone
cell   EXEMPT_RESPONSE_DRIFT_ULP 4.0 -> 1.0e9, one variable moved
out    FAILED test_a_MOVED_response_is_caught
claim  "Without this the comparison above inspects two numbers that are equal by
        construction on a clean tree, and would look identical to one that
        compares nothing."                                       -- :129-131
       -- refuted by the first cell: it IS identical to one that compares
          nothing, and this test does not notice.
```

What the counter actually binds, stated exactly: it forbids the ceiling being
raised above 10 ULP. It does not exercise `_measured()`, the golden read, or the
comparison. My condition offered two ways out and the round took neither -- it
wrote a third sentence, and the first cell refutes it.

**Closed when** the counter perturbs a value on the path
`test_every_recorded_pair_is_still_detected` runs, so that neutering that
assertion reddens it -- the shape `test_a_LARGER_deviation_fails_the_calibration`
now has -- or the docstring says it is an ordering check on two constants and is
not a control on the test above it.

**R174. (blocking) `EXEMPT_RESPONSE_DRIFT_ULP`'s reason is the argument the same
commit withdrew forty lines above, and the arithmetic it states evaluates to
zero.** `floatfea/tolerances.py:558-561`.

```
code   :558  "Reason for 4.0: the same choice as `DELTA_CALIBRATION_ULP`, for the
              same argument -- four times a maximum observed at zero"
code   :517  the entry twenty lines above, THIS commit: "the observed maximum is
              2, not 1, and the ceiling carries 2x of headroom rather than the 4x
              the withdrawn sentence claimed"
cmd    the measured drift of this quantity, run-to-run and run-to-golden
out    0.000e+00  (my last round, unchanged; the entry states it too)
       -- four times zero is zero. The stated derivation does not produce 4.0,
          and "the same argument" names an argument withdrawn in the same diff.
```

The FORM is right and I say so: ULP of the recorded ratio, on a quantity that is
bit-reproducible by construction, with the borrowed `1e-11` gone. It is the REASON
that is now a sentence no measurement supports. The honest form is available and
short: the measured drift is exactly zero, and the value is a platform allowance
chosen at N ULP because a last-bit difference must not redden a golden file.

**Closed when** the reason states what sets `4.0` without citing a withdrawn
argument -- either the zero measurement plus the allowance rule, or a pointer to
`DELTA_CALIBRATION_ULP`'s own CURRENT reason, which is a 2-ULP observation and not
"a maximum observed at zero".

**R175. (blocking) `boundary_margin_min = 7616x` is not measured at a boundary. The
bisection uses a fixed bracket and never checks the crossing is inside it; 13 of
the 110 reported bases never leave `lo = 1.0`, and the published MINIMUM is one of
them. Five more bases are dropped by a bare `except`.**
`scripts/regen_figures.py:100-144`; `docs/milestones/F2_figures.md:31-35`;
`docs/milestones/F2.md:658-668`.

```
claim  "This bisects each base's member length until the SHEAR defect's effective
        size crosses CD, and reports the range."         -- regen_figures.py:104
code   lo, hi = 1.0, 1.0e7 ; mid = (lo*hi)**0.5 ; ... ; base["stations"] = repr(lo)
       -- if eff(1.0) is already < CD, hi collapses to 1.0 on the first pass, lo
          never moves, and the margin is evaluated at L = 1 m.
cell   the shipped construction re-run over all 115 solved bases, recording
       eff/CD at the point each one reports
out    included 110, silently dropped 5 (exception inside the loop)
       converged (eff within 1% of CD)      97
       NEVER BRACKETED                      13, every one with lo = 1.0
       boundary_kilo_L414p6   eff/CD = 0.0296   <- boundary_margin_min_at
       -- the figure named for the crossing is evaluated 34x below it
cell   min and max over the 97 bases that DO converge, one variable moved
out    min 7630.16x at boundary_thin_exempt_L38 (axis)
       max 23918.6x at band_edge_thickwall_free_dir
       spread 3.135x
cell   by orientation, converged only
out    axis        n=38  all 7630.16x exactly
       in_plane_y  n= 4  all 7630.16x exactly
       skew        n=47  8422.3x to 9787.5x
       free_dir    n= 8  7658.97x to 23918.6x
```

So the published minimum is wrong by `1.0018x` -- small -- and wrong in kind: it is
the one number in the range that is not a boundary margin, it is the headline of
the finding it answers, and `boundary_margin_max` and `boundary_margin_spread` are
fine only because the loosest base happened to converge. The plan's orientation
sentence survives the correction: axis-aligned bases are the bottom of the
converged range too, so that claim is not at issue.

`except Exception: continue` at `:139-140` is the second half. A base whose
bisection probe leaves the admissible band is dropped from a min-and-max with no
count and no message -- the recorded rule is that an unsupported case raises, it
never defaults. I added two such bases to the corpus and confirmed the figure did
not move and nothing said why (see the corpus paragraph).

**Closed when** the bisection asserts its bracket contains the crossing, a base
whose crossing lies outside `[1, 1e7]` is either bracketed wider or reported, the
dropped bases are counted in the generated file rather than swallowed, and
`boundary_margin_min` is the minimum over bases that reached the boundary.

**R176. (blocking) R167 and R148 are recorded closed. Between them the conditions
named eight sites; four moved. The four that did not are a shipped test comment
carrying figures that are `191x` off and three `tolerances.py` entries whose
correct values are generated four lines away -- and the report's sentence is
"every named site is a figure reference".**
`tests/verification/rung1/test_corpus_configurations.py:993-1000`;
`floatfea/tolerances.py:411`, `:459`, `:492-493`; report section 3.

```
claim  "R167: every named site is a figure reference."           -- report sec. 3
claim  "R148 | closed -- no longer stated as a law"        -- report sec. 5 table
cmd    grep -rn "2.838e+05|12/lambda_elem|19 (entry" tests/ floatfea/ docs/
out    test_corpus_configurations.py:994  "On 19 (entry, defect) pairs"
       test_corpus_configurations.py:996  "K_bend/K_max ~ 12/lambda_elem^2"
       test_corpus_configurations.py:997  "still RED, from 2.838e+05x at the
                                           weakest to 1.114e+08x"
       -- the exact three figures the plan withdrew this round, in the file the
          plan withdrew them for, at the lines my condition named
cell   UNCONDITIONALLY_RED pairs below CD, at this commit
out    22 pairs, weakest 1486x    -- 19 and 2.838e+05x, 191x off, third round
cmd    grep -n "90-entry|8.701e+06|3.9413e-14|2.537e+07" floatfea/tolerances.py
out    :411 "90-entry"   (generated corpus_entries 139)
       :459 "8.701e+06x at L/r_min = 558"   (generated 8.698e+06x, L/r_min 991)
       :492 "3.9413e-14 at band_edge_isotropic_bracing"  (generated 3.9459e-14 at
            aaa_band_edge_twin);  :493 "2.537e+07x"  (generated 2.534e+07x)
```

The guard cannot catch this and says so: `test_report_carried.py:34-37` declares
that "whether a touched file was touched at the right line" is not checked and is
the reviewer's. Both files were touched elsewhere in the diff, so both findings are
green in the guard and false in the record. **Fifth consecutive round** -- R129 at
3 of 5, R141 at 2 of 3, R143 at 1 of 2, R158 at 1 of 3 and R160 at 2 of 3, now R167
at 4 of 8 and R148 at 1 of 2.

**Closed when** each of the four sites is regenerated, given a pointer, or stated
as left with its reason, one line per site; and the report's summary sentence
matches the site list rather than the plan half of it.

**R177. (blocking) The sentence withdrawn from `tolerances.py` this round survives
verbatim inside the assertion it justifies.**
`tests/verification/rung1/test_corpus_configurations.py:1085-1090`.

```
code   :1089  "The measured deviation is exactly 1.000 ULP, the single rounding of
               max|CD k| / max|k|, and the ceiling is four times it."
code   tolerances.py:517-524, this commit: the maximum is 2, the headroom is 2x,
       and "four times the only value ever observed" is withdrawn
cmd    grep -rn "1.000 ULP|four times" tests/ floatfea/
out    the tolerance entry (corrected) and this comment (not), plus my corpus
       header quoting it as the finding
```

This is R167's species -- a figure duplicated into a code comment where nothing
regenerates it -- landing on the very number the round corrected, four lines above
the assertion. A reader who opens the test to check the calibration reads the
withdrawn claim.

**Closed when** `:1085-1090` states the measured maximum or points at the tolerance
entry, and carries no second copy of the distribution.

**R178. (blocking) The histogram published in `tolerances.py` is one unseeded random
draw that nothing can reproduce. Re-drawn to the same protocol and the same size,
the cells differ.** `floatfea/tolerances.py:518-522`.

```
code   :520-522  "over 5222 admissible configurations the histogram is
                  0 ULP x 5106     1 ULP x 113     2.000 ULP x 3"
cell   5222 admissible configurations drawn to the protocol the entry describes
       (D 1e-4..8 m, t/D 0.004..0.499, L/D 2..3e6, four orientations, roll and
       anisotropy), seeded 20260908, at this commit
out    0 ULP x5082    1 ULP x140    max 1.000 ULP
       -- 140 against 113, and no 2-ULP configuration in this draw at all
```

The provenance is correct -- the figures are mine, from my corpus header at
`ca42b3f` -- and the CEILING is not in question: the observed maximum of 2.000 is
reproducible deterministically, because I put those three configurations in the
corpus and `calibration_ulp_worst` regenerates as `2.000 ULP`. What is not
reproducible is the table. BI3, locked at `8d6ba7d` one commit before this range,
says a table in this file is produced by a script at the commit it describes or it
is not in this file. Nothing produces this one; it names no commit, no seed and no
script, and my condition asked for exactly those.

**Closed when** the entry carries the single number it needs -- the observed
maximum -- and points at `calibration_ulp_worst`, with the distribution in the step
report where regeneration is a rule; or a committed script produces the histogram.

**R179. (recordable) `Generated at 7e6df21` is false: at that commit the shipped
generator does not produce this table.** `docs/milestones/F2_figures.md:40`.

```
cell   check out 7e6df21, restore HEAD's F2_figures.md, run --check
out    "regen_figures: F2_figures.md is stale"
       -- the table describes 98b5747's classify floor, not 7e6df21's
```

It is the live instance of R170: the stamp sits below the `--check` cut, so nothing
compares it, and a stamp nothing compares is the one line in a generated file that
can lie. **Closed when** the stamp is regenerated with the table or dropped.

**R180. (recordable) The calibration counter's decision boundary was sampled on one
side. `+3` ULP already fails; the record says `+5` is "the first value that must be
caught".** `floatfea/tolerances.py:534-540`;
`tests/verification/rung1/test_corpus_configurations.py:1210-1212`.

```
claim  "measured, 2 ULP passes and 5 ULP fails, so the counter sits at the first
        value that must be caught"
cell   inject k ULP into injected_delta and run the shipped calibration, k = 0..5
out    +0 PASS  +1 PASS  +2 PASS  +3 FAIL  +4 FAIL  +5 FAIL
```

The number 5 is defensible by its other rule -- the smallest integer above a
ceiling of 4 -- and the counter is correctly directed: lowering a counter tightens
the claim, and 40 -> 5 is a tightening I welcome. It is the "so" that is unmeasured:
the boundary is between 2 and 3, and it was not solved for.
**Closed when** the sentence states the measured boundary, or drops the causal
clause and keeps the definitional one.

**R181. (recordable) The header mechanism's reach, measured. Naming the PREVIOUS
verdict instead of the latest costs one assertion.**
`tests/test_report_carried.py:84-134`.

```
control drop a carried finding from the report          -> red  (the guard works)
cell    header -> "Answers: verdict 17 @ 4183adb", one variable moved
out     1 failed, 76 passed  -- ten of verdict 18's identifiers stop being demanded
cell    header -> "verdict 11 @ fc3c9a8"
out     11 failed, 42 passed  -- an old verdict DOES redden, so the evasion is
                                 cheap only for the ADJACENT one
cell    header -> 98b5747 (a commit with no verdict file), and an empty-tree sha
out     89 passed -- git show fails and _verdict_text_at falls back to the newest
        verdict, which is the strict direction. Not exploitable.
cell    two "Answers:" headers, stale first
out     11 failed -- re.search takes the first; a stale first header reddens
```

So the one hole is the adjacent-verdict swap, at a cost of one assertion, and it is
exactly the hole item 1b exists to fill. I performed 1b this round and it passed.
Recording the number so the next reader knows what the machine is worth: **one
failing assertion, not zero.**
**Closed when** it is a 4a item alongside R171, or the docstring records the
one-assertion cost.

## Tolerances touched

**Two entries renamed and re-derived, one counter lowered, no accuracy value
loosened, no production code moved.**

```
cmd  git diff --stat 7e6df21..f963b3d -- floatfea
out  floatfea/tolerances.py | 74 ++++---   (the only floatfea file in the range)
cmd  the diff read line by line for a value that moved in the permissive direction
out  none. DELTA_CALIBRATION_ULP_COUNTER 40 -> 5 TIGHTENS (a smaller injected
     defect must now be caught). EXEMPT_RESPONSE_DRIFT 1e-11 relative -> 4 ULP of
     the recorded ratio is a TIGHTENING by 1.2e+04x on that quantity.
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `DELTA_CALIBRATION_ULP` `:527` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `5.0`, injected | `tolerances.py:517-526`, `F2.md:924`. Record corrected; the histogram is unreproducible -- **R178** -- and its duplicate at `test:1089` was not corrected -- **R177**. |
| `DELTA_CALIBRATION_ULP_COUNTER` `:540` | `40.0` | `5.0` | ULP multiple | -- | `tolerances.py:529-539`. **Now a true injection, verified by neutering the shipped assertion.** Boundary sampled on one side -- **R180**. |
| `EXEMPT_RESPONSE_DRIFT` to `EXEMPT_RESPONSE_DRIFT_ULP` `:561` | `1e-11` relative | `4.0` ULP | ULP multiple, dimensionless | `10.0` ULP | `tolerances.py:544-560`, `F2.md:927`. Form correct and the borrow is gone; the reason cites a withdrawn argument -- **R174**; the counter is not injected -- **R173**. |
| `EXEMPT_RESPONSE_DRIFT_COUNTER` to `_ULP_COUNTER` `:567` | `1e-6` relative | `10.0` ULP | ULP multiple | -- | `tolerances.py:563-566`. Binds the ceiling from above at 10 ULP and nothing else. |

Both renames are reflected in the plan's table (`F2.md:925-928`) and
`test_plan_matches_tolerances.py` binds them in both directions -- I confirmed by
appending `NEWLY_ADDED_FUDGE: Final[float] = 0.25`, which gives
`FAILED test_every_declared_tolerance_appears_in_the_plan[NEWLY_ADDED_FUDGE]`.

`tests/regression/g22_exempt_pair_responses.json` grew 39 -> 41 rows, both new rows
being my eighteenth-round corpus entries, with a corpus round given as the reason.
I recomputed all 41 and every one reproduces to `0.0` relative.

**What held.** These reproduce at my run: `1266 passed`; every row of
`docs/milestones/F2_figures.md` against a fresh `--check` at `f963b3d`;
`boundary_margin_min/max/spread` to every digit (their PLACEMENT is R175, not their
arithmetic); the classify ablation 49/47/44; the calibration's injection under five
separate ways of breaking it; `UNCONDITIONALLY_RED`'s membership; the green-boundary
claim of section 0, simulated with a committed verdict; `0.0887x`; `1486x`;
`6.264e+05x`; `2.37x`. These do **not**: `boundary_margin_min` as a boundary
(R175); the histogram cells (R178); `Generated at 7e6df21` (R179); "every named
site is a figure reference" (R176); "the first value that must be caught" (R180);
"would look identical to one that compares nothing" (R173); "four times a maximum
observed at zero" (R174).

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a HOLD, not a STOP: rung 1
is green at `f963b3d`, no production code moved, no existing golden value moved,
every tolerance change is a tightening, the `process:` and plan commits are
correctly standalone and additive, and the round's headline move -- the calibration
counter becoming a real injection -- survives five ways of breaking it.

1. **R173, R174 -- the two tolerance defects, first.** A counter that is `10 > 4` in
   the file R163 named, under a docstring claiming to be the control it is not; and
   a reason that cites the argument withdrawn forty lines above it.
2. **R175 -- the published boundary minimum is not at a boundary.** 13 of 110 bases
   never bracket, 5 more are swallowed by a bare `except`, and the converged range
   is `7630.16x` to `23918.6x`.
3. **R176 -- R167 and R148 closed at four sites of eight, fifth round running**,
   with the report's own summary sentence the thing that is false. Site by site:
   one code comment block and three `tolerances.py` entries.
4. **R177, R178 -- the record of `DELTA_CALIBRATION_ULP`.** The withdrawn sentence
   survives in the test; the replacement table cannot be reproduced.
5. **R179, R180, R181 -- recordable**, each answerable in one line or one cell.
6. **R132, R134, R135, R136, R137 -- untouched from the fifteenth verdict**, R132
   and R136 folded into R176's site list.
7. **R151, R152, R159, R162, R172 -- declared open**, answerable in one line each.
8. **R113, R95, R97, R98, R100-R103, R63, R76, R79, R80 -- carried, unchanged.**
9. **R170, R171 -- taken to 4a** under BU0, which I accept. R6, R16, R25, R30, R31,
   R32, R33, R36, R50, R52, R62 -- 4a or later.

**Adversarial corpus (BE3): 6 new entries committed, all unseen by the implementer;
every outcome measured at `f963b3d` before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **145** entries, 121 solved,
committed separately at `eb5e1a8` immediately before this verdict and touching no
code. Full suite with the corpus applied: **1294 passed, 2 failed.**

The coverage measurement, stated plainly: **3 of my 6 new entries produce a new
exempt-and-detected pair, and BS2's golden file caught all six pairs by name, on its
third round against unseen input** -- `bu_exempt_detected_margin_1p03` (all three
kinds), `bu_exempt_floor_edge_0p976` and `bu_midprobe_drop_D2000_L1e7`. BT0's
figures file caught its own staleness again, on `corpus_entries`, `corpus_solved`,
`exempt_total`, `exempt_by_defect`, `exempt_detected` and
`below_ceiling_dropped_shear_parameter`. Both mechanisms work and I say so.

**Against that: the other 3 entries are invisible to every shipped assertion, and
that is the measurement of R175.** `bu_bracket_top_D1e5_axis_L1e7` and
`bu_bracket_top_D1e6_skew_L1e7` have their crossing above the bisection's bracket
top -- `eff/CD` is `597.9` and `9.620e+05` at `L = 1e7`;
`bu_midprobe_drop_D5000_aniso_L1e7` is dropped at the first probe. None of the three
moved `boundary_margin_min`, `_max` or `_spread` by a digit, because the generator
discards exactly the bases that would expose it -- a figure a corpus cannot reach is
a figure a corpus cannot check.

**Nineteen consecutive rounds have found no element defect**, and the reading is
unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side. Every
defective instrument this milestone has been a test, a tolerance record, a generator
or a document; the element has been fine every time.

**Witness channel unavailable.** `git remote -v` is empty, so no PR and no
`[witness ...]` comment; per `docs/SUPERVISOR.md` that is an unavailable check, not
a pass. Nineteen consecutive reviews by one reader.

**The standing question for the next round.** Last round I asked, for every number
this repository publishes, what would have to change in the world for it to change
here. This round answers it once and the answer is "nothing": `boundary_margin_min`
is regenerated faithfully, from a bisection that for that base never ran, over a
base list that silently omits the cases that would move it. So the question
sharpens. **For every generated figure, what is the input that would move it, and is
that input in the corpus -- or is the generator structurally unable to see it?** A
figure that regenerates is not thereby a figure that is measured; `--check` proves
only that the same code met the same data twice.
