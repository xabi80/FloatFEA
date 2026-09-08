# Review — F2 step 4
Reviewed commit: ca42b3fd9919db6892b2372ad6810fa50971ee04
Verdict: HOLD
Tests: 1211 passed, 0 failed, 0 skipped   (my run at `b21b520`, `python -m pytest -q`,
68.67s. With my eighteenth-round corpus applied: **1239 passed, 2 failed**.)

**Reviewed code commit: `ad2164d`; process `69c5858`; plan `ba4c21a`; report `b21b520`.**
The header stamp is `ca42b3f`, my own corpus commit, made immediately before this
verdict and touching no code.

Eighteenth pass. Range `4183adb..b21b520`, four commits.

```
cmd  git diff 4183adb..b21b520 -- .claude docs/SUPERVISOR.md
out  one hunk in .claude/hooks/require-verdict.sh: the dirty-tree branch MOVED
     below the BS0 call, +12 comment lines. Nothing deleted, no guard weakened.
cmd  git show --stat 69c5858
out  process: R153 ... .claude/hooks/require-verdict.sh | 23 +++--   (only file)
cmd  git log --oneline 4183adb..b21b520 -- CLAUDE.md
out  (nothing)
cmd  every commit in the range checked for touching floatfea/ AND docs/reviews/
out  (none)
cmd  grep -rn "xfail|pytest.skip|mark.skip" tests/ --include=*.py
out  (nothing)
```

**The instruction change is correctly routed for the second round running.**
Standalone `process:` commit, cites R153, touches only the hook, and I read every
added line: the move is exactly the reordering R153 asked for and nothing else.
`ba4c21a` is plan-only and `ad2164d` is code-only.

**R153 was answered better than I asked.** I asked for the hook to reach its
branch; the round moved the mechanism out of the hook into `tests/test_report_carried.py`
and left the hook call as a local signal. I broke that test five ways and it held
on the one that matters -- dropping a finding from the report reddens it -- so the
guard is real. Its reach is smaller than its docstring says, measured in **R171**.

**Three of this round's five substantive moves survive being broken deliberately.**
The calibration's shipped assertion is live on a ULP sweep; `test_plan_figures.py`
reddens on any edit above its cut line and reddened on my corpus round unprompted;
R161's completion reddens the exact cell that passed last round. Details under
**What held**.

This is a HOLD for seven things. Two are the same defect the round was written to
fix, reappearing inside the commit that fixed it; three are closing conditions that
named sites and were closed at some of them -- the **fourth, fifth and sixth**
consecutive occurrence; one is a tolerance justification refuted by measurement at
this commit; and one is a published margin that is not the tightest, where the cell
that settles it takes two minutes and I ran it.

## Carried

Every item from the seventeenth verdict (`HOLD @ f66e4e0`), re-measured at
`b21b520`, plus the older carry. **The report carries all 61 expected identifiers**
-- `test_report_carried.py` asserts it and I confirmed it passes for the right
reason by dropping `R156` from the table and watching it redden.

- **R153 (blocking) -- CLOSED, and the answer is larger than the finding.** The
  reorder is at `.claude/hooks/require-verdict.sh:115-120`; the mechanism is
  `tests/test_report_carried.py`. `scripts/check_carried.py` is declared **no
  change** by name, correctly. Reach measured in **R171**.
- **R154 (blocking) -- CLOSED, with an ambiguity recorded.** The row now carries a
  mark. It is a kind-level count, not the named pair's classification -- see
  **R172**. Today all three marked minima do classify `below resolution`, so
  nothing on the printed row is false.
- **R155 (blocking) -- CLOSED AT PART, FOR THE SECOND ROUND.** The generator is
  the right answer and the detection table is regenerated. `F2.md:507`
  ("90-entry"), `:521` ("Zero entries fail to redden") and `:669`/`:673` are
  untouched and refuted, and 13 of the 25 generated figures are referenced
  nowhere -- four of them being exactly the values R132/R136 say are stale. See
  **R167**.
- **R156 (blocking) -- CLOSED ON THE BAND, AND ITS SPECIES RECURS TWICE.** The
  calibration is now in ULP and the shipped assertion is live: my sweep is green
  at `+2` added ULP and red at `+5`. But `classify`'s floor is still the 47-ULP
  relative band (**R166**), and `EXEMPT_RESPONSE_DRIFT`, created this round, is a
  48000-ULP band on a quantity measured at 0.0 (**R164**).
- **R157 (blocking) -- NOT CLOSED. A disagreement was recorded where a cell was
  available.** The two constructions never disagreed; the held variable is
  orientation. 104 bisections, 92 s. See **R169**.
- **R158 (recordable) -- CLOSED AT ONE SITE OF THREE.** The module docstring is
  corrected; the failure message and the runner's printed line are byte-identical
  and the claim is now false for 22 of 39 rows rather than 20 of 34. See **R165**.
- **R159 (recordable) -- OPEN, declared.** The cancellation sentence in
  `_homogeneous` at `test_corpus_configurations.py:885-888` is unchanged.
- **R160 (recordable) -- CLOSED AT TWO SITES OF THREE.** My condition named
  `:1084`, `:965` and `test_exempt_pair_responses.py:90-92`. The first and third
  moved; `classify`'s floor did not. See **R166**. And the third's replacement is
  the borrowed number renamed -- **R164**.
- **R161 (recordable) -- CLOSED, and I re-ran the exact cell.** Appending
  `NEWLY_ADDED_FUDGE: Final[float] = 0.25` to `floatfea/tolerances.py` gave
  `1028 passed` last round; at this commit it gives
  `FAILED test_every_declared_tolerance_appears_in_the_plan[NEWLY_ADDED_FUDGE]`.
- **R162 (recordable) -- OPEN, declared.** Sec. 5's `9.8e-11` still carries no
  construction. `docs/SUPERVISOR.md` and `tests/corpus/g22_model_configurations.txt`
  are declared **no change** and both are correct -- but neither is a site I named;
  the parser charged them to R162. See **R171(b)**.
- **R148 (recordable) -- OPEN, declared.** `12/lambda_elem^2` at
  `test_corpus_configurations.py:988` and `F2.md:670`.
- **R151, R152 (recordable) -- OPEN, declared.** Unchanged.
- **R129 -- folded into R167.** **R130 -- CLOSED** (fifteenth verdict).
- **R131 -- CLOSED at my sixteenth verdict; the report's table says "open".**
  Recorded as a disagreement, not a finding: the report may decline my closure,
  but the two artifacts now differ on the status of R131 and of R138.
- **R132 (blocking) -- OPEN, UNTOUCHED, and the remedy was built and not applied.**
  `tolerances.py:492-493` still says `3.9413e-14 at band_edge_isotropic_bracing`
  and `2.537e+07x`; `docs/milestones/F2_figures.md` now GENERATES
  `detection_edge = 3.9459e-14`, `detection_edge_at = aaa_band_edge_twin`,
  `counter_defect_over_edge = 2.534e+07x` and `counter_headroom_room = 2.37x`, and
  no reference points at them. Folded into **R167**.
- **R133 (blocking) -- CLOSED.** The comment at `:1074-1076` was replaced wholesale
  by the R156 rewrite, so the two incompatible counts are gone; the surviving
  statement at `:969-971` says "on one of them", which my ablation confirms
  (a bare `>=` frees 2 pairs at 133 entries, both `one_element_scaled`; it was 1 at
  99 entries). The sentence at `:519-526` no longer exists.
- **R134 (recordable) -- OPEN.** "nine orders" at `:1025` for `9.881e+06`.
- **R135 (recordable) -- OPEN AND WIDER.** `74 -> 81 -> 89 -> 99 -> 109` solved.
- **R136 (recordable) -- OPEN, UNTOUCHED.** `tolerances.py:459` `8.701e+06x at
  L/r_min = 558`; the generator gives `8.698e+06x at L/r_min 991`. Also
  `tolerances.py:411` "90-entry corpus" against a generated `corpus_entries = 133`.
  Folded into **R167**.
- **R137 (recordable) -- OPEN, UNTOUCHED, STILL A TAUTOLOGY.** `:1046` asserts
  `delta < CD` inside a branch whose condition is `delta < CD*(1 - 1e-14)`.
- **R138 -- CLOSED** (sixteenth verdict; the report says open -- see R131).
- **R139 (blocking) -- CLOSED.**
- **R113, R95, R97, R98 -- OPEN, correctly declared.**
- **R100 -- PARTLY ANSWERED AND NOW BETTER.** `scripts/` is `check_carried.py
  regen_figures.py write_verdict.py`. A regeneration script now exists and is
  asserted; the word "regenerated" in the plan's tolerance table is still unearned
  for `tolerances.py` itself.
- **R101, R102, R103 -- OPEN.** `grep -n "revision 1" floatfea/tolerances.py`
  gives `:189` and `:624`, both "revision 10".
- **R115 through R128 -- closed at the fourteenth and fifteenth verdicts.** Kept as
  a range deliberately; nothing open is inside it, which I checked, because the
  parser in `test_report_carried.py` sees only the endpoints (**R171(d)**).
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.**
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, routed to
  step 4a or later.
- **R68's standard -- MET again.** Sec. 1 records the round's own two bugs in the
  new guard, found by running it, without being asked. Second round running.

## Findings

**R163. (blocking) `DELTA_CALIBRATION_ULP`'s counter is asserted of itself. Delete
the shipped calibration assertion entirely and the counter still passes.**
`tests/verification/rung1/test_corpus_configurations.py:1192-1207`.

```
code   cd = CD ; nudged = cd + 40 * math.ulp(cd)
       ulp = abs(nudged - cd) / math.ulp(cd)
       assert ulp > DELTA_CALIBRATION_ULP
       -- no entry, no model, no call to injected_delta. It is 40.0 > 4.0 with
          three float operations in between.
cell   replace the shipped "assert ulp <= DELTA_CALIBRATION_ULP" with
       "assert True or ...", one variable moved
out    2 passed, 624 deselected
       -- the calibration test AND its counter both green with the calibration
          assertion gone.
```

The recorded rule is "a gate carries its own failure: break the claimed property
and confirm the assertion goes red". The claimed property is that
`injected_delta`'s measurement of the counter-defect sits within four ULP of the
declared size, and no shipped test breaks it. **I did, and the shipped assertion is
sound** -- adding k ULP inside `injected_delta` gives green at k = 2 and red at
k = 5, so the decision boundary is between 3 and 4 added ULP as declared. That
measurement is mine, taken in this review; nothing in the repository takes it.

Same species, milder, at `tests/regression/test_exempt_pair_responses.py:120-137`:
`test_a_MOVED_response_is_caught` does call `assert_close`, but it re-implements
the call rather than exercising the shipped one.

```
cell   in test_every_recorded_pair_is_still_detected, EXEMPT_RESPONSE_DRIFT -> 1.0
out    4 passed   -- a 100% drift allowance on the golden file, and its own
                     counter is green.
```

**Closed when** each counter reddens on a defect injected into the path the shipped
assertion runs -- so that removing or widening the shipped assertion reddens the
counter -- or each docstring says plainly that it checks the ordering of two
constants and is not a control on the test above it.

**R164. (blocking) `EXEMPT_RESPONSE_DRIFT` is `SUBDIVISION_INVARIANCE` renamed. Same
value, a measured drift of exactly zero, and a band of 4.8e+04 ULP -- R156's finding,
in the tolerance the same commit created to answer R160.**
`floatfea/tolerances.py:530-547`.

```
claim  "ITS OWN ENTRY BECAUSE IT IS ITS OWN QUANTITY (R160)."      -- :536
claim  "the admissible move is round-off in the ratio and nothing else.
        Measured across a full re-run, every recorded pair reproduces to 0.0."
cmd    SUBDIVISION_INVARIANCE == EXEMPT_RESPONSE_DRIFT
out    True   (1.000e-11 both)
cell   _measured() twice, and against the golden, 39 rows
out    max relative drift run-vs-run    0.000e+00
       max relative drift run-vs-golden 0.000e+00
cmd    the band expressed in ULP of the smallest recorded ratio-to-ceiling, 1.069
out    1e-11 * 1.069 / ulp(1.069) = 4.81e+04 ULP
```

The entry's own reason -- round-off in the ratio and nothing else -- justifies a
value near one ULP. The value chosen is the number it was borrowing, to the digit.
A borrowed band that keeps its value and changes its name answers the CITATION half
of R160 and not the MEASUREMENT half, and this repository's own doctrine, written
nineteen lines earlier in the same file at `:511-521`, is that a relative
engineering band on an exactness quantity is the defect.

Note the direction: the shipped test compares now/ceiling against was/ceiling, both
recomputed from the same corpus by the same code, so the quantity is bit-reproducible
by construction. Its class is exactness, not accuracy.

**Closed when** the band is what the measurement supports -- an equality, or a small
ULP multiple with the zero-drift measurement recorded beside it -- or the entry
states that 1e-11 is inherited from `SUBDIVISION_INVARIANCE` and says what
measurement would move it.

**R165. (blocking) R158 is recorded closed. One of its three sentences was corrected;
the two that a reader meets at a failure are byte-identical, and the claim is now
false for 22 of 39 rows rather than 20 of 34.**
`tests/regression/test_exempt_pair_responses.py:102-104`;
`tests/verification/rung1/test_corpus_configurations.py:1447-1450`.

```
claim  "R158: the golden file's premise is corrected"          -- report sec. 4
cmd    git diff 4183adb..b21b520 -- tests/  piped through grep "carry no red"
out    (nothing: the docstring hunk rewrote lines 3-7 only)
code   :103  "This pair carries no red assertion because its defect is below the
              declared resolution, so nothing else would have noticed"
code   :1447 "N of M pairs are below the declared resolution and carry no red
              assertion: dropped_flip 9, dropped_shear_parameter 23,
              wrong_dof_index 13"
cell   golden composition by defect kind at this commit
out    39 rows: dropped_shear_parameter 17, wrong_dof_index 13, dropped_flip 9
       -> 22 of 39 ARE asserted red by UNCONDITIONALLY_RED
```

The printed line names its own refutation inside the same f-string: it enumerates
`dropped_flip` and `wrong_dof_index`, both in `UNCONDITIONALLY_RED`, in the sentence
that says they carry no red assertion. My condition read "Closed when THE THREE
SENTENCES scope themselves to the classifiable defect". This is the **fourth**
consecutive round in which a condition that named sites was closed at some of them
and recorded as answered -- R129 at 3 of 5, R141 at 2 of 3, R143 at 1 of 2, and now
R158 at 1 of 3, R160 at 2 of 3 (**R166**) and R155 at part again (**R167**). Six such
in one round is the most this milestone has had.

The guard added this round cannot catch it: `test_exempt_pair_responses.py` is in the
diff, so `test_every_named_site_is_touched_or_declared` is green for R158. Its
docstring says so, correctly.

**Closed when** both remaining sentences scope to `dropped_shear_parameter`, or say
that the other three kinds are covered twice, site by site.

**R166. (blocking) R160 is recorded closed at two sites of three: `classify`'s floor
still borrows `ROUNDOFF_IDENTITY`, and the comment above it -- "THE SAME ULP
ALLOWANCE THE CALIBRATION DOES" -- was made false by this very commit.**
`tests/verification/rung1/test_corpus_configurations.py:971-976`.

```
claim  :971  "THE COMPARISON CARRIES THE SAME ULP ALLOWANCE THE CALIBRATION
              DOES (R142)."
code   :975  floor = PATCH_TEST_EXACTNESS_COUNTER_DEFECT * (1.0 - ROUNDOFF_IDENTITY)
cmd    (CD - CD*(1-1e-14)) / math.ulp(CD)   against   DELTA_CALIBRATION_ULP
out    47.0 ULP   against   4.0 ULP        ratio 11.75x
```

The sentence was true at `f66e4e0` and false at `ad2164d`, and the commit that made
it false is the commit that moved the calibration. This is the exact pattern the
round diagnosed in the plan -- a figure correct when written and wrong when read --
appearing in the code it wrote to fix it.

**And I measured the harm and it is zero**, so this is about the record and about
the site R160 named, not a hole:

```
cell   exempt-pair count under four floors, one variable moved
out    bare >= CD      47 pairs   shear 23, flip 9, dof 13, one_element_scaled 2
       CD - 1 ULP      45 pairs   shear 23, flip 9, dof 13
       CD - 4 ULP      45 pairs   shear 23, flip 9, dof 13
       CD - 47 ULP     45 pairs   shear 23, flip 9, dof 13   <- shipped
cell   2256 random admissible configurations, any defect landing strictly between
       CD - 47 ULP and CD - 4 ULP
out    0
```

It matters because `classify` is the DECISION rule and the calibration is only the
MEASUREMENT rule: the 47-ULP band survives in the one that exempts a pair from being
asserted red, eight lines from where a 4-ULP band replaced it.

**Closed when** `classify`'s floor is expressed in the same ULP quantity as the
calibration, or the comment says the two allowances differ by 11.75x and why.

**R167. (blocking) The generator is the right answer and it was not applied to the
sites the open findings name. Four claims in the locked plan are refuted at this
commit, thirteen of the twenty-five generated figures are referenced nowhere, and
four of those thirteen are exactly the values R132 and R136 say are stale in
`tolerances.py`.** `docs/milestones/F2.md:507`, `:521`, `:669`, `:673`;
`tests/verification/rung1/test_corpus_configurations.py:985-990`;
`floatfea/tolerances.py:411`, `:459`, `:492-493`.

```
plan :507   "Worst over the 90-entry corpus {{fig:clean_worst_ratio}}"
gen         corpus_entries 133, corpus_solved 109 -- generated, referenced nowhere
plan :521   "Zero entries fail to redden"
gen  :518   dropped shear param  margin_dropped_shear_parameter = 0.0006932x
gen         below_ceiling_dropped_shear_parameter = 6 of 109, referenced at :543
            -- the plan asserts and refutes itself six lines apart, and the
               refutation is one of its own generated figures
plan :669   "on 19 (entry, defect) pairs ... a structural defect's effective size
             falls below 1e-6"
plan :673   "Every one of those 19 is still red, by 2.838e+05x at the weakest
             (shear_defect_exempt_L2500, wrong_dof_index) to 1.114e+08x"
cell        UNCONDITIONALLY_RED pairs with effective size below CD, at this commit
out         22 pairs, not 19
            weakest 1486x at bs_boundary_aniso1e6_L414590 / wrong_dof_index
            -- 191x off, and a different entry
            strongest 1.114e+08x -- the only one of the three that reproduces
cmd         the same two numbers, duplicated in the code
out         test_corpus_configurations.py:985-990 carries "19", "2.838e+05x",
            "1.114e+08x" verbatim
cmd         set of generated names minus set of referenced names
out         13 names, including detection_edge, detection_edge_at,
            counter_defect_over_edge, counter_headroom_room, corpus_entries,
            corpus_solved, exempt_by_defect, calibration_ulp_worst
```

The generated `clean_worst_ratio` sits inside the sentence "over the **90-entry**
corpus", so one number in that sentence regenerates and the other does not -- the
hybrid BI3 warns about, in the artifact BI3 was written for. Six lines below, "Those
**six** are the entries" is hand-typed beside the generated "6 of 109", which will
move without it.

**Closed when** `:507`, `:521`, `:669`, `:673` and
`test_corpus_configurations.py:985-990` are each regenerated, referenced, or stated
as left with a reason, site by site; and the four detection-edge figures either reach
`tolerances.py:459`, `:492-493` and `:411` by pointer or those entries say which
commit they were measured at.

**R168. (blocking) `DELTA_CALIBRATION_ULP`'s justification is refuted by measurement
at this commit. "Four times the only value ever observed" is 2x the observed
maximum: 2.000 ULP occurs, three times in 5222 admissible configurations.**
`floatfea/tolerances.py:513-521`.

```
claim  "the measured deviation is exactly 1.000 ULP over every configuration
        tried ... so 4.0 is four times the only value ever observed"   -- :515-518
cell   abs(injected_delta(e,"one_element_scaled") - CD) / ulp(CD) over random
       admissible configurations: D 1e-4..8 m, t/D 0.004..0.499, L/D 2..3e6,
       four orientations, roll and anisotropy
out    sweep A: 2256 evaluated, max 2.0000 ULP, 1 above 1 ULP
       sweep B: 2966 evaluated, histogram 0.0 x2690, 1.0 x274, 2.0 x2
       total 5222 evaluated, 3 at 2.000 ULP, none above
cmd    the three added to tests/corpus at ca42b3f, then python scripts/regen_figures.py
out    calibration_ulp_worst   1.000 ULP  ->  2.000 ULP
```

**The ceiling holds** -- 2 < 4, and the shipped assertion is live, which I checked
separately (R163). The finding is the record: the entry says the value has never been
seen above 1.000 ULP, and a five-thousand-configuration sweep at this commit says
otherwise, so the stated headroom is 2x and not 4x. All three are thick-walled,
t/D 0.44 to 0.48, with strong anisotropy, where the argmax of the numerator and of
the denominator need not coincide and the deviation stops being two roundings of one
ratio -- which is also why the two-rounding bound of 1.049 ULP, that the value looks
derivable from, is not the bound.

This is a live BI3 case rather than a historical one: the generated
`calibration_ulp_worst` and the tolerance's prose disagree the moment this corpus
lands, and only one of the two is regenerated.

**Closed when** the entry's reason states the measured maximum at a named commit and
the sweep that produced it, or `calibration_ulp_worst` is the only place the number
lives and the entry points at it.

**R169. (blocking) R157's "disagreement" is not one. The two constructions differ in
one held variable -- orientation -- and a 104-base sweep gives 7616.2x to 23918.6x.
The plan publishes 9267x as the room the rule has "where it is actually tight", and
it is neither the tightest nor a property of the rule.**
`docs/milestones/F2.md:645-657`; `scripts/regen_figures.py:95-126`.

```
claim  "The reviewer reports 7630.2x to five digits across nine families; that
        construction is theirs, this repository computes the other, and the two
        are recorded rather than averaged."                    -- F2.md:650-652
claim  "that construction is theirs and is not reproduced here" -- F2.md:655-657
        -- two adjacent paragraphs, one saying the construction is reproduced
           here and one saying it is not
cell   _boundary_margin run from EVERY solved corpus entry as its base, one
       variable moved (the base), 104 converged
out    7616.2x  x3    axis-aligned      e.g. boundary_kilo_L414p6
       7630.2x  x38   axis-aligned      e.g. boundary_thin_exempt_L38
       8218-9043x     free direction / roll
       9267.2x  x25   skew              e.g. slender_L_r_126   <- the published one
       9530-9788x     skew + roll
       16535-23919x   free direction + strong anisotropy
       TIGHTEST 7616.2x   LOOSEST 23918.6x   spread 3.14x
cell   add one admissible entry with lambda = 5.6767 (L/D = 2.002, axis) and
       regenerate, one variable moved
out    boundary_margin_one_family   9267x  ->  7630x
```

So my 7630.2x and the repository's 9267x were never two constructions. They are one
construction at two orientations, and the sweep that says so ran in 92 s. My own
headline last round -- "the same to five digits across nine section families" -- is
refuted by my own table in the same finding, which listed 7630.2, 9267.2 and 9530.3;
**I withdraw that sentence.** What is true is that the value is constant across
SECTION families at fixed orientation and moves 3.14x with orientation.

Two further properties of the construction, both measured:

* The base is the minimum by `member_lambda` and the bisection then **discards the
  base's length**, so the stated rationale -- the corpus's stubbiest entry -- does not
  determine the answer: 38 bases with different lambda give the identical 7630.2x.
  Section and orientation determine it.
* Because the selection is by lambda, **a corpus round can move a published plan
  figure by 1.22x**, and did: `bt_stubbiest_thinwall_axis_L4p004` in my corpus at
  `ca42b3f` takes the selection.

And the direction is wrong for a margin: 9267x is published as "how much room does the
rule have where it is actually tight" while 7616.2x exists in the same corpus.

**Closed when** the published boundary margin is the minimum over the bases the corpus
holds, or the figure is named for what it is -- one orientation, one section -- and the
spread is stated beside it; and `F2.md:655-657`'s "is not reproduced here" is removed,
since it is.

**R170. (recordable) `regen_figures.py --check` compares only the text above its
"Generated at" cut, and `_defined()` reads the whole file. A hand-typed row below the
cut resolves a figure reference, and a duplicate row overrides a generated value,
with the suite green.** `scripts/regen_figures.py:157-160`;
`tests/test_plan_figures.py:35-36`.

```
cell   append below the "Generated at" line two rows, hand_typed_margin = 5.150e+09x
       and a SECOND clean_worst_ratio = 999999x, and reference the first from the plan
out    python -m pytest -q tests/test_plan_figures.py  ->  15 passed
       python scripts/regen_figures.py --check         ->  "up to date", rc=0
control edit clean_worst_ratio ABOVE the cut, one character
out    FAILED test_the_generated_figures_are_not_stale
       -- the guard is real above the cut
```

5.150e+09x is the exact stale figure this round was built to eliminate, and it came
back through the file that eliminated it. `_defined()` builds a dict, so the later
duplicate silently wins; nothing asserts that a reference resolves to a GENERATED
value rather than to a row that happens to be in the file.

**Closed when** `--check` compares the whole file, with the commit stamp regenerated
or dropped, or `_defined()` reads only above the cut and rejects a duplicate name.

**R171. (recordable) `test_report_carried.py`'s reach, measured. It is a real guard --
it reddens when a finding is dropped -- and five of its limits are wider than the two
its docstring declares.** `tests/test_report_carried.py:35-40`, `:105-129`.

```
control drop the R156 row from the report
out     FAILED test_the_report_carries_the_finding[R156]     <- it works

(a) the site pattern requires a "/", so a bare filename is invisible:
cmd     per finding, paths caught against bare filenames present
out     R154 caught none, missed CLAUDE.md and test_corpus_configurations.py
        R156 caught none, missed test_corpus_configurations.py
        R159 caught none, missed test_corpus_configurations.py
        R158 and R160 also miss test_corpus_configurations.py
        -- five findings, and it is the primary site of three of them

(b) the LAST finding's block runs to end of file and absorbs every path in the
    rest of the verdict:
out     R162 charged with docs/SUPERVISOR.md,
        tests/corpus/g22_model_configurations.txt, floatfea/tolerances.py and
        tests/regression/g22_exempt_pair_responses.json -- none of which R162
        names. Two of the report's three "no change" declarations answer a
        parser artifact rather than a finding.

(c) a heading written with a space instead of the dot after the number drops the
    finding silently:
cell    malform the R162 heading AND delete the R162 row from the report
out     test_the_report_carries_the_finding[R162] does not exist; the meta-test
        stays green because nine other headings still match.

(d) a range in the verdict's Carried contributes only its endpoints:
out     "R115-R128" gives R115 and R128; R116 to R127 are never demanded.

(e) _changed_files() diffs the reviewed commit against the WORKING TREE, so the
    result is not a function of the commit:
cmd     check the report out at 4183adb, run the guard
out     22 failed: 18 identifiers and 4 sites
claim   "it found 23 failures ... 18 uncarried numbers and 5 named sites"
                                                          -- report sec. 1
        -- the 18 reproduces; 4 against 5 does not, and no command is given.
```

(e) is deliberate per the docstring, and its cost is that a green run does not mean
the same thing twice. **Closed when** the docstring records (a), (b) and (d) as reach
limits, or the parse gains a meta-check that every R-number appearing anywhere in the
verdict is either expected or explicitly excluded; and when the "23 / 5" figure
carries its command or is restated as what a clean checkout gives.

**R172. (recordable) The exempt mark added to the margins row is a kind-level count
printed on an entry-level row.**
`tests/verification/rung1/test_corpus_configurations.py:1477-1481`.

```
out    dropped_flip   minimum 6.264e+05x at shear_edge_L4000_aniso_weak
                      [9 EXEMPT: below the declared resolution]
cell   classification of the pair each row NAMES
out    dropped_flip / shear_edge_L4000_aniso_weak              below resolution
       wrong_dof_index / bs_boundary_aniso1e6_L414590          below resolution
       dropped_shear_parameter / shear_defect_live_thin_L1990  below resolution
```

Today all three coincide and nothing printed is false, which is why this is
recordable and R154 is closed. The latent case is a kind whose minimum is `live`
while the kind has exempt pairs: the row would read "[N EXEMPT]" beside a pair that
is not. **Closed when** the mark states the named pair's own classification, or the
count is moved off the row.

## Tolerances touched

**Two new entries in `floatfea/tolerances.py`, each with a counter, both named in the
plan's table, both now asserted in BOTH directions by
`test_plan_matches_tolerances.py`. No existing value moved.**

```
cmd  git diff 4183adb..b21b520 -- floatfea/tolerances.py, deletions only
out  (nothing: +50, -0)
cmd  git diff --stat 4183adb..b21b520 -- floatfea
out  floatfea/tolerances.py | 50 ++++++   (the only floatfea file in the range)
```

| site | value | form | counter | counter in its own quantity | justification located |
|---|---|---|---|---|---|
| `DELTA_CALIBRATION_ULP` `:522` | `4.0` | ULP multiple, dimensionless | `40.0` | yes, ULP | `tolerances.py:507-521`, `F2.md:883`. Measured maximum is **2.000 ULP**, not `1.000` -- **R168**. The counter is not injected -- **R163**. |
| `DELTA_CALIBRATION_ULP_COUNTER` `:529` | `40.0` | ULP multiple | -- | -- | placed inside the old 47.22-ULP band; the placement argument is correct and I reproduced the arithmetic |
| `EXEMPT_RESPONSE_DRIFT` `:544` | `1e-11` | relative, dimensionless | `1e-6` | yes, response-ratio | `tolerances.py:530-543`, `F2.md:886`. Identical to `SUBDIVISION_INVARIANCE`; measured drift `0.0`; the band is `4.81e+04` ULP -- **R164**. |
| `EXEMPT_RESPONSE_DRIFT_COUNTER` `:551` | `1e-6` | relative | -- | -- | five orders above the band: one perturbation, not a detection threshold. The threshold is the band itself, `1.0e-11`, which I solved for last round. |

`DELTA_CALIBRATION_ULP`'s FORM is right and is the round's best move: it is the first
exactness tolerance in this repository expressed in ULP with the measurement that sets
it, which is what the recorded rule asks for. Its NUMBER survives my attack -- green
at +2 added ULP, red at +5 -- and its RECORD does not (**R168**).
`EXEMPT_RESPONSE_DRIFT` gets the citation right and the measurement wrong (**R164**).

`tests/regression/g22_exempt_pair_responses.json` grew from 34 to 39 rows, all five
new rows being my seventeenth-round corpus entries, with a corpus round given as the
reason. Nothing was regenerated to match new output; I recomputed all 39 values and
every one reproduces to `0.0` relative.

**What held.** I re-derived every published figure independently. These **reproduce**:
`1211 passed`; all 25 rows of `docs/milestones/F2_figures.md`, recomputed from a fresh
`--check`; `EXEMPT 45 of 436` with `dropped_flip 9, dropped_shear_parameter 23,
wrong_dof_index 13` and 39 detected; `8.698e+06x`; `0.0006932x`; `0.0887x`; `1486x`;
`6.264e+05x`; `3.9459e-14 at aaa_band_edge_twin`; `2.534e+07x`; `2.37x`;
`1.114e+08x`; the classify ablation; R161's cell, inverted from last round; the 18
uncarried identifiers of sec. 1; and the calibration's decision boundary between 3 and
4 added ULP. These do **not**: `1.000 ULP` as a maximum (2.000 -- R168); `19 pairs`;
`2.838e+05x at shear_defect_exempt_L2500`; `90-entry`; `8.701e+06x at L/r_min 558`;
`3.9413e-14 at band_edge_isotropic_bracing`; `2.537e+07x`; "Zero entries fail to
redden"; `105-entry`; "eight sites"; `9.8e-11`; and "23 failures / 5 named sites".

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a HOLD, not a STOP: rung 1 is
green at `b21b520`, no production code moved, no existing tolerance and no existing
golden value moved, both new tolerances are bound in both directions by a test that
now catches what it missed last round, the `process:` and plan commits are correctly
standalone, and the two new guards are real guards -- I reddened each of them by
breaking what it watches.

1. **R163, R164 -- the two tolerance defects, first, because they are this round's own
   species recurring inside the fix.** A counter that is 40 > 4, and a band that
   changed its name and kept its number.
2. **R165, R166, R167 -- three closing conditions closed at part**, in the round whose
   headline guard was written for exactly that. Site by site: two sentences, one floor
   and one comment, four plan lines and one duplicated code comment.
3. **R168 -- 2.000 ULP observed where the record says 1.000 has never been exceeded.**
   The ceiling holds; the sentence does not, and the generated figure moves the moment
   this corpus lands.
4. **R169 -- the boundary margin.** 7616.2x to 23918.6x over 104 bases, one variable
   moved; the published figure is the looser one and a corpus entry takes it.
5. **R170, R171, R172 -- the reach of the three new guards**, recordable, each
   answerable in a docstring line or one assertion.
6. **R132, R134, R135, R136, R137 -- untouched from the fifteenth verdict**, with R132
   and R136 now having their correct values generated four lines away.
7. **R148, R151, R152, R159, R162 -- declared open**, answerable in one line each.
8. **R113, R95, R97, R98, R100-R103, R63, R76, R79, R80 -- carried, unchanged.**
9. **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- step 4a or later.**

**Adversarial corpus (BE3): 6 new entries committed, all unseen by the implementer;
every outcome measured before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **139** entries, 115 solved,
committed separately at `ca42b3f` immediately before this verdict and touching no
code. Full suite with the corpus applied: **1239 passed, 2 failed.**

The coverage measurement, stated plainly: **2 of my 6 new entries produce a new
exempt-and-detected pair, and BS2's golden file caught both by name, on its second
round against unseen input** -- `bt_boundary_axis_iso_below_L414p593` and
`bt_boundary_rolled_aniso_below_L513p206`, both under `dropped_shear_parameter`.
**And BT0's figures file caught its own staleness on its first round**, reporting the
seven figures that move -- including `calibration_ulp_worst 1.000 -> 2.000 ULP` and
`boundary_margin_one_family 9267x -> 7630x`, which are R168 and R169 arriving as a
build failure rather than as a review finding. That is the mechanism working, and it
is the strongest thing in this round.

Against that: the three 2-ULP entries pass under `DELTA_CALIBRATION_ULP = 4.0` and
**no shipped assertion notices that the tolerance's stated headroom just halved** --
the only thing that notices is a generated table nothing asserts a bound on.

**Eighteen consecutive rounds have found no element defect**, and the reading is
unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side. Every
defective instrument this milestone has been a test, a tolerance record or a document;
the element has been fine every time.

**Witness channel unavailable.** `git remote -v` is empty, so no PR and no
`[witness ...]` comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a
pass. Eighteen consecutive reviews by one reader.

**The standing question for the next round.** Last round I asked, for every guard,
what command shows the code path was entered. This round answers it for three guards
and exposes the question underneath. `DELTA_CALIBRATION_ULP_COUNTER` is entered and
proves nothing; `EXEMPT_RESPONSE_DRIFT` is entered and its number came from somewhere
else; `boundary_margin_one_family` is regenerated faithfully from a selection nobody
chose. **For every number this repository publishes, what would have to change in the
world for it to change here -- and is that the same thing the number claims to be
about?** A figure that moves when an unrelated corpus entry is added is not about the
rule; a band that moves only when a different test's mesh study moves is not about the
response.
