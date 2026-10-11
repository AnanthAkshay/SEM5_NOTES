# Repository Branch & Push State Audit

Date: 11 October 2026, 17:46 IST  
Baseline Tag: `pre-se-important-q` (commit `efc1a37`)

---

## 1. Local Branches Summary

| Branch | HEAD Commit | Subject / Goal | Status vs `main` | Status vs Upstream Remote | Notes |
|---|---|---|---|---|---|
| `main` | `efc1a37` | Production branch | Active base (0 ahead, 0 behind) | In sync with `origin/main` | Deployed to GitHub Pages |
| `se-important-q` | `c316a30` | Add SE Important Questions PDF & tests | **6 commits ahead**, 0 behind | In sync with `origin/se-important-q` | Ready to merge into `main` |
| `ai-unit12-pdfs` | `efc1a37` | Show only Unit-1/Unit-2 recent PDFs | 0 ahead, 0 behind | Fully merged into `main` | Completed |
| `ai-unit12-notes` | `0536fd5` | AI Unit 1 & 2 lecture notes | 0 ahead, 8 behind | Incorporated into `main` | Completed |
| `ai-recent-notes-sync` | `a197205` | AI recent notes sync | 0 ahead, 20 behind | Incorporated into `main` | Completed |
| `only-recent-notes` | `e9656de` | Only HTML + Handwritten + Recent Notes | 0 ahead, 37 behind | Incorporated into `main` | Completed |
| `sync-notes-folders` | `2d91847` | Initial notes folders reorganization | 0 ahead, 38 behind | Incorporated into `main` | Completed |
| `cie1-rebuild` | `14d8fa9` | CIE-1 scope rebuild & portal repair | 0 ahead, 39 behind | Incorporated into `main` | Completed |

All 7 historical local branches (`ai-unit12-pdfs`, `ai-unit12-notes`, `ai-recent-notes-sync`, `only-recent-notes`, `sync-notes-folders`, `cie1-rebuild`) have **0 unmerged commits ahead of main**. Their histories were linearly integrated into `main`.

---

## 2. Uncommitted Working Directory State

- **Tracked Modified Files:** None (`working tree clean`).
- **Untracked Diagnostic Artifacts (in `audit/`):**
  - Diagnostic JSON files (`lh-home.json`, `lh_cn_u2.json`, `lh_ml_u1.json`, `protected_snapshot_se_important_q.json`, `se_important_topics_extracted.json`, etc.) generated during automated verification.
  - Excluded from production site commits to prevent repository bloat.

---

## 3. SE Granular Commits on `se-important-q`

1. `d5bb259` — `se: add se-units-1-2-important-questions.pdf`
2. `5e9f232` — `se: register Unit 1 and 2 important questions in subjects.js`
3. `a56eb83` — `search: update SE entries in notes index`
4. `773956f` — `cache/progress: bump versions`
5. `c83e3f3` — `docs: update README SE row`
6. `c316a30` — `test: SE important questions verification suite`

All 6 commits pushed to `origin/se-important-q`.
