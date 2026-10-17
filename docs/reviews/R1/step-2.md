# Review — R1 step 2
Reviewed commit: d205833943b7a4fa56c349d06fbd6f0d0f86e5fc
**Reviewed commit: `d205833943b7a4fa56c349d06fbd6f0d0f86e5fc`.**
Verdict: HOLD
**Reviewed commit: `d205833943b7a4fa56c349d06fbd6f0d0f86e5fc`.**
Tests: 3625 passed, 9 failed, 1 skipped
Scope: **ES0 INTERIM CHECK.** No new report revision exists, so this counts against no
round and revision 3 of 3 remains available. One blocking finding.

**MY OWN RUN, AT THE REVIEWED COMMIT, TREE CLEAN.** `python -m pytest -q --tb=no -rf`:
`9 failed, 3625 passed, 1 skipped, 2 warnings in 903.55s (0:15:03)`. I did not take the
report's count, and there is no report revision to take one from. The implementer ran
`tests/unit tests/regression/test_r1_published_artifacts.py` only (224 passed) and asked
whether the light scope requires the full suite. **It did, and that is where the finding
is:** the subset the implementer chose cannot contain the red this commit creates. ES0's
light scope is "the suite and CI at the commit", and an eight-file subset is not the
suite. Nine reds locally, nine in CI, identical ids.

**EU1 DOES NOT ATTACH, AND I RAN ITS CASE ANYWAY.** No tolerance value and no declared
counter moves:

```
cmd    git diff 62e48af..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 62e48af..HEAD -- floatfea tests scripts | grep "^+" |
       grep -cE "isclose|abs_tol|rel_tol|approx|atol|rtol"
out    0
```

The adversarial case was run regardless, at a configuration the diff did not choose: the
whole declared type space rather than the three fields the diff names. See Findings and
Corpus.

**THE SEPARATE DIFFS, ALL EMPTY, NO STOP-CLASS FINDING.**

```
cmd    git diff --stat 62e48af..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)
cmd    git diff 62e48af..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py            -- a file, as my instructions say it must be
cmd    git diff --stat 62e48af..HEAD
out    floatfea/run/config.py 18+/3-, scripts/carried_table.py 16+/1-,
       tests/unit/test_run_config.py 42+/5-     -- three files, nothing else
```

**STEP 1b DOES NOT FIRE AND I AM SAYING SO RATHER THAN SKIPPING IT.** There is no new
report revision, so there is no new `Answers:` header to compare. The newest revision
reads `Answers: verdict 6 @ 43bcd0c` and verdict 7 is newer, which is precisely the state
ES0 describes as legitimate -- a report predating the findings it has not yet answered.
Revision 3 must read `Answers: verdict 8 @ <this verdict's commit>`.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R837** (the `str()` coercion survives at a fourth declared string) | **ANSWERED, AND WIDER THAN THE CONDITION ASKED** | `_require_string` now wraps all three `Path(str(...))` sites: `config.py:600` deck, `:762` npz, `:852` directory. Verified by my own mutation, not by reading the report: baseline **126 passed**; reverting one site at a time gives `1 failed, 125 passed` and the one red is that site's own parametrisation -- `[floatsim.deck-deck]`, `[load_cases.npz-npz]`, `[outputs.directory-directory]`, one id each. All three reverted at once: `3 failed, 123 passed`. The condition asked for one row per call site; three rows shipped. Closed. |
| **R837's census half** | **NOT MET -- third round on the same needle. R842.** | the condition was "the census published as a needle that finds `str(` at any nesting depth". The census I was given reports the wrong count by six. Non-blocking (a sentence in a report that does not exist yet), recorded as **R842** so revision 3 publishes a measurement rather than a grep. |
| **R838** (R831's needle solved in one direction only) | **STILL OPEN, untouched by this diff** | `git diff 62e48af..HEAD -- tests/regression/` is empty. Correctly deferred: it does not block and the implementer named it revision-3 work. The two weakening directions are still green. |
| **R839** (the eight reds have one cause, section 7 states two) | **STILL OPEN, AND IT MOVED: there are now TWO causes and the second is new** | traced again, one id at a time per EG3(i). The cascade's `[baseline]` inner run now names **two** reds where last round it named one. The second is this commit's own. See **R841**. |
| **R840** (`carried_table.py` does not escape the cell separator) | **DONE, THE REPAIR IS CORRECT -- and it is in the wrong commit. R841.** | `_cell` at `scripts/carried_table.py:219`. I reproduced both figures: the committed revision-2 table has 4 rows with the wrong cell count (R819, R825, R826, R828); the new generator gives `rows with cell count != 3: 0` over 19 rows, counted with an escape-aware splitter. The escape is right. What it also does is redden a guard at a pushed, reviewed commit for a cause no clause covers. |
| **R835** (EG3's enumeration) | **still open, still Xabier's** | not a round's work. This commit is its sixth measurement, and this time the enumeration is not SHORT -- it is LONG. Recorded under R841's judge paragraph as a new direction for the same proposal rather than as a second proposal. |
| **R836** (the r754 margin in the wrong variable) | **answered at verdict 7, unchanged** | recorded item, no change in this diff. |
| **C29, C34, C35** | **done at verdict 7, unchanged** | `ruff check floatfea tests scripts`, `black --check floatfea tests scripts` (147 files) and `mypy floatfea scripts/f4_dynamic_residual.py` (43 files) green on my machine, and green in CI at this commit. I ran all three. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C38, C39, C40** | **carry to the closure commit** | not re-reviewed item by item. **C27 recurs -- R842.** **C37 widens: the "Quote the name." sentence now fires at three PATH fields** (`outputs.directory`, `floatsim.deck`, `load_cases.npz`), so the noun is wrong for five of six call sites rather than one of three. Same item, bigger. |
| `scripts/suite_count.py`'s own line + CZ1 (ii)/(iii)'s four outputs | **still owed, correctly** | FC1: a line naming a sha cannot be inside that sha. Due in the follow-on commit, as verdict 6 ruled and verdict 7 affirmed. Not a finding. |
| **EG3(ii): state (1) measured at verdict 7's own commit** | **DONE; the number is inside R841** | the report-guard files run in a real worktree at this tree with verdict 7 present. |

## Findings

**ONE BLOCKS, and it is not in `floatfea/`.** The R837 repair is complete, bound site by
site, and survives the whole declared type space. The blocking finding is the ninth red
this commit creates in its own gating apparatus -- which the implementer's eight-file run
could not see, and which wears a boundary-state name while having a non-boundary cause.

**R841. (BLOCKS -- CZ0 head (d), with CA2) THE NINTH RED AT THIS COMMIT IS CAUSED BY THIS
COMMIT'S OWN GENERATOR CHANGE AND BY NEITHER EG3 BOUNDARY STATE. One variable moved,
everything else held: removing the escape takes the suite from 9 failed to 8. The red
carries a name that is ON STATE (2)'s LIST, so a reader matching nine ids against EG3's
enumeration concludes all nine are designed -- which is R629's shape exactly, and the
reason EG3(i) demands the individual trace.**

```
claim  of the nine reds at this commit, eight are the step-boundary cause and the ninth
       is the R840 escape, measured rather than classified
cmd    python -m pytest -q --tb=no -rf     (mine, at the reviewed commit, tree clean)
out    9 failed, 3625 passed, 1 skipped in 903.55s
         test_the_Carried_table_is_what_the_generator_produces
         test_the_report_carries_a_WHOLE_SUITE_count
         test_the_guard_survives_the_state[baseline] + 6 others
cmd    gh run view 39057667873 --log-failed      (CI, same commit)
out    9 failed, 1147 passed, 1 skipped in 635.58s -- the same nine ids
cell   a WORKTREE at HEAD (not a git archive -- these guards read git), `_cell` removed
       from the one row it is applied to, nothing else touched:
out    with the escape      9 failed, 262 passed, 1 skipped
       escape REMOVED       8 failed, 263 passed, 1 skipped
       the test that moved  test_the_Carried_table_is_what_the_generator_produces
       the other eight      unchanged, id for id
cmd    the failing assertion's own message, at HEAD
out    "4 generated rows are not in the report's Carried section, the first being:
          | R819 | **answered** ... | (the ceiling) \| answered, and more completely ..."
       -- the four rows are R819, R825, R826, R828: the four R840 named
cmd    tests/test_report_carried.py:1117-1121, and what it compares
out    VERDICT_TEXT = _verdict_text_at(ANSWERED)   -- the verdict the REPORT ANSWERS
       CARRIED      = _section(_newest_revision(REPORT_TEXT), "Carried")
       -- so it compares the generator's output for verdict 6 against revision 2's
          published table, and revision 2 is CLOSED: verdict 7 exists, and EK3 forbids
          any commit touching a closed report before a newer verdict
cmd    the cascade, traced individually per EG3(i): [baseline] on its own
out    "baseline: expected a clean run", and the inner log names TWO failures --
         test_the_Carried_table_is_what_the_generator_produces
         test_the_report_carries_a_WHOLE_SUITE_count
       At verdict 7 the same inner run named ONE. The seven cascading states now inherit
       a second cause, and it is this commit's.
cmd    test_the_guard_reads_the_step_being_worked_on, on its own
out    PASSED  -- state (1)'s own named baseline did not fire, as expected: a verdict
                  exists and the tree is in state (2)
rule   CZ0 (d), a red test at the reviewed commit; CA2, which CLAUDE.md does not carry so
       I keep it in full -- a red CI is a HOLD regardless of what the local run says;
       EG3(i) -- EVERY red traces by name to the step-boundary cause or it is CZ1 (iv)
       unchanged; FN2/R813 -- "the membership rule is verdict-dependent, measured against
       a verdict-exists control, and the enumeration is a convenience"; BP0 -- when a
       decision rule changes, every figure citing the old rule is regenerated or withdrawn
       IN THE SAME COMMIT; EK3 -- a commit never touches a closed step report
judge  **the ablation is the whole finding.** This red is not verdict-dependent: a verdict
       exists at this commit and the red is caused by the escape, which I established by
       removing the escape and nothing else. By FN2's rule it is not a member of state
       (2), and the fact that its NAME is on state (2)'s enumeration is the hazard rather
       than the defence -- the enumeration has been short twice (EH1, FN2) and this is the
       first time it is LONG. A list of names cannot distinguish a designed boundary red
       from an apparatus change that reddens a listed name; only running the id under a
       one-variable ablation can.
       **And BP0 with EK3 decides which commit the escape belonged in.** BP0 says the
       figure is regenerated in the same commit as the rule; EK3 says a closed report may
       not be touched; so the only commit that may carry a change to `carried_table.py` is
       the commit that writes the next report revision, because that is the only commit
       that may regenerate the table the generator feeds. FF0's "fixed in the next commit"
       is satisfied by revision 3's commit and does not license leaving a pushed, reviewed
       commit red for a cause no clause covers. **The escape itself is correct and must
       not be reverted** -- 4 of 15 malformed rows before, 0 of 19 after, both reproduced
       here. What is wrong is that the step's own record now reads nine reds where eight
       are designed, and nothing in the tree says which is which.
       **This is also R839 one round later in the same shape:** verdict 7 found section 7
       claiming two causes where the trace gave one; this commit creates a second cause
       and there is no revision in which to say so.
```

**Closed when** revision 3's commit carries the regenerated section 8 from this generator
-- which clears the red by construction, since the guard reads the newest revision's
Carried section and the sha in that revision's own `Answers:` line -- **and** its section 7
traces all reds individually with the ninth's cause named as the generator change,
established by the ablation, rather than filed under the EH1 cascade or under FC1. If any
pushed commit before that one still carries this red, that commit's report states which of
the three causes each red has. **Reverting `_cell` is not the repair and would re-open
R840.** The reusable half, which is what I want recorded: a change to a generator whose
output is published inside a closed artifact lands in the commit that next regenerates
that artifact, and in no earlier one.

**R842. (DOES NOT BLOCK -- recorded; the census, for the THIRD consecutive round) THE
NEEDLE THAT CERTIFIES THE str() CLASS CLOSED IS STILL THE WRONG INSTRUMENT, AND THE
COUNT I WAS GIVEN IS WRONG BY SIX. The class IS closed -- I closed it with the type space,
not with a grep -- and that is the point.**

```
claim  the unanchored census does not return "only two docstring-prose mentions"
cmd    grep -c "str(" floatfea/run/config.py
out    8
cmd    grep -n "str(" floatfea/run/config.py
out    114, 274     docstring prose
       138          key = str(key_node.value)
       153          texts = [str(k.value) for k, _v in node.value if ...]
       517,521,523  return str(path.relative_to(...)) / str(path)
       894          _reject_unknown(loaded, _TOP, str(source.name))
cmd    what each of the six live ones does, read rather than counted
out    138/153  yaml.ScalarNode.value is ALREADY a str: these are the TEXT half of the
                duplicate check and the message that names collapsed keys -- R822's own
                repair. No declared input VALUE passes through either.
       517-523  Path -> text on the provenance OUTPUT path, not on an input
       894      source.name is already a str
rule   verdict 7's closing condition on R837 -- "the census is published as a command that
       finds a str( at any nesting depth, not as the spelling the repair used"; C27
       verbatim -- "the needle searches for its own repair and reports success"; BF0
judge  the class is genuinely closed and the needle still cannot say so. `= str(` missed
       three sites; `str(` unanchored finds eight and the claim attached to it says two,
       so the instrument is now wrong in the other direction. **A census over a spelling
       cannot answer a question about a type.** The measurement that does answer it is in
       Corpus below: every declared field in the schema crossed with seven YAML shapes,
       154 cases through the real load_config, zero coercions. Non-blocking because the
       sentence is in a report that does not exist yet; recorded so revision 3 publishes
       the grid rather than the grep. If the grep ships with "two" beside it, that is C27
       for a fourth round.
```

**R843. (DOES NOT BLOCK -- recorded) THE ONE VALUE IN THE STRING SPACE THAT STILL LOADS
AND IS STILL NOT A DIRECTORY: an EMPTY STRING at `outputs.directory` RESOLVES TO THE
CONFIG FILE'S OWN DIRECTORY, so the three EZ0 deliverables are written beside the config
-- for the shipped example, into the tracked `examples/`. EH4's weakening direction on the
check this commit added.**

```
claim  the new type check's boundary, solved from the side that WEAKENS it
cmd    outputs.directory offered each of False / True / 12 / None / [] / {} / the empty
       string, through the real load_config on the shipped example
out    False         REFUSED   outputs.directory: False (bool) is not a string...
       True          REFUSED   ...
       12            REFUSED   ...
       None          REFUSED   ...
       []            REFUSED   ...
       {}            REFUSED   ...
       empty string  LOADED    dir=examples        <- the config file's own directory
       CONTROL: ../results/R1/example   LOADED     dir=example
cmd    where the artifacts then go
out    floatfea/cli.py:343  out = cfg.outputs.directory, and _write_member_forces does
       path.parent.mkdir(parents=True, exist_ok=True)
rule   EH4 -- the injection falls toward the clean value until a clean case passes; and
       (base / the empty string).resolve() is base, which is the config's own folder
judge  **milder than R837 and in the same family.** A `directory:` key written with nothing
       after it is None and is now refused, which is the invited typo; an empty string
       takes deliberate quotes, so this is not a plausible slip. But it is the one
       admissible member of the string space that is not a usable directory, and the
       consequence is three deliverables written into whatever folder holds the config --
       a TRACKED source directory for the shipped example, which _absolutise's own
       docstring says the tests take care to avoid. One line, at that site alone: `tag`
       and `window_rule` legitimately default to the empty string and must keep doing so.
       Not blocking; if revision 3 leaves it, it leaves it with that sentence.
```

**R844. (DOES NOT BLOCK -- closure item C41, and the figure is MINE) "THREE OF ITS FIVE
SIBLINGS ARE BOOLEANS IN THE SHIPPED EXAMPLE" IS WRONG AT TWO SOURCE-TREE SITES. FIVE OF
FIVE ARE. It is verdict 7's own figure, republished into `floatfea/` and `tests/` without
being re-measured, and the argument it supports gets STRONGER when corrected -- which is
why nobody checked it.**

```
claim  the outputs block's five non-directory keys, as the shipped example declares them
cmd    yaml.safe_load of examples/platform12_placeholder.yaml, the outputs block minus
       directory, each value with its type
out    siblings declared: 5
       report: (True, bool)            member_forces_csv: (True, bool)
       utilisation_csv: (True, bool)   required_section: (False, bool)
       truss_sizing: (False, bool)
       booleans: 5
cmd    where the sentence is
out    floatfea/run/config.py:858         three of its five siblings ARE booleans in the
                                          shipped example
       tests/unit/test_run_config.py:507  THREE of its five siblings are booleans in the
                                          shipped example
       docs/reviews/R1/step-2.md:93       -- verdict 7, where it came from
rule   CW0 -- prose in the source tree is a test, a triple, or deleted; BP0/CP3 -- a figure
       is taken against the tree it describes, after the last edit
judge  a reviewer's figure copied into two shipped files is still a claim about the code,
       and one command refutes it. Closure item, not blocking: the sentence is a comment
       and a docstring, the refusal it argues for is correct, and correcting the count
       makes the asymmetry argument stronger rather than weaker. **The reason to record it
       is the direction of travel.** Verdict 7 measured every declared BOOLEAN in the same
       block and recorded that all five refuse by name -- five -- then wrote "three of its
       five" one paragraph later. The implementer carried the wrong half into `floatfea/`.
       A number a reviewer publishes is a number the implementer will paste, so it is
       subject to CP3 like any other.
```

**THE IMPLEMENTER'S OWN QUESTION, ANSWERED BY MEASUREMENT RATHER THAN BY READING, AND IT
IS NOT A FINDING.** "Does the `_absolutise` change make some OTHER case in that file
vacuous?"

```
claim  the conditional fixture diverges from the unconditional one on exactly the three
       cases under test, and on nothing else in the file
cell   _absolutise instrumented to print every divergence -- non-string, missing block,
       missing key, empty string -- and the whole file run
out    53 tests, 3 divergences, all three the new rows:
         non-string bool  outputs.directory=False
         non-string bool  floatsim.deck=False
         non-string int   load_cases.npz=1
       missing-block: 0   missing-key: 0   empty-string: 0
cell   the fixture reverted to the unconditional form, config.py untouched
out    3 failed, 123 passed   -- exactly the three new rows, by id
rule   my own recorded guard: a fixture that silently stops transforming an input is the
       shape of a test that cannot fail, so check that the collection the assertion
       inspects can still contain the failure
judge  **50 of the 53 take a byte-identical path, and the three that do not are the three
       the change exists for.** Nothing in the file is made vacuous today, and the
       ablation says the change was NECESSARY rather than incidental: with the old fixture
       the three cases die inside the fixture and never reach load_config. One latent
       weakening, recorded and not a finding: the new form silently skips when the BLOCK or
       the KEY is absent, where the old form raised KeyError for floatsim.deck and
       outputs.directory. Zero tests exercise that today -- measured, not assumed, by the
       two counters above -- so a future case that deletes `outputs` would run against an
       unresolved relative path instead of erroring loudly. One line to make the skip say
       which of the two reasons it skipped for.
```

## Try to break it -- the adversarial cases I ran, and what they found

* **The whole declared type space, not the three fields the diff names.** 22 declared
  leaves x 7 YAML shapes = 154 cases through the real `load_config`. **Zero coercions, zero
  non-ConfigError exceptions, zero refusals that fail to name the field.** Every LOADED row
  is legitimate: a number in range, a boolean in a boolean field, None in the two optional
  sensitivities, and three empty-string cases of which two are documented defaults.
  **R843** is the third.
* **Fifteen revert-red-restore cycles of my own**, baseline 126: the three new call sites
  one at a time (1 failed each, bound by id), all three at once (3 failed), the fixture
  reverted (3 failed), and the escape ablated in a real worktree (9 -> 8). **Every repair
  in this commit is held and bound to its own site.**
* **The nine reds traced ONE ID AT A TIME, not as a family.** That is what found **R841**.
  Ruling the cascade by class would have filed a new cause under an old heading for the
  second round running.
* **The verdict-exists control, and I did it in a WORKTREE.** The previous round recorded
  that `git archive` gives 30 failed at a commit CLAUDE.md cites as 0 failed, because these
  guards read git. I took that warning: every report-guard measurement here is in a real
  worktree at `d205833`, and only the mutation cycles that touch no git-reading guard are
  in an archive.
* **A whole-file regeneration of all three published deliverables**, run from this tree and
  diffed line for line against the committed artifacts. `governing U = 1.71167 at
  platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)`, 1248 rows, 32 rows. Differences:
  the provenance path prefix (my run was from a worktree, so the relative deck path renders
  with a `wt/` segment) and one timing cell, build 0.19 -> 0.12. **No engineering number
  moved.** 8, 8 and 20 diff lines on the three files, all accounted for.
* **The escape's own output, counted with an escape-aware splitter** rather than taking the
  implementer's figure: 0 of 19 rows with the wrong cell count, and 4 of 15 in the committed
  revision-2 table. Both figures reproduce.
* **ruff, black --check and mypy in CI's own wider forms**, on my machine: green, 147 files,
  43 source files. And green in CI at this commit, on a machine neither of us controls.

**What I did not find, and it is the larger part.** R837's repair is the strongest of the
step so far: the finding named one site, the repair took three, each is bound to its own
parametrisation by id, and the class survives a 154-case type grid rather than a needle.
The fixture repair that came with it was necessary, was reasoned about in writing, and the
implementer asked to have it attacked rather than asserting it was safe -- which is the
right instinct and the reason I could answer it with a divergence count instead of an
opinion. R840's escape is correct and reproduces in both directions. The blocking finding
is not in the engineering code and not in the repair; it is that fixing a gating generator
one commit early left a pushed, reviewed tree red for a reason no clause names, in a step
whose last two rounds were both about reds being filed under the wrong cause.

## CI at the reviewed commit: RED, nine reds, EIGHT designed and ONE not

```
cmd    gh run list --commit d205833943b7a4fa56c349d06fbd6f0d0f86e5fc
         --json name,conclusion,workflowName,status
out    [{"conclusion":"failure","name":"CI","status":"completed","workflowName":"CI"}]
       -- NOTE FOR THE NEXT READER: `gh run list --commit d205833` (the SHORT sha)
          returns an empty list. The run exists; the flag needs the full sha. A reviewer
          who takes the short form reaches CK2's unavailable state by accident.
cmd    gh run view 39057667873 --json jobs, read at STEP level
out    lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS / guards and meta-tests FAILURE
         -> 9 failed, 1147 passed, 1 skipped in 635.58s
       the verification ladder : SUCCESS   -- rungs 1, 2, 3, 6+regression, 4, 5, all six
       CI determinism -- leg / ten legs agree : SKIPPED
cmd    gh run view 39057667873 --log-failed, the nine FAILED ids
out    identical to my own local nine
```

**Not CK2's exhausted-allowance state.** Both real jobs ran with per-step conclusions and
real counts -- fourteen minutes on the lint job, seven on the ladder -- so this is a
completed red build and not a never-started one. The two determinism jobs are skipped by
the workflow's own event gate (CK0 by design) and are recorded as that, not as an
unavailable check. `mypy` is green here, and the `unit tests` and `guards and meta-tests`
steps both RAN rather than being skipped behind an earlier red, which is the thing CZ1
(iii) exists to see.

**On CA2, which I keep in full because CLAUDE.md does not carry it:** a red CI is a HOLD
regardless of the local run, and EG3 is the only clause that qualifies CZ0's head (d).
Eight of the nine trace by name and by ablation to the step-boundary cause and are waived.
**The ninth does not, so head (d) stands and this HOLDS.** The waiver is conditional on
every red tracing, and one does not.

## Corpus (EG4(e))

**The pause held. Zero new entries, `tests/corpus/` untouched by me, `git status
--porcelain` empty.** Neither exception opens: this diff touches no part of F4's
load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about the declared config strings this diff refuses --
the same check verdicts 6 and 7 made, re-made here because R837 is again a
declared-identifier finding.

**I ran the recorded substitute, both halves, and this round BOTH paid:**

* **A continuum grid over the parameter space a decision rule guards** -- every declared
  leaf in the schema (22) crossed with the seven YAML shapes a lenient parser takes
  (False, True, 12, None, the empty string, the empty list, the empty map), 154 cases
  through the real `load_config`. **R843**, and the measurement that actually closes
  R837's class and so grounds **R842**.
* **A regeneration check on a published deliverable** -- all three R1 artifacts regenerated
  from this tree and diffed over the whole file rather than over a needle. **Found
  nothing**: the only differences are the provenance path prefix of my own run and one
  timing cell. U = 1.71167 reproduces at platform:hub4_arm ROOT. That is what says
  `floatfea/run/config.py` changing did not move a published figure, and it is worth as
  much here as a finding would have been.

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff --stat 62e48af..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 62e48af..HEAD -- floatfea tests scripts | grep "^+" |
       grep -cE "isclose|abs_tol|rel_tol|approx|atol|rtol"
out    0
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a
       tolerance under another name
judge  the diff is one type-guard call at three sites, three test parametrisations, one
       conditional in a fixture and one string escape. The only comparisons it introduces
       are `not isinstance(value, str)` and `isinstance(value, str)`, which carry no
       number. EU1 therefore does not attach; the adversarial case was run anyway.
```

## Closure items (CZ0)

ES0 says an interim check writes no closure list, so this is not one. Two entries are
recorded because they amend items that already exist, and one is new because its content
is a figure of mine:

* **C37 widens.** `_require_string`'s "a name written without quotes ... Quote the name."
  now fires at three PATH fields as well. The noun is wrong for five of its six call sites,
  not one of three. Same item.
* **C27 recurs for a third round** -- see R842. Still a closure item; the code it was about
  is now closed.
* **C41 (new).** The "three of its five siblings" sentence at `floatfea/run/config.py:858`
  and `tests/unit/test_run_config.py:507`. Five of five. **It is my predecessor's figure**
  (`docs/reviews/R1/step-2.md:93`), and the ledger entry should say so.

Everything else carries unchanged: C26, C28, C30, C31, C32, C33, C36, C38, C39, C40.

## Next step opens when

**Step 2 stays open, and NOTHING in this check consumes a round.** Revision 3 of 3 is
intact and is the last one. ES0: a verdict forced at a turn boundary on a tree with no new
report revision counts against none.

1. **R841** -- revision 3's commit carries the regenerated section 8 from the escaping
   generator, and its section 7 traces the nine reds individually with the ninth's cause
   named as the generator change, established by an ablation, rather than filed under the
   EH1 cascade or FC1. Do not revert `_cell`. If a pushed commit intervenes and still
   carries the red, its report states which of the three causes each red has.
2. **FL2's five gate items**, which is what step 2 is for and of which none is built.
3. **R842 and R843** -- not blocking, both one line. R842 is retired by publishing the grid
   instead of the grep; R843 by refusing an empty `directory` at that site alone, or by
   stating that the site was left and why.
4. **R838 and C40** -- unchanged from verdict 7: the regeneration comparison for
   `results/R1/example/` closes R838's three directions at once and retires C40 with it.
5. **The closure list** -- C26, C27, C28, C30, C31, C32, C33, C36, C37, C38, C39, C40, C41
   -- fixed once in the step's closure commit.
6. **`scripts/suite_count.py`'s line and CZ1 (ii)/(iii)'s four outputs**, in the follow-on
   commit, as already ruled twice.
7. **Run the WHOLE suite before invoking me, not a subset.** The eight-file run this commit
   reports (224 passed) is green and true and cannot contain R841. ES0's light scope is the
   suite; a subset chosen by the author of the diff is the same shape as a needle chosen by
   the author of the repair.
8. **The push (FP1), continued.** It gave this round a completed CI run at the judged
   commit, nine reds matching mine id for id, and a green `mypy` and six green ladder rungs
   on a machine neither of us controls.

**ON THE ESCALATION, which is already with Xabier and which I am not re-opening.** The
implementer has relayed it verbatim and I endorse that relay. I add only the measurement
this round contributes, because it sharpens the choice rather than restating it: **the
findings are still cheap and the rounds are still expensive.** R837 was three one-line call
sites and three test rows, all three bound by id; R841 is a question of which commit
carries sixteen lines; R842, R843 and C41 are one line each. Nothing in two rounds has cost
more than an hour of work. What has cost the step is that each round ends and the next
cannot begin until a verdict exists. That is Xabier's trade to make, not mine and not the
implementer's.

**Where I disagree with the CRITERION rather than with the work -- one thing, and I am
saying it once.** FF0 says an apparatus closure item is "fixed in the next commit"; BP0
says a changed rule's figures are regenerated in the same commit; EK3 says a closed report
may not be touched. For a change to a generator whose output is published inside a closed
report revision, those three can be satisfied together only by the commit that writes the
next revision -- and no clause says so, which is why this commit shipped a red that no
state's list covers and that the implementer could not have cleared from where they stood.
I have ruled under CZ0 (d) and EG3(i) as written, and the repair I ask for costs nothing
beyond what revision 3 already owes. **The clause I think is missing is one sentence:** an
FF0-class repair to a generator lands in the commit that next regenerates the artifact it
feeds. It goes to Xabier through the implementer; it is not a round, and it is not a HOLD
on anything but the red itself.

**One housekeeping consequence of my own measurement, declared rather than left to be
found.** The report-guard ablation needed a real worktree, because these guards read git
and a `git archive` copy gives 30 failed at a commit that is 0 failed. `git worktree
remove` then could not delete `.git/worktrees/wt23` on this machine -- Permission denied,
the same failure the previous round recorded -- so the count went from 185 to 187. The
working tree is clean, `git status --porcelain` is empty, no measurement is affected, and
no file outside `docs/reviews/` was written by me.

**What this commit got right, and it is much the larger part.** The one blocking finding
from verdict 7 was answered at the layer the finding was about: the condition asked for one
call site and one row, and the repair took three call sites and three rows, each bound to
its own id by mutation. The class is now closed against a type space rather than a
spelling, which I verified with 154 cases the diff did not choose. The fixture repair was
necessary, was reasoned about in writing, and was offered for attack rather than asserted
safe -- which is why I could answer it with a divergence count instead of an opinion.
R840's escape is correct and reproduces in both directions. `ruff`, `black`, `mypy` and six
ladder rungs are green here and in CI, and the three published deliverables regenerate from
this tree with no engineering number moved.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 2
Reviewed commit: 129747bcec6357b16229b2811b0000d434d954af
**Reviewed commit: `129747bcec6357b16229b2811b0000d434d954af`.**
Verdict: HOLD
**Reviewed commit: `129747bcec6357b16229b2811b0000d434d954af`.** Revision 2 of 3 under ES0.
Tests: 3623 passed, 8 failed, 1 skipped

**THE TEST LINE IS MY OWN RUN THIS TIME.** `python -m pytest -q --tb=no -rf` at the reviewed
commit, tree clean: `8 failed, 3623 passed, 1 skipped, 2 warnings in 1554.92s (0:25:54)`. The
eight `FAILED` ids are identical to the report's Â§7 list and to CI's. The machine that could
not run its own suite last round ran it in twenty-six minutes, so the figure the report owed is
paid and independently reproduced rather than reconciled.

**THE `Answers:` HEADER IS CORRECT (step 1b).** `docs/reports/R1/step-2.md:781` reads
`Answers: verdict 6 @ 43bcd0c`, and `43bcd0c` is the newest verdict commit in `git log`. One
comparison, it holds, no HOLD on that head.

**ALL SIX GUARDS I DIFF SEPARATELY ARE UNTOUCHED, AND THERE IS NO STOP-CLASS FINDING.**
`git diff --stat 43bcd0c..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md` is empty;
`git diff 43bcd0c..HEAD -- tests/conftest.py 'tests/**/conftest.py'` is empty, and
`git ls-files` on that pathspec gives the one file `tests/conftest.py`, as my instructions say
it must; `git diff --stat 43bcd0c..HEAD -- floatfea/tolerances.py` is empty.

**EU1 DOES NOT ATTACH AND THIS IS NOT AN INTERIM CHECK.** No tolerance value and no declared
counter moves in this diff -- measured, not asserted: the diff of `floatfea tests scripts`
grepped for `isclose|abs_tol|rel_tol|approx|atol|rtol` and for any new numeric comparison
returns nothing. A new report revision exists, so this is a reviewed round under ES0 and it is
the second of three.

## Carried

**Verdict 6's four blocking findings: ALL FOUR ANSWERED, AND I VERIFIED EVERY ONE BY MUTATION
RATHER THAN BY READING THE REPORT.** Twelve revert-red-restore cycles of my own, in a
`git archive` copy, against a baseline of **123 passed in 119.85s** on
`tests/unit/test_run_config.py` + `tests/unit/test_run_pipeline_refusals.py` +
`tests/regression/test_r1_published_artifacts.py`.

| item | status | where, measured by me |
|---|---|---|
| R831 (three deliverables stale; the marker needle) | **ANSWERED, and I checked it the strongest way available** | the needle is `floatfea.cli.TABLE_CAVEATS` at `tests/regression/test_r1_published_artifacts.py:75`, 9 x 3 = 27 verbatim cases. Rewording one caveat in `cli.py` with the files left alone gives **3 failed, 120 passed**; restored **123 passed**. And rather than trust the caveats alone I regenerated all three artifacts from this tree and diffed the WHOLE file: `report.md` 2 differing lines, both the config filename my probe used; the CSVs 2 each, the same. **Nothing else in any deliverable is stale.** Closed. Two blind directions recorded as **R838** -- neither is the unmet half of the condition. |
| R832 (the FQ3 empty-basis branch held by nothing) | **ANSWERED, both halves live** | `test_FQ3_R832_an_EMPTY_basis_says_so_AND_no_caveat_contradicts_it` at `tests/unit/test_run_pipeline_refusals.py:604`. Reverting the `if basis:`/`else` hunk to the field-by-field form: **1 failed, 122 passed**, and the one red is that test. The implementer asked whether the narrowed needle is now too narrow to fail -- **it is not**: restoring the pre-R829 caveat wording gives **4 failed**, the three artifact cases plus that same test. The two halves redden under two different mutations, which is what makes them two halves. Closed. |
| R833 (the name-key refusal held at one of three sites) | **ANSWERED AT ALL THREE, bound per site** | the call site is a parameter at `tests/unit/test_run_config.py:375-385`. Removing one `_require_name_keys` line at a time: `sections.groups` **4 failed** on exactly the four `[*-sections.groups]` ids, `mass_distribution` body names **4 failed** on exactly the four `[*-mass_distribution body names]` ids, `line_masses` **4 failed**; restored **15 passed**. Each site's four shapes redden and no other site's do. R825's two named lines are both held. Closed. |
| R834 (`str()` on a declared string) | **ANSWERED AT THREE SITES, AND A FOURTH EXISTS -- R837** | `_require_string` at `floatfea/run/config.py:233`, applied at `:612`, `:701`, `:802`. Reverting each to `str(...)` reddens exactly its own parametrisation -- `[floatsim.tag-tag]`, `[lumped[].label-lumped]`, `[load_cases.window_rule-window_rule]`, one id each, control `4 passed`. **The two extra sites were NOT scope you should not have taken** -- they are the finding, and `tag`/`window_rule` reaching `provenance()` is verified at `config.py:530` and `:560`. The scope was right and it was one site short. **R837.** |
| R835 (EG3's enumeration) | **recorded, carried to Xabier, and I measured it again** | this commit's eight reds give the fifth independent confirmation. See **R839**. |
| R836 (the r754 margin in the wrong variable) | **answered** | Â§7 re-measures it as the round-tripped ratio, `300.0000000000001`, and keeps it as a recorded item rather than a change. That is the right disposition. |
| C29 (FF0 class, overdue) | **DONE in this commit** | `scripts/ci_section.py:185-199`. `python scripts/ci_section.py` exits 0 and reproduces the report's Â§0 **byte-identically**, which I ran. |
| C34, C35 | **done here**, though the pointer file still lists them `later` | `ruff check floatfea tests scripts`, `black --check floatfea tests scripts` (147 files) and `mypy floatfea scripts/f4_dynamic_residual.py` (43 files) are green on my machine in CI's own wider forms, and C35's sentence went with the needle. The pointer-file discrepancy is declared in Â§9 and is correct as a ledger. |
| C26, C27, C28, C30, C31, C32, C33 | carry to the closure commit | not re-reviewed item by item. **C27 recurs in the code -- see R837.** |
| `scripts/suite_count.py`'s own line | **still owed, correctly** | FC1: a line naming a sha cannot be inside that sha. It goes in the follow-on commit with CZ1 (ii)/(iii)'s four outputs, which is where verdict 6 ruled it belongs. Not a finding. |

## Findings

**ONE BLOCKS. It is the fifth consecutive round in which the deciding half is the other
instance of the thing just fixed -- and this round the pattern moved into the NEEDLE that was
used to prove the class closed.**

**R837. (BLOCKS -- CZ0 head a) THE str() COERCION SURVIVES AT A FOURTH DECLARED STRING,
`outputs.directory`, AND IT IS THE FIELD THE THREE PUBLISHED DELIVERABLES ARE WRITTEN TO.
Every other key in the same function refuses by type four lines below it. And section 5's
command cannot reach it, which is C27 one round later in the same shape.**

```
claim  outputs.directory is a declared string that coerces rather than refuses, and the
       three EZ0 artifacts land in a directory named after the coerced value
cmd    every declared string field in the schema offered a bare YAML word, through the real
       load_config, on a fresh `git archive HEAD` copy of the shipped example
out    floatsim.tag = False          REFUSED : floatsim.tag: False (bool) is not a string...
       floatsim.tag = 2024           REFUSED : floatsim.tag: 2024 (int) is not a string...
       load_cases.window_rule = 1    REFUSED : load_cases.window_rule: 1 (int) is not a...
       floatsim.deck = False         REFUSED : ...False does not exist. The deck is...
       load_cases.npz = False        REFUSED : ...does not exist...
       outputs.directory = False     LOADED  : outdir=WindowsPath('.../examples/False')
       outputs.directory = 12        LOADED  : outdir=WindowsPath('.../examples/12')
       outputs.directory = None      LOADED  : dir='None'
       CONTROL: untouched            LOADED  : dir='example'
cmd    floatfea/run/config.py:852, and the nine lines after it
out    852:  directory = Path(str(block.get("directory", "results/run")))
       856:  for name in known[1:]:
       858:      if not isinstance(value, bool):
       859:          raise ConfigError(f"{where}.{name}: expected true or false, got ...")
cmd    where those three artifacts are written
out    floatfea/cli.py:343  out = cfg.outputs.directory
       :345 / :348 / :351   out / "member_forces.csv" | "utilisation.csv" | "report.md"
       and _write_member_forces does path.parent.mkdir(parents=True, exist_ok=True)
rule   _require_string's own docstring, written in THIS commit at
       floatfea/run/config.py:233 -- "A declared NAME or provenance string IS a string, or
       it is refused"; and CLAUDE.md, "Never let a validation failure degrade to a warning.
       The reader rejects bad records"
judge  **the asymmetry is inside one function and visible in nine consecutive lines.**
       known[1:] skips `directory` deliberately, so the five booleans beside it are refused
       by name -- `outputs.report: expected true or false, got 'no'`, which I measured -- and
       the one declared STRING in the block is coerced. `directory: no` is the exact typo the
       block invites, because three of its five siblings ARE booleans in the shipped example;
       the reader gets the three published deliverables in a directory literally named
       `False` instead of a refusal. This is verdict 6's R834 one field across, under the
       reasoning verdict 6 itself gave: the loader's guarantee is false for a measured class
       of its own declared input. **Milder than the label case** -- no number moves, and the
       CLI prints the path it wrote -- and CZ0's heads are about WHERE, not about severity.
```

```
claim  section 5's refutation command cannot refute section 5's claim, which is C27's defect
cmd    docs/reports/R1/step-2.md:1002-1008
out    claim  three declared string fields coerced, and the command that reaches all three
       cmd    grep -nE "=\s*str\(" floatfea/run/config.py        (before this revision)
       cmd    the same command, now
       out    (no output)
cmd    the command that does reach the fourth site
out    grep -nE "Path\(str\(" floatfea/run/config.py
       600:    deck = Path(str(_require(block, "deck", where)))
       762:    npz = Path(str(npz_raw))
       852:    directory = Path(str(block.get("directory", "results/run")))
rule   BF0, and verdict 6's C27 verbatim -- "the needle is the two spellings the same commit
       deleted, so it searches for its own repair and reports success"
judge  the needle requires str( immediately after the `=`, so it sees three keyword arguments
       and cannot see a str( nested one call in. `(no output)` is then published as evidence
       that the class is closed. **C27 was ruled a closure item last round and the identical
       needle shipped again one round later** -- which is the argument for blocking on the
       code rather than only ledgering the sentence. `deck` and `npz` are the same spelling
       and happen to refuse, via an existence check rather than a type check; `directory` has
       no existence check because it is created.
```

**Closed when** `outputs.directory` refuses a non-string -- _require_string already exists and
already takes a scalar -- with one row on the existing
`test_FQ2_R834_a_DECLARED_STRING_FIELD_refuses_a_non_string` parametrisation that reddens when
that one call site is reverted, pasted per call site as verdict 6 required. **Or** the report
states that the site was deliberately left and why, with the command that reaches it. And the
census is published as a command that finds a str( at any nesting depth, not as the spelling
the repair used.

**R838. (DOES NOT BLOCK -- recorded) R831's NEEDLE IS SOLVED IN ONE DIRECTION. The gate asserts
that the code's text is a subset of the file's, not that the two agree: a caveat DELETED from
cli.py leaves the retired sentence in all three deliverables with nothing red, which is R831's
own species. And the one non-caveat header line in the same block, LABEL, is asserted against
the F6 deliverable and not against these three.**

```
claim  the artifact gate's boundary, solved in BOTH directions (EH4)
cell   one element of TABLE_CAVEATS changed at a time in a `git archive HEAD` copy; the
       deliverables never regenerated; tests/regression/test_r1_published_artifacts.py +
       test_f6_deliverable_agrees_with_itself.py, baseline 62 passed
out    a caveat REWORDED            (the direction built for)   3 failed, 59 passed
       a caveat ADDED to the code                               3 failed, 62 passed
       a caveat DELETED from the code   (WEAKENS)               59 passed, 0 failed
       a COMMA in a caveat becomes a SEMICOLON   (WEAKENS)      62 passed, 0 failed
       CONTROL: a WORD in the same caveat changes               3 failed, 59 passed
       LABEL reworded in cli.py, files left alone              123 passed, 0 failed
       restored                                                 62 passed
rule   EH4 -- the ceiling falls toward the clean value and the injection rises until a clean
       case trips; and my own recorded guard, check that the collection the assertion
       inspects can contain the failure
judge  **the two green rows are the two that weaken the gate, and nobody swept either.** A
       deleted caveat is exactly what R831 was -- a published sentence the code has retired --
       and the new needle cannot see it, because the assertion quantifies over what the code
       still says. The comma row is _normalised's own blind spot and is narrow (punctuation
       only); the control one position away reddens, so the gate is live there. LABEL is
       asserted at tests/regression/test_f6_deliverable_agrees_with_itself.py:191 for
       results/F6/ and nowhere for results/R1/example/, which is the asymmetry verdict 6's
       R831 already named. **I am not blocking on it:** the gate's own claim is
       one-directional and honestly stated, verdict 6's closing condition is met in full, and
       my whole-file regeneration diff says no deliverable is stale in ANY direction today.
       The repair is one command and it closes all three directions at once.
```

**Would close it** -- a regeneration comparison for results/R1/example/, the shape
test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree already has for results/F6/:
run, write to a temp directory, compare the header blocks line for line with the timing table
excluded. Not new apparatus, and test_r1_example_golden.py already pays the run. It reddens on a
reword, a deletion, an addition and a LABEL change alike.

**R839. (DOES NOT BLOCK -- recorded; it is R835's fifth measurement) ALL EIGHT REDS AT THIS
COMMIT HAVE ONE CAUSE, AND IT IS FC1's. The report files seven of them as the EH1 cascade and
one as FC1, as two causes. Traced individually per EG3(i), the seven cascade off the same
missing suite_count.py line as the eighth -- and NEITHER boundary state's own named member
fired.**

```
claim  each of the eight, traced by running the id on its own rather than by family
cmd    each of the 8 FAILED ids, one pytest invocation each
out    test_the_report_carries_a_WHOLE_SUITE_count
         "the newest revision carries no whole-suite line ... Generate it with
          python scripts/suite_count.py"                       -> FC1, commit-dependent
       test_the_guard_survives_the_state[baseline] and the six others
         inner run, all seven identical:
           FAILED tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count
           1 failed, 247 passed, 1 skipped
         then  assert 1 == 0
cmd    test_the_guard_reads_the_step_being_worked_on, on its own
out    PASSED      -- state (1)'s own named baseline did not fire
cmd    the verdict-exists control, in a real WORKTREE at bd315a1, both report-guard files
out    149 passed in 205.35s        -- 0 failed
cmd    the same control as a git archive copy instead of a worktree
out    30 failed, 124 passed        -- these guards read git log; an archive has no .git
rule   EG3(i) -- each FAILED id matched to the state's own list, not "the failures look like
       the boundary set"; EH1 -- the cascade is identified by the baseline being red and by
       each cascading state's own failure line, not by its name; FC1 -- neither of the two
       can pass in the commit it describes
judge  **the report's claim is TRUE and its attribution of cause is one cause too many.** All
       eight are the single commit-dependent cause FC1 names, every one absent at a commit
       where the line exists, so not one is CZ1 (iv) and the step-boundary waiver applies in
       full. The cascade is correctly identified by EH1's rule; what section 7 does not say is
       what [baseline] is red ABOUT. **This is the fifth independent demonstration that the
       enumeration cannot be reasoned with and the rule can:** here the list would have had a
       reviewer looking for a verdict-dependent red that is green, and filing seven
       commit-dependent reds under a verdict-dependent heading. **And the control has a trap
       of its own that no directive records:** git archive gives 30 failed at the very commit
       CLAUDE.md cites as 0 failed, because the guards read git. A control for a git-reading
       guard is a worktree or it is nothing. I endorse R835's proposal unchanged; it is
       Xabier's, not a round's.
```

**R840. (DOES NOT BLOCK -- FF0-class gating apparatus, fixed in the next commit, NOT ledgered)
scripts/carried_table.py DOES NOT ESCAPE THE CELL SEPARATOR, SO FOUR OF THE FIFTEEN ROWS --
the ones whose subject was lifted from a verdict's own TABLE -- RENDER WITH EXTRA CELLS IN A
THREE-COLUMN TABLE.**

```
claim  the report's section 8 is exactly what the generator emits, and the generator emits
       broken markdown rows
cmd    python scripts/carried_table.py docs/reviews/R1/step-2.md
              docs/reports/R1/step-2-answers.json    -- compared with the report's section 8
out    15 rows, byte-identical to the report's. Rows whose cell count is not 3:
         4 ['R819', 'R825', 'R826', 'R828']
       each of those four ends in a truncated fragment of my own Carried table rather than
       in a subject
rule   FF0 with EK2 -- anything that reads the gating record is fixed in the next commit, and
       a guard that fails false is fixed or deleted, never extended
judge  my Carried section is a table, so its cells contain the separator character, and the
       generator pastes them raw into a cell of its own table. The implementer did not write
       these rows and could not have fixed them by writing differently. Nothing green is made
       to mean the wrong thing, so it is not blocking; it is in the class FF0 says is not
       ledgered. One escape on the subject cell.
```

**One housekeeping note, not a finding against this commit.** `git worktree list` carries
eleven live suite-count registrations under TEMP, and `ls .git/worktrees | wc -l` is **185**
stale entries that `git worktree prune` cannot delete on this machine. scripts/suite_count.py creates
one per invocation. The working tree is clean and nothing is wrong with any measurement; it is
state accumulating in .git/ that a later reader will have to reason about.

## The three things the report asked to have attacked -- my rulings

**1. R831's NEEDLE AND ITS PARAMETRISATION ARE RIGHT, AND 9 x 3 IS THE RIGHT COUNT.** The
EX3/R724 and R741/R742 caveats each name two findings and are each ONE element of
TABLE_CAVEATS, so one case per element is one case per published sentence -- which is the
object that can go stale. The eleven-marker list was the thing that was wrong about the count,
not the nine. The normalisation does not let a rewording through: a word changed one position
from the comma reddens three cases. It lets a comma/semicolon substitution through, which is
R838's narrow half. **And the hole I went looking for is not there:** deriving the
parametrisation from len(TABLE_CAVEATS) looked like the "empty parameter set reads green"
defect, and pyproject.toml:81 carries `empty_parameter_set_mark = "fail_at_collect"`, so
emptying the tuple gives `1 error in 0.98s` and not a green skip. That is the second argument
this round I converted to a measurement and lost.

**2. THE CONTENDED WALL CLOCK: a closure item, and the reason is not indulgence.** I ran the
same configuration a third time while my own suite and twelve mutation cycles held the machine
and got `total wall time 126.26 s` against the published 97.27 and revision 1's 65.97. So the
published figure is not reproducible within a factor of two, and that is a property of the
quantity rather than of this run. It is nonetheless TRUE of the run that produced the artifact,
no engineering number moved -- my whole-file regeneration diff puts every other line identical
-- and CZ0 retires the truth of a published figure as a blocking head. **What is actually wrong
is where the mitigation lives:** section 2 says it was taken under load, and section 2 is a step
report, which is not what goes to Xabier. The deliverable itself says nothing. Closure item
**C36**, and the fix is a generated line beside the table rather than a decision to stop
publishing it -- FL1(d) asks for the wall time, and a withheld figure is worse than a noisy one
carrying its operating point.

**3. R832's NARROWED NEEDLE IS NOT TOO NARROW.** Measured, not argued: restoring the pre-R829
caveat text reddens that test. The first version reddening on cli.py:77's C_m caveat was the
right thing to notice and the right repair -- a gate that reddens on a true sentence about
another quantity is a gate that will be widened by whoever next trips it.

## Try to break it -- the adversarial cases I ran, and what they found

* **Every declared string field in the schema, offered False, an int and None, through the real
  load_config** -- the type space rather than the three fields the diff chose. **R837**, and it
  is the round's only blocking finding.
* **Every declared BOOLEAN in the same block, offered 'no', 0 and 'false'.** All five refuse by
  name. Found nothing, and it is what makes R837 an asymmetry inside one function rather than a
  missing feature of the schema.
* **A whole-file regeneration of all three published deliverables, diffed line for line against
  the committed files.** The strongest form of the check that found R831 last round.
  **Found nothing** -- two lines per file, all of them the config filename my own probe used.
  That is the measurement that closes R831, rather than the caveat gate's 27 green cases.
* **The artifact gate's boundary in BOTH directions** -- reworded, added, deleted, and a comma
  turned into a semicolon, with a word-level control at the same position. **R838**: the two
  weakening directions are the two that are green.
* **Twelve revert-red-restore cycles, one per call site**, against a 123-passed baseline: three
  _require_name_keys sites, three _require_string sites, the `if basis:` branch, the retired
  caveat, a reworded caveat, LABEL, and the emptied tuple. **Every repair in this commit is
  held, and bound to its own site** -- I confirmed the binding by id, not by count.
* **The eight reds traced one id at a time instead of as a family.** **R839** -- one cause, not
  two, and neither state's named member fired.
* **The verdict-exists control run two ways**, archive and worktree: 30 failed against 0 failed
  at the same commit. The control CLAUDE.md prescribes is only valid as a worktree.
* **python scripts/ci_section.py re-run and diffed against the committed section 0.**
  Byte-identical. C29's hint fires in both refusal paths and does not fire on a correct marker.
* **The emptied-tuple probe**, looking for a parametrisation that reads green over nothing.
  Lost: fail_at_collect is configured.

**What I did not find, and it is the larger part.** The reviewer's question was adopted as a
method and it worked: the call site is a parameter in three separate gates now, every repair in
this commit reddens when it is reverted, and the two sites nobody asked for were the right two.
R831's repair went further than its condition -- the needle, the regeneration taken after the
last edit, and the false docstring sentence deleted in the same commit. R832's needle was
narrowed for a stated reason and the narrowing was then measured rather than assumed. The
whole-suite figure that was owed was paid, from the implementer's own machine, matching mine to
the test. **The one blocking finding is the fourth instance of a three-instance repair, found by
the type space and not by the diff -- and the needle that certified the class closed is the same
needle verdict 6 named as C27.**

## CI at the reviewed commit: RED, eight reds, all one boundary cause, and it does not HOLD

```
cmd    gh run list --commit 129747bcec6357b16229b2811b0000d434d954af
         --json name,conclusion,workflowName,status
out    [{"conclusion":"failure","name":"CI","status":"completed","workflowName":"CI"}]
       -- it was in_progress when I began and completed while I measured; a run that has not
          finished is not a pass, so this is read only after completion
cmd    gh run view 39053434877 --json jobs, read at STEP level
out    lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS / guards and meta-tests FAILURE
         -> 8 failed, 1148 passed, 1 skipped in 648.51s
       the verification ladder : SUCCESS
         rungs 1, 2, 3, 6+regression, 4, 5 -- all six SUCCESS
       CI determinism -- leg / ten legs agree : SKIPPED
cmd    gh run view 39053434877 --log-failed, the eight FAILED ids
out    identical to my own local eight, and to the report's section 7 list
```

**Not CK2's exhausted-allowance state.** Both real jobs ran with per-step conclusions and real
counts -- ten minutes on the guards step alone -- so the absent runner name is not the
never-started signal CK2 describes. The two determinism jobs are skipped by the workflow's own
event gate (CK0 by design) and are recorded as that, not as an unavailable check.

**On CA2, which I keep in full because CLAUDE.md does not carry it:** a red CI is a HOLD
regardless of the local run, and EG3 is the clause that qualifies CZ0's head (d) for a step's
own boundary red. Every one of the eight traces by name to FC1's cause, individually and not by
family, and every one is green at a verdict-exists worktree control. So the red is recorded as
red with its cause named and **CI does not HOLD on head (d)**. What would HOLD is a ninth, and
there is none. mypy -- which was CI-only red at 60f3176 -- is green here, and the `unit tests`
and `guards and meta-tests` steps both RAN rather than being skipped behind an earlier red,
which is the thing CZ1 (iii) exists to see.

**EG3(ii): I measure state (1) clearing at my own verdict commit and the counts go in the next
revision's Carried.** My instructions have me run before writing, so it is measured after this
file exists.

## Corpus (EG4(e))

**The pause held. Zero new entries this round, tests/corpus/ is untouched by me, and
`git status --porcelain` is empty.** Neither exception opens: this revision touches no part of
F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
tests/verification/rung4/, not about the declared config strings this revision refuses -- the
same check verdict 6 made, re-made here because R837 is again a declared-identifier finding.

**I ran the recorded substitute instead, both halves, and this round only one of them produced
the blocking finding** -- which is the honest count, and the first time in five rounds they have
not both paid:

* **a continuum grid over the parameter space a decision rule guards** -- every declared string
  field and every declared boolean in the schema, offered False / int / None / 'no' / 0 /
  'false' through the real load_config; and the artifact gate's text boundary in four
  directions with a control at each. **R837 and R838.**
* **a regeneration check on a published deliverable** -- all three artifacts regenerated from
  this tree and diffed over the whole file rather than over the needle. **Found nothing**,
  which is what closes R831 and is worth as much here as a finding would have been: it is the
  only measurement in this round that says the deliverables are clean in every direction,
  including the two R838 shows no gate covers.

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff --stat 43bcd0c..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 43bcd0c..HEAD -- floatfea tests scripts | grep "^+" | grep -E
       "isclose|abs_tol|rel_tol|approx|atol|rtol|[<>]=? *[0-9]"
out    (no output)
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name
judge  the diff is one type guard, three call sites, three test parametrisations, a generated
       deliverable regeneration and one refusal message. The only new comparison anywhere in
       it is `not isinstance(value, str)`, which is a type test and carries no number.
```

## Closure items (CZ0, fixed once in the step's closure commit)

C26, C27, C28, C30, C31, C32 and C33 carry unchanged from verdict 6 and are not re-reviewed
item by item. C29 is done; C34 and C35 are done. R840 is FF0-class and is fixed in the next
commit rather than ledgered. New:

* **C36.** results/R1/example/report.md's timing table publishes a contended wall clock with no
  operating point in the artifact. Measured three times on three machine states: 65.97, 97.27
  and 126.26 s total. The mitigation is in the step report, which is not what goes to Xabier.
  A generated line beside the table, not a withdrawal of the figure.
* **C37.** _require_string's message says "a name written without quotes ... Quote the name."
  and it now fires for load_cases.window_rule, which is a sentence rather than a name. The
  refusal is right; the noun is wrong for one of its three call sites.
* **C38.** docs/reports/R1/step-2.md:1002-1008 -- the claim is "three declared string fields
  coerced" and the command is the spelling the repair used. The sentence is the prose half of
  R837 and is C27 recurring; it is ledgered here and the code is what blocks.
* **C39.** docs/reports/R1/step-2.md:1086-1101 attributes the seven cascading reds to the EH1
  cascade and the eighth to FC1, as two causes. R839's trace says there is one. The
  classification of the cascade is correct; the cause behind [baseline] is not stated.
* **C40.** tests/regression/test_r1_published_artifacts.py:16 -- the module docstring now says
  "What is checked here is the published FORM", which is broader than the file checks: LABEL,
  the provenance block and the wave-basis line are published form and are not asserted against
  these three artifacts. R838 is the measurement. CW0.

## Next step opens when

**Step 2 stays open. Revision 2 of 3 is spent; ONE reviewed revision remains, and none of step
2's own gate is built.** Section 9 says so correctly, and verdict 6 ruled that is not a finding
for a revision answering findings. It is a schedule fact, and after this round it is the
schedule fact that matters most.

**THE ESCALATION CLAUSE IS NOW LIVE AND I AM STATING IT RATHER THAN LETTING IT BE INFERRED.**
Step 1 closed at the ES0 cap carrying five blocking items. Step 2 has spent two of its three
revisions on findings, has FL2's five gate items entirely unbuilt, and carries one blocking item
out of this round. If revision 3 does not carry both R837 and FL2's five items, step 2 closes at
the cap with blocking items and that is **two consecutive steps**, which CLAUDE.md says is
escalated with the choice stated: **slip the 5 November date, or reduce FL2's scope.** I endorse
neither -- FQ4 forbids the implementer trimming scope, and the date is Xabier's judgement rather
than mine. What I will say is that the findings per round are not what is slowing this step
down: each has been one line of code or one test row, and all twelve of the repairs I cycled
this round held. The cost is the round, not the repair.

1. **R837** -- outputs.directory refuses a non-string, with one row on the existing R834
   parametrisation reddening when that one call site is reverted, pasted per call site. Or the
   report states the site was deliberately left, with the command that reaches it. And the
   census published as a needle that finds str( at any nesting depth.
2. **R838 and R840** -- not blocking, and both are one line. If revision 3 has room, the
   regeneration comparison for results/R1/example/ closes R838's three directions at once and
   retires C40 with it; carried_table.py's separator escape is FF0-class and is due in the next
   commit regardless.
3. **FL2's five gate items**, which is what step 2 is for.
4. **The closure list** -- C26, C27, C28, C30, C31, C32, C33, C36, C37, C38, C39, C40 -- fixed
   once in the step's closure commit.
5. **scripts/suite_count.py's line and CZ1 (ii)/(iii)'s four outputs**, in the follow-on commit,
   as already ruled.
6. **The push (FP1), continued exactly as done here.** It gave this round a completed CI run at
   the judged commit, eight reds that match mine id for id, a green mypy on a machine neither of
   us controls, and six green ladder rungs. It is not an open item and must not become one.

**Where I disagree with the CRITERION rather than with the work: nothing new.** R835 stands as
verdict 6 wrote it, the implementer is right to carry it to Xabier rather than act on it, and
R839 is its fifth measurement rather than a second proposal.

**What this commit got right, and it is much the larger part.** Four blocking findings answered,
and every one of them answered at the layer the finding was about rather than at the layer the
repair was first written: the call site became a parameter in three separate gates, each bound
to its own site, which I verified by id. The needle that could not fail was replaced by one that
can, and the sentence claiming otherwise was deleted in the same commit instead of being
ledgered. A first attempt at the R832 gate reddened on a true sentence about another quantity,
and that was recorded as the mirror of R831 rather than quietly narrowed. Two sites nobody asked
for were found by asking the right question, and both were real. The deliverables were
regenerated after the last edit to the code they publish, and I verified that over the whole
file and not over the caveats. The whole-suite figure that was owed, on a machine that could not
produce it last round, was produced and matches mine to the test.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 2
Reviewed commit: 09d5bc9acc3d9eea0a77a21b3e2bf8943ae8f50e
**Reviewed commit: `09d5bc9acc3d9eea0a77a21b3e2bf8943ae8f50e`.**
Verdict: HOLD
**Reviewed commit: `09d5bc9acc3d9eea0a77a21b3e2bf8943ae8f50e`.** Revision 1 of 3 under ES0.
Tests: 3768 passed, 9 failed, 1 skipped

**THE TEST LINE IS CI's AT THE REVIEWED COMMIT, NOT MINE, AND I SAY SO RATHER THAN PRESENTING
IT AS A LOCAL RUN.** My own `python -m pytest -q` reached `[ 7%]` in 100 minutes against the
eight production `tilted_dynamics.py` processes, and I stopped mine rather than theirs -- the
implementer's own measurement, reproduced. What I did instead is below; the whole-suite figure
comes from the one machine neither of us controls.

```
claim  the whole tree was measured at the reviewed commit, across the three pytest
       invocations whose union IS the tree
cmd    gh run view 39044715217 --log, per step; .github/workflows/ci.yml:402-414, 503-514
out    unit tests                        pytest tests/unit                    163 passed
       the verification ladder, 6 rungs  rung1 1276 / rung2 216 / rung3 314 /
                                         rung6+regression 343 / rung4 66 / rung5 87
                                         collected, 0 failed, 0 errored, 0 skipped each
       guards and meta-tests             pytest tests --ignore=tests/unit
                                           --ignore=tests/verification
                                           --ignore=tests/regression
                                         9 failed, 1303 passed, 1 skipped in 465.75s
       total                             3768 passed, 9 failed, 1 skipped
rule   CA2, and my instructions' "run it yourself" -- which I could not, and the substitute
       is named as a substitute
judge  163 + 2302 + 1303 + 9 + 1 = 3778, and the implementer's last complete local run was
       3756 passed / 21 failed / 1 skipped = 3778. The two environments collect the same
       tree. **No STOP on the missing whole-suite line** -- FC1 already says the line cannot
       be in the commit it describes, and a measurement AT the commit exists; what is absent
       is the report's copy of it.
```

**MY OWN RUNS, named as subsets and not as the suite.** `tests/unit` + `tests/verification/rung5`
+ `tests/regression/test_r1_published_artifacts.py` = **298 passed in 496.43s**.
`tests/regression/test_f6_deliverable_agrees_with_itself.py` = **20 passed in 192.09s**.
`tests/verification/rung5` = **87 passed**. A `git archive HEAD` mutation copy baseline
(`rung5` + `test_run_config.py` + the artifact regression) = **171 passed**, and that baseline
is what the eleven cells below are measured against. `ruff check floatfea tests scripts`,
`black --check floatfea tests scripts` (147 files) and `mypy floatfea scripts/f4_dynamic_residual.py`
(43 files) are green on this machine at CI's own wider forms, not only the report's narrower ones.

**THE `Answers:` HEADER IS CORRECT (step 1b).** `docs/reports/R1/step-2.md:5` reads
`Answers: verdict 5 @ a777cc3`, and `a777cc3` is the newest verdict commit in `git log`. One
comparison, it holds, no HOLD on that head.

**FIVE OF THE SIX GUARDS I DIFF SEPARATELY ARE UNTOUCHED, AND THERE IS NO STOP-CLASS FINDING.**
`git diff --stat a777cc3..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md` is empty;
`git diff a777cc3..HEAD -- tests/conftest.py 'tests/**/conftest.py'` is empty and
`git ls-files` on that pathspec gives the one file `tests/conftest.py`, as my instructions say
it must. `floatfea/tolerances.py` moves by three comment lines and no value -- detailed under
`## Tolerances touched`.

**EU1 attaches and I ran its case.** A threshold's VALUE moved -- `300000.0` read as `/F_y`
became a flat `300.0` -- so the adversarial case is required rather than optional, and I ran it
at configurations the diff did not choose: four grades x five public entry points x six `D/t`,
the ceiling moved in BOTH directions including by one ULP, the two clauses decoupled, and a
29501-point round-trip sweep. Results under `## Try to break it`.

## Carried

**Verdict 5's four blocking findings: all four ANSWERED IN THE CODE. Two of the four are held
by nothing, and that is the whole of this verdict.** C22 is done. R829 and R830 are answered,
R830 completely.

| item | status | where, measured |
|---|---|---|
| R825 (the `str()` collapse one layer down) | **answered in the code; HELD AT ONE OF THREE SITES** | `_require_name_keys` refuses `bool`, `int` and `None` keys at `line_masses`, `sections.groups` and `mass_distribution`'s body names -- I ran all five through the real `load_config` and the string control still loads. **Removing the `sections.groups` call site gives `171 passed`; removing the body-name call site gives `171 passed`.** Verdict 5's condition named BOTH `:611` and `:661`. **R833.** And a fourth declared name still coerces -- **R834.** |
| R826 (nothing holds the R822/R823 repair) | **answered** | `test_FQ2_R822_YAML_TYPING_collapses_are_REFUSED` is five cases over the five productions, the text-identical control still names its key and line, the clean nested document still loads, and the merge refusal has its own case. I removed the count check's call site: `4 failed, 167 passed`. The condition verdict 3 wrote -- "at least one case whose two keys differ in TEXT and agree after construction" -- is met four times over. |
| R827 / R819 (the ceiling) | **answered, and more completely than FQ0 asked** | the constant, both message sites, the `section_class` docstring's number, the caveat in all three artifacts, the gate's needle, and a third entry point the directive's own gate did not drive. Eleven new rung-5 cases. My own four-grade table is below. **One open half: the sentence at `api_wsd.py:233` attributes a refusal to the function that does not refuse** -- closure item C26. |
| R828 (the reddening half holds a frozen file) | **answered** | asserted on `exported_wave_basis` and on `provenance()` themselves. I confirmed the CSV-header check could not have served: it builds `expected_keys` from `provenance()`. |
| R829 (the CSV caveat and the fallback) | **answered in the code; HELD BY NOTHING; and the deliverable does not carry it** | **R831 and R832.** |
| R830 (the numerical stack unpinned) | **answered, and the open half is closed** | `numpy==2.5.4`, `scipy==1.18.1`, `h5py==3.16.0` in the one file. My interpreter now reads `numpy 2.5.4 scipy 1.18.1` -- the set CI resolved at run `38927091674` -- so the two sides agree package by package for the first time. The golden movement was reported and not re-baselined, which is FQ3 obeyed; I verified the cell myself and it holds (below). |
| **C22** (FF0 class, overdue by one commit) | **DONE, and the measurement is unambiguous** | the marker reads `2`, `scripts/ci_section.py` emits, and the report's Â§0 carries the generated table. At `cfb76ff` thirteen reds; at `09d5bc9` **nine**, and the five that cleared are exactly the C22 family -- `test_the_report_carries_a_CI_SECTION`, `test_the_reported_CI_counts_are_not_all_zero`, `test_the_CI_section_is_about_the_REVIEWED_commit`, `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`, `test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph`. |
| C20, C21, C23, and the earlier C-items | carry unchanged | not re-reviewed item by item; the closure list below adds to them. |

## Findings

**Four block. Two are recorded and named. Every one of the four came from running something
the diff did not choose, and three of them are the same shape the last four rounds have each
named once: the repair is correct about the instance it was aimed at.**

**R831. (BLOCKS -- CZ0 head a, EZ0) ALL THREE PUBLISHED ARTIFACTS UNDER `results/R1/example/`
ARE STALE AGAINST THE CODE AT THIS COMMIT, ON THE EXACT CAVEAT FQ3 ORDERED REPAIRED. They
were regenerated in this commit -- and regenerated BEFORE the `cli.py` edit, which is the CP3
ordering error Â§7 confesses for the F6 deliverable, a second time in the same commit and
undeclared. The gate that should see it keys on MARKERS, so all 33 of its cases are green.**

```
claim  the caveat the code produces and the caveat the deliverables publish are different
       sentences, and the difference is the R829 repair
cmd    for each artifact, every element of floatfea.cli.TABLE_CAVEATS matched against the
       file's own text, comma-normalised for the CSV writer
out    results/R1/example/report.md          caveats: 9  NOT PRESENT verbatim: [4]
       results/R1/example/member_forces.csv  caveats: 9  NOT PRESENT verbatim: [4]
       results/R1/example/utilisation.csv    caveats: 9  NOT PRESENT verbatim: [4]
cmd    grep -c for each wording, in the code and in the three files
out                                            NEW wording   OLD wording
       floatfea/cli.py                              1             0
       results/R1/example/report.md                 0             1
       results/R1/example/member_forces.csv         0             1
       results/R1/example/utilisation.csv           0             1
rule   `floatfea/cli.py:60-62`, this commit's own diff -- TABLE_CAVEATS[4] became "EX3 /
       R724: where a run covers a SINGLE heading ... The heading itself is in the wave-basis
       line above WHEN THE EXPORT RECORDED ONE; that line says so either way."
       `cli.py:140` and `cli.py:265` are the only two places a caveat reaches a file.
judge  **the three deliverables publish the pre-repair sentence** -- "the heading these loads
       were exported at is in the provenance above" -- which is the sentence R829 named as
       false whenever the fallback fires and which FQ3 ordered repaired. The repair is in
       `floatfea/` and it is not in the deliverable. And the artifacts WERE regenerated here:
       the `R741 / R742 / FQ0` caveat moved and `report.md`'s timing table moved `66.49 ->
       65.85`, which only a re-run produces. So the regeneration happened between the two
       `cli.py` edits of this one commit. Â§7 states this ordering error for
       `results/F6/floatfea_results_report.md` and calls it "CP3's ordering, and I got it
       wrong the first time"; it happened twice and the second instance is not declared.
```

```
claim  nothing in the tree can see it, and the gate's own docstring claims it can
cmd    python -m pytest -q tests/regression/test_r1_published_artifacts.py
out    47 passed            -- including all 33 (file, marker) cases
cmd    tests/regression/test_r1_published_artifacts.py:33-36
out    CAVEAT_MARKERS = ("R739", "R740", "FA3", "EZ2", "EX3", "R724", "FA0", "FA1", "R741",
                         "R742", "R743")
cmd    tests/regression/test_r1_published_artifacts.py:14-18
out    "**THE ARTIFACTS ARE COMMITTED, SO THIS READS THEM RATHER THAN REGENERATING THEM.**
        ... reading the committed files also catches a regeneration that was never
        committed -- which a test that regenerates cannot."
rule   CW0, and my own recorded guard -- check that the collection the assertion inspects
       can actually contain the failure
judge  the gate asserts that the MARKER `EX3` appears. `EX3` appears in the stale sentence
       too, so the published text may drift arbitrarily from `TABLE_CAVEATS` with 33 of 33
       cases green. **The docstring's claim is the exact claim the measurement above
       refutes**, and `results/F6/` has the gate this needs
       (`test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`, which caught the
       limit moving and which I ran myself) while `results/R1/example/` has none. This is
       R828 one round later, on the other deliverable.
```

**Closed when** the three artifacts are regenerated at the answering commit with the paste taken
after the last edit to the code they publish (CP3), and one existing gate's needle is the caveat
TEXT rather than its marker -- changing `test_every_caveat_reaches_EVERY_published_artifact`'s
parametrisation from `CAVEAT_MARKERS` to `floatfea.cli.TABLE_CAVEATS` is a needle change to a
gate that already exists, exactly as R827's `300000/Fy` needle was, and it is not new apparatus.
A case that reddens when one caveat is reworded in `cli.py` and the files are not regenerated is
the counter.

**R832. (BLOCKS -- CZ0 head c) THE R829 / FQ3 EMPTY-BASIS BRANCH IS HELD BY NOTHING. The branch
FQ3 named in its own words can be reverted to the contradictory field-by-field fallback with the
measuring half of the suite green, at the identical count. Â§4 pastes a revert-red-restore cycle
for eight repairs and not for this one, and Â§8's table records R829 as answered.**

```
claim  the repair FQ3 required is detected by no test in this repository
cmd    git archive HEAD into the scratchpad; in the copy replace the `if basis:` / `else`
       hunk at floatfea/cli.py:111-137 with the old `.get(..., "(not recorded)")` form --
       ONE hunk, nothing else touched -- then run the files that exercise `_header_lines`
       and the published artifacts
out    reverted  -> 113 passed in 502.27s
       restored  -> 113 passed in 514.16s       (tests/unit/test_run_pipeline_refusals.py
                                                 tests/regression/test_r1_published_artifacts.py
                                                 tests/unit/test_run_config.py)
cmd    git grep -ln "NOT RECORDED by the export" -- tests
out    (nothing)
rule   FQ3 -- "an empty-basis branch in the CSV path (no contradictory sentences)"; and
       verdict 5's R829, whose subject is the pair of sentences that cannot both be true
judge  **the branch is correct and nothing holds it.** `tests/unit/test_run_pipeline_refusals.py:585-600`
       drives `_header_lines` on a RunResult whose basis is the real sidecar's, so it
       exercises the `if` and never the `else`. The three new FQ2 cases are the right shape --
       at the generator, not at the file -- and the branch this commit added is the one they
       do not reach. **This is R826's own finding, one round later, inside a repair made to
       answer it**: five repairs were cycled because a directive named five, and the sixth
       repair in the same commit was not.
```

**Closed when** one case builds a `RunResult` with `wave_basis={}`, passes it through
`_header_lines`, and asserts both halves -- that the line says the basis was NOT RECORDED, and
that no caveat in the same output asserts the heading is in the provenance -- reddening when the
branch is reverted. `:585-600` already builds the stub and already calls `_header_lines`, so this
is one more parametrisation on an existing test, not new apparatus. State the cycle.

**R833. (BLOCKS -- CZ0 head c) THE NAME-KEY REFUSAL IS HELD AT ONE OF ITS THREE CALL SITES, AND
THE ONE IT IS HELD AT IS THE ONE Â§4's CYCLE CHOSE. Verdict 5's R825 named both sites by line;
`sections.groups` is the one where the collapsed value is a STIFFNESS.**

```
claim  two of the three `_require_name_keys` call sites can be deleted with the measuring
       half of the suite green
cmd    in the archive copy, one call-site line removed at a time, nothing else touched;
       tests/unit/test_run_config.py + tests/verification/rung5 +
       tests/regression/test_r1_published_artifacts.py
out    baseline                                                 171 passed
       `_require_name_keys(lines, ...)` removed   (line_masses)  4 failed, 167 passed
       `_require_name_keys(groups_raw, ...)` removed             171 passed
       `_require_name_keys(block, where)` removed  (bodies)      171 passed
       restored                                                 171 passed
cmd    grep -rn "are not strings|Quote the name|_require_name_keys" tests/ --include=*.py
out    tests/unit/test_run_config.py:380
       tests/unit/test_run_config.py:381        -- two lines, one test, one mapping
cmd    which mapping that test exercises
out    tests/unit/test_run_config.py:376  data["mass_distribution"]["platform"] =
                                            {"line_masses": yaml.safe_load(block)}
rule   verdict 5's R825 -- "Closed when two keys that differ in text and agree after `str()`
       are refused at BOTH sites (`:611` and `:661`)"; and CLAUDE.md, "A closing condition
       that names sites is closed site by site. Half of an item is not the item"
judge  the code reaches all three sites and I confirmed all five refusals through the real
       `load_config`. What holds them is one parametrised test over one of the three.
       **`sections.groups` is the site verdict 5 ranked higher** -- "one of the two declared
       tubes is gone with no message ... `sections.groups` is wired to the model in step 1,
       and FL2(a) makes group labels user-chosen" -- and it is the unheld one. Â§4's cycle row
       reads "R825 (name-key check removed from line_masses)", so the cycle was run on the one
       site that is held. **R755's shape for a fourth round: right about the axis its author
       swept, silent about the two with nothing on them.**
```

**Closed when** the existing `test_FQ2_R825_a_NON_STRING_NAME_KEY_is_REFUSED` parametrisation
gains a `sections.groups` case and a `mass_distribution` body-name case -- the test already takes
`(label, block)` and already mutates the example dict, so this is two rows -- each reddening when
its own call site is removed, with the string control still loading. **Paste the cycle PER CALL
SITE, not per finding.**

**R834. (BLOCKS -- CZ0 head a) THE `str()` COERCION FQ1 ORDERED DELETED SURVIVES AT A FOURTH
DECLARED NAME, `mass_distribution.<body>.lumped[].label`. Two declared labels the reader wrote
differently arrive indistinguishable. And Â§2's claim that none survives carries a command that
cannot find it.**

```
claim  a lumped mass's declared label is still coerced, and two of them collapse to one name
cmd    the shipped example with `platform` given an explicit distribution carrying two lumped
       masses, labels `true` (unquoted) and the quoted string "True", through the real
       `load_config`
out    LOADED. lumped labels: ["True", "True"]
       two DECLARED labels, both arrive as: ["True"]
cmd    floatfea/run/config.py:669
out    label=str(item.get("label", f"lumped_{i}")),
rule   FQ1's own argument, which `_require_name_keys`'s docstring states at
       floatfea/run/config.py:248-252 -- "These keys are NAMES -- member groups, body names --
       and a name is a string: `true` is a boolean the reader did not mean and `1` is a
       number. Refused with 'quote the name'"
judge  `LumpedMass.label` is annotated `str` and is the only identifier a point mass has. The
       schema's own discipline is refuse-not-coerce -- `_checked` at `:202` rejects a `bool`
       explicitly, by name, for every declared NUMBER -- and this one declared field coerces
       instead. Two masses the reader distinguished become two masses with one name, and a
       default `lumped_{i}` can be collided with by an explicit `lumped_0`. **No mass reaches a
       member today**: `floatfea/run/pipeline.py:163-171` refuses explicit mode because
       "nothing consumes it yet -- FL2 wires it". That is R822's exact position one round ago,
       which verdict 4 ruled blocking for the stated reason that the loader's guarantee is
       false for a measured class of its own declared input and the step that wires it is the
       step the finding carries into. FL2 is Â§9's first two rows. **FQ1's letter does not cover
       a label -- it says "mapping whose keys are names" -- so this is not a directive breach.
       It is the same defect one field across, and I am naming it before FL2 ships the
       consumer.**
```

```
claim  Â§2's refutation command cannot refute Â§2's claim
cmd    docs/reports/R1/step-2.md:115-117
out    claim  no str() coercion on a name key survives anywhere in the schema
       cmd    grep -n "str(g)|str(name)" floatfea/run/config.py
       out    (no output)
cmd    the command that does reach it
out    grep -n "label=str(" floatfea/run/config.py   ->  669:  label=str(item.get(...))
rule   BF0 -- "A claim without its command is not written", and a triple whose command cannot
       fail is not a triple
judge  the needle is the two spellings the same commit deleted, so it searches for its own
       repair and reports success. The claim is universal ("anywhere in the schema") and the
       command is particular to two call sites. Prose, so the sentence itself is closure item
       C27; the code it misdescribes is the finding above.
```

**Closed when** `lumped[].label` refuses a non-string with the same message, or the report states
that the site was deliberately left and why, with the command that reaches it.
`_require_name_keys` already exists and takes a mapping; a scalar needs the one `isinstance`
check, not a new helper. And one case that reddens when it is removed.

**R835. (DOES NOT BLOCK -- recorded, and it is a directive to propose rather than a finding)
EG3's ENUMERATION IS SHORT OR MIS-FILED A FIFTH TIME, AND I MEASURED A NAME SECTION 7 DOES NOT
LIST. I agree with all three of the implementer's and I am adding a fourth.**

```
claim  `test_the_report_carries_a_WHOLE_SUITE_count` is on state (2)'s list (FC1) and fired in
       state (1) at this commit
cmd    gh run view 39044715217 --log-failed, the nine FAILED ids
out    tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
       tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count
       tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
       ...[non_numeric_step_suffix]  ...[superscript_digit_step_number]
       ...[draft_suffix_beside_a_step_report]  ...[step_number_is_the_empty_string]
       ...[verdict_amended_after_the_commit_the_report_answers]  ...[zero_padded_step_number]
cmd    each of the seven planted states' own failure line
out    2 failed, 400 passed, 1 skipped   -- identical in all seven inner runs
rule   CLAUDE.md, FC1 -- state (2)'s list gains `test_the_report_carries_a_WHOLE_SUITE_count`
       and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`
judge  this tree is state (1) -- a report with no verdict -- and the name fired here. FC1's
       stated REASON covers it (neither can pass in the commit it describes) and that reason is
       state-independent, so it is admitted and is NOT CZ1 (iv); what is wrong is the state it
       is filed under, which is EJ2's correction a third time. **And the seven planted states
       are the cascade EH1 describes, identified as EH1 requires -- by the baseline being red
       and by each state's own 2-failed/400-passed/1-skipped line, not by name.** So there are
       TWO distinct reds at this commit and seven echoes of them, which is exactly what the
       report claims. The enumeration has now been short or wrong at EH1 (two each side), EJ2
       (two mis-filed), FN2 (three names), SECTION 7 (three more) and here (a fourth). **The
       membership RULE has been right every time and the list has never once been right.** My
       proposal is under its own heading below, so it leaves the loop rather than becoming a
       round.
```

**R836. (DOES NOT BLOCK -- recorded) The r754 sweep's zero margin is correctly recorded, and the
margin was measured in the wrong variable. The answer happens to be the same at this `D`.**

```
claim  the guard compares `d_outer / wall`, not the `d_over_t` the sweep intends, and the round
       trip through D/(D/x) is where the margin lives
cmd    scripts/measure/r754_stress_vs_grade.py:81-84
out    steps = round((DT_HI - DT_LO) / DT_STEP) + 1
       d_over_t = DT_LO + i * DT_STEP
       f_xc = local_buckling_stress(D, D / d_over_t, fy, E)      <- the guard recomputes D/t
cmd    all 29501 points, both variables, at D = 2.5
out    max intended d_over_t          : 300.0
       max ROUND-TRIPPED d_outer/wall : 300.0        (at i = 29500)
       points whose round-tripped d_t EXCEEDS 300.0  : 0
cmd    python scripts/measure/r754_stress_vs_grade.py ; echo exit
out    exit: 0        -- the EZ0 producer still runs, refusing none of its 29501 points
rule   SECTION 5's own triple, which measures max(5.0 + i*0.01) over range(29501)
judge  the conclusion stands and the margin is `0.000e+00`, which I confirm. The measurement
       behind it is of the value the script CONSTRUCTS rather than of the value the new guard
       COMPARES, and those are different functions -- at another `D` they need not agree. The
       fragility is real, and recording it rather than changing it is right: it is not a defect
       repair. Closure item C28 carries the corrected measurement.
```

## The four things the report asked to have attacked -- my rulings

**1. `section_class` AS A NON-REFUSING CLASSIFIER IS THE RIGHT SPLIT, THE CEILING NARROWS NOTHING
LEGITIMATE, AND I TRIED TO BREAK IT FIVE WAYS INCLUDING THE TWO THAT WEAKEN IT (EH4). The only
thing wrong at that clause is a sentence.**

```
claim  every entry that returns a capacity refuses at 300.01 and admits 300, at four grades;
       the classifier returns no capacity and labels `slender`
cmd    D = 2.5, wall = D/(D/t); five public entries x four grades x six D/t, through the real
       module
out    grade  D/t      section_class  local_buckling  axial_compr   bending      check_member
       S235   299.99   reduced_2      +1.604570e+08   +8.292474e+07 +1.2344e+08  U=0.0134
       S235   300.00   reduced_2      +1.604552e+08   +8.292388e+07 +1.2344e+08  U=0.0134
       S235   300.01   slender        REFUSED         REFUSED       REFUSED      REFUSED
       S355   300.00   reduced_2      +2.423897e+08   +1.187297e+08 +1.5118e+08  U=0.0096
       S355   300.01   slender        REFUSED         REFUSED       REFUSED      REFUSED
       S460   300.00   reduced_2      +3.140825e+08   +1.470399e+08 +1.5587e+08  U=0.0079
       S460   300.01   slender        REFUSED         REFUSED       REFUSED      REFUSED
       S690   300.00   reduced_2      +4.200000e+08   +1.840690e+08 +1.0232e+08  U=0.0071
       S690   300.01   slender        REFUSED         REFUSED       REFUSED      REFUSED
       and 845.1 / 2585 / 10000 REFUSED at all four grades on all four capacity entries
rule   FQ0 -- refuse D/t > 300 at every site, and a test asserts that D/t = 300 is accepted
       and 300.01 is refused through the public entry points
judge  **the split is right and it is not a hole argued around.** `section_class` returns no
       allowable; `reduced_2` is live to `300.0` inclusive at every grade, so the clause's
       legitimate domain is not narrowed at the top; and `_capacity_entries()` in the gate is
       the honest enumeration of what must refuse. The one site reachable to a published figure
       through the classifier is `scripts/measure/f6_results_report.py:312`, which publishes
       `klass.branch` and `klass.limit_3` -- and the member checks downstream of it refuse, so
       a slender section crashes the producer rather than publishing a capacity.
```

```
claim  the boundary solved in BOTH directions, including the two that WEAKEN the gate
cell   one variable each, in the archive copy; baseline 171 passed
out    ceiling 300.0 -> 300.00000000000006  (+1 ULP, WEAKEN)    4 failed, 167 passed
       ceiling 300.0 -> 301.0               (WEAKEN)           11 failed, 160 passed
       ceiling 300.0 -> 299.99              (TIGHTEN)          27 failed, 144 passed
       the two clauses DECOUPLED: a separate 900.0 on the two
         3.2.2 sites, limit_3 left at 300                       8 failed, 163 passed
       the `local_buckling_stress` refusal DELETED              5 failed, 166 passed
       restored                                                171 passed
rule   EH4 -- the ceiling falls toward the clean value, and the injection rises until a clean
       case trips
judge  **zero margin in both directions**: one ULP up reddens, one hundredth down reddens. And
       the hole I expected is not there -- I thought one constant serving two clauses made
       `test_G61_the_two_clauses_AGREE_about_the_slenderness_limit` unfalsifiable, since sharing
       a constant means the two can no longer disagree. Measured, decoupling them gives
       8 failed: the test drives `allowable_axial_compression` at D/t = 700 and expects a
       refusal, so a divergent 3.2.2 ceiling reddens it. The gate carries its own failure.
       **That is the one argument in this review I converted to a measurement and lost, and
       losing it is the answer to the question.**
```

```
claim  the one thing wrong at that clause is prose, and it contradicts this commit's own gate
cmd    floatfea/checks/api_wsd.py:233-235
out    "D/t > 300 IS REFUSED RATHER THAN EXTRAPOLATED. The clause's third branch is written
        only to D/t = 300; beyond it local buckling governs ... Returning a number there would
        be inventing a clause."
cmd    section_class(2.5, 2.5/300.01) at four grades
out    OK  branch=slender  limit_3=300      -- it returns, at every grade
rule   CW0 -- prose in the source tree is a test, a triple, or deleted
judge  `api_wsd.py:233` is the docstring of the one function that does NOT refuse, and R819's
       condition named `:228` as a site. Under FQ0 the NUMBER there is now right, which is what
       the condition asked for, so R819 closes. What is left is the attribution: the report's
       section 3 says `section_class` is deliberately not a refusal site, and
       `test_FQ0_section_class_CLASSIFIES_above_the_ceiling_and_hands_off_the_refusal` says the
       same, and this docstring says the opposite. Closure item C26, named rather than
       smuggled, and it is the only reason I am not calling section 3 complete.
```

**2. SECTION 5's GOLDEN RULING IS CORRECT, I VERIFIED IT IN THE STRONGER DIRECTION, AND THE
REGENERATION IT LICENSED WAS NOT FINISHED -- which is R831.**

```
claim  the shipped F6 deliverable IS a regeneration of this tree at the pin, and FQ0's ruling
       and not the pin is what moved line 42
cell   ONE variable: BENDING_THIRD_BRANCH_MAX_D_OVER_T 300.0 -> 300000.0/355.0. Pins, tree,
       generator and interpreter all held. My interpreter reads numpy 2.5.4, scipy 1.18.1 --
       the PINNED set, and the set CI resolved.
cmd    python -m pytest -q tests/regression/test_f6_deliverable_agrees_with_itself.py, at HEAD
out    20 passed in 192.09s
cmd    the same file with the constant reverted
out    1 failed, 19 passed in 190.75s
       line 42  shipped "... 29.1268 / 58.2535 / 300.0000"  vs fresh "... / 845.0704"
       line 154 shipped "| G6.1 | ... | pass |"              vs fresh "| ... | FAIL |"
       line 165 shipped "  G6.1   87 passed"                 vs fresh "  G6.1  11 failed, 76 passed"
cmd    the same file at HEAD again
out    20 passed in 163.92s
rule   FQ3 -- if the golden moves under the pin, STOP and report, do not re-baseline silently;
       and BP0 -- when a decision rule changes, every figure citing the old rule is regenerated
       or withdrawn in the same commit
judge  **the judgement is right, and I ran it the right way round.** The implementer's cell
       measured the state BEFORE regenerating, so their HEAD showed one line differing; mine
       measures AFTER, so HEAD is green and the REVERT is red -- which is the direction that
       distinguishes "the rule moved the figure" from "the figure is stale for some other
       reason". 3768 passed / 9 failed at the pin, with CI's rung-6 step (which runs
       tests/regression) green at this sha, is the same answer on a third machine. **FQ3's stop
       condition was correctly ruled not met, and BP0's regeneration was the right action.**
       What is wrong is that the same commit regenerated three OTHER deliverables and left them
       stale on a different line -- R831. The ruling is sound; the regeneration it authorised
       stopped one file short.
```

**3. C22: I ACCEPT THE RULING. It is a fix, not the removal of a guard's cause, and the
measurement is the five reds that cleared.** `scripts/ci_section.py`'s refusal is correct -- a
report must not publish a CI table for a commit with no run -- and the marker was a stale
DECLARATION, not a symptom. The marker reading 1 while step 2 was worked made `REPORT` resolve
to the closed step 1's newest revision, which answers verdict 2 at `582cde72`, a pre-FP1 commit
that will never have a run. Bumping it to 2 is repairing the input. The proof is at the reviewed
commit: the five C22 guards are absent from the nine reds, and section 0 carries a generated
table with real counts. **One residue, and I am NOT asking for a guard:**
`test_the_plan_names_the_step_under_execution` asserts `_plan_step() in REPORTED`, which a
lagging marker satisfies whenever both steps have reports, so the same staleness is admissible
again -- and a new assertion is new apparatus under the F6 freeze, so it goes onto
`docs/milestones/F2a.md` as a line and nowhere else. Closure item C29 is only that the
generator's refusal message names the missing run and not the marker, which is what sent two
rounds looking at the generator.

**4. THE MISSING WHOLE-SUITE FIGURE IS NOT A STOP, and I would rather say so than let it be
inferred.** The implementer offered it as a legitimate STOP; I decline it, on a measurement
rather than on indulgence. A whole-suite measurement at the reviewed commit EXISTS -- CI ran
`pytest tests/unit`, the six ladder rungs, and `pytest tests` with the three directory ignores,
at `09d5bc9`, and the union of those three invocations is the tree. The totals reconcile with
the implementer's own last complete local run to the test: 3768 passed, 9 failed, 1 skipped; two
distinct reds and seven echoes, every one traced by name. What is absent is the report's own
`scripts/suite_count.py` line, and FC1 already rules that it cannot be inside the commit it
describes. **The discipline that matters is the one the report kept:** it labelled a stale figure
as stale, named the four edits that followed it, and listed its subsets AS subsets. R309/CI1 is
the substitution it was avoiding and it avoided it. I will say the obvious thing once: a tree
whose own author cannot run its suite is a tree where the next real red hides, and that is a
scheduling fact for Xabier rather than a finding against this revision.

## Try to break it -- the adversarial cases I ran, and what they found

* **The clause's ceiling SOLVED in both directions rather than sampled on one side** -- +1 ULP,
  +1.0, -0.01, the two clauses decoupled, and the refusal deleted. Five cells, baseline 171.
  **Found nothing: zero margin both ways, and the agreement test carries its own failure.**
* **Five public entry points x four grades x six D/t through the real module.** Found nothing in
  the code and one sentence -- C26.
* **A 29501-point round-trip sweep of the EZ0 producer's own grid**, in the variable the new
  guard actually compares. **R836**, and the producer still exits 0.
* **The three `_require_name_keys` call sites removed one at a time.** **R833** -- two of three
  are held by nothing.
* **The name-key type space through the real `load_config`** -- bool, int and None at all three
  sites, plus the string control. The code is right at all three.
* **One field across from where FQ1 stopped**: two lumped masses whose labels differ only by
  quoting. **R834.**
* **The R829 branch reverted, one hunk, identical subset both ways.** **R832** -- 113 passed and
  113 passed.
* **A regeneration check on the published deliverables, in the direction that weakens the gate**
  -- not whether the file carries the marker but whether it carries what the code now produces.
  **R831**, the round's largest finding, and it took one command.
* **The section-5 cell re-run in the opposite direction** -- HEAD green, the revert red.
  Confirmed the ruling.
* **The operating-point assertion solved rather than sampled**: in
  `test_FQ2_R818_the_PROVENANCE_carries_the_sensitivity_operating_points` the whole numeric claim
  is a substring test for the character 1, which is True at K = 1, 1.5, 10, 0.1 and 21 and False
  only at 2. The half that matters -- the key and the two names reaching `provenance()` -- does
  carry its own failure, which the report measured. Closure item C30.

**What I did not find.** The FQ0 repair is the most thorough thing in this milestone so far:
three entry points, four grades, both message sites, the literal folded into the named constant,
the unreachable guard kept with the reason written at it, eleven cases, and a sweep domain
derived from the ceiling instead of a stale literal. I attacked it five ways and it held five
times. The loader's code repair is right at all three sites. The pin is right, and the golden
movement was reported rather than buried. **Every one of this round's four findings is about what
HOLDS a correct repair, or about a file the repair did not reach -- none is about the repair.**

**The pattern, named for a sixth round, because it has moved one step again.** Verdict 2: the
verifiable half gets verified and the deciding half gets described. Verdict 3: the deciding half
is what holds the repair. Verdict 4: the deciding half is the axis the author did not sweep.
Verdict 5: the deciding half is one layer below where the repair stops. **This round: the
deciding half is the OTHER INSTANCE of the thing just fixed.** The CP3 ordering error was found,
named and fixed for one deliverable, and repeated for three others in the same commit. The cycle
was run for the five repairs a directive named and not for the sixth in the same commit. The
name-key check was cycled at one of the three call sites it was installed at. The `str()`
coercion was deleted at the two spellings the grep knew and survives at the third. In each case
the author found the defect, understood it exactly, wrote it down correctly -- and applied the
fix to the instance they were looking at. The question that catches this round is: **what else in
this commit is an instance of the thing I just fixed?**

## CI at the reviewed commit: RED, two distinct reds, both traced, and it does not HOLD

```
cmd    gh run list --commit 09d5bc9 --json name,conclusion,workflowName,status
out    []            -- the short sha returns nothing; the run is on the full sha
cmd    gh run list --branch F3 --json databaseId,headSha,conclusion,status, matched on headSha
out    run 39044715217, head 09d5bc9acc3d9eea0a77a21b3e2bf8943ae8f50e, event push,
       status completed, conclusion FAILURE
cmd    gh run view 39044715217 --json jobs, read at STEP level
out    lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (163 passed) / guards and meta-tests FAILURE
       the verification ladder : SUCCESS
         rung1 1276 / rung2 216 / rung3 314 / rung6+regression 343 / rung4 66 / rung5 87
         collected, 0 failed, 0 errored, 0 skipped each; run_rung: OK six times
       CI determinism -- leg, and ten legs agree : SKIPPED (workflow_dispatch only, CK0)
```

**Not CK2's exhausted-allowance state.** Both real jobs ran for ten and seven minutes with
per-step conclusions and real counts, so the absent runner name is not the never-started signal
CK2 describes. The two determinism jobs are skipped by the workflow's own event gate, which is
CK0 by design and is recorded as that rather than as an unavailable check.

**The nine, each matched to its state's own list.** This tree is **EG3 state (1)** -- a report
exists, no verdict yet.

* `test_the_guard_reads_the_step_being_worked_on` -- state (1), the named baseline. Its own
  failure line reads that step 2 has a report and no verdict yet, which is the state by
  definition.
* `test_the_report_carries_a_WHOLE_SUITE_count` -- admitted under **FC1's stated reason**, which
  is state-independent; filed under state (2) and fired here. **R835**, and it is not CZ1 (iv).
* the seven `test_the_guard_survives_the_state` parametrisations -- the cascade, identified as
  EH1 requires: by the baseline being red and by each state's own failure line carrying the
  inner run's 2 failed, 400 passed, 1 skipped. Seven identical inner lines, which is the
  signature.

**So there are TWO distinct reds and seven echoes of them, and that is exactly what the report
claims.** ruff, black --check, mypy, actionlint, `pytest tests/unit` and all six ladder rungs are
GREEN in CI at this sha. **On CA2, which I keep in full because CLAUDE.md does not carry it:** a
red CI is a HOLD regardless of the local run, and EG3 is the clause that qualifies CZ0's head (d)
for a step's own boundary red. Both distinct reds are that boundary, by name and by reason, so
the red is recorded as red with its cause named and **CI does not HOLD**. What would HOLD is a
third, and there is none. **Four of the thirteen at `cfb76ff` were C22 and they are gone**, which
is FF0's cost paid off in one commit, exactly as FF0 predicts.

**EG3(ii): I measure state (1) clearing at my own verdict commit and the counts go in the next
revision's Carried.** My instructions have me run before writing, so it is measured after this
file exists.

## Corpus (EG4(e))

**The pause held. Zero new entries this round, and `tests/corpus/` is untouched by me --
`git status --porcelain` is empty.** Neither exception opens: this revision touches no part of
F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/test_f4_static_and_mapping.py:470-491`, not about `LumpedMass.label` --
I checked, because R834 is a label finding and the exception would have opened had it been the
same label.

**I ran the recorded substitute instead, both halves, and both produced a blocking finding** --
the fifth consecutive round in which they have:

* **a continuum grid over the parameter space a decision rule guards** -- the API ceiling across
  four grades and five public entry points, solved in both EH4 directions including by one ULP;
  the 29501-point round-trip sweep of the producer's own grid; and the name-key type space at all
  three call sites with the sites removed one at a time. **R833, R834, R836.**
* **a regeneration check on a published deliverable** -- not whether the artifact mentions the
  marker but whether it carries what the code now produces, over all nine caveats and all three
  files. **R831**, and it is this round's largest finding.

## Tolerances touched

**One THRESHOLD moved, by directive, and its effective value TIGHTENED by 2.8x at S355. No
accuracy tolerance moved, and `floatfea/tolerances.py` carries no new entry.**

| | |
|---|---|
| name | `BENDING_THIRD_BRANCH_NUMERATOR` becomes `BENDING_THIRD_BRANCH_MAX_D_OVER_T` |
| old | `300000.0`, read as this over F_y in MPa -- 845.07 at S355, 1276.6 at S235 |
| new | `300.0`, a FLAT D/t, the same at every grade |
| form | dimensionless ratio threshold, a clause constant. Not an accuracy tolerance and not relative to a response scale. It lives in `floatfea/checks/api_wsd.py` beside `LOCAL_BUCKLING_DT`, which `floatfea/tolerances.py:2940` already names as a THRESHOLD of this family with its counter-case in rung 5 -- so the location is the recorded precedent and not an exception |
| counter | `test_G61_the_third_branch_LIMIT_is_what_decides_the_refusal` -- moves the limit to 200.0 past a D/t = 250 point and asserts the branch changes, with the control re-asserted after restore. **I solved it in both directions rather than accepting it: +1 ULP gives 4 failed, +1.0 gives 11 failed, -0.01 gives 27 failed. Zero margin on both sides.** |
| direction | **TIGHTENING.** The admitted domain shrinks from D/t <= 845.07 to D/t <= 300 at S355. Nothing that was refused is now admitted, at any of the four grades I ran |
| justification located | `docs/directives/FQ.md:7-13` and `:37-48`, verbatim per FP0, committed at `58f2df0` as a standalone plan commit BEFORE any of it was acted on -- I verified the ordering in `git log`. Xabier records 300000/Fy as his own error. Restated at `floatfea/checks/api_wsd.py:73-97` with the three figures it retires named: 300000/F_y, 845.1 and 734.3 |
| rescue test | **none.** No test was red before this change and made green by it. The change breaks eleven rung-5 cases and they were re-derived rather than relaxed -- 700.0 left a parametrisation because it is now outside the clause, and an assertion on a 7000-point count was replaced by a STRUCTURAL claim (the accepted band is contiguous and its top IS the ceiling) rather than by a smaller literal. **That is the opposite of widening and it is the harder choice** |

```
cmd    git diff a777cc3..HEAD -- floatfea/tolerances.py
out    three comment lines: the constant renamed in the THRESHOLD paragraph at :2940, and
       D/t <= 300 attributed to FQ0 at :2933. No value.
cmd    the diff searched for isclose, abs_tol, rel_tol, approx, atol, rtol, powers of two, and
       bare numeric comparisons
out    new comparisons: d_t > BENDING_THIRD_BRANCH_MAX_D_OVER_T (twice, the threshold above),
       not isinstance(key, str) (a type test), `if basis:` (an emptiness test), and one
       structural claim about a refusal message
out    six new not-a-tolerance annotations, each on an EXACT equality against a clause constant
       or a declared input -- three against 300.0, one against 734.3370568237008, one against
       24.2, and one structural inequality. None is a comparison epsilon and none is a value
       chosen to make two numbers agree. I read all six.
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name, including tier cutoffs in screening
judge  the one movement is a tier cutoff TIGHTENING under a directive that names the previous
       value as an error, with its counter solved in both directions and no test rescued.
```

## Closure items (CZ0, fixed once in the step's closure commit)

C29 is FF0-class gating apparatus and is fixed in the NEXT commit rather than ledgered. The rest
are prose and figures.

* **C26.** `floatfea/checks/api_wsd.py:233-235` attributes a refusal to `section_class`, which
  does not refuse. CW0, and it contradicts the report's section 3 and
  `test_FQ0_section_class_CLASSIFIES_above_the_ceiling_and_hands_off_the_refusal`.
* **C27.** `docs/reports/R1/step-2.md:115-117` -- the claim is universal and the command is the
  two spellings the same commit deleted, so it cannot fail. BF0.
* **C28.** `docs/reports/R1/step-2.md:303-310` measures the sweep margin in the value the script
  constructs rather than in `d_outer / wall`, which is what the guard compares. The conclusion
  stands; R836 carries the corrected measurement.
* **C29 (FF0 class, next commit).** `scripts/ci_section.py`'s refusal names the missing run and
  not the stale step marker, which sent two rounds looking at the generator. A message change,
  not a new state.
* **C30.** `test_FQ2_R818_the_PROVENANCE_carries_the_sensitivity_operating_points` is named for
  the operating points and its numeric assertion is a substring test for the character 1, true
  at four of the six values I probed. Either assert the value or rename the test.
* **C31.** `constraints-dev.txt:50-52` carries "One line of 464 ... differed at the pin", which
  is the FIRST regeneration's figure; two lines differ in the committed artifact. The same file
  says, correctly, that counts belong in the report rather than in the comment (BI3) -- and then
  carries one. CP3.
* **C32.** `docs/reports/R1/step-2.md:274-282` claims the regeneration moves ONLY the line FQ0's
  rule governs; two lines moved. Section 7 corrects it, so this is the stale half of a pair.
* **C33.** `docs/reports/R1/step-2.md:89` closes a code fence and continues prose on the same
  line, duplicating lines 74-76 verbatim.
* **C34.** Section 7's CZ1 (ii) commands are narrower than CI's own -- `black --check floatfea
  tests` against CI's `floatfea tests scripts`, and `mypy floatfea` against CI's
  `mypy floatfea scripts/f4_dynamic_residual.py`. All four pass in both forms on this machine;
  the paste should be the gate CI runs.
* **C35.** `tests/regression/test_r1_published_artifacts.py:14-18` claims that reading the
  committed files "catches a regeneration that was never committed". R831 is the measurement
  that refutes it. The sentence goes with the needle change R831 requires.

## Where I disagree with the CRITERION rather than with the work

**EG3's enumerated lists should be deleted and the membership RULE kept.** Said once, here, so it
leaves the loop and goes to Xabier through the implementer rather than becoming another round.
The rule -- verdict-dependent, measured against a verdict-exists control -- has been right at
every application. The list has been wrong at EH1 (short two on each side), at EJ2 (two
mis-filed), at FN2 (short three names), in this report's section 7 (three more) and in my R835
(a fourth). That is five corrections to one enumeration, each adopted by its own directive, and
each round spends a paragraph reconciling a tree against a list that running the ids settles in
one command. **A list of names cannot be checked against a failure message; only running the id
at a verdict-exists commit can** -- which FN2 states in its own words and then adds three names
to the list anyway. I am not asking for new apparatus: the control already exists and both
reviewers already run it. I am asking that the list stop being the thing a round is measured
against.

## Next step opens when

**Step 2 stays open and nothing in it has closed. Revision 1 of 3 is spent.** Step 2's own gate
is FL2's five items, and section 10 correctly says none is built -- that is expected of a
revision answering FQ0 to FQ3, and it is not a finding.

**Schedule, ruled on because FQ5 asked and sections 1 and 9 answered.** The report gives R1
complete on **5 November** against a 28 October target, reports it the day it is known, and
carries the per-item estimate, the measured 1266 lines to move, the calendar arithmetic and a
1.3x re-work factor taken from this milestone's own history. **I endorse the date and the method
and I will not soften either**: three revisions and five carried items in step 1, four more from
step 2's first commit, four more here. CLAUDE.md requires an escalation with the choice stated
when two consecutive steps close carrying blocking items, and section 9 states it -- step 2's
gate alone, with FL3 slipping -- and then declines to propose it because FQ4 forbids trimming.
**That is the right refusal and the choice is Xabier's.** One correction: the 1.3x is applied to
a nine-day estimate the report itself calls judgement rather than measurement, so 5 November
inherits the softer of its two inputs. Report the next slip the day it is known, as this one was.

1. **R831** -- the three artifacts under `results/R1/example/` regenerated at the answering
   commit with the paste taken last (CP3), and one existing gate's needle changed from
   `CAVEAT_MARKERS` to `floatfea.cli.TABLE_CAVEATS`. The counter is a caveat reworded in
   `cli.py` with the files left alone.
2. **R832** -- one case on a `RunResult` with an empty `wave_basis`, asserting both halves and
   reddening when the branch is reverted. `tests/unit/test_run_pipeline_refusals.py:585-600`
   already builds the stub. Paste the cycle.
3. **R833** -- the existing name-key parametrisation gains a `sections.groups` row and a
   `mass_distribution` body-name row, each reddening when its own call site is removed, with the
   string control still loading. **Paste the cycle PER CALL SITE.** R825 is not closed until both
   sites verdict 5 named are held.
4. **R834** -- `lumped[].label` refuses a non-string with the same message, or the report says
   the site was left and why, with the command that reaches it. One case that reddens.
5. **The closure list above**, fixed once in the step's closure commit -- except C29, which is
   FF0-class and is fixed in the next commit rather than ledgered.
6. **R835 and R836** -- recorded, not blocking. R835 is a directive to propose, not an edit.
7. **The push (FP1), continued exactly as done here.** It gave this check a readable CI run at
   the judged commit, a 3778-test total reconciled across two environments, six green ladder
   rungs and a green mypy on a machine neither of us controls. It is not an open item and must
   not become one again.

**What this commit got right, and it is much the larger part.** FQ0 was executed past its own
letter: the directive named a gate, the implementer found that the gate drove one entry point of
three, and then said so in the test's own docstring rather than quietly widening the gate. A
refusal message that was self-refuting at its own boundary was found by reading it rather than by
a test. A guard the ruling made unreachable was KEPT, with the reason written at the guard, which
is the opposite of the cheap move. A stale literal in a sweep domain was replaced by a structural
claim instead of by a smaller literal. The constant's rename reached `tolerances.py`'s comment,
which nothing in the suite would have caught. The golden moved and was reported with a
one-variable cell instead of re-baselined -- and the cell is correct, which I checked in the
direction its author could not. A premature sentence in `constraints-dev.txt` was corrected to
what the measurement said, with the author's own name on the error. C22's cause was diagnosed
correctly after two verdicts had attributed it to the wrong file. And the whole-suite figure was
owed, labelled as owed, and its subsets labelled as subsets, on a machine that could not produce
it -- which is the one place in this history where the honest answer and the convenient answer
were furthest apart.
