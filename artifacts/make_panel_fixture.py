"""AN2 -- a MINIATURE panel-bearing record, so the AF3 identity becomes a CI test.

G1.6 was the one gate whose evidence was a script in `artifacts/` rather than a
test. The closure artifact claims every gate fails a build when broken; G1.6 was
the sole exception, and it is the gate with the longest and subtlest history. An
exception is where rot starts.

The reconstruction identity is **size-independent**:

    F_j = -sum_p  p_p (n_p . d_j,p) A_p     must equal     w^2 A_jk + i w B_jk

so it does not need the 12-buoy platform. Two small spheres at one frequency
reproduce it exactly, run in seconds, and commit small.

Two deliberate simplifications, both stated because they narrow what the test
covers:

1. **`rotation_center` is set to each body's own origin**, so Capytaine's
   rotational DOF share the record's moment reference. On the real platform the
   two differ, and the transformation between them belongs to F4's mapping -- this
   fixture does not exercise it.
2. **One frequency.** The identity holds per-frequency; the fixture pins the
   arithmetic, not the frequency dependence.

Writes `tests/fixtures/panel_reconstruction.npz`. It is a GOLDEN FILE:
regenerating it requires a written explanation of why the numbers moved.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

import numpy as np

warnings.simplefilter("ignore")
sys.path.insert(0, r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")

import capytaine as cpt  # noqa: E402
from capytaine.meshes.predefined import mesh_sphere  # noqa: E402

from floatsim.io.flr_panels import PanelGeometry, extract_scattered  # noqa: E402

OUT = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\FLOATFEA\tests\fixtures\panel_reconstruction.npz")
OMEGA = 2.0
RHO, G = 1025.0, 9.81
CENTRES = [(0.0, 0.0, 0.0), (4.0, 0.0, 0.0)]

bodies = []
for i, c in enumerate(CENTRES):
    m = mesh_sphere(radius=1.0, center=c, resolution=(8, 8))
    b = cpt.FloatingBody(mesh=m, center_of_mass=np.array(c), name=f"body{i + 1}")
    b.rotation_center = np.asarray(c, dtype=float)   # == the moment reference
    b.add_all_rigid_body_dofs()
    bodies.append(b)
allb = bodies[0]
for b in bodies[1:]:
    allb = allb + b
im = allb.immersed_part()
mesh = im.mesh
P = mesh.nb_faces
dofs = list(im.dofs)
print(f"mesh {P} wetted panels, {len(dofs)} DOF, {len(CENTRES)} bodies")

geom = PanelGeometry(
    centroid=np.asarray(mesh.faces_centers, dtype=np.float64),
    area=np.asarray(mesh.faces_areas, dtype=np.float64),
    normal=np.asarray(mesh.faces_normals, dtype=np.float64),
)
D = np.stack([np.asarray(im.dofs[n], dtype=np.float64) for n in dofs])

solver = cpt.BEMSolver()
probs = [cpt.RadiationProblem(body=im, omega=OMEGA, radiating_dof=d,
                              water_depth=float("inf"), rho=RHO, g=G) for d in dofs]
results = solver.solve_all(probs, keep_details=True, progress_bar=False)

rad = np.empty((len(dofs), P), dtype=np.complex128)
for i, r in enumerate(results):
    rad[i] = extract_scattered(solver, r, geom)

A = np.asarray([[r.added_mass[j] for j in dofs] for r in results]).T
B = np.asarray([[r.radiation_damping[j] for j in dofs] for r in results]).T

# The identity, verified here before anything is committed: a fixture that does
# not itself satisfy the identity would make the test assert a wrong number.
w = np.einsum("pc,jpc->jp", geom.normal, D) * geom.area
R = -np.einsum("jp,kp->jk", w, rad)
T = OMEGA**2 * A + 1j * OMEGA * B
resid = np.linalg.norm(R - T) / np.linalg.norm(T)
print(f"identity residual at generation: {resid:.3e}")
if not resid < 1e-10:
    raise SystemExit(f"fixture does NOT satisfy the identity ({resid:.3e}); not written")

np.savez_compressed(
    OUT, omega=np.array([OMEGA]), radiation=rad, dof_fields=D,
    centroid=geom.centroid, area=geom.area, normal=geom.normal,
    A=A, B=B, dof_names=np.array(dofs, dtype=object),
    n_bodies=np.array([len(CENTRES)]),
)
print(f"wrote {OUT.name}  {OUT.stat().st_size / 1e3:.1f} kB")
