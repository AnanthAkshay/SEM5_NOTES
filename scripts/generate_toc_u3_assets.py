"""
generate_toc_u3_assets.py - Generates theme-aware SVG diagrams for TOC Unit 3:
1. Figure 3.1: Ambiguity Parse Trees for abab (Ramaiah SEE Jan 2026 Q5.c)
2. Figure 3.2: CFG Simplification & CNF Reduction Pipeline
3. Figure 3.3: Pushdown Automaton State Diagram & Stack ID Flow for a^n b^n (Ramaiah CIE-2 Q1.b)
"""

def generate_ambiguity_parse_trees_svg():
    return '''<svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Two distinct parse trees demonstrating grammar ambiguity for string abab (Ramaiah SEE Jan 2026 Q5.c)">
  <defs>
    <style>
      .tree-node { fill: var(--surface); stroke: var(--border); stroke-width: 2; }
      .tree-leaf { fill: rgba(46, 195, 107, 0.15); stroke: var(--green); stroke-width: 2; }
      .tree-txt { font-family: var(--font-mono); font-size: 13px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .tree-edge { stroke: var(--ink); stroke-width: 1.5; }
      .tree-panel { fill: var(--surface-alt); stroke: var(--border); stroke-width: 1.2; rx: 8px; }
      .tree-title { font-family: var(--font-display); font-size: 12px; font-weight: 700; fill: var(--ink); text-anchor: middle; }
    </style>
  </defs>

  <!-- Parse Tree 1 (Left Panel) -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="360" height="235" class="tree-panel"/>
    <text x="180" y="24" class="tree-title">Parse Tree 1: (Derivation A)</text>

    <!-- Root S (180, 50) -->
    <line x1="180" y1="50" x2="110" y2="100" class="tree-edge"/>
    <line x1="180" y1="50" x2="250" y2="100" class="tree-edge"/>

    <circle cx="180" cy="50" r="18" class="tree-node"/>
    <text x="180" y="50" class="tree-txt">S</text>

    <!-- S -> a B -->
    <circle cx="110" cy="100" r="16" class="tree-leaf"/>
    <text x="110" y="100" class="tree-txt" fill="var(--green)">a</text>

    <circle cx="250" cy="100" r="18" class="tree-node"/>
    <text x="250" y="100" class="tree-txt">B</text>

    <!-- B -> b S -->
    <line x1="250" y1="100" x2="200" y2="150" class="tree-edge"/>
    <line x1="250" y1="100" x2="300" y2="150" class="tree-edge"/>

    <circle cx="200" cy="150" r="16" class="tree-leaf"/>
    <text x="200" y="150" class="tree-txt" fill="var(--green)">b</text>

    <circle cx="300" cy="150" r="18" class="tree-node"/>
    <text x="300" y="150" class="tree-txt">S</text>

    <!-- S -> a B -> a b -->
    <line x1="300" y1="150" x2="260" y2="200" class="tree-edge"/>
    <line x1="300" y1="150" x2="340" y2="200" class="tree-edge"/>

    <circle cx="260" cy="200" r="16" class="tree-leaf"/>
    <text x="260" y="200" class="tree-txt" fill="var(--green)">a</text>

    <circle cx="340" cy="200" r="16" class="tree-leaf"/>
    <text x="340" y="200" class="tree-txt" fill="var(--green)">b</text>
  </g>

  <!-- Parse Tree 2 (Right Panel) -->
  <g transform="translate(390, 10)">
    <rect x="0" y="0" width="360" height="235" class="tree-panel"/>
    <text x="180" y="24" class="tree-title">Parse Tree 2: (Derivation B)</text>

    <!-- Root S (180, 50) -->
    <line x1="180" y1="50" x2="90" y2="100" class="tree-edge"/>
    <line x1="180" y1="50" x2="180" y2="100" class="tree-edge"/>
    <line x1="180" y1="50" x2="270" y2="100" class="tree-edge"/>

    <circle cx="180" cy="50" r="18" class="tree-node"/>
    <text x="180" y="50" class="tree-txt">S</text>

    <!-- S -> a B -> a (a B B) -->
    <circle cx="90" cy="100" r="16" class="tree-leaf"/>
    <text x="90" y="100" class="tree-txt" fill="var(--green)">a</text>

    <!-- Branch via a B B -->
    <circle cx="180" cy="100" r="18" class="tree-node"/>
    <text x="180" y="100" class="tree-txt">B</text>

    <!-- B -> b and B -> b -->
    <line x1="180" y1="100" x2="140" y2="150" class="tree-edge"/>
    <line x1="180" y1="100" x2="220" y2="150" class="tree-edge"/>

    <circle cx="140" cy="150" r="16" class="tree-leaf"/>
    <text x="140" y="150" class="tree-txt" fill="var(--green)">b</text>

    <circle cx="220" cy="150" r="18" class="tree-node"/>
    <text x="220" y="150" class="tree-txt">A</text>

    <line x1="220" y1="150" x2="200" y2="200" class="tree-edge"/>
    <line x1="220" y1="150" x2="240" y2="200" class="tree-edge"/>

    <circle cx="200" cy="200" r="16" class="tree-leaf"/>
    <text x="200" y="200" class="tree-txt" fill="var(--green)">a</text>

    <circle cx="270" cy="100" r="16" class="tree-leaf"/>
    <text x="270" y="100" class="tree-txt" fill="var(--green)">b</text>

    <text x="180" y="222" font-family="var(--font-sans)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">Both yield string: 'abab' &bull; AMBIGUOUS</text>
  </g>
</svg>'''

def generate_pda_stack_trace_svg():
    return '''<svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Pushdown Automaton State Diagram and Stack Trace for a^n b^n (Ramaiah CIE-2 Q1.b)">
  <defs>
    <style>
      .pda-state { fill: var(--surface); stroke: var(--border); stroke-width: 2.2; }
      .pda-acc { fill: rgba(46, 195, 107, 0.12); stroke: var(--green); stroke-width: 2.5; }
      .pda-acc-in { fill: none; stroke: var(--green); stroke-width: 1.8; }
      .pda-txt { font-family: var(--font-mono); font-size: 14px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .pda-line { stroke: var(--ink); stroke-width: 1.8; fill: none; marker-end: url(#arrow-pda); }
      .pda-lbl { font-family: var(--font-mono); font-size: 11px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .stack-box { fill: var(--surface-alt); stroke: var(--border); stroke-width: 1.5; }
      .stack-elem { fill: rgba(46, 195, 107, 0.15); stroke: var(--green); stroke-width: 1.2; }
      .stack-txt { font-family: var(--font-mono); font-size: 11.5px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
    </style>
    <marker id="arrow-pda" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink)"/>
    </marker>
  </defs>

  <!-- Left: PDA State Transition Diagram -->
  <g transform="translate(10, 15)">
    <!-- Start Arrow -->
    <line x1="20" y1="100" x2="55" y2="100" class="pda-line"/>
    <text x="36" y="90" class="pda-lbl">Start</text>

    <!-- State q0 (Push phase) -->
    <circle cx="95" cy="100" r="30" class="pda-state"/>
    <text x="95" y="100" class="pda-txt">q₀</text>

    <!-- q0 self-loop: a, Z0 -> AZ0 and a, A -> AA -->
    <path d="M 80 72 C 60 20, 130 20, 110 72" class="pda-line"/>
    <text x="95" y="24" class="pda-lbl">a, Z₀ / AZ₀</text>
    <text x="95" y="38" class="pda-lbl">a, A / AA</text>

    <!-- q0 to q1 on b, A -> epsilon -->
    <path d="M 125 100 L 235 100" class="pda-line"/>
    <text x="180" y="88" class="pda-lbl">b, A / &epsilon;</text>

    <!-- State q1 (Pop phase) -->
    <circle cx="265" cy="100" r="30" class="pda-state"/>
    <text x="265" y="100" class="pda-txt">q₁</text>

    <!-- q1 self-loop: b, A -> epsilon -->
    <path d="M 250 72 C 230 20, 300 20, 280 72" class="pda-line"/>
    <text x="265" y="32" class="pda-lbl">b, A / &epsilon;</text>

    <!-- q1 to q2 on epsilon, Z0 -> Z0 -->
    <path d="M 295 100 L 405 100" class="pda-line"/>
    <text x="350" y="88" class="pda-lbl">&epsilon;, Z₀ / Z₀</text>

    <!-- State q2 (Accept state) -->
    <circle cx="435" cy="100" r="30" class="pda-acc"/>
    <circle cx="435" cy="100" r="24" class="pda-acc-in"/>
    <text x="435" y="100" class="pda-txt" fill="var(--green)">q₂</text>
  </g>

  <!-- Right: Stack Trace Visualizer for w = aabb -->
  <g transform="translate(490, 15)">
    <rect x="0" y="0" width="250" height="210" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2"/>
    <text x="125" y="22" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">Stack ID Sequence (w = aabb)</text>

    <!-- Step 0: [Z0] -->
    <rect x="15" y="40" width="46" height="30" class="stack-box"/>
    <text x="38" y="55" class="stack-txt">Z₀</text>
    <text x="38" y="82" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">(q₀, aabb)</text>

    <!-- Step 1: [A, Z0] -->
    <rect x="70" y="40" width="46" height="50" class="stack-box"/>
    <rect x="73" y="43" width="40" height="20" class="stack-elem"/>
    <text x="93" y="53" class="stack-txt">A</text>
    <text x="93" y="75" class="stack-txt">Z₀</text>
    <text x="93" y="102" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">(q₀, abb)</text>

    <!-- Step 2: [A, A, Z0] -->
    <rect x="125" y="40" width="46" height="70" class="stack-box"/>
    <rect x="128" y="43" width="40" height="18" class="stack-elem"/>
    <text x="148" y="52" class="stack-txt">A</text>
    <rect x="128" y="64" width="40" height="18" class="stack-elem"/>
    <text x="148" y="73" class="stack-txt">A</text>
    <text x="148" y="95" class="stack-txt">Z₀</text>
    <text x="148" y="122" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">(q₀, bb)</text>

    <!-- Step 3: [A, Z0] -->
    <rect x="180" y="40" width="46" height="50" class="stack-box"/>
    <rect x="183" y="43" width="40" height="20" class="stack-elem"/>
    <text x="203" y="53" class="stack-txt">A</text>
    <text x="203" y="75" class="stack-txt">Z₀</text>
    <text x="203" y="102" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">(q₁, b)</text>

    <!-- Final Step note -->
    <text x="125" y="165" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--green)" text-anchor="middle">&vdash; (q₁, &epsilon;, Z₀) &vdash; (q₂, &epsilon;, Z₀)</text>
    <text x="125" y="185" font-family="var(--font-sans)" font-size="11" fill="var(--ink)" text-anchor="middle">ACCEPTED by Final State q₂ &check;</text>
  </g>
</svg>'''
