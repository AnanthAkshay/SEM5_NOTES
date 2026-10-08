"""
generate_ml_u2_assets.py - Generates theme-aware SVGs for Machine Learning Unit 2:
- Figure 2.1: 2D Principal Component Analysis (PCA) Geometric Projection (Ramaiah CIE-2 2026 Q2.c)
- Figure 2.2: Version Space and General-to-Specific Hypothesis Lattice (Mitchell 1997 & CIE-1 Q3.b)
"""

def generate_pca_projection_svg():
    """Figure 2.1: 2D PCA Geometric Projection with Eigenvector Axes"""
    return '''<svg viewBox="0 0 780 360" width="100%" height="360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Principal Component Analysis 2D Geometric Projection">
  <defs>
    <marker id="pca-arr-pc1" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="pca-arr-pc2" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#3B82F6" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="350" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">PRINCIPAL COMPONENT ANALYSIS (PCA) GEOMETRIC PROJECTION (CIE-2 Q2.c)</text>

  <!-- Original Coordinate Axes centered at (390, 190) -->
  <line x1="120" y1="190" x2="660" y2="190" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4 4" />
  <text x="650" y="180" font-family="var(--font-mono)" font-size="11" fill="var(--ink-muted)" text-anchor="end">Original Feature x&#x2081;</text>

  <line x1="390" y1="50" x2="390" y2="330" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4 4" />
  <text x="400" y="65" font-family="var(--font-mono)" font-size="11" fill="var(--ink-muted)">Original Feature x&#x2082;</text>

  <!-- Origin / Mean Center -->
  <circle cx="390" cy="190" r="5" fill="var(--ink)" />
  <text x="402" y="205" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--ink)">Mean &mu; (0, 0)</text>

  <!-- PC1 Axis: Eigenvector e1 = [1, 1]/sqrt(2) -> 45 degree line (slope = -1 in SVG coords) -->
  <line x1="200" y1="310" x2="580" y2="70" stroke="var(--brand)" stroke-width="2.5" marker-end="url(#pca-arr-pc1)" />
  <text x="590" y="65" font-family="var(--font-mono)" font-size="12" font-weight="800" fill="var(--brand)">PC1 (&lambda;&#x2081; = 6.0, 75.0% Var)</text>
  <text x="590" y="80" font-family="var(--font-mono)" font-size="9.5" fill="var(--brand)">v&#x2081; = [0.707, 0.707]&#x1d40;</text>

  <!-- PC2 Axis: Eigenvector e2 = [1, -1]/sqrt(2) -> -45 degree line (perpendicular to PC1) -->
  <line x1="260" y1="60" x2="520" y2="320" stroke="#3B82F6" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#pca-arr-pc2)" />
  <text x="530" y="325" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="#3B82F6">PC2 (&lambda;&#x2082; = 2.0, 25.0% Var)</text>
  <text x="530" y="340" font-family="var(--font-mono)" font-size="9.5" fill="#3B82F6">v&#x2082; = [0.707, -0.707]&#x1d40;</text>

  <!-- Ellipse of Variance along PC1 -->
  <ellipse cx="390" cy="190" rx="180" ry="60" transform="rotate(-45 390 190)" fill="var(--brand)" fill-opacity="0.08" stroke="var(--brand)" stroke-width="1.2" stroke-dasharray="5 4" />

  <!-- Data Points and Orthogonal Projections onto PC1 -->
  <!-- Point 1: (300, 260) -> projected onto PC1 line -->
  <circle cx="280" cy="270" r="5" fill="#10B981" />
  <line x1="280" y1="270" x2="295" y2="250" stroke="var(--ink-muted)" stroke-width="1.2" stroke-dasharray="3 3" />
  <circle cx="295" cy="250" r="3.5" fill="var(--brand)" />

  <!-- Point 2: (340, 220) -->
  <circle cx="330" cy="235" r="5" fill="#10B981" />
  <line x1="330" y1="235" x2="342" y2="220" stroke="var(--ink-muted)" stroke-width="1.2" stroke-dasharray="3 3" />
  <circle cx="342" cy="220" r="3.5" fill="var(--brand)" />

  <!-- Point 3: (450, 150) -->
  <circle cx="460" cy="140" r="5" fill="#10B981" />
  <line x1="460" y1="140" x2="445" y2="155" stroke="var(--ink-muted)" stroke-width="1.2" stroke-dasharray="3 3" />
  <circle cx="445" cy="155" r="3.5" fill="var(--brand)" />

  <!-- Point 4: (490, 110) -->
  <circle cx="510" cy="100" r="5" fill="#10B981" />
  <line x1="510" y1="100" x2="495" y2="120" stroke="var(--ink-muted)" stroke-width="1.2" stroke-dasharray="3 3" />
  <circle cx="495" cy="120" r="3.5" fill="var(--brand)" />

  <!-- Legend Box -->
  <g transform="translate(30, 260)">
    <rect width="210" height="75" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <circle cx="15" cy="18" r="4.5" fill="#10B981" />
    <text x="28" y="22" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Original 2D Data Points</text>
    <circle cx="15" cy="38" r="3.5" fill="var(--brand)" />
    <text x="28" y="42" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">1D Projected Coordinates</text>
    <line x1="8" y1="58" x2="22" y2="58" stroke="var(--brand)" stroke-width="2" />
    <text x="28" y="62" font-family="var(--font-body)" font-size="10.5" font-weight="700" fill="var(--brand)">Principal Component 1 Axis</text>
  </g>
</svg>'''

def generate_version_space_svg():
    """Figure 2.2: Version Space & Hypothesis Lattice (Mitchell 1997 & CIE-1 Q3.b)"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Version Space and Hypothesis Lattice">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">VERSION SPACE &amp; GENERAL-TO-SPECIFIC HYPOTHESIS ORDERING (MITCHELL 1997)</text>

  <!-- General Boundary G at Top -->
  <g transform="translate(140, 55)">
    <rect width="500" height="50" rx="10" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="2" />
    <text x="250" y="24" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)" text-anchor="middle">GENERAL BOUNDARY G&#x2080; = { &lang; ?, ?, ?, ?, ?, ? &rang; }</text>
    <text x="250" y="40" font-family="var(--font-body)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">Maximally general hypotheses consistent with training data D</text>
  </g>

  <!-- Arrow pointing down: More Specific -->
  <line x1="90" y1="70" x2="90" y2="270" stroke="var(--ink-muted)" stroke-width="1.5" />
  <polyline points="85 260, 90 270, 95 260" fill="none" stroke="var(--ink-muted)" stroke-width="1.5" />
  <text x="80" y="170" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--ink-muted)" transform="rotate(-90 80 170)" text-anchor="middle">MORE SPECIFIC (&ge;&#x2092;) &rarr;</text>

  <!-- Version Space Shaded Convex Hull -->
  <path d="M 190 105 L 590 105 L 510 235 L 270 235 Z" fill="var(--green-tint)" fill-opacity="0.12" stroke="var(--green)" stroke-width="1.5" stroke-dasharray="5 3" />
  <text x="390" y="170" font-family="var(--font-mono)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">VERSION SPACE VS&#x1d34;,&#x1d30;</text>
  <text x="390" y="188" font-family="var(--font-body)" font-size="10" fill="var(--green)" text-anchor="middle">All hypotheses h &isin; H consistent with all positive and negative samples</text>

  <!-- Intermediate Hypotheses inside Version Space -->
  <g transform="translate(220, 130)">
    <rect width="160" height="26" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="80" y="17" font-family="var(--font-mono)" font-size="9" fill="var(--ink)" text-anchor="middle">&lang; Sunny, ?, ?, Strong, ?, ? &rang;</text>
  </g>
  <g transform="translate(400, 130)">
    <rect width="160" height="26" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="80" y="17" font-family="var(--font-mono)" font-size="9" fill="var(--ink)" text-anchor="middle">&lang; Sunny, Warm, ?, ?, ?, ? &rang;</text>
  </g>

  <!-- Specific Boundary S at Bottom -->
  <g transform="translate(190, 235)">
    <rect width="400" height="50" rx="10" fill="var(--surface-alt)" stroke="var(--green)" stroke-width="2" />
    <text x="200" y="24" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--green)" text-anchor="middle">SPECIFIC BOUNDARY S = { &lang; Sunny, Warm, ?, Strong, ?, ? &rang; }</text>
    <text x="200" y="40" font-family="var(--font-body)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">Maximally specific hypotheses consistent with training data D</text>
  </g>

  <!-- S0 Initial State -->
  <g transform="translate(260, 295)">
    <text x="130" y="18" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">Initial S&#x2080; = &lang; &Phi;, &Phi;, &Phi;, &Phi;, &Phi;, &Phi; &rang; (Zero Coverage)</text>
  </g>
</svg>'''
