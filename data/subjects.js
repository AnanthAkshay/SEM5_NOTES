/**
 * SEM 5 · ISE Notes - Central Data Store
 * All subjects, units, files, syllabus data, and timetables are managed here.
 * Add new subjects, units, or files here without modifying any HTML.
 */

window.SEM5_DATA = {
  meta: {
    siteTitle: "SEM 5 · ISE Notes",
    tagline: "Department of Information Science & Engineering",
    semester: "Semester V",
    academicYear: "2024–2025 / 2025–2026",
    lastUpdated: "October 2026",
    repositoryName: "SEM5_NOTES",
    studentDegree: "B.E. Information Science & Engineering"
  },

  // Exam Timetable section (config-driven, placeholder slots)
  timetable: {
    enabled: true,
    title: "Exam & Assessment Schedules",
    subtitle: "Department schedules for Semester V examinations",
    items: [
      {
        id: "theory-see",
        title: "Semester-End Theory Examination (SEE)",
        category: "Theory",
        status: "Schedule Awaited",
        statusBadge: "Pending",
        pdfUrl: "", // Add relative path when available, e.g. "notes/timetables/see_theory.pdf"
        dateRange: "To be announced",
        description: "Official SEE schedule from the office of the Controller of Examinations."
      },
      {
        id: "lab-see",
        title: "Semester-End Practical / Lab Examination",
        category: "Laboratory",
        status: "Schedule Awaited",
        statusBadge: "Pending",
        pdfUrl: "", // Add relative path when available
        dateRange: "To be announced",
        description: "Batch-wise practical examination dates for ISE Semester V labs."
      },
      {
        id: "cie-1",
        title: "Continuous Internal Evaluation (CIE-1)",
        category: "Internal",
        status: "Completed / Reference Papers Available",
        statusBadge: "Completed",
        pdfUrl: "notes/evs/practice/evs-cie1-qp-2024.pdf",
        dateRange: "Term 03/10/2024 to 25/01/2025",
        description: "CIE-1 question papers available under EVS and ML Practice sections."
      }
    ]
  },

  subjects: [
    // 1. AI - Artificial Intelligence
    {
      id: "ai",
      code: "ISE552",
      name: "Artificial Intelligence",
      shortName: "AI",
      credits: "3:0:0",
      contactHours: "42 Hours",
      coordinator: "Dr Jagadeesh Sai D",
      prerequisites: "Nil",
      status: "syllabus_only", // "full_notes" | "syllabus_only"
      accent: {
        primary: "#8B5CF6",
        secondary: "#A78BFA",
        subtle: "rgba(139, 92, 246, 0.12)",
        glow: "rgba(139, 92, 246, 0.28)"
      },
      tags: ["Core ISE", "Elective", "AI & ML Track"],
      description: "Foundations of intelligent agents, problem-solving search algorithms, game theory, first-order logic reasoning, uncertainty, and modern Generative AI foundations.",
      notesNotice: "Notes coming soon. The complete syllabus, NPTEL video lecture links, recommended textbooks, and evaluation scheme are detailed below.",
      syllabus: {
        textbook: {
          title: "Artificial Intelligence: A Modern Approach",
          edition: "4th Edition (2021/2022)",
          authors: "Stuart Russell and Peter Norvig",
          publisher: "Pearson Education"
        },
        referenceBooks: [
          {
            title: "Artificial Intelligence and Machine Learning",
            edition: "1st Edition (2025)",
            authors: "Pradeep Singh, Tapan K. Gandhi and Balasubramanian Raman",
            publisher: "McGraw Hill India"
          },
          {
            title: "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
            edition: "3rd Edition (2022)",
            authors: "Aurélien Géron",
            publisher: "O'Reilly Media"
          }
        ],
        pedagogyMethod: "Project Based Learning & Conceptual Learning through NPTEL video lectures and discussion-based sessions.",
        evaluationScheme: {
          cieMarks: "50 Marks",
          seeMarks: "100 Marks (Scaled to 50 Marks)",
          details: [
            { component: "Internal Test - I", marks: 30, cos: "CO1, CO2, CO3" },
            { component: "Internal Test - II", marks: 30, cos: "CO3, CO4, CO5" },
            { component: "Average of Tests", marks: 30, note: "Average of Test-I and Test-II" },
            { component: "Other Components (MCQ / Project)", marks: 20, cos: "CO1, CO2, CO3, CO4, CO5" },
            { component: "Total CIE", marks: "50 Marks", note: "30 (Tests Avg) + 20 (MCQ/Project)" },
            { component: "Semester-End Exam (SEE)", marks: "50 Marks", note: "100 marks exam scaled down to 50" }
          ]
        },
        courseOutcomes: [
          {
            co: "CO1",
            text: "Understand the fundamentals of Artificial Intelligence and apply problem-solving techniques using agents to solve problems.",
            mapping: "PO-1, 2, 3, 5, 12; PSO-1, 3"
          },
          {
            co: "CO2",
            text: "Analyze uninformed and informed search strategies in solving real world problems.",
            mapping: "PO-1, 2, 3, 5, 12; PSO-1, 3"
          },
          {
            co: "CO3",
            text: "Apply adversarial search methods to make optimal game decisions and construct knowledge-based agents using logical reasoning.",
            mapping: "PO-1, 2, 3, 5, 12; PSO-1, 3"
          },
          {
            co: "CO4",
            text: "Apply knowledge using the syntax and semantics of First-Order Logic, and inference techniques to solve reasoning problems.",
            mapping: "PO-1, 2, 3, 5, 6, 12; PSO-1, 3"
          },
          {
            co: "CO5",
            text: "Apply algorithms for classical planning in AI and analyze the philosophical, ethical, and safety implications of artificial intelligence.",
            mapping: "PO-1, 2, 3, 5, 8, 12; PSO-1, 3"
          }
        ],
        units: [
          {
            unitNumber: 1,
            title: "Introduction to Artificial Intelligence & Intelligent Agents",
            topics: "Introduction to Artificial Intelligence, definition and goals of AI, foundations of AI, types of AI, applications of AI in engineering and society. Intelligent Agents: Agents and environments, sensors and actuators, rational agents, rationality, performance measures, PEAS representation, single-agent and multi-agent environments. Types of Agents: Simple reflex agents, model-based reflex agents, goal-based agents, utility-based agents, learning agents.",
            pedagogy: "Conceptual Learning through NPTEL video lectures and discussion-based sessions.",
            links: [
              { label: "NPTEL Course - AI Fundamentals", url: "https://nptel.ac.in/courses/112103280" },
              { label: "NPTEL Course - AI Search & Knowledge", url: "https://nptel.ac.in/courses/106106126" },
              { label: "NPTEL Video: Module 1 Lecture 2", url: "https://media.dev.nptel.ac.in/content/mp4/112/103/112103280/MP4/mod01lec02.mp4" }
            ]
          },
          {
            unitNumber: 2,
            title: "Problem-Solving Agents & Search Strategies",
            topics: "Problem-Solving Agents: Problem formulation, initial state, actions, transition model, goal test, path cost, state-space representation. Uninformed Search: Breadth First Search, Depth First Search, Uniform Cost Search, Depth-Limited Search, Iterative Deepening Search. Informed Search: Heuristic search, heuristic functions, Greedy Best-First Search, A* Search, admissible heuristics, consistent heuristics. Local Search: Hill Climbing, Simulated Annealing, local search applications. Adversarial Search: Game playing, game formulation, Minimax algorithm, Alpha-Beta pruning, evaluation functions.",
            pedagogy: "Case-based Learning using NPTEL videos and real-world case studies.",
            links: [
              { label: "NPTEL Video: State Space & Search (Mod 3 Lec 8)", url: "https://media.dev.nptel.ac.in/content/mp4/112/103/112103280/MP4/mod03lec08.mp4" },
              { label: "NPTEL Video: Informed Search Strategies (Mod 3 Lec 9)", url: "https://media.dev.nptel.ac.in/content/mp4/112/103/112103280/MP4/mod03lec09.mp4" },
              { label: "NPTEL Video: Adversarial Search & Games (Mod 4 Lec 11)", url: "https://media.dev.nptel.ac.in/content/mp4/112/103/112103280/MP4/mod04lec11.mp4" }
            ]
          },
          {
            unitNumber: 3,
            title: "Knowledge-Based Agents & Logical Reasoning",
            topics: "Knowledge-Based Agents: Knowledge and intelligence, knowledge representation, knowledge bases, inference. Propositional Logic: Propositions, logical connectives, truth tables, logical equivalence, inference, resolution. First-Order Logic: Predicates, variables, constants, functions, quantifiers, representation of knowledge using First-Order Logic. Reasoning: Forward chaining, backward chaining, rule-based reasoning.",
            pedagogy: "Hands-on Learning with NPTEL tutorials and guided agents building.",
            links: [
              { label: "NPTEL Video: Propositional & FOL Logic (Mod 8 Lec 23)", url: "https://media.dev.nptel.ac.in/content/mp4/112/103/112103280/MP4/mod08lec23.mp4" },
              { label: "NPTEL Course - Knowledge Representation", url: "https://nptel.ac.in/courses/106106140" },
              { label: "NPTEL Video: Inference & Resolution (Mod 4 Lec 10)", url: "https://media.dev.nptel.ac.in/content/mp4/112/103/112103280/MP4/mod04lec10.mp4" }
            ]
          },
          {
            unitNumber: 4,
            title: "Uncertainty & Generative AI",
            topics: "Uncertainty in AI: Sources of uncertainty, probability basics, conditional probability, Bayes' theorem, Bayesian reasoning, introduction to Bayesian Networks. Generative AI: Introduction to Generative AI, generative versus discriminative AI, Large Language Models, Transformer architecture – high-level understanding, foundation models, multimodal AI, AI assistants.",
            pedagogy: "Theoretical foundation paired with contemporary Generative AI architectures.",
            links: [
              { label: "Recommended Resource / Platform", url: "https://www.coursera.org/learn/raspberry-pi-platform" }
            ]
          },
          {
            unitNumber: 5,
            title: "Prompt Engineering, Ethics & Real-World Applications",
            topics: "Prompt Engineering: Introduction to prompting, zero-shot prompting, few-shot prompting, role prompting, structured prompting, prompt evaluation, hallucinations and limitations of Generative AI. Responsible and Ethical AI: AI bias, fairness, transparency, Explainability, privacy, security, copyright and intellectual property, human oversight, responsible use of Generative AI. AI Applications: AI in healthcare, cybersecurity, finance, smart cities, robotics, education, manufacturing and software engineering.",
            pedagogy: "Ethics workshops and domain case studies.",
            links: [
              { label: "NPTEL Video: AI Ethics & Society (Mod 1 Lec 3)", url: "https://media.dev.nptel.ac.in/content/mp4/107/106/107106090/MP4/mod01lec03.mp4" },
              { label: "NPTEL Course: Ethical & Responsible AI", url: "https://nptel.ac.in/courses/106105077" },
              { label: "NPTEL Video: Applications of AI (Mod 12 Lec 92)", url: "https://media.dev.nptel.ac.in/content/mp4/106/102/106102220/MP4/mod12lec92.mp4" }
            ]
          }
        ]
      },
      units: [
        {
          id: "ai-syllabus-unit",
          unitNumber: "Syllabus",
          title: "Official Syllabus & Course Scheme",
          isPractice: false,
          files: [
            {
              id: "ai-syl-pdf",
              title: "AI - ISE552 Official Syllabus Document",
              originalName: "AI-ISE552 SYLLABUS.docx",
              path: "notes/ai/syllabus/ai-ise552-syllabus.pdf",
              originalPath: "notes/ai/syllabus/ai-ise552-syllabus.docx",
              type: "pdf",
              size: "0.11 MB",
              sizeBytes: 113825,
              isConverted: true
            },
            {
              id: "ai-syl-img",
              title: "AI Syllabus Document - High Resolution Capture",
              originalName: "Screenshot 2026-10-06 003549.png",
              path: "notes/ai/syllabus/ai-syllabus-screenshot.png",
              originalPath: null,
              type: "png",
              size: "0.12 MB",
              sizeBytes: 129603,
              isConverted: false
            }
          ]
        }
      ]
    },

    // 2. CN - Computer Networks
    {
      id: "cn",
      code: "IS53",
      name: "Computer Networks",
      shortName: "CN",
      credits: "3:0:0 (Pending Dept Confirmation)",
      isCreditPending: true,
      contactHours: "40 Hours (Approx)",
      coordinator: "ISE Department Faculty",
      prerequisites: "Data Communications, Basic Networking",
      status: "full_notes",
      accent: {
        primary: "#06B6D4",
        secondary: "#22D3EE",
        subtle: "rgba(6, 182, 212, 0.12)",
        glow: "rgba(6, 182, 212, 0.28)"
      },
      tags: ["Core ISE", "Systems & Networking"],
      description: "Network architectures, OSI & TCP/IP models, Physical and Data Link protocols, network addressing, routing algorithms, transport layer reliable transmission, and application services.",
      units: [
        {
          id: "cn-unit1",
          unitNumber: 1,
          title: "Unit 1: Introduction to Computer Networks & Data Link Layer",
          topics: "Network architectures, OSI reference model, TCP/IP protocol suite, physical layer transmission media, data link layer framing, error detection & correction, flow control mechanisms.",
          isPractice: false,
          files: [
            {
              id: "cn-u1-pdf",
              title: "IS53 CN Unit 1 Complete Notes",
              originalName: "IS53-CN-Unit1.pdf",
              path: "notes/cn/unit1/is53-cn-unit1.pdf",
              originalPath: null,
              type: "pdf",
              size: "15.72 MB",
              sizeBytes: 16486434,
              isConverted: false
            }
          ]
        },
        {
          id: "cn-unit2",
          unitNumber: 2,
          title: "Unit 2: Network Layer & Routing Protocols",
          topics: "Network layer design issues, IPv4 & IPv6 packet formats, subnetting, CIDR, routing algorithms (Distance Vector, Link State), congestion control principles.",
          isPractice: false,
          files: [
            {
              id: "cn-u2-pdf",
              title: "IS53 CN Unit 2 Complete Notes",
              originalName: "IS53-CN-Unit2.pdf",
              path: "notes/cn/unit2/is53-cn-unit2.pdf",
              originalPath: null,
              type: "pdf",
              size: "13.07 MB",
              sizeBytes: 13706981,
              isConverted: false
            }
          ]
        }
      ]
    },

    // 3. EVS - Environmental Studies
    {
      id: "evs",
      code: "HS 510",
      name: "Environmental Studies",
      shortName: "EVS",
      credits: "1:0:0 (Pending Dept Confirmation)",
      isCreditPending: true,
      contactHours: "20 Hours (Approx)",
      coordinator: "Humanities & Sciences Dept",
      prerequisites: "Nil",
      status: "full_notes",
      accent: {
        primary: "#10B981",
        secondary: "#34D399",
        subtle: "rgba(16, 185, 129, 0.12)",
        glow: "rgba(16, 185, 129, 0.28)"
      },
      tags: ["Mandatory Course", "Sustainability & Ecology"],
      description: "Ecosystem structure and biodiversity conservation, renewable & non-renewable natural resources, environmental pollution, social issues, climate change, and human population impact.",
      units: [
        {
          id: "evs-unit1",
          unitNumber: 1,
          title: "Unit 1: Ecosystems & Biodiversity",
          topics: "Concept of an ecosystem, ecological succession, food chains, food webs, ecological pyramids, biodiversity values and threats, conservation of biodiversity.",
          isPractice: false,
          files: [
            {
              id: "evs-u1-pdf",
              title: "Unit 1: Ecosystems & Biodiversity Presentation Notes",
              originalName: "Unit-1.pptx",
              path: "notes/evs/unit1/unit-1.pdf",
              originalPath: "notes/evs/unit1/unit-1.pptx",
              type: "pdf",
              size: "2.15 MB",
              sizeBytes: 2256187,
              isConverted: true
            }
          ]
        },
        {
          id: "evs-unit2",
          unitNumber: 2,
          title: "Unit 2: Natural Resources & Conservation",
          topics: "Forest resources, water resources distribution, mineral extraction impacts, food resources and modern agriculture, land degradation, soil erosion and desertification.",
          isPractice: false,
          files: [
            {
              id: "evs-u2-overview-pdf",
              title: "Unit 2: Natural Resources Presentation Overview",
              originalName: "Unit-2.pptx",
              path: "notes/evs/unit2/unit-2.pdf",
              originalPath: "notes/evs/unit2/unit-2.pptx",
              type: "pdf",
              size: "1.57 MB",
              sizeBytes: 1651484,
              isConverted: true
            },
            {
              id: "evs-u2-forest",
              title: "Forest Resources & Ecological Importance of Forests",
              originalName: "1. Unit-2 Forest resources - Ecological importance of forests - Copy.pdf",
              path: "notes/evs/unit2/unit-2-forest-resources.pdf",
              originalPath: null,
              type: "pdf",
              size: "0.32 MB",
              sizeBytes: 339179,
              isConverted: false
            },
            {
              id: "evs-u2-water",
              title: "Water Resources & Global Distribution Assessment",
              originalName: "2. Unit-2 Water resources - Global water resources distribution.pdf",
              path: "notes/evs/unit2/unit-2-water-resources.pdf",
              originalPath: null,
              type: "pdf",
              size: "0.30 MB",
              sizeBytes: 316208,
              isConverted: false
            },
            {
              id: "evs-u2-mineral",
              title: "Mineral Resources & Extraction Environmental Effects",
              originalName: "3. Unit-2 Mineral resources - Environmental effects of extracting and processing of mineral resources.pdf",
              path: "notes/evs/unit2/unit-2-mineral-resources.pdf",
              originalPath: null,
              type: "pdf",
              size: "0.26 MB",
              sizeBytes: 269287,
              isConverted: false
            },
            {
              id: "evs-u2-food",
              title: "Food Resources & Environmental Effects of Modern Agriculture",
              originalName: "4. Unit-2 Food resources - Effects of modern agriculture.pdf",
              path: "notes/evs/unit2/unit-2-food-resources.pdf",
              originalPath: null,
              type: "pdf",
              size: "0.26 MB",
              sizeBytes: 273094,
              isConverted: false
            },
            {
              id: "evs-u2-land",
              title: "Land Resources: Soil Erosion & Desertification",
              originalName: "5. Unit-2 Land resources - Soil erosion and Desertification.pdf",
              path: "notes/evs/unit2/unit-2-land-resources.pdf",
              originalPath: null,
              type: "pdf",
              size: "0.29 MB",
              sizeBytes: 299829,
              isConverted: false
            }
          ]
        },
        {
          id: "evs-unit3",
          unitNumber: 3,
          title: "Unit 3: Environmental Pollution & Control",
          topics: "Causes, effects and control of air, water, soil, marine, noise, and thermal pollution. Solid waste management and disaster management.",
          isPractice: false,
          files: [
            {
              id: "evs-u3-pdf",
              title: "Unit 3: Environmental Pollution & Control Presentation Notes",
              originalName: "Unit-3.pptx",
              path: "notes/evs/unit3/unit-3.pdf",
              originalPath: "notes/evs/unit3/unit-3.pptx",
              type: "pdf",
              size: "1.70 MB",
              sizeBytes: 1783149,
              isConverted: true
            }
          ]
        },
        {
          id: "evs-unit4",
          unitNumber: 4,
          title: "Unit 4: Social Issues & The Environment",
          topics: "Sustainable development, urban energy issues, water conservation, rain water harvesting, watershed management, environmental ethics, and climate change.",
          isPractice: false,
          files: [
            {
              id: "evs-u4-pdf",
              title: "Unit 4: Social Issues & The Environment Presentation Notes",
              originalName: "Unit-4.pptx",
              path: "notes/evs/unit4/unit-4.pdf",
              originalPath: "notes/evs/unit4/unit-4.pptx",
              type: "pdf",
              size: "3.34 MB",
              sizeBytes: 3505326,
              isConverted: true
            }
          ]
        },
        {
          id: "evs-unit5",
          unitNumber: 5,
          title: "Unit 5: Human Population & The Environment",
          topics: "Population growth and variations, population explosion, environment and human health, human rights, value education, HIV/AIDS, women and child welfare, role of IT in environment and health.",
          isPractice: false,
          files: [
            {
              id: "evs-u5-pdf",
              title: "Unit 5: Human Population & The Environment Presentation Notes",
              originalName: "Unit-5.pptx",
              path: "notes/evs/unit5/unit-5.pdf",
              originalPath: "notes/evs/unit5/unit-5.pptx",
              type: "pdf",
              size: "1.22 MB",
              sizeBytes: 1283697,
              isConverted: true
            }
          ]
        },
        {
          id: "evs-practice",
          unitNumber: "Practice",
          title: "Practice & Continuous Internal Assessment",
          topics: "Official test papers, portion reviews (L1-L6), Bloom's taxonomy distribution, and question formats.",
          isPractice: true,
          files: [
            {
              id: "evs-cie1-qp",
              title: "EVS CIE-1 Internal Assessment Question Paper (2024–2025)",
              originalName: "EVS_CIE1_QP-2024 (1).docx",
              path: "notes/evs/practice/evs-cie1-qp-2024.pdf",
              originalPath: "notes/evs/practice/evs-cie1-qp-2024.docx",
              type: "pdf",
              size: "0.12 MB",
              sizeBytes: 124985,
              isConverted: true
            }
          ]
        }
      ]
    },

    // 4. ML - Machine Learning
    {
      id: "ml",
      code: "ISE554",
      name: "Machine Learning",
      shortName: "ML",
      credits: "3:0:0 (Pending Dept Confirmation)",
      isCreditPending: true,
      contactHours: "42 Hours (Approx)",
      coordinator: "ISE Department Faculty",
      prerequisites: "Python Programming, Linear Algebra, Probability",
      status: "full_notes",
      accent: {
        primary: "#F97316",
        secondary: "#FB923C",
        subtle: "rgba(249, 115, 22, 0.12)",
        glow: "rgba(249, 115, 22, 0.28)"
      },
      tags: ["Core ISE", "Data Science & AI"],
      description: "Supervised and unsupervised learning, decision trees, artificial neural networks, Bayesian classifiers, regression methodologies, algorithm execution pipelines, and evaluation metrics.",
      units: [
        {
          id: "ml-unit1",
          unitNumber: 1,
          title: "Unit 1: Introduction to Machine Learning & Concept Learning",
          topics: "Well-posed learning problems, designing a learning system, perspective and issues in machine learning, concept learning task, Find-S algorithm, version spaces and candidate elimination algorithm, inductive bias.",
          isPractice: false,
          files: [
            {
              id: "ml-u1-pdf",
              title: "ML Unit 1: Introduction & Concept Learning Notes",
              originalName: "Unit 1.pdf",
              path: "notes/ml/unit1/unit-1.pdf",
              originalPath: null,
              type: "pdf",
              size: "2.39 MB",
              sizeBytes: 2508842,
              isConverted: false
            }
          ]
        },
        {
          id: "ml-unit2",
          unitNumber: 2,
          title: "Unit 2: Decision Trees & Neural Networks",
          topics: "Decision tree representation, ID3 algorithm, entropy, information gain, pruning, neural network representations, perceptrons, multi-layer networks and backpropagation algorithm.",
          isPractice: false,
          files: [
            {
              id: "ml-u2-pdf",
              title: "ML Unit 2: Decision Tree Learning & Artificial Neural Networks",
              originalName: "Unit 2.pdf",
              path: "notes/ml/unit2/unit-2.pdf",
              originalPath: null,
              type: "pdf",
              size: "2.03 MB",
              sizeBytes: 2132489,
              isConverted: false
            }
          ]
        },
        {
          id: "ml-unit3",
          unitNumber: 3,
          title: "Unit 3: Regression Techniques & Algorithm Execution",
          topics: "Linear regression, polynomial regression, cost functions, gradient descent optimization, step-by-step workflow for executing machine learning algorithms on real datasets.",
          isPractice: false,
          files: [
            {
              id: "ml-u3-poly-pdf",
              title: "Unit 3: Polynomial Regression & Mathematical Formulation",
              originalName: "Unit 3(Polynomial Regression).pdf",
              path: "notes/ml/unit3/unit-3-polynomial-regression.pdf",
              originalPath: null,
              type: "pdf",
              size: "0.71 MB",
              sizeBytes: 740320,
              isConverted: false
            },
            {
              id: "ml-u3-steps-pdf",
              title: "Unit 3: Step-by-Step Implementation Guide for ML Algorithms",
              originalName: "Unit 3(Steps for MLalg).pdf",
              path: "notes/ml/unit3/unit-3-steps-for-mlalg.pdf",
              originalPath: null,
              type: "pdf",
              size: "89.5 KB",
              sizeBytes: 91608,
              isConverted: false
            }
          ]
        },
        {
          id: "ml-practice",
          unitNumber: "Practice",
          title: "Practice & Examination Question Banks",
          topics: "Unit-wise question banks, numerical problems on Find-S and Candidate Elimination, decision tree derivations, and exam preparation questions.",
          isPractice: true,
          files: [
            {
              id: "ml-u1-qb",
              title: "ML Unit 1: Comprehensive Question Bank (QB)",
              originalName: "Unit 1(QB).pdf",
              path: "notes/ml/practice/unit-1-qb.pdf",
              originalPath: null,
              type: "pdf",
              size: "4.04 MB",
              sizeBytes: 4237370,
              isConverted: false
            }
          ]
        }
      ]
    },

    // 5. REACT_JS - Front end Development using ReactJS
    {
      id: "reactjs",
      code: "ISAEC594",
      name: "Front end Development using ReactJS",
      shortName: "ReactJS",
      credits: "1:0:0:1",
      contactHours: "15L + 15S",
      coordinator: "J R Shruti",
      prerequisites: "HTML, CSS, and JavaScript",
      status: "syllabus_only",
      accent: {
        primary: "#3B82F6",
        secondary: "#60A5FA",
        subtle: "rgba(59, 130, 246, 0.12)",
        glow: "rgba(59, 130, 246, 0.28)"
      },
      tags: ["AEC Elective", "Web Development", "Frontend Track"],
      description: "Modern declarative user interfaces, React philosophy, JSX compilation, component lifecycles, state and prop management, SyntheticEvents, controlled forms, and lifting state.",
      notesNotice: "Notes coming soon. The complete 3-unit syllabus transcribed from the official course outline with all documentation links and delivery tools is presented below.",
      syllabus: {
        textbook: {
          title: "Official React Documentation & Modern React Guides",
          edition: "React 18 / 19",
          authors: "React Core Team",
          publisher: "Meta Open Source"
        },
        referenceBooks: [
          {
            title: "Learning React: Modern Patterns for Developing React Apps",
            edition: "2nd Edition",
            authors: "Alex Banks and Eve Porcello",
            publisher: "O'Reilly Media"
          }
        ],
        pedagogyMethod: "Chalk and talk, PowerPoint Presentations, Live Coding Sessions, Demonstrations, and Hands-on Practice in Lab.",
        units: [
          {
            unitNumber: 1,
            title: "Unit I: Introduction to React and JSX",
            topics: "Introduction to React: Features of React, React Philosophy (Declarative UI, Component-Based Architecture, One-Way Data Flow), Virtual DOM, React vs. Other Frameworks (Angular, Vue), Setting up React Environment (Node.js, npm, Vite), Project Structure, Introduction to JSX: JSX Syntax, Embedding Expressions, Conditional Rendering, JSX Compilation with Babel & JSX Transform.",
            pedagogy: "PowerPoint Presentations, Live Coding Sessions, Demonstrations, Hands-on Practice.",
            links: [
              { label: "React Docs: Introducing JSX", url: "https://legacy.reactjs.org/docs/introducing-jsx.html" },
              { label: "React Native: Introduction to React", url: "https://reactnative.dev/docs/next/intro-react" }
            ]
          },
          {
            unitNumber: 2,
            title: "Unit II: Components, Props and State",
            topics: "Components: Functional Components, Overview of Class Components, Creating and Rendering Components, Passing & Accessing Props, Props vs. State, React Fragments, this.props.children, Introduction to State using useState, Rendering Components.",
            pedagogy: "Chalk and talk, PowerPoint Presentations, Live Coding Sessions, Demonstrations, Hands-on Practice.",
            links: [
              { label: "React Native: Core Components", url: "https://reactnative.dev/docs/next/intro-react" },
              { label: "React Docs: Components and Props", url: "https://legacy.reactjs.org/docs/components-and-props.html" },
              { label: "React Docs: React Component API", url: "https://legacy.reactjs.org/docs/react-component.html" }
            ]
          },
          {
            unitNumber: 3,
            title: "Unit III: Events and Form Handling",
            topics: "Handling Events in React: SyntheticEvent, Arrow Functions, bind(), Event Handling in Functional and Class Components, Controlled and Uncontrolled Components (Overview), Controlled Inputs (Forms), Form Elements: input, textarea, select, Lifting State Up.",
            pedagogy: "Chalk and talk, PowerPoint Presentations, Live Coding Sessions, Demonstrations, Hands-on Practice.",
            links: [
              { label: "React Docs: Handling Events", url: "https://legacy.reactjs.org/docs/handling-events.html" },
              { label: "freeCodeCamp: How to Handle Events in React", url: "https://www.freecodecamp.org/news/how-to-handle-events-in-react/" },
              { label: "Scaler Topics: React Event Handling Deep Dive", url: "https://www.scaler.com/topics/react/event-handling-in-react/" },
              { label: "AngularMinds Guide: Best Practices of Form Handling & Event Binding", url: "https://www.angularminds.com/blog/best-practices-of-form-handling-and-event-binding-in-react" }
            ]
          }
        ]
      },
      units: [
        {
          id: "react-syllabus-unit",
          unitNumber: "Syllabus",
          title: "Official Syllabus Document",
          isPractice: false,
          files: [
            {
              id: "react-syl-img",
              title: "ReactJS ISAEC594 Syllabus Official Outline",
              originalName: "Screenshot 2026-10-06 004002.png",
              path: "notes/reactjs/syllabus/reactjs-syllabus-screenshot.png",
              originalPath: null,
              type: "png",
              size: "0.47 MB",
              sizeBytes: 492109,
              isConverted: false
            }
          ]
        }
      ]
    },

    // 6. RMIPR - Research Methodology & IPR
    {
      id: "rmipr",
      code: "ISE555",
      name: "Research Methodology & Intellectual Property Rights",
      shortName: "RM & IPR",
      credits: "2:0:0 (Pending Dept Confirmation)",
      isCreditPending: true,
      contactHours: "28 Hours (Approx)",
      coordinator: "ISE Department Faculty",
      prerequisites: "Basic Technical Writing & Analytical Skills",
      status: "full_notes",
      accent: {
        primary: "#EC4899",
        secondary: "#F472B6",
        subtle: "rgba(236, 72, 153, 0.12)",
        glow: "rgba(236, 72, 153, 0.28)"
      },
      tags: ["Professional Development", "Research & Patents"],
      description: "Research formulation, literature review methodologies, hypothesis testing, experimental design, patents, copyrights, trademarks, licensing, and trade secrets.",
      units: [
        {
          id: "rmipr-unit1",
          unitNumber: 1,
          title: "Unit 1: Research Methodology Fundamentals & Problem Formulation",
          topics: "Meaning of research, objectives of research, motivation in research, types of research, research approaches, significance of research, research methods versus methodology, research and scientific method, research process, criteria of good research, defining the research problem.",
          isPractice: false,
          files: [
            {
              id: "rmipr-u1-pdf",
              title: "RM & IPR Unit 1 Complete Presentation Notes",
              originalName: "RM & IPR Unit 1 PPT (1).pptx",
              path: "notes/rmipr/unit1/rm-ipr-unit1.pdf",
              originalPath: "notes/rmipr/unit1/rm-ipr-unit1.pptx",
              type: "pdf",
              size: "0.64 MB",
              sizeBytes: 674560,
              isConverted: true
            }
          ]
        },
        {
          id: "rmipr-unit2",
          unitNumber: 2,
          title: "Unit 2: Research Design & Intellectual Property Rights",
          topics: "Need for research design, features of a good design, important concepts relating to research design, basic principles of experimental designs, introduction to IPR, patent laws, patent filing, copyrights and infringement.",
          isPractice: false,
          files: [
            {
              id: "rmipr-u2-pdf",
              title: "RM & IPR Unit 2 Complete Presentation Notes",
              originalName: "Unit 2 ppt.pptx",
              path: "notes/rmipr/unit2/rm-ipr-unit2.pdf",
              originalPath: "notes/rmipr/unit2/rm-ipr-unit2.pptx",
              type: "pdf",
              size: "1.26 MB",
              sizeBytes: 1319874,
              isConverted: true
            }
          ]
        }
      ]
    },

    // 7. SE - Software Engineering
    {
      id: "se",
      code: "IS52",
      name: "Software Engineering",
      shortName: "SE",
      credits: "3:0:0 (Pending Dept Confirmation)",
      isCreditPending: true,
      contactHours: "40 Hours (Approx)",
      coordinator: "ISE Department Faculty",
      prerequisites: "Object-Oriented Programming, Data Structures",
      status: "full_notes",
      accent: {
        primary: "#6366F1",
        secondary: "#818CF8",
        subtle: "rgba(99, 102, 241, 0.12)",
        glow: "rgba(99, 102, 241, 0.28)"
      },
      tags: ["Core ISE", "Software Development Lifecycle"],
      description: "Software processes, Agile methodologies, requirements engineering, system modeling, architectural design, software testing, maintenance, and project management.",
      units: [
        {
          id: "se-unit1",
          unitNumber: 1,
          title: "Unit 1: Software Processes, Agile Development & Requirements Engineering",
          topics: "Unit 1.1: Professional software development, software processes and process models. Unit 1.2: Agile software development, agile methods, plan-driven vs agile, Extreme Programming, Scrum. Unit 1.3: Requirements engineering, functional and non-functional requirements, requirement specification, validation.",
          isPractice: false,
          files: [
            {
              id: "se-u1-1-pdf",
              title: "Unit 1.1: Software Processes & SDLC Models",
              originalName: "Unit 1.1.pptx",
              path: "notes/se/unit1/unit-1-1.pdf",
              originalPath: "notes/se/unit1/unit-1-1.pptx",
              type: "pdf",
              size: "0.30 MB",
              sizeBytes: 313186,
              isConverted: true
            },
            {
              id: "se-u1-2-pdf",
              title: "Unit 1.2: Agile Software Development & Scrum",
              originalName: "Unit 1.2.pptx",
              path: "notes/se/unit1/unit-1-2.pdf",
              originalPath: "notes/se/unit1/unit-1-2.pptx",
              type: "pdf",
              size: "0.71 MB",
              sizeBytes: 739555,
              isConverted: true
            },
            {
              id: "se-u1-3-pdf",
              title: "Unit 1.3: Requirements Engineering & System Modeling",
              originalName: "Unit 1.3.pptx",
              path: "notes/se/unit1/unit-1-3.pdf",
              originalPath: "notes/se/unit1/unit-1-3.pptx",
              type: "pdf",
              size: "0.52 MB",
              sizeBytes: 550417,
              isConverted: true
            }
          ]
        },
        {
          id: "se-unit2",
          unitNumber: 2,
          title: "Unit 2: Architectural Design & Implementation",
          topics: "Architectural design decisions, architectural views, architectural patterns (layered, repository, client-server, pipe and filter), application architectures, object-oriented design using UML.",
          isPractice: false,
          files: [
            {
              id: "se-u2-pdf",
              title: "Unit 2: Architectural Design & System Architecture Notes",
              originalName: "Unit 2.pptx",
              path: "notes/se/unit2/unit-2.pdf",
              originalPath: "notes/se/unit2/unit-2.pptx",
              type: "pdf",
              size: "0.40 MB",
              sizeBytes: 416031,
              isConverted: true
            }
          ]
        }
      ]
    },

    // 8. TOC - Theory of Computation
    {
      id: "toc",
      code: "IS51",
      name: "Theory of Computation",
      shortName: "TOC",
      credits: "3:0:0 (Pending Dept Confirmation)",
      isCreditPending: true,
      contactHours: "42 Hours (Approx)",
      coordinator: "ISE Department Faculty",
      prerequisites: "Discrete Mathematical Structures",
      status: "full_notes",
      accent: {
        primary: "#F59E0B",
        secondary: "#FBBF24",
        subtle: "rgba(245, 158, 11, 0.12)",
        glow: "rgba(245, 158, 11, 0.28)"
      },
      tags: ["Core Theoretical CS", "Automata & Grammars"],
      description: "Automata theory, deterministic and non-deterministic finite automata, regular expressions, pumping lemma, context-free grammars, pushdown automata, Turing machines, and undecidability.",
      units: [
        {
          id: "toc-unit1",
          unitNumber: 1,
          title: "Unit 1: Introduction to Finite Automata & Regular Expressions",
          topics: "Central concepts of automata theory, DFA definition, transition tables, state diagrams, NFA with and without epsilon transitions, equivalence of DFA and NFA, conversion of NFA to DFA, regular expressions.",
          isPractice: false,
          files: [
            {
              id: "toc-u1-main",
              title: "Unit 1: Finite Automata & Regular Expressions (Comprehensive)",
              originalName: "Unit 1.pdf",
              path: "notes/toc/unit1/unit-1.pdf",
              originalPath: null,
              type: "pdf",
              size: "22.38 MB",
              sizeBytes: 23471151,
              isConverted: false,
              isAlternate: false
            },
            {
              id: "toc-u1-alt",
              title: "Unit 1 & 2: Alternate / Condensed Notes (Part 1)",
              originalName: "Toc unit 1 and 2.pdf",
              path: "notes/toc/unit1/toc-unit-1-and-2-alternate.pdf",
              originalPath: null,
              type: "pdf",
              size: "5.57 MB",
              sizeBytes: 5845150,
              isConverted: false,
              isAlternate: true,
              alternateLabel: "Alternate / Condensed Notes"
            }
          ]
        },
        {
          id: "toc-unit2",
          unitNumber: 2,
          title: "Unit 2: Properties of Regular Languages & Pumping Lemma",
          topics: "Proving languages not to be regular using Pumping Lemma, closure properties of regular languages, decision properties of regular languages, equivalence and minimization of automata.",
          isPractice: false,
          files: [
            {
              id: "toc-u2-main",
              title: "Unit 2: Regular Languages & Pumping Lemma (Comprehensive)",
              originalName: "Unit 2.pdf",
              path: "notes/toc/unit2/unit-2.pdf",
              originalPath: null,
              type: "pdf",
              size: "10.97 MB",
              sizeBytes: 11498155,
              isConverted: false,
              isAlternate: false
            }
          ]
        },
        {
          id: "toc-unit3",
          unitNumber: 3,
          title: "Unit 3: Context-Free Grammars & Pushdown Automata",
          topics: "Context-Free Grammars (CFG), parse trees, ambiguity in grammars and languages, Pushdown Automata (PDA) definition, languages of a PDA, equivalence of PDA and CFG, deterministic PDA.",
          isPractice: false,
          files: [
            {
              id: "toc-u3-main",
              title: "Unit 3: CFGs & Pushdown Automata (Comprehensive)",
              originalName: "Unit 3.pdf",
              path: "notes/toc/unit3/unit-3.pdf",
              originalPath: null,
              type: "pdf",
              size: "23.56 MB",
              sizeBytes: 24704030,
              isConverted: false,
              isAlternate: false
            },
            {
              id: "toc-u3-alt",
              title: "Unit 3: Alternate / Condensed Notes",
              originalName: "TOC_ unit3.pdf",
              path: "notes/toc/unit3/toc-unit3-alternate.pdf",
              originalPath: null,
              type: "pdf",
              size: "2.65 MB",
              sizeBytes: 2781833,
              isConverted: false,
              isAlternate: true,
              alternateLabel: "Alternate / Condensed Notes"
            }
          ]
        },
        {
          id: "toc-unit4",
          unitNumber: 4,
          title: "Unit 4: Properties of CFLs & Introduction to Turing Machines",
          topics: "Normal forms for CFGs (CNF, GNF), pumping lemma for CFLs, closure and decision properties of CFLs, Turing Machine model, definition, instantaneous descriptions, transition diagrams.",
          isPractice: false,
          files: [
            {
              id: "toc-u4-main",
              title: "Unit 4: Properties of CFLs & Turing Machines (Comprehensive)",
              originalName: "Unit 4.pdf",
              path: "notes/toc/unit4/unit-4.pdf",
              originalPath: null,
              type: "pdf",
              size: "2.62 MB",
              sizeBytes: 2743614,
              isConverted: false,
              isAlternate: false
            }
          ]
        },
        {
          id: "toc-unit5",
          unitNumber: 5,
          title: "Unit 5: Undecidability & Computational Complexity",
          topics: "Undecidability, the halting problem, post correspondence problem, recursively enumerable languages, Chomsky hierarchy, classes P and NP, introduction to NP-completeness.",
          isPractice: false,
          files: [
            {
              id: "toc-u5-main",
              title: "Unit 5: Undecidability & Complexity Classes (Comprehensive)",
              originalName: "Unit 5.pdf",
              path: "notes/toc/unit5/unit-5.pdf",
              originalPath: null,
              type: "pdf",
              size: "4.24 MB",
              sizeBytes: 4446567,
              isConverted: false,
              isAlternate: false
            }
          ]
        }
      ]
    }
  ]
};
