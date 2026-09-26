"""The staleness checker, against the three findings that asked for it (CX1).

`scripts/precommit_stale.py` is the reviewer's own suggestion at the fiftieth
verdict: any commit changing a figure class, a regex, a generator or a
tolerance row greps the tree for the old class name, the old number and the
old row name before it is committed. Five rounds of findings were sentences
written in the commit that repaired the same species elsewhere, and the
reading was that this is not a detection problem -- so the help is a command
run at commit time, not another pattern.

WHAT IS CONTROLLED HERE, and one of the three is a MISS:

  R452  an old NUMBER surviving -- `114` in a tolerance entry after the
        corpus reached 126. CAUGHT.
  R451  an old CLASS surviving -- a row called `derived` after its sibling
        commit made it `words`. CAUGHT.
  R454  four sentences citing a withheld count -- "it breached at MORE of the
        reviewer's clean frames than the ratio did". NOT CAUGHT, and the test
        below asserts that it is not, because a checker whose suite contains
        only its successes is the shape this repository keeps finding. The
        sentences name neither a number nor a row, so nothing on the minus
        side of that diff points at them.

The third control is therefore a recorded limitation with a test that fails
if the limitation ever silently becomes a capability nobody noticed.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _module():
    spec = importlib.util.spec_from_file_location(
        "precommit_stale", ROOT / "scripts" / "precommit_stale.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["precommit_stale"] = mod
    spec.loader.exec_module(mod)
    return mod


S = _module()


_R452_DIFF = """--- a/docs/milestones/F2_figures.md
+++ b/docs/milestones/F2_figures.md
-| `rigid_mode_corpus_frames` | 114 |
+| `rigid_mode_corpus_frames` | 126 |
"""

_R451_DIFF = """--- a/scripts/regen_figures.py
+++ b/scripts/regen_figures.py
-            _floor("rigid_mode_corpus_refused", "derived"),
+            _floor("rigid_mode_corpus_refused", "words"),
"""

_R454_DIFF = """--- a/scripts/regen_figures.py
+++ b/scripts/regen_figures.py
-    # What keeps it out is that no sentence anywhere needs it.
+    # Published, by the same rule as its two siblings.
"""

_RENAMED_ROW_DIFF = """--- a/scripts/regen_figures.py
+++ b/scripts/regen_figures.py
-    rows.append(("rigid_mode_seventh_orders", f"{x:.3f}"))
+    rows.append(("rigid_mode_seventh_in_orders", f"{x:.3f}"))
"""

_NO_CHANGE_DIFF = """--- a/README.md
+++ b/README.md
-a sentence about nothing measurable
+another sentence about nothing measurable
"""


def test_R452_an_old_NUMBER_is_extracted_from_the_minus_side() -> None:
    """The figure row's old value is what the entry five lines away kept."""
    tokens = S.old_tokens(_R452_DIFF)
    assert "114" in tokens["numbers"], tokens
    assert "126" not in tokens["numbers"], "the NEW value is not a stale token"


def test_R451_an_old_CLASS_is_extracted_with_its_row() -> None:
    tokens = S.old_tokens(_R451_DIFF)
    assert "rigid_mode_corpus_refused/derived" in tokens["classes"], tokens


def test_a_RENAMED_row_is_extracted_and_a_REVALUED_one_is_not() -> None:
    """The bare name, not the quoted form.

    A row whose VALUE moved is removed and re-added, and comparing the quoted
    form reported every live `{{fig:...}}` citation of it as surviving a
    rename that never happened -- 170 of the first version's 188 survivors on
    one round's diff.
    """
    assert "rigid_mode_seventh_orders" in S.old_tokens(_RENAMED_ROW_DIFF)["rows"]
    assert not S.old_tokens(_R452_DIFF)["rows"], "a revalued row is not a renamed one"


def test_a_row_that_did_not_change_yields_nothing() -> None:
    """A checker that fires on every commit is a checker nobody runs."""
    assert not any(S.old_tokens(_NO_CHANGE_DIFF).values())


def test_a_row_whose_class_is_unchanged_is_not_reported() -> None:
    same = _R451_DIFF.replace('"words"', '"derived"')
    assert not S.old_tokens(same)["classes"]


def test_R454_IS_A_RECORDED_MISS_and_not_a_control() -> None:
    """The four citing sentences name neither a number nor a row.

    If this ever starts passing, the checker gained a capability and the
    docstring above is out of date -- which is the same species it exists to
    catch, so it is asserted in the direction that fails on a silent change.
    """
    assert not any(S.old_tokens(_R454_DIFF).values()), (
        "the checker now extracts something from a prose-only diff. That is "
        "an improvement and the module docstring must stop calling R454 a "
        "recorded miss."
    )


def test_the_SURVIVOR_search_skips_a_withdrawal_marker() -> None:
    """A quoted old value is the repository's own way of recording history."""
    assert S._WITHDRAWN.search("`114` stood here and the corpus is 126")
    assert S._WITHDRAWN.search("the sentence is withdrawn (R451)")
    assert not S._WITHDRAWN.search("over all 114 corpus frames")


def test_the_checker_runs_over_this_round_and_says_what_it_looked_for() -> None:
    """A meta-test: the entry point must work on a real range, not just data."""
    code = S.main(["precommit_stale.py", "HEAD~1..HEAD"])
    assert code in (0, 1), code


@pytest.mark.parametrize("kind", ["numbers", "rows", "classes"])
def test_every_token_kind_is_reachable(kind: str) -> None:
    """Each extractor has at least one diff in this file that exercises it."""
    seen = set()
    for diff in (_R452_DIFF, _R451_DIFF, _RENAMED_ROW_DIFF):
        for k, v in S.old_tokens(diff).items():
            if v:
                seen.add(k)
    assert kind in seen, f"no control diff exercises `{kind}`"
