"""The re-exports two by-path consumers depend on, asserted rather than commented (FL1).

**THIS TEST EXISTS BECAUSE A LINT AUTOFIX ALREADY BROKE IT ONCE, IN THE SAME SESSION
THAT WROTE THE COMMENT WARNING ABOUT IT.** FL1 moved the member-force core out of
`scripts/measure/member_forces_table.py` into `floatfea/post/forces_table.py`. Two
scripts -- `f6a_premise_check.py` and `f6_results_report.py` -- load that script BY PATH
through `importlib` and reach for these names as attributes of the loaded module, so
after the move they resolve only because the script imports them back into its own
namespace.

`ruff` reads them as unused, because within that file they are. The import block carries
`# noqa: F401` for exactly that reason, and the first attempt to say so in a comment was
undone two commands later: an import-sort autofix merged two blocks and dropped four of
the names, leaving `_joint_wiring`, `_lam_full_scale`, `_net_field` and `_station_values`
unresolvable. Nothing was red. The consumers fail with an `AttributeError` at the far end
of an `importlib` load, with nothing in either file to point at.

A comment cannot survive a tool that rewrites the lines it describes. This can.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "measure" / "member_forces_table.py"

# The eight attributes the two consumers actually reach for. Taken from the tree rather
# than from memory:
#
#   claim: these are exactly the `MFT.<name>` lookups the two consumers make
#   cmd:   grep -ohE "MFT\.[A-Za-z_]+" scripts/measure/f6a_premise_check.py \
#            scripts/measure/f6_results_report.py | sort -u
#   out:   the eight names below
CONSUMED = (
    "_joint_wiring",
    "_lam_full_scale",
    "_net_field",
    "_static_rows",
    "_station_values",
    "_stresses",
    "map_joint_reactions",
    "solve_inertia_relief",
)


def _load_by_path() -> object:
    """Load the script the way its two consumers do, not by package import.

    The route is the subject: a package import would not reproduce the `sys.path`
    arrangement those scripts rely on, and it is the by-path attribute lookup that
    broke.
    """
    for entry in (str(ROOT), str(ROOT / "scripts")):
        if entry not in sys.path:
            sys.path.insert(0, entry)
    spec = importlib.util.spec_from_file_location("member_forces_table", SCRIPT)
    assert spec is not None and spec.loader is not None, SCRIPT
    module = importlib.util.module_from_spec(spec)
    sys.modules["member_forces_table"] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("name", CONSUMED)
def test_the_by_path_consumers_can_still_reach_every_name(name: str) -> None:
    """Each name resolves on the module as loaded by path.

    Parametrised one name per case ON PURPOSE (EG3(i)'s discipline applied to a test
    rather than to a verdict): a single assertion over the tuple reports the first
    missing name and hides the rest, and the autofix that caused this dropped FOUR.
    """
    module = _load_by_path()
    assert hasattr(module, name), (
        f"`member_forces_table.{name}` does not resolve. Two scripts load that file by "
        f"path and read this attribute; before FL1's move it was defined there, and it "
        f"now resolves only via the `# noqa: F401` re-export block. If a lint autofix "
        f"removed it as unused, restore it to that block rather than deleting this case."
    )


def test_the_names_this_test_guards_are_the_ones_the_consumers_ASK_FOR() -> None:
    """The guarded list is read off the consumers, so it cannot drift from them.

    Without this, `CONSUMED` is a list someone typed once. A consumer that starts
    reaching for a ninth attribute would be unprotected, and the failure mode is the
    same `AttributeError` this file exists to prevent.
    """
    import re

    asked: set[str] = set()
    for rel in ("f6a_premise_check.py", "f6_results_report.py"):
        text = (ROOT / "scripts" / "measure" / rel).read_text(encoding="utf-8")
        asked.update(re.findall(r"MFT\.([A-Za-z_][A-Za-z0-9_]*)", text))

    assert asked, (
        "no `MFT.<name>` lookups found in either consumer. Either they stopped loading "
        "the script by path -- in which case this whole file can go -- or the pattern "
        "this test greps for no longer matches how they do it."
    )
    unguarded = sorted(asked - set(CONSUMED))
    assert not unguarded, (
        f"the consumers reach for {unguarded}, which `CONSUMED` does not list, so those "
        f"attributes are unprotected. Add them to `CONSUMED`."
    )
