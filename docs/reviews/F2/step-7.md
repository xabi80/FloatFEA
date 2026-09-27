# Review � F2 step 7
Reviewed commit: 173130785ff91c3ba5997776ff02953ff691e110
Verdict: PASS

**Reviewed commit: `36b5899`. Sixty-third verdict, the SECOND and LAST on step 7.**
**DK2’s cap applies: this verdict closes step 7 and closes F2.** The `Reviewed
commit:` line stamped at the top of this file by `scripts/write_verdict.py` is my
corpus commit `1731307`, not the commit judged (R513, unchanged).

Tests: **2761 passed, 1 failed, 0 skipped** — my run, `python -m pytest -q` at
`36b5899`, 674.38 s, Python 3.13 on Windows, 2 warnings (both pre-existing, the
`orient_norm_overflow` g22 entry). **CI at the reviewed commit is 3 failed, all in
`tests/test_report_guard_states.py`, and two of the three do not reproduce on my
machine.** That is R544 and it is the one blocking item in this verdict.

**PASS IS THE CAP, NOT A CLEAN BILL, AND I AM SAYING SO IN THE FIRST PARAGRAPH.**
Absent DK2 this would be a HOLD under CA2 — a red CI is a HOLD regardless of the
local run. DK2 is a throughput decision made above me and it says the step closes
on this verdict with open blocking items carried by name, so R544 carries into F3
and blocks there. **The verification ladder, all ten determinism legs and the
agreement job are SUCCESS at `36b5899`**, so no rung is red and this is not a STOP.

## You were right and so was the fix — R541, checked four ways, two of them mine

**R541’s correction is right, and I did not take the report’s word for any part of
it.** The strongest evidence is a witness that shares nothing with the module’s
derivation:

```
cell  THE CLASSICAL SHEAR-FLEXIBLE HERMITE SHAPE FUNCTIONS, written out from the
      standard (1 + Phi) form -- not from beam.py, not from eq. 5.36 -- and
      compared with the shipped bending_interpolation term by term at 11
      stations, over Phi = 0, 1e-3, 0.1, 1, 2.5, 10, 100 and L = 0.5, 4, 60 m.
out   N_w     worst relative 3.6e-15 over all 21 combinations
      N_theta worst relative 1.0e-15
judge THE CORRECTED INTERPOLATION *IS* THE CLASSICAL SHEAR-FLEXIBLE ELEMENT, at
      every Phi and every span. This is a fourth independent witness and the only
      one that could not have shared the error: the determinant, the energy
      identity and the cantilever all run through the same algebra, and this does
      not. The - Phi xi / 6 sign is not a plausible choice, it is the element.
cell  BIT-IDENTICAL STIFFNESS, wider than the claim. Worktrees at 968435a~1 and
      HEAD, local_stiffness hashed as raw bytes over THREE sections
      (D=0.3/t=0.008, D=0.6/t=0.012, D=3.0/t=0.001) x THREE spans (1, 4, 60 m).
out   9 of 9 hashes identical. local_mass differs at 9 of 9, as it must.
judge THE REPORT CLAIMS THREE SPANS AND I CHECKED NINE CASES. Rung 1 is not in
      play, and the claim is stronger than the one published.
cell  UNIT SCALING, because an exactness identity that is not dimensionless is a
      defect. The energy identity at Phi held fixed while the length scale moves
      1e-3 .. 1e3 and the modulus scale 1e-6 .. 1e6.
out   8.1e-16 .. 2.7e-15 across six decades of length and twelve of modulus
judge DIMENSIONLESS AND SCALE-FREE. No operating point is hidden in it.
```

## DN0’s second branch — RULED ON, AND IT WAS TAKEN CORRECTLY

**You asked me to rule on this and the answer is yes, with one correction to how
the first cell is described and none to the conclusion.**

The branch condition was: *if the ratios recover once the stiff modes are out of
`lambda_max`, the degradation was conditioning.* The numbers refute it and the
refutation does not depend on the contrast that could not be run. At `n = 16` the
discretisation error is `1.9494e-06` against a floor of `1.9340e-10` — four orders
above it — while the ratio has already fallen to `10.31`. A floor four orders below
the signal cannot be what moved the signal. The floor reaching `1.2785e-08` against
`1.4059e-08` at `n = 128` explains the finest mesh and nothing coarser. The rotary
ablation is a genuine one-variable cell against its own closed form and lands on
`13.63, 10.31, 6.62, 4.47` — identical to four figures, which is as clean a
refutation as this kind of cell produces.

**Saying the model was already planar-bending-only, so DN0’s contrast could not be
run as a contrast, is the right thing to have written.** A cell that cannot be run
reported as a cell that was run is the defect; a cell that cannot be run reported
as such is a finding about the directive, not about the work. And it does not
weaken the branch: DN0’s condition is about whether the ratios *recover*, and they
do not recover in a model where the stiff modes were never in `lambda_max` to begin
with — which is a stronger statement than the contrast would have given.

**And I confirm the residual is not identified and that this is the honest state.**
I looked for it in one place the report did not, and found something adjacent that
matters more than the order: see R545.

## DN1’s energy check — I tried to make it pass on a wrong element and could not

```
cell  THE SHEAR TERM COEFFICIENT, SWEPT rather than flipped. The shipped
      interpolation with - s * Phi / 6 in both of its sites, s swept, run through
      the SHIPPED _energy_mismatch at all five probes.
out   s          worst over the five probes      verdict against 1e-14
      1.0        2.0e-15                         passes  (correct element)
      1.0000001  2.5e-13                         FAILS   (25x the ceiling)
      1.000001   2.5e-11                         FAILS
      1.001      2.5e-07                         FAILS
      0.9        2.8e-03                         FAILS
      0.0        9.1e-01                         FAILS   (shear term deleted)
      -1.0       LinAlgError at Phi = 1          FAILS   (R541 as it shipped)
judge THE DETECTION THRESHOLD IS s - 1 ~ 4e-9, SOLVED FOR RATHER THAN SAMPLED.
      This is a counter in the counter own sense: not one arbitrary perturbation
      but a measured boundary, and the shipped defect sits nine decades outside it.
cell  THE OTHER HALF OF THE FIELD, because a check on the shear term could be
      blind to the rest. The theta interpolation quadratic coefficient perturbed
      by eps.
out   eps = 1e-9 gives 5.5e-09, already 5.5e+05 times the ceiling
judge IT SEES BOTH HALVES OF THE FIELD, not just the term it was written for.
cell  A GATE CARRIES ITS OWN FAILURE, run rather than argued. R541 injected back
      into floatfea.element.beam through a -p plugin loaded before collection, so
      the real module path is patched and not a test-local name -- then each
      assertion run clean and injected.
out                                                             CLEAN   INJECTED
      test_the_frequency_sequence_is_MONOTONE_under_refinement    pass    FAIL
      test_the_SHIPPED_element_approaches_its_OWN_continuum       pass    FAIL
      test_the_INTERPOLATED_FIELDS_OWN_ENERGY_equals_the_stiffness pass   FAIL
      test_the_PHI_ZERO_limit_reproduces_the_TRANSCRIBED_mass_matrix pass  pass
      test_the_six_RIGID_BODY_inertias_of_ONE_ELEMENT_are_exact     pass   pass
judge THREE ASSERTIONS NOW REDDEN ON THE DEFECT AND THE TWO DIAGNOSED AS BLIND
      ARE STILL BLIND, exactly as the closure artifact says. The gate that was
      missing exists and it fires.
```

**And the resolution repair is real.** `interp` is a parameter of
`_field_coefficients` and `_energy_mismatch`, `_flipped` calls
`bending_interpolation(length, -phi, xi)`, and I checked that `phi` appears in
`bending_interpolation` at exactly two sites, both as `- phi/6`, so passing `-phi`
reproduces the shipped defect bit for bit and nothing else. The counter injects the
defect that shipped, not an invention.

## My own instructions (4b), conftest (4c), tolerance VALUES (4)

```
cmd  git diff acb5e8c..36b5899 -- .claude docs/SUPERVISOR.md
out  (empty). NOT A STOP on this head.
cmd  git ls-files -- tests/conftest.py  and the double-star half beside it
out  tests/conftest.py   -- the expectation the instruction prints, met
cmd  git diff acb5e8c..36b5899 -- the same pathspec
out  (empty)
cmd  git ls-files "*conftest.py" ; git ls-files | grep -iE "pytest_|plugin"
out  tests/conftest.py, and nothing else. No plugin entered the tree, no rung
     grew a conftest, and the six CH2/CI0 channels are closed by inspection.
     Six tests entered rung 2 this round and none arrived with a hook.
cmd  for each commit in acb5e8c..36b5899: does it touch floatfea/ AND docs/reviews/?
out  none. b52b370 is verdict 62, alone, and it is BEFORE the code it judged --
     which is the right order and is what the separate-commit rule asks for.
cmd  the plan re-locks: do 87606e7 and 6b39b78 touch anything but docs/milestones/?
out  no. Two standalone plan: commits, each naming its directive (AO4/DN0, DM1).
     The process discipline held.
cmd  git diff acb5e8c..36b5899 -- floatfea/tolerances.py, non-comment +/- lines
out  (empty). 25 changed lines, every one a comment.
cmd  every NAME: Final[...] = value at acb5e8c and at 36b5899, diffed
out  48 and 48, byte-identical. NOT ONE VALUE MOVED.
cmd  ruff check floatfea tests ; black --check floatfea tests ; mypy floatfea
out  All checks passed! ; 84 files unchanged ; no issues in 27 source files
```

## CI (3b) — RED at the reviewed commit, and thank you for dispatching it

```
cmd  gh run list --commit 36b5899 --json name,conclusion,workflowName
out  []  -- the commit filter returns nothing again, the same quirk as at
     acb5e8c and 792c44e. Recorded so the next reader does not read it as absent.
cmd  gh run view 36313726383 --json status,conclusion,headSha,event,jobs
out  completed FAILURE  headSha 36b5899e...  workflow_dispatch
     the verification ladder             SUCCESS
     CI determinism -- leg (1)..(10)     SUCCESS, all ten
     CI determinism -- ten legs agree    SUCCESS
     lint, unit and guards               FAILURE
cmd  gh run view 36313726383 --log-failed, failing names deduplicated
out  3, all in tests/test_report_guard_states.py:
       ...[answers_header_names_an_older_verdict_commit]
       ...[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_
           actually_REDDENS_CONTROL]
       ...[guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_
           SUITE_WAS_RED]
cmd  the same three, locally at 36b5899
out  1 failed, 2 passed -- only the third reproduces here
judge NOT CK2: real step counts, a real runner, and a real ladder result. **THIS
     IS CA2 IN ITS TEXTBOOK FORM** -- two of three reds exist only on a machine
     neither of us controls, which is the entire reason the rule is written down.
     It is R544 and it BLOCKS under (d). It is NOT a low rung: the ladder is
     SUCCESS at this commit and so are all ten determinism legs.
cmd  gh pr view 1 --json comments, length of the array
out  0 -- no outside-witness comment. Unavailable check, fourteenth round, and
     F2 now closes without one ever having been posted. That is a gap in the
     record and it goes in the closure artifact as one.
```

**Item 1b — CHECKED, AND CLEAN.**

```
cmd  the newest Answers line in revision 2 of the report under review
out  docs/reports/F2/step-7.md:278 -- Answers: verdict 62 @ b52b370
cmd  git log --oneline --follow -- docs/reviews/F2/step-7.md | head -1
out  b52b370 review: F2 step 7 -- sixty-second verdict, HOLD @ acb5e8c
judge THE HEADER NAMES THE LATEST. One comparison, made, it matches, so every
     Carried claim in revision 2 is about the right list.
```

## Carried

Verdict 62 was a HOLD carrying **R541**, **R542** and **R543** as blocking, C14 to
C19 as closure items, and seven numbered conditions.

- **R541 — ANSWERED at `968435a`, and I verified it four ways, two of them cells
  the report does not contain.** All five named sites: `beam.py:277` and `:283`
  carry `- phi / 6.0` and `- phi * xi / 6.0`; the module comment at `:173-207` now
  derives the slope condition from `M = EI theta-prime` and
  `V = -EI theta-double-prime`, giving `w-prime = theta - c theta-double-prime`,
  and abandons the old `M-prime = V` route — and it does the right thing by saying
  the derivation is NOT what settles it, the two convention-free checks are; the
  energy assertion at non-zero `Phi` exists
  (`test_the_INTERPOLATED_FIELDS_OWN_ENERGY_equals_the_stiffness`); `Phi = 1` is in
  its parametrisation, which is the singular case evaluated rather than avoided. My
  own witness against the classical `(1 + Phi)` shape functions agrees to
  `3.6e-15`. **Answered, and the fix is better evidenced than the finding was.**
- **R541 condition (4) — ANSWERED at `2048ad9`.** The `asserted = (4, 8, 16)`
  truncation is gone; the loop runs `reported[:-1]` against `reported[1:]` over
  `4..128`. I re-measured: positive and falling at every mesh, both planes, all
  three modes, at this geometry.
- **R541 condition (5) — ANSWERED at `968435a`.** The V6.1 golden is regenerated in
  the same commit as the fix, with the explanation in `docs/closure/F2-step7.md` §2
  as its own docstring requires. I checked the count: `126` numeric leaves, `56`
  changed. Both figures are exactly right. **A golden regenerated in the same
  commit as the code it tracks is correct here and not the tolerance-widening
  shape** — the golden is a record of output, the explanation is written, and the
  36 regression failures before the regen are published.
- **R542 — ANSWERED at `2048ad9`.** The assertion covers what it prints, the
  docstring account of the old range names the defect rather than restating the
  withdrawn reason, and a new positivity predicate was added beside the falling
  one. I injected the defect: both halves redden. **Answered — and the claim that
  the property is exact theory is bounded rather than universal, which is R545.**
- **R543 — ANSWERED at `e0ab508`, value unmoved, and the numbers are exactly
  right.** I re-took all five spans through the comparison the test itself makes
  (`rho_a = 2.5`, normalised on `max|want|`): `0.54, 0.54, 4.07, 2.02, 4.93` ULP,
  worst `1.0952e-15`, headroom `9.13x`. Every figure in the entry reproduces to
  four figures. `git diff` over the file is 25 lines, all comments; the 48
  constants are byte-identical. **The residue is that the regenerator the entry
  cites prints nothing — C20, closure.**
- **Condition 4 (the V6.1 golden regenerated with the written explanation) — MET.**
- **Condition 5 (AO4 re-argued in a standalone plan: commit) — MET at `87606e7`,
  and it is the right shape.** §141 quotes the withdrawn sentences rather than
  deleting them, names R541 as the cause, and records which DN0 branch applied.
  `docs/milestones/F2.md:2071-2079` corrects the AO4 row the same way. Two
  standalone plan: commits, neither touching `floatfea/` or `tests/`.
- **Condition 6 (C14 to C19 in one closure commit) — MET at `41a200c`** for the
  three with a site in the tree (C15, C16, C17), with C14 answered in §1 of the
  report and C18/C19 absorbed by the plan re-lock and the artifact. I verified the
  C17 repair: `sequences(no_phi=True)` now patches `shear_parameter` alone and the
  `bending_mass` rewrite is gone, so the cell moves one variable, and both legs
  still read `0.000e+00`. Not re-reviewed item by item beyond that.
- **Condition 7 (`0 failed` locally apart from the verdict-absence guards, and a
  SUCCESS ladder on CI at a commit whose push touches `floatfea/`) — HALF MET, and
  the unmet half is R544.** The ladder is SUCCESS at the reviewed commit. The local
  run is `1 failed` and the failure is NOT a verdict-absence guard; CI is `3
  failed`. The last push touching `floatfea/` (`968435a`) is a failure, and the
  failure at `41a200c` was measured before revision 2 landed — those two I accept
  as superseded. The three at `36b5899` are not superseded by anything.
- **Conditions 1, 2, 3 — MET**, as the R541/R542/R543 rows above.
- **C1 to C13 and C14 to C19 — closure items, carried into the artifact, NOT
  re-reviewed item by item** per CZ0. C14, C15, C16, C17 are answered; C18 and C19
  are absorbed.
- **R475 / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 /
  R523 / R524 / R525 / R526 / R527 / R528 / R529 / R533 / R535 / R538 / R539 and
  the 48 frozen 4a items — OPEN on the closure list, none re-reviewed.**

## Findings

**R544. (BLOCKS — (d).) THREE TESTS ARE RED AT THE REVIEWED COMMIT IN CI AND ONE OF
THEM IS RED LOCALLY. THE ONE I CAN REPRODUCE IS A NEGATIVE CONTROL THAT WAS PASSING
VACUOUSLY UNTIL THIS STEP REMOVED THE UNRELATED CAUSE, AND IT IS NOW TELLING THE
TRUTH: THE STATE IT PLANTS IS NOT THE STATE IT NAMES.**

```
cmd  python -m pytest -q   (my run, at 36b5899, 674.38 s)
out  1 failed, 2761 passed, 0 skipped
     FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state
       [guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED]
     this state is a defect and must fail -- the nested guard reported 206 passed
cmd  the same single test in a worktree at acb5e8c, the commit verdict 62 judged
out  1 passed
judge IT PASSED THERE AND FAILS HERE, so it is NEW THIS STEP. But it passed there
     for a reason that has nothing to do with the state: at acb5e8c the nested
     guard failed because step 7 had a report and no verdict, so code != 0 was
     satisfied by the verdict-absence guard and ANY state would have passed this
     control. Verdict 62 ruled those eight reds not-(d) and was right to. The cost
     of that ruling is visible here: the control was certifying nothing, and the
     moment the verdict existed and the guard went otherwise green, it went red.
cmd  tests/test_report_guard_states.py:457-488 (suite_line_at_an_older_ancestor)
     and :253-276 (_seed_older_verdict), read today
out  the action takes git log --format=%h -- docs/reviews/F2/step-7.md, and at
     36b5899 that path has ONE commit, so it seeds. _seed_older_verdict commits
     TWO commits ON TOP of the scratch HEAD. older[1] is then the FIRST of those
     two -- a commit one behind the scratch HEAD, a DESCENDANT of the commit the
     report sits on, not an ancestor of it. The whole-suite line is rewritten to
     name it, the report is left modified so _report_anchor() returns HEAD, and the
     guard measures rev-list --count older[1]..HEAD = 1, which is <= 1, so it
     correctly passes.
cmd  git rev-list --count b52b370..36b5899
out  8
judge SO THE STATE IS NOT BUILT. A genuine older ancestor -- b52b370, the commit of
     the previous verdict, which is what the comment on the action says it means to
     point at -- gives distance 8 and reddens
     test_the_whole_suite_line_is_about_a_commit_that_exists at
     tests/test_report_carried.py:2332. The guard under test is FINE. The harness
     that is supposed to prove it is what is broken, and the control is the thing
     in this repository that noticed.
cmd  the other two, locally
out  both pass here and both fail in CI. answers_header_names_an_older_verdict_
     commit goes through the same seeding path.
     guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_
     REDDENS_CONTROL is the meta-control over
     tests/test_report_guard_states.py:195-211, whose two entries declare
     shallow_clone_depth_1 as named_fail and two_digit_step_number as green; one
     of those declarations is false on Linux and true on Windows.
judge **A RED CI IS A HOLD (CA2) AND ONLY DK2 IS STOPPING ME FROM WRITING ONE.**
     Two of three reds are invisible from here, which is the measured reason CA2
     exists. Under CZ0 the SUBSTANCE is apparatus and would be a closure item;
     (d) is a separate head and a red test blocks on being red.
```

  **Closed when** `python -m pytest -q` is `0 failed` and the `lint, unit and
  guards` job is SUCCESS, at one commit, with all three states named: (1)
  `_seed_older_verdict` stops being used for `suite_line_at_an_older_ancestor` and
  `answers_header_names_an_older_verdict_commit`, or the two actions point at a real
  ancestor of the commit the report sits on rather than at `older[1]` of a history
  the seeding just extended — and the fix is demonstrated by the guard going RED on
  the rebuilt state, not by the control going green; (2) the two declarations in
  `REQUIREMENT_CHANGED` are re-measured on Linux and the one that is wrong is
  corrected; (3) the distance `git rev-list --count <planted>..<anchor>` is printed
  by the harness when the control fails, so the next reader does not have to
  re-derive it. **This is an existing guard failing false. `CLAUDE.md` says such a
  guard is fixed or deleted, never extended, and nothing here needs new apparatus.**

---

**R545. (CLOSURE under CZ0, and it is the one I would most like argued with.)
THE G2.4 POSITIVITY-AND-FALLING ASSERTION IS EXACT THEORY ONLY WHILE THE FIRST
THREE DISCRETE EIGENVALUES ARE ALL FLEXURAL. AT THE ADMISSION LIMIT `L/D = 2` THE
THIRD IS NOT, AND THE ASSERTION WOULD CALL A DEFECT-FREE ELEMENT BROKEN BY 34%.**

```
cmd  tests/verification/rung2/test_consistent_mass.py:881-884 and :919, and
     docs/milestones/F2.md:158
out  on the corrected element it is exact theory rather than a measurement that
     happened to come out that way ; YES on the SIGN, asserted over n = 4..128 ;
     and the message the assertion carries: the interpolation family is
     length-independent and conforming, so Rayleigh-Ritz forbids it -- R541 was
     this assertion failing, and the cause was the shear term sign
cell THE SAME PREDICATES, OFF THE ONE GEOMETRY THEY ARE PARAMETRISED ON. Six
     sections x L, n = 4..128, both planes, modes 1..3.
out  D=0.3 t=0.008 L=30   L/D=100  Phi=7.0e-04  no negatives, no rises
     D=0.6 t=0.012 L=3    L/D=5    Phi=0.28     no negatives, no rises
     D=1.0 t=0.05  L=2    L/D=2    Phi=1.66     mode 3 NEGATIVE at every mesh,
                                                -0.3153 at n=4 to -0.3383 at
                                                n=128, and RISING at all five
                                                refinements
     D=2.0 t=0.5   L=4    L/D=2    Phi=1.15     mode 3 -0.1882, same shape
     D=1.0 t=0.05  L=1    L/D=1    Phi=6.65     modes 2 AND 3
     D=0.1 t=0.004 L=100  L/D=1000 Phi=6.8e-06  mode 1 RISES, 4.65e-09 at n=64
                                                to 2.29e-08 at n=128
cell LOCALISE IT BEFORE BLAMING ANYTHING -- the element or the reference.
out  at D=1.0 t=0.05 L=2, the n=128 discrete spectrum is
     432.61, 1058.00, 1105.67, 1671.39, 1746.10, 2273.93 Hz
     and the flexural roots are 432.60, 1057.92, 1671.06, 2273.08.
     Discrete 1, 2, 4, 6 are flexural 1, 2, 3, 4, each high by 1.3e-05 .. 3.7e-04.
     1105.67 and 1746.10 are INTRUDERS, and 1746.00 is the first root of the
     second branch. The intruder at 1105.67 CONVERGES -- 1144.4, 1106.9, 1105.65
     over n = 4, 16, 128 -- so it is a genuine continuum eigenvalue, approached
     FROM ABOVE.
judge **RAYLEIGH-RITZ IS NOT VIOLATED AND THE ELEMENT IS NOT WRONG.** What breaks
     is the PAIRING: the k-th discrete eigenvalue is compared with the k-th
     FLEXURAL root, and once the second spectral branch descends past the third
     flexural mode those are different objects. The -33.8% is the distance between
     two correct numbers that are not about the same mode.
cmd  the DN1 energy identity at all 20 corpus entries below
out  <= 2.3e-15 on 20 of 20
judge SO THE ELEMENT IS RIGHT ON EVERY MEMBER WHERE THE ASSERTION WOULD SAY IT IS
     WRONG, measured on the shipped check rather than argued.
```

  **Why this is a closure item and not (c), said explicitly because it is close.**
  What the gate asserts, on which quantity, at which threshold, is correct at the
  geometry it is parametrised on — I re-measured it and it holds. What is false is
  the GENERALISATION published beside it in two places, and a false sentence is a
  closure item under CZ0 even when it is about a gate. **What makes it worth more
  than its class**: the failure message tells a future reader that a red means the
  shear sign is wrong again, and the platform model in F3 puts stubby braces into
  exactly this test. The first person to extend the parametrisation gets a red on a
  correct element with a message naming the element.
  **Closed when** the docstring at `:881-884` and `docs/milestones/F2.md:158` state
  the bound — the property holds while the first three eigenvalues are flexural,
  which is `Phi` small enough that the second branch has not descended — and the
  message names the branch crossing as the first thing to check. No new apparatus:
  this is two sentences and one string.

---

**On the one caller of `bending_interpolation`, which I checked rather than
accepted.** `grep -rn` over `floatfea/` and `scripts/` gives `bending_mass` at
`beam.py:306` and nothing else; `local_mass` reaches `assemble_mass_dense` through
`floatfea/assemble/system.py:102` and `scripts/regen_f2_golden.py:122,131`.
`floatfea/post/`, `export/`, `solve/` and `checks/` contain `__init__.py` and
nothing else. **The blast radius in the closure artifact is correct as published**,
including the claim that no stress recovery consumes the interpolation.

**On an adversarial case that failed to be adversarial, recorded because a probe
that finds a guard working is worth the same as one that finds a hole.** The whole
V2.5/G2.4 rung runs on `I_y == I_z`. I tried to build a member with `I_z = 8 I_y`,
which is what the docstring at `beam.py:314-320` says F3 introduces, and the tree
refused it twice: `basis.kappa` raises for `shape="i_beam"` with a message naming
Cowper (1966) Table 1 and the words *rather than defaulting*, and
`floatfea/model/material.py:101` raises for a circular shape whose second moments
differ. **An asymmetric section is unconstructible at F2 and that is correct**, so
the assertion-domain question I was chasing does not exist yet. It is an F3
question and it arrives with the section registry, not with the mass matrix.

## Closure items (CZ0). None of these is (a), (b), (c) or (d).

**C20. `floatfea/tolerances.py:1389-1391` cites a regenerator that prints
nothing.** The entry records `4.93 ULP, 1.0952e-15, 9.13x` — all three exactly
right, I re-took them — and says the worst value above is re-taken by
`python -m pytest tests/verification/rung2 -q -s -k PHI_ZERO`. That command prints
`5 passed` and no number:
`test_the_PHI_ZERO_limit_reproduces_the_TRANSCRIBED_mass_matrix` has no `capsys`
block. So the measurement in `tolerances.py` has neither of the two exits BI3
offers: no script produces it, and the pointer that is supposed to stand in for one
does not. `1.0952e-15` appears nowhere in the tree but that comment, the report and
verdict 62. **Closed by one `print` in that test, or by pointing at §1 of the
report, which IS regenerated by rule.** Recorded also as a pattern: this is the
fifth consecutive verdict in which a condition naming `tolerances.py` was answered
at the sites it listed and left something in the same entry wrong. The value is
right and the margin is right; only the way back to them is missing.

**C21. `docs/reports/F2/step-7.md:511` publishes `1.4e-15` and the command it cites
prints `1.5208e-15`.** The other four probes match to two figures; this one does
not, and it is stable — I ran the command twice and got `1.5208e-15` both times,
with a seeded RNG. It is the pre-parameter version of the number, which is the shape
BP0 names: the code moved when `interp` became a parameter and the figure citing it
was republished. **Closed by re-taking the line.** Noted with some care: the
paragraph two screens below it is the one where the same class of error is confessed
and credited to the number-sourcing guard.

**C22. The schedule is slipped in the report and not in the locked plan, and the
triple the report gives for it is refuted by the command inside it.**
`docs/milestones/F2.md:1745-1746` still reads `| **4 October** | F2 closes |` and
`| **9 October** | F3 closes |`. §1 of the report cites
`grep -n "5 October\|10 October" docs/milestones/F2.md` and prints the new DM
dates; I ran it and its only hit is line 1749,
`| **25 October** | the code-check screen |`, matched as a substring. So the one
authoritative record of the dates was re-locked twice this round without the dates
moving. **The slip itself is reported the day it is known, which is what CZ0 asks
for, and I am holding nothing on a date.** Closed by the dates moving in the plan,
in the plan: commit that records DM.

**C23. `docs/closure/F2-step7.md:91` — all 60 rung-2 tests pass on both signs.**
True of the tree at `acb5e8c`; false at the commit that publishes it. Rung 2
collects `66` here and I measured four ids reddening on the injected sign.
**Closed by tensing it to the tree it describes**, or by giving the new count and
the four.

**C24. `floatfea/element/beam.py:211-212` — that is what makes the G2.4 band
one-sided (AO4).** Verdict 62 filed this sentence as part of R541 because AO4 then
said no band was one-sided. AO4 now says the SIGN half is asserted and the ORDER
half is not, so the sentence is half true and does not say which half. The
paragraph added below it at `:216-223` is correct and load-bearing; this line is the
one that did not move with the re-lock. **Closed by naming the half.**

**C25. No outside-witness comment exists on PR #1 for any step of F2.** Fourteen
rounds, the comment array is length `0`. `docs/SUPERVISOR.md:41-46` records steps
1 to 4 as permanently without one; steps 5, 6 and 7 are now in the same condition,
and F2 closes with twenty-eight consecutive reviews written by one reader. Closed by
recording it in the closure artifact as a gap in the record rather than as a
satisfied channel.

**C26. C1 to C19 carry into the closure artifact unchanged**, with C12, C14, C15,
C16, C17 answered and C18 absorbed by the plan re-lock.

## Tolerances touched

**NONE. No constant was created, retired, moved, renamed or revalued.**

```
cmd  every NAME: Final[...] = value at acb5e8c and at 36b5899, diffed
out  48 and 48, byte-identical. added [] removed [] changed []
cmd  git diff acb5e8c..36b5899 -- floatfea/tolerances.py, non-comment +/- lines
out  (empty) -- 25 changed lines, every one a comment
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| — | — | — | **no tolerance value touched this round** | — | — |

`ROUNDOFF_IDENTITY` — value `1e-14` unchanged. Form relative and dimensionless.
Counter `ROUNDOFF_IDENTITY_COUNTER = 1.0e-8`, injected as the non-orthogonal
`I + [theta x]` map at `theta = 1e-4`, with its own bisection table. **The recorded
basis R543 asked for is answered and I re-measured every figure in it**: five spans
`0.54, 0.54, 4.07, 2.02, 4.93` ULP, worst `1.0952e-15` at `L = 1000`, headroom
`9.13x`. The entry says which site sets it. The regenerator it cites prints nothing
— C20, closure, not a value question.

**And a new counter arrived on an existing constant, which is the right way to add
one.** `test_the_SHIPPED_SIGN_FLIP_breaks_the_energy_identity` is the counter for
`ROUNDOFF_IDENTITY` at the five sites of the energy identity, injected as the
shipped sign rather than as an invention. I solved for its detection boundary rather
than sampling one side: the same assertion reddens at a shear-coefficient error of
about `4e-9` relative, and the injected defect is nine decades outside it. **That is
a counter in the sense the guard means — a measured threshold, in the quantity the
assertion itself uses, not one arbitrary perturbation.** `FREE_FREE_FREQUENCY` and
`RIGID_LINK_CONSTRAINT` — still not created; the ruling in verdict 62 stands, and
the order band is on the frozen list in `F2a.md` with its one-line adoption written
out.

## Adversarial corpus (BE3, scoped by DE2 to the element)

**20 new entries, all unseen by the implementer, committed separately at `1731307`.
A new file, `tests/corpus/g24_branch_crossing_members.txt`, batch 12.** The axis is
the branch crossing: members at which the k-th discrete eigenvalue is not the k-th
flexural mode. No batch has touched it, and it is the opposite shape to batch 11 —
there the element was wrong and the checks were blind; here the element is right and
the check is what breaks.

```
cmd  grep -c "^id=" tests/corpus/g24_branch_crossing_members.txt
out  20
cmd  the DN1 energy identity at each entry
out  <= 2.3e-15 on 20 of 20
cmd  the verbatim predicates errors[n][mode] > 0 and after < before, n = 4..128,
     modes 1..3, at each entry
out  g24_false_red=yes on 10 of 20
```

**Coverage measurement. The element is correct on 20 of 20, measured, and the
shipped G2.4 assertion would call 10 of those 20 a defective element** — every one
of the eight members at the `L/D >= 2` admission limit the builder itself names, one
more at `L/D = 1` below it, and one at `L/D = 1000` that is not a branch crossing at
all but the round-off floor of the eigensolver, on the single entry where the
hypothesis DN0 refuted IS the mechanism. **The shipped checks catch 0 of 20 as
defects, which is correct, and that is the point: this batch measures FALSE reds,
not misses.** Nothing in it is red at this commit — the assertion is parametrised on
one geometry and none of these members is in it.

**And the counterweight, because right-every-time is not allowed to become a prior,
and this round it runs in the new direction.** Verdict 62 found an element defect
after sixty-one that did not. This round I could not find another one: four
independent witnesses agree the corrected interpolation is the classical element, a
swept-coefficient probe puts the detection threshold of the new check at `4e-9`
relative, the energy identity is invariant over six decades of length and twelve of
modulus, and the two asymmetric-section attacks I built were refused by validators in
`floatfea/` with the right messages. **The honest statement about the consistent mass
at `36b5899` is stronger than not yet contradicted: it WAS contradicted, the
contradiction was localised to one sign in one line, and the corrected element now
agrees with a witness that shares none of its derivation.** What I found instead is
that the check built to defend it over-claims its own reach, which is R545 — the same
species as R542, one level up.

## On the criterion, said once

**I accept CZ0 and DK2 and I have ruled under both.** R545 is a substantive finding
about a gate and I have classed it as closure rather than blocking, because what the
gate asserts is true where it is asserted and only the sentence beside it
over-reaches. Every other sentence finding is in the closure list. I have one thing
to record and it is not an argument.

**PASS WITH A RED CI IS THE COST OF THE CAP AND IT SHOULD BE VISIBLE IN THE CLOSURE
ARTIFACT, NOT ONLY HERE.** CA2 and DK2 disagree at this commit and DK2 wins by
construction. I think that is the right trade — the ladder is green, all ten
determinism legs are green, the reds are three states in a report-process harness,
and none of them is about the platform or the element. But F2 closes with a red
`lint, unit and guards` job, and the next reader of `docs/closure/F2.md` should learn
that from the artifact rather than from this file. **If the cap were mine I would
have taken one more verdict for R544 specifically, because two of its three reds are
invisible from the machine the implementer works on, and that is precisely the
failure mode CA2 was written for.** That is a remark about the cap and not a HOLD; it
goes to Xabier through the implementer and it does not become another round.

## Carried for the next step — what blocks in F3

- **R544 — BLOCKING, by name, into the first step of F3.** Three red tests at
  `36b5899`, one local and three in CI. Its closing condition is above, site by
  site. **The first step of F3 does not close while it is open.**
- **R545 — carried as a closure item with a site**, and it is the one I would put at
  the top of the list, because the platform model in F3 is what makes it live.
- **C20 to C26, and C1 to C19 from verdicts 61 and 62 — into `docs/closure/F2.md` as
  a list**, absorbed once, not re-reviewed item by item.
- **The 48 frozen `F2a.md` items and R475 / R487 / R488 / R492 / R493 / R500 / R501 /
  R513 / R519 / R521 / R522 / R523 / R524 / R525 / R526 / R527 / R528 / R529 / R533 /
  R535 / R538 / R539 — unchanged on the closure list.**

## Next step opens when

**STEP 7 IS CLOSED AND F2 IS CLOSED, on this verdict, under DK2.** The first step of
F3 may open. The conditions below are for F3, not for step 7, and R544 is the one
that gates it.

1. **R544 is `0 failed` locally AND `lint, unit and guards` is SUCCESS in CI, at one
   commit**, with the rebuilt state demonstrated by the guard going RED on it. This
   is the blocking carry and it is answered before the first step of F3 closes.
2. **`docs/closure/F2.md` absorbs C1 to C26 in one list**, and records two things
   that are about the process rather than the work: that F2 closed with a red CI job
   under the cap in DK2, and that no outside-witness comment was ever posted.
3. **The two sentences and one assertion message in R545** land before any F3 test
   parametrises G2.4 over a platform member. If a stubby brace enters that test
   first, the red it produces is a false red and the message will name the element.
4. **DM0 and DM2 are not covered by this verdict** and neither is reviewed here.
