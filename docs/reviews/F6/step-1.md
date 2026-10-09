# Review — F6 step 1
Reviewed commit: 517f8e201a1860142277d155b03b221458f482bb
Verdict: HOLD
**Reviewed commit: `0b9ea0d`** (`0b9ea0dd5cec0a6382c26fafae31be6f488a7d0b`, tree clean when
I judged it; my corpus batch 42 is committed on top at `517f8e2`, which is why the plain
`Reviewed commit:` stamp above is not the commit I judged -- R718's subject, and this bold
line is the mechanism.)
Tests: 3125 passed, 43 failed, 1 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `0b9ea0d`, `589.90s`. The
report states no suite count at all, so there is no figure of its to compare with.)

## Round of 2026-10-09 -- ROUND 1 OF THREE, F6 step 1. **HOLD.** Eight blocking items -- six on the code and the deliverable, two on a red suite and a red CI -- and the one that matters is a sign.

**WHY HOLD, IN FIVE SENTENCES.** I was asked to check the six clauses' coefficients
independently and I did: `10340`/`20680` with `F_y` in MPa, `0.5 A` beam shear,
`W_t = 2J/D`, `C_m` as a declared input, the `3.3.2` max-of-two, `C_c`, the `F_e'`
expression and the `3.2.2` branch boundary are **all correct**, and the branch boundary is
continuous to the fifteenth digit. **What is wrong is upstream of all of them: the column
the check reads publishes compression as positive, and `check_member` reads it as
tension.** Measured from a displacement whose sense cannot be argued with -- a member
stretched 1 mm publishes `N = -5510102.18698421` at both stations -- against
`docs/conventions.md:320`, which locks tension positive. Every `axial branch`, every `F_a`,
every `u_axial` and every `governing_clause` in `docs/F6_utilisation.csv` and
`docs/F6_utilisation.md` is wrong on every row; the four over-unity rows are Â§ 3.3.2 and not
Â§ 3.3.1; `F_a` is published as `213.00 MPa` -- the exact figure the same file's FA1 label
calls superseded -- where the clause gives `73.25`; and the **FA2 headline `0.024114` that
the report uses to invert its own advice to Xabier about `K` becomes `0.151293`** once the
sign and `C_m` are each corrected one at a time. **The governing `U = 1.815` is also not the
quantity its label names**: it is the per-component envelope bound, where the per-instant
value is `1.7115`.

**No STOP.** No low rung is red: `the verification ladder` is SUCCESS in CI at the reviewed
commit, all six rungs, and every one of my 43 local reds is in three report-guard files.
The locked plan is not wrong -- on the contrary, Â§ 3 item 2 of it is one of the things the
code does not do -- so nothing needs reopening.

**AND THE STEP IS OUT OF SCOPE AGAINST ITS OWN LOCKED PLAN, which I rule on rather than
block on.** `docs/milestones/F6.md` Â§ 3 is step 1 and it is the six clauses *plus* G6.1's
documented hand calculations *plus* a counter-case per check. Â§ 4 is step 2 and it is
`scripts/measure/`, the utilisation table and the top ten. This commit shipped Â§ 4's
deliverable and none of Â§ 3's gate, which is the two halves of the plan swapped. FA3
directed the send, so I am not treating it as a silent adaptation -- but the consequence is
exactly what CZ0 (a) was amended for: **a utilisation table a structural engineer sizes
steel against went to Xabier with no gate, no counter-case, no tolerance and nothing under
`tests/` reading either new file.** `grep -rl api_wsd tests/` is empty. Six of my eight
findings are things G6.1 would have caught, and that is the measurement on the ordering, not
an opinion about it. See Â§ *On FA3 versus G6.1* -- that one goes to Xabier.

## 0. CI AT THE REVIEWED COMMIT -- RED, AND THE LADDER IS THE HALF THAT IS GREEN

```
cmd    gh run list --commit 0b9ea0dd5cec0a6382c26fafae31be6f488a7d0b --json databaseId,conclusion,status
out    [{"conclusion":"failure","databaseId":37883813296,"status":"completed"}]
cmd    gh run view 37883813296 --json jobs -q '.jobs[] | "\(.name)\t\(.conclusion)"'
out    lint, unit and guards              failure    (11m26s)
out    the verification ladder            success    (3m34s)
out    CI determinism -- leg              skipped
out    CI determinism -- ten legs agree   skipped
cmd    gh run view 37883813296 --json jobs   (step level, the failing job)
out    1..9  checkout / setup / install / actionlint / ruff / black --check / mypy /
out          unit tests                                              all success
out    10    guards and meta-tests                                   FAILURE
judge  **CA2: A RED CI IS A HOLD REGARDLESS OF WHAT THE LOCAL RUN SAYS, and here the local
       run agrees.** This is not CK2: the jobs ran on a real runner for eleven minutes,
       there is no payment annotation and no two-second zero-step job. It is not CA2's
       unavailable state either -- the run completed at the reviewed commit's own sha.
       `guards and meta-tests` is the step that fails, which is the same family as my 43,
       and `the verification ladder` passing is why this is a HOLD and not a STOP.
```

## 1. MY OWN INSTRUCTIONS, THE CONFTEST AND THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py
cmd    git diff cdbbf79..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
judge  CH2/CI0: the one conftest in the tree is untouched in this range, so no rung's
       green is forged from its own directory and I did not have to read a hookwrapper.
cmd    git diff cdbbf79..HEAD -- floatfea/tolerances.py
out    (empty)
judge  NOT ONE VALUE, COUNTER, FORM OR COMMENT MOVED. EU1 does not fire on this diff -- and
       I ran the adversarial case anyway, at every `D/t` and `KL/r` boundary the clause
       module has, because the diff introduced two decision rules with no tolerance behind
       them at all. That is what found R742.
cmd    git diff --stat cdbbf79..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 6 ++++--
cmd    git log --oneline cdbbf79..HEAD -- docs/SUPERVISOR.md
out    767fb86 process: EZ0 -- CZ0 (a) gains "or in a published deliverable"
cmd    git show --stat 767fb86
out    CLAUDE.md | 15 ++++++++++++++-     docs/SUPERVISOR.md | 6 ++++--
judge  **CORRECT AND CLEAN.** A standalone `process:` commit citing EZ0 by name, touching
       nothing under `floatfea/`, `tests/` or `scripts/`. I read the diff line by line: it
       is purely additive, it deletes no guard, and the amended head and its definition
       are byte-identical with `CLAUDE.md`'s. `.claude/agents/gating-supervisor.md` is
       untouched -- which is itself a problem, and it is C45 below rather than a finding,
       because the file that governs what I read now disagrees with the two files that
       say it is the single home of the list.
```

## 2. THE SIX CLAUSES, CHECKED AGAINST THE STANDARD INDEPENDENTLY -- WHAT IS RIGHT

The hand-back asked for this specifically and named three of the four things it was least
sure of. I re-derived each from the clause rather than from the module, and from the US
forms and their conversion rather than from the SI numbers the module carries.

```
rule   API RP 2A-WSD section 3.2.3: the US branch limits are `1500/F_y` and `3000/F_y` with
       `F_y` in ksi; `1 ksi = 6.894757 MPa`
out    1500 x 6.894757 = 10342.1    3000 x 6.894757 = 20684.3
out    the module carries 10340 and 20680, which is the standard's own SI rounding
out    10340/355 = 29.1268    20680/355 = 58.2535    D/t shipped = 13.8889
judge  **THE CONVERSION IS RIGHT AND IT IS DONE IN ONE PLACE** (`PASCAL_PER_MPA`, read only
       at `:101`). The 145x risk the module's docstring names is real and is not realised.
rule   section 3.2.4(a): the beam shear stress for a cylinder is `V / (0.5 A)`, `F_v = 0.4 F_y`
out    `V/(0.5 A)` is `2 V/A`, so using `A` reads 2x LOW -- the direction the comment claims
judge  CORRECT, including the direction, which is the half a comment usually gets wrong.
rule   section 3.2.4(b): `f_vt = M_t D / (2 I_p)`, `F_vt = 0.4 F_y`
out    `M_t D / (2 I_p)` is `M_t / (2 J / D)`, and the script passes `2 J / D`
judge  CORRECT.
rule   section 3.3.2 requires BOTH (3.3.2-1) with the `C_m/(1 - f_a/F_e')` amplification AND
       (3.3.2-2) `f_a/(0.6 F_y) + f_b/F_b`, and permits the single in-lieu form only at
       `f_a/F_a <= 0.15`
out    the module evaluates both and takes `max`, and omits the in-lieu relaxation
judge  **CORRECT AND CONSERVATIVE IN THE RIGHT DIRECTION.** `max` of two utilisations is
       the right expression of "both must be <= 1", and dropping a permission cannot
       under-report. `F_e' = 12 pi^2 E / (23 (KL/r)^2)` is the same expression as the
       elastic `F_a`, which is why the report's two `73.25` lines agree -- that is the
       standard, not a copy-paste.
rule   section 3.2.2: inelastic below `C_c`, elastic at and above, `C_c = sqrt(2 pi^2 E/F_y)`
out    C_c                                   = 108.05885001274791
out    inelastic form as the ratio -> 1      = 92608695.65217389 Pa
out    elastic form at KL/r = C_c            = 92608695.65217392 Pa
out    KL/r = C_c - 1e-12                    -> inelastic;  = C_c -> elastic
judge  **CONTINUOUS TO THE FIFTEENTH DIGIT AND THE `>=` IS ON THE CORRECT SIDE.** `12/46`
       is identically the inelastic limit, so the whole safety-factor polynomial
       `5/3 + 3x/8 - x^3/8` is transcribed right. This was the coefficient the hand-back
       was least sure of and it is correct.
```

**So four of the five things I was asked to attack in Â§ 1 of the hand-back hold.** The
fifth, `C_m = 0.85`, does not, and it does not for a reason the module states backwards --
R743.

## Findings

**R739. (BLOCKING. (a) AS AMENDED BY EZ0, AND ALSO (a) ON THE UNAMENDED HEAD, BECAUSE THE
DEFECT IS IN `floatfea/`.) THE PUBLISHED `N` COLUMN IS COMPRESSION-POSITIVE AND
`check_member` READS IT AS TENSION-POSITIVE. 128 OF 256 ROWS ARE CLASSIFIED IN THE WRONG
SENSE, AND SO IS EVERY ROW OF BOTH PUBLISHED TABLES.**
`floatfea/checks/api_wsd.py:254` (`in_tension = axial_n >= 0.0`),
`scripts/measure/api_wsd_utilisation.py:138` (`axial_n=float(r["N"])`), against
`docs/conventions.md:320`. Published in `docs/F6_utilisation.csv` (`axial_branch`,
`F_a_MPa`, `u_axial`, `governing_clause`) and `docs/F6_utilisation.md`.

```
claim  a positive `N` in docs/F4_member_forces.csv is a tension force
cmd    move node_b of platform:hub1_arm OUTWARD along the member axis by 1 mm -- an
       unambiguous stretch -- and read what member_forces publishes at each station
rule   docs/conventions.md:320, locked at F0: "Positive axial force: tension positive."
out    end_a = [-5510102.187, 0, 0, 0, 0, 0]      end_b = [+5510102.187, 0, 0, 0, 0, 0]
out    EA/L x 1e-3 (the true internal N, tension positive) = +5510102.18698421
out    published ROOT N  =  end_a[0] = -5510102.18698421
out    published TIP  N  = -end_b[0] = -5510102.18698421
judge  **BOTH STATIONS PUBLISH COMPRESSION-POSITIVE.** `k_local @ (t @ u)` is the force the
       NODES exert on the ELEMENT, not the force the element exerts on the nodes, and the
       module's own equilibrium note confirms the sense: `Vz_A + Vz_B` equals the member's
       weight `+1532812.5 N`, which only holds for forces applied TO the element.
```

**THE REACH, each cell with one variable moved and everything else held -- same CSV, same
filter, same section, same `C_m`:**

```
rule   the shipped decision rule, `in_tension = axial_n >= 0.0`, against the same rule
       reading `-axial_n`
out    branch assignment    : 128 rows published `tension` are in COMPRESSION, and all 128
out                           published `elastic`/`inelastic` are in TENSION
out    branch HISTOGRAM     : elastic 32; inelastic 96; tension 128 -- IDENTICAL EITHER WAY
out    governing clause     : all four over-unity rows go 3.3.1 -> 3.3.2; all ten published
out                           top-ten rows read `3.3.1 interaction`
out    F_a on the 4 platform ROOTs : published 213.00 MPa, clause gives 73.25 MPa (elastic
out                           at KL/r = 121.5) -- u_axial low by 2.9079x
out    F_a on the hub ROOTs : published 213.00 MPa, clause gives 161.02 MPa (inelastic at
out                           60.8) -- u_axial low by 1.3228x
out    u_axial, worst station : 0.000358 published, 0.001043 corrected
out    u_axial, platform:hub1_arm ROOT : 0.033966 published, 0.098847 corrected
out    largest |U(K=2)-U(K=1)| : 0.024114 published, 0.034926 corrected
out    worst compression station : U = 1.70984 published, 1.81496 corrected -- the worst
out                           station in the whole table IS a compression station
judge  **THE HISTOGRAM BEING IDENTICAL IS WHY NOTHING LOOKED WRONG.** The split is 128/128
       because every station contributes one `total_max` row and one `total_min` row of
       opposite axial sign, so the one summary number a reader would sanity-check is
       invariant under the inversion. The report publishes that number as the FA2 answer.
```

**AND IT PUTS `213.00 MPa` BACK INTO A DELIVERABLE THAT SPENDS A LABEL SAYING IT IS
SUPERSEDED.** `docs/F6_utilisation.md:35`'s FA2 table publishes `F_a = 213.00` on all ten
rows; the same file's FA1 inheritance says the `213.0 MPa` generic `0.6 F_y` reference "is
SUPERSEDED by F6's API RP 2A-WSD clauses and it is NOT the API bending allowable". Both
sentences are in one published file and they contradict each other, and the reason is this
sign: with the sign corrected, no governing row's `F_a` is `0.6 F_y` at all.

**Closed when** the sign convention is stated once and read once: `docs/conventions.md:320`
is the authority, so either `member_forces` returns the internal action (and the five other
components are re-derived with it, not just negated) or the consumer negates at the one
boundary where it reads the CSV, with the convention named in `check_member`'s docstring and
in `MemberCheck.in_tension`; **plus** the two attribution sentences at
`floatfea/post/member_forces.py:23` and `scripts/measure/member_forces_table.py:415`
corrected, **plus** `docs/F6_utilisation.csv` and `docs/F6_utilisation.md` regenerated in
the same commit (BP0), **plus** the 1 mm prescribed-stretch cell above pasted as the
control -- it costs four lines, needs no npz, and is the one route that cannot share an
assumption with either file. My figures to beat are in the two blocks above.

**R740. (BLOCKING. (a) UNDER EZ0.) `U = 1.815` IS THE PER-COMPONENT ENVELOPE BOUND, THE
DELIVERABLE'S LABEL SAYS IT IS THE PER-INSTANT VALUE, AND IT IS NOT EXACTLY EITHER.**
`scripts/measure/api_wsd_utilisation.py:79-81` (the label), `:126` (the `total*` filter) and
`:209` (the max over rows), published at `docs/F6_utilisation.md:13` and in every row of
`docs/F6_utilisation.csv`.

```
claim  "The utilisations are computed from F4's PER-INSTANT stresses where available; the
       per-component envelope is an upper bound and is reported separately in F4's table."
cmd    the basis values F4's CSV actually carries, and which of them the filter keeps
out    dynamic_max 288   dynamic_min 288   static 48   total_max 288   total_min 288
out    the filter keeps `basis.startswith("total")`, i.e. total_max and total_min ONLY
out    F4's per-instant figure is computed in memory and published in docs/F4_member_forces.md
out      alone; THE CSV CARRIES NO PER-INSTANT ROW, so "where available" is nowhere
rule   docs/milestones/F6.md section 4: "Both of F4's stress columns carry through -- per-instant and
       envelope upper bound -- and the utilisation is computed from each, labelled.
       Collapsing them would be the one thing this milestone could do that makes F4's
       table less honest than it is."
out    platform:hub2_arm ROOT, T = 12.5 s:  per-instant 455.7 MPa   envelope 483.2 MPa
out    U from the envelope   = 1.81496   <- what is published
out    U from the per-instant = 455.7/266.25 = 1.7115
out    the gap, 0.103 in U, is 4.3x the K sensitivity the report leads with
judge  **AND IT IS NOT THE PER-COMPONENT BOUND EITHER.** The bending resultant is formed
       INSIDE each `total` row before the max over rows is taken, so a station whose `My`
       peaks on `total_max` and whose `Mz` peaks on `total_min` is published BELOW the true
       per-component bound. The published number is a third quantity -- the worse of two
       per-component rows -- and it has no stated provenance that is true.
```

**Closed when** the label states which quantity the column is, measured rather than
asserted, and the two columns Â§ 4 requires exist -- or, if the per-instant column genuinely
cannot be formed without re-running F4's driver, the label says exactly that and the one
number above (`1.81496` against `1.7115` at the governing station) is published beside it so
a reader knows the size of what is missing. The deliverable's own labels are the half of it
Xabier reads first.

**R741. (BLOCKING. (a), AND THE LOCKED PLAN REQUIRES IT IN ITS OWN WORDS.) Â§ 3.2.2's
LOCAL-BUCKLING CHECK IS NOT IMPLEMENTED AND A SLENDER SECTION IS NOT REFUSED -- IT PASSES
SILENTLY, WHICH IS THE EXACT PHRASE THE PLAN FORBIDS.**
`floatfea/checks/api_wsd.py:132-153` (`allowable_axial_compression`), against
`docs/milestones/F6.md` Â§ 3 item 2.

```
rule   docs/milestones/F6.md section 3 item 2, LOCKED: "D/t is checked against the
       local-buckling limit first, because beyond it the global check is not the binding
       one ... so local buckling does not govern *this* section and the check must still
       refuse rather than pass silently on one that is slender."
cmd    inspect.signature(allowable_axial_compression)
out    (k_l_over_r: float, fy: float = 355000000.0, e: float = 210000000000.0)
judge  it takes no `D` and no `t`, so it cannot check `D/t` at all.
cmd    allowable_axial_compression(80.0) with the section at D/t = 100
out    (136098611.12499207, 'inelastic')   -- no refusal, no reduction, no flag
rule   API RP 2A-WSD section 3.2.2(b): `F_xc = F_y` only for `D/t <= 60`; above it the local
       buckling stress replaces `F_y` in the column formula
cmd    grep -n "60|Fxc|local buckling" floatfea/checks/api_wsd.py
out    one comment line, at :97, and it is about `D/t = 300` in the BENDING clause
judge  **THE ONLY REFUSAL IN THE MODULE IS `allowable_bending`'s at `D/t > 300`, which is a
       different clause and a different limit.** A caller asking for the axial allowable
       alone -- which is the public API, it is in `__all__` -- gets a number computed on the
       full `F_y` at any slenderness. It is vacuous at the shipped `D/t = 13.8889`, which is
       precisely EU1's shape: the configuration the commit chose cannot see it.
```

**Closed when** `allowable_axial_compression` either implements Â§ 3.2.2(b) or refuses above
its limit, and the limit it uses is the clause's (`D/t = 60`) rather than the bending
clause's `300` -- with the refusal exercised, because a refusal nothing reaches is not a
refusal. `basis.chs_class_limits()` is named in the plan row and already exists.

**R742. (BLOCKING. (a).) `allowable_bending` RETURNS MORE THAN `0.75 F_y`, WHICH NO READING
OF Â§ 3.2.3 PERMITS, FOR `D/t` IN `(29.1268, 30.5974)`. THE CAUSE IS THAT `10340` ENCODES
`E = 200 GPa` AND THE MODULE COMPUTES WITH `E_STEEL = 210e9`.**
`floatfea/checks/api_wsd.py:102-103` (the limits) against `:174` (the first reduced branch),
and `floatfea/basis.py:46`.

```
claim  section 3.2.3's branches are monotone and capped at 0.75 F_y
cmd    allowable_bending at and just above the first branch limit
out    F_b at D/t = 29.1268            = 267.7855873914286 MPa
out    0.75 F_y                        = 266.25 MPa
out    ratio                           = 1.0057674643809524   (+1.5356 MPa)
out    the reduced_1 branch crosses 0.75 F_y at D/t = 30.59737736765419
cmd    the D/t at which [0.84 - 1.74 F_y D/(E t)] F_y equals 0.75 F_y
out    0.051724 x E / F_y = 30.597295774647886  -- the crossing, to five figures
out    0.051724 x 29000 ksi = 1500.0  -- which is the US form of the same limit
cmd    the second boundary, D/t = 58.2535
out    reduced_1 gives 237.37 MPa and reduced_2 gives 235.32 MPa -- a step DOWN of 0.87%
judge  **ONE CAUSE, TWO DISCONTINUITIES IN OPPOSITE DIRECTIONS, WHICH IS WHAT RULES OUT A
       TRANSCRIPTION SLIP IN ONE COEFFICIENT.** `1500/F_y[ksi]` is exactly the continuity
       point at `E = 29000 ksi = 199948 MPa`, and `10340/F_y[MPa]` is its conversion. The
       module runs at `210000 MPa`, 5.0% higher, so the branch limit sits 5.0% below the
       continuity point and the reduced branch pokes above the cap on the interval between
       them. Vacuous at `D/t = 13.8889` and not vacuous as a clause: the module is in
       `__all__` and is the one the next section will be checked with.
```

**Closed when** the module either (i) states the modulus the clause's own limits were derived
at, keeps `10340`/`20680`, and caps the reduced branch at `0.75 F_y` so the function cannot
return above the clause's own ceiling, or (ii) derives both limits from `E` so the branches
are continuous by construction -- with the chosen reading stated and the
`1.0057674643809524` above reproduced or refuted. **Not** by changing `E_STEEL`: that is a
locked material constant and this is a clause-transcription question.

**R743. (BLOCKING. (a).) `CM_NO_TRANSVERSE_LOAD = 0.85` IS DECLARED UNDER THE WRONG CLAUSE
CATEGORY AND ITS CONSERVATISM IS STATED BACKWARDS. MEASURED, IT IS A LARGER LEVER ON THE
GOVERNING NUMBER THAN `K` IS, AND THE REPORT'S HEADLINE SAYS `K` WAS THE LARGEST.**
`floatfea/checks/api_wsd.py:71-77`, published at `docs/F6_utilisation.md` in "The section and
the slenderness" as `C_m = 0.85` (Â§ 3.3.2, no transverse load -- a declared input).

```
claim  "0.85 is the conservative reading of a clause whose alternatives need an end-moment
       ratio the screen does not resolve"
rule   section 3.3.2's amplified form is f_a/F_a + C_m f_b / [(1 - f_a/F_e') F_b], so C_m
       MULTIPLIES the bending term: a smaller C_m gives a SMALLER utilisation
cmd    four cells, one variable each, same CSV, same filter, same section
out    shipped (C_m = 0.85, sign as shipped) : worst U 1.81496   largest |dU over K| 0.024114
out    sign fixed alone                      : worst U 1.81496   largest |dU over K| 0.034926
out    C_m = 1.0 alone                       : worst U 1.81496   largest |dU over K| 0.128855
out    both                                  : worst U 1.81754   largest |dU over K| 0.151293
out    platform:hub1_arm ROOT, both corrected: 1.18820 -> 1.37969
out    platform:hub3_arm ROOT, both corrected: 1.20215 -> 1.37951
judge  **"CONSERVATIVE" IS THE WRONG DIRECTION, MEASURED: C_m = 1.0 RAISES EVERY
       COMPRESSION UTILISATION.** And the category is wrong twice over. API's
       no-transverse-loading case is C_m = 0.6 - 0.4 M_1/M_2, not 0.85; 0.85 is the
       sidesway case, which is the reading K = 2.0 itself rests on ("no reliable lateral
       restraint"), and the docstring's own next sentence says these arms DO carry a
       distributed body force. So the constant is plausibly the right NUMBER under a
       category its name, its docstring and the deliverable's label all deny.
```

**This is the one place I disagree with the report's headline rather than with a number in
it.** The hand-back asked me to attack the claim that `K` is not the largest modelling
choice. It is not -- but on the report's own metric `C_m` moves the governing number
`5.3x` further than `K` does, and with both corrected the amplified form of Â§ 3.3.2 begins
to govern, which puts `K` back inside the number through `F_e'`. The conclusion "the axial
term contributes almost nothing" **survives** -- `u_axial = 0.001043` against
`u_bending = 1.81460` at the governing station -- and that half of the advice to Xabier is
sound. What does not survive is `0.024114` as the measure of how much the modelling choices
move the answer.

**Closed when** the constant is named for the category it is, the docstring states the
direction as measured (`C_m = 1.0` raises `U`, here from `1.18820` to `1.37969` at
`platform:hub1_arm` ROOT with the sign also corrected) rather than asserting conservatism,
the published label stops saying "no transverse load" in a deliverable whose own load basis
is a distributed body force, and the choice between API's sidesway category and its
transverse-loading-with-unrestrained-ends category is stated with its reason -- or `1.0` is
adopted. I am not ruling which; I am ruling that the three current statements of it cannot
all be true.

**R744. (BLOCKING. (c) -- ASSERTION DOMAIN BLINDNESS, AND IT IS THE CONTROL THAT ANSWERED
VERDICT 109's BLOCKING FINDING.) THE SAG-SIGN GUARD READS THE INTERMEDIATE AND NOT THE LINE
THAT SETS THE PUBLISHED VALUE. R734's EXACT DEFECT RETURNS ON A ONE-CHARACTER CHANGE WITH
THE GUARD SILENT.**
`scripts/measure/member_forces_table.py:446-449` (the two assignments) against `:452-462`
(the guard), published in `docs/F4_member_forces.csv`'s MID rows.

```
claim  "the check is a sign comparison and needs no constant. It catches exactly the defect
       that shipped, and it cannot be satisfied by a configuration that happens to sit at
       zero because it skips those."
cmd    three copies of the module, one variable moved in each, `_station_values` called on
       platform:hub1_arm with a uniform a_y = 3 m/s^2 so that w_local[1] is nonzero
rule   the guard at :452-462 compares copysign(sag_z) against copysign(want * load)
out    base                                  OK        mid Mz = +2.92968750e+06
out    `sag_z = +w_local[1]...` -> `-w_local[1]...`    REFUSED (the guard fires)
out    `mid[5] = mid[5] + sag_z` -> `- sag_z`          OK, SILENT, mid Mz = -1.46484375e+07
out    the fixture is not degenerate: w_local[1] = 28125.0, so the `load == 0: continue`
out      branch is not taken
judge  **THE GUARD RESTATES THE LINE ABOVE IT.** `sag_z` is assigned `+w_local[1] * span^2
       / 8` and the guard then asserts that `sag_z` has the sign of `+w_local[1]`, with
       `span^2/8 > 0` always -- so for the quantity that is PUBLISHED, `mid[5]`, the guard
       has no reach at all. The defect that shipped as R734 was a wrong sign on the
       published MID `Mz`; the repair split that one line into two, and the half the guard
       reads is not the half that publishes. One character, factor of 5 and a sign change,
       suite green.
```

**I am blocking on a guard, which CZ0 classes as a closure item, and I am naming that rather
than smuggling it.** My instructions' carve-out is for a closure item that touches (c), and
this is that: it is the ONLY check in the tree on the sign of a published column -- `grep
-rl member_forces_table tests/` is still empty -- so what it claims, on which quantity, is a
gate assertion in substance even though it is a runtime refusal in form. It is also the
third round running on the same two lines, and the reason it recurs is not carelessness: it
is that the repair's own control was written to the shape of the previous defect rather than
to the published quantity.

**Closed when** the comparison is on `mid[5]` -- the delta the station actually publishes,
against the sign of its own load component -- so that a flip in either half reddens, with
the mutation above re-run and both outcomes pasted. One expression, no new file, no
threshold, and no new apparatus.

**R745. (BLOCKING. (d).) 43 RED TESTS AT THE REVIEWED COMMIT AND A RED CI JOB, AND THE
EG3(i) TRACE IS NOT PASTED BECAUSE THE REPORT CARRIES NO TEST COUNT AT ALL. AT LEAST 16 OF
THE REDS ARE OUTSIDE BOTH OF EG3's LISTS AND ARE THE REPORT'S OWN MISSING SECTIONS.**
`docs/reports/F6/step-1.md` (the whole file), `docs/reports/F6/step-1-answers.json` (absent).

```
cmd    python -m pytest -q -p no:randomly   (my own run, tree clean at 0b9ea0d)
out    43 failed, 3125 passed, 1 skipped in 589.90s
out    by file: tests/test_report_carried.py 19; tests/test_report_guard_states.py 19;
out            tests/test_report_numbers_are_sourced.py 5
out    NOTHING under tests/verification, tests/unit or tests/regression is red
cmd    EG3(i)'s trace -- each FAILED id matched to state (1)'s own list
out    on the list    : test_the_guard_reads_the_step_being_worked_on
out    the cascade    : test_report_guard_states.py[baseline] is red and its own failure
out                     line pastes the test_report_carried.py reds, so the other 18 states
out                     cascade off it
out    OUTSIDE BOTH LISTS, each one an omission of the report itself:
out      test_the_report_names_the_verdict_it_answers   -- no `Answers: verdict <n> @ <sha>`
out      test_the_report_carries_a_WHOLE_SUITE_count    -- no suite count anywhere
out      test_the_report_carries_a_CI_SECTION           -- no CI section
out      test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW -- no 0a table
out      test_the_ROUNDS_SECTION_is_the_GENERATORS...   -- no 0a table
out      test_the_reported_CI_counts_are_not_all_zero   -- no CI rows
out      test_the_Carried_table_is_what_the_generator_produces  -- step-1-answers.json
out      test_the_generator_would_catch_a_row_under_the_wrong_number  -- same file absent
out      test_there_are_pointers_to_resolve             -- no Carried row names a section
out      test_a_report_does_not_say_CLOSED              -- no Carried table to parse
out      test_every_number_in_prose_is_sourced... x 5   -- sections 1, 2, 5, 6, 7
judge  **EG3's WAIVER IS CONDITIONAL ON THE TRACE AND THE TRACE IS NOT PASTED.** The report
       states no test count, so there is no claim for me to check and no "only those"
       sentence to hold it to. CZ1 (iv) is therefore unchanged for every red above.
```

**I MEASURED WHICH OF THEM MY OWN VERDICT CLEARS, because that is the half no verdict can
take after the fact.** In a detached worktree at `0b9ea0d` with a placeholder verdict
committed at `docs/reviews/F6/step-1.md`, the three files go from **43 red to 31 red**: 12
clear at the verdict commit, and the 31 that remain are the report's own omissions plus the
cascade plus state (2)'s named five. So writing this verdict does not fix it, and the
answering revision must.

**AND ONE PART OF THIS IS NOT THE REPORT'S FAULT AND GOES TO XABIER.** `VERDICT` resolves to
`docs/reviews/F6/step-{max(REVIEWED)}.md` and falls back to `step-0.md` when `REVIEWED` is
empty (`tests/test_report_carried.py:211`). At the **first step of a new milestone** that
directory is empty, so a dozen assertions are keyed on a file that cannot exist yet. This is
EG3's boundary one level up -- a MILESTONE boundary rather than a step boundary -- and
EG3's two lists do not name it. I am not asking for new apparatus; the fix is a third state
in EG3's list, which is prose in `CLAUDE.md`. Until it exists, the honest reading is the one
EG3 already gives: record the red with its cause named, and name it in the report.

**Closed when** the report carries, generated rather than written: an
`Answers: verdict 110 @ <this verdict's sha>` header, `docs/reports/F6/step-1-answers.json`
committed, the `## 0`/`## 0a` CI sections from `scripts/ci_section.py`, the whole-suite line
from `scripts/suite_count.py` run AFTER every other edit (CP3), and the five unsourced
sections' numbers inside a command block or table of their own section -- with the resulting
`FAILED` list pasted and every id in it matched by name to EG3's state (2).

**R746. (BLOCKING. (d), AND IT IS THE FIRST THING MY INSTRUCTIONS TELL ME TO CHECK.) THE
REPORT'S `Carried` SECTION ANSWERS VERDICT 108's LIST, NOT VERDICT 109's. R731 IS NAMED AS
BLOCKING WHEN IT WAS CLOSED, AND R734, R735, R736, R737 AND R738 ARE NOT NAMED AT ALL.**
`docs/reports/F6/step-1.md:5` (`Answers: FA3 opens the step`) and `:134-135`.

```
claim  "R730, R731 and R732 carry from F4's ledger, R730 and R731 blocking."
cmd    the newest verdict's own Carried and `Carried for F5's ledger` sections
rule   my instruction 1b: the `Answers: verdict <n> @ <sha>` header names the LATEST
       verdict, and a report answering a superseded round has every `Carried` claim about
       the wrong list
out    verdict 109 (`cdbbf79`, judging `3305473`): R731 CLOSED as to every condition;
out      R732 CLOSED and its warrant stronger than written; R730 NOT CLOSED and renamed
out      R734; R735, R736, R737, R738 raised
out    verdict 109's "the names that stay blocking": R730/R734, and R737
out    the report names: R730 blocking, R731 blocking, R732 carrying
judge  **TWO OF THE THREE DISPOSITIONS ARE WRONG AND THE TWO NEW NAMES ARE ABSENT.** This
       is exactly the failure 1b exists to prevent, and it is not academic: R737 is a
       blocking carry that nothing in this step mentions, and R734's fourth condition --
       the corrected CSV going to Xabier with a sentence saying which column moved -- is
       unevidenced anywhere.
```

**The substance is better than the list.** R734's repair at `029cce5` is correct and I
verified it myself, below. The finding is the ledger, not the work -- and the ledger is what
the whole arrangement exists to re-read.

**Closed when** the header reads `Answers: verdict 110 @ <sha>` and the `Carried` section is
the generator's table over verdict 109's and this verdict's items, with R731 and R732 marked
closed by verdict 109 rather than carried, and R737 named.

## Closure items

Named with their site and what would close each. The implementer fixes the whole list once,
in the step's closure commit; they are not re-reviewed item by item and the step is not held
on one. F4's numbering ended at C40, so this list starts at C41.

* **C41.** `scripts/measure/api_wsd_utilisation.py:264`. The published `branch at K=2`
  column is computed as `kl2 >= 108.059` -- a literal -- while the utilisation on the same
  row used `column_slenderness_parameter() = 108.05885001274791`, and `locked.axial_branch`
  was available per row. Two rules for one decision inside one file, disagreeing on
  `KL/r` in `[108.05885, 108.059)`. **Closed when** the column reads the branch the check
  returned, or the literal is deleted in favour of the function.
* **C42.** `scripts/measure/api_wsd_utilisation.py:84-91`. `_section()` reads
  `built.bodies[0].members[0]` and the result is applied to all sixteen members, while
  `_kl_over_r()` four lines later reads each member's own body. Measured: all sixteen share
  `A = 1.31192909`, `I_y = 0.88797921`, `J = 1.77595841`, `D = 2.5`, so it is vacuous today.
  **Closed when** one `assert` states the equality the first function assumes, or `_section`
  takes the body.
* **C43.** `floatfea/checks/api_wsd.py:101`. `section_class(2.5, 0.18, fy=355.0)` returns
  `compact` with `limit_1 = 29126760.56` and `allowable_bending` returns `266.25 Pa`. The
  module's own docstring names this exact failure as the reason the SI forms matter, and
  nothing refuses it. **Closed when** an `F_y` that is not plausibly in pascals raises, or
  the docstring stops claiming the risk is handled.
* **C44.** `scripts/measure/api_wsd_utilisation.py:314-316`. "**{len(over)} of
  {len(all_stations)} member-stations exceed U = 1.0** ... All four are platform arm ROOTs"
  -- a computed count beside a hand-written "four". **Closed when** the sentence is
  generated from the same set, or the count is removed from the prose.
* **C45.** `.claude/agents/gating-supervisor.md:219` still reads `(a) a defect in
  `floatfea/`;` while `CLAUDE.md:152` and `docs/SUPERVISOR.md:27` carry EZ0's amendment --
  and `docs/SUPERVISOR.md:24-26` says the list "lives there, once". So the file that
  governs what the reviewer reads disagrees with the two files that point at it, and the
  reviewer reads the unamended head. **Closed when** a standalone `process:` commit citing
  EZ0 brings the agent file into line. Process class, not step work.
* **C46.** `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]`
  is red on its own fixture: "`frames.txt` now counts as a site: True, expected False". A
  guard failing false. **Closed when** it is fixed or deleted (CZ0), never accommodated.
* **C47.** `scripts/measure/member_forces_table.py:65` still reads "the midspan moment is
  the chord mean plus `w L^2 / 8`", one sign for two planes, against `:448` (`-w_z`) and
  `:449` (`+w_y`). That is R735 unchanged and still open. **Closed when** both sentences
  carry the two signs separately or point at the derivation.
* **C48.** `docs/milestones/F6.md` Â§ 3 item 3 names the branch limit as `1500/F_y`, the ksi
  form, where the code correctly uses `10340/F_y` with `F_y` in MPa. **Closed when** the
  plan row names the SI form the code implements.
* **C49.** `floatfea/checks/api_wsd.py:220-246`. `check_member`'s docstring says the
  arguments are keyword-only and why, and says nothing about the sign convention of
  `axial_n` -- which is the one argument whose sign changes a decision. R739's repair
  should land here too. **Closed when** the docstring and `MemberCheck.in_tension` name
  `docs/conventions.md:320`.
* **R735, R736, R738, C34 to C40, and the `0.2240`/`0.2239` item** -- all still open from
  verdict 109, carried in `docs/closure/F4.md:147` as a list, and not re-adjudicated here.
* **R712 to R717, C2 to C15, C24 to C33** -- still open, carried in the F4 closure
  artifact, not re-reviewed item by item, per CZ0.

## Tolerances touched

```
cmd    git diff cdbbf79..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff cdbbf79..HEAD -- floatfea/ | grep -E "^\+[A-Z_]+: Final"
out    +PASCAL_PER_MPA: Final[float] = 1.0e6
out    +ALLOWABLE_TENSION_FACTOR: Final[float] = 0.6
out    +ALLOWABLE_SHEAR_FACTOR: Final[float] = 0.4
out    +BEAM_SHEAR_AREA_FACTOR: Final[float] = 0.5
out    +CM_NO_TRANSVERSE_LOAD: Final[float] = 0.85
judge  **NO TOLERANCE VALUE OR COUNTER MOVED ANYWHERE IN THE TREE, AND NOTHING WAS
       WIDENED.** EU1 does not fire on this diff; I ran its adversarial case anyway,
       because the diff introduced two DECISION RULES with no tolerance behind either --
       Â§ 3.2.2's branch and Â§ 3.2.3's three branches -- and a branch boundary is a
       threshold whether or not it is called one. Running the clauses at the boundaries the
       commit did not choose is what found R742 and R741.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `PASCAL_PER_MPA` | -- | `1.0e6` | a unit conversion, not a tolerance | none, correctly | `floatfea/checks/api_wsd.py:55-56` | **ADMISSIBLE and correctly NOT in `tolerances.py`.** It is a unit, read in exactly one place (`:101`), and I verified the branch limits it feeds against the ksi forms and their conversion: `1500 x 6.894757 = 10342.1`, `3000 x 6.894757 = 20684.3`. |
| `ALLOWABLE_TENSION_FACTOR` `0.6`, `ALLOWABLE_SHEAR_FACTOR` `0.4` | -- | as shown | clause coefficients | none, correctly | `:58-62` | **ADMISSIBLE.** Â§ 3.2.1 and Â§ 3.2.4 give exactly these. They are the clause, not a threshold anything is compared against, and the module's docstring says so -- which is the right reading of `CLAUDE.md`'s rule. |
| `BEAM_SHEAR_AREA_FACTOR` `0.5` | -- | `0.5` | the clause's own idealisation | none, correctly | `:64-69` | **ADMISSIBLE, and the direction in the comment is right** -- `V/(0.5 A)` is `2 V/A`, so using `A` reads 2x low, which is what it claims. |
| `CM_NO_TRANSVERSE_LOAD` `0.85` | -- | `0.85` | a declared modelling input that MULTIPLIES a published utilisation | none, and it needs one | `:71-77` and `docs/F6_utilisation.md` | **BLOCKED, R743.** Not because `0.85` is necessarily the wrong number -- it may be right under API's sidesway category -- but because the name, the docstring and the published label all attribute it to the no-transverse-load category, which is a different formula, and the stated direction is backwards: measured, `C_m = 1.0` moves the governing metric from `0.024114` to `0.128855`. A value that scales a published utilisation and has no counter is a tolerance in all but name. |
| the two Â§ 3.2.3 branch limits `10340`/`20680` | -- | as shown | dimensionless, `F_y` in MPa | none, and R742 is what a counter would have found | `:102-103`, `:86-88` | **BLOCKED, R742.** The numbers are the standard's. They are inconsistent with `E_STEEL = 210e9` by construction, and the consequence is an allowable above the clause's own cap on an interval of `D/t`. |
| the Â§ 3.2.2 branch at `C_c` | -- | `>=` | dimensionless | none needed -- the branches are continuous there | `:149` | **CLEAN, and I solved the boundary in both directions.** `C_c - 1e-12` takes the inelastic branch, `C_c` takes the elastic, and the two forms agree to `92608695.65217389` against `92608695.65217392`. Nothing to declare. |
| everything else in the F4 block | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 109 (`cdbbf79`, judging `3305473`, an EQ0 review of the F4 closure commit counting
against no step's rounds) was a **HOLD** carrying two names and a closure list. Every one,
with status. **The report's own `Carried` section is about verdict 108's list instead, which
is R746.**

* **R730 / R734 (blocking, carried into F6's ledger) -- CLOSED, and I measured all four
  parts of my own condition rather than three.** Answered at `029cce5`.
  **(1)** `scripts/measure/member_forces_table.py:449` now reads
  `mid[5] = mid[5] + sag_z` with `sag_z = +w_local[1] * span * span / 8.0`, and the
  calibration sentence is replaced by the derivation -- `e_x x F = (0, -F_z, +F_y)` giving
  `M_z'' = -w_y` and `M_y'' = +w_z` -- which is the route I asked for and not a
  recalibration. **(2)** BP0's regeneration is in the same commit:
  `docs/F4_member_forces.csv` (768 lines changed) and `docs/F4_member_forces.md`, and **the
  two top-ten figures I predicted independently reproduce exactly** -- `384.6 / 396.7` and
  `384.6 / 396.1` are what the regenerated table carries. **(3)** The control runs where
  `w_local[1]` is nonzero. **(4)** The sentence saying which column moved and by how much is
  in the commit message. **Does not carry as written. Its residue is R744** -- the control
  from part (3) is on the wrong half of the expression, which I measured rather than read.
* **R737 (blocking, carried into F6's ledger) -- STILL OPEN, AND NOTHING IN THIS STEP
  MENTIONS IT.** `grep -rn HSP_COMMIT tests/` returns my own corpus entry and
  `tests/verification/rung3/test_platform_deck_export.py:166`, which asserts the pin file
  names the commit -- not that the recorded provenance is compared against it, which is what
  the finding was. My condition offered two branches and either is one line: F6 decides
  whether `HSP_COMMIT` goes into the provenance at the next export, or records that the tag
  alone is the warrant and a moved tag is out of scope. **Carries, still blocking.**
* **R731, R732 -- remain closed by verdict 109** and are not re-raised. The report lists
  R731 as blocking; it is not. R746.
* **R735, R736, R738 and the `0.2240`/`0.2239` item (closure) -- STILL OPEN**, correctly, and
  carried as a list rather than landed. I verified only that R735 has not regressed further:
  `:65` still gives one sign for two planes. C47 above.
* **C34 to C40, R712 to R717, C2 to C15, C24 to C33 (closure) -- STILL OPEN**, carried in
  `docs/closure/F4.md:147` and not re-adjudicated.
* **The MID exclusion -- RULED, and the report's reason is the wrong one.** `docs/milestones/F6.md`
  Â§ 0 requires the step-1 report to state R730's discharge. R730/R734 **is** discharged (above),
  so the live reason to exclude MID is **R736's unmeasured-direction bending approximation**,
  not R730. Excluding MID is the right call and I am not reopening it; the report should say
  it rests on R736 and on the absence of a refined-mesh comparison, which is true, rather
  than on R730, which is not.
* **The schedule.** The report states the 22 October working target and the 28 October
  committed date and says the working target holds. I am recording rather than escalating:
  R739 is a sign and a regeneration, R741 to R743 are each a few lines, and G6.1 is the
  step's actual locked content and is unstarted. **If revision 2 closes still carrying any
  of R739 to R746, that is the second consecutive step boundary carrying blocking items in
  this milestone's first step, and the choice -- slip the date or reduce scope -- has to be
  stated rather than restated.**

## Try to break it -- what I ran and what it said

Six adversarial configurations, none of them chosen by the diff. Four found something.

```
1  A MEMBER IN PURE TENSION, sense prescribed rather than inferred -- node B moved 1 mm
   outward along the member axis. Published N = -5510102.18698421 at both stations.
   -> R739. This is the one that outranks everything in the report.
2  THE SAME TABLE WITH THE AXIAL SIGN INVERTED, one variable moved: branch histogram
   IDENTICAL (128/128), governing clause flips on every row, F_a wrong by 2.9079x on the
   four governing stations, FA2 headline 0.024114 -> 0.034926.  -> R739's reach.
3  A SLENDER TUBE, D/t = 100 -- admissible input, past API 3.2.2.b's limit of 60.
   allowable_axial_compression returns 136098611.12 Pa, branch inelastic, no refusal.
   -> R741, and the locked plan requires the refusal in its own words.
4  THE BRANCH BOUNDARIES THEMSELVES, solved rather than sampled. D/t = 29.1268 gives
   F_b = 267.79 MPa against a 0.75 F_y cap of 266.25, and the reduced branch stays above
   the cap to D/t = 30.5974.  -> R742.
5  C_m AT API's OTHER CATEGORY, 1.0 -- one variable moved. The governing metric goes
   0.024114 -> 0.128855, and with the sign also corrected two stations go 1.188 -> 1.380
   and 1.202 -> 1.380.  -> R743, and it inverts the report's own ranking of its levers.
6  THE SAG GUARD, MUTATED ON EACH HALF OF ITS EXPRESSION SEPARATELY, on a fixture where
   w_y = 28125.0 rather than zero. The intermediate reddens; the published line does not,
   and MID Mz goes +2.93e+06 -> -1.46e+07.  -> R744.
```

**And two things I tried that did NOT break, recorded because an absence of a finding is
also a measurement.** `MemberCheck.utilisation` cannot under-report the interaction --
`u_combined >= u_bending` holds identically in both clauses, because Â§ 3.3.2's simple form
is `f_a/(0.6 F_y) + u_bending` and `f_a >= 0`. And the empty-parameter-set shape is handled:
if the `GOVERNING_PERIODS` filter matched nothing, `:178` raises rather than writing a
zero-row CSV that would read green.

## The adversarial corpus (BE3)

**BATCH 42, committed separately at `517f8e2`:
`tests/corpus/f6_api_wsd_sign_convention_and_clause_boundaries.txt`, 22 entries, every one
new this round and none of them read by the implementer.**

EG4(e)'s pause to 28 October permits it and the file header claims the exception explicitly:
every entry is on F4's load-mapping surface -- the `N` column of
`docs/F4_member_forces.csv`, the generator that writes it, and, new this round, the code
that READS that column and BRANCHES ON ITS SIGN to pick an allowable. A miss here reaches a
published allowable and a published clause number, not only a member force.

**COVERAGE: the shipped checks catch 5 of 22.**

```
cmd    grep "^id=" <the file> | grep -c "expect=catch"
out    5
cmd    grep "^id=" <the file> | grep -c "expect=miss"
out    17
```

Against the last four rounds -- 1 of 16, 9 of 21, 4 of 11, 8 of 13 -- this is the second
lowest, and for the same reason batch 41's was the lowest: **the surface has no gate.**
`grep -rl api_wsd tests/` is empty, so nothing under `tests/` reads either new file, and
seventeen of the twenty-two misses are on code that no test imports. The five catches are
all controls, and two of them are the measurements the hand-back asked for and did not have
(the branch-boundary continuity, and the sag guard's reach on each half separately).

**The useful number for the plan is not 5 of 22; it is that six of my eight blocking
findings are things G6.1's hand calculations and counter-cases would have caught.** That is
the measurement on the ordering, and it is in the section below.

## On FA3 versus G6.1 -- this one is Xabier's, not the implementer's

I was asked to rule on whether shipping a utilisation table before G6.1 is acceptable under
FA3's ordering, or whether FA3 and G6.1 conflict. **They conflict, and the measurement is
this round.**

FA3 says send it as soon as the first full pass exists. G6.1 says every one of the six
clauses is verified against an independent hand calculation before the milestone has a
result. Both are reasonable and they cannot both be honoured in one commit, because the
thing FA3 asks to be sent is the output of the thing G6.1 asks to be verified first.

**What the conflict cost, measured rather than argued.** Of my eight blocking findings,
**six are inside the scope of G6.1's own gate**: the sign convention (an independent hand
calculation of a member in tension finds it immediately), the local-buckling refusal (a
counter-case per clause is literally the missing refusal), the bending-branch cap (a hand
calculation at the branch limit is the first thing one does), `C_m`'s category and
direction (a hand calculation states the category it used), the provenance label (a hand
calculation names its input), and the sag guard's reach (a counter-case per check). Only
R745/R746, the report guards, are outside it. **And the table has already been sent.** The
correction that now has to go out is the second correction to a deliverable in eight days.

**My recommendation, offered once and not as a HOLD.** Keep FA3's ordering but bind it:
a published deliverable may go before its gate **if** the send carries, on its face, the
sentence that its clause implementations are unverified and that the numbers may move --
and if the gate lands in the next commit rather than the next revision. That is one
sentence in the label block and it is cheaper than a second correction. The alternative is
to invert the ordering for F6 step 2, which costs the send date.

**It is not a HOLD and it does not become another round.** I am ruling the step HOLD on
(a) and (d) items that stand on their own. This paragraph leaves the loop.

## On C27, for the third time -- also Xabier's

The report is right that the two directives disagree and right that this commit satisfies
both only by carrying the marker and the report together.

```
cmd    git log --oneline -2 -- docs/milestones/F6.md
out    0b9ea0d F6 step 1: the six API RP 2A-WSD clauses ...
out    da0e472 plan: EZ2 the envelope basis, EZ3 the numbering, EZ4 the F6 lock
cmd    git show --stat 0b9ea0d | grep -E "milestones/F6|reports/F6"
out    docs/milestones/F6.md       | 34 +++-
out    docs/reports/F6/step-1.md   | 135 ++++++++++++++
judge  marker and report in ONE commit, so FA3's "first commit" and the guard's "the commit
       that adds the report" coincide. They coincide only because this step took one
       commit. At `4344495` they did not and the guard refused.
```

**My ruling, and it is a ruling on the mechanism rather than a preference.** The guard's
rule is the one that can be enforced and the directive's is not: a marker moved in a
commit with no report leaves the tree in a state where `STEP` resolves to a step with no
report, which is the state `test_the_plan_names_the_step_under_execution` exists to refuse.
**So the guard is right and FA3's wording should change**, not the guard -- "the marker
moves in the commit that adds the step's report" is one phrase, it is enforceable, and it
costs nothing because a step's first commit can simply carry the report stub. If Xabier
prefers the directive's wording, the guard has to be deleted rather than extended (CZ0),
and then nothing checks the marker at all. **That is the choice, stated once.** It needs a
decision because luck of ordering has now resolved it twice and will not a third time.

## On the criterion -- I was asked, and I agree with it, and EZ0 is why this round is cheap

CZ0 as amended by EZ0 is right and I applied it. **All eight of my findings are (a), (c) or
(d)**: four defects in `floatfea/`, two in a published deliverable and its generator, and
two on a red suite with a red CI. **Nothing in this verdict is held against
a figure or a sentence** -- nine prose items went into the closure list, including C44 and
C48 which under the retired head would each have been a finding and would each have moved
nothing.

**AND I WANT TO RECORD WHAT EZ0 BOUGHT, because I asked for it twice and it is now
measurable.** R739 and R740 are both in the class the amendment added. Under the unamended
head R740 would be a closure item -- `scripts/` is not `floatfea/`, a label is not a
tolerance, the generator asserts nothing, and no test was red on it -- and `U = 1.815` would
have gone to Xabier labelled as a per-instant stress for a second round. R739 happens to sit
in `floatfea/` as well, so it would have blocked either way; R740 would not have. **One of
my two highest-value findings this round is blocking only because of EZ0.** That is the
third consecutive round in which the amendment's class carried the highest-value finding,
and it is the last time I will say so.

**One note on what EZ0 does NOT reach, said once.** `docs/F6_utilisation.csv` and
`docs/F6_utilisation.md` are generated by `scripts/measure/`, so they are squarely inside
the amendment. `floatfea/post/member_forces.py:23`'s inverted attribution sentence is in
`floatfea/` but is prose, and I have filed its substance under R739 as a site of the sign
defect rather than as a sentence -- which I think is the right reading, because the sentence
is the only statement of the convention anywhere and the next reader will take it as
authoritative. If that reading is too wide, say so and I will file it as closure class.

## Next step opens when

**STEP 1 STAYS OPEN. THIS WAS ROUND 1 OF THREE AND TWO REVIEWED REVISIONS REMAIN.** In
order, cheapest first, and the first one is one character plus a regeneration:

1. **R739 is answered** -- the sign convention is read once, from `docs/conventions.md:320`,
   with the 1 mm prescribed-stretch cell pasted as the control, both attribution sentences
   corrected, and `docs/F6_utilisation.csv` and `docs/F6_utilisation.md` regenerated in the
   **same** commit (BP0). My figures to beat: `F_a = 73.25` on the four platform ROOTs and
   `161.02` on the hub ROOTs, `u_axial = 0.001043` at the governing station, all four
   over-unity rows at Â§ 3.3.2, and `largest |U(K=2)-U(K=1)| = 0.034926`. If the regeneration
   disagrees with those, the disagreement is the finding and I want to see it rather than a
   reconciliation.
2. **R740 is answered** in the same commit, because it is the same label block and the same
   regeneration: the published column says which quantity it is, and `1.81496` against
   `1.7115` at the governing station is published beside it.
3. **R746 is answered** -- the `Answers:` header names this verdict, and the `Carried`
   section is the generator's table over verdict 109's list with R731 and R732 closed and
   **R737 named**.
4. **R745 is answered** -- the report's generated sections exist: `step-1-answers.json`
   committed, `## 0` and `## 0a` from `scripts/ci_section.py`, the whole-suite line from
   `scripts/suite_count.py` run AFTER every other edit, the five sections' numbers sourced,
   and the resulting `FAILED` list pasted with every id matched by name to EG3's state (2).
   **CI must be green at the revision's own commit**, or red with its cause named and
   traced.
5. **R741, R742, R743 and R744 are answered** -- each is a few lines and none needs a run.
6. **R737 is answered or recorded**, per verdict 109's two branches. One line either way.
7. **G6.1 is the step's locked content and is unstarted.** `docs/verification/api_wsd/`,
   six hand calculations not derived from the code, a counter-case per clause with a
   declared injection size and a plan row, and the tolerance the comparison needs -- which
   `docs/milestones/F6.md` Â§ 3 says must reflect float arithmetic and nothing else. **Six of
   my eight findings are inside that gate's scope.** It is not optional and it is not step 2.

**What I will not accept at revision 2.** A sign fix without the prescribed-sense control
pasted, because this project has now twice calibrated a sign against a cell that could not
see it. A regenerated table whose provenance label still names a column it does not read. A
clause function that returns an allowable above its own clause's cap. A `C_m` whose stated
direction is still the opposite of its measured one. And a control that reads the
intermediate rather than the published quantity -- that is R744, it is the third round on
those two lines, and the question for all five is the same one: if the thing this assertion
claims were false, would it go red. Today the measured answer is no for each.

**And one thing on the record for the implementer rather than against them.** The hand-back
named the five things to attack in priority order, and the order was right: item 1 was where
the defect was, item 3 asked me to attack a conclusion that turned out to be half wrong in
the direction the hand-back itself suspected, and item 4 self-reported the missing gate
before I could find it. The clause arithmetic the hand-back was least sure of -- `C_c`, the
safety-factor polynomial, the `3.3.2` max-of-two, the two shear forms, the SI conversion --
is correct in every case, and I checked each from the US forms rather than from the module.
**Three of the four numbers you have sent Xabier in this project were wrong, and the reason
is not the arithmetic: it is that nothing between the arithmetic and the send reads either
file.** That is G6.1, and it is the next thing to build.
