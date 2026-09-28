"""The FloatSim state this repository is pinned to, and what it is known to carry.

`docs/hsp-coupling.md` requires FloatFEA to record the tag it is pinned to, so
that every FE result is traceable to an exact simulator state. These constants
are stamped into every run log; a result that cannot name its pin is not
traceable and should not be trusted.

Re-pinning is a deliberate act, not a version bump: re-run the verification set,
confirm nothing moved, and note it in the milestone closure artifact. An
unexplained change in FE results after re-pinning is a finding *about FloatSim*,
and is one of the more valuable things this tool will produce.
"""

from __future__ import annotations

from typing import Final

HSP_TAG: Final[str] = "floatfea-ref-1"
HSP_COMMIT: Final[str] = "25de7ce"
HSP_WORKTREE: Final[str] = "../HSP-stable"
"""Production FloatSim runs live in this worktree, checked out at the tag, so
they are unaffected by export development on main."""

PINNED_ON: Final[str] = "2026-08-10"

# ---------------------------------------------------------------------------
# Reproducible baseline at the tag (gate G1.5 compares against this).
#
# Environment is requirements-lock.txt in the HSP repo, not the manifest: the
# same manifest in a different install order produces a different environment
# (installing capytaine 2.3.1 after xarray downgrades pandas 3.0.5 -> 2.3.3).
# ---------------------------------------------------------------------------
BASELINE: Final[dict[str, int]] = {
    "passed": 801,
    "failed": 0,
    "skipped": 50,
    "xfailed": 20,
}

BASELINE_CONDITIONS: Final[tuple[str, ...]] = (
    "OMP_NUM_THREADS=1, MKL_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1",
    "Hypothesis derandomized via HSP tests/conftest.py",
    ".hypothesis example database cleared before the run",
    "capytaine 2.3.1, numpy 2.4.4, scipy 1.17.1, xarray 2026.7.0, " "pandas 2.3.3, netCDF4 1.7.4",
)

# ---------------------------------------------------------------------------
# Known deviations inherited by every FE result computed from this pin.
#
# These are not FloatFEA defects and they are not fixed here. They are recorded
# because a report that does not name them invites the reader to attribute them
# to the structural model.
# ---------------------------------------------------------------------------
KNOWN_DEVIATIONS: Final[tuple[tuple[str, str], ...]] = (
    (
        "KD-2-revised",
        "FloatSim pitch natural period 32.34 s vs OpenFAST 26.83 s (+20.54%), "
        "attributed to a combined-deck mass-aggregation discrepancy. 5 xfails. "
        "Same class of problem as G3.1b. Any frozen mass inherits it.",
    ),
    (
        "F-RESONANCE-PEAK-FRAGILITY",
        "Heave RAO comparison is fragile within +/-25% of omega_n_heave "
        "(zeta = 0.057% radiation-only, bare-BEM Q ~ 1000). A property of the "
        "comparison, not a defect in either tool.",
    ),
    (
        "LATENT: connector attachment transform property test",
        "test_property_F_ref_equals_T_pullback_of_F_attach fails for extreme "
        "inputs (K ~ 1e8 against a 1 nm moment arm) at rtol 1e-8. It does NOT "
        "appear in the baseline above: derandomizing Hypothesis and clearing "
        "the example database means the deterministic exploration no longer "
        "reaches that corner. The fragility is unfixed, not absent -- it has "
        "become invisible. Disposal is to pin the corner as an explicit "
        "@example and narrow the strategy domain, so exclusion is a stated "
        "scope decision rather than a consequence of which seeds get drawn.",
    ),
    (
        "xi[3:6] interpretation",
        "FloatSim interprets the rotational state three ways: ZYX-intrinsic "
        "Euler (morison.py), axis-angle rotvec (joints.py), and a linearised "
        "rotation vector (hydrostatics.py). They agree to first order only. At "
        "the measured max|theta| = 0.15657 rad they differ by 0.4% at the spar "
        "lever. See docs/conventions.md sec. Rotations.",
    ),
)
