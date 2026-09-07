# Review — F2 step 4
Reviewed commit: 77b1ad418aa0f2cf77e488607b29169a4c8877b7
Verdict: HOLD
Tests: 947 passed, 0 failed, 0 skipped   (my run at `9b866ce`, `python -m pytest -q`,
30.26s. With my sixteenth-round corpus applied at `77b1ad4`: **996 passed, 1 failed**.)

**Reviewed code commit: `a634970`; plan `d920a8d`; report `9b866ce`.** The header
stamp is `77b1ad4`, my own corpus commit, made immediately before this verdict and
touching no code.

Sixteenth pass. Range `5e923a3..9b866ce`, three commits. `git diff
5e923a3..9b866ce -- .claude docs/SUPERVISOR.md` is **empty** and `git log
--oneline 5e923a3..9b866ce -- CLAUDE.md` returns nothing: my own instructions
were not touched, which I diffed rather than inferred from a suite that does not
read them. `git diff --stat 5e923a3..9b866ce -- floatfea` is **empty** -- no
production code, and no tolerance, moved in this range. No commit touches both
`floatfea/` and `docs/reviews/`.

**Rung 1 is green and the STOP is lifted.** Both of the fifteenth verdict's STOP
conditions were met: the plan reopened in a standalone commit before the code
(`d920a8d`), and the two red rung-1 cases are green without a number moving.
`git diff 5e923a3..9b866ce -- floatfea/tolerances.py` is empty, `git diff --stat
... -- tests/regression` is empty, no `expect` field on any corpus line changed,
no `xfail`, no `skip`. I checked each of those rather than accepting the claim.

**R130 was answered, and answered well.** The plan took the third option, the
metric is the one the evidence supported, and every headline figure in sec. 2-4 of
the report reproduces on my run: `4447x`, `4.263e+08x`, `19` pairs,
`2.838e+05x at shear_defect_exempt_L2500/wrong_dof_index`, `1.114e+08x`,
`15 of 89`, and all seven cells of the bending-only table. Sec. 4's withdrawal of the
`live` half is the right call and the honest one -- I tried to find the thing it
might be hiding and did not find one. **BR4 is not triggered: BR1-BR2 are not
refuted.** I could not produce a live pair that responds below the ceiling in a
3045-pair sweep, and the metric is unit-invariant to six digits across `10^6` of
length unit, which nobody had measured.

This is a HOLD for what the round did not carry, and for one defect in the part
the directive called load-bearing.

## Carried

Every item from the fifteenth verdict (`STOP @ 7daffed`, committed `5e923a3`),
traced through `5e923a3..9b866ce` and re-measured, plus the older carry. **The
report carries none of R129-R139 by number**; the statuses below are mine.

- **R129 (STOP) -- CLOSED AT THREE SITES OF FIVE, OPEN AT TWO.** `:558` now says
  `6.0e7`; `:557-560` carry the runner's edge and the solved boundary; `:564`'s
  "harder entry loosens" mechanism is withdrawn with the reason. `:531` and
  `:542` are untouched and `:542` is refuted at this commit. See **R141**.
- **R130 (STOP) -- CLOSED.** The plan reopened, stated which of the three options
  it takes, and measured the block dependence. Credit; this was the hard one.
- **R131 (blocking) -- CLOSED on the move it named.** I re-ran the cell:
  `CD 1e-6 -> 1e-4` **and** `HEADROOM 6.0e7 -> 3.0e9` now gives `2 failed, 945
  passed`; `CD` alone gives `2 failed, 995 passed` via
  `test_the_counter_DEFECT_SIZE_cannot_be_raised`. Both constants are bounded.
  What replaced the surface is **R145**.
- **R132 (blocking) -- OPEN, untouched.** `sed -n '492,493p' floatfea/tolerances.py`
  still prints `3.9413e-14` and `2.537e+07x`; the runner prints `3.9459e-14` and
  `2.534e+07x`. `git diff 5e923a3..9b866ce -- floatfea/tolerances.py` is empty.
  The plan was corrected to the runner's figures at `d920a8d`; the tolerance entry
  that the plan's figures came from was not, so the two documents now disagree
  where they agreed before the range.
- **R133 (blocking) -- OPEN, untouched.**
  `tests/verification/rung1/test_corpus_configurations.py:519-526` still states
  the causal chain I refuted with a controlled revert. It is now wrong twice: the
  route it describes does not exist, and the classification it blames the
  arithmetic for is computed by a function whose result is exact for the shipped
  `CD` and inexact for others -- see **R142**, which is the same arithmetic seen
  from the other end.
- **R134 (recordable) -- OPEN.** "nine orders" for `9.881e+06` stands in revision
  15 sec. 5; revision 16 does not correct it.
- **R135 (recordable) -- OPEN AND WIDER.** `74` became `81` became `89`. The
  locked plan still says `0 of 74 entries` at `:538` (**R141**), and the report's
  own opening says `105-entry corpus` where the runner prints `113` (**R151**).
- **R136 (recordable) -- OPEN, untouched.** `floatfea/tolerances.py:459` still
  says `at L/r_min = 558`; the runner prints `at posed_axis (L/r_min 46.5)`.
- **R137 (recordable) -- OPEN, untouched.** The tautology is at
  `test_corpus_configurations.py:1027`, one line below the branch condition that
  guarantees it.
- **R138 (recordable) -- CLOSED in the module it named**, and I verified the
  numbers did not move: over all six states the direct application changes the
  asserted ratio by at most `1.7e-4` against a band of `5e-2`, and the resultant
  ratios by at most `4.4e-5`. Scope wording is **R151**.
- **R139 (blocking) -- OPEN, AND NO LONGER LATENT.** See **R143**. At `7daffed`
  the branch was dead; at `9b866ce` it exempts 15 pairs and the printed table
  still has no marker and no count.
- **R113 -- carried, OPEN, correctly declared.** `grep -n "_section(entry"` still
  returns `:673` inside `_inadmissible`.
- **R95 -- carried, OPEN, correctly declared.** `pytest.raises(ValueError)` with no
  `match` at `:738`.
- **R97 -- carried, OPEN.** `grep -n "never asserted at a constant"
  docs/milestones/F2.md` returns `:783` and `:1503`.
- **R98 -- carried, OPEN.** `INADMISSIBLE` four occurrences, none an assertion.
- **R100 -- carried, OPEN.** `ls scripts/` is still `write_verdict.py` alone, and
  this round put a seven-column measured table into the **locked plan**, which is
  the one document nothing regenerates (**R146**).
- **R101, R102, R103 -- carried, OPEN.** `grep -n "revision 1"
  floatfea/tolerances.py` returns `:189` and `:624`, both "revision 10".
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.**
- **R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36, R50, R52, R62 -- still
  open**, routed to step 4a or later.
- **R115-R128 -- closed at the fourteenth and fifteenth verdicts.**
- **R68's standard -- LAPSED for the second consecutive round.** Revision 16
  records no section on the round's own errors, in a round whose commit message
  and report both carry a stale corpus count.

## Findings

**R140. (blocking) The report's `Carried` section omits R129-R139 entirely --
eleven findings from the verdict it is answering, five of them blocking or
STOP-class.** `docs/reports/F2/step-4.md` sec. 8.

```
claim  "R122-R128 closed. R123 answered by 2-4. R113, R95, R97, R98, R100-R103,
        R63, R76, R79, R80 and the older set open, unchanged."   -- report sec. 8
cmd    sed -n '/^# Revision 16/,$p' docs/reports/F2/step-4.md | grep -nE "R1(29|3[0-9])"
out    (nothing)
```

Five of the eleven are substantively answered in prose without their numbers
(R129 partly, R130, R131, R138; R135 not at all), and four are untouched in the
repository (R132, R133, R136, R137). The one that matters most is R139: it was
blocking, it was latent when I raised it, this range made it live, and nothing in
the report mentions it.

This is the guard the whole arrangement exists for, and it is the second
consecutive round in which a closing condition that named sites was closed at
some of them and recorded as answered. `CLAUDE.md` sec. "A closing condition that
names sites is closed site by site" was written for exactly this, one round ago.
**Closed when** the report carries R129-R139 by number with a status each --
answered where, still open, or withdrawn why.

**R141. (blocking) R129 is closed at three sites of five. `F2.md:534-542` still
publishes three figures the shipped runner refutes at this commit, in the
document that was reopened to fix them.** `docs/milestones/F2.md:531`, `:538`,
`:542`.

```
plan :538  "Re-measured against the ceiling: 0 of 74 entries at or below it,
            minimum margin 1739x at plan_headline_lam2885"
cmd        python -m pytest -q -s <the corpus runner> -k REPORTED
out        dropped_shear_parameter minimum 0.0006932x at shear_defect_live_thin_L1990
           and six entries at or below the ceiling: 0.8806, 0.7813, 0.4247,
           0.0006932, 0.002448, 0.8806
```

Three refutations in one bullet: `74` (89 solved), `0 of 74` (6 of 89), and
`minimum 1739x` (`0.0006932x`, six orders out and on the wrong side of 1). The
next sentence, `:542` -- "`Phi ~ 1/lambda^2` does shrink the defect on a slender
member; it does not take it below the ceiling anywhere in the corpus" -- is the
sentence whose falsity is the entire subject of BR1, still standing 80 lines
above the section written to replace it. `:531`'s near-axis sentence is likewise
untouched.

The plan commit corrected the sites it chose and left the two the previous
verdict also named. Nothing catches this: `tests/test_plan_matches_tolerances.py`
checks values, and these are prose (its own docstring says so, correctly).
**Closed when** `:531`, `:538` and `:542` are each answered or stated as left with
a reason, as R129's condition asked.

**R142. (blocking) The calibration the round calls load-bearing is asserted with
`==` on a justification that is arithmetically false, and it goes red on a
legitimate corpus entry with a message that misdiagnoses the failure.**
`tests/verification/rung1/test_corpus_configurations.py:1050-1065`; report sec. 2;
`F2.md:600-606`; commit message BR1.

```
claim  "the injection is `CD * k` and the measure is `max|CD * k_hat| /
        max|k_hat|`, so the constant divides out and the result is the same
        float. If this ever needs a tolerance, the two sides have stopped being
        the same quantity."                              -- :1057-1060
cell   (CD*x)/x == CD over 200000 random x in [1e-3, 1e3], CD the only variable
out    CD=1e-6    fails on    381 of 200000  (0.19%)
       CD=1e-4    fails on  31200 of 200000  (16%)
       CD=3.7e-6  fails on  47945 of 200000  (24%)
       The constant does NOT divide out. IEEE 754 division is a second rounding.
```

It is not a hypothetical. One entry of my sixteenth-round corpus -- an admissible
member, nothing exotic -- reddens it at the shipped `CD`:

```
cmd    python -m pytest -q -k CALIBRATED     (with my corpus, 99 solved)
out    AssertionError: br2_floor_thick_iy1e6_L1000: the counter-defect injection
       measures 9.9999999999999974e-07 ... against its declared size
       9.9999999999999995e-07. The measure and the claim are no longer in the
       same units.
       assert 9.999999999999997e-07 == 1e-06
```

One unit in the last place. The measure and the claim are in **exactly** the same
units; the message sends the next reader after a units bug that does not exist.
And the green at `9b866ce` is 89 draws at `p = 0.0019` -- about a one-in-seven
chance of having been red at the commit that published it, which is a property
the stated mechanism denies can exist. The previous form,
`assert_close(1 + measured, 1 + CD, ROUNDOFF_IDENTITY, ...)`, was correct and was
replaced by a tightening the arithmetic does not support.

This is the recorded rule on exactness tolerances, in its own words: an exactness
tolerance is a small ULP multiple justified by the recorded measurements, and the
record says so. **Closed when** the assertion admits the one-ULP band the division
actually has, with the measurement above or one like it as its justification, and
the message says what a failure would mean.

**R143. (blocking) R139 stands, and the exemption it describes went from 0 pairs
to 15 in this range.** `test_corpus_configurations.py:1021-1027`, `:1231`.

```
cmd  python -m pytest -q -s <the corpus runner> -k REPORTED
out  ... dropped_shear_pa ...  shear_edge_iso_L4000       0.8806   <- exempted
                               every_state_edge_iso_L85     2956   <- exempted
     (same column, same format, no marker; no line anywhere gives the number of
      exempted pairs)
     dropped_shear_parameter minimum 0.0006932x at shear_defect_live_thin_L1990
```

The printed minimum for `dropped_shear_parameter` is `0.0006932x` -- a number
below the ceiling, published in a margin table, with nothing saying that this
pair was exempted rather than asserted. A reader of that table cannot tell which
of the 89 pairs the gate held to the ceiling. **Closed when** the classification
appears in the printed row and the count of exempted pairs is printed.

**R144. (blocking) Nine of the fifteen exempted pairs are detected -- one by
2956x -- so the exemption drops assertions that pass, and nothing records that it
did.** `test_corpus_configurations.py:1021-1027`.

```
rule  exempted iff injected_delta < CD; the branch returns before `worst` is
      computed, so the response is never asserted
cell  compute the response anyway for all 15 exempted pairs, nothing else moved
out   every_state_edge_iso_L85   eff/CD 0.388     response 2956x   DETECTED
      every_state_edge_iso_L90   eff/CD 0.309     response 2352x   DETECTED
      unit_milli_lam2885         eff/CD 0.228     response 1739x   DETECTED
      plan_headline_lam2885      eff/CD 0.228     response 1739x   DETECTED
      unit_kilo_lam2885          eff/CD 0.228     response 1739x   DETECTED
      shear_edge_thick_L4000     eff/CD 0.00164   response 12.5x   DETECTED
      shear_edge_thin_L200       eff/CD 0.00089   response 6.80x   DETECTED
      shear_edge_iso_L3000       eff/CD 0.00037   response 2.78x   DETECTED
      shear_edge_iso_L4000_skew  eff/CD 0.000116  response 1.07x   DETECTED
      -- 6 others genuinely below the ceiling
      9 of 15 exempted pairs would have PASSED the assertion that was skipped
```

My corpus makes the tightest case available: `boundary_exempt_detected_L420` sits
at `eff/CD = 0.9495` -- five per cent under the declared resolution -- and the gate
detects it by `7245x`. The gate is being told to stop looking at a case where it
works by four orders. The day the element regresses there, nothing goes red,
because the response is never computed.

The fix is one predicate and needs no new constant: exempt only when the pair is
below resolution **and** the response is at or below the ceiling; assert red
otherwise. That is not a measured per-entry resolution (R56's species) -- the
resolution stays the declared constant; it is a refusal to drop an assertion that
would pass. **Closed when** an exempted pair whose response exceeds the ceiling is
asserted red, or the report states the count and says why the assertions are
dropped anyway.

**R145. (blocking) The one property that makes `injected_delta` "the residual's
norm" -- the homogeneous scaling -- is asserted by nothing, and the test cited for
it cannot see it. Provenance, not existence.**
`test_corpus_configurations.py:877-887` (`_homogeneous`), `:915-916`, `:1050-1065`.

```
claim  "The same scaling `interior_out_of_balance` applies before it takes a
        norm, so a defect measured through here is measured in the units the
        gate decides in."                                       -- :883-885
       "`test_the_delta_measure_is_CALIBRATED` pins it in both directions."
cell   ell := 1.0 (no scaling at all), the one variable moved, full suite
out    3 failed, 944 passed -- and test_the_delta_measure_is_CALIBRATED is GREEN
cell   ell := 10 x member length, one variable moved, full suite
out    947 passed
cell   ell := 1000 x member length, one variable moved, full suite
out    947 passed   (fails first at 1e5, via the no-op control, not via CALIBRATED)
```

The calibration is blind to it by the same algebra it is justified with: for a
whole-element injection the scaling cancels, so `==` holds for any `ell`
whatsoever. The bending-only control is blind too -- with no scaling at all it
still gives `stub 0.558 > slender 0.173` and `stub < 1`, so both of its
assertions pass.

I measured the harm before recording it, and it is currently zero: inflating
`ell` by `1000x` changes the classification of **28 of 356 pairs**, and all 28
are in `UNCONDITIONALLY_RED`, where the classification is bypassed -- the shear
exemption stays at exactly 15 of 89 across `1x`, `10x` and `1000x`. So this is a
provenance finding, not a live hole: the claim that the metric is in the
residual's units is true (I read `interior_out_of_balance` and confirmed
`char_length = float(stations[-1])` on both sides) and is believed on reading
rather than on a check. **Closed when** something reddens if `_homogeneous` stops
using the residual's characteristic length -- a bending-only ratio compared against
a value that depends on it will do, since that is the direction where it does not
cancel -- or the report says plainly that nothing does.

Two smaller things measured in the same place, recorded rather than made
findings: `injected_delta` takes its norm on the local, unassembled element
matrix while the residual takes its on the assembled global one, and over 160
pairs the two differ by `1.03x` to `7.33x`; and the calibration's bending-only
half checks only the two extreme entries, which is honest but is not the
corpus-wide `< 1` the prose states -- I measured it over all 89 and the maximum is
`0.193`, at the stubbiest, so the prose happens to hold.

**R146. (recordable) The bending-only table is indexed by a variable it is not a
function of, in the section whose finding is that that variable was never the
variable -- and it is published in the locked plan, which nothing regenerates.**
`docs/milestones/F2.md:610-613`; report sec. 2; `d920a8d`.

```
published   L/r_min       6      47      65     233     389    2527   23084
            bending-only  0.193  0.0450  0.0258 2.28e-3 8.22e-4 1.95e-5 2.34e-7
cmd         the same measure over every solved entry at each of those L/r_min
out         lam 47:  9.722e-05, 0.04495, 0.04566   over 20 entries  -- 470x spread
            lam 65:  0.02578 .. 0.1251             over  6 entries  --  4.8x spread
```

Every published cell reproduces; the table is not wrong. What it is, is a
one-to-one presentation of a relation that is one-to-many by a factor of 470 at
its second column, three lines under the sentence "the variable was never a
slenderness". The most slender solved entry (`L/r_min = 192370`) has ratio
`3.369e-07`, larger than the `2.34e-07` the table's last column shows at
`23084`, so "that ratio falls with slenderness" does not hold monotonically
either -- 16 adjacent pairs in the sorted list rise.

And it is in `F2.md`. BI3's rule -- a table is regenerated by a script at the
commit it describes, or it lives in the step report, which is regenerated by rule
-- was written about `tolerances.py`, and the plan is a stronger case of the same
thing: it is locked, so it is the one artifact that is never regenerated by
anything. This is the standing question I closed the fifteenth verdict with,
answered in the wrong direction. **Closed when** the table is in the report with a
pointer from the plan, or the plan's row names the entry each cell was measured
at.

**R147. (recordable) BR2's `4447x` is a property of the corpus, and it is not
measured at the point the rule decides.** `F2.md:621-623`; report sec. 3.

```
claim  "response/ceiling divided by effective/CD spans 4447x .. 4.263e+08x. The
        claim needs only the smaller end, and 4447x is the margin the rule stands
        on."
cmd    the same ratio over a 3045-live-pair sweep (D in 0.05/0.6/3.0,
       t in 0.001/0.012/0.15, L in 8 values, 3 orientations, 5 extras)
out    minimum 3999x at D=3.000 t=0.15000 L=1000 axis I_y/I_z=1e6;
       103 pairs below 4447x
```

The bound is sound -- the minimum ratio is a valid lower bound on the response at
the boundary -- so BR2 is not refuted, and I say so. What is wrong is the
operating point. `4447x` is the minimum over pairs whose `effective/CD` spans
nine orders; the rule decides at `effective/CD = 1`, and nothing in the shipped
corpus is within three orders of that. I solved it:

```
cmd   bisect L for effective(dropped_shear_parameter) = CD exactly, L the only
      variable moved, 46 steps
out   iso   D=0.600 t=0.01200  L* = 414.6   L/r_min 1994   response 7630x ceiling
      thin  D=0.050 t=0.00100  L* =  34.6   L/r_min 1847   response 7633x
      thick D=0.600 t=0.15000  L* = 334.4   L/r_min 1848   response 7633x
```

`7630x`, not `4447x`, and the same to three digits in three section families --
which is a stronger result than the one published. My corpus now carries entries
on both sides of that crossing and one on it. **Closed when** the margin is quoted
at the boundary as well as as a bound, per "a ratio carries its operating point".

**R148. (recordable) `K_bend/K_max ~ 12/lambda_elem^2` is stated as a general law
and is wrong by more than `2x` on 15 of 89 entries.**
`test_corpus_configurations.py:962-971` (`UNCONDITIONALLY_RED`'s comment);
`F2.md:635-638`; report sec. 4.

```
claim  "K_bend/K_max ~ 12/lambda_elem^2 shrinks any bending-block defect however
        structural it is"
cmd    measured / predicted, over all 89 solved entries
out    median 0.993, min 0.002, max 7.8e+05
       15 of 89 outside [0.5, 2.0] -- every one anisotropic
```

On the 19 pairs the sentence is used to explain, it is good: `0.589` or `1.18` on
18 of them. As a general law about "any bending-block defect" it fails by five
orders when `I_y != I_z`, because `lambda` is built on `r_min` while the block the
measure perturbs is fixed at `x-y`. My `aniso_bend_block_is_largest` is the case:
same `L/r_min` as `shear_edge_iso_L4000`, where `dropped_flip` measures `0.397 CD`
and is one of the 19, and here it measures `4.013e+04 CD` -- so "the most slender
entries" is not what selects the 19 either. **Closed when** the sentence is scoped
to the isotropic case it holds in, or restated as the bound it is.

**R149. (recordable) The locked plan was edited inside the step commit.**
`a634970` touches `docs/milestones/F2.md:1407-1412` and
`tests/verification/rung1/`, `tests/test_plan_matches_tolerances.py`.

The change is a good one -- it converts a stale value into an explicit record of a
superseded decision -- it is disclosed at length in the commit message, and it was
forced by the new test on its first run, which is the mechanism working. It is
still a locked-plan edit in a commit that also touches `tests/`, one commit after
a STOP whose subject was the plan being adapted without a reopen. `CLAUDE.md`
makes this STOP-class for `.claude/` and `docs/SUPERVISOR.md` and not for the
plan, which is why this is recordable and not a STOP. **Closed when** the next
plan edit, however small, is its own commit.

**R150. (recordable) `test_plan_matches_tolerances.py` covers 5 of the 11
tolerance names the plan mentions, and `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` --
one of the two constants in the move it was built to stop -- is not one of them.**
`tests/test_plan_matches_tolerances.py:38-41`.

```
cmd   python -m pytest tests/test_plan_matches_tolerances.py -q --collect-only
out   564-PATCH_TEST_COUNTER_HEADROOM-6.0e7,
      887-PANEL_RECONSTRUCTION_RESIDUAL_COUNTER-1.0e-5,
      1290-RESULTANT_EXACTNESS-1e-9, 1292-RESULTANT_EXACTNESS_COUNTER-6.8e-7,
      1412-PATCH_TEST_EXACTNESS-5e-15                          -- 5 rows
cmd   tolerance names the plan mentions but never in NAME = value form
out   PATCH_TEST_EXACTNESS_COUNTER_DEFECT, DEAD_DOF_RELATIVE_FLOOR,
      INTERPOLATED_REFERENCE_TOLERANCE_FLOOR, MEMBER_ORIENTATION_DEGENERACY,
      PANEL_RECONSTRUCTION_RESIDUAL, SUBDIVISION_INVARIANCE
```

The regex requires name and value on one line with an `=` between them.
`F2.md:546` states the counter-defect's value as "could be raised from `1e-6` to
`1e+6`", which no pattern of this shape can see, so the plan can state a value in
a form the test does not match -- that is the hole, and the constant this whole
round is about is in it. It is separately guarded by
`test_the_counter_DEFECT_SIZE_cannot_be_raised` (I checked: moving it alone to
`1e-4` gives `2 failed`), so nothing is unguarded; the finding is that the new
test's reach is narrower than the sentence "every constant named in this file
carries the value `tolerances.py` ships" at `F2.md:576`.

The meta-test does fire -- I broke it three ways: a pattern matching nothing gives
"no tolerance value was found in the plan"; a pattern matching two names gives
"only [...] matched"; the shipped pattern gives 5 rows and passes. Its floor of
`>= 3` has two names of headroom against the five it finds. **Closed when**
`F2.md:576` says what the test checks (values stated as `NAME = value`), or the
plan states the counter-defect in a form the test reads.

**R151. (recordable) Three counts in the report and commit messages do not match
the repository.** report opening, sec. 6; `9b866ce` and `a634970` commit messages.

```
claim  "947 passed on the reviewer's 105-entry corpus"
cmd    python -m pytest -q -s <the corpus runner> -k corpus
out    corpus: 113 entries executed by this module ... 89 solved, 24 refused,
       113 total          (113 is the number written in the verdict this report
       answers)

claim  "All eight (1 + size) - 1 sites in test_patch_test.py"
cmd    grep -c "defect_size=" tests/verification/rung1/test_patch_test.py
out    7   (7 call sites reaching 2 application lines, :455 and :470)

claim  "so there is one convention rather than two"
cmd    grep -rn "scale - 1.0" tests/ --include=*.py
out    tests/unit/test_assembly_and_solve.py:223   k[d[i], d[j]] += (scale - 1.0)
       * kb[i, j]      with scale looped over (1.0, 1.0 + eps), eps = 1.0e-7
```

The third site is harmless numerically -- at `eps = 1e-7` the quantisation is
`2.2e-09` relative -- and it is outside the module the sentence scopes itself to.
It is listed because "one convention rather than two" is a claim about the
repository and there are two.

**R152. (recordable) Two sentences about the guards behind the exemption are
false in the vocabulary this range introduced.**
`test_corpus_configurations.py:1022-1024`, `:1145-1146`.

```
claim  "test_every_entry_carries_at_least_one_LIVE_defect refuses an entry whose
        every defect lands here [below resolution]"              -- :1023-1024
rule   that test's predicate is injected_delta(entry, k) > 0.0, not
       >= PATCH_TEST_EXACTNESS_COUNTER_DEFECT
out    the two senses of "live" are different; an entry with all four defects
       below resolution and all four non-zero passes it

claim  "Measured at this commit: every one of the four defects is live on every
        solved entry"                                            -- :1145-1146
cmd    count pairs with injected_delta < CD
out    34 of 356  (19 structural + 15 shear)
```

Both were true at `7daffed` and were made false by BR1, which is the species this
milestone keeps meeting: a sentence that was right when written and is wrong when
read. Nothing is unguarded -- `UNCONDITIONALLY_RED` means the three structural
defects cannot be exempted whatever `classify` says -- so this is wording.
**Closed when** the two senses of "live" are distinguished, or the claim about
what that test refuses is removed.

## Tolerances touched

**None.** `git diff 5e923a3..9b866ce -- floatfea/tolerances.py` is empty; `git
diff --stat 5e923a3..9b866ce -- floatfea` is empty. No golden file moved
(`tests/regression` empty in the range), no `expect` field on any corpus line
changed, `grep -rn "xfail|pytest.skip" tests/` returns nothing.

The one thing in this round that behaves like a tolerance and is not one is
`_homogeneous`'s `ell` (**R145**): it can be inflated `1000x` with the suite green
and it changes the classification of 28 of 356 pairs. I measured that it moves no
decision on this corpus -- all 28 are in `UNCONDITIONALLY_RED` -- and record it as
provenance rather than as a hidden tolerance.

I re-derived every published figure independently. `4447x`, `4.263e+08x`,
`19 pairs`, `2.838e+05x`, `1.114e+08x`, `15 of 89`, `1.1566e-10`, `5.5780e-11`,
`1.0262e-10`, `0.8806x`, `0.4247x`, `0.7813x`, all seven bending-only cells, and
the `==` on all 89 shipped entries -- **all reproduce**. `105-entry corpus`,
`eight sites`, `0 of 74`, `minimum margin 1739x`, `3.9413e-14` and `2.537e+07`
do not.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a HOLD, not a STOP: rung
1 is green at `9b866ce`, the plan was reopened in its own commit before the code,
and R130 -- the hard one -- is closed. **BR4 is not triggered.** BR1 and BR2 are
not refuted and should not be removed: I could not find a live pair that fails to
redden in 3045, the boundary is family-independent at `L/r_min ~ 1994` with
`7630x` of margin, and the classification is unit-invariant to six digits across
`10^6` of length unit, which is a stronger result than anything published for it.

1. **R140 -- the carry.** R129-R139 by number, with a status each. This is first
   because it is the mechanism, not the content.
2. **R141 -- R129's two remaining sites**, `F2.md:531` and `:534-542`, whose three
   figures the shipped runner refutes at this commit.
3. **R142 -- the `==` calibration.** It is not exact by algebra, it reddens on a
   legitimate entry at the shipped counter-defect size, and its message
   misdiagnoses. This is the one defect in the part the round called load-bearing.
4. **R143, R144 -- the exemption.** Printed unmarked and uncounted; and 9 of its
   15 pairs are detected, one by `2956x`, with the assertion dropped anyway.
5. **R145 -- the homogeneous scaling has no guard**, and the test cited for it
   cannot have one by construction.
6. **R146-R148 -- three published relations** stated more generally than they
   hold: a table indexed by a variable it is not a function of, a ratio away from
   its operating point, and a law that fails by five orders off the isotropic case.
7. **R132, R133, R136, R137 -- untouched from the fifteenth verdict.**
8. **R149, R150, R151, R152 -- recordable**, answerable in prose or one line each.
9. **R113, R95, R97, R98, R100-R103, R63, R76, R79, R80 -- carried, unchanged.**

**Adversarial corpus (BE3): 10 new entries committed, all unseen by the
implementer; 1 red at `9b866ce`, 9 green, every outcome measured before the line
was written.** `tests/corpus/g22_model_configurations.txt`, now **123** entries,
99 solved, committed separately at `77b1ad4` immediately before this verdict and
touching no code. Full suite with the corpus applied: **996 passed, 1 failed.**

The coverage measurement, stated plainly: **the implementer's rule decides at
`effective = CD`, and no shipped corpus entry was within three orders of that
crossing.** The published tightness was measured over pairs spanning nine orders
of defect size and quoted as if it were the margin at the decision point; it is
not, and the real one is `1.7x` better. Three of my entries now straddle the
crossing and one sits on it at `eff/CD = 0.999928`. Two more put the same member
at the crossing in a `10^6` range of length unit and find the classification
identical to six digits -- the strongest positive result of the round, and one the
report does not claim. One entry reddens the calibration by a single ULP, which is
R142 and was predicted from the arithmetic before it was run.

**Sixteen consecutive rounds have found no element defect**, and the reading is
unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side. Five
of the five defective instruments this milestone have been tests, and the sixth is
R142 -- a `==` in a calibration, on an element that is fine.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass.
Sixteen consecutive reviews by one reader.

**The standing question for the next round:** every one of R142, R145, R146, R147
and R148 is a true measurement wearing a claim one size too large -- an exact
comparison whose exactness is luck, a norm believed to be the residual's because
it is written down next to one, a table read as a function, a ratio read at the
wrong point, a fit read as a law. The numbers are all correct. **For every figure
in this round, what is the smallest change to the corpus or the constants that
would make the sentence around it false -- and has that change been tried?**
