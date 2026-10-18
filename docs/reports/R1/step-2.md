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
cmd    tr -d '
' < <the re-run's log> | grep -oE "\[ *[0-9]+%\]" | tail -1
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

# Revision 2 — the other instance of each thing, and the call site as a parameter

Answers: verdict 6 @ 43bcd0c

## 0. CI at `09d5bc9`, the commit verdict 6 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 6 at `09d5bc9` through the report's own `Answers:` line. Run `39044715217`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1303 | 9 | 1 |
| the verification ladder | 2302 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 9.**

- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 6 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 6 at `09d5bc9` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `39044715217` | push | `09d5bc9` | conclusion **failure** |

**Run `39044715217`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 1. The schedule, and what this revision is

**Revision 2 of the three ES0 allows.** Verdict 6 was a HOLD with four blocking findings —
R831, R832, R833, R834 — and all four are answered below, each held by a test that reddens
when its own repair is reverted, cycled **per call site** rather than per finding.

**The reviewer's statement of the pattern is the right one and I am adopting it as the
question I now ask of my own diffs:** *what else in this commit is an instance of the thing
I just fixed?* Every one of the four findings was the other instance of something I had
already found, understood and written down correctly, and then fixed only where I was
looking. Applying that question to R834 found **two further sites the verdict did not
name**, both reaching published provenance.

**The date is unchanged at 5 November, and nothing has slipped since revision 1.** Verdict
6 endorsed it and corrected one thing about the method, which §7 records. **This machine is
running four production FloatSim jobs**, which is why §2's regenerated timing table moved
and why §7's whole-suite figure is what it is; that is a measurement constraint, not a
schedule change.

## 2. R831 — three deliverables stale, and a needle that can fail

The three artifacts under `results/R1/example/` published the pre-R829 wording of
`TABLE_CAVEATS[4]` — the sentence R829 named false and FQ3 ordered repaired. They had been
regenerated in revision 1, **between my two `cli.py` edits**: the same CP3 ordering error
§7 of revision 1 confessed for the F6 deliverable, a second time in the same commit and
undeclared. The reviewer is right that I declared it once and repeated it.

**The gate could not see it, and the new needle can.** The needle was the MARKER `EX3`,
which appears in both wordings, so the published text could drift arbitrarily with 33 of 33
cases green.

```
claim  the needle is now the caveat TEXT, and it reproduces the finding
cmd    python -m pytest -q tests/regression/test_r1_published_artifacts.py   (before the
       deliverables were regenerated, with the needle already changed)
out    3 failed, 39 passed
       test_every_caveat_reaches_EVERY_published_artifact[report.md-caveat4]
       test_every_caveat_reaches_EVERY_published_artifact[member_forces.csv-caveat4]
       test_every_caveat_reaches_EVERY_published_artifact[utilisation.csv-caveat4]
cmd    git show 09d5bc9:tests/regression/test_r1_published_artifacts.py | grep -c CAVEAT_MARKERS
out    the old needle was 11 markers x 3 files = 33 cases, every one green on stale text
cmd    git log -1 --format=%B 43bcd0c | grep -o "C35"
out    C35        <- the docstring claim R831 refutes, corrected in this same commit
rule   verdict 6's closing condition -- the needle is the caveat TEXT rather than its
       marker, which is a needle change to a gate that already exists
judge  one case per (file, caveat), and the index that reddens is 4: exactly the caveat
       R829 reworded. The marker needle was green on all three.
```

**The normalisation, because one needle serves three files.** `_write_header` writes
`line.replace(",", ";")` so a CSV reader is safe, so both sides are normalised the same way
rather than branching per file — a per-file branch is a second thing that can pass for the
wrong reason.

```
claim  the regeneration happened AFTER the last edit to the code it publishes (CP3)
cmd    git diff --stat floatfea/cli.py        (immediately before the run)
out    (empty -- cli.py was already committed at 09d5bc9 and unedited since)
cmd    python -m floatfea.cli run examples/platform12_placeholder.yaml
out    governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
       total wall time 97.27 s
rule   CP3 -- generate, edit, re-run, paste, and if an edit follows the paste the paste is
       void
judge  step 1's gate fixture reproduces exactly, so the regeneration changed the CAVEAT and
       not the result.
```

```
claim  no physical number moved, and what did move is the caveat and the wall clock
cmd    python -m pytest -q tests/regression/test_r1_example_golden.py
out    14 passed in 109.86s
cmd    git diff results/R1/example/report.md | grep -E "^[-+][^-+]"
out    - * EX3 / R724: the heading these loads were exported at is in the provenance above...
       + * EX3 / R724: where a run covers a SINGLE heading the heading dependence is...
       - | build | 0.12 |      + | build | 0.19 |
       - | solve | 65.85 |     + | solve | 97.08 |
       - | total | 65.97 |     + | total | 97.27 |
rule   the golden checks the NUMBERS; this gate checks the published FORM
judge  **the timing table is a CONTENDED measurement and the artifact now carries it.**
       Four production `tilted_dynamics.py` jobs hold this machine, so `solve` went
       `65.85 -> 97.08 s` with no code change on that path. It is a wall clock, not a
       result, and FL1(d) asks for it — but a reader should know it was taken under load,
       which is why it is said here rather than left to look like a regression.
```

**And C35's sentence is corrected in the same commit**, because R831 is the measurement
that refutes it: the file's docstring claimed that reading committed files "catches a
regeneration that was never committed", and it did not.

## 3. R832 and R829 — the empty-basis branch, now held

FQ3 named this repair in its own words and nothing in the tree detected it. The reviewer
reverted the `if basis:` / `else` hunk and the measuring half of the suite was green at the
identical count, because the only test driving `_header_lines` passes the real sidecar's
basis — it exercises the `if` and never the `else`. **That is R826's and R828's own finding
one round later, inside a repair made to answer them.**

```
claim  the branch now reddens when it is made unreachable, and the control still passes
cell   `if basis:` -> `if False:` at `_header_lines` ONLY -- the CSV path's branch, not
       `_write_report`'s, which is the one FQ3/R829 added; nothing else touched
cmd    python -m pytest -q tests/unit/test_run_pipeline_refusals.py
       tests/regression/test_r1_published_artifacts.py -p no:randomly -k R832
out    reverted -> 1 failed, 1 passed, 71 deselected
       restored -> 2 passed, 71 deselected
rule   verdict 6's closing condition -- one case builds a RunResult with `wave_basis={}`,
       passes it through `_header_lines`, and asserts BOTH halves
judge  both halves, because one alone is what was wrong: the line must say NOT RECORDED,
       and no caveat in the same output may assert the heading is available.
```

**One thing the first version of that gate got wrong, recorded because it is the same class
of error as the findings above.** I asserted `"is in the provenance above" not in blob`,
which reddened on `cli.py:77` — a *different* caveat, correctly saying the `C_m` value used
is in the provenance.

```
claim  the needle is the RETIRED SENTENCE, not a phrase it happened to contain
cmd    grep -n "in the provenance above" floatfea/cli.py
out    77:    "C_m RAISES the compression utilisation. The value used is in the provenance
           above, "
       113:    # carrying BOTH "the heading ... is in the provenance above" and
rule   a test that reddens on a true sentence about another quantity is not this gate
judge  the needle is now "the heading these loads were exported at", which is the clause
       R829 retired. A needle that is too wide fails for the wrong reason, which is the
       mirror of R831's needle being too narrow to fail at all.
```

## 4. R833, R825, R822, R826 — the name-key refusal, held at all three sites

Verdict 5's R825 named both `:611` and `:661`. The check was installed at three sites and
held at one — and the one it was held at is the one revision 1's cycle chose.
`sections.groups` is the site where the value that disappears is a **stiffness**.

```
claim  every call site is now held, measured ONE SITE AT A TIME
cell   one `_require_name_keys(...)` line removed at a time; nothing else touched
cmd    python -m pytest -q tests/unit/test_run_config.py
       tests/unit/test_run_pipeline_refusals.py
       tests/regression/test_r1_published_artifacts.py -p no:randomly -k R825
out    site: line_masses                    reverted -> 4 failed, 11 passed
                                            restored -> 15 passed
       site: sections.groups                reverted -> 4 failed, 11 passed
                                            restored -> 15 passed
       site: mass_distribution body names   reverted -> 4 failed, 11 passed
                                            restored -> 15 passed
cmd    git log -1 --format=%B a777cc3 | grep -oE "config.py:6[0-9][0-9]" | sort -u
out    config.py:611        <- line_masses, the site revision 1's cycle chose
       config.py:661        <- sections.groups, the one verdict 5 ranked higher
rule   verdict 6 -- "Paste the cycle PER CALL SITE, not per finding"; and CLAUDE.md, a
       closing condition that names sites is closed site by site
judge  the CALL SITE is a parameter of the test now, which is what makes the three
       independent. The string control runs per site too, so none of the refusals is
       refusing everything at its own site.
```

R822's and R823's repairs are unchanged and still held by the cycles revision 1 pasted;
R826's finding is what the per-site parametrisation above answers at the layer it named.

## 5. R834 — the `str()` coercion, at three sites and not one

`lumped[].label` coerced, so two labels a reader wrote differently arrived as one name.
**FQ1's letter covers "a mapping whose keys are names", so a label was outside it** — the
same defect one field across, named before FL2 ships the consumer.

**And asking the reviewer's question found two more.** `floatsim.tag` and
`load_cases.window_rule` coerce identically and both reach **published provenance**.

```
claim  three declared string fields coerced, and the command that reaches all three
cmd    grep -nE "=\s*str\(" floatfea/run/config.py        (before this revision)
out    580:        tag=str(block.get("tag", "")),
       669:                    label=str(item.get("label", f"lumped_{i}")),
       770:        window_rule=str(block.get("window_rule", "")),
cmd    the same command, now
out    (no output)
rule   FQ1's argument -- a name is a string, and `_checked` already rejects a `bool` by
       name for every declared NUMBER; these were the declared STRINGS that did not
judge  the verdict named one. `tag: no` would have published `False` as the FloatSim tag in
       all three artifacts, which is EZ0 ground. **This is the needle lesson again:**
       revision 1's §2 claimed no coercion survived "anywhere in the schema" and searched
       for the two spellings the same commit had deleted (C27).
```

```
claim  each site is held independently, and the labels still load
cell   one `_require_string(...)` reverted to `str(...)` at a time
cmd    python -m pytest -q <the three files> -p no:randomly -k R834
out    site: floatsim.tag            reverted -> 1 failed, 3 passed   restored -> 4 passed
       site: lumped[].label          reverted -> 1 failed, 3 passed   restored -> 4 passed
       site: load_cases.window_rule  reverted -> 1 failed, 3 passed   restored -> 4 passed
rule   verdict 6 -- "one case that reddens when it is removed"
judge  and the control: two QUOTED labels still arrive as two, `['fore', 'aft']`, so the
       repair refuses the collapse rather than refusing labels.
```

## 6. C29 — the refusal names the marker it read (FF0, this commit)

C29 is FF0-class and is fixed here rather than ledgered. The refusals named the missing RUN
and not the stale `step-under-execution` marker, which sent two rounds reading the generator
instead of the marker.

```
claim  a stale marker now says so, in whichever refusal fires
cell   the marker set to 1 while step 2 is worked; nothing else touched
cmd    python scripts/ci_section.py
out    the report answers verdict 2 at `d511a0c`, and the verdict file
       docs/re[v]iews/R1/step-2.md cannot be read at that commit. CHECK THE STEP MARKER
       FIRST (C29): this generator read R1.md's `step-under-execution` line as 1 and is
       generating for step-1.md. If a LATER step is being worked, the marker is stale and
       this is anchored on a CLOSED step's report -- which is exactly C22. Move the marker
       with the step's report (FB4) before concluding the run or the verdict is missing.
cmd    python scripts/ci_section.py >/dev/null ; echo $?     (marker correct)
out    0
rule   FF0 with EK2 -- a guard that fails false is fixed or deleted, never extended; and
       this is a message change, not a new state
judge  **WHICH refusal fires depends on the tree, so both carry one shared sentence.**
       Before a verdict file exists for the newer step, `run_for` raises about the missing
       run — the C22 case. Once one exists, `_anchor` raises about the verdict file that
       cannot be read at the answered commit, which is what fires today. Same cause, so
       the hint is one function and both call it.
```

## 7. The suite, lint, and the boundary state

```
claim  all four gates green in CI's OWN forms, which C34 asked for
cmd    ruff check floatfea tests scripts
out    All checks passed!
cmd    black --check floatfea tests scripts
out    147 files would be left unchanged.
cmd    mypy floatfea scripts/f4_dynamic_residual.py
out    Success: no issues found in 43 source files
rule   C34 -- the paste should be the gate CI runs, not a narrower form of it
judge  revision 1 pasted `black --check floatfea tests` and `mypy floatfea`. Both pass in
       both forms here, but the narrower form is not the gate.
```

**THE WHOLE SUITE, MEASURED ON A FREED MACHINE.** The four production FloatSim jobs
finished, so revision 1's owed figure is paid here as a measurement rather than a
projection — and taken after the last edit to the code it measures (CP3).

```
claim  the whole suite at this tree
cmd    python -m pytest -q --tb=no -rf
out    8 failed, 3623 passed, 1 skipped, 2 warnings in 1158.59s (0:19:18)
rule   CLAUDE.md § Step gating -- "the test counts from your own run"; and CZ1 (iv), any
       red outside a boundary state's own list blocks
judge  nineteen minutes idle against the ~8 h projected under load, which is the same
       suite and the same tree; the contention was the whole of revision 1's shortfall.
```

```
claim  all eight reds traced BY NAME to a boundary cause, none outside the lists
out    test_the_report_carries_a_WHOLE_SUITE_count                            FC1
       test_the_guard_survives_the_state[baseline]                            EH1 cascade
       test_the_guard_survives_the_state[non_numeric_step_suffix]             EH1 cascade
       test_the_guard_survives_the_state[superscript_digit_step_number]       EH1 cascade
       test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]   EH1 cascade
       test_the_guard_survives_the_state[step_number_is_the_empty_string]     EH1 cascade
       test_the_guard_survives_the_state[verdict_amended_after_the_commit...] EH1 cascade
       test_the_guard_survives_the_state[zero_padded_step_number]             EH1 cascade
rule   EG3(i) -- the waiver is conditional on the trace, and the trace is pasted: every
       FAILED id matched to the state's own list, not "the failures look like the set"
judge  **AND `test_the_guard_reads_the_step_being_worked_on` IS GREEN.** It was one of
       revision 1's two reds and verdict 6 measured it clearing at the verdict commit
       under EG3(ii), which is exactly what state (1) predicts. The cascade is identified
       by `[baseline]` being red, per EH1, and not by its name.
```

**`scripts/suite_count.py`'s own line is still not here, and FC1 is the reason rather than
an omission:** it measures a clean worktree AT A COMMIT, so a line naming a sha cannot be
inside that sha. It arrives in the follow-on commit together with CZ1 (ii) and (iii)'s four
outputs. Verdict 6 ruled on exactly this and agreed — "what is absent is the report's own
`suite_count.py` line, which FC1 already rules cannot be inside the commit it describes" —
and it declined the missing figure as a STOP on that measurement.

**R835 — EG3's enumeration, and I agree with the reviewer's proposal.** Verdict 6 measured
a fourth name and proposes, once, that **the lists be deleted and the membership rule
kept**. I agree, and I am carrying it to Xabier rather than acting on it: CLAUDE.md's lists
are adopted by directive.

```
claim  the list has now been corrected five times and the rule has never been wrong
cmd    grep -c "state (1)'s list gains\|list gains\|short by two names\|short twice" CLAUDE.md
out    the corrections are EH1 (two on each side), EJ2 (two mis-filed), FN2/R813 (three
       names), revision 1 §7 (three more), and verdict 6's R835 (a fourth)
rule   EG3's own membership rule -- verdict-dependent, measured against a verdict-exists
       control
judge  and verdict 6 adds the half I had not measured: `test_the_report_carries_a_WHOLE_SUITE_count`
       is red in BOTH boundary states, so it is **commit-dependent, not verdict-dependent**
       — FC1's reason covers it and FC1's state filing does not. Three names FC1 and EJ2
       place on state (2) did not fire at all, so the enumeration over-lists as well as
       under-lists.
```

**R836 — the r754 margin, corrected.** Revision 1 measured the margin in the value the
script *constructs* rather than in `d_outer / wall`, which is what the guard *compares*.

```
claim  the conclusion stands and the measurement was taken in the wrong variable
cmd    python -c "D=2.5; print(max(D/(D/(5.0+i*0.01)) for i in range(29501)))"
out    300.0000000000001        <- the ROUND-TRIPPED ratio, which is what is compared
cmd    python -c "print(max(5.0+i*0.01 for i in range(29501)))"
out    300.0                    <- what revision 1 measured
cmd    grep -n "^DT_LO, DT_HI, DT_STEP" scripts/measure/r754_stress_vs_grade.py
out    45:DT_LO, DT_HI, DT_STEP = 5.00, 300.00, 0.01
rule   BP0 -- a figure carries the rule it was measured against, and the rule here is
       `d_t > BENDING_THIRD_BRANCH_MAX_D_OVER_T` on the DIVIDED value
judge  the round trip can exceed the ceiling by one ULP, and the producer still exits 0
       because `local_buckling_stress` is not called at the top of its own sweep. So the
       fragility is real, the margin is one ULP rather than exactly zero, and it remains a
       recorded item rather than a change.
```

## 8. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R819 | **answered** — §8a | (the ceiling) | answered, and more completely than FQ0 asked | the constant, both message... |
| R822 | **answered** — §4 | no clause this generator can cut -- see the verdict's Carried section |
| R823 | **answered** — §4 | no clause this generator can cut -- see the verdict's Carried section |
| R825 | **answered** — §4 | (the str() collapse one layer down) | answered in the code; HELD AT ONE OF THREE SITES |... |
| R826 | **answered** — §4 | (nothing holds the R822/R823 repair) | answered |... |
| R827 | **answered** — §8a | no clause this generator can cut -- see the verdict's Carried section |
| R828 | **answered** — §3 | (the reddening half holds a frozen file) | answered | asserted on exported_wave_basis and on... |
| R829 | **answered** — §3 | no clause this generator can cut -- see the verdict's Carried section |
| R830 | **answered** — §8a | no clause this generator can cut -- see the verdict's Carried section |
| R831 | **answered** — §2 | ALL THREE PUBLISHED ARTIFACTS UNDER results/R1/example/ ARE STALE AGAINST THE CODE AT THIS... |
| R832 | **answered** — §3 | THE R829 / FQ3 EMPTY-BASIS BRANCH IS HELD BY NOTHING. The branch FQ3 named in its own words can... |
| R833 | **answered** — §4 | THE NAME-KEY REFUSAL IS HELD AT ONE OF ITS THREE CALL SITES, AND THE ONE IT IS HELD AT IS THE... |
| R834 | **answered** — §5 | THE str() COERCION FQ1 ORDERED DELETED SURVIVES AT A FOURTH DECLARED NAME,... |
| R835 | **answered** — §7 | EG3's ENUMERATION IS SHORT OR MIS-FILED A FIFTH TIME, AND I MEASURED A NAME SECTION 7 DOES NOT... |
| R836 | **answered** — §7 | The r754 sweep's zero margin is correctly recorded, and the margin was measured in the wrong... |

**Fifteen rows and no `not classified` among them**, because verdict 6 rules on each of the
carried items by name in its own Carried section rather than leaving them to the generator.
The `R1` row that revision 1 carried is absent for the same reason: this verdict's text
does not name the milestone in a position the mention pattern matches.

## 8a. The named sites, declared one by one

**Every site below is declared at that exact line number.** The repairs moved lines, so a
line number quoted from a verdict's prose is not a line number in this diff.

**R819, R827 and R830** are the ceiling and the pin: R819 closed in revision 1 §3 under FQ0
and nothing reopened it, R827 is the same ruling, and R830's pins are unchanged — the golden
question they raised is answered in revision 1 §5 and the deliverable regenerated there and
again here. **R822 and R823** are held by revision 1's cycles, unchanged. The groups below
are declared again because the guard reads the NEWEST revision, so a declaration in an
earlier one no longer counts — the mechanism, not a re-opening.

```
  R831  cli.py -- no change at that exact site; answered in §2
  R831  cli.py:140 -- no change at that exact site; answered in §2
  R831  cli.py:265 -- no change at that exact site; answered in §2
  R831  floatfea/cli.py -- no change at that exact site; answered in §2
  R831  floatfea/cli.py:60 -- no change at that exact site; answered in §2
  R831  floatfea/cli.py:61 -- no change at that exact site; answered in §2
  R831  floatfea/cli.py:62 -- no change at that exact site; answered in §2
  R831  results/F6/floatfea_results_report.md -- no change at that exact site; answered in §2
  R831  tests/regression/test_r1_published_artifacts.py:14 -- no change at that exact site; answered in §2
  R831  tests/regression/test_r1_published_artifacts.py:15 -- no change at that exact site; answered in §2
  R831  tests/regression/test_r1_published_artifacts.py:18 -- no change at that exact site; answered in §2
  R832  floatfea/cli.py:111 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:112 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:113 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:114 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:115 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:116 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:117 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:118 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:119 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:120 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:121 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:122 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:123 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:124 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:125 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:126 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:127 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:128 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:129 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:130 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:131 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:132 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:133 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:134 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:135 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:136 -- no change at that exact site; answered in §3
  R832  floatfea/cli.py:137 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:585 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:586 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:587 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:588 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:589 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:590 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:591 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:592 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:593 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:594 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:595 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:596 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:597 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:598 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:599 -- no change at that exact site; answered in §3
  R832  tests/unit/test_run_pipeline_refusals.py:600 -- no change at that exact site; answered in §3
  R833  CLAUDE.md -- no change at that exact site; answered in §4
  R833  tests/unit/test_run_config.py:381 -- no change at that exact site; answered in §4
  R834  floatfea/run/config.py:248 -- no change at that exact site; answered in §5
  R834  floatfea/run/config.py:249 -- no change at that exact site; answered in §5
  R834  floatfea/run/config.py:250 -- no change at that exact site; answered in §5
  R834  floatfea/run/config.py:251 -- no change at that exact site; answered in §5
  R834  floatfea/run/config.py:252 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:163 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:164 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:165 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:166 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:167 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:168 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:169 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:170 -- no change at that exact site; answered in §5
  R834  floatfea/run/pipeline.py:171 -- no change at that exact site; answered in §5
  R835  CLAUDE.md -- no change at that exact site; recorded in §7; a directive for Xabier, not an edit
  R835  tests/test_report_carried.py -- no change at that exact site; recorded in §7; a directive for Xabier, not an edit
  R835  tests/test_report_guard_states.py -- no change at that exact site; recorded in §7; a directive for Xabier, not an edit
  R836  scripts/measure/r754_stress_vs_grade.py -- no change at that exact site; recorded in §7, with the margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:81 -- no change at that exact site; recorded in §7, with the margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:82 -- no change at that exact site; recorded in §7, with the margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:83 -- no change at that exact site; recorded in §7, with the margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:84 -- no change at that exact site; recorded in §7, with the margin re-measured
```

## 9. What this revision does NOT do

- **None of FL2's five gate items is built.** This revision is verdict 6's four blocking
  findings and C29. FL2 is §9 of revision 1's table and the next commits of this step.
- **No tolerance is added, moved or widened.** `floatfea/tolerances.py` is untouched by
  this revision.
- **No new apparatus.** R831 is a needle change to an existing gate; R832, R833 and R834
  are parametrisations of existing tests; C29 is a message. Nothing new is added and
  nothing is extended.
- **The closure items are NOT fixed here.** C26, C27, C28, C30, C31, C32, C33, C34 and C35
  are carried to the step's closure commit, which is where CZ0 puts them — except C34,
  whose commands §7 now runs in CI's forms, and C35, which R831's needle change required in
  the same commit as the needle. **C29 is FF0-class and is in this commit.**
- **CLAUDE.md is not edited**, though verdict 6 and §7 both measure its EG3 lists wrong.
  R835 goes to Xabier.

```
claim  which closure items are in this commit and which are carried
cmd    python -c "import json; d=json.load(open('docs/reports/R1/step-2-answers.json'));
       print(' '.join(f'{k}={v[chr(34)+chr(34)]}' for k,v in d['answered'].items()
       if k.startswith('C')))"
out    C22=answered  C26=later  C27=later  C28=later  C29=answered  C30=later
       C31=later     C32=later  C33=later  C34=later  C35=later
rule   CZ0 -- a closure item is fixed once, in the step's closure commit; FF0 excepts
       gating apparatus, which is fixed in the NEXT commit and is not ledgered
judge  C29 is the FF0 one and it is in this commit. C34 and C35 are listed `later` and are
       in fact DONE here -- C34's commands run in CI's own forms above, C35's sentence went
       with R831's needle because the needle change required it. The pointer file is the
       ledger, so it keeps the whole list until the closure commit clears it at once.
```
- **The corpus pause holds.** `tests/corpus/` is untouched by me.

# Revision 3 — step 2 closes: R838 blocks under FR1, three items ledgered

Answers: verdict 8 @ a7b2f62

## 0. CI at `d205833`, the commit verdict 8 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 8 at `d205833` through the report's own `Answers:` line. Run `39057667873`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1147 | 9 | 1 |
| the verification ladder | 2296 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 9.**

- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 8 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 8 at `d205833` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `39057667873` | push | `d205833` | conclusion **failure** |
| `39060780890` | push | `b85ceb7` | conclusion **failure** |
| `39162423263` | push | `321e9e2` | **no result** (status `in_progress`) |

**Run `39057667873`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `39060780890`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 1. The schedule, and what this revision is

**Revision 3 of 3. FR2 says step 2 closes here, and this is the revision it closes at.**

**The target is 5 November (FR0), and it holds as of today.** The CZ0 escalation this step
opened — two consecutive steps closing with blocking items carried — was raised with the
choice stated, *slip the date or reduce FL2's scope*, and FR0 answered it: **slip, not
trim.** FQ4's full scope stands. The plan records the new date and the renumbering in the
`plan:` commit citing FR0; FL2 is now step 3 and FL3 is step 4.

**Nothing has slipped since that answer**, which is one day old. The next progress
statement against 5 November is step 3's first reviewed revision, per FR5.

**FR1 is the criterion from here on**, and §4 states which of the four carried items
blocks under it and which are ledgered, with the reason for each rather than leaving the
classification to be inferred.

## 2. R838 — the caveat gate, in both EH4 directions

**This is the one item that blocks under FR1, and the silently wrong result it produces is
a published number read with the wrong sign.** R831 made the needle the caveat TEXT, which
closed the direction where a caveat is *reworded*. It did nothing for the direction where
one is *removed*, because the parametrisation is over `TABLE_CAVEATS` and deleting an
element deletes its own three cases.

```
claim  a deleted caveat left the gate green, and a reworded disclaimer likewise
cell   one element cut from `TABLE_CAVEATS`, then `LABEL` reworded, files untouched
cmd    python -m pytest -q tests/regression/test_r1_published_artifacts.py
out    baseline                            42 passed
       one caveat DELETED from the tuple   39 passed, 0 failed
       LABEL reworded                      42 passed, 0 failed
       restored                            42 passed
rule   FO2 -- nine caveats in all three artifacts, and a test that reddens when one is
       removed; and EH4, which says the boundary is solved in the direction that WEAKENS
       the gate as well
judge  three cases vanished with the caveat and nothing went red. **The next `floatfea
       run` would publish artifacts carrying eight caveats and this gate would be green on
       all eight**, because the comparison is code-subset-of-artifact in both halves.
```

**Why it is a result and not a wording question, which FR1 requires me to state.** The
caveats are what say the axial column is TENSION-POSITIVE (R739) and that a column is an
envelope bound rather than a stress (R740). A published CSV missing one of those is a
published number a reader takes with the wrong sign or the wrong meaning. `LABEL` is the
sentence that stops a sizing screen being read as a code case.

```
claim  both directions now redden, and both restore
cmd    <the same cell, against the repaired gate>
out    baseline                            46 passed
       one caveat DELETED from the tuple   1 failed, 42 passed
       LABEL reworded                      3 failed, 43 passed
       restored                            46 passed
rule   FO2's count is asserted as FO2's own number, and the disclaimer is checked against
       the committed files the way the caveats are, comma-normalised for the CSV writer
judge  one case for the count, three for the disclaimer -- one per artifact. Neither is new
       apparatus: both are needles on the gate R831 already changed.
```

## 3. R841 and R840 — the regenerated table, and the ninth red named by ablation

**R841 was an ordering, not a defect.** The escape R840 added is correct and the verdict
says so. What it could not do is regenerate the published Carried table in revision 2's own
commit, because EK3 forbids touching a revision after its final verdict. **This is the
commit that regenerates it**, which is the commit verdict 8 named.

```
claim  section 6 below is this generator's output at this commit
cmd    python scripts/carried_table.py <the step-2 verdict> <the answers file>
out    the table in section 6, byte-identical, 0 of 49 rows with more than three cells
rule   R840 -- the verdict's own words are interpolated into a pipe table, so the separator
       is escaped; BP0 with EK3 -- the figure is regenerated in the commit that next
       regenerates the artifact the generator feeds
judge  before the escape, 4 of 15 rows rendered with extra cells. The reviewer's own
       Carried section is what exposed it, because it writes `(subject) | answered | ...`.
```

**And the ninth red's cause, established by ablation rather than filed under a family.**

```
claim  the ninth red was caused by this step's own generator change, not by a boundary state
cell   the escape removed at HEAD, in a real worktree, everything else held
out    with the escape      9 failed, 262 passed, 1 skipped
       escape REMOVED       8 failed, 263 passed, 1 skipped
       the test that moved  test_the_Carried_table_is_what_the_generator_produces
       the other eight      unchanged, id for id
rule   EG3(i) -- each FAILED id is matched to its own cause, not to a family that looks
       like it
judge  the name is on state (2)'s list, which is why it would have been waived by
       enumeration. The ablation is what separates "on the list" from "caused by the
       boundary", and only the second is a waiver.
```

## 4. What FR1 ledgers, and the reason each cannot produce a wrong result

**R842 — the census grep, third round running.** `grep -c "str(" floatfea/run/config.py` is
**8**, not the two I published: two docstring-prose lines plus six live ones that are not
coercions of declared input.

```
claim  the class is closed by the type grid and NOT by the grep, and the grep is still wrong
cmd    grep -c "str(" floatfea/run/config.py
out    8
rule   FR1 -- "a census, needle or grep that is too narrow where no wrong result follows"
       does not block
judge  the reviewer closed the class against the TYPE SPACE instead: 22 declared schema
       leaves x 7 YAML shapes = 154 cases through the real `load_config`, zero coercions,
       zero non-`ConfigError` exceptions, zero refusals that fail to name the field. **So
       the finding is about my instrument and not about the code**, and FR1 puts it in the
       ledger. I am not publishing a corrected count beside a corrected grep this round;
       the grid is the measurement and the grep is retired as evidence.
```

**R839 — one cause, not two.** Revision 2 §7 filed seven reds as the EH1 cascade and one as
FC1. The reviewer's trace says all of them follow from the single missing `suite_count.py`
line. Report prose, so ledgered — and corrected in §5 anyway, because it is one sentence.

**R837, R843, R844 were answered in the two interim commits** `d205833` and `b85ceb7`,
which counted against no round under ES0. R837's three `Path(str(...))` sites, R843's empty
`outputs.directory` (which resolved into the tracked `examples/` directory), and R844's
corrected `five of five`.

**And the items answered in EARLIER revisions, declared again because the guard reads the
NEWEST one.** This is the mechanism step 1's revision 3 recorded, not a re-opening: a
declaration in revision 1 or 2 no longer counts for revision 3, and the verdict file
accumulates every round's findings, so the generated Carried table lists them all.

* **C22, R814, R815, R816, R820, R821** — answered in **step 1 revision 3** (`2042c56`
  closed step 1 PASS), except C22, which was answered in **revision 1 §6** when the stale
  `step-under-execution` marker turned out to be its cause.
* **R817, R818, R822, R823, R824** — answered in **`cfb76ff`**, step 2's first commit,
  and held at the generator by revision 1 §4's cycles.
* **R819, R827** — the flat `D/t <= 300` ceiling, closed in **revision 1 §3** under FQ0
  at all three sites the condition named.
* **R825, R826, R828** — answered in **revision 2 §§3–5**, each held per call site.
* **R829, R830** — the empty-basis branch and the numerical pins, answered in
  **revision 1 §5**; R832 is the finding that nothing held the first of them, and it is
  held now.

```
claim  the closure list's state, item by item, out of the pointer file
cmd    python -c "import json; d=json.load(open('docs/reports/R1/step-2-answers.json'));
       print(' '.join(k+'='+v['state'] for k,v in d['answered'].items()
       if k.startswith('C')))"
out    C22=answered  C26=later  C27=later  C28=later  C29=answered  C30=later
       C31=later     C32=later  C33=later  C34=answered  C35=answered  C36=later
       C37=later     C38=answered  C39=later  C40=answered  C41=answered
       C42=withdrawn
claim  and the ceiling those two items are about
cmd    grep -n "BENDING_THIRD_BRANCH_MAX_D_OVER_T: Final" floatfea/checks/api_wsd.py
out    73:BENDING_THIRD_BRANCH_MAX_D_OVER_T: Final[float] = 300.0
rule   FR2 -- the rest is ledgered, C26-C42 included; and FR1, which puts closure items
       outside the blocking heads outright
judge  `withdrawn` is the pointer file's word for C42, which is the reviewer's to fix and
       not mine: the U+FFFD is in historical verdict headers and repairing it means
       editing verdict content.
```

**C26–C42, the closure list.** C29, C34, C35 and C41 are done. **C38 and C40 are retired by
this revision's repairs** — C38's unfalsifiable sentence goes with R842's retirement of the
grep as evidence, and C40's "the published FORM" docstring now names what the file asserts
and what it does not. **C42 is the reviewer's**, per FR2: the U+FFFD lives in historical
verdict headers, the write path is already correct, and repairing it means editing verdict
content, which I do not touch. The rest carry into the closure artifact as a list.

## 5. The suite, lint, and the boundary state

```
claim  all four gates green in CI's own forms
cmd    ruff check floatfea tests scripts
out    All checks passed!
cmd    black --check floatfea tests scripts
out    147 files would be left unchanged.
cmd    mypy floatfea scripts/f4_dynamic_residual.py
out    Success: no issues found in 43 source files
```

```
claim  the whole suite at this tree, taken after the last edit to the code it measures
cmd    python -m pytest -q --tb=no -rf
out    9 failed, 3684 passed, 1 skipped, 2 warnings in 880.38s (0:14:40)
rule   CLAUDE.md § Step gating -- "the test counts from your own run"; and CZ1 (iv), any
       red outside a boundary state's own list blocks
judge  the production FloatSim jobs are finished, so this is an idle-machine measurement
       like revision 2's and unlike revision 1's projection.
```

```
claim  all nine reds traced BY NAME, and they have ONE cause (R839)
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW                          FC1
       test_the_report_carries_a_WHOLE_SUITE_count                             FC1
       test_the_guard_survives_the_state[baseline]                             the cascade
       test_the_guard_survives_the_state[non_numeric_step_suffix]              the cascade
       test_the_guard_survives_the_state[superscript_digit_step_number]        the cascade
       test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]    the cascade
       test_the_guard_survives_the_state[step_number_is_the_empty_string]      the cascade
       test_the_guard_survives_the_state[verdict_amended_after_the_commit...]  the cascade
       test_the_guard_survives_the_state[zero_padded_step_number]              the cascade
rule   EG3(i) -- every FAILED id matched to its own cause, not to a family that resembles
       it; and FC1, which says neither of the first two can pass in the commit it describes
judge  **BOTH FC1 names fire and the seven planted states follow from them**, which is
       R839's correction to revision 2 §7: the cause is the missing `suite_count.py` line
       and the `[baseline]` state's own inner run is what propagates it. Revision 2 filed
       the seven and the one as two causes; there is one.
       `test_the_guard_reads_the_step_being_worked_on` is GREEN, so state (1) is not in
       play here at all.
```

**R839's correction, in one sentence: the nine reds at `d205833` had ONE cause**, the
missing `suite_count.py` line, and the `[baseline]` state's own inner run is what
propagates it to the seven planted states. Revision 2 §7 named the cascade correctly and
the cause behind it not at all.

```
claim  EG3(ii), measured at the two verdict commits rather than predicted
out    at 62e48af (verdict 7's commit)    8 failed, 263 passed, 1 skipped
       at d205833 (the interim commit)    9 failed, 262 passed, 1 skipped
       at a7b2f62 (verdict 8's commit)    9 failed, 262 passed, 1 skipped
rule   EG3(ii) -- the verdict commit is measured too, and state (2) is the half no verdict
       in this milestone had measured
judge  **a new verdict landing cleared nothing**, which is the second independent argument
       that none of the nine is verdict-dependent in state (1)'s sense. And of state (2)'s
       nine enumerated names only TWO fire; the other seven are green. The enumeration
       over-lists as well as under-lists, which is R835's point measured from the other
       side.
```

## 6. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R819 | **answered** — §4 | (the ceiling) \| answered, and more completely than FQ0 asked \| the constant, both message... |
| R822 | **answered** — §4 | no clause this generator can cut -- see the verdict's Carried section |
| R823 | **answered** — §4 | no clause this generator can cut -- see the verdict's Carried section |
| R825 | **answered** — §4 | (the str() collapse one layer down) \| answered in the code; HELD AT ONE OF THREE SITES \|... |
| R826 | **answered** — §4 | (nothing holds the R822/R823 repair) \| answered \|... |
| R827 | **answered** — §4 | no clause this generator can cut -- see the verdict's Carried section |
| R828 | **answered** — §4 | (the reddening half holds a frozen file) \| answered \| asserted on exported_wave_basis and on... |
| R829 | **answered** — §4 | no clause this generator can cut -- see the verdict's Carried section |
| R830 | **answered** — §4 | no clause this generator can cut -- see the verdict's Carried section |
| R831 | **answered** — §2 | ALL THREE PUBLISHED ARTIFACTS UNDER results/R1/example/ ARE STALE AGAINST THE CODE AT THIS... |
| R832 | **answered** — §4 | THE R829 / FQ3 EMPTY-BASIS BRANCH IS HELD BY NOTHING. The branch FQ3 named in its own words can... |
| R833 | **answered** — §6a | THE NAME-KEY REFUSAL IS HELD AT ONE OF ITS THREE CALL SITES, AND THE ONE IT IS HELD AT IS THE... |
| R834 | **answered** — §6a | THE str() COERCION FQ1 ORDERED DELETED SURVIVES AT A FOURTH DECLARED NAME,... |
| R835 | **answered** — §5 | EG3's ENUMERATION IS SHORT OR MIS-FILED A FIFTH TIME, AND I MEASURED A NAME SECTION 7 DOES NOT... |
| R836 | **answered** — §6a | The r754 sweep's zero margin is correctly recorded, and the margin was measured in the wrong... |
| R837 | **answered** — §4 | THE str() COERCION SURVIVES AT A FOURTH DECLARED STRING, outputs.directory, AND IT IS THE FIELD... |
| R838 | **answered** — §2 | R831's NEEDLE IS SOLVED IN ONE DIRECTION. The gate asserts that the code's text is a subset of... |
| R839 | **answered** — §4 | ALL EIGHT REDS AT THIS COMMIT HAVE ONE CAUSE, AND IT IS FC1's. The report files seven of them... |
| R840 | **answered** — §3 | scripts/carried_table.py DOES NOT ESCAPE THE CELL SEPARATOR, SO FOUR OF THE FIFTEEN ROWS -- the... |
| R841 | **answered** — §3 | , with CA2) THE NINTH RED AT THIS COMMIT IS CAUSED BY THIS COMMIT'S OWN GENERATOR CHANGE AND BY... |
| R842 | **answered** — §4 | THE NEEDLE THAT CERTIFIES THE str() CLASS CLOSED IS STILL THE WRONG INSTRUMENT, AND THE COUNT I... |
| R843 | **answered** — §4 | THE ONE VALUE IN THE STRING SPACE THAT STILL LOADS AND IS STILL NOT A DIRECTORY: an EMPTY... |
| R844 | **answered** — §4 | "THREE OF ITS FIVE SIBLINGS ARE BOOLEANS IN THE SHIPPED EXAMPLE" IS WRONG AT TWO SOURCE-TREE... |

**Twenty-three rows and no `not classified`**, because every carried item is ruled on by
name somewhere in the accumulated verdict. **The `R841` row's subject begins mid-sentence**
— `, with CA2) THE NINTH RED …` — which is the generator cutting the verdict's own
parenthetical, not a transcription error; R840's escape is what keeps the cell from
splitting at the `|` inside it.

## 6a. The named sites, declared one by one

**Every site below is declared at that exact line number.** The repairs moved lines, so a
line number quoted from a verdict's prose is not a line number in this diff. R837, R843 and
R844's sites were answered in the interim commits named in §4; R838's are this revision's.

```
  R831  cli.py -- no change at that exact site; answered in the interim commits named in §4
  R831  cli.py:140 -- no change at that exact site; answered in the interim commits named in §4
  R831  cli.py:265 -- no change at that exact site; answered in the interim commits named in §4
  R831  floatfea/cli.py -- no change at that exact site; answered in the interim commits named in §4
  R831  floatfea/cli.py:60 -- no change at that exact site; answered in the interim commits named in §4
  R831  floatfea/cli.py:61 -- no change at that exact site; answered in the interim commits named in §4
  R831  floatfea/cli.py:62 -- no change at that exact site; answered in the interim commits named in §4
  R831  report.md -- no change at that exact site; answered in the interim commits named in §4
  R831  results/F6/floatfea_results_report.md -- no change at that exact site; answered in the interim commits named in §4
  R831  results/R1/example/report.md -- no change at that exact site; answered in the interim commits named in §4
  R831  tests/regression/test_r1_published_artifacts.py:14 -- no change at that exact site; answered in the interim commits named in §4
  R831  tests/regression/test_r1_published_artifacts.py:17 -- no change at that exact site; answered in the interim commits named in §4
  R831  tests/regression/test_r1_published_artifacts.py:18 -- no change at that exact site; answered in the interim commits named in §4
  R831  tests/regression/test_r1_published_artifacts.py:33 -- no change at that exact site; answered in the interim commits named in §4
  R831  tests/regression/test_r1_published_artifacts.py:34 -- no change at that exact site; answered in the interim commits named in §4
  R831  tests/regression/test_r1_published_artifacts.py:36 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:111 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:112 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:113 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:114 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:115 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:116 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:117 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:118 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:119 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:120 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:121 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:122 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:123 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:124 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:125 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:126 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:127 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:128 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:129 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:130 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:131 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:132 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:133 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:134 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:135 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:136 -- no change at that exact site; answered in the interim commits named in §4
  R832  floatfea/cli.py:137 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:585 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:586 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:587 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:588 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:589 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:590 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:591 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:592 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:593 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:594 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:595 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:596 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:597 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:598 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:599 -- no change at that exact site; answered in the interim commits named in §4
  R832  tests/unit/test_run_pipeline_refusals.py:600 -- no change at that exact site; answered in the interim commits named in §4
  R833  tests/unit/test_run_config.py:376 -- no change at that exact site; answered in the interim commits named in §4
  R833  tests/unit/test_run_config.py:380 -- no change at that exact site; answered in the interim commits named in §4
  R833  tests/unit/test_run_config.py:381 -- no change at that exact site; answered in the interim commits named in §4
  R834  docs/reports/R1/step-2.md:115 -- no change at that exact site; answered in the interim commits named in §4
  R834  docs/reports/R1/step-2.md:116 -- no change at that exact site; answered in the interim commits named in §4
  R834  docs/reports/R1/step-2.md:117 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/config.py:248 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/config.py:249 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/config.py:250 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/config.py:251 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/config.py:252 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/config.py:669 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:163 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:164 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:165 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:166 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:167 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:168 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:169 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:170 -- no change at that exact site; answered in the interim commits named in §4
  R834  floatfea/run/pipeline.py:171 -- no change at that exact site; answered in the interim commits named in §4
  R835  tests/test_report_carried.py -- no change at that exact site; recorded in §7; a directive for Xabier, not an edit
  R835  tests/test_report_guard_states.py -- no change at that exact site; recorded in §7; a directive for Xabier, not an edit
  R836  scripts/measure/r754_stress_vs_grade.py -- no change at that exact site; recorded in revision 2 §7, margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:81 -- no change at that exact site; recorded in revision 2 §7, margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:82 -- no change at that exact site; recorded in revision 2 §7, margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:83 -- no change at that exact site; recorded in revision 2 §7, margin re-measured
  R836  scripts/measure/r754_stress_vs_grade.py:84 -- no change at that exact site; recorded in revision 2 §7, margin re-measured
  R837  docs/reports/R1/step-2.md:1002 -- no change at that exact site; answered in the interim commits named in §4
  R837  docs/reports/R1/step-2.md:1003 -- no change at that exact site; answered in the interim commits named in §4
  R837  docs/reports/R1/step-2.md:1004 -- no change at that exact site; answered in the interim commits named in §4
  R837  docs/reports/R1/step-2.md:1005 -- no change at that exact site; answered in the interim commits named in §4
  R837  docs/reports/R1/step-2.md:1006 -- no change at that exact site; answered in the interim commits named in §4
  R837  docs/reports/R1/step-2.md:1007 -- no change at that exact site; answered in the interim commits named in §4
  R837  docs/reports/R1/step-2.md:1008 -- no change at that exact site; answered in the interim commits named in §4
  R837  floatfea/cli.py:343 -- no change at that exact site; answered in the interim commits named in §4
  R837  floatfea/run/config.py:233 -- no change at that exact site; answered in the interim commits named in §4
  R837  floatfea/run/config.py:852 -- no change at that exact site; answered in the interim commits named in §4
  R837  report.md -- no change at that exact site; answered in the interim commits named in §4
  R838  cli.py -- no change at that exact site; answered in §2, both EH4 directions
  R838  test_f6_deliverable_agrees_with_itself.py -- no change at that exact site; answered in §2, both EH4 directions
  R838  test_r1_example_golden.py -- no change at that exact site; answered in §2, both EH4 directions
  R838  tests/regression/test_f6_deliverable_agrees_with_itself.py:191 -- no change at that exact site; answered in §2, both EH4 directions
  R839  scripts/suite_count.py -- no change at that exact site; ledgered under FR1; corrected in §5 anyway
  R839  suite_count.py -- no change at that exact site; ledgered under FR1; corrected in §5 anyway
  R839  tests/test_report_carried.py -- no change at that exact site; ledgered under FR1; corrected in §5 anyway
  R840  docs/reviews/R1/step-2.md -- no change at that exact site; answered in §3
  R840  scripts/carried_table.py -- no change at that exact site; answered in §3
  R840  scripts/suite_count.py -- no change at that exact site; answered in §3
  R841  carried_table.py -- no change at that exact site; answered in §3 by the regeneration
  R841  tests/test_report_carried.py:1117 -- no change at that exact site; answered in §3 by the regeneration
  R841  tests/test_report_carried.py:1118 -- no change at that exact site; answered in §3 by the regeneration
  R841  tests/test_report_carried.py:1119 -- no change at that exact site; answered in §3 by the regeneration
  R841  tests/test_report_carried.py:1120 -- no change at that exact site; answered in §3 by the regeneration
  R841  tests/test_report_carried.py:1121 -- no change at that exact site; answered in §3 by the regeneration
  R843  floatfea/cli.py:343 -- no change at that exact site; answered in the interim commits named in §4
  R844  docs/reviews/R1/step-2.md:93 -- no change at that exact site; answered in the interim commits named in §4
  R844  floatfea/run/config.py:858 -- no change at that exact site; answered in the interim commits named in §4
```

## 7. Step 2 closes here — what is done, and what is NOT

- **FL2 is not built in step 2 and was never going to be.** FR2 moved it to step 3 and FR3
  says all five items are built before step 3's first reviewed revision. §9 of revision 1
  carries the per-item estimate they are measured against.
- **No tolerance was added, moved or widened in any of step 2's three revisions.**
  `floatfea/tolerances.py` is untouched by this revision; FQ0's clause constant moved in
  revision 1 and is recorded there with its counter solved in both directions.
- **No new apparatus.** R838 is two needles on a gate R831 already changed; R840 is an
  escape; R841 is a regeneration. Nothing new, nothing extended.
- **The closure list carries forward** into `docs/closure/R1.md`.

```
claim  exactly which items carry, taken from the pointer file rather than retyped
cmd    python -c "import json; d=json.load(open('docs/reports/R1/step-2-answers.json'));
       print(' '.join(k for k,v in d['answered'].items()
       if k.startswith('C') and v['state']=='later'))"
out    C26 C27 C28 C30 C31 C32 C33 C36 C37 C39
rule   CZ0 -- the implementer fixes the whole list once, in the step's closure commit, and
       it is not re-reviewed item by item; FR2 ledgers the rest
judge  ten items, and C42 is not among them because it is recorded as the reviewer's.
```
- **R835 goes to Xabier and is not acted on here.** Both reviewers and both of my own
  measurements say EG3's enumerated lists are wrong in both directions while the membership
  rule has never been; the proposal is to delete the lists and keep the rule. CLAUDE.md's
  lists are adopted by directive, so that is his edit and not mine.
- **The corpus pause holds.** The reviewer's adversarial cases are untouched by me.
