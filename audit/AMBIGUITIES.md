# SEM 5 · Folder Synchronisation & Ingestion Ambiguities

This document records architectural decisions made while ingesting the reorganised subject folders into the unified `notes/` layout.

---

## 1. 'Recent Notes' vs. 'Older versions / Vercel Notes'

### Policy Decision:
1. **Primary Surface:** The files located in `Recent Notes/` represent the student's latest semester materials and take top prominence in each subject view.
2. **Older Versions Grouping:** Where `Vercel Notes/` contains distinct slides/documents from past years or alternate professors, they are placed under an explicit `Older versions` collapsible group so students can still reference them without cluttering the primary view.
3. **Deduplication:** Where a file in `Vercel Notes/` is byte-identical to a file in `Recent Notes/` (e.g. `TOC_Notes.pdf`), only the primary version in `Recent Notes/` is served; the duplicate is not duplicated in `subjects.js`.

### Per-Subject Summary:
- **IS51 (ML):** `Recent Notes/` contains the latest 14 chapter slide decks and notes from Prof. Shruti M, plus lab notebooks. `Vercel Notes/` does not exist here. Impromptu duplicate `Chapter_5_4_Validation_of_Regression_Methods_Detailed (1).pptx` was deduplicated.
- **IS52 (SE):** `Recent Notes/` contains AY 2026–27 Unit 1.1, 1.2, 1.3, 2.1, 2.2 PPTXs. `Vercel Notes/` has older 2024–25 notes and PPTs (covering Units 1–5). Unit 1 and 2 PPTs in `Vercel Notes/` are marked as `Older versions`, while Units 3, 4, 5 are kept on the out-of-scope hold list.
- **IS53 (CN):** `Recent Notes/` contains the massive comprehensive `CN-UNIT1 Complete.pptx`, `CN-Unit2 Complete.pptx`, and `Unit3a.pptx`. `Vercel Notes/` contains older last-year chapter-by-chapter PPTs (`ch03.pptx`, `ch04.ppt`, `ch19.ppt`, etc.). These last-year PPTs are placed under a collapsed `Older versions (last year slides)` group.
- **IS54 (TOC):** `Recent Notes/` contains the complete handwritten scanned `TOC_Notes.pdf` (45.5 MB). `Vercel Notes/` contains individual unit PDF extractions (`Unit 1.pdf`, `Unit 2.pdf`, `Unit 3.pdf`). Both are valuable: `TOC_Notes.pdf` is primary, and unit-wise PDFs serve as unit-specific downloads.
- **HS510 (EVS):** `Recent Notes/` contains 5 modular topic PDFs for Unit 2 and Unit 1–5 PPTXs. `Vercel Notes/` contains merged `Unit-1 Notes, MCQ & Questions.pdf`, `Unit-2 Notes...`. Both are preserved: modular PPTXs and topic PDFs in primary, merged study packs in practice/older.
- **AL58 (RMIPR):** `Recent Notes/` contains Unit 1–3 PPTXs and worksheets. `Other_Component/` contains Assignments and Quizzes. `Vercel Notes/` contains older unit PDFs. Assignments/Quizzes go to `practice/`, primary PPTXs to `recent-notes/`.
- **ISE552 (AI):** `Recent Notes/` contains professor PDFs on search algorithms (`AI-Intelligent_Agents`, `Uninformed_Search`, `Informed_Search`, `Local_Search`, `Adversarial_Search`). `Vercel Notes/` has older consolidated Unit 1 and Unit 2 PDFs. Consolidated PDFs are kept in older versions.

---

## 2. CIE-1 Scope & Out-of-Scope Hold Policy

Per `data/scope.json`, only materials strictly corresponding to CIE-1 (13–16 Oct 2026) are active on the primary subject tabs:
- **In-Scope Units:**
  - AI: Units 1 & 2
  - CN: Units 1, 2, 3 (up to IPv4 Classless addressing)
  - EVS: Units 1 & 2
  - ML: Units 1, 2, 3 (Regression portion only)
  - ReactJS: Units 1 & 2
  - RMIPR: Units 1, 2, 3 (up to Good Sample Design)
  - SE: Units 1 & 2 (AY 2026–27 syllabus)
  - TOC: Units 1 & 2

- **Hold List (Preserved in filesystem, kept off active CIE-1 study index):**
  - All Unit 4 and Unit 5 notes across all subjects.
  - Unit 3 for EVS, TOC, AI, SE, ReactJS.
  - Out-of-scope portions of Unit 3 for ML, CN, RMIPR.

---

## 3. Question Papers (CIE vs. SEE)

- **CIE Papers:** Placed under `notes/<subject>/practice/` and surfaced as primary practice for the upcoming CIE-1 exam.
- **SEE Papers:** (Semester End Examination papers from 2022–2026). Placed under `notes/<subject>/practice/see/` and clearly tagged as `SEE Question Paper` so students know they test the entire semester syllabus, not just CIE-1.

---

## 4. Textbooks & Copyright Handling

- Textbooks found in `AL58 - RM/Books`, `HS510 - EVS`, `IS51 - ML/ML-THEORY`, `IS52 - SE/Book`, `IS53 - CN/BOOK`, `ISAEC591 - Eco/Book` are quarantined into `.gitignore` protected `sources/textbooks/`.
- They will never be tracked in git, served over HTTP, or indexed in search.

---

## 5. Lab Manuals & Jupyter Notebooks (`.ipynb`)

- ML Lab programs (`ML-1.ipynb`, `ML-Prog2.ipynb`, `ML-Prog-3.ipynb`) and SE Kanban Lab Manual are placed under `notes/<subject>/lab/`.
- `.ipynb` files will have rendered HTML previews alongside raw `.ipynb` download links.

---

## 6. Strict Notes Policy: Interactive HTML + Handwritten + Recent Notes Only (Branch `only-recent-notes`)

Per user directive on branch `only-recent-notes`:
1. **Strict Unit Notes Structure:** Under the `Notes & Docs` tab for every subject, every unit displays ONLY and EXACTLY:
   - **Row 1:** Interactive HTML Notes (`Unit N: Interactive Notes`)
   - **Row 2:** Handwritten Notebook (`Handwritten notebook (PDF)`)
   - **Row 3+:** Recent Notes — files mapped directly from the student's authoritative recent notes folder for that unit.
2. **Removal of Old/Duplicate Slides:** All older faculty slide decks, old alternate/condensed TOC notes, chapter presentations, and past semester duplicate PDFs were unlinked from the site, un-indexed from search, and safely moved out of the served tree into the gitignored directory `archive/removed-from-site/<subject>/`. Over 186.4 MB (and over 230 MB with older archives) was pruned from the served tree, significantly shrinking the deployment payload.
3. **Preservation of Non-Notes Categories:**
   - **Solved PYQs:** Preserved in the dedicated `Solved PYQs` tab with interactive answers and vector handwritten revision sheets.
   - **Practice & Question Papers:** Preserved in the `Practice` tab with CIE and SEE question paper bundles.
   - **Official Syllabus Documents:** Preserved in the `Syllabus & Books` tab.
   - **Laboratory Manuals & Notebooks:** Preserved in the `Laboratory` tab.
   These categories are NOT study "notes" and remain intact without polluting the unit study note hierarchy.
4. **Encoding & Title Sanity:**
   - Eradicated all mojibake sequences (e.g. `Ãƒâ€šÃ‚·`, `Â`, `â€`).
   - Fixed copy-pasted title bugs (e.g. "Requirements Engineering" incorrectly assigned to TOC and ML).
   - Created automated audit script `scripts/verify_no_mojibake.py` to enforce zero encoding errors in CI/testing.

---

## 7. AI (ISE552) Recent Notes Resolution & Problem-Solving Variant

1. **`AI-2.pdf` vs Unit Assignment:**
   - Rendered inspection proved `AI-2.pdf` is the comprehensive lecture presentation for Unit 1 (*Introduction to Artificial Intelligence & Intelligent Agents*). Mapped to `Unit 1 Recent Notes` as `ai-intelligent-agents-intro.pdf`.
2. **`AI-Intelligent_Agents.pdf` vs `AI-Intelligent_Agents-PS.pdf`:**
   - Both files cover Problem-Solving Agents (Initial State, Actions, Transition Model, Goal Test, Path Cost, Bengaluru → Hyderabad state space).
   - `AI-Intelligent_Agents.pdf` contains 15 slides.
   - `AI-Intelligent_Agents-PS.pdf` contains the exact same 15 content slides plus a 16th trailing blank slide.
   - To preserve both without confusion while maintaining distinct metadata:
     - `AI-Intelligent_Agents.pdf` is registered as `"Problem-Solving Agents & State-Space Formulation"` (`ai-problem-solving-agents.pdf`).
     - `AI-Intelligent_Agents-PS.pdf` is registered as `"Problem-Solving Agents (Problem Set & Formulation)"` (`ai-problem-solving-agents-ps.pdf`).
3. **Local Search & Adversarial Search Scope:**
   - In the MSRIT ISE552 syllabus, Local Search and Adversarial Search are explicitly topics 4 and 5 of **Unit 2** (NOT Unit 3).
   - Since Unit 2 is fully in CIE-1 scope, both `ai-local-search.pdf` and `ai-adversarial-search.pdf` are 100% in-scope under Unit 2.
4. **Important Questions Board Photo:**
   - The WhatsApp image lists 9 core Unit 1 questions. Preserved under `notes/ai/recent-notes/ai-important-questions.jpg` and registered in Unit 1 Recent Notes. Full model answers are accessible on both the Unit 1 HTML page and the AI Solved PYQs page.


