"""
build_ml_u1_enriched.py - Programmatically enriches Machine Learning Unit 1 notes:
- Academic Verification Box (S. Sridhar & M. Vijayalakshmi 2021 OUP, Tom Mitchell 1997, Ramaiah CIE-1 March 2026, SEE June/July 2026)
- Accurate Official Syllabus Topics in Hero Card
- 3 Theme-Aware SVG Figures:
  - Figure 1.2: End-to-End ML Pipeline (SEE 2026 Q1.a)
  - Figure 1.3: Bias-Variance Tradeoff Curve (SEE 2026 Q1.c)
  - Figure 1.4: 2x2 Confusion Matrix & Diagnostic Metrics Map (CIE-1 2026 Q2.a & SEE 2026 Q1.b)
- Interactive Confusion Matrix & Diagnostic Performance Metrics Analyzer in Vanilla JS
- Fully transcribed, authentically solved examination questions from Ramaiah CIE-1 and SEE 2026
- 6 Verified Practice Problems with hidden solutions
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_ml_u1_assets import (
    generate_ml_process_pipeline_svg,
    generate_bias_variance_svg,
    generate_confusion_matrix_svg
)

def build():
    path = "notes/ml/unit1/unit-1-notes.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. ACADEMIC VERIFICATION BOX
    verif_box = '''        <div class="verification-box">
          <div class="verif-header">
            <span class="verif-badge">ACADEMIC AUDIT &amp; SOURCES</span>
            <span class="verif-date">Audited: October 2026</span>
          </div>
          <p class="verif-text"><strong>Prescribed Textbooks:</strong> S. Sridhar and M. Vijayalakshmi, <em>Machine Learning</em>, 1st Edition (2021), Oxford University Press (Chapters 1 &amp; 2); Tom M. Mitchell, <em>Machine Learning</em>, McGraw-Hill (1997) (Chapters 1 &amp; 2).</p>
          <p class="verif-text"><strong>Verification Sources:</strong> Prescribed VTU/Ramaiah syllabus specifications, faculty lecture slides in <code>notes/ml/unit1/</code>, and authentic examination papers transcribed directly from <code>notes/ml/practice/ml-cie-1-2-see.pdf</code> (Ramaiah Internal Assessment - I March 2026 and Semester End Examination June/July 2026, Course Code 23IS62). All descriptive statistics, sample variances, Pearson correlation coefficients, and confusion matrix diagnostics verified via automated unit test suite (<code>audit/verify/ml/verify_ml_u1.py</code>).</p>
          <p class="verif-note"><em>Honest Disclosure:</em> The prescribed Sridhar-Vijayalakshmi and Mitchell textbooks were consulted through syllabus topic mapping and official exam solutions; all mathematical definitions of $(T, P, E)$, bias-variance decomposition, and metric equations strictly adhere to standard academic formulations.</p>
        </div>'''

    target_hero = '</div>\n      </header>'
    if 'class="verification-box"' not in html:
        html = html.replace(target_hero, '</div>\n' + verif_box + '\n      </header>', 1)

    # 2. UPDATE SYLLABUS LIST IN HERO
    old_syllabus = '''          <ul class="syllabus-list">
            <li>Complete unit syllabus topics.</li>
          </ul>'''
    new_syllabus = '''          <ul class="syllabus-list">
            <li><strong>Introduction &amp; Fundamentals:</strong> Need for Machine Learning, Classical Programming vs ML Paradigm, Machine Learning in Relation to Other Fields (AI, Data Mining, Statistics), Challenges of Machine Learning.</li>
            <li><strong>Machine Learning Explained:</strong> Tom Mitchell's formal $(T, P, E)$ definition with worked engineering domains (Checkers, Digit OCR, Weather Forecast).</li>
            <li><strong>Learning Paradigms:</strong> Supervised Learning, Unsupervised Learning, and Reinforcement Learning comparisons with formal input-output mappings.</li>
            <li><strong>Machine Learning Process:</strong> End-to-end 7-stage lifecycle pipeline from problem formulation and data collection to deployment and drift monitoring.</li>
            <li><strong>Understanding Data – 1:</strong> Big Data Analysis Framework (The 5 Vs: Volume, Velocity, Variety, Veracity, Value) and distributed processing pipelines.</li>
            <li><strong>Descriptive Statistics &amp; Univariate Analysis:</strong> Measures of Central Tendency (Mean, Median, Mode), Dispersion (Variance, Standard Deviation, Range, IQR), Tukey's $1.5 \\times IQR$ outlier fences, Skewness, Kurtosis.</li>
            <li><strong>Bivariate &amp; Multivariate Data:</strong> Covariance, Pearson correlation coefficient ($r$), Covariance Matrix, Feature Scaling (Min-Max Normalization, Z-Score Standardization).</li>
          </ul>'''
    if old_syllabus in html:
        html = html.replace(old_syllabus, new_syllabus, 1)

    # 3. FIGURE 1.2: ML PROCESS PIPELINE IN § 5 (#sec-ml-process)
    fig_pipeline = f'''
        <!-- FIGURE 1.2: END-TO-END ML PROCESS PIPELINE (RAMAIAH SEE 2026 Q1.a) -->
        <figure class="diagram-card" id="fig-ml-pipeline">
          {generate_ml_process_pipeline_svg()}
          <figcaption class="diagram-title">Figure 1.2: End-to-End Machine Learning Process Engineering Lifecycle (Ramaiah SEE 2026 Q1.a Solved)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">7-stage production architecture: Problem Formulation &rarr; Data Collection &rarr; Cleaning &amp; Imputation &rarr; Feature Engineering &rarr; Training &rarr; Diagnostics &rarr; Deployment with automated drift feedback.</p>
        </figure>'''

    m_sec_process = re.search(r'(<section[^>]*id="sec-ml-process".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if m_sec_process:
        html = html[:m_sec_process.start(2)] + fig_pipeline + '\n\n        ' + html[m_sec_process.start(2):]

    # 4. FIGURE 1.3: BIAS-VARIANCE TRADEOFF IN § 6 (#sec-challenges)
    fig_bv = f'''
        <!-- FIGURE 1.3: BIAS-VARIANCE TRADEOFF CURVE (RAMAIAH SEE 2026 Q1.c) -->
        <figure class="diagram-card" id="fig-bias-variance">
          {generate_bias_variance_svg()}
          <figcaption class="diagram-title">Figure 1.3: Bias-Variance Decomposition vs Model Complexity (Ramaiah SEE 2026 Q1.c Solved)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Total test error decomposes as $\\text{{Bias}}^2 + \\text{{Variance}} + \\sigma^2$. Highlights the Underfitting regime (high bias), Optimal Sweet Spot, and Overfitting regime (high variance).</p>
        </figure>'''

    m_sec_challenges = re.search(r'(<section[^>]*id="sec-challenges".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if m_sec_challenges:
        html = html[:m_sec_challenges.start(2)] + fig_bv + '\n\n        ' + html[m_sec_challenges.start(2):]

    # 5. FIGURE 1.4 & INTERACTIVE CONFUSION MATRIX WIDGET IN § 10 (#sec-univariate-analysis)
    fig_cm = f'''
        <!-- FIGURE 1.4: CONFUSION MATRIX & DIAGNOSTIC METRICS (RAMAIAH CIE-1 2026 Q2.a & SEE Q1.b) -->
        <figure class="diagram-card" id="fig-confusion-matrix">
          {generate_confusion_matrix_svg()}
          <figcaption class="diagram-title">Figure 1.4: Confusion Matrix Grid &amp; Marginal Diagnostic Formulas (Ramaiah CIE-1 Q2.a &amp; SEE Q1.b Solved)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Comprehensive 2&times;2 contingency matrix mapping True Positives ($TP$), False Positives ($FP$), False Negatives ($FN$), and True Negatives ($TN$) to Precision, Recall, Specificity, Accuracy, and $F_1$-score.</p>
        </figure>'''

    interactive_cm = '''
        <!-- INTERACTIVE CONFUSION MATRIX & DIAGNOSTIC METRIC EXPLORER -->
        <div class="interactive-card" id="cm-explorer-widget">
          <div class="interactive-header">
            <div class="interactive-title">
              <span>🎯</span> Interactive Confusion Matrix &amp; Diagnostic Metric Analyzer
            </div>
            <span class="interactive-badge">LIVE JS ENGINE</span>
          </div>

          <p style="font-size:14.5px; color:var(--ink-muted); margin-bottom:1.25rem;">
            Adjust the 2&times;2 contingency counts below or select an authentic university exam preset to dynamically calculate Precision, Recall, Specificity, Accuracy, and $F_1$-Score in real time.
          </p>

          <div style="margin-bottom:1.25rem;">
            <label for="select-cm-preset" class="control-label" style="font-weight:600; margin-bottom:0.4rem; display:block;">Select Authentic Exam Preset:</label>
            <select id="select-cm-preset" class="slider-input" style="height:38px; width:100%; padding:0 10px; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:var(--ink); font-weight:500;" aria-label="Select Confusion Matrix Preset">
              <option value="cie1" selected>Ramaiah CIE-1 March 2026 Q2.a &bull; Spam Filter (TP=70, TN=50, FP=20, FN=10)</option>
              <option value="see2026">Ramaiah SEE June/July 2026 Q1.b &bull; Clinical Diagnostic (TP=50, TN=35, FP=5, FN=10)</option>
              <option value="biopsy">Practice Problem 4 &bull; Cancer Screening (TP=85, TN=890, FP=20, FN=5)</option>
              <option value="custom">Custom Values</option>
            </select>
          </div>

          <div class="interactive-grid" style="grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap:0.75rem;">
            <div class="control-group">
              <label for="input-cm-tp" class="control-label">
                <span>True Pos (TP)</span>
              </label>
              <input type="number" id="input-cm-tp" class="slider-input" min="0" max="10000" value="70" style="padding:6px 10px; font-family:var(--font-mono); font-weight:700; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:var(--green);" aria-label="True Positives">
            </div>

            <div class="control-group">
              <label for="input-cm-fp" class="control-label">
                <span>False Pos (FP)</span>
              </label>
              <input type="number" id="input-cm-fp" class="slider-input" min="0" max="10000" value="20" style="padding:6px 10px; font-family:var(--font-mono); font-weight:700; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:#EF4444;" aria-label="False Positives">
            </div>

            <div class="control-group">
              <label for="input-cm-fn" class="control-label">
                <span>False Neg (FN)</span>
              </label>
              <input type="number" id="input-cm-fn" class="slider-input" min="0" max="10000" value="10" style="padding:6px 10px; font-family:var(--font-mono); font-weight:700; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:#EF4444;" aria-label="False Negatives">
            </div>

            <div class="control-group">
              <label for="input-cm-tn" class="control-label">
                <span>True Neg (TN)</span>
              </label>
              <input type="number" id="input-cm-tn" class="slider-input" min="0" max="10000" value="50" style="padding:6px 10px; font-family:var(--font-mono); font-weight:700; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:var(--brand);" aria-label="True Negatives">
            </div>
          </div>

          <div class="results-grid" style="margin-top:1.25rem;">
            <div class="res-card">
              <span class="res-label">Accuracy (ACC)</span>
              <span id="out-cm-acc" class="res-value" style="color:var(--ink);">80.00%</span>
              <span id="out-cm-acc-sub" class="res-sub">120 / 150</span>
            </div>
            <div class="res-card">
              <span class="res-label">Precision (PPV)</span>
              <span id="out-cm-prec" class="res-value" style="color:var(--brand);">77.78%</span>
              <span id="out-cm-prec-sub" class="res-sub">TP / (TP + FP)</span>
            </div>
            <div class="res-card">
              <span class="res-label">Recall / Sensitivity</span>
              <span id="out-cm-rec" class="res-value" style="color:var(--green);">87.50%</span>
              <span id="out-cm-rec-sub" class="res-sub">TP / (TP + FN)</span>
            </div>
            <div class="res-card">
              <span class="res-label">Specificity (TNR)</span>
              <span id="out-cm-spec" class="res-value" style="color:var(--ink);">71.43%</span>
              <span id="out-cm-spec-sub" class="res-sub">TN / (TN + FP)</span>
            </div>
            <div class="res-card">
              <span class="res-label">F1-Score (Harmonic Mean)</span>
              <span id="out-cm-f1" class="res-value" style="color:var(--green);">82.35%</span>
              <span id="out-cm-f1-sub" class="res-sub">2 &times; (P &times; R) / (P + R)</span>
            </div>
            <div class="res-card">
              <span class="res-label">Clinical / System Triage Status</span>
              <span id="out-cm-verdict" class="res-value" style="font-size:12px; font-weight:700; color:var(--brand);">BALANCED SPAM CLASSIFIER</span>
              <span id="out-cm-verdict-sub" class="res-sub">Good balance between precision &amp; recall</span>
            </div>
          </div>
        </div>

        <script>
        (function() {
          function computeMetrics() {
            var tp = parseFloat(document.getElementById('input-cm-tp').value) || 0;
            var fp = parseFloat(document.getElementById('input-cm-fp').value) || 0;
            var fn = parseFloat(document.getElementById('input-cm-fn').value) || 0;
            var tn = parseFloat(document.getElementById('input-cm-tn').value) || 0;

            var total = tp + fp + fn + tn;
            var acc = total > 0 ? (tp + tn) / total : 0;
            var prec = (tp + fp) > 0 ? tp / (tp + fp) : 0;
            var rec = (tp + fn) > 0 ? tp / (tp + fn) : 0;
            var spec = (tn + fp) > 0 ? tn / (tn + fp) : 0;
            var f1 = (prec + rec) > 0 ? (2 * prec * rec) / (prec + rec) : 0;

            document.getElementById('out-cm-acc').textContent = (acc * 100).toFixed(2) + '%';
            document.getElementById('out-cm-acc-sub').textContent = (tp + tn) + ' / ' + total;

            document.getElementById('out-cm-prec').textContent = (prec * 100).toFixed(2) + '%';
            document.getElementById('out-cm-prec-sub').textContent = tp + ' / ' + (tp + fp);

            document.getElementById('out-cm-rec').textContent = (rec * 100).toFixed(2) + '%';
            document.getElementById('out-cm-rec-sub').textContent = tp + ' / ' + (tp + fn);

            document.getElementById('out-cm-spec').textContent = (spec * 100).toFixed(2) + '%';
            document.getElementById('out-cm-spec-sub').textContent = tn + ' / ' + (tn + fp);

            document.getElementById('out-cm-f1').textContent = (f1 * 100).toFixed(2) + '%';
            document.getElementById('out-cm-f1-sub').textContent = 'F₁ = ' + f1.toFixed(4);

            var verdictEl = document.getElementById('out-cm-verdict');
            var verdictSubEl = document.getElementById('out-cm-verdict-sub');

            if (fn > 0 && (fn / (tp + fn)) > 0.15) {
              verdictEl.textContent = 'HIGH MISS RATE (RISK)';
              verdictEl.style.color = '#EF4444';
              verdictSubEl.textContent = 'FNR = ' + ((fn / (tp + fn)) * 100).toFixed(1) + '%. Unsuitable for medical screening!';
            } else if (rec >= 0.90) {
              verdictEl.textContent = 'CLINICALLY SAFE (HIGH RECALL)';
              verdictEl.style.color = 'var(--green)';
              verdictSubEl.textContent = 'Catches ' + (rec * 100).toFixed(1) + '% of true positive disease cases.';
            } else {
              verdictEl.textContent = 'BALANCED PERFORMANCE';
              verdictEl.style.color = 'var(--brand)';
              verdictSubEl.textContent = 'Solid compromise between false alarms and misses.';
            }
          }

          var preset = document.getElementById('select-cm-preset');
          var inTP = document.getElementById('input-cm-tp');
          var inFP = document.getElementById('input-cm-fp');
          var inFN = document.getElementById('input-cm-fn');
          var inTN = document.getElementById('input-cm-tn');

          if (preset) {
            preset.addEventListener('change', function() {
              if (preset.value === 'cie1') {
                inTP.value = 70; inFP.value = 20; inFN.value = 10; inTN.value = 50;
              } else if (preset.value === 'see2026') {
                inTP.value = 50; inFP.value = 5; inFN.value = 10; inTN.value = 35;
              } else if (preset.value === 'biopsy') {
                inTP.value = 85; inFP.value = 20; inFN.value = 5; inTN.value = 890;
              }
              computeMetrics();
            });
          }

          [inTP, inFP, inFN, inTN].forEach(function(el) {
            if (el) el.addEventListener('input', function() {
              if (preset) preset.value = 'custom';
              computeMetrics();
            });
          });

          computeMetrics();
        })();
        </script>'''

    m_sec_stats = re.search(r'(<section[^>]*id="sec-univariate-analysis".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if m_sec_stats:
        html = html[:m_sec_stats.start(2)] + fig_cm + '\n\n' + interactive_cm + '\n\n        ' + html[m_sec_stats.start(2):]

    # 6. ENRICH SECTION 12 (#sec-multivariate-stats) WITH VERIFIED BIVARIATE NUMERICALS
    num_bivariate = r'''
        <div class="callout callout-math" id="worked-numerical-bivariate">
          <span class="callout-label">WORKED NUMERICAL: BIVARIATE COVARIANCE &amp; PEARSON CORRELATION (VERIFIED)</span>
          <p><strong>Problem Statement:</strong> An instructor monitors $n=5$ undergraduate engineering students, tracking hours spent studying per week ($X$) against final exam marks ($Y$):</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead><tr><th>Student</th><th>Hours ($X$)</th><th>Marks ($Y$)</th><th>$x_i - \bar{X}$</th><th>$y_i - \bar{Y}$</th><th>$(x_i - \bar{X})(y_i - \bar{Y})$</th><th>$(x_i - \bar{X})^2$</th><th>$(y_i - \bar{Y})^2$</th></tr></thead>
              <tbody>
                <tr><td>1</td><td>2</td><td>50</td><td>$-3.2$</td><td>$-18.0$</td><td>$+57.60$</td><td>$10.24$</td><td>$324.0$</td></tr>
                <tr><td>2</td><td>4</td><td>60</td><td>$-1.2$</td><td>$-8.0$</td><td>$+9.60$</td><td>$1.44$</td><td>$64.0$</td></tr>
                <tr><td>3</td><td>5</td><td>65</td><td>$-0.2$</td><td>$-3.0$</td><td>$+0.60$</td><td>$0.04$</td><td>$9.0$</td></tr>
                <tr><td>4</td><td>7</td><td>80</td><td>$+1.8$</td><td>$+12.0$</td><td>$+21.60$</td><td>$3.24$</td><td>$144.0$</td></tr>
                <tr><td>5</td><td>8</td><td>85</td><td>$+2.8$</td><td>$+17.0$</td><td>$+47.60$</td><td>$7.84$</td><td>$289.0$</td></tr>
                <tr style="font-weight:700; background:var(--surface-alt);"><td>Sum ($\Sigma$)</td><td>$26.0$</td><td>$340.0$</td><td>$0.0$</td><td>$0.0$</td><td>$\mathbf{137.00}$</td><td>$\mathbf{22.80}$</td><td>$\mathbf{830.00}$</td></tr>
              </tbody>
            </table>
          </div>
          <p><strong>Step 1: Compute Sample Means:</strong></p>
          $$\bar{X} = \frac{26}{5} = \mathbf{5.20}, \quad \bar{Y} = \frac{340}{5} = \mathbf{68.00}$$
          <p><strong>Step 2: Sample Covariance $\text{Cov}(X, Y)$ ($n-1 = 4$ degrees of freedom):</strong></p>
          $$\text{Cov}(X, Y) = \frac{\sum (x_i - \bar{X})(y_i - \bar{Y})}{n - 1} = \frac{137.00}{4} = \mathbf{+34.2500}$$
          <p><strong>Step 3: Sample Standard Deviations $s_X$ and $s_Y$:</strong></p>
          $$s_X = \sqrt{\frac{22.80}{4}} = \sqrt{5.70} \approx \mathbf{2.3875}, \quad s_Y = \sqrt{\frac{830.00}{4}} = \sqrt{207.50} \approx \mathbf{14.4049}$$
          <p><strong>Step 4: Pearson Correlation Coefficient $r$:</strong></p>
          $$r = \frac{\text{Cov}(X, Y)}{s_X \cdot s_Y} = \frac{137.00}{\sqrt{22.80 \times 830.00}} = \frac{137.00}{\sqrt{18924.00}} = \frac{137.00}{137.5645} \approx \mathbf{+0.9959}$$
          <p><em>Interpretation:</em> $r = +0.9959 \approx +1.0$ confirms an extremely strong positive linear relationship ($R^2 = 0.9918$, meaning $99.18\%$ of the variation in exam marks is explained by study hours).</p>
        </div>'''

    m_sec12 = re.search(r'(<section[^>]*id="sec-multivariate-stats".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if m_sec12:
        html = html[:m_sec12.start(2)] + num_bivariate + '\n\n        ' + html[m_sec12.start(2):]

    # 7. SOLVED EXAM ARCHIVE (Ramaiah CIE-1 March 2026 & SEE June/July 2026)
    archive_section = r'''      <section id="sec-questions-asked-before" class="notes-section exam-archive">
        <div class="section-badge">&block; ARCHIVE</div>
        <h2 class="section-title">Solved Questions from Past Department Examinations</h2>
        <p class="section-lead">The following questions have been transcribed directly from official Ramaiah Institute of Technology examination papers in <code>notes/ml/practice/ml-cie-1-2-see.pdf</code> (Internal Assessment - I March 2026 and Semester End Examination June/July 2026, Course Code 23IS62), solved with complete derivations and mathematical equations:</p>

        <!-- CIE-1 Q1.a -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (March 2026) &bull; Q 1(a)</span>
            <span class="archive-marks">[6 Marks &bull; Blooms L2, CO1]</span>
          </div>
          <p class="archive-q">"Explain the difference between supervised and unsupervised learning with suitable examples."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <div class="table-wrap">
              <table class="data-table">
                <thead><tr><th>Dimension</th><th>Supervised Learning</th><th>Unsupervised Learning</th></tr></thead>
                <tbody>
                  <tr><td><strong>Data Format</strong></td><td>Labeled tuples $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$ with ground-truth supervisor labels.</td><td>Unlabeled feature vectors $\mathcal{D} = \{x_i\}_{i=1}^N$ with zero supervisor guidance.</td></tr>
                  <tr><td><strong>Goal / Objective</strong></td><td>Learn mapping $f: \mathcal{X} \to \mathcal{Y}$ minimizing loss $\sum L(y_i, f(x_i))$.</td><td>Discover latent probability densities, clusters, or lower-dimensional manifolds.</td></tr>
                  <tr><td><strong>Feedback Signal</strong></td><td>Direct error signal $(y_i - \hat{y}_i)$ providing explicit gradient feedback.</td><td>No explicit external error; guided by internal compactness or reconstruction loss.</td></tr>
                  <tr><td><strong>Sub-tasks</strong></td><td>Classification (discrete labels) and Regression (continuous values).</td><td>Clustering, Dimensionality Reduction, and Association Rule Mining.</td></tr>
                  <tr><td><strong>Algorithms</strong></td><td>Linear/Logistic Regression, Decision Trees, Support Vector Machines, Random Forests.</td><td>K-Means, AGNES/DIANA Hierarchical, DBSCAN, PCA, Apriori.</td></tr>
                  <tr><td><strong>Concrete Example</strong></td><td><strong>Spam Filter:</strong> Classifying email as Spam ($y=1$) or Ham ($y=0$) from word frequencies.</td><td><strong>Customer Segmentation:</strong> Grouping shoppers into behavior clusters based on spending volume.</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- CIE-1 Q2.a -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (March 2026) &bull; Q 2(a)</span>
            <span class="archive-marks">[6 Marks &bull; Blooms L3, CO1]</span>
          </div>
          <p class="archive-q">"A model predicts whether an email is spam or not. The results are: $TP = 70, TN = 50, FP = 20, FN = 10$. Compute the following performance measures with necessary mathematical equations: a) Accuracy, b) Precision, c) Recall, d) F1-Score, e) Sensitivity, f) Specificity."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Total Instances:</strong> $N = TP + TN + FP + FN = 70 + 50 + 20 + 10 = \mathbf{150}$.</p>
            <ul>
              <li><strong>a) Accuracy:</strong> Proportion of total correct classifications:
                $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{70 + 50}{150} = \frac{120}{150} = \mathbf{0.8000 \quad (80.00\%)}$$</li>
              <li><strong>b) Precision (Positive Predictive Value):</strong> Proportion of flagged emails that are genuinely spam:
                $$\text{Precision} = \frac{TP}{TP + FP} = \frac{70}{70 + 20} = \frac{70}{90} \approx \mathbf{0.7778 \quad (77.78\%)}$$</li>
              <li><strong>c) Recall (Sensitivity / True Positive Rate):</strong> Proportion of actual spam emails successfully caught:
                $$\text{Recall} = \frac{TP}{TP + FN} = \frac{70}{70 + 10} = \frac{70}{80} = \mathbf{0.8750 \quad (87.50\%)}$$</li>
              <li><strong>d) F1-Score:</strong> Harmonic mean of Precision and Recall:
                $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times \frac{0.7778 \times 0.8750}{0.7778 + 0.8750} = \frac{1.3611}{1.6528} \approx \mathbf{0.8235 \quad (82.35\%)}$$</li>
              <li><strong>e) Sensitivity:</strong> Identical to Recall ($TPR$):
                $$\text{Sensitivity} = \frac{TP}{TP + FN} = \frac{70}{80} = \mathbf{0.8750 \quad (87.50\%)}$$</li>
              <li><strong>f) Specificity (True Negative Rate):</strong> Proportion of actual non-spam (ham) emails correctly preserved:
                $$\text{Specificity} = \frac{TN}{TN + FP} = \frac{50}{50 + 20} = \frac{50}{70} \approx \mathbf{0.7143 \quad (71.43\%)}$$</li>
            </ul>
          </div>
        </div>

        <!-- CIE-1 Q3.a -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (March 2026) &bull; Q 3(a)</span>
            <span class="archive-marks">[6 Marks &bull; Blooms L2, CO1]</span>
          </div>
          <p class="archive-q">"What is overfitting and underfitting in machine learning? What are the common techniques used to prevent overfitting and underfitting?"</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <ul>
              <li><strong>Underfitting (High Bias):</strong> The model is overly simplistic and fails to capture the underlying geometric trend in the training data, resulting in poor performance on both training and validation sets ($E_{\text{train}} \gg 0, E_{\text{val}} \gg 0$).
                <br><em>Mitigation:</em> Increase model capacity (e.g. higher polynomial degree, deeper trees), engineer more descriptive features, decrease regularization penalties ($\lambda$).</li>
              <li><strong>Overfitting (High Variance):</strong> The model fits the idiosyncrasies, random noise, and outliers of the training set rather than the underlying data-generating distribution, yielding stellar training accuracy but disastrous test accuracy ($E_{\text{train}} \approx 0, E_{\text{val}} \gg 0$).
                <br><em>Mitigation:</em>
                <ol>
                  <li><strong>Regularization:</strong> Add $L_1$ (Lasso: penalizes absolute weights) or $L_2$ (Ridge: penalizes squared weights) penalty terms to cost function.</li>
                  <li><strong>Cross-Validation:</strong> Use $K$-fold cross-validation to rigorously validate model stability across disjoint folds.</li>
                  <li><strong>Early Stopping:</strong> Halt iterative gradient optimization when validation loss begins to rise.</li>
                  <li><strong>Pruning / Structural Constraints:</strong> Restrict max tree depth and minimum samples per leaf in decision trees.</li>
                  <li><strong>Data Augmentation &amp; Ensemble Methods:</strong> Expand training diversity or aggregate across uncorrelated estimators (e.g. Random Forest bagging).</li>
                </ol></li>
            </ul>
          </div>
        </div>

        <!-- SEE June/July 2026 Q1.b -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah SEE Examination (June/July 2026) &bull; Q 1(b)</span>
            <span class="archive-marks">[8 Marks &bull; Blooms L3, CO1]</span>
          </div>
          <p class="archive-q">"A binary classifier produced the following confusion matrix: Predicted Positive = 50, Predicted Negative = 10 for Actual Positive; Predicted Positive = 5, Predicted Negative = 35 for Actual Negative. i) Calculate Accuracy, Precision, Recall, and F1-score. ii) Interpret the performance of the model. iii) Comment on whether the model is suitable for critical applications like medical diagnosis."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Given Contingency Values:</strong> $TP = 50, FN = 10, FP = 5, TN = 35$. Total population $N = 100$.</p>
            <p><strong>i) Numerical Metric Computation:</strong></p>
            <ul>
              <li>$\mathbf{\text{Accuracy}} = \frac{50 + 35}{100} = \frac{85}{100} = \mathbf{0.8500 \quad (85.00\%)}$</li>
              <li>$\mathbf{\text{Precision}} = \frac{TP}{TP + FP} = \frac{50}{50 + 5} = \frac{50}{55} \approx \mathbf{0.9091 \quad (90.91\%)}$</li>
              <li>$\mathbf{\text{Recall}} = \frac{TP}{TP + FN} = \frac{50}{50 + 10} = \frac{50}{60} \approx \mathbf{0.8333 \quad (83.33\%)}$</li>
              <li>$\mathbf{F_1\text{-Score}} = 2 \times \frac{0.9091 \times 0.8333}{0.9091 + 0.8333} = \frac{1.5151}{1.7424} \approx \mathbf{0.8696 \quad (86.96\%)}$</li>
            </ul>
            <p><strong>ii) Performance Interpretation:</strong> The classifier demonstrates high precision ($90.91\%$), meaning when it predicts positive, it is trustworthy with few false alarms ($FP=5$). Accuracy ($85\%$) and $F_1$ ($86.96\%$) indicate solid overall discriminative capacity on general benchmarks.</p>
            <p><strong>iii) Clinical Diagnosis Suitability Verdict (CRITICAL):</strong> <strong>NO, the model is UNSUITABLE for critical medical diagnosis.</strong> In clinical screening (e.g. malignant cancer, sepsis, cardiac arrest), the penalty of a <em>False Negative ($FN$)</em> is catastrophic (untreated mortality). Here, $FN = 10$ out of $60$ actual patients means the classifier <strong>misses $16.67\%$ of sick patients</strong> (False Negative Rate $\text{FNR} = 10/60 = 16.67\%$). Life-critical medical triage demands Recall $\ge 98\%–99\%$, achieved by lowering the decision threshold to trade off lower precision in exchange for near-zero false negatives.</p>
          </div>
        </div>

        <!-- SEE June/July 2026 Q1.c -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah SEE Examination (June/July 2026) &bull; Q 1(c)</span>
            <span class="archive-marks">[6 Marks &bull; Blooms L2, CO1]</span>
          </div>
          <p class="archive-q">"Explain how bias and variance change with model complexity using a suitable example."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p>Under squared error loss, the expected prediction error on unseen data decomposes into three orthogonal components:</p>
            $$\mathbb{E}[(y - \hat{f}(x))^2] = \underbrace{\text{Bias}[\hat{f}(x)]^2}_{\text{Approximation Error}} + \underbrace{\text{Var}[\hat{f}(x)]}_{\text{Estimation Sensitivity}} + \underbrace{\sigma^2}_{\text{Irreducible Noise}}$$
            <ul>
              <li><strong>Low Complexity Models (e.g. Linear Model $y = w_1 x + w_0$ on quadratic curve):</strong>
                <br>&bull; <em>High Bias:</em> The model makes rigid, incorrect mathematical assumptions, systematically unable to fit curves.
                <br>&bull; <em>Low Variance:</em> Training on different random subsets of data yields almost identical straight lines.
                <br>&bull; <em>Result:</em> Underfitting. High training and validation errors.</li>
              <li><strong>High Complexity Models (e.g. 15th-Degree Polynomial or Unpruned Decision Tree):</strong>
                <br>&bull; <em>Low Bias:</em> Extremely flexible hypotheses can weave through every single data point.
                <br>&bull; <em>High Variance:</em> Highly sensitive to training sample fluctuations; a change of 2 data points completely alters polynomial coefficients.
                <br>&bull; <em>Result:</em> Overfitting. Near-zero training error, catastrophic test error.</li>
              <li><strong>Optimal Tradeoff (Figure 1.3):</strong> Found at the minimum of the U-shaped total error curve, balancing bias and variance.</li>
            </ul>
          </div>
        </div>

        <!-- SEE June/July 2026 Q2.b -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah SEE Examination (June/July 2026) &bull; Q 2(b)</span>
            <span class="archive-marks">[7 Marks &bull; Blooms L3, CO1]</span>
          </div>
          <p class="archive-q">"A machine learning model is developed using a dataset and produces the following results: Training Accuracy = 98%, Validation Accuracy = 72%. Based on the above information: i) Determine whether the model is overfitting or underfitting. ii) Suggest at least two methods to improve the model performance. iii) Explain the role of training, validation, and testing datasets in identifying such issues."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <ul>
              <li><strong>i) Diagnosis:</strong> The model is severely <strong>OVERFITTING</strong>. The massive $26\%$ generalization gap ($98\% - 72\% = 26\%$) proves that the model memorized the training sample noise and idiosyncrasies rather than learning true inductive features.</li>
              <li><strong>ii) Two Remediation Strategies:</strong>
                <ol>
                  <li><em>Apply $L_2$ Regularization (Weight Decay) or Dropout:</em> Penalize large parameter weights to constrain hypothesis capacity.</li>
                  <li><em>Gather More Training Data or Apply Data Augmentation:</em> Exposing the learner to more varied samples restricts variance.</li>
                  <li><em>Reduce Model Architecture Complexity:</em> Lower polynomial degree or restrict maximum tree depth.</li>
                </ol></li>
              <li><strong>iii) Roles of Data Partitions:</strong>
                <br>&bull; <strong>Training Set ($60\%–70\%$):</strong> Used exclusively by the optimizer to adjust weights and parameters via loss minimization.
                <br>&bull; <strong>Validation Set ($15\%–20\%$):</strong> Used to evaluate performance on unseen data during training, tune hyperparameters (learning rate, $\lambda$), and perform early stopping.
                <br>&bull; <strong>Testing Set ($15\%–20\%$):</strong> Held out completely untouched until final model selection to provide an unbiased, gold-standard estimate of real-world generalization performance.</li>
            </ul>
          </div>
        </div>

        <!-- SEE June/July 2026 Q2.c -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah SEE Examination (June/July 2026) &bull; Q 2(c)</span>
            <span class="archive-marks">[6 Marks &bull; Blooms L2, CO1]</span>
          </div>
          <p class="archive-q">"Discuss the challenges posed by unbalanced datasets and methods to handle them."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <ul>
              <li><strong>Challenges of Class Imbalance:</strong>
                <br>&bull; <em>Accuracy Paradox:</em> In a dataset with $99\%$ negative (legitimate transactions) and $1\%$ positive (credit card fraud), a naive classifier predicting "Always Negative" achieves $99\%$ accuracy while detecting zero frauds.
                <br>&bull; <em>Gradient Dominance:</em> The majority class dominates loss calculations, pulling parameter updates away from rare minority features.</li>
              <li><strong>Handling Techniques:</strong>
                <ol>
                  <li><strong>Resampling Strategies:</strong>
                    <br>&bull; <em>SMOTE (Synthetic Minority Over-sampling Technique):</em> Synthesizes new minority instances along $k$-NN interpolations.
                    <br>&bull; <em>Random Undersampling:</em> Downsamples majority class (risks throwing away valuable data).</li>
                  <li><strong>Cost-Sensitive Learning:</strong> Assign an asymmetric cost matrix $C(\text{FN}) \gg C(\text{FP})$ in the loss function, penalizing misclassified minority samples heavily.</li>
                  <li><strong>Alternative Evaluation Metrics:</strong> Discard Raw Accuracy in favor of Precision-Recall AUC ($PR\text{-}AUC$), Balanced Accuracy, and $F_\beta$-Score ($\beta=2$ for recall priority).</li>
                  <li><strong>Threshold Moving:</strong> Shift the classification decision threshold from default $0.5$ down to a lower probability (e.g. $0.15$) to prioritize recall.</li>
                </ol></li>
            </ul>
          </div>
        </div>
      </section>'''

    # Replace old questions-asked-before section with enriched archive
    m_archive = re.search(r'<section[^>]*id="sec-questions-asked-before".*?</section>', html, re.DOTALL)
    if m_archive:
        html = html[:m_archive.start()] + archive_section + html[m_archive.end():]

    # 8. ENRICH PRACTICE PROBLEMS WITH 6 VERIFIED NUMERICALS
    practice_section = r'''      <section id="sec-practice-problems" class="notes-section">
        <h2 class="section-title">Practice Problems (Step-by-Step Verified Solutions)</h2>
        <p class="section-lead">The following 6 practice problems have been mathematically recomputed and verified via <code>audit/verify/ml/verify_ml_u1.py</code>. Attempt each manually before expanding the solution blocks.</p>

        <!-- Problem 1: Full Descriptive Statistics -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 1 (Descriptive Statistics &amp; Fences):</strong> A batch of 10 student quiz scores is: $S = [45, 52, 60, 60, 68, 72, 75, 80, 88, 90]$. Compute: (i) Mean, (ii) Median, (iii) Mode, (iv) Sample Variance $s^2$, (v) Sample Standard Deviation $s$, (vi) Interquartile Range ($IQR$), and (vii) Tukey's outlier fences $[L, U]$.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <ul>
                <li><strong>Mean:</strong> $\bar{x} = \frac{45+52+60+60+68+72+75+80+88+90}{10} = \frac{690}{10} = \mathbf{69.00}$</li>
                <li><strong>Median:</strong> Sorted array ($n=10$). Middle values at index 5 and 6: $\frac{68 + 72}{2} = \mathbf{70.00}$</li>
                <li><strong>Mode:</strong> Value with highest frequency: $\mathbf{60}$ (appears twice).</li>
                <li><strong>Sum of Squared Deviations $\sum (x_i - \bar{x})^2$:</strong>
                  $$(-24)^2 + (-17)^2 + (-9)^2 + (-9)^2 + (-1)^2 + (+3)^2 + (+6)^2 + (+11)^2 + (+19)^2 + (+21)^2 = 576 + 289 + 81 + 81 + 1 + 9 + 36 + 121 + 361 + 441 = \mathbf{1996.00}$$</li>
                <li><strong>Sample Variance ($s^2$):</strong> $s^2 = \frac{1996.00}{10 - 1} = \frac{1996}{9} \approx \mathbf{221.78}$</li>
                <li><strong>Sample Standard Deviation ($s$):</strong> $s = \sqrt{221.78} \approx \mathbf{14.8922}$</li>
                <li><strong>Quartiles &amp; IQR:</strong> Lower half $\{45, 52, 60, 60, 68\} \implies Q_1 = 60$. Upper half $\{72, 75, 80, 88, 90\} \implies Q_3 = 80$.
                  <br>$IQR = Q_3 - Q_1 = 80 - 60 = \mathbf{20.00}$.</li>
                <li><strong>Tukey Fences:</strong> Lower Fence $= Q_1 - 1.5 \times IQR = 60 - 30 = \mathbf{30.00}$. Upper Fence $= Q_3 + 1.5 \times IQR = 80 + 30 = \mathbf{110.00}$. Since all values lie in $[30, 110]$, there are <strong>zero outliers</strong>.</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 2: Min-Max & Z-Score Normalization -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 2 (Data Normalization &amp; Standard Scaling):</strong> Normalize the vector $V = [12, 18, 24, 30, 36]$ into: (i) Range $[0, 1]$ using Min-Max scaling, (ii) Range $[-1, 1]$ using Min-Max scaling, and (iii) Standardized Z-scores ($z = \frac{x - \mu}{\sigma}$).
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <p>$\min(V) = 12, \max(V) = 36$, $\text{Range} = 36 - 12 = 24$. Mean $\mu = \frac{120}{5} = 24.0$. Population Variance $\sigma^2 = \frac{(-12)^2 + (-6)^2 + 0^2 + 6^2 + 12^2}{5} = \frac{144 + 36 + 0 + 36 + 144}{5} = \frac{360}{5} = 72.0 \implies \sigma = \sqrt{72} \approx \mathbf{8.4853}$.</p>
              <ul>
                <li><strong>(i) Min-Max $[0, 1]$:</strong>
                  <br>&bull; $12 \to \frac{12-12}{24} = \mathbf{0.00}$
                  <br>&bull; $18 \to \frac{18-12}{24} = \mathbf{0.25}$
                  <br>&bull; $24 \to \frac{24-12}{24} = \mathbf{0.50}$
                  <br>&bull; $30 \to \frac{30-12}{24} = \mathbf{0.75}$
                  <br>&bull; $36 \to \frac{36-12}{24} = \mathbf{1.00}$</li>
                <li><strong>(ii) Min-Max $[-1, 1]$ ($x_{\text{new}} = 2 \times x_{[0,1]} - 1$):</strong>
                  <br>Vector: $[\mathbf{-1.00, -0.50, 0.00, +0.50, +1.00}]$</li>
                <li><strong>(iii) Z-Score Standardization:</strong>
                  <br>&bull; $12 \to \frac{12-24}{8.4853} = \mathbf{-1.4142}$
                  <br>&bull; $18 \to \frac{18-24}{8.4853} = \mathbf{-0.7071}$
                  <br>&bull; $24 \to \frac{24-24}{8.4853} = \mathbf{0.0000}$
                  <br>&bull; $30 \to \frac{30-24}{8.4853} = \mathbf{+0.7071}$
                  <br>&bull; $36 \to \frac{36-24}{8.4853} = \mathbf{+1.4142}$</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 3: Bivariate Covariance and Pearson r -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 3 (Bivariate Association):</strong> Compute the Sample Covariance and Pearson Correlation Coefficient for $X = [2, 4, 5, 7, 8]$ and $Y = [50, 60, 65, 80, 85]$.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <p>$\bar{X} = 5.2, \bar{Y} = 68.0, n=5$.</p>
              $$\sum (x_i - \bar{X})(y_i - \bar{Y}) = 137.00, \quad \sum (x_i - \bar{X})^2 = 22.80, \quad \sum (y_i - \bar{Y})^2 = 830.00$$
              <ul>
                <li>$\text{Cov}(X, Y) = \frac{137.00}{4} = \mathbf{+34.2500}$</li>
                <li>$s_X = \sqrt{\frac{22.80}{4}} \approx 2.3875, \quad s_Y = \sqrt{\frac{830.00}{4}} \approx 14.4049$</li>
                <li>$r = \frac{137.00}{\sqrt{22.80 \times 830.00}} = \frac{137.00}{137.5645} = \mathbf{+0.9959}$</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 4: Biopsy Screening Diagnostic Evaluation -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 4 (Imbalanced Medical Screening):</strong> In an automated cancer screening test on $1000$ biopsy images, the model yields: $TP = 85, TN = 890, FP = 20, FN = 5$. Compute: Accuracy, Precision, Recall, Specificity, F1-Score, and False Negative Rate ($FNR$).
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <ul>
                <li>$\text{Accuracy} = \frac{85 + 890}{1000} = \frac{975}{1000} = \mathbf{97.50\% \quad (0.9750)}$</li>
                <li>$\text{Precision} = \frac{85}{85 + 20} = \frac{85}{105} \approx \mathbf{80.95\% \quad (0.8095)}$</li>
                <li>$\text{Recall (Sensitivity)} = \frac{85}{85 + 5} = \frac{85}{90} \approx \mathbf{94.44\% \quad (0.9444)}$</li>
                <li>$\text{Specificity} = \frac{890}{890 + 20} = \frac{890}{910} \approx \mathbf{97.80\% \quad (0.9780)}$</li>
                <li>$F_1\text{-Score} = 2 \times \frac{0.8095 \times 0.9444}{0.8095 + 0.9444} = \frac{1.5289}{1.7539} \approx \mathbf{87.18\% \quad (0.8718)}$</li>
                <li>$\text{FNR} = \frac{5}{90} = \mathbf{5.56\%}$ (Only $5.56\%$ of malignancies are missed, significantly safer than a general $16.7\%$ baseline).</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 5: Outlier Detection using IQR -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 5 (Sensor Outlier Detection):</strong> A temperature telemetry feed produces readings: $\{14, 19, 21, 24, 25, 28, 31, 35, 78\}$. Identify any outliers using Tukey's $1.5 \times IQR$ method.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <p>Sorted dataset ($n=9$): Median = 25 (5th value).</p>
              <ul>
                <li>Lower half: $\{14, 19, 21, 24\} \implies Q_1 = \frac{19 + 21}{2} = \mathbf{20.00}$</li>
                <li>Upper half: $\{28, 31, 35, 78\} \implies Q_3 = \frac{31 + 35}{2} = \mathbf{33.00}$</li>
                <li>$IQR = Q_3 - Q_1 = 33.00 - 20.00 = \mathbf{13.00}$</li>
                <li>Lower Fence: $Q_1 - 1.5 \times 13 = 20 - 19.5 = \mathbf{0.50}$</li>
                <li>Upper Fence: $Q_3 + 1.5 \times 13 = 33 + 19.5 = \mathbf{52.50}$</li>
                <li><strong>Conclusion:</strong> $78 > 52.50$. Therefore, <strong>$78$ is an extreme outlier</strong> requiring imputation or filtering before model ingestion.</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 6: Mitchell T, P, E Specification -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 6 (Mitchell Learning Triad):</strong> Formally formulate the Task ($T$), Performance Measure ($P$), and Training Experience ($E$) for: (i) Autonomous Vehicle Lane Following, and (ii) Credit Card Fraud Detection.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <ul>
                <li><strong>(i) Autonomous Vehicle Lane Following:</strong>
                  <br>&bull; <em>Task ($T$):</em> Steering the vehicle within lane boundaries using streaming forward camera video.
                  <br>&bull; <em>Performance ($P$):</em> Average distance from lane center and number of human disengagements per $1,000$ km.
                  <br>&bull; <em>Experience ($E$):</em> Sequence of camera frames paired with human driver steering angle recordings.</li>
                <li><strong>(ii) Credit Card Fraud Detection:</strong>
                  <br>&bull; <em>Task ($T$):</em> Classifying incoming credit card transactions as fraudulent ($1$) or legitimate ($0$).
                  <br>&bull; <em>Performance ($P$):</em> Precision-Recall Area Under Curve ($PR\text{-}AUC$) and financial loss prevented.
                  <br>&bull; <em>Experience ($E$):</em> Historical database of transactional logs annotated with confirmed bank fraud chargebacks.</li>
              </ul>
            </div>
          </details>
        </div>
      </section>'''

    # Replace practice problems section
    m_practice = re.search(r'<section[^>]*id="sec-practice-problems".*?</section>', html, re.DOTALL)
    if m_practice:
        html = html[:m_practice.start()] + practice_section + html[m_practice.end():]

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"ML Unit 1 enriched successfully! File size: {len(html)} bytes")

if __name__ == "__main__":
    build()
