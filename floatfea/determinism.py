"""Every library default that can vary a result, pinned in one place (Q4).

Why this is a module and not three fixes
----------------------------------------
Three library-default nondeterminisms have now surfaced in this project, each
found the hard way and each fixed where it was found:

1. **Hypothesis seeding** — `derandomize=False` by default, so two runs explore
   different examples and a property test that passes today fails tomorrow with no
   code change. Fixed in `HSP:tests/conftest.py` during F1.
2. **BLAS thread count** — reduction order varies with thread count, so a sum is
   not bit-reproducible across machines. Pinned for the G1.5 baseline.
3. **Sparse factorisation ordering** — a fill-reducing permutation chosen by a
   heuristic that varies with library version moves stored results with no code
   change. Surfaced at F2's lock.

**Three is a class, not three incidents.** Meeting the fourth the way the first
three were met is the expensive option, so the class is enumerated here once.

What counts as a member
-----------------------
Any library whose **default** can change a numerical result across runs, versions,
or thread counts, without any change to this repository's code. The test beside
this module asserts each is pinned; adding a library to the project means adding
it here or explaining why it is exempt.

Not covered, deliberately
-------------------------
This pins *defaults*. It cannot pin genuine algorithmic nondeterminism (an
iterative solver with a random restart), nor differences across CPU architectures
or library builds. Those need a tolerance, not a seed, and the distinction matters:
pinning a seed makes a run *repeatable*, which is not the same as making it
*correct*.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:  # numpy stays a deferred import at run time, per pin_threads
    import numpy as np
    from numpy.typing import NDArray

# ---------------------------------------------------------------------------
# 1. Threading. Reduction ORDER varies with thread count, so a floating-point
#    sum is not bit-reproducible across machines unless the count is fixed.
#    Set before numpy/scipy import to take effect -- hence a module imported
#    early, not a call made late.
# ---------------------------------------------------------------------------
THREAD_ENV: Final[tuple[str, ...]] = (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
)

# ---------------------------------------------------------------------------
# 2. Sparse direct solve. SuperLU's column permutation default is
#    COLAMD, whose output can differ between SciPy versions. Pinned explicitly
#    so a stored result moves only when this constant moves.
#
#    NATURAL would be reproducible but catastrophic for fill-in; COLAMD is the
#    right algorithm and the point is to NAME it, not to avoid it.
# ---------------------------------------------------------------------------
SPARSE_PERMC_SPEC: Final[str] = "COLAMD"

# ---------------------------------------------------------------------------
# 3. ARPACK eigensolvers. `scipy.sparse.linalg.eigsh` starts from a RANDOM
#    vector unless `v0` is given, so eigenvalues can differ run to run in the
#    last digits -- and for a degenerate or clustered spectrum, the returned
#    EIGENVECTORS can differ completely.
#
#    G2.1 (six rigid-body modes) has a six-fold degenerate zero eigenvalue, which
#    is exactly the case where an unseeded start is least reproducible. Any call
#    must pass `v0=deterministic_v0(n)`.
# ---------------------------------------------------------------------------
ARPACK_V0_SEED: Final[int] = 20260830

# ---------------------------------------------------------------------------
# 4. Python hash randomisation. Affects iteration order of sets and of dicts
#    keyed by str. Harmless until an assembly or DOF ordering is built by
#    iterating a set, at which point it silently permutes the matrix.
# ---------------------------------------------------------------------------
HASH_SEED_ENV: Final[str] = "PYTHONHASHSEED"

# ---------------------------------------------------------------------------
# 5. Hypothesis. FloatFEA does not use it yet; HSP does, pinned in its conftest.
#    Named here so the class stays complete rather than accurate-by-omission.
# ---------------------------------------------------------------------------
HYPOTHESIS_DERANDOMIZE: Final[bool] = True


def pin_threads(n: int = 1) -> None:
    """Fix every BLAS/OpenMP thread count. Call before importing numpy."""
    for var in THREAD_ENV:
        os.environ[var] = str(n)


def deterministic_v0(n: int) -> NDArray[np.float64]:
    """A fixed ARPACK starting vector of length ``n``.

    Seeded from a dedicated generator rather than the global numpy state, so a
    caller that seeds numpy elsewhere cannot change an eigenvalue result.
    """
    # ANNOTATED, NOT `object` (CE0). The old return type made four numpy calls
    # in `test_determinism_pins.py` unresolvable, and those four appeared under
    # one interpreter and not the other -- indistinguishable, to the version
    # guard, from a real use of a newer API. A vague annotation is noise a
    # detector has to be tuned around.
    import numpy as np

    out: NDArray[np.float64] = np.random.default_rng(ARPACK_V0_SEED).standard_normal(n)
    return out


def report() -> dict[str, object]:
    """Everything this module pins, for a run log."""
    return {
        "threads": {v: os.environ.get(v) for v in THREAD_ENV},
        "sparse_permc_spec": SPARSE_PERMC_SPEC,
        "arpack_v0_seed": ARPACK_V0_SEED,
        "pythonhashseed": os.environ.get(HASH_SEED_ENV),
        "hypothesis_derandomize": HYPOTHESIS_DERANDOMIZE,
    }
