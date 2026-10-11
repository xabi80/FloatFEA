# Review — F6b step 1
Reviewed commit: e001aec0648b1b3b8b2a1cc37ae5897f7c658b63
Verdict: HOLD
Tests: 3289 passed, 37 failed, 1 skipped   (my own run, `python -m pytest -q -p no:randomly`, 769.92s)

## Round of 2026-10-11 -- F6b step 1, revision 1. **HOLD on ONE item, and it changes the headline.**

**Reviewed commit: `e001aec`.**

**Which clause I ruled under.** `CLAUDE.md` § "Step gating": **CZ0 (a) as amended by EZ0** --
a defect in a published deliverable -- with FI5's restatement that review effort goes to the
numbers. CA2/CK2 for the CI reading; EG3/EH1/EJ2/FC1 for the boundary red; EG4(e) for the
corpus; EH4 for the boundaries. **EU1 does not arise and I verified it rather than taking
it.** This increment touches no `floatfea/` and no `tests/`, so there is no element, solver
or tolerance surface in it at all.

**FI5 ASKED ME TO RECOMPUTE THE GOVERNING CHORD FORCE AND ITS REQUIRED AREA BY HAND. I DID,
AND BOTH REPRODUCE.** § 2 laid out every term and the addition closes:

```
claim  the governing chord force and area, by hand from FI1(a) and § 3.2.2
cmd    my own arithmetic on § 2's three terms, then my own tube algebra and clause
       transcription (A = pi/4(D^2-di^2), r = sqrt(I/A), C_c = sqrt(2 pi^2 E / Fy))
out    N/4     = -8.0025e+04 / 4   = -2.0006e+04
       My/(2h) =  1.801835e+08 / 6 =  3.003058e+07
       Mz/(2b) =  2.689043e+08 / 16 = 1.680652e+07
       bot_-b  = -2.0006e4 - 3.003058e7 - 1.680652e7 = -4.6857106e+07 N
       published                                      -4.685711e+07 N
       D from A: 0.125442 D^2 = A -> D = 1.33462 m, t = 0.055609, r = 0.451871 m
       KL/r = 3/0.451871 = 6.639 ; C_c = 108.06 -> INELASTIC, as published
       F_a = (1 - 6.639^2/(2*108.06^2))*355 / (5/3 + 3*6.639/(8*108.06) - 6.639^3/(8*108.06^3))
           = 354.33 / 1.689679 = 209.70 MPa
       A   = 4.685711e+07 / 2.0970e+08 = 0.22345 m^2   published 0.223439 m^2
rule   `A_required = |F| / F_a`, § 3.2.2 at `K = 1.0`, `L = 3 m` as § 2 declares
judge  **five-figure agreement on the area and exact agreement on the force.** And the
       three force terms are independently corroborated: `My = 1.8018e+08`,
       `Mz = 2.6890e+08`, `N = -8.0025e+04` at `platform:hub2_arm ROOT T=12.5` are the
       numbers I measured for a DIFFERENT purpose in verdict 122's R783 cell, one
       milestone ago. The arithmetic is right. **What is wrong is the `L = 3 m`.**
```

**And FI1(b)'s triangle derivation is right, derived by me from first principles rather
than checked against its own equilibrium.** Three point areas `A_c` at `(±b/2, 0)` and
`(0, h)`: centroid `h/3`; `I_yy = Σ A_c d² = A_c[2(h/3)² + (2h/3)²] = (2/3)A_c h²`;
`I_zz = A_c·2(b/2)² = A_c b²/2`; `F = A_c M d / I` gives `+My/h` at the apex,
`−My/(2h)` at each bottom chord, `±Mz/b` on the bottom pair and **zero `Mz` at the apex**.
Your own warning was the right one -- both equilibrium checks close for a wrong `I` with
consistent levers -- so I did not use them. `I_yy` and `I_zz` are the discrete second
moments and they are correct. **Apex-up declared with both moment signs evaluated per
instant is sufficient**: hogging and sagging are both reached, and flipping the section
would be a different truss, not a different load case.

**FI4(iii)'s hand table, all four by hand:** `A_c = M/(hσ)` with `M = 324 MN·m`,
`σ = 0.6·355 = 213.0 MPa` gives `324/639 = 0.50704`, `324/852 = 0.38028`,
`324/1065 = 0.30423`, `324/1278 = 0.25352` -- your `0.5070 / 0.3803 / 0.3042 / 0.2535`
exactly, and the directive's `0.51 / 0.38 / 0.30 / 0.25` confirmed as a rounding of them.

## Carried

**Checked, nothing carried from F6a** -- it closed with no blocking item open and its ledger
(R788-R791) stays on `docs/closure/F6a.md`. **One item of mine does close here, and it is
not F6b's:**

```
claim  R800 is fixed, and the exact state I reached in the last round now refuses
cmd    a throwaway clone at e001aec: plant docs/reports/F7/step-1.md with no verdict,
       docs/reports/F7/step-2.md AND docs/reviews/F7/step-2.md stamped at HEAD
out    BLOCK: "these step reports have no supervisor verdict: docs/reports/F6b/step-1.md
               docs/reports/F7/step-1.md"
cmd    the same clone, no plant; then count F2 names in the refusal
out    BLOCK naming docs/reports/F6b/step-1.md only; F2 names in it: 0
cmd    git show 6de156e -- .claude/hooks/require-verdict.sh | code hunk only
out    + pre_gating="docs/reports/F2/step-1.md docs/reports/F2/step-2.md docs/reports/F2/step-3.md"
       - gate_from / the whole verdict-set loop: DELETED
cmd    awk the block() body | sha256sum ; bash -n
out    42ab11d92c8e7215  (unchanged across 31fe039, 60bb3f0, 6de156e) ; (no output)
judge  **R800 is CLOSED by construction, not by measurement alone**: there is no
       `gate_from` any more, so there is no state left for an inference to be wrong in.
       `6de156e` is a standalone `process:` commit citing R800, touching only the hook,
       and I read all 69 changed lines. **No STOP-class finding.** The F2 trio stays
       exempt and the three paths are declared with the measurement beside them.
```

## Findings

**R801. (a, BLOCKING) The declared truss geometry is self-inconsistent for `h ≠ b`, and
BOTH ways of resolving it move the published platform-box headline from mass-consistent to
not. Exactly one cell in the whole sweep flips, and it is the headline.**

```
claim  the unbraced length used for the chord, located in the generator
cmd    grep -n "panel_length=min\|panel = min\|FI1: diagonals" scripts/measure/f6b_truss_sizing.py
out    298:    a_c, branch_c = area_for_compression(-worst_c[0], panel_length=min(h, b))
       309:    # FI1: diagonals at 45°, panel length = the face dimension, force = ...
       315:    panel = min(h, b)
rule   FI1: "Diagonals at 45° (panel length = the face dimension)" -- and a box with
       `h = 3`, `b = 8` has TWO face dimensions, 3 and 8
judge  **the comment says "the face dimension" and the code takes the minimum of two
       different ones.** At `h = 3, b = 8` a 45° diagonal in a 3 m panel spans 3 m across
       the face; the horizontal faces are 8 m across, so it does not reach the far chord.
       The geometry cannot be built as declared, and the two repairs available go in
       opposite places.
```

```
claim  BRANCH (A) -- 45° on every face, so the panel differs per face. A circular tube has
       `r_y = r_z`, so a corner chord braced every `h` in the vertical plane and every `b`
       in the horizontal one buckles over `max(h, b)`.
cmd    my own re-size of the PUBLISHED chord force at `L = max(h,b) = 8`, same clause
       transcription, diagonals unchanged
out    A at L=3 : 0.223439  (reproduces the published figure exactly)
       A at L=8 : 0.230871  ->  1.0333x
       line mass 9175 -> 9452 kg/m      ratio 0.979 -> **1.007**
rule   `max U`'s analogue here: `ratio = line mass / μ <= 1.0`, μ = 9375 kg/m
```

```
claim  BRANCH (B) -- one uniform panel `p = min(h,b) = 3`, so `L = 3` stands and the chord
       is braced at 3 m in both planes -- but then the two 8 m faces' diagonals are not at
       45°: θ = atan(8/3) = 69.44°, length = hypot(3,8) = 8.544 m per 3 m of truss.
cmd    my own recompute: force falls by sin45/sin69.44 = 0.7552, steel per unit length
       rises by 8.544/3 = 2.848 instead of the published 1.41421
out    diagonal steel 0.122584 -> 0.154528 m^2
       line mass 9175 -> 9463 kg/m      ratio 0.979 -> **1.009**
rule   FI2: `(Σ chord A + diagonal A · length per panel / panel length) · ρ · 1.15`
```

```
claim  how far this reaches: every cell of all four sweeps, under both branches
cmd    my own script over the 168 published answers, re-sizing from each cell's own
       published chord force and diagonal area
out    section  group     published shallowest   under (A)        under (B)
       box      platform  (3, 8) @ 0.979         (4, 6) @ 0.965   (4, 6) @ 0.960
       box      hub       (2, 2) @ 0.674         (2, 2) @ 0.674   (2, 2) @ 0.674
       triangle platform  (4, 8) @ 0.948         (4, 8) @ 0.967   (4, 8) @ 0.976
       triangle hub       (2, 2) @ 0.664         (2, 2) @ 0.664   (2, 2) @ 0.664
       cells that flip from mass-consistent to not:
         under (A): [(3, 8, 0.979 -> 1.007)]      under (B): [(3, 8, 0.979 -> 1.009)]
judge  **surgical, and that is what makes it a finding rather than a quibble.** One cell
       flips, under either branch, and it is the one number the deliverable leads with.
       The hub headlines sit at `h = b = 2`, where `min = max` and the inconsistency does
       not exist. The platform triangle headline survives both (0.967 / 0.976). The error
       scales with aspect ratio and the headline is at the grid's most extreme ratio, 8:3
       -- **`min(h,b)` is most wrong exactly where the sweep's answer was taken.**
cell   one variable moved per branch: the chord's `L` in (A), the larger faces' diagonal
       geometry in (B). Same forces, same clause, same ρ, same joint allowance.
```

**Closed when** the deliverable's platform-box headline is a cell that survives its own
declared geometry -- `h = 4 m` at `b = 6 m` under both branches -- **and the geometry is
stated unambiguously rather than assumed twice.** Either 45° on every face, and then the
chord is braced over `max(h, b)`; or a uniform panel at `min(h, b)`, and then the larger
faces' diagonals carry their true angle and length. **Either one; what may not stand is a
sizing that takes the shorter buckling length from one reading and the shorter diagonal from
the other.** If FI1's declared geometry is itself the problem, that is a plan question and
it stops and asks rather than being resolved in the generator.

### The six things you asked me to attack, ruled

**(1) FI3's one real decision -- sizing each group to the envelope over its members -- is
what FI3 meant, and I would have ruled it that way without being asked.** FI3 says "one
section per arm group", and FG2's two groups are unchanged here. Sizing each arm for its own
orientation would publish four different platform arms at one heading, and the `Mz ≈ 0` on
arms 1 and 3 is a fact about which way the wave is coming, not about the steel: your plan
§ 2b records `My = 1.916016e+08` on all four at ROOT static, which is my own verdict 122
measurement, and the four arms are geometrically identical. **`b` may not be made small on
the grounds that `Mz ≈ 0`, and the plan says so in those words.** The decision is right and
it is stated in the deliverable as a finding, which is where it belongs.

**(2) Ruled above: the derivation is right and I checked `I`, not the equilibrium.**

**(3) MONOTONICITY HOLDS, AND IT IS NOW MEASURED RATHER THAN HOPED.** This is the doubt you
were least confident about and it is the one that cost least to settle:

```
claim  `slack(D) = F_a(D) − |F|/A(D)` is strictly increasing with exactly one root, over
       every panel length and every demand the sweep produces
cmd    my own sweep: 145 distinct demands (4.181e+06 to 1.795e+08 N) x 13 panel lengths
       (every min(h,b), every max(h,b), and every min/sin45), 4001 samples of D in
       [0.02, 6.0] each
out    pairs where slack is NOT strictly increasing, or has more than one sign change: 0
       1885 pairs x 4001 samples = 7541885 evaluations
rule   the docstring's claim: "the demand |F|/A(D) falls as D grows and F_a(D) rises, so
       |F|/A − F_a is monotone decreasing and has one root"
judge  **true, and provable as well as measured.** At fixed `D/t`, `r ∝ D`, so `KL/r` falls
       monotonically and `F_a` rises monotonically to `0.6 F_y`; `|F|/A` falls as `D²`; and
       § 3.2.2(b)'s local-buckling reduction is a function of `D/t` ALONE, which is held at
       24 -- so there is no term that can turn the sign round. **The slender end is where
       `F_a` is smallest, which makes `slack` more negative, not non-monotone.** The
       bisection's root is the root. And `slack(hi) < 0` raising rather than extrapolating
       is the right refusal; nothing in the sweep reached it because nothing needed `D > 6 m`.
```

**(4) Your torsion finding is confirmed by hand, and the repair's own figure is right.**

```
claim  the torsion share formed from its own terms, not by differencing
cmd    my own arithmetic: q = |T|/(2 A_enc), A_enc = b h = 24 m^2 at (3, 8);
       share = q h / face shear
out    q     = 1.411678e-09 / 48       = 2.94099e-11 N/m
       q h   = 2.94099e-11 x 3         = 8.82298e-11 N
       share = 8.82298e-11 / 2.956708e+06 = 2.98406e-17
       published 2.984057271793956e-17
judge  **exact to six figures by hand.** `T = -1.41e-09 N·m` against a face shear of
       `2.96e+06 N` is a ratio of `1e-17`, and a difference of two resolutions that agree
       to sixteen figures cannot represent it -- returning exactly zero was the correct
       output of the wrong method. This is G4.1's rule and you applied it. **And the part
       that matters most is how you caught the stale differencing lines: the figure
       disagreed with a hand calculation.** Nothing in this repository would have caught
       `0.000e+00` for a quantity whose true value is `1e-17`, because both read as zero
       to any threshold anyone would write. That is worth recording as the reason FI5 asks
       for a hand recomputation at all.
```

**(5) FI4(v)'s narrow answer is ACCEPTABLE and no ablation cell is required.** BG0 attaches
to a *causal* sentence -- "X caused Y" -- and your answer is not one: "a vertical force on
the centreline makes no moment about the vertical axis through that centreline" is statics,
exact rather than approximate, and it answers the question FI4(v) asked. **What would have
needed the cell is the claim you correctly did not make** -- attributing `My` between the
remainder and the arms' own mass -- and you said so. The right disposition is to answer the
question asked and name the one you cannot answer, which is what § 3 does.

**And your sharper finding is confirmed, independently, and it is the most valuable thing in
the increment.**

```
claim  the remainder's height is not a modelling choice, and no truss in the grid reaches
       the deck CoG
cmd    build_superstructure(), then my own closed form (z_cog − f·z_joint)/(1−f)
out    model: z_joint=24.668478  z_cog=35.000000  z_r=65.994565  f=0.75
       closed form                       = 65.994564803    |diff| = 1.421e-14 m
       a chord-symmetric truss reaches z_joint + h/2, so CoG 35.0 needs h = 20.6630 m
       the grid stops at h = 10 -> best CoG 29.668 m, short by 5.332 m
judge  **confirmed to 1.4e-14 m, and the inversion is right.** `h/2` is the correct ceiling
       for a truss with equal chords top and bottom; a triangle apex-up reaches only
       `z_joint + h/3`, so `h/2` is the generous bound and the conclusion holds a fortiori.
       **At every depth in the grid and whatever `f` is** -- because `f` cancels out of the
       ceiling. This is the FI4(v) flag turned into a number and it is the finding increment
       2 actually needs.
```

**(6) FI4(iii)'s hand table confirmed above, all four values, by hand.**

## Tolerances touched

**None, and EU1 does not arise -- verified, not taken.**

```
cmd  git diff --stat 91dd224..HEAD -- floatfea tests floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 91dd224..HEAD -- tests/conftest.py 'tests/**/conftest.py'
     git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  (empty) ; tests/conftest.py
```

**No `floatfea/` and no `tests/` line changed**, which is FI0's "post-processing only" taken
literally, so no value, no counter and no injection -- and § 4 of the plan is right that
`D/t = 24`, the `1.15` joint allowance, the 45° diagonals, the grids and `F_y` are FI's
declared inputs carried in the label rather than tolerances. **One caution for the record,
not a finding:** `D/t = 24` and `1.15` are the two declared inputs that most behave like
tolerances, because the answer scales directly with both -- the label names them, which is
what the rule asks, and if increment 2 ever chooses either to make two numbers agree it
becomes `floatfea/tolerances.py`'s business.

**My own instructions: `git log 91dd224..HEAD -- .claude docs/SUPERVISOR.md` gives one
commit, `6de156e`**, standalone `process:`, citing R800, touching only the hook, read line
by line and measured in `Carried`. **No step commit touches them. No STOP-class finding.**

## The suite, lint and CI at the reviewed commit (CA2, CK2)

```
cmd  python -m pytest -q -p no:randomly          (mine, at e001aec)
out  37 failed, 3289 passed, 1 skipped, 2 warnings in 769.92s (0:12:49)
     all 37 are in tests/test_report_carried.py (18) and test_report_guard_states.py (19)
     outside those two files: 0 failed
     tests/test_report_numbers_are_sourced.py: 21 passed   <- the control, and it holds
cmd  gh api .../runs/38145178050/jobs  (head e001aec)
out  lint, unit and guards     failure   runner "GitHub Actions 1000001686"
       steps: actionlint OK, ruff OK, black --check OK, mypy OK, unit tests OK,
              guards and meta-tests FAILURE        <- the ONLY failing step
     the verification ladder   success   runner "GitHub Actions 1000001687"
     CI determinism -- leg / ten legs agree   skipped (workflow_dispatch only, by design)
cmd  gh run view 38145178050 --log-failed | the run's own summary line
out  37 failed, 975 passed
```

**CI is RED and it does not HOLD, under EG3 and nothing else -- and the reason is measured
rather than assumed.** CI's count is the same **37** as my own run; `ruff`, `black`, `mypy`
and the unit-test step all SUCCEEDED, so `guards and meta-tests` is seen to have RUN rather
than skipped behind an earlier red (CZ1 (iii)'s own concern); and the ladder is green on a
second runner. **CA2 is satisfied because nothing outside the boundary set is red, not
because a local run said so.** CK2 does not apply: no job has `runner_name: ""` with a
payment annotation.

**The boundary red, traced by name (EG3 state (1), generalised).** `docs/reviews/F6b/` did
not exist at the reviewed commit -- not "no verdict for this step" but **no verdict for the
MILESTONE**, so every verdict-reading guard reads an empty string. The 18 in
`test_report_carried.py` are state (1)'s own `test_the_guard_reads_the_step_being_worked_on`,
the FC1 pair (`test_the_report_carries_a_WHOLE_SUITE_count`,
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`) which cannot pass in the commit they
describe, and the parametrisations that collapse to `(no finding parsed from the verdict)`,
`(none)` and `(no site parsed)` -- each naming the empty verdict in its own failure line,
not identified by family. The 19 in `test_report_guard_states.py` cascade off a red
`[baseline]` (EH1). **Any red outside that set is CZ1 (iv) unchanged, and there is none.**

**The `1 skipped` is new this milestone and I am naming it rather than passing over it**, as
the only line in my run that F6a's runs did not have. **It is a closure item, not a
finding** -- but a skip that appears with a new increment is worth a sentence in the
artifact saying which test and why, because "empty parameter set is an error, not a skip" is
this project's own rule and a reader cannot tell the two apart from a count.

## The corpus (EG4(e))

**The pause held. No corpus file added by the implementer or by me, and no batch run** --
`git log 91dd224..HEAD -- tests/corpus` is empty, so 0 new entries and no coverage
measurement, which is the pause's intended consequence. EG4(e)'s two open exceptions (F4's
load-mapping gate, EB6's label-provenance gate) are untouched.

**What I ran instead -- the recorded substitute, both halves:**

* **A continuum grid over the parameter space the decision rule guards.** The sizing
  re-derived independently of the generator over all 168 published answers, both branches of
  the geometry, plus 7.54 million evaluations of the bisection's own monotonicity over every
  demand and every panel length. **R801 came out of the grid and nothing else** -- it is
  invisible from the single cell the deliverable reports.
* **A regeneration check on the published deliverable.** `f6b_truss_sizing.py` then
  `f6b_report.py` then `git diff --stat -- results/F6b/` is empty at this commit. I ran it
  rather than reading your claim of it.

## Try to break it

**The case I built is the one the sweep's own shape makes available: the answer sits at the
grid's most extreme aspect ratio, and the only length entering § 3.2.2 is a `min` over two
numbers that are 8 and 3.** That is R801. Everything else held -- the chord force, the area,
the triangle's section properties, the hand table, the torsion term, the remainder-height
closed form and the bisection's single root all reproduce, most by hand and all of them
independently of the generator.

**What I could NOT break:** the hub answers (at `h = b = 2` the inconsistency does not
exist), the platform triangle headline (survives both branches), and FI3's envelope decision
(correct, and the alternative is void at the next heading).

## Next step opens when

**FI5 says STOP after this, so the HOLD's force is on the deliverable rather than on a gate,
and it is one item:**

1. **R801** -- the platform-box headline is a cell that survives its own declared geometry,
   and the geometry is stated once rather than assumed twice. `h = 4 m, b = 6 m` is the cell
   under both branches. **The sweep tables move with it, and BP0 applies: the chord `A`
   column, the line-mass column and both platform ratio tables are regenerated, not
   patched.**
2. **The corrected deliverable is re-sent to Xabier**, because the uncorrected one carries a
   headline that reads mass-consistent and is not. That is the item; a corrected file
   sitting in `results/` is not it.
3. **The `1 skipped` is named in the closure artifact** with which test and why.
4. **CZ1's four outputs** at the closure commit, in its own record. **EQ0 applies if that
   commit changes a gate or a tolerance** -- on current scope it changes neither, so it is
   not reviewed, which means item 1 is answered on your record with the triples and nobody
   checks it. Say that plainly in the artifact rather than implying a review that will not
   happen.

**And what this HOLD is not about.** The arithmetic is right everywhere I could reach it,
and FI5 asked for exactly the check that found the one thing that is not. Six required items
answered, a torsion term caught by its own author against a hand value, a premise verified,
and a deck-CoG result increment 2 needs. **The HOLD is one `min` where the geometry has two
numbers**, and it blocks only because it moves the single figure the document leads with.

## Disagreement with the criterion -- none this round

R801 is squarely CZ0 (a) as amended by EZ0: a defect in `results/F6b/truss_sizing.md` and in
the `scripts/measure/` script that produces it, changing a published headline. I did not
have to reach for a carve-out, and nothing else I found is blocking -- the `1 skipped` and
the `D/t = 24` caution are both closure items and I have said so at each.
