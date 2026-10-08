"""
generate_ml_u3_assets.py - Generates theme-aware SVGs for Machine Learning Unit 3:
- Figure 3.1: Linear Regression OLS Best-Fit Line & Residuals (Ramaiah CIE-1 2026 Q1.c)
- Figure 3.2: Complete ID3 Decision Tree for Play Tennis (Ramaiah CIE-1 Q3.c & SEE Q5.b)
"""

def generate_linear_regression_svg():
    """Figure 3.1: Linear Regression OLS Best-Fit Line and Residuals"""
    return '''<svg viewBox="0 0 780 360" width="100%" height="360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ordinary Least Squares Linear Regression Best-Fit Line and Residuals">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="350" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">ORDINARY LEAST SQUARES (OLS) REGRESSION &amp; RESIDUALS (RAMAIAH CIE-1 Q1.c)</text>

  <!-- Axes: X = 0 to 12 (mapped to pixel x: 90 to 710), Y = 40 to 100 (mapped to pixel y: 310 to 60) -->
  <!-- Y Axis -->
  <line x1="90" y1="50" x2="90" y2="310" stroke="var(--ink-muted)" stroke-width="2" />
  <text x="45" y="180" font-family="var(--font-body)" font-size="12" font-weight="700" fill="var(--ink)" transform="rotate(-90 45 180)" text-anchor="middle">Exam Marks Y (%)</text>
  <!-- Y Ticks: 40, 50, 60, 70, 80, 90, 100 -->
  <text x="80" y="314" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="end">40</text>
  <text x="80" y="272" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="end">50</text>
  <text x="80" y="230" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="end">60</text>
  <text x="80" y="188" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="end">70</text>
  <text x="80" y="146" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="end">80</text>
  <text x="80" y="104" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="end">90</text>
  <text x="80" y="62" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="end">100</text>

  <!-- X Axis -->
  <line x1="90" y1="310" x2="730" y2="310" stroke="var(--ink-muted)" stroke-width="2" />
  <text x="410" y="342" font-family="var(--font-body)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">Study Hours X (Hours / Week)</text>
  <!-- X Ticks: 0, 2, 4, 6, 7, 8, 10, 12 -->
  <text x="90" y="325" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">0</text>
  <text x="193" y="325" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">2</text>
  <text x="296" y="325" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">4</text>
  <text x="400" y="325" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">6</text>
  <text x="451" y="325" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">7*</text>
  <text x="503" y="325" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">8</text>
  <text x="606" y="325" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">10</text>

  <!-- Regression Line: Y = 4.50*X + 41.00 -->
  <!-- At X=0: Y=41.00 -> y = 310 - (1/60)*250 = 305.8 -->
  <!-- At X=11: Y=90.50 -> y = 310 - (50.5/60)*250 = 99.6 -->
  <!-- x_scale = 51.67 px / unit, y_scale = 4.167 px / unit from 40 -->
  <line x1="90" y1="306" x2="658" y2="99" stroke="var(--brand)" stroke-width="2.5" />
  <text x="665" y="95" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)">&#x177; = 4.50X + 41.00</text>

  <!-- Data Points: (2, 50), (4, 60), (6, 65), (8, 80), (10, 85) -->
  <!-- Point 1: X=2 (193), Y=50 (268). Fitted Y=50.0 (268) -> residual = 0 -->
  <line x1="193" y1="268" x2="193" y2="268" stroke="#EF4444" stroke-width="1.8" />
  <circle cx="193" cy="268" r="5.5" fill="var(--green)" />
  <text x="193" y="258" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)" text-anchor="middle">(2, 50)</text>

  <!-- Point 2: X=4 (297), Y=60 (227). Fitted Y=59.0 (231) -> residual = +1.0 -->
  <line x1="297" y1="227" x2="297" y2="231" stroke="#EF4444" stroke-width="2" />
  <circle cx="297" cy="227" r="5.5" fill="var(--green)" />
  <text x="297" y="217" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)" text-anchor="middle">(4, 60)</text>

  <!-- Point 3: X=6 (400), Y=65 (206). Fitted Y=68.0 (193) -> residual = -3.0 -->
  <line x1="400" y1="206" x2="400" y2="193" stroke="#EF4444" stroke-width="2" stroke-dasharray="3 2" />
  <circle cx="400" cy="206" r="5.5" fill="var(--green)" />
  <text x="400" y="222" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)" text-anchor="middle">(6, 65)</text>

  <!-- Point 4: X=8 (503), Y=80 (143). Fitted Y=77.0 (156) -> residual = +3.0 -->
  <line x1="503" y1="143" x2="503" y2="156" stroke="#EF4444" stroke-width="2" stroke-dasharray="3 2" />
  <circle cx="503" cy="143" r="5.5" fill="var(--green)" />
  <text x="503" y="133" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)" text-anchor="middle">(8, 80)</text>

  <!-- Point 5: X=10 (606), Y=85 (122). Fitted Y=86.0 (118) -> residual = -1.0 -->
  <line x1="606" y1="122" x2="606" y2="118" stroke="#EF4444" stroke-width="2" />
  <circle cx="606" cy="122" r="5.5" fill="var(--green)" />
  <text x="606" y="138" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)" text-anchor="middle">(10, 85)</text>

  <!-- Target Prediction for X=7: Fitted Y = 4.5*7 + 41 = 72.50 (175) -->
  <line x1="451" y1="310" x2="451" y2="175" stroke="var(--brand)" stroke-width="1.8" stroke-dasharray="4 3" />
  <line x1="90" y1="175" x2="451" y2="175" stroke="var(--brand)" stroke-width="1.8" stroke-dasharray="4 3" />
  <circle cx="451" cy="175" r="6" fill="var(--brand)" stroke="#FFFFFF" stroke-width="2" />
  <rect x="462" y="160" width="160" height="26" rx="6" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.2" />
  <text x="542" y="177" font-family="var(--font-mono)" font-size="10.5" font-weight="800" fill="var(--brand)" text-anchor="middle">&#x177;(7) = 72.50 Marks</text>

  <!-- Legend Box -->
  <g transform="translate(110, 60)">
    <rect width="210" height="65" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <circle cx="15" cy="16" r="4.5" fill="var(--green)" />
    <text x="26" y="20" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Observed Sample (x&#x1d62;, y&#x1d62;)</text>
    <line x1="8" y1="36" x2="22" y2="36" stroke="var(--brand)" stroke-width="2.5" />
    <text x="26" y="40" font-family="var(--font-body)" font-size="10.5" font-weight="700" fill="var(--brand)">OLS Fitted Regression Line</text>
    <line x1="8" y1="52" x2="22" y2="52" stroke="#EF4444" stroke-width="2" stroke-dasharray="3 2" />
    <text x="26" y="55" font-family="var(--font-body)" font-size="10.5" fill="#EF4444">Residual e&#x1d62; = y&#x1d62; - &#x177;&#x1d62;</text>
  </g>
</svg>'''

def generate_decision_tree_svg():
    """Figure 3.2: Complete ID3 Decision Tree for Play Tennis (Ramaiah CIE-1 Q3.c & SEE Q5.b)"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Complete ID3 Decision Tree for Play Tennis">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">COMPLETE INDUCED ID3 DECISION TREE (RAMAIAH CIE-1 Q3.c &amp; SEE Q5.b)</text>

  <!-- Root Node: Outlook (IG = 0.3219) -->
  <g transform="translate(320, 50)">
    <rect width="140" height="44" rx="8" fill="var(--brand-tint)" stroke="var(--brand)" stroke-width="2" />
    <text x="70" y="22" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--brand)" text-anchor="middle">OUTLOOK?</text>
    <text x="70" y="36" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">IG = 0.3219 (Max)</text>
  </g>

  <!-- Branch 1: Outlook = Sunny (Left) -->
  <line x1="340" y1="94" x2="190" y2="160" stroke="var(--ink-muted)" stroke-width="1.8" />
  <rect x="220" y="115" width="65" height="20" rx="4" fill="var(--surface-alt)" stroke="var(--border)" />
  <text x="252" y="129" font-family="var(--font-mono)" font-size="9.5" font-weight="600" fill="var(--ink)" text-anchor="middle">Sunny (4)</text>

  <!-- Branch 2: Outlook = Overcast (Middle) -->
  <line x1="390" y1="94" x2="390" y2="160" stroke="var(--ink-muted)" stroke-width="1.8" />
  <rect x="355" y="115" width="70" height="20" rx="4" fill="var(--surface-alt)" stroke="var(--border)" />
  <text x="390" y="129" font-family="var(--font-mono)" font-size="9.5" font-weight="600" fill="var(--ink)" text-anchor="middle">Overcast (2)</text>

  <!-- Branch 3: Outlook = Rain (Right) -->
  <line x1="440" y1="94" x2="590" y2="160" stroke="var(--ink-muted)" stroke-width="1.8" />
  <rect x="495" y="115" width="60" height="20" rx="4" fill="var(--surface-alt)" stroke="var(--border)" />
  <text x="525" y="129" font-family="var(--font-mono)" font-size="9.5" font-weight="600" fill="var(--ink)" text-anchor="middle">Rain (4)</text>

  <!-- Level 1 Left Internal Node: Humidity -->
  <g transform="translate(120, 160)">
    <rect width="140" height="44" rx="8" fill="var(--brand-tint)" stroke="var(--brand)" stroke-width="1.8" />
    <text x="70" y="22" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">HUMIDITY?</text>
    <text x="70" y="36" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">IG = 0.8113</text>
  </g>

  <!-- Level 1 Middle Leaf: Pure YES (2+, 0-) -->
  <g transform="translate(340, 160)">
    <rect width="100" height="44" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="2" />
    <text x="50" y="24" font-family="var(--font-display)" font-size="13" font-weight="800" fill="var(--green)" text-anchor="middle">YES &check;</text>
    <text x="50" y="38" font-family="var(--font-mono)" font-size="9.5" fill="var(--green)" text-anchor="middle">Pure (2+, 0-)</text>
  </g>

  <!-- Level 1 Right Internal Node: Wind -->
  <g transform="translate(520, 160)">
    <rect width="140" height="44" rx="8" fill="var(--brand-tint)" stroke="var(--brand)" stroke-width="1.8" />
    <text x="70" y="22" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">WIND?</text>
    <text x="70" y="36" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">IG = 0.8113</text>
  </g>

  <!-- Level 2 Subtree under Humidity -->
  <!-- Humidity = High -> NO -->
  <line x1="150" y1="204" x2="100" y2="255" stroke="var(--ink-muted)" stroke-width="1.5" />
  <rect x="75" y="220" width="50" height="18" rx="4" fill="var(--surface-alt)" stroke="var(--border)" />
  <text x="100" y="232" font-family="var(--font-mono)" font-size="9" fill="var(--ink)" text-anchor="middle">High (3)</text>
  <g transform="translate(55, 255)">
    <rect width="90" height="40" rx="8" fill="#EF4444" fill-opacity="0.12" stroke="#EF4444" stroke-width="1.8" />
    <text x="45" y="22" font-family="var(--font-display)" font-size="12" font-weight="800" fill="#EF4444" text-anchor="middle">NO &cross;</text>
    <text x="45" y="35" font-family="var(--font-mono)" font-size="9" fill="#EF4444" text-anchor="middle">Pure (0+, 3-)</text>
  </g>

  <!-- Humidity = Normal -> YES -->
  <line x1="230" y1="204" x2="270" y2="255" stroke="var(--ink-muted)" stroke-width="1.5" />
  <rect x="235" y="220" width="65" height="18" rx="4" fill="var(--surface-alt)" stroke="var(--border)" />
  <text x="267" y="232" font-family="var(--font-mono)" font-size="9" fill="var(--ink)" text-anchor="middle">Normal (1)</text>
  <g transform="translate(230, 255)">
    <rect width="90" height="40" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.8" />
    <text x="45" y="22" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">YES &check;</text>
    <text x="45" y="35" font-family="var(--font-mono)" font-size="9" fill="var(--green)" text-anchor="middle">Pure (1+, 0-)</text>
  </g>

  <!-- Level 2 Subtree under Wind -->
  <!-- Wind = Weak -> YES -->
  <line x1="550" y1="204" x2="500" y2="255" stroke="var(--ink-muted)" stroke-width="1.5" />
  <rect x="480" y="220" width="55" height="18" rx="4" fill="var(--surface-alt)" stroke="var(--border)" />
  <text x="507" y="232" font-family="var(--font-mono)" font-size="9" fill="var(--ink)" text-anchor="middle">Weak (3)</text>
  <g transform="translate(455, 255)">
    <rect width="90" height="40" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.8" />
    <text x="45" y="22" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">YES &check;</text>
    <text x="45" y="35" font-family="var(--font-mono)" font-size="9" fill="var(--green)" text-anchor="middle">Pure (3+, 0-)</text>
  </g>

  <!-- Wind = Strong -> NO -->
  <line x1="630" y1="204" x2="680" y2="255" stroke="var(--ink-muted)" stroke-width="1.5" />
  <rect x="640" y="220" width="60" height="18" rx="4" fill="var(--surface-alt)" stroke="var(--border)" />
  <text x="670" y="232" font-family="var(--font-mono)" font-size="9" fill="var(--ink)" text-anchor="middle">Strong (1)</text>
  <g transform="translate(635, 255)">
    <rect width="90" height="40" rx="8" fill="#EF4444" fill-opacity="0.12" stroke="#EF4444" stroke-width="1.8" />
    <text x="45" y="22" font-family="var(--font-display)" font-size="12" font-weight="800" fill="#EF4444" text-anchor="middle">NO &cross;</text>
    <text x="45" y="35" font-family="var(--font-mono)" font-size="9" fill="#EF4444" text-anchor="middle">Pure (0+, 1-)</text>
  </g>
</svg>'''
