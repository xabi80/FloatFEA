"""Save Capytaine's own per-panel DOF displacement fields. No BEM solve.

The generalized force for DOF j is  F_j = -sum_p  p_p (n_p . d_j,p) A_p, where
d_j is the DOF's displacement field. Capytaine defines that field itself, so
using its arrays avoids assuming a rotation centre -- and the rotational DOF here
are built about `rotation_center`, which is NOT the body reference point that
conventions.md makes the moment reference. Reconstructing the moment arm by hand
would be assuming exactly the thing conventions.md forbids assuming.
"""
from __future__ import annotations
import sys, warnings, time
from pathlib import Path
import numpy as np
_H = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
for sub in ("platform-12buoy", "spar-fin-decay", "cluster-3buoy-rigid"):
    sys.path.insert(0, str(_H/"studies"/sub))
warnings.simplefilter("ignore")
import platform_fin_bem as pfb

t0 = time.perf_counter()
im = pfb.make_combined(0.215).immersed_part()
names = list(im.dofs)
D = np.stack([np.asarray(im.dofs[n], dtype=np.float64) for n in names])
print(f"dof fields {D.shape}   ({len(names)} DOF, {D.shape[1]} panels, 3 comp)")
out = Path(__file__).resolve().parent / "dof_fields.npz"
np.savez_compressed(out, dofs=D, names=np.array(names, dtype=object))
print(f"wrote {out.name}  {out.stat().st_size/1e6:.1f} MB   in {(time.perf_counter()-t0)/60:.1f} min")
