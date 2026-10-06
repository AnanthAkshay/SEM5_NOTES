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
  - [3. Adding Exam Timetable PDFs](#3-adding-exam-timetable-pdfs)
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
- **Data-Driven Decoupling**: All subjects, units, notes, links, and timetables reside in [`data/subjects.js`](./data/subjects.js). Modify content without touching any HTML.

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
- Dynamic visual completion percentages per subject and across the entire semester dashboard.
- Includes a one-click progress reset modal for fresh exam prep cycles.

### 📌 Pinned Subjects & Recently Opened
- Pin high-priority subjects to the top of your dashboard.
- Recently opened document row displays the last 4 accessed notes for quick resumption.

### 🌓 Dark & Light Modes
- Bespoke obsidian theme (`#0a0d14`) with glassmorphism and subtle accent glows.
- Clean high-contrast paper light mode for daylight reading.
- Synchronizes with system preference and saves custom user selection in `localStorage`.

### 🖨️ Printable Syllabus View
- Dedicated print stylesheet (`@media print`) that renders clean black-and-white syllabus sheets without navigation clutter, sidebars, or dark backgrounds.

### 📅 Exam Timetable Hub
- Config-driven schedule cards for Semester-End Theory Examinations (SEE), Practical Lab exams, and Continuous Internal Evaluations (CIE).

---

## 📊 Subject Coverage & Inventory

| Subject Name | Code | Credits | Type | Coverage Status | Materials Included |
|---|---|---|---|---|---|
| **Artificial Intelligence** | `ISE552` | `3:0:0` | Core Elective | **Syllabus & Info** | 5 Units transcribed with topics, NPTEL video links, Russell & Norvig 4th ed textbook, reference books, CO1–CO5 mapping, and CIE/SEE marking scheme. *(Notes coming soon)* |
| **Computer Networks** | `IS53` | *Pending* | Core ISE | **Full Notes** | Unit 1 (15.7 MB) and Unit 2 (13.1 MB) comprehensive lecture notes. |
| **Environmental Studies** | `HS 510` | *Pending* | Mandatory | **Full Notes + Practice** | Units 1–5 PPT presentations (+ PDFs), Unit 2 topic resource PDFs (Forest, Water, Mineral, Food, Land), plus 2024–2025 CIE-1 Question Paper. |
| **Machine Learning** | `ISE554` | *Pending* | Core ISE | **Full Notes + Practice** | Unit 1 notes, Unit 2 notes, Unit 3 (Polynomial Regression & Steps for ML Algorithms), and Unit 1 Question Bank (QB). |
| **Front end Dev using ReactJS** | `ISAEC594` | `1:0:0:1` | AEC Elective | **Syllabus & Info** | Units I–III transcribed syllabus, pedagogy delivery tools, and official React documentation links. *(Notes coming soon)* |
| **Research Methodology & IPR** | `ISE555` | *Pending* | Core ISE | **Full Notes** | Unit 1 PPT (+ PDF) and Unit 2 PPT (+ PDF) complete presentations. |
| **Software Engineering** | `IS52` | *Pending* | Core ISE | **Full Notes** | Unit 1.1, Unit 1.2, Unit 1.3, and Unit 2 presentations (+ PDFs). |
| **Theory of Computation** | `IS51` | *Pending* | Core ISE | **Full Notes** | Units 1–5 comprehensive notes + Alternate/condensed versions for Units 1 & 3. |

---

## 🏛️ Project Architecture

```text
SEM5_NOTES/
├── index.html              # Main application shell (SPA architecture)
├── README.md               # Comprehensive documentation & setup guide
├── .gitignore              # Ignores OS, IDE, and raw root duplicates
├── css/
│   └── style.css           # Design system tokens, dark/light themes, animations & print styles
├── js/
│   └── app.js              # Application controller, router, search, and storage
├── data/
│   └── subjects.js         # Single source of truth for all content & timetables
└── notes/                  # Organized, URL-safe document repository
    ├── ai/
    │   └── syllabus/       # Converted PDF, original DOCX, syllabus screenshots
    ├── cn/
    │   ├── unit1/          # IS53 CN Unit 1 notes
    │   └── unit2/          # IS53 CN Unit 2 notes
    ├── evs/
    │   ├── unit1/ to unit5/# Converted PDFs and original PPTX files
    │   └── practice/       # Converted CIE-1 Question Paper
    ├── ml/
    │   ├── unit1/ to unit3/# Machine Learning units 1-3
    │   └── practice/       # Machine Learning Question Bank (QB)
    ├── reactjs/
    │   └── syllabus/       # Syllabus screenshot & transcribed content
    ├── rmipr/
    │   ├── unit1/          # RM & IPR Unit 1 PPT & PDF
    │   └── unit2/          # RM & IPR Unit 2 PPT & PDF
    ├── se/
    │   ├── unit1/          # SE Units 1.1, 1.2, 1.3 PPTs & PDFs
    │   └── unit2/          # SE Unit 2 Architectural Design PPT & PDF
    └── toc/
        ├── unit1/ to unit5/# Theory of Computation comprehensive units 1-5
        ├── unit1/          # TOC Unit 1 & 2 Alternate / Condensed notes
        └── unit3/          # TOC Unit 3 Alternate / Condensed notes
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
    lastUpdated: "October 2026"
  },
  timetable: { ... },
  subjects: [
    {
      id: "ai",
      code: "ISE552",
      name: "Artificial Intelligence",
      shortName: "AI",
      credits: "3:0:0",
      contactHours: "42 Hours",
      coordinator: "Dr Jagadeesh Sai D",
      status: "syllabus_only", // "full_notes" | "syllabus_only"
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

### 3. Adding Exam Timetable PDFs

In [`data/subjects.js`](./data/subjects.js), locate the `timetable.items` array. Place your timetable PDF in `notes/timetables/` and update `pdfUrl`:

```javascript
{
  id: "theory-see",
  title: "Semester-End Theory Examination (SEE)",
  category: "Theory",
  status: "Schedule Published",
  statusBadge: "Completed",
  pdfUrl: "notes/timetables/see_theory_dec2026.pdf",
  dateRange: "Dec 15, 2026 – Jan 05, 2027",
  description: "Official SEE schedule published by the Controller of Examinations."
}
```

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
