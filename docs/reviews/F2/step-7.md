# Review � F2 step 7
Reviewed commit: 6864b542dd07457c59d52c95e80b5b92e6e60724
Verdict: PASS

**Reviewed commit: `2e24459`.**
Tests: 2838 passed, 0 failed, 0 skipped   (my own run at `2e24459`, `python -m pytest -q`, 616.90s)

**Seventieth verdict on F2; the seventh written into this file after step 7's closure
verdict (DD1). STEP 7 IS AND STAYS CLOSED. F2 IS AND STAYS CLOSED.** Verdict 63 at
`2c48a4f` remains F2's closure verdict and nothing here withdraws it.

**THIS IS THE THIRD ROUND AGAINST THE CAP AND THE CAP CLOSES IT (CZ0, DR1).** Verdict 68
was the first, 69 the second. After this verdict the round structure is spent: the three
blocking items still open are carried by name in `## Carried for the next step` and stay
blocking there, and the closure items go into the closure artifact as a list. **DK0: the
F3 re-lock at `772f01e` did not restart the count and I am not treating it as having.**

**WHY PASS AND NOT HOLD.** The four code findings verdict 69 raised are answered, and I
re-measured every one of them myself rather than reading the report. The tree is green on
my run and CI is green at the judged commit. The three findings below are real and two of
them are (c); under CZ0 on the third verdict they carry rather than hold.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 2e24459 --json conclusion,status,workflowName
out  []        -- the --commit filter does not return a run still in flight
cmd  gh run list --limit 4 --json headSha,databaseId,status,conclusion
out  36462874787  2e24459  push  in_progress   -- so the run EXISTS at the judged commit
cmd  gh run view 36462874787 --json status,conclusion   (polled to completion)
out  completed success
cmd  gh run view 36462874787 --json jobs
out  the verification ladder    success  13 steps
     lint, unit and guards      success  14 steps
     CI determinism -- leg               skipped, 0 steps
     CI determinism -- ten legs agree    skipped, 0 steps
cmd  gh run view 36462874787 --log | grep -E "passed|failed"
out  run_rung: 1276 / 66 / 147 / 134 / 127 collected, 0 failed, 0 errored, 0 skipped
     ruff All checks passed!   unit tests 88 passed   guards and meta-tests 1000 passed
```

**CI IS GREEN AT THE JUDGED COMMIT.** Every rung of the ladder collected and none failed.
This is the first green CI conclusion in this round and it is on the commit I am judging,
not on a neighbour and not on a dispatch.

**The two determinism jobs are `skipped` with zero steps.** That is neither red nor green
and it is NOT CK2's allowance state -- no billing annotation, and every other job in the
same run executed. Recorded as unavailable on this run. The last run that executed them is
`36455024518`, the `workflow_dispatch` at `2dc6a99`, where all ten legs read 134 passed / 0
failed; `git diff 2dc6a99..HEAD -- .github` is empty, so nothing about the determinism
configuration has moved since they last ran.

## Carried

Verdict 69 carried six blocking items -- R576, R577, R578, R579, R580, R581 -- and nine
closure items C1 to C9. **I re-measured each of the four code findings in a scratch
worktree outside the repository rather than reading the report on them.**

* **R576 -- ANSWERED IN SECTION 0, NOT ANSWERED IN SECTIONS 3 AND 4. It carries, as R582.**
  `772f01e` is a standalone `plan:` commit and it re-locks DJ1 and DJ2 properly: DV0 names a
  source that exists, DV1 states the arm directions as measured and withdraws the 45-degree
  rationale, DV2 records heading 45 as pending an HSP BEM solve at Xabier's discretion, which
  is an owner. All three strands of R576 are answered where §0 answers them. The superseded
  text is kept beside the new text rather than deleted, which is the right way to do it. What
  was not done is §3 and §4, which still carry the withdrawn sentences verbatim. See R582.
* **R577 -- ANSWERED, and I measured the enforcement rather than the diff.**
  `floatfea/io/reader.py::_validate_scale` now refuses an absent or unrecognised `scale`, a
  `scale: "model"` record, and a converted record missing `froude_lambda`, missing the
  FROUDE-SCALED sentence, or carrying a non-finite lambda. Three new `Fault` members, six new
  matrix mutations, `_good_meta()` now declares `"full"`, and the real-writer control has
  flipped from ACCEPT to a refusal asserted to be `SCALE_NOT_FULL` and nothing else. My run:
  the rung-4 suite reports `scales refused: 8 of 8`.
* **R578 -- ANSWERED, and I re-ran all three of the cells that refuted the old counter.**
  Every one of them now moves, which is the thing that was wrong before:

```
cell   ONE VARIABLE: delete `patch.setattr(froude, "DIMENSIONS", broken)` in the counter
out    the DECLARED-TABLE check misses 0 -> 7, and the counter test FAILS
       (at 2dc6a99 this cell changed NOTHING)
cell   ONE VARIABLE: replace the shipped table assertion with `assert True`
out    the DECLARED-TABLE check misses 0 -> 7, and the counter test FAILS
       (at 2dc6a99 this cell still reported full sensitivity)
cell   ONE VARIABLE: make `to_model_scale` multiply, in floatfea/io/froude.py
out    the ROUND TRIP misses 7 -> 0, and the counter equality FIRES
       (at 2dc6a99 this cell still printed "the ROUND TRIP misses 7")
judge  both published figures now move when the thing they name moves. R578 is closed.
```

* **R579 -- ANSWERED, measured on the two arrays the finding named.**

```
cmd  to_full_scale(np.ones((2,6)), "force", 50.0)
out  ValueError -- trailing axis 6 is a declared composite width; name the composite
cmd  to_full_scale(np.ones((1,6)), "wrench", 50.0)
out  [125000 125000 125000 6250000 6250000 6250000]   -- the dimensionally correct result
cmd  to_full_scale(np.ones((2,4)), "force", 50.0)     -- lam[N,4]
out  ValueError
cmd  froude_factor("wrench", 50.0)
out  ValueError -- a composite has no single factor
```

* **R581 -- ANSWERED, and wider than the finding asked for.**

```
cmd  froude_factor("force", lam) for lam in {nan, inf, 1e-300, -0.0, 1e200}
out  nan REFUSED   inf REFUSED   -0.0 REFUSED
     1e-300 REFUSED -- "lambda**3 is not representable" (it underflowed to 0.0 before)
     1e200  REFUSED -- the overflow side, which the finding did not name
```

* **R580 -- ANSWERED. The tree is green and I did not take that from the report.**
  My own whole-suite run at `2e24459` is 2838 passed, 0 failed, 0 skipped, and CI at the same
  commit is a success conclusion with 0 failed in every job that ran. R570's site is closed in
  the better of the two forms verdict 69 offered: `tests/test_report_guard_states.py:625-632`
  now writes **no count at all** and points at `test_the_corpus_and_the_states_agree`, which
  prints it at the commit that runs it. `grep -rn "twelve are unbuilt" tests/` is empty.
* **C1 to C9 -- LANDED IN ONE COMMIT, `e4d5895`, and I am not re-reviewing them item by
  item (CZ0).** Two I noticed in passing and record as done because they were the two with
  content: C7 put a V3.2 and a V4.0 row in `docs/verification/README.md`, and C9 put the
  corrected DQ2 gimbal measurement into `docs/platform-joints.md` with
  `scripts/measure_platform_joints.py` beside it. I ran that script myself: 16 of 16
  two-rotation gimbals, worst released-moment leak 2.753e-15 relative, and the offset cell
  reproduces (rank 3 over all four rows at 1.689 m, rank 1 at 0 m, rank 1 over the lock row
  in both). The number in the report is the number the script prints.

## Findings

**R582. (plan, blocking) The F3 re-lock repaired §0 and left §3 and §4 carrying the
withdrawn text verbatim. `docs/milestones/F3.md:225`, `:231`, `:243`.**

§0 answers R576. §3 is the section headed *"GEOMETRY AND SECTIONS — LOCKED (DJ1)"* and it
is the numbered work list the builder is written from, so it is the half that gets executed.

```
claim  the plan still names a source that does not exist, and still says diagonal
cmd    grep -n "model-definition YAML\|diagonal arms\|two-run reduced set" docs/milestones/F3.md
out    :35  (the superseded text, correctly labelled as superseded)
out    :225 1. **read the layout from HSP's model-definition YAML at full scale**
out    :226    the X-brace, two diagonal arms crossing at the central hub
out    :243 * the twelve full-scale runs, or the two-run reduced set
cmd    grep -n "YAML mass" docs/milestones/F3.md
out    :231 3. **size every other member to reproduce its body's YAML mass**
judge  :225-226 is the sentence DV1 withdrew, unlabelled, in the executable section.
       :243 is the reduced-set fallback DV2 says is REMOVED and the twelve-run basis
       DV2 replaced with six at 0 degrees. A plan that contradicts itself between the
       answer and the work list is a plan whose first executable step is ambiguous, and
       R576 was exactly that finding.
```

**Closed when** §3(1) reads the generated deck at `data/platform/platform12_deck.yaml` with
the arms axial, §3(3) says deck mass rather than YAML mass or is left with the pointer made
explicit, and §4 carries DJ2 as DV2 re-locked it. A plan re-lock; DK0 applies and it does not
buy a fresh three.

**R583. (c, blocking) The half of G3.2 that runs in CI carries the gate id on the one
assertion in the module that cannot fail. `tests/verification/rung3/test_platform_deck_export.py:79-93`.**

This is the invocation's question 2 and the ruling is in two parts. **The split is honest and
the reasoning behind it is right**: a `skipif` on the cross-repository half would have read as
a pass in every CI summary, `CLAUDE.md` names `skip` in the same sentence as `xfail`, and
moving that half to a procedure with a command is the better of the two. **What is wrong is
what was left carrying the gate id.**

```
rule   the assertion at :90 -- `yaml.safe_load(yaml.safe_dump(raw, sort_keys=False)) == raw`
cell   ELEVEN mutations of the committed YAML, one variable each, in a scratch worktree
out    a buoy reference point moved to 99.0          4 passed
       every mass multiplied by ten                  4 passed
       every body z negated                          4 passed
       a buoy moved onto the diagonal                4 passed
       a coordinate replaced by .nan                 4 passed
       a duplicated `name` key                       4 passed
       the document re-emitted with sort_keys=True   4 passed
       the header falsified to bodies 99 joints 99   4 passed
       the file truncated to the header alone        2 failed -- NEITHER of them this one
       a body dropped                                1 failed -- topology, not this one
       a hub moved onto the diagonal                 1 failed -- axial, not this one
judge  test_G3_2_the_committed_YAML_ROUND_TRIPS_without_loss is green on 11 of 11,
       including a file that parses to None. `safe_load(safe_dump(x)) == x` is a property
       of PyYAML for any structure of plain scalars; no committed content reddens it.
       "If the thing it claims were false, would this go red?" -- no.
```

**And its docstring names the one case I could construct that a stronger form would catch,
and does not catch it.** *"nothing in the file is lost or reordered by a parse-and-re-emit
cycle"* -- the sorted-keys cell reorders every key in the document and the assertion is green,
because `==` on dicts is order-insensitive.

The three siblings do carry their failure and they are the real content of this module:
topology catches a dropped body and a relabelled joint, and the axial test catches a diagonal
hub and an unequal arm. **The finding is not that the module is worthless. It is that the
assertion named for the gate is the one that certifies nothing**, so a reader of the ladder
sees G3.2 green and it means the three unnamed assertions passed.

**Closed when** the G3.2 id sits on an assertion a committed-file defect can redden -- a
comparison of the file body against `yaml.safe_dump(safe_load(body), sort_keys=False)` as
TEXT would redden the sorted-keys and duplicate-key cells, and a committed digest of the file
body would redden all eleven -- or the id moves onto the assertions that already fail. I am
describing the test, not writing it.

**R584. (c, blocking) The other half of G3.2 claims "rebuilt from HSP AT THE PIN and
compared" and measures neither the pin nor the provenance. `scripts/export_platform_deck.py:55-79`
and `:150-159`.**

This is the invocation's question 1, and the answer is that the preflight is not sufficient
and the comparison does not compare what the file publishes. **The round trip living in the
generator is right** -- a lossy dump is never written, and I confirmed that independently.

```
cmd    python scripts/export_platform_deck.py --check       (my machine, this commit)
out    HSP floatfea-ref-1 @ 25de7ce / bodies 17 joints 16 /
       round trip: re-validated dump equals the source dump (9 top-level keys) /
       data/platform/platform12_deck.yaml matches the deck            exit 0
judge  the committed YAML does reproduce the deck built from HSP, today, here. That is
       the strongest statement available about this file and it holds.
```

The two gaps are in what the procedure would still accept.

```
claim  the preflight does not check that the pinned worktree is CLEAN
cmd    grep -n "porcelain\|diff-index\|status" scripts/export_platform_deck.py
out    (no output)
judge  `_preflight` reads `git describe` and `git rev-parse HEAD`. A worktree at the pinned
       commit with a tracked file locally modified passes every check and exports a deck
       built from the modified file, under a header that names the pin. The docstring says
       the pin exists "so that a model exported today and a model exported next month are
       the same model"; HEAD alone does not give that. I verified today's worktree IS clean
       (`git -C ../HSP-runs status --porcelain` shows one untracked output directory and
       nothing else), so the SHIPPED file is sound -- the gap is in the guarantee, not the
       artifact, which is why it is a gate finding and not a defect in the deck.
claim  `--check` strips the header from both sides before comparing
cmd    the slice at :154-155, `splitlines()[len(header(...).splitlines()):]` on each side
out    the HSP tag, the HSP commit, the body and joint counts and the source path are
       compared with nothing
cell   ONE VARIABLE: the header rewritten to `bodies 99` / `joints 99`, content untouched
out    the suite half: 4 passed. the check half: excluded by construction.
judge  the provenance the file publishes on its face is the thing neither half of G3.2
       reads. The date has to be excluded -- it moves daily -- but the tag, the commit and
       the counts do not.
```

**Closed when** the preflight refuses a worktree with modified tracked files, and `--check`
compares the provenance lines it can compare (tag, commit, counts, source) rather than
excluding the whole header to get past the date.

**R585. (closure) The three environment-sensitive reds have ONE diagnosis, it is not the
guard, and the report's attribution of them to CI's environment is refuted by CI.
`tests/test_report_guard_states.py:503`.**

This is the invocation's question 3, and the implementer was right to put it in front of a
reader rather than pick a side. I diagnosed it.

```
cell   ONE VARIABLE: whether the tree the harness copies from has `.git` as a DIRECTORY
       or as a `gitdir:` FILE. Everything else held -- same commit, same interpreter.
cmd    python -m pytest tests/test_report_guard_states.py -q     (main checkout, .git is a dir)
out    24 passed
cmd    the same, in a `git worktree add --detach` tree at the same commit (.git is a 76-byte file)
out    3 failed, 21 passed -- exactly the three the report names
cmd    the traceback of shallow_clone_depth_1
out    tests/test_report_guard_states.py:503 shutil.rmtree(work / ".git", onerror=_force_remove)
       NotADirectoryError: [WinError 267] The directory name is invalid: ...\repo\.git
judge  `_build` assumes `.git` is a directory. In a linked worktree it is a file pointing
       back at the original repository, so `rmtree` raises, and the third state fails for
       the same root cause one step later -- its `git commit` in the copy returns 1 because
       the copied `gitdir:` pointer still addresses the original worktree, so there is
       nothing to commit. NEITHER environment is telling the truth about the guard: the
       clean-worktree red is a property of `git worktree`, not of the tree under test.
claim  the clean worktree is NOT "the same environment CI runs in"
cmd    gh run view 36462874787 --log | grep "guards and meta-tests"
out    1000 passed, 1 warning in 595.09s    -- at the judged commit, these three GREEN
judge  `actions/checkout` produces a real `.git` directory. The sentence in the report at
       §5 is refuted by the run that ran the same tests.
```

**This is a closure item and not (d)**: the three are green on my run, green in CI, and green
in the working checkout. What it costs is the trustworthiness of `scripts/suite_count.py`,
which is the generator of the report's own suite line -- it will invent this red again at
every step, and a false red in the one line a reader uses to tell a green tree from a green
subset is worse than no line. **Closed when** either `suite_count.py` stops measuring inside a
linked worktree, or the harness is deleted at the site per DR1 with the reason recorded. Under
the freeze the permitted move is deletion, not repair; which of the two is the implementer's
call and I am not asking for new apparatus either way.

## The rulings the invocation asked for

**Question 4 -- `_validate_scale` running LAST. The ordering argument is SOUND, and I
measured the direction it actually buys.** If `validate()` raises a `SCALE_*` fault, every
earlier validator returned without raising, so `test_real_writer_output_is_REFUSED_only_for_its_SCALE`
is a stronger positive control than the acceptance it replaced: it certifies units,
provenance, gravity, integrator, time base, kinematics, loads and joints on real writer
output in the same assertion. The hiding runs the other way -- a record that is model scale
AND malformed reports the other fault -- and that is a misdiagnosis, never an acceptance,
because nothing returns from `validate()` without passing `_validate_scale`. I checked there
is no second entry point: `grep -n "^def " floatfea/io/reader.py` gives one public function.
The one consequence worth writing down is the converse, which the docstring does not claim
and no test rests on: the ABSENCE of a scale fault is not proof the scale was checked first.

**Question 5 -- `measure_platform_joints.py` and `export_platform_deck.py` are NOT apparatus
under the freeze. Your claim stands and I am ruling it rather than letting it stand.** DR1
and CZ0 freeze "guards, scanners, meta-tests, detectors or report generators" -- the class
that checks the process. Neither script is collected by pytest, neither asserts anything
about a report or a commit, and neither gates a step. One measures a physical property of the
platform and the other generates model data. `scripts/rigid_counter_response.py` is the
precedent and it is the same class. **The one tension, stated so it is on the record:**
`docs/verification/README.md` now makes `--check` half of gate G3.2, which makes that script
a gate PROCEDURE. That does not make it frozen apparatus, but it does mean R584 is a gate
finding rather than a script nit, and it means the half only counted this round because a
second machine ran it.

**The dispatched CI run as the source for the CI section -- ACCEPTABLE, and superseded.** A
`workflow_dispatch` at `2dc6a99` runs the same workflow on the same commit; the event does
not change what was measured, and carrying ten determinism legs a push run does not is more
evidence rather than less. It also reproduced my 25 reds independently with the ladder green
at 1728, which is the property CA2 exists for. Two conditions, both met: the run is at the
commit the section claims, and the section says on its face that it is a dispatch and why.
It is moot now -- there is a push run at the judged commit and it is green -- but the ruling
stands for the next time a rebase leaves a judged commit unpushed. **The report's own general
lesson is the right one: push before the verdict, not after.**

**The two pasted unrun counts -- recorded, not a finding.** Both were caught and amended
before pushing, and both amendments record the numbers they replaced. Nothing in the tree
reads a commit message, so no guard could have caught either. What I will say is that the
second one is CP2 exactly, in a commit whose subject was a guard, and that the pattern the
implementer names -- the attention goes to the fix and the prose written around it inherits
none of the discipline applied to it -- is now recorded three times in three milestones by
the person it keeps happening to. That is the useful part.

**The undeclared `1e-12` and `round(..., 9)` -- fixed, and the fix is the right form.**
`ROUNDOFF_IDENTITY` used relative against the arm radius, dimensionless, with the reason at
the site. I checked the margin: the worst off-axis residue in the deck is `1.837e-16` of the
radius (hub4, `sin(3*pi/2)` round-off), against a threshold of `1e-14` -- 54x of headroom --
and the defect it exists to catch, a hub genuinely on the diagonal, reads `0.7071`, which is
`7e13` times the threshold. The decision boundary is nowhere near either.

**DV4 item 4 -- not building a second `sections.py` was right.** One formula with two sources
is the failure mode `docs/conventions.md` exists to prevent. Reporting it instead of building
it is the correct call and needs no ruling from me.

**And `tests/test_report_carried.py:916` -- confirmed not used.** `grep -n "unavailable"` over
the report shows no CK2 escape claimed in any revision. Neither of CK2's two shapes was true
this round and the report does not claim otherwise.

## Closure items

None of these blocks. Fix the list once, in the closure commit, and do not re-review them
item by item.

* **C10. R585, the environment-sensitive reds and the sentence attributing them to CI.**
  `docs/reports/F2/step-7.md:1297-1299`. Its own diagnosis is above; the sentence "which is
  the same environment CI runs in" is refuted by the CI run at the judged commit.
* **C11. `tests/verification/rung3/test_platform_deck_export.py:103-106` asserts arithmetic
  on three literals in its own file.** `BODIES * 6 - JOINTS * JOINT_ROWS == 38` compares
  `17 * 6 - 16 * 4` with `38` and never touches the parsed deck; it is green whatever the
  YAML holds. **Closed when** the identity is computed from `len(raw["bodies"])` and the
  joints as parsed, or the line goes.
* **C12. `floatfea/io/froude.py::_refuse_uncovered` refuses a genuinely scalar 2-D array
  whose trailing axis is 4, 5 or 6.** Measured: `to_full_scale(np.ones((3,6)), "pressure", 50)`
  raises. The refusal is the safe direction and the docstring documents the 1-D residual
  honestly, but not this one. **Closed when** the docstring names the 2-D false positive too,
  or the schema is cited as having no such array.
* **C13. The report's `Answers:` line reads `verdict 69 @ 4ff1008` where verdict 69 asked for
  `@ 2dc6a99`.** It names the LATEST verdict, which is what instruction 1b is about, and
  `check_carried` is green on it, so nothing substantive turns on it. **Closed when** the two
  conventions agree -- either the judged commit or the commit the verdict text is final at,
  named once.
* **C14. `docs/reports/F2/step-7.md:1086-1087` says F3 closes 10 October.** The re-lock at
  `772f01e` moved it to 13 October two commits later. BP0: when the rule moves, the figure
  citing it is regenerated or withdrawn in the same commit. **Closed when** the paragraph
  carries the date in the plan at the commit that publishes it.
* **C15. `docs/milestones/F3.md:29-32` and the deck disagree about the hub arm.** DJ1 says
  "a cross through the centre, 50 m to each hub". Measured from the exported deck: the hub
  reference is at radius 50.000 m exactly, but 24.67 m above the origin while the platform
  reference is at 35.0 m, so the platform-to-hub member is 51.06 m and inclined 11.7 degrees.
  The 25 m cluster arm is exactly 25.000 m horizontal and F1:389's sizing basis survives
  unchanged. **Closed when** the plan states the hub arm as the deck has it, because §2's
  `L/D` and `L/r` refusals are computed on member length and 51.06 is not 50.
* **C16. Nothing states that each hub carries THREE cluster arms at 120 degrees.** Measured:
  attach points at (0.5, 0), (-0.25, +0.4330), (-0.25, -0.4330) from each hub, twelve arms in
  four tripods. Every plan sentence reads as though "cluster arms 25 m from each hub" were a
  count-free fact. **Closed when** the count and the spacing are written down where the
  builder reads them.

## Tolerances touched

**None.**

```
cmd  git diff 2dc6a99..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 2dc6a99..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        -- CI0: the pathspec resolves; the instruction is not broken
cmd  git diff 2dc6a99..HEAD -- .github
out  (no output)
```

**No new conftest and no plugin was added, so CH2's reading has nothing new to read.** The
one existing conftest is unchanged, byte for byte, across this round.

The new rung-3 module imports one existing entry, `ROUNDOFF_IDENTITY`, at two sites. Both are
relative and dimensionless -- `min(|x|,|y|) / radius` and `(max - min) / max` over the four
arm radii -- which is the entry's declared form, and the measured worst is `1.837e-16`
against `1e-14`. No value was added, none was changed, and nothing was widened.

**One form note, not blocking:** `BODIES`, `JOINTS` and `JOINT_ROWS` carry a `not-a-tolerance`
marker with a source, which is the right shape for counts of objects.

## What I built to break it

Everything below ran in a `git worktree` under the session scratch directory, outside the
repository, and was removed. Nothing was written into the tree except this verdict and the
corpus.

1. **Eleven mutations of the committed deck YAML** against the rung-3 module. Result is
   R583: the assertion carrying the gate id is green on all eleven.
2. **Verdict 69's three refuting cells, re-run against the repaired counter.** All three now
   move. That is the strongest single thing in this round and it is why R578 is closed rather
   than accepted.
3. **The composite channels the schema marks REQUIRED**, `mu[N,6]` and `lam[N,4]`, through
   both the scalar path and the composite path, plus a composite with the wrong width and a
   composite name passed to `froude_factor`. All four behave.
4. **The lambda guard at five values**, including the two the finding did not name --
   `1e200` overflows and is refused, `1e-300` underflows and is refused.
5. **`--check` on a second machine**, which is the only independent evidence that the
   committed file is the deck. It passes.
6. **`measure_platform_joints.py` re-run**, to check the 16-of-16 and the 2.753e-15 rather
   than read them.
7. **The environment cell for the three reds**, one variable, which is R585.

**The adversarial case that did NOT pass when it should have failed is R583**, and it
outranks everything in the report, which is why it is the finding that carries.

## Corpus this round (BE3)

**`tests/corpus/platform_deck_source.txt`, batch 18, committed separately at `6864b54`.**
Thirty-six entries, none of them seen by the implementer, in three sections: the committed
file mutated, the generator and its preflight, and the exported model against what DJ1 and
DV0 say about it.

**In scope under DE2** -- "from F3 -- the platform model" -- so it is not an apparatus corpus,
DR1 does not defer it to `docs/milestones/F2a.md`, and nothing is transcribed.

**THE COVERAGE MEASUREMENT: 20 of the 36 entries assert that a defect must be caught by
something shipped. Nine are caught. Eleven are not.** That is the number, and it replaces the
implementer's own: the rung-3 module was built with four assertions and the count that matters
is not how many shapes those four were built for.

The eleven missed, named because a count without its members is not a measurement: a single
body coordinate moved to 99.0; every mass multiplied by ten; every z negated; a buoy moved
onto the diagonal; a `.nan` coordinate; a duplicated key; the document re-emitted with sorted
keys; the header's own body and joint counts falsified; a wholly different but conformant deck
substituted; the preflight against a dirty pinned worktree; and `--check` against a falsified
header. The nine caught are a dropped body, a relabelled joint, a truncated file, a diagonal
hub, an unequal arm, a symlink to HSP-stable, a worktree past the tag, a missing file, and the
round trip itself.

**Eight entries are questions rather than mutations** (`expect=explain`) and they are the
half I would read first: the hub arm is 51.06 m and inclined, each hub carries three cluster
arms, the buoy reference is 84 m below its joint point, and the vertical datum is unstated.
Those are about the model F3 is about to build, not about a check.

**The standing measurement.** `cmd grep -h "^id=" tests/corpus/*.txt | wc -l`; `out` 1198
entries across 19 files. Of the apparatus corpus, the untranscribed count stays where DR1 put
it and is reported by the corpus-agreement test rather than written down here.

## My own instructions (4b)

```
cmd  git diff 2dc6a99..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git log --format="%h %s" 2dc6a99..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
```

**Nothing touched them this round and no commit mixes them with `floatfea/` or `tests/`.**
`4ff1008` touches `docs/reviews/F2/step-7.md` alone and it is a reformatting of my own
previous verdict's six finding headings to DU1's shape; it changes no verdict, no class and
no `Closed when`, and I read all six hunks. I have complied with both DU1 rules here: the
judged commit is restated bolded and backticked at the top, and every blocking finding heads
`**R<n>. (<class>, blocking) ...**` with the status inside the parentheses.

## On the criterion, once

**CZ0 is the right rule and it paid this round.** Nine closure items landed in one commit,
none of them consumed a round, and the round went to the boundary and the deck instead. The
four code findings from verdict 69 are all closed and I could measure every one of them in
about twenty minutes because they were specific.

**One note, and it is the same seam I flagged last round rather than a new objection.** R582
is a plan finding and R576 was; neither is one of CZ0's four heads. I am classing it
`(plan, blocking)` and carrying it because a plan that contradicts itself between its answer
and its work list is the condition a STOP exists for, and because the alternative -- classing
it as prose -- would let the executable section of a locked plan drift from the locked answer
with nothing that reads it. I am not asking for a ruling and this does not become another
round. It goes to Xabier through the implementer if it goes anywhere.

**And I will say the schedule thing plainly, because it is the one number CZ0 is protecting.**
F3 now closes 13 October and the member-force table 23 October. Nothing in this round touched
the platform model itself -- the deck is exported and measured, and that is the input, not the
model. Two consecutive post-closure rounds have now ended carrying blocking items. That is
CZ0's escalation condition, and the choice it names is the supervisor's: slip the date, or
reduce scope. I am recording that it is triggered, not choosing.

## Carried for the next step

These carry **by name** and stay **blocking** in the next step's `Carried` section (CZ0). They
are not re-opened here and they do not hold anything now.

* **R582 (plan, blocking)** -- `docs/milestones/F3.md:225`, `:231`, `:243` still carry the
  withdrawn DJ1 and DJ2 text in the executable sections.
* **R583 (c, blocking)** -- the assertion carrying G3.2's id in
  `tests/verification/rung3/test_platform_deck_export.py:79-93` cannot fail; 0 of 11 mutations.
* **R584 (c, blocking)** -- `scripts/export_platform_deck.py`: the preflight accepts a dirty
  pinned worktree, and `--check` excludes the provenance header from the comparison.

**C10 to C16 are closure items** and go into the closure artifact as a list if they are not
closed before it.

## Next step opens when

**Step 7 is closed and stays closed; this verdict is about the tree and about a plan.** The
cap is spent. The next step opens now, with the three items above carried into it as blocking.

1. **The next report's header is `Answers: verdict 70 @ 2e24459`** -- the latest verdict and
   the commit it judged. The stamped header on this file is my corpus commit `6864b54`, per
   R513, and the body restates the judged commit per DU1.
2. **R582, R583 and R584 are answered in the next step's first commits**, each at the sites
   named, site by site. R582 is a `plan:` commit citing the directive; R583 and R584 are one
   assertion and one predicate between them and neither needs new apparatus.
3. **C10 to C16 land in one closure commit** and are not re-reviewed individually.
4. **The green stays green.** My run is 2838 passed / 0 failed / 0 skipped and CI at the
   judged commit is a success conclusion; anything less than that at the next answering commit
   is (d).
5. **Push before the verdict, not after.** The CI section generated cleanly this round only
   because the judged commit was a branch head when it was pushed.
