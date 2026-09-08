# Review — F2 step 4
Reviewed commit: 37353b532ece7e0b4d912abe0ecd39f1330b6f38
Verdict: HOLD
Tests: 1465 passed, 0 failed, 0 skipped   (my run at `cfb61fe`, `python -m pytest -q`,
82.3 s. With my twentieth-round corpus applied: **1483 passed, 2 failed**.)

**Reviewed code commit: `6a7c125` + `7d34675`; plan `5bc8869`; report `cfb61fe`.**
The header stamp is `37353b5`, my own corpus commit, made immediately before this
verdict and touching no code.

Twentieth pass. Range `ba3a93c..cfb61fe`, four commits.

```
cmd  git diff ba3a93c..cfb61fe -- .claude docs/SUPERVISOR.md
out  (empty)  -- my instructions untouched this round. Nothing added, nothing
     deleted.
cmd  per commit, files under floatfea/ and under docs/reviews/
out  5bc8869 0/0 ; 6a7c125 1/0 ; 7d34675 0/0 ; cfb61fe 0/0  -- correctly routed
cmd  git diff ba3a93c..cfb61fe -- floatfea/tolerances.py | grep -E "^[+-][A-Z_]+.*Final"
out  (nothing)  -- NO CONSTANT MOVED this round. Comments only.
cmd  git diff ba3a93c..cfb61fe -- tests/ | grep "xfail|pytest.skip|mark.skip"
out  (nothing)
cmd  grep -n "^Answers:" docs/reports/F2/step-4.md ; newest commit on the verdict
out  :2860 verdict 18 @ 7e6df21 ; :3003 verdict 19 @ ba3a93c ; newest is ba3a93c
```

**Item 1b, performed: the header names the latest verdict.** The newest revision
carries exactly one `Answers:` line and it names `ba3a93c`, the newest commit
touching the verdict file. PASS on that item, and the round added a guard of its
own for the two-header case.

**The round's real closures, stated first.** R175's bracket is genuinely bracketed
and I could not break it; R179's whole-file `--check` is the right cut and nothing
in that file now sits below a comparison; R173's counter is a real injection -- I
deleted its gate outright and the counter went red. R176's three `tolerances.py`
sites and the `test_corpus_configurations.py` comment block are all genuinely
fixed, breaking a five-round species. Those are good moves and I say so before the
rest.

**And the round's headline mechanism cannot fail for the defect it was written
for.** `tests/test_counters_are_injected.py` neuters the *ceiling constant* that a
degenerate counter also reads, rather than the gate's assertion -- so both
historical defective counters fail under it too, and it admits them. That is
**R182**, and it outranks everything in the report.

## Carried

Every item from the nineteenth verdict (`HOLD @ f963b3d`), re-measured at
`cfb61fe`, plus the older carry.

- **R173 (blocking) -- CLOSED, and I broke it to prove it.** The counter now
  perturbs a recorded value and runs `test_every_recorded_pair_is_still_detected`
  on it. Cell: replace that gate with `lambda: None`, one variable moved --> the
  counter fails (`Failed`). Second cell: ceiling -> inf --> fails. It is an
  injection. The meta-test that certifies it is not -- see **R182**.
- **R174 (blocking) -- CLOSED ON THE ARGUMENT, with one false pointer.** "Four
  times a maximum observed at zero" is withdrawn, the arithmetic that evaluated to
  zero is gone, and the class argument is a real argument: the quantity's own drift
  is exactly `0.000e+00`, so it takes a sibling's measured maximum rather than
  fitting to nothing. **I judge it a reason, not a rationalisation.** The defect is
  the pointer -- see **R191** -- and that it leans on **R184**.
- **R175 (blocking) -- CLOSED, and the refusals are genuine.** I re-ran the shipped
  construction: 116 converged + 5 refused + 0 unbracketed = 121 = `corpus_solved`,
  everything accounted. I checked all five refusals myself rather than accepting
  them: each brackets fine and bisects fine, and raises only at the final
  `_oob_with_injected`, where the converged length puts the orientation node
  `0.358 deg` / `2.043 deg` off the axis, below `MEMBER_ORIENTATION_DEGENERACY`.
  **That is genuinely the probe's fault and not a base you should have kept.**
  min/max/spread reproduce to every digit. What the fix did not reach is **R187**:
  the minimum is a 49-base plateau and `_min_at` is decided at the ninth digit.
- **R176 (blocking) -- CLOSED AT EVERY SITE.** `tolerances.py:411`, `:459`,
  `:492-493` all point at generated figures now; the counts and margins are out of
  `test_corpus_configurations.py:993-1000`. One survivor at a site the condition
  did not name: **R192**.
- **R177 (blocking) -- CLOSED.** `grep -rn "1.000 ULP|four times it" tests/ floatfea/`
  returns only withdrawal text.
- **R178 (blocking) -- NOT CLOSED, AND RECORDED CLOSED.** The unreproducible table
  is still in `floatfea/tolerances.py`, its named site is declared `no change --
  names it in evidence, not as a site to change`, and the generated replacement now
  contradicts it in every cell. See **R184**, and **R185** for what the replacement
  measures.
- **R179 (recordable) -- CLOSED.** The stamp is gone, `--check` compares the whole
  file, and `regen_figures.py --check` is green at `cfb61fe`. I read the file for
  anything else nothing compares: there is nothing -- every row is generated and
  the header is fixed text inside the comparison. **Nothing else in that file is
  unverifiable.**
- **R180 (recordable) -- NOT CLOSED, AND RECORDED CLOSED.** Both named sites still
  carry the false sentence verbatim, both declared `no change`. See **R186**.
- **R181 (recordable) -- OPEN, correctly declared**, with the duplicate-header case
  now guarded. The one-assertion cost of the adjacent-verdict swap stands.
- **R170, R171 -- 4a, accepted.** Four of R171's parser holes are fixed here, which
  I welcome; **R189** and **R190** are two more, and they stay 4a.
- **R172 (recordable) -- OPEN, declared.** Unchanged.
- **R159, R162, R151, R152 (recordable) -- OPEN, declared, unchanged.**
- **R148 -- CLOSED.** `K_bend/K_max ~ 12/lambda_elem^2` is now stated as the
  isotropic circular case and not as a law.
- **R129, R131, R132, R136, R138, R139 -- as declared;** R132's and R136's sites are
  closed inside R176.
- **R134, R135, R137 (recordable) -- OPEN, UNTOUCHED.** "nine orders"; the solved
  count is now 121; the `delta < CD` assert inside a branch requiring
  `delta < CD - 4*ulp(CD)` is still a tautology.
- **R113, R95, R97, R98, R100, R101, R102, R103 -- OPEN, correctly declared.**
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict; the report lists it open.**
  Recorded as a disagreement, not a finding.
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, 4a or later.
- **R68's standard -- MET, fourth round.**

## Findings

**R182. (blocking) The counter meta-test neuters the wrong thing and cannot fail
for either defect it was written for. Both R163's and R173's counter bodies PASS
it. "It caught the exempt-drift counter as written" is refuted by one cell.**
`tests/test_counters_are_injected.py:46-50`, `:77-101`; report section 2.

```
code   def _neuter_ulp(module, name):  setattr(module, name, float("inf"))
       -- it raises the CEILING CONSTANT. But a degenerate counter is exactly one
          that compares itself against that same constant, so raising it makes the
          degenerate counter fail too, and the meta-test reads that as injection.
cell   R173's counter body, verbatim, with EXEMPT_RESPONSE_DRIFT_ULP -> inf
out    raises AssertionError  -> the meta-test PASSES it
cell   R163's counter body -- 40*ulp(CD)/ulp(CD) > DELTA_CALIBRATION_ULP --
       with DELTA_CALIBRATION_ULP -> inf
out    raises AssertionError  -> the meta-test PASSES it
cell   THE DISCRIMINATING NEUTERING: replace the GATE FUNCTION with a no-op,
       one variable moved, constants untouched
out    R163's counter        PASSES  -> defect exposed
       R173's counter        PASSES  -> defect exposed
       shipped calibration   Failed  -> genuinely injected
       shipped exempt-drift  Failed  -> genuinely injected
claim  "It caught the exempt-drift counter as written."          -- report sec. 2
       -- refuted by cell 1. It would have passed it.
```

Its reach, stated exactly: it catches only a counter that neither runs the gate
**nor mentions the ceiling**. Neither historical defect had that shape; both
mentioned the ceiling. This is the eighth guard's own species -- a check that
passes while certifying nothing -- landing on the commit that generalises the
eighth guard.

**Closed when** the neutering replaces the gate's assertion (its function, or the
assertion inside it) rather than a constant the counter also reads, and the
meta-test is shown RED against the R163 and R173 counter bodies -- the two cells
above, run and pasted.

**R183. (blocking) `_NOT_REGISTERABLE`'s single exemption is false as written, and
the pair it exempts registers under the meta-test's own recipe. It also names the
counter as the gate.** `tests/test_counters_are_injected.py:63-69`.

```
claim  "its gate is the red-on-defect assertion, which compares against
        PATCH_TEST_EXACTNESS inline in 296 parametrised cases rather than through
        a module-level name"
cmd    grep -n "PATCH_TEST_EXACTNESS," tests/verification/rung1/test_corpus_configurations.py
out    :83  -- it IS a module-level name, imported at module scope and resolved at
       call time. setattr reaches it.
cell   CORPUS.PATCH_TEST_EXACTNESS -> inf, one variable moved
out    gate  test_the_corpus_entry_behaves_as_the_reviewer_recorded : PASS
             (worst <= inf, vacuous -- correctly neutered)
       counter test_..._goes_RED_under_every_injected_defect, 3 pairs :
             FAIL, FAIL, FAIL (AssertionError)
       -- exactly what the meta-test requires. It registers.
note   the entry also mislabels the pair: the red-on-defect test is the COUNTER;
       the gate is the exactness assertion at `:749`.
```

The only real obstacle is that the counter takes `(entry, kind)`, which a one-line
wrapper binding a single pair removes. So the biggest counter in the file sits
outside the guard written for counters, behind a reason that is not the reason.

**Closed when** the pair is registered -- gate
`test_the_corpus_entry_behaves_as_the_reviewer_recorded`, ceiling
`PATCH_TEST_EXACTNESS`, counter a wrapper on one `(entry, kind)` pair -- or the
exemption states the true obstacle and drops the false claim about module-level
names.

**R184. (blocking) R178 is recorded closed, its named site is untouched, and the
unreproducible histogram is still in `floatfea/tolerances.py` -- now contradicted
by the generated one it is cited through. BI3, locked two commits before this
range, forbids exactly this.** `floatfea/tolerances.py:523-527`; report section 4
and the declaration table.

```
cmd    grep -n "5106" floatfea/tolerances.py
out    :527  "0 ULP x 5106      1 ULP x 113      2.000 ULP x 3"
       over :525 "5222 admissible configurations"  -- unchanged, byte for byte
cmd    grep calibration_ulp_histogram docs/milestones/F2_figures.md
out    :42  0 ULP x4760, 1 ULP x137, 2 ULP x103
       -- two histograms of the same-named quantity, in the same repository,
          disagreeing in every cell and in their totals (5222 vs 5000)
claim  "R178: the histogram is seeded and generated, so the table reproduces"
       -- the GENERATED table reproduces. THE TABLE IN tolerances.py DOES NOT, and
          it is the one BI3 is about and the one R178 named.
decl   `floatfea/tolerances.py:518` .. `:522`  "no change -- R178 names it in
       evidence, not as a site to change"
       -- FALSE. R178's headline is "The histogram published in tolerances.py";
          `:518-522` at the reviewed commit IS that histogram.
```

This is the answer to the question the round asks of its own guard, and it is one
of the two places I found it: **the `no change` mechanism was used to wave away a
site the finding was about.** The guard did its job -- it forced the site to be
named -- and the naming was answered with a sentence that is not true.

**Closed when** `tolerances.py` carries the single number it needs (observed
maximum 2 ULP) and a pointer to `calibration_ulp_worst`, with no table -- per BI3
and per R178's own first branch.

**R185. (blocking) The generated `calibration_ulp_histogram` is 5000 resamples of
121 deterministic points. Its cells are seed noise, and it narrows the population
it replaces without saying so.** `scripts/regen_figures.py:104-125`.

```
cell   the EXACT distribution over the 121 solved entries, no draw, no seed
out    {0 ULP: 115, 1 ULP: 3, 2 ULP: 3}
       the 2-ULP entries are bt_calib_2ulp_thick_aniso5e4_L68,
       bt_calib_2ulp_skew_aniso37e4_L0p86, bt_calib_2ulp_inplane_aniso1e5_L30
cell   the shipped draw at seeds 20260908 / 1 / 2 / 20260909, one variable moved
out    2 ULP x103 / x126 / x110 / x124      1 ULP x137 / x119 / x133 / x140
       -- +/-20% on the seed alone. The seed is what makes it reproduce; the
          measurement underneath it is 121 numbers.
claim  the entry it replaces described "5222 admissible configurations" over a
       sweep in D, t/D, L/D, orientation, roll and anisotropy
       -- the replacement samples only the corpus. Narrower population, same name.
```

Drawing 5000 times with replacement from 121 points adds multiplicity noise and no
information. The exact statement is cheaper, needs no seed, and cannot drift.

**Closed when** the figure is the exact per-entry count over the solved corpus
(`0 ULP xN, 1 ULP xN, 2 ULP xN`, no `random`, no draw count), or the sweep itself
is generated with its protocol declared.

**R186. (blocking) R180 is recorded closed with its false sentence intact at both
named sites, both declared `no change`. Re-solved: the boundary is between 2 and
2.5 ULP, not at 5.** `floatfea/tolerances.py:542-543`;
`tests/verification/rung1/test_corpus_configurations.py:1224-1226`.

```
cmd    grep -rn "ULP passes and 5 ULP fails" floatfea/ tests/
out    floatfea/tolerances.py:542
       tests/verification/rung1/test_corpus_configurations.py:1225
       "... so the counter sits at the first value that must be caught"
cell   inject k ULP into injected_delta and run the shipped calibration
out    +0 PASS  +1 PASS  +2 PASS  +2.5 FAIL  +3 FAIL  +4 FAIL  +5 FAIL
decl   `floatfea/tolerances.py:534` .. `:540` and
       `tests/verification/rung1/test_corpus_configurations.py:1210` .. `:1212`
       -- all ten rows "no change -- R180 names it in evidence, not as a site to
          change". R180's condition was "the sentence states the measured
          boundary, or drops the causal clause". The sentence IS the site.
report "R180 closed -- the counter runs its gate now, so the constant is the size
        injected rather than a claimed threshold"
       -- true, and not what R180 was about.
```

**Closed when** both sites state the measured boundary (between 2 and 3 ULP) or
drop the "so the counter sits at the first value that must be caught" clause and
keep the definitional one -- the smallest whole number above the ceiling.

**R187. (blocking) `boundary_margin_min_at` is a selection at the ninth
significant digit, not a location -- and the selector is an undeclared convergence
threshold in a file the tolerance scanner does not read.**
`scripts/regen_figures.py:201`; `docs/milestones/F2_figures.md:37`.

```
cell   the shipped construction, all 116 converged bases, at cfb61fe
out    minimum 7630.155140054562 at boundary_kilo_L414p6
       bases printing as `7630.16x`            49 of 116
       bases within 1e-9 relative of the min    2
       -- the published minimum is a 49-base plateau, flat to 8 significant
          figures. `_min_at` names whichever wins at the 9th.
cell   ONE VARIABLE MOVED: `hi / lo < 1.000001` -> `hi / lo < 1.0 + 1e-12`,
       nothing else touched
out    minimum 7630.1551260985825 at aniso_bend_block_is_largest
       -- `_min_at` changes; `boundary_margin_min` still prints 7630.16x
cell   my four corpus entries added, shipped threshold unchanged
out    boundary_margin_min_at  boundary_kilo_L414p6 -> cf_minshadow_D0p239_...
       boundary_margin_min     7630.16x -> 7630.16x   (UNCHANGED)
cmd    grep -n "not-a-tolerance" scripts/regen_figures.py ; the scanner's file set
out    :201  "# not-a-tolerance: bisection convergence"
       tests/test_no_tolerance_literals.py:128  _test_files() = TESTS.rglob("test_*.py")
       -- scripts/ is not scanned. That marker is read by nothing.
```

`CLAUDE.md` Tolerances names convergence thresholds explicitly. `1.000001`,
`1.0e9`, the `1.000001` bracket-bottom factor, `5000` draws and seed `20260908`
all sit outside `tolerances.py` and outside the scanner, and the first of them is
measurably load-bearing for a published figure.

**Closed when** `boundary_margin_min_at` reports the plateau rather than one name
-- how many bases share the minimum at the published precision -- and the
convergence threshold is declared, or the figure is shown insensitive to it by
re-running at two thresholds and getting the same published row.

**R188. (blocking) Report section 1's site counts describe no state of this
repository, and contradict the report's own table.** report section 1.

```
claim  "It shows 70 sites where the file-level version showed 5."
cmd    the shipped parse at cfb61fe: len(SITES), and how many need a declaration
out    186 parametrisations; 145 not covered by a hunk; 145 declared; 0 missing
cmd    the FILE-level parser of ba3a93c, run on this round's verdict and diff
out    18 parametrisations, 2 failures (both R181's, from the end-of-file absorb)
       -- neither 70 nor 5 is reproducible, and the declaration table below the
          sentence has exactly 145 rows.
```

**Closed when** the sentence carries the command that produces its numbers, as
every figure in a report must.

**R192. (blocking, the smallest of these) A fourth copy of the stale
detection-edge ratio survives in `tolerances.py`, in the present tense, at a site
no condition named.** `floatfea/tolerances.py:505-507`.

```
code   :507  "against the smallest edge the ratio is `2.537e+07` and `2.0e7` fails"
cmd    grep counter_defect_over_edge docs/milestones/F2_figures.md
out    2.534e+07x
```

R176 fixed `:492-493` and left the same number, present tense, fifteen lines above.
**Closed when** it reads as history -- the value at the derivation -- or points at
`counter_defect_over_edge`.

**R189. (recordable, 4a) The `no change` escape is a bare substring test, so one
declaration pre-closes every site whose `path:line` is a prefix of it.**
`tests/test_report_carried.py:271-277`.

```
code   if site in text_line or (line == 0 and path in text_line): return
cell   sites a FUTURE verdict could name, tested against THIS report's table
out    tests/test_report_carried.py:12   already declared away (by the `:120` row)
       floatfea/tolerances.py:53         already declared away (by the `:534` row)
       scripts/regen_figures.py:10       already declared away (by the `:100` row)
       docs/milestones/F2.md:66          already declared away (by the `:660` row)
cell   sites closed ONLY by adjacency to a pure insertion (the count == 0 span),
       measured at this commit
out    0  -- the +/-1 hatch exists and was not used this round
```

Anchor the match on a non-digit boundary. 4a with R171.

**R190. (recordable, 4a) The report's `{{fig:...}}` placeholders are bound by
nothing.** `tests/test_plan_figures.py:39-40`.

```
code   _referenced() reads PLAN only
cmd    the 11 distinct names the report uses, checked against the figures table
out    all 11 resolve at cfb61fe -- checked by hand, which is the point
```

**R191. (recordable) `EXEMPT_RESPONSE_DRIFT_ULP`'s reason is a reason; its pointer
is false.** `floatfea/tolerances.py:570-576`.

```
code   "the basis for that class is `DELTA_CALIBRATION_ULP`'s seeded histogram"
       -- the histogram in THIS FILE is the unseeded one (R184). The seeded one
          lives in the figures file, over a different population (R185).
judge  the ARGUMENT is sound and I say so: the quantity's own drift is exactly
       zero, so there is nothing to fit to, and borrowing a sibling's measured
       maximum is the honest move. It is not a rationalisation.
cell   MY OWN SUPPORT FOR IT, offered because the entry needs it: 2947 admissible
       random configurations (D 1e-4..8 m, t/D 0.004..0.499, L/D 2.5..1e6, four
       orientations, anisotropy to 1e6) plus 4296 draws targeted at the known
       2-ULP region
out    maximum 1.000 ULP on the random sweep, 2.000 ULP on the targeted one.
       NOTHING ABOVE 2 ULP IN 7243 TRIES. The 2x headroom is real and measured.
warn   the class maximum currently rests on 6 corpus entries, 3 of them planted by
       me at the eighteenth verdict. Remove them and `calibration_ulp_worst` falls
       to 1 and the stated headroom doubles.
```

**Closed when** the pointer names `calibration_ulp_worst` in the figures file
rather than "the histogram" in a file where the histogram is the wrong one.

## Tolerances touched

**None. No constant moved in this range.**

```
cmd  git diff ba3a93c..cfb61fe -- floatfea/tolerances.py | grep -E "^[+-][A-Z_]+.*Final"
out  (nothing)
cmd  the diff read line by line for a value that moved in any direction
out  comments only, at four entries. No threshold, no counter, no form.
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `DELTA_CALIBRATION_ULP` `:534` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `5.0`, injected (verified) | `tolerances.py:511-533`. Table still unreproducible -- **R184**; the counter's boundary sentence still false -- **R186**. |
| `EXEMPT_RESPONSE_DRIFT_ULP` `:578` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `10.0`, injected (verified two ways) | `tolerances.py:561-577`. Reason re-derived and now sound -- **R191** on the pointer only. |
| `PATCH_TEST_COUNTER_HEADROOM` `:509` | `6.0e7` | `6.0e7` (unchanged) | ratio, dimensionless | -- | `tolerances.py:491-508`. Stale figure at `:507` -- **R192**. |
| `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` `:467` | `1.0e-6` | unchanged | relative defect size | the red-on-defect test | outside the new injection guard on a false reason -- **R183**. |

**Undeclared thresholds outside `tolerances.py`, measured as load-bearing:**
`scripts/regen_figures.py:165` (`1.000001` bracket bottom, `1.0e9` bracket top),
`:201` (`1.000001` convergence -- changes a published figure, R187), `:116-120`
(`5000` draws, seed `20260908` -- sets every cell of a published histogram, R185).
The scanner does not read `scripts/`.

**What held.** These reproduce at my run: `1465 passed`; `regen_figures --check`
green; every row of `F2_figures.md` against a fresh run; `boundary_margin_min`
`7630.155140054562`, `_max` `23918.611998211458`, `spread` `3.135`, `bases 116`,
`refused` five by name, `unbracketed` none -- **116 + 5 + 0 = 121 = corpus_solved,
everything accounted**; all five refusals verified to be probe artefacts at the
converged length, not bases that should have been kept; the exempt-drift counter's
injection under two ways of breaking it; the calibration counter's injection under
two more; `calibration_ulp_worst` `2.000 ULP` and my own 7243-configuration
support for it. These do **not**: "it caught the exempt-drift counter as written"
(R182); the `_NOT_REGISTERABLE` reason (R183); "the histogram is seeded and
generated, so the table reproduces" (R184); "70 sites where the file-level version
showed 5" (R188); R178's and R180's `no change` declarations (R184, R186);
`boundary_margin_min_at` as a location (R187); `2.537e+07` (R192).

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a HOLD, not a STOP: rung 1
is green at `cfb61fe`, `floatfea/` production code is untouched for a fifth
consecutive round, no constant moved at all this round, no test was skipped or
xfailed, my instructions are byte-identical, the plan and step commits are
correctly routed, and three of the round's four substantive fixes survive every way
I found to break them.

1. **R182 first, before anything else.** The mechanism this round is built on
   admits both defects it was written for. Two cells, already run, are in the
   finding; the fix is to neuter the gate rather than the constant, and to show the
   meta-test red against the two historical counter bodies.
2. **R183 -- the exemption, which registers.** One wrapper, or a true reason.
3. **R184, R185 -- the histogram, both halves.** The stale table is still in
   `tolerances.py` against a locked BI3, and the generated replacement is a
   resampling whose cells belong to the seed.
4. **R186 -- R180's sentence, at both named sites.** Still false, recorded closed.
5. **R187 -- `boundary_margin_min_at`, and the thresholds in `scripts/`.**
6. **R188, R192 -- two figures that do not describe the repository**, one line each.
7. **R189, R190 -- 4a**, with R170, R171, R172, R159, R162, R151, R152.
8. **R134, R135, R137 -- untouched from the fifteenth verdict.**
   R129/R131/R132/R136/R138/R139 as declared.
9. **R113, R95, R97, R98, R100-R103, R63, R76, R79, R80 -- carried, unchanged.**
   R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- 4a or later.

**On the `no change` mechanism, since the round asks.** It is a real improvement
and I want it kept. 145 declarations on 186 parametrisations, every one present;
the file-level parser on the same data would have demanded 18 and failed 2. I
sampled the declarations against the reviewed commit's actual line contents: the
`scripts/regen_figures.py:100-143`, `docs/milestones/F2.md:658-668` and
`tests/test_report_carried.py:84-134` blocks are honestly quoted evidence, and
`test_corpus_configurations.py:993` is a context line above a hunk that did move.
**Two are not**: R178's `tolerances.py:518-522` and R180's two site blocks are the
findings themselves, declared as evidence. So the escape hatch is being used to
wave away real sites -- twice out of 145 -- and both times on the item the
declaration then let be recorded closed. The mechanism found them for me, which is
why it should stay; the discipline it needs is that a site inside a finding's
**Closed when** can never be answered with `no change`.

**Adversarial corpus (BE3): 4 new entries committed, all unseen by the
implementer; every outcome measured at `cfb61fe` before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **149** entries, 125 solved,
committed separately at `37353b5` immediately before this verdict and touching no
code. Full suite with the corpus applied: **1483 passed, 2 failed.**

The coverage measurement, stated plainly: **2 of my 4 new entries produce a new
exempt-and-detected pair and BS2's golden file caught both by name** --
`cf_minshadow_D0p0586_t0p0064_axis|dropped_shear_parameter` and
`cf_minshadow_D0p4317_t0p1687_axis|dropped_shear_parameter` -- and BT0's figures
file caught its staleness on nine rows. Both mechanisms work, fourth round running
against input their authors never saw.

**Against that, and it is R187's measurement:** the entry that changes
`boundary_margin_min_at` is invisible. `_min_at` moves from `boundary_kilo_L414p6`
to `cf_minshadow_D0p239_t0p0903_axis` while `boundary_margin_min` still reads
`7630.16x` -- so the only thing that reddens is the byte comparison, which says the
file changed, not that the figure now means something different. Three of the four
entries also sit on the classification boundary itself, at `eff/CD` =
`1.00001531315`, `0.999996865945` and `0.999993001633` -- `1.5e-5`, `3.1e-6` and
`7.0e-6` from `CD`, from both sides, against a previous closest approach of
`2.4e-2`. The decision surface is now bracketed to `1.5e-5` in the corpus.

**What I could not build, recorded so a figure is not over-read.**
`boundary_margin_unbracketed` is `0: none`, and with the bracket at
`[shortest admissible, 1e9]` and `eff/CD` falling as roughly `L^-4` I could not
construct a base that escapes it. That row may be structurally unreachable, and a
row that cannot move is not a check.

**Twenty consecutive rounds have found no element defect**, and the reading is
unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side. Every
defective instrument this milestone has been a test, a tolerance record, a
generator or a document. This round adds a new species to that list: **a meta-test
written to catch defective counters, which passes both of the defective counters
that motivated it.**

**Witness channel unavailable.** `git remote -v` is empty, so no PR and no
`[witness ...]` comment; per `docs/SUPERVISOR.md` that is an unavailable check, not
a pass. Twenty consecutive reviews by one reader.

**The standing question for the next round.** Last round I asked, for every
generated figure, what input would move it and whether the corpus can reach it.
This round answers it and sharpens it once more: `boundary_margin_min_at` moved
under my corpus and nothing noticed, because a whole-file comparison proves only
that the file equals the run. So -- **for every check added in a round, what is the
defect it was written for, and does it go red on that defect's actual code?** R182
is that question asked of this round's headline, and the answer was no.
