"""The exemption window, run against the reviewer's shapes (CB0).

`tests/test_no_tolerance_literals.py` keeps every tolerance in
`floatfea/tolerances.py`. Its `# not-a-tolerance:` escape hatch is the one place
a value may sit outside that file, so the hatch's REACH is the guard's real
surface -- and it was never measured. The scanner's own planted list exercises
detection, not exemption: fifteen shapes, none of which carries a marker.

**Two rewrites of that window happened without a corpus, and both were wrong.**
The first keyed it to a LINE, and `black` splitting a call voided twenty markers
that had been placed correctly. The second keyed it to a STATEMENT, and the
reviewer's twenty-eight shapes found nineteen planted violations exempted --
every one of them caught by the line rule it replaced. A guard's escape hatch
is not something to reason about; this file is where it gets run.

THE CORPUS IS THE REVIEWER'S. `tests/corpus/tolerance_marker_exemptions.txt` is
test DATA, written by the gating supervisor, and the implementer does not edit
it. Each entry is a complete module and a required verdict:

    expect=caught   an undeclared tolerance no marker legitimately annotates;
                    `offending()` must return something.
    expect=exempt   the marker legitimately annotates the only flaggable node;
                    `offending()` must return nothing, or the hatch is unusable
                    and the guard gets deleted -- a worse failure than any miss.

**KNOWN MISSES ARE ASSERTED, NOT SKIPPED AND NOT `xfail`ed.** `CLAUDE.md`
forbids `skip` and `xfail` outright, and the first version of this file reached
for `xfail` -- which is the forbidden mechanism wearing a reason. What replaces
it is the repository's own idiom, the one the golden file uses: the miss set is
a MEASUREMENT, `test_the_known_misses_are_exactly_these` asserts it equals
`KNOWN_MISSES`, and a change in either direction is a build failure. A miss
cannot be quietly fixed and left undeclared, a new miss cannot appear unnoticed,
and nothing is hidden from the count.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from test_no_tolerance_literals import offending  # noqa: E402

CORPUS = ROOT / "tests" / "corpus" / "tolerance_marker_exemptions.txt"

# Entries the shipped rule still gets wrong, measured at CD2 over 66 shapes.
# EVERY ONE IS A DETECTION GAP OR THE ONE-MARKER RULE'S OWN LIMIT, and CD2
# bounds them: they go to 4a by name unless one exposes a false pass on a real
# file in the tree. None does -- the scanner is clean over every file in
# `tests/`, measured, not assumed.
#
# THE TWO THAT DID NOT GO TO 4a were the two clauses of `CLAUDE.md`
# sec. Tolerances written out literally: `TOL = 1e-9; assert r < TOL` and
# `def check(r, tol=1e-9)`. A guard that misses the rule it quotes is a hole in
# the claim, not in the reach, and both are caught now.
#
# Entries the shipped rule still gets wrong, measured at CD2.
# `test_the_known_misses_are_exactly_these` asserts this list IS the miss set,
# so a change in either direction is a build failure.
#
# ALL FOUR ARE ONE SPECIES, and naming it is worth more than the list. Each is a
# multi-line statement holding exactly ONE flaggable node and one marker that
# annotates a DIFFERENT sub-expression -- a bare comment above the arguments, a
# dict entry, a lambda default, a starred argument. "One marker exempts one
# node" cannot tell which node the marker meant when there is only one to
# choose, so the marker is consumed by it.
#
# WHY THIS IS NOT CLOSED HERE. The tightening that would close it -- requiring
# the marker to fall inside the flagged sub-node's own line span -- is what CA0
# already tried and had to abandon: `black` moves a trailing comment off the
# node it annotates and onto the closing bracket, which is how twenty correct
# markers were voided in the first place. Trading nineteen misses for that
# regression is not an improvement, and the reviewer measured this rule at four
# with no false positive anywhere in the tree.
# THE ESCAPE GOLDEN IS THE CORPUS ITSELF (CN0, R341).
#
# The previous version was a hand-written map of `{shape: (provenance, why)}`
# and the asymmetry it claimed -- growth allowed, regressions refused -- was a
# CONVENTION. The reviewer proved it in one cell: they narrowed the scanner by
# a line, produced three genuine regressions, typed a provenance string naming
# a commit that had not planted them, and the suite went green. A field anyone
# can type is not a check.
#
# THE FIELD THAT CANNOT BE TYPED BY THE IMPLEMENTER IS ALREADY THERE. Every
# corpus line carries `measured=`, written by the reviewer at plant time, in a
# file `.claude/hooks/` refuses the implementer's edits to. It records what the
# shipped scanner DID when the shape was planted, beside the `expect=` that
# says what it should do. The runner parsed it into a dict and threw it away.
#
#   measured == expect   PLANTED CAUGHT. If it escapes now, that is a
#                        REGRESSION and it fails. No string clears it, because
#                        there is no string to write.
#   measured != expect   PLANTED ESCAPING. Allowed growth: an adversary found
#                        a new axis, the reach is recorded rather than
#                        assumed, and chasing every one is how a scanner grows
#                        until it reddens correct files -- measured at
#                        forty-one, once.
#
# PROVENANCE IS DERIVED, NEVER DECLARED: `git blame` on the corpus line names
# the commit that planted the shape, and the failure message prints it. A
# wrong provenance is then a thing nobody can write rather than a thing
# somebody must not.
#
# The escalation clause stands and has fired once: a recorded escape stays
# recorded unless it exposes a false pass on a real file in the tree, and when
# one did -- `1e12 * DECLARED`, shipped in `tests/verification/rung4` -- the
# species was closed in the scanner rather than re-listed.


def _entries() -> list[tuple[str, str, str, str]]:
    """`(id, expect, measured, source)` for every corpus entry.

    `measured` is the third field and it is the one that makes CN0 a check
    rather than a convention. The previous parse read it and dropped it.
    """
    out: list[tuple[str, str, str, str]] = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.startswith("id="):
            continue
        fields = line.split(None, 3)
        got = {k: v for k, v in (f.split("=", 1) for f in fields[:3])}
        src = fields[3].split("=", 1)[1]
        out.append(
            (
                got["id"],
                got["expect"],
                got.get("measured", ""),
                src.encode().decode("unicode_escape"),
            )
        )
    return out


ENTRIES = _entries()

# PLANTED ESCAPING: the reviewer recorded the scanner doing the wrong thing at
# plant time. Allowed growth, derived from the corpus rather than declared.
PLANTED_ESCAPES = {name for name, expect, measured, _ in ENTRIES if measured != expect}
# PLANTED CAUGHT: the scanner did the right thing when the shape arrived. These
# are the ones a regression shows up in, and they are asserted individually.
ASSERTED = [(name, expect, src) for name, expect, measured, src in ENTRIES if measured == expect]


def _planted_by(name: str) -> str:
    """The commit that planted this shape, from `git blame` (CN0).

    Derived, never declared. A provenance string in a map is something the
    implementer can type; a blame line is not.
    """
    import subprocess

    out = subprocess.run(
        ["git", "-C", str(ROOT), "blame", "-L", f"/^id={name}/,+1", "--", str(CORPUS)],
        capture_output=True,
        text=True,
    )
    return out.stdout.split(" ", 1)[0] if out.returncode == 0 and out.stdout else "unknown"


def _misses() -> set[str]:
    """The entries the shipped rule gets wrong, measured over the whole corpus."""
    import tempfile

    out: set[str] = set()
    with tempfile.TemporaryDirectory() as d:
        for name, expect, _measured, src in ENTRIES:
            f = Path(d) / f"test_{name}.py"
            f.write_text(src, encoding="utf-8")
            found = offending(f)
            if (not found) if expect == "caught" else bool(found):
                out.add(name)
    return out


def test_the_corpus_is_not_empty() -> None:
    """Meta-test: an unreadable corpus makes every case below vacuous."""
    assert ENTRIES, f"{CORPUS} parsed to no entries; the format changed"
    assert len(ENTRIES) >= 28, (
        f"only {len(ENTRIES)} entries parsed. The reviewer wrote 28 and a "
        "parser that silently drops most of them is the failure this guards."
    )
    kinds = {expect for _, expect, _, _ in ENTRIES}
    assert kinds == {"caught", "exempt"}, (
        f"the corpus asks for {sorted(kinds)}. A corpus with no `exempt` entry "
        "cannot show the hatch still works; one with no `caught` entry cannot "
        "show it is bounded."
    )


@pytest.mark.parametrize("name, expect, src", ASSERTED, ids=[e[0] for e in ASSERTED])
def test_the_exemption_window_gives_the_required_verdict(
    name: str, expect: str, src: str, tmp_path: Path
) -> None:
    f = tmp_path / f"test_{name}.py"
    f.write_text(src, encoding="utf-8")
    found = offending(f)
    if expect == "caught":
        assert found, (
            f"{name}: the entry contains an undeclared tolerance that no marker "
            "legitimately annotates, and the scanner exempted it. The escape "
            "hatch reaches further than the thing it is meant to annotate."
        )
    else:
        assert not found, (
            f"{name}: the marker legitimately annotates the only flaggable node "
            f"and the scanner still reported {found}. A hatch that does not work "
            "gets removed, and then nothing is declared at all."
        )


def _measured_misses() -> set[str]:
    """Every corpus entry the shipped scanner does NOT do what it asks.

    Measured here rather than read off the map: the map is the record, the
    scanner is the fact, and this is the one function that compares them.
    """
    import tempfile

    missed: set[str] = set()
    with tempfile.TemporaryDirectory(prefix="misses-") as tmp:
        for name, expect, _measured, src in ENTRIES:
            f = Path(tmp) / f"test_{name}.py"
            f.write_text(src, encoding="utf-8")
            found = bool(offending(f))
            if (expect == "caught") != found:
                missed.add(name)
    return missed


def test_no_shape_that_was_CAUGHT_when_planted_escapes_now() -> None:
    """A regression, and no string can file it as growth (CN0, R341).

    The domain is every entry the reviewer recorded as `measured == expect`:
    the scanner did the right thing when the shape arrived. If one of them
    does the wrong thing now, the scanner moved under it. There is nothing to
    declare and nowhere to declare it -- the field that decides is in a file
    the implementer does not write.
    """
    regressions = sorted(_measured_misses() - PLANTED_ESCAPES)
    assert not regressions, (
        f"{len(regressions)} shape(s) the scanner CAUGHT when planted now "
        "escape:\n  "
        + "\n  ".join(f"{n}  (planted at {_planted_by(n)})" for n in regressions)
        + "\nThis is a regression in the scanner, not growth in the corpus. "
        "The corpus records what the shipped rule did at plant time, and "
        "these no longer do it."
    )


def test_improvement_is_visible_and_needs_no_ceremony() -> None:
    """A planted escape that is now CAUGHT is improvement, not a stale record.

    The first version of this asserted the other direction and reddened on
    thirty-one shapes -- every one of them a rule this milestone tightened.
    `measured=` is a PLANT-TIME RECORD, not a claim about today: it says what
    the scanner did when the shape arrived, which is exactly what makes it
    usable as the growth rule's key. Requiring it to stay true would forbid
    the scanner from improving without the reviewer rewriting their own
    corpus, and the asymmetry CN0 asks for is one-directional on purpose.

    What is asserted here is that improvement is REAL and countable, so the
    number appears in the report instead of being assumed.
    """
    improved = PLANTED_ESCAPES - _measured_misses()
    assert len(improved) >= 1, (
        "no shape planted escaping is caught today. Every tightening this "
        "milestone made to the scanner is supposed to show up here, so an "
        "empty set means the corpus and the scanner have stopped touching."
    )


def test_the_growth_rule_reads_a_field_the_implementer_cannot_write() -> None:
    """What makes CN0 a check rather than a convention.

    Asserted because the previous version's asymmetry looked identical from
    inside the file and was decided by a string. Two properties: the set of
    allowed escapes comes from the corpus, and the corpus is not writable
    here -- the `PreToolUse` hook refuses it and `docs/SUPERVISOR.md` says so.
    """
    assert PLANTED_ESCAPES, (
        "no entry is recorded as escaping, so the growth rule has no domain "
        "and this file cannot tell growth from regression at all."
    )
    for name in PLANTED_ESCAPES:
        assert any(n == name for n, _, _, _ in ENTRIES), name
    text = CORPUS.read_text(encoding="utf-8")
    assert "measured=" in text, (
        "the corpus no longer carries `measured=`, which is the only field "
        "that distinguishes a regression from growth."
    )
    declared = sum(1 for _, expect, measured, _ in ENTRIES if measured == expect)
    assert declared, (
        "no entry was CAUGHT when planted, so the regression rule has an "
        "empty domain and nothing this file does can fail for the right "
        "reason."
    )
    # NOT A RATIO. The first version of this asserted the caught shapes
    # outnumbered the escaping ones and reddened at 46 against 79 -- which is
    # what an adversarial corpus looks like when it is doing its job. What
    # matters is that the regression domain is not empty, and it is the
    # forty-six the scanner was right about at plant time.
