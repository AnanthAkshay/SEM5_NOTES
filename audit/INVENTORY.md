# Repository & Materials Inventory — CIE-1 Scope Rebuild

**Date of Audit**: October 9, 2026  
**Auditor**: Antigravity Assistant for Aki (5th Sem ISE, MSRIT)  
**Target Milestone**: CIE-1 Examination Period (13–16 October 2026)  
**Safety Status**: Git tag `pre-cie1-scope` established; working on branch `cie1-rebuild`.

---

## 1. Syllabus Ground Truth & Hierarchy

The newest syllabus source always takes precedence. Conflicts between older batch PDFs and newest department course documents are resolved in favor of the 2026–27 course outlines.

| Priority | Document / Path | Scope / Coverage | Role in CIE-1 Rebuild |
| :--- | :--- | :--- | :--- |
| **P1 (Highest)** | `IS52 - SE/SE-Syllabus2026-27.docx` | Software Engineering (IS52) | **Authoritative SE Syllabus**. Supersedes the 2024 batch PDF. New Coordinator: Dr. Krishna Raj RM. Updated Agile & Model-driven topics. |
| **P1 (Highest)** | `ISE552 - AI/AI-ISE552 SYLLABUS.docx` | Artificial Intelligence (ISE552) | **Authoritative AI Syllabus**. Coordinator: Dr. Jagadeesh Sai D. Contains detailed 5-unit curriculum & NPTEL links. |
| **P2 (Batch)** | `ISE_III_year_Syllabus_2024_Batch_final.pdf` (83 pages) | All 5th Sem Core & Elective Courses | **Current Batch Curriculum (AY 2026–2027, Batch 2024)**. Covers CN (24IS53), ML (24IS51), TOC (24IS54), RMIPR (24AL58), EVS (24HS510), ReactJS (24ISAEC594). |
| **P3 (Schedule)**| `CIE1 Schedule.pdf` (Page 2) | Official Department CIE-1 Timetable | **Definitive Exam Schedule & Time Slots** (13 Oct – 16 Oct 2026). Confirms course codes, timings, and coordinators. |
| **P4 (Historical)**| `2023_batch5-6_sem_syllabus.pdf` (90 pages) | Previous Batch (AY 2025–2026, Batch 2023) | Used only for cross-referencing previous batch subject codes (`IS51` vs `IS61`, etc.). |
| **P5 (Cached)** | `audit/syllabus_ground_truth.json` & `audit/*_raw.txt` | Pre-parsed text dumps | Quick machine lookup of transcribed section boundaries. |

---

## 2. Textbooks Present (Source Material Only — Never Published)

In accordance with **Safety Rule 3**, all copyrighted reference textbooks are added to `.gitignore` under root and `sources/textbooks/`, strictly excluded from git tracking, and never served on the website. Notes and answers cite them by Author, Edition, Chapter, Section, and Page.

| Subject | Textbook Title & Authors | Local File Location | Size | Citation Key |
| :--- | :--- | :--- | :--- | :--- |
| **ML** | *Machine Learning*, S. Sridhar & M. Vijayalakshmi (Oxford University Press, 2021) | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/1. Machine Learning by S Sridhar.pdf` | 76.0 MB | `Sridhar & Vijayalakshmi 2021` |
| **ML** | *Machine Learning*, Tom M. Mitchell (McGraw-Hill, 1997) | `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/2. Tom Mitchell.pdf` | 57.5 MB | `Mitchell 1997` |
| **SE** | *Software Engineering*, Ian Sommerville, 10th Edition (Pearson, 2016) | `IS52 - SE/Book/Software Engineering - Ian Sommerville.pdf` | 3.93 MB | `Sommerville 10e` |
| **CN** | *Data Communications and Networking*, Behrouz A. Forouzan, 5th Edition (McGraw-Hill, 2013) | `IS53 - CN/BOOK/fifth-edition-data-communications-and-networking.pdf` | 65.4 MB | `Forouzan 5e` |
| **CN** | *CS8591 Computer Networks Lecture Notes* | `IS53 - CN/Vercel Notes/last year ppts/CS8591 CN Notes.pdf` | 7.04 MB | `Anna Univ CS8591` |
| **RM & IPR** | *Research Methodology: Methods and Techniques*, C.R. Kothari & Gaurav Garg, 4th Edition (New Age, 2019) | `AL58 - RM/Books/CR Kothari Research Methodology (1).pdf` | 1.91 MB | `Kothari 4e` |
| **RM & IPR** | *Research Methods for Engineers*, David V. Thiel (Cambridge University Press, 2014) | `AL58 - RM/Books/David V. Thiel - Research Methods for Engineers.pdf` | 12.4 MB | `Thiel 2014` |
| **Eco (Out)**| *Engineering Economics*, R. Panneerselvam, 2nd Edition (PHI, 2013) | `ISAEC591 - Eco/Book/engineering economics 239p -- R_ Panneerselvam.pdf` | 0.67 MB | *Out of CIE-1 scope* |
| **AI** | *Artificial Intelligence: A Modern Approach*, Stuart Russell & Peter Norvig, 4th Edition | Synthesized through faculty decks (`AI-Intelligent_Agents`, `AI-Adversarial_Search`) | — | `Russell & Norvig AIMA` |
| **TOC** | Faculty Course Notes & Lecture Compilations | `IS54 - TOC/Recent Notes/TOC_Notes.pdf`, `Toc unit 1 and 2.pdf`, `Turing machine.pdf` | 51.5 MB | `MSRIT TOC Notes` |
| **EVS** | Unit-wise Notes, MCQ & Questions, Dr. H U Raghavendra | `HS510 - EVS/Vercel Notes/Unit-1…5 Notes, MCQ & Questions.pdf` | 33.5 MB | `Raghavendra EVS` |

---

## 3. Faculty Lecture Material Inventory

### 3.1 Computer Networks (24IS53)
- `IS53 - CN/Recent Notes/CN-UNIT1 Complete.pptx` (15.6 MB) — Introduction, physical layer, topologies, OSI & TCP/IP layers.
- `IS53 - CN/Recent Notes/CN-Unit2 Complete.pptx` (12.8 MB) — Data link layer, framing, flow control, error control (CRC, Checksum, Hamming), MAC protocols, CSMA/CD, CSMA/CA, Ethernet.
- `IS53 - CN/Recent Notes/Unit3a (1) (1).pptx` (1.55 MB) — Network layer services, packet switching, IPv4 addressing (Classful & Classless CIDR).
- `IS53 - CN/Vercel Notes/last year ppts/IPV4 completed unit 2.ppt` (6.14 MB) — In-depth subnetting and CIDR address mask numericals.
- `IS53 - CN/Vercel Notes/last year ppts/ch03.pptx`, `ch04.ppt`, `ch19.ppt`, `ch20.ppt`, `ch21.ppt`, `ch22.ppt`, `ch23.ppt`, `ch24.ppt`.

### 3.2 Front-end Development using React JS (24ISAEC594)
- `ISAEC594 - React/Recent Notes/UNIT-1 ReactJS.pptx` (2.68 MB, 115 slides) — React introduction, JSX, Virtual DOM, Components (Class & Functional), Props, State, Component Lifecycle.
- `ISAEC594 - React/Recent Notes/Unit-2.pdf` (0.52 MB) — React Hooks (`useState`, `useEffect`, `useContext`, `useRef`), Event handling, Forms & controlled inputs, Lifting state up.

### 3.3 Artificial Intelligence (24ISE552)
- `ISE552 - AI/Recent Notes/AI-Intelligent_Agents.pdf` & `AI-Intelligent_Agents-PS.pdf` (0.40 MB) — AI definitions (4 approaches), Agents, Environments, PEAS representation, 5 agent architectures.
- `ISE552 - AI/Recent Notes/AI-AGENTS-Uninformed_Search.pdf` (0.17 MB) — Problem-solving agents, BFS, DFS, DLS, IDDFS, Uniform Cost Search, Bidirectional Search.
- `ISE552 - AI/Recent Notes/AI-Informed_Search.pdf` (0.17 MB) — Best-First Search, Greedy Search, A* Search, Admissible & Consistent Heuristics, 8-puzzle numericals.
- `ISE552 - AI/Recent Notes/AI-Local_Search.pdf` (0.17 MB) — Hill climbing (foothill, ridge, plateau problems), Simulated Annealing, Genetic Algorithms.
- `ISE552 - AI/Recent Notes/AI-Adversarial_Search.pdf` (0.19 MB) — Game theory, Minimax algorithm, Alpha-Beta pruning traces.
- `ISE552 - AI/Recent Notes/AI-2.pdf` (1.62 MB) — Consolidated Unit 1 & Unit 2 faculty slide compilation.
- `ISE552 - AI/Recent Notes/WhatsApp Image 2026-09-07 at 9.11.31 AM.jpeg` — **9 High-Priority Important Questions photo**.

### 3.4 Software Engineering (24IS52)
- `IS52 - SE/Recent Notes/Unit 1.1.pptx` (0.29 MB) — Professional software development, Software engineering ethics.
- `IS52 - SE/Recent Notes/Unit 1.2.pptx` (0.58 MB) — Software process models (Waterfall, Incremental, Reuse-oriented), Process activities, Coping with change.
- `IS52 - SE/Recent Notes/Unit 1.3.pptx` (0.44 MB) — Agile software development, Agile methods, Extreme Programming (XP), Scrum, Agile project management.
- `IS52 - SE/Recent Notes/Unit 2.1.pptx` (1.86 MB) — Requirements engineering (Functional & Non-functional), Software Requirements Specification (SRS), IEEE 830, Elicitation & Validation.
- `IS52 - SE/Recent Notes/Unit 2.2.pptx` (0.67 MB) — System modeling, Context models, Interaction models (Use Case, Sequence), Structural models (Class), Behavioral models (State Machine).
- `IS52 - SE/LAB/GitHub_Kanban_Product_Backlog_Mini_Sprint_Lab_Manual.pdf` — Practical lab exercises for Unit 1.

### 3.5 Machine Learning (24IS51)
- `IS51 - ML/Recent Notes/Machine_Learning_Chapter_3_Basic_Concepts_of_Learning.pptx` & `Basics_of_Learning_Theory...pptx` — Unit 1 Introduction, Well-posed learning problems, Designing learning systems, Perspectives and issues.
- `IS51 - ML/Recent Notes/Chapter_2_Understanding_Data...pptx` & `Chapter_2_Mathematics_Feature_Engineering...pptx` — Unit 2 Data types, Correlation, Covariance, Feature scaling, Normalization, Standardization.
- `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-1/ML-Correlation_and_Covariance_Problems_with_Solutions.docx` — Worked covariance/correlation numerical problems.
- `IS51 - ML/Recent Notes/Chapter_5_Regression_Analysis_Detailed.pptx`, `Chapter_5_1_5_2_5_3_Detailed...pptx`, `Chapter_5_4_Validation_of_Regression...pptx` — Unit 3 Regression Analysis (Simple Linear Regression, OLS derivations, Multiple Linear Regression, Polynomial Regression, Ridge & Lasso Regularization, Logistic Regression, Cost functions, Gradient Descent).
- `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-3/Linear_Regression and multiple linear regression_problems.docx` — Worked regression numericals with step-by-step math.
- `IS51 - ML/Recent Notes/Shruti mam/ML-THEORY/UNIT-3/Logistic Regression and multinomial logistic regression.docx` — Logistic regression derivations and odds ratios.
- `IS51 - ML/NPTEL/` — Weekly assignment question banks covering regression and foundational concepts.

### 3.6 Research Methodology & IPR (24AL58)
- `AL58 - RM/Recent Notes/RM & IPR Unit 1 PPT (1).pptx` (0.88 MB) — Unit 1 Research problem, objectives, types of research, research approaches, criteria of good research.
- `AL58 - RM/Recent Notes/Unit 2 ppt.pptx` (2.49 MB) — Unit 2 Defining research problem, technique involved, literature review, research design, exploratory/descriptive/causal designs.
- `AL58 - RM/Recent Notes/Unit 3 part 1.pptx` (0.94 MB) — Unit 3 Sampling design, census vs sample, steps in sample design, criteria of selecting sampling procedure, characteristics of good sample design.
- `AL58 - RM/Other_Component/Important Question.pdf` (0.17 MB, 7 pages) — Department curated high-yield question compilation.
- `AL58 - RM/Other_Component/Assignment I.pdf`, `Assignment II.pdf`, `Quiz.pdf` — Continuous assessment problem sets.
- `AL58 - RM/Recent Notes/AL58 unit 1/2/3 worksheet.pdf` — Unit-wise worksheets with practice exercises.

### 3.7 Environmental Studies (24HS510)
- `HS510 - EVS/Recent Notes/Unit-1.pptx` (2.31 MB) & `Unit-1 Notes, MCQ & Questions.pdf` — Environment definition, scope, multidisciplinary nature, public awareness, ecosystem structure, energy flow, food chains.
- `HS510 - EVS/Recent Notes/Unit-2.pptx` (1.72 MB) & `Unit-2 Notes, MCQ & Questions.pdf` — Natural resources, forest resources, water resources, mineral resources, food resources, land resources.
- `HS510 - EVS/Recent Notes/1. Unit-2 Forest resources...pdf` to `5. Unit-2 Land resources...pdf` — Specialized topic decks.
- `HS510 - EVS/CIE - PYQ_s/EVS_CIE1_QP-2024 (1).docx` — 50-mark question bank.

### 3.8 Theory of Computation (24IS54)
- `IS54 - TOC/Recent Notes/TOC_Notes.pdf` & `Toc unit 1 and 2.pdf` — Complete handwritten & typed lecture notes for Unit 1 & Unit 2.
- `IS54 - TOC/Vercel Notes/Unit 1.pdf` (22.4 MB) & `Unit 2.pdf` (11.0 MB) — DFA, NFA, $\epsilon$-NFA, subset construction algorithm, DFA minimization (table-filling algorithm), regular expressions, Arden's theorem, Pumping Lemma for Regular Languages.

---

## 4. Question Paper & PYQ Audit (Subject-by-Course-Name Resolution)

As instructed, course names were extracted **directly from the text inside the question papers**, resolving scheme/semester code reuse:

| Relative File Path | Scanned / Text | Pages | Course Name Extracted from Inside Paper | Scheme Code on Paper | Actual Target Subject |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `IS53 - CN/CIE - PYQ_s/CIE1&2-2025.pdf` | **Scanned** (Rendered) | 2 | `Computer Networks` (IA-1 & IA-2) | `IS53` | **CN (CIE-1 & 2)** |
| `IS53 - CN/SEE - PYQ_s/JAN2026.pdf` | Text (4645 chars) | 2 | `Computer Networks` | `23IS53` | **CN (SEE)** |
| `IS53 - CN/SEE - PYQ_s/2025.pdf` | Text (4618 chars) | 2 | `Computer Networks` | `IS53` | **CN (SEE)** |
| `IS53 - CN/SEE - PYQ_s/2025(O).pdf` | Text (3866 chars) | 2 | `Computer Networks` | `IS51(OOO)` | **CN (SEE)** |
| `IS53 - CN/SEE - PYQ_s/2024.pdf` | Text (4799 chars) | 2 | `Computer Networks` | `IS53` | **CN (SEE)** |
| `IS53 - CN/SEE - PYQ_s/JAN2023.pdf` | Text (4837 chars) | 3 | `Computer Networks` | `IS51` | **CN (SEE)** |
| `IS53 - CN/SEE - PYQ_s/MAKEUP 2023.pdf` | Text (5282 chars) | 3 | `Computer Networks` | `IS51` | **CN (SEE)** |
| `ISAEC594 - React/SEE - PYQ_s/JAN2026.pdf` | Text (4173 chars) | 3 | `Frontend Development using React JS` | `23ISAEC594` | **ReactJS (SEE)** |
| `ISE552 - AI/CIE - PYQ_s/CIE1&2-2025.pdf` | **Scanned** (Rendered) | 3 | `Artificial Intelligence` (IA-1 & IA-2) | `IS52` | **AI (CIE-1 & 2)** |
| `ISE552 - AI/CIE - PYQ_s/CIE1-2022.pdf` | **Scanned** (Rendered) | 2 | `Artificial Intelligence` (IA-1) | `ISE552` | **AI (CIE-1)** |
| `ISE552 - AI/CIE - PYQ_s/CIE2-2022.pdf` | **Scanned** (Rendered) | 2 | `Artificial Intelligence` (IA-2) | `ISE552` | **AI (CIE-2)** |
| `ISE552 - AI/SEE - PYQ_s/JAN2026.pdf` | Text (4623 chars) | 3 | `Artificial Intelligence` | `23IS52` | **AI (SEE)** |
| `ISE552 - AI/SEE - PYQ_s/2025.pdf` | Text (4037 chars) | 2 | `Artificial Intelligence` | `IS52` | **AI (SEE)** |
| `ISE552 - AI/SEE - PYQ_s/2024.pdf` | Text (4294 chars) | 2 | `Artificial Intelligence` | `IS52` | **AI (SEE)** |
| `ISE552 - AI/SEE - PYQ_s/MAY2023.pdf` | Text (4432 chars) | 2 | `Artificial Intelligence` (6th Sem Elective) | `ISE644` | **AI (SEE)** |
| `IS52 - SE/CIE - PYQ_s/CIE1&2-2025.pdf` | **Scanned** (Rendered) | 2 | `Software Engineering` (IA-1 & IA-2) | `IS51` | **SE (CIE-1 & 2)** |
| `IS52 - SE/SEE - PYQ_s/JAN2026.pdf` | Text (4522 chars) | 2 | `Software Engineering` | `21/22/23IS51` | **SE (SEE)** |
| `IS52 - SE/SEE - PYQ_s/2025.pdf` | Text (4143 chars) | 2 | `Software Engineering` | `IS51` | **SE (SEE)** |
| `IS52 - SE/SEE - PYQ_s/2025(O).pdf` | Text (3264 chars) | 2 | `Software Engineering` | `IS53(OOO)` | **SE (SEE)** |
| `IS52 - SE/SEE - PYQ_s/2024.pdf` | Text (3374 chars) | 2 | `Software Engineering` | `IS51` | **SE (SEE)** |
| `IS52 - SE/SEE - PYQ_s/2023.pdf` | Text (3557 chars) | 2 | `Software Engineering` | `IS53` | **SE (SEE)** |
| `IS51 - ML/CIE - PYQ_s/CIE1&2-2026.pdf` | **Scanned** (Rendered) | 4 | `Machine Learning` (IA-1 & IA-2) | `22IS62 / IS51` | **ML (CIE-1 & 2)** |
| `IS51 - ML/SEE - PYQ_s/JULY2026.pdf` | Text (6353 chars) | 3 | `Machine Learning` | `23IS62` | **ML (SEE)** |
| `IS51 - ML/SEE - PYQ_s/2025.pdf` | Text (5617 chars) | 4 | `Machine Learning` | `21/22IS62` | **ML (SEE)** |
| `IS51 - ML/SEE - PYQ_s/SUPPLE AUGUST 2025.pdf`| Text (5083 chars) | 3 | `Machine Learning` | `22IS62` | **ML (SEE)** |
| `IS51 - ML/SEE - PYQ_s/2024.pdf` | Text (5957 chars) | 3 | `Machine Learning` | `IS62` | **ML (SEE)** |
| `IS51 - ML/SEE - PYQ_s/MAKEUP2024.pdf` | Text (4896 chars) | 3 | `Machine Learning` | `IS62` | **ML (SEE)** |
| `IS51 - ML/SEE - PYQ_s/2023.pdf` | Text (5618 chars) | 4 | `Machine Learning` | `IS61` | **ML (SEE)** |
| `AL58 - RM/CIE - PYQ_s/2025 CIE.pdf` | **Scanned** (Rendered) | 2 | `Research Methodology & IPR` (IA-1 & 2) | `AL58` | **RMIPR (CIE)** |
| `AL58 - RM/CIE - PYQ_s/2024 CIE.pdf` | **Scanned** (Rendered) | 2 | `Research Methodology & IPR` (IA-1 & 2) | `AL58` | **RMIPR (CIE)** |
| `AL58 - RM/CIE - PYQ_s/2023 CIE.pdf` | **Scanned** (Rendered) | 2 | `Research Methodology & IPR` (IA-1 & 2) | `AL58` | **RMIPR (CIE)** |
| `AL58 - RM/SEE - PYQ_s/JAN2026.pdf` | Text (4300 chars) | 2 | `Research Methodology & IPR` | `23AL58` | **RMIPR (SEE)** |
| `AL58 - RM/SEE - PYQ_s/2025.pdf` | Text (4100 chars) | 2 | `Research Methodology & IPR` | `AL58` | **RMIPR (SEE)** |
| `AL58 - RM/SEE - PYQ_s/MAKEUP2025.pdf` | Text (3337 chars) | 2 | `Research Methodology & IPR` | `AL58` | **RMIPR (SEE)** |
| `AL58 - RM/SEE - PYQ_s/2024.pdf` | Text (4200 chars) | 2 | `Research Methodology & IPR` | `AL58` | **RMIPR (SEE)** |
| `AL58 - RM/SEE - PYQ_s/MAKEUP2024.pdf` | Text (3500 chars) | 2 | `Research Methodology & IPR` | `AL58` | **RMIPR (SEE)** |
| `HS510 - EVS/CIE - PYQ_s/CIE1&2-2025.pdf`| **Scanned** (Rendered) | 2 | `Environmental Studies` (IA-1 & 2) | `HS510` | **EVS (CIE)** |
| `HS510 - EVS/CIE - PYQ_s/CIE1&2-2024.pdf`| **Scanned** (Rendered) | 3 | `Environmental Studies` (IA-1 & 2) | `HS510` | **EVS (CIE)** |
| `HS510 - EVS/CIE - PYQ_s/CIE1&2-2023.pdf`| **Scanned** (Rendered) | 4 | `Environmental Studies` (IA-1 & 2) | `HS510` | **EVS (CIE)** |
| `HS510 - EVS/SEE - PYQ_s/JAN2026.pdf` | Text (4738 chars) | 3 | `Environmental Studies` | `23HS510` | **EVS (SEE)** |
| `HS510 - EVS/SEE - PYQ_s/2025.pdf` | Text (4200 chars) | 3 | `Environmental Studies` | `HS510` | **EVS (SEE)** |
| `HS510 - EVS/SEE - PYQ_s/FEB2024.pdf` | Text (4150 chars) | 3 | `Environmental Studies` | `HS510` | **EVS (SEE)** |
| `IS54 - TOC/CIE - PYQ_s/CIE1&2-2025.pdf` | **Scanned** (Rendered) | 6 | `Theory of Computation` (IA-1, 2 & SEE) | `IS54` | **TOC (CIE & SEE)** |
| `IS54 - TOC/SEE - PYQ_s/JAN2026.pdf` | Text (4791 chars) | 3 | `Theory of Computation` | `21/22/23IS54` | **TOC (SEE)** |
| `IS54 - TOC/SEE - PYQ_s/2025.pdf` | Text (3774 chars) | 2 | `Theory of Computation` | `IS54` | **TOC (SEE)** |
| `IS54 - TOC/SEE - PYQ_s/2024.pdf` | Text (4275 chars) | 3 | `Theory of Computation` | `IS54` | **TOC (SEE)** |

---

## 5. Junk & Build Artifacts Excluded from Repository

The following files and directories are excluded via `.gitignore` and must never be tracked or deployed to GitHub Pages:

- **Copyrighted Textbooks**: `*Sridhar*.pdf`, `*Mitchell*.pdf`, `*Sommerville*.pdf`, `*Forouzan*.pdf`, `*data-communications-and-networking*.pdf`, `*Kothari*.pdf`, `*Thiel*.pdf`, `*Panneerselvam*.pdf`, `*engineering economics*.pdf`, `sources/textbooks/`.
- **Scratch and Test Directories**: `scratch/`, `build/`, `audit/screens/`, `audit/scanned_pyq/`.
- **Node & Python Runtime**: `node_modules/`, `__pycache__/`, `*.pyc`, `.playwright/`, `playwright-report/`, `test-results/`.
- **Build Logs & Metadata**: `*.log`, `npm-debug.log*`, `lighthouse/`, `*.report.json`, `*.report.html`.
- **Stray OS Artifacts**: `Thumbs.db`, `.DS_Store`, `[Dd]esktop.ini`.

---

## 6. Old-vs-New Unit Map & CIE-1 Scoping Table

| Subject | Code | Old Served Units | New CIE-1 Scope | Changes & Adjustments |
| :--- | :--- | :--- | :--- | :--- |
| **Computer Networks** | `24IS53` | Units 1, 2, 3 | **Unit 1, Unit 2, Unit 3 up to "IPv4 Addressing – Classless"** | • Units 1 & 2 fully retained.<br>• Unit 3 trimmed: stop at IPv4 Classless/CIDR/subnetting.<br>• Removed Unit 3 topics after CIDR (NAT, IPv6, routing). |
| **React JS** | `24ISAEC594` | Units 1, 2, 3 | **Unit 1, Unit 2 (Full)** | • Units 1 & 2 retained.<br>• Unit 3 (Redux, Router, Server-side) removed from CIE-1 scope. |
| **Artificial Intelligence** | `24ISE552` | Units 1, 2, 3 | **Unit 1, Unit 2 (Full)** | • Units 1 & 2 retained.<br>• Unit 3 (Knowledge representation, logic, planning) removed from CIE-1 scope.<br>• High-priority 9-question photo bank answered in Unit 1. |
| **Software Engineering** | `24IS52` | Units 1, 2, 3 | **Unit 1, Unit 2 (Full)** | • Updated to 2026–27 syllabus (Dr. Krishna Raj RM).<br>• Units 1 & 2 retained (Agile, Scrum, XP, Requirements, UML, Context/Interaction/Behavioral models).<br>• Unit 3 (Architectural design, testing) removed. |
| **Machine Learning** | `24IS51` | Units 1, 2, 3 | **Unit 1, Unit 2, Unit 3 (Regression Portion Only)** | • Unit 1 & Unit 2 retained.<br>• Unit 3 strictly trimmed: keep Linear, Multiple, Polynomial, Ridge/Lasso, and Logistic Regression.<br>• Dropped KNN/similarity and Decision Trees from Unit 3. |
| **RM & IPR** | `24AL58` | Units 1, 2, 3 | **Unit 1, Unit 2, Unit 3 up to "Characteristics of a Good Sample Design"** | • Units 1 & 2 retained.<br>• Unit 3 strictly trimmed: stop at Sample Design characteristics.<br>• Dropped Hypothesis testing, data collection, measurement, and IPR. |
| **Environmental Studies** | `24HS510` | Units 1, 2, 3 | **Unit 1, Unit 2 (Full)** | • Units 1 & 2 retained.<br>• Unit 3 (Energy resources) removed from CIE-1 scope. |
| **Theory of Computation** | `24IS54` | Units 1, 2, 3 | **Unit 1, Unit 2 (Full)** | • Units 1 & 2 retained (DFA, NFA, Regular Expressions, Pumping Lemma).<br>• Unit 3 (CFGs, Pushdown Automata) removed from CIE-1 scope. |

---

*Inventory completed and recorded in accordance with Section 1.*
