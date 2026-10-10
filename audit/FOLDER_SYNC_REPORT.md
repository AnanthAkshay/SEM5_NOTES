# SEM 5 · Notes Folder Synchronization Audit Report

**Date:** October 10, 2026  
**Branch:** `sync-notes-folders` (Tagged at `pre-sync-folders`)  
**Status:** Initial Filesystem Scan & Mismatch Analysis Complete  

---

## 1. Executive Summary

- **Total Files Scanned:** 379
- **Total Duplicate Hash Groups:** 40
- **Mismatches in `data/subjects.js` (Dead links):** 0
- **Unregistered Files in `notes/`:** 24
- **Raw Files in Subject Workspace Directories:** 211
- **Files with Confusing / Non-URL-Safe Filenames:** 89

### Inventory by Classification
| Classification | Count | Description |
|:---|:---:|:---|
| **Faculty notes** | 160 | Files categorized under Faculty notes |
| **Handwritten** | 73 | Files categorized under Handwritten |
| **PYQ/Question paper** | 68 | Files categorized under PYQ/Question paper |
| **Unit notes** | 27 | Files categorized under Unit notes |
| **Lab** | 21 | Files categorized under Lab |
| **Assignment/Quiz/Worksheet** | 11 | Files categorized under Assignment/Quiz/Worksheet |
| **Reference/other** | 10 | Files categorized under Reference/other |
| **Question bank** | 6 | Files categorized under Question bank |
| **Syllabus** | 3 | Files categorized under Syllabus |

---

## 2. Identified Textbooks & Copyrighted Works (To Quarantine)
> [!IMPORTANT]
> These files are published textbooks with third-party copyrights. Per academic portal policy, they are strictly quarantined to `sources/textbooks/`, gitignored, and NEVER published on the live site.

| Subject | File Name | Size | Rel Path | Action |
|:---|:---|:---:|:---|:---|
| RMIPR | `CR Kothari Research Methodology (1).pdf` | 1.91 MB | `AL58 - RM/Books/CR Kothari Research Methodology (1).pdf` | Move to `sources/textbooks/` (Quarantined) |
| RMIPR | `David V. Thiel - Research Methods for Engineers. 1-Cambridge Uni Press (2014).pdf` | 12.36 MB | `AL58 - RM/Books/David V. Thiel - Research Methods for Engineers. 1-Cambridge Uni Press (2014).pdf` | Move to `sources/textbooks/` (Quarantined) |
| SE | `Software Engineering - Ian Sommerville.pdf` | 3.93 MB | `IS52 - SE/Book/Software Engineering - Ian Sommerville.pdf` | Move to `sources/textbooks/` (Quarantined) |
| CN | `fifth-edition-data-communications-and-networking.pdf` | 65.35 MB | `IS53 - CN/BOOK/fifth-edition-data-communications-and-networking.pdf` | Move to `sources/textbooks/` (Quarantined) |
| ECO | `engineering economics 239p -- R_ Panneerselvam.pdf` | 683.5 KB | `ISAEC591 - Eco/Book/engineering economics 239p -- R_ Panneerselvam.pdf` | Move to `sources/textbooks/` (Quarantined) |

---

## 3. Duplicate Content Analysis (Exact SHA-256 Collisions)
The following files have identical byte contents (identical SHA-256) across multiple locations:

| Short Hash | Size | Files Sharing Identical Content |
|:---|:---:|:---|
| `690a4d7bea` | 43.47 MB | `IS54 - TOC/TOC_Notes.pdf`<br>`IS54 - TOC/Recent Notes/TOC_Notes.pdf` |
| `da0700a059` | 23.56 MB | `IS54 - TOC/Vercel Notes/Unit 3.pdf`<br>`notes/toc/unit3/unit-3.pdf` |
| `c572c68940` | 22.38 MB | `IS54 - TOC/Vercel Notes/Unit 1.pdf`<br>`notes/toc/unit1/unit-1.pdf` |
| `8533e1c151` | 12.41 MB | `HS510 - EVS/Recent Notes/Unit-4.pptx`<br>`notes/evs/unit4/unit-4.pptx` |
| `3c46e2a055` | 10.97 MB | `IS54 - TOC/Vercel Notes/Unit 2.pdf`<br>`notes/toc/unit2/unit-2.pdf` |
| `958ae55a9e` | 5.63 MB | `HS510 - EVS/Recent Notes/Unit-3.pptx`<br>`notes/evs/unit3/unit-3.pptx` |
| `4a59a2109c` | 5.57 MB | `IS54 - TOC/Vercel Notes/Toc unit 1 and 2.pdf`<br>`notes/toc/unit1/toc-unit-1-and-2-alternate.pdf` |
| `63599ce7fc` | 4.24 MB | `IS54 - TOC/Vercel Notes/Unit 5.pdf`<br>`notes/toc/unit5/unit-5.pdf` |
| `f216da470a` | 2.68 MB | `ISAEC594 - React/Recent Notes/UNIT-1 ReactJS.pptx`<br>`notes/reactjs/unit1/reactjs-unit1.pptx` |
| `29d1fd7e9e` | 2.65 MB | `IS54 - TOC/Vercel Notes/TOC_ unit3.pdf`<br>`notes/toc/unit3/toc-unit3-alternate.pdf` |
| `44e2610cb7` | 2.62 MB | `IS54 - TOC/Vercel Notes/Unit 4.pdf`<br>`notes/toc/unit4/unit-4.pdf` |
| `f88d924745` | 2.31 MB | `HS510 - EVS/Recent Notes/Unit-1.pptx`<br>`notes/evs/unit1/unit-1.pptx` |
| `52eaa85244` | 1.86 MB | `IS52 - SE/Recent Notes/Unit 2.1.pptx`<br>`notes/se/unit2/unit-2.pptx` |
| `7e15eaf5c4` | 1.72 MB | `HS510 - EVS/Recent Notes/Unit-2.pptx`<br>`notes/evs/unit2/unit-2.pptx` |
| `da9833ba85` | 1.62 MB | `ISE552 - AI/Recent Notes/AI-2.pdf`<br>`notes/ai/unit1/ai-intro-intelligent-agents.pdf` |
| `4b80b98893` | 1.37 MB | `HS510 - EVS/Recent Notes/Unit-5.pptx`<br>`notes/evs/unit5/unit-5.pptx` |
| `d0fe7437e0` | 878.2 KB | `IS54 - TOC/CIE - PYQ_s/CIE1&2-2025.pdf`<br>`notes/toc/practice/toc-cie-1-2-see.pdf` |
| `f78a94534e` | 595.6 KB | `IS52 - SE/Recent Notes/Unit 1.2.pptx`<br>`notes/se/unit1/unit-1-2.pptx` |
| `ffd1b90a09` | 524.1 KB | `ISE552 - AI/CIE - PYQ_s/CIE1&2-2025.pdf`<br>`notes/ai/practice/ai-cie-1-and-2.pdf` |
| `e2cc5e0352` | 486.9 KB | `HS510 - EVS/CIE - PYQ_s/CIE1&2-2025.pdf`<br>`notes/evs/practice/evs-cie-1.pdf` |
| `1dac17b342` | 450.9 KB | `IS52 - SE/Recent Notes/Unit 1.3.pptx`<br>`notes/se/unit1/unit-1-3.pptx` |
| `eb90bc4737` | 409.3 KB | `ISE552 - AI/Recent Notes/AI-Intelligent_Agents-PS.pdf`<br>`notes/ai/unit1/ai-problem-solving-agents-alt.pdf` |
| `9fab6beb07` | 408.7 KB | `ISE552 - AI/Recent Notes/AI-Intelligent_Agents.pdf`<br>`notes/ai/unit1/ai-problem-solving-agents.pdf` |
| `3bb0eb2f9c` | 331.2 KB | `HS510 - EVS/Recent Notes/1. Unit-2 Forest resources - Ecological importance of forests - Copy.pdf`<br>`notes/evs/unit2/unit-2-forest-resources.pdf` |
| `467dbf5555` | 314.9 KB | `IS52 - SE/CIE - PYQ_s/CIE1&2-2025.pdf`<br>`notes/se/practice/se-cie-1-and-2.pdf` |
| `0088245d5d` | 308.8 KB | `HS510 - EVS/Recent Notes/2. Unit-2 Water resources - Global water resources distribution.pdf`<br>`notes/evs/unit2/unit-2-water-resources.pdf` |
| `2b6d055d93` | 299.0 KB | `IS53 - CN/CIE - PYQ_s/CIE1&2-2025.pdf`<br>`notes/cn/practice/cn-cie-1-and-2.pdf` |
| `fd8c3fbb7b` | 292.8 KB | `HS510 - EVS/Recent Notes/5. Unit-2 Land resources - Soil erosion and Desertification.pdf`<br>`notes/evs/unit2/unit-2-land-resources.pdf` |
| `1e1b1dd7b2` | 266.7 KB | `HS510 - EVS/Recent Notes/4. Unit-2 Food resources - Effects of modern agriculture.pdf`<br>`notes/evs/unit2/unit-2-food-resources.pdf` |
| `88691cc0c5` | 263.0 KB | `HS510 - EVS/Recent Notes/3. Unit-2 Mineral resources - Environmental effects of extracting and processing of mineral resources.pdf`<br>`notes/evs/unit2/unit-2-mineral-resources.pdf` |
| `b6a971e1d2` | 246.1 KB | `AL58 - RM/CIE - PYQ_s/2025 CIE.pdf`<br>`notes/rmipr/practice/rmipr-cie-1-and-2.pdf` |
| `ec144ec408` | 173.7 KB | `ISE552 - AI/Recent Notes/AI-Informed_Search.pdf`<br>`notes/ai/unit2/ai-informed-search.pdf` |
| `b38e69e199` | 170.4 KB | `ISE552 - AI/Recent Notes/AI-AGENTS-Uninformed_Search.pdf`<br>`notes/ai/unit2/ai-uninformed-search.pdf` |
| `f9ad028ea4` | 170.3 KB | `ISE552 - AI/Recent Notes/AI-Local_Search.pdf`<br>`notes/ai/unit2/ai-local-search.pdf` |
| `16279ad03c` | 121.4 KB | `AL58 - RM/SEE - PYQ_s/MAKEUP2025.pdf`<br>`notes/rmipr/practice/rmipr-makeup-apr-2025.pdf` |
| `53e1390c46` | 117.4 KB | `AL58 - RM/SEE - PYQ_s/2025.pdf`<br>`notes/rmipr/practice/rmipr-see-feb-mar-2025.pdf` |
| `197f661a70` | 78.8 KB | `HS510 - EVS/CIE - PYQ_s/EVS_CIE1_QP-2024 (1).docx`<br>`notes/evs/practice/evs-cie1-qp-2024.docx` |
| `a5447a12cb` | 71.6 KB | `IS51 - ML/Recent Notes/Chapter_5_4_Validation_of_Regression_Methods_Detailed (1).pptx`<br>`IS51 - ML/Recent Notes/Chapter_5_4_Validation_of_Regression_Methods_Detailed.pptx` |
| `6e4a2cb87f` | 30.9 KB | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/KNN algorithm with problems (1).docx`<br>`IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-3/KNN algorithm with problems.docx` |
| `c6820eb574` | 18.0 KB | `ISE552 - AI/AI-ISE552 SYLLABUS.docx`<br>`notes/ai/syllabus/ai-ise552-syllabus.docx` |

---

## 4. Subject-by-Subject Full Inventory & Tree

### Computer Networks (24IS53)

- **Raw Workspace Files:** 27
- **Notes Portal Files (`notes/cn/`):** 20

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `fifth-edition-data-communications-and-networking.pdf` | `IS53 - CN/BOOK/fifth-edition-data-communications-and-networking.pdf` | 65.35 MB | Reference/other | ✅ Yes |
| `CIE1&2-2025.pdf` | `IS53 - CN/CIE - PYQ_s/CIE1&2-2025.pdf` | 299.0 KB | PYQ/Question paper | ✅ Yes |
| `CN-UNIT1 Complete.pptx` | `IS53 - CN/Recent Notes/CN-UNIT1 Complete.pptx` | 15.62 MB | Faculty notes | ✅ Yes |
| `CN-Unit2 Complete.pptx` | `IS53 - CN/Recent Notes/CN-Unit2 Complete.pptx` | 12.78 MB | Faculty notes | ✅ Yes |
| `Unit3a (1) (1).pptx` | `IS53 - CN/Recent Notes/Unit3a (1) (1).pptx` | 1.55 MB | Faculty notes | ✅ Yes |
| `2024.pdf` | `IS53 - CN/SEE - PYQ_s/2024.pdf` | 596.4 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025(O).pdf` | `IS53 - CN/SEE - PYQ_s/2025(O).pdf` | 119.1 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025.pdf` | `IS53 - CN/SEE - PYQ_s/2025.pdf` | 152.5 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JAN2023.pdf` | `IS53 - CN/SEE - PYQ_s/JAN2023.pdf` | 647.1 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JAN2026.pdf` | `IS53 - CN/SEE - PYQ_s/JAN2026.pdf` | 331.3 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAKEUP 2023.pdf` | `IS53 - CN/SEE - PYQ_s/MAKEUP 2023.pdf` | 618.5 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `IS53-CN-Unit1.pdf` | `IS53 - CN/Vercel Notes/IS53-CN-Unit1.pdf` | 15.72 MB | Faculty notes | ✅ Yes |
| `IS53-CN-Unit2.pdf` | `IS53 - CN/Vercel Notes/IS53-CN-Unit2.pdf` | 13.07 MB | Faculty notes | ✅ Yes |
| `CS8591 CN Notes (annauniversityedu.blogspot.com).pdf` | `IS53 - CN/Vercel Notes/last year ppts/CS8591 CN Notes (annauniversityedu.blogspot.com).pdf` | 7.04 MB | Faculty notes | ✅ Yes |
| `IPV4 completed  unit 2.ppt` | `IS53 - CN/Vercel Notes/last year ppts/IPV4 completed  unit 2.ppt` | 6.14 MB | Faculty notes | ✅ Yes |
| `Unit1.pdf` | `IS53 - CN/Vercel Notes/last year ppts/Unit1.pdf` | 3.98 MB | Faculty notes | ✅ Yes |
| `Unit2.pdf` | `IS53 - CN/Vercel Notes/last year ppts/Unit2.pdf` | 6.60 MB | Faculty notes | ✅ Yes |
| `ch03.pptx` | `IS53 - CN/Vercel Notes/last year ppts/ch03.pptx` | 3.31 MB | Faculty notes | ✅ Yes |
| `ch04.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch04.ppt` | 436.5 KB | Faculty notes | ✅ Yes |
| `ch19.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch19.ppt` | 1.18 MB | Faculty notes | ✅ Yes |
| `ch1_v1.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch1_v1.ppt` | 722.0 KB | Faculty notes | ✅ Yes |
| `ch20.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch20.ppt` | 1.60 MB | Faculty notes | ✅ Yes |
| `ch21.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch21.ppt` | 1.23 MB | Faculty notes | ✅ Yes |
| `ch22.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch22.ppt` | 2.20 MB | Faculty notes | ✅ Yes |
| `ch23.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch23.ppt` | 2.58 MB | Faculty notes | ✅ Yes |
| `ch24.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch24.ppt` | 1.02 MB | Faculty notes | ✅ Yes |
| `ch2_v1.ppt` | `IS53 - CN/Vercel Notes/last year ppts/ch2_v1.ppt` | 2.40 MB | Faculty notes | ✅ Yes |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `cn-cie-1-and-2.pdf` | `notes/cn/practice/cn-cie-1-and-2.pdf` | 299.0 KB | PYQ/Question paper | ✅ Yes |
| `cn-pyq-handwritten.pdf` | `notes/cn/pyq/handwritten/cn-pyq-handwritten.pdf` | 806.5 KB | Handwritten | ✅ Yes |
| `cn-pyq-preview.webp` | `notes/cn/pyq/handwritten/cn-pyq-preview.webp` | 39.7 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/cn/pyq/pyq-answers.html` | 116.4 KB | Unit notes | ✅ Yes |
| `cn-unit1-handwritten.pdf` | `notes/cn/unit1/handwritten/cn-unit1-handwritten.pdf` | 1.04 MB | Handwritten | ✅ Yes |
| `cn-unit1-preview.webp` | `notes/cn/unit1/handwritten/cn-unit1-preview.webp` | 83.5 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/cn/unit1/handwritten/toc.json` | 1.1 KB | Handwritten | ✅ Yes |
| `is53-cn-unit1.pdf` | `notes/cn/unit1/is53-cn-unit1.pdf` | 11.70 MB | Faculty notes | ✅ Yes |
| `is53-cn-unit1.pptx` | `notes/cn/unit1/is53-cn-unit1.pptx` | 16.68 MB | Faculty notes | ⚠️ Unregistered |
| `unit-1-notes.html` | `notes/cn/unit1/unit-1-notes.html` | 116.7 KB | Unit notes | ✅ Yes |
| `cn-unit2-handwritten.pdf` | `notes/cn/unit2/handwritten/cn-unit2-handwritten.pdf` | 835.5 KB | Handwritten | ✅ Yes |
| `cn-unit2-preview.webp` | `notes/cn/unit2/handwritten/cn-unit2-preview.webp` | 80.6 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/cn/unit2/handwritten/toc.json` | 1.1 KB | Handwritten | ✅ Yes |
| `is53-cn-unit2.pdf` | `notes/cn/unit2/is53-cn-unit2.pdf` | 9.79 MB | Faculty notes | ✅ Yes |
| `is53-cn-unit2.pptx` | `notes/cn/unit2/is53-cn-unit2.pptx` | 13.89 MB | Faculty notes | ⚠️ Unregistered |
| `unit-2-notes.html` | `notes/cn/unit2/unit-2-notes.html` | 90.1 KB | Unit notes | ✅ Yes |
| `cn-unit3-handwritten.pdf` | `notes/cn/unit3/handwritten/cn-unit3-handwritten.pdf` | 543.6 KB | Handwritten | ✅ Yes |
| `cn-unit3-preview.webp` | `notes/cn/unit3/handwritten/cn-unit3-preview.webp` | 72.0 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/cn/unit3/handwritten/toc.json` | 1.1 KB | Handwritten | ✅ Yes |
| `unit-3-notes.html` | `notes/cn/unit3/unit-3-notes.html` | 53.5 KB | Unit notes | ✅ Yes |

### Frontend Development using ReactJS (24ISAEC594)

- **Raw Workspace Files:** 3
- **Notes Portal Files (`notes/reactjs/`):** 14

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `UNIT-1 ReactJS.pptx` | `ISAEC594 - React/Recent Notes/UNIT-1 ReactJS.pptx` | 2.68 MB | Faculty notes | ✅ Yes |
| `Unit-2.pdf` | `ISAEC594 - React/Recent Notes/Unit-2.pdf` | 534.5 KB | Faculty notes | ✅ Yes |
| `JAN2026.pdf` | `ISAEC594 - React/SEE - PYQ_s/JAN2026.pdf` | 334.4 KB | PYQ/Question paper | ℹ️ SEE Practice |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `reactjs-pyq-handwritten.pdf` | `notes/reactjs/pyq/handwritten/reactjs-pyq-handwritten.pdf` | 1.18 MB | Handwritten | ✅ Yes |
| `reactjs-pyq-preview.webp` | `notes/reactjs/pyq/handwritten/reactjs-pyq-preview.webp` | 36.2 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/reactjs/pyq/pyq-answers.html` | 95.2 KB | Unit notes | ✅ Yes |
| `reactjs-syllabus-screenshot.png` | `notes/reactjs/syllabus/reactjs-syllabus-screenshot.png` | 480.6 KB | Lab | ✅ Yes |
| `reactjs-unit1-handwritten.pdf` | `notes/reactjs/unit1/handwritten/reactjs-unit1-handwritten.pdf` | 1.00 MB | Handwritten | ✅ Yes |
| `reactjs-unit1-preview.webp` | `notes/reactjs/unit1/handwritten/reactjs-unit1-preview.webp` | 81.1 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/reactjs/unit1/handwritten/toc.json` | 1.4 KB | Handwritten | ✅ Yes |
| `reactjs-unit1.pdf` | `notes/reactjs/unit1/reactjs-unit1.pdf` | 1.88 MB | Faculty notes | ✅ Yes |
| `reactjs-unit1.pptx` | `notes/reactjs/unit1/reactjs-unit1.pptx` | 2.68 MB | Faculty notes | ⚠️ Unregistered |
| `unit-1-notes.html` | `notes/reactjs/unit1/unit-1-notes.html` | 89.5 KB | Unit notes | ✅ Yes |
| `reactjs-unit2-handwritten.pdf` | `notes/reactjs/unit2/handwritten/reactjs-unit2-handwritten.pdf` | 1.04 MB | Handwritten | ✅ Yes |
| `reactjs-unit2-preview.webp` | `notes/reactjs/unit2/handwritten/reactjs-unit2-preview.webp` | 72.0 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/reactjs/unit2/handwritten/toc.json` | 1.1 KB | Handwritten | ✅ Yes |
| `unit-2-notes.html` | `notes/reactjs/unit2/unit-2-notes.html` | 82.9 KB | Unit notes | ✅ Yes |

### Artificial Intelligence (24ISE552)

- **Raw Workspace Files:** 20
- **Notes Portal Files (`notes/ai/`):** 21

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `AI-ISE552 SYLLABUS.docx` | `ISE552 - AI/AI-ISE552 SYLLABUS.docx` | 18.0 KB | Lab | ✅ Yes |
| `CIE1&2-2025.pdf` | `ISE552 - AI/CIE - PYQ_s/CIE1&2-2025.pdf` | 524.1 KB | PYQ/Question paper | ✅ Yes |
| `CIE1-2022.pdf` | `ISE552 - AI/CIE - PYQ_s/CIE1-2022.pdf` | 1.09 MB | PYQ/Question paper | ✅ Yes |
| `CIE2-2022.pdf` | `ISE552 - AI/CIE - PYQ_s/CIE2-2022.pdf` | 900.0 KB | PYQ/Question paper | ✅ Yes |
| `AI-2.pdf` | `ISE552 - AI/Recent Notes/AI-2.pdf` | 1.62 MB | Faculty notes | ✅ Yes |
| `AI-AGENTS-Uninformed_Search.pdf` | `ISE552 - AI/Recent Notes/AI-AGENTS-Uninformed_Search.pdf` | 170.4 KB | Faculty notes | ✅ Yes |
| `AI-Adversarial_Search.pdf` | `ISE552 - AI/Recent Notes/AI-Adversarial_Search.pdf` | 189.9 KB | Faculty notes | ✅ Yes |
| `AI-Informed_Search.pdf` | `ISE552 - AI/Recent Notes/AI-Informed_Search.pdf` | 173.7 KB | Faculty notes | ✅ Yes |
| `AI-Intelligent_Agents-PS.pdf` | `ISE552 - AI/Recent Notes/AI-Intelligent_Agents-PS.pdf` | 409.3 KB | Faculty notes | ✅ Yes |
| `AI-Intelligent_Agents.pdf` | `ISE552 - AI/Recent Notes/AI-Intelligent_Agents.pdf` | 408.7 KB | Faculty notes | ✅ Yes |
| `AI-Local_Search.pdf` | `ISE552 - AI/Recent Notes/AI-Local_Search.pdf` | 170.3 KB | Faculty notes | ✅ Yes |
| `WhatsApp Image 2026-09-07 at 9.11.31 AM.jpeg` | `ISE552 - AI/Recent Notes/WhatsApp Image 2026-09-07 at 9.11.31 AM.jpeg` | 37.2 KB | PYQ/Question paper | ✅ Yes |
| `2024.pdf` | `ISE552 - AI/SEE - PYQ_s/2024.pdf` | 766.6 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025.pdf` | `ISE552 - AI/SEE - PYQ_s/2025.pdf` | 131.6 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JAN2026.pdf` | `ISE552 - AI/SEE - PYQ_s/JAN2026.pdf` | 343.0 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAY2023.pdf` | `ISE552 - AI/SEE - PYQ_s/MAY2023.pdf` | 712.8 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `AI_ppts.pdf` | `ISE552 - AI/Vercel Notes/AI_ppts.pdf` | 4.26 MB | Faculty notes | ✅ Yes |
| `Unit 1.pdf` | `ISE552 - AI/Vercel Notes/Unit 1.pdf` | 2.94 MB | Faculty notes | ✅ Yes |
| `Unit 2.pdf` | `ISE552 - AI/Vercel Notes/Unit 2.pdf` | 2.49 MB | Faculty notes | ✅ Yes |
| `Units 3, 4 and 5 (incomplete).pdf` | `ISE552 - AI/Vercel Notes/Units 3, 4 and 5 (incomplete).pdf` | 4.52 MB | Faculty notes | ❌ Hold (Out of scope) |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `ai-cie-1-and-2.pdf` | `notes/ai/practice/ai-cie-1-and-2.pdf` | 524.1 KB | PYQ/Question paper | ✅ Yes |
| `ai-pyq-handwritten.pdf` | `notes/ai/pyq/handwritten/ai-pyq-handwritten.pdf` | 895.9 KB | Handwritten | ✅ Yes |
| `ai-pyq-preview.webp` | `notes/ai/pyq/handwritten/ai-pyq-preview.webp` | 36.9 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/ai/pyq/pyq-answers.html` | 105.0 KB | Unit notes | ✅ Yes |
| `ai-ise552-syllabus.docx` | `notes/ai/syllabus/ai-ise552-syllabus.docx` | 18.0 KB | Lab | ⚠️ Unregistered |
| `ai-ise552-syllabus.pdf` | `notes/ai/syllabus/ai-ise552-syllabus.pdf` | 111.2 KB | Lab | ✅ Yes |
| `ai-syllabus-screenshot.png` | `notes/ai/syllabus/ai-syllabus-screenshot.png` | 126.6 KB | Lab | ✅ Yes |
| `ai-intro-intelligent-agents.pdf` | `notes/ai/unit1/ai-intro-intelligent-agents.pdf` | 1.62 MB | Faculty notes | ✅ Yes |
| `ai-problem-solving-agents-alt.pdf` | `notes/ai/unit1/ai-problem-solving-agents-alt.pdf` | 409.3 KB | Faculty notes | ✅ Yes |
| `ai-problem-solving-agents.pdf` | `notes/ai/unit1/ai-problem-solving-agents.pdf` | 408.7 KB | Faculty notes | ✅ Yes |
| `ai-unit1-handwritten.pdf` | `notes/ai/unit1/handwritten/ai-unit1-handwritten.pdf` | 958.0 KB | Handwritten | ✅ Yes |
| `ai-unit1-preview.webp` | `notes/ai/unit1/handwritten/ai-unit1-preview.webp` | 84.4 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/ai/unit1/handwritten/toc.json` | 1.2 KB | Handwritten | ✅ Yes |
| `unit-1-notes.html` | `notes/ai/unit1/unit-1-notes.html` | 130.8 KB | Unit notes | ✅ Yes |
| `ai-informed-search.pdf` | `notes/ai/unit2/ai-informed-search.pdf` | 173.7 KB | Faculty notes | ✅ Yes |
| `ai-local-search.pdf` | `notes/ai/unit2/ai-local-search.pdf` | 170.3 KB | Faculty notes | ✅ Yes |
| `ai-uninformed-search.pdf` | `notes/ai/unit2/ai-uninformed-search.pdf` | 170.4 KB | Faculty notes | ✅ Yes |
| `ai-unit2-handwritten.pdf` | `notes/ai/unit2/handwritten/ai-unit2-handwritten.pdf` | 889.3 KB | Handwritten | ✅ Yes |
| `ai-unit2-preview.webp` | `notes/ai/unit2/handwritten/ai-unit2-preview.webp` | 81.4 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/ai/unit2/handwritten/toc.json` | 1.2 KB | Handwritten | ✅ Yes |
| `unit-2-notes.html` | `notes/ai/unit2/unit-2-notes.html` | 94.1 KB | Unit notes | ✅ Yes |

### Software Engineering (24IS52)

- **Raw Workspace Files:** 29
- **Notes Portal Files (`notes/se/`):** 22

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `Software Engineering - Ian Sommerville.pdf` | `IS52 - SE/Book/Software Engineering - Ian Sommerville.pdf` | 3.93 MB | Reference/other | ✅ Yes |
| `CIE1&2-2025.pdf` | `IS52 - SE/CIE - PYQ_s/CIE1&2-2025.pdf` | 314.9 KB | PYQ/Question paper | ✅ Yes |
| `GitHub_Kanban_Product_Backlog_Mini_Sprint_Lab_Manual.pdf` | `IS52 - SE/LAB/GitHub_Kanban_Product_Backlog_Mini_Sprint_Lab_Manual.pdf` | 46.7 KB | Lab | ✅ Yes |
| `Unit 1.1.pptx` | `IS52 - SE/Recent Notes/Unit 1.1.pptx` | 297.7 KB | Faculty notes | ✅ Yes |
| `Unit 1.2.pptx` | `IS52 - SE/Recent Notes/Unit 1.2.pptx` | 595.6 KB | Faculty notes | ✅ Yes |
| `Unit 1.3.pptx` | `IS52 - SE/Recent Notes/Unit 1.3.pptx` | 450.9 KB | Faculty notes | ✅ Yes |
| `Unit 2.1.pptx` | `IS52 - SE/Recent Notes/Unit 2.1.pptx` | 1.86 MB | Faculty notes | ✅ Yes |
| `Unit 2.2.pptx` | `IS52 - SE/Recent Notes/Unit 2.2.pptx` | 684.7 KB | Faculty notes | ✅ Yes |
| `SE-Syllabus2026-27.docx` | `IS52 - SE/SE-Syllabus2026-27.docx` | 18.9 KB | Lab | ✅ Yes |
| `2023.pdf` | `IS52 - SE/SEE - PYQ_s/2023.pdf` | 576.8 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2024.pdf` | `IS52 - SE/SEE - PYQ_s/2024.pdf` | 577.8 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025(O).pdf` | `IS52 - SE/SEE - PYQ_s/2025(O).pdf` | 116.6 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025.pdf` | `IS52 - SE/SEE - PYQ_s/2025.pdf` | 117.3 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JAN2026.pdf` | `IS52 - SE/SEE - PYQ_s/JAN2026.pdf` | 310.7 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `Unit 2.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit 2.pptx` | 1.49 MB | Faculty notes | ✅ Yes |
| `Unit-1.1.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-1.1.pptx` | 323.6 KB | Faculty notes | ✅ Yes |
| `Unit-1.2.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-1.2.pptx` | 568.7 KB | Faculty notes | ✅ Yes |
| `Unit-1.3.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-1.3.pptx` | 444.8 KB | Faculty notes | ✅ Yes |
| `Unit-3.1.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-3.1.pptx` | 438.6 KB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit-3.2.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-3.2.pptx` | 697.9 KB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit-5.1.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-5.1.pptx` | 304.3 KB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit-5.2.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-5.2.pptx` | 751.6 KB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit-5.3.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit-5.3.pptx` | 444.0 KB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit_4.pptx` | `IS52 - SE/Vercel Notes/PPTs/Unit_4.pptx` | 12.09 MB | Faculty notes | ✅ Yes |
| `Unit 1.pdf` | `IS52 - SE/Vercel Notes/Unit 1.pdf` | 1.39 MB | Faculty notes | ✅ Yes |
| `Unit 2.pdf` | `IS52 - SE/Vercel Notes/Unit 2.pdf` | 1.06 MB | Faculty notes | ✅ Yes |
| `Unit 3.pdf` | `IS52 - SE/Vercel Notes/Unit 3.pdf` | 824.5 KB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit 4.pdf` | `IS52 - SE/Vercel Notes/Unit 4.pdf` | 3.87 MB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit 5.pdf` | `IS52 - SE/Vercel Notes/Unit 5.pdf` | 860.5 KB | Faculty notes | ❌ Hold (Out of scope) |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `se-cie-1-and-2.pdf` | `notes/se/practice/se-cie-1-and-2.pdf` | 314.9 KB | PYQ/Question paper | ✅ Yes |
| `se-pyq-handwritten.pdf` | `notes/se/pyq/handwritten/se-pyq-handwritten.pdf` | 902.7 KB | Handwritten | ✅ Yes |
| `se-pyq-preview.webp` | `notes/se/pyq/handwritten/se-pyq-preview.webp` | 36.9 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/se/pyq/pyq-answers.html` | 136.6 KB | Unit notes | ✅ Yes |
| `se-unit1-handwritten.pdf` | `notes/se/unit1/handwritten/se-unit1-handwritten.pdf` | 909.6 KB | Handwritten | ✅ Yes |
| `se-unit1-preview.webp` | `notes/se/unit1/handwritten/se-unit1-preview.webp` | 89.7 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/se/unit1/handwritten/toc.json` | 1.2 KB | Handwritten | ✅ Yes |
| `unit-1-1.pdf` | `notes/se/unit1/unit-1-1.pdf` | 305.8 KB | Faculty notes | ✅ Yes |
| `unit-1-1.pptx` | `notes/se/unit1/unit-1-1.pptx` | 306.7 KB | Faculty notes | ⚠️ Unregistered |
| `unit-1-2.pdf` | `notes/se/unit1/unit-1-2.pdf` | 722.2 KB | Faculty notes | ✅ Yes |
| `unit-1-2.pptx` | `notes/se/unit1/unit-1-2.pptx` | 595.6 KB | Faculty notes | ⚠️ Unregistered |
| `unit-1-3.pdf` | `notes/se/unit1/unit-1-3.pdf` | 537.5 KB | Faculty notes | ✅ Yes |
| `unit-1-3.pptx` | `notes/se/unit1/unit-1-3.pptx` | 450.9 KB | Faculty notes | ⚠️ Unregistered |
| `unit-1-notes.html` | `notes/se/unit1/unit-1-notes.html` | 106.8 KB | Unit notes | ✅ Yes |
| `se-unit2-handwritten.pdf` | `notes/se/unit2/handwritten/se-unit2-handwritten.pdf` | 624.4 KB | Handwritten | ✅ Yes |
| `se-unit2-preview.webp` | `notes/se/unit2/handwritten/se-unit2-preview.webp` | 83.4 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/se/unit2/handwritten/toc.json` | 1.1 KB | Handwritten | ✅ Yes |
| `unit-2-notes.html` | `notes/se/unit2/unit-2-notes.html` | 86.4 KB | Unit notes | ✅ Yes |
| `unit-2-system-modeling.pdf` | `notes/se/unit2/unit-2-system-modeling.pdf` | 1.16 MB | Faculty notes | ✅ Yes |
| `unit-2-system-modeling.pptx` | `notes/se/unit2/unit-2-system-modeling.pptx` | 2.36 MB | Faculty notes | ⚠️ Unregistered |
| `unit-2.pdf` | `notes/se/unit2/unit-2.pdf` | 406.3 KB | Faculty notes | ✅ Yes |
| `unit-2.pptx` | `notes/se/unit2/unit-2.pptx` | 1.86 MB | Faculty notes | ⚠️ Unregistered |

### Machine Learning (24IS51)

- **Raw Workspace Files:** 57
- **Notes Portal Files (`notes/ml/`):** 21

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `CIE1&2-2026.pdf` | `IS51 - ML/CIE - PYQ_s/CIE1&2-2026.pdf` | 554.2 KB | PYQ/Question paper | ✅ Yes |
| `Assignment-1extended.pdf` | `IS51 - ML/NPTEL/Assignment-1extended.pdf` | 1.03 MB | Assignment/Quiz/Worksheet | ✅ Yes |
| `Assignment-3Extended.pdf` | `IS51 - ML/NPTEL/Assignment-3Extended.pdf` | 1.71 MB | Assignment/Quiz/Worksheet | ✅ Yes |
| `Assignment-5Extended.pdf` | `IS51 - ML/NPTEL/Assignment-5Extended.pdf` | 1.21 MB | Assignment/Quiz/Worksheet | ✅ Yes |
| `Assignment2.pdf` | `IS51 - ML/NPTEL/Assignment2.pdf` | 478.2 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `ML_CurrentYear_Nptel2026.pdf` | `IS51 - ML/NPTEL/ML_CurrentYear_Nptel2026.pdf` | 1019.8 KB | PYQ/Question paper | ✅ Yes |
| `ML_NPTEL_1,2,3,5MultipleCombined.pdf` | `IS51 - ML/NPTEL/ML_NPTEL_1,2,3,5MultipleCombined.pdf` | 3.44 MB | Faculty notes | ✅ Yes |
| `week0-8_UnknownYear.pdf` | `IS51 - ML/NPTEL/week0-8_UnknownYear.pdf` | 1.44 MB | Faculty notes | ✅ Yes |
| `week1-8_UnknownYear2.pdf` | `IS51 - ML/NPTEL/week1-8_UnknownYear2.pdf` | 3.01 MB | Faculty notes | ✅ Yes |
| `week1-8_Year2022.pdf` | `IS51 - ML/NPTEL/week1-8_Year2022.pdf` | 1.50 MB | PYQ/Question paper | ✅ Yes |
| `Basics_of_Learning_Theory_S_Sridhar_Machine_Learning.pptx` | `IS51 - ML/Recent Notes/Basics_of_Learning_Theory_S_Sridhar_Machine_Learning.pptx` | 1.21 MB | Reference/other | ✅ Yes |
| `Chapter_2_10_Feature_Engineering_Dimensionality_Reduction_Sridhar_Vijayalakshmi.pptx` | `IS51 - ML/Recent Notes/Chapter_2_10_Feature_Engineering_Dimensionality_Reduction_Sridhar_Vijayalakshmi.pptx` | 83.8 KB | Reference/other | ✅ Yes |
| `Chapter_2_Mathematics_Feature_Engineering_Dimensionality_Reduction.pptx` | `IS51 - ML/Recent Notes/Chapter_2_Mathematics_Feature_Engineering_Dimensionality_Reduction.pptx` | 105.1 KB | Faculty notes | ✅ Yes |
| `Chapter_2_Understanding_Data_Sridhar_Vijayalakshmi.pptx` | `IS51 - ML/Recent Notes/Chapter_2_Understanding_Data_Sridhar_Vijayalakshmi.pptx` | 301.9 KB | Reference/other | ✅ Yes |
| `Chapter_3.6_Modeling_ML_Detailed.pptx` | `IS51 - ML/Recent Notes/Chapter_3.6_Modeling_ML_Detailed.pptx` | 65.0 KB | Faculty notes | ✅ Yes |
| `Chapter_3.7_Learning_Frameworks_Detailed.pptx` | `IS51 - ML/Recent Notes/Chapter_3.7_Learning_Frameworks_Detailed.pptx` | 58.2 KB | Faculty notes | ✅ Yes |
| `Chapter_3_5_Detailed_Induction_Bias_Bias_Variance.pptx` | `IS51 - ML/Recent Notes/Chapter_3_5_Detailed_Induction_Bias_Bias_Variance.pptx` | 80.1 KB | Faculty notes | ✅ Yes |
| `Chapter_5_1_5_2_5_3_Detailed_PPT_Problems_Solutions.pptx` | `IS51 - ML/Recent Notes/Chapter_5_1_5_2_5_3_Detailed_PPT_Problems_Solutions.pptx` | 87.0 KB | Faculty notes | ✅ Yes |
| `Chapter_5_4_Validation_of_Regression_Methods_Detailed (1).pptx` | `IS51 - ML/Recent Notes/Chapter_5_4_Validation_of_Regression_Methods_Detailed (1).pptx` | 71.6 KB | Faculty notes | ✅ Yes |
| `Chapter_5_4_Validation_of_Regression_Methods_Detailed.pptx` | `IS51 - ML/Recent Notes/Chapter_5_4_Validation_of_Regression_Methods_Detailed.pptx` | 71.6 KB | Faculty notes | ✅ Yes |
| `Chapter_5_Regression_Analysis_Detailed.pptx` | `IS51 - ML/Recent Notes/Chapter_5_Regression_Analysis_Detailed.pptx` | 88.3 KB | Faculty notes | ✅ Yes |
| `Machine_Learning_Chapter_3_Basic_Concepts_of_Learning.pptx` | `IS51 - ML/Recent Notes/Machine_Learning_Chapter_3_Basic_Concepts_of_Learning.pptx` | 57.4 KB | Faculty notes | ✅ Yes |
| `Machine_Learning_Chapter_4_Similarity_Based_Learning.pptx` | `IS51 - ML/Recent Notes/Machine_Learning_Chapter_4_Similarity_Based_Learning.pptx` | 61.6 KB | Faculty notes | ✅ Yes |
| `Multivariate Statistics Notes.pdf` | `IS51 - ML/Recent Notes/Multivariate Statistics Notes.pdf` | 1.74 MB | Faculty notes | ✅ Yes |
| `Linear & ridge regression....docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-1/Linear & ridge regression....docx` | 1.13 MB | Lab | ✅ Yes |
| `ML-1.ipynb` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-1/ML-1.ipynb` | 401.2 KB | Lab | ✅ Yes |
| `ML-1_simple.ipynb` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-1/ML-1_simple.ipynb` | 545.4 KB | Lab | ✅ Yes |
| `winequality-red.csv` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-1/winequality-red.csv` | 82.2 KB | Lab | ✅ Yes |
| `winequality-white.csv` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-1/winequality-white.csv` | 258.2 KB | Lab | ✅ Yes |
| `winequality.names` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-1/winequality.names` | 3.2 KB | Lab | ✅ Yes |
| `Logistic Regression and multinomial logistic regression.docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-2/Logistic Regression and multinomial logistic regression.docx` | 55.4 KB | Lab | ✅ Yes |
| `ML-Prog2.ipynb` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-2/ML-Prog2.ipynb` | 105.2 KB | Lab | ✅ Yes |
| `ML-Prog-3.ipynb` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/ML_programs/ML_Prog-3/ML-Prog-3.ipynb` | 502.2 KB | Lab | ✅ Yes |
| `Customer_Purchases.xlsx` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/Tableau_/Customer_Purchases.xlsx` | 11.9 KB | Lab | ✅ Yes |
| `Tableau.pptx` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/Tableau_/Tableau.pptx` | 3.12 MB | Lab | ✅ Yes |
| `Tableau_Sales_Dataset31-08.xlsx` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/Tableau_/Tableau_Sales_Dataset31-08.xlsx` | 13.1 KB | Lab | ✅ Yes |
| `Untitled0.ipynb` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/Tableau_/Untitled0.ipynb` | 5.5 KB | Lab | ✅ Yes |
| `syllabus_ML-lab_ISL56.pdf` | `IS51 - ML/Recent Notes/Shruti mam/ML-LAB/Tableau_/syllabus_ML-lab_ISL56.pdf` | 417.1 KB | Lab | ✅ Yes |
| `1. Machine Learning by S Sridhar.pdf` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/1. Machine Learning by S Sridhar.pdf` | 76.00 MB | Reference/other | ✅ Yes |
| `2. Tom Mitchell.pdf` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/2. Tom Mitchell.pdf` | 57.50 MB | Reference/other | ✅ Yes |
| `IMPARTUS.xlsx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/IMPARTUS.xlsx` | 8.4 KB | Faculty notes | ✅ Yes |
| `KNN algorithm with problems (1).docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/KNN algorithm with problems (1).docx` | 30.9 KB | Faculty notes | ✅ Yes |
| `6_Correlation_and_Covariance_Problems_with_Solutions.docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-1/6_Correlation_and_Covariance_Problems_with_Solutions.docx` | 38.8 KB | Faculty notes | ✅ Yes |
| `ML-Correlation_and_Covariance_Problems_with_Solutions.docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-1/ML-Correlation_and_Covariance_Problems_with_Solutions.docx` | 28.8 KB | Faculty notes | ✅ Yes |
| `ML-UNIT-1.pptx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-1/ML-UNIT-1.pptx` | 6.02 MB | Faculty notes | ✅ Yes |
| `ML-UNIT-2.pptx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-2/ML-UNIT-2.pptx` | 3.00 MB | Faculty notes | ✅ Yes |
| `KNN algorithm with problems.docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-3/KNN algorithm with problems.docx` | 30.9 KB | Faculty notes | ✅ Yes |
| `Linear_Regression and multiple linear regression_problems.docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-3/Linear_Regression and multiple linear regression_problems.docx` | 46.4 KB | Faculty notes | ✅ Yes |
| `Logistic Regression and multinomial logistic regression.docx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-3/Logistic Regression and multinomial logistic regression.docx` | 1.38 MB | Faculty notes | ✅ Yes |
| `ML-UNIT-3.pptx` | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-3/ML-UNIT-3.pptx` | 247.5 KB | Faculty notes | ✅ Yes |
| `link.txt` | `IS51 - ML/Recent Notes/Shruti mam/link.txt` | 72 B | Faculty notes | ✅ Yes |
| `2023.pdf` | `IS51 - ML/SEE - PYQ_s/2023.pdf` | 749.5 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2024.pdf` | `IS51 - ML/SEE - PYQ_s/2024.pdf` | 677.7 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025.pdf` | `IS51 - ML/SEE - PYQ_s/2025.pdf` | 439.9 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JULY2026.pdf` | `IS51 - ML/SEE - PYQ_s/JULY2026.pdf` | 395.1 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAKEUP2024.pdf` | `IS51 - ML/SEE - PYQ_s/MAKEUP2024.pdf` | 701.2 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `SUPPLE AUGUST 2025.pdf` | `IS51 - ML/SEE - PYQ_s/SUPPLE AUGUST 2025.pdf` | 384.6 KB | PYQ/Question paper | ℹ️ SEE Practice |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `ml-cie-1-2-see.pdf` | `notes/ml/practice/ml-cie-1-2-see.pdf` | 977.1 KB | PYQ/Question paper | ✅ Yes |
| `unit-1-qb.pdf` | `notes/ml/practice/unit-1-qb.pdf` | 4.04 MB | Question bank | ✅ Yes |
| `ml-pyq-handwritten.pdf` | `notes/ml/pyq/handwritten/ml-pyq-handwritten.pdf` | 921.4 KB | Handwritten | ✅ Yes |
| `ml-pyq-preview.webp` | `notes/ml/pyq/handwritten/ml-pyq-preview.webp` | 39.3 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/ml/pyq/pyq-answers.html` | 111.9 KB | Unit notes | ✅ Yes |
| `ml-unit1-handwritten.pdf` | `notes/ml/unit1/handwritten/ml-unit1-handwritten.pdf` | 1.15 MB | Handwritten | ✅ Yes |
| `ml-unit1-preview.webp` | `notes/ml/unit1/handwritten/ml-unit1-preview.webp` | 89.9 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/ml/unit1/handwritten/toc.json` | 1.7 KB | Handwritten | ✅ Yes |
| `unit-1-notes.html` | `notes/ml/unit1/unit-1-notes.html` | 150.4 KB | Unit notes | ✅ Yes |
| `unit-1.pdf` | `notes/ml/unit1/unit-1.pdf` | 2.39 MB | Faculty notes | ✅ Yes |
| `ml-unit2-handwritten.pdf` | `notes/ml/unit2/handwritten/ml-unit2-handwritten.pdf` | 1.04 MB | Handwritten | ✅ Yes |
| `ml-unit2-preview.webp` | `notes/ml/unit2/handwritten/ml-unit2-preview.webp` | 88.5 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/ml/unit2/handwritten/toc.json` | 1.6 KB | Handwritten | ✅ Yes |
| `unit-2-notes.html` | `notes/ml/unit2/unit-2-notes.html` | 122.8 KB | Unit notes | ✅ Yes |
| `unit-2.pdf` | `notes/ml/unit2/unit-2.pdf` | 2.03 MB | Faculty notes | ✅ Yes |
| `ml-unit3-handwritten.pdf` | `notes/ml/unit3/handwritten/ml-unit3-handwritten.pdf` | 563.9 KB | Handwritten | ✅ Yes |
| `ml-unit3-preview.webp` | `notes/ml/unit3/handwritten/ml-unit3-preview.webp` | 79.7 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/ml/unit3/handwritten/toc.json` | 1.5 KB | Handwritten | ✅ Yes |
| `unit-3-notes.html` | `notes/ml/unit3/unit-3-notes.html` | 64.3 KB | Unit notes | ✅ Yes |
| `unit-3-polynomial-regression.pdf` | `notes/ml/unit3/unit-3-polynomial-regression.pdf` | 723.0 KB | Faculty notes | ✅ Yes |
| `unit-3-steps-for-mlalg.pdf` | `notes/ml/unit3/unit-3-steps-for-mlalg.pdf` | 89.5 KB | Faculty notes | ✅ Yes |

### Research Methodology & IPR (24AL58)

- **Raw Workspace Files:** 30
- **Notes Portal Files (`notes/rmipr/`):** 22

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `CR Kothari Research Methodology (1).pdf` | `AL58 - RM/Books/CR Kothari Research Methodology (1).pdf` | 1.91 MB | Reference/other | ✅ Yes |
| `David V. Thiel - Research Methods for Engineers. 1-Cambridge Uni Press (2014).pdf` | `AL58 - RM/Books/David V. Thiel - Research Methods for Engineers. 1-Cambridge Uni Press (2014).pdf` | 12.36 MB | Reference/other | ✅ Yes |
| `2023 CIE.pdf` | `AL58 - RM/CIE - PYQ_s/2023 CIE.pdf` | 347.3 KB | PYQ/Question paper | ✅ Yes |
| `2024 CIE.pdf` | `AL58 - RM/CIE - PYQ_s/2024 CIE.pdf` | 1.36 MB | PYQ/Question paper | ✅ Yes |
| `2025 CIE.pdf` | `AL58 - RM/CIE - PYQ_s/2025 CIE.pdf` | 246.1 KB | PYQ/Question paper | ✅ Yes |
| `Assignment I.pdf` | `AL58 - RM/Other_Component/Assignment I.pdf` | 159.8 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `Assignment II.pdf` | `AL58 - RM/Other_Component/Assignment II.pdf` | 751.8 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `Important Question.pdf` | `AL58 - RM/Other_Component/Important Question.pdf` | 173.8 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `Quiz.pdf` | `AL58 - RM/Other_Component/Quiz.pdf` | 73.8 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `AL58 unit 1 worksheet.pdf` | `AL58 - RM/Recent Notes/AL58 unit 1 worksheet.pdf` | 62.6 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `AL58 unit 2 worksheet.pdf` | `AL58 - RM/Recent Notes/AL58 unit 2 worksheet.pdf` | 58.6 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `AL58 unit 3 worksheet.pdf` | `AL58 - RM/Recent Notes/AL58 unit 3 worksheet.pdf` | 335.3 KB | Assignment/Quiz/Worksheet | ✅ Yes |
| `RM & IPR Unit 1 PPT (1).pptx` | `AL58 - RM/Recent Notes/RM & IPR Unit 1 PPT (1).pptx` | 901.1 KB | Faculty notes | ✅ Yes |
| `Unit 2 ppt.pptx` | `AL58 - RM/Recent Notes/Unit 2 ppt.pptx` | 2.49 MB | Faculty notes | ✅ Yes |
| `Unit 3 part 1.pptx` | `AL58 - RM/Recent Notes/Unit 3 part 1.pptx` | 959.1 KB | Faculty notes | ✅ Yes |
| `2022.pdf` | `AL58 - RM/SEE - PYQ_s/2022.pdf` | 587.9 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2023.pdf` | `AL58 - RM/SEE - PYQ_s/2023.pdf` | 578.0 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2024.pdf` | `AL58 - RM/SEE - PYQ_s/2024.pdf` | 579.4 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025.pdf` | `AL58 - RM/SEE - PYQ_s/2025.pdf` | 117.4 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JAN2026.pdf` | `AL58 - RM/SEE - PYQ_s/JAN2026.pdf` | 301.0 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAKEUP2024.pdf` | `AL58 - RM/SEE - PYQ_s/MAKEUP2024.pdf` | 577.5 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAKEUP2025.pdf` | `AL58 - RM/SEE - PYQ_s/MAKEUP2025.pdf` | 121.4 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `Makeup 2022.pdf` | `AL58 - RM/SEE - PYQ_s/Makeup 2022.pdf` | 590.0 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `Supply 2023.pdf` | `AL58 - RM/SEE - PYQ_s/Supply 2023.pdf` | 575.7 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `Unit 1.pdf` | `AL58 - RM/Vercel Notes/Unit 1.pdf` | 769.1 KB | Faculty notes | ✅ Yes |
| `Unit 2.pdf` | `AL58 - RM/Vercel Notes/Unit 2.pdf` | 1.43 MB | Faculty notes | ✅ Yes |
| `Unit 3 Statistical Table.pdf` | `AL58 - RM/Vercel Notes/Unit 3 Statistical Table.pdf` | 3.12 MB | Faculty notes | ✅ Yes |
| `Unit 3.pdf` | `AL58 - RM/Vercel Notes/Unit 3.pdf` | 1.12 MB | Faculty notes | ✅ Yes |
| `Unit 4.pdf` | `AL58 - RM/Vercel Notes/Unit 4.pdf` | 1.90 MB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit 5.pdf` | `AL58 - RM/Vercel Notes/Unit 5.pdf` | 638.8 KB | Faculty notes | ❌ Hold (Out of scope) |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `rmipr-cie-1-and-2.pdf` | `notes/rmipr/practice/rmipr-cie-1-and-2.pdf` | 246.1 KB | PYQ/Question paper | ✅ Yes |
| `rmipr-makeup-apr-2025.pdf` | `notes/rmipr/practice/rmipr-makeup-apr-2025.pdf` | 121.4 KB | PYQ/Question paper | ✅ Yes |
| `rmipr-see-feb-mar-2025.pdf` | `notes/rmipr/practice/rmipr-see-feb-mar-2025.pdf` | 117.4 KB | PYQ/Question paper | ✅ Yes |
| `rmipr-pyq-handwritten.pdf` | `notes/rmipr/pyq/handwritten/rmipr-pyq-handwritten.pdf` | 873.7 KB | Handwritten | ✅ Yes |
| `rmipr-pyq-preview.webp` | `notes/rmipr/pyq/handwritten/rmipr-pyq-preview.webp` | 40.1 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/rmipr/pyq/pyq-answers.html` | 113.9 KB | Unit notes | ✅ Yes |
| `rmipr-unit1-handwritten.pdf` | `notes/rmipr/unit1/handwritten/rmipr-unit1-handwritten.pdf` | 882.2 KB | Handwritten | ✅ Yes |
| `rmipr-unit1-preview.webp` | `notes/rmipr/unit1/handwritten/rmipr-unit1-preview.webp` | 82.8 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/rmipr/unit1/handwritten/toc.json` | 1.4 KB | Handwritten | ✅ Yes |
| `rm-ipr-unit1.pdf` | `notes/rmipr/unit1/rm-ipr-unit1.pdf` | 658.8 KB | Faculty notes | ✅ Yes |
| `rm-ipr-unit1.pptx` | `notes/rmipr/unit1/rm-ipr-unit1.pptx` | 895.9 KB | Faculty notes | ⚠️ Unregistered |
| `unit-1-notes.html` | `notes/rmipr/unit1/unit-1-notes.html` | 93.0 KB | Unit notes | ✅ Yes |
| `rmipr-unit2-handwritten.pdf` | `notes/rmipr/unit2/handwritten/rmipr-unit2-handwritten.pdf` | 787.0 KB | Handwritten | ✅ Yes |
| `rmipr-unit2-preview.webp` | `notes/rmipr/unit2/handwritten/rmipr-unit2-preview.webp` | 77.1 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/rmipr/unit2/handwritten/toc.json` | 1.2 KB | Handwritten | ✅ Yes |
| `rm-ipr-unit2.pdf` | `notes/rmipr/unit2/rm-ipr-unit2.pdf` | 1.26 MB | Faculty notes | ✅ Yes |
| `rm-ipr-unit2.pptx` | `notes/rmipr/unit2/rm-ipr-unit2.pptx` | 2.51 MB | Faculty notes | ⚠️ Unregistered |
| `unit-2-notes.html` | `notes/rmipr/unit2/unit-2-notes.html` | 78.2 KB | Unit notes | ✅ Yes |
| `rmipr-unit3-handwritten.pdf` | `notes/rmipr/unit3/handwritten/rmipr-unit3-handwritten.pdf` | 337.6 KB | Handwritten | ✅ Yes |
| `rmipr-unit3-preview.webp` | `notes/rmipr/unit3/handwritten/rmipr-unit3-preview.webp` | 53.6 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/rmipr/unit3/handwritten/toc.json` | 1.3 KB | Handwritten | ✅ Yes |
| `unit-3-notes.html` | `notes/rmipr/unit3/unit-3-notes.html` | 28.0 KB | Unit notes | ✅ Yes |

### Environmental Studies (24HS510)

- **Raw Workspace Files:** 26
- **Notes Portal Files (`notes/evs/`):** 29

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `CIE1&2-2023.pdf` | `HS510 - EVS/CIE - PYQ_s/CIE1&2-2023.pdf` | 328.1 KB | PYQ/Question paper | ✅ Yes |
| `CIE1&2-2024.pdf` | `HS510 - EVS/CIE - PYQ_s/CIE1&2-2024.pdf` | 2.36 MB | PYQ/Question paper | ✅ Yes |
| `CIE1&2-2025.pdf` | `HS510 - EVS/CIE - PYQ_s/CIE1&2-2025.pdf` | 486.9 KB | PYQ/Question paper | ✅ Yes |
| `EVS_CIE1_QP-2024 (1).docx` | `HS510 - EVS/CIE - PYQ_s/EVS_CIE1_QP-2024 (1).docx` | 78.8 KB | PYQ/Question paper | ✅ Yes |
| `1. Unit-2 Forest resources - Ecological importance of forests - Copy.pdf` | `HS510 - EVS/Recent Notes/1. Unit-2 Forest resources - Ecological importance of forests - Copy.pdf` | 331.2 KB | Faculty notes | ✅ Yes |
| `2. Unit-2 Water resources - Global water resources distribution.pdf` | `HS510 - EVS/Recent Notes/2. Unit-2 Water resources - Global water resources distribution.pdf` | 308.8 KB | Faculty notes | ✅ Yes |
| `3. Unit-2 Mineral resources - Environmental effects of extracting and processing of mineral resources.pdf` | `HS510 - EVS/Recent Notes/3. Unit-2 Mineral resources - Environmental effects of extracting and processing of mineral resources.pdf` | 263.0 KB | Faculty notes | ✅ Yes |
| `4. Unit-2 Food resources - Effects of modern agriculture.pdf` | `HS510 - EVS/Recent Notes/4. Unit-2 Food resources - Effects of modern agriculture.pdf` | 266.7 KB | Faculty notes | ✅ Yes |
| `5. Unit-2 Land resources - Soil erosion and Desertification.pdf` | `HS510 - EVS/Recent Notes/5. Unit-2 Land resources - Soil erosion and Desertification.pdf` | 292.8 KB | Faculty notes | ✅ Yes |
| `Unit-1.pptx` | `HS510 - EVS/Recent Notes/Unit-1.pptx` | 2.31 MB | Faculty notes | ✅ Yes |
| `Unit-2.pptx` | `HS510 - EVS/Recent Notes/Unit-2.pptx` | 1.72 MB | Faculty notes | ✅ Yes |
| `Unit-3.pptx` | `HS510 - EVS/Recent Notes/Unit-3.pptx` | 5.63 MB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit-4.pptx` | `HS510 - EVS/Recent Notes/Unit-4.pptx` | 12.41 MB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit-5.pptx` | `HS510 - EVS/Recent Notes/Unit-5.pptx` | 1.37 MB | Faculty notes | ❌ Hold (Out of scope) |
| `2025.pdf` | `HS510 - EVS/SEE - PYQ_s/2025.pdf` | 122.3 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `FEB2024.pdf` | `HS510 - EVS/SEE - PYQ_s/FEB2024.pdf` | 668.4 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JAN2026.pdf` | `HS510 - EVS/SEE - PYQ_s/JAN2026.pdf` | 324.3 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAKEUP2024.pdf` | `HS510 - EVS/SEE - PYQ_s/MAKEUP2024.pdf` | 617.3 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAKEUP2025.pdf` | `HS510 - EVS/SEE - PYQ_s/MAKEUP2025.pdf` | 119.0 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `MAKEUP2026.pdf` | `HS510 - EVS/SEE - PYQ_s/MAKEUP2026.pdf` | 345.0 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `EVS links.pdf` | `HS510 - EVS/Vercel Notes/EVS links.pdf` | 75.5 KB | Faculty notes | ✅ Yes |
| `Unit-1 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-1 Notes, MCQ & Questions.pdf` | 1.04 MB | Question bank | ✅ Yes |
| `Unit-2 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-2 Notes, MCQ & Questions.pdf` | 616.3 KB | Question bank | ✅ Yes |
| `Unit-3 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-3 Notes, MCQ & Questions.pdf` | 634.5 KB | Question bank | ❌ Hold (Out of scope) |
| `Unit-4 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-4 Notes, MCQ & Questions.pdf` | 563.9 KB | Question bank | ❌ Hold (Out of scope) |
| `Unit-5 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-5 Notes, MCQ & Questions.pdf` | 576.8 KB | Question bank | ❌ Hold (Out of scope) |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `evs-cie-1.pdf` | `notes/evs/practice/evs-cie-1.pdf` | 486.9 KB | PYQ/Question paper | ✅ Yes |
| `evs-cie1-qp-2024.docx` | `notes/evs/practice/evs-cie1-qp-2024.docx` | 78.8 KB | PYQ/Question paper | ⚠️ Unregistered |
| `evs-cie1-qp-2024.pdf` | `notes/evs/practice/evs-cie1-qp-2024.pdf` | 122.1 KB | PYQ/Question paper | ✅ Yes |
| `evs-pyq-handwritten.pdf` | `notes/evs/pyq/handwritten/evs-pyq-handwritten.pdf` | 791.6 KB | Handwritten | ✅ Yes |
| `evs-pyq-preview.webp` | `notes/evs/pyq/handwritten/evs-pyq-preview.webp` | 36.9 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/evs/pyq/pyq-answers.html` | 89.4 KB | Unit notes | ✅ Yes |
| `evs-unit1-handwritten.pdf` | `notes/evs/unit1/handwritten/evs-unit1-handwritten.pdf` | 771.4 KB | Handwritten | ✅ Yes |
| `evs-unit1-preview.webp` | `notes/evs/unit1/handwritten/evs-unit1-preview.webp` | 76.0 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/evs/unit1/handwritten/toc.json` | 1.2 KB | Handwritten | ✅ Yes |
| `unit-1-notes.html` | `notes/evs/unit1/unit-1-notes.html` | 73.7 KB | Unit notes | ✅ Yes |
| `unit-1.pdf` | `notes/evs/unit1/unit-1.pdf` | 2.15 MB | Faculty notes | ✅ Yes |
| `unit-1.pptx` | `notes/evs/unit1/unit-1.pptx` | 2.31 MB | Faculty notes | ⚠️ Unregistered |
| `evs-unit2-handwritten.pdf` | `notes/evs/unit2/handwritten/evs-unit2-handwritten.pdf` | 728.8 KB | Handwritten | ✅ Yes |
| `evs-unit2-preview.webp` | `notes/evs/unit2/handwritten/evs-unit2-preview.webp` | 76.3 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/evs/unit2/handwritten/toc.json` | 1.2 KB | Handwritten | ✅ Yes |
| `unit-2-food-resources.pdf` | `notes/evs/unit2/unit-2-food-resources.pdf` | 266.7 KB | Faculty notes | ✅ Yes |
| `unit-2-forest-resources.pdf` | `notes/evs/unit2/unit-2-forest-resources.pdf` | 331.2 KB | Faculty notes | ✅ Yes |
| `unit-2-land-resources.pdf` | `notes/evs/unit2/unit-2-land-resources.pdf` | 292.8 KB | Faculty notes | ✅ Yes |
| `unit-2-mineral-resources.pdf` | `notes/evs/unit2/unit-2-mineral-resources.pdf` | 263.0 KB | Faculty notes | ✅ Yes |
| `unit-2-notes.html` | `notes/evs/unit2/unit-2-notes.html` | 65.3 KB | Unit notes | ✅ Yes |
| `unit-2-water-resources.pdf` | `notes/evs/unit2/unit-2-water-resources.pdf` | 308.8 KB | Faculty notes | ✅ Yes |
| `unit-2.pdf` | `notes/evs/unit2/unit-2.pdf` | 1.57 MB | Faculty notes | ✅ Yes |
| `unit-2.pptx` | `notes/evs/unit2/unit-2.pptx` | 1.72 MB | Faculty notes | ⚠️ Unregistered |
| `unit-3.pdf` | `notes/evs/unit3/unit-3.pdf` | 1.70 MB | Faculty notes | ⚠️ Unregistered |
| `unit-3.pptx` | `notes/evs/unit3/unit-3.pptx` | 5.63 MB | Faculty notes | ⚠️ Unregistered |
| `unit-4.pdf` | `notes/evs/unit4/unit-4.pdf` | 3.34 MB | Faculty notes | ⚠️ Unregistered |
| `unit-4.pptx` | `notes/evs/unit4/unit-4.pptx` | 12.41 MB | Faculty notes | ⚠️ Unregistered |
| `unit-5.pdf` | `notes/evs/unit5/unit-5.pdf` | 1.22 MB | Faculty notes | ⚠️ Unregistered |
| `unit-5.pptx` | `notes/evs/unit5/unit-5.pptx` | 1.37 MB | Faculty notes | ⚠️ Unregistered |

### Theory of Computation (24IS54)

- **Raw Workspace Files:** 15
- **Notes Portal Files (`notes/toc/`):** 19

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `CIE1&2-2025.pdf` | `IS54 - TOC/CIE - PYQ_s/CIE1&2-2025.pdf` | 878.2 KB | PYQ/Question paper | ✅ Yes |
| `TOC_Notes.pdf` | `IS54 - TOC/Recent Notes/TOC_Notes.pdf` | 43.47 MB | Faculty notes | ✅ Yes |
| `2024.pdf` | `IS54 - TOC/SEE - PYQ_s/2024.pdf` | 884.0 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `2025.pdf` | `IS54 - TOC/SEE - PYQ_s/2025.pdf` | 147.6 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `JAN2026.pdf` | `IS54 - TOC/SEE - PYQ_s/JAN2026.pdf` | 404.5 KB | PYQ/Question paper | ℹ️ SEE Practice |
| `TOC_Notes.pdf` | `IS54 - TOC/TOC_Notes.pdf` | 43.47 MB | Faculty notes | ✅ Yes |
| `TOC_ unit3.pdf` | `IS54 - TOC/Vercel Notes/TOC_ unit3.pdf` | 2.65 MB | Faculty notes | ❌ Hold (Out of scope) |
| `TOC_unit4.pdf` | `IS54 - TOC/Vercel Notes/TOC_unit4.pdf` | 2.24 MB | Faculty notes | ❌ Hold (Out of scope) |
| `Toc unit 1 and 2.pdf` | `IS54 - TOC/Vercel Notes/Toc unit 1 and 2.pdf` | 5.57 MB | Faculty notes | ✅ Yes |
| `Turing machine.pdf` | `IS54 - TOC/Vercel Notes/Turing machine.pdf` | 1.80 MB | Faculty notes | ✅ Yes |
| `Unit 1.pdf` | `IS54 - TOC/Vercel Notes/Unit 1.pdf` | 22.38 MB | Faculty notes | ✅ Yes |
| `Unit 2.pdf` | `IS54 - TOC/Vercel Notes/Unit 2.pdf` | 10.97 MB | Faculty notes | ✅ Yes |
| `Unit 3.pdf` | `IS54 - TOC/Vercel Notes/Unit 3.pdf` | 23.56 MB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit 4.pdf` | `IS54 - TOC/Vercel Notes/Unit 4.pdf` | 2.62 MB | Faculty notes | ❌ Hold (Out of scope) |
| `Unit 5.pdf` | `IS54 - TOC/Vercel Notes/Unit 5.pdf` | 4.24 MB | Faculty notes | ❌ Hold (Out of scope) |

#### Existing Served Notes Files (`notes/`)
| File Name | Path | Size | Classification | Registered in `subjects.js` |
|:---|:---|:---:|:---|:---:|
| `toc-cie-1-2-see.pdf` | `notes/toc/practice/toc-cie-1-2-see.pdf` | 878.2 KB | PYQ/Question paper | ✅ Yes |
| `toc-pyq-handwritten.pdf` | `notes/toc/pyq/handwritten/toc-pyq-handwritten.pdf` | 783.4 KB | Handwritten | ✅ Yes |
| `toc-pyq-preview.webp` | `notes/toc/pyq/handwritten/toc-pyq-preview.webp` | 36.7 KB | Handwritten | ✅ Yes |
| `pyq-answers.html` | `notes/toc/pyq/pyq-answers.html` | 114.1 KB | Unit notes | ✅ Yes |
| `toc-unit1-handwritten.pdf` | `notes/toc/unit1/handwritten/toc-unit1-handwritten.pdf` | 628.1 KB | Handwritten | ✅ Yes |
| `toc-unit1-preview.webp` | `notes/toc/unit1/handwritten/toc-unit1-preview.webp` | 66.6 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/toc/unit1/handwritten/toc.json` | 1.3 KB | Handwritten | ✅ Yes |
| `toc-unit-1-and-2-alternate.pdf` | `notes/toc/unit1/toc-unit-1-and-2-alternate.pdf` | 5.57 MB | Faculty notes | ✅ Yes |
| `unit-1-notes.html` | `notes/toc/unit1/unit-1-notes.html` | 81.1 KB | Unit notes | ✅ Yes |
| `unit-1.pdf` | `notes/toc/unit1/unit-1.pdf` | 22.38 MB | Faculty notes | ✅ Yes |
| `toc-unit2-handwritten.pdf` | `notes/toc/unit2/handwritten/toc-unit2-handwritten.pdf` | 910.0 KB | Handwritten | ✅ Yes |
| `toc-unit2-preview.webp` | `notes/toc/unit2/handwritten/toc-unit2-preview.webp` | 80.6 KB | Handwritten | ✅ Yes |
| `toc.json` | `notes/toc/unit2/handwritten/toc.json` | 1.2 KB | Handwritten | ✅ Yes |
| `unit-2-notes.html` | `notes/toc/unit2/unit-2-notes.html` | 111.3 KB | Unit notes | ✅ Yes |
| `unit-2.pdf` | `notes/toc/unit2/unit-2.pdf` | 10.97 MB | Faculty notes | ✅ Yes |
| `toc-unit3-alternate.pdf` | `notes/toc/unit3/toc-unit3-alternate.pdf` | 2.65 MB | Faculty notes | ⚠️ Unregistered |
| `unit-3.pdf` | `notes/toc/unit3/unit-3.pdf` | 23.56 MB | Faculty notes | ⚠️ Unregistered |
| `unit-4.pdf` | `notes/toc/unit4/unit-4.pdf` | 2.62 MB | Faculty notes | ⚠️ Unregistered |
| `unit-5.pdf` | `notes/toc/unit5/unit-5.pdf` | 4.24 MB | Faculty notes | ⚠️ Unregistered |

### Engineering Economics (ISAEC591 - Elective)

- **Raw Workspace Files:** 1
- **Notes Portal Files (`notes/eco/`):** 0

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `engineering economics 239p -- R_ Panneerselvam.pdf` | `ISAEC591 - Eco/Book/engineering economics 239p -- R_ Panneerselvam.pdf` | 683.5 KB | Reference/other | ✅ Yes |

### Repository Root Documents

- **Raw Workspace Files:** 3
- **Notes Portal Files (`notes/root/`):** 0

#### Raw Reorganised Source Files
| File Name | Path | Size | Classification | In CIE-1 Scope? |
|:---|:---|:---:|:---|:---:|
| `2023_batch5-6_sem_syllabus.pdf` | `2023_batch5-6_sem_syllabus.pdf` | 1.50 MB | Syllabus | ✅ Yes |
| `CIE1 Schedule.pdf` | `CIE1 Schedule.pdf` | 921.6 KB | Syllabus | ✅ Yes |
| `ISE_III_year_Syllabus_2024_Batch_final.pdf` | `ISE_III_year_Syllabus_2024_Batch_final.pdf` | 1.39 MB | Syllabus | ✅ Yes |

---

## 5. Confusing / Non-URL-Safe Filename Registry
Files containing whitespace, parentheses, copy suffixes, or special punctuation that must be safely normalised into lowercase kebab-case paths for robust web hosting:

| Original File Name | Relative Location | Proposed Clean Name |
|:---|:---|:---|
| `CR Kothari Research Methodology (1).pdf` | `AL58 - RM/Books/CR Kothari Research Methodology (1).pdf` | `cr-kothari-research-methodology-1.pdf` |
| `David V. Thiel - Research Methods for Engineers. 1-Cambridge Uni Press (2014).pdf` | `AL58 - RM/Books/David V. Thiel - Research Methods for Engineers. 1-Cambridge Uni Press (2014).pdf` | `david-v-thiel-research-methods-for-engineers-1-cambridge-uni-press-2014.pdf` |
| `2023 CIE.pdf` | `AL58 - RM/CIE - PYQ_s/2023 CIE.pdf` | `2023-cie.pdf` |
| `2024 CIE.pdf` | `AL58 - RM/CIE - PYQ_s/2024 CIE.pdf` | `2024-cie.pdf` |
| `2025 CIE.pdf` | `AL58 - RM/CIE - PYQ_s/2025 CIE.pdf` | `2025-cie.pdf` |
| `Assignment I.pdf` | `AL58 - RM/Other_Component/Assignment I.pdf` | `assignment-i.pdf` |
| `Assignment II.pdf` | `AL58 - RM/Other_Component/Assignment II.pdf` | `assignment-ii.pdf` |
| `Important Question.pdf` | `AL58 - RM/Other_Component/Important Question.pdf` | `important-question.pdf` |
| `AL58 unit 1 worksheet.pdf` | `AL58 - RM/Recent Notes/AL58 unit 1 worksheet.pdf` | `al58-unit-1-worksheet.pdf` |
| `AL58 unit 2 worksheet.pdf` | `AL58 - RM/Recent Notes/AL58 unit 2 worksheet.pdf` | `al58-unit-2-worksheet.pdf` |
| `AL58 unit 3 worksheet.pdf` | `AL58 - RM/Recent Notes/AL58 unit 3 worksheet.pdf` | `al58-unit-3-worksheet.pdf` |
| `RM & IPR Unit 1 PPT (1).pptx` | `AL58 - RM/Recent Notes/RM & IPR Unit 1 PPT (1).pptx` | `rm-ipr-unit-1-ppt-1.pptx` |
| `Unit 2 ppt.pptx` | `AL58 - RM/Recent Notes/Unit 2 ppt.pptx` | `unit-2-ppt.pptx` |
| `Unit 3 part 1.pptx` | `AL58 - RM/Recent Notes/Unit 3 part 1.pptx` | `unit-3-part-1.pptx` |
| `Makeup 2022.pdf` | `AL58 - RM/SEE - PYQ_s/Makeup 2022.pdf` | `makeup-2022.pdf` |
| `Supply 2023.pdf` | `AL58 - RM/SEE - PYQ_s/Supply 2023.pdf` | `supply-2023.pdf` |
| `Unit 1.pdf` | `AL58 - RM/Vercel Notes/Unit 1.pdf` | `unit-1.pdf` |
| `Unit 2.pdf` | `AL58 - RM/Vercel Notes/Unit 2.pdf` | `unit-2.pdf` |
| `Unit 3 Statistical Table.pdf` | `AL58 - RM/Vercel Notes/Unit 3 Statistical Table.pdf` | `unit-3-statistical-table.pdf` |
| `Unit 3.pdf` | `AL58 - RM/Vercel Notes/Unit 3.pdf` | `unit-3.pdf` |
| `Unit 4.pdf` | `AL58 - RM/Vercel Notes/Unit 4.pdf` | `unit-4.pdf` |
| `Unit 5.pdf` | `AL58 - RM/Vercel Notes/Unit 5.pdf` | `unit-5.pdf` |
| `CIE1&2-2023.pdf` | `HS510 - EVS/CIE - PYQ_s/CIE1&2-2023.pdf` | `cie1-2-2023.pdf` |
| `CIE1&2-2024.pdf` | `HS510 - EVS/CIE - PYQ_s/CIE1&2-2024.pdf` | `cie1-2-2024.pdf` |
| `CIE1&2-2025.pdf` | `HS510 - EVS/CIE - PYQ_s/CIE1&2-2025.pdf` | `cie1-2-2025.pdf` |
| `EVS_CIE1_QP-2024 (1).docx` | `HS510 - EVS/CIE - PYQ_s/EVS_CIE1_QP-2024 (1).docx` | `evs-cie1-qp-2024-1.docx` |
| `1. Unit-2 Forest resources - Ecological importance of forests - Copy.pdf` | `HS510 - EVS/Recent Notes/1. Unit-2 Forest resources - Ecological importance of forests - Copy.pdf` | `1-unit-2-forest-resources-ecological-importance-of-forests-copy.pdf` |
| `2. Unit-2 Water resources - Global water resources distribution.pdf` | `HS510 - EVS/Recent Notes/2. Unit-2 Water resources - Global water resources distribution.pdf` | `2-unit-2-water-resources-global-water-resources-distribution.pdf` |
| `3. Unit-2 Mineral resources - Environmental effects of extracting and processing of mineral resources.pdf` | `HS510 - EVS/Recent Notes/3. Unit-2 Mineral resources - Environmental effects of extracting and processing of mineral resources.pdf` | `3-unit-2-mineral-resources-environmental-effects-of-extracting-and-processing-of-mineral-resources.pdf` |
| `4. Unit-2 Food resources - Effects of modern agriculture.pdf` | `HS510 - EVS/Recent Notes/4. Unit-2 Food resources - Effects of modern agriculture.pdf` | `4-unit-2-food-resources-effects-of-modern-agriculture.pdf` |
| `5. Unit-2 Land resources - Soil erosion and Desertification.pdf` | `HS510 - EVS/Recent Notes/5. Unit-2 Land resources - Soil erosion and Desertification.pdf` | `5-unit-2-land-resources-soil-erosion-and-desertification.pdf` |
| `EVS links.pdf` | `HS510 - EVS/Vercel Notes/EVS links.pdf` | `evs-links.pdf` |
| `Unit-1 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-1 Notes, MCQ & Questions.pdf` | `unit-1-notes-mcq-questions.pdf` |
| `Unit-2 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-2 Notes, MCQ & Questions.pdf` | `unit-2-notes-mcq-questions.pdf` |
| `Unit-3 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-3 Notes, MCQ & Questions.pdf` | `unit-3-notes-mcq-questions.pdf` |
| `Unit-4 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-4 Notes, MCQ & Questions.pdf` | `unit-4-notes-mcq-questions.pdf` |
| `Unit-5 Notes, MCQ & Questions.pdf` | `HS510 - EVS/Vercel Notes/Unit-5 Notes, MCQ & Questions.pdf` | `unit-5-notes-mcq-questions.pdf` |
| `CIE1&2-2026.pdf` | `IS51 - ML/CIE - PYQ_s/CIE1&2-2026.pdf` | `cie1-2-2026.pdf` |
| `Chapter_5_4_Validation_of_Regression_Methods_Detailed (1).pptx` | `IS51 - ML/Recent Notes/Chapter_5_4_Validation_of_Regression_Methods_Detailed (1).pptx` | `chapter-5-4-validation-of-regression-methods-detailed-1.pptx` |
| `Multivariate Statistics Notes.pdf` | `IS51 - ML/Recent Notes/Multivariate Statistics Notes.pdf` | `multivariate-statistics-notes.pdf` |
| ... and 49 additional files ... | | |
