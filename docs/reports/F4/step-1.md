# F4 step 1 — load mapping

<!-- step-under-execution marker lives in docs/milestones/F4.md -->

# Revision 1 — the mapping, the static and dynamic cases, and EK4's preview

**2026-10-05.**

## 1. The reading

**Measured against EK4's preview target of 8 Oct: HELD, three days early.** F4 is
committed for 19 Oct with a working target of 14 Oct and both hold. No slippage to
report today.

## 1a. There is no CI section, and the generator says why

```
cmd    python scripts/ci_section.py
out    ci_section: no numbered verdict under docs/reviews/F4, so there is no reviewed
out    commit to anchor on. F4 carries the step marker and has not been reviewed yet --
out    the CI section is written at the first revision that answers a verdict, and
out    there is none.
rule   CX0: sections 0 and 0a are generated or they are not written
judge  SO THE ABSENCE IS DESIGNED, and the generator declares it in words rather than
       raising something a reader has to interpret. This report names no verdict and
       carries no CI table because there is no F4 verdict to answer; the first
       revision that answers one carries both.
```

## 1b. The first-report-of-a-MILESTONE boundary, traced by name

EG3's state (1) is written for a step boundary INSIDE a milestone, where a verdict
exists in the same directory. At a MILESTONE boundary nothing does: the guards resolve
the verdict path to `step-0.md` under this milestone's review directory when no
numbered verdict is there, that file does not exist, so `VERDICT_TEXT` is empty and
every guard parsing findings, sites or pointers from it has nothing to read. **That is
wider than state (1)'s named list and I am not claiming its carve-out.**

```
cmd    the three report-parametrised files, clean clone outside OneDrive, origin
         resolving, at the tree this commit lands
out    43 failed
out      22 x tests/test_report_carried.py
out      19 x tests/test_report_guard_states.py
out       2 x tests/test_report_vocabulary_corpus.py
rule   EG3(i): every red traces BY NAME, and "only those" carries the FAILED list as
       its command
judge  ONE CAUSE. Each of the 22 in the first file either parses findings,
       sites or pointers out of `VERDICT_TEXT` -- which is empty -- or asks for a CI
       section that section 1a shows the generator declines to write. The 19
       states cascade off a red baseline, whose own failure line is one of those. The
       2 vocabulary rows judge the spelling of a `Carried` table the
       generator produced with no verdict to read.
judge  **AND ONE OF THE STATES IS THIS CONDITION'S OWN CONTROL.**
       `newest_report_has_no_verdict_yet` exists to plant exactly the situation the
       tree is now really in -- so the plant changes nothing and the state cannot
       discriminate. That is the vacuous-control shape of R657/R658 arriving from the
       other direction: not a locator that misses its target, but a target the tree
       already occupies. It is reported, not repaired: DR1 freezes apparatus and EK2
       permits repairing a LOCATOR, which this is not.
```

**The full list, so "only those" is checkable rather than asserted:**

```
  test_report_carried.py::test_the_report_names_the_verdict_it_answers
  test_report_carried.py::test_a_blocking_item_is_not_routed_to_4a
  test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
  test_report_carried.py::test_the_parse_found_something_to_check
  test_report_carried.py::test_the_report_carries_the_finding[(no finding parsed from the verdict)]
  test_report_carried.py::test_a_report_does_not_say_CLOSED
  test_report_carried.py::test_every_carried_item_carries_one_of_the_report_words
  test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces
  test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number
  test_report_carried.py::test_there_are_pointers_to_resolve
  test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]
  test_report_carried.py::test_the_report_carries_a_CI_SECTION
  test_report_carried.py::test_no_RUN_ID_appears_outside_THE_GENERATED_CI_SECTIONS
  test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
  test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph
  test_report_carried.py::test_every_CI_RUN_the_report_names_carries_its_conclusion
  test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit
  test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count
  test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero
  test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]
  test_report_carried.py::test_the_diff_the_site_check_needs_is_available
  test_report_carried.py::test_every_named_site_is_touched_or_declared[(no site parsed)-]
  test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
  test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]
  test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]
  test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]
  test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]
  test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]
  test_report_guard_states.py::test_the_guard_survives_the_state[reviews_directory_renamed_away]
  test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]
  test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]
  test_report_guard_states.py::test_the_guard_survives_the_state[verdict_file_is_a_directory]
  test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]
  test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]
  test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]
  test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
  test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1_reports_one_diagnosis_not_sixteen]
  test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]
  test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]
  test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]
  test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]
  test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[legitimate_open_row]
  test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]
```

## 2. EK0(a) — the premise check, which could have stopped step 1

```
claim  the per-body external hydrodynamic force on each of the five FE bodies is
       identically zero in FloatSim, over all six cases
cmd    for each case: build_system verbatim from the study, then over EVERY step the
       time term `external_force(t)` plus the lagged `state_force`, sliced per body
out    T_full  10.0s  4001 steps  max over the 5 FE bodies = 0.000000e+00 N
out    T_full  12.5s  4001 steps  0.000000e+00 N
out    T_full  14.0s  4001 steps  0.000000e+00 N
out    T_full  15.0s  4001 steps  0.000000e+00 N
out    T_full  16.2s  4001 steps  0.000000e+00 N
out    T_full  20.0s  4001 steps  0.000000e+00 N
out    MAX OVER ALL SIX CASES AND ALL FIVE BODIES: 0.000000e+00 N
rule   EK0(a): report the max; if it is nonzero, STOP
judge  NO STOP. 24006 steps, not a snapshot -- a premise checked at one instant is not
       checked. It is zero BY CONSTRUCTION rather than by cancellation: those five
       bodies carry no `hydro_body_label`, so no excitation channel addresses their
       rows. That makes the premise robust, and it also means this check would NOT
       catch a body that acquired a label later, which is why EK0(a) runs it over all
       six cases every time rather than once.
```

## 3. EK0(d) — the static case and its three checks

```
cmd    solve_superstructure_static, full scale, load path platform then hubs
out    body       weight N     applied N   sum React N  sum err  worst horiz N  backward
out    platform  12262500.0  -12262500.0   12262500.0  0.00e+00     0.000e+00  2.01e-18
out    hub1      14715000.0  -17780625.0   17780625.0  0.00e+00     0.000e+00  5.47e-18
out    hub2      14715000.0  -17780625.0   17780625.0  0.00e+00     0.000e+00  3.87e-18
out    hub3      14715000.0  -17780625.0   17780625.0  2.10e-16     0.000e+00  3.17e-18
out    hub4      14715000.0  -17780625.0   17780625.0  2.10e-16     0.000e+00  4.15e-18
rule   EK0(d): report the reactions and the sum per body
judge  CHECK 1, conservation: worst 2.095e-16.
judge  CHECK 2, the support scheme: the horizontal restraint's reactions are EXACTLY
       0.000e+00 on all five bodies. **THE SECOND SENTENCE THAT STOOD HERE IS WITHDRAWN
       (R672, revision 3 section 4).** It said this zero "proves vertical-only joints
       plus a minimal restraint is the right scheme rather than a convenient one". It
       does not: an eight-DOF restraint -- `ux, uy` at all four joints, for three
       in-plane rigid motions -- gives 0.000000e+00 on all five bodies with the platform
       reactions BIT-IDENTICAL. The figure measures that the applied load is purely
       vertical and nothing about the restraint.
judge  CHECK 3, symmetry: the platform's four hub reactions are each
       3065625.000000 N, spread (max-min)/mean = 9.11e-16, each exactly weight/4. This
       is the only one of the three the FE stiffness participates in, because the
       fourth vertical support is redundant.
judge  each hub then carries 14715000 + 3065625 = 17780625 N, which is the `applied`
       column above.
```

## 4. EK0(e) and DQ8 — the dynamic case over DQ6's window

```
cmd    all six cases, duration = ramp + 15 T_model, window = the final 5 T_model
out    T_full  duration   window from   steps   duality   relief residual / scale
out    10.0s     31.21s      24.14s      707   0.000e+00        4.371e-13
out    12.5s     36.52s      27.68s      885   0.000e+00        3.539e-13
out    14.0s     39.70s      29.70s      991   0.000e+00        1.772e-13
out    15.0s     41.82s      31.82s     1061   0.000e+00        3.311e-13
out    16.2s     44.37s      32.91s     1146   0.000e+00        2.699e-13
out    20.0s     52.43s      38.28s     1415   0.000e+00        1.203e-13
rule   EN2: STOP for a nonzero equal-and-opposite residual, or a per-body dynamic
       residual not small against the reaction scale
judge  NO STOP on either. DQ6 FORCED THREE RUNS LONGER THAN EJ4's 40 s: at T_full =
       15, 16.2 and 20 s, 40 s never reaches ramp + 15 periods, so they are extended
       as DQ6 directs -- T = 20 s needs 52.43 s.
judge  THE DUALITY CHECK IS ON FLOATSIM'S OWN JACOBIAN, and my first version was
       VACUOUS: it asserted `duality_residual(blk, -blk)`, which is zero by
       construction whatever the Jacobian does. The shipped check forms
       `g[rows].T @ lam[rows]` and compares the 6-DOF blocks the two bodies actually
       receive. What that catches is a Jacobian whose two blocks are not negatives,
       which would push the same force into both bodies and leave every member force
       wrong in the same direction on both sides of a joint -- a state no per-body
       equilibrium check would see.
judge  THE INERTIA-RELIEF ACCELERATION IS A PREDICTION. `a = (R^T M R)^-1 R^T f` uses
       the FE mass matrix and the applied reactions only; FloatSim's `xi_ddot` never
       enters the solve, which is what lets DQ8 assert the two agree at step 2. Taking
       it from the export would compare a number with itself (R600).
```

## 5. Member forces, and the static half checked by hand

```
claim  the static member forces are right
cmd    member_forces over each body with the static displacement
out    N = 0 and Vy = Mz = 0 at every station, both bodies
out    all four platform arms identical; all three arms of each hub identical
out    platform arm tip Vz = 2.2992e+06 N
rule   an independent arithmetic check, not a second run of the same code
judge  **THIS SECTION WAS WRONG AND THE WAY IT WAS WRONG IS WORSE THAN THE NUMBERS
       (R663).** It read: "the tip shear reconciles by hand: the 3065625 N reaction
       less half the member's own 156250 x 9.81 = 1533000 N weight gives 2.2996e+06
       against the computed 2.2992e+06." That subtraction IS the defective formula's
       own identity, so it agreed with the defect and would have REDDENED on the
       correct code. It was not an independent check; it was the bug restated.
judge  and the arithmetic was rounded in the one place that mattered:
       156250 x 9.81 = 1532812.5, not 1533000, and the exact figure would have shown
       the agreement was exact rather than approximate.
judge  WHAT IS TRUE, AT ISSUE 2: N = 0 because gravity is vertical and every member
       lies in the joint plane; Vy = Mz = 0 because nothing loads horizontally. The
       figures are in section 12 and the gate is conservation, not an end value.
judge  ONE ELEMENT PER MEMBER at F3's mesh, so two stations per member. EK1 asks the
       report to state that count and this is it.
```

## 6. EK4's PRELIMINARY preview

Written to `docs/reports/F4/preview-PRELIMINARY.md` and delivered. **The figures are
not restated here (EI4).** What the file carries beyond the envelope: the heading-0
load split (arms along `x` axial, arms along `y` in transverse shear), the `Mz`
hand-check, and the `y -> -y` mirror pairs agreeing to every digit shown.

## 7. DQ9 — EB6's second side, settled

```
cmd    read the pinned hydro database's fields and the .nc's variables
out    body_labels is a 12-tuple of NAMES; reference_point is [0,0,0], shape (3,);
out    the .nc's body_name is one string 'buoy1+buoy2+...+buoy12'
judge  `body_labels` is an ORDERING and carries no positions, so it is NOT a second
       side: an ordering moves with a consistent rename, which is R650's own reason
       for withdrawing the cluster angle.
cmd    |A_inf| heave-heave coupling for all 66 buoy pairs against the separation
       rebuilt from the four constants
out    Spearman(separation, coupling) = -0.9785; coupling 9.32e-03 .. 3.16e-01
out    the 4 largest couplings are the 4 closest pairs, SETS EQUAL: True
out    buoy2-buoy4, buoy3-buoy10, buoy6-buoy7, buoy7-buoy11
rule   EM1: an exact SET assertion, with its blind class enumerated and its band
       margin solved both ways
judge  TWO SIDES. It is independent OF THE EXPORT -- the BEM result cannot be permuted
       along with a deck export -- and NOT independent of the design constants, since
       the mesh was built from them.
cmd    the 4th and 5th couplings, and the automorphisms of the 4-pair graph
out    4th 3.150450e-01, 5th 1.198639e-01 -> the 4th must FALL by 2.6284x to tie the
out    5th, and the 5th must RISE by the same 2.6284x
out    blind class: 16 permutations of the 7 touched labels x 5! = 1920, of 12!
out    = 479001600 -> 4.008e-06
judge  THE MARGIN IS 2.63x AND NOT THE 2.65x I FIRST REPORTED. My first figure took
       the 5th pair by DISTANCE (coupling 1.188625e-01) when the assertion is on the
       COUPLING ordering, whose 5th is 1.198639e-01. EM1 adopted 2.65x from my report;
       the measured value is 2.63x and this is the correction.
judge  both directions are the same single number because a set equality has no
       threshold to move -- only the gap between the 4th and 5th closes, from either
       side.
judge  the blind class is the automorphism group: `buoy6-buoy7-buoy11` is a path whose
       centre is pinned by degree (2), `buoy2-buoy4` and `buoy3-buoy10` are two
       interchangeable edges (8), five labels are untouched (120). THE FIRST SIDE IS
       BLIND TO NONE OF THEM, so the two sides together are blind only to the
       identity.
```

## 8. Findings

```
claim  F4-R1 (MINE). The preview's first run added MODEL-scale joint reactions to
       FULL-scale static forces.
cmd    the first run's envelope, dynamic part against static
out    the dynamic contribution was ~1e-5 of the static
rule   a design wave cannot be negligible against self-weight -- which is how it
       announced itself, not a guard
judge  `build_superstructure` converts the deck by `lambda`; `res.lam` comes out of a
       model-scale run. `floatfea/io/froude.py` had already anticipated it:
       COMPOSITE_BLOCKS["joint_multiplier_yaw_locked"] = ((0,3,"force"),(3,4,"moment")),
       with R579's note that scaling the block as pure force "leaves the moment columns
       short by exactly lambda" and as pure moment leaves the forces long by the same
       factor -- "Neither raised. Both results look like numbers." Force x125000,
       moment x6250000.
judge  FIXED in the driver and the table re-run. The largest model-scale joint force
       99.499 N becomes 1.2437e+07 N, the same order as the static 4.7e+06.

claim  F4-R2 (OPEN, and I am naming it rather than leaving it found). There is NO
       GUARD against F4-R1 recurring.
cmd    grep for a test over the scale conversion in the preview driver
out    none exists
rule   the conversion belongs at the I/O boundary (`docs/conventions.md`), so the
       library modules correctly take whatever vector they are handed
judge  the consequence is that the guard has to be a test on the DRIVER, and DR1
       freezes new apparatus through F6. So it is recorded as an open item for the
       reviewer to route rather than apparatus I add on my own authority.

claim  R661 (EK3). F3 step 3's section 8 declares R657's and R658's sites "answered
       at an earlier revision ... verdict 87's own Carried section records it closed",
       about two items sections 9 and 14 of that same report call open and blocking.
rule   EK3: a prose defect found after a step closes is fixed in the next step's first
       report or in docs/closure/** alone, and does not open a round
judge  CORRECTED HERE, which is where EK3 puts it. The cause is my fill-in DEFAULT for
       a site the diff does not touch, not the generator: `untouched_sites.py` emits
       the column empty by design. R657 and R658 are OPEN AND BLOCKING and are carried
       by name below.
```

## 9. Carried

**From verdict 92 and its predecessors**, by name:

| item | disposition |
|---|---|
| R657, R658 | **answered** at `e505f28` under EK2 — the plant locators are anchored, one pattern serving both sites |
| C119 | **answered** at `9020c6c` under EK2 — the id prefix is consumed outside the capture |
| R656 | **open** — ledgered after 28 Oct per EK2, unchanged |

```
cmd    the three affected states, as shipped
out    3 passed
cmd    the same with one line of prose quoting the needle appended -- the exact
         condition that broke them
out    3 passed
cmd    the same with every plant truly suppressed, each write putting back what it read
out    3 failed, with the nested run 368 passed
rule   a planted defect whose presence changes nothing measures nothing
judge  all three discriminate, and 368 reproduces verdict 92's own figure.
cmd    the site parse after C119, over the live verdict
out    sites still carrying an id prefix: []      total sites 174
judge  nine cases were tested, three of them the defect.
```

* **R659, R660, R662** — answered in F3's closure artifact and step-3 report; not
  reopened.
* **R638** — worked in F4, closed before F4 closes (EJ1). Not touched this step.
* **R637 clause (iii)** — its object is R662. Not touched this step.
* **R653** — the `RHO_INF` witness gap. Unchanged; no assertion added (DR1).
* **The DR1 / CZ0 conflict** — RESOLVED by EK2 and applied twice this step.

## 10. Tolerances touched

```
cmd    git diff --name-only <the F3 closing commit>..HEAD -- floatfea/tolerances.py
out    (no output)
judge  NO TOLERANCE WAS DECLARED OR MOVED. F4 declares none until step 2 measures one,
       which is what the locked plan's gate table says: every F4 row reads "to be
       measured at step 2" or names the step that measures it.
```

## 11. The whole suite

**Whole suite: 2793 passed, 43 failed, 1 skipped**, one invocation, no `--ignore`, in
a clean clone outside the OneDrive tree with `origin` resolving, 500.91s.

```
cmd    python -m pytest -q, the tree this commit lands
out    43 failed, 2793 passed, 1 skipped, 2 warnings in 500.91s (0:08:20)
cmd    git diff --name-only <the F3 closing commit>..HEAD -- floatfea
out    the five new mapping modules, and nothing else
rule   R309: one line, not seven subsets, because a subset cannot see a failure in an
       eighth file
judge  all 43 are in the three report-parametrised files and all 43 are section 1b's
       one cause; `floatfea/` and the verification ladder are green. The figure is
       taken at the tree this commit lands rather than in the working copy, and it is
       RE-TAKEN at the committed sha afterwards -- R651 and R654 were both a count
       taken before the edit that changed it.
```

---

# Revision 2 — the ninety-third verdict's seven blocking items

Answers: verdict 93 @ 3a908fa

**2026-10-05.**

## 12. R663 — a real defect in `floatfea/`, and the gate that now catches it

```
claim  member_forces returned `k u` with the element's equivalent load omitted
cmd    for one platform arm: k_local @ T @ u, then the same minus the element
         equivalent load formed independently as M_e (T a_g)
out                        SHIPPED (k u)   WITH f_eq SUBTRACTED
out    end B Vz             2.299219e+06          3.065625e+06
out    end B My            -6.386719e+06         -3.725290e-09
out    Vz_A + Vz_B          0.000000e+00          1.532813e+06
out    the tip reaction                           3.065625e+06
out    the member's weight                        1.532812e+06
out    mu L^2 / 12                                6.386719e+06
rule   a member carrying its own distributed weight must show that weight in the SUM
       of its two end shears
judge  CONFIRMED, independently of the verdict. `k u` carries the rigid null space, so
       its end shears cancel IDENTICALLY -- which is why the weight could never appear
       and why no comparison against a hand-computed END value can see it. The shipped
       tip moment is exactly `-mu L^2 / 12` where a roller carries none, and the
       shipped tip shear is 25.0000% below the reaction it must equal.
cmd    the fix, over all 16 members: |Vz_A + Vz_B - weight| / weight
out    worst 5.696e-16; every tip shear equals its support reaction to every digit
out    (3065625.000000 platform, 5926875.000000 hub)
judge  FIXED. The reach was every Vz and My in both tables of the preview, which is
       REISSUED as issue 2 and supersedes the first.
```

## 13. The gates, each with a counter-case that must redden

`tests/verification/rung4/test_f4_static_and_mapping.py`, 9 tests.

| gate | counter-case | answers |
|---|---|---|
| member end shears sum to the load carried | the shipped `k u` must fail it, asserted | R663 |
| tip shear = support reaction | two separately derived numbers | R663 |
| static sum vs the INDEPENDENT `weight_N` | remainder dropped; gravity reversed | R664, R665 |
| duality is a property of the JACOBIAN | a both-blocks-`+I` mutant must read `2.0` | R668 |
| EB6 first side vs HSP-stable | the two CLOSEST labels transposed | R667 |

```
cmd    pytest tests/verification/rung4/test_f4_static_and_mapping.py -q
out    9 passed
cmd    widen EB6_POSITION_CEILING from 1.0e-6 to 1.0e+3 and re-run
out    1 failed, 8 passed      -- the counter-case, and only it
rule   a ceiling nothing fails against is not a ceiling
judge  the ceiling is load-bearing and the counter-case discriminates on it.
judge  **AND MY FIRST EB6 COUNTER-CASE WAS WEAK.** It measured a property of the
       GEOMETRY -- that a transposition moves a label further than the ceiling -- and
       inferred the gate would notice. It now runs the gate's OWN comparison against a
       permuted expectation. Inferring that a gate would catch something is not
       measuring that it does.
judge  R664's fix is the one move the verdict named: `sum_error` compares two numbers
       both derived from `f`, while `weight_N` comes from the deck and entered no
       comparison. It does now.
judge  R668: no module under `floatfea/` reads a Jacobian, and the
       `g[rows].T @ lam[rows]` check section 4 describes lives in a driver that was
       never committed -- so the shipped duality figure WAS zero by construction. The
       property is now asserted where it lives, on a Jacobian.
judge  R669: nine tests now import the five modules. The four gate rows the plan marks
       "to be measured at step 1" have assertions behind them.
```

## 14. R667's limitation, stated rather than left to be found

```
cmd    the skip condition on EB6's two tests
out    skipif not (HSP-stable/studies/platform-12buoy/platform_common.py).is_file()
rule   EB6's expected side is read READ-ONLY from HSP-stable by DS0's design
judge  so the gate CANNOT RUN where that worktree is absent, which includes CI. It
       passes locally and skips there. **A SKIPPING GATE IS A GAP**, and the skip
       reason says so in those words rather than reading as a pass. Routing it is the
       reviewer's: the alternatives are vendoring the four constants into the
       repository, which puts the expected side where a permutation could reach it, or
       accepting a gate that runs in one place only.
```

## 15. R666 — my "ONE CAUSE" was wrong for three of the 43

```
cmd    the verdict's own cells, which I accept rather than re-derive
out    a stub verdict      43 -> 33   (10 clear, 0 new)
out    **CLOSED** -> **answered**   33 -> 32
out    **ledgered** -> **open**     32 -> 29
rule   EG3(i): a red that does not trace to the stated cause still blocks
judge  THREE OF THE 43 WERE NOT THE MILESTONE BOUNDARY. They were vocabulary: my
       Carried table used words the report's own spelling rules do not permit. Section
       1b's LIST was complete and verified set-identical by the verdict; its SENTENCE
       was wrong. Both one-word changes are made.
judge  this is the eighty-third verdict's R629 shape at forty-three-red scale: a real
       defect inside a group ruled by class.
```

## 16. Carried

| item | disposition |
|---|---|
| R663, R664, R665, R666, R668 | **answered** this round, each with a counter-case |
| R669 | **answered** in part — nine gates now import the five modules |
| R667 | **answered**, with the skip limitation stated in § 14 |
| R656 | **open** with Xabier |
| R653 | **open**; becomes a gate finding at step 2 |
| R638 | **open** under EJ1, which requires it answered before F4 ends |
| C135 to C143 | **open** — absorbed in the closure commit, not re-reviewed individually |

The verdict **withdrew one of its own predecessor's closing conditions** and recorded
that my refusal to write an `Answers:` header naming another milestone's verdict into
F4's first report was right.

```
cmd    the four constants F4 step 1 declares, and the plan rows that move them
out    F4_MEMBER_FORCE_CONSERVATION                 1.0e-13
out    F4_MEMBER_FORCE_CONSERVATION_COUNTER_DEFECT  0.5
out    F4_EB6_POSITION_M                            1.0e-6
out    F4_STATIC_REACTION_AGREEMENT                 1.0e-12
cmd    pytest tests/test_plan_matches_tolerances.py tests/test_no_tolerance_literals.py
         tests/verification/rung4/test_f4_static_and_mapping.py -q
out    183 passed
rule   every numerical tolerance lives in floatfea/tolerances.py, and it moves with a
       plan edit or it does not move
judge  **THE TOLERANCE GUARD REFUSED ME THREE TIMES AND WAS RIGHT EACH TIME.** My first
       version put the two ceilings in module constants with "not-a-tolerance"
       docstrings; they are comparison epsilons reaching comparisons, which is exactly
       the clause about a tolerance under another name. They are declared now, with
       derivations and counter-cases, and `docs/milestones/F4.md` section 5a is the plan
       edit that moves them.
judge  and TWO literals went away rather than being exempted: the Jacobian test's values
       are EXACT in binary floating point -- `x + (-x)` is exactly zero and
       `max|2 lam| / max|lam|` exactly 2 -- so it asserts equality, which is stronger
       than any epsilon and removes the question of which epsilon.
```

## 17. The whole suite

SUITE2_PLACEHOLDER

# Revision 3 — the ninety-fourth verdict's nine blocking items

Answers: verdict 94 @ de9a448

**2026-10-05.**

## 0. CI at `7c8e4ae`, the commit verdict 94 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 94 at `7c8e4ae` through the report's own `Answers:` line. Run `37349836460`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 891 | 39 | 1 |
| the verification ladder | 1865 | 0 | 2 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 2 not green.**

- lint, unit and guards (failure)
- the verification ladder (failure)

**Failing tests named in the log: 39.**

- `tests/test_report_carried.py::test_the_report_carries_the_finding[R622]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R626]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R631]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R635]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R637]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R654]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R655]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R657]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R658]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R659]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R660]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R661]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R662]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_report_does_not_say_CLOSED` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R664-floatfea/solve/static.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/loads/selfweight.py:86]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:21]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:22]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-docs/closure/F3.md:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-tests/verification/rung3/test_platform_skeleton.py:711]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R668-joint_reactions.py:89]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[legitimate_open_row]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 94 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 94 at `7c8e4ae` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37349836460` | push | `7c8e4ae` | conclusion **failure** |
| `37405359199` | push | `ed484dd` | conclusion **failure** |
| `37409288843` | push | `ca8b51b` | conclusion **failure** |

**Run `37349836460`, conclusion **failure**: 39 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R622]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R626]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R631]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R635]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R637]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R654]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R655]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R657]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R658]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R659]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R660]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R661]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R662]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_report_does_not_say_CLOSED` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R664-floatfea/solve/static.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/loads/selfweight.py:86]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:21]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:22]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-docs/closure/F3.md:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-tests/verification/rung3/test_platform_skeleton.py:711]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R668-joint_reactions.py:89]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[legitimate_open_row]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]` (lint, unit and guards)

**Run `37405359199`, conclusion **failure**: 39 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R622]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R626]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R631]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R635]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R637]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R654]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R655]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R657]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R658]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R659]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R660]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R661]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R662]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_report_does_not_say_CLOSED` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R664-floatfea/solve/static.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/loads/selfweight.py:86]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:21]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:22]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/solve/static.py:23]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-docs/closure/F3.md:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-tests/verification/rung3/test_platform_skeleton.py:711]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R668-joint_reactions.py:89]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[legitimate_open_row]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]` (lint, unit and guards)

**Run `37409288843`, conclusion **failure**: 36 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R622]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R626]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R631]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R635]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R637]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R654]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R655]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R657]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R658]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R659]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R660]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R661]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R662]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_report_does_not_say_CLOSED` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R664-floatfea/solve/static.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R665-floatfea/loads/selfweight.py:86]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-docs/closure/F3.md:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R667-tests/verification/rung3/test_platform_skeleton.py:711]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R668-joint_reactions.py:89]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[legitimate_open_row]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]` (lint, unit and guards)

## 1. The reading

**Measured against the dates, today, 5 October.**

| what | date | status today |
|---|---|---|
| EK4's preview | 8 Oct | **held** — issue 3 shipped today, three days early |
| member-force table | 23 Oct | on track; step 1 of three closes this round |
| F4 working target | 14 Oct | on track |
| F4 committed | 19 Oct | on track |
| step 1 rounds | round 3 of 3 | the last one CZ0 allows; two steps remain after it |

```
claim  the dates in that table are the ones the directives and the plan actually set
cmd    grep -n '19 Oct\|23 Oct\|14 Oct\|8 Oct' docs/milestones/F4.md | head -4
out    133:for step 2's gates. **Label it PRELIMINARY.** Target 8 Oct.
out    375:| F4 | 19 Oct | 14 Oct |
out    376:| member-force table | 23 Oct | 17 Oct |
out    377:| code check | 28 Oct | 22 Oct |
rule   CZ0: throughput is a requirement and slippage is reported the day it is known
judge  the plan's table is `committed | working`, so the member-force table's WORKING
       target is 17 Oct and its committed date is 23 Oct. My row above quotes the
       committed one, which is the date that matters to Xabier.
judge  the table is not a measurement of the code -- it is a restatement of the
       commitments -- so the command that checks it is a grep over the plan, and that
       is the command a reader needs to refute any row of it.
```
 **No slippage to report
today, and the arithmetic that would produce some is this:** step 1 has consumed its
three rounds, so if anything blocking survives this revision it carries into step 2 by
name and blocks there — which costs step 2 round budget, not calendar, unless step 2 then
needs three rounds of its own. If that happens the choice CZ0 names is live and I will
state it the day it is known rather than at step 2's close. The ninety-fourth verdict put
this arithmetic on the record because nobody raised it; it is raised here now, and the
previous revision's paragraph is **rewritten and not carried** (verdict 94, item 10).

All nine blocking items are answered below. Four needed code that did not exist: the
pinned snapshot's second half, two tolerances, three gate rows. One of them — R675 —
turned out to be worse than the verdict said, and that is in § 7.

## 2. R670 and R667 — the EB6 gate reads a pinned snapshot, and the rung has no skip

The verdict's routing: a `skipif` is not available inside `tests/verification/`, and of
the two alternatives revision 2 offered it takes neither. EO0 ruled the same way and named
the shape — a committed fixture whose provenance is a hash of the source. That is what
ships.

```
claim  the rung runs every case with no skip, which is the exact red the verdict read
cmd    bash scripts/run_rung.sh full:tests/verification/rung4
out    run_rung: 150 collected, 0 failed, 0 errored, 0 skipped
out    run_rung: OK -- 1 director(y|ies) ran
rule   scripts/run_rung.sh:274-276 -- a rung with any skipped case exits FAIL
judge  the verdict's log read `run_rung: FAIL -- 2 skipped in tests/verification/rung4`
       with `137 collected, 0 failed, 0 errored, 2 skipped`. It now reads 150 and 0.
```

```
claim  the expected side is HSP-stable's own source and the deck export cannot reach it
cmd    python scripts/export_buoy_centers_ref.py --check
out    EB6 reference: current. blob b8b8123904af, tag floatfea-ref-1, 12 buoys and 4 hubs.
rule   EO0(a): generated from the source code, never from the deck export
judge  the snapshot carries the blob sha of `platform_common.py` and the pinned tag, and
       the gate asserts the recorded blob matches the one it expects, so a moved source
       reddens rather than passing. `--check` is in the DS0 preflight (EO0(c)) and is not
       a pytest skip, which is the whole point.
```

**R667's hub extension ships too**, and is in § 8 with the other gate rows.

```
claim  the snapshot's provenance names every line the expected side is read from,
       including the hub Body the DQ9 extension needs
cmd    python -c "import json,pathlib; print(json.loads(pathlib.Path(
         'data/platform/buoy_centers_ref.json').read_text())['provenance']['lines'])"
out    CLUSTER_ARM_RADIUS :33, CLUSTER_ANGLES_DEG :34, BUOY_ANGLES_DEG :35,
out    BUOY_RADIUS :36, Z_HUB_REF :102, buoy_centers() :51-58, the hub Body :157,
out    hydro_body_label :140
judge  `:157` is the line DQ9 names for the hub positions and `:140` is EK0(a)'s premise.
       Both are in one snapshot with one blob sha, so one `--check` covers all of it.
``` **What this gate does NOT catch, stated rather than left to be
found:** a body whose geometry changes in HSP-stable AFTER this blob. `--check` is what
sees that, and the same limitation applies to EK0(a)'s premise gate for the same reason.

**The verdict's closure item about this gate's honesty is answered here rather than in
the closure commit, because it is about what the gate reads:** the docstring said "the
constants are read from the file, so a change there reaches this gate", and two of the
four were literals in the test.

```
claim  all four constants now sit in the snapshot, so a change to any of them is seen
cmd    grep -n 'BUOY_ANGLES_DEG\|CLUSTER_ARM_RADIUS\|BUOY_RADIUS\|Z_HUB_REF' scripts/export_buoy_centers_ref.py
out    BUOY_ANGLES_DEG = (0.0, 120.0, 240.0)  -- named with its citation at
out      `cluster-3buoy-rigid/cluster_common.py:47` and compared by `--check`
out    _constants() parses CLUSTER_ARM_RADIUS, CLUSTER_ANGLES_DEG and BUOY_RADIUS
out    _z_hub() parses Z_HUB_REF
judge  the generator refuses rather than guessing if any parse fails, so a renamed or
       moved constant reddens the snapshot build instead of silently vendoring a stale
       value.
```

## 3. R671 — the ceiling is bounded above, and the counter-case is why

The rename to `_COUNTER` was in the previous commit and the verdict accepted it. What was
missing is the second half of the closing condition: the counter-case's assertion had to
compare the defect against the CEILING, so that widening makes it harder.

```
claim  the signature assertion read `< CEILING`, which got EASIER as the ceiling rose
cmd    git show 6cf4efe~2 -- tests/verification/rung4/test_f4_static_and_mapping.py | grep -n 'abs(carried) / weight'
out    -    assert abs(carried) / weight < F4_MEMBER_FORCE_CONSERVATION, (
out    +    assert abs(carried) / weight < F4_MEMBER_FORCE_CONSERVATION_COUNTER, (
judge  two assertions were reading the ceiling in the direction that loosens. The
       signature now reads against the counter, which the ceiling cannot move.
```

```
claim  a new assertion compares the defect's error against the ceiling itself
cmd    grep -n -A3 'the ceiling .* is not below the error' tests/verification/rung4/test_f4_static_and_mapping.py
out    assert relative > F4_MEMBER_FORCE_CONSERVATION, (
out        f"the ceiling {F4_MEMBER_FORCE_CONSERVATION:.3e} is not below the error the "
out        f"defect produces, {relative:.3e}. The gate above would ACCEPT R663."
rule   the defect's relative conservation error is exactly 1.0 -- `k u` loses the
       member's ENTIRE weight -- so a ceiling at or above 1.0 reddens here
```

```
cmd    python scratchpad/sweep_r671.py
out    WEAKENING -- how far may the ceiling RISE?
out         ceiling   passed  failed   failing ids BESIDES the plan guard
out         1.0e-13      410       0   -                                  (shipped)
out          1.0e-9      409       1   plan guard only
out            0.49      409       1   plan guard only
out             0.5      408       2   test_the_ceiling_sits_below_its_counter_case[F4_MEMBER_FORCE_CONSERVATION]
out             1.0      407       3   + test_G4_the_conservation_gate_REDDENS_without_the_equivalent_load
out             2.0      407       3   + the same
out          1.0e+6      407       3   + the same
out    TIGHTENING -- how far may it FALL before the clean case trips?
out         1.0e-15      409       1   plan guard only
out         5.0e-16      408       2   test_G4_member_end_shears_sum_to_the_load_the_member_carries
out    restored; git status --short clean
rule   the bracket asserts `ceiling < counter` (0.5); the counter-case asserts the
       defect's error (exactly 1.0) exceeds the ceiling
```

The ceiling is bounded above twice over: at `0.5` by the counter bracket the rename
restored, and at `1.0` by the counter-case's own new assertion. Below, it reaches
`1.0e-15` and the CLEAN gate trips at `5.0e-16`.

**And two figures I wrote in this section's first draft were wrong, which is why they now
carry a command.** `test_report_numbers_are_sourced` named both as unsourced and both were
also false: one was rounded off a stale division, the other does not correspond to
anything I can reconstruct.

```
claim  the clean worst, the room beneath the ceiling, and the bracket above it
cmd    python -c "...conservation worst over all 16 members with the `rho A L` form,
         then C/worst and 0.5/C..."
out    clean conservation worst (rho A L form) = 5.696163e-16
out    ceiling 1.0e-13;  room beneath = 175.6x;  bracket above = 0.5/1.0e-13 = 5.0e+12x
out    WITHDRAWN, first draft of this section: "178x of room beneath it and 3850x above"
out      -- 178 was a rounded stale division, 3850 corresponds to nothing
rule   the gate asserts `worst < F4_MEMBER_FORCE_CONSERVATION`; the bracket asserts
       `ceiling < 0.5`; the counter-case asserts the defect's error (1.0) > ceiling
cell   re-measured AFTER § 7's change from the body average to `rho A L`, because that
       change moves the quantity the figure describes. It did not move the value --
       `5.696163e-16` is the same number the ninety-fourth verdict read -- and the point
       is that I measured rather than carrying it.
```

**I did not widen anything, exempt an entry, or extend the rung3 guard.** The suffix that
already works is the whole repair, exactly as the verdict said.

## 4. R672 and R665 — the determinacy claim is WITHDRAWN, site by site

The verdict offered two ways to close this and said the eight-DOF cell is the
discriminator. I take the withdrawal, not the new gate, and the reason is that the
measurement does not support the claim in any form:

```
claim  `worst_horizontal_N` is exactly zero for a grossly redundant restraint too
cmd    python scratchpad/cell_r672.py
out    platform        0.000000e+00      0.000000e+00   (8 DOF restrained for 3 rigid motions)
       hub1            0.000000e+00      0.000000e+00   (6 DOF restrained for 3 rigid motions)
       hub2            0.000000e+00      0.000000e+00   (6 DOF restrained for 3 rigid motions)
       hub3            0.000000e+00      0.000000e+00   (6 DOF restrained for 3 rigid motions)
       hub4            0.000000e+00      0.000000e+00   (6 DOF restrained for 3 rigid motions)
out    platform vertical reactions, minimal   : 3065625.000000 x4
out    platform vertical reactions, eight-DOF : 3065625.000000 x4
out    BIT-IDENTICAL: True
rule   R665's condition: EITHER the quantity says what it measures with a relative
       threshold and a counter, OR a check a redundant restraint reddens
cell   the restraint replaced by `ux, uy` at ALL FOUR joints -- eight DOF for three rigid
       motions -- with the loads, the geometry, the sections and the mass held. One
       variable moved.
judge  a figure that is identically zero for both the minimal and the eight-DOF restraint
       cannot be evidence about either, so there is nothing to put a threshold on. The
       claim goes.
```

**Both named sites, each with its hunk:**

```
claim  floatfea/solve/static.py:21-23 no longer claims the zero proves the scheme right
cmd    git show 6cf4efe~1 -- floatfea/solve/static.py | grep -E '^[-+].*(support scheme|determinate|purely vertical)'
out    -  * the horizontal restraint's reactions are ZERO -- that the support scheme is right. A
out    -    vertical load system can induce no horizontal reaction in a determinate restraint, so
out    -    a nonzero value means the restraint is carrying load it should not.
out    +    that the zero proves the support scheme determinate rather than convenient -- is
out    +    WITHDRAWN (R672). `gravity_load` is nonzero only on `uz`, `rx` and `ry`, so the
out    +    that removes the three in-plane rigid motions, determinate or grossly redundant.
judge  the bullet now says the figure measures that the APPLIED LOAD is purely vertical
       and nothing about the restraint, says the old claim is withdrawn, and says no
       threshold is declared so it is reported rather than asserted on.
```

```
claim  report section 3 CHECK 2's sentence is withdrawn as well
cmd    git diff --stat HEAD -- docs/reports/F4/step-1.md ; grep -n 'proves' docs/reports/F4/step-1.md
out    **THE SECOND SENTENCE THAT STOOD HERE IS WITHDRAWN (R672, revision 3
out    section 4).** It said this zero "proves vertical-only joints plus a minimal
out    restraint is the right scheme rather than a convenient one". It does not: an
out    eight-DOF restraint gives 0.000000e+00 on all five bodies with the platform
out    reactions BIT-IDENTICAL.
judge  revision 1's section 3 is amended in place rather than contradicted later in the
       file, because a reader who stops at section 3 is the reader the claim misleads.
```

**And the report's own table was wrong about which finding this gate answers:**

```
claim  revision 2's gate table credits the static-weight gate with answering R665
cmd    grep -n 'R664, R665' docs/reports/F4/step-1.md
out    406:| static sum vs the INDEPENDENT `weight_N` | remainder dropped; gravity
out        reversed | R664, R665 |
judge  it answers R664. R665 is answered in this section, by withdrawal, and nothing in
       that gate addresses the support scheme at all. The row stands as revision 2 wrote
       it and is corrected here rather than edited there, because a reader following the
       verdict's closure item needs to find both.
```

## 5. R673 and R666 — all 39 reds, traced, and the one that was not a boundary red

```
claim  the whole suite was 39 red at the reviewed commit, and all 39 sit in three files
cmd    python -m pytest -q   (clone outside OneDrive)   then the three files alone
out    39 failed, 2857 passed, 1 skipped, 2 warnings in 901.15s
out    the three files alone: 39 failed, 151 passed, 1 skipped in 65.27s
rule   EG3(i): the waiver is conditional on the trace, and the trace is pasted
judge  the two counts are equal and the sets are nested, so NOTHING outside
       test_report_carried.py, test_report_guard_states.py and
       test_report_vocabulary_corpus.py was red. That is the claim the trace needs.
```

**The trace, by name.**

```
claim  the 39 split into four groups and the groups sum to 39
cmd    python -c "rows=[13,8,1,1,1,7,5,3]; print(sum(rows), 13+8+1+1+1, 7, 5, 3)"
out    39   on EG3 state (2)'s list: 24   EH1 cascade: 7   off both lists: 5
out    NOT boundary reds: 3
rule   EG3(i): every FAILED id is matched to the state's own list, and a red that does
       not match is CZ1 (iv) unchanged
```

| count | id | where it sits |
|---|---|---|
| 13 | `test_the_report_carries_the_finding[R622 R626 R631 R635 R637 R654 R655 R657 R658 R659 R660 R661 R662]` | EG3 state (2), item 2 |
| 8 | `test_every_named_site_is_touched_or_declared[…]` | EG3 state (2), item 1 |
| 1 | `test_the_CI_section_is_about_the_REVIEWED_commit` | EG3 state (2), item 3 |
| 1 | `test_the_Carried_table_is_what_the_generator_produces` | EG3 state (2), item 4 |
| 1 | `test_the_generator_would_catch_a_row_under_the_wrong_number` | EG3 state (2), item 5 |
| 7 | `test_the_guard_survives_the_state[baseline + 6]` | EH1's cascade — the baseline is red and each row's own failure line says so |
| 5 | CI section, `## 0a` rounds table, whole-suite line, CI-table rows, CI counts all zero | **off both EG3 lists**, and each one's own failure line reads "the newest report revision has no …" — state (2) by its own definition |
| 3 | `test_a_report_does_not_say_CLOSED` + 2 `test_report_vocabulary_corpus` rows | **NOT a boundary red.** Fixed. |

**The five off-list ids are a correction to EG3's state (2) list**, measured the way EJ2
made its two: each was run on its own, not ruled as part of a 39-red family.

```
claim  each of the five fails because the ANSWERING REVISION does not exist yet
cmd    python -m pytest <each id> -q --tb=line, one at a time
out    "the newest report revision has no `## ... CI ...` section"
out    "no `## 0a` table in the newest revision"
out    "the 0a table has no rows"
out    "the newest revision carries no whole-suite line"
out    "every CI row in step-1.md reports zero passed and zero failed"
judge  that is state (2) -- verdict written, answering report not yet -- and none of the
       five is on EG3's list for it. I am not proposing a clause; I am recording the
       measurement and letting the reviewer rule, because EG3's lists have been short
       twice before and both corrections came from running the off-list ids alone.
```

**The three that were not boundary reds, and R666's remaining third:**

```
claim  the R638 Carried row used a word only a verdict may use
cmd    python -m pytest tests/test_report_carried.py::test_a_report_does_not_say_CLOSED -q
out    before: assert not [('R638', '**open** under EJ1, closed before F4 closes')]
out    after:  6 status cells parsed, 0 say `closed`   ->   33 passed
judge  the row now reads `**open** under EJ1, which requires it answered before F4 ends`.
       "closes" is not "closed" and the row still says what it DID.
rule   CC1: only a verdict closes an item
```

```
claim  the two vocabulary-corpus rows were a CASCADE off that one red, not defects
cmd    python -m pytest tests/test_report_vocabulary_corpus.py -q, before and after
out    before: legitimate_open_row and two_spaces_before_the_item_number both
out            "the corpus requires `allowed` and the shipped guard says `refused`,
out             reported by test_a_report_does_not_say_CLOSED"
out    after:  33 passed
judge  the corpus harness appends its row to the newest Carried text and runs the shipped
       guard, so a guard already red on the base text reports every row as refused. They
       cleared with the baseline and neither is a guard defect. The identification is
       EH1's -- the baseline being red plus each row's own failure line, not the name.
```

**And the mechanism, because the verdict asked for it and the answer is unflattering:**
`docs/reports/F4/step-1-answers.json` **did not exist**. Revisions 1 and 2 wrote the
`Carried` table by hand, which is exactly the failure `scripts/carried_table.py` was
committed to remove, and thirteen rows went missing because nothing read the verdict. The
file exists now and § 14's table is generated from it.

## 6. R674 and R664 — the comparison is SIGNED and both counter-cases corrupt the MODEL

```
claim  the gate compares the signed applied load, so a reversed field reddens on EVERY body
cmd    grep -n 'applied_N == pytest.approx' tests/verification/rung4/test_f4_static_and_mapping.py
out    assert case.applied_N == pytest.approx(expected, rel=F4_STATIC_REACTION_AGREEMENT)
judge  `abs(case.applied_N)` is gone. The platform row -- the one the verdict measured
       reading `rel 0.000e+00` under reversal -- now reddens with the four hub rows.
```

```
claim  reversing GRAVITY_VECTOR in the SOURCE reddens the gate
cmd    python scratchpad/cell_r674.py
out    CLEAN            platform  applied_N=-1.226250e+07   expected=-1.226250e+07
out                     SIGNED rel = 0.000000e+00      abs() rel = 0.000000e+00
out    GRAVITY NEGATED  platform  applied_N= 1.226250e+07   expected=-1.226250e+07
out                     SIGNED rel = 2.000000e+00      abs() rel = 0.000000e+00
out    and over the rung: 4 failed, 146 passed (clean: 150 passed), the reds being
out      test_G4_1_static_the_sum_is_checked_against_the_INDEPENDENT_weight
out      test_G4_1_static_the_weight_check_REDDENS_on_the_two_worst_misses
out      test_G4_member_end_shears_sum_to_the_load_the_member_carries
out      test_EO1_static_member_forces_match_STATICS_not_the_model
cell   `GRAVITY_VECTOR` negated in `floatfea/io/frames.py` and nothing else; the file is
       restored and `git status --short` is clean afterwards.
```

```
claim  the declared counter-case injects into the model, not into the expected side
cmd    grep -n -B2 -A6 'corrupt_body = ' tests/verification/rung4/test_f4_static_and_mapping.py
out    246:    corrupt_body = (
out    247-        replace(platform, remainder_mass=0.0) if injection == "remainder_dropped" else platform
out    248-    )
out    249-    accel = _gravity_field(corrupt_body.model.n_dof)
out    250-    if injection == "gravity_reversed":
out    251-        accel = -accel
rule   R674: "the two counter-cases are injected into the MODEL -- GRAVITY_VECTOR
       negated, the remainder diagonal dropped -- and re-solved"
out    the dropped-remainder injection measures clean    applied_N=-1.226250e+07  weight_N=1.226250e+07  rel=0.000000e+00
out    dropped  applied_N=-6.131250e+06  weight_N=1.226250e+07  rel=5.000000e-01 per body
judge  `corrupt = -case.weight_N` is gone. The remainder injection is
       `replace(platform, remainder_mass=0.0)`, which changes the MODEL and re-solves,
       and the verdict's figure to beat was `5.000e-01` on the platform.
```

## 7. R675 — the count is asserted, the docstring says what the gate is, AND THE AVERAGE WAS WRONG

**(a) The vacuous-pass hazard.**

```
claim  the tip-shear gate asserts the number of comparisons it made
cmd    grep -n 'checked == 16' tests/verification/rung4/test_f4_static_and_mapping.py
out    178:    assert checked == 16, (
judge  the silent `continue` can no longer take the count to zero without a word. My
       non-reproduction of the "0 assertions" half stands as recorded (EO3): at the
       reviewed commit 16 of 16 ran and 0 skipped. The assertion closes the hazard rather
       than the symptom.
```

**(b) The conservation gate's reach — and this is where the verdict understated it.**

The docstring already said the gate is blind to the solve. The other half of the condition
was the body average, and the verdict's reason for objecting was that nothing asserted the
premise. **I asserted it and the premise is false.**

```
claim  a hub's three members are NOT equal in length
cmd    python -c "...for m in body.members: print(m.label, repr(m.length))"
out    hub1:buoy1_arm  25.0
out    hub1:buoy2_arm  25.0
out    hub1:buoy3_arm  25.000000000000004
out    hub2:buoy4_arm  25.000000000000004
out    hub2:buoy5_arm  25.000000000000007
out    hub2:buoy6_arm  25.0
out    (the platform's four are all exactly 50.0)
rule   `member_mass / len(members)` is each element's mass only if the lengths are
       identical, so the premise is exact equality
judge  one and two ulp, out of the 120-degree cluster geometry. Equal to round-off is not
       equal. And the consequence is not a missed defect: on a frame with genuinely
       unequal members the average is the WRONG number and this gate FALSE-REDDENS, which
       is a wrong answer rather than a blind spot.
```

So the premise is not asserted — it is removed. The gate compares against `rho * A * L`,
the prismatic mass of THAT element, which is also independent of the assembler whose
consistent mass matrix the gate reads through `element_equivalent_load` (EA4).

```
claim  the closed form reproduces each element's mass and sums to member_mass exactly
cmd    python -c "...sum(rho A L) vs body.member_mass per body..."
out    platform  sum(rho A L)=6.2500000000e+05  member_mass=6.2500000000e+05  rel=0.000e+00
out    hub1      sum(rho A L)=7.5000000000e+05  member_mass=7.5000000000e+05  rel=0.000e+00
out    hub2, hub3, hub4: the same, rel=0.000e+00.  worst body-level rel: 0.0
out    each element: rho A L = 1.5625000000e+05 (platform), 2.5000000000e+05 (hubs)
```

## 8. R676 and R669 — the three remaining gate rows are assertions

Three rows had no assertion anywhere. All three ship, each with a counter-case, and none
of it is apparatus DR1 freezes: these are the locked plan's own gate rows for this step.

**(i) EK0(d) platform symmetry** — the only one of EK0(d)'s three the FE stiffness
participates in.

```
claim  the four hub reactions are asserted equal, and the gate reddens on an unsymmetric frame
cmd    python -m pytest tests/verification/rung4 -q -k EK0d
out    2 passed, 148 deselected in 0.48s
rule   F4_STATIC_SYMMETRY_SPREAD = 1.0e-12 on `(max - min) / mean`
```

```
claim  clean and injected, both measured, and the injection moves ONE variable
cmd    python scratchpad/measure_r676.py
out    CLEAN spread (max-min)/mean = 9.1139e-16
out    softening 0.01 -> 1.5617e+00, reactions 671905.5, 671905.5, 5459344.5, 5459344.5
cell   one platform arm's `I_y`, `I_z` and `J` scaled; `A` HELD, so the body's mass is
       identical and the only thing that moved is the stiffness that decides the split.
judge  the verdict's own discriminator figures -- `671905.5`, `5459344.5`, spread
       `1.5617` against a clean `9.11e-16` -- reproduce on my instrument to every digit.
```

```
cmd    python scratchpad/sweep_f4_static_symmetry_spread.py
out    WEAKENING                        TIGHTENING
out      1.0e-12  434 passed  0 failed    1.0e-12  434 passed  0 failed
out          1.0  433         1  plan         1.0e-15  433      1  plan
out          1.5  432         2  + the counter bracket
out          2.0  431         3  + test_EK0d_the_symmetry_gate_REDDENS_on_an_unsymmetric_frame
out                                        5.0e-16  432      2  + test_EK0d_the_platform_
out                                                                four_hub_reactions_are_EQUAL
out    restored; git status --short clean
rule   clean spread 9.113860057399177e-16, so the shipped 1.0e-12 sits 1097x above it
```

**And the weakening direction on the INJECTION rather than the ceiling (EH4)** — EH4 asks
for the direction that makes the gate look WEAK, so the injection is shrunk until a clean
case would pass:

```
claim  a softening of one part in 1e9 is still caught, by 404x
cmd    python -c "...spread at factor 1.0 and at 1.0-1e-9, against the 1.0e-12 ceiling..."
out    softening                    1.0 -> spread 9.1139e-16   vs 1.0e-12: 9.114e-04x
out    softening            0.999999999 -> spread 4.0464e-10   vs 1.0e-12: 4.046e+02x
rule   the gate asserts `spread < F4_STATIC_SYMMETRY_SPREAD`
judge  so the gate does not need a large defect to see one, and the clean case sits
       three decades BELOW the ceiling rather than just under it.
```

**(ii) G4.4 mapping conservation** — and `map_joint_reactions` is now called by a test.

```
claim  the mapper's resultant force AND moment about the origin are asserted
cmd    python -m pytest tests/verification/rung4 -q -k G4_4
out    3 passed, 147 deselected in 0.49s
rule   F4_MAPPING_CONSERVATION = 1.0e-12, relative, force and moment normalised separately
judge  the quantity is not exactly zero and the reason is summation order, not physics:
       the mapper accumulates per node and the expected side per joint. A relative
       round-off ceiling is the right form and the measured clean value is 1.8726e-16.
```

```
claim  the resultant FORCE alone is blind to a block on the wrong node; the MOMENT is not
cmd    python scratchpad/measure_r676b.py
out    wrong NODE, same body: force 5.2050529737194385e-17  moment 0.24374825705420716
out    sign NOT flipped on the platform side  0.9202048893902944
cell   one block moved to another node of the SAME body, with the blocks, the bodies and
       every other node held.
judge  that is why the moment about the origin is part of the quantity rather than a
       second check, and why the counter is taken from the wrong-node injection: it is
       the SMALLER of the two defects the gate must catch.
```

```
cmd    python scratchpad/sweep_f4_mapping_conservation.py
out    WEAKENING                        TIGHTENING
out      1.0e-12  434 passed  0 failed    1.0e-12  434 passed  0 failed
out          0.1  433         1  plan         1.0e-15  433      1  plan
out          0.2  432         2  + the counter bracket
out          0.3  431         3  + test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node
out          1.0  430         4  + the same, both parametrisations
out                                        1.0e-16  432      2  + test_G4_4_the_mapping_
out                                                                CONSERVES_the_joint_resultants
out    restored; git status --short clean
rule   clean value 1.8726e-16, so the shipped 1.0e-12 sits 5341x above it
```

**What this gate does NOT check, stated:** that `joint_order` matches the deck's. It
builds the wiring from the builder's own maps so it can run without an HSP worktree —
R670's lesson — and the deck's authority over the order is the driver's business.

**(iii) EK0(a) the premise** — as an assertion, and it is a DIFFERENT statement from the
report's figure.

```
claim  no body outside the twelve buoys carries a hydro_body_label in HSP-stable
cmd    python -m pytest tests/verification/rung4 -q -k EK0a
out    5 passed, 145 deselected in 0.38s
rule   EK0's scope correction: the five FE bodies are DRY, and EK0(a) says STOP if not
judge  the report measured a SAMPLE -- 24,006 steps over six cases, all
       `0.000000e+00 N`. This asserts the STRUCTURAL reason it is zero: no excitation
       channel addresses a body with no label, so nothing is relying on cancellation.
       The sample cannot run in CI without an HSP worktree and a gate that skips turns
       its rung red; this one runs wherever the snapshot does.
```

```
claim  the snapshot records the label sites and `--check` compares them
cmd    python -c "import json,pathlib; print(json.loads(pathlib.Path('data/platform/buoy_centers_ref.json').read_text())['hydro_body_label_sites'])"
out    ['f"buoy{k + 1}"']
judge  one site, in `platform_common.py:140`, and it can only ever produce `buoy<n>`. The
       counter-case runs THE GATE'S OWN CHECK on four corrupted values rather than
       restating the assertion -- `duality_residual(a, -a)` was found passing for exactly
       that reason and this file is written after that finding.
```

**What it does NOT catch:** a body that acquires a label AFTER this blob. `--check` in the
DS0 preflight is what sees that. Same limitation as EB6's first side, same reason, and
both say so in their own docstrings.

**The fourth row, EB6's hub extension**, ships in the same file, asserting all four hub
joints against the snapshot's `hub_positions_xyz_m`.

```
claim  the hub side asserts all four joints and reads the pinned snapshot
cmd    grep -n 'checked == 4' tests/verification/rung4/test_f4_static_and_mapping.py
out    409:    assert checked == 4, f"{checked} of 4 hub joints were checked, not all of them"
judge  the provenance line in § 2 names `the hub Body :157`, which is the line DQ9
       required the extension to cite.
```

## 9. R677 and R663 — omission raises

```
claim  `member_forces` has no default for the equivalent load; omission is a TypeError
cmd    grep -n 'f_eq_global' floatfea/post/member_forces.py | head -3
out    HUNK_R677
judge  the verdict asked for "it raises, it never defaults" and offered a sentinel as the
       cheap form. A REQUIRED argument is cheaper and stronger: a sentinel can be passed
       by a caller who has not thought about it, and a missing argument cannot be. The
       three counter-case call sites that need the defective path pass `np.zeros(12)`
       explicitly, which is the defect STATED rather than forgotten.
```

## 10. R678 and R668 — the both-zero duality case raises

```
claim  `duality_residual` raises when both shares are zero
cmd    grep -n -A6 'if scale == 0.0' floatfea/loads/joint_reactions.py
out    HUNK_R678
judge  it returned `0.0`, the same number a satisfied law returns, so the published
       `0.000e+00` could not distinguish a satisfied law from an absent load. It now
       cannot be reached silently. The window figure is a statement about a law.
```

## 11. EO0 to EO4 — the directives this round carried, each with its measurement

**EO2. The hand-rolled Froude arithmetic is gone, and what it got wrong is not what I
expected.**

```
claim  the two conversions that EXISTED were numerically identical to the converter
cmd    python scratchpad/eo2_cell.py
out    period (full->model)  1.9798989873e+00 vs 1.9798989873e+00  ratio 1.0000000000x
out    length (model->full)  3.9000000000e+02 vs 3.9000000000e+02  ratio 1.0000000000x
judge  so removing them moved nothing, and the report should not claim they were wrong.
```

```
claim  the defect was a conversion that was MISSING, at an implicit lambda^0
cmd    python scratchpad/eo2_cell.py
out    rows 0:3 (force)   lambda^0 = 1  vs  lambda^3   short by a factor of 125,000
out    rows 3:4 (moment)  lambda^0 = 1  vs  lambda^4   short by a factor of 6,250,000
out    T_full 14.0s: model 6.7570e+01 N -> full 8.4462e+06 N, ratio 124,999x
rule   the ratio of the driver's own two printed numbers identifies the row: lambda^3 is
       a force row, lambda^4 would be the moment row
judge  all five printed cases give 124,996x to 125,001x and never 6,250,000x, so the
       governing entry is a force row in each. `res.lam` entered the sum at 8.000e-06 of
       its true size.
```

**EO4. Preview issue 3**, at `docs/reports/F4/preview-PRELIMINARY.md`: static-only,
dynamic-only and total columns separated, one table per component, plus EK1's `f`
sensitivity at 0.25 and 0.75.

```
claim  issue 2's dynamic columns did not change by any digit
cmd    python scratchpad/make_issue3.py
out    worst dynamic move vs issue 2: 0.000e+00   worst total move: 0.000e+00
rule   |a-b| / max(|a|,|b|) per component per member over the dyn and tot envelopes
judge  expected, and not a tautology: the conversions that were removed were exact
       equivalents and the one that was missing had already been repaired before issue 2.
```

```
claim  f moves My and does not move Vz at all
cmd    python scratchpad/eo4_fsens.py
out    member                 Vz@.25      Vz@.50      Vz@.75   My .25/.50   My .75/.50
out    platform:hubN_arm  3.0656e+06  3.0656e+06  3.0656e+06       1.1667       0.8333
out    hubN:buoyM_arm     5.9269e+06  5.9269e+06  5.9269e+06       1.1304       0.8696
out    worst relative Vz move over the whole table: 8.882e-16
out    admissible=True on all 5 bodies at f = 0.25, 0.50 and 0.75; min eig(J_r) 3.7920e+07
out    f=0.75: the four hubs' equivalent density is 11433.5 kg/m^3, above steel at 7850
judge  f moves mass between two places both inside the member's span, so the total
       carried weight is conserved exactly and the root shear is fixed; what f changes is
       the lever. The static root moment therefore carries a modelling band of about
       +-17% from f alone and the shear carries none.
cell   f set to 0.25, 0.50 and 0.75 with the geometry, the sections, the deck mass and
       the support scheme held; one variable.
```

**And `f = 0.75` is admissible, which was a question and not an assumption**: all five
bodies PSD at all three fractions, minimum eigenvalue `3.7920e+07`. At `f = 0.75` the four
hubs carry a second finding — equivalent density `11433.5 kg/m^3`, above steel at 7850 —
and the platform stays below steel everywhere. Reaching 0.25 and 0.75 needed an optional
`build_superstructure(mass_fraction=...)` because neither is on the ladder and 0.75 is
above its first rung; it bypasses `admissible()` and reports a finding on every body
saying so, and the default path is bit-identical.

**EO1's analytic gate and EO0's snapshot** shipped in the previous commit and the verdict
read them. **EO3**: my non-reproduction of R675's "0 assertions" half stands as recorded.

## 12. Findings answered

Generated: `python scripts/answered_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R622 | carried | **carried** | §14b | `` | carried from an earlier verdict |
| R626 | carried | **carried** | §14b | `` | carried from an earlier verdict |
| R631 | carried | **carried** | §14b | `` | carried from an earlier verdict |
| R635 | carried | **carried** | §14b | `` | carried from an earlier verdict |
| R637 | carried | **answered** | §16 | `` | carried from an earlier verdict |
| R638 | carried | **carried** | §14b | `` | carried from an earlier verdict |
| R653 | carried | **carried** | §14b | `` | carried from an earlier verdict |
| R654 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R655 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R656 | carried | **carried** | §14b | `` | carried from an earlier verdict |
| R657 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R658 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R659 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R660 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R661 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R662 | carried | **answered** | §14a | `` | carried from an earlier verdict |
| R663 | recorded | **answered** | §9 | `` | , A DEFECT IN `floatfea/`.) `floatfea/post/member_forces.py:78` |
| R664 | recorded | **answered** | §6 | `` | , A GATE ASSERTION THAT CANNOT FAIL.) |
| R665 | recorded | **answered** | §4 | `` | .) THE EK0(d) SUPPORT-SCHEME CHECK CANNOT FAIL, AND NO THRESHOLD IS |
| R666 | recorded | **answered** | §5 | `` | , THREE RED TESTS THAT ARE NOT THE MILESTONE BOUNDARY, AND CI IS |
| R667 | recorded | **answered** | §2 | `` | .) EB6's GATE DOES NOT EXIST, AND REPORT SECTION 7 REPORTS A SECOND |
| R668 | recorded | **answered** | §10 | `` | .) THE EK0(e) DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE STATE |
| R669 | recorded | **answered** | §8 | `` | .) FOUR GATE ROWS THE LOCKED PLAN MARKS "TO BE MEASURED AT STEP 1" |
| R670 | recorded | **answered** | §2 | `` | , CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4.) |
| R671 | recorded | **answered** | §3 | `` | , A TOLERANCE WHOSE CEILING NOTHING BOUNDS ABOVE.) |
| R672 | recorded | **answered** | §4 | `` | , CARRIED FROM VERDICT 93 AND UNANSWERED.) R665 IS UNTOUCHED AT |
| R673 | recorded | **answered** | §5 | `` | , 39 RED TESTS AT THE REVIEWED COMMIT AND NOT ONE IS A BOUNDARY |
| R674 | recorded | **answered** | §6 | `` | and (c), THE COUNTER-CASE DOES NOT RUN THE INJECTION IT NAMES, AND |
| R675 | recorded | **answered** | §7 | `` | , TWO GATES WHOSE REACH IS NARROWER THAN THE TABLE CLAIMS, ONE OF |
| R676 | recorded | **answered** | §8 | `` | , CARRIED FROM VERDICT 93 AND ANSWERED FOR ONE ROW OF FOUR.) THREE |
| R677 | recorded | **answered** | §9 | `` | and (b), R663 CLOSING CONDITION SECOND BRANCH IS NOT MET: IT |
| R678 | recorded | **answered** | §10 | `` | , R668 SECOND CLAUSE, UNTOUCHED.) `duality_residual` STILL RETURNS |

## 13. Sites named by findings and not touched

Generated: `python scripts/untouched_sites.py`, which reads the guard's OWN site list --
`tests/test_report_carried.py`'s `SITES` -- rather than forming a second opinion. Every
row is either a hunk in this round's range or a stated reason it was left.

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R663 | `floatfea/post/member_forces.py:78` | the file is touched and this line number is the old one || **no change** at `:78` — the subtraction moved to `:130` and the required argument is at `:96` |
| R664 | `floatfea/solve/static.py:92` | the file is touched and this line number is the old one || **no change** at `:92` — `sum_error` is at `:91-98` and was ALREADY a signed sum; the `abs()` that was blind was in the test file and is fixed in § 6 |
| R665 | `floatfea/loads/selfweight.py:86` | the file is untouched || **no change** — R672 is answered by WITHDRAWING the claim (§ 4), not by changing the restraint, which the measurement shows is not the thing at fault |
| R667 | `docs/closure/F3.md:179` | the file is untouched || **no change** — F3's closure artifact is closed; EK3 routes post-closure prose and it does not open a round |
| R667 | `tests/verification/rung3/test_platform_skeleton.py:711` | the file is untouched || **no change** — rung 3's skeleton test is not EB6's gate; EB6 ships at rung 4 and § 2 carries it |
| R668 | `joint_reactions.py:89` | the file is touched and this line number is the old one || **no change** at `:89` — the `raise` is at `:61-70`, which § 10 shows |
| R670 | `scripts/run_rung.sh:274` | the file is untouched || **no change** — the ladder script is RIGHT and the gate was wrong; the skip is gone, not the rule |
| R670 | `scripts/run_rung.sh:275` | the file is untouched || **no change** — as `:274` |
| R670 | `scripts/run_rung.sh:276` | the file is untouched || **no change** — as `:274` |
| R671 | `floatfea/tolerances.py:1888` | the file is touched and this line number is the old one || **no change** at `:1888` — the entry is at `:1893` and its value is unmoved; what changed is the counter-case in the test file, § 3 |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:89` | the file is untouched || **no change** — the verdict said do NOT extend this guard, and the `_COUNTER` suffix is the whole repair |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:90` | the file is untouched || **no change** — as `:89` |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:91` | the file is untouched || **no change** — as `:89` |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:92` | the file is untouched || **no change** — as `:89` |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:93` | the file is untouched || **no change** — as `:89` |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:94` | the file is untouched || **no change** — as `:89` |
| R672 | `floatfea/loads/selfweight.py` | the file is untouched || **no change** — the restraint is not what was wrong; the claim about it was, and § 4 withdraws it at both named sites |
| R673 | `scripts/suite_count.py` | the file is untouched || **no change** — the script was correct and simply had not been run; § 16 now carries its output, taken after the last edit |
| R674 | `static.py:86` | the file is touched and this line number is the old one || **no change** at `:86-91` — `sum_error`'s own docstring already said the sign is "the one error this check exists for", and that sentence was TRUE; the gate that ignored it is the test, fixed in § 6 |
| R674 | `static.py:87` | the file is touched and this line number is the old one || **no change** — as `:86` |
| R674 | `static.py:88` | the file is touched and this line number is the old one || **no change** — as `:86` |
| R674 | `static.py:89` | the file is touched and this line number is the old one || **no change** — as `:86` |
| R674 | `static.py:90` | the file is touched and this line number is the old one || **no change** — as `:86` |
| R674 | `static.py:91` | the file is touched and this line number is the old one || **no change** — as `:86` |
| R677 | `floatfea/post/member_forces.py:95` | the file is touched and this line number is the old one || **no change** at `:95` — the signature's required `f_eq_global` is at `:96`, one line down, and § 9 carries it |

## 14. Carried

Generated: `python scripts/carried_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R622 | **carried** — §14b | F4's own, not yet reached. |
| R626 | **carried** — §14b | 's residue, R635 and the long closed |
| R631 | **carried** — §14b | 's residue, R635 and the long closed |
| R635 | **carried** — §14b | no clause this generator can cut -- see the verdict's Carried section |
| R637 | **answered** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R638 | **carried** — §14b | OPEN, unchanged, EJ1 governs, closed before F4 closes. floatfea/tolerances.py |
| R653 | **carried** — §14b | OPEN, carried, and about to become (c). A grep for RHO_INF over tests and |
| R654 | **answered** — §14a | CLOSED, not reopened, nothing in this range touches their sites. |
| R655 | **answered** — §14a | CLOSED, not reopened, nothing in this range touches their sites. |
| R656 | **carried** — §14b | OPEN WITH XABIER, unchanged, correctly not repaired. scripts/ci_section.py is |
| R657 | **answered** — §14a | ANSWERED AND CLOSED at e505f28. The word is mine. Section 8 carries the |
| R658 | **answered** — §14a | ANSWERED AND CLOSED at e505f28, same constant, same commit, same reading. |
| R659 | **answered** — §14a | CLOSED, not reopened, nothing in this range touches their sites. |
| R660 | **answered** — §14a | ANSWERED at 0c490bf, the standalone closure commit verdict 92 said was worth |
| R661 | **answered** — §14a | ANSWERED in report section 8, where EK3 puts it, and the cause is correctly |
| R662 | **answered** — §14a | no clause this generator can cut -- see the verdict's Carried section |
| R663 | **answered** — §9 | , A DEFECT IN floatfea/.) floatfea/post/member_forces.py:78 RETURNS THE ELEMENT NODAL FORCE AND... |
| R664 | **answered** — §6 | , A GATE ASSERTION THAT CANNOT FAIL.) floatfea/solve/static.py:92: StaticCase.sum_error IS AN... |
| R665 | **answered** — §4 | .) THE EK0(d) SUPPORT-SCHEME CHECK CANNOT FAIL, AND NO THRESHOLD IS DECLARED FOR IT.... |
| R666 | **answered** — §5 | , THREE RED TESTS THAT ARE NOT THE MILESTONE BOUNDARY, AND CI IS RED AT THE REVIEWED COMMIT.)... |
| R667 | **answered** — §2 | .) EB6's GATE DOES NOT EXIST, AND REPORT SECTION 7 REPORTS A SECOND SIDE TO A FIRST SIDE THAT... |
| R668 | **answered** — §10 | .) THE EK0(e) DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE STATE THE DOCSTRING NAMES IS... |
| R669 | **answered** — §8 | .) FOUR GATE ROWS THE LOCKED PLAN MARKS "TO BE MEASURED AT STEP 1" HAVE NO ASSERTION ANYWHERE,... |
| R670 | **answered** — §2 | , CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4.)... |
| R671 | **answered** — §3 | , A TOLERANCE WHOSE CEILING NOTHING BOUNDS ABOVE.) floatfea/tolerances.py:1888... |
| R672 | **answered** — §4 | , CARRIED FROM VERDICT 93 AND UNANSWERED.) R665 IS UNTOUCHED AT EVERY SITE ITS CLOSING... |
| R673 | **answered** — §5 | , 39 RED TESTS AT THE REVIEWED COMMIT AND NOT ONE IS A BOUNDARY RED.) Section 8 traces all 39... |
| R674 | **answered** — §6 | and (c), THE COUNTER-CASE DOES NOT RUN THE INJECTION IT NAMES, AND THE GATE IS SIGN-BLIND ON... |
| R675 | **answered** — §7 | , TWO GATES WHOSE REACH IS NARROWER THAN THE TABLE CLAIMS, ONE OF THEM VACUOUSLY PASSABLE.)... |
| R676 | **answered** — §8 | , CARRIED FROM VERDICT 93 AND ANSWERED FOR ONE ROW OF FOUR.) THREE OF R669 FOUR GATE ROWS STILL... |
| R677 | **answered** — §9 | and (b), R663 CLOSING CONDITION SECOND BRANCH IS NOT MET: IT DEFAULTS.)... |
| R678 | **answered** — §10 | , R668 SECOND CLAUSE, UNTOUCHED.) duality_residual STILL RETURNS 0.0 FOR A BOTH-ZERO SHARE,... |

### 14a. Answered earlier in F4 step 1, and not reopened

* **R654, R655, R657, R658, R659, R660, R661, R662** — closed at verdict 93. Nothing in
  this round's range touches their sites. They are rows above because verdict 94's
  `Carried` section names them, and their absence from revision 2's hand-written table
  was part of R673 (i).

### 14b. Open, not answered in this round

* **R638** — open under EJ1, which requires it answered before F4 ends. The six F4
  tolerance entries this step added do not touch it.
* **R653** — open, carried, becomes (c) at step 2. A grep for `RHO_INF` over `tests` and
  `floatfea` still returns nothing.
* **R656** — open with Xabier. `scripts/ci_section.py` is not in this round's range.
* **R622, R626, R631, R635** — on the EJ3 ledger at `docs/closure/F3.md` § 8, unchanged
  and not re-reviewed (CZ0).

### 14c. Closure items

**C135 to C151 are open and go into the step closure commit, not re-reviewed item by item
(CZ0).** Two are answered early because they are about the honesty of a gate that changed
in this round rather than about prose: **C146** in § 2 and **C148** in § 4. **C144, C145
and C147** are figures in revision 2's section 13 and 16 that the verdict measured as
stale or miscounted; they are corrected in the closure commit with the machine named.
**C149** and **C150** are a wrong word in a tolerance comment and a plan row that says
"both edges solved" where the lower edge is vacuous. **C151** is revision 1's section 1a,
which EK3 governs.

## 15. Tolerances touched

**TWO DECLARED, NONE MOVED.** No existing value, form, counter or injection changed.

| constant | old | new | form | counter | injected by |
|---|---|---|---|---|---|
| `F4_STATIC_SYMMETRY_SPREAD` | none | `1.0e-12` | dimensionless, relative | `..._COUNTER = 1.5` | `test_EK0d_the_symmetry_gate_REDDENS_on_an_unsymmetric_frame` |
| `F4_STATIC_SYMMETRY_SPREAD_COUNTER` | none | `1.5` | dimensionless | is the counter | the same test |
| `F4_MAPPING_CONSERVATION` | none | `1.0e-12` | dimensionless, relative | `..._COUNTER = 0.2` | `test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node` |
| `F4_MAPPING_CONSERVATION_COUNTER` | none | `0.2` | dimensionless | is the counter | the same test |

Both counters are round bounds declared BELOW their measured injection, and the
counter-case asserts an ordering rather than a windowed equality.

```
claim  each declared counter sits below the injection it names
cmd    python scratchpad/measure_r676.py ; python scratchpad/measure_r676b.py
out    symmetry, one arm softened 100x          : 1.5616518375226505   declared 1.5
out    mapping, a block on the wrong node       : 0.24374825705420716  declared 0.2
out    mapping, a sign not flipped              : 0.9202048893902944   (the larger one)
rule   the counter is the smallest defect the gate must still fail, so the declared
       value is below the measurement and the gate's assertion is `measured > counter`
```

```
claim  the first version used `approx(rel=1.0e-9)` and the literal guard refused it
cmd    python -m pytest tests/test_no_tolerance_literals.py -q
out    line 592: approx(rel=<literal>)
out    line 593-760: approx(rel=<literal>)
out    Declare the value in floatfea/tolerances.py, use floatfea.testing.assert_close, or
out    annotate `# not-a-tolerance: ...`
judge  the guard was right and `# not-a-tolerance:` would have been false -- a relative
       window on a measured spread IS a comparison tolerance. A bit-exact equality on a
       solve-derived number is not portable to CI's platform either, so the counters
       became bounds and the assertions became orderings.
```

```
claim  no tolerance literal reaches a comparison, and both ceilings are bracketed
cmd    python -m pytest tests/verification/rung4 tests/test_no_tolerance_literals.py
         tests/test_plan_matches_tolerances.py
         tests/verification/rung3/test_tolerance_counter_cases.py -q
out    434 passed in 2.12s
rule   BR0: a tolerance moves with a plan edit
judge  four rows added to `docs/milestones/F4.md` § 5a in the same commit as the
       constants. Every perturbation of either ceiling reddens
       `test_the_plan_and_the_code_agree`, which is the pairing working.
```

## 16. The whole suite

Generated by `python scripts/suite_count.py`, run AFTER every other edit (CP3, and R637
clause (iii)).

**Whole suite at `6cf4efe`: 2745 passed, 2 failed, 0 skipped.** **The excluded set: 138 passed, 35 failed, 1 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 174 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed** `tests.test_report_vocabulary_corpus::test_the_guard_rules_on_the_spelling[legitimate_open_row]`
- **failed** `tests.test_report_vocabulary_corpus::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R622]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R626]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R631]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R635]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R637]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R654]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R655]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R657]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R658]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R659]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R660]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R661]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R662]`
- **failed, in the excluded set** `tests.test_report_carried::test_a_report_does_not_say_CLOSED`
- **failed, in the excluded set** `tests.test_report_carried::test_the_Carried_table_is_what_the_generator_produces`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_a_CI_SECTION`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`
- **failed, in the excluded set** `tests.test_report_carried::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_section_is_about_the_REVIEWED_commit`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_a_WHOLE_SUITE_count`
- **failed, in the excluded set** `tests.test_report_carried::test_the_reported_CI_counts_are_not_all_zero`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R664-floatfea/solve/static.py:92]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R665-floatfea/loads/selfweight.py:86]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R667-docs/closure/F3.md:179]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R667-tests/verification/rung3/test_platform_skeleton.py:711]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R668-joint_reactions.py:89]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]`
```

**The two failures OUTSIDE the excluded set are the cascade, and they clear with this
commit.** `test_the_guard_rules_on_the_spelling[legitimate_open_row]` and
`[two_spaces_before_the_item_number]` both report "the corpus requires `allowed` and the
shipped guard says `refused`, reported by `test_a_report_does_not_say_CLOSED`" — and that
guard is red at `6cf4efe` because the R638 row still carried the word `closed` there. The
row is fixed in THIS revision's commit, which `6cf4efe` does not contain.

**That is CZ1's class exactly: a check whose input is the commit itself cannot be measured
before the commit exists.** `scripts/suite_count.py` builds a clean worktree at the sha, so
it cannot see an uncommitted report, and "I ran it before committing" is not a measurement
for the three files parametrised over this report. The re-run AT this revision's own commit
is below, taken after it existed.
