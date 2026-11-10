# Review — R1 step 4 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 602bce8d84745a71bb80b36c52a735aaa97f3ad4
**Reviewed commit: `602bce8d84745a71bb80b36c52a735aaa97f3ad4`.**
Verdict: PASS
Scope: **the EQ0 review of the follow-on closure commit `602bce8`, recorded as an ES0 INTERIM CHECK because no new report revision exists.** The newest report revision is step 4 revision 4 at `dc49552`, which verdict 55 reviewed, so this counts against no round (ES0) -- and a review of a closure commit counts against no step's rounds in any case (EB4). **Step 4 stays CLOSED (DD1) and R1 stays CLOSED (GF2); this verdict reopens neither, and `--closes` is correctly absent (FK1).** Written with `--interim` (FS2). **Ruled under FR1 with EZ0** -- see `## Which criterion I ruled under`, where I say why FR1 rather than CZ0 and name the finding I would have blocked on under CZ0. **GE3: `R835: unchanged, R2`. Not re-measured.** EU1 does not arise -- no tolerance value and no declared counter moved -- and I ran adversarial configurations anyway. **GA3's 150-line target is OVERRUN and I say so rather than trimming the evidence**: the overrun is the independent recomputation of section 8 from verdict 55's own text, four injected states in worktrees of my own, two controlled cells on CI, a six-entry corpus batch with its coverage number, EH4 solved in both directions on the one gate in the window, and a measured answer to the hook question you raised for Xabier.
Tests: **4393 collected, 8 failed, 4385 passed, 0 skipped AT THE JUDGED COMMIT, MY OWN RUN, in a clean worktree of my own (FV2/GF3 a), `-p no:randomly`, PYTHONPATH unset: `8 failed, 4385 passed, 2 warnings in 2970.64s (0:49:30)`.** **THE EIGHT ARE THE ONLY REDS IN THE WHOLE SUITE, so CZ1 (iv) is not reached**, and I ruled all eight per id against the FS1/FT1 predicate myself rather than accepting your group -- see `## The eight, per id`. Your control reproduces exactly: the two report-guard files give **403 passed, 0 failed at `dc49552`** and **8 failed, 395 passed at `602bce8`**, same 403 collected, in worktrees of mine. **The partition closes, which is how I know the 4393 is not one number covering a hole**: `tests/unit` 470, `tests/verification` 2099, `tests/regression` 477 and the root files 1347 collect to exactly 4393. Lint at the judged commit, my own clean worktree: `ruff` `All checks passed!`, `black --check` `128 files would be left unchanged.`, `mypy` `Success: no issues found in 45 source files`.
CI: **run `42771308680` at the judged commit EXISTS and is PARTLY CONCLUDED, and I record it as that rather than as a pass.** `lint, unit and guards` **failure** at step 10 `guards and meta-tests` -- which is the eight and nothing more, every id ruled against the FS1/FT1 predicate by me -- with actionlint, ruff, black, mypy and the unit tests all success before it, **so the guards step is seen to have RUN rather than been skipped behind an earlier red (CZ1 iii)**. `the verification ladder` **had NOT finished when I ruled**: rungs 1, 2 and 3 `success`, rung 6 `in_progress`, rungs 4 and 5 `pending`. **A run that has not finished is not a pass.** No rung is red, so nothing here is a STOP, and the ladder's result for this CODE is already on the record at the tag's own concluded run -- see `## CI at the reviewed commit`. Both determinism jobs `skipped` by their own `workflow_dispatch` condition, and they started BEFORE the lint job concluded, which is the cell for R1196. **CA2 is not reached and CZ1 (iv) does not arise.**
Door (FV2 / GF3 a): **the new door, end to end, and it worked again.** `git worktree add -b review/r1-step4-closure-602bce8 <a path outside the repository> 602bce8d8...`; every measurement below taken in worktrees of my own; this verdict written there through `scripts/write_verdict.py`, committed on that branch and pushed. Fast-forward it with `git merge --ff-only origin/review/r1-step4-closure-602bce8`. **In `C:/dev/floatfea` I ran only read-only `git` and `gh`** -- `worktree prune --dry-run`, `worktree list`, `log`, `show`, `ls-remote`, `gh run list/view`, plus one read-only run of your own `PreToolUse` hook with fabricated stdin -- and `git status --porcelain` there is empty. **Two disclosures of my own are R1201 and R1202.**

## Carried

Every open item of the newest verdict -- `a666b25`, the addendum, verdict 57 -- and of verdict 56 beneath it.

* **R1185 (the one BLOCKING item) -- ANSWERED, AND I RECOMPUTED IT FROM VERDICT 55 RATHER THAN FROM EITHER OF OUR ARITHMETIC.** You told me not to take yours; I did not take mine either. **The corrected derivation is RIGHT, row by row.**

```
claim  verdict 55 item 3's ten names, which two GF3 closes, and where the other
       two struck rows come from
cmd    sed -n '813p' docs/reviews/R1/step-4.md        -- item 3, verbatim
out    L5 and its phantom citation, L9, R1149's dead pause clause, R1155, R1165,
       SR-41, SR-44, R835, R1181's substantive half, R1180's remedy      = TEN
cmd    sed -n '814p'                                  -- item 4, verbatim
out    "The FV2 commit door, which is nobody's inside this loop"
cmd    sed -n '802p' and '803p'   -- verdict 55's own ## Closure items rows
out    R1182 -> "nothing, under EK2. R2, one line";  R1181 -> report prose, EK3
cmd    sed -n '813p' docs/reviews/R1/step-4.md | grep -c R1182
out    0      -- R1182 is NOT in item 3, so the "+2" attribution is right
cmd    sed -n '/^| # | item |/,/^$/p' docs/closure/R1.md | grep -c '^| [0-9]'
out    10     -- rows: L5, L9, R835/R861, R1155, R1165, R1180, R1182, SR-41,
                SR-44, the SUPERVISOR.md step-5 line
cmd    awk over the struck table -- its row count and leading cells
out    4 rows: FV2 door, R1181-substantive, R1149, R1181-prose
cmd    sed -n '503,825p' docs/reviews/R1/step-4.md | grep -niE "witness|step 5"
out    one hit, R1180's own heading. **The SUPERVISOR.md step-5 line is not in
       verdict 55 at all**, so row 10 really is "found closing this"
rule   section 8's corrected header and rule line: 10 - 2 + 2 = 10
judge  **the mapping closes exactly, in both directions.** The two GF3 closes are
       R1149 (e) and R1181-substantive (b), both from item 3; the eight that
       carry are rows 1,2,3,4,5,6,8,9; the +2 are row 7 and row 10. The FV2 door
       is item 4 and R1181's prose half is the closure-item table, as the
       corrected header says. **There is no sixth stale figure in section 8**
```

And I checked what the tag published, since the finding was that it shipped inside the tag: `git show a780a9d:docs/closure/R1.md` reads *"three of them are closed by GF3"* and *"less the three GF3 closes and the one closed by rule, plus R1182 ... and the SUPERVISOR.md step-5 line"* -- `10 - 3 - 1 + 2 = 8` under a table of 10. **The R1185 note's account of its own defect is accurate to the word.** `git cat-file -t R1` is `tag` and it resolves to `a780a9d5...`, so the tag is annotated and unmoved, as the note says.

* **R1189 (a) -- ANSWERED AT BOTH SITES, AND THE BRANCH OF CW0 YOU CHOSE IS THE RIGHT ONE.** You reasoned that no triple could carry it. I measured the vocabulary instead of accepting the reasoning.

```
claim  whether tests/test_tree_prose_consistent.py can express a run conclusion
cmd    grep -n "_VOCABULARY" tests/test_tree_prose_consistent.py
out    235: _VOCABULARY = {"count": count, "lines": lines, "files": files,
                           "defined": defined}
cmd    git grep -nE "4750f07|b286e01" -- floatfea tests scripts .github
         docs/milestones docs/verification
out    (empty)
cmd    git grep -lE "4750f07|b286e01"              -- every tracked file
out    docs/closure (the new measurement), docs/digests, docs/directives (GF3
       verbatim), docs/reviews (mine). **Nothing in the source tree**
rule   CW0 -- a claim about this repository in a comment or docstring is a test,
       a triple, or deleted
judge  four verbs, all over this tree, none able to ask GitHub anything, so the
       triple branch was genuinely unavailable and "deleted, with the measurement
       relocated to where a gh command can be pasted" is the correct branch of
       the menu. **And there is no third site**: the finding named one, you found
       two, and the census over the whole source tree now returns nothing
```

* **R1189 (b) -- ANSWERED, BY A STRONGER MEASUREMENT THAN THE CONDITION ASKED FOR, AND I RULE IT SATISFIED.** The condition said "cites GC2 with the diff listing". **GC2's ancestor rule exists for a commit that has no run**; `a780a9d` now has one, and a concluded run at a commit's own sha outranks an inherited one. **The departure is correct and you named it rather than smuggling it**, which is what the rule asks. Verified independently at run `42761104562`: head `a780a9d5...`, `the verification ladder` **SUCCESS with all six rungs success** (step order 1, 2, 3, 6, 4, 5), `lint, unit and guards` failure with steps 5-9 -- actionlint, ruff, black, mypy, unit tests -- **all success and only step 10 `guards and meta-tests` red**, both determinism jobs `skipped`. **Every figure in the new block reproduces.** One clause of its judge line is false and that is R1196.
* **R1189 (c) -- still open, correctly not acted on.** `docs/closure/R1.md:520-521` still reads *"asserts `cancel-in-progress is True`"* in the present tense. I re-read the paragraph: it is explicitly forward-looking about the rename, a reader is not misled, and verdict 56's closing list did not ask for it. R2 or a final prose pass.
* **R1192 -- ANSWERED, AND I RAN THE WIDER CENSUS RATHER THAN TRUSTING THAT SIX WAS ALL.** Both strikes are in place at `docs/digests/2026-11-09.md:157`. `grep -rniE "step 5|step-5" --include=*.md docs/` less `docs/reviews/`: every remaining hit is another milestone's step 5 (which exists), inside the struck `Tomorrow` block, one of GF1/GF2's own corrections, or ledger row 10's accurate description of `docs/SUPERVISOR.md`. **There is no seventh live false "step 5" sentence about R1.** And the base case the strike cites is real: `docs/directives/GF.md:17-18` reads *"GF2 -- Base case for the CZ1 recursion: the milestone's final verdict (55, PASS, nothing blocking) closes R1"*, so the second strike is justified by the directive and not asserted. **One figure inside that repair went stale in the same commit -- R1198.**
* **R1194 -- ANSWERED, AND I RE-MEASURED THE BLOCK RATHER THAN READING IT.** `git ls-remote origin 'refs/heads/review/*'` gives the four refs at the four shas the block publishes -- `a666b25`, `1a942b1`, `d40f8c6`, `ae96a38`; `git merge-base --is-ancestor` is TRUE for all four against `F3`; `grep -c "review/r1-step3" docs/reviews/R1/step-3.md` is **9**; `grep -c "FV2 gives me no other door" docs/reviews/R1/step-4.md` is **3**. The stranded-verdict hazard it cites is in step 3's own file -- *"MY ADDENDUM WAS STRANDED AND NEVER REACHED `F3`"*, with the repair note naming `eac8af4`. **It is a reviewer-side finding and you recorded it as the reviewer's, correctly.**
* **R1186 -- still open, routed to R2 by verdict 56 item 4, and now CONFIRMED INDEPENDENTLY AND EXTENDED.** See `## Corpus`: a job-level `cancel-in-progress: true` leaves all eight assertions green, and the job it matters most for is the **ladder** -- the job whose cancellation voided a published result both times -- not determinism.
* **R1187's open half -- PARTLY DISCHARGED, and the rest by this commit's own run.** The tag commit's ladder job has concluded SUCCESS on all six rungs, on a machine neither side controls: the first concluded ladder in this window. The run at `602bce8` is the first concluded run covering `tests/` and `.github/` since `d8ee517`, so the inverted gate reaches that machine for the first time. See `## CI`.
* **R1188 -- still open, Xabier's, and now MEASURED rather than forecast.** The `concurrency` group lever is unchanged and the run at `602bce8` queued behind `8985a0a`'s rather than running beside it: created `06:51:25Z`, jobs started `08:02:03Z` -- **seventy-one minutes queued.** That is exactly the trade R1188 named.
* **R1190 -- still open, and I have a correction to it that is MINE, not yours.** See R1200.
* **R1191 -- ANSWERED, and the answer is yes.** The definition loaded into this invocation IS current: it carries GF3 (a)'s named-branch door, GF3 (d)'s full-sha paragraph, FV4 and GE3, and it matches `602bce8:.claude/agents/gating-supervisor.md`, whose newest touching commit is `793e45b`. **I am operating under the post-`793e45b` text and I used the new door.**
* **R1193 -- still open, Xabier's, and I am still the measurement.** My loaded instructions carry the dead corpus-pause clause in two places, both reading "paused until 28 October". I ruled under `CLAUDE.md` section GC3 instead, which leaves batches to my discretion, and I ran one.
* **R1195 -- mine, and your note is accepted.** `git worktree prune --dry-run --verbose` in your checkout prints nothing, so the registrations are live directories and prune cannot close it. `git worktree list` is **15**. R1202 is my own accounting for this round.
* **R835: unchanged, R2** (GE3). Not re-measured.

## Findings

**NONE BLOCK under FR1. For each I tried to write FR1's silently-wrong-result sentence; where I could not the reason is given, and where I could I say so.**

### R1196 (ledger). THE NEW DIGEST BLOCK ATTRIBUTES THE DETERMINISM JOBS' `skipped` TO THE RED JOB ABOVE THEM. THE WORKFLOW'S OWN GRAPH REFUTES IT, AND SO DOES A THREE-RUN CELL.

`docs/digests/2026-11-09.md:229-230`, the judge line of the block you added: *"It did happen one level up -- both determinism jobs are `skipped` behind the red, which is the same hiding at job scope."*

```
claim  whether the determinism jobs' skipped is CAUSED by lint, unit and guards
       failing
cmd    yaml.safe_load('.github/workflows/ci.yml'); each job's needs and if
out    determinism          needs: None  if: github.event_name=='workflow_dispatch'
       determinism_verdict  needs: ['determinism']
                            if: always() && ... 'workflow_dispatch'
       checks               needs: None  if: None
       ladder               needs: None  if: None
cmd    gh run view <id> --json jobs, for all three runs in the window
out    a780a9d  lint failure    ladder success    leg skipped  ten legs skipped
       4750f07  lint SUCCESS    ladder cancelled  leg skipped  ten legs skipped
       b286e01  lint cancelled  ladder cancelled  leg skipped  ten legs skipped
cell   one variable -- the lint job's conclusion, moved across ALL THREE of its
       values. The determinism jobs' outcome does not move
rule   BG0 -- a causal sentence carries the cell that isolates it
judge  **determinism has no needs at all, so nothing above it can suppress it**,
       and it reads skipped in the run where lint SUCCEEDED. At this commit's own
       run both determinism jobs started at 08:02:01Z and were skipped BEFORE the
       lint job concluded. The hedge in the same sentence -- "workflow_dispatch-
       gated by CK0 in any case" -- names the real and only cause; the clause
       before it asserts a mechanism that does not exist
```

**Why it does not block, and the sentence I could not write.** FR1's head is a wrong number in a deliverable or an input used other than as declared. No number moves, and the operative fact for a reader -- that no determinism result exists for a push -- is right and is stated in the same sentence. **Under CZ0 (a) as amended by EZ0 I would have blocked on it**, because a digest is a file sent to Xabier, and I say so rather than smuggling it. *Closed when* the clause says the determinism jobs are `workflow_dispatch`-gated and therefore never run on a push, with the `needs: None` measurement, or drops the "same hiding at job scope" claim.

### R1197 (ledger). THE REPAIR OF R1185 POINTS AT "THE TABLE ABOVE" AND THE TABLE IS BELOW.

`docs/closure/R1.md:921`.

```
claim  what is above line 921 and what is below it
cmd    sed -n '921p'; the nearest '^| ' line before 920; the ledger table's line
out    :921  "10 - 2 + 2 = 10, which is the number of rows in the table above."
       :890  | `TRUSS_FACE_CLOSURE_RELATIVE_COUNTER` | ...   <- the nearest table
                ABOVE, which is section 7's tolerance table
       :925  | # | item | what it is | where it goes |       <- the ledger table,
                BELOW
rule   the same paragraph's other pointer, "The struck table below", which is
       right: the struck table is at :948
judge  the count is correct and the table has ten rows; **the pointer is
       inverted.** The rule block at :957 says "the table above" correctly,
       because from there it is above -- which is where the wording came from
```

Prose in a published deliverable with the number right: FR1's third class. *Closed when* the word is `below`, or the sentence names section 8's table instead of a direction.

### R1198 (ledger). THE REPAIR OF R1192 REPUBLISHED A MEASURED DISTANCE THAT ITS OWN INSERTION MOVED. CP3, IN THE SAME COMMIT RATHER THAN A LATER ONE.

`docs/digests/2026-11-09.md:165-166`: *"**Nineteen lines below this paragraph** the same file says 'There is no step 5' in bold."*

```
claim  the distance the sentence publishes, at the commit that publishes it
cmd    line numbers of "it clears when ..." and of "^**There is no step 5", at
         both commits
out    8985a0a   sentence :157   bold :176   distance 19   <- TRUE when measured
       602bce8   sentence :157   bold :186   distance 29
rule   CP3 -- the paste is copied from a run executed AFTER the final edit, and
       if an edit follows the paste the paste is void
judge  **the commit's own ten-line blockquote is the edit that moved it.** No
       anchor gives nineteen at 602bce8: from the sentence it is 29, from the
       blockquote's first line 24, from its last 16. The figure was correct in
       verdict 56, where 19 was measured at 8985a0a, and it was carried into the
       repair without re-measuring -- which is the species the repair was about
```

FR1's third class, figure wording. **Recorded for its shape rather than its cost**: the paste and the voiding edit are the SAME commit, which is the cheapest case CP3 covers and the easiest to miss. **And my own digit census could not see it** -- the figure is spelled as a word, so `grep -oE '[0-9]+'` over the added lines returns nothing for it and I found it by reading. *Closed when* the distance is re-measured or the locator is replaced by the line number.

### R1199 (ledger, low). THE PREDICATE TABLE GIVES LIMB TWO's REASON FOR A RED WHOSE MEASURED CAUSE IS A DIFFERENT ONE. THE OUTCOME IS UNCHANGED.

`docs/closure/R1.md:167` routes `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` to **limb two**, *"no run exists for a commit before it is pushed"*. Its actual failure line at `602bce8` is *"the 0a table has neither a run row nor the generator's zero-run row"*, and runs do exist in this round. I measured its dependence at five commits: `dc49552` **1 passed**; `8985a0a`, `e274e4c`, `a666b25` and `602bce8` all **1 failed**. It reddens the moment a verdict commit lands after the report, which is EG3 state (2) and limb ONE's reason. **It is a boundary red either way and CZ1 (iv) is not reached**; only the reason is not the measured one. One line, no round.

### R1200 (FF0-class, not ledgered -- it decides which verdict a future green is believed about). THE PUBLISHED BASE-CASE INSTRUCTION NAMES VERDICT 55 AND NO SHA, ITS OWN JUSTIFYING CLAUSE NOW POINTS SOMEWHERE ELSE, AND ONE OF THE TWO SHAS A READER WOULD REACH FOR SILENTLY SELECTS VERDICT 54.

`docs/closure/R1.md:179` and `:484-485`; `docs/digests/2026-11-09.md:157` -- edited by this commit -- and `:206`. The artifact's own words at `:484-485`: *"R2's first report answers verdict 55 in its Carried section, as any step report answers the newest verdict."*

```
claim  what "Answers: verdict 55 @ <sha>" resolves to, for each sha a reader
       would reach for
cmd    _verdict_text_at(sha) from tests/test_report_carried.py, at 602bce8
out    d5add31  verdict 55's own COMMIT   newest entry dc49552, Closes: 1,
                                          findings to R1184      <- CORRECT
       dc49552  the commit verdict 55     newest entry c2bf7d7, Closes: 0,
                REVIEWED                  findings to R1178      <- VERDICT 54
cmd    git show dc49552:docs/reviews/R1/step-4.md | grep -c "^Closes: R1/step-4"
out    0     -- verdict 55 does not exist at dc49552; it was committed after it
cell   one variable -- the sha in the header. VERDICT_TEXT, the findings set, the
       carry requirement and the site set all move with it
cmd    inject the R2 state in a worktree of mine -- the step-under-execution
         marker moved from docs/milestones/R1.md to a new R2.md, and
         docs/reports/R2/step-1.md added -- then flip ONLY which verdict the
         header names
out    answers 55 @ dc49552  ->  test_the_answered_verdict_is_the_NEWEST_one
                                 1 passed
       answers 57 @ a666b25  ->  1 passed
       the module resolves MILESTONE=R2, VERDICT=docs/reviews/R2/step-0.md,
       exists False -- so that test returns early UNCONDITIONALLY
rule   the artifact's own sentence at :484-485
judge  **"@ dc49552" makes every carry, finding and site guard measure VERDICT 54
       while the header declares 55**, and R1179-R1184 drop out of the carry
       requirement unseen. The one guard that compares the header with reality is
       vacuous in exactly the state the instruction is for. **And "as any step
       report answers the newest verdict" no longer selects verdict 55**: 56, 57
       and this verdict followed it
```

**Weighted honestly, in both directions.** `d5add31` IS in the artifact, labelled *"the verdict commit"*, at `:56`, `:58`, `:151`, `:153` and `:216` -- three hundred lines from the instruction, and a grep for "verdict 55" returns twelve hits with the sha in none of them. The report's own earlier headers -- `verdict 53 @ b0ff398`, `verdict 54 @ 5f02798` -- establish the convention, which makes the mistake less likely; nothing catches it if it is made. **It does not block this commit**: no wrong number exists in `602bce8` and there is no open step to hold. **But it is not a ledger row either** -- under FF0 an item that decides whether a green is believed goes in the next commit. *Closed when* the four sites give the sha, or say "the newest verdict's commit" instead of a number. **The correct sha for verdict 55 is `d5add31`; after this verdict merges, the newest verdict's commit is this one.**

**And one half of this I could NOT measure, recorded as that rather than drawn from.** Whether the EIGHT clear in the R2 state is still unmeasured: my stub R2 report gave 48 reds, which are the stub's own missing generated sections and not a measurement -- the same wall verdict 56's R1190 probe hit. **I am not publishing 48 as a figure.** It needs a real R2 report, which is EG3 (ii) from your side one more time.

### R1201. THE PreToolUse HOOK'S FALSE REFUSALS, MEASURED. YOUR ESCALATION IS SUBSTANTIATED AND ITS WORDING IS WIDER THAN THE CAUSE.

You raised this for Xabier and said you split the measurement rather than rewording the command. I ran the hook directly with fabricated stdin carrying no agent_type, which is what the implementer looks like to it.

```
claim  which read-only Bash commands naming the verdict directory are refused
cmd    printf <hook JSON> | bash .claude/hooks/protect-reviews.sh
out    grep -c Closes docs/reviews/R1/step-4.md                       ALLOW
       sed -n 1,5p docs/reviews/R1/step-4.md                          ALLOW
       wc -l docs/reviews/R1/step-4.md > /tmp/n                       ALLOW
       grep -v "^#" docs/reviews/R1/step-4.md > "$SP/out.txt"         DENY
       git log --oneline -- docs/reviews/R1/step-4.md | grep install   DENY
       cat docs/reviews/R1/step-4.md | grep -c touch                  DENY
rule   the hook's own recorded sentence -- "every widening of this rule has cost
       a read and bought nothing"
judge  **three false refusals, all reads, and the cause is NOT "the command text
       names the directory"**, because a bare grep -c is allowed. Two causes:
       the R1107 UNRESOLVED clause, which refuses a redirect whose target is a
       SCRATCHPAD path merely because it is spelled with a variable; and the
       VERBS clause, which matches install, touch, cp, mv, rm, dd, tee and
       truncate ANYWHERE in the command, including inside a grep pattern.
       **These are the fifth and sixth instances of the pattern the hook records
       about itself**
```

**For Xabier, and not the implementer's to fix.** UNRESOLVED was bought by three matrix rows that wrote a verdict through an unresolvable target, so deleting it reopens a write hole; the repair is to ask whether an unresolved target COULD be protected, not to refuse every variable. **I did not edit the hook and I may not.** Your escalation stands; only the sentence describing it needs narrowing.

### R1202. MY OWN HAZARD THIS ROUND, STATED BECAUSE NOBODY ELSE WOULD SEE IT.

I wrote the new corpus file into my suite worktree -- the one where my own whole-suite run was measuring -- and it sat there untracked for about three tool calls before I noticed and moved it out. Its git status is empty again. **I then measured whether it could have moved anything rather than assuming it could not**: no test enumerates the corpus directory (each scanner names its own file by path), the CW0 prose guard reads only .py and .md files, and the only guard that reads untracked state is the site resolver, which would have had to be handed that path by a verdict. **The file now lives in my review worktree and is committed separately from this verdict**, as BE3 requires. Three reviewer worktrees of mine were created this round; the two throwaway ones are removed and the registration count is back to 15. **Recorded as mine, like R1195.**

## The eight, per id, at this commit, on my own measurement -- and the state has CHANGED since verdict 56

**The state you named is right and it matters: `a666b25` is now the newest verdict and no report answers it, so this is EG3 state (2), not the state verdict 56 measured.** I ruled each id against the FS1/FT1 predicate individually, as EG3 (i) requires, rather than ruling a cascade by family -- which is the condition the eighty-third verdict earned when the eighth member of such a group turned out to be a real defect (R629).

**ONE ROOT AND SEVEN CASCADE IDS, AND I MEASURED THE CASCADE RATHER THAN INFERRING IT.**

```
claim  what each of the eight fails ON, individually
cmd    run each of the seven guard_survives ids ALONE and extract the INNER
         FAILED list its own message pastes
out    all seven: inner `1 failed, 378 passed`, and the single inner id is
       tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
       -- the same one in every case, no eighth cause hiding in the group
cmd    the ROOT id alone, at five commits in the window
out    dc49552   1 passed     <- report newer than the verdict
       8985a0a   1 failed
       e274e4c   1 failed
       a666b25   1 failed
       602bce8   1 failed
cell   one variable -- whether a verdict commit newer than the report exists.
       The report is frozen at dc49552 by EK3 and its content never moved
rule   FS1 with FT1 -- a red is a boundary red if it names a finding or a site
       of the newest verdict, OR if its subject is the commit carrying it
judge  **the root red is verdict-dependent BY MEASUREMENT, not by family**: it is
       green in the one state where the report is the later of the two and red in
       every state where a verdict follows it. That is EG3 state (2) exactly, and
       it clears on the answering report. The seven are its cascade, each one
       traced by its own pasted inner list. **No red fails the predicate, so
       CZ1 (iv) does not arise**
```

**AND CI'S OWN EIGHT ARE THE SAME EIGHT, ON A MACHINE NEITHER OF US CONTROLS.** At `8985a0a`'s concluded run the `guards and meta-tests` step reports `8 failed, 1339 passed in 497.94s` and the ids are identical to mine, id for id. That is a different operating system, a different libm and a different BLAS reaching the same eight, which is the one thing a local run cannot establish.

**One honest narrowing of your own control.** You wrote that `dc49552` against `602bce8` is "one variable". It is not -- several commits separate them. The isolation is the five-commit series above, which puts the flip at the landing of a verdict newer than the report and nowhere else.

## CI at the reviewed commit: THE RUN EXISTS, ITS GUARDS JOB HAS CONCLUDED WITH EXACTLY THE EIGHT, AND ITS LADDER HAD NOT FINISHED WHEN I RULED

**Full 40 characters, always (GF3 d): `gh run list --commit 602bce8d84745a71bb80b36c52a735aaa97f3ad4`.** One run, `42771308680`.

| job | conclusion | what it says |
|---|---|---|
| `lint, unit and guards` | **failure** | step 10 `guards and meta-tests`. Steps 5 to 9 -- actionlint, ruff, black --check, mypy, unit tests -- are ALL success, **so the guards step is seen to have RUN rather than been skipped behind an earlier red, which is exactly what CZ1 (iii) exists to see** |
| `the verification ladder` | **no result yet** | rungs 1, 2 and 3 `success`; rung 6 `in_progress`; rungs 4 and 5 `pending`. **A run that has not finished is not a pass and I record it as that rather than skipping it.** No rung is red, so nothing here is a STOP |
| `CI determinism -- leg` | `skipped` | by its own `workflow_dispatch` condition -- unavailable, not passing |
| `CI determinism -- ten legs agree` | `skipped` | the same |

**The guards red is the eight and nothing more.** The step-level log is not downloadable until the whole run concludes, so I did not take the ids from it; I took them from my own whole-suite run at this commit and from the concluded run at `8985a0a`, where the same step reports `8 failed, 1339 passed in 497.94s` with ids identical to mine. **Every one satisfies the FS1/FT1 predicate per id by my own measurement, so CA2 is not reached and CZ1 (iv) does not arise.**

**AND THE LADDER'S RESULT FOR THIS CODE IS ALREADY ON THE RECORD, WHICH I MEASURED RATHER THAN WAITED FOR.**

```
claim  whether the tag commit's green ladder describes the tree under review
cmd    git diff --stat a780a9d50de4d60a8312e425541a83dc11bb1d04..602bce8
         -- . ":(exclude)docs"
out    .claude/agents/gating-supervisor.md | .github/workflows/ci.yml |
       CLAUDE.md | tests/goldens/collected_tests.txt |
       tests/test_ci_workflow_is_wellformed.py
cmd    gh run view 42761104562 --json jobs            -- the tag's own run
out    the verification ladder   SUCCESS, all six rungs success
judge  **no floatfea/ file moved and nothing any ladder rung reads moved** -- the
       two tests/ paths are a root guard and the collected-set golden -- so the
       tag's concluded ladder measures this tree's ladder on a machine neither of
       us controls. **And I ran all six rungs myself as well**: they are inside
       my 4385 passed, 0 failed at the judged commit
```

**R1188, measured rather than forecast.** The run was created at `06:51:25Z` and its jobs started at `08:02:03Z`: **seventy-one minutes queued** behind `8985a0a`'s run, because GF3 (c) turned cancellation off and left the `concurrency` group in place. That is the trade R1188 named, and it is the reason the ladder had not finished when I ruled. The lever is Xabier's.

## Tolerances touched

**None.**

```
cmd    git diff 8985a0a..602bce8 --numstat -- floatfea floatfea/tolerances.py
         tests/conftest.py 'tests/**/conftest.py' .claude docs/SUPERVISOR.md
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
```

No value, no form, no counter, and floatfea/ is untouched entirely. **No conftest or plugin under tests/ moved, so CH2/CI0 is clear** -- I read the diff as empty rather than inferring it from a green suite, and the ls-files line returns a file, so the instruction is not silently matching nothing. **.claude/ and docs/SUPERVISOR.md are untouched by this commit, so there is no STOP-class finding**, and the only commit touching them since the R1 tag is 793e45b, a standalone process: commit citing GF3 whose diff contains no floatfea/ and no tests/ -- measured, not read from its message.

## EQ0: THIS COMMIT IS PROSE-ONLY, SO EQ0 EXEMPTS IT. YOUR MEASUREMENT IS RIGHT, AND HERE IS THE CHECK THAT COULD HAVE REFUTED IT

You asked me to check rather than accept it, and you named the two hazards. Both are closed, and the second check carries the weight, because the first has a hole.

```
claim  whether either code-bearing file changed any behaviour
cmd    non-comment lines of ci.yml at both commits, diffed
out    IDENTICAL -- every added and removed line begins with a hash
cmd    yaml.safe_load both whole files and compare the LOADED objects
out    parsed equal: True
cmd    the same, through the file's own duplicate-REJECTING loader
out    loads clean; concurrency group unchanged, cancel-in-progress False
cmd    ast.parse both versions of tests/test_ci_workflow_is_wellformed.py with
         every docstring stripped, and compare the dumps
out    AST minus docstrings equal: True; the nine function names unchanged
rule   EQ0 -- a closure commit that changes a gate or a tolerance is reviewed;
       one that changes only prose is not
judge  **prose only, so EQ0 exempts this commit and the right finding is to say
       so.** The first check has a hole worth naming: stripping hash-prefixed
       lines would also strip hash lines that were CONTENT inside a YAML block
       scalar, so an identical result there is consistent with a real change.
       The parsed-object comparison is what closes it, because a changed scalar
       changes the object. **Your worry about the collected-set golden is
       answered by the name list**: the golden holds node ids and no test name
       moved, which is why 438f2db needed its own commit for GF3 (c)'s rename
       and this one does not
```

I reviewed it anyway, under EB4, because you invoked me and because this window also contains CZ1 (iv) for the R1 tag's own red. **It consumed no round either way.**

## EH4: THE ONE GATE IN THE WINDOW, SOLVED IN BOTH DIRECTIONS

The inverted assertion is that the parsed concurrency mapping has cancel-in-progress exactly False. EH4 asks for the weakening side too, which is the side nobody chooses.

```
cmd    mutate the parsed document, dump it back, run the eight assertions
out    control, round-tripped                        8 passed   <- the control
       D1  cancel-in-progress -> true                1 failed   CAUGHT
       D2  the key deleted entirely                  1 failed   CAUGHT
       D2  the whole concurrency block deleted       1 failed   CAUGHT
       D2  the STRING "false"                        1 failed   CAUGHT
       D2  the integer 0                             1 failed   CAUGHT
       D2  an expression that is true on a push      1 failed   CAUGHT
rule   EH4 -- both directions, including the two that weaken a gate
judge  **the assertion is an IDENTITY check, not a truthiness check, so every
       weakening shape reddens.** Worth measuring rather than assuming: an
       equality against False would have passed the integer 0, and a falsiness
       test would have passed the deleted key. **The gate is sound at WORKFLOW
       scope and blind at JOB scope**, which is the corpus batch below
```

## Corpus -- EG4(e) IS DEAD BY DATE AND GC3 LEAVES BATCHES TO ME, SO I RAN ONE

**The pause did not hold and cannot: my own loaded instructions still read "paused until 28 October" in two places and it is 10 November.** That is R1193, the reviewer's own item and still Xabier's. I ruled under CLAUDE.md section GC3 and ran a batch, because this window contains the one gate whose coverage nobody had measured from outside.

**tests/corpus/ci_workflow_job_gating_shapes.txt, batch 54, 6 entries, ALL NEW, committed separately.** The axis is the one your own R1186 opened: the shipped check asserts CK0's and GF3 (c)'s claims as properties of the parsed document, which is the right form -- but every one of its eight assertions reads either a WORKFLOW-level key or ONE NAMED JOB, and GitHub honours concurrency and needs at job scope too.

**Coverage, measured rather than asserted: 1 of 6 caught.** The control is the round trip itself: the unmutated document, dumped and reloaded, gives 8 passed, so the dump is not what moves an outcome.

```
out    determinism  job-level cancel-in-progress true     8 passed  MISSED
       LADDER       job-level cancel-in-progress true     8 passed  MISSED
       determinism  needs: [checks]                       8 passed  MISSED
       determinism  if: always()                          1 failed  CAUGHT
       determinism  if: always() OR ...workflow_dispatch   8 passed  MISSED
       determinism_verdict  if: always() OR ...!=...       8 passed  MISSED
judge  **R1186 is confirmed from outside, and it is wider than it was filed as.**
       It named the determinism job; the LADDER is the job whose cancellation
       voided a published result twice, at 4750f07 and b286e01, and a job-level
       key there is invisible too. **And one shape is new**: the determinism
       gate is a SUBSTRING test for workflow_dispatch in the condition, so
       always() OR github.event_name == workflow_dispatch contains the token,
       passes the gate, and is true on every push. A needle that tests for the
       presence of a token cannot test the token's effect
```

**No guard is asked for and none may be built** -- EK2 repairs or deletes, it does not extend, and R1186 is already routed to R2. The entries are data; what they measure is that the coverage claim rests on shapes its own author chose. **And I checked my batch cannot redden anything**: the four root guards plus the three CI-gate files give **305 passed** with the file present.

## Which criterion I ruled under, and the one question inside it

**I ruled under FR1 with EZ0, and I am not asking for the criterion to move.** Two readings are available and I am naming the choice rather than leaving it silent. CLAUDE.md scopes FR1 to "the remainder of R1", and my own agent file says CZ0 "is the criterion again once R1 closes" -- and R1 closed at GF2 and is tagged. **I ruled FR1 for three reasons**: this commit is R1's own closure follow-on, required by R1's CZ1 (iv); verdicts 56 and 57 were both written after GF2 closed R1 and both ruled under FR1 explicitly, so ruling CZ0 now would judge a repair under a rule it was not commissioned under, which is BP0 applied to the criterion itself; and FR1 exists because the cost is the round and not the repair.

**It changes nothing material this round, which is why this is one paragraph and not an escalation.** The only finding the two readings separate is R1196, and I have named it as the one I would have blocked on under CZ0 (a) as amended by EZ0. **If Xabier reads FR1 as having lapsed at the tag, then R1196 blocks and its repair is one clause.** Either way you have the information, and no round turned on it.

## Next step opens when

**NO STEP IS OPEN AND NOTHING HERE OPENS ONE.** Step 4's disposition is verdict 55's Closes: R1/step-4; R1's is GF2 and the pushed R1 tag. This verdict reopens neither (DD1), and the Stop hook keys on the Closes: line rather than on a header, so a PASS from me creates no refusal.

1. **R1200, in the next commit rather than the ledger (FF0).** Four sites give the base-case instruction with no sha; "@ dc49552" silently selects verdict 54 and nothing in the R2 state catches it. One clause each.
2. **R1196, R1197, R1198 and R1199 -- one line each, in that commit or in R2's first report.** None blocks under FR1. R1196 is the one that blocks under CZ0.
3. **To R2 as already routed, unchanged by me:** section 8's ten rows, R1186 (now wider -- the ladder job as well), R1188 and the concurrency group lever, R1189 (c), R1190 with my R1200 correction, R1191, R1193, R1201, and R835.
4. **For R2's first report, which is EG3 (ii) from your side one more time:** it answers **the newest verdict's commit**, which after this merge is this verdict's commit, and it measures the eight at its own commit. **R1200 is the warning that the sha is the load-bearing part, not the number.**
5. **Nothing is owed to me.** R1195, R1201 and R1202 are mine or Xabier's.

**On the schedule.** R1 closed on 9 November, inside FW0's 10 November, at full scope, and this commit discharges its last blocking item. **Nothing in this round moved a date.**


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 8985a0ae223a030f5d1468ca8c1e173909959083
**Reviewed commit: `8985a0ae223a030f5d1468ca8c1e173909959083`.**
Verdict: HOLD
Scope: **ADDENDUM to the interim check at `8985a0a`, same tree, same round, no new report revision â€” so it counts against no round (ES0) and carries no `Closes:` line (FK1).** The verdict above is unchanged: HOLD on R1185, eight other findings, step 4 CLOSED (DD1), R1 CLOSED (GF2). **This entry exists because I found one thing AFTER writing it, and it is a correction to the verdict above, not to the work.** Two disclosures and one measurement, each MINE.
Tests: unchanged from the entry above and not re-run: **4393 collected, 8 failed, 4385 passed, 0 skipped at `8985a0a`**, my own runs. Nothing in the tree moved between the two entries.

## Carried

* **Everything in the entry above, unchanged.** R1185 still blocks and its closing condition is unchanged. R1186 to R1193 stand as written.
* **One sentence of my own above is CORRECTED here, and it is the one about my own door.**

## Findings

### R1194. THE FV2 ESCALATION'S PREMISE WAS FALSE BY MEASUREMENT, AND THE EVIDENCE WAS THREE MERGED BRANCHES AT `origin` IN THIS MILESTONE. IT IS A REVIEWER-SIDE FINDING AND IT IS NOT THE IMPLEMENTER'S.

My entry above says *"Fifth round of escalation ended"*, and `docs/closure/R1.md` records the door as *"ruled after four consecutive rounds of escalation"* under which *"the reviewer committed in the implementer's working tree because nothing else could move `F<n>`"*. **I checked that premise after writing it, and it does not hold.**

```
claim  whether a named review branch had ever moved a verdict onto F3 before GF3 (a)
cmd    git ls-remote origin "refs/heads/review/*"
out    e274e4c  refs/heads/review/R1-closure-56     <- mine, today
       1a942b1  refs/heads/review/r1-step3-v40
       d40f8c6  refs/heads/review/r1-step3-v41
       ae96a38  refs/heads/review/r1-step3-v42
cmd    git merge-base --is-ancestor <each> F3
out    all three: ANCESTORS -- merged. "review: R1 step 3 interim check at 503b256",
       "... at 609f9ac", "... at f87e087", dated 29 October
cmd    grep -c "FV2 gives me no other door" on each step's verdict file
out    docs/reviews/R1/step-4.md   3
       docs/reviews/R1/step-3.md   0
cmd    grep -n "review/r1-step3" docs/reviews/R1/step-3.md
out    :4934  "wt-verdict (branch review/r1-step3-v34, where this file is written)"
       :5283, :5450  the same, two more rounds -- the step-3 reviewer recorded the door
                     it used, three times, under its own "WHERE I WORKED (FV2)" heading
cell   one variable -- the step. Same repository, same FV2 text, same `write_verdict.py`
rule   the escalation's own words: "FV2 provides no other door"
judge  **the door existed, was used at least three times in the PREVIOUS STEP of this
       same milestone, and all three verdicts reached `F3` by it.** The step-4 reviewers
       then escalated it as unsolved for four consecutive rounds and wrote in the
       implementer's checkout instead. **That is SR-70's shape exactly** -- an escalation
       of a question the repository had already answered -- except that this time the
       answer was in the previous step's own verdict file, written by a reviewer
```

**GF3 (a) is still the right ruling and I am not asking for it back:** it makes the door mandatory, documents the fast-forward, and names the ref-graph property that makes the separation structural rather than behavioural. **What is wrong is the history around it**, and three places carry it: my entry above (*"fifth round of escalation ended"*), `docs/closure/R1.md` Â§ *How a verdict reaches the branch*, and `docs/SUPERVISOR.md`'s retained escalation block. **Under FR1 none of this blocks** â€” no number is wrong and no input is used other than as declared, and a verdict is not a published deliverable. **It is recorded because the lesson is the one FP0 and GC2 were both built for: read the record before escalating**, and because the cost was real â€” step 3's L39 was a verdict stranded on an unmerged `review/` branch, which is the door's known hazard, and the step-4 rounds paid for the escalation instead of for the hazard.

*Closed when* the sentence in `docs/closure/R1.md` says the door had been used in step 3 and was escalated anyway â€” one clause, in the same follow-on commit as R1185. **Mine to find, not yours to apologise for.**

### R1195. TWO DISCLOSURES ABOUT MY OWN DOOR, BECAUSE THE SENTENCE I WROTE ABOVE IS WIDER THAN WHAT I MEASURED.

My `Door` line above says *"Nothing of mine was written in `C:/dev/floatfea`"*. **That is true of its WORKING TREE and not of its `.git`, and the distinction is the one FV2 actually turns on.** Stated rather than left for someone to find:

```
claim  what this review wrote inside the implementer's repository
cmd    git status --porcelain in C:/dev/floatfea, before and after
out    (empty) both times -- the WORKING TREE is untouched, which is what FV2's two
       recorded failures were about
cmd    what nevertheless reached its `.git`
out    (i)  four `git worktree add` registrations -- mine; the door itself needs them
       (ii) one `git fetch origin review/R1-closure-56`, which I ran to verify the
            fast-forward applies. **AVOIDABLE**: the same ancestry is checkable in my
            own worktree, since `8985a0a` is my commit's parent
rule   FV2 -- "never run `checkout`, `reset`, or any write of any kind in the
       implementer's WORKING TREE"
judge  **no breach, and the wider sentence I wrote was imprecise.** `git worktree add`
       writes repository metadata and the door GF3 (a) rules cannot be used without it,
       so "the reviewer writes nothing in the implementer's repository" is not achievable
       as stated anywhere; "nothing in its working tree" is, and is what matters
```

**And the accumulation, which is mine and my predecessors' litter rather than a defect:** `git worktree list` in the implementer's checkout shows **eleven** reviewer worktrees registered under the session scratchpad, four of them mine and seven from earlier invocations. `git worktree prune` would clear the dead ones and it is a write I will not make. *Closed when* someone with the implementer's tree runs `git worktree prune`, or FV2 says who may.

## Tolerances touched

**None.** Nothing in the tree moved between this entry and the one above; the diff is empty by construction.

## Next step opens when

**Unchanged from the entry above, plus one clause.** R1185 is still the one blocking item and still one sentence. **Add to the same follow-on commit:** R1194's clause in `docs/closure/R1.md` Â§ *How a verdict reaches the branch* â€” that the door had been used three times in step 3 and was escalated anyway. **R1195 is mine and needs nothing from you.**

**And one thing I will not do.** My entry above is pushed on `review/R1-closure-56` and I am not force-pushing to fix a sentence in it â€” `CLAUDE.md` lists force-push among the standing constraints that need Xabier. **An addendum is the sanctioned way to correct a verdict**, so this is it, and the uncorrected sentence stays visible above with this entry naming it. That is the same choice step 3's L39 reached from the other side.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 8985a0ae223a030f5d1468ca8c1e173909959083
**Reviewed commit: `8985a0ae223a030f5d1468ca8c1e173909959083`.**
Verdict: HOLD
Scope: **R1 step 4 â€” ES0 INTERIM CHECK (counts against no round) AND the EQ0 review of `d8ee517`'s gate change (counts against no step's rounds, EB4).** No new report revision exists: the newest is step 4 revision 4 at `dc49552`, which verdict 55 reviewed. **Step 4 stays CLOSED (DD1) and R1 stays CLOSED (GF2); this verdict reopens neither, and `--closes` is correctly absent (FK1).** Written with `--interim` (FS2). **Ruled under FR1 with EZ0** â€” see `## Which criterion I ruled under`. **GE3: `R835: unchanged, R2`. Not re-measured.** EU1 does not arise (no tolerance value and no declared counter moved), but the adversarial case was run anyway, because the diff moves a *gate assertion* and the configuration a diff chooses is the only one it demonstrates. **GA3's 150-line target is OVERRUN at 403 lines and I say so rather than trimming the evidence**: the overrun is six injection and probe cells, a four-run controlled pair on CI itself, the golden measured against live collection in both directions per root, a full census of live "step 5" assertions, the four-way partition of the suite, and nine findings each carrying its own closing condition. GA3 says the target does not limit what I may rule.
Tests: **4393 collected, 8 failed, 4385 passed, 0 skipped AT THE JUDGED COMMIT `8985a0a`, MY OWN RUNS, in EI0's two halves, in `git worktree`s of my own (FV2), `-p no:randomly`, against a venv of my own installed from my worktree** (`import floatfea` resolves inside it, measured). Main half **3961 passed, 0 failed, 0 skipped in 3132.39s (0:52:12)**, with the two known benign warnings (a `numpy` deprecation site and the `RuntimeWarning: overflow encountered in dot` that `rung1`'s `orient_norm_overflow` corpus entry exists to raise). **And I partitioned it four ways and ran every part separately as well, which is how I know the 3961 is not one number covering a hole**: `tests/unit` **470 passed**, `tests/verification` (rungs 1 to 6) **2099 passed, 0 failed in 143.09s**, and the root guard files less the three report-parametrised ones **915 passed**. `470 + 2099 + 477 + 1347 = 4393` by collection, and `1347 - 432 = 915`, so the partition closes. **NO RUNG IS RED, so nothing here is a STOP**, and I measured the ladder myself rather than inferring it from a job that had not finished. Order-independence spot-checked with pytest-randomly ENABLED: `tests/unit` + `rung5` **557 passed**.. The three report-parametrised files **8 failed, 424 passed** of `432`: `test_report_carried.py` + `test_report_guard_states.py` **8 failed, 395 passed in 91.23s**, `test_report_numbers_are_sourced.py` **29 passed**. **All eight reds are EG3 state (2), ruled per id against the FS1/FT1 predicate below, and CI's own eight at `a780a9d` are the same set.** **CI at the judged commit: UNAVAILABLE -- the run EXISTS, is `pending`, and has created ZERO jobs. A run that has not finished is not a pass, and I record it as that rather than skipping it (CK2's third state by a different cause: queued, not unpaid). It is not red. R1187 has the full trace, the partition that says exactly which two files CI has never run, and the reason it is queued (R1188).** The only CI red in the window is `guards and meta-tests` at `a780a9d` -- `8 failed, 1339 passed` -- and all eight satisfy the FS1/FT1 predicate per id by my own measurement, so CA2 is not reached and CZ1 (iv) does not arise. Lint at the judged commit, in my own clean worktree: `ruff` `All checks passed!`, `black --check` `128 files would be left unchanged.`, `mypy` `Success: no issues found in 45 source files`.
Door (FV2/GF3 a): **I used the new door and it worked.** `git worktree add` at `8985a0a`, `git switch -c review/R1-closure-56`, the verdict written there through `scripts/write_verdict.py`, committed on that branch and pushed. **Nothing of mine was written in `C:/dev/floatfea`** â€” there I ran only read-only `git` and `gh`. Fast-forward it with `git merge --ff-only origin/review/R1-closure-56`. Every injection, probe and control below ran in a second worktree of mine. **One thing about GF3 (a) that is not a finding against the work and is a finding about the procedure: R1191.**

## Carried

* **Verdict 55's one blocking item, R1178 â€” answered at verdict 55, not reopened here.** Nothing carried from it.
* **Verdict 55 `## Closure items`, five rows â€” three FIXED in `82842ae`, two routed to R2. I re-measured all five rather than reading the table.**
  * **R1179 â€” ANSWERED.** `430` is gone as a figure about a commit; `docs/closure/R1.md:19-21` now quotes each guards-half figure with the tree it was taken in. **I reproduced all three arms**: `432 passed, 0 failed` at `dc49552`, `8 failed, 424 passed` at `d5add31`, `8 failed, 424 passed` at `8985a0a`. The published `407 @ 566ef94` I did not re-take.
  * **R1183 â€” ANSWERED.** The promised paste is at `:74-75`, `54 passed in 0.05s`.
  * **R1184 â€” ANSWERED, and in the form the condition named.** `docs/USER_GUIDE.md:319` now reads *"**none moved** â€” another clause is the larger here, which is reason 1 below; whether such a row moves at some other `C_m` is where its kink falls (R1184)"*, and reason 1 at `:334` is *"Another clause governs the row at this `C_m`"* â€” which is what verdict 55 asked for by name. The retired mechanism is gone from the cell.
  * **R1180 â€” R2, as routed.** Not built; FK2 and EK2 are the stated reason and they hold.
  * **R1182 â€” R2, one line, as routed.** Not extended, which EK2 requires.
* **Verdict 55 item 3's ten R2 names â€” ALL TEN ACCOUNTED FOR in `docs/closure/R1.md` Â§ 8: eight carried, two closed. The ROWS are right; the sentence that derives them is not â€” R1185.**
* **Verdict 55 item 4, the FV2 commit door â€” CLOSED by GF3 (a), and I used it.** Fifth round of escalation ended.
* **Verdict 55 item 5, the ladder green at the closure commit's own pushed sha â€” PARTLY DISCHARGED.** `82842ae`'s pushed run `42600509104` has `the verification ladder` = **success**, all six rungs, on a machine neither of us controls. At the tag commit `a780a9d` that job had **not concluded** when I ruled, and at the judged commit no run had started â€” R1187.
* **R835: unchanged, R2** (GE3).
* **The three pathspecs my instructions diff separately, each measured.** `floatfea/tolerances.py` â†’ empty. `tests/conftest.py 'tests/**/conftest.py'` â†’ empty, and `git ls-files` over the same pathspec gives `tests/conftest.py`, so the instruction is not broken. `.claude docs/SUPERVISOR.md` â†’ `793e45b` only, a standalone `process:` commit citing GF3 and touching no `floatfea/` and no `tests/`. **NOT a STOP** â€” see item 4 of my rulings.

## Findings

**NINE FINDINGS, R1185 to R1193. ONE BLOCKS.** For the five that are ledger rows -- R1186, R1188, R1189, R1190, R1192 -- I tried to write FR1's silently-wrong-result sentence and could not, and each says why rather than leaving it implied. **R1187 is a CI record and not a finding against the work**; **R1193 is FF0-class** -- the gating apparatus, which FF0 puts in the next commit rather than on the ledger; **R1191 is about the procedure and goes to Xabier.** I am not giving a count by criterion: verdict 55 declined to and was right, because a count of what a criterion catches is a property of the list.

### R1185 (BLOCKING). SECTION 8's RECONCILIATION RULE DOES NOT YIELD SECTION 8's COUNT, AND IT MISSTATES WHICH ITEMS ARE CLOSED â€” IN THE SECTION THAT DEFINES WHAT R2 INHERITS, INSIDE THE `R1` TAG.

`docs/closure/R1.md` Â§ 8. Its header says *"Verdict 55 Â§ Next step opens when item 3 names ten things for R2; **three of them are closed by GF3** and are struck below with what closes each, one is closed by rule, and the rest carry"*, and its `rule` line says *"verdict 55 item 3's ten names, **less the three GF3 closes and the one closed by rule**, plus R1182 ... and the SUPERVISOR.md step-5 line found here"*.

```
claim  how many of verdict 55 item 3's ten names GF3 closes, and whether the published
       derivation reproduces the published count
cmd    sed -n '/^| # | item |/,/^$/p' docs/closure/R1.md | grep -c '^| [0-9]'
out    10
cmd    sed -n '/^| item | closed by |/,/^$/p' docs/closure/R1.md | grep -c '^| ~~'
out    4
cmd    verdict 55 "Next step opens when" items 3 and 4, read against the four struck rows
out    item 3's ten:  L5, L9, R1149, R1155, R1165, SR-41, SR-44, R835,
                      R1181-substantive, R1180
       struck rows:   the FV2 door       <- verdict 55 item **4**, NOT item 3
                      R1181-substantive  <- item 3, GF3 (b)
                      R1149              <- item 3, GF3 (e)
                      R1181 prose half   <- verdict 55's `## Closure items` table, NOT item 3
rule   the artifact's own `rule` line: ten, less three, less one, plus two
judge  **the published arithmetic is 10 - 3 - 1 + 2 = 8 and the published `out` is 10.**
       Of item 3's ten, GF3 closes TWO. The correct derivation is 10 - 2 + 2 = 10, and
       that one reproduces the table exactly
```

**The ROWS are right and I checked every one.** All ten of item 3's names are accounted for â€” eight carried (L5, L9, R835, R1155, R1165, R1180, SR-41, SR-44) and two struck (R1149, R1181-substantive) â€” plus R1182 from verdict 55's closure-item table and the `docs/SUPERVISOR.md` step-5 line the implementer found itself, which I confirmed at `docs/SUPERVISOR.md:155`. **And all four struck rows are genuinely closed**, verified rather than accepted: GF3 (a) is in both reviewer files, GF3 (b) quotes GC2 verbatim and correctly, GF3 (e) records the expiry, and EK3 closes the prose half by rule.

**FR1's sentence, which is why this blocks rather than ledgers.** The silently wrong result is **R2's inherited carry list**. Â§ 8 is the only place that states how that list was derived; it is a published deliverable under EZ0; it is inside the `R1` tag; and a reader applying its stated rule to verdict 55 removes **three** of item 3's ten where only **two** are closed â€” and the text cannot say which third, because the third struck row is not in item 3 at all. One live R2 item is dropped and nothing determines which. The implementer named the stake itself: *"If that reconciliation is wrong, R2's first report inherits a wrong carry list."* It is a wrong number in a published deliverable, FR1's first head, and none of FR1's three non-blocking classes reaches it: it is not a refusal message, not a census needle, and **not report prose** â€” a closure artifact is not a report, which is the distinction EZ0 and EK3 both turn on.

*Closed when* Â§ 8's header and `rule` line say **two** of item 3's ten are closed by GF3 and name the other two struck rows' actual sources â€” verdict 55 item 4 for the FV2 door, verdict 55's `## Closure items` table for R1181's prose half â€” or drop the derivation and let the table stand on the `cmd` that counts it. **One sentence, one follow-on `closure:` commit, which is CZ1 (iv)'s shape. It reopens neither step 4 nor R1, and the ten rows do not need re-auditing: I audited them.**

### R1186 (ledger). THE INVERTED GATE PINS THE WORKFLOW-LEVEL KEY ONLY, AND A JOB-LEVEL `cancel-in-progress: true` WALKS PAST ALL EIGHT TESTS IN THE FILE.

`tests/test_ci_workflow_is_wellformed.py:137-141`. **First, the gate carries its own failure in every direction I could construct, including the revert you asked about** â€” EH4, and the four arms are one variable each, restored between every one:

```
claim  the inverted assertion reddens on the revert and on three other defeats
cmd    one variable per arm, in a worktree of MINE at 8985a0a, restored between each
out    baseline, `cancel-in-progress: false`                 1 passed
       A1  reverted to `true`                                1 FAILED at :138
       A2  the `cancel-in-progress` key deleted              1 FAILED at :138
       A3  the whole `concurrency:` block deleted            1 FAILED at :138
       A4  `cancel-in-progress: "false"`, a YAML string      1 FAILED at :138
       restored                                              1 passed
rule   the shipped assertion, `concurrency.get("cancel-in-progress") is False`
judge  **a silent revert to `true` reddens here, which is the gate's own claim, and the
       gate is not vacuous on absence either** -- a missing key or a missing block gives
       `None is False` and fails. `is False` also refuses the quoted string, which is
       the safe direction, since GitHub reads a non-empty string as truthy
```

**The hole, found by inverting the direction (EH4's weakening side):**

```
claim  a job-level concurrency block that cancels, beneath a workflow-level `false`
cmd    inject `concurrency: {group: job-${{ github.ref }}, cancel-in-progress: true}`
         into the first job of the workflow; run the whole file
out    tests/test_ci_workflow_is_wellformed.py      8 passed
rule   the gate reads `_doc().get("concurrency")` -- the top-level mapping only
judge  **the behaviour GF3 (c) forbids is reachable with every assertion in the file
       green.** No job-level block exists today, so nothing is wrong now
```

**Why it does not block.** FR1's second class verbatim â€” a needle too narrow where no wrong result follows â€” and EK2 forbids widening the guard. A2 and A3 are the over-strict direction and are **not** a defect: GitHub's default for an absent key is already `false`, so the gate pins the literal rather than the behaviour, which is the right choice for a gate. *Closed when* nothing, under EK2. **R2, one line.**

### R1187. CI AT THE JUDGED COMMIT, AND THE PART OF IT THAT IS NOT A BOUNDARY STATE: NO CONCLUDED RUN HAS EVER COVERED THE INVERTED GATE OR THE REGENERATED GOLDEN.

**There IS a run at the judged commit and it has not started. That is neither CK0-by-design absence nor CK2's exhausted allowance** â€” `8985a0a` touches `docs/digests/**`, which is NOT in `paths-ignore`, so the workflow accepted it and created run `42762822199`. It is `pending` with **zero jobs** at 06:35 UTC, when I ruled -- one hour and three minutes after the push -- queued behind the run at the tag commit, whose ladder job was still on rung 6 at the same moment. That is R1188. **I did not wait on a machine: I measured the whole suite and the whole ladder myself instead**, which is what verdict 55 did at this same boundary and for the same reason. **A run that has not finished is not a pass**, so I record it as unavailable rather than skipping it, and I judge the commit on everything else â€” which I can do precisely, because the `tests/` delta is two files:

```
claim  what CI has concluded on, and exactly which part of this tree it has never seen
cmd    git diff --name-only 82842ae..8985a0a -- tests/unit tests/verification
         tests/regression tests/corpus tests/goldens "tests/*.py"
out    tests/goldens/collected_tests.txt
       tests/test_ci_workflow_is_wellformed.py
       -- and NOTHING under tests/unit, tests/verification, tests/regression or
          tests/corpus: 0 files each
cmd    gh api .../actions/runs/42600509104/jobs   -- at 82842ae, the last CONCLUDED run
out    the verification ladder     completed  SUCCESS  -- all six rungs
       lint, unit and guards       completed  failure  -- the EG3 eight, traced in section 0c
cmd    gh api .../actions/runs/42761104562/jobs   -- at a780a9d, the TAG commit
out    lint, unit and guards       completed  failure
         actionlint, ruff, black --check, mypy, unit tests  ALL success -- none skipped
         guards and meta-tests     FAILURE: 8 failed, 1339 passed in 687.26s
         -- the same eight ids as my own run, set-identical, only-in-CI none
       the verification ladder     in_progress on `ladder 6`; rungs 1, 2, 3 success,
                                   rungs 4 and 5 pending -- NO RESULT for this job
       CI determinism (both)       skipped by their own condition -- unavailable, not passing
cmd    gh run list --commit 8985a0ae223a030f5d1468ca8c1e173909959083 (the FULL 40, GF3 d)
out    [{"databaseId":42762822199,"status":"pending","conclusion":""}]
rule   CA2 -- a red CI is red; CK2 -- an unavailable run is neither; GC2 -- an ancestor
       run evidences a commit whose diff to it lists only paths the run cannot see
judge  **CI has concluded on every test in this tree EXCEPT the two files `d8ee517` and
       `438f2db` changed**, because `tests/unit`, `tests/verification`, `tests/regression`
       and `tests/corpus` are byte-identical to `82842ae`, whose ladder was green on all
       six rungs on a machine neither of us controls. **So the inverted gate assertion
       and the regenerated golden have NEVER RUN IN CI, at any commit.** I measured both
       myself at the judged commit instead -- the four root guards plus both files that
       read the workflow, **232 passed, 0 failed**, including this gate's own 8 and the
       golden guard's 105 -- and lint at the judged commit in my own clean worktree:
       `ruff` `All checks passed!`, `black --check` `128 files would be left unchanged.`,
       `mypy` `Success: no issues found in 45 source files`
```

**Why this does not HOLD on its own.** The only CI red anywhere in the window is `guards and meta-tests` at `a780a9d`, and all eight of its ids satisfy the FS1/FT1 predicate by my own measurement below, so CA2's "a red CI is a HOLD" is not reached and CZ1 (iv) does not arise for them. The pending run is CK2-adjacent â€” unavailable, not red â€” and the ladder job at the tag commit is unavailable too. **What I will not do is call any of it a pass.** *Closed when* a pushed run covering `tests/` and `.github/` is seen to conclude with `guards and meta-tests` reaching the runner and reddening on nothing but the boundary set.

### R1188 (ledger). GF3 (c) TRADES "A RUN IS VOIDED" FOR "THE JUDGED COMMIT'S RUN HAS NOT STARTED", AND THE LEVER THAT WOULD AVOID BOTH IS THE ONE LINE GF3 (c) DID NOT TOUCH.

**The before/after pair is real and I measured both sides**, which you had done once and in one direction. **I also correct the mechanism, because the ablation is not the one the commit message describes:**

```
claim  cancel-in-progress's effect, as a controlled pair over four real runs
cmd    gh run list --branch F3 --json databaseId,headSha,status,conclusion,createdAt
out    42590412570  4750f07  completed  CANCELLED   09:03 -> 10:23  (82842ae pushed 10:23)
       42608004706  b286e01  completed  CANCELLED   11:18 -> 11:19  (4e5d57e pushed 11:19)
       42761104562  a780a9d  in_progress            05:16 -> ...    (8985a0a pushed 05:32)
       42762822199  8985a0a  PENDING, zero jobs created
cmd    git show a780a9d:.github/workflows/ci.yml | grep -n cancel-in-progress
out    43:  cancel-in-progress: true
cell   ONE VARIABLE -- the `cancel-in-progress` of the SUPERSEDING (pushed) commit.
       a780a9d's OWN workflow still says `true` and its run was NOT cancelled, so the
       setting that governs is the new run's and not the in-flight run's
rule   GF3 (c), and R449 -- a cancelled run is `completed` with NO RESULT
judge  **the claim holds, and the mechanism is sharper than the commit message states:
       the superseding commit's workflow is what decides.** That also means a revert
       takes effect on the next push, so the gate above protects a live setting
```

**What nothing in the repository records is the cost, and it is not Actions minutes.** `concurrency.group` is still `ci-${{ github.ref }}`, so `cancel-in-progress: false` does not mean *runs proceed in parallel* â€” it means **they queue**. Measured: fourteen minutes after `8985a0a` was pushed its run had **zero jobs created**, while `a780a9d`'s ladder was on rung 6 with rungs 4 and 5 still pending. **FP1's guarantee and CZ1 (iii) therefore serialise at roughly 50-85 minutes per queued run**, and a step that pushes a series of commits puts the judged commit's run hours behind HEAD. GF3 (c) named the *setting*; the line that produces the queueing is the *group*. A per-sha group would give GF3 (c)'s stated goal with no queue at all. **I am not asking for that repair**: it is a workflow decision with an Actions-allowance side (CK0) and it is Xabier's, not a round's. **Ledger: no number in any artifact is wrong, so FR1's sentence cannot be written.** *Closed when* the trade is recorded where the setting is, or the group is ruled on. R2.

### R1189 (ledger). THREE SENTENCES â€” ONE IN THE SOURCE TREE, TWO IN PUBLISHED DELIVERABLES â€” ARE TRUE, AND NONE CARRIES ITS COMMAND.

I verified all three. None is false; each is a BF0/CW0/BP0 form defect and FR1's sentence cannot be written for any of them.

* `.github/workflows/ci.yml:15-22` â€” the CK0 block asserts *"a push of mine cancelled the run a REVIEWER WAS READING, at 4750f07 and again at b286e01"*. That is prose in the source tree claiming something about this repository, which CW0 says is a test, a triple, or deleted. **It is TRUE** â€” both runs read `conclusion: cancelled` in R1188's table â€” and no triple accompanies it.
* `docs/digests/2026-11-09.md`, the GF4 block â€” *"CI's verification ladder green including rung 6 over all of tests/regression"*, attached to the tag commit. **True of the tag commit's CODE, not of its own run**: `git diff 82842ae..a780a9d -- . ":(exclude)docs"` is **empty**, so the green ladder at 82842ae does describe that tree â€” which is exactly the GC2 ancestor rule adopted in the same turn, and it is not cited here. The ladder job at a780a9d had not concluded.
* `docs/closure/R1.md` Â§ 0d â€” *"tests/test_ci_workflow_is_wellformed.py asserts cancel-in-progress is True"*, present tense: true inside the tag, false at the judged commit. The paragraph is explicitly forward-looking about the rename, so a reader is not misled.

*Closed when* the first carries a triple or is cut back to the measurement, and the second cites GC2 with the diff listing. The follow-on commit or R2, implementer's choice.

### R1190 (ledger, and the probe is MINE). THE EIGHT DO NOT CLEAR ON A NEWER REPORT COMMIT â€” ONLY ON ONE THAT ANSWERS VERDICT 55. THE ARTIFACT IS WORDED CORRECTLY; A READER COULD TAKE IT THE OTHER WAY.

I ran the control the implementer may not run, because EK3 forbids touching a closed report in the real tree:

```
claim  whether a commit touching the step report clears EG3 state (2)
cmd    in a worktree of mine at 8985a0a: append one comment line to
         docs/reports/R1/step-4.md, commit, run the two report-guard files
out    9 failed, 394 passed -- the same eight PLUS
         test_the_answered_verdict_is_the_NEWEST_one
cell   one variable -- one commit touching the report, with no header changed
judge  **a newer report COMMIT does not clear them; it adds a ninth.** The condition is
       the report's Answers: header naming verdict 55, which is what sections 0b and 0d
       actually say and what EG3's sharpening means by "cleared BY THE ANSWERING
       REPORT". The published wording is right; the mechanism is stricter than
       "the moment R2's first report exists" reads to someone skimming
```

**And my second probe was INCONCLUSIVE and I record it as that rather than drawing from it.** A stub revision carrying `Answers: verdict 55` gave `241 failed, 162 passed` â€” the stub's own defects, not a measurement of the base case â€” and among them a new `test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]`, which is EG3 state (1) arriving as state (2) leaves. **So I did not verify GF2's base case end to end, and nothing inside R1 can**: it needs a real R2 report. *Closed when* R2's first report lands and the eight are measured at it â€” EG3 (ii) from the implementer's side, one more time.

### R1191. GF3 (a) REACHED THE FILE BUT NOT THE REVIEWER. A FINDING ABOUT THE PROCEDURE, FOR XABIER, NOT FOR THE IMPLEMENTER'S TREE.

GF3 (a)'s procedure is in `.claude/agents/gating-supervisor.md` at the judged commit; I read the diff and it is there, correct, and additive. **The agent definition loaded into THIS invocation is the pre-793e45b text**: it still reads `git worktree add <path> <sha>` with no `-b`, and it still carries *"How your verdict then reaches branch F<n> is NOT settled"*. I used the new door because the invocation message told me to, and it worked; a reviewer invoked without that message would have followed the old text and written in the implementer's tree.

**Why this is worth a line rather than nothing.** `CLAUDE.md` makes an unnoticed edit to these files a STOP-class finding precisely because *"a reviewer cannot be relied on to notice an instruction that is no longer there"*. The converse is now measured: **a reviewer cannot be relied on to notice an instruction that has just arrived.** An edit to the agent file does not take effect for a subagent already launched, so a `process:` commit's effect on the reviewer is delayed by at least one session. **This is not a defect in 793e45b**, which did exactly what GF3 (a) authorised. *For Xabier:* the first invocation after a change to the reviewer's instruction files should say so in the invocation, as this one did.

### R1192 (ledger). THERE IS A SIXTH "STEP 5" SENTENCE. IT IS LIVE, UNMARKED, AND IN THE SAME FILE THAT LATER SAYS IN BOLD THAT THERE IS NO STEP 5 â€” AND THE CENSUS THAT WOULD HAVE FOUND IT IS ONE CHARACTER WIDER THAN THE ONE THAT WAS RUN.

`docs/digests/2026-11-09.md:157`, in the live `## CZ1 at the closure commit` section â€” not inside the struck `Tomorrow` block, not quoted, not dated:

```
claim  every live, unmarked "step 5" assertion about R1 in this tree
cmd    grep -rniE "step 5|step-5|step five" --include=*.md . | grep -v ./docs/reports/
         | grep -v ./docs/reviews/ | grep -v ./.venv/
out    docs/digests/2026-11-09.md:157  "... it clears when step 5's report answers
                                        verdict 55, so repeating the measurement would
                                        reproduce the same eight forever"
       docs/digests/2026-11-09.md:172  inside the struck Tomorrow block -- marked, fine
       docs/digests/2026-11-09.md:222  the SUPERVISOR.md observation -- accurate
       docs/SUPERVISOR.md:155          R2 ledger row 10 -- correctly routed, not edited
       docs/closure/R1.md 181/364-390/867/883   all GF1/GF2's own corrections
       CLAUDE.md, docs/closure/F*.md   other milestones' step 5, which exist
rule   GF2: "all five routed the eight boundary reds to step 5's report ... all five are
       corrected in place"
judge  **five were corrected and there are six.** The sixth is in the paragraph whose
       next bold sentence is "The recursion has no base case" -- which GF2 supplied a
       base case for, in the commit before this file was last edited. **Nineteen lines
       below it the same file says "There is no step 5" in bold.** GF1's needle was run
       over `docs/milestones/R1.md`; the sentences it was about live in `docs/`
```

**Why it does not block.** A digest is reporting (FZ: *"Reporting is a daily digest"*), so this is FR1's third class â€” report prose â€” and no number in it is wrong. **I am recording it because of its shape, not its cost:** it is the census-needle species this milestone opened with (R755) and closed its first finding on, and the one-character fix to GF1's own needle â€” the directory instead of the file â€” finds it. *Closed when* the sentence is struck or dated in place like the two above it, and the paragraph's "no base case" bold is marked as superseded by Â§ 0d. **One line each, in the follow-on commit with R1185.**

### R1193. GF3 (e) FIXED ONE OF THREE COPIES OF THE CORPUS-PAUSE CLAUSE. THE TWO IT DID NOT FIX ARE THE REVIEWER'S OWN INSTRUCTION FILES, AND ONE OF THEM NOW CITES A `CLAUDE.md` HEADING THAT NO LONGER EXISTS.

This is the C45 drift, on the same clause, created by the repair of C45's other half â€” and **I am the measurement**: my loaded instructions told me the pause was in force and I had to rule under `CLAUDE.md` against them.

```
claim  where the corpus-pause clause lives, and what each copy says after GF3 (e)
cmd    grep -nc "^### Corpus batches pause until 28 October" CLAUDE.md
out    0        -- the heading is GONE; GF3 (e) renamed it
cmd    grep -n "^### .*corpus pause" CLAUDE.md
out    551:### The corpus pause EXPIRED on 28 October and was left expired (EG4(e), GC3)
cmd    grep -n "^### Corpus batches pause until 28 October" docs/SUPERVISOR.md
out    748:### Corpus batches pause until 28 October (EG4(e))
         -- a LIVE section, unmarked, undated, verbatim the clause GF3 (e) expired
cmd    sed -n '762p' docs/SUPERVISOR.md
out    otherwise stands.   (".. this applies from F4's load-mapping gates on; the
                            corpus pause above otherwise stands.")  -- a SECOND live
                            assertion, in EH4's section
cmd    grep -n "paused.*28 October|Corpus batches pause until 28 October" .claude/agents/gating-supervisor.md
out    287:  corpus batches are **paused** until 28 October, except mutation
       389:  two exceptions are `CLAUDE.md` section "Corpus batches pause until 28 October
rule   the agent file's own FE1 note: "a citation to a document that does not state a
       rule would delete it", and C45 -- "four consecutive verdicts reported the drift"
judge  **three copies, one fixed.** `:287` asserts the pause is IN FORCE, which is false.
       `:389` cites the `CLAUDE.md` section BY ITS OLD HEADING, which resolves to
       nothing -- or, worse, to the quoted historical block, which states the clause as
       if live. `docs/SUPERVISOR.md:748` carries the whole dead clause as a live section
       and `:762` leans on it. **GF3 (e) says "CLAUDE.md corpus-pause clause"; the clause
       was in three files**
```

**Why it does not block, and why it is not a ledger row either.** No number is wrong and no input is used other than as declared, so FR1's sentence cannot be written. But **FF0 puts a closure item in the gating apparatus in the next commit rather than on the ledger** â€” *"anything that reads the gating record, or decides whether a green is believed"* â€” and what the reviewer may spend a round on is exactly that. **And the implementer may not fix it unilaterally**: `CLAUDE.md` says these two files change only in a standalone `process:` commit citing the directive asking for the change, and GF3 (e) names `CLAUDE.md`. **That is the finding's point, not an obstacle to it** â€” the repair needs one line from Xabier extending GF3 (e) to its other two sites, and asking for it is cheaper than a round.

*Closed when* `docs/SUPERVISOR.md:748-755` and `:762` and `.claude/agents/gating-supervisor.md:287` and `:389` say what `CLAUDE.md:551` says, in a standalone `process:` commit citing whatever authorises it.

## Which criterion I ruled under

**FR1 with EZ0, and I say why rather than leaving the choice silent, because you asked.** The commits under review exist to close R1 â€” GF1 through GF4 are R1's own closing â€” so the criterion in force for the rest of R1 is the criterion that governs the act of closing it. R2 has not opened, so CZ0's un-narrowed form has no step to govern, and applying it here would judge R1's closure under a criterion R1 was not executed under.

**It changes two calls and I state both.** Under CZ0 (a) as amended by EZ0, R1189's three sentences would be in the blocking class â€” a defect in a published deliverable â€” and under CZ0 (c) R1186's job-level hole is at least arguable as a gate that does not claim what it appears to. Under FR1 neither can be given the silently-wrong-result sentence, so both are ledger rows. **R1185 blocks under both.** I do not disagree with the criterion and I am not asking for it to move.

## Tolerances touched

**None.**

```
cmd    git diff dc49552..8985a0a --numstat -- floatfea/tolerances.py tests/conftest.py
         "tests/**/conftest.py"
out    (empty)
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py
cmd    git diff --stat dc49552..8985a0a -- floatfea results examples scripts data artifacts
out    (empty)
judge  no tolerance, no counter, no conftest, no module and no published engineering
       deliverable moved in the whole window. EU1 does not arise; the adversarial case
       was run anyway, for the gate assertion, and it is R1186
```

## The three things you asked me to attack

**1. The inverted gate (d8ee517): it carries its own failure and the revert reddens.** R1186's first block â€” four arms, one variable each, restored between every one. The one hole is job-level and is a ledger row. **The behavioural half is R1188**, where I measured both directions and sharpened the mechanism.

**2. The golden (438f2db): verified against COLLECTION, both directions, and nothing else moved.**

```
claim  the golden against what the tree actually collects, and the old-vs-new set diff
cmd    the generator's own collected(root), per root, at 8985a0a, in my worktree
out    [tests]            golden 931  collected 931
       [tests/unit]       253 / 253
       [rung1]             61 / 61
       [rung3]             92 / 92
       [rung4]            101 / 101
       [tests/regression] golden 193  collected 193
       recorded-but-NOT-collected: none in every root
       collected-but-not-recorded: none in every root
cmd    parse d8ee517's golden against 438f2db's, section by section, as sets
out    [tests]            930 -> 931  removed: 1 (test_a_superseded_run_is_cancelled)
                                      added:   2 (the NOT_cancelled rename, and the
                                                  R1156 test)
       [tests/regression] 192 -> 193  removed: 0  added: 1 (the R1156 test)
       every other section            removed: 0  added: 0
       declared count == actual line count in all six sections, before and after
cmd    git log --oneline -S <the R1156 test name> -- the gate file ; then
         git log --oneline a596fa7..8985a0a -- tests/goldens/collected_tests.txt
out    a596fa7 fix: R1156 -- the published C_m caveat named the WRONG CLAUSE ...
       438f2db (the only commit)
judge  **931 and 193 are collection facts and not arithmetic**, and nothing disappeared
       under cover of the rename: exactly one removal, in exactly one section. The R1156
       addition landed in a596fa7 and the golden was untouched between then and 438f2db,
       so this IS the first regeneration since and the one-directional guard never
       needed it. **No rule was bent and your account of it is exact.** The golden is
       now complete in BOTH directions, which it was not before
```

**2b. AND THE GUARD THAT LICENSES 438f2db CARRIES ITS OWN FAILURE, IN BOTH DIRECTIONS.** The whole case for `438f2db` rests on `test_collected_set_golden.py` being one-directional, and nothing in this repository had measured that it is:

```
claim  the golden guard reddens on a removal and stays green on an addition
cmd    in a worktree of mine at 8985a0a, one variable per arm, restored between each:
         delete one test function from tests/test_one_gravity.py; then instead ADD one
out    C0  baseline                              105 passed
       C1  one function DELETED                  1 FAILED, 104 passed
             test_every_recorded_test_is_still_collected[tests]
             assert not ['tests/test_one_gravity.py::test_NO_gravity_literal_...']
       C2  one NEW function ADDED                105 passed
       C3  restored                              105 passed
rule   the guard's own docstring -- "ONE-DIRECTIONAL on purpose: a new test is not the
       failure mode" -- and `CLAUDE.md` section Testing on a rename being a removal
       plus an addition
judge  **both directions hold.** So the R1156 addition genuinely needed no ceremony and
       the rename genuinely needed its own commit, which is what `438f2db` did. The
       guard is not vacuous: it names the exact id that went missing
```

**3. The closure artifact (a780a9d): one blocking finding, and the fifth stale figure you told me to assume is R1185 â€” it is a derivation and not a measurement.** The triples I re-ran all reproduce: GF1's four step headings and `step 4 -> 3 / step 5 -> 0` on the `-E` needle with its control; GE1's `3` witness runs and three appendices; Â§ 8's `10` rows and `4` struck rows. The `R1` tag is annotated, reads `R1: tool ready`, points at `a780a9d50de4d60a8312e425541a83dc11bb1d04`, and `git ls-remote --tags origin` shows it pushed. **GF1 is right: `docs/milestones/R1.md` Â§ 3 lists four steps and there is no step 5.** The five corrected step-5 sentences are each corrected in place and each says so.

## The EG3 eight, ruled per id against the FS1/FT1 predicate â€” my measurement, not your group

**You told me not to take the group from you, so I did not.** I measured the set at three commits and against CI, and I tested the predicate per id.

```
claim  the eight are verdict-dependent, measured rather than classed by family
cmd    the two report-guard files, in three worktrees of MINE, one variable --
         whether a verdict newer than the newest report revision exists
out    dc49552  report written, verdict not yet     403 passed, 0 failed
       d5add31  verdict written, report not yet     8 failed, 395 passed
       8985a0a  the judged commit                   8 failed, 395 passed  -- the SAME ids
       (+ test_report_numbers_are_sourced.py 29 passed at the judged commit,
          so the guards half is 8 failed, 424 passed of 432 -- which is exactly the
          figure section 0c publishes, reached independently)
cmd    CI's own FAILED list at a780a9d, run 42761104562, step `guards and meta-tests`
out    8 failed, 1339 passed in 687.26s -- the same eight ids.
       only-in-CI: none.  only-local: none
cell   ONE VARIABLE between the first two arms -- the verdict file. Same two files,
       byte-identical; 403 = 8 + 395, so the denominator is held
rule   FS1 with FT1: limb one -- the red names a finding or a site of the newest
       verdict; limb two -- its SUBJECT is the commit carrying it
judge  `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` -> **LIMB TWO**, which FT1 names
       by id and for the reason that applies here: its message is that the round's table
       has no run row, and no run row can exist for a commit before it is pushed.
       The seven `test_the_guard_survives_the_state[...]` ids -> **LIMB ONE**, on the
       control above and on R813's precedent that limb one is a REASON and not a
       mention -- `test_the_R507_cases_rule_as_measured[frames.txt]` named no verdict in
       its failure line either and CLAUDE.md rules it limb one.
       **All eight satisfy the predicate. CZ1 (iv) does not arise for them, and CA2's
       "a red CI is a HOLD" is therefore not reached.**
```

**And the count is SENSITIVE at nine, which I measured rather than assumed** â€” the hazard EG3 (i) exists for is a real defect sitting inside a group nobody reads individually (R629). My R1190 probe put a ninth red into the same two files and **it appeared by name** (`test_the_answered_verdict_is_the_NEWEST_one`), so a ninth would not hide behind the eight. **I did not rule any of them as a cascade by class.**

## Corpus (ES0's light clause, and GC3)

**No batch, and the reason is the clause and not the pause.** The `CLAUDE.md` pause **expired on 28 October and GC3 left it expired**, so batches are at my discretion â€” but **ES0 makes an interim check light and says "no corpus batch" outright**, and that is what I ruled under. **The pause did not hold because it no longer exists**, and I say so because my own two instruction files still describe it as in force while `CLAUDE.md` governs â€” which is R1193, found by this sentence.

**What I ran instead.** The recorded substitute is a continuum grid over the parameter space a decision rule guards, and a regeneration check on a published deliverable. **The grid is not available and I say why rather than substituting silently**: the decision rule under review is a boolean YAML key, so there is no parameter space to grid. **The regeneration check I DID run**, because a null expectation is still a measurement:

```
claim  the published deliverable regenerates at the judged commit
cmd    python -m floatfea.cli run examples/platform12_placeholder.yaml in my worktree
         at 8985a0a, then git diff -- results/R1/example
out    member_forces.csv, utilisation.csv   BYTE-IDENTICAL
       report.md        3 lines: build 0.12 -> 0.15, solve 64.40 -> 96.48,
                                 total 64.52 -> 96.63
       governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
rule   R850's known exclusion -- the wall-clock table is the only permitted drift
judge  **every physical number in all three artifacts regenerates byte-identical**, and
       the headline reproduces exactly. The only drift is the wall-clock table, already
       on the ledger
```

Beside it: **five injections on the gate assertion** (four defeats plus the job-level hole), **a controlled four-run pair on the behaviour the directive claims**, **the golden against live collection in both directions per root AND the golden guard itself proved to redden on a removal and not on an addition**, **two probes of the EG3 base case that no commit of the implementer's may run**, and **a full census of live "step 5" assertions across the tree**. Four of those six produced findings (R1186, R1188, R1190, R1192). `tests/corpus/` is unchanged: **0 new entries, so the coverage number is 0 of 0 and I am not reporting a count I did not measure.**

## Next step opens when

**STEP 4 IS CLOSED AND R1 IS CLOSED. THIS VERDICT REOPENS NEITHER, AND IT MUST NOT BE READ AS DOING SO (DD1).** Step 4's disposition is verdict 55's `Closes: R1/step-4`; R1's is GF2 and the pushed `R1` tag. **The HOLD is on one sentence in `docs/closure/R1.md` Â§ 8**, discharged by a follow-on commit â€” CZ1 (iv)'s shape, EB4's cost, which is none. If the `Stop` hook reads this header and refuses, DD1 is the rule the disagreement is resolved against and this paragraph is the record of it.

1. **R1185, in one follow-on `closure:` commit.** Â§ 8's header and `rule` line corrected to **two** of item 3's ten closed by GF3, with the other two struck rows' sources named. **Nothing else in Â§ 8 needs touching** â€” the ten rows and the four struck rows are right, row by row, and re-auditing them is not what this asks for.
1b. **The three prose fixes that belong in the same commit, because they are in the same two files and cost nothing extra:** R1192's sentence at `docs/digests/2026-11-09.md:157` and the "no base case" bold above it; R1189's workflow comment and its digest ladder sentence. **These are FR1's third class and do not block** â€” they are here because a second commit for them is more expensive than the lines themselves.
2. **CZ1 (ii) and (iii) at that commit**, with the full 40-character sha (GF3 d), and any red traced by name per id under EG3 as Â§ 0c already does.
3. **R1187's open half, which effort cannot close.** The judged commit's run and the tag commit's ladder job are not the implementer's to hurry; what is owed is that the next pushed run covering `tests/` and `.github/` is seen to conclude, and that the inverted gate is seen to pass on a machine neither side controls â€” because at the moment it never has.
4. **To R2 or to Xabier, and nothing inside R1 reaches them:** R1186, R1188, R1190, R1191, R1193, and whatever of R1189 and R1192 the follow-on commit does not take, plus Â§ 8's own ten rows. **R1185's repair does not change that list**; it changes the sentence that derives it.
5. **R2's first report answers verdict 55** and measures the eight at its own commit, which is EG3 (ii) from the implementer's side. **R1190 is the warning that the `Answers:` header is the load-bearing part**, not the commit.

**On SR-72, which you asked me to rule: you were right, and it is not FZ (d).** FZ (d) escalates *anything needing a standing constraint broken*. The split breaks none; the **unsplit** reading would have broken one, and `CLAUDE.md` calls that a STOP-class finding in its own words. GF3's "one standalone `process:` commit" is a packaging instruction, not one of FZ's six escalation triggers, and one standalone `process:` commit does exist at `793e45b` holding exactly the items that need it. FZ rule 7 is the right instrument and no published number differs between the readings. **I would have done the same**, and had you escalated it I would have said that instead.

**On GF3 (b), which you asked me to check rather than take: the repair states GC2 CORRECTLY.** `CLAUDE.md` Â§ *The judged commit always has a CI run* now quotes GC2, and I diffed the quote against `docs/directives/GC.md:38-43`: verbatim to the rewrap, including the conditional â€” `git diff --name-only <ancestor>..<judged>` lists only paths-ignored paths â€” and the three things the report must state. The surrounding sentence is accurate too: `docs/reports/**` is in the workflow's `paths-ignore`, which is why the report-only tip commit is the case it covers. **And `docs/directives/FP.md` is correctly left unedited** â€” amending a verbatim record stops it being one â€” with `docs/directives/README.md` recording that choice and its reason. SR-70 is closed and recorded as your own error in both places. I spent no finding establishing it, as you asked.

**On the schedule.** FW0's 10 November holds and R1 closed inside it, on 9 November, full scope with FT2.7 included. The one blocking item is one sentence and costs no round under ES0 and EB4.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4
Reviewed commit: dc49552fd719067d8482a104d47b6cd008a6608e
**Reviewed commit: `dc49552fd719067d8482a104d47b6cd008a6608e`.**
Closes: R1/step-4
Verdict: PASS
Scope: **R1 step 4, REVISION 4 at `dc49552` -- a REVIEWED REVISION, so this CONSUMES A ROUND. Step 4 stood at 2 of 3 and stands at 3 of 3 (ES0), so the step CLOSES here and this verdict carries `--closes R1/step-4`** (FK1). The increment is NOT closed: `docs/closure/R1.md` has no closure commit, and CZ1 (ii)/(iii) re-take its figures at one. The report carries `# Revision 4` / `Answers: verdict 54 @ 5f02798`, which names the NEWEST verdict, so the 1b check passes and I say so rather than leaving it silent. Ruled under **FR1 with EZ0**. **No finding blocks, and for each I tried to write FR1's sentence and could not** -- that is one line each rather than a round, which is what FR1 asks for. **GE3: `R835: unchanged, R2`. Not re-measured.** GA3's 150-line target is OVERRUN at 317 lines and I am saying so rather than trimming the evidence: the overrun is six injection and sweep cells, the complete numeric census of the caveat, the ladder I measured myself because CI's had not finished, and six ledger findings each carrying its own closing condition. GA3 says the target does not limit what I may rule.
Tests: **4393 passed, 0 failed, 0 skipped AT THE JUDGED COMMIT, MY OWN RUNS, in EI0's two halves, in clean worktrees of my own (FV2), `-p no:randomly`, PYTHONPATH unset.** The main half **3961 passed, 0 failed, 0 skipped in 2914.51s (0:48:34)** and the three report-parametrised files **432 passed, 0 failed in 93.21s**. **432 is exactly the report's section 11 figure at its own state, measured independently by me**, and I also measured **430 at `4750f07`**, which confirms the report's cell that the figure moved when section 10 was added and is not a flake. Lint at the judged commit: `ruff` `All checks passed!`, `black --check` `128 files would be left unchanged.`, `mypy` `Success: no issues found in 45 source files`. **ZERO REDS ANYWHERE, so neither EG3 boundary state arises, the FS1/FT1 predicate is not reached, there is no `FAILED` list to classify and CZ1 (iv) does not arise.** Third consecutive boundary with nothing to classify.
Door (FV2/GE4): **every measurement below was taken in `git worktree`s of my own** under the session scratchpad -- one kept clean for the suite at `dc49552`, one for every injection, one at `4750f07` -- so each restore ran in MY tree and the implementer's was never written by a probe. In `C:/dev/floatfea` I ran read-only `git` and `gh`, **plus the two writes FV2 gives me no other door for: the corpus commit `173c64c` and this verdict.** Both touch one reviewer directory, one file each; `git status --porcelain` was empty before and after. **That is the standing escalation in `docs/SUPERVISOR.md` section FV2, now in its fourth consecutive round. It needs Xabier, not another round, and I am not inventing a procedure for it.**

## Carried

* **R1178 -- ANSWERED AT ALL FIVE SITES, AND I ATTACKED IT RATHER THAN READING IT.** The condition set and its contrapositive are gone from `floatfea/cli.py:111-137`, from all three artifacts and from both `docs/USER_GUIDE.md` paragraphs, and what replaces them is the closed form rather than a sixth rewording. **I measured the form rather than reasoning about it**, over a population neither of us chose:

```
claim  the published sentence -- the column is EXACTLY THE LARGER OF B AND a + C_m*s,
       NON-DECREASING, FLAT below the kink at C_m = (B - a)/s, flat across the whole
       declared domain when (B - a)/s exceeds 2.0, and flat at every C_m whatsoever
       only when s = 0 -- on members its author did not choose
cmd    60000 random tubulars, D 0.3-3.0 m, D/t 15-320, KL/r 10-200, biaxial moment,
       both shears, torsion; 17614 admissible COMPRESSION cases; each evaluated at 13
       C_m from 0.1 to 100 and fitted against max(B, a + C_m*s)
out    closed-form violations (rel > 1e-12)            0      worst rel 4.35e-16
       monotonicity violations                         0
       kink <-> flat-across-0.1..2.0 mismatches        0
       s == 0 <-> flat-at-every-C_m mismatches         0
rule   the sentence as shipped in cli.py and in the commented header of both CSVs
judge  the first of the six versions of this sentence that a member cannot refute.
       The precondition is in the code and not in the sentence: f_a >= f_e RAISES, so
       s >= 0 always and the column cannot fall. I constructed that refusal
       (slender_near_euler_refusal, KL/r 195) rather than assuming it
```

* **R1178's remaining universal, attacked as you asked, and IT HOLDS.** `s = 0` iff flat at every C_m is above, 0 mismatches, and the zero-moment fixture is flat at `C_m = 1e9`. The kink sentence is true from BOTH sides of BOTH ends (EH4), solved not sampled: kink `2.0000001` flat, kink `1.995` and `1.9999999999` not flat, kink `0` rising from the declared floor up. **Your published digits reproduce exactly** -- `0.818471 -> 1.639720`, kink `0.980652` (`0.98`), the fixture's kink `3.040895` (`3.04`), `5.0e8/1.65125628e8 = 3.0280` (`3.03x`), the guide's factor `2.003394` (`2.0034`). **And the one existential the caveat states with a specific label is true for that label**: a row reading `3.2.4 beam shear` AND `simple` at `0.85` -- `shear_y_n = 7.58716187e+07`, `U = 0.814537` -- reads `3.3.2 interaction` at `2.00` with `U = 1.639720`. **No seventh correction is needed and the pointer-to-the-guide remedy is not called for.**
* **AND THE CENSUS OF THE CAVEAT'S NUMBERS IS COMPLETE RATHER THAN SAMPLED**, because a sample is how a stale figure survives:

```
claim  every numeric token the shipped caveat publishes, and whether I reproduced it
cmd    re.findall on floatfea.cli.TABLE_CAVEATS' C_m entry, the whole string
out    15 distinct tokens: 0, 1, 2, 4 (in `s = 0`, `1 - f_a/F_e'`, the clause numbers);
       3.2, 3.3 (clause prefixes); 0.1 and 2.0 (MOMENT_REDUCTION_CM's declared bounds);
       0.85 (the tabulated value); 2.00; 0.98; 3.03; 3.04; 0.818471; 1.639720
judge  the five that are MEASUREMENTS are 0.98, 3.03, 3.04, 0.818471 and 1.639720, and
       I reproduced all five -- 0.980652, 3.0280, 3.040895, and the two exactly. The
       rest are structural. NOTHING in the caveat is a figure I did not re-derive
```
* **L1, L2, L3, L4 -- ANSWERED and re-measured by me, not accepted.** L1: the caveat names six (`R743 / R1156 / R1162 / R1168 / R1174 / R1178`) and the artifact now READS the count from the caveat. L2: `grep -c "not-a-tolerance: EXACT equality"` is `6`. L3: label and paragraph both say `566ef94`. L4: `density > basis.RHO_STEEL` is at `floatfea/model/platform.py:878`. **And the L3 repair published a fifth figure of the same class in the same block -- R1179 below.**
* **L5 -- CORRECTLY NOT ACTED ON.** One line under GA1, no census, no guard extended, and the phantom not guessed into an `HSP:` prefix (SR-66). R2.
* **L6 -- ANSWERED**, in revision 4's text with EK3's mechanical reason given rather than by touching revision 3.
* **L7 -- WITHDRAWN, AND I REPRODUCED THE WITHDRAWAL RATHER THAN ACCEPTING IT. The withdrawal does NOT overreach.** My own run, `rho: 7000.0`, absolute paths, output outside the repository:

```
claim  a reader at a non-default rho can tell which reference each body list used
cmd    my own run at rho 7000; every line of the generated report.md naming a density
out    :56-62  hub1..hub4: the equivalent density is 11433.5 kg/m^3, ABOVE steel at 7850.
       :110    rho was declared as 7000 kg/m^3 (nominal) ... Equivalent densities:
                 hub1 11433.5, hub2 11433.5, hub3 11433.5, hub4 11433.5, platform 7146.0
       :111    DZ5 / ER1(e): hub1, hub2, hub3, hub4, platform carry an equivalent
                 density ABOVE the declared nominal
judge  the DISCRIMINATING row is `platform` at 7146.0 -- in the second list and not the
       first -- and the reader has 7000 on the line IMMEDIATELY ABOVE and 7850 inside
       the first sentence. Nothing is ambiguous. Your L7 is right and my predecessor's
       premise was wrong; the item is closed by the tool and belongs off R1's open list
```

* **L8 -- one line, no action, as ruled.** Re-measured by the report and the coverage is where the verdict said: rung 5, not the gate.
* **L9 -- the reviewer's own; no action owed.** Fail-loud.
* **Item 3 of verdict 54's conditions -- CI at revision 4's own commit: UNAVAILABLE, not red (CK2), and I record it as that rather than skip it.** See `## CI` below.
* **Item 4 -- DISCHARGED, and by my own runs rather than the report's.** Both halves at the judged commit, above.
* **Item 5 -- "nothing else of substance" HELD.** The diff is one sentence, five sites, four figures, one assertion block, the SR log and the digests. **No tolerance, no conftest, no `.claude`, no `docs/SUPERVISOR.md`, no new apparatus.**
* **R835: unchanged, R2** (GE3).

## Findings

**NONE BLOCK. For each I tried to write FR1's sentence and could not, and the reason is given rather than implied.**

### R1179 (ledger). THE REPAIR OF L3 PUBLISHED A FIFTH STALE FIGURE IN THE SAME BLOCK, ONE COMMIT LATE, FOR THE REASON CP3 NAMES.

`docs/closure/R1.md:30-32` publishes *"the three files at the report's own state are 430 passed, 0 failed."*

```
claim  the figure the closure artifact publishes, against the tree it describes
cmd    the three report-parametrised files, my own clean worktrees, -p no:randomly
out    at 4750f07   430 passed in 95.87s     <- the figure as published
       at dc49552   432 passed in 93.21s     <- the judged commit
rule   CP3: the paste is copied from a run executed AFTER the final edit, and if an
       edit follows the paste the paste is void. 7a9cf08 wrote the block, 4750f07 and
       dc49552 edited the report after it
judge  430 describes NO COMMIT -- it is the working tree with revision 4's body and
       without its section 10 -- and it is labelled as the report's own state inside a
       block stamped 566ef94. The report's own section 11 publishes 432 and explains
       the move, so the two deliverables disagree by 2
```

**Why it does not block.** Both figures are `0 failed`; no engineering number, gate threshold or input depends on either, so the silently-wrong-result sentence cannot be written. It is the class verdict 54 ledgered as L1-L4, in the same file, and **it self-clears**: CZ1 (ii) re-takes every figure in that block at the closure commit. *Closed when* the block is regenerated at the closure commit that exists.

### R1180 (ledger). `docs/USER_GUIDE.md` IS NOT IN THE GATE'S `ARTIFACTS`, SO FOUR PUBLISHED FIGURES IN THE WITNESS'S ONLY INPUT ARE RE-DERIVED BY NOTHING.

`tests/regression/test_r1_published_artifacts.py:69` is `ARTIFACTS = (REPORT, FORCES, UTILISATION)`. The new `for figure in (...)` loop re-derives `0.818471` and `1.639720` from the model and asserts them in `source` and in each of those three. The guide carries the same two digits plus `2.0034` and the kink `3.04`, and `grep -n USER_GUIDE tests/regression/test_r1_published_artifacts.py` gives two COMMENTS and no read. The two kink digits `0.98` and `3.04` are re-derived nowhere at all -- `grep -rn "3\.0408|0\.9806" tests/` is empty, and the flat-at-`0.10` assertion tests only `kink >= 2.0`, not `== 3.04`.

**All four are CORRECT at this commit; I measured every one** (`0.980652`, `3.040895`, `2.003394`, and the two utilisations). So no wrong number exists and FR1's sentence cannot be written. **It is the BP0 exposure and not a defect**, and under GE1/FK2 a new read is not asked for in the last revision ES0 allows. **AND THIS IS AN INSTANCE OF R1165, NOT A NEW ITEM, WHICH I CHECKED RATHER THAN PRESENTED AS NEW**: `grep -rln USER_GUIDE tests/` gives two files, one of them a corpus text file and the other this gate's two comments, so **nothing in `tests/` reads the guide at all** -- which is R1165, already on the open list. What is new is only that R1178's repair put four more re-derivable figures behind it. *Closed when* the guide is in the set the published-digit loop walks, or the guide cites the deliverable instead of repeating its digits. R2, with R1165.
### R1181 (ledger). SECTION 10's BOLDED SENTENCE IS REFUTED BY THE COMMAND SECTION 10 ITSELF NAMES.

Section 10 says **"It is pushed and the run was started by the push"**.

```
cmd    gh run list --commit dc49552fd719067d8482a104d47b6cd008a6608e --json databaseId
out    []
cmd    sed -n '22,25p' .github/workflows/ci.yml
out    paths-ignore:
         - "docs/reports/**"
rule   section 10's own cmd line, and the workflow's own trigger
judge  dc49552 touches ONLY docs/reports/R1/step-4.md, so the workflow DECLINED to run
       and no push could have started one. The commit IS pushed; the run is not
```

**Report prose, so FR1's third class and not blocking.** The substantive half is R2's and is not the implementer's to fix: **FP1's guarantee -- "the judged commit always has a CI run" -- cannot hold for a report-only tip commit**, because CK0's `paths-ignore` excludes exactly the path a report lives at. The repository already has the predicate and the true wording -- `report_only()` at `scripts/ci_section.py:350` and `report-only; no run by design` at `:592` -- but `section()` anchors on the ANSWERED commit through `_anchor()`, so no generated mode covers the report's OWN commit and section 10 is hand-written by necessity. *Closed when* FP1 and CK0 are reconciled by a directive, or the own-commit paragraph states `report_only`'s outcome instead of a push that did not run.

### R1182 (ledger). THE CROSSOVER ROW's LABEL ASSERTION CANNOT TELL THE TWO SHEAR CLAUSES APART.

`"3.2.4" in cross_lo.governing` matches both `3.2.4 beam shear` and `3.2.4 torsional shear`. My own arm, the two labels swapped in `candidates` with every value untouched:

```
cmd    "3.2.4 beam shear": u_shear / "3.2.4 torsional shear": u_torsion  ->  swapped
out    test_r1_published_artifacts.py      47 passed       <- blind
       test_r1_example_golden.py           14 passed       <- blind
       tests/verification/rung5             2 failed       <- caught
       test_r1_example_regenerates.py       1 failed       <- caught
       tests/unit                         470 passed
cell   one variable -- the two dict keys. Same commit, nothing else moved
judge  a wrong governing_clause in a published CSV IS caught, by the ladder and by the
       regeneration gate. The needle is wider than the quantity; the coverage is
       elsewhere and real
```

FR1's second class verbatim -- a needle too narrow where no wrong result follows. **One line, no fix asked**, and under EK2 the needle is not extended. R2.

## Rulings you asked for

1. **The remaining universal: attacked, and it holds.** Above, under `Carried`. 17614 admissible compression members, four properties, 0 mismatches; both ends of the declared domain solved from both sides; the one labelled existential constructed. **No seventh correction, and I am not asking for the pointer remedy.**
2. **The three isolating arms are the RIGHT THREE and I reproduced them at the lines you published -- but the conclusion you drew from B2 does not follow, and verdict 54's ledger call STANDS.**

```
claim  your three arms, re-run in a worktree of my own
out    B2 label at a fixed C_m   1 failed, 46 passed   test_r1_published_artifacts.py:636
       B3 cm clamped at 1.0      1 failed, 46 passed   test_r1_published_artifacts.py:718
       B1 retraction deleted     4 failed, 43 passed   :173 three times (verbatim
                                                       propagation) and :456
cell   one variable per arm, every other line held
judge  all three fire where you said, and the retraction is additionally held in place
       by the verbatim-propagation guard on all three artifacts, which you did not claim
```

**And B2 escapes MORE of the tree than you measured, which strengthens the row rather than weakening it** -- you ran three files; I ran the ladder and the unit suite too: `rung5 87 passed`, `tests/unit 470 passed`, `regenerates 11 passed`, `golden 14 passed`. **The crossover row really is the only thing in the tree that fires.**

**Why the ledger call was still right.** Ruling 1 measured whether the clause the LABEL names can disagree in VALUE with the published `utilisation` **in this code** -- 0 of 33151, and it is still 0, because `candidates` keys the same five fields `utilisation` maxes over. B2 measures a different thing: whether a defect that makes them disagree in IDENTITY would be CAUGHT. My R1182 arm answers that for the general case -- **the identity class was never uncovered**; the ladder and the regeneration gate catch a label swap. B2 is the one corner they miss, and your row closes that corner. **A coverage measurement does not retroactively make a correctness ruling wrong**, and GA1 is what kept the first from becoming a build order in a step with one revision left.
3. **L7's withdrawal: ENDORSED, reproduced, and it does not overreach.** Above, with the discriminating row named. It belongs off R1's open list and the closure artifact is right.
4. **EG3 (ii): your reading is correct and it is NOT in your favour.** At the judged commit both halves are `0 failed` in my own clean worktrees, so neither boundary state arises, the predicate is not tested, and there is no list to paste. You measured state (2) at `566ef94`; I measured the same half at `dc49552` and at `4750f07` and got `432` and `430`, both `0 failed`. **Publishing `407 passed` as a measurement rather than as an expectation is the right form, and it is the first time in this step that EG3 (ii) was measured from the implementer's side.**
### R1183 (ledger). THE CZ1 BLOCK PROMISES A PASTE THAT IS NOT IN THE FILE.

`docs/closure/R1.md:38-39` says the one main-half test the closure commit can move *"is run at this commit and **pasted below**"*.

```
claim  the paste the CZ1 block says is below it
cmd    grep -n "closure_evidence|rung3" docs/closure/R1.md
out    38:exactly one main-half test** -- `tests/verification/rung3/test_closure_...
       (the promise itself, and nothing else)
cmd    python -m pytest -q -p no:randomly
         tests/verification/rung3/test_closure_evidence_exists.py   -- my own run at dc49552
out    54 passed in 0.06s
cmd    python -m pytest -q --collect-only, main half, at dc49552
out    3961 tests collected
judge  the UNDERLYING CLAIM IS TRUE -- I ran the file and it is green, and the main
       half still collects the 3961 the block publishes -- so the accounting holds and
       only its evidence is missing. BF0: a claim that names its output and gives none
```

**Not blocking: the fact is right and I measured it, so no wrong number exists and FR1's sentence cannot be written.** It is the same block and the same commit as R1179 and goes on the same list. *Closed when* the block carries the paste it promises, or drops the promise -- and CZ1 (ii) requires the file's figures re-taken at the closure commit in any case.
### R1184 (ledger). A THIRD SITE OF THE RETIRED MECHANISM IS LEFT IN THE GUIDE, TWO PARAGRAPHS ABOVE THE PARAGRAPH THAT RETRACTS IT.

`docs/USER_GUIDE.md:319`, in the `Cm: 1.2` table, untouched by this diff:

```
| 14 governed by `3.2.4 beam shear` | none moved â€” not an interaction clause |
```

**The reason is the mechanism R1178 retired.** The cell one row above it is the contrast that makes the point: `| 6 governed by 3.3.1 interaction | none moved â€” the clause carries no C_m |` is a reason that IS general and IS true, because the tension branch never evaluates the amplified form. "Not an interaction clause" is not general: `3.2.4` does not carry `C_m`, which is why the row is flat *at this run's* `C_m`, and a larger one moves it. Verdict 54's closing condition named `docs/USER_GUIDE.md:332-334` and `:295-302` and both were repaired; this third site was named by neither of us.

**Every FIGURE in that table is correct and I re-derived all of it rather than reading it:**

```
claim  the guide's whole Cm: 1.2 table, from the shipped example, one variable moved
cmd    my own run of examples/platform12_placeholder.yaml with Cm: 1.2, nothing else
         touched, output outside the repository; then both utilisation.csv compared row
         by row on (member, station, period)
out    3.3.1 interaction    n= 6  rose= 0  fell=0      <- guide: none moved
       3.3.2 interaction    n=12  rose=10  fell=0      <- guide: 10 rose, 0 fell
       3.2.4 beam shear     n=14  rose= 0  fell=0      <- guide: none moved
       governing U  1.71167 -> 2.05621                 <- guide: 1.71167 -> 2.05621
       unmoved 3.3.2 rows: hub1_arm TIP u_bending 1.59266e-10, hub3_arm TIP 1.71774e-09
                                                       <- guide: 1.6e-10 and 1.7e-09
       the ten that moved read `simple` at 0.85        <- guide: all ten are simple
cell   one variable -- Cm. Same deck, same npz, same section, same window
judge  nine figures, nine matches. The factual half of the cell is TRUE; only the
       reason attached to it is the retired one (BG0)
```

**Why it does not block, and the sentence I could write if it did.** I can write *"a reader takes 'not an interaction clause' as the reason and reports no `C_m` exposure for a member whose published utilisation nearly doubles by `C_m = 2.00`"* -- but FR1's head is a wrong NUMBER in a deliverable or an input used other than as declared, and this is neither: every number in the table is right, and **the same section retracts the reason 34 lines below, in bold, with the counter-example and its digits** (`:352-355`). A reader of the section gets the correct rule. **Under CZ0 as it stands outside R1 I would have blocked on it, and I am saying so rather than smuggling it.** *Closed when* the cell's reason reads what the corrected item 1 reads -- another clause is the larger of the two at this `C_m` -- or the cell gives the count and no reason.
## Tolerances touched

**None.**

```
cmd    git diff 5f02798..dc49552 --numstat -- floatfea/tolerances.py tests/conftest.py
         'tests/**/conftest.py' .claude docs/SUPERVISOR.md
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
```

No value, no form, no counter. **No conftest or plugin under `tests/` moved, so CH2/CI0 is clear** -- I read the diff as empty rather than inferring it from a green suite, and the `ls-files` line returns a file, so the instruction is not silently matching nothing. **`.claude/` and `docs/SUPERVISOR.md` are untouched since `5f02798`, so there is no STOP-class finding.** The six new assertions are exact equality with `# not-a-tolerance:` at each site and the comments are correct: a clause `C_m` does not enter returns the identical float, and `cm * 0.0` is `0.0`. SR-67 records the choice NOT to introduce a relative-error threshold for the closed-form check, which would have been a tolerance in the last revision ES0 allows; I agree with it.

**EU1 does not attach** -- no tolerance value or declared counter moved -- **and I ran the adversarial configuration anyway**, because that is what found R1178 and R694 before it. Here it is the 17614-member sweep and the four boundary constructions, and nothing in them refutes the shipped sentence.

## Corpus (EG4(e) is dead by date; GC3 leaves batches to me)

**The pause did NOT hold and cannot: `CLAUDE.md` and my own agent file still read "pause until 28 October" and it is 9 November.** That is R1149, the reviewer's own item and still Xabier's. **I ran a batch AND the recorded substitute.**

**`tests/corpus/cm_kink_against_the_declared_domain.txt`, batch 53, 14 entries, ALL NEW, committed separately at `173c64c`.** The axis is the one the repair now rests on: where the kink falls against `MOMENT_REDUCTION_CM`'s declared bounds, solved from both sides of both ends (EH4) -- the knife edge at the ceiling (`2.0000001`, `2.0` to `4e-11`, `1.995`), the knife edge at the floor (`0`, `0.1`, `0.0999`), `s = 0` reached two ways, the tension branch, the biaxial resultant, `D/t` at its declared ceiling, a stubby `KL/r = 20` section, and all four clause channels live at once.

**Coverage, measured rather than asserted: `0 of 14` refute the published sentence**, against batch 52's `8 of 10` refuting the sentence this one replaced. **The shipped check evaluates `1 of the 14`** -- the tension row, which is its own `tension_lo` fixture -- and constructs no member resembling the other thirteen. A closed form is the first version of this sentence a member could have refuted, and 14 members its author did not write did not refute it.

**The substitute, both halves.** The continuum sweep is above. The regeneration check on the published deliverable:

```
cmd    python -m floatfea.cli run examples/platform12_placeholder.yaml in a clean
         worktree of mine, then git diff -- results/R1/example
out    results/R1/example/report.md | 4 ++--   (solve 64.40 -> 67.28, total 64.52 -> 67.40)
       member_forces.csv, utilisation.csv     byte-identical
judge  every physical number in all three artifacts regenerates byte-identical, and the
       only drift is the wall-clock table, which is R850's known exclusion and already
       on the ledger. U = 1.71167 unchanged
```
## CI at the reviewed commit: UNAVAILABLE BY CK0's DESIGN, and I record it as that rather than as a pass

**There is NO run at `dc49552` and there cannot be.** The commit touches only `docs/reports/**`, which the workflow ignores. **That is not CK2's exhausted allowance and it is not a red; it is an unavailable check**, so it does not HOLD by itself and I judge the step on everything else.

**The last run that EXECUTED, and whether the code has moved since.**

| run | head | status | conclusion |
|---|---|---|---|
| `42564673979` | `c2bf7d7` | completed | **success** -- but `566ef94` moved `floatfea/cli.py`, `tests/regression/` and `results/` after it, so it does NOT describe this tree |
| `42590412570` | `4750f07` | `in_progress` when I ruled, on its `ladder 6` step | **no result** -- a run that has not finished is not a pass, and I did not wait on it; I measured the ladder myself instead |

**And `4750f07` is CODE-IDENTICAL to the judged commit, which I measured rather than assumed**, so its run is the one that measures this code:

```
cmd    git diff --stat 4750f07..dc49552 -- . ":(exclude)docs/reports"
out    (empty)
cmd    gh api .../actions/runs/42590412570/jobs   -- job and step conclusions
out    lint, unit and guards        completed  SUCCESS -- every step RAN, none skipped:
         actionlint, ruff, black --check, mypy, unit tests, guards and meta-tests
       the verification ladder      in_progress on `ladder 6`; rungs 1, 2, 3 `success`, rungs 4 and 5 `pending` -- NO RESULT for this job
       CI determinism -- leg        skipped by its own condition -- unavailable, not passing
       CI determinism -- ten legs   skipped by its own condition -- unavailable, not passing
rule   CA2/CK2: a red CI is red, an unavailable run is neither. This is the third state
       again, by a different cause from CK2's -- declined rather than unpaid
judge  `guards and meta-tests` reached the runner and passed on a machine neither of us
       controls, at code identical to the tree under review -- which is what CZ1 (iii)
       exists to see. The LADDER job had not finished, so it says nothing and I inferred nothing from it.
```

**AND BECAUSE THE RUN AT `4750f07` HAD NOT FINISHED ITS LADDER WHEN I RULED, I RAN THE LADDER MYSELF RATHER THAN WAITING ON A MACHINE.** A low rung red is a STOP, and that is not a thing to infer from an unfinished job:

```
claim  every verification rung at the judged commit, in my own clean worktree
cmd    python -m pytest -q -p no:randomly tests/verification/rung<n>, n = 1..5
out    rung1  1276 passed, 2 warnings in 98.58s
       rung2    66 passed in 1.42s
       rung3   325 passed in 10.51s
       rung4   345 passed in 3.67s
       rung5    87 passed in 0.46s
rule   the collect counts CI published at `c2bf7d7` -- 1276 / 66 / 325 / 477 / 345 / 87 --
       so these five agree with CI's own denominators test for test
judge  **no rung is red and no low rung is red, so nothing here is a STOP.** Rung 6 is
       the 477 and it is inside my main half, which is ``3961 passed, 0 failed, 0 skipped`` -- so the whole
       ladder is measured by me at the judged commit even where CI had not finished
```

**A methodological note that is MINE, not the implementer's.** `gh run list --commit` with a 7-character sha returns `[]` SILENTLY -- it matches the full 40 characters only -- which reads exactly like a commit that never ran, and it is how I nearly mis-recorded three commits this round. `docs/SUPERVISOR.md` section 3b and my own agent file both give the abbreviated form. **The implementer's apparatus already has this right** -- `full_sha()` at `scripts/ci_section.py:285`, with the hazard stated in its docstring -- **and my instructions do not.** It needs a standalone `process:` commit citing a directive, which is not mine to write and is not a finding against this step.
## Closure items

**One line each, with the file, the line and what closes it. Fixed once in the closure commit, not re-reviewed item by item.** The evidence for each is the finding of the same number above.

| item | file and line | what closes it |
|---|---|---|
| R1179 | `docs/closure/R1.md:30-32` -- `430` where the judged commit is `432` | the CZ1 block regenerated at the closure commit, which CZ1 (ii) requires anyway |
| R1183 | `docs/closure/R1.md:38-39` -- a paste promised and absent | the paste, or the promise dropped |
| R1184 | `docs/USER_GUIDE.md:319` -- *"none moved -- not an interaction clause"* | the reason the corrected item 1 gives, or the count with no reason. **The one I would have blocked on under CZ0 outside R1** |
| R1180 | `tests/regression/test_r1_published_artifacts.py:69` -- the guide is not in `ARTIFACTS`; `0.818471`, `1.639720`, `2.0034`, `3.04`, `0.98` re-derived nowhere for it | the guide in the set the published-digit loop walks, or the guide citing the deliverable instead of repeating its digits. R2 if the closure commit does not reach it |
| R1182 | `tests/regression/test_r1_published_artifacts.py:686` -- `"3.2.4" in cross_lo.governing` matches both shear clauses | nothing, under EK2. R2, one line |
| R1181 | `docs/reports/R1/step-4.md` section 10 -- *"the run was started by the push"* | report prose, so EK3 puts it out of reach; its substantive half is R2's |

## Next step opens when

**STEP 4 IS CLOSED.** `Closes: R1/step-4`. Nothing above blocks, the step is at ES0's cap, and R1178 -- the step's one blocking item -- is answered and measured at all five of its sites.

**R1's INCREMENT is NOT closed, and these are its conditions.**

1. **The closure commit, with CZ1's four outputs in order:** (i) make it; (ii) at it, tree clean, paste `ruff check floatfea tests`, `black --check floatfea tests`, `mypy floatfea` and `pytest -q`; (iii) push it and paste `gh run list --commit` with the FULL 40-character sha and job-level conclusions, so the lint job's `guards and meta-tests` step is seen to have RUN; (iv) answer any red in a follow-on that repeats (ii) and (iii). Under EQ0 I review it only if it changes a gate or a tolerance; prose alone is not reviewed, and either way it counts against no step's rounds (EB4).
2. **The closure list, fixed once in that commit and not re-reviewed item by item:** R1179 (the `430`, which CZ1 (ii) re-takes anyway), R1183 (the promised paste, same block, same commit), R1184 (the guide's third site -- **the one I would have blocked on under CZ0 outside R1**), R1180, R1182.
3. **To R2 rather than to the closure commit:** L5 and its phantom citation, L9, R1149's dead pause clause, R1155, R1165, SR-41, SR-44, R835, R1181's substantive half -- FP1 against CK0's `paths-ignore` -- and R1180's remedy if the closure commit does not reach it.
4. **The FV2 commit door, which is nobody's inside this loop.** Fourth consecutive round in which a reviewer has written two commits into the implementer's checkout because FV2 provides no other door, and said so in the verdict. It needs a decision from Xabier.
5. **The whole verification ladder green at the closure commit's own pushed sha**, rungs 1 to 6, with the job table. I measured rungs 1 to 5 myself at this commit and rung 6 inside the green main half, so none is red today; the closure commit's own pushed run is what must show all six green on a machine neither of us controls.

**On the schedule.** FW0's 10 November holds: step 4 closes on 9 November with its blocking item answered, and what remains is a closure commit and a list. **On the sixth correction**, the report's reading is better than the count: the first five were claims ABOUT configurations and each was refuted by a configuration its author had not run; the sixth is the closed form, which has no configurations to choose. I tried to refute it on 17614 members and four constructed boundaries and could not. **That is the first time in this milestone that a repair of this sentence has survived a population its author did not write**, and it is why this closes rather than carrying a seventh.

## I do not disagree with the criterion

FR1 is the rule I ruled under and I am not asking for it to move. **The honest test of it this round is R1184, and I am giving no count of the rest.** R1179, R1183 and R1184 are each a defect in a file that goes to Xabier, so each would have been blocking under CZ0 (a) as amended by EZ0; R1181 is report prose, which EZ0 excludes outright; R1180 and R1182 are coverage rather than defect, and whether CZ0 (c) reaches them is exactly the kind of thing I would be guessing at. **A count here would be a property of my own list and not of the criterion, which is the lesson of the sentence this whole step was about, so there is no count.**

For every finding I tried to write FR1's silently-wrong-result sentence. For five I could not and said why. **For R1184 I could write it, and FR1's head still does not cover it** -- every number in that table reproduces, nine figures for nine, and the retraction sits 34 lines below the cell in bold with its counter-example -- so I ruled it a ledger item **and said which way I would have gone under the wider criterion** rather than smuggling it in as blocking or leaving the disagreement silent. That is what FR1's last sentence asks for, and it cost this step nothing: the step closes on its date with its one blocking item measured at every site.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4
Reviewed commit: c2bf7d75e8e7baa915156bb29ccb911b240ea730
**Reviewed commit: `c2bf7d75e8e7baa915156bb29ccb911b240ea730`.**
Verdict: HOLD
Scope: **R1 step 4, REVISION 3 at `c2bf7d7` -- a REVIEWED REVISION, so this CONSUMES A ROUND. Step 4 stood at 1 of 3 and stands at 2 of 3 (ES0).** The report carries `# Revision 3` / `Answers: verdict 53 @ b0ff398`, which names the NEWEST verdict -- the addendum -- so the 1b check passes and I am saying so rather than leaving it silent. Ruled under **FR1 with EZ0**, and the one blocking finding carries its silently-wrong-result sentence. No `--interim`; ****no closing line** (FK1, no `--closes`), because the step does not close here. **GE3: `R835: unchanged, R2`. Not re-measured.** GA3's 150-line target is OVERRUN at 198 lines, and I am saying so rather than trimming the evidence: the overrun is the CI partition block, the withdrawal of a figure of my own, and the blocking finding's two census blocks. GA3 says the target does not limit what I may rule blocking, and one thing is.
Tests: **4368 passed, 0 failed, 0 skipped AT THE JUDGED COMMIT, MY OWN RUN, in EI0's two halves, AND CI's run at the same commit agrees with it.** CI run `42564673979` at `c2bf7d7` is `completed` / **success**, and its three test steps PARTITION the suite: `470` unit + `1322` guards + `2576` ladder = **4368**, which is exactly my own `pytest --collect-only` total and exactly the report's `3961 + 407`. **MY OWN RUNS at the judged commit, in clean worktrees of my own (FV2), `-p no:randomly`: the main half **3961 passed, 0 failed, 0 skipped in 2849.16s (0:47:29)** and the three report-parametrised files **407 passed, 0 failed in 86.33s** -- 3961 + 407 = 4368, the same total CI measured and the same the report names. Also FV1's local selection IN FULL **764 passed, 0 failed, 0 skipped**; `ruff` `All checks passed!`, `black --check` `128 files would be left unchanged.`, `mypy` `Success: no issues found in 45 source files`. **My first whole-tree local run said `17 failed, 3944 passed` and I WITHDREW IT -- the cause was my own `PYTHONPATH` and `## The run` carries the one-variable cell.** Zero reds anywhere, local or CI.
Door (FV2/GE4): **every measurement below was taken in `git worktree`s of my own at `c2bf7d7`** under the session scratchpad -- one kept clean for the suite, one for every injection, so each `git checkout`/`cp` restore ran in MY tree. In `C:/dev/floatfea` I ran read-only `git`, `gh` and process queries, **plus the two writes FV2 gives me no other door for: the corpus commit `2ff2398` and this verdict.** Both touch one reviewer directory and leave the tree clean; `git status --porcelain` was empty before and after. That is the open escalation in `docs/SUPERVISOR.md` section FV2 -- recorded, not tidied, and not resolved inside this round.

## Carried

* **R1168 -- ANSWERED, and the repair it produced is this round's blocking finding (R1178).** `WITH A BENDING TERM TO MULTIPLY` is now GONE from `floatfea/cli.py` by assertion, which the gate requires -- but it is still in `docs/USER_GUIDE.md:298`, so the two published deliverables disagree again, in reverse. Folded into R1178.
* **R1169 -- ANSWERED.** `docs/directives/FZ.md:915` is the entry; the dated in-place correction block is at 929-967. Mechanism re-read, not the prose.
* **R1170 -- ANSWERED, section 4, and I reproduced it myself rather than accepting the attribution.** `u_combined = max(amplified, simple)` -> `amplified`, one line, in my own tree: `assert '3.3.2' in '3.2.3 bending'` at `test_r1_published_artifacts.py:514`, `1 failed, 46 deselected`. The report's `:514` is right at this commit.
* **R1171 -- ANSWERED.** The three report-parametrised files are `407 passed, 0 failed` at the report's own state, my own run.
* **R1172 -- ANSWERED and CHECKED BY COLLECTION, not by reading.** `--collect-only` at `c2bf7d7` gives **4368**, and `4368 - 407 = 3961`, which is the main half the report names. The accounting holds.
* **R1173 -- ANSWERED.** `docs/closure/R1.md` carries three runs, three fixture tables with expected beside got, three transcripts. I re-derived all five fixtures from the shipped artifacts myself: `32 rows`, `[('12.5', 26), ('15', 4), ('16.2', 2)]`, `over unity: 4`; `1248 rows` with `288/288/48/48/288/288`; governing `platform:hub2_arm ROOT 12.5 1.71167 3.3.2 interaction`. The transcripts are internally consistent with the tree -- run 2's install block matches `constraints-dev.txt`'s pins (`mypy 2.4.0`, `ruff 0.17.1`, `pytest 9.1.1`, `numpy 2.5.4`) and the local venv.
* **R1174 -- the COUNT is gone and the CONDITION that replaced it is false. R1178.**
* **R1175 -- ANSWERED.** `grep -c -- "-c '" docs/USER_GUIDE.md` is `0`; the paragraph now carries the measurement.
* **R1176 -- ANSWERED, section 8.** `tests/regression/test_ft27_topology_solve.py` collects `9 tests`. Built.
* **R1177 -- agreed, no action asked.**
* **Interim check item 4 -- CLOSED, at the wrong commit.** `docs/milestones/F2a.md` landed in `8de5d2b`, not `43f8bb0` (`git log --oneline c992e54..HEAD -- docs/milestones/F2a.md` gives one line, `8de5d2b`; `43f8bb0` touches the digest and `FZ.md` only). Ledger row L6.
* **Interim check item 5 -- the suite half is DISCHARGED at this commit, the CI half is NOT.** See `## CI` below.
* **R835: unchanged, R2** (GE3).

## Findings

### R1178 (BLOCKING). THE REPAIR OF R1174 REPLACED A WRONG COUNT WITH A FALSE UNIVERSAL, AND THE DELIVERABLE'S OWN COLUMNS REFUTE IT ON 10 OF 32 ROWS INCLUDING THE HEADLINE.

`floatfea/cli.py:111-124`, regenerated into `results/R1/example/report.md:75` and line `41` of both CSVs. The new caveat states three conditions as NECESSARY and then gives the contrapositive explicitly: *"A larger C_m RAISES the published utilisation of a row only where ALL THREE of these hold ... Anywhere else the published column is FLAT in C_m."* The three are (i) `3.3.2` governs the row, (ii) there is a bending term, (iii) C_m is above the overtake. **A reader evaluates (i) and (iii) by reading `governing_clause` and `interaction_form`, because those are COLUMNS of the file the sentence is printed in. At the row's own state the sentence is false on every row that moves.**

```
claim  the published condition set, evaluated at each row's own state, against the
       column the sentence is about
cmd    census of results/R1/example/utilisation.csv: rows where utilisation_Cm_sens
       != utilisation, and whether (i)+(ii)+(iii) hold at that row
out    32 rows | utilisation_Cm_sens != utilisation on 10
       of those 10, ALL THREE conditions hold on: 0
       their interaction_form column: {'simple': 10}   <- (iii) is FALSE on all ten
       rows where ALL THREE hold: 2  -- and both of those are FLAT
       headline platform:hub4_arm ROOT: form=simple  1.71167 -> 1.71365
rule   the published sentence: "Anywhere else the published column is FLAT in C_m"
```

So the condition set is **0 for 12** as a predictor on the deliverable's own table: satisfied by two rows that are flat, violated by all ten that rise. And the subordinate clause -- *"a row governed by 3.2.4 shear is flat in C_m however large its bending term"* -- is false inside C_m's own declared bounds `0.1 .. 2.0`:

```
cmd    check_member(axial_n=-6.0e6, moment_y_nm=1.5e8, torsion_nm=1.65125628e8) at
       cm = 0.85 and cm = 2.00, every other input held
out    cm=0.85  governing='3.2.4 torsional shear'  form=simple     U=0.8184711191258446
       cm=2.00  governing='3.3.2 interaction'      form=amplified  U=1.6397199836312206
cell   one variable -- C_m. u_bending=0.7930651386236371 at both
judge  a 3.2.4-governed row at 0.82 reaches 1.64. Under unity to 64% OVER, and the
       caveat says this row cannot move
```

**AND THE SENTENCE CANNOT BE READ SO THAT BOTH HALVES ARE TRUE, WHICH IS WHY THIS IS NOT A MISREADING OF MINE.** There are two available readings of (iii) -- the C_m you move FROM, which is the row's own published state, or the C_m you move TO. Under the ROW-STATE reading, (iii) is false on all ten rows that rise and the census above refutes it. Under the DESTINATION reading those ten are allowed, and then the clause *"a row governed by 3.2.4 shear is flat in C_m"* is refuted by the construction below -- because "a row governed by 3.2.4 shear" can only name the row's own `governing_clause` column, and that row goes from 0.818 to 1.640. **Each reading refutes a different half.** Whichever one the repair meant, one half of the published sentence is false, and the reader has no way to know which reading to apply.

**THE COUNTER-EXAMPLE WAS ALREADY IN THE REPOSITORY WHEN THE SENTENCE WAS WRITTEN, FOR THE SECOND TIME IN TWO COMMITS.** `tests/corpus/cm_direction_claim_members.txt` line 12, `id=compression_beam_shear_governs`, committed at `cb520c6` ONE COMMIT BEFORE `e526a9e`: `0.9662150503393355 -> 0.9951911821042186` over `0.85 -> 1.20`, governed by `3.2.4 beam shear` at the low end. R1174 was "the corpus named this case one commit earlier"; R1178 is the NEXT ENTRY IN THE SAME FILE, one repair later.

**And the gate knows the crossover exists.** The new row's own guard asserts `'3.2.4' in governing` at BOTH C_m values. Solved in the direction that weakens it (EH4): the guard holds down to `torsion_nm = 330811663.0070415`, and the shipped fixture is `5.0e8` -- a margin of **1.51x**. Just below it the fixture becomes the configuration above. **The fixture is guarded away from the case the published sentence excludes, and nothing reads the guard back into the sentence.**

**FR1's sentence, which is why this blocks rather than ledgers.** The silently wrong result is an engineer's C_m-exposure answer, taken from the decision rule the deliverable itself publishes beside the numbers: the caveat tells a reader that a row whose `interaction_form` column reads `simple`, or whose `governing_clause` reads `3.2.4`, is FLAT in C_m -- and on 10 of the 32 shipped rows, including `platform:hub4_arm ROOT` at `U = 1.71167`, it is not, while on a shear-governed member inside the declared bounds the same sentence conceals `0.818 -> 1.640`. Every number in every artifact is correct; the published rule for reading them is false, and false in the unconservative direction. **This is not report prose (FR1's third class) -- it is `floatfea/` and three published deliverables, and the sentence is a claim about the values in the same file.** It is the sixth correction of one sentence (R743, R1156, R1162, R1168, R1174, this) and the third in a row verified only against configurations its own author chose.

*Closed when* the caveat states what the code does rather than a condition set over the row's own columns -- the honest form is the one the GUIDE's three-reason list at `docs/USER_GUIDE.md:330-340` nearly has: `utilisation` is the maximum over clauses, `C_m` enters only `3.3.2`, and `u_combined` can rise while `utilisation` does not **until `3.3.2` overtakes, which a larger C_m can make it do** -- with no universal about what a shear-governed row "cannot" do. Four sites: `floatfea/cli.py`, the three regenerated artifacts, `docs/USER_GUIDE.md:332-334` (the same false universal) and `docs/USER_GUIDE.md:295-302` (the R1168 wording this repair deleted from the deliverables as incomplete, left standing in the guide). And a row that reddens when the universal is restored -- the corpus entry above is one, and it needs no injected defect.

### Ledger (FR1: none can cause a silently wrong result; one line each)

**L1.** `docs/closure/R1.md:347` says the C_m caveat had "four" corrections, `R743, R1156, R1162 and R1168`; the shipped caveat names five (`grep -o "R743 / R1156 / R1162 / R1168 / R1174" floatfea/cli.py` matches). The artifact was written at `8de5d2b` and the repair landed at `e526a9e` after it -- BP0, one commit late.

**L2.** `docs/closure/R1.md:394` says "the two new assertions added in step 4"; there are **four**, each with its own `# not-a-tolerance: EXACT equality` -- `tension_lo` (`a596fa7`), `compress_mid` (`092334a`), `flat_lo` (`af9c6aa`), `shear_lo` (`e526a9e`), all inside step 4 by `git log -S`. Its two stated reasons cover two of the four.

**L3.** `docs/closure/R1.md` section 0 names TWO different commits for one figure: the generated block says "Whole suite at `e526a9e`", the paragraph at `:47` says "measured at `8de5d2b`, the commit that added this file". The report's section 11 says `e526a9e`, so `:47` is the wrong one -- and it is the sentence that tells the reader to read the label.

**L4.** `docs/closure/R1.md:204` cites `floatfea/model/platform.py:879` for `density > basis.RHO_STEEL`; it is at `:878`. **This is the fifth stale citation you asked me to look for, and it is in the published deliverable rather than in the report** -- section 5 corrected the report's copy and left the artifact's.

**L5.** `tests/verification/rung3/test_closure_evidence_exists.py:45` cannot see a citation that carries a line number: the regex requires a closing backtick straight after `.py`/`.md`, so `` `path.py:879` `` matches nothing. Measured across all 13 closure artifacts: 21 citations are invisible to it, and one is a live phantom -- `docs/closure/F0.md:122` cites `docs/m11-platform-plan.md:637`, which does not exist in this repository and carries no `HSP:` prefix. **GA1: one ledger line, no further census** -- I ran it once, it is above, and I am not extending the guard.

**L6.** `docs/reports/R1/step-4.md` section 8a condition 4 attributes `docs/milestones/F2a.md` to `43f8bb0`; it landed in `8de5d2b`. The condition itself IS closed.

**L7.** section 5's premise for leaving the density item as a ledger row is refuted by the tool's own output: *"neither sentence in `report.md` says which reference it used"*. Both do. At `rho: 7000` my own run writes `the equivalent density is 11433.5 kg/m^3, ABOVE steel at 7850` and `carry an equivalent density ABOVE the declared nominal`. **The item is already closed by the tool, not deferred** -- which is the answer to your question 4 for that half.

**L8.** `tests/regression/test_r1_published_artifacts.py` is green under a C_m leak into `u_shear` -- all `47 passed` with `u_shear = cm * f_v / allow_shear`, because all four of its controls carry `shear_y_n = shear_z_n = 0`. **Coverage exists elsewhere and I measured it rather than reporting a hole:** `rung5/test_g61_api_wsd_hand_calculations.py::test_each_check_REDDENS_under_the_load_the_plan_asks_for[beam shear]` fails under the same injection (`1 failed, 556 passed`). One line, no action.

## Rulings you asked for

1. **The label/number split (section 2a) -- your ledger call is RIGHT, and I converted it from reasoning into a measurement.** `candidates` maps the five labels to the same five fields and `governing = max(candidates, ...)`, while `utilisation = max` of those fields, so they cannot disagree in value. Measured over 33151 admissible random tubulars (D 0.5-2.5 m, D/t 20-300, KL/r 20-160, biaxial moment, shear, torsion, C_m uniform on 0.1-2.0): the field the LABEL names differs from the published `utilisation` on **0**, and ties broken by dict insertion order occur on **0**. Correctly not built against under GA1.
2. **The new row, checked hardest -- it carries its own failure, at the assertion and with the digits you published.** `u_torsion = cm * f_vt / allow_shear`, one line, my own tree: `AssertionError: ... '3.2.4 torsional shear': 2.106579274469036 -> 4.956657116397731`, `test_r1_published_artifacts.py:620`, `1 failed, 46 deselected`. EH4 in both directions: the detection side is 1 ULP of the field (smallest multiplicative leak detected, `eps = 9.65e-17`, relative defect `1.11e-16`), the weakening side is the `1.51x` torsion margin in R1178.
3. **Condition 5's premise -- you are right and my predecessor was wrong, and it is checkable from the tree.** `git worktree list` in the main checkout still shows `suite-count-x86d2suk/tree` at **`8de5d2b`**, not `cbb8027`, so the live run was the authoritative one. No `suite_count` or `suite-count` process is alive now; fifteen `suite-count-*` directories remain under `TEMP`. Neither figure is published, which I confirmed rather than took.
4. **Four stale citations -- you left a fifth, L4, and it is in the closure artifact.** The four you name resolve at this commit: `:514`/`:544`/`:620` are the three assertions, `FZ.md:915` is the SR entry, `USER_GUIDE.md:298` is the qualifier, `platform.py:878` is the gate, `platform12_placeholder.yaml:193` is `required_section: false`.
5. **Your two "ledger rather than repair" calls:** the density half is L7 -- closed, not deferred, and the premise was wrong in your favour. The label/number half is ruling 1 -- correct, and now measured. **Neither should have been repaired here.**
6. **GE's five clauses: all five done, in GE's order.** GE1 built rather than argued; GE2's three held to one line of substance each, with the zero-moment row as the non-prose half; GE3 routed; GE4 escalated with the measurement rather than answered, which is what GE4 asked for when its own text was false; GE5 spent.

## Tolerances touched

**None.**

```
cmd    git diff c992e54..HEAD --numstat -- floatfea/tolerances.py tests/conftest.py
         'tests/**/conftest.py' .claude docs/SUPERVISOR.md
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
```

No value, no form, no counter. **No conftest or plugin under `tests/` changed, so CH2/CI0 is clear** -- nothing that writes the gate's own record moved, and I read the one conftest's diff as empty rather than inferring it from a green suite. **`.claude/` and `docs/SUPERVISOR.md` are untouched since `c992e54`**; the two `process:` commits that changed them (`b8d573f`, `5e0808e`) were reviewed at the interim check and are before this range, so there is no STOP-class finding here.

**EU1 does not attach** (no tolerance value or counter moved) **and I ran the adversarial case anyway**, because EU1's lesson is that the configuration nobody chose is the one that measures -- and here it is what found R1178. The one new assertion is exact equality with `# not-a-tolerance:` and the comment is correct: a clause C_m does not enter returns the identical float.

## Corpus (EG4(e)'s pause is spent by date; GC3 leaves batches to me)

**The pause did NOT hold and could not: `CLAUDE.md` still reads "pause until 28 October" and it is 8 November.** That is R1149, mine, and still Xabier's; my own agent file carries the same dead clause. **I ran a batch, and I ran the recorded substitute as well.**

**`tests/corpus/cm_condition_set_necessity.txt`, batch 52, 10 entries, ALL NEW, committed separately at `2ff2398`.** The axis is batch 51's one repair later: the three published conditions evaluated AT THE ROW'S OWN STATE, which is the only state a reader of `utilisation.csv` has. **Eight of the ten refute the published universal; two are controls where it is true, one of them the shipped gate's own fixture.**

**Coverage, measured rather than asserted: the check under review EVALUATES 2 of the 10 -- its own two fixtures -- and 0 of the 8 that refute.** Its assertions about the condition are string needles over the caveat's own words (`"GOVERNS that row"`, `"MAXIMUM"`, `"NO COUNT OF"`, `"BENDING TERM TO MULTIPLY" not in`), which test that the sentence is PRESENT and cannot test whether it is TRUE. **Batch 51's coverage against this round's repair is 0 of 2 for the second consecutive round** -- entries 11 and 12 were both live counter-examples when the repair shipped.

**The substitute, which is what produced R1178:** a census of a published deliverable against its own caveat (10 of 32 rows, 0 of 12 predicted) and a continuum sweep of C_m over the decision rule the caveat describes, bisected for the crossover rather than sampled.


## CI at the reviewed commit: run `42564673979`, COMPLETED, conclusion **SUCCESS** -- and it is a whole-suite measurement

| job | conclusion |
|---|---|
| `lint, unit and guards` | **success** -- every step RAN, none skipped: `actionlint`, `ruff`, `black --check`, `mypy`, `unit tests` (`470 passed`), `guards and meta-tests` (`1322 passed, 1 warning`) |
| `the verification ladder` | **success** -- all six rungs in the workflow's own order `1, 2, 3, 6, 4, 5`, each `run_rung: OK`, `0 failed, 0 errored, 0 skipped`, collecting `1276 / 66 / 325 / 477 / 345 / 87` |
| `CI determinism -- leg` | skipped by its own condition -- **unavailable, not passing** |
| `CI determinism -- ten legs agree` | skipped by its own condition -- **unavailable, not passing** |

**`guards and meta-tests` reaching the runner and passing is what CZ1 (iii) exists to see, and it did**, and rung 6 ran `tests/regression` in full -- the only coverage of the directory this round changed, and the one the interim check could not measure.

```
claim  CI's three test steps PARTITION the suite at this commit, so this is a
       whole-suite figure and not a sample
cmd    470 (unit) + 1322 (guards) + (1276+66+325+477+345+87 = 2576, ladder)
out    4368
rule   my own `pytest --collect-only` at `c2bf7d7` gives 4368, and the report's
       two halves give 3961 + 407 = 4368. The same denominator three ways
judge  4368 passed, 0 failed, 0 skipped at the judged commit, on a machine
       neither the implementer nor I control. Nothing is red anywhere
```

**EG3 IS NOT REACHED AND THERE IS NOTHING TO CLASSIFY.** Every half is `0 failed`, so neither of EG3's two boundary states arises, the FS1/FT1 predicate is not tested, and CZ1 (iv) does not arise. No `FAILED` list is pasted because there is none. That is the second consecutive boundary with nothing to classify, and the report says so correctly.

**A commit landed after the one I judge.** `5a9467c`, `docs: SR-57 to SR-62 ...`, touches `docs/directives/FZ.md` and `docs/digests/` only. Not my subject, and it moves nothing I measured.

## The run, and a figure of MINE that I withdrew rather than published

**My own runs at `c2bf7d7`, in worktrees of my own, `-p no:randomly`:**

```
the MAIN HALF, pristine worktree, PYTHONPATH unset
  (the same command scripts/suite_count.py runs)  3961 passed, 0 failed, 0 skipped
                                                       in 2849.16s (0:47:29)
the three report-parametrised files                407 passed, 0 failed in  86.33s
                                          TOTAL   4368 passed, 0 failed, 0 skipped
FV1's local selection IN FULL -- tests/unit, the four root guards,
  test_r1_published_artifacts.py, test_r1_example_regenerates.py,
  test_r1_example_golden.py                        764 passed, 0 failed in 391.45s
pytest --collect-only, whole suite                4368 collected
ruff check floatfea tests                         All checks passed!
black --check floatfea tests                      128 files would be left unchanged.
mypy floatfea                                     Success: no issues found in 45 source files
```

**AN EARLIER WHOLE-TREE RUN OF MINE SAID `17 failed, 3944 passed`. THAT FIGURE IS WITHDRAWN, THE CAUSE IS MINE, AND I MEASURED IT RATHER THAN ATTRIBUTING IT.** All 17 were in `tests/test_ci_ladder_gating.py`; the clean re-run above has the same denominator and none of them.

```
cell   one variable -- whether PYTHONPATH is set. Same file, same commit, same
       pristine worktree, same interpreter, nothing else moved
out    PYTHONPATH = my worktree  ->  17 failed, 47 passed in 94.21s
       PYTHONPATH unset          ->  64 passed,  0 failed in 117.23s
rule   scripts/run_rung.sh:213 joins PYTHONPATH with a POSIX COLON. On Windows
       the separator is a semicolon, so any pre-existing PYTHONPATH makes the
       value unparseable, `-p rung_no_xpass` never loads, and pytest exits 1
       with no junit -- which the gate reports as "produced no readable junit
       report ... and nothing describes what it did"
judge  I set PYTHONPATH so the imported source was MY worktree's and not the
       main tree's, which is FV2's whole point. The implementer does not, and
       `scripts/suite_count.py` does not. The reds were my harness. CI's
       `guards and meta-tests` runs this exact file and is green at this commit
```

**L9, one line under GA1 rather than a finding.** That failure mode is FAIL-LOUD -- every rung reddens and `test_the_changed_requirements_are_exactly_these` goes red with it -- so it cannot make a red rung look green. What it does do is make the seven conftest-forgery entries stop disagreeing with their declarations, which reads as *those channels are now closed* when in fact no rung ran. GA1's test is whether it could hide a blocking finding; it fails closed, so: one ledger line, no census, no fix asked, and the apparatus freeze holds.

**I also voided an earlier run of my own by probing in the worktree it was reading**, which is the ordering lesson this project already has written down. The second run was made in a worktree I then touched for nothing else. Recorded because a reviewer's contaminated figure is the same defect as anyone's.

## Next step opens when

Step 4 stays open at **2 of 3** reviewed revisions. **Revision 4 is the last one ES0 allows, so one blocking item and a short list is what it should carry.**

1. **R1178**, at its four named sites -- `floatfea/cli.py`, the three regenerated artifacts, `docs/USER_GUIDE.md:332-334` and `docs/USER_GUIDE.md:295-302` -- with the universal gone rather than reworded, and a row that reddens when it is restored. **A corpus entry that needs no injected defect is in `tests/corpus/cm_condition_set_necessity.txt`; the shipped fixture is `1.51x` from being one.** Closed site by site, each with its hunk or the reason the site was left.
2. **L1, L2, L3, L4** -- the four stale figures in `docs/closure/R1.md`, which is the file that goes to Xabier. Re-measured at the commit that publishes them, not carried over (BP0, CP3). **L5 is apparatus and is one line under GA1; do not census it and do not extend the guard.**
3. **CI at revision 4's own commit, COMPLETED and green**, with the job table (FP1). It is green and complete at THIS commit, rung 6 included, so this is a carry-forward of the standing requirement and not an open item against revision 3.
4. **The whole-suite line at revision 4's own commit**, both halves, with the figure re-taken after the last edit.
5. **Nothing else.** GE1's "nothing else of substance" still governs, and nothing in this verdict asks for new apparatus, a new guard or a new scanner.

**On the schedule, since the report raises it and I am the other half of that judgement.** R1's date is 10 November and this HOLD spends one of the two remaining days. One blocking item, one sentence, four sites and four stale figures is a half-day of work, so the date is reachable -- but this is the **sixth** correction of one sentence and the **third consecutive** one to ship a claim its own author's configurations could not refute. If revision 4 produces a seventh, the honest reading is that the sentence should be replaced by a pointer to the guide's three-reason list and the measurement, rather than corrected again, and I would say so then rather than in the closure.

## I do not disagree with the criterion

FR1 is the rule I ruled under and I am not asking for it to move. **R1178 is blocking because I can write FR1's sentence for it, and I wrote it** -- a published decision rule that contradicts the published columns it is printed beside, in the unconservative direction, on the headline row. Everything that could not be given that sentence is a ledger line above, including findings I would have liked to block on under CZ0 as it stands outside R1. The distinction I drew is the one FR1 asks for: a wrong count of corrections cannot mislead anyone about a member; a published rule saying a member has no C_m exposure when it has two-fold can.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: c992e5432561342aea90d9c445b9c4a0d88ded93
**Reviewed commit: `c992e5432561342aea90d9c445b9c4a0d88ded93`.**
Verdict: PASS
Scope: **ADDENDUM to the ES0 interim check at `c992e54`, correcting MY OWN figure and MY OWN causal claim. NO new findings, no change of disposition.** Still an interim check, still `--interim`, still counting against no round; step 4 stays at **1 of 3**, and the entry below it stands on everything except the two statements corrected here. Written because the whole-suite run I had abandoned COMPLETED after I wrote that entry, and it refutes what I said about it. BP0 and CP3 require a figure to be regenerated or withdrawn when the measurement underneath it moves; R861 is the precedent for a reviewer withdrawing its own figure one commit after publishing it.

## Carried

Nothing new is carried and nothing carried is discharged here. **R1170, R1171, R1172 and R1173 remain open exactly as the entry below states; R1168 and R1169 remain answered; R1174-R1177 remain ledger rows; `R835: unchanged, R2`.** This addendum touches only the two statements named below.

## Findings

**THE WHOLE-SUITE FIGURE EXISTS AND IS GREEN. MY ENTRY SAID IT COULD NOT BE TAKEN, AND THAT IS WITHDRAWN.**

```
claim  the whole suite at the judged commit
cmd    python -m pytest -q -p no:randomly        (my own worktree at c992e54)
out    4329 passed, 2 warnings in 3169.41s (0:52:49)
rule   0 failed, 0 skipped. 4329 is the SAME total verdict 51 measured at 6876854
       (3957 main half + 372 report files = 4329), so the count is unmoved across
       the six commits of this range
```

Both warnings are pre-existing and benign: a `numpy` deprecation site, and `RuntimeWarning: overflow encountered in dot` raised deliberately by `tests/verification/rung1/test_corpus_configurations.py::...[orient_norm_overflow]`, which is a corpus entry whose whole point is the overflow.

**So the record is now: `4329 passed, 0 failed, 0 skipped` at `c992e54`, plus CI `success` at the same commit** -- run `42553224916` completed after I wrote the entry below, with all six ladder rungs green (`ladder 1, 2, 3, 6, 4, 5` each `success`), `lint, unit and guards` green with every step run including `guards and meta-tests`, and the two determinism jobs `skipped` by their own conditions. **Zero reds anywhere, local or CI.** The entry below recorded CI as `in_progress`, which was true at every point it measured; this discharges it.

**AND THE CAUSAL CLAIM IS REFUTED, BY THE ABLATION I SHOULD HAVE RUN BEFORE WRITING IT (BG0, applied to me).** The entry below says the whole-suite figure "is NOT in this verdict, and the reason is a measurement rather than a choice", and attributes it to the live `suite_count.py` run. **The processes were real and the attribution was not measured.**

```
cell   one variable -- whether a `suite_count.py` run is live. Verdict 51's run at
       6876854, same machine, no such run: 2824.73s + 76.04s = 48:20 for the same
       4329 tests. Mine at c992e54, four such processes live: 52:49
judge  the contention cost about +9% of wall time. It did not prevent the
       measurement; the run completed normally while I was reading a
       block-buffered progress file and inferring a stall from it
```

**What I actually did was read a buffered file and call it a stall.** The dots in that file lag the run by a whole output block, so "8% after a hundred minutes" was never a measurement of progress -- it was a measurement of buffering. Invoking GE5 to sample was therefore unnecessary, though the sample itself (FV1's selection, 1136 passed) is correct and independently useful.

**What SURVIVES from that passage, because it was measured rather than inferred:** a `suite_count.py` run was live in the main tree at `suite-count-x86d2suk` with four processes while the invocation said it had been stopped; fifteen `suite-count-*` worktrees have accumulated under `TEMP`; and every `--out` went to a pytest tmpdir with `git status -- results/ scripts/` empty, so nothing in the repository was at risk. The request that its figure not be published also stands, since the invocation itself says it was at a stale commit.

*Nothing here blocks and nothing here is new against the implementer.* Both corrections are to my own prose, and under FR1 a reviewer's own wrong figure in a verdict is the same class as any other figure -- it goes on the record and does not consume a round.

## Tolerances touched

**None**, unchanged from the entry below: `git diff c88b0c0..c992e54 --numstat -- floatfea/tolerances.py tests/conftest.py 'tests/**/conftest.py'` is empty, and no value, form or counter moved. No ablation in this addendum; nothing was run that could change one.

## Next step opens when

**Unchanged from the entry below, with items 5's CI half and the whole-suite half both now DISCHARGED at `c992e54`.** Revision 3 still owes, in order: **R1173** (witness run 3 and `docs/closure/R1.md` with every transcript and each fixture's result against expected -- and that file has since landed at `8de5d2b`, which no verdict has reviewed); **R1174** (the caveat's third flat cause named in `floatfea/cli.py`, regenerated into all three artifacts, with `docs/USER_GUIDE.md:297` brought into line with its own table at 282-286); **R1170, R1171, R1172, R1175, R1176** answered at their named sites with every `out` re-taken after the last edit (CP3); and a CI run plus a whole-suite line **at revision 3's own commit**, since the two discharged here are at `c992e54` and three commits have landed since.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: c992e5432561342aea90d9c445b9c4a0d88ded93
**Reviewed commit: `c992e5432561342aea90d9c445b9c4a0d88ded93`.**
Verdict: PASS
Scope: **ES0 INTERIM CHECK on R1 step 4 at `c992e54`.** `docs/reports/R1/step-4.md`'s newest mark is still `# Revision 2` / `Answers: verdict 50 @ 2158500`, so there is NO new reviewed revision: this counts against **no round** and step 4 stays at **1 of 3**. Written with `--interim` (FS2); no `Closes:` line (FK1). Ruled under **FR1 with EZ0**, and for each row I either give the silently-wrong-result sentence or say I cannot write it. **The `Answers:` check does not fire a HOLD here, and I am saying so rather than leaving it silent:** that check asks whether a REVIEWED REVISION answers the newest verdict, and its own stated reason is that "between a verdict landing and the report answering it the report legitimately predates the findings". That state is EG3 state (2) and it is the premise of an interim check, not a defect -- so revision 2 answering verdict 50 while verdict 51 exists is the designed state, and verdict 51's list (R1168-R1173) is answered in revision 3.
Tests: **1136 passed, 0 failed, 0 skipped** -- MY OWN RUNS AT THE JUDGED COMMIT, in clean worktrees of my own (FV2), over FV1's local selection in full: `tests/unit` **470 passed**, the four root guards plus the two R1-example regression files **247 passed**, `tests/regression/test_r1_published_artifacts.py` **47 passed**, and the three report-parametrised files **372 passed**. **ZERO REDS ANYWHERE.** Lint at the judged commit: `ruff` `All checks passed!`, `black --check` `128 files would be left unchanged.`, `mypy` `Success: no issues found in 45 source files`. **THE WHOLE-SUITE FIGURE IS NOT HERE and `## The run` says why, with the measurement** -- I sampled under GE5 because a `suite_count.py` run is still live in the main tree.
Door (FV2/GE4): **Every measurement in this verdict was taken in `git worktree`s of my own at `c992e54` under the session scratchpad** -- one for the suite, one for every ablation -- so each `git checkout --` restoring an arm ran in MY tree and could not reach the implementer's. In `C:/dev/floatfea` I ran read-only `git`, `gh` and process queries only. **The one write: this verdict file, written by `scripts/write_verdict.py` and committed in `C:/dev/floatfea`, touching `docs/reviews/R1/step-4.md` and nothing else** -- which is the door `docs/SUPERVISOR.md` section FV2 now records as the only one that exists until Xabier rules, because a detached worktree cannot move `F3`. I am naming it rather than tidying it, and nothing of yours moved: your uncommitted `docs/milestones/F2a.md` and untracked `docs/closure/R1.md` are untouched and were never staged.

## Carried

* **R1168 -- ANSWERED, and a new finding came out of the repair.** The closing condition was disjunctive: the caveat carries the guide's qualifier, **or** names which column it means. `floatfea/cli.py:113-114` now carries `WITH A BENDING TERM TO MULTIPLY`, regenerated into all three artifacts, and the zero-moment row is in the test. The first disjunct is met. **The defect the second disjunct was for is still there, and the repair's own new sentence now asserts against it -- R1174 below.**
* **R1169 -- ANSWERED.** `docs/directives/FZ.md` SR-48 now says what the hook does rather than what one refusal looked like. I checked the mechanism and not the prose: `.claude/hooks/protect-reviews.sh:109` is the `UNRESOLVED` pattern and `:205` applies it to the extracted targets, which is the cause SR-48 now names. The `+6 over 3` figure is accepted.
* **R1170 -- STILL OPEN.** The correction belongs in revision 3 and is not in the tree. I reproduced the substance: with `u_combined = amplified` the row fails at **`tests/regression/test_r1_published_artifacts.py:488`**, `assert '3.3.2' in '3.2.3 bending'`, `1 failed, 46 passed`. Your `:488` is right; my `:471` was the pre-edit number.
* **R1171 -- STILL OPEN.** Report prose; revision 3.
* **R1172 -- STILL OPEN.** Report prose; revision 3. **And its species recurred one section earlier -- R1176.**
* **R1173 -- STILL OPEN, in progress.** Witness run 3 is still running and `docs/closure/R1.md` is uncommitted, so nothing published yet certifies the gate. Unchanged as the step's closing condition.
* **R835: unchanged, R2** (GE3). Not re-measured.

## Findings

**R1174. THE REPAIR'S OWN NEW SENTENCE IS FALSE ON THE SHIPPED TABLE, AND MY CORPUS NAMED THE CASE ONE COMMIT EARLIER.** `floatfea/cli.py:115-118`, `results/R1/example/report.md:75` and both CSV headers now read "it is **FLAT in two places**: below the C_m at which amplified overtakes the simpler form ...; and wherever the bending term vanishes". There is a third place, it is in the published table, and it is where five of the seven `amplified` rows live.

```
claim  the caveat's new clause enumerates every flat case in the shipped table
cmd    census of results/R1/example/utilisation.csv: rows with interaction_form ==
       'amplified' and utilisation == utilisation_Cm_sens, split by governing_clause
out    32 rows | amplified 7 | of those FLAT in C_m: 7 | of those u_bending != 0: 7
       governing of the flat ones: {'3.2.4 beam shear': 5, '3.3.2 interaction': 2}
rule   the published clause: "FLAT in two places"
```

The two `3.3.2`-governed ones are cause 2 in substance (`u_bending` = 1.6e-10 and 1.7e-9). **The five beam-shear ones are neither cause**, and four of them carry a bending term that is small but real:

```
out    hub1:buoy2_arm TIP 12.5  u_bending=0.000668252  u_combined=0.00795334  u_shear=0.0808802  U=Cm_sens=0.0808802
       hub3:buoy8_arm TIP 15    u_bending=0.00384156   u_combined=0.00839908  u_shear=0.076495   U=Cm_sens=0.076495
```

On those rows the amplified form governs the 3.3.2 candidate, there IS a bending term to multiply, the interaction value really is C_m-dependent, and the published column is exactly flat because beam shear is about ten times larger. The cause is that `utilisation` is `max` over six candidates, which the sentence never says.

Constructed clean rather than resting on a near-zero term, at the published sensitivity pair (`Cm: 0.85`, `Cm_sensitivity: 1.0`), re-measured at `c992e54` (BP0, CP3):

```
cmd    check_member(axial_n=-6.0e6, moment_y_nm=1.5e8, torsion_nm=5.0e8, cm=0.85|1.00|1.20)
out    cm=0.85  u_combined=0.8145365841867335  U=2.4783285581988657  form=simple
       cm=1.00  u_combined=0.8340589817224682  U=2.4783285581988657  form=amplified
       cm=1.20  u_combined=0.9951911821042186  U=2.4783285581988657  form=amplified
```

Amplified form, full bending term, published utilisation exactly flat across the whole sweep.

**That configuration is `tests/corpus/cm_direction_claim_members.txt` line 84, `id=compression_torsional_shear_governs`, `breaks_second_clause=yes`, committed at `cb520c6` one commit before the repair.** Verdict 51's R1168 named the same thing -- "20 of the 32 shipped rows govern on a clause C_m does not enter at all" -- and offered the "names which column it means" route for exactly it. The repair took the other route and then added a *count* over the axis it had not swept. **This is the sentence's fifth correction (R743, R1156, R1162, R1168, this), and every one was verified against configurations its own author chose.**

*Not blocking, and I cannot write FR1's sentence for it:* no number in any artifact is wrong -- `utilisation` and `utilisation_Cm_sens` are both correct on all 32 rows -- and FR1's own third non-blocking example is a wrong count in prose ("three of five siblings"). So this is a ledger row by the criterion's own precedent, not by my preference. *Closed when* the clause names the real third cause: that `utilisation` is the maximum over clauses, so C_m moves it only where `3.3.2 interaction` governs. **`docs/USER_GUIDE.md`'s own table at 282-286 already says it** -- "14 governed by `3.2.4 beam shear` | none moved -- not an interaction clause" -- while the guide's prose at **:297** repeats the two-cause enumeration. One clause fixes both, which is inside GE2's cap.

**R1175. THE POWERSHELL PARAGRAPH IS WRONG ABOUT THE COMMANDS IT WARNS ABOUT, IN A FILE WHOSE ONLY APPARATUS IS A READER (R1165).** `docs/USER_GUIDE.md:65` -- added in this diff -- reads "The single-quoted `python -c` ... one-liners in sections 6 and 8 are also quoted for a POSIX shell and need their quotes reworked in PowerShell".

```
claim  the guide contains single-quoted `python -c` one-liners
cmd    grep -n -- "\.exe -c \|python -c " docs/USER_GUIDE.md
out    65 (the sentence itself), 490, 890, 915, 937, 951
cmd    grep -on -- "-c '" docs/USER_GUIDE.md
out    (empty)
```

Three things in one sentence. None of the five is `python -c`; all are `.venv/Scripts/python.exe -c`. None is single-quoted; all five are double-quoted outside with single quotes inside -- the opposite way round. And the advice itself is refuted by running them: pasted into PowerShell with their quotes untouched and only the `&` prefix the same paragraph correctly requires,

```
cmd    powershell -NoProfile -File <probe>: & python -c "<guide line 890, verbatim>"
out    platform:hub2_arm ROOT 12.5 1.71167 3.3.2 interaction        exit=0
cmd    powershell -NoProfile -File <probe>: & python -c "<guide line 915, verbatim>"
out    32 rows / [('12.5', 26), ('15', 4), ('16.2', 2)] / over unity: 4        exit=0
```

Both reproduce the guide's own published output byte for byte. "Sections 6 and 8" is the one part that checks out. *Not blocking:* guide prose, FR1's third class, and what it pushes a reader toward is unnecessary work rather than a wrong number. *Closed when* the sentence is cut back to the executable prefix, which is the true part, or re-measured in PowerShell.

**R1176. R1172's SPECIES, ONE SECTION EARLIER, WITH A COMMAND THAT CANNOT REFUTE ITS OWN CLAIM.** Revision 2 section 9 publishes "**What is NOT built is FT2.7**" and "FT2.7 is the plan row that is not built", under `cmd grep -c 'FT2.7' docs/milestones/R1.md` / `out 14`. **FT2.7 is built.**

```
cmd    git log --oneline --diff-filter=A -- tests/regression/test_ft27_topology_solve.py
out    2b3f14e R1 step 3, FT2.7: R868 through a solve, R870's two sentences, ...
cmd    grep -c "def test" tests/regression/test_ft27_topology_solve.py
out    4
```

The command counts how often a **plan** names an id; the claim is about what the **tree** holds. A needle that cannot go red is not a check (BF0, CW0), and this one was aimed at the wrong document entirely. You found it yourself and you were right not to escalate on it. *Not blocking:* report prose, and the FZ (e) escalation it nearly produced was never sent. **Your container question: revision 3 is right, and the reason is mechanical rather than stylistic.** EK3's own measurement is that *any* commit touching a closed report before a newer verdict exists reddens the guards, and reverting the content byte-for-byte does not help -- `7 failed, 16 passed` both ways. An in-place fix would buy a red tree for nothing. *Closed when* revision 3 states it with a command that reads the tree.

**R1177. GE2's CAP.** GE2 said "one line each. No essays." R1168 and R1170 were held to it; R1169's correction is 39 lines in `docs/directives/FZ.md` (`git diff c88b0c0..c992e54 --numstat -- docs/directives/FZ.md` gives `39 0`). The content is good and the one-line lesson is in it. *Not blocking:* directive-form drift in a non-deliverable, no wrong result anywhere. One line, no action asked.

## Tolerances touched

**None.**

```
cmd    git diff c88b0c0..c992e54 --numstat -- floatfea/tolerances.py tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
```

No value, no form, no counter. No conftest or plugin under `tests/` changed, so CH2/CI0 is clear and nothing that writes the gate's own record moved.

**EU1 does not attach -- and I ran the adversarial case anyway, because EU1's lesson is that the configuration nobody chose is the one that measures.** The two new assertions are exact equality and both carry `# not-a-tolerance:`, correctly: `cm * 0.0` is `0.0` at every C_m, so these are the same float and not nearby ones. Five one-line ablation arms, each restored, all inside my own worktree:

```
A  source-only revert of the qualifier (cli.py)       ->  4 failed, 43 passed    [yours, reproduced]
B  artifacts-only revert, all three files             ->  4 failed, 43 passed    [yours, reproduced]
C  cm leaked onto the AXIAL term of `amplified`       ->  1 failed, 46 passed at :555,
                                                          0.02839797981371557 -> 0.05679595962743114   [yours, reproduced]
D  `max(amplified, simple)` -> `amplified`            ->  1 failed at :488, '3.3.2' in '3.2.3 bending'  [R1170, reproduced]
E  cm leaked onto the AXIAL term of `simple` (MINE)   ->  1 failed at :527, the FLAT BAND,
                                                          0.811315867352269 -> 0.8123894396304239
```

**Arm E withdraws your unpublished concern in item 3.** The flat band's equality assertion is NOT shadowed under every one-line ablation: `simple = cm * f_a / (ALLOWABLE_TENSION_FACTOR * fy) + u_bending` keeps the `interaction_form == "simple"` guard true and reddens the band on its own message. It carries its own failure. Do not publish it as a weakness; the correct statement is the ablation that reaches it.

**And the new R1168 row's guard is the strongest one available, which is worth recording because it reads weaker than its siblings.** They guard on `"3.3.2" in governing`; it guards on `interaction_form == "amplified"`. That is forced, not lax: with `u_bending` exactly zero, `u_combined == u_axial`, and `max()` over the candidate dict returns the earlier key, so `governing` is `'3.2.2 compression'` at every C_m and `governing == "3.3.2 interaction"` is **unreachable** at exactly zero bending. Measured at `cm = 0.1, 0.85, 1.0, 2.0`: `form=amplified  gov=3.2.2 compression  U=0.02839797981371557` at all four.

**EH4, both directions, including the one that weakens the gate.** The row's only hidden vacuity is shear or torsion dominating the maximum -- which is the very mechanism R1174 is about -- and nothing in the fixture guards it. Solved:

```
cmd    bisect shear_y_n for the largest value at which arm C still reddens the row
out    5290371.294334104 N
rule   the shipped fixture is shear_y_n = 0.0, so the margin is the whole interval 0 .. 5.29e+06
```

At `shear_y_n = 1.0e7` the row is green under arm C. The shipped point is the maximally non-vacuous one; a later edit adding shear to `common` would silence this row without reddening anything.

## Rulings you asked for

1. **GE's "revision 2" resolved as REVISION 3 under FZ rule 7: I agree, and the mechanical reason is stronger than the convention one.** `_newest_revision()` takes the LAST `# Revision` mark, so renumbering a reviewed revision would move what every report guard measures and make ES0's count unreadable. Correctly not FZ (f): no published number differs between the readings.
2. **GE4: you described what happens rather than what GE4 wished happened, and the description is accurate.** I verified the two load-bearing facts independently rather than taking your pastes: `grep -nE '"(commit|add)"|check_call|\.run\(' scripts/write_verdict.py` is empty, and `git worktree list` has `C:/dev/floatfea` as the only worktree holding `[F3]` with every reviewer worktree detached. The sentence in my own agent file was false and is now right. The open half is correctly unsolved, correctly recorded in `docs/SUPERVISOR.md`, and correctly escalated instead of invented.
3. **The reviewer-instruction changes are NOT a STOP.** `b8d573f` and `5e0808e` are standalone `process:` commits citing GE4 and GE3, touching only `.claude/agents/gating-supervisor.md` and `docs/SUPERVISOR.md`, with nothing from `floatfea/` or `tests/` in either (`git show --stat` on both). Read line by line: both are purely additive, and no guard is removed, narrowed or weakened. GE3's insertion also says in its own text that the FS1/FT1 predicate is unaffected, which is the sentence a later reader needs.
4. **Your three revert arms: reproduced exactly, all three, in a worktree where a restore is safe.** Table above. The arm you disclosed as invalid cost nothing in the end, and disclosing it is why I could re-run the right ones instead of inheriting them.
5. **The guide, read adversarially.** Four new claims checked mechanically and all four hold. The regeneration pipeline really does exit `1` on a clean tree with no output (`git diff -U0 results/R1/example/ | grep ... | grep -v ...` -> no output, `EXIT=1`). The duplicate-key refusal fires with the message you describe and says nothing about the key already in the block: `duplicate key 'required_section' at line 194. YAML's default is last-wins and silent ...`, exit `2`. `required_section: false` really is already at example line 193. And section 7.5's second refusal really is slow and writes nothing: `1248 member-force rows in 80.2 s`, then `32 checked stations in 0.00 s`, then the message, exit `2`, **0 files in the output directory** -- the "nothing partial is left on disk" property measured rather than asserted. Your `67.0 s` and my `80.2 s` are both wall clocks on different loads, which the guide already says differ. **I also went looking for a THIRD slow refusal and did not find one:** `floatfea/run/pipeline.py:571` ("no checked station fell on a governing period") is post-solve, but the obvious route to it is pre-empted by an earlier check -- `governing_periods: [13.0]`, inside the band, gives "names [13.0] s, which dynamic_inputs.npz does not contain" in `0.75 s`. One axis swept; that is not a proof, and the census is non-blocking either way (FR1's second class).

## Corpus (ES0's light clause)

**No batch this round, and the reason is ES0 rather than EG4(e):** an interim check is light by rule -- no corpus batch, no closure list. EG4(e)'s pause is spent by date in any case (28 October), and my agent file and `CLAUDE.md` both still read "pause until 28 October", which is now a dead clause rather than a live one. **The recorded substitute is what I ran instead, and it is what produced this round's lead finding:** a continuum sweep of C_m over the decision rule the caveat describes, and a regeneration-style census of a published deliverable against its own caveat. **Coverage of the standing corpus against this round's repair: batch 51 carries two entries on this axis -- `compression_torsional_shear_governs` and `compression_beam_shear_governs` -- and the repair caught 0 of 2.** Entry 11 is a live counter-example to the sentence the repair shipped, re-measured at `c992e54` above.

## The continuum grid I ran instead of a batch, and what it measured

41 C_m points across the whole declared domain `MOMENT_REDUCTION_CM = ("-", 0.1, 2.0)`, on a random tubular population (diameter 0.5-2.5 m, D/t 20-300, K L/r 20-160, with shear, torsion and moment), the axial force held per member so that each sweep is one member:

```
cmd    sweep check_member over 41 C_m points per member, 2868 non-degenerate members
out    members swept: 2868 | evaluations: 117588
       NEVER LOWERS violated on: 0          <- the caveat's FIRST clause holds
       utilisation ROSE over 0.1 .. 2.0 on: 2426 | EXACTLY FLAT over the whole domain on: 442
       R1174 shape (amplified at C_m = 1.0, u_bending > 1e-6, yet FLAT 0.85 -> 1.0): 898
rule   the caveat as published at c992e54: never lowers; raises wherever the amplified
       form governs with a bending term to multiply; flat in TWO places
```

So the first clause is in good shape -- zero violations in 117588 evaluations -- and **R1174's shape is 898 of 2868 members, 31%, not an edge case**, alongside 5 of the 32 shipped rows.

**One correction to my own probe, recorded because it is this project's own recorded lesson.** My first sweep put `axial_n=-random.uniform(...)` *inside* the C_m comprehension, so each of the 41 points was a different member and the script reported "NEVER LOWERS violated on 1800 members". That figure is withdrawn; it was 41 members compared with each other rather than one member swept. The number above is the corrected run, and the difference is one line.

**The caveat as it reaches the two CSVs reads as THREE items under a count of two**, which is worth one line because it is mechanical and not a choice: `floatfea/cli.py:211` writes comment lines as `line.replace(",", ";")`, so "below the C_m at which amplified overtakes the simpler form the clause also requires, the larger of the two governing; and wherever ..." becomes `A; B; and C`. Whichever way R1174 is repaired, the semicolon pass is what a CSV reader sees.

## The run, and the one figure I did NOT take

**All of this is my own run, at `c992e54`, in clean worktrees of my own (FV2), with `-p no:randomly`. 1136 passed, 0 failed, 0 skipped, across four selections with no overlap:**

```
tests/unit                                                      470 passed in 164.06s
the four FV1 root guards + test_r1_example_regenerates.py
  + test_r1_example_golden.py                                   247 passed in 198.06s
tests/regression/test_r1_published_artifacts.py (the diff's)      47 passed in   0.41s
the three report-parametrised files                             372 passed in  90.33s
ruff check floatfea tests        All checks passed!
black --check floatfea tests     128 files would be left unchanged.
mypy floatfea                    Success: no issues found in 45 source files
```

That is FV1's local selection in full -- the modules the diff touches, `tests/unit`, the four root guards, and the regression tests that read the deliverables this diff regenerates -- and the artifacts regenerate to the committed bytes with only the three wall clocks moving (`solve` 64.39 -> 65.85, `total` 64.51 -> 65.97 in this diff). `U = 1.71167` is unmoved, and the timing exclusion is itself guarded by `test_R845_the_CSVs_carry_NO_excluded_timing_row`.

**The three report-parametrised files are 372 passed, 0 FAILED.** So EG3's two boundary states are both clear at this commit, the FS1/FT1 predicate is not reached because there is nothing to classify, and CZ1 (iv) does not arise.

**THE WHOLE-SUITE FIGURE IS NOT IN THIS VERDICT, AND THE REASON IS A MEASUREMENT RATHER THAN A CHOICE.** I started `python -m pytest -q` at the judged commit and abandoned it at 8% after about a hundred minutes. The cause:

```
claim  a `suite_count.py` run is STILL LIVE in the main tree and is why the machine
       could not give me a whole-suite figure
cmd    Get-CimInstance Win32_Process | where CommandLine -like '*suite-count*'
out    33768  C:\dev\floatfea\.venv\...\python.exe -m pytest -q -p no:randomly
              --ignore=tests/test_report_carried.py --ignore=..._numbers_are_sourced.py
              --ignore=..._guard_states.py
              --junit-xml=...\suite-count-x86d2suk\tree\.suite.xml
       31552  (the same command, a second process)
       33508  ...\suite-count-x86d2suk\tree\scripts\measure\member_forces_table.py --out ...
       18352  (the same command, a second process)
cmd    ls -d C:/Users/xlama/AppData/Local/Temp/suite-count-*
out    fifteen worktrees
rule   the invocation says "I stopped my own `suite_count.py` run rather than have its
       worktree contend with yours"
```

**The stop did not take.** *Not blocking, and nothing is at risk in the repository:* every `--out` goes to a pytest tmpdir under `TEMP`, and `git status --short -- results/ scripts/` in the main tree is empty, so no deliverable is being written by a stale-commit process. **GE5 is the clause that covers what I did instead** -- "if it costs time again, sample the child, per the reviewer" -- so I sampled, and the sample is FV1's own selection rather than an arbitrary slice. **Two things for revision 3:** confirm that run's figure is not published (it is at a stale commit by your own account, and a stale published count is R1047's defect), and take the whole-suite line at the revision's own commit with nothing else running.

**CI at `c992e54`: run `42553224916`, still `in_progress` at every point I measured it, so it is NOT a pass and I am recording it as unfinished rather than as green.** It is not CK2's exhausted-allowance state -- the jobs have steps, real durations and a runner. What has completed:

```
lint, unit and guards            completed  success   -- every step RAN, none skipped,
                                 including `guards and meta-tests`, `ruff`, `black`,
                                 `mypy`, `actionlint` and `unit tests`
the verification ladder          in_progress -- rungs 1, 2 and 3 `success`; rung 6 running;
                                 rungs 4 and 5 pending
CI determinism -- leg            skipped (its own condition)
CI determinism -- ten legs agree skipped (its own condition)
```

**Nothing is red.** `guards and meta-tests` reaching the runner and passing is the thing CZ1 (iii) exists to see, and it did. An unfinished run is neither a pass nor a red, so it is not CZ0 (d) and it does not hold the step; it is a check to complete before revision 3, and if the ladder reddens that is FF0-class and goes in the next commit ahead of everything else.

## Next step opens when

Step 4 is still open, this interim check closes nothing, and step 4 stays at **1 of 3** reviewed revisions. For **revision 3**, under GE1's "nothing else of substance":

1. **R1173**: witness run 3 completes with no help, and `docs/closure/R1.md` is committed with every run's transcript and each fixture's result against expected. Still the step's closing condition.
2. **R1174**: the caveat's third flat cause named in `floatfea/cli.py`, regenerated into all three artifacts, and `docs/USER_GUIDE.md:297` brought into line with its own table at 282-286. One clause, inside GE2's cap.
3. **R1170, R1171, R1172, R1175, R1176** answered in revision 3's prose, each at the site named, with every `out` line re-taken after the last edit (CP3).
4. **`docs/milestones/F2a.md` is modified and uncommitted** in the main tree as of this check -- commit it, so GE3's routing of R835 is in the tree rather than in a working file.
5. **CI at the revision's own commit completed and green**, with the job-level table in the report (FP1), and the whole-suite line taken at that commit with the `suite_count.py` run of this turn confirmed dead and its figure unpublished.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4
Reviewed commit: 687685431bcd3c8798811f7757fb03365bd4d932
**Reviewed commit: `687685431bcd3c8798811f7757fb03365bd4d932`.**
Verdict: PASS
Reviewed commit: 687685431bcd3c8798811f7757fb03365bd4d932
Scope: **R1 step 4, REVISION 2 -- the SECOND of ES0's three reviewed revisions.** Step 4 stood at 0 of 3 (verdicts 49 and 50 were interim checks and cost none); it stands at **1 of 3** after this. **Nothing is closed** -- no `Closes:` line (FK1).
Tests: **4329 passed, 0 failed, 0 skipped** -- MY OWN RUN AT THE JUDGED COMMIT, in clean worktrees of my own (FV2), in EI0's two halves: the main half **3957 passed, 0 failed, 0 skipped in 2824.73s (0:47:04)**, and the three report-parametrised files **372 passed, 0 failed in 76.04s**, both at `6876854`. **ZERO REDS ANYWHERE.** So EG3's two boundary states are both CLEAR at this commit -- the report answers the newest verdict -- and FS1/FT1's predicate is not reached, because there is nothing to classify. CZ1 (iv) does not arise.
Ruled under **FR1 with EZ0**, as the invocation asks. **NOTHING BLOCKS**, and for each ledger row I give the FR1 sentence rather than a classification. Six rows, one line each (GA3).
CI (FP1), taken by me at the judged commit: run **42456514283**, event `push`. **`lint, unit and guards` is `completed/SUCCESS`** -- `actionlint`, `ruff`, `black --check`, `mypy`, `unit tests` AND **`guards and meta-tests`** all `success`. That last step is the one CZ1 (iii) exists to see RUN rather than skipped behind an earlier red, and this is the first commit in step 4 at which it is green. **And the whole run is `completed/SUCCESS`**: all six ladder rungs -- `1, 2, 3, 6, 4, 5` -- `success`. Rung 6 is where `tests/regression` runs (`.github/workflows/ci.yml:510`, `sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression`), and it is the only CI coverage of the one test file this commit touches, so I waited for it rather than ruling on a partial run. **There is no red at the judged commit on either machine, mine or GitHub's**, so CA2 is not reached and no waiver is needed.

**WHERE I WORKED (FV2).** Two worktrees of my own outside the repository, both detached at `6876854`. No `checkout`, `reset` or write of any kind in the implementer's tree except the two sanctioned ones -- the corpus commit `cb520c6` and this verdict. `git status --porcelain` there was empty before I wrote and HEAD was `6876854`. Every ablation arm was reverted inside my own worktree with `git checkout --` and `git status --porcelain` checked empty each time.

**STEP 1b: THE `Answers:` HEADER NAMES THE NEWEST VERDICT.** Revision 2 reads `Answers: verdict 50 @ 2158500`; `grep -c "^Verdict:" docs/reviews/R1/step-4.md` is **3** and verdict 50 is the newest. No HOLD on 1b.

**THE MANDATED SEPARATE DIFFS, 2158500..HEAD, three commits -- all four empty.**

```
cmd  git diff 2158500..HEAD --numstat -- floatfea/tolerances.py          ->  (empty)
cmd  git diff 2158500..HEAD --numstat -- tests/conftest.py "tests/**/conftest.py"  ->  (empty)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"  ->  tests/conftest.py
     -- the pathspec RESOLVES, so no CH2/CI0 channel is opened
cmd  git diff --stat 2158500..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md  ->  (empty)
     -- NO STOP-class finding. `ec93df6` touches a GATE but not my instructions
cmd  git diff --stat 2158500..HEAD -- tests/corpus docs/reviews  ->  (empty)
```

## Carried

| item | status | measured by me |
|---|---|---|
| **R1157, R1158** (the guide cited a committed `solve` row its own commit had moved) | **ANSWERED by WITHDRAWAL, which is the stronger branch of the closing condition** | the timing-row needle `^\| *(build\|load\|solve\|code_check\|total) *\| *[0-9]` gives **0** in `docs/USER_GUIDE.md` and **5** in `results/R1/example/report.md`, so the needle reporting the absence has a control that it finds (CW0). `grep -c "190.07|70.47|64.08|63.96" docs/USER_GUIDE.md` -> **0**. Section 8.7 now names the row LABELS instead, and I ran that check -- see "Try to break it" |
| **R1159** (10 of 32 for a sentence about both columns) | **ANSWERED, reproduced to the row** | my own read of the shipped CSV: `Cm_sens differs 10 | K_sens differs 2 | either 12 | of 32 rows`. The guide now carries all three |
| **R1160** (`1e-10` where it is `9.5e-10`) | **ANSWERED, reproduced** | the four platform-arm `static` ROOT torsions are `0`, `-3.515518e-24`, `-9.513095e-10`, `-1.240771e-24`; largest in magnitude `9.513095e-10`, which the guide now prints in full. `My = +1.916016e+08` with `Mz = N = 0` on all four, so FL1(c)'s fifth fixture holds in the same read |
| **R1161** (lambda is the Froude scale in 4.1/4.7 and the wavelength in 7.3/8.3) | **ANSWERED by a note in 7.3, and every figure in it checks out** | `L = 9.81*12.5^2/(2*pi) = 243.95`; `24.2/243.95 = 0.0992`, which is what the refusal prints; `24.2/50 = 0.484` against `1/7 = 0.1429`; and 8.3's `T = 10 s` row is `24.2/156.13 = 0.1550 > 0.1429`, so the cross-reference to 8.3 holds too. `floatfea/loads/period_band.py:165` is `def deep_water_wavelength` -- the citation resolves |
| **R1162** (the published caveat's "RAISES" was non-strict) | **FIXED rather than ledgered, and I endorse the call. The repair's SECOND clause is now unconditional and false -- that is R1168** | the caveat's first clause ("never lowers") is right on all 12 of my corpus entries on both readings. The gate reddens on each half of the repair alone, and I ablated the flat-band assertion DIRECTLY rather than accept the published cell -- see R1170 |
| **R1163** (the compression control is blind to a C_m defect in `[0.85, 0.9758)`) | **ANSWERED by measurement with the gate NOT re-aimed, and the magnitude claim reproduced rather than relayed** | `CM_JOINT_TRANSLATION 0.85 -> 0.8585`, one line, in my own worktree: **2 failed, 85 passed**, the two `test_G61_...` ids by name; restored, **87 passed**. The overtake reproduces at `cm = 0.9757684714917533` and the new control asserts `0.90`, inside the band |
| **R1164** (the provenance roll did not mention GD) | **ANSWERED** | the roll carries `GD` once, with `GC.md:109-144` as where its text is |
| **R1165** (the guide is a published deliverable no guard reads) | **CORRECTLY NOT REPAIRED; it is on `docs/milestones/F2a.md:353` with what a gate would assert and why extending `ROOTS` is the wrong shape** | GA1 and "no new apparatus through F6" both forbid building it. The reviewer's reading is the bound until R2, which is why I ran the regeneration check, the lambda arithmetic and every figure in the new prose myself |
| **R1147** (the delta is six rows over three paths, not four over one) | **ANSWERED at all SEVEN named sites, and the EH4 table RE-RUN rather than extended by hand** | I reproduced BOTH figures. At `66c7331` with that commit's own newest verdict as `VERDICT_TEXT`: **2255 -> 2261, gained 6, lost 0, 3 distinct paths**, the six by `(finding, path)`. At `6876854`: **NEW 94, OLD 83, gained 11, lost 0, 7 paths**, and the EH4 table row for row -- including `.gitattributes-backup -> site? False` and `x.gitattributes -> no match`. The instability note (three, four, six, eleven, each with its commit) is right and is R861 again |
| **R1148** (`carried_table.SITE` lacked the lookbehind) | **ANSWERED in `6ec0425`, ablated at verdict 49; not reopened** | unchanged |
| **R1150** (EQ0 cited where GB2 governs) | **ANSWERED in all three places** | revision 1's section 1 (`:79`) and section 5 (`:357`) and the answers file's `_` block (`:17`) all say EQ0 is cited by ANALOGY; `docs/directives/GB.md:26` is cited as the authority; DK0's reason is stated |
| **R1151, R1152, R1153, R1154** (closure items) | **all four CLOSED** | the stray `#` is gone; the roll lists `GB.md` once; section 4's bold line is scoped to `.gitattributes` with a pointer to section 2; `EG3 STATE (1)` is now named in revision 1's section 11 |
| **R1166** (the answers-file needle matched a bare basename) | **FIXED in `ec93df6`, correctly -- my ruling is in answer 3** | reproduced over all 21 step reports: **agree-and-resolve 13 | agree-and-match-nothing 7 | differ 1**, the one being this report, where the OLD needle resolves to a file that is not there and the NEW one to a file that is. **Nothing is LOST by the narrowing**: the no-match path falls back to the conventional location |
| **R1167** (the implementer's own justification for R1162 was wrong) | **SELF-FOUND, corrected in place and dated, and the replacement measurement reproduces exactly -- answer 2** | from the shipped CSV: of the twelve `3.3.2 interaction` rows the **10 that move are `simple` at `C_m = 0.85`** and the **2 that do not are `amplified`** with `u_bending` of `1.592660e-10` and `1.717740e-09`, both at a TIP station. The causal half is deductive, not merely observed: `simple` is C_m-free, so a row whose `Cm_sens` differs cannot still be on `simple` at `1.0` |
| **R1149** (EG4(e)'s pause expired 28 October) | **ANSWERED by GC3 -- it stays expired, batches at my discretion. I ran one** | batch 51, `cb520c6`, committed separately from this verdict. 12 entries, all new |
| **R835 / R861** (EG3's enumeration is a function of what the reviewer writes) | **still open, still Xabier's. Measured again this round, from the COLLECTION side** | the three report files collect **622 cases at `ec93df6` and 372 at `6876854`**, and go from **87 failed to 0 failed**, because `SITES` and `EXPECTED` are parametrised over the newest verdict and the carried set. No test changed between those two trees. ELEVENTH measurement; relayed, not re-litigated |
| **`docs/SUPERVISOR.md` says `write_verdict.py` "commits to the branch"** | **still open, still MINE, and it bound me again** | the script does not commit at all, and the only tree where a commit reaches branch `F3` is the implementer's -- which FV2 tells me never to write in. I used the two sanctioned doors and nothing else and left the tree clean. Recorded a second time rather than resolved inside a round |
| **verdict 47 item 10(a)** (`docs/closure/R1.md` must carry the `cz1-closure-outputs` block the moment it exists) | **STILL LIVE** | `ls docs/closure/` gives `F2 F3 F4 F6 F6a F6b` and no `R1.md` |
| **CZ1 (ii)/(iii)'s four outputs** | **owed at a closure commit that still does not exist** | unchanged |
| **step 4's OWN GATE, the witness half** | **NOT EVIDENCED, and no carried item held it until now -- that is R1173** | see the finding |

## Findings

**NOTHING BLOCKS.** No tolerance moved, no declared input moved, CI's lint-and-guards job is green at the judged commit, the three report-parametrised files are **0 failed** there, and the published artifacts regenerate byte-for-byte except two wall clocks. Six ledger rows follow, one line each, each with the FR1 sentence.

**R1168 -- the one I nearly blocked on.** `floatfea/cli.py:111-113` and the same sentence in `results/R1/example/report.md` and both published CSV headers: R1162's repair corrected the first clause and left the second UNCONDITIONAL -- "RAISES it wherever the amplified form governs". It is **false** for a compression member with no bending term: `check_member(axial_n=-6.0e6, moment_y_nm=0.0)` gives `interaction_form = "amplified"` and `U = 0.02839797981371557` at `cm = 0.85, 1.0, 1.2 and 2.0`, EXACTLY equal -- a zero-moment brace, not a degenerate case. It is false again under the other reading of "the compression utilisation": with `torsion_nm=5.0e8` the `u_combined` column rises `0.814537 -> 0.995191` while the PUBLISHED `utilisation` column is exactly flat, and 20 of the 32 shipped rows govern on a clause C_m does not enter at all. **`docs/USER_GUIDE.md` section 4.6 carries the qualifier the caveat does not** -- "raises it wherever the amplified form governs *with a bending term to multiply*" -- so the two published deliverables SR-45 was written to reconcile **still disagree, on the very clause R1167 is about.** *Not blocking:* no number is wrong and the outcome is right in sign -- "never lowers" holds on all 12 corpus entries on both readings -- which is FR1's first non-blocking class one step across. **This is the sentence's FOURTH correction (R743, R1156, R1162, this).** *Closed when* the caveat carries the guide's qualifier, or names which column it means; the existing `"NEVER LOWERS" in text` row already pins the string, so it is one string and no new apparatus.

**R1169.** `docs/directives/FZ.md` SR-48 and revision 2 section 2 both state that `git show 66c7331:docs/reviews/R1/step-3.md` redirected into the scratchpad is "**refused by the `PreToolUse` hook**". **It is not, at this commit.** FX1 changed the clause to extract redirect TARGETS and test them one by one, and the hook's own comment names `wc -l <a verdict> > /tmp/n` as a read the PREVIOUS form denied. Measured, by running `.claude/hooks/protect-reviews.sh` by hand with that command as a main-session caller: **empty output, exit 0 -- ALLOW**; `cp docs/reviews/R1/step-3.md <elsewhere>` on the same harness is **DENY**, so the probe discriminates. `.claude/settings.json` carries no deny rule, so nothing else could have refused it. **And the figure needs no redirect at all:** pipe the blob into a process and set `VERDICT_TEXT` in memory, which is what I did. *Not blocking:* the figure the non-reproduction protected is CORRECT, so nothing downstream is wrong, and FM1 was never engaged because no workaround was needed. *Closed when* SR-48 says what the hook actually does, or pastes the refusal.

**R1170.** Revision 2 section 5's cell for the `max()` ablation reports "**1 failed** -- at the flat-band assertion, which is the one that should fire". The count is right and the attribution is wrong: with `u_combined = amplified` the row fails at **`tests/regression/test_r1_published_artifacts.py:471`**, the BRANCH GUARD -- `"3.3.2" in compress_lo.governing`, which becomes `"3.2.3 bending"` -- and never reaches `:501`. **I then ablated the flat band directly** (the amplification scaled by `1.2` so the overtake falls below `0.85`, one line, restored) and it DOES redden at `:501` with its own message, so the new control is not vacuous. *Not blocking:* the gate carries its own failure; the sentence about which assertion carries it does not, which is BG0 and the same species as R1167 three paragraphs earlier in the same section. *Closed when* the cell names `:471` and keeps an ablation that reaches `:501`.

**R1171.** Three published `out` lines in revision 2 are false AT THE COMMIT, all by one mechanism -- a needle that matches the prose written around it after the figure was pasted (CP3: an edit after the paste voids the paste). Section 2's `(no output)` prints **3** lines, all inside revision 2's own repair table and its own `cmd`. Section 3's `2` is **8**. Section 5's `1` is **2**, the second being the `cmd` line itself. In all three the SUBSTANCE holds -- I checked the seven R1147 sites, the three R1150 sites and revision 1's `EG3 STATE (1)` sentence individually. *Not blocking:* report prose, FR1's third class. **The revision already records this species about a fourth needle** -- "anchored on the row LABEL and matched section 8.7's own new prose, which is why it carries a control and a digit now" -- and these three did not get that treatment. *Closed when* each is re-taken after the last edit, or scoped to exclude its own section.

**R1172.** Section 11's whole-suite line names **`092334a`**, two commits before the judged one, and its `note` justifies the gap for `ec93df6` only -- correctly, since that commit touches a file inside `suite_count.py`'s own exclusion. It is silent about **`6876854` itself**, which changes `tests/regression/test_r1_published_artifacts.py` (an assertion message) and `docs/milestones/F2a.md`, and both are inside the MAIN half: the first is a main-half test file, the second is read by `test_tree_prose_consistent.py`'s `ROOTS`. *Not blocking:* the complement IS measured -- the commit's own FV1 block gives `47 passed` on that file and `269 passed` on the four root guards plus it, at the final tree -- and **my own main half AT THE JUDGED COMMIT is `3957 passed, 0 failed, 0 skipped in 2824.73s`, identical to the published figure**, so the stale provenance cost nothing this time -- which is why this is a ledger row and not a block, and not a reason to leave the note as it stands. *Closed when* the note names both commits, or the line is taken at the report's own commit.

**R1173. STEP 4's GATE IS HALF-UNEVIDENCED, AND NO ITEM CARRIED IT UNTIL NOW.** `docs/milestones/R1.md` section 3, step 4: "a fresh-context agent with no history clones the repo, follows **only** `docs/USER_GUIDE.md`, and reproduces step 1's five fixtures. **Its transcript goes in `docs/closure/R1.md`.**" The witness ran, and it earned R1156 plus three guide repairs, and `a596fa7`'s message is a good account of what it got STUCK on. What no file in this repository says is that it **reproduced the five fixtures**: `grep -rn "transcript" docs/reports/R1/ docs/digests/2026-11-0*.md` is **empty**, `docs/closure/R1.md` does not exist, and SR-44 records that the witness's worktree was made from `master`, which carries no guide, so it recovered with `git log --all -- "*USER_GUIDE*"` -- not a user action, and not "follows only the guide". Revision 2 section 9 nonetheless reads "the step's own work -- the guide and the witness -- is done". *Not blocking, and the reasoning is on the record because I nearly did block:* FR1 asks for the silently wrong result and today there is none -- the closure artifact does not exist, so nothing published asserts the gate is met, and verdict 47 item 10(a) already holds the closure's own obligations. The wrong result is PROSPECTIVE: the moment `docs/closure/R1.md` certifies FL3(b), a deliverable sent to Xabier asserts a reproduction nothing in the repository recorded. **So it does not block this revision and it IS the condition the step closes on**, stated two days before FW0's date rather than inside the closure.

## Answers to the six questions, since you asked for the rulings and not the outcomes

1. **R1162: fixing a ledgered item was RIGHT, and your replacement justification IS measured.** A ledger ruling is a floor on what blocks, not a ceiling on what may be repaired -- SR-45 says exactly that and it is the correct reading of FR1; FZ rule 5 is the authority, and the repair arrived with a named row that reddens on a revert of each half alone. The replacement ground -- "unconditionally false for a member inside the flat band, with the control at the test's own member" -- is measured, and I reproduced the control: `cm = 0.90` gives `interaction_form = "simple"` and the same float as `0.85`. It is **not** the same shape of unmeasured sentence, because the band is EXHIBITED at a member rather than argued from the formula. What is still unmeasured is the OTHER clause of the same sentence, and that is R1168.
2. **R1167's replacement measurement: taken from the CSV myself, and it reproduces to the digit.** 10 moved / 2 unmoved; the 10 all `simple` at `0.85`, the 2 both `amplified` at `1.592660e-10` and `1.717740e-09`. And the causal half is deductive rather than merely observed, which is stronger than the report claims for it: `simple` carries no C_m, so a row whose `Cm_sens` differs from `utilisation` CANNOT still be on `simple` at `C_m = 1.0` -- the overtake is forced by the data, not inferred from it.
3. **R1166: `ec93df6` is a commit you were REQUIRED to make, and GA1's test is satisfied on the information rather than on the colour.** FF0 settles it outright and names the class -- "the report guards ... is fixed in the next commit" -- and its recorded reason is your own objection answered in advance: C89 kept the suite red by eight for a whole milestone, and "a tree that is red by design is a tree in which the next real red is harder to see." On GA1's own words, "could hide a blocking finding": a red that is identical for a right table and a wrong one hides the FINDING while showing a colour. That is your argument and I accept it. GA1's freeze clause is not touched either -- no new guard, a needle repaired under EK2, no `is_file()` fallback, and nothing lost (13 agree-and-resolve, 7 fall back to the convention, 0 lost).
4. **Citing my figure was acceptable and revision 2 owes no reproduction -- but the route you could not find exists, and R1169 is that the reason you gave for not using it is untrue.** You did the right thing twice: you refused to rephrase past a hook (FM1), and you said plainly that you had not reproduced it instead of implying you had. The route needs no redirect and no worktree: `git show <sha>:docs/reviews/...` piped into a process that sets `VERDICT_TEXT` in memory. I ran it, and `+6 rows over 3 paths, 0 lost` is correct.
5. **Your widened `EXPECTED`-plus-`SITES` domain is the right one, and relaying my ruling is good enough -- but the question is MOOT at the judged commit.** The three report files are **372 passed, 0 failed** at `6876854` in my own worktree, and CI's `guards and meta-tests` step agrees on a machine neither of us controls. **There are no reds to classify**, so FS1/FT1 and CZ1 (iv) are not reached and the three ids you flagged do not arise. Your first probe's narrowness is the right thing to have recorded rather than quietly widened: a needle narrower than the guard it audits is this project's recurring species, and you caught it in your own work.
6. **The guide's new prose: I ran all of it, and the one wrong figure I found is in the CAVEAT, not in the guide.** Section 4.6's two-mechanism paragraph, section 7.3's lambda note and section 8.5's torsion figure all check out to the digit -- the arithmetic is in the `Carried` rows above. Section 8.7's rewritten claim is the one I was most suspicious of, because it replaces four numbers with a universal, and it holds: see "Try to break it". Your instinct is right that a user finding one of these is worse than my finding it, and R1165 is the honest answer -- the bound is a reader until R2 opens, so the reading has to be done at every revision rather than once.

## Tolerances touched

**None, and EU1 does not attach** -- and it would not attach anyway, since this is a reviewed revision and not an interim check.

```
cmd  git diff 2158500..HEAD --numstat -- floatfea/tolerances.py   ->  (empty)
cmd  git diff 2158500..HEAD -- floatfea tests scripts | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance"  ->  (no match)
rule CLAUDE.md section Tolerances, including anything functioning as a tolerance under
     another name -- a convergence threshold, a comparison epsilon, a tier cutoff
judge no tolerance VALUE and no DECLARED COUNTER moved. The two assertions the diff adds
     are EXACT equality and both carry `# not-a-tolerance:`. **I ran the adversarial
     configurations anyway** -- R694's lesson is that a value which does not move is the
     worst case and not the safest -- over the twelve corpus members including C_m at
     BOTH ends of its declared domain `MOMENT_REDUCTION_CM = ("-", 0.1, 2.0)`, and that
     sweep is where R1168 came from. The one number in the diff that could have been a
     threshold and is not: `cm = 0.90` in the new control is a point INSIDE a measured
     band whose own edge is published at `0.9757684714917533`
```

## Try to break it -- what I ran, and what it found

* **The regeneration check on the published deliverables, which is the recorded substitute's second half.** `floatfea run examples/platform12_placeholder.yaml` in a clean worktree of mine: `governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)` -- FL1(c)'s fixture to the digit, on a machine the commit was not written on, with `707/884/990/1061/1146/1415` steps and `1248` rows. The guide's 8.7 gate (the FILTERED diff) printed **nothing**, the unfiltered diff printed exactly four lines -- `solve` and `total` -- and `git diff --numstat results/R1/example/` is `2 2 report.md` and nothing else. **So 8.7's new universal holds**: every line it printed was one of the five row labels, which is the claim that replaced the withdrawn figures.
* **A continuum sweep over the parameter space the C_m caveat guards**, which is the substitute's first half, and it is where **R1168** came from: twelve member configurations, both ends of C_m's declared domain, zero and tiny and substantial bending, all five governing clauses, and the minus-zero axial boundary. `12 of 12 rule as written, 0 disagree`.
* **The flat-band control ablated DIRECTLY rather than through the `max()`.** That is R1170: the published cell's ablation never reaches the new assertion; mine does, and the assertion is sound.
* **The C_m magnitude gate reverted at one per cent.** `2 failed, 85 passed`, both `test_G61_...` ids by name, restored to `87 passed`. R1163's "the magnitude is held elsewhere" is true and the gate is sharp.
* **R1147's delta measured at BOTH verdict states**, which is the only way to show the count is a property of the newest verdict rather than of the pattern: `+6/3` at `66c7331` and `+11/7` at `6876854`, 0 lost in both, and the EH4 table reproduced row for row.
* **The hook exercised rather than assumed** (R1169): three commands through `protect-reviews.sh` by hand, one allow and one deny, so the probe discriminates.
* **The `_ANSWERS_PATH` narrowing in the direction that LOSES a site** -- EH4's weakening direction, and my own standing note that a narrowed predicate opens a hole the wider one covered. Over all 21 step reports: 13 agree and resolve, 7 match nothing and fall back to the conventional path, 1 differs and the new one is right. **Nothing is lost.**
* **What I did not find, and it is much the larger part.** Every figure in this revision's repairs that I re-took came back exactly right: the 10/2/12 split, `9.513095e-10`, `243.95 / 0.0992 / 0.484 / 0.1429 / 0.1550`, the overtake at `0.9757684714917533`, the `2 failed, 85 passed`, the `21/13/7/1` needle control, both R1147 deltas, and the EH4 table. Three of the six ledger rows are the implementer's OWN corrections to its own work, found inside the same hour it made them (R1166, R1167, and SR-49's near-miss). **SR-49 is the most useful paragraph in the diff**: a heading anchor that exists in BOTH revisions duplicated 3610 lines, `_newest_revision()` would have measured the DUPLICATE, every report guard would have been green on it, and what caught it was the next edit asserting its anchor was unique. That is a guard-shaped hole reported by the one person who could have hidden it.

## A CORRECTION TO MY TWO PREDECESSORS, because it has now cost three reviewers an hour each

**The "frozen" suite is not frozen, it is not OneDrive, and it is not worktree contention. The parent process is BLOCKED IN `subprocess.wait()` and the reviewer has been sampling the wrong process.** Verdict 48 killed its combined run after "824 s of CPU and then frozen ... zero CPU movement over 20 s" and attributed it to a `.git` on OneDrive. Verdict 49 refuted the OneDrive half correctly -- same symptom on local disk, and it resumed -- and then attributed it to "contention between my own concurrent worktrees over one shared object store", at **exactly 9% complete**, which is where mine stopped too. Both diagnoses are wrong, and the measurement that settles it is sampling the CHILD:

```
cmd   the child processes of the stalled pytest, by command line
out   python scripts/measure/member_forces_table.py --out <tmp>/forces.csv
        --summary <tmp>/forces.md --provenance <tmp>/mutated.provenance.json
      -- spawned by test_R951_the_TWO_GENERATORS...
cell  child and parent CPU sampled TOGETHER, four times, 6 s apart
out   23:23:40  child=62.42   parent=787.203125
      23:23:46  child=gone    parent=787.218750
      23:23:52  child=gone    parent=787.218750
      23:23:58  child=gone    parent=787.234375
judge the CHILD was burning CPU and then exited; the PARENT moved by 31 ms, which is
      what a process blocked in `subprocess.wait()` looks like. `member_forces_table.py`
      is a full solve, ~60 s of child CPU each, and `grep -rln member_forces_table tests/`
      names seven test modules, one of which has 37 cases. The 9% plateau is that block
rule  my own recorded guard -- "assertion domain blindness": the collection the
      measurement inspects cannot contain the thing it is looking for. A parent's CPU
      counter cannot show a child's work. Three reviewers in three rounds have sampled it
```

**Consequence, so nobody pays this again:** do not kill it, do not serialise for THIS reason, and if you want to know whether it is alive, sample the child. The two halves still want serialising for the window, which is EI0's reason and is unaffected.

## Corpus (EG4(e) / GC3)

**THE PAUSE IS EXPIRED (R1149) AND GC3 LEAVES IT EXPIRED, SO I RAN A BATCH -- and I ran both halves of the recorded substitute as well, and both paid.** `tests/corpus/cm_direction_claim_members.txt`, **12 entries, ALL NEW**, committed separately from this verdict in `cb520c6`.

**The coverage measurement my instructions ask for, which is the number that matters rather than mine:** of the twelve shapes, **3 are evaluated by a shipped row** -- the flat band below the overtake (revision 2's own new control), the tension case, and the strict rise under compression with a substantial moment -- and **9 by nothing**. The two that REFUTE the published sentence are both among the nine, `pure_axial_compression_zero_moment` and `compression_torsional_shear_governs`, because **no shipped row varies C_m at zero bending moment, and no shipped row asserts anything about the `utilisation` column under C_m at all.** Measured: `cm=` appears in four rows of `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py` and seven of `tests/regression/test_r1_published_artifacts.py`, and in all eleven the moment is non-zero and the quantity asserted is `u_combined`. **The planted-shape count for this sentence is three repairs over three axes; the axis that refutes it is the fourth, and a corpus is what found it.**

## Next step opens when

**STEP 4 STAYS OPEN at 1 of 3 reviewed revisions. Nothing is closed by this verdict.** There is no step 5 -- the plan's header is "STOP after R1 closes" -- so what follows is revision 3 and then the closure.

1. **R1173 FIRST, BECAUSE IT IS THE STEP'S GATE.** Either the witness transcript exists and records the five fixtures reproduced from the guide alone -- in `docs/closure/R1.md`, which is where the plan puts it -- or the witness is re-run from a clone of the branch that actually carries the guide, and its transcript goes there. **Nothing else in step 4 is load-bearing by comparison, and revision 2 asserts this half is "done" while no file in the repository evidences it.** It is two days to FW0's date and this is the one item in this step whose cost I cannot bound for you; if re-running the witness puts 10 November at risk, FZ (e) says so on the day you know it, not in the closure.
2. **R1168 is one string and I would take it in the same commit.** The caveat should carry the guide's own qualifier, or say which column it means. The row that pins the string already exists, so this is a repair and not new apparatus.
3. **R1169, R1170, R1171 and R1172 together: four prose corrections, one commit, no investigation and no census of siblings (GA1).** Each is one line and each has its command above.
4. **The closure, when it comes, is CZ1's four outputs in that order, and EQ0 makes it REVIEWED if it moves a gate or a tolerance** -- R1168's string edit would, which is a reason to take it in revision 3 rather than in the closure. Verdict 47 item 10(a) stands: `docs/closure/R1.md` must carry the `cz1-closure-outputs` block the moment it exists, or `cz1_record()` returns the empty string and the report guards fail with no fallback.
5. **R835/R861 and the `docs/SUPERVISOR.md` contradiction remain MINE and go to Xabier, not into a round.** The collection figure is R861's eleventh measurement: `622 -> 372` cases and `87 -> 0` failures across one verdict boundary, with no test changed between the trees.
6. **The schedule, in your own frame.** GD2 put revision 2 at end of 9 November and it is pushed on the 7th -- two days inside. FW0's R1 date is 10 November and unchanged. **I do not escalate under FZ (e) either**, because I am not forecasting a slip; but R1173 is the first thing in this step whose cost is not a one-line repair, and revision 3 is the last revision that can report a slip the day it is known rather than after.

*Length: this runs past GA3's 150-line target, in the `Carried` table and in the six answers. The invocation asked for those rulings rather than their outcomes, and I would rather hand you the commands than the adjective.*


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: a596fa76b969b6bbf680df9029b94aabd45112a4
**Reviewed commit: `a596fa76b969b6bbf680df9029b94aabd45112a4`.**
Verdict: PASS
Tests: **45 failed, 517 passed in 211.61s** in the three report-parametrised files, measured by me AT MY OWN VERDICT COMMIT `954e69d` -- which is EG3 (ii), the half no verdict in this milestone had measured until recently. The whole-suite figure is unchanged from the entry below: **4477 passed, 42 failed, 0 skipped** of 4519 at `a596fa7`, with CI run `42446638701` red only at `guards and meta-tests` and the whole verification ladder green.
Scope: **ADDENDUM to the ES0 interim check below, on the same commit. It counts against no round either, and closes nothing** -- no `Closes:` line (FK1). It adds no new finding: it **RENUMBERS the nine ledger rows of that entry from `L1`-`L9` to `R1157`-`R1165`** so that the gating mechanism can see them. Everything else in that entry stands unaltered, and its measurements are where the evidence is.

**WHY THIS ADDENDUM EXISTS, AND IT IS A DEFECT OF MINE.** I wrote my nine ledger rows as `**L1.` ... `**L9.`, following GA3's "one ledger line each". `tests/test_report_carried.py:237` extracts a verdict's findings with

```
_FINDING = re.compile(r"^(?:\*\*|#{2,4}\s+)(R\d+)(?:[.\s]|,(?!\s*R\d))", re.MULTILINE)
```

so **an `L`-labelled row is not a finding to the guard at all.** Measured at `954e69d`: `test_the_report_carries_the_finding` is parametrised over **R518 and R1147-R1154 -- verdict 48's findings -- and not one of mine**, and `_FINDING.findall(VERDICT_TEXT)` is non-empty only because verdict 48's preserved entry is still in the file. So the mechanism would have gone green on a report that answered the previous round and ignored this one, and nothing would have said so.

**That is this project's recurring species, committed from my side of the loop: a check whose collection cannot contain the thing it is looking for.** It is also why the renumbering is the repair and a sentence asking the implementer to remember is not -- ES0 says an interim check's findings join the step's list, and the list is read by a machine.

## Carried

Everything in the entry below, unchanged -- R1148 answered and ablated, R1139 answered, R1147/R1150/R1151/R1152/R1153/R1154 deferred to revision 2 under GC4, R1149 and R835/R861 mine and Xabier's, verdict 47 item 10(a) still live, CZ1's four outputs owed at a closure commit that does not exist. **Nothing is added and nothing is withdrawn.**

## Findings

**NOTHING BLOCKS.** The nine below are the SAME nine rows as `L1`-`L9` in the entry beneath this one, renumbered. Each is a ledger row under FR1, each with the sentence FR1 asks for, and the measurement for each is in that entry at the matching `L` number.

**R1157.** (was L1) `docs/USER_GUIDE.md:102` says the committed `results/R1/example/report.md` records `solve | 190.07`; it records `63.96`, and `a596fa7` is the commit that moved it while editing the guide -- CP3 inside one commit. No gate, CSV, input or design number is wrong by a wall clock the guide itself calls not-a-specification. *Closed when* `:102` cites the committed value or withdraws the figure.

**R1158.** (was L2) `docs/USER_GUIDE.md:951-957` publishes `-| solve | 190.07 |` / `-| total | 190.20 |` as the committed side; it is `63.96` / `64.08`. Same cause and same edit as R1157.

**R1159.** (was L3) `docs/USER_GUIDE.md:251` -- "10 of 32 rows" for a sentence about BOTH sensitivity columns; `Cm_sens` differs on 10, `K_sens` on 2, the pair on 12.

**R1160.** (was L4) `docs/USER_GUIDE.md:893` -- "the largest is `1e-10 N.m`"; it is `9.513095e-10`, printed correctly as `-9.5e-10` two sentences earlier.

**R1161.** (was L5) the guide defines lambda as the Froude scale in 4.1/4.7 and uses it as the wavelength in 7.3/8.3, with no note.

**R1162.** (was L6) the published C_m caveat's "RAISES" is non-strict: `max(amplified, simple)` flattens C_m below the overtake and 2 of 12 rows do not move. Never wrong in sign, so no number is wrong. Pre-existing (R743).

**R1163.** (was L7) `test_R1156_...`'s compression control is blind to any C_m defect in `[0.85, 0.9758)` at its chosen member; `amplified` overtakes `simple` at `cm = 0.9757685`, and the row steps C_m by 0.35. EH4's weakening direction, solved.

**R1164.** (was L8) `docs/directives/README.md`'s provenance roll does not mention GD; its text is recorded verbatim in `GC.md:109-144` by GD's own `Record:` line, so no rule is lost.

**R1165.** (was L9) `docs/USER_GUIDE.md` is a published deliverable (EZ0) that no guard reads -- `tests/test_tree_prose_consistent.py:99`'s `ROOTS` excludes `docs/` at large. **No new apparatus through F6**, so it goes on `docs/milestones/F2a.md`; R1157-R1160 are what the absence cost in the file's first week.

## Tolerances touched

**None, and EU1 does not attach.** Unchanged from the entry below, where the commands are: `git diff 66c7331..HEAD -- floatfea/tolerances.py | wc -l` is `0`, no declared counter moved, and I ran the adversarial configurations anyway -- the `Cm = 1.2` run and R1163's boundary solve, which is what found R1163.

## Next step opens when

**NOTHING IS OPENED AND NOTHING IS CLOSED.** Step 4 stays open at **0 of 3 reviewed revisions**.

1. **R1157 and R1158 first, together: one edit.** Then R1159 and R1160.
2. **R1157-R1165 must appear in revision 2's `Carried` section**, which is now something the guard will ask for rather than something you have to remember -- that is the whole content of this addendum.
3. **R1147, R1150, R1151, R1152, R1153 and R1154 are unchanged and still revision 2's.**
4. **EG3 (ii), paid from my side:** `45 failed, 517 passed` at `954e69d`, in the same five classes as the 42 at `a596fa7` -- 26 site cases, 9 finding cases, 3 that reach neither FS1 limb and are ruled on the measured cause, and the 7-state cascade. The count rose because my own verdict is now the newest; **it is a function of what I write, which is R861 again.** They clear when revision 2 answers them, not by time.
5. **R1149, R835/R861 remain MINE and go to Xabier.** So does one more, and it is about my own instructions: **`docs/SUPERVISOR.md` says `scripts/write_verdict.py` "commits to the branch" and it does not commit at all** -- the reviewer must commit, and the only tree where that reaches branch `F3` is the implementer's checkout, which FV2 tells the reviewer never to write in. I resolved it by using the one sanctioned door and nothing else, left the tree clean, and am recording the contradiction rather than letting the next reviewer discover it.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 4 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: a596fa76b969b6bbf680df9029b94aabd45112a4
**Reviewed commit: `a596fa76b969b6bbf680df9029b94aabd45112a4`.**
Verdict: PASS
Tests: **4477 passed, 42 failed, 0 skipped** of 4519 collected -- MY OWN RUN at the judged commit, in clean worktrees of my own (FV2), in EI0's two halves: the main half `3957 passed, 2 warnings in 2991.22s (0:49:51)`, **0 failed and 0 skipped**, and the three report-parametrised files `42 failed, 520 passed in 205.08s`. **Every red is inside those three files and nowhere else**; all 42 are EG3 state (2), and the trace is finding 3.
CI (FP1): run **42446638701** at `a596fa7`, `completed/failure`. **The verification ladder is SUCCESS, all six rungs.** `lint, unit and guards` failed only at `guards and meta-tests`, with `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all SUCCESS above it, so nothing hid behind an earlier red (CZ1 (iii)). That step reports **42 failed, 1435 passed** and its FAILED list is **id for id identical to mine** -- a machine I do not control, a different OS, reaching the same 42. **CA2's HOLD is not reached because every one of the 42 satisfies the FS1/FT1 predicate or the measured cause in finding 3**, not because my local run was green.
Scope: **ES0 INTERIM CHECK.** `git log --oneline 66c7331..HEAD -- docs/reports/R1/step-4.md` is empty, so there is no new report revision and this counts against **none** of step 4's three. **Step 4 stands at 0 of 3; nothing is closed** -- no `Closes:` line (FK1). Light scope held: suite, CI, and a CZ0 (a)-(d) / FR1 scan of the diff. **No corpus batch and no closure list**, per ES0 -- not because EG4(e)'s pause holds, which it does not: it expired 28 October, which is R1149, mine, still Xabier's.
Ruled under **FR1 with EZ0. NOTHING BLOCKS**, and for each ledger row I give the sentence FR1 asks for rather than a classification.

**WHERE I WORKED (FV2).** Three worktrees of my own outside the repository, detached at `a596fa7`. Every arm reverted with `git checkout --` inside my own worktree, `git status --porcelain` empty afterwards each time. The implementer's tree: `git status --porcelain` empty and HEAD `a596fa7`, checked before I wrote.

**STEP 1b DOES NOT BITE, AND MY INSTRUCTIONS DISAGREE WITH CLAUDE.md ON IT.** `docs/SUPERVISOR.md` 1b says HOLD if the report's `Answers:` header names an earlier verdict than the newest. It names 47 @ `779e79a`; the newest is 48 @ `6370e99`. **I ruled under CLAUDE.md -- ES0 and EG3 state (2) -- not under 1b**, because ES0 defines an interim check as a verdict on a tree with no new revision and EG3 state (2) names this exact state as designed and self-clearing. Read literally, 1b makes every interim check after a verdict an automatic HOLD and state (2) unreachable. For Xabier, once; not a round.

**THE MANDATED SEPARATE DIFFS, `66c7331..HEAD`, four commits.**

```
cmd  git diff 66c7331..HEAD -- floatfea/tolerances.py | wc -l        ->  0 (not in the diff)
cmd  git diff 66c7331..HEAD -- tests/conftest.py 'tests/**/conftest.py' | wc -l  ->  0
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'  ->  tests/conftest.py
     -- the pathspec RESOLVES; not an empty result, so no CH2/CI0 channel is opened
cmd  git diff --stat 66c7331..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md  ->  (empty)
     -- no STOP-class finding
cmd  git diff --stat 66c7331..HEAD -- tests/corpus docs/reviews
out  site_pattern_path_forms.txt 78+ / docs/reviews/R1/step-4.md 459+ -- both MINE
     (`829942d`, `6370e99`); the implementer wrote neither
cmd  git diff 66c7331..HEAD -- floatfea | grep -c "^[+-][^+-]"
out  10 -- ALL TEN inside cli.py's TABLE_CAVEATS C_m string
cmd  the shipped example configuration, PARSED on both sides
out  yaml.safe_load(66c7331:examples/platform12_placeholder.yaml) == yaml.safe_load(HEAD:..)
     True -- the 11/4 diff there is comment-only; no declared input moved
cmd  ruff / black --check / mypy, over floatfea tests scripts
out  All checks passed! / 162 files would be left unchanged. / Success: 45 source files
cmd  FV1's four root guards  ->  222 passed in 39.62s
     (221 at 66c7331; the +1 is the new regression file being collected, which is
      test_collected_set_golden doing its job rather than a count drifting)
```

## Carried

| item | status | measured by me |
|---|---|---|
| **R1148** (`carried_table.SITE` missing two pieces of `_SITE`) | **ANSWERED in `6ec0425`, and THE SECOND TOKEN IS IN SCOPE -- I ablated it rather than accept the account.** | One variable at a time, both patterns over all 18 verdict files: **HEAD 0 files disagreeing; lookbehind ONLY 6 files (33 tokens gained, 3 LOST); prefix ONLY 18 (3004 gained); neither 18 (3037 gained, 3 lost).** So `(?:R\d+-)*` is what makes the two copies agree on the DECISION, which is R1148's own first closing branch. The three tokens the lookbehind-only form LOSES are `frames.txt`, `g22_model_configurations.txt`, `tree_prose_claims.txt` -- the `check_sites` false-failure direction, measured rather than asserted. |
| **R1139** | answered at verdict 48; carries nothing | not reopened |
| **R1147, R1150, R1151, R1152, R1153, R1154** | **still open, correctly deferred to revision 2 under GC4** | R1147's seven sites are untouched and all still RESOLVE: `docs/directives/FZ.md:576` is byte-identical **and still at line 576** (the 130 FZ insertions begin at 687), so the closing condition did not go stale under this diff. R1151's site still ends `...stays out.#`. **R1152: the roll lists `GB.md` once and `GB.md` still has its own bullet below it -- the roll-plus-bullet shape R1152 described -- but the condition as written, "the roll lists it once", is met.** Closure item; not re-reviewed item by item (CZ0). |
| **R1149** (EG4(e)'s pause expired 28 October) | **MINE and still Xabier's** | it is 7 November. ES0 runs no batch at an interim check anyway, so the pause did not decide this round. |
| **R835 / R861** (EG3's enumeration; the baseline is a function of what the reviewer writes) | **still open, still Xabier's -- measured this round from a NEW direction, the COLLECTION side** | the three report files collect **3039 cases at `66c7331` and 562 at `a596fa7`**, down 2477, because `SITES` and the carried-row set are parametrised over the NEWEST VERDICT and verdict 48 is 459 lines where 47 was far longer. `test_every_named_site_is_touched_or_declared` goes **2261 -> 43**. Nothing vanished: the denominator is my own prose. **A whole-suite count compared across a verdict boundary is not a comparison** -- worth knowing before the next revision publishes one. |
| **verdict 47 item 10(a)** (`docs/closure/R1.md` must carry the `cz1-closure-outputs` block the moment it exists) | **STILL LIVE** | `ls docs/closure/` has no `R1.md` |
| **CZ1 (ii)/(iii)'s four outputs** | **owed at the closure commit, which still does not exist** | unchanged |

## Findings

**NOTHING BLOCKS.** No tolerance moved, no declared input moved, the lint gate and the four root guards are green, CI's whole ladder is green, and every red traces to EG3 state (2) by measurement. The three things you asked for first, then the ledger.

### 1. R1156's repair and its gate -- VERIFIED by my own arms; the repair is right

```
cmd   baseline, tests/regression/test_r1_published_artifacts.py   ->  47 passed
cell  `git checkout 66c7331 -- floatfea/cli.py` ALONE, artifacts untouched, restored after
out   4 failed, 43 passed -- test_R1156_... plus caveat8 on all three artifacts
cell  `git checkout 66c7331 -- results/R1/example` ALONE, source untouched, restored after
out   4 failed, 43 passed -- the same four
cell  `cm` injected into the 3.3.1 TENSION branch of check_member, one line, restored
out   1 failed -- test_R1156_..., firing on its OWN branch guard ("the tension case does
      not reach a 3.3.1 clause -- it governs on '3.2.3 bending'"), because cm * u_bending
      at cm = 0.85 drops u_combined to 0.6956 under u_bending 0.7931 and the governing
      clause flips. It reddens, and the assertion that fires is the one saying the control
      has stopped measuring its own branch. That is the right failure, not a lucky one.
rule  FZ rule 5 -- a named test row that fails on a revert of the repair ALONE. It does
      now; SR-43 records honestly that the first version did not.
```

**The repaired sentence is a property of the CODE, not of this example.** `api_wsd.py:588-590` forms `u_combined` with no `cm` in the `in_tension` branch; `:600` is `amplified = u_axial + cm * u_bending / (1.0 - f_a / f_e)` in the compression branch alone, and `"3.3.1 interaction"` is emitted only when `in_tension`. So "leaves every row whose `governing_clause` reads `3.3.1 interaction` untouched" holds universally, not merely over the shipped 32 rows.

**The ablation behind it reproduces exactly, on my own run at the configuration the commit describes and prints no command for** -- `Cm: 1.2`, everything else held:

```
out   governing U = 2.05621 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
      3.3.1 interaction   6 rows    6 same,  0 moved
      3.3.2 interaction  12 rows   10 ROSE,  0 fell,  2 same
      3.2.4 beam shear   14 rows   14 same
      -- the guide's section 4.6 table, figure for figure, measured rather than read
```

**FZ (c): I agree it is NOT an escalation, for a stronger reason than the one given.** The code-check basis did not move and no computed value moved -- **and `CM_JOINT_TRANSLATION`'s docstring already read "3.3.1 case (a)" for the VALUE and "3.3.2" for the TERM before this commit** (`api_wsd.py:110`, `:117-119`). The repair aligned a published caveat with an attribution the source of truth already carried, which is narrower than deciding one.

### 2. docs/USER_GUIDE.md -- I ran every command it prints. Four figures are wrong; none blocks

**Reproduced exactly in my own clean worktree:** `--help` verbatim; 6.1's eleven sections in that order and its admissibility table verbatim; 6.2's and 6.3's column lists against the real headers, with `source` and `heading_deg` empty on all 48 `static` rows; 6.6 (`168 rows`, box/False 84, triangle/True 84); 8.1 (`platform:hub2_arm ROOT 12.5 1.71167 3.3.2 interaction`, deliberate `max()` tie-break and all); 8.2 (`32 rows`, `[('12.5',26),('15',4),('16.2',2)]`, `over unity: 4`); 8.4 (`1248 rows`, all six basis counts); 8.5 (all four arms byte-identical); **8.7 -- I ran `floatfea run` and the filtered diff printed NOTHING, both CSVs byte-identical**; 9 (`470 passed`); the whole section 8 console block including `707/884/990/1061/1146/1415` steps, `1248`, `32` and the governing line; **all six refusal messages in 7.1, 7.6, 7.7, 7.8, 7.9 and 7.12 verbatim, with exit 2 and 7.12's exit 1 exactly as stated**; every bound and default in 4.1/4.3/4.4/4.6/4.7 against `config.py:187-201` and `CodeCheck`; 7.3's band arithmetic; 4.3's `z_r(f)` against `platform.py:839`; 4.7's `100/50 = 2 m`; 6.2's `4%` against caveat 2's own `4.0%`; and **every citation resolves** -- 20 of 20 internal section references against 43 headings, 11 of 12 cited paths present, the twelfth the absent root `README.md` that SR-44 already routes to R2.

That is a good document, and the commands say so better than an adjective would. The four wrong figures are L1-L4.

### 3. The 42 reds, each id against the FS1/FT1 predicate -- and a CONTROL for the three you flagged

```
out   42 failed, 520 passed (562 collected), and CI's guards step gives the same 42:
       9  test_the_report_carries_the_finding[R518, R1147..R1154]      NAME a finding
      23  test_every_named_site_is_touched_or_declared[...]            NAME a site
       3  test_the_Carried_table_is_what_the_generator_produces
          test_the_generator_would_catch_a_row_under_the_wrong_number
          test_the_CI_section_is_about_the_REVIEWED_commit
       7  test_the_guard_survives_the_state[7 states] -- INNER list read from its own
          output rather than inferred from the name (EG3 (i)): `baseline` gives
          `34 failed, 475 passed`, every id of the 35 above and no other id anywhere
```

**Your reading of the three is wrong, and the right ground is a measurement.** Routing them through "the site `docs/reports/R1/step-4.md`, which R1154 names" would waive any red that merely TOUCHES a file named anywhere in a verdict -- a hole wide enough to drive CZ1 (iv) through, worth refusing even where the outcome is the same. Instead:

```
cell  the SAME three ids at `66c7331`, where the newest report ANSWERS the newest verdict.
      ONE variable moved between the trees: verdict 48 landed. The report did not change.
out   66c7331  8 failed, 3031 passed -- none of the three is in the list
      a596fa7  all three RED
judge verdict-dependent BY MEASUREMENT, not by family.
      `..._Carried_table_is_what_the_generator_produces` names R518, R849 and 32 more of
      verdict 48's own rows IN ITS FAILURE LINE, so it reaches FS1 limb one outright.
      `..._would_catch_a_row_under_the_wrong_number` and
      `..._CI_section_is_about_the_REVIEWED_commit` reach NEITHER limb as worded -- one
      reports an empty candidate list, the other two shas -- and I rule them boundary reds
      on the measured cause, because a predicate that excluded them would make EG3 state
      (2) UNREACHABLE and every verdict in this repository would redden the tree it lands
      in. **R835/R861's fourth measured shortfall. Relayed, not re-litigated.**
```

## Ledger (FR1: none can cause a silently wrong result; one line each)

**L1.** `docs/USER_GUIDE.md:102` says the committed `results/R1/example/report.md` records `solve | 190.07`. It records **63.96** -- and **`a596fa7` is the commit that moved it**, having edited the guide and regenerated the report in the same commit without re-taking the figure: **CP3 inside one commit, where an edit after the paste voids the paste.** Not blocking: a wall clock the guide itself calls not-a-specification, so no gate, CSV, input or design number is wrong by it. *Closed when* `:102` cites the committed value or withdraws the figure.

**L2.** `docs/USER_GUIDE.md:951-957` -- 8.7's reference diff shows `-| solve | 190.07 |` and `-| total | 190.20 |` as the COMMITTED side; it is `63.96` and `64.08`, and my own regeneration gave `-| solve | 63.96 |` / `+| solve | 86.68 |`. Same cause and same edit as L1.

**L3.** `docs/USER_GUIDE.md:251` says "those columns differ from `utilisation` on 10 of 32 rows" of a sentence about BOTH sensitivity columns. Measured: `utilisation_Cm_sens` differs on **10**, `utilisation_K_sens` on **2**, the pair on **12**. The argument survives either figure; the number was swept on one of the two axes it is attributed to.

**L4.** `docs/USER_GUIDE.md:893` says "the largest is `1e-10 N.m`". The largest is **9.513095e-10**, which the same paragraph prints correctly as `-9.5e-10` two sentences earlier. One order of magnitude, self-contradicting on the page.

**L5.** The guide defines lambda as the FROUDE SCALE in 4.1/4.7 and uses it as the WAVELENGTH in 7.3/8.3 (`H/lambda <= 1/7`, `H/lambda = 0.1550`) with no note; a reader taking 4.1's definition computes `24.2/50 = 0.484` against a stated limit of `0.1429`. Inherited from the artifact's own column name, which is why it is a ledger row and not a defect in the guide alone.

**L6.** The published C_m caveat says a larger C_m "RAISES the compression utilisation", unconditionally. It is **non-decreasing, not increasing**: `u_combined = max(amplified, simple)` flattens C_m below the overtake, and 2 of the 12 `3.3.2 interaction` rows in the shipped example do not move. The guide's 4.6 says so; the caveat does not. The direction is never wrong in SIGN, so no number is wrong. Pre-existing (R743), not created here.

**L7.** **I solved the new gate's boundary in the WEAKENING direction (EH4), which the commit did not.** `test_R1156_...`'s compression control is **blind to any C_m defect in `[0.85, 0.9758)`** at its chosen member: that member sits on the `simple` form at `cm = 0.85` and `amplified` only overtakes at **`cm = 0.9757685`** (bisected, 80 iterations). The row passes because it steps C_m by `0.35`, which is `2.8x` the detection boundary. The tension half is sharp -- exact equality, and my injection arm reddened it. Not blocking: the row's job is the clause attribution, it reddens on a revert and on a branch swap, and C_m's magnitude is held elsewhere. On the record so nobody re-derives it.

**L8.** `docs/directives/README.md`'s provenance roll does not mention **GD**. Its text IS recorded verbatim inside `GC.md:109-144` by GD's own `Record:` line, which `GC.md` states -- so C25 does not reproduce and no rule is lost. The index is the only place it is absent.

**L9.** `docs/USER_GUIDE.md` is a published deliverable (EZ0) that **no guard reads**: `tests/test_tree_prose_consistent.py:99`'s ROOTS is `("floatfea", "tests", "scripts", "docs/milestones", "docs/verification")`. 996 lines of figures whose only bound is a reader -- CJ0 applied to a deliverable. **No new apparatus through F6**, so it goes on `docs/milestones/F2a.md`; L1-L4 are what the absence cost in the file's first week.

## Tolerances touched

**None, and EU1 does not attach.**

```
cmd   git diff 66c7331..HEAD -- floatfea/tolerances.py | wc -l   ->  0
cmd   git diff 66c7331..HEAD -- floatfea tests scripts | grep "^+" |
        grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance"  ->  (no match)
rule  CLAUDE.md section Tolerances, including anything functioning as a tolerance under
      another name -- a convergence threshold, a comparison epsilon, a tier cutoff
judge no tolerance VALUE and no DECLARED COUNTER moved, so EU1's adversarial-case
      requirement is not triggered. **I ran the adversarial configurations anyway**,
      because R694's lesson is that a value which does not move is the worst case and not
      the safest: the Cm = 1.2 run in finding 1 and L7's boundary solve are both
      configurations the diff did not choose, and L7 is what the second one found. The two
      exact-equality assertions the new file adds both carry `# not-a-tolerance:`, and
      tests/test_no_tolerance_literals.py is green on them (222 passed).
```

## Next step opens when

**NOTHING IS OPENED AND NOTHING IS CLOSED BY THIS VERDICT.** It is an ES0 interim check: step 4 stays open at **0 of 3 reviewed revisions**, and the findings above join the step's list to be answered in revision 2 under GC4.

1. **L1 and L2 first, together: one edit, and the only findings here a user trips over in one command.** `a596fa7` created them by regenerating `report.md` in the same commit that wrote the sentence citing it. L3 and L4 go with them.
2. **R1147, R1150, R1151, R1152, R1153, R1154 are unchanged and remain revision 2's**, with R1147's seven sites verified still valid and still correctly numbered at this commit.
3. **R1148 is answered and its second token IS in scope.** Ablated at 6 files of 18; nothing further owed.
4. **L9 is the structural one.** A 996-line published deliverable no guard reads, in a milestone that forbids building one. `docs/milestones/F2a.md` is where it goes; the reviewer's reading is the bound until then, which is why I ran all six of section 7's refusals and every command in section 8 rather than reading them.
5. **R1149 and R835/R861 are MINE and go to Xabier, not into a round.** The corpus pause's own date passed ten days ago; EG3's fourth measured predicate shortfall is finding 3, and the collection-count figure in `Carried` is the tenth measurement of R861's point.
6. **A CORRECTION TO MY PREDECESSOR, because it would otherwise cost the next reviewer an hour.** Verdict 48 killed its combined run after "824 s of CPU and then frozen ... zero CPU movement over 20 s" and attributed it to a `.git` on OneDrive. **This `.git` is on local disk, the same thing happened to me, and it was not a freeze.** My main half sat at **exactly 854.75 s of CPU across three samples 6 s apart, at 9% complete** -- and once my other worktrees went idle it **resumed and finished: 1839 s and climbing, then `3957 passed in 2991.22s`**. It was BLOCKED on contention between my own concurrent worktrees over one shared object store, not dead. **Do not kill it; serialise it.** I could not kill it even when I tried, which is the only reason this measurement exists.
7. **The schedule.** FW0's date is 10 November and it is 7 November: **three days**, against step 4 estimated at one and a half to two days plus half a day of closures (`docs/milestones/R1.md:52`), with GD2 putting revision 2 at end of 9 November. The guide exists and is good; FT2.7 does not. **I do not escalate under FZ (e) -- I am not forecasting a slip past 10 November -- but the margin is now under a day, and the next revision is the last one that can report a slip the day it is known rather than after.**
8. **What this diff got right, and it is much the larger part.** The one real defect was found by the FL3 witness, traced from a guide sentence back through three published artifacts to the source string, and fixed AT THE SOURCE rather than in the artifacts. The gate was then written, measured against a revert, found NOT to fail, and rebuilt to read `TABLE_CAVEATS` -- and that failure was recorded as SR-43 rather than quietly repaired, which is the most useful paragraph in the diff. The repair KEPT the true half of the sentence it corrected, the value's own clause, instead of swapping one error for another. The stale `truss_sizing` comment in the shipped example was found and fixed with both end-to-end tests named, and both exist at the paths given. R1148 went beyond its stated condition for a reason that measures out. SR-44 reported a missing root `README.md` as a real new-user condition found by an accident, rather than writing into the guide something that could not document its own absence. And each of the three commits carries a `LOCAL SELECTION (FV1)` block, so the complement is a measurement rather than an omission.

*Length: this runs past GA3's 150-line target by a little. The overrun is finding 2's measurement list and finding 3's control, and I would rather hand you the commands than the adjective.*


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

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
