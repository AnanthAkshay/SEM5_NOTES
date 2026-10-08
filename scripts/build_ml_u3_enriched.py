"""
build_ml_u3_enriched.py - Programmatically enriches Machine Learning Unit 3 notes:
- Academic Verification Box (Sridhar & Vijayalakshmi 2021 OUP, Mitchell 1997, Ramaiah CIE-1, CIE-2, SEE 2026)
- Accurate Official Syllabus Topics in Hero Card
- 2 Theme-Aware SVG Figures:
  - Figure 3.1: Linear Regression OLS Line & Residuals (Ramaiah CIE-1 March 2026 Q1.c)
  - Figure 3.2: Complete ID3 Decision Tree for Play Tennis (Ramaiah CIE-1 Q3.c & SEE Q5.b)
- Interactive Linear Regression & Gradient Descent Explorer in Vanilla JS
- Fully transcribed, authentically solved examination questions from Ramaiah CIE-1, CIE-2, and SEE 2026
- 6 Verified Practice Problems with hidden solutions
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_ml_u3_assets import (
    generate_linear_regression_svg,
    generate_decision_tree_svg
)

def build():
    path = "notes/ml/unit3/unit-3-notes.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. ACADEMIC VERIFICATION BOX
    verif_box = '''        <div class="verification-box">
          <div class="verif-header">
            <span class="verif-badge">ACADEMIC AUDIT &amp; SOURCES</span>
            <span class="verif-date">Audited: October 2026</span>
          </div>
          <p class="verif-text"><strong>Prescribed Textbooks:</strong> S. Sridhar and M. Vijayalakshmi, <em>Machine Learning</em>, 1st Edition (2021), Oxford University Press (Chapters 5, 6 &amp; 7); Tom M. Mitchell, <em>Machine Learning</em>, McGraw-Hill (1997) (Chapter 3: Decision Tree Learning; Chapter 8: Instance-Based Learning).</p>
          <p class="verif-text"><strong>Verification Sources:</strong> Prescribed VTU/Ramaiah syllabus specifications, faculty lecture slides in <code>notes/ml/unit3/</code>, and authentic examination papers transcribed directly from <code>notes/ml/practice/ml-cie-1-2-see.pdf</code> (Ramaiah Internal Assessment - I March 2026, Internal Assessment - II May 2026, and Semester End Examination June/July 2026, Course Code 23IS62). All OLS regression closed-form slopes ($b=4.5000, a=41.0000, \\hat{Y}(7)=72.50$), $K$-NN regression predictions ($\\hat{y}=180.67$), ID3 Shannon entropies ($H(S)=0.97095, IG(\\text{Outlook})=0.32193$), and Logistic sigmoid probabilities verified via automated test suite (<code>audit/verify/ml/verify_ml_u3.py</code>).</p>
          <p class="verif-note"><em>Honest Disclosure:</em> The prescribed textbooks were consulted through syllabus topic mapping and official exam solutions; all mathematical formulas for Ordinary Least Squares, Gini Impurity, and Information Gain follow standard machine learning conventions.</p>
        </div>'''

    target_hero = '</div>\n      </header>'
    if 'class="verification-box"' not in html:
        html = html.replace(target_hero, '</div>\n' + verif_box + '\n      </header>', 1)

    # 2. UPDATE SYLLABUS LIST IN HERO
    old_syllabus = '''          <ul class="syllabus-list">
            <li>Complete unit syllabus topics.</li>
          </ul>'''
    new_syllabus = '''          <ul class="syllabus-list">
            <li><strong>Similarity-based Learning:</strong> Instance-based vs Eager learning, $K$-Nearest-Neighbor ($K$-NN) algorithm, distance metrics (Euclidean, Manhattan, Minkowski), Weighted $K$-NN ($1/d^2$), Nearest Centroid (Rocchio) classifier, Locally Weighted Regression (LWR) with Gaussian kernel.</li>
            <li><strong>Regression Analysis:</strong> Introduction to Regression, Ordinary Least Squares (OLS) closed-form normal equations, Multiple Linear Regression ($\mathbf{w} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$), Polynomial Regression basis expansion, Logistic Regression (sigmoid activation, log-odds, binary cross-entropy loss).</li>
            <li><strong>Decision Tree Learning:</strong> Decision tree model structure, Shannon Entropy $H(S) = -\\sum p_i \\log_2 p_i$, Information Gain ($ID3$), Gain Ratio ($C4.5$), Gini Impurity ($CART$), Overfitting in decision trees, Pre-pruning and Post-pruning algorithms.</li>
          </ul>'''
    if old_syllabus in html:
        html = html.replace(old_syllabus, new_syllabus, 1)

    # 3. FIGURE 3.1 & INTERACTIVE LINEAR REGRESSION WIDGET IN § 6 (#sec-linear-regression)
    fig_lr = f'''
        <!-- FIGURE 3.1: LINEAR REGRESSION OLS BEST-FIT LINE & RESIDUALS (RAMAIAH CIE-1 Q1.c) -->
        <figure class="diagram-card" id="fig-linear-regression">
          {generate_linear_regression_svg()}
          <figcaption class="diagram-title">Figure 3.1: Ordinary Least Squares (OLS) Regression Fit &amp; Residuals (Ramaiah CIE-1 Q1.c Solved)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Study Hours ($X$) vs Exam Marks ($Y$) yields optimal least-squares line $\\hat{{Y}} = 4.50X + 41.00$. Vertical red lines depict residuals $e_i = y_i - \\hat{{y}}_i$. Target prediction for $X=7$ hours is $\\hat{{Y}}(7) = 72.50$ marks.</p>
        </figure>'''

    interactive_lr = '''
        <!-- INTERACTIVE LINEAR REGRESSION & ERROR MINIMIZATION EXPLORER -->
        <div class="interactive-card" id="lr-explorer-widget">
          <div class="interactive-header">
            <div class="interactive-title">
              <span>📈</span> Interactive Linear Regression &amp; Error Minimizer
            </div>
            <span class="interactive-badge">LIVE JS ENGINE</span>
          </div>

          <p style="font-size:14.5px; color:var(--ink-muted); margin-bottom:1.25rem;">
            Adjust the slope ($m$) and intercept ($c$) sliders to observe how the Mean Squared Error ($MSE$) and Coefficient of Determination ($R^2$) respond across the Ramaiah CIE-1 exam dataset $[(2, 50), (4, 60), (6, 65), (8, 80), (10, 85)]$.
          </p>

          <div class="interactive-grid">
            <div class="control-group">
              <label for="slider-lr-slope" class="control-label">
                <span>Slope ($m$):</span>
                <span id="lbl-lr-slope" class="control-val">4.50</span>
              </label>
              <input type="range" id="slider-lr-slope" class="slider-input" min="1.0" max="8.0" step="0.05" value="4.50" aria-label="Regression Slope">
            </div>

            <div class="control-group">
              <label for="slider-lr-intercept" class="control-label">
                <span>Intercept ($c$):</span>
                <span id="lbl-lr-intercept" class="control-val">41.00</span>
              </label>
              <input type="range" id="slider-lr-intercept" class="slider-input" min="20.0" max="60.0" step="0.25" value="41.00" aria-label="Regression Intercept">
            </div>

            <div class="control-group">
              <label for="slider-lr-query" class="control-label">
                <span>Query Study Hours ($X$):</span>
                <span id="lbl-lr-query" class="control-val">7.0 hrs</span>
              </label>
              <input type="range" id="slider-lr-query" class="slider-input" min="1.0" max="12.0" step="0.5" value="7.0" aria-label="Query Study Hours">
            </div>
          </div>

          <div class="results-grid" style="margin-top:1.25rem;">
            <div class="res-card">
              <span class="res-label">Regression Equation</span>
              <span id="out-lr-eq" class="res-value" style="font-family:var(--font-mono); color:var(--brand);">&#x177; = 4.50X + 41.00</span>
              <span class="res-sub">Line of best fit</span>
            </div>
            <div class="res-card">
              <span class="res-label">Predicted Marks &#x177;(X)</span>
              <span id="out-lr-pred" class="res-value" style="font-family:var(--font-mono); color:var(--green);">72.50 Marks</span>
              <span id="out-lr-pred-sub" class="res-sub">For X = 7.0 study hours</span>
            </div>
            <div class="res-card">
              <span class="res-label">Mean Squared Error (MSE)</span>
              <span id="out-lr-mse" class="res-value" style="font-family:var(--font-mono); color:var(--ink);">4.00</span>
              <span id="out-lr-mse-sub" class="res-sub">SSE / 5 = 20.00 / 5</span>
            </div>
            <div class="res-card">
              <span class="res-label">Goodness of Fit (R&sup2;)</span>
              <span id="out-lr-r2" class="res-value" style="font-family:var(--font-mono); color:var(--green);">0.9759 (97.59%)</span>
              <span class="res-sub">1 - (SSE / SST)</span>
            </div>
          </div>
        </div>

        <script>
        (function() {
          var pts = [
            { x: 2, y: 50 },
            { x: 4, y: 60 },
            { x: 6, y: 65 },
            { x: 8, y: 80 },
            { x: 10, y: 85 }
          ];
          var meanY = 68.0;
          var sst = 0;
          pts.forEach(function(p) { sst += Math.pow(p.y - meanY, 2); }); // 830.0

          function updateLR() {
            var m = parseFloat(document.getElementById('slider-lr-slope').value);
            var c = parseFloat(document.getElementById('slider-lr-intercept').value);
            var q = parseFloat(document.getElementById('slider-lr-query').value);

            document.getElementById('lbl-lr-slope').textContent = m.toFixed(2);
            document.getElementById('lbl-lr-intercept').textContent = c.toFixed(2);
            document.getElementById('lbl-lr-query').textContent = q.toFixed(1) + ' hrs';

            var sse = 0;
            pts.forEach(function(p) {
              var yHat = m * p.x + c;
              sse += Math.pow(p.y - yHat, 2);
            });
            var mse = sse / pts.length;
            var r2 = 1.0 - (sse / sst);

            var pred = m * q + c;

            document.getElementById('out-lr-eq').textContent = '\u0177 = ' + m.toFixed(2) + 'X + ' + c.toFixed(2);
            document.getElementById('out-lr-pred').textContent = pred.toFixed(2) + ' Marks';
            document.getElementById('out-lr-pred-sub').textContent = 'For X = ' + q.toFixed(1) + ' study hours';
            document.getElementById('out-lr-mse').textContent = mse.toFixed(2);
            document.getElementById('out-lr-mse-sub').textContent = 'SSE / 5 = ' + sse.toFixed(2) + ' / 5';

            var r2El = document.getElementById('out-lr-r2');
            r2El.textContent = (r2 * 100).toFixed(2) + '% (R\u00b2 = ' + r2.toFixed(4) + ')';
            r2El.style.color = r2 >= 0.90 ? 'var(--green)' : (r2 >= 0.70 ? 'var(--brand)' : '#EF4444');
          }

          var sM = document.getElementById('slider-lr-slope');
          var sC = document.getElementById('slider-lr-intercept');
          var sQ = document.getElementById('slider-lr-query');

          if (sM && sC && sQ) {
            sM.addEventListener('input', updateLR);
            sC.addEventListener('input', updateLR);
            sQ.addEventListener('input', updateLR);
            updateLR();
          }
        })();
        </script>'''

    m_sec6 = re.search(r'(<section[^>]*id="sec-linear-regression".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if m_sec6:
        html = html[:m_sec6.start(2)] + fig_lr + '\n\n' + interactive_lr + '\n\n        ' + html[m_sec6.start(2):]

    # 4. FIGURE 3.2: COMPLETE ID3 DECISION TREE IN § 10 (#sec-dt-algorithms)
    fig_dt = f'''
        <!-- FIGURE 3.2: COMPLETE ID3 DECISION TREE (RAMAIAH CIE-1 Q3.c & SEE Q5.b) -->
        <figure class="diagram-card" id="fig-decision-tree">
          {generate_decision_tree_svg()}
          <figcaption class="diagram-title">Figure 3.2: Induced ID3 Decision Tree for Play Tennis (Ramaiah CIE-1 Q3.c &amp; SEE Q5.b Solved)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Root node splits on Outlook ($IG=0.3219$). Overcast branch terminates in pure 'Yes' leaf. Sunny branch splits on Humidity ($IG=0.8113$), and Rain branch splits on Wind ($IG=0.8113$).</p>
        </figure>'''

    m_sec10 = re.search(r'(<section[^>]*id="sec-dt-algorithms".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if m_sec10:
        html = html[:m_sec10.start(2)] + fig_dt + '\n\n        ' + html[m_sec10.start(2):]

    # 5. SOLVED EXAM ARCHIVE (Ramaiah CIE-1, CIE-2, SEE 2026)
    archive_section = r'''      <section id="sec-questions-asked-before" class="notes-section exam-archive">
        <div class="section-badge">&block; ARCHIVE</div>
        <h2 class="section-title">Solved Questions from Past Department Examinations</h2>
        <p class="section-lead">The following examination questions have been transcribed from the official Ramaiah Institute of Technology papers in <code>notes/ml/practice/ml-cie-1-2-see.pdf</code> (CIE-1 March 2026, CIE-2 May 2026, and SEE June/July 2026, Course Code 23IS62), solved with complete derivations and step-by-step mathematical proofs:</p>

        <!-- CIE-1 Q1.c: Hours Studied vs Marks Regression -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (March 2026) &bull; Q 1(c)</span>
            <span class="archive-marks">[3 Marks &bull; Blooms L3, CO3]</span>
          </div>
          <p class="archive-q">"The following data represents hours studied (X) and marks obtained (Y): X = [2, 4, 6, 8, 10], Y = [50, 60, 65, 80, 85]. i. Compute slope (b) and intercept (a). ii. Write the regression equation. iii. Predict marks for X = 7 hours."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Step 1: Compute Means ($n=5$):</strong></p>
            $$\bar{X} = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = \mathbf{6.0}, \quad \bar{Y} = \frac{50 + 60 + 65 + 80 + 85}{5} = \frac{340}{5} = \mathbf{68.0}$$
            <p><strong>Step 2: Compute Summations:</strong></p>
            <div class="table-wrap">
              <table class="data-table" style="font-family:var(--font-mono); text-align:center;">
                <thead><tr><th>$x_i$</th><th>$y_i$</th><th>$x_i - \bar{X}$</th><th>$y_i - \bar{Y}$</th><th>$(x_i - \bar{X})(y_i - \bar{Y})$</th><th>$(x_i - \bar{X})^2$</th></tr></thead>
                <tbody>
                  <tr><td>2</td><td>50</td><td>$-4$</td><td>$-18$</td><td>$+72$</td><td>16</td></tr>
                  <tr><td>4</td><td>60</td><td>$-2$</td><td>$-8$</td><td>$+16$</td><td>4</td></tr>
                  <tr><td>6</td><td>65</td><td>$0$</td><td>$-3$</td><td>$0$</td><td>0</td></tr>
                  <tr><td>8</td><td>80</td><td>$+2$</td><td>$+12$</td><td>$+24$</td><td>4</td></tr>
                  <tr><td>10</td><td>85</td><td>$+4$</td><td>$+17$</td><td>$+68$</td><td>16</td></tr>
                  <tr style="font-weight:700; background:var(--surface-alt);"><td>$\Sigma$</td><td></td><td>$0$</td><td>$0$</td><td>$\mathbf{180}$</td><td>$\mathbf{40}$</td></tr>
                </tbody>
              </table>
            </div>
            <ul>
              <li><strong>i. Slope ($b$) and Intercept ($a$):</strong>
                $$b = \frac{\sum (x_i - \bar{X})(y_i - \bar{Y})}{\sum (x_i - \bar{X})^2} = \frac{180}{40} = \mathbf{4.5000}$$
                $$a = \bar{Y} - b \bar{X} = 68.0 - (4.50 \times 6.0) = 68.0 - 27.0 = \mathbf{41.0000}$$</li>
              <li><strong>ii. Regression Equation:</strong>
                $$\mathbf{\hat{Y} = 4.50 X + 41.00}$$</li>
              <li><strong>iii. Predict Marks for $X = 7$ Hours:</strong>
                $$\hat{Y}(7) = 4.50(7) + 41.00 = 31.50 + 41.00 = \mathbf{72.50 \text{ Marks}}$$</li>
            </ul>
          </div>
        </div>

        <!-- CIE-1 Q2.c: Logistic vs Linear Regression -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (March 2026) &bull; Q 2(c)</span>
            <span class="archive-marks">[3 Marks &bull; Blooms L2, CO3]</span>
          </div>
          <p class="archive-q">"Differentiate Logistic Regression and Linear Regression in machine learning."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <div class="table-wrap">
              <table class="data-table">
                <thead><tr><th>Dimension</th><th>Linear Regression</th><th>Logistic Regression</th></tr></thead>
                <tbody>
                  <tr><td><strong>Target Output Space</strong></td><td>Continuous real numbers: $y \in (-\infty, +\infty)$.</td><td>Categorical / Discrete probability: $\hat{y} \in [0, 1]$.</td></tr>
                  <tr><td><strong>Mathematical Function</strong></td><td>Linear combination: $\hat{y} = \mathbf{w}^T \mathbf{x} + b$.</td><td>Sigmoid transformation: $\hat{y} = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$.</td></tr>
                  <tr><td><strong>Cost / Loss Function</strong></td><td>Mean Squared Error (Convex): $\frac{1}{2m} \sum (y - \hat{y})^2$.</td><td>Binary Cross-Entropy (Log-Loss): $-\sum [y \log \hat{y} + (1-y)\log(1-\hat{y})]$.</td></tr>
                  <tr><td><strong>Optimization Technique</strong></td><td>Closed-form Normal Equation or Gradient Descent.</td><td>Iterative Gradient Descent / Newton-Raphson.</td></tr>
                  <tr><td><strong>Primary Objective</strong></td><td>Predicting continuous quantities (House prices, stock yield).</td><td>Binary / Multiclass Classification (Spam, medical diagnosis).</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- CIE-1 Q3.c & SEE Q5.b: ID3 Information Gain -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah CIE-1 (March 2026) &bull; Q 3(c) / SEE (July 2026) &bull; Q 5(b)</span>
            <span class="archive-marks">[3 / 12 Marks &bull; Blooms L3, CO3]</span>
          </div>
          <p class="archive-q">"Consider the dataset of 10 samples for predicting whether to Play Tennis. Compute information gain of attribute outlook using ID3 algorithm."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Step 1: Compute Total Entropy $H(S)$ of the 10-instance dataset ($6 \text{ Yes}, 4 \text{ No}$):</strong></p>
            $$H(S) = -\left(\frac{6}{10}\right)\log_2\left(\frac{6}{10}\right) - \left(\frac{4}{10}\right)\log_2\left(\frac{4}{10}\right) = -0.6(-0.73697) - 0.4(-1.32193) = 0.44218 + 0.52877 = \mathbf{0.97095 \text{ bits}}$$
            <p><strong>Step 2: Partition by Attribute $\text{Outlook} \in \{\text{Sunny}, \text{Overcast}, \text{Rain}\}$:</strong></p>
            <ul>
              <li><strong>Sunny (4 instances: 1 Yes, 3 No):</strong>
                $$H(S_{\text{Sunny}}) = -\frac{1}{4}\log_2\left(\frac{1}{4}\right) - \frac{3}{4}\log_2\left(\frac{3}{4}\right) = 0.50000 + 0.31128 = \mathbf{0.81128 \text{ bits}}$$</li>
              <li><strong>Overcast (2 instances: 2 Yes, 0 No):</strong> Completely pure subset:
                $$H(S_{\text{Overcast}}) = \mathbf{0.00000 \text{ bits}}$$</li>
              <li><strong>Rain (4 instances: 3 Yes, 1 No):</strong>
                $$H(S_{\text{Rain}}) = -\frac{3}{4}\log_2\left(\frac{3}{4}\right) - \frac{1}{4}\log_2\left(\frac{1}{4}\right) = 0.31128 + 0.50000 = \mathbf{0.81128 \text{ bits}}$$</li>
            </ul>
            <p><strong>Step 3: Remainder / Expected Child Entropy:</strong></p>
            $$\text{Remainder}(S, \text{Outlook}) = \sum_{v} \frac{|S_v|}{|S|} H(S_v) = \frac{4}{10}(0.81128) + \frac{2}{10}(0) + \frac{4}{10}(0.81128) = \frac{8}{10}(0.81128) = \mathbf{0.64902 \text{ bits}}$$
            <p><strong>Step 4: Information Gain:</strong></p>
            $$\mathbf{IG(S, \text{Outlook}) = H(S) - \text{Remainder}(S, \text{Outlook}) = 0.97095 - 0.64902 = \mathbf{0.32193 \text{ bits}}}$$
            <p><em>Conclusion:</em> Because $IG(S, \text{Outlook}) = 0.32193$ is positive and maximal among candidates, Outlook is selected as the designated root node of the ID3 decision tree (Figure 3.2).</p>
          </div>
        </div>

        <!-- CIE-2 Q1.a: CART Algorithm -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (May 2026) &bull; Q 1(a)</span>
            <span class="archive-marks">[3 Marks &bull; Blooms L2, CO3]</span>
          </div>
          <p class="archive-q">"Explain the working of the CART algorithm."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Classification and Regression Trees (CART)</strong>, developed by Breiman et al., constructs strictly <em>binary trees</em> (every non-leaf node has exactly two children):</p>
            <ul>
              <li><strong>1. Splitting Criterion (Gini Impurity for Classification):</strong>
                $$\text{Gini}(S) = 1 - \sum_{i=1}^C p_i^2$$
                For a binary split candidate dividing $S$ into subsets $S_L$ and $S_R$, CART selects the split maximizing the reduction in impurity:
                $$\Delta \text{Gini}(S, A) = \text{Gini}(S) - \left( \frac{|S_L|}{|S|}\text{Gini}(S_L) + \frac{|S_R|}{|S|}\text{Gini}(S_R) \right)$$</li>
              <li><strong>2. Splitting for Regression Trees:</strong> Uses Mean Squared Error (variance reduction): $\sum_{x \in S_L}(y_i - \bar{y}_L)^2 + \sum_{x \in S_R}(y_i - \bar{y}_R)^2$.</li>
              <li><strong>3. Cost-Complexity Pruning:</strong> Minimizes cost function $R_\alpha(T) = R(T) + \alpha |T|$ where $R(T)$ is misclassification rate, $|T|$ is number of terminal nodes, and $\alpha$ is penalty parameter tuned via cross-validation.</li>
            </ul>
          </div>
        </div>

        <!-- CIE-2 Q3.a: K-NN Regression on HPI -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (May 2026) &bull; Q 3(a)</span>
            <span class="archive-marks">[3 Marks &bull; Blooms L3, CO3]</span>
          </div>
          <p class="archive-q">"Age and Loan are predictors and House Price Index (HPI) is the numerical target attribute. The distance given is Euclidean distance. Apply K-NN Regression to find HPI if Age is 48 and Loan is $142,000. Assume K = 3."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Given 11 instances with pre-computed Euclidean distances from query $(48, \$142,000)$:</strong></p>
            <p>Sorting all 11 samples by ascending Euclidean distance to identify the $K=3$ nearest neighbors:</p>
            <ol>
              <li><strong>Rank 1 (Sample 11):</strong> Age 33, Loan $\$150,000 \implies \mathbf{\text{Distance} = 8,000}, \quad \mathbf{\text{HPI} = 264}$</li>
              <li><strong>Rank 2 (Sample 5):</strong> Age 35, Loan $\$120,000 \implies \mathbf{\text{Distance} = 22,000}, \quad \mathbf{\text{HPI} = 139}$</li>
              <li><strong>Rank 3 (Sample 9):</strong> Age 60, Loan $\$100,000 \implies \mathbf{\text{Distance} = 42,000}, \quad \mathbf{\text{HPI} = 139}$</li>
            </ol>
            <p><em>(Next nearest is Sample 7 with distance $47,000$, excluded since $K=3$).</em></p>
            <p><strong>Unweighted $K$-NN Regression Prediction:</strong></p>
            $$\hat{y}_{\text{HPI}} = \frac{1}{K} \sum_{i=1}^3 y_i = \frac{264 + 139 + 139}{3} = \frac{542}{3} \approx \mathbf{180.67}$$
            <p><strong>Optional Distance-Weighted Prediction ($w_i = \frac{1}{d_i^2}$):</strong></p>
            $$\hat{y}_w = \frac{264\left(\frac{1}{8^2}\right) + 139\left(\frac{1}{22^2}\right) + 139\left(\frac{1}{42^2}\right)}{\frac{1}{8^2} + \frac{1}{22^2} + \frac{1}{42^2}} \approx \mathbf{245.97}$$
          </div>
        </div>

        <!-- SEE June/July 2026 Q5.a: Multiple Linear Regression -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah SEE Examination (June/July 2026) &bull; Q 5(a)</span>
            <span class="archive-marks">[8 Marks &bull; Blooms L3, CO3]</span>
          </div>
          <p class="archive-q">"Compare simple linear regression and multiple linear regression with suitable examples. Using the housing dataset (Size, Bedrooms, Age, House Price), formulate a multiple linear regression equation to predict house price."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <ul>
              <li><strong>Simple Linear Regression:</strong> Models the relationship between <em>one</em> scalar predictor $x$ and scalar target $y$:
                $$y = w_0 + w_1 x + \epsilon$$
                <em>Example:</em> Predicting house price based solely on floor area ($x_1$).</li>
              <li><strong>Multiple Linear Regression:</strong> Models the relationship between $p$ multiple independent variables $\mathbf{x} = [x_1, x_2, \dots, x_p]^T$ and scalar target $y$:
                $$y = w_0 + w_1 x_1 + w_2 x_2 + \dots + w_p x_p + \epsilon = \mathbf{w}^T \mathbf{x} + \epsilon$$</li>
              <li><strong>Housing Price Multiple Regression Equation Formulation:</strong>
                $$\mathbf{\widehat{\text{Price}} = w_0 + w_1 (\text{Size}) + w_2 (\text{Bedrooms}) + w_3 (\text{Age})}$$
                Where $\mathbf{w} = [w_0, w_1, w_2, w_3]^T$ is solved via the closed-form normal equations:
                $$\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$</li>
            </ul>
          </div>
        </div>
      </section>'''

    # Replace old questions-asked-before section
    m_archive = re.search(r'<section[^>]*id="sec-questions-asked-before".*?</section>', html, re.DOTALL)
    if m_archive:
        html = html[:m_archive.start()] + archive_section + html[m_archive.end():]

    # 6. ENRICH PRACTICE PROBLEMS WITH 6 VERIFIED PROBLEMS
    practice_section = r'''      <section id="sec-practice-problems" class="notes-section">
        <h2 class="section-title">Practice Problems (Step-by-Step Verified Solutions)</h2>
        <p class="section-lead">The following 6 practice problems have been mathematically verified via <code>audit/verify/ml/verify_ml_u3.py</code>. Attempt each manually before expanding the solution blocks.</p>

        <!-- Problem 1: KNN Classification -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 1 (K-NN Classification &amp; Weighted Voting):</strong> Given 5 training instances: $A(1, 2) \to +1, B(2, 3) \to +1, C(3, 1) \to -1, D(5, 4) \to -1, E(6, 5) \to -1$. For query point $Q(2, 2)$: (i) Find the 3 nearest neighbors. (ii) Predict class using majority voting. (iii) Predict class using inverse square distance weighting ($w_i = 1/d^2$).
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <p>Euclidean distances from $Q(2, 2)$:</p>
              <ul>
                <li>$d(Q, A) = \sqrt{(1-2)^2 + (2-2)^2} = \sqrt{1} = \mathbf{1.0000} \implies \text{Label: } +1$</li>
                <li>$d(Q, B) = \sqrt{(2-2)^2 + (3-2)^2} = \sqrt{1} = \mathbf{1.0000} \implies \text{Label: } +1$</li>
                <li>$d(Q, C) = \sqrt{(3-2)^2 + (1-2)^2} = \sqrt{1 + 1} = \sqrt{2} \approx \mathbf{1.4142} \implies \text{Label: } -1$</li>
                <li>$d(Q, D) = \sqrt{3^2 + 2^2} = \sqrt{13} \approx 3.6056$</li>
                <li>$d(Q, E) = \sqrt{4^2 + 3^2} = \sqrt{25} = 5.0000$</li>
              </ul>
              <p><strong>(i) Top 3 Nearest:</strong> $\{A, B, C\}$.</p>
              <p><strong>(ii) Majority Voting:</strong> Labels $\{+1, +1, -1\} \implies \text{Sum} = +1 > 0 \implies \mathbf{\text{Class } +1}$.</p>
              <p><strong>(iii) Inverse-Square Weighted Voting:</strong>
                <br>&bull; Weight for $+1$: $w_A + w_B = \frac{1}{1^2} + \frac{1}{1^2} = 1.0 + 1.0 = \mathbf{2.0000}$.
                <br>&bull; Weight for $-1$: $w_C = \frac{1}{(\sqrt{2})^2} = \frac{1}{2} = \mathbf{0.5000}$.
                <br>Since $2.0000 > 0.5000$, predicted label is strictly $\mathbf{+1}$.</p>
            </div>
          </details>
        </div>

        <!-- Problem 2: Linear Regression OLS -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 2 (Linear Regression Normal Equation):</strong> For points $X = [1, 2, 3, 4, 5]$ and $Y = [2, 3, 5, 4, 6]$, find: (i) OLS regression slope $m$ and intercept $c$, (ii) Predicted value $\hat{y}(6)$, and (iii) Coefficient of determination $R^2$.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <p>$\bar{X} = 3.0, \bar{Y} = 4.0, n = 5$.</p>
              <ul>
                <li>$\sum (x_i - \bar{X})(y_i - \bar{Y}) = (-2)(-2) + (-1)(-1) + (0)(1) + (1)(0) + (2)(2) = 4 + 1 + 0 + 0 + 4 = \mathbf{9.0}$.</li>
                <li>$\sum (x_i - \bar{X})^2 = 4 + 1 + 0 + 1 + 4 = \mathbf{10.0}$.</li>
                <li>$\mathbf{m = \frac{9.0}{10.0} = 0.9000}, \quad \mathbf{c = 4.0 - (0.90 \times 3.0) = 1.3000}$.</li>
                <li>Equation: $\mathbf{y = 0.90 x + 1.30}$.</li>
                <li>$\mathbf{\hat{y}(6) = 0.90(6) + 1.30 = 5.40 + 1.30 = 6.7000}$.</li>
                <li>$SS_{\text{tot}} = 10.0, SS_{\text{res}} = 1.90 \implies \mathbf{R^2 = 1 - \frac{1.90}{10.0} = 0.8100 \quad (81.00\%)}$.</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 3: ID3 Root Selection on 6 instances -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 3 (ID3 Decision Tree Split):</strong> A dataset of 6 instances has 4 Positive and 2 Negative examples. Feature Outlook partitions into Sunny (1+, 2-) and Overcast (3+, 0-). Compute $H(S)$ and $IG(S, \text{Outlook})$.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <ul>
                <li>$H(S) = -\frac{4}{6}\log_2\left(\frac{4}{6}\right) - \frac{2}{6}\log_2\left(\frac{2}{6}\right) \approx \mathbf{0.9183 \text{ bits}}$.</li>
                <li>$H(S_{\text{Sunny}}) = -\frac{1}{3}\log_2\left(\frac{1}{3}\right) - \frac{2}{3}\log_2\left(\frac{2}{3}\right) \approx \mathbf{0.9183 \text{ bits}}$.</li>
                <li>$H(S_{\text{Overcast}}) = \mathbf{0.0000 \text{ bits}}$ (pure node).</li>
                <li>$\text{Remainder} = \frac{3}{6}(0.9183) + \frac{3}{6}(0.0) = \mathbf{0.4591 \text{ bits}}$.</li>
                <li>$\mathbf{IG(S, \text{Outlook}) = 0.9183 - 0.4591 = 0.4591 \text{ bits}}$.</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 4: Logistic Regression Probability -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 4 (Logistic Regression Odds &amp; Sigmoid):</strong> A trained logistic model has weights $w_0 = -3.0, w_1 = 0.5, w_2 = 0.2$. For input feature vector $x = [4, 10]$: (i) Compute the logit score $z$. (ii) Compute the odds ratio $e^z$. (iii) Compute probability $P(y=1|x)$.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <ul>
                <li><strong>Logit:</strong> $z = w_0 + w_1 x_1 + w_2 x_2 = -3.0 + 0.5(4) + 0.2(10) = -3.0 + 2.0 + 2.0 = \mathbf{+1.0000}$.</li>
                <li><strong>Odds:</strong> $\text{Odds} = e^z = e^{1.0} \approx \mathbf{2.7183}$.</li>
                <li><strong>Sigmoid Probability:</strong>
                  $$P(y=1|x) = \sigma(z) = \frac{1}{1 + e^{-1.0}} = \frac{1}{1 + 0.36788} = \frac{1}{1.36788} \approx \mathbf{0.7311 \quad (73.11\%)}.$$</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 5: CART Gini Impurity -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 5 (Gini Impurity Calculation):</strong> A binary dataset $S$ contains 4 positive and 6 negative instances. Compute the Gini Impurity $\text{Gini}(S)$. If a split divides $S$ into $S_L$ (3+, 1-) and $S_R$ (1+, 5-), compute the Gini Gain $\Delta \text{Gini}$.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <ul>
                <li>$\text{Gini}(S) = 1 - \left[\left(\frac{4}{10}\right)^2 + \left(\frac{6}{10}\right)^2\right] = 1 - [0.16 + 0.36] = 1 - 0.52 = \mathbf{0.4800}$.</li>
                <li>$\text{Gini}(S_L) = 1 - \left[\left(\frac{3}{4}\right)^2 + \left(\frac{1}{4}\right)^2\right] = 1 - [0.5625 + 0.0625] = \mathbf{0.3750}$.</li>
                <li>$\text{Gini}(S_R) = 1 - \left[\left(\frac{1}{6}\right)^2 + \left(\frac{5}{6}\right)^2\right] = 1 - \left[\frac{1 + 25}{36}\right] = 1 - \frac{26}{36} \approx \mathbf{0.2778}$.</li>
                <li>$\text{Weighted Gini} = \frac{4}{10}(0.3750) + \frac{6}{10}(0.2778) = 0.1500 + 0.1667 = \mathbf{0.3167}$.</li>
                <li>$\mathbf{\Delta \text{Gini} = 0.4800 - 0.3167 = 0.1633}$. (Positive gain confirms informative split).</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 6: Locally Weighted Regression Kernel -->
        <div class="problem-card">
          <div class="problem-statement">
            <strong>Problem 6 (LWR Gaussian Kernel Weights):</strong> For query point $x_q = 5$ and bandwidth parameter $\tau = 2.0$, compute the Gaussian kernel weights $w_i = \exp\left(-\frac{(x_i - x_q)^2}{2\tau^2}\right)$ for data points $x_1 = 3, x_2 = 5, x_3 = 8$.
          </div>
          <details class="model-answer">
            <summary>View Verified Solution</summary>
            <div class="answer-body">
              <p>$2\tau^2 = 2(2^2) = 2(4) = 8.0$.</p>
              <ul>
                <li>$x_1 = 3 \implies (3 - 5)^2 = 4 \implies w_1 = \exp\left(-\frac{4}{8}\right) = e^{-0.5} \approx \mathbf{0.6065}$.</li>
                <li>$x_2 = 5 \implies (5 - 5)^2 = 0 \implies w_2 = \exp(0) = \mathbf{1.0000}$ (Maximum weight at query point).</li>
                <li>$x_3 = 8 \implies (8 - 5)^2 = 9 \implies w_3 = \exp\left(-\frac{9}{8}\right) = e^{-1.125} \approx \mathbf{0.3247}$.</li>
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

    print(f"ML Unit 3 enriched successfully! File size: {len(html)} bytes")

if __name__ == "__main__":
    build()
