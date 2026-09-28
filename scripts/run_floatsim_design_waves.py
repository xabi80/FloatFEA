#!/usr/bin/env python
"""Run DQ0's design-wave cases in `../HSP-runs`, never in `../HSP-stable` (DS0, DS1).

    python scripts/run_floatsim_design_waves.py

WHY A SEPARATE WORKTREE. `../HSP-stable` is reserved for production FloatSim runs
(`floatfea/hsp_pin.py`), and this repository wrote into it once: a
`platform_bem.py run` regenerated `platform12_bem.nc` and overwrote the version
commit `e1010fe` had corrected, after which FloatSim's own restoring-PSD gate
refused the database. Nothing upstream was wrong. `../HSP-runs` is a second
worktree at the same tag, and runs happen only there.

THE HASH CHECK IS THE POINT, not a formality. The committed database carries PR8
STEP 4's hydrostatic correction, which `platform_bem.py` does not reproduce -- so
a regenerated database is silently a different physical model. This asserts the
file is byte-identical to its committed blob before anything runs, and aborts if
it is not.

WHAT IS NOT DONE HERE, and it is not an oversight:

* **`platform_bem.py run` is never invoked.** See above.
* **Heading 45 degrees is not run.** `platform_rao_pilot.run_case` constructs its
  wave with `heading_deg=0.0` hardcoded, so the second heading needs either a
  parameter in HSP's study script -- an HSP change -- or a FloatFEA-side
  integration loop that re-implements the validated adaptive-settle logic. Both
  are decisions rather than edits, so this runs the 0-degree set and says so.
* **`.flr` records are not written.** `floatfea/export/` is a stub; the converter
  is later work. What each case writes is the solve-state window the converter
  will read: time, all 102 DOF, and accelerations, through HSP's own
  `_write_case_csv`.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
import time
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

RUNS = Path(__file__).resolve().parents[2] / "HSP-runs"
STABLE = Path(__file__).resolve().parents[2] / "HSP-stable"
STUDY = RUNS / "studies" / "platform-12buoy"
DATABASE = STUDY / "platform12_bem.nc"
OUT = STUDY / "floatfea_design_waves"

LAMBDA = 50.0
"""Froude scale of the model-definition YAML. Full scale is lambda times this.

not-a-tolerance: the model's own scale factor, recorded in every record's
`assumptions` block by the converter. Nothing is compared against it.
"""

H_FULL = 24.2
"""H_max = 1.86 * Hs at the survival state Hs = 13 m (DQ0)."""

T_FULL = (10.0, 12.5, 14.0, 15.0, 16.2, 20.0)
"""DQ0's six periods: DNV's associated range sqrt(6.5 H) to sqrt(11 H) plus
shoulders."""


def _fail(message: str) -> None:
    sys.exit(f"REFUSED: {message}")


def _committed_blob(rel: str) -> str:
    out = subprocess.run(
        ["git", "-C", str(RUNS), "ls-files", "-s", rel], capture_output=True, text=True
    )
    if out.returncode != 0 or not out.stdout.strip():
        _fail(f"git does not track {rel} in {RUNS.name}")
    return out.stdout.split()[1]


def _blob_of_file(path: Path) -> str:
    out = subprocess.run(
        ["git", "-C", str(RUNS), "hash-object", str(path)], capture_output=True, text=True
    )
    if out.returncode != 0:
        _fail(f"git could not hash {path}")
    return out.stdout.strip()


def preflight() -> None:
    """Refuse to run unless the worktree and the database are what they claim."""
    if not RUNS.is_dir():
        _fail(f"{RUNS} does not exist. Create it with `git worktree add`.")
    if RUNS.resolve() == STABLE.resolve():
        _fail("the runs worktree is HSP-stable, which is read-only from here (DS0)")

    tag = subprocess.run(
        ["git", "-C", str(RUNS), "describe", "--tags"], capture_output=True, text=True
    ).stdout.strip()
    from floatfea.hsp_pin import HSP_TAG

    if tag != HSP_TAG:
        _fail(f"{RUNS.name} is at {tag!r}, not the pinned {HSP_TAG!r}")

    rel = "studies/platform-12buoy/platform12_bem.nc"
    committed, actual = _committed_blob(rel), _blob_of_file(DATABASE)
    if committed != actual:
        _fail(
            f"{rel} is NOT the committed blob.\n"
            f"  committed {committed}\n  on disk   {actual}\n"
            "The committed database carries PR8 STEP 4's hydrostatic correction, "
            "which platform_bem.py does not reproduce. A regenerated file is a "
            "different physical model and FloatSim's restoring gate will refuse "
            "it. Restore it with `git checkout --` and do not regenerate."
        )
    digest = hashlib.sha256(DATABASE.read_bytes()).hexdigest()[:16]
    print(f"worktree  {RUNS.name} at {tag}")
    print(f"database  blob {committed[:12]}, sha256 {digest} -- matches the commit")
    print(f"output    {OUT}")


def main() -> int:
    preflight()
    sys.path.insert(0, str(STUDY))
    sys.path.insert(0, str(STUDY.parent / "cluster-3buoy-rigid"))
    import platform_rao_pilot as prp
    from floatsim.driver import build_system
    from floatsim.hydro.readers.capytaine import read_capytaine

    OUT.mkdir(parents=True, exist_ok=True)
    h_model = H_FULL / LAMBDA
    periods = [t / LAMBDA**0.5 for t in T_FULL]
    print(f"\nH_full {H_FULL} m -> H_model {h_model:.4f} m")
    print(
        "T_full -> T_model: "
        + ", ".join(f"{a:g}->{b:.4f}" for a, b in zip(T_FULL, periods, strict=True))
    )
    print("heading 0 deg only -- see the module docstring for why\n", flush=True)

    deck = prp._deck_with_drag()
    hydro_dof = prp._hydro_dof(deck)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        setup = build_system(
            deck,
            bem_databases={},
            dt=0.01,
            t_max_kernel=30.0,
            solve_equilibrium=False,
            shared_hydro_database=read_capytaine(DATABASE),
            asymptote_check_override=prp._ASYMPTOTE_OVR,
            kernel_decay_floor_override=prp._KERNEL_EXEMPT,
        )
    hdb_force = read_capytaine(DATABASE)

    total = 0.0
    for t_full, t_model in zip(T_FULL, periods, strict=True):
        started = time.perf_counter()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            case = prp.run_case(
                setup,
                hdb_force,
                hydro_dof,
                height_m=h_model,
                period_s=t_model,
                ramp_s=20.0,
                cap_settle_s=600.0,
                window_periods=10.0,
                dt=0.01,
            )
        elapsed = time.perf_counter() - started
        total += elapsed
        tag = f"T{t_full:g}s_full_H{H_FULL:g}m_head0"
        path = OUT / f"case_{tag}.csv"
        prp._write_case_csv(path, case)
        wrote = path.is_file() and path.stat().st_size > 0
        print(
            f"  T_full {t_full:5.1f} s  T_model {t_model:.4f} s  "
            f"{elapsed:7.1f} s  settled={case['settled']}  "
            f"steps={case['n_steps']}  export={'yes' if wrote else 'NO'}  "
            f"{path.stat().st_size / 1024:.0f} kB",
            flush=True,
        )

    print(f"\nsix cases at heading 0: {total:.1f} s = {total / 60:.2f} min")
    print(f"twelve cases would be about {2 * total / 60:.1f} min if 45 deg costs the same")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
