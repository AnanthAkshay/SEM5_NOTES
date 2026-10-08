"""
generate_ai_u3_assets.py - Generates theme-aware SVGs for AI Unit 3 notes:
- Figure 3.1: Minimax Game Tree with Alpha-Beta Pruning Cutoffs (Ramaiah CIE-1 Q1.c, Q2.c, Q3.c)
- Figure 3.2: Australia Map Coloring CSP Constraint Graph & AC-3 Arc Consistency (Audit Verified)
"""

def generate_minimax_alphabeta_svg():
    """Figure 3.1: Minimax Game Tree with Alpha-Beta Pruned Branches"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Minimax Game Tree with Alpha-Beta Pruning Cutoffs">
  <defs>
    <marker id="mb-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink-muted)" />
    </marker>
    <marker id="mb-arr-opt" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--green)" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">MINIMAX WITH &alpha;-&beta; PRUNING &bull; ROOT MAX = 3 &bull; &beta; &le; &alpha; PRUNING CUTOFFS (RAMAIAH CIE-1 Q1.c, Q2.c)</text>

  <!-- Tree Layers Annotations on Left -->
  <text x="35" y="70" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)">PLY 0: MAX (&Delta;)</text>
  <text x="35" y="150" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--green)">PLY 1: MIN (&nabla;)</text>
  <text x="35" y="240" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--ink-muted)">LEAF UTILITIES</text>

  <!-- Level 0: Root MAX Node A -->
  <g transform="translate(390, 65)">
    <!-- Upward triangle for MAX -->
    <polygon points="0,-18 20,18 -20,18" fill="var(--brand-tint)" stroke="var(--brand)" stroke-width="2" />
    <text x="0" y="12" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)" text-anchor="middle">3</text>
    <text x="32" y="5" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">A [&alpha;=3, &beta;=&infin;]</text>
  </g>

  <!-- Branches from Root A to B, C, D -->
  <line x1="380" y1="85" x2="160" y2="135" stroke="var(--green)" stroke-width="2.5" />
  <line x1="390" y1="85" x2="390" y2="135" stroke="var(--ink-muted)" stroke-width="1.5" />
  <line x1="400" y1="85" x2="620" y2="135" stroke="var(--ink-muted)" stroke-width="1.5" />

  <!-- Level 1: MIN Node B (Left Subtree) -->
  <g transform="translate(160, 150)">
    <!-- Downward triangle for MIN -->
    <polygon points="0,18 20,-18 -20,-18" fill="var(--green-tint)" stroke="var(--green)" stroke-width="2" />
    <text x="0" y="-3" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--green)" text-anchor="middle">3</text>
    <text x="-40" y="-5" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">B</text>
  </g>

  <!-- Leaves under B: 3, 12, 8 -->
  <line x1="150" y1="170" x2="90" y2="225" stroke="var(--green)" stroke-width="2" />
  <line x1="160" y1="170" x2="160" y2="225" stroke="var(--ink-muted)" stroke-width="1.2" />
  <line x1="170" y1="170" x2="230" y2="225" stroke="var(--ink-muted)" stroke-width="1.2" />

  <!-- Leaf 3 -->
  <circle cx="90" cy="235" r="14" fill="var(--surface-alt)" stroke="var(--green)" stroke-width="2" />
  <text x="90" y="239" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--green)" text-anchor="middle">3</text>

  <!-- Leaf 12 -->
  <circle cx="160" cy="235" r="14" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="160" y="239" font-family="var(--font-mono)" font-size="11" font-weight="600" fill="var(--ink-muted)" text-anchor="middle">12</text>

  <!-- Leaf 8 -->
  <circle cx="230" cy="235" r="14" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="230" y="239" font-family="var(--font-mono)" font-size="11" font-weight="600" fill="var(--ink-muted)" text-anchor="middle">8</text>

  <!-- Level 1: MIN Node C (Middle Subtree - PRUNED!) -->
  <g transform="translate(390, 150)">
    <polygon points="0,18 20,-18 -20,-18" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="2" />
    <text x="0" y="-3" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">2</text>
    <text x="-38" y="-5" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">C [&beta;=2]</text>
  </g>

  <!-- Leaves under C: 2, 4 (pruned), 6 (pruned) -->
  <line x1="380" y1="170" x2="320" y2="225" stroke="var(--ink-muted)" stroke-width="1.5" />
  <line x1="390" y1="170" x2="390" y2="225" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="4 2" />
  <line x1="400" y1="170" x2="460" y2="225" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="4 2" />

  <!-- Leaf 2 -->
  <circle cx="320" cy="235" r="14" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="320" y="239" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">2</text>

  <!-- Pruned Leaf 4 -->
  <circle cx="390" cy="235" r="14" fill="var(--surface-alt)" stroke="#EF4444" stroke-width="1.2" stroke-dasharray="2 2" />
  <text x="390" y="239" font-family="var(--font-mono)" font-size="11" fill="#EF4444" text-anchor="middle">4</text>
  <line x1="375" y1="220" x2="405" y2="250" stroke="#EF4444" stroke-width="2" />

  <!-- Pruned Leaf 6 -->
  <circle cx="460" cy="235" r="14" fill="var(--surface-alt)" stroke="#EF4444" stroke-width="1.2" stroke-dasharray="2 2" />
  <text x="460" y="239" font-family="var(--font-mono)" font-size="11" fill="#EF4444" text-anchor="middle">6</text>
  <line x1="445" y1="220" x2="475" y2="250" stroke="#EF4444" stroke-width="2" />

  <!-- Cutoff Callout on C -->
  <rect x="410" y="160" width="105" height="24" rx="4" fill="#FEF2F2" stroke="#EF4444" stroke-width="1" />
  <text x="462" y="176" font-family="var(--font-mono)" font-size="9" font-weight="700" fill="#EF4444" text-anchor="middle">&beta;=2 &le; &alpha;=3 &rarr; CUTOFF</text>

  <!-- Level 1: MIN Node D (Right Subtree) -->
  <g transform="translate(620, 150)">
    <polygon points="0,18 20,-18 -20,-18" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="2" />
    <text x="0" y="-3" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">2</text>
    <text x="32" y="-5" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">D [&beta;=2]</text>
  </g>

  <!-- Leaves under D: 14, 5, 2 -->
  <line x1="610" y1="170" x2="550" y2="225" stroke="var(--ink-muted)" stroke-width="1.2" />
  <line x1="620" y1="170" x2="620" y2="225" stroke="var(--ink-muted)" stroke-width="1.2" />
  <line x1="630" y1="170" x2="690" y2="225" stroke="var(--ink-muted)" stroke-width="1.2" />

  <!-- Leaf 14 -->
  <circle cx="550" cy="235" r="14" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="550" y="239" font-family="var(--font-mono)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">14</text>

  <!-- Leaf 5 -->
  <circle cx="620" cy="235" r="14" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="620" y="239" font-family="var(--font-mono)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">5</text>

  <!-- Leaf 2 -->
  <circle cx="690" cy="235" r="14" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="690" y="239" font-family="var(--font-mono)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">2</text>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(35, 275)">
    <rect width="710" height="42" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="355" y="18" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Root MAX chooses move to B with value 3 &bull; &alpha; acts as best MAX value; &beta; acts as best MIN value.</text>
    <text x="355" y="32" font-family="var(--font-mono)" font-size="10" fill="var(--green)" text-anchor="middle">Cutoff occurs at Node C because &beta;=2 &le; &alpha;=3, pruning 2 terminal leaf evaluations.</text>
  </g>
</svg>'''

def generate_csp_map_coloring_svg():
    """Figure 3.2: Australia Map Coloring CSP Constraint Graph & AC-3 Domain Pruning"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Australia Map Coloring CSP Constraint Graph and AC-3 Domain Pruning">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">AUSTRALIA MAP COLORING CSP &bull; CONSTRAINT GRAPH &amp; AC-3 ARC CONSISTENCY (AUDIT VERIFIED)</text>

  <!-- Left: Constraint Graph Layout (7 regions) -->
  <g transform="translate(30, 50)">
    <rect width="360" height="265" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="180" y="24" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--brand)" text-anchor="middle">CONSTRAINT NETWORK GRAPH (BINARY &ne;)</text>

    <!-- Constraint Edges (Connecting adjacent regions) -->
    <!-- WA-NT, WA-SA -->
    <line x1="80" y1="120" x2="160" y2="80" stroke="var(--border-strong)" stroke-width="1.8" />
    <line x1="80" y1="120" x2="160" y2="170" stroke="var(--border-strong)" stroke-width="1.8" />

    <!-- NT-SA, NT-Q -->
    <line x1="160" y1="80" x2="160" y2="170" stroke="var(--border-strong)" stroke-width="1.8" />
    <line x1="160" y1="80" x2="250" y2="90" stroke="var(--border-strong)" stroke-width="1.8" />

    <!-- SA-Q, SA-NSW, SA-V -->
    <line x1="160" y1="170" x2="250" y2="90" stroke="var(--border-strong)" stroke-width="1.8" />
    <line x1="160" y1="170" x2="260" y2="170" stroke="var(--border-strong)" stroke-width="1.8" />
    <line x1="160" y1="170" x2="230" y2="230" stroke="var(--border-strong)" stroke-width="1.8" />

    <!-- Q-NSW, NSW-V -->
    <line x1="250" y1="90" x2="260" y2="170" stroke="var(--border-strong)" stroke-width="1.8" />
    <line x1="260" y1="170" x2="230" y2="230" stroke="var(--border-strong)" stroke-width="1.8" />

    <!-- Node WA (Assigned Red) -->
    <circle cx="80" cy="120" r="22" fill="#FEE2E2" stroke="#EF4444" stroke-width="2.5" />
    <text x="80" y="124" font-family="var(--font-display)" font-size="12" font-weight="800" fill="#EF4444" text-anchor="middle">WA</text>
    <text x="80" y="156" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="#EF4444" text-anchor="middle">{R}</text>

    <!-- Node NT -->
    <circle cx="160" cy="80" r="20" fill="var(--surface)" stroke="var(--border-strong)" stroke-width="2" />
    <text x="160" y="84" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">NT</text>
    <text x="160" y="112" font-family="var(--font-mono)" font-size="8.5" fill="var(--green)" text-anchor="middle">{G, B}</text>

    <!-- Node SA -->
    <circle cx="160" cy="170" r="20" fill="var(--surface)" stroke="var(--border-strong)" stroke-width="2" />
    <text x="160" y="174" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">SA</text>
    <text x="160" y="202" font-family="var(--font-mono)" font-size="8.5" fill="var(--green)" text-anchor="middle">{G, B}</text>

    <!-- Node Q -->
    <circle cx="250" cy="90" r="20" fill="var(--surface)" stroke="var(--border-strong)" stroke-width="2" />
    <text x="250" y="94" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Q</text>
    <text x="250" y="122" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">{R, G, B}</text>

    <!-- Node NSW -->
    <circle cx="260" cy="170" r="20" fill="var(--surface)" stroke="var(--border-strong)" stroke-width="2" />
    <text x="260" y="174" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">NSW</text>
    <text x="260" y="202" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">{R, G, B}</text>

    <!-- Node V -->
    <circle cx="230" cy="230" r="18" fill="var(--surface)" stroke="var(--border-strong)" stroke-width="2" />
    <text x="230" y="234" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">V</text>
    <text x="230" y="258" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">{R, G, B}</text>

    <!-- Node T (Tasmania - Disconnected) -->
    <circle cx="315" cy="230" r="18" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" stroke-dasharray="3 2" />
    <text x="315" y="234" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">T</text>
    <text x="315" y="258" font-family="var(--font-mono)" font-size="8" fill="var(--ink-muted)" text-anchor="middle">{R, G, B}</text>
  </g>

  <!-- Right: AC-3 Domain Reduction Trace -->
  <g transform="translate(410, 50)">
    <rect width="345" height="265" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="172" y="24" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--green)" text-anchor="middle">AC-3 ARC CONSISTENCY TRACE (WA = RED)</text>

    <g transform="translate(20, 42)">
      <rect width="305" height="135" rx="8" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
      <text x="15" y="22" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">Step</text>
      <text x="65" y="22" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)">Arc Evaluated</text>
      <text x="180" y="22" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)">Domain Action</text>

      <line x1="10" y1="30" x2="295" y2="30" stroke="var(--border)" stroke-width="1" />

      <text x="15" y="50" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">1</text>
      <text x="65" y="50" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">(NT, WA)</text>
      <text x="180" y="50" font-family="var(--font-mono)" font-size="9" fill="var(--green)">Prune 'R' from NT &rarr; {G, B} &check;</text>

      <text x="15" y="72" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">2</text>
      <text x="65" y="72" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">(SA, WA)</text>
      <text x="180" y="72" font-family="var(--font-mono)" font-size="9" fill="var(--green)">Prune 'R' from SA &rarr; {G, B} &check;</text>

      <text x="15" y="94" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">3</text>
      <text x="65" y="94" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">(Q, NT)</text>
      <text x="180" y="94" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">Consistent (NT has {G,B})</text>

      <text x="15" y="116" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">4</text>
      <text x="65" y="116" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">(T, *)</text>
      <text x="180" y="116" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">No mainland neighbors &rarr; {R,G,B}</text>
    </g>

    <!-- AC-3 Complexity Box -->
    <g transform="translate(20, 190)">
      <rect width="305" height="60" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.2" />
      <text x="152" y="18" font-family="var(--font-mono)" font-size="10" font-weight="800" fill="var(--green)" text-anchor="middle">AC-3 WORST-CASE COMPLEXITY</text>
      <text x="152" y="36" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">Time: O(c &bull; d&sup3;) &bull; Space: O(c)</text>
      <text x="152" y="50" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">c = 9 binary constraint arcs &bull; d = 3 colors {R, G, B}</text>
    </g>
  </g>
</svg>'''
