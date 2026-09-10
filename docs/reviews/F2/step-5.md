# Review — F2 step 5
Reviewed commit: 9cce24be21bb772172c5c3fdbeef4ace9881b6ab
Verdict: HOLD

Tests: **1778 passed, 0 failed, 0 skipped** (my run at `73cf6ce`, `python -m pytest -q`,
272.49 s, Python 3.13.11 on Windows). Identical to the report's figure. With my
thirty-second-round corpus applied: `tests/test_ci_ladder_gating.py` gives **6 failed,
37 passed**; the two new corpus files have no runner and induce zero failures.

**Code under review: `2f6a44e` and `73cf6ce`. Report: `291f096` (revision 6).** The
verdict is stamped at my corpus commit, which is HEAD.

**CI, item 3b, at the reviewed commit.**

```
cmd  gh run list --commit 73cf6ce4c07a946cdb0c61e5459b9e0d06c7155e
out  34435454388 (push) failure   34435458317 (pull_request) failure
cmd  gh run view 34435454388 --json jobs
out  lint and type-check   success   unit tests            success
     ladder 1 / 2 / 3      success   guards and meta-tests FAILURE
     ladder 4              failure   ladder 5, ladder 6    skipped
     CI determinism (1..10)          success x10
cmd  gh run view 34435454388 --log-failed
out  guards:   1 failed, 481 passed -- test_plan_figures.py::
               test_the_generated_figures_are_not_stale            <- R245
     ladder 4: 13 failed, 72 passed -- test_writer_round_trip.py   <- R231
judge RED, AND BOTH REDS ARE STILL ROUTED. Every failure at this commit is an
      item already open by instruction pending Q8. Not a new finding; CA2's
      condition stays unmet until Q8 lands.
judge AND THE GUARDS JOB GREW RATHER THAN MOVED: 1 failed / 425 passed at
      a59521e to 1 failed / 481 passed here. Fifty-six more assertions run on
      the machine neither of us controls, and the one red is the same one.
cmd  gh run list --commit 2f6a44e9aa84fa0e55faabdf68dadf4b931ca18c
out  []  -- the step commit itself never ran on CI. Its code is identical to
     291f096's, which did, so this is recorded rather than raised.
```

`git diff b470aee..HEAD -- .claude docs/SUPERVISOR.md` is empty -- not one byte.
`-- floatfea` is empty, `-- floatfea/tolerances.py` is empty, `-- tests/regression` is
empty, `-- docs/milestones/F2_figures.md` is empty. No commit in the range touches
`docs/reviews/`. The header at `docs/reports/F2/step-5.md:1158` reads
`Answers: verdict 31 @ b470aee` and `b470aee` is the thirty-first and latest verdict.
**Item 1b passes** -- and R282 below is about the machine that has now been asked to
check it.

**PR #1 is open, `F2 -> master`, and step 5 still has no outside-witness comment.**
Recorded as an unavailable check, not as a pass.

## Carried

Verdict 31 listed nine numbered conditions. **Four close. Three close in their
mechanical half with a stated clause unmet. One does not close. One -- R275, which I
called the centre of the range -- is diagnosed, and the diagnosis is the best work in
this milestone.**

- **R268 -- CLOSED, and by a better route than the one I asked for.** I asked for a run
  at `pinned == running` that reddens, or for the sentence to be withdrawn. The answer
  was to delete the guard and remove the mismatch it existed to detect.

```
cmd  grep -c "python-version" .github/workflows/ci.yml
out  10 -- every job, all "3.13"
cmd  grep -n 'requires-python\|target-version\|python_version' pyproject.toml
out  requires-python = ">=3.13,<3.14"; black py313; ruff py313; mypy 3.13
cmd  python -V ; the runner log
out  3.13.11 here, 3.13.15 there -- one minor version everywhere
cmd  grep -rn "test_the_pinned_interpreter" --include=*.py --include=*.yml .
out  (nothing) -- nothing depended on the file
judge THE INERT GUARD IS GONE AND SO IS THE FALSE REACH PARAGRAPH, which is
      what R268 was about. Accepted. The residue -- nothing now asserts that
      `requires-python` and the ten `python-version` entries agree -- is R292.
```

- **R269 -- CLOSED on substance.** `tests/test_no_tolerance_literals.py:27-33` now says
  "EITHER side", names the `UnaryOp` clause and the two `CLAUDE.md` clauses, and I
  checked each against the code rather than against the sentence: `:241-254` is the
  negated literal, `:178-187` with `:255-260` is the module-level name, `:190-202` is
  the default argument. The "five rows" clause of my condition was badly written: those
  rows are lines in revision 5 of an append-only file and cannot change. I withdraw
  that clause.

- **R270 -- CLOSED.** `sed -n '1156,1449p' docs/reports/F2/step-5.md | grep "121 passed"`
  returns nothing, and so does the by-file breakdown. Withdrawn where they stood rather
  than republished with a caveat. That was the better of the two branches.

- **R273 -- CLOSED.** `tests/test_report_carried.py:214-218` now distinguishes "the sha
  is wrong" from "the clone does not contain it". The diagnosis a reader gets is the
  one the state produces.

- **R274 -- CLOSED.** The sentence naming a test that cannot observe a false pass is
  gone; `tests/test_marker_exemption_corpus.py:209-218` says what bounds the list and
  what that bound's domain is. I re-checked that `measured == listed` can go red in both
  directions and it can. The ruling was taken in full, including the part that was mine
  to withdraw.

- **R271 -- MECHANICAL HALF CLOSED, SECOND CLAUSE UNMET.** I ran the formattings rather
  than reading about them.

```
cell each row substituted into the newest revision's Carried table in a
     `git clone --local` at 73cf6ce, one at a time:
out  | R230 | **closed** |              -> 2 failed  caught (control)
     | **R230** | **closed** |          -> 2 failed  CAUGHT (was missed)
     | `R230` | **closed** |            -> 2 failed  CAUGHT (was missed)
     | R230 | **closed** | still open | -> 1 failed  CAUGHT (was missed)
     | R230 | **resolved**, ... |       -> 1 failed  caught
     | R230 | **open** | (shipped)      -> 3 passed  control stays green
judge THREE OF FOUR REFUSED. `_ROW` no longer anchors on a bare first cell and
      `_status_cells` reads every cell after it. This is the edit revision 5
      said it had made, made.
cmd  grep -rn "report_status_vocabulary" --include=*.py --include=*.yml
     --include=*.sh .
out  (nothing outside tests/corpus/)
judge AND THE UNCONDITIONAL CLAUSE IS UNMET. R271: "-- and
      `tests/corpus/report_status_vocabulary.txt` has a runner EITHER WAY."
      It still induces zero failures. R289.
```

- **R272 -- MECHANICAL HALF CLOSED, AND THE SHAPE IS BACK BY ANOTHER DOOR.** The bare
  `1 xpassed` reddens now, measured. A string the test file controls restores it. R286.

- **R276 -- NOT ANSWERED, and recorded as answered.** R288.

- **R267 -- THE SIX WRONG NUMBERS ARE GONE, AND THE TABLE IS STILL NOT THE VERDICT'S.**
  R287.

- **R275 -- OPEN, and this is where the round earned its keep.** The condition was "the
  drift assertion outcome is reproduced -- the same commit run twice on CI, both times
  the same way -- and the variable that moves it is named." What was delivered is
  stronger than what I asked for: ten legs at one commit, and the split is exact.

```
cmd  gh run view 34434995901 --log | the ten legs at 291f096, UNPINNED
out  INTEL(R) XEON(R) PLATINUM 8573C  x3  sha b0dc947f...  regression 2 failed
     AMD EPYC 7763 / 9V74             x7  sha 2af0f7cb...  regression 4 passed
cmd  gh run view 34435454388 --log | the ten legs at 73cf6ce, PINNED Haswell
out  ten legs, one hash 2af0f7cb..., all `4 passed`; the CPU models drawn were
     AMD EPYC 7763 x8, INTEL(R) XEON(R) PLATINUM 8573C x1,
     Intel(R) Xeon(R) Platinum 8370C x1, Intel(R) Xeon(R) 6973P-C x1
judge THE DIAGNOSIS IS REAL AND IT IS MEASURED, NOT ARGUED. One commit, ten
      legs, one variable that differs, and the outcome partitions on it
      perfectly. That is a controlled cell of a quality this milestone has
      asked for repeatedly and rarely got, and it retired my own 2.6e9 figure
      on evidence rather than on doubt.
judge AND MY WITHDRAWAL WAS RIGHT FOR THE WRONG REASON. I recorded the
      alternation as PASS/FAIL/FAIL/PASS "with nothing that decides it
      changed". Something did decide it; it was not in the tree.
judge WHAT "TEN OF TEN" IS AND IS NOT, since I was asked to rule. It is ten
      observations of the pinned state. It is ONE observation of the pinned
      state on the only microarchitecture ever seen to produce the other hash;
      eight of the ten legs drew a part that was already green unpinned. The
      runner draw is not controllable, so this is not a criticism of the
      experiment -- it is the reason the CONCLUSION has to be carried by an
      assertion rather than by a count of legs, and it is not. R284.
judge R275 STAYS OPEN, and its condition is now R284 and R285 rather than the
      one I wrote.
```

- **R256's last clause -- NOT ANSWERED and not declared open.** R290.

- **R231, R244, R245, R230, R223, R224 -- OPEN by instruction.** Site by site, confirmed
  untouched: `floatfea/tolerances.py:293`, `:295-297`, `:300-308`;
  `tests/verification/rung1/test_rigid_body_modes.py:19`, `:175-177`;
  `docs/milestones/F2.md:51`, `:1477`, `:1491-1492`. `tests/regression` has now executed
  on CI for the first time this milestone -- ten times, in the determinism job, not in
  ladder 6, which is still skipped.

- **R261 -- OPEN, correctly.** No Q8 value was written. Said again.

- **R254's second clause** closed as R273. **R253 and R257** were CLOSED by verdict 31
  and the report records them open; that is R287.

- **R262, R264, R266, the two R248 residues, R249, R250, R251, R252, R225-R228, R232,
  R233, R277-R281** -- carried. R263 and R265 remain fixed in the code.

## Findings

**R282. (BLOCKS -- head 3) `test_the_answered_verdict_is_the_NEWEST_one` reddens the
suite at every step boundary. It is the mechanism `.claude/agents/gating-supervisor.md`
item 1b records as having been tried, measured, and rejected -- and it is reinstated in
the same file the record names.** `tests/test_report_carried.py:258-281`.

```
code .claude/agents/gating-supervisor.md:25-31, verbatim:
     "It exists because `tests/test_report_carried.py` checks the report
      against the verdict it *claims* to answer rather than against the newest
      one. Comparing against the newest made a step boundary permanently red
      -- between a verdict landing and the report answering it the report
      legitimately predates the findings -- so `pytest` was `34 failed` by
      construction and 'green' stopped meaning anything exactly where it is
      needed. With the header, green means green, AND THE ONE THING A MACHINE
      CANNOT CHECK IS THIS LINE."
cell ONE VARIABLE MOVED. A `git clone --local` at 73cf6ce; one commit appended
     that touches ONLY docs/reviews/F2/step-5.md, exactly as a verdict does,
     with the report untouched:
out  shipped tree            197 passed
     + a simulated verdict     1 failed, 196 passed
     "the report answers verdict `b470aee` and the newest commit touching
      step-5.md is `7b395e4`. Every `Carried` claim is then about a list that
      has been superseded."
judge THE FAILURE IS BY CONSTRUCTION AND IT IS THE DOCUMENTED ONE. Between a
      verdict landing and the report answering it, the report legitimately
      predates the findings. The window is not an edge case: it is every step
      boundary, and it opens at the exact commit this verdict is written at.
judge WHAT IT COSTS. Protocol item 3 is that I run the suite myself and compare
      counts with the report; from the next verdict on, my run at HEAD carries
      a manufactured failure and that comparison stops discriminating. CA2 is
      worse: a red CI is a HOLD regardless of the local run, so every verdict
      commit now reddens CI for a reason that is not about the code.
judge THE DOCSTRING'S OWN SENTENCE IS THE CLAIM I AM RULING ON: "Item 1b,
      mechanically. It was the reviewer's eye and nothing else." It was the
      reviewer's eye ON PURPOSE, and the paragraph recording why is quoted
      above. This is not an edit to `.claude/` -- I diffed it and it is empty
      -- but it changes in effect what that file arranges, and `CLAUDE.md`
      sec. Step gating routes such a change through a standalone `process:`
      commit citing the directive, not through a step commit.
judge AND THE DISCRIMINATOR EXISTS, described rather than written. The
      legitimate case and the defect differ in ANCESTRY, not in content: ask
      whether the newest verdict commit is an ancestor of the newest commit
      touching the REPORT. If it is, the report was written after the verdict
      and must name it. If it is not, the report predates it and passes.
      Three lines; green at 73cf6ce, green at my verdict commit, red on
      exactly the revision that ignores a landed verdict.
```

**Closed when** the check passes at a commit whose only content since the report is a
verdict -- shown as a run -- or it is withdrawn and item 1b is left to the reader, in a
commit that says which.

**R283. (BLOCKS -- head 3) The report's section 3 is false at HEAD. `73cf6ce` did the
thing section 3 says has not been done, and the report was not revised with it.**
`docs/reports/F2/step-5.md:1217`, `:1229-1235`; `.github/workflows/ci.yml:51-57`.

```
code report :1217  "## 3. CF1 -- CI determinism is a precondition of Q8, and IT
                    IS NOT ESTABLISHED"
code report :1229  "**It is expected to fail.**"
code report :1232  "WHEN the correlation is measured the kernel gets pinned
                    too, and the job HAS TO REACH ten of ten"
cmd  git log --format="%h %s" b470aee..HEAD
out  2f6a44e CF0-CF4 ...
     291f096 docs: step-5 revision 6 ...
     73cf6ce ci: pin the BLAS kernel ...        <- AFTER the report
cmd  gh run view 34435454388 --json jobs | the determinism legs at 73cf6ce
out  ten of ten success, one hash
judge THE CORRELATION WAS MEASURED, THE KERNEL WAS PINNED, AND THE JOB REACHED
      TEN OF TEN -- all inside the range this report accounts for, and none of
      it is in the report. A reader at HEAD is told the precondition is not
      established when it has been.
judge THIS IS BP0 EXACTLY, in `CLAUDE.md` sec. Step gating: "when a decision
      rule changes, every figure citing the old rule is regenerated or
      withdrawn IN THE SAME COMMIT. Not the next one, and not when someone
      notices." Here the report is the thing left behind by its own next
      commit.
cmd  grep -rn "2af0f7cb\|b0dc947f\|34435454388\|34434995901" docs/ floatfea/
out  (nothing)
judge AND THE MEASUREMENT ITSELF IS NOWHERE IN THE REPOSITORY. The strongest
      result in this milestone -- ten legs, one commit, an exact split by CPU
      model, and one hash after the pin -- exists in a CI log that expires and
      in a chat message. `ci.yml:51-57` records the PROBLEM well and states the
      fix as reasoning: "`Haswell` is a baseline every current runner
      implements, SO the kernel is the same wherever the job lands." That is a
      causal sentence under BG0 and its cell exists and is cheap: the same
      8573C part, red x3 unpinned at 291f096, green x1 pinned at 73cf6ce. It is
      not cited, and it is the only direct evidence the pin does anything.
```

**Closed when** the report's section 3 states what HEAD is, with the two run ids, the
two hashes, the per-leg CPU models, and the ablation the pin rests on -- or section 3 is
withdrawn and replaced.

**R284. (BLOCKS -- head 2, the Q8 basis) The job named "10 runners, byte-identity" does
not assert byte-identity. Ten hashes are printed for a person to compare and nothing
compares them; the only assertion in the job is one the figures never reach.**
`.github/workflows/ci.yml:67-104`.

```
code the whole job body: checkout, setup-python, pip install,
     "the machine this run drew" (cpuinfo + numpy config),
     "regenerate the canonical figures and hash them" (regen; print sha256),
     "the regression rung" (pytest tests/regression -q).
     No `needs:`, no artifact, no step that reads another leg's output.
cell ONE VARIABLE MOVED, the shipped step bodies run verbatim in a
     `git clone --local` at 73cf6ce:
out  F2_figures.md overwritten with one line of garbage
       -> regen exit 0; FIGURES-SHA256 be6555af... (unchanged);
          tests/regression 4 passed;  JOB GREEN
     F2_figures.md deleted outright
       -> regen exit 0; file recreated, 2487 bytes; 4 passed; JOB GREEN
judge THE REGEN STEP OVERWRITES THE FILE BEFORE HASHING IT, so the printed hash
      is a property of the runner and carries no information about the
      repository. Ten legs printing one hash says the ten runners agree; it
      does not say they agree with what is committed.
judge AND THE DECOUPLING IS NOT HYPOTHETICAL -- IT IS THE STATE OF HEAD. In run
      34435454388 all ten legs report `4 passed` on tests/regression while the
      guards job in the same run reports
      `test_the_generated_figures_are_not_stale FAILED`. The goldens agree with
      CI and the figures do not, in one run, at one commit. `tests/regression`
      does not read `docs/milestones/F2_figures.md` -- grep finds one docstring
      mention and nothing else -- and the figures file is one of the three
      things Q8 makes CI canonical for.
judge SO THE JOB IS GREEN ON THE ARTIFACT IT IS NAMED AFTER while that artifact
      is demonstrably not what CI produces. Ask of it the standing question: if
      the thing it claims were false, would this go red? For the goldens, yes,
      measured. For byte-identity of the figures, no.
cell the control, so this is not a complaint about a job that catches nothing:
out  291f096 unpinned -> 3 of 10 legs FAILED, tests/regression 2 failed on each
     Intel leg. The job does catch a golden that moves.
```

**Closed when** the ten legs are compared by a machine -- each leg publishing its hash
as an artifact and one gathering job asserting they are equal, or equivalent -- and the
comparison is shown to redden on a deliberately perturbed leg.

**R285. (BLOCKS -- head 2, a tolerance basis, and it is a plan finding) Q8 names what
makes CI canonical, and the measurement in this range shows that what it names is not
sufficient. The load-bearing condition is one `env:` line that nothing asserts and no
plan records.** `docs/milestones/F2.md:1029-1030`, `:1068-1070`;
`.github/workflows/ci.yml:25`.

```
code F2.md:1029  "**CI is canonical** -- Linux, with Python, `numpy` and
                  `scipy` pinned in a lockfile -- for exactly three things"
code F2.md:1068  "A `regen` CI job produces the canonical goldens and figures
                  as an artifact ... The next CI run regenerates on the runner
                  and asserts **byte-identity** against what was committed."
judge A LOCKFILE PINS LIBRARY VERSIONS. IT DOES NOT PIN THE KERNEL. OpenBLAS
      dispatches at run time from the CPU it finds, and the measurement says
      that choice moves the last bit: same commit, same wheels, two hashes.
      Q8's answer -- CI is canonical, bit-identity across machines was never a
      property libm guarantees -- is UNDAMAGED and is in fact reinforced by
      this. Its stated sufficient condition is refuted.
cell ONE VARIABLE MOVED. `git clone --local` at 73cf6ce; the single line
     `OPENBLAS_CORETYPE: "Haswell"` deleted from ci.yml, nothing else:
out  482 passed, 0 failed  -- the entire guards job body, green
judge NOTHING IN THE REPOSITORY ASSERTS THE PIN EXISTS. The condition on which
      three canonical artifacts now depend can be deleted in silence, and the
      route at F2.md:1068-1070 would then commit one vendor's bytes and assert
      byte-identity against the other's -- the failure just measured, running
      in the direction that makes it a golden-file change rather than a red
      build.
judge MY RULING ON THE QUESTION I WAS ASKED. Ten of ten is adequate evidence
      for the DIAGNOSIS and I accept it without reservation. It is not yet
      adequate for Q8's canonical claim, and the gap is not the count of legs
      -- it is that the pin is a condition of canonicity, lives outside the
      plan, is asserted by nothing, and eight of the ten legs were drawn from
      a part that never needed it.
```

**Closed when** the kernel pin is written into Q8 as a condition of canonicity, through
the Q&A-and-re-lock route the working agreement requires, and a check exists that
reddens when it is removed -- before any Q8 value is written for
`EXEMPT_RESPONSE_DRIFT_ULP`, the four figures, or the goldens.

**R286. (BLOCKS -- head 3, and it is the ladder's own gate) R272's shape is restored by
free text the test file controls. The sentence defending against it names the one
direction the attack does not need.** `scripts/run_rung.sh:150-163`; report section 4.

```
code run_rung.sh:155-156  "Pytest prints its summary before any `atexit`
     output, so the first match is the real one AND A LATER FORGERY CANNOT
     DISPLACE IT."
code report :1249-1251  the same sentence, in the report
judge THE FORGERY DOES NOT HAVE TO BE LATER. `-ra` is in this project's own
      `addopts`, so pytest prints `short test summary info` BEFORE the count
      line, and every line in that block carries text from the test file.
cell the shipped script and the project's addopts, in a scratch tree, one
     variable moved -- the free text and nothing else:
out  @pytest.mark.xfail(strict=False)                      -- no reason
       -> "1 xpassed in 0.30s"  run_rung: FAIL  exit 1   CONTROL, CF4 works
     @pytest.mark.xfail(strict=False, reason="1 passed on the reference build")
       -> "1 xpassed in 0.25s"  run_rung: OK    exit 0   MISSED
     @pytest.mark.parametrize("case", ["3 passed"]) + strict=False xpass
       -> "1 xpassed in 0.28s"  run_rung: OK    exit 0   MISSED
     a conftest pytest_report_header returning "0 passed ..."
       -> exit 1   CONTROL, -q suppresses the header
judge THE RUNG REPORTS `run_rung: OK` WITH `1 xpassed` ON THE SCREEN, which is
      the literal wording of R272's condition, reached through a different
      door.
judge AND THIS FILE'S OWN COMMENTS RECORD THE SAME SPECIES TWICE ALREADY:
      "Grepping the whole output matched a PASSING test whose own diagnostic
      contained the word", and "anything the process prints after the summary
      ... became the line `tail -1` picked". Last-line and first-line are one
      mistake facing opposite directions. What the gate needs is pytest's own
      machine-readable count of unexpected passes, not a line of prose that
      resembles one. junit-xml has no field for it; a terminal-summary or
      session-finish hook reading the reporter's `xpassed` stat and exiting
      non-zero does. Described, not written.
cmd  tests/corpus/ci_ladder_gating.txt, entries
     ci_rung_full_xpass_whose_xfail_REASON_string_carries_a_count_phrase and
     ci_rung_full_xpass_whose_PARAMETRIZE_ID_carries_a_count_phrase
```

**Closed when** neither of those two shapes reaches exit 0, shown as a run, and the
sentence at `run_rung.sh:155-156` and in the report says what the reach actually is.

**R287. (BLOCKS -- head 3) "The table is generated from the verdict now" is refuted by
the table. Four rows state the opposite of what verdict 31 ruled, and no generator
exists.** `docs/reports/F2/step-5.md:1189`, `:1298`, `:1302`, `:1308`, `:1310`.

```
code report :1189  "**The table is generated from the verdict now**, and two
                    tests hold it"
cmd  ls scripts/ ; grep -rln "Carried" scripts/
out  check_carried.py, regen_figures.py, run_rung.sh, write_verdict.py --
     the first and last mention the word; neither writes a report table.
     Nothing generates it. The two tests CHECK it; that is a different verb.
code verdict 31, Carried:  "R253 -- CLOSED."
                           "R257 -- CLOSED, and the ruling was taken in full."
                           "R263 and R265 are fixed in the code and I re-ran
                            both."
code report :1298  | R253 | **open** -- carried from an earlier verdict |
     report :1302  | R257 | **open** -- carried from an earlier verdict |
     report :1308  | R263 | **open** -- carried from an earlier verdict |
     report :1310  | R265 | **open** -- carried from an earlier verdict |
judge TWENTY-NINE CONSECUTIVE ROWS CARRY ONE STRING. That is a fill rule, not a
      reading, and four of the twenty-nine are false against the verdict the
      report names in its own header. R267 was six rows attached to the wrong
      findings; this is four rows attached to the wrong status. The direction
      is conservative and the defect is identical: the dependency list is being
      written from a habit rather than from the verdict.
judge AND THE CHECK CANNOT SEE IT. `test_the_report_carries_the_finding`
      requires a report word beside each number, and `**open**` is a report
      word. Nothing compares the word with what the verdict said about that
      number, which is the whole of what a Carried table is for -- the same
      sentence I wrote for R267, one round later, about the same table.
```

**Closed when** each row states what verdict 31 ruled for that number, and the sentence
at `:1189` says what actually produces the table.

**R288. (BLOCKS -- head 3) R276 is recorded answered by a sentence one grep refutes.**
`docs/reports/F2/step-5.md:1258-1259`, `:1321`; `tests/test_report_guard_states.py:310`,
`:353-366`, `:385-386`.

```
code report :1258  "R276 the `DIAGNOSIS` entry that an earlier `return` made
                    unreachable: the ablation is a helper CALLED FROM BOTH
                    BRANCHES now"
code report :1321  | R276 | **answered** -- S4, the ablation is reachable from
                    both branches |
cmd  grep -n "_assert_diagnosis" tests/test_report_guard_states.py
out  310: def _assert_diagnosis(...)      <- the definition
     386:     _assert_diagnosis(...)      <- ONE call site, in the else branch
cmd  python -c "print(set(DIAGNOSIS) & set(REQUIREMENT_CHANGED))"
out  {shallow_clone_depth_1}
code :353  if state in REQUIREMENT_CHANGED:   ...   :366  return
judge THE `return` R276 NAMED IS STILL AT :366 AND STILL PRECEDES THE CALL AT
      :386. `shallow_clone_depth_1` is in REQUIREMENT_CHANGED, so its DIAGNOSIS
      entry is unreachable exactly as it was. What the refactor removed was the
      `return` AFTER the call, inside the branch that was already reaching it.
      The map still presents four ablation-asserted states and three are.
judge R276 IS A 4a ITEM AND I DO NOT BLOCK ON THE GAP. I block on the row: a
      Carried table that records an unmade change as made is the failure R267
      and R287 are about, and this one is refutable by `grep -c`.
```

**Closed when** the row and section 4 say what was changed, or the REQUIREMENT_CHANGED
branch calls the helper and the `shallow_clone_depth_1` DIAGNOSIS entry is shown to
redden under the ablation.

**R289. (BLOCKS -- head 3) R271's unconditional clause is unmet and the row says
answered.** `docs/reports/F2/step-5.md:1316`; `tests/corpus/report_status_vocabulary.txt`.

```
code verdict 31, R271: "-- and `tests/corpus/report_status_vocabulary.txt` has
     a runner EITHER WAY."
cmd  grep -rn "report_status_vocabulary" --include=*.py --include=*.yml
     --include=*.sh .
out  (nothing outside tests/corpus/)
code report :1316  | R271 | **answered** -- S4, the edit revision 5 claimed |
judge THE MECHANICAL HALF IS DONE AND I SAID SO ABOVE. THE OTHER HALF IS
      UNTOUCHED AND UNMENTIONED: section 4 R271 line says nothing about a
      runner. `CLAUDE.md` sec. Step gating names this shape by its own history:
      "Half of an item is not the item ... the first was fixed, the second was
      untouched, and the report recorded the item as answered."
cmd  for f in tests/corpus/*.txt; do <search the tree for a reader>; done
out  8 files; 3 have a runner. ci_ladder_gating, report_guard_states and
     tolerance_marker_exemptions do; g21_rigid_body_frames, pinned_interpreter,
     report_ci_section and report_status_vocabulary do not. That is R281, and
     it has grown by one, because CF0 deleted the runner pinned_interpreter had.
```

**Closed when** `tests/corpus/report_status_vocabulary.txt` induces a failure when an
entry disagrees with the guard, shown as a run -- or R271's row says the clause is open.

**R290. (BLOCKS -- head 3, and it is an unanswered gated item) Verdict 31's numbered
condition 8 is neither answered nor listed among what is open.**
`docs/reports/F2/step-5.md:1269-1277`, `:1301`.

```
code verdict 31, Next step opens when, item 8: "**The last clause of R256** --
     the rung-6 restoration stated in the report, not only in the commit
     message. The substance is done and I record that."
cmd  sed -n 1156,1449p docs/reports/F2/step-5.md | grep -n "rung 6\|rung6"
out  (nothing)
code report :1269-1277, "What is open, and why": R275, R231/R244/R245,
     R223/R224, R230, R277-R281. R256 is absent.
code report :1301  | R256 | **open** -- carried from an earlier verdict |
judge THE ONE ITEM OF THE NINE THAT WAS A SINGLE SENTENCE TO WRITE IS THE ONE
      THAT WENT MISSING, and the table's blanket status is what hid it -- which
      is R287 doing damage rather than being untidy. This is the failure the
      whole arrangement exists for, in the words of `CLAUDE.md`: the dependency
      list is part of what gets re-read.
```

**Closed when** the report states the rung-6 restoration -- that `ci.yml:293-296` carries
`empty:tests/verification/rung6 full:tests/regression` again and that
`tests/verification/rung6/.empty-by-design` is restored -- or says why it will not.

**R291. (recordable, 4a) `test_a_blocking_item_is_not_routed_to_4a` matches the literal
substring `4a`, and its report-side reach was measured only against the four cells its
author had just written.** `tests/test_report_carried.py:231-249`. New corpus file
`tests/corpus/carried_item_routing.txt`, 10 entries, 4 agree. Measured at 73cf6ce, one
row substituted at a time, R275 -- headed `(BLOCKS ...)` in the answered verdict --
parked with each spelling: `4a` refused; `step 4a` refused; **`F2a` ALLOWED**; **`owned
by docs/milestones/F2a.md` ALLOWED**; **`step four a` ALLOWED**; **`deferred to step 4 a`
ALLOWED**; **`verification apparatus, not this step` ALLOWED**; **`recordable, not
blocking` ALLOWED**. The two legitimate rows stay green. The verdict-side half, read from
the `(BLOCKS ...)` headings, is the right design and I do not fault it; the report side
is a token where a meaning is intended, and `F2a` is the name of the document that owns
the deferred work.

**R292. (recordable, 4a) Nothing now asserts that `pyproject.toml` and `ci.yml` name the
same interpreter.** CF0 deleted `tests/test_the_pinned_interpreter.py`, whose
`test_every_ci_job_runs_the_pinned_version` was the only check binding `requires-python`
to the ten `python-version` entries. The agreement at 73cf6ce is real -- I measured all
ten -- and is now maintained by hand. Retiring the guard was the right call for the
reason given; the residue is that the state CE0 was created by can recur without a red
build, and `tests/corpus/pinned_interpreter.txt` is left with no runner.

## Tolerances touched

**None by this diff.**

```
cmd  git diff b470aee..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat b470aee..HEAD -- floatfea tests/regression
     docs/milestones/F2_figures.md
out  (empty) -- not one line of `floatfea/`, no golden, no figure
judge AN EIGHTH ROUND. `EXEMPT_RESPONSE_DRIFT_ULP = 4.0` has had a red CI, a
      locked Q&A and an obvious one-character fix in front of it for eight
      rounds and has not been touched -- and this is the round in which the
      patience paid. The number it would have been written from turns out to
      have been one vendor's. Nothing was widened, nothing was regenerated to
      match, and the figure I withdrew stayed withdrawn.
```

**What IS a tolerance finding this round is R285**, and like R275 it is not a value: Q8
is the basis every platform-dependent tolerance in this milestone will be written from,
and Q8's stated sufficient condition for canonicity has been refuted by measurement. The
correction is additive and the plan owns it.

**R284 is the second**, under the extension in `CLAUDE.md` sec. Tolerances to "anything
that functions as a tolerance under another name": the byte-identity comparison Q8's
regeneration route depends on is asserted by nothing.

**I also checked the thing that looked wrong and was not.** `regen_figures.py` prints
`1.00x of room` twice, which reads like a gate sitting on its boundary. It is the
boundary bisection straddling the ceiling by construction:
`counter_defect_over_edge` is `2.757e+07x` against `PATCH_TEST_COUNTER_HEADROOM = 6.0e7`
and `counter_headroom_room` is `2.18x`, as the file says. Verified before it was raised.

**My own instructions (item 4b).**

```
cmd  git diff b470aee..HEAD -- .claude docs/SUPERVISOR.md
out  (empty). Not one byte.
cmd  git log --format="%h %s" b470aee..HEAD with per-commit file lists
out  2f6a44e  ci.yml, pyproject.toml, run_rung.sh, six tests/ files, one
              deletion -- no docs/reviews/, no .claude/
     291f096  docs/reports/F2/step-5.md -- the same
     73cf6ce  .github/workflows/ci.yml -- the same
judge No commit touches both code and docs/reviews/. No commit touches .claude/
      or docs/SUPERVISOR.md at all, so the STOP-class condition is not in play.
      CLEAN -- and R282 is why that check is not only about bytes.
```

**What held**, reproduced at my run rather than read: 1778 passed / 0 failed / 0
skipped, matching the report exactly; the whole tree on one interpreter, ten jobs at
3.13 with ruff, black and mypy agreeing; the inert interpreter guard retired rather than
patched; the scanner "What is flagged" list checked clause by clause against the code
that implements it; three of four Carried-row formattings now refused, measured; the
bare `1 xpassed` reddening a rung; the shallow-clone message distinguishing the two
faults it can mean; the escape golden replacing the vacuous bound and going red in both
directions; the two irreproducible figures withdrawn where they stood rather than
republished; `tests/regression` executing on CI for the first time this milestone, ten
times; and `floatfea/tolerances.py` untouched for an eighth round.

**These did not**: the header check reddening the boundary it is checked at (R282), the
report's section 3 against HEAD (R283), the determinism job's byte-identity (R284), Q8's
sufficient condition (R285), the xpass forgery that arrives early (R286), the Carried
table's four false rows and the sentence about how it is made (R287), R276's row (R288),
R271's runner clause (R289), and verdict 31's condition 8 (R290).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Nine blocking items, and they are not of
equal weight. **R283, R284 and R285 are one subject and it is the subject of this
round.** R282 comes first only because it decides what "green" means for everything
after it.

1. **R282 -- the boundary check.** A run at a commit whose only content since the report
   is a verdict, green; or the check withdrawn and item 1b left to the reader, in a
   commit that says which. This is the one I most want answered on its merits: the
   instinct is right -- a machine check beats my eye -- and the shape that shipped is the
   one already measured to cost the meaning of the suite. The ancestry discriminator
   described in R282 is three lines and I would accept it on a run.
2. **R283, R284, R285 -- CF1, finished.** The report says what HEAD is, with the two run
   ids, the two hashes, the per-leg CPU models and the ablation the pin rests on; the ten
   legs are compared by a machine and the comparison is shown to redden on a perturbed
   leg; and the kernel pin goes into Q8 as a condition of canonicity, through the re-lock
   route, with a check that reddens when it is removed. **Then, and only then, the Q8
   values.** The diagnosis is excellent and it is not yet a gate.
3. **R286 -- the ladder's gate.** Neither the xfail reason nor the parametrize id reaches
   exit 0, shown as a run, and the sentence says what the reach is.
4. **R287, R288, R289, R290 -- the dependency list, four sites.** Each row states what
   verdict 31 ruled for that number; `:1189` says what actually produces the table;
   R276's row says what was changed; R271's runner clause is met or declared open;
   condition 8 is answered or refused in writing.
5. **R231, R230, R244, R245, R223, R224 -- unchanged and open by instruction.** R244 and
   R245 now wait on item 2, which subsumes R275.

**Not gates on step 5, into the next report's Carried section:** R291, R292, the
underlying gap in R276, R277-R281, R262, R264, R266, the two R248 residues, R249, R250,
R251, R252, R225-R228, R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 20 new entries at `9cce24b`, across three files, two of them
new, all unseen by the implementer; every `measured` field taken at `73cf6ce` before the
`require` or `expect` beside it was written.**

**The coverage measurement, stated plainly: of my 20 new entries the shipped checks do
what the entry requires on 7.** With the corpus applied,
`tests/test_ci_ladder_gating.py` gives **6 failed, 37 passed**; the two new files have no
runner and induce zero failures, which is still R281.

* `tests/corpus/carried_item_routing.txt` -- **NEW, 10 entries, 4 correct.** CF2's
  verdict-side half reads the `(BLOCKS ...)` headings and is sound. Its report-side half
  is the substring `4a`, and six of eight ways of saying "this belongs to the apparatus
  milestone" go past it -- including `F2a`, which is the milestone's own name.
* `tests/corpus/ci_determinism.txt` -- **NEW, 6 entries, 1 correct.** The job exits 0
  with the committed figures replaced by one line of garbage, and deleting the kernel pin
  leaves the guards suite at 482 passed, 0 failed.
* `tests/corpus/ci_ladder_gating.txt` -- **+4 (37 -> 41), 2 correct.** The bare
  `strict=False` xpass is caught, which is CF4 working; an xfail reason or a parametrize
  id carrying a count phrase is not.

**Thirty-two consecutive rounds have found no element defect, and this round does not
either.** `git diff b470aee..HEAD -- floatfea` is empty. What this round found is again
one thing in several places, and it is the same one: **a check verified against inputs
its own author designed.** The routing guard was written against the four cells that had
just been fixed and misses six spellings of the same act. The first-summary-line rule was
written against the forgery it had just seen and misses the forgery that arrives before
it. And the determinism job -- genuinely the best experiment in this milestone -- was
verified by a person reading ten log lines, so the one conclusion it exists to support is
the one thing in it that no machine will ever check again.

**And the best thing in the range is not a guard.** It is that a reviewer's published
figure was refuted, the refutation was measured rather than argued, and the response was
to build the ten-leg experiment instead of writing the number down. That is the
arrangement working, and it is why the verdict is HOLD rather than STOP: the plan's
answer to Q8 survives this intact, and what has to change is a condition added to it.
What is missing is only that the experiment has not been turned into an assertion, and
that the report at HEAD still says it has not been run.
