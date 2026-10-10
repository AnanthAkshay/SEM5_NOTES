# AI (ISE552) · Recent Notes Audit & Synchronisation Report

**Date:** 2026-10-10  
**Source of Truth:** `A:\SEM 5\ISE552 - AI\Recent Notes` (8 files)  
**Target Subject:** `24ISE552` — Artificial Intelligence  
**Scope Authority:** `data/scope.json` & `notes/ai/syllabus/ai-ise552-syllabus.docx` (CIE-1 Scope: Unit 1 & Unit 2 Full)

---

## 1. Executive Summary & Root Cause Diagnosis

### Symptom:
On the live site under `Artificial Intelligence (24ISE552)`, Unit 1 displayed **zero** Recent Notes files, and Unit 2 displayed only a single file (`ai-adversarial-search.pdf`). The student's latest lecture decks for Introduction to AI, Problem-Solving Agents, Uninformed Search, Informed Search, Local Search, and the 9-question classroom board scan were absent from the active unit views.

### Root Cause Analysis:
1. **Mislocated Files During Previous Sync:** When older faculty slides were archived, 6 of the student's recent files had previously been stored under `notes/ai/unit1/` and `notes/ai/unit2/` with legacy filenames (`unit1_ai-intro-intelligent-agents.pdf`, `unit2_ai-uninformed-search.pdf`, etc.). Because they were not inside `notes/ai/recent-notes/`, the sync script classified them as old faculty slides and quarantined them into `archive/removed-from-site/ai/`.
2. **Authoritative PC Folder Was Unsynced:** The authoritative folder `A:\SEM 5\ISE552 - AI\Recent Notes` contains all 8 files with identical timestamps (`09-10-2026 22:01`).
3. **No Stale Hashes or Corrupt Files:** All files on disk are 100% valid and verified via SHA-256 against the source folder.

---

## 2. File-by-File Status Matrix

| Source Filename | Size | SHA-256 (prefix) | Current Repo State | Diagnosis Status | Assigned Unit | Clean URL-Safe Target Name |
|---|---|---|---|---|---|---|
| `AI-2.pdf` | 1,701,680 B | `da9833ba8541` | Quarantined in archive | In repo archive, not registered | **Unit 1** | `notes/ai/recent-notes/ai-intelligent-agents-intro.pdf` |
| `WhatsApp Image 2026-09-07...jpeg` | 38,050 B | `84f2f3a9cf1b` | In `practice/` only | In repo, missing from recent-notes | **Unit 1** | `notes/ai/recent-notes/ai-important-questions.jpg` |
| `AI-Intelligent_Agents.pdf` | 418,510 B | `9fab6beb0704` | Quarantined in archive | In repo archive, not registered | **Unit 2** | `notes/ai/recent-notes/ai-problem-solving-agents.pdf` |
| `AI-Intelligent_Agents-PS.pdf` | 419,163 B | `eb90bc473710` | Quarantined in archive | In repo archive, not registered | **Unit 2** | `notes/ai/recent-notes/ai-problem-solving-agents-ps.pdf` |
| `AI-AGENTS-Uninformed_Search.pdf` | 174,456 B | `b38e69e199cc` | Quarantined in archive | In repo archive, not registered | **Unit 2** | `notes/ai/recent-notes/ai-uninformed-search.pdf` |
| `AI-Informed_Search.pdf` | 177,846 B | `ec144ec40860` | Quarantined in archive | In repo archive, not registered | **Unit 2** | `notes/ai/recent-notes/ai-informed-search.pdf` |
| `AI-Local_Search.pdf` | 174,371 B | `f9ad028ea466` | Quarantined in archive | In repo archive, not registered | **Unit 2** | `notes/ai/recent-notes/ai-local-search.pdf` |
| `AI-Adversarial_Search.pdf` | 194,418 B | `558783e9d1ca` | Active in `recent-notes/` | In repo & registered correctly | **Unit 2** | `notes/ai/recent-notes/ai-adversarial-search.pdf` |

---

## 3. PDF Page-by-Page Inspection & Content Breakdown

Every PDF was rendered and examined page-by-page using `pypdfium2` and `pypdf`:

1. **`AI-2.pdf` (39 Pages):**
   - *Title:* Artificial Intelligence — Introduction & Intelligent Agents
   - *Content:*
     - Chapter 1: Introduction to AI, Definition, 4 Approaches (Acting Humanly, Thinking Humanly, Thinking Rationally, Acting Rationally).
     - Chapter 2: Agents & Environments, Sensors & Actuators, Rationality, PEAS representation, Environment classifications (Observable, Deterministic, Episodic, Static, Discrete, Single/Multi-Agent).
     - Structure of Agents: Simple Reflex, Model-Based Reflex, Goal-Based, Utility-Based, Learning Agents.
     - Chapter 3.1: Intro to Problem-Solving Agents.
   - *Unit Alignment:* **Unit 1: Introduction to Artificial Intelligence & Intelligent Agents**.

2. **`WhatsApp Image 2026-09-07 at 9.11.31 AM.jpeg` (Image):**
   - *Title:* Classroom Board Curated List of 9 Core Questions.
   - *Questions Listed:*
     1. What is Artificial Intelligence?
     2. What are the types of AI?
     3. What is the difference between AI, ML, and Deep Learning?
     4. What are the applications of AI?
     5. What is an intelligent agent?
     6. What are sensors and actuators?
     7. What is a rational agent?
     8. What are the different types of intelligent agents?
     9. What is the difference between supervised and unsupervised learning?
   - *Unit Alignment:* **Unit 1 Recent Notes**.
   - *Status in Site:* All 9 questions are fully solved in `notes/ai/pyq/pyq-answers.html` (Questions 1–9) and in `notes/ai/unit1/unit-1-notes.html`.

3. **`AI-Intelligent_Agents.pdf` (15 Pages):**
   - *Title:* Problem-Solving Agents — Problem Formulation & State-Space Representation.
   - *Content:*
     - 5 Components of Well-Defined Problems: Initial State, Actions, Transition Model, Goal Test, Path Cost.
     - Bengaluru → Hyderabad route-finding state space representation.
     - State space, path, and solution concepts.
   - *Unit Alignment:* **Unit 2: Problem-Solving Agents & Search Strategies** (Topic 1).

4. **`AI-Intelligent_Agents-PS.pdf` (16 Pages):**
   - *Title:* Problem-Solving Agents (Problem Set & Formulation Variant).
   - *Comparison:* Contains the exact same 15 content slides as `AI-Intelligent_Agents.pdf` plus a 16th trailing blank slide.
   - *Unit Alignment:* **Unit 2 Recent Notes** (labeled as Problem Set variant).

5. **`AI-AGENTS-Uninformed_Search.pdf` (15 Pages):**
   - *Title:* Uninformed Search Strategies (Blind Search).
   - *Content:* Breadth-First Search (BFS), Uniform-Cost Search (UCS), Depth-First Search (DFS), Depth-Limited Search (DLS), Iterative Deepening Search (IDS).
   - *Evaluation Criteria:* Completeness, Time Complexity, Space Complexity, Optimality.
   - *Unit Alignment:* **Unit 2: Problem-Solving Agents & Search Strategies** (Topic 2).

6. **`AI-Informed_Search.pdf` (19 Pages):**
   - *Title:* Informed (Heuristic) Search Strategies.
   - *Content:* Heuristic function $h(n)$, Greedy Best-First Search, A* Search ($f(n) = g(n) + h(n)$), Admissible heuristics, Consistent (monotonic) heuristics, 8-puzzle numerical heuristic evaluations.
   - *Unit Alignment:* **Unit 2: Problem-Solving Agents & Search Strategies** (Topic 3).

7. **`AI-Local_Search.pdf` (19 Pages):**
   - *Title:* Local Search Algorithms & Optimization.
   - *Content:* State-space optimization landscape, Hill-Climbing Search (Greedy local search), Failure modes (Local Maxima, Ridges, Plateaux), Stochastic / Random-Restart Hill Climbing, Simulated Annealing.
   - *Unit Alignment:* **Unit 2: Problem-Solving Agents & Search Strategies** (Topic 4).

8. **`AI-Adversarial_Search.pdf` (19 Pages):**
   - *Title:* Adversarial Search & Game Playing.
   - *Content:* Two-player zero-sum deterministic games, Minimax algorithm, Minimax value computation, Alpha-Beta Pruning, Alpha cut-offs, Beta cut-offs.
   - *Unit Alignment:* **Unit 2: Problem-Solving Agents & Search Strategies** (Topic 5).

---

## 4. Syllabus & CIE-1 Scope Verification

Per the official MSRIT ISE552 syllabus (`notes/ai/syllabus/ai-ise552-syllabus.docx`):
- **Unit 1:** Introduction to AI, Foundations, Types of AI, Applications, Intelligent Agents, Environments, PEAS, Types of Agents.
  - *Files Assigned:* `ai-intelligent-agents-intro.pdf`, `ai-important-questions.jpg`.
- **Unit 2:** Problem-Solving Agents, Problem formulation, Uninformed Search (BFS, DFS, UCS, DLS, IDS), Informed Search (Greedy, A*), Local Search (Hill Climbing, Simulated Annealing), Adversarial Search (Minimax, Alpha-Beta Pruning).
  - *Files Assigned:* `ai-problem-solving-agents.pdf`, `ai-problem-solving-agents-ps.pdf`, `ai-uninformed-search.pdf`, `ai-informed-search.pdf`, `ai-local-search.pdf`, `ai-adversarial-search.pdf`.
- **Unit 3 (Knowledge-Based Agents & Logic), Unit 4 (Uncertainty & GenAI), Unit 5 (Prompt Engineering & Ethics):**
  - Held out-of-scope for CIE-1 per `data/scope.json`.
  - None of the 8 recent files cover Unit 3, 4, or 5 topics. Therefore, **all 8 files are 100% in-scope for CIE-1**.

---

## 5. Site Architecture After Synchronisation

Every unit under the **Notes & Docs** tab for AI will strictly display:
```text
Unit 1: Introduction to Artificial Intelligence & Intelligent Agents (4 files)
  1. Unit 1: Interactive Notes (HTML)
  2. Handwritten notebook (PDF)
  3. Introduction to AI & Intelligent Agents Lecture Presentation (Recent Notes PDF)
  4. Important Questions Board Photo - 9 Core Questions (Recent Notes Image)

Unit 2: Problem-Solving, Search Algorithms & Game Playing (8 files)
  1. Unit 2: Interactive Notes (HTML)
  2. Handwritten notebook (PDF)
  3. Problem-Solving Agents & State-Space Formulation (Recent Notes PDF)
  4. Problem-Solving Agents - Problem Set (Recent Notes PDF)
  5. Uninformed Search Strategies - BFS, DFS, UCS, DLS, IDS (Recent Notes PDF)
  6. Informed Search Strategies - Heuristics, Greedy & A* (Recent Notes PDF)
  7. Local Search Algorithms - Hill Climbing & Simulated Annealing (Recent Notes PDF)
  8. Adversarial Search & Game Playing - Minimax & Alpha-Beta (Recent Notes PDF)
```

All 7 other subjects remain 100% untouched and byte-identical.
