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
