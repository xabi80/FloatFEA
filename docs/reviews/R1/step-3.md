# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 945d250941b9fe8f79b16bd4170dbef225628348
**Reviewed commit: `945d250941b9fe8f79b16bd4170dbef225628348`.**
Verdict: HOLD
Tests: 3595 passed, 104 failed, 1 skipped, 2 warnings in 1005.68 s (0:16:45)   (my own run, at the reviewed commit, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the fourth in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **ONE FINDING
BLOCKS (R866)** and it is in FL2(c), the item this turn shipped: `load_cases.headings` is
accepted, validated, and read by nothing, and `floatfea run` publishes all three deliverables
for a configuration declaring three headings. Five more findings are ledgered.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1";
`docs/directives/FR.md`). For R866 I state the silently wrong result it produces; for each of
the other five I state that it produces none, and for the one that will produce one later
(R869) I name the trigger.

**SIX COMMITS IN ONE TURN IS ONE CHECK, which is my own ruling from the previous round and I
hold to it.** The sequencing is better than one diff would have been: each item's own commit
told me which configuration its author chose, and both of the configurations that produced
findings are ones no commit chose.

```
cmd    git diff --name-status eb85d08..HEAD
out    M CLAUDE.md / M docs/SUPERVISOR.md / A docs/directives/FS.md /
       M docs/directives/README.md / M examples/platform12_placeholder.yaml /
       M floatfea/cli.py / M floatfea/model/platform.py / M floatfea/run/config.py /
       M floatfea/run/pipeline.py / M scripts/write_verdict.py /
       A tests/unit/test_headings_and_bem_coverage.py /
       A tests/unit/test_topology_from_config.py
cmd    git diff eb85d08..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff eb85d08..HEAD -- tests/conftest.py and the double-star pathspec
out    (empty)
cmd    git ls-files -- tests/conftest.py and the double-star pathspec
out    tests/conftest.py                       -- a file, as my instructions say it must be
cmd    git ls-files | grep -i conftest          -- the whole-tree census (CH2/CI0)
out    tests/conftest.py
       tests/test_supervisor_conftest_pathspec.py   -- one conftest, depth one, unchanged
cmd    git diff --stat eb85d08..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 99 +++------  (26 insertions, 73 deletions)
       -- NOT a STOP. It is in e227200, a STANDALONE process: commit citing FS1, whose only
          other file is CLAUDE.md; git show --stat e227200 touches no floatfea/ and no
          tests/. I read every removed line: the enumerations go, CZ1 (iv) stays, EG3 (i)
          stays and now cites the predicate. No guard was removed. One sentence SURVIVED
          that FS1 retired -- R871 below.
cmd    git diff --stat eb85d08..HEAD -- results scripts/measure
out    (empty)                                 -- no published deliverable moved
cmd    git status --porcelain
out    (empty)                                 -- clean before I ran anything and after
cmd    ruff check floatfea tests scripts ; black --check floatfea tests scripts ; mypy floatfea
out    All checks passed! / 150 files would be left unchanged /
       Success: no issues found in 42 source files
cmd    <this body> | python scripts/write_verdict.py --milestone R1 --step 3 --interim
out    the file you are reading
       -- **FS2's WRITE PATH IS EXERCISED AND IT WORKS. R856 IS ANSWERED.** This is the
          first verdict in step 3 that is not hand-written, and the implementer was right
          that the write was the one half it could not measure.
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`) and four
verdicts are now newer than it. That is EG3 state (2) and it is the whole of this tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R856** (write_verdict.py refuses a step with no report) | **ANSWERED, and I verified the half the implementer could not: the WRITE.** | `scripts/write_verdict.py:166-180` adds `--interim`; `:233-236` puts "ES0 INTERIM CHECK (counts against no round)" in the header. This file went through it. I also checked what the new header could break and it breaks nothing: a grep for the heading across `scripts`, `tests` and `.claude` reaches `write_verdict.py:234`, two synthetic fixtures in `tests/test_report_carried.py` and the agent template; the `Stop` hook and all four resolvers read the `Verdict:` and `Reviewed commit:` lines, both unchanged. |
| **R835, R836** (EG3's enumerated lists, nine measurements, wrong in both directions) | **ANSWERED by FS1/e227200, and I applied the predicate per id to all 104 reds rather than ruling a cascade. 102 satisfy it; TWO DO NOT -- R871 and my criterion note.** | `CLAUDE.md:429-477`, `docs/SUPERVISOR.md:556-585`. The predicate is right where the lists were wrong, and its first application is measured in the CI section below. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **ANSWERED as a ROUTING decision: FS3 ledgers it to FL3**, and the directive is now recorded where a repair can be checked against it (`docs/directives/FS.md:28`, FP0). | Not the implementer's to repair in code, and no longer open against step 3. |
| **R862** (three hand copies of the stage set; the pipeline computes the published total) | **still open, correctly, and NOT YET DUE -- I measured that the trigger has not fired rather than taking the commit's word.** | The five timing assignments in `floatfea/run/pipeline.py` are unchanged (653, 701, 712, 717, with 720-721 summing four of them) and `WALL_TIME_STAGES` at `floatfea/cli.py:37-43` is unchanged. **No timed stage was added, so the 40.000 s understatement is not reachable at this commit.** It blocks in the commit that adds one, which is FS0's item 4 or 5. |
| **R863** (the exclusion set is now defined by the code under test) | **still open, untouched** | the diff over `tests/regression` since eb85d08 is empty. |
| **R864** (the byte-identity claim's witness is blind to its own subject) | **still open; its condition is a sentence in the report and no report revision exists** | unchanged by this diff. |
| **R865** (the docstring at `tests/regression/test_r1_example_regenerates.py:224`) | **still open, untouched, correctly so** | same empty diff over `tests/regression`. |
| **R847 / C43** (section 3's "0 of 49 rows" does not reproduce) | **still open; FR1's third class, and no revision exists in which it could be answered** | unchanged. |
| **R848** (the empty-directory refusal admits a bare dot, a dot-slash, a double dot, a padded dot) | **still open, untouched** | the diff over `floatfea/cli.py` since eb85d08 is one comment block inside `_cmd_export`. |
| **R849 with R854** (four gates quantify over hard-coded three-file tuples) | **still open, both sites; step 3 has added no deliverable yet, so it is not yet worse** | `tests/regression/test_r1_example_regenerates.py:51`; `tests/regression/test_r1_published_artifacts.py:69`. R862 is the same species in a third place. |
| **R855** (the suite at a commit carrying no report revision) | **WITHDRAWN, and the standing condition IS MET at this commit** | the turn states plainly which runs it made (267 passed on two subsets, 2516 passed over three directories) and that it did NOT measure the whole suite at 945d250. No green is stated that was not taken. **I produced the whole-suite number, as I do by rule: 104 failed, 3595 passed, 1 skipped.** |
| **The fourth wrong figure** (290 where the run printed 267) | **CORRECTED ON THE RECORD, and I re-took the figure rather than accepting that it had been checked** | `945d250` names the pattern (R853, R857, R844, this) instead of the instance, which is what BP0 asks for. I re-ran the command `cadbbf7` cites -- `pytest -q tests/unit tests/regression/test_r1_published_artifacts.py` -> **267 passed** at this commit. The nine refusal messages reproduce and the 19-passed revert-red-restore baseline reproduces. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally AND on a machine neither of us controls** | mine above; CI run 39361398619, job `lint, unit and guards`, read at STEP level: actionlint, ruff, black --check, mypy and unit tests all SUCCESS, only `guards and meta-tests` FAILURE. Every step RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | unchanged by this diff. |
| **C44, C45** | **C44 carries. C45 RECURRED IN THIS TURN'S OWN PROCESS COMMIT and that is R871** -- the commit that retired the hand lists left one in my instructions and removed it from `CLAUDE.md`. | measured in R871. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer and not the list. |
| **EG3(ii): the verdict commit measured** | **DONE, by the control rather than by family** | at `bd315a1` -- a commit where a verdict exists WITH its answering report -- the two report-guard files are **149 passed, 0 failed**, so not one of this tree's 104 reds is red where the boundary state is absent. That is the measurement that separates "red because no answering report exists" from "red for another reason", and it is what covers the two ids the predicate does not admit. |
| scripts/suite_count.py's own line, and CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer. |

## Findings

**ONE BLOCKS.** No tolerance moved, no conftest moved, no published deliverable moved -- and I
established the last of those by regenerating the deliverables from this tree rather than by
reading the diff: **the default star is unmoved, `U = 1.71167 at platform:hub4_arm ROOT
(T = 12.5 s, 3.3.2 interaction)`, identical to the committed `results/R1/example/report.md:63`.**
The label-preservation property FL2(a) was built around holds, and I checked it by running the
model rather than by reading `_platform_label`.

**R866. (BLOCKS -- FR1's second head, an input accepted and used other than as declared)
`load_cases.headings` IS PARSED, RANGE-CHECKED, REPEAT-CHECKED -- AND READ BY NOTHING.
`floatfea run` ACCEPTS A CONFIGURATION DECLARING THREE HEADINGS, EXITS 0, AND WRITES ALL THREE
PUBLISHED DELIVERABLES FOR ONE. This repository already refuses exactly this situation twelve
lines away (R809), and the new field departs from that pattern.**

```
claim  nothing in floatfea/ reads the declared heading set
cmd    grep -rn "headings" --include=*.py floatfea
out    floatfea/run/config.py       -- the field (:421) and its parser (:866)
       floatfea/run/pipeline.py:515 -- uncovered_headings
       floatfea/run/pipeline.py:543 -- refuse_uncovered_headings
       floatfea/cli.py:407          -- a COMMENT saying where the call site would go
       -- ZERO call sites of either function in floatfea/; the only callers are the new tests
cell   the shipped example with load_cases.headings [0.0, 45.0, 90.0] and NOTHING else
       changed, through the real CLI, outputs redirected to a temporary directory
out    $ python -m floatfea.cli run <that config>
       EXIT=0
       wrote member_forces.csv (1248 rows) / utilisation.csv (32 rows) / report.md
       governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
       total wall time 77.35 s
       -- 1248 rows and 32 stations, the same as the single-heading baseline, because the
          declared set reached nothing
cmd    what the three artifacts say about the heading they were produced at
out    report.md:7   * **config** -- headings_three_declared.yaml
       report.md:23  * **heading** -- 0.0 deg
       report.md:55  EX3/R724: where a run covers a SINGLE heading the heading dependence
                     is UNTESTED ...
       utilisation.csv line 3: "# caveat: ... where a run covers a SINGLE heading ..."
       -- the caveat is TRUE OF THE RUN AND FALSE OF THE CONFIGURATION, and nothing anywhere
          names the two declared headings that were never run
cmd    the pattern this repository already has for a declared input it cannot honour
out    floatfea/cli.py:354-362, R809:
         if cfg.outputs.required_section or cfg.outputs.truss_sizing:
             raise ConfigError("... are FL2(b) and are not wired in R1 step 1 ... Refused
               before any output is written, so nothing on disk describes a run that did
               not happen.")
       -- the same shape, in the same function, twelve lines above the run_pipeline call,
          and R809's own recorded reason is that three artifacts had been left on disk
          mentioning the refusal nowhere
cmd    whether the missing check is buildable HERE, which is the question the turn asked me
out    floatfea/run/pipeline.py:558 exported_wave_basis ALREADY reads the heading the npz was
       exported at, from the sidecar, in this repository, with no HSP worktree -- measured on
       the committed data/f4/dynamic_inputs.npz it returns heading_deg 0.0. So "the declared
       set must be exactly the heading this npz carries" is one comparison between two
       values that are both already in hand.
rule   FR1's second head, verbatim -- "an input accepted and used other than as declared";
       and CLAUDE.md's non-negotiable that a validation failure never degrades to a warning
judge  **THE SILENTLY WRONG RESULT, stated as FR1 requires: `results/<dir>/utilisation.csv`
       and `report.md` published as the output of a configuration declaring headings
       [0, 45, 90], with U = 1.71167 presented as THE governing utilisation, when it is the
       envelope over heading 0 alone.** Someone sizes steel against a U that covers one of
       three declared wave directions, and no line in any artifact and no exit code says so.
       The field's own docstring at `floatfea/run/config.py:425` ANTICIPATES the reader who
       will expect the envelope -- which makes this the known case rather than the missed
       one, and the docstring is in the file that reader does not open. `examples/` documents
       the new `topology` block in twenty-two lines and the new `headings` field in none.
```

**Closed when** `floatfea run` refuses a declared `load_cases.headings` it cannot honour,
before any output is written, in the form R809 already uses at `floatfea/cli.py:354` -- and the
sharper form is available for free: refuse unless the declared set is exactly the heading
`exported_wave_basis` read from the npz, naming both values. The ENVELOPE is not what I am
asking for; see the scope answer below.

**R867. (DOES NOT BLOCK -- ledgered) DECLARATION ORDER AND DIRECTION DECIDE WHETHER A DECLARED
TOPOLOGY CAN BE RUN AT ALL. The schema says order and direction do not identify a member (it
compares a frozenset); the builder's node NAMES say they do. Measured: the same five members
declared brace-first die with a KeyError three layers downstream -- and that is the exact order
the turn's own test uses.**

```
claim  a valid declared topology is runnable or not depending on the order it is written in
cell   nine topologies through the real builder, then joint_nodes_of, then the real CLI; one
       variable moved each; outputs redirected so no committed artifact was touched
out    the declared star                  run OK   U = 1.71167   (identical to the default)
       braced star, ARMS FIRST            run OK   U = 1.82047   1326 rows, 34 stations
       braced star, BRACE FIRST           EXIT 1   KeyError: no node named
                                                   'platform:hub1_arm_tip'   (0.1 s)
       one arm written [hub1, centre]     EXIT 1   KeyError, the same
       hub4 reached only by a brace       EXIT 1   KeyError, the same
       a ring with no centre member       EXIT 1   KeyError, the same
       three arms only                    EXIT 1   KeyError, the same
       a single member                    EXIT 1   KeyError, the same
       an unknown node hub9               REFUSED at build, by name, as designed
cmd    why order decides it, from the code rather than from the run
out    floatfea/model/platform.py:629 -- node() dedups by COORDINATE and keeps the name of
       whichever label reached the point FIRST. A brace declared before the arm that shares
       its hub takes the node, so the arm's platform:<hub>_arm_tip name is never created;
       and [hub1, centre] names it _arm_a rather than _arm_tip.
       floatfea/solve/static.py:135 and floatfea/post/forces_table.py:169 then look that
       name up and nodes.index raises.
cmd    the schema's own position on whether order identifies a member
out    floatfea/run/config.py:898 -- the duplicate key is a frozenset, so [hub1, centre] is
       refused as a duplicate of [centre, hub1]. The two layers disagree about whether
       direction matters.
cmd    the direction that is SAFE, measured before I claimed the one that is not (EH4)
out    for the name platform:<hub>_arm_tip to exist at all, some member must be labelled
       platform:<hub>_arm with its END away from the body centre, which requires the FIRST
       declared end to be centre -- so the tip name, WHEN IT EXISTS, is always at that hub's
       own deck joint. **A declared topology can lose a support node; it cannot silently
       acquire the wrong one.** That is why this is loud rather than silent, and I measured
       it rather than assuming it.
rule   FR1 -- a refusal whose message is unclear but whose outcome is right does not block;
       and my own guard that a gate carries its own failure, applied to the feature itself
judge  **it does not block: exit 1, a traceback, and nothing written** -- I checked the last
       clause by listing the output directory after the brace-first run, and no directory was
       created. What it costs is the feature: FL2(a)'s whole subject is non-star topologies,
       and of the eight non-default topologies I declared, exactly ONE runs. The two that
       SHOULD run and do not (brace-first, and an arm written the other way round) are
       rejected by a name lookup rather than by a refusal, which is why no reader would get
       "write the arms first" out of the message.
```

**Closed when** the node name is independent of declaration order and direction, or the schema
refuses the orders the builder cannot honour and names what to change -- in
`floatfea/run/config.py` if it is a schema rule, at `floatfea/model/platform.py:629` if it is a
naming one.

**R868. (DOES NOT BLOCK -- ledgered) THE COMMITTED TEST FOR "A NON-STAR TOPOLOGY" BUILDS THE
ONE ORDER THAT CANNOT BE RUN, AND NO TEST IN THE DIFF PUTS ANY DECLARED TOPOLOGY THROUGH A
SOLVE. The shipped example's comment shows the runnable order; the shipped test shows the
other one, and nothing compares them.**

```
claim  the new tests stop at the builder, so R867 was outside the collection they inspect
cmd    tests/unit/test_topology_from_config.py:92
out    braced = (("hub1", "hub2"), *STAR)      <- the brace FIRST, the order that dies
       ... and the case asserts labels, the centre name, the centre xy and len(members) == 5
cmd    how far the file reaches
out    a grep for solve, joint_nodes_of, compute_rows and run( in that file finds nothing.
       Nineteen cases, every one of them at build_superstructure or load_config.
cmd    the shipped documentation on the same question
out    examples/platform12_placeholder.yaml:35 lists the four arms and THEN [hub1, hub2] --
       the order that runs. The example and the test disagree and nothing compares them.
rule   my own recorded guard -- check that the collection the assertion inspects can actually
       contain the failure; and BE3's species, a check verified against inputs its own author
       chose
judge  **it does not block** -- no number is wrong and every one of the nineteen cases asserts
       something true. It is recorded because it is the reason R867 shipped: nineteen green
       cases over a feature whose failure is three layers past where all nineteen stop.
```

**Closed when** one case takes a declared non-default topology through `floatfea run` (or at
minimum through `joint_nodes_of` and `compute_rows`) and asserts a published number -- the
braced star's `U = 1.82047` is a value this round has already measured.

**R869. (DOES NOT BLOCK AT THIS COMMIT -- ledgered, WITH ITS TRIGGER NAMED) A DECLARED TOPOLOGY
THAT DOES NOT REACH THE CENTRE BUILDS HAPPILY, AND `_build_body` RIGID-LINKS THE WHOLE PLATFORM
REMAINDER -- 1.875e+06 kg at the shipped f -- TO A `platform_centre` NODE THAT IS AN ENDPOINT OF
NO MEMBER. Nothing refuses the disconnection; the only thing that stops it is R867's name
lookup.**

```
claim  the builder has no connectivity check, so the remainder can hang off nothing
cell   the ring ([hub1,hub2], [hub2,hub3], [hub3,hub4], [hub4,hub1]), built
out    members: platform:hub1_hub2, platform:hub2_hub3, platform:hub3_hub4,
                platform:hub4_hub1
       node names: platform_centre, platform:hub1_hub2_a, platform:hub1_hub2_tip,
                   platform:hub2_hub3_tip, platform:hub3_hub4_tip, platform_remainder
       -> platform_centre is node 0 and NO member has it as an endpoint
       check_limits, check_rigid_modes and admissible all pass; the build RETURNS
cmd    what centre_node carries
out    floatfea/model/platform.py:626 creates it unconditionally, and rigid_links (:762) ties
       remainder_node to it and measures the offset from it. remainder_mass at the shipped
       f = 0.5 is 1.875e+06 kg -- the same magnitude as every member's share put together.
cmd    whether anything refuses the disconnection
out    a grep for connected, connectivity and component in floatfea/model/platform.py finds
       nothing. The refusal that does fire is KeyError: no node named
       'platform:hub1_arm_tip', which is about a NAME and not about a graph.
cmd    why it does not block TODAY, measured rather than asserted
out    every path from a declared topology to a number goes through
       floatfea/post/forces_table.py:169 or floatfea/solve/static.py:135; the CLI has exactly
       two subcommands (run, export), export refuses unconditionally, and the ring run raised
       in 0.1 s with no output directory created.
rule   FR1's first head; and my own guard that a residual destroys information, applied to a
       mass that is present in the mass report and absent from the stiffness
judge  **it does not block at this commit and it is one accident away from doing so.** The
       accident is any path that solves a body without looking a tip name up -- a
       topology-aware support scheme is the obvious one, and FS0's items 4 and 5 re-solve.
       **At the commit where that happens, the platform's entire remainder mass and the loads
       reaching it are structurally absent from the frame, every member force is low by the
       share it carried, and the mass report still balances.** That is the defect the turn
       correctly found in geometry[0][1], one step further out: the centre is now in the right
       PLACE and still need not be attached to anything.
```

**Closed when** the builder refuses a declared platform topology whose members do not connect
the centre to every hub the deck owns, naming the hubs that are unreachable -- which also
subsumes five of R867's seven refusing cases and leaves R867 as the two that should run.

**R870. (DOES NOT BLOCK -- ledgered) FL2(a) AS SHIPPED IS A SUBSET OF THE LOCKED PLAN'S (a),
AND TWO SENTENCES IN `floatfea/run/pipeline.py` NOW DESCRIBE IT IN THE FUTURE TENSE WHILE IT HAS
LANDED.**

```
claim  the plan's (a) names four things and two of them are not built
cmd    docs/milestones/R1.md:81
out    "Member topology from the config: a list of members (body, end A / end B by node,
        joint label or coordinates, section group)."
       built:     ends by NODE NAME, platform only
       not built: COORDINATES (an end can only be centre or a deck hub, so a brace to a
                  mid-arm point cannot be declared) and SECTION GROUP per member; and body
                  is platform-only, which the commit justifies and I accept -- the hub
                  tripods are the deck's fact
cmd    the two source-tree sentences
out    floatfea/run/pipeline.py:123 "FL2(a) replaces this with a member list carrying its own
         group labels"  -- FL2(a) has landed and it does not
       floatfea/run/pipeline.py:180 "FL2(a) is where the builder gains per-body fractions"
         -- it did not
rule   CW0 -- prose in the source tree is a test, a triple, or deleted; and the step-3 gate at
       docs/milestones/R1.md:352, which is what the closing revision is judged against
judge  **it does not block**: no number is wrong, and both sentences sit inside refusals whose
       OUTCOMES are right. It is recorded now rather than at the close, because the closing
       revision will be read against FL2(a) and not against the commit message, and because
       the two refusals currently point a reader at a milestone that has already happened.
```

**Closed when** the first reviewed revision either builds the two remaining axes or records the
deviation with its reason, and the two sentences say what is true at their own commit.

**R871. (DOES NOT BLOCK -- apparatus, FF0 class: fixed in the next commit, not ledgered) FS1'S
OWN COMMIT LEFT A HAND LIST IN MY INSTRUCTIONS AND REMOVED IT FROM `CLAUDE.md`. Its check could
not see it, because the needle looked for the words "state (2) list" and the surviving list is
introduced by "The only failures are". AND FC1'S CLAUSE IS NOW ABSENT FROM BOTH FILES, so the
two reds FC1 existed to admit have no clause under which they are boundary reds.**

```
cmd    the two files on the same sentence
out    CLAUDE.md:421           "(2) Verdict written, answering report not yet. The answering
                                report clears them."
       docs/SUPERVISOR.md:547  "(2) ... THE ONLY FAILURES ARE
                                test_every_named_site_is_touched_or_declared,
                                test_the_report_carries_the_finding,
                                test_the_CI_section_is_about_the_REVIEWED_commit,
                                test_the_Carried_table_is_what_the_generator_produces and
                                test_the_generator_would_catch_a_row_under_the_wrong_number,
                                each naming a finding or a site of the newest verdict."
cmd    the commit's own check, re-run
out    grep -c over both files for the three list phrases
       -> CLAUDE.md:0   docs/SUPERVISOR.md:0      -- TRUE, and blind to the surviving list
cmd    the needle that does find it
out    grep -c test_every_named_site_is_touched_or_declared CLAUDE.md docs/SUPERVISOR.md
       -> CLAUDE.md:0   docs/SUPERVISOR.md:1
cmd    FC1 clause
out    grep -c for the FC1 heading in both files
       -> 0 and 0                                   -- removed from both
rule   C45, which is this item own name -- a mirror of a living document is a figure whose
       rule moves underneath it, which is BP0 applied to the criterion; and R755/R770 shape,
       a census whose domain cannot contain the thing it is looking for
judge  **it does not block under FR1**: no wrong result follows, and it is the gating
       apparatus, which FF0 takes out of the ledger and into the next commit. Two separate
       things in one finding -- the surviving list is C45 fifth occurrence and is one line to
       delete, and the missing FC1 clause is the criterion gap in my disagreement section
       below, which I ruled around with the bd315a1 control rather than holding the tree on.
```

**Closed when** `docs/SUPERVISOR.md:547` stops enumerating and cites the predicate, in a
standalone `process:` commit citing FS1 -- and the FC1 question is answered by Xabier.

The three commands above, verbatim, so the next reader re-runs them rather than reconstructing:

```
grep -c "state (1)'s list\|state (2)'s list\|own list" CLAUDE.md docs/SUPERVISOR.md
grep -c "test_every_named_site_is_touched_or_declared" CLAUDE.md docs/SUPERVISOR.md
grep -c "The two CZ1-class guards join state (2)" CLAUDE.md docs/SUPERVISOR.md
```

## Where I disagree with the CRITERION rather than with the work (said once, for Xabier)

**FS1's predicate is better than the lists at every id I tested but two, and those two are
structurally unpassable, so a literal reading of it has no exit.**

```
cmd    the predicate applied to all 104 reds, one id at a time
out    68  test_every_named_site_is_touched_or_declared[R85x-<site>]  names a finding AND a
                                                                      site of the newest
                                                                      verdict           OK
       21  test_the_report_carries_the_finding[R845..R865]             names a finding   OK
       10  test_the_guard_survives_the_state[...]                      satisfied only
             through its INNER FAILED list, which names R862, R863 and R865 sites -- I ran
             them and read the inner lists rather than ruling them by family            OK
        1  test_the_CI_section_is_about_the_REVIEWED_commit            "the CI section's
             first commit is d205833 and the verdict judged d89566d"    names the newest
                                                                        verdict          OK
        1  test_the_Carried_table_is_what_the_generator_produces       "26 generated rows
             are not in the report's Carried section" -- generated FROM the newest verdict OK
        1  test_the_generator_would_catch_a_row_under_the_wrong_number  StopIteration off
             that same baseline                                                         OK
        1  test_the_report_carries_a_WHOLE_SUITE_count   "the newest revision carries no
             whole-suite line"               -- names NO finding and NO site       **NOT OK**
        1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  "run 39162423263: the table says
             in_progress, gh says failure"   -- names NO finding and NO site       **NOT OK**
cmd    what the two are, and why no commit can ever clear them
out    they are FC1's pair. scripts/suite_count.py measures a CLEAN WORKTREE AT A COMMIT, so
       the line naming a sha cannot be inside that sha; scripts/ci_section.py --rounds needs
       a RUN, and no run exists for a commit before it is pushed. **FC1's clause was deleted
       from CLAUDE.md by this turn's own process commit** and survives only as a bullet
       explaining why the lists went.
cmd    the control I ruled on instead
out    bd315a1 (a verdict WITH its answering report), the two report-guard files
       -> 149 passed, 0 failed, and every one of this tree's 104 absent from that set
judge  **I ruled both as boundary reds under CZ1's own reusable half** -- "a check whose input
       is the commit itself cannot be measured before the commit exists" -- and I measured it
       rather than asserting it. I am not expressing this as a HOLD: it is not one of FR1's
       heads, and the right answer is a clause and not a commit. **The fix is one sentence:
       the predicate, OR CZ1's reusable half.** Without it the next reviewer reads "any other
       red blocks", finds two, and has no exit -- which is DD1's shape, and DD1 cost two
       verdicts that were not about the work.
```

## Try to break it -- what I ran, and what it found

* **Nine declared topologies, none of them the two the commits chose**, through the real
  builder, then `joint_nodes_of`, then the real CLI with outputs redirected: a ring with no
  centre member, a single member, three arms only, hub4 reached only by a brace, an arm written
  `[hub1, centre]`, the brace declared first, the brace declared last, the declared star, and an
  unknown node name. **One of the eight non-default topologies runs.** That produced R867, R868
  and R869. The implementer named three of these cases itself and was right that they were the
  ones to try.
* **Three full `floatfea run` executions writing all three deliverables into a temporary
  directory**: the baseline-equivalent (`U = 1.71167`, 1248 rows, 32 stations, identical to the
  committed `results/R1/example/report.md:63`), the braced star (`U = 1.82047`, 1326 rows, 34
  stations) and the three-heading configuration (`U = 1.71167`, 1248 rows -- R866). The first is
  the control that says both commits moved nothing on the default path, taken by running the
  model rather than by reading the diff. The second says a declared topology is NOT inert: it
  reaches the published number.
* **Both EH4 directions on the one new decision rule.** Strengthening: every malformation of
  `covered` I could construct makes `uncovered_headings` refuse MORE and never less -- a string
  `0,45`, radians and an empty tuple all return the declared heading as uncovered, `None` raises
  a `TypeError`, and ints, `numpy.float64`, `float32` and a plain list all compare equal, so no
  declared heading passes that should not. Weakening: the only input that could make a declared
  heading pass wrongly is a `covered` set that contains it, which is the caller's fact and is
  precisely why the parameter is a parameter. **The function is sound; what is missing is a
  caller, and that is R866.**
* **The schema's refusals re-run rather than read**: the nine `topology` cases and the seven
  `headings` cases all refuse with the needles claimed, and `_checked` at
  `floatfea/run/config.py:202` refuses a bool and a NaN explicitly, so `headings` reuses the one
  declared domain rather than a second copy of it. That half of FL2(c) is solid.
* **The predicate's first application, 104 ids one at a time**, with the cascade read off its own
  inner FAILED lists, plus the `bd315a1` control. That produced R871 and the criterion note.
* **My own set against CI's, both directions.** `comm -23` and `comm -13` over the two sorted
  104-id lists are both empty: the SAME SET, id for id, on two operating systems.
* **The new verdict header against every resolver that reads a verdict file, before I used it.**
  No guard keys on the heading line, so FS2's suffix cannot make this verdict invisible to the
  hook or to the three report guards.

**What I did not find, and it is the larger part.** FL2(a) found and fixed a real defect its own
feature would have created, in the place that is hardest to see -- a centre inferred from the
first member, which is correct for every configuration that existed before the commit -- and
fixed it by passing the fact down from the layer that owns it rather than by adding an assertion.
The property that mattered most, the declared star being the generated star with its labels,
holds under a full run and not only under a unit test. The commit that corrected its own wrong
figure did it on the record rather than by amending, and named the pattern instead of the
instance. FS1 removes an enumeration that was wrong in both directions and keeps CZ1 (iv) and
EG3 (i) intact; FS2's message says plainly which half it could not measure, which is exactly the
half I measured, and it works. `uncovered_headings` is a good function with its covered set
correctly parameterised.

## The two scope questions, answered

**On FL(c)'s third part: your reading is RIGHT and I am not asking you to build the envelope.**
A dynamic-inputs npz records one heading -- `exported_wave_basis` returns a single `heading_deg`,
the committed npz carries no heading key at all and the value lives in the sidecar -- so an
envelope over several headings needs load data at several headings, and manufacturing it is
"never invent a load distribution", which is CLAUDE.md's own non-negotiable and not a judgement
call. **What I would separate out, as a scope statement for Xabier and not as a finding:** the
MECHANISM is buildable here and the DATA is not. `load_cases.npz` is a single path; making it a
list, one file per heading, each carrying its own recorded heading, with the envelope over the
union and the governing heading reported, needs no HSP worktree -- it needs a second file, and
the second file is `export`'s job. Put that way the item stops being "underdetermined" and
becomes "the mechanism waits on nothing, the data waits on FL1", which is a smaller thing to
carry into FL3.

**On the BEM covered set being a parameter: AGREED, and that is not what R866 is.** Which
headings the dataset carries is the pinned HSP state's fact, a hard-coded list here would be
FloatFEA asserting something nothing in this tree can check, and taking it as an argument is the
right call -- I tried to break the function and could not. The step that went one too far is the
next one: "the covered set is HSP's fact" was used to leave the refusal with **no call site at
all**, while the fact that IS local -- the heading the npz in hand was exported at, which
`exported_wave_basis` already reads -- is compared against nothing. So, to your question as you
asked it: no, you have not used "it is HSP's fact" to avoid building the BEM check. You have
used the absence of a call site for THAT check as the reason there is no heading check at all in
`run`, and the local one is buildable today.

## CI at the reviewed commit: RED, 104 reds, ALL 104 boundary by MEASUREMENT

```
cmd    gh run list --commit 945d250941b9fe8f79b16bd4170dbef225628348
         --json conclusion,status,databaseId,workflowName
out    one run: databaseId 39361398619, workflowName CI, status completed,
       conclusion failure
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is not
          a pass and I did not record one. The judged commit had a run because it was pushed
          first (FP1).
       A NOTE FOR WHOEVER GENERATES THE CI SECTION: the same command with the SHORT sha,
          945d250, returns an empty list. The full sha returns the run. No bearing on this
          verdict; recorded because the generator takes a sha.
cmd    gh run view 39361398619 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1, 2, 3, 6, 4 and 5 -- all six rungs SUCCESS. No rung is red, so nothing
         above is uninterpretable and there is no STOP.
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS / guards and meta-tests FAILURE
         -- every step RAN rather than being skipped behind an earlier red, which is what
            CZ1 (iii) exists to see, and mypy is green there, so FP1's CI-only types-PyYAML
            red has stayed fixed
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39361398619 --log-failed, unique ids
out    68  test_every_named_site_is_touched_or_declared[...]
       21  test_the_report_carries_the_finding[R845..R865]
       10  test_the_guard_survives_the_state[baseline + 9]
        5  the five named in my criterion section above
       --- 68 + 21 + 10 + 5 = 104 exactly, with no remainder, and all 104 inside
           tests/test_report_carried.py and tests/test_report_guard_states.py
cmd    my own 104 against CI's 104, both directions
out    comm -23 (mine) (CI's)   (empty)
       comm -13 (mine) (CI's)   (empty)        -- the SAME SET, two machines, two OSes
cmd    the control that makes the trace a measurement and not a classification
out    bd315a1, the two report-guard files -> 149 passed, 0 failed
       -- not one of the 104 is red where a verdict exists WITH its answering report, so all
          104 are boundary-dependent BY MEASUREMENT rather than by family
cmd    the warning, traced rather than left as a count
out    a numpy overflow in dot, raised by
       tests/verification/rung1/test_corpus_configurations.py with the orient_norm_overflow
       entry -- a reviewer corpus entry whose whole purpose is to overflow a norm. Designed.
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with FS1's predicate; EG3 (i) -- every red tested
       INDIVIDUALLY or it is CZ1 (iv) unchanged
judge  **102 of 104 satisfy the predicate, the remaining two are FC1's pair and are boundary by
       the control, so the waiver applies in full and CA2's HOLD is not reached by CI.** FR1's
       red-test head does not stand on the boundary reds. **This verdict's HOLD is R866 and
       nothing else.**
```

**Not CK2's exhausted-allowance state.** `runnerName` is null for all four jobs including the two
that SUCCEEDED, so an empty runner name cannot separate the states in this repository and I did
not use it. What separates them: both real jobs carry per-step conclusions, real counts and four-
and fifteen-minute durations (02:54:02Z to 02:58:32Z, and 02:54:01Z to 03:09:30Z), and the two
skipped jobs are the determinism workflow's own event gate (CK0), with empty step lists at a
zero-second duration, which arises from a designed condition and not from an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree was
clean before and after.** Neither exception opens: this diff touches no part of F4's load-mapping
gate, and EB6's label-provenance gate is about buoy-centre labels in `tests/verification/rung4/`,
not about a topology list or a heading field. The last corpus commit remains `ba1527e`
(batch 47).

**I ran the recorded substitute and both halves paid again, for the eighth consecutive round:**

* **A continuum grid over the parameter space the new decision rules guard.** Two axes, because
  the diff moved two. The TOPOLOGY axis: member count 1/3/4/5, centre-touching or not,
  declaration order brace-first against arms-first, direction centre-then-hub against
  hub-then-centre, a hub reachable by its own arm against by a brace, and a known against an
  unknown node name. The COVERED-SET axis for `uncovered_headings`: tuple, list, numpy float64,
  numpy float32, ints, a string, radians, empty, `None`, minus-zero against zero, and 360 against
  0. It produced **R867, R868 and R869**, every one from a point on the order/connectivity axis
  that no commit swept.
* **A regeneration check on a published deliverable, in both directions.** Three full runs
  writing the three R1 artifacts: the default path reproduces the committed governing
  `U = 1.71167` exactly, which is the control; the braced star moves it to `1.82047`, which says
  the feature is live; and the three-heading configuration reproduces `1.71167` while declaring
  two headings that never happened, which is **R866**, this round's blocking finding.

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff eb85d08..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    the same diff, plus lines only, grepped for isclose, abs_tol, rel_tol, approx, atol,
       rtol, _COUNTER, tolerance, slack and epsilon
out    tests/unit/test_topology_from_config.py:70  "not-a-tolerance: the same two points"
       tests/unit/test_headings_and_bem_coverage.py:110  "not-a-tolerance: the declared
                                                          domain"
       -- two exactness comparisons, both annotated, neither introducing a value
claim  the one thing in this diff that could function as a tolerance under another name is the
       heading comparison in uncovered_headings, and it is EXACT by decision
cmd    the comparison, and the reason given for it
out    floatfea/run/pipeline.py:534 -- "An EXACT comparison, because a heading is a declared
       input and not a measurement ... there is no tolerance here to choose."
       I tested the near miss: uncovered_headings((44.9,), (0,45,90,135,180)) -> (44.9,)
rule   CLAUDE.md section Tolerances, its clause on anything that functions as a tolerance under
       another name; EU1
judge  **EU1 does not attach by its own words** -- no tolerance value and no declared counter
       moves -- **and I ran the adversarial case anyway**, because R694's lesson is that a value
       which does not move is the worst case and not the safest. The configurations the diff did
       not choose are the eight topologies and the three-heading config, and three findings came
       out of them. **The exact comparison is the right form here and I am not asking for a
       tolerance: a declared input compared with a tolerance is how 44.9 becomes 45.**
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1 -- no `Closes:`
line, deliberately, and the tool now writes a header that says which kind of verdict this is).**
Step 3 remains open with all three reviewed revisions available. **The HOLD is R866, and it is
answered before FL2's items 3, 4 and 5 continue** -- which costs FS0 nothing, because R866 IS an
FL2(c) item and the repair is the shape R809 already has twelve lines away.

1. **R866, before the next FL2 item.** A refusal in `_cmd_run`, before any output is written, for
   a declared `load_cases.headings` the run cannot honour -- and the sharper form is free: refuse
   unless the declared set is exactly the heading `exported_wave_basis` read from the npz, naming
   both values. One test that runs the shipped example with three declared headings and asserts
   the exit is non-zero AND the output directory is empty, which is R809's own two-part
   assertion.
2. **R867, R868 and R869 together in the first reviewed revision, or a stated reason not to.**
   They are one repair: refuse the topologies that cannot be built into a frame (R869 subsumes
   five of R867's seven), make the two that should run actually run (R867), and put one declared
   topology through a run (R868). The braced star's `U = 1.82047` and the default's `1.71167` are
   both measured in this verdict, so either is an assertable number.
3. **R862 IN THE COMMIT THAT ADDS A TIMED STAGE, not after it** -- unchanged, and verified not
   yet due. R863, R864 and R865 in the first reviewed revision, each with its figure regenerated
   at that commit (CP3). R847, R848, and R849 with R854, unchanged. R870 at the close or earlier.
4. **R871 in one standalone `process:` commit citing FS1** -- one sentence in
   `docs/SUPERVISOR.md:547`. It is apparatus, so FF0 takes it into the next commit rather than
   into the closure list, and it is not part of the HOLD.
5. **The FC1 question goes to Xabier with my criterion note, not into a round.** I ruled around
   it this time with the `bd315a1` control; the next reviewer reading "any other red blocks" will
   find two and have no exit.
6. **R852 is now routed rather than open** (FS3 to FL3). R856 and R835/R836 are ANSWERED by this
   turn's two process commits, and I exercised the write path that FS2's own message said it
   could not.
7. **The schedule, and FS4's checkpoint.** FR0's 5 November stands. FS4 asks for FL2 in its first
   reviewed revision by **26 October**: two of five items are built on 19 October, the band check
   is next, and the two sizing items carry FM0's re-solve loop and R862 with them. **Nothing has
   slipped yet and I am not re-opening the escalation FR0 answered** -- but the two sizing items
   are the large ones and they sit behind a checkpoint four days out. If the 26th arrives with
   items 4 and 5 unbuilt, FS4 asks for that report ON THE 26TH with a realistic date, not at the
   step's close.
8. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 104
   reds identical to mine id for id on a different operating system, and all six ladder rungs
   green.

**What this turn got right, and it is much the larger part.** It took FS0's order seriously and
built the model-facing item first. It found a real defect its own feature would have created and
fixed it at the layer that owns the fact, and it kept the published labels -- which I verified by
a full run against a deliverable written three commits earlier rather than by reading
`_platform_label`. It declined to invent the other headings' loads and said so, which is the most
valuable output available at that moment and is CLAUDE.md's own sentence for it. It corrected its
own figure on the record for the fourth time and named the pattern instead of the instance.
**And it asked me to attack the fix rather than the feature, which is where three of my six
findings came from: the fix is right, and the two layers around it -- the node names above it and
the connectivity below it -- are where a declared topology still goes wrong.**


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3
Reviewed commit: d89566d09019dc3bb744c3ad21e859d268ca21de
**Reviewed commit: `d89566d09019dc3bb744c3ad21e859d268ca21de`.**
Verdict: PASS
Tests: 3553 passed, 89 failed, 1 skipped, 2 warnings in 974.92 s (0:16:14)   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK, the third in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **Nothing
blocks.** R860 is answered at the site its condition named, and I checked the refactor
against artifacts committed three commits before it rather than against the diff. Four
findings below, none blocking, plus the one ruling the implementer asked for by name (R855)
and an answer to the sequencing question taken from the hook's own text.

**I RULED UNDER FR1 WITH EZ0** (`docs/directives/FR.md:14-26`, `CLAUDE.md` section "What
blocks for the rest of R1"). For each finding I say the silently wrong result it would
produce, or that it produces none. **This file is HAND-WRITTEN because the one sanctioned
path in refuses it -- R856, third measured occurrence.**

```
cmd    git diff --name-status 948b36a..HEAD
out    M  floatfea/cli.py
       M  tests/regression/test_r1_example_regenerates.py
       -- two files, 67 insertions, 12 deletions, nothing else
cmd    git diff --stat 948b36a..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff 948b36a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 948b36a..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
cmd    git ls-files | grep -i conftest             -- the whole-tree census, since the ladder's
                                                     gate reads a record a rung's own conftest
                                                     could write (CH2/CI0)
out    tests/conftest.py
       tests/test_supervisor_conftest_pathspec.py  -- one conftest, at depth one, unchanged
cmd    git diff --stat 948b36a..HEAD -- results scripts docs
out    (empty)                                   -- no published deliverable moved
cmd    git status --porcelain
out    (empty)                                   -- clean before I ran anything and after
cmd    printf <the four mandatory sections, with the Verdict line first> |
         python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       -- R856 again, at scripts/write_verdict.py:181. I also measured the ORDER of its
          refusals, which no previous round did: a body that does not begin with the
          Verdict line is refused FIRST, so the no-report refusal is reached only by a
          well-formed verdict and the file cannot be written by accident.
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict.
The newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`) and
three verdicts are newer than it. That is EG3 state (2) by definition, and it is the whole
of this tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R860** (`_TIMING_STAGES` was a hand copy of the literal at `floatfea/cli.py:297` and nothing compared them) | **ANSWERED AT THE SITE THE CONDITION NAMED, and I verified both halves myself. It has a REMAINDER that "there is no second copy" misses -- R862.** | `floatfea/cli.py:37-43` defines `WALL_TIME_STAGES`, `:320` iterates it, `tests/regression/test_r1_example_regenerates.py:45` imports it. The provenance is structural rather than inferred from a green: `grep -n "WALL_TIME_STAGES\|for stage in" floatfea/cli.py` is two lines, `37` and `320`, and the gate has no tuple of its own left. I reproduced their red (a sixth name in the tuple -> `10 passed, 1 failed`, `EXCLUSION_pin ('the SHIPPED report', ['build','code_check','load','solve','total'])`) and their baseline (`11 passed`). **And the pin cannot fail false**, which I measured rather than inferring from the generator's defensive `if stage in result.timings`: `grep -rn "RunResult(" floatfea` is ONE construction (`pipeline.py:675`), all five `timings[...]` assignments above it are unconditional, and every branch between them RAISES rather than returning. |
| **R857** (the comparable counts were measured against the rule the same commit deleted) | **ANSWERED, and the figure is right at this commit by my own measurement rather than by taking theirs** | `tests/regression/test_r1_example_regenerates.py:99` now reads 97/1286/70 and the file records all three wrong versions. Mine, through the gate's own `_lines()`: report.md total 105 comparable 97 timing 5 prov 3; member_forces.csv 1289 / 1286 / 0 / 3; utilisation.csv 73 / 70 / 0 / 3. The published arithmetic 105 - 8 = 97 holds, and the two CSV figures are unmoved because neither carries a timing row. **The rule did not move in this commit** -- the tuple's five names and their order are unchanged -- so 97 is measured against the rule the file runs (BP0), and the third statement of this number is the first correct one. |
| **R858** (the file claimed both excluded classes were "checked separately") | **ANSWERED, and the replacement sentence is TRUE -- I measured it over all FIVE rows and not the two it names** | `:55-66`. Mine: `| load |`, `| code_check |`, `| solve |`, `| total |` and `| build |` each edited in the shipped report, one at a time, each through the real eleven cases -> **11 passed, 0 failed on every one of the five**. And the broad half of the sentence, which is the half I could have let pass on the file's own authority: `grep -rn "Wall time\|wall_time\|timings" --include=*.py tests` reaches exactly one assertion on a wall clock, `test_the_run_reports_a_wall_time_for_every_stage`, and it reads `result.timings` from a LIVE run and never a published file. **So "no test in this repository reads a published wall-clock VALUE" is true as written.** |
| **R859** (the new comment named the wrong assertion) | **HALF ANSWERED. The pin comment is corrected and I confirmed every clause of it. THE DOCSTRING OF THE SAME FUNCTION, WHICH R859's OWN JUDGE NAMED, IS UNTOUCHED AND STILL FALSE -- R865.** "Half of an item is not the item" is CLAUDE.md's own sentence, and I apply it to my predecessor's condition rather than to the implementer's reading of it. | Corrected at `:241-245`, each clause measured: a sixth unrecognised `| mesh |` row reddens REGENERATES[report.md] (16 line(s) differ, shipped has 98 comparable lines against 97) with the pin GREEN; a duplicate `| total |` reddens the pin; a deleted `| code_check |` reddens the pin. Untouched: `:228`, "a fourth non-deterministic line reaching the deliverable reddens here instead of being absorbed". |
| **R861** (the baseline of nine was wrong within one commit; the trace is a predicate and not a count) | **ANSWERED, and the implementer did the half I could not check -- it corrected the figure TO XABIER and not only here** | I applied the predicate rather than a number: **89 reds, all 89 inside tests/test_report_carried.py (79) and tests/test_report_guard_states.py (10)**; the 17 carries_the_finding cases parametrised on exactly R845-R861; the 57 named_site cases on sites of R850-R861; ten survives_the_state cases whose inner runs read 77 failed, 160 passed, 1 skipped (two read 78) and name those. **And my set and CI's set are the SAME SET**: comm -23 and comm -13 over the two sorted id lists are both empty, 89 against 89. |
| **R855** (the suite was not run at a pushed reviewed commit, third occurrence; the implementer asks me to rule it once rather than keep deciding it) | **WITHDRAWN FOR A COMMIT THAT CARRIES NO REPORT REVISION, with one standing condition. Ruled once, in its own section below.** | The condition is met in this commit: it names the runs it made and states plainly that it has NOT measured the whole suite at this sha. An unmeasured green would be a different matter, and that section says what I would do about one. |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- C43, and there is no report revision in which it could be answered** | FR1's third class. Unchanged by this diff. |
| **R848** (the empty-directory refusal admits a bare dot, a dot-slash, a double dot and a padded dot) | **still open, untouched, correctly so** | `git diff 948b36a..HEAD -- floatfea` is floatfea/cli.py alone, and its two hunks are the constant and its use. Non-blocking, ruled three times. |
| **R849 with R854** (the caveat, disclaimer, provenance AND regeneration gates quantify over hard-coded three-file tuples, and step 3 publishes two more deliverables) | **still open, both sites, and it is the oldest live item FL2 lands on** | NAMES at tests/regression/test_r1_example_regenerates.py:51; ARTIFACTS at tests/regression/test_r1_published_artifacts.py:69. Answered WHILE step 3 is built, as verdict 9 ruled and verdicts 10 and 11 repeated. **R862 is the same species in a third place**, which is the reason to do it once rather than file by file. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **with Xabier, relayed verbatim, unchanged by this diff** | not the implementer's to repair in code. |
| **R856** (write_verdict.py refuses a step with no report) | **with Xabier; THIRD measured occurrence, in my command block above, with its refusal ORDER measured for the first time** | apparatus, not ledgered (FF0); the exit is a clause and not a commit. |
| **R835, R836** (EG3's enumeration; and R836) | **still open, still Xabier's; this commit is the TENTH measurement and it over-lists again** | run on their own rather than read off a cascade, which is EJ2's discipline: the two off-list state-(2) names give **24 passed in 0.29s**. Two of the enumerated names are green while seven fire. Relayed unchanged. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally AND on a machine neither of us controls** | mine: All checks passed! / 148 files would be left unchanged / Success: no issues found in 43 source files. CI run 39176380750, job `lint, unit and guards`, read at STEP level: actionlint SUCCESS, ruff SUCCESS, black --check SUCCESS, mypy SUCCESS, unit tests SUCCESS (186 passed in 163.91s), guards and meta-tests FAILURE. Every one RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried -- and I nearly filed a false sibling to it** | the em dash in _PROVENANCE_PATH and in the three published provenance lines is `e2 80 94`, U+2014, in BOTH files. My terminal rendered it as a replacement character and I was one step from writing a mojibake finding against a published deliverable; the bytes refuted it. Recorded because "verify the reference" is my own guard and this is the round it caught me rather than the code. |
| **C43, C44, C45** | **C43 and C44 carry; C45 unchanged and still unpayable before step 3's report exists** | verdict 10's process note stands, with verdict 11's correction to its baseline figure. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer and not the list. |
| **EG3(ii): the verdict commit measured** | **DONE at the reviewed commit; the measurement AT the verdict commit is owed to the next revision, as always, because I run before I write** | the two report-guard files hold 89 of the suite's 89 reds and the two id sets are identical to CI's, so no red sits outside the boundary. |
| scripts/suite_count.py's own line + CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer. |

## The R855 ruling, said once

**The implementer asked me to rule it rather than let it be re-decided every commit, and
that is the right request. R855 IS WITHDRAWN FOR A COMMIT THAT CARRIES NO REPORT REVISION,
with one standing condition.**

```
claim  nothing in the governing documents puts the whole suite on an interim COMMIT; ES0
       puts it on the interim CHECK, and the check is mine
cmd    CLAUDE.md, ES0's third bullet
out    "An interim check is light: the suite and CI at the commit, plus a CZ0 (a)-(d) scan
        of the diff since the last verdict."
       -- the subject of that sentence is the check
cmd    CLAUDE.md, section Step gating, item 1 -- where the implementer's own run IS required
out    "Write docs/reports/F<n>/step-<k>.md: what was built, the test counts from your own
        run ..."
       -- the obligation attaches to a REPORT, and an interim commit has none by FR3's
          own design
cmd    EG3(i), the clause R855 was argued from
out    "The PRE-INVOCATION GREEN REQUIREMENT is waived only if EVERY red traces by name to
        the step-boundary cause."
       -- it waives a requirement stated elsewhere; it does not create one, and the tree it
          speaks of is red by construction for the whole of step 3
cell   what the double run has bought where both halves were measured: verdict 10 ran the
       suite at e818375 against an implementer who had run a 400-case subset, and verdict
       11 at e6a20e3 against one who had run a single file
out    9 reds and 78 reds; in both, the whole suite's set and the two report-guard files'
       set were THE SAME SET, so nothing was hiding in either, and the reviewer's run
       produced the number both times. This commit is the third: 89 and 89, same set.
judge  **the information is never lost, because I run the suite at the reviewed commit by
       rule and I have no discretion to skip it.** A second sixteen-minute run inside the
       same turn boundary reaches no reader the first does not, and the loop pays for it
       twice at every turn against a 5 November date. **What I am NOT withdrawing is the
       claim discipline, and it is the whole of the condition:** a commit that has not
       measured the suite SAYS SO, as this one does, and never states or implies a green it
       did not take. An unmeasured green is a different finding with a different name --
       it is a claim with no command (BF0) about the one measure this loop cannot
       re-derive -- and I would hold the next revision on one.
       R855 stands unchanged for a commit that CARRIES a report revision (item 1's own
       words) and for a closure commit (CZ1 (ii)). It is withdrawn for an interim commit,
       and it is withdrawn by me rather than argued down by the implementer, which is the
       part of the record that matters.
rule   ES0 as written; CLAUDE.md Step gating item 1; EG3(i); and my own instruction to run
       the suite myself and never to accept a pass count from a report
```

## The sequencing question, answered from the hook's own text

**The implementer's premise is false, and that is the whole answer: five commits in ONE
TURN is ONE interim check, not five.**

```
claim  the hook fires at a TURN BOUNDARY on a TREE COMPARISON and has no notion of how
       many commits reached that tree
cmd    .claude/hooks/require-verdict.sh, the only comparison in the file that can refuse a
       step commit
out    if ! git diff --quiet "$reviewed" -- "$report" floatfea tests
             ':(exclude)tests/corpus' 2>/dev/null; then
         block "floatfea/, tests/, or $report changed since the verdict at $reviewed."
       -- a diff between two TREES. There is no commit walk and no commit count anywhere
          in the file; I read all of it.
cmd    the directive the implementer read as pointing the other way
out    docs/directives/FR.md, FR3: "Build ALL of it before the first reviewed revision.
       Interim checks run as the hook requires and count against no round."
       -- "all of it before the first reviewed REVISION" constrains the revision, not the
          commit, and the sentence after it anticipates interim checks in the plural
judge  **commit granularity is yours and it costs you nothing either way.** The number of
       interim checks is the number of turn boundaries. **I would rather have the five
       commits than the one**, and the reason is not reviewability in the abstract: three
       of the last four rounds' findings came from running the model at a configuration the
       commit did not choose, and with five commits each item's own diff tells me which
       configuration its author chose. One undifferentiated diff adding member topology,
       two optional analyses with a re-solve loop, a headings list with a refusal and a
       per-case band check gives me one surface and an ES0 scope that is light by rule.
       **But if the build is naturally one turn, make it one turn and as many commits as
       the work has shapes.** I will not spend a round on either choice, and I am not
       asking you to change the plan.
```

## Findings

**NOTHING BLOCKS.** The diff is one `floatfea/` refactor with no behavioural change and one
test file's comments. No tolerance moved. No published deliverable moved -- and I
established that by regenerating all three from this tree, not by reading the diff. Under
FR1 none of the four findings below can put a wrong number in front of anyone **at this
commit**, and for the two that could at a later one I name the number and what makes it
live.

**THE IMPLEMENTER'S OWN REQUEST IS WHERE TWO OF THE FOUR CAME FROM.** It asked me to check
independently that the refactor changed no published figure -- "the one thing I would least
like to have got wrong". The answer is that **the claim is true and the measurement offered
for it cannot see the thing it claims** (R864), and that the refactor's remainder is in the
copy nobody looked at (R862).

**R862. (DOES NOT BLOCK -- ledgered) "THERE IS NO SECOND COPY" IS REFUTED BY ONE GREP.
THREE HAND COPIES OF THE STAGE SET REMAIN AND ONE OF THEM COMPUTES THE PUBLISHED
`| total |`. The commit unified the WRITER and the EXCLUSION and left the PRODUCER. At
FL2's shape the published total understates the run by 40.000 s with both gates green.**

```
claim  the stage set still exists in three places the new constant does not reach
cmd    grep -rn 'for stage in ("build"' --include=*.py . and
       grep -rn '("build", "load", "solve", "code_check")' --include=*.py .
out    tests/regression/test_r1_example_golden.py:318
         for stage in ("build", "load", "solve", "code_check", "total"):   <- FIVE, a copy
       tests/regression/test_r1_example_golden.py:321
         parts = sum(result.timings[s] for s in ("build","load","solve","code_check"))
       floatfea/run/pipeline.py:673
         timings[k] for k in ("build", "load", "solve", "code_check") if k in timings
       -- the last of these IS the published `| total |` row
cmd    what the golden gate claims, in its own failure message
out    "`total` is ... and its parts sum to ...; the reported total must be the sum of the
        stages, not a separate measurement."
cell   FL2's shape, one variable moved: a sixth timed stage at 40.0 s, pipeline.py:673
       untouched, the REAL test_the_run_reports_a_wall_time_for_every_stage called on it
out    TODAY (five stages)     PASSED   published total 97.273 s, real 97.273 s
       a SIXTH timed stage     PASSED   published total 97.273 s, real 137.273 s
                                        -> understated by 40.000 s, and the gate whose own
                                           message is "total must be the sum of the
                                           stages" is GREEN
cmd    why the five-name copy at :318 cannot see it either
out    it asserts PRESENCE (`stage in result.timings`) over its own list, so a stage ADDED
       to the set is outside the collection the assertion inspects, by construction
rule   my own recorded guard, verbatim -- check that the collection the assertion inspects
       can actually contain the failure; FR1's first head, a wrong number in a report
judge  **it does not block at this commit, and I measured that rather than asserting it.**
       `| total | 97.27 |` is correct today: the five published rows are
       0.19 + 0.00 + 97.08 + 0.00 = 97.27, `grep -n "timings\[" pipeline.py` is five lines
       of which one IS total, so the four summands are the only timed stages, and the
       full-precision identity is green. **The silently wrong result it produces, for the
       record, is a published `| total |` row that is labelled the total and is not** --
       and it arrives from ONE new `timings[...] = ...` line, whether or not the new row is
       published, with test_the_run_reports_a_wall_time_for_every_stage certifying it.
       That is R860's own argument one level down: R860 said a hand copy cannot know, and
       the repair unified the copy that decides the COMPARISON and left the copy that
       decides the NUMBER. **At the commit that adds a timed stage this is a wrong number
       in a published deliverable and it blocks then.**
```

**Closed when** `floatfea/run/pipeline.py:673` derives its summands from `WALL_TIME_STAGES`
rather than restating four of them, and the two literals at
`tests/regression/test_r1_example_golden.py:318` and `:321` come from the same place -- at
the latest in the commit that adds a timed stage.

**R863. (DOES NOT BLOCK -- ledgered; it is the EH4 direction the repair opened) THE
EXCLUSION SET IS NOW DEFINED BY THE CODE UNDER TEST, SO A SIXTH PUBLISHED ROW IS EXEMPTED
SILENTLY. Measured: a sixth stage published AND named is green on 11 of 11 -- green even
when the shipped value is 4521.30 against a fresh 0.00.**

```
claim  the repair moves the exclusion's declaration from a place a reviewer reads to a
       place the generator decides, and the widening then needs no test-file diff
cell   the real gate's eleven cases, fresh side held fixed at my own 70.37 s regeneration,
       PUBLISHED redirected to a copy so the committed artifacts were never written
out    BASELINE (unmodified, HEAD as committed)                      11 passed,  0 failed
       a SIXTH stage in the TUPLE ONLY (the implementer's cell)      10 passed,  1 failed
         FAILED EXCLUSION_pin ('the SHIPPED report', [the five])
       a sixth stage PUBLISHED and NAMED (FL2's shape)               11 passed,  0 failed
       ... and its published value DIFFERS from the fresh run
           (| sizing | 4521.30 | against a fresh | sizing | 0.00 |)  11 passed,  0 failed
       RESTORED                                                      11 passed,  0 failed
cmd    the two configurations side by side, which is the whole of the finding
out    BEFORE this commit: widening the exemption meant editing `_TIMING_STAGES` in
         tests/regression/test_r1_example_regenerates.py -- a diff in a test file.
       AFTER: it means adding the name to WALL_TIME_STAGES in floatfea/cli.py, which is the
         SAME one-line change that makes the row publishable at all. The exemption becomes
         a side effect of the publication.
cmd    the row shape the exclusion keys on
out    r"^\|\s*(build|load|solve|code_check|total)\s*\|\s*[0-9.]+\s*\|\s*$"
       -- a NAME and a number. Nothing in it says "a time", and nothing says "inside the
          Wall time table".
cmd    whether a non-time quantity can reach an exempted row today, read rather than assumed
out    floatfea/run/pipeline.py:605, 653, 664, 669, 672 -- every member of the tuple is a
       time.perf_counter() delta, and the branches between them raise rather than return
cmd    the direction that is CLOSED, measured before I claimed the one that is open
out    an engineering `| total | 4521.30 |` row elsewhere in report.md  9 passed, 2 failed
         FAILED REGENERATES[report.md] -- 14 line(s) differ, 102 against 97
         FAILED EXCLUSION_pin -- (... ['total','total'])   the duplicate is caught
rule   EH4 -- the boundary is solved in the direction that WEAKENS the gate, and the
       injection rises until a clean case trips; my own guard that a gate carries its own
       failure
judge  **it does not block, and the reason is a measurement rather than a judgement of
       severity.** Every member of the tuple is a wall clock on every admissible config, so
       no engineering number is reachable through this door today, and a second occurrence
       of any of the five is caught by the pin. **What is reachable with no signal at all
       is a sixth wall clock** -- the thing R860 was about, in the direction R860 did not
       look. The repair is still the right one: before it the gate was machine-dependent,
       which is worse. **But the exclusion is no longer DECLARED, it is DERIVED, and a
       derived exemption cannot be reviewed in the diff that widens it.** Neither close
       below is new apparatus: anchor the regex to the `## Wall time` section so that an
       exempted row is exempt for WHERE it is; or state in the report, with the two green
       rows above, that adding a name to WALL_TIME_STAGES exempts a published row from
       comparison with nothing red, and that this is accepted for a wall clock.
```

**Closed when** an exempted row is exempt by its position in the `## Wall time` table rather
than by its name matching a tuple the generator controls -- or the report states that
widening with those two measurements beside it.

**R864. (DOES NOT BLOCK -- ledgered, FR1's third class) "THE REFACTOR PRODUCES BYTE-IDENTICAL
DELIVERABLES" IS TRUE, AND THE REGENERATION GATE CANNOT SEE IT EITHER WAY. The five lines
the refactor touches are the five it excludes: reordered, or with every value replaced, the
comparable-line lists are IDENTICAL and the pin is GREEN.**

```
claim  the witness offered for the claim is blind to the claim's own subject
cell   the gate's own _lines() and pin applied to the shipped report and to two mutations
       of it, one variable moved each, nothing regenerated
out    REORDERED (| total | first)      comparable lines identical: True   pin green: True
       ALL FIVE VALUES -> 999.99        comparable lines identical: True   pin green: True
cmd    the five single-value edits through the real eleven cases
out    | load | -> 999.99        11 passed       | total | -> 0.01      11 passed
       | code_check | -> 999.99  11 passed       | build | -> 999.99    11 passed
       | solve | -> 0.01         11 passed
cmd    the cell that DOES isolate the claim, which is the diff and not a run
out    git diff 948b36a..HEAD -- floatfea/cli.py: the five names and their order are
       unchanged, `_write_report`'s loop body is unchanged, and `if stage in
       result.timings` is unchanged. **That is the evidence, and it is sufficient.**
cmd    the independent half, which is stronger than the diff and which the implementer did
       not claim
out    the three artifacts were last written at 129747b, THREE commits before this refactor
       (git log --oneline -1 -- results/R1/example/), and my regeneration from THIS tree
       differs from them on 0 of 97, 0 of 1286 and 0 of 70 comparable lines, at
       governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
       -- a writer refactored at d89566d reproducing files written at 129747b is the
          statement that wanted making
cmd    and the claim as WORDED, tested
out    the deliverable is NOT byte-identical and never was: my run published
       `| solve | 70.20 |` against the shipped `| solve | 97.08 |`. It is identical on
       every COMPARABLE line, which is a different and true sentence.
rule   BF0 with BG0 -- a causal sentence carries the cell that isolates it, one variable
       moved; and my own guard that a residual destroys information, applied to a gate that
       drops the very lines it is being asked about
judge  **it does not block**: the claim is true, nothing in the deliverable moved, and I
       verified it by two routes. It is recorded for its shape, which is this project's own
       recurring one -- **the measurement cited for a claim excluded the claim's subject by
       construction.** The same constant's docstring says it is "the stages the published
       report's table carries, IN ORDER", and the order of that table is the one property
       of it nothing in the tree checks, which is the first measurement above.
```

**Closed when** the step's report states the claim as "identical on every comparable line,
and the five excluded rows are not compared in either direction", with the regeneration
against `129747b`'s artifacts as its command -- or drops the claim and cites the diff, which
is what actually carries it.

**R865. (DOES NOT BLOCK -- ledgered; R859's THIRD SITE, the one R859's own judge named) THE
DOCSTRING OF THE FUNCTION WHOSE COMMENT WAS CORRECTED STILL SAYS "A FOURTH NON-DETERMINISTIC
LINE REACHING THE DELIVERABLE REDDENS HERE INSTEAD OF BEING ABSORBED", AND IT IS FALSE IN
BOTH HALVES. The line is not absorbed, and this assertion cannot see it.**

```
claim  the pin's second assertion cannot fail in the direction the docstring claims for it
cmd    tests/regression/test_r1_example_regenerates.py:224-229, untouched by this diff
out    "This pins the excluded set by KEY in both the shipped and the fresh report, so a
        fourth non-deterministic line reaching the deliverable reddens here instead of
        being absorbed."
cell   a fourth provenance key injected into the shipped report, one line, nothing else
out    `# npz: /home/someone-else/junk/other_cases.npz`
       matched by _PROVENANCE_PATH : False      -> it is NOT absorbed
       excluded from the comparison: False
       comparable lines 97 -> 99                -> the COMPARISON reddens, loudly
       the pin's key set                        -> ['config','deck','load_cases'], GREEN
cmd    why it can never be otherwise, from the regex rather than from the run
out    ^(?:#\s*|\*\s+\*\*)(config|deck|load_cases)(?:\*\*)?\s*[:<em-dash>-]\s*(.+?)\s*$
       -- `keys` is drawn from that three-way alternation, so
          assert keys == ["config","deck","load_cases"] can fail only by OMISSION. A
          fourth key is outside the collection the assertion inspects.
rule   my own guard -- check that the collection the assertion inspects can contain the
       failure; CW0 -- prose in the source tree is a test, a triple, or deleted
judge  **it does not block**: the behaviour is the safe one, the red is loud, and no number
       moves. It carries because R859's judge named this docstring explicitly -- "the
       pre-existing docstring of that test has the same shape" -- and the comment eight
       lines below it was corrected while this was not. **The sentence is wrong in the
       direction that makes the gate sound stronger**, which is the direction R853, R857
       and R859 were each wrong in, in this same file, in three consecutive commits.
```

**Closed when** that docstring says which assertion fires for a fourth excluded line -- the
comparison, not the pin -- and says that the key assertion bounds omission only; or says
nothing and lets the five test functions speak.

## Try to break it -- what I ran, and what it found

* **One full regeneration of all three deliverables from this tree into a temporary
  directory**, with the fixture's own recipe: 70.37 s, `governing U = 1.71167 at
  platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)`, **0 differing comparable lines
  in all three files** at 97 / 1286 / 70. That is the control for everything below and the
  independent answer to the one thing the implementer asked me to check -- and it is a
  stronger answer than the diff, because the committed artifacts were written at `129747b`,
  three commits before this refactor.
* **Sixteen injections against the five real test functions**, fresh side held fixed, one
  edit each, with the gate's `PUBLISHED` root redirected to a copy so the committed
  artifacts were never written: baseline; a sixth stage in the tuple only; a sixth stage
  published and named; the same with a value differing by 4521.30 from the fresh run; an
  engineering `| total |` row elsewhere in the report; all five wall-clock values one at a
  time; the governing U; a duplicate `| total |`; a deleted `| code_check |`; a sixth
  unrecognised `| mesh |` row; a timing row in a CSV; and a restore.
  **Each of the gate's five functions was shown to carry its own failure by at least one
  red, and every injection was red somewhere except the rows the exclusion tolerates by
  design -- which is R863, and it now includes a sixth row nobody has published yet.**
* **Both EH4 directions on the thing the diff changed.** Strengthening: the pin requires
  exactly five rows, and I showed it cannot fail false by reading `pipeline.py` --
  `grep -rn "RunResult(" floatfea` is one construction, all five `timings[...]` are
  unconditional above it, and the branches between them raise rather than return.
  Weakening: the exclusion's membership now comes from the code under test (R863).
* **The gate's blindness to its own excluded rows, solved in the two directions the diff
  did not choose**: the five rows reordered, and all five values replaced -- identical
  comparable lines and a green pin in both. That is R864, and it is what makes the
  implementer's byte-identity claim true-but-unwitnessed rather than wrong.
* **A census of the stage set rather than a reading of the diff**, which is what found
  R862: three hand copies remain and one of them computes the published `| total |`. Then
  the FL2 cell on the real golden gate: a sixth timed stage, the published total 40.000 s
  short, and the gate that asserts the sum GREEN.
* **The fourth-provenance-key direction** of the pin, from the regex rather than from a
  run: the key assertion can fail only by omission (R865).
* **The 89 reds one id at a time**, with the cascade identified by its inner FAILED lists
  and by `[baseline]` being red rather than by its names, and the two off-list state-(2)
  names run on their own (24 passed).
* **The bytes of the one thing I was about to get wrong.** My terminal rendered the em dash
  in `_PROVENANCE_PATH` and in the three published provenance lines as a replacement
  character, and I was one command from filing a mojibake finding against a published
  deliverable. `e2 80 94` in both files. Recorded under C42.

**What I did not find, and it is the larger part.** The repair does what R860's condition
asked and the provenance is structural rather than inferred from a green: one definition in
`floatfea/cli.py`, one import, no tuple left in the test. The deliverables are unmoved and I
proved it against artifacts written three commits earlier rather than by reading the diff.
The pin's new strictness cannot fail false on any admissible config. R857's figure is right
at the third attempt and the file records all three versions, which is the behaviour BP0
wants and is rarer than it should be. R858's replacement sentence is true in the broad form
and not only in the two rows it names -- I checked the broad form. **All four of my findings
are in a copy, a derivation, a witness or a sentence; not one of them is a number in a gate
or in a deliverable at this commit.**

## CI at the reviewed commit: RED, 89 reds, ALL 89 traced to EG3 state (2)

```
cmd    gh run list --commit d89566d09019dc3bb744c3ad21e859d268ca21de
         --json conclusion,status,databaseId,workflowName
out    [{"conclusion":"failure","databaseId":39176380750,"status":"completed",
         "workflowName":"CI"}]
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is
          not a pass and I did not record one. The judged commit had a run because it was
          pushed first (FP1).
cmd    gh run view 39176380750 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         run_rung: ladder 1  1276 collected, 0 failed, 0 errored, 0 skipped
                   ladder 2    66 / ladder 3   314 / ladder 6   225 /
                   ladder 4   343 / ladder 5    87      -- all OK, all 0 failed
         -- 225 at e6a20e3 and 225 here, which is right: this commit adds no case
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 163.91s) /
         guards and meta-tests FAILURE (89 failed, 1056 passed, 1 skipped, 1 warning
                                        in 711.21s)
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39176380750 --log-failed, unique ids, matched against state (2)'s list
out    57  test_every_named_site_is_touched_or_declared[R850..R861-<site>]  -> state (2)
       17  test_the_report_carries_the_finding[R845..R861]                  -> state (2)
        1  test_the_CI_section_is_about_the_REVIEWED_commit                 -> state (2)
        1  test_the_Carried_table_is_what_the_generator_produces            -> state (2)
        1  test_the_generator_would_catch_a_row_under_the_wrong_number      -> state (2)
        1  test_the_report_carries_a_WHOLE_SUITE_count                      -> FC1
        1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW                   -> FC1
       10  test_the_guard_survives_the_state[baseline + 9]                  -> the cascade
       --- 57 + 17 + 1 + 1 + 1 + 1 + 1 + 10 = 89 exactly, with no remainder
cmd    the control that makes the trace a measurement rather than a classification: my own
       89 sorted against CI's 89, both directions
out    comm -23 (mine) (CI's)   (empty)
       comm -13 (mine) (CI's)   (empty)
       -- the SAME SET, id for id, on two machines and two operating systems
cmd    the cascade identified by its own failure lines rather than by its names (EH1)
out    each inner run reads "77 failed, 160 passed, 1 skipped" (two read 78) and names the
       report-guard ids above; the [baseline] state is red, which is EH1's other half
cmd    the two state-(2) names that did NOT fire, run on their own (EJ2, R835)
out    test_the_answered_verdict_is_the_NEWEST_one and
       test_a_carried_row_points_at_a_section_that_discusses_it  -> 24 passed in 0.29s
cmd    the one warning, traced rather than left as a count
out    numpy/linalg/_linalg.py:2784 RuntimeWarning: overflow encountered in dot, raised by
       tests/verification/rung1/test_corpus_configurations.py::
         test_the_corpus_entry_behaves_as_the_reviewer_recorded[orient_norm_overflow]
       -- a reviewer corpus entry whose whole purpose is to overflow a norm. Designed.
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with EH1, EJ2 and FC1; EG3(i) -- EVERY red traces
       by name or it is CZ1 (iv) unchanged
judge  **all 89 trace, and the waiver applies in full: CZ0 (d) / FR1's red-test head does
       not stand and CA2's HOLD is not reached.** The predicate, not a count (R861): every
       red is in one of the two report-guard files, and each names a finding or a site of
       the newest verdict or is a survives_the_state case whose inner list names those.
       Both FC1 reds are unclearable before step 3's report exists. Every step in the lint
       job RAN rather than being skipped behind an earlier red, which is what CZ1 (iii)
       exists to see, and mypy is green there, so the CI-only types-PyYAML red FP1 found
       has stayed fixed.
```

**Not CK2's exhausted-allowance state.** `runnerName` is null for all four jobs including
the two that SUCCEEDED, so an empty runner name cannot separate the states in this
repository and I did not use it. What separates them: both real jobs carry per-step
conclusions, real counts and five- and fifteen-minute durations (23:24:27Z -> 23:29:11Z and
23:24:28Z -> 23:39:46Z), and the two skipped jobs are the determinism workflow's own event
gate (CK0) with empty step lists at a zero-second duration, which arises from a designed
`if:` and not from an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree
was clean before and after I wrote this file.** Neither exception opens: this diff touches
no part of F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre
labels in `tests/verification/rung4/`, not about a wall-clock table. The last corpus commit
remains `ba1527e` (batch 47).

**I ran the recorded substitute, and both halves paid again:**

* **A regeneration check on a published deliverable, in both directions** -- all three R1
  artifacts regenerated from this tree and diffed line for line (0 differing at 97 / 1286 /
  70), then sixteen injections against the gate that guards them, plus the two mutations
  the diff did not choose (reorder, and all five values). It produced **R863 and R864**.
* **A continuum grid over the parameter space the decision rule guards** -- the stage-set
  axis this time, since that is the axis the diff moved: the set's SOURCE (restated vs
  imported), its SIZE (five, six-in-tuple-only, six-published-and-named), the value axis
  (`0.00`, `0.01`, `999.99`, `1234.00`, `4521.30`), the position axis (inside the table,
  elsewhere in the report, in a CSV), and the order axis. It produced **R862**, from the
  one point on the source axis nobody swept: the copies that are not the gate's.

**This is the seventh consecutive round in which the regeneration check's weakening
direction produced the round's findings.**

## Tolerances touched

**None.** No value, no form, no counter, no injection -- and I treated the EXCLUSION as a
tolerance under another name and ran EU1's adversarial case anyway.

```
cmd    git diff 948b36a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 948b36a..HEAD | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance|slack|epsilon"
out    "tolerance because the rows are two-decimal, and that is a threshold this gate has
        no business introducing."   -- an unchanged line moved by context, recording a
        DECLINED threshold. No value is introduced.
claim  the one thing in this diff that functions as a tolerance under another name is the
       EXCLUSION, and its FORM moved even though no value did
cmd    the form, before and after
out    before: a tuple DECLARED in the test file
       after:  the same five names IMPORTED from the code under test
rule   CLAUDE.md section Tolerances, its clause on anything that functions as a tolerance
       under another name; EU1 -- an interim check whose diff moves a value or a declared
       counter includes the adversarial case, the model run at a configuration the diff did
       not choose
judge  **EU1 does not attach by its own words** -- no value and no declared counter moves --
       **and I ran it anyway, because R694's lesson is that a value which does not move is
       the worst case and not the safest.** The configuration the diff did not choose is a
       sixth stage published and named, and it is R863: eleven of eleven green with a
       published value 4521.30 away from the fresh one. The diff's own cell chose the
       tuple-only case, which reddens. **A form change with no value change is exactly the
       shape EU1 was earned on**, and it is why I ran the model at three stage-set sizes
       rather than reading the grep.
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1 -- no `Closes:`
line, deliberately).** Step 3 remains open with all three reviewed revisions available.
Nothing blocks, so FR3's instruction stands and it is the only thing that matters this
week: **build the rest of FL2.**

1. **FL2, complete, before step 3's first reviewed revision (FR3).** Five items, none
   built: member topology from the config with the star as the default; `required_section`
   and `truss_sizing` in `floatfea run` with FM0's re-solve loop; the optional analyses off
   by default; headings as a list with the BEM refusal; the band check per case with
   out-of-band cases unable to govern. **This is the third commit of step 3 and all three
   have been spent on gate items the plan routes to the ledger.** I am recording the
   arithmetic and not a fault: FR0's date is 5 November, eighteen days out, five items.
2. **R862 IN THE COMMIT THAT ADDS A TIMED STAGE, not after it.** It is the one of my four
   that becomes a wrong number in a published deliverable, and `truss_sizing` with a
   re-solve loop is the thing that adds the stage. One derivation at
   `floatfea/run/pipeline.py:673`, and the two literals in
   `tests/regression/test_r1_example_golden.py` with it.
3. **R849 with R854, over TWO files, still answered WHILE step 3 is built**, and R862 makes
   it three places where the same set is restated. Two new deliverables are coming.
4. **R863, R864, R865 in the first reviewed revision**, each with its figure regenerated at
   that commit (CP3). R847, R848 unchanged; R850 is half paid and R851, R853, R857, R858
   are paid; R859 is paid at two of its three sites.
5. **R852 and R856 remain with Xabier**, relayed correctly this turn, and R835's tenth
   measurement with them. Neither R852 nor R856 is the implementer's to repair in code.
6. **R855 is withdrawn for interim commits, with the condition in its own section.** The
   whole-suite number at a reviewed commit is mine to produce, and I have produced it at
   all three commits of this step. A commit that has not measured it says so.
7. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 89
   reds identical to mine id for id on a different operating system, and all six ladder
   rungs green with rung 6 at the same 225 collected as before -- which is the right
   number for a commit that adds no case.
8. **The schedule.** FR0's 5 November stands and nothing has slipped against it yet. Step 3
   opened on 18 October; three commits in, FL2 is unbuilt by design under FR3. I am not
   re-opening the escalation FR0 answered. **The next progress statement is step 3's first
   reviewed revision (FR5), and the sequencing answer above says that revision may arrive
   on as many commits as the work has shapes, in one turn.**

**What this commit got right, and it is much the larger part.** It took R860 before FL2
rather than after, which was the whole reason the previous verdict named it, and it took it
in the form that removes a copy rather than the form that adds an assertion -- one
definition, one import, no tuple left in the test. It corrected a figure that had been wrong
twice and **recorded both wrong versions and why each was wrong**, which is what BP0 asks
for and what nothing in this repository would otherwise do. It replaced a false sentence
about the wall clock with a true one, and the true one is true in the broad form I tested
and not only in the two rows it cites. It corrected its own mechanism sentence to the
assertion that actually fires. **And it asked me to check the one thing it least wanted to
have got wrong, which is how two of my four findings exist**: the byte-identity claim is
true, its witness is blind, and the copy that decides the published number was never in the
diff.

---

<!-- EARLIER ROUNDS, VERBATIM. Hand-appended in the form
     scripts/write_verdict.py uses, under DX2: each round is added and no prior
     round is rewritten or removed. The tool refused this step (R856). -->

# Review — R1 step 3
Reviewed commit: e6a20e330fa1afc91fdc32b3d4eb3292f45898a2
**Reviewed commit: `e6a20e330fa1afc91fdc32b3d4eb3292f45898a2`.**
Verdict: PASS
Tests: 3547 passed, 78 failed, 1 skipped   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK, the second in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **Nothing
blocks.** Three of the four gate findings verdict 10 ledgered are repaired, and I verified each
by my own injections rather than by reading theirs; five findings below, none blocking.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1",
`docs/directives/FR.md`). For each finding I say the silently wrong result it would produce, or
that it produces none. **This file is HAND-WRITTEN because the one sanctioned path in refused it
again -- R856, second occurrence, measured below.**

```
cmd    git diff --name-status 0aa0c4a..HEAD
out    M  tests/regression/test_r1_example_regenerates.py
       -- one file, 68 insertions, 5 deletions, nothing else
cmd    git diff --stat 0aa0c4a..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff 0aa0c4a..HEAD -- floatfea
out    (empty)                                   -- FR1 head (a) is unreachable from this diff
cmd    git diff 0aa0c4a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 0aa0c4a..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
cmd    git diff 0aa0c4a..HEAD -- results scripts docs
out    (empty)                                   -- no published deliverable moved
cmd    printf <the four mandatory sections> | python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       EXIT=1                                    -- R856, unchanged and unchangeable here
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report, so
there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`), and two
verdicts are newer than it. That is EG3 state (2) by definition, and it is the whole of this
tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R850** (the wall-clock exclusion covered three of the five rows the generator writes; and no check reads a published wall-clock value) | **HALF ANSWERED. The five-stage half is repaired and I verified it in both EH4 directions. THE PROSE HALF IS UNTOUCHED AND STILL FALSE -- see R858.** My closing condition named two things, and "half of an item is not the item" is CLAUDE.md's own sentence. | Repaired: `_TIMING_STAGES` feeds both the regex and the pin, so those two cannot drift apart. Verified by me: `| load |` and `| code_check |` set to `999.99` are now green (both were inside the byte comparison before); a DUPLICATE `| total | 1234.00 |` row reddens the pin; a MISSING `| code_check |` row reddens the pin; a timing-shaped row reaching a CSV reddens `test_R845_the_CSVs_carry_NO_excluded_timing_row`. **So the widening is bounded in all three files, which is the question the implementer asked me.** Still open: the claim that both excluded classes "ARE CHECKED SEPARATELY", while nothing in the tree reads a published wall-clock value. |
| **R851** (`_provenance` returned a dict so a duplicate `# deck:` line collapsed; the key-set pin read `report.md` alone) | **ANSWERED, and I reproduced my own exact injection against the repair rather than taking its counter-cases** | `_provenance_lines` and `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE` in the same file. My verdict-10 injection -- a second `# deck:` line with the SAME basename and a different directory, green before -- now reddens, in utilisation.csv and in report.md, **and reddens exactly one case** (the new one), which is the measurement that says the repair and not something else caught it. Two evasions I had not tried are caught as well, by different tests: `# Deck:` (capital, unmatched by the exclusion) falls into the byte comparison; `#deck:` with no space is caught by the new test AND by the basename test. The FRESH half of the new test is live -- injecting into the regenerated side alone reddens it. |
| **R853** (the published "102, 1289 and 73 comparable lines" did not reproduce) | **ANSWERED IN FORM, WRONG IN SUBSTANCE -- the corrected figure is correct against the rule the SAME COMMIT deleted. See R857.** | The commit took my 99/1286/70 and published it while widening the exclusion from three stage rows to five, which makes the report's comparable count 97. BP0 names this exactly: when a decision rule changes, every figure citing the old rule is regenerated in the same commit. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **relayed to Xabier by the implementer, correctly, and unchanged by this diff** | Mine, not the implementer's to repair in code. No new measurement this round. |
| **R856** (`write_verdict.py` refuses a step with no report) | **relayed to Xabier, and this is its SECOND measured occurrence** | the refusal is in my command block above. Under FF0 it is apparatus and not ledgered; the exit remains a clause, not a commit. |
| **R855** (the suite was not run at a pushed reviewed commit, and the tree's reds were not recorded with their cause named) | **STILL OPEN, third commit running. The implementer ran one file and asked whether the light scope requires the full run. IT DOES. I ran it: 78 failed, 3547 passed, 1 skipped in 966.33 s, every red traced below one id at a time.** | The offer to produce it rather than argue the scope is the right instinct and I am recording that; the answer is that ES0's light scope is the suite, and EG3(i) makes the waiver conditional on a trace that is pasted. **And the baseline I gave for that trace was wrong within one commit -- R861.** |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- C43, and there is no report revision in which it could be answered** | FR1's third class. Unchanged by this diff. |
| **R848** (the empty-directory refusal admits a bare dot, a dot-slash, a double dot and a padded dot) | **still open, untouched, correctly so** | `git diff 0aa0c4a..HEAD -- floatfea` is empty. Non-blocking, same class as R843. |
| **R849 with R854** (the caveat, disclaimer, provenance AND regeneration gates quantify over hard-coded three-file tuples, and step 3 publishes two more files) | **still open, both sites, and now with a second reason to be done before FL2 lands** | the two constants are `NAMES` in the regeneration gate and `ARTIFACTS` in the published-artifacts gate. Answered WHILE step 3 is built, as verdict 9 ruled. R860 below gives the same item its sharper reason. |
| **R835, R836** (EG3's enumeration; and R836) | **still open, still Xabier's; this commit is the ninth measurement of the enumeration** | and it over-lists again: of state (2)'s enumerated names, seven fire and two (`test_the_answered_verdict_is_the_NEWEST_one`, `test_a_carried_row_points_at_a_section_that_discusses_it`) are green. Relayed unchanged. |
| **C29, C34, C35** (`ruff`, `black`, `mypy`) | **green at this commit, locally AND on a machine neither of us controls** | mine: `ruff` `All checks passed!`; `black` `148 files would be left unchanged`; `mypy` `Success: no issues found in 43 source files`. CI run 39173178232, job `lint, unit and guards`, step level: `actionlint` SUCCESS, `ruff` SUCCESS, `black --check` SUCCESS, `mypy` SUCCESS, `unit tests` SUCCESS (`186 passed in 164.24s`). Every one RAN rather than being skipped behind an earlier red. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | not repaired here. |
| **C43, C44, C45** | **C43 and C44 carry; C45 is unchanged and still unpayable before step 3's report exists** | see verdict 10's process note, which stands except for its baseline figure (R861). |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| **The R850/R851/R853 ROUTING QUESTION the implementer asked me to check** | **ANSWERED: half right. EK2 governs the FORM of a repair and these repairs honour it; it is not a route that pre-empts the ledger, and FF0 does not reach this file.** | See the routing ruling below. No repair has to be undone. |
| **EG3(ii): the verdict commit measured** | **DONE, by me, at this commit** | the two report-guard files at e6a20e3: **78 failed, 165 passed, 1 skipped**, which is the same 78 as the whole suite's and the same 78 as CI's, id for id. |
| `scripts/suite_count.py`'s own line + CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer. |

## The routing ruling

**The implementer asked for the classification to be checked as hard as the repairs, so it is
checked here and not glossed.** The answer is that it is half right, and nothing has to be
undone.

```
claim  EK2 is a constraint on the FORM of a repair, not a route that pre-empts the ledger
cmd    CLAUDE.md, the clause EK2 is cited from
out    "No new apparatus through F6. ... An existing guard that fails false is fixed or
        deleted, never extended."
       -- it says what a repair may be. It says nothing about when, or about the ledger.
claim  FF0's route does not reach this file
cmd    CLAUDE.md section "What blocks, and what is a closure item (CZ0)", the FF0 paragraph
out    "Anything that reads the gating record, or decides whether a green is believed -- the
        report guards, scripts/ci_section.py, scripts/suite_count.py, .claude/hooks/, the EG3
        lists -- is fixed in the next commit."
       -- tests/regression/test_r1_example_regenerates.py decides whether a PUBLISHED
          DELIVERABLE is believed. It reads no gating record and no green. Not FF0's class.
claim  the locked plan routes a non-blocking interim finding to the ledger, by name
cmd    docs/milestones/R1.md, step 3's paragraph
out    "Only FR1-blocking items from those checks are fixed in flight; everything else is
        ledgered. That ordering is the directive's answer to the measurement both reviewers
        reached independently -- the repairs were one line each and the rounds were the cost."
rule   FR1 -- R850, R851 and R853 were each ruled NON-blocking in verdict 10, so the plan's
       sentence routes all three to the ledger
judge  **the repairs are sound and I would rather have them than not; the route was the
       ledger.** Three consequences, and they are bookkeeping rather than rework. (i) EK2's
       form is honoured and conspicuously so: the set is NAMED rather than the comparison
       given slack, and the 0.02 tolerance I proposed against myself was declined -- that is
       the right call and it is the opposite of widening. (ii) R850, R851 and R853 stay on the
       R1 ledger as PAID EARLY, R850 as HALF paid, so the closure list does not lose them.
       (iii) The cost is the one the plan's sentence predicts: this is the second commit of
       step 3, and FL2 has five items with none of them built, against FR0's 5 November. The
       implementer says so plainly and claims none of it, which is the correct thing to have
       done; I am recording the arithmetic rather than a fault.
```

## Findings

**NOTHING BLOCKS.** The diff is one test file. No `floatfea/` line moved, no tolerance moved,
no published deliverable moved -- and I established the last of those by regenerating all three
artifacts twice rather than by reading the diff. Under FR1 none of the five findings below can
put a wrong number in front of anyone, and I say which for each.

**R857. (DOES NOT BLOCK -- ledgered) R853'S REPAIR REPUBLISHED R853'S DEFECT. The corrected
figure `99, 1286 and 70 COMPARABLE lines` in the exclusion comment was measured against the
THREE-stage exclusion that THIS COMMIT deleted. Under the shipped five-stage rule the report's
comparable count is 97. The two CSV figures are right.**

```
claim  the figure the file publishes as "the measurement that says the numbers are reproduced"
       is not a measurement of the rule the file now runs
cmd    the gate's own `_lines()` applied to the three shipped files, at this commit
out    report.md          total  105   comparable  97   timing-excluded 5   prov-excluded 3
       member_forces.csv  total 1289   comparable 1286  timing-excluded 0   prov-excluded 3
       utilisation.csv    total   73   comparable  70   timing-excluded 0   prov-excluded 3
cmd    the same three files under the regex this commit DELETED, (build|solve|total)
out    report.md 99, member_forces.csv 1286, utilisation.csv 70
       -- 99 is exactly the old rule's answer, which is where the published figure came from
cell   one variable moved and nothing else: the same `_PROVENANCE_PATH`, the same three files,
       the same `_lines`, the stage tuple three names versus five
out    99 -> 97 on report.md, 1286 -> 1286, 70 -> 70
cmd    what the gate's own failure message prints when it reddens, so the contradiction is
       inside the file rather than inferred
out    "report.md is not what this tree regenerates: 1 line(s) differ, shipped has 97
        comparable lines against 97"   -- from my injection of U = 0.99999
rule   BP0 -- when a decision rule changes, every figure citing the old rule is regenerated or
       withdrawn IN THE SAME COMMIT; CP2 -- a repair carries no new numeric claim outside a
       triple; and my own recorded guard that a reference is verified independently of the
       thing it measures
judge  **it does not block.** 97 against 99 is a claim about the gate's reach, not a number in
       a gate, a CSV, a report or a published deliverable: nothing asserts on it, and a reader
       of a RED is told 97 by the assertion message itself. No silently wrong result follows,
       so it is FR1's third class. **It is recorded because of what it is an instance of.**
       R853 was "a figure that is the total minus the wrong exclusion"; its repair is "a figure
       measured against the exclusion the same commit replaced". The attention went to the
       thing being fixed and the number written around the fix inherited none of the discipline
       being applied to it -- which is CP2's own sentence, and CZ0's: the highest-value finding
       in two of this project's rounds was a defect inside the repair of the previous finding.
```

**Closed when** the comparable counts in that comment are those of the rule the file actually
runs -- 97, 1286, 70 -- regenerated at the commit that publishes them (CP3), or the figure is
withdrawn and the claim left qualitative.

**R858. (DOES NOT BLOCK -- ledgered; it is the OPEN HALF of R850) THE FILE STILL ASSERTS THAT
BOTH EXCLUDED CLASSES "ARE CHECKED SEPARATELY", AND NOTHING IN THE TREE READS A PUBLISHED
WALL-CLOCK VALUE. The repair made that sentence LESS true, not more: the exclusion went from
three tolerated rows to five.**

```
claim  the file's own declared discipline is false for one of its two excluded classes
cmd    the header comment of tests/regression/test_r1_example_regenerates.py, first paragraph
out    "TWO DECLARED CLASSES OF LINE ARE EXCLUDED FROM THE BYTE COMPARISON, AND BOTH ARE
        CHECKED SEPARATELY. An excluded line is a line nothing checks unless something else
        checks it."
cell   my injections against the real gate's five test functions, the fresh side held fixed at
       my own 68.82 s regeneration, one edit each
out    CONTROL unmodified                                11 passed,  0 failed
       | load | 0.00 |       -> | load | 999.99 |        11 passed,  0 failed   <- GREEN
       | code_check | 0.00 | -> | code_check | 999.99 |  11 passed,  0 failed   <- GREEN
       -- before this commit both of these were COMPARED. The repair is right and the
          sentence describing it is now wrong about five rows instead of three.
cmd    whether anything anywhere reads a published wall-clock value
out    nothing. The provenance class has `test_R845_the_PROVENANCE_values_agree_by_BASENAME`
       and, since this commit, `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE`. The
       wall-clock class has no counterpart, by design and correctly -- I proposed the sum
       identity against myself in verdict 10 and withdrew it, and the commit records that
       withdrawal in the same comment, which is the right thing to have written down.
rule   CW0 -- prose in the source tree is a test, a triple, or deleted; and the closing
       condition of R850, which named this site
judge  **it does not block**: a wall-clock second is not a number anyone sizes steel against,
       and FR1's third class covers the sentence. It carries because R850's closing condition
       named two things and one of them was done. The repair I asked for is five words -- the
       wall-clock VALUES are excluded and unchecked -- plus the observation that the pin and
       `test_R845_the_CSVs_carry_NO_excluded_timing_row` bound WHERE they may appear rather
       than WHAT they say. That is the honest description of a structure that is, in fact,
       honest, and I measured its bound in both directions.
```

**Closed when** that paragraph says of the wall-clock class what the two green rows above say,
and the commit message's "BOTH are checked elsewhere rather than merely dropped" is corrected
with it.

**R859. (DOES NOT BLOCK -- ledgered) THE NEW COMMENT NAMES THE WRONG ASSERTION. It says a sixth
stage row "reddens HERE rather than being absorbed", where HERE is the key-set pin. It reddens
the byte comparison; the pin stays green. The pin catches a DUPLICATE of a named stage and a
MISSING one -- which it does, and that is the stronger property.**

```
claim  the mechanism sentence attached to the repair is not the mechanism
cmd    the comment above the pin's `assert stages == sorted(_TIMING_STAGES)`
out    "ALL FIVE STAGES `cli.py` WRITES (R850), so a sixth reddens here rather than being
        absorbed, and so `load` and `code_check` stop sitting inside the byte comparison"
cell   one injection at a time into the shipped report, every other input held
out    | mesh | 3.00 | added                     10 passed, 1 failed
         FAILED REGENERATES[report.md]: "16 line(s) differ, shipped has 98 comparable lines
         against 97"                            -- the COMPARISON, and the pin is GREEN
       | total | 1.2e3 | added                   10 passed, 1 failed
         FAILED REGENERATES[report.md]          -- scientific notation is unmatched by the
                                                   digit-and-dot class, so it is compared,
                                                   which is the safe direction
       a DUPLICATE | total | 1234.00 | row       10 passed, 1 failed
         FAILED EXCLUSION_pin: ('the SHIPPED report', [... 'total', 'total'])   <- THE PIN
       the | code_check | row DELETED            10 passed, 1 failed
         FAILED EXCLUSION_pin: ('the SHIPPED report', ['build','load','solve','total'])
       | total | 5.00 | added to utilisation.csv 10 passed, 1 failed
         FAILED CSVs_NO_timing_row: "shipped utilisation.csv carries a timing row"
rule   BG0 -- a causal sentence carries the cell that isolates it; CW0; and my own recorded
       guard that a gate carries its own failure, asked of each of the five functions
judge  **it does not block** -- no number moves, and every one of those injections is red
       somewhere, so the gate is sound and only its description is wrong. The same error is in
       the report I was given ("a | mesh | row added -- a SIXTH row reddens the pin"), and the
       pre-existing docstring of that test has the same shape ("a fourth non-deterministic
       line ... reddens here"). **What the measurement shows is better than the claim**: a
       stage row can only be swallowed if it is one of exactly five names, in report.md,
       exactly once each -- a duplicate reddens the pin, a missing one reddens the pin, a sixth
       name reddens the comparison, and one in a CSV reddens the CSV test. That is the answer
       to "is the exclusion now too wide": **five tolerated rows, in one file, pinned by name
       and by count -- and the | mesh | case was not what bounded it.**
```

**Closed when** those two comments say which assertion fires for which class of intrusion, or
say nothing and let the five test functions speak.

**R860. (DOES NOT BLOCK -- ledgered, and it is the one of the five that step 3 is about to walk
into) `_TIMING_STAGES` IS A HAND COPY OF THE LITERAL TUPLE AT `floatfea/cli.py:297`, AND NOTHING
COMPARES THEM. R850 WAS THAT DRIFT. The repair removes the drift between the regex and the pin
and leaves the drift that caused it.**

```
claim  the repaired gate restates the generator's stage set in a second place instead of
       reading it from the one place it is defined
cmd    grep -rn "_TIMING_STAGES" --include=*.py .
out    tests/regression/test_r1_example_regenerates.py -- three hits: the tuple, the regex and
       the pin. All in the test file; nothing reads cli.py and nothing asserts equality.
cmd    the generator's own definition
out    floatfea/cli.py:297   for stage in ("build", "load", "solve", "code_check", "total"):
       -- a literal inside a function body; grep for a module-level STAGE constant in
          floatfea/ returns nothing
cmd    the sentence this leaves unchecked, which is a claim about the code in a comment
out    "floatfea/cli.py:297 writes build, load, solve, code_check, total."
       -- true today; nothing in the tree would notice it becoming false
cmd    whether the pin's new strictness can fail false instead, which is the direction that
       worried me more -- the generator guards its own loop with `if stage in result.timings`,
       so it contemplates a missing stage
out    floatfea/run/pipeline.py:605, 653, 664, 669, 672 -- all five assignments are
       unconditional on any run that returns a RunResult, and `_utilisations` is called
       unconditionally just above the code_check stamp. **So requiring all five rows cannot
       fail false on an admissible config today**, and I measured that rather than inferring it
       from the defensive guard.
rule   my own recorded guard -- provenance, not existence: that a value reaches the assertion
       through the thing that defines it is asserted structurally, not inferred from a passing
       test; EK2 -- a guard that fails false is fixed, and this is that fix one level up
judge  **it does not block.** The failure mode is a FALSE RED, which is loud, and the five
       names agree today -- CI's ladder 6 went 222 -> 225 collected with 0 failed, so the
       repair is green on a machine neither of us controls. **It carries because step 3 is the
       commit that makes it live.** FL2 adds `required_section` and `truss_sizing` to
       `floatfea run` with FM0's re-solve LOOP; a sizing loop that times itself adds a sixth
       stage to `result.timings` and a sixth row to that table, and the next sub-10-ms
       two-decimal row inside the byte comparison is R850 verbatim, in the step whose own gate
       is the thing that adds it. Two cheap closes, neither of them new apparatus: `cli.py`
       names the tuple as a module constant and the test imports it, or the pin asserts the
       gate's set against the generator's. The first also turns that comment sentence into a
       fact the tree holds.
```

**Closed when** the stage set reaches the regex and the pin from the one place the generator
defines it, or an assertion in the existing file compares the two sets.

**R861. (DOES NOT BLOCK -- it is a CORRECTION TO MY OWN VERDICT 10, and the implementer has
already relayed the wrong number) THE BASELINE OF NINE REDS WAS WRONG WITHIN ONE COMMIT OF MY
WRITING IT. The tree is at 78, and VERDICT 10 IS THE CAUSE: two of the report guards are
parametrised over the NEWEST VERDICT's findings and sites, so the baseline is a function of what
I write, not of what the implementer commits.**

```
claim  the number I told the implementer to trace against is not a constant
cmd    python -m pytest -q --tb=no -rf        (mine, at e6a20e3, tree clean)
out    78 failed, 3547 passed, 1 skipped in 966.33s (0:16:06)
cmd    verdict 10's own instruction, in this file below
out    "for the rest of step 3 the baseline is nine reds, every interim check traces against
        it one id at a time, and a tenth red is CZ1 (iv) unchanged"
cell   collection counted per file at both commits, in a worktree at e818375, nothing else
       moved
out    tests/regression/test_r1_example_regenerates.py     8 -> 11   (+3, the new test)
       tests/test_collected_set_golden.py                 77 -> 78   (+1, see below)
       tests/test_report_carried.py                      304 -> 221  (-83)
       tests/test_report_guard_states.py                  23 -> 23
       whole suite                                      3705 -> 3626  (-79, fully attributed)
       -- the -83 is `test_every_named_site_is_touched_or_declared` and
          `test_the_report_carries_the_finding`, parametrised over the newest verdict's sites
          and findings. Verdict 9 named a larger set and step 2's third revision ANSWERED it;
          verdict 10 names 12 findings and 51 sites and no report answers it, so 63 cases went
          from green to red while the parametrisation itself shrank.
cmd    the +1, so the delta is attributed and not rounded off
out    tests/test_collected_set_golden.py::test_every_test_name_cited_in_prose_exists gains the
       citation of `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE` in the new helper's
       docstring, and it PASSES -- the "every citation resolves" guard working on this commit's
       own prose
cmd    the control that says nothing outside the two report-guard files is red
out    python -m pytest -q --tb=no tests/test_report_carried.py tests/test_report_guard_states.py
       78 failed, 165 passed, 1 skipped in 162.59s
       -- 78 in the whole suite and 78 in those two files is the same 78, so the other 3382
          collected cases are green. That is the statement that protects the trace, and it is a
          predicate rather than a count.
rule   EG3(i) -- every red traces BY NAME or it is CZ1 (iv) unchanged; EH1 -- the cascade is
       identified by the baseline being red and by each cascading state's own failure line; and
       C89's recorded lesson, that a tree red by design is a tree in which the next real red is
       harder to see
judge  **it does not block, and it is mine rather than the implementer's.** The operative
       correction, because the implementer will otherwise apply the wrong rule next commit:
       **"a tenth red is CZ1 (iv)" is WITHDRAWN.** The test is not a number. It is: every red
       is in `tests/test_report_carried.py` or `tests/test_report_guard_states.py`, and each
       either names a finding or a site of the newest verdict, or is a
       `test_the_guard_survives_the_state` case whose own inner FAILED list names those. A red
       that fails that predicate is CZ1 (iv) whether it is the tenth or the seventy-ninth.
       **And the count will move again at every verdict I write, including this one, because I
       am its input** -- which is the part worth keeping: a baseline whose value depends on the
       reviewer's own output cannot be handed to the implementer as a number.
```

**Closed when** nothing: it is a correction to a verdict, recorded so that the next commit
traces against the predicate rather than against nine.

## CI at the reviewed commit: RED, 78 reds, ALL 78 traced to EG3 state (2)

```
cmd    gh run list --commit e6a20e330fa1afc91fdc32b3d4eb3292f45898a2
         --json conclusion,status,databaseId,workflowName
out    [{"conclusion":"failure","databaseId":39173178232,"status":"completed",
         "workflowName":"CI"}]
       -- the run was IN PROGRESS when I began and I waited six polls for it. An unfinished
          run is not a pass and I did not record one.
cmd    gh run view 39173178232 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1  1276 collected, 0 failed / ladder 2  66 / ladder 3  314 /
         ladder 6  225 collected, 0 failed  (222 at e818375, so the THREE new cases ran and
                                             passed on a Linux runner) /
         ladder 4  343 / ladder 5  87
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 164.24s) / guards and meta-tests FAILURE
         (78 failed, 1050 passed, 1 skipped in 693.69s)
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39173178232 --log-failed, the unique ids, matched against state (2)'s list
out    51  test_every_named_site_is_touched_or_declared[R850..R856-<site>]   -> EG3 state (2)
       12  test_the_report_carries_the_finding[R845..R856]                   -> EG3 state (2)
        1  test_the_CI_section_is_about_the_REVIEWED_commit                  -> EG3 state (2)
        1  test_the_Carried_table_is_what_the_generator_produces             -> EG3 state (2)
        1  test_the_generator_would_catch_a_row_under_the_wrong_number       -> EG3 state (2)
        1  test_the_report_carries_a_WHOLE_SUITE_count                       -> FC1
        1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW                    -> FC1
       10  test_the_guard_survives_the_state[baseline + 9]                   -> the cascade
       --- 51 + 12 + 1 + 1 + 1 + 1 + 1 + 10 = 78 exactly, with no remainder
cmd    the cascade identified by its own failure lines rather than by its names (EH1)
out    each inner run reads "66 failed, 154 passed, 1 skipped in 4.1-4.5s" and names
       test_the_report_carries_the_finding[R845] first; one reads 67 failed. The [baseline]
       state is red, which is EH1's other half.
cmd    the two state-(2) names that did NOT fire, so the enumeration is measured rather than
       assumed (R835)
out    test_the_answered_verdict_is_the_NEWEST_one                PASSED
       test_a_carried_row_points_at_a_section_that_discusses_it   all PASSED
       -- the enumeration over-lists here, for the ninth time
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with EH1, EJ2 and FC1 -- state (2) is the
       verdict-written-report-not-yet boundary and it is designed; EG3(i) -- the waiver is
       conditional on the trace and the trace is pasted
judge  **all 78 trace, and the waiver applies in full: CZ0 (d) does not stand and CA2's HOLD is
       not reached.** I measured that rather than classifying it, and the control that makes it
       a measurement is the one in R861: the whole suite's 78 and the two report-guard files'
       78 are the same 78, so no red sits outside the boundary set. Every step in the lint job
       RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to
       see, and mypy is green there, so the CI-only types-PyYAML red FP1 found has stayed
       fixed. **The judged commit had a run because it was pushed first (FP1).**
```

**Not CK2's exhausted-allowance state, and the usual discriminator does not work here.**
`runnerName` is null in this repository's API output for ALL FOUR jobs including the one that
SUCCEEDED, so an empty runner name cannot separate the states on this project and I did not use
it. What separates them: both real jobs carry per-step conclusions, real counts and fifteen-
and ten-minute durations (22:39:22Z -> 22:54:19Z, 22:39:23Z -> 22:49:04Z), and the two skipped
jobs are the determinism workflow's own event gate (CK0) with empty step lists at a zero-second
duration -- which arises from a designed `if:` and not from an unstarted runner.

## Try to break it -- what I ran, and what it found

* **Two full regenerations of all three deliverables from this tree into temporary
  directories**, with the fixture's own recipe: 68.82 s and 70.55 s, `governing U = 1.71167 at
  platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)` both times, and **0 differing
  comparable lines in all three files** at 97 / 1286 / 70. That is the control for everything
  below and the fifth and sixth independent machine states for the wall clock.
* **Eighteen injections against the five real test functions**, fresh side held fixed, one edit
  each, with the gate's `PUBLISHED` root redirected to a copy so the committed artifacts were
  never touched: baseline; a sixth `| mesh |` row; `| load |` and `| code_check |` at `999.99`;
  a duplicated `| total |` row carrying an engineering-sized number; a deleted `| code_check |`
  row; a timing-shaped row in a CSV; `| total | 1.2e3 |`; duplicate `# deck:` lines with a
  DIFFERENT basename in all three files; duplicate `# deck:` lines with the SAME basename in
  two (my own verdict-10 green, now red); the same duplicate on the FRESH side only; `# Deck:`
  with a capital; `#deck:` with no space; and the governing `U` control. **Every one of the five
  test functions was shown to carry its own failure by at least one red, and every injection
  was red somewhere except the two rows the exclusion now tolerates by design.**
* **Both EH4 directions on the thing I was asked to attack.** The weakening direction: the
  exclusion is two rows wider than it was and no check reads a tolerated value (R858). The
  strengthening direction: the pin now requires EXACTLY five rows, so a duplicate or a missing
  one reddens it -- and I checked that this new strictness cannot fail false by reading
  `pipeline.py` rather than trusting the generator's defensive `if stage in result.timings`.
* **The comparable-line counts recomputed under both rules**, which is what found R857, and the
  per-file collection delta recomputed in a worktree at `e818375`, which is what found R861 and
  attributed all 79 of it.
* **The 78 reds one id at a time**, with each cascading state's inner FAILED list read rather
  than inferred from its name, and the two enumerated state-(2) names that do NOT fire named.

**What I did not find, and it is the larger part.** The R851 repair closes my own injection
exactly, in all three files, on both sides, with precisely one new case firing -- and two
evasions I invented afterwards are caught as well, by two different tests. The R850 repair
removes a real machine-dependent false red, derives the regex and the pin from one tuple, and
**declines the tolerance I offered it**, recording the refusal in the comment so that a later
reader does not re-propose it; that paragraph is the best thing in the diff. `ruff`, `black`,
`mypy`, 186 unit tests and all six ladder rungs are green, locally and in CI, and the three new
cases ran and passed on a Linux runner. Nothing in `floatfea/` moved and no deliverable moved.
**All five of my findings are in a figure, a sentence or a structural provenance -- not one of
them is a number in a gate.**

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree was
clean before and after I wrote this file.** Neither exception opens: this diff touches no part
of F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about a published-artifact comparison. The last corpus commit
remains `ba1527e` (batch 47).

**I ran the recorded substitute, and both halves paid:**

* **A regeneration check on a published deliverable, in both directions** -- two independent
  full regenerations of all three R1 artifacts, diffed line for line, then eighteen injections
  against the gate that guards them. It produced **R857, R858 and R859**.
* **A continuum grid over the parameter space a decision rule guards** -- the exclusion's own
  space this time: the stage-name axis (three names, five names, a sixth name, a duplicate, a
  deletion), the value axis (`0.00`, `0.01`, `999.99`, `1234.00`, `1.2e3`), the file axis (all
  three artifacts), and the provenance axis (basename, directory, duplicate, capital, no space,
  fresh side). It produced **R860**, from the one axis the diff did not vary: WHERE the stage
  set comes from.

**This is the sixth consecutive round in which the regeneration check's weakening direction
produced the round's findings.**

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff 0aa0c4a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 0aa0c4a..HEAD | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance|slack"
out    "tolerance because the rows are two-decimal, and that is a threshold this gate has no
        business introducing. The reviewer proposed it against itself and withdrew it; I am
        recording that so the next reader does not re-propose it."
       -- a comment RECORDING A DECLINED threshold. No value is introduced.
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name
judge  nothing moves, and the one threshold this step invited was declined by the implementer
       after I declined to ask for it. **EU1 does not attach** -- no value and no declared
       counter moves -- and I ran the adversarial configuration anyway, eighteen injections and
       two full model runs, because R694's lesson is that a value which does not move is the
       worst case and not the safest.
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1 -- no `Closes:`
line).** Step 3 remains open with all three reviewed revisions available. Nothing blocks, so
FR3's instruction stands and it is the only thing that matters this week: **build the rest of
FL2.**

1. **FL2, complete, before step 3's first reviewed revision (FR3).** Five items, none built:
   member topology from the config with the star as the default; `required_section` and
   `truss_sizing` in `floatfea run` with FM0's re-solve loop; the optional analyses off by
   default; headings as a list with the BEM refusal; the band check per case. The commit says
   so and claims none of it, which is correct. **This is the second commit of step 3 and both
   have been spent on ledgered gate items.** The locked plan routes those to the ledger by
   name, and FR0's date is 5 November.
2. **R860 before FL2 lands, not after.** It is the one of my five that FL2 itself makes live: a
   sizing loop that times itself puts a sixth sub-10-ms row in that table, and the hand copy of
   the stage tuple will not know. One import or one assertion.
3. **R849 with R854, over TWO files, still answered WHILE step 3 is built.** Two new
   deliverables are coming and both constants are hard-coded three-name tuples.
4. **R857, R858, R859 in the first reviewed revision**, with every figure regenerated at that
   commit (CP3) -- 97 rather than 99, the wall-clock sentence corrected, the mechanism sentences
   naming the assertion that actually fires. R847 and R848 unchanged; R850 is half paid, and
   R851 and R853 are paid.
5. **R852 and R856 remain with Xabier**, relayed correctly and verbatim this turn. Neither is
   the implementer's to repair in code.
6. **The whole-suite run and the EG3 state recorded at every commit of step 3** (R855, third
   occurrence), **against the PREDICATE in R861 and not against nine.** Every red in
   `tests/test_report_carried.py` or `tests/test_report_guard_states.py` naming a finding or a
   site of the newest verdict, or a `survives_the_state` case whose inner list names those;
   anything else is CZ1 (iv).
7. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 78
   reds matching mine id for id, and the three new cases green inside ladder 6 on a machine
   neither of us controls. I waited for the run rather than recording an unfinished one.
8. **The schedule.** FR0's 5 November stands. Step 3 opened on 18 October; two commits in, FL2
   is unbuilt by design under FR3, and nothing has slipped against a date yet. **I am not
   re-opening the escalation FR0 answered, and I am recording one number rather than a warning:
   five items, eighteen days, two commits spent on the ledger.** The next progress statement is
   step 3's first reviewed revision (FR5).

**What this commit got right.** It repaired a guard of its own that failed false, in the one way
EK2 permits -- by naming the real set rather than by giving the comparison slack -- and it wrote
down the tolerance it declined so that the next reader cannot re-propose it. It found the
dict-collapse in `_provenance` by reading the code I pointed at rather than taking my word,
extended the new check to all three artifacts and to both sides, and recorded the wrong figure
it was replacing instead of quietly substituting the right one. It accepted the two greens I had
reasoned were unreachable and did not pad the diff with them. **And it asked for its own
classification to be checked, which is how R861 got found: I went looking for the baseline I had
given it, and the baseline was wrong.**

---

<!-- EARLIER ROUNDS, VERBATIM. Hand-appended in the form
     scripts/write_verdict.py uses, under DX2: each round is added and no prior
     round is rewritten or removed. The tool refused this step (R856). -->

# Review — R1 step 3
Reviewed commit: e818375beb4198f853d5c6427b0ea2c7bbbfe8c6
**Reviewed commit: `e818375beb4198f853d5c6427b0ea2c7bbbfe8c6`.**
Verdict: PASS
Tests: 3695 passed, 9 failed, 1 skipped   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK.** No report revision exists for step 3, so this counts against
no round and all three reviewed revisions remain available. **Nothing blocks.** Both
blocking items step 2 carried are ANSWERED, measured by me rather than read; six findings
are ledgered and one is an apparatus item that FF0 routes to the next commit.

**I RULED UNDER FR1 WITH EZ0** (`docs/directives/FR.md:14-26`, `CLAUDE.md` section "What
blocks for the rest of R1"). No finding below can cause a silently wrong result, and I say
so for each rather than leaving the classification implicit. **This file is HAND-WRITTEN
because the one sanctioned path in refuses it -- R856.**

```
cmd    git diff --stat e93becf..HEAD
out    tests/regression/test_r1_example_regenerates.py  | 201 +
       tests/regression/test_r1_published_artifacts.py  |  16 +
       -- two files, both tests, nothing else
cmd    git diff --stat e93becf..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff e93becf..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff e93becf..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers:` header to compare. The newest revision in the tree is step 2's
third, `Answers: verdict 8 @ a7b2f62` (`docs/reports/R1/step-2.md:1302`), and verdict 9 is
newer -- which is EG3 state (2) by definition and is designed, not a defect.
`test_the_guard_reads_the_step_being_worked_on` is **green** in my run, which says
mechanically that state (1) is not in play.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R845** (not one number in the three published R1 deliverables is compared against anything) | **ANSWERED IN CODE, and I verified the repair by my own regeneration rather than by reading its counter-cases. The REPORT half of the condition is owed, correctly, at step 3's first reviewed revision.** | `tests/regression/test_r1_example_regenerates.py`, 8 cases. I ran `floatfea run` on the shipped example into a temp directory with the fixture's own recipe (68.95 s, `governing U = 1.71167 at platform:hub4_arm ROOT`) and compared every line: **report.md 99 comparable lines, 0 differing; member_forces.csv 1286, 0 differing; utilisation.csv 70, 0 differing.** Then I injected: the governing `**U = 1.71167 -> 0.99999` reddens `REGENERATES[report.md]`; the **last digit of member_forces.csv line 701** and of **utilisation.csv line 60** each redden their own file's case, so the comparison reaches the middle of a 1289-line CSV and not only row 1. The condition asked for the wall clock excluded BY NAME rather than by tolerance, and it is a regex over stage names. **Closed in code.** Owed: the report pasting both directions, every figure regenerated at the report's own commit (CP3) -- three of the figures the new file already publishes are wrong, see R853. |
| **R846** (the R838 repair is green on three injections one step above the one it was built for) | **ANSWERED, and I reproduced all three injections and the restore** | `tests/regression/test_r1_published_artifacts.py:112-117` (nine distinct non-blank), `:139` (`LABEL.strip()`), `:171` (`caveat.strip()`). My own harness, 31 cases over the three artifacts: baseline **31 passed**; caveat 8 = a duplicate of caveat 4 -> **1 failed** (`NINE_caveats`, naming `9 entries and 8 distinct non-blank ones`); caveat 8 = `""` -> **4 failed** (three membership cases by file, plus the count); `LABEL = ""` -> **3 failed**, one per artifact; restored -> **31 passed**. The three doors verdict 9 measured open are shut. **The next injection up is still green -- R852 -- and it is not the implementer's to fix.** |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- ledgered, and there is no report revision in which it could be answered** | FR1's third class. It is C43 on the closure list. |
| **R848** (the empty-directory refusal admits `.`, `./`, `..`, `" . "`) | **still open, untouched by this diff, and correctly so** | `git diff e93becf..HEAD -- floatfea` is empty. Non-blocking, same class as R843, ruled twice. |
| **R849** (the caveat, disclaimer and provenance gates quantify over a hard-coded three-file tuple, and step 3 publishes two more files) | **still open, and it now has a SECOND site -- R854** | `ARTIFACTS` at `tests/regression/test_r1_published_artifacts.py:69` and now `NAMES` at `tests/regression/test_r1_example_regenerates.py:48`. Verdict 9 said R849 is answered WHILE step 3 is built; that is unchanged, and the condition now names two files. |
| **R835** (EG3's enumeration) | **still open, still Xabier's; this commit is its eighth measurement** | of state (2)'s enumerated names, **two fire and the rest are green**, and both that fire do so for FC1's reason. It over-lists here as it under-listed at EH1, FN2 and EJ2. Relayed unchanged. |
| **R836** | **recorded, no change in this diff** | unchanged. |
| **C29, C34, C35** (`ruff`, `black`, `mypy`) | **green at this commit, on a machine neither of us controls** | CI run 39169784204, job `lint, unit and guards`, read at step level: `actionlint` SUCCESS, `ruff` SUCCESS (`All checks passed!`), `black --check` SUCCESS, `mypy` SUCCESS, `unit tests` SUCCESS (`186 passed in 67.62s`). Every one RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | not repaired in this verdict; repaired by the rounds that touch the files. |
| **C43, C44, C45** | **C43 and C44 carry; C45's ROUTING WAS MINE AND IT WAS WRONG** | verdict 9 ledgered C45. **FF0 says a closure item in the gating apparatus is NOT ledgered** -- `scripts/ci_section.py` reads the gating record -- so C45 belonged in the next commit, not on the list. I am correcting my own routing. See the process note: it cannot in fact be fixed before step 3's report exists, and that is the thing worth recording rather than the misfiling. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| `scripts/suite_count.py`'s own line + CZ1 (ii)/(iii)'s four outputs | **still owed, and now STRUCTURALLY UNPAYABLE until step 3's report exists** | see the process note. Not a finding against the implementer. |
| **EG3(ii): the verdict commit measured** | **DONE, by me, at this commit** | the two report-guard files: **9 failed, 320 passed, 1 skipped**, the same nine ids as verdict 9's and the same nine as CI's, traced one at a time under R855. |

## Findings

**NOTHING BLOCKS.** The diff is two test files, no `floatfea/` change, no tolerance, and the
three published deliverables are byte-unchanged -- which I established by regenerating them,
not by reading the diff. Both carried blocking items are answered at the layer they were
about. The seven findings below are the weakening directions I could still reach, and under
FR1 none of them can put a wrong number in front of anyone; I say which, for each.

**The implementer asked for the EXCLUSION to be attacked, and that is where four of the
seven are.** Two classes of line are dropped from the byte comparison and the commit message
claims "**BOTH are checked elsewhere rather than merely dropped**". For the provenance class
that is true in part and I measured its reach. **For the wall-clock class it is false:
nothing in the tree reads any published wall-clock value.**

**R850. (DOES NOT BLOCK -- ledgered) THE WALL-CLOCK EXCLUSION COVERS THREE OF THE FIVE ROWS
THE GENERATOR WRITES, SO TWO WALL-CLOCK ROWS SIT INSIDE A BYTE COMPARISON -- and in the other
direction no check anywhere reads a published wall-clock VALUE: `| total | 97.27 |` edited to
`| total | 999.99 |` and `| solve | 97.08 |` edited to `| solve | 0.01 |` are both green on
all 8 cases.**

```
claim  the exclusion's declared class and the generator's actual output are not the same set
cmd    floatfea/cli.py:296-299, the row loop
out    for stage in ("build", "load", "solve", "code_check", "total"):
           lines.append(f"| {stage} | {result.timings[stage]:.2f} |")
       -- FIVE stages, every one a time.perf_counter() delta (floatfea/run/pipeline.py:605,
          653, 664, 669, 672)
cmd    the exclusion regex, tests/regression/test_r1_example_regenerates.py:56
out    r"^\|\s*(build|solve|total)\s*\|\s*[0-9.]+\s*\|\s*$"       -- THREE
cmd    the file's own declared class, :54-55
out    "the report carries a `| stage | seconds |` table whose THREE rows cannot agree
        between two runs"
cell   my own injections against the real gate's four test functions, one edit each, the
       fresh side held fixed at my own 68.95 s run of the shipped example
out    CONTROL unmodified                        8 passed, 0 failed
       | total | 97.27 | -> | 999.99 |           8 passed, 0 failed   <- GREEN
       | solve | 97.08 | -> | 0.01 |             8 passed, 0 failed   <- GREEN
       | load | 0.00 | -> | 0.01 |               7 passed, 1 failed   <- COMPARED
       | code_check | 0.00 | -> | 0.01 |         7 passed, 1 failed   <- COMPARED
cell   the margin on the two compared rows, solved rather than sampled: the printed row
       flips at 5 ms, and the load stage is np.load + exported_froude_lambda + the period
       check
out    first pass 1.6 ms, then 0.7 ms (12.8 MB npz, lazy open)  -> margin 3.1x on the
       coldest sample I could take
cmd    the same two rows on a Linux runner with a different filesystem
out    ladder 6 (empty:tests/verification/rung6 full:tests/regression):
       214 collected at 8542d79 -> 222 collected here, 0 failed, 0 errored -- the 8 new
       cases RAN and passed there, so both compared rows printed 0.00 on that machine too
rule   my own recorded guard -- an excluded line is a line nothing checks unless something
       else checks it, which the file itself says at :50-51; EH4 -- the boundary is solved in
       the direction that weakens the gate
judge  **two statements in opposite directions, and neither is a silently wrong result.**
       (i) `load` and `code_check` are inside the comparison with a 3.1x margin to a FALSE
       RED. A false red is loud, so it does not block -- but the pressure a false red creates
       is to widen the exclusion, at the worst possible moment to be deciding what the
       exclusion means. (ii) No published wall-clock value is checked by anything, so the
       commit message's "both are checked elsewhere" is false for this class. That is prose
       (FR1's third class) and the number is a wall clock nobody sizes steel against, so it
       does not block either. **And I checked the obvious repair and WITHDREW it:**
       `timings["total"]` is the exact sum of the four at full precision
       (floatfea/run/pipeline.py:672), but the published rows are rounded to 2 dp, so
       `total == build + load + solve + code_check` on the PRINTED values needs up to 0.02
       of slack -- which is a tolerance, in `tolerances.py`, for a wall clock. I am not
       asking for it.
       What I would accept: the exclusion covers all five stages the generator writes, the
       pin at :172-175 lists all five, and the docstring says the wall-clock VALUES are
       excluded and unchecked instead of saying they are checked elsewhere.
```

**Closed when** the exclusion and its pin cover the same five stage names
`floatfea/cli.py:297` writes, and the two prose claims -- at
`tests/regression/test_r1_example_regenerates.py:54-55` and in the commit message -- are
corrected to what was measured.

**R851. (DOES NOT BLOCK -- ledgered) THE PROVENANCE EXCLUSION IS CHECKED BY BASENAME ONLY,
AND THE KEY-SET PIN READS `report.md` ALONE. Three injections measured green: the deck path's
DIRECTORY swapped in all three files, the `load_cases` MODE word changed, and a second
contradictory `# deck:` line inserted into a CSV.**

```
claim  the reach of the exclusion the implementer asked me to attack, solved from the side
       that weakens it (EH4)
cell   the real gate's four test functions, fresh side held fixed, one class of edit each
out    CONTROL unmodified                                            8 passed, 0 failed
       deck DIRECTORY swapped, basename kept, all three files        8 passed, 0 failed  <- GREEN
         data/platform/platform12_deck.yaml -> /home/someone-else/junk/platform12_deck.yaml
       CONTROL deck BASENAME changed, all three files                5 passed, 3 failed
         -> "the deck provenance names 'OTHER_deck.yaml' in the committed file and
             'platform12_deck.yaml' in a fresh run of this tree"   -- the basename half WORKS
       load_cases MODE word npz -> static, all three files           8 passed, 0 failed  <- GREEN
       a SECOND "# deck: /home/someone-else/junk/platform12_deck.yaml" line
         inserted into utilisation.csv                               8 passed, 0 failed  <- GREEN
       CONTROL an extra "| solve | 3.00 |" row in report.md          6 passed, 2 failed
         -> EXCLUSION pin: ('the SHIPPED report', ['build','solve','solve','total'])
       CONTROL the three provenance lines DELETED from report.md     6 passed, 2 failed
       CONTROL the three timing rows DELETED from report.md          7 passed, 1 failed
cmd    why the duplicate is invisible, read rather than guessed
out    tests/regression/test_r1_example_regenerates.py:105-112 -- _provenance returns a
         DICT keyed on config|deck|load_cases, so two lines with one key COLLAPSE and the
         last wins; :168-177 -- the pin iterates over report.md and the fresh report ONLY,
         so for the two CSVs the excluded set is pinned by nothing
rule   EH4; and my own recorded guard -- check that the collection the assertion inspects can
       contain the failure
judge  **it does not block, and I want the reason on the record rather than the ruling.** No
       number moves in any of the three. None of the three is a string this tool can emit:
       the directory component is a FUNCTION OF THE CONFIG'S OWN LOCATION
       (floatfea/run/config.py:507-523 -- anchored on source.parent, then its parent, then
       absolute), which is exactly why the exclusion exists and why the fixture's copy in a
       temp directory differs at all. So a wrong directory in a shipped artifact is reachable
       only by a hand-edit, and a hand-edited provenance path puts no wrong engineering
       number in front of anyone. Under FR1 that is not a silently wrong result, and under
       its second head nothing is accepted and used other than as declared -- the deck that
       was USED is the right one in every green row above.
       **What I would accept, if it is cheap:** the pin loop at :168 runs over all three
       files rather than over the report, which is the same loop already written; and the
       shipped path is compared by resolving it against the two anchors _relative uses
       instead of by rsplit("/", 1)[-1].
```

**Closed when** the excluded key set is pinned in all three artifacts rather than in the
report alone -- or the report states that the two CSVs' excluded set is pinned by nothing and
why that is acceptable.

**R852. (DOES NOT BLOCK -- ledgered, AND IT IS THE ONE I MOST WANT READ, because no repair the
implementer can write will close it) A CAVEAT TRUNCATED TO ITS OWN MARKER IS GREEN ON 31 OF
31 CASES. TABLE_CAVEATS[8] reduced from R743's sentence to the string "R743:" passes the new
distinct-and-non-blank count, passes all 27 membership cases, and passes after the artifacts
are regenerated. So does LABEL = "a". This is R831 returning in a new shape: R831 was "the
needle is the MARKER and the marker survives a rewording", and truncating the text to the
marker turns the needle back into a marker.**

```
claim  the repaired gate's boundary, one injection above the three it was built for
cell   floatfea.cli.TABLE_CAVEATS / LABEL rebound and the gate re-imported so it reads the
       mutated value, the three committed artifacts untouched, 31 cases (9 caveats x 3 files
       + 3 disclaimer + the count)
out    BASELINE                                              31 passed,  0 failed
       caveat 8 = DUPLICATE of caveat 4                      30 passed,  1 failed
       caveat 8 = ""                                         27 passed,  4 failed
       LABEL = ""                                            28 passed,  3 failed
       caveat 8 truncated to its first word, "R743:"         31 passed,  0 failed  <- GREEN
       caveat 8 = "C_m"                                      31 passed,  0 failed  <- GREEN
       LABEL = "a"                                           31 passed,  0 failed  <- GREEN
       RESTORED                                              31 passed,  0 failed
cmd    what the published caveat says, so the loss is stated rather than implied
out    floatfea/cli.py, TABLE_CAVEATS[8]:
       "R743: C_m MULTIPLIES the bending term in section 3.3.1's interaction, ..."
       -- the sentence that delegates the C_m DIRECTION to a published sensitivity column
cmd    whether the new R845 gate catches it instead
out    no. The regeneration gate compares the shipped files against a fresh run, so once the
       artifacts are regenerated BOTH sides carry the stub and both are green. The two gates
       compose against a stub that was never regenerated, and neither covers a regenerated
       one.
cmd    whether any record of the nine caveat TEXTS exists to compare against
out    grep -n "caveat" docs/directives/FO.md
       :20-22  "all nine caveats in the header; a test that reads the published .md and .csv
                files, not a stub. Each must redden when one caveat is removed"
       -- FO2 records the COUNT and the mechanism. It records no caveat text.
rule   my own recorded guard -- a gate carries its own failure, and "R743:" in text cannot
       fail against a file that contains R743's real caveat; EH4 -- the injection rises until
       a clean case trips
judge  **it does not block, for a reason that is not about severity.** The published outcome
       is the one verdict 9 stated for R846 -- a utilisation column whose C_m direction is a
       stub while the gate certifies nine of nine -- so by severity it IS R846. But **no
       comparison between the code and the files can detect it**, because both halves carry
       the stub; the only check that could is a comparison against an independent record of
       what the nine caveats SAY, and this repository has none. The cheap alternative is a
       minimum length or word count, which is a threshold for a sentence and belongs in
       tolerances.py if anywhere, and I am not asking for that. **So this is not the
       implementer's to repair in code.** It is a question for Xabier about FO2: if the nine
       caveats are load-bearing enough that their absence is a wrong result, their TEXTS
       belong in the directive record, and then one list comparison closes the class
       permanently. Recorded, measured and relayed -- not a round.
```

**Closed when** FO2's nine caveat texts exist in a record the gate can compare against -- or
the report states, with the three green rows above, that the caveat gate cannot distinguish a
caveat from its own marker and that this is accepted.

**R853. (DOES NOT BLOCK -- ledgered, FR1's third class) "102, 1289 AND 73 COMPARABLE LINES"
DOES NOT REPRODUCE. The comparable counts are 99, 1286 and 70. The published figures are the
report's total minus its three provenance lines, and the two CSVs' TOTAL line counts -- so the
timing exclusion was subtracted nowhere and the provenance exclusion was subtracted only for
the report.**

```
claim  the figure the new file offers as "the measurement that says the numbers are
       reproduced" (tests/regression/test_r1_example_regenerates.py:62-64)
cmd    the gate's own _lines() applied to the three shipped files and to my own fresh run
out    report.md          total 105   comparable 99    differing 0
       member_forces.csv  total 1289  comparable 1286  differing 0
       utilisation.csv    total 73    comparable 70    differing 0
cmd    where the published numbers come from
out    102 = 105 - 3   (the provenance lines only)
       1289, 73        = the TOTAL line counts, with nothing excluded
rule   BF0 with CP3 -- the figure is pasted from the run that produced the artifact and the
       paste is the last edit; BP0 -- a figure carries the rule it was measured against
judge  the substantive claim -- that nothing but the two declared classes differs -- is TRUE,
       and I verified it independently on a fourth machine state: 0 differing comparable
       lines in all three files. Only the three counts are wrong, and they are wrong in the
       direction that makes the gate sound wider than it is. FR1's third class; no number in
       a gate or a deliverable moves. **It is recorded because it is the figure the step's own
       repair is measured by**, which is exactly what R847 was two rounds ago.
```

**R854. (DOES NOT BLOCK -- ledgered; it joins R849) R849 NOW HAS A SECOND SITE. The new gate
repeats the hard-coded three-file tuple, so FR3's two further deliverables would arrive
UNCOMPARED as well as uncaveated.**

```
claim  the artifact set is fixed in the source in two files now, not one
cmd    the two constants
out    tests/regression/test_r1_published_artifacts.py:69  ARTIFACTS = (REPORT, FORCES,
                                                                        UTILISATION)
       tests/regression/test_r1_example_regenerates.py:48  NAMES = ("report.md",
                                                                    "member_forces.csv",
                                                                    "utilisation.csv")
cmd    what step 3 publishes, from the plan
out    docs/milestones/R1.md step 3 -- required_section and truss_sizing in `floatfea run`,
       both OFF in the shipped example today
rule   my own recorded guard -- check that the collection the assertion inspects can contain
       the failure
judge  not a defect today: the two outputs are off, the files do not exist, and the gate is
       green because main() writes exactly these three. Verdict 9 ruled R849 answered WHILE
       step 3 is built; the only change is that its closing condition now names two files,
       and the second is the one that compares NUMBERS. A fourth deliverable that arrives
       with no numeric comparison is R845 with a different file name, and that is the one of
       my seven findings that could later put a wrong number in front of someone.
```

**R855. (DOES NOT BLOCK -- ledgered, and it is the SECOND occurrence) THE SUITE WAS NOT RUN AT
A PUSHED, REVIEWED COMMIT, AND THE TREE'S NINE REDS WERE NOT RECORDED WITH THEIR CAUSE NAMED.
The implementer ran `tests/regression tests/unit` (408 passed) and asked whether the light
scope requires the full run. It does, and EG3(i) requires the FAILED list pasted with the
state named. I did both; nothing was hiding this time.**

```
claim  ES0's light scope is the suite, and EG3's waiver is conditional on a trace that was
       not written
cmd    python -m pytest -q --tb=no -rf        (mine, at the reviewed commit, tree clean)
out    9 failed, 3695 passed, 1 skipped in 957.64s (0:15:57)
cmd    the implementer's two figures, cross-checked against CI's own numbers rather than
       re-run
out    unit tests 186 passed + ladder 6 222 collected = 408   (this commit, run 39169784204)
       unit tests 186 passed + ladder 6 214 collected = 400   (8542d79, run 39164110433)
       -- both reported counts are exactly right, and the +8 is this gate
cmd    the nine reds, traced ONE ID AT A TIME per EG3(i), not as a family
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
         "run 39162423263: the table says no result (status in_progress), gh says failure"
                                                                      -> FC1, and C45
       test_the_report_carries_a_WHOLE_SUITE_count
         "the newest revision carries no whole-suite line ... Generate it with
          python scripts/suite_count.py"                              -> FC1
       test_the_guard_survives_the_state[baseline] and six others
         each inner run read individually: 2 failed, 301 passed, 1 skipped, and the two
         FAILED ids inside each are the two above                     -> the cascade
       test_the_guard_reads_the_step_being_worked_on                  -> PASSED
rule   ES0 -- an interim check is the suite and CI at the commit plus a CZ0 (a)-(d) scan;
       EG3(i) -- the waiver is conditional on the trace and the trace is pasted; CA2, which I
       keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD regardless of
       the local run; EH1 -- the cascade is identified by the baseline being red and by each
       cascading state's own failure line, not by its name
judge  **all nine trace, to two names rather than to a family, and the waiver applies in full
       -- so CZ0 (d) does not stand and CA2's HOLD is not reached.** I measured that rather
       than classifying it. The finding is that the record did not say so at a pushed commit,
       for the second time in three commits: verdict 8's R841 was a NINTH red that an
       eight-file subset could not contain, and the subset is the same shape of choice. It
       does not block under FR1 -- no wrong number follows, and in fact nothing was hiding --
       but a tree whose reds are not traced is the tree in which the next real one is not
       seen, and R629 is this project's own measured instance of that.
```

**Closed when** the next commit in step 3 records the whole-suite run and names the EG3 state
with its FAILED list, as every revision in step 2 did.

**R856. (DOES NOT BLOCK -- APPARATUS, and under FF0 it is NOT LEDGERED: it is fixed in the next
commit) `scripts/write_verdict.py` REFUSES TO WRITE A VERDICT FOR A STEP THAT HAS NO REPORT,
AND FR3 PLUS ES0 MAKE THAT THE NORMAL STATE OF AN INTERIM CHECK. This verdict is hand-written
because the one sanctioned path into `docs/reviews/` refused it.**

```
claim  the sanctioned path cannot write the verdict the Stop hook requires
cmd    printf the four mandatory sections with a PASS header |
         python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       EXIT=1
cmd    the refusal site
out    scripts/write_verdict.py:179-181
         report = root / f"docs/reports/{args.milestone}/step-{args.step}.md"
         if not report.exists(): sys.exit(f"refused: no step report at {report}")
cmd    whether the state is exceptional
out    docs/directives/FR.md:28-33 (FR3) -- "Build ALL of it before the first reviewed
       revision. Interim checks run as the hook requires and count against no round."
       CLAUDE.md (ES0) -- "a verdict the hook forces at a turn boundary mid-step, on a tree
       with NO new report revision, is an INTERIM CHECK"
rule   FF0 -- anything that reads the gating record, or decides whether a green is believed,
       is fixed in the next commit under EK2's repair-not-extend rule; and the file's own
       docstring already records the precedent: "the reviewer could not write an R1 verdict
       through the one sanctioned path in, and hand-wrote it instead"
judge  the refusal was right when every step's first reviewed artifact was its report. FR3
       inverted that: step 3's report comes after all of FL2, so every interim check in step 3
       is a verdict on a step with no report, and the only path in refuses all of them. The
       check that is wanted is "a step with no report AND no diff to judge"; here the diff is
       217 lines. **I am recording it rather than widening it** -- EK2 says a guard that fails
       false is fixed or deleted, never extended, and which of those this is, is Xabier's
       call, because it is the reviewer's own tooling and the file says so itself at :44-48.
       Until then the hand-written file IS the verdict, as it was for R1 step 1.
```

## The process note this tree is about to need, said once

**FR3 + FC1 + EK3 means the tree is RED BY TWO FOR THE WHOLE OF STEP 3, by construction, and
no file says so.** `test_the_report_carries_a_WHOLE_SUITE_count` wants a line inside the
newest report revision; `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` wants that revision's
CI table regenerated (C45). The newest revision is step 2's third, and **EK3 forbids any
commit touching a closed step report**, so neither can be written until step 3's first
revision exists -- which FR3 places after all five of FL2's items. FC1 says both are designed
and self-clearing "in the next commit"; FF0 says an apparatus item is "fixed in the next
commit". **Neither is available here, and that is neither the implementer's fault nor mine.**
The consequence is operational and I will act on it: for the rest of step 3 the baseline is
nine reds, every interim check traces against it one id at a time, and a tenth red is CZ1 (iv)
unchanged. This is C89's shape -- "a tree that is red by design is a tree in which the next
real red is harder to see" -- and it goes to Xabier with R856, because the exit is a clause
and not a commit.

## Try to break it -- what I ran, and what it found

* **A full regeneration of all three deliverables from this tree into a temp directory, with
  the fixture's own recipe.** 68.95 s, `governing U = 1.71167 at platform:hub4_arm ROOT`,
  **0 differing comparable lines in all three files** (99, 1286, 70). That is the control for
  everything below, and the fourth independent machine state for the wall clock.
* **Thirteen injections against the new gate**, each run against the real test functions with
  the fresh side held fixed: the governing U; the last digit of member_forces.csv line 701;
  the last digit of utilisation.csv line 60; five wall-clock edits; three provenance edits; a
  duplicated provenance line in a CSV; an extra timing-shaped row; and two deletion controls.
  **Three classes came back green -- R850, R851 -- and each of the gate's four test functions
  was shown to carry its own failure by at least one red.**
* **Seven injections against the repaired caveat gate**, including the three verdict 9
  measured (all three redden, 1 / 4 / 3 cases, and restore) and **three one step above
  (R852)**. My first pass of that harness had a bug -- three cases ran with the unmutated
  tuple and printed `31 passed`, which would have read as the repair not working. I found it
  because `R846 b` should have reddened and did not, fixed the harness and re-ran. Recorded
  because an instrument that silently fails to inject is the shape of every finding in this
  section.
* **The boundary on the two compared wall-clock rows, solved rather than sampled:** the
  printed row flips at 5 ms, and the load stage measures 1.6 ms cold and 0.7 ms warm --
  margin 3.1x.
* **CI read at the step level, both jobs**, including the ladder's rung-6 collected count
  before and after, which is what says the new gate RAN on a machine neither of us controls
  rather than being collected and skipped.
* **The nine reds one id at a time**, with each cascading state's inner FAILED list read
  rather than inferred from its name.

**What I did not find, and it is the larger part.** R845's repair does what verdict 9 asked
and it is stronger than the condition required: it reaches the last digit of any line in any
of the three files, it is redirected so it cannot overwrite the evidence it checks, and it
arrives green on a Linux runner as well as here. R846's three doors are shut. No `floatfea/`
line moved, no tolerance moved, the three deliverables are byte-unchanged, and `ruff`,
`black`, `mypy`, 186 unit tests and all six ladder rungs are green in CI. **The exclusion --
the thing I was asked to attack -- is honest in its structure: it is declared, it is pinned
for the report, and its deletion direction is backstopped. Where it leaks, it leaks on paths
and on a wall clock, and not on one engineering number.**

## CI at the reviewed commit: RED, nine reds, ALL NINE traced to FC1's designed pair

```
cmd    gh run list --commit e818375beb4198f853d5c6427b0ea2c7bbbfe8c6
         --json conclusion,status,databaseId
out    [{"conclusion":"failure","databaseId":39169784204,"status":"completed"}]
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is not
          a pass and I did not record one. The SHORT sha returns an empty list; the flag
          needs the full sha, as verdict 9 recorded.
cmd    gh run view 39169784204 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1  1276 collected, 0 failed / ladder 2  66 / ladder 3  314 /
         ladder 6  222 collected, 0 failed  (empty:rung6 full:tests/regression; 214 at
                                             8542d79, so the 8 new cases ran and passed) /
         ladder 4  343 / ladder 5  87
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 67.62s) / guards and meta-tests FAILURE
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39169784204 --log-failed, the ids
out    identical to my own nine, id for id, and each cascading state's inner run reads
       "2 failed, 301 passed, 1 skipped" naming the two FC1 ids
rule   CA2 -- a red CI is a HOLD regardless of the local run; EG3 with FC1 -- the two
       CZ1-class names are state (2)'s and neither can pass in the commit it describes;
       EG3(i) -- EVERY red traces by name or it is CZ1 (iv) unchanged
judge  **all nine trace, and the waiver applies in full: CZ0 (d) does not stand.** Both FC1
       reds are designed and neither is clearable before step 3's report exists -- see the
       process note. Every step in the lint job RAN rather than being skipped behind an
       earlier red, which is what CZ1 (iii) exists to see, and mypy is green there, so the
       CI-only types-PyYAML red FP1 found has stayed fixed.
```

**Not CK2's exhausted-allowance state.** Both real jobs have per-step conclusions, real counts
and eight- and nine-minute durations; the two skipped jobs are the determinism workflow's own
event gate and not an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree
was clean before I wrote this file.** Neither exception opens: this diff touches no part of
F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about a caveat tuple or a published-artifact comparison. The
last corpus commit remains `ba1527e` (batch 47).

**I ran the recorded substitute, and the half that paid is the one this step is about:**

* **A regeneration check on a published deliverable, taken in BOTH directions** -- all three
  R1 artifacts regenerated from this tree and diffed line for line (0 differing), then
  thirteen injections against the gate that now guards them. It produced R850, R851 and R853.
  **This is the fifth consecutive round in which the regeneration check's weakening direction
  produced the round's findings.**
* **A continuum grid over the parameter space a decision rule guards** -- the caveat gate's
  mutation space rather than the config's this time: duplicate, blank, whitespace-only,
  truncated-to-first-word, degenerate-substring, and the same five on LABEL. It produced
  **R852**, the one finding here that no code in this repository can close.

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff e93becf..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff e93becf..HEAD -- floatfea tests scripts | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance"
out    (no match)
cmd    the same, widened to any literal comparison the diff adds
out    93:+   assert main(["run", str(cfg)]) == 0        -- an exit code
       210:+  assert len({c.strip() for c in TABLE_CAVEATS if c.strip()}) == 9
       -- FO2's own declared count, annotated at :204-209; ruled a declared quantity and not
          a threshold at verdict 9, and that ruling is unchanged by the new form
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name
judge  nothing moves. **EU1 does not attach** -- no value and no declared counter moves --
       and I ran adversarial configurations anyway, twenty of them, because R694's lesson is
       that a value which does not move is the worst case and not the safest. And I declined
       to ask for the one new threshold this step invited: a slack on the published
       wall-clock sum (R850).
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1).** Step 3
remains open with all three reviewed revisions available. Nothing blocks, so FR3's instruction
stands: build the rest of FL2.

1. **FL2, complete, before step 3's first reviewed revision (FR3):** member topology from the
   config with the star as the default; `required_section` and `truss_sizing` in `floatfea
   run` with FM0's re-solve loop; headings as a list with the BEM refusal; the period-band
   check. None of it is in this commit, as the commit says.
2. **R849 with R854 -- answered WHILE step 3 is built, over TWO files now.** The caveat,
   disclaimer, provenance AND regeneration gates are written over the artifact set the config
   declares, not over two hard-coded three-name tuples. A fifth deliverable arriving with no
   numeric comparison is R845 with a different file name.
3. **R850's two prose corrections and the five-stage exclusion**, R851's pin over three files,
   R853's three counts -- all in the first reviewed revision, with every figure regenerated at
   that commit (CP3). R847 and R848 unchanged.
4. **R852 and R856 go to Xabier, not into a round.** R852 needs FO2's caveat texts recorded
   before any gate can see the defect; R856 needs a clause about the reviewer's own tooling.
   Both are relayed with their measurements and neither is the implementer's to repair in code.
5. **The whole-suite run and the EG3 state recorded at every commit of step 3** (R855),
   against a baseline of nine, with a tenth red treated as CZ1 (iv).
6. **The push (FP1) continued.** It gave this round a completed CI run at the judged commit,
   nine reds matching mine id for id, and the new gate's 8 cases green inside the ladder's
   rung 6 on a machine neither of us controls. I waited for the run rather than recording an
   unfinished one.
7. **The schedule.** FR0's 5 November is the target. Step 3 opened on 18 October carrying two
   blocking items, both answered in its first commit, with FL2 unbuilt by design. Nothing has
   slipped and I am not re-opening the escalation FR0 answered; the next progress statement is
   step 3's first reviewed revision (FR5).

**What this commit got right, and it is much the larger part.** Two blocking items were
answered first, at the layer each was about, in one commit, with counter-cases in both EH4
directions and a redirected fixture so the gate cannot overwrite its own evidence. The
implementer reproduced my R845 finding independently instead of taking it, flagged the one
lint choice that reads like an omission (`strict=False`, and the reasoning is right -- the
length mismatch is reported with both counts, which I confirmed by injecting one), and found
the provenance exclusion by RUNNING the gate rather than by anticipating it, which is the only
way that class is ever found. **Every one of my seven findings is in the reach of a check, not
in a number: nothing in `floatfea/` moved, no deliverable moved, and the gate that now guards
them reaches the last digit of every line in all three files.**
