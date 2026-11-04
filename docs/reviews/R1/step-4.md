# Review — R1 step 4
Reviewed commit: 66c7331402512e674d0f65bc4059c8b4aa415cde
**Reviewed commit: `66c7331402512e674d0f65bc4059c8b4aa415cde`.**
Verdict: PASS
Tests: **6986 passed, 8 failed, 0 skipped** -- MY OWN RUN AT THE JUDGED COMMIT, in clean worktrees of my own (FV2), taken in EI0's TWO HALVES: the main half `3955 passed, 0 failed, 0 skipped in 2810.50s (0:46:50)`, and the three report-parametrised files `8 failed, 3031 passed in 562.56s (0:09:22)`. Total collected 6994. **The main half is 3955 passed, 0 failed -- identical to your section 11 figure at `8800696`, measured by me at `66c7331`**, so every red in this tree is inside the three files that read this report and NOWHERE ELSE. **ALL EIGHT ARE EG3 STATE (1) -- report written, verdict not yet -- and I ruled each by the FS1/FT1 predicate per id, not by family; the list and the trace are in the CI section below.** The lint gate at CI's own scope is green at this commit: `ruff` `All checks passed!`, `black --check` `162 files would be left unchanged.`, `mypy` `Success: no issues found in 45 source files`, and FV1's four root guards `221 passed`.
Note on the halves, because it is a measurement about the measurement: **my first attempt at the COMBINED run blocked** -- 824 s of CPU and then frozen, no child process, 49 threads, zero CPU movement over 20 s -- and I killed it and re-ran serially rather than reporting a partial. The cause was my own parallel git work against a `.git` that lives on OneDrive. That is the same trap your section 11 reports falling into from the other side, and it is why EI0 exists.
Scope: **NOT A REVIEWED REVISION UNDER ES0, AND NOT AN INTERIM CHECK EITHER. I rule under GB2 verbatim -- "It returns for review at no step's cost" (`docs/directives/GB.md:26`) -- and NOT under EQ0, which the report cites and which governs a CLOSURE commit. All three of step 4's ES0 revisions remain available after this verdict.** See R1150: the outcome the report asks for is right and its authority is the directive, not EQ0.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1"). **NOTHING BLOCKS.** Verdict 47's one blocking item, R1139, is ANSWERED -- measured by me, two independent ways, in both EH4 directions -- and I withdraw one clause of my predecessor's own closing condition as the wrong test. Four findings are ledger rows and one is a closure item; for each I say why no silently wrong result follows, because FR1 requires that sentence rather than a classification.

**WHERE I WORKED (FV2).** Three worktrees of my own outside the repository, all detached at `66c7331`: one for the whole suite, one for the guard runs, one for the arms and the lint gate. **No `checkout`, `reset` or write of any kind in your tree** -- `git status --porcelain` there is empty and `git rev-parse HEAD` is `66c7331`, checked at the end. Every arm was restored inside my own worktree with `git checkout --` and `git status --porcelain` was empty afterwards, checked each time. One disclosure: I wrote my corpus file into the suite worktree by mistake while its run was at 5%, and moved it out within a minute. It cannot have perturbed anything -- **no test in this repository globs `tests/corpus/`; every consumer names its file as a module constant** -- and I checked that rather than assuming it.

**STEP 1b: THE `Answers:` HEADER NAMES THE NEWEST VERDICT.**

```
cmd    git log --oneline -1 -- docs/reviews/
out    779e79a review: R1 step 3 revision 3 at 6fb64c6 -- PASS, the step CLOSES,
         one blocking item carries
cmd    grep -n "^Answers: verdict" docs/reports/R1/step-4.md
out    5:Answers: verdict 47 @ 779e79a      -- the newest revision's, and the only one
judge  one comparison, not a diff. No HOLD on that head.
```

**THE MANDATED SEPARATE DIFFS, over `779e79a..HEAD` -- EIGHT commits. That is wider than the `efd2722..66c7331` range the invocation names, and I used the wider one, because `a156173`, `218730a` and `628f134` are also unjudged.**

```
cmd    git log --oneline 779e79a..HEAD | wc -l
out    8
cmd    git diff 779e79a..HEAD -- floatfea/tolerances.py | wc -l
out    0          -- the file is not in the diff at all
cmd    git diff --stat 779e79a..HEAD -- floatfea
out    (empty)    -- NO production code moved in this range
cmd    git diff 779e79a..HEAD -- tests/conftest.py 'tests/**/conftest.py' | wc -l
out    0          -- no new or changed conftest, no new plugin, so the CH2/CI0
                      forgery channels are not opened
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py    -- the pathspec RESOLVES, as my instructions say it must.
                               Not an empty result.
cmd    git diff --stat 779e79a..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)    -- my own instructions are untouched; no STOP-class finding
cmd    git diff --stat 779e79a..HEAD -- tests/corpus
out    (empty)    -- the adversarial cases are untouched by you
cmd    git diff --stat 779e79a..HEAD   (the whole range)
out    docs/digests/2026-11-03.md 170+ / docs/directives/FZ.md 177+ /
       docs/directives/GB.md 61+ / docs/directives/README.md 7 /
       docs/milestones/R1.md 17 / docs/reports/R1/step-4-answers.json 1221+ /
       docs/reports/R1/step-4.md 3369+ / scripts/carried_table.py 8 /
       tests/test_report_carried.py 52
       -- the only executable change is the site pattern in two files
```

**THE LINT GATE AND THE FOUR ROOT GUARDS AT THE JUDGED COMMIT, mine, in a clean worktree.**

```
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests scripts
out    162 files would be left unchanged.
cmd    python -m mypy floatfea
out    Success: no issues found in 45 source files
cmd    python -m pytest -q tests/test_no_tolerance_literals.py
         tests/test_tree_prose_consistent.py tests/test_collected_set_golden.py
         tests/test_one_gravity.py
out    221 passed in 35.67s
rule   FV1's four root guards, and CZ0 (d) -- a lint red is not a test red but it is
       the class CZ1 (ii) exists for, and it is green here
```

## Carried

Every open item from verdict 47 with its status. **Not "checked, nothing carried" -- there was one blocking item and it is answered.**

| item | status | where, measured by me |
|---|---|---|
| **R1139** (the site pattern cannot match a stemless dotfile at all; section 8b published 2167 rows under a universal heading over a set of 2170) -- **verdict 47's ONLY blocking finding** | **ANSWERED. Measured two independent ways, both EH4 directions run by me rather than read. ONE CLAUSE OF MY PREDECESSOR'S CONDITION IS WITHDRAWN AS THE WRONG TEST -- see the note under this table. The residual is R1147 and it does not block.** | `tests/test_report_carried.py:281-307`, `scripts/carried_table.py:119-125`. **(1) My own re-implementation** of `_sites_by_finding()` against the OLD and NEW patterns over the judged verdict file: `2255 -> 2261`, **gained 6, LOST 0**. **(2) The real gate's own collection, one variable moved** -- `_SITE` reverted to the pre-repair literal in a worktree of mine, nothing else touched, restored, `git status --porcelain` empty: `--collect-only` gives **2255** with **0** dotfile cases, HEAD gives **2261** with **6**, by id `[R959-.gitattributes]`, `[R967-.gitattributes]`, `[R975-.gitattributes]`, `[R1139-.gitattributes]`, `[R1139-.gitignore]`, `[R1139-.gitkeep]`. **All three ids my condition named are collected.** **The gate is GREEN AND COMPLETE:** `test_every_named_site_is_touched_or_declared` is `2261 passed`; section 8b publishes **2226** and says `2226`; `2226 untouched + 35 touched = 2261`, computed from the generator's own `state_of()`. **So the heading is true over the complete set**, which is the part verdicts 46 and 47 both refused to let stand. **The two copies agree character-for-character** in the shared body. **Nothing was lost, and it is impossible by construction** -- branch 1's final component must end `.ext`, so a base with a leading dot and no second dot could never have matched it, which is why the narrowing cannot take a pre-existing site. |
| **R1139, continued: the narrowing's COST, measured rather than stated** | **the docstring's two claims are both TRUE by measurement** | `tests/verification/rung7/.empty-by-design` and `a/b/.newdotfile` MATCH the pattern and are **not** sites, so a closing condition asking either to be CREATED collects no case and reads as answered -- that is R518's forbidden direction, and GB2 accepts it as documented. `tests/verification/rung1/test_new_thing.py` **is** still a site before it exists, so the extension form kept R518. **And the gate carries its own failure on the new rows:** all 8 `no change` literals for `.gitattributes` broken, one variable -> `4 failed` naming all four ids; the `.gitignore` literal alone broken -> `1 failed` naming `[R1139-.gitignore]`; tree restored both times. |
| **R1140** (five planted heading forms invisible to all six anchors; 14 live heading-shaped lines outside every anchor) -- R1 ledger | **correctly carried, untouched, and I did not reopen it** | listed at `docs/reports/R1/step-4.md:685`. `git diff 779e79a..HEAD -- scripts/check_carried.py scripts/answered_table.py` is empty. |
| **R1144** (the declaration lookup is keyed on the PATH, not on the finding) -- R1 ledger | **carried, and I QUANTIFIED it instead of relaying it, because this repair creates four more instances** | listed at `:685`. At the judged commit: **1141 of 2261 rows -- 50.5% -- sit on a `(path, line)` site that more than one finding names**; 311 such sites of 1431 distinct. The repair's `.gitattributes` site is one, named by **four** findings, and my arm shows the consequence: breaking R959's declaration alone leaves `[R959-.gitattributes]` **GREEN**, because R967's, R975's and R1139's rows still carry the literal. Only breaking all four reddens all four. **Not new and not yours to fix** -- the only repairs are new apparatus, forbidden through F6 -- but the number is on the record now instead of the word "one". |
| **R1141** (R1135 recorded CLOSED in three places and never closed) -- closure item, GB3 routed it here | **ANSWERED in section 3, and I verified the route rather than the words** | `grep -rn 'the wider pattern takes no text that is not an id' docs/ tests/ scripts/` gives exactly one report site, `docs/reports/R1/step-3.md:8914`, two quotations in the verdict file (`:244`, `:947`), and section 3's three new occurrences. EK3 does forbid the edit at its own site; GB3's route is the step-4 report, which section 3 is. **No id-shaped predicate was added to the reader** -- `git diff 779e79a..HEAD -- scripts/ci_section.py` is empty -- which is SR-24's ruling and I endorse it again. |
| **R1142, R1143, R1145, R1146** -- closure items | **correctly carried as a list, not re-reviewed item by item (CZ0)** | all four at `:685`. |
| **R1122, R1123** | **carried unchanged; R1123 bought three more rows and you reported them** | section 7, `:705-712`. Consistent with the seven rows already recorded, and you used the editing tool rather than reshaping anything (FM1). |
| **R1109-R1116 and the `L` ids** | **carried, and YOUR OWN CORRECTION IS RIGHT -- I reproduced it** | the grep over the verdict file gives `L47 L48 L49 L50 L51 L52 L53 L54 L55 L56 L57 L58 L59 L60` -- **FOURTEEN**, not the eleven every prior report and digest in this step carried. section 7's figure is the grep's. |
| **section 7's own derived count** | **reproduced exactly** | `297` of `299` non-`answered` entries in `docs/reports/R1/step-4-answers.json`, and the two `answered` ids are exactly `R1139` and `R1141` -- what GB2 and GB3 asked for, and nothing else. |
| **CZ1 (ii) and (iii), the four outputs** | **verdict 47 ruled them OWED AT THE CLOSURE COMMIT, which still does not exist. Unchanged. section 5's extra measurement is above and beyond and I spot-checked it.** | run `41678716379` at `628f134` is `completed/success`, and its lint job's steps `actionlint`/`ruff`/`black`/`mypy`/`unit tests`/`guards and meta-tests` are all `success` -- the guards step RAN, which is what CZ1 (iii) exists to see. Not a finding against the work. |
| **verdict 47 item 10(a)** -- the moment `docs/closure/R1.md` exists it MUST carry the `<!-- cz1-closure-outputs -->` block, or `cz1_record()` returns `""` and the report guards fail with no fallback | **STILL LIVE, and still correctly not acted on** | `ls docs/closure/` has no `R1.md`. Relayed unchanged; it is the one thing a closure commit can get wrong that no run before it can see. |
| **R835** (EG3's enumeration) | **still open, still Xabier's, and this is its NINTH measurement -- from a new direction** | a **THIRD** id reaches FT1's limb two this round, `test_the_guard_reads_the_step_being_worked_on`, where FT1's own figure was two. That is R861 arriving again: the baseline is a function of what the reviewer writes. Relayed with the measurement, not as a round. |
| **R845-R856, R857-R1137, R1, R836, R838, R843, R847, R848, R849** and the rest | **carry to the closure artifact as a list**, not re-reviewed item by item (CZ0) | section 7 names all 297 individually rather than as a family, which is what EG3 (i) asks for. This row is the pointer, not the list. |
| **the EG4(e) corpus pause** | **IT HAS EXPIRED, and three consecutive verdicts -- my predecessor's among them -- recorded it as holding. This is R1149 and it is MINE, not yours.** | `CLAUDE.md:551` reads "Corpus batches pause until **28 October**"; it is **3 November**. I ran a batch. |
| **EG3 (ii): the verdict commit measured** | **state (1) is the live state, and EG3 says I measure state (1) clearing at MY verdict commit. The number is in the Next-step section.** | not a finding against the work. |

**THE CLAUSE I WITHDRAW, said plainly, because withdrawing my predecessor's own condition needs saying.** R1139's closing condition (i) asked for "the count moving by **EXACTLY three** with no token that is not a site entering", and for "section 8b's row count moving to **2170**". Both numbers are functions of *which verdict is newest*, and verdict 47 wrote them while verdict 46 still was -- the same BP0 mechanism your section 2 correctly identified for `.gitattributes`, and verdict 47's own R861 note already said a reviewer's baseline "is a function of what the reviewer writes". **So "exactly three" and "2170" are WITHDRAWN as the wrong test.** What I put in their place is what I measured: **every token the branch gains is a tracked file, nothing is lost, and section 8b's heading is true over the complete set.** All three hold. **R1139 is answered.** That the report's own account of the delta is short by two is a separate, non-blocking finding (R1147) and not a reason to keep the item open.

## Findings

**NOTHING BLOCKS, and FR1 asks me to say why for each rather than classify.** No production code moved, no tolerance moved, no deliverable moved, the lint gate and the four root guards are green, the site gate is `2261 passed`, and the one red at HEAD is EG3 state (1) by its own assertion message. **The carried blocking item is answered at the layer it was about.** The four findings below are the weakening directions I could still reach; none of them can put a wrong number in front of anyone, and I give the sentence for each.

### R1147 (DOES NOT BLOCK -- R1 ledger; FR1's SECOND and THIRD classes, and CLAUDE.md's own worked example of a non-blocking finding). The repair's published delta is **SIX rows over THREE paths**, not the four rows over one path that section 2, section 4, SR-25 and the digest all state. `.gitignore` and `.gitkeep` are gained too, both tracked, and **both are named inside the very verdict block the repair answers.** The EH4 claim "Only `.gitattributes` is GAINED" is false, and the table's `.gitkeep` row tests the SEPARATOR form -- the one that is refused -- and not the bare form, which is the one admitted.

```
claim  the delta, measured by the real gate with ONE VARIABLE moved and nothing else
cell   `_SITE` reverted to the pre-repair literal in a worktree of my own at the
       judged commit, `scripts/carried_table.py` left alone, `--collect-only` on
       the gate's own parametrised test; restored with `git checkout --` and
       `git status --porcelain` empty afterwards
out    OLD   2255 collected, 0 stemless-dotfile cases
       NEW   2261 collected, 6 stemless-dotfile cases
       delta +6, lost 0
cmd    the six, by collected id
out    test_every_named_site_is_touched_or_declared[R959-.gitattributes]
       test_every_named_site_is_touched_or_declared[R967-.gitattributes]
       test_every_named_site_is_touched_or_declared[R975-.gitattributes]
       test_every_named_site_is_touched_or_declared[R1139-.gitattributes]
       test_every_named_site_is_touched_or_declared[R1139-.gitignore]
       test_every_named_site_is_touched_or_declared[R1139-.gitkeep]
cmd    where the two unlisted paths come from -- they are not hypothetical
out    docs/reviews/R1/step-3.md:325  **`.gitignore` the PATH appears 0 times: the
       docs/reviews/R1/step-3.md:328  `.gitkeep` 0, `.flr` 0, `empty-by-design` 0.
       -- inside R1139's OWN BLOCK. Verdict 47 wrote `.gitignore` in the sentence
          asserting it appears zero times, and by writing it made it appear once.
cmd    both tracked, so sites by the gate's own rule
out    .gitignore -> .gitignore, artifacts/.gitignore      tracked
       .gitkeep   -> docs/closure/.gitkeep                 tracked
cmd    the CLASS the branch admits, over the whole repository rather than over the
       one path -- `git ls-files` filtered to stemless-dotfile basenames
out    .gitattributes  .gitignore  artifacts/.gitignore  docs/closure/.gitkeep
       tests/verification/rung6/.empty-by-design
       -- FOUR distinct basenames. `.empty-by-design` is the fourth and it is not a
          row only because the newest verdict writes it WITHOUT its leading dot.
rule   BP0, which section 2 invokes correctly and then applies to one of three paths; and
       EH4 -- the boundary is solved from the side that weakens the claim too
judge  **THE SILENTLY WRONG RESULT FR1 ASKS FOR DOES NOT EXIST, and that is why this
       is a ledger row and not a block.** I checked the three places it could have
       been and each is clean: (i) the GENERATED section 8b publishes 2226 rows and says
       `2226`, and `2226 + 35 touched = 2261` from the generator's own `state_of()`,
       so the heading is true over the COMPLETE set; (ii) all six rows are declared
       -- `test_every_named_site_is_touched_or_declared` is `2261 passed`, so no
       closing condition naming any of the three paths can read as answered; (iii)
       the gate's collected set CONTAINS the fault, which is the exact half that was
       missing in R1139 and the reason verdict 47 blocked it. So this lands in FR1's
       second class -- a census too narrow where no wrong result follows -- and it is
       verbatim the example CLAUDE.md gives for the third: "a figure pasted from a
       verdict without re-measurement (`three of five siblings` where five of five
       are)". **Ruling it a block would be ruling on the count rather than the kind,
       which is the thing verdict 47 said it would not do.**
       **What it IS, and the reason I am spending a finding on it rather than a
       line:** this is the species that has produced every blocking finding in this
       milestone, one more time. section 2's probe is section 4's probe -- filtered to
       `.gitattributes`, correctly for section 4, which is scoped to "the complete set of
       `.gitattributes` cases" and is TRUE -- reused for a claim about the whole
       delta, which is not. The sweep was over the axis its author chose, and the two
       shapes it misses are written in the block being answered. You found the
       self-reference mechanism (`SITES` is derived from the newest verdict) and
       applied it to one of the three paths it applies to.
```

**Closed when** these SEVEN live sites say six rows over three paths, site by site: `docs/reports/R1/step-4.md:121`, `:136`, `:141`, `:233`; `docs/directives/FZ.md:576`; `docs/digests/2026-11-03.md:287`, `:293`. **And the EH4 table carries the BARE `.gitignore` and `.gitkeep` rows** -- it currently tests `foo/.gitkeep`, which the narrowing refuses, and never the bare form, which it admits. `tests/corpus/site_pattern_path_forms.txt` is the measured set; 26 of 26 entries rule as required at this commit.

### R1148 (DOES NOT BLOCK -- R1 ledger; FR1's second class). **The SECOND copy of the pattern is the configuration nobody ran, and the new branch widened it by 1031 tokens.** `scripts/carried_table.py`'s `SITE` has no `(?<![\w.-])` lookbehind, so with the stemless alternative it now matches the decimal tail of every number in the verdict file. The comment the repair adds says this copy carries "the same" decision as `_SITE`; the bodies are character-identical and **the decisions now differ on 1031 tokens.** Its only consumer, `check_sites()`, has had an EMPTY parameter set for all four steps of R1.

```
claim  the two copies agree on TEXT and disagree on BEHAVIOUR, and the new branch is
       what made the gap large
cmd    the shared body compared character for character
out    test_body.replace(lookbehind).replace(line-suffix) == table_body   ->  True
cmd    the same five hostile tokens through BOTH copies
out    token                 _SITE                     carried_table.SITE
       x.gitattributes       []                        ['.gitattributes']
       foo.gitignore         []                        ['.gitignore']
       a_b.gitkeep           []                        ['.gitkeep']
       1.gitignore           []                        ['.gitignore']
       R1139-.gitattributes  [('.gitattributes',..)]   ['.gitattributes']
cell   the OLD and NEW `carried_table.SITE` over the judged verdict file, one
       variable -- the stemless alternative -- and nothing else
out    OLD 311 distinct tokens   NEW 1342   GAINED 1031   LOST 0
cmd    what the 1031 are
out    .0  .00  .000  .0000  .000000000000000  .0000000000000004  .0002  .0005  ...
       -- the fractional part of every decimal number in the file. `\.[\w-]+(?![\w-])`
          with no lookbehind matches inside `1.0000x` at the dot.
cmd    whether anything observes it
out    scripts/carried_table.py:343 is the only call site, inside main(); no test
       calls check_sites. And the parameter set is empty at every step of R1:
         step-1-answers.json  0 of 3 entries declare a site
         step-2-answers.json  0 of 49
         step-3-answers.json  0 of 291
         step-4-answers.json  0 of 299
       check_sites(answered, blocks) -> []
rule   my own recorded guards -- "empty parameter set is an error, not a skip", and
       "a gate carries its own failure"; EH4, the direction that WEAKENS; and the
       repair's own comment, which is the claim being tested
judge  **no silently wrong result follows, so it is a ledger row.** `check_sites`
       only REPORTS, it is the explicitly weaker of two checks -- the file says so
       at :168-172, "a declared site is a second, weaker check" -- and its input has
       been empty for 642 entries across four steps, so the widening is unobservable
       and so would any future narrowing be. Nothing is published from it and no
       number moves. **Both halves are pre-existing in kind and this commit made one
       of them bigger:** the vacuity is not yours, the 1031 is. It is worth a finding
       because the comment asserts the copies cannot drift again, and the first thing
       I did to the second copy -- run it, which the report's EH4 table does not --
       found that they already disagree, on more tokens than the whole pattern
       matched before.
```

**Closed when** either the two copies are made to agree on the DECISION as well as the text -- the lookbehind carried across, a one-token edit and not new apparatus -- or the comment at `scripts/carried_table.py:119-121` says the copies share the alternation and NOT the anchoring, with `check_sites()`'s empty domain recorded beside it. **Do not add a guard for it**; `CLAUDE.md` forbids new apparatus through F6 and `docs/milestones/F2a.md` is where it goes.

### R1149 (DOES NOT BLOCK -- and it is MINE, not yours). **The corpus pause EG4(e) names expired on 28 October, and three consecutive verdicts including my predecessor's recorded it as holding.** I read the clause rather than the habit, and ran a batch.

```
claim  the clause is dated and the date has passed
cmd    grep -n "Corpus batches pause until" CLAUDE.md
out    551:### Corpus batches pause until 28 October (EG4(e))
cmd    today, and whether any directive extends it
out    3 November 2026. `grep -rn "corpus" docs/directives/*.md` is EMPTY -- no
       directive mentions the corpus at all, so nothing extends the pause.
       `docs/directives/FR.md:52` moves a MILESTONE date from 28 October to
       5 November, which is a different date about a different thing.
cmd    what the last three verdicts recorded
out    "The pause held. Zero new entries." -- verdict 47, and the two before it
rule   my own instructions: add unseen entries at every review EXCEPT WHILE BATCHES
       ARE PAUSED, reading the clause rather than a copy of it
judge  **a dated pause read as indefinite is a rule that quietly outlived its own
       text.** No wrong number follows from it; what follows is that the one
       measurement my instructions call the coverage measurement was not taken for
       three rounds. It is Xabier's to close -- either the pause is extended in
       writing or it is over -- it is not the implementer's, and it is not a round.
       I acted on the text: `tests/corpus/site_pattern_path_forms.txt`, 26 entries,
       committed separately from this verdict.
```

### R1150 (DOES NOT BLOCK -- R1 ledger; FR1's second class). **section 1 and section 5 cite EQ0 and EB4 as the authority for "no step's cost". EQ0 governs a CLOSURE COMMIT, and this is a step's FIRST commit.** The outcome is right; the authority is GB2's own sentence, and that is what I ruled under.

```
claim  EQ0's subject is a closure commit, and this commit is not one
cmd    the clause, read rather than cited
out    CLAUDE.md -- "A closure commit that changes a gate or a tolerance is
       reviewed; one that changes only prose is not." And EB4's own reason: "It
       judges a commit written after the last reviewed round, so it is not
       implementer work done for the next step."
cmd    what this commit is
out    the `step-under-execution` marker moved to `4` in `489bad7`, and the report
       carries `# Revision 1`. EB4's reason is therefore FALSE of it -- this IS
       implementer work done for step 4.
cmd    the authority that does cover it, verbatim
out    docs/directives/GB.md:23-26 -- "GB2 -- Step 4's first commit, as you
       proposed: ... It returns for review at no step's cost."
rule   "Where this file and CLAUDE.md disagree, CLAUDE.md governs -- until a
       directive changes it." GB2 is that directive, recorded verbatim under FP0
       before it was acted on, which is what FP0 exists to make possible.
judge  **the disposition is right and the citation is not, and it matters for one
       reason.** If EQ0 were the authority, every step's first commit that touches a
       gate would be free of ES0's cap -- which is DK0's recorded concern word for
       word: "if reopening the plan bought three more rounds, every reopen would buy
       them and the cap would mean nothing." A directive naming ONE commit cannot be
       generalised by a clause about a different kind of commit. **No wrong number
       follows and nothing is published from it**, so it is a ledger row -- but the
       next step's first commit does not inherit this, and the report should not read
       as though it does.
```

**THERE IS A THIRD SITE and I found it after writing the finding: the `_` block of `docs/reports/R1/step-4-answers.json` carries the same two sentences** -- "It changes a gate, so EQ0 makes it reviewed and EB4 charges it to no step's rounds." *The rest of that block is right and I checked it: 2 answered, the count derived from the list rather than typed, 297 ledger rows pointing at section 7 -- so R1133's defect is not repeated.*

**Closed when** section 1, section 5 and the answers file's `_` block cite `docs/directives/GB.md:26` as the authority and say EQ0 is cited by analogy rather than as the governing clause -- or Xabier rules that EQ0 extends to a step's first commit, which is a `plan:` commit and not a report edit.

## Closure items (CZ0: listed, fixed once in the closure commit, not re-reviewed item by item)

**R1151.** `tests/test_report_carried.py:280` ends `...and stays out.#` -- a stray `#` appended where the new comment block begins. `ruff` and `black` are both green on it because it is inside a comment, and nothing else in the tree reads it. Pure formatting; FR1's third class. **Closed when** the line ends at the full stop.

**R1152.** `docs/directives/README.md` lists `GB.md` TWICE -- appended to the verbatim roll and again as its own bullet immediately below. Both statements are true and one is redundant. **Closed when** the roll lists it once. *The substance of that bullet is right and I want it recorded separately: GA is cited by GB and exists in no file, you did NOT reconstruct it, and the README says the record is missing instead of inventing wording. That is the correct handling of C25 and it is the second chance this project has had to get it wrong.*

**R1153.** section 4's bold line says "The repair makes four new parametrised cases exist". The section is scoped to `.gitattributes` and its own `claim` field is correctly scoped; the bold line is not. Same cause as R1147, closes with it. **Closed when** the line says six cases over three paths, or states the section's scope as the claim field does.

**R1154.** EG3 (i) asks for the `FAILED` list pasted **and the sentence saying which of the two states it is.** section 10 and section 11 paste both lists and section 10 gives the reason in substance -- "no step-4 verdict can exist before step 4's report is pushed" -- but neither names the state. `grep -n "state (1)\|state (2)" docs/reports/R1/step-4.md` is **0**. The substance is right and more precise than the label would be, so nothing follows from it; the clause names the sentence explicitly and it costs one line. **Closed when** one sentence says this is EG3 state (1), report written and verdict not yet.

## Tolerances touched

**None.** No value, no form, no counter, no injection, and **EU1 does not attach** -- no tolerance value and no declared counter moved, so the adversarial-case requirement EU1 adds is not triggered. I ran adversarial configurations anyway, because R694's lesson is that a value which does not move is the worst case and not the safest, and the configuration nobody chose is where R1148 came from.

```
cmd    git diff 779e79a..HEAD -- floatfea/tolerances.py | wc -l
out    0                -- the file is not in the diff at all
cmd    git diff 779e79a..HEAD -- floatfea tests scripts | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance"
out    (no match)
cmd    the same widened to any numeric literal the diff adds to executable code
out    (no match) -- the only executable lines added are two regex alternatives and
       four lines of `_is_a_site`; the rest is comment and docstring
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a
       tolerance under another name -- a convergence threshold, a comparison epsilon,
       a "small number" guard, a tier cutoff
judge  nothing moves. The one thing in this diff that could have been a threshold and
       is not: `_is_a_site`'s stemless test is `base.startswith(".") and "." not in
       base[1:]`, a structural predicate with no number in it.
```

## Try to break it -- what I ran, and what it found

**The case this step should fail is "a closing condition naming a stemless dotfile reads as answered", and I built it in both directions.**

* **The real gate's collection with the regex reverted, one variable, restored afterwards.** `2255 -> 2261`, gained 6, lost 0, the six listed by collected id. **This is the measurement the report's own probe could not take**, because its probe was filtered to `.gitattributes`. It is where R1147 came from.
* **The gate ARMED on the new rows, twice.** All eight `no change` literals for `.gitattributes` broken -> `4 failed` naming all four ids. The `.gitignore` literal alone broken -> `1 failed` naming `[R1139-.gitignore]`. And the control that matters: **R959's declaration alone broken leaves its own case GREEN**, because three sibling findings name the same path -- which is R1144, quantified at 1141 of 2261 rows.
* **A continuum census over the path-FORM axis, over the WHOLE verdict corpus rather than the one file.** All 17 verdict files, every token the new branch matches: **115 distinct stemless-dotfile shapes**, of which `_is_a_site` admits **4** and refuses 111. The refused 111 are Python attribute accesses (`.conclusion`, `.startswith`, `.databaseId`), format specs (`.0f`, `.6g`), bare extension words (`.py`, `.md`) and decimal tails. **Seven are separator-bearing and every one is noise** -- `./.git`, `wt/.git`, `.../clone/.git`, `.../sweep/.git`, `a/.gitattributes`, `foo/.gitkeep`, `tests/verification/rung5/.empty-by-design`. So the narrowing is load-bearing against SEVEN shapes, not the one the report names, and that is a stronger result than the report claims.
* **The narrowing's cost, measured instead of stated.** `tests/verification/rung7/.empty-by-design` and `a/b/.newdotfile` match and are not sites; `tests/verification/rung1/test_new_thing.py` still is. Both halves of the docstring hold.
* **The SECOND copy, which the report's EH4 table never runs.** That is R1148: `carried_table.SITE` gains 1031 tokens the gate cannot see, and its only consumer has had an empty parameter set for 642 entries across four steps.
* **The nine CI reds at the nearest executed run, one id at a time and not by family.** Every inner `FAILED` line in all seven cascading states, extracted from the log rather than inferred from the state's name: **15 occurrences of `test_the_report_carries_a_WHOLE_SUITE_count` and 15 of `test_the_guard_reads_the_step_being_worked_on`, and nothing else.** Seven states x 2 + 1 top-level each = exactly 15. No third id appears anywhere in the log.
* **A corpus batch on the same axis, 26 entries, 0 misses** -- including the four tracked stemless dotfile basenames the repository actually has, where the report's table carries one.

**What I did not find, and it is the larger part.** The repair is the right repair and it is better than its own account of it. It is a parser repair under EK2 -- an alternative added to an existing pattern, no new regex object, no guard extended, no apparatus added -- and it is applied to BOTH copies in the same commit, which is the drift R1128 was found by. `_is_a_site`'s narrowing is minimal, structural, carries no number, and is justified against seven live noise shapes rather than the one that was reported. Nothing was lost, and I established that it is impossible to lose anything rather than merely observing that nothing was. section 8b's heading is now true over the complete set, which is the whole of what verdicts 46 and 47 refused to let stand. **And the two things you corrected against yourself are the two that matter most:** the `L` count was eleven in every prior report and digest and is fourteen, and you re-ran section 10's pass count after the edit that changed it rather than carrying `3029` forward -- which is CP3 being applied, not cited.

## Corpus (EG4(e))

**THE PAUSE HAS EXPIRED AND I RAN A BATCH. That is a change from the last three verdicts and R1149 is the reason.** `CLAUDE.md:551` reads "Corpus batches pause until **28 October**"; it is 3 November; `grep -rn "corpus" docs/directives/*.md` is empty, so no directive extends it. I read the clause rather than the habit.

**`tests/corpus/site_pattern_path_forms.txt` -- 26 entries, ALL NEW, committed separately from this verdict.** The coverage measurement my instructions ask for: **26 of 26 rule as the entry requires at `66c7331`, 0 misses.** That is the best number any batch has returned in this milestone, and I want the reason on the record rather than the number: **it is clean because the repair is structurally right, and the defect this round is in the RECORD of the repair, which no corpus can see.** A corpus measures a decision rule against shapes its author did not choose; it cannot measure whether the sentence describing the rule is true. R1147 came from the arm, not from the batch.

**Two entries whose outcome is right for a reason worth naming, so a later reader does not take them as clean.** `dotfile_trailing_slash_path`: `.gitignore/foo` is TRUNCATED to `.gitignore` and admitted because that truncation happens to be a tracked file, not because the token names it. `dotfile_capitalised`: `.GITATTRIBUTES` is refused only by case -- the tracked-path check is case-sensitive, so a verdict that writes the name in capitals loses the site silently. Both are in the file's header.

**I also ran the recorded substitute, both halves, and both paid:**

* **A continuum grid over the parameter space a decision rule guards** -- the path-FORM axis over all 17 verdict files, 115 distinct shapes, and then the second copy of the same rule. That produced **R1147** and **R1148**.
* **A regeneration check on a published artifact** -- section 8b against the generator's own `state_of()` over `SITES`: `2226 + 35 = 2261`, so the published row count is the generator's at this commit and the heading is true. That one came back CLEAN, and I record the clean result because a swept axis with nothing on it is the sentence R755 was about.

## CI: UNAVAILABLE at the judged commit, by CK0's design, and I record it as that rather than as a pass

**`gh run list --commit 66c7331402512e674d0f65bc4059c8b4aa415cde` is `[]` -- with the FULL sha, not the short one.** The commit is pushed; GitHub created no run, because its whole diff is `docs/reports/**` and the workflow path-ignores that. **This is not CK2's exhausted-allowance state** -- there is no unstarted job, no empty `runner_name`, no spending annotation; there is no run at all.

```
cmd    git show --stat --format='' HEAD
out    docs/reports/R1/step-4.md | 111   -- ONE file
cmd    grep -n -A 2 'paths-ignore' .github/workflows/ci.yml
out    24:    paths-ignore:
       25-      - "docs/reports/**"
cmd    every commit in the range, full sha, with its run
out    628f134  41678716379  completed/success
       a156173  (no run -- pushed with 218730a; GitHub builds the push tip)
       218730a  41769148306  completed/cancelled   (concurrency group)
       efd2722  41769547062  completed/cancelled   (concurrency group)
       489bad7  41776482587  completed/cancelled   (concurrency group)
       8800696  41776618449  completed/FAILURE
       3e008d7  (no run -- path-ignored)
       66c7331  (no run -- path-ignored)
rule   CK2's shape applied to CK0's cause: name the last run that EXECUTED and check
       whether the code has moved since
cmd    git diff --stat 8800696..66c7331 -- floatfea tests scripts .github
         tests/verification
out    (empty)  -- NO code moved between the last executed run and the judged commit,
                   so run 41776618449's result still describes the tree under review
```

**That run concluded `failure` with NINE reds, and the waiver applies -- but only because I checked the predicate per id, which is the one thing a list cannot do.**

```
cmd    gh run view 41776618449 --json jobs, at STEP level
out    the verification ladder : SUCCESS
         ladder 1 / ladder 2 / ladder 3 / ladder 6 / ladder 4 / ladder 5, all success
       lint, unit and guards  : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS / guards and meta-tests FAILURE
       CI determinism -- leg / ten legs agree : SKIPPED (workflow_dispatch only)
       -- every step above the failing one RAN rather than being skipped behind it,
          which is what CZ1 (iii) exists to see
cmd    gh run view 41776618449 --log-failed | grep -oE "FAILED [^ ]+" | sort -u
out    the same nine as section 0a and section 10, id for id
cmd    EVERY `FAILED` id anywhere in the log, counted -- the inner lists of all seven
       cascading states read rather than inferred from their names (EG3 (i))
out    15  test_the_report_carries_a_WHOLE_SUITE_count
       15  test_the_guard_reads_the_step_being_worked_on
        1  test_the_guard_survives_the_state[baseline]
        1  ...[non_numeric_step_suffix]      1  ...[superscript_digit_step_number]
        1  ...[draft_suffix_beside_a_step_report]   1  ...[step_number_is_the_empty_string]
        1  ...[verdict_amended_after_the_commit_the_report_answers]
        1  ...[zero_padded_step_number]
       -- 7 states x 2 inner + 1 top-level each = 15 and 15 exactly. NO THIRD ID
          APPEARS ANYWHERE IN THE LOG, so the cascade is established by measurement
          and not by family, which is what R629 cost.
rule   FS1 with FT1, applied per id; CA2, which I keep in full because CLAUDE.md does
       not carry it; EG3 (i), the trace pasted
judge  **all nine are boundary reds and CZ1 (iv) is not reached.**
       `test_the_report_carries_a_WHOLE_SUITE_count` is FT1's limb two by name.
       **`test_the_guard_reads_the_step_being_worked_on` is a THIRD id reaching limb
       two, and I am ruling it there explicitly rather than quietly.** It names no
       finding and no site, so limb one does not reach it; its assertion is
       `STEP_REPORT == _PAIRED` and its own message is "step 4 has a report and no
       verdict yet ... Invoke the gating-supervisor" -- so its SUBJECT is whether the
       commit carrying it has a verdict for its own newest report, and **a commit
       cannot contain its own review.** That is limb two's reason exactly, and FS1/FT1
       say in terms that both limbs are reasons and not lists. It is also EG3 state
       (1)'s own definitional red: if the predicate excluded it, EG3 state (1) would
       be unreachable and every step's first verdict in this repository would block.
       FT1's figure was two ids; this is three. **That is R835/R861 again -- the
       baseline is a function of what the reviewer writes -- and it is relayed, not
       re-litigated.**
       And the ninth red CLOSED between that run and the judged commit, which I
       verified rather than accepted: `test_the_report_carries_a_WHOLE_SUITE_count` is
       GREEN in my own run at HEAD, because section 11 is what `3e008d7` adds, and CI could
       not see it because the commit that adds it is path-ignored.
```

### The EIGHT reds in MY OWN tree at `66c7331`, traced ONE ID AT A TIME (EG3 (i)), not by family

```
cmd    python -m pytest -q --tb=no -rf  tests/test_report_carried.py
         tests/test_report_numbers_are_sourced.py tests/test_report_guard_states.py
out    8 failed, 3031 passed in 562.56s (0:09:22)
       FAILED test_the_guard_reads_the_step_being_worked_on
       FAILED test_the_guard_survives_the_state[baseline]
       FAILED test_the_guard_survives_the_state[non_numeric_step_suffix]
       FAILED test_the_guard_survives_the_state[superscript_digit_step_number]
       FAILED test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]
       FAILED test_the_guard_survives_the_state[step_number_is_the_empty_string]
       FAILED test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
       FAILED test_the_guard_survives_the_state[zero_padded_step_number]
cmd    id 1's own assertion message, read rather than classified
out    AssertionError: step 4 has a report and no verdict yet. That is the legitimate
       boundary -- the verdict is written after the report is committed -- and until
       it lands this guard checks step 4, so step 4's carry list is UNCHECKED. Invoke
       the gating-supervisor.
       assert 4 == 3                   (tests/test_report_carried.py:577)
cmd    ids 2-8, EACH RUN SEPARATELY and its INNER FAILED list read from its own
       output rather than inferred from its name -- seven invocations, not one
out    baseline                                             1 failed, 2985 passed
       non_numeric_step_suffix                              1 failed, 2985 passed
       superscript_digit_step_number                        1 failed, 2985 passed
       draft_suffix_beside_a_step_report                    1 failed, 2985 passed
       step_number_is_the_empty_string                      1 failed, 2985 passed
       verdict_amended_after_the_commit_the_report_answers  1 failed, 2985 passed
       zero_padded_step_number                              1 failed, 2985 passed
       -- and in ALL SEVEN the single inner FAILED id is
          `test_the_report_carried.py::test_the_guard_reads_the_step_being_worked_on`.
          NO OTHER ID APPEARS IN ANY OF THE SEVEN.
cmd    the complement -- every other test in the repository
out    main half: 3955 passed, 0 failed, 0 skipped, `grep -c "^FAILED"` = 0
       -- so there is no red anywhere outside the three files that read this report
rule   FS1 with FT1, per id; EG3 (i), the trace pasted and each id matched
       individually, because the eighth member of a group ruled by class was R629
judge  **EIGHT reds, ONE cause, and the cause is measured rather than asserted.** At
       CI's run the cascade carried TWO inner ids; here it carries ONE, because
       `test_the_report_carries_a_WHOLE_SUITE_count` closed at `3e008d7`. That change
       in the inner list between two commits is itself the control: the cascade
       follows its cause and is not a fixed family. **All eight are EG3 state (1) and
       the waiver applies in full, so CZ0 (d) does not stand and CA2's HOLD is not
       reached.** The verdict commit this file lands in is what clears them.
```

**The tension with FP1 is real and the report states it instead of letting `[]` read as a pass, which is the right handling.** FP1 wants a CI run at the judged commit; CK0 guarantees there is none when the diff is a report. I am not making it a finding against the implementer -- it is two clauses of `CLAUDE.md` that cannot both hold for a report-only commit, the code is covered by the run at `8800696` with an empty diff between, and the honest record is "unavailable, with the last executed run named and its reach measured". That goes to Xabier with R835.

## Next step opens when

**STEP 4 IS NOT CLOSED BY THIS VERDICT AND NOTHING IS OPENED BY IT.** This is a PASS on a commit GB2 sent back for review at no step's cost, so it carries no `Closes:` line (FK1), and **all three of step 4's ES0 reviewed revisions remain available.** Step 4 stands at **0 of 3**. R1139 is answered and carries nothing forward; the five items below are a ledger and a closure list, and none of them holds the step.

1. **R1139 IS ANSWERED and does not carry.** I withdrew two numbers from my predecessor's own closing condition as the wrong test and substituted what I measured. The step's work -- `docs/USER_GUIDE.md`, which still does not exist, and the fresh-context witness -- is what step 4 is for, and none of it is in this commit, as section 1 says.
2. **R1147 is the one to read first.** Seven live sites across three files, named individually in its closing condition. It does not block and it is the species that has produced every blocking finding in this milestone: a sweep over the axis its author chose. **The two paths it misses are written inside the verdict block the repair answers.** If any part of this verdict is worth an hour, it is that sentence rather than the count.
3. **R1148 is the one I would most want measured before it matters.** The second copy of a decision that two commits in a row have been about. Its repair is a one-token edit and NOT new apparatus; its alternative is a correction to the comment that claims the copies cannot drift. `check_sites()`'s empty domain -- 0 of 3, 0 of 49, 0 of 291, 0 of 299 -- goes on the record either way.
4. **R1150 is a citation, not a disposition.** The outcome GB2 asks for is right and I granted it. What must not travel is the idea that EQ0 makes a step's first commit free whenever it touches a gate; that is DK0's concern verbatim and it would empty ES0's cap.
5. **R1151, R1152, R1153 are closure items** and are not re-reviewed item by item.
6. **R1149 and R835 are MINE and go to Xabier, not into a round.** R1149: the corpus pause's own date passed six days ago and three verdicts including mine carried it as live -- either it is extended in writing or it is over, and I have acted on the text. R835: FT1's limb-two figure was two ids and this round makes it three, for the same reason R861 withdrew its own baseline one commit after writing it. Neither is the implementer's to repair.
7. **The FP1/CK0 tension is recorded, not charged to you.** A report-only commit cannot have a CI run and FP1 asks for one. The code is covered: `git diff 8800696..66c7331 -- floatfea tests scripts .github tests/verification` is empty, so the last executed run describes the tree under review, and all nine of its reds trace by the predicate per id.
8. **EG3 (ii), which is mine to pay and I am paying it in this verdict.** State (1) is the live state: `test_the_guard_reads_the_step_being_worked_on` is red at `66c7331` because no step-4 verdict exists. The verdict commit this file lands in is what clears it. **I cannot paste the number into the file that causes it** -- that is CZ1's reusable half from my side of the loop -- so I run the two report-guard files AT my own verdict commit after it exists and hand the counts back with this verdict. If they do not clear, that is mine to answer and not yours.
9. **The schedule.** FW0's date is 10 November and it is 3 November, so seven days remain -- which reproduces: the date arithmetic is 7 and `grep -c 'FT2.7' docs/milestones/R1.md` is 14, both exactly as section 1 publishes them. Step 4 is estimated at one and a half to two days plus half a day of closures at `docs/milestones/R1.md:52`, and `docs/USER_GUIDE.md` is still ABSENT -- that file is the thing that is not built and it is the whole of step 4. **I read nothing here as slippage and nothing is escalated under FZ (e).** This commit spent itself on a one-line parser repair, its declaration rows and one routed correction, which is what GB2 asked for and nothing more.
10. **GB1 is withdrawn correctly and I checked it rather than taking it.** At `779e79a`, before any edit, `docs/milestones/R1.md` section 3 already read `Step 3 -- FL2, complete (FR3)` and `Step 4 -- guide and witness (FR4)`. The three `FLn -- STEP n` lines sit inside `## 1. The directive, verbatim`, and the quotation is **unfenced** -- 0 code fences precede line 99 -- so FL's bold renders identically to a plan step row, which is exactly how it was misread. GB1's authorised header edit had no target, and **you did not manufacture one**: `218730a` is `15 insertions, 0 deletions`, a standalone `plan:` commit touching only the plan, adding a supersession note above a verbatim quotation rather than rewriting it (FP0). **SR-28 left standing with the correction beneath it is the right disposition and the right convention.** SR-32's reasoning is also right and I verified its mechanism: `^# Revision \d+` is the anchor in `scripts/ci_section.py:211` AND `tests/test_report_carried.py:330`, so a different header would have broken the anchor rather than expressed the ruling. Keeping it is mechanically necessary and I endorse it.
11. **What this commit got right, and it is much the larger part.** The one blocking item was answered first, at the layer it was about, in both copies, in one commit, with the narrowing's cost documented in three places before anyone asked. The repair was chosen for the reason that matters -- a gate that cannot see a site in a published CSV's own attributes file is the EZ0 class CZ0 was amended to protect -- and it was the branch verdict 47 preferred without being told which. GB1 was reported as WRONG by the person who raised it, with the measurement that refutes it. GA was recorded as MISSING rather than reconstructed, which is C25 handled correctly at the second opportunity. Five of your own stale pastes were caught before push and recorded where they happened; the `L` count was corrected against three of your own prior documents; `3029` was re-run to `3031` after the edit that moved it. **And section 10 asks me to check the nine reds by the predicate rather than by your say-so, which is the request that makes the trace worth running** -- I ran it, all nine hold, and the third limb-two id is a finding against my own side of the loop rather than yours.
