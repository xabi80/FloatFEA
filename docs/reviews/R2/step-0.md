# Review — R2 step 0
Reviewed commit: 4c19570907a3f3f300222f9e95ffd79d95e26556
**Reviewed commit: `4c19570907a3f3f300222f9e95ffd79d95e26556`.**
Verdict: HOLD
Scope: **R2 step 0, REVISION 1 -- a REVIEWED REVISION, not an interim check.**
`docs/reports/R2/step-0.md` exists at this commit, so under ES0 this is **1 of step 0's
3 revisions** and **2 remain**. It closes nothing, so `--closes` is correctly absent (FK1).
**Ruled under FR1 with EZ0**, and each blocking finding names the silently wrong result it
produces. **GE3: `R835: unchanged, R2`. Not re-measured.**

**ITEM 1b IS THE FINDING, AND IT IS THE ONE COMPARISON A MACHINE WAS NOT GIVEN.** The
report's header reads `Answers: verdict 61 @ c931885`. The newest verdict is **62**, at
reviewed commit `9e1092a`, written by commit `0901933`. **The invocation told me the header
names verdict 62 and `0901933`; it does not, and `grep` over the whole report finds
`verdict 62`, `0901933` and `9e1092a` zero times.** R1230 below, with the consequence
measured rather than asserted.

**4 / 4b / 4c, each diffed separately against `0901933`:** `floatfea/tolerances.py` 0 lines;
`.claude docs/SUPERVISOR.md` 0 lines, so **no STOP-class finding**; `tests/conftest.py`
0 lines, and `git ls-files -- tests/conftest.py 'tests/**/conftest.py'` returns
`tests/conftest.py` as it must. No new conftest, no new plugin.
**EU1 does not arise, measured not taken:** `git diff 0901933..HEAD | grep -cE '^[-+].*_COUNTER'`
is `0`. I ran the adversarial cases anyway and they are where R1226's closure came from.
**One correction to my own instructions, stated rather than worked around:** step 2 says
`git diff -- floatfea tests docs`, which **misses `scripts/`** -- where two of the three
repairs under review live. I diffed the whole commit.

Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`.**
* FV1 selection plus the deliverable regression test (`tests/unit`, the four root guards,
  rung 3 deck export, rung 4 G4.1, `tests/regression/test_f6_deliverable_agrees_with_itself.py`):
  **2 failed, 862 passed in 341.01s.** The two are conditions 4 and 6 by name --
  `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` and
  `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`. Both still open and
  correctly so. The report's `1 failed, 839 passed` is the same tree over a narrower
  selection: 862 - 839 = 23 is the deliverable file it did not include.
* **The six report-guard files, which the report did not run and left to me.** CI's wide
  selection, `pytest tests --ignore=tests/unit --ignore=tests/verification --ignore=tests/regression`:
  **146 failed, 1103 passed, 1 skipped in 595.04s.** Verdict 61 gave 187 and verdict 62 gave
  172 at `9e1092a`; **the answering report moved 172 -> 146.** Per file: `test_report_carried`
  151 -> 129, `test_report_guard_states` 20 -> 7, `test_report_numbers_are_sourced` 1 -> 8,
  `test_report_vocabulary_corpus` 0 -> 2. **EG3 (ii) is measured on my side; it is still
  owed on the report's.**
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`, `mypy floatfea`:
  **all clean, my own runs** -- 163 files unchanged, 45 source files.
* **NOT RUN LOCALLY, and I say which rather than implying coverage:** rungs 1, 2, 5, 6 and
  `tests/regression` beyond the one deliverable test. **No `floatfea/` file is in this diff at
  all** (`git diff --stat 0901933..HEAD -- floatfea` is empty), so FV1 puts the rest on CI.

CI: **run `44140076843` at the FULL sha `4c19570907a3f3f300222f9e95ffd79d95e26556` EXISTS,
so FP1 held.** `lint, unit and guards` **CONCLUDED FAILURE at step 10 `guards and
meta-tests`**, with `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all
**success** before it -- so the guards step is seen to have RUN rather than been skipped
behind an earlier red (CZ1 iii). **`the verification ladder` had NOT finished when I ruled**
(`in_progress` at 18:14:29Z, started 17:43:22Z -- 31 minutes): **rungs 1, 2 and 3 SUCCESS**, rung 6 running,
**rungs 4 and 5 unmeasured.** A run that has not finished is not a pass. Both determinism
jobs `skipped` by their own `workflow_dispatch` condition. **NOT CK2** -- runners
`1000001920` and `1000001921` were assigned and both jobs executed for minutes.
**CA2 IS REACHED: CI IS RED AT THE JUDGED COMMIT.** CI's per-id list is **unavailable, not
skipped over**: `gh run view --job 134240156555 --log-failed` answers *"run 44140076843 is
still in progress; logs will be available when it is complete"* -- but my own wide run IS
that job's selection, so nothing hides inside CI's aggregate that I have not measured.
GC2 does not arise: the diff touches `scripts/` and `tests/`.

Door (FV2 / GG2): `git worktree add -b review/4c19570907a3 <a path outside the repository>
4c19570907a3f3f300222f9e95ffd79d95e26556` **succeeded on the first try, so no review of
this commit existed.** Every measurement above was taken in that worktree; this verdict is
written there through `scripts/write_verdict.py` (`grep -nE '"(commit|add)"|check_call|\.run\('`
over it: no match), committed on that branch and pushed -- merge with `git merge --ff-only
origin/review/4c19570907a3`. **My own writes, all in my own worktree and all reverted before
committing:** the verdict file moved aside and back (cell A), a planted
`docs/reports/R2/step-1.md` with the plan marker at 0 and 1 and back (cell B), the report
moved aside and back (the vocabulary cell). `git status --porcelain` in my worktree is empty
but for the corpus file, which is committed separately at `91f083d`.
**Outside the repository, read-only:** `git -C <HSP-stable|HSP-runs>
hash-object/rev-parse/status/check-attr/config`, and three throwaway `git init` trees under
my scratch directory for the R1226 cells. Nothing wrote a byte into either HSP worktree or
into `C:\dev\floatfea`.

**AND A DISCLOSURE, BECAUSE IT IS THE HAZARD FV2 EXISTS FOR AND IT WAS LIVE WHILE I RULED.**
`C:\dev\floatfea` was clean when I was invoked and is **dirty now** -- `git status --porcelain`
there shows `docs/reports/R2/step-0.md`, `docs/reports/R2/step-0-answers.json`,
`tests/test_report_carried.py` and `tests/test_report_guard_states.py` modified. Those are
four of the five files I judged. **Every read I took was of the commit, in my own worktree,
so the addendum-29 defect did not arise** -- but in a shared checkout it would have, on
exactly these files, and the reading would have been of work that is not in `4c19570`.
I judged `4c19570` and nothing else.

## Carried

Verdict 62's five numbered conditions, plus the header requirement and the EG3 (ii) paste it
closed on. **TWO ANSWERED AND CLOSED, ONE HALF-ANSWERED, THREE OPEN, AND THE HEADER
REQUIREMENT FAILED.**

* **R1226 (the stable key, R1213 one key over) -- ANSWERED AND CLOSED, both limbs, and I ran
  the control and the direction the commit did not.** The refusal is inside `_source()`, not
  at module level, so it cannot take a rung down in collection. Six values through `--check`,
  with exit codes measured separately because a pipe to `tail` hides them:
  ```
  cmd  FLOATFEA_HSP_STABLE=<...>/HSP-runs    export_buoy_centers_ref.py --check
  out  REFUSED: the STABLE key resolves to ...\HSP-runs, which is not an HSP-stable
       worktree ... records a source it did not read (R1226)            exit 1
  cmd  FLOATFEA_HSP_STABLE=<...>/HSP-stable  (the control)
  out  EB6 reference: current. blob b8b8123904af, tag floatfea-ref-1    exit 0
  cmd  <...>/HSP-stable/../HSP-runs
  out  REFUSED ... resolves to ...\HSP-runs   -- `resolve()` normalises the hop, so the
                                                 classic bypass is closed
  cmd  a REAL directory named HSP-stable-copy, source present and committed
  out  REFUSED by the name predicate          -- measured with the existence refusal cleared,
                                                 so the predicate is what fired
  cmd  C:/nope/HSP-stable  and  C:/nope/not/a/tree
  out  R1214's "declared and is not a directory" refusal, which fires first
  cmd  <...>/hsp-stable  (case-folded, existing)
  out  current  -- correct: `resolve()` restores the on-disk case, so it IS the tree
  ```
* **R1226's SECOND LIMB -- THE CHOICE IS RIGHT, AND THE REASON IS STRONGER THAN THE ONE THE
  DOCSTRING GIVES.** You asked me to rule on hashing the working file against `--dirty`.
  **Hashing is correct**, and measurements say so rather than the argument:
  ```
  cmd  git -C HSP-stable hash-object <rel> ; git -C HSP-stable rev-parse HEAD:<rel>
  out  b8b8123904af...   b8b8123904af...      -- IDENTICAL on a clean tree
  cmd  git -C HSP-stable config core.autocrlf ; git check-attr text eol -- <rel>
  out  true ; text: unspecified, eol: unspecified
  rule `git hash-object <path>` applies the attribute filters, so CRLF working bytes hash to
       the LF blob. Had it not, `data/platform/buoy_centers_ref.json` would have STOPPED
       REGENERATING at this commit -- R1223's shape -- and `--check` would be a third red.
  cell ONE VARIABLE, the working file's bytes, in a throwaway git tree named HSP-stable:
         clean                              -> "current"
         comment-only edit, no value moves  -> "the VALUES match but the source blob moved,
                                                b8b8123904af -> 48391dd3de42"
         Z_HUB_REF edited                   -> "STALE -- hub_positions_xyz_m differs"
       and the OLD code on that same dirty tree: `rev-parse HEAD:<rel>` still returns
       `b8b8123904af`, so `--check` would have printed `current`.
  judge `--dirty` would have said "something here is uncommitted" while publishing
       `b8b8123904af` beside numbers that did not come from it. The hash makes `check()`'s
       own `blob_sha` comparison (`:172-180`) the thing that catches it, and that comparison
       already ships. Your docstring's reason is right; this is the measurement of it.
  ```
  **The residual, stated rather than left:** a real directory *named* `HSP-stable` holding
  other content still prints `current` (measured). A name predicate is defeated by a name and
  always will be; what covers the rest is the blob sha, which catches any tree whose bytes
  differ. The pair is sound. The shapes nothing catches are in my corpus below.
* **R1227 (R1206's fourth site) -- ANSWERED, AND I WITHDRAW THE `_PAIRED` HALF OF MY OWN
  CONDITION.** `assert REPORTED & REVIEWED` is the right predicate and `:217` does **not**
  need to move. You asked for this explicitly; here is the cell.
  ```
  cell ONE VARIABLE -- the verdict file present or absent, at this commit:
         both present        -> REPORTED [0] REVIEWED [0] _PAIRED 0 STEP 0 STEP_REPORT 0,
                                test green
         verdict moved aside -> 1 failed at tests/test_report_carried.py:585,
                                "reports exist for steps [0] and verdicts for []; no step
                                 has both"
  rule `STEP_REPORT == _PAIRED` at `:606`, the assertion I said would go silently vacuous
  judge IT IS UNREACHABLE IN THAT STATE. `_PAIRED`'s `else 0` arm is taken exactly when
       `REPORTED & REVIEWED` is empty, which is exactly when the NEW first assertion fires --
       and it fires with a message that is TRUE. `grep -rn _PAIRED tests/ scripts/ .claude/`
       gives three code sites, all in this one file (`:217`, `:237`, `:606`), and `:237`'s
       use is sound in every state I constructed. The sequencing closes it, so my "treat
       `:229` in the same commit" was wrong: it asked you to change a line that is
       load-bearing for nothing.
  ```
* **AND THE MARKER MEASUREMENT IS WITHDRAWN TOO -- IT IS MINE, AND YOU WERE RIGHT TO ASK FOR
  IT RULED EXPLICITLY RATHER THAN LET IT STAND.** Verdict 62 recorded `marker 0 -> STEP 0` and
  `marker 3 -> STEP 0` and attached the cause *"the `else 0` arm is doing the work"*. The
  figures were right; the cause was not.
  ```
  cell ONE VARIABLE -- the marker, with a step-1 report planted beside the step-0 one:
         marker 0 -> _PLAN_STEP 0 _PAIRED 0 STEP 0 REPORT step-0.md
         marker 1 -> _PLAN_STEP 1 _PAIRED 0 STEP 1 REPORT step-1.md
  judge THE MARKER DOES CONTROL WHICH REPORT THE GUARD READS. It had no effect at `9e1092a`
       because `3 not in REPORTED` -- only step 0 has a report -- not because the resolver
       ignores it. A measurement over one value of the other axis with a causal sentence
       attached: BG0, on my side of the loop. **Nothing to fix; the claim is withdrawn.**
  ```
* **"One, and this is it" -- ANSWERED, and the replacement is not decorative.**
  `assert not Path(relative).is_absolute(), "the probe value must be relative to mean
  anything"` is what stops the R1219 test passing on an absolute value, which is the shape
  R1229 was. The probe directory is out of the repository root, and `git status --porcelain`
  was empty after every run I made. **R1229 discharged.** One ledger note: `os.path.relpath`
  raises `ValueError` when `tmp_path` and the repo root are on different drives -- loud, not
  silent, so it is a note and not a finding.
* **R1225 (ii) -- THE RECORDING HALF IS ANSWERED; THE HOLDING HALF IS NOT, AND THE OBVIOUS
  REPAIR IS NOT A ONE-LINER. R1232 below.** The `environment` block is only built on a write
  run, which nothing covers, so I exercised it: it builds and serialises, and it is already
  informative -- `numpy 2.5.4 / scipy 1.18.1 / xarray 2026.4.0` against
  `BASELINE_CONDITIONS`' `2.4.4 / 1.17.1 / 2026.7.0`, three libraries off the artifact's
  basis, with `threads` all `null` and `openblas_coretype` `null`.
* **R1225 (i) -- ANSWERED FOR THE DECISION, NOT FOR THE CLAIM IT IS USED TO SUPPORT. R1233.**
* **R1225 (iii) -- ANSWERED.** Section 7 escalates under **FQ3** by name, does **not** trigger
  `R2.md` section 6 item 2, and says so. The implementer's tree shows no `data/` entry:
  **no write run was made.** This was the one decision in the step that could have
  republished a dozen figures in a file sent to Xabier, and it was taken correctly for the
  second round running.
* **Conditions 4 and 6 -- OPEN, UNCHANGED, AND CORRECTLY SO.** Both red in my own run, both
  recorded red with their cause named, neither cleared by writing a provenance. The staleness
  message now names three blobs rather than two because this commit touched
  `export_f4_dynamic_inputs.py`; that is the diff, not a new defect.
* **Condition 7 (a concluded GREEN ladder in CI at the follow-on sha) -- NOT MET.** Rungs 1-3
  are SUCCESS in CI at this sha, which is new and worth having. **Rungs 4 and 5 are still
  unmeasured in CI at any commit of this step.**
* **The header requirement -- FAILED. R1230.** **EG3 (ii)'s paste -- NOT DONE**: the report
  carries no report-guard count, because `<!-- WHOLE_SUITE -->` was never filled.
* **R1221 and R1228 -- STILL OPEN, and FF0 said "next commit". R1235.** **R1217, R1218 --
  still open**, unchanged and not answerable here; R1218 becomes CZ0 (b) when step 2 writes
  the entry. **The R1213 message assertion -- ledger, and the answer to your question is no:**
  `:209` asserts the two keys differ, so the identity path cannot fire and the assertion is
  not vacuous. It stays a ledger row and I am not asking you to narrow it in a round.
  **R1212, R1203, R1204 -- reviewer-side or Xabier's. R1224 -- mine, no action.**
* **Verdict 58's twelve items and verdict 59's four report items -- PARTLY ROUTED.** Section 8
  routes R1196-R1201 and R1186/R1188/R1189(c)/R1190/R1191/R1193 to step 1, which is a
  disposition and acceptable. Four of them (R1197-R1200) are nonetheless red as missing carry
  rows, which is R1230's consequence rather than a separate item.

## Findings

**R1230. (BLOCKS) THE `Answers:` HEADER NAMES VERDICT 61 WHILE THE NEWEST IS 62, AND THE
GATE'S FINDING SET IS COMPUTED FROM THE VERDICT THE HEADER NAMES. ITEM 1b.**

```
claim  the report answers the newest verdict
cmd    git show HEAD:docs/reports/R2/step-0.md | sed -n '5p'
out    Answers: verdict 61 @ c931885
cmd    sed -n '1,4p' docs/reviews/R2/step-0.md ; git log --oneline -1 -- docs/reviews/R2/step-0.md
out    # Review -- R2 step 0 -- ES0 INTERIM CHECK ... Reviewed commit: 9e1092a...
       0901933 review: R2 step 0 ES0 INTERIM CHECK at 9e1092a -- HOLD, two blocking findings
cmd    grep -n "verdict 62\|0901933\|9e1092a" docs/reports/R2/step-0.md
out    (nothing -- three needles, zero hits)
cmd    tests/test_report_carried.py:406-412 -- ANSWERED = _answered_verdict(REPORT_TEXT);
       VERDICT_TEXT = _verdict_text_at(ANSWERED); EXPECTED = _FINDING.findall(VERDICT_TEXT) | ...
out    ANSWERED = c931885, EXPECTED = 27 ids, and
         R1225 in EXPECTED: False  R1226: False  R1227: False  R1228: False  R1229: False
cell   ONE VARIABLE -- the sha in the header. `_verdict_text_at('0901933')` gives EXPECTED =
       32, and the five it adds are EXACTLY ['R1225','R1226','R1227','R1228','R1229'].
rule   tests/test_report_carried.py:514 test_the_answered_verdict_is_the_NEWEST_one, whose own
       docstring reads "Item 1b, mechanically ... A header naming a real but older verdict
       commit passed every check: the sha resolves, the findings parse, and the carry table
       is complete about a list that has been superseded."
out    FAILED -- "the report at `4c19570` is newer than the verdict at `0901933` and names
       `c931885`. Written with the newest verdict available, it must answer that one."
judge  That red names no finding and no site of the newest verdict, and its SUBJECT is not
       the commit carrying it -- it is measurable at this commit and it was. It fails the
       FS1/FT1 predicate in both limbs, so **CZ1 (iv) applies unchanged and it blocks.**
```

**The silently wrong result, in the form FR1 asks for -- two of them.** First: `EXPECTED` is
the domain of `test_the_report_carries_the_finding`, so **neither of verdict 62's blocking
findings is a parametrised case at this commit.** A revision that had answered nothing about
R1225 or R1226 would read green on the one gate CLAUDE.md says the whole arrangement exists
for -- *"the dependency list is part of what gets re-read at every step"* -- and the list it
re-read is the superseded one. That is assertion domain blindness on the gate whose domain
IS the dependency list. Second: `scripts/ci_section.py:203 _anchor()` reads **this same
header** (`_ANSWERS` at `:178`), so generating section 10 now produces a CI table anchored on
`c931885` and publishes it under the heading *"CI at the judged commit"* -- a wrong commit,
and therefore wrong pass/fail counts, in the mandatory section of the report GI6 sends to
Xabier, and silent because a CI table looks identical whichever commit it describes.

**And the report is split between two verdicts rather than simply stale.** Section 7 and all
three code comments answer verdict 62 (R1225, R1226, R1227 by name). The header, section 8's
table, `step-0-answers.json` and section 9's red trace answer verdict 61. The prose at
lines 8-12 asserts the opposite of what line 5 does -- *"This header names 61 because the
newest verdict is the one the guard checks against"* -- and its parenthetical enumerates
"61, 60, 59" with 62 absent. BP0 at the scale of a whole document: the body moved and the
header did not.

*Closed when* the header names `0901933` **and section 8 plus `step-0-answers.json` carry the
32-id list in the same commit.** Fixing the header alone makes it worse by five: the table has
no row for any of R1225-R1229, and it is also missing R1213, R1214, R1215, R1221, R1222,
R1223 and `R2`, which the verdict it *names* already demanded --
`test_the_report_carries_the_finding` is red on exactly those ten ids today. The 107
`test_every_named_site_is_touched_or_declared[...]` reds and the seven
`test_the_guard_survives_the_state[...]` reds are the same item: the harness copies the real
report into every planted tree, so `baseline` reports *"expected a clean run"* with 122 of
these inside it, and **the harness that holds the resolver in place is certifying nothing
while the carry list is short.**

**R1231. (BLOCKS) ALL THREE GENERATED SECTIONS ARE UNFILLED PLACEHOLDERS, AND CI IS RED AT
THIS COMMIT, WHICH IS THE EXACT STATE CE1 WAS ADOPTED FOR.**

```
cmd    tail -6 docs/reports/R2/step-0.md
out    <!-- WHOLE_SUITE -->   ## 10. CI at the judged commit   <!-- CI_SECTION -->
cmd    pytest -q tests/test_report_carried.py -k "CI_SECTION or REVIEWED_commit or
       counts_are_not_all_zero or ROUNDS_SECTION"
out    test_the_report_carries_a_CI_SECTION  "the newest report revision has no
         `## ... CI ...` section"  assert '' -- the section body is EMPTY, not a placeholder
         that parses
       test_the_CI_section_is_about_the_REVIEWED_commit  "the CI section names no commit"
       test_the_reported_CI_counts_are_not_all_zero      "the shape without the measurement"
       test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph  "no `## 0a` table"
rule   CLAUDE.md section Step gating: "A report is its generated sections plus at most one
       hand-written paragraph." This report is the hand-written paragraphs and none of the
       generated sections.
judge  Four reds, none naming a finding or a site of the newest verdict, and none whose
       SUBJECT is this commit: a run exists at this sha (`44140076843`), FP1's push happened,
       so `python scripts/ci_section.py` and `--rounds` were both runnable here. They fail
       the FS1/FT1 predicate in both limbs, so **CZ1 (iv) applies unchanged.**
```

**The silently wrong result.** CI is **red at the judged commit** -- `lint, unit and guards`
concluded `failure` -- and no revision of the report says so. CE1 was adopted because CI had
been red at three consecutive reviewed commits with no revision saying so; this is the fourth,
and the report GI6 sends to Xabier carries no CI status at all. **Order matters and it is the
operative instruction: fix R1230 first.** Generating the section against the present header
anchors it on `c931885`, which replaces "no CI status" with "a CI status about the wrong
commit", and the second is worse than the first.

**R1232. (DOES NOT BLOCK -- the condition stands for the write run) R1225 (ii) IS RECORDED AND
NOT HELD, AND `pin_threads()` CANNOT BE WIRED AT THE CALL SITE THE DIFF CREATED.**

```
claim  the generation environment is "recorded in the provenance and held at the point of
       generation", which is what verdict 62's condition (ii) says
cmd    grep -n "pin_threads\|determinism\." scripts/export_f4_dynamic_inputs.py
out    :554  **determinism.report(),     -- and no other hit. `report()` only.
cmd    sed -n '64p;72p' scripts/export_f4_dynamic_inputs.py ;
       grep -n "Call before importing numpy" floatfea/determinism.py
out    64  import numpy as np
       72  from floatfea import determinism, hsp_pin  # noqa: E402
       floatfea/determinism.py:96  """Fix every BLAS/OpenMP thread count. Call before
                                      importing numpy."""
judge  **THE RECORDING HALF IS DONE AND IS THE RIGHT HALF TO DO FIRST.** An unpinned run now
       records `threads: {all null}` and `openblas_coretype: null`, which is a TRUE statement
       about the run, so an unpinned write run is loud rather than silent -- which is why
       this does not block under FR1. **The holding half is open, and the one-line repair is
       not available at `:72`:** the only import site the diff created is eight lines AFTER
       `import numpy as np`, and `pin_threads`'s own documented precondition is the opposite.
       Wiring it there would write `threads: {"OMP_NUM_THREADS": "1", ...}` into the
       provenance of a run whose BLAS had already initialised at the ambient count -- a
       provenance field that is false, which is strictly worse than the null it replaces.
       I did NOT measure a thread count and I assert none: there is no `threadpoolctl` here.
       What I assert is the documented precondition and the two line numbers.
```
*Closed when* either the pin is set before `import numpy` and the provenance records the
pinned values, or the write run is launched with the five `THREAD_ENV` variables set in its
environment and the report says that is the mechanism. **Either way: no write run before it.**
One ledger note on the same block: `baseline_conditions` is a tuple of prose sentences while
`versions` is a dict, so nothing can compare the two without a parse. Recorded, not asserted,
is what was asked for, so this is a note.

**R1233. (DOES NOT BLOCK) R1225 (i) IS SATISFIED FOR THE RULING AND NOT FOR THE SENTENCE IT IS
USED TO SUPPORT. ~200 eps IS CONSISTENT WITH THE PIN -- HERE IS WHY, SINCE YOU ASKED.**

The three rows are arithmetically right -- I recomputed every ratio and every eps count from
the pasted maxima (`4.3670e-14 / 196.7`, `8.5350e-15 / 38.4`, `5.4106e-15 / 24.4`) -- and the
answer is **yes, and the bound is two lines rather than a feeling**: a sequential convolution
over `N = 884` steps accumulates round-off between `sqrt(N) * eps` and `N * eps`, i.e.
**30 eps to 884 eps**, and 196.7 eps sits inside that band. `4.37e-14` relative is **twelve
decades** below the `1e-3` I named as "a different and larger finding" and ten below the six
figures `U = 1.71167` is published to. **It is round-off. Your reading is correct, and the
self-correction of the `1.210e-01` probe -- an elementwise ratio anchored on near-zero
entries, which measures the entry and not the array -- is the right diagnosis of the right
error.**

**What one case does not support is the sentence attached to it.** `--check` names **36 of
100** arrays across **six** cases; section 7 measures **three arrays of one case**. The
conclusion *"no published number can move"* is a claim over all six periods taken from one,
and `results/R1/example/member_forces.csv` publishes `G4.1` rows at every period. The
mechanism is period-independent and I expect the other five to look the same -- which is the
point: an expectation is what a measurement is for. **This does not block and is not a
condition of step 0**, because option 2 is not being taken and nothing is republished. It
**is** a condition of choosing option 2: the other five cases are measured before any
re-base, or the sentence is reduced to "at the governing period".

**R1234. (DOES NOT BLOCK -- FF0, next commit) `tests/test_report_vocabulary_corpus.py` HAS TWO
NEW REDS AND THEY ARE MINE, NOT YOURS.**

```
cmd    pytest -q tests/test_report_vocabulary_corpus.py, report present vs report moved aside
out    report present -> 2 failed: legitimate_open_row, two_spaces_before_the_item_number
       report absent  -> 32 passed
cmd    grep -n "legitimate_open_row\|two_spaces" tests/corpus/report_status_vocabulary.txt
out    :58  expect=allowed measured=allowed     row=| R231 | **open** - Q8 is locked; ... |
       :97  expect=allowed measured=allowed...  row=|  R230 | **answered** in section 1 |
judge  **BOTH `measured=` FIELDS WERE RECORDED IN A TREE WITH NO REPORT, WHERE THE GUARD
       COULD NOT RULE AT ALL.** `allowed` there meant "never evaluated", not "allowed" -- a
       baseline taken in a vacuous state, which is this project's own recorded guard applied
       to my own directory. The moment a report exists the shipped guard refuses two row
       shapes the corpus declares legitimate. Under FR1 the outcome is a refusal and so is
       loud, which is why it does not block; it is gating apparatus, so FF0 rather than the
       ledger. **I have NOT edited the corpus to match the guard** -- that is widening by
       another name -- and the test's own message names the two exits: repair the guard so a
       two-space indent and a hyphenated open row are ruled on, or declare the disagreement
       with a reason. The first is yours under EK2; if the guard turns out to be right, the
       re-measurement is mine and I will take it next round.
```

**R1235. (DOES NOT BLOCK -- FF0, and it was due in THIS commit) R1221 AND R1228 ARE
UNCHANGED.** Verdict 62's item 5 read *"R1227 and R1228 in the next commit (FF0, not the
ledger) ... R1221 is in the same file and belongs in the same commit."* This is that commit;
R1227 and R1229 are in it, these two are not, and the commit does not say they were left.
Measured: `tests/test_report_guard_states.py:117` still quotes
`max(_PLAN_STEP if _PLAN_STEP in REPORTED else 0, _PAIRED)` against the code's
`_PLAN_STEP is not None and _PLAN_STEP in REPORTED` at `:236`; and `EXPECTED` at this commit
**literally contains `'R2'`** -- the phantom id is the first element of the 27 printed under
R1230. **Both in the next commit.**

**R1236. (DOES NOT BLOCK -- ledger) TWO FIGURES IN THE REPORT THAT ONE COMMAND EACH REFUTES.**
Section 6's R1205 block pastes `out  ('R2', 1) R2.md`; the command it names prints
**`('R2', 0)`**. Section 9 predicts `test_the_plan_names_the_step_under_execution` "stays red
on the sentinel collision"; it **passes** (`1 passed`, measured), as verdict 62 and `R2.md:15`
both already recorded. The second is the more useful of the two, because section 9 is the
report's red trace and it predicts a red that does not exist while omitting the one that
blocks. Report prose, so FR1 does not block it -- but EG3 (i) asks for every red traced by
name, and the trace that exists is wrong in both directions. Also ledger:
`test_every_number_in_prose_is_sourced_in_its_own_section` is red on the preamble and on
sections 2, 3, 6, 7, 8 and 9, plus `test_a_table_of_numbers_shows_where_it_came_from[8.
Carried]`.

**WHAT THIS COMMIT GOT RIGHT, AND IT IS THE LARGER PART OF IT.** GI3 (a) is the measurement I
most expected to have to re-derive, and it reproduces exactly: I rebuilt the momentum balance
from `case1/m_xddot`, `case1/contrib` and `case1/pair_body` myself and got `2.414413e+01`
against `2.414287e+01` on the platform and `1.4537e+01 / 1.4534e+01` on hub1, ratio 1.0001 --
the report's own table -- and the judgement that a "share" between the two sides is 1:1 by
construction is right, and is the honest answer to a question GI asked in a form the model
cannot answer. The static/dynamic decomposition is exact: `269.72` and `455.72 MPa`,
`My static 1.916016e+08`, `Mz dynamic 2.689043e+08`, and the dynamic `My` of `-1.141810e+07`
is `total_instant - static` to the digit, all read out of the published CSVs. All six
utilisations check (`1.71167` twice, `1.18223`, `1.17709`, `0.808211`, `0.790493`). Section
2a's loop-gain table is internally consistent at every one of its 24 cells and its control
`2059.7 t` reproduces; section 5's deck census is exact on all 17 bodies and `43 005 t` is
`344.04 kg x 50^3` to the tonne. **And three figures were corrected against the author's own
earlier statements before anyone asked** -- 74 minutes to 26, the ballast sign, and the
`1.210e-01` probe -- each with the reason the first version was wrong. The
`(1 - 0.75) x 2500` corroboration in section 4 is the kind of cross-check that catches a
basis error, and it is the second time this step has found one that way.

## Tolerances touched

**None, measured twice.** `git diff 0901933..HEAD -- floatfea/tolerances.py` is 0 lines, and
`git diff 0901933..HEAD | grep -cE "^[-+].*_COUNTER"` is `0`. **EU1 therefore does not
arise**, and I ran the model at configurations the diff did not choose anyway -- which is
where R1226's closure and R1234 came from. One tolerance-shaped thing remains implicated and
is not a tolerance: `--check`'s comparison is `np.array_equal` with no threshold, by Q8's
rule. **If any answer to R1225 introduces a tolerance on that comparison, that is a widening
and it is refused.** R1218's row-1 form question is still unwritten and becomes CZ0 (b) at
step 2.

## Corpus

**One batch, committed separately at `91f083d`: `tests/corpus/hsp_worktree_key_provenance.txt`,
28 entries, all new.** GC3 left the pause expired, so this is my own call under GA3's length
target. The surface is the one this step's only code change touches: GI3(e) turned a wrong
path from a MISSING directory into a RESOLVING one, so the question became whether the tree
that was read is the tree the artifact declares.

**12 of the 28 measured this round. 6 caught, 3 reach a green `--check`, 1 correctly needs no
refusal, 1 is not live on this tree, 16 carried unmeasured.** The three that get through:
a real directory *named* `HSP-stable` holding other content (`current`, exit 0); the stable
key set to the **empty string**, which falls through as unset and exits **0** with *"HSP-stable
absent, so the snapshot cannot be re-derived here"* -- a gate that could not compare returning
0, which is *empty parameter set is an error, not a skip*, and which is pre-existing rather
than in this diff; and a stable tree at another tag with byte-identical source, where nothing
is wrong because `hsp_tag` is a literal on both sides. Both entries verdict 62 said it would
write are in it, and `declared_tag_is_a_literal` is still live. **What I ran beside the batch**
is the recorded substitute, and it is where R1230 came from: a regeneration check on a
published deliverable (the EB6 snapshot, in a throwaway tree, in both directions) and a
continuum over the parameter space the new resolver guards.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN** -- which GI6 holds anyway, so this HOLD costs
no schedule, and you are right that it does not. **Rounds: this consumed revision 1 of 3
under ES0. Two remain.** R1226, R1227, R1229 and R1225 (iii) are **DISCHARGED and are not
re-measured**, and two conditions of my own are **WITHDRAWN** (the `_PAIRED` half of R1227,
and the marker's cause). What remains, in this order, because the order is load-bearing:

1. **R1230 -- the header to `0901933`, AND the 32-id carry list in the same commit.** Not the
   header alone: section 8, `step-0-answers.json` and the generated Carried table move
   together, or the next revision is red by five more than this one.
2. **R1231 -- `python scripts/ci_section.py`, `--rounds`, and the whole-suite line, AFTER
   item 1.** CI is red at this sha and the report has to say so.
3. **R1232 -- no write run until the pin is above `import numpy` or in the invocation's
   environment, and the provenance records the pinned values.** The recording half is done.
4. **Conditions 4 and 6 -- unchanged, still subordinate to R1225, still red with their cause
   named.** Do not clear the staleness guard by writing a provenance whose npz moved for an
   unrecorded reason.
5. **Condition 7 -- a concluded, GREEN ladder in CI.** Rungs 1-3 are green at this sha; 4 and
   5 have still never run in CI during this step.
6. **R1234 and R1235 in the next commit (FF0, not the ledger).** R1233's five remaining cases
   only if option 2 goes on the table.

**Nothing here is a STOP, and I considered it on the ladder.** Rungs 1, 2 and 3 are SUCCESS in
CI at this commit, which is the first time this step has had that; the two local reds are a
provenance comparison and a regeneration comparison rather than numerical disagreements at a
rung, and R1225 established that what moved is the committed golden and not the code. No
`floatfea/` file is in this diff. The locked plan is faithful to GI and needs no reopening,
and `R2.md` section 6 item 2 is still the one clause I rule must NOT be triggered yet.

**And I disagree with nothing in the criterion this round.** FR1 did the work it was adopted
for: R1233, R1234 and R1236 would each have been a blocking round under the unamended CZ0,
and each is a line here instead. The two findings that block are both "a wrong number in a
report, silently" with the sentence written out, which is the test FR1 asks for and the
reason it is cheap to apply.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 9e1092a35eed45ee5351789778a3c50752af1bb1
**Reviewed commit: `9e1092a35eed45ee5351789778a3c50752af1bb1`.**
Verdict: HOLD
Scope: **ES0 INTERIM CHECK on the OPEN step, the third.** `git ls-files docs/reports/R2` is
EMPTY, so no new report revision exists and this **counts against none of step 0's three
revisions** and closes nothing; `--closes` is correctly absent (FK1). Light per ES0: the
suite, CI at the commit, a CZ0 (a)-(d) scan of the diff. **Ruled under FR1 with EZ0**, and
each blocking finding names the silently wrong result it produces. **GE3: `R835: unchanged,
R2`. Not re-measured.** 1b does not arise -- there is no report, so there is no `Answers:`
header to compare against the newest verdict.
**EU1 does not arise, measured not taken:** `git diff 3d24e1c..HEAD -- floatfea/tolerances.py`
is 0 lines, so is `git diff 91c2d2e..HEAD`, and `git diff 3d24e1c..HEAD | grep -cE '^[-+].*_COUNTER'`
is `0`. I ran the adversarial case anyway and it is where both blocking findings came from.
**CH2/CI0: `git ls-files -- tests/conftest.py 'tests/**/conftest.py'` returns `tests/conftest.py`,
and `git diff 3d24e1c..HEAD` over it is 0 lines. No new conftest, no new plugin.**
**4b: `git diff 3d24e1c..HEAD -- .claude docs/SUPERVISOR.md` is 0 lines. No STOP-class finding.**
Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`.**
* `tests/unit` + the four root guards: **703 passed in 196.31s.** That is verdict 60's 692 at
  `3d24e1c` plus the new file's 10 plus one parametrised root-guard case over the new file.
* `tests/verification/rung4/test_f4_g41_dynamic.py` + `tests/regression/test_f6_deliverable_agrees_with_itself.py`:
  **2 failed, 138 passed in 146.11s.** The two are conditions 4 and 6 BY NAME --
  `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` and
  `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`. Both still open.
* the new file's revert-red-restore cycles, **run by me rather than taken**: R1214's `raise`
  reverted to `tried.append(...); continue` gives **2 failed, 8 passed**; R1213's name test
  disabled with `if False and ...` gives **1 failed, 9 passed**; **R1219's anchor removed
  gives 1 failed, 9 passed, a cycle the commit did not report**; all restored gives
  **10 passed**, with `git status --porcelain` empty.
* **CI's own wide guards selection**, `pytest tests --ignore=tests/unit
  --ignore=tests/verification --ignore=tests/regression`, in my worktree: **172 failed, 1057
  passed, 1 skipped in 555.85s**, and the reds are confined to THREE files --
  `test_report_carried.py` 151, `test_report_guard_states.py` 20,
  `test_report_numbers_are_sourced.py` 1. **No root test outside the report guards is red at
  this commit.** Per-id ruling under FS1/FT1 below.
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`, `mypy floatfea`:
  **all clean, my own runs** -- 163 files unchanged, 45 source files.
* **NOT RUN LOCALLY and I say which rather than implying coverage:** rungs 1, 2, 5, 6 and
  `tests/regression` beyond the one deliverable test. The diff's only `floatfea/` file is
  `hsp_pin.py` (32 lines) and the only rung tests reaching it are rung 3's deck export and
  rung 4's G4.1, both run above; FV1 puts the rest on CI.
CI: **run `44133344180` at the FULL sha `9e1092a35eed45ee5351789778a3c50752af1bb1` EXISTS, so
FP1 held.** `lint, unit and guards` **CONCLUDED FAILURE at step 10 `guards and meta-tests`**,
with `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all **success** before it
-- so the guards step is seen to have RUN rather than been skipped behind an earlier red
(CZ1 iii), and CI's `mypy` passes at the pinned toolchain this time. **`the verification
ladder` had NOT finished when I ruled** (`in_progress`, runner `GitHub Actions 1000001919`,
started 17:06:50Z); a run that has not finished is not a pass. Both determinism jobs
`skipped` by their own `workflow_dispatch` condition. **NOT CK2** -- runners `1000001918` and
`1000001919` were assigned and both jobs executed for minutes. **CA2 IS REACHED: CI is red at
the judged commit.** CI's per-id list is **UNAVAILABLE, not skipped over**: `gh run view --job
<id> --log-failed` answers *"run 44133344180 is still in progress; logs will be available when
it is complete"* while the ladder runs, so the id-for-id agreement with my local 172 is
deferred -- but my local run IS that selection, so nothing is hiding inside CI's aggregate
that I have not measured. GC2 does not arise: the diff touches `floatfea/` and `tests/`.
Door (FV2 / GG2): `git worktree add -b review/9e1092a35eed <a path outside the repository>
9e1092a35eed45ee5351789778a3c50752af1bb1` **succeeded on the first try, so no review of this
commit existed.** Every measurement above was taken in that worktree; this verdict is written
there through `scripts/write_verdict.py` (`grep -nE '"(commit|add)"|check_call|\.run\(' ` over
it: no match), committed on that branch and pushed -- merge with `git merge --ff-only
origin/review/9e1092a35eed`. **Writes of my own, all in my own worktree and all reverted
before committing:** the three revert cycles, a planted `docs/reports/R2/step-0.md` for the
R1227 cell, and the plan marker moved to `3` and back for the provenance cell.
`git status --porcelain` in my worktree is empty. In `C:\dev\floatfea` I ran only read-only
`git` and `gh`. **Two read-only things I ran outside the repository and disclose rather than
leave for you to find:** `git -C <HSP-runs> describe/rev-parse/status --porcelain`, and
`export_buoy_centers_ref.py --check` under two values of `FLOATFEA_HSP_STABLE` -- `--check`
compares and writes nothing (`:188`). Neither wrote a byte anywhere.

## Carried

Verdict 60's five conditions and verdict 61's two. **FIVE ANSWERED, TWO OPEN, and one of the
five answered its condition without closing its finding.**

* **R1213 (the DS0 refusal that did not fire) -- ANSWERED, verified three ways.** The name
  test is at `run_floatsim_design_waves.py:112-119`, **beside** the identity test at `:120`
  and not replacing it (EK2), and `test_the_DS0_refusal_fires_when_the_RUNS_key_names_the_STABLE_tree`
  drives `preflight()` rather than reading its source. Revert cycle: **1 failed**. And the
  adversarial case the commit did not run -- a **case-folded** value:
  ```
  cmd  Path('C:/users/xlama/onedrive/documents/buoy/hsp-stable').resolve().parts
  out  ('C:\','Users','xlama','OneDrive','Documents','buoy','HSP-stable')
       NAME TEST ("HSP-stable" in parts): True
  rule run_floatsim_design_waves.py:112; Windows `resolve()` restores the on-disk case for an
       existing path, so the predicate is not defeated by the casing of the declaration
  ```
* **R1214 (set-but-wrong silently discarded) -- ANSWERED AS WRITTEN, and the finding is not
  closed: see R1226.** The condition was *"a source that is set and not a directory is a
  refusal and only an unset source falls through"*, and that is exactly what shipped
  (`hsp_pin.py:120-126`, with the legacy sibling moved outside the loop at `:128-130`). Both
  directions (EH4): revert gives **2 failed**; unset still resolves through. **And the
  direction the condition did not ask for, measured because R670 is the reason
  `require=False` exists:** a set-and-wrong key now raises `SystemExit` from a module-level
  constant in six scripts, so I checked it cannot take a rung down in collection --
  `FLOATFEA_HSP_RUNS=C:/nope/not/a/worktree python -m pytest --collect-only
  tests/verification/rung4 tests/verification/rung3` gives **670 tests collected in 0.75s, no
  errors.** R670 is not resurrected.
* **R1206 (`0` is both a legal step number and the resolvers' sentinel) -- THE CONDITION'S
  THREE LINES ARE FIXED AND THE FINDING IS NOT CLOSED. R1227 below, with the cell.** Exit
  (iii) was the right exit and the escalation was rightly withdrawn; `_plan_step() is not
  None` is green, `check_carried._active_step()` is `('R2', 0)`, `ci_section` is `R2 0`, and
  `test_R887_the_plant_base_is_the_step_the_GUARD_reads` passes its `STEP == guard.STEP`
  assertion. A **fourth** site of the same `> 0` collision is live.
* **R1215 (the marker comment said the opposite of the marker) -- ANSWERED.** `R2.md:5-25`
  now reads `IT READS 0, WHICH IS WHAT IS UNDER EXECUTION`, with the withdrawn escalation and
  its refuting grep recorded. Read against the diff, not inferred.
* **R1216 (the census described the pre-change tree in the commit that changed it) --
  ANSWERED.** `R2.md:208-223` states BOTH counts and names why they differ. **R1219 --
  ANSWERED** (`hsp_pin.py:106-111`), and I measured the revert cycle the report did not.
  **R1220 -- ANSWERED**, with one defect in the new file: R1229.
* **CZ1 (iv), the rung-4 staleness red (condition 4) -- OPEN.** Confirmed red in my own run.
  **The diagnosis offered for it is refuted by a measurement already in this repository:
  R1225.**
* **R1223 (the published deliverable stops regenerating, condition 6) -- OPEN.** Confirmed
  red in my own run; the four differing lines are the same `pass` to `FAIL` and `116 passed`
  to `1 failed, 115 passed` cells verdict 61 named. **Not touched, which is right.**
* **Condition 7 (the follow-on commit's own CI run GREEN on the LADDER) -- NOT MET.** The
  ladder job at this sha is still `in_progress`, so **rungs 4 and 5 remain unmeasured in CI
  at any commit of this step.** That is the hiding CZ1 (iii) exists for; the condition stands.
* **R1222 -- ANSWERED, and the prediction verdict 60 recorded before measuring is
  CONFIRMED.** `test_a_blocking_item_is_not_routed_to_4a` is **green** at this commit, because
  the newest verdict writes dispositions in the parenthesised form the parser needs: that id
  plus `test_the_plan_names_the_step_under_execution` give **2 passed**. Withdrawn.
* **R1217, R1218, R1221 -- STILL OPEN**, unchanged and not answerable by this commit (R1218
  becomes CZ0 (b) when step 2 writes the entry; R1221 is FF0 and belongs with R1227 in the
  same file). **`declared` is still a config key no config declares.** **Verdict 58's twelve
  items and verdict 59's four report items -- STILL OPEN, due in R2's first report.**
  **R1212, R1203, R1204 -- reviewer-side or Xabier's. R1224 -- mine, recorded, no action.**

## Findings

**R1225. (BLOCKS) THE `--check` REFUSAL IS NOT THREAD COUNT. The npz golden moved when THIS
REPOSITORY'S OWN numpy/scipy PIN moved, and the ablation cell is already in the git history:
`--check` was GREEN before the pin and refuses after it, with the thread count unpinned on
BOTH sides.**

```
claim  `--check` ran with no thread pins, and the six named arrays are what multi-threaded
       BLAS would perturb  (the commit message's diagnosis)
cmd    git log --oneline -1 -- data/f4/dynamic_inputs.npz
out    62a8281  R1 step 1 revision 3
cmd    git show cfb76ff   (R1 step 2, first commit -- AFTER 62a8281, npz untouched since)
out    cmd  python scripts/export_f4_dynamic_inputs.py --check   (on the shipped npz)
       out  100 arrays reproduce the committed file EXACTLY      (exit 0, no stray file)
cmd    git log --oneline -S "numpy==2.5.4" -- constraints-dev.txt
out    09d5bc9  R1 step 2, revision 1: FQ0-FQ3, and a refusal site nobody had named
cmd    git merge-base --is-ancestor cfb76ff 09d5bc9 ; echo $?
out    0        -- the GREEN --check PRECEDES the pin move
cmd    constraints-dev.txt, the FQ3 block's own measured table
out    numpy  local 2.4.0   CI 2.5.4        scipy  local 1.17.1   CI 1.18.1
       "a minor bump in either can move the last bits of a linear solve. The verification
        ladder asserts at ULP scale, so 'can move a number' is not hypothetical here"
       "FQ3: if the golden moves under these pins, STOP and report rather than re-baselining."
cmd    python -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"
out    2.5.4 1.18.1          -- i.e. AT the pin, which is the value that moved
cmd    git grep -ln "pin_threads\|OMP_NUM_THREADS" -- scripts floatfea pyproject.toml
out    floatfea/determinism.py   floatfea/hsp_pin.py
       -- nothing in the export path pins threads, and nothing did at cfb76ff either
cell   ONE VARIABLE ACROSS THE GREEN/RED BOUNDARY. Thread count: unpinned at cfb76ff
       (green, 100 arrays EXACT) and unpinned today (red, 36 of 100 differ). numpy and
       scipy: moved, by the named commit, between the two.
rule   scripts/export_f4_dynamic_inputs.py:476-500 -- np.array_equal, Q8's golden rule,
       "there is no tolerance on this comparison"
judge  **THE THREAD COUNT IS HELD CONSTANT ACROSS THE BOUNDARY, SO IT IS NOT THE CAUSE.**
       The diagnosis cites `ci.yml:67-69`; three lines BELOW that citation the same file
       says *"THE BLAS KERNEL, PINNED (CF1). Thread count alone was not enough."*
       `OPENBLAS_CORETYPE` is unset locally. And 36 of 100 arrays differ while all 64 input
       arrays are bit-identical -- the signature of a solver-bit move, not of inputs that
       moved. Measured: HSP-runs is at `floatfea-ref-1` / `25de7ce`, clean but for the
       untracked `floatfea_design_waves/` export, so no input moved either.
```

**The silently wrong result, in the form FR1 asks for.** Condition 4 as verdict 60 wrote it
says *"then a full **write** run, which is the only thing that rewrites `import_closure`"*.
Executed on this machine that overwrites `data/f4/dynamic_inputs.npz` with arrays computed at
numpy 2.5.4 / scipy 1.18.1 / an unpinned OpenBLAS kernel, writes a fresh provenance **that
records none of those three** -- there is no `threads`, no `coretype` and no library version
in `dynamic_inputs.provenance.json`, I read every key -- and moves every `G4.1 force` and
`G4.1 moment` figure in `results/F6/floatfea_results_report.md`, a file sent to Xabier, for a
toolchain reason, **with the staleness guard and R1223's deliverable test both going GREEN to
confirm it.** That is CLAUDE.md's golden-file rule verbatim: *"Regenerating a golden file to
match new output, without that explanation, is the same error as widening a tolerance."* The
npz is the one canonical artifact that **cannot** be produced in the canonical environment --
CI checks out no HSP worktree, which is EX0's whole reason -- so Q8's "CI is canonical" does
not reach it, and `tests/test_ci_canonical_environment.py` reads the workflow, not this file.

*Closed when* three things are true. **(i)** The **magnitude** is measured and reported per
array -- max |fresh - committed| and its ratio to the array's own scale, with the operating
point. `--check` prints names only, correctly, because FP2/C20 made it a gate and not a
report; so this is a one-off probe under `/tmp`, not apparatus. A last-bits move (relative
`~1e-16`) is consistent with the pin; `1e-3` is a different and larger finding. *A residual
destroys information* -- 36 names cannot tell a wrong sign from a wrong magnitude. **(ii)** No
write run until the environment the regeneration runs under is recorded in the provenance and
held at the point of generation. `floatfea/determinism.py` already has `pin_threads` and
`report()` and nothing in the export path calls either, so this is wiring and not new
apparatus. **This answers your question directly: FF0-class, next commit, not a ledger row** --
`--check` is the thing that decides whether the committed npz is believed and whether `R2.md`
section 6 item 2 fires, it reported REFUSED with no defect established, and EK2 says a guard
that fails false is fixed. **(iii)** The escalation is raised under **FQ3**, not under `R2.md`
section 6 item 2. *"If it refuses again with the pins set, I read that as section 6 item 2's
escalation"* -- **no.** That item asks whether a **zero-change FloatSim re-run** is
bit-identical, and the premise is untested while numpy, scipy and the BLAS kernel all sit off
the values the artifact was built under; reopening the R2 plan on it attributes to FloatSim an
effect this repository has already measured twice, CF1 by CPU vendor and FQ3 by library minor.
FQ3's ruling already covers it: **STOP and report rather than re-baselining.** *A causal claim
carries its ablation*, and this one cost three `git log` commands. **If the pinned re-run in
flight comes back GREEN, R1225 still stands:** a bit-exactness gate whose answer depends on
unrecorded ambient conditions is the finding, and a pass does not record them either.

**R1226. (BLOCKS) R1213 ONE KEY OVER: NOTHING TIES THE TREE THE STABLE KEY NAMES TO THE TREE
THE SNAPSHOT DECLARES, AND I RAN IT WITH A CONTROL.**

```
claim  the two-key split makes a stable key pointed at the runs tree safe
cmd    FLOATFEA_HSP_STABLE=.../buoy/HSP-runs    python scripts/export_buoy_centers_ref.py --check
out    EB6 reference: current. blob b8b8123904af, tag floatfea-ref-1, 12 buoys and 4 hubs.
       exit=0
cmd    FLOATFEA_HSP_STABLE=.../buoy/HSP-stable  python scripts/export_buoy_centers_ref.py --check
out    EB6 reference: current. blob b8b8123904af, tag floatfea-ref-1, 12 buoys and 4 hubs.
       exit=0      (the control)
cell   ONE VARIABLE -- the tree the key names. The two outputs are BYTE-IDENTICAL and both
       exit 0, so the gate that certifies the EB6 reference cannot tell which worktree it
       was derived from.
rule   scripts/export_buoy_centers_ref.py:172  "source": f"HSP-stable/{SOURCE_REL}"  <- a LITERAL
                                         :176  "hsp_tag": hsp_pin.HSP_TAG            <- a MODULE CONSTANT
                                         :180  "blob_sha": _blob_sha(source)         <- from WHICHEVER tree
cmd    grep -n SystemExit scripts/export_buoy_centers_ref.py
out    :75 "is not a file"  :93 "could not read the blob sha"  :111 :135 :146 :167 (parse/shape)
       -- no DS0 name refusal, no tag refusal, no dirtiness refusal, on any line
```

**The silently wrong result.** `data/platform/buoy_centers_ref.json` -- a committed data file
and the input to EB6's label-provenance gate -- regenerated from the **runs** worktree while
its own `provenance.source` declares `HSP-stable/studies/platform-12buoy/platform_common.py`
and its `provenance.hsp_tag` declares `floatfea-ref-1`, **because both are literals that
cannot be wrong**, with `blob_sha` taken from the other tree's index so both sides move
together and `--check` prints `current`. That is FR1's second head verbatim, and CLAUDE.md's
own note on that head covers this case word for word: *"No number was wrong in any artifact at
the time, and the input was used other than as declared."* **Both worktrees are at the same
tag today -- `blob b8b8123904af` from either -- so nothing in the tree as it stands is wrong,
and I say so rather than overstating it.** `hsp_pin.py:36-46` states this hazard in prose and
names this file as the reason there are two keys; what it does not do is refuse it, and
GI3(e) is what made a key able to name the wrong tree at all, exactly as it did for R1213.
**A second limb, same file, from reading rather than running:** `:153` reads the constants
from the WORKING file (`source.read_text()`) while `:88-93` takes `blob_sha` from
`git rev-parse HEAD:<rel>`, so a dirty stable worktree records a sha for a version of the file
the numbers did not come from.

*Closed when* `export_buoy_centers_ref.py` refuses a stable key whose resolved path is not
`HSP-stable` -- the one-line predicate this commit just wrote at
`run_floatsim_design_waves.py:112`, inverted -- or declares the tree it actually read instead
of the literal; with both runs pasted and the control beside them (EH4). The dirtiness limb
closes with `--dirty` on the describe, or by taking the sha from the working file; **say which
and why**, not both.

**R1227. (DOES NOT BLOCK -- FF0, next commit, not the ledger) R1206's FOURTH SITE:
`tests/test_report_carried.py:579` still reads `assert STEP > 0`, and it goes red with a FALSE
message the moment the step-0 report lands -- which is your next commit.**

```
cmd    plant a minimal docs/reports/R2/step-0.md in my own worktree, then
       pytest -q tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    E  AssertionError: reports exist for steps [0] and verdicts for [0]; no step has
          both. There is no carry list to check.
       E  assert 0 > 0
       tests\test_report_carried.py:579
       1 failed   (and test_the_plan_names_the_step_under_execution: 1 passed)
rule   tests/test_report_carried.py:579, inside test_the_guard_reads_the_step_being_worked_on
judge  step 0 HAS both, so the message is FALSE -- `0` is the sentinel AND the value, which
       is R1206 verbatim at a site its three line numbers did not name. The condition asked
       for `:100`, `:111` and `:617`; those three are fixed and the finding is not.
```

Three things make this more than one line. **The assert is FIRST in its test, so three further
assertions in the same function are dead for the whole of step 0** -- the spelling check,
`STEP_REPORT == _PAIRED`, and `STEP_REPORT - STEP <= 1`, which is the one that forbids opening
step k+1 over an unreviewed step k. **The obvious repair makes one of them silently vacuous:**
`_PAIRED` at `:229` is `max(REPORTED & REVIEWED) if ... else 0`, so at step 0 the sentinel
equals the value there too -- fix `:579` alone and `STEP_REPORT == _PAIRED` passes at step 0
whether a verdict exists or not, which is loud today only because `:579` fires first.
**Treat `:229` in the same commit.** And it changes the class of one red next revision:
`test_the_guard_reads_the_step_being_worked_on` is state (2) today (`assert REPORTED`, no
report directory) and becomes **CZ1 (iv)** the moment the report exists, because the answering
report does not clear it. A third measurement, on provenance rather than existence:
`marker 0 -> STEP 0, REPORT step-0.md` and `marker 3 -> STEP 0, REPORT step-0.md`, so the plan
marker currently has **no effect** on which report the guard reads -- the `else 0` arm is doing
the work, and the repair's claim that the resolver follows the plan is not demonstrated by
this tree.

**R1228. (DOES NOT BLOCK -- FF0, next commit) `tests/test_report_guard_states.py:117` quotes
the expression this commit changed.** It reads *"The guard resolves `max(_PLAN_STEP if
_PLAN_STEP in REPORTED else 0, _PAIRED)`"*, while `test_report_carried.py:236` now reads
`max(_PLAN_STEP if _PLAN_STEP is not None and _PLAN_STEP in REPORTED else 0, _PAIRED)`. BP0 at
the smallest scale, inside the gating apparatus, and the same shape as R1215 which this commit
fixed one file over: a figure whose rule moved underneath it, in the file that exists to hold
the other guard's resolution.

**R1229. (DOES NOT BLOCK -- ledger, and the direct answer to your question)
`tests/unit/test_hsp_worktree_resolution.py:123` IS AN ASSERTION THAT CANNOT FAIL, and it is
the ONLY other one of that shape in the file.**

```
cmd    sed -n '121,123p' tests/unit/test_hsp_worktree_resolution.py
out        got = hsp_pin.worktree("runs")
           assert got.name == "HSP-runs"
           assert not got.is_absolute() or True  # the value is a path, existing or not
rule   `X or True` is True for every X -- in the file whose own docstring says "A check that
       cannot fail is not a check (CW0)", eleven lines above it
judge  Delete it; `:122` is the real check and it does fail if `worktree()` refuses or
       returns another name. I checked the other nine individually: four are held by the
       revert cycles I ran (R1213, R1214 twice, R1219), and the remaining five -- the
       precedence pair, key independence, `require=True`, the unknown key -- each drive
       `worktree()` or `preflight()` and assert on the returned value or the raised message,
       so each can fail. **One, and this is it.**
```

Two smaller notes against the same file, both ledger. The R1213 test's message assertion is
`"HSP-stable" in message and "DS0" in message`, and the **identity** refusal's message
(`"the runs worktree is HSP-stable, which is read-only from here (DS0)"`) satisfies both
clauses -- so the assertion cannot tell which of the two refusals fired, which is R1213's whole
content. It is not vacuous here, because `:209` asserts the two keys differ and the identity
path therefore cannot fire; a match on `R1213` or `by NAME` would make it say what it means.
And `:148-161` creates and `rmdir`s `HSP-runs-r1219-probe` **in the repository root**, outside
`tmp_path`, in the file whose docstring says *"NOTHING HERE TOUCHES A REAL WORKTREE"*: an
interrupted run leaves it behind, and `mkdir(exist_ok=True)` with an unconditional `rmdir`
deletes a pre-existing directory of that name. It cleaned up correctly in my run --
`git status --porcelain` empty.

**FS1/FT1 PER-ID RULING ON THE 172 REDS, checked against each id's own failure rather than by
family name (EG3 (i)).** State **(2)** throughout: a verdict exists, the answering report does
not, `git ls-files docs/reports/R2` is empty. **Limb one** -- names a finding or a site of the
newest verdict -- takes the 110 `test_every_named_site_is_touched_or_declared[R12xx-<path>:<line>]`
and the 27 `test_the_report_carries_the_finding[R12xx]`, each of which carries a verdict-60 or
verdict-61 finding id **in its own parameter**; that is the whole of R835, the count being a
function of what the reviewer wrote. The 19
`test_report_guard_states.py::test_the_guard_survives_the_state[...]`,
`test_R887_the_plant_base_is_the_step_the_GUARD_reads` (*"the harness copies FROM step-0.md,
which does not exist"*, with its `STEP == guard.STEP` assertion PASSING),
`test_report_numbers_are_sourced.py::test_the_report_parsed_into_sections`, and the 12
`test_report_carried.py` singletons about the absent report --
`the_report_names_the_verdict_it_answers`, `carries_a_CI_SECTION`,
`reported_CI_counts_are_not_all_zero`, `the_Carried_table_is_what_the_generator_produces`,
`the_ROUNDS_SECTION...`, `a_carried_row_points_at_a_section_that_discusses_it`,
`a_report_does_not_say_CLOSED`, `there_are_pointers_to_resolve`,
`the_parse_found_something_to_check`, `the_generator_would_catch_a_row_under_the_wrong_number`,
`the_CI_section_is_about_the_REVIEWED_commit`, `the_guard_reads_the_step_being_worked_on` --
are each about the report that answers this verdict and clear when it is written (EG3 state
(2), cleared BY THE ANSWERING REPORT and not by time). **Limb two** -- subject IS the commit
carrying it -- takes the remaining two, as FT1 names them:
`test_the_report_carries_a_WHOLE_SUITE_count` and
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`. **No id fails the predicate, so no red here
is CZ1 (iv)** -- with the single exception R1227 records, whose class changes next revision.
**R835: unchanged, R2 (GE3).** Not re-measured further.

## Tolerances touched

**None, measured twice.** `git diff 3d24e1c..HEAD -- floatfea/tolerances.py` is 0 lines and so
is `git diff 91c2d2e..HEAD -- floatfea/tolerances.py`. No declared counter moves:
`git diff 3d24e1c..HEAD | grep -cE "^[-+].*_COUNTER"` is `0`. **EU1 therefore does not arise**,
and I ran the model at configurations the diff did not choose anyway -- which is where R1225
and R1226 came from. One tolerance-shaped thing is implicated by R1225 and is NOT a tolerance:
`--check`'s comparison is `np.array_equal` with no threshold, by Q8's rule, and nothing in
R1225 asks for one. **If any answer to condition 4 introduces a tolerance on that comparison,
that is a widening and it is refused.**

## Corpus

**No batch, and ES0 is why, not GC3.** An interim check is light by rule: *"No corpus batch,
no closure list."* My own instructions say "add unseen entries at every review"; where the two
differ CLAUDE.md governs and I say so rather than quietly following the looser one.
**What I ran instead is the recorded substitute, and it produced both blocking findings:** a
continuum over the parameter space the new resolver guards (the stable key at the runs tree
with a control, a case-folded value, a set-and-wrong key through collection of two rungs, the
plan marker at 0 and at 3, three revert-red-restore cycles) plus a **regeneration check on a
published deliverable** -- the F6 results report and the npz, which is where R1225 lives.
Nothing in `tests/corpus/` covers worktree-key *provenance* as against resolution;
`stable_key_names_the_runs_tree` and `declared_tag_is_a_literal` are the entries I would write
next round if R1226 is not closed by then.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN** -- which GI6 holds anyway, so this HOLD costs
no schedule. Step 0's remaining work (the FloatSim run, GI3(b)'s wall time, (a) and (d)) is
the right work to continue with. **Conditions 1, 2, 3-as-written, 5, and R1216/R1219/R1220 are
DISCHARGED and are not re-measured.** What remains:

1. **R1225 -- the magnitude, then the decision, then the escalation under FQ3.** (i) the
   per-array magnitude and its ratio to that array's own scale, pasted, with the operating
   point; (ii) **no write run** until the generation environment is recorded in the provenance
   and held at the point of generation, through the existing `floatfea/determinism.py` (FF0,
   next commit); (iii) if it is a last-bits move, the escalation is **FQ3** -- *STOP and
   report, do not re-baseline* -- and **NOT** `R2.md` section 6 item 2, whose premise is
   untested while the pin sits off the artifact's basis. A green pinned re-run does not close
   this; it only changes which sentence is written.
2. **Condition 4 (the staleness red) and condition 6 (R1223) -- UNCHANGED and now subordinate
   to R1225.** Verdict 60's ordering was right and is what saved the npz; what has changed is
   that the second half of it is not available yet. **Do not clear the staleness guard by
   writing a provenance whose npz moved for an unrecorded reason** -- that turns both reds
   green and publishes the move. If answering R1225 means the figures legitimately move, that
   is a golden-file change and it carries a written explanation naming the pin commit
   `09d5bc9`, per CLAUDE.md section Testing.
3. **Condition 7 -- a concluded, GREEN ladder in CI at the follow-on sha.** Rungs 4 and 5 have
   not been measured in CI at any commit of this step.
4. **R1226 -- the stable key refuses a tree that is not `HSP-stable`, or the snapshot declares
   the tree it read.** Both runs pasted, control beside them (EH4), and the dirtiness limb
   answered or declared left with its reason.
5. **R1227 and R1228 in the next commit (FF0, not the ledger), and R1227 covers `:229` as well
   as `:579`.** R1221 is in the same file and belongs in the same commit. **R1229 is a ledger
   row: delete the line.**

**And for the step-0 report itself, so the next revision is a revision and not a round:** its
`Answers:` header names **THIS verdict and this sha** (`9e1092a35eed45ee5351789778a3c50752af1bb1`),
not verdict 60 or 61 -- the newest verdict is the one the guard checks against and the one
thing a machine cannot check. EG3 (ii): paste the report-guard files run AT my verdict commit;
verdict 61 asked for that figure at `b2dc268` and gave 187 to compare against, and at this
commit the wide guards selection is **172 failed, 1057 passed, 1 skipped**, of which
`tests/test_report_carried.py` is 151. Verdict 58's twelve open items and verdict 59's four
report items are due in it.

**Rounds: step 0 has consumed NONE of its three ES0 revisions.** Verdict 59 was the plan lock;
60, 61 and this are interim checks. The next report revision is the first.

**Nothing here is a STOP, and I considered it twice.** Rung 4 is red and one `tests/regression`
test is red, which read like low-rung failures -- but both are provenance and regeneration
comparisons rather than numerical disagreements at a rung, and R1225 establishes that what
moved is the committed golden and not the code: `git diff --stat 3d24e1c..HEAD -- floatfea` is
`hsp_pin.py` alone, 32 lines, and rungs 1, 2 and 3 were SUCCESS in CI at the previous sha over
byte-identical rung code. The locked plan is faithful to GI and needs no reopening; **`R2.md`
section 6 item 2 is the one clause I am ruling must NOT be triggered yet**, which is the
opposite of reopening it. If Xabier's answer under FQ3 is that the npz is re-baselined at the
pin, that is a golden-file change with a written explanation, not a plan change.

**What this commit got right, and it is the larger part.** Five conditions answered in one
commit with no re-measurement asked for. Each repair is held by a test that reddens when the
repair is reverted, and I ran all three cycles myself rather than taking them -- plus a fourth,
R1219's, that the report did not claim. **The commit found and fixed a check of its own that
could not fail, and said so**; that is the most useful sentence in the diff, and the only other
instance in the file is one decorative line. The escalation was withdrawn on a measurement
rather than defended, with its own wrong premise named as BF0's shape applied to an escalation.
And **condition 4 was stopped at the refusal rather than pushed through it** -- the one decision
in this step that could have republished a dozen figures in a file sent to Xabier, taken
correctly, with the bit-identity prediction admitted wrong before anyone asked for it.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 3d24e1c3808cd6be35490eab76b43f5ccf9d175b
**Reviewed commit: `3d24e1c3808cd6be35490eab76b43f5ccf9d175b`.**
Verdict: HOLD
Scope: **ADDENDUM to the interim check above, same reviewer, same branch, same judged
commit, accumulating under DX2.** It exists because **CI's verification ladder concluded
AFTER I ruled** and it found a red I had not measured -- in `tests/regression`, which I
declined to run locally and gave a reason for that THIS REFUTES. Still an ES0 interim check:
it counts against none of step 0's three revisions and closes nothing. One new blocking
finding, one correction to my own Tests line, and two measurements that arrived late.

## Carried

Everything carried in the entry below stands unchanged -- R1206 open and blocking, R1213,
R1214, R1215, R1221, R1222, the ledger, and the rung-4 staleness red under CZ1 (iv).
**R1223 below is a consequence of that staleness red reaching a published deliverable**, so
it is answered by the same follow-on commit and adds no separate work. Nothing is withdrawn.

## Findings

**R1223. (BLOCKS) A PUBLISHED DELIVERABLE no longer regenerates from this tree, and the two
rows that moved are gate STATUSES: the shipped report says `G4.1 force ... pass` where this
tree produces `FAIL`.**

```
claim  CI's ladder is a pass, or its red is the staleness guard I already ruled
cmd    gh api .../actions/runs/44118920983/jobs  (after the run CONCLUDED, 16:25Z)
out    the verification ladder: CONCLUDED FAILURE
       ladder 1 success, ladder 2 success, ladder 3 success,
       ladder 6 -- it stays fixed  FAILURE,  ladder 4 SKIPPED, ladder 5 SKIPPED
cmd    gh run view --job <the ladder job> --log-failed
out    run_rung: FAIL -- tests/regression is red.
       run_rung: 477 collected, 1 failed, 0 errored, 0 skipped
       run_rung:   failure  tests.regression.test_f6_deliverable_agrees_with_itself::
                            test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree
cmd    the same test, my own run, in my own worktree at the judged sha
out    1 failed in 56.14s -- "the committed deliverable is not what this tree regenerates:
       4 line(s) differ, shipped has 470 lines against 470.
         line 154: shipped `| G4.1 force | ... | F4_G41_DYNAMIC_FORCE | pass |`
                   vs fresh `| ... | F4_G41_DYNAMIC_FORCE | FAIL |`
         line 155: shipped `| G4.1 moment | ... | pass |` vs fresh `| ... | FAIL |`
         line 165: shipped `  G4.1 force       116 passed`
                   vs fresh `  G4.1 force       1 failed, 115 passed`"
cell   ONE VARIABLE -- the same test at `91c2d2e`'s code, in the worktree at `8d40843`
       (which adds only verdict 59's file to that tree)
out    1 passed in 74.74s
rule   tests/regression/test_f6_deliverable_agrees_with_itself.py:317; EZ0 -- a published
       deliverable is anything under `results/` or `scripts/measure/` that produces one
judge  **THIS COMMIT CAUSED IT.** Green at 91c2d2e, red at 3d24e1c, code the only variable.
       It is downstream of the rung-4 staleness guard -- the G4.1 gate's 116 cases include
       it, so `116 passed` became `1 failed, 115 passed` and the generator wrote `FAIL` --
       but it is a STRICTLY LARGER claim than the staleness red, and FS1's predicate does
       not reach it: it names no finding and no site of verdict 59, and its subject is a
       shipped deliverable rather than the commit carrying it. CZ1 (iv).
```

**The silently wrong result, in the form FR1 asks for:** the shipped F6 results report --
a file sent to Xabier -- states that gates `G4.1 force` and `G4.1 moment` **pass**, with
`116 passed` beside them, while the tree at this commit regenerates the same report with
`FAIL` and `1 failed, 115 passed`. A reader of the deliverable is told a dynamic-equilibrium
gate holds; the tree says it does not. That is FR1's first head verbatim -- a wrong value in
a published deliverable -- and it is invisible to `pytest tests/unit`, to the four root
guards, to `ruff`, `black` and `mypy`, and to the selection either of us ran before CI.

**And the correction, which is mine (R1224, DOES NOT BLOCK -- a reasoning error of my own,
recorded so the next round does not inherit it).** My Tests line argued that rungs 1, 2, 5,
6 and `tests/regression` could not be reached, because `git diff --stat ... -- floatfea` is
`hsp_pin.py` alone and only two test files import it. **The argument is refuted by the
measurement:** `tests/regression` reaches the changed lines INDIRECTLY, through a gated run
of the G4.1 gate inside the deliverable generator. An import census over `tests/` cannot see
a test that shells out to a generator that runs another gate. **FV1's own clause said so and
I read past it:** *"any regression test that reads a deliverable the diff regenerates"* runs
locally. This diff regenerates one. Convert arguments into measurements -- the measurement
was 56 seconds and I reasoned instead.

## Tolerances touched

**None.** Unchanged from the entry below and re-checked against this red: the four differing
lines are STATUS and COUNT cells, not thresholds -- `2.5e-12` / `F4_G41_DYNAMIC_FORCE` and
`0.0002` / `F4_G41_DYNAMIC_MOMENT` are byte-identical on both sides of the comparison, so no
tolerance moved and none is implicated. EU1 still does not arise.

## Next step opens when

The five conditions below stand, with one addition and one sharpening.

6. **R1223 -- the deliverable regenerates.** It should fall out of condition 4 (the
   provenance refresh) with no separate work, and the check is one command:
   `pytest -q tests/regression/test_f6_deliverable_agrees_with_itself.py` green at the
   follow-on commit, pasted. **If it does NOT go green once the provenance is refreshed,
   stop and say so** -- that would mean the G4.1 gate's `116 passed` is not restored by the
   refresh, which is a different and larger finding than anything in this file.
   **Do not regenerate the deliverable to match a red gate.** Re-running
   `scripts/measure/f6_results_report.py` now would write `FAIL` into the shipped report and
   turn this test green while publishing a failing gate; that is the golden-file error
   CLAUDE.md names, one artifact over.
7. **Condition 4 is sharpened: the follow-on commit's own CI run must be GREEN on the
   LADDER, not only on lint** (CZ1 (iii), (iv)). Rungs 4 and 5 were SKIPPED behind this red,
   so **nothing at this commit has measured rung 4 or rung 5 in CI at all** -- including the
   staleness guard's companions and the whole of rung 5. That is the hiding CZ1 (iii) exists
   for, and it is why a concluded, green ladder at the follow-on sha is the condition rather
   than a local run.

**Two measurements that arrived after I ruled, recorded here so the next revision does not
have to take them.** CI at the judged commit is now fully concluded: `lint, unit and guards`
FAILURE (the 108, as traced), `the verification ladder` FAILURE at `ladder 6` with rungs 4
and 5 skipped, both determinism jobs skipped by their own condition -- so **CA2 is reached
on both jobs**, and rungs 1, 2 and 3 are measured SUCCESS in CI at this sha, which is the
half of my STOP paragraph that survives. And EG3 (ii), measured at MY verdict commit
`b2dc268` on the two report-guard files: **187 failed, 120 passed, 1 skipped in 111.90s**,
up from the 107 those two files carried at `3d24e1c` -- because
`test_every_named_site_is_touched_or_declared` is parametrised over the newest verdict's
sites and this verdict names many more. That is R835 in one line, not re-measured further
(GE3). Paste that count in the next revision; the number to compare against is 187.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 3d24e1c3808cd6be35490eab76b43f5ccf9d175b
**Reviewed commit: `3d24e1c3808cd6be35490eab76b43f5ccf9d175b`.**
Verdict: HOLD
Scope: **ES0 INTERIM CHECK on the OPEN step** -- no new report revision exists
(`git ls-files docs/reports/R2` is empty; `docs/reports/R2/step-0.md` is untracked), so this
**counts against none of step 0's three revisions** and closes nothing, and `--closes` is
correctly absent (FK1). Light scope per ES0: the suite, CI at the commit, and a CZ0 (a)-(d)
scan of the diff. **Ruled under FR1 with EZ0**, and each blocking finding names the silently
wrong result it produces. **GE3: `R835: unchanged, R2`. Not re-measured.**
**EU1 DOES NOT ARISE, MEASURED RATHER THAN TAKEN:** `git diff adc6c3c..3d24e1c --
floatfea/tolerances.py` is empty, so is `git diff 91c2d2e..3d24e1c -- floatfea/tolerances.py`,
and no declared counter moves anywhere in the diff. **I took the diff from `91c2d2e`, the last
JUDGED commit, not from `adc6c3c`**, so `8c0edce` is inside it and is judged below.
**GA3's length target is OVERRUN and I say so rather than trimming the evidence**: the
overrun is the per-id trace of 108 reds with its one-variable control (EG3 (i) forbids ruling
a cascade by family), two blocking findings with their cells, and the four rulings you asked
for by name.
Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`, and the first
reproduces your figure exactly rather than taking it.**
* your stated selection -- `tests/unit` + the four root guards +
  `rung3/test_platform_deck_export.py` + `rung4/test_f4_g41_dynamic.py`:
  **1 failed, 828 passed in 365.65s**, and the one failure is the staleness guard.
* the six report-guard files: **108 failed, 557 passed, 1 skipped in 442.68s**, traced per
  id below. Your selection excludes all six, so your report's "1 failed" is true of what it
  ran and silent about the file where the marker decision lands.
* CI's own guards selection, `pytest tests --ignore=tests/unit --ignore=tests/verification
  --ignore=tests/regression`, in a second worktree: **108 failed, 1047 passed, 1 skipped in
  903.77s -- THE SAME 108, id for id.** `comm -23` and `comm -13` over the two sorted FAILED
  lists are BOTH EMPTY, so **no root test outside the six report-guard files is red at this
  commit** and nothing is hiding inside CI's aggregate.
* the one-variable control (marker back on R1 step 4, this commit's code unchanged):
  **8 failed, 849 passed in 607.41s** -- see the trace.
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`,
  `mypy floatfea`: **all clean, my own runs.**
* **NOT RUN LOCALLY and I say which rather than implying coverage**: rungs 1, 2, 5, 6 and
  `tests/regression`. The reason is measured, not assumed:
  `git diff --stat 91c2d2e..HEAD -- floatfea` is `hsp_pin.py` alone, and
  `git grep -ln hsp_pin -- tests` outside the corpus returns only
  `rung3/test_platform_deck_export.py` and `rung4/test_f4_g41_dynamic.py`, so no test in
  those rungs reaches a changed line. FV1 puts the whole of `tests/regression` on CI.
CI: **run `44118920983` at the FULL sha `3d24e1c3808cd6be35490eab76b43f5ccf9d175b` EXISTS
and `lint, unit and guards` CONCLUDED FAILURE**, at step 10 `guards and meta-tests`, with
`actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all **success** before it --
so the guards step is seen to have RUN rather than been skipped behind an earlier red
(CZ1 iii). **`the verification ladder` had NOT finished when I ruled** (`in_progress`, both
runners assigned, started 15:50:31Z); a run that has not finished is not a pass. Expect it
to redden at `ladder 4` on the same staleness guard -- and note CI orders `ladder 6 --
tests/regression` BEFORE `ladder 4`, so that rung is not hidden behind it. Both determinism
jobs `skipped` by their own `workflow_dispatch` condition. **This is NOT CK2**: runners
`GitHub Actions 1000001916` and `1000001917` were assigned and the jobs executed for
minutes. **CA2 IS REACHED -- CI is red at the judged commit** -- and the per-id list is
**unavailable, not skipped over**: `gh run view --log` refuses while any job is in progress
(*"logs will be available when it is complete"*), so the id-for-id agreement between my 108
and CI's list is deferred to the next revision. FP1 held: the commit was pushed before I was
invoked. GC2 does not arise -- `git diff --name-only 91c2d2e..HEAD` touches `floatfea/` and
`scripts/`, so the push triggered a run of its own. **One throughput observation, not a
finding:** the runs at `91c2d2e` and `8c0edce` are STILL `in_progress` after 1h18 and 1h00,
their ladders unfinished, because GG3's per-commit group no longer cancels them -- three
ladders now run in parallel and CI's answer arrives long after the commit.
Door (FV2 / GG2): `git worktree add -b review/3d24e1c3808c <a path outside the repository>
3d24e1c3808cd6be35490eab76b43f5ccf9d175b` **succeeded on the first try, so no review of this
commit existed**; `git push origin review/3d24e1c3808c` likewise. Every measurement above was
taken in that worktree, and this verdict is written there through `scripts/write_verdict.py`,
committed on that branch and pushed -- merge it with `git merge --ff-only
origin/review/3d24e1c3808c`. **Three writes of my own, all in my own worktree and all
reverted before committing** -- the marker-1 cell, the marker control, and a second DETACHED
worktree for CI's wide selection, which I removed with `rm -rf` followed by `git worktree
prune` -- the one `.git`-metadata write I made in `C:\dev\floatfea`, which touches no file
in the working tree and which I disclose rather than leave for you to find. `git status --porcelain` there is empty
and both marker lines read as committed. In `C:\dev\floatfea` I ran only read-only `git` and
`gh`, and the one write-shaped thing I did touch -- `preflight()` against the real
`HSP-stable` -- reads only (`git describe`, `git hash-object` without `-w`) and wrote nothing.

## Carried

Verdict 59's four blocking findings, its four closing conditions, and verdict 58's items
routed to R2's first report. **Three of four answered; two halves open.**

* **R1205 (two live markers; the `Carried` gate reporting on F2 step 4) -- ANSWERED, and I
  re-ran both checks the condition asked for rather than reading them.**
  `docs/milestones/R1.md:3` now reads `<!-- step-under-execution: moved to R2 at step 0
  (GI) -->`, the `F2.md:10` form.
  ```
  cmd  grep -rnE "<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->" docs/milestones/
  out  docs/milestones/R2.md:3   (one plan, not two)
  cmd  python -c "import sys; sys.path.insert(0,'scripts'); import check_carried as cc; print(cc._active_step())"
  out  ('R2', 0)
  cmd  python scripts/check_carried.py ; echo exit=$?
  out  check_carried: .../docs/reviews/R2/step-0.md or .../docs/reports/R2/step-0.md missing
       exit=1
  cmd  python -c "import sys; sys.path.insert(0,'.'); import scripts.ci_section as c; print(c.MILESTONE, c.STEP)"
  out  R2 0
  ```
  The gate that was green about the wrong milestone is now red about the right one, naming
  the file the next revision adds. That is the repair.

* **R1206 (`0` is both a legal step number and the resolvers' sentinel) -- STILL OPEN,
  still blocking, and it carries by name into step 0's list.** You do not claim it
  answered; what shipped is verdict 59's **cell 2**, not exit (ii) -- see R1215 and
  ruling (1), where I withdraw the escalation by measurement.

* **R1207 (step 2's gates (ii) and (iii) both passable by a no-op) -- ANSWERED in the
  plan, at `docs/milestones/R2.md:317-332`.** (ii) is now a pair with the inverted half
  stated as the gate ("a run at a PERTURBED mass does *not* [reproduce], differing in
  `case<i>/body_mass`, `m_xddot` and `accel`"), and (iii) closes against
  `case<i>/body_mass` read back from the npz. Both citations resolve in substance; one
  line number is off by three (R1217).

* **R1208 (one key is silent in one direction) -- HALF ANSWERED. The two keys are
  written and routed correctly; the half that says "the three DS0 refusals shown firing
  after the change" FAILS BY MEASUREMENT.** The routing I checked site by site, as you
  asked:
  ```
  cmd  git grep -n "hsp_pin.worktree(" -- scripts
  out  export_buoy_centers_ref.py:42   "stable"     <- correct, the no-refusal site
       export_platform_deck.py:45      "runs"
       measure_platform_joints.py:52   "runs"
       report_joint_reactions.py:96    "runs"
       run_floatsim_design_waves.py:55 "runs"   :56 "stable"   <- both, correct
  cmd  for each touched script: import it with NO worktree present and NO env var set
  out  OK export_buoy_centers_ref / export_platform_deck / measure_platform_joints /
       report_joint_reactions / run_floatsim_design_waves / f4_dynamic_residual /
       export_f4_dynamic_inputs      (7 of 7 -- `require=False` does what its docstring
       claims and R670's import-time ImportError is avoided, measured not argued)
  ```
  The refusals are **R1213**: two of the three fire on the adversarial input, one does not.

* **Verdict 59's ledger -- R1209, R1210, R1211, the Â§4 row-1 form, the CP3 header, the
  triple grammar, and Â§5's DO-NOT-HAND-EDIT line: all SIX addressed in the plan diff.**
  I read each against its site. R1209's census is rewritten with a needle that finds all
  seven (`git grep -nE '(ROOT|parents?\[[0-9]\])...'`) and now splits runs from stable;
  R1210's false `out` line is replaced by what the command returns, with the consequence
  for D4 stated; R1211 gains the one-body/three-component limit and the GI1 declared-file
  distinction; Â§5 gains the deck bullet; the CP3 header names its two carried figures; the
  triple-grammar paragraph is accurate -- `grep -c "^cmd:" docs/milestones/R2.md` is `0`
  and the file says so rather than pretending otherwise. **The Â§4 row-1 form is half
  right and I re-open that half as a ledger item (R1218).**

* **R1212 -- unchanged, mine, Xabier's.** The verdict is at `step-0.md` and not `plan.md`
  for the reason recorded there; this entry accumulates into the same file under DX2.

* **Verdict 58's items -- R1196 to R1201, R1186, R1188, R1189 (c), R1190, R1191, R1193 --
  STILL OPEN, due in R2's first report**, which is in flight. None is answerable by this
  commit and none is a plan matter. **R1193 stays discharged from my side** (I am
  operating under the post-`2e08766` text). **R1203, R1204 -- reviewer-side or Xabier's.**

* **Verdict 59's four "things for step 0's report" -- not yet due**, and three of the four
  are the report that is in flight. The `--check` determinism run is ruling (4) below,
  where I correct what it can and cannot clear.

## The 108, per id, at this commit -- traced from each id's own message (EG3 (i))

```
cmd    python -m pytest -q -p no:randomly <the six report-guard files>, my own run in my
       own worktree at the judged sha
out    108 failed, 557 passed, 1 skipped in 442.68s
cmd    grep "^FAILED" | strip the parameter | sort | uniq -c
out    50  test_every_named_site_is_touched_or_declared[...]
       21  test_the_report_carries_the_finding[...]
       19  test_the_guard_survives_the_state[...]
       18  singletons in test_report_carried / test_report_guard_states /
             test_report_numbers_are_sourced
rule   FS1 with FT1, per id. Limb one: names a finding or a site of the NEWEST verdict
       (verdict 59, `adc6c3c`, whose entry is in this same file). Limb two: its SUBJECT is
       the commit carrying it.
```

**The 50 and the 21 are parametrised over verdict 59's OWN findings and sites**, so limb one
holds by construction, and their messages say what clears them: *"...the step's diff does not
touch it, and the newest report revision does not say..."* and *"the report does not carry
..."*. EG3 state (2), cleared by the answering report. **Three of the 50 are worth naming
rather than waiving silently, because their content IS R1213:**
`[R1208-run_floatsim_design_waves.py:98]`, `[R1208-report_joint_reactions.py:106]` and
`[R1208-export_platform_deck.py:75]` -- the three DS0 refusals -- are red because *the diff
does not touch them*. The guard is enforcing CLAUDE.md's *a closing condition that names
sites is closed site by site*, mechanically, and it is right: two of the three needed no
change and one did.

**The 19 share ONE cause with the singleton `test_R887_...`, and the harness names it
itself** rather than being ruled by class: R887 reports *"the harness copies FROM step-0.md,
which does not exist. Every state built by a `copy2` dies in `_build` before planting
anything."* State (2). Two of the 19 additionally report `<state>: expected a clean run`,
which is the same absence seen from inside the inner run.

**The 18 singletons, each read individually. SIXTEEN are state (2) in their own words** --
*"the newest report revision has no `Answers:` header"*, *"...no Carried section"*, *"...no
`## ... CI ...` section"*, *"the CI section names no commit"*, *"no step report found
under docs/reports/R2"*, *"step-0-answers.json is not committed ... That is EG3 state (2)"*.
That sixteen includes the two names FC1 put under limb two,
`test_the_report_carries_a_WHOLE_SUITE_count` and
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` -- **and limb two is not needed for either
here**, because at this commit they fail on report absence like the rest (*"the newest
revision carries no whole-suite line"*, *"the 0a table has neither a run row nor the
generator's zero-run row"*). Measured, not assumed from the name. **And two are neither,
and they are the two that matter:**

* **`test_the_plan_names_the_step_under_execution` is R1206 ITSELF.** The marker count is
  now 1, so the first assertion passes; it dies at `assert _plan_step() > 0`. It is not a
  boundary red and it needs no waiver -- it is the true, loud symptom of an open blocking
  finding carried from verdict 59, and it clears when exit (iii) is taken and not when a
  report is written.

* **`test_a_blocking_item_is_not_routed_to_4a` IS MINE, AND NO REPORT CAN CLEAR IT --
  R1222 under Findings.** It is red on verdict 59's heading FORMAT, not on anything the
  implementer did or can do.

**So: of 108, ONE HUNDRED AND SIX are EG3 state (2) and the waiver covers them --
50 + 21 + 19 + 16, which sums exactly; ONE is R1206, already blocking and already carried;
ONE is mine (R1222). The 109th red, `test_the_npz_is_NOT_STALE...` in the separate rung-4
run, fails the predicate and is CZ1 (iv) unchanged.**

**THE CONTROL, ONE VARIABLE, AND IT IS THE MEASUREMENT THAT SETTLES OWNERSHIP OF ALL 108.**
A list of names cannot be checked against a failure message and a family cannot be ruled as a
cascade (EG3 (i)), so I moved the marker back to `8c0edce`'s state **with this commit's CODE
DIFF LEFT IN PLACE** -- R1 at step 4, R2's retired -- and re-ran the identical selection in my
own worktree, then reverted (`git status --porcelain` empty, both marker lines back):

```
cmd    the judged tree (R1 retired, R2 at step 0), six report-guard files
out    108 failed, 557 passed, 1 skipped in 442.68s
cmd    ONE VARIABLE MOVED -- the marker back on R1 step 4, R2's retired, same code
out      8 failed, 849 passed in 607.41s
cmd    the eight, by name
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
       test_the_guard_survives_the_state[baseline, non_numeric_step_suffix,
         superscript_digit_step_number, draft_suffix_beside_a_step_report,
         step_number_is_the_empty_string,
         verdict_amended_after_the_commit_the_report_answers, zero_padded_step_number]
rule   FS1/FT1 per id, and `8c0edce`'s own trace of the same eight
judge  **THE EIGHT ARE EXACTLY THE SET `8c0edce` TRACED BY NAME, id for id**, including the
       one it showed red at `251af69` before this turn began. So **not one of the 108 is
       caused by the code in this commit** -- the hundred extra are a function of the
       marker/no-report state alone, and the collection total moves with it (666 vs 857)
       because both guards are parametrised over the active report's verdict (R861).
```

That is the control R1 step 1's report got wrong by comparing two instances of the SAME state:
here the two cells differ in one variable and the code is held fixed, so it separates "red
because no report exists" from "red because of this diff". The answer is all of the first.

## Findings

**R1213. (BLOCKS) The DS0 refusal in `run_floatsim_design_waves.py` DOES NOT FIRE on the
input this diff newly admits, and I ran it against the real production worktree rather than
reasoning about it.**

```
claim  verdict 59's condition 4 -- "the three DS0 refusals shown still firing" -- holds
       after the change
cmd    FLOATFEA_HSP_RUNS=C:/Users/xlama/OneDrive/Documents/buoy/HSP-stable, the stable key
       UNSET and its legacy sibling absent (the state measured at C:\dev\floatfea);
       import scripts/run_floatsim_design_waves and call preflight() -- preflight only,
       nothing written
out    RUNS   = C:\Users\xlama\OneDrive\Documents\buoy\HSP-stable
       STABLE = ...\scratchpad\HSP-stable            (the legacy candidate, absent)
       worktree  HSP-stable at floatfea-ref-1
       database  blob f26501001916, sha256 3dca8b131b4a028b -- matches the commit
       output    ...\HSP-stable\studies\platform-12buoy\floatfea_design_waves
       >>> preflight() RETURNED. DS0 did not fire.
cmd    the same input, through the OTHER two refusals' predicate
out    "HSP-stable" in RUNS.resolve().parts  ->  True     (they DO fire)
       RUNS.resolve() == STABLE.resolve()    ->  False    (this one does not)
rule   scripts/run_floatsim_design_waves.py:102 -- the refusal is an IDENTITY test against
       the other key, not a NAME test. report_joint_reactions.py:109 and
       export_platform_deck.py:77 test the name and are unaffected.
cell   one variable: at `91c2d2e`, `RUNS = Path(__file__).resolve().parents[2] /
       "HSP-runs"` reads no config and no environment, so no input could reach this state.
       The diff is what makes it reachable; the refusal is what was supposed to hold it.
```

**The silently wrong result.** `main()` calls `preflight()` and then, at
`run_floatsim_design_waves.py:138`, `OUT.mkdir(parents=True, exist_ok=True)` and writes six
`case_*.csv` solve-state windows **inside the tree `RUNS` names** -- so six FloatSim
design-wave solves run and write into `HSP-stable`, the read-only production worktree GI1,
`R2.md:366` and `docs/hsp-coupling.md:121` (*"`HSP-stable` is read-only from FloatFEA
(DS0)"*) forbid writing to, with the one refusal that exists to prevent exactly that
printing nothing. The module's own docstring records the precedent: *"this repository wrote
into it once: a `platform_bem.py` run regenerated `platform12_bem.nc` and overwrote the
version commit `e1010fe` had corrected, after which FloatSim's own restoring-PSD gate
refused the database."* And the export is read back by `report_joint_reactions.py:121`
(`EXPORT.glob("case_*.csv")`) through **its own** runs key, so a case set written into one
tree is described from the other -- the September case set is still sitting in `HSP-runs`.
That is FR1's second head: an input accepted and used other than as declared, with DS0's
declaration silent.

*Closed when* `preflight()` refuses on the measured input -- the one-line name test the
other two sites already carry, kept **beside** the identity test rather than replacing it
(EK2: repair, not a new mechanism) -- and the run above is pasted showing the refusal, which
is also what `R2.md:253` and `:291` promise and what verdict 59's condition 4 asked for.

**R1214. (BLOCKS) A key that is SET BUT WRONG is silently discarded and a different
worktree is used.**

```
claim  what happens to a declared value that is not a directory
cmd    FLOATFEA_HSP_STABLE=C:/typo/HSP-stable-oops (set, not a directory), with a legacy
       sibling of the repo root that EXISTS; then hsp_pin.worktree("stable")
out    legacy sibling exists?  True
       worktree('stable') -> ...\scratchpad\HSP-stable
       the declared value was DISCARDED with no message and no refusal
cmd    the same shape through `declared`, which is the config half GI3(e) asks for
out    declared=<nonexistent>, env set to another existing tree -> the ENV tree is
       returned; the declared value is discarded silently
rule   floatfea/hsp_pin.py:90-101 -- the loop appends `f"{source}: {path} is not a
       directory"` to `tried` and then CONTINUES. `tried` is read only under
       `require=True`, which NO caller passes (`git grep -n "require=" -- scripts` is
       empty), so the distinction between NOT SET and SET-AND-WRONG is computed and
       thrown away.
```

**The silently wrong result.** `data/platform/buoy_centers_ref.json` -- a committed data
file and the input to EB6's label-provenance gate -- regenerated from a worktree nobody
declared, with its `"source"` field naming `HSP-stable/...` and `_blob_sha` recording that
other tree's sha, so both sides move together and `--check` stays green. That is C155's
shape and it is the **same defect R1208 was**, surviving one level up inside the resolver
written to fix it: `export_buoy_centers_ref.py` is the one site with no tag, name, commit or
dirtiness refusal -- I checked, its only `SystemExit` on the tree is "the source file is not
a file" (`:74-76`) -- which is precisely why you gave it the stable key. A typo'd or stale
`FLOATFEA_HSP_STABLE` on a checkout that satisfies the legacy convention reaches it today,
and that convention is the DOCUMENTED one: `docs/hsp-coupling.md:45` and `:141-142`
prescribe `git worktree add ../HSP-stable` and `../HSP-runs` as the scheme, so a conforming
checkout HAS the sibling this falls through to.

*Closed when* a source that is **set and not a directory** is a refusal and only an **unset**
source falls through -- the information is already in `tried`, so this is a two-line change
in `hsp_pin.worktree` and no new apparatus. CLAUDE.md's own line is the rule here: *never
let a validation failure degrade to a warning*; this one degrades to silence. FZ rule 2 says
refuse rather than silently adjust.

**R1215. (DOES NOT BLOCK -- FF0, next commit, not the ledger) `docs/milestones/R2.md:5`
says the marker reads `1` while `:3` reads `0`, and calls the shipped state "exit (ii)",
which it is not.** No wrong number follows, so FR1 does not block it; FF0 keeps it out of
the ledger because it is the gating apparatus's own record.

```
cmd    sed -n '3p;5p' docs/milestones/R2.md
out    3: <!-- step-under-execution: 0 -->
       5: <!-- IT READS 1 WHILE STEP 0 IS BEING WORKED, AND THAT IS R1206'S EXIT (ii)
          CHOSEN DELIBERATELY ...
cmd    the same comment, 29 lines down
out    "SO THE MARKER READS 0 AND NOT 1"
rule   verdict 59's exit (ii) is "keep the marker at the NEXT step and record step 0
       another way". The marker is at the CURRENT step, so what shipped is the judged
       tree's cell 2 -- no exit taken. You say R1206 is open, which is right; the plan
       file says the opposite twice.
```

This is BP0 on the smallest possible scale: the first sentence was written for the marker-1
attempt and the decision moved underneath it. It is in the file four resolvers read, beside
the value they read, and it says the opposite of the value. One paragraph, next commit.

**THE RED. I REACH YOUR CONCLUSION AND NOT YOUR REASONING, AND THE REASONING MATTERS
BECAUSE IT IS FS1's FIRST LIVE FAILURE IN THE OTHER DIRECTION.**

`tests/verification/rung4/test_f4_g41_dynamic.py::test_the_npz_is_NOT_STALE_against_the_code_that_generated_it`
is **CZ1 (iv), unwaived**. You wrote that it "names no finding or site of verdict 59". It
names three:

```
cmd    the assertion message, from my own run
out    floatfea/hsp_pin.py: tree 1d18d35e24c7 vs provenance d2e055b9fdc0;
       scripts/export_f4_dynamic_inputs.py: tree e5b4b012a56a vs provenance 3127f6ffe524;
       scripts/report_joint_reactions.py: tree 7166c5ef0a5f vs provenance 006af3e1d622
rule   FS1 limb one -- "names a finding or a site of the newest verdict". All three files
       are sites of verdict 59 (R1208 names `hsp_pin.py:20` and
       `report_joint_reactions.py:96`; R1207 names `export_f4_dynamic_inputs.py:467-479`
       and `:390`), and `test_every_named_site_is_touched_or_declared` is parametrised
       over two of them BY NAME in this very run.
judge  **LIMB ONE IS SATISFIED IN LETTER AND FAILS IN SUBSTANCE, so the red blocks.**
       Both limbs are REASONS, not names (FS1), and the reason behind limb one is EG3's
       two states -- *designed, and SELF-CLEARING*. This red does not clear when the
       answering report is written, and it did not exist because a verdict exists: it
       exists because committed data went stale against committed code. Limb two is not
       reached either -- its subject is the npz, not this commit. CZ1 (iv) stands.
```

That is worth one sentence of record and no more (GE3: `R835: unchanged, R2`): the predicate
has now been short in **both** directions in one tree -- too narrow for the no-report reds
below, too wide for this one -- and in both cases what settled it was the failure message,
not the name.

**And your stated answer does not clear it, which is the part that would have cost a
commit.** `--check` measures the right thing and cannot discharge the guard:

```
claim  `scripts/export_f4_dynamic_inputs.py --check` clears the staleness red
cmd    read the --check path: scripts/export_f4_dynamic_inputs.py:435, :444-:504
out    `--check` writes `dynamic_inputs.check.npz`, compares arrays with
       `np.array_equal`, unlinks, and `return`s -- it never reaches
       `PROVENANCE.write_text` at :540. The guard compares the provenance's
       `import_closure` blob shas against the tree's, so only a provenance REWRITE
       clears it.
cmd    whether a full regeneration churns the 12 MiB npz as well -- measured, because I
       assumed it would and I was wrong
out    np.savez_compressed of identical arrays, twice, two seconds apart:
       file bytes identical? True   (arrays equal? True)
rule   the guard at tests/verification/rung4/test_f4_g41_dynamic.py:321
judge  so the sequence that clears it is `--check` FIRST (your determinism and GI3(b)
       wall-time measurement, and if it differs, that is R2.md Â§6 item 2's escalation and
       the provenance must NOT be refreshed), then a full WRITE run, whose git diff should
       be the provenance json alone. If `dynamic_inputs.npz` moves in that diff, the
       arrays moved and Â§6 item 2 is live.
```

**R1221. (DOES NOT BLOCK -- FF0, next commit) The `Carried` gate is parametrised over
PHANTOM finding ids -- `R2`, and `R1` too -- and no wording on my side can avoid them.**
FR1 does not block it; FF0 keeps it out of the ledger, because this is the gate R1205
exists to protect.
```
claim  the ids `test_the_report_carries_the_finding` demands of the step-0 report are
       findings
cmd    tests/test_report_carried.py:387-390 -- EXPECTED = _FINDING.findall(VERDICT_TEXT)
       | _MENTION.findall(_section(VERDICT_TEXT, "Carried")); _MENTION is
       re.compile(r"\bR\d+\b") at :238
out    the parametrised ids at this commit include [R2] and [R835] beside [R1205..R1208]
       and verdict 58's R1186..R1204
cmd    where `R2` comes from -- the Carried section of verdict 59, six times
out    "routed to **R2's first report**", "due in R2's first report", "routed to R2",
       "R835 is R2's under GE3", "It asks R2's first report", "docs/milestones/R2.md:12"
cmd    whether a reviewer can write a Carried section without it
out    grep -o "\bR2\b" <this verdict's Carried section> | wc -l  ->  10, and
       grep -o "\bR1\b" -> 1, so THIS entry injects TWO phantoms. All eleven are either
       the milestone label or a path -- `docs/milestones/R2.md`, `('R2', 0)` and
       `docs/milestones/R1.md:3`, which is R1205's OWN site and therefore mandatory in a
       Carried section that answers it.
rule   `\bR\d+\b` cannot distinguish a finding id from a milestone label in a repository
       whose milestones are `R1` and `R2`. In the F-era it could not fire -- `F6` is not
       `R\d+` -- so this is FF0's `F*.md` glob defect one needle over.
judge  the guard then requires the report to "carry R2" as a Carried row, which it will
       satisfy BY ACCIDENT, since every report mentions its own milestone. A gate that
       goes green for the wrong reason on the one gate CLAUDE.md says the whole
       arrangement exists for. EK2: fixed, not extended -- the `_MENTION` needle needs to
       exclude the active milestone's own label, or `EXPECTED` needs to take ids only
       from `_FINDING`-shaped lines.
```

**R1222. (DOES NOT BLOCK -- MINE, and no report can clear it)
`test_a_blocking_item_is_not_routed_to_4a` is red because verdict 59 wrote its dispositions
as PROSE and the gate parses them from PARENTHESES.**

```
cmd    the id's own message, from my run
out    "no `**R<n>. (<disposition>)` heading parsed from step-0.md at all. The heading
        format changed and this check passes on anything."
rule   tests/test_report_carried.py:423-428 -- `_findings()` matches
       r"^(?:\*\*|#{2,4}\s+)(R\d+)\.?\s*\(([^)]*)\)", so the disposition must sit in
       parentheses immediately after the id. Verdict 59 wrote `**R1205. TWO plans carry a
       live ... BLOCKS.**` -- the disposition is in the prose -- so `_findings()` is EMPTY
       and the guard's own non-vacuity check fires.
judge  **the answering report cannot fix a verdict's heading format**, so this red is
       neither state (2) nor limb two; it is the R861 shape, a guard parametrised over what
       the reviewer itself wrote. Every finding in THIS entry uses the parenthesised form.
       **Prediction, recorded before the measurement (EG3 (ii) measures state (1) at the
       verdict commit): this id is GREEN at my verdict commit.** Paste that run in the next
       revision; if it is still red, the parser wants something else and that is a finding
       against the guard, not against the verdict.
```

## The four rulings you asked for

**(1) THE ESCALATION IS WITHDRAWN -- NOT BECAUSE EK2 AND FF0 AUTHORISE A HOOK CHANGE, BUT
BECAUSE NO HOOK CHANGE IS NEEDED. R1206's exit (iii) is three lines in `tests/`.** You
asked me to rule on whether EK2 plus FF0 authorise the `.claude/hooks/` edit without a
directive. They do not, and CLAUDE.md is unambiguous: `.claude/hooks/` changes only in a
standalone `process:` commit citing the directive asking for it, and mixed into a commit
touching `floatfea/` or `tests/` it is a **STOP-class finding**. You were right to refuse
that door. **But the premise -- "one of its six sites is
`.claude/hooks/require-verdict.sh:81,110`" -- is wrong, and I measured it rather than
reading the two line numbers you named:**

```
claim  the hook needs the sentinel separated from the value
cmd    sed -n '81p;110p;134p' .claude/hooks/require-verdict.sh
out    81   marker_re='<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->'
       110  step=$(grep -oE "$marker_re" "$plans" | head -1 | grep -oE '[0-9]+')
       134  if [ -z "$step" ]; then        <- THE HOOK'S SENTINEL IS THE EMPTY STRING
cmd    grep -n '"0"\|-eq 0\|step -gt\|step == 0' .claude/hooks/require-verdict.sh
out    (no match)
cmd    where the collision actually is
out    tests/test_report_carried.py:100   return None, 0
       tests/test_report_carried.py:111   return None, 0
       tests/test_report_carried.py:617   assert _plan_step() > 0
rule   `0` is READABLE at :110 and distinct from unreadable at :134, so the hook resolves
       `report=docs/reports/R2/step-0.md` correctly at marker 0. `check_carried` falls back
       to `("F2", 4)` and `ci_section` to `F2.md` -- neither uses `0` as a sentinel, and I
       ran both at marker 0 above: `('R2', 0)` and `R2 0`.
judge  **exit (iii) is: give `_active_plan` a sentinel that is not `0` (`-1` or `None`), and
       make :617 assert on THAT rather than on `> 0`.** One file, in `tests/`, where EK2's
       "a guard that fails false is fixed, not extended" applies directly and no directive
       is required. Take it; it is cheaper than the state you shipped and it ends the red.
```

**And one correction to the discriminator you chose it on.** Your third measurement --
"at marker 1, `ci_section.py` raises `FileNotFoundError` on `docs/reports/R2/step-1.md`" --
is true, and it is **not a discriminator at this commit**, because marker 0 raises the same
error one filename over:

```
cmd    marker 0, as judged, in a worktree at the commit:  python scripts/ci_section.py
out    FileNotFoundError: ...\docs\reports\R2\step-0.md
cmd    marker 1 (one variable moved, reverted after):     python scripts/ci_section.py
out    FileNotFoundError: ...\docs\reports\R2\step-1.md
cmd    and at marker 1 the IMPORT you cited succeeds
out    imported, MILESTONE= R2 STEP= 1
judge  the difference appears only once `docs/reports/R2/step-0.md` EXISTS, which at this
       commit it does not -- it is untracked. The right reason for 0 over 1 is simpler and
       does not need the generator: step 0 is the step being worked, so 0 is the only value
       that makes every resolver name the file the next revision adds. Marker 1 would point
       them at a report that will never be written during step 0.
```

**(2) The FS1/FT1 predicate on the staleness red: I reach your conclusion, by the other
route.** See THE RED under Findings. It blocks; CZ1 (iv) stands; `--check` alone will not
clear it.

**(3) The cherry-pick of verdict 59: ACCEPTABLE HERE, AND I VERIFIED THE BYTES MYSELF
RATHER THAN TAKING THEM. The procedure item is not the cherry-pick.**

```
cmd    git rev-parse review/91c2d2e05c7b ; git diff review/91c2d2e05c7b adc6c3c -- docs/reviews/R2/step-0.md
out    8d40843a353ad580f1faba5c9babeadcc61c5b6b
       (empty)
cmd    git show --stat adc6c3c
out    docs/reviews/R2/step-0.md | 246 +++++  -- one file, 246 insertions, nothing else
rule   CLAUDE.md's escalation head is "a write to `docs/reviews/` outside
       `write_verdict.py`". The content was written by `write_verdict.py` on my branch and
       is byte-identical here, so nothing was written to that tree by any other hand.
       SUPERVISOR.md's `--ff-only` exists so that the move "cannot alter a byte"; that
       property held, and it held as a MEASUREMENT instead of as a structural guarantee.
```

So: not an escalation, and the verdict commit is clean and separate from the code it judges,
which is what step gating actually requires. **What I would record for Xabier is the cause
you named, not the cherry-pick**: the `--ff-only` door presumes the branch does not move
while a review is in flight, and once `8c0edce` landed on `F3` a linear-history merge of my
branch was impossible -- rebase-then-ff and cherry-pick are the same operation. The rule
that would have prevented it is "do not commit to the reviewed branch between invoking the
reviewer and merging the verdict", and that is not written anywhere. One line for Xabier; I
am not asking for a round on it.

**(4) `8c0edce`, which you flagged as unjudged: JUDGED, AND IT IS SOUND -- but note that
this commit reverses it.** Its diff is one file, `docs/milestones/R2.md`, retiring R2's
marker; its three-row control (`19 failed` / `54 failed` / `8 failed`, one variable each)
is the right shape and its EG3 (i) trace of the remaining eight runs each id individually
with a counted inner site, which is the discipline the eighty-third verdict asked for. **Two
observations rather than findings.** First, `3d24e1c` puts the live marker back on R2 at
step 0 and retires R1's -- i.e. it ships the middle row of `8c0edce`'s own control, the one
that commit measured at `54 failed, 103 passed` and rejected. My measurement of that state
now is **108 failed**, higher because verdict 59 exists and two guards are parametrised over
its findings and sites. That is not a contradiction -- the marker had to move for R1205 --
but `8c0edce`'s comment, which said "R1's marker stays live until R2 has a report to gate",
is the sentence `3d24e1c` overrode without withdrawing (it is gone from the file, so this is
an observation and not R1215). Second, `8c0edce`'s eighth red,
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`, is in my 108 as well and its exit is now
the ordinary one: it is FT1 limb two, and FP1's push is what clears it.

## Ledger (FR1: none of these can cause a silently wrong result; one line each)

* **R1216 -- Â§2c's census and Â§3's step-0 gate describe the PRE-change tree, in the commit
  that changed it (CP3/BP0).** Â§2 is headed *"What exists today, measured"* and Â§2c's `out`
  block lists all seven assignments in their old form with `-> MISSING`
  (`export_platform_deck.py:45 ROOT.parent/"HSP-runs"`), while the same commit rewrote :45
  to `hsp_pin.worktree("runs")`. The paste is void the moment an edit follows it. And Â§3's
  gate routes **"`export_buoy_centers_ref.py` and `hsp_pin` on `worktree_stable`"** while
  the commit DELETED `hsp_pin`'s own assignment rather than routing it -- so the shipped
  state is **six assignments in five files**, not the seven in six the gate names.
  `git grep -n "hsp_pin.worktree(" -- scripts` returns six lines; `git grep -n HSP_WORKTREE`
  returns no code site anywhere.
* **R1217 -- two citations land three lines short.** `export_f4_dynamic_inputs.py:390` is
  `"joint_body_b"`; `body_mass` is `:393` -- the substantive claim ("taken from the deck the
  solve used", `float(body[n].mass)`) is correct. `report_joint_reactions.py:106` is the
  `is_dir` check; the DS0 name refusal is `:109-110`. The second is inherited from verdict
  59's own text, so it is mine as much as yours.
* **R1218 -- Â§4 row 1's FORM is half right, and the justification is attached to the wrong
  quantity.** Trim in absolute radians is sound (an angle is already dimensionless). Draft
  in absolute **metres** is the form my own standing rule calls a defect -- it either fails
  the unit-scaling test or passes it vacuously -- and the reason given, *"a relative
  tolerance on a draft that passes through zero trim is unbounded"*, is trim's reason
  wearing draft's label: draft does not pass through zero. Verdict 59 named the response
  scale it should be relative to (the BEM reference draft, or the buoy radius). Nothing is
  compared yet, so no number can be wrong today; it becomes CZ0 (b) the moment step 2
  writes the entry.
* **R1219 -- a RELATIVE value in either key makes the resolution CWD-dependent, which is
  the defect GI3(e) exists to remove.** Measured, one variable (the cwd):
  `FLOATFEA_HSP_RUNS=HSP-runs` gives `...\scratchpad\fake\HSP-runs` from one directory and
  `...\scratchpad\HSP-runs` from another. `is_dir()` is tested before `resolve()`, so which
  tree is found depends on where the script was invoked. One line: resolve a relative value
  against `_repo_root()`, or refuse it.
* **R1220 -- NOTHING EXERCISES `hsp_pin.worktree`, and that is how R1213 and R1214 stayed
  invisible.** `git diff --stat 91c2d2e..HEAD -- tests` is empty while the commit adds ~95
  lines to `floatfea/`; `git grep -n "hsp_pin.worktree\|worktree(\"" -- tests` returns
  nothing. Both blocking findings above are one assertion each in a test that does not
  exist, and the DS0 refusal has never been run with the property it claims broken. *A gate
  carries its own failure* -- the repair of R1213 is the place to put it, not new apparatus.
* **The `declared` parameter is a config key no config declares.** The docstring calls it
  "a config key, `floatsim.worktree_runs` / `floatsim.worktree_stable`"; those names exist
  only in `R2.md:249-250` and in that docstring, no caller passes `declared`, and no schema
  mentions them. True of a half-built mechanism and fine as such -- it is named here so the
  revision that wires it closes R1214 in the same breath (CW0: prose in the source tree
  does not claim things about the code).

## Tolerances touched

**None, measured twice.** `git diff adc6c3c..3d24e1c -- floatfea/tolerances.py` is empty and
so is `git diff 91c2d2e..3d24e1c -- floatfea/tolerances.py`. No declared counter moves: the
only tolerance-shaped values in the diff are `R2.md` Â§4's five FUTURE declarations, three of
which are to be written and two of which are correctly classified as not-tolerances -- I
re-checked both classifications and both still hold, and the iteration cap's "nothing
mechanical will hold it" note is true (`tests/test_no_tolerance_literals.py:39`: *"integers
are counts and are never flagged"*). **EU1 therefore does not arise**, and I still ran the
model at configurations the diff did not choose -- which is where R1213, R1214 and R1219
came from.

## Corpus

**No batch, and ES0 is why, not GC3.** An interim check is light by rule: *"No corpus batch,
no closure list."* My own instructions say "add unseen entries at every review"; where the
two differ, CLAUDE.md governs and I am saying so rather than quietly following the looser
one. **What I ran instead is the recorded substitute, and it produced both blocking
findings**: a sweep of the new resolver at seven configurations the diff did not choose
(declared-wrong + env-right, declared-wrong + nothing, `require=True`, the runs key pointed
at the real `HSP-stable`, the stable key set-but-wrong over an existing legacy sibling, a
relative value from two cwds, and all seven touched scripts imported with no worktree and no
env at all), plus a one-variable control on the marker state and a regeneration check on the
plan's own citations. **Batch 26 had already predicted the marker half**
(`tests/corpus/plan_step_marker_resolution.txt`, `id=step_number_is_zero`); nothing in
`tests/corpus/` covers worktree-key resolution, and the R1213/R1214 shapes are the entries
I would write next round if the repair has not already closed them.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN -- which GI6 holds anyway, so this HOLD costs
no schedule.** It is not a stop-work order: step 0's remaining items (the FloatSim run,
GI3(b)'s wall time, (a) and (d)) are exactly the right work to continue with. What must not
happen is step 0 CLOSING with the five conditions below unanswered, and **all five of them
fit in the follow-on commit CZ1 (iv) already requires.** No re-measurement of anything the
plan already settled.

1. **R1213 -- `run_floatsim_design_waves.preflight()` refuses on the measured input.** The
   name test the other two sites already carry, added **beside** the identity test rather
   than replacing it, and the run pasted: `FLOATFEA_HSP_RUNS` pointed at the stable
   worktree, `FLOATFEA_HSP_STABLE` unset, `preflight()` called. That is also `R2.md:253`'s
   and `:291`'s own promise.
2. **R1214 -- a key that is SET and not a directory REFUSES; only an UNSET key falls
   through.** `tried` already distinguishes them. Show both directions (EH4): the set-wrong
   case refuses, and the unset case still resolves through to the legacy sibling so a
   conforming checkout keeps working.
3. **R1206 -- one exit taken, and ruling (1) says it needs no directive and no hook edit.**
   `tests/test_report_carried.py:100`, `:111`, `:617`. Then
   `test_the_plan_names_the_step_under_execution` is green with R2 step 0 under execution,
   and the three-cell table re-run. If you choose a different exit, say which and why; what
   is not available is leaving the tree red by design, which is C89's measured cost.
4. **CZ1 (iv) -- the staleness red answered, in this order, with both outputs pasted:**
   `python scripts/export_f4_dynamic_inputs.py --check` **first** (your determinism
   prediction, GI3(b)'s wall time, and `R2.md` Â§6 item 2's premise, in one run -- and if it
   reports a difference, STOP: that is the escalation, and the provenance is not refreshed);
   then a full **write** run, which is the only thing that rewrites `import_closure`. Expect
   the git diff to be `dynamic_inputs.provenance.json` alone -- `savez_compressed` is
   byte-reproducible, measured above -- and if `dynamic_inputs.npz` moves in that diff, the
   arrays moved and Â§6 item 2 is live. Then the guard green at the follow-on commit.
5. **R1215 -- the marker comment says what the marker says** (FF0, next commit, not the
   ledger).

**And for the step-0 report itself, so the next revision is a revision and not a round:**
its `Answers:` header names **THIS verdict and this sha**, not verdict 59 -- the newest
verdict is the one the guard checks against and the one thing a machine cannot check; the
`Carried` section answers R1206, R1213, R1214 and the ledger above **by hand**, since
`check_carried.py` now correctly reports R2 and will name every finding in this file; and
verdict 58's twelve open items plus verdict 59's four report items are due in it.

**Rounds: step 0 has consumed NONE of its three ES0 revisions.** Verdict 59 was the plan
lock and this is an interim check; both count against none. The next report revision is the
first.

**Nothing here is a STOP, and I considered it.** Rung 4 is red, which is the one thing that
reads like a low-rung failure -- but the red is a provenance-digest comparison, not a
numerical disagreement at a rung, and the low rungs cannot be reached by this diff. Measured
rather than assumed: `git diff --stat 91c2d2e..HEAD -- floatfea` is `hsp_pin.py` ALONE, and
`git grep -ln hsp_pin -- tests` (excluding the corpus) returns exactly
`rung3/test_platform_deck_export.py` and `rung4/test_f4_g41_dynamic.py` -- so rungs 1, 2, 5
and 6 contain no test that reaches a changed line. Rung 3's deck-export test and the rest of
rung 4's G4.1 gate are green in my own run at this commit. I did NOT run rungs 1, 2, 5, 6 or
`tests/regression` locally, and CI's ladder job at this sha had not concluded when I ruled;
CI runs rung 6 and `tests/regression` BEFORE rung 4, so the staleness red will not hide
them. The plan is faithful to GI and nothing in it needs reopening.

**What this commit got right, and it is the larger part.** It answered three of four
blocking findings in one commit with no re-measurement asked for, which is what verdict 59
said the HOLD should cost. The two-key routing is correct at every one of the six sites, and
`require=False` is the right default for the right reason -- R670's import-time failure --
which I measured by importing all seven touched scripts with no worktree and no environment
at all. It deleted `HSP_WORKTREE` rather than wiring a constant nothing reads. It raised two
procedure items against itself before I could find them, and the escalation it refused to
take was refused on the correct rule even though the premise turned out to be wrong. And it
said plainly that the red blocks and that R1206 is open, which is the behaviour that makes a
report worth reading last.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 91c2d2e05c7b89a6169c359bc144a1438b6540a1
**Reviewed commit: `91c2d2e05c7b89a6169c359bc144a1438b6540a1`.**
Verdict: HOLD
Scope: **the PLAN-LOCK round GI2 asks for** -- `docs/milestones/R2.md`, added at `91c2d2e`, judged against `docs/directives/GI.md` recorded verbatim at `de04131`. It consumes **none of step 0's three ES0 revisions** and closes nothing, so `--closes` is correctly absent (FK1). Ruled under **FR1 with EZ0**, and every blocking finding below names the silently wrong result it produces. **GE3: `R835: unchanged, R2`. Not re-measured.** EU1 does not arise -- `git diff de04131..HEAD -- floatfea/tolerances.py` is empty and the commit touches one file -- and I ran the model at configurations the diff did not choose anyway. **GA3's length target is OVERRUN and I say so rather than trimming the evidence**: the overrun is four blocking findings with their controlled cells, an independent re-derivation of sec.2's five blocks, a read of HSP's own deck builder, and a procedure finding of my own.
Tests: **692 passed, 0 failed, 0 skipped** on `tests/unit` plus the four root guards, my own run in my own worktree at the judged sha, `-p no:randomly`: `692 passed in 194.86s`. That is **470 + 222 and it matches your two runs exactly.** The three report-guard files: **19 failed, 320 passed in 110.41s.** CI's identical guards selection at the judged commit: **19 failed, 1235 passed in 588.62s -- the SAME nineteen ids**, so the two measurements agree and nineteen is the whole of it. I did not re-run `tests/verification` or `tests/regression`, and the reason is measured: `git diff --stat 251af69..91c2d2e -- floatfea tests scripts .github` is **EMPTY**, and the last concluded run's ladder was SUCCESS on all six rungs over that byte-identical code.
CI: **run `44107452079` at the full sha `91c2d2e05c7b89a6169c359bc144a1438b6540a1` EXISTS and `lint, unit and guards` CONCLUDED FAILURE**, at step 10 `guards and meta-tests`, with actionlint, ruff, black, mypy and the unit tests all `success` **before** it -- so the guards step is seen to have RUN rather than been skipped behind an earlier red (CZ1 iii). `the verification ladder` had **NOT finished when I ruled** (`in_progress`); a run that has not finished is not a pass, and no rung is red, so nothing here is a STOP. Both determinism jobs `skipped` by their own `workflow_dispatch` condition. **This is not CK2** -- runners were assigned and the jobs executed for ten minutes. **CA2 IS REACHED: the job is red at the judged commit and twelve of its nineteen reds FAIL the FS1/FT1 predicate**, so the EG3 waiver does not cover them and CZ1 (iv) stands. FP1 held -- the commit was pushed before I was invoked, which is also why `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` is GREEN here and was red at `251af69`.
Door (FV2 / GG2): `git worktree add -b review/91c2d2e05c7b <a path outside the repository> 91c2d2e05c7b89a6169c359bc144a1438b6540a1` **succeeded on the first try, so no review of this commit existed.** Every measurement below taken in that worktree; this verdict written there through `scripts/write_verdict.py`, committed on that branch and pushed. **Two writes of my own, both in my worktree and both reverted before committing** -- the marker cells in R1206 -- and `git status --porcelain` there is empty. In `C:\dev\floatfea` I ran only read-only `git` and `gh`.

**THE FILENAME I WAS ASKED FOR DOES NOT EXIST AND COULD NOT, SO THIS IS `step-0.md` -- R1212.** `scripts/write_verdict.py` writes `docs/reviews/<milestone>/step-<step>.md` and has no other path, the `PreToolUse` hook refuses every other door into `docs/reviews/`, and `scripts/ci_section.py:153-157` globs `step-*.md` with `re.fullmatch(r"step-0*([0-9]+)")` -- so a verdict at `plan.md` would have left R2's CI-section anchor missing and the report guards red with nothing in the loop able to clear them, which is the FP1 failure mode `CLAUDE.md` already records.

## The nineteen, per id, at this commit -- traced from CI's own messages, not classified by family (EG3 (i))

```
cmd    the FAILED list from CI's completed `guards and meta-tests` step, read from
       the job log rather than inferred
out    1   test_the_plan_names_the_step_under_execution
             "2 plans carry a `<!-- step-under-execution: N -->` line
              (['R1.md', 'R2.md']); exactly one must ... which is how a guard comes
              to read a closed milestone's last step and report green while checking
              nothing."
       11  test_the_FAILED_reader_takes_an_id_WITH_A_SPACE[...] -- ALL ELEVEN
             "SystemExit: .../docs/milestones/F2.md carries no
              `<!-- step-under-execution: N -->` line" (scripts/ci_section.py:135)
       7   test_the_guard_survives_the_state[...] -- 2 "expected a clean run",
             5 "a file that is not a numbered step must be stepped over"
cmd    the inner run inside each of the seven, from its own output
out    "12 failed, 284 passed" in all seven, and the twelve ARE the twelve above
cmd    the control -- CI's FAILED list at 251af69, where only R1.md carried a marker
out    7  test_the_guard_survives_the_state[...]   <- the SAME seven
       1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  <- GREEN here
       and NEITHER test_the_plan_names... NOR any FAILED_reader id
rule   FS1 with FT1, per id. Limb one: names a finding or a site of the NEWEST
       verdict (63affd1's entry on 602bce8). Limb two: its SUBJECT is the commit
       carrying it.
judge  **THE SEVEN are EG3 state (2) and the waiver holds** -- a verdict exists and
       no answering report revision does; they are red in both trees and R2's first
       report clears them. **THE TWELVE ARE NEW AT THIS COMMIT AND FAIL BOTH LIMBS.**
       `docs/milestones/R2.md` did not exist when the newest verdict was written and
       is not among its sites, and none of the twelve is about the commit carrying
       it -- their subject is the marker state of two plan files. **So CZ1 (iv) is
       unchanged for the twelve, and that is R1205 and R1206.**
```

The seven's inner list has gone from **one** id at the previous verdict's trace to **twelve** here, which is the control that the cascade follows its cause rather than being a fixed family -- and the cause it is now following is the one this commit introduced.

## Carried

The newest verdict is `63affd1`'s entry on `602bce8` (verdict 58), and its open items are routed to **R2's first report**, which does not exist yet -- this commit is the plan commit GI2 makes the first of the milestone, so it predates the report that answers them. None of them is answerable by a plan file and none holds this lock. Status, one line each:

* **R1202 (FF0, the base-case sha at five sites) -- ANSWERED before this commit**, at `bb952e7` (`closure: R1202 (FF0) at FIVE sites, not the four named`). Not carried.
* **R1196, R1197, R1198, R1199, R1200, R1201 -- still open, due in R2's first report**, as verdict 58 item 2 routes them. Six prose/one-line items in two files; none blocks under FR1 and none is a plan matter.
* **R1186, R1188, R1189 (c), R1190, R1191, R1193 -- still open, routed to R2** by verdict 58 item 3. R1193 (the dead corpus-pause clause in my own instructions) is **DISCHARGED from my side**: `2e08766` replaced it and I am operating under the post-`2e08766` text -- `grep -c "the corpus pause is \*\*EXPIRED\*\*" .claude/agents/gating-supervisor.md` is 1. R1188's concurrency lever is **answered by GG3**: the group is now per-commit and run `44107452079` started 3 s after creation rather than queueing 71 minutes.
* **R1203, R1204, R835 -- reviewer-side or Xabier's.** R835 is R2's under GE3 and I did not re-measure it.
* **Verdict 58 item 4 -- the one I check here.** It asks R2's first report to answer the newest verdict's commit and carry verdicts 55 through 58. `docs/milestones/R2.md:12` carries that instruction by sha (`63affd1` or later) and by number (verdicts 55 onward), faithfully to GI2. Nothing to answer yet.

## Findings

**R1205. TWO plans carry a live `step-under-execution` marker, and the gate that enforces the `Carried` section now reports on F2 step 4. BLOCKS.**

```
claim  how many plans declare a step under execution at this commit
cmd    grep -rlE "<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->" docs/milestones/
out    docs/milestones/R1.md      (line 3: `<!-- step-under-execution: 4 -->`)
       docs/milestones/R2.md      (line 3: `<!-- step-under-execution: 0 -->`)
cmd    python -c "import sys; sys.path.insert(0,'scripts'); import check_carried as cc; print(cc._active_step())"
out    ('F2', 4)
cmd    python scripts/check_carried.py ; echo exit=$?
out    check_carried: the newest report's Carried section omits R216, R217, R218,
         R219, R220, R221, R222
       verdict declares 7 findings; 0 are carried
       exit=0
cmd    python -c "import scripts.ci_section as c; print(c.MILESTONE)"
out    SystemExit: docs\milestones\F2.md carries no `<!-- step-under-execution: N -->`
       line, so there is no step to generate a section for.
rule   scripts/check_carried.py:126-130 and scripts/ci_section.py:98-106 -- both fall
       back to F2 when the count is not exactly one; .claude/hooks/require-verdict.sh:105
       blocks a turn on it; tests/test_report_carried.py:608 asserts against it
judge  **New at this commit** -- at `251af69` only R1.md carried a marker and
       `test_the_plan_names_the_step_under_execution` was green in CI there.
```

**The silently wrong result:** `scripts/check_carried.py` -- the gate that enforces the one thing `CLAUDE.md` says the whole arrangement exists for, that the previous review's open items get re-read -- reports on `docs/reports/F2/step-4.md` against `docs/reviews/F2/step-4.md`, names seven F2 findings nobody has to answer, and **exits 0**. R2 step 0's report can ship with an absent or wrong `Carried` section and nothing is red. Its own comment is the sentence: *"a guard reporting green about the wrong milestone."* Second consequence: `scripts/ci_section.py` cannot import, so R2's report cannot generate the CI section CE1 makes mandatory, and **11 report-guard ids die on that import** (`SystemExit` at `scripts/ci_section.py:135`). *Closed when* `docs/milestones/R1.md:3` retires its marker the way `F2.md:10`, `F3.md:9` and `F6a.md:3` retire theirs -- `<!-- step-under-execution: moved to R2 at step 0 (GI) -->` -- in a commit that also answers R1206.

**R1206. `step 0` is not representable: `0` is both a legal step number (GI3) and the resolvers' sentinel for "unclear". BLOCKS (CZ1 (iv)); apparatus, so FF0 and not the ledger.**

```
cmd    cell 1 -- the judged tree (R1=4, R2=0), test_the_plan_names_the_step_under_execution
out    RED: "2 plans carry a `<!-- step-under-execution: N -->` line"
cmd    cell 2 -- R1's marker retired, R2's left at 0. ONE VARIABLE MOVED
out    RED: "docs/milestones/R2.md carries no readable step number, so the guards fell
       back to the newest complete report/verdict pair ... it makes the step boundary
       permanently red."   assert 0 > 0   where 0 = _plan_step()
cmd    cell 3 -- R1 retired AND R2's marker set to 1
out    RED at tests/test_report_carried.py:639 instead -- the expected "no report yet"
       state, which R2's first report clears
rule   tests/test_report_carried.py:617; _active_plan returns the sentinel `(None, 0)`
       at :110, so a real step 0 and "no marker" are the same value
judge  Retiring R1's marker does NOT clear this. My own corpus predicted it:
       tests/corpus/plan_step_marker_resolution.txt, `id=step_number_is_zero`,
       `expect=caught measured=RED_the_plan_carries_no_readable_step_number`, batch 26.
```

On its own this red is TRUE and loud, so it misleads nobody once R1205 is fixed -- but it cannot be left, because a tree red by design is a tree in which the next real red is harder to see, which is C89's measured cost, and FF0 puts an item in the gating apparatus in the next commit rather than the ledger. Three exits and **the choice is yours, not mine**: renumber R2's steps 1..5 (which breaks GI's own numbering and GI2's "before any step-1 code"); keep the marker at the NEXT step and record step 0 another way; or separate the sentinel from the value in the three resolver copies and the two scripts -- a repair of an existing guard, which EK2 permits and FK2's "no new apparatus" does not forbid. *Closed when* one is chosen, the cell above is re-run, and `test_the_plan_names_the_step_under_execution` is green with R2 under execution.

**R1207. Step 2's gates (ii) and (iii) are both passed by a build in which the mass never reaches FloatSim. BLOCKS.**

```
claim  what the zero-change test's own input is
cmd    python -c "import yaml; d=yaml.safe_load(open('data/platform/platform12_deck.yaml'));
         print([(b['name'],b['mass']) for b in d['bodies'] if b['name'] in ('platform','hub1')])"
out    [('buoy1', 28.67)... ('hub1', 12.0), ('platform', 20.0)]
cmd    python -c "import numpy as np; z=np.load('data/f4/dynamic_inputs.npz');
         print(list(z['case0/body_mass']))"
out    [20.0, 12.0, 12.0, 12.0, 12.0]
rule   GI5 step 2: "feeding today's masses reproduces the reference run ... bit-identical"
judge  the committed deck's masses ARE today's masses, so a build whose override
       plumbing is a NO-OP reproduces the reference run EXACTLY. (ii) is green on code
       that ignores its mass input entirely.
claim  whether (iii) can fail
rule   D1: `body mass = m_nonstruct + k x m_steel`; GI5 step 2: "member steel +
       non-structural + ballast = body mass, exactly"
judge  D1 DEFINES body mass as that sum, so the identity is over FloatFEA's own
       arithmetic and cannot fail on anything but an addition bug.
```

**The silently wrong result:** the converged design step 3 publishes -- its sections, member forces, utilisations, the iteration table, and everything it writes under `results/` -- computed from FloatSim runs that used the deck's own masses rather than the sized ones, with gates (ii) and (iii), `pytest`, `ruff`, `black`, `mypy` and all six ladder rungs green. That is the loop still open at exactly the end GI0 exists to close, and no gate in the locked set would say so.

**The repair needs no new apparatus, because the mechanism already ships, inverted.** `scripts/export_f4_dynamic_inputs.py:467-479` is already Q8's rule -- `np.array_equal` over every array, *"there is no tolerance on this comparison"*, non-finite failing in its own right. So **(ii) becomes a pair**: the zero-change run reproduces bit-identically **and** a run at a perturbed mass does NOT, differing in `case<i>/body_mass`, `m_xddot` and `accel`. And **(iii) closes against the run's own record** -- `case<i>/body_mass`, which `export_f4_dynamic_inputs.py:390` takes from the deck the solve actually used -- rather than against the tool's variables. Provenance, not existence. *Closed when* sec.3's step-2 gate carries the inverted half of (ii) and (iii) reads back from the npz.

**R1208. sec.2c specifies ONE config key routed to all six sites, and the six sites are not one worktree. BLOCKS.**

```
cmd    for each: test -d and git describe --tags
out    C:/Users/xlama/OneDrive/Documents/buoy/HSP-stable  EXISTS  floatfea-ref-1
       C:/Users/xlama/OneDrive/Documents/buoy/HSP-runs    EXISTS  floatfea-ref-1
       ../HSP-stable and ../HSP-runs from C:\dev\floatfea  BOTH MISSING
cmd    git grep -nE '(ROOT|parents?\[[0-9]\])\s*(\.parent)?\s*/\s*"HSP-' -- '*.py'
out    scripts/export_buoy_centers_ref.py:42    HSP_STABLE -> HSP-stable
       scripts/export_platform_deck.py:45       HSP_RUNS   -> HSP-runs
       scripts/measure_platform_joints.py:48    HSP_RUNS   -> HSP-runs
       scripts/report_joint_reactions.py:96     HSP_RUNS   -> HSP-runs
       scripts/run_floatsim_design_waves.py:50  RUNS       -> HSP-runs
       scripts/run_floatsim_design_waves.py:51  STABLE     -> HSP-stable
rule   DS0, enforced by three refusals keyed on the NAME `HSP-stable`:
       report_joint_reactions.py:106, export_platform_deck.py:75,
       run_floatsim_design_waves.py:98
judge  five of the six sites want HSP-runs, one wants HSP-stable, and the three
       refusals make a single key pointed at HSP-stable loud. **The remaining
       direction is silent**: a single key pointed at HSP-runs sends
       `export_buoy_centers_ref` there, and that script has no DS0 refusal of its own.
```

**The silently wrong result:** `data/platform/buoy_centers_ref.json` -- a shipped data file, the input to EB6's label-provenance gate -- regenerated from `HSP-runs` while its `"source"` field declares `HSP-stable/studies/platform-12buoy/platform_common.py` and `_blob_sha` records that tree's sha. `--check` stays green because both sides move together, which is C155's shape, recorded in that file's own docstring. Both worktrees are at `floatfea-ref-1` today, so the bytes match and nothing shows -- and R2 is about to start running FloatSim in one of them. That is FR1's second head verbatim: an input accepted and used other than as declared. **FZ rule 7 would probably reach the right answer on its own**, and I block anyway because the plan's own words specify the wrong thing and GI2 gives no review between this one and step 0's close. *Closed when* sec.2c and sec.3's step-0 gate say TWO keys, name which sites take which, keep `export_buoy_centers_ref` on the stable key, and show the three DS0 refusals still firing.

## The four rulings you asked for

**(1) Is the plan faithful to GI? YES on every gate, with two departures you should state.** GI5 step 2's four sub-gates are all present at `R2.md:173-180` and GI5 step 3's acceptance at `:182-187`, none softened. Five additions are all STRICTER and each traces to GI's own text: read-only-on-HSP and the run folder on (i) (GI1), "not warned" on (iv), the refusal-by-name for a non-converged design on step 3 (D3's last sentence, which GI5 step 3 did not itself carry), the heading refusal on step 1 (FL2(c)), and "never the witness" on step 4. The departures:

* **GI5 step 1's input is "a FloatSim npz"; `R2.md:168` makes it "a FloatSim solve".** sec.2d's reading is right and I measured it: `scripts/export_f4_dynamic_inputs.py:187-196` calls `solve_one`, and the npz is that run's OUTPUT -- there is no FloatSim-written npz in this repository to read. But the consequence is that **step 1 performs the FloatSim invocation GI5 assigns to step 2**, which GI6 gates, and the plan does not say so. State which, and which part of GI6's hold it crosses.
* **`R2.md:165` drops GI3(d)'s purpose clause** "so draft can be held (GI4 D2)". One clause; sec.4 row 1 carries the tie. Prose.

And one addition I checked rather than accepted: step 1's `U = 1.71167` **"at `platform:hub4_arm` ROOT"** is right as the TOOL's own line, and it is a **tie at six figures** -- `docs/F6_utilisation.csv:40` and `:44` give `hub2_arm` and `hub4_arm` the same `1.71167`, and `docs/USER_GUIDE.md:966-975` records the full-precision split. An acceptance that asserts the member NAME must read the tool's line, never a `max()` over the rounded CSV.

**(2) Are sec.2's five measured blocks true? Four yes, one wrong in its `out` line, and the census in sec.2c wrong three ways.**

* **sec.2a -- TRUE, and the "no escalation" conclusion is RIGHT.** The census reproduces line for line (four sites, the numbers as printed), and the mechanism reproduces by reading: `solve_one` builds the deck from `prp._deck_with_drag()`, mutates it at `report_joint_reactions.py:158-163`, and runs `integrate_cummins` -- a FloatSim **time-domain** integration, in-process, HSP source untouched. `case0/body_mass = [20.0, 12.0, 12.0, 12.0, 12.0]` reproduces too. **I went one step further than the plan and read HSP's own builder, which settles GI3(c) harder than sec.2a does:** `platform_rao_pilot._deck_with_drag()` **takes no arguments and reads no file** -- it constructs all 17 bodies in Python from `platform_common.py:41` (`PLATFORM_MASS = 10.0`), `:158` (`mass=cc.ARM_MASS_TOTAL`), `:159` (`Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)`, the hubs) and `:177-178` (the platform). So there is **no file input to HSP's builder at all**, the returned object is the only override point, and the escalation GI1 contemplates is not merely unnecessary -- it is the ONLY alternative, and it would be an edit to FloatSim source. **Your reading is right; raise no escalation.** And an independent corroboration the plan does not give: GI4 D1's own `625 t` and `375 t` are `(1 - 0.75) x 2500 t` and `(1 - 0.75) x 1500 t`, i.e. ER0's platform at lambda = 50, not HSP's 1250 t -- **GI4's numbers confirm sec.2a's reading of "today's masses"**. Caveats are R1207 and R1211.
* **sec.2b -- the conclusion is TRUE and reproduces; one `out` line is FALSE.** `periods_full_s = [10, 12.5, 14, 15, 16.2, 20]`, six cases in the npz, one heading => **six FloatSim cases per iteration** YES, and D4 needs no working-set escalation on heading count YES. But "config declares ONE heading" is not what the command returns: `grep -n heading examples/platform12_placeholder.yaml` returns exactly one line and it is **a comment at line 8**. The config declares **no heading key at all**; heading 0 lives in `report_joint_reactions.WAVE_HEADING_DEG` and in `data/f4/dynamic_inputs.provenance.json`'s `run.heading_deg: 0.0`. **That matters forward**: D4's "every heading in the R1 config" is *unrepresentable* today, and that absent key is what step 1's heading refusal has to grow into. **The 3.66 h / 40.6 GB figures ARE good enough for a plan row, and the reason is specific**: the second heading is excluded by GI1's ban on `platform_bem.py`, not by its cost, so the figures could be wrong by a decade and sec.2b's conclusion would not move. The plan attributes them to the docstring, which is what BP0 needs. One wording point -- sec.2b bolds them as "**measured**" when they are *recorded as measured elsewhere*; if any decision ever rests on them, they get re-taken.
* **sec.2c -- the diagnosis is RIGHT, the WIDER READING IS AUTHORISED, and the census is wrong three ways.** See the ruling below and R1208/R1209.
* **sec.2d -- TRUE and measured.** `cli.py:1279` is the FL2(c) comment, `:1291-1297` the refusal, and the command validates its config and the declared cases before refusing.
* **sec.2e -- TRUE, and I reproduced the consequence rather than reading it.** `rho_eq = f.M_b/(L_b.A)` by construction (`floatfea/model/platform.py:47-48`), so at the shipped config the builder gives platform `rho_eq = 7146.0` / member mass `1875.0 t` and each hub `11433.5` / `1125.0 t` -- **independent of the section, exactly as claimed**. `cli.py:830-833` ships the same sentence to every reader. The second sentence (three configurations, identical densities) carries no triple and I did not reproduce it; the mechanism half is enough to carry sec.2e.

**THE RULING ON THE SIX-SITE READING, WHICH YOU ASKED FOR DIRECTLY: YOUR READING IS RIGHT AND I WOULD GO FURTHER.** GI3(e) names `hsp_pin.HSP_WORKTREE` as the symptom -- *"It does not resolve from `C:\dev\floatfea`"* -- and prescribes a mechanism (*"a config key with an env-var fallback"*). Fixing only that constant fixes **nothing**, and that is measured: `git grep -n HSP_WORKTREE` over the whole tree returns the definition at `floatfea/hsp_pin.py:20` and three documentation hits, and **no consumer**. GI3(e) exists so that step 0's own items (b) and (d) can open the worktree, so routing the sites that actually open it through the new key is the **same item**, not new scope. It is authorised; write it. **R1208 is the one condition on it**: two keys, not one.

**(3) The two "not a tolerance" classifications -- BOTH CORRECT, and one has a shipped precedent.**

* **The iteration cap `8` -- correctly not a tolerance.** Nothing is compared against `8` to decide a result is good; exceeding it produces a **refusal** (D3's "stop and report", `R2.md:186`'s "refused by name"), not an accepted number. That is this repository's own test, stated in `PLATFORM_MASS_OVERRIDE`'s docstring: *"not-a-tolerance: ... Nothing is compared against them."* **But the classification is only as safe as that refusal, and nothing mechanical will hold the value**: `tests/test_no_tolerance_literals.py`'s own docstring says *"integers are counts and are never flagged"*, so `8` becoming `80` is invisible to the one guard that would look. Declare it as a named module constant with a `not-a-tolerance:` justification -- the convention `PLATFORM_OVERRIDE` and `hsp_pin.BASELINE` already use -- so raising it is a visible act. And `R2.md:195` says "**Every** value below goes in `floatfea/tolerances.py`" while two rows say they are not tolerances: say where those two live.
* **The determinism bound -- correctly not a tolerance, and row 5 is not a declaration to write at all.** The comparison already exists in exactly the right form at `scripts/export_f4_dynamic_inputs.py:467-479`: `np.array_equal` on the raw arrays, *"A regeneration either reproduces it exactly or it does not (Q8); there is no tolerance on this comparison"*, with non-finite values failing in their own right rather than comparing equal to zero. Step 2 reuses it rather than re-deriving it. **And that makes sec.6 item 2 measurable today -- see (4).**

**(4) What sec.6 should settle now. Three things, and the first is nearly free.**

**(a) sec.6 item 2's premise is measurable TODAY, and the whole of step 2's (ii) rests on it.** `python scripts/export_f4_dynamic_inputs.py --check` re-runs all six cases through `solve_one` and compares bit-exactly against the committed npz. That single command **is** GI3(b)'s wall-time measurement *and* the determinism measurement; running it twice costs one more pass. Nothing in this repository has published a measurement of FloatSim's determinism on this path, and Q8's premise is the thing step 2's bit-identical gate is built on. Convert the argument into a measurement.

**(b) sec.6 does not carry the contradiction between D1 and the step-2 bookkeeping identity, and GI6 is the only scheduled point where D1-D4 can be corrected.** D1: `body mass = m_nonstruct + k x m_steel`. GI5 step 2 (iii): `member steel + non-structural + ballast = body mass, exactly`. **The two are consistent only if ballast == 0** -- and if ballast is identically zero then D2's draft can never be held when `m_steel` moves, so (iv)'s refusal fires on the design rather than on a test. One of the two has to gain a ballast term and Xabier is the one who says which. This is loud rather than silent when it bites, so it does not block; it belongs in step 0's report because that is where it can still be cheap.

**(c) sec.6 item 3 is not a contingency -- it is a number, available today, and step 0 (d) should publish it.** Measured at this commit from the shipped deck and the shipped builder:

```
cmd    which bodies carry a hydro label
out    buoy1..buoy12  hydro_body_label = 'buoy1'...   platform, hub1..hub4  None
cmd    the builder's own member geometry and D1 at k = 1.0, lambda = 50
out    platform  steel 2059.7 t vs 1875.0 t allocated   steel/alloc = 1.0985
       each hub  steel  772.4 t vs 1125.0 t allocated   steel/alloc = 0.6866
       D1: platform 2500 -> 2684.7 t (+7.39%), each hub 1500 -> 1147.4 t (-23.51%)
       the five bodies 8500 -> 7274.3 t = -1225.7 t (-14.42%)
       the 12 buoys carry 43005 t, so the deficit is 2.85% of them
rule   D3's convergence band is 0.5% per body between iterations
judge  **the bodies whose mass D1 changes carry NO buoyancy, and the bodies that
       carry buoyancy are not changed by sizing.** So D2's "every floating body (or
       the buoy carrying a changed body) gets compensating ballast" is written for a
       picture this deck does not have: ballast has to sit on the NON-wetted bodies,
       and "the draft is held" becomes a condition on total weight and its
       distribution, measured per BUOY. And iteration one moves every mass one to two
       decades outside D3's band, so the loop certainly iterates -- what nobody has
       measured is whether the BEM reference survives the ballast it implies.
```

This also reproduces both near ends of `R2.md:31`'s range (`+10%` -> `+9.85%`, `-31%` -> `-31.34%`) at this commit, which is the re-measurement sec.0 routes to step 0 (a).

## Ledger (FR1: none of these can cause a silently wrong result; one line each)

* **R1209 -- sec.2c's census is wrong three ways, in the R755/R1147 shape: an `out` block that reports more than its own `cmd` returns.** The heading says "five sites" and the body says "SIX sites in five files"; it is **six files**, not five; counting assignments it is **seven**, because `run_floatsim_design_waves.py` has two (`RUNS` at `:50`, `STABLE` at `:51`) at line numbers the plan prints as `49-50`; and **the quoted needle cannot see either of them** -- `grep -rn "HSP_RUNS\s*[:=]\|HSP_STABLE\s*[:=]\|HSP_WORKTREE" --include=*.py .` returns **five** lines, not the six printed. The needle that finds all seven is in R1208's block. The plan's `HSP_WORKTREE`-has-no-consumer claim is **TRUE** -- I ran it over the whole tree, not just `*.py`.
* **R1210 -- sec.2b's "config declares ONE heading" is false as measured** (see ruling 2). The conclusion is unaffected.
* **R1211 -- sec.2a and sec.3 use one word for two mechanisms, GI3(c)'s first half is unanswered, and four of the five bodies have never been overridden by anything.** GI1 requires mass changes to go *"through HSP's deck builder with a declared override file, as ER0 did"*; `R2.md:174` says FloatFEA "writes the override file" YES, while sec.2a's judge says step 2 must "move it out of a script global into the tool", which is the **in-memory** path where nothing on disk declares what was applied. ER0 did BOTH -- `export_platform_deck.apply_override` mutates in memory **and serialises to `data/platform/platform12_deck.yaml`**, and `export_f4_dynamic_inputs` records the dict in `dynamic_inputs.provenance.json`'s `"override"` block. Step 2 says which, and the declared-on-disk half is what makes the override auditable. GI3(c)'s first half -- *how* mass and inertia enter the builder -- has the precise answer in ruling 2 and the plan does not state it. And **the existing helper is the wrong shape to generalise**: `_apply_platform_override` selects `b.name == "platform"` and sets three inertia components, while `_inertia_matrix` reads six and *"the off-diagonals are read rather than assumed zero"*; the four hubs sit at `cc.ARM_MASS_TOTAL` and the literal `Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)` with **no override anywhere in this repository**. One body -> five, three components -> six, and `export_platform_deck.apply_override`'s generic dict walk is the better shape.
* **sec.4 row 1 does not declare the FORM of the equilibrium-drift tolerance, and draft is a LENGTH.** An absolute tolerance on a dimensional quantity either fails the unit-scaling test or passes it vacuously, so the entry has to be relative to a stated response scale -- the BEM reference draft, or the buoy radius -- and dimensionless, with trim against a stated angle scale. sec.4's stated purpose is to be reviewable before the value exists, so the form belongs there now.
* **sec.2's CP3 header overclaims.** It says "Figures taken at this commit, after the last edit", and two are not: sec.0's `+10% to +29% / -31% to -55%` (attributed to pre-R2 work and correctly routed to step 0 (a) -- both near ends reproduce, ruling 4c) and sec.2e's "three configurations" (no triple at all, and a causal "so" with no cell, BG0). Say which figures are this commit's and which are carried.
* **sec.2's five triples are not machine-checked and two are not runnable.** `tests/test_tree_prose_consistent.py` reads `^claim:` / `^cmd:` / `^out:`; `grep -c "^cmd:" docs/milestones/*.md` is 0 everywhere, so the space-aligned form R1.md and R2.md both use is invisible to the guard that scans `docs/milestones`. And `python -c "...np.load(NPZ)..."` has no `NPZ`, while sec.2b's is an ellipsis. R1.md uses the same form, so this is the house convention and not a new deviation -- but a `cmd` a reader cannot run is not a check.
* **sec.5 does not carry GI1's "the deck stays DO-NOT-HAND-EDIT".** One line; it belongs beside the three prohibitions.
* **R1212 -- MINE, and it goes to Xabier, not into a round.** I was asked to write `docs/reviews/R2/plan.md`. That path does not exist and cannot: `scripts/write_verdict.py` writes `docs/reviews/<milestone>/step-<step>.md` and has no other path, the `PreToolUse` hook refuses every other door, and `scripts/ci_section.py:153-157` globs `step-*.md` with `re.fullmatch(r"step-0*([0-9]+)")`, so a file named `plan.md` would not be found and R2's CI-section anchor would stay missing -- the FP1 failure mode `CLAUDE.md` already records. I used `--step 0 --interim`: no report revision exists, it consumes none of step 0's three ES0 revisions, and it closes nothing. **The `--interim` header the tool stamps says "ES0 INTERIM CHECK", which is accurate about rounds and mislabels the round's nature** -- this is GI2's plan lock. If a separate plan-lock artifact is wanted, that is an edit to `write_verdict.py` and to `ci_section.py`'s glob, and it is Xabier's to authorise.

## Tolerances touched

**None.** `git diff de04131..HEAD -- floatfea/tolerances.py` is empty and the commit touches one file. sec.4 declares five future entries and I ruled on their classification above; **"None of them exists yet" is true** -- the only convergence entry in the file is `BOUNDARY_BISECTION_CONVERGENCE` at `:1290`, which is a solver-internal bisection and not D3's loop. EU1 does not arise.

## Corpus

**No new batch, and GC3 leaves that to me.** What I ran instead is the substitute GG1 records, and it is where three of the four blocking findings came from: a **continuum grid over the parameter space D1's rule guards** (all five bodies, steel against allocated mass, through the shipped builder -- ruling 4c), a **regeneration check on the published figures** (sec.0's two ranges, sec.2a's npz block, sec.2e's densities, all re-derived at this commit), and **three controlled cells on the marker state**, one variable each. A batch would have bought none of them on a commit that contains no code.

**And batch 26 had already predicted both halves of R1205 and R1206.** `tests/corpus/plan_step_marker_resolution.txt` carries `id=two_plans_carry_it_F3_and_a_new_F4 ... expect=caught measured=RED_2_plans_carry_it` and `id=step_number_is_zero ... expect=caught measured=RED_the_plan_carries_no_readable_step_number`. **The tree is now in both states at once**, eleven batches later, and that is the corpus doing the job it exists for -- which is the reason I am not spending this round writing another one.

## Next step opens when

**STEP 0 DOES NOT OPEN YET, AND THE REASON IS CHEAP: one commit touching `docs/milestones/R1.md` and `docs/milestones/R2.md`, with no re-measurement of anything.** GI2 asks for one round and I am not asking for a second review before step 0's code -- **PASS follows automatically from the four conditions below being visible in the diff**, and I have written them so that the implementer can satisfy them without another invocation. What they must not do is start step 0's code with the gating apparatus in the state R1205 measures.

1. **R1205 -- `docs/milestones/R1.md:3`'s marker retired**, in the form `F2.md:10`, `F3.md:9` and `F6a.md:3` use. Then `python scripts/check_carried.py` names **R2**, not F2 step 4, and `python -c "import scripts.ci_section"` stops raising. Paste both.
2. **R1206 -- one of the three exits chosen for step 0's number**, with `test_the_plan_names_the_step_under_execution` green at R2 under execution, and the cell re-run. If the exit is renumbering, say what happens to GI2's "before any step-1 code".
3. **R1207 -- sec.3's step-2 gate carries the inverted half of (ii)**, and **(iii) reads `case<i>/body_mass` back from the npz the solve wrote.** Both are amendments to `R2.md`, not code: GI6 holds step-2 code regardless, and this is the only moment at which the gate is still free.
4. **R1208 -- sec.2c and sec.3's step-0 gate say TWO keys**, which sites take which, `export_buoy_centers_ref` on the stable key, and the three DS0 refusals shown still firing.

**Then step 0 opens and nothing else does.** GI6 holds step 2 regardless, and step 1's code waits on Xabier's answer to D1-D4 as well -- because ruling (1)'s first departure means step 1 as written performs the FloatSim invocation GI5 assigns to step 2. Say which in the amendment.

**And four things for step 0's report, none of which blocks and all of which are cheap now:** the `--check` determinism run (ruling 4a, one command, answers GI3(b) too); the D1/(iii) ballast contradiction put in front of Xabier (4b); GI3(d) answered with the wetted/non-wetted split and the `-1225.7 t` first iteration (4c); and GI3(c) answered in BOTH halves, with HSP's zero-argument builder named, because that is what tells Xabier the escalation is not merely unnecessary but impossible without an edit to FloatSim source.

**On the schedule.** GI sets no date and `R2.md:14-16` says so rather than inventing one, which is the right handling. This HOLD costs one commit and no measurement. **Nothing here is a STOP**: the plan is faithful to GI, the ladder was green on all six rungs at the last concluded run over code byte-identical to this tree, and no low rung is red.

**What the plan got right, and it is much the larger part.** It went and measured the five things the steps rest on instead of asserting them, and four of the five hold exactly as written. It found the override path GI3(c) asks about and read it correctly enough to withdraw an escalation -- which is the single most consequential call in the document, and it is right for a reason stronger than the one it gives. It noticed that "today's masses" is ambiguous and that `None` is a different run, which is the distinction the zero-change test lives or dies on. It read GI3(e) wider than GI wrote it and said why, on the half-an-item rule, rather than doing the literal minimum. And it declared two of its five tolerance rows as **not** tolerances with the reasoning attached, which is the step at which a tolerance usually ships without a counter.
