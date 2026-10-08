"""
generate_ai_u2_assets.py - Generates theme-aware SVGs for AI Unit 2 notes:
- Figure 2.1: A* Graph Search Expansion Tree with g, h, f values (Audit Verified: Cost = 8)
- Figure 2.2: 8-Puzzle State Search Space under A* with h1 Misplaced Tiles (Ramaiah CIE-1 Q2.b)
- Figure 2.3: Simulated Annealing Energy Landscape & Boltzmann Acceptance Curve P = exp(dE/T)
"""

def generate_astar_search_tree_svg():
    """Figure 2.1: A* Graph Search Expansion Tree with f(n) = g(n) + h(n)"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A* Graph Search Expansion Tree">
  <defs>
    <marker id="ast-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink-muted)" />
    </marker>
    <marker id="ast-arr-opt" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--green)" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">A* GRAPH SEARCH TRACE &bull; OPTIMAL PATH: S &rarr; A &rarr; B &rarr; C &rarr; D &rarr; G [COST = 8]</text>

  <!-- Graph on Left (S, A, B, C, D, G) -->
  <g transform="translate(30, 50)">
    <rect width="270" height="265" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="135" y="24" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--brand)" text-anchor="middle">PHYSICAL WEIGHTED GRAPH</text>

    <!-- Edge Lines -->
    <!-- S to A (c=1), S to B (c=4) -->
    <line x1="50" y1="75" x2="135" y2="75" stroke="var(--green)" stroke-width="2.5" />
    <text x="92" y="68" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)">1</text>

    <line x1="50" y1="75" x2="50" y2="165" stroke="var(--ink-muted)" stroke-width="1.5" />
    <text x="35" y="125" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)">4</text>

    <!-- A to B (c=2), A to C (c=5), A to D (c=12) -->
    <line x1="135" y1="75" x2="50" y2="165" stroke="var(--green)" stroke-width="2.5" />
    <text x="96" y="115" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)">2</text>

    <line x1="135" y1="75" x2="135" y2="165" stroke="var(--ink-muted)" stroke-width="1.5" />
    <text x="145" y="125" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)">5</text>

    <!-- B to C (c=2) -->
    <line x1="50" y1="165" x2="135" y2="165" stroke="var(--green)" stroke-width="2.5" />
    <text x="92" y="158" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)">2</text>

    <!-- C to D (c=2), C to G (c=4) -->
    <line x1="135" y1="165" x2="220" y2="165" stroke="var(--green)" stroke-width="2.5" />
    <text x="175" y="158" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)">2</text>

    <line x1="135" y1="165" x2="220" y2="235" stroke="var(--ink-muted)" stroke-width="1.5" />
    <text x="170" y="210" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)">4</text>

    <!-- D to G (c=1) -->
    <line x1="220" y1="165" x2="220" y2="235" stroke="var(--green)" stroke-width="2.5" />
    <text x="232" y="205" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)">1</text>

    <!-- Nodes -->
    <!-- Node S -->
    <circle cx="50" cy="75" r="16" fill="var(--surface)" stroke="var(--brand)" stroke-width="2" />
    <text x="50" y="79" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--brand)" text-anchor="middle">S</text>
    <text x="50" y="103" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">h=7</text>

    <!-- Node A -->
    <circle cx="135" cy="75" r="16" fill="var(--surface)" stroke="var(--green)" stroke-width="2" />
    <text x="135" y="79" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">A</text>
    <text x="135" y="52" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">h=6</text>

    <!-- Node B -->
    <circle cx="50" cy="165" r="16" fill="var(--surface)" stroke="var(--green)" stroke-width="2" />
    <text x="50" y="169" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">B</text>
    <text x="50" y="193" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">h=4</text>

    <!-- Node C -->
    <circle cx="135" cy="165" r="16" fill="var(--surface)" stroke="var(--green)" stroke-width="2" />
    <text x="135" y="169" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">C</text>
    <text x="135" y="193" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">h=2</text>

    <!-- Node D -->
    <circle cx="220" cy="165" r="16" fill="var(--surface)" stroke="var(--green)" stroke-width="2" />
    <text x="220" y="169" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">D</text>
    <text x="220" y="145" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">h=1</text>

    <!-- Node G -->
    <circle cx="220" cy="235" r="16" fill="var(--green-tint)" stroke="var(--green)" stroke-width="2.5" />
    <text x="220" y="239" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">G</text>
    <text x="220" y="260" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="var(--green)" text-anchor="middle">h=0</text>
  </g>

  <!-- Priority Queue & Expansion Flow on Right -->
  <g transform="translate(325, 50)">
    <rect width="430" height="265" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="215" y="24" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--ink)" text-anchor="middle">A* SEARCH EXPANSION TREE WITH f(n) = g(n) + h(n)</text>

    <!-- Step 1: Root S -->
    <g transform="translate(160, 40)">
      <rect width="110" height="34" rx="6" fill="var(--surface)" stroke="var(--brand)" stroke-width="1.5" />
      <text x="55" y="17" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">S: g=0, h=7</text>
      <text x="55" y="29" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--brand)" text-anchor="middle">f = 7</text>
    </g>

    <!-- Branches from S to A and B -->
    <line x1="190" y1="75" x2="110" y2="105" stroke="var(--green)" stroke-width="2" marker-end="url(#ast-arr-opt)" />
    <line x1="240" y1="75" x2="310" y2="105" stroke="var(--ink-muted)" stroke-width="1.2" marker-end="url(#ast-arr)" />

    <!-- Step 2: Node A and Node B (direct from S) -->
    <g transform="translate(55, 105)">
      <rect width="110" height="34" rx="6" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.5" />
      <text x="55" y="17" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">A: g=1, h=6</text>
      <text x="55" y="29" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--green)" text-anchor="middle">f = 7 (POPPED)</text>
    </g>

    <g transform="translate(260, 105)">
      <rect width="110" height="34" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.2" />
      <text x="55" y="17" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">B: g=4, h=4</text>
      <text x="55" y="29" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">f = 8 (Delayed)</text>
    </g>

    <!-- Step 3: Successors from A -> B (via A) and C (via A) -->
    <line x1="110" y1="140" x2="110" y2="165" stroke="var(--green)" stroke-width="2" marker-end="url(#ast-arr-opt)" />
    <g transform="translate(55, 165)">
      <rect width="110" height="34" rx="6" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.5" />
      <text x="55" y="17" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">B: g=3, h=4</text>
      <text x="55" y="29" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--green)" text-anchor="middle">f = 7 (POPPED)</text>
    </g>

    <!-- Step 4: From B to C -->
    <line x1="165" y1="182" x2="200" y2="182" stroke="var(--green)" stroke-width="2" marker-end="url(#ast-arr-opt)" />
    <g transform="translate(200, 165)">
      <rect width="105" height="34" rx="6" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.5" />
      <text x="52" y="17" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">C: g=5, h=2</text>
      <text x="52" y="29" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--green)" text-anchor="middle">f = 7 (POPPED)</text>
    </g>

    <!-- Step 5: From C to D and G -->
    <line x1="252" y1="200" x2="252" y2="225" stroke="var(--green)" stroke-width="2" marker-end="url(#ast-arr-opt)" />
    <g transform="translate(200, 225)">
      <rect width="105" height="34" rx="6" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.5" />
      <text x="52" y="17" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">D: g=7, h=1</text>
      <text x="52" y="29" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--green)" text-anchor="middle">f = 8 (POPPED)</text>
    </g>

    <!-- Step 6: From D to Goal G -->
    <line x1="305" y1="242" x2="330" y2="242" stroke="var(--green)" stroke-width="2.5" marker-end="url(#ast-arr-opt)" />
    <g transform="translate(330, 225)">
      <rect width="90" height="34" rx="6" fill="var(--green)" stroke="var(--green-hover)" stroke-width="2" />
      <text x="45" y="17" font-family="var(--font-mono)" font-size="10.5" font-weight="800" fill="var(--green-ink)" text-anchor="middle">G: g=8, h=0</text>
      <text x="45" y="29" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--green-ink)" text-anchor="middle">f = 8 &check; GOAL</text>
    </g>
  </g>
</svg>'''

def generate_eight_puzzle_search_svg():
    """Figure 2.2: 8-Puzzle A* Search Tree with h1 (Misplaced Tiles) - Ramaiah CIE-1 Q2.b"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="8-Puzzle A* Search State Tree with Misplaced Tiles Heuristic">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">8-PUZZLE A* SEARCH TREE &bull; HEURISTIC h₁(n) = MISPLACED TILES (RAMAIAH CIE-1 Q2.b)</text>

  <!-- Root Start State (Depth 0) -->
  <g transform="translate(325, 50)">
    <rect width="130" height="70" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="65" y="20" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">START STATE (g=0)</text>
    <!-- Mini 3x3 Grid representation -->
    <text x="65" y="38" font-family="var(--font-mono)" font-size="11" fill="var(--ink)" text-anchor="middle">[ 2  8  3 ]</text>
    <text x="65" y="50" font-family="var(--font-mono)" font-size="11" fill="var(--ink)" text-anchor="middle">[ 1  _  4 ]</text>
    <text x="65" y="62" font-family="var(--font-mono)" font-size="11" fill="var(--ink)" text-anchor="middle">[ 7  6  5 ]</text>
    <text x="65" y="82" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">h₁=4, f = 0+4 = 4</text>
  </g>

  <!-- Connecting Lines from Root to Depth 1 (4 actions: UP, DOWN, LEFT, RIGHT) -->
  <line x1="340" y1="135" x2="110" y2="160" stroke="var(--ink-muted)" stroke-width="1.2" />
  <line x1="370" y1="135" x2="280" y2="160" stroke="var(--green)" stroke-width="2.5" />
  <line x1="410" y1="135" x2="500" y2="160" stroke="var(--ink-muted)" stroke-width="1.2" />
  <line x1="440" y1="135" x2="670" y2="160" stroke="var(--ink-muted)" stroke-width="1.2" />

  <!-- Action Labels -->
  <text x="195" y="145" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">UP (slide 8 down)</text>
  <text x="310" y="145" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--green)">LEFT (slide 1 right)</text>
  <text x="465" y="145" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">RIGHT (slide 4 left)</text>
  <text x="590" y="145" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">DOWN (slide 6 up)</text>

  <!-- Child 1: Move UP -->
  <g transform="translate(45, 165)">
    <rect width="130" height="70" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="65" y="20" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--ink-muted)" text-anchor="middle">MOVE UP</text>
    <text x="65" y="38" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 2  _  3 ]</text>
    <text x="65" y="50" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 1  8  4 ]</text>
    <text x="65" y="62" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 7  6  5 ]</text>
    <text x="65" y="82" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">g=1, h₁=5 &rarr; f=6</text>
  </g>

  <!-- Child 2: Move LEFT (OPTIMAL CANDIDATE - EXPANDED) -->
  <g transform="translate(215, 165)">
    <rect width="130" height="70" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="2" />
    <text x="65" y="20" font-family="var(--font-mono)" font-size="10.5" font-weight="800" fill="var(--green)" text-anchor="middle">MOVE LEFT &starf;</text>
    <text x="65" y="38" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">[ 2  8  3 ]</text>
    <text x="65" y="50" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">[ _  1  4 ]</text>
    <text x="65" y="62" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">[ 7  6  5 ]</text>
    <text x="65" y="82" font-family="var(--font-mono)" font-size="9.5" font-weight="800" fill="var(--green)" text-anchor="middle">g=1, h₁=3 &rarr; f=4 (BEST)</text>
  </g>

  <!-- Child 3: Move RIGHT -->
  <g transform="translate(435, 165)">
    <rect width="130" height="70" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="65" y="20" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--ink-muted)" text-anchor="middle">MOVE RIGHT</text>
    <text x="65" y="38" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 2  8  3 ]</text>
    <text x="65" y="50" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 1  4  _ ]</text>
    <text x="65" y="62" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 7  6  5 ]</text>
    <text x="65" y="82" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">g=1, h₁=5 &rarr; f=6</text>
  </g>

  <!-- Child 4: Move DOWN -->
  <g transform="translate(605, 165)">
    <rect width="130" height="70" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="65" y="20" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--ink-muted)" text-anchor="middle">MOVE DOWN</text>
    <text x="65" y="38" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 2  8  3 ]</text>
    <text x="65" y="50" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 1  6  4 ]</text>
    <text x="65" y="62" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">[ 7  _  5 ]</text>
    <text x="65" y="82" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">g=1, h₁=5 &rarr; f=6</text>
  </g>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(45, 270)">
    <rect width="690" height="48" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="345" y="20" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">A* Priority Queue Decision: Node with minimum f(n) = 4 is popped from OPEN list.</text>
    <text x="345" y="36" font-family="var(--font-mono)" font-size="10" fill="var(--green)" text-anchor="middle">Branches with f=6 are preserved in the Priority Queue and explored only if the f=4 subtree cost escalates.</text>
  </g>
</svg>'''

def generate_simulated_annealing_svg():
    """Figure 2.3: Simulated Annealing Energy Landscape & Boltzmann Acceptance Curve"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Simulated Annealing State Landscape and Temperature Acceptance Curve">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">SIMULATED ANNEALING &bull; ESCAPING LOCAL MAXIMA VIA BOLTZMANN PROBABILITY P = exp(&Delta;E / T)</text>

  <!-- Left: Objective Function Landscape -->
  <g transform="translate(25, 55)">
    <rect width="360" height="260" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="180" y="24" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">STATE SPACE OBJECTIVE LANDSCAPE</text>

    <!-- Axes -->
    <line x1="30" y1="220" x2="330" y2="220" stroke="var(--border-strong)" stroke-width="1.5" />
    <line x1="30" y1="40" x2="30" y2="220" stroke="var(--border-strong)" stroke-width="1.5" />
    <text x="180" y="238" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">State Space Dimension (x)</text>
    <text x="20" y="50" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" transform="rotate(-90 20 50)" text-anchor="end">Objective E(s)</text>

    <!-- Landscape Curve: Local Max, Shoulder, Global Max -->
    <path d="M 30 190 Q 70 180 90 120 Q 110 80 130 130 Q 150 170 170 170 Q 190 170 210 130 Q 240 60 260 50 Q 280 60 300 150 L 330 200" fill="none" stroke="var(--ink)" stroke-width="2.5" />

    <!-- Local Max Annotation -->
    <circle cx="100" cy="98" r="5" fill="#EF4444" />
    <text x="100" y="85" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="#EF4444" text-anchor="middle">Local Maxima</text>

    <!-- Downhill Move Arrow -->
    <path d="M 105 105 Q 125 155 145 150" fill="none" stroke="#EF4444" stroke-width="2" stroke-dasharray="3 2" />
    <text x="145" y="130" font-family="var(--font-mono)" font-size="8.5" fill="#EF4444">&Delta;E &lt; 0 (Downhill)</text>
    <text x="145" y="142" font-family="var(--font-mono)" font-size="8" fill="var(--ink-muted)">Accepted if R &lt; exp(&Delta;E/T)</text>

    <!-- Global Max Annotation -->
    <circle cx="260" cy="50" r="6" fill="var(--green)" />
    <text x="260" y="38" font-family="var(--font-mono)" font-size="10" font-weight="800" fill="var(--green)" text-anchor="middle">GLOBAL MAXIMA &starf;</text>
  </g>

  <!-- Right: Boltzmann Probability Acceptance vs Temperature Curve -->
  <g transform="translate(405, 55)">
    <rect width="350" height="260" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="175" y="24" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--green)" text-anchor="middle">PROBABILITY P(accept &Delta;E = -5) vs TEMPERATURE T</text>

    <!-- Table of Probabilities (Audit Verified) -->
    <g transform="translate(25, 45)">
      <rect width="300" height="110" rx="8" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
      <text x="15" y="22" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">Temperature (T)</text>
      <text x="150" y="22" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">Formula</text>
      <text x="240" y="22" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)">P(Accept)</text>

      <line x1="10" y1="30" x2="290" y2="30" stroke="var(--border)" stroke-width="1" />

      <text x="15" y="48" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">T = 1000 K (Hot)</text>
      <text x="150" y="48" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)">exp(-5 / 1000)</text>
      <text x="240" y="48" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="var(--green)">99.50% &check;</text>

      <text x="15" y="68" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">T = 100 K (Warm)</text>
      <text x="150" y="68" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)">exp(-5 / 100)</text>
      <text x="240" y="68" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="var(--green)">95.12% &check;</text>

      <text x="15" y="88" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">T = 10 K (Cool)</text>
      <text x="150" y="88" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)">exp(-5 / 10)</text>
      <text x="240" y="88" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="var(--brand)">60.65%</text>

      <text x="15" y="104" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">T = 1 K (Cold)</text>
      <text x="150" y="104" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)">exp(-5 / 1)</text>
      <text x="240" y="104" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="#EF4444">0.67% (Greedy)</text>
    </g>

    <!-- Key Takeaway Box -->
    <g transform="translate(25, 170)">
      <rect width="300" height="75" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.2" />
      <text x="150" y="22" font-family="var(--font-mono)" font-size="10" font-weight="800" fill="var(--green)" text-anchor="middle">COOLING SCHEDULE BEHAVIOR</text>
      <text x="15" y="42" font-family="var(--font-body)" font-size="10" fill="var(--ink)">1. High T: Acts like random walk to escape local traps.</text>
      <text x="15" y="58" font-family="var(--font-body)" font-size="10" fill="var(--ink)">2. As T &rarr; 0: P &rarr; 0, collapses smoothly to Hill-Climbing</text>
      <text x="15" y="70" font-family="var(--font-body)" font-size="10" fill="var(--ink)">to converge precisely on the nearest peak.</text>
    </g>
  </g>
</svg>'''
