#!/usr/bin/env python
"""Where `clean_worst_ratio` comes from, state by state (R303).

The canonical render and a laptop render disagree by 7.3% on this figure while
`clean_worst_entry` is byte-identical on both, so no argmax over ENTRIES
flipped. The figure is

    max over entries of ( max over states of _oob_state(entry, state) ) / ceil

and there are two argmaxes in it. This prints the inner one: the winning
entry's out-of-balance for every state, which state wins, and the ratio -- so
the two machines can be compared row by row rather than at the single number
the figures file publishes.

    python scripts/localise_clean_worst.py

It writes nothing and asserts nothing. It is a measurement instrument, run on
both machines and quoted in the step report; the assertion that comes out of it
lives in `scripts/regen_figures.py --check`.
"""

from __future__ import annotations

import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests" / "verification" / "rung1"))


def main() -> int:
    import test_corpus_configurations as C

    from floatfea.tolerances import PATCH_TEST_EXACTNESS as CEIL

    worst_entry, worst_val = None, -1.0
    for e in C.SOLVED:
        v = max(C._oob_state(e, st) for st in C.STATES)
        if v > worst_val:
            worst_entry, worst_val = e, v

    assert worst_entry is not None
    print(f"machine     {platform.machine()} / {platform.processor() or 'unknown'}")
    print(f"python      {platform.python_version()}")
    try:
        import numpy

        print(f"numpy       {numpy.__version__}")
    except ImportError:  # pragma: no cover - numpy is a hard dependency
        pass
    print(f"entry       {worst_entry['id']}")
    print(f"ceiling     {CEIL:.17e}")
    print()
    print("state                    out-of-balance          ratio to ceiling")
    rows = [(st, C._oob_state(worst_entry, st)) for st in C.STATES]
    for st, val in rows:
        mark = "  <- wins" if val == worst_val else ""
        print(f"{str(st):<24} {val:.17e}  {val / CEIL:.6f}{mark}")
    print()
    print(f"clean_worst_ratio        {worst_val / CEIL:.4f}x")
    print(f"clean_worst_entry        {worst_entry['id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
