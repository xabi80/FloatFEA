#!/usr/bin/env python3
"""Write a supervisor verdict to docs/reviews/F<n>/step-<k>.md.

Used only by the gating-supervisor agent. The editing tools are blocked from
docs/reviews/ by a PreToolUse hook; this is the one sanctioned path in.

Usage:
    python scripts/write_verdict.py --milestone 2 --step 5 < review.md

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

The `Reviewed commit:` stamp is taken from `HEAD`, which is structurally NOT the
reviewed commit whenever the reviewer commits its corpus first -- as it is
instructed to. The body names the commit it judged; that line does not. Recorded
here rather than fixed, because changing what the stamp reads is a change to the
reviewer's own tooling and goes through a directive, not through this edit.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REQUIRED = ("## Carried", "## Findings", "## Tolerances touched", "## Next step opens when")
VERDICTS = ("PASS", "HOLD", "STOP")


def sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--milestone", type=int, required=True)
    ap.add_argument("--step", type=int, required=True)
    args = ap.parse_args()

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
    report = root / f"docs/reports/F{args.milestone}/step-{args.step}.md"
    if not report.exists():
        sys.exit(f"refused: no step report at {report}")

    out = root / f"docs/reviews/F{args.milestone}/step-{args.step}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    header = f"# Review — F{args.milestone} step {args.step}\nReviewed commit: {sha()}\n"

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
    previous = out.read_text(encoding="utf-8") if out.is_file() else ""
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
    out.write_text(rounds, encoding="utf-8")
    kept = len(previous.strip().splitlines())
    print(
        f"wrote {out.relative_to(root)}  ({m.group(1)} @ {sha()[:10]}); "
        f"{kept} lines of earlier rounds preserved"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
