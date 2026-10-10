# 🎓 SEM 5 · ISE Notes Portal

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Deploy-success?style=for-the-badge&logo=github)](https://ananthakshay.github.io/SEM5_NOTES/)
[![Semester](https://img.shields.io/badge/Semester-V%20(5th%20Sem)-indigo?style=for-the-badge)](https://ananthakshay.github.io/SEM5_NOTES/)
[![Department](https://img.shields.io/badge/Department-ISE-blue?style=for-the-badge)](https://ananthakshay.github.io/SEM5_NOTES/)
[![Tech Stack](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20Vanilla%20JS-amber?style=for-the-badge)](https://ananthakshay.github.io/SEM5_NOTES/)
[![License](https://img.shields.io/badge/License-MIT%20%2F%20Academic-emerald?style=for-the-badge)](LICENSE)

> **Department of Information Science & Engineering (ISE) · Semester V**  
> A bespoke, lightweight, and data-driven study portal crafted for 5th Semester ISE engineering students. Built with pure HTML5, modern CSS3 variables, and vanilla JavaScript—zero external build steps, 100% relative paths, and instant deployment on GitHub Pages.

> [!IMPORTANT]
> **CIE-1 Examination Scope & Verification Notice**:  
> The portal has been strictly trimmed and rebuilt for the **5th Semester CIE-1 Examinations (13–16 October 2026)**. All definitions, algorithm traces, network diagrams, and numerical calculations are compiled directly from prescribed textbooks, faculty lecture slides, and department question papers. Out-of-scope portions are archived under git tag `pre-cie1-scope`. See [`CIE1_SCOPE.md`](./CIE1_SCOPE.md) for full authoritative scope boundaries.
> 
> **CIE-1 Syllabus Coverage (19 In-Scope Units & 8 Solved PYQ Banks)**:  
> - **Computer Networks (`24IS53`):** Units 1, 2, 3 up to "IPv4 Addressing – Classless" (CIDR/VLSM included; NAT/IPv6 out)  
> - **React JS (`24ISAEC594`):** Units 1 & 2 (Full)  
> - **Artificial Intelligence (`24ISE552`):** Units 1 & 2 (Full) + Faculty 9-question priority list  
> - **Software Engineering (`24IS52`):** Units 1 & 2 (Full)  
> - **Machine Learning (`24IS51`):** Units 1, 2, 3 (Regression portion only; KNN/Decision Trees out)  
> - **Research Methodology & IPR (`24AL58`):** Units 1, 2, 3 up to "Characteristics of a Good Sample Design"  
> - **Environmental Studies (`24HS510`):** Units 1 & 2 (Full)  
> - **Theory of Computation (`24IS54`):** Units 1 & 2 (Full)

🌐 **Live Website**: [https://ananthakshay.github.io/SEM5_NOTES/](https://ananthakshay.github.io/SEM5_NOTES/)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Subject Coverage & Inventory](#-subject-coverage--inventory)
- [Project Architecture](#-project-architecture)
- [Single Source of Truth (`data/subjects.js`)](#-single-source-of-truth-datasubjectsjs)
- [How to Add or Edit Content](#-how-to-add-or-edit-content)
  - [1. Adding a New Unit Note](#1-adding-a-new-unit-note)
  - [2. Adding Practice Papers or Question Banks](#2-adding-practice-papers-or-question-banks)
- [Interactive Notes Template & Tooling](#-interactive-notes-template--tooling)
  - [Canonical Template Structure](#canonical-template-structure)
  - [Re-Applying Template Shell (`scripts/apply_notes_template.py`)](#re-applying-template-shell-scriptsapply_notes_templatepy)
  - [Automated Style & Content Regression Testing (`scripts/check_notes_style.js`)](#automated-style--content-regression-testing-scriptscheck_notes_stylejs)
- [Local Development](#-local-development)
- [GitHub Pages Deployment](#-github-pages-deployment)
- [Browser Compatibility & Accessibility](#-browser-compatibility--accessibility)
- [License](#-license)

---

## 💡 Overview

Preparing for Semester V requires rapid access to clean unit notes, lecture presentations, practice question papers, and syllabus schemes across all core and elective subjects.

This study website consolidates materials into an intuitive web interface with:
- **Zero Build Toolchain**: No Node build steps or bulky dependencies. Fast load times and high Lighthouse performance.
- **In-Browser Document Reader**: PPTX and DOCX notes converted to high-fidelity PDFs for instant in-browser previewing, while preserving original file downloads.
- **Data-Driven Decoupling**: All subjects, units, notes, labs, and syllabus schemes reside in [`data/subjects.js`](./data/subjects.js). Modify content without touching any HTML.

---

## 🌟 Key Features

### 🔍 Instant Global Search (`Ctrl+K` or `/`)
- Instant keyword filtering across subject names, course codes, unit titles, document filenames, and transcribed syllabus topics (e.g. *Pumping Lemma*, *Scrum*, *PEAS*, *Candidate Elimination*).
- Keyboard navigable with <kbd>↑</kbd> <kbd>↓</kbd> arrows and <kbd>Enter</kbd> to jump directly into the document viewer.

### 📄 Built-in PDF & Slides Viewer
- Desktop modal reader with integrated zoom, rotation, fullscreen, direct download, and open-in-new-tab actions.
- Automatically falls back to native browser PDF viewer on mobile screens (< 768px) for optimal touch zooming.
- Lazy-loads documents only upon user click to keep initial page load lightweight.

### 📥 Dual Download Option
- For all presentations (`.pptx`) and Word documents (`.docx`), provides both:
  1. **View / Download PDF**: High-fidelity reading format.
  2. **Download Original**: Direct access to editable slides or documents.

### ⏱️ Study Progress Tracking
- Checkbox on every file and unit to mark as completed.
- Progress persists in `localStorage` across sessions.
- Dynamic visual completion percentages per subject.
- Includes a one-click progress reset modal for fresh exam prep cycles.

### 📌 Pinned Subjects
- Pin high-priority subjects to the top of your dashboard for quick resumption.

### 🌓 Modern "Hope Rise" Warm Editorial Design System
- **Curated Warm Palette**:
  - Light (Primary):
    - `--bg`: `#F6E9CF` warm cream fading softly into `--bg-soft`: `#FBF8F1` near-white down the hero.
    - `--surface`: `#FFFFFF` pure white rounded cards and sheets.
    - `--border`: `#E7DEC9` thin crisp warm-gray divider.
    - `--ink`: `#1A1A17` near-black headlines and body (14.2:1 AAA).
    - `--ink-muted`: `#6B665A` warm muted descriptions (5.3:1 AA).
    - `--label`: `#3A372F` tiny uppercase navigation labels (8.5:1 AAA).
  - Single Action Color:
    - `--green`: `#2EC36B` vivid green for primary actions, toggles, checkmarks, and progress fill.
    - `--green-ink`: `#0F2A18` high-contrast ink text on green fills (7.8:1 AAA).
    - `--green-tint`: `#DDF3E5` / `--green-tint-ink`: `#17673A` for pill tags.
  - Dark Mode:
    - `--bg`: `#16140F` warm near-black background (flat, no gradient).
    - `--surface`: `#1F1C15`, `--border`: `#343025`, `--ink`: `#F6E9CF` (14.2:1 AAA).
- **Typography**:
  - Display: **Bricolage Grotesque** (Weight 800, tight tracking `-0.03em`, line-height `0.95`) for hero headline and section titles.
  - Body & UI: **Inter** (400, 500, 600, 700) for editorial readability.
  - Code & Units: **JetBrains Mono** for course codes and metadata.
- **Consistent Shape Language**:
  - **Pills (`999px`)**: Buttons, tags, chips, search bar, and segmented tab tracks.
  - **Circles (`44px` / `36px`)**: Outlined icon buttons with diagonal arrows (`↗`).
  - **Cards & Sheets**: `28px` radius on desktop, `24px` on mobile, white surface, thin border, no heavy elevation.
- **Mobile-First Experience**:
  - Full-screen cream navigation drawer sheet with Esc key dismissal and body lock.
  - PWA manifest (`manifest.webmanifest`) and iOS/Android app icons.
  - 100% WCAG AA compliant across all text and UI elements.

### 🖨️ Printable Syllabus View
- Dedicated print stylesheet (`@media print`) that renders clean black-and-white syllabus sheets without navigation clutter, sidebars, or dark backgrounds.

### 📑 Scheme & Evaluation Guide (`#scheme`)
- Dedicated view with the complete V Semester Teaching Scheme (Sl 1–10, 22 credits total) and credit breakdown (L: 18, T: 1, P: 3, S: 18).
- Comprehensive evaluation breakdown: Continuous Internal Evaluation (CIE) and Semester-End Examination (SEE) rules for IPCC (Integrated), PCC/PEC/HSMC, AEC, PCC Lab, and NCMC courses.

### 🧪 Integrated & Autonomous Laboratories
- **Machine Learning Lab -1 (`ISL56`)**: Dr. Shruti G (Prereq: Python). Part A Tableau dashboards and Part B Python ML algorithms on benchmark UCI datasets.
- **Computer Networks Laboratory (`ISL57`)**: Charunayana V. Part A socket programming & routing algorithms in C/Java and Part B NS-2 simulations.
- **Software Engineering Integrated Lab (`IS52`)**: Mushtaq Ahmed D M. Practical exercises covering Agile Kanban, SRS specification, UML modeling, and test-driven development.

### 📝 Practice Exam Papers & Question Banks
- Direct access to verified **CIE-1, CIE-2, SEE, and Make-Up examination papers** across all courses with quick-view document integration.

---

## 📊 Subject Coverage & Inventory (CIE-1 Examination Schedule: 13–16 Oct 2026)

| Exam Date & Time | Course Code | Subject Name | Type | Coordinator | CIE-1 Scope Portion | Registered Files & Size | Notes, PYQ & Handwritten Status |
|---|---|---|---|---|---|---|---|
| **Tue 13-10-2026, 09:30–10:30** | `24IS53` | **Computer Networks** | PCC | Suresh Kumar K R | Units 1, 2, Unit 3 up to "IPv4 Addressing – Classless" | **18 files** · 27.9 MB | **CIE-1 Ready:** Units 1–3 Notes, 20 Solved PYQs, 4 Vector Handwritten Notebooks, Recent Notes (Complete Unit 1 & 2 decks, Unit 3 IPv4) |
| **Tue 13-10-2026, 13:30–14:30** | `24ISAEC594` | **Frontend Dev using React JS** | AEC | J R Shruti | Units 1 & 2 (Full) | **10 files** · 6.7 MB | **CIE-1 Ready:** Units 1–2 Notes, 21 Solved PYQs, 3 Vector Handwritten Notebooks, Recent Notes (Complete Unit 1 & 2 decks) |
| **Wed 14-10-2026, 09:30–10:30** | `24ISE552` | **Artificial Intelligence** | PEC | Dr. Jagadeesh Sai D | Units 1 & 2 (Full) | **24 files** · 10.8 MB | **CIE-1 Ready:** Units 1–2 Notes, Faculty 9-Q List (Photo scan & answers), 22 Solved PYQs, 3 Vector Handwritten Notebooks, Recent Notes (Intro, Problem-Solving, Uninformed, Informed, Local & Adversarial decks) |
| **Wed 14-10-2026, 13:30–14:30** | `24IS52` | **Software Engineering** | IPCC | Mushtaq Ahmed D M | Units 1 & 2 (Full) | **19 files** · 7.3 MB | **CIE-1 Ready:** Units 1–2 Notes, 20 Solved PYQs, 3 Vector Handwritten Notebooks, Recent Notes (Unit 1.1–1.3, Unit 2.1–2.2), Agile Lab Manual |
| **Thu 15-10-2026, 09:30–10:30** | `24IS51` | **Machine Learning** | PCC | Dr. Sumana M | Units 1, 2, Unit 3 (Regression only) | **33 files** · 19.5 MB | **CIE-1 Ready:** Units 1–3 Notes, 20 Solved PYQs, 4 Vector Handwritten Notebooks, Recent Notes (Ch 2–5 regression decks), Lab Notebooks |
| **Thu 15-10-2026, 15:00–16:00** | `24AL58` | **Research Methodology & IPR** | HSMC | Dr. Anitha P | Units 1, 2, Unit 3 up to Sample Design Characteristics | **32 files** · 13.8 MB | **CIE-1 Ready:** Units 1–3 Notes, 23 Solved PYQs, 4 Vector Handwritten Notebooks, Recent Notes (Units 1–3 PPTXs) |
| **Fri 16-10-2026, 09:30–10:30** | `24HS510` | **Environmental Studies** | NCMC | Civil / H&S Faculty | Units 1 & 2 (Full) | **18 files** · 11.6 MB | **CIE-1 Ready:** Units 1–2 Notes, 25 Solved PYQs, 3 Vector Handwritten Notebooks, Recent Notes (Unit 1 & 2 PPTXs, Unit 2 Topic PDFs) |
| **Fri 16-10-2026, 13:30–14:30** | `24IS54` | **Theory of Computation** | PCC | Dr. Rajeshwari S B | Units 1 & 2 (Full) | **11 files** · 48.3 MB | **CIE-1 Ready:** Units 1–2 Notes, 20 Solved PYQs, 3 Vector Handwritten Notebooks, Recent Notes (Complete Course Notebook, 45.5 MB) |

**Total Registry**: **165 registered files** across 8 subjects (**145.8 MB** total), **421 indexed search items**.

---

## 🏛️ Project Architecture

```text
SEM5_NOTES/
├── index.html              # Main application shell (SPA architecture)
├── README.md               # Comprehensive documentation & verified syllabus matrix
├── .gitignore              # Ignores OS, IDE, audit directories, archive/, and textbooks
├── assets/
│   └── katex/              # Self-hosted KaTeX (CSS, JS, and web fonts for offline math rendering)
├── css/
│   ├── style.css           # Design tokens, themes, scheme view, lab programs & print styles
│   └── notes.css           # Interactive study notes stylesheet (Hope Rise theme tokens, sidebar TOC)
├── js/
│   ├── app.js              # Application controller, hash router, global search, and progress storage (v4)
│   └── notes.js            # Interactive notes engine (TOC scrollspy, collapsibles, copy buttons)
├── data/
│   ├── subjects.js         # Single source of truth (158 files, V Sem Scheme, subjects, labs, timetables)
│   ├── notes-index.json    # Compact global search index for all 414 searchable entries
│   └── notes-index.js      # Offline fallback search index wrapper for file:// protocols
├── scripts/
│   ├── sync_subjects_from_folders.py  # Synchronizes data/subjects.js strictly with HTML + Handwritten + Recent Notes
│   ├── build_notes_index.py           # Generates data/notes-index.json and notes-index.js
│   ├── verify_no_mojibake.py          # Enforces 0 mojibake and strict subject title matching
│   ├── verify_cie1_gates.py           # Validates all 8 quality gates (Scope, Coverage, PYQ, Links, etc.)
│   └── verify_viewer_and_subject_pages.js # Playwright strict unit notes & viewer validation suite
├── archive/
│   └── removed-from-site/  # Quarantined older faculty slides & duplicate PDFs (gitignored, off-site)
└── notes/                  # URL-safe, lowercase, kebab-case document and study notes repository
    ├── <subject>/          # e.g., ml, se, cn, toc, ai, rmipr, reactjs, evs
    │   ├── recent-notes/   # Latest uploaded lecture slides, presentations, and notebooks
    │   ├── unit1/ unit2/   # Interactive HTML notes and handwritten notebook PDFs
    │   ├── unit3/          # (where within CIE-1 scope: ML, CN, RMIPR)
    │   ├── practice/       # Question banks, CIE papers, assignments, quizzes, and SEE papers
    │   ├── pyq/            # CIE-1 Solved PYQs (Interactive HTML & Handwritten PDF)
    │   └── lab/ / syllabus/# Lab programs (.ipynb & HTML preview) and official syllabus documents
```

---

## 🗃️ Single Source of Truth (`data/subjects.js`)

All subject cards, units, file paths, syllabus text, and examination schedules are governed by `window.SEM5_DATA` in [`data/subjects.js`](./data/subjects.js).

You can modify or expand the entire site by simply editing this file.

```javascript
window.SEM5_DATA = {
  meta: {
    siteTitle: "SEM 5 · ISE Notes",
    tagline: "Department of Information Science & Engineering",
    semester: "Semester V",
    totalCredits: 22,
    lastUpdated: "October 2026"
  },
  scheme: { ... },
  subjects: [
    {
      id: "ai",
      code: "ISE552",
      name: "Artificial Intelligence",
      shortName: "AI",
      credits: "3:0:0",
      contactHours: "42 Hours",
      coordinator: "Dr. Jagadeesh Sai D",
      status: "full_notes", // "full_notes" | "syllabus_only"
      accent: { primary: "#8B5CF6", secondary: "#A78BFA", glow: "rgba(139, 92, 246, 0.28)" },
      units: [ ... ],
      syllabus: { ... }
    },
    ...
  ]
};
```

---

## ✍️ How to Add or Edit Content

### 1. Adding a New Unit Note

1. Place your PDF or presentation into `notes/<subject>/<unit>/` with a clean, lowercase name (e.g. `notes/cn/unit3/is53-cn-unit3.pdf`).
2. Open [`data/subjects.js`](./data/subjects.js) and locate the subject's matching unit.
3. Append a new object to the `files` array:

```javascript
{
  id: "cn-u3-pdf",
  title: "Unit 3: Transport Layer Protocols",
  originalName: "IS53-CN-Unit3.pdf",
  path: "notes/cn/unit3/is53-cn-unit3.pdf",
  originalPath: null,
  type: "pdf",
  size: "14.2 MB",
  isConverted: false
}
```

### 2. Adding Practice Papers or Question Banks

Add a unit with `isPractice: true`:

```javascript
{
  id: "ml-practice",
  unitNumber: "Practice",
  title: "Practice & Examination Question Banks",
  isPractice: true,
  files: [
    {
      id: "ml-u1-qb",
      title: "ML Unit 1: Comprehensive Question Bank (QB)",
      originalName: "Unit 1(QB).pdf",
      path: "notes/ml/practice/unit-1-qb.pdf",
      type: "pdf",
      size: "4.04 MB",
      isConverted: false
    }
  ]
}
```

### 3. Adding or Editing Interactive HTML Notes

1. Create `notes/<subject>/unit<N>/unit-<N>-notes.html` following the standard Hope Rise unit template:
   - Header with breadcrumbs, title, badge tags, reading time, and link back to subject page (`../../../index.html#subject/<id>`).
   - Sticky sidebar Table of Contents (`<nav id="toc" class="toc-sidebar">`).
   - Content sections matching the official syllabus line-for-line (`<section id="sec-..." class="note-section">`).
   - Pure inline SVG diagrams (scalable, accessible `<title>`/`<desc>`, matching theme variables).
   - KaTeX formulas and step-by-step solved numericals.
   - End-of-unit Quick Revision Sheet, collapsible Important Questions (2M/5M/10M), Past Exam Questions, and Practice Problems.
2. Link the shared CSS and JS:
   - `<link rel="stylesheet" href="../../../assets/katex/katex.min.css" />`
   - `<link rel="stylesheet" href="../../../css/notes.css" />`
   - `<script src="../../../assets/katex/katex.min.js"></script>`
   - `<script src="../../../assets/katex/contrib/auto-render.min.js"></script>`
   - `<script src="../../../js/notes.js"></script>`
3. Register the file in [`data/subjects.js`](./data/subjects.js) as the first file entry in the unit:
   ```javascript
   {
     id: "<subject>-u<N>-notes",
     title: "Unit <N>: Interactive Notes",
     originalName: "unit-<N>-notes.html",
     path: "notes/<subject>/unit<N>/unit-<N>-notes.html",
     originalPath: null,
     type: "notes",
     tag: "Interactive notes",
     readingTime: "40 min read",
     size: "Interactive Notes",
     isConverted: false
   }
   ```
4. Rebuild the search index:
   ```bash
   python audit/generate_notes_index.py
   python -c "with open('data/notes-index.json','r',encoding='utf-8') as f: r=f.read(); open('data/notes-index.js','w',encoding='utf-8').write('window.SEM5_NOTES_INDEX = ' + r + ';\n')"
   ```

---

## 📐 Interactive Notes Template & Tooling

All 24 interactive HTML study notes (`notes/<subject>/unit<N>/unit-<N>-notes.html`) share an identical, robust, self-sufficient "Hope Rise" presentation layer designed for maximum legibility, zero layout shift, and instant loading.

### Canonical Template Structure

- **Self-Sufficient Design System (`css/notes.css`)**:
  - Independent CSS reset and Hope Rise tokens (`--bg`, `--surface`, `--border`, `--ink`, `--green`).
  - Strict AA contrast across both light (cream `#F6E9CF`) and dark (warm near-black `#16140F`) themes.
  - Sticky two-column layout on desktop (centered `1200px` container, `260px` sticky independent TOC sidebar, max `760px` reading column).
  - Responsive collapse: below `1024px`, the desktop sidebar transitions to a mobile floating/sticky "On this page" pill button with an accessible modal drawer sheet (Esc dismissal, focus trap, no wide-screen leaks).
  - Defensive scroll safety: all tables, pre blocks, and KaTeX math formulas are contained in horizontally scrollable surfaces without viewport blowouts at viewports down to 320px.
- **Shared Interactive Engine (`js/notes.js`)**:
  - Zero-dependency client script handling theme sync before paint, reading progress bar, scrollspy table-of-contents tracking, study progress persistence (`sem5_progress_v1`), code copy buttons, KaTeX auto-rendering, and print view expansion.

### Re-Applying Template Shell (`scripts/apply_notes_template.py`)

To ensure absolute consistency across all current and future note pages, the wrapper shell (HTML head, top bar, TOC sidebar, breadcrumbs, and footer) can be regenerated while preserving the article body content byte-for-byte:

```bash
python scripts/apply_notes_template.py
```

This script:
1. Parses each note page and extracts all `<section>` elements verbatim.
2. Validates section counts and SHA-256 hashes against recorded baselines.
3. Wraps the exact, untampered content inside the canonical Hope Rise template with verified relative paths.

### Automated Style & Content Regression Testing (`scripts/check_notes_style.js`)

An automated Playwright test suite verifies visual and functional fidelity across all 24 pages:

```bash
# 1. Start the local server under /SEM5_NOTES/ subpath:
python audit/serve_subpath.py

# 2. Run the automated Playwright regression suite:
node scripts/check_notes_style.js
```

The test runner asserts for every page:
- **Asset Integrity**: 100% of linked CSS, JS, fonts, and KaTeX assets return HTTP 200 with zero browser console errors.
- **Computed Styles**: Body font (Inter), centered `1200px` container, un-underlined TOC links, H1 line-height $\le 1.2$, and styled callout boxes.
- **Responsive Layout**: Zero horizontal overflow at `1280px`, `768px`, `390px`, and `320px` viewports.
- **TOC Modes**: Sticky sidebar visible at `1280px` (mobile button hidden); drawer button visible and closed by default at `390px`.
- **Theme Accessibility**: WCAG AA color contrast verified in both light and dark modes.
- **Content Immutability**: Real-time SHA-256 hash comparison proving note content is 100% unaltered.
- **Contact Sheet**: Captures light and dark screenshots at `1280px` and `390px` for all 24 pages, compiling `audit/screens/index.html` for instant visual inspection.

---

## ✍️ Handwritten-Style Study Notebooks (A4 Vector PDF)

For all 24 units across all 8 subjects, complete **handwritten-style notebook PDFs** are provided alongside the interactive HTML notes.

> **Honest Transparency**: Labeled as *"Handwritten-style notes (generated from the unit notes)"*. These are not condensed revision summaries; each notebook contains **100% of the syllabus content**, converted page-by-page into an authentic lined notebook aesthetic.

### Aesthetic & Technical Features

- **Genuine Notebook Aesthetics**: Rendered with subtle ruled paper lines (28px spacing), dual red left margin lines, 3 standard binder punch holes, and handwritten callouts with rough-edged borders.
- **Crisp Vector Ink**: KaTeX mathematical formulas and Greek symbols rendered directly into vector curves in royal blue ink (`#1A365D`), preserving absolute sharpness at any zoom level.
- **Styled Diagrams**: SVG architectural diagrams and state machines rendered with handwritten labels and rough sketching aesthetics.
- **Searchable & Selectable**: Full selectable text layer and PDF outline bookmarks (matching all unit sections and subsections) generated via `pypdf`.
- **Lightweight PDFs**: High optimization ensures all 24 notebooks are between **0.76 MB and 2.00 MB** (well under the 12 MB mobile threshold).
- **WebP Previews**: A 400px WebP thumbnail preview generated for instant card loading.

### Rebuild Commands & Engine

The build toolchain uses Headless Chromium (Playwright) to layout pages into exact A4 notebook pages, followed by Python post-processing for bookmarks and metadata:

```bash
# Build a single unit notebook:
node scripts/build_handwritten.js --subject cn --unit 1

# Rebuild all 24 units across all 8 subjects:
node scripts/build_handwritten.js --all

# Run the strict coverage & font allow-list verification gate (asserts 100% heading and font compliance):
python scripts/check_handwritten_coverage.py --all

# Rebuild the global search index (284 sections across all 8 subjects):
python scripts/build_notes_index.py

# Post-process bookmarks, metadata, and outlines on a PDF:
python scripts/postprocess_pdf.py --pdf notes/cn/unit1/handwritten/cn-unit1-handwritten.pdf --toc notes/cn/unit1/handwritten/toc.json
```

### Font Credits & Open Font Licenses (OFL)

All handwritten fonts bundled locally under `fonts/` are distributed under the [SIL Open Font License (OFL 1.1)](https://openfontlicense.org/). The build enforces zero external CDN font dependencies and a strict local font allow-list:

| Font Family | Designer / Foundry | License | Purpose in Notebook |
| :--- | :--- | :--- | :--- |
| **Patrick Hand** | Patrick Wagesreiter | SIL OFL 1.1 | Body text, bullet points & descriptions |
| **Caveat** | Pablo Impallari | SIL OFL 1.1 | Unit cover title & primary unit headings |
| **Kalam** | Indian Type Foundry | SIL OFL 1.1 | Section subheadings (H2/H3), callout badges |
| **JetBrains Mono** | JetBrains | SIL OFL 1.1 | Code snippets, terminal blocks, algorithm matrices |

---

## 💻 Local Development

Clone the repository and run any simple static server:

```bash
# Clone the repository
git clone https://github.com/AnanthAkshay/SEM5_NOTES.git
cd SEM5_NOTES

# Preview with Python:
python -m http.server 3000

# Or preview with Node.js:
npx serve .
```

Open `http://localhost:3000` in your web browser.

---

## 🚀 GitHub Pages Deployment

The repository is pre-configured with relative paths and `.nojekyll` for GitHub Pages hosting:

1. **Push your code to GitHub**:
   ```bash
   git branch -M main
   git push -u origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub (`https://github.com/AnanthAkshay/SEM5_NOTES`).
   - Click **Settings** ➔ **Pages** (under *Code and automation*).
   - Under **Build and deployment**:
     - **Source**: `Deploy from a branch`
     - **Branch**: `main`
     - **Folder**: `/ (root)`
   - Click **Save**.

3. **Verify Live Deployment**:
   Run the automated live site verification test suite against the deployed site:
   ```bash
   node scripts/check_live.js https://ananthakshay.github.io/SEM5_NOTES/
   ```

---

## 📱 Browser Compatibility & Accessibility

- **Responsive Viewports**: Tested across 360px mobile viewports, iPad tablets, laptops, and ultra-wide displays.
- **Accessibility**: Semantic HTML5 tags (`<main>`, `<header>`, `<footer>`, `<section>`), visible focus indicators (`:focus-visible`), and ARIA landmarks.
- **System Themes**: Automatically honors `prefers-color-scheme` and `prefers-reduced-motion`.

---

## ⚖️ License & Attributions

- **Study Notes & Notebooks**: Copyright &copy; 2024–2026 Akshay A. All rights reserved. Prepared for personal, non-commercial educational study only.
- **Curriculum & Exam Papers**: Original syllabus outlines, lecture presentations, and examination question papers are the intellectual property of the respective course faculty and Ramaiah Institute of Technology (MSRIT) / VTU.
- **Third-Party Libraries & Fonts**: Distributed under open-source licenses (KaTeX: MIT, Rough.js: MIT, Handwritten Fonts: SIL OFL 1.1). See [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md) for full license details.
