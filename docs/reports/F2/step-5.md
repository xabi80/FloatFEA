# F2 step 5 — V1.1 rigid-body modes, gate G2.1

Answers: verdict 25 @ aae355a

**2026-09-09.** Three commits since step 4's PASS: `2f92c58` (figures), `7774e14`
(closure) and `b67163f` (`process:`), then `4a23232` (plan, re-locked) and
`d1fea41` (step).

## 0. What this step is, and one input it did not have

G2.1: an unconstrained assembly has exactly six zero-energy modes. The gate is
two assertions, four declared tolerances, two negative controls in opposite
directions, and two injected counters — all in the first commit, per BZ2.

**One thing is recorded before anything else, because it is a gap and not a
choice.** The directive names "AX3's shape" for this step's model. **`AX3` does
not exist in this repository.** A grep over every file finds it only in prose I
wrote in two revisions of the step-4 report, from which it entered the directive.
The plan's own case table says V1.1's reference is *constructed*, and the
verification README says only "an unconstrained model", so a constructed frame is
what the locked plan asks for and is what shipped. If `AX3` names a real platform
shape, the gate and both controls are unchanged and only `_frame()` moves — but
the geometry is not something I will invent a meaning for.

```
cmd    grep -rni "ax3" over the whole repository, excluding .git
out    two hits, both in docs/reports/F2/step-4.md, both mine, both prose
cmd    the plan's case table row for V1.1
out    "| V1.1 | constructed | 6 zero eigenvalues by ratio ... | G2.1 |"
```

## 1. The gate

```
cmd    python -m pytest tests/verification/rung1/test_rigid_body_modes.py -q
out    8 passed
       lambda_6 4.2634e-07  lambda_7 2.6631e+07  ratio 1.6009e-14 vs 1e-12
       worst analytic vector outside the computed span 5.3061e-15 vs 1e-13
rule   ratio <= RIGID_BODY_MODE_RATIO and loss <= RIGID_BODY_SUBSPACE_LOSS
```

**A ratio, because G2.1 says so and the reason is in the statement.** The
eigenvalues of a stiffness matrix carry units and scale with `E`, with the
section and with the mesh. A ceiling on them would be a ceiling on the model.

**The span assertion is the half AP3 calls the real content.** Inside the
six-fold degenerate zero eigenvalue the eigenvectors are an arbitrary basis —
non-unique *in principle*, not merely non-reproducible — so asserting mode shapes
asserts what the mathematics does not confer. What is invariant under every basis
choice in that block is that the six analytic rigid-body vectors lie in the
computed span. Measured on the **worst** of the six, never on a mean.

## 2. The controls, and the one that failed first

```
cmd    the pinned-DOF control, at every one of the 30 degrees of freedom
out    nullspace dimensions {5} -- not a chosen DOF, all of them
cmd    the torsional-release control
out    lambda_7 4.4889e-07  lambda_8 2.6884e+07  nullspace 7
```

**The release control read SIX on its first version, and it was right to.** The
frame put the released member off-axis. The assembled matrix is in global
coordinates, so cutting a global rotation is not cutting a member's torsion: no
mechanism was created and the control measured nothing while claiming to build a
seventh mode. The member is parallel to global x now, so its torsion **is** the
component being cut, and the control asserts that premise about its own geometry
before it measures anything.

That is the whole argument for having built it: the gate was green through both
versions, and only the control could tell the difference.

**The release is built by DOF mapping**, because `releases.py` is step 11 and
does not exist. The released member's rotation about its own axis is assembled
into one extra scalar degree of freedom instead of into the shared node's. The
extra mode is provable rather than measured — that member can twist rigidly about
its own axis at zero strain energy while nothing else moves — which is why the
control asserts an exact count rather than a threshold.

## 3. Four tolerances, each set from the first run

| name | value | clean | headroom | counter | response |
|---|---|---|---|---|---|
| `RIGID_BODY_MODE_RATIO` | `1e-12` | `{{fig:rigid_body_mode_ratio}}` | ~62x | `1.0e-12` | `{{fig:rigid_body_counter_ratio}}` |
| `RIGID_BODY_SUBSPACE_LOSS` | `1e-13` | `{{fig:rigid_body_subspace_loss}}` | ~19x | `1.0e-12` | `{{fig:rigid_body_counter_loss}}` |

**Both counters are one defect**, and that is content rather than economy: a
diagonal stiffness resisting a rigid translation must lift a zero eigenvalue
**and** remove that translation from the span. One defect, both halves.

**Every figure above is a generated name from this gate's first commit.** R194's
remedy is applied at the start here rather than five rounds into it, which is the
one thing step 4 would have wanted done differently.

```
cmd    the defect sweep, one variable moved, at this commit
out    size    1e-14      1e-12      1e-08
       ratio   3.03e-13   3.06e-11   3.06e-07
       loss    7.59e-14   7.47e-12   7.47e-08
judge  linear over eight decades, so the ceiling is crossed by a defect between
       1e-14 and 1e-13 of the largest entry. The counter sits one decade above
       that crossing deliberately: a counter on its own detection edge tests the
       edge rather than the gate.
```

## 4. Both counters are registered, and pass both cells

```
cmd    python -m pytest tests/test_counters_are_injected.py -q
out    14 passed  (5 registered x 2 cells + 3 controls + the registry test)
```

They inject through `assembled`, the one function both gates read, so the
**shipped** gate computes the defective number and decides on it. A counter that
builds a defective matrix itself and compares the result with the ceiling never
runs the assertion it defends — R163's defect, three times in step 4.

**Their widened ceilings are measured, not typed.** The injection is a defect
*size*, so how far it lifts the quantity is a property of the frame;
`counter_response` returns it at the commit that runs. A literal there would be
stale the first time the frame moved.

## 5. The `v0` pin, and where I departed from the directive's wording

BZ2 says "`v0` pinned". **The gate is a dense symmetric eigensolve and has no
starting vector**, so pinning one would be vacuous, and choosing ARPACK for the
gate in order to have a pin to point at would be choosing a less accurate method
to satisfy a guard. What AP3's pin actually buys is that the ARPACK path is
reproducible, and that is asserted directly:

```
cmd    two ARPACK runs from determinism.deterministic_v0
out    max |difference| 0.000e+00, bit-identical
cmd    two runs from an UNPINNED random start
out    they differ, max |difference| 1.490e-07
judge  the second is the control. If two unpinned runs ever agreed, the pinned
       assertion would pass with the pin removed, and it fails rather than skips.
```

This is a departure from the literal wording and it is flagged rather than
buried. If the ruling is that the gate itself must run ARPACK under the pin, that
is a plan change and it comes back to the supervisor.

## 6. Carried

| item | status |
|---|---|
| step 4's twenty-fifth verdict | **PASS** at `4ccd166`. Its corpus round is regenerated in `2f92c58`, its closure artifact is `7774e14` |
| R200–R204, R206, R210, R215–R220, R222 | **open at 4a**, unchanged by this step and untouched by it |
| R221 — the ceiling margin is defended by a corpus that samples the interior | **open at 4a, and named first.** One round of searching the admissible corners halved it, `7.93x -> 3.62x` |
| R218 — a step report that states no suite count | **answered here**: `1578 passed, 0 failed, 0 skipped` |
| every earlier item | **as declared in the step-4 closure artifact**, `docs/closure/F2-step4.md` |

**Nothing from step 4 is carried as unanswered into this step**, because step 4
closed on a PASS. The 4a list is in the closure artifact by name, which is half
of R220's condition; the other half is `docs/milestones/F2a.md` carrying it with
the verdict each item came from, and that is 4a lock work.

## 7. What I am asking for

**A PASS**, or a **HOLD naming the item.** Two things I would rather have ruled
on than left:

1. **`AX3`.** The frame is constructed, which is what the locked plan asks for.
   If a specific platform shape was meant, say so and only `_frame()` moves.
2. **The dense eigensolver**, §5. The directive says the pin; the gate has
   nothing to pin, and the pin is exercised on the path that has one.

## 8. Witness

**The channel is open for the first time this milestone**: `xabi80/FloatFEA`,
private, PR #1, `F2 -> master`. Steps 1 to 4 have no witness comment and never
will — twenty-five consecutive reviews of step 4 were written by one reader, and
opening the channel now does not change that. **Step 5 is the first step that can
carry one.** There is no `[witness ...]` comment yet, which is an unavailable
check rather than a pass.

---

# Revision 2 — the range that had no report, and two guards that had no corpus

Answers: verdict 27 @ 8ffbd51

**2026-09-09.** Five commits since the twenty-sixth verdict: `e5f6deb` (lint),
`99d0565` (CI), `3577930` (`process:`), `76c186a` (CB0/CB1) and this one.

## 0. What this revision is, and what it is not

**R223 and R224 are NOT answered here.** G2.1's replacement quantity is a lock
Q&A (Q7) and the cross-platform golden question is another (Q8); both are with
the technical supervisor, and CB3 puts them after this work. They stay open on
the record.

**R232 is why this revision exists.** Three commits landed with no step report
covering them, in a milestone whose whole method is that every range is
reported. This revision covers all five.

## 1. R229 — the exemption window, with the reviewer's corpus

The window was rewritten twice without a corpus and was wrong both times. It is
now run against the reviewer's twenty-eight shapes, in the suite.

```
cmd    python -m pytest tests/test_marker_exemption_corpus.py -q
out    26 passed
rule   expect=caught -> `offending()` must return something;
       expect=exempt -> it must return nothing
out    4 of 28 remain, all four are `expect=caught`;
       all four `expect=exempt` entries pass, and the whole tests/ tree still
       scans clean -- no false positive anywhere
```

Three changes, one per species the reviewer measured:

- **markers are read from COMMENT TOKENS**, never from raw text. The scanner's
  own docstring said "message strings are not on that path" while a marker
  inside an assertion message exempted the statement.
- **a compound statement's header ends at the first DESCENDANT statement**, not
  at `body[0]`. `ast.Match` has no `body`, so every `match` fell to the
  whole-statement branch — the "far larger hole" the comment claimed to avoid,
  in the one compound statement it did not name.
- **one marker exempts at most one node**, consumed in source order.

**The four that remain are one species, and naming it is worth more than the
list.** Each is a multi-line statement holding exactly one flaggable node, with
a marker annotating a different sub-expression — a bare comment above the
arguments, a dict entry, a lambda default, a starred argument. "One marker, one
node" cannot tell which node was meant when there is only one to choose. The
tightening that would close it is what CA0 already tried and had to abandon,
because `black` moves a trailing comment onto the closing bracket; trading
nineteen misses for that regression is not an improvement.

**Not `xfail`, not `skip`.** The first version of that file reached for `xfail`,
which is the mechanism `CLAUDE.md` forbids wearing a reason. The miss set is
asserted instead, in the golden-file idiom: `KNOWN_MISSES` must **equal** the
measured miss set, so a miss that gets fixed and a miss that appears are both
build failures.

## 2. R230 — the ladder's gate, and the sentence withdrawn

```
cmd    python -m pytest tests/test_ci_ladder_gating.py -q
out    12 passed -- all ten of the reviewer's layouts, in the suite, so in CI
```

The step body is `scripts/run_rung.sh` now, so it can be executed off GitHub,
and the expectation is **declared** per directory rather than inferred from a
glob:

```
full:<dir>    exists, collects at least one test, and the run then stands on
              its own exit code. Exit 5 is a FAILURE.
empty:<dir>   exists, carries `.empty-by-design`, collects nothing. A test
              appearing there is a stale declaration and fails.
```

**The withdrawn sentence.** `ci.yml` named "a renamed directory" as a defect the
guard caught, and the reviewer measured it going from exit 4 to exit 0. The
sentence is withdrawn in the comment, and it is true now because
`ci_rung_directory_renamed` runs and requires the failure.

**Two of the ten require a different outcome under the declared rule**, both
stricter, both recorded in `REQUIREMENT_CHANGED` and asserted rather than
assumed:

| entry | why the requirement changes |
|---|---|
| `ci_rung_genuinely_empty` | rung 1 is declared `full:`, so a rung 1 holding only `__init__.py` now FAILS — the emptied-directory case CB1 asks to redden |
| `ci_rung6_both_populated` | rung 6's directory is declared `empty:`, so a test appearing in it FAILS as a stale declaration rather than running silently |

These change the reviewer's own `require=` field and are theirs to rule on.

## 3. R233 — the enumeration that was not complete

`e5f6deb`'s body typed six line numbers and they are the pre-commit ones for two
and neither pre nor post for four. The six sites are the right six.

```
cmd    grep -n NPY002 tests/verification/rung3/test_determinism_pins.py, at HEAD
out    :53 :55 :69 :70 :71 :72
```

And the rule enumeration was presented as complete and was not. Produced rather
than typed, at the commit that published it:

```
cmd    python -m ruff check floatfea tests --statistics, before e5f6deb
out    43 E501, 8 E702, 8 SIM300, 7 I001, 6 NPY002, 4 SIM117, 4 UP037,
       3 F401, 2 B905, 2 E741, 2 F821, 1 B007, 1 F841, 1 SIM102, 1 UP035
       -- 93, and the body named ten of the fifteen rules
judge  `SIM300` reflected the operand order of three assertions and `I001`
       sorted imports. The reviewer checked both are semantically inert and I
       am not re-asserting it; what was wrong was calling the list complete.
```

## 4. A finding of my own, found by fixing R232

**The carry guard has been reading step 4 since step 5 opened.**
`tests/test_report_carried.py` named `step-4.md` in two places. Step 5 has a
report and two verdicts, and the guard went on checking a report that could not
change against a verdict already answered — green for free, on a step nobody was
working on.

```
cmd    pytest tests/test_report_carried.py -q, before this commit
out    122 passed
cmd    the same, with the guard following the newest step and before this
       revision was written
out    80 failed, 13 passed
judge  every one of the 80 is a step-5 finding the report did not carry. The
       guard was not passing; it was reading the wrong file.
```

It follows the newest report now, and `test_the_guard_reads_the_step_being_worked_on`
fails if the verdict beside it is missing.

## 5. Classified under BU0

| item | class | reason |
|---|---|---|
| R229 | **blocking — a guard's reach, and it is a counter to the tolerance rule** | answered, §1 |
| R230 | **blocking — a published sentence about what CI catches** | answered, §2 |
| R231 | **open, and correctly** — the platform finding | Q8 is with the technical supervisor; nothing here touches it |
| R232 | **blocking — the record** | this revision |
| R233 | **4a by the reviewer, taken here** | §3, one command each |
| R223, R224 | **open** | Q7. Not answered here and not claimed to be |
| R225–R228 | **4a**, unchanged | |

## 6. Carried

| item | status |
|---|---|
| R6 | **4a or later** - classified in section 5 |
| R16 | **4a or later** - classified in section 5 |
| R25 | **4a or later** - classified in section 5 |
| R30 | **4a or later** - classified in section 5 |
| R33 | **4a or later** - classified in section 5 |
| R36 | **4a or later** - classified in section 5 |
| R50 | **4a or later** - classified in section 5 |
| R52 | **4a or later** - classified in section 5 |
| R62 | **4a or later** - classified in section 5 |
| R63 | **4a or later** - classified in section 5 |
| R65 | **4a or later** - classified in section 5 |
| R68 | **4a or later** - classified in section 5 |
| R76 | **4a or later** - classified in section 5 |
| R79 | **4a or later** - classified in section 5 |
| R80 | **4a or later** - classified in section 5 |
| R95 | **4a or later** - classified in section 5 |
| R97 | **4a or later** - classified in section 5 |
| R98 | **4a or later** - classified in section 5 |
| R100 | **4a or later** - classified in section 5 |
| R103 | **4a or later** - classified in section 5 |
| R113 | **4a or later** - classified in section 5 |
| R124 | **4a or later** - classified in section 5 |
| R129 | **4a or later** - classified in section 5 |
| R131 | **4a or later** - classified in section 5 |
| R132 | **4a or later** - classified in section 5 |
| R134 | **4a or later** - classified in section 5 |
| R139 | **4a or later** - classified in section 5 |
| R148 | **4a or later** - classified in section 5 |
| R151 | **4a or later** - classified in section 5 |
| R152 | **4a or later** - classified in section 5 |
| R159 | **4a or later** - classified in section 5 |
| R162 | **4a or later** - classified in section 5 |
| R170 | **4a or later** - classified in section 5 |
| R171 | **4a or later** - classified in section 5 |
| R172 | **4a or later** - classified in section 5 |
| R181 | **4a or later** - classified in section 5 |
| R189 | **4a or later** - classified in section 5 |
| R190 | **4a or later** - classified in section 5 |
| R198 | **4a or later** - classified in section 5 |
| R199 | **4a or later** - classified in section 5 |
| R200 | **4a or later** - classified in section 5 |
| R215 | **4a or later** - classified in section 5 |
| R216 | **4a or later** - classified in section 5 |
| R222 | **4a or later** - classified in section 5 |
| R223 | **open** — G2.1's quantity is Q7, with the technical supervisor |
| R224 | **open** — answered with Q7's plan edit, not before it |
| R225 | **4a lock item**, unchanged |
| R226 | **4a lock item**, unchanged |
| R227 | **4a lock item**, unchanged |
| R228 | **4a lock item**, unchanged |
| R229 | **closed** — §1, the corpus runs in the suite; 4 of 28 remain, named |
| R230 | **closed** — §2, the ten layouts run in the suite |
| R231 | **open by instruction** — the platform finding; Q8 is with the supervisor |
| R232 | **closed** — this revision covers all five commits |
| R233 | **closed** — §3, taken from 4a; the enumeration is produced, not typed |

### Sites named by findings and not touched

Declared by exact site, each row saying what the line is.

| site | status |
|---|---|
| `CLAUDE.md` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `tests/corpus/tolerance_marker_exemptions.txt` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:108` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:109` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:110` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:114` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:115` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `tolerances.py` | **no change** -- R229 quotes it as evidence, not as a site to change |
| `__init__.py` | **no change** -- R230 quotes it as evidence, not as a site to change |
| `test_exempt_pair_responses.py` | **no change** -- R230 quotes it as evidence, not as a site to change |
| `tests/corpus/ci_ladder_gating.txt` | **no change** -- R230 quotes it as evidence, not as a site to change |
| `tests/verification/rung4/test_writer_round_trip.py:92` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:93` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:94` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:95` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:96` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:97` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:98` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:99` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:100` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:101` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:102` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `tests/verification/rung4/test_writer_round_trip.py:103` | **no change, and deliberately** -- this is the cross-platform golden question. Changing what it asserts is a plan edit (Q8) and it comes before code, not after |
| `docs/SUPERVISOR.md:63` | **no change** -- R232 quotes it as evidence, not as a site to change |
| `tests/verification/rung3/test_determinism_pins.py` | **no change** -- R233 quotes it as evidence, not as a site to change |

## 7. What I am asking for

**A PASS on CB0–CB2**, or a **HOLD naming the item.** R223, R224 and R231 stay
open by instruction, not by omission.

## 8. Witness and CI

CI at the previous commit: static, unit and rungs 1–3 green; **rung 4 red with
13 failures**, which is R231 and is untouched here. Rungs 5 and 6 have still
never executed on this branch. No `[witness ...]` comment yet.

---

# Revision 3 — four guards that could not report, and the jobs that never ran them

Answers: verdict 28 @ 8e7418f

**2026-09-09.** One commit since the twenty-eighth verdict: `4a8d2a3`.

## 0. Where this stands

R229 and R230 closed at the third verdict. **R231 stays open by instruction** —
the cross-platform golden question is Q8, with the technical supervisor, and
CB3 puts the plan edit before any code. R223 and R224 stay open for Q7 in the
same way. Nothing here touches either, and this revision does not claim it does.

Four items blocked and all four were the same shape: **a guard that could not
report what it found.**

## 1. R234 — a guard that took the suite with it

```
cell   a report with no verdict beside it, which is EVERY step boundary
out    before: `1 error`, ZERO of 1589 tests collected
       after:  1599 collected, 1 named failure, 1598 pass
judge  item 1b one level down and worse. 1b made a boundary red; this made it
       silent, and a suite that runs nothing looks exactly like a suite that
       has nothing to say.
cmd    python -m pytest tests/test_report_guard_states.py -q
out    7 passed -- all six of the reviewer's states, none a collection error,
       every failing state reported by a named test
```

Three changes. Module scope cannot raise: `_read` returns `""` for a missing
file, and the carry comparison runs against the newest **complete** pair so it
stays meaningful at the boundary. An empty parametrise is no longer a collection
error — `empty_parameter_set_mark = fail_at_collect` turned an unreadable
verdict into the same "no tests ran", so the list carries a placeholder that
fails **by name**. And `test_the_guard_reads_the_step_being_worked_on` carries
the pending-verdict message as one test while the rest of the file runs.

## 2. R235 — the guards had never run in CI

```
cmd    the eight paths ci.yml named, collected
out    1296 of 1589. The missing 293 are every top-level tests/*.py
judge  the tolerance scanner, the carry guard, the counter meta-test, the plan
       and figure checks and both new runners. Two commits said "in the suite,
       so in CI" about files no job had ever seen.
```

A `guards` job runs them. The claim is mechanical now rather than repeated:
`tests/test_ci_runs_the_whole_suite.py` parses the workflow, replays each run
step's arguments, and requires the union to be the whole suite.

```
cell   remove the guards job, one variable moved
out    326 of 1622 collected tests are run by no CI job
judge  not vacuous. Its FIRST version was: it kept only path tokens, so
       `pytest tests --ignore=...` contributed the bare token `tests` and the
       union was everything by construction -- the same defect it was written
       to find, recorded rather than quietly replaced.
```

## 3. R236, R237 — two sentences

**R236.** `ci.yml` said adding a test to a rung is not a CI edit. Under the
declared rule it is: the first test in an `empty:` rung makes the declaration
stale and the job fails. The comment now says what it costs — delete the marker
and change `empty:` to `full:` in the same commit — four lines above the block
that withdraws the previous version of the same claim.

**R237.** The scanner's "What is flagged" list promised any float threshold. It
reads `node.comparators` and never `node.left`, so `assert 0.05 > ratio` is
invisible. The sentence is fixed. Widening the reach is 4a's, and three of the
reviewer's new marker shapes are that species.

## 4. The three case files, absorbed

| file | entries | was |
|---|---|---|
| ladder layouts | 22 | 10 |
| marker shapes | 46 | 28 |
| guard states | 6 | new |

**The twelve new layouts found four defects in `run_rung.sh`**, each fixed: a
`full:` directory carrying a stale `.empty-by-design` marker, a rung whose every
test is skipped (pytest exits 0, and `CLAUDE.md` forbids a skip outright), a path
containing a space (the directory list was a string and the shell re-split it),
and a success line printed for a rung that had already failed.

**The four new marker misses are named, not counted.** Three are R237's
left-operand species, which is a gap in *detection* that no exemption rule can
reach. The fourth is the one-marker-one-node rule meeting its own limit: a single
`Compare` node holding the same literal twice is one node, so exempting it
exempts both.

```
cmd    python -m pytest -q
out    1626 passed, 0 failed, 0 skipped in 190.16s
cmd    ruff / black --check / mypy
out    All checks passed! / 68 files unchanged / Success: no issues in 25 files
```

## 5. Classified under BU0

| item | class | reason |
|---|---|---|
| R234, R235, R236, R237 | **blocking — a guard's reach and two published sentences** | answered, §1–§3 |
| R231 | **open by instruction** | Q8, with the technical supervisor |
| R223, R224 | **open by instruction** | Q7, same |
| R238, R239 | **4a by the reviewer, taken here** | the four `run_rung.sh` residues are fixed in §4; §3's filtered `out` is pasted now |
| R225–R228 | **4a**, unchanged | |

## 6. Carried

| item | status |
|---|---|
| R6 | **4a or later** - classified in section 5 |
| R16 | **4a or later** - classified in section 5 |
| R25 | **4a or later** - classified in section 5 |
| R30 | **4a or later** - classified in section 5 |
| R33 | **4a or later** - classified in section 5 |
| R36 | **4a or later** - classified in section 5 |
| R50 | **4a or later** - classified in section 5 |
| R52 | **4a or later** - classified in section 5 |
| R62 | **4a or later** - classified in section 5 |
| R63 | **4a or later** - classified in section 5 |
| R65 | **4a or later** - classified in section 5 |
| R68 | **4a or later** - classified in section 5 |
| R76 | **4a or later** - classified in section 5 |
| R79 | **4a or later** - classified in section 5 |
| R80 | **4a or later** - classified in section 5 |
| R95 | **4a or later** - classified in section 5 |
| R97 | **4a or later** - classified in section 5 |
| R98 | **4a or later** - classified in section 5 |
| R100 | **4a or later** - classified in section 5 |
| R103 | **4a or later** - classified in section 5 |
| R113 | **4a or later** - classified in section 5 |
| R124 | **4a or later** - classified in section 5 |
| R129 | **4a or later** - classified in section 5 |
| R131 | **4a or later** - classified in section 5 |
| R132 | **4a or later** - classified in section 5 |
| R134 | **4a or later** - classified in section 5 |
| R139 | **4a or later** - classified in section 5 |
| R148 | **4a or later** - classified in section 5 |
| R151 | **4a or later** - classified in section 5 |
| R152 | **4a or later** - classified in section 5 |
| R159 | **4a or later** - classified in section 5 |
| R162 | **4a or later** - classified in section 5 |
| R170 | **4a or later** - classified in section 5 |
| R171 | **4a or later** - classified in section 5 |
| R172 | **4a or later** - classified in section 5 |
| R181 | **4a or later** - classified in section 5 |
| R189 | **4a or later** - classified in section 5 |
| R190 | **4a or later** - classified in section 5 |
| R198 | **4a or later** - classified in section 5 |
| R199 | **4a or later** - classified in section 5 |
| R200 | **4a or later** - classified in section 5 |
| R215 | **4a or later** - classified in section 5 |
| R216 | **4a or later** - classified in section 5 |
| R220 | **4a or later** - classified in section 5 |
| R222 | **4a or later** - classified in section 5 |
| R223 | **open** — G2.1's quantity is Q7 |
| R224 | **open** — answered with Q7's plan edit |
| R225 | **4a or later** - classified in section 5 |
| R226 | **4a or later** - classified in section 5 |
| R227 | **4a or later** - classified in section 5 |
| R228 | **4a or later** - classified in section 5 |
| R229 | **closed** at the third verdict |
| R230 | **closed** at the third verdict |
| R231 | **open by instruction** — Q8 is with the technical supervisor |
| R232 | **closed** in revision 2 |
| R233 | **closed** in revision 2 |
| R234 | **closed** — §1, the guard reports instead of dying |
| R235 | **closed** — §2, a `guards` job plus a mechanical coverage check |
| R236 | **closed** — §3, the sentence says what the declared rule costs |
| R237 | **closed** — §3, the contract; the reach is 4a |
| R238 | **closed** — §4, all four residues, found by the new layouts |
| R239 | **closed** — §3's `out` is pasted rather than summarised |

### Sites named by findings and not touched

Declared by exact site, each row saying what the line is.

| site | status |
|---|---|
| `CLAUDE.md` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:314` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:315` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:316` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-6.md` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `step-4.md` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `step-6.md` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `tests/corpus/report_guard_states.txt` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:62` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:63` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:64` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:65` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:84` | **no change** -- R234 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:243` | **no change** -- R235 quotes it as evidence, not as a site to change |
| `__init__.py` | **no change** -- R236 quotes it as evidence, not as a site to change |
| `test_r6.py` | **no change** -- R236 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:53` | **no change** -- R236 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:54` | **no change** -- R236 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:55` | **no change** -- R236 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:56` | **no change** -- R236 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:57` | **no change** -- R236 quotes it as evidence, not as a site to change |
| `tests/corpus/tolerance_marker_exemptions.txt` | **no change** -- R237 quotes it as evidence, not as a site to change |
| `tests/verification/rung3/test_basis_constants.py:192` | **no change** -- R237 quotes it as evidence, not as a site to change |
| `tests/verification/rung4/test_reference_provenance.py:30` | **no change** -- R237 quotes it as evidence, not as a site to change |
| `tests/corpus/ci_ladder_gating.txt` | **no change** -- R238 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:279` | **no change** -- R239 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:280` | **no change** -- R239 quotes it as evidence, not as a site to change |

## 7. What I am asking for

**A PASS on CC**, or a **HOLD naming the item.** R223, R224 and R231 are open by
instruction and are not offered as answered.

## 8. CI

At the previous commit: static, unit and rungs 1–3 green; **rung 4 red with the
same 13 platform failures**, which is R231. Rungs 5 and 6 have still never run.
The `guards` job is new and runs for the first time on this commit.



---

# Revision 4 — status is the verdict's to give, and one was taken

Answers: verdict 29 @ 476f909

**2026-09-09.** Commits since the twenty-ninth verdict, listed in §6.

## 0. The one that matters

**I recorded an item as closed at a verdict whose own text said it was not.**
The third verdict reads *"MECHANISM VERIFIED, CLOSING CONDITION NOT MET.
Carried, not closed."* Revision 3 wrote `closed at the third verdict` twice.
**R230 is reopened by name and is OPEN.**

Nothing could have caught it. A status is prose, and the carry guard's own
docstring says it never checks whether the status beside an item is true. So the
fix is not a better checker.

**CC1: the word is gone.** A report says what it DID — *answered*, *open*,
*withdrawn*. Only a verdict says *closed*. Taking the strongest word away from
the party that does not get to use it removes the failure mode instead of
detecting it.

```
cmd    python -m pytest tests/test_report_carried.py -q, at revision 3
out    62 status cells parsed, 10 say `closed`  -- FAILED
rule   `test_a_report_does_not_say_CLOSED`, and its other half
       `test_every_carried_item_carries_one_of_the_report_words`, so banning a
       word cannot become saying nothing
```

## 1. CD1 — the guard states, bounded

**R243, the shallow clone.** `_changed_lines()` never read git's return code, so
a diff against a commit the clone does not contain returned empty — which reads
exactly like *the step changed nothing*, and 23 site checks passed for that
reason on every shallow checkout.

```
cell   one machine, one commit, one variable
out    full clone `122 passed`; `git clone --depth 1` `23 failed, 99 passed`
fix    `fetch-depth: 0` on all nine checkouts, and the git failure is REPORTED
rule   reported by a NAMED test, not raised: a raise at module scope is R234
       again -- the import dies and none of the file is collected
```

**R246, the step number.** `str.isdigit()` admits a strictly larger set than
`int()` accepts, so a superscript one passed the filter and raised inside the
comprehension, taking the suite down at collection.

```
cmd    a superscript-digit report file present, before and after
out    before: `Interrupted: 1 error`, zero of 1656 tests
       after:  `121 passed` -- the file is stepped over
judge  the repair before this one caught `OSError` because `OSError` was the
       failure it had already seen. The pattern is `[0-9]+` now, and the
       docstring no longer says "never raises".
```

**R247, the detector.** The harness certifying R234 could not tell a collection
error from an all-red run: it searched stdout for a word, and its mirror
`or "passed" in log` disabled the check entirely as soon as anything passed. It
reads pytest's junit report now, and *did not collect* and *everything failed*
are two assertions.

## 2. CD1's boundary, and what goes to 4a

CD1 bounds this deliberately: the guard's job is to make a false status and a
missing commit impossible, not to survive every shape written in a round. **A
guard that grows a case per round never converges.**

| state | class | reason |
|---|---|---|
| shallow clone | **blocking — the guard's claim** | answered, §1. Its corpus row requires `green`; the repaired guard reports a NAMED failure instead, because a guard that cannot see the diff and says nothing is the defect. Recorded as a requirement disagreement, the fourth |
| verdict amended after the answered commit | **blocking — the guard's claim** | the guard reads the verdict from git at the answered sha, so a working-copy edit must change nothing |
| superscript digit, empty step number, draft suffix, non-numeric suffix | **answered** | one pattern covers all four |
| reports and reviews directories renamed away; report or verdict is a directory; two reports ahead of the verdict; a non-commit `Answers:` sha | **4a by name** | each is a distinct filesystem shape and none of them can produce a FALSE status or hide a missing commit, which is the bound CD1 sets |

## 3. CD3 — what the 34 reds at the reviewed commit are

**Neither golden growth nor product failures.** They are the reviewer's new
cases arriving faster than the runners that read them: the corpus grew by 38
entries and my `LAYOUTS`, `STATES` and `KNOWN_MISSES` covered the old set.

```
cmd    the reds at 476f909, by file
out    12 marker shapes, 10 guard states, 9 ladder layouts, 1 site declaration
judge  every one is a case the runner does not yet build, not a defect in what
       the case tests. BY1 asks the reviewer to carry regeneration in the corpus
       commit; there is nothing to regenerate here -- no golden and no figure
       moves -- so BY1 is not engaged. What the round shows instead is that a
       corpus commit lands red by construction, which is what BE3 intends.
```

## 4. CD2 — two shapes that are the rule itself

Two of the reviewer's new scanner shapes are the two clauses of `CLAUDE.md`
§ Tolerances written out literally, and both scanned clean. That is a hole in
the claim rather than in the reach, and it is fixed; both are the scanner's
negative controls now.

## 5. Q8 — locked, and what it does not yet license

**`5697b2a`, re-locked.** CI is canonical for the golden files, for every
tolerance whose measured basis is platform-dependent, and for
`docs/milestones/F2_figures.md`. Each canonical file carries its version stamp
inside itself, so a mismatch is visible where the number is read; the stamp is
what enforces the rule.

**Two directives in the same turn disagreed about whether it was locked**, one
recording it confirmed and the next asking for Xabier's word. I stopped and
asked rather than choosing, because a plan edit under an ambiguous lock is the
error this milestone exists to punish. The confirmation came and the edit is in.

**What it does not license yet.** The sequence puts the measurements after this
edit and after the guard findings: the drift tolerance measured at `2.6e9` ULP
on the runner, and the four figure rows that do not reproduce there, stay
unwritten until they are measured on CI under this Q&A. Nothing here writes a
value.

## 6. Carried

| item | status |
|---|---|
| R223 | **open by instruction** — Q7 |
| R224 | **open by instruction** — Q7 |
| R225 | **open** - 4a or a later step |
| R228 | **open** - 4a or a later step |
| R230 | **open — REOPENED BY NAME.** Revision 3 gave it a status only a verdict may give, against that verdict's own words; §0 |
| R231 | **open** — Q8 is locked; the measurement comes next |
| R232 | **answered** in revision 2 |
| R233 | **answered** in revision 2 |
| R234 | **answered** — §1, the failure is a named test, not a dead import |
| R235 | **answered** in the previous revision |
| R236 | **answered** in the previous revision |
| R237 | **answered** in the previous revision |
| R238 | **answered** in the previous revision |
| R239 | **answered** in the previous revision |
| R240 | **open** — the `guards` job is red; the reds are §3 |
| R241 | **withdrawn by me** — the sentence claimed a first run that had already happened and finished red |
| R242 | **answered** — §0, and CC1 removes the word |
| R243 | **answered** — §1, `fetch-depth: 0` and the return code read |
| R244 | **open** — Q8 is locked; the drift tolerance is measured on CI under it before any value is written |
| R245 | **open** — the four moving figures, same route |
| R246 | **answered** — §1, `[0-9]+` and `int()` |
| R247 | **answered** — §1, junit rather than substrings |
| R248 | **open** - 4a or a later step |
| R249 | **open** - 4a or a later step |
| R250 | **open** - 4a or a later step |
| R251 | **open** - 4a or a later step |
| R252 | **open** - 4a or a later step |

### Sites named by findings and not touched

Declared by exact site, each row saying what the line is.

| site | status |
|---|---|
| `test_counters_are_injected.py` | **no change** -- R240 quotes it as evidence, not as a site to change |
| `test_plan_figures.py` | **no change** -- R240 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:651` | **no change** -- R241 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:652` | **no change** -- R241 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:653` | **no change** -- R241 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:654` | **no change** -- R241 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:442` | **no change** -- R242 quotes it as evidence, not as a site to change |
| `tests/corpus/report_guard_states.txt` | **no change** -- R243 quotes it as evidence, not as a site to change |
| `floatfea/tolerances.py:713` | **no change, and deliberately** -- the value is measured on CI under Q8 before it is written, and that measurement is next |
| `tests/regression/test_exempt_pair_responses.py:109` | **no change, and deliberately** -- the value is measured on CI under Q8 before it is written, and that measurement is next |
| `tests/test_counters_are_injected.py:170` | **no change, and deliberately** -- the value is measured on CI under Q8 before it is written, and that measurement is next |
| `F2_figures.md` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `docs/milestones/F2_figures.md` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `docs/milestones/F2_figures.md:34` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `docs/milestones/F2_figures.md:35` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `docs/milestones/F2_figures.md:36` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `docs/milestones/F2_figures.md:37` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `docs/milestones/F2_figures.md:38` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:113` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:114` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:115` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:116` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:117` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:118` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:119` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:120` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:121` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:122` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:123` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:124` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:125` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:126` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:127` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:128` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:129` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:130` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:131` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:132` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:133` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:134` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:135` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:136` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:137` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:138` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:139` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:140` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:141` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:142` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:143` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:144` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:145` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:146` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `scripts/regen_figures.py:147` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `tests/test_plan_figures.py:73` | **no change, and deliberately** -- the four figures are regenerated on CI under Q8, same reason |
| `tests/test_report_guard_states.py:135` | **no change** -- R247 quotes it as evidence, not as a site to change |
| `CLAUDE.md` | **no change** -- R248 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh` | **no change** -- R248 quotes it as evidence, not as a site to change |
| `tests/corpus/ci_ladder_gating.txt` | **no change** -- R248 quotes it as evidence, not as a site to change |
| `tests/corpus/tolerance_marker_exemptions.txt` | **no change** -- R249 quotes it as evidence, not as a site to change |
| `tests/test_ci_runs_the_whole_suite.py` | **no change** -- R250 quotes it as evidence, not as a site to change |
| `tests/verification/rung5/test_uncovered.py` | **no change** -- R250 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-6-draft.md` | **no change** -- R251 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:69` | **no change** -- R251 quotes it as evidence, not as a site to change |
| `regen_figures.py` | **no change** -- R252 quotes it as evidence, not as a site to change |
| `scripts/regen_figures.py:327` | **no change** -- R252 quotes it as evidence, not as a site to change |
| `scripts/regen_figures.py:328` | **no change** -- R252 quotes it as evidence, not as a site to change |
| `scripts/regen_figures.py:329` | **no change** -- R252 quotes it as evidence, not as a site to change |
| `scripts/regen_figures.py:330` | **no change** -- R252 quotes it as evidence, not as a site to change |
| `scripts/regen_figures.py:331` | **no change** -- R252 quotes it as evidence, not as a site to change |
| `scripts/regen_figures.py:332` | **no change** -- R252 quotes it as evidence, not as a site to change |

## 7. What I am asking for

**A PASS on CD0–CD4**, or a **HOLD naming the item and the head.** R231, R244
and R245 are open pending the CI measurements Q8 now licenses; R223 and R224 are
open pending Q7; R230 is open by my own error.

---

# Revision 5 — one interpreter, and CI stops being invisible

Answers: verdict 30 @ 1b93db0

**2026-09-09.** Commits since the thirtieth verdict, listed in §6.

## 0. CI at the reviewed commit `fa3b070`

**Mandatory from CE1, and the reason it is mandatory is that this table would
have been the shortest route to the round's headline.** Run `34408014924`.

| job | passed | failed | skipped |
|---|---|---|---|
| lint and type-check | 1 | 0 | 0 |
| unit tests | 88 | 0 | 0 |
| guards and meta-tests | 386 | 4 | 0 |
| ladder 1 -- the solver is a solver | 1013 | 0 | 0 |
| ladder 2 -- the element is the element | 1 | 0 | 0 |
| ladder 3 -- the model is the platform | 106 | 0 | 0 |
| ladder 4 -- the loads are the loads | 72 | 13 | 0 |
| ladder 5 -- independent confirmation | 0 | 0 | 0 |
| ladder 6 -- it stays fixed | 0 | 0 | 0 |

The two ladder jobs with nothing in them did not run: they are `needs:`-gated
behind ladder 4, which is R231. `lint and type-check` and `ladder 2` report a
step outcome rather than a test count.

**Three of the four guard failures are R244 and R245**, routed to Q8. **The
fourth was mine**, and §1 is about it.

`tests/test_report_carried.py` fails a report with no such table, and one whose
rows are all zeros. A red CI that no report mentions is a red CI nobody reads,
and it went unmentioned at three consecutive reviewed commits.

## 1. CE0 — the environment was three things

```
was    requires-python ">=3.11"; runner 3.11.16; implementer 3.13
wrote  shutil.rmtree(..., onexc=...)   -- `onexc` arrived in 3.12
judge  green locally, green in review, red on the runner -- in the ONE test that
       measures the shallow-clone repair, which is to say the one place that
       could only be checked on the machine where the shallow clone was found
```

Nothing detected it. `ruff` reads syntax and the call is valid syntax at every
version; the type checker was pointed at `floatfea/` and the call was in
`tests/`.

**`requires-python` pins one minor version now, every CI job runs it, and
`tests/test_the_pinned_interpreter.py` type-checks the tree at the pinned
version and at the running one and takes the difference.** An error that appears
only under the pin is a use of something the pin does not have. Self-calibrating,
so there is no baseline to go stale.

```
cell   the guard, against the call that started this
out    `Unexpected keyword argument "onexc"` at 3.11, absent at 3.13 -- caught
cell   the same guard after the fix
out    empty difference
judge  it also found four FALSE positives from `deterministic_v0 -> object`; a
       vague annotation is noise a detector has to be tuned around, so the
       annotation is fixed rather than the detector loosened
```

**What CE0 asked for and I could not do: install the pinned interpreter
locally.** Only 3.13 and 3.14 are on this machine and installing one is not
mine to do. The difference-guard is what covers the gap, and it covers the
class rather than the instance.

## 2. CE2 — the ablation asserts the diagnosis

`assert code != 0` was satisfied by the repair **and by its absence**: with the
return-code branch removed the shallow clone still exits non-zero, with sixteen
site failures instead of one named diagnosis.

**The harness now asserts the pair**: the named diagnosis must fail, and the
tests that defer to it must not. Removing the branch turns the deferring tests
red, which is a different set, so the assertion distinguishes the two states
that `code != 0` conflated.

## 3. CE3 — the vocabulary, the trade, and the arm that could not fire

**The vocabulary leaked four ways of five.** It read raw cell text and only the
last cell. It reads markdown-stripped text across every cell now, the forbidden
set is enumerated with synonyms, and the contradiction domain is every finding
the verdict names rather than the three lines that used a phrase.

**The trade was ruled against me and the ruling is better than either option I
offered.** I framed it as node-keying versus value-keying. Value-keying **plus
one more marker comment in each of the two bracket statements** leaves both
files clean, measured, at a cost of two comment lines — and node-keying
reinstated the earlier hole one level down, where only the lower bound of a
bracket is deliberate and the upper one rides free.

**And the `xpassed` arm could never be fed**: the filter that supplies it listed
four outcomes and not that one, so an xfail-only rung whose test unexpectedly
passes exited zero and reported success.

## 4. My own ratio rule, withdrawn

The known-miss list is bounded by `no false pass on a real file` now, not by a
ratio against the corpus.

```
judge  the rule compared the miss count with the SIZE of an adversarial corpus,
       and the reviewer writes that corpus. It grew faster than the fixes, so
       the rule fired on the reviewer's effort rather than on the guard's reach
cell   what firing pushed me toward: scanning every expression that merely
       CONTAINS a float
out    seven correct files reddened. Rejected, and recorded rather than quietly
       dropped
rule   every miss carries its species, and the scanner is clean over every file
       under `tests/` at every commit -- which is asserted by a different test
       and is the thing that actually matters
```

## 5. Q8 — two clauses not yet true

The plan text was ruled correct and leaving the values unwritten was ruled
right. Two clauses are not yet true of the repository and both must land before
any Q8 value is written: **there is no lockfile** (`numpy>=1.26`, `scipy>=1.11`
are floors), and **the basis for the number `2` is not published in the
quantity the rule uses** — the round-trip test prints an absolute
`max |diff| = 1.110e-16`, not a ULP fraction of channel amplitude.

## 6. Carried

| item | status |
|---|---|
| R223 | **open** — Q7 |
| R224 | **open** — Q7 |
| R225 | **open** - 4a or a later step |
| R228 | **open** - 4a or a later step |
| R230 | **open** — reopened by name in revision 4 |
| R231 | **open** — Q8's CI measurement |
| R232 | **open** - 4a or a later step |
| R233 | **open** - 4a or a later step |
| R237 | **open** - 4a or a later step |
| R240 | **open** — §0 carries the counts; three of four are Q8's |
| R241 | **withdrawn by me** in revision 4 |
| R242 | **answered** in revision 4 |
| R243 | **answered** in revision 4, and its ablation is §2 |
| R244 | **open** — Q8's CI measurement |
| R245 | **open** — Q8's CI measurement |
| R246 | **answered** in revision 4 |
| R247 | **answered** in revision 4 |
| R248 | **answered** — §1, the interpreter is pinned and the class is guarded |
| R249 | **answered** — §2, the ablation asserts the diagnosis |
| R250 | **open** — the unasserted reference set in the coverage check, 4a |
| R251 | **answered** — §3, the vocabulary reads stripped text across all cells |
| R252 | **answered** — §3, the contradiction domain is every finding |
| R253 | **answered** — §3, value-keying plus two marker comments |
| R254 | **answered** — §3, the `xpassed` arm can be fed |
| R255 | **answered** — §0, the report carries CI per job |
| R256 | **open** — the rung-6 prose and corpus sites, 4a |
| R257 | **open** — 4a |
| R258 | **open** — 4a |
| R259 | **open** — 4a |
| R260 | **open** — 4a |
| R261 | **open** — 4a |
| R262 | **open** — 4a |
| R263 | **open** — 4a |
| R264 | **open** — 4a |
| R265 | **open** — 4a |
| R266 | **open** — 4a |

### Sites named by findings and not touched

Declared by exact site, each row saying what the line is.

| site | status |
|---|---|
| `test_report_carried.py:186` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `test_report_carried.py:479` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `test_report_carried.py:480` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `test_report_carried.py:481` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `test_report_carried.py:482` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `test_report_carried.py:483` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `test_report_carried.py:484` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/corpus/report_guard_states.txt` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:276` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:277` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:278` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:279` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:280` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:281` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:282` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:283` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:284` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:285` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:286` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:287` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:288` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:289` | **no change** -- R254 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:29` | **no change** -- R255 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:30` | **no change** -- R255 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:31` | **no change** -- R255 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:32` | **no change** -- R255 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:33` | **no change** -- R255 quotes it as evidence, not as a site to change |
| `run_rung.sh:5` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:11` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:12` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:13` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:53` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:54` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:55` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:56` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:57` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:231` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:232` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:233` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_ladder_gating.py:234` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `test_ci_runs_the_whole_suite.py` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `tests/verification/rung6/__init__.py` | **no change** -- R256 quotes it as evidence, not as a site to change |
| `CLAUDE.md` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `docs/milestones/F2.md` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:154` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:155` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:156` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:157` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:158` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:159` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:160` | **no change** -- R257 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:713` | **no change** -- R258 quotes it as evidence, not as a site to change |
| `tests/corpus/report_status_vocabulary.txt` | **no change** -- R259 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:288` | **no change** -- R259 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:138` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:140` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:141` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:142` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:143` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:144` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:145` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:146` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `tests/corpus/ci_ladder_gating.txt` | **no change** -- R260 quotes it as evidence, not as a site to change |
| `F2_figures.md` | **no change** -- R261 quotes it as evidence, not as a site to change |
| `tests/verification/rung4/test_writer_round_trip.py:100` | **no change** -- R261 quotes it as evidence, not as a site to change |
| `tests/corpus/tolerance_marker_exemptions.txt` | **no change** -- R262 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:326` | **no change** -- R264 quotes it as evidence, not as a site to change |
| `step-0006.md` | **no change** -- R265 quotes it as evidence, not as a site to change |
| `step-01.md` | **no change** -- R265 quotes it as evidence, not as a site to change |
| `step-06.md` | **no change** -- R265 quotes it as evidence, not as a site to change |
| `step-6.md` | **no change** -- R265 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:85` | **no change** -- R265 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:820` | **no change** -- R266 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:821` | **no change** -- R266 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:822` | **no change** -- R266 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:823` | **no change** -- R266 quotes it as evidence, not as a site to change |

## 7. What I am asking for

**A PASS on CE0–CE3**, or a **HOLD naming the item and the head.** R231, R244
and R245 are open pending the Q8 measurements; R223 and R224 pending Q7; R230
open by my own error.


---

# Revision 6 — the table is built from the verdict, and two redirections

Answers: verdict 31 @ b470aee

**2026-09-09.** Commits since the thirty-first verdict, listed in §7.

## 0. CI at the reviewed commit `a59521e`

Run `34424766023`.

| job | passed | failed | skipped |
|---|---|---|---|
| lint and type-check | 1 | 0 | 0 |
| unit tests | 88 | 0 | 0 |
| guards and meta-tests | 425 | 1 | 0 |
| ladder 1 -- the solver is a solver | 1013 | 0 | 0 |
| ladder 2 -- the element is the element | 1 | 0 | 0 |
| ladder 3 -- the model is the platform | 106 | 0 | 0 |
| ladder 4 -- the loads are the loads | 72 | 13 | 0 |
| ladder 5 -- independent confirmation | 0 | 0 | 0 |
| ladder 6 -- it stays fixed | 0 | 0 | 0 |

Both reds are open by instruction. The guards job moved `4 failed / 386 passed`
to `1 failed / 425 passed`.

## 1. R267 — the table, and how it got wrong

**I wrote statuses for a block of findings without reading what each one said.**
Six rows attached this step's work to numbers naming different items, and four
of eight blocking items were recorded at 4a. A report may say it has not
answered an item; it may not re-file the verdict's ruling about which step the
item belongs to.

**The table is generated from the verdict now**, and two tests hold it:

```
rule   `test_a_blocking_item_is_not_routed_to_4a` -- the verdict's own
       `(BLOCKS ...)` headings are the domain, so the classification is read
       rather than remembered
rule   `test_the_answered_verdict_is_the_NEWEST_one` -- item 1b, mechanically.
       A header naming a real but OLDER verdict passed every check: the sha
       resolves, the findings parse, and the carry table is complete about a
       list that has been superseded
out    both fire on revision 5, which is how they were checked
```

## 2. CF0 — the guard is retired, and the pin moved to the interpreter that exists

**CE0's guard asserted nothing in the configuration it was built to reach.** It
returned early when the pinned and running versions coincide, which is all nine
CI jobs and is also the state CE0 asks for locally: anti-correlated with its own
goal.

**The answer was not a better guard.** `requires-python`, `ruff`, `black`,
`mypy` and every CI job are on **3.13**, which is the interpreter installed on
this machine. There is now one version, so there is no mismatch to detect, and
`tests/test_the_pinned_interpreter.py` is deleted rather than repaired.

`xfail_strict = true` is in `pyproject.toml` — one line, and the never-xfail
rule becomes the runner's rather than something each caller passes.

## 3. CF1 — CI determinism is a precondition of Q8, and it is not established

**This is the finding that outranks the rest, and it is the reviewer's.** One
regression test went `PASS, FAIL, FAIL, PASS` across four consecutive runs with
the deciding files byte-identical between them. They withdrew their own `2.6e9`
figure as a basis, and were right to: it came from one of the two failing runs.

**Q8 says CI is canonical. That assumes CI agrees with itself.** A `determinism`
job now runs the figure regeneration and the regression rung **ten times on ten
separate runners**, printing the CPU model and the numpy build configuration
beside each result.

**It is expected to fail.** The likely mechanism is that hosted runners are
different machines and BLAS picks its kernel from the CPU it finds, so the last
bit of a factorisation depends on which machine the job drew. Threads are pinned;
the kernel is not. When the correlation is measured the kernel gets pinned too,
and the job has to reach ten of ten before any Q8 value is written.

**No Q8 value is written here**, and the withdrawn figure stays withdrawn.

## 4. R269–R274 — six answered, each at its own site

```
R269  the scanner's "What is flagged" list has now been wrong in BOTH
      directions: it said "any float threshold" while only the right operand
      was read, and after the left operand was read it still said it was not.
      It describes the scanner now, and what is NOT read is listed by species
      in the corpus runner rather than described in prose
R271  three of four formattings still went past. `_ROW` and `_status_cells`
      are the edit revision 5 SAID it made: the first cell may be bolded or
      backticked, and every cell after it is read
R272  `@pytest.mark.xfail(strict=False)` overrides the ini setting, so the
      shape survived `xfail_strict`. The rung reads pytest's FIRST summary
      line -- printed before any `atexit` output, so a later forgery cannot
      displace it -- and an xpass is a failure there
R273  the second clause: the message no longer tells its reader that a real
      commit "is not a commit in this repository" when the cause is a shallow
      clone
R274  the vacuous bound is replaced by the escape golden -- the escape set is
      enumerated by species and asserted EQUAL to the measurement, so it goes
      red on a new escape and on a fixed one
R276  the `DIAGNOSIS` entry that an earlier `return` made unreachable: the
      ablation is a helper called from both branches now
```

## 5. R270 — two figures withdrawn rather than republished

The two figure rows that do not reproduce on CI are **withdrawn from this
report's prose**. They are not republished with a caveat and they are not
quietly left: under Q8 they are CI's to produce, and CI has not yet been shown
to produce them twice the same way. That is §3.

## 6. What is open, and why

| item | why it is open |
|---|---|
| R275 | the alternating measurement. CF1's job must reach ten of ten first |
| R231, R244, R245 | the Q8 values, which R275 blocks |
| R223, R224 | Q7, which follows Q8 |
| R230 | reopened by my own error at revision 4 |
| R277–R281 | recordable at 4a in the verdict's own classification |

## 7. Carried

| item | status |
|---|---|
| R223 | **open** — carried from an earlier verdict |
| R224 | **open** — carried from an earlier verdict |
| R225 | **open** — carried from an earlier verdict |
| R228 | **open** — carried from an earlier verdict |
| R230 | **open** — carried from an earlier verdict |
| R231 | **open** — carried from an earlier verdict |
| R232 | **open** — carried from an earlier verdict |
| R233 | **open** — carried from an earlier verdict |
| R244 | **open** — carried from an earlier verdict |
| R245 | **open** — carried from an earlier verdict |
| R248 | **open** — carried from an earlier verdict |
| R249 | **open** — carried from an earlier verdict |
| R250 | **open** — carried from an earlier verdict |
| R251 | **open** — carried from an earlier verdict |
| R252 | **open** — carried from an earlier verdict |
| R253 | **open** — carried from an earlier verdict |
| R254 | **open** — carried from an earlier verdict |
| R255 | **open** — carried from an earlier verdict |
| R256 | **open** — carried from an earlier verdict |
| R257 | **open** — carried from an earlier verdict |
| R258 | **open** — carried from an earlier verdict |
| R259 | **open** — carried from an earlier verdict |
| R260 | **open** — carried from an earlier verdict |
| R261 | **open** — carried from an earlier verdict |
| R262 | **open** — carried from an earlier verdict |
| R263 | **open** — carried from an earlier verdict |
| R264 | **open** — carried from an earlier verdict |
| R265 | **open** — carried from an earlier verdict |
| R266 | **open** — carried from an earlier verdict |
| R267 | **answered** — §1, the table is generated from the verdict |
| R268 | **answered** — §2, the guard is retired and the pin moved to 3.13 |
| R269 | **answered** — §4, the list describes the scanner |
| R270 | **answered** — §5, both figure rows taken out of the prose |
| R271 | **answered** — §4, the edit revision 5 claimed |
| R272 | **answered** — §4, the first summary line, and `xfail_strict` |
| R273 | **answered** — §4, the second clause of the message |
| R274 | **answered** — §4, the escape golden replaces it |
| R275 | **open** — §3, CF1 must reach ten of ten first |
| R276 | **answered** — §4, the ablation is reachable from both branches |
| R277 | **open** — recordable at 4a in the verdict's own classification |
| R278 | **open** — recordable at 4a in the verdict's own classification |
| R279 | **open** — recordable at 4a in the verdict's own classification |
| R280 | **open** — recordable at 4a in the verdict's own classification |
| R281 | **open** — recordable at 4a in the verdict's own classification |

### Sites named by findings and not touched

Declared by exact site, each row saying what the line is.

| site | status |
|---|---|
| `.claude/agents/gating-supervisor.md` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `CLAUDE.md` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1043` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1044` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1045` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1046` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1047` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1048` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1049` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1050` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1051` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1052` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1053` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1054` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1055` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1056` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1057` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1058` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1059` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1060` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1061` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1062` | **no change** -- R267 quotes it as evidence, not as a site to change |
| `test_report_guard_states.py:247` | **no change** -- R268 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1104` | **no change** -- R269 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1105` | **no change** -- R269 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1106` | **no change** -- R269 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1107` | **no change** -- R269 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1108` | **no change** -- R269 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:713` | **no change** -- R270 quotes it as evidence, not as a site to change |
| `tests/corpus/report_status_vocabulary.txt` | **no change** -- R271 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:325` | **no change** -- R271 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:125` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:126` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:127` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:128` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:129` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:130` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:131` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `tests/corpus/ci_ladder_gating.txt` | **no change** -- R272 quotes it as evidence, not as a site to change |
| `docs/SUPERVISOR.md` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `floatfea/determinism.py` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `floatfea/tolerances.py` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `step-06.md` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `test_no_tolerance_literals.py:362` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `test_no_tolerance_literals.py:363` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `test_no_tolerance_literals.py:364` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_marker_exemption_corpus.py:210` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_marker_exemption_corpus.py:211` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_marker_exemption_corpus.py:212` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_marker_exemption_corpus.py:213` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_marker_exemption_corpus.py:214` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_marker_exemption_corpus.py:215` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_marker_exemption_corpus.py:216` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:362` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:363` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:364` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:365` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:366` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:367` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:368` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:369` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_no_tolerance_literals.py:370` | **no change** -- R274 quotes it as evidence, not as a site to change |
| `tests/test_counters_are_injected.py` | **no change** -- R275 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:132` | **no change** -- R276 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:133` | **no change** -- R276 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:134` | **no change** -- R276 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:135` | **no change** -- R276 quotes it as evidence, not as a site to change |
| `tests/corpus/report_ci_section.txt` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:436` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:437` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:438` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:439` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:440` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:441` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:442` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:443` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:444` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:445` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:446` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:447` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:448` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:449` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:450` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:451` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:452` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:453` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:454` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:455` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:456` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:457` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:458` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:459` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:460` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:461` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:462` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:463` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:464` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:465` | **no change** -- R277 quotes it as evidence, not as a site to change |
| `tests/corpus/pinned_interpreter.txt` | **no change** -- R278 quotes it as evidence, not as a site to change |
| `test_a.py` | **no change** -- R279 quotes it as evidence, not as a site to change |
| `test_b.py` | **no change** -- R279 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:255` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:256` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:257` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:258` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:259` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:260` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:261` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:262` | **no change** -- R280 quotes it as evidence, not as a site to change |
| `tests/test_ci_ladder_gating.py:263` | **no change** -- R280 quotes it as evidence, not as a site to change |

## 8. What I am asking for

**A PASS on CF0, CF2, CF3 and CF4**, or a **HOLD naming the item and the head.**
CF1 is running and its result gates Q8; nothing here writes a Q8 value.

---

# Revision 7 — the job compares, the generator exists, and the pin is in the plan

Answers: verdict 32 @ 49c8449

**2026-09-10.** Commits since the thirty-second verdict, listed in §6.

## 0. CI at the reviewed commit `73cf6ce`

| job | passed | failed | skipped |
|---|---|---|---|
| lint and type-check | 1 | 0 | 0 |
| unit tests | 88 | 0 | 0 |
| guards and meta-tests | 481 | 1 | 0 |
| ladder 1 -- the solver is a solver | 1013 | 0 | 0 |
| ladder 2 -- the element is the element | 1 | 0 | 0 |
| ladder 3 -- the model is the platform | 106 | 0 | 0 |
| ladder 4 -- the loads are the loads | 72 | 13 | 0 |
| ladder 5 -- independent confirmation | 0 | 0 | 0 |
| ladder 6 -- it stays fixed | 0 | 0 | 0 |
| CI determinism -- 10 runners | 10 | 0 | 0 |

Both reds are the sine and cosine round-trip comparisons, open under Q8.

## 1. R284 — the determinism job agreed with itself

**It regenerated the figures and then hashed what it had just written.** So it
agreed on every runner, and would have agreed with a committed file replaced by
one line of garbage — the reviewer ran exactly that and the job went green. The
decoupling was visible in the live run: ten legs reported the regression rung
passing while the guards job in the same run reported the figures stale.

**It compares now.** The committed file is hashed *before* anything touches it,
then `regen_figures.py --check` compares a fresh render against what is
committed, and the post-render hash is printed beside the first.

```
rule   `--check` returns non-zero when the rendered file differs from the
       committed one, so the leg fails instead of agreeing with itself
judge  the ten-of-ten result stands as evidence that the RENDER is stable
       across runners. It was never evidence that the render matches what is in
       the repository, and this revision does not claim the old job showed that.
```

## 2. R285 — the pin belongs in the plan, and the measurement with it

Q8 named "Linux, with Python, numpy and scipy pinned in a lockfile" as the
canonical environment. **A lockfile does not pin the BLAS kernel**, and the
kernel is what the split was. Deleting one `env:` line leaves the guard suite
entirely green, so nothing in the repository would have noticed its removal.

The plan carries the condition and the measurement now, through the re-lock
route. The numbers are in `docs/milestones/F2.md`, not only here.

## 3. R282 — the check I added is the mechanism the record says was rejected

`.claude/agents/gating-supervisor.md` item 1b records, in terms, that comparing
against the newest verdict made a step boundary permanently red and that the one
thing a machine cannot check is that line. **I reinstated it, and it reddened
the suite at the commit the verdict was written at.**

**The discriminator is ancestry, and it is three lines.**

```
rule   newest commit touching the VERDICT vs newest commit touching the REPORT
       verdict is the later  -> the report legitimately predates it. Pass.
       report is the later    -> it was written with the newest verdict
                                 available and must name that one.
out    at HEAD: 197 passed. At a commit whose only content since the report is
       a verdict: passes, which is the closing condition
```

That is not item 1b restored by machine. It is the narrower claim a machine can
make: a report may not be newer than the verdict it declines to answer.

## 4. R287–R290 — the table, the generator, and the ablation

**`scripts/carried_table.py` exists.** The previous revision said the table "is
generated from the verdict" and no generator was in the repository, so the
sentence was unverifiable — and wrong in four rows. The script reads each
finding's own `(BLOCKS …)` or `(recordable, 4a)` heading; only items this round
acted on carry hand-written text.

```
cmd    python scripts/carried_table.py docs/reviews/F2/step-5.md answered.json
out    the table in §7, verbatim
```

**R276, twice.** The `REQUIREMENT_CHANGED` branch returned before `DIAGNOSIS`
was consulted, so the one state in both maps escaped its own ablation. The
previous revision said this was fixed and the call site never landed.
`_assert_diagnosis` has two call sites.

**R286.** `-ra` is in `addopts`, so pytest printed a per-test summary *before*
its count line, carrying text the test file controls: an `xfail` reason of
`"1 passed on the reference build"`, or a parametrize id of `"3 passed"`. A
conftest's `pytest_report_header` prints earlier still. The rung runs with
`-rN --no-header`, so the first count line is pytest's own, and all four of the
reviewer's shapes now redden.

## 5. What is open

| item | why |
|---|---|
| R231, R244, R245 | the Q8 values. The kernel pin makes the measurement possible; it has not been taken |
| R275 | the re-measurement itself |
| R223, R224 | Q7, which follows Q8 |
| R230 | reopened by my own error at revision 4 |
| the 4a set | recordable in the verdict's own classification |

## 6. Carried

| item | status |
|---|---|
| R223 | **open** — carried from an earlier verdict |
| R224 | **open** — carried from an earlier verdict |
| R225 | **open** — carried from an earlier verdict |
| R228 | **open** — carried from an earlier verdict |
| R230 | **open** — carried from an earlier verdict |
| R231 | **open** — carried from an earlier verdict |
| R232 | **open** — carried from an earlier verdict |
| R233 | **open** — carried from an earlier verdict |
| R244 | **open** — carried from an earlier verdict |
| R245 | **open** — carried from an earlier verdict |
| R248 | **open** — carried from an earlier verdict |
| R249 | **open** — carried from an earlier verdict |
| R250 | **open** — carried from an earlier verdict |
| R251 | **open** — carried from an earlier verdict |
| R252 | **open** — carried from an earlier verdict |
| R253 | **open** — carried from an earlier verdict |
| R254 | **open** — carried from an earlier verdict |
| R256 | **open** — carried from an earlier verdict |
| R257 | **open** — carried from an earlier verdict |
| R261 | **open** — carried from an earlier verdict |
| R262 | **open** — carried from an earlier verdict |
| R263 | **open** — carried from an earlier verdict |
| R264 | **open** — carried from an earlier verdict |
| R265 | **open** — carried from an earlier verdict |
| R266 | **open** — carried from an earlier verdict |
| R267 | **open** — carried from an earlier verdict |
| R268 | **open** — carried from an earlier verdict |
| R269 | **open** — carried from an earlier verdict |
| R270 | **open** — carried from an earlier verdict |
| R271 | **open** — carried from an earlier verdict |
| R272 | **open** — carried from an earlier verdict |
| R273 | **open** — carried from an earlier verdict |
| R274 | **open** — carried from an earlier verdict |
| R275 | **open** — §5, the re-measurement has not been taken |
| R276 | **open** — carried from an earlier verdict |
| R277 | **open** — carried from an earlier verdict |
| R281 | **open** — carried from an earlier verdict |
| R282 | **answered** — §3, ancestry rather than recency |
| R283 | **answered** — §1 and §2 state what `73cf6ce` did |
| R284 | **answered** — §1, the job compares against the committed file |
| R285 | **answered** — §2, the pin and its measurement are in the plan |
| R286 | **answered** — §4, `-rN --no-header` |
| R287 | **answered** — §4, `scripts/carried_table.py` is committed |
| R288 | **answered** — §4, the four rows are generated from the headings |
| R289 | **answered** — §4, `_assert_diagnosis` has two call sites |
| R290 | **answered** — §4, the vocabulary corpus runner |
| R291 | **open** — recordable at 4a in the verdict's own classification |
| R292 | **open** — recordable at 4a in the verdict's own classification |

### Sites named by findings and not touched

Declared by exact site, each row saying what the line is.

| site | status |
|---|---|
| `.claude/agents/gating-supervisor.md` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `.claude/agents/gating-supervisor.md:25` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `.claude/agents/gating-supervisor.md:26` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `.claude/agents/gating-supervisor.md:27` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `.claude/agents/gating-supervisor.md:28` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `.claude/agents/gating-supervisor.md:29` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `.claude/agents/gating-supervisor.md:30` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `.claude/agents/gating-supervisor.md:31` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `CLAUDE.md` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:258` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:259` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:260` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:261` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:262` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:263` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:266` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:267` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:269` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:273` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:281` | **no change** -- R282 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1217` | **no change** -- R283 quotes it as evidence, not as a site to change |
| `F2_figures.md` | **no change** -- R284 quotes it as evidence, not as a site to change |
| `docs/SUPERVISOR.md` | **no change** -- R284 quotes it as evidence, not as a site to change |
| `docs/milestones/F2_figures.md` | **no change** -- R284 quotes it as evidence, not as a site to change |
| `floatfea/tolerances.py` | **no change** -- R284 quotes it as evidence, not as a site to change |
| `F2.md:1029` | **no change** -- R285 quotes it as evidence, not as a site to change |
| `F2.md:1068` | **no change** -- R285 quotes it as evidence, not as a site to change |
| `F2.md:1069` | **no change** -- R285 quotes it as evidence, not as a site to change |
| `F2.md:1070` | **no change** -- R285 quotes it as evidence, not as a site to change |
| `docs/milestones/F2.md:1029` | **no change** -- R285 quotes it as evidence, not as a site to change |
| `docs/milestones/F2.md:1030` | **no change** -- R285 quotes it as evidence, not as a site to change |
| `run_rung.sh:155` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `run_rung.sh:156` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:150` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:151` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:152` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:153` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:154` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:155` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:156` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:157` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:158` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:159` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:160` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:161` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:162` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `scripts/run_rung.sh:163` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `tests/corpus/ci_ladder_gating.txt` | **no change** -- R286 quotes it as evidence, not as a site to change |
| `check_carried.py` | **no change** -- R287 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1189` | **no change** -- R287 quotes it as evidence, not as a site to change |
| `write_verdict.py` | **no change** -- R287 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1258` | **no change** -- R288 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1259` | **no change** -- R288 quotes it as evidence, not as a site to change |
| `tests/test_report_guard_states.py:310` | **no change** -- R288 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1316` | **no change** -- R289 quotes it as evidence, not as a site to change |
| `tests/corpus/report_status_vocabulary.txt` | **no change** -- R289 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1269` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1270` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1271` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1272` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1273` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1274` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1275` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1276` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/reports/F2/step-5.md:1277` | **no change** -- R290 quotes it as evidence, not as a site to change |
| `docs/milestones/F2a.md` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/corpus/carried_item_routing.txt` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:231` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:232` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:233` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:234` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:235` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:236` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:237` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:238` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:239` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:240` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:241` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:242` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:243` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:244` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:245` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:246` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:247` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:248` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/test_report_carried.py:249` | **no change** -- R291 quotes it as evidence, not as a site to change |
| `tests/corpus/pinned_interpreter.txt` | **no change** -- R292 quotes it as evidence, not as a site to change |
| `tests/test_the_pinned_interpreter.py` | **no change** -- R292 quotes it as evidence, not as a site to change |

## 7. What I am asking for

**A PASS**, or a **HOLD naming the item and the head.** No Q8 value is written
here.
