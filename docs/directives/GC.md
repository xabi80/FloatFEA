# DIRECTIVE GC — reissue GA, rulings on the 4–5 Nov handback, focus on FL3

Received 4 November 2026. Recorded verbatim on receipt, as the first commit of the turn,
under FP0. The text below is the directive exactly as given; nothing in it is paraphrased,
reordered or summarised. **GC0 is reproduced here as part of GC and also in its own file,
`GA.md`, which is where GC's own `Record:` line sends it.**

```
DIRECTIVE GC — reissue GA, rulings on the 4–5 Nov handback, focus on FL3
Record: docs/directives/GA.md (the text in GC0, verbatim, dated as
received now; note in it that it was issued earlier in the supervisor
channel but never delivered) and docs/directives/GC.md. One commit.

GC0 — DIRECTIVE GA (as originally issued; GA6 replaced by GC5)
  GA1 — Apparatus freeze. No new guards, generators, matrix harnesses or
    hook clauses on the review/report apparatus until R1 is tagged. An
    apparatus defect is fixed ONLY if it could hide a blocking finding or
    make a wrong engineering result look green (the R1117 class).
    Otherwise it gets one ledger line, with no investigation and no
    census of sibling sites.
  GA2 — Pushes. Push only immediately before invoking the reviewer (FP1)
    or at end of day. One push per answered round.
  GA3 — Reviewer invocation. For the remaining R1 rounds, the invocation
    asks for:
      - blocking findings in full
      - non-blocking findings as one ledger line each
      - apparatus findings only under the GA1 test
    Target verdict length: 150 lines or fewer. This does not limit what
    the reviewer may rule blocking.
  GA4 — Reporting. FZ digest only, one screen. No running narrative.
    Self-found defects: a count plus one line each. Corrections to your
    own earlier claims: one line each.
  GA5 — Priority is tool function. Any R1 item not yet started that is
    apparatus, or documentation beyond USER_GUIDE.md, goes to R2.

GC1 — SR-28 withdrawal: accepted. The fence note is fine.

GC2 — FP1 vs CK0, ruled: for a commit whose diff touches only
  paths-ignored files, FP1 is satisfied by the concluded CI run at its
  nearest ancestor that has a run, provided
  `git diff --name-only <ancestor>..<judged>` lists only paths-ignored
  paths. The report states both shas, the diff listing and the run id.
  No workflow change.

GC3 — R1149 (EG4(e) corpus pause expired 28 Oct): leave it expired.
  The reviewer runs corpus batches at its own discretion, under GA3's
  length target. No extension directive.

GC4 — R1147, R1148, R1150–R1154: apply GA1. Fix in revision 2 only
  those that could hide a blocking finding or a wrong engineering
  result. Ledger the rest, one line each. R1150's three wrong citations
  (EQ0 → GB2) are a one-line text fix. Do it, no essay.

GC5 — Repo move (replaces GA6). After recording GA and GC: confirm
  `git rev-list --all --not --remotes=origin` is 0, then STOP and say
  "ready to move". Xabier clones to a non-OneDrive folder and restarts
  you there. On restart:
    - confirm the clone's HEAD matches origin
    - run the unit tier once as a sanity check
    - continue

GC6 — Revision 2 = FL3's substance. Write docs/USER_GUIDE.md first,
  aimed at a reader who has never seen the repo. It covers:
    - install
    - the YAML config: every key, its units, model vs full scale, λ
    - `floatfea run` and `floatfea export`
    - what each output file contains, including the superseded-row flag
    - the refusals a user will meet (heading range, the wave-height pair
      vs λ, the BEM headings refusal, the period band) and how to fix
      each
    - the golden example end to end (U = 1.71167)
  Then the fresh-agent witness. The witness gets only USER_GUIDE.md and
  the repo. It must reproduce the golden result and one modified config
  without help. Record every place it got stuck. Each one is a guide
  defect: fix the guide, not the witness.
  Target: revision 2 to the reviewer by end of 8 Nov, leaving two
  rounds before 10 Nov.
```

## What changes in the loop

Recorded as pointers, not as a reading — GA4 is one screen and GA1 retires the census.

* **GA1** — until R1 is tagged, an apparatus defect is fixed only under its two-part test;
  otherwise one ledger line, **no investigation and no census of sibling sites**.
* **GA2** — push only immediately before invoking the reviewer, or at end of day, one per
  answered round. **GC5 overrides it for this turn**: Xabier clones from GitHub, so this
  commit is pushed when it is made.
* **GA3** — carried into the reviewer invocation verbatim. It does not limit what the
  reviewer may rule blocking, and touches neither FR1's heads nor the ES0 cap.
* **GA5 / GC6** — apparatus and documentation beyond `USER_GUIDE.md` go to R2.
* **GC2** — resolves the FP1/CK0 tension this milestone escalated. Step 4's §10 pasted the
  judged commit's own `git show --stat`, not the ancestor-to-judged diff GC2 names:

        claim  §10 states the ancestor and its conclusion, but no ancestor..judged diff
        cmd    grep -c 'git diff --name-only' docs/reports/R1/step-4.md
        out    2        -- both inside R1053's ledger rows (:541, :937), neither in §10
        cmd    sed -n '3275p' docs/reports/R1/step-4.md
        out    cmd    git show --stat --format='' HEAD

  Revision 2 states both shas, the `--name-only` listing and the run id.
* **GC3** — EG4(e) stays expired; R1149 is answered without a new directive.
* **GC4** — the disposition of verdict 48's eight items, under GA1 rather than item by item.
* **GC6** — revision 2 to the reviewer by **end of 8 November**, two rounds before FR0's
  10 November date.
