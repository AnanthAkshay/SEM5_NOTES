# Scope Decisions & Ambiguities Log (CIE-1 Rebuild)

**Date**: October 9, 2026  
**Auditor**: Antigravity Assistant for Aki (5th Sem ISE, MSRIT)  
**Status**: Log of all conservative judgement calls and scope boundaries implemented for the CIE-1 Rebuild.

---

## 1. Software Engineering (24IS52) Syllabus Hierarchy

- **Ambiguity**: The repository contains `ISE_III_year_Syllabus_2024_Batch_final.pdf` (which listed Prof. Mushtaq Ahmed D M as coordinator and older textbook editions) and the newly added `IS52 - SE/SE-Syllabus2026-27.docx` (which lists Dr. Krishna Raj RM as coordinator, includes updated Agile topics, specific lab exercises for GitHub Kanban, Product Backlog, and IEEE 830 SRS preparation).
- **Decision Taken**: Adopted `IS52 - SE/SE-Syllabus2026-27.docx` as the authoritative syllabus ground truth for 2026–27.
- **Rationale**: The docx file is explicitly dated 2026–27 for the current academic session. All faculty slide decks in `IS52 - SE/Recent Notes/` (`Unit 1.1.pptx`, `Unit 1.2.pptx`, `Unit 1.3.pptx`, `Unit 2.1.pptx`, `Unit 2.2.pptx`) strictly follow this updated structure.
- **Alternative if Disagreed**: If the earlier 2024 batch syllabus is preferred, restore the Mushtaq Ahmed coordinator header and remove the GitHub Kanban lab mapping from Unit 1.

---

## 2. Machine Learning (24IS51) Unit 3 Scope ("Only the Regression portion")

- **Ambiguity**: The official syllabus lists Unit 3 under two major headings: (1) *Similarity-based Learning* (KNN, Weighted KNN, Nearest Centroid, LWR) followed by *Regression Analysis* (Linear, Multiple, Polynomial, Logistic), and (2) *Decision Tree Learning* (ID3, C4.5, CART). Aki's prompt specified: *"Unit 3 only the Regression portion"*.
- **Decision Taken**: Kept strictly the **Regression Analysis** topics:
  - Simple Linear Regression (OLS closed-form derivations, slope, intercept).
  - Multiple Linear Regression (matrix Normal Equation $\beta = (X^T X)^{-1} X^T Y$).
  - Polynomial Regression (non-linear feature expansion).
  - Evaluation Metrics (MSE, RMSE, MAE, $R^2$, Adjusted $R^2$).
  - Gradient Descent Optimization (Batch, SGD, Mini-batch, learning rate).
  - Regularization: Ridge Regression (L2) and Lasso Regression (L1) with analytical solutions, as taught in faculty slides (`Chapter_5_Regression_Analysis_Detailed.pptx`) and lab problem sets (`Linear & ridge regression....docx`).
  - Logistic Regression (Sigmoid function, Log-odds, Maximum Likelihood Estimation, Cross-entropy loss, decision boundary).
  - **Excluded / Placed on Hold**: Nearest-Neighbor Learning, Weighted KNN, Nearest Centroid, Locally Weighted Regression (LWR), and all Decision Tree Learning (Entropy, Information Gain, Gini index).
- **Rationale**: The prompt explicitly stated: *"Drop similarity-based learning/KNN, decision trees and anything else that Unit 3 contains, unless the syllabus lists it under regression"*.
- **Alternative if Disagreed**: If KNN / Decision Trees are in Aki's teacher's CIE-1 portion, flip `in_scope` for KNN in `data/scope.json` and restore the KNN section in `notes/ml/unit3/unit-3-notes.html`.

---

## 3. Computer Networks (24IS53) Unit 3 Scope ("Up to IPv4 Addressing – Classless")

- **Ambiguity**: Unit 3 in the syllabus lists: *"Network layer: Network layer services, Introduction to connectionless service and connection oriented service, Congestion control, IPV4 Addresses (Address space, classful addressing, classless addressing, and NAT), Internet protocol (IP) datagram format, fragmentation, IP options, ICMP error reporting and query messages, Routing algorithms: Distance Vector Routing, Link State Routing, Multicast Distance Vector (DVMRP)."*
- **Decision Taken**: Kept all topics from the start of Unit 3 through **IPv4 Addressing – Classless** (inclusive):
  - Network layer services, datagram vs virtual circuit, congestion control.
  - IPv4 Addressing: address space, notation, classful addressing (Classes A–E).
  - Classless addressing (CIDR, prefix length `/n`, network/broadcast addresses).
  - Subnetting and Supernetting numericals, variable-length subnet masking (VLSM), block design.
  - **Excluded / Placed on Hold**: NAT (Network Address Translation), IPv4 datagram header format, fragmentation & MTU, IP options, ICMP, and all routing algorithms (Distance Vector, Link State).
- **Rationale**: Boundary guidance specifies *"Up to X means everything listed in the syllabus order up to and including X; nothing after it"*.
- **Alternative if Disagreed**: If NAT or IPv4 Header format is included in CIE-1 by the instructor, append them to Unit 3.

---

## 4. Research Methodology & IPR (24AL58) Unit 3 Scope ("Up to Characteristics of a Good Sample Design")

- **Ambiguity**: Unit 3 in the syllabus covers *Method of Data Collection*, *Sampling Design*, *Measurement and Scaling Techniques*, and *Data Analysis: Testing of Hypotheses* (z-test, t-test, Chi-square, ANOVA). Aki's prompt specified: *"Unit 3 up to 'Characteristics of a Good Sample Design' (inclusive)"*.
- **Decision Taken**:
  - **Included**: Primary and Secondary data collection methods, Sampling fundamentals (Census vs Sample survey, need for sampling, implications of sample design), Steps in sampling design, Criteria of selecting a sampling procedure, Characteristics of a good sample design.
  - **Excluded / Placed on Hold**: Types of sample designs (Stratified, Cluster, Multi-stage), Measurement and scaling techniques (Likert scale, semantic differential), and all Hypothesis Testing (Null/Alt hypothesis, Type I/II errors, z/t/chi-square/ANOVA tests).
- **Rationale**: Strict adherence to the cutoff point specified in the syllabus topic order.
- **Alternative if Disagreed**: If sampling techniques (Probability vs Non-probability sampling) or hypothesis testing were covered in class before CIE-1, restore them from `notes/rmipr/unit3/unit-3-notes.html` hold list.

---

## 5. Question Paper Subject Identification via Internal Text

- **Ambiguity**: Past exam question papers often use reused course codes (e.g., `IS51` was Machine Learning in 2024 batch, but was Software Engineering in the 2022 batch, and was Computer Networks in the 2020 batch!). File names like `IS52 - SE/SEE - PYQ_s/2024.pdf` contain headers with `IS51`.
- **Decision Taken**: Every question paper has been classified strictly by the **Course Name printed in the header table inside the PDF** (e.g., `"Course Name : Software Engineering"` maps to SE, regardless of whether the code printed is `IS51` or `IS52`).
- **Rationale**: MSRIT revised scheme numbers across autonomous cycles (2021, 2022, 2023, 2024 batches), shifting subject codes while retaining the underlying curriculum. Identifying by printed course title prevents question misattribution.

---

## 6. Curated AI Important Questions List

- **Ambiguity**: `ISE552 - AI/Recent Notes/WhatsApp Image 2026-09-07 at 9.11.31 AM.jpeg` contains 9 handwritten/typed questions without year or mark tags.
- **Decision Taken**: Assigned these questions the highest priority tag (`High Priority · Department Question List`) and created explicit exam-standard answers (6M/5M length) mapped to Section 1 of AI notes and in the PYQ answer bank.

---

*All ambiguous boundaries logged and traced to source files.*
