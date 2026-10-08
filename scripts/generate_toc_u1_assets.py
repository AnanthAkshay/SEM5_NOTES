"""
generate_toc_u1_assets.py - Generates theme-aware SVG state diagrams for TOC Unit 1:
1. Figure 1.1: DFA ending in '01' over {0, 1}
2. Figure 1.2: Parity DFA (Even a's, Odd b's) from Ramaiah SEE Jan 2026 Q1.b.iv
3. Figure 1.3: Epsilon-NFA to DFA Lazy Construction from Ramaiah CIE-1 Q2.a
4. Figure 1.4: DFA for even length beginning with '00' from Ramaiah CIE-1 Q3.a.i
"""

def generate_dfa_ends_01_svg():
    return '''<svg viewBox="0 0 680 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DFA accepting strings ending in 01">
  <defs>
    <style>
      .state-c { fill: var(--surface); stroke: var(--border); stroke-width: 2.2; }
      .state-start { stroke: var(--ink); stroke-width: 2.5; }
      .state-acc { fill: rgba(46, 195, 107, 0.12); stroke: var(--green); stroke-width: 2.5; }
      .state-acc-inner { fill: none; stroke: var(--green); stroke-width: 1.8; }
      .st-txt { font-family: var(--font-mono); font-size: 15px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .trans-line { stroke: var(--ink); stroke-width: 1.8; fill: none; marker-end: url(#arrow-toc); }
      .trans-lbl { font-family: var(--font-mono); font-size: 12.5px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .start-arrow { stroke: var(--ink); stroke-width: 2; fill: none; marker-end: url(#arrow-toc); }
    </style>
    <marker id="arrow-toc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink)"/>
    </marker>
  </defs>

  <!-- Start Arrow -->
  <line x1="30" y1="100" x2="85" y2="100" class="start-arrow"/>
  <text x="50" y="88" class="trans-lbl">Start</text>

  <!-- State q0 (Start) -->
  <circle cx="120" cy="100" r="30" class="state-c state-start"/>
  <text x="120" y="100" class="st-txt">q₀</text>

  <!-- Self-loop on q0 (input 1) -->
  <path d="M 105 72 C 100 25, 140 25, 135 72" class="trans-line"/>
  <text x="120" y="32" class="trans-lbl">1</text>

  <!-- q0 to q1 on 0 -->
  <path d="M 150 90 L 290 90" class="trans-line"/>
  <text x="220" y="78" class="trans-lbl">0</text>

  <!-- State q1 (Seen 0) -->
  <circle cx="320" cy="100" r="30" class="state-c"/>
  <text x="320" y="100" class="st-txt">q₁</text>

  <!-- Self loop on q1 (input 0) -->
  <path d="M 305 72 C 300 25, 340 25, 335 72" class="trans-line"/>
  <text x="320" y="32" class="trans-lbl">0</text>

  <!-- q1 to q2 on 1 -->
  <path d="M 350 90 L 490 90" class="trans-line"/>
  <text x="420" y="78" class="trans-lbl">1</text>

  <!-- State q2 (Accept, Seen 01) -->
  <circle cx="520" cy="100" r="30" class="state-acc"/>
  <circle cx="520" cy="100" r="24" class="state-acc-inner"/>
  <text x="520" y="100" class="st-txt">q₂</text>

  <!-- q2 back to q1 on 0 -->
  <path d="M 500 120 C 450 170, 390 170, 340 125" class="trans-line"/>
  <text x="420" y="165" class="trans-lbl">0</text>

  <!-- q2 back to q0 on 1 -->
  <path d="M 520 130 C 520 190, 120 190, 120 130" class="trans-line"/>
  <text x="320" y="195" class="trans-lbl">1</text>
</svg>'''

def generate_parity_dfa_svg():
    return '''<svg viewBox="0 0 680 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="4-State Parity DFA for Even a's and Odd b's (Ramaiah SEE Jan 2026 Q1.b.iv)">
  <defs>
    <style>
      .p-state { fill: var(--surface); stroke: var(--border); stroke-width: 2.2; }
      .p-acc { fill: rgba(46, 195, 107, 0.12); stroke: var(--green); stroke-width: 2.5; }
      .p-acc-in { fill: none; stroke: var(--green); stroke-width: 1.8; }
      .p-txt { font-family: var(--font-mono); font-size: 13.5px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .p-sub { font-family: var(--font-sans); font-size: 10px; fill: var(--ink-muted); text-anchor: middle; }
      .p-line { stroke: var(--ink); stroke-width: 1.6; fill: none; marker-end: url(#arrow-p); }
      .p-lbl { font-family: var(--font-mono); font-size: 12px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
    </style>
    <marker id="arrow-p" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink)"/>
    </marker>
  </defs>

  <!-- Start Arrow to q_ee -->
  <line x1="30" y1="90" x2="90" y2="90" class="p-line"/>
  <text x="55" y="78" class="p-lbl">Start</text>

  <!-- q_ee (Even a, Even b) -> Top Left -->
  <circle cx="130" cy="90" r="32" class="p-state"/>
  <text x="130" y="90" class="p-txt">q_ee</text>
  <text x="130" y="45" class="p-sub">(Even a, Even b)</text>

  <!-- q_oe (Odd a, Even b) -> Top Right -->
  <circle cx="470" cy="90" r="32" class="p-state"/>
  <text x="470" y="90" class="p-txt">q_oe</text>
  <text x="470" y="45" class="p-sub">(Odd a, Even b)</text>

  <!-- q_eo (Even a, Odd b) -> Bottom Left (ACCEPT STATE) -->
  <circle cx="130" cy="210" r="32" class="p-acc"/>
  <circle cx="130" cy="210" r="26" class="p-acc-in"/>
  <text x="130" y="210" class="p-txt" fill="var(--green)">q_eo</text>
  <text x="130" y="258" class="p-sub">(Even a, Odd b &bull; ACCEPT)</text>

  <!-- q_oo (Odd a, Odd b) -> Bottom Right -->
  <circle cx="470" cy="210" r="32" class="p-state"/>
  <text x="470" y="210" class="p-txt">q_oo</text>
  <text x="470" y="258" class="p-sub">(Odd a, Odd b)</text>

  <!-- Horizontal transitions on 'a' -->
  <!-- q_ee to q_oe (Top a forward) -->
  <path d="M 162 80 L 438 80" class="p-line"/>
  <text x="300" y="70" class="p-lbl">a</text>
  <!-- q_oe to q_ee (Top a backward) -->
  <path d="M 438 100 L 162 100" class="p-line"/>
  <text x="300" y="112" class="p-lbl">a</text>

  <!-- q_eo to q_oo (Bottom a forward) -->
  <path d="M 162 200 L 438 200" class="p-line"/>
  <text x="300" y="190" class="p-lbl">a</text>
  <!-- q_oo to q_eo (Bottom a backward) -->
  <path d="M 438 220 L 162 220" class="p-line"/>
  <text x="300" y="232" class="p-lbl">a</text>

  <!-- Vertical transitions on 'b' -->
  <!-- q_ee to q_eo (Left b downward) -->
  <path d="M 120 122 L 120 178" class="p-line"/>
  <text x="106" y="150" class="p-lbl">b</text>
  <!-- q_eo to q_ee (Left b upward) -->
  <path d="M 140 178 L 140 122" class="p-line"/>
  <text x="154" y="150" class="p-lbl">b</text>

  <!-- q_oe to q_oo (Right b downward) -->
  <path d="M 460 122 L 460 178" class="p-line"/>
  <text x="446" y="150" class="p-lbl">b</text>
  <!-- q_oo to q_oe (Right b upward) -->
  <path d="M 480 178 L 480 122" class="p-line"/>
  <text x="494" y="150" class="p-lbl">b</text>
</svg>'''

def generate_even_len_00_svg():
    return '''<svg viewBox="0 0 740 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DFA for even length strings beginning with 00 (Ramaiah CIE-1 Q3.a.i)">
  <defs>
    <style>
      .el-state { fill: var(--surface); stroke: var(--border); stroke-width: 2.2; }
      .el-acc { fill: rgba(46, 195, 107, 0.12); stroke: var(--green); stroke-width: 2.5; }
      .el-acc-in { fill: none; stroke: var(--green); stroke-width: 1.8; }
      .el-dead { fill: rgba(239, 68, 68, 0.1); stroke: #EF4444; stroke-width: 2; }
      .el-txt { font-family: var(--font-mono); font-size: 14px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .el-line { stroke: var(--ink); stroke-width: 1.6; fill: none; marker-end: url(#arrow-el); }
      .el-lbl { font-family: var(--font-mono); font-size: 12px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
    </style>
    <marker id="arrow-el" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink)"/>
    </marker>
  </defs>

  <!-- Start Arrow -->
  <line x1="20" y1="80" x2="60" y2="80" class="el-line"/>
  <text x="40" y="68" class="el-lbl">Start</text>

  <!-- q0 (len 0) -->
  <circle cx="90" cy="80" r="28" class="el-state"/>
  <text x="90" y="80" class="el-txt">q₀</text>

  <!-- q0 to q1 on 0 -->
  <path d="M 118 80 L 202 80" class="el-line"/>
  <text x="160" y="70" class="el-lbl">0</text>

  <!-- q1 (len 1, saw 0) -->
  <circle cx="230" cy="80" r="28" class="el-state"/>
  <text x="230" y="80" class="el-txt">q₁</text>

  <!-- q1 to q2 on 0 -->
  <path d="M 258 80 L 392 80" class="el-line"/>
  <text x="325" y="70" class="el-lbl">0</text>

  <!-- q2 (len 2 even, saw 00 -> ACCEPT) -->
  <circle cx="420" cy="80" r="28" class="el-acc"/>
  <circle cx="420" cy="80" r="22" class="el-acc-in"/>
  <text x="420" y="80" class="el-txt" fill="var(--green)">q₂</text>

  <!-- q2 to q3 on 0,1 -->
  <path d="M 448 70 L 572 70" class="el-line"/>
  <text x="510" y="60" class="el-lbl">0, 1</text>

  <!-- q3 (len odd >= 3) -->
  <circle cx="600" cy="80" r="28" class="el-state"/>
  <text x="600" y="80" class="el-txt">q₃</text>

  <!-- q3 back to q2 on 0,1 -->
  <path d="M 572 90 L 448 90" class="el-line"/>
  <text x="510" y="102" class="el-lbl">0, 1</text>

  <!-- Trap state (q_trap) on bottom -->
  <circle cx="160" cy="170" r="25" class="el-dead"/>
  <text x="160" y="170" class="el-txt" fill="#EF4444">q_d</text>

  <!-- q0 on 1 to trap -->
  <path d="M 105 104 L 145 148" class="el-line"/>
  <text x="115" y="132" class="el-lbl">1</text>

  <!-- q1 on 1 to trap -->
  <path d="M 215 104 L 175 148" class="el-line"/>
  <text x="205" y="132" class="el-lbl">1</text>

  <!-- Trap self loop on 0,1 -->
  <path d="M 148 193 C 140 225, 180 225, 172 193" class="el-line"/>
  <text x="160" y="215" class="el-lbl">0, 1</text>
</svg>'''
