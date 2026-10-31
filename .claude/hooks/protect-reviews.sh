#!/usr/bin/env bash
# PreToolUse hook: the reviewer's directories are not the implementer's.
#
#   docs/reviews/    verdicts, written through scripts/write_verdict.py
#   tests/corpus/    adversarial test data written by the reviewer (BE3)
#
# WHO IS ASKING, and how this hook knows (BG6). The hook's stdin JSON carries
# `agent_type` and `agent_id` when the caller is a SUBAGENT, and omits both when
# it is the main session. Measured, by dumping the JSON from both:
#
#   main session   keys: cwd, effort, hook_event_name, permission_mode,
#                        prompt_id, scratchpad_dir, session_id, tool_input,
#                        tool_name, tool_use_id, transcript_path
#   subagent       the same keys PLUS agent_id and agent_type
#
# So the earlier note that "hook protection is honour-based between two agents on
# one machine" is wrong, and this hook now keys on the identifier: the
# gating-supervisor may write those directories and nothing else may.
#
# IT ALSO COVERS Bash NOW. The previous version matched Write|Edit|MultiEdit
# only, so a shell redirect went straight past it -- the implementer could have
# written a verdict with `>`.
#
# The Bash rule looks for WRITE INTENT, not for the directory name. A first
# version scanned the whole command string and denied this hook's own commit,
# because the commit MESSAGE mentioned `docs/reviews/` -- it would equally have
# denied `grep`, `cat` and `git log` on those paths, which is both useless and
# the kind of guard people route around. So the match is:
#
#   * a redirect (`>` / `>>`) whose target contains the directory;
#   * a mutating verb -- tee, cp, mv, rm, install, truncate, dd, touch -- in the
#     same command segment as the directory;
#   * `sed -i` in the same segment;
#   * `git checkout|restore|rm|mv` in the same segment.
#
# THREE HOLES THE REVIEWER MEASURED, TWO CLOSED HERE (BH5):
#
#   1. `cd tests/corpus && echo x > y` was ALLOWED -- the protected path is in
#      one segment and the write in another. Closed: for a caller that is not the
#      supervisor, ANY command mentioning a protected directory together with a
#      redirect or a mutating verb ANYWHERE in it is denied.
#
#      "Over-blocking the implementer costs nothing" was WRONG as first written.
#      The scan also listed a bare `cd` as write intent, which denied every READ
#      of a verdict made from a command beginning with `cd` -- nearly all of
#      them, and it blocked the first attempt to read the eighth verdict. The
#      `cd` clause bought nothing: `cd tests/corpus && echo x > y` is already
#      caught by the redirect in the same command string. Over-blocking a WRITE
#      costs nothing; over-blocking a READ costs the ability to work.
#
#      That sentence had to be applied twice more. The whole-command redirect
#      match also fired on `2>&1`, so `pytest ... 2>&1` on a path under
#      tests/corpus/ was denied -- a read, again. The redirect clause now ignores
#      file-descriptor redirections. THE PATTERN, recorded because it is the
#      third instance: every widening of this rule has cost a read and bought
#      nothing, because the implementer's writes here are already caught by the
#      narrow forms.
#
#      AND THEN THE THIRD FIX OVER-CORRECTED (R84). "Ignore file-descriptor
#      redirections" was implemented as "ignore any redirect preceded by a
#      digit", which cleared `2> <protected path>` -- a write. The exemption is
#      now the two things that write no file: `>&`, and a redirect to the null
#      device.
#
#      THE MATRIX IS RUN IN BOTH DIRECTIONS on every change to this clause, and
#      the run is pasted into the commit that makes the change. Four of the four
#      defects in this hook were found by someone hitting them, not by the hook
#      being exercised; a guard whose only evidence is that it has not fired is
#      not evidence.
#   2. Malformed JSON FAILED OPEN -- the python helper printed nothing, `agent`
#      and `hit` came back empty, and the case fell through to `exit 0`. Closed:
#      the helper prints a sentinel on any parse failure and the hook denies.
#   3. `NotebookEdit` was not in the matcher. Closed in settings.json -- and
#      NOT closed in the hook, which read only `file_path` and `path`, so
#      `notebook_path` resolved to the empty string and the call was ALLOWED for
#      three further rounds. Half a fix, on a hole whose two halves live in two
#      files. Closed properly: the hook reads every key a tool names a target
#      with, and the matrix carries a row per key.
#
# LIMITATION that remains, stated because it decides what this is worth: a path
# assembled at runtime from pieces is not caught, and neither is a mutating verb
# outside the list. It takes accidental writes to zero and makes a deliberate one
# require intent; the outside witness's commit-separation check remains the guard
# that does not depend on this hook at all.

input=$(cat)

# python3 does not exist on every machine this repo is worked on (Windows/Git
# Bash has `python`). Both hooks FAIL CLOSED when the interpreter is missing.
PY_BIN=$(command -v python3 || command -v python || true)
if [ -z "$PY_BIN" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"No python interpreter found; protect-reviews.sh cannot resolve the target path and would FAIL OPEN. Denying by default."}}\n'
  exit 0
fi

read -r agent hit <<EOF
$(printf '%s' "$input" | "$PY_BIN" -c '
import json, re, sys

PROTECTED = r"(?:docs[/\\]+reviews|tests[/\\]+corpus)"
VERBS = r"(?:tee|cp|mv|rm|install|truncate|dd|touch)"

try:
    d = json.load(sys.stdin)
    ti = d.get("tool_input", {}) or {}
except Exception:
    # FAIL CLOSED. Input this hook cannot parse is input it cannot clear.
    print("- unparseable")
    raise SystemExit(0)
agent = d.get("agent_type") or "-"

# EVERY key a tool names a target with, not the two the editing tools use
# (R78, hole 3, open since the third round). `NotebookEdit` passes
# `notebook_path`, so a verdict written as a notebook went straight past a
# hook whose whole job is that directory. The matcher in settings.json was
# fixed to LIST NotebookEdit; the hook still could not see its argument.
path = next((ti[k] for k in ("file_path", "path", "notebook_path")
             if ti.get(k)), "")
command = ti.get("command") or ""

hit = "none"
if re.search(PROTECTED, path):
    hit = "reviews" if re.search(r"docs[/\\]+reviews", path) else "corpus"
elif command and re.search(PROTECTED, command):
    # WHOLE COMMAND, not per segment (BH5 hole 1). Segmenting let
    # `cd tests/corpus && echo x > y` through: the path was in one segment and
    # the write in another. A caller that is not the supervisor has no
    # legitimate write here, so any write shape anywhere in a command that
    # mentions a protected directory is refused.
    # A REDIRECT IS A WRITE WHERE ITS TARGET IS, NOT WHERE THE COMMAND HAPPENS
    # TO MENTION A PATH (FX1). This is the FOURTH instance of the pattern this
    # hook records about itself, and the first in which the over-refusal blocked
    # the repair for it: the patch command below was itself denied, because its
    # text named the directory and it had a redirect to the scratchpad.
    #
    # The previous form asked only WHETHER a redirect appeared anywhere in a
    # command mentioning a protected directory. The matrix pasted into the FX
    # commit shows that denying four reads and no additional write, among them
    # the one FX was raised for:
    #
    #   python scripts/carried_table.py <a verdict> <answers.json> > <scratchpad>
    #
    # a committed generator whose INPUT is the verdict and whose OUTPUT is the
    # scratchpad -- and `tests/test_report_carried.py` re-runs it and compares
    # against what the report committed, so its table cannot be hand-written
    # instead. Also denied: `wc -l <a verdict> > /tmp/n`, the same command with
    # `2>&1`, and a pytest run over corpus DATA with its output in a file.
    #
    # So targets are extracted and tested one by one. `2>&1` yields no target,
    # because `&` is outside the target character class, and `> /dev/null`
    # yields a target that simply is not protected -- which is why the R84
    # exemption list is GONE rather than extended. It was a list of shapes that
    # write no FILE, and asking where the file IS answers that question without
    # a list anyone has to keep complete. The R84 defect was an incomplete
    # version of exactly that list.
    #
    # NO APOSTROPHES ANYWHERE IN THIS BLOCK, and that is load-bearing rather
    # than style: the whole helper is one single-quoted shell argument, so an
    # apostrophe in a COMMENT terminates it. Three of them in the first draft of
    # this very clause did, bash raised a syntax error, `2>/dev/null` swallowed
    # it, and the hook ALLOWED a Write straight at a verdict. See the empty-hit
    # guard below, which is what makes that loud instead.
    targets = [m.group(2) for m in re.finditer(r"([0-9]*)>>?\s*([^\s;|&<>]+)", command)]

    # BH5 HOLE 1 IS NOT REOPENED, AND IT NEEDS ITS OWN CLAUSE NOW. The hole was
    # `cd tests/corpus && echo x > y`: a RELATIVE target resolved against a
    # protected cwd, so no target string names the directory. The broad match
    # caught it incidentally; this catches it on purpose. The note above saying
    # "the `cd` clause bought nothing" was true while the broad match existed
    # and is false now -- with targets tested individually this clause is the
    # only thing between that command and an allow, which the matrix checks in
    # both the corpus and the reviews direction.
    cd_into = re.search(r"\bcd\s+[^\s;|&]*" + PROTECTED, command)

    writes = (
        any(re.search(PROTECTED, t) for t in targets)
        or (cd_into and targets)
        or re.search(r"\b" + VERBS + r"\b", command)
        or re.search(r"\bsed\b[^\n]*-i", command)
        or re.search(r"\bgit\b[^\n]*\b(?:checkout|restore|rm|mv)\b", command)
    )
    if writes:
        hit = ("reviews" if re.search(r"docs[/\\]+reviews", command)
               else "corpus")
print(agent, hit)
' 2>/dev/null)
EOF

# THE HELPER NOT RUNNING AT ALL IS A FOURTH FAIL-OPEN ROUTE, AND IT WAS OPEN
# UNTIL THIS COMMIT (found while making the FX change, by the matrix FX requires).
#
# BH5 hole 2 closed the case where the helper RUNS and cannot parse its JSON: it
# prints `- unparseable` and the case below denies. Nothing covered the case
# where the helper does not run -- a shell syntax error inside the single-quoted
# block, a python that dies on import, a machine where the interpreter exists but
# the block is malformed. Then `$(...)` is empty, `read` leaves both variables
# empty, no `case` arm matches, and the hook falls through to `exit 0`: ALLOW.
#
# Measured, because that is how it was found: three apostrophes in a comment in
# the clause above broke the quoting, and the matrix went from 18 writes denied
# to 24 rows ALLOWED -- `Write` at a verdict, `rm` of a verdict and unparseable
# input among them. `bash -n` passed, because the shell syntax is still valid
# once the quotes rebalance, and `2>/dev/null` hid the error from the operator.
#
# The helper prints two tokens on every path it can reach, so an empty `hit`
# means it did not reach any of them. That is input this hook cannot clear.
if [ -z "$hit" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"protect-reviews.sh produced no decision at all -- its helper did not run (a quoting or interpreter failure, not a parse failure). A hook that cannot answer cannot clear a request, so this fails CLOSED. Run the hook by hand without 2>/dev/null to see the error."}}\n'
  exit 0
fi

# The reviewer writes these directories. Nobody else does, including any other
# subagent: a general-purpose agent has no business writing a verdict either.
if [ "$agent" = "gating-supervisor" ]; then
  exit 0
fi

case "$hit" in
  unparseable)
    cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"protect-reviews.sh could not parse its own hook input. A hook that cannot read the request cannot clear it, so this fails CLOSED (BH5)."}}
EOF
    ;;
  reviews)
    cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"docs/reviews/ is written only by the gating-supervisor, through scripts/write_verdict.py. The implementer does not write, edit, or delete verdicts -- and this now covers Bash as well as the editing tools, so a shell redirect is refused too."}}
EOF
    ;;
  corpus)
    cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"tests/corpus/ holds adversarial cases written by the REVIEWER (BE3). A check measured against a corpus its own author wrote measures nothing; that is why this directory is not the implementer's. Write the check, not the cases it is scored against."}}
EOF
    ;;
esac
exit 0
