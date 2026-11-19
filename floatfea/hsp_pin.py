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
from collections.abc import Callable
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

    The decision table itself lives in `resolve_declared_path` -- see its docstring
    for why it is one function and not two copies.
    """
    if which not in _LEGACY_SIBLING:
        raise ValueError(f"which must be 'runs' or 'stable', not {which!r}")
    env_name = HSP_RUNS_ENV if which == "runs" else HSP_STABLE_ENV
    legacy = _repo_root().parent / _LEGACY_SIBLING[which]
    return resolve_declared_path(
        what=f"HSP {which} worktree",
        declared=declared,
        declared_source=f"declared (floatsim.worktree_{which})",
        env_name=env_name,
        fallback=legacy,
        fallback_source=f"legacy sibling of the repo root: {legacy}",
        what_require=f"pinned HSP {which} worktree",
        require=require,
        exists=Path.is_dir,
        noun="a directory",
        hint=(f"Set ${env_name}, or declare floatsim.worktree_{which} in the run config."),
        extra=f" (tag {HSP_TAG})",
    )


def resolve_declared_path(
    *,
    what: str,
    what_require: str | None = None,
    declared: Path | str | None,
    declared_source: str,
    env_name: str,
    fallback: Path,
    fallback_source: str,
    require: bool,
    exists: Callable[[Path], bool],
    noun: str,
    hint: str,
    extra: str = "",
) -> Path:
    """`declared` key, then `$env_name`, then `fallback`. One table, one reader.

    **IT IS ONE FUNCTION BECAUSE A SECOND COPY OF THIS TABLE IS THE DEFECT R2 STEP 0
    PAID FIVE ROUNDS FOR.** That step's one recurring shape was "one predicate, two
    readers, diverging on a clause after they were made to agree on the first" --
    R1221, R1240, R1250, R1256 and R1261 were each that, and each needed fixing twice.
    GJ1 adds a third thing to resolve by exactly this table (the FloatSim interpreter),
    so the table is factored here rather than written again. `worktree()`'s behaviour is
    unchanged and `tests/unit/test_hsp_worktree_resolution.py` is what says so.

    The three rules it carries, each earned at a measured defect:

    * **R1214** -- a source that is SET AND WRONG refuses. Only an UNSET one falls
      through. The first version appended to `tried` and continued whenever a set path
      was not valid, so a mistyped key was silently discarded and the caller opened a
      different target from the one declared, with nothing printed: FR1's second head.
      Someone who sets a key has stated an intent, and the only honest answers are
      "that one" or a refusal naming it.
    * **R1219** -- a RELATIVE value anchors to the repository root, never the cwd, so
      the same declaration cannot name two targets depending on where the process was
      started.
    * **The fallback is not such a source.** Nobody set it; it is the implicit default,
      so its absence is the ordinary state of a machine that has not got the thing --
      true of CI by design -- and it falls through under `require=False`.
    """
    # THE TWO MESSAGES DIFFERED BY ONE WORD AND A TEST ASSERTS IT. The declared-and-wrong
    # refusal says "the HSP runs worktree"; the cannot-locate refusal says "the PINNED HSP
    # runs worktree (tag ...)". Factoring the table collapsed them to one label and
    # `test_require_True_refuses_and_names_every_candidate_it_tried` went red on the
    # missing word -- which is the test doing its job: a refusal's wording is what a
    # person reads at 2am, and a refactor is not a licence to reword it.
    tried: list[str] = []
    for source, value in (
        (declared_source, declared),
        (f"${env_name}", os.environ.get(env_name)),
    ):
        if value is None or value == "":
            tried.append(f"{source}: not set")
            continue
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = _repo_root() / path
        if exists(path):
            return path.resolve()
        raise SystemExit(
            f"REFUSED: the {what} was declared and is not {noun}.\n"
            f"  {source} = {path}\n"
            f"This is not silently replaced by another source (R1214): a key that is set "
            f"states an intent, and using a different one than the one declared is an "
            f"input used other than as declared. Fix the value or unset it."
        )
    if exists(fallback):
        return fallback.resolve()
    tried.append(f"{fallback_source} is not {noun}")
    if require:
        raise SystemExit(
            f"REFUSED: cannot locate the {what_require or what}{extra}.\n"
            + "".join(f"  tried {line}\n" for line in tried)
            + hint
        )
    return fallback


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
