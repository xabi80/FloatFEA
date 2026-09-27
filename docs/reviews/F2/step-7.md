# Review — F2 step 7
Reviewed commit: 7d47828877d26d8c0b2aa3082583faa790169b7e
Verdict: HOLD

**Reviewed commit: `acb5e8c`. Sixty-second verdict, and the FIRST on step 7.** DK2
allows two, so the next one closes the step. The `Reviewed commit:` line stamped at
the top of this file by `scripts/write_verdict.py` is my corpus commit `7d47828`,
not the commit judged (R513, unchanged).

Tests: **2717 passed, 8 failed, 0 skipped** -- my run, `python -m pytest -q` at
`acb5e8c`, 734.39 s, Python 3.13 on Windows, 2 warnings (both pre-existing, the
`orient_norm_overflow` g22 entry). All 8 failures are the verdict-absence guard and
are cleared by this file existing; see the CI block below. They are NOT the reason
for the HOLD.

**The HOLD is a defect in `floatfea/element/beam.py` and it is not a small one.**
The shear term in `bending_interpolation` has the wrong SIGN. That makes the
consistent mass matrix wrong at `O(Phi)` -- 46% in energy at the builder's own
`L/D = 2` limit -- makes `bending_interpolation` invert a singular matrix at
`Phi = 1`, which is `L/D = 2.64` for a steel tube and therefore inside the
admissible domain, and it is the whole cause of the step's headline finding. With
one variable moved and nothing else, the "the interpolation spaces are not nested"
conclusion evaporates: the largest rise in any frequency under refinement goes from
`1.476e-04` and `7.924e-05` to **`0.000e+00`** in both boundary conditions.

## Item 1b -- CHECKED, AND CLEAN

```
cmd  the newest Answers line in the report under review
out  docs/reports/F2/step-7.md:4 -- "Answers: verdict 61 @ 52941f7"
cmd  git log --oneline --follow -- docs/reviews/F2/step-6.md | head -1
out  52941f7 review: F2 step 6 -- sixty-first verdict, PASS @ 792c44e
judge THE HEADER NAMES THE LATEST. One comparison, made, it matches, so every
     Carried claim in the report is about the right list.
```

## CI (3b) -- and thank you for dispatching it

```
cmd  gh run list --commit acb5e8c --json name,conclusion,workflowName
out  []  -- the commit filter returns nothing again, the same quirk as at
     792c44e. Recorded so the next reader does not read it as an absent run.
cmd  gh run view 36292692101 --json status,conclusion,headSha,event,jobs
out  completed failure  headSha acb5e8cd...  workflow_dispatch
     the verification ladder             success  13 steps
     CI determinism -- leg (1)..(10)     success  13 steps each
     CI determinism -- ten legs agree    success   4 steps
     lint, unit and guards               FAILURE  13 steps
cmd  gh run view 36292692101 --log-failed, failing names deduplicated
out  8 names, ALL of them:
       test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
       test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
       ...[non_numeric_step_suffix] [superscript_digit_step_number]
       ...[draft_suffix_beside_a_step_report] [step_number_is_the_empty_string]
       ...[verdict_amended_after_the_commit_the_report_answers]
       ...[zero_padded_step_number]
judge REAL STEP COUNTS AND A REAL RUNNER -- this is not CK2. The verification
     ladder is SUCCESS at the reviewed commit, and so are all ten determinism
     legs and the agreement job, which is C12 answered on a tree that contains
     the new per-frame eigenvalue assertion. **The eight red names are one cause,
     and it is this verdict's absence**: I reproduced them locally and every one
     traces to `test_report_carried.py:417`, "step 7 has a report and no verdict
     yet ... Invoke the gating-supervisor." NOT (d), and I am not holding on it.
cmd  python -m pytest tests/test_report_guard_states.py tests/test_report_carried.py
     tests/test_report_numbers_are_sourced.py -q   (at acb5e8c, my run)
out  8 failed, 218 passed
judge **AND THIS IS WHAT I WANT INSTEAD, SINCE YOU ASKED.** Your invocation says
     "my local run of the two report guards at acb5e8c is 1 failed, 199 passed,
     and that is the one failure." There are THREE report-parametrised files --
     the report's own section 5 names all three -- and the third contributes
     seven of the eight. The number is not wrong about anything that matters and
     the cause is identical; the accounting is short by one file. Re-take that
     line over all three. **Closure item C14, not (d).**
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, thirteenth round.
```

## My own instructions (4b), conftest (4c), tolerance VALUES (4)

```
cmd  git diff 792c44e..acb5e8c -- .claude docs/SUPERVISOR.md
out  (empty). NOT A STOP on this head.
cmd  git ls-files -- the conftest pathspec, both halves
out  tests/conftest.py   -- the instruction's own expectation, met
cmd  git diff 792c44e..acb5e8c -- the same pathspec
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added and no rung
     grew a conftest, so the CH2/CI0 channel is closed by inspection this round.
     60 new tests entered rung 2 and none of them arrived with a hook.
cmd  for each commit in 792c44e..acb5e8c: does it touch floatfea/ AND docs/reviews/?
out  none. 52941f7 is verdict 61, alone.
cmd  git diff 792c44e..acb5e8c -- floatfea/tolerances.py, non-comment +/- lines
out  (empty). 72 changed lines, every one a comment.
cmd  every NAME: Final[...] = value at 792c44e and at acb5e8c
out  48 and 48; added [] removed [] changed []. NOT ONE VALUE MOVED.
```

## Carried

Verdict 61 was a PASS that CLOSED step 6, carrying **R540** as blocking by name,
C1 to C13 as closure items, and conditions 3 and 4.

- **R540 -- ANSWERED, at `d147f25`, and I checked both halves against the diff.**
  (1) `floatfea/tolerances.py:389-431` now states both directions explicitly --
  AS A FLOOR ON lambda_7, AS A CEILING ON lambda_6 per frame at
  `test_rigid_body_corpus.py:230`, and IT IS ONE CONSTANT AND NOT TWO -- and the
  paragraph WHAT CARRIES THE CEILING'S PREMISE retires the Courant-Fischer
  citation of the residual half by name. (2) The sensitivity split is published
  where the gate's claim is stated, as the *command* rather than as a table
  (`python scripts/rigid_counter_response.py`, BI3's exit), and the entry says in
  terms that one of the three shapes reddens no frame at any size the script
  reaches, four decades above the injection. That is the precise sentence the
  condition asked for. **No value moved**, which was the condition.
- **Section 3's twelve rows for R540's sites -- ACCEPTED AS RECORDED.** You asked
  whether I want them differently. No. ANSWERED AND THE BLOCK MOVED, not no
  change because the lines did change, is the honest row for a rewritten block,
  and it is the first time in four verdicts that this table has not carried a
  reason copied from a different finding. Leave it.
- **Condition 3 (one `workflow_dispatch` so the determinism legs describe the
  tree) -- MET**, at `36292692101`, ten legs plus the agreement job all success at
  the reviewed commit. One caveat for the record and not a finding: ten legs
  agreeing is a statement about reproducibility, not about correctness, and R541
  below is a matrix all ten legs agree on.
- **Condition 4 (`0 failed` locally and a completed SUCCESS on a push touching
  code) -- NOT MET, and correctly not met.** 8 failed locally, one cause, this
  verdict's absence; and the last push that touched code, `9bc35bc`, is a failure
  for the same cause. I am treating neither as (d) and I say so above.
- **C1 to C13 -- closure items, carried, NOT re-reviewed item by item** per CZ0.
  C12 is answered (above). C2, C3, C4 and C13 are recorded as answered at
  `83bc146`; I did not re-measure them and do not need to.
- **R475 / R487 / R488 / R492 / R493 / R500 / R501 / R513 / R519 / R521 / R522 /
  R523 / R524 / R525 / R526 / R527 / R528 / R529 / R533 / R535 / R538 / R539 and
  the 48 frozen 4a items -- OPEN on the closure list, none re-reviewed.** The
  report's section 4 note that `carried_table.py` and `test_report_carried.py`
  disagree about R523, R524, R525 and R528 is correct, is recorded rather than
  papered over, and is a closure item (C15).

## Findings

**What I tried hardest to break is the cell your invocation asked me to break, and
it broke.** Six cells, all at `acb5e8c`, all run from the session scratch directory
outside the repository. Nothing I ran is in the tree.

```
cell ONE VARIABLE, and it is a SIGN. Is the field `bending_interpolation` returns
     the field whose strain energy is the shipped `bending_stiffness`
     (Przemieniecki eq. 5.36)? The two are the same object -- eq. 5.36 IS the
     exact strain energy of the exact homogeneous Timoshenko field -- so
     q^T k q must equal the analytic integral
     int EI th'^2 dx + kappa G A gamma^2 L for every nodal q. Measured over 8
     random q, at the two candidate signs of the shear term: alpha = +1/6
     (shipped, `+ phi * xi / 6`) and alpha = -1/6.
out  Phi       alpha = +1/6 (SHIPPED)      alpha = -1/6
     1e-3          3.634e-03                1.782e-15
     1e-2          3.711e-02                2.535e-15
     0.1           2.799e-01                3.140e-15
     1.0           9.071e-01                2.028e-15
     5.0           5.554e-01                1.605e-14
judge THE SHIPPED SIGN IS WRONG AND THE OTHER ONE IS EXACT. The mismatch is
     O(Phi) and it is not a subtlety: at Phi = 1 the mass matrix belongs to a
     field carrying 91% the wrong strain energy for the stiffness beside it.
cell THE SAME THING FROM THE PHYSICS SIDE, because an algebra check can share an
     error with the algebra. Cantilever, one element, tip shear P: the deflection
     must be P L^3 / 3EI + P L / kappa G A -- bending and shear ADD. Solved for
     alpha rather than sampled.
out  w(L) = P L^3/(3 EI) - 6 alpha P L/(kappa G A)  =>  alpha = -1/6.
     The shipped alpha = +1/6 SUBTRACTS the shear deflection.
judge The standard Timoshenko pair is d/dx(EI psi') + kappa G A (w' - psi) = 0,
     so V = -EI psi'' and w' = psi - c psi'' with c = EI/kappa G A. The module
     comment derives M' = V and gets w' = psi + c psi''. One sign.
cell THE DETERMINANT OF THE MAP THE MODULE INVERTS, solved rather than sampled.
     `T` at `beam.py:243-251`.
out  det(T) = L (1/6 - alpha Phi) ... shipped alpha = +1/6  =>  L (1 - Phi)/6
                                      corrected alpha = -1/6 => L (1 + Phi)/6
     Phi:      0      0.5     0.9     1.0      1.1      2.0
     shipped  1.250  0.625   0.125  0.000   -0.125   -1.250
     correct  1.250  1.875   2.375  2.500    2.625    3.750
judge THE SHIPPED PARAMETRISATION IS SINGULAR AT Phi = 1 AND THE SIGN OF ITS
     DETERMINANT FLIPS ABOVE IT. The corrected form gives (1 + Phi), which is
     exactly the denominator the classical shear-flexible shape functions carry
     and never vanishes for Phi >= 0. That agreement is the third independent
     witness.
cell YOUR OWN CELL, RE-RUN THROUGH YOUR OWN HELPERS
     (`test_consistent_mass._bending_frequencies` and
     `._pinned_pinned_frequencies`, imported, not reimplemented), with ONE
     variable moved -- the sign -- and the same beam, meshes and eigensolver.
out  SHIPPED   w += +Phi xi/6 : free-free rise 1.476e-04  pinned-pinned 7.924e-05
     CORRECTED w += -Phi xi/6 : free-free rise 0.000e+00  pinned-pinned 0.000e+00
judge **THE TWO FIGURES THE REPORT PUBLISHES AS THE PROOF THAT RAYLEIGH-RITZ DOES
     NOT APPLY TO THIS ELEMENT FAMILY ARE REPRODUCED EXACTLY, AND THEY GO TO
     ZERO WHEN THE SIGN IS FIXED.** They are the defect, not a property of the
     family.
cell AND NESTING DIRECTLY, because the conclusion deserves a measurement that
     does not go through an eigensolver. (i) Sample the coarse element's four
     (w, theta) shape functions on [0, L/2] at 41 points and least-squares them
     onto the fine element's four with Phi(L/2) = 4 Phi(L). (ii) Build the exact
     prolongation P -- coarse nodes to even fine nodes, midpoints interpolated
     by the element's own shape functions -- and compare P' K_f P and P' M_f P
     with K_c, M_c on the shipped 30 m beam.
out  (i) ||coarse - fine c|| / ||coarse|| = 3.907e-16, fine rank 4, and per
         shape function 2.4e-16 .. 4.3e-16
     (ii) n= 4->8   ||P'K_fP-K_c||/||K_c|| = 6.750e-05   mass 5.180e-16
          n= 8->16                          1.096e-03          6.067e-16
          n=16->32                          2.233e-02          2.894e-16
          n=32->64                          2.523e+00          4.622e-16
judge THE SPACES ARE NESTED AND THE REASON IS STRUCTURAL: Phi = 12 c / L^2 with
     c = EI/kappa G A, so the element's field family is
     {theta in P2, w' = theta -+ c theta''} -- a condition with NO L in it. The
     Phi-dependence is the dimensionless rendering of a length-independent
     constant, which is why Phi(L/2) = 4 Phi(L) exactly and why the family cannot
     depend on the mesh. The MASS nests to round-off at every level. The
     STIFFNESS does not nest against this prolongation, and diverges as the mesh
     refines, because the prolongation uses the shipped interpolation and the
     stiffness does not come from it. That split -- mass 5e-16, stiffness 2.5 --
     localises the defect to the interpolation and clears eq. 5.36.
cell THE STUBBY BEAM, which is the case the guard tells me to construct. Thin
     tube D=0.3 t=0.008 steel, at and around the builder's L/D >= 2.
out  L/D = 2.00  L=0.600 m  Phi=1.742   energy mismatch 4.62e-01
     L/D = 2.64  L=0.791934845805 m  Phi=1.000000000000
                 local_mass RETURNS, max|m| = 1.62e+30 for a 46 kg member
     Phi = 1.000001   max|bending_mass| / max|bending_mass(Phi=0)| = 2.52e+10
     Phi = 1.01                                                     2.51e+02
     and D=3.0 t=0.001 at Phi = 1: local_mass RAISES LinAlgError: Singular matrix
judge A MEMBER THE BUILDER ADMITS PRODUCES A MASS MATRIX OF 1e30 OR AN EXCEPTION.
     L/D >= 2 is F2.md section 5i's own limit and Phi = 1 sits at L/D = 2.64 for
     every steel tube, because Phi ~ 62 (r/L)^2 / kappa is section-independent to
     first order. This is not a corner of the domain; it is the middle of the
     stubby end of it.
cell AND WHY NOTHING IN THE TREE SEES ANY OF THIS -- assertion domain blindness,
     measured rather than argued. The verbatim bodies of
     `test_the_six_RIGID_BODY_inertias_of_ONE_ELEMENT_are_exact` and
     `test_the_MODEL_rigid_body_block_is_the_ANALYTIC_mass_and_inertia`,
     evaluated at each of my 15 corpus members.
out  green on 10 of 15, RED on 4, raises on 1. The 4 are within 1e-7 of Phi = 1
     and are caught by arithmetic blow-up, not by the sign. Every member at
     L/D = 2 is GREEN with an energy mismatch of 0.46.
     The shipped parametrisation of the rigid-inertia test ALREADY RUNS at
     Phi = 2.509 (D=0.3, t=0.008, L=0.5) and Phi = 10.169 (D=0.6, t=0.012,
     L=0.5) and passes both.
judge THE FOUR CHECKS V2.5 SHIPS ARE ALL EVALUATED WHERE THE SHEAR TERM
     MULTIPLIES NOTHING. The Euler-Bernoulli checkpoint is at Phi = 0 by
     construction. The six rigid-body inertias and Phi^T M Phi are quadratic
     forms of vectors whose cubic coefficient c3 is zero, and c3 is the only
     coefficient the shear term multiplies. So the Phi-dependent half of the
     matrix -- the entire reason a Timoshenko mass matrix is not an
     Euler-Bernoulli one -- is asserted by nothing, and the two counters, a
     lumped mass and a dropped coupling block, are both blind to it too.
```

---

**R541. (BLOCKS -- (a), and it is the step's substance.) THE SHEAR TERM IN
`floatfea/element/beam.py:bending_interpolation` HAS THE WRONG SIGN. THE CONSISTENT
MASS MATRIX IS WRONG AT O(Phi), IT IS SINGULAR AT Phi = 1 WHICH IS L/D = 2.64 AND
INSIDE THE ADMISSIBLE DOMAIN, AND THE STEP'S HEADLINE FINDING -- THAT THE
INTERPOLATION SPACES ARE NOT NESTED -- IS THIS DEFECT AND NOT A PROPERTY OF THE
ELEMENT FAMILY.**

```
cmd  floatfea/element/beam.py:247 and :253, read today
out  [1.0, ll, ll / 2.0, ll * (1.0 / 3.0 + phi / 6.0)]
     [1.0, ll * xi, ll * xi**2 / 2.0, ll * (xi**3 / 3.0 + phi * xi / 6.0)]
     and the module comment at :186-188 deriving it:
       V' = 0 => V constant ; M' = V, M = EI th' => th quadratic ;
       w' = th + V/(kappa G A) => w cubic
cmd  the six cells above
out  energy vs eq. 5.36: 3.6e-03 .. 9.1e-01 shipped, <= 2.0e-14 corrected;
     the cantilever solves alpha = -1/6; det(T) = L(1-Phi)/6 shipped and
     L(1+Phi)/6 corrected; your own rise figures 1.476e-04 and 7.924e-05 go to
     0.000e+00 and 0.000e+00; nesting residual 3.907e-16; local_mass max|m| =
     1.62e+30 at Phi = 1
cmd  grep -rn "bending_interpolation" floatfea tests scripts
out  beam.py:232 (its definition) and beam.py:276 (bending_mass). NOTHING ELSE.
judge THE BLAST RADIUS IS THE CONSISTENT MASS MATRIX AND EVERYTHING DOWNSTREAM OF
     IT -- every frequency in this repository, G2.4 in all three of its
     assertions, the V6.1 golden's mass rows, and F3's G3.1a inertia
     reconciliation. The STIFFNESS is clean: it is eq. 5.36 transcribed and my
     cell certifies it against the corrected field to 2e-14. **The default
     hypothesis is that the code is wrong and this time it is.**
```

  **Closed when**, site by site: (1) `floatfea/element/beam.py:247` and `:253`
  carry `- phi / 6.0` and `- phi * xi / 6.0`, and the module comment at `:180-190`
  derives w' = theta - c theta'' from d/dx(EI psi') + kappa G A (w' - psi) = 0
  rather than from M' = V; (2) a shipped assertion compares the strain energy of
  `bending_interpolation`'s field against q^T k q for the same member at a Phi
  that is not zero -- this is an assertion on an existing quantity, not new
  apparatus, and it is the one check that would have caught this; (3) Phi = 1 and
  L/D = 2 are in the parametrisation of whatever asserts (2), so the singular case
  is evaluated rather than avoided; (4)
  `test_the_SHIPPED_element_approaches_its_OWN_continuum`'s `asserted = (4, 8, 16)`
  at `:891` extends over the whole reported range -- with the sign corrected the
  error against the exact Timoshenko reference falls monotonically from `2.74e-04`
  to `1.08e-08` through n = 256 in mode 1 and at every mode, measured, so the
  truncation is no longer needed; (5) the V6.1 golden is regenerated with the
  explanation of why the mass invariants moved, which is the case its own docstring
  says the explanation is for.

---

**R542. (BLOCKS -- (c).) `test_the_SHIPPED_element_approaches_its_OWN_continuum`
ASSERTS OVER n = 4, 8, 16 AND REPORTS n = 32, 64, 128, AND THE STATED REASON FOR
STOPPING AT 16 IS THE DEFECT IN R541. THE DOMAIN OF THE ONLY Phi != 0 ASSERTION
AGAINST A REFERENCE WAS NARROWED UNTIL THE FAULT FELL OUTSIDE IT.**

```
cmd  tests/verification/rung2/test_consistent_mass.py:865-872 and :891
out  "The range stops at 16 and the reason is measured, not chosen -- beyond it
     the non-nested wobble ... is the same size as the discretisation error, and
     the error changes sign at n=32."
     asserted = (4, 8, 16)
cell ONE VARIABLE, the sign, over the FULL reported range, modes 1 / 2 / 3
out  SHIPPED    n=  4 +2.6222e-04  +3.9809e-03  +1.8350e-02
                n= 16 +8.9198e-07  +1.4212e-05  +7.1431e-05
                n= 32 -8.1685e-07  -1.3098e-05  -6.6539e-05   <- the sign change
                n=256 +8.1368e-09  +1.0619e-07  +5.3575e-07
     CORRECTED  n=  4 +2.7397e-04  +4.1574e-03  +1.9198e-02
                n= 16 +1.9494e-06  +3.1023e-05  +1.5566e-04
                n= 32 +2.9424e-07  +4.6956e-06  +2.3651e-05
                n=256 +1.0816e-08  +5.7878e-08  +2.9050e-07
judge THE SIGN CHANGE AT n = 32 IS THE DEFECT. Corrected, the error is positive
     and falling at every mesh from 4 to 256, so `after < before` holds over the
     whole range and there is nothing to truncate. The narrowing is not itself
     dishonest -- the reason given is a real measurement and it is written down --
     but it is the shape the guard names: a test correct about a domain that
     excludes the fault. **It also passes on BOTH sides**: my table shows
     `after < before` over 4 -> 8 -> 16 for the shipped AND the corrected element,
     so this assertion certifies nothing about the sign either.
```

  **Closed when** the assertion covers the range the test prints, on the corrected
  element, and the docstring's account of why the range is what it is matches what
  the code does. This closes with R541 and is listed separately because it is a
  gate assertion and would still be a finding if R541 were somehow wrong.

---

**R543. (BLOCKS -- (b).) `ROUNDOFF_IDENTITY`'s RECORDED BASIS IS FALSIFIED BY THE
SITES THIS STEP ADDED TO IT, IN THE ENTRY THIS STEP'S OWN CLOSURE COMMIT REWROTE.**

```
cmd  floatfea/tolerances.py:1375-1382, read today
out  "Worst measured across its sites is one ULP, 2.2204e-16, and 1e-14 sits ~45x
     above that."
     and immediately below it, added at d147f25:
     "THE SITE COUNT IS NOT WRITTEN HERE (BI3). It said its nine sites, and step 7
     added more when V2.5's Euler-Bernoulli limit and its six rigid-body inertias
     came to this constant"
cmd  the five spans of test_the_PHI_ZERO_limit_reproduces_the_TRANSCRIBED_mass_matrix,
     measured through the shipped bending_mass and euler_bernoulli_bending_mass
out  L=0.5      1.1956e-16  = 0.54 ULP
     L=1.0      1.1956e-16  = 0.54 ULP
     L=3.7      9.0480e-16  = 4.07 ULP
     L=40.0     4.4764e-16  = 2.02 ULP
     L=1000.0   1.0952e-15  = 4.93 ULP   <- the new worst
     headroom against 1e-14: 9.13x, not 45x
cmd  the report's own V2.5 paragraph
out  "the Phi->0 limit against an independently transcribed Euler-Bernoulli
     consistent mass (1.1e-15 worst over five spans)"
judge THE NUMBER WAS MEASURED AND PUBLISHED IN THE REPORT AND NOT CARRIED INTO THE
     ENTRY. The commit that added the new-sites-arrived paragraph is the commit
     that left the measurement one line above it stale. **No value need move** --
     9.13x is adequate headroom for a round-off identity and I am not asking for
     1e-13 or for 1e-15. What must move is the recorded basis, because BD1's own
     paragraph in this entry says the value is set by the tightest member of the
     group, and a reader who trusts one ULP and 45x will make the next decision on
     a margin five times smaller than stated. This is the fourth consecutive
     verdict in which a condition naming `floatfea/tolerances.py` was answered at
     the sites it listed and left at a site in the same entry.
```

  **Closed when** `floatfea/tolerances.py:1380-1382` states the worst measured
  across its sites at the commit that publishes it, with the headroom recomputed,
  and says which site sets it -- or cites the command that produces it, which is
  BI3's other exit and the one the same entry already took for the site count.
  **Note this figure moves again when R541 lands**, because the Euler-Bernoulli
  limit is taken at Phi = 0 where the sign is irrelevant and I expect it
  unchanged, but the rigid-inertia and Phi^T M Phi sites are not. Re-take it after
  the fix, not before.

---

**On the two tolerances that were NOT created -- you asked and I have checked both.
NEITHER BLOCKS.**

```
cmd  git diff 792c44e..acb5e8c -- floatfea/tolerances.py, added constants
out  (empty) -- no constant was created
cmd  grep -n "ROUNDOFF_IDENTITY|pytest.raises" tests/verification/rung2/test_releases_and_links.py
out  every assertion in the file is <= ROUNDOFF_IDENTITY, > ROUNDOFF_IDENTITY (the
     counters), or pytest.raises -- 2 raises, 4 counters, 12 identities
judge `RIGID_LINK_CONSTRAINT` NOT CREATED IS CORRECT AND IS THE TIGHTER DIRECTION,
     for the reason you give: a kinematic transfer is exact in exact arithmetic, so
     a round-off identity is a stronger assertion than any engineering band, and a
     new constant would have had to be looser. The counters are asserted as strict
     exceedances with their magnitudes printed, which is the right form. Accepted.
     `FREE_FREE_FREQUENCY` NOT CREATED does not block either, but the tighter
     direction overstates it: an assertion that does not exist is not tighter than
     one that does, it is absent. What replaced it -- strict monotone error
     reduction and a strict ordering -- is genuinely threshold-free and cannot be
     widened, and that is the honest statement. The reason the band was withdrawn
     is R541 and not the element family, so its absence is a consequence of the
     defect rather than a decision about the element, and AO4 is re-argued after
     the fix. **That is a plan question, not a value question; it does not block
     this step and it needs no new apparatus.**
```

**On rho (I_y + I_z) versus rho J -- you asked me to rule and you are RIGHT, and it
is not close.** J is the St-Venant torsion constant, a stiffness property defined by
the warping problem; the rotary inertia of a cross-section about the member axis is
its polar SECOND MOMENT OF AREA, I_y + I_z, by the definition of a mass moment of
inertia. They coincide for a circular tube and diverge for everything F3 introduces.
That is a fact about what the two symbols mean, not a choice this project could have
made differently, so it does not belong in `docs/conventions.md` and the docstring at
`beam.py:299-308` is the right place for it. **Not a finding, and the sentence saying
that using J would put the error only on the sections F3 introduces is correct and
worth keeping.**

**On V6.1 excluding frequencies -- honest, and weaker than it needs to be.** The
stated reason (`tests/regression/test_f2_shipped_matrices.py:16-25`) is that the
cross-platform `eigh` drift is unmeasured. The guard is honest: it says which of the
two forms it is, names the tighter neighbour, and says what taking the measurement
would cost. But "the cross-platform drift is a measurement nobody has taken" is a
prose claim about this repository with no triple, and the ten-leg determinism job
that ran green at this very commit is the apparatus that would take a large part of
it. Closure item C16, and I am not holding a step on the scope of a golden. **What I
will say plainly: with R541 open, the one quantity V6.1 excludes is the quantity most
sensitive to the defect, and the three summaries it does record on the mass matrices
are the ones that WILL move when the sign is fixed.** That is the golden working.

**And one prose finding I am classing as part of R541 rather than as closure, because
it is the only statement of the derivation the mass matrix rests on.**
`floatfea/element/beam.py:170-175` says the interpolation spans exactly the space the
exact stiffness eq. 5.36 is built from, so stiffness and mass are a conforming
Rayleigh-Ritz pair, and **that is what makes G2.4's band one-sided (AO4)**. Both
sentences are false as of `258e26e`, which rewrote AO4 to say no band is one-sided,
and the first is false as arithmetic -- my first cell measures the two spaces
disagreeing by up to 0.91. `git log --oneline 0ffd6bd..258e26e` shows the plan re-lock
landing two commits after the module comment, which is BP0's shape exactly: a
decision rule moved and the sentence citing it was republished unchanged.

## Closure items (CZ0). None of these is (a), (b), (c) or (d).

**C14. The invocation's report-guard count is short by one file.** "the two report
guards ... 1 failed, 199 passed"; there are three, the report's own section 5 names
them, and the third contributes seven of the eight failures. Same cause, cleared by
this verdict. Closed by re-taking the line over all three files.

**C15. `scripts/carried_table.py` and `tests/test_report_carried.py` disagree about
R523, R524, R525 and R528.** Recorded in section 4 rather than papered over, which is
the right response; the generator's docstring still claims it uses the same rule as
the guard. Closed by the docstring saying which rule it uses.

**C16. `tests/regression/test_f2_shipped_matrices.py:21` -- the sentence that the
cross-platform drift is a measurement nobody has taken is a CW0 claim with no
triple**, and the ten-leg determinism job is part of the apparatus that would take
it. Closed by a triple or by deleting the sentence.

**C17. `tests/verification/rung2/test_consistent_mass.py:786-789 -- cell ONE
VARIABLE: Phi MOVES TWO.** `sequences(no_phi=True)` patches `shear_parameter -> 0.0`
AND rewrites `bending_mass` to pass `rho_i = 0.0`, so the Phi = 0 leg has no rotary
inertia either. BG0 asks for one variable. It does not change the conclusion of R541
-- my own cell moves only the sign and is decisive -- but the published cell does not
isolate what it says it isolates. Closed by turning rotary inertia off in both legs
or in neither.

**C18. `docs/milestones/F2.md:161-177` publishes the non-nesting conclusion as a
locked plan section**, and `tests/verification/rung2/test_consistent_mass.py:18-49`
and `:508-516` as module prose. All of it is downstream of R541 and is withdrawn or
rewritten with it. Listed as closure because it is prose; the substance is R541 and
condition 5 below.

**C19. C1 to C13 from verdict 61** carry into the closure artifact unchanged, C12
answered.

## Tolerances touched

**NONE. No constant was created, retired, moved, renamed or revalued.**

```
cmd  every NAME: Final[...] = value at 792c44e and at acb5e8c
out  48 and 48. added [] removed [] changed []
cmd  git diff 792c44e..acb5e8c -- floatfea/tolerances.py, non-comment +/- lines
out  (empty) -- 72 changed lines, every one a comment
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance value touched this round** | -- | -- |

`ROUNDOFF_IDENTITY` -- value `1e-14` unchanged, form relative and dimensionless,
counter `ROUNDOFF_IDENTITY_COUNTER = 1.0e-8` injected as the non-orthogonal
I + [theta x] map at theta = 1e-4 with its own bisection table. **The entry gained
sites this step and its recorded worst was not re-taken: R543.** The real worst at
this commit is `1.0952e-15` at the L = 1000 span of the new Euler-Bernoulli
checkpoint, 9.13x of headroom where the entry claims 45x.

`RIGID_MODE_BOUND` -- value `199.526231496888` unchanged. Its entry now states both
directions and no longer cites the retired residual half: **R540 answered.**

`FREE_FREE_FREQUENCY`, `RIGID_LINK_CONSTRAINT` -- not created. Ruled on above;
neither omission blocks.

## Adversarial corpus (BE3, scoped by DE2 to the element)

**15 new entries, all unseen by the implementer, committed separately at `7d47828`.
A new file, `tests/corpus/g24_consistent_mass_members.txt`, batch 11.** The axis is
the shear parameter Phi, which no batch has touched, and the shape is the stubby
member at and around the builder's own L/D >= 2.

```
cmd  grep -c "^id=" tests/corpus/g24_consistent_mass_members.txt
out  15
cmd  the verbatim bodies of the two shipped geometry-taking V2.5 checks, evaluated
     at each entry
out  green 10, RED 4, raises 1
```

**Coverage measurement. The shipped checks catch 4 of 15 and raise on 1, and the 4
are not caught for the right reason** -- each is within 1e-7 of Phi = 1, where the
singular parametrisation blows the matrix up far enough to break even the rigid-body
quantities. On the other 10, including every one of the five members at L/D = 2 where
the energy mismatch is 0.46, every shipped check is green. **The checks in the tree
caught 0 of 15 for the reason that matters.**

**And the counterweight, because right-every-time is not allowed to become a prior --
except this round it runs the other way and I should say so.** Sixty-one verdicts
found no element defect. This one did, in the first commit of new element mathematics
since step 4, and it was found by asking a question none of the four shipped checks
asks: does the interpolation the mass matrix integrates belong to the stiffness
beside it? The element's rigid-body behaviour is still exact -- 1.62e+30 entries and
all -- which is precisely why sixty-one rounds of rigid-body assertions could not
have found this. Not yet contradicted was the strongest statement available about the
element last week; this week the statement about the CONSISTENT MASS is
"contradicted, and the contradiction is localised to one sign in one line." The
stiffness is unaffected and I checked it independently.

## On the criterion, said once

**I accept CZ0 and DK2 and I am ruling under both.** Nothing in this verdict is a
finding about prose that holds the step -- R541 is `floatfea/`, R542 is a gate
assertion, R543 is a tolerance's recorded basis, and every sentence finding is in the
closure list. I have one thing to say that is not an argument with the criterion.

**The no-new-apparatus-through-F6 freeze and R541 pull against each other, and I am
resolving it in the freeze's favour, but the resolution should be visible.** The one
check that would have caught this defect -- comparing the strain energy of the
interpolation against q^T k q at a non-zero Phi -- is four lines and is not a
scanner, a detector or a generator. I have written R541's condition (2) as an
assertion on an existing quantity for exactly that reason, and I believe that is
inside the freeze. If the implementer reads it as outside, it goes on `F2a.md` and the
fix ships without it; I would rather have the fix than the check. Recorded because the
next reader should know the freeze was considered and not forgotten.

## The schedule

**4 October does not obviously hold any more, and this is the day it is known, so I am
saying it rather than waiting for the step to close.** R541 is one sign in one line
and the fix is minutes. What is not minutes: the V6.1 golden regenerates, the G2.4
assertions in `test_consistent_mass.py` are re-derived over a range that now extends
to n = 256, AO4 is re-argued in a `plan:` commit because its stated reason for
withdrawing the one-sided band was a non-nesting that does not exist, and the closure
artifact absorbs C14 to C19. DK2 gives one more verdict. **The choice CZ0 asks for,
stated: either 4 October slips by the time the AO4 re-lock takes, or G2.4's physics
assertion ships as the ordering plus the corrected convergence and the one-sided band
goes to F3 with the re-lock.** I have no vote on which; both are defensible and the
second keeps the date. What is not defensible is shipping the mass matrix as it
stands, because F4's inertia relief and F3's G3.1a both read it and neither would
catch this.

## Next step opens when

**Step 7 stays OPEN. This is verdict 1 of the 2 DK2 allows, so the next verdict closes
F2 whatever it says** -- which means everything below lands in one commit series, and
anything still open then carries by name into F3's first step.

1. **R541 -- the sign, all five of its sites**: `beam.py:247`, `:253`, the module
   comment at `:180-190`, an assertion at non-zero Phi, and Phi = 1 and L/D = 2
   inside its parametrisation.
2. **R542 -- the asserted mesh range covers the reported one** on the corrected
   element.
3. **R543 -- `ROUNDOFF_IDENTITY`'s recorded worst and headroom re-taken** at the
   commit that publishes them, AFTER the fix, or replaced by the command.
4. **The V6.1 golden regenerated with the written explanation** of why the mass
   invariants moved, in the closure artifact, per its own docstring.
5. **AO4 re-argued in a standalone `plan:` commit**, because `F2.md:161-177` gives a
   reason for withdrawing the one-sided band that does not exist. Whether the band is
   adopted or deferred to F3 is the implementer's call with Xabier; what cannot stand
   is the locked plan asserting a non-nesting this verdict measured at `0.000e+00`.
6. **C14 to C19 in one closure commit**, not re-reviewed item by item.
7. **`python -m pytest -q` is `0 failed` apart from the verdict-absence guards, and
   the verification ladder is SUCCESS on CI** at a commit whose push touches
   `floatfea/`. The ladder is rung 2 now and it is declared FULL, which is the one
   thing in this step that worked exactly as designed:
   `test_every_test_in_the_suite_is_run_by_some_ci_job` caught 60 tests running in no
   CI job, and `add3beb` deleted the `.empty-by-design` marker in the same commit that
   changed the declaration. Recorded as a guard earning its keep.
