# Review — F2 step 4
Reviewed commit: f66e4e0f1571b72af8040ee74787ecd09a7f8397
Verdict: HOLD
Tests: 1028 passed, 0 failed, 0 skipped   (my run at `e8920b8`, `python -m pytest -q`,
35.23s. With my seventeenth-round corpus applied at `f66e4e0`: **1077 passed, 1 failed**.)

**Reviewed code commit: `6c1e834`; process `f9c64fc`; plan `253ee7a`; report `e8920b8`.**
The header stamp is `f66e4e0`, my own corpus commit, made immediately before this
verdict and touching no code.

Seventeenth pass. Range `4631c18..e8920b8`, four commits.

```
cmd  git diff 4631c18..e8920b8 -- .claude docs/SUPERVISOR.md
out  one hunk, +24 lines, 0 deletions, in .claude/hooks/require-verdict.sh
cmd  git show --stat f9c64fc
out  process: BS0 ...  .claude/hooks/require-verdict.sh | scripts/check_carried.py
     (no floatfea/, no tests/)
cmd  git log --oneline 4631c18..e8920b8 -- CLAUDE.md
out  (nothing)
```

**The instruction change is correctly routed.** It is a standalone `process:`
commit, it cites its directive in the message, it touches no `floatfea/` and no
`tests/`, and I read all 24 added lines: nothing is deleted and no guard is
weakened. That is the shape CLAUDE.md sec. "The reviewer's own instructions are
not edited inside a step" asks for, and it is the first time this milestone it has
been met on the first try. **R149 is closed by not repeating it**: `253ee7a` is
plan-only and `6c1e834` is code-only.

```
cmd  git diff 4631c18..e8920b8 -- floatfea/tolerances.py ; git diff --stat ... -- floatfea
out  (empty) ; (empty)
cmd  grep -rn "xfail|pytest.skip|@pytest.mark.skip" tests/ --include=*.py
out  (nothing)
cmd  git diff --stat 4631c18..e8920b8 -- tests/regression
out  2 files changed, 146 insertions  (both NEW files; no golden value moved)
```

No production code, no tolerance, no `expect` field and no existing golden value
moved in this range. No commit touches both `floatfea/` and `docs/reviews/`.

**Three of this round's four substantive moves are right, and I checked each by
breaking it rather than by reading it.** `classify`'s ULP floor is necessary and in
the safe direction; BS3's control is genuine on three mutants; BS2's golden file
binds in both directions and caught five of my eleven unseen entries; and sec. 5's
refusal to make the normalisation change the directive asked for is a correct
measurement that I reproduced to four digits. Details under **What held**.

This is a HOLD for four things: a guard added this round that cannot run, two items
recorded closed that are closed at part, and an allowance whose record is 47x
smaller than the allowance.

## Carried

Every item from the sixteenth verdict (`HOLD @ 9b866ce`, committed `4631c18`),
re-measured at `e8920b8`, plus the older carry. **The report carries all thirteen by
number in a table (sec. 7)** -- R140's condition met -- and I checked each status
against the repository rather than accepting it.

- **R140 (blocking) -- CLOSED AS AN ITEM, AND ITS MECHANISM DOES NOT RUN.** Sec. 7
  lists R140-R152 with a status each, and lists R129-R139. That is the condition.
  The script it points at is **R153**.
- **R141 (blocking) -- CLOSED AT TWO SITES OF THREE.** `:538`'s three figures are
  regenerated and `:542`'s sentence is gone. `F2.md:531` is byte-identical and
  sec. 6 does not mention it. Recorded "closed". See **R155**.
- **R142 (blocking) -- CLOSED ON THE `==`, OPEN ON THE BAND.** The `==` is gone, the
  withdrawn argument is stated at the site, and `classify` carries the same
  allowance -- I confirmed the exempt count `41 -> 40` by ablation, and the extra
  pair under the bare `>=` is `one_element_scaled 1`, the gate's own counter-defect.
  The allowance is 47.2 ULP where three sentences say one. See **R156**.
- **R143 (blocking) -- CLOSED ON THE COUNT, OPEN ON THE ROW.** My condition named two
  things. The count is printed. The row is not marked. Recorded "marked and
  counted". See **R154**.
- **R144 (blocking) -- CLOSED, AND MY PROPOSED FIX IS WITHDRAWN BY ME.** The site's
  argument is correct: asserting "red wherever the response exceeds the ceiling
  regardless of classification" is the predicate and the outcome in one number,
  which is R137's own species. The golden file is a better answer than the one I
  asked for. Its premise covers 14 of its 34 rows -- **R158**.
- **R145 (blocking) -- CLOSED, and it is the strongest work in the round.** Three
  mutants: `ell -> 1.0` reddens `test_the_delta_measure_is_UNIT_INVARIANT`;
  `ell -> 1000*ell` leaves all four green, which is the docstring's own claim; and
  making the control's `globals()` patch a no-op reddens the control itself, so it
  cannot pass while measuring the unpatched function. The new causal sentence beside
  it is **R159**.
- **R146 (recordable) -- CLOSED.** Re-indexed by `K_bend/K_max`, which it is a
  function of, and the `470x` spread is stated.
- **R147 (recordable) -- OPEN.** Answered with a figure measured under the one defect
  kind whose operating point is an identity. See **R157**.
- **R148 (recordable) -- OPEN, declared.** `12/lambda_elem^2` still stated as a
  general law at `test_corpus_configurations.py:985` and `F2.md:662`.
- **R149 (recordable) -- CLOSED by not repeating it.** Verified above.
- **R150 (recordable) -- CLOSED on its condition, with a new hole.** All 25 declared
  tolerances are bound: `_stated_in_plan()` gives 30 rows, 25 distinct names, and
  `set(_declared()) - names` is empty. The direction not checked is **R161**.
- **R151 (recordable) -- OPEN, declared.** `105-entry corpus` at report `:2487`,
  `All eight ... sites` at `:2592`.
- **R152 (recordable) -- OPEN, declared.** `:1041` and `:1229` unchanged.
- **R129 -- OPEN AT ONE SITE.** Folded into R141/R155 above.
- **R130 -- CLOSED** (fifteenth verdict). **R131 -- CLOSED** (sixteenth verdict).
- **R132 (blocking) -- OPEN, UNTOUCHED, AND NOW WIDER BY A THIRD FIELD.**
  `tolerances.py:492-493` says `3.9413e-14 at band_edge_isotropic_bracing` and
  `2.537e+07x`; the shipped runner prints `detection edge 3.9459e-14 at
  aaa_band_edge_twin ... 2.534e+07x`. The named entry is now wrong too.
- **R133 (blocking, fifteenth verdict) -- OPEN, UNTOUCHED, and now self-contradicted
  inside its own file.** `test_corpus_configurations.py:519-526` still states the
  causal chain I refuted with a controlled revert, and says the arithmetic "put the
  gate's OWN counter-defect below its own resolution **on every entry**". The
  comment this round added at `:1074-1076` says a bare `>=` did it "on **one** of
  them" -- and my ablation says one. Two comments in one file, 550 lines apart, give
  incompatible counts for the same phenomenon. This item was listed in my sixteenth
  verdict's opening conditions and is a HOLD on its own.
- **R134 (recordable) -- OPEN.** "nine orders" for `9.881e+06` stands.
- **R135 (recordable) -- OPEN AND WIDER.** `74 -> 81 -> 89 -> 99` solved.
- **R136 (recordable) -- OPEN, UNTOUCHED, AND NOW A DISAGREEMENT THIS ROUND CREATED.**
  `tolerances.py:459` says `8.701e+06x ... at L/r_min = 558`. Folded into **R155**.
- **R137 (recordable) -- OPEN, UNTOUCHED, AND STILL A TAUTOLOGY AFTER THE ULP FIX.**
  `:1046` asserts `delta < PATCH_TEST_EXACTNESS_COUNTER_DEFECT` one line below a
  branch whose condition is now `delta < CD*(1 - 1e-14)`, which implies it.
- **R138 (recordable) -- CLOSED** (sixteenth verdict).
- **R139 (blocking) -- CLOSED** by R143/R144's work.
- **R113 -- OPEN, correctly declared.** `_section(entry` at `:443`, `:562`.
- **R95 -- OPEN, correctly declared.** `pytest.raises(ValueError)` with no `match` at
  `:738`.
- **R97 -- OPEN.** `never asserted at a constant` at `F2.md:808`, `:1565`.
- **R98 -- OPEN.** `INADMISSIBLE`, four occurrences, none an assertion.
- **R100 -- PARTLY ANSWERED.** `ls scripts/` is now `check_carried.py
  write_verdict.py`. Still no regeneration script; the plan's new tolerance table
  says "**Regenerated** from `floatfea/tolerances.py`" and nothing regenerates it --
  but it is *asserted* by a test on all 25 names, which is stronger than a script. I
  record that as the better answer with the word "regenerated" unearned.
- **R101, R102, R103 -- OPEN.** `grep -n "revision 1" floatfea/tolerances.py` gives
  `:189` and `:624`, both "revision 10".
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.**
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, routed to
  step 4a or later.
- **R115-R128 -- closed at the fourteenth and fifteenth verdicts.**
- **R68's standard -- MET.** Revision 17 sec. 4 records the round's own error -- the
  control that patched a second module object and passed for the wrong reason --
  without being asked. First time in three rounds.

## Findings

**R153. (blocking) The guard written to make the carry mechanical cannot run. The
branch that invokes `scripts/check_carried.py` is unreachable from the Stop hook,
in both directions, by construction.** `.claude/hooks/require-verdict.sh:79`, `:97-106`.

```
claim  "That is now a build failure: ... the Stop hook refuses to end a turn on a
        difference."                                        -- report sec. 1
cmd    echo '{"stop_hook_active":false}' | bash .claude/hooks/require-verdict.sh
out    {"decision":"block","reason":"floatfea/, tests/, or docs/reports/F2/step-4.md
        changed since the verdict at 77b1ad4... Re-invoke the gating-supervisor"}
       -- line 81. check_carried.py did not run.
```

It is not a timing accident, it is the branch algebra. Line 79 blocks and exits
whenever `git diff --quiet "$reviewed" -- "$report" floatfea tests` is non-clean.
Line 98 skips whenever `git diff --quiet "$reviewed" -- "$report"` **is** clean. The
report is inside the first pathspec, so a dirty report implies line 79 fires first,
and a clean report implies line 98 skips. There is no state in between:

```
cell  the two --quiet diffs the hook runs, at two hypothetical reviewed commits
out   reviewed=e8920b8 (report clean):  line79 blocks? no   BS0 check runs? NO
      reviewed=6c1e834 (report dirty):  line79 blocks? YES  BS0 check runs? NO
```

The script itself is sound and its meta-check fires -- zero parsed findings is a
failure, not a pass, and I confirmed the exit-1 path. What does not exist is the
mechanism. The report's evidence for it is a manual `python
scripts/check_carried.py`, which is the implementer running it by attention, which
is the thing BS0 was written to stop depending on.

Two further reaches it does not have, recorded so it is not trusted past them.
**(a)** It enforces only the *newest verdict's* `**R<n>.` headings. R132, R133, R136
and R137 are carried in my `Carried` section, not as findings, so the script would
pass a report that dropped all four -- which is exactly the omission class it was
built for, and four of those items are open right now. **(b)** Its parse is
all-or-nothing: a verdict whose heading reads `**R153 (blocking)` rather than
`**R153.` contributes nothing and the meta-check stays silent as long as one other
heading matches. I also confirmed that a `Carried` section which is nothing but the
comma-separated identifiers passes (declared), and that with two headings matching
`.*Carried.*` it reads the **last** one.

**Closed when** the hook actually runs the check on the state it is meant to guard
-- the natural place is inside line 79's failure path, since that is the state in
which the report has been reworked -- and the demonstration is the hook invoked at a
commit where a finding is missing, with the blocking JSON pasted.

**R154. (blocking) R143 is recorded closed as "marked and counted". The count is
printed; the row is not marked, and the row is the half the finding was about.**
`test_corpus_configurations.py:1422-1440`; report sec. 3 and sec. 7.

```
claim  "| R143 | closed -- sec.3, marked and counted |"      -- report sec. 7
cmd    python -m pytest -q -s <the corpus runner> -k REPORTED
out    EXEMPT  40 of 396 (entry, defect) pairs ...            <- the count, new
       MARGINS ...
         dropped_shear_parameter minimum 0.0006932x at shear_defect_live_thin_L1990
                                                              <- unchanged, unmarked
```

`0.0006932x` is a number below the ceiling published in a margins table, and that
pair is exempt-and-not-detected -- one of the six. Nothing on the row says so. My
condition read "Closed when the classification appears in the printed row **and**
the count of exempted pairs is printed"; the second conjunct is done and the first
is not, and the report records the item closed.

This is the **third consecutive round** in which a closing condition that named
sites was closed at some of them and recorded as answered -- R129 at three of five,
R141 at two of three (**R155**), R143 at one of two. CLAUDE.md sec. "A closing
condition that names sites is closed site by site" was written for this after the
first occurrence. **Closed when** the row carries the classification, or the report
says the row was left and why.

**R155. (blocking) R141's third site is untouched; the plan's own detection table
fifteen lines above the paragraph this round added about a stale figure is refuted
by four orders; and this round's plan edit created a disagreement between `F2.md`
and `tolerances.py` on one measure that now has two published values.**
`docs/milestones/F2.md:507-522`, `:531`, `:642`, `:695`, `:713`;
`floatfea/tolerances.py:459`.

```
plan :509      "Worst over the 90-entry corpus 0.0887x"
plan :513-518  dropped flip           5.150e+09x   L/r_min 2332
               one wrong DOF index    5.227e+09x   L/r_min 1058
               one element x (1+1e-6) 8.701e+06x   L/r_min  558
plan :520      "Zero entries fail to redden"
cmd            python -m pytest -q -s <the corpus runner> -k REPORTED
out            dropped_flip            minimum 6.264e+05x at shear_edge_L4000_aniso_weak
               wrong_dof_index         minimum 2.838e+05x at shear_defect_exempt_L2500
               one_element_scaled      minimum 8.698e+06x at br2_floor_thick_iy1e6_L1000
               dropped_shear_parameter minimum 0.0006932x  (6 of 99 at or below the ceiling)
               123 entries, 99 solved; worst clean 0.0887x   <- the only one that holds
```

Two of the three rows are wrong by **four orders**, the third by 3e-4 and at the
wrong entry, "zero entries fail to redden" is refuted by the fourth defect kind, and
"90-entry" is two corpus rounds stale. `git diff 4631c18..e8920b8 --
docs/milestones/F2.md` does not touch any of it. The paragraph added at `:534-542`
in this very range says "AND THE FIGURE THAT REPLACED IT WENT STALE THE SAME WAY" --
the round diagnosed the species correctly and regenerated one instance of it fifteen
lines below four more.

The `8.701e+06x` figure appears at `F2.md:517`, `:695`, `:713`, at
`tolerances.py:459`, and -- regenerated to `8.698e+06x` this round -- at `F2.md:642`.
A reader of the locked plan now finds two different values for the same measure, and
`tolerances.py:459` additionally names `L/r_min = 558` where the runner names
`L/r_min 991.1`. `test_plan_matches_tolerances.py` cannot see any of it: these are
prose, and its own docstring says so correctly.

And `F2.md:531` -- R141's third named site -- is byte-identical.

**Closed when** each of `:509`, `:513-518`, `:520`, `:531` and the four remaining
`8.701e+06x` sites is regenerated or stated as left with a reason, site by site; or
the figures move out of the locked plan into the report, which is regenerated by
rule, with a pointer left behind -- BI3's own remedy applied to the one artifact
nothing regenerates.

**R156. (blocking) The allowance that replaced the `==` is 47.2 ULP. The code
comment, the assertion message and the report all say one ULP, and no measurement of
the actual band was taken.** `test_corpus_configurations.py:1074-1092`, `:963-966`;
report sec. 2.

```
claim  "TO ONE ULP, NOT EXACTLY"                            -- :1074
claim  "Within one ULP this is rounding"                    -- :1089, the message
claim  "the message says one ULP"                           -- report sec. 2
code   assert_close(measured, CD, ROUNDOFF_IDENTITY, floor=eps*CD)
cmd    tol*scale / ulp(CD),  ROUNDOFF_IDENTITY = 1e-14, CD = 1e-6
out    1e-14 * 1e-6 = 1e-20 ;  1 ULP of 1e-6 = 2.1176e-22  ->  47.22 ULP
       (the `floor` is the vacuity guard only: assert_close fails on
        diff > tol*scale and never adds the floor. 100*floor = 2.2e-20 << 1e-6,
        so the floor is inert here.)
cell   |injected_delta(e,"one_element_scaled") - CD| / ulp, one variable moved
out    99 shipped entries      max 1.000 ULP  (98 exact, 1 at -1)
       372 grid configurations max 1.000 ULP
       360 random admissible   max 1.000 ULP
       831 configurations, largest deviation observed: exactly 1 ULP
```

The measurement supports 1-2 ULP; the code admits 47. `ROUNDOFF_IDENTITY` is a
CLASS: ACCURACY entry carrying `ROUNDOFF_IDENTITY_COUNTER = 1e-8` in a different
quantity -- an engineering number reached for where the recorded rule asks for "a
small ULP multiple justified by the recorded measurements, and the record says so,
so a later reader does not reach for an engineering number".

**I measured the harm and it is zero on everything I can construct** -- nothing
realistic perturbs this ratio by `1e-14` relative and not by orders -- so this is a
finding about the record, not a hole. It is blocking because it sits in the one part
of the round the report calls load-bearing, because it is precisely R142's unclosed
half (the **one-ULP** band the division actually has, "with the measurement above or
one like it as its justification"), and because a 47x-too-large exactness tolerance
is how the next one gets set. **Closed when** either the band matches the
measurement or the three sentences match the band, with the ULP sweep recorded.

**R157. (blocking) R147's operating-point margin is measured under the one defect
kind whose operating point is an identity rather than a selection. Measured where
the rule binds it is `7630.2x`, not `8.698e+06x` -- and it is the same to five
digits across nine section families.** `docs/milestones/F2.md:634-648`; report sec. 6.

```
claim  "At the corpus pair sitting closest to the boundary the rule decides
        (effective = 1.0000 x CD, the same entry under one_element_scaled) the
        margin is 8.698e+06x ... how much room does the rule have where it is
        actually tight."                                     -- F2.md:638-643
rule   injected_delta(e,"one_element_scaled") == CD on EVERY solved entry, by
       construction -- that is what test_the_delta_measure_is_CALIBRATED asserts
cmd    pairs within [0.9, 1.1] x CD, per defect kind, weakest response
out    one_element_scaled       99 pairs   weakest 8.698e+06x   <- published
       dropped_shear_parameter   4 pairs   weakest    7245x     <- binds
       (boundary_on_the_edge_L414p6 at eff/CD 0.999928 -> 9267x;
        boundary_exempt_detected_L420 at 0.9495 -> 7245x; all four are already
        in the shipped corpus and three are in the shipped golden file)
cell   bisect L to effective(dropped_shear_parameter) = CD, L the only variable
       moved, 70 steps, nine section families
out    iso 7630.2x   thin 7630.2x   thick 7630.2x   big D=3.0 m 7630.2x
       aniso 688 7630.2x   aniso 1e6 7630.2x
       micro D=0.6 mm 9267.2x   skew 9267.2x   skew+roll 9530.3x
       D from 6e-4 to 3.0 m, t/D 0.02..0.25, L/r_min 1994..1.99e6
```

`8.698e+06x` is a true number about `one_element_scaled` and it is 1140x the margin
at the point where the rule actually decides something. The plan says my `7630x` "is
attributed, not published, because I did not reproduce that construction" -- the
construction is one bisection on one variable, it reproduces across nine families to
five digits, and four pairs of the **shipped** corpus sit at the boundary with no
construction at all. "A ratio carries its operating point" asks for the point where
the predicate flips, and for `one_element_scaled` there is no such point.

**Closed when** the boundary margin is quoted for a defect kind whose effective size
is not identically `CD`, or the plan says plainly that `8.698e+06x` is the margin
under the calibrated defect and is not the tightest.

**R158. (recordable) The golden file's premise -- "carries no red assertion" -- is
true of 14 of its 34 rows. Twenty are `dropped_flip` or `wrong_dof_index`, which
`UNCONDITIONALLY_RED` asserts regardless of classification. The runner prints the
same sentence about all 40 exempt pairs.**
`tests/regression/test_exempt_pair_responses.py:3-7`, `:93-95`;
`test_corpus_configurations.py:1428-1430`.

```
claim  "A pair whose injected defect is below CD carries no red assertion"     -- :3
claim  "this pair carries no red assertion ..., so nothing else would have
        noticed"                                          -- the failure message :93
claim  "EXEMPT 40 of 396 ... carry no red assertion"      -- the printed line
cell   make one recorded pair stop being detected, one variable moved
out    a dropped_flip pair  -> 2 failed: the golden AND
                              test_the_corpus_entry_goes_RED_under_every_injected_defect
       a dropped_shear pair -> 1 failed: the golden alone
cmd    composition of the golden file by defect kind
out    dropped_shear_parameter 14 | wrong_dof_index 11 | dropped_flip 9
       20 of 34 are already asserted red by UNCONDITIONALLY_RED
```

The file is not wrong to record them -- pinning the value is more than pinning
`> ceiling` -- but "nothing else would have noticed" is false for 20 of 34, and it is
the sentence a later reader will use to decide what the file is for. **Closed when**
the three sentences scope themselves to the classifiable defect, or say that the
other three kinds are covered twice.

**R159. (recordable) The causal sentence added to `_homogeneous` this round is
refuted by a one-variable cell. The conclusion holds; the mechanism given for it does
not.** `test_corpus_configurations.py:883-890`.

```
claim  "Multiplying it by a constant is a change of convention, not a defect: it
        rescales every rotational row and column of both the numerator and the
        denominator, and `injected_delta` is a ratio of the two."
cell   ell -> 1000*ell, one variable moved, all 396 pairs
out    effective size moved on 200 of 396 pairs, up to 1054x;
       classification changed on 62 pairs
cell   ell -> 0.001*ell
out    moved on 297 of 396, up to 5.5e+04x; classification changed on 32
```

It does not cancel, because `injected_delta` is a ratio of two **maxima** over a
matrix whose entries are scaled non-uniformly, and the argmax moves.

**And the conclusion is right, which I measured rather than assumed.** All 62 changes
are in `UNCONDITIONALLY_RED` kinds; zero `dropped_shear_parameter` classifications
move, and I hunted for one over 1208 further configurations spanning `D = 0.05..3.0`,
`t = 5e-4..0.15`, `L = 0.5..5e4`, three orientations and four anisotropies -- **0
flips**. Better still: at `ell -> 1000*ell` the full suite is now **red**, at
`test_the_recorded_set_is_the_measured_set`. BS2's golden file has incidentally
become the guard on `ell` that R145 asked for, and a stronger one than the
unit-invariance test. Say the measurement; drop the "because". **Closed when** the
sentence is the bound it is -- no decision on this corpus moves; the classification
of 62 of 396 pairs does, all of them in `UNCONDITIONALLY_RED` -- or the cancellation
claim is removed.

**R160. (recordable) Two accuracy tolerances were borrowed into new quantities this
round, and neither borrowed a counter in the new quantity.**
`test_corpus_configurations.py:1084`, `:965`;
`tests/regression/test_exempt_pair_responses.py:90-92`.

`ROUNDOFF_IDENTITY` (counter `1e-8`, in the round-off-identity quantity) now sets the
calibration's band and `classify`'s floor. `SUBDIVISION_INVARIANCE` (counter
`4.8e-8`, in the subdivision-invariance quantity) now sets the exempt-pair regression
band. The recorded rule: "A counter measured in a different quantity is evidence for
a different test."

I measured the missing one by inverting the decision rule and solving:

```
cell  perturb one recorded golden response by rel; bisect on rel
out   2.0e-11 RED | 1.1e-11 RED | 1.0e-11 green | 9e-12 green | 5e-12 green
      -> the regression's counter, in its own quantity, is 1.0e-11 exactly
```

**Closed when** each borrowed use records its counter in its own quantity, or the
report states the two measured numbers: `1.000 ULP` from R156 and `1.0e-11` here.

**R161. (recordable) `test_plan_matches_tolerances.py` runs plan -> code only. A new
constant added to `tolerances.py` and never named in the plan passes with the full
suite green.** `tests/test_plan_matches_tolerances.py:48-58`.

```
claim  "A tolerance can now move only together with a plan edit"          -- :8
cell   append `NEWLY_ADDED_FUDGE: float = 0.25` to floatfea/tolerances.py,
       nothing else moved, full suite
out    1028 passed
cmd    set(_declared()) - {name for _, name, _ in _stated_in_plan()}
out    set()      -- true today, asserted nowhere
```

`_stated_in_plan()` iterates the plan, so the plan can only be wrong about a constant
it mentions. The completion is one assertion on that set difference, and the report's
sentence "every declared tolerance is tabulated" is a fact about today rather than a
property. Its meta-test's floor is still `>= 3` against 25 names. **Closed when** the
set difference is asserted, or the docstring says the check is one-directional.

**R162. (recordable) Sec. 5's third figure carries no command and I could not
reproduce it. The two that decide the section reproduce exactly.** report sec. 5.

```
claim  "uniform (1 + CD) on the whole model measures CD to 9.8e-11 relative"
cmd    max|H(CD*K_assembled)| / max|H(K_assembled)| over 99 solved entries
out    max relative error vs CD = 0.000e+00   (exact -- numerator and denominator
       share an argmax, so the scaling is a single common factor)
```

A construction that assembles a `(1 + CD)`-scaled model and differences it would
plausibly give `~1e-10`; that is a guess, and the block gives no command. Recorded
under "every claim carries its command" rather than as a contradiction. **Closed
when** the figure carries the construction that produced it.

## Tolerances touched

**None in `floatfea/tolerances.py`.** `git diff 4631c18..e8920b8 --
floatfea/tolerances.py` is empty and `git diff --stat ... -- floatfea` is empty. No
existing golden value moved.

**Two comparison thresholds were introduced in `tests/`, both composed from declared
constants, and both are new uses of an existing name in a new quantity.**

| site | form | old | new | counter in its own quantity |
|---|---|---|---|---|
| `test_corpus_configurations.py:1084` | `assert_close(measured, CD, ROUNDOFF_IDENTITY, floor=eps*CD)` | `==`, 0 ULP | 47.2 ULP | **not recorded**; I measured `1.000 ULP` over 831 configurations (**R156**) |
| `test_corpus_configurations.py:965` | `CD * (1 - ROUNDOFF_IDENTITY)` | `CD` | 47 ULP lower | direction is safe -- it widens `live`, never `below resolution`; ablation confirms exempt `41 -> 40`, the freed pair being `one_element_scaled` |
| `test_exempt_pair_responses.py:90` | `assert_close(now/ceil, was/ceil, SUBDIVISION_INVARIANCE, floor=eps)` | new file | 1e-11 relative | **not recorded**; I solved it: `1.0e-11` exactly (**R160**) |

`tests/regression/g22_exempt_pair_responses.json` is a **new** golden file, 34 rows,
generated with my sixteenth-round corpus applied. Nothing was regenerated to match
new output. One structural note, not a finding: the file is keyed on corpus entry
ids, so every reviewer corpus round will redden
`test_the_recorded_set_is_the_measured_set` and be closed by regeneration. That is
the design and the docstring says so; it is also the one place in this repository
where regenerating a golden becomes routine, and the closure artifact should carry
the per-round reason rather than a standing one.

**What held.** I re-derived every published figure independently. These
**reproduce**: `1028 passed`; `EXEMPT 40 of 396` with `dropped_flip 9,
dropped_shear_parameter 20, wrong_dof_index 11` and `34 detected`; the `41 -> 40`
ablation with `one_element_scaled 1` as the freed pair; `3999x` at
`br2_floor_thick_iy1e6_L1000`; `8.698e+06x`; `0.0006932x`; `0.0887x`; sec. 5's
`0.1206 .. 0.1409 x CD` and `0 of 99`; `25` of 25 tolerance names bound; the `0.19%`
and `24%` division measurements; the golden file's detection boundary at exactly
`1.0e-11`; and all three BS3 mutants. These do **not**: `8.701e+06x at L/r_min 558`,
`5.150e+09x`, `5.227e+09x`, `90-entry`, `3.9413e-14`, `2.537e+07x`, `105-entry`,
`eight sites`, `9.8e-11`, and "one ULP".

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a HOLD, not a STOP: rung 1 is
green at `e8920b8`, no production code or tolerance moved, the `process:` commit and
the plan commit are both correctly standalone, and three of the four substantive
moves survive being broken deliberately.

1. **R153 -- the guard that cannot run.** First, because it is the mechanism. The
   hook's own invocation is unreachable; the demonstration is the hook run at a
   commit with a missing finding, with the blocking JSON pasted.
2. **R154, R155 -- two items recorded closed that are closed at part**, plus the plan
   table at `F2.md:513-521` refuted by four orders fifteen lines above this round's
   own paragraph about stale figures. Site by site.
3. **R133 -- untouched from the fifteenth verdict**, blocking, and now contradicted
   by a comment added this round in the same file.
4. **R156 -- the 47-ULP band with a one-ULP record.** Either number may move; they
   have to be the same number.
5. **R157 -- the operating point.** `7630.2x` across nine families from a bisection
   on one variable, against `8.698e+06x` published as "where it is actually tight".
6. **R132, R136, R137 -- untouched from the fifteenth verdict**, and R132 is now
   wrong in three fields rather than two.
7. **R148, R151, R152 -- declared open by the report**, answerable in one line each.
8. **R158, R159, R160, R161, R162 -- recordable.**
9. **R113, R95, R97, R98, R100-R103, R63, R76, R79, R80 -- carried, unchanged.**

**Adversarial corpus (BE3): 11 new entries committed, all unseen by the implementer;
every outcome measured before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **133** entries, 109 solved,
committed separately at `f66e4e0` immediately before this verdict and touching no
code. Full suite with the corpus applied: **1077 passed, 1 failed.**

The coverage measurement, stated plainly and in the implementer's favour this time:
**5 of my 11 new entries produce a new exempt-and-detected pair, and BS2's golden
file caught all 5** -- by name, in one assertion, on entries its author had never
read (`bs_boundary_aniso1e6_L414590|wrong_dof_index`,
`bs_boundary_aniso688_L10875|dropped_shear_parameter`,
`bs_boundary_aniso688_L10875|wrong_dof_index`,
`bs_boundary_big_D3_L2080|dropped_shear_parameter`,
`bs_just_below_iso_L430|dropped_shear_parameter`). That is the first guard in this
milestone to bind on unseen input on its first round, and it is a measurement the
implementer's own planted-pair count could not have produced.

Against that: the entries were chosen because the *published* margin at the rule's
operating point is measured under the one defect kind that has no operating point,
and `bs_boundary_big_D3_L2080` states the case in one line -- `eff/CD = 0.99996`,
four parts in `1e5` below the declared resolution and forty billion times outside the
ULP allowance `classify` gained this round, detected by `7630x`, and the assertion is
not made.

**Seventeen consecutive rounds have found no element defect**, and the reading is
unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side. Every
defective instrument this milestone has been a test or a document; the element has
been fine every time, and that is exactly the pattern "do not let right every time
become a prior" warns about.

**Witness channel unavailable.** `git remote -v` is empty, so no PR and no
`[witness ...]` comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a
pass. Seventeen consecutive reviews by one reader -- and R153 is what that costs: a
guard was written, reviewed by its author, reported as working, and does not execute.

**The standing question for the next round.** This round wrote three new guards. I
broke two of them by mutating the code they watch and they held; the third I broke by
running it. **For every guard in this repository, what is the command that shows it
executing -- not that it exists, not that it passes, but that the code path was
entered?** `check_carried.py` passes when run by hand and is never run;
`test_the_delta_measure_is_UNIT_INVARIANT` is entered and reddens on its mutant.
Provenance, not existence, applied to the guards themselves.
