"""Every test named as gate evidence must exist and be collectable (AL3).

Why this exists
---------------
G1.1 was recorded **PASS** in `docs/closure/F1.md` citing a writer/reader
round-trip in `tests/verification/rung4`. **There was no such test.** It survived
until a queued work item happened to point at it — which means the closure
artifact was certifying rather than recording, and every downstream milestone
would have inherited it as a foundation.

A closure artifact is a claim about what was verified. Nothing checked that the
claim's *evidence* existed, so this applies the Z4 / `live_dof` treatment to the
milestone record itself: a row citing a phantom test now fails CI instead of
waiting to be noticed.

Scope, honestly
---------------
This enforces **existence and collectability** — AL2's question (a). It cannot
enforce question (b), whether the named test tests *what the row claims*; that
needs reading, and it is the harder failure (see the tenth guard in
`docs/instrumentation.md`). What this does guarantee is that (b) always has
something real to be asked about.

Cross-repo evidence is prefixed `HSP:` in the artifact and is **not** checked
here: `CLAUDE.md` says the codebases meet only at the interchange file, so this
suite must not require HSP to be present. The prefix makes that boundary explicit
rather than silent — an unprefixed path is asserted to be FloatFEA-local.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[3]   # tests/verification/rung3/<file>
CLOSURE = sorted((REPO / "docs" / "closure").glob("F*.md"))

# Backticked paths that look like repository files.
_PATH = re.compile(r"`((?:HSP:)?(?:tests|floatfea|docs)/[A-Za-z0-9_./-]+\.(?:py|md))`")


def _cited(doc: Path) -> list[str]:
    return sorted(set(_PATH.findall(doc.read_text(encoding="utf-8"))))


def test_there_are_closure_artifacts_to_check() -> None:
    """Meta-test: this whole module is vacuous if the glob finds nothing."""
    assert CLOSURE, "no docs/closure/F*.md found -- every test below is vacuous"


@pytest.mark.parametrize("doc", CLOSURE, ids=lambda d: d.stem)
def test_the_artifact_cites_evidence_at_all(doc: Path) -> None:
    """A closure artifact naming no evidence cannot be audited."""
    assert _cited(doc), f"{doc.name} names no evidence files; it cannot be checked"


@pytest.mark.parametrize("doc", CLOSURE, ids=lambda d: d.stem)
def test_every_cited_local_file_exists(doc: Path) -> None:
    missing = [
        c for c in _cited(doc)
        if not c.startswith("HSP:") and not (REPO / c).is_file()
    ]
    assert not missing, (
        f"{doc.name} cites evidence that DOES NOT EXIST: {missing}. "
        "This is the G1.1 failure: a gate recorded PASS against a phantom test."
    )


@pytest.mark.parametrize("doc", CLOSURE, ids=lambda d: d.stem)
def test_every_cited_local_test_file_contains_tests(doc: Path) -> None:
    """Existence is not enough -- an empty test file is a phantom with a filename."""
    empty = []
    for c in _cited(doc):
        if c.startswith("HSP:") or not c.startswith("tests/"):
            continue
        f = REPO / c
        if f.is_file() and "def test_" not in f.read_text(encoding="utf-8"):
            empty.append(c)
    assert not empty, f"{doc.name} cites test files containing no tests: {empty}"


@pytest.mark.parametrize("doc", CLOSURE, ids=lambda d: d.stem)
def test_cross_repo_evidence_is_marked_as_such(doc: Path) -> None:
    """An HSP path written without the prefix would be silently unchecked.

    `tests/unit/...` is HSP's layout; FloatFEA has no `tests/unit/` directory.
    An unprefixed path there is a cross-repo citation that this suite would
    otherwise report as missing, or worse, that a future reorganisation would
    make accidentally resolve.
    """
    unmarked = [
        c for c in _cited(doc)
        if c.startswith("tests/unit/") and not (REPO / c).is_file()
    ]
    assert not unmarked, (
        f"{doc.name} cites what looks like HSP evidence without the 'HSP:' "
        f"prefix: {unmarked}"
    )


def test_the_guard_can_actually_fail() -> None:
    """Negative control: a phantom citation must be detected.

    Without this the parametrized tests above pass trivially on any artifact
    whose citations all happen to resolve, and would keep passing if the regex
    silently stopped matching anything.
    """
    fake = "`tests/verification/rung4/test_this_does_not_exist.py`"
    found = _PATH.findall(fake)
    assert found == ["tests/verification/rung4/test_this_does_not_exist.py"]
    assert not (REPO / found[0]).is_file()
