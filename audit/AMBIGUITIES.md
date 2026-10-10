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
