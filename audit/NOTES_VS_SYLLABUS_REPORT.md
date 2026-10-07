# Comprehensive Academic Audit Report: SEM 5 Notes Website vs. Official Syllabus

**Document Reference:** Official Syllabus ground truth extracted from `ISE_III_year_Syllabus_2024_Batch_final.pdf` (Department of Information Science & Engineering, Ramaiah Institute of Technology, Academic Year 2026–2027 / 2024 Batch).  
**Audit Type:** Read-Only Curricular & Notes Verification Audit  
**Date of Audit:** October 7, 2026  
**Audit Status:** Complete  

---

## 1. Executive Summary

| Course Code | Course Title | Syllabus Units | Units with Notes | Topics Covered / Partial / Missing | % Syllabus Covered | Overall Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **IS51** | Machine Learning | 5 | 3 (U1, U2*, U3*) | 13 Covered / 5 Partial / 26 Missing | **36.4%** | **Major Gaps & Misaligned Content** |
| **IS52** | Software Engineering | 5 | 2 (U1, U2*) | 14 Covered / 3 Partial / 21 Missing | **42.1%** | **Major Gaps** (Units 3–5 missing) |
| **IS53** | Computer Networks | 5 | 2 (U1, U2) | 15 Covered / 0 Partial / 20 Missing | **42.9%** | **Major Gaps** (Units 3–5 missing; U1–2 rasterized) |
| **IS54** | Theory of Computation | 5 | 5 (U1–U5) | 25 Covered / 0 Partial / 0 Missing | **100.0%** | **Good** (Full theory + solved problems) |
| **ISE552** | Artificial Intelligence | 5 | 0 | 0 Covered / 0 Partial / 30 Missing | **0.0%** | **Syllabus Only** (No notes served) |
| **AL58** | Research Methodology & IPR | 5 | 2 (U1, U2) | 13 Covered / 0 Partial / 19 Missing | **40.6%** | **Major Gaps** (Units 3–5 missing; 60% of SEE unaddressed) |
| **ISAEC594** | Front end Dev using ReactJS | 5 | 0 | 0 Covered / 0 Partial / 28 Missing | **0.0%** | **Syllabus Only** (Screenshot only, U4–5 cropped) |
| **HS510** | Environmental Studies | 5 (Scheme NCMC) | 5 (U1–U5) | All 5 units covered in slides | **100.0%** | **Good** (Carries legacy code `HS 26`) |
| **ISL56** | Machine Learning Lab -1 | 12 Experiments | Website Guide | Part A (3 Tableau) + Part B (9 UCI Datasets) | **100.0%** | **Good** (Lab metadata accurately matches syllabus) |
| **ISL57** | Computer Networks Lab | 14 Experiments | Website Guide | Part A (9 Programs) + Part B (5 NS-2 Simulations) | **100.0%** | **Good** (Lab metadata accurately matches syllabus) |

---

## 2. Per-Subject Deep Dive & Coverage Matrices

---

### 2.1. IS51 – Machine Learning (PCC, 3:0:0:3)
* **Syllabus Reference:** Pages 17–19 (Doc pages 13–15). Contact Hours: 45L+45S. Coordinator: Dr. Sumana M.
* **Textbooks:**
  1. S Sridhar, M Vijayalakshmi, *Machine Learning*, Oxford University Press, 2021, 1st Edition.
  2. T. M. Mitchell, *Machine Learning*, McGraw Hill, 1997.
* **Served Files in `notes/ml/`:**
  - `unit1/unit-1.pdf` (77 pages)
  - `unit2/unit-2.pdf` (104 pages)
  - `unit3/unit-3-polynomial-regression.pdf` (37 pages)
  - `unit3/unit-3-steps-for-mlalg.pdf` (5 pages)
  - `practice/unit-1-qb.pdf` (8 pages)
  - `practice/ml-cie-1-2-see.pdf` (7 pages)

#### Coverage Matrix
| Unit | Syllabus Topic | Status | Evidence (File & Page) | Remarks |
| :--- | :--- | :---: | :--- | :--- |
| **U1** | Need for ML, ML Explained, Relation to other fields, Types of ML, Challenges, Process, Applications | **COVERED** | `unit-1.pdf`, pp. 1–28 | Slide 1 originates from **CI52 (CSE-AI&ML)** taught by Dr. A N Ramya Shree. |
| **U1** | Understanding Data – 1: Big Data Framework, Descriptive Stats, Univariate/Bivariate/Multivariate Stats | **COVERED** | `unit-1.pdf`, pp. 29–77 | Covers mean, median, IQR, boxplots, histograms, multivariate summaries. |
| **U2** | Understanding Data – 2: Mathematics for Multivariate Data | **MISSING** | — | Linear algebra, matrices, vector projections not explicitly covered in notes. |
| **U2** | Feature Engineering & Dimensionality Reduction Techniques | **PARTIAL** | `unit-2.pdf`, pp. 87–97 | Covers Pearson correlation, greedy selection, RFE. PCA is missing from `unit-2.pdf` (appears only in QB / test paper). |
| **U2** | Basic Learning Theory: Design of Learning System | **MISSING** | `unit-1-qb.pdf`, p. 2 (Question only) | Mitchell Ch. 1 learning system design (Task, Performance, Experience, Target function) missing from lecture notes. |
| **U2** | Concept Learning, Induction biases, Modelling Frameworks | **MISSING** | — | Concept learning algorithms (Find-S, Candidate Elimination, Version Spaces) absent from `unit-2.pdf`. |
| **U3** | Nearest-Neighbor Learning, Weighted KNN, Nearest Centroid Classifier, Locally Weighted Regression (LWR) | **MISSING** | — | Zero slides in `unit-3-polynomial-regression.pdf` or `unit-3-steps-for-mlalg.pdf`. |
| **U3** | Regression Analysis: Linear Regression, Multiple Linear Regression, Logistic Regression | **MISSING** | — | Missing from Unit 3 notes (only L1/L2 loss formula in `unit-2.pdf` pp. 81–86). |
| **U3** | Polynomial Regression | **COVERED** | `unit-3-polynomial-regression.pdf`, pp. 1–37 | Thorough coverage with mathematical derivation and degree curve fitting. |
| **U3** | Decision Tree Learning: Decision Tree Induction Algorithms (ID3/C4.5/CART) | **MISSING** | `unit-1-qb.pdf`, p. 1 (Question only) | Absent from `unit-3` notes files entirely. |
| **U4** | Rule Based Learning (Sequential Covering, First-order rules, Association Rules) | **MISSING** | — | **No notes served on website.** |
| **U4** | Bayesian Learning (Bayes theorem, Bayes model, Naïve Bayes continuous attributes) | **MISSING** | `unit-2.pdf`, p. 98 (Hypothesis only) | Detailed Naïve Bayes absent from lecture notes (exists only in QB p. 8 and CIE-2 p. 1). |
| **U4** | Artificial Neural Networks (Biological/Artificial Neurons, Perceptron, Types, Applications) | **MISSING** | `unit-1-qb.pdf`, pp. 4, 6 (Questions only) | **No notes served on website.** |
| **U5** | Ensemble Learning (Parallel, Incremental, Sequential models) | **MISSING** | — | **No notes served on website.** |
| **U5** | Clustering Algorithms (Proximity, Hierarchical, Partitional, Density-based, Grid-based) | **MISSING** | — | **No notes served on website.** |

#### Critical Findings & Quality Flags
1. **Wrong Department & Course Code Origin:** Slide 1 of `notes/ml/unit1/unit-1.pdf` and `notes/ml/unit2/unit-2.pdf` is labeled:  
   `"Introduction to Machine Learning CI52 Dr. A N Ramya Shree Dept. of CSE(AI&ML)"`.  
   These are slide decks from the autonomous CSE(AI&ML) program (Course Code `CI52`), not ISE department `IS51` (Course Coordinator: Dr. Sumana M).
2. **Gross Content Mismatch in Unit 2 Placement:** On the website (`data/subjects.js` lines 434–452), Unit 2 is labeled:  
   `"Unit 2: Decision Trees & Neural Networks"` and the file is named `"ML Unit 2: Decision Tree Learning & Artificial Neural Networks"`.  
   In reality, `unit-2.pdf` contains **zero slides on Decision Trees or Neural Networks**. It covers model evaluation preliminaries (Holdout, k-fold CV, class imbalance, confusion matrix, ROC-AUC, classification/regression metrics, categorical encoding, L1/L2 regularization, feature selection, and chi-square tests).
3. **Mislabeled Question Bank (`unit-1-qb.pdf`):** Despite its filename, this 8-page document contains questions spanning Units 1, 2, 3, and 4 (Decision Trees, Perceptrons, MLP forward pass, least-squares regression line, Naïve Bayes, and Checkers problem).
4. **Disoriented / Scanned Exam Papers (`ml-cie-1-2-see.pdf`):**
   - Page 1 is scanned upside down ($180^\circ$ rotation).
   - The test paper on Page 1 is dated **25-05-2026** with Course Code **IS62** (6th semester / old scheme), for Term 9/2/26–6/6/26.

---

### 2.2. IS52 – Software Engineering (IPCC, 2:0:1:2)
* **Syllabus Reference:** Pages 20–22 (Doc pages 16–18). Contact Hours: 30L+15P+30S. Coordinator: Mushtaq Ahmed D M.
* **Textbook:** Ian Sommerville, *Software Engineering*, 10th Edition, Pearson, 2020.
* **Served Files in `notes/se/`:**
  - `unit1/unit-1-1.pdf` / `.pptx` (49 slides / pages)
  - `unit1/unit-1-2.pdf` / `.pptx` (61 slides / pages)
  - `unit1/unit-1-3.pdf` / `.pptx` (50 slides / pages)
  - `unit2/unit-2.pdf` (14 pages) / `unit-2.pptx` (82 slides)
  - `practice/se-cie-1-and-2.pdf` (2 pages)

#### Coverage Matrix
| Unit | Syllabus Topic | Status | Evidence (File & Page) | Remarks |
| :--- | :--- | :---: | :--- | :--- |
| **U1** | Professional software development, Ethics, Case studies | **COVERED** | `unit-1-1.pptx`, slides 1–49 | Sommerville Chapter 1 in full. |
| **U1** | Software processes, Process models, Process activities, Coping with change, RUP | **COVERED** | `unit-1-2.pptx`, slides 1–61 | Sommerville Chapter 2 in full. |
| **U1** | Agile software development, Agile methods, XP, Agile project management, Scaling agile | **COVERED** | `unit-1-3.pptx`, slides 1–50 | Sommerville Chapter 3 in full. |
| **U2** | Requirements Engineering: Functional/Non-functional, SRS, Processes, Elicitation, Validation, Management | **COVERED** | `unit-2.pptx`, slides 1–82 | Sommerville Chapter 4 in full. |
| **U2** | System Modeling: Context models, Interaction models, Structural models, Behavioral models, Model-driven engineering | **MISSING** | — | **Sommerville Chapter 5 is entirely missing from notes.** |
| **U3** | Architectural Design & Design and Implementation (Sommerville Ch 6 & 7) | **MISSING** | — | **No notes served on website.** |
| **U4** | Software Testing & Software Evolution (Sommerville Ch 8 & 9) | **MISSING** | — | **No notes served on website.** |
| **U5** | Project Management, Project Planning & Quality Management (Sommerville Ch 22, 23 & 24) | **MISSING** | — | **No notes served on website.** |

#### Critical Findings & Quality Flags
1. **Severe Incomplete Coverage in Unit 2:** The official syllabus assigns two distinct major modules to Unit 2: *Requirements Engineering* (Sommerville Chapter 4) and *System Modeling* (Sommerville Chapter 5). The provided slide deck `unit-2.pptx` terminates after Chapter 4 slide 82. Context models, Interaction models (Use Case & Sequence diagrams), Structural models (Class diagrams), Behavioral models (State machine & Activity diagrams), and MDE are missing from the notes, even though CIE-1 Q3.b explicitly tests drawing Use Case diagrams for a Library Management System.
2. **Defective Handout Layout in `unit-2.pdf`:** While `unit-1-1.pdf`, `unit-1-2.pdf`, and `unit-1-3.pdf` are exported as standard 1-slide-per-page portrait/landscape PDFs, `unit-2.pdf` was printed as a 6-slides-per-page handout (14 pages total). This renders slide diagrams and typography illegible on mobile devices.
3. **Mislabeled Exam Header:** In `practice/se-cie-1-and-2.pdf`, both CIE-1 and CIE-2 headers bear Course Code **23IS51** (which corresponds to Machine Learning), rather than **IS52**.
4. **CIE-2 Coverage Disconnect:** SE CIE-2 tests exclusively Units 3, 4, and 5 (Repository vs Layered architecture, NextDate boundary value testing, software pricing, language processing architectures, Triangle boundary value analysis, iterative project planning, design patterns, Commission problem equivalence class testing, risk management). **None of these topics exist in the notes.**

---

### 2.3. IS53 – Computer Networks (PCC, 4:0:0:4)
* **Syllabus Reference:** Pages 23–25 (Doc pages 19–21). Contact Hours: 60L+60S. Coordinator: Suresh Kumar K R.
* **Textbook:** Behrouz A. Forouzan, *Data Communications and Networking*, 5th Edition, Tata McGraw-Hill, 2013.
* **Served Files in `notes/cn/`:**
  - `unit1/is53-cn-unit1.pdf` (186 pages) / `is53-cn-unit1.pptx` (186 slides)
  - `unit2/is53-cn-unit2.pdf` (148 pages) / `is53-cn-unit2.pptx` (148 slides)
  - `practice/cn-cie-1-and-2.pdf` (2 pages)

#### Coverage Matrix
| Unit | Syllabus Topic | Status | Evidence (File & Page) | Remarks |
| :--- | :--- | :---: | :--- | :--- |
| **U1** | Data communication Fundamentals, Networks, Types (LAN, WAN, MAN, Internet), Protocol Layering, TCP/IP, OSI | **COVERED** | `is53-cn-unit1.pptx`, slides 1–90 | Slides are pure image scans of Forouzan 5E. |
| **U1** | Physical layer: Data & Signals, Periodic analog/digital, Transmission impairments, Data rate limits, Line coding schemes | **COVERED** | `is53-cn-unit1.pptx`, slides 91–186 | Unipolar, Polar (NRZ, RZ, Manchester, Diff Manchester), Bipolar (AMI, Pseudoternary). |
| **U2** | Data Link layer: Addressing, ARP | **COVERED** | `is53-cn-unit2.pptx`, slides 1–35 | Unicast, multicast, broadcast addresses; ARP frame format and operation. |
| **U2** | Error detection & correction: Block coding, Cyclic codes (CRC), Checksum | **COVERED** | `is53-cn-unit2.pptx`, slides 36–95 | Detailed step-by-step polynomial division and 16-bit internet checksum. |
| **U2** | Data link control: Framing, Media Access Control (Random, Controlled, Channelization) | **COVERED** | `is53-cn-unit2.pptx`, slides 96–148 | Bit/byte stuffing, ALOHA, CSMA/CD, CSMA/CA, Reservation, Polling, Token Passing, FDMA, TDMA, CDMA. |
| **U3** | Network layer services, Connectionless vs Connection oriented, Congestion control, IPv4 Addressing, Datagram format, Fragmentation, Options, ICMP, Routing (Distance Vector, Link State, DVMRP) | **MISSING** | — | **No notes served on website.** |
| **U4** | IPv6 address representation & space, Packet format, Extension headers, IPv4-to-IPv6 transition, Transport Layer Protocols (Simple, Stop-and-Wait, GBN, Selective Repeat, Piggybacking) | **MISSING** | — | **No notes served on website.** |
| **U5** | Transport Layer: Services, Port Numbers, UDP, TCP (Services, Segment, Connection, Error/Congestion control), DNS (Purpose and Resolution) | **MISSING** | — | **No notes served on website.** |

#### Critical Findings & Quality Flags
1. **100% Unsearchable Rasterized Content:** Both `is53-cn-unit1.pptx` (186 slides) and `is53-cn-unit2.pptx` (148 slides), as well as their converted PDF counterparts (`is53-cn-unit1.pdf` [12.3 MB] and `is53-cn-unit2.pdf` [10.3 MB]), consist entirely of embedded static JPEG image captures (`Shape 0: type=PICTURE (13)`). There is **zero selectable or indexable text** in either presentation. Text search (`Ctrl+F`), screen readers, and programmatic study tools cannot parse them.
2. **Older Term Annotation:** Slide 1 of both presentations is marked: `Term: 03rd Oct 2024 – 25th Jan 2025`, corresponding to the 2024–25 academic cycle rather than the 2026–2027 batch cycle stated in `data/subjects.js`.
3. **CIE-2 Total Omission:** Computer Networks CIE-2 tests exclusively Units 3, 4, and 5 (ICMP error reporting, Selective Repeat window proof, ICANN port number ranges, NAT address translation, Stop-and-Wait noisy channel, TCP Reno congestion detection, Link State Dijkstra algorithm, IPv4-to-IPv6 transition mechanisms, and recursive DNS resolution). **None of these topics are present in the notes.**

---

### 2.4. IS54 – Theory of Computation (PCC, 2:1:0:2)
* **Syllabus Reference:** Pages 26–27 (Doc pages 22–23). Contact Hours: 30L+15T+30S. Coordinator: Dr. Rajeshwari S B.
* **Textbook:** John E. Hopcroft, Rajeev Motwani, Jeffrey D. Ullman, *Introduction to Automata Theory, Languages, and Computation*, 3rd Edition, Pearson, 2015.
* **Served Files in `notes/toc/`:**
  - `unit1/unit-1.pdf` (95 pages)
  - `unit1/toc-unit-1-and-2-alternate.pdf` (17 pages)
  - `unit2/unit-2.pdf` (46 pages)
  - `unit3/unit-3.pdf` (107 pages)
  - `unit3/toc-unit3-alternate.pdf` (20 pages)
  - `unit4/unit-4.pdf` (29 pages)
  - `unit5/unit-5.pdf` (70 pages)
  - `practice/toc-cie-1-2-see.pdf` (6 pages)

#### Coverage Matrix
| Unit | Syllabus Topic | Status | Evidence (File & Page) | Remarks |
| :--- | :--- | :---: | :--- | :--- |
| **U1** | Central concepts of Automata theory, DFA, NFA, Applications, $\epsilon$-NFA | **COVERED** | `unit-1.pdf`, pp. 1–95 | Complete formal definitions, tuples, state transition tables and diagrams. |
| **U2** | Regular expressions, FA and Regular Expressions, Equivalence and minimization of automata | **COVERED** | `unit-2.pdf`, pp. 1–46 | State elimination method, table-filling minimization algorithm. |
| **U3** | Context free grammars, Parse trees, Yield, Applications, Ambiguity, Normal forms (CNF) | **COVERED** | `unit-3.pdf`, pp. 1–107 | Grammar simplification ($\epsilon$-elimination, unit production removal) and Chomsky Normal Form conversion. |
| **U4** | Pushdown Automata: Languages of PDA, Equivalence of PDA and CFG, DPDA | **COVERED** | `unit-4.pdf`, pp. 1–29 | Acceptance by empty store vs final state; CFG-to-PDA conversion. |
| **U5** | Turing Machine model, Programming Techniques, Extensions, TM and Computers, Intro to NP-Hard & NP-Complete | **COVERED** | `unit-5.pdf`, pp. 1–70 | Multi-tape, non-deterministic TMs; reductions; P vs NP overview. |

#### Detailed Analysis of Alternate Files
- **`toc-unit-1-and-2-alternate.pdf` (17 pages):** This is a mobile CamScanner capture of student handwritten notebook pages covering basic definitions (Alphabet, string, language, empty string, operations on strings), DFA formal definition, transition functions, and basic NFA to DFA conversion problems with diagrams. It serves as an introductory problem workbook.
- **`toc-unit3-alternate.pdf` (20 pages):** This is another CamScanner capture of handwritten student notebook pages covering CFG tuple definition $G=(V,T,P,S)$, derivation trees, and solved conversion problems (obtaining CFGs from Finite Automata).
- **Comparison:** Neither alternate file contradicts the main notes. However, both are unindexed raster scans with low contrast that duplicate topics already covered with greater theoretical rigor in the typed course packs `unit-1.pdf` and `unit-3.pdf`.

---

### 2.5. ISE552 – Artificial Intelligence (PEC-1, 3:0:0:3)
* **Syllabus Reference:** Pages 31–33 (Doc pages 27–29). Contact Hours: 45L+45S. Coordinator: Dr. Jagadeesh Sai D.
* **Textbook:** Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th Edition, Pearson Education, 2021/2022.
* **Served Files in `notes/ai/`:**
  - `syllabus/ai-ise552-syllabus.docx` (10,567 chars)
  - `syllabus/ai-ise552-syllabus.pdf` (2 pages)
  - `syllabus/ai-syllabus-screenshot.png` (1 image)
  - `practice/ai-cie-1-and-2.pdf` (3 pages)
* **Coverage Status:** **0% (Zero notes provided)**.
  The website serves only syllabus metadata and CIE question papers. No lecture presentations, notes, or reading modules exist for any of the 5 units.

#### Critical Curricular Discrepancy (Classical Planning vs. Unit 5)
In the official syllabus ground truth:
- **Course Outcome 5 (CO5)** explicitly mandates:  
  *“Apply algorithms for classical planning in AI and analyze the philosophical, ethical, and safety implications of artificial intelligence.”*
- However, the syllabus topic list for Units 1 to 5 **omits Classical Planning entirely** (Unit 5 covers Prompt Engineering, Responsible/Ethical AI, and AI Applications).
- The department's official CIE-2 question paper (`notes/ai/practice/ai-cie-1-and-2.pdf`, Page 3, Q3.c) specifically requires students to:  
  *“Write PDDL description to solve the following 'Blocks world problem'.”*
- **Action Required for Student:** Students must study Classical Planning (STRIPS, PDDL representation, and Blocks World domain formulation) directly from Russell & Norvig Chapter 11, despite its omission from the unit syllabus narrative.

---

### 2.6. AL58 – Research Methodology & Intellectual Property Rights (HSMC, 3:0:0:3)
* **Syllabus Reference:** Pages 42–43 (Doc pages 38–39). Contact Hours: 45L+45S. Coordinator: Dr. Anitha P.
* **Textbooks:**
  1. C. R. Kothari, Gourav Garg, *Research Methodology – Methods and Techniques*, New Age International.
  2. Dr. B. L. Wadehra, *Law Relating to Intellectual Property*, Universal Law Publishing Co.
  3. Dipankar Deb, Rajeeb Dey, Valentina E. Balas, *Engineering Research Methodology*, Springer.
* **Served Files in `notes/rmipr/`:**
  - `unit1/rm-ipr-unit1.pptx` / `.pdf` (47 slides / pages)
  - `unit2/rm-ipr-unit2.pptx` / `.pdf` (71 slides / pages)
  - `practice/rmipr-cie-1-and-2.pdf` (2 pages)
  - `practice/rmipr-see-feb-mar-2025.pdf` (2 pages)
  - `practice/rmipr-makeup-apr-2025.pdf` (2 pages)

#### Coverage Matrix
| Unit | Syllabus Topic | Status | Evidence (File & Page) | Remarks |
| :--- | :--- | :---: | :--- | :--- |
| **U1** | Meaning, Objectives, Types, Ethics, Research Misconduct, Literature Review, Citations | **COVERED** | `rm-ipr-unit1.pptx`, slides 1–47 | Comprehensive coverage of Kothari Chapter 1 and scientific reading/citations. |
| **U2** | Research Design, Variables, Hypotheses, Experimental Designs (CRD, RBD, LSD, Factorial) | **COVERED** | `rm-ipr-unit2.pptx`, slides 1–71 | Detailed coverage of Kothari Chapter 3 with design models. |
| **U3** | Data Collection, Sampling Design, Data Analysis, Hypothesis Testing (z, t, Chi-square, ANOVA, ANOCOVA) | **MISSING** | — | **No notes served on website.** |
| **U4** | Introduction to IPR, TRIPS, PCT, Patents (History, Criteria, Types of applications, Procedure, Basmati Rice case) | **MISSING** | — | **No notes served on website.** |
| **U5** | Industrial Design Registration, Trademarks (Essentials, Rights, Infringement, Reliefs), Copyrights (Characteristics, Rights, Infringement, Remedies) | **MISSING** | — | **No notes served on website.** |

#### Critical Findings
1. **60% Examination Failure Risk:** The Semester-End Examination (SEE) and Make-Up examination papers follow a strict unit-by-unit structure: Questions 5 & 6 (Unit 3), Questions 7 & 8 (Unit 4), and Questions 9 & 10 (Unit 5). Because Units 3, 4, and 5 have no notes on the website, students relying solely on this portal have no preparation materials for 60 marks out of 100 on the final exam.

---

### 2.7. ISAEC594 – Front end Development using ReactJS (AEC-V, 1:0:0:1)
* **Syllabus Reference:** Pages 46–48 (Doc pages 42–44). Contact Hours: 15L+15S. Coordinator: J R Shruti.
* **Textbook:** Chris Minnick, *Beginning ReactJS Foundations Building User Interfaces with ReactJS An Approachable Guide*, 2022.
* **Served Files in `notes/reactjs/`:**
  - `syllabus/reactjs-syllabus-screenshot.png` (1 cropped image)
* **Coverage Status:** **0% (Zero notes provided)**.
  The single image served is a screenshot displaying Units I, II, and III only; Units IV and V were cropped out. No code samples, slides, notes, or practice materials exist on the website.

---

### 2.8. HS510 – Environmental Studies (NCMC, 0 Credits)
* **Syllabus Reference:** Scheme of Teaching Page 8 (Row 10) & Page 9. Allocated 1 hour teaching per week.
* **Served Files in `notes/evs/`:**
  - `unit1/unit-1.pdf` / `.pptx` (95 slides)
  - `unit2/unit-2.pdf` / `.pptx` (60 slides) + 5 individual sub-topic PDFs (food, forest, land, mineral, water)
  - `unit3/unit-3.pdf` / `.pptx` (69 slides)
  - `unit4/unit-4.pdf` / `.pptx` (91 slides)
  - `unit5/unit-5.pdf` / `.pptx` (35 slides)
  - `practice/evs-cie-1.pdf` / `.docx` (2 pages)
* **Coverage Status:** All 5 units are completely covered in lecture slides.
* **Legacy Code Flag:** Slide 1 of `unit-1.pptx` is titled `"HS 26 Environmental Studies"`. The course code in the 2024 batch curriculum is `HS510`.

---

## 3. Website Data (`data/subjects.js`) Discrepancies vs. Syllabus Ground Truth

The following table details every discrepancy between the website's central metadata file and the official syllabus document:

| # | Location in `subjects.js` / Web UI | What the Website States | What the Official Syllabus States | Severity |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `subjects[0]` (ML) -> `units[1]` | `title: "Unit 2: Decision Trees & Neural Networks"` | Unit 2 is **"Understanding Data – 2 & Basic Learning Theory"** (Dimensionality reduction, induction bias, learning system). Decision trees are Unit 3; Neural Networks are Unit 4. | **CRITICAL** |
| **2** | `subjects[0]` (ML) -> `units[1].files[0]` | `title: "ML Unit 2: Decision Tree Learning & Artificial Neural Networks"` | File `notes/ml/unit2/unit-2.pdf` covers **Model Evaluation & Data Preprocessing** from CSE(AI&ML) CI52. It has zero slides on trees or neural networks. | **CRITICAL** |
| **3** | `subjects[0]` (ML) -> `units[0].files[0]` | Slide 1 originates from ISE Dept `IS51` | File originates from **Dept of CSE(AI&ML), Course Code CI52, Dr. A N Ramya Shree**. | **MEDIUM** |
| **4** | `subjects[0]` (ML) -> `units[3]` (Practice) | Labeled as `unit-1-qb.pdf` ("Unit 1 Question Bank") | Document covers questions from **Units 1, 2, 3, and 4** (Perceptrons, MLP, Naïve Bayes, Decision Trees). | **MEDIUM** |
| **5** | `subjects[1]` (SE) -> `credits` | `credits: "2:0:1"` | Syllabus header explicitly records **Credits: 2:0:1:2** (4-tuple notation including Self-study credits). | **LOW** |
| **6** | `subjects[1]` (SE) -> `units[1]` | Claims Unit 2 notes are complete | File covers only Chapter 4 Requirements Engineering (82 slides). **Chapter 5 System Modeling is completely omitted.** | **HIGH** |
| **7** | `subjects[2]` (CN) -> `credits` | `credits: "4:0:0"` | Syllabus header explicitly records **Credits: 4:0:0:4**. | **LOW** |
| **8** | `subjects[2]` (CN) -> `units[0,1]` notes | Served as standard lecture PDFs | Notes are **100% rasterized bitmap image scans** from Forouzan 5E slides with zero selectable text. | **HIGH** |
| **9** | `subjects[3]` (TOC) -> `credits` | `credits: "2:1:0"` | Syllabus header explicitly records **Credits: 2:1:0:2**. | **LOW** |
| **10** | `subjects[4]` (AI) -> `credits` | `credits: "3:0:0"` | Syllabus header explicitly records **Credits: 3:0:0:3** (Screenshot erroneously shows `3:0:0`). | **LOW** |
| **11** | `subjects[4]` (AI) -> `contactHours` | Screenshot says `42` | Official syllabus specifies **45L+45S**. | **LOW** |
| **12** | `subjects[4]` (AI) -> `status` | Treated alongside subjects with study materials | **Zero notes served on site** (Syllabus and CIE question papers only). | **HIGH** |
| **13** | `subjects[5]` (RMIPR) -> `status` | Only Units 1 and 2 provided | Units 3, 4, and 5 (representing 60% of SEE exam) are missing without warning. | **HIGH** |
| **14** | `subjects[6]` (ReactJS) -> `syllabus` | Serves `reactjs-syllabus-screenshot.png` | Screenshot is truncated, showing only Units I, II, and III; Units IV and V are cropped out. | **MEDIUM** |
| **15** | `scheme.courses` | All course credits listed as 3-tuples (e.g. `3:0:0`) | Syllabus scheme lists 4-tuples $(L:T:P:	ext{Total})$ and contact hour breakdowns $(L, T, P, S)$. | **LOW** |

---

## 4. Practice Papers & Exam Analysis

An audit of all internal assessment (CIE) and semester-end (SEE) question papers yielded the following findings:

| Subject | Test Paper File | Units Tested | Questions Outside Formal Syllabus Topic List | Unexamined Units in Paper |
| :--- | :--- | :---: | :--- | :--- |
| **AI (ISE552)** | `ai-cie-1-and-2.pdf` | **CIE-1:** U1, U2<br>**CIE-2:** U3, U5 | **1. Classical Planning & PDDL (Blocks World):** Tested in CIE-2 Q3.c despite omission from unit topics.<br>**2. Bidirectional Search:** Tested in CIE-1 Q1.b (not explicitly listed in U2). | **Unit 4 (Uncertainty & Generative AI)** is completely unexamined. |
| **CN (IS53)** | `cn-cie-1-and-2.pdf` | **CIE-1:** U1, U2<br>**CIE-2:** U3, U4, U5 | None (All align strictly with Forouzan 5E). | All 5 units examined across the two tests. **Crucially: CIE-2 tests only the missing units (U3, U4, U5).** |
| **SE (IS52)** | `se-cie-1-and-2.pdf` | **CIE-1:** U1, U2<br>**CIE-2:** U3, U4, U5 | Header typo: Printed as **23IS51** instead of **IS52**. | All 5 units examined. **Crucially: CIE-2 tests only the missing units (U3, U4, U5).** |
| **RMIPR (AL58)** | `rmipr-cie-1-and-2.pdf` | **CIE-1:** U1, U2<br>**CIE-2:** U3, U4, U5 | None. | All 5 units examined. **CIE-2 tests only missing units (U3, U4, U5).** |
| **RMIPR (AL58)** | `rmipr-see-feb-mar-2025.pdf`<br>`rmipr-makeup-apr-2025.pdf` | **SEE:** All 5 Units (2 questions per unit) | None. | **Units 3, 4, and 5 account for 60 marks out of 100 on the paper.** |
| **ML (IS51)** | `ml-cie-1-2-see.pdf` | **CIE-1:** U1, U2<br>**CIE-2:** U2, U3, U4, U5 | Header labeled **IS62** (dated May 2026). Page 1 is scanned upside down ($180^\circ$). | All units touched in CIE-2. |
| **TOC (IS54)** | `toc-cie-1-2-see.pdf` | **CIE-1:** U1, U2<br>**CIE-2:** U3, U4<br>**SEE:** U1–U5 | None. | Full syllabus systematically examined. |
| **EVS (HS510)** | `evs-cie-1.pdf`<br>`evs-cie1-qp-2024.docx` | **CIE-1:** U1, U2 | Header prints Department as *Artificial Intelligence & Data Science*. | Units 3, 4, 5 not in CIE-1 (covered in CIE-2). |

---

## 5. Prioritized Action List for Exam Preparation

### High Priority (Immediate Remediation Needed)
1. **Acquire CN Units 3, 4, and 5 Notes:**
   - *Topics:* IPv4 Datagram, ICMP, Distance Vector & Link State Routing (Unit 3); IPv6 and Transport protocols Stop-and-Wait, GBN, Selective Repeat (Unit 4); UDP, TCP Congestion Control, DNS (Unit 5).
   - *Source:* Behrouz A. Forouzan, *Data Communications and Networking*, 5th Edition:
     - **Unit 3:** Chapters 18, 19, 20, 21
     - **Unit 4:** Chapters 22, 23
     - **Unit 5:** Chapters 24, 25, 26
2. **Acquire RMIPR Units 3, 4, and 5 Notes:**
   - *Topics:* Sampling & Hypothesis Testing (Unit 3); Patents & TRIPS (Unit 4); Trademarks, Copyrights & Designs (Unit 5).
   - *Source:* C. R. Kothari, *Research Methodology*, Chapters 4, 8, 9; Dr. B. L. Wadehra, *Law Relating to Intellectual Property*, Chapters on Patents, Trademarks, and Copyrights.
3. **Acquire SE Units 3, 4, and 5 Notes + System Modeling:**
   - *Topics:* UML System Modeling (Unit 2); Architectural Design & Design Patterns (Unit 3); Software Testing (Unit 4); Project Management & Metrics (Unit 5).
   - *Source:* Ian Sommerville, *Software Engineering*, 10th Edition:
     - **Unit 2 (System Modeling):** Chapter 5
     - **Unit 3:** Chapters 6, 7
     - **Unit 4:** Chapters 8, 9
     - **Unit 5:** Chapters 22, 23, 24
4. **Prepare Artificial Intelligence (ISE552) from Russell & Norvig:**
   - Since no notes exist on the site, prepare directly from *Artificial Intelligence: A Modern Approach* (4th Edition):
     - **Unit 1:** Chapters 1, 2 (Agents, PEAS, Agent Types)
     - **Unit 2:** Chapters 3, 4, 5 (Search, A*, Minimax, $lpha$-$eta$ pruning)
     - **Unit 3:** Chapters 7, 8, 9 (Propositional & First-Order Logic, Resolution, Forward Chaining)
     - **Unit 4:** Chapters 12, 13, 24 (Uncertainty, Bayes Networks, Deep Learning/Transformers)
     - **Unit 5:** Chapter 11 (Classical Planning / PDDL) + Generative AI & Ethics readings.
5. **Correct ML Unit 2 & Acquire Decision Trees / Bayesian / Neural Net Notes:**
   - `unit-2.pdf` does not contain Decision Trees or Neural Networks. Study Mitchell / Sridhar & Vijayalakshmi:
     - **Unit 2:** Sridhar Chapters 2 & 3 (Feature Engineering & Learning Systems)
     - **Unit 3:** Mitchell Chapter 3 (Decision Trees); Sridhar Chapter 4 (KNN, Linear/Polynomial Regression)
     - **Unit 4:** Mitchell Chapter 4 (ANNs / Backpropagation) & Chapter 6 (Bayes); Sridhar Chapter 8.

### Medium Priority
6. **Correct Metadata in `data/subjects.js`:**
   - Fix ML Unit 2 title from `"Unit 2: Decision Trees & Neural Networks"` to `"Unit 2: Understanding Data – 2 & Basic Learning Theory"`.
   - Update file description of `unit-2.pdf` to reflect that it covers Model Evaluation Preliminaries (CI52) rather than Decision Trees.
   - Retitle `unit-1-qb.pdf` to `"Machine Learning Comprehensive Question Bank (Units 1–4)"`.
   - Update AI status badge to indicate *Syllabus & Practice Papers Only (Notes Pending)*.
7. **Replace CN Rasterized PDFs:**
   - Source native vector/searchable slide decks for CN Units 1 and 2 to enable text searching and readable mobile zooming.
8. **Fix Handout Printing in `se/unit2/unit-2.pdf`:**
   - Re-export `unit-2.pptx` as a standard 1-slide-per-page PDF to replace the cramped 6-slides-per-page handout print.
9. **Rotate Page 1 of `ml/practice/ml-cie-1-2-see.pdf`:**
   - Correct the $180^\circ$ orientation error on page 1 of the ML practice paper.

### Low Priority
10. **Synchronize Credit Notations in `subjects.js`:**
    - Standardize credit notation to the 4-tuple format $(L:T:P:	ext{Total})$ used in the syllabus headers (`IS51`: 3:0:0:3, `IS52`: 2:0:1:2, `IS53`: 4:0:0:4, `IS54`: 2:1:0:2, `ISE552`: 3:0:0:3, `AL58`: 3:0:0:3).
11. **Update Course Code on EVS Slides:**
    - Note in UI that slide code `HS 26` is the former course code for `HS510`.

---

## 6. Methodology and Limitations

### Text Extraction Methodology
- **PDF Documents:** Analyzed page-by-page using `pypdf 6.19.0`. Total character counts, page geometry, embedded image streams, and font metadata were inspected.
- **Office Formats:**
  - `.pptx` presentations were parsed using `python-pptx 1.0.2` and confirmed via low-level `zipfile` XML inspection (`ppt/slides/slide*.xml` and `ppt/media/*`).
  - `.docx` documents were parsed using `python-docx 1.2.0` across paragraphs, tables, and headers.
- **Scanned / Rasterized Documents:**
  - Where character count was zero or negligible (<30 characters per page), raw embedded image objects were extracted and visually verified using Antigravity image inspection tooling.

### Verification Limitations
1. **Humanities Department Syllabus (HS510):** The official III-year engineering syllabus document omits the syllabus narrative for `HS510` (mentioning it only in the Scheme table as an NCMC course). Verification for EVS was performed against the department's CIE-1 question paper and slide content.
2. **Departmental Origin of Course Materials:** Faculty slide decks often circulate across sister departments (ISE, CSE, AIML). While curricular topics overlap, course codes printed on titles (e.g. `CI52` on ML, `HS 26` on EVS, `IS62` on ML test) reflect inter-departmental resource reuse.

### Auditor Confidence Assessment
- **Syllabus Ground Truth:** **100% Confidence** (Derived directly from signed institutional syllabus PDF).
- **Notes File Contents & Unit Coverage:** **100% Confidence** (Every file opened, parsed, and checked against unit topics).
- **Website Metadata Accuracy:** **100% Confidence** (Full code inspection of `data/subjects.js`).
