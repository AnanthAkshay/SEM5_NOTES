"""
generate_toc_u2_assets.py - Generates theme-aware SVG diagrams for TOC Unit 2:
1. Figure 2.1: 6-State DFA Minimization from Ramaiah CIE-1 Q1.b
2. Figure 2.2: Thompson's Construction for (00)* 11 (0+1)* from Ramaiah CIE-1 Q2.b
3. Figure 2.3: State Elimination GTG Step-by-Step from Ramaiah SEE Jan 2026 Q3.c
"""

def generate_cie1_min_dfa_svg():
    return '''<svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Minimization of 6-state DFA from Ramaiah CIE-1 Q1.b">
  <defs>
    <style>
      .m-state { fill: var(--surface); stroke: var(--border); stroke-width: 2.2; }
      .m-acc { fill: rgba(46, 195, 107, 0.12); stroke: var(--green); stroke-width: 2.5; }
      .m-acc-in { fill: none; stroke: var(--green); stroke-width: 1.8; }
      .m-txt { font-family: var(--font-mono); font-size: 14px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .m-line { stroke: var(--ink); stroke-width: 1.6; fill: none; marker-end: url(#arrow-m); }
      .m-lbl { font-family: var(--font-mono); font-size: 11.5px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .panel-bg { fill: var(--surface-alt); stroke: var(--border); stroke-width: 1.2; rx: 8px; }
      .panel-txt { font-family: var(--font-display); font-size: 12px; font-weight: 700; fill: var(--ink); text-anchor: middle; }
    </style>
    <marker id="arrow-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink)"/>
    </marker>
  </defs>

  <!-- Left: Original 6-State DFA (q1, q2, q3 are Accept) -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="420" height="235" class="panel-bg"/>
    <text x="210" y="24" class="panel-txt">Original 6-State DFA (Ramaiah CIE-1 Q1.b)</text>

    <!-- Top Row: Accept States q1, q2, q3 -->
    <circle cx="70" cy="80" r="24" class="m-acc"/>
    <circle cx="70" cy="80" r="19" class="m-acc-in"/>
    <text x="70" y="80" class="m-txt" fill="var(--green)">q₁</text>

    <circle cx="210" cy="80" r="24" class="m-acc"/>
    <circle cx="210" cy="80" r="19" class="m-acc-in"/>
    <text x="210" y="80" class="m-txt" fill="var(--green)">q₂</text>

    <circle cx="350" cy="80" r="24" class="m-acc"/>
    <circle cx="350" cy="80" r="19" class="m-acc-in"/>
    <text x="350" y="80" class="m-txt" fill="var(--green)">q₃</text>

    <!-- Bottom Row: Non-Accept States q4, q5, q6 -->
    <circle cx="70" cy="180" r="24" class="m-state"/>
    <text x="70" y="180" class="m-txt">q₄</text>

    <circle cx="210" cy="180" r="24" class="m-state"/>
    <text x="210" y="180" class="m-txt">q₅</text>

    <circle cx="350" cy="180" r="24" class="m-state"/>
    <text x="350" y="180" class="m-txt">q₆</text>

    <!-- Horizontal transitions on 'a' -->
    <path d="M 94 72 L 186 72" class="m-line"/>
    <text x="140" y="64" class="m-lbl">a</text>
    <path d="M 234 72 L 326 72" class="m-line"/>
    <text x="280" y="64" class="m-lbl">a</text>

    <path d="M 94 172 L 186 172" class="m-line"/>
    <text x="140" y="164" class="m-lbl">a</text>
    <path d="M 234 172 L 326 172" class="m-line"/>
    <text x="280" y="164" class="m-lbl">a</text>

    <!-- Vertical transitions on 'b' -->
    <path d="M 62 104 L 62 156" class="m-line"/>
    <text x="50" y="130" class="m-lbl">b</text>
    <path d="M 78 156 L 78 104" class="m-line"/>
    <text x="90" y="130" class="m-lbl">b</text>

    <path d="M 202 104 L 202 156" class="m-line"/>
    <text x="190" y="130" class="m-lbl">b</text>
    <path d="M 218 156 L 218 104" class="m-line"/>
    <text x="230" y="130" class="m-lbl">b</text>

    <path d="M 342 104 L 342 156" class="m-line"/>
    <text x="330" y="130" class="m-lbl">b</text>
    <path d="M 358 156 L 358 104" class="m-line"/>
    <text x="370" y="130" class="m-lbl">b</text>
  </g>

  <!-- Right: Minimized 2-State DFA -->
  <g transform="translate(450, 10)">
    <rect x="0" y="0" width="300" height="235" class="panel-bg"/>
    <text x="150" y="24" class="panel-txt">Minimized Equivalent DFA (2 States)</text>

    <!-- Start Arrow -->
    <line x1="20" y1="120" x2="55" y2="120" class="m-line"/>
    <text x="36" y="110" class="m-lbl">Start</text>

    <!-- State {q1, q2, q3} (Accept) -->
    <circle cx="100" cy="120" r="34" class="m-acc"/>
    <circle cx="100" cy="120" r="28" class="m-acc-in"/>
    <text x="100" y="120" class="m-txt" font-size="12" fill="var(--green)">{q₁,q₂,q₃}</text>

    <!-- State {q4, q5, q6} (Non-Accept) -->
    <circle cx="230" cy="120" r="34" class="m-state"/>
    <text x="230" y="120" class="m-txt" font-size="12">{q₄,q₅,q₆}</text>

    <!-- Self-loop on Accept on 'a' -->
    <path d="M 85 88 C 75 40, 125 40, 115 88" class="m-line"/>
    <text x="100" y="50" class="m-lbl">a</text>

    <!-- Self-loop on Non-Accept on 'a' -->
    <path d="M 215 88 C 205 40, 255 40, 245 88" class="m-line"/>
    <text x="230" y="50" class="m-lbl">a</text>

    <!-- Between {q1..} and {q4..} on 'b' -->
    <path d="M 134 110 L 196 110" class="m-line"/>
    <text x="165" y="100" class="m-lbl">b</text>

    <path d="M 196 130 L 134 130" class="m-line"/>
    <text x="165" y="145" class="m-lbl">b</text>
  </g>
</svg>'''

def generate_thompson_nfa_svg():
    return '''<svg viewBox="0 0 740 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Thompson's Construction for (00)* 11 (0+1)* (Ramaiah CIE-1 Q2.b)">
  <defs>
    <style>
      .t-box { fill: var(--surface); stroke: var(--border); stroke-width: 2; }
      .t-acc { fill: rgba(46, 195, 107, 0.12); stroke: var(--green); stroke-width: 2.2; }
      .t-acc-in { fill: none; stroke: var(--green); stroke-width: 1.6; }
      .t-txt { font-family: var(--font-mono); font-size: 13px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .t-line { stroke: var(--ink); stroke-width: 1.6; fill: none; marker-end: url(#arrow-t); }
      .t-lbl { font-family: var(--font-mono); font-size: 11px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .t-block-bg { fill: var(--surface-alt); stroke: var(--border); stroke-dasharray: 4 4; stroke-width: 1; rx: 6px; }
      .t-block-title { font-family: var(--font-display); font-size: 11px; font-weight: 700; fill: var(--ink-muted); text-anchor: middle; }
    </style>
    <marker id="arrow-t" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink)"/>
    </marker>
  </defs>

  <!-- Block 1: (00)* -->
  <rect x="20" y="25" width="230" height="170" class="t-block-bg"/>
  <text x="135" y="45" class="t-block-title">Block 1: (00)* (Kleene Star)</text>

  <!-- Block 2: 11 -->
  <rect x="270" y="25" width="200" height="170" class="t-block-bg"/>
  <text x="370" y="45" class="t-block-title">Block 2: 11 (Concat)</text>

  <!-- Block 3: (0+1)* -->
  <rect x="490" y="25" width="230" height="170" class="t-block-bg"/>
  <text x="605" y="45" class="t-block-title">Block 3: (0+1)* (Star of Union)</text>

  <!-- Nodes in Block 1 -->
  <circle cx="55" cy="110" r="20" class="t-box"/>
  <text x="55" y="110" class="t-txt">s₀</text>

  <circle cx="135" cy="110" r="20" class="t-box"/>
  <text x="135" y="110" class="t-txt">s₁</text>

  <circle cx="215" cy="110" r="20" class="t-box"/>
  <text x="215" y="110" class="t-txt">s₂</text>

  <path d="M 75 110 L 115 110" class="t-line"/>
  <text x="95" y="100" class="t-lbl">0</text>
  <path d="M 155 110 L 195 110" class="t-line"/>
  <text x="175" y="100" class="t-lbl">0</text>

  <!-- Bypass epsilon for (00)* -->
  <path d="M 55 90 C 55 50, 215 50, 215 90" class="t-line"/>
  <text x="135" y="58" class="t-lbl">&epsilon;</text>

  <!-- Loop back epsilon -->
  <path d="M 215 130 C 215 170, 55 170, 55 130" class="t-line"/>
  <text x="135" y="165" class="t-lbl">&epsilon;</text>

  <!-- Connect Block 1 to Block 2 -->
  <path d="M 235 110 L 295 110" class="t-line"/>
  <text x="265" y="100" class="t-lbl">&epsilon;</text>

  <!-- Nodes in Block 2 -->
  <circle cx="315" cy="110" r="20" class="t-box"/>
  <text x="315" y="110" class="t-txt">s₃</text>
  <circle cx="375" cy="110" r="20" class="t-box"/>
  <text x="375" y="110" class="t-txt">s₄</text>
  <circle cx="435" cy="110" r="20" class="t-box"/>
  <text x="435" y="110" class="t-txt">s₅</text>

  <path d="M 335 110 L 355 110" class="t-line"/>
  <text x="345" y="100" class="t-lbl">1</text>
  <path d="M 395 110 L 415 110" class="t-line"/>
  <text x="405" y="100" class="t-lbl">1</text>

  <!-- Connect Block 2 to Block 3 -->
  <path d="M 455 110 L 515 110" class="t-line"/>
  <text x="485" y="100" class="t-lbl">&epsilon;</text>

  <!-- Nodes in Block 3 -->
  <circle cx="535" cy="110" r="20" class="t-box"/>
  <text x="535" y="110" class="t-txt">s₆</text>

  <circle cx="675" cy="110" r="24" class="t-acc"/>
  <circle cx="675" cy="110" r="19" class="t-acc-in"/>
  <text x="675" y="110" class="t-txt" fill="var(--green)">s₇</text>

  <!-- Self-loop on (0+1) -->
  <path d="M 525 90 C 515 45, 555 45, 545 90" class="t-line"/>
  <text x="535" y="55" class="t-lbl">0, 1</text>

  <path d="M 555 110 L 651 110" class="t-line"/>
  <text x="605" y="100" class="t-lbl">&epsilon;</text>
</svg>'''
