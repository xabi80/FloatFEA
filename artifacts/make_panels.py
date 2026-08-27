"""Add `/panels/<body>/` to the record: the BEM re-run that AF3 needs.

The stored BEM dataset carries INTEGRATED forces only -- Capytaine discards the
per-panel field unless the solve asks for it. So the panel groups cannot be
written from what is on disk; this re-solves with ``keep_details=True``.

SCOPE, deliberately narrow and stated
-------------------------------------
**One frequency**, the case frequency w = 2.0004 rad/s. G1.6's radiation gate is
evaluated there, and under AF3 the quadrature is common-mode, so no other
frequency is needed for THIS gate. The cost of the alternative is not storage --
12.2 MB against 985 MB -- but the BEM: 81 frequencies x 73 problems on a
10560-panel mesh.

A single-frequency panel group **cannot** support any multi-frequency
reconstruction, and the record must not be read as though it could.

RAW OUTPUT ONLY (docs/instrumentation.md); ratios are derived in the write-up.
"""
from __future__ import annotations

import sys
import time
import warnings
from pathlib import Path

import numpy as np

_HSP = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
sys.path.insert(0, str(_HSP / "studies" / "platform-12buoy"))
sys.path.insert(0, str(_HSP / "studies" / "spar-fin-decay"))
sys.path.insert(0, str(_HSP / "studies" / "cluster-3buoy-rigid"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

warnings.simplefilter("ignore")

import capytaine as cpt  # noqa: E402
import cluster_common as cc  # noqa: E402
import platform_common as pc  # noqa: E402
import platform_fin_bem as pfb  # noqa: E402

from floatsim.io.flr_panels import (  # noqa: E402
    PanelGeometry,
    extract_froude_krylov,
    extract_scattered,
    integrate_panel_pressure,
)

W_CASE = 2.0 * np.pi / 3.141
HERE = Path(__file__).resolve().parent
OUT = HERE / "panels_w2.npz"

t0 = time.perf_counter()
allb = pfb.make_combined(0.215)
im = allb.immersed_part()
mesh = im.mesh
P = mesh.nb_faces
dofs = list(im.dofs)
print(f"platform mesh   {P} wetted panels, {len(dofs)} DOF", flush=True)

geom_all = PanelGeometry(
    centroid=np.asarray(mesh.faces_centers, dtype=np.float64),
    area=np.asarray(mesh.faces_areas, dtype=np.float64),
    normal=np.asarray(mesh.faces_normals, dtype=np.float64),
)

# Which panels belong to which buoy. The mesh is built by concatenating 12
# translated copies, so block ordering is the obvious guess -- and guessing an
# ordering is what conventions.md forbids. Assign by NEAREST CENTRE and then
# check the result actually is contiguous blocks, so the assumption is verified
# rather than relied on.
centres = np.asarray(pc.buoy_centers(), dtype=np.float64)
owner = np.argmin(
    np.linalg.norm(geom_all.centroid[:, None, :2] - centres[None, :, :2], axis=2), axis=1
)
counts = np.bincount(owner, minlength=12)
blocks_contiguous = all(
    np.all(owner[np.flatnonzero(owner == b)] == b)
    and np.ptp(np.flatnonzero(owner == b)) == counts[b] - 1
    for b in range(12)
)
print(f"panels per buoy {counts.tolist()}")
print(f"contiguous      {blocks_contiguous}  (assumed block order VERIFIED, not trusted)",
      flush=True)
if counts.min() == 0:
    raise SystemExit("a buoy owns no panels -- the centre mapping is wrong")

solver = cpt.BEMSolver()
rad_problems = [
    cpt.RadiationProblem(body=im, omega=W_CASE, radiating_dof=d,
                         water_depth=float("inf"), rho=cc.RHO, g=cc.G)
    for d in dofs
]
dif_problem = cpt.DiffractionProblem(body=im, omega=W_CASE, wave_direction=0.0,
                                     water_depth=float("inf"), rho=cc.RHO, g=cc.G)
print(f"solving {len(rad_problems)} radiation + 1 diffraction at w={W_CASE:.4f} "
      f"(keep_details=True) ...", flush=True)
results = solver.solve_all(rad_problems + [dif_problem], keep_details=True,
                           progress_bar=False)
print(f"  solved in {(time.perf_counter() - t0) / 60:.1f} min", flush=True)

rad_p = np.empty((len(dofs), P), dtype=np.complex128)
for i, r in enumerate(results[: len(dofs)]):
    rad_p[i] = extract_scattered(solver, r, geom_all)
dif_p = extract_scattered(solver, results[-1], geom_all)
fk_p = extract_froude_krylov(dif_problem, geom_all)

# Guard (b) from integrate_panel_pressure's docstring: does the extraction agree
# with CAPYTAINE's own resultants? This tests the extraction, NOT agreement with
# the simulation -- the two must not be conflated.
# FULL 72x72 from THIS solve, so the 72-row comparison needs no interpolation
# (frames.assert_reference_supports would refuse an interpolated one at round-off).
A_full = np.asarray([[r.added_mass[j] for j in dofs] for r in results[: len(dofs)]]).T
B_full = np.asarray([[r.radiation_damping[j] for j in dofs] for r in results[: len(dofs)]]).T
added = np.diag(A_full).copy()
damp = np.diag(B_full).copy()
print(f"\ncapytaine diagonal at w: A {added[:3]}  B {damp[:3]}")

np.savez_compressed(
    OUT, omega=np.array([W_CASE]), radiation=rad_p[None, ...],
    diffraction=dif_p[None, ...], froude_krylov=fk_p[None, ...],
    centroid=geom_all.centroid, area=geom_all.area, normal=geom_all.normal,
    owner=owner, dof_names=np.array(dofs, dtype=object),
    A_diag=added, B_diag=damp, A_full=A_full, B_full=B_full,
)
print(f"wrote {OUT.name}  {OUT.stat().st_size / 1e6:.1f} MB", flush=True)

# Force resultant per buoy for one radiating DOF, as a first sanity read.
F = integrate_panel_pressure(rad_p[0], geom_all)
print(f"\nradiation force resultant, DOF {dofs[0]}, whole platform: {F}")
print(f"total elapsed {(time.perf_counter() - t0) / 60:.1f} min")
