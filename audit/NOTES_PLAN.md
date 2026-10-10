# Master Plan & Implementation Progress: Semester V Interactive HTML Study Notes

**Target:** High-yield, exam-focused, beautifully styled interactive HTML study notes for Units 1, 2, and 3 across all 8 Semester V subjects.  
**Design System:** Hope Rise Warm Editorial Theme (Cream `--bg: #F6E9CF`, soft surface `--surface: #FFFFFF`, green accent `--green: #2EC36B`, typography: Bricolage Grotesque + Inter + JetBrains Mono, pill shapes, zero gradients/glassmorphism).  
**Offline & Self-Contained:** Self-hosted KaTeX in `assets/katex/`, inline handcrafted SVGs for all diagrams, clean semantic HTML, full light/dark theme synchronization, print-ready stylesheets, and site search integration.

---

## 1. Subjects & Units Scope Checklist

- [ ] **Shared Infrastructure & Core Assets**
  - [x] Self-host KaTeX in `assets/katex/`
  - [ ] Shared Stylesheet `css/notes.css`
  - [ ] Shared Interactive Script `js/notes.js`

- [ ] **1. Machine Learning (IS51)**
  - [x] **Unit 1 (PILOT):** Introduction & Understanding Data – 1 (`notes/ml/unit1/unit-1-notes.html`)
  - [x] **Unit 2:** Understanding Data – 2 & Basic Learning Theory (`notes/ml/unit2/unit-2-notes.html`)
  - [x] **Unit 3:** Similarity-based Learning, Regression & Decision Trees (`notes/ml/unit3/unit-3-notes.html`)

- [ ] **2. Theory of Computation (IS54)**
  - [x] **Unit 1:** Finite Automata & Regular Expressions (`notes/toc/unit1/unit-1-notes.html`)
  - [ ] **Unit 2:** Regular Languages, Properties & Minimization (`notes/toc/unit2/unit-2-notes.html`)
  - [ ] **Unit 3:** Context-Free Grammars & Pushdown Automata (`notes/toc/unit3/unit-3-notes.html`)

- [ ] **3. Computer Networks (IS53)**
  - [ ] **Unit 1:** Data Communication Fundamentals & Physical Layer (`notes/cn/unit1/unit-1-notes.html`)
  - [ ] **Unit 2:** Data Link Layer, Error Control & MAC (`notes/cn/unit2/unit-2-notes.html`)
  - [ ] **Unit 3:** Network Layer Services, IPv4 & Routing (`notes/cn/unit3/unit-3-notes.html`)

- [ ] **4. Artificial Intelligence (ISE552)**
  - [ ] **Unit 1:** Introduction to AI, Intelligent Agents & Search (`notes/ai/unit1/unit-1-notes.html`)
  - [ ] **Unit 2:** Uninformed, Informed & Local Search (`notes/ai/unit2/unit-2-notes.html`)
  - [ ] **Unit 3:** Adversarial Search (Games) & Constraint Satisfaction (`notes/ai/unit3/unit-3-notes.html`)

- [ ] **5. Software Engineering (IS52)**
  - [ ] **Unit 1:** Professional Software Development, Processes & Agile (`notes/se/unit1/unit-1-notes.html`)
  - [ ] **Unit 2:** Requirements Engineering & System Modeling (`notes/se/unit2/unit-2-notes.html`)
  - [ ] **Unit 3:** Architectural Design & Object-Oriented Design (`notes/se/unit3/unit-3-notes.html`)

- [ ] **6. Research Methodology & IPR (AL58)**
  - [ ] **Unit 1:** Introduction to Research, Ethics & Literature Review (`notes/rmipr/unit1/unit-1-notes.html`)
  - [ ] **Unit 2:** Research Design, Experimental Design & Sampling (`notes/rmipr/unit2/unit-2-notes.html`)
  - [ ] **Unit 3:** Data Collection, Measurement & Hypothesis Testing (`notes/rmipr/unit3/unit-3-notes.html`)

- [ ] **7. Environmental Studies (HS510)**
  - [ ] **Unit 1:** Environment, Ecosystems & Ecological Succession (`notes/evs/unit1/unit-1-notes.html`)
  - [ ] **Unit 2:** Natural Resources, Energy & Conservation (`notes/evs/unit2/unit-2-notes.html`)
  - [ ] **Unit 3:** Biodiversity, Threats & Conservation Strategies (`notes/evs/unit3/unit-3-notes.html`)

- [ ] **8. Front End Development using ReactJS (ISAEC594)**
  - [ ] **Unit 1:** Introduction to React, Vite & JSX (`notes/reactjs/unit1/unit-1-notes.html`)
  - [ ] **Unit 2:** Components, Props, State & Lifecycle (`notes/reactjs/unit2/unit-2-notes.html`)
  - [ ] **Unit 3:** Events, Forms & Lifting State Up (`notes/reactjs/unit3/unit-3-notes.html`)

- [ ] **Website Integration & Documentation**
  - [ ] Update `data/subjects.js` with all 24 interactive HTML notes entries
  - [ ] Generate compact search index `data/notes-index.json` and integrate with modal search
  - [ ] Update subject cards hash chips & status labels (AI and ReactJS no longer 'syllabus only')
  - [ ] Update `README.md` with complete documentation of the interactive study notes architecture

---

## 2. Topic Breakdown by Course and Unit

### 1. Machine Learning (IS51)
* **Unit 1: Introduction & Understanding Data – 1**
  1. Need for Machine Learning, Machine Learning Explained (Tom Mitchell's formal definition: Task $T$, Performance $P$, Experience $E$)
  2. Machine Learning in Relation to Other Fields (AI, Statistics, Data Mining, Pattern Recognition, Cognitive Science)
  3. Types of Machine Learning (Supervised Learning, Unsupervised Learning, Semi-Supervised Learning, Reinforcement Learning)
  4. Challenges of Machine Learning (Insufficient Training Data, Poor Data Quality, Non-representative Data, Overfitting, Underfitting, Curse of Dimensionality)
  5. Machine Learning Process Lifecycle (Problem Formulation, Data Collection, Data Preprocessing & Cleaning, Feature Engineering, Model Training, Model Evaluation, Model Deployment & Monitoring)
  6. Machine Learning Applications (Computer Vision, Natural Language Processing, Healthcare & Medical Diagnosis, Financial Fraud Detection, Recommendation Systems, Autonomous Vehicles)
  7. Big Data Analysis Framework (The 5 Vs: Volume, Velocity, Variety, Veracity, Value; Distributed Frameworks: Hadoop MapReduce, Apache Spark)
  8. Descriptive Statistics (Measures of Central Tendency: Mean, Median, Mode; Measures of Dispersion: Range, Variance $\sigma^2$, Standard Deviation $\sigma$, Interquartile Range $IQR$)
  9. Univariate Data Analysis and Visualization (Frequency Tables, Histograms, Box Plots & 5-Number Summary, Q-Q Plots, Kernel Density Estimation)
  10. Bivariate and Multivariate Data (Scatter Plots, Contingency Tables, Heatmaps, Pair Plots, Multivariate Relationships)
  11. Multivariate Statistics (Covariance Matrix $\Sigma$, Pearson's Correlation Coefficient $r$, Spearman Rank Correlation, Feature Normalization: Min-Max Scaling vs Z-Score Standardization)
  * **Solved Numericals:**
    - Manual computation of Mean, Median, Mode, Variance, Standard Deviation, and IQR for a discrete dataset.
    - Min-Max normalization ($[0, 1]$ and $[-1, 1]$) and Z-score standardization for given data samples.
    - Pearson correlation coefficient $r$ calculation step-by-step between two feature variables.

* **Unit 2: Understanding Data – 2 & Basic Learning Theory**
  1. Mathematics for Multivariate Data (Vectors, Matrices, Linear Transformations, Dot Product, Matrix Decomposition, Eigenvalues & Eigenvectors, Covariance Matrices)
  2. Feature Engineering (Feature Selection: Filter methods, Wrapper methods, Embedded methods; Feature Extraction; Handling Missing Values, Imputation, One-Hot Encoding, Binning)
  3. Dimensionality Reduction Techniques (The Curse of Dimensionality, Principal Component Analysis [PCA] derivation and step-by-step procedure, Singular Value Decomposition [SVD] intuition, Linear Discriminant Analysis [LDA] overview)
  4. Design of a Learning System (Choosing Training Experience, Choosing Target Function, Choosing Representation for the Target Function, Choosing Learning Algorithm - Mitchell's Checkers Player Case Study)
  5. Introduction to Concept Learning (General-to-Specific Ordering of Hypotheses, Hypothesis Representation)
  6. Find-S Algorithm (Finding maximally specific hypothesis, Algorithmic steps, Limitations of Find-S)
  7. Candidate Elimination Algorithm & Version Spaces (Definition of Version Space, $G$-Set [General Boundary], $S$-Set [Specific Boundary], Boundary update rules for positive and negative training examples)
  8. Inductive Biases (Need for Inductive Bias, Fundamental assumption of inductive learning, The Unbiased Learner Fallacy)
  9. Modeling in Machine Learning & Learning Frameworks (Empirical Risk Minimization [ERM], Structural Risk Minimization, Probably Approximately Correct [PAC] Learning framework, Vapnik-Chervonenkis [VC] Dimension intuition)
  * **Solved Numericals:**
    - PCA step-by-step on 2D data: Centering, Covariance matrix calculation, Eigenvalues/Eigenvectors, Principal component projection.
    - Find-S manual trace on an EnjoySport weather attribute dataset.
    - Candidate Elimination trace showing $S$-set and $G$-set state transitions across positive and negative instances.

* **Unit 3: Similarity-based Learning, Regression Analysis & Decision Trees**
  1. Nearest-Neighbor Learning (Instance-based / Lazy learning paradigm, 1-Nearest Neighbor, K-Nearest Neighbors [KNN] classification, Distance metrics: Euclidean, Manhattan, Minkowski, Cosine distance)
  2. Weighted K-Nearest-Neighbor Algorithm (Distance-weighted voting functions $w_i = 1 / d(x_q, x_i)^2$, Shepard's method)
  3. Nearest Centroid Classifier (Rocchio classification, Prototype calculation, Linear decision boundaries, Comparison with KNN)
  4. Locally Weighted Regression (LWR: Non-parametric regression, Kernel weighting function, Lowess intuition)
  5. Introduction to Regression Analysis (Regression vs Classification, Dependent vs Independent variables)
  6. Simple Linear Regression (Ordinary Least Squares [OLS] derivation, Loss function / Mean Squared Error, Closed-form solutions for slope $m$ and intercept $c$, Gradient descent optimization)
  7. Multiple Linear Regression (Vector formulation, Normal equation $(X^T X)^{-1} X^T y$, Multicollinearity, $R^2$ coefficient of determination vs Adjusted $R^2$)
  8. Polynomial Regression (Fitting non-linear curves, Degree selection, Bias-Variance tradeoff, Overfitting detection)
  9. Logistic Regression (Sigmoid activation function $\sigma(z)$, Odds ratio and Logit, Binary Cross-Entropy / Log Loss, Decision boundary derivation)
  10. Decision Tree Learning Model (Tree architecture: Root, Internal decision nodes, Leaf classifications; Inductive bias: Occam's Razor)
  11. Decision Tree Induction Algorithms (ID3, C4.5, CART; Information Theory: Shannon Entropy $H(S)$, Information Gain $IG(S, A)$, Split Information and Gain Ratio, Gini Impurity, Pre-pruning and Post-pruning)
  * **Solved Numericals:**
    - KNN classification with $k=3$ and distance-weighted voting on a 2D coordinate dataset.
    - Manual Ordinary Least Squares calculation (Slope $m$, Intercept $c$, $R^2$) on a sample dataset.
    - ID3 Decision Tree root node selection: Step-by-step Entropy and Information Gain calculation across all features.

---

### 2. Theory of Computation (IS54)
* **Unit 1: Finite Automata & Regular Expressions**
  - Central concepts of automata theory (Alphabet $\Sigma$, Strings $\Sigma^*$, Languages $L$, Empty string $\epsilon$).
  - Deterministic Finite Automata (DFA): 5-tuple formal definition $(Q, \Sigma, \delta, q_0, F)$, transition table, state diagram, extended transition function $\hat{\delta}$, language accepted $L(M)$.
  - Nondeterministic Finite Automata (NFA): Formal definition, transition function $\delta: Q \times \Sigma \to 2^Q$, language acceptance.
  - $\epsilon$-NFA: $\epsilon$-transitions, $\epsilon$-closure computation.
  - Equivalence of DFA and NFA: Subset Construction Algorithm (Power set construction).
  - Conversion of $\epsilon$-NFA to DFA.
  - Applications of finite automata (Lexical analyzers, grep/regex search engines).
  * **Designs & Numericals:**
    - DFA design for specific languages (e.g. strings ending in 01, binary numbers divisible by 3, even number of 0s and 1s).
    - NFA to DFA subset construction table with dead/trap state handling.
    - $\epsilon$-closure computation and $\epsilon$-NFA to DFA step-by-step transformation.

* **Unit 2: Regular Languages, Properties & Minimization**
  - Regular Expressions (RE): Formal recursive definition, operator precedence, algebraic laws.
  - Equivalence of RE and Finite Automata: Thompson's Construction ($\epsilon$-NFA from RE).
  - Finite Automata to Regular Expressions: State Elimination Method and Arden's Theorem ($R = Q + RP \implies R = QP^*$).
  - Pumping Lemma for Regular Languages: Formal theorem statement, adversarial game formulation ($w = xyz$, $|xy| \le n$, $|y| \ge 1$), proofs of non-regularity ($a^n b^n$, $ww^R$, $0^{n^2}$, palindromes).
  - Closure Properties of Regular Languages: Union, Intersection, Complement, Concatenation, Kleene Star, Reversal, Difference.
  - Decision Properties of Regular Languages: Emptiness, Finiteness, Membership, Equivalence.
  - Minimization of DFA: Myhill-Nerode theorem, Table-Filling Algorithm (Marking method) step-by-step.
  * **Designs & Numericals:**
    - Thompson's construction of $\epsilon$-NFA from a given regular expression.
    - State elimination method to extract RE from DFA.
    - Pumping Lemma step-by-step contradiction proofs.
    - DFA minimization table-filling worked example with before-and-after state transition diagrams.

* **Unit 3: Context-Free Grammars & Pushdown Automata**
  - Context-Free Grammars (CFG): 4-tuple formal definition $(V, T, P, S)$, productions, language of a grammar $L(G)$.
  - Derivations: Leftmost Derivation (LMD), Rightmost Derivation (RMD), Sentential forms.
  - Parse Trees: Tree construction, yield of a parse tree, relationship between derivations and parse trees.
  - Ambiguity in Grammars and Languages: Ambiguous grammars, Disambiguation techniques (Operator precedence and associativity, If-then-else dangling else), Inherent ambiguity.
  - Simplification of CFGs: Elimination of Useless symbols (Generating and Reachable symbols), Elimination of Null ($\epsilon$) productions, Elimination of Unit productions ($A \to B$).
  - Chomsky Normal Form (CNF): Definition ($A \to BC$ or $A \to a$), 4-step conversion procedure from arbitrary CFG. Greibach Normal Form (GNF) basics.
  - Pushdown Automata (PDA): 7-tuple formal definition $(Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$, Instantaneous Descriptions (IDs), Acceptance by final state $L(M)$ vs acceptance by empty stack $N(M)$, Equivalence of acceptance methods.
  - Deterministic PDA (DPDA) vs Nondeterministic PDA (NPDA).
  * **Designs & Numericals:**
    - LMD, RMD, and Parse tree construction for arithmetic expressions.
    - Disambiguation and proof of ambiguity for a sample grammar.
    - Complete step-by-step CNF conversion of a CFG.
    - PDA design with transition table and instantaneous description trace for $L = \{a^n b^n \mid n \ge 1\}$ and $L = \{w c w^R \mid w \in \{0, 1\}^*\}$.

---

### 3. Computer Networks (IS53)
* **Unit 1: Data Communication Fundamentals & Physical Layer**
  - Data communication components (Message, Sender, Receiver, Transmission Medium, Protocol), Network criteria, Physical topologies (Mesh, Star, Bus, Ring, Hybrid).
  - Network categories: LAN, MAN, WAN, Internetwork (The Internet).
  - Protocol Layering principles, TCP/IP 5-layer suite, OSI 7-layer reference model (Physical, Data Link, Network, Transport, Session, Presentation, Application) with detailed duties of each layer.
  - Physical Layer: Data and Signals (Analog vs Digital signals), Periodic analog signals (Amplitude, Frequency, Period, Phase, Wavelength), Time vs Frequency domain representation.
  - Bandwidth of signals, Digital signals (Bit rate, Bit duration, Baseband vs Broadband transmission).
  - Transmission Impairments: Attenuation, Distortion, Noise (Thermal, Induced, Crosstalk, Impulse), Signal-to-Noise Ratio (SNR and $SNR_{dB}$).
  - Data Rate Limits: Nyquist Bit Rate for noiseless channels ($C = 2B \log_2 L$), Shannon Capacity formula for noisy channels ($C = B \log_2(1 + \text{SNR})$).
  - Line Coding Schemes: Digital-to-Digital conversion, Line coding properties (DC component, Self-synchronization), Unipolar (NRZ), Polar (NRZ-L, NRZ-I, RZ, Manchester, Differential Manchester), Bipolar (AMI, Pseudoternary).
  * **Solved Numericals:**
    - Signal attenuation calculations in decibels ($dB = 10 \log_{10}(P_2 / P_1)$).
    - Nyquist max data rate calculation for multi-level signal channels.
    - Shannon channel capacity and SNR requirements calculation.
    - Waveform sketch generation for a given binary bit stream across all line coding schemes.

* **Unit 2: Data Link Layer, Error Control & MAC**
  - Data Link Layer duties and framing methods, Types of addresses (Unicast, Multicast, Broadcast).
  - Address Resolution Protocol (ARP): ARP request/reply, packet format, ARP cache operation, ARP spoofing attacks.
  - Error Detection and Correction: Types of errors (Single-bit vs Burst errors), Redundancy concept, Detection vs Correction.
  - Block Coding: Hamming distance $d(x, y)$, Minimum Hamming distance $d_{min}$, Conditions for error detection ($d_{min} \ge s + 1$) and correction ($d_{min} \ge 2t + 1$).
  - Cyclic Codes & Cyclic Redundancy Check (CRC): Polynomial representation of codes, CRC generator polynomial criteria, CRC hardware & binary long division at sender and receiver.
  - Internet Checksum: 16-bit one's complement addition, Sender checksum generation, Receiver verification.
  - Data Link Control: Framing (Byte stuffing with ESC flags, Bit stuffing with `01111110` delimiter).
  - Media Access Control (MAC): Random Access Protocols (Pure ALOHA, Slotted ALOHA, CSMA, CSMA/CD with binary exponential backoff algorithm, CSMA/CA with IFS and contention window).
  - Controlled Access Protocols: Reservation, Polling, Token Passing.
  - Channelization: FDMA, TDMA, CDMA (Orthogonal Walsh codes, chip sequences).
  * **Solved Numericals:**
    - Complete CRC polynomial division at sender (generating codeword) and receiver (verifying with no remainder).
    - Internet Checksum step-by-step computation for multiple 16-bit words.
    - Bit stuffing and byte stuffing trace on given data streams.
    - ALOHA maximum throughput calculation ($S = G e^{-2G}$ vs $S = G e^{-G}$).
    - CSMA/CD minimum frame size calculation given cable length and propagation speed ($L_{min} = 2 \times t_{prop} \times \text{Bandwidth}$).

* **Unit 3: Network Layer Services, IPv4 & Routing**
  - Network Layer services: Packetizing, Routing, Forwarding. Connectionless service (Datagram networks) vs Connection-oriented service (Virtual-circuit networks).
  - Network Performance Metrics: Transmission delay, Propagation delay, Queuing delay, Processing delay, Bandwidth-Delay Product (BDP).
  - Congestion Control: Congestion symptoms, Open-loop control (Leaky bucket, Token bucket), Closed-loop control (Choke packets, Backpressure).
  - IPv4 Addressing: Address space ($2^{32}$), Classful addressing (Class A, B, C, D, E boundaries, Default masks, NetID/HostID), Subnetting & Supernetting.
  - Classless Addressing (CIDR): Slash notation (/n), Prefix length, Subnet mask calculation, Finding First Address (Network address), Last Address (Broadcast address), and number of valid hosts.
  - Variable Length Subnet Masking (VLSM) hierarchical design.
  - Network Address Translation (NAT): NAT operation, Private IP address blocks (RFC 1918), NAT translation table, NAPT / Port forwarding.
  - IPv4 Datagram Header: Structure and all 14 fields (Version, IHL, TOS/DSCP, Total Length, Identification, Flags [DF, MF], Fragment Offset, TTL, Protocol, Header Checksum, Source & Destination IP, Options).
  - Datagram Fragmentation and Reassembly algorithm.
  - ICMPv4: Message types, Error-reporting messages (Destination unreachable, Time exceeded, Parameter problem, Source quench, Redirection), Query messages (Echo request/reply, Timestamp).
  - Routing Algorithms: Graph abstraction, Distance Vector Routing (Bellman-Ford algorithm, Routing table exchanges, Count-to-infinity problem, Split horizon, Poison reverse).
  - Link State Routing: Dijkstra's Shortest Path algorithm, Link state advertisement (LSA) flooding, Shortest Path First (SPF) tree construction.
  - Multicast Routing: Multicast Distance Vector Routing (DVMRP basics).
  * **Solved Numericals:**
    - CIDR block analysis (Given an IP and CIDR prefix, determine Network address, Directed broadcast address, First host, Last host, and Total assignable hosts).
    - VLSM design for an enterprise with 4 departments requiring 120, 60, 30, and 10 hosts.
    - IPv4 Fragmentation problem (Given a 4000-byte datagram and MTU of 1500 bytes, compute fragment lengths, DF/MF flags, and fragment offsets).
    - Dijkstra's Algorithm step-by-step table trace for shortest path routing tree.

---

### 4. Artificial Intelligence (ISE552)
* **Unit 1: Introduction to AI, Intelligent Agents & Search**
  - Definitions of AI: Thinking Humanly (Cognitive modeling), Acting Humanly (Turing Test approach), Thinking Rationally (Laws of Thought / Logic), Acting Rationally (Rational Agent approach).
  - Foundations of AI: Philosophy, Mathematics, Economics, Neuroscience, Psychology, Computer Engineering, Control Theory, Linguistics.
  - Intelligent Agents: Agent and Environment, Percept sequence, Agent function $f: P^* \to A$, Agent program.
  - Concept of Rationality: Performance measure, Omniscience vs Rationality, Information gathering, Autonomy.
  - Nature of Environments: PEAS Specification (Performance measure, Environment, Actuators, Sensors).
  - Environment Classifications: Fully observable vs Partially observable, Single-agent vs Multi-agent (Competitive vs Cooperative), Deterministic vs Stochastic, Episodic vs Sequential, Static vs Dynamic, Discrete vs Continuous, Known vs Unknown.
  - Agent Architectures: Simple reflex agents, Model-based reflex agents, Goal-based agents, Utility-based agents, Learning agents.
  - Problem Solving by Search: Problem-solving agents, Well-defined problems and solutions (Initial state, Actions $Actions(s)$, Transition model $Result(s, a)$, Goal test, Path cost $c(s, a, s')$), Formulating problems.
  - State Space Formulation for Toy and Real-world Problems: 8-puzzle, 8-queens, Vacuum world, Route-finding, Travelling Salesperson Problem (TSP).
  * **Worked Traces & Problems:**
    - Formal PEAS specification and environment characterization for 4 distinct systems (Autonomous Delivery Drone, Smart Medical Diagnostic System, Warehouse Automated Guided Vehicle, Interactive AI Language Tutor).
    - Complete State-Space graph formulation, branching factor calculation, and state space size estimation for the 8-puzzle problem.

* **Unit 2: Uninformed, Informed & Local Search**
  - Uninformed Search Strategies (Blind search):
    - Breadth-First Search (BFS): Queue frontier, Completeness, Time $O(b^d)$, Space $O(b^d)$, Optimality.
    - Uniform-Cost Search (UCS / Dijkstra on trees): Priority queue frontier, Optimality with non-negative step costs, Time/Space $O(b^{1 + \lfloor C^* / \epsilon \rfloor})$.
    - Depth-First Search (DFS): Stack frontier, Completeness on finite spaces, Time $O(b^m)$, Space $O(bm)$, Optimality.
    - Depth-Limited Search (DLS): Cutoff mechanism, Incompleteness.
    - Iterative Deepening Depth-First Search (IDDFS): Combining BFS optimality and DFS linear memory, Time $O(b^d)$, Space $O(bd)$.
    - Bidirectional Search: Meeting of frontiers.
    - Comprehensive comparative matrix of uninformed search strategies.
  - Informed (Heuristic) Search Strategies:
    - Best-First Search, Heuristic functions $h(n)$.
    - Greedy Best-First Search: Evaluation function $f(n) = h(n)$, Incompleteness and sub-optimality.
    - $A^*$ Search: Evaluation function $f(n) = g(n) + h(n)$.
    - Conditions for Optimality of $A^*$: Admissibility for tree search ($h(n) \le h^*(n)$), Consistency / Monotonicity for graph search ($h(n) \le c(n, a, n') + h(n')$).
    - Heuristics for 8-Puzzle: Manhattan distance, Misplaced tiles. Dominance of heuristics ($h_2(n) \ge h_1(n)$).
  - Local Search Algorithms & Optimization:
    - State space landscape (Current state, Objective function, Global maximum, Local maxima, Ridges, Plateaux, Shoulder).
    - Hill-Climbing Search (Greedy local search), Failure modes, Variants: Stochastic hill-climbing, First-choice hill climbing, Random-restart hill climbing.
    - Simulated Annealing: Inspiration from metallurgy, Temperature parameter $T$, Acceptance probability $P = e^{\Delta E / T}$, Cooling schedule.
    - Local Beam Search: Tracking $k$ states simultaneously.
    - Genetic Algorithms: Chromosome representation, Fitness function, Selection, Crossover (single-point, multi-point), Mutation.
  * **Solved Numericals & Traces:**
    - Uninformed search comparison trace: BFS, DFS, and UCS step-by-step node expansion tables on a state graph.
    - $A^*$ Search manual step-by-step trace on a pathfinding graph showing Open list (priority queue), Closed list, $g(n)$, $h(n)$, and $f(n)$ values at every expansion step.
    - Proof and verification of heuristic admissibility and consistency on given problem instances.
    - Simulated Annealing downhill move probability calculation at decreasing temperatures $T=1000, 100, 10$.

* **Unit 3: Adversarial Search & Constraint Satisfaction Problems**
  - Adversarial Search (Games): Games as search problems, Types of games (Deterministic, Zero-sum, Perfect information: Chess, Checkers, Go, Tic-Tac-Toe).
  - Minimax Algorithm: Game tree structure (MAX nodes, MIN nodes, Terminal states, Utility function), Minimax value definition, Recursive mathematical formulation, Optimal play.
  - Alpha-Beta Pruning: Pruning principle, $\alpha$ (best choice for MAX so far) and $\beta$ (best choice for MIN so far), Pruning condition ($\beta \le \alpha$), Alpha-beta search algorithm, Effectiveness of alpha-beta pruning (Move ordering, Worst-case $O(b^m)$ vs Best-case $O(b^{m/2})$).
  - Constraint Satisfaction Problems (CSP): Formal definition $(X, D, C)$ - Variables $X$, Domains $D$, Constraints $C$. Constraint types: Unary, Binary, Higher-order / Global constraints (Alldiff).
  - Constraint Propagation: Constraint graph representation, Node Consistency, Arc Consistency (AC-3 algorithm step-by-step), Path Consistency.
  - Backtracking Search for CSPs: Basic recursive backtracking, Heuristics for variable ordering: Minimum Remaining Values (MRV / Most Constrained Variable), Degree Heuristic; Heuristic for value ordering: Least Constraining Value (LCV).
  - Forward Checking: Detecting failures early, Arc consistency in search.
  * **Solved Traces & Numericals:**
    - Complete Minimax evaluation on a 4-ply game tree with terminal utility payoffs.
    - Alpha-Beta Pruning step-by-step trace: Identifying every evaluated node, updating $[\alpha, \beta]$ windows, and explicitly identifying all pruned branches/subtrees.
    - AC-3 algorithm full queue trace on a Map Coloring problem (e.g. Map of Australia with 7 regions and 3 colors {Red, Green, Blue}).
    - CSP Backtracking trace combining MRV, Degree Heuristic, and Forward Checking on a 4-Queens problem.

---

### 5. Software Engineering (IS52)
* **Unit 1: Professional Software Development, Processes & Agile**
  - Professional Software Development: Nature of software, Software engineering definition, Software engineering vs Computer Science, Attributes of good software (Maintainability, Dependability & Security, Efficiency, Acceptability), Software engineering diversity.
  - Software Engineering Ethics: ACM/IEEE Code of Ethics (Public, Client & Employer, Product, Judgment, Management, Profession, Colleagues, Self).
  - Case Studies: Insulin Pump control system (Safety-critical), Mentcare mental health patient management system (Privacy-critical), Wilderness weather station (Distributed data collection).
  - Software Processes: Software process models (Waterfall model, Incremental development, Integration and configuration / Reuse-oriented software engineering), Process activities (Specification, Design and Implementation, Validation, Evolution).
  - Coping with Change: System prototyping, Incremental delivery, Boehm's Spiral Model (4 sectors: Determine objectives, Identify and resolve risks, Development and testing, Plan next phase).
  - Process Improvement: CMMI capability maturity model (Initial, Managed, Defined, Quantitatively Managed, Optimizing).
  - Agile Software Development: Agile Manifesto principles, Plan-driven vs Agile development, Extreme Programming (XP: Pair programming, Test-first development, Refactoring, Continuous integration).
  - Scrum Framework: Scrum roles (Product Owner, Scrum Master, Development Team), Scrum events (Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective), Scrum artifacts (Product Backlog, Sprint Backlog, Increment, Burndown charts), Scaling agile methods.
  * **Worked Examples & Scenarios:**
    - Sprint velocity and burndown rate calculation across a 3-sprint release schedule.
    - Process model selection evaluation for 4 distinct industry problem scenarios.
    - Detailed comparative analysis matrix: Waterfall vs Agile vs Reuse-Oriented.

* **Unit 2: Requirements Engineering & System Modeling**
  - Requirements Engineering: Functional vs Non-functional requirements (Product, Organizational, External requirements), Metrics for quantifying non-functional requirements (Speed, Size, Ease of use, Reliability, Robustness, Portability).
  - Software Requirements Document (SRS): Structure of SRS, IEEE 830 standard guidelines, Target audience of SRS.
  - Requirements Specification: Natural language, Structured specifications, Tabular specifications.
  - Requirements Engineering Processes: Elicitation and analysis (Interviews, Scenarios, Use cases, Ethnography/Observation), Requirements validation (Reviews, Prototyping, Test-case generation), Requirements management (Requirements planning, Change management, Traceability matrix - RTM).
  - System Modeling: Context models (System boundaries, Architecture context), Interaction models (Use Case modeling: Actors, Use cases, `<<include>>`, `<<extend>>`; Sequence diagrams: Lifelines, messages, synchronous/asynchronous calls, return values).
  - Structural Models: Class diagrams (Associations, aggregations, compositions, generalizations/inheritance, multiplicities).
  - Behavioral Models: Activity diagrams (Swimlanes, fork, join, decision nodes), State machine diagrams (States, events, transitions, guards).
  - Model-Driven Engineering (MDE, MDA: Computation Independent Model [CIM], Platform Independent Model [PIM], Platform Specific Model [PSM]).
  * **Worked Examples & Diagrams:**
    - Full IEEE 830 SRS section write-up for a Smart University Library Management System with verifiable NFR metrics.
    - Complete Use Case diagram design with comprehensive tabular use case specifications for Student Course Registration.
    - Sequence diagram trace for User Authentication & Two-Factor OTP Verification.
    - Requirements Traceability Matrix (RTM) linking 6 user requirements to architectural modules and unit tests.

* **Unit 3: Architectural Design & Object-Oriented Design**
  - Architectural Design: Architectural design decisions, Non-functional influences on architecture (Performance, Security, Safety, Availability, Maintainability).
  - Architectural Views: Kruchten's 4+1 View Model (Logical view, Process view, Development view, Physical view, Use case/Scenarios view).
  - Architectural Patterns: Structure, advantages, disadvantages, and applications of:
    - Model-View-Controller (MVC)
    - Layered Architecture
    - Repository Architecture
    - Client-Server Architecture
    - Pipe and Filter Architecture
  - Application Architectures: Transaction processing systems (Data processing systems e.g. E-commerce checkout), Language processing systems (Compilers, interpreters).
  - Object-Oriented Design using the UML: 5-step design process (Understand system context, Design system architecture, Identify principal system objects, Develop design models, Specify object interfaces).
  - Design Patterns (Gang of Four - GoF): Categories (Creational, Structural, Behavioral). Detailed study of:
    - Singleton Pattern
    - Factory Method Pattern
    - Adapter Pattern
    - Observer Pattern (Publish-Subscribe)
  - Implementation Issues: Software reuse, Configuration management, Host-target development.
  - Open Source Development: Open source licensing models (GPL, LGPL, BSD, MIT, Apache), Managing open-source dependencies and licensing risks.
  * **Worked Examples & Code:**
    - Architectural pattern selection trade-off matrix for 4 enterprise systems.
    - Complete Object-Oriented design (Class diagram + method contracts) for an Automated Teller Machine (ATM) subsystem.
    - Clean, production-ready code implementation and structural diagram for the Observer Pattern and Singleton Pattern.

---

### 6. Research Methodology & IPR (AL58)
* **Unit 1: Introduction to Research, Ethics & Literature Review**
  - Meaning and definition of research, Scientific method, Objectives of research (Exploratory, Descriptive, Diagnostic, Hypothesis-testing), Motivation in research.
  - Types of Research: Descriptive vs Analytical, Applied vs Fundamental/Basic, Quantitative vs Qualitative, Conceptual vs Empirical, One-time vs Longitudinal, Laboratory vs Field research.
  - Research Approaches (Inferential, Experimental, Simulation). Significance of research.
  - Ethics in Research: Fundamental ethical principles (Honesty, Objectivity, Integrity, Carefulness, Openness, Respect for intellectual property, Confidentiality, Social responsibility).
  - Research Misconduct: Fabrication, Falsification, Plagiarism (FFP), Self-plagiarism / Salami slicing, Redundant publication, Ghost authorship, Gift/Honorary authorship, Conflicts of interest.
  - Literature Review & Technical Reading: Objectives and importance of literature review, Synthesis of new and existing knowledge, Analysis and synthesis of prior art, Identifying research gaps.
  - Bibliographic Databases: Scopus, Web of Science, IEEE Xplore, Google Scholar, PubMed; Journal metrics: Impact Factor (IF), CiteScore; Author metrics: $h$-index, $i10$-index.
  - Citations and Attributions: Functions and attributes of citations, Citation styles (IEEE, APA, MLA, Harvard, Chicago), Impact of title and keywords on citation velocity, Knowledge flow through citation networks, Acknowledgments, Attributions, and Copyright permissions.
  * **Solved Metrics & Numericals:**
    - Manual calculation of a researcher's $h$-index from a citation distribution table.
    - Step-by-step computation of a journal's 2-year Journal Impact Factor (JIF).
    - Citation formatting exercise comparing IEEE and APA formats for books, journal articles, and conference papers.

* **Unit 2: Research Design, Experimental Design & Sampling**
  - Research Design: Meaning and need for research design, Features of a good research design.
  - Core Concepts in Research Design: Dependent and Independent Variables, Extraneous Variables, Control, Confounded Relationship, Research Hypothesis (Null hypothesis $H_0$, Alternative hypothesis $H_1$, Directional vs Non-directional), Experimental and Control Groups, Treatments, Experiment.
  - Experimental Designs:
    - Informal Experimental Designs: Before-and-after without control, After-only with control, Before-and-after with control.
    - Formal Experimental Designs: Completely Randomized Design (CRD), Randomized Block Design (RBD), Latin Square Design (LSD), Factorial Designs.
  - Sampling Design: Census vs Sample Survey, Steps in sampling design, Criteria for selecting a sampling procedure, Characteristics of a good sample design.
  - Types of Sample Designs:
    - Probability Sampling: Simple Random Sampling, Systematic Sampling, Stratified Random Sampling (Proportional vs Disproportional), Cluster Sampling, Multi-Stage Sampling.
    - Non-Probability Sampling: Convenience Sampling, Purposive / Judgment Sampling, Quota Sampling, Snowball Sampling.
  - Sample Size Determination: Factors influencing sample size, Sample size formula for estimating proportions ($n = \frac{Z^2 p q}{E^2}$) and means ($n = \frac{Z^2 \sigma^2}{E^2}$), Finite population correction factor.
  * **Solved Numericals & Worked Examples:**
    - Sample size determination calculation for given confidence level ($95\%$, $Z=1.96$), allowable margin of error $E=0.04$, and estimated proportion $p=0.5$.
    - Experimental variable identification and confounder analysis in 3 case studies (Clinical drug trial, Machine learning model benchmark, Educational pedagogy study).
    - ANOVA layout and degrees of freedom table construction for CRD and RBD experimental designs.

* **Unit 3: Data Collection, Measurement & Hypothesis Testing**
  - Data Collection: Primary Data vs Secondary Data.
  - Methods of Primary Data Collection: Observation Method (Structured vs Unstructured, Participant vs Non-participant), Interview Method (Personal, Telephone, Structured vs Unstructured), Questionnaire Method (Design guidelines, Pre-testing / Pilot survey, Open-ended vs Closed-ended questions), Schedule Method.
  - Measurement and Scaling: Nominal Scale, Ordinal Scale, Interval Scale, Ratio Scale (Properties, permissible statistics).
  - Tests of Sound Measurement:
    - Reliability: Test-retest reliability, Alternative-form reliability, Split-half reliability, Internal consistency (Cronbach's Alpha $\alpha$).
    - Validity: Content validity, Criterion-related validity (Concurrent, Predictive), Construct validity (Convergent, Discriminant).
  - Testing of Hypotheses: Fundamental concepts (Null hypothesis $H_0$, Alternative hypothesis $H_1$, Level of significance $\alpha$, Type I Error [$\alpha$], Type II Error [$\beta$], Power of a test [$1 - \beta$], Critical region / Rejection region, Two-tailed vs One-tailed tests, $p$-value approach).
  - 5-Step Hypothesis Testing Procedure.
  - Parametric vs Non-Parametric Tests:
    - Parametric: $Z$-Test (Single mean, Difference of means), Student's $t$-Test (Single mean, Independent two-sample, Paired $t$-test), ANOVA ($F$-test).
    - Non-Parametric: Chi-Square ($\chi^2$) Test (Goodness of fit, Test of independence of attributes).
  * **Solved Numericals:**
    - Complete $Z$-Test for a large sample mean ($n > 30$) with formulation of hypotheses, test statistic calculation, critical value comparison at $\alpha = 0.05$, and formal decision.
    - Student's $t$-Test worked example for a small sample ($n = 10$) comparing sample mean to population standard.
    - Chi-Square ($\chi^2$) test of independence on a $2 \times 2$ contingency table with calculated vs critical $\chi^2$ statistic.

---

### 7. Environmental Studies (HS510)
* **Unit 1: Environment, Ecosystems & Ecological Succession**
  - Definition, scope, and importance of Environmental Studies, Need for public awareness, Multidisciplinary nature of environmental science.
  - Ecosystem Concept: Structure and components of an ecosystem.
    - Abiotic Components: Climatic factors (Temperature, Light, Humidity, Precipitation), Edaphic factors (Soil composition, pH), Chemical factors (Organic and inorganic nutrients).
    - Biotic Components: Producers (Autotrophs), Consumers (Heterotrophs: Herbivores, Carnivores, Omnivores), Decomposers (Saprotrophs: Fungi, Bacteria).
  - Functional Ecosystem Dynamics:
    - Energy flow in ecosystems (First and Second Laws of Thermodynamics, Lindeman's 10% Trophic Transfer Efficiency Law, Y-shaped energy flow model).
    - Food Chains: Grazing food chain vs Detritus food chain.
    - Food Webs: Complexity, stability, trophic interactions.
    - Ecological Pyramids: Pyramid of Numbers, Pyramid of Biomass, Pyramid of Energy; Upright vs Inverted pyramids in terrestrial and aquatic ecosystems.
  - Major Ecosystem Types: Forest ecosystem, Grassland ecosystem, Desert ecosystem, Aquatic ecosystems (Freshwater: Ponds, Lakes, Streams, Rivers; Marine: Oceans, Coral reefs, Estuaries).
  - Ecological Succession: Definition, causes, and mechanisms (Nudation, Invasion / Migration, Ecesis, Aggregation, Competition, Reaction, Stabilization / Climax community), Primary vs Secondary succession, Hydrosere (Hydrarch) stages, Xerosere (Xerarch) stages.
  - Biogeochemical Cycles: Carbon cycle, Nitrogen cycle, Water (Hydrological) cycle.
  * **Calculations & Models:**
    - Energy flow calculation across 4 trophic levels (Producer -> Primary Consumer -> Secondary Consumer -> Tertiary Consumer) using Lindeman's 10% law.
    - Population doubling time calculation using the Rule of 70 ($T = 70 / r$).

* **Unit 2: Natural Resources, Energy & Conservation**
  - Natural Resources: Classification (Renewable vs Non-Renewable resources).
  - Forest Resources: Global and Indian forest cover, Uses of forests, Deforestation causes and ecological consequences, Timber extraction, Mining effects on forests, Dams and their impact on forests and indigenous tribal populations, Forest conservation movements: Chipko Movement, Appiko Movement.
  - Water Resources: Surface water vs Ground water distribution, Over-utilization and water table depletion, Floods, Droughts, Conflicts over water (Inter-state river disputes: Cauvery and Krishna river disputes), Big dams: Benefits and ecological problems, Rainwater Harvesting methods (Rooftop collection, Recharge pits).
  - Mineral Resources: Use and exploitation, Environmental impacts of mining and mineral processing, Acid mine drainage, Rehabilitation of abandoned mined lands.
  - Food Resources: World food problems, Impacts of agriculture and overgrazing, Modern agricultural practices (High-Yield Varieties, Fertilizer pollution, Biomagnification of pesticides [DDT], Waterlogging, Soil salinity), Sustainable agriculture.
  - Land Resources: Land as a resource, Land degradation causes, Man-induced landslides, Soil erosion types, Desertification causes and mitigation, Soil conservation measures (Terracing, Contour bunding, Afforestation).
  - Energy Resources: Growing global energy demands, Non-renewable energy sources (Coal, Petroleum, Natural gas, Nuclear power; Nuclear hazards and disposal of radioactive wastes, Chernobyl, Fukushima), Renewable energy sources (Solar energy, Wind power, Hydroelectric power, Biomass & Biogas, Geothermal energy, Tidal & Wave energy).
  * **Calculations & Models:**
    - Rooftop rainwater harvesting yield calculation formula ($V = A \times R \times C$).
    - Solar PV rooftop energy generation and annual carbon offset calculation.

* **Unit 3: Biodiversity, Threats & Conservation Strategies**
  - Biodiversity: Definition, Levels of biodiversity:
    - Genetic Diversity (Variation of genes within species).
    - Species Diversity (Species richness and species evenness).
    - Ecosystem / Community Diversity (Alpha, Beta, Gamma diversity).
  - Biogeographical Classification of India (10 Biogeographic zones).
  - Value of Biodiversity: Consumptive use value, Productive use value, Social value, Ethical value, Aesthetic value, Option value, Ecosystem services.
  - Biodiversity at Global, National, and Local Levels: India as one of the 17 Mega-diversity nations.
  - Biodiversity Hotspots: Hotspot criteria (Norman Myers criteria: $\ge 1500$ endemic vascular plant species, $> 70\%$ habitat loss), The 4 Indian Biodiversity Hotspots (Western Ghats & Sri Lanka, Eastern Himalayas, Indo-Burma, Sundaland).
  - Threats to Biodiversity: Habitat destruction and fragmentation, Poaching of wildlife, Man-wildlife conflict causes and mitigation, Invasive alien species (Lantana, Parthenium, Water Hyacinth), Environmental pollution, Climate change.
  - Endangered and Endemic Species of India: IUCN Red Data Book categories (Extinct, Critically Endangered, Endangered, Vulnerable, Near Threatened, Least Concern).
  - Conservation of Biodiversity:
    - In-situ Conservation: National Parks (IUCN Category II), Wildlife Sanctuaries (IUCN Category IV), Biosphere Reserves (Core, Buffer, Transition zones), Sacred Groves. Project Tiger, Project Elephant.
    - Ex-situ Conservation: Botanical Gardens, Zoological Parks, Seed Banks, Gene Banks, Cryopreservation, Tissue Culture.
  * **Calculations & Indices:**
    - Simpson's Diversity Index ($D = 1 - \sum \frac{n(n-1)}{N(N-1)}$) step-by-step computation for two forest communities.
    - Shannon-Wiener Diversity Index ($H' = -\sum p_i \ln p_i$) and Species Evenness calculation.

---

### 8. Front End Development using ReactJS (ISAEC594)
* **Unit 1: Introduction to React, Vite & JSX**
  - What is React? Single Page Applications (SPA), History, Evolution, and Ecosystem.
  - Key Features of React: Component-Based Architecture, Declarative UI (Declarative vs Imperative programming paradigms), One-Way Data Flow (Unidirectional data binding).
  - The Virtual DOM: How the Browser DOM works and browser reflow/repaint performance bottlenecks. What is the Virtual DOM? The Reconciliation algorithm (Heuristic $O(n)$ diffing algorithm, Fiber architecture, Batching updates).
  - React vs Other Front-End Frameworks: Comparison with Angular (Framework vs Library, Two-way vs One-way binding, TypeScript/templates vs JavaScript/JSX) and Vue.js.
  - Setting up the React Development Environment: Node.js, npm, npx. Modern build tooling with Vite (Why Vite replaced Create React App: Native ES Modules, esbuild pre-bundling, Hot Module Replacement [HMR]). Initializing and running a Vite React project.
  - React Project Structure: Directory walkthrough (`index.html`, `src/main.jsx`, `src/App.jsx`, `assets/`, `package.json`, `vite.config.js`). Execution lifecycle from entry point to browser render.
  - Introduction to JSX (JavaScript XML): What is JSX and why use it? JSX Syntax Rules: Single root element requirement, closing all tags, camelCase attribute naming (`className` instead of `class`, `htmlFor` instead of `for`).
  - Embedding JavaScript Expressions in JSX: Curly brace `{}` syntax, arithmetic expressions, function calls, variable interpolations.
  - Conditional Rendering in JSX: `if/else` statements, Ternary operator (`condition ? <TrueView /> : <FalseView />`), Short-circuit logical AND (`condition && <View />`), Switch statements.
  - Rendering Lists: Transforming arrays using `.map()`, The critical role of the unique `key` prop in React diffing, Why index should not be used as key for dynamic lists.
  - JSX Compilation Under the Hood: Babel transpilation, Legacy `React.createElement()` vs React 17+ Modern JSX Transform (`_jsx` runtime).
  * **Tested Runnable Code Snippets:**
    - Complete Vite project bootstrap and running instructions.
    - Dynamic greeting component with expressions and styling.
    - Conditional rendering dashboard displaying login state and notifications.
    - Product catalog list renderer with unique keys and price badges.
    - Raw transpiled JSX code comparison side-by-side with original JSX.

* **Unit 2: Components, Props, State & Lifecycle**
  - Components: What is a component? The building blocks of React UIs.
  - Functional Components: Modern standard syntax, Arrow function components, Pure functions in React.
  - Overview of Class Components: ES6 class syntax, `render()` method, `this` keyword binding, Why the industry shifted to functional components with Hooks.
  - Creating and Rendering Components: Component composition, Parent-child relationships, Nesting components.
  - Props (Properties): What are Props? Passing data down the component tree.
  - Accessing Props: Props object vs Object destructuring in function signatures, Setting default prop values, Type checking concepts.
  - Immutability of Props: Why props are read-only and must never be modified by the receiving child component.
  - Advanced Props Patterns: Passing functions / callbacks as props, `props.children` and container/wrapper component patterns.
  - React Fragments: The wrapper `<div>` problem (DOM pollution and styling breakage), `<React.Fragment>` and shorthand syntax `<> ... </>`, Passing `key` to fragments in mapped lists.
  - Introduction to State using `useState`: What is state? Props vs State (Comprehensive comparative matrix).
  - The `useState` Hook: Declaring state variables and setter functions, Initial state values, Asynchronous nature of state updates and batching.
  - Functional State Updates: Why and when to use `setCount(prev => prev + 1)` instead of `setCount(count + 1)`.
  - Re-rendering Mechanics: What triggers a component re-render? Component lifecycle mental model in functional components.
  - State Immutability Rules: Updating primitive state vs updating objects and arrays (Using the spread operator `...` and immutable array methods `.filter()`, `.map()`, `[...arr, newItem]`).
  * **Tested Runnable Code Snippets:**
    - Interactive Counter with configurable step size and reset buttons.
    - Reusable User Profile Badge using `props` destructuring and `children` container pattern.
    - Dynamic Todo list demonstrating immutable array state additions and deletions.
    - Expandable / Collapsible FAQ accordion card.

* **Unit 3: Events, Forms & Lifting State Up**
  - Handling Events in React: Native DOM event handling vs React event system.
  - SyntheticEvent: Cross-browser event wrapper, Event normalization, Event delegation at root container.
  - Event Naming and Syntax: camelCase event names (`onClick`, `onChange`, `onSubmit`), Passing function references vs invoking functions (`onClick={handleClick}` vs `onClick={handleClick()}`).
  - Passing Arguments to Event Handlers: Inline arrow functions (`onClick={() => handleDelete(id)}`), Curried functions.
  - Controlled vs Uncontrolled Components: Detailed architectural comparison, Single source of truth principle, When to use each.
  - Controlled Form Inputs: Managing text inputs with `value` and `onChange`, Preventing form desynchronization.
  - Handling Diverse Form Elements:
    - Text inputs (`<input type="text">`)
    - Text areas (`<textarea>`)
    - Select dropdowns (`<select>`)
    - Checkboxes (`<input type="checkbox">`)
    - Radio buttons (`<input type="radio">`)
  - Scalable Form State: Single unified change handler for multi-input forms using computed property names `[e.target.name]: e.target.value`.
  - Form Submission and Validation: Handling form submit with `e.preventDefault()`, Client-side validation logic, Displaying dynamic inline error messages.
  - Lifting State Up: Why and when to lift state up? Finding the common ancestor component, Passing state down as props and passing setter functions down as callback handlers, Two-way synchronization between sibling components.
  * **Tested Runnable Code Snippets:**
    - Full-featured, validated User Registration Form with multiple input types and real-time validation error alerts.
    - Interactive Temperature Converter demonstrating lifting state up between synchronized Celsius and Fahrenheit input components.
    - Live Search Filter component filtering a list of items based on real-time query state in parent component.

---

## 3. Implementation Log & Commit History

| Stage / Unit | Status | Notes File Path | Commits / Notes |
| :--- | :--- | :--- | :--- |
| **Shared Assets** | In Progress | `assets/katex/`, `css/notes.css`, `js/notes.js` | KaTeX extracted; writing CSS & JS |
| **ML Unit 1 (PILOT)** | Pending | `notes/ml/unit1/unit-1-notes.html` | Pilot build & verification |
| **ML Unit 2** | Pending | `notes/ml/unit2/unit-2-notes.html` | |
| **ML Unit 3** | Pending | `notes/ml/unit3/unit-3-notes.html` | |
| **TOC Unit 1** | Pending | `notes/toc/unit1/unit-1-notes.html` | |
| **TOC Unit 2** | Pending | `notes/toc/unit2/unit-2-notes.html` | |
| **TOC Unit 3** | Pending | `notes/toc/unit3/unit-3-notes.html` | |
| **CN Unit 1** | Pending | `notes/cn/unit1/unit-1-notes.html` | |
| **CN Unit 2** | Pending | `notes/cn/unit2/unit-2-notes.html` | |
| **CN Unit 3** | Pending | `notes/cn/unit3/unit-3-notes.html` | |
| **AI Unit 1** | Pending | `notes/ai/unit1/unit-1-notes.html` | |
| **AI Unit 2** | Pending | `notes/ai/unit2/unit-2-notes.html` | |
| **AI Unit 3** | Pending | `notes/ai/unit3/unit-3-notes.html` | |
| **SE Unit 1** | Pending | `notes/se/unit1/unit-1-notes.html` | |
| **SE Unit 2** | Pending | `notes/se/unit2/unit-2-notes.html` | |
| **SE Unit 3** | Pending | `notes/se/unit3/unit-3-notes.html` | |
| **RMIPR Unit 1** | Pending | `notes/rmipr/unit1/unit-1-notes.html` | |
| **RMIPR Unit 2** | Pending | `notes/rmipr/unit2/unit-2-notes.html` | |
| **RMIPR Unit 3** | Pending | `notes/rmipr/unit3/unit-3-notes.html` | |
| **EVS Unit 1** | Pending | `notes/evs/unit1/unit-1-notes.html` | |
| **EVS Unit 2** | Pending | `notes/evs/unit2/unit-2-notes.html` | |
| **EVS Unit 3** | Pending | `notes/evs/unit3/unit-3-notes.html` | |
| **ReactJS Unit 1** | Pending | `notes/reactjs/unit1/unit-1-notes.html` | |
| **ReactJS Unit 2** | Pending | `notes/reactjs/unit2/unit-2-notes.html` | |
| **ReactJS Unit 3** | Pending | `notes/reactjs/unit3/unit-3-notes.html` | |
| **Integration** | Pending | `data/subjects.js`, `data/notes-index.json`, `README.md` | Final wiring & index |
