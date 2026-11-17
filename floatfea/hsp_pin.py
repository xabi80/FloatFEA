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

import os
from pathlib import Path
from typing import Final, Literal

HSP_TAG: Final[str] = "floatfea-ref-1"
HSP_COMMIT: Final[str] = "25de7ce"

PINNED_ON: Final[str] = "2026-08-10"

# ---------------------------------------------------------------------------
# Where the two pinned worktrees are (GI3(e), R1208).
#
# `HSP_WORKTREE: Final[str] = "../HSP-stable"` used to live here. It was READ BY
# NOTHING -- a declared constant with no consumer, verified over the whole tree --
# while six other files carried seven assignments of their own, none of which
# resolves from this repository's actual location. GI3(e) asked for a config key
# with an env-var fallback; R1208 is why there are TWO keys and not one.
#
# TWO, BECAUSE ONE IS SILENT IN ONE DIRECTION. DS0 is enforced by three refusals
# keyed on the NAME `HSP-stable`, so a single key pointed at STABLE is loud. A
# single key pointed at RUNS is not: `scripts/export_buoy_centers_ref.py` has no
# DS0 refusal, so it would regenerate `data/platform/buoy_centers_ref.json` -- the
# input to EB6's label-provenance gate -- from the runs tree while that file's
# `"source"` field declares `HSP-stable/...` and its `_blob_sha` records that
# tree's sha. Both worktrees sit at the same tag today, so the bytes match and
# `--check` stays green with both sides moving together. That is C155's shape and
# FR1's second head: an input accepted and used other than as declared.
#
# THIS RESOLVES A PATH AND NOTHING ELSE. It does not check the tag. Each caller's
# own tag refusal stays exactly where it is, because R1208's closing condition is
# that those three refusals are still seen to fire -- centralising them here would
# have replaced three loud, differently-worded refusals with one, which is the
# repair-not-extend line EK2 draws.
# ---------------------------------------------------------------------------

HSP_RUNS_ENV: Final[str] = "FLOATFEA_HSP_RUNS"
HSP_STABLE_ENV: Final[str] = "FLOATFEA_HSP_STABLE"

_LEGACY_SIBLING: Final[dict[str, str]] = {"runs": "HSP-runs", "stable": "HSP-stable"}
"""The pre-GI3(e) convention: a sibling of the repository root. Kept as the last
fall-back so a checkout that already satisfies it keeps working unchanged."""


def worktree(
    which: Literal["runs", "stable"],
    declared: Path | str | None = None,
    *,
    require: bool = False,
) -> Path:
    """The pinned HSP worktree, resolved in one place.

    Order: `declared` (a config key, `floatsim.worktree_runs` /
    `floatsim.worktree_stable`), then the environment variable, then the legacy
    sibling of the repository root.

    **`require=False` IS THE DEFAULT AND THAT IS DELIBERATE.** The six call sites
    this replaces are MODULE-LEVEL constants, and three of them are imported by
    `tests/` and by `scripts/export_f4_dynamic_inputs.py`. Refusing at import
    would turn "this machine has no worktree" -- which is true of CI, by design,
    since no HSP worktree is checked out there -- into an ImportError that takes
    the whole module with it. That is R670's shape: 124 of 126 gate cases errored
    in CI while all 126 passed on the machine that wrote them.

    So the default returns the best CANDIDATE, existing or not, exactly as the
    bare `ROOT.parent / "HSP-runs"` expressions it replaces did; each caller's own
    preflight still refuses, with its own message, and R1208's three DS0 refusals
    are untouched. `require=True` is for a caller that is about to open the tree
    and wants one refusal naming every place it looked.
    """
    if which not in _LEGACY_SIBLING:
        raise ValueError(f"which must be 'runs' or 'stable', not {which!r}")
    env_name = HSP_RUNS_ENV if which == "runs" else HSP_STABLE_ENV
    legacy = _repo_root().parent / _LEGACY_SIBLING[which]
    tried: list[str] = []
    # R1214. A SOURCE THAT IS SET AND WRONG IS A REFUSAL. ONLY AN UNSET ONE FALLS THROUGH.
    #
    # The first version of this loop appended to `tried` and CONTINUED whenever a set path
    # was not a directory, so a mistyped `FLOATFEA_HSP_RUNS` was silently discarded and the
    # legacy sibling used instead -- the caller then opened a DIFFERENT tree from the one
    # declared, with nothing printed. That is FR1's second head: an input accepted and used
    # other than as declared. Someone who sets a key has stated an intent, and the only
    # honest answers are "that tree" or a refusal naming it.
    #
    # The legacy sibling is NOT such a source. Nobody set it; it is the implicit
    # pre-GI3(e) fallback, so its absence is the ordinary state of a machine with no
    # worktree -- true of CI by design -- and it falls through under `require=False` for
    # the import-time reason in the docstring above.
    for source, value in (
        (f"declared (floatsim.worktree_{which})", declared),
        (f"${env_name}", os.environ.get(env_name)),
    ):
        if value is None or value == "":
            tried.append(f"{source}: not set")
            continue
        # R1219. A RELATIVE VALUE IS RESOLVED AGAINST THE REPOSITORY ROOT, NOT THE CWD.
        # `FLOATFEA_HSP_RUNS=../HSP-runs` otherwise resolved to a different tree
        # depending on where the process was started -- measured at two values -- so the
        # same declaration named two worktrees. The repo root is the only anchor that is
        # a property of the declaration rather than of the caller's shell.
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = _repo_root() / path
        if path.is_dir():
            return path.resolve()
        raise SystemExit(
            f"REFUSED: the HSP {which} worktree was declared and is not a directory.\n"
            f"  {source} = {path}\n"
            f"This is not silently replaced by another source (R1214): a key that is set "
            f"states an intent, and using a different tree than the one declared is an "
            f"input used other than as declared. Fix the value or unset it."
        )
    if legacy.is_dir():
        return legacy.resolve()
    tried.append(f"legacy sibling of the repo root: {legacy} is not a directory")
    if require:
        raise SystemExit(
            f"REFUSED: cannot locate the pinned HSP {which} worktree (tag {HSP_TAG}).\n"
            + "".join(f"  tried {line}\n" for line in tried)
            + f"Set ${env_name}, or declare floatsim.worktree_{which} in the run config."
        )
    return legacy


def _repo_root() -> Path:
    """This repository's root, from this file's own location."""
    return Path(__file__).resolve().parents[1]


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
