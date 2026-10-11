# F6a — THE REQUIRED SECTION · INCREMENT CLOSURE

**Status: CLOSED pending the EQ0 review this artifact asks for.** One step, one reviewed
revision under FG1's lighter process. **Verdict 122 HELD on three items**, every one a
sentence published around numbers the reviewer reproduced to the digit by an independent
route; all three are repaired at `35de6cb`, together with two gating-apparatus items under
FF0 and the five closure items.

**FG1 allowed one reviewed revision and it has had it.** This artifact exists because
verdict 122's item 6 reasoned that the closure commit would change no gate and no tolerance
and therefore would not be reviewed. **That reasoning no longer holds and I am saying so
rather than taking the exemption:** `35de6cb` changes a gate assertion (R784's exemption
clause in `tests/test_report_carried.py`) and adds one (C99's test in
`tests/verification/rung3/test_platform_skeleton.py`). EQ0 applies on its own terms, and
EB4 says that review counts against no step's rounds.

Committed date: **FG5 asked for the deliverable by 16 October. It existed on 10 October and
was corrected on 10 October.** The date holds; nothing was traded for it.

---

## 0. Verification at closure (CZ1)

{{SECTION_0}}

---

## 1. What F6a ships

**The deliverable**: `results/F6a/required_section.md` and `results/F6a/required_section.csv`,
labelled INDICATIVE — a stand-in tube for a truss of undecided depth, placeholder masses,
one heading, `F_y` assumed. Sent to Xabier twice: the first version on 10 October, the
corrected version the same day, with a PDF rendered outside the repository.

**The search**: `scripts/measure/f6a_required_section.py`. FG3's three searches per group
against F4's governing envelope, per instant, at ROOT / MID / TIP, under the same API
RP 2A-WSD clauses as F6 (`F_y = 355 MPa`, `K = 2.0`, `C_m = 0.85`, no one-third increase).
A candidate outside a clause's own range is refused, never extrapolated.

**The premise check**: `scripts/measure/f6a_premise_check.py`. FG2's premise, verified in
both halves and **narrower than it was stated** — see § 3.

**The generator**: `scripts/measure/f6a_report.py`, reading three files and typing no
measured figure.

**One `floatfea/` change**: `build_superstructure(measurement_sections=...)`, a sensitivity
entry point with no default, no environment variable and no file it can be set from. It
exists because FG2's premise cannot be verified without a way to build at a section the deck
does not record.

### The six answers

| group | search | D [m] | t [mm] | D/t | A [m²] | W [m³] | max U | ρA/μ |
|---|---|---|---|---|---|---|---|---|
| platform | (i) `D = 2.5` fixed | 2.5 | 410 | 6.10 | 2.6920 | 1.2212 | 0.9957 | **2.254** |
| platform | (ii) `t = 180` fixed | 3.2 | 180 | 17.78 | 1.7078 | 1.2212 | 0.9958 | **1.430** |
| platform | (iii) minimum area | 6.0 | 55 | 109.09 | 1.0272 | 1.5128 | 0.9835 | 0.860 |
| hubs | (i) `D = 2.5` fixed | 2.5 | 140 | 17.86 | 1.0380 | 0.5801 | 0.9899 | 0.543 |
| hubs | (ii) `t = 180` fixed | 2.3 | 180 | 12.78 | 1.1988 | 0.5899 | 0.9726 | 0.627 |
| hubs | (iii) minimum area | 6.0 | 30 | 200.00 | 0.5627 | 0.8356 | 0.9911 | 0.294 |

The table is the deliverable's and is reproduced here as the increment's result, not as a
second source. **Every digit was reproduced by the reviewer independently** — clause
transcription, section-property algebra, brute-force search with no area pruning, and member
lengths set from the deck geometry rather than read from the search's own helper.

## 2. The tolerances F6a declares

**None.** No value was added to `floatfea/tolerances.py` and none was moved.

```
claim  no tolerance moved across the whole increment -- four commits, ca611e3..HEAD
cmd    git log --oneline ca611e3..HEAD ; git diff --stat ca611e3..HEAD -- floatfea/tolerances.py
out    35de6cb F6a step 1 revision 2: verdict 122's three sentences, two apparatus items, ...
       1d2be7b review: F6a step 1 revision 1 -- HOLD on three, all sentences and all mine. ...
       8c14931 F6a step 1: the required section, its premise, and the mass contradiction
       4013d61 process: FF0 -- a closure item in the gating apparatus is not ledgered
       (the diff is empty)
rule   `max U <= 1.0` is the clause's own threshold; the grid steps are FG3's and declared;
       the premise's `1.608328e-15` is reported against round-off, not against a ceiling
judge  no counter is declared or moved, so **EU1 does not arise** -- there is no
       configuration axis for an adversarial case to range over, because no number in this
       increment was chosen to make two quantities agree.
```

## 3. The finding that matters most, which is not a defect

**FG2's premise is TRUE and NARROWER than it was asserted, and the narrowing is the
increment's most useful output.**

FG2 asserted that section choice does not change the loads or the member forces. On the
static case that holds to round-off — `1.742356e-15` relative at the worst of the three
searches, over a `2.62×` span of platform area. (`1.608328e-15` is the figure the deliverable
publishes; it is answer (iii)'s, not the worst of the three, and this artifact says which.) **On the dynamic case the member forces MOVE.** The argument
originally given for why they could not was wrong, and the mechanism is specific: the
d'Alembert field is an *acceleration*, and what turns it into a load is
`element_equivalent_load = M_e @ a_e` with the consistent element mass matrix, whose rotary
terms are `ρ_eq·I = μ·r²`. **`r` moves with the section even though `μ` is held.**

What does not move is `max U` — the quantity the search's answer actually depends on — after
re-selecting which instant governs at the sized section. **Largest change across all six
answers `3.496e-06`; smallest margin `1 − max U` across all six `4.220e-03`** — the motion is
`1207×` inside the tightest margin, and the two are quoted from different answers deliberately
(the largest motion is on the hubs at (iii), the smallest margin on the platform at (ii)), so
the comparison is the worst case of each rather than one answer's pair.

**So the premise the method needs is a statement about `max U`, not about the forces.** That
is a weaker claim than FG2's and it is the one that is true. It is recorded here because
increment 2 will re-run this machinery with a different mass basis and the distinction is
what makes the re-run legitimate.

## 4. The blocking items, and how each was repaired

### R781 — a provenance sentence that told the reader not to check

`results/F6a/required_section.md:5` said "no figure is typed", and four figures in the
document were string literals in the generator. **All four were correct.** The defect was
that three of them could not be read from anything, and the sentence that said so was the
one sentence telling a reader these figures cannot go stale. BP0's recorded species exactly.

Repaired by the first of the two routes the condition offered: `f6a_premise_check.py` emits
JSON and the generator reads it; F6's stand-in `U` is read out of `docs/F6_utilisation.csv`.
The label now says **"No MEASURED figure is typed"** and names what is written literally —
the declared inputs and the clause's own constants.

### R782 — a docstring claiming a comparison the file did not make

It said it compared "on BOTH the static and the dynamic cases"; it called `_static_rows`
twice, at one search per invocation. Repaired by **putting the dynamic half in the file**
rather than by narrowing the claim, because the reviewer's measurement of it is not in this
repository and a narrowed docstring would have left no record of it in the tree. Both halves
now run at all six answers.

### R783 — a grid coincidence published as a property of the structure

The two constrained platform answers agree to six figures on `W`. **The mechanism is real**:
bending is `99.98595%` of `U` at the governing station and both answers sit in the same
compact branch, so `F_b` is identically `0.75 F_y` and the required `W` is the same quantity
in both searches. **The precision was not.** Inverting the decision rule instead of sampling
the grid puts the two exact requirements `7.994e-05` apart; the published grid answers agree
to `2.565e-06`, which is `4.2e-04` of one grid step in `W` at `D = 2.5 m`. Two independent
grids landing that close is luck.

```
claim  the fraction of a grid step the published agreement amounts to
cmd    python -c "the published_spread_relative and grid_step_W_at_D_2.5 keys of
       results/F6a/required_section.json, and their ratio"
out    published spread relative = 2.564914e-06
       grid step in W at D=2.5   = 0.007515 m3 = 6.153911e-03 relative
       the spread as a fraction of ONE grid step = 4.168e-04
rule   the deliverable's own generated line 155: "one grid step in W at D = 2.5 m is
       0.007515 m^3, so that agreement is 4.2e-04 of ONE step"
judge  **a draft of this artifact said `3.85e-05` here**, taken by dividing by the D-grid's
       larger step rather than the one the sentence names. One grid, one step, one
       denominator -- and the figure published is the deliverable's own.
```

Repaired by publishing the number that transfers — `W_req = M_res / F_b = 1.215739 m³`, with
its allowable named, because answer (iii) does not share it at `D/t = 109.09` — and by naming
the six-figure agreement as a coincidence inside the mechanism's own spread.

## 5. The two gating-apparatus items (FF0 — fixed, not ledgered)

**R784.** `test_a_report_does_not_say_CLOSED`'s exemption was keyed on the sanctioned
sentence alone, so a table whose item rows the parser cannot read took the early return with
`CLOSED` in it. **Fixed, and not by the clause the condition proposed.** The condition named
"no finding mentioned in the section at all"; implemented, that clause refused this report's
own revision 1, which declares the empty carry and then names the eleven items that stay on
F6's ledger — the declaration done well. The clause adopted asks the **verdict's** finding
list instead, which is also the half an implementer cannot write, the reviews tree being
hook-protected. Two cases, one per direction.

**R785.** `scripts/write_verdict.py --milestone` was `type=int`, so `F6a` was inexpressible
through the one sanctioned path into the reviews tree — the reviewer wrote verdict 122 by
widening the type in a wrapper. It now takes a label; `6a`, `6` and `F6a` are accepted and a
non-label is refused, the value still being a path segment.

## 6. The ledger — what is open, by name

**Nothing blocking.** F6a's five closure items C98–C102 were all **fixed in `35de6cb`**
rather than deferred, because four of the five are in the published deliverable or in
`floatfea/` and the deliverable was being re-sent. Deferring them would have meant sending a
file with known defects in it.

| item | what it was | where it was fixed |
|---|---|---|
| C98 | the boundary caveat had no direction and no rate | the search's `boundary_sweep`, published in the deliverable |
| C99 | the `measurement_sections` comment's mechanism was wrong (CW0) | a test, `test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION` |
| C100 | a missing code fence made the report render wrong | one fence; the count goes 37 → 38 |
| C101 | "THE EIGHTEENTH" for what the same revision calls the seventeenth | the word |
| C102 | the `× the μ-basis term` column was the mass-ratio column restated | the two-row table is deleted |

**F6's ledger stays on `docs/closure/F6.md` and is not re-opened here.** FG1 scoped this
increment to the numbers. The long-standing set — R765–R768, R773, R774, R777–R780, C41–C70,
C77–C79, C82, C90–C97 — is unchanged by F6a and nothing in it reached a member force in this
increment.

**One item of F6's ledger did clear.** C89 and C88 were repaired under FE0 before F6a opened,
which is why this increment's suite is green with zero waived reds rather than red by eight.

## 7. The limitations every F6a number carries

These are the deliverable's own label, repeated because a number travels further than its
caption:

1. **The arms are trusses, not tubes.** Every section here is a stiffness-equivalent
   stand-in for a triangulated arm of undecided depth (`docs/milestones/F1.md:390`). `W`
   grows with `D²t` and a truss buys it with depth; the transfer is qualitative.
2. **The masses are placeholders.** Platform `9.375 t/m`, hubs `15.0 t/m`, and § 8 is about
   exactly this.
3. **One heading, 0°.** F4's envelope is the four in-band periods at one heading. A heading
   plan is increment 3.
4. **`F_y = 355 MPa` is assumed**, not specified. It is the single most load-bearing
   unverified input in the chain: `F_b`, `F_a`, `F_v` and `F_xc` all scale with it.
5. **The grid's bounds are FG3's.** `D ∈ [2.0, 6.0] m`, and the minimum-area answers sit at
   the upper bound. § 8.

## 8. The contradiction increment 2 has to break

**The section each platform arm needs to pass outweighs the mass assumed for it.** `ρA_req/μ`
is `2.254` at answer (i) and `1.430` at answer (ii). Only the minimum-area answer is
mass-consistent, and it sits at the grid's upper bound.

**The model cannot feel this**, and that is why the search converges: `_build_body` computes
`member_mass = fraction × deck_mass` with no section term and then back-computes
`density = line_mass / section.A`, so `ρ·A` is the deck's own `μ` whatever `A` is. A heavier
section carries no more self-weight in the solve.

**And the arm-weight term alone understates it.** Holding the body's remainder mass at its
published value and scaling only the arm, the implied static root moment is `1.752×` the
present total at answer (i) and `1.258×` at answer (ii) — **two of the three platform answers
imply more root moment than the static case currently carries in total**, before any wave
load and before the larger section that extra weight would itself require.

**The conclusion is also a function of a bound that was given rather than derived.** The
minimum passing area falls as the bound rises — `ρA/μ` is `1.126` at `D = 4.0 m`, `1.014` at
`4.9`, `0.972` at `5.0` — so the mass-consistency verdict for answer (iii) **flips between
`D = 4.9` and `D = 5.0 m`**. Had FG3 written `D ≤ 4.9 m`, the increment's headline finding
would have read the other way: no mass-consistent section anywhere in the declared range.

**This increment does not iterate the mass.** FG4 says not to and FG6 stops work here.
Increment 2 needs Xabier's mass budget; increment 3 needs a heading plan.

## 9. One finding of my own, in a repair

The first sentence written about C98's boundary sweep said the minimum passing area falls
**monotonically** toward the bound. It does not — `9` of `36` platform steps rise, the
largest by `2.38%`, and `18` of `40` on the hubs, because the 5 mm wall step quantises the
answer. Every figure the paragraph published was correct; the shape claimed over them was
not, and I had looked at five of forty-one rows.

**This is the species F6's closure artifact records six instances of, happening a seventh
time and in my own repair of a closure item: an assertion whose domain excludes the thing it
names.** The question that caught it is the one that catches all of them — *what is the
collection this sentence quantifies over, and did I look at it?*

Six of the seven were caught by a reviewer. This one was caught by running the check the
sentence implied, which is cheaper, and it is the only one of the seven where the rule was
already written down when the sentence was written.
