# F2 step 5 — V1.1 rigid-body modes / gate G2.1 · CLOSURE

**Status:** closing on the fifty-third verdict, under CZ0's three-verdict rule.
Fifty-two review rounds on this step. **No defect was ever found in the element
formulation or in the gate's quantity after it took its present form.**

    claim  over the last twelve commits under review, `floatfea/` received no
           change outside comments -- every finding in that span was in the
           record describing the gate or in the apparatus certifying it
    cmd    git diff 7ffd67a~12..7ffd67a -- floatfea/ | grep -E "^[+-]" |
           grep -v "^[+-][+-]" | grep -vE "^[+-][[:space:]]*#" |
           grep -vE "^[+-][[:space:]]*$" | wc -l
    out    0

---

## 1. What G2.1 asserts — two claims, not one

The gate is two independent statements about the assembled stiffness `K`, both
taken on `K_hat = K / max|K|`, and **both must hold**:

**Claim A — the six analytic rigid-body vectors are annihilated.**

    max_j ( ||K_hat v_j|| / ||v_j|| )  <=  RIGID_MODE_EXACTNESS

Six analytic vectors — three translations, three rotations about the centroid
— are imposed directly. No eigensolver, no solve, no starting vector. This is
a statement about `K` and those six vectors and nothing else.

**Claim B — there is no seventh.**

    lambda_7(K_hat)  >=  RIGID_MODE_BOUND * ||K_hat|| * eps

Claim A plus Courant–Fischer puts six eigenvalues at the arithmetic floor, so
what remains to certify is that the seventh is not there. That is a statement
about `lambda_7` alone, and it is **not a count of small eigenvalues**. A
count is what this gate asserted before CU0, and nothing in the repository
could distinguish one small eigenvalue from another under it: the two
constants entered the only assertion as their product, so no measurement here
could attribute a decision to either.

**Why two and not one.** Claim A is exact and unconditional, and it is the one
that would catch a defective element. Claim B is conditional on the frame's
conditioning and is the one that goes undecidable. Collapsing them would make
a conditioning-limited frame look like a failed element.

| constant | value | form |
|---|---|---|
| `RIGID_MODE_EXACTNESS` | `1e-15` | relative, dimensionless |
| `RIGID_MODE_BOUND` | `199.526231496888` | multiple of `‖K_hat‖ · eps` |
| `RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | `1.0e-14` | injected stiffness |
| `RIGID_MODE_BOUND_COUNTER_DEFECT` | `1.0e-13` | injected stiffness |

`RIGID_MODE_BOUND` replaced `RIGID_MODE_FLOOR * 10**RIGID_MODE_GAP` at CU0:
the two entered the only assertion as their product, so the decision had one
degree of freedom and now has one constant. The value is that product, to the
digit.

## 2. Undecidable is a third outcome, and this is its domain

A frame whose `lambda_7` falls **below** the bound is not declared defective.
It is declared **undecidable**, which is a red outcome distinct from failure:
the arithmetic at that conditioning cannot tell a mechanism from round-off, and
saying so is the honest answer. A frame is decided only when `lambda_7` is
above the bound; it fails only when a genuine seventh mode is found.

Measured over the reviewer's corpus, `tests/corpus/g21_rigid_body_frames.txt`,
none of it written by the implementer. Every frame falls in exactly one of
three classes: **decided and clear of the window**, **refused and clear of
it**, or **inside the window**, where the outcome is a property of the machine.

**The counts are deliberately not written here, and this paragraph is why.**
They were published figures; they read 126 / 33 / 88 / 25 / 13 when this
artifact was first written, and by the time it was next read the corpus had
grown twice and every one of them was wrong. Each time, the repair was a commit
after a closed step, which reddened a second guard. DB1 retires them: the claim
is that no frame breaches the ceiling and that every refusal is a declared
outcome, and `tests/verification/rung1/test_rigid_body_corpus.py`
asserts it over whatever the corpus holds. A reader who wants today's partition
runs that test.

**The window is real and it is a property of the arithmetic, not of the
element.** The thirteen frames inside it are a unit-system list, not a geometry
list: micrometre units, millimetre spans, span multipliers of 10³ and 10⁴. The
gate refuses them; it does not guess.

## 3. The window depends on the platform, and the figures say which

Every published figure for this gate is rendered from `docs/milestones/
F2_figures.md`, which is generated on CI and is canonical. It is canonical
because the same measurement differs between a Linux runner and this laptop —
the mechanism ceiling is `1.6519` canonically and `1.5243` here, and the
mechanism count is `347` against `350`. Neither machine is wrong. A figure
quoted without naming where it was measured is the defect, and the repository
answers it by having exactly one place figures come from.

## 4. What the gate was measured against

| control | result |
|---|---|
| `RIGID_MODE_EXACTNESS_COUNTER_DEFECT` | injected, asserted red, `4.54x` past a bisected detection edge |
| `RIGID_MODE_BOUND_COUNTER_DEFECT` | injected, asserted red |
| genuine mechanisms over the corpus's own unit × span cell | every one detected; none escaped |
| adversarial corpus | the reviewer's frames, none written by the implementer; the count is not published (DB1) |

## 5. Where the apparatus stopped — the number to read first

The reviewer measures its own corpus shapes against the checks written for
them, and reports what fraction the implementer's guards catch. Over the last
two rounds:

* fifty-first verdict: **2 of 22** unseen defect shapes caught;
* fifty-second verdict: **1 of 19** caught by any shipped assertion, and
  **0 of 19** by the check written for the shape's own class.

It went down. That is recorded here as the measured value of the verification
apparatus this step built, and it is the reason CZ0 freezes that apparatus
through F6: six consecutive rounds of findings, every one correct, none of them
in `floatfea/`, against a coverage number that fell while they were being
fixed.

The same fact is in the suite rather than only in prose. `_REPORT_SHAPES` in
`tests/test_report_carried.py` carries **ten rows asserting `must_refuse=
False`** — corpus shapes the CI-record guards demonstrably do not catch,
asserted as not caught, so that closing one later is a deliberate act and not
an accident.

## 6. The 4a list is frozen

`docs/milestones/F2a.md` § 7 holds **48 items**: every item open at the
fifty-second verdict plus the four recorded there. Nothing is added to it from
here. An item found after this commit goes into a verdict and into the
milestone's closure artifact, not into that plan.

## 7. Deferred, and why

* **R458** — the source-tree prose reading has a declared scope, and `PLAN.md`,
  `docs/conventions.md`, `docs/hsp-coupling.md`, `docs/closure/` and the
  workflow YAML sit outside it without being declared excluded. Open. Widening
  the scope is apparatus work, which CZ0 freezes.
* **R447**, restated and open.
* **R231, R244, R245, R275** — Q8 values, which cannot be written before the
  canonical render they depend on.
* **R230** — open.
* **Step R** — four F1 reader tolerances (`floatfea/io/reader.py:157,208,225`
  and `frames.py:358`) carry undeclared thresholds. They are F1 code and they
  are carried into F2's closure, where CQ1/CR0 executes the declaration row.
* The verification ladder's **V5.1** independent witness (CalculiX) is F7. Until
  it runs, every pass in this milestone means *not yet contradicted* by an
  instrument that shares assumptions with the thing it measures.

## 8. Tolerances touched at this step

All four constants in § 1 live in `floatfea/tolerances.py` with their
justification there and in `docs/milestones/F2.md`;
`tests/test_plan_matches_tolerances.py` asserts the two agree. `RIGID_MODE_
FLOOR` and `RIGID_MODE_GAP` are **retired**, with their entries marked rather
than deleted, and their counters retired with them.

**No tolerance was widened at this step.** Every value that moved, moved
because the quantity it bounds changed form, and each is recorded at its entry
with the measurement that set it.
