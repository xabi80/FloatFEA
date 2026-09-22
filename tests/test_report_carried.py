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


_PLAN = ROOT / "docs" / "milestones" / "F2.md"
_STEP_LINE = re.compile(r"<!--\s*step-under-execution:\s*(\d+)\s*-->")


def _plan_step() -> int:
    """The step the plan says is under execution, or 0 if it says nothing.

    RETURNS 0 rather than raising: this runs at import, and a raise at import
    is R234 -- the module fails to collect and the suite reports one error
    instead of running. `test_the_plan_names_the_step_under_execution` is the
    named test that carries the message.
    """
    try:
        m = _STEP_LINE.search(_PLAN.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return 0
    return int(m.group(1)) if m else 0


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

# DB2: THE STEP COMES FROM THE PLAN, and the two paths below are resolved
# separately because they answer different questions.
#
#   REPORT  -- the report of the step under execution. It carries the whole-
#              suite line and the generated CI sections, and it is the file
#              a reader means by "the report".
#   VERDICT -- the file the newest verdict is IN. At a step boundary that is
#              the PREVIOUS step's file: the step-6 report answers verdict 54,
#              which the reviewer wrote into the step-5 verdict file. Taking
#              this from the plan's number would look for a file that does not
#              exist and call it a missing verdict.
#
# Conflating the two is R234 one level up: `max(REPORTED & REVIEWED)` pinned
# BOTH to the newest complete pair, so a report for the next step could never
# be the one checked, and the boundary could not be left.
_PLAN_STEP = _plan_step()
_PAIRED = max(REPORTED & REVIEWED) if (REPORTED & REVIEWED) else 0
# THE LATER OF THE TWO, because they disagree in opposite directions.
#
#   plan ahead of the pair -- the boundary DB2 exists to let us leave: the next
#     step has a report and its verdict is not written yet.
#   pair ahead of the plan -- the plan line was not advanced, or a synthetic
#     state injected a newer complete pair without touching the plan, which is
#     what the guard-state harness does. Reading the plan there would take step
#     5 while a complete step-10 pair sits in the tree.
#
# The second case is not hypothetical: the first version of this took the plan
# whenever its step had a report, and the harness reddened on
# `two_digit_step_number` -- injected report AND verdict for step 10, plan line
# untouched at 5 -- which is the state the harness exists to inject.
STEP = max(_PLAN_STEP if _PLAN_STEP in REPORTED else 0, _PAIRED)
VERDICT = REVIEWS / f"step-{max(REVIEWED)}.md" if REVIEWED else REVIEWS / "step-0.md"
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


def test_the_plan_names_the_step_under_execution() -> None:
    """DB2. `_plan_step` returns 0 rather than raising, so this carries it.

    A raise at import is R234: the module does not collect and `pytest -q`
    reports one error having run none of the file.
    """
    assert _plan_step() > 0, (
        f"{_PLAN} carries no `<!-- step-under-execution: N -->` line, so the "
        "guards fell back to the newest complete report/verdict pair. That is "
        "the behaviour DB2 replaced, and it makes the step boundary "
        "permanently red."
    )
    assert _plan_step() in REPORTED, (
        f"the plan says step {_plan_step()} is under execution and there is no "
        f"`step-{_plan_step()}.md` under {REPORTS}. The line is advanced in the "
        "commit that adds the next step's report, never before it."
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


# CU3 / R412: A RUN IS NEVER NAMED WITHOUT ITS OVERALL CONCLUSION.
#
# Twice in two rounds a report described a CI run job by job, every sentence
# true, and left out the one word that says what the run DID. The second time
# the run had concluded `failure` while the three job groups the report named
# were all green -- the failing job was a fourth one the sentence did not
# reach. Per-job lines cannot carry this: a run can conclude `failure` with
# every job it names green, which is exactly the shape that got past both
# rounds.
#
# `scripts/ci_section.py` now puts the conclusion in the heading and on the
# leg table's first line. These two make it a build failure rather than a
# habit: the first for any run id anywhere in the revision, the second for the
# specific shape -- a green-looking job table under a run that failed.
# NOT `\\b...\\b`: a word boundary sits between `.` and a digit, so the
# first version matched `526231496888` inside `199.526231496888` and asked
# for a conclusion on a tolerance value. A run id is not part of a longer
# number, and this guard caught its own author on its first report.
# THE PATTERN, AT ITS THIRD VERSION, AND THE REVIEWER MEASURED THE SECOND.
#
# `\b...\b` matched `526231496888` inside `199.526231496888` and asked for a
# conclusion on a tolerance value. Tightening both sides to reject a digit or
# a DOT then rejected the most ordinary way anyone writes a run id -- at the
# end of a sentence. `tests/corpus/report_ci_section.txt` measures that
# version at **2 of 7** unseen shapes caught (R429). The misses were a
# trailing full stop, the same inside a list item, a 13-digit id, thousands
# separators, and the word `conclusion` appearing only in the COMMAND.
#
#   right side  a digit is still rejected, and so is `.` FOLLOWED BY A DIGIT
#               -- which is what `199.526231496888` is -- but a sentence-final
#               full stop is not a decimal point;
#   left side   unchanged;
#   length      `9,` and not `9,12`: GitHub run ids are not bounded at twelve
#               and the corpus plants a thirteen-digit one;
#   commas      stripped between digits before the scan, so `35,479,925,335`
#               is one id rather than four short numbers.
_RUN_ID = re.compile(r"(?<![\d.])(\d{9,})(?!\d)")

# THE RIGHT-HAND DOT GUARD IS GONE (R444). It was there to keep
# `526231496888` inside `199.526231496888` out, and the LEFT lookbehind
# already does that -- the digits inside a decimal have a dot before them.
# What the right-hand guard did instead was miss a run id followed by a
# decimal: `run 35479925335.0 seconds long` was never seen.
#
# SEPARATORS ARE JOINED ONLY AFTER THE WORD `run` (R444). The first version
# stripped commas between digits anywhere, which joined a plain list --
# `100,200,300,400` -- into a twelve-digit id and demanded a conclusion for
# it. A grouped id is only a grouped id where someone wrote `run` in front of
# it; a bare list of numbers is a list.
_GROUPED = re.compile(r"(?i)\brun\s+(\d[\d,\s_\u2013-]{6,}\d)")


def _joined(text: str) -> str:
    """`run 35,479,925,335` -> `run 35479925335`, and nothing else joined."""

    def fix(m: re.Match[str]) -> str:
        return m.group(0)[: m.start(1) - m.start(0)] + re.sub(r"[,\s_\u2013-]", "", m.group(1))

    return _GROUPED.sub(fix, text)


# A CONCLUSION IS A RESULT BESIDE THE WORD, ON A LINE THAT IS NOT A COMMAND
# (CW3, R444). The previous version matched a bare VALUE anywhere in the
# paragraph, which the reviewer refuted four ways: the value inside a `--jq`
# filter, inside a `grep` needle, inside a negation, and an unrelated
# `skipped` about a different job rescuing a naked run id.
_VALUE = (
    r"success|failure|cancelled|canceled|skipped|timed_out|neutral|stale"
    r"|action_required|startup_failure"
)
_CONCLUSION = re.compile(rf"conclusion[^A-Za-z0-9]{{0,12}}\b({_VALUE})\b", re.I)
_COMMANDISH = re.compile(r"(?:\bgh\s|--json|--jq|--log|\bgrep\b|\bjq\b|\|)")

# THE HISTORY OF THIS PATTERN, in one place, because it has been wrong three
# ways. `conclusion\s+\**([A-Za-z_]+)` was satisfied by the `gh` flag with the
# output never pasted -- R412's own shape. A bare VALUE anywhere replaced it
# and was satisfied by a `--jq` filter, a `grep` needle, a negation, and an
# unrelated `skipped` about a different job (R444). What is required now is
# the WORD and the VALUE together, on a line that is not a command.


def runs_without_a_conclusion(text: str) -> list[tuple[str, str]]:
    """`(run id, the paragraph)` for every run named with no result beside it.

    A FUNCTION rather than a loop inside the test, so the controls below can
    run it on text that is not this report. R430: a guard that cannot be shown
    to fail is the thing this repository keeps rediscovering.
    """
    naked = []
    for para in _paragraphs(text):
        flat = _joined(para)
        hits = list(_RUN_ID.finditer(flat))
        # PER RUN, NOT PER PARAGRAPH (R457). One conclusion anywhere in a
        # paragraph satisfied every id in it, so "Run A had conclusion
        # success. Run B is also named here." passed -- the R412 shape with a
        # neighbour. Each id owns the text from itself to the next id.
        for k, m in enumerate(hits):
            end = hits[k + 1].start() if k + 1 < len(hits) else len(flat)
            if not _stated_in(flat[m.start() : end]):
                naked.append((m.group(1), " ".join(para.split())[:90]))
    return naked


def _stated_in(segment: str) -> bool:
    """Is a RUN's conclusion stated here, on text that is not a command?

    THE SEGMENT IS FLATTENED BEFORE THE SEARCH, not filtered line by line
    (R457). A value that wrapped to the next line was refused, because the
    word was on one line and the result on the next. Command text is removed
    from each line rather than the whole line being discarded, so a genuine
    result pasted after the command that produced it still counts.

    WHAT THIS DOES NOT DISTINGUISH, stated because the reviewer asked for a
    rule that says which: a JOB's conclusion from the RUN's. "the ladder job
    conclusion was success" satisfies it. The generated sections make that
    moot -- they print the run's conclusion from `gh run view --json
    conclusion`, and CX0 forbids a run id anywhere else -- so the
    distinction has no site left to matter at.
    """
    kept = []
    for line in segment.splitlines():
        tail = line
        for marker in ("->", " out ", "	out "):
            if marker in tail:
                tail = tail.split(marker, 1)[1]
                break
        else:
            if _COMMANDISH.search(tail):
                continue
        kept.append(tail)
    return bool(_CONCLUSION.search(" ".join(kept)))


def a_green_table_under_a_failed_run(text: str) -> str | None:
    """The reason this CI section reads green while its run did not, or None.

    Also a function for the same reason. On a report whose section 0 concludes
    `success` it returns None, which at `d8ac843` meant the shipped test
    asserted nothing at all and had no state in
    `tests/test_report_guard_states.py` (R430).
    """
    if not text.strip() or _UNAVAILABLE.search(text):
        return None
    stated = [c.lower() for c in _CONCLUSION.findall(text)]
    if not stated:
        return "the CI section states no overall conclusion"
    if all(c in ("success", "skipped") for c in stated):
        return None
    red = re.search(r"(\d+)\s+jobs?,\s*(\d+)\s+not green", text)
    if not red:
        return f"conclusion {stated} and no `N jobs, M not green` line"
    if int(red.group(2)) == 0 and _GREEN_UNDER_RED not in text:
        return (
            f"conclusion {stated} with {red.group(1)} jobs and none not "
            f"green, and no `{_GREEN_UNDER_RED}`"
        )
    return None


# The literal a report writes to say "yes, this run failed and the jobs I show
# are green; here is why". Nothing infers it, exactly like `no change` in the
# untouched-sites table.
_GREEN_UNDER_RED = "GREEN JOBS UNDER A FAILED RUN"


def _paragraphs(text: str) -> list[str]:
    return [p for p in re.split(r"\n\s*\n", text) if p.strip()]


def _zero_sections() -> str:
    """Every `## 0...` section of the newest revision, joined.

    THE GENERATED ONES. Section 0 is `python scripts/ci_section.py` and
    section 0a is `--rounds`; between them they are the only place a run's
    outcome is allowed to appear (CX0).
    """
    body = _newest_revision(REPORT_TEXT)
    out = []
    for m in re.finditer(r"^##+ 0[a-z]?\.", body, re.MULTILINE):
        nxt = re.search(r"^##+ ", body[m.end() :], re.MULTILINE)
        out.append(body[m.start() : m.end() + nxt.start()] if nxt else body[m.start() :])
    return "\n".join(out)


# THE MARKER THE GENERATOR WRITES, not a heading number (CY3, R463). Keying
# on `## 0<letter>.` made the exemption a title anyone could choose: a `## 0b.`
# of prose was outside every CI rule, and section 11's hand-written reason
# column was inside the exemption for free. A generator emits this line; a
# hand-written section that claims it is claiming its output is reproducible,
# which is the next check along.
# `\s*$` AND NOT `$`: the report is CRLF and `$` stops before the `\n`,
# so the trailing `\r` made every marker invisible and the split returned
# nothing -- which read as "no generated section" rather than as an error.
_GENERATED_MARK = re.compile(r"^<!-- generated: (\S+) -->\s*$", re.MULTILINE)


def _generated(body: str) -> str:
    """Every section this report does not write by hand.

    Sections 0 and 0a are `scripts/ci_section.py`; 11 and 12 are
    `untouched_sites.py` and `carried_table.py`, both of which quote the
    VERDICT -- and a verdict naming a run id would otherwise make the
    report's own rule fire on the reviewer's words.
    """
    out = []
    for m in _GENERATED_MARK.finditer(body):
        head = body.rfind("\n## ", 0, m.start())
        start = head + 1 if head != -1 else m.start()
        nxt = re.search(r"^##+ ", body[m.end() :], re.MULTILINE)
        out.append((start, m.end() + nxt.start() if nxt else len(body)))
    return out


def _generated_text(body: str) -> str:
    return "\n".join(body[a:b] for a, b in _generated(body))


def _hand_written(body: str) -> str:
    """The revision with every generated section cut out, BY INDEX.

    Not by `replace` (CX0): the joined sections and the body differ in
    their line endings, so removing one from the other removed nothing
    and the guards below read the generated tables as prose.
    """
    keep, last = [], 0
    for a, b in _generated(body):
        keep.append(body[last:a])
        last = b
    keep.append(body[last:])
    return "".join(keep)


def test_no_RUN_ID_appears_outside_THE_GENERATED_CI_SECTIONS() -> None:
    """R449, mechanically. A run's outcome is generated or it is not written.

    Section 0a was prose. It named three runs and got one of them wrong in
    both halves -- a `cancelled` run published as `FAILURE` with its
    cancelled ladder published as green, beside the `gh` command that
    refutes it. The conclusion guard could not see it: the paragraph carried
    the word and a value, which is all that rule asks.

    So the rule is not "say the conclusion" any more, it is "do not type the
    run". `scripts/ci_section.py` and `--rounds` emit every run this round
    from `gh run list --json ... status,conclusion`, and a run id anywhere
    else in the revision is a typed CI fact.
    """
    body = _newest_revision(REPORT_TEXT)
    allowed = _generated_text(body)
    stray = []
    for para in _paragraphs(body):
        if para in allowed or all(line in allowed for line in para.splitlines()):
            continue
        for run_id in set(_RUN_ID.findall(_joined(para))):
            if run_id not in allowed:
                stray.append((run_id, " ".join(para.split())[:90]))
    assert not stray, (
        "these paragraphs name a CI run outside the generated sections:\n"
        + "\n".join(f"  run {r}: {t}..." for r, t in stray)
        + "\nA run's outcome is what `scripts/ci_section.py` prints or it is "
        "not written. R449 was a cancelled run typed as a failure with a "
        "reason it never reached."
    )


_ROUNDS_HEADER = "| run | event | head | outcome |"
_ROUNDS_ROW = re.compile(r"^\|\s*`(\d{9,})`\s*\|[^|]*\|[^|]*\|\s*(.+?)\s*\|\s*$", re.M)
_SECTION_0_RUN = re.compile(r"Run `(\d{9,})`,[^.]*conclusion \*\*\w+\*\*")


def _gh_outcome(run_id: str) -> str | None:
    """`gh run view <id>`'s own words for what that run did, or None."""
    out = subprocess.run(
        ["gh", "run", "view", run_id, "--json", "status,conclusion"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if out.returncode != 0 or not out.stdout.strip():
        return None
    got = json.loads(out.stdout)
    if got["status"] != "completed":
        return "no result"
    if not got["conclusion"] or got["conclusion"] == "cancelled":
        return "no result"
    return got["conclusion"].lower()


def ci_table_defects(zero: str, lookup) -> list[str]:
    """Every way the CI table can disagree with the runs it claims to report.

    A FUNCTION WITH AN INJECTED LOOKUP, so the reviewer's report-level shapes
    can be run without the network while the shipped test uses `gh`.
    """
    rows = _ROUNDS_ROW.findall(zero)
    if _ROUNDS_HEADER not in zero:
        return ["the 0a table is missing its header"]
    if not rows:
        return ["the 0a table has a header and no rows"]
    out = []
    for run_id, stated in rows:
        truth = lookup(run_id)
        if truth is None:
            out.append(f"run {run_id}: `gh run view` returns nothing -- no such run")
            continue
        ok = "no result" in stated if truth == "no result" else truth in stated.lower()
        if not ok:
            out.append(f"run {run_id}: the table says `{stated}`, gh says `{truth}`")
    # A ROW MUST NOT CONTRADICT THE FAILING-NAME BLOCK GENERATED BESIDE IT.
    for run_id, stated in rows:
        marker = f"Run `{run_id}`, conclusion **failure**"
        if marker in zero and "failure" not in stated.lower():
            out.append(
                f"run {run_id}: the row says `{stated}` and a failing-test block "
                "for the same run stands under it"
            )
    return out


def test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW() -> None:
    """R462. Nothing re-ran `gh`, so R449's exact content was re-admissible.

    The reviewer measured four edits that every guard accepted: a cancelled
    row rewritten to `success`; a failure rewritten to `success` with its
    failing-test bullets left underneath; an invented run id; and every row
    deleted with the header kept. Each is the CI record in the report not
    being the CI record, which is CE1's whole subject.

    So this asks `gh`. It is the one test in the suite that reaches the
    network, and it FAILS rather than skips when it cannot -- a check that
    goes quiet when the tool is missing is the shape three verdicts have
    now named.
    """
    zero = _generated_text(_newest_revision(REPORT_TEXT))
    rows = _ROUNDS_ROW.findall(zero)
    assert rows, (
        "the 0a table has no rows. `python scripts/ci_section.py --rounds` "
        "emits one row per run of this round, and an empty table with its "
        "header kept passed every other guard here."
    )
    assert not ci_table_defects(zero, _gh_outcome), "\n".join(ci_table_defects(zero, _gh_outcome))


_TRUTH = {
    "35559285688": "no result",
    "35559285363": "failure",
    "35563850428": "success",
    "35561482997": "failure",
    # THE TWO RED RUNS OF THE FIFTY-SECOND ROUND, and the run at the commit
    # verdict 52 judged. `99999999999` is absent on purpose: `.get` returns
    # None for it, which is what a lookup of a run nobody made returns.
    "35659133236": "failure",
    "35660198114": "failure",
    "35664796051": "success",
}

_MARK = "<!-- generated: scripts/ci_section.py -->"
_BASE = (
    "## 0a. Runs since the commit verdict 51 judged\n\n"
    + _MARK
    + "\n\nGenerated: `python scripts/ci_section.py`, anchored on verdict 51.\n\n"
    + _ROUNDS_HEADER
    + "\n|---|---|---|---|\n"
    "| `35559285688` | push | `afc5b05` | **no result** (`cancelled`) |\n"
    "| `35559285363` | workflow_dispatch | `afc5b05` | conclusion **failure** |\n"
    "| `35563850428` | push | `6170263` | conclusion **success** |\n"
)


def _shape(name: str) -> str:
    """The reviewer's eleven report-level edits, by id."""
    if name == "a_0a_row_hand_edited_from_no_result_to_conclusion_success":
        return _BASE.replace("**no result** (`cancelled`)", "conclusion **success**")
    if name == "a_0a_row_hand_edited_from_failure_to_success_with_its_failing_list_left_below":
        return (
            _BASE.replace(
                "| `35559285363` | workflow_dispatch | `afc5b05` | conclusion **failure** |",
                "| `35559285363` | workflow_dispatch | `afc5b05` | conclusion **success** |",
            )
            + "\n**Run `35559285363`, conclusion **failure**: 15 failing test name(s).**\n"
        )
    if name == "an_invented_run_id_added_as_a_0a_table_row":
        return _BASE + "| `99999999999` | push | `deadbee` | conclusion **success** |\n"
    if name == "every_0a_row_deleted_and_the_header_kept":
        return _BASE.split("|---|---|---|---|")[0] + "|---|---|---|---|\n"
    if name == "control_section_0a_deleted_entirely":
        return "## 1. The reading\n\nnothing about CI here.\n"
    if name == "prose_about_runs_under_a_0b_heading":
        return (
            _BASE + "\n## 0b. What the runs mean\n\nRun 35559285688 was a clean green "
            "build and nothing went wrong.\n"
        )
    if name == "an_invented_run_id_under_a_0b_heading":
        return _BASE + "\n## 0b. What the runs mean\n\nRun 99999999999 also passed.\n"
    if name == "a_false_CI_sentence_in_the_section_11_reason_column":
        return (
            _BASE + "\n## 3. Sites\n\n| item | site | diff | why |\n|---|---|---|---|\n"
            "| R1 | `a.py` | untouched | run 35559285688 concluded success, ladder green |\n"
        )
    if name == "a_false_CI_sentence_in_the_section_12_subject_column":
        return (
            _BASE + "\n## 4. Carried\n\n| item | status | subject |\n|---|---|---|\n"
            "| R2 | **carried** | run 35561482997 concluded success |\n"
        )
    if name == "a_red_run_at_a_commit_that_was_force_pushed_away":
        return _BASE + (
            "| `35561482997` | push | `2bd9e89` \u2014 **head not in current history** "
            "| conclusion **failure** |\n"
        )
    if name == "the_Generated_provenance_line_is_itself_typed":
        return (
            "## 0a. Runs since the commit verdict 51 judged\n\n"
            "Generated: `python scripts/ci_section.py`, anchored on verdict 51.\n\n"
            + _ROUNDS_HEADER
            + "\n|---|---|---|---|\n"
            "| `35559285688` | push | `afc5b05` | conclusion **success** |\n"
        )
    # ---- the twelve handed over at the fifty-second verdict -------------
    if name == "prose_about_runs_under_a_heading_that_types_the_generated_marker":
        return _BASE + (
            "\n## 0d. What the runs mean\n\n"
            + _MARK
            + "\n\nRun `35659133236` was a clean green build; nothing this round "
            "went red.\n"
        )
    if name == "an_invented_run_id_inside_a_section_that_types_the_marker":
        return _BASE + (
            "\n## 0d. What the runs mean\n\n" + _MARK + "\n\nRun `99999999999` passed as well.\n"
        )
    if name == "a_prose_section_marked_generated_by_a_script_that_does_not_exist":
        return _BASE + (
            "\n## 0d. Coverage\n\n<!-- generated: scripts/no_such_script.py -->"
            "\n\nRun `35563850428` covered every leg.\n"
        )
    if name == "a_0a_row_whose_head_column_names_a_commit_the_run_was_not_at":
        return _BASE.replace(
            "| `35563850428` | push | `6170263` | conclusion **success** |",
            "| `35563850428` | push | `deadbee` | conclusion **success** |",
        )
    if name == "a_0a_row_whose_event_column_is_falsified":
        return _BASE.replace(
            "| `35559285363` | workflow_dispatch | `afc5b05` | conclusion **failure** |",
            "| `35559285363` | push | `afc5b05` | conclusion **failure** |",
        )
    if name == "a_0a_row_stating_two_outcomes_at_once":
        return _BASE.replace(
            "| `35559285363` | workflow_dispatch | `afc5b05` | conclusion **failure** |",
            "| `35559285363` | workflow_dispatch | `afc5b05` | conclusion **failure**, "
            "effectively **success** |",
        )
    if name == "the_two_non_green_rows_deleted_and_the_green_one_kept":
        return (
            _BASE.split("|---|---|---|---|")[0]
            + "|---|---|---|---|\n"
            + "| `35563850428` | push | `6170263` | conclusion **success** |\n"
        )
    if name == "a_0a_table_copied_forward_from_the_previous_round_unchanged":
        # EVERY ROW INDIVIDUALLY TRUE, three newer runs unlisted. The text is
        # `_BASE` itself under a later verdict number.
        return _BASE.replace(
            "## 0a. Runs since the commit verdict 51 judged",
            "## 0a. Runs since the commit verdict 52 judged",
        )
    if name == "the_head_not_in_current_history_label_stripped_from_a_row":
        return _BASE + ("| `35561482997` | push | `2bd9e89` | conclusion **failure** |\n")
    if name == "a_false_narrative_paragraph_appended_inside_the_generated_0a_section":
        return _BASE + (
            "\nBoth failures were the same report-staleness guard, and the "
            "verification ladder was green in each.\n"
        )
    if name == "control_a_real_failure_row_rewritten_to_conclusion_success":
        return _BASE + ("| `35659133236` | push | `1796183` | conclusion **success** |\n")
    if name == "control_a_naked_run_id_in_a_plain_paragraph_outside_any_marked_section":
        return _BASE + "\n## 1. The reading\n\nRun 35660198114 was fine.\n"
    raise AssertionError(name)


_REPORT_SHAPES = [
    ("a_0a_row_hand_edited_from_no_result_to_conclusion_success", True),
    ("a_0a_row_hand_edited_from_failure_to_success_with_its_failing_list_left_below", True),
    ("an_invented_run_id_added_as_a_0a_table_row", True),
    ("every_0a_row_deleted_and_the_header_kept", True),
    ("control_section_0a_deleted_entirely", True),
    ("prose_about_runs_under_a_0b_heading", True),
    ("an_invented_run_id_under_a_0b_heading", True),
    ("a_false_CI_sentence_in_the_section_11_reason_column", True),
    ("a_false_CI_sentence_in_the_section_12_subject_column", True),
    ("a_red_run_at_a_commit_that_was_force_pushed_away", False),
    ("the_Generated_provenance_line_is_itself_typed", True),
    # THE TWELVE FROM THE FIFTY-SECOND VERDICT'S CORPUS COMMIT (217a5ce).
    # `must_refuse` IS WHAT THE GUARDS WERE MEASURED TO DO with each shape at
    # the commit these rows were written. Ten of them do not catch it, so ten
    # rows are False. The corpus's `measured=` field records the same
    # measurement, and the two agreed when this was written -- but the field
    # is prose in a file the reviewer may rewrite, and this row is the
    # assertion. R481: the earlier wording here said `must_refuse` IS that
    # field, which would make a corpus edit silently redefine what the suite
    # asserts. It does not. A row changes when someone re-measures.
    #
    # The rows make the hole a fact the suite states rather than one a grep of
    # the corpus finds. Every False row is in the frozen 4a list in
    # docs/milestones/F2a.md, and CZ0 freezes the apparatus that would close
    # it -- so a row here flipping to True later is a change somebody made on
    # purpose, and it flips in the same commit as the repair.
    ("prose_about_runs_under_a_heading_that_types_the_generated_marker", False),
    ("an_invented_run_id_inside_a_section_that_types_the_marker", False),
    ("a_prose_section_marked_generated_by_a_script_that_does_not_exist", False),
    ("a_0a_row_whose_head_column_names_a_commit_the_run_was_not_at", False),
    ("a_0a_row_whose_event_column_is_falsified", False),
    ("a_0a_row_stating_two_outcomes_at_once", False),
    ("the_two_non_green_rows_deleted_and_the_green_one_kept", False),
    ("a_0a_table_copied_forward_from_the_previous_round_unchanged", False),
    ("the_head_not_in_current_history_label_stripped_from_a_row", False),
    ("a_false_narrative_paragraph_appended_inside_the_generated_0a_section", False),
    ("control_a_real_failure_row_rewritten_to_conclusion_success", True),
    ("control_a_naked_run_id_in_a_plain_paragraph_outside_any_marked_section", True),
]


@pytest.mark.parametrize("name, must_refuse", _REPORT_SHAPES, ids=[s[0] for s in _REPORT_SHAPES])
def test_the_CI_GUARDS_rule_on_the_reviewer_REPORT_shapes(name: str, must_refuse: bool) -> None:
    """R462, R463. Eleven edits to the report itself, not to a paragraph.

    Each is checked by the three things that decide a CI section: the
    generated/hand-written split, the table-versus-`gh` comparison, and the
    naked-run-id rule. `lookup` is injected, so a shape naming a run that
    does not exist is refused here without the network.
    """
    text = _shape(name)
    zero = _generated_text(text)
    hand = _hand_written(text)
    refused = bool(
        ci_table_defects(zero, _TRUTH.get)
        or runs_without_a_conclusion(hand)
        or any(_RUN_ID.findall(_joined(hand)))
    )
    assert (
        refused == must_refuse
    ), f"shape `{name}`: the guards {'allowed' if must_refuse else 'refused'} it"


def test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph() -> None:
    """R449. Section 0a was prose, and prose is where the CI record drifted.

    Structural rather than byte-for-byte: the generator is re-run at review
    time against a repository that has moved on, so its newest row is not in
    the committed text. What is checked is that the section IS the
    generator's shape -- its provenance line and its table -- and that every
    run id in the revision sits in one of the two generated forms. A
    sentence about a run cannot satisfy either, which is what R449 was.
    """
    body = _newest_revision(REPORT_TEXT)
    zero = _generated_text(body)
    assert _ROUNDS_HEADER in zero, (
        "no `## 0a` table in the newest revision. `python "
        "scripts/ci_section.py --rounds` emits every run this round with what "
        "it did; a paragraph about them is what R449 was."
    )
    # EACH SECTION'S PROVENANCE LINE NAMES THE INVOCATION THAT REPRODUCES IT
    # (R468). This assertion used to require the bare string on section 0a,
    # which `--rounds` writes -- so the guard REQUIRED the false line, and
    # correcting the generator would have reddened it.
    assert "Generated: `python scripts/ci_section.py --rounds`" in zero, (
        "the 0a block carries no `--rounds` provenance line. `python "
        "scripts/ci_section.py` with no flag prints section 0, not this one."
    )
    assert (
        "Generated: `python scripts/ci_section.py`" in zero
    ), "the section 0 block carries no generator provenance line."
    tabled = {m.group(1) for m in _ROUNDS_ROW.finditer(zero)}
    inline = set(_SECTION_0_RUN.findall(zero))
    for run_id in set(_RUN_ID.findall(_joined(_hand_written(body)))):
        assert run_id in tabled or run_id in inline, (
            f"run {run_id} is named in the revision but is in neither "
            "generated form -- not a row of the 0a table and not section 0's "
            "own `Run ..., conclusion ...` line. It was typed."
        )
    for _id, outcome in _ROUNDS_ROW.findall(zero):
        assert _CONCLUSION.search("conclusion " + outcome) or "no result" in outcome, (
            f"the 0a row for run {_id} reads `{outcome}`, which is neither a "
            "conclusion nor `no result`."
        )


def test_every_CI_RUN_the_report_names_carries_its_conclusion() -> None:
    """R412, twice. A run id with no conclusion beside it is the whole defect.

    Scoped to the paragraph, because that is the unit a reader takes a claim
    from: a conclusion three sections away is not beside anything. A table row
    naming a run is a paragraph of its own under this split, which is right --
    a row that names a run states something about it.
    """
    # THE GENERATED SECTIONS ARE NOT READ HERE (CX0). They are the CI record
    # and they carry their own rules -- `test_the_ROUNDS_SECTION_is_the_
    # GENERATORS_and_not_a_paragraph` checks their shape and every outcome in
    # them. This guard is about the PROSE, where R412 and R449 both happened,
    # and running it over a generated table made its own `no result` rows
    # look like naked ids.
    body = _newest_revision(REPORT_TEXT)
    naked = runs_without_a_conclusion(_hand_written(body))
    assert not naked, (
        "these paragraphs name a CI run and never say what it concluded:\n"
        + "\n".join(f"  run {r}: {t}..." for r, t in naked)
        + "\nA run's job rows can all be green while the run concluded "
        "`failure`; that is how R412 happened twice. Name the conclusion, or "
        "do not name the run."
    )


def test_a_GREEN_JOB_TABLE_does_not_stand_under_a_FAILED_run() -> None:
    """The specific shape, refused (CU3).

    When the CI section's own stated conclusion is not `success`, a table in
    which nothing is red is a table that reads as a green build. The report
    may still be right -- the failures can be report-staleness guards that the
    next commit fixes, which is what happened -- but it has to SAY so, and the
    literal is how it says it.
    """
    why = a_green_table_under_a_failed_run(_ci_section())
    assert why is None, (
        f"the CI section: {why}. That reads as a green build. Write "
        f"`{_GREEN_UNDER_RED}` in this section with the reason, or the table "
        "is telling a reader the opposite of what the run did."
    )


# THE CONTROLS FOR BOTH GUARDS (R429, R430, R444). Nineteen shapes the
# reviewer wrote into its CI-section corpus over two verdicts and measured
# the shipped pattern against: 2 of 7 the first time, 3 of 12 the second.
# Each id below is that file's and the text is the paragraph it describes.
#
# THE IDS ARE READ FROM THE CORPUS, NOT REMEMBERED (R440). The previous
# version said a change to either one "shows up as a disagreement" and
# nothing in the repository read the file, so a shape added there appeared
# nowhere. `test_every_corpus_shape_is_transcribed` below reads the ids and
# fails on any that is not here. The reviewer owns the file and the
# PARAGRAPHS are still transcriptions of its prose descriptions -- that half
# is a reading and is not mechanised.
_CI_SHAPES: list[tuple[str, str, bool]] = [
    ("run_id_ends_a_sentence", "The dispatch for this round was run 35479925335.", True),
    (
        "run_id_immediately_before_a_period_in_a_list_item",
        "* The push run for this round is 35479506950.",
        True,
    ),
    ("run_id_13_digits", "The paragraph names run 3547992533512 and no result.", True),
    (
        "run_id_with_thousands_separators",
        "The paragraph names run 35,479,925,335 and no result.",
        True,
    ),
    (
        "the_word_conclusion_is_in_the_COMMAND_and_never_in_the_OUTPUT",
        "cmd gh run view 35479506950 --json conclusion status\nout I did not paste it",
        True,
    ),
    (
        "run_id_ends_a_sentence_inside_backticks",
        "The push run for this round is `35479506950`.",
        True,
    ),
    ("control_run_id_then_a_space", "The push run for this round is 35479506950 .", True),
    # And the shape that must be ALLOWED, or the guard refuses every report.
    (
        "a_run_named_with_its_result",
        "Run `35482244521` at `d8ac843`, event `push`, conclusion **success**.",
        False,
    ),
    (
        "the_tolerance_value_that_is_not_a_run_id",
        "RIGID_MODE_BOUND = 199.526231496888, which is 10.0 * 10**1.3.",
        False,
    ),
    # THE FORTY-NINTH VERDICT'S TWELVE. The first four are the R412 shape one
    # level up: the value is in the command, in a needle, negated, or about a
    # different job.
    (
        "conclusion_value_only_inside_a_jq_filter",
        "Run 35479925335: gh run list --json conclusion "
        "--jq 'select(.conclusion==\"success\")' -- output never pasted.",
        True,
    ),
    (
        "conclusion_value_only_inside_a_grep_needle",
        "cmd gh run view 35489487935 --log-failed | grep -c failure\nout not pasted",
        True,
    ),
    (
        "the_result_is_negated",
        "Run 35479925335 was not a failure as far as I could tell.",
        True,
    ),
    (
        "an_unrelated_skipped_rescues_a_naked_run_id",
        "Run 35479925335 - the determinism legs were skipped and nothing else is said.",
        True,
    ),
    (
        "comma_list_of_three_digit_numbers",
        "Counts across the corpus: 100,200,300,400 and nothing else.",
        False,
    ),
    (
        "run_id_with_spaces_as_separators",
        "The paragraph names run 35 479 925 335 and no result.",
        True,
    ),
    (
        "run_id_broken_across_a_line_with_a_hyphen",
        "The paragraph names run 354799-\n25335 and no result.",
        True,
    ),
    (
        "run_id_followed_by_a_decimal_fraction",
        "The dispatch was run 35479925335.0 seconds long and no result.",
        True,
    ),
    (
        "run_id_preceded_by_a_dot_in_a_decimal",
        "0.35479925335 is the run and no result is given.",
        False,
    ),
    ("an_eight_digit_id", "The paragraph names run 35479925 and no result.", False),
    (
        "control_a_workflow_url_with_no_result",
        "https://github.com/x/y/actions/runs/35479925335 shows what happened.",
        True,
    ),
    (
        "control_an_id_inside_a_fenced_block_with_no_result",
        "```\ngh run view 35479925335\n```",
        True,
    ),
    # AND THE SHAPE THAT MUST STILL BE ALLOWED, in the form this report uses.
    # THE FIFTIETH VERDICT'S TWENTY. The substantive one is the first: the
    # guard decided per PARAGRAPH, so one conclusion satisfied every id in
    # it. Five of the twenty are shapes the reviewer expects ALLOWED and two
    # of those were false positives.
    (
        "conclusion_stated_for_a_DIFFERENT_run_in_the_same_paragraph",
        "Run 35489487935 had conclusion success. Run 35545894507 is also named here.",
        True,
    ),
    (
        "two_runs_one_conclusion",
        "Runs 35479925335 and 35489487935: conclusion success",
        True,
    ),
    (
        "run_id_with_underscores_as_separators",
        "The paragraph names run 35_479_925_335 and no result.",
        True,
    ),
    (
        "conclusion_word_and_value_split_by_a_newline",
        "Run 35479925335, event push, conclusion\n**success** on both jobs.",
        False,
    ),
    (
        # THE RULE THAT SAYS WHICH, since the corpus asked for one: the value
        # must sit within twelve NON-ALPHANUMERIC characters of the word, so
        # `conclusion was success` does not satisfy it, and neither does `the
        # conclusion of the whole exercise ... was success`. That refuses a
        # job's conclusion written in a sentence, and it refuses some true
        # statements about the run too. The generated sections write
        # `conclusion **success**`, so the adjacency costs nothing where it
        # matters, and the looser form is exactly where a job's result gets
        # mistaken for a run's.
        "conclusion_of_a_job_not_the_run",
        "Run 35479925335: the ladder job conclusion was success; the run itself is not stated.",
        True,
    ),
    (
        "the_word_conclusion_far_from_its_value",
        "Run 35479925335, the conclusion of the whole exercise after a long "
        "argument nobody wanted was success.",
        True,
    ),
    (
        "conclusion_value_inside_a_yaml_snippet_no_pipe",
        "Run 35479925335\nconclusion: success",
        False,
    ),
    (
        "a_result_word_with_no_run_word_and_no_conclusion",
        "35479925335 finished green and everything passed.",
        True,
    ),
    (
        "value_only_in_a_markdown_table_row",
        "Run 35479925335\n| job | conclusion |\n| ladder | success |",
        True,
    ),
    (
        "commandish_line_that_also_carries_the_real_result",
        "cmd gh run view 35479925335 --json conclusion -> conclusion **failure**",
        False,
    ),
    (
        "conclusion_spelled_as_a_verb",
        "Run 35479925335 concluded: success",
        True,
    ),
    (
        "run_id_in_a_url_query_string",
        "See ?run_id=35479925335 for what happened.",
        True,
    ),
    (
        "thirteen_digit_id_with_a_conclusion",
        "Run 3547992533512 had conclusion success.",
        False,
    ),
    (
        "conclusion_value_more_than_twelve_chars_after_the_word",
        "Run 35479925335 conclusion, as reported by the API, success",
        True,
    ),
    (
        "conclusion_inside_an_inline_code_span",
        "Run 35479925335, `conclusion=success`",
        False,
    ),
    (
        "em_dash_separated_conclusion",
        "The paragraph names run 35479925335 and the conclusion \u2014 success",
        False,
    ),
    (
        "id_split_by_a_markdown_bold_marker",
        "Run **35479925335** and no result.",
        True,
    ),
    (
        "no_run_id_at_all_but_a_conclusion",
        "conclusion success and no run named",
        False,
    ),
    (
        "run_id_as_part_of_a_longer_token",
        "Artifact a35479925335b was produced; no result given.",
        True,
    ),
    (
        "the_generated_section_line_at_this_commit",
        "Generated: `python scripts/ci_section.py`, anchored on verdict 49 at "
        "`ed67a7d`. Run `35489487935`, event push, conclusion **success**",
        False,
    ),
    (
        "the_generated_section_line",
        "Generated: `python scripts/ci_section.py`, anchored on verdict 48 at "
        "`a0b2873`. Run `35489487935`, event `push`, conclusion **success**.",
        False,
    ),
]

_CI_CORPUS = ROOT / "tests" / "corpus" / "report_ci_section.txt"


def test_every_corpus_shape_is_transcribed() -> None:
    """R440. The disagreement the comment above promises, made to happen.

    The reviewer owns the corpus and adds shapes to it between verdicts. Until
    now nothing here read it, so a shape added there was measured by nobody
    and the sentence claiming otherwise was refuted by one grep. Reading the
    IDS is the mechanical half; the paragraphs are still transcriptions of the
    file's prose descriptions, which is a reading and is not mechanised.
    """
    ids = re.findall(r"^id=(\S+)", _CI_CORPUS.read_text(encoding="utf-8"), re.M)
    assert len(ids) >= 19, f"the corpus parsed to {len(ids)} ids; the pattern broke"
    # THE FIRST FOUR ENTRIES ARE ABOUT A DIFFERENT GUARD. They were written at
    # the thirty-first verdict against `test_the_report_carries_a_CI_SECTION`
    # -- whole job TABLES, rewritten or invented -- and not against either of
    # the two run-id guards these shapes control. They are named rather than
    # filtered by a pattern, so a new table shape is not silently excluded.
    table_shapes = {
        "the_shipped_section_0_table_unmodified",
        "a_red_run_reported_as_all_green",
        "no_run_id_and_an_invented_green_table",
        "three_rows_of_a_table_about_something_else",
    }
    known = {s[0] for s in _CI_SHAPES} | {s[0] for s in _REPORT_SHAPES} | table_shapes
    missing = [i for i in ids if i not in known]
    assert not missing, (
        f"{len(missing)} shape(s) in {_CI_CORPUS.name} are not transcribed into "
        f"`_CI_SHAPES`: {missing}. Each one is a paragraph nobody has run the "
        "guard against."
    )


@pytest.mark.parametrize("name, text, must_refuse", _CI_SHAPES, ids=[s[0] for s in _CI_SHAPES])
def test_the_RUN_CONCLUSION_guard_rules_on_the_reviewer_shapes(
    name: str, text: str, must_refuse: bool
) -> None:
    """`tests/corpus/report_ci_section.txt`, applied to the function directly."""
    got = bool(runs_without_a_conclusion(text))
    assert got == must_refuse, (
        f"shape `{name}`: the guard "
        f"{'allowed' if must_refuse else 'refused'} it.\n    {text}\n"
        "The reviewer measured this pattern at 2 of 7 on these shapes; a row "
        "that flips back is that coverage going backwards."
    )


_GREEN_TABLE_SHAPES: list[tuple[str, str, bool]] = [
    (
        "a_failed_run_whose_every_job_reads_green",
        "## 0. CI at `abc1234` \u2014 conclusion **FAILURE**\n\n"
        "| job | passed | failed | skipped |\n|---|---|---|---|\n"
        "| lint | 10 | 0 | 0 |\n\n**Job conclusions: 4 jobs, 0 not green.**",
        True,
    ),
    (
        "the_same_section_saying_so",
        "## 0. CI at `abc1234` \u2014 conclusion **FAILURE**\n\n"
        "| job | passed | failed | skipped |\n|---|---|---|---|\n"
        "| lint | 10 | 0 | 0 |\n\n**Job conclusions: 4 jobs, 0 not green.**\n\n"
        "GREEN JOBS UNDER A FAILED RUN: the failures are report guards.",
        False,
    ),
    (
        "a_failed_run_with_a_red_job",
        "## 0. CI at `abc1234` \u2014 conclusion **FAILURE**\n\n"
        "**Job conclusions: 4 jobs, 1 not green.**",
        False,
    ),
    (
        "a_green_run",
        "## 0. CI at `abc1234` \u2014 conclusion **SUCCESS**\n\n"
        "**Job conclusions: 4 jobs, 0 not green.**",
        False,
    ),
    ("a_section_with_no_conclusion_at_all", "## 0. CI at `abc1234`\n\nsome prose", True),
]


@pytest.mark.parametrize(
    "name, text, must_refuse", _GREEN_TABLE_SHAPES, ids=[s[0] for s in _GREEN_TABLE_SHAPES]
)
def test_the_GREEN_TABLE_guard_has_a_negative_control(
    name: str, text: str, must_refuse: bool
) -> None:
    """R430. This guard returns early on every report that is green.

    At `d8ac843` section 0 concluded `success`, so the shipped assertion above
    asserted nothing and no state in `tests/test_report_guard_states.py`
    covered it. These five run the function on text of their own.
    """
    got = a_green_table_under_a_failed_run(text) is not None
    assert got == must_refuse, (
        f"shape `{name}`: the guard "
        f"{'allowed' if must_refuse else 'refused'} it.\n    {text[:200]}"
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
        <sha>       the report path is UNTRACKED -- a copy, not a committed
                    report -- and the anchor is the newest commit touching
                    the reports TREE instead. R388: the first version of this
                    table said this state returns `""`, and it does not; the
                    commit message had it right and the docstring did not.
        ""          nothing under `docs/reports/` has any history at all. Only
                    then does rule 1 stand down and rule 2 carry the claim
                    alone.

    Conflating the untracked state with "not committed yet" is the whole of
    R377: any state where `git log -1 -- REPORT` came back empty took the
    HEAD branch, which is the pre-CP1 rule R361 refuted, and switched rule 2
    off with it.

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
# THE CONCATENATION IS NOT AN EVASION AND THE LINE SHOULD SAY SO (R382).
# `.claude/hooks/protect-reviews.sh` refuses any Bash COMMAND whose text names
# the verdict tree, which includes `grep -rn` and `python - <<PY` one-liners
# written while working on this file; the split spelling is what lets those
# be run at all. It is also the shape that hook names as its own limitation,
# so writing it without this sentence looks exactly like getting an edit past
# it. `grep -rn "docs/reviews" tests/` will not find this line -- that is the
# cost, it is real, and 4a has it recorded.
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
        # NOTHING UNDER `docs/reports/` HAS ANY HISTORY (R377, and R388's
        # second site). This is NOT 'the report path has no history': an
        # untracked report falls back to the reports TREE and gets a sha,
        # which is the second state and is handled above. This branch is
        # the third and last -- no commit anywhere touched a report -- so
        # there is no commit to
        # measure a distance to, so rule 1 has nothing to say and saying it
        # anyway is what made this red at every reviewer commit. Rule 2 still
        # applies and is the half that carries the claim: whatever this tree
        # is, no commit touching code may sit between the measurement and the
        # head. `test_the_anchor_fallback_cannot_be_taken_in_this_repository`
        # is what
        # stops this branch from ever being taken in this repository.
        intruders = _implementer_commits_after(sha)
        assert not intruders, (
            f"{len(intruders)} commit(s) touching code follow `{sha}`, the "
            "commit the whole-suite line names, and nothing under the reports "
            "tree has any history to anchor a distance to:\n  " + "\n  ".join(intruders)
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
