# SEM 5 ISE — CIE-1 Official Scope & Examination Specification

**Examination Period:** Tuesday, 13 October 2026 – Friday, 16 October 2026  
**Institution:** Ramaiah Institute of Technology (MSRIT), Autonomous Scheme  
**Department:** Information Science & Engineering (ISE), 5th Semester (2024 Batch)  
**Evaluation:** Continuous Internal Evaluation - I (CIE-1), 1 Hour per Paper, 30 Marks  
**Baseline Git Tag:** `pre-cie1-scope` (Full 24-unit archive)  
**Active Production Branch:** `cie1-rebuild`  

---

## 1. Authoritative CIE-1 Examination Schedule

| Date & Time | Course Code | Subject Name | Credits | Scope Limits | Solved PYQs | Handwritten PDF |
|---|---|---|---|---|---|---|
| **Tue 13-10-2026, 09:30–10:30** | `24IS53` | **Computer Networks** | 4:0:0 | Unit 1, Unit 2, Unit 3 up to "IPv4 Addressing – Classless" (CIDR/VLSM included; NAT/IPv6/routing out) | 20 in-scope (8 hold) | 74 pages (U1: 34, U2: 24, U3: 16) + 23p PYQ |
| **Tue 13-10-2026, 13:30–14:30** | `24ISAEC594` | **Frontend Dev using React JS** | 1:0:0 | Unit 1, Unit 2 (Full) | 21 in-scope (10 hold) | 51 pages (U1: 26, U2: 25) + 25p PYQ |
| **Wed 14-10-2026, 09:30–10:30** | `24ISE552` | **Artificial Intelligence** | 3:0:0 | Unit 1, Unit 2 (Full) | 22 in-scope (10 hold) | 55 pages (U1: 28, U2: 27) + 26p PYQ |
| **Wed 14-10-2026, 13:30–14:30** | `24IS52` | **Software Engineering** | 2:0:1 | Unit 1, Unit 2 (Full) | 20 in-scope (18 hold) | 44 pages (U1: 27, U2: 17) + 4p PYQ |
| **Thu 15-10-2026, 09:30–10:30** | `24IS51` | **Machine Learning** | 3:0:0 | Unit 1, Unit 2, Unit 3 (Regression portion only; KNN/Decision Trees out) | 20 in-scope (18 hold) | 82 pages (U1: 35, U2: 32, U3: 15) + 4p PYQ |
| **Thu 15-10-2026, 15:00–16:00** | `24AL58` | **Research Methodology & IPR** | 3:0:0 | Unit 1, Unit 2, Unit 3 up to "Characteristics of a Good Sample Design" (IPR & hypothesis testing out) | 23 in-scope (18 hold) | 54 pages (U1: 23, U2: 21, U3: 10) + 25p PYQ |
| **Fri 16-10-2026, 09:30–10:30** | `24HS510` | **Environmental Studies** | 0:0:0 | Unit 1, Unit 2 (Full) | 25 in-scope (15 hold) | 41 pages (U1: 21, U2: 20) + 22p PYQ |
| **Fri 16-10-2026, 13:30–14:30** | `24IS54` | **Theory of Computation** | 2:1:0 | Unit 1, Unit 2 (Full) | 20 in-scope (18 hold) | 44 pages (U1: 17, U2: 27) + 20p PYQ |

---

## 2. Subject-by-Subject In-Scope Breakdown

### 1. Computer Networks (24IS53)
- **In-Scope Units:**
  - **Unit 1:** Data communications components, transmission modes, topologies, LAN/WAN, Circuit vs Packet switching, TCP/IP protocol suite (5 layers, encapsulation), OSI model vs TCP/IP, Physical layer media (Guided & Unguided).
  - **Unit 2:** Data Link layer services, Framing (bit & byte stuffing), Error control, Block codes & Hamming distance, CRC (hardware division, generator polynomials), Checksum calculation, Noiseless channels, Noisy ARQ protocols (Stop-and-Wait, Go-Back-N, Selective Repeat, Piggybacking), MAC protocols (Pure & Slotted ALOHA, CSMA, CSMA/CD, CSMA/CA), Controlled Access, CDMA chip sequences, IEEE 802.3 Ethernet frame and minimum length calculation.
  - **Unit 3 (Truncated):** Network layer services, Packet switching (Datagram vs Virtual Circuit), IPv4 32-bit addresses, Classful addressing, Classless addressing (CIDR prefix length), Subnetting/Supernetting, Hierarchical delegation, and VLSM numerical block design.
- **Out of Scope (Excised from Site):**
  - Unit 3 topics after Classless IPv4: NAT, IPv4 datagram header fields, fragmentation, MTU, ICMP, Routing algorithms (Dijkstra, Bellman-Ford, DVMRP).
  - Units 4 & 5: IPv6, Transport layer (TCP/UDP, congestion control), Application layer (DNS, HTTP).

### 2. Front-end Development using React JS (24ISAEC594)
- **In-Scope Units:**
  - **Unit 1:** React background, core philosophy, SPA architecture, Virtual DOM vs Real DOM, React reconciliation, JSX syntax and compilation, `React.createElement`, React elements vs components, Function vs Class components, Pure components, Props, Prop-drilling, `children` prop, Component composition.
  - **Unit 2:** State management, `useState`, State lifting, Component lifecycle phases, `useEffect` dependencies, Event handling, Synthetic events, Controlled vs Uncontrolled forms, Conditional rendering, List keys, React Fragments, Error boundaries.
- **Out of Scope (Excised from Site):**
  - Unit 3: React Router (v6 `BrowserRouter`, `Routes`, `Route`, `useNavigate`, `useParams`), Context API (`createContext`, `useContext`), Redux / Redux Toolkit, Custom Hooks, Performance optimization (`useMemo`, `useCallback`).

### 3. Artificial Intelligence (24ISE552)
- **In-Scope Units:**
  - **Unit 1:** 4 Historical definitions of AI, Turing Test, Rationality vs Omniscience, PEAS specifications, Environment classification (Observable, Deterministic, Episodic, Static, Discrete, Single-Agent), Agent architectures (Simple reflex, Model-based, Goal-based, Utility-based, Learning), Problem-solving agents, State-space search formulation (Vacuum World, 8-Puzzle, 8-Queens), Faculty 9-question priority list.
  - **Unit 2:** Uninformed search algorithms (BFS, DFS, Uniform-Cost Search, Depth-Limited Search, Iterative Deepening Search, Bidirectional Search), Heuristic search (Greedy Best-First, A* Graph Search, Admissibility and Consistency of heuristics, Dominance), Local search (Hill Climbing, Local Maxima/Plateaus, Simulated Annealing), Adversarial search (Minimax algorithm, Alpha-Beta pruning traces).
- **Out of Scope (Excised from Site):**
  - Unit 3: Knowledge representation, Propositional Logic, First-Order Logic (FOL), Inference, Unification, Resolution theorem proving, Forward and Backward chaining.

### 4. Software Engineering (24IS52)
- **In-Scope Units:**
  - **Unit 1:** Professional software development, Software ethics, Process models (Waterfall, Incremental, Reuse-oriented), Process activities (Specification, Development, Validation, Evolution), Coping with change (Prototyping, Incremental delivery, Boehm's Spiral), Agile development principles, Extreme Programming (XP), Scrum framework (Sprint, Product Backlog, Roles, Ceremonies).
  - **Unit 2:** Requirements Engineering (Functional vs Non-functional requirements, Software Requirements Document IEEE 830, Elicitation and analysis, Validation, Management), System Modeling (Context models, Interaction models / Use case & Sequence diagrams, Structural models / Class diagrams, Behavioral models / State machine diagrams).
- **Out of Scope (Excised from Site):**
  - Unit 3: Architectural Design, Implementation, Software Testing (Component, Integration, System, Acceptance testing).

### 5. Machine Learning (24IS51)
- **In-Scope Units:**
  - **Unit 1:** Well-posed learning problems, Designing a learning system (Checkers game formulation, Target function, Function representation, Estimating training values, Adjusting weights / LMS rule), Concept learning, Find-S algorithm, Version Spaces and Candidate-Elimination algorithm, Inductive Bias.
  - **Unit 2:** Decision tree representation, Appropriate problems for decision tree learning, ID3 algorithm, Entropy and Information Gain calculations, Inductive bias in decision tree learning, Overfitting issues and Reduced-error pruning.
  - **Unit 3 (Regression Portion Only):** Simple Linear Regression (Least Squares Normal Equations derivation, Cost function $J(\theta)$), Multiple Linear Regression, Polynomial Regression, Ridge Regression ($L_2$ regularisation), Lasso Regression ($L_1$ regularisation), Logistic Regression (Sigmoid function, Log-loss / Cross-Entropy, Decision boundary).
- **Out of Scope (Excised from Site):**
  - Unit 3 non-regression topics: Similarity-based learning, $k$-Nearest Neighbors (KNN), Weighted KNN, Curse of dimensionality, Distance metrics.

### 6. Research Methodology & IPR (24AL58)
- **In-Scope Units:**
  - **Unit 1:** Meaning, objectives, motivation, and types of research; Research approaches, Significance, Research methods vs Methodology, Scientific method, Research process (step-by-step), Criteria of good research, Problems encountered by researchers in India.
  - **Unit 2:** Meaning of research problem, Selecting the problem, Necessity of defining the problem, Techniques involved in defining a problem, Meaning of research design, Need for research design, Features of a good design, Important concepts relating to research design, Different research designs (Exploratory, Descriptive, Diagnostic, Hypothesis-testing).
  - **Unit 3 (Sample Design Up to Characteristics):** Census and sample survey, Implications of sample design, Steps in sampling design, Criteria for selecting a sampling procedure, Characteristics of a good sample design.
- **Out of Scope (Excised from Site):**
  - Unit 3 remainder: Different types of sample designs (Probability vs Non-probability sampling), Measurement and scaling techniques, Methods of data collection.
  - Unit 4: Hypothesis testing ($t$-test, $z$-test, ANOVA, Chi-square).
  - Unit 5: Intellectual Property Rights (Patents, Trademarks, Copyrights, Trade Secrets, Infringement).

### 7. Environmental Studies (24HS510)
- **In-Scope Units:**
  - **Unit 1:** Scope & importance of environment, Multidisciplinary nature, Earth's spheres (Atmosphere, Hydrosphere, Lithosphere, Biosphere), Ecosystem concept, Structure and functions of ecosystems, Food chains, Food webs, Ecological pyramids, Energy flow & Lindeman's 10% law, Major ecosystems (Forest, Grassland, Desert, Aquatic), Ecological succession, Biogeochemical cycles (Carbon, Nitrogen, Hydrological), Biodiversity (Genetic, Species, Ecosystem diversity; Hotspots; Threats; Conservation).
  - **Unit 2:** Natural resources: Forest resources (deforestation, timber extraction, mining, dams), Water resources (over-utilization, floods, droughts, conflicts), Mineral resources, Food resources (world food problems, modern agriculture, fertilizer-pesticide issues, water logging, salinity), Land resources (land degradation, soil erosion, desertification).
- **Out of Scope (Excised from Site):**
  - Unit 3: Environmental pollution (Air, Water, Soil, Marine, Noise, Thermal, Nuclear hazards, Solid waste management).
  - Unit 4: Social issues and environment (Water conservation, Rainwater harvesting, Global warming, Acid rain, Ozone depletion, Environmental Protection Acts).
  - Unit 5: Human population and environment.

### 8. Theory of Computation (24IS54)
- **In-Scope Units:**
  - **Unit 1:** Central concepts of Automata Theory (Alphabets $\Sigma$, Strings $\Sigma^*$, Languages $L$), Deterministic Finite Automata (DFA 5-tuple, Transition functions, Language acceptance, State diagram construction), Non-deterministic Finite Automata (NFA 5-tuple), Equivalence of DFA and NFA (Subset construction algorithm with dead state elimination), Finite Automata with $\epsilon$-transitions ($\epsilon$-NFA, $\epsilon$-closure, conversion of $\epsilon$-NFA to DFA), Applications of Finite Automata.
  - **Unit 2:** Regular Expressions (Formal recursive definition, Operators, Precedence, RE formulation), Finite Automata and Regular Expressions (Thompson's construction algorithm), Converting FA to Regular Expression (State elimination method & Arden's theorem), Pumping Lemma for Regular Languages (Proof methodology, Contradiction proofs for $a^n b^n$, $a^p$), Closure properties of Regular Languages (Union, Concatenation, Star, Intersection, Complement, Reversal), Decision properties (Emptiness, Finiteness, Membership), Equivalence and Minimization of Automata (Myhill-Nerode Table-Filling algorithm).
- **Out of Scope (Excised from Site):**
  - Unit 3: Context-Free Grammars (CFGs), Derivations (LM/RM), Parse trees, Ambiguity, Chomsky Normal Form (CNF), Grammar simplifications (Elimination of useless, unit, and $\epsilon$-productions).
  - Unit 4: Pushdown Automata (PDA, Instantaneous descriptions, Acceptance by final state vs empty stack, DPDA vs NPDA, CFG to PDA conversion).
  - Unit 5: Turing Machines (7-tuple formal definition, Instantaneous descriptions, Programming techniques, Subroutines, Multi-tape TMs, Non-deterministic TMs, Halting problem, NP-Hard and NP-Complete overview).

---

## 3. Strict Verification & Integrity Guarantees

1. **Zero Out-of-Scope Content on Served Site:**
   - Every Unit 3 page of 2-unit subjects (React, AI, SE, EVS, TOC) has been excised from `notes/`, `data/subjects.js`, and the search index.
   - For 3-unit subjects with partial limits (CN, ML, RMIPR), Unit 3 notes have been trimmed to the exact syllabus cutoff point.
2. **Recoverability Guarantee:**
   - Baseline repository snapshot is preserved under permanent git tag `pre-cie1-scope`.
   - Out-of-scope faculty reference files and question papers are maintained safely in the repository.
3. **Solved PYQ Bank Integrity:**
   - Over 170 distinct exam questions categorized across CIE, SEE, and Makeup papers.
   - Every in-scope question features an exam-grade model answer with diagrams, worked calculations, and verified textbook citations.
   - Out-of-scope questions are logged in `data/pyq/<subject>.json` under `out_of_scope_questions` with explicit exclusion justifications.
4. **Vector Handwritten Notebooks:**
   - 100% heading coverage across all 19 in-scope units and 8 PYQ banks.
   - Rendered using embeddable open-source vector fonts (Patrick Hand, Caveat, Kalam, JetBrains Mono); zero Type-3 font dependencies.
