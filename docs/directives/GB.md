# DIRECTIVE GB — SR-28 ruling and step-4 start

Received 3 November 2026. Recorded verbatim on receipt, as the first commit of the turn,
under FP0. The text below is the directive exactly as given; nothing in it is paraphrased,
reordered or summarised.

```
DIRECTIVE GB — SR-28 ruling and step-4 start
Record: docs/directives/GB.md.

GB1 — SR-28: AUTHORISED as a standalone `plan:` commit.
  - Change ONLY the section headers of docs/milestones/R1.md so they match
    the renumbering the plan itself states ("Four steps, not three… the
    renumbering is below").
  - No change to any step's content, closing conditions, scope or order.
  - Put the header diff (old → new, one line each) in the commit message
    and the digest.
  - If the plan's renumbering text does not say which content is step 4,
    do not pick one. Escalate with both readings, recommended first.
  - Correction: my GA5 said "step 4, then FL3". That was my wording, not
    a ruling. The plan's renumbering governs which work is step 4.

GB2 — Step 4's first commit, as you proposed:
  - R1139's held patch and its three declaration rows
  - the step-4 report skeleton and the marker
  It returns for review at no step's cost.
  R1139's narrowing (a stemless dotfile is a site only once it exists) is
  accepted as documented.

GB3 — R1141 (R1135's sentence never reduced): answer it in step 4. Make
  the edit wherever the sentence lives now. If it lives only in the
  closed step-3 report (EK3), the step-4 report carries the correction
  and points to it. Count it in the digest's self-found line under GA4,
  with no essay.

GB4 — Reminder of GA4: daily digest, one screen. This handback was a
  narrative. Next time, digest only.

Before GB1: confirm in one line that everything is pushed and no
worktree holds unpushed work, so Xabier can move the repo off OneDrive.
```

## GA IS MISSING FROM THIS RECORD, AND I CANNOT RECONSTRUCT IT

GB cites two of its own predecessor's clauses — **GA4** (daily digest, one screen) and
**GA5** (which GB1 now corrects as wording rather than a ruling). There is no
`docs/directives/GA.md`, and GA is cited **nowhere else in the repository either**:

    claim  GA is cited in no file in this repository outside this one
    cmd    grep -rn "GA[0-9]" --include='*.md' docs/ CLAUDE.md | grep -v '^docs/directives/GB.md'
    out    (no output)

**This is C25 again — the exact defect FP0 was adopted for**, one directive letter later.
GA was acted on (the digest format is GA4's) and recorded in no file, so the only surviving
text of GA4 and GA5 anywhere in this repository is GB's two quotations of them above.

I am **not** reconstructing it. FL.md is reconstructed from a session summary and the
README says so because the summary was faithful in substance; here I have no summary of GA
at all, and a record that invents a directive's wording is worse than a record that says it
is missing. If GA's message is still available, it should be committed as `GA.md` under FP0
and this section replaced by a pointer.
