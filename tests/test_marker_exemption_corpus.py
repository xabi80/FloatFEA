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
# THE ESCAPE GOLDEN, KEYED BY SHAPE, WITH PROVENANCE (CM4).
#
# `{id: (planted by, what the shipped rule does with it)}`. The rule is
# asymmetric on purpose, and the asymmetry is the whole point:
#
#   A REVIEWER-PLANTED SHAPE THAT ESCAPES IS ADDED, with their commit named.
#   That is allowed growth: an adversary who finds a new axis has told us
#   something, and recording it is how the reach stays measured instead of
#   assumed. Chasing every one of them is how a scanner grows until it
#   reddens correct files -- measured at forty-one of them, once.
#
#   A SHAPE PREVIOUSLY CAUGHT THAT STARTS ESCAPING IS A REGRESSION and fails.
#   It arrives as a name in the measured set that this map does not carry,
#   and there is no way to record it without naming who planted it and when.
#
#   A SHAPE THAT STARTS BEING CAUGHT also fails, so the map cannot quietly
#   outlive what it describes -- but the fix there is one deletion and a
#   sentence, not work.
#
# The escalation clause stands and has fired once: a miss stays here unless
# one of them exposes a false pass on a real file in the tree. At the
# thirty-sixth verdict one did -- `1e12 * DECLARED`, shipped in
# `tests/verification/rung4` -- and that species was closed in the scanner
# rather than re-listed.
KNOWN_MISSES: dict[str, tuple[str, str]] = {
    "detect_annotated_module_float_threshold": (
        "CD2, the reviewer's corpus at that round",
        "module-level named float, but an AnnAssign rather than an Assign",
    ),
    "detect_dict_lookup_threshold": (
        "CD2, the reviewer's corpus at that round",
        "expression-valued threshold: a dict lookup",
    ),
    "detect_float_call_around_literal": (
        "CD2, the reviewer's corpus at that round",
        "expression-valued threshold: float(...) around the literal",
    ),
    "detect_function_local_float_threshold": (
        "CD2, the reviewer's corpus at that round",
        "a named float bound inside a function, not at module scope",
    ),
    "detect_keyword_only_default_tolerance": (
        "CD2, the reviewer's corpus at that round",
        "a keyword-only parameter default; only positional defaults are read",
    ),
    "detect_lambda_default_tolerance": (
        "CD2, the reviewer's corpus at that round",
        "a lambda's default, not a FunctionDef's",
    ),
    "detect_literal_times_scale": (
        "CD2, the reviewer's corpus at that round",
        "expression-valued threshold: literal times a scale",
    ),
    "detect_module_float_built_by_arithmetic": (
        "CD2, the reviewer's corpus at that round",
        "a module-level name bound to an EXPRESSION rather than a literal",
    ),
    "detect_negative_module_float_threshold": (
        "CD2, the reviewer's corpus at that round",
        "a module-level name bound to a negated literal",
    ),
    "detect_numpy_isclose_positional_rtol": (
        "CD2, the reviewer's corpus at that round",
        "a tolerance in a POSITIONAL slot, not a keyword",
    ),
    "detect_power_expression_threshold": (
        "CD2, the reviewer's corpus at that round",
        "expression-valued threshold: a power expression",
    ),
    "detect_round_to_decimals": (
        "CD2, the reviewer's corpus at that round",
        "expression-valued threshold: round(x, n)",
    ),
    "detect_tuple_unpacked_bounds": (
        "CD2, the reviewer's corpus at that round",
        "the threshold reaches the comparison through a tuple unpack",
    ),
    "detect_walrus_bound_threshold": (
        "CD2, the reviewer's corpus at that round",
        "the threshold is bound by a walrus and compared as a Name",
    ),
    "marker_in_lambda_default_same_stmt": (
        "CD2, the reviewer's corpus at that round",
        "the marker annotates a different sub-expression of the same statement",
    ),
    "marker_in_multiline_dict_literal_same_stmt": (
        "CD2, the reviewer's corpus at that round",
        "the marker annotates a different sub-expression of the same statement",
    ),
    "marker_in_multiline_starred_call_args": (
        "CD2, the reviewer's corpus at that round",
        "the marker annotates a different sub-expression of the same statement",
    ),
    "marker_on_bare_comment_line_inside_call": (
        "CD2, the reviewer's corpus at that round",
        "the marker annotates a different sub-expression of the same statement",
    ),
    "same_literal_twice_on_one_compare_node": (
        "CD2, the reviewer's corpus at that round",
        "one Compare node, two identical literals, one marker",
    ),
    "yoda_left_literal_with_marker_on_other_clause": (
        "CD2, the reviewer's corpus at that round",
        "one Compare node, two literals, one marker",
    ),
    # --- planted at `34bce16`, the thirty-eighth round: twenty shapes off
    # the axis the narrow rule is keyed on, thirteen of them escaping.
    "detect_ifexp_literal_branch": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_inline_dict_subscript_threshold": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_integer_iteration_threshold": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_literal_beside_a_LOCAL_name": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_literal_divided_by_literal": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_literal_in_abs_call": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_literal_in_float_call_AGAIN": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_literal_via_isclose_kwarg": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_numpy_minimum_candidate": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_product_of_two_literals": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_sorted_subscript_threshold": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_unary_PLUS_literal": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
    "detect_walrus_threshold": (
        "34bce16, the thirty-eighth round",
        "off the axis the narrow BinOp rule is keyed on",
    ),
}


def _entries() -> list[tuple[str, str, str]]:
    """`(id, expect, source)` for every corpus entry."""
    out: list[tuple[str, str, str]] = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.startswith("id="):
            continue
        fields = line.split(None, 3)
        got = {k: v for k, v in (f.split("=", 1) for f in fields[:3])}
        src = fields[3].split("=", 1)[1]
        out.append((got["id"], got["expect"], src.encode().decode("unicode_escape")))
    return out


ENTRIES = _entries()
ASSERTED = [e for e in ENTRIES if e[0] not in KNOWN_MISSES]


def _misses() -> set[str]:
    """The entries the shipped rule gets wrong, measured over the whole corpus."""
    import tempfile

    out: set[str] = set()
    with tempfile.TemporaryDirectory() as d:
        for name, expect, src in ENTRIES:
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
    kinds = {expect for _, expect, _ in ENTRIES}
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
        for name, expect, src in ENTRIES:
            f = Path(tmp) / f"test_{name}.py"
            f.write_text(src, encoding="utf-8")
            found = bool(offending(f))
            if (expect == "caught") != found:
                missed.add(name)
    return missed


def test_the_known_misses_are_exactly_these() -> None:
    """The escape golden, in both directions and with different meanings (CM4).

    A NEW ESCAPE is a name the scanner misses that this map does not carry.
    It may be allowed growth -- a reviewer planting a shape on a new axis --
    but it is never silent: adding it requires naming who planted it, which
    is the record that makes "the reach is measured" a true sentence.

    A SHAPE THAT STARTS BEING CAUGHT is the other direction, and it fails so
    the map cannot outlive what it describes.
    """
    missing = sorted(set(_measured_misses()) - set(KNOWN_MISSES))
    stale = sorted(set(KNOWN_MISSES) - set(_measured_misses()))
    assert not missing, (
        f"{len(missing)} shape(s) escape the scanner and are not recorded:\n  "
        + "\n  ".join(missing)
        + "\nIf a reviewer planted them, add each with their commit as its "
        "provenance -- growth is allowed and silence is not. If one of them "
        "was CAUGHT before, it is a regression and the scanner is what moves."
    )
    assert not stale, (
        f"{len(stale)} recorded miss(es) are now caught:\n  "
        + "\n  ".join(stale)
        + "\nDelete them from KNOWN_MISSES with a sentence saying what closed "
        "them; a golden that outlives its measurement is the shape this file "
        "exists to refuse."
    )
    for name, entry in KNOWN_MISSES.items():
        assert (
            isinstance(entry, tuple) and len(entry) == 2
        ), f"{name} carries {entry!r}; every entry is (provenance, reason)"
        assert entry[0].strip(), f"{name} names no commit or round that planted it"
