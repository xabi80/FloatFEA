# Review — F2 step 5
Reviewed commit: 217a5ce23f781bd41be03bb4eb25481872b6b119
Verdict: HOLD

**Reviewed commit: `b21760b`.** Report revision 26, `Answers: verdict 51 @
7ffd67a`. The `Reviewed commit:` line stamped above by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus
commit `217a5ce` -- not the commit judged. R373, still open; read `b21760b`.

Tests: **2575 passed, 0 failed, 0 skipped** at `b21760b` (my run, clean tree,
`python -m pytest -q`, 605.01 s, Python 3.13 on Windows).

**Commits judged: `eb5a19c`, `706d4e6` (process), `1796183`, `0fbfbe9`,
`b21760b` (report).**

**Item 1b.** Revision 26 line 9590 reads `Answers: verdict 51 @ 7ffd67a`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`7ffd67a4be4c1d43ff3836f01f5f6e7f541cdc99`. It is the latest. **Passes.**

**The section 5 suite line reconciles to the unit, measured not read.**

```
cmd  python -m pytest --collect-only -q                       (at b21760b)
out  2575 tests collected
cmd  the same for the three files section 5 names as excluded
out  369 tests collected
judge 2575 - 369 = 2206, which is the report line exactly. The report took
     it at 0fbfbe9 and b21760b changes only the report, so the two agree.
```

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT, AND THE DETERMINISM LEGS RAN

```
cmd  gh run view 35664796051 --json headSha,event,status,conclusion
out  head b21760b, event workflow_dispatch, status completed, SUCCESS
cmd  gh run view 35664796051 --json jobs
out  13 jobs, ALL success: "lint, unit and guards" 14 steps, "the
     verification ladder" 13 steps, "CI determinism -- leg (1..10)" 13 steps
     each, "CI determinism -- ten legs agree" 4 steps
judge GREEN ON LINUX AT THE COMMIT I JUDGE, and not CK2: every job ran real
     steps for minutes. `gh run list --commit b21760b` returned an empty
     list on my first call and the run on the second; I record the flake
     rather than the first answer.
judge AND THE TEN DETERMINISM LEGS EXECUTED, which they have not done at any
     commit in the last several rounds. R383 state has changed -- see
     Carried.
cmd  gh run list --limit 15 --json databaseId,headSha,conclusion,event
out  35659133236 push 1796183 FAILURE; 35660198114 push 0fbfbe9 FAILURE;
     35664796051 dispatch b21760b SUCCESS. No other run since 6170263.
cmd  gh run view 35659133236 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  9 rows: test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW, and the eight
     test_report_guard_states parametrisations it cascades into
cmd  the same for 35660198114
out  9 rows: test_the_whole_suite_line_is_about_a_commit_that_exists, and
     the same eight
judge BOTH REDS ARE THE REPORT OWN GUARDS AND BOTH ACCOUNTS I WAS GIVEN ARE
     TRUE. What I was told named one failure each; there are nine each, and
     the other eight are the `baseline: expected a clean run` cascade from
     the first. Section 0a publishes all nine of each, generated, so the
     report is the more complete of the two accounts.
cmd  python scripts/ci_section.py --rounds, re-run by me at b21760b
out  the three committed rows and both nine-line blocks reproduce BYTE FOR
     BYTE, plus a fourth row for 35664796051 that did not exist when the
     report was written. THE COMMITTED 0a IS FAITHFUL.
cmd  python scripts/ci_section.py --history / --commits, re-run by me
out  0b reproduces byte for byte; 0c reproduces plus b21760b.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

**And I tested the CY0 mechanism rather than reading it.** Calling
`rounds_runs()` with an anchor old enough to reach last round prints
`35561482997 push 2bd9e89 ORPHANED conclusion **failure**`. The
time-not-ancestry selection and the *head not in current history* label both
work. That is the substance of R461 and it is real.

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff --stat 7ffd67a..b21760b -- .claude docs/SUPERVISOR.md
out  .claude/hooks/stale-before-commit.sh | 41 ++    (new)
     .claude/settings.json                | 10 ++
cmd  git log --format=%h%x20%s -- .claude/hooks/stale-before-commit.sh
out  706d4e6 process: the staleness checker is wired to a pre-commit hook
     (CY2, R465)
cmd  git show --stat 706d4e6
out  TWO FILES, both under .claude/, nothing under floatfea/ tests/ scripts/
judge STANDALONE, `process:`-prefixed, CITES THE DIRECTIVE. NOT A STOP. I
     read both files line by line: 51 lines added, 0 removed, NO GUARD
     DELETED. The hook decides `ask`, never `deny` except when python is
     missing, and it does not touch the reviews/corpus PreToolUse hook
     beside it. The wiring is the right answer to R465. Its comment is not
     -- R467.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction own expectation
cmd  git diff 7ffd67a..b21760b -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung green is written by code in its own directory.
cmd  git diff 7ffd67a..b21760b -- floatfea/tolerances.py | grep -E "^[+-][A-Z_]+.*Final"
out  (empty) -- NO CONSTANT MOVED. The 20 changed lines are comments.
cmd  git diff --stat 7ffd67a..b21760b -- docs/milestones docs/verification PLAN.md docs/closure
out  (empty) -- the locked plan was not touched.
```

## Carried

Verdict 51 held on R459, R460, R461 and recorded R462-R466. **R459 is
answered and answered well. The R461 mechanism half is answered and I
verified it; its narrative half is neither done nor declared -- R470. R460 is
answered in `scripts/precommit_stale.py` and re-broken one commit later in
`.claude/hooks/stale-before-commit.sh` -- R467. R462, R463, R464, R465 and
R466 are answered in letter; three of them leave the class open and those are
recorded, not held.** What holds this step is three sentences a command
refutes and one status claim -- the sixth round running in which the defect
is in the prose around the repair rather than in the repair.

- **R459 -- ANSWERED, at both sites its condition named, and by the better of
  the two routes offered.** `_paths()` has no exclusion list at all, so
  `files()` means what a reader grep means, and both claims were
  regenerated. I ran `grep -rl RIGID_MODE_FLOOR tests/ --include=*.py` (3
  files) and the same for `RIGID_BODY_MODE_RATIO` (4), and `:460` now reads
  THREE with the third enumerated and `:565` reads FOUR with the fourth
  enumerated. I also checked the two triples the round did NOT touch:
  `RIGID_BODY_MODE_RATIO_COUNTER_DEFECT` and `RIGID_BODY_SUBSPACE_LOSS` do
  not occur in the guard module, so `:598` and `:658` are still right and
  were correctly left alone. **Closed.**
- **R460 -- ANSWERED IN `scripts/precommit_stale.py`, AND REBROKEN IN THE
  NEXT COMMIT.** The docstring withdraws `12 ... 5 survivors, 1 TRUE and 4
  false`, names the command that prints `11 numbers ... 14 survivors`, and
  records my classification of all fourteen as false. That is the repair
  asked for, done properly. `706d4e6` then publishes `four in five` in
  hand-written prose in the hook. **Reopened as R467.**
- **R461 -- MECHANISM ANSWERED AND VERIFIED; NARRATIVE NOT ANSWERED AND NOT
  DECLARED.** The condition named three things. The first -- a commit list
  that is what the command prints -- is answered by generating section 0c.
  The second and third -- one sentence saying the `docs:` commit was split
  after `test_a_docs_commit_does_not_also_edit_the_guard_that_judges_it`
  refused it, naming run `35561482997` at `2bd9e89` and why section 0a could
  not show it -- are absent from revision 26 and absent from the
  untouched-sites table. **R470.**
- **R462 -- ANSWERED IN LETTER, and the network test is the right call.**
  `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` asks `gh` for every row
  and fails rather than skips; the guards job got a token so it can. All four
  of the edits I measured last round are now refused, and I confirmed the
  row-versus-failing-block cross-check fires. What is still open is the
  class: the row head and event cells are not read at all, and a table can
  drop rows as long as one survives. **R472**, recorded.
- **R463 -- ANSWERED IN LETTER.** The split keys on a generated-marker
  comment rather than on a heading number, and both of my `## 0b.` shapes are
  now refused. The exemption is still a string the implementer types, and
  adding that one line re-admits both. **R471**, recorded.
- **R464 -- ANSWERED IN LETTER, AND THE DOCSTRING DID NOT FOLLOW.** Equality
  refuses all four of my re-admissions through shipped controls, and the
  uniqueness rule was inverted correctly. The rule is now a registry, the
  module stated purpose no longer describes it, and six of nine unseen
  shapes ship green. **R469** holds on the sentence; the mechanism goes to
  4a.
- **R465 -- ANSWERED.** `.claude/hooks/stale-before-commit.sh` runs
  `scripts/precommit_stale.py` on any Bash command containing `git commit`,
  in a standalone `process:` commit. `ask` rather than `deny` is the right
  decision at a fourteen-in-fourteen false rate. **Closed on the wiring**;
  the figure inside it is R467.
- **R466 -- ANSWERED, and it dissolves exactly as claimed.** I ran
  `count("tests/test_tree_prose_consistent.py", "RIGID")` giving `11` and
  `count("tests/prose_triple_controls.txt", "RIGID")` giving `6`. Neither
  raises. **Closed.**
- **R458 -- OPEN, correctly, and not claimed.** 4a.
- **R447 -- OPEN, restated on `rigid_body_mode_ratio`.** 4a.
- **R383 -- OPEN, BUT ITS STATE HAS CHANGED AND THE REPORT DOES NOT SAY SO.**
  Ten determinism legs and the agreement job executed and concluded `success`
  at `b21760b`, 13 steps each. That is the first execution I have been able
  to record in many rounds. The report does not mention it and publishes no
  leg table, so nothing in the repository carries the result. Closing path:
  `python scripts/ci_section.py --legs` at a commit whose run has leg rows.
  Not a hold -- the run is in section 0a and is green -- but it is a
  measurement the round earned and did not bank.
- **R419, R431, R432, R433 -- OPEN, correctly listed.** 4a.
- **R411 -- ANSWERED for revision 26.** There is no section 9 any more;
  section 0c is the commit list and it is generated. Recurrence watch only.
- **R410, R413, R414, R400, R401, R402, R390, R391, R392, R393 -- OPEN at
  4a**, correctly listed.
- **R370, R371, R372, R373, R374 -- OPEN at 4a.** R373 bites again in this
  verdict header.
- **R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350 second
  half, R330, R331, R332 -- OPEN at 4a, correctly listed.**
- **R231, R244, R245, R275 -- OPEN, unblocked.** Step R has not run.
- **R230, R261 -- OPEN by instruction, correctly listed.**
- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a.**
- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 12 status-versus-subject disagreement stays at 4a.
- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** R250,
  R251, R226, R227, R264 and R266 still have no row; R348 territory.
- **R365-R369, R375-R382, R384 -- carried in `step-5-answers.json`.**
- **R223, R224, R394-R399, R403-R409, R412, R415-R418, R420, R421-R430,
  R434-R446, R448-R457 -- closed earlier**, not reopened.

## Findings

**First, what is right, and it is again the larger part.**

**THE GENERATED SURFACE GREW AND IT IS FAITHFUL.** I re-ran all three new
generators at `b21760b`: sections 0a, 0b and 0c each reproduce byte for byte,
with only the rows that post-date the report added. `rounds_runs()` selecting
by time is a real fix and I tested the mechanism itself -- given an anchor
that reaches last round it labels `35561482997` at `2bd9e89` *head not in
current history*, which is precisely what R461 said could not happen. The
`gh` cross-check is the right answer to R462 and it fails rather than
skipping; the token commit exists because it did fail, in CI, on the run
before.

**AND THE GATE HAS NOT MOVED.** `floatfea/` carries no executable change for
the eighth consecutive round; rung 1 is green in my run and in CI at the
commit I judge, and the ten determinism legs ran green there for the first
time in many rounds.

---

**R467. (BLOCKS -- CP2, fourth round running, and it is the head. The figure
R460 WITHDREW is republished, one commit after the withdrawal, in the file
that answers R465.)** `.claude/hooks/stale-before-commit.sh:35-37`.

```
code :35 "# The survivors are reported, not decided: every one needs a look,
     :36  and the measured false rate on a real round was four in five. The
     :37  reason carries the whole list so the decision is made against the
          lines rather than the count."
rule THE RULE THIS FIGURE IS MEASURED AGAINST CHANGED LAST ROUND. R460
     withdrew `5 survivors, 1 TRUE and 4 false` because no command at that
     commit produced it; the measurement that replaced it is 14 survivors,
     0 true.
cmd  python scripts/precommit_stale.py afc5b05^..afc5b05
out  11 numbers, 0 renamed rows, 0 changed classes; 14 survivors
judge 14 AND 0, NOT 4 AND 5. `four in five` IS THE WITHDRAWN RATIO, exactly:
     4 false of 5 survivors.
cmd  git show -s --format=%B 706d4e6 | grep -i fourteen
out  "the measured false rate on the one round it has been run against is
     fourteen reports and zero defects"
judge THE COMMIT MESSAGE IS RIGHT AND THE FILE IT COMMITS IS WRONG. Same
     commit, same author, same minute.
cmd  git log -1 --format=%h -- scripts/precommit_stale.py
out  eb5a19c -- the docstring was corrected in the commit BEFORE this one,
     and correctly: it names the command, prints 14, and records 0 true.
cell ONE VARIABLE, THE FILE. Three places in this round carry the figure:
     the module docstring (14/0, right), the commit message (14/0, right),
     the hook comment (4-in-5, the withdrawn one). Nothing distinguishes
     them but which file the sentence was typed into.
judge AND IT IS LOAD-BEARING. The sentence is the stated reason the hook
     ASKS instead of DENYING. A decision rule justified by a figure the
     previous verdict withdrew is the BP0 shape exactly, in the commit
     answering the finding that withdrew it.
```

  **Closed when** `:35-37` carries the figure a named command reproduces at
  the commit publishing it -- fourteen survivors, zero true -- or carries no
  figure and points at the `scripts/precommit_stale.py` docstring, which
  already has it. The BI3 remedy.

**R468. (BLOCKS. Three published provenance sentences, each refuted by
running the command it names -- and one shipped test asserts the wrong
string is present.)** `scripts/ci_section.py:139-144`, and sections 0a, 0b
and 0c of `docs/reports/F2/step-5.md`.

```
code :139 `def _generated_by(number, sha, legs: bool = False)`
     :140 the flag is set to ` --legs` when `legs` is true and to the empty
          string otherwise, and `--legs` is the only flag it can ever be
judge `rounds_section`, `history_section` and `commits_section` all call
     `_generated_by(number, sha)`, so all three publish the line
     `Generated: python scripts/ci_section.py`.
cmd  python scripts/ci_section.py | head -1
out  ## 0. CI at `6170263`, the commit verdict 51 judged -- conclusion
     **SUCCESS**
judge A READER WHO RUNS THE NAMED COMMAND TO CHECK SECTION 0a GETS SECTION
     0. The three sections added or rewritten this round to make the CI
     record reproducible each name a command that reproduces a different
     section.
cmd  the actual commands, which I had to find by reading main()
out  --rounds, --history, --commits. All three reproduce byte for byte.
code tests/test_report_carried.py:1358 asserts that the string
     "Generated: `python scripts/ci_section.py`" is in the generated text
judge SO THE GUARD REQUIRES THE FALSE STRING. Adding the flag to
     `_generated_by` reddens that assertion, which is why this is a finding
     about two files and not one.
judge THIS IS THE ROUND OWN SUBJECT. CY0 through CY4 are about a report
     whose facts are generated rather than typed; the one sentence that says
     WHICH generator produced a section is wrong in three of the four.
```

  **Closed when** each generated section provenance line names the
  invocation that reproduces it -- `--rounds`, `--history`, `--commits` --
  and `tests/test_report_carried.py:1358` asserts the string the generator
  now writes.

**R469. (BLOCKS -- CW0. The guard own docstring states a property the
inverted rule does not have, and I measured six unseen shapes through it.)**
`tests/test_tree_prose_consistent.py:42-50` and `:428-445`.

```
code :43 "A command whose answer is `none` or a count proves nothing unless
     :44  the needle it searches for CAN BE FOUND AT ALL."
     :49 "Every such triple names a planted line ... and this file asserts
     :50  the same needle is found there. A needle that cannot match fails
          its control."
judge UNDER EQUALITY THE NEEDLE IS THE PLANTED LINE. `control_defect` now
     asks whether the control text EQUALS the needle, so "the same needle is
     found there" is true by construction for every needle a triple
     registers, and establishes nothing about findability. The check is a
     REGISTRY.
cmd  the shipped control_defect(), and test_a_prose_triple_still_says_what_
     the_tree_says, on ten unseen shapes, each with one control line added
     whose text IS the needle
out  SHIPS GREEN, 6 of 9 defect shapes: a misspelled constant
     (`RIGID_MODE_FLOR`, out `none`); a unicode-hyphen lookalike; the
     lower-cased constant name; an English sentence nobody would write; a
     nonsense token; and `defined("RIGID_MODE_BONUD")` with the misspelling
     planted -- which is the SHIPPED shape
     `defined_of_a_misspelled_constant`, refused today only because its
     `ctl:` is empty, and not because the misspelling is detected.
out  1 refused, and by the R443a empty-glob raise rather than by
     control_defect. 2 are stale-sentence entries. The control stays allowed.
judge 0 OF 9 REFUSED BY THE FUNCTION THE RULE LIVES IN.
code :443 rule 3 reads "THE NEEDLE MATCHES ITS OWN CONTROL AND NO OTHER. A
     needle matching several planted lines is a needle nobody has thought
     about." Under equality a needle can match several planted lines only if
     two plants are byte-identical, which is not what that sentence
     describes.
judge THE INVERSION IS STILL THE RIGHT DIRECTION and I want that recorded:
     it refuses all four of my re-admissions through shipped controls, and
     a file of bare needles is easier to read adversarially than a file of
     plausible fake code. What is not true is the sentence above it.
```

  **Closed when** `:42-50` and `:428-445` say what the rule now does -- a
  needle is registered, by exact text, and registration is a decision a
  reader can see rather than a demonstration that the needle can match -- or
  the rule acquires the property the docstring claims. The mechanism choice
  belongs to 4a; the sentence is this step.

**R470. (BLOCKS -- half of an item is not the item. R461 is published as
`answered` with two of the three parts its condition named absent from the
report, and absent from the table whose job is to declare a site left.)**
`docs/reports/F2/step-5.md` sections 2, 3 and 4.

```
code s2 the row reading R461, class blocks, state **answered**, where
        section 2, site docs/reports/F2/step-5.md
code v51 "Closed when section 9 out is what `git log --oneline` prints at
     the report own commit, AND the report states in one sentence that the
     `docs:` commit was split after
     test_a_docs_commit_does_not_also_edit_the_guard_that_judges_it refused
     it, NAMING run 35561482997 at 2bd9e89 as a run of this round that
     section 0a cannot show, and why."
cmd  a case-insensitive grep over revision 26 for 35561482997, 2bd9e89,
     split, rewrit and force
out  four hits, ALL of them the generic mechanism prose in the section 0b
     provenance line and in section 1. NEITHER the run id NOR the split
     sentence appears anywhere in revision 26.
cmd  read section 3, generated by scripts/untouched_sites.py, for an R461
     row
out  no R461 row at all. Section 3 carries rows for R459, R460, R462, R464
     and R465.
judge SO THE SITE WAS NEITHER ANSWERED NOR DECLARED LEFT, and the status
     cell says `answered`. CLAUDE.md records this shape by name because R29
     did it.
judge THE SUBSTANCE IS LARGELY DONE AND I SAY SO ABOVE: the mechanism is
     built, I tested it against a real orphaned head, and it would have
     caught last round rewrite. What is missing is one sentence and a run
     id -- the cheapest half of the item, left out of the half that was
     expensive.
```

  **Closed when** revision 27 either carries the sentence and the run id its
  condition named, or carries an R461 row in section 3 stating the site was
  left and why -- with the argument, which is a good one, that sections 0a
  and 0b now make it structural.

---

**Recorded, and lock items for step 4a (BU0). None of these touches the gate
assertion, a tolerance, or the truth of a published figure.**

**R471. The generated/hand-written split now keys on a string the
implementer types, so R463 moved house rather than closing.** Measured at
`b21760b` by calling `_generated_text`, `_hand_written`, `ci_table_defects`
and `_RUN_ID` directly, with the lookup injected. Adding the single line
`<!-- generated: scripts/ci_section.py -->` under any heading makes the whole
section exempt: (a) a paragraph naming a real run with a false story, and
(b) the same paragraph naming run `99999999999`, are both ALLOWED -- these
are the two shapes the shipped `_REPORT_SHAPES` refuses without the marker.
(c) The regex captures the script name in group 1 and discards it, so a
marker naming `scripts/no_such_script.py` works identically. (d) The span
runs from the heading before the marker to the next heading, so prose added
anywhere inside a genuinely generated section -- including two sentences of
false narrative appended after the last generated line of section 0a -- is
exempt too. Nothing re-runs a generator and compares. Five entries in
`tests/corpus/report_ci_section.txt`.

**R472. `ci_table_defects()` reads the outcome cell and nothing else, and
asks for non-emptiness rather than completeness.** Measured the same way.
(a) The head cell can name any commit: the green row rewritten to read head
`deadbee` passes, which is the ORIGINAL CE1 defect -- a table published for
a different commit than the one it describes. (b) The event cell can be
falsified from `workflow_dispatch` to `push`, which is the difference
between CI running on its own and a reviewer triggering it. (c) An outcome
cell reading `conclusion **failure** -- effectively success` passes, because
the test asks only that the `gh` word be *in* the cell. (d) Deleting both
failure rows and their failing-test blocks and keeping the green one passes:
the zero-row case I handed over last round is closed and the class is not,
because nothing asks `gh` which runs exist in the window. (e) The *head not
in current history* label -- the whole of the CY0 answer to R461 -- sits in
the unread head cell and can be deleted by hand without reddening anything.
Five entries in the same file. The remedy is the one the condition named:
compare the committed row SET with a fresh render, not each row against
`gh`.

**R473. The suite now requires an authenticated `gh` to pass anywhere.**
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` fails rather than skips
when `gh run view` returns nothing, which is what three verdicts asked for
and I endorse. The cost, which is written down nowhere: a clone without `gh`
or without a token cannot get a green run, and the message it gets is
`no such run` rather than `gh is not authenticated`. Distinguishing the two
is one test on the return code.

**R474. The section 0c out block is not what its cmd prints.** The
provenance line names `git log --oneline <judged>..HEAD`;
`commits_section()` reverses the list and truncates every line to 76
characters, so four of the six subjects are cut mid-word. The content is
complete and correct -- I compared it against the real command -- but a
reader diffing the block against the command gets six differences. Either
state the two transforms or drop them.

## Tolerances touched

**NONE. No constant was created, retired, or moved.**

```
cmd  git diff 7ffd67a..b21760b -- floatfea/ | grep -E "^[+-][A-Z_]+.*Final"
out  (empty)
cmd  git diff --stat 7ffd67a..b21760b -- floatfea/
out  floatfea/tolerances.py | 20 ++-   -- ONE FILE, every line a comment
judge NO VALUE WAS WIDENED AND NO VALUE MOVED. What changed is the two claim
     sentences R459 named, each now enumerating the third and fourth file,
     and each out block gaining the guard module. I verified both against
     `grep -rl <needle> tests/ --include=*.py`: three and four.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2575 passed at b21760b -- no undeclared literal entered tests/ this
     round and nothing was added to tolerance_marker_exemptions.txt.
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance touched this round** | -- | -- |

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**CY4 asked for PASS with the 4a list carried, or HOLD naming the head. The
head is R467** -- `four in five`, in `.claude/hooks/stale-before-commit.sh`,
which is the ratio verdict 51 withdrew, republished one commit after the
withdrawal, inside the file that answers R465, while the same round commit
message and module docstring both carry the corrected fourteen-and-zero.
That is not a number in passing: it is the stated reason the hook asks
rather than denies.

**Four items hold.**

1. **R467 -- the withdrawn figure, republished.** Lines 35-37 of the new
   hook.
2. **R468 -- three provenance lines naming a command that prints a different
   section**, and a shipped assertion that requires the wrong string.
3. **R469 -- the control rule docstring states a property the inverted rule
   does not have.** 0 of 9 unseen defect shapes refused by
   `control_defect()`; 6 ship green.
4. **R470 -- R461 published as `answered` with two of the three parts of its
   condition neither done nor declared left.**

**The finding behind the findings, sixth round running, and it has narrowed
once more.** Last round every hold was in the hand-written residue *around*
generated work, and the answer was to generate more. That worked: the
hand-written surface of the report is now one paragraph, six generated
sections reproduce byte for byte under my own re-runs, and **not one finding
this round is in the generated text of the report or in its one paragraph.**
All four are in prose the generation did not reach -- a hook comment, a
provenance string inside the generator itself, a guard docstring, and a
status cell. The species has not changed in six rounds: *a sentence stating
a fact about the code, written beside a repair, that one command refutes.*
What has changed is that the surface it can live on is now small enough to
read in full, which is how I found all four.

**Adversarial corpus (BE3): 22 new entries across two files, all unseen by
the implementer, committed separately at `217a5ce`.**

**`tests/corpus/report_ci_section.txt`, 55 to 66. Twelve entries: ten defect
shapes and two controls. The shipped guards refuse 0 of the 10; both
controls are caught.**

**`tests/corpus/prose_triple_shapes.txt`, 36 to 45. Ten entries: nine defect
shapes (six guard shapes, two stale-sentence observations, one boundary
case) and one allow-control. `control_defect()` refuses 0 of the 9; six ship
green through the whole module; one is refused by the R443a empty-glob
raise; the control stays allowed.**

**Coverage measurement: 0 of the 19 new defect shapes are caught by the
check written for its class, and 1 of 19 by any shipped assertion. LAST
ROUND IT WAS 2 OF 22, AND I WAS ASKED TO SAY SO IF IT HAD NOT MOVED. IT HAS
NOT MOVED -- IT HAS GONE DOWN.** That is not a regression in the guards,
which are stronger than they were: every one of the shapes I handed over
last round is now refused. It is the same measurement BE3 exists to produce.
A check verified against shapes its author transcribed from my previous list
catches that list, and the next list goes through. The implementer own
count -- eleven report shapes and five triple shapes, all refused -- is the
count of what I handed over, and it is not a coverage number.

```
cmd  python -m pytest tests/test_report_carried.py -q -k corpus  (after my adds)
out  test_every_corpus_shape_is_transcribed goes red on my 12 new CI ids,
     which is the R440 mechanism working. The 2575-pass run above is at
     b21760b, before my corpus commit.
```

**Not gates on step 5, into the next report Carried section:** R471, R472,
R473, R474, R458, R447 (restated), R383 (state changed -- the legs ran green
at `b21760b` and nothing banked the result), R419, R431, R432, R433, R410,
R411 (answered for revision 26, recurrence watch), R413, R414, R400, R401,
R402, R390, R391, R392, R393, R370, R371, R372, R373, R374, R362, R363,
R364, R354, R355, R356, R357, R347, R348, R349, R350 second half, R330,
R331, R332, the section 12 status-versus-subject disagreement, R321, R322,
R300, R291, R292, R281, R231, R244, R245, R275, R230, R261, the underlying
gap in R276, R277, R262, R264, R266, the two R248 residues, R249-R252,
R225-R228, R232, R233, and everything already at 4a.
**R459, R462, R463, R464, R465 and R466 are closed.** R460 is answered in
`scripts/` and reopened as R467 in `.claude/`; the R461 mechanism is closed
and its narrative reopens as R470.

**Fifty-two rounds have found no element defect and this round found none
either.** Rung 1 green in my run and in CI at the commit I judge; thirteen
jobs with real steps on Linux at `b21760b`, including ten determinism legs
and their agreement job -- the first legs to execute in many rounds, and the
one genuinely new piece of evidence about the code that this round produced.
It still means "not yet contradicted": ladder 5 has printed
`OK -- 0 directories ran` every time it has run, the leg result is in no
table, and V5.1 against CalculiX is the witness that has not spoken.
