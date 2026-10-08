"""
generate_cn_u1_assets.py - Generates verified inline SVGs and HTML snippets for CN Unit 1.
"""

def generate_cascaded_db_svg():
    return '''<svg viewBox="0 0 720 180" width="100%" height="180" role="img" aria-label="Cascaded Decibel Stages Transmission Diagram">
  <title>Cascaded Decibel Stages Diagram</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />
  
  <!-- Stage 1: Input -->
  <g transform="translate(30, 45)">
    <circle cx="25" cy="40" r="18" fill="var(--surface-alt)" stroke="var(--ink)" stroke-width="1.8" />
    <text x="25" y="44" fill="var(--ink)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">TX</text>
    <text x="25" y="75" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">P_in</text>
    <text x="25" y="90" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">10.0 mW</text>
  </g>

  <!-- Arrow 1 to Cable 1 -->
  <line x1="85" y1="85" x2="130" y2="85" stroke="var(--ink)" stroke-width="2" />
  <polygon points="128,81 136,85 128,89" fill="var(--ink)" />

  <!-- Stage 2: Cable Segment 1 (-3 dB) -->
  <g transform="translate(140, 50)">
    <rect x="0" y="0" width="120" height="70" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" rx="8" />
    <text x="60" y="24" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">Cable Segment 1</text>
    <text x="60" y="44" fill="#B91C1C" font-family="var(--font-mono)" font-size="13" font-weight="700" text-anchor="middle">-3 dB Loss</text>
    <text x="60" y="60" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">P = 5.0 mW</text>
  </g>

  <!-- Arrow 2 to Amplifier -->
  <line x1="265" y1="85" x2="310" y2="85" stroke="var(--ink)" stroke-width="2" />
  <polygon points="308,81 316,85 308,89" fill="var(--ink)" />

  <!-- Stage 3: Amplifier (+7 dB) -->
  <g transform="translate(320, 45)">
    <!-- Amplifier triangle -->
    <polygon points="10,5 95,40 10,75" fill="rgba(46,195,107,0.15)" stroke="var(--green)" stroke-width="2" />
    <text x="45" y="38" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">In-Line Amp</text>
    <text x="45" y="54" fill="var(--green)" font-family="var(--font-mono)" font-size="12" font-weight="700" text-anchor="middle">+7 dB Gain</text>
    <text x="105" y="30" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10">P = 25.1 mW</text>
  </g>

  <!-- Arrow 3 to Cable 2 -->
  <line x1="440" y1="85" x2="480" y2="85" stroke="var(--ink)" stroke-width="2" />
  <polygon points="478,81 486,85 478,89" fill="var(--ink)" />

  <!-- Stage 4: Cable Segment 2 (-3 dB) -->
  <g transform="translate(490, 50)">
    <rect x="0" y="0" width="120" height="70" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" rx="8" />
    <text x="60" y="24" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">Cable Segment 2</text>
    <text x="60" y="44" fill="#B91C1C" font-family="var(--font-mono)" font-size="13" font-weight="700" text-anchor="middle">-3 dB Loss</text>
    <text x="60" y="60" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Net: +1 dB</text>
  </g>

  <!-- Arrow 4 to Output -->
  <line x1="615" y1="85" x2="650" y2="85" stroke="var(--ink)" stroke-width="2" />
  <polygon points="648,81 656,85 648,89" fill="var(--ink)" />

  <!-- Stage 5: Output -->
  <g transform="translate(645, 45)">
    <circle cx="35" cy="40" r="18" fill="rgba(46,195,107,0.2)" stroke="var(--green)" stroke-width="2" />
    <text x="35" y="44" fill="var(--ink)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">RX</text>
    <text x="35" y="75" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">P_out</text>
    <text x="35" y="90" fill="var(--green)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">12.589 mW</text>
  </g>

  <!-- Summary Footnote -->
  <text x="360" y="160" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Total Link dB = (-3 dB) + (+7 dB) + (-3 dB) = +1 dB &bull; P_out = 10 mW &times; 10^(1/10) = 12.589 mW</text>
</svg>'''

def generate_bdp_pipe_svg():
    return '''<svg viewBox="0 0 720 220" width="100%" height="220" role="img" aria-label="Bandwidth Delay Product Pipe Volume Conceptual Diagram">
  <title>Bandwidth-Delay Product Pipe Representation</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />

  <text x="360" y="28" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">Bandwidth-Delay Product (BDP) as a Transmission Pipe</text>

  <!-- Pipe Body -->
  <g transform="translate(60, 45)">
    <!-- Background of cylinder -->
    <rect x="50" y="20" width="500" height="90" fill="rgba(46,195,107,0.12)" stroke="none" />
    
    <!-- Top & bottom cylinder walls -->
    <line x1="50" y1="20" x2="550" y2="20" stroke="var(--ink)" stroke-width="2" />
    <line x1="50" y1="110" x2="550" y2="110" stroke="var(--ink)" stroke-width="2" />

    <!-- Left opening (ellipse) -->
    <ellipse cx="50" cy="65" rx="18" ry="45" fill="var(--surface-alt)" stroke="var(--ink)" stroke-width="2" />

    <!-- Bits inside pipe (flowing circles) -->
    <g fill="var(--green)" opacity="0.85">
      <circle cx="100" cy="45" r="5" /><circle cx="120" cy="75" r="5" /><circle cx="150" cy="55" r="5" />
      <circle cx="180" cy="85" r="5" /><circle cx="210" cy="45" r="5" /><circle cx="240" cy="65" r="5" />
      <circle cx="270" cy="50" r="5" /><circle cx="300" cy="80" r="5" /><circle cx="330" cy="60" r="5" />
      <circle cx="360" cy="40" r="5" /><circle cx="390" cy="70" r="5" /><circle cx="420" cy="55" r="5" />
      <circle cx="450" cy="85" r="5" /><circle cx="480" cy="50" r="5" /><circle cx="510" cy="75" r="5" />
    </g>

    <!-- Right end (ellipse) -->
    <ellipse cx="550" cy="65" rx="18" ry="45" fill="rgba(46,195,107,0.25)" stroke="var(--ink)" stroke-width="2" />

    <!-- Cross section dimension (Bandwidth) -->
    <line x1="15" y1="20" x2="15" y2="110" stroke="var(--ink)" stroke-width="1.5" />
    <polygon points="12,23 15,16 18,23" fill="var(--ink)" />
    <polygon points="12,107 15,114 18,107" fill="var(--ink)" />
    <text x="8" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="end">Cross-Section = Bandwidth (B)</text>

    <!-- Length dimension (Delay) -->
    <line x1="50" y1="125" x2="550" y2="125" stroke="var(--ink)" stroke-width="1.5" />
    <polygon points="53,122 46,125 53,128" fill="var(--ink)" />
    <polygon points="547,122 554,125 547,128" fill="var(--ink)" />
    <text x="300" y="142" fill="var(--ink)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">Length = Propagation Delay (T_prop)</text>

    <!-- Sender TX -->
    <text x="50" y="5" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">Transmitter</text>
    <!-- Receiver RX -->
    <text x="550" y="5" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">Receiver</text>
  </g>

  <!-- Central Volume formula -->
  <text x="360" y="200" fill="var(--ink)" font-family="var(--font-mono)" font-size="12" font-weight="700" text-anchor="middle">Pipe Volume = Bandwidth &times; Delay = Total Maximum Bits "In Flight" on the Link</text>
</svg>'''

def generate_hybrid_star_bus_svg():
    return '''<svg viewBox="0 0 720 280" width="100%" height="280" role="img" aria-label="Hybrid Network Topology: Star Backbone with 3 Bus Networks">
  <title>Hybrid Topology: Star Backbone with 3 Bus Networks (CIE-1 Question)</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />

  <text x="360" y="28" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">Hybrid Topology: Central Star Backbone with Three Bus Branches</text>

  <!-- Central Star Hub / Switch -->
  <g transform="translate(360, 85)">
    <circle cx="0" cy="0" r="32" fill="var(--surface-alt)" stroke="var(--green)" stroke-width="2.5" />
    <text x="0" y="-4" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">Central</text>
    <text x="0" y="12" fill="var(--green)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">Switch/Hub</text>
  </g>

  <!-- Branch 1: Bus Network 1 (Left) -->
  <g transform="translate(40, 160)">
    <!-- Backbone line from switch -->
    <path d="M 290 -75 L 120 0" stroke="var(--ink)" stroke-width="2" stroke-dasharray="4,3" />
    <!-- Bus backbone -->
    <line x1="20" y1="20" x2="220" y2="20" stroke="var(--ink)" stroke-width="3" />
    <!-- Terminators -->
    <rect x="15" y="14" width="6" height="12" fill="#B91C1C" />
    <rect x="219" y="14" width="6" height="12" fill="#B91C1C" />
    <text x="120" y="12" fill="var(--ink-muted)" font-family="var(--font-display)" font-size="10" font-weight="700" text-anchor="middle">Bus 1 (Finance)</text>
    <!-- Tap lines & PCs -->
    <line x1="50" y1="20" x2="50" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="35" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="50" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 1</text>

    <line x1="120" y1="20" x2="120" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="105" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="120" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 2</text>

    <line x1="190" y1="20" x2="190" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="175" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="190" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 3</text>
  </g>

  <!-- Branch 2: Bus Network 2 (Center Bottom) -->
  <g transform="translate(260, 160)">
    <!-- Backbone link from central switch -->
    <line x1="100" y1="-43" x2="100" y2="20" stroke="var(--ink)" stroke-width="2" stroke-dasharray="4,3" />
    <!-- Bus backbone -->
    <line x1="10" y1="20" x2="190" y2="20" stroke="var(--ink)" stroke-width="3" />
    <!-- Terminators -->
    <rect x="5" y="14" width="6" height="12" fill="#B91C1C" />
    <rect x="189" y="14" width="6" height="12" fill="#B91C1C" />
    <text x="100" y="12" fill="var(--ink-muted)" font-family="var(--font-display)" font-size="10" font-weight="700" text-anchor="middle">Bus 2 (Engineering)</text>
    <!-- Tap lines & PCs -->
    <line x1="40" y1="20" x2="40" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="25" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="40" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 4</text>

    <line x1="100" y1="20" x2="100" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="85" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="100" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 5</text>

    <line x1="160" y1="20" x2="160" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="145" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="160" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 6</text>
  </g>

  <!-- Branch 3: Bus Network 3 (Right) -->
  <g transform="translate(480, 160)">
    <!-- Backbone line from switch -->
    <path d="M -90 -75 L 80 0" stroke="var(--ink)" stroke-width="2" stroke-dasharray="4,3" />
    <!-- Bus backbone -->
    <line x1="10" y1="20" x2="210" y2="20" stroke="var(--ink)" stroke-width="3" />
    <!-- Terminators -->
    <rect x="5" y="14" width="6" height="12" fill="#B91C1C" />
    <rect x="209" y="14" width="6" height="12" fill="#B91C1C" />
    <text x="110" y="12" fill="var(--ink-muted)" font-family="var(--font-display)" font-size="10" font-weight="700" text-anchor="middle">Bus 3 (Admin)</text>
    <!-- Tap lines & PCs -->
    <line x1="40" y1="20" x2="40" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="25" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="40" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 7</text>

    <line x1="110" y1="20" x2="110" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="95" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="110" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 8</text>

    <line x1="180" y1="20" x2="180" y2="55" stroke="var(--ink)" stroke-width="1.5" />
    <rect x="165" y="55" width="30" height="22" rx="4" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="180" y="70" fill="var(--ink)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">PC 9</text>
  </g>

  <!-- Legend -->
  <text x="360" y="265" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Star links (dashed) connect central switch to drop taps; thick solid lines are terminated coaxial/twisted bus backbones.</text>
</svg>'''

if __name__ == '__main__':
    print("SVGs generated successfully.")
