# Review — F2 step 7
Reviewed commit: b9dd0273f54667268dff5e76944b5e99df354648
Verdict: STOP

**Reviewed commit: `2dc6a99`.**
Tests: 2729 passed, 25 failed, 0 skipped   (my run at `2dc6a99`, `python -m pytest -q`, 572.15s)

**Sixty-ninth verdict on F2; the sixth written into this file after step 7's closure
verdict (DD1). STEP 7 IS AND STAYS CLOSED. F2 IS AND STAYS CLOSED.** Verdict 63 at
`2c48a4f` remains F2's closure verdict and nothing here withdraws it. Under DR1 this is
the second post-closure round counted against the next step's cap; verdict 68 was the
first.

**WHY STOP AND NOT HOLD.** A STOP is "the locked plan is wrong". It is, at its first
executable step, and it is wrong in three independent places measured below (R576).
`CLAUDE.md` says do not soften a STOP into a HOLD, and my own instructions say the same,
so I am not recording this as a tall HOLD. **The implementer stopped and reported rather
than adapting the plan, which is exactly what the working agreement asks for; the STOP is
the mechanism that records it, not a judgement on that decision.** Nothing about the
DS2 work at `ca6959a` is uninterpretable because of it -- that commit precedes the lock --
so the findings below still stand and still have to be answered.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 2dc6a99 --json name,conclusion,workflowName
out  []        -- UNAVAILABLE. Recorded as unavailable, not skipped over.
```

The local head `2dc6a99` was rebased this turn and has not been pushed; `origin/F3` is
`6186eb4`, a different sha. This is NOT CK2's allowance state -- runs are executing and
billing is live. **The last run that EXECUTED on a commit in this range is `c78d895`,
and the code under review has not moved since:**

```
cmd  git diff --stat c78d895..HEAD -- floatfea tests scripts .github
out  (no output)   -- the two commits after it are docs/milestones/F3.md only
cmd  gh run view 36440843564 --json jobs
out  "the verification ladder"    success  -- 13 steps, 2m32s. NO RUNG IS RED.
     "lint, unit and guards"      failure  -- 14 steps, 5m22s, a real execution
     two determinism jobs         skipped
cmd  gh run view 36440843564 --log-failed | tail -1
out  25 failed, 913 passed, 1 warning in 290.29s
```

**CI and my machine agree on the count and on the set: 25.** That is up from ONE at
verdict 68. The ladder being green is why this STOP is about the plan and not about a
low rung.

## Carried

Verdict 68 carried **R567** blocking by name and listed R568-R575 as closure items. The
invocation asks me to rule on each.

* **R567 -- WITHDRAWN, and say why rather than let it lapse.** Its site,
  `test_the_guard_survives_the_state[two_digit_step_number]`, no longer exists: `391e375`
  deleted the state under DT2, which is one of the two DR1-compliant moves verdict 68
  itself named ("or records that the state was deleted under DR1 with the reason at the
  site"). The reason is at the site, in the STATES dict where the entry was. The deletion
  is clean in extent for the parametrisation -- `BUILT_ENTRIES` filters the corpus by
  `STATES`, so the case disappears rather than erroring -- and the corpus row stays as the
  record. **It is withdrawn as an item and replaced by R580: the tree is redder now, and
  for different reasons.** Deleting it did not reduce the red count and the commit message
  says so plainly, which is the right way to have written it.
* **R568 -- ANSWERED in substance, and its repair introduced two stale numbers.** The note
  at `tests/test_report_carried.py:2183-2198` now names both losses. Closure item C1.
* **R569 -- ANSWERED.** The claim that `test_collected_set_golden.py` carries the retired
  property is withdrawn at the site and replaced with "nothing replaces it". Correct.
* **R570 -- NOT ANSWERED. The site was never touched.** This is the one the report gets
  wrong, and it is (d) at the reviewed commit. See R580.
* **R571 -- ANSWERED, both sites.** `tests/test_report_guard_states.py:268-273` no longer
  names `_older_ancestor`; `tests/test_report_carried.py:2263` no longer names
  `_implementer_commits_after()`. Verified line by line.
* **R572 -- ANSWERED.** `cmd grep -rn "_last_commit_touching" tests scripts`; `out` (no
  output).
* **R573 -- ANSWERED, AND RE-BROKEN BY THE NEXT COMMIT.** `docs/closure/F2.md:206-224` was
  re-measured at `e500ea0` and now names `two_digit_step_number` as the red -- which
  `391e375` deleted one commit later, and whose reproduction command
  (`pytest tests/test_report_guard_states.py -q`, `out 1 failed`) gives `7 failed` at HEAD.
  Closure item C2. This is BP0's shape twice in the same paragraph in two commits.
* **R574 -- ANSWERED.** The four-row ledger is in `docs/milestones/F2a.md`, including
  R562's constraint travelling with the backstop. This was the one verdict 68 would not
  let slide and it landed. Its own count ("22 unbuilt") is stale at HEAD -- closure item C3.
* **R575 -- ANSWERED in substance.** `scripts/run_floatsim_design_waves.py:20-31` now names
  the single-heading BEM database as the binding constraint and demotes the hardcoded
  argument. The named site at line 27 is still red in the site guard; that is part of R580.

## Findings

**R576. (plan, blocking) F3's locked plan is wrong at its first executable step, in three
independent places. `docs/milestones/F3.md:24-26`, `:70`, `:77`, `:152-158`.**

The implementer reported the first of these against itself and stopped rather than
adapting. That is the correct move and I am confirming the finding independently.

```
claim  DJ1 sources the layout from an HSP model-definition YAML, and no such file exists
cmd    find ../HSP-runs ../HSP-stable -name "*.yaml" -o -name "*.yml"
out    studies/cluster-3buoy-rigid/deck_bem_morison.yaml, deck_bem_only.yaml
       examples/two_body_semisub_barge.yml, tests/fixtures/bem/orcaflex/platform_small.yml
cmd    ls ../HSP-runs/studies/platform-12buoy/
out    platform_common.py, platform_bem.py, build_platform_mesh.py, ... -- no YAML
judge  the 12-buoy deck is built in Python. Two 3-buoy-cluster decks, one semisub example
       and one orcaflex fixture are the only YAMLs upstream. The named reference does not
       exist, and G3.1a -- "size every other member to reproduce its body's YAML mass" --
       has no reference either. "Verify the reference" is the guard, and this reference
       is not merely unverified, it is absent.
```

```
claim  DJ1's geometry is wrong: the arms do not lie on the diagonals
cmd    grep -n "CLUSTER_ANGLES_DEG =" ../HSP-runs/studies/platform-12buoy/platform_common.py
out    34:CLUSTER_ANGLES_DEG = np.array([0.0, 90.0, 180.0, 270.0])  # C4-a
judge  `docs/milestones/F3.md:25` says "two diagonal arms crossing at the central hub".
       The arms lie along +/-x and +/-y. The same wrong belief is published twice at this
       commit -- once in a locked plan and once in a step report -- which is why it is a
       plan finding and not only a prose one.
```

```
claim  DJ2 locks a load basis this repository records as unobtainable
cmd    grep -n "45" docs/milestones/F3.md
out    :70  headings 0 and 45, 3 seeds each -- 12 runs
out    :77  the REDUCED set: 1 seed at 0 and 45 -- 2 runs
cmd    sed -n '20,31p' scripts/run_floatsim_design_waves.py
out    "the BEM database is solved at a single wave heading ... it needs a BEM solve at
       the second heading, which is 3.66 h and 40.6 GB measured ... an HSP task"
judge  R575 established that one commit earlier. The fallback keeps both headings, so the
       runtime escape does not escape this. The plan was locked over the top of a
       constraint the same tree had just recorded.
```

**Closed when** the plan reopens and DJ1 names a source that exists (`platform_common.py`
and what in it), states the arm directions as measured, and DJ2 either drops heading 45 or
records the BEM solve as a precondition with an owner. This is a plan re-lock; per DK0 it
does not restart the verdict count.

**R577. (a, blocking) `floatfea/io/reader.py::validate` enforces nothing from `scale`.
This is the direct answer to the invocation's question 1, and the answer is no.**

DU0 re-locked `docs/load-interchange-v1.md` sec.2.1 to say the field "constrains the
READER". Measured, at `2dc6a99`, against the shipped validator:

```
cell   ONE VARIABLE: the `scale` value in the G1.2 positive-control fixture. Everything
       else held. Probe under /tmp, not in the repository.
cmd    validate(record) for scale in {model, full, banana, MODEL, 50.0, absent}
out    scale='model'  -> ACCEPTED       scale='banana' -> ACCEPTED
       scale='full'   -> ACCEPTED       scale=absent   -> ACCEPTED
       scale='MODEL'  -> ACCEPTED       scale=50.0     -> ACCEPTED
cmd    grep -n "scale" floatfea/io/reader.py
out    (no output)   -- the reader does not read the field at all
judge  the enumeration is not enforced, the field is not required, and a record declaring
       model scale is read as SI full scale by everything downstream. The gravity check
       cannot stand in for it: |g| is 9.81 at both scales.
```

**And the shipped gate asserts the wrong direction.** `tests/verification/rung4/
test_validator_matrix.py:55` puts `"scale": "model"` in `_good_meta()` -- the fixture whose
docstring is "A minimal record that MUST validate. The positive control." So G1.2 currently
*asserts* that a model-scale record is well-formed and acceptable. That is the assertion,
not an oversight in it, which is why this is (a) and (c) rather than a closure item.

**`provenance()` and `assumption_record()` do not close this.** They are correct in
content -- `scale: "full"`, `source_scale: "model"`, `froude_lambda`, the bases and every
derived exponent, and a sentence saying no quantity was measured at full scale. But:

```
cmd    grep -rn "froude" floatfea/ scripts/ --include=*.py -i | grep -v io/froude.py
out    scripts/run_floatsim_design_waves.py:57 (a docstring about the study scale)
judge  nothing in floatfea/ calls to_full_scale, provenance or assumption_record. The
       non-confusability property lives entirely inside a module with no caller, and the
       one component that WOULD have to refuse a mis-declared record does not look at the
       field. Available is not enforced.
```

**Closed when** `validate()` rejects a record whose `scale` is absent or not in the
enumeration; rejects `scale: "model"` (or accepts it only through a named conversion path
that sets the provenance fields); rejects `scale: "full"` carrying `source_scale` without
`froude_lambda`; and `_good_meta()` declares what a well-formed record actually is. The
fault needs a name in `Fault` beside the eight that are there.

**R578. (b, blocking) The DS2 counter's injection is inert, and its round-trip control
cannot fail. `tests/verification/rung4/test_froude_scaling.py:95-141`.**

This is the invocation's question 2, and the ruling is: **the intent is legitimate, the
published figure is correct, and the control as written asserts its own premise.** Three
cells, one variable each, in a scratch worktree outside the repository.

```
cell   ONE VARIABLE: delete `patch.setattr(froude, "DIMENSIONS", broken)` at :115.
cmd    python -m pytest tests/verification/rung4/test_froude_scaling.py -q
out    20 passed; the DECLARED-TABLE check misses 0; the ROUND TRIP misses 7
judge  IDENTICAL to the unmutated run. The injection changes nothing. The table half
       reads `broken[quantity]` directly at :116 and never goes through the module; the
       round-trip half at :121 computes `(values * factor) / factor`, which returns its
       input for any finite non-zero factor whatever DIMENSIONS holds.
```

```
cell   ONE VARIABLE: gut the SHIPPED assertion at :59 to `derived == approx(derived)`.
cmd    the same run
out    20 passed; the DECLARED-TABLE check misses 0
judge  the counter certifies a COPY of the assertion, not the assertion. "A gate carries
       its own failure" requires breaking the property and confirming the assertion goes
       red; this one would report full sensitivity for a test that checks nothing.
```

```
cell   ONE VARIABLE: make `to_model_scale` multiply instead of divide, in floatfea/.
cmd    the same run
out    12 failed, 8 passed -- AND the counter still printed "the ROUND TRIP misses 7"
judge  the control does not touch `to_full_scale` or `to_model_scale`. Its equality is a
       statement about IEEE division, not about `test_the_ROUND_TRIP_returns_the_input`.
```

**The number it publishes is right, and I measured it the honest way so the repair is not
mistaken for a retraction:** composing the SHIPPED `to_full_scale` and `to_model_scale`
under a real module-level injection gives **7 of 7 missed**. So `docs/load-interchange-v1.md`
sec.2.1's "measured, 7 of 7 planted exponent errors survived it" is true; its evidence is
not the thing it names.

**The shipped gate itself does carry its failure**, and that is worth recording in the same
breath: `DIMENSIONS["moment"]` length 2 -> 3 in the module reddens
`test_the_derived_exponents_match_the_DECLARED_table`; `TIME_EXPONENT` 0.5 -> 1.0 reddens
four tests. The defect is in the counter, not in the gate.

**Closed when** the counter injects through the module -- compose `to_full_scale` and
`to_model_scale` for the round-trip half, and run the shipped table assertion (or call the
shipped test function) for the table half -- so that both figures move when the thing they
name moves. The equality on the round-trip control may stay if it does; keep the sentence
that says the blindness is by construction, because that is the claim being made
load-bearing and it is the right claim.

**R579. (a, blocking) The converter cannot express the two composite channels the schema
marks REQUIRED, and scaling one of them silently under-scales half of it.
`floatfea/io/froude.py:96-128`.** This is the case I built to break the step, and it passed
when it should have refused.

```
cell   the schema's own required arrays. /loads/<body>/radiation/mu[N,6] -- force in
       columns 0-2, moment in 3-5. /joints/<id>/lam[N,n_rows] -- yaw_locked is 4 rows,
       three force and one moment.
cmd    to_full_scale(np.ones((2,6)), "force", 50.0)
out    [125000, 125000, 125000, 125000, 125000, 125000]
cmd    the dimensionally correct result
out    [125000, 125000, 125000, 6250000, 6250000, 6250000]
judge  the moment columns come out SHORT by exactly lambda = 50. Scaling the same array
       as "moment" makes the force columns LONG by 50. No name in DIMENSIONS is correct
       for either array, and no call raises. The API takes one quantity per array, and
       the two channels the record must carry are not one quantity.
```

Nothing calls this yet, which is why the harm is latent rather than realised -- and it is
still (a), because `mu` is the first array the converter will be handed and the failure is
silent, not loud. `CLAUDE.md`: "a wrong answer that looks right is worse than a crash."

**Closed when** `to_full_scale` refuses an array whose declared quantity does not cover it
-- either a composite quantity (`wrench`, force rows plus moment rows, with the row map
declared) or an explicit refusal for `mu` and `lam` by name. A silent single-exponent
result for a mixed-dimension array must not be reachable.

**R580. (d, blocking) 25 tests are red at `2dc6a99`, locally and in CI, up from one at
verdict 68. R570 is not answered at its site and the report records it as answered.**

```
cmd  python -m pytest -q 2>&1 | tail -1
out  25 failed, 2729 passed, 2 warnings in 572.15s
cmd  gh run view 36440843564 --log-failed | tail -1      (c78d895, code-identical)
out  25 failed, 913 passed in 290.29s
```

The root causes, measured rather than taken from the report:

```
claim  R570's site was never touched, and the text still says twelve
cmd    grep -rn "twelve are unbuilt" tests/
out    tests/test_report_guard_states.py:628
cmd    git log --oneline -S "twelve are unbuilt" -- tests/test_report_guard_states.py
out    85541e1    -- which is BEFORE verdict 68. e500ea0 did not touch it.
cmd    python -m pytest tests/test_report_guard_states.py -q -s -k corpus_and_the_states
out    23 entries awaiting transcription
judge  the finding was "twelve is 22"; the answer is neither twelve nor 22, it is 23, and
       the sentence still reads twelve. `docs/reports/F2/step-7.md:887-895` declares all
       nine sites ANSWERED with "the text moved with the rewrite". The text did not move.
       Ten of the 25 reds are this, and seven more are guard states whose nested run fails
       on exactly these ten. That is 17 of 25 from one unanswered item.
```

```
claim  the remaining reds are not the `Answers:` class the report attributes them to
cmd    python -m pytest "tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]" -q
out    the nested log names R570-:616 .. :624 and R575-:27, 16 failed, 167 passed
cmd    grep -n "test_the_answered_verdict_is_the_NEWEST_one" (in the failure list)
out    not present -- the Answers header is CORRECT at this commit
judge  `Answers: verdict 68 @ 83c7ba5` names the latest verdict, so my instruction 1b is
       satisfied and that class of red is genuinely closed. The report's section 5 predicts
       "this revision closes them"; the revision landed and the count went 12 -> 25. Six
       more are the absent CI section, which DU1 addresses and which this verdict's bolded
       `Reviewed commit` line should let the generator produce. Two are unsourced numbers
       in the report's own prose.
```

**Closed when** `tests/test_report_guard_states.py:628` states a count that is true at the
commit publishing it -- or, better under BI3, states no count at all and points at
`test_the_corpus_and_the_states_agree`, which prints it -- and the whole suite is green at
the answering commit. The nine sites R570 named are closed site by site, not in a table
that says they moved.

**R581. (a, blocking, one line) `floatfea/io/froude.py:98` -- the lambda guard is defeated
by nan, inf and subnormals.**

```
cmd  froude_factor("force", lam) for lam in {nan, inf, 1e-300, -0.0}
out  nan    -> returned nan     (no raise)
     inf    -> returned inf     (no raise)
     1e-300 -> returned 0.0     (no raise) -- annihilates every scaled array
     -0.0   -> raised ValueError
judge  `if lam <= 0.0` is False for nan, so a nan scale propagates silently into every
       quantity in the record. The module's own test asserts the guard for 0.0 and stops
       there. "Never let a validation failure degrade to a warning" -- this one degrades
       to nothing at all.
```

**Closed when** the guard is `if not math.isfinite(lam) or lam <= 0.0` (or equivalent) and
the counter names nan among the refused values.

## Closure items

None of these blocks. Fix the list once, in the step's closure commit, and do not
re-review them item by item.

* **C1. `tests/test_report_carried.py:2195-2198` -- the R568 repair published two numbers
  that were stale within two commits.** "24 commits behind HEAD" is 32
  (`git rev-list --count 41a200c..HEAD`); "the tree reports 1 failed" is 25; "203 passed"
  is 183 collected in that module now. CP2's exact species, in the prose written around the
  fix. And the whole block is a narrative claim about the repository in the source tree,
  which CW0 says is a test, a triple, or deleted -- it is none of the three. **Closed when**
  the block carries no measured number, or the numbers are in `claim:`/`cmd:`/`ctl:`/`out:`
  form that `tests/test_tree_prose_consistent.py` evaluates.
* **C2. `docs/closure/F2.md:206-224` is wrong again, one commit after being repaired.** It
  names `two_digit_step_number` as the red and `391e375` deleted that state; its `cmd`
  prints `7 failed`, not `1 failed`. **Closed when** section 3 says what is red at the
  closing commit and records that the account is as of a named commit.
* **C3. `docs/milestones/F2a.md`'s ledger row says "46 entries, 24 built, 22 unbuilt at
  this commit"; it is 23 at `2dc6a99`.** Same shape, and the row is the ledger R574 asked
  for, so it is worth getting right. **Closed when** the row cites the reporter instead of
  a frozen count.
* **C4. Three dangling references to the deleted state.**
  `tests/test_report_guard_states.py:212-221` still holds a `REQUIREMENT_CHANGED` entry
  keyed `two_digit_step_number` -- dead data with a present-tense reason for a state that
  does not exist -- and `tests/test_report_carried.py:174, :748` are comments describing
  what the state does. R561 and R571 were both this; this is the third and fourth. **Closed
  when** the entry and the two comments are removed or rewritten in the past tense.
* **C5. `floatfea/io/froude.py:88` -- "Every quantity the interchange schema carries, by
  dimensions" is false.** The schema carries `area[P]` twice (panels, plate patches) and
  `froude_factor("area", 50)` raises. The raise is the right behaviour; the sentence is
  wrong, and it is the sentence that would stop someone checking. **Closed when** it says
  what the table is -- the quantities DR4(c) declared plus the ones needed so far -- or
  `area` is added.
* **C6. `floatfea/io/froude.py:5-6` and `:30-32` state facts about the tree with no triple.**
  "Nothing downstream of the reader multiplies anything by lambda" (true only because
  nothing calls the module at all) and the named test citation. CW0. **Closed when** each is
  a triple or deleted.
* **C7. `tests/verification/rung4/test_froude_scaling.py` is not on the ladder.**
  `docs/verification/README.md` rung 4 lists V4.1-V4.6, all load-mapping; nothing there
  mentions Froude scaling, and the test carries no gate id. It reddens the ladder job, and
  a reader cannot tell from the ladder what rung 4 now asserts. **Closed when** the README
  carries a row for it.
* **C8. `docs/reports/F2/step-7.md:803-804` -- the X-brace sentence, which the implementer
  reported against itself.** I confirmed it independently: `CLUSTER_ANGLES_DEG =
  [0, 90, 180, 270]`, so the arms lie along +/-x and +/-y and it is the ZERO-degree heading
  that runs along an arm. It is a BG0 failure -- a causal sentence with no isolating cell --
  and it is also one of the two number-sourcing reds. **On the deferral: reporting it the
  day it was known is right and I am not asking for a revision.** But withdrawing one
  sentence is a one-line deletion, not a revision, and the sentence is currently keeping a
  test red; DU2/DU3 defer revisions, not retractions. **Closed when** the sentence is struck
  -- in F3's first commit if that is the plan, but say in the strike that the arms are
  axial, because the same belief is in `docs/milestones/F3.md:25` and R576 turns on it.
* **C9. The corrected DQ2 gimbal measurement is not in the repository.** The implementer
  found its own first measurement wrong -- rank over all four constraint rows including the
  translational rows' `-skew(arm_a)` coupling, rather than the rotational row alone -- and
  corrected it before reporting: 16 of 16 two-rotation gimbals, worst released-moment leak
  2.75e-15 relative. **That is the discipline this arrangement is for, and it is the
  strongest thing in this round.** Nothing in `floatfea/` depends on either number and
  neither is published, so there is no stale figure. **Closed when** the corrected
  measurement is written down where F5-prep's DJ0 verification will read it, with the cell
  that distinguishes the two ranks -- otherwise the wrong one is the one somebody re-derives.

## Tolerances touched

**None.**

```
cmd  git diff 0a660ce..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 0a660ce..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        -- CI0: the pathspec resolves; the instruction is not broken
cmd  git diff 0a660ce..HEAD -- .github
out  (no output)
```

The new module imports one existing entry, `ROUNDOFF_IDENTITY = 1e-14`, at three sites.
**That use is inside the entry's declared class and inside its recorded basis, measured
rather than assumed:**

```
rule   the entry's class is "relative agreement for a property EXACT in exact arithmetic,
       dimensionless in every use", basis "worst measured across its sites 4.93 ULP"
cmd    the shipped round trip over all 15 quantities at lambda = 50, worst relative
       residual
out    1.0327e-16 (angular_acceleration) = 0.47 ULP, 96.8x of headroom
judge  the new site is an order tighter than the entry's recorded worst, so the basis
       sentence is not falsified by it and BD1's "set by the tightest member" is not
       triggered. The other use, `abs=ROUNDOFF_IDENTITY` on an exponent equality, is an
       exactness comparison on a dimensionless integer-or-half -- correct form.
```

Two form notes, neither blocking: `LAMBDA = 50.0` and the three exponents carry
`not-a-tolerance` markers with reasons, which is the right shape; and the counter for this
gate is R578's subject, not a `tolerances.py` counter, because no value was added.

## My own instructions (4b)

```
cmd  git diff 0a660ce..HEAD -- .claude docs/SUPERVISOR.md
out  docs/SUPERVISOR.md | 38 ++++++  -- additive only, zero deletions
cmd  git show --stat c78d895
out  docs/SUPERVISOR.md alone, a standalone `process:` commit citing DU1
```

**Not a STOP-class finding.** DU1 adds two format rules about my output and removes no
guard; I read the diff line by line. I have complied with both in this verdict: the judged
commit is restated bolded and backticked above, and every blocking finding heads
`**R<n> (<class>, blocking)**`. No commit in this range touches both my instructions and
`floatfea/` or `tests/`.

## Corpus this round (BE3)

**`tests/corpus/froude_scale_boundary.txt`, batch 17, committed separately at `b9dd027`.**
Not an apparatus corpus -- its surfaces are `floatfea/io/reader.py` and
`floatfea/io/froude.py` -- so DE2 and DR1 do not reach it and it is not deferred to 4a.

**37 new entries, none of them seen by the implementer. 20 of the 37 are already violated
by the shipped code or the shipped checks; 17 are met.** That is the coverage measurement,
and it is the implementer's own count that it replaces: DS2's counter reports 7 of 7
planted shapes caught, and 7 of 7 is coverage of the seven rows DR4(c) wrote.

The three that carry the most: `reader_scale_model_accepted` (R577),
`froude_mu_scaled_as_force` (R579), `counter_injection_is_inert` (R578). The 17 met are
worth as much as the 20 missed -- every unknown-quantity entry raises, which is the right
behaviour and is the strongest thing about the module.

**The standing measurement.** `cmd grep -h "^id=" tests/corpus/*.txt | wc -l`; `out` 1162
entries across 18 files. Of the apparatus corpus, 23 entries remain untranscribed and are
ledgered in `docs/milestones/F2a.md` under DR1 -- one more than the ledger says, because
`391e375` deleted another built state (C3). **Verdict 68 measured zero new entries and said
so; this round measured 37, and 20 of them came back red.** That is the only number here
that says whether any of this works, and this round it says the boundary was not checked
by anything outside the hand that wrote it.

## On the criterion, once, and it is not a disagreement

CZ0 is the right rule and it did work this round: six of verdict 68's eight items were
prose, they were fixed in one commit, and I have not re-reviewed them individually. Two
notes rather than an objection.

**First, a STOP is not one of CZ0's four heads and should not be read as an exception to
it.** CZ0 governs what consumes a review round; "the locked plan is wrong" ends the round
structure rather than spending one. I am flagging the seam because a reader comparing
R576 against (a)-(d) will not find it there.

**Second, and this is the one I would put in front of Xabier: a prose finding that keeps a
test red is not a prose finding.** C8's X-brace sentence and C1's stale numbers are exactly
the class CZ0 demoted -- and `test_every_number_in_prose_is_sourced_in_its_own_section` is
red on both, so the tree cannot be green while they stand. Under CZ0 they are closure items
that wait for the closure commit; under CZ0 (d) the tree they keep red is blocking. That is
not a contradiction to resolve in a verdict, but it does mean "fix the closure list once, at
the end" and "get to green" are the same deadline for a subset of the list, and the report
should not plan around them as if they were not.

I am not asking for a ruling to proceed. This goes to Xabier through the implementer and
does not become another round.

## Next step opens when

**Step 7 is closed and stays closed. Nothing here reopens it.** This verdict is about the
tree, and about a plan locked at the commit it judges.

1. **F3's plan reopens (R576).** It is not executed against in the meantime -- and it has
   not been, which I verified: no code was written against a substitute layout source.
   DJ1 gets a source that exists, the arm directions as measured, and DJ2 gets a decision
   on heading 45. **Per DK0 the re-lock does not restart the verdict count.**
2. **R577, R578, R579 and R581 are answered in `floatfea/` and in the rung-4 module.** They
   are one commit's work between them and none needs new apparatus: R577 is a check in an
   existing validator with a new `Fault` member, R578 is a change of what the counter calls,
   R579 is a refusal, R581 is one predicate.
3. **R580 clears when the suite is green at the answering commit**, with R570's nine sites
   closed site by site rather than declared moved in a table.
4. **The nine closure items land in one commit** and are not re-reviewed individually.
5. **`Answers: verdict 69 @ 2dc6a99`** is the header the next report carries. This is the
   latest verdict as of this commit, and `2dc6a99` is the commit it judged; the stamped
   header on this file is my corpus commit `b9dd027`, per R513.
6. **One round remains against the cap** before it closes the next step (DR1: verdict 68
   was the first, this is the second). Spend it on `floatfea/` -- the element and the
   boundary -- not on the harness.
