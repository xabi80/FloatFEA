#!/usr/bin/env python
"""EX0(b): G4.1 dynamic's two residuals and both counter-cases, recomputed from the npz.

    python scripts/f4_dynamic_residual.py            # print the window rule's inputs

**NO FLOATSIM, NO `HSP-runs`, NO SOLVE.** That is the whole point of this module and the
reason EX0 re-locked the plan: the gate it replaces ran green on one machine and errored on
124 of 126 cases in CI, because the file it reached for resolves `ROOT.parent / "HSP-runs"`.
Nothing here imports anything outside `numpy` and the standard library.

WHAT IT READS. `data/f4/dynamic_inputs.npz`, written by
`scripts/export_f4_dynamic_inputs.py`, plus that file's provenance JSON. Per case and per
FE body, over the DQ6 window:

    base     (steps, 5, 6)   `a_eff @ xi_ddot(n) - rhs(n)`, the discrete balance's own
                             non-reaction terms
    contrib  (steps, 20, 6)  each (body, joint) pair's generalized reaction on that body
    m_xddot  (steps+1, 5, 6) `M_eff @ xi_ddot`, at `n-1` and at every `n`
    accel    (steps, 5, 6)   FloatSim's per-body accelerations

THE RESIDUAL IS THE DISCRETE ONE, which is what `base` exists for:

    resid = base - sum_j contrib_j

`base` is stored because the reactions and `M a` alone give only the CONTINUOUS balance,
and R711 measured that at `2.393343e-03` on the force channel where the locked discrete
form reads `1.086249e-16` -- `2.2e+13` times larger. A ceiling recomputed from the
continuous form would be red everywhere; one fitted to it would be thirteen decades loose.

BOTH COUNTER-CASES ARE CLOSED FORMS, not re-solves:

    one joint dropped   resid + contrib_p, so the SIGNAL is exactly |contrib_p|
    M scaled by 1+eps   resid + (1-alpha_m) eps M xi_ddot(n) + alpha_m eps M xi_ddot(n-1)

The second follows from `m_scaled = (1 + eps) * m_eff` scaling the whole matrix, and from
the injection reaching both `a_eff xi_ddot(n)` and the `alpha_m M xi_ddot(n-1)` inside
`rhs`. R719 and R720: a counter's response is the DIFFERENCE from the clean residual. Both
counters once reported `max_t |resid_injected|`, which includes the clean floor, so a
member contributing nothing reported its body's own clean value and read as a response.

ABSENCE AND STALENESS ARE REFUSALS, NEVER SKIPS (EX0(b)). `load()` raises `InputsMissing`.
A skipped gate reports green, which is the one outcome that must not be reachable from a
missing file.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

ROOT = Path(__file__).resolve().parents[1]
NPZ = ROOT / "data" / "f4" / "dynamic_inputs.npz"
PROVENANCE = ROOT / "data" / "f4" / "dynamic_inputs.provenance.json"

CHANNELS = ("force", "moment")
"""EV1's two, gated separately and never combined."""

_SLICE = {"force": slice(0, 3), "moment": slice(3, 6)}

_ARRAYS = (
    "times",
    "base",
    "contrib",
    "m_xddot",
    "accel",
    "resid_control",
    "body_mass",
    "body_J_G",
)


class InputsMissing(RuntimeError):
    """The committed inputs are absent, unreadable, or do not match their provenance.

    A distinct type so a gate can assert the REFUSAL rather than catching everything, and
    so no caller can mistake it for "nothing to measure here".
    """


@dataclass(frozen=True)
class BodyCase:
    """One FE body in one case: the two residuals and the two denominators."""

    body: str
    period_full_s: float
    force_rel: float
    moment_rel: float
    den_force: float
    den_moment: float


@dataclass(frozen=True)
class Inputs:
    """Every case's arrays, with the bodies and the pair labels that index them."""

    fe_bodies: tuple[str, ...]
    periods_full_s: tuple[float, ...]
    mass_eps: float
    cases: tuple[dict[str, NDArray[np.float64]], ...]
    pair_labels: tuple[tuple[str, ...], ...]
    pair_body: tuple[NDArray[np.int64], ...]
    alpha_m: tuple[float, ...]


@dataclass(frozen=True)
class WindowRule:
    """EV1's window rule on one channel, over the WHOLE counter family.

    A dataclass and not a dict: the caller reads `lower_edge` and `eh4_rise_to`, and a
    `dict[str, object]` makes every one of those an untyped lookup -- which is how a
    ceiling comes to be compared against a string.
    """

    channel: str
    clean_worst: float
    clean_at: str
    live: int
    vacuous: int
    vacuous_keys: tuple[tuple[str, str, float], ...]
    weakest: float
    weakest_at: tuple[str, str, float] | None
    centre: float
    lower_edge: float
    upper_edge: float
    eh4_fall_to: float
    eh4_rise_to: float

    @property
    def satisfiable(self) -> bool:
        """Both edges at least 2x, which is what EV1 requires of a declared ceiling."""
        return self.live > 0 and self.lower_edge >= 2.0 and self.upper_edge >= 2.0


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(npz: Path = NPZ, provenance: Path = PROVENANCE) -> Inputs:
    """The committed inputs, with the sha checked. Raises `InputsMissing` otherwise.

    THE SHA IS CHECKED BEFORE ANYTHING IS READ. A stale npz beside a fresh provenance is
    the state this guards: the figures would be a correct computation on the wrong window,
    which is the one failure mode a numeric tolerance cannot see.
    """
    if not npz.exists():
        raise InputsMissing(
            f"{npz} is absent. EX0(b): the gate REFUSES rather than skipping, because a "
            "skipped gate reports green. Regenerate with "
            "`python scripts/export_f4_dynamic_inputs.py`, which needs an HSP worktree."
        )
    if not provenance.exists():
        raise InputsMissing(
            f"{provenance.name} is absent, so the npz's sha cannot be checked. An "
            "unverified input is refused: a stale file computes correctly on the wrong "
            "window, and no numeric tolerance can see that."
        )
    declared = json.loads(provenance.read_text(encoding="utf-8"))
    want = str(declared.get("npz", {}).get("sha256", ""))
    if not want:
        raise InputsMissing(f"{provenance.name} declares no npz sha256.")
    got = _sha256(npz)
    if want != got:
        raise InputsMissing(
            f"{npz.name} has sha256 {got} and its provenance declares {want}. One of the "
            "two is stale. Regenerate both with "
            "`python scripts/export_f4_dynamic_inputs.py`."
        )

    raw = np.load(npz, allow_pickle=False)
    fe_bodies = tuple(str(x) for x in raw["fe_bodies"])
    periods = tuple(float(x) for x in raw["periods_full_s"])
    cases: list[dict[str, NDArray[np.float64]]] = []
    labels: list[tuple[str, ...]] = []
    bodies: list[NDArray[np.int64]] = []
    alphas: list[float] = []
    for i in range(len(periods)):
        cases.append({k: np.asarray(raw[f"case{i}/{k}"], dtype=np.float64) for k in _ARRAYS})
        labels.append(tuple(str(x) for x in raw[f"case{i}/pair_label"]))
        bodies.append(np.asarray(raw[f"case{i}/pair_body"], dtype=np.int64))
        alphas.append(float(raw[f"case{i}/alpha_m"]))
    return Inputs(
        fe_bodies=fe_bodies,
        periods_full_s=periods,
        mass_eps=float(raw["mass_eps"]),
        cases=tuple(cases),
        pair_labels=tuple(labels),
        pair_body=tuple(bodies),
        alpha_m=tuple(alphas),
    )


def decomposition_gap(inp: Inputs, i: int) -> float:
    """How far `base - sum_p contrib_p` sits from the directly-formed residual.

    **THIS IS NOT A REDUNDANT CHECK, AND THE FORCE CHANNEL IS WHY.** The export stores
    `resid_control`, the residual formed with the reaction as ONE matvec `g_mid.T @ lam`.
    This module forms it as `base - sum_p contrib_p`. Equal in exact arithmetic, not in
    floating point -- and the force residual closes to about `1e-16` RELATIVE, so the
    summation order is not a rounding detail there, it is comparable to the whole quantity.

    Measured across the two implementations the force clean worst moved from
    `1.8556070086831165e-16` at hub2/T20 to `2.112671361106528e-16` at platform/T20, a
    factor of `1.139` and a different body, while the moment channel agreed to `1.371e-11`
    relative. Normalised by each body-case's own denominator, so the figure is on the same
    scale as the ceilings it bears on.
    """
    resid = _residual(inp, i)
    control = inp.cases[i]["resid_control"]
    den = _denominators(inp, i)
    worst = 0.0
    for channel in CHANNELS:
        sl = _SLICE[channel]
        diff = np.linalg.norm(resid[:, :, sl] - control[:, :, sl], axis=2).max(axis=0)
        for k in range(len(inp.fe_bodies)):
            scale = float(den[channel][k])
            if scale > 0.0:
                worst = max(worst, float(diff[k]) / scale)
    return worst


def _residual(inp: Inputs, i: int) -> NDArray[np.float64]:
    """`base - sum_j contrib_j`, per step and per FE body. The locked discrete form."""
    resid = np.array(inp.cases[i]["base"], dtype=np.float64)
    contrib = inp.cases[i]["contrib"]
    for p, k in enumerate(inp.pair_body[i]):
        resid[:, int(k), :] -= contrib[:, p, :]
    return resid


def _denominators(inp: Inputs, i: int) -> dict[str, NDArray[np.float64]]:
    """`max_t Sum_j |F_j|` and `max_t Sum_j (|r_j x F_j| + |M_j|)`, per FE body.

    SUMS OF MAGNITUDES, which is the property the superseded single-scalar form lacked: a
    window in which the reactions nearly balance has a small `|Sum_j F_j|` and an ordinary
    `Sum_j |F_j|`, so dividing by the first manufactures a large relative residual out of
    a quiet case.
    """
    contrib = inp.cases[i]["contrib"]
    steps = contrib.shape[0]
    out: dict[str, NDArray[np.float64]] = {}
    for channel in CHANNELS:
        per_step = np.zeros((steps, len(inp.fe_bodies)), dtype=np.float64)
        mags = np.linalg.norm(contrib[:, :, _SLICE[channel]], axis=2)
        for p, k in enumerate(inp.pair_body[i]):
            per_step[:, int(k)] += mags[:, p]
        out[channel] = per_step.max(axis=0)
    return out


def body_cases(inp: Inputs) -> list[BodyCase]:
    """The clean figures: one row per FE body per case, never averaged (`CLAUDE.md`)."""
    rows: list[BodyCase] = []
    for i, period in enumerate(inp.periods_full_s):
        resid = _residual(inp, i)
        den = _denominators(inp, i)
        for k, name in enumerate(inp.fe_bodies):
            num_f = float(np.linalg.norm(resid[:, k, 0:3], axis=1).max())
            num_m = float(np.linalg.norm(resid[:, k, 3:6], axis=1).max())
            df, dm = float(den["force"][k]), float(den["moment"][k])
            rows.append(
                BodyCase(
                    body=name,
                    period_full_s=period,
                    force_rel=num_f / df if df > 0.0 else math.nan,
                    moment_rel=num_m / dm if dm > 0.0 else math.nan,
                    den_force=df,
                    den_moment=dm,
                )
            )
    return rows


def joint_drop_signals(inp: Inputs, channel: str) -> dict[tuple[str, float], float]:
    """`|contrib_p|` over the window, normalised by the pair's own body's denominator.

    R719: THE SIGNAL, NOT THE ABSOLUTE RESIDUAL. Dropping one joint changes the residual
    by exactly that joint's own contribution, so `dropped - clean` IS `contrib_p` -- the
    quantity an earlier threshold computed and used as a FILTER where it belonged as the
    response.
    """
    out: dict[tuple[str, float], float] = {}
    for i, period in enumerate(inp.periods_full_s):
        den = _denominators(inp, i)[channel]
        contrib = inp.cases[i]["contrib"]
        mags = np.linalg.norm(contrib[:, :, _SLICE[channel]], axis=2).max(axis=0)
        for p, label in enumerate(inp.pair_labels[i]):
            scale = float(den[int(inp.pair_body[i][p])])
            if scale > 0.0:
                out[(label, period)] = float(mags[p]) / scale
    return out


def mass_scale_signals(inp: Inputs, channel: str) -> dict[tuple[str, float], float]:
    """EV1's second injection: `M` scaled by `1 + eps`, as a closed form.

    `(1 - alpha_m) eps M xi_ddot(n) + alpha_m eps M xi_ddot(n-1)`, because the injection
    reaches `a_eff xi_ddot(n)` and the `alpha_m M xi_ddot(n-1)` inside `rhs`. A wrong `M`
    is wrong everywhere the residual reads it, not in one place.
    """
    out: dict[tuple[str, float], float] = {}
    eps = inp.mass_eps
    for i, period in enumerate(inp.periods_full_s):
        den = _denominators(inp, i)[channel]
        mx = inp.cases[i]["m_xddot"]
        am = inp.alpha_m[i]
        delta = (1.0 - am) * eps * mx[1:, :, :] + am * eps * mx[:-1, :, :]
        mags = np.linalg.norm(delta[:, :, _SLICE[channel]], axis=2).max(axis=0)
        for k, name in enumerate(inp.fe_bodies):
            scale = float(den[k])
            if scale > 0.0:
                out[(name, period)] = float(mags[k]) / scale
    return out


def drop_one_pair_gaps(inp: Inputs) -> dict[tuple[str, float], float]:
    """Each pair's own contribution, at its WORSE channel, normalised. 120 members.

    This is the counter-case for `decomposition_gap`. Dropping one pair from
    `base - sum_p contrib_p` changes it by exactly that pair's contribution, so the induced
    gap IS the joint-drop signal and no separate injection is needed.

    It lives here rather than in the gate because the ceiling's own reduction lives here: a
    counter computed beside its ceiling cannot drift from it, and a gate reaching into
    `_denominators` to recompute the normalisation is how the two come to disagree.
    """
    out: dict[tuple[str, float], float] = {}
    for i, period in enumerate(inp.periods_full_s):
        den = _denominators(inp, i)
        contrib = inp.cases[i]["contrib"]
        for p, label in enumerate(inp.pair_labels[i]):
            k = int(inp.pair_body[i][p])
            gaps = [
                float(np.linalg.norm(contrib[:, p, _SLICE[c]], axis=1).max()) / float(den[c][k])
                for c in CHANNELS
                if float(den[c][k]) > 0.0
            ]
            if gaps:
                out[(label, period)] = max(gaps)
    return out


def clean_worst(inp: Inputs, channel: str) -> tuple[float, str]:
    """The GLOBAL clean worst over all body-cases, and where it is.

    R719: GLOBAL, not per case. A per-case maximum is whichever body happens to carry that
    case, so a test excluding against it can compare a body's clean value with itself --
    which admitted a vacuous pair at `T_full = 10`, clearing by `1.000000049477`.
    """
    rows = body_cases(inp)
    return max(
        (getattr(r, f"{channel}_rel"), f"{r.body}/T{r.period_full_s:g}")
        for r in rows
        if not math.isnan(getattr(r, f"{channel}_rel"))
    )


def family(inp: Inputs, channel: str) -> dict[tuple[str, str, float], float]:
    """EV1's WHOLE counter family on one channel: both injections, keyed by kind.

    R722: THE WINDOW RULE IS TAKEN OVER BOTH INJECTIONS. The force ceiling, its counter
    and its EH4 bound were each declared over the joint-drop family alone, and the mass
    injection binds five decades below it -- `3.385828902450096e-08` against
    `0.14137099995337896`. The declared `0.1` counter sat `2.95e+06` times ABOVE a defect
    the same gate asserts it must fail, and the published EH4 rise bound was out by
    `4.17537e+06x` in the one direction EH4 exists to force.
    """
    out: dict[tuple[str, str, float], float] = {}
    for (label, period), value in joint_drop_signals(inp, channel).items():
        out[("drop", label, period)] = value
    for (label, period), value in mass_scale_signals(inp, channel).items():
        out[("mass", label, period)] = value
    return out


def window_rule(inp: Inputs, channel: str) -> WindowRule:
    """EV1's window rule over the WHOLE family: the centre, the edges, the vacuous set."""
    worst, where = clean_worst(inp, channel)
    fam = family(inp, channel)
    live = {k: v for k, v in fam.items() if v > worst}
    vacuous = {k: v for k, v in fam.items() if v <= worst}
    if not live:
        return WindowRule(
            channel=channel,
            clean_worst=worst,
            clean_at=where,
            live=0,
            vacuous=len(vacuous),
            vacuous_keys=tuple(sorted(vacuous)),
            weakest=math.nan,
            weakest_at=None,
            centre=math.nan,
            lower_edge=math.nan,
            upper_edge=math.nan,
            eh4_fall_to=math.nan,
            eh4_rise_to=math.nan,
        )
    weakest = min(live.values())
    at = min(live, key=lambda k: live[k])
    centre = math.sqrt(worst * weakest)
    return WindowRule(
        channel=channel,
        clean_worst=worst,
        clean_at=where,
        live=len(live),
        vacuous=len(vacuous),
        vacuous_keys=tuple(sorted(vacuous)),
        weakest=weakest,
        weakest_at=at,
        centre=centre,
        lower_edge=centre / worst,
        upper_edge=weakest / centre,
        eh4_fall_to=2.0 * worst,
        eh4_rise_to=weakest / 2.0,
    )


def main() -> int:
    inp = load()
    print(f"  {len(inp.fe_bodies)} FE bodies x {len(inp.periods_full_s)} cases")
    for channel in CHANNELS:
        r = window_rule(inp, channel)
        print()
        print(f"  --- {channel} ---")
        print(f"  clean worst : {r.clean_worst!r}  at {r.clean_at}")
        print(f"  family      : {r.live} live, {r.vacuous} vacuous")
        if r.live:
            print(f"  weakest     : {r.weakest!r}  at {r.weakest_at}")
            print(f"  centre      : {r.centre:.6e}")
            print(f"  edges       : {r.lower_edge:.6g}x / {r.upper_edge:.6g}x")
            print(f"  both edges >= 2x: {r.satisfiable}")
            print(f"  EH4 fall to {r.eh4_fall_to:.6e}, rise to {r.eh4_rise_to:.6e}")
        for key in r.vacuous_keys:
            print(f"      vacuous {key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
