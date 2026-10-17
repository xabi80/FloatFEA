# Report — R1 step 2

# Revision 1 — FQ0–FQ3 answered, a third refusal site nobody had named, and the date

Answers: verdict 5 @ a777cc3

## 0. CI at `cfb76ff`, the commit verdict 5 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 5 at `cfb76ff` through the report's own `Answers:` line. Run `38927091674`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1124 | 13 | 1 |
| the verification ladder | 2292 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 13.**

- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 5 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 5 at `cfb76ff` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `38927091674` | push | `cfb76ff` | conclusion **failure** |

**Run `38927091674`, conclusion **failure**: 13 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 1. The schedule, and what this revision is

**This is step 2's first reviewed revision.** The interim check at `a777cc3` counted
against no round under ES0, so all three revisions remain. It ruled PASS with four
blocking findings — R825, R826, R827, R828 — and recorded R829, R830 and C22. **DIRECTIVE
FQ ruled on every one of them before I touched it**, so this revision is the execution of
FQ0–FQ3 and not my own reading of the findings.

**THE 28 OCTOBER DATE DOES NOT HOLD FOR R1 COMPLETE, AND I AM REPORTING IT THE DAY I KNOW
IT (FQ5).** Step 3 is what does not fit. The per-item estimate is in §9 with its
assumptions, and the scope is unchanged — FQ4 said do not trim, and nothing below is
trimmed. What I am reporting is the date, not a reduced milestone.

```
claim  the four blocking findings and the three recorded items of verdict 5
cmd    git log -1 --format=%B a777cc3 | grep -oE "R8[0-9]{2}|C22" | sort -u | tr '\n' ' '
out    C22 R825 R826 R827 R828 R829 R830
claim  the date, which is §9's subject and is stated here because FQ5 asks for it early
out    R1 complete        5 November      (§9's table and its assumptions)
       step 2's own gate  29-30 October
       the target         28 October       does NOT hold for R1 complete
out    step 2's own gate  29-30 October     R1 complete  5 November
out    the target         28 October        does NOT hold for R1 complete
rule   FQ5: a realistic finish date, the remaining items, and the estimate per item
``` The per-item estimate is in §9 with its assumptions, and the
scope is unchanged — FQ4 said do not trim, and nothing below is trimmed. What I am
reporting is the date, not a reduced milestone.

## 2. R825 / FQ1 — a name key is a string, and the coercion is deleted

**R825 is the layer below R822, and R822's repair could not reach it.** `_no_duplicates`
compares the keys PyYAML will *build*, so it catches `no`/`No` (both `False`). It is
correctly silent when YAML builds two *distinct* keys — and the bool `True` and the string
`'True'` are exactly that. The schema then coerced both with `str(g)`, and one of two
declared line masses was gone.

```
claim  two declared line masses became one, before this repair
cmd    python -c "import yaml; print(yaml.safe_load(\"{true: 100.0, 'True': 900.0}\"))"
out    {True: 100.0, 'True': 900.0}        <- PyYAML keeps BOTH
       {'True': 900.0}                     <- after the schema's str(g), last-wins
rule   FQ1: name-keyed mappings REQUIRE string keys; delete the str(g) coercion
judge  the comparison was right and the COERCION was the defect. Refused now, not coerced.
```

FQ1 names `line_masses` and `sections.groups`. I applied it to a third mapping on the same
argument — `mass_distribution`'s body names, where `{no: ...}` would arrive as `False` and
match no body the deck declares.

```
claim  no str() coercion on a name key survives anywhere in the schema
cmd    grep -n "str(g)\|str(name)" floatfea/run/config.py
out    (no output)
cmd    grep -c "_require_name_keys" floatfea/run/config.py
out    4
judge  one shared check, three call sites, and the message says **Quote the name.**
```

## 3. R827 / FQ0 — the flat 300, and a THIRD site the directive's own gate did not drive

FQ0 ruled § 3.2.3's third range ends at a flat `D/t <= 300`, overruling FB1's
`300000/F_y`, and named `300000/Fy` as Xabier's own error. `BENDING_THIRD_BRANCH_NUMERATOR
= 300000.0` is replaced by `BENDING_THIRD_BRANCH_MAX_D_OVER_T = 300.0`, eleven rung-5 tests
moved with it, and the caveat in all three artifacts states `D/t <= 300`.

**AND THE REQUIRED GATE, AS I FIRST WROTE IT, DROVE ONE ENTRY POINT OUT OF THREE.** FQ0
says "refuse `D/t > 300` at every site" and "a test asserts that `D/t = 300` is accepted and
`300.01` is refused, through the public entry point**s**". My gate drove
`allowable_bending` only. `local_buckling_stress` — public, exported, and called directly
by `scripts/measure/r754_stress_vs_grade.py` — refused nothing:

```
claim  local_buckling_stress admitted everything, and went NEGATIVE far outside the clause
cmd    python -c "from floatfea.basis import FY_S355; from floatfea.checks.api_wsd import \
       local_buckling_stress as f; [print(dt, f(2.5, 2.5/dt, FY_S355)) for dt in \
       (300.01, 845.0, 1e4, 1e6)]"
out    300.01     +2.423869e+08     returned
       845.0      +1.419794e+08     returned
       10000      -2.343000e+08     returned, NEGATIVE
       1000000    -1.999800e+09     returned, NEGATIVE
rule   FQ0: refuse D/t > 300 at EVERY site
judge  `F_xc = F_y [1.64 - 0.23 (D/t)^(1/4)]` crosses zero at `(1.64/0.23)**4 = 2585`, so
       this returned a buckling stress with the WRONG SIGN. `allowable_axial_compression`
       refused above 300 and never saw it; a direct caller did -- the one in
       `scripts/measure/r754_stress_vs_grade.py`.
cmd    git diff floatfea/checks/api_wsd.py | grep -cE "^-.*BENDING_THIRD_BRANCH_NUMERATOR"
out    the retired constant was `BENDING_THIRD_BRANCH_NUMERATOR = 300000.0`, read as
       `300000/F_y[MPa]`, which FQ0 names as FB1's own error
```

A second defect at the same clause: the § 3.2.2 refusal message was **false at its own
boundary**, because `{d_t:.1f}` rounds the input to the ceiling it is being compared against.

```
claim  refusing an input of D/t = 300.01 printed a self-refuting sentence
cmd    git diff floatfea/checks/api_wsd.py | grep -E "^[-+].*d_t:\.(1f|6g)"
out    -            f"D/t = {d_t:.1f} exceeds 300, beyond which API section 3.2.2 is not written. "
       +            f"D/t = {d_t:.6g} exceeds {BENDING_THIRD_BRANCH_MAX_D_OVER_T:.0f}, beyond "
rule   FO0's wording, applied to this site: the message is true of every value it refuses
out    before: "D/t = 300.0 exceeds 300, ..."   <- 300.0 does not exceed 300
       after : "D/t = 300.01 exceeds 300, ..."
judge  it sent a reader looking for a defect in the comparison instead of at their section.
```

A third, smaller: the axial site carried the ceiling as a **bare literal `300.0`**, a second
copy of the same number. It now reads the named constant. **That substitution is
behaviour-neutral and is NOT held by a test** — the cycle in §4 holds the ceiling's
*value*, not the fact that one site reads the other's name. I am saying so rather than
implying the cycle covers it.

The boundary, as it now stands at every entry, four grades each:

```
claim  300 accepted and 300.01 refused at every entry that returns a capacity
cmd    python -m pytest -q tests/verification/rung5 -p no:randomly -k FQ0
out    11 passed, 76 deselected in 0.14s
rule   FQ0's own requirement, through the public entry points
out    local_buckling_stress         300.00 ACCEPTED   300.01 REFUSED
       allowable_axial_compression   300.00 ACCEPTED   300.01 REFUSED
       allowable_bending             300.00 ACCEPTED   300.01 REFUSED
       section_class                 300.00 reduced_2  300.01 slender  (classifier; no capacity)
judge  `section_class` is deliberately not a refusal site: it returns no capacity, and
       `slender` is the honest label above the ceiling. Both halves of that split are
       asserted so neither can drift.
```

**R819 closes with this**, per FQ0: the caveat, the code and the gate now state one number.

## 4. R826 and R828 / FQ2 — every repair held, and the cycle pasted

FQ2 required the revert-red-restore cycle for R822, R823, R825, R817 and R818, the last at
the generator rather than the committed file. R826 and R828 are the findings that nothing
held those repairs; both were correct.

```
claim  each repair is held by a test that fails when the repair alone is reverted
cmd    python <scratch>/cycles.py        (revert -> run -> restore, one anchor each)
out    R822  (count check deleted; text check untouched)
         reverted -> 5 failed, 24 passed      restored -> 29 passed
       R823  (merge-key refusal made inert)
         reverted -> 1 failed, 28 passed      restored -> 29 passed
       R825  (name-key check removed from line_masses)
         reverted -> 4 failed, 25 passed      restored -> 29 passed
       R817  (exported_wave_basis returns {})
         reverted -> 2 failed, 27 passed      restored -> 29 passed
       R818  (code_check_sensitivities deleted from provenance)
         reverted -> 1 failed, 28 passed      restored -> 29 passed
rule   FQ2: every repair is held by a test that fails when the repair is reverted
judge  R828's specific point is answered by asserting on `provenance()` and on
       `exported_wave_basis` THEMSELVES. The CSV header check could not serve: it DERIVES
       its expectation from `provenance()`, so deleting a key moves the expectation with it.
```

And the three new repairs of §3, by the same method:

```
claim  the FQ0 repairs are held too
cmd    python <scratch>/fq0_cycles.py
out    the lbs refusal deleted            reverted -> 5 failed, 6 passed   restored -> 11 passed
       the axial message back to `:.1f`    reverted -> 1 failed, 10 passed  restored -> 11 passed
       the ceiling made grade-dependent    reverted -> 7 failed, 4 passed   restored -> 11 passed
rule   FQ2, applied to this revision's own repairs rather than only to the named five
judge  the third cycle holds the VALUE. The literal-to-constant substitution is not held
       by any of them, which §3 states.
```

## 5. R829, R830 / FQ3 — the empty-basis branch, the pins, and A GOLDEN THAT MOVED

**R829.** The CSV path emitted one line with `(not recorded)` substituted field by field, so
a sidecar-less npz produced a file carrying both "the heading … is in the provenance above"
and "heading (not recorded) deg" — two sentences that cannot both be true. FL1(a) admits
such an npz, so it is reachable. `_write_report` already had the branch; the CSV path did
not, which is why the contradiction appeared in two artifacts of three. Both now branch.

**R830, and this is the part that needs reading.** FQ3 said: pin `numpy` and `scipy` and
every package whose version can move a number, and **if the golden moves under the pin,
STOP and report; do not re-baseline silently.**

```
claim  the golden MOVED under the pin
cmd    python -m pytest -q tests/regression -p no:randomly
out    1 failed, 215 passed  --  test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree
out    line 42: shipped '... limits 29.1268 / 58.2535 / 845.0704'
              vs fresh '... limits 29.1268 / 58.2535 / 300.0000'
rule   FQ3: if the golden moves under the pin, STOP and report
judge  ONE line of 464 differs, and it is a section-class LIMIT, not a member force. That
       shape is wrong for a solver bit moving.
```

**The pin was not the mover.** The cell moves one variable — the FQ0 constant — and holds
the pins, the tree and the generator fixed:

```
claim  the shipped 845.0704 regenerates byte-identically at the new pin, once the rule is back
cell   BENDING_THIRD_BRANCH_MAX_D_OVER_T 300.0 -> 300000.0/355.0; pins, tree, generator held
cmd    <patch the constant> ; python -m pytest -q <the R756 id> ; <restore>
out    with FQ0 in place   : 1 line differs  -- line 42, 845.0704 -> 300.0000
       with it reverted    : 2 lines differ  -- lines 154 and 165, the G6.1 gate going FAIL
                             and line 42 AGREES
rule   BP0: when a decision rule changes, every figure citing the old rule is regenerated
       or withdrawn IN THE SAME COMMIT
judge  line 42 is absent from the diff the moment the rule is restored, so the mover is
       FQ0's ruling and not `numpy==2.5.4` / `scipy==1.18.1`. **No number moved under the
       pin.** This is BP0's regeneration, not FQ3's stop condition.
```

So `results/F6/floatfea_results_report.md` is regenerated, and the regeneration touches
exactly the line the rule governs:

```
claim  the regeneration moves ONLY the line FQ0's rule governs
cmd    python scripts/measure/f6_results_report.py ; diff <before> <after>
out    42c42
       <   section class (3.2.3)   : compact   limits 29.1268 / 58.2535 / 845.0704
       ---
       >   section class (3.2.3)   : compact   limits 29.1268 / 58.2535 / 300.0000
judge  one line of 464, and no member force, stress or utilisation moved.
```

**One sentence I wrote was false, and it was false because I wrote it before the run.**
`constraints-dev.txt` said of the golden "It did not [move]". It did move, and the reason
was mine.

```
claim  the premature sentence is corrected to what the measurement says
cmd    git diff constraints-dev.txt | grep -E "^[-+]# (It did not|IT MOVED)"
out    -# It did not -- the ladder and the golden are recorded in the step report at the pin.
       +# IT MOVED, AND THE PIN WAS NOT THE MOVER. One line of 464 in
rule   BF0: a claim without its command is not written
judge  claim first and measurement second is the defect BF0 exists to prevent, and the file
       now carries the claim plus a pointer to this section rather than the table (BI3).
```

**One latent fragility, recorded and not changed.** `scripts/measure/r754_stress_vs_grade.py`
is an EZ0 producer that sweeps to `DT_HI = 300.00` by float accumulation, which now sits
exactly on the refusal boundary.

```
claim  the sweep lands ON the ceiling with zero margin, and refuses nothing today
cmd    grep -n "^DT_LO, DT_HI, DT_STEP" scripts/measure/r754_stress_vs_grade.py
out    45:DT_LO, DT_HI, DT_STEP = 5.00, 300.00, 0.01
cmd    python -c "print(max(5.0 + i*0.01 for i in range(29501)))"
out    300.0            exceeds 300.0: False      margin: 0.000e+00
judge  correct today and refusing none of its 29501 points. One ULP of accumulation the
       other way would start raising inside a deliverable producer. Recorded as a closure
       item rather than changed, because changing it is not a defect repair.
```

## 6. C22 — the cause was the step marker, not the generator

C22 has been carried as "`scripts/ci_section.py` exits 1 on the never-pushed anchor", due
in the last commit and not done, and verdict 5 records that four of thirteen reds are that
guard. **The generator is not defective and its refusal is correct.** A report must not
publish a CI table for a commit that has no run, and refusing rather than warning is what
this repository requires everywhere else.

```
claim  the generator succeeds on a pushed anchor and the anchor was the problem
cmd    grep -n "step-under-execution" docs/milestones/R1.md
out    3:<!-- step-under-execution: 1 -->          <- while step 2 was being worked
cell   one variable moved: the anchor. `cs._anchor = lambda: ("5", <cfb76ff full sha>)`
cmd    python -c "<load ci_section; override _anchor; call section()>"
out    section() SUCCEEDED, length 2171
       | lint, unit and guards | 1124 | 13 | 1 |
       | the verification ladder | 2292 | 0 | 0 |
rule   FF0/EK2: a guard that fails false is fixed or deleted, never extended
judge  the marker read `1`, so `REPORT` resolved to the CLOSED step 1's report, whose
       newest revision answers a verdict that judged `582cde72` -- a pre-FP1 commit that
       was never pushed. The generator was faithfully generating for a closed step. **No
       guard is extended and no new state is invented**; the marker is bumped to 2, which
       FB4 says travels with this report, and §0 above is the generated result.
```

## 7. The suite, lint, and the boundary state

**The whole-suite line `scripts/suite_count.py` produces is not here, for the reason FC1
gives: it measures a clean worktree AT A COMMIT, so a line naming a sha cannot be inside
that sha. It arrives in the follow-on commit with CZ1 (ii) and (iii)'s four outputs.**

```
claim  lint, format and types are green at this commit
cmd    ruff check floatfea tests scripts
out    All checks passed!
cmd    black --check floatfea tests
out    113 files would be left unchanged.
cmd    mypy floatfea
out    Success: no issues found in 42 source files
rule   CZ1 (ii): the gates `pytest` does not run are run and pasted
```

**THE WHOLE-SUITE FIGURE IS OWED AND IS NOT IN THIS COMMIT, AND I AM NOT SUBSTITUTING
SUBSETS FOR IT.** R309/CI1 is that substitution exactly — seven subset counts, every one
correct, while the suite was red on a test in none of the seven. So the number below is
labelled as what it is.

```
claim  the last COMPLETE whole-suite run, and what changed after it
cmd    python -m pytest -q --tb=no -rf
out    21 failed, 3756 passed, 1 skipped, 2 warnings in 931.44s (0:15:31)
rule   CP3: a figure is pasted from the run that produced the artifact it is pasted into,
       and the pasting is the LAST edit
judge  FOUR THINGS CHANGED AFTER IT, so it does NOT describe the committed tree: the four
       `not-a-tolerance:` annotations, black's reformat of one line, the F6 deliverable's
       SECOND regeneration, and this report. Of its 21 reds, 9 were EG3 boundary and 12
       were mine — and those 12 are what the four changes answer.
```

The 12 were: three `test_no_undeclared_tolerance_reaches_a_comparison` files (CZ0 (b) — a
clause constant and a declared input reaching a comparison without the marker), eight
`test_report_numbers_are_sourced` sections, and `test_R756`, which went red a SECOND time
because I regenerated the F6 deliverable before adding the `local_buckling_stress` refusal
instead of after it — CP3's ordering, and I got it wrong the first time.

```
claim  the second regeneration moved only the rung-5 TALLY, no physical number
cmd    diff <the first regeneration> <the second>
out    165c165
       <   G6.1             77 passed
       ---
       >   G6.1             87 passed
cmd    git diff results/F6/floatfea_results_report.md | grep -cE "^[-+][^-+]"
out    4        <- two lines: FQ0's limit, and the tally that moved because I added tests
judge  the tally moved because this revision ADDS ten G6.1 cases. No member force, stress
       or utilisation differs from the committed deliverable.
```

**Why the re-run is not in this commit, measured rather than asserted.**

```
claim  this machine cannot complete the suite today
cmd    Get-CimInstance Win32_Process -Filter "Name='python.exe'" | ? CommandLine -like *tilted_dynamics*
out    8 x tilted_dynamics.py (platform/cluster runs), 8000+ s CPU each, started 07:33
cmd    tr -d '' < <the re-run's log> | grep -oE "\[ *[0-9]+%\]" | tail -1
out    [  9%]     after ~45 min -> ~8 h projected, against a 931 s idle-machine baseline
judge  the suite is contending with PRODUCTION FloatSim runs on this machine. I stopped my
       own run and left the production ones alone. The whole-suite line arrives in the
       follow-on commit under CZ1 (ii)/(iv) — which is where FC1 already puts it, because
       it cannot pass in the commit it describes.
```

**What I did measure after the final edit, named as subsets and not as the suite:**

```
cmd    python -m pytest -q tests/test_no_tolerance_literals.py
out    64 passed
cmd    python -m pytest -q tests/test_report_numbers_are_sourced.py
out    29 passed
cmd    python -m pytest -q tests/verification/rung5 tests/test_no_tolerance_literals.py
out    151 passed
cmd    python -m pytest -q tests/regression/test_f6_deliverable_agrees_with_itself.py
out    20 passed
cmd    python -m pytest -q <the 236 named-site parametrisations>
out    236 passed
judge  these cover the four post-run changes and nothing more. They are NOT the suite.
```

**EG3's enumeration is short a fourth time, and it is measured rather than argued.** At
`cfb76ff` thirteen reds fired. Three of them do not sit where CLAUDE.md's convenience list
puts them:

```
claim  three of the thirteen are verdict-dependent but mis-filed or absent from both lists
cmd    <at bd315a1, a verdict-exists closure commit> python -m pytest -q <the three ids>
out    3 passed in 0.24s
rule   EG3's membership rule: "verdict-dependent, measured against a verdict-exists
       control", the enumeration being a convenience
judge  `test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` is on NEITHER list.
       `test_the_report_carries_a_CI_SECTION` and
       `test_the_reported_CI_counts_are_not_all_zero` are filed under state (1) and fired
       in state (2) -- the same mis-filing EJ2 corrected for two other names. I am NOT
       editing CLAUDE.md's EG3 list: it is adopted by directive, and proposing it is the
       reviewer's to do. Recorded here so it is not found a fifth time by accident.
```

The reviewer reached the same classification independently at `a777cc3`, and this agrees
with it and adds only which names the enumeration misses.

```
claim  the reviewer measured the same control and got the same answer
cmd    git log -1 --format=%B a777cc3 | grep -o "149 passed 0 failed at the bd315a1[^.]*"
out    149 passed 0 failed at the bd315a1 verdict-exists control
judge  independent of my three-id run above, and consistent with it.
```

**Apparatus debris, declared and not touched.** FF0 class, declared rather than repaired
inside this step commit.

```
claim  `git worktree prune` cannot delete the stubs `scripts/suite_count.py` leaves
cmd    git worktree prune -v 2>&1 | grep -c "Permission denied"
out    180
cmd    git worktree list | grep -c "suite-count-"
out    11       <- listed with no directory behind them
judge  a tree whose apparatus is permanently noisy is one where the next real red hides,
       which is FF0's own reason -- but repairing it is not this step's work.
```

## 8. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R1 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R788 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R791 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R804 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R805 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R806 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R807 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R808 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R809 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R810 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R811 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R812 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R813 | **not classified in this verdict** — carried in from an earlier one | carried, and the verdict says nothing further about it here |
| R814 | **answered** — §8a | The admissibility floor is a threshold on a computed result, borrowed from a bound written for... |
| R815 | **answered** — §8a | R806's named minimum list is met for four of nine; five caveats are absent from all three... |
| R816 | **answered** — §8a | No test in this repository reads any artifact under results/R1/example/, so the three published... |
| R817 | **answered** — §8a | The three published artifacts state neither the HEADING nor the WAVE HEIGHT, and two of the... |
| R818 | **answered** — §8a | K_sensitivity and Cm_sensitivity are declared, reach two PUBLISHED COLUMNS, and reach no... |
| R819 | **answered** — §8a | The new R741 / R742 caveat makes two statements about the bending allowable that the code... |
| R820 | **answered** — §8a | R814's repair is held in place by nothing. The same 100.0 kg/m^3 floor, reintroduced through a... |
| R821 | **answered** — §8a | study_only: true permitting an otherwise-refused configuration is now asserted by no test,... |
| R822 | **answered** — §8a | THE DUPLICATE-KEY GUARD NOW KEYS ON THE KEY'S TEXT WHILE PyYAML BUILDS THE DICT FROM THE KEY'S... |
| R823 | **answered** — §8a | The implementer's own question, answered: the continue loses nothing, by measurement, and the... |
| R824 | **answered** — §8a | The environment divergence that produced this red is STRUCTURAL, not a one-off, and "no local... |
| R825 | **answered** — §2 | THE DUPLICATE-KEY COLLAPSE SURVIVES ONE LAYER DOWN, AT THE SCHEMA'S OWN str(). Two declared... |
| R826 | **answered** — §4 | NOTHING IN tests/ HOLDS THE R822 OR R823 REPAIR. Both halves of this commit's loader fix can be... |
| R827 | **answered** — §3 | THE CORRECTED R741/R742 CAVEAT NAMES A D/t CEILING 15% ABOVE WHERE THE CODE ACTUALLY REFUSES,... |
| R828 | **answered** — §4 | R817's AND R818's REDDENING HALF HOLDS THE COMMITTED FILE AND NOT THE GENERATOR. The heading,... |
| R829 | **answered** — §5 | The implementer's question 5, answered: (not recorded) is the right choice, and the caveat... |
| R830 | **answered** — §5 | The implementer's question 2, answered: the direction is right, and constraints-dev.txt's own... |

**Thirteen of the thirty-one rows are not findings of this verdict**, and §8a says which
group each belongs to. The `R1` row is the milestone's own name — the generator's mention
pattern matches `R1` wherever a verdict names the milestone, so every R-series report
carries a spurious `R1` row. FF0-class apparatus, declared rather than touched inside a
step commit, as in step 1's revisions 2 and 3.

## 8a. The named sites, declared one by one

**Every site below is declared at that exact line number**, and where the site belongs to
one of this round's findings the substance is answered in the section named beside it. The
repairs moved lines, so a line number quoted from a verdict's prose is not a line number in
this diff.

**Three groups, and only one is this round's work.** R814, R815 and R816 were answered in
**step 1 revision 3**, and step 1's closure verdict `2042c56` was PASS — under DD1 that step is
closed. R817–R824 were answered in **`cfb76ff`**, step 2's first commit, and verdict 5
rules on each in its own table. Both groups are declared again here because the guard reads
the NEWEST revision, so a declaration in an earlier one no longer counts — that is the
mechanism step 1 revision 3 recorded, not a re-opening. The `R1` row is the milestone's own
name, which the generator's mention pattern matches wherever a verdict names the milestone;
`R788` and `R791` stay on the F6a and F6b ledgers.

```
claim  every site the newest verdict names is answered or declared, by exact name
cmd    python -m pytest -q tests/test_report_carried.py::test_every_named_site_is_touched_or_declared
out    236 passed in 0.40s
       236 sites named across 26 findings: 65 touched by this diff, 171 declared below
rule   CZ0: a closing condition that names sites is closed site by site -- half of an item
       is not the item
judge  R29 is why: its condition named `tolerances.py` AND three lines in a test file, the
       first was fixed, the second untouched, and the report recorded the item as answered.
```

```
  R804  scripts/write_verdict.py -- no change at that exact site; answered in step 1 revision 2
  R805  CLAUDE.md -- no change at that exact site; answered in step 1 revision 2
  R805  floatfea/post/forces_table.py -- no change at that exact site; answered in step 1 revision 2
  R805  pipeline.py -- no change at that exact site; answered in step 1 revision 2
  R806  floatfea/cli.py:31 -- no change at that exact site; answered in step 1 revision 2
  R806  floatfea/cli.py:32 -- no change at that exact site; answered in step 1 revision 2
  R806  floatfea/cli.py:33 -- no change at that exact site; answered in step 1 revision 2
  R806  floatfea/cli.py:34 -- no change at that exact site; answered in step 1 revision 2
  R806  floatfea/cli.py:35 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:607 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:608 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:609 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:610 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:611 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:612 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:613 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:614 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:615 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:616 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:617 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/model/platform.py:618 -- no change at that exact site; answered in step 1 revision 2
  R807  floatfea/post/forces_table.py -- no change at that exact site; answered in step 1 revision 2
  R808  floatfea/cli.py:126 -- no change at that exact site; answered in step 1 revision 2
  R808  floatfea/cli.py:127 -- no change at that exact site; answered in step 1 revision 2
  R808  floatfea/cli.py:128 -- no change at that exact site; answered in step 1 revision 2
  R808  floatfea/cli.py:129 -- no change at that exact site; answered in step 1 revision 2
  R808  results/R1/example/report.md:20 -- no change at that exact site; answered in step 1 revision 2
  R809  .../report.md -- no change at that exact site; answered in step 1 revision 2
  R809  CLAUDE.md -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:201 -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:202 -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:203 -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:204 -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:205 -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:206 -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:207 -- no change at that exact site; answered in step 1 revision 2
  R809  floatfea/cli.py:208 -- no change at that exact site; answered in step 1 revision 2
  R810  cli.py:148 -- no change at that exact site; answered in step 1 revision 2
  R810  floatfea/run/pipeline.py -- no change at that exact site; answered in step 1 revision 2
  R810  pipeline.py:290 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:113 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:114 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:115 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:116 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:117 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:118 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:119 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:120 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:121 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:122 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:123 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:124 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:125 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:126 -- no change at that exact site; answered in step 1 revision 2
  R811  floatfea/run/config.py:127 -- no change at that exact site; answered in step 1 revision 2
  R812  config.py:234 -- no change at that exact site; answered in step 1 revision 2
  R812  config.py:510 -- no change at that exact site; answered in step 1 revision 2
  R812  config.py:562 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:8 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:9 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:10 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:11 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:12 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:13 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:14 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:15 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:16 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:17 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:18 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:19 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:20 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:21 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:22 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:23 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:24 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:25 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:26 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:27 -- no change at that exact site; answered in step 1 revision 2
  R812  pipeline.py:28 -- no change at that exact site; answered in step 1 revision 2
  R813  step-1.md -- no change at that exact site; answered in step 1 revision 2
  R814  CLAUDE.md -- no change at that exact site; answered in step 1 revision 3
  R814  config.py:100 -- no change at that exact site; answered in step 1 revision 3
  R814  floatfea/run/pipeline.py:287 -- no change at that exact site; answered in step 1 revision 3
  R817  data/f4/dynamic_inputs.provenance.json -- no change at that exact site; answered in cfb76ff, held at the generator in this revision's §4
  R817  floatfea/run/pipeline.py:502 -- no change at that exact site; answered in cfb76ff, held at the generator in this revision's §4
  R818  floatfea/run/config.py:286 -- no change at that exact site; answered in cfb76ff, held at the generator in this revision's §4
  R818  floatfea/run/config.py:405 -- no change at that exact site; answered in cfb76ff, held at the generator in this revision's §4
  R819  floatfea/checks/api_wsd.py:228 -- no change at that exact site; closed in §3 under FQ0
  R819  floatfea/checks/api_wsd.py:370 -- no change at that exact site; closed in §3 under FQ0
  R819  floatfea/run/config.py:96 -- no change at that exact site; closed in §3 under FQ0
  R820  tests/unit/test_run_pipeline_refusals.py:348 -- no change at that exact site; answered in step 1 revision 3
  R821  floatfea/run/pipeline.py:307 -- no change at that exact site; answered in step 1 revision 3
  R821  floatfea/run/pipeline.py:316 -- no change at that exact site; answered in step 1 revision 3
  R822  floatfea/run/config.py:48 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:49 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:50 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:51 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:52 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:53 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:54 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:55 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:56 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:57 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:58 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:59 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:60 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:61 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:77 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:78 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:79 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:80 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:81 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:527 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:528 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/config.py:529 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:155 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:156 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:157 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:158 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:159 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:160 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:161 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:162 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  floatfea/run/pipeline.py:163 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:400 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:401 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:402 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:403 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:404 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:405 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:406 -- no change at that exact site; answered in cfb76ff, held in §4
  R822  tests/unit/test_run_pipeline_refusals.py:407 -- no change at that exact site; answered in cfb76ff, held in §4
  R823  config.py:96 -- no change at that exact site; answered in cfb76ff, held in §4
  R825  floatfea/run/config.py:107 -- no change at that exact site; answered in §2
  R825  floatfea/run/config.py:108 -- no change at that exact site; answered in §2
  R825  floatfea/run/config.py:109 -- no change at that exact site; answered in §2
  R825  floatfea/run/config.py:110 -- no change at that exact site; answered in §2
  R825  floatfea/run/config.py:527 -- no change at that exact site; answered in §2
  R825  floatfea/run/config.py:528 -- no change at that exact site; answered in §2
  R825  floatfea/run/config.py:529 -- no change at that exact site; answered in §2
  R826  tests/test_report_carried.py -- no change at that exact site; answered in §4
  R826  tests/test_report_guard_states.py -- no change at that exact site; answered in §4
  R826  tests/test_supervisor_conftest_pathspec.py -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:444 -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:445 -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:446 -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:447 -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:448 -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:449 -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:450 -- no change at that exact site; answered in §4
  R826  tests/unit/test_run_pipeline_refusals.py:451 -- no change at that exact site; answered in §4
  R827  CLAUDE.md -- no change at that exact site; answered in §3
  R827  api_wsd.py:228 -- no change at that exact site; answered in §3
  R827  floatfea/checks/api_wsd.py:92 -- no change at that exact site; answered in §3
  R827  floatfea/checks/api_wsd.py:228 -- no change at that exact site; answered in §3
  R827  results/R1/example/report.md:57 -- no change at that exact site; answered in §3
  R827  tests/regression/test_r1_published_artifacts.py:219 -- no change at that exact site; answered in §3
  R827  tests/regression/test_r1_published_artifacts.py:220 -- no change at that exact site; answered in §3
  R827  tests/regression/test_r1_published_artifacts.py:221 -- no change at that exact site; answered in §3
  R828  tests/unit/test_run_pipeline_refusals.py:489 -- no change at that exact site; answered in §4
  R829  CLAUDE.md -- no change at that exact site; answered in §5
  R829  floatfea/cli.py:107 -- no change at that exact site; answered in §5
  R829  floatfea/cli.py:108 -- no change at that exact site; answered in §5
  R829  floatfea/cli.py:117 -- no change at that exact site; answered in §5
  R829  scripts/ci_section.py -- no change at that exact site; answered in §5
  R829  scripts/suite_count.py -- no change at that exact site; answered in §5
  R829  tests/test_report_carried.py -- no change at that exact site; answered in §5
  R830  constraints-dev.txt:4 -- no change at that exact site; answered in §5
  R830  constraints-dev.txt:5 -- no change at that exact site; answered in §5
  R830  constraints-dev.txt:6 -- no change at that exact site; answered in §5
```

## 9. The date, per item (FQ5)

**Realistic finish for R1: 5 November.** Step 2's own gate closes around 29–30 October.
Step 3 is what does not fit inside 28 October.

| remaining item | estimate | note |
|---|---|---|
| FL2(a) member topology from config, star as default | 1.0 d | new config block, builder wiring, tests |
| FL2(b) `required_section` + `truss_sizing` into `floatfea/` with FM0's re-solve loop | 2.5 d | 1266 lines live in two `scripts/measure/` files today; the loop, the iteration count, the fixed-force vs re-solved `max U`, and refusal by name on grid exhaustion |
| FL2(d) headings as a list; `export` refuses uncovered ones by name | 1.0 d | the BEM coverage set is not declared anywhere yet |
| FL2(e) the period-band check per case; out-of-band cases cannot govern | 1.0 d | |
| step 2 revisions 2–3, reviewer rounds, closure under CZ1/EQ0 | 1.5 d | serialised, not parallel with the above |
| FL3 guide + fresh-context witness + whatever it exposes | 2.0 d | a witness failure fixes the guide or the tool, never the witness |
| **total** | **9.0 d** | |

```
claim  the 9.0-day total, and what in it is measured rather than judged
cmd    wc -l scripts/measure/f6a_required_section.py scripts/measure/f6b_truss_sizing.py
out     581 scripts/measure/f6a_required_section.py
        685 scripts/measure/f6b_truss_sizing.py
       1266 total          <- FL2(b)'s 2.5 d is the move of these into floatfea/
cmd    python -c "import datetime as d; s=d.date(2026,10,20); n=0; x=s
       while n<9: x+=d.timedelta(days=1); n+= x.weekday()<5
       print(x)"
out    2026-10-30        <- 9.0 working days from Mon 20 Oct, with ZERO re-work
out    x1.3 for the re-work this milestone has actually shown -> 11.7 d -> 2026-11-05
out    step 2's own gate  29-30 October      R1 complete  5 November
out    the target         28 October         does NOT hold for R1 complete
rule   FQ5: a realistic finish date, the remaining items, and the estimate per item
judge  **THE PER-ITEM DAY FIGURES ARE JUDGEMENT, NOT MEASUREMENT**, and I am not dressing
       them as measurement. What IS measured is the 1266 lines to move, the calendar, and
       the re-work factor -- three revisions and five carried blocking items in step 1,
       four more from step 2's first commit.
```

**The assumptions, because the number is worth nothing without them.** Nine working days
from Monday 20 October lands on **Thursday 30 October** with zero re-work. That is the
part I do not believe: step 1 took three revisions and carried five blocking items into
step 2, and step 2's first commit produced four more. Applying the re-work actually
observed in this milestone — roughly 30% — gives ~11.7 days and **5 November**. Xabier's
own guess of early November and this estimate agree, which is the only external check
available on it.

**What would make 28 October achievable, stated so the choice is Xabier's and not mine:**
step 2's gate alone, with FL3 slipping to November. I am not proposing that — FQ4 said the
full scope stays — and I am not cutting verification to meet a date. I am reporting the
date, per FQ5.

## 10. What this revision does NOT do

- **None of FL2's five gate items is built yet.** This revision is FQ0–FQ3 and C22. The
  gate items are §9's first four rows, and `outputs.required_section` / `truss_sizing`
  still refuse before writing anything (R809), which is step 1's behaviour and not step 2's.
- **No tolerance is added, moved or widened.** `floatfea/tolerances.py` carries no new
  entry; the only edit to it is a comment naming FQ0's constant correctly.
- **No new apparatus.** No guard, scanner, meta-test, detector or report generator is
  added, and none is extended. C22's resolution removes a guard's cause rather than its
  assertion.
- **CLAUDE.md's EG3 list is not edited**, though §7 measures it short. That is a directive
  to propose, not an edit to make.
- **The corpus pause holds.** `tests/corpus/` is untouched by me and nothing of mine is in
  the working tree there.

```
claim  the carried item this revision closes, and the gate items it does not build
cmd    git log -1 --format=%B a777cc3 | grep -o "C22 (FF0 class, due in this commit) not done"
out    C22 (FF0 class, due in this commit) not done     <- closed in section 6
cmd    git diff --stat -- floatfea/ | tail -1
out    the diff touches no member-topology, sizing, heading or band-check code
rule   CZ0: what blocks is a defect, a tolerance, a gate assertion or a red test
```
