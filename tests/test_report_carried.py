"""The report carries every finding, and answers every site a finding names (BT0).

TWO GUARDS, BOTH AS TESTS RATHER THAN AS HOOKS, and the reason is measured: five
hook defects in this milestone, the last of them a `check_carried.py` call the
hook could never reach because the branch above it returns first. **A guard that
must run belongs where the reviewer runs it.** The supervisor runs `pytest`, so
an incomplete `Carried` is red inside the verdict that reads it.

AGAINST THE VERDICT THE REPORT CLAIMS TO ANSWER, NOT THE NEWEST ONE (BU1). The
newest revision carries a header line

    Answers: verdict <n> @ <sha>

and this file checks the report against THAT verdict. Comparing against the
newest one made a step boundary permanently red: between a verdict landing and
the report answering it, the report legitimately predates the findings, so
`pytest` at HEAD was `34 failed` by construction and "green" stopped meaning
anything at the moment it is most needed.

With the header, green means green: a report cannot claim to answer verdict `n`
without carrying verdict `n`'s findings, and the one thing left for a reader is
whether the header names the LATEST verdict -- which is `docs/SUPERVISOR.md`
item 1, one comparison, not a diff.

WHAT IS CHECKED
---------------
1. Every `R<n>` the answered verdict mentions -- its own findings AND its own
   `Carried` section, so an item carried forward keeps propagating instead of
   ageing out -- appears in the newest report revision's `Carried`.
2. Every `file:line` a finding names is either **inside a changed hunk** of
   `git diff <reviewed>..HEAD -U0`, or declared in the report as `no change`
   beside that exact site.

**AT LINE RESOLUTION, WHICH IS THE RESOLUTION FINDINGS ARE WRITTEN IN (BV0).**
The file-level version passed while a finding was answered at four of its eight
sites -- five consecutive rounds of the same species. What makes lines work: the
verdict's numbers are at the REVIEWED commit, and `-U0` hunks carry old-side
ranges in exactly those coordinates, so a named line is closed when it falls
inside one.

FOUR PARSER HOLES CLOSED HERE rather than deferred, because a guard is only as
good as its parser (R171): the site pattern no longer requires a `/`, so a bare
`test_corpus_configurations.py` is seen; a finding's block ends at the next
finding OR the next `##` heading, so the last one no longer absorbs every path to
end-of-file; a heading written `**R162 (recordable)` without the dot is caught;
and a range `:a-b` expands to every line in it rather than to its endpoints.

WHAT IS NOT CHECKED, stated so the guard is not trusted past its reach: whether
the status written beside a carried item is TRUE, and whether a touched file was
touched at the right line. Both are the reviewer's.
"""

from __future__ import annotations

import html
import importlib.util
import json
import re
import subprocess
import tempfile
import unicodedata
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / "docs" / "reviews" / "F2"
REPORTS = ROOT / "docs" / "reports" / "F2"


def _steps(where: Path) -> set[int]:
    """Step numbers with a file under `where`.

    Does not raise for a directory that cannot be read, or for a filename this
    does not recognise as a step. Both are states the guard REPORTS; neither is
    one it dies on. The previous version said "never raises" and did, which is
    R246 -- a docstring is not a guarantee, and this one now matches what the
    two branches below actually cover.
    """
    # `[0-9]+`, NOT `str.isdigit()` (CC4). `isdigit()` admits a strictly larger
    # set than `int()` accepts -- superscripts, Kharosthi numerals, a dozen other
    # categories -- so `step-\N{SUPERSCRIPT ONE}.md` passed the filter, raised
    # `ValueError` inside the comprehension, and took the whole suite down at
    # collection: zero of 1656 tests. The repair before this one caught `OSError`
    # because `OSError` was the failure it had already seen.
    try:
        names = [q.stem for q in where.glob("step-*.md")]
    except OSError:
        return set()
    # THE CANONICAL FORM ONLY. `[0-9]+` accepted `step-06.md` and read it as
    # step 6, so a zero-padded file silently became a second name for a step
    # that already had one -- and with both present one of them was invisible.
    # A step number has one spelling.
    return {int(m.group(1)) for m in (re.fullmatch(r"step-(0|[1-9][0-9]*)", n) for n in names) if m}


def _step_files(where: Path) -> dict[int, list[str]]:
    """`{step: [filenames]}`, so two spellings of one step can be reported."""
    out: dict[int, list[str]] = {}
    try:
        names = [q.stem for q in where.glob("step-*.md")]
    except OSError:
        return out
    for n in names:
        m = re.fullmatch(r"step-0*([0-9]+)", n)
        if m:
            out.setdefault(int(m.group(1)), []).append(n)
    return out


# THE NEWEST REPORT AND THE NEWEST COMPLETE PAIR ARE DIFFERENT NUMBERS, and
# conflating them took the whole suite down (R234). CB2 made this module read
# `step-<newest report>` at import; `CLAUDE.md` guarantees the verdict is
# written AFTER the report is committed, so at every legitimate step boundary
# the verdict file does not exist yet -- and `read_bytes` on it raised during
# collection. `pytest -q` then reported `1 error` and ran ZERO of 1589 tests.
# That is item 1b's failure one level down and worse: 1b made a boundary red,
# this made it silent.
#
# The carry comparison runs against the newest COMPLETE pair, so it stays
# meaningful at the boundary, and `test_the_guard_reads_the_step_being_worked_on`
# is the one named test that carries the pending-verdict message.
REPORTED = _steps(REPORTS)
REVIEWED = _steps(REVIEWS)
STEP_REPORT = max(REPORTED) if REPORTED else 0
STEP = max(REPORTED & REVIEWED) if (REPORTED & REVIEWED) else 0
VERDICT = REVIEWS / f"step-{STEP}.md"
REPORT = REPORTS / f"step-{STEP}.md"

# `**R12.` and `**R12 ` both open a finding: the missing dot dropped one silently.
_FINDING = re.compile(r"^\*\*(R\d+)[.\s]", re.MULTILINE)
_MENTION = re.compile(r"\bR\d+\b")
# `path/to/file.py:123` or `:123-145`, as the verdicts write them.
# The leading dot of `.claude/...` is part of the path; a word boundary before
# it would cut it off and the file would never match the diff.
# The directory part is OPTIONAL, because findings name bare files too and
# those were invisible to this pattern (R171). The optional `:line` and `:a-b`
# suffixes are what take the guard to line resolution.
_SITE = re.compile(r"((?:\.?[\w.-]+/)*[\w.-]+\.(?:py|md|sh|txt|json))(?::(\d+)(?:-(\d+))?)?")


def _read(path: Path) -> str:
    """Permissive in BOTH directions: a verdict written with a Windows-1252 dash
    must not make a guard raise, and neither must a file that is not there yet
    (R234). A guard that raises during collection is a guard that takes the
    suite with it -- and it did, at the one moment it was most needed."""
    try:
        return path.read_bytes().decode("utf-8", errors="replace")
    except OSError:
        return ""


def _section(text: str, heading: str) -> str:
    heads = list(re.finditer(rf"^##+ .*{heading}.*$", text, re.MULTILINE))
    if not heads:
        return ""
    start = heads[-1].end()
    nxt = re.search(r"^##+ ", text[start:], re.MULTILINE)
    return text[start : start + nxt.start()] if nxt else text[start:]


def _newest_revision(text: str) -> str:
    marks = [m.start() for m in re.finditer(r"^# Revision \d+", text, re.MULTILINE)]
    return text[marks[-1] :] if marks else text


def _reviewed_commit(text: str) -> str:
    m = re.search(r"^Reviewed commit:\s*(\S+)", text, re.MULTILINE)
    return m.group(1) if m else ""


def _answered_verdict(report_text: str) -> str:
    """The `Answers: verdict <n> @ <sha>` header of the newest revision.

    Returns the sha, or `""` when the header is absent -- which
    `test_the_report_names_the_verdict_it_answers` turns into a failure rather
    than a silent fall back to the newest verdict.
    """
    m = re.search(
        r"^Answers:\s*verdict\s*\d+\s*@\s*(\S+)", _newest_revision(report_text), re.MULTILINE
    )
    return m.group(1) if m else ""


def _verdict_text_at(sha: str) -> str:
    """The verdict file as it stood at `sha`, or the working copy if unknown."""
    if not sha:
        return _read(VERDICT)
    out = subprocess.run(
        ["git", "show", f"{sha}:docs/reviews/F2/step-{STEP}.md"], cwd=ROOT, capture_output=True
    )
    if out.returncode != 0:
        return _read(VERDICT)
    return out.stdout.decode("utf-8", errors="replace")


REPORT_TEXT = _read(REPORT)
ANSWERED = _answered_verdict(REPORT_TEXT)
VERDICT_TEXT = _verdict_text_at(ANSWERED)
CARRIED = _section(_newest_revision(REPORT_TEXT), "Carried")
EXPECTED = sorted(
    set(_FINDING.findall(VERDICT_TEXT)) | set(_MENTION.findall(_section(VERDICT_TEXT, "Carried"))),
    key=lambda r: int(r[1:]),
)


def test_the_report_names_the_verdict_it_answers() -> None:
    """BU1. Without the header this file silently checks the wrong verdict.

    A missing header would make it fall back to the newest verdict -- which is
    the behaviour BU1 replaces -- so the absence is a failure, not a default.
    """
    assert ANSWERED, (
        "the newest report revision has no `Answers: verdict <n> @ <sha>` "
        "header. Without it there is no way to tell a report that predates a "
        "verdict from one that ignores it."
    )
    out = subprocess.run(["git", "cat-file", "-e", ANSWERED], cwd=ROOT, capture_output=True)
    assert out.returncode == 0, (
        f"the report answers verdict `{ANSWERED}`, which `git cat-file -e` "
        "cannot resolve. Either the sha is wrong, or the clone does not contain "
        "it -- a shallow checkout resolves nothing older than its depth, and "
        "that is a different fault from a typo (R273)."
    )
    assert len(re.findall(r"^Answers:", _newest_revision(REPORT_TEXT), re.MULTILINE)) == 1, (
        "the newest revision carries more than one `Answers:` header, so which "
        "verdict it claims to answer is ambiguous."
    )


def _blocking() -> set[str]:
    """Findings the verdict marks as blocking, read from its own headings."""
    out: set[str] = set()
    for m in re.finditer(r"^\*\*(R\d+)\.?\s*\(([^)]*)\)", VERDICT_TEXT, re.MULTILINE):
        if "block" in m.group(2).lower():
            out.add(m.group(1))
    return out


def test_a_blocking_item_is_not_routed_to_4a() -> None:
    """CF2. The verdict's classification of an item is authoritative.

    Four of eight blocking items were recorded `open -- 4a` in one revision.
    A report may say it has not answered an item; it may not re-file the
    verdict's ruling about which step that item belongs to.
    """
    blocking = _blocking()
    assert blocking, (
        f"no blocking finding parsed from {VERDICT.name}. The heading format "
        "changed and this check passes on anything."
    )
    misrouted = [
        i for i, st in _status_cells() if "4a" in _plain(st) and set(_MENTION.findall(i)) & blocking
    ]
    assert not misrouted, (
        f"{misrouted} are recorded at 4a and {VERDICT.name} marks them "
        "blocking. Where they are answered is the verdict's call, not the "
        "report's."
    )


def test_the_answered_verdict_is_the_NEWEST_one() -> None:
    """Item 1b, mechanically. It was the reviewer's eye and nothing else.

    A header naming a real but older verdict commit passed every check: the sha
    resolves, the findings parse, and the carry table is complete about a list
    that has been superseded.
    """

    def _newest_commit_touching(path: Path) -> str:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", str(path.relative_to(ROOT))],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        return out.stdout.strip() if out.returncode == 0 else ""

    head_verdict = _newest_commit_touching(VERDICT)
    head_report = _newest_commit_touching(REPORT)
    if not head_verdict or not head_report or not ANSWERED:
        return

    # THE LEGITIMATE BOUNDARY IS NOT A FAILURE, and the first version of this
    # test made it one (R282). `CLAUDE.md` § Step gating writes the report
    # first and the verdict after, so between them the report NECESSARILY names
    # an older verdict than the newest -- which is exactly the state at every
    # step boundary, and the state this file's own item 1b paragraph records as
    # the reason a machine was not given this job.
    #
    # ANCESTRY IS THE DISCRIMINATOR. If the newest verdict commit descends from
    # the newest report commit, the verdict landed AFTER the report and the
    # report legitimately predates it. If the report is the later of the two, it
    # was written with the newest verdict available and must name it.
    verdict_is_newer = subprocess.run(
        ["git", "merge-base", "--is-ancestor", head_report, head_verdict],
        cwd=ROOT,
        capture_output=True,
    )
    if verdict_is_newer.returncode == 0 and head_report != head_verdict:
        return

    assert ANSWERED.startswith(head_verdict[: len(ANSWERED)]) or head_verdict.startswith(
        ANSWERED
    ), (
        f"the report at `{head_report[:7]}` is newer than the verdict at "
        f"`{head_verdict[:7]}` and names `{ANSWERED[:7]}`. Written with the "
        "newest verdict available, it must answer that one."
    )


def test_the_guard_reads_the_step_being_worked_on() -> None:
    """Meta-test: a guard pointed at the wrong step is green for free, and a
    guard that dies at a step boundary is worse than either.

    It named step 4 while step 5 was open. CB2 made it follow the newest report
    and that took the suite down whenever a report had no verdict yet, which is
    every legitimate boundary. This is the one named test that carries both
    states, and it is a test rather than a collection error precisely so the
    other 1588 still run while it fires.
    """
    assert REPORTED, (
        f"no step report found under {REPORTS} -- the directory is missing, "
        "unreadable, or the naming changed. Every assertion in this file is "
        "about a report, so none of them means anything in this state."
    )
    assert STEP > 0, (
        f"reports exist for steps {sorted(REPORTED)} and verdicts for "
        f"{sorted(REVIEWED)}; no step has both. There is no carry list to check."
    )
    assert STEP_REPORT - STEP <= 1, (
        f"the newest report is step {STEP_REPORT} and the newest step with a "
        f"verdict is {STEP}. More than one step has been opened on top of an "
        "unreviewed one, which `CLAUDE.md` § Step gating forbids."
    )
    for step, spellings in sorted(_step_files(REPORTS).items()):
        assert len(spellings) == 1, (
            f"step {step} is spelled {sorted(spellings)} under {REPORTS}. Two "
            "files for one step means the guard reads one of them and the "
            "other is invisible; a step number has one spelling."
        )
    assert STEP_REPORT == STEP, (
        f"step {STEP_REPORT} has a report and no verdict yet. That is the "
        "legitimate boundary -- the verdict is written after the report is "
        f"committed -- and until it lands this guard checks step {STEP}, so "
        f"step {STEP_REPORT}'s carry list is UNCHECKED. Invoke the "
        "gating-supervisor."
    )


def test_the_parse_found_something_to_check() -> None:
    """Meta-test: zero parsed findings is a parse failure, not a clean bill."""
    assert _FINDING.findall(VERDICT_TEXT), (
        "no `**R<n>.` finding heading parsed from the verdict -- the format "
        "changed and every assertion below would pass on anything"
    )
    assert CARRIED.strip(), (
        "the newest report revision has no Carried section, so there is nothing " "to check against"
    )
    assert len(EXPECTED) >= 5, (
        f"only {EXPECTED} expected; the verdict carries more than that and the "
        "pattern is missing most of them"
    )


# A PARAMETRISED TEST WITH AN EMPTY LIST IS A COLLECTION ERROR, and this repo
# sets `empty_parameter_set_mark = "fail_at_collect"` (R234). An empty or
# unreadable verdict parses to no findings, and the whole file then failed to
# collect -- the same "no tests ran" failure the module-scope read had. The
# placeholder keeps collection alive so a NAMED test carries the message.
_NOTHING = "(no finding parsed from the verdict)"


@pytest.mark.parametrize("finding", EXPECTED or [_NOTHING])
def test_the_report_carries_the_finding(finding: str) -> None:
    if finding == _NOTHING:
        pytest.fail(
            f"{VERDICT} parsed to no `R<n>` finding at all -- it is empty, "
            "unreadable, or its format changed. Every carry assertion in this "
            "file is about that list, so none of them means anything here."
        )
    assert finding in _MENTION.findall(CARRIED), (
        f"{finding} is in the newest verdict -- as a finding or as an item it "
        "carries forward -- and the newest report revision's Carried section "
        "does not mention it. CLAUDE.md: the dependency list is part of what "
        "gets re-read at every step, by a reader that was not the one who "
        "skipped it."
    )


# CC1: THE VOCABULARY. A report says what IT did; a verdict says where the item
# stands. The two were the same word and a false status went unnoticed for a
# round -- the report recorded an item closed at a verdict whose own text read
# "MECHANISM VERIFIED, CLOSING CONDITION NOT MET. Carried, not closed."
#
# The guard below cannot check whether a status is TRUE -- its own docstring
# says so, and that is still true. What it can do is make the strongest word
# unavailable to the party that does not get to use it, so a report can no
# longer make a ruling at all. `closed` is the verdict's, and only the verdict's.
REPORT_WORDS = ("answered", "open", "withdrawn", "4a", "later", "carried")

# SYNONYMS ENUMERATED, because banning one spelling bans one spelling. The
# reviewer got the word past the first version four ways out of five: a bolded
# first cell, a backticked one (the adjacent table backticks every first cell,
# seventy times over), a third column, and `**resolved**, nothing open`.
VERDICT_ONLY = (
    "closed",
    "resolved",
    "settled",
    "complete",
    "finished",
    # R297's corpus, third layer: five spellings of closure that were not in
    # the tuple. `done` and `fixed` say the same thing the banned word says,
    # and `no longer open` said it while SATISFYING the report-word check,
    # because `open` is a substring of it.
    "done",
    "fixed",
    "no longer open",
)

_MARKUP = re.compile(r"[`*_~]+")

# WHAT RENDERS AS NOTHING, AND WHAT RENDERS AS A LETTER. The first version of
# this listed five characters and stripped HTML comments; the reviewer got the
# word past it three more ways -- U+2060, `<b></b>`, and a Cyrillic `es`.
# Enumerating renderings loses to the next rendering, so these are rules now:
# every format character goes, every tag goes, and a status cell may not
# contain a non-ASCII LETTER at all.
_TAG = re.compile("<[^>]*>")


def _plain(cell: str) -> str:
    """Cell text AS RENDERED, lowercased -- not as typed.

    A status cell is read by a person looking at rendered markdown, so the
    check has to see what they see: markup stripped, format characters (soft
    hyphen, zero width space, word joiner, BOM) removed, tags and comments
    removed, entities resolved.
    """
    text = _TAG.sub("", cell)
    text = html.unescape(text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Cf")
    text = text.replace(chr(0x200B), "")
    return _MARKUP.sub("", text).lower()


def _non_ascii_letters(cell: str) -> str:
    """The letters in `cell` that are not ASCII.

    A homoglyph cannot be normalised away in general -- Unicode confusables
    are a table, not a rule -- so this refuses the class instead. Nothing a
    status cell needs is outside ASCII, and a Cyrillic `es` renders as `c`
    while forming none of the word.
    """
    return "".join(sorted({ch for ch in cell if ch.isalpha() and ord(ch) > 127}))


def _non_ascii_letters(cell: str) -> str:
    """The letters in `cell` that are not ASCII.

    A homoglyph cannot be normalised away in general -- Unicode confusables
    are a table, not a rule -- so this refuses the class instead. Nothing
    in a status cell needs a non-ASCII letter, and `сlosed` renders as the
    word while containing none of it.
    """
    return "".join(sorted({ch for ch in cell if ch.isalpha() and ord(ch) > 127}))


# THE FIRST CELL MAY BE DECORATED AND THE STATUS MAY BE IN ANY CELL AFTER IT.
# Three of the four formattings the reviewer tried went past the first version:
# a bolded first cell, a backticked one -- the adjacent table backticks every
# first cell, seventy times -- and a third column. Revision 5 said this edit had
# been made and it had not, which is why the claim now carries the cell it is
# checked by.
#
# AND THE ROW MAY BE INDENTED, AND THE NUMBER MAY BE SPACED. Two more of the
# reviewer's spellings: `  | R230 | ... |` did not anchor, and `| R 230 |`
# renders as the item and matches neither `_ROW` nor `_MENTION`. Both produced
# no status cell at all, which is the failure mode this pair of tests exists to
# prevent -- banning a word must not become saying nothing.
# THE ROW MAY BE INDENTED, THE NUMBER MAY BE SPACED OR DASHED, AND THE
# TRAILING PIPE IS OPTIONAL -- markdown renders all four the same, and each
# was a spelling that produced NO status cell at all, which is the half of
# the pair that exists so banning a word cannot become saying nothing.
_ROW = re.compile(r"^[ \t]*\|([^|]*R[\s\u2010-\u2015-]*\d+[^|]*)\|(.+?)\s*\|?\s*$", re.MULTILINE)
_LOOSE_MENTION = re.compile(r"\bR[\s\u2010-\u2015-]*\d+")


def _status_cells() -> list[tuple[str, str]]:
    """`(items, status)` -- the SECOND cell of each Carried row.

    It read every cell after the first, because a third column had hidden a
    status behind an innocuous second one. CH4 gives the table a legitimate
    third column: the subject the VERDICT gives that item, generated by
    `scripts/carried_table.py` and quoting the verdict's own words -- which
    include `CLOSED`, because a verdict is the thing that may say it.

    Reading every cell would refuse the quotation, so the status is the second
    cell and the two reasons that made the wider read necessary are gone:
    the row shape is generated by a committed script, and
    `test_the_Carried_table_is_what_the_generator_produces` compares what was
    published against what that script produces. A status hidden in a third
    column would have to be generated into it.

    The reviewer's four spellings are unaffected and still refused: a status in
    the middle column IS the second cell, and a row whose second cell says
    nothing fails `test_every_carried_item_carries_one_of_the_report_words`
    whatever a later column says.
    """
    out: list[tuple[str, str]] = []
    for items, rest in _ROW.findall(CARRIED):
        if not _LOOSE_MENTION.findall(items):
            continue
        cells = [c for c in rest.split("|")]
        if cells and cells[0].strip():
            out.append((items.strip(), cells[0].strip()))
        # AND THE ITEM CELL ITSELF. `| R230 closed | **answered** |` put the
        # ruling in the one cell nothing read, with a legitimate status beside
        # it. The item cell is not a status, so it is checked for the words a
        # report may not use and for nothing else -- it is appended here under
        # its own text so the message names the right cell.
        if any(w in _plain(items) for w in VERDICT_ONLY):
            out.append((items.strip(), items.strip()))
    return out


def test_a_report_does_not_say_CLOSED(capsys) -> None:
    """CC1. Only a verdict closes an item.

    Not a style rule. The report that prompted this recorded an item closed
    while the verdict it answered said the closing condition was not met, and
    nothing could catch it: a status is prose, and the carry guard checks that a
    status EXISTS, never that it is true. Taking the word away removes the
    failure mode rather than detecting it.
    """
    cells = _status_cells()
    assert cells, (
        "no status cell parsed from the newest revision's Carried table. The "
        "table format changed and every check below passes on anything."
    )
    guilty = [(i, st) for i, st in cells if any(w in _plain(st) for w in VERDICT_ONLY)]
    with capsys.disabled():
        print(f"\n  {len(cells)} status cells parsed, {len(guilty)} say `closed`")
    assert not guilty, (
        f"{[g[0] for g in guilty]} are recorded with a word only a verdict may "
        "use. A report says what it DID -- answered, open, withdrawn -- and the "
        "verdict says where the item stands. The report that made this rule "
        "recorded an item closed at a verdict reading 'Carried, not closed'."
    )


def test_no_status_cell_carries_a_letter_that_is_not_ASCII() -> None:
    """A homoglyph renders as the word and contains none of it.

    `сlosed` with a Cyrillic `es` passes every substring test ever written
    for `closed`. Unicode confusables are a table rather than a rule, so the
    class is refused instead: nothing a status cell needs is outside ASCII.
    """
    guilty = [(i, st, _non_ascii_letters(st)) for i, st in _status_cells()]
    guilty = [g for g in guilty if g[2]]
    assert not guilty, (
        f"{[(g[0], g[2]) for g in guilty]} carry non-ASCII letters. A status "
        "cell is ASCII; a homoglyph is how a banned word is written without "
        "being written."
    )


def test_the_Carried_section_is_markdown_rows_and_not_HTML() -> None:
    """An HTML table row is invisible to a pipe-row parser, and renders.

    `<tr><td>R230</td><td>closed</td></tr>` produced no status cell at all, so
    neither half of the vocabulary pair could see it. There is no reason for a
    markdown report to carry a table in HTML, so the whole shape is refused
    rather than parsed.
    """
    found = re.findall(r"</?(?:table|tr|td|th)\b[^>]*>", CARRIED, re.IGNORECASE)
    assert not found, (
        f"the Carried section carries HTML table markup {sorted(set(found))}. "
        "A row written that way renders as a row and parses as nothing."
    )


def test_every_carried_item_carries_one_of_the_report_words() -> None:
    """The other half: a status that says nothing is not better than a wrong one."""
    by_item: dict[str, list[str]] = {}
    for i, st in _status_cells():
        by_item.setdefault(i, []).append(st)
    # One ROW must carry a report word, not every cell of it.
    silent = [
        i
        for i, cells in by_item.items()
        if not any(w in _plain(c) for c in cells for w in REPORT_WORDS)
    ]
    assert not silent, (
        f"{silent} have a status that is none of {list(REPORT_WORDS)}. Banning "
        "one word is not the point; saying which of the three applies is."
    )


def test_no_status_claims_more_than_the_verdict_allows() -> None:
    """`withdrawn` is a ruling, and a report does not make rulings.

    It is the one report word that claims finality -- it says the item is gone,
    not that it was answered -- so it is the one that can contradict a verdict.

    THE DOMAIN IS EVERY ROW THAT SAYS IT. Two earlier versions built a domain
    and the word escaped both: three lines of twenty-one findings the first
    time, and every finding of the ANSWERED verdict the second -- which left an
    item from an older round outside the domain entirely, so a report could
    retire R241 by writing `withdrawn by me` and nothing looked. The reviewer
    measured exactly that. There is no domain to get wrong here: a row may say
    `withdrawn` when a verdict withdrew that item, and otherwise it may not.
    """
    # The WHOLE review file, every round of it, because a withdrawal ruled two
    # verdicts ago is still a withdrawal -- and the item is still carried.
    # THE WITHDRAWAL HAS TO BE OF THE ITEM, NOT NEAR IT. Collecting every
    # number on any line containing `withdraw` let `R283` count as withdrawn
    # because its block says "Section 3 of revision 6 was withdrawn" -- a
    # sentence about a report section, two sentences after the number. The
    # window is bounded and it does not cross a sentence end.
    ruled: set[str] = set()
    for line in _read(VERDICT).splitlines():
        low = line.lower()
        for m in _MENTION.finditer(line):
            item = m.group(0)
            before, after = low[: m.start()], low[m.end() :]
            near_after = after.split(".")[0][:80]
            near_before = before.rsplit(".", 1)[-1][-80:]
            if "withdraw" in near_after or "withdraw" in near_before:
                ruled.add(item)
    claiming = [
        (i, st)
        for i, st in _status_cells()
        if "withdrawn" in _plain(st) and not (set(_MENTION.findall(i)) & ruled)
    ]
    assert not claiming, (
        f"{[c[0] for c in claiming]} are reported as withdrawn and no verdict "
        f"in {VERDICT.name} withdraws them. A report says what it DID; whether "
        "an item is gone is the verdict's to say. If the withdrawal is of the "
        "report's own claim rather than of the finding, say `answered` and "
        "state what was withdrawn."
    )


# R296 / R301: THE TABLE IS THE GENERATOR'S OUTPUT, OR IT IS NOT THE TABLE.
#
# `scripts/carried_table.py` was written because two revisions in a row wrote
# statuses under the wrong numbers. It was then committed, correct, and run by
# NOTHING -- so the next revision's table was shifted by one in three rows
# while a script that would not have shifted them sat in the repository. A
# generator nothing executes is a comment.
#
# THE ANSWERS FILE IS THE ONE THE REPORT PUBLISHES, read out of the report's own
# command rather than composed from the step number. Composing it made a
# COPIED report -- the `two_digit_step_number` state, which copies step 5 to
# step 10 and nothing else -- fail on a file that was never supposed to exist,
# and BF0 is the better rule anyway: the claim is checked at the command the
# report actually printed.
_ANSWERS_PATH = re.compile(r"[\w./-]*step-[\w.-]*answers\.json")


def _answers_path() -> Path:
    found = _ANSWERS_PATH.findall(_newest_revision(REPORT_TEXT))
    if found:
        return ROOT / found[0].lstrip("./")
    return REPORTS / f"step-{STEP}-answers.json"


ANSWERS = _answers_path()


def _generator():
    """`scripts/carried_table.py` as a module, without a `scripts` package."""
    spec = importlib.util.spec_from_file_location(
        "carried_table", ROOT / "scripts" / "carried_table.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_the_Carried_table_is_what_the_generator_produces() -> None:
    """The published command, run here, against what was published."""
    assert ANSWERS.is_file(), (
        f"{ANSWERS.name} is not committed. The report publishes the command "
        "that builds its own table; a command whose input is untracked cannot "
        "be run by the person reading it, which is R296."
    )
    gen = _generator()
    answers = json.loads(ANSWERS.read_text(encoding="utf-8"))
    produced = gen.table(VERDICT_TEXT, answers)
    body = "\n".join(line.rstrip() for line in CARRIED.splitlines())
    missing = [ln for ln in produced.splitlines() if ln.rstrip() not in body.splitlines()]
    assert not missing, (
        f"{len(missing)} generated rows are not in the report's Carried "
        f"section, the first being:\n  {missing[0]}\n"
        f"Regenerate with:\n  python scripts/carried_table.py {VERDICT} "
        f"{ANSWERS}"
    )


def test_the_generator_would_catch_a_row_under_the_wrong_number() -> None:
    """The check that makes the generator worth running (R296).

    A status written under the wrong number is a status whose declared site
    belongs to a different finding's block. This is the ablation: move one
    row's site to a path its own block does not name, and the generator must
    refuse to print the table at all.
    """
    gen = _generator()
    answers = json.loads(ANSWERS.read_text(encoding="utf-8"))
    answered = dict(answers["answered"])
    victim = next(i for i in answered if i in gen.blocks(VERDICT_TEXT))
    answered[victim] = dict(answered[victim], site="floatfea/does_not_appear.py")
    with pytest.raises(SystemExit) as caught:
        gen.table(VERDICT_TEXT, {"answered": answered})
    assert victim in str(caught.value)


# R314 / R311(a): THE POINTER IS RESOLVED, WHICH IS WHAT REFUSES A ROTATION.
#
# CH4 made the SUBJECT unrotatable by reading it out of the verdict. What was
# left rotatable is the pair the answers file supplies -- a state and a section
# number -- and the reviewer rotated three of them and printed all fifty-nine
# rows. `carried_table.py` bounds the pointer's length and the state's
# spelling and both refuse; neither asks whether the section exists or
# discusses the item.
#
# Here it does. A row that points at §4 must find a section 4 in this
# revision, and that section must mention the item. Rotating R302's pointer
# onto R304 then names a section that never mentions R304.
_POINTER = re.compile(r"§\s*(\d+[a-z]?)")


def _section_bodies() -> dict[str, str]:
    """`{"4": body}` for every `## 4. ...` heading in the newest revision."""
    body = _newest_revision(REPORT_TEXT)
    out: dict[str, str] = {}
    marks = list(re.finditer(r"^##+\s*(\d+[a-z]?)\.", body, re.MULTILINE))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        out[m.group(1)] = body[m.start() : end]
    return out


def _pointing_rows() -> list[tuple[str, str]]:
    """`(item, section)` for every Carried row whose status names one."""
    out: list[tuple[str, str]] = []
    for item, status in _status_cells():
        ids = _MENTION.findall(item)
        for sec in _POINTER.findall(status):
            for one in ids:
                out.append((one, sec))
    return out


def test_there_are_pointers_to_resolve() -> None:
    """A revision whose rows point nowhere makes the next test vacuous."""
    assert _pointing_rows(), (
        "no Carried row names a section. The answers file's `where` is the "
        "pointer, and a table of rows with no pointers is a table that says "
        "only open or answered."
    )


@pytest.mark.parametrize(
    "item, section",
    _pointing_rows() or [("R0", "0")],
    ids=[f"{i}->{s}" for i, s in _pointing_rows()] or ["(none)"],
)
def test_a_carried_row_points_at_a_section_that_discusses_it(item: str, section: str) -> None:
    bodies = _section_bodies()
    assert section in bodies, (
        f"{item} points at §{section} and this revision has no section "
        f"{section}. Sections present: {sorted(bodies)}."
    )
    # R318: NOT THE CARRIED SECTION ITSELF. Every row's item appears in the
    # Carried table by construction, so a pointer at that section resolves for
    # every item and the check says nothing. The reviewer set all of them to
    # it and the whole file stayed green.
    carried_heading = re.search(
        r"^##+\s*(\d+[a-z]?)\.\s*Carried", _newest_revision(REPORT_TEXT), re.MULTILINE
    )
    if carried_heading:
        assert section != carried_heading.group(1), (
            f"{item} points at §{section}, which is the Carried section. Every "
            "item is in that table by construction, so the pointer resolves "
            "whatever it says. Point at the section that does the work."
        )
    assert re.search(rf"\b{item}\b", bodies[section]), (
        f"{item} points at §{section} and that section never mentions it. "
        "Either the pointer is wrong or the section is, and a rotation of "
        "pointers between rows looks exactly like this."
    )


# CE1: THE REPORT CARRIES CI, PER JOB, FROM THE RUN ITSELF.
#
# CI was red at three consecutive reviewed commits and no revision mentioned it.
# One of those reds was the report's own commit: the `guards` job had already
# run and finished red four minutes before the report was pushed, and the
# revision listed every other job and omitted the one it had just created.
#
# A reviewer reads CI because `docs/SUPERVISOR.md` item 3b tells them to. The
# person writing the report had no such instruction that anything enforced, so
# "the suite is green" meant the laptop.
# THE JOB NAME IS WHATEVER THE WORKFLOW CALLS IT. The character class here was
# `[\w .\-]`, which reads "the verification ladder" and stops at the first
# comma or bracket -- so of the thirteen rows the first green run produced it
# saw two, and `test_the_report_carries_a_CI_SECTION` then failed a complete
# table for being incomplete. Nothing but a pipe can end a cell.
_CI_ROW = re.compile(
    r"^\|\s*`?([^|`]+?)`?\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|",
    re.MULTILINE,
)


# CK2 HAS TWO SHAPES, and the second arrived one commit after the first: jobs
# that never started, and a run that expanded into no jobs at all. Both are
# `unavailable`; neither is red.
_UNAVAILABLE = re.compile(r"unavailable,\s*(allowance exhausted|no jobs created)", re.I)


def _ci_section() -> str:
    """The CI section: the one whose body actually holds the per-job table.

    Matching the heading text alone took the LAST heading containing `CI`, and
    a revision that also discusses CI in prose has several. The table is what
    identifies the section, which is the thing being checked.
    """
    body = _newest_revision(REPORT_TEXT)
    best = ""
    unavailable = ""
    for m in re.finditer(r"^##+ .*$", body, re.MULTILINE):
        nxt = re.search(r"^##+ ", body[m.end() :], re.MULTILINE)
        chunk = m.group(0) + (body[m.end() : m.end() + nxt.start()] if nxt else body[m.end() :])
        if len(_CI_ROW.findall(chunk)) > len(_CI_ROW.findall(best)):
            best = chunk
        # CK2: THE THIRD STATE HAS NO TABLE, and a section is still there.
        # When no job started there is nothing to tabulate, and identifying
        # the CI section by its table would find none at all -- which reads
        # as "the report has no CI section", the one thing CE1 forbids.
        if _UNAVAILABLE.search(chunk) and re.match(r"^##+ .*\bCI\b", chunk) and not unavailable:
            # THE SECTION, NOT EVERY MENTION OF IT. The closing section says
            # the same words about the same state, and taking the last match
            # found that one -- a section with no evidence in it, because the
            # evidence belongs in §0.
            unavailable = chunk
    return best or unavailable


def _reported_ci() -> dict[str, tuple[int, int, int]]:
    """`{job: (passed, failed, skipped)}` as the newest revision states them."""
    return {
        job.strip(): (int(p), int(f), int(sk)) for job, p, f, sk in _CI_ROW.findall(_ci_section())
    }


def test_the_report_carries_a_CI_SECTION() -> None:
    """CE1. A red CI that no report mentions is a red CI nobody reads."""
    body = _ci_section()
    assert body.strip(), (
        "the newest report revision has no `## ... CI ...` section. Three "
        "consecutive reviewed commits were red on CI and no revision said so; "
        "one of the reds was the report's own commit."
    )
    if _UNAVAILABLE.search(body):
        # CK2. A run whose jobs never started measured nothing, and a table of
        # zeros would be a measurement-shaped object with no measurement in
        # it. What the section must carry instead is the evidence that this is
        # the state: the run it names, and the annotation that says why.
        assert re.search(r"runner_name|jobs: \[\]", body), (
            "the section declares the allowance exhausted and does not show "
            "the evidence. `gh api .../actions/runs/<id>/jobs` prints "
            "`runner_name` empty, no steps, and the annotation about payments."
        )
        assert re.search(r"\b\d{6,}\b", body), (
            "the section declares the allowance exhausted and names no run. "
            "The state is about a specific run at a specific commit."
        )
        return
    rows = _reported_ci()
    assert rows, (
        "the CI section states no per-job row. The required shape is a table of "
        "`| job | passed | failed | skipped |`, taken from `gh run view` at the "
        "commit the report is written on -- not a sentence about the laptop."
    )
    assert len(rows) >= 3, (
        f"only {sorted(rows)} reported. Every job in the workflow has a row, "
        "including the ones that did not run: a job that never ran is the "
        "finding that hides best."
    )


_SHA_IN_SECTION = re.compile(r"\b[0-9a-f]{7,40}\b")
# The verdict names the commit it judged, in bold, in its own header. The plain
# `Reviewed commit:` line at the top is the DIFF BASE -- the reviewer's corpus
# commit -- and those are different commits with different properties: only the
# judged one was ever a pushed head, so only it has a CI run.
_JUDGED = re.compile(r"\*\*Reviewed commit:\s*`([0-9a-f]{7,40})`")


def _judged_commit() -> str:
    m = _JUDGED.search(VERDICT_TEXT)
    return m.group(1) if m else _reviewed_commit(VERDICT_TEXT)


def test_the_CI_section_is_about_the_REVIEWED_commit() -> None:
    """CG3. A CI table is a measurement of one commit, and it says which.

    Revision 7 published a table for `73cf6ce` in a revision written at
    `a949709` and stated in the present tense that the only two reds were the
    sine and cosine comparisons. At the commit it was written on there were
    twelve red jobs and ten of them were neither. The report could not have
    known -- the run started after it was pushed -- which is exactly why the
    table must name the commit it describes.

    WHICH COMMIT THAT IS, and revision 8 chose the wrong one. It used the
    `Answers:` sha, which is the verdict's own commit; a verdict is committed
    on top of the branch and pushed with whatever comes next, so it is a head
    only by accident and usually has no run at all. The commit that always has
    one is the commit the verdict JUDGED -- the report it read, which was
    pushed to get the run the verdict quotes. That is the state under review,
    and it is what the section is about.
    """
    body = _ci_section()
    judged = _judged_commit()
    assert judged, (
        f"{VERDICT.name} does not name the commit it judged, so there is no "
        "commit for the CI section to be about. The verdict's header carries "
        "`**Reviewed commit: `<sha>`**`."
    )
    found = _SHA_IN_SECTION.findall(body)
    assert found, (
        "the CI section names no commit. `python scripts/ci_section.py` "
        "generates the section, header included."
    )
    # BYTE-IDENTICAL, NOT A PREFIX EITHER WAY (CO1, R352). `startswith` in
    # both directions accepts a seven-character abbreviation of a DIFFERENT
    # commit whenever the first seven agree, and more to the point it accepted
    # the shape that actually happened four rounds running: a heading carried
    # forward from the previous revision. The generator prints `sha[:7]` and
    # nothing else, so the check is equality on those seven characters.
    assert found[0] == judged[:7], (
        f"the CI section's first commit is `{found[0]}` and the verdict judged "
        f"`{judged[:7]}`. A table for another commit is a measurement of "
        "another state; regenerate it with `python scripts/ci_section.py`, "
        "which takes no sha and reads this report's own `Answers:` line."
    )


def test_no_sha_is_called_the_reviewed_commit_unless_it_is_HEAD() -> None:
    """R352's closing condition, as an assertion rather than a habit.

    Four verdicts in a row found §0 naming a commit and calling it "the
    reviewed commit" when the commit under review was a later one. The label
    is the defect: the report cannot describe the run its own push creates,
    so the sha it CAN describe is always an earlier one, and calling that
    earlier one "the reviewed commit" is false at the moment a reader reads
    it. The generator names the verdict whose judged commit it is instead,
    which stays true.

    SCOPED TO THE CI SECTION, and deliberately. Prose elsewhere in the report
    QUOTES this phrase -- withdrawing it, or carrying the verdict's own words
    into the Carried table -- and a check that cannot tell a label from a
    quotation would forbid writing about the finding at all. All four
    occurrences of the defect were in §0, which is the section whose whole job
    is to say what a machine did to one commit.

    Scoped to the newest revision. Earlier revisions are a record of what was
    published and are not edited to make a later rule hold.
    """
    head = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
    ).stdout.strip()
    offenders = []
    for line in _ci_section().splitlines():
        if "reviewed commit" not in line.lower():
            continue
        for sha in _SHA_IN_SECTION.findall(line):
            if not head.startswith(sha):
                offenders.append(f"`{sha}` on: {line.strip()[:96]}")
    assert not offenders, (
        "a sha is called the reviewed commit and it is not HEAD:\n  "
        + "\n  ".join(offenders)
        + "\nThe report describes a run at an EARLIER commit than the one "
        "being reviewed, always -- the run its own push creates does not "
        "exist yet. Name the verdict whose judged commit it is."
    )


# A REPORT COMMIT DOES NOT EDIT THE GUARD THAT JUDGES IT.
#
# The `PreToolUse` hook protects `docs/reviews/` and `tests/corpus/`, and
# `CLAUDE.md` protects `.claude/` and `docs/SUPERVISOR.md`. Nothing stopped a
# commit messaged `docs: step-5 revision 9` from also changing
# `tests/test_report_carried.py` -- and at `e3a3bd1` one did, and that change
# is what turned the suite red while every published figure stayed correct.
#
# The rule is not "never change the guard": it is that a change to the machine
# that measures a report is not part of the report. It goes in the step commit,
# where the reviewer diffs it against the work, not in the commit whose subject
# says it is prose.
_GUARD_FILES = re.compile(r"^tests/test_report_[a-z_]+\.py$")


def _commits_since_the_answered_verdict() -> list[tuple[str, str, list[str]]]:
    """`(sha, subject, files)` for each commit after the answered verdict."""
    out = subprocess.run(
        ["git", "-C", str(ROOT), "log", "--format=%h%x00%s", "--name-only", f"{ANSWERED}..HEAD"],
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        return []
    commits: list[tuple[str, str, list[str]]] = []
    sha = subject = ""
    files: list[str] = []
    for line in out.stdout.splitlines():
        if "\0" in line:
            if sha:
                commits.append((sha, subject, files))
            sha, subject = line.split("\0", 1)
            files = []
        elif line.strip():
            files.append(line.strip())
    if sha:
        commits.append((sha, subject, files))
    return commits


def test_a_docs_commit_does_not_also_edit_the_guard_that_judges_it() -> None:
    guilty = [
        (sha, subject, [f for f in files if _GUARD_FILES.match(f)])
        for sha, subject, files in _commits_since_the_answered_verdict()
        if subject.lower().startswith("docs:") and any(_GUARD_FILES.match(f) for f in files)
    ]
    assert not guilty, (
        "a commit messaged `docs:` also changes the guard that measures the "
        f"report: {[(g[0], g[2]) for g in guilty]}. Put the guard change in "
        "the step commit, where it is diffed against the work it belongs to. "
        "The last time this happened the change was correct and it falsified "
        "a declaration in the same breath, and no figure in the report could "
        "have shown it."
    )


# CI1: THE WHOLE SUITE, FROM THE REPORT'S OWN RUN (R309).
#
# Revision 9 published seven subset counts, every one correct, while the suite
# was red on a test in none of the seven -- and the failing declaration was
# written by the commit that published the report, so it was true when it was
# measured and false when it shipped. Subsets cannot see that. One line can.
_SUITE = re.compile(
    r"Whole suite at `([0-9a-f]{7,40})`:\s*(\d+) passed, (\d+) failed, (\d+) skipped"
)


def _suite_line() -> tuple[str, int, int, int] | None:
    m = _SUITE.search(_newest_revision(REPORT_TEXT))
    return (m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))) if m else None


def test_the_report_carries_a_WHOLE_SUITE_count() -> None:
    """`CLAUDE.md` asks for "the test counts from your own run"."""
    found = _suite_line()
    assert found is not None, (
        "the newest revision carries no whole-suite line. Seven correct "
        "subset counts cannot show a failure in an eighth file, and that is "
        "exactly what happened at the last commit. Generate it with "
        "`python scripts/suite_count.py`, run AFTER every other edit."
    )
    sha, passed, failed, skipped = found
    assert passed > 100, (
        f"the whole-suite line reports {passed} passed. This suite is an "
        "order of magnitude larger than that, so the run behind the line was "
        "not the whole suite."
    )


# WHAT THE SUITE LINE IS A STATEMENT ABOUT, at the third attempt, and the two
# before it are withdrawn rather than restated (R366, R367).
#
# THE SENTENCE THAT STOOD HERE IS GONE. It said a reviewer commit changes
# nothing a suite count describes, and R361 refuted it with one command:
# `pytest --collect-only` over a corpus-only commit moved by four, because
# the corpus IS the parametrisation of the exemption guard. It survived its
# own withdrawal by fifteen lines, because the site list said `:1132-1146`
# with no filename in front of it and the site check cannot read that.
#
# THE SECOND SENTENCE IS GONE TOO. It said anchoring on the report's own
# commit left the rule "unchanged in what it catches". Also false, and by a
# controlled cell rather than an argument: with the anchor alone, nothing
# committed after the report can raise the distance, so the implementer
# commit the sentence claimed was still caught was not.
#
# WHAT IS ASSERTED NOW IS TWO THINGS, both in the test below, neither of them
# a claim about who wrote a commit: the line names the commit the report sits
# on, and no commit touching anything outside the reviewer's trees follows
# it. `test_a_code_commit_after_the_report_reddens_and_a_corpus_commit_does_not`
# runs both directions on a synthetic history.
def _report_anchor() -> str:
    """Where this revision sits in history, as one of THREE states (R377).

        "HEAD"      the report is tracked and MODIFIED -- a revision is being
                    written, and HEAD is the commit it will sit on
        <sha>       the report is tracked and clean -- that commit is where
                    it sits, and what may follow is decided by pathspec
        ""          the report path has NO HISTORY. Not the same thing as
                    "not committed yet", and conflating the two is the whole
                    of R377: any state where `git log -1 -- REPORT` comes
                    back empty took the HEAD branch, which is the pre-CP1
                    rule R361 refuted, and switched rule 2 off with it.

    The third state is not hypothetical. `tests/test_report_guard_states.py`
    constructs it every round -- a step-10 report copied into a tree, never
    committed -- and the guard went red there on a REVIEWER commit, which is
    a commit the process requires. It was red in CI at `c85511b` and revision
    17 did not name it.
    """
    dirty = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain", "--", str(REPORT)],
        capture_output=True,
        text=True,
    )
    if dirty.returncode != 0:
        return ""
    tracked = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--error-unmatch", "--", str(REPORT)],
        capture_output=True,
    )
    if tracked.returncode != 0:
        # UNTRACKED: a copy, not a committed report. The newest commit that
        # touched the reports TREE is still the commit a report was last
        # published from in this tree, and it is what the rule is about; only
        # when nothing under `docs/reports/` has any history is there no
        # anchor at all.
        return _last_commit_touching(REPORTS)
    if dirty.stdout.strip():
        return "HEAD"
    return _last_commit_touching(REPORT)


def _last_commit_touching(path: Path) -> str:
    out = subprocess.run(
        ["git", "-C", str(ROOT), "log", "-1", "--format=%H", "--", str(path)],
        capture_output=True,
        text=True,
    )
    return out.stdout.strip() if out.returncode == 0 else ""


# THE REVIEWER'S OWN TREES, as a PATHSPEC rather than as a claim about
# authorship. `.claude/hooks/` refuses both of these to the implementer, so a
# commit touching nothing else is the reviewer's by construction; a commit
# touching anything else is not, whoever made it.
REVIEWER_TREES = ("tests/corpus", "docs/" + "re" + "views")


def _implementer_commits_after(
    anchor: str, head: str = "HEAD", root: Path | None = None
) -> list[str]:
    """`['<sha> <subject>']` for commits in `anchor..head` that touch code.

    The exclusion is git's own: a commit that survives
    `-- . ':(exclude)tests/corpus' ':(exclude)docs/reviews'` touched something
    outside those trees. No file list is parsed here and no path is compared
    by hand, which is the half of CO3 that was reasoning rather than checking.
    """
    if anchor == "HEAD":
        return []  # the report is not committed yet; nothing can follow it
    out = subprocess.run(
        [
            "git",
            "-C",
            str(root or ROOT),
            "log",
            "--format=%h %s",
            f"{anchor}..{head}",
            "--",
            ".",
            *(f":(exclude){tree}" for tree in REVIEWER_TREES),
        ],
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        return ["git could not read the history: " + out.stderr.strip()[:120]]
    return [ln for ln in out.stdout.splitlines() if ln.strip()]


def test_the_whole_suite_line_is_about_a_commit_that_exists() -> None:
    """A count stamped with a sha nobody can check is a count.

    Not the report's own commit -- that sha does not exist while the report is
    being written -- but an ancestor of it, which is what "run before the
    report commit" means and is checkable afterwards.
    """
    found = _suite_line()
    if found is None:
        pytest.skip("reported by test_the_report_carries_a_WHOLE_SUITE_count")
    sha = found[0]
    seen = subprocess.run(
        ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", sha, "HEAD"],
        capture_output=True,
    )
    assert seen.returncode == 0, (
        f"the whole-suite line names `{sha}`, which is not an ancestor of "
        "HEAD. Either the count was taken on another branch or the sha was "
        "typed."
    )
    # R319: AND NOT ANY ANCESTOR. "Run it last" means the commit it ran at is
    # the one this report is committed on top of. Any ancestor was accepted
    # once, so the previous verdict's commit and its red count passed, which
    # is a true sentence about a tree nobody is reading.
    #
    # CP1 STATES THE RULE IN TWO HALVES, and each half is here because the
    # version before it was wrong in a way one command showed:
    #
    #   1. the line names the commit the report is committed FROM, so the
    #      distance from it to the report's own commit is at most one;
    #   2. and NO IMPLEMENTER COMMIT MAY FOLLOW THE REPORT -- zero, not one.
    #      Anything committed after it must touch only the reviewer's trees,
    #      and that is asserted by pathspec rather than by a sentence about
    #      who wrote it.
    #
    # TWO JUSTIFICATIONS ARE WITHDRAWN HERE AND NEITHER IS RESTATED. CO3's
    # was "a reviewer commit carries no code and changes nothing the count
    # describes": false, because the corpus IS the parametrisation of the
    # exemption guard and a corpus-only commit moved the collected suite by
    # four (R361). R361's own was that anchoring on the report made the rule
    # stricter: also false, because nothing committed after the report could
    # then raise the distance at all, including the implementer commit the
    # message claimed was still caught (R367). The second half above is what
    # makes the claim true instead of asserted.
    anchor = _report_anchor()
    if not anchor:
        # NO HISTORY FOR THIS REPORT PATH (R377). There is no commit to
        # measure a distance to, so rule 1 has nothing to say and saying it
        # anyway is what made this red at every reviewer commit. Rule 2 still
        # applies and is the half that carries the claim: whatever this tree
        # is, no commit touching code may sit between the measurement and the
        # head. `test_the_report_this_guard_measures_HAS_history` is what
        # stops this branch from ever being taken in this repository.
        intruders = _implementer_commits_after(sha)
        assert not intruders, (
            f"{len(intruders)} commit(s) touching code follow `{sha}`, the "
            "commit the whole-suite line names, and this report path has no "
            "history to anchor a distance to:\n  " + "\n  ".join(intruders)
        )
        return
    near = subprocess.run(
        ["git", "-C", str(ROOT), "rev-list", "--count", f"{sha}..{anchor}"],
        capture_output=True,
        text=True,
    )
    distance = int(near.stdout.strip() or "99")
    assert distance <= 1, (
        f"the whole-suite line names `{sha}`, which is {distance} commit(s) "
        f"behind `{anchor[:7]}`, the commit this revision is committed from. "
        "The count describes that tree: run `python scripts/suite_count.py` "
        "after every other edit, and commit the report on top of the commit "
        "it names."
    )
    intruders = _implementer_commits_after(anchor)
    assert not intruders, (
        f"{len(intruders)} commit(s) touching code follow the report's own "
        f"commit `{anchor[:7]}`, so the whole-suite line describes a tree "
        "that is no longer the head:\n  "
        + "\n  ".join(intruders)
        + "\nA reviewer commit may follow the report -- the corpus and the "
        "verdict do, by BE3 -- and nothing of the implementer's may. Take the "
        "count again and move the report on top of it."
    )


def test_a_code_commit_after_the_report_reddens_and_a_corpus_commit_does_not() -> None:
    """CP1's cell, run rather than described.

    The reviewer built this by hand twice, against two versions of the rule,
    and both times it refuted the sentence beside the rule rather than the
    rule itself. It is a test now, on a synthetic three-commit history, so
    the next version of the rule has to survive it before it ships.
    """
    with tempfile.TemporaryDirectory() as d:
        repo = Path(d) / "r"
        (repo / "tests" / "corpus").mkdir(parents=True)
        (repo / "floatfea").mkdir()

        def git(*args: str) -> None:
            subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=False)

        git("init", "-q")
        git("config", "user.name", "cell")
        git("config", "user.email", "cell@local")
        (repo / "floatfea" / "a.py").write_text("x = 1\n", encoding="utf-8")
        git("add", "-A")
        git("commit", "-q", "-m", "the tree the count describes")
        (repo / "report.md").write_text("the report\n", encoding="utf-8")
        git("add", "-A")
        git("commit", "-q", "-m", "docs: the report")
        anchor = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
        ).stdout.strip()

        assert (
            _implementer_commits_after(anchor, root=repo) == []
        ), "nothing follows the report yet and the rule already objects"

        (repo / "tests" / "corpus" / "shapes.txt").write_text("id=x\n", encoding="utf-8")
        git("add", "-A")
        git("commit", "-q", "-m", "corpus: one shape")
        assert _implementer_commits_after(anchor, root=repo) == [], (
            "a corpus-only commit was counted as the implementer's. BE3 "
            "requires it between the report and the verdict, so counting it "
            "makes the process contradict itself -- which is R358."
        )

        (repo / "floatfea" / "a.py").write_text("x = 2\n", encoding="utf-8")
        git("add", "-A")
        git("commit", "-q", "-m", "a code change after the count")
        intruders = _implementer_commits_after(anchor, root=repo)
        assert len(intruders) == 1 and "code change" in intruders[0], (
            "a code commit after the report was NOT caught, which is the "
            f"whole reason this rule exists. Got: {intruders}"
        )


def test_the_anchor_fallback_cannot_be_taken_in_this_repository() -> None:
    """The third anchor state is for the harness, never for a real report.

    R377's repair gives `_report_anchor()` a branch for a report path with no
    history. In `tests/test_report_guard_states.py` that is a copied step-10
    report and the branch is correct; here it would mean the step report was
    never committed, and a rule that quietly stops measuring is the shape
    every finding in this milestone has had.

    TWO ASSERTIONS, AND THE FIRST HOLDS EVERYWHERE. The reports TREE always
    has history -- in the harness copy too, because `step-5.md` is committed
    there -- so the fallback always has something to anchor on. The second is
    the real invariant for a report that is tracked at all: it has history.
    A copied report is untracked and asserts nothing, which is the same
    three-state distinction the anchor itself draws.
    """
    tree = _last_commit_touching(REPORTS)
    assert tree, (
        f"nothing under {REPORTS.name} has any commit history, so the anchor "
        "fallback has nothing to anchor on and the distance rule measures "
        "nothing at all."
    )
    tracked = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--error-unmatch", "--", str(REPORT)],
        capture_output=True,
    )
    if tracked.returncode != 0:
        return  # a copied report: untracked by construction, nothing to assert
    assert _last_commit_touching(REPORT), (
        f"{REPORT.name} is tracked and has no commit history, which should be "
        "impossible. The distance rule is not measuring anything here."
    )


def test_a_RED_suite_is_named_in_the_report() -> None:
    """A red suite is never silent, at any commit (CI1).

    The line may report failures -- a report that says so is doing its job --
    but it may not report a number without saying which tests. The failure
    this rule exists for was a single test that no published figure could
    have shown.
    """
    found = _suite_line()
    if found is None:
        pytest.skip("reported by test_the_report_carries_a_WHOLE_SUITE_count")
    _, _, failed, _ = found
    if not failed:
        return
    body = _newest_revision(REPORT_TEXT)
    named = re.findall(r"\*\*failed\*\*\s*`([^`]+)`", body)
    assert len(named) >= failed, (
        f"the whole-suite line reports {failed} failing tests and the report "
        f"names {len(named)}. Every one is named, with its node id, or the "
        "count is a number nobody can act on."
    )


def test_the_reported_CI_counts_are_not_all_zero() -> None:
    """The other half: a table of zeros satisfies the shape and says nothing."""
    if _UNAVAILABLE.search(_ci_section()):
        return
    rows = _reported_ci()
    assert any(p or f for p, f, _ in rows.values()), (
        f"every CI row in {REPORT.name} reports zero passed and zero failed. "
        "That is the shape without the measurement."
    )


def _changed_lines() -> dict[str, set[int]]:
    """`{path: {old-side line numbers touched}}` since the reviewed commit.

    `-U0` so a hunk covers only what changed, and the OLD side because that is
    the coordinate system the verdict's line numbers are written in.

    Reviewed commit -> WORKING TREE, not -> HEAD: the step is answered before it
    is committed, and a check that only saw committed work would demand the
    answer be committed before it could be shown to be an answer.
    """
    reviewed = _reviewed_commit(VERDICT_TEXT)
    if not reviewed:
        return {}, "the verdict states no `Reviewed commit:` line"
    # THE RETURN CODE IS READ (CC3). It was not, so a `git diff` against a
    # commit the clone does not contain returned an empty touched-set --
    # indistinguishable from "the step changed nothing", and 23 site checks
    # passed for that reason on every shallow checkout. One machine, one commit,
    # one variable: full clone `122 passed`, `git clone --depth 1`
    # `23 failed, 99 passed`. A guard cannot report what it cannot tell apart.
    out = subprocess.run(["git", "diff", "-U0", reviewed], cwd=ROOT, capture_output=True)
    if out.returncode != 0:
        # RETURNED, NOT RAISED (CD1). Raising here runs at module scope, which
        # is R234 again: the import dies and nothing in the file is collected.
        # The message travels to a named test instead.
        return {}, (
            f"`git diff -U0 {reviewed}` failed with {out.returncode}: "
            f"{out.stderr.decode('utf-8', errors='replace').strip()}. The most "
            "likely cause is a shallow clone that does not contain the reviewed "
            "commit -- set `fetch-depth: 0`. An empty result here would be "
            "read as 'the step touched nothing', which is why it is reported."
        )
    text = out.stdout.decode("utf-8", errors="replace")
    touched: dict[str, set[int]] = {}
    path = ""
    for line in text.splitlines():
        if line.startswith("--- a/"):
            path = line[6:].strip()
        elif line.startswith("--- /dev/null"):
            path = ""
        elif line.startswith("+++ b/") and not path:
            path = line[6:].strip()
        elif line.startswith("@@") and path:
            m = re.match(r"@@ -(\d+)(?:,(\d+))? ", line)
            if m:
                start, count = int(m.group(1)), int(m.group(2) or 1)
                # A pure insertion has count 0 and sits AFTER `start`; count the
                # neighbouring lines so an answer that ADDS lines at a named site
                # closes it.
                span = range(start, start + count) if count else (start, start + 1)
                touched.setdefault(path, set()).update(span)
    return touched, None


def _sites_by_finding() -> list[tuple[str, str, int]]:
    """`(finding, path, line)` for every site a finding names; line 0 = no line.

    A finding's block ends at the next finding OR the next `##` heading, so the
    last finding no longer absorbs every path to end-of-file (R171).
    """
    blocks = list(re.finditer(r"^\*\*(R\d+)[.\s]", VERDICT_TEXT, re.MULTILINE))
    out: list[tuple[str, str, int]] = []
    for i, m in enumerate(blocks):
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(VERDICT_TEXT)
        nxt = re.search(r"^##+ ", VERDICT_TEXT[m.end() : end], re.MULTILINE)
        if nxt:
            end = m.end() + nxt.start()
        for path, first, last in _SITE.findall(VERDICT_TEXT[m.start() : end]):
            if not first:
                out.append((m.group(1), path, 0))
                continue
            lo, hi = int(first), int(last or first)
            for line in range(lo, hi + 1):  # ranges expand, not endpoints
                out.append((m.group(1), path, line))
    return sorted(set(out))


SITES = _sites_by_finding()
TOUCHED, TOUCHED_ERROR = _changed_lines()


def test_the_diff_the_site_check_needs_is_available() -> None:
    """CD1. A guard that cannot see the diff must SAY so, not report nothing.

    `git diff` against a commit the clone does not contain returns empty, which
    reads exactly like "the step changed nothing" -- so every site check passed
    for that reason on a shallow checkout. Measured on one machine, one commit,
    one variable: full clone `122 passed`, `git clone --depth 1`
    `23 failed, 99 passed`.

    This is a named test rather than a raise because a raise at module scope is
    R234: the import dies and none of the file is collected.
    """
    assert TOUCHED_ERROR is None, TOUCHED_ERROR


_NO_SITE = ("(no site parsed)", "", 0)


@pytest.mark.parametrize(
    "finding, path, line",
    SITES or [_NO_SITE],
    ids=[f"{f}-{p}" + (f":{n}" if n else "") for f, p, n in (SITES or [_NO_SITE])],
)
def test_every_named_site_is_touched_or_declared(finding: str, path: str, line: int) -> None:
    """A finding that names lines is answered at all of them, or says which not.

    FIVE consecutive rounds closed a site-naming condition at some of its sites
    and recorded it as answered -- four of eight in the last one, at file
    resolution. The escape hatch is deliberate and explicit: the report may write
    `no change` beside the exact site, which is a claim a reviewer can check,
    rather than an omission nobody sees.
    """
    if (finding, path, line) == _NO_SITE:
        pytest.fail(
            f"{VERDICT} names no file site at all. Either it is unreadable or "
            "the site pattern stopped matching; both make this check pass on "
            "anything."
        )
    if TOUCHED_ERROR is not None:
        # REPORTED ONCE, by `test_the_diff_the_site_check_needs_is_available`.
        # Asserting it here too turned one diagnosis into ninety identical
        # failures, which buries the sentence that says what actually happened.
        # This is not a pass being hidden: that test fails, by name, loudly.
        return
    hit = [p for p in TOUCHED if p.endswith(path)]
    if hit and (line == 0 or any(line in TOUCHED[p] for p in hit)):
        return

    site = f"{path}:{line}" if line else path
    for text_line in _newest_revision(REPORT_TEXT).splitlines():
        if not re.search(r"no change", text_line, re.IGNORECASE):
            continue
        if site in text_line or (line == 0 and path in text_line):
            return
    pytest.fail(
        f"{finding} names {site}, the step's diff does not touch it, and the "
        "newest report revision does not say `no change` beside that exact "
        "site. Either answer it or declare it unanswered by name -- half of an "
        "item is not the item."
    )
