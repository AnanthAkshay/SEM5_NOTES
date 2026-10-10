# Handwritten Notebooks Conversion Progress

## Master Checklist

- [x] **Part 0: Baseline & Inventory**
  - [x] Read previous audits, `data/subjects.js`, `css/notes.css`, and verified local assets.
  - [x] Repository and `.git` size audit (`.git`: 192.6 MiB, repo disk total: ~611 MiB).
  - [x] Full baseline inventory of all 24 unit notes pages (headings, callouts, tables, diagrams, formulas, code, word counts).
  - [x] Listed syllabus-only units skipped (Units 4 & 5 for ML, SE, CN, TOC, AI, RMIPR; Labs ISL56 & ISL57).

- [ ] **Part 5: Pilot Phase (TOC Unit 1 & CN Unit 1)**
  - [x] Downloaded & bundled local Google Fonts (`fonts/`) under OFL (Patrick Hand, Caveat, Kalam, Gaegu, Indie Flower, Architects Daughter, Shadows Into Light, JetBrains Mono).
  - [x] Created handwritten notebook stylesheet (`css/handwritten.css`) with ruled lines, red margins, punched holes, inks, and KaTeX integration.
  - [x] Built conversion & pagination engine (`scripts/build_handwritten.js`).
  - [x] Built PDF postprocessing script with bookmarks & metadata (`scripts/postprocess_pdf.py`).
  - [x] Built coverage & fidelity verification gate (`scripts/check_handwritten_coverage.py`).
  - [x] **TOC Unit 1 Pilot**: 25 pages, 1.40 MB, 5,067 words (Ratio: 1.06), 12/12 headings verified.
  - [x] **CN Unit 1 Pilot**: 32 pages, 1.70 MB, 6,835 words (Ratio: 1.00), 10/10 headings verified.
  - [x] Captured and visually inspected 6 representative pages each (contents, text, diagram, table, callout, numerical).
  - [x] Coverage gate: 100% PASS for both pilot units (`audit/handwritten_coverage.md`).

- [ ] **Phase 2: Remaining Units (Pending Approval / Autonomous Pipeline)**
  - [ ] **CN (IS53)**: Unit 2, Unit 3
  - [ ] **TOC (IS54)**: Unit 2, Unit 3
  - [ ] **ML (IS51)**: Unit 1, Unit 2, Unit 3
  - [ ] **AI (ISE552)**: Unit 1, Unit 2, Unit 3
  - [ ] **SE (IS52)**: Unit 1, Unit 2, Unit 3
  - [ ] **RMIPR (AL58)**: Unit 1, Unit 2, Unit 3
  - [ ] **REACT_JS (ISAEC594)**: Unit 1, Unit 2, Unit 3
  - [ ] **EVS (HS510)**: Unit 1, Unit 2, Unit 3

- [ ] **Phase 3: Site Integration & Verification**
  - [ ] Register handwritten entries in `data/subjects.js` (type: "handwritten", generated: true).
  - [ ] Update subject views with handwritten file rows, preview/download links.
  - [ ] Add link cards on HTML notes pages.
  - [ ] Update homepage and search index.
  - [ ] Content-hash verification (zero changes to HTML body text).
