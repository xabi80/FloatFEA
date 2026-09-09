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
