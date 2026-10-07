# F4 step 2 — the dynamic case, the load mapping, and a new mass basis

Answers: verdict 96 @ 5786bed

# Revision 1 — EQ0, EQ2's basis-independent half, and ER1's premise check

Answers: verdict 96 @ 5786bed

**2026-10-06.**

## 0. CI at `84de436`, the commit verdict 96 judged — conclusion **SUCCESS**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 96 at `84de436` through the report's own `Answers:` line. Run `37424376028`, event `push`, conclusion **success**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1892 | 0 | 0 |
| lint, unit and guards | 1042 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 0 not green.**

**Failing tests named in the log: 0.**

## 0a. Runs since the commit verdict 96 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 96 at `84de436` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37424376028` | push | `84de436` | conclusion **success** |
| `37431234061` | push | `5786bed` | conclusion **success** |
| `37478402259` | push | `b979b68` | conclusion **failure** |

**Run `37478402259`, conclusion **failure**: 1 failing test name(s) in the log.**
- `tests/test_no_tolerance_literals.py::test_no_undeclared_tolerance_reaches_a_comparison[test_f4_static_and_mapping.py]` (lint, unit and guards)

## 0b. The reds at this commit are EG3 state (1), traced by name (EG3(i))

**EIGHT reds, and every one traces to a single cause: step 2 has a report and no verdict
yet.** My first draft of this section claimed the guard-state baseline was green, and
quoted a count for it. That was false: the figure was taken before the step marker moved
from 1 to 2, and I had not re-run it at this content when I wrote the sentence. It is the
same shape as § 12a -- a count carried across a change that invalidated it. The corrected
measurement:

```
claim  the report-guard files give one red, and it is state (1)'s own named test
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py -q -rf
out    FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    1 failed, 252 passed in 2.73s
```

```
claim  the guard-state file gives seven, and they are the cascade off a red baseline
cmd    python -m pytest tests/test_report_guard_states.py -q -rf
out    7 failed, 16 passed in 140.95s
out    FAILED ...[baseline]
out    FAILED ...[non_numeric_step_suffix]
out    FAILED ...[superscript_digit_step_number]
out    FAILED ...[draft_suffix_beside_a_step_report]
out    FAILED ...[step_number_is_the_empty_string]
out    FAILED ...[verdict_amended_after_the_commit_the_report_answers]
out    FAILED ...[zero_padded_step_number]
rule   EH1: the cascade is identified by the BASELINE being red and by each cascading
       state's own failure line, not by its name
```

```
claim  the baseline's nested run fails for that one reason and says so itself
cmd    python -m pytest "tests/test_report_guard_states.py::test_the_guard_survives_the_
       state[baseline]" -q --tb=long
out    AssertionError: step 2 has a report and no verdict yet. That is the legitimate
out    boundary -- the verdict is written after the report is committed -- and until it
out    lands this guard checks step 2, so step 2's carry list is UNCHECKED. Invoke the
out    gating-supervisor.
out    FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    1 failed, 217 passed in 3.03s
judge  THIS IS STATE (1): report written, verdict not yet. The step marker moved from 1
       to 2 with this report, so `docs/reviews/F4/step-2.md` does not exist and every
       nested run inherits the same single failure. The reviewer measures it clearing at
       the verdict commit. ANY failure outside this trace would be CZ1 (iv) unchanged,
       and there is none -- the eight ids above are the whole list.
```

## 1. The reading

**This revision exists because the `Stop` hook required a verdict covering the tree, not
because step 2's work is done.** EQ3 says "one reviewer invocation, at the report", and
the report EQ3 means is the one at the end of step 2. Three commits of step-2 work landed
first — EQ0's rule, EQ2's basis-independent half, and ER1(c)'s premise check — and the
hook refuses a turn while `floatfea/` or `tests/` has moved past the newest verdict. I
cannot write a verdict and I will not revert verified work to silence a hook, so the
honest resolution is a real report of what has actually landed, early.

**I am asking the reviewer to rule on whether this round counts against step 2's three.**
My reading is that it should not: EB4 exempts a verdict whose occasion belongs to the
process rather than to the work, and the occasion here is a hook firing on a mid-step
commit. But that is a reading of EB4, not EB4, and it is the reviewer's call. If it does
count, step 2 has two rounds for ER1's remainder plus the whole of EQ3, and I would want
that said now rather than discovered at the third verdict.

**Measured against the dates, today, 6 October.**

| what | date | status today |
|---|---|---|
| F4 working target | 14 Oct | **at risk** — ER1 is a two-day item, see § 8 |
| member-force table | 17 Oct working, 23 Oct committed | on track |
| code check | 22 Oct working, 28 Oct committed | on track |
| F4 committed | 19 Oct | on track |

```
claim  the dates in that table are the ones the plan sets, not mine
cmd    grep -n '19 Oct\|23 Oct\|28 Oct' docs/milestones/F4.md | head -4
out    375:| F4 | 19 Oct | 14 Oct |
out    376:| member-force table | 23 Oct | 17 Oct |
out    377:| code check | 28 Oct | 22 Oct |
rule   CZ0: slippage is reported the day it is known
judge  ER1 arrived today and is two days of work (§ 8). The 14 Oct WORKING target is
       what absorbs it; the committed dates do not move and I am not asking them to.
```

## 2. EQ0 — the rule adopted, in the reviewer's wording

Committed standalone at `9985bcd`, touching `CLAUDE.md` and `docs/SUPERVISOR.md` and
nothing else, as the rule about the reviewer's own instructions requires.

```
claim  the clause is in both files, at the same anchor, identical
cmd    git show --stat 9985bcd
out    CLAUDE.md          | 40 ++++++++++++++++++++++++++++++++++++++++
out    docs/SUPERVISOR.md | 40 ++++++++++++++++++++++++++++++++++++++++
out    2 files changed, 80 insertions(+)
judge  both files already carried the CZ1 section verbatim, so the clause appends at the
       same anchor and they stay identical rather than drifting -- which is the thing
       C131 keeps naming.
```

It records the rule — *a closure commit that changes a gate or a tolerance is reviewed;
one that changes only prose is not* — that the review counts against no step's rounds,
and **why a green suite was not enough**, which is the argument for it: a counter on the
wrong side of its own defect, a decision rule nothing holds in place, and four figures
whose rule the same commit deleted were all invisible to `pytest -q`, to the lint trio,
and to a green CI run at the commit's own sha. It also records EK3's mechanical reason
with the three-run measurement behind it.

## 3. ER1(c) — the STOP check on ER0's new mass basis, and it does NOT stop

ER1(c): "The admissibility check still applies; if any body is not PSD at 0.75, STOP and
report." Every body is PSD. The override is applied **in memory** to a copy of the deck,
so the generated file stays generator-only and nothing is hand-edited.

```
claim  the override is ER0's, at model scale, with the reference point untouched
cmd    python scratchpad/er1c_stop.py
out    platform mass    10.0 -> 20.0   (model scale)
out    platform Ixx/Iyy/Izz 10.0/10.0/20.0 -> 20.0/20.0/40.0
out    platform reference point [0.0, 0.0, 0.7]  (UNCHANGED, ER0(b))
rule   ER0(a) scales the inertia with the mass; ER0(b) leaves the CoG where it is
```

```
claim  every body is admissible at f = 0.75 on the new basis -- NO STOP
cmd    python scratchpad/er1c_stop.py
out    platform  f=0.75  admissible=True  m_member=1.875000e+06  m_remainder=6.250000e+05
out    hub1..4   f=0.75  admissible=True  m_member=1.125000e+06  m_remainder=3.750000e+05
rule   `admissible()`: `m_r >= 0` and no eigenvalue of `J_r` below `-tol` (DY0d)
judge  `admissible()` is CALLED, not re-implemented, so this is the shipped decision and
       not a second opinion about it.
```

**The three quantities ER0 asks to be reported, per body:**

| body | remainder position (full scale) | link | eig(J_r) | triangle slack | rho_eq |
|---|---|---|---|---|---|
| platform | `[3.4e-15, -3.0e-15, 65.995]` | `41.326086` m | `4.666294e+09`, `4.666294e+09`, `1.093623e+10` | `-1.603643e+09` | `7146.0` |
| hub1 | `[50, 0, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522913e+06` | `11433.5` |
| hub2 | `[0, 50, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522912e+06` | `11433.5` |
| hub3 | `[-50, 0, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522913e+06` | `11433.5` |
| hub4 | `[0, -50, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522913e+06` | `11433.5` |

**ER0(b)'s prediction is confirmed and the reason it holds is worth stating.** The
remainder sits `41.326086 m` above the joint plane, which is the "≈ 41 m" ER0(b) expected
— and that link length is **unchanged from the old basis**, because the remainder's
position is fixed by matching the deck's CoG and that constraint is linear in mass.
Doubling the mass doubles `m_remainder` and moves the lever not at all.

```
claim  the link length does not move when the mass doubles
cmd    python scratchpad/er1c_stop.py   (the NEW BASIS and OLD BASIS blocks, both f=0.75)
out    new basis: |link| = 41.326086 m, m_remainder = 6.250000e+05
out    old basis: |link| = 41.326086 m, m_remainder = 3.125000e+05
cell   only the platform's mass and inertia moved; the geometry, the reference point,
       the joints and f are all held
```

**The negative triangle slack is inherited, not created**, which DZ5 recorded and EA3
ruled on: the deck's own `J_G` sits on the lamina boundary, `admissible()` tests PSD and
deliberately not realisability, and the slack is negative at every `f > 0` on either
basis.

**And the sizing problem has moved to the hubs.**

```
claim  the platform's equivalent density is now BELOW steel and the hubs' is above it
cmd    python scratchpad/er1c_stop.py   (the rho_eq lines of all three blocks)
out    new basis, f=0.75:  platform rho_eq = 7146.0   hub1..4 rho_eq = 11433.5
out    old basis, f=0.75:  platform rho_eq = 3573.0   hub1..4 rho_eq = 11433.5
out    new basis, ladder:  platform rho_eq = 4764.0   hub1..4 rho_eq = 7622.4
rule   `basis.RHO_STEEL` = 7850 kg/m^3, which is the value `_build_body` reports a
       finding against
cell   between the two f=0.75 rows only the platform's mass and inertia moved, so the
       platform figure doubles and the hub figure does not move at all
judge  the platform doubled from 3573.0 to 7146.0 and is still under steel; the hubs
       are unchanged because their mass is unchanged and only `f` moved. On this basis
       the density finding is a hub-section question and not a platform one.
```

## 3a. ER1(d) — Xabier's static arithmetic, confirmed

All eight figures reproduce exactly. Nothing to correct.

| | R | w·L | root Vz | root My |
|---|---|---|---|---|
| platform arm | `6,131,250` N | `4,598,437.5` N | `1,532,812.5` N | `191,601,562.5` N·m |
| hub arm | `6,948,750` N | `3,678,750` N | `3,270,000` N | `127,734,375` N·m |

```
claim  each of the eight follows from ER0's inputs and the Froude table, by hand
cmd    20.0 kg * 125000 = 2.5e6 kg ; * 9.81 = 24,525,000 N ; / 4 arms = 6,131,250 N
       0.75 * 2.5e6 / 4 = 468,750 kg ; * 9.81 = 4,598,437.5 N
       6,131,250 - 4,598,437.5 = 1,532,812.5 N
       6,131,250 * 50 - 4,598,437.5 * 25 = 191,601,562.5 N.m
       12.0 kg * 125000 * 9.81 = 14,715,000 N ; + 6,131,250 handed down = 20,846,250 N
       / 3 arms = 6,948,750 N ; 0.75 * 1.5e6 / 3 * 9.81 = 3,678,750 N
       6,948,750 - 3,678,750 = 3,270,000 N
       6,948,750 * 25 - 3,678,750 * 12.5 = 127,734,375 N.m
out    every line above evaluates to the figure ER1(d) states
rule   mass and force scale as lambda^3 = 125000; length as lambda = 50
judge  these are the EXPECTED values the static analytic gate will assert against once
       ER1 lands. They are not asserted yet, and § 7 is why.
```

## 4. R683 — the counter-case that holds R679's rule in place exists now

```
claim  the parametrisation carries `internal_joint_dropped`
cmd    grep -rn internal_joint_dropped tests/verification/rung4/test_f4_static_and_mapping.py
out    861: "injection", ["sign_not_flipped", "wrong_node_same_body", "internal_joint_dropped"]
out    872: the docstring sentence that says what it is for
out    906: the comment that records why the claim was false before
rule   EQ2(b): a claim that a test exists is pasted from grep or `pytest -k`, never from
       memory
```

```
claim  reverting R679's per-body rule to the aggregate reddens it, and nothing else
cmd    python scratchpad/eq2_ablate.py
out    as shipped (per body)        28 passed in 0.56s
out    REVERTED to the aggregate    1 failed, 27 passed in 0.78s
out    RED  test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node[internal_joint_dropped]
cell   only the aggregation moved -- `_mapping_error` sums over bodies on both sides,
       exactly as it did before `ecace4a`. Every injection is untouched.
judge  ONE test reddens and it is the right one. Before this row both shipped
       counter-cases were red under the aggregate too, so reverting the rule left the
       whole suite green and nothing held it in place -- which is what R683 was.
```

**Why the closure commit's claim was false.** The patch that added the row raised before
writing, I read a stale `git diff --stat` as evidence it had applied, and then edited that
patch script in a way that removed the row entirely. The refutation was one `grep` and I
did not run it. EQ2(b)'s wording is the rule that would have caught it.

## 5. R684 — a legal sparse row no longer raises, and the zero case has its own answer

```
claim  a row with only `buoy1`'s block nonzero is legal and leaves four bodies at zero
cmd    python scratchpad/eq2_measure.py
out    joint_order[0] = ('buoy1', 'buoy1', 'hub1')
out    ||lam|| = 1.912540e+06   nonzero rows: 4 of 64
out    hub2, hub3, hub4, platform: expected resultant array([0., 0., 0., 0., 0., 0.])
out    the SHIPPED gate RAISES: AssertionError: hub2's expected resultants are
out    array([0., 0., 0., 0., 0., 0.]), so there is no scale to normalise by
judge  C158's replacement assertion said no body can have a zero resultant for a nonzero
       row. It can. The premise was the reviewer's and verdict 96 withdrew it; my
       implementation of it was faithful, which is the part worth saying -- a faithful
       implementation of a wrong premise is still a wrong gate.
```

```
claim  the mapper puts EXACTLY zero on a body with no applied load, so that case is
       asserted absolutely rather than normalised
cmd    python scratchpad/eq2_measure.py
out    hub2, hub3, hub4, platform: mapped max|.| = 0.0
out    hub1 (the one body that does carry load): 1.4085799532319176e+08
rule   EQ2(c): for a body whose applied load is exactly zero, assert that its mapped load
       is exactly zero (absolute); otherwise use the relative form
```

```
claim  restoring C158's assertion reddens the new counter-case, and nothing else
cmd    python scratchpad/eq2_ablate.py
out    as shipped (zero scale handled)  28 passed in 0.56s
out    C158's assertion restored        1 failed, 27 passed in 0.81s
out    RED  test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked
```

## 6. R653 — answered by name, because step 2 is the condition it was waiting for

Verdict 92 carried R653 on the condition that it becomes blocking "if a G4.x gate ever
cites this residual as evidence that FloatSim's scheme is reproduced". F4 step 2's G4.1
does exactly that, per body and per case, so it is answered rather than carried a fifth
time.

```
claim  the grep the driver's own comment recorded as empty now returns two files
cmd    grep -rln RHO_INF floatfea/ tests/
out    floatfea/io/integrator.py
out    tests/verification/rung4/test_f4_static_and_mapping.py
judge  the driver's comment said, in its own `cmd:`/`out:` pair, "(no output) -- nothing
       asserts this value". That was true and it is no longer.
```

```
claim  the closed form reproduces the interchange specification's own published
       coefficients, which are not derived from this code (EA4)
cmd    python -m pytest tests/verification/rung4 -q -k R653
out    2 passed, 155 deselected in 0.47s
rule   docs/load-interchange-v1.md SECTION 4, lines 259-260: at rho_inf = 0.9,
       alpha_m = 0.42105, alpha_f = 0.47368, difference 0.05263, gamma = 0.55263,
       beta = 0.27701 -- compared at five decimal places, which is exact
judge  NO TOLERANCE IS DECLARED and none is wanted: the specification publishes five
       places and the comparison is against the value rounded to five places. A ceiling
       here would be a number with nothing behind it.
```

`FLOATSIM_RHO_INF` and `generalized_alpha_coefficients` live in
`floatfea/io/integrator.py`; `scripts/report_joint_reactions.py` imports both and keeps no
copy of either, so the two-copies shape cannot return.

```
claim  the driver holds no copy of the constant or the derivation
cmd    grep -n 'RHO_INF\|alpha_m =' scripts/report_joint_reactions.py
out    RHO_INF = FLOATSIM_RHO_INF
out    alpha_m, alpha_f, beta, _gamma = generalized_alpha_coefficients(RHO_INF)
rule   C131: a rule written twice drifts, and an earlier version of this driver held two
       copies of this number whose 0.05 disagreement made the residual "429x louder"

claim  my first citation of the specification was false
cmd    grep -n '^## ' docs/load-interchange-v1.md | awk -F: '$1<=259' | tail -1
out    211:## 4. Time alignment is a required field
judge  I wrote "sec.6". Section 6 is `## 6. Two-pass generation`, which begins at line
       571 and is about something else entirely. A false citation in a docstring is the
       CW0 shape and it was mine; one grep settles it.
```

## 7. R682 and R685 — OPEN, held by ER2, and what is already measured

**These are not answered and I am not claiming they are.** ER2 puts ER1's new mass basis
before any step-2 tolerance work "so nothing is calibrated twice", and both items are
figures derived from `mu`, `M` and `f` — all three of which ER0 changes. Answering them on
the old basis and again on the new one is the double calibration ER2 exists to prevent.

**What is already measured, so the reviewer can see the work is done and only its basis is
waiting.** On the OLD basis, in the gate's own denominator:

```
claim  the counter 0.05 sits ABOVE the defect on 12 of the 16 members
cmd    python scratchpad/eq2_measure.py
out    platform:hub1_arm   defective root 1.2134765625000013e+08  tip/root 5.2631578947368425e-02  = 1/19
out    hub3:buoy9_arm      defective root 1.2262499999999999e+08  tip/root 4.1666666666666269e-02  = 1/24
out    SMALLEST over the 16: 0.04166666666666627 = 1/24 on hub3:buoy9_arm
out    LARGEST  over the 16: 0.05263157894736891 = 1/19
out    counter 0.05  below EVERY defect: False   members whose defect is below it: 12
out    counter 0.04  below EVERY defect: True    members whose defect is below it: 0
rule   the counter is the smallest defect the gate must still fail
judge  my published 5.555556e-02 divided by the CORRECT root moment; the gate divides by
       the DEFECTIVE one, which is larger by exactly the tip moment being tested. No
       member reads 5.555556e-02 on either basis.
```

The test-side half of R682 — the counter-case running over all 16 members instead of the
platform's first — is written and was reverted with the value, because a counter-case over
16 members and a counter declared for one are not a consistent pair. Both land together on
the new basis.

R685's four figures are re-measured under the per-body rule and are in hand:

```
claim  the mapping entry's four figures, under the rule that replaced the aggregate
cmd    python scratchpad/eq2_measure.py
out    clean, per body                       : 2.1962235947826024e-16
out    ceiling 1.0e-12 is above it by        : 4553.3x
out    wrong node, same body: force 2.092543223926032e-16
out                           moment 0.9597085787263796
out    sign not flipped     : worst  3.5569621874567385
rule   relative, force and moment normalised separately, worst over the five bodies
judge  the `0.2` counter does NOT move: under the aggregate the wrong-node injection
       measured 0.24374825705420716 and 0.2 was the round bound below it; per body the
       same injection is about four times larger, so 0.2 is further below the defect
       than it was declared to be. It errs safe and the ordering it depends on survives.
```

They are held with R682 so that `floatfea/tolerances.py` changes once.

## 8. ER1's cost, said the day I know it

**ER1 is a two-day item, not a one-day item.** ER1 asks me to say so the day I know, and I
know today.

* **ER1(b) is the long pole.** Six FloatSim design-wave re-runs in `../HSP-runs` with the
  override applied in memory by the run script, a fresh `res.lam` export, then EK0(a)
  repeated over all 24,006 steps and the EJ4 per-body residual on the new runs. The
  REPLAY alone was about 25 minutes of solve time this session; full runs with export are
  longer, and the in-memory override is new code written against HSP-stable's API, which
  stays read-only at `floatfea-ref-1`.
* **ER1(d) is the wide one.** BP0 requires every figure and counter that depends on `mu`,
  `M` or `f` re-derived in the SAME commit: the static analytic gate's four expected
  values, the tip-moment counter, `F4_STATIC_REACTION_AGREEMENT_COUNTER`, the symmetry
  counter, the conservation counter, and ER0 into both `F3.md` § 0 and `F4.md` § 0.
* **(a), (c) and (e)** are a few hours each. (c) is now a one-line default change plus the
  findings it reports, because § 3 has already measured that it is admissible.

**A suggestion rather than a request:** ER3's preview issue 4 needs the new runs only for
its dynamic columns. The static-only columns and the `f = 0.5` / `f = 1.0` sensitivity need
only ER1(c), which is done — so a static-only issue 4 is available inside a day if that is
worth having before the dynamic half.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R622 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R626 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R631 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R635 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R638 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R653 | carried | **answered** | §6 | `` | carried from an earlier verdict |
| R656 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R663 | recorded | **NOT ANSWERED** |  | `` | , A DEFECT IN `floatfea/`.) `floatfea/post/member_forces.py:78` |
| R664 | recorded | **NOT ANSWERED** |  | `` | , A GATE ASSERTION THAT CANNOT FAIL.) |
| R665 | recorded | **NOT ANSWERED** |  | `` | .) THE EK0(d) SUPPORT-SCHEME CHECK CANNOT FAIL, AND NO THRESHOLD IS |
| R666 | recorded | **NOT ANSWERED** |  | `` | , THREE RED TESTS THAT ARE NOT THE MILESTONE BOUNDARY, AND CI IS |
| R667 | recorded | **NOT ANSWERED** |  | `` | .) EB6's GATE DOES NOT EXIST, AND REPORT SECTION 7 REPORTS A SECOND |
| R668 | recorded | **NOT ANSWERED** |  | `` | .) THE EK0(e) DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE STATE |
| R669 | recorded | **NOT ANSWERED** |  | `` | .) FOUR GATE ROWS THE LOCKED PLAN MARKS "TO BE MEASURED AT STEP 1" |
| R670 | recorded | **NOT ANSWERED** |  | `` | , CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4.) |
| R671 | recorded | **NOT ANSWERED** |  | `` | , A TOLERANCE WHOSE CEILING NOTHING BOUNDS ABOVE.) |
| R672 | recorded | **NOT ANSWERED** |  | `` | , CARRIED FROM VERDICT 93 AND UNANSWERED.) R665 IS UNTOUCHED AT |
| R673 | recorded | **NOT ANSWERED** |  | `` | , 39 RED TESTS AT THE REVIEWED COMMIT AND NOT ONE IS A BOUNDARY |
| R674 | recorded | **NOT ANSWERED** |  | `` | and (c), THE COUNTER-CASE DOES NOT RUN THE INJECTION IT NAMES, AND |
| R675 | recorded | **NOT ANSWERED** |  | `` | , TWO GATES WHOSE REACH IS NARROWER THAN THE TABLE CLAIMS, ONE OF |
| R676 | recorded | **NOT ANSWERED** |  | `` | , CARRIED FROM VERDICT 93 AND ANSWERED FOR ONE ROW OF FOUR.) THREE |
| R677 | recorded | **NOT ANSWERED** |  | `` | and (b), R663 CLOSING CONDITION SECOND BRANCH IS NOT MET: IT |
| R678 | recorded | **NOT ANSWERED** |  | `` | , R668 SECOND CLAUSE, UNTOUCHED.) `duality_residual` STILL RETURNS |
| R679 | recorded | **answered** | §9a | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) G4.4's GATE SUMS ITS |
| R680 | recorded | **answered** | §9a | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) R675's BODY AVERAGE IS |
| R681 | recorded | **answered** | §9a | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) `F4_STATIC_TIP_MOMENT_N_M = |
| R682 | recorded | **open** | §7 | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) |
| R683 | recorded | **answered** | §4 | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) NOTHING IN THE TREE HOLDS |
| R684 | recorded | **answered** | §5 | `` | , AND IT CARRIES INTO STEP 2 BY NAME. THE PREMISE IT RESTS ON WAS |
| R685 | recorded | **open** | §7 | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) THE `F4_MAPPING_CONSERVATION` |

**16 finding(s) with no row in the answers file: ['R663', 'R664', 'R665', 'R666', 'R667', 'R668', 'R669', 'R670', 'R671', 'R672', 'R673', 'R674', 'R675', 'R676', 'R677', 'R678'].**

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R663 | `docs/reports/F4/preview-PRELIMINARY.md` | the file is untouched | **no change** — answered at step 1 (R677, the required argument). Step 2's range does not touch this site. |
| R663 | `floatfea/post/member_forces.py:78` | the file is untouched | **no change** — answered at step 1 (R677, the required argument). Step 2's range does not touch this site. |
| R664 | `floatfea/solve/static.py:92` | the file is untouched | **no change** — answered at step 1 (R674, the signed comparison). Step 2's range does not touch this site. |
| R665 | `floatfea/loads/selfweight.py:86` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R665 | `floatfea/solve/static.py:21` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R665 | `floatfea/solve/static.py:22` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R665 | `floatfea/solve/static.py:23` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R667 | `docs/closure/F3.md:179` | the file is untouched | **no change** — answered at step 1 (R670's pinned snapshot and R676's hub side). |
| R667 | `tests/verification/rung3/test_platform_skeleton.py:711` | the file is untouched | **no change** — answered at step 1 (R670's pinned snapshot and R676's hub side). |
| R668 | `joint_reactions.py:89` | the file is touched and this line number is the old one | **no change** — answered at step 1 (R678, `duality_residual` raises). |
| R670 | `scripts/run_rung.sh:274` | the file is untouched | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `scripts/run_rung.sh:275` | the file is untouched | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `scripts/run_rung.sh:276` | the file is untouched | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:265` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:266` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:267` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:268` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:269` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:270` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:271` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:272` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R671 | `floatfea/tolerances.py:1888` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:89` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:90` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:91` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:92` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:93` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:94` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R672 | `floatfea/loads/selfweight.py` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `floatfea/solve/static.py` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `static.py:21` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `static.py:22` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `static.py:23` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R673 | `scripts/suite_count.py` | the file is untouched | **no change** — answered at step 1; `scripts/suite_count.py` was correct and simply had not been run. |
| R674 | `static.py:86` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:87` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:88` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:89` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:90` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:91` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `tests/verification/rung4/test_f4_static_and_mapping.py:161` | the file is touched and this line number is the old one | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R677 | `floatfea/post/member_forces.py:95` | the file is untouched | **no change** — answered at step 1; `f_eq_global` is a required argument. |
| R678 | `floatfea/loads/joint_reactions.py` | the file is untouched | **no change** — answered at step 1; the both-zero case raises. |
| R679 | `docs/milestones/F4.md:310` | the file is touched and this line number is the old one | **no change** — answered in step 1's closure commit, per body, and verified by verdict 96 (§ 9a). |
| R681 | `floatfea/tolerances.py:1966` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1967` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1968` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1969` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1970` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1971` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1972` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1973` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `test_f4_static_and_mapping.py:504` | the file is touched and this line number is the old one | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R682 | `F4.md:346` | the file is touched and this line number is the old one | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R682 | `docs/milestones/F4.md:346` | the file is touched and this line number is the old one | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R682 | `floatfea/tolerances.py` | the file is untouched | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R682 | `test_f4_static_and_mapping.py:552` | the file is touched and this line number is the old one | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R685 | `floatfea/tolerances.py` | the file is untouched | **no change** — OPEN and HELD by ER2 with R682, so `tolerances.py` changes once (§ 7). |

## 9. Carried

Generated: `python scripts/carried_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R622 | **carried** — §9b | F4's own, not yet reached. |
| R626 | **carried** — §9b | 's residue, R635 and the long closed |
| R631 | **carried** — §9b | 's residue, R635 and the long closed |
| R635 | **carried** — §9b | no clause this generator can cut -- see the verdict's Carried section |
| R637 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R638 | **carried** — §9b | OPEN, unchanged, EJ1 governs, closed before F4 closes. floatfea/tolerances.py |
| R653 | **answered** — §6 | OPEN, carried, and about to become (c). A grep for RHO_INF over tests and |
| R654 | **not classified in this verdict** — carried in from an earlier one | CLOSED, not reopened, nothing in this range touches their sites. |
| R655 | **not classified in this verdict** — carried in from an earlier one | CLOSED, not reopened, nothing in this range touches their sites. |
| R656 | **carried** — §9b | OPEN WITH XABIER, unchanged, correctly not repaired. scripts/ci_section.py is |
| R657 | **not classified in this verdict** — carried in from an earlier one | ANSWERED AND CLOSED at e505f28. The word is mine. Section 8 carries the |
| R658 | **not classified in this verdict** — carried in from an earlier one | ANSWERED AND CLOSED at e505f28, same constant, same commit, same reading. |
| R659 | **not classified in this verdict** — carried in from an earlier one | CLOSED, not reopened, nothing in this range touches their sites. |
| R660 | **not classified in this verdict** — carried in from an earlier one | ANSWERED at 0c490bf, the standalone closure commit verdict 92 said was worth |
| R661 | **not classified in this verdict** — carried in from an earlier one | ANSWERED in report section 8, where EK3 puts it, and the cause is correctly |
| R662 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R663 | **open** — blocking, and not answered in this round | , A DEFECT IN floatfea/.) floatfea/post/member_forces.py:78 RETURNS THE ELEMENT NODAL FORCE AND... |
| R664 | **open** — blocking, and not answered in this round | , A GATE ASSERTION THAT CANNOT FAIL.) floatfea/solve/static.py:92: StaticCase.sum_error IS AN... |
| R665 | **open** — blocking, and not answered in this round | .) THE EK0(d) SUPPORT-SCHEME CHECK CANNOT FAIL, AND NO THRESHOLD IS DECLARED FOR IT.... |
| R666 | **open** — blocking, and not answered in this round | , THREE RED TESTS THAT ARE NOT THE MILESTONE BOUNDARY, AND CI IS RED AT THE REVIEWED COMMIT.)... |
| R667 | **open** — blocking, and not answered in this round | .) EB6's GATE DOES NOT EXIST, AND REPORT SECTION 7 REPORTS A SECOND SIDE TO A FIRST SIDE THAT... |
| R668 | **open** — blocking, and not answered in this round | .) THE EK0(e) DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE STATE THE DOCSTRING NAMES IS... |
| R669 | **open** — blocking, and not answered in this round | .) FOUR GATE ROWS THE LOCKED PLAN MARKS "TO BE MEASURED AT STEP 1" HAVE NO ASSERTION ANYWHERE,... |
| R670 | **open** — blocking, and not answered in this round | , CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4.)... |
| R671 | **open** — blocking, and not answered in this round | , A TOLERANCE WHOSE CEILING NOTHING BOUNDS ABOVE.) floatfea/tolerances.py:1888... |
| R672 | **open** — blocking, and not answered in this round | , CARRIED FROM VERDICT 93 AND UNANSWERED.) R665 IS UNTOUCHED AT EVERY SITE ITS CLOSING... |
| R673 | **open** — blocking, and not answered in this round | , 39 RED TESTS AT THE REVIEWED COMMIT AND NOT ONE IS A BOUNDARY RED.) Section 8 traces all 39... |
| R674 | **open** — blocking, and not answered in this round | and (c), THE COUNTER-CASE DOES NOT RUN THE INJECTION IT NAMES, AND THE GATE IS SIGN-BLIND ON... |
| R675 | **open** — blocking, and not answered in this round | , TWO GATES WHOSE REACH IS NARROWER THAN THE TABLE CLAIMS, ONE OF THEM VACUOUSLY PASSABLE.)... |
| R676 | **open** — blocking, and not answered in this round | , CARRIED FROM VERDICT 93 AND ANSWERED FOR ONE ROW OF FOUR.) THREE OF R669 FOUR GATE ROWS STILL... |
| R677 | **open** — blocking, and not answered in this round | and (b), R663 CLOSING CONDITION SECOND BRANCH IS NOT MET: IT DEFAULTS.)... |
| R678 | **open** — blocking, and not answered in this round | , R668 SECOND CLAUSE, UNTOUCHED.) duality_residual STILL RETURNS 0.0 FOR A BOTH-ZERO SHARE,... |
| R679 | **answered** — §9a | , AND IT CARRIES INTO STEP 2 BY NAME.) G4.4's GATE SUMS ITS RESIDUAL OVER ALL FIVE BODIES, SO... |
| R680 | **answered** — §9a | , AND IT CARRIES INTO STEP 2 BY NAME.) R675's BODY AVERAGE IS STILL LIVE IN... |
| R681 | **answered** — §9a | , AND IT CARRIES INTO STEP 2 BY NAME.) F4_STATIC_TIP_MOMENT_N_M = 1.0 IS AN ABSOLUTE TOLERANCE... |
| R682 | **open** — §7 | , AND IT CARRIES INTO STEP 2 BY NAME.) F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05 IS DECLARED... |
| R683 | **answered** — §4 | , AND IT CARRIES INTO STEP 2 BY NAME.) NOTHING IN THE TREE HOLDS R679'S PER-BODY RESIDUAL IN... |
| R684 | **answered** — §5 | , AND IT CARRIES INTO STEP 2 BY NAME. THE PREMISE IT RESTS ON WAS MINE AND I WITHDRAW IT.)... |
| R685 | **open** — §7 | , AND IT CARRIES INTO STEP 2 BY NAME.) THE F4_MAPPING_CONSERVATION ENTRIES REPUBLISH FOUR... |

### 9a. Answered in step 1's closure commit and verified by verdict 96

* **R679, R680, R681** — fixed in `ecace4a` and reproduced by the reviewer at
  `84de436`: R679's per-body rule (`1.778481e+00` and `1.635665e+00` against the
  aggregate's `1.872582e-16` and `9.362910e-17`), R680's `rho A L`, R681's relative
  tip-moment form. This revision did no work on them, which is why they point here.

### 9b. Open elsewhere, not answered in this round

* **R638** — open under EJ1, which requires it answered before F4 ends.
* **R656** — open with Xabier.
* **R622, R626, R631, R635** — on the EJ3 ledger at `docs/closure/F3.md` § 8, unchanged
  and not re-reviewed (CZ0).

### 9c. Closure items

**C161 to C166 and C137/C141/C144/C145/C147/C148/C151 are open and go into step 2's
closure commit, not re-reviewed item by item (CZ0).** One of them is answered early
because it is housekeeping the directive asked for by name: **C166** is § 10.

## 10. Housekeeping — the stale worktree registrations (EQ4)

EQ4 asks for the paths so they can be deleted by hand. `git worktree prune` cannot remove
them on this machine: it exits `Permission denied` on the pack files inside each
registration.

```
claim  nine registrations, of which eight are stale
cmd    git worktree list
out    C:/Users/xlama/OneDrive/Documents/buoy/FLOATFEA  b979b68 [F3]   <- the real one
out    C:/Users/xlama/AppData/Local/Temp/claude/C--Users-xlama-OneDrive-Documents-buoy-
out      FLOATFEA/ec986bd8-d1bc-48a2-918b-168c4b1be465/scratchpad/wt84  8368c51
out    C:/Users/xlama/AppData/Local/Temp/suite-count-6_es7sst/tree      3fdfc79
out    C:/Users/xlama/AppData/Local/Temp/suite-count-6mfeb05h/tree      f839dd8
out    C:/Users/xlama/AppData/Local/Temp/suite-count-f78bb4m4/tree      3fdfc79
out    C:/Users/xlama/AppData/Local/Temp/suite-count-f_sfu9l2/tree      8beb0e4
out    C:/Users/xlama/AppData/Local/Temp/suite-count-qcfoceyc/tree      3fdfc79
out    C:/Users/xlama/AppData/Local/Temp/suite-count-qj9dnjl4/tree      24e8bb2
out    C:/Users/xlama/AppData/Local/Temp/suite-count-woj9990l/tree      8beb0e4
judge  the `wt84` one is a reviewer worktree from F3 step 3's eighty-fourth verdict and
       the seven others are `scripts/suite_count.py`'s. Since C154, `_real_git_dir_into`
       copies the whole common directory into every scratch build of the guard-state
       harness, and these registrations go with it -- harmless, and a reason to clear
       them rather than leave them accumulating.
```

**To clear them:** delete the eight folders listed above, then
`git worktree prune` in the repository.

## 11. Tolerances touched

**NONE.** No value, form, counter or injection changed in this revision.

```
claim  floatfea/tolerances.py is untouched across this revision's range
cmd    git diff --stat 5786bed..HEAD -- floatfea/tolerances.py
out    (no output)
rule   BR0: a tolerance moves with a plan edit, and no tolerance moved
judge  R682 and R685 are the two items that would have moved it, and § 7 is why they did
       not. `docs/milestones/F4.md` changed only in its step marker, 1 -> 2.
```

## 12. The whole suite

Generated by `python scripts/suite_count.py`, run AFTER every other edit (CP3).

**Whole suite at `b979b68`: 2753 passed, 1 failed, 0 skipped.** **The excluded set: 271 passed, 0 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 271 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed** `tests.test_no_tolerance_literals::test_no_undeclared_tolerance_reaches_a_comparison[test_f4_static_and_mapping.py]`
```

### 12a. The one red at `b979b68` was mine, and it is fixed in this revision's commit

```
claim  `b979b68` shipped a red that rung 4 could not see
cmd    python -m pytest "tests/test_no_tolerance_literals.py::test_no_undeclared_
       tolerance_reaches_a_comparison[test_f4_static_and_mapping.py]" -q
out    line 1008: comparison against 0.05263
out    line 1021: comparison against 0.8
out    line 1028: comparison against 0.5
judge  all three are in MY R653 gate, and none of them is a tolerance: `0.05263` is a
       value the interchange specification PUBLISHES and is compared exactly after
       rounding to the five places it prints; `0.8` is FloatSim's spectral radius, the
       input R653 exists to pin; `0.5` and `1.0` are the mathematical ranges `beta` and
       `gamma` have for a dissipative step. The guard offers
       `# not-a-tolerance: <why it is an input>` for exactly this, and that is what they
       carry now.
```

```
claim  the marker has to sit on the comparison's OWN line, and my first attempt put it
       above
cmd    python -m pytest tests/test_no_tolerance_literals.py tests/verification/rung4 -q
out    first attempt (explanation above the assert): 1 failed, 211 passed
out    marker on the comparison line:                212 passed in 1.22s
rule   `_marker_lines` tokenises and collects the line of each COMMENT token carrying
       the marker, so a comment on the preceding line is not on the comparison's line
judge  the explanation stays above, where it is readable, and a short
       `# not-a-tolerance: see above` sits on the line the guard reads.
```

```
claim  CI caught the same three literals at the same commit, independently of me
cmd    gh run view <the b979b68 run in section 0a> --json conclusion,jobs ; then
       gh run view <it> --log-failed | grep 'comparison against'
out    conclusion: failure
out    JOB the verification ladder: success
out    JOB lint, unit and guards: failure
out        STEP guards and meta-tests: failure
out    E           line 1008: comparison against 0.05263
out    E           line 1021: comparison against 0.8
out    E           line 1028: comparison against 0.5
judge  the same three lines, to the line number, from a machine that did not know what
       I had run. The ladder job was GREEN there -- which is exactly why rung 4 could
       not see this and why "rung 4 is green" was not the claim I needed.
```

**HOW I SHIPPED IT, because the mechanism is the one CZ1 names.** I ran
`tests/verification/rung4` after reverting R682, and rung 4 was green:

```
claim  rung 4 was green at the commit that shipped the red
cmd    python -m pytest tests/verification/rung4 -q   [at b979b68]
out    157 passed in 1.01s
rule   `tests/test_no_tolerance_literals.py` is NOT under `tests/verification/rung4`,
       so no count from that directory can speak for it
```

The guard that reads that file is not in rung 4 -- it is `tests/test_no_tolerance_literals.py`
-- and I had run it earlier, against the version WITH R682, where the literals did not
exist because R682's own edits were in the file. The revert changed the file and I
re-measured only the directory I had been watching. "I ran the tests" is not a
measurement of the tests I did not run.

# Revision 2 — EQ3's DQ4 and DQ5, R685 closed, DQ8 per body, and R704/R705

Answers: verdict 101 @ 4b8f079

**2026-10-06.**

## 0. CI at `e76f165`, the commit verdict 101 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 101 at `e76f165` through the report's own `Answers:` line. Run `37566586915`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1977 | 0 | 0 |
| lint, unit and guards | 992 | 135 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 135.**

- `tests/test_report_carried.py::test_the_report_carries_the_finding[R686]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R687]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R688]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R689]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R690]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R691]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R692]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R693]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R694]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R695]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R696]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R697]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R698]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R699]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R700]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R701]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R702]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R703]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-floatfea/io/integrator.py:27]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-floatsim/solver/newmark.py:222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-integrator.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-scripts/export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-scripts/report_joint_reactions.py:77]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/test_no_tolerance_literals.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1016]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1017]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1018]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1019]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1020]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1021]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1022]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1023]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1024]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1025]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1026]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1027]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1028]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1029]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1030]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1031]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1032]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1033]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1034]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1035]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1036]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1037]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1038]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1039]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1040]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1041]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1042]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1043]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1044]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1045]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1046]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1037]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1038]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1039]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1040]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1041]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1042]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1043]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1044]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1045]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1046]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-docs/load-interchange-v1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-docs/reports/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:999]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1000]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1001]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1002]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1003]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1004]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1005]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1006]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1007]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1008]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1009]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1010]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1011]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1012]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1013]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F4.md:5]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-docs/milestones/F4.md:348]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-floatfea/tolerances.py:1990]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-test_f4_static_and_mapping.py:549]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-tests/test_plan_matches_tolerances.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-tests/verification/rung4/test_f4_static_and_mapping.py:549]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R694-floatfea/model/platform.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R695-tests/verification/rung4/test_f4_static_and_mapping.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-docs/milestones/F4.md:473]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1974]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1975]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:10]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:12]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:13]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:95]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:526]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:527]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:555]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:556]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-scratchpad/er1b_runs.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-scripts/export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2115]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2118]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 101 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 101 at `e76f165` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37566586915` | push | `e76f165` | conclusion **failure** |
| `37570352720` | push | `36a5003` | **no result** (`cancelled`) |
| `37570657425` | push | `b68f2f7` | conclusion **failure** |

**Run `37566586915`, conclusion **failure**: 135 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R686]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R687]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R688]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R689]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R690]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R691]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R692]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R693]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R694]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R695]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R696]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R697]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R698]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R699]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R700]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R701]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R702]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R703]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-floatfea/io/integrator.py:27]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-floatsim/solver/newmark.py:222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-integrator.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-scripts/export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-scripts/report_joint_reactions.py:77]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/test_no_tolerance_literals.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1016]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1017]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1018]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1019]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1020]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1021]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1022]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1023]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1024]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1025]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1026]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1027]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1028]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1029]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1030]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1031]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1032]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1033]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1034]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1035]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1036]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1037]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1038]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1039]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1040]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1041]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1042]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1043]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1044]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1045]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1046]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1037]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1038]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1039]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1040]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1041]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1042]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1043]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1044]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1045]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1046]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-docs/load-interchange-v1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-docs/reports/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:999]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1000]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1001]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1002]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1003]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1004]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1005]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1006]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1007]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1008]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1009]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1010]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1011]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1012]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1013]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F4.md:5]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-docs/milestones/F4.md:348]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-floatfea/tolerances.py:1990]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-test_f4_static_and_mapping.py:549]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-tests/test_plan_matches_tolerances.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-tests/verification/rung4/test_f4_static_and_mapping.py:549]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R694-floatfea/model/platform.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R695-tests/verification/rung4/test_f4_static_and_mapping.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-docs/milestones/F4.md:473]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1974]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1975]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:10]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:12]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:13]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:95]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:526]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:527]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:555]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:556]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-scratchpad/er1b_runs.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-scripts/export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2115]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2118]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `37570657425`, conclusion **failure**: 184 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R686]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R687]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R688]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R689]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R690]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R691]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R692]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R693]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R694]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R695]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R696]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R697]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R698]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R699]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R700]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R701]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R702]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R703]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R704]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R705]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-floatfea/io/integrator.py:27]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-floatsim/solver/newmark.py:222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-integrator.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-scripts/export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-scripts/report_joint_reactions.py:77]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/test_no_tolerance_literals.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1016]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1017]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1018]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1019]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1020]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1021]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1022]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1023]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1024]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1025]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1026]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1027]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1028]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1029]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1030]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1031]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1032]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1033]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1034]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1035]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1036]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1037]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1038]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1039]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1040]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1041]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1042]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1043]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1044]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1045]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1046]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1037]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1038]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1039]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1040]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1041]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1042]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1043]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1044]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1045]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1046]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-docs/load-interchange-v1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-docs/reports/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:999]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1000]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1001]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1002]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1003]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1004]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1005]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1006]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1007]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1008]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1009]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1010]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1011]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1012]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1013]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R689-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F4.md:5]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-docs/SUPERVISOR.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-docs/milestones/F4.md:348]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-floatfea/tolerances.py:1990]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-test_f4_static_and_mapping.py:549]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-tests/test_plan_matches_tolerances.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R691-tests/verification/rung4/test_f4_static_and_mapping.py:549]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R694-floatfea/model/platform.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R694-floatfea/tolerances.py:2027]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R695-floatfea/tolerances.py:1979]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R695-tests/verification/rung4/test_f4_static_and_mapping.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R696-floatfea/tolerances.py:1942]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1974]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1975]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R698-floatfea/tolerances.py:1960]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R698-floatfea/tolerances.py:1961]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R698-floatfea/tolerances.py:1962]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:10]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:12]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:13]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:95]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:526]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:527]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:555]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:556]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-scratchpad/er1b_runs.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-scripts/export_platform_deck.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R700-scripts/report_joint_reactions.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:200]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:201]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:202]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:203]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:204]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:205]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:206]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R702-docs/reports/F4/preview-PRELIMINARY.md:208]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R702-docs/reports/F4/preview-PRELIMINARY.md:209]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R702-docs/reports/F4/preview-PRELIMINARY.md:210]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2107]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2108]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2110]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2111]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2112]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2113]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2114]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2115]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2117]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2118]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R704-floatfea/model/platform.py:116]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R704-floatfea/tolerances.py:1988]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R704-floatfea/tolerances.py:1989]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R704-tests/verification/rung4/test_f4_static_and_mapping.py:355]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-docs/milestones/F4.md:72]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2239]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2240]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2241]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2242]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2243]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2244]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2245]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2246]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2247]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2248]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2249]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2250]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2251]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2252]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2253]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2254]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2255]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2256]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2257]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-tests/verification/rung4/test_f4_static_and_mapping.py:1511]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-tests/verification/rung4/test_f4_static_and_mapping.py:1512]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R705-tests/verification/rung4/test_f4_static_and_mapping.py:1515]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0b. The reds at this commit are EG3 state (2), traced by name (EG3(i))

**Verdict written, answering report not yet** — which is this revision. CI's own
decomposition at `e76f165`, from the run's log rather than from my laptop:

```
claim  every red at the reviewed commit is in the two report-guard files
cmd    python scripts/ci_section.py   (the 135 names it lists, grouped by test id)
out    107  test_every_named_site_is_touched_or_declared
out     18  test_the_report_carries_the_finding
out      7  test_the_guard_survives_the_state
out      1  test_the_generator_would_catch_a_row_under_the_wrong_number
out      1  test_the_Carried_table_is_what_the_generator_produces
out      1  test_the_CI_section_is_about_the_REVIEWED_commit
out    107 + 18 + 7 + 1 + 1 + 1 = 135, the whole count
judge  five of the six ids are EG3 state (2)'s own list (EH1); the seventh test's seven
       parametrisations are the cascade off a red baseline, identified by their own
       failure lines and not by their names. State (2) is cleared BY THIS REPORT and not
       by time.
```

**And C7 is right that my `136`/`108` was wrong for that commit — the reason is CZ1's own
reusable half.** I published `136 failed` and `108` of the site guard from a run on my
WORKING TREE; CI at `e76f165` reads `135` and `107`.

```
cell   ONE VARIABLE: whether the tree under test is a commit. Same suite, same machine.
out    working tree, DQ4/DQ5 not yet committed : 136 failed, 3056 passed  (108 sites)
out    CI at e76f165, the commit itself        : 135 failed              (107 sites)
judge  `test_every_named_site_is_touched_or_declared` asks, per site, whether a commit
       TOUCHED it. Its answer is a function of the commit graph, so on an uncommitted
       tree one site reads differently -- and that is exactly CZ1's sentence: "a check
       whose input is the commit itself cannot be measured before the commit exists".
       I knew the rule and applied it to lint and the report guards, and then took a
       count of the report guards from a tree that was not a commit.
```

## 1. The schedule, and it holds

**Step 2's date is 14 October and it holds.** Verdict 101 was an ES0 interim check and
counts against no round, so verdict 97 remains round 1 of three and **this revision is
round 2, with one revision remaining.** EQ3's four gate rows are shipped — DQ4(i),
DQ4(ii), DQ5 and the per-body half of G4.1's quantity — and two of EQ3's items are not:
**G4.1's dynamic gate and G4.5's `dt`/`dt/2` measurement**, which wait on the six FloatSim
runs and now also on a plan decision about DQ8's quantity (section 8). That is reported
the day it is known, which is today, and it is a scope question rather than a slip: if the
plan decision lands this week both fit inside step 3 without moving 14 October. **No step
has yet closed carrying a blocking item, so DZ7c does not fire.** R704 and R705 were
answered the same day they were raised.

## 2. R704 — and R694's second entry, which is the half I left

R694's `Closed when` named two entries. I repaired one, reported both, and the reviewer
measured the other still frozen. **This is the sixth appearance of that shape in this
milestone** and the first on a gate rather than a sentence.

```
claim  the frozen `0.375` equality FALSE-REDDENS at five of six non-vacuous rungs
cmd    python scratchpad/verify_r704_r705.py
out         f               shortfall       f/2  closed form  old 0.375   floor
out      0.75     0.37500000000000006     0.375         PASS       PASS    PASS
out       0.5     0.25000000000000017      0.25         PASS       FAIL    PASS
out       0.4      0.2000000000000001       0.2         PASS       FAIL    PASS
out       0.3     0.15000000000000022      0.15         PASS       FAIL    PASS
out       0.2     0.10000000000000019       0.1         PASS       FAIL    PASS
out       0.1      0.0500000000000004      0.05         PASS       FAIL    PASS
out       0.0   6.075906704932774e-16       0.0  VACUOUS, skipped
rule   the counter-case must hold at every rung the ladder descends to
judge  every one of those rungs is `admissible`, so none is unreachable. This is the R680
       shape and not the R682 one: the gate does not let a defect through, it reddens on
       correct code. My six figures reproduce the reviewer's to the digit.
```

```
claim  the repair is the closed form at the body's own `f`, in `_defect_tip_ratio`'s shape
cmd    grep -n "expected_shortfall = platform.mass_fraction" tests/verification/rung4/test_f4_static_and_mapping.py
out    375:    expected_shortfall = platform.mass_fraction / 2.0
rule   the shortfall is `f/2` -- the omitted load is the member's whole weight and half
       lands at each node, which is statics and not this code (EA4)
judge  `f` is read from the body, so no rung can invalidate it, and the constant is
       demoted to a floor: `F4_STATIC_REACTION_AGREEMENT_COUNTER` moves `0.375` -> `0.04`,
       below the smallest non-vacuous defect `0.05`, margin `1.2500x`. EH4's weakening
       side: the defect may shrink to `0.8000` of its size before the floor stops
       bracketing it. At `f = 0` there is no omitted load, so the case SKIPS with the
       reason named rather than passing vacuously.
```

**What I am taking from the sixth repetition, since the reviewer said it would not accept
a seventh.** The failure is not inattention to the condition — I read it — it is that I
checked the site I had just edited and treated the edit as the evidence. The command that
would have caught all six is the same one: a `grep` for every occurrence of the thing
being fixed, run **after** the fix, pasted. EU4 says exactly that, and R705 below is where
I actually did it.

## 3. R705 — a gate that could not fail on a sign, and all three of its named sites

```
claim  three sign mutants, magnitudes exactly preserved, read the CLEAN value
cmd    python scratchpad/verify_r704_r705.py
out      none (clean)                     force 2.4835e-16  moment 5.9605e-16
out      node A rotational rows flipped   force 2.4835e-16  moment 2.0000e+00  CAUGHT
out      node B rotational rows flipped   force 2.4835e-16  moment 2.0000e+00  CAUGHT
out      both ends flipped                force 2.4835e-16  moment 2.0000e+00  CAUGHT
rule   `F4_DQ4_ELEMENT_VECTOR` = 1.0e-12
judge  `2.0` is the exact algebra of comparing `-x` with `+x`, and the FORCE channel stays
       at round-off because the injection moves no magnitude. Under the shipped
       `abs(abs(f[ra]) - want_m)` all three read the clean value to every digit.
```

The signs are **measured, not fitted**, which matters because a sign chosen to make a
mutant red is the defect wearing the repair's clothes:

```
claim  the element's convention is `('xy', +1, -1)` and `('xz', -1, +1)`, on every element
cmd    python scratchpad/r704_r705.py
out    the distinct (plane, sign_A, sign_B) patterns over EVERY element:
out    [('xy', 1, -1), ('xz', -1, 1)]
judge  that is the `flip = diag([1, -1, 1, -1])` `local_mass` applies to the xz plane and
       documents. Taken from the textbook form `(L^2/12) e1 x w` and checked against the
       element, not read off the element and written down as the expectation.
```

**All three sites the condition named, closed site by site, with the grep pasted (EU4).**

```
rule   R705's `Closed when` named three things: the assertion at :1511-1515, the
       antisymmetry `f[ra] == -f[rb]` as an alternative, and the docstring sentence at
       :1426-1431. Half of an item is not the item.
```

```
claim  `abs(abs(` survives three times and EVERY ONE IS PROSE quoting the withdrawn form
cmd    grep -n "abs(abs(" tests/verification/rung4/test_f4_static_and_mapping.py
out    1474:    took `abs(abs(f[ra]) - want_m)` and read the clean value to every digit under the
out    1544:FAIL ON ONE. `abs(abs(f[ra]) - want_m)` discards exactly the sign `docs/milestones/F4.md`
out    1709:    error of comparing `-x` with `+x`. Under the `abs(abs(f[ra]) - want_m)` this gate
judge  I first wrote `out  (no output)` here FROM THE EXPECTATION, and the command prints
       three lines. All three are inside docstrings describing what the gate used to do,
       which is why the count is 3 and not 0 -- but "no output" was not what the command
       said, and I pasted it before running it. That is the BF0 shape, inside the section
       that is about the BF0 shape, caught by running the command I had already written
       down.
cmd    grep -n "Had the convention disagreed" tests/verification/rung4/test_f4_static_and_mapping.py
out    (no output -- this one I ran; `grep -c` returns 0)
cmd    grep -n "sign_a \* want_m\|sign_b \* want_m" tests/verification/rung4/test_f4_static_and_mapping.py
out    1591:                abs(f[ra] - sign_a * want_m) / want_m,
out    1592:                abs(f[rb] - sign_b * want_m) / want_m,
judge  the SIGNED comparison is the only one in the code path; the three prose mentions
       describe the form it replaced. Three sites named, three sites closed, and the third
       was a separate commit (`b68f2f7`) rather than a line I claimed the first covered.
```

**And the sign flip SHIPS as a counter-case, which is more than the condition asked for
and is the part that matters.** An assertion with no counter-case is an assertion anything
may quietly undo:

```
cell   ONE VARIABLE: the two signed lines reverted to `abs(abs(f[ra]) - want_m)`
cmd    python scratchpad/verify_r705_docstring.py
out    with the `abs` restored : 1 failed, 99 passed in 0.99s
out      FAILED ...::test_DQ4_ii_the_closed_form_gate_REDDENS[moment_sign_flipped]
out    restored                : 100 passed in 0.84s
judge  that row and nothing else, read from the FAILED list rather than counted from the
       total. Before this commit the same reversion left the whole file green -- R683's
       lesson: the injection that distinguishes two forms of a rule is the one that holds
       the rule.
```

**I also corrected an overstatement of my own inside the repair (CP2).** My first wording
said the node-A flip "leaves every per-node figure unmoved". It does not:

```
claim  the flip MOVES DQ4(i)'s per-node figure and stays at round-off
cmd    python scratchpad/verify_r705_docstring.py
out    clean            worst per-node  2.796036563614433e-15  NOT CAUGHT
out    node A flipped   worst per-node  3.140164140674671e-15  NOT CAUGHT
rule   `F4_DQ4_RIGID_VECTOR` = 1.0e-12
judge  it moves by 12% and both values are four orders inside the ceiling. "Unmoved" was
       the wrong word; the docstring now carries both figures instead of the adjective.
       The star geometry summing the centre-node moments to zero is why the response is
       round-off rather than nothing at all — the reviewer's mechanism, my measurement.
```

## 4. R685 — closed, and it was wider than the finding said

The reviewer reproduced every replacement figure independently and closed it. What I
record here is the part that was mine to learn:

```
claim  the entry published four figures measured against the rule R679 DELETED
cmd    git show da7c25b~1:floatfea/tolerances.py | grep -n "1.8726e-16\|5341x\|0.2437\|0.9202"
out    2179:# 0.24374825705420716.
out    2181:# Reason for 1e-12: the measured clean value is 1.8726e-16. It is not exactly zero and
out    2184:# form. 1e-12 is 5341x above the measurement.
out    2190:# MEASURES 0.24374825705420716. The other injection -- one side of a hub-platform joint
out    2191:# losing its sign flip -- reads 0.9202048893902944, so the wrong-node defect is the
out    -- FIVE lines, not the six I first listed: `2178`, which carries the
out       `5.2050529737194385e-17` force figure, is matched by NO needle in this command.
out       Four needles, five lines; the sixth row was a figure I knew was there and the
out       command does not find.
rule   BP0: when a decision rule changes, every figure citing the old rule is regenerated
       or withdrawn IN THE SAME COMMIT
judge  R679 changed the quantity from a sum over five bodies to a `max` over five. Both
       are "the mapping error" and they are not the same number.
```

**How I found it is the transferable part.** I opened that entry intending to append one
paragraph recording a ladder-wide re-measurement. The paragraph existed in my head as
text; the anchor I patched against **did not exist in the file**, and the patch raised. Had
it matched approximately I would have appended a correct paragraph above four wrong
figures. EQ2's sentence — "a claim that a test exists is pasted from grep or pytest
output, never from memory" — applies to a claim that a *paragraph* exists too.

The replacements, every one reproduced by the reviewer independently to the last digit:

```
claim  the per-body figures the entry now carries
cmd    python scratchpad/r685_measure.py && python scratchpad/r685_split.py
out    worst clean over the five bodies : 2.1962235947826024e-16   (hub1)
out    platform clean                   : 0.0   exactly
out    ceiling 1.0e-12 above it by      : 4553.3x
out    wrong node: force 0.0 exactly, moment 0.9597085787263796
out    sign not flipped                 : 3.5569621874567385
out    internal joint dropped           : 1.7784810937283693
out    smallest injection               : 0.9597085787263796
out    counter 0.2, margin              : 4.7985x
out    counter / ceiling                : 2.000e+11x  -- ELEVEN decades, not twelve
out    every figure BIT-IDENTICAL across all seven rungs: True
rule   `F4_MAPPING_CONSERVATION` = 1.0e-12, `_COUNTER` = 0.2
judge  the entry said "Twelve decades above the ceiling" and 0.2/1e-12 is 2e+11. The
       symmetry counter's identical sentence IS right at 1.3/1e-12; this one was copied
       to a value four decades smaller and never re-taken.
```

```
claim  the gate and its counter-case measure the SAME quantity, which I checked rather
       than assumed
cmd    grep -n "def _mapping_error" -A 7 tests/verification/rung4/test_f4_static_and_mapping.py
out    return max(_body_errors(built, loads, want).values())
judge  had they differed, the counter would have been bracketing a quantity no gate
       asserts -- a (c) finding wearing a green suite.
```

## 5. R695, R696 and R698 — closed, and R695's closure was mechanical

All three were answered in `30e4395`, which verdict 101 read for the first time. Recorded
here because the reviewer's method on R695 is the one I should have used on R704:

```
claim  every live injector citation in `tolerances.py` resolves to a real test
cmd    grep -nE "Injected by|injections are run by" floatfea/tolerances.py | grep -oE "test_[A-Za-z0-9_]+" | sort -u
out    test_DQ4_i_the_PER_NODE_gate_REDDENS
out    test_DQ4_ii_the_closed_form_gate_REDDENS
out    test_DQ5_the_free_fall_gate_REDDENS
out    test_EB6_a_PERMUTED_export_reddens_the_gate
out    test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula
out    test_G4_the_defective_formula_misses_the_reaction_by_f_over_two
out    test_R653_a_COEFFICIENT_WRONG_IN_THE_LAST_PRINTED_PLACE_reddens_the_gate
judge  seven citations, seven resolve, zero phantoms. The reviewer swept the WHOLE file
       rather than reading the one line R695 named -- which is the difference between
       closing a finding and closing its example.
```

R696's and R698's figures, which the reviewer measured rather than read:

```
claim  the ceiling entry's live sentences are on the new basis, and the equality's
       justification is the window and not exact arithmetic
cmd    (reviewer's run, reproduced: the support-reaction magnitudes and the four arms'
       spread at the shipped basis)
out    support reaction magnitudes : 6.13e+06 to 6.95e+06 N
out    exact                       : 6131249.999999998 .. 6948750.0000000065
out    the shortfall sentence      : 37.5000%
out    the four arms' spread       : 4.4e-16
rule   `F4_STATIC_REACTION_AGREEMENT` = 1e-12, so the window is 1e-12 against a spread
       of 4.4e-16
judge  the old figures survive only where labelled as old, or where correct for the
       corner they describe. R698 is a BG0 failure inside a tolerance comment -- value
       and form right, cause unmeasured -- which is where I least expected to find one.
```

## 6. R682 and R691 — both closed, at the fifth-missed site

R682's value half closed with `_defect_tip_ratio`. R691 closed at the site I had missed
five times, and the repair is the generalisable part:

```
claim  the fifth-missed site now carries the closed form rather than a basis-specific pair
cmd    grep -n "12-5f\|12-5a\|12f/17" tests/verification/rung4/test_f4_static_and_mapping.py
out    600:  "the DEFECTIVE root moment this ratio uses is `f/(12-5f)` on a platform "
out    601:  "arm -- 1/11 at ER0's f = 0.75 -- and `a/(12-5a)` with `a = 12f/17` on a "
out    620:  `a = 12f/17` on a hub arm: a hub's three arms carry `f` of the hub mass, but
out    656:  # `a / (12 - 5a)` with `a = f` on a platform arm and `a = 12f/17` on a hub arm
out    678:  "`a/(12-5a)` with `a = f` on a platform arm and `a = 12f/17` on a hub "
rule   a repair survives the NEXT change of basis, not just this one
judge  THE LINES ARE NOT :553-558 ANY MORE, and that is worth pasting rather than
       repeating the verdict's numbers. :553-558 is where they sat at `e76f165`, the
       commit the reviewer read; R704, R705 and the DQ4/DQ5 block pushed them to
       600-678. A line range quoted from a verdict is stale the moment the file moves,
       which is why the grep is the citation and the range is not.
judge2 the old text named a basis-specific pair, so every basis change stranded it again
       -- which is why it was missed five times rather than once.
```

## 7. EQ3 — DQ4(i), DQ4(ii) and DQ5, with the six declarations accepted

The reviewer accepted all six values and forms and ran EU1's adversarial case on them.

```
claim  the four quantities, their worst clean values and their counters
cmd    python scratchpad/dq4_dq5_measure.py && python scratchpad/dq4_dq5_counters.py
out    DQ4(ii)            worst clean 1.9371509552001953e-15   ceiling clear 516.2x
out    DQ4(i) per node    worst clean 2.796036563614433e-15    ceiling clear 357.6x
out    DQ4(i) rotations   worst clean 1.2417634328206378e-16
out    DQ5                worst clean 1.3335849658769691e-15   ceiling clear 749.9x
out    counters: 5.0e-4 vs 1.0e-3 (margin 2.0000x) twice; 4.0e-4 vs 8.33e-4 (2.0833x)
rule   each ceiling is a round-off ceiling over every non-vacuous rung of the ladder
```

The table is that run, one row per gate:

| gate | quantity | worst clean | ceiling clear | counter |
|---|---|---|---|---|
| DQ4(ii) | `M_e a` against `mu L/2`, `+-mu L^2/12` | `1.9371509552001953e-15` | `516.2x` | `5.0e-4` vs `1.0e-3`, margin `2.0000x` |
| DQ4(i) per node | `M a` against the closed-form construction | `2.796036563614433e-15` | `357.6x` | `5.0e-4` vs `1.0e-3`, margin `2.0000x` |
| DQ4(i) rotations | `R^T M R a` against the deck's 6x6 | `1.2417634328206378e-16` | — | — |
| DQ5 | `a = g`, `alpha = 0`, member forces zero | section 7a — **the published figure is short** | `749.9x` as published, `745.5x` corrected (C2) | `4.0e-4` vs `8.33e-4`, margin `2.0833x` |

**DQ4(i)'s rotational half is a restatement of the rung-3 mass-property gate, and the
gate says so.** The reviewer measured it as *narrower* than I claimed:

```
claim  the rotational half reaches nine of the ten entries G3.1a B compares, not ten
cmd    (reviewer's run: a 100% deck_mass error against the rotational columns)
out    deck_mass scaled x2 : the rotational half stays GREEN
rule   the rigid 6x6 about the CoG has ten independent entries: mass, three CoG
       couplings, six of J
judge  the expected rotational columns are the skew first moment and `J_G alpha`, and
       NEITHER contains the mass -- so a mass error is invisible to this half and it is
       a strict subset of G3.1a B rather than an equal. I over-stated the gate and
       thereby under-stated my own finding. It ships because the locked plan's row asks
       for it, labelled.
```

**The expected side is orientation-free, and that is what makes it independent.**
`M_A = (L^2/12) e1 x w`: the cross product annihilates the axial component on its own, so
`rotation_matrix`, the roll angle, the orientation node, `local_mass` and `M` are all off
that path. The reviewer checked it attribute by attribute and confirmed it.

**NOT COVERED, recorded because DQ5's row instructs it:** rotational fields have no
per-node expected side. A rigid angular acceleration is position-dependent and I could not
write a consistent nodal form for it independent of the element code. Rotations are
covered at the resultant level only.

## 7a. DQ5's rung dependence — the figure EU1 saved, and the one it did not

```
claim  DQ5's clean value RISES as `f` falls, so the shipped rung is not its worst case
cmd    python scratchpad/dq4_dq5_counters.py
out       f    DQ5 clean
out    0.75    3.780e-16
out     0.5    3.795e-16
out     0.4    4.218e-16
out     0.3    4.887e-16
out     0.2    7.171e-16
out     0.1    1.334e-15
rule   the ceiling is a round-off ceiling over every rung the ladder descends to
judge  a 3.53x spread. Measured at the shipped rung alone the entry would have published
       `2645.8x` of headroom where the ladder-wide figure is `749.9x`. Nothing in the diff
       pointed at `f = 0.1`; it is the configuration nobody chose, which is EU1's own
       first phrase.
```

**And C2 is right that the figure is still short.**

```
claim  the true worst clean is on a direction my sweep did not cover
cmd    (reviewer's run: all three directions, where mine covered minus_z and x)
out    worst clean : 1.3414143963362381e-15   on platform / y / moment
out    ceiling clear : 745.5x, where I published 749.9x
rule   `F4_DQ5_FREE_FALL` = 1.0e-12
judge  the GATE reads every direction and is unaffected; the published number was taken
       from a sweep narrower than the thing it described. Same error as the rung one, one
       axis further in -- which is why it is a closure item and not a defect.
```

**The causal claim I attached to the rung spread is NOT measured and I am withdrawing it
rather than defending it.** I wrote that the rise is conditioning — less member mass, more
lumped remainder. Under BG0 that needs one variable moved with everything else held, and I
did not isolate it. The measurement stands; the explanation does not.

## 8. DQ8's residual per body — and why no tolerance is declared on it

```
claim  the function the plan names returned ONE number for all seventeen bodies
cmd    git show e76f165~1:scripts/report_joint_reactions.py | grep -n "worst_discrete = max"
out    281:        worst_discrete = max(worst_discrete, float(np.max(np.abs(resid))))
rule   DQ8: "G4.1 is per body and per case, never aggregated"
judge  the R679 shape again. `docs/milestones/F4.md:398` names this function as the one
       that forms the quantity, and the quantity it formed is the one the plan forbids.
       EJ4's `3.96e-06` was measured from that key, so it is withdrawn as a per-body
       reference by name rather than re-based underneath it (BP0); the aggregate key is
       kept so the published figure still has the thing it described.
```

```
claim  the per-body breakdown runs, and the `rel` column is entirely the moment channel
cmd    python scripts/report_joint_reactions.py --period 10.0 --duration 40.0
out    body             worst N    reaction N          rel    force rel   moment rel
out    platform      3.3284e-09    1.1923e+00   2.7915e-09   2.7353e-16   2.7915e-09
out    hub1          1.5733e-10    1.3756e+00   1.1437e-10   2.8247e-16   1.1437e-10
out    hub2          5.9092e-10    1.4306e+00   4.1304e-10   2.3281e-16   4.1304e-10
out    hub3          1.6255e-10    1.4857e+00   1.0941e-10   2.6155e-16   1.0941e-10
out    hub4          5.9092e-10    1.4306e+00   4.1304e-10   2.3281e-16   4.1304e-10
out    force rel  : 2.3281e-16 to 1.0012e-14   over seventeen bodies
out    moment rel : 1.0941e-10 to 2.7915e-09
out    rel        : identical to moment rel on all seventeen
judge  the aggregate for this case is `3.328367e-09 N`, which happens to BE the platform's
       own worst, so here it hid nothing -- and it still names no body, and the reaction
       scales range `5.2845e-01` to `1.5061e+00`, so the relative ordering is not the
       absolute ordering.
```

**The dimensional point, and the reviewer's correction to it, which makes the refusal more
right rather than less.** I argued that `max |Sum reactions|` is a force scale, so dividing
a moment residual by it yields a quantity with units of length and not a ratio. The
reviewer split the scale and found my premise wrong on **6 of 17 bodies**: on
`buoy1/2/3/7/8/9` the moment rows dominate the reaction vector, so there it is `force_rel`
that carries the dimension and `moment_rel` that is dimensionless. My sentence "`force rel`
IS dimensionless on all seventeen" is **false on six**.

So the position is stronger than I put it: **which channel is dimensionless depends on
which component happens to be larger at that body in that window.** A tolerance on DQ8's
scalar would be a tolerance on a quantity whose units change per body and per case.
**Declining to declare is the correct refusal**, and the reviewer ruled it not a blocking
omission. Both forms are reported — `<body>_rel` as DQ8 words it, plus `<body>_force_rel`
and `<body>_moment_rel` — so the choice can be made against numbers. **C1 is answered
before the G4.1-dynamic quantity is chosen**, per the verdict, because that choice is (c)
and C1 is its input.

A body with no reaction scale gets **no** relative key rather than a guarded one:

```
rule   C158's finding: a `max(..., 1.0)` floor inside a gate is a tolerance under another
       name, so a body whose reactions vanish over the window is a case with its own
       right answer -- the residual must be zero ABSOLUTELY -- and gets the absolute key
       with no sentinel a gate could compare against
out    on this case the branch was NOT taken: 17 of 17 bodies had a scale
```

C5 records that the per-body label map is validated by count only, which is a real gap and
is on the corpus list for the batch that resumes at the end of October.

## 9. The two rulings I asked for, and what I take from them

Both went my way and both came back sharper than I sent them, which is the useful part.

```
out    ruling 1  DQ4(i)'s resultant half: I claimed ten entries, it reaches nine. A
out              100% deck_mass error leaves it green.
out    ruling 2  DQ8's normalisation: right in kind, premise wrong on 6 of 17 bodies,
out              and the conclusion strengthened rather than weakened.
judge  in both I reasoned correctly to a conclusion and got a COUNT wrong inside it, and
       in both the count was something I could have measured and did not.
```

In both cases I reasoned correctly to a conclusion and got a *count* wrong inside it, and
in both cases the count was something I could have measured and did not. The pattern is
the same as R704's: the argument gets the attention and the enumeration does not.

## 10. Closure items — C1 to C7, and R697 with R699 to R703

Per CZ0 these are fixed **once, in the step's closure commit**, are not re-reviewed item by
item, and the step is not held on one.

```
claim  the list is the verdict's own, seven items, read off its Closure items section
cmd    (the verdict's `## Closure items` block, C1 to C7)
out    C1 dimensional direction  C2 DQ5 worst clean  C3 the :971 figure
out    C4 the oblique field      C5 the label map    C6 R697/R699-R703 carried
out    C7 the 135/107 count
```

Listed here so the list is in the report rather than only in the verdict:

| item | what it is | where |
|---|---|---|
| C1 | `scripts/report_joint_reactions.py:238` has the dimensional direction backwards — `N·m/N` is **length** — and both it and the commit message are incomplete per the 11-of-17 measurement | **answered before the G4.1-dynamic quantity is chosen** |
| C2 | `F4_DQ5_FREE_FALL`'s worst clean is `1.3414143963362381e-15` on `platform/y/moment` (`745.5x`), not `1.3335849658769691e-15` (`749.9x`) | section 7a |
| C3 | `:971`'s `2.092543e-16` is `hub3`'s clean round-off, not the injected body's | closure commit |
| C4 | the oblique field adds no discrimination — both sides are exactly linear in `field` | closure commit |
| C5 | the per-body label map is validated by count only | closure commit; corpus 28 Oct |
| C6 | R697 and R699–R703 carried unchanged, not re-adjudicated | this section |
| C7 | my `136`/`108` is `135`/`107` | section 0b |

**R697, R699, R700, R701, R702 and R703** are the previous round's closure items, carried
unchanged per that verdict's own instruction and C6 of this one — named individually
rather than as a range, because a range is not a list and the row that points here has to
find its own number. R697 is the f/2 mechanism being false of 12 of the 16 members; R699
is the BP0 sweep's five further f/M-dependent figures; R700 is the replay driver shipping
with the override off; R701 and R702 are the two preview figures true of less than they
claimed; R703 is the symmetry entry's lost injection-side edge. The reviewer spot-checked
R697 and reports it still open. All six go into the closure commit's single list with
C1–C7.

## 11. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R653 | **answered** — revision 1 | R682, R683, R684, R685, R653 and |
| R679 | **answered** — step 1 closure | 's remainder (R683 IS that remainder, so five distinct) -- plus C161 to C166 and the |
| R682 | **answered** — §6 | R682, R683, R684, R685, R653 and |
| R683 | **answered** — revision 1 | R682, R683, R684, R685, R653 and |
| R684 | **answered** — revision 1 | R682, R683, R684, R685, R653 and |
| R685 | **answered** — §4 | R682, R683, R684, R685, R653 and |
| R686 | **answered** — verdict 98 | test_R653_the_value_the_DRIVER_reconstructs_with_is_the_declared_one CANNOT FAIL ON THE... |
| R687 | **answered** — verdict 98 | THE RANGE ASSERTION CLAIMS A PROPERTY GENERALIZED-ALPHA DOES NOT HAVE, AND THAT FALSE SENTENCE... |
| R688 | **answered** — verdict 98 | round(x, 5) == published IS A COMPARISON EPSILON, THE TEST AND THE REPORT BOTH CALL IT EXACT,... |
| R689 | **answered** — verdict 99, as R692 | THE PRODUCTION MAPPING GATE READS 0.000e+00 ON A ROW IT COMPARES NOTHING IN, AND PASSES ON AN... |
| R690 | **answered** — verdict 99 | to (d), and I say so rather than dressing it as more.) ER0, ER1, ER2, EQ2, EQ3 AND EQ4 EXIST... |
| R691 | **answered** — §6 | R682's FALSE ARITHMETIC IS DELETED FROM tolerances.py AND LEFT STANDING IN THE PLAN ROW THAT IS... |
| R692 | **answered** — verdict 99 | compared > 0 IS R689's CLOSING CONDITION MINUS ITS COUNT. ALL SIXTEEN DEGRADED ROWS STILL READ... |
| R693 | **answered** — verdict 99 | THE NEW COUNTER'S BRACKET IS PUBLISHED AS 2x AND MEASURES 1.0857x, AND THE SENTENCE SAYING NO... |
| R694 | **answered** — §2 | F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05 AND F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.375... |
| R695 | **answered** — §5 | floatfea/tolerances.py:1979 NAMES AN INJECTOR THAT DOES NOT EXIST, and e2fa88a is the commit... |
| R696 | **answered** — §5 | THE CEILING ENTRY BRACKETING THE MOVED COUNTER STILL PUBLISHES THE OLD BASIS.... |
| R697 | **carried** — §10 | THE f/2 MECHANISM IS FALSE OF 12 OF THE 16 MEMBERS. floatfea/tolerances.py:1974-1975 ("The... |
| R698 | **answered** — §5 | THE EQUALITY'S JUSTIFICATION IS REFUTED BY ITS OWN MEASUREMENT.... |
| R699 | **carried** — §10 | THE BP0 SWEEP MISSED FIVE MORE f/M-DEPENDENT FIGURES, AND ONE IS THE SITE R691's CLOSING... |
| R700 | **carried** — §10 | THE REPLAY DRIVER SHIPS WITH THE OVERRIDE OFF, AND ONE SENTENCE CLAIMS OTHERWISE. cmd grep -n... |
| R701 | **carried** — §10 | "Vz does not move with f at all" IS TRUE ONLY OF THE STATION THE TABLE REPORTS.... |
| R702 | **carried** — §10 | "My runs from 1.1200x to 0.8800x" IS THE HUB'S RANGE PUBLISHED AS THE WHOLE RANGE.... |
| R703 | **carried** — §10 | THE SYMMETRY ENTRY LOST ITS INJECTION-SIDE EDGE (EH4). floatfea/tolerances.py:2104-2118. The... |
| R704 | **answered** — §2 | F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.375 IS STILL A FROZEN EQUALITY PINNED TO f = 0.75, AND... |
| R705 | **answered** — §3 | DQ4(ii)'s MOMENT CHANNEL CANNOT FAIL ON A SIGN, AND THE PLAN DECLARES ITS QUANTITY AS... |

## 11a. Every named site this round's diff does not touch, declared by name

The site guard's escape hatch is deliberate and explicit: the report may write
`no change` beside the **exact** site, which is a claim a reviewer can check, rather
than an omission nobody sees. Its own docstring records that five consecutive rounds
closed a site-naming condition at some of its sites and recorded it as answered --
and R704 is the sixth, so this table is not a formality.

```
claim  every site below is named by the verdict and untouched by this round's diff
cmd    python -m pytest tests/test_report_carried.py::test_every_named_site_is_touched_or_declared -q
out    154 sites, before this table existed, across 18 findings
rule   a site is TOUCHED by the diff or DECLARED `no change` beside its exact token
judge  the two findings this round answers are R704 and R705; everything else was
       closed in an earlier round or is a closure item carried by instruction. The
       four rows that matter are the ones where a BRANCH was chosen -- R705's
       `tolerances.py` entry is the branch I did NOT take, and saying so is the
       difference between a choice and an oversight.
```

| finding | site | this round | why |
|---|---|---|---|
| R686 | `HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `floatfea/io/integrator.py:27` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `floatsim/solver/newmark.py:222` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `integrator.py` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `scripts/export_platform_deck.py` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `scripts/report_joint_reactions.py:77` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/test_no_tolerance_literals.py` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1016` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1017` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1018` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1019` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1020` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1021` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1022` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1023` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1024` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1025` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1026` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1027` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1028` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1029` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1030` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1031` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1032` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1033` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1034` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1035` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1036` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1037` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1038` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1039` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1040` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1041` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1042` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1043` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1044` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1045` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1046` | **no change** | closed in an earlier round (verdict 98). This round's diff does not reach it. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1037` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1038` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1039` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1040` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1041` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1042` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1043` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1044` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1045` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1046` | **no change** | closed in an earlier round (verdict 98), on branch A as offered. |
| R688 | `CLAUDE.md` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `docs/load-interchange-v1.md` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1000` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1001` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1002` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1003` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1004` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1005` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1006` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1007` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1008` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1009` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1010` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1011` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1012` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1013` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:999` | **no change** | closed in an earlier round (verdict 98), on the branch it took. |
| R689 | `CLAUDE.md` | **no change** | closed in an earlier round as R692 (verdict 99). |
| R690 | `F3.md` | **no change** | closed in an earlier round (verdict 99). |
| R690 | `docs/milestones/F3.md` | **no change** | closed in an earlier round (verdict 99). |
| R690 | `docs/milestones/F4.md:5` | **no change** | closed in an earlier round (verdict 99). |
| R691 | `CLAUDE.md` | **no change** | closed by the fifth-missed-site repair in `30e4395`, read by verdict 101. |
| R691 | `docs/SUPERVISOR.md` | **no change** | closed by the fifth-missed-site repair in `30e4395`, read by verdict 101. |
| R691 | `docs/milestones/F4.md:348` | **no change** | closed by the fifth-missed-site repair in `30e4395`, read by verdict 101. |
| R691 | `floatfea/tolerances.py:1990` | **no change** | closed by the fifth-missed-site repair in `30e4395`, read by verdict 101. |
| R691 | `test_f4_static_and_mapping.py:549` | **no change** | closed by the fifth-missed-site repair in `30e4395`, read by verdict 101. |
| R691 | `tests/test_plan_matches_tolerances.py` | **no change** | closed by the fifth-missed-site repair in `30e4395`, read by verdict 101. |
| R691 | `tests/verification/rung4/test_f4_static_and_mapping.py:549` | **no change** | closed by the fifth-missed-site repair in `30e4395`, read by verdict 101. |
| R694 | `floatfea/model/platform.py:116` | **no change** | tip-moment half closed in `30e4395`; the reaction half IS R704, section 2. |
| R694 | `floatfea/tolerances.py:2027` | **no change** | tip-moment half closed in `30e4395`; the reaction half IS R704, section 2. |
| R695 | `floatfea/tolerances.py:1979` | **no change** | closed in `30e4395` and verified by the reviewer's whole-file sweep, section 5. |
| R695 | `tests/verification/rung4/test_f4_static_and_mapping.py:315` | **no change** | closed in `30e4395` and verified by the reviewer's whole-file sweep, section 5. |
| R696 | `floatfea/tolerances.py:1942` | **no change** | closed in `30e4395`, section 5. |
| R697 | `floatfea/tolerances.py:1974` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R697 | `floatfea/tolerances.py:1975` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:320` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:321` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:322` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:323` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R698 | `floatfea/tolerances.py:1960` | **no change** | closed in `30e4395`, section 5. |
| R698 | `floatfea/tolerances.py:1961` | **no change** | closed in `30e4395`, section 5. |
| R698 | `floatfea/tolerances.py:1962` | **no change** | closed in `30e4395`, section 5. |
| R699 | `floatfea/post/member_forces.py:10` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R699 | `floatfea/post/member_forces.py:12` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R699 | `floatfea/post/member_forces.py:13` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:526` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:527` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:555` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:556` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:95` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R700 | `export_platform_deck.py` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R700 | `scratchpad/er1b_runs.py` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R700 | `scripts/export_platform_deck.py` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R700 | `scripts/report_joint_reactions.py` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:200` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:201` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:202` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:203` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:204` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:205` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:206` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R702 | `docs/reports/F4/preview-PRELIMINARY.md:208` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R702 | `docs/reports/F4/preview-PRELIMINARY.md:209` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R702 | `docs/reports/F4/preview-PRELIMINARY.md:210` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2104` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2105` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2106` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2107` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2108` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2109` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2110` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2111` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2112` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2113` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2114` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2115` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2116` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2117` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R703 | `floatfea/tolerances.py:2118` | **no change** | closure item, carried unchanged by the verdict's own instruction. Section 10. |
| R704 | `floatfea/model/platform.py:116` | **no change** | cited as what the counter DEPENDS on -- `MASS_FRACTION_LADDER` -- not as a defect to repair. Correct as it stands. |
| R704 | `floatfea/tolerances.py:1988` | **no change** | the verdict cites these two lines as proof the closed form was ALREADY in the tree. The repair reads `f/2` from the body; these lines were right and stay. |
| R704 | `floatfea/tolerances.py:1989` | **no change** | as `:1988` -- the closed form the repair uses, already correct before it. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:355` | **no change** | the block the condition named is REWRITTEN (section 2); this exact line is unchanged context inside the docstring the rewrite inserted, and the answering assertion is now at `:375`. |
| R705 | `docs/milestones/F4.md:72` | **no change** | cited as the AUTHORITY declaring `+-mu L^2/12`, not as a defect. The gate was wrong and the plan was right. |
| R705 | `floatfea/tolerances.py:2239` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2240` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2241` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2242` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2243` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2244` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2245` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2246` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2247` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2248` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2249` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2250` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2251` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2252` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2253` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2254` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2255` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2256` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `floatfea/tolerances.py:2257` | **no change** | the condition's THIRD branch -- state that the sign is out of DQ4(ii)'s scope and name the rung-2 test. I took the FIRST branch instead (the signed comparison plus a counter-case), so this entry is deliberately untouched rather than overlooked. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1511` | **no change** | the assertion is REWRITTEN (section 3); the signed comparison is now at `:1591-1592` and this line is unchanged context. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1512` | **no change** | as `:1511`. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1515` | **no change** | as `:1511`. |

## 12. Tolerances touched

```
claim  TWO values moved and six were declared; none was widened
cmd    git diff fa709df..HEAD -- floatfea/tolerances.py | grep -E "^[-+]F4_"
out    -F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.375
out    +F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.04
out    -F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER: Final[float] = 0.05
out    +F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER: Final[float] = 0.005
out    +F4_DQ4_ELEMENT_VECTOR: Final[float] = 1.0e-12
out    +F4_DQ4_ELEMENT_VECTOR_COUNTER: Final[float] = 5.0e-4
out    +F4_DQ4_RIGID_VECTOR: Final[float] = 1.0e-12
out    +F4_DQ4_RIGID_VECTOR_COUNTER: Final[float] = 5.0e-4
out    +F4_DQ5_FREE_FALL: Final[float] = 1.0e-12
out    +F4_DQ5_FREE_FALL_COUNTER: Final[float] = 4.0e-4
rule   a counter moving DOWN makes the gate demand more of the defect, not less
judge  I WROTE "one value moved" AND THE DIFF SHOWS TWO. The tip-moment counter moved
       0.05 -> 0.005 in `30e4395`, which is inside this range -- the commit verdict 101
       read for the first time, and the one my own invocation scoped out of the range.
       The table below was short a row for the same reason. This is why the section
       carries the diff rather than a count I remembered.
```

| constant | before | after | why |
|---|---|---|---|
| `F4_STATIC_REACTION_AGREEMENT_COUNTER` | `0.375` | `0.04` | **R704.** A frozen equality pinned to `f = 0.75` became the floor beneath every rung; the expected side is now `f/2` at the body's own `f`. Smallest non-vacuous defect `0.05`, margin `1.2500x` |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `0.05` | `0.005` | **R694**, in `30e4395`. The same repair on the other entry R694's condition named: the counter-case compares against the closed form `a/(12-5a)` at each body's own `f` and the constant became the floor beneath every rung. Smallest at any rung with `f > 0` is `0.006060606060606062`, margin `1.2121x` |
| `F4_DQ4_ELEMENT_VECTOR` | — | `1.0e-12` | DQ4(ii), new. Worst clean `1.9371509552001953e-15`, clear `516.2x`; shear-independent over five decades of `phi` |
| `F4_DQ4_ELEMENT_VECTOR_COUNTER` | — | `5.0e-4` | smallest of **three** injections (`1.0e-3`), the third being R705's sign flip at exactly `2.0` |
| `F4_DQ4_RIGID_VECTOR` | — | `1.0e-12` | DQ4(i), new. Worst clean `2.796036563614433e-15`, clear `357.6x` |
| `F4_DQ4_RIGID_VECTOR_COUNTER` | — | `5.0e-4` | smallest of two (`1.0e-3`); the other strengthens as the ladder descends |
| `F4_DQ5_FREE_FALL` | — | `1.0e-12` | DQ5, new. Worst clean at `f = 0.1`, not the shipped rung; `749.9x` as published and `745.5x` corrected (C2) |
| `F4_DQ5_FREE_FALL_COUNTER` | — | `4.0e-4` | smallest of two (`8.33e-4`), and the two redden different channels |

**No other tolerance moved**, and neither move was a widening: `0.375 -> 0.04` and
`0.05 -> 0.005` are both counters moving **down**, which makes each gate demand more of
the defect rather than less.

## 13. Lint, types, and the whole suite

```
claim  lint, formatting and types are green at this commit
cmd    python -m ruff check floatfea tests && python -m black --check floatfea tests
       && python -m mypy floatfea
out    All checks passed!
out    98 files would be left unchanged.
out    Success: no issues found in 36 source files
judge  `pytest` does not run any of the three, which is CZ1's reason for running them
       separately and pasting each.
```

**The reds are EG3 state (2) and section 0b traces every one.** The run below is the
whole suite at this revision's own commit, generated by `scripts/suite_count.py` and run
**after** every other edit to this report (R309): a count taken before an edit is a count
that does not describe what shipped.

**What the two numbers measure, because they do not measure the same tree.** The
generator runs in a clean worktree **at the last commit**, which is `b68f2f7` — a commit
where this revision does not exist.

```
cmd    python scripts/suite_count.py
out    whole suite at b68f2f7 : 2855 passed, 0 failed, 0 skipped
out    the excluded set       : 192 passed, 184 failed, 0 skipped
cmd    python -m pytest tests/test_report_carried.py
       tests/test_report_numbers_are_sourced.py tests/test_tree_prose_consistent.py -q
out    1 failed, 386 passed   (the one was test_the_report_carries_a_WHOLE_SUITE_count,
out                            which this paste answers)
rule   EG3 state (2): a verdict written, its answering report not yet committed
```

So:

* **the first count is the result**: `2855 passed, 0 failed, 0 skipped` over the whole
  suite outside the three files parametrised over this report. Nothing in `floatfea/`,
  `tests/verification/`, `tests/unit/`, `tests/regression/` or any guard outside those
  three is red.
* **the excluded set's 184 failures are EG3 state (2) and nothing else**: a verdict
  written, its answering report not yet committed. Every id below is
  `test_the_report_carries_the_finding`, `test_every_named_site_is_touched_or_declared`,
  `test_the_Carried_table_is_what_the_generator_produces`,
  `test_the_generator_would_catch_a_row_under_the_wrong_number`,
  `test_the_CI_section_is_about_the_REVIEWED_commit`, or the
  `test_the_guard_survives_the_state` cascade off a red baseline — which is EH1's
  corrected state (2) list, plus the cascade identified by the baseline being red.
* **it is cleared BY THIS REVISION's own commit and not by time** (EG3's sharpening). The
  three files are green against this revision in the working tree, measured separately:
  `1 failed, 386 passed` before the suite line existed, and that one was
  `test_the_report_carries_a_WHOLE_SUITE_count`, which this paste answers.

That is the self-reference the generator's exclusion exists for: the report guards cannot
be measured at a commit that does not contain the report, and CZ1's reusable half is the
same sentence — a check whose input is the commit itself cannot be measured before the
commit exists. **The counts at this revision's own commit are pasted in the next
revision's `Carried`** (EG3 condition (ii)).

**Whole suite at `b68f2f7`: 2855 passed, 0 failed, 0 skipped.** **The excluded set: 192 passed, 184 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 376 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R686]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R687]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R688]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R689]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R690]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R691]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R692]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R693]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R694]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R695]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R696]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R697]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R698]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R699]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R700]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R701]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R702]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R703]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R704]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R705]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_Carried_table_is_what_the_generator_produces`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_section_is_about_the_REVIEWED_commit`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-floatfea/io/integrator.py:27]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-floatsim/solver/newmark.py:222]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-integrator.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-scripts/export_platform_deck.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-scripts/report_joint_reactions.py:77]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/test_no_tolerance_literals.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1016]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1017]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1018]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1019]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1020]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1021]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1022]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1023]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1024]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1025]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1026]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1027]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1028]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1029]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1030]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1031]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1032]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1033]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1034]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1035]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1036]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1037]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1038]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1039]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1040]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1041]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1042]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1043]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1044]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1045]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R686-tests/verification/rung4/test_f4_static_and_mapping.py:1046]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1037]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1038]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1039]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1040]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1041]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1042]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1043]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1044]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1045]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R687-tests/verification/rung4/test_f4_static_and_mapping.py:1046]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-CLAUDE.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-docs/load-interchange-v1.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-docs/reports/F4/step-2.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:999]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1000]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1001]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1002]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1003]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1004]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1005]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1006]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1007]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1008]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1009]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1010]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1011]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1012]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R688-tests/verification/rung4/test_f4_static_and_mapping.py:1013]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R689-CLAUDE.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F3.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R690-docs/milestones/F4.md:5]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R691-CLAUDE.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R691-docs/SUPERVISOR.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R691-docs/milestones/F4.md:348]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R691-floatfea/tolerances.py:1990]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R691-test_f4_static_and_mapping.py:549]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R691-tests/test_plan_matches_tolerances.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R691-tests/verification/rung4/test_f4_static_and_mapping.py:549]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R694-floatfea/model/platform.py:116]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R694-floatfea/tolerances.py:2027]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R695-floatfea/tolerances.py:1979]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R695-tests/verification/rung4/test_f4_static_and_mapping.py:315]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R696-floatfea/tolerances.py:1942]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1974]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R697-floatfea/tolerances.py:1975]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:320]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:321]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:322]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R697-tests/verification/rung4/test_f4_static_and_mapping.py:323]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R698-floatfea/tolerances.py:1960]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R698-floatfea/tolerances.py:1961]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R698-floatfea/tolerances.py:1962]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:10]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:12]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-floatfea/post/member_forces.py:13]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:95]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:526]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:527]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:555]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R699-tests/.../rung4/test_f4_static_and_mapping.py:556]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R700-export_platform_deck.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R700-scratchpad/er1b_runs.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R700-scripts/export_platform_deck.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R700-scripts/report_joint_reactions.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:200]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:201]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:202]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:203]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:204]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:205]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R701-docs/reports/F4/preview-PRELIMINARY.md:206]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R702-docs/reports/F4/preview-PRELIMINARY.md:208]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R702-docs/reports/F4/preview-PRELIMINARY.md:209]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R702-docs/reports/F4/preview-PRELIMINARY.md:210]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2104]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2105]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2106]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2107]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2108]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2109]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2110]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2111]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2112]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2113]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2114]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2115]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2116]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2117]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R703-floatfea/tolerances.py:2118]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R704-floatfea/model/platform.py:116]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R704-floatfea/tolerances.py:1988]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R704-floatfea/tolerances.py:1989]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R704-tests/verification/rung4/test_f4_static_and_mapping.py:355]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-docs/milestones/F4.md:72]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2239]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2240]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2241]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2242]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2243]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2244]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2245]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2246]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2247]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2248]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2249]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2250]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2251]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2252]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2253]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2254]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2255]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2256]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-floatfea/tolerances.py:2257]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-tests/verification/rung4/test_f4_static_and_mapping.py:1511]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-tests/verification/rung4/test_f4_static_and_mapping.py:1512]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R705-tests/verification/rung4/test_f4_static_and_mapping.py:1515]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
```

# Revision 3 — R706, R707, and R708 which the settling loop found in my own counters

Answers: verdict 102 @ 061f4c3

**2026-10-06.**

## 0. CI at `bac3017`, the commit verdict 102 judged — **no run, and the generator says so**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 102 at `bac3017` through the
report's own `Answers:` line. **The generator exits 1 and this is its output
verbatim:**

```
no CI run at bac301796de7190f3bdf52a47a3c7dfe40a46669. A commit that was never pushed has no run, and a report cannot publish a table for it.
```

That is correct and it is CK0, not CK2. **This is the first round in this step whose JUDGED
COMMIT is a report commit**, and a report commit costs no run by design:

```
claim  the judged commit has no run, and the workflow says why
cmd    gh run list --commit bac301796de7190f3bdf52a47a3c7dfe40a46669
out    (no output)
cmd    grep -n "paths-ignore" -A 3 .github/workflows/ci.yml
out    24:    paths-ignore:
out    25:      - "docs/reports/**"
cmd    git diff --stat b68f2f7..bac3017 -- floatfea tests scripts data .github
out    (empty)
rule   CK0: a report revision changes no code, so the guards that read it run on the next
       code push and locally every time
judge  `bac3017` touches only `docs/reports/F4/step-2.md` and its answers file, so the
       CODE under review at `bac3017` is `b68f2f7`'s code exactly, and `b68f2f7`'s run is
       the evidence for it. The reviewer made this same ruling twice in this step, at
       `fa709df` and at `bac3017` itself.
```

**The run that describes the reviewed code**, job by job, from `gh`:

```
claim  run 37570657425 at `b68f2f7` is failure at the guards job only; the ladder is green
cmd    gh run view 37570657425 --json jobs --jq '.jobs[] | "\(.name)\t\(.conclusion)"'
out    lint, unit and guards  failure
out    the verification ladder  success
out    CI determinism -- ten legs agree  skipped
out    CI determinism -- leg  skipped
rule   the verification ladder is the gate; the guards job carries the report guards,
       which are EG3 state (2) at that commit
judge  184 ids, all on state (2)'s list, decomposed in revision 2 section 0b and
       re-measured by the reviewer at `135 + 20 + 7 + 1 + 1 + 1`. **A SECTION THE
       GENERATOR CANNOT PRODUCE IS A GAP IN THE APPARATUS AND I AM NAMING IT RATHER THAN
       WORKING AROUND IT**: `tests/test_report_carried.py`'s CI guards assume the judged
       commit has a run, and a round judged at a report commit breaks that assumption.
       Under DR1 that is a guard failing FALSE -- there is genuinely no run and the report
       says so -- and DR1 says such a guard is fixed or deleted, never extended. It is
       apparatus, so it does not go in a step commit. **Recorded for Xabier with C12.**
```

**The job table of that run**, counted by `scripts/ci_section.py`'s own `counts`
rather than by a reimplementation of it, because the generator's refusal is about which
COMMIT to anchor on and not about counting:

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 981 | 184 | 0 |
| the verification ladder | 1978 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |

**Run `37570657425`, conclusion `failure`. Job conclusions: 4 jobs, 1 not green** --
`lint, unit and guards` (failure); `the verification ladder` **success**; the two
`CI determinism` jobs `skipped`, which is CK0's own `workflow_dispatch` condition and not
CK2. The guards job's failures are the 184 EG3 state (2) ids.

**AND THE APPARATUS HAS NO STATE FOR THIS, WHICH I AM NAMING RATHER THAN DRESSING AS
ONE.** `tests/test_report_carried.py` knows three CI states: a run with jobs, CK2 (a run
whose jobs were never created, which its `_UNAVAILABLE` pattern matches on a fixed phrase
about the billing allowance), and -- through `scripts/ci_section.py` -- a run that exists.
It has **no state for "the judged commit is a report commit, so `paths-ignore` created no
run at all"**. Writing CK2's phrase here would assert a billing state that is not the case;
the truth is CK0. **An earlier draft of this paragraph QUOTED that phrase in order to
reject it, and the guard matched the quotation and routed this section into the CK2 branch**
-- a measurement artefact of describing a pattern inside the text the pattern reads, which
is worth recording. So this
section names the judged commit first, states that it has no run and why, and carries the
counts of the run whose CODE is identical to it -- which is the reviewer's own reasoning at
`fa709df`, applied here.

**The structural point for Xabier, with C12.** A report revision never gets a run, so a
round whose judged commit is a report commit can never have a generated section 0. The fix
is a process one and there are two shapes: the verdict names the newest CODE commit as the
one it judged, or a report revision is pushed together with a code commit. Both are
outside a step commit. **Under DR1 this is a guard failing false -- there is genuinely no
run and this section says so correctly -- and DR1 says such a guard is fixed or deleted,
never extended.**

## 0a. Runs since the commit verdict 102 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 102 at `bac3017` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37577408916` | push | `c78918c` | **no result** (`cancelled`) |
| `37577931492` | push | `77d4a6b` | conclusion **failure** |

**Run `37577931492`, conclusion **failure**: 8 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R704-tests/verification/rung4/test_f4_static_and_mapping.py:356]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0b. The reds, and there are none outside the step boundary

```
claim  the whole tree is green at the last code commit, with no report-guard exclusion
cmd    python -m pytest tests -q          (the reviewer's own run at bac3017)
out    3236 passed, 0 failed, 0 skipped in 654.90s
cmd    python scripts/suite_count.py      (mine, at b68f2f7)
out    Whole suite: 2855 passed, 0 failed, 0 skipped
out    The excluded set: 192 passed, 184 failed, 0 skipped
rule   EG3 state (2): a verdict written, its answering report not yet committed
judge  `2855 + 381 = 3236` reconciles exactly, and the reviewer said so. The 184 were
       measured at `b68f2f7`, a commit where revision 2 did not exist; at revision 2's
       own commit all 381 report-guard cases pass, which is EG3 condition (ii) and is in
       revision 2 section 13. **This revision creates state (2) again** and it clears at
       this revision's own commit; the measurement goes in the closure section.
```

## 1. The schedule, and what closes with this revision

**Step 2's date is 14 October and it holds.** This is **round 2's answering revision and
the third of three, so step 2 closes here.** What closes with it: R704, R705, R706, R707
and R708 all answered, EQ3's DQ4(i), DQ4(ii) and DQ5 shipped with counters that bracket
their ceilings' domains, R685 closed, and DQ8's residual per body with the dimensional
finding reported rather than papered over. **What carries, by name and still blocking
under CZ0:** nothing. **What carries as closure items:** C1 to C15 and R697, R699, R700,
R701, R702 and R703, listed in section 6. **What is not built and is step 3's:** G4.1's
dynamic gate and G4.5's measurement, both of which wait on the six FloatSim runs and on a
plan decision about DQ8's quantity — C1 is that decision's input and is answered before
it. No step has closed carrying a blocking item, so DZ7c does not fire.

## 2. R706 — the floor was the platform arm's, published as the quantity's

```
claim  the ceiling this counter brackets reads SIXTEEN members; the counter injected into
       one
cmd    sed -n '182,215p' tests/verification/rung4/test_f4_static_and_mapping.py | grep -nE "checked|assert"
out    8:    checked = 0
out    15:            checked += 1
out    29:    assert checked == 16, (
rule   a counter brackets the domain of the ceiling it is declared against
judge  R704 generalised this quantity over `f` and left it specific to the member CLASS,
       and those are the same generalisation.
```

**The entry said so eighteen lines above its own value, which is the part worth keeping.**

```
claim  the narrowness was written down in the same entry I edited
cmd    git show c78918c~1:floatfea/tolerances.py | sed -n '1990,1992p'
out    # `0.5/2 = 0.25` and `0.75/2 = 0.375`. C149's correction stands -- the hub arms
out    #  are the smaller figure and the platform value is declared because it is the
out    #  member the counter-case injects into.
judge  not hidden, not subtle, and not new. I moved the value and did not read up.
```

```
claim  the hub-arm shortfall is `6f/17` and sits BELOW the declared floor
cmd    python <the sixteen-member loop, at every rung>
out       f      platform f/2            hub 6f/17            min over 16
out    0.75   0.37499999999999983   0.2647058823529406   0.2647058823529406
out     0.5    0.2499999999999997  0.17647058823529332  0.17647058823529332
out     0.4   0.19999999999999976   0.1411764705882346   0.1411764705882346
out     0.3    0.1499999999999998  0.10588235294117578  0.10588235294117578
out     0.2    0.0999999999999997  0.07058823529411722  0.07058823529411722
out     0.1   0.04999999999999985  0.03529411764705815  0.03529411764705815
out    sixteen members at every rung; worst disagreement with the closed form 1.93e-14
rule   `F4_STATIC_REACTION_AGREEMENT_COUNTER`, the smallest defect the gate must fail
judge  `6f/17` is `_defect_tip_ratio`'s own `12/17` -- hub weight over total applied,
       14715000 against 14715000 + 6131250 -- halved. Not a fitted factor. `0.04` sat
       above the defect on all TWELVE hub arms at `f = 0.1`, every rung `admissible`.
```

```
claim  `0.03` clears every member at every rung and the boundary is solved both ways
cmd    python <the same loop, against the declared floor>
out    smallest over every non-vacuous rung and all 16: 0.03529411764705815
out    floor 0.03 margin : 1.1765x ; the old 0.04 margin : 0.8824x
out    EH4: 6f/17 = 0.04 at f = 0.11333333333333334
judge  the whole failure lived below `f = 0.1133`, and the floor may be no higher than
       0.03529411764705883.
cell   ONE VARIABLE: `_reaction_shortfall` reverted to `f / 2.0` for every class
cmd    python -m pytest tests/verification/rung4/test_f4_static_and_mapping.py -q
out    1 failed, 100 passed   FAILED ...::test_G4_the_defective_formula_misses_the_
       reaction_by_f_over_two
out    restored: 101 passed
judge  it fails at the SHIPPED rung, not only at f = 0.1, because the closed-form
       equality catches a wrong member class immediately.
```

**And the one suspicion of mine the measurement refuted.** I asked the reviewer to check
whether the two floors shared a derivation and so might share an error.

```
claim  `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.005` is safe on all sixteen at every rung
cmd    python <R694's ablation, every rung, minimum over all members>
out           f               min ratio   floor 0.005   old 0.05  admissible
out        0.75      0.0566037735849053          PASS       FAIL        True
out         0.5     0.03448275862068926          PASS       FAIL        True
out         0.1    0.006060606060605793          PASS       FAIL        True
out    the `min ratio` column is the minimum over every member of every body
judge  they were NOT derived the same way. R694's repair already generalised over the
       member class, into `_defect_tip_ratio`; R704's did not. The suspicion was right in
       kind and wrong in fact, and only the loop separated them. **`0.005` is not
       touched.**
```

## 3. R707 — a gate that could not fail on the attribute its own expected side read

```
claim  a doubled remainder, a 0.1% error and a moved node ALL read the clean value
cmd    python <the injection on the BODY ATTRIBUTE, every rung>
out       f      clean                   m_r doubled             m_r +0.1%            node moved
out    0.75  5.108969552176339e-16  5.108969552176339e-16  5.108969552176339e-16  5.108970e-16
out     0.5  6.386211940220424e-16  6.386211940220424e-16  6.386211940220424e-16  6.386212e-16
out     0.1  4.789658955165317e-16  4.789658955165317e-16  4.789658955165317e-16  4.789659e-16
rule   `F4_DQ4_RIGID_VECTOR` = 1.0e-12
judge  to every digit, at every rung. The blind fraction of the body's mass is 0.25 at
       f = 0.75 and 0.90 at f = 0.1 -- it GROWS as the ladder descends, the opposite
       direction from the `remainder_dropped` row's own behaviour, so neither row's
       direction could be inferred from the other.
```

**My first cell was wrong and looked like a refutation, which is the part I want recorded.**

```
claim  injecting into `M` alone was CAUGHT and said nothing about R707
cmd    python <the injection into the matrix, not the attribute>
out    remainder x2 : 0.6666666666666666 at f = 0.75, 1.0 below -- CAUGHT
judge  moving the matrix moves ONE side, so of course the comparison sees it. R707 is
       about a value on BOTH sides, so the injection has to move the BODY ATTRIBUTE. I
       produced a confident "not reproduced" that was an artefact of where I put the
       defect, and the verdict's figure was right.
```

```
claim  the repair is one expression, declares no new constant, and clean does not move
cmd    python <the repaired expected side, every rung>
out    REPAIRED: m_r doubled 0.6666666666666666 (f=0.75), 1.0 below
out    REPAIRED: m_r +0.1%   0.0006666666666664893 (f=0.75), 1.0e-03 below
out    worst clean under the repair : 6.386211940220424e-16
rule   `deck_mass - sum(rho A L)` is DY0's own definition of the remainder
judge  clean is unchanged TO EVERY DIGIT, because the two are equal when the split is
       right -- which is what makes this a reach fix rather than a recalibration.
cell   ONE VARIABLE: the expected side reverted to `body.remainder_mass`
out    1 failed, 100 passed   FAILED ...[remainder_mass_scaled]
judge  that row and nothing else. Without it, restoring the shared read leaves the whole
       suite green and nothing holds the independence (R683's lesson).
```

**What the repair does NOT reach, stated rather than left to be found.** Both sides still
read `body.remainder_node`, so a remainder lumped at the wrong node of the right body is
outside this gate either way. The rung-3 mass-property gate's CoG comparison is what
catches it, and this gate's entry had the relationship backwards:

```
claim  the entry's only statement of what this gate adds over the rung-3 gate was
       inverted on the node half
cmd    git show 77d4a6b~2:floatfea/tolerances.py | grep -n "passes G3.1a and fails here"
out    2312:# passes G3.1a and fails here, and the dynamic residual DQ8 defines divides by `M a
rule   G3.1a compares mass, CoG and inertia; this gate compares the nodal vector
judge  for the remainder's NODE the opposite of that sentence is true -- the CoG
       comparison catches a moved remainder and this gate does not -- so the one
       sentence saying what the gate adds was wrong about the half R707 is on. It is
       rewritten with the rung-3 gate named.
```

## 4. R708 — the settling loop, run on my own counters, found one

The round-2 verdict named what it would not accept at this revision: *a counter whose
domain is narrower than the domain of the ceiling it brackets, with the narrowness
unstated*, and gave the settling command. I ran it on the three constants I had just
declared rather than waiting for it to be run on them.

```
claim  the counter-cases injected into `bodies[0]` while their ceilings read five
cmd    git show 77d4a6b~1:tests/verification/rung4/test_f4_static_and_mapping.py | grep -c "body = built.bodies\[0\]"
out    4
rule   a counter brackets the domain of the ceiling it is declared against (R706)
judge  I WROTE 3 HERE AND THE COMMAND PRINTS 4. Three are the counter-cases R708 widened;
       the fourth is `test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula`, which is a
       counter-case for a DIFFERENT ceiling -- `test_EO1_static_member_forces_match_
       STATICS_not_the_model`, whose own assertion is also platform-only -- so its domain
       matches its ceiling and it is not an instance. The count was wrong; the claim it
       was supporting was not. Two of the three widened also picked one field or one
       direction out of several.
```

```
claim  `F4_DQ4_RIGID_VECTOR_COUNTER = 5.0e-4` sat ABOVE its defect on a HUB
cmd    python <the settling loop: 5 bodies x 4 fields, every rung>
out       f      mass_scaled min        remainder_mass min      where
out    0.75   0.001000000000000298   0.00039999999999946773   hub2/oblique
out     0.5   0.001000000000000298   0.000666666666666371     hub1/oblique
out     0.4   0.0010000000000002659  0.0007499999999997228    hub2/oblique
out     0.3   0.001000000000000186   0.0008235294117645755    hub1/oblique
out     0.2   0.0010000000000002659  0.0008888888888885439    hub1/z
out     0.1   0.0010000000000002659  0.0009473684210523983    hub1/oblique
out    counter 0.0005 below the smallest: False   margin 0.8000x
rule   the counter is the smallest defect the gate must still fail, over the ceiling's
       domain
judge  **the platform is the STRONGEST body for that injection, not a representative
       one**: its remainder is a quarter of its mass at `f = 0.75` and a hub's is less.
       R707's published `0.0006666666666664893` is the platform's figure; the quantity's
       is `0.00039999999999946773`. I took the counter where the defect is largest, which
       is the opposite of what a counter is for.
```

```
claim  3.0e-4 clears every body, every field and every rung
cmd    python -c "print(0.00039999999999946773/3.0e-4)"
out    1.3333333333315591
out    EH4 weakening side: 0.7500 -- a 25% window, the narrowest in the F4 block
cell   ONE VARIABLE: the counter reverted to 5.0e-4
out    1 failed, 100 passed   FAILED ...[remainder_mass_scaled]  ; restored: 101 passed
judge  the widened counter-case catches the wrong value at the SHIPPED rung.
```

**The other two were safe on value and narrow on domain**, which is the half R706 says
must not be left unstated:

```
claim  DQ4(ii)'s and DQ5's published injection figures were one body's
cmd    python <the settling loop on both>
out    DQ4(ii) moment_scaled, min over 5 bodies x every element x 2 planes:
out      0.0010000000000004098   (the entry published 0.001000000000000745)
out    DQ4(ii) lumped 1.0 ; sign_flipped 2.0000000000000004 ; margin 2.0000x
out    DQ5 moment_factor, min over 5 bodies x 3 directions:
out      0.0007216878364869912 on hub4 / x
out      (the entry published 0.0008333333333333215, the platform under -z)
out    DQ5 remainder_drop min 0.25000000000000006 ; margin 1.8042x not 2.0833x
rule   BP0: the rule beneath these figures changed from "one body" to "the ceiling's
       domain" in the same commit, so the figures are regenerated in it
judge  neither value moves. What was wrong is that a reader comparing `4.0e-4` with
       `8.33e-4` computes 2.0833x where the quantity gives 1.8042x, and the margin is the
       number a reviewer attacks.
```

```
claim  the weakest DQ5 case is not the one a reader would guess
cmd    python <the settling loop, where-column>
out    weakest at every rung: hub4/x, and hub2/x at f = 0.2 -- never platform/minus_z
judge  free fall straight down on the platform is the obvious case and it is the
       STRONGEST. A hub falling sideways is the weakest, and nothing in the shipped
       configuration points at it.
```

```
claim  the domain is now asserted, so narrowing it back fails loudly
cmd    grep -n "of 5 bodies were injected\|of 20 body/field\|of 15 body/direction" tests/verification/rung4/test_f4_static_and_mapping.py
out    1836:        f"{len(per_body)} of 5 bodies were injected. The ceiling reads five, so a "
out    1918:        f"{len(per_case)} of 20 body/field cases were injected. The ceiling reads five "
out    2104:        f"{len(per_case)} of 15 body/direction cases were injected. The ceiling reads "
judge  the same device as `assert checked == 16` in the ceiling R706 was about. A count is
       what distinguishes "compared and clear" from "never reached", which is R689 on a
       different gate.
```

## 5. What the five instances have in common, which is the only generalisation I will claim

R682, R694, R704, R706 and R708 are the same defect five times. The shape is **not** "a
counter calibrated at one rung". It is **a counter calibrated at one POINT of whatever the
ceiling's domain is** — and `f`, the member class, the body, the field and the direction
are all coordinates of that domain. Each time, the fix generalised over the coordinate
that had just been found and left the others:

| # | the coordinate that was narrow | found by |
|---|---|---|
| R682 | the basis (`M`, `f`) | the reviewer |
| R694 | the ladder rung | the reviewer |
| R704 | the ladder rung, on the sister entry | the reviewer |
| R706 | the member class | the reviewer |
| R708 | the body, the field, the direction | me, with the reviewer's loop |

The transferable part is the loop, not the list: **a counter's quantity, evaluated at
every point of the ceiling's own parametrisation, minimum pasted.** Where that is cheap it
is the derivation; the three counter-cases now assert their own domain size so the loop
cannot be silently narrowed again. I am not claiming the shape is now closed — four of the
five were found by someone else, and the fifth only because the fourth handed me the
command.

## 6. Closure items — C1 to C15, and R697 with R699 to R703

Per CZ0 these are fixed **once, in the step's closure commit**, are not re-reviewed item by
item, and the step is not held on one.

```
claim  the list is the verdict's own, fifteen plus six carried
cmd    (the round-2 verdict's `## Closure items` block, C8 to C15, plus C1 to C7 carried)
out    C8 the direction argument is false of a floor   C9 a bare ZeroDivisionError
out    C10 a published f label wrong by rounding       C11 an ablation count with no
out    C12 three cited scripts not in the tree             stated selection
out    C13 the stale `:3` header                      C14 "every element" cannot vary
out    C15 R697 is R706's source sentence             C1-C7 carried unchanged
```

**C1 and C12 are the two that are not simple prose fixes.**

* **C1** — the dimensional direction in `scripts/report_joint_reactions.py` is backwards
  and both it and the commit message are incomplete against the reviewer's
  eleven-of-seventeen measurement. It is **answered before the G4.1-dynamic quantity is
  chosen**, because that choice is (c) and C1 is its input.

```
claim  the comment asserts the wrong direction for a moment over a force
cmd    grep -n "1/length" scripts/report_joint_reactions.py
out    238:    three. Dividing a moment by a force scale gives a number with units of 1/length, so
rule   N.m / N is LENGTH
judge  mine, written in the commit that introduced the per-body breakdown.
```
* **C12** — three `scratchpad/` scripts cited as `cmd` are not in the tree, so a third
  party cannot run them. **This is a real limit on BF0 and I am raising it rather than
  deciding it**, because the two obvious fixes pull against each other: committing the
  measurement scripts adds files under `scripts/`, which brushes DR1's freeze; inlining
  every loop makes the reports much longer. The reviewer keeps its harnesses in its own
  scratchpad by the same convention, so the asymmetry is only that my `cmd` lines name
  paths and its do not. **Xabier's call.**

| item | what it is | where |
|---|---|---|
| C1 | the dimensional direction, and its 11-of-17 premise | **before the G4.1-dynamic quantity** |
| C2 | DQ5's worst clean | **answered early**, in `c78918c` |
| C3 | a figure without its body (`:971`) | closure commit |
| C4 | the oblique field's claimed discrimination | closure commit |
| C5 | the per-body label map validated by count only | closure commit; corpus 28 Oct |
| C6 | R697 and R699–R703 carried | this section |
| C7 | the `135`/`107` count | revision 2 section 0b |
| C8 | "a counter moving down demands more" is false of a floor | closure commit |
| C9 | a bare `ZeroDivisionError` at `f = 0` | closure commit |
| C10 | a published `f` label wrong by rounding | closure commit |
| C11 | the ablation count has no stated selection | closure commit |
| C12 | three cited scripts not in the tree | **process question, above** |
| C13 | the stale `:3` header | closure commit |
| C14 | "measured on every element" cannot vary | closure commit |
| C15 | R697 is R706's source sentence — one fix for both | closure commit |

**R697, R699, R700, R701, R702 and R703** are carried unchanged by the earlier verdict's
instruction and C6 of the round-2 one, named individually because a range is not a list.

## 7. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R653 | **answered** — revision 1 | R682, R683, R684, R685, R653 and |
| R679 | **answered** — step 1 closure | 's remainder (R683 IS that remainder, so five distinct) -- plus C161 to C166 and the |
| R682 | **answered** — revision 2 | R682, R683, R684, R685, R653 and |
| R683 | **answered** — revision 1 | R682, R683, R684, R685, R653 and |
| R684 | **answered** — revision 1 | R682, R683, R684, R685, R653 and |
| R685 | **answered** — revision 2 | R682, R683, R684, R685, R653 and |
| R686 | **answered** — verdict 98 | test_R653_the_value_the_DRIVER_reconstructs_with_is_the_declared_one CANNOT FAIL ON THE... |
| R687 | **answered** — verdict 98 | THE RANGE ASSERTION CLAIMS A PROPERTY GENERALIZED-ALPHA DOES NOT HAVE, AND THAT FALSE SENTENCE... |
| R688 | **answered** — verdict 98 | round(x, 5) == published IS A COMPARISON EPSILON, THE TEST AND THE REPORT BOTH CALL IT EXACT,... |
| R689 | **answered** — verdict 99, as R692 | THE PRODUCTION MAPPING GATE READS 0.000e+00 ON A ROW IT COMPARES NOTHING IN, AND PASSES ON AN... |
| R690 | **answered** — verdict 99 | to (d), and I say so rather than dressing it as more.) ER0, ER1, ER2, EQ2, EQ3 AND EQ4 EXIST... |
| R691 | **answered** — revision 2 | R682's FALSE ARITHMETIC IS DELETED FROM tolerances.py AND LEFT STANDING IN THE PLAN ROW THAT IS... |
| R692 | **answered** — verdict 99 | compared > 0 IS R689's CLOSING CONDITION MINUS ITS COUNT. ALL SIXTEEN DEGRADED ROWS STILL READ... |
| R693 | **answered** — verdict 99 | THE NEW COUNTER'S BRACKET IS PUBLISHED AS 2x AND MEASURES 1.0857x, AND THE SENTENCE SAYING NO... |
| R694 | **answered** — §2 | F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05 AND F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.375... |
| R695 | **answered** — revision 2 | floatfea/tolerances.py:1979 NAMES AN INJECTOR THAT DOES NOT EXIST, and e2fa88a is the commit... |
| R696 | **answered** — revision 2 | THE CEILING ENTRY BRACKETING THE MOVED COUNTER STILL PUBLISHES THE OLD BASIS.... |
| R697 | **carried** — §6 | THE f/2 MECHANISM IS FALSE OF 12 OF THE 16 MEMBERS. floatfea/tolerances.py:1974-1975 ("The... |
| R698 | **answered** — revision 2 | THE EQUALITY'S JUSTIFICATION IS REFUTED BY ITS OWN MEASUREMENT.... |
| R699 | **carried** — §6 | THE BP0 SWEEP MISSED FIVE MORE f/M-DEPENDENT FIGURES, AND ONE IS THE SITE R691's CLOSING... |
| R700 | **carried** — §6 | THE REPLAY DRIVER SHIPS WITH THE OVERRIDE OFF, AND ONE SENTENCE CLAIMS OTHERWISE. cmd grep -n... |
| R701 | **carried** — §6 | "Vz does not move with f at all" IS TRUE ONLY OF THE STATION THE TABLE REPORTS.... |
| R702 | **carried** — §6 | "My runs from 1.1200x to 0.8800x" IS THE HUB'S RANGE PUBLISHED AS THE WHOLE RANGE.... |
| R703 | **carried** — §6 | THE SYMMETRY ENTRY LOST ITS INJECTION-SIDE EDGE (EH4). floatfea/tolerances.py:2104-2118. The... |
| R704 | **answered** — §2 | F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.375 IS STILL A FROZEN EQUALITY PINNED TO f = 0.75, AND... |
| R705 | **answered** — round 2 | DQ4(ii)'s MOMENT CHANNEL CANNOT FAIL ON A SIGN, AND THE PLAN DECLARES ITS QUANTITY AS... |
| R706 | **answered** — §2 | F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.04 IS THE PLATFORM ARM'S FLOOR PUBLISHED AS THE... |
| R707 | **answered** — §3 | DQ4(i) CANNOT FAIL ON THE REMAINDER MASS OR ON THE REMAINDER NODE, AND THE ENTRY'S ONLY... |

## 7a. Every named site this round's diff does not touch, declared by name

```
claim  every site below is named by a verdict and untouched by this round's diff
cmd    python -m pytest tests/test_report_carried.py::test_every_named_site_is_touched_or_declared -q
out    173 sites before this table existed, across 20 findings
rule   a site is TOUCHED by the diff or DECLARED `no change` beside its exact token
judge  the two findings this round answers are R706 and R707, plus R708 which is mine.
       The substantive rows are the ones where something was deliberately left: R706's
       `tolerances.py:1990` is a sentence that was RIGHT and is not edited, and R707's
       node sites are the half of the gate the repair does not reach.
```

| finding | site | this round | why |
|---|---|---|---|
| R686 | `HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `floatfea/io/integrator.py:27` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `floatsim/solver/newmark.py:222` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `integrator.py` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `scripts/export_platform_deck.py` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `scripts/report_joint_reactions.py:77` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/test_no_tolerance_literals.py` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1016` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1017` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1018` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1019` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1020` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1021` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1022` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1023` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1024` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1025` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1026` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1027` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1028` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1029` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1030` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1031` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1032` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1033` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1034` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1035` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1036` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1037` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1038` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1039` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1040` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1041` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1042` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1043` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1044` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1045` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R686 | `tests/verification/rung4/test_f4_static_and_mapping.py:1046` | **no change** | closed at verdict 98. This round's diff does not reach it. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1037` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1038` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1039` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1040` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1041` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1042` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1043` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1044` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1045` | **no change** | closed at verdict 98, on branch A as offered. |
| R687 | `tests/verification/rung4/test_f4_static_and_mapping.py:1046` | **no change** | closed at verdict 98, on branch A as offered. |
| R688 | `CLAUDE.md` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `docs/load-interchange-v1.md` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1000` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1001` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1002` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1003` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1004` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1005` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1006` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1007` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1008` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1009` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1010` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1011` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1012` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:1013` | **no change** | closed at verdict 98, on the branch it took. |
| R688 | `tests/verification/rung4/test_f4_static_and_mapping.py:999` | **no change** | closed at verdict 98, on the branch it took. |
| R689 | `CLAUDE.md` | **no change** | closed at verdict 99 as R692. |
| R690 | `F3.md` | **no change** | closed at verdict 99. |
| R690 | `docs/milestones/F3.md` | **no change** | closed at verdict 99. |
| R690 | `docs/milestones/F4.md:5` | **no change** | closed at verdict 99. |
| R691 | `CLAUDE.md` | **no change** | closed in `30e4395`, read by verdict 101. |
| R691 | `docs/SUPERVISOR.md` | **no change** | closed in `30e4395`, read by verdict 101. |
| R691 | `docs/milestones/F4.md:348` | **no change** | closed in `30e4395`, read by verdict 101. |
| R691 | `floatfea/tolerances.py:1990` | **no change** | closed in `30e4395`, read by verdict 101. |
| R691 | `test_f4_static_and_mapping.py:549` | **no change** | closed in `30e4395`, read by verdict 101. |
| R691 | `tests/test_plan_matches_tolerances.py` | **no change** | closed in `30e4395`, read by verdict 101. |
| R691 | `tests/verification/rung4/test_f4_static_and_mapping.py:549` | **no change** | closed in `30e4395`, read by verdict 101. |
| R694 | `floatfea/model/platform.py:116` | **no change** | tip-moment half in `30e4395`; the reaction half is R704 then R706. |
| R694 | `floatfea/tolerances.py:2027` | **no change** | tip-moment half in `30e4395`; the reaction half is R704 then R706. |
| R695 | `floatfea/tolerances.py:1979` | **no change** | closed in `30e4395`, verified by the reviewer's whole-file sweep. |
| R695 | `tests/verification/rung4/test_f4_static_and_mapping.py:315` | **no change** | closed in `30e4395`, verified by the reviewer's whole-file sweep. |
| R696 | `floatfea/tolerances.py:1942` | **no change** | closed in `30e4395`. |
| R697 | `floatfea/tolerances.py:1974` | **no change** | closure item, carried by instruction. Section 6; C15 pairs it with R706. |
| R697 | `floatfea/tolerances.py:1975` | **no change** | closure item, carried by instruction. Section 6; C15 pairs it with R706. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:320` | **no change** | closure item, carried by instruction. Section 6; C15 pairs it with R706. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:321` | **no change** | closure item, carried by instruction. Section 6; C15 pairs it with R706. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:322` | **no change** | closure item, carried by instruction. Section 6; C15 pairs it with R706. |
| R697 | `tests/verification/rung4/test_f4_static_and_mapping.py:323` | **no change** | closure item, carried by instruction. Section 6; C15 pairs it with R706. |
| R698 | `floatfea/tolerances.py:1960` | **no change** | closed in `30e4395`. |
| R698 | `floatfea/tolerances.py:1961` | **no change** | closed in `30e4395`. |
| R698 | `floatfea/tolerances.py:1962` | **no change** | closed in `30e4395`. |
| R699 | `floatfea/post/member_forces.py:10` | **no change** | closure item, carried by instruction. Section 6. |
| R699 | `floatfea/post/member_forces.py:12` | **no change** | closure item, carried by instruction. Section 6. |
| R699 | `floatfea/post/member_forces.py:13` | **no change** | closure item, carried by instruction. Section 6. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:526` | **no change** | closure item, carried by instruction. Section 6. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:527` | **no change** | closure item, carried by instruction. Section 6. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:555` | **no change** | closure item, carried by instruction. Section 6. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:556` | **no change** | closure item, carried by instruction. Section 6. |
| R699 | `tests/.../rung4/test_f4_static_and_mapping.py:95` | **no change** | closure item, carried by instruction. Section 6. |
| R700 | `export_platform_deck.py` | **no change** | closure item, carried by instruction. Section 6. |
| R700 | `scratchpad/er1b_runs.py` | **no change** | closure item, carried by instruction. Section 6. |
| R700 | `scripts/export_platform_deck.py` | **no change** | closure item, carried by instruction. Section 6. |
| R700 | `scripts/report_joint_reactions.py` | **no change** | closure item, carried by instruction. Section 6. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:200` | **no change** | closure item, carried by instruction. Section 6. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:201` | **no change** | closure item, carried by instruction. Section 6. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:202` | **no change** | closure item, carried by instruction. Section 6. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:203` | **no change** | closure item, carried by instruction. Section 6. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:204` | **no change** | closure item, carried by instruction. Section 6. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:205` | **no change** | closure item, carried by instruction. Section 6. |
| R701 | `docs/reports/F4/preview-PRELIMINARY.md:206` | **no change** | closure item, carried by instruction. Section 6. |
| R702 | `docs/reports/F4/preview-PRELIMINARY.md:208` | **no change** | closure item, carried by instruction. Section 6. |
| R702 | `docs/reports/F4/preview-PRELIMINARY.md:209` | **no change** | closure item, carried by instruction. Section 6. |
| R702 | `docs/reports/F4/preview-PRELIMINARY.md:210` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2104` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2105` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2106` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2107` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2108` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2109` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2110` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2111` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2112` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2113` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2114` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2115` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2116` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2117` | **no change** | closure item, carried by instruction. Section 6. |
| R703 | `floatfea/tolerances.py:2118` | **no change** | closure item, carried by instruction. Section 6. |
| R704 | `floatfea/model/platform.py:116` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `floatfea/tolerances.py:1988` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `floatfea/tolerances.py:1989` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `floatfea/tolerances.py:1995` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:350` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:351` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:352` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:353` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:354` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:355` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R704 | `tests/verification/rung4/test_f4_static_and_mapping.py:356` | **no change** | answered in `36a5003`; R706 is its member-class half, section 2. |
| R705 | `docs/milestones/F4.md:72` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2239` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2240` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2241` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2242` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2243` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2244` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2245` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2246` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2247` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2248` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2249` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2250` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2251` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2252` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2253` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2254` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2255` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2256` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `floatfea/tolerances.py:2257` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1511` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1512` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1513` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1514` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R705 | `tests/verification/rung4/test_f4_static_and_mapping.py:1515` | **no change** | closed at all three sites in `36a5003` and `b68f2f7`, round 2. |
| R706 | `tests/verification/rung4/test_f4_static_and_mapping.py:391` | **no change** | closed in an earlier round. |
| R707 | `docs/milestones/F4.md:431` | **no change** | closed in an earlier round. |
| R707 | `floatfea/model/platform.py:718` | **no change** | closed in an earlier round. |
| R707 | `floatfea/model/platform.py:719` | **no change** | closed in an earlier round. |
| R707 | `floatfea/model/platform.py:720` | **no change** | closed in an earlier round. |
| R707 | `floatfea/model/platform.py:721` | **no change** | closed in an earlier round. |
| R707 | `floatfea/model/platform.py:722` | **no change** | closed in an earlier round. |
| R707 | `floatfea/model/platform.py:723` | **no change** | closed in an earlier round. |
| R707 | `floatfea/model/platform.py:724` | **no change** | closed in an earlier round. |
| R707 | `floatfea/tolerances.py:2310` | **no change** | closed in an earlier round. |

## 8. Tolerances touched

```
claim  two values moved in this revision's range and no value was widened
cmd    git diff bac3017..HEAD -- floatfea/tolerances.py | grep -E "^[-+]F4_"
out    -F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.04
out    +F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.03
out    -F4_DQ4_RIGID_VECTOR_COUNTER: Final[float] = 5.0e-4
out    +F4_DQ4_RIGID_VECTOR_COUNTER: Final[float] = 3.0e-4
rule   a counter moving DOWN narrows what the gate will accept as clean
```

| constant | before | after | why |
|---|---|---|---|
| `F4_STATIC_REACTION_AGREEMENT_COUNTER` | `0.04` | `0.03` | **R706.** `0.04` was the platform arm's floor; the hub arms are `6f/17` and read `0.03529411764705815` at `f = 0.1`. Clears every one of sixteen members at every rung by `1.1765x` |
| `F4_DQ4_RIGID_VECTOR_COUNTER` | `5.0e-4` | `3.0e-4` | **R708.** `5.0e-4` sat above the remainder defect on `hub2` under the oblique field (`0.00039999999999946773`). The platform is the strongest body for that injection, not a representative one. Margin `1.3333x` |

**`F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` is NOT touched**, and the reason is measured
rather than assumed:

```
claim  the tip-moment floor is already a floor under all sixteen members at every rung
cmd    python <R694's ablation, minimum over every member of every body, each rung>
out    the `floor 0.005` column reads PASS at 0.75, 0.5, 0.4, 0.3, 0.2 and 0.1
out    the `old 0.05` column reads FAIL at every rung below the first
rule   the counter is the smallest defect the gate must still fail
judge  R694 forced the member-class split into `_defect_tip_ratio`, so this entry was
       already general over the coordinate R706 found narrow in its sister. Section 2
       carries the full run.
```

## 9. Lint, types, and the whole suite

```
claim  lint, formatting and types are green at this commit
cmd    python -m ruff check floatfea tests && python -m black --check floatfea tests
       && python -m mypy floatfea
out    All checks passed!
out    98 files would be left unchanged.
out    Success: no issues found in 36 source files
judge  `pytest` runs none of the three, which is CZ1's reason for pasting each.
```

**The first count is the result: `2856 passed, 0 failed, 0 skipped`** over the whole suite
outside the three files parametrised over this report. Nothing in `floatfea/`,
`tests/verification/`, `tests/unit/`, `tests/regression/` or any other guard is red.

```
cmd    python scripts/suite_count.py
out    Whole suite at 77d4a6b : 2856 passed, 0 failed, 0 skipped
out    The excluded set       : 373 passed, 8 failed, 0 skipped
cmd    python -m pytest tests/test_report_carried.py
       tests/test_report_numbers_are_sourced.py tests/test_tree_prose_consistent.py -q
out    1 failed, 392 passed  (the one was test_the_report_carries_a_WHOLE_SUITE_count,
out                          which this paste answers)
rule   EG3 state (2): a verdict written, its answering report not yet committed
```

**The eight, traced by name (EG3(i)).** Seven are `test_the_guard_survives_the_state` --
`baseline` plus the six planted states that cascade off a red baseline, identified by the
baseline being red and by each state's own failure line, which is EH1's correction. The
eighth is `test_every_named_site_is_touched_or_declared[R704-tests/verification/rung4/
test_f4_static_and_mapping.py:356]`.

**That eighth one is CZ1's own sentence for the third time in this step, and it is worth
saying plainly.** Section 7a's table was built from the WORKING TREE and the site resolves
one line earlier there than it does at the commit:

```
claim  the same site has a different line number in the working tree and at 77d4a6b
cmd    python -m pytest tests/test_report_carried.py::
       test_every_named_site_is_touched_or_declared -q     (working tree)
out    the R704 rows end at test_f4_static_and_mapping.py:355
cmd    python scripts/suite_count.py                       (clean worktree at 77d4a6b)
out    ...test_every_named_site_is_touched_or_declared[R704-tests/verification/rung4/
out       test_f4_static_and_mapping.py:356]
rule   the guard asks, per site, whether a COMMIT touched it
judge  R706's and R708's commits moved the line between the two measurements. The guard's answer is a function of the commit graph, so it cannot be settled
before the commit exists -- which is exactly why CZ1 says "I ran it before committing" is
not a measurement for this class. **It is re-measured at this revision's own commit and
answered in a follow-on if it survives** (CZ1 (iv)); the closure section carries that
measurement.

**Whole suite at `77d4a6b`: 2856 passed, 0 failed, 0 skipped.** **The excluded set: 373 passed, 8 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 381 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R704-tests/verification/rung4/test_f4_static_and_mapping.py:356]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
```
