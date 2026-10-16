# Review — R1 step 1
Reviewed commit: 60f3176a0796c298d55d79494c7aa013abb1fd16
**Reviewed commit: `60f3176a0796c298d55d79494c7aa013abb1fd16`.**
Verdict: PASS
Tests: 3554 passed, 13 failed, 1 skipped   (my own run, `python -m pytest -q`, 679.10s)

**THIS IS AN INTERIM CHECK UNDER ES0 AND IT COUNTS AGAINST NO ROUND.** There is no new
report revision and there cannot be one: step 1 closed at verdict 3 with
`Closes: R1/step-1`, and ES0 caps the step at three reviewed revisions. The `Stop` hook
forced this check because `floatfea/run/config.py` moved after that verdict. Light scope
as ES0 writes it: the suite and CI at the commit, plus a CZ0 (a)-(d) scan of the diff.
No corpus batch, no closure list.

**THE DISPOSITION WORD IS `PASS` AND IT IS NOT AN ENDORSEMENT -- R822 BLOCKS.** The
reasoning is set out once, under its own heading below, because the honest reading of my
own instructions is that a blocking finding wants a HOLD and HOLD is not available here.
R822 joins step 1's carried list and is answered in step 2's FIRST commit, before any FL2
work, alongside R817 to R821 under FO3.

**EU1: I agree it does not attach, and I ran the adversarial case anyway -- and that is
what found R822.** `git diff 2042c56..HEAD -- floatfea/tolerances.py` is empty, the diff
declares no counter, and nothing in it is a value chosen to make two numbers agree. But
the scan of the diff is not what found the finding; running the loader at inputs the diff
did not choose is, which is EU1's own stated reason rather than its scope.

## Carried

**Verdict 3's five blocking items: NOT RE-REVIEWED AND ALL FIVE STILL OPEN.** The diff
since verdict 3 is one function body in `floatfea/run/config.py` and touches none of
them.

| item | status | where |
|---|---|---|
| R817 (heading and wave height absent from all three artifacts) | **still open** | the diff is `floatfea/run/config.py` alone, 22 insertions, 2 deletions; `results/` and `floatfea/run/pipeline.py` are untouched |
| R818 (the two declared sensitivities reach no artifact) | **still open** | same diff; `provenance()` at `floatfea/run/config.py:405` is outside the changed hunk, which is `:62-96` |
| R819 (the R741/R742 caveat refuted by the code at any `Fy`) | **still open** | `floatfea/checks/api_wsd.py` and `floatfea/cli.py` untouched |
| R820 (R814's repair held in place by nothing) | **still open** | `tests/unit/test_run_pipeline_refusals.py` untouched |
| R821 (`study_only` asserted by no test) | **still open** | same |

That is correct and expected: 60f3176 is a CZ1 (iv) follow-on answering the CI red at
2042c56, not a revision answering verdict 3. Recorded so the list is re-read rather than
assumed, which is the one thing this project has already failed once.

**Verdict 3's named conditions 6 and 7 have both MOVED, and condition 7 is CLOSED.**

| condition | status |
|---|---|
| 7. Push the branch | **DONE, and it is the most valuable thing in this commit history.** `git ls-remote --heads origin` gives `60f3176a... refs/heads/F3`. The first CI run any R1 work has ever had found a red that four local gates on this machine cannot produce, and it had skipped `unit tests` and `guards and meta-tests` behind it. CI has now RUN R1's unit tests (success) and its guards. Three verdicts asked for this; it bought a finding immediately, which is CZ1 (iii) measured rather than argued. |
| 6. EG3(ii), the verdict commit measured | **done by me instead, and it produced the control the EG3 enumeration needed.** See the trace section. |

**C22's premise has moved and the item narrows.** With the branch pushed,
`python scripts/ci_section.py --rounds` now exits 0 and emits the table; only the
per-commit form still refuses, and for a different reason than verdict 3 recorded.

```
claim  the rounds generator works now and the per-commit generator still does not
cmd    python scripts/ci_section.py --rounds > /dev/null ; echo exit=$?
out    exit=0      and the table carries both runs: 38834673534 at 2042c56, failure;
                   38835420645 at 60f3176, failure, 13 failing test names
cmd    python scripts/ci_section.py > /dev/null ; echo exit=$?
out    exit=1      no CI run at 582cde72..., and the commit touches paths the workflow
                   does NOT ignore
rule   verdict 3's C22 -- scripts/ci_section.py refuses with exit 1 where it should emit
       the section body
judge  the remaining refusal is no longer about a push policy. It anchors on the commit
       the newest REPORT revision answers, 582cde7 at verdict 2, and that commit predates
       the push, so no run will ever exist for it. C22's repair is unchanged in substance
       and its justification sentence is now wrong. Re-measure it in step 2's first
       commit rather than carrying verdict 3's wording.
```

## Findings

One blocks. Two are recorded, named and do not block. One is a correction to the EG3
enumeration, measured, which is Xabier's directive to adopt and not mine.

**R822. (BLOCKS -- CZ0 heads a and c) THE DUPLICATE-KEY GUARD NOW KEYS ON THE KEY'S TEXT
WHILE PyYAML BUILDS THE DICT FROM THE KEY'S CONSTRUCTED VALUE. Where the two differ the
duplicate is accepted and silently resolved last-wins -- five measured classes, refused
one commit earlier -- and the gate that should hold it cannot contain the failure.**

The commit's own sentence is the claim: *"A config key is a YAML scalar -- these are field
names -- so `ScalarNode.value` is the identity the duplicate check wants."* `ScalarNode.value`
is the key's TEXT. The identity PyYAML uses when it builds the mapping is the key's
CONSTRUCTED value, and YAML 1.1 implicit typing makes those two different functions.

```
claim  five classes of duplicate key are refused at 2042c56 and silently last-wins at
       60f3176, one variable moved -- the commit
cmd    the same 17-case table loaded through `_NoDuplicateLoader` in two trees: HEAD, and
       `git archive 2042c56` unpacked into the scratchpad
out                        2042c56                      60f3176
       no: / No:           ConfigError duplicate False   OK  {False: 2}
       yes: / true:        ConfigError duplicate True    OK  {True: 2}
       ~: / null:          ConfigError duplicate None    OK  {None: 2}
       1: / 01:            ConfigError duplicate 1       OK  {1: 'b'}
       1.0: / 1.00:        ConfigError duplicate 1.0     OK  {1.0: 'b'}
       control, a: twice   ConfigError duplicate 'a'     ConfigError duplicate 'a'
rule   `floatfea/run/config.py:48-61` -- "A YAML loader that REFUSES a duplicate mapping
       key (R811). `yaml.safe_load` is last-wins and silent, which is the worst of the
       three possible behaviours."
judge  in every one of the five the reader sees two values in the file and the run gets
       the second. That sentence is R811's whole content, and the module docstring is the
       only place this repository states it.
```

```
claim  it is reachable through a DECLARED FIELD of the shipped schema, and the surviving
       key looks legitimate
cmd    the shipped example with paths absolutised, `platform: {f: 0.75}` replaced by an
       explicit distribution, through `load_config`
out    line_masses: {1: 100.0, 01: 900.0}   -> LOADED  line_masses={'1': 900.0}
       line_masses: {no: 100.0, No: 900.0}  -> LOADED  line_masses={'False': 900.0}
       control, 1: twice                    -> REFUSED "duplicate key '1' at line 35"
rule   `floatfea/run/config.py:527-529` -- the comprehension keyed on `str(g)` over
       `lines.items()`
judge  `line_masses` is keyed by member group and the group names are the USER's, which is
       the one free-form key space the step-1 schema has. `str(g)` then turns the collapsed
       key back into a plausible string: the file declares two line masses in kg/m and the
       configuration object carries one, under a name (`'1'`) indistinguishable from the
       first of them. A line mass is a load.
```

```
claim  no number ships from this today, and the exposure opens in the very next step
cmd    floatfea/run/pipeline.py:155-163
out    the modes check raises -- "only the `f` (fraction) mode is wired to the builder in
       R1 step 1 ... FL2 wires it; until then this is refused rather than half-applied."
rule   CZ0 (a), a defect in `floatfea/`
judge  the pipeline refuses explicit mode, so the silently-wrong configuration object
       cannot reach a member force at this commit. **It is still a defect in `floatfea/`**
       -- the loader's stated guarantee is false for a measured class of its own declared
       input -- and the step that wires explicit mode is FL2(a), which is the step this
       finding carries into. The fix and the exposure are in the same step, which is why
       the condition is "step 2's first commit" and not "eventually".
```

```
claim  the gate's three parametrisations cannot contain the failure, and the commit
       message's own behavioural command is blind on exactly the axis the diff moved
cmd    tests/unit/test_run_pipeline_refusals.py:400-407 -- the three needle/addition pairs
out    ("    Fy: 355000000.0", "    Fy: 275000000.0")
       ("  platform: {f: 0.75}", "  platform: {f: 0.30}")
       ("  K: 2.0", "  K: 3.0")
cmd    python -m pytest -q tests/unit/test_run_pipeline_refusals.py
out    22 passed
rule   the gate's own docstring -- "Parametrised across three sections because a loader
       fixed for one mapping depth can still be last-wins at another"
judge  all three duplicates are TEXT-IDENTICAL, so all three are green under either
       keying. The gate is parametrised over mapping DEPTH and the change moved key
       IDENTITY; the collection the assertion inspects cannot contain the failure. The
       commit message attaches `-k "R811 or FO0 or duplicate" -> 8 passed, 37 deselected`
       to the sentence "loses no duplicate a configuration could express", and that
       command cannot refute that sentence. This is R755's shape -- right about the axes
       its author swept, silent about the one with nothing on it -- and R820's shape one
       verdict earlier: a behavioural claim carrying a command that measures something
       adjacent.
```

```
claim  a repair exists that is complete, typed under BOTH stub versions, and needs no
       ignore -- so the condition is closeable rather than a wish
cmd    mypy --python-version 3.13 --strict --warn-unreachable --warn-unused-ignores on a
       scratch file calling loader.construct_scalar, flatten_mapping, construct_mapping
out    construct_scalar -> str ;  construct_mapping -> dict[Hashable, Any] ;
       flatten_mapping typed ;  Success: no issues found in 1 source file
cmd    the same 11-case table through a prototype that flattens merges first, keeps the
       text check, then compares len(mapping) against len(node.value)
out    all five collapse classes REFUSED, "collapsed duplicate: 2 keys -> 1 entries";
       plain dup REFUSED; clean nested OK; a single merge OK; a two-source merge OK
rule   CZ0 (a) -- the condition has to be closeable without reintroducing the ignore CI
       rejected
judge  **this is a demonstration that a typed route exists, NOT a prescription.** The
       property the repair needs is that the check's key identity is the identity PyYAML
       uses to build the dict; how that is spelled is the implementer's. Note that
       `construct_scalar` alone does NOT fix it -- it returns the text.
```

**Closed when** the five classes above are refused again (the two-tree table is the
counter-case, and a text-identical control stays refused so the check is not simply a
blanket raise); the R811 gate gains at least one case whose two keys differ in TEXT and
agree after construction, so the collection can contain the failure; and the docstring
sentence at `floatfea/run/config.py:77-81` is corrected or deleted (CW0 -- it is the only
statement in this repository of what the loader guarantees, which is why it closes with
the code and not in a ledger). Regenerated at the answering commit (CP3).

**R823. (DOES NOT BLOCK -- recorded and named) The implementer's own question, answered:
the `continue` loses nothing, by measurement, and the reason given for it is not the
operative one.**

```
claim  no non-scalar key node can carry a duplicate past the check
cmd    six documents through `_NoDuplicateLoader` at HEAD, one per non-scalar tag
       SafeLoader can construct, plus a duplicate pair
out    a !!seq key     ConstructorError, found unhashable key
       a !!map key     ConstructorError
       a !!set key     ConstructorError
       an !!omap key   ConstructorError
       a !!pairs key   ConstructorError
       a seq key twice ConstructorError
rule   the docstring's claim -- "skipping it loses no duplicate a configuration could
       actually express"
judge  **the claim is TRUE and I confirm it.** The operative reason is not "a non-scalar
       key cannot be a field in this schema" -- the loop runs over EVERY mapping in the
       document, not only the field mappings -- it is that every non-scalar node
       SafeLoader can construct is UNHASHABLE, so PyYAML refuses the document downstream.
       The behaviour is right; the sentence attributes it to the wrong mechanism. At
       2042c56 the same six gave a bare `TypeError: unhashable type` from inside the
       check, so the `continue` also turned that into a located YAML error. An improvement.
```

```
claim  merge keys went from a hard crash to working, and merged keys bypass the duplicate
       check entirely
cmd    the same documents in two trees, then a merge through the real schema
out    2042c56  a merge key gave ConstructorError, could not determine a constructor for
                the tag tag:yaml.org,2002:merge -- ANY merge key crashed
       60f3176  the same document loads: {'base': {'x': 1}, 'd': {'x': 1, 'y': 2}}
       60f3176  the example with an anchored `platform: {f: 0.75}` and a `hub1` that
                merges it and then overrides -- LOADED, hub1 f = 0.1, platform f = 0.75
rule   `SafeConstructor.construct_mapping` calls `flatten_mapping` INSIDE itself, so
       `config.py:96` runs the merge AFTER the loop at `:84-95` has finished
judge  not a defect -- merge is YAML's own feature and explicit-wins is its own rule, so
       no explicitly written value is silently lost. It is an UNDECLARED WIDENING of the
       accepted input language: `_NoDuplicateLoader` now admits anchors, aliases and
       merges that it rejected outright one commit ago, nothing in the schema documents
       them, no test exercises them, and R811's premise is that a reader can see the
       effective value at its own key. Named for step 2's list rather than ledgered,
       because step 1 has no open ledger and FL3(a) has to document the input language.
```

**R824. (DOES NOT BLOCK -- recorded and named) The environment divergence that produced
this red is STRUCTURAL, not a one-off, and "no local command could have found it" is true
of the pinned tree and false of the cause.**

```
claim  both type-checking inputs are unpinned floors and CI resolved different ones
cmd    grep -n types-PyYAML and mypy in pyproject.toml ; mypy --version ; the CI install log
out    pyproject:  "types-PyYAML>=6.0"   "mypy>=1.9"
       local:      types-PyYAML 6.0.12.20260408 ; mypy 1.20.2
       CI run 38835420645: types-PyYAML-6.0.12.20260906 ; mypy-2.4.0
cmd    mypy --python-version 3.13 --strict on a scratch call to construct_object, locally
out    error: Call to untyped function "construct_object" in typed context [no-untyped-call]
rule   CZ1's reusable half -- a check whose input is the commit itself cannot be measured
       before the commit exists -- and its sibling, a check whose input is a RESOLUTION
       cannot be measured in a different one
judge  the diagnosis in the commit message is exact and I reproduced every figure in it.
       What it does not say is that CI runs a different MAJOR version of the type checker,
       2.4.0 against 1.20.2, so `mypy floatfea` locally and `mypy` in CI are two
       instruments, and this class of red will recur on the next stub or checker release.
       Not (a)-(d): `pyproject.toml` is project configuration, not `floatfea/` behaviour,
       not a tolerance, not a gate assertion, and no test is red for it. Named because the
       cheap options -- pin both, or resolve CI's set locally before pushing -- are a line
       each, and because "no local command could have found it" will otherwise be read as
       a permanent property of the tree.
```

## THE EG3 ENUMERATION IS SHORT BY ONE NAME, MEASURED (not adopted by me)

13 failed locally and 13 failed in CI, and the two sets are identical. Twelve map onto
EG3's two lists as corrected by EH1, EJ2, FC1 and FN2. **One is on neither list**, and I
ran it individually rather than as part of a cascade, which is what EG3(i) exists to force:

```
tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph
    AssertionError: no `## 0a` table in the newest revision.
```

```
claim  it is verdict-dependent by measurement, against a verdict-exists control
cmd    a git worktree at bd315a1, a commit where report and verdict are in sync; then
       python -m pytest -q tests/test_report_carried.py tests/test_report_guard_states.py
out    149 passed in 134.82s    -- 0 failed
rule   FN2's membership rule -- "verdict-dependent, measured against a verdict-exists
       control, and the enumeration is a convenience that has now been short twice"
judge  it is green where an answering revision exists and red here, so it belongs on
       **state (2)'s** list: only the answering report can add the `## 0a` table, and EK3
       bars adding one to step 1's closed report. The enumeration has now been found short
       four times -- two names each side at EH1, two placements at EJ2, three at FN2, and
       this one. **The pattern is the finding, not the name:** a list of names cannot be
       checked against a failure message, and only running the id at a control settles it.
       I record the measurement; adopting it into `CLAUDE.md` is a directive and Xabier's,
       not mine.
```

## The 13 reds, traced by name (EG3(i)), and why CA2 does not HOLD here

**CI at the reviewed commit is RED and I am not ruling it a blocking (d).** The trace is
the condition and it is pasted.

```
cmd    gh run list --commit 60f3176a0796c298d55d79494c7aa013abb1fd16 --json name,conclusion,workflowName,status
out    [{"conclusion":"failure","name":"CI","status":"completed","workflowName":"CI"}]
cmd    gh run view 38835420645 --json jobs, step conclusions
out    lint, unit and guards : FAILURE
         actionlint success / ruff success / black --check success / mypy SUCCESS /
         unit tests SUCCESS / guards and meta-tests FAILURE
       the verification ladder : SUCCESS, rungs 1, 2, 3, 6, 4, 5 all success
       CI determinism -- leg, and ten legs agree : skipped
cmd    sed -n '85,95p' .github/workflows/ci.yml
out    the determinism jobs are gated on the workflow_dispatch event -- CK0, by hand only
cmd    the CI log's outer short-summary, against my own python -m pytest -q
out    CI    : 13 failed, 1124 passed, 1 skipped in 458.16s
       local : 13 failed, 3554 passed, 1 skipped in 679.10s
       the two FAILED id lists are IDENTICAL
```

The 13, each matched to its state's own list:

* `test_the_report_carries_a_CI_SECTION` -- state (1), FN2
* `test_the_reported_CI_counts_are_not_all_zero` -- state (1), FN2
* `test_the_CI_section_is_about_the_REVIEWED_commit` -- state (2), EG3
* `test_the_report_carries_a_WHOLE_SUITE_count` -- state (2), FC1
* `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` -- state (2), FC1
* `test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` -- **off both lists**,
  measured verdict-dependent at the bd315a1 control above
* `test_the_guard_survives_the_state[baseline]` and six planted states --
  `non_numeric_step_suffix`, `superscript_digit_step_number`,
  `draft_suffix_beside_a_step_report`, `step_number_is_the_empty_string`,
  `verdict_amended_after_the_commit_the_report_answers`, `zero_padded_step_number` --
  the cascade, identified as EH1 requires by the baseline being red and by each state's
  own failure line embedding the inner run's `6 failed, 230 passed, 1 skipped`

```
claim  not one of the 13 is red where an answering revision exists
cmd    the two report-guard files at bd315a1, a verdict-exists commit
out    149 passed, 0 failed
rule   EG3 as corrected by FN2 -- membership is verdict-dependent, measured against a
       verdict-exists control
judge  this tree is EG3 state (2): verdict 3 at 2042c56 is newer than report revision 3,
       whose `Answers: verdict 2 @ d511a0c` line is correct for the revision it is. The
       state clears BY THE ANSWERING REPORT and not by time, and step 1's answering report
       cannot be written -- ES0 caps the step and EK3 bars touching a closed report. **So
       the state clears at step 2's report and nowhere earlier.** Every red traces, so the
       waiver's condition is met and none is CZ1 (iv).
```

**On CA2, which I keep in full because `CLAUDE.md` does not carry it.** CA2 says a red CI
is a HOLD regardless of the local run. EG3 is the clause that qualifies CZ0's head (d) for
a step's own boundary red on EITHER side of the verdict, and it is written about CZ1 step
(iii), which IS the pushed run. Every one of the 13 is that boundary red, by name and by
control. **The red is recorded as red with its cause named, and it does not HOLD.** What
would HOLD is a fourteenth, and there is none: `mypy`, `ruff`, `black`, `unit tests` and
all six ladder rungs are green in CI at this sha, which is the first time in this
milestone that any of it has been true.

## Why PASS and not HOLD, said once

R822 blocks under CZ0 (a) and (c). My instructions say not to soften a HOLD into a PASS,
and I am not: I am recording that **HOLD's own definition is unavailable at this commit**,
and saying so where it can be disagreed with.

HOLD means "the step stays open; the listed items are answered before anything else, and
the next step does not begin." Step 1 does not stay open -- verdict 3 is its closure
verdict, PASS, carrying `Closes: R1/step-1`, and DD1 says a step's disposition is read
from its closure verdict and that a later verdict about the state of the TREE does not
reopen it. Step 2 has already begun. And a HOLD written into this file puts the `Stop`
hook, which reads the last line, into exactly the documented conflict with DD1 that cost
two verdicts in F6, neither of which was about the work.

ES0 designs the alternative and I am using it rather than inventing one: *"Its findings
join the step's list and are answered in the next revision."* R822 joins R817 to R821,
stays blocking, and goes into step 2's FIRST commit before any FL2 work under FO3 -- which
is also when its exposure opens, because FL2(a) is what wires the explicit mass
distribution the finding is reachable through. The practical effect of a HOLD is obtained
without re-creating the trap.

**If that reading of ES0 and DD1 is wrong, it is wrong about the criterion and not about
the work**, and it goes to Xabier through the implementer rather than becoming another
round. Said once.

## The adversarial cases I ran, and what they found

* **The loader's key-identity space, 17 cases in TWO TREES** -- text duplicates, the five
  YAML 1.1 implicit-type collapses, quoted against plain, alias-as-key, nested depth, and
  six non-scalar key tags. One variable moved: the commit. **R822** and **R823**.
* **The configuration the diff did not choose, through the real schema** -- the shipped
  example with an explicit `line_masses` distribution, at numeric and boolean-looking group
  names, with a text-identical control. That is what turned R822 from a property of a
  loader into a property of a declared field.
* **A merge key through the real schema**, shadowing an anchored `f: 0.75` with `f: 0.10`
  on `hub1`: loads, where it crashed one commit earlier. **R823.**
* **A typed repair prototyped against all 11 cases**, so R822's condition is closeable
  without reintroducing the ignore CI rejected.
* **The verdict-exists control at bd315a1**, which made the 13 a measurement rather than a
  family resemblance -- and which found the off-list name.
* **Both type-checking instruments compared**, local against CI's resolved set. **R824.**

What I did NOT find: the `continue` the report asked me to attack is sound. Six non-scalar
key tags, every one refused. I tried to build a non-scalar key that reaches the schema and
there is none, because every non-scalar value `SafeLoader` constructs is unhashable. The
hole is one line above it, on the axis nobody was looking at.

## Corpus (EG4(e))

**The pause held. Zero new entries this round** -- `tests/corpus/` is untouched by me, and
ES0's light scope says no corpus batch for an interim check, so there is no coverage count
to report. R1 step 1 touches neither exception: not F4's load-mapping gate, not EB6's
label-provenance gate.

I ran **the recorded substitute's first half** instead -- a continuum grid over the
parameter space a decision rule guards, here the key-identity space of
`_NoDuplicateLoader`, swept in two trees. It produced this round's only blocking finding.
The second half, a regeneration check on a published deliverable, I did not run: the diff
touches nothing any deliverable reads, and verdict 3 regenerated all three artifacts line
for line one commit ago.

## Tolerances touched

**None.**

```
cmd    git diff 2042c56..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 2042c56..HEAD, searched for isclose, abs_tol, rel_tol, approx, atol, rtol
       and bare numeric comparisons
out    no new comparison; the diff's only comparisons are a set membership test on a
       string and an isinstance against yaml.ScalarNode
```

Neither is a tolerance under any name: one is set membership on a string, the other a type
test. The five collapse classes in R822 are not a tolerance either -- nothing in them is a
value chosen to make two numbers agree, and the repair direction is a stricter refusal,
not a wider one. **EU1 therefore does not attach, and I say so having run its measurement
anyway rather than having inferred it from the diff.**

## Next step opens when

Step 2 is already open (verdict 3). What this check changes is the content of its first
commit, and these are the conditions rather than "the above":

1. **R822** -- the five collapse classes refused again, with a text-identical control still
   refused; one R811 case whose two keys differ in text and agree after construction, so
   the gate's collection can contain the failure; and `floatfea/run/config.py:77-81`
   corrected or deleted. In the SAME commit as R817 to R821 under FO3, before any FL2
   work, and before FL2(a) wires the explicit mass distribution it is reachable through.
2. **R817, R818, R819, R820, R821** -- unchanged from verdict 3, all five still open, each
   with its own condition in that verdict's `Next step opens when`.
3. **R823 and R824** -- recorded, not blocking. The merge and anchor widening is documented
   or refused, and the two type-checking floors are pinned or CI's resolution is run
   locally before a push. Neither is (a)-(d) and neither should consume a round.
4. **C22, re-measured rather than re-quoted.** Its repair stands; its justification
   sentence does not, because `--rounds` now works and the per-commit form refuses for a
   reason the push cannot fix.
5. **The push, continued.** It is closed as an open item and it should not become one
   again: push the report commit BEFORE invoking me, as the report proposes -- **and push
   the verdict commit too**, because `scripts/ci_section.py` anchors on the commit the
   report answers, and FC1's two guards need a run at the commit they describe. **Yes to
   the process change, with that addition.** It makes CA2 measurable at every reviewed
   commit for the first time in this milestone, and this commit is the argument for it:
   one push found a red that four green local gates could not produce.

**What this commit got right, and it is most of it.** The repair removes the condition
rather than the symptom, which is the right instinct; the diagnosis of the stub divergence
is exact and every figure in it reproduced; the commit is a standalone CZ1 (iv) follow-on
that touches nothing else, with `floatfea/tolerances.py`, `tests/conftest.py`, `.claude/`
and `docs/SUPERVISOR.md` all untouched, each diffed separately; and the question the report
asked me to attack was the right question, asked honestly, about the right line of the
diff. It was one line away from the hole.

**The pattern, named once more because it has now held for four consecutive rounds.**
Verdict 2: the verifiable half gets verified and the deciding half gets described.
Verdict 3: the deciding half is no longer the repair, it is what holds the repair. This
round: **the deciding half is the axis the author did not sweep.** The commit carried a
behavioural command for its behavioural claim -- which is more than BF0 asks -- and that
command was parametrised over mapping depth while the change moved key identity. R755 was
this. R820 was this. The cheap question that catches it is not "is there a command?" but
"can that command fail on the axis this diff moved?"


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 1
Reviewed commit: 62a8281cd0eba008c6c135775199dec86749f7e7
**Reviewed commit: `62a8281cd0eba008c6c135775199dec86749f7e7`.**
Closes: R1/step-1
Verdict: PASS
Tests: 3554 passed, 13 failed, 1 skipped   (my own run, `python -m pytest -q`, 689.53s)

**THE PASS IS ES0's CAP CLOSING THE STEP, NOT AN ENDORSEMENT OF THE TREE.** This is the
THIRD reviewed revision, which is the last this step gets, and five blocking items are open.
`CLAUDE.md` Â§ Step gating says what happens to them: *"A blocking item still open at that
point carries by name into the next step's `Carried` section and stays blocking there."*
R817, R818, R819, R820 and R821 carry, they stay blocking, and under FO3 they are answered in
step 2's FIRST commit before any FL2 work. Written with `--closes R1/step-1` (FK1) because
the step closes; the items do not.

## Carried

**Verdict 2's three findings. All three are answered on the substance DIRECTIVE FO ruled, and
two of them left a new hole that this round measures.**

| item | status | where |
|---|---|---|
| R814 | **answered on the code; what holds it is R820** | `floatfea/run/pipeline.py:290-291` -- `DENSITY` is no longer imported, the comparison is `== 0.0`, and `f = 0.0106` runs. I re-measured the acceptance set at `f = 1e-09, 1e-04, 0.0053, 0.0106, 0.75`: all five ACCEPTED, which is FO0 exactly. What nothing holds in place is the absence -- R820. |
| R815 | **answered** | all eleven markers in all three artifacts, verified by me below, and the gate's list is the condition's list in both halves (`tests/regression/test_r1_published_artifacts.py`, `tests/unit/test_run_pipeline_refusals.py:475`). The REWORDING is R817 and R819. |
| R816 | **answered** | `tests/regression/test_r1_published_artifacts.py` reads the committed files. I removed one caveat from the artifact and one from the generator and both halves reddened, by file and by marker. |

**Verdict 2's seven named conditions, one by one -- a closing condition that names sites is
closed site by site.**

| condition | status |
|---|---|
| 1. R814's floor | **done on the code, OPEN on the pin.** Verdict 2 asked for BOTH edges; only the refused edge (`f = 0.0`) is pinned. R820. |
| 2. R815's five caveats, and the gate's marker list | **done**, and the rewording introduced R817 and R819. |
| 3. R816's published-string assertion | **done.** The governing line is asserted in full and the doubled prefix reddens by construction. |
| 4. C11 (`floatfea/run/pipeline.py:9-28`, FF0 class, due in the next commit) | **NOT DONE.** Still "Four declared things reach the model today", and FO1 made it shorter by one more: `froude_lambda` is now read from the npz as well. Re-listed as C19. |
| 5. FN0's open half | **done.** The re-export happened, the key is in the npz, `--check` completes, and the premise "it cannot be re-exported here" is withdrawn by the implementer in its own words. |
| 6. EG3(ii) | **done** -- `15 failed, 240 passed, 1 skipped` at `d511a0c`, consistent with verdict 2's own whole-suite count of 15 at `582cde7`. I did not re-run it; the clause assigns that measurement to the implementer. |
| 7. Push the branch | **REFUSED BY THE ENVIRONMENT, and recorded under its own heading, which is exactly what the condition asked for if pushing was unavailable.** Fourteen commits unpushed, `origin/F3` still at `bd315a1`, and FL1(c)'s golden has now never run in CI for three rounds. Carried as a named condition, not as a finding against the implementer. |

**Verdict 1 and 2's closure items.** C9 and C10 are closed. C12, C13, C14, C15, C16, C17 and
C18 remain open and are not re-reviewed. C11 is re-listed as C19, because it was due in the
next commit and the next commit did not carry it.

## Findings

Five, all (a) or (c). Three are in the three published artifacts; two are in what holds the
repairs in place. **Four of the five are inside the REPAIRS of verdict 2's findings**, which
is the case EQ0 was written for: the substance FO ruled is done, and the half that decides
whether a reader or a test can tell is not.

**R817. (BLOCKS -- CZ0 head a) The three published artifacts state neither the HEADING nor
the WAVE HEIGHT, and two of the caveats they carry are about exactly those two facts. The
committed deliverables they replace stated both.**

```
claim  the heading appears nowhere in the published artifacts except inside the caveat that
       refers to it
cmd    grep -in "heading" results/R1/example/report.md results/R1/example/utilisation.csv
       results/R1/example/member_forces.csv
out    one hit per file, and each is the EX3 / R724 caveat line itself --
         "every case in a run carries the heading its load cases declare. Where that is a
          single heading the heading dependence is UNTESTED"
cmd    grep -in "heading" docs/F6_utilisation.csv docs/F4_member_forces.csv
out    F6_utilisation.csv:10   "EX3 / R724: all cases are heading 0 degrees."
       F4_member_forces.csv:6  "EX3 / R724: all six cases are heading 0 degrees."
rule   verdict 2's R815 -- the replaced deliverable's header is the standard, because this
       artifact "replaces it for a reader"; and EX3/R724 is a recorded finding ABOUT the
       heading
judge  the caveat warns that the heading dependence is untested WHERE the run is a single
       heading, and the artifact never says how many headings there were, or which. In the
       file that carries it, the sentence is a tautology.
```

```
claim  the same for the wave height, which is the quantity the admissible period band is
       computed from
cmd    grep -inE "24\.2|wave height|steepness" results/R1/example/report.md
out    two hits, both caveat text ("... outside the associated-period range for this wave
       height ..."); no value of H anywhere, and no band bounds
cmd    the committed deliverable
out    F4_member_forces.csv:11  "T = 10 s and T = 20 s are outside the associated-period
       range for H = 24.2 m -- and T = 10 s exceeds the deep-water breaking steepness"
rule   FA0's caveat as republished -- "a governing period sitting just below the band's LOWER
       BOUND is IN by FA0's ruling rather than by rounding"
judge  the artifact publishes rows at `T = 10` and `T = 20`, lists four admitted periods, and
       names neither the band nor the `H` it is computed from. A reader cannot check that
       `12.5 s` is `0.042 s` below `sqrt(6.5 H)`, which is the whole content of FA0.
```

```
claim  both facts are available where the pipeline already reads, so this is a provenance
       line and not a measurement
cmd    python -I -c "import json; print(json.load(open('data/f4/dynamic_inputs.provenance.json'))['run'])"
out    {'heading_deg': 0.0, 'wave_height_model_m': 0.484, 'wave_height_full_m': 24.2,
        'periods_full_s': [10.0, 12.5, 14.0, 15.0, 16.2, 20.0], ...}
rule   `floatfea/run/pipeline.py:502` -- `exported_froude_lambda` already opens that sidecar
judge  the repair is one or two lines in `RunConfig.provenance()` plus the case that reddens
       when they are dropped. FL2(c) and FL2(d) need both fields anyway.
```

**Closed when** the heading (or heading list) and the wave height reach the provenance block
of all three artifacts, with the band's two bounds wherever a caveat refers to them, and one
case reddens when a field is dropped.

**R818. (BLOCKS -- CZ0 head a) `K_sensitivity` and `Cm_sensitivity` are declared, reach two
PUBLISHED COLUMNS, and reach no artifact. A VACUOUS sensitivity publishes as a sensitivity
and the header does not move.**

```
claim  a run whose declared sensitivities are vacuous is indistinguishable, in the artifact,
       from the shipped one
cmd    two full runs of `floatfea run` into the scratchpad, from configs differing in two
       lines -- A: K_sensitivity 1.0, Cm_sensitivity 1.0 (the shipped example);
       B: K_sensitivity 2.0 (= K), Cm_sensitivity 0.1
out    A  utilisation_K_sens == utilisation on 30 of 32 rows ; Cm_sens on 22 of 32
       B  utilisation_K_sens == utilisation on 32 of 32 rows ; Cm_sens on 32 of 32
       governing row A: U 1.71167  K_sens 1.71167  Cm_sens 1.71365
       governing row B: U 1.71167  K_sens 1.71167  Cm_sens 1.71167
       header diff A vs B: ONE line, "# config: configA.yaml" / "# config: configB.yaml"
       worst |A-B| over the 32 rows: K_sens 3.42e-02, Cm_sens 9.24e-03
rule   the republished R743 caveat -- "The value used is in the provenance above, and the run
       reports a one-variable sensitivity BESIDE it"
judge  B's two columns are copies of the base column, published under a sensitivity label,
       with nothing in the file saying what variable moved or how far. `provenance()` builds
       `code_check` from `k`, `cm` and `one_third_increase` only
       (`floatfea/run/config.py:405`), and the two sensitivities are declared fields of that
       same block (`floatfea/run/config.py:286`, `examples/platform12_placeholder.yaml:96`).
```

```
claim  the gate that should have caught it cannot contain the fields
cmd    read the key list in test_provenance_records_every_declared_thing
out    config, deck, hsp_tag, froude_lambda, mass_distribution, sections, material,
       load_cases, governing_periods_s, code_check
rule   CZ0(c), and the recorded guard "assertion domain blindness"
judge  the assertion inspects a ten-key list and `K_sensitivity` is not a key -- it is inside
       the formatted `code_check` string. The collection the test inspects cannot contain the
       failure. This is R812's shape, "declared and consumed by nothing a reader can see", at
       two more coordinates, one round after R812 was ruled answered.
```

**And this is the half of R743 the rewording dropped**, which is the report's own question 3.
The original says `C_m = 0.85` "is the LESS onerous of the two" reported; the replacement
delegates the DIRECTION to a column whose operating point the artifact does not publish, and
run B shows the direction can be reversed -- `Cm_sensitivity = 0.1` is less onerous than the
declared value -- with no visible change anywhere in the file. **Closed when** both
sensitivity values are in the provenance of all three artifacts, or the column is omitted
where it equals the base, and one case reddens when a declared sensitivity does not reach the
header.

**R819. (BLOCKS -- CZ0 head a) The new R741 / R742 caveat makes two statements about the
bending allowable that the code refutes, and it is in all three artifacts.**

```
claim  (i) 0.75*Fy is the COMPACT-branch allowable, not "the first reduction below the
       compact branch"
cmd    allowable_bending / section_class at the shipped section, D = 2.5 m, t = 0.18 m,
       Fy = 355 MPa
out    D/t=13.9   branch=compact    F_b=266.25 MPa   (0.75*Fy = 266.25 MPa)
       D/t=40     branch=reduced_1  F_b=256.43 MPa
rule   `floatfea/checks/api_wsd.py:370` -- "compact  D/t <= 10340/F_y :  F_b = 0.75 F_y" --
       with `:375` `cap = 0.75 * fy` and `:377` compact -> `f_b = cap`
judge  the shipped section IS compact and its `F_b` IS `0.75*Fy`, so the published sentence
       calls the compact allowable a reduction below itself. The original was true and
       carried its measurement: "F_b is capped at 0.75 Fy -- the first reduced branch
       exceeded it to D/t = 30.60" (`docs/F6_utilisation.csv:5`). The rewording replaced a
       measured fact with a false one -- and in both CSVs the comma-to-semicolon escaping
       turns an ambiguous appositive into a flat assertion.
```

```
claim  (ii) "D/t > 300 is refused rather than extrapolated" is false at the shipped Fy
cmd    the same call at D/t = 300, 400, 845, 846
out    D/t=300  branch=reduced_2  F_b=151.18 MPa   -- COMPUTED, not refused
       D/t=400  branch=reduced_2  F_b=116.37 MPa   -- COMPUTED, not refused
       D/t=845  REFUSED (F_b = -3.8518e+07 Pa, not positive)
       D/t=846  REFUSED (exceeds 845.1 = 300000/F_y)
rule   `floatfea/checks/api_wsd.py:73` `BENDING_THIRD_BRANCH_NUMERATOR = 300000.0`, `:246`
       `limit_3 = BENDING_THIRD_BRANCH_NUMERATOR / fy_mpa`, and `:77`'s own sentence -- "At
       F_y = 355 MPa the limit is 845.1"
judge  the threshold is `300000/F_y[MPa]`, which equals 300 only at `F_y = 1000 MPa`. The
       declared domain admits `D/t` up to 50000 (`floatfea/run/config.py:96` and `:97`), so
       the band from 300 to 845 is reachable and the artifact misdescribes what the tool does
       there. This half is INHERITED verbatim from `docs/F6_utilisation.csv:5`, and
       `floatfea/checks/api_wsd.py:228` carries it too (CW0). What is new is that a GENERATOR
       now ships it with every run, at any `Fy`.
```

**Closed when** both statements are true of the code at any `Fy` -- or the sentence is
replaced by the branch table the code implements -- and the same correction reaches
`floatfea/checks/api_wsd.py:228`. Regenerated at the answering commit (CP3).

**R820. (BLOCKS -- CZ0 heads b and c) R814's repair is held in place by nothing. The same
100.0 kg/m^3 floor, reintroduced through a local variable, leaves 186 of 186 green --
including the test named `test_FO0_NO_THRESHOLD_REMAINS_on_a_computed_quantity`.**

```
claim  the exact threshold verdict 2 blocked on can come back with the suite green
cmd    git archive HEAD into the scratchpad; in the copy, replace the guard's two lines with
         rho = {b.name: float(b.equivalent_density) for b in built.bodies}
         massless = [n for n, v in rho.items() if v == 0.0 or v < 100.0]
       then python -m pytest -q tests/unit tests/regression/test_r1_published_artifacts.py
out    22 passed   (tests/unit/test_run_pipeline_refusals.py alone)
       186 passed  (the whole unit tree plus the published-artifact file)
rule   `tests/unit/test_run_pipeline_refusals.py:348` -- "no `DENSITY`, no ordering against an
       equivalent density, `== 0.0` present, the module does not import the bound"
judge  all four needles hold under the mutation. `DENSITY` is absent, `== 0.0` is present,
       `equivalent_density) <` never appears because the value is bound to a name first, and
       `hasattr(pipeline, "DENSITY")` is still False. The test's NAME is a claim about
       behaviour and its assertions are about four strings.
```

```
claim  the value case cannot catch it either, and the reason is the finding's own number
cmd    the guard's verdict at five fractions, in the clean tree and in the mutated copy
out    f=1e-09   rho_eq platform=9.52795e-06   clean ACCEPTED   mutated REFUSED
       f=1e-04   rho_eq platform=0.952795      clean ACCEPTED   mutated REFUSED
       f=0.0053  rho_eq platform=50.4982       clean ACCEPTED   mutated REFUSED
       f=0.0106  rho_eq platform=100.996       clean ACCEPTED   mutated ACCEPTED
       f=0.75    rho_eq platform=7145.97       clean ACCEPTED   mutated ACCEPTED
rule   verdict 2's condition -- "the boundary is pinned by a test at BOTH edges, the largest
       accepted and the smallest refused"
judge  `f = 0.0106` is the one positive fraction the suite tests, and it is the fraction the
       OLD FLOOR ALSO ACCEPTED: `100.996 > 100` is why it was a finding rather than a
       refusal. So the new case reddens only for a floor above about 101, and the refused
       edge `f = 0.0` is the only edge pinned. Four of the five rungs change behaviour under
       the mutation and no test moves.
```

**Ruling on the instrument, which the report asked for (its question 2): source-reading is a
legitimate instrument and is not the defect. The needles are.** `equivalent_density) <` is a
textual form rather than a behaviour, and one local binding walks past all four of them --
the same shape as the 302-decade patch, one level up. The behavioural pin needs no sweep and
no new apparatus: one case asserting that a body with an arbitrarily small POSITIVE
equivalent density is ACCEPTED (`f = 1e-09` gives `rho_eq = 9.5e-06` and is accepted today)
reddens under ANY positive floor, and its zero is the quantity's own, so it introduces no
threshold of its own. Keep the source-reading test beside it -- it catches the obvious return
-- but it is not the pin. **Closed when** the acceptance edge is pinned behaviourally far
below any plausible floor, so that the mutation above reddens.

**R821. (BLOCKS -- CZ0 head c) `study_only: true` permitting an otherwise-refused
configuration is now asserted by no test, because the test that asserted it was deleted in
this commit.**

```
claim  the escape hatch is unasserted
cmd    in the scratchpad copy, make the refusal unconditional --
         floatfea/run/pipeline.py:307  `if not cfg.study_only:`  ->  `if True:`
       then python -m pytest -q tests/unit tests/regression/test_r1_published_artifacts.py
out    186 passed
cmd    git diff d511a0c..HEAD -- tests/unit/test_run_pipeline_refusals.py | grep "^-def"
out    -def test_FN1_the_SHIPPED_fraction_is_admissible
       -def test_FN1_study_only_PERMITS_it_and_the_label_says_so
rule   the refusal's own promise at `floatfea/run/pipeline.py:316` -- "Set `study_only: true`
       to run it anyway -- every output will then carry `STUDY -- NOT FOR DESIGN`"
judge  the promise is in a message the suite asserts (`"study_only: true" in message`) and
       the behaviour it promises is asserted nowhere. The direction of harm is a refusal
       rather than a wrong number, which is why this is the lesser of the two deletions. The
       other one, `test_FN1_the_SHIPPED_fraction_is_admissible`, IS covered -- by
       `test_FO0_a_SMALL_fraction_is_a_LEGITIMATE_INPUT` and by the golden -- and needs
       nothing. The study LABEL is adequately covered too:
       `test_R806_a_STUDY_run_says_so_in_EVERY_header_line_block` for the generator and
       `test_a_NON_STUDY_run_carries_no_STUDY_label_anywhere` as the control.
```

**Closed when** one case asserts that an inadmissible configuration with `study_only: true`
runs, and that the label reaches what it writes.

## The five things the report asked to have attacked -- my rulings

**1. THE REWRITTEN DATA FILE IS SAFE, I DID NOT TAKE THE PASTE, AND THE INSTRUMENT YOU USED
IS THE WRONG ONE FOR THE CLAIM.** I asked the stronger question -- the committed npz against
the one in `d511a0c`, array by array, byte by byte -- which needs no HSP worktree:

```
claim  every pre-existing array is bit-identical and the only change is the added key
cmd    git show d511a0c:data/f4/dynamic_inputs.npz > <scratch>/old.npz ; then per key compare
       dtype, shape and `a.tobytes() == b.tobytes()`
out    old arrays: 99   new arrays: 100
       only in old: []   only in new: ['froude_lambda']
       shared keys: 99   BIT-IDENTICAL on shared keys: True
       new key: froude_lambda  float64  ()  50.0
       arrays containing NaN (old): 0
rule   FO1's "the golden must still pass byte-identically", and EX0(c)
judge  **nothing downstream moved.** Why the instrument still matters:
       `scripts/export_f4_dynamic_inputs.py:461-470` computes `max|a-b| / max|a|` and keeps
       it only `if gap > worst`, so a NaN pair gives `nan > 0.0 == False` and the line prints
       `0.000000e+00`; and `--check` RETURNS 0 whatever the number is, so it is a report and
       not a gate. Here it was adequate -- zero arrays carry a NaN, measured above -- and a
       byte comparison is the instrument this particular claim wants. C20.
```

**2. The structural proof: ruled above, and it is R820.** Reading source rather than sweeping
values is the right choice; the four needles are not the property, and I broke the property
with the suite green. The alternative is not a property test over `f` -- it is one acceptance
case at a positive density far below any floor.

**3. THE REWORDING DID DROP SOMETHING, THREE TIMES, AND YOU ASKED THE RIGHT QUESTION.** R817
(the heading and the wave height stopped being stated at all), R818 (R743's direction was
delegated to a column whose operating point is unpublished) and R819 (R742's measured fact
became a false one). Two of the five rewordings are clean: `FA1` and `EZ2` generalise
correctly and lose nothing load-bearing. One more thing to watch rather than a finding --
`FA0`'s "the response rises as the period falls across the band" and `EX3`'s "the governing
component on the transverse arms is entirely dynamic" are MEASUREMENTS of the placeholder,
now generated unconditionally for every configuration. They are true here and they are not
properties of an unknown platform. C21.

**4. The study label's reach: unchanged from C16, and I rule with you again.** The non-study
control in the new file is the right half to have added -- a generator that stamped
everything could not pass it. The gap is a different one and it is R821.

**5. YOUR LIVE QUESTION, ANSWERED: it does not need a new diagnostic, because the diagnostic
is already there and already published -- and that is measured, not argued.**

```
claim  what a 1%-mass configuration actually tells its reader today
cmd    build_model at f = 0.0106 on every body; print the build's own findings and the mass
out    FINDING: platform: the mass fraction is 0.0106, handed in by the caller rather than
         taken from (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never
         consulted for it. This body is a MEASUREMENT, not one to ship.
       (the same line for hub1..hub4)
       platform   member_mass=26500.0 kg   rho_eq=100.9963
       hub1..hub4 member_mass=15900.0 kg   rho_eq=161.5941
rule   R807's repair -- the build's own findings reach both CSV headers and the report
judge  the artifact already says the fraction was handed in rather than reached, that the
       body is a MEASUREMENT and not one to ship, and the mass table already carries
       `26500` against `2.5e+06`. **Do not add a rule that judges the fraction.** A
       threshold is what R814 was; a reported finding is what FO0 asked for. If anything is
       added it is the equivalent density against the declared nominal in BOTH directions --
       DZ5 already fires for "above steel" and could as cheaply say "two orders below the
       declared nominal" -- and that is a sentence, not a refusal.
```

## The adversarial cases I ran, and what they found

* **Two full runs of the tool at a configuration the diff did not choose** (`K_sensitivity`
  equal to `K`; `Cm_sensitivity = 0.1`): the sensitivity columns collapse onto the base on 32
  of 32 rows and the header does not move. **R818.**
* **A regeneration of all three published artifacts from the committed configuration**, into
  the scratchpad: `governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2
  interaction)`, `1248` member-force rows, `32` checked stations, and the committed files
  reproduce LINE FOR LINE apart from the three declared paths (my config lives elsewhere) and
  the wall-time table -- 6 differing lines in each CSV, 12 in the report, every one accounted
  for. **The published artifacts are not stale.**
* **Both halves of the caveat gate, broken on purpose**: removing `FA0` from the artifact
  gives `FAILED tests/regression/test_r1_published_artifacts.py::test_every_caveat_reaches_EVERY_published_artifact[report.md-FA0]`,
  and removing it from `TABLE_CAVEATS` gives `FAILED tests/unit/test_run_pipeline_refusals.py::test_R806_R807_the_header_carries_the_BUILDERS_OWN_assumptions_and_findings`.
  Both carry their own failure. **R815 and R816 are properly closed.**
* **Two mutations of the repaired guard** -- the floor through a local binding, and the
  `study_only` escape made unconditional: `186 passed` each. **R820 and R821.**
* **A continuum grid over `f`** at `1e-09, 1e-04, 0.0053, 0.0106, 0.75` in two trees, which
  is what separated "the floor is gone" from "the floor's absence is pinned".
* **The clause functions at eight `D/t` values**, either side of both published thresholds.
  **R819.**

## CI at the reviewed commit: UNAVAILABLE -- and it is a THIRD unavailable state

```
cmd    gh run list --commit 62a8281 --json name,conclusion,workflowName
out    []
cmd    git ls-remote --heads origin | grep F3 ; git rev-parse HEAD
out    bd315a17...  refs/heads/F3
       62a8281c...  (local, fourteen commits unpushed)
cmd    gh run list --limit 5 --json headSha,conclusion,workflowName
out    five completed runs with real conclusions; the newest is bd315a1, CI, success
```

**Not CK2's exhausted-allowance state**: runs do execute on this account, there are no
`runner_name: ""` jobs, no two-second durations and no spending annotation. There is simply
no run, because nothing was pushed. **The last run that executed is `bd315a1` and it does
not describe this tree** -- `git diff bd315a1..HEAD --stat -- tests/verification scripts
.github` is seven files, `206 insertions, 470 deletions`. So the step is judged on everything
else, and my own gates are green: `ruff check floatfea tests scripts` -> `All checks
passed!`; `black --check floatfea tests scripts` -> `147 files would be left unchanged.`;
`mypy floatfea` -> `Success: no issues found in 42 source files`.

**And `.github/workflows/ci.yml:277` still makes CI canonical for `tests/regression`, which
is where `test_r1_example_golden.py` and the new `test_r1_published_artifacts.py` live.
FL1(c) calls that golden "a golden regression test in CI" and it has never run in CI.** Three
rounds. That is an unavailable check and not a red, so it does not block -- and it is the
first named condition for step 2.

## The boundary red, traced by name (EG3(i))

13 failed, and my own run reproduces the report's counts exactly. Six in
`tests/test_report_carried.py`, each read individually:

```
test_the_report_carries_a_CI_SECTION            "no CI section in the newest revision"
test_the_CI_section_is_about_the_REVIEWED_commit
test_the_reported_CI_counts_are_not_all_zero    "every CI row reports zero and zero"
test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph
test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
test_the_report_carries_a_WHOLE_SUITE_count
```

and seven in `tests/test_report_guard_states.py` -- `[baseline]` plus six planted states,
each failing with the inner run's own `6 failed, 230 passed` embedded in its assertion, which
is EH1's identification rule: the baseline is red and each cascading state's own failure line
says so.

**I traced the cause rather than the family, and it is one line of output:**

```
cmd    python scripts/ci_section.py ; echo exit=$?
out    no CI run at 582cde72..., and the commit touches paths the workflow does NOT ignore --
       so it is a commit that was never pushed, not one the workflow declined. A report
       cannot publish a table for it.
       exit=1
cmd    grep -n "_UNAVAILABLE = " tests/test_report_carried.py
out    1249: _UNAVAILABLE = re.compile(r"unavailable,\s*(allowance exhausted|no jobs created)")
```

So the generator KNOWS the state and refuses with exit 1, the report therefore has no CI
section at all, and the guards' only escape hatch recognises two unavailable strings that do
not include this one. **Two of the six are FC1's named pair** -- `test_the_report_carries_a_WHOLE_SUITE_count`
and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` -- which cannot pass in the commit they
describe. **The other four are a function of `gh run list` returning `[]` at a commit nobody
could push.**

**I am not ruling any of the 13 CZ1 (iv) against the implementer, and I am not ruling them a
blocking (d).** Nothing outside those two files is red -- 3554 passed, including every
element, solver, load-path, code-check, configuration, deliverable and ladder test -- and no
action available to the implementer clears these six: the cause is a permission policy
outside the repository and a guard they are instructed to fix rather than extend. Recording
them as blocking would make the step unclosable from this environment, which is the DD1 trap
with no exit.

**The repair is FF0 class and is due in the next commit rather than the ledger:**
`scripts/ci_section.py` already prints the right sentence and throws it away with exit 1. It
should emit the SECTION with that sentence as the body -- a third unavailable state,
`unavailable -- never pushed` -- and `_UNAVAILABLE` should recognise it. A guard that fails
false in a state nobody declared is fixed, not extended (EK2). C22.

## Corpus (EG4(e))

**The pause held. Zero new entries this round**, so there is no coverage count to report; R1
step 1 touches neither exception -- not F4's load-mapping gate and not EB6's
label-provenance gate. I ran the recorded substitute instead, both halves, and both produced
blocking findings:

* **a continuum grid over the parameter space the decision rules guard** -- `f` at five
  points in two trees, the two declared sensitivities at a configuration the diff did not
  choose, and the clause functions at eight `D/t` values spanning both published thresholds.
  This produced **R818**, **R819** and **R820**.
* **a regeneration check on a published deliverable** -- the three artifacts re-run from the
  committed configuration and diffed line for line (clean), the npz compared byte for byte
  against its predecessor (clean), and the artifacts' caveat block compared against the
  committed deliverables they replace marker by marker AND SENTENCE BY SENTENCE. This
  produced **R817** and **R819**.

## Tolerances touched

**`floatfea/tolerances.py` is untouched -- `git diff d511a0c..HEAD -- floatfea/tolerances.py`
is empty -- and ONE tolerance-under-another-name was REMOVED.**

```
old      rho_eq < 100.0 kg/m^3 refuses, read from config.py's declared NOMINAL bound
new      none. `== 0.0` on the computed equivalent density, plus `admissible()`, whose own
         tolerance is declared in floatfea/tolerances.py
form     was ABSOLUTE and dimensional (kg/m^3); there is now no comparison to have a form
counter  DECLARED structurally -- no `DENSITY`, no ordering, `== 0.0` present -- and MEASURED
         DEFEATED: R820. The smallest defect the suite's value cases detect is still
         "rho_eq is exactly 0.0", exactly as in verdict 2, and the floor they do not detect
         is the same 100.0 the repair was asked to remove.
justif.  `floatfea/run/pipeline.py:252-289`, and it is a good entry: it names what was
         removed, why the removal rather than a smaller number, and what replaced it.
```

My own grep over the diff for `isclose`, `abs_tol`, `rel_tol`, `approx`, `atol`, `rtol` and
`2**-n` finds no new comparison -- only prose using the word "tolerance". The one new magic
number is `assert len(head) >= 20` at `tests/regression/test_r1_published_artifacts.py:78`;
the CSV headers carry 38 comment lines, so the assertion has 18 lines of slack and would pass
with half the block gone. Each required caveat is separately asserted, so it is not
load-bearing: C23.

## Closure items

Fixed once, in the step's closure commit, and not re-reviewed item by item. **C22 is FF0
class and belongs in the next commit rather than the ledger.** Verdict 1 and 2's C12 to C18
remain open and carry forward unchanged.

* **C19** (was C11, and it was due in the previous commit). `floatfea/run/pipeline.py:9-28`
  still reads "Four declared things reach the model today" and is now short by three:
  `froude_lambda` reaches `build_superstructure` and `compute_rows` and is now read from the
  npz as well, `window_rule` reaches `provenance()`, and the two sensitivities reach
  `check_member`. CW0 applies to it -- a reader uses that list as a contract.
* **C20.** `scripts/export_f4_dynamic_inputs.py:461-470` -- `--check`'s comparison is
  NaN-blind (`nan > worst` is False, so a NaN pair prints `0.000000e+00`) and the command
  returns 0 whatever the difference is, so it is a report and not a gate. Zero arrays carry a
  NaN today, so it was adequate for FO1; a byte comparison is the instrument.
* **C21.** `floatfea/cli.py`'s new `FA0` and `EX3 / R724` caveats state placeholder
  MEASUREMENTS unconditionally -- "the response rises as the period falls across the band",
  "the governing component on the transverse arms is entirely dynamic". True of this
  configuration, not properties of an unknown platform, and now generated for every run.
* **C22 (FF0 class, next commit).** `scripts/ci_section.py` refuses with exit 1 where it
  should emit `unavailable -- never pushed` as the section body, and
  `tests/test_report_carried.py:1249`'s `_UNAVAILABLE` does not recognise that state. Four
  guards report a push policy as a red tree.
* **C23.** `tests/regression/test_r1_published_artifacts.py:78` -- `len(head) >= 20` against
  38 actual lines; and `:133` pins the string `11433`, which is one placeholder digit string
  standing in for "the equivalent densities are reported".
* **C24.** `results/R1/example/report.md` and both CSVs record `hsp_tag: (pinned HSP state;
  see docs/hsp-coupling.md and floatfea/hsp_pin.py)` -- a pointer where the npz's own sidecar
  records the resolved tag. Faithful to the configuration, which declares that string
  (`examples/platform12_placeholder.yaml:19`), so it is the example's field rather than the
  code's.
* **C25.** **DIRECTIVE FO's text is in no file in this repository.** `FO0`, `FO1` and `FO2`
  are cited as the governing rule in `floatfea/run/pipeline.py`,
  `scripts/export_f4_dynamic_inputs.py`, `tests/regression/test_r1_example_golden.py`,
  `tests/regression/test_r1_published_artifacts.py` and
  `tests/unit/test_run_pipeline_refusals.py`, and `grep -c "FO0\|FO1\|FO2\|FO3"
  docs/milestones/R1.md` is `0`. FM0 got a plan section (R1.md section 2c-i) and FN2 and FN3
  got standalone `process:` commits; FO got neither, so five shipped gates name a rule a
  later reader cannot read. **A closure item under CZ0 -- a plan is prose -- but it is the
  one closure item that blocks the REPAIR of a blocking finding**, because R820's condition
  is "what FO0 actually requires" and that sentence currently exists only in a transcript.

## Next step opens when

**Step 2 opens immediately.** The step is closed by ES0's cap, this verdict carries
`Closes: R1/step-1`, and the five findings carry by name into step 2's `Carried` section
where they STAY BLOCKING (`CLAUDE.md` section "Step gating"). Under FO3 they go into step 2's
FIRST commit, before any FL2 work, with no slip to the 28 October target -- 14 days, two
steps, and each of these five is smaller than any of the three that came before them.

Step 2's first commit answers these, and they are the conditions rather than "the above":

1. **R817** -- the heading and the wave height reach the provenance of all three artifacts,
   with the band's bounds wherever a caveat refers to them, and a case reddens when one is
   dropped.
2. **R818** -- the two declared sensitivities reach the provenance of all three artifacts,
   and a case reddens when a declared sensitivity does not reach the header.
3. **R819** -- both statements in the R741 / R742 caveat are true of the code at any `Fy`, or
   are replaced by the branch table the code implements, and
   `floatfea/checks/api_wsd.py:228` is corrected with them.
4. **R820** -- the ACCEPTANCE edge is pinned behaviourally at a positive equivalent density
   far below any plausible floor, so that the local-variable reintroduction reddens.
5. **R821** -- one case asserts that `study_only: true` permits an inadmissible configuration
   and that the label reaches what it writes.
6. **C22, in the next commit and not the ledger** (FF0): `scripts/ci_section.py` emits the
   `unavailable -- never pushed` section and the guard recognises it, so four guards stop
   reporting a push policy as a red tree.
7. **The push.** Fourteen commits, two verdicts and FL1(c)'s golden have never reached CI,
   and `.github/workflows/ci.yml:277` makes CI canonical for `tests/regression`. Not an
   action I can take and not one the implementer was permitted. It is Xabier's decision and
   it is now the oldest open item in this milestone. **If it is still refused when step 2 is
   reported, say so again under its own heading** -- an unavailable check recorded three
   rounds running is a fact about the project, not about a round.
8. **C25**, because R820's own condition cites a directive no file carries. One plan
   paragraph, as FM0 got.

**What this revision got right, and it is the larger part.** FO1's re-export was the
dangerous one -- a committed 12 MiB data file that every figure in four increments reads from
-- and it was done with the control FIRST, which is the right order, and it is bit-identical
by my own independent measurement. The floor is GONE rather than moved, which is the harder
of the two available repairs and the correct one. All eleven markers travel to all three
artifacts and both halves of that gate redden when broken. The published artifacts regenerate
line for line from the committed configuration. And the withdrawal in section 4 -- "I
asserted a blocker without running the one command that tests it" -- is the sentence a later
reader will find most useful in this file.

**The pattern across the three rounds is unchanged, and naming it once more is now the
useful thing rather than the fix.** Verdict 2 said the verifiable half gets verified and the
deciding half gets described. This round it moved one step along: the deciding half is no
longer the repair, it is **what holds the repair**. A floor removed with nothing pinning the
absence. Five caveats delivered, two of them now saying something the code refutes. Two
sensitivity columns published with their operating point nowhere. Each repair was real; what
none of them carried was the measurement that would fail if the repair were undone -- and
that, exactly, is what step 2's first commit is for.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 1
Reviewed commit: 582cde72c72d85b9f3cb9d0019e297eb5e04f4b1
**Reviewed commit: `582cde72c72d85b9f3cb9d0019e297eb5e04f4b1`.**
Verdict: HOLD
Tests: 3519 passed, 15 failed, 1 skipped   (my own run, `python -m pytest -q`, 711.75s)

Written with `scripts/write_verdict.py --milestone R1 --step 1`, which now works: R804 is
answered and this entry carries the bold anchor the tool emits, so `ci_section.py` has a
commit to walk from the next revision on.

## Carried

**Verdict 1's ten items, each with its status and where.** Eight were (a)-class, two FF0.

| item | status | where |
|---|---|---|
| R804 | **answered** | `f13f519` + `e6076cc`. `_plan_labels()` reads `docs/milestones/`; `--milestone R1` resolves and `--milestone 1` refuses. Verified: `MILESTONE = R1`, `VERDICT_IN_REPO = docs/reviews/R1/step-1.md`. The anchor is emitted. |
| R805 | **answered** | `floatfea/post/forces_table.py:87,:430` -- the scale is a required parameter with no default, the module constant is gone, `run` refuses a mismatch naming both. Byte-identity re-verified by me, below. |
| R806 | **PARTLY -- still open as R815** | four of the nine named caveats travel; five do not. |
| R807 | **answered** | `floatfea/cli.py` `_header_lines` -- all six `assumptions` and all nine body `findings` reach both CSV headers and the report, generated from the build. Measured in the published artifacts. |
| R808 | **PARTLY -- still open as R816** | the line reads `platform:hub4_arm`; nothing asserts the published string. |
| R809 | **answered** | `floatfea/cli.py:263-278` -- the check is the first thing after `load_config`. My run: exit 2, output directory absent, nothing written. |
| R810 | **PARTLY -- still open as R814** | the two sampled ends refuse; the range named in the condition is not gated and the boundary was sampled, not solved. |
| R811 | **answered** | `floatfea/run/config.py` `_NoDuplicateLoader`. Five shapes I wrote, none of them the implementer's, all refused, below. One closure item on the message. |
| R812 | **answered on substance; C11 open** | `window_rule` is in `provenance()` and reaches every header. `pipeline.py:9-28`'s enumeration is still "Four declared things" and is now short by two. |
| R813 | **answered** | `585f707`, standalone `process:` citing FN2, `CLAUDE.md` plus `docs/SUPERVISOR.md`, additive only, byte-identical block in both. Not a STOP. |

**Verdict 1's closure items.** C9 done in `585f707`. C10 done -- the utilisation CSV's
trailing columns are now `utilisation, governing_clause, utilisation_K_sens,
utilisation_Cm_sens` with no repeat. C2 was ruled FF0 class and due in the next commit; it
is not done and is re-listed as C11. C1, C3, C4, C5, C6, C7 and C8 remain open and are not
re-reviewed.

## Findings

Three. Each is a carried item whose named condition is half-met, and in each case the half
that is missing is the half that decides something. None is a new subject.

**R814. (BLOCKS -- CZ0 heads b and c) The admissibility floor is a threshold on a computed
result, borrowed from a bound written for a declared input, and it admits a frame whose
members carry 1% of the body mass -- which then publishes `U = 2.15615` with no label.**

`floatfea/run/pipeline.py:287` reads `floor = DENSITY[1]`, i.e. `config.py:100`'s
`("kg/m^3", 100.0, 25000.0)`, and compares `body.equivalent_density` against it. Verdict
1's own ruling on claim 4 held that a `Bound` is not a tolerance BECAUSE "no result is
compared against it", and named R810 as the limit of that ruling. The repair compared a
result against it.

```
claim  the boundary, solved in BOTH directions rather than sampled (EH4)
cmd    bisect f to 12 digits over the real build-plus-guard path, both edges
out    UPPER  largest f PSD on EVERY body = 0.951684564548 (platform fails first)
       LOWER  smallest f the GUARD ACCEPTS = 0.010495432737
              at that edge: platform rho_eq = 100.0000, member_mass = 26238.58 kg
              of a 2.5e+06 kg body; hubs rho_eq = 160.0000
              rho_eq is 1/78.5 of steel and every body is PSD
rule   the guard's own sentence, "members this light carry no mass, so their forces mean
       nothing", and verdict 1's condition "solve the boundary both ways"
judge  the review asked for a range and got four samples. 0.0 and near-1.0 refuse; the
       decade from 0.0105 to 0.75 is ungated.
```

```
claim  what the tool does just inside that edge
cmd    python -m floatfea.cli run <example with f: 0.0106 on every body>
out    exit 0 ; member_forces.csv 190984 B, utilisation.csv 12252 B, report.md 7415 B
       governing U = 2.15615 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
       STUDY label present: False
       mass row: | `platform` | 0.0106 | 2.500000e+06 | 2.650000e+04 | ... | 101.0 | OK |
rule   FN1: "run REFUSES any body whose equivalent density is below the declared floor"
judge  26% above the shipped governing utilisation, published, unlabelled, with `OK` in
       the PSD column and `101.0` in the density column. This is R810's own shape at a
       fraction R810 did not sample.
```

```
claim  nothing holds the threshold's VALUE in place -- the weakening direction (EH4)
cmd    patch pipeline.DENSITY's lower bound and re-evaluate FN1's three counter-cases
       and its control at each value
out    floor=100     FN1 green: True    f=0.0106 ACCEPTED
       floor=1       FN1 green: True    f=0.005  ACCEPTED
       floor=1e-09   FN1 green: True    f=1e-09  ACCEPTED
       floor=1e-300  FN1 green: True
       floor=0       FN1 green: False
rule   tests/unit/test_run_pipeline_refusals.py::test_FN1_an_inadmissible_fraction_is_REFUSED
       at [1.0, 0.999999, 0.0], plus test_FN1_the_SHIPPED_fraction_is_admissible
judge  the floor may fall 302 DECADES with every counter-case and the control still
       green. The only thing pinned is a strict inequality at exactly zero, because the
       only case in the suite is f = 0.0, where rho_eq is exactly 0.0. The number 100 is
       undetectable, unasserted and underived.
```

And the refusal's sentence is false of one of the values it refuses:

```
claim  f = 0.0 is a rung of the ladder, and is admissible there
cmd    MASS_FRACTION_LADDER ; admissible() per body at f = 0.0
out    MASS_FRACTION_LADDER = (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0)
       f = 0.0 -> psd_false = []   (all five bodies admissible)
rule   the refusal reads "this mass distribution is one the shipped builder would never
       have reached ... admissible() at every rung"
judge  the ladder's last rung is 0.0 and admissible() holds there, so the builder
       descending the ladder COULD reach it. The guard refuses a rung and accepts
       0.0105, which is not a rung at all.
```

**Closed when** the condition is on a quantity with a non-arbitrary zero -- `member_mass
> 0`, or membership of the ladder -- so no threshold exists; OR, if a threshold is the
answer, its value is derived, lives in `floatfea/tolerances.py`, is relative to a stated
scale rather than absolute in kg/m^3, and arrives with the counter CLAUDE.md requires: the
smallest member-mass deficit the same assertion detects, in the same quantity. Either way
the boundary is pinned by a test at BOTH edges -- the largest accepted and the smallest
refused -- so that the 302 decades above cannot happen, and the refusal's own sentence is
true of every value it refuses.

**R815. (BLOCKS -- CZ0 heads a and c) R806's named minimum list is met for four of nine;
five caveats are absent from all three published artifacts, and the gate asserts only the
four that are present.**

```
claim  which of the nine named caveats reach the published deliverables
cmd    grep -c each marker in the three files under results/R1/example/
out    R739   present     R740   present     FA3    present     R730   present (in FA3)
       R724   0 0 0       EX3    0 0 0       heading 0 0 0
       R743   0 0 0       "LESS onerous" 0 0 0
       FA0    0 0 0       FA1    0 0 0       R741   0 0 0       R742   0 0 0
       ASSUMED 0 0 0      PRELIMINARY 0 0 0  FA2 0 0 0          "K = 1.0" 0 0 0
rule   verdict 1, "Next step opens when" item 2: "(R739, R740, EX3/R724, R743, FA0, FA1,
       FA3, R730, R741/R742 at minimum)"
judge  the published utilisation CSV carries U = 1.71167 and does not say that every case
       is heading 0 and the heading dependence is UNTESTED, that C_m = 0.85 is the LESS
       onerous of the two reported, that T = 12.5 s sits below the band's lower bound and
       was chosen to represent its edge, or that F_b is capped at 0.75 Fy and D/t > 300 is
       refused rather than extrapolated. All four are in the committed
       docs/F6_utilisation.csv header that this artifact replaces for a reader.
```

The report's stated reason for the split is sound and does not cover these. Section 4 says
the column caveats are the writer's business and the build's properties come from the
builder; the invocation adds that the placeholder masses and the assumed grade are
configuration properties sitting in the provenance block. I agree with the split -- a
generated header cannot go stale, which is the right property -- and none of the five above
is a configuration property. They are clause caveats, exactly like the four that are there.

```
claim  what the gate asserts
cmd    grep the marker tuple in tests/unit/test_run_pipeline_refusals.py
out    for marker in ("R739", "R740", "FA3", "EZ2"):
rule   CZ0(c): what a gate claims, on which quantity
judge  the gate is the condition's own list minus five, so the four that travel are
       pinned and the five that do not are pinned absent.
```

**Closed when** each of the five named is in the artifact that carries the numbers, or is
declared in the report as left with the reason; and the gate's marker list is the same list
as the condition, so a sixth cannot quietly go missing. Regenerated at the answering
commit (CP3).

**R816. (BLOCKS -- CZ0 head c) No test in this repository reads any artifact under
`results/R1/example/`, so the three published deliverables are asserted by nothing, and
R808's second half is not done.**

```
claim  nothing reads the published artifacts or the code that writes them
cmd    grep -rn for _write_report, _write_member_forces, _write_utilisations, _cmd_run,
       cli.main and results/R1 over tests/
out    (no output)
cmd    grep -rln "floatfea.cli" tests/
out    tests/unit/test_run_pipeline_refusals.py      -- imports _header_lines only
rule   verdict 1, R808: "Closed when the line names platform:hub4_arm AND the golden test
       asserts the published string, not only the dict fields"
judge  the new header test builds a stub RunResult and asserts the return value of
       _header_lines. It cannot see _write_header, _write_report, the governing line, the
       comma-to-semicolon escaping or the file on disk. R808 was a defect in _write_report
       whose repair had already been asserted once in a commit message without having been
       made -- section 5 of the report says so in its own words -- and the published
       string is still the thing nothing checks.
```

This is one assertion in an existing regression file, not new apparatus, and FL1(c) already
makes the example a golden. **Closed when** a test reads the committed artifacts, or a
fresh run's, and asserts the governing line verbatim, with the measurement that re-doubling
the body prefix reddens it.

## The five things the report asked to have attacked -- my rulings

**1. The one part of FN0 left open: THERE IS A FOURTH OPTION, AND IT IS THAT THE PREMISE IS
FALSE.** The dilemma rests on "that npz cannot be regenerated here -- it needs the pinned
HSP worktree". It is here.

```
claim  the pinned HSP worktree is present beside this repository, and the export runs
cmd    ls -d ../HSP-stable ../HSP-runs ; git -C each describe --tags ;
       python scripts/export_f4_dynamic_inputs.py --check
out    ../HSP-stable  floatfea-ref-1
       ../HSP-runs    floatfea-ref-1
       --check: imported g41_dynamic, applied the ER0 override
         ("platform mass/inertia OVERRIDDEN in memory (ER0): mass 10.0 -> 20.0 ...")
         and began solving "## T_full = 10 s  (model 1.4142 s)"
rule   scripts/export_f4_dynamic_inputs.py:146-148, which records the three checkouts and
       their tags: "../HSP-runs floatfea-ref-1 / ../HSP-stable floatfea-ref-1"
judge  the script's own docstring names the worktrees, both are at the pin, and the
       generator starts. Anyone who can run --check can run the export, because --check IS
       the export plus a comparison -- so the first horn, "reddening a gate on a file
       nobody here can re-export", is self-cancelling, and option (a) needs no waiting and
       no ruling.
```

If the re-export turns out not to complete, the fourth option is still not (b): it is
**make the sidecar the single record and delete the npz-key branch.** A preferred
read-path that no file this repository can produce will ever populate is a second source
exercised only by a synthetic test, which is the structure R805 was. One record, read one
way, and a file recording nothing refuses -- which is what FN0 is for.

**2. Byte-identity after the signature change: VERIFIED, independently, both files.**

```
claim  the deliverable regenerates byte-identically after FN0 changed _lam_full_scale and
       compute_rows
cmd    python scripts/measure/member_forces_table.py --out <tmp>.csv --summary <tmp>.md ;
       diff -q and sha256sum against docs/F4_member_forces.csv and .md
out    CSV IDENTICAL   MD IDENTICAL
       ed089b780e34db049059f671e1a09ed09d7ee679e48a4b4fcf97139e08258686  both .csv
       5492b591c57b420531f7e14247922d02bb4f76473a4d98600a5a83aa49c7bba0  both .md
rule   FL1(c)'s "EXACTLY"
judge  it did not move. The .md sha is new information -- the report pasted one sha for
       both files -- and it matches too. Every figure in both revisions stands.
```

**3. FN1's per-body guard: the SHAPE is right, and your re-measurement agrees with my
verdict rather than correcting it.** Measured here: f = 0.999999 gives
`platform=False hub1..hub4=False`, five of five, and f = 1.0 gives
`platform=True, hub1..hub4=False`, four of five. Verdict 1's text reads "f = 0.999999 all
four hubs and the platform PSD=False" and "f = 1.0 the four hubs PSD=False, the platform
PSD=True" -- the same two numbers. The report's section 7 attributes "four of five at
f = 0.999999" to the verdict; the verdict said all five. The measurement is not in dispute
and the citation is C15. Independently: the largest f admissible on every body is
0.951684564548, the platform is the first to fail, and f = 1.0 is admissible on the
platform again -- so non-monotone is confirmed, and **per body is the only correct shape.**
The guard's condition is not over-engineered; its threshold is R814.

**4. The study label's reach: a closure item, and I rule with you.** Measured on a real
run rather than on `_header_lines`:

```
cmd    run at f = 1.0 with study_only: true, then grep the written files
out    console: "STUDY -- NOT FOR DESIGN."   governing U = 1.58583
       member_forces.csv : STUDY in file True ; in non-comment lines False
       utilisation.csv   : STUDY in file True ; in non-comment lines False
       report.md         : STUDY in file True ; in non-comment lines True
```

FN1 asks that every output carry it and every output does. A reader who strips comment
lines from a CSV has stripped the provenance, the deck, the material and nine findings
along with it -- the label is no worse served than anything else in that block. C16, and it
is the right call to have declared it rather than waited.

**5. R806's header split: the split is right and the list is short.** One list would make
the builder's half copyable and therefore stale, which is the property section 4 correctly
protects. The five missing caveats are not configuration properties, so the split does not
explain them -- see R815.

## The adversarial cases I ran, and what the gates detect

Beyond R814's three cells: five duplicate-key shapes the implementer did not write, all
refused, including the two that a loader fixed at one depth would miss.

```
cmd    load_config on five duplications I constructed
out    REFUSED  a second top-level code_check block        -> names 'code_check', line 109
       REFUSED  a FLOW mapping, platform: {f: 0.75, f: 0.30} -> names 'f', line 32
       REFUSED  a QUOTED key beside a bare one, K then "K"   -> names 'K', line 90
       REFUSED  a duplicate inside sections.groups           -> names 'platform', line 48
       REFUSED  a duplicate governing_periods                -> names it, line 84
rule   floatfea/run/config.py _no_duplicates, registered on DEFAULT_MAPPING_TAG
judge  R811 is closed on substance and the registration covers every mapping depth and
       both YAML styles. The message names the key and the line and not the two values,
       which the condition asked for -- C14, because the key and the line locate it.
```

And the mismatch refusal, inverted (EH4): the smallest declared mismatch that refuses is
one ULP, which is correct -- an exact comparison with no epsilon is what CLAUDE.md requires
-- but the message it then prints is C13.

## CI at the reviewed commit: UNAVAILABLE (not red, not green)

```
cmd    gh run list --commit 582cde7 --json name,conclusion,workflowName
out    []
cmd    the same for 585f707, f13f519, e6076cc
out    []  []  []
cmd    git ls-remote --heads origin | grep F3 ; git rev-parse HEAD
out    bd315a17...  refs/heads/F3
       582cde72...  (local, unpushed)
```

Not CK2's exhausted-allowance state: there are no started-but-unrun jobs, no empty
`runner_name` and no spending annotation -- `gh run list --limit 5` returns five completed
runs with real conclusions. There is simply no run. The last run that executed is `bd315a1`
(workflow CI, `success`), and CK2's follow-up question again has a non-empty answer:

```
cmd    git diff bd315a1..HEAD --stat -- tests/verification scripts .github
out    scripts/check_carried.py 12 +- / scripts/ci_section.py 12 +- /
       scripts/measure/f6a_premise_check.py 4 +- /
       scripts/measure/member_forces_table.py 492 +------ /
       scripts/write_verdict.py 120 +--- /
       tests/verification/rung3/test_closure_evidence_exists.py 8 +-
```

So that green does not describe this tree, and the step is judged on everything else. My
own gates: `ruff check floatfea tests scripts` gives `All checks passed!`;
`black --check floatfea tests scripts` gives `146 files would be left unchanged.`;
`mypy floatfea` gives `Success: no issues found in 42 source files`.

**And this is the second consecutive round in which FL1(c)'s gate has not run.**
`.github/workflows/ci.yml:130` runs `pytest tests/regression` and `:277` records that CI is
canonical for `tests/regression` under Q8 -- which is exactly where
`test_r1_example_golden.py` lives. The golden that FL1(c) calls "a golden regression test in
CI" has never executed in CI. That is an unavailable check and not a red, so it does not
block; it is a named condition below, because a gate that has never run is not yet a gate.

## The boundary red, traced by name

15 failed, all in the two report-guard files. Eight in `tests/test_report_carried.py`, each
run with its own failure line read individually (EG3(i), R644's discipline):

```
test_a_blocking_item_is_not_routed_to_4a      "no blocking finding parsed from step-1.md.
                                               The heading format changed"
test_the_generator_would_catch_a_row_under_the_wrong_number
                                              StopIteration at :1141 -- gen.blocks() empty
test_the_CI_section_is_about_the_REVIEWED_commit
                                              "step-1.md does not name the commit it
                                               judged ... carries **Reviewed commit:**"
test_the_report_carries_a_CI_SECTION          "no CI section in the newest revision"
test_the_reported_CI_counts_are_not_all_zero  "every CI row reports zero and zero"
test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph
                                              "no 0a table in the newest revision"
test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
                                              "the 0a table has neither a run row nor the
                                               generator's zero-run row"
test_the_report_carries_a_WHOLE_SUITE_count   "carries no whole-suite line"
```

The other seven are `tests/test_report_guard_states.py` -- `[baseline]` plus six planted
states, each failing with the inner run's own `8 failed, 224 passed` embedded in its
assertion, which is EH1's identification rule: the baseline is red and each cascading
state's own failure line says so.

**Seven of the eight are MY defect, not the implementer's, and I measured the cause rather
than inferring it.** `python scripts/ci_section.py` prints "verdict 1 at `633b376` does not
name the commit it judged in its header", and `carried_table.classify()` returns `{}`
because verdict 1's headings carry no `(class)` parenthetical. Verdict 1 was hand-written --
that is R804 -- so neither convention is in it, and the CI section is UNGENERABLE rather
than absent. `MILESTONE` resolves to `R1` correctly, so the R1-awareness repairs are sound
and the format is the whole of it. The eighth,
`test_the_report_carries_a_WHOLE_SUITE_count`, is FC1: it cannot pass in the commit it
describes.

**This is neither EG3 state**, because the verdict and the answering report both exist, and
I am not ruling it CZ1 (iv) against the implementer: the cause is in a file they are
forbidden to edit and no action of theirs could clear it. It clears from their side when
revision 3 names THIS verdict in its `Answers:` header -- `ci_section.py` reads the verdict
out of git at the sha the report names, so it needs this commit to exist first. EG3(ii)
applies: run the two report-guard files at this verdict's commit and paste the counts in
revision 3.

Separately, `test_a_blocking_item_is_not_routed_to_4a` is a guard doing exactly what a
guard should: it refused to pass vacuously on a verdict whose format it could not parse,
and said so in one sentence. Nothing about it is to be changed.

## Corpus (EG4(e))

**The pause held. No batch, and no entry added -- zero new entries this round**, so there
is no coverage count to report. R1 step 1 touches neither exception: not F4's load-mapping
gate and not EB6's label-provenance gate. I ran the recorded substitute instead, both
halves, and both produced a blocking finding:

* **a continuum grid over the parameter space the decision rules guard** -- `f` over
  sixteen points plus a twelve-digit bisection at BOTH edges, the density floor swept over
  five values spanning 302 decades, `froude_lambda` at one ULP, 1e-10, 1e-3, 1, 25 and 49,
  and five duplicate-key shapes. This produced R814.
* **a regeneration check on a published deliverable** -- regenerating
  `docs/F4_member_forces.csv` and `.md` through the refactored script, both sha256
  identical, and comparing `results/R1/example/*` against the committed deliverables'
  caveat blocks marker by marker. This produced R815, and R816 followed from asking what
  asserts the artifacts it compared.

## Tolerances touched

**One, and it is R814.** `git diff 472bcd1..HEAD -- floatfea/tolerances.py` is empty and no
entry in that file moved. But `floatfea/run/pipeline.py:287` introduced a comparison of a
COMPUTED equivalent density against `DENSITY[1] = 100.0 kg/m^3`, which is a "small number
guard" under CLAUDE.md's own list and therefore a tolerance under another name:

```
old      none -- the quantity was not compared against anything
new      rho_eq < 100.0 kg/m^3 refuses, read from config.py:100's declared NOMINAL bound
form     ABSOLUTE and dimensional, kg/m^3. Not relative to any stated response scale.
counter  none declared. Measured: the value may fall 302 decades with every FN1
         counter-case and the control still green, so the smallest defect the assertion
         detects is "rho_eq is exactly 0.0" and nothing else.
justif.  located nowhere. The docstring justifies the CONDITION -- "f = 0 puts no mass on
         the members" -- and not the VALUE, and the condition it justifies is equally true
         at f = 0.0106, where the guard passes.
```

My own grep over the changed files for `isclose`, `abs_tol`, `rel_tol`, `approx`, `atol`,
`rtol` and `2**-n` finds nothing else. The three new `# not-a-tolerance:` annotations are
correct: two are Froude scales read from a record and compared exactly, the third is
`(50/25)**4`, an integer power of two exact in binary floating point. The one-ULP mismatch
refusal confirms no epsilon was introduced on the scale comparison, which is the right
call.

## Closure items

Fixed once, in the step's closure commit; not re-reviewed item by item. C11 is FF0 class
and belongs in the next commit rather than the ledger. Verdict 1's C1, C3, C4, C5, C6, C7
and C8 remain open and carry forward unchanged.

* **C11.** `floatfea/run/pipeline.py:9-28` -- still "Four declared things reach the model
  today", and now short by two in both directions: `froude_lambda` reaches
  `build_superstructure` at `:324` and `:332` and `compute_rows` at `:618`, and
  `window_rule` reaches `provenance()`. Neither is in the reaching list or the refused
  list, which is the structure R805 hid inside. Verdict 1 ruled this FF0 class and due in
  the next commit; it is prose a reader uses as a contract and CW0 applies to it.
* **C12.** The two deliverable-producing scripts each carry their own
  `FROUDE_LAMBDA = 50.0` -- `scripts/measure/member_forces_table.py:134` -- while the build
  beside it takes `build_superstructure()`'s default, `floatfea/model/platform.py:727`,
  `froude_lambda: float = 50.0`. Two sources in one function, currently equal, in a file
  EZ0 classes as producing a published deliverable. `forces_table`'s own new docstring says
  "a default would be the same constant wearing a different hat"; the function it feeds has
  one. I did NOT block: no declared input can make the two disagree, so no reader can reach
  it, which is what separates this from R805. One keyword at `member_forces_table.py:271`
  and `:318` and `f6a_premise_check.py:251`, `:255`, `:277`, `:310` closes it.
* **C13.** The scale-mismatch refusal prints its consequence through `{:g}`, so at a
  one-ULP mismatch it reads "The declared scale is larger by a factor of 1, which is 1x on
  every force and 1x on the locked moment." The refusal is right and its own stated
  consequence is "none".
* **C14.** `floatfea/run/config.py` `_no_duplicates` names the key and the line, not the
  two values. Verdict 1's condition named both values; the key and the line locate it, so
  the substance is closed.
* **C15.** `docs/reports/R1/step-1.md` section 7 attributes "four of five at f = 0.999999"
  to verdict 1. The verdict reads "all four hubs and the platform PSD=False" there -- five
  of five -- and four of five at f = 1.0. The measurement agrees; the citation does not.
* **C16.** The study label reaches every header block, the provenance and the console, and
  not the CSV column names or the filenames. Declared in section 12 rather than found,
  which is the right way round.
* **C17.** `scripts/write_verdict.py` `_plan_labels` globs `docs/milestones/*.md`, so
  `F2_figures` -- a figures file, not a locked plan -- is in the accepted set, and the
  refusal's own message calls the set "locked plan". `main()`'s report check stops it
  reaching a path. FF0 class, declared in section 2.
* **C18.** `scripts/carried_table.py`'s `MENTION = r"\bR\d+\b"` matches the milestone name
  `R1`, so every R-series report carries a spurious `R1` row. FF0 class, declared in
  section 14.

## Next step opens when

Step 2 does not open. ES0: this is the SECOND reviewed revision, so revision 3 is the last
one this step gets, and any item still blocking then carries by name into step 2's
`Carried` section and stays blocking there. The plan's FG1 wording, "one reviewed report
revision per step", was already overtaken by the HOLD; ES0's cap is what governs.

1. **R814** -- the floor is a derived quantity or it is not a threshold. If it stays a
   threshold it lives in `floatfea/tolerances.py`, relative to a stated scale, with its
   counter measured in the same quantity; either way the boundary is pinned at BOTH edges
   so it cannot fall 302 decades green, and the refusal's sentence is true of every value
   it refuses -- including f = 0.0, which is a rung.
2. **R815** -- EX3/R724, R743, FA0, FA1 and R741/R742 travel with the artifacts that carry
   the numbers, or each is declared left with its reason; and the gate's marker list is the
   condition's list.
3. **R816** -- one assertion reads the published governing line and reddens on a re-doubled
   prefix.
4. **C11**, as the FF0-class item: `pipeline.py`'s enumeration is complete in both
   directions.
5. **FN0's open half** -- re-export with the key, now that the premise is refuted, or take
   the sidecar as the single record and delete the unexercised branch. Either closes it
   without a ruling, and `--check`'s array-set gate is weakened by neither.
6. **EG3(ii)** -- the two report-guard files run at THIS verdict's commit, counts pasted in
   revision 3.
7. **Push the branch** so that a CI run exists at the reviewed commit, because `ci.yml:277`
   makes CI canonical for `tests/regression` and FL1(c)'s golden has not run there in two
   rounds. If pushing is not available from this environment, that is a fact to report in
   revision 3 under its own heading -- not a step to pass over.

The substance of this revision is good and the repairs are real: R805 was the serious one
and it is properly fixed, with no module constant, no default, a required parameter, a
refusal that names both scales and the 8x and 16x it would have cost, and byte-identity
re-proven on BOTH deliverable files after the signature moved. R807 turned nine discarded
findings into generated header lines that cannot go stale. R809's refusal now arrives
before its own side effects, measured empty. R811 refuses five shapes I invented, at two
depths and in both YAML styles. The three findings have one thing in common and it is worth
naming: **each is the half of a condition that decides something, left behind by the half
that is visible.** A guard whose condition is right and whose threshold is held in place by
nothing; a caveat list that travels for the four markers a test names and not the five it
does not; a published string fixed in the artifact and asserted by nothing -- one round
after that same string's repair had been claimed and not made. The pattern is not
carelessness. It is that the verifiable half gets verified and the deciding half gets
described, and under CZ0 the deciding half is the half that blocks.

The schedule is not at risk. Fifteen days, two steps, and these three are each smaller than
any of the ten that came before them.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 1
Reviewed commit: 472bcd1a22175eae6e8e43aeffdbf109be0eaab0
Verdict: HOLD
Tests: 3356 passed, 37 failed, 1 skipped   (my own run, `python -m pytest -q`, 703.78s)

**WRITTEN BY HAND, AND THAT IS FINDING R804.** `scripts/write_verdict.py` is the one
sanctioned path into this directory and it cannot express `R1`:

```
cmd  echo "Verdict: HOLD" | python scripts/write_verdict.py --milestone R1 --step 1
out  write_verdict.py: error: argument --milestone: milestone 'R1' is not a label of the
     form 2, 2a, 6, 6a, F6a -- the value becomes a path segment
```

Passing `--milestone 1` to satisfy the validator would have written this verdict into
`docs/reviews/F1/step-1.md` (`:148` hard-codes the `F`), i.e. into another milestone's
record. So this entry is written directly, in the format `write_verdict.py` produces, and
the deviation is recorded here rather than left silent. The `PreToolUse` hook clears
`gating-supervisor`; the file is at the correct path.

## Carried

**Checked, nothing carried.** R1 step 1 is this milestone's first step, `docs/reviews/R1/`
did not exist before this entry, and `git log` confirms no prior verdict in R1 — FL opened
the step and FM0 re-locked the plan at `a507baf` before any code. Neither is a verdict with
findings. F6b closed at the verdict carrying `Closes: F6b` (FK1) with no blocking item
open; the report's section 8 makes CLAUDE.md's declaration and names R788-R791 as staying
on the F6a/F6b ledgers without reopening them. I confirm that disposition: none of the four
is in `floatfea/`, a tolerance, a gate assertion, or red here.

The report's `Answers:` header names "FL opens the step; FM0 amended the plan" rather than
a verdict. With no verdict in R1 there is none to name, so the superseded-round check is
vacuous and not a HOLD.

## Findings

Ten items. Eight are defects in `floatfea/` or in a published deliverable under `results/`
(EZ0) and block under CZ0(a); two are FF0 class in the gating apparatus. None is a
tolerance and none is a red test. Ordered by what a reader of the output loses.

**R804. `scripts/write_verdict.py` cannot write an R1 verdict — the SIXTH F-assumption, in
the gate's own writing path.** Section 5a found and repaired five sites (the hook,
`check_carried`, `ci_section`, `test_report_carried`, `test_plan_matches_tolerances`). This
one was missed by both passes, and it is the one that stops the gate working.

```
cmd  grep -n "_milestone|docs/reviews/F|docs/reports/F|F{cleaned}" scripts/write_verdict.py
out  :70   re.fullmatch(r"\d+[a-z]?", cleaned)      after stripping only a leading F/f
     :104  the same expression in _closes
     :110  return f"F{cleaned}"                     --closes could only ever emit `F...`
     :143  report = root / f"docs/reports/F{m}/step-{k}.md"
     :148  out    = root / f"docs/reviews/F{m}/step-{k}.md"
rule FF0: anything that reads the gating record, or decides whether a green is believed,
     is fixed in the NEXT commit under EK2's repair-not-extend rule
```

Five F-assumptions in one file, and `:148` is worse than a refusal: with the validator
satisfied by `--milestone 1` it silently targets F1's verdict file. FF0 class, so the next
commit and not the ledger. **Closed when** `--milestone R1 --step 1` writes this path,
`--closes R1/step-1` emits `Closes: R1/step-1`, and the report check reads
`docs/reports/R1/`; and when the search that found the other five is re-run over `scripts/`
without a pager, so a seventh site cannot hide behind `| head`.

**R805. `floatsim.froude_lambda` reaches the builder and NOT the dynamic scaling.** A
declared field, inside a declared range, that changes half the model.

```
cmd  grep -n "FROUDE_LAMBDA|froude_lambda" floatfea/post/forces_table.py
out  83:  FROUDE_LAMBDA = 50.0
     120: to_full_scale(block, "joint_multiplier_yaw_locked", FROUDE_LAMBDA)
cmd  inspect.signature(forces_table._lam_full_scale)
out  (lam_row: NDArray[np.float64]) -> NDArray[np.float64]      -- no lambda parameter
cmd  build at the declared lambda, and print the factor the dynamic path applies
out  config froude_lambda = 50 -> platform deck_mass 2500000.0, arm length 50.0
     config froude_lambda = 25 -> platform deck_mass  312500.0, arm length 25.0
     the dynamic multipliers are scaled by 50.0 in BOTH cases
     to_full_scale(ones, "joint_multiplier_yaw_locked", 25) = [15625 15625 15625 390625]
     to_full_scale(ones, "joint_multiplier_yaw_locked", 50) = [125000 125000 125000 6250000]
     ratio applied/correct at a declared lambda = 25 build = [8 8 8 16]
rule FL1(a): the deck reference "and optional overrides, declared and recorded in
     provenance"; CLAUDE.md: never assume a unit
```

`FROUDE_LAMBDA`'s declared range is `[1, 1000]`. A configuration declaring `25.0` builds
the geometry and the masses at scale 25 and scales every joint reaction as if at 50 —
**8x too large on force, 16x on the locked moment** — and `provenance()` prints
`froude_lambda: 25.0` into the CSV header and the report, so the artifact says the run was
at 25. This is the same hazard `_lam_full_scale`'s own docstring records being caught once
("the symptom was a PLAUSIBLE WRONG ANSWER rather than a crash"), now reachable from a
declared field with nothing refusing it. `pipeline.py`'s docstring enumerates four fields
that reach the model and two that are refused; `froude_lambda` is in neither list and is
the fifth.

Nothing in the suite can see it: the example declares `50.0`, `forces_table` hard-codes
`50.0`, and the two agree at exactly one point of a three-decade range. The only test that
touches the field —
`tests/unit/test_run_pipeline_refusals.py::test_provenance_records_every_declared_thing:253`
— asserts that it is *printed*, which is the half that makes the defect dangerous.

**Closed when** the scale the dynamic path applies comes from the configuration (a
parameter on `_lam_full_scale` / `compute_rows`), or a declared value other than the one
`forces_table` can honour is refused by name; and a test builds at two different declared
lambda and shows the applied factor following it.

**R806. The published artifacts under `results/R1/example/` drop the label blocks their own
numbers carry in `docs/`, and `cli.py`'s `LABEL` says they are in the run report when they
are not.** EZ0: anything under `results/` is a published deliverable.

```
cmd  grep -c '^#' docs/F4_member_forces.csv results/R1/example/member_forces.csv
out  docs/F4_member_forces.csv              17
     results/R1/example/member_forces.csv   11  (1 generic line + 10 provenance key-values)
cmd  grep -c '^#' docs/F6_utilisation.csv results/R1/example/utilisation.csv
out  docs/F6_utilisation.csv                12
     results/R1/example/utilisation.csv     11  (1 generic line + 10 provenance key-values)
cmd  for each caveat, grep results/R1/example/report.md
out  TENSION 0 / tension 0 / R739 0 / R740 0 / "UPPER BOUND" 0 / "upper bound" 0 /
     heading 0 / EX3 0 / R724 0 / R730 0 / PRELIMINARY 0 / total_max 0 / DZ5 1
rule floatfea/cli.py:31-35 -- "every assumption it rests on is listed in the run report"
```

What is published without them: **R739** (the `N` column is tension-positive, the convention
that, published the other way, "put every over-unity station on API 3.3.1 instead of
3.3.2"); **R740** (288 `total_max` and 288 `total_min` rows whose six components do not
occur together and from which a utilisation is an upper bound, shipped here with no warning
at all); **EX3/R724** ("all cases are heading 0 degrees. The heading dependence is
UNTESTED"); **R743** (`C_m = 0.85` is the LESS onerous of the two); **FA3**, **FA0**,
**FA1**, **R730**, **R741/R742**, and **"PRELIMINARY until F4 closes"**. The utilisation CSV
carries the governing `U = 1.71167` someone sizes steel against and none of its twelve
committed caveats.

The `LABEL` sentence is a CW0 claim about the code, published verbatim into all three
artifacts, and the grep above refutes it. **Closed when** the caveats a reader must act on
travel with the artifact that carries the numbers, and `LABEL`'s sentence is either true or
deleted.

**R807. The builder's own findings are dropped by the whole run path, including five that
say these bodies are not shippable.**

```
cmd  grep -rn "findings" floatfea/run/ floatfea/cli.py floatfea/post/forces_table.py
out  (no output)
cmd  Superstructure.findings for the DEFAULT descent vs for the shipped example
out  default descent (what the measure script builds) : 4 findings
     the example, f handed in by the config           : 9 findings, of which five read
       "<body>: the mass fraction is 0.75, handed in by the caller rather than taken from
        (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never consulted for
        it. This body is a MEASUREMENT, not one to ship."
cmd  grep -c "not one to ship|MEASUREMENT|handed in by the caller" results/R1/example/report.md
out  0  0  0
rule floatfea/model/platform.py:607-618, which writes that finding precisely so a caller
     cannot take an unladdered body for a shipped one
```

Declaring `f: 0.75` explicitly is physically identical to the descent — the example's
comment says so and it is true — but it sets `laddered=False`, which is what *creates*
these five findings. So the findings R1 newly provokes are exactly the ones R1 silently
discards, and `_check_material` re-derives the density one in its own words while the other
five vanish. Its re-derivation also has a narrower domain than the builder's: it fires on
`rho_eq > declared.rho`, so a configuration declaring `rho: 20000` would publish silently
where the builder still flags above-steel.

**Closed when** `floatfea run` surfaces `Superstructure.findings` in the report and in the
CSV headers, and the re-derived density note is either removed in favour of the builder's or
keyed on the same threshold.

**R808. `results/R1/example/report.md:20` publishes a doubled body prefix on the one line a
reader acts on.**

```
cmd  grep -n "^..U =" results/R1/example/report.md
out  20:**U = 1.71167** at `platform:platform:hub4_arm` ROOT, `T_full = 12.5 s`, ...
rule floatfea/cli.py:126-129 formats `{governing[body]}:{governing[member]}` while
     `member` already carries the body prefix
```

The identification of the governing member is malformed in the published artifact, and a
reader cannot grep for that string in either CSV. **Closed when** the line names
`platform:hub4_arm` and the golden test asserts the published string, not only the dict
fields.

**R809. A refused run writes every artifact first.** `floatfea/cli.py:201-208` places the
`required_section` / `truss_sizing` refusal AFTER the three writes and after the governing
line is printed.

```
cmd  floatfea run on a copy of the example with outputs.required_section: true
out  ... 1248 member-force rows in 71.5 s ... 32 checked stations
     floatfea: outputs.required_section / outputs.truss_sizing are FL2(b) and are not
       wired in R1 step 1 ... Refused rather than silently skipped.
     wrote .../member_forces.csv (1248 rows) / .../utilisation.csv (32 rows) / .../report.md
     governing U = 1.71167 at platform:hub4_arm ROOT
     EXIT CODE: 2
     files left by the REFUSED run: member_forces.csv 186958 B, report.md 3575 B,
       utilisation.csv 8280 B
     any of the three mentions the refusal: no
rule CLAUDE.md -- never let a validation failure degrade to a warning
```

"Refused rather than silently skipped" is what the message says; what the disk holds is a
complete, unmarked artifact set indistinguishable from a successful run, with the declared
`required_section` output absent and nothing recording that. A refusal that arrives after
its own side effects is a warning. **Closed when** the check runs before the pipeline — it
is knowable at `load_config` — so a refused run writes nothing, with the measurement that
the output directory is empty.

**R810. A physically unrealisable mass distribution runs to completion and publishes a
screen.** Solved in the weakening direction (EH4): the grid rises until a clean case trips.

```
cmd  build at f = 0.0, 1e-9, 0.5, 0.999999, 1.0 (MASS_FRACTION declared range [0, 1])
out  f = 0.999999  all four hubs and the platform PSD=False, rho_eq 15244.7 / 9527.9
     f = 1.0       the four hubs PSD=False, the platform PSD=True   -- non-monotone
     f = 0.0       member_mass 0.0 on every body, rho_eq = 0.0      -- massless members
     f = 0.5, 0.75 PSD=True everywhere
cmd  grep -rn "admissible|psd" floatfea/run/pipeline.py floatfea/cli.py
out  pipeline.py:290 psd_admissible=bool(admissible(body))
     cli.py:148      OK if entry.psd_admissible else FAILS
rule the golden test's own message: "a non-PSD remainder is not a body"
```

Nothing refuses it. A non-PSD remainder reaches the reader as the word `FAILS` in one cell
of a markdown table, beside a governing utilisation computed on it. And `f = 0.0` yields an
equivalent density of `0.0 kg/m^3`, two decades below the config's own `DENSITY` floor of
`100` — the schema bounds the declared NOMINAL and not the value the model uses. Before R1
no caller could reach a non-PSD `f`: the builder descended `MASS_FRACTION_LADDER` and
`admissible()` gated each rung. The configuration is what opened the range, and it opened it
without the gate. The non-monotonicity at `f = 1.0` is why a spot check would have missed
this.

**Closed when** a configuration whose remainder is not PSD, or whose members come out
massless, is refused by name with the body and the fraction — or the decision to run anyway
is recorded as a locked one and printed where the number is. Solve the boundary both ways:
the largest `f` that is PSD on every body and the smallest that is not.

**R811. Duplicate YAML keys are silently last-wins, which is the exact failure
`_reject_unknown` exists to prevent.**

```
cmd  load a configuration declaring one key twice
out  Fy: 355000000.0 then Fy: 275000000.0   -> ACCEPTED, cfg Fy = 2.75e+08
     platform: {f: 0.75} then {f: 0.30}     -> ACCEPTED, cfg f(platform) = 0.3
     code_check {K: 2.0} then {K: 3.0}      -> ACCEPTED, cfg K = 3.0
rule floatfea/run/config.py:113-127 -- "the reader sets `fy: 420`, the tool runs at 355,
     and the report carries a number nobody asked for. Spelling is part of the interface."
```

`yaml.safe_load` keeps the last duplicate. A misspelling is refused and a duplication is
not, though the duplication is worse: the reader sees `Fy: 355000000.0` on the line they
wrote and the tool runs 275. `Fy` happens to be saved by `_check_material`'s cross-check;
`f`, `K`, `Cm`, `d_outer` and `wall` are cross-checked against nothing. None of the 34
refusal tests covers the shape and section 4's table does not list it. **Closed when** a
duplicate key is refused naming the key and both values.

**R812. `load_cases.window_rule` is accepted, stored, and consumed by nothing.**

```
cmd  grep -rn "window_rule" floatfea/ examples/
out  config.py:234  window_rule: str = ""
     config.py:510  listed in _reject_unknown's known set
     config.py:562  window_rule=str(block.get("window_rule", ""))
     examples/platform12_placeholder.yaml:84  window_rule: "the committed window per case"
cmd  grep -c "window" results/R1/example/member_forces.csv results/R1/example/report.md
out  0  0
rule pipeline.py:8-28 -- "Two do not [reach the model] ... so they are CHECKED AND REFUSED
     rather than ignored"
```

It is in neither the reaching list nor the refused list: it reaches nothing, is refused by
nothing, and is not even in `provenance()`. A user writing `window_rule: "the peak 3
cycles"` gets the committed window and no word about it. Same class as `rho` and `G`, which
were handled. **Closed when** it is refused, consumed, or at minimum recorded in
provenance — and when `pipeline.py`'s enumeration is complete, which R805 also requires.

**R813. EG3's state (1) list is short by three names, and the report's trace proves
reproducibility rather than cause.** The report compares this tree against `e001aec` (F6b's
first-report commit) and finds the two FAILED lists identical. I reproduced that exactly —
and both commits are instances of THE SAME state, so the comparison cannot separate "caused
by the absent verdict" from "red in both trees for another reason". The control that does
separate them is a commit where a verdict exists:

```
cmd  worktree at e001aec, run the two report-guard files, comm against this tree
out  there 37 / here 37 / here-not-there (none) / there-not-here (none)
cmd  worktree at bd315a1 (a verdict EXISTS, report closed), the same two files
out  0 failed
cmd  comm -12 (this tree's 37) (bd315a1's reds)
out  (empty)  -- not one of the 37 is red where a verdict exists
```

So all 37 are verdict-dependent BY MEASUREMENT, EG3(i) is discharged, and **no red here is
CZ1 (iv)**. But three of them are on neither EG3 list and each needed its own run (R644's
discipline): `test_the_reported_CI_counts_are_not_all_zero` ("every CI row in step-1.md
reports zero passed and zero failed"), `test_the_report_carries_a_CI_SECTION`, and
`test_the_R507_cases_rule_as_measured[frames.txt]` — whose failure line mentions no verdict
at all (`_is_a_site('frames.txt')` is `True`, expected `False`) and which is nonetheless
green the moment a verdict exists. The EG3 lists are named in FF0, so this is FF0 class.

**Closed when** the three are on state (1)'s list, or the list's membership rule is stated
as "verdict-dependent, measured against a verdict-exists control" rather than enumerated.

## The five claims the report asked to have attacked - my rulings

**1. Byte-identity: VERIFIED, and the re-key is correct. Its stated justification is not.**

```
cmd  regenerate with the refactored script; diff and sha256 against the committed file
out  CSV IDENTICAL
     ed089b780e34db049059f671e1a09ed09d7ee679e48a4b4fcf97139e08258686  regenerated
     ed089b780e34db049059f671e1a09ed09d7ee679e48a4b4fcf97139e08258686  docs/F4_member_forces.csv
cmd  git diff a507baf..HEAD --stat -- docs/F4_member_forces.csv docs/F6_utilisation.csv
out  (empty)  -- the comparison target was not regenerated to match
cmd  python -m pytest -q tests/regression/test_r1_example_golden.py
out  8 passed in 70.45s
```

The move changed no number, and the baseline it is compared against is untouched, which is
the strong form of the claim. On the re-key, the many-build case the byte diff cannot reach:

```
cmd  eight sequential builds at eight sections; count distinct id(body.model) and retained
out  distinct ids over 8 sequential builds: 8        (8 = no id reuse)
     models held alive by the cache: 10
```

Correct: the entry holds the model, so the id cannot be recycled, and step 2 will not get
stale rotations. The REASON given at the site is refuted by one command and is closure item
C1: node coordinates do NOT move with the section, so the old `(body.name, member.label)`
key returned a numerically correct matrix for exactly the case the docstring names. The
re-key is still the right change — FL2(a) puts topology in the config, where coordinates
will move — but it is a precaution, not a repair, and the cache now retains every model
ever built.

**2. The rounding-boundary row: NOT a blocking defect. I rule with you.** The committed
`0.0738577` is the correct output of a documented two-stage path that writes six significant
figures and reads them back; the configured run is the more accurate of the two; the station
is at 7.4% of allowable and no decision rests on its sixth figure. Your weaker statement is
the honest one and it is sufficient: it does not matter whether other rows are AFFECTED by
the intermediate rounding, only whether any row's PUBLISHED DIGIT changes, and that is
measured at one of 32. The test is the right shape — it names the row, pins the difference
at one unit in the last published digit, reddens on a second differing row, reddens on a
different magnitude, and reddens if the row starts agreeing. Independently: 0 of 7488 force
cells differ at the shipped configuration.

**3. The one-third increase: refusing is correct, and no locked decision is reopened.**
FL1(a) lists the FIELD; EZ4 Q2 fixes its only admissible VALUE. A directive naming an option
does not overrule a Q&A that locked the option off, and a field whose refusal cites the
clause is a declared option, not an omission. The message names EZ4 Q2 and what to do. One
closure item only (C4): the refusal fires in `_utilisations` after a 67-second solve though
it is decidable at `load_config` — the same misplacement as R809, without R809's
consequence.

**4. The field ranges are NOT tolerances. I agree, explicitly, because the rule's wording is
absolute and the ruling needs to be on the record.** A tolerance in this repository is a
value against which a RESULT is compared, or one introduced to make two numbers agree;
CLAUDE.md's own list is convergence thresholds, comparison epsilons, small-number guards and
tier cutoffs. A `Bound` in `config.py` is the declared DOMAIN OF AN INPUT: no result is
compared against it, nothing is made to agree by it, and widening one can only admit a
configuration that was previously refused outright. It cannot turn a red into a green, which
is the property the prohibition exists to protect. They stay in `config.py`, and FL3(a)
wants them documented there. I verified nothing tolerance-shaped was added:

```
cmd  grep -nE "isclose|abs_tol|rel_tol|approx|2\*\*-|atol|rtol" over the five new/moved files
out  four hits, all the word "approximation" in prose
cmd  git diff d29bf6b..HEAD --stat -- floatfea/tolerances.py
out  (empty)
```

Both tolerances you removed before committing were right to remove: the implied-`nu`
`isclose` compared two declared constants with nothing to be approximate about, and the
residual is exactly `0.0` on all five bodies because the two halves sum to the whole. Note
R810 as the one place this ruling has a limit — a bound on a declared NOMINAL (`rho`) that
the model does not use does not bound the value the model computes.

**5. Section groups keyed by body name: not a finding for step 1.** Measured, per body:

```
out  platform D=3.000 A=1.5947 ; hub1..hub4 D=2.500 A=1.3119  (platform group changed alone)
     a group the deck does not have -> REFUSED naming it and the deck's bodies
     a group the deck has and the config does not -> REFUSED naming it
```

The per-group dict reaches each body correctly and both directions of the mismatch are
refused. See C8 for the two siblings that will break with it in FL2(a).

**And the three corrections you offered.** `hub4_arm` is right and `hub2_arm` was an artifact
of maxing a rounded deliverable; the golden's three-way assertion (published value, body and
station, plus hub4 ranked first at full precision and strictly ahead of hub2) is the correct
shape and does not pin a tie-break. The twelve test names in section 4's table all resolve
to a real `def` at the path given, checked mechanically. The FF0 repair is additive and
deletes no guard — I diffed `.claude/hooks/require-verdict.sh` line by line: `1e330cc` is
standalone, cites FF0, touches nothing under `floatfea/` or `tests/`, the label validator
still refuses `R1draft`, `F6ab`, `Freports`, `F6-draft`, `1` and the empty string, the tie
is still refused naming both paths, `m_body` survives only in a comment, and the widened
glob admits no non-plan file (`docs/milestones/*.md` yields exactly `R1.md` under the marker
grep). **Not a STOP.**

## The adversarial case, and what the gate detects

The step's gate carries its own failure. One variable moved, in process, against the
committed deliverable, and repeated once:

```
cmd  run the pipeline at wall = 0.1818 (1% thicker) on every group; compare all 7488
     published cells and the governing U against docs/F4_member_forces.csv
out  CONTROL unmutated              : 0/7488 differ, governing U = 1.71167     -> GREEN
     wall 1% thicker on every group : 2058/7488 differ, governing U = 1.69845  -> RED
       by basis: dynamic_max 491, dynamic_min 518, total_max 461, total_min 459,
                 total_instant 79, static 50 ; worst relative 1.458e+02
rule the force-cell and governing-U assertions in tests/regression/test_r1_example_golden.py
```

So the golden is live on the quantity the configuration most directly controls, and it is
live despite `rho_eq` being back-computed to hold `rho*A` invariant — the motion is mostly
in the dynamic bases, which is F6a's recorded rotary-inertia mechanism, with 50 static cells
moving too. The adversarial cases it is BLIND to are R805's (lambda agrees at the single
point the example sits on) and R810's (the shipped fraction is PSD, so no assertion in the
suite ever sees a non-PSD build).

## CI at the reviewed commit: UNAVAILABLE (not red, not green)

```
cmd  gh run list --commit 472bcd1 --json name,conclusion,workflowName
out  []
cmd  git ls-remote --heads origin | grep F3 ; git rev-parse HEAD
out  bd315a17...  refs/heads/F3
     472bcd1a...  (local)
```

No workflow ran on the reviewed commit, nor on any of the four in scope: they are not
pushed. This is NOT CK2's exhausted-allowance state — there are no started-but-unrun jobs,
no empty `runner_name`, no spending annotation; there is simply no run. Recorded as
unavailable rather than skipped over. The last run that executed is `bd315a1` (workflow CI,
`success`, 2026-10-12T05:47Z), and CK2's follow-up question has a non-empty answer:

```
cmd  git diff bd315a1..HEAD --stat -- tests/verification scripts .github
out  scripts/check_carried.py 12 +- / scripts/ci_section.py 12 +- /
     scripts/measure/member_forces_table.py 482 +------ /
     tests/verification/rung3/test_closure_evidence_exists.py 8 +-
```

So that green does NOT describe the tree under review — the 482-line extraction from the
deliverable-producing script is inside the gap. The step is judged on everything else, and
the three lint gates are green under my own run: `ruff check floatfea tests scripts` gives
`All checks passed!`, `black --check floatfea tests scripts` gives `146 files would be left
unchanged`, `mypy floatfea` gives `Success: no issues found in 42 source files`.

FL1(c) asks for a CI golden and the wiring is there: `tests/regression` runs in the `ladder`
job's rung-6 step (`.github/workflows/ci.yml:501`, `sh scripts/run_rung.sh
empty:tests/verification/rung6 full:tests/regression`), and `data/f4/dynamic_inputs.npz` is
tracked, so the golden is runnable on a clean checkout. It has simply never run.

## Corpus (EG4(e))

**The pause held; no batch, and no entry added.** R1 step 1 touches neither exception — not
F4's load-mapping gate and not EB6's label-provenance gate. I ran the recorded substitute
instead, both halves, and both produced blocking findings:

* **a continuum grid over the parameter space the decision rules guard** — `f` over
  `{0.0, 1e-9, 0.5, 0.999999, 1.0}`, `froude_lambda` over `{1, 25, 50}`, `d_outer` over
  `{2.5, 2.6..3.2, 3.0, 4.0}`, `wall` over `{0.18, 0.1818, 1.3}`, heading over
  `{0, 45, 360, 400}`, plus four duplicate-key shapes and the string / bool / NaN shapes.
  This produced R805, R810 and R811.
* **a regeneration check on a published deliverable** — regenerating
  `docs/F4_member_forces.csv` through the refactored script (sha256 identical) and comparing
  `results/R1/example/*` against the committed deliverables' label blocks. This produced
  R806, R807 and R808.

Twelve of the refusals in section 4's table I exercised myself against configurations the
implementer did not write; every one refused, and each message named the field, the value,
the range and the unit. The three holes above are not refusals that fail — each is a shape
with no refusal at all, which is why a grid over the declared domain found them and a list
of planted shapes would not have.

## Tolerances touched

**None, verified independently.** `git diff d29bf6b..HEAD -- floatfea/tolerances.py` is
empty. My own grep over `config.py`, `pipeline.py`, `cli.py`, `forces_table.py` and
`test_r1_example_golden.py` for `isclose|abs_tol|rel_tol|approx|2**-|atol|rtol` finds only
the word "approximation" in prose. The two the implementer removed before committing are
correctly gone and both replacements are exact comparisons. The 15 `Bound` constants in
`config.py` are declared input domains and not tolerances, ruled above under claim 4. One
cosmetic exception is C6.

## Closure items

Fixed once, in the step's closure commit; not re-reviewed item by item. C2 and C9 are FF0
class and belong in the next commit rather than the ledger.

* **C1.** `floatfea/post/forces_table.py:180-191` — the `_rotation` docstring's reason is
  refuted: "returns bodies with the SAME names at a different geometry" is false for a
  section change (node coordinates are identical across two builds at `D = 2.5` and
  `D = 4.0`, and the matrix is a pure function of the two end coordinates). The re-key is
  right; the justification should say it is unique by construction and that FL2(a) is what
  will move coordinates. Note also that the cache now retains every model built (10 models
  after 10 builds) under precisely the loop it was changed for.
* **C2.** `floatfea/run/pipeline.py:8-28` — the docstring enumerates four fields that reach
  the model and two that are refused. The true counts are five and two (R805, R812). It is
  prose a reader uses as a contract, so FF0 class alongside its code.
* **C3.** `tests/regression/test_r1_example_golden.py:190` — still reads "the station is at
  `U = 0.074`" after the report corrected that figure to `U = 0.0738576` elsewhere. Correct
  to two significant figures, so not false; inconsistent with the repair it belongs to.
* **C4.** The `one_third_increase` refusal fires in `_utilisations` after a 67-second solve
  though it is decidable at `load_config`.
* **C5.** `floatfea/post/forces_table.py` raises `SystemExit` in two places. Named in the
  report and correctly left out of a byte-identity commit; it belongs in the next one.
* **C6.** `floatfea/run/config.py:465` — `("m", -1.0e4, 1.0e4)` is an inline bound where the
  other fifteen are named module constants, so the lumped-mass position is the one field
  whose domain is not documented where the schema documents domains (FL3(a) will need it).
* **C7.** `floatfea/cli.py` has no test of any kind — 262 lines, FL1(b)'s deliverable, and
  the only file in the step with no coverage. R806, R808 and R809 all live in it. I am not
  asking for new apparatus: the two new test files cover `config.py` and `pipeline.py`, and
  the third file that shipped is the one nothing reads.
* **C8.** `_k_l_over_r` and `RunResult.section_properties` both take `body.members[0]` as the
  body's representative. True today (every body's members share one length: 25.0 on each hub,
  50.0 on the platform) and silently false under FL2(a)'s member list. `_sections_for`
  carries a note saying FL2(a) replaces it; these two do not, and `_rotation` is what that
  latency costs.
* **C9.** EG3's state (1) list (R813's three names). FF0 class.
* **C10.** `results/R1/example/utilisation.csv` repeats `utilisation` and `governing_clause`
  in trailing columns (`DictWriter` over the record's own keys), so the published screen has
  two columns carrying the same number under different headings.

## Next step opens when

Step 2 does not open. R804 is answered first, because nothing else can be recorded through
the sanctioned path until it is. Then, specifically:

1. **R805** — the scale applied to the dynamic multipliers follows the declared
   `froude_lambda`, or a value `forces_table` cannot honour is refused by name; with a test
   that builds at two declared lambda and shows the applied factor following it. Not a test
   that the value is printed.
2. **R806, R807, R808** — the artifacts under `results/R1/example/` carry the caveats their
   numbers carry in `docs/` (R739, R740, EX3/R724, R743, FA0, FA1, FA3, R730, R741/R742 at
   minimum); the builder's nine findings reach the report; the governing line names
   `platform:hub4_arm`; and `cli.py`'s `LABEL` sentence is true or deleted. Regenerated at
   the answering commit, not carried over (CP3).
3. **R809** — the `required_section` / `truss_sizing` check runs before the pipeline, with
   the measurement that a refused run leaves the output directory empty.
4. **R810** — a non-PSD remainder or a massless member is refused by name with the body and
   the fraction, and the boundary is solved in BOTH directions rather than sampled.
5. **R811** — a duplicate YAML key is refused naming the key and both values, with the three
   shapes above as the cases.
6. **R812** — `window_rule` is refused, consumed, or recorded; and `pipeline.py`'s
   enumeration is complete.
7. **R813 and C2 / C9** — the FF0-class items, in the next commit, not the ledger.

Everything FL1 asked for is present and the hardest part of it is right: the core moved
byte-identically against an untouched baseline, the example reproduces 7488 force cells and
31 of 32 utilisations exactly with the 32nd's cause isolated inside the test, the governing
`U = 1.71167` is confirmed on the correct arm, the twelve refusals all refuse with messages
a reader can act on, the gate reddens on a 1% section change, and the whole suite is green
outside a boundary state I measured to be verdict-dependent. What the ten findings have in
common is narrower than "the step is not done": with one exception they are about what the
tool SAYS about a run it has performed — a declared field that reaches half the model and is
reported as though it reached all of it, nine findings the builder wrote and the reporter
dropped, a label block that did not travel with its numbers, a refusal that arrives after
its own artifacts, a doubled prefix, a duplicate key accepted in silence. R1's whole subject
is a tool that someone else will point at a configuration nobody here has seen. On that
subject the output is the product, and FL1(a)'s "refusing with messages" is the deliverable
rather than the packaging.

The schedule is not at risk from this HOLD. Nine of the ten are small and local, and the
step's substance — the schema, the CLI, the extraction, the golden — stands.
