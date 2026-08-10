# CLAUDE.md — FloatFEA

Guidance for Claude Code working in this repository. Read `PLAN.md` before
starting any milestone work.

---

## What this repository is

A structural finite element tool for the floating platform simulated by FloatSim
(`github.com/xabi80/HSP`). It reads a versioned load interchange file, builds a
space-frame model, applies FloatSim loads with inertia relief, solves, and
produces member forces, stresses, and code utilisations. Detailed shell
sub-models are exported to CalculiX rather than solved here.

This is engineering analysis software. A wrong answer that looks right is worse
than a crash. Most of what follows exists to make wrongness loud.

## Working agreement

Work proceeds milestone by milestone under the same audit-driven gating used on
HSP: **skeleton plan → review → lock Q&A → detailed plan → review → commit →
execute → closure artifact.** Do not begin implementing a milestone whose
detailed plan has not been reviewed and locked. If execution reveals that the
locked plan was wrong, stop and say so — do not silently adapt the plan while
implementing it.

Merges are rebase-then-fast-forward-only. History stays linear.

Each milestone closes with a closure artifact in `docs/closure/F<n>.md`
recording what was built, which gates pass, what was deferred and why, and any
number that moved.

## Tolerances

**Every numerical tolerance in this repository lives in `floatfea/tolerances.py`.**
No exceptions, no local literals, no default arguments carrying a tolerance.

Do not modify that file to make a failing test pass. If a test fails, the
default hypothesis is that the code is wrong, not that the tolerance is tight.
Changing a tolerance requires a written justification in the milestone closure
artifact naming the physical or numerical reason the previous value was
incorrect. A tolerance change in the same commit as the code change it rescues
will be rejected in review.

The same rule applies to anything that functions as a tolerance under another
name: convergence thresholds, comparison epsilons, "small number" guards,
tier cutoffs in screening, and any factor introduced to make two numbers agree.

## Relationship to HSP / FloatSim

FloatSim is in active production use. It is **not forked**. FloatFEA pins a
tagged HSP state, and a second worktree at that tag serves production runs while
export development happens on main. Full scheme in `docs/hsp-coupling.md`.

Any change to HSP in service of FloatFEA is **additive only**: new modules, new
entry points, no lines added to the integrator or the force model. Gate G1.5
proves it by requiring HSP's regression suite to produce bit-identical results
on the export branch and at the tag. The replay hook is the single permitted
touch on the solve loop, and it must be inert when output is disabled.

If FloatFEA appears to need a change to FloatSim's physics, stop. That is a
conversation, not an edit.

## Non-negotiables

Never widen a tolerance, skip a test, or mark a test `xfail` to get a green
build. Report the failure instead.

Never modify FloatSim's solve path. See above.

Never invent a load distribution. Distributed loads arrive strip-resolved in
v1. If a record carries no strip data, the solver refuses to build load cases
from it — it does not fall back to an assumed distribution. If the interchange
file lacks resolution needed for some source, that is a schema problem and it
goes back to `docs/load-interchange-v1.md` and to HSP. Any fallback
distribution in use must be recorded in the file's `assumptions` block and
surfaced in the run log, so that a result computed under a fallback can never
be mistaken for one computed under full data.

Never let a validation failure degrade to a warning. The reader rejects bad
records. A structure analysed under misinterpreted loads is the failure mode
this whole project is built to prevent.

Never average a per-case diagnostic. Equilibrium residual, utilisation, and
convergence are reported per case. An outlier hidden in a mean is the specific
thing these diagnostics exist to catch.

Never introduce a fudge factor. If two results disagree, the disagreement is the
finding. Report it.

Never assume a coordinate frame, a sign convention, a rotation order, or a unit.
All four are declared in `docs/conventions.md` and carried explicitly in the
interchange file. If something is ambiguous, stop and ask rather than picking
the convention that makes the current test pass.

## Conventions

`docs/conventions.md` is locked at F0 and is authoritative for frames, signs,
units, rotation representation, and numbering. It reconciles explicitly with
FloatSim's `docs/multibody-conventions.md`; where the two differ, the
transformation is written there once and referenced everywhere else. Changing it
requires reopening the F0 gate, not an inline edit.

Internally, SI throughout: metres, kilograms, seconds, newtons, radians. No unit
conversion happens anywhere except at the I/O boundary.

## Testing

`tests/unit/` for component behaviour, `tests/verification/` for the ladder in
`docs/verification/README.md`, `tests/regression/` for golden files.

The verification ladder is ordered by dependency. A failure at a low rung makes
higher rungs uninterpretable — do not investigate a rung 5 discrepancy while a
rung 1 test is red.

Golden-file changes require a written explanation of why the numbers moved.
Regenerating a golden file to match new output, without that explanation, is
the same error as widening a tolerance.

## Style

Python, type-hinted, `numpy` and `scipy.sparse` for the numerics. Vectorise
where it is natural; do not obfuscate an element formulation to save a loop that
runs once per element. Element mathematics carries a comment naming the
reference — textbook, equation number — so the formulation can be checked
against a source rather than re-derived.

Prefer explicit and slow over clever and fast until a profiler says otherwise.
The bottleneck will be the solve, not the assembly.

## When you are stuck

Say so. Do not produce a plausible number to fill a gap. An honest "the load
mapping for this source is underdetermined by the current schema" is the most
valuable output available at that moment.
