# R1 step 4 — guide and witness

# Revision 1 — the step opens: R1139's held repair, its FOUR declaration rows, and R1141

Answers: verdict 47 @ 779e79a
Answers file: `docs/reports/R1/step-4-answers.json`

**2026-11-03. THE SCHEDULE: R1 is due 10 November, full scope, FT2.7 included (FW0), and
seven days remain.** Step 3 closed on 3 November at verdict 47 (PASS) carrying one blocking
item, which this commit answers. Step 4 is the guide and the witness — `docs/USER_GUIDE.md`,
which does not yet exist, and a fresh-context agent reproducing step 1's five fixtures — and
the plan estimates it at one and a half to two days plus half a day for the closures, so the
date holds with margin for three reviewed revisions. **Nothing has slipped and nothing is
escalated under FZ (e).** This is the one hand-written paragraph CZ0 allows a report, and it
carries the schedule because that is what CZ0 says it carries.

```
claim  seven days remain to FW0's 10 November, and FT2.7 is in R1's scope
cmd    python -c "import datetime; a=datetime.date(2026,11,3); \
                  b=datetime.date(2026,11,10); print((b-a).days)"
out    7
cmd    grep -c 'FT2.7' docs/milestones/R1.md
out    14
rule   FW0: "R1 IS DUE 10 NOVEMBER, FULL SCOPE, FT2.7 INCLUDED"
```

## 0. CI at `6fb64c6`, the commit verdict 47 judged — conclusion **SUCCESS**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 47 at `6fb64c6` through the report's own `Answers:` line. Run `41665006727`, event `push`, conclusion **success**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 3907 | 0 | 0 |
| the verification ladder | 2571 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 0 not green.**

**2 job(s) SKIPPED, so unavailable rather than passing:** `CI determinism -- ten legs agree`, `CI determinism -- leg`. A skipped job measured nothing; its zeros are an absence of evidence and not a pass.

**Failing tests named in the log: 0.**

## 0a. Runs since the commit verdict 47 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 47 at `6fb64c6` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that reached no conclusion ABOUT THE CODE -- cancelled, or still running -- has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it. A cancelled run IS `completed`, which is why the test is the conclusion and not the status (CX0, R449, R1130).

| run | event | head | outcome |
|---|---|---|---|
| `41665006727` | push | `6fb64c6` | conclusion **success** |
| `41678716379` | push | `628f134` | conclusion **success** |
| `41769148306` | push | `218730a` | **no result** (`cancelled`) |
| `41769547062` | push | `efd2722` | **no result** (status `in_progress`) |

## 1. What this commit is, and what it is not

**It is step 4's FIRST commit, under directive GB2.** It carries three things and nothing
else: R1139's held repair, the declaration rows that repair makes necessary, and R1141.

**IT IS NOT A REVIEWED REVISION UNDER ES0.** It changes a gate — the site predicate two
guards share — so EQ0 makes it reviewed and EB4 charges that review to no step's rounds.
All three of step 4's ES0 revisions remain available after it. The `# Revision 1` header
above is the form every generator and guard in this repository reads to find the newest
block; it is not a claim on a round, and the reviewer is asked to rule on that basis.

```
claim  this commit touches no production code and no tolerance
cmd    git diff --stat efd2722 -- floatfea
out    (empty)
cmd    git diff efd2722 -- floatfea/tolerances.py | wc -l
out    0
rule   CZ0 (b) is not reached; the diff is a parser repair and a report
```

```
claim  it touches neither the reviewer's instructions nor the adversarial cases
cmd    git diff --stat efd2722 -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)
cmd    git diff --stat efd2722 -- tests/corpus
out    (empty)
rule   the STOP-class head in CLAUDE.md is not reached
```

**THE RANGE IS `efd2722` AND NOT `efd2722..HEAD`, ON PURPOSE.** These four claims are
about THIS commit, and CZ1's reusable half is that a check whose subject is the commit
itself cannot be measured before the commit exists. `git diff efd2722` measures the
working tree that BECOMES this commit, which is measurable while the report is being
written; the same commands in their `..HEAD` form are re-run after the commit and pasted
into its message, so both halves are on the record and neither is a remembered run (CP3).

## 2. R1139 — the held repair, and the row count that moved underneath it

**R1139 is verdict 47's one blocking finding and it carries by name into this step.** The
site pattern required at least one character before the dot (`[\w.-]+\.`), so a stemless
dotfile could not enter `SITES` **at all**, whatever the extension class. `.gitattributes`
is named in the blocks of R959, R967 and R975 — the findings about the byte content of
published CSV deliverables — and `.gitattributes` is the file that decides those bytes.

**The repair adds a second alternative for the stemless form, after the extension form so
the extension branch still wins where both could match.** `_is_a_site` is narrowed for that
one shape: a stemless dotfile must be tracked, separator or not.

```
claim  the delta is FOUR rows, not the three the held patch measured
cmd    python -I <probe> .        # imports tests/test_report_carried.py and filters SITES
out    ('R1139', '.gitattributes', 0)
       ('R959',  '.gitattributes', 0)
       ('R967',  '.gitattributes', 0)
       ('R975',  '.gitattributes', 0)
rule   SITES is derived from the NEWEST verdict file; the patch was measured when
       verdict 46 was newest and verdict 47's own R1139 block names the path too
```

**THE COUNT MOVED BECAUSE THE RULE BENEATH IT MOVED, WHICH IS BP0 AND I AM NOT QUIETLY
SUBSTITUTING THE NEW NUMBER.** SR-25 says the branch "gains EXACTLY the three rows R1139
names" and verdict 47's own R1139 heading says section 8b publishes `2167` of `2170`. Both
were correct when taken, against a verdict file whose newest entry was verdict 46. Verdict
47 then became the newest verdict, its R1139 block names `.gitattributes` in its own text,
and the delta is four. **SR-25 is corrected in place in `docs/directives/FZ.md` rather than
rewritten**, and GB2's phrase "its three declaration rows" is answered with four rows and
this paragraph, not with three rows and a silence.

```
claim  EH4 -- both directions. Only `.gitattributes` is GAINED; every other newly
       matching shape is refused, and nothing that was a site stops being one
cmd    python -I <probe> .        # OLD vs NEW anchor, then `_is_a_site` on the match
out    text                       OLD                      NEW                      site?
       .gitattributes             None                     .gitattributes           True
       a/.gitattributes           None                     a/.gitattributes         False
       foo/.gitkeep               None                     foo/.gitkeep             False
       .github/workflows/ci.yml   .github/workflows/ci.yml .github/workflows/ci.yml True
       scripts/ci_section.py      scripts/ci_section.py    scripts/ci_section.py    True
       .gitattributes-backup      None                     .gitattributes-backup    False
       .gitattributesX            None                     .gitattributesX          False
       x.gitattributes            None                     None                     False
       .github                    None                     .github                  False
       ./.git                     None                     ./.git                   False
       frames.txt                 frames.txt               frames.txt               False
rule   the WEAKENING direction is the one that matters: five shapes newly MATCH the
       pattern and `_is_a_site` refuses every one of them, so the gate does not widen
```

```
claim  the figures this section cites are the ones those records actually carry
cmd    grep -c 'SR-25\|SR-26' docs/directives/FZ.md
out    3
cmd    grep -o 'publishes 2167 rows under the heading' docs/reviews/R1/step-3.md | head -1
out    publishes 2167 rows under the heading
rule   verdict 47's own R1139 heading is where `2167` and `2170` come from, and
       `SR-25` and `SR-26` are headings in FZ's SR log, not measurements
```

**`./.git` IS THE ROW THE FIRST FORM OF THIS REPAIR GAINED BY MISTAKE**, and it is why
`_is_a_site` is narrowed rather than left alone. It is a fragment of
`find . -not -path "./.git/*"` inside R1122's block — a directory in a shell exclusion, not
a site. It got in because R518 admits any separator-bearing path even when nothing is
there, on the ground that a closing condition may name a file to be CREATED; **that ground
rests on the extension telling a filename from a directory name, and a stemless dotfile has
no extension.**

**What the narrowing costs, said rather than left to be found (and accepted as documented
under GB2):** a stemless dotfile a closing condition asks to be CREATED is not a site until
it exists. That is the one direction R518 says must never be silent, so it is said here, in
the docstring, and in SR-26. The extension form is unchanged —
`tests/verification/rung1/test_new_thing.py` is still a site before it exists — and the
narrowing reaches only the shape that produced the noise.

---

## 3. R1141 — R1135's sentence, corrected here because its own report is closed (GB3)

**R1141 is that R1135 was recorded CLOSED in three places and was not closed.** The report,
section 5's table and SR-24 all said the weakening sentence had been reduced to its measured
domain. The ruling was right and verdict 47 endorsed it; **the edit was never made.** That
is the third time in step 3 that a repair was recorded as done and was not, after R1125 and
R1130, and it is the same shape I was fixing in the other two.

```
claim  the sentence is still universal, and it lives in exactly one file
cmd    grep -rn 'the wider pattern takes no text that is not an id' docs/ tests/ scripts/
out    docs/reports/R1/step-3.md:8914  (and two mentions inside the verdict file,
       which are the reviewer's own quotations of it)
rule   one site, in a report whose final verdict is 47
```

```
claim  SR-24 is a heading in FZ's SR log, and `0 of 3810` is verdict 46's figure
       for the reader's live domain -- neither is measured here
cmd    grep -c 'SR-24' docs/directives/FZ.md
out    2
cmd    grep -c '3810' docs/reviews/R1/step-3.md
out    4
rule   both are citations. The only thing this section measures is where the
       sentence lives, which is the triple above
```

**IT IS CORRECTED HERE AND NOT THERE, BECAUSE EK3 FORBIDS THERE.** `docs/reports/R1/step-3.md`
is closed by verdict 47, and EK3 is that a commit never touches a step report after that
report's final verdict — measured three ways, one variable moved, with the report's content
reverted byte-identical still giving `7 failed`. GB3 routes it here, so:

> **The sentence at `docs/reports/R1/step-3.md:8914` reads `claim  the weakening direction:
> the wider pattern takes no text that is not an id`. IT CLAIMS MORE THAN WAS MEASURED. The
> true claim is the narrow one: _over the four refusals and three shapes listed beneath it,
> the wider pattern takes no text that is not an id._ Nothing was measured outside that
> domain, and the universal form should never have been written.**

**No id-shaped predicate is added to the reader**, which is SR-24's ruling and verdict 47's
endorsement of it: the live domain was clean at 0 of 3810 and a new requirement on a clean
reader is apparatus this milestone does not get.

---

## 4. The declaration rows `.gitattributes` now needs

**The repair makes four new parametrised cases exist, and an undeclared site is a red.**
Each row below is the site, what this diff says about it, and why it was left. The phrase
`no change` is the literal string the guard looks for on the site's own line.

```
claim  these four rows are the complete set of `.gitattributes` cases, and the
       table below is that set -- not a selection from it
cmd    python -I <probe> .     # filters tests/test_report_carried.py's own SITES
out    ('R1139', '.gitattributes', 0)
       ('R959',  '.gitattributes', 0)
       ('R967',  '.gitattributes', 0)
       ('R975',  '.gitattributes', 0)
rule   the same `SITES` the guard parametrises over, so the table cannot
       enumerate a different set than the check does
```

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R959 | `.gitattributes` | the file is untouched | **no change.** R959 is about the stored bytes of `docs/F6_utilisation.csv`; the declaration this gate was blind to is now visible, and the byte question itself carries as a ledger row. |
| R967 | `.gitattributes` | the file is untouched | **no change.** Same file, same reason: the gate can now see the site, which is what R1139 asked for. Changing the attributes would re-normalise a published deliverable and is not in this step's scope. |
| R975 | `.gitattributes` | the file is untouched | **no change.** The third of the byte-content group. Visible, declared, and untouched. |
| R1139 | `.gitattributes` | the file is untouched | **no change.** This row exists BECAUSE of the repair: verdict 47's own R1139 block names the path, so the finding that the path was invisible now names it as a site. The repair is in the pattern, not in `.gitattributes`. |

**THAT FOURTH ROW IS THE ONE GB2 DID NOT KNOW ABOUT, AND IT IS NOT A BONUS.** It is the
measurement in section 2: the set is derived from the newest verdict, the newest verdict
changed, and a repair measured against the old one shipped a count that was already stale.
A repair whose row count depends on which verdict is newest is not a fixed delta.

---

## 5. CZ1 — what is owed, what is not, and what I measured anyway

**Verdict 47 rules that CZ1 (ii) and (iii) are OWED AT THE CLOSURE COMMIT, WHICH DOES NOT
EXIST**, so the four outputs are not a debt this report pays. Its own row says so: *"OWED at
the closure commit, which does not exist yet. The whole-suite line is paid in s.11 and I
reproduced it."* Step 3's eleven closure items were answered inside revision 3 at `00cbafb`
and `6fb64c6`, both of which verdict 47 reviewed; no separate closure commit was written.

**I measured the four gates at `628f134` regardless**, because that commit is the one that
recorded step 3's closing and nothing between it and this report measures it. Its CI run
is `41678716379` and it reached **conclusion `success`** — named here because R412
happened twice: a run's job rows can all be green while the run concluded `failure`.

```
claim  the four CZ1 (ii) gates at 628f134, in a clean detached worktree
cmd    git worktree add --detach <wt> 628f134 && cd <wt>
       python -m ruff check floatfea tests
       python -m black --check floatfea tests
       python -m mypy floatfea
out    git status --porcelain   : (empty)
       ruff                     : All checks passed!
       black                    : 128 files would be left unchanged.
       mypy                     : Success: no issues found in 45 source files
rule   CZ1 (ii), three of its four; the fourth is below
```

```
claim  CZ1 (iii) at 628f134 -- run `41678716379` reached conclusion **success**,
       and its `guards and meta-tests` step RAN rather than being skipped
cmd    gh run list --commit $(git rev-parse 628f134) --json databaseId,conclusion,status
out    [{"databaseId":41678716379 -> conclusion **success**, "status":"completed"}]
cmd    gh api repos/xabi80/FloatFEA/actions/runs/41678716379 -> conclusion **success**
         /jobs -q '.jobs[] | select(.name=="lint, unit and guards") | .steps[] | ...'
out    5  success  actionlint          8   success  mypy
       6  success  ruff                9   success  unit tests
       7  success  black --check       10  success  guards and meta-tests
rule   CZ1 (iii) exists to show the guards step RAN rather than being skipped behind an
       earlier red. Step 10 is `success`, not `skipped`, and the RUN's own conclusion is
       marked beside each id above -- job rows can be green under a failed run (R412)
note   the `out` line reorders `gh`'s own field order, which prints `conclusion` FIRST.
       That is not cosmetic: the guard gives each run id the text from itself to the next
       id, so a conclusion printed BEFORE the id leaves the id naked. The id and its
       conclusion are written adjacent here for that reason, and the raw `gh` order is
       `{"conclusion":"success","databaseId":...,"status":"completed"}`
```

**AND `gh run list --commit` NEEDS THE FULL SHA.** With the short `628f134` it prints `[]`
— an empty result that reads exactly like "no run exists for this commit". That is a trap in
CZ1 (iii)'s own paste, it is not a defect in `floatfea/`, and it is recorded as a ledger row
rather than claimed as a finding.

```
claim  the short sha gives an empty result where the full sha gives run
       `41678716379`, conclusion **success**
cmd    gh run list --commit 628f134 --json databaseId,conclusion,status
out    []
cmd    gh run list --commit 628f13455d7a3409cfbf68a6b45f72ff0c9a5ed2 --json ...
out    [{"databaseId":41678716379 -> conclusion **success**, "status":"completed"}]
rule   one variable moved -- the sha's length -- and nothing else (BG0)
```

**EQ0 attaches to this commit.** It changes a gate, so it is reviewed, and EB4 charges that
review to no step's rounds. Verdict 47 predicted exactly this: *"if it lands in the closure
commit that commit is REVIEWED, at no step's cost (EB4)."*

## 6. The findings this commit answers

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R1 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R835 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R836 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R838 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R843 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R845 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R846 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R847 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R848 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R849 | carried | **later** | §7 | `` | carried from an earlier verdict |
| R850 | recorded | **later** | §7 | `` | THE WALL-CLOCK EXCLUSION COVERS THREE OF THE FIVE ROWS |
| R851 | recorded | **later** | §7 | `` | THE PROVENANCE EXCLUSION IS CHECKED BY BASENAME ONLY, |
| R852 | recorded | **later** | §7 | `` | A CAVEAT TRUNCATED TO ITS OWN MARKER IS GREEN ON 31 OF |
| R853 | recorded | **later** | §7 | `` | "102, 1289 AND 73 COMPARABLE LINES" |
| R854 | recorded | **later** | §7 | `` | R849 NOW HAS A SECOND SITE. The new gate |
| R855 | recorded | **later** | §7 | `` | THE SUITE WAS NOT RUN AT |
| R856 | recorded | **later** | §7 | `` | `scripts/write_verdict.py` REFUSES TO WRITE A VERDICT FOR A STEP THAT HAS NO REPORT, |
| R857 | recorded | **later** | §7 | `` | R853'S REPAIR REPUBLISHED R853'S DEFECT. The corrected |
| R858 | recorded | **later** | §7 | `` | THE FILE STILL ASSERTS THAT |
| R859 | recorded | **later** | §7 | `` | THE NEW COMMENT NAMES THE WRONG ASSERTION. It says a sixth |
| R860 | recorded | **later** | §7 | `` | `_TIMING_STAGES` IS A HAND COPY OF THE LITERAL TUPLE AT `floatfea/cli.py:297`, AND NOTHING |
| R861 | recorded | **later** | §7 | `` | THE BASELINE OF NINE REDS WAS WRONG WITHIN ONE COMMIT OF MY |
| R862 | recorded | **later** | §7 | `` | "THERE IS NO SECOND COPY" IS REFUTED BY ONE GREP. |
| R863 | recorded | **later** | §7 | `` | THE |
| R864 | recorded | **later** | §7 | `` | "THE REFACTOR PRODUCES BYTE-IDENTICAL |
| R865 | recorded | **later** | §7 | `` | THE |
| R866 | blocks | **later** | §7 | `` | `load_cases.headings` IS PARSED, RANGE-CHECKED, REPEAT-CHECKED -- AND READ BY NOTHING. |
| R867 | recorded | **later** | §7 | `` | DECLARATION ORDER AND DIRECTION DECIDE WHETHER A DECLARED |
| R868 | recorded | **later** | §7 | `` | THE COMMITTED TEST FOR "A NON-STAR TOPOLOGY" BUILDS THE |
| R869 | recorded | **later** | §7 | `` | A DECLARED TOPOLOGY |
| R870 | recorded | **later** | §7 | `` | FL2(a) AS SHIPPED IS A SUBSET OF THE LOCKED PLAN'S (a), |
| R871 | recorded | **later** | §7 | `` | FS1'S |
| R872 | recorded | **later** | §7 | `` | `headings: [360.0]` IS INSIDE THE DECLARED DOMAIN AND IS |
| R873 | recorded | **later** | §7 | `` | A SIDECAR WHOSE |
| R874 | recorded | **later** | §7 | `` | THE DECLARED SIDE REFUSES A BOOL BY NAME AND THE RECORDED |
| R875 | recorded | **later** | §7 | `` | 82f922c FIXED THE LIST R871 NAMED AND LEFT ITS SIBLING TWO PARAGRAPHS ABOVE. `docs/SUPERVISOR.md |
| R876 | recorded | **later** | §7 | `` | R872 PUT AN |
| R877 | blocks | **later** | §7 | `` | R874's REPAIR IS GATED BEHIND `load_cases.headings` BEING |
| R878 | recorded | **later** | §7 | `` | `floatfea/cli.py:146-149` SUBSCRIPTS FOUR KEYS THAT |
| R879 | recorded | **later** | §7 | `` | TWO OF THE THREE THINGS R873's AND R874's CONDITIONS NAMED |
| R880 | recorded | **later** | §7 | `` | `.claude/agents/gating-supervisor.md` TELLS ME TO READ "EH1, EJ2 AND FC1 -- THE TWO BOUNDARY |
| R881 | recorded | **later** | §7 | `` | THE |
| R882 | recorded | **later** | §7 | `` | R877's CLOSING CONDITION NAMED TWO SITES AND THE SECOND |
| R883 | recorded | **later** | §7 | `` | TWO SENTENCES IN `_validated_wave_basis`'s OWN DOCSTRING |
| R884 | recorded | **later** | §7 | `` | COMPLETE-OR-EMPTY HOLDS ONLY WHEN `run` IS A MAPPING. A |
| R885 | recorded | **later** | §7 | `` | THE RAW DOMAIN CHECK REFUSES A SIGNED RECORDING, AND |
| R886 | recorded | **later** | §7 | `` | THE `# noqa: F401` THIS COMMIT ADDED SUPPRESSES NOTHING |
| R887 | blocks | **later** | §7 | `` | `ba0ce03` MOVED THE MARKER TO A STEP WITH NO REPORT, AND THE NEGATIVE-CONTROL |
| R888 | recorded | **later** | §7 | `` | THE R799/R800 ORPHAN |
| R889 | recorded | **later** | §7 | `` | "A DEADLOCK THAT HAD |
| R890 | recorded | **later** | §7 | `` | THE CHECKPOINT'S "OF STEP 3'S NINE CODE COMMITS, TWO WERE |
| R891 | recorded | **later** | §7 | `` | REPLAY 1 IN `f9954f7`'s MESSAGE -- "(empty) exit=0 <- THIS |
| R892 | recorded | **later** | §7 | `` | "AND THE CONTROL, ONE VARIABLE MOVED -- THE OLD HOOK ON |
| R893 | recorded | **later** | §7 | `` | ONE LIVE SITE STILL STATES THE PREMISE FT0 RETIRED AS A |
| R894 | recorded | **later** | §7 | `` | R1's STEP-3 GATE ROW DOES NOT CARRY FT2's ITEMS 6 AND 7, |
| R895 | blocks | **later** | §7 | `` | THE RECORDED WAVE-HEIGHT PAIR IS NEVER CHECKED AGAINST LAMBDA, AND |
| R896 | blocks | **later** | §7 | `` | THE SAME DEFECT AT A SECOND DOOR, AND IT IS THE ONE EZ0 NAMES BY NAME. |
| R897 | blocks | **later** | §7 | `` | R887 IS NOT CLOSED. TWO NEGATIVE-CONTROL STATES NOW DIE IN `_build` WITH |
| R898 | recorded | **later** | §7 | `` | `closed_by_a_pass` |
| R899 | recorded | **later** | §7 | `` | `docs/SUPERVISOR.md` STATES CZ0's FOUR HEADS AS THE CRITERION BOTH REVIEWERS RULE UNDER, NAMES |
| R900 | recorded | **later** | §7 | `` | "ALL FOUR ARE PUSHED (FP1), SO EACH HAS A CI RUN |
| R901 | recorded | **later** | §7 | `` | `NEXT` CARRIES TWO STACKED DOCSTRINGS AND THE SECOND IS A |
| R902 | blocks | **later** | §7 | `` | THE GENERATOR NOW VALIDATES THE RECORDED WAVE HEIGHT AND THEN IGNORES IT. EVERY NUMBER THE DELIV |
| R903 | blocks | **later** | §7 | `` | THE REPAIR ROUTED THE FOUR `WAVE_BASIS_KEYS` AND LEFT FIVE RECORDED FIELDS AT THE SAME READER UN |
| R904 | recorded | **later** | §7 | `` | THE REPAIRED ASSERTION IS TWO SCALAR COMPARISONS WHERE THE CLOSING CONDITION SAID "EVERY COPY TH |
| R905 | recorded | **later** | §7 | `` | R895's REPAIR REPLACED ONE UNVERIFIABLE ABSENCE CLAIM IN `floatfea/` WITH ANOTHER, AND ADDED TWO |
| R906 | blocks | **later** | §7 | `` | A RED TEST AT THE REVIEWED COMMIT THAT FAILS BOTH LIMBS OF THE PREDICATE. `c071e68` DELETED `FRO |
| R907 | blocks | **later** | §7 | `` | THE R902 REPAIR REACHED THE COMPUTED TABLE AND LEFT THE PUBLISHED VERDICTS. AT A RECORDED HEIGHT |
| R908 | blocks | **later** | §7 | `` | THE REPAIR MADE `sidecar.run.lambda` THE FROUDE SCALE OF A PUBLISHED CSV, AND NOTHING COMPARES I |
| R909 | blocks | **later** | §7 | `` | `run.periods_full_s` IS NOT MERELY PRINTED -- IT IS THE LOOP VARIABLE OF THE BAND TABLE. A SEVEN |
| R910 | recorded | **later** | §7 | `` | THE R904 LOOP INSPECTS 16 OF THE 29 ACTIONS `STATES` CARRIES AND SKIPS 13 UNDER A SILENT `else:  |
| R911 | recorded | **later** | §7 | `` | `pipeline.py:704-717` says "no declared counterpart exists for any of them", which is false for  |
| R912 | recorded | **later** | §7 | `` | The complete-or-empty contract now fires on a sidecar that records NO wave basis at all. A `run` |
| R913 | recorded | **later** | §7 | `` | The `WAVE_BASIS_KEYS` docstring says the five fields are what "every published artifact states", |
| R914 | recorded | **later** | §7 | `` | `scripts/measure/member_forces_table.py:147-153` is now a bare string expression documenting a c |
| R915 | recorded | **later** | §7 | `` | A sidecar without `run.lambda` is refused as PARTIAL even though the npz carries the authoritati |
| R916 | recorded | **later** | §7 | `` | `hsp_tag = True` publishes `provenance tag : True`. Acceptable as declared open (heading 1): a s |
| R917 | recorded | **later** | §7 | `` | The second sub-case of R884, the uncaught `TypeError` at `pipeline.py:869` from a membership tes |
| R918 | recorded | **later** | §7 | `` | Two cosmetic exits that publish first and fail after: `member_forces_table.py:312` raises `Value |
| R919 | blocks | **later** | §7 | `` | THE R906 REPAIR PUT A PUBLISHED-DELIVERABLE GENERATOR ON AN AUTHORITY NOTHING CROSS-CHECKS AND N |
| R920 | recorded | **later** | §7 | `` | `floatfea/run/pipeline.py:944-946` says "The committed `data/f4/dynamic_inputs.npz` **predates t |
| R921 | recorded | **later** | §7 | `` | A second site of R918, in the script this commit changed: `scripts/measure/f6a_premise_check.py: |
| R922 | recorded | **later** | §7 | `` | `tests/regression/test_f6_deliverable_agrees_with_itself.py:490` scans a HAND-WRITTEN list of tw |
| R923 | recorded | **later** | §7 | `` | `test_the_names_this_test_guards_are_the_ones_the_consumers_ASK_FOR` greps for the `MFT` attribu |
| R924 | recorded | **later** | §7 | `` | `scripts/measure/member_forces_table.py:148-154` is still the bare string expression R914 named, |
| R925 | blocks | **later** | §7 | `` | THE FROUDE CONVERSION FACTORS ARE PUBLISHED AS `lambda = 50` LITERALS INTO BOTH F4 DELIVERABLES, |
| R926 | blocks | **later** | §7 | `` | THE REPAIR ROUTED TWO OF THE THREE PUBLISHING READERS THROUGH THE VALIDATOR. THE THIRD -- `f6_re |
| R927 | blocks | **later** | §7 | `` | `--provenance` IS DECLARED AS "the authority for the scale and the height" AND THIS COMMIT TOOK  |
| R928 | recorded | **later** | §7 | `` | The R909 orphan check compares a sidecar float against a float parsed back out of a `{:g}`-forma |
| R929 | recorded | **later** | §7 | `` | R909's condition said "in both directions". `set(_recorded) - _solved` is computed; `_solved - s |
| R930 | recorded | **later** | §7 | `` | `member_forces_table.py:166` says of the `GOVERNING_PERIODS` docstring that "no number for them  |
| R931 | recorded | **later** | §7 | `` | `SENSITIVITY_PERIODS = (10.0, 20.0)` at `:180` is referenced by nothing -- `grep -rn "SENSITIVIT |
| R932 | recorded | **later** | §7 | `` | `validated_export_scale` raises `ConfigError`, and neither generator catches it, so an out-of-do |
| R933 | recorded | **later** | §7 | `` | `grep -rn "R907\|R909" tests/ --include=*.py` is **empty**, and nothing in `tests/` or `.github/ |
| R934 | recorded | **later** | §7 | `` | The two `scripts/measure/` readers now REFUSE a disagreeing npz/sidecar pair; `floatfea run` --  |
| R935 | recorded | **later** | §7 | `` | The five new cells import `validated_export_scale` function-locally, five times, rather than ext |
| R936 | blocks | **later** | §7 | `` | THE FA0 CLAUSE IS GATED ON A MEMBERSHIP PREDICATE, NOT ON THE SEA STATE FA0 RULED ON, SO `docs/F |
| R937 | blocks | **later** | §7 | `` | THE R925 REPAIR PUBLISHES THE TWO CONVERSION FACTORS THROUGH `:.0f`, SO THE FACTOR IN BOTH F4 DE |
| R938 | blocks | **later** | §7 | `` | `f6_results_report.py` NOW RESOLVES THE SCALE AND THE WAVE BASIS FROM `--npz` AND `--provenance` |
| R939 | recorded | **later** | §7 | `` | The new destination-only arm asserts the wrong directory for `append_finding`, and declares thre |
| R940 | recorded | **later** | §7 | `` | The new gate's property (iii) is green on the tree R925 lived in, and no test anywhere asserts t |
| R941 | recorded | **later** | §7 | `` | `validated_export_scale`'s explicit-sidecar form inherits the default form's silent skip: the co |
| R942 | recorded | **later** | §7 | `` | Two prose residues of the new two-branch form. The computed branch's "breaking ... <list>" quant |
| R943 | recorded | **later** | §7 | `` | `results/F6/F4_member_forces.csv` is a third copy of the SCALE line, byte-identical to `docs/F4_ |
| R944 | blocks | **later** | §7 | `` | THE R936 REPAIR PUBLISHES "T = 12.5 s IS INSIDE THE BAND AT THIS HEIGHT" AT EVERY RECORDED HEIGH |
| R945 | blocks | **later** | §7 | `` | THE NEW JOIN IS A SUBSTRING TEST, SO A FORCES TABLE GENERATED AT lambda = 500 IS ACCEPTED AT RES |
| R946 | blocks | **later** | §7 | `` | `test_R933_ANOTHER_SEA_STATE_RUNS_rather_than_refusing[f6_results_report.py]` ASSERTS EXIT 0 FOR |
| R947 | recorded | **later** | §7 | `` | The published-factor format now has TWO definitions. `f6_results_report.py:333-338` re-implement |
| R948 | recorded | **later** | §7 | `` | The node-id diff that could not see the eleventh id: the added id is in `tests/test_no_tolerance |
| R949 | recorded | **later** | §7 | `` | R918's shape, with a second witness: `member_forces_table.py` ends with `args.out.relative_to(RO |
| R950 | blocks | **later** | §7 | `` | THE R944 REPAIR REPLACED A ONE-SIDED TEST WITH A FOUR-WAY CATEGORY AND THEN READ THREE OF THE FO |
| R951 | blocks | **later** | §7 | `` | `f6_results_report.py:636` STILL DECIDES "IS THIS THE REFERENCE SEA STATE?" WITH THE MEMBERSHIP  |
| R952 | blocks | **later** | §7 | `` | THE NEW HEIGHT JOIN SKIPS WHEN THE HEADER CARRIES NO HEIGHT -- `if _seen_h and ...` -- SO R938 O |
| R953 | recorded | **later** | §7 | `` | The other boundary of the R944 `else` arm, solved because EH4 asks for both. Just above `H = 24. |
| R954 | recorded | **later** | §7 | `` | `tests/regression/test_generators_refuse_mismatched_inputs.py:9-15` says "The cells are cheap be |
| R955 | recorded | **later** | §7 | `` | `member_forces_table.py:396-397` prints `args.out.relative_to(ROOT)` AFTER both files are writte |
| R956 | recorded | **later** | §7 | `` | CLOSED at the cause.** `ls scratch` is "No such file or directory", `grep -rn 'ROOT / "scratch"' |
| R957 | blocks | **later** | §7 | `` | THE R951 REPAIR DROPPED THE FOUR MEMBERSHIP CONJUNCTS AND KEYS ON HEIGHT ALONE, SO THE HAND-WRIT |
| R958 | blocks | **later** | §7 | `` | THE PERIOD JOIN IS ONE-DIRECTIONAL. `set(_recorded) - _solved` REFUSES A DECLARED PERIOD WITH NO |
| R959 | blocks | **later** | §7 | `` | , AND CA2: A RED CI IS A HOLD) CI IS RED AT THE REVIEWED COMMIT. `ladder 6 -- it stays fixed` FA |
| R960 | recorded | **later** | §7 | `` | `scripts/measure/member_forces_table.py:458` says "The five other `scripts/measure/` scripts sti |
| R961 | recorded | **later** | §7 | `` | `_shown` is now defined twice, identically, at `f6_results_report.py:240` and `member_forces_tab |
| R962 | recorded | **later** | §7 | `` | FA0 ruled at one sea state. The predicate now reads that height from a mutable input file rather |
| R963 | recorded | **later** | §7 | `` | R950's decision boundary is not bracketed by any cell. With params at 10.0 and 14.21 (the no-que |
| R964 | recorded | **later** | §7 | `` | `test_R951`'s `claimed` needle is asserted nowhere to be FOUND: `grep -rn "The governing basis i |
| R965 | recorded | **later** | §7 | `` | The height-mismatch refusal interpolates a Python list: "the CSV's own caveats state H = ['24.1' |
| R966 | recorded | **later** | §7 | `` | One document, one height, two spellings: `f6_results_report.py:551` writes `H = {h_full} m` and  |
| R967 | blocks | **later** | §7 | `` | THE THIRD INPUT IS JOINED TO NOTHING. `--util` CARRIES EVERY UTILISATION THE REPORT PUBLISHES AN |
| R968 | blocks | **later** | §7 | `` | R957 IS NOT CLOSED. THE REFERENCE GATE IS A HEIGHT COMPARISON AND THE NEW JOIN DOES NOT CONSTRAI |
| R969 | blocks | **later** | §7 | `` | THE JOIN COMPARES SETS WHERE THE DOCUMENT ITERATES A LIST. A DUPLICATE DECLARED PERIOD PASSES BO |
| R970 | recorded | **later** | §7 | `` | THE R959 CLASS IS CLOSED FOR CSVs AND OPEN FOR EVERY OTHER DELIVERABLE. IN A FRESH CHECKOUT AT T |
| R971 | recorded | **later** | §7 | `` | R959's CONDITION (ii) IS UNMET AT THE SITE I NAMED, AND THE REPORT DOES NOT SAY THE SITE WAS LEF |
| R972 | recorded | **later** | §7 | `` | `test_R959`'s docstring says "`*.csv -text` stores the bytes. This asserts the property directly |
| R973 | recorded | **later** | §7 | `` | OBSERVED LIVE, WITH A TRACEBACK)** My first probe handed the generator a forces CSV with no non- |
| R974 | recorded | **later** | §7 | `` | `git worktree list` carries twelve `AppData/Local/Temp/suite-count-*/tree` registrations, and `g |
| R975 | recorded | **later** | §7 | `` | `.gitattributes` says "Every tracked CSV here is a generator artifact, so the rule is the file s |
| R976 | blocks | **later** | §7 | `` | A DUPLICATED UTILISATION ROW PASSES BOTH NEW JOINS AND IS PUBLISHED TWICE. ONE VARIABLE MOVED -- |
| R977 | blocks | **later** | §7 | `` | R968 IS NOT CLOSED. THE NEW CONJUNCT READS ITS REFERENCE FROM THE SAME FILE `--provenance` DEFAU |
| R978 | blocks | **later** | §7 | `` | THE UTIL JOIN COMPARES KEYS AND PERIODS AND NOT THE QUANTITY THE TWO TABLES SHARE. ONE VARIABLE  |
| R979 | recorded | **later** | §7 | `` | THE DERIVATION MIRRORS TWO OF THE PRODUCER'S FOUR CONJUNCTS. IT IS AN OVER-REFUSAL AND NEVER A S |
| R980 | recorded | **later** | §7 | `` | THE JOIN IS VACUOUS WHEN BOTH DERIVED SETS ARE EMPTY, AND THE ONLY THING THAT CATCHES IT IS THE  |
| R981 | recorded | **later** | §7 | `` | R918 / R956's REPAIR REACHED TWO FILES AND THE CENSUS IS SEVEN SHORT. I HIT IT LIVE: `api_wsd_ut |
| R982 | recorded | **later** | §7 | `` | THE NEW UTIL REFUSAL'S NARRATIVE HALF IS ONE-DIRECTIONAL.** Driving the `_util_extra` branch pri |
| R983 | recorded | **later** | §7 | `` | `STATIONS_CHECKED` ARRIVES FROM `floatfea.run.pipeline`, WHICH DOES NOT WRITE THE FILE.** `api_w |
| R984 | recorded | **later** | §7 | `` | THE JOIN KEYS DROP `body`.** `_util_expected`, `_util_got` and `_periods_for` key on `(member, s |
| R985 | recorded | **later** | §7 | `` | `_wrong_period` COMPARES PERIODS AS STRINGS** (`r.get("period_full_s", "")` against a set of str |
| R986 | blocks | **later** | §7 | `` | THREE OF THE SEVEN CLAIMS IN THE PARAGRAPH `_reference` GUARDS ARE ABOUT THE STRESS BOUND, WHICH |
| R987 | blocks | **later** | §7 | `` | THE RECORDED HEADING AND THE RECORDED PERIOD COUNT ARE PUBLISHED AS LITERALS AT FOUR SITES OUTSI |
| R988 | recorded | **later** | §7 | `` | FOUR MORE LITERALS OF THE SAME CLASS ARE TRUE TODAY AND GO FALSE AT A NAMED NEXT ITEM.** `:713`  |
| R989 | recorded | **later** | §7 | `` | THE TURN'S SUITE FIGURE IS NOT A WHOLE-SUITE FIGURE: `--ignore=tests/test_report_carried.py` EXC |
| R990 | recorded | **later** | §7 | `` | MY OWN STATE-(2) CONTROL DID NOT MEASURE WHAT I SAID IT MEASURED. `docs/reviews/R1/step-3.md` DO |
| R991 | blocks | **later** | §7 | `` | THE THREE BOUND SENTENCES ARE NOW INTERPOLATED, AND TWO OF THEIR CONCLUSIONS ARE STILL DECIDED B |
| R992 | blocks | **later** | §7 | `` | THE NEW VALUE JOIN REACHES ALL 23 PUBLISHED UTILISATION COLUMNS AND DOES NOT REACH `sigma_Pa`, W |
| R993 | recorded | **later** | §7 | `` | THE EH4 TABLE IN `test_R978_a_CHANGE_BELOW_THE_PUBLISHED_PRECISION_is_accepted`'s DOCSTRING IS M |
| R994 | recorded | **later** | §7 | `` | FOUR MORE LITERAL CLAIMS ABOUT THE RUN SIT OUTSIDE THE CENSUS'S STATED DOMAIN, AND TWO OF THEM S |
| R995 | recorded | **later** | §7 | `` | `git diff --stat HEAD~1` IS `816 insertions(+), 102 deletions(-)`, NOT `792`.** `git diff --shor |
| R996 | recorded | **later** | §7 | `` | A NEGATIVE NEEDLE THAT EMBEDS A SPELLED COUNT IS VACUOUS AT ANY OTHER COUNT.** `assert "largest  |
| R999 | recorded | **later** | §7 | `` | THE DIFF MADE `sigma_Pa` AND `tau_Pa` ORPHAN COLUMNS OF A PUBLISHED DELIVERABLE, AND IT IS THE O |
| R1000 | recorded | **later** | §7 | `` | A RANK CLAUSE CAN PUBLISH TWO EQUAL FIGURES AS THE EVIDENCE FOR A STRICT ORDERING.** At my state |
| R1001 | recorded | **later** | §7 | `` | TWO CITATIONS IN THE NEW R994 COMMENT RESOLVE ONE FRAME AND FIVE LINES OFF.** `f6_results_report |
| R1002 | recorded | **later** | §7 | `` | R993's RESIDUE: THE DOCSTRING STILL PUBLISHES THREE ROWS WHILE THE CELL RUNS ONE OF THEM.** The  |
| R1003 | recorded | **later** | §7 | `` | MY VERDICT 21 NAMED THE RIGHT REPAIR FOR R992 FOR THE WRONG REASON, AND THE WRONG REASON WAS THE |
| R1005 | blocks | **later** | §7 | `` | THE NPZ RECORDS EACH CASE'S PERIOD TWICE, NOTHING COMPARES THE TWO, AND FL2(d)'s SCREEN IS KEYED |
| R1006 | blocks | **later** | §7 | `` | and (d), FR1) TWO RED TESTS AT THE REVIEWED COMMIT THAT FAIL THE FS1/FT1 BOUNDARY PREDICATE, IN  |
| R1007 | blocks | **later** | §7 | `` | A MALFORMED SIDECAR `run` BLOCK NOW SILENTLY DISABLES THE WHOLE FL2(d) SCREEN, AND I MEASURED TH |
| R1008 | recorded | **later** | §7 | `` | `out_of_band_governing` ADMITS A BREAKING WAVE WITH NO FURTHER DECLARATION, AND `BREAKING` HAS N |
| R1009 | recorded | **later** | §7 | `` | THE EH4 BREAKING CELL ASSERTS THE LABEL WHERE THE LOAD-BEARING PROPERTY IS THE DECISION.** `test |
| R1010 | recorded | **later** | §7 | `` | TEN LIVE COPIES OF THE BAND AND STEEPNESS COEFFICIENTS REMAIN IN THE TWO EZ0 GENERATOR SCRIPTS A |
| R1011 | recorded | **later** | §7 | `` | `_recorded_height`'s DOCSTRING STATES A FALSE CALL GRAPH AS THE REASON FOR ITS ASYMMETRY WITH `_ |
| R1012 | recorded | **later** | §7 | `` | `refuse_cases_that_cannot_govern` SILENTLY SKIPS A DECLARED PERIOD THAT IS NOT IN THE FILE.** Bo |
| R1013 | recorded | **later** | §7 | `` | FOUR STALE LINE CITATIONS IN THE LIVE TREE; THE CENSUS IS IN ANSWER (5c) ABOVE AND YOUR LIST OF  |
| R1014 | recorded | **later** | §7 | `` | THE FU0 EXEMPTION'S REVERSE GUARD PASSES ON A PARTIAL REPAIR.** Three arms in answer (4) above.  |
| R1015 | recorded | **later** | §7 | `` | THE `H = 0` REFUSAL IS RIGHT AND ITS MESSAGE IS ODD, AND CALM WATER CAN SET AN ENVELOPE IF DECLA |
| R1016 | recorded | **later** | §7 | `` | A NEGATIVE CONTROL THAT DIES IN `next()`.** `tests/test_report_carried.py::test_the_generator_wo |
| R1017 | recorded | **later** | §7 | `` | NO CI JOB RUNS `tests/regression/`, SO FL2(d)'s END-TO-END GATE HAS NO INDEPENDENT WITNESS.** `. |
| R1018 | blocks | **later** | §7 | `` | THE NEW `test_one_gravity.py` RELOADS A LIBRARY MODULE AND POISONS IT FOR THE REST OF THE PROCES |
| R1021 | blocks | **later** | §7 | `` | R1005 REPAIR IS EVADED BY DELETING THE SECOND RECORD AT EXACTLY THE INDICES THAT DISAGREE, WHICH |
| R1022 | blocks | **later** | §7 | `` | R1019 DOMAIN CHECK REACHES ONE OF THE THREE READERS OF `periods_full_s`, AND THE TWO IT MISSES A |
| R1023 | recorded | **later** | §7 | `` | R1017 IS FALSE: `tests/regression/` RUNS ON EVERY PUSH, IN THE `ladder` JOB. The entry I routed  |
| R1024 | recorded | **later** | §7 | `` | THE R1018 FOUR-ARM TABLE IN THE COMMIT MESSAGE IS STALE BY THE TWO CELLS THE SAME COMMIT ADDED.* |
| R1025 | recorded | **later** | §7 | `` | R1010 REPAIR IS HOLDABLE BY A TEST, MEASURED, SO "A NO-OP SUBSTITUTION CANNOT BE DETECTED" IS FA |
| R1026 | recorded | **later** | §7 | `` | FIVE PUBLISHED LITERALS OF THE BAND AND STEEPNESS CONSTANTS SURVIVE R1010 SWEEP, AND ONE OF THEM |
| R1027 | recorded | **later** | §7 | `` | `floatfea/basis.py:89` SAYS `period_band.py` IS "THE ONLY CONSUMER OF THESE THREE CONSTANTS", AN |
| R1028 | recorded | **later** | §7 | `` | TWO OBSERVATIONS ON R1019 PLACEMENT, BOTH ABOUT WHERE RATHER THAN WHETHER.** (i) The refusal sit |
| R1029 | recorded | **later** | §7 | `` | THE DEFECT ARM 06 FOUND IN THE NEW REFUSAL IS STILL STANDING IN THE OLD ONE, WHICH IS THE MESSAG |
| R1030 | recorded | **later** | §7 | `` | THE `# not-a-tolerance:` MARKER IS AN UNCONDITIONAL, FREE-TEXT SILENCER ON THE COMPARISON OWN LI |
| R1031 | recorded | **later** | §7 | `` | `tests/unit` IS A PUSH PATH, AND THE STEP IT RUNS IN GREW BY 149 SECONDS AT THIS COMMIT.** The C |
| R1032 | recorded | **later** | §7 | `` | THE GUARD THAT READS WHICH FINDINGS A VERDICT MARKS AS BLOCKING CANNOT TELL "BLOCKS" FROM "DOES  |
| R1033 | blocks | **later** | §7 | `` | THE TYPE GATE THIS COMMIT ADDED FOR THAT FAMILY LISTS THE PYTHON TYPES A JSON SIDECAR CAN PRODUC |
| R1034 | recorded | **later** | §7 | `` | THE `mass_eps` CONCLUSION IS RIGHT AND NEITHER REASON GIVEN FOR IT IS WHAT HOLDS IT.** The turn' |
| R1035 | recorded | **later** | §7 | `` | THE EMPTY-SEQUENCE ALLOWANCE IS SAFE AND ITS STATED REASON NAMES A CHECK THAT NEVER RUNS ON IT.* |
| R1036 | recorded | **later** | §7 | `` | THE DOOR'S DOCSTRING MEASURES THE MODEL-SCALE CASE AT ONE OF ITS THREE CALLERS. I WENT TO SHOW T |
| R1037 | recorded | **later** | §7 | `` | THE NEW REFUSAL'S REMEDY SENTENCE WILL BE WRONG FOR THE FILES THIS STEP'S OWN GATE PRODUCES.** T |
| R1038 | recorded | **later** | §7 | `` | THE DUPLICATED `not-a-tolerance:` BLOCK.** `tests/unit/test_forces_table_reexports.py` carries t |
| R1039 | recorded | **later** | §7 | `` | R899's COUNT IS WRONG IN ONE DIRECTION AND THE DRIFT IS REAL IN THE OTHER.** Verdict 24 reported |
| R1040 | recorded | **later** | §7 | `` | THERE IS A THIRD RECORD OF THE SAME QUANTITY AND NOTHING COMPARES IT.** The sidecar's `run` bloc |
| R1042 | blocks | **later** | §7 | `` | THE SAME DEFECT AT A FOURTH SITE, IN THE SAME FUNCTION AS THE THIRD, FOUR LINES BELOW THE REPAIR |
| R1043 | blocks | **later** | §7 | `` | with CA2: a red test and a red CI at the reviewed commit, failing BOTH limbs of the FS1/FT1 pred |
| R1044 | recorded | **later** | §7 | `` | of my own amended R1033 condition, and it was neither met nor stated as left) THE MEMBERSHIP IS  |
| R1045 | recorded | **later** | §7 | `` | THE DOCSTRING THAT TELLS A READER WHICH BRANCH IS LIVE IS FALSE IN ITS FIRST CLAUSE.** `exported |
| R1046 | recorded | **later** | §7 | `` | A SHAPE-(2,) `froude_lambda` IS REFUSED WITH "the npz could not be read".** Driven: `np.array([5 |
| R1047 | recorded | **later** | §7 | `` | THE PRE-COMMIT SELECTION RULE WAS "WHAT DID I EDIT" AND IT HAS TO BE "WHAT EXERCISES WHAT I EDIT |
| R1048 | recorded | **later** | §7 | `` | A WAITER ANCHORED ON `[0-9]+ failed,` FIRED ON AN INNER SYNTHETIC RUN'S SUMMARY AT 52%.** They c |
| R1049 | recorded | **later** | §7 | `` | `scripts/write_verdict.py` STAMPS `HEAD`, AND `HEAD` IS NOT THE JUDGED COMMIT WHEN THE IMPLEMENT |
| R1050 | recorded | **later** | §7 | `` | THE TRACKED FILE THAT REVERTED AT 17:36 WAS ME, NOT A SYNC.** The implementer measured a tracked |
| R1051 | blocks | **later** | §7 | `` | THE JOINT-REACTION ARRAY'S DTYPE IS CHECKED NOWHERE. A BOOL-TYPED `case{i}/lam` IS ACCEPTED, SOL |
| R1052 | recorded | **later** | §7 | `` | THE TWO SCALE READERS RAISE AN UNCAUGHT `AttributeError` OR `OverflowError` ON SIX SIDECAR SHAPE |
| R1053 | recorded | **later** | §7 | `` | THE COMMIT MESSAGE'S OWN `git diff --name-only` OUTPUT NAMES TWO FILES WHERE THE DIFF IS THREE.* |
| R1054 | recorded | **later** | §7 | `` | `floatfea/run/config.py` SAYS "every one of numpy's twenty-two dtype KINDS is a single non-empty |
| R1055 | recorded | **later** | §7 | `` | THE COMPLEMENT NAMES 17 EXCLUDED ROOT FILES AS "the remaining root-level report guards". AT MOST |
| R1056 | recorded | **later** | §7 | `` | THE R1044 REPAIR IS CORRECT AND HELD BY NOTHING.** Restoring `kind in "iuf"` in place of the tup |
| R1057 | recorded | **later** | §7 | `` | A NEW PARAMETER'S OWN LABEL DESCRIBES A DIFFERENT VALUE.** In the R1042 cell: `pytest.param("JSO |
| R1058 | blocks | **later** | §7 | `` | A NON-FINITE `case{i}/lam` IS ACCEPTED, SOLVED AND PUBLISHED. THE GOVERNING CASE SET TO NaN GIVE |
| R1059 | recorded | **later** | §7 | `` | THE ADMITTED SET IS float16, float32 AND float64, AND THE DOCSTRING'S OWN REASON -- TRUNCATION - |
| R1060 | recorded | **later** | §7 | `` | THE INSTINCT WAS RIGHT, THE CONCLUSION IS RIGHT, AND THE RUN YOU PASTED DID NOT REACH THE CODE I |
| R1061 | recorded | **later** | §7 | `` | FOUR MEASUREMENTS ARE PUBLISHED IN A `floatfea/` DOCSTRING AND IN A USER-FACING REFUSAL, AND NOT |
| R1062 | recorded | **later** | §7 | `` | THE REFUSAL DOES NOT NAME THE FILE, AND THIS STEP'S OWN GATE PUTS SEVERAL FILES IN ONE RUN.** Ev |
| R1063 | blocks | **later** | §7 | `` | A `case{i}/lam` WITH ZERO TIMESTEPS IS |
| R1064 | recorded | **later** | §7 | `` | THE TREE FINGERPRINT CARRIES NO COMMAND |
| R1065 | recorded | **later** | §7 | `` | `test_the_SEARCH_reads_no_gravity_at_all` |
| R1066 | recorded | **later** | §7 | `` | A BIG-ENDIAN `>f8` `lam` IS REFUSED WITH |
| R1067 | recorded | **later** | §7 | `` | "candidate {index} of {count}" MIXES A |
| R1068 | recorded | **later** | §7 | `` | THE R1060 INCIDENTAL IS AT A SECOND |
| R1069 | blocks | **later** | §7 | `` | THE DIAGONAL FORCE AND THE DIAGONAL'S BUCKLING LENGTH ARE |
| R1070 | blocks | **later** | §7 | `` | R1063 SURVIVES ONE MORE KEY EDIT. NOTHING |
| R1071 | blocks | **later** | §7 | `` | `sections.truss.d_over_t` AND `joint_allowance` ACCEPT A |
| R1072 | blocks | **later** | §7 | `` | THE TRIANGLE'S FACE-SHEAR ALLOCATION DOES NOT CLOSE AGAINST `Vz` OR `T`, THE BOX'S CLOSES EXACTL |
| R1073 | blocks | **later** | §7 | `` | THE REWRITTEN BULLET PUBLISHES THE *FORCE* FACTOR AS THE *AREA* FACTOR, AND THE AREA FACTOR IS L |
| R1074 | blocks | **later** | §7 | `` | THE GENERATOR HARD-CODES FOUR FIGURES ABOUT *THIS DECK* AND *THIS GRID* INTO AN ARTIFACT IT WRIT |
| R1075 | blocks | **later** | §7 | `` | THE NEW PARAGRAPH PUBLISHES "A ROW WITH A LARGE TORSION PUTS `uniform_panel` AHEAD FOR BOTH SHAP |
| R1076 | blocks | **later** | §7 | `` | THE AREA-FACTOR TABLE IS A FOUR-ROW SAMPLE AT ONE UNSTATED LOAD AND ONE UNSTATED READING OF A QU |
| R1077 | blocks | **later** | §7 | `` | THE R1075 REPAIR PUT FOUR NEW DECK-SPECIFIC LITERALS, INCLUDING THE WORDS "ON THIS DECK", INTO T |
| R1078 | blocks | **later** | §7 | `` | THE COMPUTED FIGURE THAT REPLACED R1074 HARD-CODED ONE IS COUNTED OVER A DOMAIN THAT CANNOT CONT |
| R1079 | blocks | **later** | §7 | `` | THE SENTENCE THAT REPLACED THE RETRACTED "NONE OF IT IS THE BRACED LENGTH" PUBLISHES A BOUND --  |
| R1080 | blocks | **later** | §7 | `` | THE BULLET THAT TELLS A READER WHETHER THE KNOWN DEFECT REACHES A PUBLISHED NUMBER CONDITIONS TH |
| R1081 | blocks | **later** | §7 | `` | THE R1077 REPAIR DELETED THE DECK-SPECIFIC LITERALS AND ALSO DELETED THE QUALIFIER THAT MADE THE |
| R1082 | blocks | **later** | §7 | `` | `_margin` NEW LABEL IS FALSE AT AN ADMISSIBLE GRID SHAPE: AT `depths: [3.0, 3.0]` THE ARTIFACT N |
| R1083 | recorded | **later** | §7 | `` | NOTHING IN THE TREE HOLDS L43's REPAIR, AND THE COMMIT MESSAGE'S ARM FIGURE FOR IT DOES NOT REPR |
| R1084 | recorded | **later** | §7 | `` | `EXACT` IS THE RIGHT WORD AND I PROVED THE HALF YOU COULD NOT -- BUT THE SAME CLAUSE RE-OPENS L4 |
| R1085 | recorded | **later** | §7 | `` | L46's TRAILING CAUSE IS A FOURTH COMMA-ITEM IN A LIST IT IS TRUE OF ONLY ONE MEMBER OF, SO AT A  |
| R1086 | recorded | **later** | §7 | `` | THE TEST COMMENT SAYS THE RETIRED WORDING IS `forbidden`. NOTHING FORBIDS IT, AND NOTHING CAN, B |
| R1087 | recorded | **later** | §7 | `` | THE NEW ASSERTIONS READ A FIFTH FIELD FROM A FIXTURE WHOSE DOCSTRING SAYS IT CARRIES FOUR, AND T |
| R1088 | recorded | **later** | §7 | `` | `no triangle figure in these tables is ever HIGH` IS FALSE UNDER ONE OF THE THREE CORRECTIONS TH |
| R1089 | recorded | **later** | §7 | `` | R1085's REPAIR INTRODUCES A THIRD AGREEMENT PAIR INTO THAT ONE SENTENCE AND ONLY THE SINGULAR BR |
| R1090 | recorded | **later** | §7 | `` | R1086 IS CLOSED AT A SITE MY CONDITION DID NOT NAME AND OPEN AT THE ONE IT DID.** `tests/regress |
| R1091 | recorded | **later** | §7 | `` | YOUR QUALIFIER IS TRUE -- WIDER THAN YOU VERIFIED IT -- AND THE ENUMERATION BEHIND IT IS COARSER |
| R1092 | recorded | **later** | §7 | `` | : 1890 cells, 139 identical, **154 MISMATCHES |
| R1093 | blocks | **later** | §7 | `` | `report.md` PUBLISHES THE FIRST FILE'S WAVE BASIS AS "THE WAVE BASIS THESE LOADS WERE EXPORTED A |
| R1094 | blocks | **later** | §7 | `` | THE FL2(d) SECTION STATES ONE FILE'S ASSOCIATED-PERIOD BAND AS THE BAND, OVER A TABLE CONCATENAT |
| R1095 | blocks | **later** | §7 | `` | A MIXED SET -- ONE FILE THAT RECORDS A HEIGHT AND ONE THAT DOES NOT -- PUBLISHES A COMPLETE-LOOK |
| R1096 | blocks | **later** | §7 | `` | `Checked stations: 64. Over unity: 16.` ON A MODEL WITH 32 STATIONS, 12 OF THEM OVER UNITY. THE  |
| R1097 | recorded | **later** | §7 | `` | `_governing_provenance`'s DOCSTRING STILL DESCRIBES THE IMPLEMENTATION THE REPAIR DELETED, AND A |
| R1098 | recorded | **later** | §7 | `` | "THE FIELDNAMES ARE STATED EXPLICITLY RATHER THAN INFERRED FROM THE RECORD" IS FALSE, AND I MEAS |
| R1099 | recorded | **later** | §7 | `` | YOUR READING OF FW1's SCOPE IS RIGHT. THE CONSEQUENCE IS THAT `utilisation.csv` NOW CARRIES 32 P |
| R1100 | recorded | **later** | §7 | `` | THE ONE-FILE AND MULTI-FILE HEADING COMPARISONS ARE DIFFERENT FUNCTIONS WITH DIFFERENT ARITHMETI |
| R1101 | recorded | **later** | §7 | `` | A REFUSAL THIS COMMIT ADDS HAS AN AGREEMENT PAIR WITH NO SINGULAR BRANCH, AND NOTHING ASSERTS EI |
| R1102 | recorded | **later** | §7 | `` | `Row.source` AND `Row.heading_deg` CARRY DEFAULTS, SO MY "APPEND WITH NO DEFAULT" CONSTRAINT BOU |
| R1103 | recorded | **later** | §7 | `` | TWO OF THE THREE ARTIFACTS' SHARED CAVEATS ARE SINGULAR PROSE ABOUT A PLURAL RUN, AND ONE OF THE |
| R1104 | blocks | **later** | §7 | `` | TWO DIFFERENT DECLARED FILES WHOSE BASENAMES COLLIDE ARE ACCEPTED AT EXIT 0, AND EVERY ARTIFACT  |
| R1105 | recorded | **later** | §7 | `` | WHAT CANCELLED THE RUN IS A PUSH FROM YOUR SIDE, AND THE MECHANISM WILL DO IT EVERY TIME.** Reco |
| R1106 | blocks | **carried** | §7 | `` | The FY3 supersession reached ONE of three sibling artifacts. 84 of 168 rows in a published CSV c |
| R1107 | recorded | **carried** | §7 | `` | The hook narrowing moved FOUR WRITE rows from DENY to ALLOW, and `>|` is the one that matters. |
| R1108 | recorded | **carried** | §7 | `` | The rung-3 class guard transfers a CLASS label to an entry that did not declare it. Your report  |
| R1109 | recorded | **later** | §7 | `` | The coincidence rule's TABLE 1 reproduces exactly. BOTH of TABLE 2's published margin figures ar |
| R1110 | recorded | **later** | §7 | `` | The plan declares `NODE_COINCIDENCE_DECIMALS` `STRUCTURAL`; the file deliberately declares no cl |
| R1111 | recorded | **later** | §7 | `` | `wave_basis_from_sidecar` is a third door and it CANNOT reconcile. Your two doors are right; the |
| R1112 | recorded | **later** | §7 | `` | A multi-element `froude_lambda` makes `_npz_scale_key` return None, which SKIPS the reconciliati |
| R1113 | recorded | **later** | §7 | `` | The third wrong-exception-class site, which you asked me to assume exists. It does, and `config. |
| R1114 | recorded | **later** | §7 | `` | `exported_wave_basis` gates on `is_file()` and `wave_basis_from_sidecar` on `exists()`, so R1007 |
| R1115 | recorded | **later** | §7 | `` | A published supersession note points at a document that does not exist. |
| R1116 | recorded | **later** | §7 | `` | The new `!=` is exact in the strict direction, as you claim. The weakening direction has one fal |
| R1117 | recorded | **carried** | §7 | `` | I removed my own worktree while a measurement was still running in it, and 33 reds are the resul |
| R1119 | blocks | **carried** | §7 | `` | `scripts/ci_section.py` cannot see a failing test whose id contains a space, so the generated CI |
| R1120 | recorded | **carried** | §7 | `` | R1118's repair reached four of the six sites. The two it missed require a dot the verdicts do no |
| R1121 | recorded | **carried** | §7 | `` | FT2.5's condition 4 -- the one sentence of disclosure for Xabier -- is absent at the first revis |
| R1122 | recorded | **later** | §7 | `` | R1115 has MOVED, and the move is in the wrong direction. One of the two destinations the publish |
| R1123 | recorded | **later** | §7 | `` | The over-refusal the hook repair costs is bigger than the one row you measured -- 5 of 10 legiti |
| R1124 | recorded | **carried** | §7 | `` | Nine of the eleven carried L ledger ids are named nowhere in the report, and the cause is that n |
| R1125 | recorded | **later** | §7 | `` | Two triples whose out field is not what the cmd printed. |
| R1126 | carried | **carried** | §7 | `` | carried from an earlier verdict |
| R1127 | carried | **carried** | §7 | `` | carried from an earlier verdict |
| R1128 | blocks | **later** | §7 | `` | `_SITE` admits only `py|md|sh|txt|json`, so no site named in a `.csv`, `.yml`, `.yaml`, `.npz`,  |
| R1129 | recorded | **later** | §7 | `` | The `answered_table` half of R1120's repair made the dot optional on BOTH sides, which widened i |
| R1130 | recorded | **later** | §7 | `` | R1125's second half is open and section 6 says it is repaired. `scripts/ci_section.py` still emi |
| R1131 | recorded | **later** | §7 | `` | Section 1's scope triple is stale at the commit that ships it. `cmd git log --oneline cd6d6fe..H |
| R1132 | recorded | **later** | §7 | `` | Section 4's triple does not support its claim. `claim ... the set is the seven it declared`; `cm |
| R1133 | recorded | **later** | §7 | `` | The `_` block of `docs/reports/R1/step-3-answers.json` is revision 1's and the file is revision  |
| R1134 | recorded | **later** | §7 | `` | A figure whose rule moved was regenerated in one place and not the other, in the same commit. Re |
| R1135 | recorded | **later** | §7 | `` | Section 2's weakening-direction claim is wider than what was measured. "the wider pattern takes  |
| R1136 | recorded | **later** | §7 | `` | and it is the SR-16 RULING YOU ASKED FOR rather than a finding against the repair.** **BP0 is sa |
| R1137 | recorded | **later** | §7 | `` | Section 0's job table publishes the two determinism jobs as `0 | 0 | 0` under **"Job conclusions |
| R1139 | blocks | **answered** | §2 | `` | The site pattern cannot match a STEMLESS DOTFILE at all, whatever the extension class, so `.gita |
| R1140 | recorded | **later** | §7 | `` | YOUR FIRST ASK, ANSWERED WITH THE ENUMERATED SET AND A COMMITTED ARM.** Five planted heading for |
| R1141 | recorded | **answered** | §3 | `` | R1135 is recorded CLOSED in three places and is not closed: the sentence it was to replace is by |
| R1142 | recorded | **later** | §7 | `` | R1132's repair publishes two wrong `out` fields, and one of them is the same defect R1132 was. |
| R1143 | recorded | **later** | §7 | `` | Section 2's four site counts are stale by exactly the R1138 repair that landed in the same commi |
| R1144 | recorded | **later** | §7 | `` | The site gate's declaration lookup is keyed on the PATH and not on the finding, so one `no chang |
| R1145 | recorded | **later** | §7 | `` | `docs/reports/R1/step-3.md`, section 10, second block: the closing code fence carries prose on t |
| R1146 | recorded | **later** | §7 | `` | The `_` block of the answers file says "R1132 Section 4's needle selected 15 headings where the  |

## 7. The ledger rows still open, every one named

**297 items point at this section.** They are named here individually and
not as a family, because EG3 (i) is that a group ruled by class is a group nobody is
reading: the eighth member of exactly such a group turned out to be a real defect
(R629). None of them is touched by this diff and none is claimed as answered.

```
claim  the count on the line above is DERIVED from the answers file, not typed
cmd    python -c "import json,pathlib; d=json.loads(pathlib.Path(
         'docs/reports/R1/step-4-answers.json').read_text(encoding='utf-8'))
         ['answered']; print(sum(1 for v in d.values() if v['state'] !=
         'answered'), len(d))"
out    297 299
rule   R1133: the previous block said THREE and listed four. The count is
       derived from the list it describes or it is not written
```

**The `L` and `R11xx` ids below are IDENTIFIERS, not measurements.** `L47` carries
no figure `47`; it is a name. They are listed so the closure artifact has them in
one place.

* `R1`, `R835`, `R836`, `R838`, `R843`, `R845`, `R846`, `R847`, `R848`, `R849`
* `R850`, `R851`, `R852`, `R853`, `R854`, `R855`, `R856`, `R857`, `R858`, `R859`
* `R860`, `R861`, `R862`, `R863`, `R864`, `R865`, `R866`, `R867`, `R868`, `R869`
* `R870`, `R871`, `R872`, `R873`, `R874`, `R875`, `R876`, `R877`, `R878`, `R879`
* `R880`, `R881`, `R882`, `R883`, `R884`, `R885`, `R886`, `R887`, `R888`, `R889`
* `R890`, `R891`, `R892`, `R893`, `R894`, `R895`, `R896`, `R897`, `R898`, `R899`
* `R900`, `R901`, `R902`, `R903`, `R904`, `R905`, `R906`, `R907`, `R908`, `R909`
* `R910`, `R911`, `R912`, `R913`, `R914`, `R915`, `R916`, `R917`, `R918`, `R919`
* `R920`, `R921`, `R922`, `R923`, `R924`, `R925`, `R926`, `R927`, `R928`, `R929`
* `R930`, `R931`, `R932`, `R933`, `R934`, `R935`, `R936`, `R937`, `R938`, `R939`
* `R940`, `R941`, `R942`, `R943`, `R944`, `R945`, `R946`, `R947`, `R948`, `R949`
* `R950`, `R951`, `R952`, `R953`, `R954`, `R955`, `R956`, `R957`, `R958`, `R959`
* `R960`, `R961`, `R962`, `R963`, `R964`, `R965`, `R966`, `R967`, `R968`, `R969`
* `R970`, `R971`, `R972`, `R973`, `R974`, `R975`, `R976`, `R977`, `R978`, `R979`
* `R980`, `R981`, `R982`, `R983`, `R984`, `R985`, `R986`, `R987`, `R988`, `R989`
* `R990`, `R991`, `R992`, `R993`, `R994`, `R995`, `R996`, `R999`, `R1000`, `R1001`
* `R1002`, `R1003`, `R1005`, `R1006`, `R1007`, `R1008`, `R1009`, `R1010`, `R1011`, `R1012`
* `R1013`, `R1014`, `R1015`, `R1016`, `R1017`, `R1018`, `R1021`, `R1022`, `R1023`, `R1024`
* `R1025`, `R1026`, `R1027`, `R1028`, `R1029`, `R1030`, `R1031`, `R1032`, `R1033`, `R1034`
* `R1035`, `R1036`, `R1037`, `R1038`, `R1039`, `R1040`, `R1042`, `R1043`, `R1044`, `R1045`
* `R1046`, `R1047`, `R1048`, `R1049`, `R1050`, `R1051`, `R1052`, `R1053`, `R1054`, `R1055`
* `R1056`, `R1057`, `R1058`, `R1059`, `R1060`, `R1061`, `R1062`, `R1063`, `R1064`, `R1065`
* `R1066`, `R1067`, `R1068`, `R1069`, `R1070`, `R1071`, `R1072`, `R1073`, `R1074`, `R1075`
* `R1076`, `R1077`, `R1078`, `R1079`, `R1080`, `R1081`, `R1082`, `R1083`, `R1084`, `R1085`
* `R1086`, `R1087`, `R1088`, `R1089`, `R1090`, `R1091`, `R1092`, `R1093`, `R1094`, `R1095`
* `R1096`, `R1097`, `R1098`, `R1099`, `R1100`, `R1101`, `R1102`, `R1103`, `R1104`, `R1105`
* `R1106`, `R1107`, `R1108`, `R1109`, `R1110`, `R1111`, `R1112`, `R1113`, `R1114`, `R1115`
* `R1116`, `R1117`, `R1119`, `R1120`, `R1121`, `R1122`, `R1123`, `R1124`, `R1125`, `R1126`
* `R1127`, `R1128`, `R1129`, `R1130`, `R1131`, `R1132`, `R1133`, `R1134`, `R1135`, `R1136`
* `R1137`, `R1140`, `R1142`, `R1143`, `R1144`, `R1145`, `R1146`

**The `L` ids and `R1109`-`R1116` carry too**, unswept, as ES0 allows. **The count
is measured here rather than carried, and it is not eleven.** Every previous report
and digest in this step says "the eleven `L` ids (L47-L56, L58)", which is verdict
46's carried list; the verdict file names FOURTEEN, because verdict 47 recorded L57
and L60 as present as well and L59 is there too. The grep is the figure:

```
claim  the L ids the verdict file actually names, and the R11xx group
cmd    grep -oE 'L(4[7-9]|5[0-9]|60)' docs/reviews/R1/step-3.md | sort -u
out    L47 L48 L49 L50 L51 L52 L53 L54 L55 L56 L57 L58 L59 L60
cmd    grep -oE 'R111[0-6]|R1109' docs/reviews/R1/step-3.md | sort -u
out    R1109 R1110 R1111 R1112 R1113 R1114 R1115 R1116
rule   BF0: the count was carried across three documents without being re-taken,
       and 11 of 14 is the kind of shortfall FS1 was adopted over. All of them go
       to the closure artifact; the three extra are named here so the artifact
       cannot inherit the short list
```

**R1122 and R1123 carry unchanged.** R1122 is a published pointer that resolves and
is empty (`results/F6b/truss_sizing.md:41`). R1123 is the hook's over-refusal, and
**this commit bought three more rows of it**: a heredoc quoting a verdict path was
refused; so was a command whose only redirect was `2>/dev/null` beside a verdict-path
mention; and so was the heredoc that would have written this very assembly script,
because the script names the verdict file it reads. Each time I used the editing tool
instead and reshaped nothing (FM1). The refusal keys on a redirect operator plus a
mention, not on the read, which is what the earlier seven rows established.

```
claim  the two remaining figures in this section's prose, sourced
cmd    grep -c 'eleven `L` ids' docs/reviews/R1/step-3.md
out    2            -- verdict 46's carried list, quoted twice in the file
cmd    sed -n '41p' results/F6b/truss_sizing.md
out    old-versus-new table, with a ratio column, is in R1 step 3's report.
rule   R1122 is that this pointer RESOLVES and the table is not there. The line
       number is the site, not a measurement, and it still points at nothing
```

## 8. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R1 | **later** — §7 | no clause this generator can cut -- see the verdict's Carried section |
| R835 | **later** — §7 | (EG3's enumeration) \| still open, still Xabier's; this commit is its eighth measurement \| of... |
| R836 | **later** — §7 | no clause this generator can cut -- see the verdict's Carried section |
| R838 | **later** — §7 | no clause this generator can cut -- see the verdict's Carried section |
| R843 | **later** — §7 | no clause this generator can cut -- see the verdict's Carried section |
| R845 | **later** — §7 | (not one number in the three published R1 deliverables is compared against anything) \| ANSWERED... |
| R846 | **later** — §7 | (the R838 repair is green on three injections one step above the one it was built for) \|... |
| R847 | **later** — §7 | (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) \| still open, correctly... |
| R848 | **later** — §7 | (the empty-directory refusal admits ., ./, .., " . ") \| still open, untouched by this diff, and... |
| R849 | **later** — §7 | (the caveat, disclaimer and provenance gates quantify over a hard-coded three-file tuple, and... |
| R850 | **later** — §7 | THE WALL-CLOCK EXCLUSION COVERS THREE OF THE FIVE ROWS THE GENERATOR WRITES, SO TWO WALL-CLOCK... |
| R851 | **later** — §7 | THE PROVENANCE EXCLUSION IS CHECKED BY BASENAME ONLY, AND THE KEY-SET PIN READS report.md... |
| R852 | **later** — §7 | A CAVEAT TRUNCATED TO ITS OWN MARKER IS GREEN ON 31 OF 31 CASES. TABLE_CAVEATS[8] reduced from... |
| R853 | **later** — §7 | "102, 1289 AND 73 COMPARABLE LINES" DOES NOT REPRODUCE. The comparable counts are 99, 1286 and... |
| R854 | **later** — §7 | R849 NOW HAS A SECOND SITE. The new gate repeats the hard-coded three-file tuple, so FR3's two... |
| R855 | **later** — §7 | THE SUITE WAS NOT RUN AT A PUSHED, REVIEWED COMMIT, AND THE TREE'S NINE REDS WERE NOT RECORDED... |
| R856 | **later** — §7 | scripts/write_verdict.py REFUSES TO WRITE A VERDICT FOR A STEP THAT HAS NO REPORT, AND FR3 PLUS... |
| R857 | **later** — §7 | R853'S REPAIR REPUBLISHED R853'S DEFECT. The corrected figure 99, 1286 and 70 COMPARABLE lines... |
| R858 | **later** — §7 | THE FILE STILL ASSERTS THAT BOTH EXCLUDED CLASSES "ARE CHECKED SEPARATELY", AND NOTHING IN THE... |
| R859 | **later** — §7 | THE NEW COMMENT NAMES THE WRONG ASSERTION. It says a sixth stage row "reddens HERE rather than... |
| R860 | **later** — §7 | _TIMING_STAGES IS A HAND COPY OF THE LITERAL TUPLE AT floatfea/cli.py:297, AND NOTHING COMPARES... |
| R861 | **later** — §7 | THE BASELINE OF NINE REDS WAS WRONG WITHIN ONE COMMIT OF MY WRITING IT. The tree is at 78, and... |
| R862 | **later** — §7 | "THERE IS NO SECOND COPY" IS REFUTED BY ONE GREP. THREE HAND COPIES OF THE STAGE SET REMAIN AND... |
| R863 | **later** — §7 | THE EXCLUSION SET IS NOW DEFINED BY THE CODE UNDER TEST, SO A SIXTH PUBLISHED ROW IS EXEMPTED... |
| R864 | **later** — §7 | "THE REFACTOR PRODUCES BYTE-IDENTICAL DELIVERABLES" IS TRUE, AND THE REGENERATION GATE CANNOT... |
| R865 | **later** — §7 | THE DOCSTRING OF THE FUNCTION WHOSE COMMENT WAS CORRECTED STILL SAYS "A FOURTH... |
| R866 | **later** — §7 | load_cases.headings IS PARSED, RANGE-CHECKED, REPEAT-CHECKED -- AND READ BY NOTHING. floatfea... |
| R867 | **later** — §7 | DECLARATION ORDER AND DIRECTION DECIDE WHETHER A DECLARED TOPOLOGY CAN BE RUN AT ALL. The... |
| R868 | **later** — §7 | THE COMMITTED TEST FOR "A NON-STAR TOPOLOGY" BUILDS THE ONE ORDER THAT CANNOT BE RUN, AND NO... |
| R869 | **later** — §7 | A DECLARED TOPOLOGY THAT DOES NOT REACH THE CENTRE BUILDS HAPPILY, AND _build_body RIGID-LINKS... |
| R870 | **later** — §7 | FL2(a) AS SHIPPED IS A SUBSET OF THE LOCKED PLAN'S (a), AND TWO SENTENCES IN... |
| R871 | **later** — §7 | FS1'S OWN COMMIT LEFT A HAND LIST IN MY INSTRUCTIONS AND REMOVED IT FROM CLAUDE.md. Its check... |
| R872 | **later** — §7 | headings: [360.0] IS INSIDE THE DECLARED DOMAIN AND IS REFUSED AGAINST AN EXPORT AT 0 DEG,... |
| R873 | **later** — §7 | A SIDECAR WHOSE heading_deg IS A LIST MAKES THE COMPARISON RAISE TypeError INSTEAD OF... |
| R874 | **later** — §7 | THE DECLARED SIDE REFUSES A BOOL BY NAME AND THE RECORDED SIDE COERCES ONE. heading_deg: true... |
| R875 | **later** — §7 | 82f922c FIXED THE LIST R871 NAMED AND LEFT ITS SIBLING TWO PARAGRAPHS ABOVE. docs/SUPERVISOR.md... |
| R876 | **later** — §7 | R872 PUT AN EQUIVALENCE RELATION INSIDE A GATE AND CALLED IT ARITHMETIC. NOTHING IN THE 29... |
| R877 | **later** — §7 | R874's REPAIR IS GATED BEHIND load_cases.headings BEING DECLARED, AND R874's OWN PUBLISHED... |
| R878 | **later** — §7 | floatfea/cli.py:146-149 SUBSCRIPTS FOUR KEYS THAT exported_wave_basis BUILDS ONE KEY AT A TIME.... |
| R879 | **later** — §7 | TWO OF THE THREE THINGS R873's AND R874's CONDITIONS NAMED ARE NOT DONE AND NOT DECLARED... |
| R880 | **later** — §7 | .claude/agents/gating-supervisor.md TELLS ME TO READ "EH1, EJ2 AND FC1 -- THE TWO BOUNDARY... |
| R881 | **later** — §7 | THE RECORDED HEADING GETS ALL THREE OF THE DECLARED SIDE'S CHECKS AND THE TWO RECORDED WAVE... |
| R882 | **later** — §7 | R877's CLOSING CONDITION NAMED TWO SITES AND THE SECOND IS UNTOUCHED AND NOT DECLARED LEFT. THE... |
| R883 | **later** — §7 | TWO SENTENCES IN _validated_wave_basis's OWN DOCSTRING AND REFUSAL TEXT ARE FALSE AT THIS... |
| R884 | **later** — §7 | COMPLETE-OR-EMPTY HOLDS ONLY WHEN run IS A MAPPING. A SIDECAR WHOSE run BLOCK IS A LIST... |
| R885 | **later** — §7 | THE RAW DOMAIN CHECK REFUSES A SIGNED RECORDING, AND docs/conventions.md:150 RECORDS THAT THE... |
| R886 | **later** — §7 | THE # noqa: F401 THIS COMMIT ADDED SUPPRESSES NOTHING TODAY AND COVERS FOUR IMPORTS TOMORROW.... |
| R887 | **later** — §7 | ba0ce03 MOVED THE MARKER TO A STEP WITH NO REPORT, AND THE NEGATIVE-CONTROL HARNESS DERIVES ITS... |
| R888 | **later** — §7 | THE R799/R800 ORPHAN SWEEP GLOBS docs/reports/F/step-.md, AND R1 IS THE ACTIVE MILESTONE. AN... |
| R889 | **later** — §7 | "A DEADLOCK THAT HAD ABSORBED SEVEN INTERIM CHECKS" IS A CAUSAL CLAIM IN THREE SHIPPED PLACES... |
| R890 | **later** — §7 | THE CHECKPOINT'S "OF STEP 3'S NINE CODE COMMITS, TWO WERE NEW FL2 ITEMS AND FIVE WERE REPAIRS... |
| R891 | **later** — §7 | REPLAY 1 IN f9954f7's MESSAGE -- "(empty) exit=0 <- THIS TREE CLEARS" -- IS FALSE AT HEAD. AT... |
| R892 | **later** — §7 | "AND THE CONTROL, ONE VARIABLE MOVED -- THE OLD HOOK ON THIS SAME TREE" MOVED TWO. THE STASH... |
| R893 | **later** — §7 | ONE LIVE SITE STILL STATES THE PREMISE FT0 RETIRED AS A RULE, AND NO LIVE PLAN STATES THE RULE... |
| R894 | **later** — §7 | R1's STEP-3 GATE ROW DOES NOT CARRY FT2's ITEMS 6 AND 7, AND THE STEP WILL BE CLOSED AGAINST... |
| R895 | **later** — §7 | THE RECORDED WAVE-HEIGHT PAIR IS NEVER CHECKED AGAINST LAMBDA, AND WAVE_HEIGHT's [0, 100] m IS... |
| R896 | **later** — §7 | THE SAME DEFECT AT A SECOND DOOR, AND IT IS THE ONE EZ0 NAMES BY NAME.... |
| R897 | **later** — §7 | R887 IS NOT CLOSED. TWO NEGATIVE-CONTROL STATES NOW DIE IN _build WITH shutil.SameFileError... |
| R898 | **later** — §7 | closed_by_a_pass READS ANY Verdict: PASS IN A STEP'S REVIEW FILE AS CLOSURE, AND R888's GLOB... |
| R899 | **later** — §7 | docs/SUPERVISOR.md STATES CZ0's FOUR HEADS AS THE CRITERION BOTH REVIEWERS RULE UNDER, NAMES... |
| R900 | **later** — §7 | "ALL FOUR ARE PUSHED (FP1), SO EACH HAS A CI RUN AVAILABLE" IS FALSE. TWO OF THE FOUR HAVE NO... |
| R901 | **later** — §7 | NEXT CARRIES TWO STACKED DOCSTRINGS AND THE SECOND IS A DEAD STRING LITERAL. claim the new... |
| R902 | **later** — §7 | THE GENERATOR NOW VALIDATES THE RECORDED WAVE HEIGHT AND THEN IGNORES IT. EVERY NUMBER THE... |
| R903 | **later** — §7 | THE REPAIR ROUTED THE FOUR WAVE_BASIS_KEYS AND LEFT FIVE RECORDED FIELDS AT THE SAME READER... |
| R904 | **later** — §7 | THE REPAIRED ASSERTION IS TWO SCALAR COMPARISONS WHERE THE CLOSING CONDITION SAID "EVERY COPY... |
| R905 | **later** — §7 | R895's REPAIR REPLACED ONE UNVERIFIABLE ABSENCE CLAIM IN floatfea/ WITH ANOTHER, AND ADDED TWO... |
| R906 | **later** — §7 | A RED TEST AT THE REVIEWED COMMIT THAT FAILS BOTH LIMBS OF THE PREDICATE. c071e68 DELETED... |
| R907 | **later** — §7 | THE R902 REPAIR REACHED THE COMPUTED TABLE AND LEFT THE PUBLISHED VERDICTS. AT A RECORDED... |
| R908 | **later** — §7 | THE REPAIR MADE sidecar.run.lambda THE FROUDE SCALE OF A PUBLISHED CSV, AND NOTHING COMPARES IT... |
| R909 | **later** — §7 | run.periods_full_s IS NOT MERELY PRINTED -- IT IS THE LOOP VARIABLE OF THE BAND TABLE. A... |
| R910 | **later** — §7 | THE R904 LOOP INSPECTS 16 OF THE 29 ACTIONS STATES CARRIES AND SKIPS 13 UNDER A SILENT else:... |
| R911 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R912 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R913 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R914 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R915 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R916 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R917 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R918 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R919 | **later** — §7 | THE R906 REPAIR PUT A PUBLISHED-DELIVERABLE GENERATOR ON AN AUTHORITY NOTHING CROSS-CHECKS AND... |
| R920 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R921 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R922 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R923 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R924 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R925 | **later** — §7 | THE FROUDE CONVERSION FACTORS ARE PUBLISHED AS lambda = 50 LITERALS INTO BOTH F4 DELIVERABLES,... |
| R926 | **later** — §7 | THE REPAIR ROUTED TWO OF THE THREE PUBLISHING READERS THROUGH THE VALIDATOR. THE THIRD --... |
| R927 | **later** — §7 | --provenance IS DECLARED AS "the authority for the scale and the height" AND THIS COMMIT TOOK... |
| R928 | **later** — §7 | The R909 orphan check compares a sidecar float against a float parsed back out of a... |
| R929 | **later** — §7 | R909's condition said "in both directions". set(_recorded) - _solved is computed; _solved -... |
| R930 | **later** — §7 | member_forces_table.py:166 says of the GOVERNING_PERIODS docstring that "no number for them is... |
| R931 | **later** — §7 | SENSITIVITY_PERIODS = (10.0, 20.0) at :180 is referenced by nothing -- grep -rn... |
| R932 | **later** — §7 | validated_export_scale raises ConfigError, and neither generator catches it, so an... |
| R933 | **later** — §7 | grep -rn "R907\\|R909" tests/ --include=.py is empty, and nothing in tests/ or .github/ invokes... |
| R934 | **later** — §7 | The two scripts/measure/ readers now REFUSE a disagreeing npz/sidecar pair; floatfea run -- the... |
| R935 | **later** — §7 | The five new cells import validated_export_scale function-locally, five times, rather than... |
| R936 | **later** — §7 | THE FA0 CLAUSE IS GATED ON A MEMBERSHIP PREDICATE, NOT ON THE SEA STATE FA0 RULED ON, SO... |
| R937 | **later** — §7 | THE R925 REPAIR PUBLISHES THE TWO CONVERSION FACTORS THROUGH :.0f, SO THE FACTOR IN BOTH F4... |
| R938 | **later** — §7 | f6_results_report.py NOW RESOLVES THE SCALE AND THE WAVE BASIS FROM --npz AND --provenance AND... |
| R939 | **later** — §7 | The new destination-only arm asserts the wrong directory for append_finding, and declares three... |
| R940 | **later** — §7 | The new gate's property (iii) is green on the tree R925 lived in, and no test anywhere asserts... |
| R941 | **later** — §7 | validated_export_scale's explicit-sidecar form inherits the default form's silent skip: the... |
| R942 | **later** — §7 | Two prose residues of the new two-branch form. The computed branch's "breaking ... <list>"... |
| R943 | **later** — §7 | results/F6/F4_member_forces.csv is a third copy of the SCALE line, byte-identical to... |
| R944 | **later** — §7 | THE R936 REPAIR PUBLISHES "T = 12.5 s IS INSIDE THE BAND AT THIS HEIGHT" AT EVERY RECORDED... |
| R945 | **later** — §7 | THE NEW JOIN IS A SUBSTRING TEST, SO A FORCES TABLE GENERATED AT lambda = 500 IS ACCEPTED AT... |
| R946 | **later** — §7 | test_R933_ANOTHER_SEA_STATE_RUNS_rather_than_refusing[f6_results_report.py] ASSERTS EXIT 0 FOR... |
| R947 | **later** — §7 | The published-factor format now has TWO definitions. f6_results_report.py:333-338 re-implements... |
| R948 | **later** — §7 | The node-id diff that could not see the eleventh id: the added id is in... |
| R949 | **later** — §7 | R918's shape, with a second witness: member_forces_table.py ends with... |
| R950 | **later** — §7 | THE R944 REPAIR REPLACED A ONE-SIDED TEST WITH A FOUR-WAY CATEGORY AND THEN READ THREE OF THE... |
| R951 | **later** — §7 | f6_results_report.py:636 STILL DECIDES "IS THIS THE REFERENCE SEA STATE?" WITH THE MEMBERSHIP... |
| R952 | **later** — §7 | THE NEW HEIGHT JOIN SKIPS WHEN THE HEADER CARRIES NO HEIGHT -- if _seen_h and ... -- SO R938... |
| R953 | **later** — §7 | The other boundary of the R944 else arm, solved because EH4 asks for both. Just above H =... |
| R954 | **later** — §7 | tests/regression/test_generators_refuse_mismatched_inputs.py:9-15 says "The cells are cheap... |
| R955 | **later** — §7 | member_forces_table.py:396-397 prints args.out.relative_to(ROOT) AFTER both files are written,... |
| R956 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R957 | **later** — §7 | THE R951 REPAIR DROPPED THE FOUR MEMBERSHIP CONJUNCTS AND KEYS ON HEIGHT ALONE, SO THE... |
| R958 | **later** — §7 | THE PERIOD JOIN IS ONE-DIRECTIONAL. set(_recorded) - _solved REFUSES A DECLARED PERIOD WITH NO... |
| R959 | **later** — §7 | , AND CA2: A RED CI IS A HOLD) CI IS RED AT THE REVIEWED COMMIT. ladder 6 -- it stays fixed... |
| R960 | **later** — §7 | scripts/measure/member_forces_table.py:458 says "The five other scripts/measure/ scripts still... |
| R961 | **later** — §7 | _shown is now defined twice, identically, at f6_results_report.py:240 and... |
| R962 | **later** — §7 | FA0 ruled at one sea state. The predicate now reads that height from a mutable input file... |
| R963 | **later** — §7 | R950's decision boundary is not bracketed by any cell. With params at 10.0 and 14.21 (the... |
| R964 | **later** — §7 | test_R951's claimed needle is asserted nowhere to be FOUND: grep -rn "The governing basis is... |
| R965 | **later** — §7 | The height-mismatch refusal interpolates a Python list: "the CSV's own caveats state H =... |
| R966 | **later** — §7 | One document, one height, two spellings: f6_results_report.py:551 writes H = {h_full} m and... |
| R967 | **later** — §7 | THE THIRD INPUT IS JOINED TO NOTHING. --util CARRIES EVERY UTILISATION THE REPORT PUBLISHES AND... |
| R968 | **later** — §7 | R957 IS NOT CLOSED. THE REFERENCE GATE IS A HEIGHT COMPARISON AND THE NEW JOIN DOES NOT... |
| R969 | **later** — §7 | THE JOIN COMPARES SETS WHERE THE DOCUMENT ITERATES A LIST. A DUPLICATE DECLARED PERIOD PASSES... |
| R970 | **later** — §7 | THE R959 CLASS IS CLOSED FOR CSVs AND OPEN FOR EVERY OTHER DELIVERABLE. IN A FRESH CHECKOUT AT... |
| R971 | **later** — §7 | R959's CONDITION (ii) IS UNMET AT THE SITE I NAMED, AND THE REPORT DOES NOT SAY THE SITE WAS... |
| R972 | **later** — §7 | test_R959's docstring says ".csv -text stores the bytes. This asserts the property directly." I... |
| R973 | **later** — §7 | OBSERVED LIVE, WITH A TRACEBACK) My first probe handed the generator a forces CSV with no... |
| R974 | **later** — §7 | git worktree list carries twelve AppData/Local/Temp/suite-count-/tree registrations, and git... |
| R975 | **later** — §7 | .gitattributes says "Every tracked CSV here is a generator artifact, so the rule is the file... |
| R976 | **later** — §7 | A DUPLICATED UTILISATION ROW PASSES BOTH NEW JOINS AND IS PUBLISHED TWICE. ONE VARIABLE MOVED... |
| R977 | **later** — §7 | R968 IS NOT CLOSED. THE NEW CONJUNCT READS ITS REFERENCE FROM THE SAME FILE --provenance... |
| R978 | **later** — §7 | THE UTIL JOIN COMPARES KEYS AND PERIODS AND NOT THE QUANTITY THE TWO TABLES SHARE. ONE VARIABLE... |
| R979 | **later** — §7 | THE DERIVATION MIRRORS TWO OF THE PRODUCER'S FOUR CONJUNCTS. IT IS AN OVER-REFUSAL AND NEVER A... |
| R980 | **later** — §7 | THE JOIN IS VACUOUS WHEN BOTH DERIVED SETS ARE EMPTY, AND THE ONLY THING THAT CATCHES IT IS THE... |
| R981 | **later** — §7 | R918 / R956's REPAIR REACHED TWO FILES AND THE CENSUS IS SEVEN SHORT. I HIT IT LIVE:... |
| R982 | **later** — §7 | THE NEW UTIL REFUSAL'S NARRATIVE HALF IS ONE-DIRECTIONAL. Driving the _util_extra branch prints... |
| R983 | **later** — §7 | STATIONS_CHECKED ARRIVES FROM floatfea.run.pipeline, WHICH DOES NOT WRITE THE FILE.... |
| R984 | **later** — §7 | THE JOIN KEYS DROP body. _util_expected, _util_got and _periods_for key on (member, station)... |
| R985 | **later** — §7 | _wrong_period COMPARES PERIODS AS STRINGS (r.get("period_full_s", "") against a set of strings)... |
| R986 | **later** — §7 | THREE OF THE SEVEN CLAIMS IN THE PARAGRAPH _reference GUARDS ARE ABOUT THE STRESS BOUND, WHICH... |
| R987 | **later** — §7 | THE RECORDED HEADING AND THE RECORDED PERIOD COUNT ARE PUBLISHED AS LITERALS AT FOUR SITES... |
| R988 | **later** — §7 | FOUR MORE LITERALS OF THE SAME CLASS ARE TRUE TODAY AND GO FALSE AT A NAMED NEXT ITEM. :713... |
| R989 | **later** — §7 | THE TURN'S SUITE FIGURE IS NOT A WHOLE-SUITE FIGURE: --ignore=tests/test_report_carried.py... |
| R990 | **later** — §7 | MY OWN STATE-(2) CONTROL DID NOT MEASURE WHAT I SAID IT MEASURED. docs/reviews/R1/step-3.md... |
| R991 | **later** — §7 | THE THREE BOUND SENTENCES ARE NOW INTERPOLATED, AND TWO OF THEIR CONCLUSIONS ARE STILL DECIDED... |
| R992 | **later** — §7 | THE NEW VALUE JOIN REACHES ALL 23 PUBLISHED UTILISATION COLUMNS AND DOES NOT REACH sigma_Pa,... |
| R993 | **later** — §7 | THE EH4 TABLE IN test_R978_a_CHANGE_BELOW_THE_PUBLISHED_PRECISION_is_accepted's DOCSTRING IS... |
| R994 | **later** — §7 | FOUR MORE LITERAL CLAIMS ABOUT THE RUN SIT OUTSIDE THE CENSUS'S STATED DOMAIN, AND TWO OF THEM... |
| R995 | **later** — §7 | git diff --stat HEAD~1 IS 816 insertions(+), 102 deletions(-), NOT 792. git diff --shortstat... |
| R996 | **later** — §7 | A NEGATIVE NEEDLE THAT EMBEDS A SPELLED COUNT IS VACUOUS AT ANY OTHER COUNT. assert "largest of... |
| R999 | **later** — §7 | THE DIFF MADE sigma_Pa AND tau_Pa ORPHAN COLUMNS OF A PUBLISHED DELIVERABLE, AND IT IS THE ONE... |
| R1000 | **later** — §7 | A RANK CLAUSE CAN PUBLISH TWO EQUAL FIGURES AS THE EVIDENCE FOR A STRICT ORDERING. At my states... |
| R1001 | **later** — §7 | TWO CITATIONS IN THE NEW R994 COMMENT RESOLVE ONE FRAME AND FIVE LINES OFF.... |
| R1002 | **later** — §7 | R993's RESIDUE: THE DOCSTRING STILL PUBLISHES THREE ROWS WHILE THE CELL RUNS ONE OF THEM. The... |
| R1003 | **later** — §7 | MY VERDICT 21 NAMED THE RIGHT REPAIR FOR R992 FOR THE WRONG REASON, AND THE WRONG REASON WAS... |
| R1005 | **later** — §7 | THE NPZ RECORDS EACH CASE'S PERIOD TWICE, NOTHING COMPARES THE TWO, AND FL2(d)'s SCREEN IS... |
| R1006 | **later** — §7 | and (d), FR1) TWO RED TESTS AT THE REVIEWED COMMIT THAT FAIL THE FS1/FT1 BOUNDARY PREDICATE, IN... |
| R1007 | **later** — §7 | A MALFORMED SIDECAR run BLOCK NOW SILENTLY DISABLES THE WHOLE FL2(d) SCREEN, AND I MEASURED THE... |
| R1008 | **later** — §7 | out_of_band_governing ADMITS A BREAKING WAVE WITH NO FURTHER DECLARATION, AND BREAKING HAS NO... |
| R1009 | **later** — §7 | THE EH4 BREAKING CELL ASSERTS THE LABEL WHERE THE LOAD-BEARING PROPERTY IS THE DECISION.... |
| R1010 | **later** — §7 | TEN LIVE COPIES OF THE BAND AND STEEPNESS COEFFICIENTS REMAIN IN THE TWO EZ0 GENERATOR SCRIPTS... |
| R1011 | **later** — §7 | _recorded_height's DOCSTRING STATES A FALSE CALL GRAPH AS THE REASON FOR ITS ASYMMETRY WITH... |
| R1012 | **later** — §7 | refuse_cases_that_cannot_govern SILENTLY SKIPS A DECLARED PERIOD THAT IS NOT IN THE FILE. Both... |
| R1013 | **later** — §7 | FOUR STALE LINE CITATIONS IN THE LIVE TREE; THE CENSUS IS IN ANSWER (5c) ABOVE AND YOUR LIST OF... |
| R1014 | **later** — §7 | THE FU0 EXEMPTION'S REVERSE GUARD PASSES ON A PARTIAL REPAIR. Three arms in answer (4) above.... |
| R1015 | **later** — §7 | THE H = 0 REFUSAL IS RIGHT AND ITS MESSAGE IS ODD, AND CALM WATER CAN SET AN ENVELOPE IF... |
| R1016 | **later** — §7 | A NEGATIVE CONTROL THAT DIES IN next().... |
| R1017 | **later** — §7 | NO CI JOB RUNS tests/regression/, SO FL2(d)'s END-TO-END GATE HAS NO INDEPENDENT WITNESS.... |
| R1018 | **later** — §7 | THE NEW test_one_gravity.py RELOADS A LIBRARY MODULE AND POISONS IT FOR THE REST OF THE... |
| R1021 | **later** — §7 | R1005 REPAIR IS EVADED BY DELETING THE SECOND RECORD AT EXACTLY THE INDICES THAT DISAGREE,... |
| R1022 | **later** — §7 | R1019 DOMAIN CHECK REACHES ONE OF THE THREE READERS OF periods_full_s, AND THE TWO IT MISSES... |
| R1023 | **later** — §7 | R1017 IS FALSE: tests/regression/ RUNS ON EVERY PUSH, IN THE ladder JOB. The entry I routed to... |
| R1024 | **later** — §7 | THE R1018 FOUR-ARM TABLE IN THE COMMIT MESSAGE IS STALE BY THE TWO CELLS THE SAME COMMIT ADDED.... |
| R1025 | **later** — §7 | R1010 REPAIR IS HOLDABLE BY A TEST, MEASURED, SO "A NO-OP SUBSTITUTION CANNOT BE DETECTED" IS... |
| R1026 | **later** — §7 | FIVE PUBLISHED LITERALS OF THE BAND AND STEEPNESS CONSTANTS SURVIVE R1010 SWEEP, AND ONE OF... |
| R1027 | **later** — §7 | floatfea/basis.py:89 SAYS period_band.py IS "THE ONLY CONSUMER OF THESE THREE CONSTANTS", AND... |
| R1028 | **later** — §7 | TWO OBSERVATIONS ON R1019 PLACEMENT, BOTH ABOUT WHERE RATHER THAN WHETHER. (i) The refusal sits... |
| R1029 | **later** — §7 | THE DEFECT ARM 06 FOUND IN THE NEW REFUSAL IS STILL STANDING IN THE OLD ONE, WHICH IS THE... |
| R1030 | **later** — §7 | THE # not-a-tolerance: MARKER IS AN UNCONDITIONAL, FREE-TEXT SILENCER ON THE COMPARISON OWN... |
| R1031 | **later** — §7 | tests/unit IS A PUSH PATH, AND THE STEP IT RUNS IN GREW BY 149 SECONDS AT THIS COMMIT. The CI... |
| R1032 | **later** — §7 | THE GUARD THAT READS WHICH FINDINGS A VERDICT MARKS AS BLOCKING CANNOT TELL "BLOCKS" FROM "DOES... |
| R1033 | **later** — §7 | THE TYPE GATE THIS COMMIT ADDED FOR THAT FAMILY LISTS THE PYTHON TYPES A JSON SIDECAR CAN... |
| R1034 | **later** — §7 | THE mass_eps CONCLUSION IS RIGHT AND NEITHER REASON GIVEN FOR IT IS WHAT HOLDS IT. The turn's... |
| R1035 | **later** — §7 | THE EMPTY-SEQUENCE ALLOWANCE IS SAFE AND ITS STATED REASON NAMES A CHECK THAT NEVER RUNS ON IT.... |
| R1036 | **later** — §7 | THE DOOR'S DOCSTRING MEASURES THE MODEL-SCALE CASE AT ONE OF ITS THREE CALLERS. I WENT TO SHOW... |
| R1037 | **later** — §7 | THE NEW REFUSAL'S REMEDY SENTENCE WILL BE WRONG FOR THE FILES THIS STEP'S OWN GATE PRODUCES.... |
| R1038 | **later** — §7 | THE DUPLICATED not-a-tolerance: BLOCK. tests/unit/test_forces_table_reexports.py carries the... |
| R1039 | **later** — §7 | R899's COUNT IS WRONG IN ONE DIRECTION AND THE DRIFT IS REAL IN THE OTHER. Verdict 24 reported... |
| R1040 | **later** — §7 | THERE IS A THIRD RECORD OF THE SAME QUANTITY AND NOTHING COMPARES IT. The sidecar's run block... |
| R1042 | **later** — §7 | THE SAME DEFECT AT A FOURTH SITE, IN THE SAME FUNCTION AS THE THIRD, FOUR LINES BELOW THE... |
| R1043 | **later** — §7 | with CA2: a red test and a red CI at the reviewed commit, failing BOTH limbs of the FS1/FT1... |
| R1044 | **later** — §7 | of my own amended R1033 condition, and it was neither met nor stated as left) THE MEMBERSHIP IS... |
| R1045 | **later** — §7 | THE DOCSTRING THAT TELLS A READER WHICH BRANCH IS LIVE IS FALSE IN ITS FIRST CLAUSE.... |
| R1046 | **later** — §7 | A SHAPE-(2,) froude_lambda IS REFUSED WITH "the npz could not be read". Driven: np.array([50.0,... |
| R1047 | **later** — §7 | THE PRE-COMMIT SELECTION RULE WAS "WHAT DID I EDIT" AND IT HAS TO BE "WHAT EXERCISES WHAT I... |
| R1048 | **later** — §7 | A WAITER ANCHORED ON [0-9]+ failed, FIRED ON AN INNER SYNTHETIC RUN'S SUMMARY AT 52%. They... |
| R1049 | **later** — §7 | scripts/write_verdict.py STAMPS HEAD, AND HEAD IS NOT THE JUDGED COMMIT WHEN THE IMPLEMENTER... |
| R1050 | **later** — §7 | THE TRACKED FILE THAT REVERTED AT 17:36 WAS ME, NOT A SYNC. The implementer measured a tracked... |
| R1051 | **later** — §7 | THE JOINT-REACTION ARRAY'S DTYPE IS CHECKED NOWHERE. A BOOL-TYPED case{i}/lam IS ACCEPTED,... |
| R1052 | **later** — §7 | THE TWO SCALE READERS RAISE AN UNCAUGHT AttributeError OR OverflowError ON SIX SIDECAR SHAPES... |
| R1053 | **later** — §7 | THE COMMIT MESSAGE'S OWN git diff --name-only OUTPUT NAMES TWO FILES WHERE THE DIFF IS THREE.... |
| R1054 | **later** — §7 | floatfea/run/config.py SAYS "every one of numpy's twenty-two dtype KINDS is a single non-empty... |
| R1055 | **later** — §7 | THE COMPLEMENT NAMES 17 EXCLUDED ROOT FILES AS "the remaining root-level report guards". AT... |
| R1056 | **later** — §7 | THE R1044 REPAIR IS CORRECT AND HELD BY NOTHING. Restoring kind in "iuf" in place of the tuple... |
| R1057 | **later** — §7 | A NEW PARAMETER'S OWN LABEL DESCRIBES A DIFFERENT VALUE. In the R1042 cell: pytest.param("JSON... |
| R1058 | **later** — §7 | A NON-FINITE case{i}/lam IS ACCEPTED, SOLVED AND PUBLISHED. THE GOVERNING CASE SET TO NaN GIVES... |
| R1059 | **later** — §7 | THE ADMITTED SET IS float16, float32 AND float64, AND THE DOCSTRING'S OWN REASON -- TRUNCATION... |
| R1060 | **later** — §7 | THE INSTINCT WAS RIGHT, THE CONCLUSION IS RIGHT, AND THE RUN YOU PASTED DID NOT REACH THE CODE... |
| R1061 | **later** — §7 | FOUR MEASUREMENTS ARE PUBLISHED IN A floatfea/ DOCSTRING AND IN A USER-FACING REFUSAL, AND... |
| R1062 | **later** — §7 | THE REFUSAL DOES NOT NAME THE FILE, AND THIS STEP'S OWN GATE PUTS SEVERAL FILES IN ONE RUN.... |
| R1063 | **later** — §7 | A case{i}/lam WITH ZERO TIMESTEPS IS ACCEPTED, SOLVED AND PUBLISHED. THE GOVERNING CASE EMPTIED... |
| R1064 | **later** — §7 | THE TREE FINGERPRINT CARRIES NO COMMAND AND THIRTEEN RECIPES DO NOT REPRODUCE IT.... |
| R1065 | **later** — §7 | test_the_SEARCH_reads_no_gravity_at_all IS FUNCTION-LOCAL AND CANNOT SEE A HELPER A SEARCH... |
| R1066 | **later** — §7 | A BIG-ENDIAN >f8 lam IS REFUSED WITH A MESSAGE THAT BLAMES THE WIDTH, WHICH IS NOT WHAT IS... |
| R1067 | **later** — §7 | "candidate {index} of {count}" MIXES A ZERO-BASED INDEX WITH A ONE-BASED COUNT, IN A... |
| R1068 | **later** — §7 | THE R1060 INCIDENTAL IS AT A SECOND SITE. scripts/measure/f6a_required_section.py:585 and... |
| R1069 | **later** — §7 | THE DIAGONAL FORCE AND THE DIAGONAL'S BUCKLING LENGTH ARE BOTH BUILT FROM panel_and_diagonal's... |
| R1070 | **later** — §7 | R1063 SURVIVES ONE MORE KEY EDIT. NOTHING BOUNDS EITHER WINDOW LENGTH BELOW, SO EMPTYING lam... |
| R1071 | **later** — §7 | sections.truss.d_over_t AND joint_allowance ACCEPT A BOOL AND A STRING, IN A FUNCTION THAT... |
| R1072 | **later** — §7 | THE TRIANGLE'S FACE-SHEAR ALLOCATION DOES NOT CLOSE AGAINST Vz OR T, THE BOX'S CLOSES EXACTLY,... |
| R1073 | **later** — §7 | THE REWRITTEN BULLET PUBLISHES THE FORCE FACTOR AS THE AREA FACTOR, AND THE AREA FACTOR IS... |
| R1074 | **later** — §7 | THE GENERATOR HARD-CODES FOUR FIGURES ABOUT THIS DECK AND THIS GRID INTO AN ARTIFACT IT WRITES... |
| R1075 | **later** — §7 | THE NEW PARAGRAPH PUBLISHES "A ROW WITH A LARGE TORSION PUTS uniform_panel AHEAD FOR BOTH... |
| R1076 | **later** — §7 | THE AREA-FACTOR TABLE IS A FOUR-ROW SAMPLE AT ONE UNSTATED LOAD AND ONE UNSTATED READING OF A... |
| R1077 | **later** — §7 | THE R1075 REPAIR PUT FOUR NEW DECK-SPECIFIC LITERALS, INCLUDING THE WORDS "ON THIS DECK", INTO... |
| R1078 | **later** — §7 | THE COMPUTED FIGURE THAT REPLACED R1074 HARD-CODED ONE IS COUNTED OVER A DOMAIN THAT CANNOT... |
| R1079 | **later** — §7 | THE SENTENCE THAT REPLACED THE RETRACTED "NONE OF IT IS THE BRACED LENGTH" PUBLISHES A BOUND --... |
| R1080 | **later** — §7 | THE BULLET THAT TELLS A READER WHETHER THE KNOWN DEFECT REACHES A PUBLISHED NUMBER CONDITIONS... |
| R1081 | **later** — §7 | THE R1077 REPAIR DELETED THE DECK-SPECIFIC LITERALS AND ALSO DELETED THE QUALIFIER THAT MADE... |
| R1082 | **later** — §7 | _margin NEW LABEL IS FALSE AT AN ADMISSIBLE GRID SHAPE: AT depths: [3.0, 3.0] THE ARTIFACT... |
| R1083 | **later** — §7 | NOTHING IN THE TREE HOLDS L43's REPAIR, AND THE COMMIT MESSAGE'S ARM FIGURE FOR IT DOES NOT... |
| R1084 | **later** — §7 | EXACT IS THE RIGHT WORD AND I PROVED THE HALF YOU COULD NOT -- BUT THE SAME CLAUSE RE-OPENS... |
| R1085 | **later** — §7 | L46's TRAILING CAUSE IS A FOURTH COMMA-ITEM IN A LIST IT IS TRUE OF ONLY ONE MEMBER OF, SO AT A... |
| R1086 | **later** — §7 | THE TEST COMMENT SAYS THE RETIRED WORDING IS forbidden. NOTHING FORBIDS IT, AND NOTHING CAN,... |
| R1087 | **later** — §7 | THE NEW ASSERTIONS READ A FIFTH FIELD FROM A FIXTURE WHOSE DOCSTRING SAYS IT CARRIES FOUR, AND... |
| R1088 | **later** — §7 | no triangle figure in these tables is ever HIGH IS FALSE UNDER ONE OF THE THREE CORRECTIONS THE... |
| R1089 | **later** — §7 | R1085's REPAIR INTRODUCES A THIRD AGREEMENT PAIR INTO THAT ONE SENTENCE AND ONLY THE SINGULAR... |
| R1090 | **later** — §7 | R1086 IS CLOSED AT A SITE MY CONDITION DID NOT NAME AND OPEN AT THE ONE IT DID.... |
| R1091 | **later** — §7 | YOUR QUALIFIER IS TRUE -- WIDER THAN YOU VERIFIED IT -- AND THE ENUMERATION BEHIND IT IS... |
| R1092 | **later** — §7 | : 1890 cells, 139 identical, 154 MISMATCHES cmd which reading, and how much out all 154 are... |
| R1093 | **later** — §7 | report.md PUBLISHES THE FIRST FILE'S WAVE BASIS AS "THE WAVE BASIS THESE LOADS WERE EXPORTED... |
| R1094 | **later** — §7 | THE FL2(d) SECTION STATES ONE FILE'S ASSOCIATED-PERIOD BAND AS THE BAND, OVER A TABLE... |
| R1095 | **later** — §7 | A MIXED SET -- ONE FILE THAT RECORDS A HEIGHT AND ONE THAT DOES NOT -- PUBLISHES A... |
| R1096 | **later** — §7 | Checked stations: 64. Over unity: 16. ON A MODEL WITH 32 STATIONS, 12 OF THEM OVER UNITY. THE... |
| R1097 | **later** — §7 | _governing_provenance's DOCSTRING STILL DESCRIBES THE IMPLEMENTATION THE REPAIR DELETED, AND... |
| R1098 | **later** — §7 | "THE FIELDNAMES ARE STATED EXPLICITLY RATHER THAN INFERRED FROM THE RECORD" IS FALSE, AND I... |
| R1099 | **later** — §7 | YOUR READING OF FW1's SCOPE IS RIGHT. THE CONSEQUENCE IS THAT utilisation.csv NOW CARRIES 32... |
| R1100 | **later** — §7 | THE ONE-FILE AND MULTI-FILE HEADING COMPARISONS ARE DIFFERENT FUNCTIONS WITH DIFFERENT... |
| R1101 | **later** — §7 | A REFUSAL THIS COMMIT ADDS HAS AN AGREEMENT PAIR WITH NO SINGULAR BRANCH, AND NOTHING ASSERTS... |
| R1102 | **later** — §7 | Row.source AND Row.heading_deg CARRY DEFAULTS, SO MY "APPEND WITH NO DEFAULT" CONSTRAINT BOUGHT... |
| R1103 | **later** — §7 | TWO OF THE THREE ARTIFACTS' SHARED CAVEATS ARE SINGULAR PROSE ABOUT A PLURAL RUN, AND ONE OF... |
| R1104 | **later** — §7 | TWO DIFFERENT DECLARED FILES WHOSE BASENAMES COLLIDE ARE ACCEPTED AT EXIT 0, AND EVERY ARTIFACT... |
| R1105 | **later** — §7 | WHAT CANCELLED THE RUN IS A PUSH FROM YOUR SIDE, AND THE MECHANISM WILL DO IT EVERY TIME.... |
| R1106 | **carried** — §7 | . The FY3 supersession reached ONE of three sibling artifacts. 84 of 168 rows in a published... |
| R1107 | **carried** — §7 | . The hook narrowing moved FOUR WRITE rows from DENY to ALLOW, and >\| is the one that matters.... |
| R1108 | **carried** — §7 | . The rung-3 class guard transfers a CLASS label to an entry that did not declare it. Your... |
| R1109 | **later** — §7 | . The coincidence rule's TABLE 1 reproduces exactly. BOTH of TABLE 2's published margin figures... |
| R1110 | **later** — §7 | . The plan declares NODE_COINCIDENCE_DECIMALS STRUCTURAL; the file deliberately declares no... |
| R1111 | **later** — §7 | . wave_basis_from_sidecar is a third door and it CANNOT reconcile. Your two doors are right;... |
| R1112 | **later** — §7 | . A multi-element froude_lambda makes _npz_scale_key return None, which SKIPS the... |
| R1113 | **later** — §7 | . The third wrong-exception-class site, which you asked me to assume exists. It does, and... |
| R1114 | **later** — §7 | . exported_wave_basis gates on is_file() and wave_basis_from_sidecar on exists(), so R1007's... |
| R1115 | **later** — §7 | . A published supersession note points at a document that does not exist.... |
| R1116 | **later** — §7 | . The new != is exact in the strict direction, as you claim. The weakening direction has one... |
| R1117 | **carried** — §7 | . I removed my own worktree while a measurement was still running in it, and 33 reds are the... |
| R1119 | **carried** — §7 | . scripts/ci_section.py cannot see a failing test whose id contains a space, so the generated... |
| R1120 | **carried** — §7 | . R1118's repair reached four of the six sites. The two it missed require a dot the verdicts do... |
| R1121 | **carried** — §7 | . FT2.5's condition 4 -- the one sentence of disclosure for Xabier -- is absent at the first... |
| R1122 | **later** — §7 | . R1115 has MOVED, and the move is in the wrong direction. One of the two destinations the... |
| R1123 | **later** — §7 | . The over-refusal the hook repair costs is bigger than the one row you measured -- 5 of 10... |
| R1124 | **carried** — §7 | . Nine of the eleven carried L ledger ids are named nowhere in the report, and the cause is... |
| R1125 | **later** — §7 | . Two triples whose out field is not what the cmd printed. claim section 1's triple shows two... |
| R1128 | **later** — §7 | . _SITE admits only py\|md\|sh\|txt\|json, so no site named in a .csv, .yml, .yaml, .npz, .toml or... |
| R1129 | **later** — §7 | . The answered_table half of R1120's repair made the dot optional on BOTH sides, which widened... |
| R1130 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1131 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1132 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1133 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1134 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1135 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1136 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1137 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1139 | **answered** — §2 | . The site pattern cannot match a STEMLESS DOTFILE at all, whatever the extension class, so... |
| R1140 | **later** — §7 | . YOUR FIRST ASK, ANSWERED WITH THE ENUMERATED SET AND A COMMITTED ARM. Five planted heading... |
| R1141 | **answered** — §3 | . R1135 is recorded CLOSED in three places and is not closed: the sentence it was to replace is... |
| R1142 | **later** — §7 | . R1132's repair publishes two wrong out fields, and one of them is the same defect R1132 was.... |
| R1143 | **later** — §7 | . Section 2's four site counts are stale by exactly the R1138 repair that landed in the same... |
| R1144 | **later** — §7 | . The site gate's declaration lookup is keyed on the PATH and not on the finding, so one no... |
| R1145 | **later** — §7 | carried, and the verdict says nothing further about it here |
| R1146 | **later** — §7 | carried, and the verdict says nothing further about it here |

## 8b. Every site verdict 47 names that this diff does not touch

**2228 rows, generated.** The set is read from `tests/test_report_carried.py`'s own `SITES` and `TOUCHED`, so the table cannot enumerate a different set than the check does.

**THE HEADING IS NOT UNIVERSAL BY ACCIDENT ANY MORE.** R1139 was that section 8b of the previous revision published 2167 rows under exactly this heading where the complete set was 2170, because a path form could not enter `SITES` at all. The repair in section 2 is what makes the heading true, and the row count below is the generator's at this commit rather than a carried figure.

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R1001 | `f6_results_report.py:718` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:793` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:794` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:795` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:796` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:797` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:798` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:799` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:800` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:801` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:802` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:803` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:804` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:805` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1001 | `floatfea/run/pipeline.py:806` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1003 | `docs/reports/R1/step-3-answers.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1003 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1003 | `test_r1_example_golden.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1003 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `pipeline.py:1239` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `pipeline.py:1252` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `pipeline.py:1262` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `post/forces_table.py:463` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `results/R1/example/utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1005 | `scripts/export_f4_dynamic_inputs.py:419` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `test_one_gravity.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `test_one_gravity.py:128` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `test_period_band.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `tests/regression/test_r1_example_golden.py:385` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `tests/regression/test_r1_example_golden.py:386` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `tests/regression/test_r1_example_golden.py:387` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `tests/regression/test_r1_example_golden.py:388` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `tests/test_no_tolerance_literals.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `tests/unit/test_period_band.py:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1006 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1007 | `pipeline.py:893` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1007 | `pipeline.py:894` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1007 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1008 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1009 | `tests/unit/test_period_band.py:151` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1010 | `basis.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1010 | `f6_results_report.py:970` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1010 | `member_forces_table.py:209` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1010 | `member_forces_table.py:681` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1010 | `period_band.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1011 | `pipeline.py:772` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1011 | `pipeline.py:773` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1011 | `pipeline.py:774` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1011 | `pipeline.py:1194` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:793` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:794` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:795` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:796` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:797` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:798` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:799` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:800` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:801` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:802` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:803` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:804` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:805` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1013 | `pipeline.py:806` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1017 | `.github/workflows/ci.yml:403` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1017 | `docs/milestones/F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1017 | `tests/regression/test_fl2d_band_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1018 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1018 | `test_one_gravity.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1018 | `test_period_band.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1018 | `tests/test_one_gravity.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1018 | `tests/test_one_gravity.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1018 | `tests/unit/test_period_band.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1021 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1021 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1021 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1021 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `floatfea/run/pipeline.py:1407` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `member_forces_table.py:330` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `pipeline.py:1407` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `scripts/f4_dynamic_residual.py:193` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1022 | `scripts/measure/f6_results_report.py:565` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `ci.yml:510` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `docs/milestones/F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `leg/regression.xml` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `scripts/run_rung.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `tests/regression/test_fl2d_band_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `tests/test_ci_runs_the_whole_suite.py:56` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1023 | `tests/test_tree_prose_consistent.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1024 | `test_period_band.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1025 | `tests/unit/test_forces_table_reexports.py:91` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1026 | `docs/F4_member_forces.md:57` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1026 | `f6_results_report.py:743` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1026 | `floatfea/cli.py:292` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1026 | `member_forces_table.py:220` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1026 | `results/R1/example/report.md:30` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1026 | `scripts/measure/member_forces_table.py:671` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1027 | `floatfea/basis.py:89` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1027 | `floatfea/cli.py:23` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1027 | `period_band.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1028 | `config.py:211` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1030 | `tests/test_no_tolerance_literals.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1031 | `ci.yml:133` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1031 | `ci.yml:338` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1032 | `tests/test_report_carried.py:358` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1032 | `tests/test_report_carried.py:359` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1032 | `tests/test_report_carried.py:360` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1032 | `tests/test_report_carried.py:361` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1032 | `tests/test_report_carried.py:362` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1032 | `tests/test_report_carried.py:363` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1032 | `tests/test_report_carried.py:364` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `f6_results_report.py:577` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `floatfea/run/config.py:295` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `floatfea/run/pipeline.py:1360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `member_forces_table.py:365` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `scripts/export_f4_dynamic_inputs.py:419` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1033 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1034 | `tests/verification/rung4/test_f4_g41_dynamic.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1034 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1035 | `config.py:1072` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1035 | `dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1035 | `tests/unit/test_run_config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1036 | `docs/F6_utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1037 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1037 | `scripts/export_f4_dynamic_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1038 | `tests/unit/test_forces_table_reexports.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1039 | `.claude/agents/gating-supervisor.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1039 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1039 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:699` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:700` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:701` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:702` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:703` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:704` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:705` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:706` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:707` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1259` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1260` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1261` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1262` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1263` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1264` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1265` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1266` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1267` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1268` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1269` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1270` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1271` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1272` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1273` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1274` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1275` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1276` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1277` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1278` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1279` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1280` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1281` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1282` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1283` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1284` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1285` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1286` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1287` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1288` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1289` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1290` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1291` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1292` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1293` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1294` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1295` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1296` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1297` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1298` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1299` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1300` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1301` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `floatfea/run/pipeline.py:1302` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `scripts/measure/f6_results_report.py:458` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `scripts/measure/f6a_premise_check.py:189` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `scripts/measure/member_forces_table.py:334` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1042 | `tests/regression/test_r1_example_golden.py:401` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1043 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1043 | `floatfea/run/config.py:295` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1043 | `floatfea/run/pipeline.py:1360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1043 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1043 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1043 | `tests/verification/rung4/test_f4_g41_dynamic.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1044 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1044 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1045 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1047 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1047 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1049 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1049 | `scripts/ci_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1049 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1050 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `docs/load-interchange-v1.md:110` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `floatfea/post/forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `floatfea/post/forces_table.py:123` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `floatfea/post/forces_table.py:464` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `forces_table.py:448` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `forces_table.py:464` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `pipeline.py:1288` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `pipeline.py:1425` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `pipeline.py:1564` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `scripts/export_f4_dynamic_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `scripts/measure/f6a_premise_check.py:208` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `scripts/measure/member_forces_table.py:406` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1051 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1052 | `scripts/measure/f6a_premise_check.py:189` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1053 | `config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1053 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1053 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1053 | `tests/unit/test_headings_and_bem_coverage.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1054 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1055 | `test_figure_local_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1055 | `test_marker_exemption_corpus.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1055 | `test_precommit_stale.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1055 | `test_supervisor_conftest_pathspec.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `docs/load-interchange-v1.md:110` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `floatfea/io/reader.py:68` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `floatfea/io/reader.py:345` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `floatfea/post/forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `floatfea/post/forces_table.py:582` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `floatfea/run/pipeline.py:967` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `floatfea/run/pipeline.py:1525` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `reader.py:378` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `scripts/export_f4_dynamic_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `scripts/export_f4_dynamic_inputs.py:476` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1058 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1059 | `docs/load-interchange-v1.md:110` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1059 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1060 | `premise_check.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1060 | `scripts/measure/f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1060 | `tests/regression/test_generators_refuse_mismatched_inputs.py:19` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1061 | `floatfea/post/forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1061 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1062 | `floatfea/run/pipeline.py:1196` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `docs/load-interchange-v1.md:110` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:88` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:89` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:90` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:91` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:92` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:93` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:94` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:582` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/post/forces_table.py:613` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `forces_table.py:88` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `forces_table.py:89` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `forces_table.py:90` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `forces_table.py:91` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `forces_table.py:92` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `forces_table.py:93` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `forces_table.py:94` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `scripts/export_f4_dynamic_inputs.py:233` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `scripts/export_f4_dynamic_inputs.py:234` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `test_fl2d_band_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `test_ft24_required_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1063 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1064 | `premise_check.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1065 | `scripts/measure/f6a_required_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1066 | `scripts/export_f4_dynamic_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1067 | `required_section.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1067 | `scripts/export_f4_dynamic_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1068 | `f6a_premise_check.py:365` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1068 | `scripts/measure/f6a_report.py:411` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1068 | `scripts/measure/f6a_required_section.py:585` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `floatfea/run/truss.py:425` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `floatfea/run/truss.py:426` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `floatfea/run/truss.py:427` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `floatfea/run/truss.py:428` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `floatfea/run/truss.py:429` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `floatfea/run/truss.py:430` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `scripts/measure/f6b_truss_sizing.py:402` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `scripts/measure/f6b_truss_sizing.py:403` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `scripts/measure/f6b_truss_sizing.py:404` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `test_ft25_truss_sizing.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1069 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1070 | `floatfea/post/forces_table.py:303` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1070 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1070 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1070 | `scripts/export_f4_dynamic_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1070 | `scripts/export_f4_dynamic_inputs.py:233` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1070 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1071 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1071 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `docs/milestones/F6b.md:32` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:613` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:614` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:615` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:616` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:617` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:618` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:619` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:620` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:621` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:631` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:632` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:633` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:634` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:635` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/cli.py:636` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/run/truss.py:169` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/run/truss.py:170` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/run/truss.py:171` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/run/truss.py:172` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `floatfea/run/truss.py:432` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `results/F6b/truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `scripts/measure/f6b_truss_sizing.py:155` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `scripts/measure/f6b_truss_sizing.py:156` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `scripts/measure/f6b_truss_sizing.py:157` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `scripts/measure/f6b_truss_sizing.py:158` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `scripts/measure/f6b_truss_sizing.py:159` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `scripts/measure/f6b_truss_sizing.py:160` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `scripts/measure/f6b_truss_sizing.py:161` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `tests/regression/test_ft25_truss_sizing.py:497` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1072 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:653` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:654` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:655` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:656` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:657` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:658` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:659` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:660` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:661` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:662` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:663` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:664` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:665` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `floatfea/cli.py:666` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1073 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `examples/platform12_placeholder.yaml:104` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `examples/platform12_placeholder.yaml:105` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:526` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:527` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:528` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:529` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:627` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:628` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:629` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:630` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:631` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:632` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1074 | `floatfea/cli.py:633` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1075 | `floatfea/cli.py:630` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1075 | `floatfea/cli.py:631` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1075 | `floatfea/cli.py:632` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1075 | `floatfea/cli.py:633` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1075 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:691` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:692` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:693` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:694` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:695` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:696` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:697` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:698` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:699` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:700` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:701` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:702` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:703` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:704` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:705` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:706` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:707` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `floatfea/cli.py:708` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1076 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:627` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:628` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:629` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:630` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:631` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:632` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:633` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:655` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:656` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:657` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:658` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:659` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:660` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:661` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:662` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `floatfea/cli.py:663` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1077 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `f6b_truss_sizing.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:523` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:524` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:525` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:526` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:527` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:528` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:529` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:530` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:531` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:532` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:533` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:534` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:535` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:536` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:537` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:538` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `floatfea/cli.py:539` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `sizing.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `test_r1_example_regenerates.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `truss.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1078 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `floatfea/cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `floatfea/cli.py:709` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `floatfea/cli.py:710` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `floatfea/cli.py:711` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `floatfea/cli.py:712` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `floatfea/cli.py:713` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `floatfea/cli.py:714` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1079 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `floatfea/cli.py:747` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `floatfea/cli.py:748` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `floatfea/cli.py:749` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `floatfea/cli.py:750` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `floatfea/cli.py:751` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `floatfea/cli.py:752` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `floatfea/run/truss.py:457` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1080 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1081 | `floatfea/cli.py:680` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1081 | `floatfea/cli.py:681` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1081 | `floatfea/cli.py:682` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1081 | `floatfea/cli.py:683` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1081 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:572` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:573` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:574` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:575` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:576` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:577` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:578` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:579` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:580` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:581` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:582` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/cli.py:583` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `step-1-answers.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `step-2-answers.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `truss.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1082 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `docs/milestones/R1.md:374` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `docs/milestones/R1.md:375` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `floatfea/cli.py:710` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `floatfea/cli.py:711` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `floatfea/cli.py:712` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `floatfea/cli.py:713` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `floatfea/cli.py:714` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `test_ft24_required_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `test_ft25_truss_sizing.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `test_tree_prose_consistent.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1083 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1084 | `floatfea/cli.py:805` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1084 | `floatfea/cli.py:806` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1084 | `floatfea/cli.py:807` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1084 | `floatfea/cli.py:808` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1085 | `floatfea/cli.py:552` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1085 | `floatfea/cli.py:553` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1085 | `floatfea/cli.py:554` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1085 | `floatfea/cli.py:555` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1085 | `floatfea/cli.py:556` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1086 | `tests/regression/test_ft25_truss_sizing.py:1079` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1086 | `tests/regression/test_ft25_truss_sizing.py:1080` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1086 | `tests/regression/test_ft25_truss_sizing.py:1081` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `floatfea/run/truss.py:210` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `floatfea/run/truss.py:211` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `floatfea/run/truss.py:212` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:885` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:886` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:887` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:888` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:889` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:890` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:891` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:892` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:893` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:894` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:895` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:896` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:897` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:898` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:899` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:900` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:901` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:902` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1087 | `tests/regression/test_ft25_truss_sizing.py:903` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1088 | `floatfea/cli.py:804` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1088 | `floatfea/cli.py:805` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `floatfea/cli.py:557` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `floatfea/cli.py:558` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `floatfea/cli.py:559` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `floatfea/cli.py:560` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1011` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1012` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1013` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1014` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1015` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1016` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1017` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1018` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1019` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1020` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1089 | `tests/regression/test_ft25_truss_sizing.py:1021` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1090 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1090 | `tests/regression/test_ft25_truss_sizing.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1090 | `tests/regression/test_ft25_truss_sizing.py:1099` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1090 | `tests/regression/test_ft25_truss_sizing.py:1100` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1090 | `tests/regression/test_ft25_truss_sizing.py:1101` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:810` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:811` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:812` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:813` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:814` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:815` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:816` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:817` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1091 | `floatfea/cli.py:818` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1092 | `floatfea/cli.py:813` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1092 | `floatfea/cli.py:814` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1092 | `floatfea/cli.py:815` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1092 | `floatfea/cli.py:816` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:333` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:334` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:335` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:336` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:337` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:338` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:339` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:340` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:341` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:342` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:343` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:344` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:345` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `floatfea/cli.py:346` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `pipeline.py:1791` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1093 | `results/R1/example/report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:358` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:359` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:361` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:362` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:363` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:364` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:365` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:366` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:367` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:368` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:369` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:370` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:371` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/cli.py:372` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1094 | `floatfea/run/pipeline.py:1694` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:350` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:351` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:352` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:353` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:354` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:355` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:356` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `floatfea/cli.py:357` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:707` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:708` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:709` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:710` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:711` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:712` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:713` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:714` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:715` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:716` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:717` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:718` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:719` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1255` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1256` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1257` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1258` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1259` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1260` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1261` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1262` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1095 | `pipeline.py:1263` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1096 | `floatfea/cli.py:417` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1096 | `floatfea/cli.py:418` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1096 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1096 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1097 | `floatfea/cli.py:294` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1097 | `floatfea/cli.py:295` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1097 | `floatfea/cli.py:296` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:262` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:263` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:264` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:265` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:266` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:267` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:268` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:269` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:270` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `floatfea/cli.py:271` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1098 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1099 | `floatfea/cli.py:268` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1099 | `floatfea/cli.py:269` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1099 | `floatfea/cli.py:270` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1099 | `floatfea/cli.py:271` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1099 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1099 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `config.py:194` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:698` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:699` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:700` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:701` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:702` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:703` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:704` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:705` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:706` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:707` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1100 | `floatfea/run/pipeline.py:708` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1101 | `floatfea/run/pipeline.py:690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1101 | `floatfea/run/pipeline.py:691` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1101 | `floatfea/run/pipeline.py:692` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1101 | `floatfea/run/pipeline.py:693` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1101 | `floatfea/run/pipeline.py:694` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1101 | `test_ft26_multi_npz.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `cli.py:209` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `cli.py:210` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `cli.py:211` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:73` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:74` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:75` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:76` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:77` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:78` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:79` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:80` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:81` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:82` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:83` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:84` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:85` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:86` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:87` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:88` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:89` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:90` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1102 | `floatfea/post/forces_table.py:91` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1103 | `floatfea/cli.py:89` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1103 | `floatfea/cli.py:90` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1103 | `floatfea/cli.py:91` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1103 | `floatfea/cli.py:92` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1103 | `floatfea/cli.py:93` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1103 | `floatfea/cli.py:94` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1103 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `.../h000/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `.../h045/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `../data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:146` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:149` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:151` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:152` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:153` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `cli.py:1237` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1532` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1533` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1534` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1535` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1536` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1537` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1600` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `config.py:1601` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `d0/../d0/v000.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `d0/v000.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `d5/V000.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `docs/F6_utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `docs/milestones/R1.md:396` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `docs/milestones/R1.md:397` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `docs/milestones/R1.md:398` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `docs/milestones/R1.md:399` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `docs/milestones/R1.md:400` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `examples/platform12_placeholder.yaml:129` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `floatfea/cli.py:474` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `floatfea/run/config.py:1532` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `floatfea/run/pipeline.py:788` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `no_sidecar/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `test_ft26_multi_npz.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1104 | `with_sidecar/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `.github/workflows/ci.yml` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `.github/workflows/ci.yml:41` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `.github/workflows/ci.yml:42` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `.github/workflows/ci.yml:43` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `floatfea/post/forces_table.py:405` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `floatfea/run/pipeline.py:793` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `scripts/suite_count.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `step-2-answers.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `test_ft26_multi_npz.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1105 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `results/F6b/truss_sizing.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `results/F6b/truss_sizing.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `results/F6b/truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `scripts/measure/f6b_report.py:88` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `tests/regression/test_fy3_triangle_closure.py:306` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1106 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1107 | `.claude/hooks/protect-reviews.sh:163` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1107 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1107 | `step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `tests/verification/rung3/test_tolerance_counter_cases.py:37` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `tests/verification/rung3/test_tolerance_counter_cases.py:38` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `tests/verification/rung3/test_tolerance_counter_cases.py:39` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `tests/verification/rung3/test_tolerance_counter_cases.py:40` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1108 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1109 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `R1.md:455` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `docs/milestones/R1.md:435` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1766` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1767` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1768` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1769` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1770` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1771` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1772` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1773` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1774` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1775` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1776` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1777` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1778` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1779` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1780` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1781` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1782` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1783` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1784` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1785` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1786` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1787` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1788` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1789` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1790` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1791` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1792` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `floatfea/tolerances.py:1793` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `tests/test_plan_matches_tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1110 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `f6a_premise_check.py:190` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `floatfea/run/pipeline.py:1452` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `scripts/measure/f6_results_report.py:474` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `scripts/measure/member_forces_table.py:348` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `tests/regression/test_generators_refuse_mismatched_inputs.py:138` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1111 | `tests/regression/test_generators_refuse_mismatched_inputs.py:139` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1686` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1687` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1688` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1689` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1691` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1692` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1693` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1694` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1112 | `floatfea/run/pipeline.py:1695` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1113 | `config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1113 | `floatfea/run/config.py:378` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1113 | `floatfea/run/pipeline.py:1777` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1114 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1114 | `floatfea/run/pipeline.py:1445` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1114 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `floatfea/run/truss.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `results/F6b/truss_sizing.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `results/F6b/truss_sizing.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `results/F6b/truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `results/F6b/truss_sizing.md:39` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `results/F6b/truss_sizing.md:40` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `results/F6b/truss_sizing.md:41` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1115 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1116 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1116 | `scripts/export_f4_dynamic_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/regression/test_generators_refuse_mismatched_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/test_ci_canonical_environment.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/test_ci_determinism_gate.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/test_ci_runs_the_whole_suite.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/test_ci_workflow_is_wellformed.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/test_collected_set_golden.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1117 | `tests/test_supervisor_conftest_pathspec.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1119 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1119 | `f6_results_report.py:718` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1119 | `scripts/ci_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1119 | `scripts/ci_section.py:412` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1119 | `tests/test_report_numbers_are_sourced.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1120 | `.claude/hooks/require-verdict.sh:461` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1120 | `answered_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1120 | `check_carried.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1120 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1120 | `scripts/answered_table.py:36` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1120 | `scripts/check_carried.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1120 | `scripts/check_carried.py:34` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1121 | `cli.py:918` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1121 | `cli.py:942` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1121 | `config.py:541` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1121 | `config.py:542` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1121 | `floatfea/cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1121 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1121 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1122 | `./results/F6b/truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1122 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1122 | `floatfea/run/truss.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1122 | `results/F6b/truss_sizing.md:39` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1122 | `results/F6b/truss_sizing.md:40` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1122 | `results/F6b/truss_sizing.md:41` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1122 | `truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1123 | `SCRATCH/out.txt` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1123 | `SCRATCH/t.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1124 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `.github/workflows/ci.yml:403` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `docs/F4_member_forces.csv:17` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `docs/F6_utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `examples/platform12_placeholder.yaml:104` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `pipeline.py:685` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `pipeline.py:686` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `pipeline.py:687` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `results/F6b/truss_sizing.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `results/F6b/truss_sizing.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `results/R1/example/utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `scripts/carried_table.py:101` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `scripts/ci_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `scripts/ci_section.py:999` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1128 | `tests/test_report_carried.py:248` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1129 | `answered_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1129 | `scripts/answered_table.py:51` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1130 | `scripts/ci_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1132 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1133 | `docs/reports/R1/step-3-answers.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1134 | `scripts/ci_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1137 | `ci.yml:90` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1139 | `.gitattributes` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1139 | `.gitignore` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1139 | `.gitkeep` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1139 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1139 | `docs/F6_utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1140 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1140 | `floatfea/plant_ctl.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1140 | `scripts/check_carried.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1140 | `tests/test_report_carried.py:403` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1141 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1141 | `docs/reports/R1/step-3.md:8914` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1142 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1143 | `.github/workflows/ci.yml` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1143 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1143 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1143 | `results/F6b/truss_sizing.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `results/F6b/truss_sizing.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3555` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3556` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3557` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3558` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3559` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3560` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3561` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1144 | `tests/test_report_carried.py:3562` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R1145 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `floatfea/cli.py:296` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `floatfea/cli.py:297` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `floatfea/cli.py:298` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `floatfea/cli.py:299` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `floatfea/run/pipeline.py:605` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `floatfea/run/pipeline.py:672` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `tests/regression/test_r1_example_regenerates.py:54` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `tests/regression/test_r1_example_regenerates.py:55` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `tests/regression/test_r1_example_regenerates.py:56` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R850 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `data/platform/platform12_deck.yaml` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:507` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:508` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:509` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:510` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:511` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:512` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:513` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:514` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:515` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:516` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:517` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:518` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:519` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:520` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:521` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:522` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `floatfea/run/config.py:523` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `home/someone-else/junk/platform12_deck.yaml` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `platform12_deck.yaml` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:105` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:106` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:107` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:108` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:109` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:110` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:111` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `tests/regression/test_r1_example_regenerates.py:112` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R851 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R852 | `docs/directives/FO.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R852 | `floatfea/cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R852 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R853 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R853 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R853 | `tests/regression/test_r1_example_regenerates.py:62` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R853 | `tests/regression/test_r1_example_regenerates.py:63` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R853 | `tests/regression/test_r1_example_regenerates.py:64` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R853 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R854 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R854 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R854 | `tests/regression/test_r1_example_regenerates.py:48` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R854 | `tests/regression/test_r1_published_artifacts.py:69` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R854 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R855 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R855 | `scripts/suite_count.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `docs/directives/FR.md:28` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `docs/directives/FR.md:29` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `docs/directives/FR.md:30` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `docs/directives/FR.md:31` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `docs/directives/FR.md:32` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `docs/directives/FR.md:33` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `scripts/write_verdict.py:179` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `scripts/write_verdict.py:180` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `scripts/write_verdict.py:181` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R856 | `step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R857 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R857 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R857 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R858 | `tests/regression/test_r1_example_regenerates.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R859 | `cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R859 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R859 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R860 | `cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R860 | `floatfea/cli.py:297` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R860 | `floatfea/run/pipeline.py:605` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R860 | `tests/regression/test_r1_example_regenerates.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R861 | `tests/regression/test_r1_example_regenerates.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R861 | `tests/test_collected_set_golden.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R861 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R862 | `floatfea/run/pipeline.py:673` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R862 | `pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R862 | `pipeline.py:673` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R862 | `tests/regression/test_r1_example_golden.py:318` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R862 | `tests/regression/test_r1_example_golden.py:321` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R863 | `floatfea/cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R863 | `floatfea/run/pipeline.py:605` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R863 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R863 | `tests/regression/test_r1_example_regenerates.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R864 | `floatfea/cli.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R865 | `home/someone-else/junk/other_cases.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R865 | `tests/regression/test_r1_example_regenerates.py:224` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R865 | `tests/regression/test_r1_example_regenerates.py:225` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R865 | `tests/regression/test_r1_example_regenerates.py:226` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R865 | `tests/regression/test_r1_example_regenerates.py:227` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R865 | `tests/regression/test_r1_example_regenerates.py:228` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R865 | `tests/regression/test_r1_example_regenerates.py:229` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:354` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:355` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:356` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:357` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:358` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:359` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:361` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:362` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/cli.py:407` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/run/config.py:425` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/run/pipeline.py:515` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/run/pipeline.py:543` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `floatfea/run/pipeline.py:558` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `report.md:7` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `report.md:23` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `report.md:55` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R866 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R867 | `floatfea/model/platform.py:629` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R867 | `floatfea/post/forces_table.py:169` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R867 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R867 | `floatfea/run/config.py:898` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R867 | `floatfea/solve/static.py:135` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R868 | `examples/platform12_placeholder.yaml:35` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R868 | `tests/unit/test_topology_from_config.py:92` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R869 | `floatfea/model/platform.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R869 | `floatfea/model/platform.py:626` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R869 | `floatfea/post/forces_table.py:169` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R869 | `floatfea/solve/static.py:135` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R870 | `docs/milestones/R1.md:81` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R870 | `docs/milestones/R1.md:352` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R870 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R870 | `floatfea/run/pipeline.py:123` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R870 | `floatfea/run/pipeline.py:180` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R871 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R871 | `CLAUDE.md:421` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R871 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R871 | `docs/SUPERVISOR.md:1` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R871 | `docs/SUPERVISOR.md:547` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R872 | `floatfea/run/config.py:189` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R872 | `floatfea/run/pipeline.py:586` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R873 | `floatfea/run/pipeline.py:583` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R873 | `floatfea/run/pipeline.py:584` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R873 | `floatfea/run/pipeline.py:585` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R873 | `floatfea/run/pipeline.py:586` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R874 | `floatfea/cli.py:146` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R874 | `floatfea/run/config.py:199` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R874 | `floatfea/run/pipeline.py:583` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R874 | `floatfea/run/pipeline.py:584` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R874 | `floatfea/run/pipeline.py:585` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R874 | `floatfea/run/pipeline.py:586` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R875 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R875 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R875 | `docs/SUPERVISOR.md:549` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R875 | `docs/SUPERVISOR.md:555` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R875 | `docs/SUPERVISOR.md:556` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R875 | `docs/SUPERVISOR.md:557` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R876 | `tests/unit/test_headings_and_bem_coverage.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `docs/conventions.md:143` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `docs/conventions.md:144` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `docs/conventions.md:145` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `docs/conventions.md:146` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `docs/conventions.md:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `examples/platform12_placeholder.yaml` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:583` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:584` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:585` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:586` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:629` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:630` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:687` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:688` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:689` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:691` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:692` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:693` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:694` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:695` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:696` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:697` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:698` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `floatfea/run/pipeline.py:699` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `report.md:23` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `tests/regression/test_r1_example_golden.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R877 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `cli.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `docs/milestones/F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:136` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:137` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:138` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:139` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:140` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:141` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:146` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:149` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:262` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:263` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:264` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:265` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:395` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:396` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/cli.py:397` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/run/pipeline.py:695` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/run/pipeline.py:696` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/run/pipeline.py:697` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/run/pipeline.py:698` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/run/pipeline.py:699` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `scripts/f4_dynamic_residual.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `tests/test_supervisor_conftest_pathspec.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `tests/unit/test_headings_and_bem_coverage.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R878 | `tests/unit/test_run_pipeline_refusals.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `config.py:212` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/config.py:202` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/config.py:208` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/config.py:212` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:581` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:582` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:583` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:584` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:585` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:586` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:587` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:588` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:589` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:590` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:591` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:592` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R879 | `floatfea/run/pipeline.py:593` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `.claude/agents/gating-supervisor.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `.claude/hooks/require-verdict.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:429` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:458` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:459` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:460` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:461` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:462` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:463` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:464` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:465` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:466` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:467` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:468` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:469` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:470` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:471` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:472` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:473` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:474` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:475` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:476` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:477` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:478` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `CLAUDE.md:479` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `config.py:196` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `data/f4/dynamic_inputs.provenance.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `docs/directives/FT.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `docs/milestones/F2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `docs/milestones/F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `pipeline.py:1027` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `scripts/f4_dynamic_residual.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `scripts/measure/f6a_required_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `scripts/measure/f6b_truss_sizing.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `tests/regression/test_r1_published_artifacts.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `tests/test_plan_figures.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `tests/test_tree_prose_consistent.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R880 | `tests/unit/test_headings_and_bem_coverage.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `floatfea/run/config.py:190` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `floatfea/run/config.py:931` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `floatfea/run/pipeline.py:52` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `floatfea/run/pipeline.py:722` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R881 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R882 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R882 | `floatfea/run/pipeline.py:589` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R882 | `floatfea/run/pipeline.py:597` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R882 | `floatfea/run/pipeline.py:633` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R883 | `floatfea/run/pipeline.py:712` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R884 | `floatfea/run/pipeline.py:802` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R885 | `docs/conventions.md:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R885 | `readers/capytaine.py:191` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R885 | `readers/capytaine.py:192` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R885 | `readers/capytaine.py:193` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R885 | `readers/capytaine.py:194` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R885 | `scripts/export_f4_dynamic_inputs.py:524` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R885 | `scripts/report_joint_reactions.py:93` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R886 | `pyproject.toml:110` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R886 | `tests/unit/test_headings_and_bem_coverage.py:35` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `.../repo/docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `docs/reports/R1/step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `tests/test_report_guard_states.py:90` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `tests/test_report_guard_states.py:91` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R887 | `tests/test_report_guard_states.py:494` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R888 | `.claude/hooks/require-verdict.sh:240` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R888 | `.claude/hooks/require-verdict.sh:276` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R888 | `docs/reports/F7/step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R888 | `docs/reports/R1/step-4.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R889 | `.claude/hooks/require-verdict.sh:157` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R889 | `docs/directives/FT.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R889 | `docs/directives/FT.md:44` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R890 | `results/R1/example/report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R890 | `results/R1/example/report.md:89` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R890 | `scripts/measure/f6a_required_section.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R890 | `scripts/measure/f6b_truss_sizing.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R891 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R892 | `...docs/reports/R1/step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R892 | `.claude/hooks/require-verdict.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R892 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R893 | `F2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R893 | `docs/milestones/F2.md:22` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R893 | `docs/milestones/F6.md:145` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R893 | `docs/milestones/R1.md:5` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R893 | `docs/milestones/R1.md:6` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R893 | `docs/reports/F6/step-1.md:22` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/directives/FT.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/milestones/R1.md:352` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/milestones/R1.md:353` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/milestones/R1.md:354` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/milestones/R1.md:355` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/milestones/R1.md:356` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/milestones/R1.md:357` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R894 | `docs/milestones/R1.md:358` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `cli.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `cli.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `cli.py:265` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `cli.py:266` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `config.py:931` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:682` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:683` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:684` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:685` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:686` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:687` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:688` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:689` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:691` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:692` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:693` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:694` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:695` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/run/pipeline.py:696` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `scripts/measure/f6_results_report.py:400` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `scripts/measure/f6_results_report.py:401` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R895 | `utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `config.py:189` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `config.py:190` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `tests/regression/test_f6_deliverable_agrees_with_itself.py:235` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R896 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R897 | `.../repo/docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R897 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R897 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R897 | `step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R897 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R897 | `tests/test_report_guard_states.py:536` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `.claude/hooks/require-verdict.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `.claude/hooks/require-verdict.sh:285` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `.claude/hooks/require-verdict.sh:286` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `.claude/hooks/require-verdict.sh:287` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `.claude/hooks/require-verdict.sh:288` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `.claude/hooks/require-verdict.sh:289` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:189` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:190` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:191` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:192` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:193` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:194` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:195` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `config.py:196` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `docs/reports/R1/step-4.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `docs/reviews/R1/step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `docs/reviews/R1/step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `floatfea/run/config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `tests/unit/test_forces_table_reexports.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R898 | `tests/unit/test_headings_and_bem_coverage.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `.claude/agents/gating-supervisor.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:24` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:25` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:26` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:27` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:28` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:29` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:30` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:31` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:32` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R899 | `docs/SUPERVISOR.md:33` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R901 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `f6_results_report.py:76` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `member_forces_table.py:143` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R902 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `config.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `config.py:196` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `config.py:733` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:961` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:962` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:963` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:964` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:965` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:966` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:967` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:968` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:969` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:970` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:971` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:972` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:973` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:974` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:975` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:976` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:977` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:978` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:979` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:980` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `pipeline.py:981` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R903 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `docs/reviews/R1/step-10.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `docs/reviews/R1/step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:851` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:852` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:853` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:854` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:855` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:856` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:857` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:858` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:859` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:860` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R904 | `tests/test_report_guard_states.py:861` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R905 | `config.py:196` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R905 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R905 | `tests/prose_triple_controls.txt` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `scripts/f4_dynamic_residual.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `scripts/measure/f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `scripts/measure/f6a_premise_check.py:188` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `tests/regression/test_f6_deliverable_agrees_with_itself.py:492` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `tests/unit/test_forces_table_reexports.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R906 | `tests/unit/test_forces_table_reexports.py:47` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `f6_results_report.py:1052` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R907 | `test_f6_deliverable_agrees_with_itself.py:235` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `f6a_premise_check.py:185` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `member_forces_table.py:287` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1012` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1013` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1014` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1015` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1016` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1017` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1027` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1028` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1029` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1030` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1031` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1032` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1033` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1034` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1035` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1036` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1037` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1038` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `pipeline.py:1039` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `scripts/export_f4_dynamic_inputs.py:430` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R908 | `tests/regression/test_r1_example_golden.py:420` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1043` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1044` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1045` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1046` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1047` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1048` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1049` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `pipeline.py:1050` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R909 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R910 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `floatfea/io/integrator.py:30` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:704` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:705` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:706` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:707` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:708` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:709` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:710` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:711` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:712` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:713` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:714` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:715` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:716` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R911 | `pipeline.py:717` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R913 | `floatfea/cli.py:145` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R913 | `floatfea/cli.py:146` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R913 | `floatfea/cli.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R913 | `floatfea/cli.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R913 | `floatfea/cli.py:149` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R914 | `scripts/measure/member_forces_table.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R914 | `scripts/measure/member_forces_table.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R914 | `scripts/measure/member_forces_table.py:149` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R914 | `scripts/measure/member_forces_table.py:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R914 | `scripts/measure/member_forces_table.py:151` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R914 | `scripts/measure/member_forces_table.py:152` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R914 | `scripts/measure/member_forces_table.py:153` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R917 | `pipeline.py:869` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R918 | `member_forces_table.py:312` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1027` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1028` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1029` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1030` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1031` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1032` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1033` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1034` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1035` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1036` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1037` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1038` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `pipeline.py:1039` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `results/F6a/premise_check.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `results/F6a/required_section.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `scripts/measure/f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R919 | `scripts/measure/f6a_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R920 | `data/f4/dynamic_inputs.npz` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R920 | `floatfea/run/pipeline.py:944` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R920 | `floatfea/run/pipeline.py:945` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R920 | `floatfea/run/pipeline.py:946` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R920 | `test_r1_example_golden.py:402` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R921 | `scripts/measure/f6a_premise_check.py:358` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R922 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R922 | `f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R922 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R922 | `tests/regression/test_f6_deliverable_agrees_with_itself.py:490` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `scripts/measure/member_forces_table.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `scripts/measure/member_forces_table.py:149` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `scripts/measure/member_forces_table.py:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `scripts/measure/member_forces_table.py:151` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `scripts/measure/member_forces_table.py:152` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `scripts/measure/member_forces_table.py:153` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R924 | `scripts/measure/member_forces_table.py:154` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R925 | `config.py:507` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R925 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R925 | `docs/F4_member_forces.csv:17` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R925 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R925 | `docs/F4_member_forces.md:21` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R925 | `member_forces_table.py:252` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R925 | `scripts/measure/member_forces_table.py:252` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R926 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R926 | `f6_results_report.py:428` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R926 | `f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R926 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R926 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R926 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R927 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R927 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R927 | `f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R927 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R927 | `member_forces_table.py:285` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R927 | `member_forces_table.py:312` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R927 | `pipeline.py:999` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R930 | `member_forces_table.py:166` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R932 | `f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R932 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:142` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:143` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:144` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:145` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:146` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:149` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `cli.py:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1098` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1099` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1100` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1101` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1102` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1103` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1104` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1105` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1106` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1107` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1108` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1109` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1110` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1111` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1112` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1113` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1114` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1115` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1116` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1117` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1118` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1119` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R934 | `pipeline.py:1120` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `tests/unit/test_headings_and_bem_coverage.py:34` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `tests/unit/test_headings_and_bem_coverage.py:35` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `tests/unit/test_headings_and_bem_coverage.py:36` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `tests/unit/test_headings_and_bem_coverage.py:37` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `tests/unit/test_headings_and_bem_coverage.py:38` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `tests/unit/test_headings_and_bem_coverage.py:39` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R935 | `tests/unit/test_headings_and_bem_coverage.py:40` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R936 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R936 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R936 | `member_forces_table.py:339` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R936 | `member_forces_table.py:493` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `docs/F4_member_forces.csv:17` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:343` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:344` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:345` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:346` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:347` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:348` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:429` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:430` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:431` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:432` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:433` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:434` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:435` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:436` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:437` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:438` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:439` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:440` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:441` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:442` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:443` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:444` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:445` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R937 | `member_forces_table.py:446` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `f6_results_report.py:305` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `f6_results_report.py:341` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `f6_results_report.py:342` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `f6_results_report.py:343` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `f6_results_report.py:344` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `f6_results_report.py:481` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R938 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `docs/milestones/F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `floatfea/run/pipeline.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `scripts/f4_dynamic_residual.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `scripts/measure/f6a_premise_check.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `tests/test_report_guard_states.py:896` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R939 | `tests/unit/test_headings_and_bem_coverage.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R941 | `pipeline.py:688` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R943 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R943 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R943 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R943 | `results/F6/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:655` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:656` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:657` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:658` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:659` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:660` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:661` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:662` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:663` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:664` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:665` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R944 | `member_forces_table.py:666` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:332` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:333` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:334` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:335` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:336` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:337` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:338` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:339` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:340` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:341` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:342` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:343` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:344` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:345` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:346` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:347` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:348` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:349` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:350` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:351` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:352` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:353` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:354` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:355` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:356` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:357` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:358` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:359` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `f6_results_report.py:360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:143` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:144` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:145` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:146` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:147` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:148` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:149` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:151` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:152` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R945 | `tests/regression/test_generators_refuse_mismatched_inputs.py:153` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `f6_results_report.py:377` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:156` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:157` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:158` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:159` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:160` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:161` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:162` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:163` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:164` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:165` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:166` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:167` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:168` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:169` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:170` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:171` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:172` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:173` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:174` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:175` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:176` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:177` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:178` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R946 | `tests/regression/test_generators_refuse_mismatched_inputs.py:179` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:333` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:334` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:335` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:336` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:337` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:338` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:347` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `f6_results_report.py:348` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R947 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R948 | `tests/test_no_tolerance_literals.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R949 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:677` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:678` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:679` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:680` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:681` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:683` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:684` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:685` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:686` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:687` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:688` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:689` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:691` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:692` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `member_forces_table.py:693` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `scripts/run_rung.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R950 | `tests/regression/test_generators_refuse_mismatched_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R951 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R951 | `f6_results_report.py:636` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R951 | `f6_results_report.py:637` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R951 | `f6_results_report.py:638` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R951 | `member_forces_table.py:542` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R951 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `f6_results_report.py:354` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `f6_results_report.py:355` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `f6_results_report.py:356` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `f6_results_report.py:357` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `f6_results_report.py:358` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `f6_results_report.py:359` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `f6_results_report.py:360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R952 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:683` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:684` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:685` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:686` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:687` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:688` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:689` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:691` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:692` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R953 | `member_forces_table.py:693` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `test_f6_deliverable_agrees_with_itself.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py:9` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py:10` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py:11` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py:12` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py:13` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py:14` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R954 | `tests/regression/test_generators_refuse_mismatched_inputs.py:15` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R955 | `member_forces_table.py:396` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R955 | `member_forces_table.py:397` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `dynamic_inputs.provenance.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `f6_results_report.py:656` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `f6_results_report.py:657` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `f6_results_report.py:658` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `f6_results_report.py:659` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `f6_results_report.py:660` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `f6_results_report.py:661` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `floatfea/run/pipeline.py:684` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `floatfea/run/pipeline.py:685` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `floatfea/run/pipeline.py:686` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `floatfea/run/pipeline.py:687` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `floatfea/run/pipeline.py:688` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `floatfea/run/pipeline.py:689` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `floatfea/run/pipeline.py:690` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R957 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R958 | `floatfea/run/pipeline.py:1132` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R958 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R958 | `scripts/measure/f6_results_report.py:558` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R958 | `scripts/measure/f6_results_report.py:570` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R958 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R958 | `scripts/measure/member_forces_table.py:339` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `.gitattributes` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/F6_utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/directives/FT.md:17` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/directives/FT.md:18` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/directives/FT.md:19` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/milestones/F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `results/F6/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `scripts/measure/member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `scripts/run_rung.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `tests/regression/test_generators_refuse_mismatched_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R959 | `tests/unit/test_forces_table_reexports.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `api_wsd_utilisation.py:241` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `api_wsd_utilisation.py:242` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `f6a_premise_check.py:360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `f6a_report.py:411` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `f6a_required_section.py:575` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `f6a_required_section.py:576` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `f6b_report.py:414` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `f6b_truss_sizing.py:679` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `f6b_truss_sizing.py:680` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `g41_dynamic.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `r754_stress_vs_grade.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R960 | `scripts/measure/member_forces_table.py:458` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R961 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R961 | `f6_results_report.py:240` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R961 | `f6_results_report.py:656` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R961 | `member_forces_table.py:248` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R961 | `member_forces_table.py:440` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R966 | `f6_results_report.py:551` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `.gitattributes` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/F6_utilisation.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/directives/FT.md:17` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/directives/FT.md:18` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/directives/FT.md:19` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/milestones/F2a.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `scripts/measure/api_wsd_utilisation.py:150` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `scripts/measure/api_wsd_utilisation.py:151` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `scripts/measure/f6_results_report.py:1172` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `scripts/measure/f6_results_report.py:1173` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `scripts/measure/f6_results_report.py:1174` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R967 | `scripts/write_verdict.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `dynamic_inputs.provenance.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:585` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:586` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:587` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:656` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:657` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:658` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:659` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:660` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `f6_results_report.py:661` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `floatfea/run/pipeline.py:1132` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `scripts/export_f4_dynamic_inputs.py:527` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R968 | `scripts/measure/member_forces_table.py:660` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `docs/directives/FR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `f6_results_report.py:570` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `f6_results_report.py:661` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `floatfea/run/config.py:949` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `scripts/run_rung.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R969 | `tests/regression/test_generators_refuse_mismatched_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `docs/F4_member_forces.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `docs/F6_utilisation.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `export_platform_deck.py:225` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `results/F6a/premise_check.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `results/F6a/required_section.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `results/F6b/truss_sizing.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `results/R1/example/report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `test_generators_refuse_mismatched_inputs.py:504` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `test_marker_exemption_corpus.py:493` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `test_platform_deck_export.py:109` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `tests/regression/test_f6_deliverable_agrees_with_itself.py:40` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `tests/regression/test_r1_example_golden.py:56` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R970 | `tests/regression/test_r1_example_regenerates.py:138` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R971 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R971 | `tests/regression/test_generators_refuse_mismatched_inputs.py:504` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R973 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R974 | `scripts/suite_count.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R975 | `.gitattributes` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R975 | `tests/test_tree_prose_consistent.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:14` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:15` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:16` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:17` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:18` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:19` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:20` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:21` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:22` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:23` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:24` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:25` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/directives/FR.md:26` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:615` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:616` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:617` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:639` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:640` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:641` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:642` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:643` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:644` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `f6_results_report.py:661` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `floatfea/run/config.py:949` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `scripts/run_rung.sh` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `step-1.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `step-2.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `tests/conftest.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R976 | `tests/regression/test_generators_refuse_mismatched_inputs.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R977 | `dynamic_inputs.provenance.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R977 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R977 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R977 | `scripts/export_f4_dynamic_inputs.py:69` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R977 | `scripts/export_f4_dynamic_inputs.py:402` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R977 | `scripts/export_f4_dynamic_inputs.py:527` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R977 | `tests/regression/test_generators_refuse_mismatched_inputs.py:622` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:77` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:196` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:197` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:198` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:199` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:200` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:201` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:202` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:203` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:204` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:205` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:206` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:207` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:208` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `api_wsd_utilisation.py:209` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `f6_results_report.py:48` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `f6_results_report.py:602` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `f6_results_report.py:603` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `floatfea/checks/api_wsd.py:561` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `floatfea/checks/api_wsd.py:562` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `floatfea/checks/api_wsd.py:563` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `floatfea/checks/api_wsd.py:564` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `floatfea/tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `scripts/measure/api_wsd_utilisation.py:205` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `scripts/measure/api_wsd_utilisation.py:206` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `scripts/measure/api_wsd_utilisation.py:207` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `scripts/measure/api_wsd_utilisation.py:208` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `scripts/measure/api_wsd_utilisation.py:209` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `scripts/measure/api_wsd_utilisation.py:229` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R978 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:56` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:164` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:165` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:166` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:167` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:168` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:169` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:170` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:171` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:172` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:173` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:174` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:175` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:176` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:177` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `api_wsd_utilisation.py:178` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `floatfea/post/forces_table.py:435` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `floatfea/post/forces_table.py:504` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `floatfea/run/config.py:419` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R979 | `member_forces_table.py:161` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R980 | `scripts/measure/f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `api_wsd_utilisation.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `api_wsd_utilisation.py:241` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `f6_results_report.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `f6_results_report.py:250` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `f6a_premise_check.py:360` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `f6a_report.py:411` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `f6a_required_section.py:575` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `f6b_report.py:414` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `f6b_truss_sizing.py:679` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `member_forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `member_forces_table.py:461` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R981 | `tests/regression/test_generators_refuse_mismatched_inputs.py:89` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R983 | `api_wsd_utilisation.py:61` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R985 | `docs/SUPERVISOR.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:17` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:18` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:19` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:20` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:21` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:22` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:23` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/directives/FT.md:24` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `docs/milestones/F6.md:102` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `f6_results_report.py:795` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `f6_results_report.py:796` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `f6_results_report.py:797` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `f6_results_report.py:1219` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `f6_results_report.py:1220` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `f6_results_report.py:1221` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `f6_results_report.py:1222` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R986 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R987 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R987 | `docs/milestones/R1.md:356` | the file is touched and this line number is the old one |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R987 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R987 | `scripts/export_f4_dynamic_inputs.py:104` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R987 | `scripts/export_f4_dynamic_inputs.py:524` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R987 | `scripts/report_joint_reactions.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R988 | `floatfea/run/config.py:419` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R990 | `CLAUDE.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R990 | `docs/reports/R1/step-2-answers.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R990 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R990 | `step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:21` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:22` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:23` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:24` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:25` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:26` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:27` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `docs/directives/FT.md:28` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:981` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1537` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1538` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1539` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1540` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1541` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1542` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1543` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1544` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1545` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1546` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `f6_results_report.py:1547` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R991 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:125` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:126` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:127` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:128` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:129` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:130` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:131` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:132` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:166` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:167` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:168` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:169` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:170` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:171` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `api_wsd_utilisation.py:172` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `f6_results_report.py:926` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `f6_results_report.py:1459` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `f6_results_report.py:1461` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/checks/api_wsd.py:561` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/checks/api_wsd.py:562` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/checks/api_wsd.py:563` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/checks/api_wsd.py:564` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:389` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:390` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:391` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:392` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:393` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:394` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:395` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:396` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:397` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:398` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:399` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:400` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:401` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:402` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:403` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:404` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:405` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:406` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `floatfea/post/forces_table.py:407` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `member_forces_table.py:777` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `results/F6/floatfea_results_report.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R992 | `tolerances.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R994 | `floatfea/model/platform.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R996 | `docs/reports/R1/step-2-answers.json` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R996 | `docs/reports/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R996 | `docs/reviews/R1/step-3.md` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R996 | `tests/test_report_guard_states.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R999 | `docs/F4_member_forces.csv` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R999 | `floatfea/cli.py:193` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R999 | `floatfea/cli.py:194` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R999 | `scripts/measure/member_forces_table.py:505` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R999 | `scripts/measure/member_forces_table.py:506` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
| R999 | `test_r1_example_golden.py` | the file is untouched |  **no change.** Verdict 47 is a PASS that closes step 3; this commit answers its one blocking finding at the pattern, and the diff is three files. Nothing in it reaches this site. |
