# F5-PREP — THE PIPELINE, PROVED END TO END BEFORE IT IS NEEDED

**Status:** SKELETON PLAN, opened 2026-09-26 under DL3. Not locked.
**Branch:** cut from `master`, deliberately — see §0.
**Schedule:** F4 and F5-prep both **17 October** (DK4, restated at DL3).

---

## 0. WHY THIS BRANCH EXISTS, AND WHY FROM `master`

**The requirement is a result, not a milestone: FloatSim loads through an FE
analysis of the main platform parts, by 31 October** (CZ0). Two things can make
that date slip, and only one of them is FE work:

1. the element, the model and the load mapping — F2, F3, F4, on the F2/F3 line;
2. **the pipeline itself** — whether an HSP run can be exported, read, and turned
   into load cases at all, on the machine that will do it, with the tagged HSP
   state that `docs/hsp-coupling.md` pins.

The second has never been run end to end. If it is broken it is broken *now*, and
finding that out on 20 October costs the date. This branch finds out this week.

**From `master` and not from F2** because the pipeline proof must not depend on
F2's unreviewed element work. If it needs F2's element to run, that is itself a
finding about the coupling, and it is better discovered as a dependency than
hidden by a branch that already has it.

---

## 1. THE TWO OPENING ITEMS (DL3)

### 1a. The F1-validated run as the pipeline proof

Take the FloatSim run F1 already validated, and carry it the whole way:

| step | what is proved | what would fail |
|---|---|---|
| export at the pinned HSP tag | the replay hook is inert when output is disabled (G1.5) | a tag that does not build, or an export that touches the solve path |
| the interchange file | it validates against `docs/load-interchange-v1.md` | a record the reader rejects — which is the reader working |
| the reader | every record is read, none degraded to a warning | a schema gap, which goes back to HSP and not into a fallback |
| **the `assumptions` block** | every fallback distribution in use is recorded **and surfaced in the run log** | a fallback that is silent, which is the failure mode this project is built to prevent |

**This is a proof of the PATH, not of the numbers.** No gate here asserts a force
is right; F1 already did that for this run. What is asserted is that the path
exists, that it rejects what it should, and that nothing is assumed quietly.

**And it is the one place a stale pin shows.** `floatfea/hsp_pin.py` names the
tagged HSP state. If the second worktree at that tag no longer builds, every
schedule after this date is wrong, and it is worth an hour now.

### 1b. DJ0's verification: all 16 joints are two-rotation gimbals

DJ0 states it; **DL3 puts the verification here rather than treating it as
given.** The check is against the platform definition, per joint, and it produces
one of three outcomes per joint:

* a two-rotation gimbal, with its locked axis named;
* something else, named — which goes back to Xabier, not into an idealisation;
* undetermined from the definition file — which is a gap in the file.

**Sixteen answers, reported per joint, never summarised as a count.** `CLAUDE.md`
§ Non-negotiables: an outlier hidden in a mean is what per-case reporting exists
to catch, and "15 of 16 are gimbals" is the same error in a smaller number.

F3 consumes the result: `gimbal_release(end, locked_axis)` needs the locked axis
per joint, and F2 step 7 already ships and tests that release pattern
(`floatfea/element/releases.py`).

---

## 2. WHAT THIS BRANCH MUST NOT DO

* **Not touch FloatSim's solve path.** `CLAUDE.md`: additive only, new modules and
  new entry points, and the replay hook is the single permitted touch. If the
  pipeline appears to need a physics change, that is a conversation.
* **Not invent a load distribution.** If a source arrives without strip
  resolution, the solver refuses to build a load case from it. A fallback in use
  is recorded in the `assumptions` block and surfaced in the run log, so a result
  computed under a fallback can never be mistaken for one computed under full
  data.
* **Not merge into F2 or F3.** This branch reports; whatever it finds becomes a
  plan item on the branch that owns it.

---

## 3. WHAT COMING BACK GREEN MEANS, AND WHAT IT DOES NOT

Green here means: the export runs at the tag, the file validates, the reader
accepts it, and the assumptions are visible. It does **not** mean the loads are
right, that the mapping to nodes is right, or that inertia relief closes — those
are F4's gates and this branch asserts none of them.

Saying that here rather than in the report, because a pipeline proof that reads
as a physics result is exactly the kind of wrongness this project is built to
make loud.
