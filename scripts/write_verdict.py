#!/usr/bin/env python3
"""Write a supervisor verdict to docs/reviews/F<n>/step-<k>.md.

Used only by the gating-supervisor agent. The editing tools are blocked from
docs/reviews/ by a PreToolUse hook; this is the one sanctioned path in.

Usage:
    python scripts/write_verdict.py --milestone F2 --step 5 < review.md
    python scripts/write_verdict.py --milestone F6a --step 1 < review.md
    python scripts/write_verdict.py --milestone R1 --step 1 < review.md

The milestone is the LOCKED PLAN's own name (FN3). `--milestone 1` refuses: it names
no plan, and the old validator would have written it into `docs/reviews/F1/`.

The review body is read from stdin. The script stamps the reviewed commit and
refuses FOUR things -- the count, not a summary of it:

    :53  a body not beginning with `Verdict: PASS|HOLD|STOP`
    :56  a body missing any mandatory section
    :58  an empty `## Carried` section
    :63  a step with no report to review

cmd: grep -n "sys.exit" scripts/write_verdict.py
out: the four lines above

IT DOES NOT REFUSE TO OVERWRITE A PASS, and this docstring said it did (DQ3).
The deleted claim was that it "refuses to overwrite a PASS with anything but a
fresh review of a changed report". No such check exists in this file.

AND IT NO LONGER OVERWRITES ANYTHING (DX2, DY6). Each round is prepended and the
earlier rounds are kept verbatim below a separator, because a guard reads the
whole file for rulings made in earlier rounds and the overwrite made that guard's
premise false. The reason is at the write site.

THE REPAIR THEN WROTE A SECOND FALSE COUNT, AND A PLACEHOLDER (C31, C32). It
said "the two refusals" one paragraph after deleting a false claim, when the grep
gives four -- CP2 is exactly the rule that a repair carries no new numeric claim
outside a triple -- and the patch script that made the edit left the token
`PLACEHOLDER_WRITE_VERDICT` in the quoted sentence, which nothing in the tree
reads and so nothing caught.

**R1049 IS CLOSED (FV3): THE STAMP IS `--judged`, NOT `HEAD`.** It used to read
`HEAD`, which is structurally NOT the reviewed commit whenever the reviewer
commits its corpus first -- as it is instructed to. The body named the commit it
judged; that line did not, and the reviewer had been writing the judged sha into
its prose by hand as a stopgap, and saying so, for several rounds.

`--judged <sha>` is now REQUIRED, it is what gets stamped, and it must be an
ancestor of `HEAD` or the tool refuses. **There is no implicit fallback to
`HEAD`,** which is the whole point: a default is what made the old line correct
by coincidence -- right exactly when the reviewer had committed nothing of its
own, and silently wrong whenever it had. Adopted by directive FV3,
`docs/directives/FV.md`.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REQUIRED = ("## Carried", "## Findings", "## Tolerances touched", "## Next step opens when")
VERDICTS = ("PASS", "HOLD", "STOP")


def _plan_labels() -> list[str]:
    """Every locked plan's label, read from the directory rather than assumed.

    This is the whole of FN3's generalisation: the set of valid milestones is the set of
    plans that EXIST, so a new series needs no edit here.

    Resolved from `__file__` rather than from `git rev-parse`, because an argparse `type=`
    callable runs before `main()` computes the root, and because a validator that shells
    out once per argument would fail differently outside a work tree than inside one.
    """
    plans = Path(__file__).resolve().parents[1] / "docs" / "milestones"
    return sorted(q.stem for q in plans.glob("*.md"))


def _resolve(label: str, what: str) -> str:
    """`label` if a locked plan carries that exact name, else a refusal naming the set.

    **THE OLD VALIDATOR STRIPPED AN `F` AND RE-ADDED IT, AND R1 IS WHY THAT FAILED (R804).**
    It accepted `2`, `2a`, `6a` or `F6a`, normalised to the numeric body, and rebuilt the
    path as `f"F{cleaned}"`. Against `R1` it refused outright -- the reviewer could not
    write an R1 verdict through the one sanctioned path in, and hand-wrote it instead --
    and that is the mild half.

    **THE SHARP HALF: `--milestone 1` SATISFIED IT AND WOULD HAVE WRITTEN INTO
    `docs/reviews/F1/step-1.md`.** A typo, or the habit of typing the step's number, put a
    verdict under a closed milestone with no error of any kind. FN3's counter-case is
    exactly that, and the repair is not a wider regex: it is that an identifier must NAME A
    LOCKED PLAN. `1` names none, so it refuses; `F1` names one and would be written where it
    belongs.

    No `F` is added and none is stripped. The label is a path segment and it is used as
    given, which is the only form that cannot silently mean a different milestone.
    """
    got = label.strip()
    if not got:
        raise argparse.ArgumentTypeError(f"{what}: an empty milestone names no plan")
    known = _plan_labels()
    if got not in known:
        raise argparse.ArgumentTypeError(
            f"{what}: {label!r} is not a locked plan. `docs/milestones/` carries "
            f"{known}. The identifier becomes a path segment, so it is used exactly as "
            f"given -- no `F` is added and none is stripped, because a bare number would "
            f"otherwise resolve to a milestone nobody named."
        )
    return got


def _milestone(value: str) -> str:
    """A milestone label naming a locked plan (R785, generalised by FN3).

    `type=int` made `F2a` and `F6a` inexpressible, which R785 fixed by taking a label.
    FN3 finishes the job: the label is validated against the plans that exist rather
    than against a pattern that assumed every milestone starts with `F`.
    """
    return _resolve(value, f"--milestone {value!r}")


def _closes(value: str) -> str:
    """A milestone label, or `milestone/step`, for the `Closes:` line (FK0).

    THE WHOLE POINT IS THAT THIS IS RECORDED AND NOT INFERRED. Three routers in three
    commits tried to infer "is this verdict closing something?" from the tree -- the
    newest verdict's disposition, the step report's own whole-suite line, the closure
    artifact's block -- and each was correct on the states its author swept and wrong on
    one nobody did (R802, R803). A boolean was standing in for a distinction the
    repository did not record anywhere.

    So the reviewer records it. This argument is the only way the line is written, and the
    verdict tree is hook-protected, so the line is settable only by the party whose
    judgement it is -- which is the property the proxies could not have.

    The milestone part goes through the same plan resolution as `--milestone` (FN3), so
    `Closes: 1` cannot name a milestone nobody declared. FK2's router compares this
    against the plan stem carrying the step marker, and the label IS that stem.
    """
    raw = value.strip()
    milestone, _, step = raw.partition("/")
    label = _resolve(milestone, f"--closes {value!r}")
    if step:
        bare = step[5:] if step.startswith("step-") else step
        if not bare.isdigit():
            raise argparse.ArgumentTypeError(
                f"--closes {value!r}: the step part must be a number, as in F6b/step-1"
            )
        return f"{label}/step-{int(bare)}"
    return label


def sha() -> str:
    """`HEAD`. Used for the ancestry check only -- never for the stamp (FV3)."""
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def _judged(value: str) -> str:
    """Resolve `--judged` to a full sha and REFUSE unless it is an ancestor of `HEAD`.

    Two refusals rather than one, because they catch different mistakes:

    * a sha git does not know -- a typo, or a commit from another clone;
    * a sha git knows that is NOT an ancestor of `HEAD` -- a commit on another branch, or
      one rebased away. A verdict anchored there names a commit this history does not
      contain, and every guard that resolves the anchor would follow it off the branch.

    **THERE IS NO FALLBACK TO `HEAD`, AND THAT IS THE POINT OF FV3.** A default is what
    made the old stamp correct by coincidence: it agreed with the judged commit exactly
    when the reviewer had not yet committed anything of its own, and disagreed silently
    whenever it had.
    """
    try:
        full = subprocess.check_output(
            ["git", "rev-parse", "--verify", value + "^{commit}"], text=True
        ).strip()
    except subprocess.CalledProcessError:
        raise argparse.ArgumentTypeError(
            f"--judged {value!r}: not a commit this repository knows. The verdict's anchor "
            f"is what every downstream guard resolves, so a sha that does not exist here "
            f"cannot be stamped (FV3)."
        ) from None
    if subprocess.call(["git", "merge-base", "--is-ancestor", full, sha()]) != 0:
        raise argparse.ArgumentTypeError(
            f"--judged {full[:12]}: a commit, but NOT an ancestor of HEAD ({sha()[:12]}). "
            f"A verdict may only judge a commit this history contains -- otherwise its "
            f"anchor points off the branch and every guard that follows it is reading "
            f"another line of development (FV3)."
        )
    return full


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--milestone", type=_milestone, required=True)
    ap.add_argument("--step", type=int, required=True)
    ap.add_argument(
        "--judged",
        type=_judged,
        required=True,
        help=(
            "the sha this verdict judges. REQUIRED, stamped verbatim, and refused unless "
            "it is an ancestor of HEAD. No fallback to HEAD (FV3, closing R1049)."
        ),
    )
    ap.add_argument(
        "--closes",
        type=_closes,
        default=None,
        help=(
            "this verdict CLOSES that step or increment; writes one `Closes:` line "
            "into this entry (FK0). FK1: a closing verdict must use it, and no other "
            "verdict may carry the line."
        ),
    )
    ap.add_argument(
        "--interim",
        action="store_true",
        help=(
            "record an ES0 INTERIM CHECK against the open step, with no report required "
            "(FS2). An interim check closes nothing, so it may not be combined with "
            "--closes."
        ),
    )
    args = ap.parse_args()
    if args.interim and args.closes:
        sys.exit(
            "refused: --interim and --closes are mutually exclusive. An interim check "
            "closes nothing (FK1), which is why FS2 gives it its own flag."
        )

    body = sys.stdin.read()
    m = re.match(r"\s*Verdict:\s*(\w+)", body)
    if not m or m.group(1) not in VERDICTS:
        sys.exit("refused: body must begin with 'Verdict: PASS|HOLD|STOP'")
    missing = [s for s in REQUIRED if s not in body]
    if missing:
        sys.exit(f"refused: missing sections {missing}")
    if re.search(r"^## Carried\s*\n\s*(?=## )", body, re.M):
        sys.exit("refused: '## Carried' is empty — write 'checked, nothing carried' if so")

    root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    # **AN INTERIM CHECK HAS NO REPORT, BY DESIGN, AND THIS REFUSAL MADE THE TOOL
    # UNUSABLE FOR ONE (R856, FS2).** ES0 defines an interim check as a verdict the
    # `Stop` hook forces mid-step on a tree with NO new report revision, and FR3 makes
    # "build the whole step, then write the report" the normal order -- so the normal
    # state of an interim check is exactly the state this line rejected.
    #
    # It refused three times in step 3 and the reviewer hand-wrote all three verdicts,
    # which is the outcome FN3 exists to prevent: a tool the reviewer cannot use is a
    # tool whose anchor line, section checks and `Closes:` discipline go unapplied.
    #
    # A reviewed revision still requires its report. `--interim` says which of the two
    # this is rather than inferring it from a missing file -- an absent report is also
    # what a mistyped `--step` looks like.
    report = root / f"docs/reports/{args.milestone}/step-{args.step}.md"
    if not report.exists() and not args.interim:
        sys.exit(
            f"refused: no step report at {report}. If this is an ES0 interim check, "
            f"pass --interim (FS2); an interim check is recorded against the open step "
            f"and needs no report."
        )

    out = root / f"docs/reviews/{args.milestone}/step-{args.step}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    # THE ANCHOR LINE THE CI SECTION GENERATOR NEEDS, EMITTED BY THE TOOL (FN3).
    #
    # `scripts/ci_section.py` walks `report -> Answers: verdict N @ <sha> -> that
    # verdict's header -> the commit it judged`, and the pattern it reads is
    # `_JUDGED = r"\*\*Reviewed commit:\s*`([0-9a-f]{7,40})`"` -- BOLD, WITH BACKTICKS.
    # This tool wrote only the plain `Reviewed commit: <sha>` line, so every verdict that
    # satisfied that generator did so because a reviewer also typed the bold form into the
    # body by hand. Six times in F6b's file, seven in F6a's.
    #
    # R1's verdict was hand-written -- that is R804 -- and it carries the plain line and
    # not the bold one, so `ci_section.py` refuses with "does not name the commit it judged
    # in its header" and the report's CI section cannot be generated at all.
    #
    # **FN3's goal is that the reviewer can USE the tool.** A tool whose output does not
    # satisfy the next gate in the chain has not met that goal, so the anchor is emitted
    # here rather than left to a convention that happened to hold nine times.
    # **FV3: `args.judged`, NOT `sha()`.** Both lines carry the same value and neither
    # reads HEAD. `sha()` survives for the ancestry check in `_judged`, nowhere else.
    anchor = f"**Reviewed commit: `{args.judged}`.**"
    header = (
        f"# Review — {args.milestone} step {args.step}"
        + (" — ES0 INTERIM CHECK (counts against no round)" if args.interim else "")
        + "\n"
        f"Reviewed commit: {args.judged}\n"
        f"{anchor}\n"
    )
    # FK0: ONE LINE, INTO THIS ENTRY, AND NOTHING OTHERWISE. It goes in the header so
    # that a reader of the NEWEST entry finds it beside `Reviewed commit:` -- the file
    # accumulates newest-first (DX2), so a parser taking the first match gets the
    # current round's line and not an earlier round's. Nothing else about the tool
    # changes: the four refusals, the report check and the accumulation are untouched.
    if args.closes:
        header += f"Closes: {args.closes}\n"

    # THE FILE ACCUMULATES. IT USED TO BE OVERWRITTEN (DX2, R567).
    #
    # This line was `out.write_text(header + body.lstrip())`, so each round replaced
    # the whole file and every earlier round survived only in git history. Measured
    # across four commits, the file went 397 -> 508 -> 508 -> 538 lines while
    # mentions of one withdrawn item went 3 -> 2 -> 2 -> 0.
    #
    # That broke a guard whose premise is stated in its own docstring:
    # `test_no_status_claims_more_than_the_verdict_allows` reads "the WHOLE review
    # file, every round of it, because a withdrawal ruled two verdicts ago is still a
    # withdrawal". Verdict 69 withdrew R567; two rounds later the text was gone, so a
    # report reporting that withdrawal truthfully went red, and twelve tests failed on
    # the one status cell.
    #
    # THE PRIOR ROUNDS ARE PRESERVED VERBATIM, newest first, below a separator. Not
    # merged, not summarised, not re-stamped: whatever the previous round said is what
    # stays on the page, because a record the current reviewer can edit is not a
    # record. The new round's own header goes at the top, so the parsers that read the
    # first `Reviewed commit:` line still find the current one.
    # C42: THE UTF-8 FIX WAS INCOMPLETE AND IT BROKE THIS TOOL ON THE VERY VERDICT
    # THAT FOUND IT. Making both sides UTF-8 fixed new files; it did nothing for a file
    # already on disk with a cp1252 header from the old `write_text` and a UTF-8 body
    # appended after. No single-encoding read can open that, so the reviewer's write
    # crashed and the earlier rounds were unreachable — the exact loss the accumulation
    # exists to prevent, reintroduced by its own repair.
    #
    # The fallback decodes a legacy file byte-for-byte rather than failing, and what is
    # written back is UTF-8, so a mixed file is repaired by the next round that touches
    # it. `latin-1` is the fallback because it maps every byte to a code point and
    # therefore cannot raise; the alternative is losing a round to an encoding.
    previous = ""
    if out.is_file():
        raw = out.read_bytes()
        try:
            previous = raw.decode("utf-8")
        except UnicodeDecodeError:
            previous = raw.decode("latin-1")
            print(
                f"note: {out.name} was not valid UTF-8; decoded as latin-1 and it is "
                "rewritten as UTF-8 below (C42)."
            )
    rounds = header + body.lstrip()
    if previous.strip():
        rounds += (
            "\n\n---\n\n"
            "<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under\n"
            "     DX2: each round is added and no prior round is rewritten or removed. -->\n\n"
            + previous.strip()
            + "\n"
        )
    # UTF-8 EXPLICITLY, ON BOTH SIDES. The original write used the platform default,
    # which is cp1252 here, and the header carries an em dash -- so the file was
    # written in cp1252 and the accumulation's read-back raised
    # `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97`. A round-trip that
    # cannot read what it wrote loses every earlier round, which is the failure this
    # change exists to prevent.
    #
    # AND `newline="\n"`, WHICH IS THE OTHER HALF OF THE SAME ROUND-TRIP (C72, EB2).
    # The read above is `read_bytes().decode()`, so a line already ending `\r\n` keeps
    # its `\r` in `previous`; the write was in text mode, where Python translates every
    # `\n` to the platform terminator. So each preserved line gained one carriage
    # return per round -- `\r\n`, then `\r\r\n`, then `\r\r\r\n` -- and read back with
    # universal newlines the file came out double-spaced, doubling again every round.
    # One verdict file had already accumulated 576 of them before anyone read it that
    # way. The reviewer was normalising to LF by hand before every invocation; this
    # removes the need and the chance of forgetting.
    out.write_text(rounds, encoding="utf-8", newline="\n")
    kept = len(previous.strip().splitlines())
    print(
        f"wrote {out.relative_to(root)}  ({m.group(1)} @ {sha()[:10]}); "
        f"{kept} lines of earlier rounds preserved"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
