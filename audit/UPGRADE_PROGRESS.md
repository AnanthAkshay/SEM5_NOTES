# Combined Sync + Quality Upgrade Progress Checklist

## Master Phases

- [x] **Part 0: Read Baseline & Repo Size Audit**
  - [x] Read `audit/NOTES_PLAN.md`, `audit/NOTES_VS_SYLLABUS_REPORT.md`, `audit/NOTES_STYLE_DIAGNOSIS.md`, `audit/content_hashes_before.json`
  - [x] Review `audit/verify/` scripts (24 scripts present)
  - [x] Run `git count-objects -vH` & report sizes (.git: 182.52 MB, notes/: 184.69 MB, repo total: 581.76 MB)

- [x] **Part B: Textbooks Local-Only & Copyright Gates**
  - [x] Verify Git history for textbook PDFs (`git log --all --name-only` -> 0 matches)
  - [x] Create `textbooks/` directory and add to `.gitignore`
  - [x] Add `*[Ff]orouzan*.pdf` and `*[Tt]extbook*.pdf` to `.gitignore`
  - [x] Forouzan Textbook edition verified: 4th Edition (2007) by Behrouz A. Forouzan & Sophia Chung Fegan (McGraw-Hill)
  - [x] Commit: `chore(security): ignore local textbook reference files and create textbooks directory` (db09c49)

- [x] **Part A: Sync New Files from Raw Subject Folders**
  - [x] **AI (ISE552)**:
    - [x] Copy `AI-2.pdf` -> `notes/ai/unit1/ai-intro-intelligent-agents.pdf`
    - [x] Copy `AI-Intelligent_Agents.pdf` -> `notes/ai/unit1/ai-problem-solving-agents.pdf`
    - [x] Copy `AI-Intelligent_Agents-PS.pdf` -> `notes/ai/unit1/ai-problem-solving-agents-alt.pdf`
    - [x] Copy `AI-AGENTS-Uninformed_Search.pdf` -> `notes/ai/unit2/ai-uninformed-search.pdf`
    - [x] Copy `AI-Informed_Search.pdf` -> `notes/ai/unit2/ai-informed-search.pdf`
    - [x] Copy `AI-Local_Search.pdf` -> `notes/ai/unit2/ai-local-search.pdf`
    - [x] Copy `AI-Adversarial_Search.pdf` -> `notes/ai/unit3/ai-adversarial-search.pdf`
  - [x] **REACT_JS (ISAEC594)**:
    - [x] Copy `UNIT-1 ReactJS.pptx` -> `notes/reactjs/unit1/reactjs-unit1.pptx`
    - [x] Convert to PDF -> `notes/reactjs/unit1/reactjs-unit1.pdf`
  - [x] **SE (IS52)**:
    - [x] Copy `se_ppt _unit 2.pptx` -> `notes/se/unit2/unit-2-system-modeling.pptx`
    - [x] Convert to PDF -> `notes/se/unit2/unit-2-system-modeling.pdf`
  - [x] Update `data/subjects.js` with new registered files, status badges, hash-chips, file totals
  - [x] Rebuild notes search index (`data/notes-index.json` / `data/notes-index.js`)
  - [x] Update `README.md` file counts & inventory
  - [x] Commit: `feat(sync): add AI lecture slide PDFs, ReactJS Unit 1 slides, and SE Unit 2 system modeling` (c543cbe)

- [ ] **Part C & D: Pilot Subject – Computer Networks (CN, IS53)**
  - [x] **Unit 1**: Verification against Forouzan 4th Ed, charts (latency breakdown bar, BDP pipe, cascaded dB stages, hybrid star-bus topology), verified numericals (attenuation, cascaded dB, Nyquist, Shannon, Store-and-Forward latency, BDP), interactive Latency & BDP explorer, "Sources & verification" box, past exam questions solved from Ramaiah CIE-1 2025.
  - [x] **Unit 2**: Verification against Forouzan 4th Ed, charts (ARP packet format, Selective Repeat sliding window timing, CRC Modulo-2 division), verified numericals (CIE-1 Q1.c CRC, CIE-2 Q1.b Selective Repeat window proof, CIE-1 Q3.b ISE DEPARTMENT 16-bit Checksum, Hamming distance, ALOHA throughput), interactive CRC-4 calculator & error injector, "Sources & verification" box, past exam questions solved from Ramaiah CIE-1 and CIE-2 2025.
  - [x] **Unit 3**: Verification against Forouzan 4th Ed, charts (IPv4 20-byte header format, CIDR prefix bit partition, Dijkstra 6-node shortest path graph, NAT packet flow), verified numericals (CIE-2 Q3.a Dijkstra 6-node step-by-step, CIE-2 Q2.a NAT translation table, CIE-2 Q2.c TCP congestion, CIE-2 Q1.c port ranges, CIE-2 Q1.a IPv4 vs IPv6, CIDR /27, VLSM 3-department, 4000-byte fragmentation), interactive IPv4 Subnet & CIDR calculator, "Sources & verification" box, 6 verified practice problems with hidden solutions.
  - [x] Update `audit/verify/cn/` scripts
  - [x] Commit CN updates per unit/purpose (921e677, 411b987, 021f57a)

- [ ] **Part C & D: Subject Upgrades (Remaining Subjects)**
  - [x] **TOC (IS54)**:
    - [x] **Unit 1**: Verification against Hopcroft 3rd Ed, state diagrams (DFA ending in '01', 4-state parity DFA, even length starting with '00'), interactive DFA string simulator in vanilla JS, solved exam questions from Ramaiah CIE-1 Oct 2025 and SEE Jan 2026, 6 verified practice problems with hidden solutions.
    - [x] **Unit 2**: Verification against Hopcroft 3rd Ed, charts (6-state DFA minimization diagram, Thompson's construction for $(00)^* 11 (0+1)^*$), verified numericals (CIE-1 Q1.b 6-state minimization to 2 states, SEE Jan 2026 Q3.b 8-state table-filling with unreachable state pruning, CIE-1 Q2.b Thompson construction, Arden's theorem, Pumping lemma for palindromes and $0^{n^2}$), interactive Table-Filling Minimizer step-by-step simulator, "Sources & verification" box, 6 verified practice problems with hidden solutions.
    - [x] **Unit 3**: Verification against Hopcroft 3rd Ed, charts (ambiguity parse trees for 'abab' SEE Jan 2026 Q5.c, PDA state transition diagram & stack ID trace for $a^n b^n$ CIE-2 Q1.b), verified numericals (CIE-2 Q1.a balanced parens & equal a/b, CIE-2 Q1.b PDA trace, CIE-2 Q2.a nullable epsilon elimination, CIE-2 Q3.a leftmost derivation, SEE Jan 2026 Q5.c ambiguity proof, CNF transformations), interactive Pushdown Automaton (PDA) stack simulator, "Sources & verification" box, 6 verified practice problems with hidden solutions.
  - [x] **ML (IS51)**:
    - [x] **Unit 1**: Verification against Sridhar & Vijayalakshmi (2021) and Mitchell (1997), charts (Figure 1.2 ML process pipeline, Figure 1.3 Bias-Variance tradeoff curve, Figure 1.4 Confusion matrix & diagnostic metrics map), verified numericals (Descriptive statistics $s^2=221.78$, Bivariate Pearson $r=0.9959$, Spam classifier metrics, Medical triage metrics), interactive Confusion Matrix & Diagnostic Metric Analyzer in vanilla JS, solved exam questions from Ramaiah CIE-1 March 2026 and SEE June/July 2026, 6 verified practice problems with hidden solutions.
    - [x] **Unit 2**: Verification against Sridhar & Vijayalakshmi (2021) and Mitchell (1997), charts (Figure 2.1 PCA 2D geometric projection, Figure 2.2 Version space & hypothesis lattice), verified numericals (CIE-2 Q2.c PCA on $C = [[4, 2], [2, 4]]$ with $\lambda_1=6.0, \lambda_2=2.0, \mathbf{e}_1=\frac{1}{\sqrt{2}}[1, 1]^T$, CIE-1 Q1.b Ordinal attribute dissimilarity, CIE-1 Q2.b 10-sample Buys_Computer Find-S trace, Candidate Elimination boundary updates, PAC $m \ge 99$ sample complexity), interactive Concept Learning & Find-S Stepper in vanilla JS, solved exam questions from Ramaiah CIE-1, CIE-2, and SEE 2026, 6 verified practice problems with hidden solutions.
    - [x] **Unit 3**: Verification against Sridhar & Vijayalakshmi (2021) and Mitchell (1997), charts (Figure 3.1 OLS regression best-fit line with residuals, Figure 3.2 Complete ID3 decision tree for Play Tennis), verified numericals (CIE-1 Q1.c Study hours regression line $\hat{Y} = 4.50X + 41.00$, predicted $\hat{Y}(7)=72.50$, CIE-2 Q3.a K-NN regression on HPI with $K=3 \implies \hat{y}=180.67$, CIE-1 Q3.c & SEE Q5.b ID3 information gain $IG(S, \text{Outlook})=0.32193$, Logistic sigmoid probabilities), interactive Linear Regression & Error Minimizer in vanilla JS, solved exam questions from Ramaiah CIE-1, CIE-2, and SEE 2026, 6 verified practice problems with hidden solutions.
  - [x] **AI (ISE552)**:
    - [x] **Unit 1**: Verification against Russell & Norvig 4th Ed and Rich & Knight 3rd Ed, charts (Figure 1.1 Four Approaches to AI 2x2 grid, Figure 1.2 Model-Based Reflex Agent architecture, Figure 1.3 PEAS Task Environment Architecture for Smart Traffic & Medical Systems), verified numericals (8-puzzle $9! = 362,880$, $181,440$ reachable states via Inversion Parity Theorem, average branching factor $b = 2.67$, 8-queens state space sizes $\binom{64}{8} \approx 4.43 \times 10^9$ down to $8! = 40,320$), interactive Agent Architecture & PEAS Environment Simulator in vanilla JS, solved exam questions from Ramaiah CIE-1 Oct 29, 2025 (Q1.a 4 AI approaches, Q2.a Model-Based Reflex agent, Q3.a PEAS for Smart Traffic & Medical Diagnosis, SEE 8-puzzle state space formulation, 7-dimension environment classification), 6 verified practice problems with hidden solutions.
    - [x] **Unit 2**: Verification against Russell & Norvig 4th Ed, charts (Figure 2.1 A* graph search expansion tree with $f=g+h$ and optimal cost 8, Figure 2.2 8-puzzle A* search tree with $h_1$ misplaced tiles, Figure 2.3 Simulated Annealing energy landscape & Boltzmann probability curve $P = e^{\Delta E / T}$), verified numericals (A* optimal path $S \to A \to B \to C \to D \to G = 8$, heuristic consistency checks, heuristic dominance $h_2 \ge h_1$, simulated annealing probabilities $T=1000\text{K} \implies 99.50\%, T=1\text{K} \implies 0.67\%$), interactive Search Algorithm & Simulated Annealing Simulator in vanilla JS, solved exam questions from Ramaiah CIE-1 Oct 29, 2025 (Q1.b Bidirectional search vs BFS/DFS, Q2.b 8-puzzle A* with $h_1$, Q3.b Uninformed search vs UCS, SEE A* tree/graph optimality proofs, Simulated annealing cooling dynamics), 6 verified practice problems with hidden solutions.
    - [x] **Unit 3**: Verification against Russell & Norvig 4th Ed, charts (Figure 3.1 Minimax game tree with $\alpha$-$\beta$ pruning cutoffs, Figure 3.2 Australia map coloring CSP constraint network & AC-3 domain pruning), verified numericals (Minimax root value $= 3$, $\beta \le \alpha \implies 2 \le 3$ cutoff pruning leaves 4 and 6, AC-3 domain reduction $WA=\{R\} \implies NT, SA \in \{G, B\}$, AC-3 arc count for complete $K_5 = 20$), interactive Game Tree & CSP Arc Consistency Simulator in vanilla JS, solved exam questions from Ramaiah CIE-1 Oct 29, 2025 (Q1.c Minimax game tree trace, Q2.c $\alpha$-$\beta$ pruning efficiency, Q3.c $\alpha$ and $\beta$ bounding parameters, SEE AC-3 on Australia map coloring, Backtracking heuristics MRV/Degree/LCV), 6 verified practice problems with hidden solutions.
  - [x] **SE (IS52)**:
    - [x] **Unit 1**: Ian Sommerville 10th Ed & Pressman 9th Ed mapping, ACM/IEEE Code of Ethics, Waterfall vs Incremental, RUP 4 phases & exit milestones, Boehm's Spiral 4 quadrants, Scrum framework & Agile Manifesto, interactive Scrum Velocity & Sprint Burndown simulator, solved CIE-1 Oct 28, 2025 questions (Q1.a, Q2.a, Q3.a), 6 verified practice problems with hidden solutions.
    - [x] **Unit 2**: Requirements Engineering (Functional vs Non-Functional, Volere template, RTM), Use Case Modeling (Actor-boundary, UML syntax, CIE-1 Q3.b Library System with 7 actors/use-cases), Sequence diagrams, High-Availability SLA calculator ($A = 99.60\%$), interactive Traceability Matrix & Availability studio, solved CIE-1 Oct 28, 2025 questions, 6 verified practice problems.
    - [x] **Unit 3**: Architectural Design (Layered vs Repository CIE-2 Q1.a, Client-Server vs Pipe-and-Filter, Language processing compiler pipeline CIE-2 Q2.a), Gang of Four Design Patterns (Creational Singleton & Object Pool, Structural Adapter & Decorator, Behavioral Observer CIE-2 Q3.a & Strategy), interactive Design Patterns Studio, solved CIE-2 Dec 22, 2025 questions, 6 verified practice problems.
  - [x] **RMIPR (AL58)**:
    - [x] **Unit 1**: C.R. Kothari 4th Ed mapping, Research definition & 4 types, Research Process flowchart, Plagiarism classifications (Direct, Mosaic, Self, Accidental), Bibliometrics ($h$-index, $i10$-index, 2-Year Clarivate JIF), interactive Bibliometrics Studio ($h=7, i10=5, JIF=5.500$), solved CIE-1 Oct 29, 2025 questions (Q1.a, Q2.a, Q3.a) and SEE Feb/Mar 2025 (Q1.a, Q1.b, Q1.c), 6 verified practice problems.
    - [x] **Unit 2**: Research Design features, Principles of Experimental Design (Randomization, Replication, Local Control), Latin Square $m \times m$ layout and ANOVA degrees of freedom ($df_{\text{error}} = (m-1)(m-2) = 6$), Probability & Non-Probability sampling, Sample Size estimation (Proportion $n=385$, Mean $n=166$), interactive Sample Size & Latin Square Studio, solved CIE-1 Oct 29, 2025 questions (Q1.b, Q2.b, Q3.b) and Make-up 2025 Q3.b, 6 verified practice problems.
    - [x] **Unit 3**: Hypothesis Testing fundamentals (Null $H_0$ vs Alternative $H_a$, Type I $\alpha$ vs Type II $\beta$ errors), Large Sample $z$-tests (Single proportion $z=-1.25$, Finite Population Correction $z=-0.6711$), Small Sample Student's $t$-test ($t=-1.5278$ on 9 student heights), Chi-Square $\chi^2$ goodness-of-fit, IPR framework (Patents, Copyrights, Trademarks, Designs), interactive Hypothesis Testing Studio, solved CIE-2 Dec 22, 2025 questions (Q1.a, Q3.b) and SEE 2025 (Q5.b, Q6.b), 6 verified practice problems.
  - [x] **ReactJS (ISAEC594)**:
    - [x] **Unit 1**: Chris Minnick (Wiley 2022) & Fullstack React mapping, React philosophy (Declarative UI, Component-based, Unidirectional data flow), Virtual DOM & Fiber reconciliation heuristic rules, Vite vs CRA architecture, JSX syntax rules & embedding expressions, interactive JSX Compilation & Virtual DOM AST Diffing Studio, model exam questions, 6 verified practice problems matching `verify_react_u1.js`.
    - [x] **Unit 2**: Functional vs Class components, props passing & destructuring (`UserBadge`), `props.children` container composition pattern (`ModalCard`), `useState` hook mechanics & batching simulations, object & array immutability with shallow reference checks, interactive State Management & Composition Studio, model exam questions, 6 verified practice problems matching `verify_react_u2.js`.
    - [x] **Unit 3**: SyntheticEvent system & event delegation, `e.preventDefault()` SPA form handling, controlled vs uncontrolled inputs, scalable multi-field form management via computed property names (`[name]: value`), Lifting State Up pattern with synchronized temperature converter ($100^\circ\text{C} = 212^\circ\text{F}$), interactive Controlled Form & State Lifting Studio, model exam questions, 6 verified practice problems matching `verify_react_u3.js`.
  - [x] **EVS (HS510)**:
    - [x] **Unit 1**: Erach Bharucha & Benny Joseph mapping, 4 domains of environment, ecosystem structure, thermodynamic energy flow, Lindeman's 10% law ($25,000 \to 2,500 \to 250 \to 25\text{ kcal}$), Rule of 70 doubling time ($T = 70/1.75 = 40\text{ yrs}$), trophic efficiency ($11.0\%$), ecological pyramids, succession stages, nitrogen cycle, interactive Ecological Energy & Lindeman Studio, solved CIE-1 2024-2025 authentic questions, 6 verified practice problems matching `verify_evs_u1.py`.
    - [x] **Unit 2**: Forest, water, mineral, food, land, and energy resources; deforestation & dams, mining impacts & Acid Mine Drainage ($H_2SO_4$), wind erosion modes (saltation, creep, suspension), fossil fuel environmental impacts vs renewable alternatives, interactive Water Harvesting ($114,750\text{ L}$) & Solar PV Carbon Offset ($6.734\text{ tons}$) Studio, solved CIE-1 2024-2025 authentic questions, 6 verified practice problems matching `verify_evs_u2.py`.
    - [x] **Unit 3**: Levels of biodiversity (genetic, species, community $\alpha, \beta, \gamma$), 10 biogeographic zones of India, mega-diversity characteristics, Norman Myers hotspot criteria (Western Ghats, Eastern Himalayas, Indo-Burma, Sundaland), The Evil Quartet threats, In-situ vs Ex-situ conservation, interactive Simpson's ($1-D=0.7416$) and Shannon-Wiener ($H'=1.4541, J'=0.9035$) Diversity Index Studio, model exam questions, 6 verified practice problems matching `verify_evs_u3.py`.

- [x] **Part E & F: Quality Gates & Final Reporting**
  - [x] Run comprehensive audit across all 24 pages (`scripts/audit_all_24_pages.js`)
  - [x] 100% Zero horizontal overflow across all 4 viewports (1280px, 768px, 390px, 320px) on all 24 pages
  - [x] All page sizes < 150 KB (well under 700 KB gate)
  - [x] 100% Academic Verification Boxes present across all 24 pages
  - [x] 100% Interactive Explorers present and tested across all 24 pages
  - [x] 100% Authentic Exam Questions and Verified Practice Problems transcribed and solved
  - [x] Compile `audit/COMPREHENSIVE_AUDIT_REPORT.md`
  - [x] Final Report
