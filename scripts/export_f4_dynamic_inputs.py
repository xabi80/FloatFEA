#!/usr/bin/env python
"""EX0(a): write `data/f4/dynamic_inputs.npz` and its provenance, from the six ER0 runs.

    python scripts/export_f4_dynamic_inputs.py
    python scripts/export_f4_dynamic_inputs.py --check    # regenerate and compare (EX0(c))

WHY THIS EXISTS. F4's G4.1 dynamic gate was written to solve through
`scripts/report_joint_reactions.py`, which opens the pinned HSP runs worktree and imports
`platform_rao_pilot`. (It read `ROOT.parent / "HSP-runs"` when this was written; GI3(e)
moved that to `hsp_pin.worktree("runs")`, which changes WHERE the tree is looked for and
nothing about the argument below.) Neither is tracked, and CI checks out no HSP worktree,
so 124 of the
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
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "measure"))

# R1225: both already existed and nothing in this path called either.
from floatfea import determinism, floatsim_env, hsp_pin  # noqa: E402

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


def _dist_version(pkg: str) -> str | None:
    """An installed package's version, or `None` if it is absent (R1225).

    `None` rather than a raise: this is provenance, and a missing package is a fact
    about the environment worth recording rather than a reason to refuse a write.
    """
    import importlib.metadata as md

    try:
        return md.version(pkg)
    except md.PackageNotFoundError:
        return None


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


def _is_tracked(path: Path) -> bool:
    """Is this file committed to this repository?

    `git ls-files --error-unmatch` is the question asked directly, rather than "is it
    under `data/`" or any other guess from the path: a scratch export outside the
    repository is untracked, a new destination inside it is untracked until somebody
    commits it, and the committed golden is tracked. A `git` that cannot answer -- not a
    repository, binary missing -- returns False, because refusing an export on the
    grounds that the check itself failed would stop work over a question nobody asked.
    """
    try:
        done = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "--error-unmatch", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:  # pragma: no cover - git missing
        return False
    return done.returncode == 0


def _recorded_path(path: Path) -> str:
    """How a written file names itself in its own provenance.

    Repository-relative with forward slashes when it is under the root -- which is what
    `data/f4/dynamic_inputs.npz` has always been, so the committed sidecar's field does
    not move -- and the absolute path otherwise, because a relative path computed against
    a root the file is not under is not a path to anything.
    """
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def sensitivity_note(prov_path: Path) -> str:
    """What a bit-exact refusal has to say beside the count of differing arrays.

    **WITHOUT THIS A READER GETS A NUMBER AND NO HANDLE.** R2 step 1 measured the handle
    on `case0` at `T_full = 10 s`, one variable per step: the same case is BIT-IDENTICAL
    at numpy 2.4.0 with the thread counts UNPINNED, differs at numpy 2.4.0 with them
    pinned to 1, and differs DIFFERENTLY at numpy 2.4.4 unpinned -- while the three PINNED
    cells at numpy 2.4.0 and 2.4.4 agree to every printed digit across two kernel
    settings -- but numpy 2.5.4 PINNED does not agree with them, so pinning narrows the
    version sensitivity without removing it. So two conditions move this comparison and
    neither is in the arrays being compared.

    **AND IT SAYS WHETHER THE FILE IT COMPARED AGAINST RECORDS THEM.** The committed
    sidecar predates R1225(ii)'s `environment` block, so it records neither, and that
    absence is printed rather than left for someone to discover: a comparison against a
    file whose conditions are unrecorded cannot be attributed to any of them.
    """
    here = {v: os.environ.get(v) for v in determinism.THREAD_ENV}
    recorded: object = None
    if prov_path.is_file():
        try:
            recorded = json.loads(prov_path.read_text(encoding="utf-8")).get("environment")
        except (OSError, ValueError):
            recorded = None
    says = (
        "records an `environment` block -- compare it against the two lines above"
        if recorded
        else "RECORDS NEITHER (its sidecar predates that block)"
    )
    return (
        "  THE COMPARISON IS SENSITIVE TO THE THREAD COUNT AND THE LIBRARY VERSIONS.\n"
        f"    this run   threads {here}\n"
        f"               OPENBLAS_CORETYPE {os.environ.get('OPENBLAS_CORETYPE')}\n"
        f"    the file   {says}\n"
        "    measured   bit-identical at numpy 2.4.0 with the threads UNPINNED. Six\n"
        "               arrays differ at every other configuration tried, and the\n"
        "               AMOUNTS differ too: 2.4.0 and 2.4.4 pinned agree with each\n"
        "               other, 2.4.4 unpinned does not, and 2.5.4 pinned does not.\n"
        "    FQ3        if the golden moves under these pins, STOP and report rather\n"
        "               than re-baselining."
    )


def covered_headings() -> list[float]:
    """The wave headings the pinned BEM dataset actually carries, in degrees.

    **FL2(c)'s REFUSAL NEEDED A SET NOBODY COULD PRODUCE, AND THIS IS IT.**
    `floatfea/run/pipeline.py:879`'s `refuse_uncovered_headings` has shipped complete and
    tested since R1, with its call site written as a comment at `cli.py:1279` because the
    covered set "is a fact about the PINNED HSP STATE: the datasets and their reader live
    in HSP, this repository contains neither". Both halves of that are still true. What
    changed at GJ1 is that FloatFEA now has an interpreter with `capytaine` and `xarray`
    in it, so the fact can be ASKED FOR instead of hard-coded.

    Asked of HSP's own reader rather than of the file: `read_capytaine` sorts the headings
    and converts radians to degrees, and a second interpretation of the same `.nc` here
    would be a second reader of one predicate -- the defect shape R2 step 0 paid five
    rounds for. Whatever FloatSim thinks it covers is what is covered.
    """
    import report_joint_reactions as rjr

    for path in (rjr.HSP_RUNS, rjr.STUDY):
        sys.path.insert(0, str(path))
    import floatsim
    import platform_rao_pilot as prp
    from floatsim.hydro.readers.capytaine import read_capytaine

    floatsim_env.refuse_unless_declared_worktree(floatsim.__file__, declared=rjr.HSP_RUNS)
    hdb = read_capytaine(prp._PLAT_NC)
    return [float(h) for h in np.asarray(hdb.heading_deg, dtype=np.float64)]


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
        # THE SHAPES MUST MATCH; THE MAGNITUDE IS THE GATE'S JOB (R726).
        #
        # This check used to compare the gap against `F4_G41_DECOMPOSITION_AGREEMENT`,
        # which put `floatfea/tolerances.py` on this script's import closure -- and the
        # closure is what the staleness gate now asserts. The consequence, measured: every
        # edit to any tolerance reddened the gate and demanded a 30-minute regeneration of
        # a 12 MiB golden file, for a value that cannot change a single number in it.
        #
        # A ceiling in two places is also one place too many. `resid_control` is stored
        # precisely so the CONSUMER can compare the two forms -- which
        # `test_the_two_WAYS_of_forming_the_reaction_agree` does, against the declared
        # ceiling, on the arrays that actually ship. What remains here is the structural
        # question this script alone can answer.
        if rebuilt.shape != reaction.shape:
            raise SystemExit(
                f"the per-joint decomposition has shape {rebuilt.shape} and the reaction "
                f"vector {reaction.shape} at step {n}; the bodies do not partition the "
                "state as this export assumes."
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
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="directory to write into; default data/f4, which is the committed location",
    )
    ap.add_argument(
        "--allow-regenerate",
        action="store_true",
        help="overwrite a COMMITTED dynamic-inputs file. Needs a written reason in the "
        "milestone closure artifact, per CLAUDE.md section Testing.",
    )
    ap.add_argument(
        "--covered-headings",
        action="store_true",
        help="print the BEM dataset's covered headings as JSON and exit (FL2(c))",
    )
    args = ap.parse_args(argv)

    # **GJ1's PREFLIGHT, AND IT IS THE FIRST THING THIS COMMAND DOES.** Every FloatSim
    # invocation by FloatFEA runs under the environment built from the pinned worktree's
    # own `requirements-lock.txt`. It REFUSES rather than re-execing (SR-76): a run whose
    # environment was silently corrected reads exactly like one that was right to begin
    # with, and FQ3 was adopted because an artifact's bit-exactness gate was deciding
    # whether to believe it while the interpreter underneath had moved -- numpy
    # 2.4.4 -> 2.5.4, scipy 1.17.1 -> 1.18.1, 36 of 100 arrays differing with all 64
    # INPUT arrays bit-identical.
    #
    # It is BEFORE the heading query as well as before the solve, because the query opens
    # the BEM dataset with `capytaine` and `xarray`, whose versions the same lock pins.
    lock_file = floatsim_env.lock_path()
    lock = floatsim_env.refuse_unless_locked(
        lock_file,
        # The MODE, not just the command: the preflight runs before the mode branch, and
        # a message reading "cannot export the dynamic inputs" for `--covered-headings`
        # describes an action nobody asked for. All three need the locked environment --
        # the heading query opens the `.nc` with `capytaine` and `xarray`, whose versions
        # the same lock pins -- so the refusal is right and only its noun was wrong.
        doing=(
            "read the BEM dataset's covered headings"
            if args.covered_headings
            else (
                "regenerate and compare the dynamic inputs"
                if args.check
                else "export the dynamic inputs"
            )
        ),
    )

    if args.covered_headings:
        print(json.dumps({"heading_deg": covered_headings()}))
        return 0

    out_dir = args.out if args.out is not None else OUT_DIR
    npz_path = out_dir / NPZ.name
    prov_path = out_dir / PROVENANCE.name
    periods = args.period or list(g41.T_FULL)

    cases = [export_case(p, args.dt) for p in periods]

    flat: dict[str, np.ndarray] = {}
    for i, c in enumerate(cases):
        for key, value in c.items():
            flat[f"case{i}/{key}"] = np.asarray(value)
    flat["fe_bodies"] = np.array(list(g41.FE_BODIES))
    flat["periods_full_s"] = np.array([c["period_full_s"] for c in cases], dtype=np.float64)
    flat["mass_eps"] = np.array(g41.MASS_EPS, dtype=np.float64)
    # THE SCALE TRAVELS WITH THE ARRAYS (FO1, answering R805). The provenance sidecar has
    # always carried `run.lambda`, and that was the only record -- so a reader had to find
    # a second file, and a copy that left it behind took the scale with it. `floatfea run`
    # prefers this key and falls back to the sidecar.
    #
    # R805 is why it matters: the joint reactions in `lam` are at MODEL scale and the
    # consumer multiplies by `lambda^3` on force and `lambda^4` on the locked moment. A
    # file whose scale is not recorded beside its data is a file whose loads cannot be
    # used without an assumption, and the assumption was wrong by 8x and 16x.
    flat["froude_lambda"] = np.array(g41.LAMBDA, dtype=np.float64)

    # **A COMMITTED GOLDEN IS NOT OVERWRITTEN WITHOUT SAYING SO (R2 step 1).** Without
    # this, `floatfea export <the export config>` -- whose `outputs.directory` is the
    # committed location, because that is what makes `--check` compare against the golden
    # -- silently replaces `data/f4/dynamic_inputs.npz`. `CLAUDE.md` § Testing:
    # "Regenerating a golden file to match new output, without that explanation, is the
    # same error as widening a tolerance", and FQ3 is a live escalation about this exact
    # file. The refusal names `--check`, which is what somebody who wanted to COMPARE
    # meant to type, and `--allow-regenerate`, which is what somebody who meant to
    # re-baseline has to type and then justify in a closure artifact.
    if not args.check and not args.allow_regenerate and _is_tracked(npz_path):
        print(
            f"  REFUSED: {_recorded_path(npz_path)} is COMMITTED, and this would "
            f"overwrite it.\n"
            "    to COMPARE against it, which is almost certainly what you want:\n"
            "        add --check; it writes nothing and reports every differing array\n"
            "    to RE-BASELINE it, which needs a written reason in the closure "
            "artifact:\n"
            "        add --allow-regenerate\n"
            "    `CLAUDE.md` section Testing: regenerating a golden to match new output, "
            "without\n"
            "    that explanation, is the same error as widening a tolerance."
        )
        return 1
    target = npz_path if not args.check else npz_path.with_suffix(".check.npz")
    out_dir.mkdir(parents=True, exist_ok=True)
    # `savez_compressed`'s stub takes `allow_pickle` where the arrays go, so a keyword
    # splat of named arrays -- which is the documented call -- does not type. Narrow
    # ignore rather than a cast, because the call itself is right.
    np.savez_compressed(target, **flat)  # type: ignore[arg-type]
    size_mb = target.stat().st_size / (1 << 20)
    # `_recorded_path`, NOT `relative_to(ROOT)`: the latter RAISES for a path outside the
    # repository, and `--out` -- added in this same step -- made that reachable. Measured
    # by running it rather than by reading it: a 26-minute export into a scratch directory
    # wrote the npz, raised HERE, and never reached the provenance, so `floatfea run` on
    # the result published "wave basis: NOT RECORDED" in both CSVs and in the report. The
    # arrays were fine and the record beside them did not exist, which is the worse of the
    # two failures -- and no unit test reached it, because the flag's own tests stop at the
    # argv the engine is handed.
    print(f"\n  wrote {_recorded_path(target)}  ({size_mb:.2f} MiB, {len(flat)} arrays)")

    if args.check:
        if not npz_path.exists():
            print(f"  REFUSED: {npz_path} is not committed; nothing to compare")
            return 1
        # CLOSED BEFORE THE UNLINK (FO1). These were left open, and `target.unlink()`
        # below then raised `PermissionError: [WinError 32] ... being used by another
        # process` on Windows -- so a `--check` that had just reported
        # `worst relative difference 0.000000e+00` exited on a traceback and left a
        # 12 MiB `dynamic_inputs.check.npz` in `data/f4/`. The comparison was right and
        # the gate looked broken, which is the worst of both.
        committed_npz = np.load(npz_path, allow_pickle=False)
        fresh_npz = np.load(target, allow_pickle=False)
        committed = dict(committed_npz)
        fresh = dict(fresh_npz)
        committed_npz.close()
        fresh_npz.close()
        missing = set(committed) ^ set(fresh)
        if missing:
            print(f"  REFUSED: the array sets differ: {sorted(missing)[:6]}")
            return 1
        # **A GATE, NOT A REPORT (FP2, closing C20).** This printed
        # `worst relative difference` and returned 0 whatever it printed, so it could not
        # fail a regeneration: `gap` was kept only `if gap > worst`, and `np.abs(nan)`
        # compares false against everything, so a NaN pair left `worst` at `0.0` and the
        # line read `0.000000e+00`. The exact sentence a reader trusts most was the one it
        # could not earn.
        #
        # THE RULE IS Q8's GOLDEN RULE: a regeneration either reproduces the committed file
        # or it does not. There is no tolerance here and none is wanted -- `np.array_equal`
        # on the raw arrays, and a non-finite value anywhere is a failure in its own right
        # because it cannot be compared.
        nonfinite: list[str] = []
        differing: list[str] = []
        for key in sorted(committed):
            a, b = committed[key], fresh[key]
            if a.dtype.kind in "fc" and not (np.isfinite(a).all() and np.isfinite(b).all()):
                nonfinite.append(key)
                continue
            if a.shape != b.shape or a.dtype != b.dtype or not np.array_equal(a, b):
                differing.append(key)

        if nonfinite:
            print(
                f"  REFUSED: NaN or inf in {len(nonfinite)} array(s): "
                f"{nonfinite[:6]}. A non-finite value cannot be compared, so this is a "
                f"failure rather than a difference of zero -- which is what the old "
                f"`worst relative difference` printed for it."
            )
            target.unlink()
            return 1
        if differing:
            print(
                f"  REFUSED: {len(differing)} array(s) differ from the committed file: "
                f"{differing[:6]}. A regeneration either reproduces it exactly or it does "
                f"not (Q8); there is no tolerance on this comparison."
            )
            # **AND THE MESSAGE NAMES THE TWO CONDITIONS THE COMPARISON IS SENSITIVE TO,
            # AND WHETHER THE FILE IT COMPARED AGAINST RECORDS THEM.** Without this a
            # reader gets a count and no handle. R2 step 1 measured the handle: the same
            # case is BIT-IDENTICAL with the thread counts unpinned and differs at
            # `3.0e-15` on `lam` with them pinned to 1, at three different numpy/scipy
            # sets -- so the thread configuration is the variable and the library versions
            # are not. `ci.yml` says the same thing from the other side: "THE BLAS KERNEL,
            # PINNED (CF1). Thread count alone was not enough."
            #
            # The committed sidecar predates R1225(ii)'s `environment` block, so it records
            # NEITHER. That absence is printed rather than left for someone to discover:
            # a comparison against a file whose conditions are unrecorded cannot be
            # attributed, and saying so is the honest output.
            print(sensitivity_note(prov_path))
            target.unlink()
            return 1
        print(f"  {len(committed)} arrays reproduce the committed file EXACTLY")
        target.unlink()
        return 0

    npz_sha = _sha256(npz_path)
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
        # R1225. THE TOOLCHAIN THIS FILE WAS BUILT UNDER, RECORDED. It was not, and the
        # consequence was measured: `--check` was GREEN at `cfb76ff` and REFUSES at
        # `9e1092a` with 36 of 100 arrays differing, while all 64 INPUT arrays stayed
        # bit-identical and the HSP worktree stayed at `floatfea-ref-1`. A variable moved
        # between those commits and it is not in this file: `constraints-dev.txt`'s numpy
        # and scipy pins (`09d5bc9`), 2.4.0 -> 2.5.4 and 1.17.1 -> 1.18.1.
        #
        # **AND THE WORD "ONE" IS WHAT R2 STEP 1 CORRECTED. THERE ARE TWO.** This comment
        # read "One variable moved", and it also read "the thread count is NOT the cause --
        # it was unpinned on both sides of the boundary". The second sentence is sound
        # about THAT boundary and was then used to read a red measured with the threads
        # PINNED, which put a second variable into a cell meant to have one. Measured on
        # `case0` at `T_full = 10 s`, one variable per step:
        #
        #   numpy 2.4.0, threads UNPINNED   16 of 16 arrays exact      <- the golden
        #   numpy 2.4.0, threads pinned 1   10 exact, 6 differ
        #   numpy 2.4.4, threads pinned 1   10 exact, 6 differ, SAME magnitudes as 2.4.0
        #   numpy 2.4.4, threads UNPINNED   10 exact, 6 differ, DIFFERENT magnitudes
        #   numpy 2.5.4, threads pinned 1   10 exact, 6 differ, DIFFERENT again
        #
        # So the committed file needs numpy 2.4.0 AND an unfixed thread count, together.
        # **AND "PINNING MAKES IT VERSION-INDEPENDENT" IS TOO STRONG**: it was written on
        # the first three rows, before the last was measured. Pinning makes 2.4.0 and 2.4.4
        # agree; 2.5.4 pinned differs from both. Pinning NARROWS the version sensitivity
        # and does not remove it.
        # `ci.yml` says the other half: "THE BLAS KERNEL, PINNED (CF1). Thread count alone
        # was not enough." The full cells are in `docs/reports/R2/step-1.md` sec. A2, which
        # is regenerated by rule, rather than here, which is not (BI3).
        #
        # So a bit-exactness gate was deciding whether this artifact is believed while
        # the conditions its answer depends on appeared nowhere in the artifact. Both
        # halves come from `floatfea/determinism.py`, which already had them and which
        # nothing in this path called.
        "environment": {
            **determinism.report(),
            "openblas_coretype": os.environ.get("OPENBLAS_CORETYPE"),
            "versions": {
                pkg: _dist_version(pkg)
                for pkg in ("numpy", "scipy", "capytaine", "xarray", "pandas", "netCDF4")
            },
            "baseline_conditions": list(hsp_pin.BASELINE_CONDITIONS),
            "note": (
                "R1225: recorded, not asserted. A refusal from `--check` against a "
                "provenance whose environment differs from this one is FQ3's case -- "
                "'if the golden moves under these pins, STOP and report rather than "
                "re-baselining' -- and not a finding about FloatSim."
            ),
            # **GJ1: THE LOCKED ENVIRONMENT'S PATH AND THE LOCK'S HASH, RECORDED.** The
            # block above was R1225's answer to "the conditions appeared nowhere in the
            # artifact", and it recorded the versions WITHOUT recording what they were
            # supposed to be -- so a reader could see numpy 2.5.4 and had nothing to
            # compare it against. This carries the lock itself: where it is, its sha256,
            # how many pins it holds, and the one editable line SR-75 does not install.
            #
            # Recorded here AND asserted at the preflight above, which is R1225's own
            # lesson applied to its own repair: recording without asserting is how the
            # drift got in, and asserting without recording leaves a reader unable to see
            # what was asserted.
            "locked": floatsim_env.record(
                lock_file=lock_file,
                lock=lock,
                floatsim_file=sys.modules["floatsim"].__file__,
            ),
        },
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
        # **THE PATH WRITTEN HERE IS THE PATH WRITTEN TO (R2 step 1).** This read
        # `"data/f4/dynamic_inputs.npz"`, a literal, which was true for as long as that
        # was the only place this script could write. `--out` made it configurable in
        # this same step and would have left every export outside `data/f4` carrying a
        # sidecar naming a file it is not beside -- a record saying something other than
        # what happened, which is FR1's second head in the provenance itself. Relative to
        # the repository root where it is under it, absolute where it is not, so the
        # committed file's own field is unchanged.
        "npz": {"path": _recorded_path(npz_path), "sha256": npz_sha},
    }
    prov_path.write_text(json.dumps(prov, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"  wrote {prov_path}  sha256 {npz_sha[:16]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
