# Coupling to HSP / FloatSim

How FloatFEA depends on FloatSim without destabilising it, and without forking
it.

---

## The requirement

FloatSim is in active use — the spar-fin decay study and whatever follows it
must keep running on a known-good simulator while export work proceeds. That is
a real constraint and it drives everything below.

## Why not a fork

A fork satisfies the requirement in the short term and fails it in the medium
term. Two FloatSims means every subsequent improvement either gets ported by
hand or silently does not exist on one side. Within a few months the fork's
physics is stale, and the stale one is the one feeding the structural tool —
member forces computed from deprecated hydrodynamics, which is the worst
available outcome for a tool whose entire purpose is to be trusted.

The concern underneath "I want to keep using the previous version" is not
actually about having two codebases. It is about having a *named, retrievable*
previous version and not having today's work break it. Those are a tag and a
discipline, not a fork.

## The scheme

**One: tag the known-good state.** This is what "the previous version" means
from now on: a permanent, retrievable, referenceable point. FloatFEA records the
tag it is pinned to, so every FE result is traceable to an exact simulator state.

`<REFERENCE_TAG>` below is a placeholder. **Ask which commit to tag — do not
assume the tip of main or the latest closed milestone.** The right point is the
state the in-flight FloatSim work is currently validated against, which may sit
on a scratch branch rather than on main. Tagging the wrong commit produces a
"stable" worktree that is not the thing actually being used, which defeats the
entire purpose of the exercise.

**Two: two worktrees, one repo.**

```
git tag -a <REFERENCE_TAG> <commit> -m "known-good state for FloatFEA pinning"
git worktree add ../HSP-stable <REFERENCE_TAG>   # production runs
# original checkout stays on main                # export development
```

Both exist on disk simultaneously. Production runs happen in `HSP-stable` and
are unaffected by anything happening on main. This is the workflow a fork was
reaching for, with none of the divergence.

**Three: export work is additive-only.** The export lands as a new module and a
new CLI entry point. It adds files. It does not add lines to the integrator, the
force model, or anything else on the solve path. The one unavoidable exception
is the replay hook, discussed below, which must be designed to be inert when
disabled.

Additive-only is not an aspiration, it is a tested property: **G1.5** requires
HSP's existing regression suite to produce bit-identical results on the export
branch and at the tag. If a single number moves, the solve path was touched.

**Four: check whether HSP needs to change at all.** Gate **G1.0** audits what
FloatSim already writes to disk. If the per-body load decomposition is already
in the existing output, that part of the `.flr` writer lives in FloatFEA as a
pure converter and HSP is untouched for it. Only the strip channels and the
replay hook are likely to require HSP changes. Do this audit before designing
anything.

## The replay protocol

Strip-resolved distributed loads are required for v1 (PLAN.md §4), and storing
them across a full sea state is prohibitive. The two-pass scheme:

**Pass one, screening.** Run FloatSim normally, writing only the body-level
channels the screening metrics need. Small. This is the run that selects
candidate snapshots.

**Pass two, replay.** Re-run with the same seed and inputs, with strip output
enabled, writing only the windows around the selected snapshots. A short window
rather than a bare instant, so a peak can be confirmed as physical rather than a
numerical spike. Tens of megabytes.

This is only sound if the replay reproduces the screening run. **G1.4** tests
exactly that: bit-identical body-level channels between the two passes, and
strip loads that integrate back to the body resultants within tolerance. That
second half matters — it is the test that catches a strip export which is
internally consistent but does not correspond to the loads the simulator
actually applied.

The replay hook is the one place export code touches the solve loop. Design it
so that with output disabled the code path is unchanged, and let G1.5 prove it.

### If replay is not deterministic

Test this in week one, before building on it. Accumulated floating-point paths,
an unseeded random draw, thread scheduling in a parallel section, or a
wall-clock dependency will all break bit-identical replay.

If it breaks, the fallback is strip output at a decimated rate across the full
history — higher storage, no second pass, no determinism requirement. It costs
disk and some time resolution on the distributed loads. Record it in the
interchange file's `assumptions` block if used, and note the decimation rate,
because a screened snapshot then lands between stored strip samples and
something has to interpolate.

Do not adopt the fallback quietly. Determinism is worth fixing on its own merits.

## Version pinning

FloatFEA pins the HSP tag it was verified against and records it in every run.
Every `.flr` record carries the HSP git SHA and run ID (**G1.3**), and a record
without provenance is rejected rather than warned about.

When HSP advances past the pinned tag, re-pinning is a deliberate act: re-run
the verification set, confirm nothing moved, note it in the milestone closure
artifact. An unexplained change in FE results after re-pinning is a finding
about FloatSim, and it is one of the more valuable things this tool will
produce.
