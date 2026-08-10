# FloatSim → FloatFEA Load Interchange, v1

**Schema version:** `1.0`
**File extension:** `.flr` (FloatSim Load Record)
**Container:** HDF5, with metadata as a JSON document stored in the root
attribute `meta`.

---

## 1. Why this document exists first

This schema is the contract between two repositories under separate review
gating. Everything FloatFEA can ever conclude about the structure is bounded by
what crosses this boundary, so the schema is specified and locked before either
side writes code against it.

HDF5 is the container because the time histories are large — tens of channels
across a 38-DOF platform over a long simulation — and HDF5 gives typed arrays,
chunking, and compression without a bespoke binary format. Metadata rides as
JSON in an attribute so it stays human-readable with `h5dump` and diffable in
review.

## 2. The central design decision: decompose by physical origin

**A net six-component load on a rigid body is not sufficient to load a flexible
frame.** Each physical load source distributes onto the structure by a different
rule:

| Source | Distributes as | Needs |
|---|---|---|
| Gravity | body force, by mass | mass distribution |
| Inertia (d'Alembert) | body force, by mass × local acceleration | rigid-body acceleration field |
| Hydrostatic / Froude-Krylov | surface pressure, by wetted geometry | instantaneous wetted surface or per-strip resultants |
| Radiation / diffraction | surface pressure | per-strip resultants |
| Morison drag | line load along the member | per-strip force per unit length |
| Connector reactions | point load | attachment node and frame |
| Mooring tension | point load | fairlead node and line direction |

If these arrive pre-summed, FloatFEA must invent a distribution and every member
force downstream inherits the invention. So they arrive separately, each with
its point or line of application.

**v1 requirement:** connector and mooring loads at named attachment points, and
**strip-resolved** distributed loads along each member — not per-body
resultants. The rationale, and why this is affordable, is in PLAN.md §4: the
strip values already exist inside FloatSim and are being discarded, and the
storage problem is solved by the two-pass replay in §7 below rather than by
reducing resolution.

A per-body resultant fallback exists only for the case where replay determinism
cannot be achieved (see `docs/hsp-coupling.md`). If it is ever used, the
distribution assumption FloatFEA applies is recorded in the file's `assumptions`
block and surfaced in the run log, so a result produced under a fallback can
never be mistaken for one produced under strip data.

## 3. Structure

```
/meta                       (root attribute, JSON)
  schema_version            "1.0"
  floatsim_version          semver
  hsp_git_sha               full 40-char SHA, dirty flag
  run_id, created_utc
  units                     {length: m, mass: kg, time: s, force: N,
                             angle: rad}          — explicit, always
  gravity                   [gx, gy, gz]
  water_density, water_depth
  assumptions[]             free-text records of any fallback applied

/frames
  global                    origin, axis convention, z-up flag,
                            still-water-level datum
  bodies/<id>               origin relative to body reference point,
                            orientation convention named explicitly
                            (e.g. "quaternion, scalar-first, body←global")

/bodies/<id>
  name, mass
  cog[3]                    in body frame
  inertia[3,3]              about CoG, in body frame
  reference_point[3]

/time
  t[N], dt, n_samples

/kinematics/<body>
  position[N,3]             of reference point, global frame
  quaternion[N,4]           scalar-first, body←global
  velocity[N,3]
  angular_velocity[N,3]     body frame — stated, not assumed
  acceleration[N,3]
  angular_acceleration[N,3]

/loads/<body>/<source>      source ∈ {gravity, hydrostatic, froude_krylov,
                                      radiation, diffraction, morison_drag,
                                      morison_inertia}
  force[N,3], moment[N,3]
  application_point[3]      or [N,3] if it moves
  frame                     "global" | "body"

/loads/strips/<member>/<source>
  s[M]                      arc-length stations along the member
  node_a, node_b            member end identifiers, for mapping to the FE mesh
  f_per_length[K,M,3]       K = replay window samples, not full history N
  window_index[K]           index into /time, so strips locate in the history
  frame

/connectors/<id>
  bodies                    [body_a, body_b]
  attach_a[3], attach_b[3]  in respective body frames
  force[N,3], moment[N,3]
  frame

/mooring/<line>
  fairlead_body, fairlead_point[3]
  tension[N,3]
  frame

/diagnostics
  equilibrium_residual[N]   FloatSim's own per-step residual
  solver_flags[N]
```

## 4. Validation rules

The reader rejects — never warns and continues — on any of the following. Gate
**G1.2** is the test that each rejection fires with a specific message.

Unknown or future `schema_version`. Missing or partial `units` block. Any unit
inconsistent with the declared system. A frame referenced but not declared in
`/frames`. A quaternion whose norm deviates from unity beyond tolerance. NaN or
inf anywhere in any channel. An inertia tensor that is not symmetric positive
definite. A body referenced in `/loads` or `/connectors` but absent from
`/bodies`. Non-monotonic or non-uniform `t` without an explicit flag. Missing
`hsp_git_sha` or `run_id` — a record without provenance is not analysable, so it
is not accepted.

Strip data adds three more. A `window_index` that does not resolve into `/time`.
A member whose strip stations `s` are not monotonic or do not span the member
length. And the important one: **strip loads that do not integrate back to the
body resultant** for the same source and timestep, within tolerance. That last
check is what catches a strip export which is internally consistent but does not
correspond to the loads the simulator actually applied, and it is the numerical
half of gate G1.4.

## 5. Channels the screening pass requires

Listed here because they constrain the schema, per §5 of PLAN.md: the metric
list must be fixed during F1 even though screening is implemented in F5.

Per-connector force and moment; per-cluster interface resultants, which may be
derived from connector channels rather than exported separately; global base
shear and overturning moment, derivable from body loads; platform pitch and roll
from kinematics; vertical acceleration per body; mooring line tension; and
relative displacement between adjacent buoys, derivable from kinematics.

Everything on that list is either exported directly or derivable from exported
channels. If a metric is added later that is neither, the schema version
increments.

## 6. Versioning

The schema version is semantic. A patch increment adds optional groups only. A
minor increment adds required groups, and the reader supports the previous minor
behind an explicit compatibility flag. A major increment breaks the reader. The
reader never guesses at an unknown version — the failure is loud and immediate,
because the alternative is silently analysing a structure with misinterpreted
loads.

## 7. Two-pass generation

A `.flr` record is written in two passes, because full-history strip data across
a sea state runs to gigabytes while the screened snapshots that actually matter
run to tens of megabytes.

**Pass one** writes body-level channels only — kinematics, per-body load
decomposition, connectors, mooring, diagnostics. This is the record the
screening pass in F5 consumes to select candidate snapshots.

**Pass two** replays the same run deterministically with strip output enabled,
writing `/loads/strips/` for a short window around each selected snapshot. The
window rather than a bare instant exists so that a peak can be confirmed as
physical rather than a numerical spike.

The result is a single record containing full-history body-level channels and
windowed strip-level channels. `window_index` is what ties the two resolutions
together, and the reader requires every strip window to resolve into `/time`.

This is only sound if pass two reproduces pass one. Gate **G1.4** requires
bit-identical body-level channels between the passes. The protocol, and the
decimated-full-history fallback for the case where determinism cannot be
achieved, are in `docs/hsp-coupling.md`.

A record may legitimately contain no strip data at all — a screening-only
record, pass one without pass two. The reader accepts it and the solver refuses
to build load cases from it, rather than the reader accepting it silently and
the solver inventing a distribution.
