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
2. Every `file:line` a finding names is either touched by the step's diff since
   the reviewed commit, or named in the report with an explicit "no change"
   beside it. Three rounds running, a condition that named sites was closed at
   some of them and recorded as answered; this fails before it can be reported.

WHAT IS NOT CHECKED, stated so the guard is not trusted past its reach: whether
the status written beside a carried item is TRUE, and whether a touched file was
touched at the right line. Both are the reviewer's.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
VERDICT = ROOT / "docs" / "reviews" / "F2" / "step-4.md"
REPORT = ROOT / "docs" / "reports" / "F2" / "step-4.md"

_FINDING = re.compile(r"^\*\*(R\d+)\.", re.MULTILINE)
_MENTION = re.compile(r"\bR\d+\b")
# `path/to/file.py:123` or `:123-145`, as the verdicts write them.
# The leading dot of `.claude/...` is part of the path; `` before it would
# cut it off and the file would never match the diff.
_SITE = re.compile(r"((?:\.?[\w.-]+/)+[\w.-]+\.(?:py|md|sh|txt|json))")


def _read(path: Path) -> str:
    """Permissive: a verdict written with a Windows-1252 dash must not make a
    guard raise, because a guard that raises is a guard that gets removed."""
    return path.read_bytes().decode("utf-8", errors="replace")


def _section(text: str, heading: str) -> str:
    heads = list(re.finditer(rf"^##+ .*{heading}.*$", text, re.MULTILINE))
    if not heads:
        return ""
    start = heads[-1].end()
    nxt = re.search(r"^##+ ", text[start:], re.MULTILINE)
    return text[start:start + nxt.start()] if nxt else text[start:]


def _newest_revision(text: str) -> str:
    marks = [m.start() for m in re.finditer(r"^# Revision \d+", text, re.MULTILINE)]
    return text[marks[-1]:] if marks else text


def _reviewed_commit(text: str) -> str:
    m = re.search(r"^Reviewed commit:\s*(\S+)", text, re.MULTILINE)
    return m.group(1) if m else ""


def _answered_verdict(report_text: str) -> str:
    """The `Answers: verdict <n> @ <sha>` header of the newest revision.

    Returns the sha, or `""` when the header is absent -- which
    `test_the_report_names_the_verdict_it_answers` turns into a failure rather
    than a silent fall back to the newest verdict.
    """
    m = re.search(r"^Answers:\s*verdict\s*\d+\s*@\s*(\S+)",
                  _newest_revision(report_text), re.MULTILINE)
    return m.group(1) if m else ""


def _verdict_text_at(sha: str) -> str:
    """The verdict file as it stood at `sha`, or the working copy if unknown."""
    if not sha:
        return _read(VERDICT)
    out = subprocess.run(
        ["git", "show", f"{sha}:docs/reviews/F2/step-4.md"],
        cwd=ROOT, capture_output=True)
    if out.returncode != 0:
        return _read(VERDICT)
    return out.stdout.decode("utf-8", errors="replace")


REPORT_TEXT = _read(REPORT)
ANSWERED = _answered_verdict(REPORT_TEXT)
VERDICT_TEXT = _verdict_text_at(ANSWERED)
CARRIED = _section(_newest_revision(REPORT_TEXT), "Carried")
EXPECTED = sorted(
    set(_FINDING.findall(VERDICT_TEXT))
    | set(_MENTION.findall(_section(VERDICT_TEXT, "Carried"))),
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
    out = subprocess.run(["git", "cat-file", "-e", ANSWERED], cwd=ROOT,
                         capture_output=True)
    assert out.returncode == 0, (
        f"the report answers verdict `{ANSWERED}`, which is not a commit in "
        "this repository."
    )


def test_the_parse_found_something_to_check() -> None:
    """Meta-test: zero parsed findings is a parse failure, not a clean bill."""
    assert _FINDING.findall(VERDICT_TEXT), (
        "no `**R<n>.` finding heading parsed from the verdict -- the format "
        "changed and every assertion below would pass on anything"
    )
    assert CARRIED.strip(), (
        "the newest report revision has no Carried section, so there is nothing "
        "to check against"
    )
    assert len(EXPECTED) >= 5, (
        f"only {EXPECTED} expected; the verdict carries more than that and the "
        "pattern is missing most of them"
    )


@pytest.mark.parametrize("finding", EXPECTED)
def test_the_report_carries_the_finding(finding: str) -> None:
    assert finding in _MENTION.findall(CARRIED), (
        f"{finding} is in the newest verdict -- as a finding or as an item it "
        "carries forward -- and the newest report revision's Carried section "
        "does not mention it. CLAUDE.md: the dependency list is part of what "
        "gets re-read at every step, by a reader that was not the one who "
        "skipped it."
    )


def _changed_files() -> set[str]:
    reviewed = _reviewed_commit(VERDICT_TEXT)
    if not reviewed:
        return set()
    # Reviewed commit -> WORKING TREE, not -> HEAD. The step is answered before
    # it is committed, and a check that only sees committed work would demand
    # the answer be committed before it can be shown to be an answer.
    out = subprocess.run(["git", "diff", "--name-only", reviewed],
                         cwd=ROOT, capture_output=True, text=True)
    return {line.strip() for line in out.stdout.splitlines() if line.strip()}


def _sites_by_finding() -> list[tuple[str, str]]:
    """`(finding, path)` for every file a finding names."""
    blocks = list(re.finditer(r"^\*\*(R\d+)\.", VERDICT_TEXT, re.MULTILINE))
    out: list[tuple[str, str]] = []
    for i, m in enumerate(blocks):
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(VERDICT_TEXT)
        body = VERDICT_TEXT[m.start():end]
        for path in set(_SITE.findall(body)):
            out.append((m.group(1), path))
    return sorted(set(out))


SITES = _sites_by_finding()


@pytest.mark.parametrize("finding, path", SITES,
                         ids=[f"{f}-{p}" for f, p in SITES])
def test_every_named_site_is_touched_or_declared(finding: str, path: str) -> None:
    """A finding that names files is answered at all of them, or says which not.

    Three consecutive rounds closed a site-naming condition at some of its sites
    and recorded it as answered. The escape hatch is deliberate and explicit: the
    report may write `no change` beside the path, which is a claim a reviewer can
    check, rather than an omission nobody sees.
    """
    if path in _changed_files():
        return
    revision = _newest_revision(REPORT_TEXT)
    for line in revision.splitlines():
        if path in line and re.search(r"no change", line, re.IGNORECASE):
            return
    pytest.fail(
        f"{finding} names {path}, the step's diff does not touch it, and the "
        f"newest report revision does not say `no change` beside it. Either "
        "answer the site or declare it unanswered by name -- half of an item is "
        "not the item."
    )
