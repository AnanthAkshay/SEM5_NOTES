"""
generate_ml_u1_assets.py - Generates theme-aware SVGs for Machine Learning Unit 1:
- Figure 1.2: End-to-End Machine Learning Process Pipeline (Ramaiah SEE 2026 Q1.a)
- Figure 1.3: Bias-Variance Trade-off & Model Complexity Curve (Ramaiah SEE 2026 Q1.c)
- Figure 1.4: Confusion Matrix & Performance Metrics Map (Ramaiah CIE-1 2026 Q2.a & SEE 2026 Q1.b)
"""

def generate_ml_process_pipeline_svg():
    """Figure 1.2: 7-Stage End-to-End ML Pipeline Flowchart"""
    return '''<svg viewBox="0 0 880 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="End-to-End Machine Learning Process Pipeline">
  <defs>
    <marker id="ml-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="ml-arr-feedback" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#EF4444" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="870" height="250" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">MACHINE LEARNING ENGINEERING PIPELINE (RAMAIAH SEE 2026 Q1.a)</text>

  <!-- Stage 1: Problem Formulation -->
  <g transform="translate(20, 60)">
    <rect width="105" height="110" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <circle cx="52" cy="30" r="14" fill="var(--brand-tint)" />
    <text x="52" y="35" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">01</text>
    <text x="52" y="65" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Problem</text>
    <text x="52" y="80" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Formulation</text>
    <text x="52" y="98" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Task (T) &amp; P</text>
  </g>

  <!-- Arrow 1->2 -->
  <line x1="125" y1="115" x2="140" y2="115" stroke="var(--brand)" stroke-width="2" marker-end="url(#ml-arr)" />

  <!-- Stage 2: Data Ingestion -->
  <g transform="translate(142, 60)">
    <rect width="105" height="110" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <circle cx="52" cy="30" r="14" fill="var(--brand-tint)" />
    <text x="52" y="35" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">02</text>
    <text x="52" y="65" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Data</text>
    <text x="52" y="80" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Collection</text>
    <text x="52" y="98" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Big Data 5Vs</text>
  </g>

  <!-- Arrow 2->3 -->
  <line x1="247" y1="115" x2="262" y2="115" stroke="var(--brand)" stroke-width="2" marker-end="url(#ml-arr)" />

  <!-- Stage 3: Preprocessing & Cleaning -->
  <g transform="translate(264, 60)">
    <rect width="105" height="110" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <circle cx="52" cy="30" r="14" fill="var(--brand-tint)" />
    <text x="52" y="35" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">03</text>
    <text x="52" y="65" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Data Cleaning</text>
    <text x="52" y="80" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">&amp; Imputation</text>
    <text x="52" y="98" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Outlier Fences</text>
  </g>

  <!-- Arrow 3->4 -->
  <line x1="369" y1="115" x2="384" y2="115" stroke="var(--brand)" stroke-width="2" marker-end="url(#ml-arr)" />

  <!-- Stage 4: Feature Engineering -->
  <g transform="translate(386, 60)">
    <rect width="105" height="110" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <circle cx="52" cy="30" r="14" fill="var(--brand-tint)" />
    <text x="52" y="35" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">04</text>
    <text x="52" y="65" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Feature</text>
    <text x="52" y="80" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Engineering</text>
    <text x="52" y="98" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Z-score / Min-Max</text>
  </g>

  <!-- Arrow 4->5 -->
  <line x1="491" y1="115" x2="506" y2="115" stroke="var(--brand)" stroke-width="2" marker-end="url(#ml-arr)" />

  <!-- Stage 5: Model Training -->
  <g transform="translate(508, 60)">
    <rect width="105" height="110" rx="10" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.8" />
    <circle cx="52" cy="30" r="14" fill="var(--brand)" />
    <text x="52" y="35" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">05</text>
    <text x="52" y="65" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--brand)" text-anchor="middle">Model</text>
    <text x="52" y="80" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--brand)" text-anchor="middle">Training</text>
    <text x="52" y="98" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Loss Minimization</text>
  </g>

  <!-- Arrow 5->6 -->
  <line x1="613" y1="115" x2="628" y2="115" stroke="var(--brand)" stroke-width="2" marker-end="url(#ml-arr)" />

  <!-- Stage 6: Evaluation & Diagnostics -->
  <g transform="translate(630, 60)">
    <rect width="105" height="110" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <circle cx="52" cy="30" r="14" fill="var(--brand-tint)" />
    <text x="52" y="35" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">06</text>
    <text x="52" y="65" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Evaluation &amp;</text>
    <text x="52" y="80" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Diagnostics</text>
    <text x="52" y="98" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Confusion Matrix</text>
  </g>

  <!-- Arrow 6->7 -->
  <line x1="735" y1="115" x2="750" y2="115" stroke="var(--brand)" stroke-width="2" marker-end="url(#ml-arr)" />

  <!-- Stage 7: Deployment & Monitoring -->
  <g transform="translate(752, 60)">
    <rect width="105" height="110" rx="10" fill="var(--surface-alt)" stroke="var(--green)" stroke-width="1.5" />
    <circle cx="52" cy="30" r="14" fill="var(--green-tint)" />
    <text x="52" y="35" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--green)" text-anchor="middle">07</text>
    <text x="52" y="65" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--green)" text-anchor="middle">Deploy &amp;</text>
    <text x="52" y="80" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--green)" text-anchor="middle">Monitor</text>
    <text x="52" y="98" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Concept Drift</text>
  </g>

  <!-- Feedback Loop Arrow from Stage 6 back to Stage 4 & 5 -->
  <path d="M 682 170 L 682 215 L 438 215 L 438 175" fill="none" stroke="#EF4444" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#ml-arr-feedback)" />
  <rect x="500" y="203" width="130" height="24" rx="6" fill="var(--surface)" stroke="#EF4444" stroke-width="1" />
  <text x="565" y="219" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="#EF4444" text-anchor="middle">&#x21a9; Hyperparameter Loop</text>
</svg>'''

def generate_bias_variance_svg():
    """Figure 1.3: Bias-Variance Tradeoff vs Model Complexity (Ramaiah SEE 2026 Q1.c)"""
    return '''<svg viewBox="0 0 780 360" width="100%" height="360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bias-Variance Tradeoff Curve vs Model Complexity">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="350" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">BIAS-VARIANCE TRADEOFF &amp; ERROR DYNAMICS (RAMAIAH SEE 2026 Q1.c)</text>

  <!-- Axes -->
  <!-- Y Axis: Error -->
  <line x1="80" y1="50" x2="80" y2="290" stroke="var(--ink-muted)" stroke-width="2" />
  <text x="40" y="160" font-family="var(--font-body)" font-size="12" font-weight="700" fill="var(--ink)" transform="rotate(-90 40 160)" text-anchor="middle">Total Prediction Error</text>
  <!-- X Axis: Model Complexity -->
  <line x1="80" y1="290" x2="740" y2="290" stroke="var(--ink-muted)" stroke-width="2" />
  <text x="410" y="325" font-family="var(--font-body)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">Model Complexity (Degrees of Freedom / Tree Depth / Polynomial Degree)</text>

  <!-- Shaded Zones: Underfitting, Optimal, Overfitting -->
  <!-- Underfitting Zone -->
  <rect x="80" y="50" width="230" height="240" fill="#3B82F6" fill-opacity="0.06" />
  <text x="195" y="75" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="#3B82F6" text-anchor="middle">UNDERFITTING ZONE</text>
  <text x="195" y="92" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">High Bias &bull; Low Variance</text>

  <!-- Optimal Sweet Spot -->
  <rect x="310" y="50" width="160" height="240" fill="var(--green-tint)" fill-opacity="0.12" />
  <line x1="390" y1="50" x2="390" y2="290" stroke="var(--green)" stroke-width="1.8" stroke-dasharray="4 3" />
  <text x="390" y="75" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--green)" text-anchor="middle">OPTIMAL COMPLEXITY</text>
  <text x="390" y="92" font-family="var(--font-mono)" font-size="9.5" fill="var(--green)" text-anchor="middle">Min Total Test Error</text>

  <!-- Overfitting Zone -->
  <rect x="470" y="50" width="270" height="240" fill="#EF4444" fill-opacity="0.06" />
  <text x="605" y="75" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="#EF4444" text-anchor="middle">OVERFITTING ZONE</text>
  <text x="605" y="92" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="middle">Low Bias &bull; High Variance</text>

  <!-- Irreducible Error baseline sigma^2 -->
  <line x1="80" y1="260" x2="740" y2="260" stroke="var(--ink-muted)" stroke-width="1" stroke-dasharray="3 3" />
  <text x="735" y="254" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink-muted)" text-anchor="end">Irreducible Error &sigma;&sup2;</text>

  <!-- Curve 1: Bias^2 (Decreasing monotonic) -->
  <path d="M 90 80 Q 220 220 730 255" fill="none" stroke="#3B82F6" stroke-width="2.5" />
  <text x="140" y="115" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="#3B82F6">Bias&sup2;</text>

  <!-- Curve 2: Variance (Increasing monotonic) -->
  <path d="M 90 258 Q 450 255 730 85" fill="none" stroke="#EF4444" stroke-width="2.5" />
  <text x="690" y="110" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="#EF4444">Variance</text>

  <!-- Curve 3: Training Error (Continues dropping near zero) -->
  <path d="M 90 140 Q 300 240 730 257" fill="none" stroke="var(--ink-muted)" stroke-width="2" stroke-dasharray="6 3" />
  <text x="620" y="275" font-family="var(--font-mono)" font-size="10" font-weight="600" fill="var(--ink-muted)">Training Error</text>

  <!-- Curve 4: Total Test/Validation Error (U-shaped convex curve) -->
  <!-- Min at x=390, y=145 -->
  <path d="M 90 110 Q 260 170 390 148 Q 520 160 730 95" fill="none" stroke="var(--brand)" stroke-width="3" />
  <circle cx="390" cy="148" r="5" fill="var(--brand)" />
  <text x="390" y="133" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)" text-anchor="middle">Min Test Error</text>

  <!-- Legend Box -->
  <rect x="85" y="338" width="650" height="1" fill="none" />
</svg>'''

def generate_confusion_matrix_svg():
    """Figure 1.4: 2x2 Confusion Matrix & Diagnostic Metrics Map (Ramaiah CIE-1 2026 Q2.a)"""
    return '''<svg viewBox="0 0 780 370" width="100%" height="370" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Confusion Matrix and Diagnostic Classification Metrics Map">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="360" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">CONFUSION MATRIX &amp; DIAGNOSTIC FORMULAS (RAMAIAH CIE-1 2026 Q2.a &amp; SEE Q1.b)</text>

  <!-- Axis Headers -->
  <text x="260" y="65" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--brand)" text-anchor="middle">PREDICTED POSITIVE</text>
  <text x="440" y="65" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--brand)" text-anchor="middle">PREDICTED NEGATIVE</text>
  <text x="630" y="65" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" text-anchor="middle">ROW MARGINALS</text>

  <!-- Row Headers -->
  <text x="40" y="130" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="start">ACTUAL POSITIVE</text>
  <text x="40" y="145" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="start">(Spam / Sick: P = 80)</text>

  <text x="40" y="225" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="start">ACTUAL NEGATIVE</text>
  <text x="40" y="240" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="start">(Ham / Healthy: N = 70)</text>

  <text x="80" y="315" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">COLUMN MARGINALS</text>

  <!-- Cell 1: True Positive (TP) -->
  <rect x="180" y="85" width="160" height="85" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.8" />
  <text x="260" y="112" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="var(--green)" text-anchor="middle">True Positive (TP)</text>
  <text x="260" y="138" font-family="var(--font-display)" font-size="22" font-weight="800" fill="var(--ink)" text-anchor="middle">70</text>
  <text x="260" y="156" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">Correctly flagged spam</text>

  <!-- Cell 2: False Negative (FN) - Type II Error -->
  <rect x="360" y="85" width="160" height="85" rx="8" fill="#EF4444" fill-opacity="0.1" stroke="#EF4444" stroke-width="1.5" />
  <text x="440" y="112" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#EF4444" text-anchor="middle">False Negative (FN)</text>
  <text x="440" y="138" font-family="var(--font-display)" font-size="22" font-weight="800" fill="#EF4444" text-anchor="middle">10</text>
  <text x="440" y="156" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">Missed spam &bull; Type II</text>

  <!-- Row 1 Marginal: Recall / Sensitivity -->
  <rect x="540" y="85" width="180" height="85" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="630" y="110" font-family="var(--font-body)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">Recall / Sensitivity</text>
  <text x="630" y="130" font-family="var(--font-mono)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">TP / (TP + FN) = 70 / 80</text>
  <text x="630" y="155" font-family="var(--font-mono)" font-size="16" font-weight="800" fill="var(--green)" text-anchor="middle">87.50% (0.875)</text>

  <!-- Cell 3: False Positive (FP) - Type I Error -->
  <rect x="180" y="180" width="160" height="85" rx="8" fill="#EF4444" fill-opacity="0.1" stroke="#EF4444" stroke-width="1.5" />
  <text x="260" y="207" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="#EF4444" text-anchor="middle">False Positive (FP)</text>
  <text x="260" y="233" font-family="var(--font-display)" font-size="22" font-weight="800" fill="#EF4444" text-anchor="middle">20</text>
  <text x="260" y="251" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">False alarm &bull; Type I</text>

  <!-- Cell 4: True Negative (TN) -->
  <rect x="360" y="180" width="160" height="85" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.8" />
  <text x="440" y="207" font-family="var(--font-mono)" font-size="12" font-weight="700" fill="var(--green)" text-anchor="middle">True Negative (TN)</text>
  <text x="440" y="233" font-family="var(--font-display)" font-size="22" font-weight="800" fill="var(--ink)" text-anchor="middle">50</text>
  <text x="440" y="251" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">Correctly kept clean ham</text>

  <!-- Row 2 Marginal: Specificity -->
  <rect x="540" y="180" width="180" height="85" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="630" y="205" font-family="var(--font-body)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">Specificity (TNR)</text>
  <text x="630" y="225" font-family="var(--font-mono)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">TN / (TN + FP) = 50 / 70</text>
  <text x="630" y="250" font-family="var(--font-mono)" font-size="16" font-weight="800" fill="var(--brand)" text-anchor="middle">71.43% (0.714)</text>

  <!-- Col 1 Marginal: Precision -->
  <rect x="180" y="275" width="160" height="75" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="260" y="297" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Precision (PPV)</text>
  <text x="260" y="315" font-family="var(--font-mono)" font-size="10.5" fill="var(--ink-muted)" text-anchor="middle">TP/(TP+FP) = 70/90</text>
  <text x="260" y="338" font-family="var(--font-mono)" font-size="15" font-weight="800" fill="var(--brand)" text-anchor="middle">77.78% (0.778)</text>

  <!-- Col 2 Marginal: Negative Predictive Value -->
  <rect x="360" y="275" width="160" height="75" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
  <text x="440" y="297" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Neg. Pred. Value</text>
  <text x="440" y="315" font-family="var(--font-mono)" font-size="10.5" fill="var(--ink-muted)" text-anchor="middle">TN/(TN+FN) = 50/60</text>
  <text x="440" y="338" font-family="var(--font-mono)" font-size="15" font-weight="800" fill="var(--ink)" text-anchor="middle">83.33% (0.833)</text>

  <!-- Bottom-Right Summary Box: Accuracy & F1-Score -->
  <rect x="540" y="275" width="180" height="75" rx="8" fill="var(--brand-tint)" stroke="var(--brand)" stroke-width="1.8" />
  <text x="630" y="297" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--brand)" text-anchor="middle">Overall Diagnostics</text>
  <text x="630" y="316" font-family="var(--font-mono)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">Accuracy: 80.00% (120/150)</text>
  <text x="630" y="336" font-family="var(--font-mono)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">F1-Score: 82.35% (0.8235)</text>
</svg>'''
