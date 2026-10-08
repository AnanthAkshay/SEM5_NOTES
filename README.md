# 🎓 SEM 5 · ISE Notes Portal

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Deploy-success?style=for-the-badge&logo=github)](https://ananthakshay.github.io/SEM5_NOTES/)
[![Semester](https://img.shields.io/badge/Semester-V%20(5th%20Sem)-indigo?style=for-the-badge)](https://ananthakshay.github.io/SEM5_NOTES/)
[![Department](https://img.shields.io/badge/Department-ISE-blue?style=for-the-badge)](https://ananthakshay.github.io/SEM5_NOTES/)
[![Tech Stack](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20Vanilla%20JS-amber?style=for-the-badge)](https://ananthakshay.github.io/SEM5_NOTES/)
[![License](https://img.shields.io/badge/License-MIT%20%2F%20Academic-emerald?style=for-the-badge)](LICENSE)

> **Department of Information Science & Engineering (ISE) · Semester V**  
> A bespoke, lightweight, and data-driven study portal crafted for 5th Semester ISE engineering students. Built with pure HTML5, modern CSS3 variables, and vanilla JavaScript—zero external build steps, 100% relative paths, and instant deployment on GitHub Pages.

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

## 📊 Subject Coverage & Inventory (Official V Semester Scheme: 22 Credits)

| Subject Name | Code | Credits (L:T:P) | Type | Coordinator | Coverage Status | Materials Included |
|---|---|---|---|---|---|---|
| **Machine Learning** | `IS51` | `3:0:0` | PCC | Dr. Sumana M | **Interactive Notes + Full PDFs + Lab + Practice** | Units 1–3 Interactive HTML Notes, Units 1–3 faculty PDFs, Unit 1 QB, ISL56 Lab Programs (Tableau + Python), and CIE-1, CIE-2 & SEE 2026 combined paper. |
| **Software Engineering** | `IS52` | `2:0:1` | IPCC | Mushtaq Ahmed D M | **Interactive Notes + Full PDFs + Lab + Practice** | Units 1–3 Interactive HTML Notes, Units 1.1–1.3 & Unit 2 PPTs/PDFs, Unit-wise practical exercises, and CIE-1 & CIE-2 combined paper. |
| **Computer Networks** | `IS53` | `4:0:0` | PCC | Suresh Kumar K R | **Interactive Notes + Full PDFs + Lab + Practice** | Units 1–3 Interactive HTML Notes, Unit 1 & Unit 2 lecture presentations, ISL57 Lab Part A & B programs, and CIE-1 & CIE-2 combined paper. |
| **Theory of Computation** | `IS54` | `2:1:0` | PCC | Dr. Rajeshwari S B | **Interactive Notes + Full PDFs + Practice** | Units 1–3 Interactive HTML Notes, Units 1–5 comprehensive notes + alternate condensed notes, and CIE-1, CIE-2 & SEE 2025 combined paper. |
| **Artificial Intelligence** | `ISE552` | `3:0:0` | PEC | Dr. Jagadeesh Sai D | **Interactive Notes + Syllabus + Practice** | Units 1–3 Interactive HTML Notes, complete 5 units transcribed from syllabus, verified NPTEL links, textbook & references, and CIE-1 & CIE-2 combined paper. |
| **Research Methodology & IPR** | `AL58` | `3:0:0` | HSMC | Dr. Anitha P | **Interactive Notes + Full PDFs + Practice** | Units 1–3 Interactive HTML Notes, Unit 1 & Unit 2 PPTs/PDFs, CIE-1 & CIE-2 paper, Make-Up Exam (Apr 2025), and SEE Backlog Exam (Feb/Mar 2025). |
| **Front end Dev using ReactJS** | `ISAEC594` | `1:0:0` | AEC | J R Shruti | **Interactive Notes + Syllabus & Info** | Units 1–3 Interactive HTML Notes with runnable code examples, Units I–V transcribed syllabus, pedagogy tools, textbooks, and documentation links. |
| **Environmental Studies** | `HS510` | `0:0:0` (NCMC) | NCMC | Civil / H&S Faculty | **Interactive Notes + Full PDFs + Practice** | Units 1–3 Interactive HTML Notes, Units 1–5 PPTs/PDFs, Unit 2 natural resource references, 2024 CIE-1 QP, and CIE-1 50-mark paper. |

---

## 🏛️ Project Architecture

```text
SEM5_NOTES/
├── index.html              # Main application shell (SPA architecture)
├── README.md               # Comprehensive documentation & verified syllabus matrix
├── .gitignore              # Ignores OS, IDE, audit directories, and raw temp files
├── assets/
│   └── katex/              # Self-hosted KaTeX (CSS, JS, and web fonts for offline math rendering)
├── css/
│   ├── style.css           # Design tokens, themes, scheme view, lab programs & print styles
│   └── notes.css           # Interactive study notes stylesheet (Hope Rise theme tokens, sidebar TOC, math & code boxes)
├── js/
│   ├── app.js              # Application controller, hash router, global search, and progress storage
│   └── notes.js            # Interactive notes engine (TOC scrollspy, collapsibles, copy buttons, progress sync)
├── data/
│   ├── subjects.js         # Single source of truth (V Sem Scheme, subjects, labs, timetables, note paths)
│   ├── notes-index.json    # Compact global search index for all 230 interactive note sections
│   └── notes-index.js      # Offline fallback search index wrapper for file:// protocols
└── notes/                  # Organized, URL-safe document and interactive notes repository
    ├── ai/
    │   ├── unit1/ to unit3/# Interactive HTML study notes (unit-1-notes.html to unit-3-notes.html)
    │   ├── syllabus/       # Converted PDF, original DOCX, syllabus screenshots
    │   └── practice/       # AI CIE-1 & CIE-2 Question Papers
    ├── cn/
    │   ├── unit1/ to unit3/# Interactive HTML notes & IS53 Computer Networks lecture presentations
    │   └── practice/       # CN CIE-1 & CIE-2 Question Papers
    ├── evs/
    │   ├── unit1/ to unit3/# Interactive HTML notes, converted PDFs, and original PPTX files
    │   └── practice/       # EVS CIE-1 (2024) QP & CIE-1 (50 Marks) Paper
    ├── ml/
    │   ├── unit1/ to unit3/# Interactive HTML notes & Machine Learning lecture notes
    │   └── practice/       # Unit 1 QB & ML CIE-1, CIE-2 and SEE Combined Paper
    ├── reactjs/
    │   ├── unit1/ to unit3/# Interactive HTML notes with tested code examples
    │   └── syllabus/       # Syllabus screenshot & transcribed content
    ├── rmipr/
    │   ├── unit1/ to unit3/# Interactive HTML notes & RM and IPR presentations
    │   └── practice/       # CIE-1 & CIE-2, Make-Up Exam (2025), SEE Exam (2025)
    ├── se/
    │   ├── unit1/ to unit3/# Interactive HTML notes & SE lecture presentations
    │   └── practice/       # SE CIE-1 & CIE-2 Question Papers
    └── toc/
        ├── unit1/ to unit3/# Interactive HTML notes with inline SVG automata & traces
        ├── unit1/ to unit5/# Theory of Computation comprehensive lecture notes
        └── practice/       # TOC CIE-1, CIE-2 and SEE Combined Paper
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

The repository is pre-configured with relative paths for GitHub Pages hosting:

1. **Push your code to GitHub**:
   ```bash
   git remote add origin https://github.com/AnanthAkshay/SEM5_NOTES.git
   git branch -M main
   git push -u origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub.
   - Click **Settings** ➔ **Pages** (under *Code and automation*).
   - Under **Build and deployment**:
     - **Source**: `Deploy from a branch`
     - **Branch**: `main`
     - **Folder**: `/ (root)`
   - Click **Save**.

3. Your website will be live in ~60 seconds at:  
   `https://AnanthAkshay.github.io/SEM5_NOTES/`

---

## 📱 Browser Compatibility & Accessibility

- **Responsive Viewports**: Tested across 360px mobile viewports, iPad tablets, laptops, and ultra-wide displays.
- **Accessibility**: Semantic HTML5 tags (`<main>`, `<header>`, `<footer>`, `<section>`), visible focus indicators (`:focus-visible`), and ARIA landmarks.
- **System Themes**: Automatically honors `prefers-color-scheme` and `prefers-reduced-motion`.

---

## ⚖️ License

Created for the students of the **Department of Information Science & Engineering**, Semester V. Distributed for academic and personal reference under the MIT License.
