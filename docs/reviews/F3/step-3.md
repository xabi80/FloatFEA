# Review — F3 step 3
Reviewed commit: c834593fa05ab8e79f9b1b0c0fdcb41df6305e73
Verdict: HOLD
**Reviewed commit: `6083a87`.** (HEAD of F3 and pushed when I began. I committed corpus
batch 32 at `c834593` before writing, so the script's `Reviewed commit:` stamp is the
corpus commit and NOT the judged one -- `scripts/write_verdict.py`'s own docstring
records that. The judged commit is `6083a87` and every figure below is taken there.)
Tests: 2953 passed, 8 failed, 0 skipped   (MY OWN run, ONE invocation, no exclusion, clean clone at `6083a87` outside the synced folder, 1409.45s)

## Round of 2026-10-02 -- EIGHTY-SEVENTH verdict. ON THE TREE. IT COUNTS AGAINST NO STEP.

**STEP 3 IS CLOSED AT PASS, AT VERDICT 86, UNDER DD1, AND NOTHING IN THIS VERDICT
REOPENS IT.** This round is about the state of the tree and about EJ4's STOP. I read
EB4 the same way the hand-back does: it counts against no step. **The disposition of
F3 step 3 is PASS.** The `Stop` hook reads the last line of this file and will now
read `HOLD`; `CLAUDE.md` section Step gating says that disagreement is resolved
against DD1, and this sentence is the record it is resolved by. **What the HOLD below
holds is F4 step 1's FIRST COMMIT, not step 3.**

**AND THE ANSWER TO THE QUESTION YOU ASKED HARDEST: EJ4's STOP IS WRONG, AND IT IS
WRONG IN A WAY THAT MAKES THE PHYSICS IN IT MORE RIGHT, NOT LESS.** The static part is
genuinely absent -- more thoroughly absent than section 6a says, and I measured it
rather than read it. But absent from FloatSim was never the blocker, because
`docs/load-interchange-v1.md` section 7 locks `gravity` and `hydrostatic` OUT of the
schema BY DECISION and `PLAN.md` G4.6 prescribes that FloatFEA rebuilds both. And
EJ4(b)'s residual IS formable, today, from what is already in process: I formed it,
and the exact discrete identity closes to `1.257436e-04 N`. **F4's load mapping is not
blocked. Nothing has to go to Xabier for F4 to start.** R645 and R646 below.

**WHAT DOES BLOCK IS TWO LINES AND IT IS THE CZ1 CLASS EXACTLY.** `ruff check` is RED
at this commit on `floatfea/tolerances.py:398`, a 126-character comment line added by
the closure commit `c9902d3`; CI's lint job fails at step 6 and **`black`, `mypy`,
`unit tests` and `guards and meta-tests` are ALL SKIPPED behind it**, which is the
single thing CZ1 (iii) was written to make visible. And the report's section 0a calls
run `36997601588` `**no result** (status in_progress)` when `gh` says `failure` -- that
run is the one that would have shown the ruff red.

## THE TREE AT 6083a87, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse F3 && git rev-parse origin/F3, before my
         corpus commit
out    6083a87a4d1391cab0a1338af1b09bd58de1fbfb   all three
cmd    git status --porcelain --untracked-files=all
out    (no output)      the working tree is CLEAN, which it was not last round
cmd    git log --oneline b7c05e7..6083a87
out    6083a87 closure: EJ4 stopped at its own condition
out    d4b89e0 report: R643's site declared
out    b702f15 report: revision 3 carries verdict 86 -- R643 and R644 added
out    c9902d3 closure: EJ1 settles C121, EJ3 ledgers the rest (F3)
out    66af185 process: R644 -- two carve-out placements corrected (EJ2)
out    aec96e0 report: F3 step 3 revision 3 -- F3 CLOSES, and the blocker was OneDrive
cmd    item 1b: the newest revision's Answers: header against the newest verdict
out    docs/reports/F3/step-3.md:955   Answers: verdict 86 @ 3b5e36b
judge  1b PASSES. Verdict 86 IS the newest verdict and the report names it. This is
       the first commit of this milestone at which that line has been right, and it
       is the one comparison a machine cannot make for me.
cmd    git diff b7c05e7..6083a87 -- tests/conftest.py "tests/**/conftest.py"
out    (no output)
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py        CI0: the pathspec resolves to a real file, as it must
judge  CH2: no conftest changed and no rung carries its own. Nothing can rewrite a
       rung's record this round.
cmd    python -m pytest -q, clean clone at 6083a87 under the LOCAL temp, ONE
         invocation, no --ignore
out    8 failed, 2953 passed, 2 warnings in 1409.45s (0:23:29)
cmd    python -m ruff check floatfea tests
out    E501 Line too long (126 > 100)  --> floatfea/tolerances.py:398:101
out    Found 1 error.      exit 1
cmd    python -m black --check floatfea tests
out    91 files would be left unchanged.      exit 0
cmd    python -m mypy floatfea
out    Success: no issues found in 30 source files
cmd    python scripts/check_carried.py
out    check_carried: all 11 findings carried      exit 0
```

## CI AT THE REVIEWED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit 6083a87a4d13... --json databaseId,conclusion,status
out    36998118365  completed  FAILURE
cmd    gh run view 36998118365 --json jobs, job by job
out    the verification ladder            SUCCESS   13 steps  10:55:05 -> 10:58:35
out    lint, unit and guards              FAILURE   14 steps  10:55:05 -> 10:55:32
out    CI determinism -- leg              skipped    0 steps
out    CI determinism -- ten legs agree   skipped    0 steps
cmd    the lint job's steps, by number and conclusion
out    5 actionlint SUCCESS, 6 ruff FAILURE, 7 black --check SKIPPED,
out    8 mypy SKIPPED, 9 unit tests SKIPPED, 10 guards and meta-tests SKIPPED
cmd    gh run view 36998118365 --log-failed
out    E501 Line too long (126 > 100) / Found 1 error. / exit code 1
judge  NOT CK2: thirteen and fourteen real steps, real durations, no spending
       annotation, no runner-never-started. The two skipped determinism jobs are
       CK0's workflow_dispatch gate, UNAVAILABLE BY DECLARATION, as at 79 to 86.
       THE LADDER IS GREEN AT THIS COMMIT, ALL SIX RUNGS -- so NO LOW RUNG IS RED
       AND NOTHING HERE IS A STOP.
judge  CI IS RED AT THE REVIEWED COMMIT AND I RECORD IT AS RED (CA2).
judge  AND THE SECOND CONSEQUENCE IS THE ONE THAT MATTERS: because `ruff` is step 6,
       `guards and meta-tests` NEVER RAN. So CI gives NO independent reading on my
       eight reds at this commit, and my own clone is the only instrument. That is
       the exact condition CA2 exists to prevent, caused by a line wrap.
cmd    gh run view 36997601588 --json jobs, the run at c9902d3
out    lint, unit and guards FAILURE, ruff FAILURE at step 6, steps 7 to 10 SKIPPED
judge  THE SAME RED SHIPPED IN TWO CLOSURE COMMITS AND NEITHER PASTED CZ1 (ii).
```

## THE EG3(i) TRACE, ALL 8 MATCHED INDIVIDUALLY, AND THEY ARE ONE CAUSE

```
out     1 x test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
out           -> ON NEITHER LIST. CZ1 (iv).
out     7 x test_the_guard_survives_the_state[baseline, non_numeric_step_suffix,
out           superscript_digit_step_number, draft_suffix_beside_a_step_report,
out           step_number_is_the_empty_string,
out           verdict_amended_after_the_commit_the_report_answers,
out           zero_padded_step_number]
out           -> cascade off a RED BASELINE, identified by the baseline's own
out              failure line and not by its name (EH1)
cmd    the baseline's own failure text, read rather than assumed
out    "1 failed, 220 passed in 5.16s", and the one failure inside the planted clone
out    is test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW, same message
cmd    python -m pytest ...::test_the_guard_reads_the_step_being_worked_on -q
out    PASSES -- so this is NOT EG3 state (1)
cmd    the five state-(2) names plus EH1's two additions
out    ALL PASS -- revision 3 answers verdict 86, so state (2) IS cleared, and
out    test_the_report_carries_a_WHOLE_SUITE_count PASSES: R643 is answered
rule   EG3(i): every red traces BY NAME, and a red that does not match is CZ1 (iv)
       unchanged
judge  ZERO of the eight are the boundary. ALL EIGHT are one cause and one fix
       clears them. EG3's own discriminator -- does the answering report clear it --
       says no: revision 3 is in the tree and it is still red.
judge  AND EG3(ii) IS CLEARED FOR VERDICT 86: I ran the three report-guard files AT
       `6083a87`, `8 failed, 273 passed in 246.93s`, 281 collected. State (2) is
       GREEN there, which is the half no verdict in this milestone had measured.
```

## MY RULING ON EJ4 -- THE THING YOU ASKED FOR, AND I RAN IT RATHER THAN READ IT

**(1) YOU ARE RIGHT THAT THE STATIC PART IS ABSENT, AND IT IS ABSENT FOR A STRONGER
REASON THAN SECTION 6a GIVES. `solve_equilibrium=False` IS NOT THE CAUSE.** One
variable moved, everything else held -- same deck, same shared database, same `dt`,
same two overrides, verbatim from the study:

```
claim  running with solve_equilibrium=True would recover the static part
cmd    build_system(deck, bem_databases={}, dt=0.01, t_max_kernel=30.0,
         solve_equilibrium=False then True, shared_hydro_database=hdb,
         asymptote_check_override=..., kernel_decay_floor_override=...)
out    False: |xi0|_inf = 0.000000e+00
out    True : |xi0|_inf = 0.000000e+00
out    |xi0_true - xi0_false|_inf = 0.000000e+00
cell   ONE VARIABLE: solve_equilibrium. Deck, database, dt, overrides all held.
rule   a causal claim carries its ablation (BG0)
judge  REFUTED. `solve_equilibrium=True` CHANGES NOTHING ON THIS DECK, so the first
       of section 6a's three ways out recovers nothing. The reason is in the function
       itself: `floatsim/solver/equilibrium.py:98` solves `C xi = F_state(0, xi, 0)`
       -- no gravity term, no buoyancy term, and no constraints.
```

```
claim  the static reaction is zero BY CONSTRUCTION and not merely unexported
cmd    |state_force(0, xi0, 0)|_inf, then |C @ xi0|_inf, then |C xi0 - F_state|_inf
out    0.000000e+00, 0.000000e+00, 0.000000e+00
cmd    the fields of the assembled left-hand side
out    CumminsLHS fields: ['C', 'M_plus_Ainf']      -- there is no force vector
cmd    diag(C) on a structural body
out    diag(C) hub1 = [0. 0. 0. 0. 0. 0.]
cmd    the bodies with no hydro label, and their weight
out    hub1..hub4 at 12.0 kg and platform at 10.0 kg -> 568.98 N
out    bodies with a hydro label: 12 of 17
rule   verify the reference independently of the thing measured
judge  xi = 0 IS AN EXACT EQUILIBRIUM OF THIS MODEL WITH ZERO JOINT REACTION. Gravity
       is nowhere in the equations; `C` is a restoring derivative and nothing else.
       Your ratio `4.655e-03` is the right finding; the per-body version is sharper
       and I give it in (4) below.
```

**(2) AND THE STATIC PART IS NOT RECOVERABLE FROM ANYTHING EXPORTED. YOU ASKED THIS
EXACT QUESTION AND THE ANSWER IS NO.**

```
cmd    the fields of the hydro database the study loads
out    ['omega','heading_deg','A','B','A_inf','C','RAO','reference_point',
out     'C_source','metadata','body_labels']
judge  NO displaced volume, NO centre of buoyancy, NO buoyancy force. `C_source` says
       the restoring is buoyancy-only; a stiffness is not a load. So the static part
       is not in the database either, and your refusal to synthesise it from the
       deck's weights was the right instinct about the wrong rule.
```

**(3) SO WHY THE STOP IS WRONG: THE LOCKED SCHEMA AND THE LOCKED PLAN BOTH ALREADY SAY
THIS, AND BOTH ALREADY SAY WHO BUILDS THE STATIC PART. IT IS FLOATFEA.**

```
cmd    grep -n "load channel" docs/load-interchange-v1.md
out    :618  | `gravity` load channel | Computed in FloatFEA from the FE mass
out           distribution -- the one load source FloatFEA knows better than
out           FloatSim, which carries a lumped placeholder. | F1 sec.3 |
out    :619  | `hydrostatic` load channel | Gravity and buoyancy cancel inside `C`
out           at xi=0 upstream. `C` is a restoring *derivative*, not a load, so
out           there is no pressure field in it to extract. Recomputed in FloatFEA
out           from hull geometry, **on the MEAN wetted surface** | Q1, **G4.6** |
cmd    sed -n 670,674p docs/load-interchange-v1.md
out    "Adding a `hydrostatic` pressure channel breaks G4.6's mean-wetted-surface
out     constraint; adding `gravity` reintroduces a lumped placeholder in place of a
out     computed distribution. BOTH WOULD READ AS IMPROVEMENTS TO SOMEONE WHO HAD
out     NOT READ THIS TABLE -- which is why the table exists."
cmd    sed -n 326,332p PLAN.md
out    "Gravity and hydrostatic cancel inside `C` at xi=0 upstream, so neither can be
out     extracted from it -- `C` is a restoring derivative, not a load. Both are
out     therefore reconstructed independently in FloatFEA: gravity from the FE mass
out     distribution, buoyancy from the hull geometry. This gate is what confirms the
out     reconstruction matches the model that generated the motions."   (G4.6)
cmd    sed -n 303,304p PLAN.md
out    "Inertial loads distributed by the FE mass matrix. Self-equilibrium verified."
rule   every citation resolves, checked mechanically
judge  YOUR SECTION 6a FINDING IS THE LOCKED SCHEMA'S OWN SENTENCE, REDISCOVERED FROM
       THE SOLVER SIDE AND WITH BETTER EVIDENCE. The decision that the static part
       does not come from FloatSim was taken at Q1 and at F1 sec.3. Section 6a's ways
       out (1) and (2) are both the thing line 670 forbids without reopening that
       decision, and line 670 predicted the very sentence that would be written.
       **"Inventing the static part from the deck's weights is exactly the load this
       repository forbids" is the one place I think you went wrong.** `Never invent a
       load distribution` is about a record with no strip resolution being given an
       assumed one. Gravity from the FE mass matrix is not assumed, it is the plan's
       own instruction at `PLAN.md:303`, it has G4.3 and G4.6 as its gates, and it is
       the ONE source the schema says FloatFEA knows better than FloatSim.
```

**(4) AND EJ4(b) IS FORMABLE TODAY. I FORMED IT. NO EXPORT, NO HSP CHANGE.** You are
right that `mu` is not on `IntegrationResult` -- I read
`floatsim/solver/newmark.py:109-137` and it carries `t, xi, xi_dot, xi_ddot, lam` and
nothing else. But `mu_n = sum_k K_k @ xi_dot_{n-k} * dt` and BOTH halves are in process
in your own script: `setup.kernel` and `res.xi_dot`. `A_inf` is inside
`setup.lhs.M_plus_Ainf`. I reproduced the SOLVER'S discretisation, not the textbook
one:

```
claim  the inertia term cannot be formed, so EJ4(b) cannot be answered
cmd    report_joint_reactions.solve_one(1.9799, 40.0, 0.01) -- your own function,
         unmodified -- then rebuild mu with RadiationConvolution(setup.kernel) pushed
         over res.xi_dot, and form the residual of the system newmark.py:414-437
         actually solves: A_eff a_{n+1} - G(mid)^T lam_{n+1} - rhs, with
         A_eff = (1-alpha_m) M + (1-alpha_f) h^2 beta C and rhs assembled term by
         term including the lagged mu_n and the lagged F_state
out    |mu|_inf over the window                                4.085851e+00 N
out    EXACT DISCRETE residual, worst over the last 100 steps   1.257436e-04 N
rule   reproduce the solver's discretisation: verify against the rule the code runs,
       not the textbook rule
judge  THE IDENTITY CLOSES. `1.257436e-04 N` against terms of 10 to 85 N is the KKT
       solve's own residual. EJ4(b) is ANSWERED and the answer needed nothing
       exported. The claim "closing the identity needs the per-body added-mass matrix
       and the memory state at that step, and NEITHER IS EXPORTED" is wrong in both
       halves for the purpose it is put to: `A_inf` is in the hydro database
       (`docs/load-interchange-v1.md:88`, "A_inf . xi_ddot is reconstructed from the
       hydro database and /kinematics") and `mu[N,6]` is ALREADY A REQUIRED CHANNEL of
       the v1 schema (`:87`). So way out (3) is not a new ask either -- it is F4's
       first item as already specified.
```

```
cmd    the CONTINUOUS per-body form EJ4(b) literally asks for, same step, t = 40.000 s
out    body       |M a|       |mu|     |C xi|  |applied| |G^T lam|   |resid|    rel
out    buoy1  3.4965e+01 1.0798e+00 1.6338e+01 8.4255e+00 2.8356e+01 2.2427e-01 6.4e-03
out    buoy8  3.2172e+01 1.8630e+00 1.2302e+01 3.1030e+01 1.4827e+00 8.4227e-01 2.6e-02
out    hub1   1.9283e+01 0.0000e+00 0.0000e+00 0.0000e+00 1.9247e+01 3.6404e-02 1.9e-03
out    platfm 1.6087e+01 0.0000e+00 0.0000e+00 0.0000e+00 1.6061e+01 2.6365e-02 1.6e-03
out    worst per-body relative residual                                     2.618e-02
out    and buoy2's |G^T lam| row reads 1.3091e+00 -- your figure, reproduced exactly
rule   a residual destroys information: report the terms beside the norm
judge  THE CONTINUOUS FORM IS 2.618e-02 RELATIVE AND THE DISCRETE FORM IS
       1.257436e-04 N, AND THE GAP IS THE POINT. `newmark.py:48` documents
       `mu_{n+1-alpha_f} ~= mu_n` as an O(h) lag; `docs/load-interchange-v1.md`
       sec.4.1-4.2 is written about exactly this and chooses the discrete form so
       that "G4.1 finally means what it says". EJ4(b) asked for the textbook
       identity; the schema had already specified the one that closes.
judge  **AND THE STRUCTURAL ROWS ARE YOUR OWN FINDING, SHARPER:** hub1 has |mu| = 0,
       |C xi| = 0, |applied| = 0, and carries `1.9247e+01 N` of joint reaction against
       a weight of 12.0 * 9.81 = 117.7 N. Four hubs and a platform, 568.98 N of
       weight, appearing nowhere in the balance. That is a better sentence for a
       reader than a ratio on one buoy row, because it needs no denominator.
```

## Carried

Verdict 86 named three blocking items by name for F4 (R643, R638, R637 clause (iii)),
one non-finding (R644), and nine closure items plus the carried ledger. Every one.

* **R643 -- ANSWERED, and I verified it the way the condition was written.**

```
cmd    git grep -n SUITE_LINE_PLACEHOLDER -- docs/reports/F3/step-3.md
out    :951   revision 2's section 11, the published record -- correct to leave
cmd    the newest revision's own suite line
out    :1356  **Whole suite at `b7c05e7`: 2901 passed, 18 failed, 1 skipped.**
cmd    python -m pytest ...::test_the_report_carries_a_WHOLE_SUITE_count -q
out    1 passed
judge  CLOSED. Every one of the eighteen is named in a `- **failed**` bullet, each
       traced, and the figure is the one from my own run at `b7c05e7` rather than
       assembled. The refusal to hand-assemble it was right and it is now a real
       measurement. R637 clause (iii) is the same OBJECT and it is NOT met -- see
       R648, which is a different red from the one R643 named.
```

* **R638 -- OPEN, and EJ1 has moved its sequencing rather than its substance. I accept
  the move and I record what it cost.** EJ1 writes it at all three sites: worked in
  F4, closed before F4 closes, does not block F4's opening. CZ0's own sentence is
  "stays blocking there", which read literally would hold F4 step 1 on it. EJ1 is a
  directive and it governs; what it changes is WHEN, not WHETHER. **The one thing I
  will not accept is a third recording.** `floatfea/tolerances.py:394-398` and
  `docs/closure/F3.md:139-142` both now read the F4 wording and the report's section
  9b row agrees, so **C121 is CLOSED**.
* **R644 -- ANSWERED AND ADOPTED, in a standalone `process:` commit, and I read every
  line of it.** See `## My own instructions` below. `66af185` is byte-identical in
  `CLAUDE.md` and `docs/SUPERVISOR.md` and touches nothing else. **And the commit
  message says it wrote `1288` from no run and corrected it unpushed.** That is CP3
  being applied by the implementer to the commit adopting CP3's neighbour, and saying
  so in the message is worth more than the slip cost.
* **R637 clauses (i) and (ii) -- CLOSED at verdict 86 and staying closed.**
* **R639, R624, R630, R632, R633, R634, C101, C104, C105 -- CLOSED and I do not reopen
  them.** The diff over `tests` and `floatfea` touches no assertion and no value; the
  only file is `floatfea/tolerances.py` and the only change in it is comment.
* **R631, R626's residue, R635 -- LEDGERED, accepted, unchanged, not re-reviewed.**
* **C118 -- CLOSED, and I reproduced it rather than taking it.**

```
cmd    git show SHA:docs/reports/F3/step-3.md piped to grep -o of the R629 sentence
         "verdict 83's one red, was answered at", counted per commit
out    95f6293 -> 1    b7c05e7 -> 3    aec96e0 -> 1    6083a87 -> 1
judge  the doubling is gone and the editing step is a replace. This was the one that
       doubled every round it was left, so closing it first was right.
```

* **C113, C115 to C117, C120, C122, C123 -- LEDGERED at `docs/closure/F3.md` section 8
  per EJ3, as I asked. C119 is routed to F4 step 1's first commit as a (c), and I
  agree with both the routing and the single exception.** The ledger literally carries
  the row that demonstrates C119 -- `| R637 | R634-docs/closure/F3.md |` -- which is
  the honest way to publish a generator defect.
* **C102, C103, C106 to C112, C114, C88, C86, C90 to C98, C100, C74, C76, C78, C82,
  C85, R610, R615 -- carried unchanged, no work asked, not re-reviewed. C89 withdrawn.
  C40, C75, C75b, C99 -- `black --check` and `mypy` are GREEN at this commit; `ruff`
  is the one that is not, and that is R647.** R622 is F4's own.

## Findings

**R645. (RULING ON A STOP. NOT (a) to (d), AND IT OUTRANKS EVERYTHING ELSE IN THIS
ROUND. EJ4's STOP IS WITHDRAWN.) F4's LOAD MAPPING IS NOT BLOCKED, AND THE DECISION
EJ4 SENDS TO XABIER WAS ALREADY TAKEN AT Q1 AND AT F1 SECTION 3.**
The physics in section 6a is right and better evidenced than the documents that
duplicate it. What is wrong is the conclusion. Three measurements, each above with its
command: `solve_equilibrium=True` changes nothing (`|xi0_true - xi0_false|_inf = 0`),
so way out (1) is empty; the equilibrium reaction on this deck is identically zero, so
way out (2) exports a zero; and `docs/load-interchange-v1.md:670` forbids both without
reopening a locked decision. The static part was always FloatFEA's to build --
`PLAN.md:326-332`, gravity from the FE mass distribution and buoyancy from the hull
geometry on the mean wetted surface, with **G4.6 as the gate that proves the
reconstruction against FloatSim's own `C`**.
**Closed when** `docs/closure/F3.md` section 6a and
`scripts/report_joint_reactions.py:217-234` say what was measured and stop saying what
must change outside FloatFEA -- site by site: (i) that the static reaction is zero BY
CONSTRUCTION and not merely unexported, with the `solve_equilibrium` ablation as the
proof; (ii) that `gravity` and `hydrostatic` are section 7 locked-out decisions which
G4.6 already routes; (iii) that the sentence "F4's export has to carry the equilibrium
reaction as well as the history" is DELETED, because that reaction is `0`; and (iv)
that the "inventing the static part" sentence is withdrawn. **No new apparatus and no
HSP change is needed for any of it.** Classed a closure item under CZ0 because it is
prose -- but it is the prose that stopped the critical path, so it is first on the
list.

**R646. (NOT BLOCKING. Same head as R645, recorded separately because it is a
different claim.) EJ4(b) IS ANSWERED, NOT BLOCKED: THE RESIDUAL CLOSES TO
`1.257436e-04 N` FROM QUANTITIES ALREADY IN PROCESS.** `mu` is reconstructible from
`setup.kernel` and `res.xi_dot`, `A_inf` is inside `setup.lhs.M_plus_Ainf`, and both
are schema-declared sources (`docs/load-interchange-v1.md:87-88`). The continuous form
EJ4(b) names reads `2.618e-02` relative, and that gap is the documented O(h) lag on
`mu_n` -- the schema's section 4.2 chose the discrete form for precisely this reason.
**Closed when** the script's closing paragraph carries the discrete residual it can
actually form, with the lag named, instead of the sentence saying the identity cannot
be closed.

**R647. (d, BLOCKING) `ruff check floatfea tests` IS RED AT THE REVIEWED COMMIT AND IN
CI, AND `black`, `mypy`, `unit tests` AND `guards and meta-tests` ARE ALL SKIPPED
BEHIND IT.**

```
cmd    python -m ruff check floatfea tests, clean clone at 6083a87
out    E501 Line too long (126 > 100) --> floatfea/tolerances.py:398:101
out    Found 1 error.
cmd    awk length on that line
out    398:126:# opening. The measurement above is what a reader needs until then:
out            this ceiling is not guarded at the strength the gate is.
cmd    grep -n "line-length" pyproject.toml
out    89:line-length = 100  [tool.black]      93:line-length = 100  [tool.ruff]
cmd    git log --oneline -1 -S on that comment text -- floatfea/tolerances.py
out    c9902d3 closure: EJ1 settles C121, EJ3 ledgers the rest (F3)
cmd    gh run view 36998118365, the lint job's steps
out    6 ruff FAILURE; 7 black SKIPPED; 8 mypy SKIPPED; 9 unit tests SKIPPED;
out    10 guards and meta-tests SKIPPED
rule   CZ1 (ii) and (iii): a closure commit is verified AFTER it exists, and the
       pasted gh run list exists so that the guards step is SEEN TO HAVE RUN
judge  THIS IS CZ1's OWN SUBJECT, SHIPPED TWICE. `pytest` does not run `ruff`, so the
       implementer's loop cannot see it; CZ1 (ii) is the step that would have, and no
       `ruff` output was pasted for `c9902d3` or for `6083a87`. The damage is not the
       lint: it is that CI has given NO reading on the suite at either commit, so my
       clone is the only instrument and CA2's whole premise is gone.
```

**Closed when** line 398 is wrapped at 100 columns in a commit that changes no
tolerance value, and the four CZ1 (ii) outputs plus a `gh run list --commit SHA` with
job-level conclusions are pasted, with the lint job's `guards and meta-tests` step
SEEN TO HAVE RUN.

**R648. (d, BLOCKING) THE REPORT'S SECTION 0a RECORDS A COMPLETED FAILURE AS
`no result`, EIGHT REDS TRACE TO IT, AND IT IS ON NEITHER CARVE-OUT LIST.**

```
cmd    python -m pytest tests/test_report_carried.py::test_the_CI_TABLE_agrees_with
         _gh_FOR_EVERY_ROW -q, clean clone at 6083a87, origin pointed at the real
         repository so gh can resolve it
out    1 failed -- run 36997601588: the table says no result, status in_progress;
out    gh says failure
cmd    the baseline of test_the_guard_survives_the_state, its own failure line
out    "1 failed, 220 passed in 5.16s", and the one failure is the SAME test
cmd    the seven cascading states
out    each fails on the red baseline, not on its own subject
rule   EG3's sharpening: state (2) is cleared BY THE ANSWERING REPORT. Revision 3 IS
       the answering report, it is in the tree, and this is still red
judge  NOT THE BOUNDARY. CZ1 (iv) unchanged, and the report itself rules it that way
       at `docs/reports/F3/step-3.md:585`, which I credit. And it is not cosmetic:
       the run the table calls no result is `c9902d3`'s -- the run that would have
       shown R647. A guard built to catch "the CI record in the report not being the
       CI record" caught exactly that, on the one row where it mattered.
judge  ONE FIX CLEARS EIGHT. And I checked the thing that would make it unfixable: it
       is NOT a deadlock. `scripts/ci_section.py --rounds` regenerated as the LAST
       edit before the commit (CP3's own ordering) gives a table that agrees with gh
       for every COMPLETED run; the row for the report's own push reads in_progress
       on both sides while CI runs, which is why this test passed on CI at `b7c05e7`
       and fails in a clone taken after the run completed.
```

**Closed when** section 0a is regenerated by `python scripts/ci_section.py --rounds`
after R647's fix is pushed and its run has completed, and a run of
`tests/test_report_carried.py` and `tests/test_report_guard_states.py` reads
`0 failed` in a clone whose `origin` resolves -- or, if a row cannot be made to agree,
the disagreement is stated as a finding about the guard rather than left red.

## Closure items

Named, not re-reviewed, none of them holding anything. Absorb the whole list in ONE
commit and verify it AFTER the commit exists (CZ1). **R645 is first.**

* **C124.** `docs/closure/F3.md` heading order is `4b, 8, 6, 6a, 7`: EJ3's section 8
  was inserted ahead of section 6 and section 6a ahead of section 7. A reader
  following the numbers reads the ledger before what carries into F4. **Closes when**
  the sections are in numeric order, or section 8 is renumbered to where it sits.
* **C125.** The hand-back's `Report guards: 320 passed` does not reproduce and cannot:
  the three report-guard files collect **281** tests at `b702f15`, `d4b89e0` and
  `6083a87` alike, and my own run of them at `6083a87` is `8 failed, 273 passed`. 320
  is above the ceiling of that selection, so the figure is of a different set.
  **Closes when** the figure names its selection or is retaken. CP3's class again.
* **C126.** EJ0's `12x` is half-measured by its author's own admission and the
  measured half does not reproduce on my instrument: the same three files at the same
  commit took `246.93s` in a clone under the local temp, against the hand-back's
  `67.49s` in a clone and "over thirteen minutes" in the synced tree. A ratio whose
  numerator and denominator come from different machine loads is not a ratio.
  **Closes when** both halves are taken back to back on one machine, or the figure is
  withdrawn and verdict 86's `1.84x` -- which WAS taken that way -- stands alone.
* **C127.** `scripts/report_joint_reactions.py:217-234` is an eighteen-line printed
  paragraph making claims about what is and is not exportable, three of which R645 and
  R646 refute. CW0: a claim about this repository in the source tree is a test, a
  triple, or deleted. **Closes when** it is one of those three.
* **C128.** `docs/reports/F3/step-3.md:1310` section 10 still reads "EH6 -- not
  started" while the hand-back says EH6/EI3 is scripts-only and started. This is C123
  unclosed and now a round older. **Closes when** the two agree.
* **C129.** EJ5's plan draft and EJ6's dates are not written, on the ground that EJ4
  says stop. R645 withdraws that ground. **Closes when** they are written, or the
  schedule paragraph says which date they are measured against and whether it holds.
* **C113, C115, C116, C117, C119, C120, C122, C123** -- as EJ3 ledgers them, C119 to
  F4 step 1's first commit as a (c). **C102, C103, C106 to C112, C114, C88, C86, C90
  to C98, C100, C74, C76, C78, C82, C85, R610, R615** -- carried unchanged. **C89**
  withdrawn. **C40, C75, C75b, C99, C101, C104, C105, C118, C121** -- CLOSED.

## Tolerances touched

```
cmd  git diff b7c05e7..6083a87 --numstat -- floatfea/tolerances.py
out  5  2
cmd  the same diff, lines matching a NAME: Final[float] = value declaration
out  (no output) -- NOT ONE VALUE LINE CHANGED, in either direction
cmd  git diff b7c05e7..6083a87 -- "tests/regression/*" tests/conftest.py
out  (no output) -- no golden moved, no parametrisation loosened, no conftest
cmd  git diff b7c05e7..6083a87 --stat -- tests floatfea
out  floatfea/tolerances.py | 7 +++++--
out  1 file changed, 5 insertions(+), 2 deletions(-)
out  AND NOTHING ELSE UNDER EITHER TREE
judge  NO TOLERANCE WAS TOUCHED AS A VALUE AND NO ASSERTION MOVED THIS ROUND. The
       entire diff under `floatfea/` and `tests/` is two comment lines becoming five
       in one entry -- and one of those five is R647.
```

| constant | value | form | counter | justification located |
|---|---|---|---|---|
| `RIGID_MODE_EXACTNESS` | `1e-15`, UNCHANGED | relative and dimensionless; correct form | **STILL NONE.** `1e-13` gives `1802 passed, 0 failed`; the solved edge is `3.783782e-12`; `3784x`, which I re-measured myself at `b7c05e7` and which nothing since has touched | `floatfea/tolerances.py:330-400` and `docs/closure/F3.md` section 4a, both now reading EJ1's F4 wording. **R638 is worked in F4 and closes before F4 closes.** |
| `PLATFORM_RIGID_MODE_EXACTNESS` | `1.154338e-18`, UNCHANGED | unchanged | unchanged; the roof assertion from verdict 86 is untouched, silent rise still `1.63x` | `floatfea/tolerances.py:453-473`; not in this round's diff. |
| `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | `1.0e-14`, UNCHANGED | unchanged | unchanged; upper edge still solved at `3.09x` | `floatfea/tolerances.py:423-446`; not in this round's diff. |
| `RIGID_MODE_BOUND` | `199.526231496888`, UNCHANGED | unchanged | unchanged | unchanged. **R631** is its open residue, ledgered under DZ7c. |

## My own instructions (4b), read line by line

```
cmd  git diff b7c05e7..6083a87 --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out  CLAUDE.md 25 +++++-----, docs/SUPERVISOR.md 25 +++++-----
out  2 files changed, 40 insertions(+), 10 deletions(-)
cmd  git log --oneline b7c05e7..6083a87 -- .claude docs/SUPERVISOR.md CLAUDE.md
out  66af185 process: R644 -- two carve-out placements corrected (EJ2)
cmd  git show 66af185 --name-only
out  CLAUDE.md, docs/SUPERVISOR.md     AND NOTHING ELSE
cmd  the ten deleted lines, read one by one
out  all ten are the EH1 paragraph being REWRITTEN, not removed: the two-list
out  sentence loses `test_the_answered_verdict_is_the_NEWEST_one` from state (1)'s
out  side and gains it, plus `test_a_carried_row_points_at_a_section_that
out  _discusses_it`, on state (2)'s. NO GUARD IS DELETED AND NOTHING IS WEAKENED --
out  state (2)'s list GROWS BY TWO and state (1)'s shrinks by one, which is strictly
out  more reds traced by name and strictly fewer waived as the boundary. The added
out  block is R644's measurement, in my own wording, unparaphrased.
judge  NO STOP-CLASS PROCESS FINDING. A standalone `process:` commit citing EJ2 by
       name, touching no `floatfea/` and no `tests/`, identical in both files. I
       verified that identity by diffing the two added blocks against each other, not
       by reading the subject line. Nothing I am instructed to carry has gone.
```

## The adversarial corpus (BE3)

**BATCH 32, committed separately at `c834593`:
`tests/corpus/f4_static_dynamic_reaction_split.txt`, 12 entries, all new.**

```
cmd  grep -c "^id=" tests/corpus/f4_static_dynamic_reaction_split.txt
out  12
cmd  git log --oneline -1 -- tests/corpus
out  c834593 corpus: batch 32 -- the static part of a joint reaction
cmd  grep -rln f4_static_dynamic_reaction_split tests/ scripts/ floatfea/
out  (no output) -- NOTHING READS IT
rule  EG4(e): batches pause after F3 step 3 EXCEPT mutation work on F4's
      load-mapping gate. This is that surface and nothing else.
```

**New entries this round: 12. Caught by the implementer's checks: 0 of 12, and the
reason is that there is no check -- no shipped file reads this corpus at `6083a87`, as
the command above shows. I am recording that as the coverage number rather than
dressing it up.** The entries are not about the case you found. They are the twelve
where the static part is **present and wrong**: a reconstruction at the wrong
waterline that is self-equilibrated and clean on G4.1 while every member carries the
wrong axial; a static part added by BOTH the export and the reconstruction; a per-body
resultant that balances and therefore cannot show that one source never arrived; and
the equilibrium row that is exported and is identically zero. Those are the shapes the
hand that writes the mapping would not choose, and nine of the twelve exist as
candidates only because of what section 6a measured.

**The method note, which is this round's transferable lesson and is not about the
element.** The two findings that mattered came from one habit each. **When a report
says a thing cannot be formed, form it** -- `mu` is genuinely not on
`IntegrationResult`, the dataclass was read correctly, and it is a deterministic
function of two things the same script already holds. **And when a report says a
decision must go outside the repository, grep the locked documents for the decision
first** -- `docs/load-interchange-v1.md:670` had not only taken it but written down in
advance the sentence that someone who had not read it would write.

## On the criterion

**I ruled under CZ0 and I have one thing to say about it, once, and it is not a
complaint about the criterion.** Two of this round's four findings block under (d) and
both are one-line fixes. The two that matter -- R645 and R646 -- are **prose**, and
under CZ0 they are closure items that I am instructed not to hold on. I have classed
them that way and I am not holding on them. But **a false sentence in a closure
artifact stopped F4's critical path**, which is the first time this milestone that the
retired blocking head would have caught something costing schedule rather than
attention. I am not asking for the head back; six rounds measured it not paying. I am
recording the one counter-example so that the next time it is weighed, this round is
in the sample. **That goes to Xabier through the implementer and it is not another
round.**

**And the EB4 reading: I agree. This round counts against no step.** Step 3's three
rounds are 84, 85 and 86; this is the eighty-seventh and its subject is the tree and a
STOP whose resolution the hand-back correctly routed out of the loop. **EJ1's
relaxation of CZ0's "stays blocking there" to "closes before F4 closes" is a loosening
of the cap's teeth** and I accept it as a directive, noting only that it is the second
mechanism this milestone to move in that direction.

## Next step opens when

**F3 STEP 3 IS CLOSED AT PASS (DD1) AND F3 IS CLOSED. THIS VERDICT DOES NOT REOPEN
EITHER, AND A VERDICT WRITTEN BY HAND IS HOW THE DISPOSITION IS RECORDED WHEN THE HOOK
AND DD1 DISAGREE.** What is held is **F4 step 1's FIRST COMMIT**, and the conditions
are two reds and nothing else:

1. **R647 -- WRAP `floatfea/tolerances.py:398` AT 100 COLUMNS.** No value changes.
   Then, at that commit, tree clean: `ruff check floatfea tests`,
   `black --check floatfea tests`, `mypy floatfea`, `pytest -q`, pushed, and
   `gh run list --commit SHA` with the job-level conclusions, so the lint job's
   `guards and meta-tests` step is SEEN TO HAVE RUN. That is CZ1 (ii) and (iii) in
   order, and it is the step that was skipped at `c9902d3` and at `6083a87`.
2. **R648 -- REGENERATE SECTION 0a AFTER THAT RUN COMPLETES**, with
   `python scripts/ci_section.py --rounds` as the LAST edit (CP3), and read `0 failed`
   on `tests/test_report_carried.py` and `tests/test_report_guard_states.py` in a
   clone whose `origin` resolves. One fix clears eight.
3. **THEN F4 OPENS, AND IT OPENS UNBLOCKED.** R645 withdraws EJ4's STOP. **Write
   EJ5's plan draft and EJ6's dates.** The static part is FloatFEA's to build --
   `PLAN.md:326-332` and `docs/load-interchange-v1.md` section 7 -- so F4 step 1 maps
   the dynamic reaction from `res.lam` AND reconstructs gravity from the FE mass
   distribution and buoyancy from the hull geometry on the mean wetted surface, with
   **G4.6 as the gate that proves the reconstruction against FloatSim's own `C`**. The
   additive HSP writer carries `res.lam`, the per-body external force and `mu[N,6]`,
   all three of which the schema already requires; it does **not** carry an
   equilibrium reaction, because that reaction is `0`.
4. **F4's `Carried` carries R638 BY NAME** (worked in F4, closed before F4 closes, per
   EJ1), **R637 clause (iii)** (whose object is now R648 and no longer R643), and
   **R645, R646, R647 and R648**, with the closure list C124 to C129 plus EJ3's
   ledger.
5. **C119 in F4 step 1's first commit**, as EJ3 routes it -- a generator that
   misreports a site is (c), and I agree.

**Schedule.** F3 closed 1 October, twelve days inside its 13 October date. F4 19
October, the member-force table 23 October, the code-check screen 28 October. **I have
one measurement that bears on them and it moves a date the right way:** EJ4's STOP was
holding F4's critical path, R645 releases it, and the release costs nothing outside
FloatFEA. CZ0's escalation stays live -- two consecutive steps closed carrying items --
but I still read neither a slip nor a scope cut as needed, and now with one fewer
reason to think otherwise. **And EH6 is less of a risk than it was being treated as:**
one case at `T = 1.9799 s`, `40 s`, `dt 0.01` ran in `5m48.6s` in the synced tree and
in about the same in my own call of `solve_one`, so six of them is under an hour. That
is the first actual number anyone has on it, and it is the hand-back's, not mine.

**One sentence for the implementer.** You asked me to check the reasoning rather than
the arithmetic, you named the exact condition that would make you wrong, and you were
right about the physics and wrong about the consequence -- which is the most useful
shape a STOP can have, because every measurement in it is load-bearing for the work
that now proceeds; the thing to take from it is that the decision you were about to
send out of the loop had already been taken and written down, in two files you had not
grepped.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 3
Reviewed commit: b7c05e7714ab030780ddd3992dc269738513be6a
Verdict: PASS
**Reviewed commit: `b7c05e7`.**  (HEAD of F3, pushed, `F3 == origin/F3`. I committed no corpus batch this round, so HEAD at write time IS the judged commit.)
Tests: 2901 passed, 18 failed, 1 skipped   (MY OWN run, ONE invocation, no exclusion, clean clone at `b7c05e7`, 1245.47s. ONE of the 18 is MY OWN artifact and I withdraw it below: CI at the same commit names SEVENTEEN and not that one. The tree's red set is 17.)

## Round of 2026-10-01 -- EIGHTY-SIXTH verdict, ROUND 3 OF 3 ON STEP 3. THE STEP CLOSES AND F3 CLOSES.

**THE SUITE LINE IS NOT A BLOCKER ON THE TREE, IT IS A BLOCKER ON ONE MACHINE, AND I
MEASURED WHICH.** The whole suite runs at this commit in ONE invocation in 20m45s and
the main half is GREEN. The reason the implementer could not take it is the filesystem,
not the suite: same commit, same selection, same machine, only the location moved --
`216.86s` in a clone under the local temp against `399.16s` in the OneDrive-synced
working tree, `1.84x`. At that factor the whole tree is ~38 minutes where the
background limit is 30. **The figure is below, the commands are named, and revision 3
may carry it.**

**THE THREE REPAIRS ARE RIGHT AND I MEASURED EVERY ONE IN THE DIRECTION THAT WEAKENS
IT (EH4).** R639's bound turns eight decades into `3.09x`; EH2(c)'s roof turns `8.7x`
of silent ceiling rise into `1.63x`; R638's recorded figures reproduce EXACTLY at the
commit that publishes them, which is the first CP3 pass this milestone has had on a
figure that mattered. I also ran the two-variable attack neither of us had: both
constants moved together, the rung stays green at ceiling `x1.63` AND injection `x3.0`.

**ONE RED BLOCKS AND IT CARRIES: `test_the_report_carries_a_WHOLE_SUITE_count`.** It is
red at `b7c05e7` and it is still red with revision 3 in the tree, because
`SUITE_LINE_PLACEHOLDER` is still at `docs/reports/F3/step-3.md:1354`. It is CZ1 (iv)
and it is (d). Three blocking items carry into F4 by name.

## THE TREE AT b7c05e7, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse F3 && git rev-parse origin/F3
out    b7c05e7714ab030780ddd3992dc269738513be6a   all three
cmd    git status --porcelain --untracked-files=all
out    M docs/reports/F3/step-3.md
judge  REVISION 3 IS UNCOMMITTED, as the hand-back says. At the reviewed commit the
       report is revision 2 and its header reads `Answers: verdict 84 @ 8368c51`,
       so ITEM 1b FAILS AT THIS COMMIT -- and it fails differently from last round:
       FIVE commits landed after verdict 85, TWO of them edited the report file, and
       the header was not moved. That is what
       `test_the_answered_verdict_is_the_NEWEST_one` says in words:
       "the report at `3fdfc79` is newer than the verdict at `f2fa598` and names
       `8368c51`". I rule the substance on revision 3 as it stands in the working
       tree, which DOES read `Answers: verdict 85 @ f2fa598`, and I record the
       commit's own state as red.
cmd    git log --oneline 95f6293..HEAD --name-only
out    b7c05e7  docs/closure/F3.md, scripts/suite_count.py,
out             tests/test_report_guard_states.py
out    24e8bb2  docs/reports/F3/step-3-answers.json, tests/test_report_carried.py,
out             tests/verification/rung3/test_platform_rigid_modes.py
out    3fdfc79  docs/closure/F3.md, docs/milestones/F3.md, the report + answers,
out             floatfea/tolerances.py, tests/test_report_guard_states.py,
out             tests/verification/rung3/test_platform_rigid_modes.py
out    4e91284  CLAUDE.md, docs/SUPERVISOR.md          <- AND NOTHING ELSE
out    31cd0db  docs/closure/F3.md, the report + answers, floatfea/tolerances.py,
out             tests/test_report_guard_states.py,
out             tests/test_report_numbers_are_sourced.py,
out             tests/verification/rung3/test_platform_rigid_modes.py
cmd    git diff 95f6293..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (no output)
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py        CI0: the pathspec resolves to a real file
cmd    grep -nE "pytest_runtest_makereport|pytest_ignore_collect|
         pytest_collection_modifyitems|hookwrapper|items.remove|pytest_plugins"
         tests/conftest.py
out    53: pytest_collection_modifyitems  -- AND I READ IT (CH2). It adds a rung
out    marker from the directory and sorts by rung. It REMOVES NOTHING, writes no
out    outcome, and there is no makereport hook, no ignore_collect, no plugin
out    loaded from tests/, and no rung carries its own conftest.
cmd    python -m pytest -q, clean clone at b7c05e7, one invocation
out    18 failed, 2901 passed, 1 skipped in 1245.47s (0:20:45)
```

## CI AT THE REVIEWED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit b7c05e7714... --json databaseId,conclusion,status
out    36964000628  completed  FAILURE
cmd    gh run view 36964000628 --json jobs, job by job
out    the verification ladder            SUCCESS   13 steps  04:18:48 -> 04:22:10
out    lint, unit and guards              FAILURE   14 steps  04:18:48 -> 04:29:33
out    CI determinism -- leg              skipped    0 steps
out    CI determinism -- ten legs agree   skipped    0 steps
cmd    the lint job's steps, by number and conclusion
out    5 actionlint SUCCESS, 6 ruff SUCCESS, 7 black --check SUCCESS, 8 mypy
out    SUCCESS, 9 unit tests SUCCESS, 10 "guards and meta-tests" FAILURE
judge  NOT CK2: thirteen and fourteen real steps, real durations, no spending
       annotation, no runner-never-started. The two skipped jobs are CK0's
       workflow_dispatch gate, UNAVAILABLE BY DECLARATION, as at verdicts 79 to 85.
       `ruff`, `black --check` and `mypy` are GREEN on a machine neither of us
       controls, and "guards and meta-tests" is SEEN TO HAVE RUN rather than been
       skipped behind an earlier red (CZ1 iii), so I did not re-run them.
       THE LADDER IS GREEN AT THIS COMMIT, ALL SIX RUNGS. NO LOW RUNG IS RED, SO
       NOTHING HERE IS A STOP.
cmd    gh run view 36964000628 --log-failed, the FAILED ids, deduplicated
out    17
judge  CI IS RED AT THE REVIEWED COMMIT AND I RECORD IT AS RED.
```

**MY EIGHTEENTH RED IS MINE AND I WITHDRAW IT.**
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` failed in my clone and does not fail
on CI. One variable, everything else held:

```
cmd    the failure text, in my clone
out    run 36900722535: `gh run view` returns nothing -- no such run
cmd    gh run view 36900722535 --json databaseId,conclusion,headSha, in the REAL
         repository
out    {"conclusion":"failure","databaseId":36900722535,
out     "headSha":"a647492e99b59eec16b0b3faf2489867d2aab596"}   -- it exists
cmd    git remote set-url origin https://github.com/xabi80/FloatFEA.git in the
         clone, then re-run that test and its sibling
out    2 passed in 0.82s
rule   verify the reference: the reference has been wrong more often than the thing
       measured
judge  MY CLONE'S `origin` WAS A LOCAL PATH, SO `gh` COULD NOT RESOLVE THE
       REPOSITORY. The red is an artifact of my own apparatus, it is withdrawn, and
       the authoritative set is CI's 17. Recorded rather than quietly dropped,
       because a reviewer's instrument has been the defect more than once this
       milestone.
```

**THE EG3(i) TRACE, ALL 17 MATCHED BY NAME, NOT BY FAMILY.** This is EG3 state (2),
verdict written and the answering report not committed:

```
out     3 x test_every_named_site_is_touched_or_declared[R633-tests/
out           test_counters_are_injected.py:317, :318, :319]  -> (2), named
out     1 x test_the_Carried_table_is_what_the_generator_produces  -> (2), named
out     1 x test_the_generator_would_catch_a_row_under_the_wrong_number -> (2)
out     1 x test_the_CI_section_is_about_the_REVIEWED_commit      -> (2), named
out     1 x test_the_answered_verdict_is_the_NEWEST_one           -> on EH1's list
out     7 x test_the_guard_survives_the_state[baseline + non_numeric_step_suffix,
out           superscript_digit_step_number, draft_suffix_beside_a_step_report,
out           step_number_is_the_empty_string,
out           verdict_amended_after_the_commit_the_report_answers,
out           zero_padded_step_number]
out           -> the cascade: baseline RED, each cascading state's own line
out     2 x test_a_carried_row_points_at_a_section_that_discusses_it[R624->4,
out           R630->4]
out           -> ON NEITHER LIST. MEASURED TO BE STATE (2) ANYWAY, see below.
out     1 x test_the_report_carries_a_WHOLE_SUITE_count
out           -> ON NEITHER LIST AND NOT CLEARED BY THE ANSWERING REPORT. CZ1 (iv).
rule   EG3(i): the waiver applies only if EVERY red traces BY NAME to the
       step-boundary cause, and a red that does not match is CZ1 (iv) unchanged
judge  16 OF 17 ARE THE BOUNDARY OR ITS CASCADE. THE SEVENTEENTH IS R643 AND IT
       BLOCKS.
```

**AND I DID NOT RULE THE TWO UNLISTED ONES BY CLASS, WHICH IS WHAT EG3(i) EXISTS TO
STOP. I RAN THEM AGAINST THE ANSWERING REPORT.**

```
cmd    python -m pytest tests/test_report_carried.py::test_a_carried_row_points_at_a
         _section_that_discusses_it ::test_the_report_carries_a_WHOLE_SUITE_count
         ::test_the_answered_verdict_is_the_NEWEST_one
         ::test_the_CI_section_is_about_the_REVIEWED_commit -q
         IN THE WORKING TREE, where revision 3 exists
out    1 failed, 31 passed in 0.42s
out    the 28 pointer parametrisations: ALL PASS -- [R624->4] and [R630->4] gone
out    test_the_answered_verdict_is_the_NEWEST_one: PASSES (names verdict 85)
out    test_the_CI_section_is_about_the_REVIEWED_commit: PASSES (section 0 resolves
out      `95f6293`, so verdict 85's condition 1 IS met by revision 3)
out    the one failure: test_the_report_carries_a_WHOLE_SUITE_count
rule   EG3's sharpening: state (2) is cleared BY THE ANSWERING REPORT, not by time
judge  THE TWO POINTER ROWS ARE STATE (2) IN SUBSTANCE AND EH1'S LIST IS SHORT BY
       A NAME. The suite line is NOT: it survives the answering report, which is the
       discriminator the carve-out is built on. One command separated a cascade from
       a defect, which is exactly what the eighty-third verdict asked for.
```

**EG3(ii) IS CLEARED AND I TOOK IT AT THE VERDICT COMMIT.** The report-guard files run
at `b7c05e7` in a clean clone: `18 failed, 221 passed, 1 skipped in 185.64s`, pasted in
full below as the guards half.

## MY RULING ON THE SUITE LINE -- THE ONE THING THE HAND-BACK ASKED FOR

**(1) THE IMPEDIMENT IS REAL ON THAT MACHINE AND IT IS NOT A PROPERTY OF THE SUITE.**
I measured the cause with one variable moved:

```
claim  the main half cannot be measured on this machine
cmd    python -m pytest tests/verification tests/unit -q, clean clone at b7c05e7
         under the LOCAL temp
out    1802 passed in 216.86s (0:03:36)
cmd    the SAME selection, the SAME commit, the SAME machine, in the OneDrive-synced
         working tree
out    1802 passed in 399.16s (0:06:39)
cell   one variable: the filesystem location. Same interpreter, same commit, same
       1802 tests, same ordering, same selection.
rule   a causal claim carries its ablation
judge  1.84x. THE WORKING TREE IS INSIDE A SYNCED FOLDER. At that factor my 20m45s
       whole-tree run is ~38 minutes in the working tree and the 30-minute
       background limit is hit, twice, exactly as reported. `--half main` lands at
       ~32 minutes, which is why it stopped and why mine did not. THE REMEDY IS NOT
       APPARATUS: run `scripts/suite_count.py` from a clone outside the synced
       folder. I am not asking for a code change and none is needed.
```

**(2) THE FIGURE, AND IT IS STRONGER THAN `--half main`.** My run has NO exclusion, so
it is the whole tree in one invocation -- which is the property R309 exists to assert,
and `--half main` deliberately gives up:

```
cmd    python -m pytest -q, clean clone at b7c05e7, ONE invocation, no --ignore
out    18 failed, 2901 passed, 1 skipped in 1245.47s (0:20:45)
       and MINUS my own withdrawn artifact: 17 failed, 2902 passed, 1 skipped
cmd    python -m pytest tests/test_report_carried.py
         tests/test_report_numbers_are_sourced.py
         tests/test_report_guard_states.py -q, same clean clone, same commit
out    18 failed, 221 passed, 1 skipped in 185.64s        <- the guards half
cmd    the arithmetic, stated so it can be refused: 2920 collected in total, 240 in
         the three report-parametrised files
out    THE MAIN HALF IS 2680 passed, 0 failed, 0 skipped -- DERIVED, not run
judge  EVERY ONE OF THE 18 REDS IS IN ONE OF THE THREE REPORT-PARAMETRISED FILES.
       So the main half is GREEN at `b7c05e7` and the derivation cannot be hiding a
       failure: there is none outside those files to hide.
```

**(3) WHAT REVISION 3 MAY CARRY.** The whole-tree line, with both commands named --
mine and CI's -- and every failure named test by test. `_SUITE` at
`tests/test_report_carried.py:2182` matches
``Whole suite at `<sha>`: <n> passed, <n> failed, <n> skipped``, which my line has;
`test_the_report_carries_a_WHOLE_SUITE_count` asserts `passed > 100`; and
`test_every_FAILING_test_in_the_whole_suite_line_is_NAMED` needs one
``- **failed** `<id>` `` bullet per failure, so all of them are listed. **The sha the
line names is `b7c05e7`, not the revision-3 commit, and that is correct** -- the
commit-distance rule is retired under DR0 and the line names the commit the count was
taken at. The guards half goes beside it as its own line, at `b7c05e7`.

**(4) I RULE AGAINST TAKING THE LINE FROM THE CI SECTION'S JOB COUNTS.** EI0(b) makes
CI the cross-check and it is a good one, but no CI job is the whole suite in one
invocation: the work is split across two jobs, two more are skipped, and the lint job's
own count is of a partition. R309's subject is precisely that seven correct subsets
cannot see a failure in an eighth. A cross-check, yes. The line, no.

**(5) AND THE IMPLEMENTER'S GUARDS FIGURE IS ONE COMMIT STALE, WHICH IS CP3's OWN
SUBJECT.** The hand-back pastes ``The report-guard set at `24e8bb2`: 222 passed, 18
failed, 1 skipped``. At `b7c05e7` it is `221 passed`, because `b7c05e7` DELETED a
parametrised state. The number was right when taken and describes a different tree from
the one revision 3 ships at. Do not paste it; paste the `b7c05e7` one.

## Carried

Verdict 85 named three blocking items (R637, R638, R639), one non-finding (R640), and
fourteen closure items. Every one is below.

* **R637 -- ANSWERED, all three clauses, and clause (i) landed on the branch I named.**

```
cmd    clause (ii): git diff 95f6293..HEAD, the two rindex sites
out    tests/test_report_numbers_are_sourced.py:102 -> _REVISIONS = [m.start() for
out      m in re.finditer(r"^# Revision \d+", TEXT, re.MULTILINE)]; BODY = the LAST
out    tests/test_report_guard_states.py:545 -> the whole plant action is DELETED,
out      so the substring call is gone with it
judge  BOTH SITES CLOSED, one by the anchored form the other three readers use and
       one by deletion. The anchored guard found a real defect on its first run --
       the report says `1 failed, an unsourced figure in the ledger section it had
       been blind to` -- which is a repair proving itself rather than describing
       itself.
cmd    clause (i): the ablation, re-run at the CURRENT commit per my condition
out    WITH the plant 1 passed / WITHOUT 1 passed / restored 1 passed
judge  IT DOES NOT DIFFER, SO MY CONDITION'S OWN SECOND BRANCH APPLIES: the state is
       deleted under DR1 with its vacuity recorded. EI1 does that, the record is at
       `docs/closure/F3.md` section 4b and in a 29-line note at
       tests/test_report_guard_states.py:247, and the implementer declined to add it
       to `REQUIREMENT_CHANGED` on the correct ground that no measurement supports a
       declaration about what the repaired guard must do. I ACCEPT THE DELETION.
cmd    AND THE THING THAT DECIDES IT FOR ME, which neither of us planned: does the
         live assertion the state was supposed to guard still fail on real data?
out    YES, TWICE, ON CI AT THIS COMMIT --
out    test_a_carried_row_points_at_a_section_that_discusses_it[R624->4] and
out    [R630->4]: "R624 points at 4 and that section never mentions it"
rule   a gate carries its own failure: if the thing it claims were false, would this
       go red?
judge  THE TREE SUPPLIED THE NEGATIVE CONTROL THE PLANTED STATE COULD NOT. What is
       lost is narrower than "the class has no control": the shipped assertion is
       demonstrably able to fail, and what has no plant is the `section !=
       carried_heading` clause specifically. `docs/closure/F3.md` section 4b states
       exactly that and no more, which is the honest version. R637 CLOSED.
cmd    clause (iii): pytest -q and CI at the answering sha read 0 failed apart from
         EG3 state (1)
out    NOT MET -- 17 reds at b7c05e7, 16 of them the boundary and ONE not. R643.
```

* **R638 -- NOT CLOSED, BY A DECISION I OFFERED, AND THE RECORD IS TRUE. IT CARRIES
  INTO F4 BY NAME.** My condition's second branch was "the measured consequence goes
  into the entry and into `docs/closure/F3.md` beside it". It did. And I did not take
  the figures on trust -- CP3 says a figure is pasted from a run after the last edit,
  and this entry's figures were first measured one commit earlier, so I re-measured all
  of them at `b7c05e7`:

```
cmd    RIGID_MODE_EXACTNESS 1e-15 -> 1e-13 in a scratch clone, then
         python -m pytest tests/verification tests/unit -q
out    1802 passed, 0 failed in 214.55s      the entry's own claim, EXACT
cmd    the unmutated control, same scope, same clone
out    1802 passed in 216.86s                so the 1802 is the whole scope, not a
out                                          subset that happened to pass
cmd    the boundary, SOLVED: 1e-15 -> 1e-11
out    1 failed, 1801 passed -- and the single failure IS
out    test_the_REFUSAL_rejects_a_LIFTED_rigid_mode, residual 3.783782e-12
rule   BP0/CP3: a figure carries the rule it was measured against, from a run after
       the last edit to the thing it describes
judge  EVERY FIGURE IN `floatfea/tolerances.py:366-396` AND IN `docs/closure/F3.md`
       SECTION 4a IS TRUE AT THE COMMIT THAT PUBLISHES IT. `3784x` of silent headroom
       on the production refusal, and NOTHING in the measuring half of the suite
       objects to a hundredfold widening. This is the first time this milestone that
       a republished figure survived my re-measurement unchanged, and it is the one
       that most needed to.
judge  SO THE GAP IS REAL, IT IS RECORDED WHERE A READER DECIDING WHETHER `1e-15` MAY
       MOVE WILL SEE IT, AND IT IS NOT CLOSED. It carries into F4 as blocking.
```

* **R639 -- ANSWERED, AND I SOLVED THE BOUNDARY IN BOTH DIRECTIONS RATHER THAN
  ACCEPTING `3.24x`.** The assertion is inside the file that computes the quantity,
  with no new apparatus and the sibling precedent named.

```
cmd    PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT swept in a scratch clone, running
         tests/verification/rung3/test_platform_rigid_modes.py AND
         tests/test_counters_are_injected.py at each value
out    1.0e-14  over 3.24x   38 passed          the shipped value, and the plan's
out                                             own declared clearance, reproduced
out    3.0e-14  over 9.71x   38 passed          STILL GREEN
out    3.2e-14  over 10.36x  1 failed, 37 passed -- and the ONE failure is
out                          test_R639_the_INJECTION_SIZE_cannot_be_raised
out    1.0e-6   over 3.2e+08x  1 failed  (verdict 85 measured 262 passed here)
out    1.0e-16  over 0.03x     6 failed -- R639, the window check, and
out                            test_a_ROTATIONAL_BLOCK_reddens_the_gate
rule   the counter-case is a detection threshold, not one arbitrary perturbation;
       and EH4: solve the edge that WEAKENS the gate
judge  EIGHT DECADES BECAME 3.09x, SOLVED, AND THE GUARD FAILS ON BOTH SIDES. The
       `<= 10.0` is a headroom bound on a DECLARED size, carries its
       not-a-tolerance justification, and nothing in the model is accepted or
       rejected by it. R639 CLOSED.
```

* **R640 -- recorded, not a finding, unchanged, and NOW ON A COMMITTED CODE PATH.**
  See C115: `scripts/suite_count.py --half guards` reaches it by construction.
* **R635 -- ruled by EH2 and the ruling is ASSERTED, not described. This is the best
  thing in the round and I measured it in the weakening direction.**

```
cmd    in a scratch clone, raise PLATFORM_RIGID_MODE_EXACTNESS and run
         tests/verification/rung3/test_platform_rigid_modes.py
out    1.154338e-18  (shipped, 1.00x)  20 passed
out    1.5e-18       (1.30x)           20 passed
out    1.88e-18      (1.63x)           20 passed
out    1.89e-18      (1.64x)           1 failed -- and it is
out                  test_EG0_the_CEILING_is_the_window_it_claims_to_be
out    1.0e-17       (8.7x)            3 failed
rule   EH2(c): both edges guarded at 2x, floor and roof. The weakest counter
       response 3.776640e-18 over 1.89e-18 is 2.00
judge  VERDICT 85 MEASURED THIS CEILING'S SILENT RISE AT 8.7x. IT IS NOW 1.63x, AND
       THE 2x ROOF IS WHERE THE REDNESS COMES FROM. The claim "both edges are guarded
       at 2x" in `floatfea/tolerances.py:453-473`, in `docs/milestones/F3.md:659-676`
       and in the report is TRUE, and I checked the ASSERTION rather than the
       sentence -- which is what the implementer says they got wrong first and fixed
       in the same commit as the text.
```

```
cmd    AND THE ATTACK NEITHER OF US HAD RUN: move BOTH constants together
out    ceiling 1.88e-18 (its roof) + injection 3.0e-14  ->  20 passed
out    ceiling 1.88e-18             + injection 5.0e-14  ->  1 failed (R639)
out    ceiling 1.88e-18             + injection 1.0e-13  ->  1 failed (R639)
rule   invert the decision rule and solve -- in TWO variables, because each guard's
       threshold is computed from the other's constant
judge  THE RESIDUAL JOINT ENVELOPE IS CEILING x1.63 AND INJECTION x3.0 AT ONCE, with
       the rung green. Before this round it was x8.7 and x10^8. That is the number
       the entry should carry the next time this is touched, and it is a MEASUREMENT
       rather than a finding: nothing is wrong, and the envelope is no longer large
       enough to hide a defect of the shapes the three counters inject.
```

* **R631, R626's residue -- OPEN, LEDGERED to `docs/closure/F3.md` section 4 under
  DZ7c, accepted, unchanged. They do NOT carry as blocking into F4.**
* **R624, R630, R632, R633, R634 -- CLOSED at verdicts 84 and 85 and staying closed.**
  This round's diff does not reopen them.
* **R636 -- closure C110, still open:** section 9a routes it as "carried as an earlier
  report records it" and it was first stated in verdict 84.
* **R641, R642 -- the implementer's own numbering, both accepted.** R641's regex is
  correct for the case it names and I checked the guard it feeds: 32 site
  parametrisations collect at `b7c05e7` and EVERY ONE resolves to a real path, so no
  phantom reaches the gate. R642's caching is sound and I read it for the one way it
  could have gone wrong -- see C116 for the residue, and note the rung-3 file now runs
  in `1.09s` against verdict 85's `49.94s` for the pair.
* **C101 -- CLOSED.** `docs/closure/F3.md:208` now reads ``866.3x` tighter, which is
  `2.94` decades`, and `1e-15 / 1.154338e-18 = 866.3`. The other site is revision 1's
  prose and the report corrects it in revision 3 section 6 as a triple, which is the
  right place for a claim about a closed revision.
* **C105 -- CLOSED by verdict 85's ruling, and the evidence that it was the right
  ruling is that `test_the_CI_section_is_about_the_REVIEWED_commit` passes against
  revision 3 with no tool change at all.**
* **C103 -- open, pending the escalation reaching Xabier. C104 -- closed.**
* **C102, C106 to C114, C88, C86, C90 to C98, C100, C74, C76, C78, C82, C85, R610,
  R615 -- carried unchanged, no work asked, not re-reviewed.**
* **C40, C75, C75b, C99 -- CLOSED and staying closed.** `ruff`, `black --check` and
  `mypy` all SUCCEEDED on CI at this commit.
* **R611, R617, C89 withdrawn and staying withdrawn. R612 to R614, R616, R618 to R621,
  R623, R625, R627, R628 closed as ruled at 79 to 85. R622 is F4.**

## Findings

**R643. (d, BLOCKING, CARRIES INTO F4) `test_the_report_carries_a_WHOLE_SUITE_count`
IS RED AT THE REVIEWED COMMIT AND STAYS RED WITH THE ANSWERING REPORT IN THE TREE.
THAT IS THE DISCRIMINATOR THE CARVE-OUT IS BUILT ON, SO IT IS NOT THE BOUNDARY.**

```
cmd    git show b7c05e7:docs/reports/F3/step-3.md | tail -3
out    ## 11. The whole suite
out    SUITE_LINE_PLACEHOLDER
cmd    the same token in the WORKING TREE, where revision 3 exists
out    docs/reports/F3/step-3.md:1354   SUITE_LINE_PLACEHOLDER
cmd    python -m pytest tests/test_report_carried.py::test_the_report_carries_a
         _WHOLE_SUITE_count -q, in the working tree
out    1 failed -- "the newest revision carries no whole-suite line"
rule   EG3's sharpening: state (2) is cleared BY THE ANSWERING REPORT. This one is
       not, and CZ1 (iv) is unchanged for anything the answering report does not
       clear
judge  VERDICT 85 NAMED THIS PLACEHOLDER AS CONDITION 1 AND IT IS STILL THERE, so it
       is a second-round miss and not a first sighting. I accept entirely that the
       implementer refused to hand-assemble it -- that refusal is correct and is the
       reason I have a clean number to give. What I cannot do is call the red
       anything other than red.
```

**Closed when** the newest revision of `docs/reports/F3/step-3.md` carries a line
matching `_SUITE` with the three counts and the commit, every failing id named in a
``- **failed** `<id>` `` bullet, and the figure taken from a run rather than assembled.
The run exists: **`18 failed, 2901 passed, 1 skipped in 1245.47s` at `b7c05e7`, one
invocation, clean clone, no exclusion**, with the guards half beside it at **`18
failed, 221 passed, 1 skipped in 185.64s`** and the seventeen CI ids as the
cross-check. Both commands are named in my section above and may be cited as the
source. **No new apparatus, no tool change, and no estimate.**

**R644. (NOT BLOCKING -- a correction to MY OWN instructions, stated once and sent out
of the loop.)** EH1's two lists are short by one name on the state-(2) side and have
one name on the wrong side. I wrote them, and the measurement is above:

```
out    test_the_answered_verdict_is_the_NEWEST_one is on STATE (1)'s list and it is
out      a STATE (2) failure: it fails exactly when a verdict exists and the report
out      has not answered it. "the report at 3fdfc79 is newer than the verdict at
out      f2fa598 and names 8368c51".
out    test_a_carried_row_points_at_a_section_that_discusses_it is on NEITHER list
out      and is a state (2) failure: red on two rows at b7c05e7, all 28
out      parametrisations green with revision 3 in the tree.
judge  EG3(i) SURVIVES THIS UNHARMED -- it is why I ran the two unlisted ones
       individually instead of ruling them by family, and the eighty-third verdict's
       lesson is the only reason the suite-line red was separated from them. But a
       list that is wrong makes the trace harder every round. THIS LEAVES THE LOOP
       and goes to Xabier through the implementer as a one-line directive; it is not
       another round and no step is held on it.
```

## Closure items

Named, not re-reviewed, none of them holding anything. Absorb the whole list in ONE
commit and verify it AFTER the commit exists (CZ1).

* **C115.** `scripts/suite_count.py --half guards` runs the guard-state harness through
  `_worktree()`, and a `git worktree` checkout has a `.git` that is a FILE -- which is
  precisely R640/C111. The harness commits into the suite-count worktree WHILE the
  count is being taken, so that half's figure is measured on a tree that moves during
  the run. My own guards figure was taken in a clone with a real `.git` directory.
  **Closes when** C111's fix lands (`_build` refuses when `.git` is a file, or the copy
  gets a real directory) -- the hazard is now on a committed code path and no longer
  only in a reviewer's scratch harness.
* **C116.** `member_stiffnesses`'s cache at
  `tests/verification/rung3/test_platform_rigid_modes.py:59` is never invalidated. I
  checked the way it could have gone wrong and it has not: `_injected`, `_negate`,
  `_retained_torsion` and `test_the_REFUSAL_rejects_a_LIFTED_rigid_mode` all
  `k.copy()`, no caller mutates the returned list, and the counters replace the module
  FUNCTION rather than the cache, so both BX0 cells still reach them -- which the five
  injection sizes above confirm by rejecting three of them. The residue is that a
  future test patching `build_superstructure` would be SILENTLY VACUOUS. **Closes
  when** the cache keys on something, or the docstring says the function must not be
  patched upstream.
* **C117.** `--half` accepts only the exact two-token form:
  `if len(argv) >= 3 and argv[1] == "--half"`. So `--half=main`, a bare `main`, and
  `--half` with no value ALL fall through silently to `both`, which is the path that
  does not finish. "An unsupported case raises, it never defaults." **Closes when** an
  unrecognised argument exits non-zero.
* **C118.** A published revision is being rewritten and a sentence is DOUBLING. Take
  the R629 sentence in revision 1 section 1 -- the one beginning "verdict 83" and
  ending "was answered at `0d911ce`" -- and count its occurrences per commit with
  `git show <sha>:docs/reports/F3/step-3.md | grep -o <that sentence> | wc -l`:
  `95f6293` gives **1**; `31cd0db`, `3fdfc79`, `24e8bb2` and `b7c05e7` give **3**; the
  working tree with revision 3 in it gives **6**. The paragraph now carries the
  sentence three times in a row. Whatever edits the report is APPENDING where it means
  to replace, and the count doubles every round it is left. **Closes when** the
  paragraph has one copy and the editing step is a replace.
* **C119.** `scripts/untouched_sites.py` has R641's defect, unfixed. Revision 3 section
  8 carries the row `| R637 | R634-docs/closure/F3.md |` -- a pytest parametrisation id
  read as a path and attributed to the wrong finding. I checked the GUARD's own
  extractor and it is clean, so this is prose rather than a gate. **Closes when** that
  generator anchors the same way `_ANSWERS_PATH` now does.
* **C120.** The deleted state's corpus row at
  `tests/corpus/report_guard_states.txt:164` now falls into `AWAITING_TRANSCRIPTION`,
  where it reads as an untranscribed WORK ITEM rather than as a control deleted for
  vacuity. Those are different statements and the count
  `test_the_corpus_and_the_states_agree` prints no longer distinguishes them. **Closes
  when** the printed line separates "not yet built" from "built, measured vacuous,
  deleted" -- or, if that is apparatus, when `docs/milestones/F2a.md` carries it as a
  row.
* **C121.** The tree says two different things about R638's disposition at one commit.
  `docs/closure/F3.md:139` and `floatfea/tolerances.py:394` say **"it carries into F4
  by name"**; `docs/reports/F3/step-3.md:1300` says **"the registry row is backlog, not
  an F4 carry"**. **I rule: R638 CARRIES INTO F4 BY NAME AND STAYS BLOCKING THERE.**
  CZ0's sentence is explicit, verdict 85 said so, and the two source-tree sites are the
  ones that are right. If EH3 says otherwise that is a directive-level conflict and it
  goes to Xabier; it is not settled by a report line. **Closes when** the report's
  section 9b row reads what the other two sites read.
* **C122.** `floatfea/tolerances.py:371-375` carries a measurement I did not ask for --
  `1802 passed, 0 failed` over `tests/verification` and `tests/unit` -- without its
  command, in a file BI3 says must not hold a regenerated table. The number is TRUE (I
  reproduced it exactly) and it IS in a proper triple in `docs/closure/F3.md` section
  4a. **Closes when** the entry keeps the one number it needs and points at section 4a
  for the rest, per BI3's own remedy.
* **C123.** Revision 3 section 10 is headed "EH6 -- not started" while the hand-back
  says EH6/EI3 is "scripts-only and started". **Closes when** the two agree.
* **C113 is still open** and section 9a still carries twelve rows reading "carried as
  an earlier report records it".
* **C102, C103, C106 to C112, C114, C88, C86, C90 to C98, C100, C74, C76, C78, C82,
  C85, R610, R615** -- carried unchanged. **C89** withdrawn. **C40, C75, C75b, C99,
  C101, C104, C105** -- CLOSED.

## Tolerances touched

```
cmd  git diff 95f6293..HEAD --numstat -- floatfea/tolerances.py
out  52  0
cmd  the same diff, lines matching a NAME: Final[float] = value declaration
out  (no output) -- NOT ONE VALUE LINE CHANGED, in either direction
cmd  git diff 95f6293..HEAD -- "tests/regression/*" tests/conftest.py
out  (no output) -- no golden moved, no parametrisation loosened, no conftest
judge  NO TOLERANCE WAS TOUCHED AS A VALUE THIS ROUND, and the file grew by 52 lines
       of comment and nothing else. What moved is TWO ASSERTIONS, both strictly
       tightening: a roof on the window and an upper bound on the injection. I solved
       both edges myself rather than taking either.
```

| constant | value | form | counter | justification located |
|---|---|---|---|---|
| `PLATFORM_RIGID_MODE_EXACTNESS` | `1.154338e-18`, UNCHANGED | relative and dimensionless; the element-local residual is homogenised, so span, orientation and reference point leave the quantity; correct form | three rows, both BX0 cells green. **AND THE ROOF IS NOW ASSERTED (EH2(c))**: the silent rise fell from `8.7x` to `1.63x`. Solved: `1.88e-18` green, `1.89e-18` red, and the red is `test_EG0_the_CEILING_is_the_window_it_claims_to_be` at `weakest/ceiling = 2.00` | `floatfea/tolerances.py:453-473` and `docs/milestones/F3.md:659-676`; the window is re-measured every run by `test_EG0_the_CEILING_is_the_window_it_claims_to_be` rather than typed (BI3). **EH2(a) and (b) are the change rule and they are prose, correctly -- nothing in them is a number.** |
| `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | `1.0e-14`, UNCHANGED | a fraction of `max abs k_e`, dimensionless; correct form | it IS the counter, and **R639 IS CLOSED**: the upper edge is now solved at `3.09x` where it was eight decades. `3.0e-14` green, `3.2e-14` red, `1.0e-16` red on the lower side | `floatfea/tolerances.py:423-446`, `docs/milestones/F3.md:668`, and the clearance now PRODUCED by `test_R639_the_INJECTION_SIZE_cannot_be_raised` rather than stated in a comment. |
| `RIGID_MODE_EXACTNESS` | `1e-15`, UNCHANGED | relative and dimensionless; correct form | **STILL NONE, AND THE GAP IS NOW WRITTEN WHERE IT WILL BE READ.** `1e-13` gives `1802 passed, 0 failed` over the measuring half; the solved edge is `3.783782e-12`; `3784x`. Every figure RE-MEASURED BY ME at `b7c05e7` and exact | its own entry at `floatfea/tolerances.py:330-397` and `docs/closure/F3.md` section 4a. **R638 carries into F4 by name.** |
| `RIGID_MODE_BOUND` | `199.526231496888`, UNCHANGED | unchanged | unchanged | unchanged. **R631** is its open residue, ledgered under DZ7c. |

**The residual joint envelope, because it is the number the next person needs:** both
constants moved together, ceiling `x1.63` AND injection `x3.0` at once, the rung stays
green at `20 passed`; `x1.63` with `x5.0` reddens. Measured at `b7c05e7` in a scratch
clone.

## My own instructions (4b), read line by line

```
cmd  git diff 95f6293..HEAD --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out  CLAUDE.md 42 ++++++, docs/SUPERVISOR.md 42 ++++++, 84 insertions(+), 0 (-)
cmd  git log --oneline 95f6293..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out  4e91284 process: CP3, the carve-out's two lists, and boundaries solved both ways
cmd  git show 4e91284 --name-only
out  CLAUDE.md, docs/SUPERVISOR.md     AND NOTHING ELSE
judge  NO STOP-CLASS PROCESS FINDING. A STANDALONE `process:` COMMIT, touching no
       `floatfea/` and no `tests/`, citing EH0, EH1 and EH4 by name. I read all 84
       added lines: three new sections -- EH1's corrected carve-out lists, EH4's
       both-directions rule, CP3's pasting order -- all ADDITIVE, nothing deleted, no
       guard weakened, and all three are my own wording unparaphrased. The EH1 and
       CP3 blocks appear in both files and EH4 appears in both.
       `b7c05e7` is ALSO labelled `process:` and touches none of these three paths,
       which I verified by the pathspec and not by the subject line.
```

## The adversarial corpus (BE3)

**NO BATCH 32, and I am saying so rather than leaving the section absent.**

```
cmd  git diff 95f6293..HEAD --stat -- tests/corpus
out  (no output)
cmd  grep -c "^id=" tests/corpus/platform_ceiling_and_counter_registration.txt
out  26        unchanged
```

**New entries this round: 0. So there is no coverage measurement this round, and that
is a cost I am naming rather than hiding.** EG4(e) pauses general batches after F3 step
3 and excepts only F4's load-mapping gate and EB6's label-provenance gate; neither is
in this step's diff, and the G2.1 ceiling is not on the exception list. Verdict 85
recorded batch 31 as the last general batch. **My standing instruction says add unseen
entries at every review; CLAUDE.md's EG4(e) is the project instruction and it
governs.** The last three measurements, for the record of what the pause is spending:
4 of 11, 8 of 13, 5 of 10, with the final round's misses all outside the element.

**AND THE METHOD NOTE, which is this round's only transferable lesson.** Verdict 85's
closing paragraph said the question that catches a silent widening is "diff the step,
then ask what the step's change makes POSSIBLE". The two best measurements this round
came from a second question that is not in my instructions either: **move TWO constants
at once when each guard's threshold is computed from the other's constant.** Each of
this round's two new assertions is strong alone -- `1.63x` and `3.09x` -- and jointly
they still admit `1.63x` times `3.0x` with the rung green, because raising the ceiling
raises the detection edges the injection bound is measured against. A one-at-a-time
sweep cannot see that, and both of ours were one-at-a-time.

Every mutation this round was applied in scratch CLONES under the session scratch
directory -- clones and not worktrees, deliberately, because C111 is open and a
worktree has a `.git` that is a file. The main repository's `HEAD` is `b7c05e7`,
`F3 == origin/F3`, and the only path modified in it is the implementer's own
uncommitted `docs/reports/F3/step-3.md`. The only path I have written in this
repository is this verdict.

## On the criterion

**I ruled under CZ0 and I have no complaint about the criterion.** One blocking item,
(d), measured on two machines and separated from a sixteen-red cascade by one command.
Nine closure items named and not re-reviewed. One item -- R644 -- is a correction to my
own instructions and I have put it under its own heading and sent it out of the loop
rather than holding anything on it. No round was spent on prose.

**One thing on the record against myself.** Verdict 85 asked for R638 either closed or
recorded, and offered the recording branch in good faith. The implementer took it, the
record is true, and I re-measured every figure in it. But the effect of my own offer is
that **the ceiling the production builder refuses real decks on leaves F3 with `3784x`
of silent headroom**, and the thing standing between a reader and a hundredfold
widening is still two string comparisons against a markdown table. That was my
decision, not theirs. It is why R638 carries into F4 as blocking rather than as a
ledger line, and why I will not accept a second recording of it.

## Carried for the next step -- F4's `Carried` section, BY NAME, BLOCKING THERE

1. **R643 -- the whole-suite line.** The figure exists and is in this verdict. The
   newest revision of `docs/reports/F3/step-3.md` carries it, with every failing id
   named, or F4's first report does under `Carried` with the commands pasted.
2. **R638 -- `RIGID_MODE_EXACTNESS` has no registered counter and widens `100x` with
   the measuring half of the suite green.** A `REGISTERED` row whose two cells reach
   `floatfea.model.platform`'s namespace, and the `1.0e-8` injection at
   `tests/verification/rung3/test_platform_rigid_modes.py:260` declared in
   `floatfea/tolerances.py` as that constant's counter-defect. Then the widening is
   re-measured and `3784x` is replaced by what the registry refuses. **C121 settles
   that this is a carry and not a backlog row.**
3. **R637's clause (iii), which is the same object as R643:** `pytest -q` and a pushed
   CI run at the answering sha reading `0 failed` apart from EG3's two states.

**Not carried, stated so no round is spent asking:** R631, R626's residue and R635 stay
LEDGERED and I accept the ledger; R639, R637 clauses (i) and (ii), R624, R630, R632,
R633, R634, C101, C104, C105 are CLOSED and I will not reopen them; R622 is F4's own;
the EG4 preview stays blocked on the ground that holds.

## Next step opens when

**STEP 3 IS CLOSED AND F3 IS CLOSED.** This was round 3 of 3 under CZ0 and the step
closes on the cap, with three items carried by name above. F4 may open. The specific
conditions on F4's first turn, in the order that unblocks the most:

1. **LAND REVISION 3 WITH THE SUITE LINE.** The number is in this verdict, taken at
   `b7c05e7` in one invocation with no exclusion, with the guards half beside it and
   CI's seventeen ids as the cross-check. Nothing is estimated and nothing is
   assembled. Run `scripts/suite_count.py` from a clone OUTSIDE the synced folder next
   time -- that is the whole of the impediment and it is measured, not guessed.
2. **THE CLOSURE COMMIT, ONE OF THEM, VERIFIED AFTER IT EXISTS (CZ1).** Nine closure
   items, then at that commit: `ruff check floatfea tests`, `black --check floatfea
   tests`, `mypy floatfea`, `pytest -q`, then `gh run list` at its own sha with the
   job-level conclusions so the lint job's `guards and meta-tests` step is seen to have
   RUN. C118 first, because it doubles every round it is left.
3. **F4's `Carried` carries R643, R638 and R637(iii) BY NAME and they block there.**
4. **R644 goes to Xabier as a one-line directive** with the two measured names. It does
   not become a round.

**Schedule.** F3 closes **13 October** and it closes TODAY, 1 October, twelve days
inside the date. F4 19 October; the member-force table 23 October; the code-check
screen 28 October. **I have no measurement that contradicts any of them**, and the
ladder is green on CI at this commit, all six rungs including ladder 3. **CZ0's
escalation clause is now LIVE and I am stating it rather than noting it:** step 2 closed
carrying four items and step 3 closes carrying three, which is two consecutive steps, so
the choice goes to Xabier -- **slip a date, or reduce scope.** My own reading is that
neither is needed yet, and the reason is specific: all three carried items are bounded
work whose closing conditions are already measured, and none of them is on F4's critical
path. **What I would watch instead is EH6.** It is the critical path, it is
scripts-only, it needs six FloatSim runs in the HSP-runs worktree, and nobody has timed
one. I still do not endorse pulling F4 to 16 October, for verdict 84's reason: the EB6
expected side is unmeasured.

**One sentence for the implementer.** The three repairs are right, the refusal to
hand-assemble the suite line was the correct call and is the reason I have a clean
number to hand you, and the single best thing in the round is that you wrote "both
edges guarded at 2x", noticed it was text ahead of code, and shipped the assertion in
the same commit -- which is CW0 working as intended, applied by you to yourself, before
I got there.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 3
Reviewed commit: 95f62936b03955a91cd879c56529d9483b5e9baf
Verdict: HOLD
**Reviewed commit: `95f6293`.**  (HEAD of F3 and pushed. For once the stamp above agrees with it: I committed no corpus batch this round, so HEAD at write time IS the judged commit. That coincidence is the whole of the deadlock and it is ruled below.)
Tests: 2889 passed, 28 failed, 0 skipped   (MY OWN run, clean worktree at `95f6293`, one invocation, no exclusion, 659.34s. CI at the same commit names the SAME 28 by id. The working tree with the uncommitted revision 2 in it reads `2867 passed, 16 failed, 1 skipped` -- a different tree, and not the number anything is decided on.)

## Round of 2026-10-01 -- EIGHTY-FIFTH verdict, ROUND 2 OF 3 ON STEP 3.

**THE DEADLOCK HAS AN ANSWER, IT IS ONE LINE, AND IT IS MINE.** Nothing in
`scripts/ci_section.py`, nothing in `tests/test_report_carried.py` and nothing in
`scripts/write_verdict.py` needs to change. Both machines already resolve the
JUDGED commit, with the identical regex and the identical comment, and
`write_verdict.py` says so in its own docstring: the body names the commit it
judged, the stamp does not. **Verdict 84 wrote that sha under the label
`Judged commit:`, which no machine reads.** The line both machines DO read is the
bolded `Reviewed commit` line, and this verdict carries it at the top of this
round. Revision 3 regenerates section 0 with `python scripts/ci_section.py` and no
arguments.

**R633 IS ANSWERED AND IT IS THE BEST REPAIR OF THIS STEP.** I did not accept the
`37 passed`: I rebuilt both BX0 cells by hand and planted the OLD body back to
check the cells still discriminate. They do. The gate ceiling is now guarded in
both directions by a measurement.

**R634 IS ANSWERED.** Two sentences corrected, the `ACCURACY` class restored, and
the refusal it now claims is exercised by `pytest.raises` on all three clauses at
solved boundaries. I checked the code and not the sentence.

**R632 IS NOT ANSWERED, AND I HAVE TO WITHDRAW A SENTENCE OF MY OWN.** At the
reviewed commit the ValueError is unchanged on both machines. In the draft that
would fix it, the state plants ONE line of 937 and passes on eight reds that have
nothing to do with pointers -- measured by ablation, identical with the plant
removed. And my verdict-84 line "none, and none is possible" about
`RIGID_MODE_EXACTNESS` was wrong. Had the implementer written it into
`tolerances.py` as my closing condition asked, a false sentence would have landed
in the authoritative tolerance file on my authority.

**AND I BROKE SOMETHING.** `RIGID_MODE_EXACTNESS` -- the ceiling the PRODUCTION
BUILDER refuses on -- can be widened a hundredfold with `1914 passed`, and the
counter injection size can be raised EIGHT DECADES with `262 passed`. Both
measured at this commit, both boundaries solved rather than sampled. R633 gave the
gate's ceiling three counters and left the refusal's ceiling with none, and the
locked plan's own section 7 row declares an upper bound that nothing asserts.

## THE TREE AT 95f6293, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse F3 && git rev-parse origin/F3
out    95f62936b03955a91cd879c56529d9483b5e9baf   all three -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    M docs/reports/F3/step-3-answers.json
out    M docs/reports/F3/step-3.md
judge  REVISION 2 IS UNCOMMITTED, as the hand-back says. So the report AT the
       reviewed commit is revision 1, which answers verdict 83 while verdict 84
       exists. Item 1b of my instructions fails at this commit -- and it fails
       for the deadlock's reason rather than for a reporting failure, so I rule
       the deadlock and not the header.
cmd    git log --oneline 6c4e651..HEAD --name-only
out    95f6293  floatfea/tolerances.py, tests/test_counters_are_injected.py,
out             tests/verification/rung3/test_platform_rigid_modes.py
cmd    git diff 6c4e651..HEAD --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (no output)
judge  ITEM 4b PASSES BY ABSENCE, verified by the diff and not by the subject
       line. NO STOP-CLASS PROCESS FINDING.
cmd    git diff 6c4e651..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (no output)
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py        CI0: the pathspec resolves to a real file
cmd    git ls-files | grep -i conftest
out    tests/conftest.py, and tests/test_supervisor_conftest_pathspec.py
judge  ONE CONFTEST, UNCHANGED, AND I READ IT LINE BY LINE AGAIN (CH2). No
       pytest_runtest_makereport, no pytest_ignore_collect, no
       pytest_collection_modifyitems that removes an item, no outcome written.
       No rung carries its own conftest and no plugin is loaded from tests/.
cmd    python -m pytest -q, clean worktree at 95f6293
out    28 failed, 2889 passed in 659.34s
```

## CI AT THE REVIEWED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit 95f6293... --json conclusion,status,databaseId
out    36907599744  completed  FAILURE
cmd    gh run view 36907599744 --json jobs, job by job
out    the verification ladder            SUCCESS   13 steps
out    lint, unit and guards              FAILURE   14 steps
out    CI determinism -- leg              skipped    0 steps
out    CI determinism -- ten legs agree   skipped    0 steps
cmd    the ladder job's steps
out    ladder 1, 2, 3, 6, 4, 5 -- ALL SUCCESS. "ladder 3 -- the model is the
out    platform" is green, and that is where the new ceiling, the three new
out    counter cells and the registry rows live.
cmd    the lint job's steps
out    actionlint SUCCESS, ruff SUCCESS, black --check SUCCESS, mypy SUCCESS,
out    unit tests SUCCESS, and "guards and meta-tests" FAILURE
judge  NOT CK2: fourteen and thirteen real steps, real durations, no spending
       annotation, no runner-never-started. The two skipped jobs are CK0's
       workflow_dispatch gate, unavailable BY DECLARATION, as at verdicts 79 to
       84. Lint and types are GREEN on a machine neither of us controls, and
       "guards and meta-tests" is seen to have RUN rather than been skipped
       behind an earlier red (CZ1 iii), so I did not re-run them.
cmd    gh run view 36907599744 --log-failed, the FAILED ids, deduplicated
out    28 -- and my own run names the SAME 28
judge  CI IS RED AT THE REVIEWED COMMIT AND I RECORD IT AS RED.
```

**THE EG3(i) TRACE, EACH ID MATCHED BY NAME TO THE STATE'S OWN LIST RATHER THAN
BY FAMILY.** This is EG3 state (2), verdict written and answering report not yet:

```
out    12 x test_every_named_site_is_touched_or_declared[R632-*, R633-*, R634-*]
out          -> state (2): each names a SITE of verdict 84
out     5 x test_the_report_carries_the_finding[R632 .. R636]
out          -> state (2): each names a FINDING of verdict 84
out     1 x test_the_CI_section_is_about_the_REVIEWED_commit     -> (2), named
out     1 x test_the_Carried_table_is_what_the_generator_produces -> (2), named
out     1 x test_the_generator_would_catch_a_row_under_the_wrong_number -> (2)
out     7 x test_the_guard_survives_the_state[baseline plus six planted]
out          -> the cascade: baseline is RED and each cascading state's own
out             failure line is `assert 1 == 0` off that baseline
out     1 x test_the_guard_survives_the_state[guard_state_every_Carried_pointer
out         _names_the_Carried_SECTION_ITSELF]
out          -> NOT THE BOUNDARY. ValueError: substring not found, at
out             tests/test_report_guard_states.py:545, on CI and on my machine.
rule   EG3(i): the waiver applies only if EVERY red traces BY NAME to the
       step-boundary cause, and a red that does not match is CZ1 (iv) unchanged
judge  27 OF 28 ARE STATE (2) OR ITS CASCADE. THE TWENTY-EIGHTH IS R632,
       UNCHANGED FROM VERDICT 84, AT THE SAME LINE, ON BOTH MACHINES. It is
       CZ1 (iv) and it blocks.
```

**EG3(ii) IS CLEARED, AND I REPRODUCED THE FIGURE RATHER THAN TAKING IT.**

```
claim  report section F: a clean worktree at 8368c51 gives 26 failed, 190 passed
cmd    git worktree add --detach <scratch> 8368c51, then python -m pytest
         tests/test_report_carried.py tests/test_report_numbers_are_sourced.py -q
out    26 failed, 190 passed in 4.63s
judge  EXACT. State (2) measured AT the verdict commit, which is the half no
       verdict in this milestone had ever taken. EG3(ii) is SATISFIED, and the
       condition earned itself again: it is what put the 26 on the page.
```

## THE RULING ON C105 -- IT IS NOT A DEADLOCK, AND THE DEFECT IS MINE

The hand-back asked which line is authoritative and offered to carry either
answer. **The judged commit, and nothing changes to get it.** I checked the ground
rather than the argument, and the ground is that both machines already encode the
implementer's reading, in the same regex:

```
cmd    scripts/ci_section.py:171 and tests/test_report_carried.py:2019
out    _JUDGED = re.compile(r"\*\*Reviewed commit:\s*`([0-9a-f]{7,40})`")
out    -- in BOTH files, byte-identical, each with a comment saying the plain
out    `Reviewed commit:` line is the DIFF BASE, the reviewer's corpus commit,
out    and that only the judged one was ever a pushed head so only it has a run
cmd    scripts/write_verdict.py, the last paragraph of its docstring
out    "The `Reviewed commit:` stamp is taken from HEAD, which is structurally
out    NOT the reviewed commit whenever the reviewer commits its corpus first --
out    as it is instructed to. THE BODY NAMES THE COMMIT IT JUDGED; that line
out    does not. Recorded here rather than fixed, because changing what the stamp
out    reads is a change to the reviewer's own tooling and goes through a
out    directive, not through this edit."
cmd    grep -n the bolded form in docs/reviews/F3/step-3.md
out    (no output)
cmd    python scripts/ci_section.py
out    verdict 84 at `8368c51` does not name the commit it judged in its header,
out    so there is no commit to report CI for.
rule   CO1: the generator refuses rather than guessing, and its refusal names the
       line it could not find
judge  THE GENERATOR IS NOT CONFUSED AND THE GUARD IS NOT KEYED TO THE WRONG
       LINE. THE DATA IS MALFORMED AND I MALFORMED IT. Verdict 84 wrote
       `Judged commit:   a647492e...` -- unbolded, unquoted, under a label
       neither file reads -- so `_JUDGED` matched nothing, `ci_section.py`
       refused, and the guard fell back to `_reviewed_commit()`, which is the
       corpus commit `6c4e651`, which has no run. Both halves of the apparent
       disagreement are one missing line.
```

**(1) THE AUTHORITATIVE LINE IS THE JUDGED COMMIT.** The implementer's reading is
correct for exactly the reason given: it is the only commit that is ever a pushed
head, therefore the only one with a run, therefore the only one whose run
describes the tree under review. **No guard change. No generator change. No tool
change. Nothing to carry.**

**(2) THE FORM IS THE BOLDED, BACKTICK-QUOTED `Reviewed commit` LINE IN THE
VERDICT BODY**, which is where `write_verdict.py` says it belongs. **This verdict
carries it**, as its second line. `scripts/ci_section.py` with no arguments will
now resolve `95f6293`, which has run `36907599744`, and
`test_the_CI_section_is_about_the_REVIEWED_commit` reads the same sha through the
same pattern. They cannot disagree: it is one regex in two files.

**(3) C105's STATED CAUSE IS WITHDRAWN -- `re.search` IS CORRECT.** I wrote that
the generator resolves the OLDEST line in the accumulating file. It does not:

```
cmd    scripts/write_verdict.py, the comment at the write site
out    "THE PRIOR ROUNDS ARE PRESERVED VERBATIM, NEWEST FIRST, below a separator
out    ... The new round's own header goes at the top, so the parsers that read
out    the first `Reviewed commit:` line still find the current one."
cmd    grep -n "^# Review" docs/reviews/F3/step-2.md
out    1 (verdict 83), 377 (verdict 82), 784 (verdict 81)
judge  THE FILE IS NEWEST-FIRST, SO THE FIRST MATCH IS THE NEWEST ROUND'S BY
       DESIGN. What happened in step-2.md is that verdict 81 wrote the bolded
       line and 82, 83 and 84 did not, so the only match in the file belonged to
       an older round. `findall(...)[-1]` would have made it WORSE: it would pin
       every future round to the OLDEST header. The defect was a missing line in
       three consecutive verdicts of mine, and the one mechanism that catches it
       is the generator refusing -- which it does, by name.
```

**(4) DO NOT ANCHOR ON THE PLAIN STAMP.** It is the diff base and is read as such
at `tests/test_report_carried.py:2328` and `:2396`, and `write_verdict.py` rules a
change to what it stamps a directive-level matter. I am not taking that change:
this round is the demonstration that it is not needed. **C105 is CLOSED by this
ruling**, and what is left of it is one regenerated section 0 in revision 3.

## Carried

Verdict 84 named three blocking items and nine closure items. Every one is below.

* **R632 -- NOT ANSWERED. SAME LINE, SAME ERROR, BOTH MACHINES, AT THE REVIEWED
  COMMIT -- and the draft that would fix it makes the state certify nothing.
  R637.** The DATA half of the condition landed and landed well:
  `docs/reports/F3/step-3-answers.json` now spreads its 22 rows over sections A,
  B, C, D, E, 9a, 9b and 9c instead of 14 of them at one section. That is a real
  repair and I am not taking it back. The GUARD half did not land.
* **R633 -- ANSWERED at `95f6293`, branch (i), which was the harder and the right
  one. I rebuilt both cells rather than accepting `37 passed`.**

```
cmd    python -m pytest tests/test_counters_are_injected.py
         tests/verification/rung3/test_platform_rigid_modes.py -q
out    37 passed in 49.94s        reproduced exactly
cmd    both BX0 cells, per registered row, driven by hand through
         _gate_cell and _ceiling_cell on the SHIPPED bodies
out    element rigid residual -- dropped flip      gate=True  ceiling=True
out    element rigid residual -- wrong dof index   gate=True  ceiling=True
out    element rigid residual -- rotational block  gate=True  ceiling=True
cmd    NON-VACUITY 1: plant the PRE-R633 body back -- compute the response and
         compare it with the ceiling inline, never calling the gate
out    dropped_flip gate=False, wrong_dof_index gate=False,
out    rotational_block gate=False       -- REJECTED, all three
cmd    NON-VACUITY 2: plant R197's shape -- call the gate, inject 1.0e-2 instead
         of the declared size, twelve decades too large
out    dropped_flip ceiling=False, wrong_dof_index ceiling=False,
out    rotational_block ceiling=False    -- REJECTED, all three
rule   gate cell: the counter must FAIL with the gate replaced by a no-op.
       ceiling cell: it must FAIL with the ceiling widened past its injection.
judge  THE CELLS DISCRIMINATE FOR THESE ROWS AND I MEASURED IT ON PLANTED BODIES
       RATHER THAN ON THE SHIPPED ONES. `_counter_reddens_the_gate` resolves
       `test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions` through the
       module global, so the no-op substitution reaches it; `match="rigid
       residual"` is the only assertion in that gate carrying the string, so the
       raise cannot be a different one; and `counter_response(kind) * WIDEN` is
       derived from the DECLARED constant, which is why cell two still rejects an
       injection that departs from it.
cmd    AND THE CONSEQUENCE, which is what the registration was FOR: widen
         PLATFORM_RIGID_MODE_EXACTNESS and run the two files
out    1.154338e-18 -> 1.0e-17   (8.7x):    2 failed, 35 passed
out    1.154338e-18 -> 1.0e-14   (8700x):  13 failed, 24 passed, and all three
out                                        new counter tests are among them
judge  THE GATE'S CEILING IS NOW GUARDED BY A MEASUREMENT IN BOTH DIRECTIONS.
       Before this commit the registry held no row for it at all. R633 CLOSED.
```

* **R634 -- ANSWERED at `95f6293`. Clauses (1) and (2) landed; clause (3) is
  superseded by my own withdrawal below. I checked the code, not the sentence.**

```
cmd    floatfea/tolerances.py:330-340 and :355-359, as they now read
out    "IT ASSERTED NOTHING BETWEEN DI0 AND F3 STEP 2, AND IT ASSERTS AGAIN NOW"
out    "`check_rigid_modes` refuses the production build on this value"
out    "its CLASS line above saying ACCURACY is right again"
cmd    does anything make that refusal RAISE, or is it a sentence?
out    tests/verification/rung3/test_platform_rigid_modes.py:272 pytest.raises
out       ValueError match="INDEFINITE"            (three negation shapes)
out    :274 pytest.raises ValueError match="rigid residual"   <- THIS constant
out    :318 pytest.raises ValueError match="first flexible mode"
out    :224 test_the_REFUSAL_accepts_every_real_member, the other side
rule   a gate carries its own failure
judge  THE SENTENCE IS BACKED BY A TEST AND NOT BY PROSE, at a boundary solved
       from both sides, and the ACCURACY class is correctly restored. CLOSED.
```

* **MY OWN VERDICT-84 SENTENCE IS WITHDRAWN, AND THE IMPLEMENTER WAS RIGHT NOT TO
  COPY IT.** R634's third clause asked the entry to say "no counter is registered
  against it and why -- the band window is empty", and my Tolerances table said
  "**none, and none is possible**". The second half is false:

```
cmd    the shipped refusal counter at tests/verification/rung3/
         test_platform_rigid_modes.py:260 -- bad[3,3] += 1.0e-8 * max|k_e| --
         evaluated on platform:hub1_arm
out    residual 3.783782e-12 = 3783.8x the 1e-15 ceiling, and :274 asserts the
out    ValueError on it
cmd    bisect the smallest injection the 1e-15 refusal detects, worst of the 16
out    dropped_flip 2.7355e-14   wrong_dof_index 1.0571e-15
out    rotational_block 6.8377e-13
judge  A COUNTER AGAINST `RIGID_MODE_EXACTNESS` IS POSSIBLE AND ONE IS ALREADY
       SHIPPED. What is impossible is REUSING THE SHARED DECLARED SIZE 1.0e-14:
       at that size dropped_flip reddens 0/16 and rotational_block 0/16 against
       1e-15, which is exactly R624 and exactly why the two ceilings are
       separate. The LOCKED PLAN states it correctly at docs/milestones/F3.md:684
       -- "no counter is registered against the refusal", with the empty-band
       reason -- and my gloss overreached that sentence. Withdrawn. What replaces
       it is R638, which is the consequence nobody had measured.
```

* **R635 -- recorded, ledgered, still NOT blocking, and I accept the ledger.**
  Section E records the measurements and routes the EG0(c)-versus-entry conflict to
  Xabier unparaphrased, which is what I asked for. No work this round.
* **R631 and R626's residue -- OPEN, LEDGERED to `docs/closure/F3.md` section 4
  under DZ7c, accepted, unchanged. They do NOT carry as blocking into F4.**
* **R624, R630 -- CLOSED at verdict 84 and staying closed.** This round's diff does
  not reach them.
* **R629 -- its DATA half is now genuinely fixed; its GUARD half is R637.** It is
  the ancestor of both R632 and R637 and this is its third shape.
* **R636 -- my own result, not a finding.** The report routes it to section 9a as
  "carried as an earlier report records it", which is false: it was first stated in
  verdict 84. Closure, C110.
* **C101 -- STILL OPEN, and the report says it is closed.** `docs/closure/F3.md:154`
  and `docs/reports/F3/step-3.md:534` both still read "five decades"; neither file
  is touched by `95f6293`. Revision 2 section D says "Corrected in both". The
  acknowledgement is right and the correction has not happened. Closure.
* **C102 -- STILL OPEN AND IT HAS A THIRD SITE NOW.** The backwards phrasing C102
  named has been copied into `floatfea/tolerances.py:356-357` by this very commit.
  The number itself is right for its operating point -- the admissible band, not
  the sixteen; on the sixteen it is `2834.3x`, which I measured -- and the sentence
  reads as though the ceiling were inside the residual rather than above it.
* **C103 -- ANSWERED in section D**, with the directory, the six filenames, the 21
  columns and the false ground struck. The blocker stands on the ground that holds.
  Closure, pending the escalation itself reaching Xabier.
* **C104 -- ANSWERED in section D** by a triple naming the commit, the false figure
  and the true one, with no number outside a triple. Closed.
* **C105 -- CLOSED by the ruling above, with its stated cause withdrawn.**
* **C106, C107, C108, C109 -- untouched, still closure, not re-reviewed.**
* **C88 -- still open, its timing condition still missed, ruled at verdict 84.**
* **C86, C90 to C98, C100, C74, C76, C78, C82, C85, R610, R615 -- carried
  unchanged, no work asked.**
* **C40, C75, C75b, C99 -- CLOSED and staying closed.** `ruff`, `black --check` and
  `mypy` all SUCCEEDED on CI at this commit.
* **R611 and R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to
  R621, R623, R625, R627, R628 closed as ruled at 79 to 83. R622 is F4. C89 stays
  withdrawn. C58 to C73, C56(iii), C56(iv), C57 -- as ruled at 77 to 83.** This
  step's diff touches none of them.

## Findings

**R637. (d AND c, BLOCKING) R632 IS UNCHANGED AT THE REVIEWED COMMIT, AND THE
DRAFT THAT WOULD FIX IT MAKES THE STATE CERTIFY NOTHING. THE SAME SUBSTRING IDIOM
MAKES A SECOND GUARD READ 22 LINES OF A 937-LINE REPORT. THIS IS R629's DEFECT IN
ITS THIRD SHAPE, AND IT IS NOW MEASURED BY ABLATION RATHER THAN ARGUED.**

```
cmd    git show 95f6293:docs/reports/F3/step-3.md | grep -c "^# Revision "
out    0
cmd    gh run view 36907599744 --log-failed | grep -i "substring not found"
out    >  head = text.rindex("# Revision ")
out    E  ValueError: substring not found
out    tests/test_report_guard_states.py:545: ValueError
judge  HALF ONE: AT THE REVIEWED COMMIT NOTHING MOVED. Verdict 84's symptom, the
       same line, on CI and on my own run. The commit message's `1 passed` was
       measured on the UNCOMMITTED tree, which is a different tree.
```

```
cmd    the working tree, where revision 2 exists: every occurrence of the
         substring the plant action searches for
out    line   7   the revision-1 heading
out    line 636   the revision-2 heading
out    line 697   inside prose, quoted, followed by a right parenthesis
out    line 916   inside prose: "...carries a `# Revision ` heading and S9 is split."
cmd    rindex takes the LAST, so what region does the plant actually mutate?
out    character 82868 -> line 916. TWENTY-TWO lines of 937.
cmd    difflib over the planted report against the original
out    ONE changed line, @@ -925 +925 @@, a single S4 -> S9 in a ledger bullet
out    about R626
cmd    count the section pointers the state CLAIMS to move, and the ones it reaches
out    33 pointer tokens in revision 2; 2 reachable from line 916; 1 changed;
out    ZERO in the Carried table
rule   the state's own name is every_Carried_pointer_names_the_Carried_SECTION_ITSELF
judge  THE PLANT MOVES 1 POINTER OF 33 AND NONE OF THEM IS A CARRIED ROW. The
       report's own ANSWER to R632 -- the sentence in section 9a that quotes the
       literal heading string -- is what redirects `rindex` away from the heading
       that same sentence says it added. The fix defeats itself through its own
       prose, which is a shape I have not seen before in this repository.
```

```
cmd    THE ABLATION (BG0). Build the same scratch state with the plant action
         REMOVED and nothing else changed, then run the guard
out    WITH the plant:     exit 1, 174 collected, 8 failed
out    WITHOUT the plant:  exit 1, 174 collected, 8 failed
out    and THE EIGHT NAMES ARE IDENTICAL:
out      test_the_Carried_table_is_what_the_generator_produces
out      test_the_generator_would_catch_a_row_under_the_wrong_number
out      test_the_CI_section_is_about_the_REVIEWED_commit
out      test_the_report_carries_a_WHOLE_SUITE_count
out      test_every_named_site_is_touched_or_declared[R633-...:317, :318, :319]
out      test_every_named_site_is_touched_or_declared[R634-docs/closure/F3.md]
cmd    what the state asserts, and whether it is in DIAGNOSIS
out    `assert code != 0` and nothing more. The state is NOT in DIAGNOSIS, so no
out    reporter is required to NAME the planted defect.
rule   a gate carries its own failure: if the thing it claims were false, would
       this go red?
judge  NO. ONE VARIABLE MOVED AND THE VERDICT DID NOT CHANGE. The state passes on
       eight reds it did not cause, none of which is a pointer check, and it would
       read `passed` with the plant action DELETED OUTRIGHT. This is R516's
       recorded failure mode -- "a state looked green ONLY because an unrelated
       test was failing in the same run" -- and EG3 institutionalises a red
       baseline at every step boundary, which is precisely when this state runs.
       So the vacuity is not occasional; it is structural at the moment of use.
```

```
cmd    grep the tree for every reader of the revision heading
out    ANCHORED, digit-required, CORRECT:
out      tests/test_report_carried.py:247        ^# Revision \d+   (MULTILINE)
out      scripts/check_carried.py:51            ^# Revision \d+   (MULTILINE)
out      scripts/ci_section.py:182              ^# Revision \d+   (MULTILINE)
out    NAIVE SUBSTRING, both wrong:
out      tests/test_report_guard_states.py:545      text.rindex("# Revision ")
out      tests/test_report_numbers_are_sourced.py:102  TEXT.rindex("# Revision ")
cmd    the second one's consequence on the working tree
out    test_the_report_parsed_into_sections FAILED -- "no fenced block in the
out    whole revision"; BODY is 22 lines of 937, so EVERY number in revisions 1
out    and 2 is outside the domain of the guard CLAUDE.md names as the mechanical
out    half of BF0
rule   assertion domain blindness: check that the collection the assertion
       inspects can actually contain the failure
judge  THE SECOND GUARD IS THE WORSE ONE, because its own vacuity alarm is the
       only thing that fired and the obvious repair is to silence the alarm. Three
       readers in this tree already get it right with the same two-token change.
```

**Closed when** all three, and the first decides it: **(i)** the ablation is RUN by
the implementer and reported -- build
`guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF` with the plant
action removed and show the nested outcome DIFFERS from the planted one by NAME and
not by exit code; if it does not differ, the state is deleted under DR1 with its
vacuity recorded, standing in my corpus row as what was measured. **(ii)**
`tests/test_report_guard_states.py:545` and
`tests/test_report_numbers_are_sourced.py:102` read the anchored
`^# Revision \d+` that the other three readers use, so a sentence quoting the
heading cannot be mistaken for one, and `test_the_report_parsed_into_sections` is
shown to parse the whole of the newest revision with its fenced-block count pasted.
**(iii)** at the answering commit `python -m pytest -q` reads `0 failed` apart from
EG3 state (1), and a pushed CI run at that sha reads the same. **No new apparatus
in any branch:** (i) is a measurement, (ii) is two regexes replacing two substring
calls on existing lines.

**R638. (b AND c, BLOCKING) `RIGID_MODE_EXACTNESS` IS THE CEILING THE PRODUCTION
BUILDER REFUSES REAL DECKS ON, AND IT CAN BE WIDENED A HUNDREDFOLD WITH EVERY
MEASUREMENT IN THE TREE GREEN. THE ONLY THING THAT NOTICES IS TWO STRING
COMPARISONS AGAINST A MARKDOWN TABLE. THE BOUNDARY IS SOLVED, NOT SAMPLED.**

```
cmd    in a scratch worktree, set RIGID_MODE_EXACTNESS 1e-15 -> 1e-13 (100x),
         nothing else, then run the plan guard, the literal guard, the counter
         registry, rung 1, rung 3, the unit tests and the regression goldens
out    2 failed, 1914 passed in 167.12s
out    FAILED test_the_plan_and_the_code_agree[F2.md-1417-RIGID_MODE_EXACTNESS-1e-15]
out    FAILED test_the_plan_and_the_code_agree[F3.md-677-RIGID_MODE_EXACTNESS-1e-15]
judge  BOTH REDS ARE BOOKKEEPING: each compares the float literal in a plan table
       with the float literal in the code. NOT ONE MEASUREMENT OBJECTS. Edit two
       markdown rows and a hundredfold widening of the production refusal is
       green -- which is the shape BG1 was created for, in this file's own words:
       "`RESULTANT_EXACTNESS` once shipped with `ceiling < counter` as its only
       guard -- two literals compared in `tolerances.py` -- and could be widened a
       hundredfold with the suite green."
cmd    INVERT THE RULE AND SOLVE IT. The binding measurement is
         test_the_REFUSAL_rejects_a_LIFTED_rigid_mode, whose injected residual is
out    3.783782e-12 on platform:hub1_arm
cmd    confirm by stepping just past it: 1e-15 -> 1e-11
out    1 failed, 1625 passed -- and the single failure IS that test
judge  SO EVERY CEILING BELOW 3.783782e-12 IS ACCEPTED BY EVERY MEASUREMENT IN
       THE TREE: 3784x OF SILENT HEADROOM, at the operating point
       platform:hub1_arm with the shipped sections, on the one ceiling whose
       subject is "every deck a reader could write". Compare the GATE's ceiling,
       measured above: it reddens at 8.7x. The two are guarded nearly three orders
       of magnitude apart and the weaker one is the one on the production path.
```

```
cmd    tests/test_counters_are_injected.py, what the registry says about this
out    test_there_is_something_to_check's docstring: "A constant with no counter
out    registered here is not covered at all"
cmd    grep RIGID_MODE_EXACTNESS tests/test_counters_are_injected.py, excluding
         the PLATFORM_ name
out    one COMMENT line at :190, and no row
cmd    and the completeness bound, after this step's repair
out    :363   assert len(REGISTERED) >= 7, with exactly 7 rows
judge  THE BOUND IS STILL THE CURRENT COUNT. `>= 4` with four rows could not see
       a fifth constant; `>= 7` with seven cannot see an eighth. It detects a
       DELETION and never an OMISSION, which is the FORM R633 found and not only
       the number -- I asked for `>= 5`, the number moved and the form did not.
       I am not asking for a new guard for that; I am recording that the guard
       cannot be the reason this is caught next time.
cmd    and the injection size that would be the missing row's counter
out    tests/verification/rung3/test_platform_rigid_modes.py:260
out      bad[3, 3] += 1.0e-8 * big
rule   CLAUDE.md section Tolerances: every numerical tolerance lives in
       floatfea/tolerances.py, "no exceptions, no local literals", and the same
       rule applies to anything functioning as a tolerance under another name
judge  THE COUNTER SIZE IS A LOCAL LITERAL IN A TEST. Every other counter in this
       repository is a declared `*_COUNTER_DEFECT` constant.
       tests/test_no_tolerance_literals.py cannot see it because its domain is
       values reaching a COMPARISON and this one reaches an INJECTION -- the
       assertion-domain shape, inside the guard written for exactly this rule.
```

**Closed when** `RIGID_MODE_EXACTNESS` has a row in
`tests/test_counters_are_injected.py`'s `REGISTERED` with both BX0 cells green --
whose counter is the body that ALREADY EXISTS, since
`test_the_REFUSAL_rejects_a_LIFTED_rigid_mode` calls `check_rigid_modes` and
already raises under `pytest.raises`, so it is a counter in BX0's sense today --
and whose injection size `1.0e-8` is DECLARED in `floatfea/tolerances.py` as that
constant's counter-defect rather than left at
`tests/verification/rung3/test_platform_rigid_modes.py:260`; **and** the widening
is re-measured after the row lands, so the `3784x` above is replaced by the factor
the registry now refuses. **No new apparatus:** one row in an existing list, one
constant declaration, one literal replaced by a name. **If instead the decision is
that this constant stays unregistered**, then the measured consequence -- `100x`,
`1914 passed`, the solved edge `3.783782e-12`, `3784x` -- goes into the entry at
`floatfea/tolerances.py` and into `docs/closure/F3.md` beside it, because a reader
deciding whether `1e-15` may move is entitled to know that nothing in the tree
would stop them.

**R639. (b, BLOCKING) THE COUNTER INJECTION SIZE CAN BE RAISED EIGHT DECADES WITH
THE WHOLE REGISTRY AND BOTH EG0 CELLS GREEN, AND THE LOCKED PLAN DECLARES AN UPPER
BOUND THAT NOTHING ASSERTS.**

```
cmd    at 95f6293's code, PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT
         1.0e-14 -> 1.0e-6, nothing else, then the registry and all of rung 3
out    262 passed in 54.43s
judge  EIGHT DECADES AND NOT ONE ASSERTION OBJECTS -- not the two BX0 cells, not
       test_EG0_the_THREE_COUNTERS_redden_every_member, not
       test_EG0_the_CEILING_is_the_window_it_claims_to_be, not the three new
       counter tests. Every one of them gets EASIER as the injection grows: 16/16
       is more true, the window's roof rises with it, and the widened ceiling the
       ceiling cell uses is itself computed from the raised size.
cmd    what the LOCKED PLAN declares this value to be
out    docs/milestones/F3.md:668 -- "The size the three counters inject at, AND
out    THE SMALLEST DEFECT THE GATE MUST STILL FAIL ... it clears the binding
out    per-member edge 3.088842e-15 by 3.24x"
rule   the counter-case is a DETECTION THRESHOLD and not one arbitrary
       perturbation
judge  THE PLAN'S OWN SENTENCE IS THE ASSERTION THAT IS MISSING. Verdict 84
       verified the LOWER side -- 12/16 at 3.050e-15, 16/16 at 3.100e-15, so
       1.0e-14 clears a solved boundary by 3.24x -- and never asked the other
       direction. At 1.0e-6 the gate's advertised detection floor is eight decades
       coarser, every "850x of detection" figure in F3 becomes wrong, and the
       suite says nothing. My own corpus batch 31 has the same blind spot: its
       entry `counter_defect_size_boundary_SOLVED` solves the LOWER edge only.
```

**Closed when** the `3.24x` clearance the locked plan declares is asserted rather
than stated. `test_EG0_the_THREE_COUNTERS_redden_every_member` already bisects
`worst_edge` per kind, so one assertion inside that existing test --
the declared injection no greater than a named clearance times `worst_edge` --
closes it, with the clearance named in `floatfea/tolerances.py` beside the value.
**No new apparatus:** the quantity is already computed by the test that would
assert it, and **the repository already ships this assertion for a sibling
constant** --
`tests/verification/rung1/test_corpus_configurations.py::test_the_counter_DEFECT_SIZE_cannot_be_raised`
does exactly this for `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`, so the precedent and
the wording both exist and neither is new.

**R640. (NOT A FINDING -- A HAZARD I CREATED AND SHOULD RECORD, because the next
person to run the suite in a worktree will hit it.)** Three harness states commit
into the parent repository when the suite runs inside a `git worktree` checkout.

```
cmd    run python -m pytest -q in a `git worktree add --detach` checkout, then
         git log --oneline -3 in that checkout
out    e9b2219  docs: step-3 revision 99 -- and the guard that judges it
out    3d0f3de  harness: the report, re-committed with an older Answers sha
out    899e077  harness: the report, re-committed with an older Answers sha
cmd    ls -la .git in that checkout
out    -rw-r--r--  76 bytes -- a FILE holding `gitdir: ...`, not a directory
rule   _build copies ROOT to tmp and then runs `git -C <copy> add` and `commit`
judge  THE COPY'S `.git` IS A POINTER, SO THE COMMIT LANDS IN THE SOURCE
       WORKTREE. The harness already records this exact hazard for `rmtree`
       (C10/R585: ".git IS NOT ALWAYS A DIRECTORY ... scripts/suite_count.py
       builds exactly that kind of tree") and fixed it there and not here.
       UNREACHABLE ON CI, where actions/checkout produces a real directory, and
       THE MAIN REPOSITORY IS UNTOUCHED -- git rev-parse HEAD is 95f6293 and
       F3 == origin/F3, both checked after every experiment. Closure item C111:
       the copy's `.git` is replaced by a real directory, or `_build` refuses
       when it is a file.
```

## Closure items

Named, not re-reviewed, none of them holding anything. Absorb the whole list in one
commit and verify it AFTER the commit exists (CZ1).

* **C101.** Still open. "five decades tighter" at `docs/closure/F3.md:154` and
  `docs/reports/F3/step-3.md:534`; neither file is touched by `95f6293`, and
  revision 2 section D says "Corrected in both". **Closes when** both sites carry
  the measured ratio and R636's detection gain replaces the sentence.
* **C102.** Still open, THIRD SITE. `docs/closure/F3.md:69`,
  `docs/milestones/F3.md:677` and now `floatfea/tolerances.py:356-357` all read
  "`51.1x` inside the clean worst". The figure is right for the admissible band and
  reads backwards; on the sixteen shipped members it is `2834.3x`, which I measured.
  **Closes when** one sweep's worst and that sweep's margin sit in the same cell at
  all three sites, with the direction of the inequality stated.
* **C103.** Answered in section D. **Closes when** the escalation itself reaches
  Xabier on the ground that holds.
* **C104.** Answered in section D by a triple. Closed.
* **C105.** CLOSED by the ruling above; its stated cause is withdrawn.
* **C106, C107, C108, C109.** Carried unchanged from verdict 84.
* **C110.** Section 9a routes R636 as "carried as an earlier report records it".
  R636 was first stated in verdict 84. **Closes when** the row says so.
* **C111.** The harness commits into a `git worktree` parent. R640 above.
  **Closes when** the scratch copy's `.git` is a real directory, or `_build`
  refuses when it is a file.
* **C112.** Section H declares R632's eleven `tests/test_report_guard_states.py`
  sites left with a boilerplate reason about step 1 and step 2. The file IS
  untouched -- I checked -- and the reason given is not the true one: verdict 84's
  R632 named `:539` to `:546` and `:777` and its condition required the plant
  action changed. **Closes when** those rows say what is true about verdict 84's
  finding, site by site.
* **C113.** Section 9a still carries 17 items, 12 of them reading "carried as an
  earlier report records it". The pointer repair is real and substantial and this
  is its residue. **Closes when** a pointer at section 9a names a disposition a
  reader can check, or 9a is split again.
* **C114.** `RIGID_MODE_EXACTNESS`'s audit trailer at `floatfea/tolerances.py:365-366`
  still ends "assertion dropped 2026-09-26 (DI0, R530)" with no line recording that
  it asserts again from F3 step 2. **Closes when** the trailer carries that date.
* **C88** -- still open, its one timing condition still missed; ruled at verdict 84.
* **C86, C90 to C98, C100** -- carried unchanged.
* **C74, C76, C78, C82, C85, R610, R615** -- ledger lines, carried unchanged.
* **C89** -- withdrawn and staying withdrawn. **C40, C75, C75b, C99** -- CLOSED.

## Tolerances touched

```
cmd  git diff 6c4e651..95f6293 --numstat -- floatfea/tolerances.py
out  25  6
cmd  the same diff, lines matching a NAME = value declaration
out  (no output) -- NOT ONE VALUE LINE CHANGED, in either direction
cmd  git diff 6c4e651..95f6293 -- "tests/regression/*" tests/conftest.py
out  (no output) -- no golden moved, no parametrisation loosened, no conftest
judge  NO TOLERANCE WAS TOUCHED AS A VALUE THIS ROUND. What moved is one
       ASSERTION -- `len(REGISTERED) >= 4` to `>= 7`, strictly stronger -- and
       three counters that previously asserted themselves now run their gate,
       which I verified on planted bodies rather than on the shipped ones. Every
       change is in the tightening direction. MY FINDINGS ARE NOT THAT ANYTHING
       WAS WIDENED: they are that two constants CAN BE widened, and I measured by
       how much.
```

| constant | value | form | counter | justification located |
|---|---|---|---|---|
| `PLATFORM_RIGID_MODE_EXACTNESS` | `1.154338e-18`, UNCHANGED | relative and dimensionless; the element-local residual is homogenised, so span, orientation and reference point leave the quantity; correct form | **now genuinely registered** -- three rows, both BX0 cells green, and I measured the cells REJECTING two planted defective bodies. Widening it `8.7x` reddens 2 tests, `8700x` reddens 13 including the three counters | `floatfea/tolerances.py:369-421`, `docs/milestones/F3.md:667`, and the derivation re-run by `test_EG0_the_CEILING_is_the_window_it_claims_to_be` at every run rather than typed (BI3). **R633's false sentence is now true, measured.** |
| `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | `1.0e-14`, UNCHANGED | a fraction of `max abs k_e`, dimensionless; correct form | it IS the counter -- and **R639**: its LOWER boundary is solved at `3.24x` and its UPPER side is asserted by nothing. `1.0e-6` reads `262 passed` | `floatfea/tolerances.py:423-446` and `docs/milestones/F3.md:668`, whose "the smallest defect the gate must still fail" is the sentence R639 asks to be made an assertion. |
| `RIGID_MODE_EXACTNESS` | `1e-15`, UNCHANGED | relative and dimensionless; correct form | **NONE, and my "none is possible" is WITHDRAWN.** One exists at `tests/verification/rung3/test_platform_rigid_modes.py:260`, `3783.8x` above the ceiling, unregistered and written as a local literal. **R638**: `1e-13` reads `1914 passed`; the solved edge is `3.783782e-12`, so `3784x` | its own entry at `floatfea/tolerances.py:330-367`, corrected this round and now TRUE about the refusal (**R634 closed**) -- and carrying `51.1x` in the backwards phrasing C102 named, which is C102's third site. |
| `RIGID_MODE_BOUND` | `199.526231496888`, UNCHANGED | unchanged | unchanged | unchanged. **R631** is its open residue, ledgered under DZ7c. |

## My own instructions (4b), read line by line

```
cmd  git diff 6c4e651..95f6293 --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out  (no output)
cmd  git log --oneline 6c4e651..95f6293 -- .claude docs/SUPERVISOR.md CLAUDE.md
out  (no output)
judge  NO STOP-CLASS PROCESS FINDING, verified by the diff and not by the subject
       line. The one commit in this round touches floatfea/tolerances.py,
       tests/test_counters_are_injected.py and
       tests/verification/rung3/test_platform_rigid_modes.py and nothing else.
       Nothing changed what I read, what I must carry, or what I may write.
```

## The adversarial corpus (BE3)

**NO BATCH 32, and I am saying so rather than leaving the section absent.** EG4(e)
pauses general batches after F3 step 3, verdict 84 recorded batch 31 as the last
general batch, and the measurement that justified stopping was batch 31's own: 26
entries, all unseen, 14 predicting `caught`, 1 reading caught, and thirteen of the
fourteen misses records rather than reachable defects.

```
cmd  grep -c "^id=" tests/corpus/platform_ceiling_and_counter_registration.txt
out  26        unchanged this round
cmd  git diff 6c4e651..95f6293 --stat -- tests/corpus
out  (no output)
```

**AND THE METHOD LESSON, which is worth more than a batch.** R638 and R639 are both
shapes batch 31 did not contain, and they share one cause: **batch 31 solved every
boundary from the side that makes the gate look strong.** Its entry
`ceiling_window_counter_edge_SOLVED` solved how far the GATE's ceiling may RISE;
its entry `counter_defect_size_boundary_SOLVED` solved how far the injection may
FALL. Neither asked how far the REFUSAL's ceiling may rise, nor how far the
injection may rise -- and those are the two directions that WEAKEN a gate. "Invert
the decision rule and solve" was applied to one edge of each pair, and two of this
round's three blocking findings came from inverting the direction and nothing else.

If Xabier would rather those three shapes be carried as corpus DATA than as
findings that close, that is a one-line directive and I will write batch 32 against
the two surfaces EG4(e) keeps open.

Every mutation this round was applied in scratch worktrees and a scratch harness
under the session scratch directory. `floatfea/tolerances.py` in the working tree
was restored and verified unchanged, the main repository's `HEAD` is `95f6293`,
`F3 == origin/F3`, and the only paths modified in it are the implementer's own two
uncommitted report files. The only path I have written in this repository is this
verdict.

## On the criterion

**I ruled under CZ0 and I have no complaint about the criterion.** Of my four
numbered items, one is (d) measured on two machines and (c) by ablation, two are
(b) on tolerance values and the form of their counters, one is explicitly not a
finding. Fourteen closure items are named and I will not re-review them. No round
was spent on prose.

**One thing on the record, because it cuts against my own last round.** Verdict 84
spent its strength on three sentences and said the element was "right and I could
not break it". The element still is. But two of this round's three blocking
findings are widenings I could have measured in that round with the same four
commands, and I did not take them because the step's new code was a gate and I
checked the new gate. **The constant that turned out easiest to widen was the old
one that nothing in the diff touched.** The question that catches it is "diff the
step, then ask what the step's change makes POSSIBLE", and it is not in my
instructions. I am not asking for apparatus; I am recording that the reading was
available and I did not take it.

## Next step opens when

**Step 3 is HELD. This is round 2 of 3: the next verdict CLOSES the step whatever
it says, and any blocking item still open then carries BY NAME into F4's `Carried`
and stays blocking there.** The conditions, in the order that unblocks the most:

1. **LAND REVISION 3.** The deadlock is ruled and needs nothing carried: the bolded
   `Reviewed commit` line naming `95f6293` is in this verdict's body, so
   `python scripts/ci_section.py` with no arguments resolves `95f6293` and run
   `36907599744`, and the guard reads the same sha through the same regex. Section
   0 and 0a must be the GENERATOR'S OUTPUT: at `95f6293` the generator refuses, so
   revision 2's section 0 carries a `Generated:` line for a command that cannot
   produce it. Regenerate, do not edit. `SUITE_LINE_PLACEHOLDER` at the end of
   section J is unfilled.
2. **R637**, all three clauses: the ablation run and reported BY NAME; both
   `rindex("# Revision ")` sites changed to the anchored form, at
   `tests/test_report_guard_states.py:545` and
   `tests/test_report_numbers_are_sourced.py:102`, with the fenced-block count of
   the newest revision pasted to show the parse reaches it; and `pytest -q` plus a
   pushed CI run at the answering sha reading `0 failed` apart from EG3 state (1).
3. **R638**: a `REGISTERED` row for `RIGID_MODE_EXACTNESS` with both cells green,
   its injection declared in `floatfea/tolerances.py` rather than left at
   `tests/verification/rung3/test_platform_rigid_modes.py:260`, and the widening
   re-measured afterwards -- OR the measured consequence written into the entry and
   into `docs/closure/F3.md`. Either way the entry stops being silent about it.
4. **R639**: the plan's declared `3.24x` clearance asserted inside
   `test_EG0_the_THREE_COUNTERS_redden_every_member`, which already computes
   `worst_edge`.
5. **The closure list absorbed in ONE commit**, verified AFTER it exists (CZ1):
   `ruff check floatfea tests`, `black --check floatfea tests`, `mypy floatfea`,
   `pytest -q` at that commit, then `gh run list` at its own sha with the job-level
   conclusions, so the lint job's `guards and meta-tests` step is seen to have RUN.

**What does NOT hold, stated so no round is spent asking:** R635, R631 and R626's
residue stay LEDGERED and I accept the ledger; the EG4 preview stays BLOCKED on the
ground that holds and that is correct -- fix the stated ground, do not work around
it; C105 is CLOSED by my ruling and needs no work beyond regenerating section 0;
R633 and R634 are CLOSED and I will not reopen them. **Do not touch
`scripts/ci_section.py`, `scripts/write_verdict.py` or
`tests/test_report_carried.py:2019` for the deadlock -- the answer was a line in my
verdict and it is now written.**

**Schedule.** F3 closes **13 October**; F4 19 October; the member-force table 23
October; the code-check screen 28 October. **I have no measurement that contradicts
any of them.** The ladder is green on CI at this commit, all six rungs including
ladder 3, which is the measurement that would. Step 3 is now on its second HOLD and
closes at the next verdict; item 2 is two regexes and a measurement, item 3 is one
row and one declaration, item 4 is one assertion in a test that already computes
the quantity. **If round 3 closes carrying blocking items, that is the second
consecutive step to do so and CZ0 requires the choice stated to Xabier: slip 13
October, or reduce F3's scope.** I do not expect it to come to that. I still do not
endorse pulling F4 to 16 October, for verdict 84's reason: the EB6 expected side is
unmeasured.

**One sentence for the implementer.** The three repairs are right and two of them
are better than what I asked for -- the counter now depends on the gate it defends
and I proved that by planting the old body back rather than by reading the diff.
What I found instead is that F3 gave the NEW ceiling three counters and left the
OLD one -- the one your builder refuses real decks on -- open by `3784x`; and the
deadlock you refused to engineer around was a line I failed to write, which was
exactly the right call to make.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 3
Reviewed commit: 6c4e6516f5a07c0f75db67c897c9258b60b3288d
Verdict: HOLD
Judged commit: a647492e99b59eec16b0b3faf2489867d2aab596  (HEAD of F3 and pushed; the stamp above is HEAD at write time, which is corpus batch 31 at 6c4e651 -- the tool records that limitation in its own docstring)
Tests: 2976 passed, 9 failed, 0 skipped   (my own run, ONE invocation, clean tree, no exclusion, 641.69s -- not the report's 2664, and not its 270/20 excluded-set split)

## Round of 2026-10-01 -- EIGHTY-FOURTH verdict, ROUND 1 OF 3 ON STEP 3.

**THE ELEMENT WORK IS RIGHT AND I COULD NOT BREAK IT.** R624 is answered, and I
re-derived the answer rather than accepting it: the window, the emptiness of the band
window, the 16/16 counts, the three detection edges and the counter-size boundary all
reproduce on my machine, and the one figure the step needed that nobody had taken --
what the new ceiling BUYS -- is a **843x to 866x gain in the smallest defect the gate
detects.** That is the strongest result in F3 and the report does not state it.

**I HOLD ON THREE THINGS AND NONE OF THEM IS THE ELEMENT.** One is a red at the
judged commit that is NOT the step-boundary class, on both machines, at the exact
site verdict 83 named -- R629 is not closed, it changed shape. Two are sentences in
`floatfea/tolerances.py`: the new entry says its three counters are registered in a
file that does not name them, and the entry 60 lines above says nothing asserts a
constant that the production builder refuses on. Both are (b) rather than prose,
because `tolerances.py` is the one file `CLAUDE.md` makes authoritative for a
tolerance and both sentences are the only statement of what their constant is for.

## THE TREE AT a647492, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    a647492e99b59eec16b0b3faf2489867d2aab596   both -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    (no output, before any work of mine)
cmd    git log --oneline 580b183..HEAD --name-only
out    0d911ce  docs/reports/F3/step-2-answers.json, step-2.md
out    47daa3d  docs/milestones/F3.md, floatfea/tolerances.py,
out             tests/test_plan_matches_tolerances.py,
out             tests/verification/rung3/test_platform_rigid_modes.py
out    f942b83  CLAUDE.md, docs/SUPERVISOR.md
out    7e86d2a  docs/milestones/F3.md
out    a647492  docs/closure/F3.md, docs/reports/F3/step-3.md and -answers.json,
out             docs/reports/F3/step-2.md
cmd    git diff 580b183..HEAD --stat -- floatfea tests docs scripts .github .claude CLAUDE.md
out    11 files, 1310 insertions, 58 deletions
judge  FIVE COMMITS AND THE PROCESS CHANGE IS STANDALONE. f942b83 touches CLAUDE.md
       and docs/SUPERVISOR.md and NOTHING ELSE, cites EG3 and EG4e in its subject,
       and is purely additive. NO STOP-CLASS PROCESS FINDING. Verified by the diff
       rather than by the subject line -- see `## My own instructions` below.
cmd    python -m pytest -q
out    9 failed, 2976 passed, 2 warnings in 641.69s (0:10:41)
cmd    python -m pytest tests/verification/rung3/test_platform_rigid_modes.py -q -s
out    16 passed in 2.33s, and every printed figure is reproduced in R636 below
cmd    the Answers header, and the newest verdict commit
out    docs/reports/F3/step-3.md:3   Answers: verdict 83 @ 580b183
out    git log --oneline -1 580b183 -> "review: F3 step 2 -- eighty-third verdict"
judge  ITEM 1b PASSES, in one comparison. The report answers the NEWEST verdict by
       that verdict's own commit. No HOLD on this head.
```

Lint and types: not re-run by me, because CI ran them at this exact commit and that is
the stronger witness -- `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests`
are five SUCCESS steps in run 36900722535, none skipped, and `guards and meta-tests`
is seen to have RUN rather than been skipped behind an earlier red (CZ1 iii).

## CI, AT THE JUDGED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit a647492... --json conclusion,status,databaseId
out    36900722535  completed  FAILURE
cmd    gh run view 36900722535 --json jobs, job by job
out    the verification ladder            SUCCESS   13 steps
out    lint, unit and guards              FAILURE   14 steps
out    CI determinism -- leg              skipped    0 steps
out    CI determinism -- ten legs agree   skipped    0 steps
cmd    the ladder job's steps
out    ladder 1, 2, 3, 6, 4, 5 -- ALL SUCCESS. "ladder 3 -- the model is the
out    platform" is green, which is where the new ceiling and the three new cells
out    live.
judge  NOT CK2: no two-second duration, no runner-never-started, no spending
       annotation. The two skipped jobs are the workflow_dispatch gate under CK0,
       unavailable BY DECLARATION, as at verdicts 79 to 83.
cmd    gh run view 36900722535 --log-failed, the FAILED ids
out    test_the_guard_reads_the_step_being_worked_on
out    test_the_guard_survives_the_state[baseline]
out    test_the_guard_survives_the_state[non_numeric_step_suffix]
out    test_the_guard_survives_the_state[superscript_digit_step_number]
out    test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]
out    test_the_guard_survives_the_state[step_number_is_the_empty_string]
out    test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
out    test_the_guard_survives_the_state[zero_padded_step_number]
out    test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]
judge  NINE, AND CI AND MY RUN AGREE BY NAME ON ALL NINE. CI is RED at the judged
       commit and I record it as red (CA2). Eight of the nine are EG3's state (1).
       The ninth is not, and it is R632.
```

**EG0(c)'S SECOND MACHINE IS MEASURED AND THERE IS NO STOP.** The directive's stop
condition is a shipped assertion, so the question is whether the ladder passed on a
machine neither of us controls:

```
cmd    the ladder job at 47daa3d, the commit that introduced the ceiling
out    run 36898482589, "the verification ladder" SUCCESS, 13 steps, ladder 3 green
cmd    git diff 47daa3d..HEAD --stat -- floatfea tests scripts .github
out    (no output) -- the code has not moved since that run
judge  `test_EG0_the_CEILING_is_the_window_it_claims_to_be` asserts
       `clean < CEILING < weakest` AND `CEILING / clean >= 2.0`, and it passed on
       Linux at the commit that ships the code, and the code is byte-identical at
       HEAD. My own reading is 3.27x. NO STOP ON EITHER MACHINE, and the directive's
       condition is satisfied by a test result rather than by a promise, which is
       exactly how it should have been written.
```

## THE SEVEN RULINGS THE HAND-BACK ASKED FOR, SO THEY ARE ON THE PAGE

**1. a647492's message says `check_carried: all 5 findings carried` and the run says
`all 8`. The self-report is right and the repair is owed.** It is pushed, history stays
linear, and it cannot be amended. **The repair is a claim/cmd/out triple in the next
revision naming the commit, the false figure and the true one** -- and under CP2 that
triple is the whole repair: no number enters the sentence explaining it without its own
command. Closure item C104, not a block: nothing downstream reads that message.

**2. Amending f942b83 from `1281` to `1237` while unpushed was RIGHT, and I want that
said without hedging.** The rule against amending protects PUBLISHED history. An
unpushed commit has none, and a commit whose body is a claim/cmd/out triple carrying a
false `out` line is a commit that would have shipped a measurement nobody could
reproduce. Amending it is the repair; leaving it and correcting it later would have put
two numbers in history where one is right. **The part that matters more than the amend
is that section 6 records it rather than fixing it quietly** -- that is CP2 applied to
the commit that adopts a rule about pasted output, and it is the correct instinct.

**3. Three pasted-figure slips in one session is worth a rule, and here is the wording.**
The diagnosis in the hand-back is right and it is not about arithmetic: all three
figures -- 93000x, 1281, 5 -- were correct when first measured and described a tree
that had moved underneath them. BF0 says the figure carries its command; BP0 says it
carries its rule; CP2 says a repair's numbers carry theirs. **None of them says WHEN
the output is taken.** My proposed sentence, for a directive, in one paragraph:

> **A figure is pasted from the run that produced the artifact it is pasted into, and
> the pasting is the LAST edit (CP3).** Where a commit message, a report section or a
> tolerance comment carries an `out` line, that line is copied from a run executed
> after the final edit to the thing it describes -- not from a remembered run and not
> from a previous round. The consequence is an ordering and not a new check: generate,
> edit, re-run, paste, commit -- **and if an edit follows the paste, the paste is void.**
> Earned three times in one session on figures that were each correct when taken.

This is not apparatus and asks for no new guard, so CZ0 does not bar it. It goes to
Xabier through the implementer; I am not treating it as a HOLD.

**4. FOLLOWING EG0(a)'s DEFINITION OVER ITS PARENTHETICAL WAS RIGHT, and I would have
held on the parenthetical.** A parenthetical that says "approximately" is an
expectation; the definition is the specification, and where they disagree the
expectation is the thing that was wrong. The measurement settles it beyond the balance
argument: **with the WEAKEST counter response as the roof, 16/16 is true by
construction; with the WORST member's response as the roof it is not.** At 2.27e-18 the
roof is 1.464442e-17, which is rotational_block's BEST member, and the weakest member's
3.776640e-18 is then only 1.66x clear -- so the directive's own 16/16 requirement would
rest on 1.66x of a round-off quantity instead of 3.27x. Publishing both windows and
naming the disagreement is the right way to record it.

**5. EG2 TO THE CLOSURE ARTIFACT RATHER THAN TO F2a WAS YOURS TO DECIDE AND YOU DECIDED
IT CORRECTLY.** I checked the ground rather than the argument:

```
cmd    head -4 docs/milestones/F2a.md
out    "# F2 step 4a - verification apparatus"
out    "**SKELETON PLAN. Not locked. Nothing here is built.**"
rule   DZ7c says a ledgered item goes to docs/milestones/F2a.md; F2a section 7 says an
       item found after that commit "is recorded in a verdict and in the milestone's
       closure artifact, and it does not enter this plan"
judge  F2a IS NOT A LOCKED PLAN AND SAYS SO IN ITS SECOND LINE, so ledgering a measured
       finding into it would have been WEAKER than the closure artifact, not
       equivalent. DZ7c's sentence and F2a's own first line conflict; the implementer
       followed the more specific one, which is the file's own statement about itself,
       and recorded the deviation in section 10 rather than taking it. That is the
       behaviour the arrangement is for. NOT A FINDING, and I am not asking for them
       to move.
```

**6. EG4's PREVIEW IS CORRECTLY BLOCKED -- AND ONE OF ITS TWO STATED GROUNDS IS FALSE.**
I checked it rather than taking it, and the conclusion survives while the reason does
not:

```
claim  the floatfea_design_waves directory "does not exist -- the six cases have never
       been run" (report section 7, and the hand-back)
cmd    ls -la ../HSP-runs/studies/platform-12buoy/floatfea_design_waves/
out    IT EXISTS and holds SIX files, dated 27 September:
out      case_T10s_full_H24.2m_head0.csv      626250 bytes
out      case_T12.5s_full_H24.2m_head0.csv    781661
out      case_T14s_full_H24.2m_head0.csv      871739
out      case_T15s_full_H24.2m_head0.csv      931141
out      case_T16.2s_full_H24.2m_head0.csv    993608
out      case_T20s_full_H24.2m_head0.csv     1220383
judge  REFUTED BY ONE ls, and it contradicts the LOCKED PLAN's own DV2 -- "the six
       cases are run, settled and exported ... 1481.7 s total". The six periods are
       exactly DJ2(b)'s: 10.0, 12.5, 14.0, 15.0, 16.2, 20.0 s at H = 24.2 m, head 0.
claim  the export cannot supply gimbal reactions
cmd    head -1 on case_T10s..., columns counted, header grepped for
       lam reaction constraint multiplier force moment
out    21 columns: t_s, platform_heave_m, platform_heave_acc_mps2, and surge/sway/
out    heave plus acceleration for buoy1_clusterA, buoy4_clusterB, buoy7_clusterC
out    ZERO matches for any reaction-like name
rule   CLAUDE.md section Non-negotiables: never invent a load distribution
judge  THE BLOCKER STANDS, ON THIS GROUND. Nine of twelve buoys are absent, the
       platform has one DOF of six, no external force is exported, so neither the
       multipliers nor F_ext minus M a is available for any body. Refusing to invent a
       load and escalating is the right call. **But the escalation must not reach
       Xabier saying the cases were never run**, because that is the one sentence in
       it he can check in five seconds and it is false. C103.
```

**7. "NO TOLERANCE WAS WIDENED IN F3" IS TRUE AND I VERIFIED IT. "FIVE DECADES TIGHTER"
IS FALSE.**

```
cmd    git diff 580b183..HEAD -- floatfea/tolerances.py, the value lines only
out    + PLATFORM_RIGID_MODE_EXACTNESS: Final[float] = 1.154338e-18
out    + PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT: Final[float] = 1.0e-14
out    no existing NAME = value line changed, in either direction
cmd    1e-15 / 1.154338e-18
out    866.3x, which is 2.94 decades
cmd    where the claim is written
out    docs/closure/F3.md:154 and docs/reports/F3/step-3.md:512 -- "five decades"
rule   a tolerance change requires a written justification naming the physical or
       numerical reason the previous value was incorrect (CLAUDE.md section Tolerances)
judge  THE DIRECTION IS RIGHT AND THE JUSTIFICATION IS SOUND: the gate's threshold
       moved from 1e-15 to 1.154338e-18, which is strictly stronger, the reason is in
       the entry, and the previous value's own entry pre-registered the re-derivation
       in words I quote in R634. THE MAGNITUDE IS WRONG BY TWO ORDERS AND NO READING
       GIVES FIVE: 1e-14/1.154338e-18 is 3.94 decades and 1e-15/1.154338e-18 is 2.94.
       It is a figure, so C101 and not a block -- but it is the fourth pasted figure of
       the session and it is in the closure artifact, which is the document a later
       reader trusts most.
```

## Carried

Verdict 83 carried five items by name and listed them as blocking in step 3.

* **R624 -- ANSWERED at 47daa3d, and I re-derived it rather than accepting it.** The
  substance is in R636 below. Both halves land: the gate gets its own ceiling, and the
  refusal keeps `1e-15` with the emptiness of the band window stated as the reason.
  **My independent sweep confirms the emptiness, which is the load-bearing half:**

```
cmd    40000 admissible (D_o, t/D_o, L) points, L constrained to L/D >= 2 and
       L/r <= 300, S355-equivalent; worst clean element_rigid_residual and weakest
       response over the three counters at the declared 1e-14
out    clean worst     1.872454e-17  at D_o 1.1791, t/D_o 0.011654, L 2.4762
out    weakest counter 1.569787e-19  rotational_block at D_o 4.0845, t/D_o 0.17689,
out                                  L 364.51
rule   a single ceiling would have to sit above every clean reading and below every
       counter response
judge  THE FLOOR IS ABOVE THE ROOF BY 119.3x, ON A GRID NEITHER OF US DESIGNED
       TOGETHER. The decision is sound and R624 is CLOSED. My counter figure agrees
       with the plan's 1.571633e-19 to three figures; my clean worst is 3.54x WORSE
       than the published 5.287607e-18 and consistent with verdict 83's own
       1.956747e-17, which is C102 and not a change to the ruling.
```

* **R629 -- NOT CLOSED. IT CHANGED SHAPE AND IT IS RED ON BOTH MACHINES. R632.** The
  fix at 0d911ce took the data half of the closing condition and neither of the two
  alternatives the condition required. The vacuity is gone from step 2's report and
  the guard is unchanged -- and step 3's own answers file puts fourteen of twenty-two
  rows back at section 9, which is again a bulleted list naming every item. The state
  now fails earlier than it used to: it cannot be BUILT.
* **R630 -- ANSWERED at 47daa3d, verified line by line, and answered better than I
  asked.** The condition was that the test comment name which end of the sixteen its
  three edges are. It does more: it carries THREE labelled sets -- the best member,
  the worst against the retired ceiling, the worst against the ceiling that ships --
  each with its rule, and the third is printed per run by the new cell rather than
  typed. I re-bisected all three sets and every figure reproduces:
  `6.266629e-17` on platform:hub4_arm, `1.262927e-18` on hub4:buoy12_arm,
  `3.088842e-15` on platform:hub4_arm, spreads 2.14x, 1.03x, 3.93x. **And no injection
  size was chosen against the best member:** the declared `1.0e-14` clears the WORST
  edge `3.088842e-15` by 3.24x, which is the condition's second half.
* **R631 -- OPEN, LEDGERED to `docs/closure/F3.md` section 4, and I ACCEPT the ledger
  under DZ7c.** No value moves, nothing it touches can change a member force or the
  G4.1 equilibrium check, and DZ7c's standing answer is reduce scope rather than slip.
  Element (iii) of its condition -- the insensitivity window -- is still unmeasured and
  the ledger says so. **It does not carry as blocking into F4; it carries as a
  recorded item in the closure artifact**, which is what DZ7c asks for this class.
* **R626's residue -- OPEN, LEDGERED to the same place, same ruling.** The two
  boundaries are written in verdict 83 and quoted in the ledger, so nothing has to be
  re-derived by whoever picks it up.
* **C88 -- STILL OPEN and its one condition WAS NOT MET.** Verdict 83 ruled that it
  waits for the closure commit with one condition: "it lands BEFORE step 3 chooses an
  injection size, because step 3 reads those rows." Step 3 chose `1.0e-14` and the
  plan block's citation is untouched at this commit. **The choice turned out right
  anyway -- I verified it against the worst member -- so this is a closure item and not
  a block**, but the condition was a condition and it was missed, and I am recording
  that rather than quietly re-ruling it.
* **C97, C98, C99, C100 -- C99 is CLOSED at f942b83**, in my own wording, unparaphrased,
  with EG3's two conditions beside it. C97, C98 and C100 are untouched and still
  closure.
* **C86, C90, C91, C92, C93, C94, C95, C96 -- STILL OPEN, closure, not re-reviewed.**
  Nothing on that list has become blocking in my reading this round.
* **C74, C76, C78, C82, C85, R610, R615 -- carried unchanged, no work asked.**
* **C40 -- CLOSED at 47daa3d, and I checked the repair rather than the claim.** The
  plan guard reads every `docs/milestones/F*.md` now and names the file it read in its
  failure message. One residue, C107: the glob reaches two files that are not locked
  plans.
* **C75, C75b -- closed and still closed.** `ruff`, `black --check` and `mypy` all
  SUCCEEDED on CI at this commit.
* **R611, R617 withdrawn and staying withdrawn. R612, R613, R614, R616, R618 to R621,
  R623, R625, R627, R628 closed as ruled at 79, 81, 82 and 83. R622 is F4. C89 stays
  withdrawn.**
* **C58 to C64, C65 to C73, C56(iii), C56(iv), C57 -- as ruled at verdicts 77 to 83.**
  This step's diff touches none of them.

## Findings

**R632. (d, BLOCKING) ONE OF THE NINE REDS IS NOT THE STEP-BOUNDARY CLASS. THE PLANT
ACTION CANNOT BUILD ITS STATE AGAINST A FIRST-REVISION REPORT, SO IT RAISES BEFORE
ANYTHING IS MEASURED -- AND THIS WILL RECUR AT EVERY FIRST REVISION OF EVERY STEP.**
EG3(i) requires each FAILED id matched by name to the state's own list. I matched all
nine by CAUSE and not by family, which is the lesson R629 was:

```
cmd    python -m pytest tests/test_report_guard_states.py -q --tb=line
out    8 failed, 16 passed in 165.97s
out    tests/test_report_guard_states.py:777: AssertionError:
out      zero_padded_step_number: a file that is not a numbered step must be stepped
out      over, not reacted to.   assert 1 == 0
out    tests/test_report_guard_states.py:545: ValueError: substring not found
cmd    the baseline's own nested failure
out    "step 3 has a report and no verdict yet. That is the legitimate boundary ...
out     Invoke the gating-supervisor."    assert 3 == 2
cmd    tests/test_report_guard_states.py:539-546, the pointers_all_at_carried action
out    head = text.rindex(the literal hash-Revision-space)
cmd    count that heading in the two reports
out    docs/reports/F3/step-2.md   1
out    docs/reports/F3/step-3.md   0
rule   EG3(i): the waiver applies only if EVERY red traces BY NAME to the
       step-boundary cause, and a red that does not match is CZ1 (iv) unchanged
judge  EIGHT OF NINE ARE STATE (1): the baseline fails because step 3 has a report and
       no verdict, and seven planted states cascade off it with assert 1 == 0. THE
       NINTH FAILS INSIDE THE HARNESS, with a ValueError in the plant action, and its
       cause has NOTHING TO DO WITH WHETHER A VERDICT EXISTS -- step-3.md is revision
       1 and carries no revision heading, so rindex raises and the state is never
       built. The verdict I am writing will clear the other eight. It will not clear
       this one.
```

**This is R629 in a second shape and the shape is worse**: before, the state planted and
could not discriminate; now it cannot plant at all, so a guard that is supposed to prove
the pointer check can fail instead reports a Python error. CZ0 is explicit that an
existing guard that fails false is fixed or deleted, never extended, and a guard that
raises on a legitimate tree state is failing false.

**Closed when** one of two things, both inside CZ0: **(i)** the plant action handles a
report with no revision heading -- plant into the whole file when there is no revision
boundary -- and the state then REDDENS, demonstrated by the nested run's own failure
line rather than by the state merely passing; or **(ii)** the state is deleted under DR1
and its vacuity is recorded in the closure artifact, standing in my corpus row as what
was measured. **And in either case**, `docs/reports/F3/step-3-answers.json` points
fourteen of its twenty-two rows at section 9 of step-3.md, which is "Where each carried
item stands" -- a bulleted list naming every item. That is the same pointer-that-cannot-
discriminate the original R629 was about, reproduced in the file written one commit
after it was fixed. **At the answering commit `python -m pytest -q` reads `0 failed`
apart from EG3 state (1), and a pushed CI run at that sha shows the same.**

**R633. (b, BLOCKING) THE NEW ENTRY'S FIRST SENTENCE SAYS ITS THREE COUNTERS ARE
REGISTERED IN `tests/test_counters_are_injected.py`. THEY ARE NOT, THE LOCKED PLAN
REQUIRES THEM TO BE, AND I MEASURED THAT THE COUNTER AS WRITTEN CANNOT BE REGISTERED --
IT FAILS THE GATE CELL ON ALL THREE KINDS.** This is not a missing table row.

```
cmd    grep -rn "PLATFORM_RIGID_MODE_EXACTNESS" tests/test_counters_are_injected.py
out    (no output)
cmd    git diff 580b183..HEAD --stat -- tests/test_counters_are_injected.py
out    (no output) -- the file is untouched by this step
cmd    floatfea/tolerances.py:354-355, the new entry's opening
out    "CLASS: ACCURACY -- hosts the three element-local counters registered in
out     tests/test_counters_are_injected.py against G2.1's gate on the real platform."
cmd    docs/milestones/F3.md section 5, the locked requirement
out    "And its three counters go back into the injection guard. ... here it is an
out    assertion again, so dropped_flip, wrong_dof_index and rotational_block are
out    registered against it."
cmd    tests/test_counters_are_injected.py:317-319, the guard's own promise
out    "It goes back UP in F3, where the element-local check becomes an assertion on
out    every real platform member and its three counters are registered against that
out    gate."
cmd    the registry, and what the completeness meta-test asserts
out    REGISTERED holds FOUR rows; test_there_is_something_to_check asserts
out    len(REGISTERED) >= 4 -- so a fifth constant with no row is invisible to the one
out    meta-test whose docstring says "A constant with no counter registered here is
out    not covered at all"
rule   (b): a tolerance's counter and HOW IT IS INJECTED. BX0's two cells are what
       prove a counter is not self-asserting; a constant absent from the registry has
       neither cell run against it.
judge  FOUR PLACES IN THE TREE SAY THIS HAPPENED OR WILL HAPPEN IN F3, F3 IS BEING
       CLOSED, AND IT DID NOT HAPPEN. And the omission is not clerical:
```

```
cmd    build the REGISTERED row by hand for test_EG0_the_THREE_COUNTERS_redden_every_
       member and run both BX0 cells per kind -- gate cell neuters
       test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions, ceiling cell widens
       PLATFORM_RIGID_MODE_EXACTNESS to 10 x 1e-14
out    dropped_flip      gate cell False   ceiling cell True
out    wrong_dof_index   gate cell False   ceiling cell True
out    rotational_block  gate cell False   ceiling cell True
rule   test_the_counter_fails_when_its_gate_is_neutered asserts the gate cell is True;
       test_the_counter_fails_when_its_ceiling_is_widened asserts the ceiling cell is
judge  THE CEILING CELL PASSES ON ALL THREE -- the counter IS sized by the constant, so
       the substance is sound and I am not claiming the counter is defective. THE GATE
       CELL FAILS ON ALL THREE, because the counter reimplements the comparison
       `r > PLATFORM_RIGID_MODE_EXACTNESS` inline instead of calling the gate it
       defends: neuter the gate and the counter still passes, which is precisely what
       that cell reports as self-asserting. Registering it is therefore a CODE CHANGE
       with a design decision in it, not a one-line addition a closure commit absorbs,
       and that is why this is (b) and blocks rather than going on the closure list.
```

**Closed when** one of three, and the choice is the implementer's: **(i)** the counter
runs the gate -- call `test_G2_1_every_MEMBER_annihilates_its_six_RIGID_motions` under
`pytest.raises` with `member_stiffnesses` patched to return the injected rows, which is
why that function is module-level and not a fixture -- and a row is added to
`REGISTERED`, with both cells green and the `>= 4` in `test_there_is_something_to_check`
moved to `>= 5` so the registry cannot silently lose it again; or **(ii)** all four
sentences are corrected to say what is true -- that the counters are asserted 16/16 by
`tests/verification/rung3/test_platform_rigid_modes.py` and are NOT in the BX0 registry,
with the reason -- in `floatfea/tolerances.py:354-355`, `docs/milestones/F3.md` section 5
and section 7, and `tests/test_counters_are_injected.py:317-319`; or **(iii)** the
registration is ruled out of scope by directive, in which case all four sentences change
anyway. **What may not stand is the present state: a tolerance entry naming a guard that
does not read it.** No new apparatus in any branch -- (i) adds a row to an existing list,
(ii) deletes four sentences.

**R634. (b, BLOCKING) `floatfea/tolerances.py` SAYS NOTHING ASSERTS
`RIGID_MODE_EXACTNESS` AND THAT IT BOUNDS NOTHING, SEVENTY-THREE LINES ABOVE A SENTENCE
THIS STEP'S OWN COMMIT WROTE SAYING THE PRODUCTION BUILDER KEEPS IT. ONE FILE, TWO
ANSWERS, AND THE LIVE ONE IS A REFUSAL ON THE PRODUCTION PATH.**

```
cmd    floatfea/tolerances.py:330
out    "AND NOTHING ASSERTS THIS CONSTANT ANY MORE (DI0, R530)."
cmd    floatfea/tolerances.py:345-348
out    "The constant is kept because the diagnostic and the closure artifact both read
out    it as the scale the retired quantity was measured against. Its CLASS line above
out    still says ACCURACY and that is now wrong in spirit: it bounds nothing."
cmd    grep -rn "RIGID_MODE_EXACTNESS" floatfea/ | grep -v PLATFORM
out    floatfea/model/platform.py:319    if residual > RIGID_MODE_EXACTNESS:
out    floatfea/model/platform.py:320    raise ValueError(... "The platform is refused
out      rather than analysed (F3 section 5, G2.1).")
cmd    floatfea/tolerances.py:403, written by THIS STEP at 47daa3d
out    "floatfea.model.platform.check_rigid_modes keeps RIGID_MODE_EXACTNESS, because
out    the refusal's subject is every deck a reader could write"
rule   CW0: a claim about this repository written in a comment is a test, a triple, or
       deleted -- and (b), because this paragraph is the ONLY statement of what this
       constant is for and the constant is the threshold the builder refuses on
judge  THE SENTENCE WAS TRUE WHEN WRITTEN AND THE REFUSAL LANDED AFTER IT, so it is
       pre-existing and I am not pretending otherwise. But THIS STEP is the commit that
       split the two ceilings and made this entry the record of the REFUSAL's ceiling,
       and it is the commit that wrote the contradicting sentence into the same file.
       docs/closure/F3.md section 3 now publishes RIGID_MODE_EXACTNESS in a column
       headed "the refusal", so a reader sent there arrives at an entry saying the value
       bounds nothing. A reader deciding whether 1e-15 may move would be told by its own
       Reason paragraph that nothing depends on it, and the production builder would
       stop refusing a defective deck.
```

**Closed when** lines 330 and 345-348 say what is true at the commit that publishes them:
that `RIGID_MODE_EXACTNESS` is asserted by `check_rigid_modes` at
`floatfea/model/platform.py:319` as the G2.1 REFUSAL's ceiling, that its subject is every
deck a reader could write, that no counter is registered against it and why -- the band
window is empty, which I confirmed independently at 119.3x -- and that what DI0 and R530
retired is the F2 claim-A assertion rather than every use of the constant. The
`CLASS: ACCURACY` line is then correct rather than "wrong in spirit". **The
pre-registration sentence at lines 348-352 is kept exactly as written, because EG0
fulfilled it to the letter and that is worth a later reader seeing.** No value moves.

**R635. (c, NOT BLOCKING, recorded with its measurement because it will fire) THE WINDOW
IS GUARDED ASYMMETRICALLY, AND EG0(c)'s 2x CLAUSE FIRES ON ROUTINE LEGAL CHANGES WHILE
THE DIRECTIVE AND THE TOLERANCE ENTRY GIVE OPPOSITE INSTRUCTIONS FOR WHAT TO DO THEN.**
The gate is correct today; this is about the next section change.

```
cmd    which assertion binds each side of the window, and at what factor
out    floor  PLATFORM_RIGID_MODE_EXACTNESS / clean >= 2.0, in
out           test_EG0_the_CEILING_is_the_window_it_claims_to_be         2x
out    roof   reddened == 16, in test_EG0_the_THREE_COUNTERS_redden_every_member   1x
judge  A SYMMETRIC WINDOW GUARDED ASYMMETRICALLY. Both margins read 3.27x today; a
       3.27x drift of the rotational_block response reddens the roof with no warning
       band first, while the same drift on the clean side is caught at 2x. That is the
       directive's design rather than a defect, and it is worth knowing which side has
       no margin clause.
cmd    hold the sixteen-member geometry and move the arm wall through the legal range,
       reading the clean worst as a fraction of the ceiling
out    t = 150 mm  0.35x     t = 160 mm  0.19x     t = 170 mm  0.87x
out    t = 175 mm  0.12x     t = 180 mm  0.08x     t = 185 mm  0.78x
out    t = 190 mm  0.34x     t = 200 mm  0.23x     t = 220 mm  0.37x
out    t = 250 mm  0.29x
cmd    the same with E at 200 GPa instead of 210, section and lengths held
out    clean worst 7.786002e-19 = 0.67x the ceiling, so 1.48x inside
rule   EG0(c): if either machine's clean worst comes within 2x of the ceiling, STOP and
       report; do not move the ceiling
judge  TWO OF TEN LEGAL WALL THICKNESSES AND ONE ROUTINE GRADE CHANGE LAND INSIDE THE
       STOP BAND -- 170 mm at 1.15x, 185 mm at 1.29x, 200 GPa at 1.48x -- and F1's own
       order check brackets exactly that thickness range ("t ~ 175 mm closes it, so
       180 mm is the buildable number"), with DV0 recording that the section "should be
       re-examined, not treated as settled". The clean worst is round-off scatter and
       not a trend: it moves between 0.08x and 0.87x across neighbouring thicknesses.
       So the first time the arm is re-sized the shipped gate STOPs, and EG0(c) says do
       not move the ceiling while the entry says "this value is re-derived rather than
       re-justified". Those are two instructions and they disagree.
```

**My reading, offered so the next round does not spend itself on it:** the entry is right
and EG0(c) means "do not WIDEN the ceiling to rescue a red", not "never re-derive it". A
re-derivation at a changed section is a new measurement of the same rule, and BP0 already
requires every figure citing the old ceiling to move with it. **That needs a sentence
where a later reader finds it, and it is a directive rather than a round.** Not blocking:
no assertion is wrong today, every figure reproduces, and the risk is dated rather than
present.

**R636. (NOT A FINDING -- THE RESULT, RECORDED BECAUSE NOBODY MEASURED IT AND IT IS THE
BEST THING IN F3.)** What the new ceiling BUYS. The report justifies the change by what
the old ceiling could not do; the stronger statement is what the new one can:

```
cmd    per member, bisect the injection size at which the residual crosses the ceiling;
       take the LARGEST over the sixteen; against 1e-15 and against 1.154338e-18
out    dropped_flip      5.285599e-14 -> 6.266629e-17    843.5x smaller
out    wrong_dof_index   1.094071e-15 -> 1.262927e-18    866.3x smaller
out    rotational_block  2.642868e-12 -> 3.088842e-15    855.6x smaller
rule   element_rigid_residual(k_local, L) <= the ceiling, per member, worst over the
       sixteen
judge  THE GATE NOW DETECTS DEFECTS ABOUT 850x SMALLER ON EVERY MEMBER. That is what
       makes this a tightening rather than a renaming, and it is the sentence I would
       have put in the closure artifact instead of "five decades".
cmd    the window as a decision rule, inverted and solved on both edges
out    lowest ceiling the shipped assertions accept   7.056514e-19 (the 2x clause)
out    highest ceiling they accept                    just under 3.776640e-18
out    so the constant is pinned inside a 5.35x interval, 1.64x and 3.27x from its edges
cmd    invert the COUNTER-SIZE rule and bisect
out    at 3.100e-15 all three counters read 16/16; at 3.050e-15 the worst reads 12/16
out    so the declared 1.0e-14 clears a SOLVED boundary by 3.24x
cmd    the same platform expressed in millimetres, a thousand-fold unit change
out    clean worst 0.33x the ceiling, weakest counter 3.28x -- STILL INSIDE
judge  FOUR THINGS A CEILING USUALLY DOES NOT HAVE: both edges solved rather than
       sampled, a counter size measured against a bisected boundary, a pinning interval
       narrower than one decade, and survival of the unit-scaling case that moved the
       RIGID_MODE_BOUND band figure by 24x. I tried to break this and could not.
cmd    and one reach boundary, so the tightening is not over-read
out    the WHOLE MATRIX negated: residual 8.7211e-20 clean, 8.7211e-20 negated, against
out    a ceiling of 1.154338e-18
judge  866x of extra sensitivity buys NOTHING against a sign error. R625's signed clause
       is still the only thing that sees one, and that deserves a sentence beside a
       ceiling advertised as a sensitivity gain.
```

## Closure items

Named, not re-reviewed, none of them holding anything. Fix the list once in the step
closure commit and verify it AFTER it exists (CZ1).

* **C101.** "five decades tighter" at `docs/closure/F3.md:154` and
  `docs/reports/F3/step-3.md:512`. The ratio is `866.3x`, which is 2.94 decades; the
  direction is right and verified. **Closes when** both places carry the measured ratio,
  and R636's `843.5x / 866.3x / 855.6x` detection gain is the figure that replaces it,
  since that is what the reader wants from the sentence.
* **C102.** `docs/closure/F3.md:69` and `docs/milestones/F3.md:677` pair the refusal's
  clean worst `5.287607e-18` with the margin `51.1x` in the same cell. `1e-15` over
  `5.287607e-18` is `189x`; `51.1x` belongs to verdict 83's `1.956747e-17`, and my own
  40000-point grid this round found `1.872454e-17`. The plan's phrasing "sits 51.1x inside
  the clean worst" also reads backwards. **Closes when** the cell carries one sweep's
  worst and that sweep's margin, with the worst of every grid tried -- `1.956747e-17` is
  the number today.
* **C103.** `docs/reports/F3/step-3.md` section 7 and the escalation it feeds say the six
  design-wave cases have never been run and the export directory does not exist. Six CSVs
  dated 27 September are there, which is what the locked plan's own DV2 records.
  **Closes when** the escalation reaches Xabier on the ground that holds -- 21 columns, no
  reaction, no external force, nine of twelve buoys absent -- and the false ground is
  struck in place.
* **C104.** `a647492`'s message says `check_carried: all 5 findings carried`; the run says
  `all 8`. Pushed and unamendable. **Closes when** the next revision carries a
  claim/cmd/out triple naming the commit, the false figure and the true one, with every
  number in the explanation inside its own triple (CP2).
* **C105.** The report's section 0 is headed "CI at `29570e1`, the commit verdict 83
  judged". Verdict 83 judged `b105de1` and its own stamp reads `5a2ff21`; `29570e1` is
  verdict 81's. `scripts/ci_section.py` is resolving the OLDEST `Reviewed commit:` line in
  the verdict file rather than the newest, which is the DX2 append-ordering trap one file
  over. Section 0a does cover this round's commits, so nothing is hidden -- but the table
  is labelled with the wrong commit. **Closes when** the anchor is the newest round's
  judged commit, or the heading says which round it is about.
* **C106.** `tests/verification/rung3/test_platform_rigid_modes.py:326-340` duplicates
  `scripts/rigid_counter_response.py:82-92`. The two are equivalent today -- I compared
  them -- and the only statement that the gate and the published sweep inject the same
  defect is the docstring. Nothing imports, nothing compares. **Closes when** the test
  imports the script's shape or the docstring stops claiming provenance it cannot carry.
* **C107.** `tests/test_plan_matches_tolerances.py:40` globs `docs/milestones/F*.md`, which
  returns `F2a.md` ("SKELETON PLAN. Not locked.") and `F2_figures.md` ("GENERATED, do not
  edit") beside the three locked plans. A tolerance value written into either would satisfy
  `test_every_declared_tolerance_appears_in_the_plan`. Latent, not live: 56 rows come from
  F2.md, 3 from F3.md, zero from the other three. **Closes when** the list is the locked
  plans or the set of files read is asserted.
* **C108.** `docs/closure/F3.md` section 5, "What is red at the closing commit", states a
  pointer and no content. **Closes when** it names the nine FAILED ids at the closing
  commit and the cause of each, which after R632 is eight in one class and one in another.
* **C109.** `docs/milestones/F3.md` now runs 0,1,2,3,4,5,7,8 -- the new section 7 was
  inserted and the old section 6 renumbered to 8, so there is no section 6.
  **Closes when** the numbering is contiguous or the gap is stated.
* **C88** -- still open, its one timing condition missed; ruled in `## Carried`.
* **C97, C98, C100, C86, C90, C91, C92, C93, C94, C95, C96** -- carried unchanged.
* **C74, C76, C78, C82, C85, R610, R615** -- ledger lines, carried unchanged.
* **C89** -- withdrawn and staying withdrawn. **C99, C40** -- CLOSED this round.

## Tolerances touched

```
cmd  git diff 580b183..HEAD --numstat -- floatfea/tolerances.py
out  80  0
cmd  the same diff, lines matching a NAME = value declaration
out  + PLATFORM_RIGID_MODE_EXACTNESS: Final[float] = 1.154338e-18
out  + PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT: Final[float] = 1.0e-14
out  no existing NAME = value line changed, in either direction
cmd  git diff 580b183..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep -i conftest
out  tests/conftest.py and tests/test_supervisor_conftest_pathspec.py -- one conftest
out  in the tree; no rung carries its own, and no plugin is loaded from tests/
cmd  tests/conftest.py, read line by line (CH2), unchanged this round and read anyway
out  it registers a hypothesis profile, adds a rung marker from the directory and SORTS
out  items by rung. No pytest_runtest_makereport, no pytest_ignore_collect, no
out  pytest_collection_modifyitems that removes an item, no outcome written.
judge  TWO VALUES DECLARED, NONE WIDENED, NO GOLDEN AND NO PARAMETRISATION LOOSENED.
       The one ASSERTION that moved -- the G2.1 gate's ceiling -- moved DOWN by 866.3x,
       which I verified by bisecting the detection edge before and after (R636). A
       tolerance declared in the same commit as the code that reads it is normally the
       finding; here the code is a new gate and the value is derived from a window the
       same commit measures, with both edges solved. That is the admissible form of it.
```

| constant | value | form | counter | justification located |
|---|---|---|---|---|
| `PLATFORM_RIGID_MODE_EXACTNESS` | `1.154338e-18`, NEW | relative and dimensionless -- the element-local residual is homogenised by `S^-1 k S^-1`, so span, orientation and reference point leave the quantity; correct form | `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1.0e-14`, three shapes, 16/16 each, binding edge `3.088842e-15` cleared by `3.24x`. **The counter is a detection THRESHOLD and not one perturbation** -- I re-bisected it and found `12/16` at `3.050e-15` | `floatfea/tolerances.py:354-409`, the table in `docs/milestones/F3.md:667`, and the derivation re-run by `test_EG0_the_CEILING_is_the_window_it_claims_to_be` at every run rather than typed (BI3 satisfied). **The one false sentence in it is R633.** |
| `PLATFORM_RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | `1.0e-14`, NEW | a fraction of `max abs k_e`, dimensionless; correct form | it IS the counter | `floatfea/tolerances.py:411-434`. The reuse of `RIGID_MODE_EXACTNESS_COUNTER_DEFECT`'s value is argued rather than assumed, and the entry says what would separate them. **R633 applies here too: nothing in the BX0 registry reads this name.** |
| `RIGID_MODE_EXACTNESS` | `1e-15`, UNCHANGED | unchanged | **none, and none is possible** -- the band window is empty, which I confirmed independently at `119.3x` | its own entry, and that entry is **R634**: it says nothing asserts the constant while `floatfea/model/platform.py:319` refuses on it. |
| `RIGID_MODE_BOUND` | `199.526231496888`, UNCHANGED | unchanged | unchanged | unchanged. **R631** is its open residue, ledgered. |

## My own instructions (4b), read line by line

```
cmd  git diff 580b183..HEAD --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out  CLAUDE.md 43 +, docs/SUPERVISOR.md 42 +, 0 deletions
cmd  git show --stat f942b83
out  CLAUDE.md and docs/SUPERVISOR.md ONLY. No floatfea/, no tests/, no scripts/.
cmd  git log --oneline 580b183..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out  f942b83 only -- one commit, and its subject cites EG3 and EG4e
judge  NO STOP-CLASS PROCESS FINDING, and I verified it the way the rule requires:
       by the diff, not by the subject. The change is a standalone `process:` commit
       citing the directives that asked for it, it is PURELY ADDITIVE -- 85 insertions,
       zero deletions, measured -- and no guard is removed, weakened or narrowed.
       Both files receive the same two blocks. The CZ1 carve-out block is MY verdict-83
       wording with the sharpening quoted verbatim, which is what C99 asked for, and
       EG3's two conditions are added beside it rather than inside it. `.claude/` is
       untouched. C99 is CLOSED.
cmd  and the one thing I checked that the diff does not show: does the carve-out
     NARROW what I must read or carry?
out  No. It waives a PRE-INVOCATION green requirement on the implementer's side and
out  adds condition (i) requiring the trace pasted per id and condition (ii) requiring
out  the verdict commit measured. Both increase what is measured. Nothing in it
out  changes what I diff, what I carry, or what I may write.
```

## THE EXCLUSION: DID IT HIDE ANYTHING? YES, AND IT IS R632

```
cmd    the report's own whole-suite line, section 12
out    "Whole suite at 7e86d2a: 2664 passed, 0 failed, 0 skipped" and "the excluded
out    set: 270 passed, 20 failed", measured at 7e86d2a -- the commit BEFORE the report
cmd    my own run, whole tree, no exclusion, at the committed revision a647492
out    9 failed, 2976 passed
judge  THE TWO ARE NOT COMPARABLE AND NEITHER IS WRONG. The report's is the tree minus
       three files at the commit before the report existed; mine is the whole tree at
       the commit that ships it. CZ1's reusable half is exactly this: the plant action
       reads the NEWEST report, and at 7e86d2a the newest report was step-2.md, which
       HAS a revision heading. The ValueError cannot exist until step-3.md is committed,
       so no run the implementer could have taken before committing would have shown it.
       THE NUMBER THAT DECIDES ANYTHING IS MINE, AND IT IS 9 FAILED.
cmd    the report's EG3(i) trace, section 12
out    "THE EXCLUDED SET'S 20 ARE THAT CASCADE" -- asserted for the family, with three
out    ids traced individually and seventeen by class
rule   EG3(i): each FAILED id is matched to the state's own list, not "the failures look
       like the boundary set"
judge  THE TRACE IS THE RIGHT SHAPE AND IT IS NOT FINISHED. The report is right that the
       condition caught two gaps in the clause's state-(2) list on CI, and right to
       record them as unlisted rather than waived -- that is the condition working. What
       it did not do is give each of the twenty a cause, and the one that needed it is
       the one that is not the boundary. EG3(i) earned itself on its first use, twice
       over: once the way the report describes, and once the way it did not.
```

**On the two UNLISTED ids the report flags for a directive, my ruling:**
`test_the_answered_verdict_is_the_NEWEST_one` and the `the_guard_survives_the_state`
cascade at `47daa3d` ARE state (2) by cause -- the report in the tree answered verdict 82
while 83 existed, and the baseline cascade follows -- and the clause's list does not name
them. **Recording them as unlisted rather than waived was the correct call and I would
have found a widened list a worse answer.** The list was written from one observation; it
is short by two names on each side. **My wording, so the channel is a verdict and not an
agent message:** *state (1)'s list is `test_the_guard_reads_the_step_being_worked_on` and
`test_the_answered_verdict_is_the_NEWEST_one`, plus the planted states that cascade off a
red baseline; state (2)'s is the five named plus the same cascade. In both states the
cascade is identified by the baseline being red and by each cascading state's own failure
line, not by its name.* That is four lines and it narrows nothing.

## The adversarial corpus (BE3)

`tests/corpus/platform_ceiling_and_counter_registration.txt`, batch 31, committed
separately from this verdict at `6c4e651`. **TWENTY-SIX ENTRIES, ALL TWENTY-SIX UNSEEN.**
In scope under DE2: the element, the gates, the platform model; section E is the
report-guard harness, in scope because it holds the only red here that is not the step
boundary.

**FOURTEEN ROWS PREDICT `caught`. ONE READS CAUGHT.** That is the worst coverage of the
milestone -- batch 29 was 8 of 13, batch 30 was 5 of 10 -- and the shape of the miss is
again the finding: **not one of the thirteen misses is the element.** Eight are sentences
in `floatfea/`, `tests/` and the artifacts that no check reads (R633, R634, C101, C102,
C103, C106, and the two record rows); five are reach boundaries of the new ceiling and of
two guards that nothing was asked to measure (R635, C107, and the registry's `>= 4`).
**The one that reads CAUGHT is R632**, and it is caught as a hard error rather than as a
reported defect, which is the finding rather than the coverage.

**Two rows are `expect=blind` and both matter.** The millimetre unit system: the ceiling
stays inside the window under a thousand-fold change of length unit, which is the first
figure in this family that survives that case -- batch 30 measured the `RIGID_MODE_BOUND`
band reading moving `24x`. And the whole matrix negated: `866x` of extra residual
sensitivity buys nothing against a sign error.

```
cmd  grep -c "^id=" tests/corpus/platform_ceiling_and_counter_registration.txt
out  26
cmd  grep -rn "platform_ceiling_and_counter_registration" tests/ scripts/ --include=*.py
out  (no output) -- named by no .py
cmd  python -m pytest tests/test_collected_set_golden.py
       tests/test_marker_exemption_corpus.py tests/test_report_vocabulary_corpus.py
       tests/test_tree_prose_consistent.py tests/test_ci_ladder_gating.py -q
out  300 passed in 132.51s        exit 0
judge  THE CORPUS COMMIT REDDENS NOTHING, measured and not reasoned.
```

**EG4(e) notes that batches pause AFTER this step, so this is the last general batch.**
F4's load-mapping gate and EB6's label-provenance gate continue, and on the measurement
above that is the right place to spend: thirteen of fourteen misses this round were
records rather than reachable defects, and the two surfaces EG4(e) keeps open are the two
where a miss reaches a member force.

Every mutation was applied in a scratch harness under the session scratch directory,
importing the shipped functions; nothing in the working tree was written.
`git status --porcelain --untracked-files=all` was empty before I began, and the only
paths I have written in this repository are that corpus file and this verdict.

## On the criterion

**I ruled under CZ0 and I have no complaint about the criterion this round.** Of my six
numbered items, one is (d) measured on two machines, two are (b) in `floatfea/tolerances.py`,
one is (c) recorded and explicitly not blocking, one is a result rather than a finding, and
nine are closure items I have named and will not re-review. **No round was spent on prose
and no round was spent re-reading the closure list**, which is what CZ0 is for.

**One thing I want on the record about the shape of this HOLD, because it is unusual.**
Two of my three blocking items are SENTENCES, which CZ0 retires as a blocking head, and I
am blocking on them anyway on the ground my own instructions give: *a docstring that is
the only statement of what a tolerance means*. Both qualify exactly. R633's sentence names
a guard as the thing that proves a counter is not self-asserting, and I measured that the
guard does not read it and cannot as written -- that is not "a figure is wrong", it is
"the mechanism named does not exist". R634's paragraph tells a reader that a constant the
production builder refuses on bounds nothing. **If either had been a sentence about a
measurement rather than about a mechanism, I would have put it on the closure list, and
verdict 83's sharpening is the test I used: does moving the sentence move a decision?**
For both, yes.

**And the cap.** This is round 1 of 3 on step 3. The three blocking items are one guard
repair, one registry decision, and one paragraph rewrite; none of them is a day of work,
and none of them touches a number. If they land, step 3 closes at round 2 and F3 closes
with it.

## Next step opens when

**Step 3 is HELD. These are answered before anything else, and F3 does not close until
they are.** The specific conditions, so that "address the above" is not what this says:

1. **R632.** `python -m pytest -q` at the answering commit reads `0 failed` apart from
   EG3 state (1), and the pushed CI run at that sha reads the same. The
   `pointers_all_at_carried` state either plants against a first-revision report and is
   shown to REDDEN by the nested run's own failure line, or is deleted under DR1 with its
   vacuity recorded. `docs/reports/F3/step-3-answers.json` points each item at the section
   that does its work rather than at the one that lists them all.
2. **R633.** Either a row for `PLATFORM_RIGID_MODE_EXACTNESS` in
   `tests/test_counters_are_injected.py`'s `REGISTERED` with both BX0 cells green and the
   completeness assertion moved to `>= 5`, or all four sentences corrected -- 
   `floatfea/tolerances.py:354-355`, `docs/milestones/F3.md` section 5 and section 7,
   `tests/test_counters_are_injected.py:317-319` -- site by site, each with its hunk.
3. **R634.** `floatfea/tolerances.py:330` and `:345-348` say what is true: the constant is
   asserted by `check_rigid_modes` at `floatfea/model/platform.py:319`, its subject is
   every deck a reader could write, no counter is registered against it and why. No value
   moves.
4. **The closure list absorbed in one commit**, with CZ1's four outputs pasted AFTER that
   commit exists: `ruff check`, `black --check`, `mypy`, `pytest -q` at the commit, then
   `gh run list` at its own sha with the job-level conclusions.

**What does NOT hold this step, stated so no round is spent asking:** R631 and R626's
residue are LEDGERED under DZ7c and I accept the ledger; R635 is recorded and not
blocking; C88's missed timing condition is a closure item because the choice it would have
affected turned out right and I verified it against the worst member; the EG4 preview stays
BLOCKED and that is correct -- fix its stated ground, do not work around it.

**Schedule.** F3 closes **13 October**; F4 19 October; the member-force table 23 October;
the code-check screen 28 October. **I have no measurement that contradicts any of them**,
and the ladder is green on CI at this commit, which is the measurement that would. The
report proposes pulling F4 to **16 October** under EG5(b): **I do not endorse that from
here.** Not because the reasoning is wrong -- the export-not-a-derivation argument is
sound and DX1 measured it -- but because the step report names the one unknown it rests on
(whether HSP-stable carries the buoy positions where a gate can cite them by file and
line) and that unknown is unmeasured, and because section 7's other factual claim about
`../HSP-runs` was refuted by one `ls`. **Measure the EB6 expected side first, then propose
the date.** Three days is not worth buying on an unread file.

**One sentence for the implementer.** The ceiling is the best-derived constant in this
repository -- both edges solved, the counter size bisected, the unit-scaling case survived,
and it buys `850x` of detection that nobody had measured. Everything I am holding on is a
sentence about a mechanism or a guard that cannot fail, and all three are in files you can
fix in one commit without touching a number.
