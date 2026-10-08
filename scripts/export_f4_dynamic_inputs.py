#!/usr/bin/env python
"""EX0(a): write `data/f4/dynamic_inputs.npz` and its provenance, from the six ER0 runs.

    python scripts/export_f4_dynamic_inputs.py
    python scripts/export_f4_dynamic_inputs.py --check    # regenerate and compare (EX0(c))

WHY THIS EXISTS. F4's G4.1 dynamic gate was written to solve through
`scripts/report_joint_reactions.py`, which reads `ROOT.parent / "HSP-runs"` and imports
`platform_rao_pilot`. Neither is tracked, and CI checks out no HSP worktree, so 124 of the
gate's 126 cases errored in CI while all 126 passed on the machine that wrote them. That is
R670 for the second time in `tests/verification/rung4/`. EX0 re-locked the plan on committed
inputs: this script needs HSP and runs on demand; the gate needs only the file it writes.

WHAT IS STORED, AND THE TWO ARRAYS BEYOND EX0(a)'s LIST -- stated rather than slipped in.

EX0(a) names the per-joint reaction histories, FloatSim's per-body accelerations, the window
times, and the per-body `M` and `J_G`. Those four are here. **They are not sufficient to
recompute the residual the plan locks**, and R711 is the measurement that says so: from the
reactions and `M a` alone one can form only the CONTINUOUS balance, which reads
`2.393343e-03` on the force channel where the locked DISCRETE form reads `1.086249e-16` --
`2.2e+13` times larger. A ceiling of `5.0e-9` recomputed from the continuous form would be
red on every body and every case, and a ceiling fitted to it would be thirteen decades loose
on a channel that closes to round-off.

So two more arrays are stored, and they are the discrete balance's own non-reaction terms:

    base     = a_eff @ xi_ddot(n) - rhs(n)        per FE body, per window step
    m_xddot  = M_eff @ xi_ddot(n)                 per FE body, per window step, plus n-1

`base` is what the reaction is subtracted FROM, so `resid = base - sum_j contrib_j` is the
locked form exactly. `m_xddot` is what EV1's mass injection perturbs, and storing it makes
that counter-case a closed form rather than a re-solve:

    resid_mass - resid = (1 - alpha_m) * eps * M xi_ddot(n) + alpha_m * eps * M xi_ddot(n-1)

because `m_scaled = (1 + eps) * m_eff` scales the whole matrix (`g41_dynamic.py:295`), and
the injection reaches `a_eff xi_ddot(n)` and the `alpha_m M xi_ddot(n-1)` inside `rhs`.

**This is a departure from the letter of EX0(a) and it goes back to Xabier.** It is not a
choice about what the gate measures -- the quantity is unchanged and the ceilings are
unchanged -- it is the minimum state needed to measure it without a solve.

WHAT IS NOT STORED, and why nothing is lost. `C`, `mu`, the external force and the added-mass
contribution are identically zero on the five FE bodies (EK0(a)), so they survive only inside
`base`, where they belong. The Jacobian is not stored: `contrib` is taken from the SAME
`g_mid` the numerator used, which is the invariant R711 turned on, and a stored Jacobian
would let a later caller rebuild it at the wrong argument.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "measure"))

# `CLAUDE.md`: every numerical tolerance in this repository lives in
# `floatfea/tolerances.py`. No local literals -- this check shipped with `1.0e-12` written
# into it, which is the rule's own prohibition, found while writing the gate that reads the
# same quantity out of the npz.
from floatfea.tolerances import F4_G41_DECOMPOSITION_AGREEMENT  # noqa: E402

OUT_DIR = ROOT / "data" / "f4"
NPZ = OUT_DIR / "dynamic_inputs.npz"
PROVENANCE = OUT_DIR / "dynamic_inputs.provenance.json"

ER0_OVERRIDE: dict[str, Any] = {
    "mass": 20.0,
    "inertia": {"Ixx": 20.0, "Iyy": 20.0, "Izz": 40.0},
}
"""ER0's platform basis, at model scale, as `data/platform/platform12_deck.yaml` declares it.

EX0(e) / R712: passed EXPLICITLY. It used to be written onto
`report_joint_reactions.PLATFORM_MASS_OVERRIDE`, a module global, by the gate's own fixture
-- so what the gate measured depended on whether that fixture had run.
"""


def _blob_sha(path: Path) -> str:
    """`git hash-object` for one file, so the provenance names the exact source."""
    out = subprocess.run(
        ["git", "hash-object", str(path)], cwd=ROOT, capture_output=True, text=True, check=True
    )
    return out.stdout.strip()


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _import_closure_shas() -> dict[str, str]:
    """R726: the blob sha of every FLOATFEA file this export's import closure reaches.

    **THE DEFENCE THIS REPLACES COVERED TWO FILES AND THE NPZ IS A FUNCTION OF AT LEAST
    FIVE.** The reviewer constructed the stale-but-accepted state: editing
    `scripts/report_joint_reactions.py` to change `heading_deg` from `0.0` to `90.0` --
    the one variable EX3/R724 declares untested -- left the gate at `112 passed` and the
    staleness test green, because the provenance named only
    `export_f4_dynamic_inputs.py` and `measure/g41_dynamic.py`. It also showed
    `floatfea/io/integrator.py` (which produces the stored `alpha_m`) and
    `data/platform/platform12_deck.yaml` passing the same way.

    Taken from `sys.modules` AFTER the solve, so it is the closure the run actually
    reached rather than a list anyone maintains. HSP's own files are excluded and the
    HSP tag covers them: they are not ours to sha, and `floatfea-ref-1` is the pin.
    """
    import sys as _sys

    out: dict[str, str] = {}
    for mod in list(_sys.modules.values()):
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        path = Path(f).resolve()
        try:
            rel = path.relative_to(ROOT)
        except ValueError:
            continue  # outside this repository -- HSP, site-packages, the stdlib
        if rel.parts and rel.parts[0] in ("floatfea", "scripts", "data"):
            out[rel.as_posix()] = _blob_sha(path)
    # The deck is data, not a module, so it is added by name.
    deck = ROOT / "data" / "platform" / "platform12_deck.yaml"
    if deck.exists():
        out[deck.relative_to(ROOT).as_posix()] = _blob_sha(deck)
    return dict(sorted(out.items()))


def _hsp_tag() -> str:
    """The HSP state this export was taken at, per `docs/hsp-coupling.md`.

    RESOLVED FROM THE IMPORTED PACKAGE, not from a guessed directory name. The first
    version looked in `ROOT.parent / "HSP"`, which does not exist in this tree, and wrote
    `UNKNOWN -- no HSP checkout beside this one` into the provenance -- a field EX0(a)
    requires, filled with a sentence about the field being unavailable. FloatSim actually
    resolves from `../HSP-runs`, and there are three HSP checkouts beside this one at two
    different states, so guessing is exactly the wrong method:

        ../HSP-runs     floatfea-ref-1
        ../HSP-stable   floatfea-ref-1
        ../HSP_code     floatfea-ref-1-99-gc2fe24f-dirty

    Asking the module where it came from cannot name the wrong one.
    """
    import floatsim

    repo = Path(floatsim.__file__).resolve().parent.parent
    for args in (["describe", "--tags", "--always", "--dirty"], ["rev-parse", "HEAD"]):
        out = subprocess.run(
            ["git", "-C", str(repo), *args], capture_output=True, text=True, check=False
        )
        if out.returncode == 0 and out.stdout.strip():
            return f"{out.stdout.strip()}  ({repo.name})"
    return f"UNKNOWN -- {repo} is not a git checkout"


def _inertia_matrix(inertia: Any) -> np.ndarray:
    """The deck's six components as a symmetric 3x3, about the body `reference_point`.

    `docs/conventions.md:171`: the record declares the tensor ABOUT THE REFERENCE POINT,
    which is the point this export's moments are taken about. The off-diagonals are read
    rather than assumed zero -- they are zero on this platform, and a deck that changed
    would otherwise be silently symmetrised.
    """
    ixx, iyy, izz = float(inertia.Ixx), float(inertia.Iyy), float(inertia.Izz)
    ixy, ixz, iyz = float(inertia.Ixy), float(inertia.Ixz), float(inertia.Iyz)
    return np.array([[ixx, -ixy, -ixz], [-ixy, iyy, -iyz], [-ixz, -iyz, izz]], dtype=np.float64)


def export_case(period_full_s: float, dt: float) -> dict[str, Any]:
    """One case's window, as the arrays the gate recomputes from."""
    import g41_dynamic as g41
    import report_joint_reactions as rjr
    from report_joint_reactions import solve_one

    from floatfea.io.integrator import generalized_alpha_coefficients

    rjr.PLATFORM_MASS_OVERRIDE = dict(ER0_OVERRIDE)

    period_model = period_full_s / g41.LAMBDA**0.5
    duration = g41.window_duration(period_model)
    print(f"\n## T_full = {period_full_s:g} s  (model {period_model:.4f} s)", flush=True)
    res, setup, deck, ext = solve_one(period_model, duration, dt)
    if res.lam is None:
        raise SystemExit("the solve returned no multipliers; `constraints` never reached it.")

    names = [b.name for b in deck.bodies]
    fe = [n for n in g41.FE_BODIES]
    fe_index = {n: names.index(n) for n in fe}
    n_bodies = len(names)

    alpha_m, alpha_f, beta, _gamma = generalized_alpha_coefficients(g41.RHO_INF)
    m_eff = setup.lhs.M_plus_Ainf
    c_mat = setup.lhs.C
    h = float(res.t[1] - res.t[0])
    a_eff = (1.0 - alpha_m) * m_eff + (1.0 - alpha_f) * (h**2) * beta * c_mat

    # `mu`, rebuilt by pushing the solver's own velocity history through a fresh buffer --
    # `g41_dynamic.py`'s construction, and the integrator's own startup convention.
    from floatsim.hydro.retardation import RadiationConvolution

    buffer = RadiationConvolution(setup.kernel)
    buffer.push(res.xi_dot[0])
    mu = np.zeros_like(res.xi_dot)
    for i in range(1, res.xi.shape[0]):
        buffer.push(res.xi_dot[i])
        mu[i] = buffer.evaluate()

    def force_at(i: int) -> np.ndarray:
        """`F_np1` as `g41_dynamic.py:272-280` builds it: time term at `t_i`, state LAGGED.

        Mirrored rather than simplified. `ext` and the state force are identically zero on
        the five FE bodies (EK0(a)), so a wrong `force_at` would be invisible here and
        wrong the moment a body becomes wetted -- which is how R711 survived reading.
        """
        f = np.asarray(ext(float(res.t[i])), dtype=np.float64)
        if getattr(setup, "state_force", None) is not None and i > 0:
            f = f + np.asarray(
                setup.state_force(float(res.t[i - 1]), res.xi[i - 1], res.xi_dot[i - 1]),
                dtype=np.float64,
            )
        return f

    win = g41.window_slice(np.asarray(res.t), period_model)
    steps = [n for n in range(*win.indices(len(res.t))) if n != 0]
    if len(steps) < 2:
        raise SystemExit(f"the DQ6 window holds {len(steps)} usable steps; the run is short.")

    # THE 20 (body, joint) PAIRS COME FROM THE CONSTRAINT TOPOLOGY, NOT FROM A NUMERIC
    # TEST. A joint acts on a body if the deck says it connects them, which is a fact about
    # the model and not about one timestep. Discovering them instead by `max |contrib| > 0`
    # at the first window step would drop any pair whose six components all happened to
    # read exactly zero there -- and the pair set is STORED and consumed by the gate, so a
    # missed pair silently narrows the counter family. That is R706, R708, R710 and R722's
    # shape, four times over: a counter declared over part of its family.
    #
    # Per hub: three buoy joints plus one platform joint. Plus the platform's four hub
    # joints. Twenty, and the count is asserted below rather than assumed.
    pairs: list[tuple[str, int]] = []
    for j, joint in enumerate(deck.joints):
        for side in (joint.body_a, joint.body_b):
            if side in fe_index:
                pairs.append((str(side), j))
    pairs.sort(key=lambda pair: (fe.index(pair[0]), pair[1]))
    base = np.zeros((len(steps), len(fe), 6), dtype=np.float64)
    m_xddot = np.zeros((len(steps) + 1, len(fe), 6), dtype=np.float64)
    accel = np.zeros((len(steps), len(fe), 6), dtype=np.float64)
    # A CONTROL ARRAY, AND IT IS NOT REDUNDANCE. `resid_control` is the residual formed the
    # way `g41_dynamic.py` forms it -- `a_eff xi_ddot - (g_mid.T lam) - rhs`, with the
    # reaction as ONE matvec. The recompute forms it as `base - sum_p contrib_p`. The two
    # are equal in exact arithmetic and NOT in floating point, and on the force channel
    # that matters: there the residual closes to `~1e-16` RELATIVE, so a difference in
    # summation order is not a rounding detail, it is the whole quantity. Measured across
    # the two implementations the force clean worst moved from `1.8556070086831165e-16` at
    # hub2/T20 to `2.112671361106528e-16` at platform/T20 -- a factor of 1.139 and a
    # different body -- while the moment channel agreed to `1.371e-11` relative.
    #
    # So the gate asserts the recompute against this, rather than anyone arguing in prose
    # that the orders agree.
    resid_control = np.zeros((len(steps), len(fe), 6), dtype=np.float64)
    # EY0: THE RAW MULTIPLIERS, so a consumer can map them to FE NODES through the
    # reviewed `map_joint_reactions` instead of deriving a frame transform of its own.
    # `contrib` is each joint's reaction at the BODY REFERENCE POINT; a member-force
    # table needs it at the joint's own node, and the transfer between the two is a
    # frame question `docs/conventions.md` is the authority on. Storing `lam` keeps that
    # question in the one module that has already been reviewed for it.
    lam_window = np.zeros((len(steps), np.asarray(res.lam).shape[1]), dtype=np.float64)
    times = np.zeros(len(steps), dtype=np.float64)
    contrib_rows: list[np.ndarray] = []

    for row, n in enumerate(steps):
        xi_n, xi_dot_n, xi_ddot_n = res.xi[n - 1], res.xi_dot[n - 1], res.xi_ddot[n - 1]
        xi_pred = xi_n + h * xi_dot_n + (h**2) * (0.5 - beta) * xi_ddot_n
        rhs = (
            (1.0 - alpha_f) * force_at(n)
            + alpha_f * force_at(n - 1)
            - alpha_m * (m_eff @ xi_ddot_n)
            - (1.0 - alpha_f) * (c_mat @ xi_pred)
            - alpha_f * (c_mat @ xi_n)
            - mu[n - 1]
        )
        mid = 0.5 * (xi_n + res.xi[n])
        lam = np.asarray(res.lam[n], dtype=np.float64)
        g_mid = setup.constraints.jacobian(mid)
        full_base = np.asarray(a_eff @ res.xi_ddot[n] - rhs, dtype=np.float64)
        contrib = g41.per_joint_contributions(g_mid, lam, n_bodies)
        full_resid = np.asarray(full_base - (g_mid.T @ lam), dtype=np.float64)

        # A CONTROL ON THE SLICING, kept in the export because nothing downstream can see
        # it: the per-joint decomposition must reproduce `g_mid.T lam` to round-off.
        reaction = np.asarray(g_mid.T @ lam, dtype=np.float64)
        rebuilt = contrib.sum(axis=0).reshape(-1)
        scale = float(np.max(np.abs(reaction))) or 1.0
        gap = float(np.max(np.abs(rebuilt - reaction))) / scale
        if gap > F4_G41_DECOMPOSITION_AGREEMENT:
            raise SystemExit(
                f"the per-joint decomposition departs from `g_mid.T lam` by {gap:.3e} "
                f"relative at step {n}, outside {F4_G41_DECOMPOSITION_AGREEMENT!r}; the "
                "bodies do not partition the state as this export assumes."
            )

        # A CONTROL ON THE TOPOLOGY, taken once: every pair the deck names must actually
        # carry a reaction, and every nonzero reaction must belong to a named pair. The
        # first half catches a joint that connects two bodies but contributes nothing; the
        # second catches a Jacobian that reaches a body the deck does not connect.
        if row == 0:
            named = {(fe_index[nm], jj) for nm, jj in pairs}
            for name in fe:
                kk2 = fe_index[name]
                for j2 in range(contrib.shape[0]):
                    live = float(np.max(np.abs(contrib[j2, kk2]))) > 0.0
                    if live and (kk2, j2) not in named:
                        raise SystemExit(
                            f"joint {j2} acts on {name} with a nonzero reaction and the "
                            "deck does not connect them. The Jacobian reaches a body the "
                            "topology does not name."
                        )
                    if (kk2, j2) in named and not live:
                        raise SystemExit(
                            f"the deck connects joint {j2} to {name} and its reaction is "
                            "identically zero over all six components at the first window "
                            "step. A pair that carries nothing is a counter-case member "
                            "that cannot redden anything, and it must be read rather than "
                            "stored."
                        )

        times[row] = float(res.t[n])
        this = np.zeros((len(pairs), 6), dtype=np.float64)
        for i, (name, j) in enumerate(pairs):
            this[i] = contrib[j, fe_index[name]]
        contrib_rows.append(this)
        # Hoisted: one matvec per step, not one per body. `m_eff` is 102x102 and the loop
        # below ran `m_eff @ xi_ddot` five times for five slices of the same product.
        m_now = m_eff @ res.xi_ddot[n]
        m_prev = m_eff @ xi_ddot_n if row == 0 else None
        for k, name in enumerate(fe):
            kk = fe_index[name]
            base[row, k] = full_base[6 * kk : 6 * kk + 6]
            accel[row, k] = res.xi_ddot[n][6 * kk : 6 * kk + 6]
            m_xddot[row + 1, k] = m_now[6 * kk : 6 * kk + 6]
            resid_control[row, k] = full_resid[6 * kk : 6 * kk + 6]
            if m_prev is not None:
                m_xddot[0, k] = m_prev[6 * kk : 6 * kk + 6]
        lam_window[row] = lam

    if len(pairs) != 20:
        raise SystemExit(
            f"{len(pairs)} (body, joint) pairs touch the five FE bodies and twenty do: the "
            "platform's four hub joints, and each hub's one platform joint plus three buoy "
            "joints. A counter-case over part of its family brackets part of it."
        )

    body = {b.name: b for b in deck.bodies}
    return {
        "period_full_s": float(period_full_s),
        "times": times,
        "base": base,
        "contrib": np.stack(contrib_rows),
        "m_xddot": m_xddot,
        "accel": accel,
        "resid_control": resid_control,
        "lam": lam_window,
        # THE DECK'S OWN JOINT ORDER, which is the authority for the block order of
        # `lam` (`map_joint_reactions`'s docstring, and the caveat at
        # `test_f4_static_and_mapping.py:844-849`: the BUILDER's order is not checked
        # against the deck's anywhere, and that is the driver's job). Recorded here so a
        # consumer can check it rather than assume it.
        "joint_body_a": np.array([str(j.body_a) for j in deck.joints]),
        "joint_body_b": np.array([str(j.body_b) for j in deck.joints]),
        "pair_label": np.array([f"{n}/{j}" for n, j in pairs]),
        "pair_body": np.array([fe.index(n) for n, _j in pairs], dtype=np.int64),
        "body_mass": np.array([float(body[n].mass) for n in fe], dtype=np.float64),
        "body_J_G": np.stack([_inertia_matrix(body[n].inertia) for n in fe]),
        "alpha_m": float(alpha_m),
        "dt": float(h),
    }


def main(argv: list[str] | None = None) -> int:
    import g41_dynamic as g41
    import report_joint_reactions as rjr

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--period", type=float, action="append")
    ap.add_argument("--dt", type=float, default=0.01)
    ap.add_argument(
        "--check",
        action="store_true",
        help="EX0(c): regenerate and compare against the committed file, do not overwrite",
    )
    args = ap.parse_args(argv)
    periods = args.period or list(g41.T_FULL)

    cases = [export_case(p, args.dt) for p in periods]

    flat: dict[str, np.ndarray] = {}
    for i, c in enumerate(cases):
        for key, value in c.items():
            flat[f"case{i}/{key}"] = np.asarray(value)
    flat["fe_bodies"] = np.array(list(g41.FE_BODIES))
    flat["periods_full_s"] = np.array([c["period_full_s"] for c in cases], dtype=np.float64)
    flat["mass_eps"] = np.array(g41.MASS_EPS, dtype=np.float64)

    target = NPZ if not args.check else NPZ.with_suffix(".check.npz")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # `savez_compressed`'s stub takes `allow_pickle` where the arrays go, so a keyword
    # splat of named arrays -- which is the documented call -- does not type. Narrow
    # ignore rather than a cast, because the call itself is right.
    np.savez_compressed(target, **flat)  # type: ignore[arg-type]
    size_mb = target.stat().st_size / (1 << 20)
    print(f"\n  wrote {target.relative_to(ROOT)}  ({size_mb:.2f} MiB, {len(flat)} arrays)")

    if args.check:
        if not NPZ.exists():
            print(f"  REFUSED: {NPZ.relative_to(ROOT)} is not committed; nothing to compare")
            return 1
        committed = np.load(NPZ, allow_pickle=False)
        fresh = np.load(target, allow_pickle=False)
        missing = set(committed.files) ^ set(fresh.files)
        if missing:
            print(f"  REFUSED: the array sets differ: {sorted(missing)[:6]}")
            return 1
        worst, where = 0.0, ""
        for key in sorted(committed.files):
            a, b = committed[key], fresh[key]
            if a.dtype.kind not in "fc":
                if not np.array_equal(a, b):
                    print(f"  REFUSED: {key} differs and is not numeric")
                    return 1
                continue
            scale = float(np.max(np.abs(a))) or 1.0
            gap = float(np.max(np.abs(a - b))) / scale
            if gap > worst:
                worst, where = gap, key
        print(f"  worst relative difference {worst:.6e}  at {where or '(none)'}")
        target.unlink()
        return 0

    npz_sha = _sha256(NPZ)
    prov = {
        "hsp_tag": _hsp_tag(),
        "override": {"platform": ER0_OVERRIDE},
        "generating_script": {
            "path": "scripts/export_f4_dynamic_inputs.py",
            "blob_sha": _blob_sha(Path(__file__)),
        },
        "measurement_module": {
            "path": "scripts/measure/g41_dynamic.py",
            "blob_sha": _blob_sha(ROOT / "scripts" / "measure" / "g41_dynamic.py"),
        },
        # R726: every FloatFEA file the run's import closure reached, not a list of two.
        "import_closure": _import_closure_shas(),
        # R726: THE RUN PARAMETERS AS EXPLICIT FIELDS, so a consumer can assert them
        # against `docs/milestones/F4.md` rather than trust that the npz was made the way
        # the plan says. The heading is first because it is the one the reviewer moved.
        "run": {
            # READ FROM THE SOLVE'S OWN MODULE, not mirrored here (R726). A mirror is
            # the thing that diverges; `report_joint_reactions` is the one source and its
            # blob sha is in `import_closure` below, so an edit to either reddens.
            "heading_deg": float(rjr.WAVE_HEADING_DEG),
            "wave_height_model_m": float(rjr.WAVE_HEIGHT_MODEL_M),
            "wave_height_full_m": float(rjr.WAVE_HEIGHT_MODEL_M) * float(g41.LAMBDA),
            "periods_full_s": [float(p) for p in periods],
            "dt": float(args.dt),
            "rho_inf": float(g41.RHO_INF),
            "lambda": float(g41.LAMBDA),
            "ramp_s": float(g41.RAMP_S),
            "window": "DQ6: the last 5 whole periods, starting no earlier than ramp + 10",
            "mass_eps": float(g41.MASS_EPS),
        },
        "npz": {"path": "data/f4/dynamic_inputs.npz", "sha256": npz_sha},
    }
    PROVENANCE.write_text(json.dumps(prov, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"  wrote {PROVENANCE.relative_to(ROOT)}  sha256 {npz_sha[:16]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
