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
       0.000e+00 on all five bodies. A vertical load system can induce no horizontal
       reaction in a determinate restraint, so this zero is what proves vertical-only
       joints plus a minimal restraint is the right scheme rather than a convenient one.
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
judge  N = 0 because gravity is vertical and every member lies in the joint plane;
       Vy = Mz = 0 because nothing loads horizontally. The tip shear reconciles by
       hand: the 3065625 N support reaction less half the member's own
       156250 x 9.81 = 1533000 N weight gives 2.2996e+06 against the computed
       2.2992e+06.
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
| R657, R658 | **CLOSED** at `e505f28` under EK2 — the plant locators are anchored, one pattern serving both sites |
| C119 | **CLOSED** at `9020c6c` under EK2 — the id prefix is consumed outside the capture |
| R656 | **ledgered** after 28 Oct per EK2, unchanged |

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
