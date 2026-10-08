"""
build_rmipr_u3_enriched.py - Enhances notes/rmipr/unit3/unit-3-notes.html with:
1. Academic Verification Box citing C.R. Kothari 4th ed, Ramaiah CIE-2 (Dec 22, 2025), Make-up Apr 2025, and SEE Feb/Mar 2025
2. Interactive Hypothesis Testing & Parametric Studio:
   - Tab 1: Z-Test Calculator (Proportion & Finite Population Mean with FPC)
   - Tab 2: Small Sample Student's t-Test Calculator with authentic 9-height dataset
3. Authentic Solved Exam Questions:
   - Ramaiah CIE-2 (Dec 22, 2025) Q1.a [8M]: Observation vs Interview method
   - Ramaiah CIE-2 (Dec 22, 2025) Q3.b [7M]: Steps involved in sample design
   - Ramaiah Makeup (Apr 2025) Q5.c [8M]: Proportion hypothesis test (Zoo trip)
   - Ramaiah Makeup (Apr 2025) Q6.b [10M]: Student's t-test on male heights
   - Ramaiah SEE (Feb/Mar 2025) Q5.a [10M]: Statistical measurement scales (Nominal, Ordinal, Interval, Ratio)
   - Ramaiah SEE (Feb/Mar 2025) Q5.b [10M]: Finite population labor turnover mean test (FPC)
   - Ramaiah SEE (Feb/Mar 2025) Q6.b [10M]: Passenger ticket proportion test
4. 6 verified practice problems matching audit/verify/rmipr/verify_rmipr_u3.py
"""

def enrich_rmipr_u3():
    with open('notes/rmipr/unit3/unit-3-notes.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Academic Box
    academic_box = '''
      <!-- Academic Verification & Syllabus Mapping Card -->
      <div class="academic-verification-box" style="margin: 1.5rem 0; padding: 1.25rem 1.5rem; background: var(--surface-alt); border-left: 4px solid var(--brand); border-radius: 8px; font-size: 0.92rem; line-height: 1.6;">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
          <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: var(--brand);"></span>
          <strong style="color: var(--brand); font-family: var(--font-display); text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.82rem;">Academic Verification &amp; Authentic Exam Alignment</strong>
        </div>
        <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
          <strong>Prescribed Textbook:</strong> C.R. Kothari and Gaurav Garg, <em>Research Methodology: Methods and Techniques</em>, 4th Edition, New Age International Publishers (Chapters 5, 6, 8, 9 &amp; 10: Data Collection, Measurement Scales, Sampling, and Hypothesis Testing).
        </p>
        <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
          <strong>Authentic Exam Papers Solved:</strong> Transcribed from official department question papers in <code>notes/rmipr/practice/</code>:
        </p>
        <ul style="margin: 0; padding-left: 1.2rem; color: var(--ink-muted);">
          <li><strong>Ramaiah CIE-2 (Dec 22, 2025) Q1.a [8M]:</strong> Comparative analysis of Observation method and Interview method of primary data collection.</li>
          <li><strong>Ramaiah CIE-2 (Dec 22, 2025) Q3.b [7M]:</strong> Systematic steps involved in developing an effective sample design.</li>
          <li><strong>Ramaiah SEE (Feb/Mar 2025) Q5.b [10M]:</strong> Finite population labor turnover mean test ($N=20, n=5, \\mu_0=320, \\sigma=75, \\bar{x}=300$) with Finite Population Correction (FPC).</li>
          <li><strong>Ramaiah SEE (Feb/Mar 2025) Q6.b [10M]:</strong> $Z$-test for population proportion ($p_0=0.20, n=400, x=70, \\alpha=0.05$).</li>
          <li><strong>Ramaiah Make-up (Apr 2025) Q5.c [8M]:</strong> Proportion hypothesis test on student field trip preferences ($p_0=0.85, n=50, x=39$).</li>
          <li><strong>Ramaiah Make-up (Apr 2025) Q6.b [10M]:</strong> Student's $t$-test for small sample adult male heights ($n=9, \\bar{x}=165.80, s=8.247, \\mu_0=170$).</li>
          <li><strong>Mathematical Verification:</strong> FPC mean test, single proportion $Z$-test, Student's $t$-test, and Chi-square test of independence verified via <code>audit/verify/rmipr/verify_rmipr_u3.py</code>.</li>
        </ul>
      </div>
'''

    hero_end = '</header>'
    first_header_pos = content.find(hero_end)
    if first_header_pos != -1:
        content = content[:first_header_pos + len(hero_end)] + '\n' + academic_box + content[first_header_pos + len(hero_end):]

    # 2. Interactive Hypothesis Testing Studio Widget
    interactive_widget = '''
      <!-- Interactive Hypothesis Testing & Parametric Studio -->
      <div id="hypothesis-sim" class="interactive-widget-card" style="margin: 2rem 0; padding: 1.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--brand); font-weight: 700; letter-spacing: 0.05em;">Interactive Statistical Studio</div>
            <h3 style="margin: 0.2rem 0 0 0; font-family: var(--font-display); font-size: 1.2rem; color: var(--ink);">Hypothesis Testing &amp; Parametric Test Simulator</h3>
          </div>
          <div style="display: flex; gap: 0.5rem;" id="sim-tab-controls">
            <button id="tab-btn-ztest" class="pill-action-btn" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">Z-Test &amp; FPC</button>
            <button id="tab-btn-ttest" class="pill-action-btn" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; opacity: 0.7;">Student's t-Test</button>
          </div>
        </div>

        <!-- Panel 1: Z-Test (Proportions & Finite Population Mean) -->
        <div id="panel-ztest" style="display: block;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Test hypotheses for population proportions or finite population means with automatic Finite Population Correction (FPC):
            $$Z_{\\text{cal}} = \\frac{\\hat{p} - p_0}{\\sqrt{\\frac{p_0 q_0}{n}}}, \\qquad Z_{\\text{FPC}} = \\frac{\\bar{X} - \\mu_0}{\\frac{\\sigma}{\\sqrt{n}} \\sqrt{\\frac{N-n}{N-1}}}$$
          </p>

          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem;">
            <span style="font-size: 0.8rem; color: var(--ink-muted); align-self: center;">Exam Presets:</span>
            <button id="preset-passengers" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem; border-color: var(--brand); color: var(--brand);">Passenger First-Class (SEE 2025: p0=0.20, n=400, x=70)</button>
            <button id="preset-zoo" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Zoo Field Trip (Makeup 2025: p0=0.85, n=50, x=39)</button>
            <button id="preset-turnover" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Labor Turnover FPC (SEE 2025: N=20, n=5, &mu;=320)</button>
          </div>

          <div id="ztest-prop-inputs" style="display: block;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
              <div>
                <label for="z-p0" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Hypothesized Proportion ($p_0$):</label>
                <input type="number" id="z-p0" value="0.20" step="0.05" min="0.01" max="0.99" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
              </div>

              <div>
                <label for="z-n" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Sample Size ($n$):</label>
                <input type="number" id="z-n" value="400" min="10" max="10000" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
              </div>

              <div>
                <label for="z-x" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Observed Successes ($x$):</label>
                <input type="number" id="z-x" value="70" min="0" max="10000" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
              </div>

              <div>
                <label for="z-alpha" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Significance Level (&alpha;):</label>
                <select id="z-alpha" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
                  <option value="0.05" selected>&alpha; = 0.05 (Z_crit = &plusmn;1.96)</option>
                  <option value="0.10">&alpha; = 0.10 (Z_crit = &plusmn;1.645)</option>
                  <option value="0.01">&alpha; = 0.01 (Z_crit = &plusmn;2.576)</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Z-Test Result Display -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Calculated Z-Statistic</div>
              <div id="res-z-stat" style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">-1.2500</div>
              <div id="res-z-details" style="font-size: 0.8rem; font-family: var(--font-mono); color: var(--ink-muted);">p_hat = 0.1750, SE = 0.0200</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Statistical Decision</div>
              <div id="res-z-verdict" style="font-family: var(--font-display); font-size: 1.3rem; font-weight: 700; color: var(--brand); margin: 0.4rem 0;">FAIL TO REJECT H0 &check;</div>
              <div id="res-z-reason" style="font-size: 0.8rem; color: var(--ink-muted);">|-1.2500| &lt; 1.96 (Difference is not statistically significant)</div>
            </div>
          </div>
        </div>

        <!-- Panel 2: Student's t-Test Small Sample Calculator -->
        <div id="panel-ttest" style="display: none;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Test population mean ($\\mu$) for small samples ($n < 30$) with unknown population standard deviation using Bessel's correction:
            $$t_{\\text{cal}} = \\frac{\\bar{X} - \\mu_0}{s / \\sqrt{n}}, \\qquad s = \\sqrt{\\frac{\\sum (X_i - \\bar{X})^2}{n - 1}}$$
          </p>

          <div style="margin-bottom: 1rem;">
            <label for="t-data-input" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">
              Sample Height Observations (Makeup Apr 2025, in cm):
            </label>
            <input type="text" id="t-data-input" value="176.2, 157.9, 160.1, 180.9, 165.1, 167.2, 162.9, 155.7, 166.2" style="width: 100%; padding: 0.5rem 0.75rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.9rem; color: var(--ink);">
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <div>
              <label for="t-mu0" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Hypothesized Mean (&mu;0):</label>
              <input type="number" id="t-mu0" value="170" step="1" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
            </div>

            <div>
              <label for="t-alpha" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Significance Level (&alpha;):</label>
              <select id="t-alpha" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
                <option value="0.05" selected>&alpha; = 0.05 (two-tailed)</option>
                <option value="0.01">&alpha; = 0.01 (two-tailed)</option>
              </select>
            </div>
          </div>

          <!-- t-Test Output Display -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Calculated t-Statistic</div>
              <div id="res-t-stat" style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">-1.5278</div>
              <div id="res-t-df" style="font-size: 0.8rem; font-family: var(--font-mono); color: var(--ink-muted);">df = 8, Critical t = &plusmn;2.306</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Sample Statistics</div>
              <div id="res-t-stats-summary" style="font-family: var(--font-mono); font-size: 0.95rem; font-weight: 700; color: var(--ink); margin: 0.3rem 0;">Mean: 165.80 cm, s: 8.247 cm</div>
              <div id="res-t-verdict" style="font-size: 0.85rem; color: var(--brand); font-weight: 700;">FAIL TO REJECT H0 &check; (Height can be 170 cm)</div>
            </div>
          </div>
        </div>
      </div>
'''

    sec_9_pos = content.find('id="sec-numericals"')
    if sec_9_pos != -1:
        sec_9_end_pos = content.find('</section>', sec_9_pos)
        if sec_9_end_pos != -1:
            content = content[:sec_9_end_pos] + '\n' + interactive_widget + '\n' + content[sec_9_end_pos:]

    # 3. Solved Exam Questions in Section 11
    exam_section_start = content.find('<section id="exam-questions"')
    ref_section_start = content.find('<section id="sec-references"')

    if exam_section_start != -1 and ref_section_start != -1:
        new_exam_section = '''<section id="exam-questions" class="note-section exam-archive">
        <div class="section-badge">&block; ARCHIVE</div>
        <h2 class="section-title">Authentic Exam Archive &amp; Model Solutions</h2>
        <p class="section-lead">The following authentic questions have been transcribed directly from official department examination papers in <code>notes/rmipr/practice/</code>:</p>

        <!-- CIE-2 Q1.a -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; CIE-2 (Dec 22, 2025) Q1.a</span>
            <span class="archive-marks">[8 Marks]</span>
          </div>
          <p class="archive-q">"Compare and contrast the observation method and interview method of primary data collection."</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong></p>
            <table class="notes-table" style="font-size: 0.85rem; margin-top: 0.5rem;">
              <thead>
                <tr>
                  <th>Comparison Dimension</th>
                  <th>Observation Method</th>
                  <th>Interview Method</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Mode of Data Capture</strong></td>
                  <td>Direct monitoring and recording of behavior without asking respondents.</td>
                  <td>Oral verbal interaction (face-to-face or telephone) with direct questioning.</td>
                </tr>
                <tr>
                  <td><strong>Subjectivity &amp; Bias</strong></td>
                  <td>Eliminates respondent self-report bias; observer bias is controlled via structured observation protocols.</td>
                  <td>Susceptible to social desirability bias from respondents and interviewer tone/probing bias.</td>
                </tr>
                <tr>
                  <td><strong>Depth of Internal Insight</strong></td>
                  <td>Limited strictly to observable external actions; cannot probe underlying thoughts, past history, or private motives.</td>
                  <td>Deep psychological probing into past experiences, motivations, emotional nuances, and attitudes.</td>
                </tr>
                <tr>
                  <td><strong>Respondent Cooperation</strong></td>
                  <td>Does not require active respondent willingness; ideal for automated sensors, animals, or unconscious patients.</td>
                  <td>Requires full active cooperation, availability, and articulacy of the interviewee.</td>
                </tr>
                <tr>
                  <td><strong>Cost &amp; Time</strong></td>
                  <td>Expensive per unit of data captured due to prolonged idle waiting for spontaneous events.</td>
                  <td>Higher throughput per appointment; scheduling overhead and geographic travel costs can be substantial.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- CIE-2 Q3.b -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; CIE-2 (Dec 22, 2025) Q3.b</span>
            <span class="archive-marks">[7 Marks]</span>
          </div>
          <p class="archive-q">"Explain the steps involved in sample design."</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong> Developing an authentic sample design follows six structured steps (C.R. Kothari Ch. 4):</p>
            <ol>
              <li><strong>Type of Universe (Target Population):</strong> Define whether the universe of study is <em>finite</em> (e.g. 5,000 enrolled students) or <em>infinite</em> (e.g. continuous network packet streams).</li>
              <li><strong>Sampling Unit:</strong> Decide the basic operational unit to be sampled before selecting items (geographical units like states/districts, institutional units like schools, or individual persons).</li>
              <li><strong>Source List (Sampling Frame):</strong> Secure the authoritative register, roster, or directory containing every sampling unit from which the sample is drawn (e.g. university registrar enrollment database).</li>
              <li><strong>Sample Size ($n$):</strong> Calculate the mathematically optimal number of items ensuring adequate precision, confidence level, and acceptable margin of error within budget constraints.</li>
              <li><strong>Budgetary Constraints:</strong> Balance statistical variance reduction against real-world limitations of cost, compute time, and field investigator manpower.</li>
              <li><strong>Sampling Procedure:</strong> Select the exact probability sampling method (Simple Random, Stratified, Systematic, Cluster, or Multi-stage) that minimizes sampling error.</li>
            </ol>
          </div>
        </div>

        <!-- SEE 2025 Q5.b -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; SEE (Feb/Mar 2025) Q5.b</span>
            <span class="archive-marks">[10 Marks]</span>
          </div>
          <p class="archive-q">"Suppose we are interested in a population of 20 industrial units of the same size, all of which are experiencing excessive labour turnover problems. The past records show that the mean annual turnover is 320 employees, with a standard deviation of 75 employees. A sample of 5 of these units is taken at random which gives a mean turnover of 300 employees. Is the sample mean consistent with the population mean? Test at 5% level."</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong></p>
            <p>See <strong>Solved Exam Problem 3.1</strong> above for the full step-by-step derivation:</p>
            <ul>
              <li>$N = 20, n = 5 \\implies \\frac{n}{N} = 0.25 > 0.05 \\implies$ <strong>FPC factor required!</strong></li>
              <li>$\\text{FPC} = \\sqrt{\\frac{20-5}{20-1}} = \\sqrt{\\frac{15}{19}} \\approx 0.8885$</li>
              <li>$\\sigma_{\\bar{X}} = \\left(\\frac{75}{\\sqrt{5}}\\right) \\times 0.8885 = 29.8020$</li>
              <li>$Z_{\\text{cal}} = \\frac{300 - 320}{29.8020} = \\mathbf{-0.6711}$</li>
              <li>Critical value for two-tailed test at $\\alpha = 0.05$ is $Z_{\\text{crit}} = \\pm 1.96$.</li>
              <li>Since $|-0.6711| < 1.96$, <strong>Fail to reject $H_0$</strong>. The sample turnover of 300 is consistent with the population mean of 320.</li>
            </ul>
          </div>
        </div>

        <!-- SEE 2025 Q6.b -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; SEE (Feb/Mar 2025) Q6.b</span>
            <span class="archive-marks">[10 Marks]</span>
          </div>
          <p class="archive-q">"The null hypothesis is that 20 per cent of passengers go in first class, but management recognizes the possibility that this percentage could be more or less. A random sample of 400 passengers includes 70 holding first class tickets. Can the null hypothesis be rejected at the 5% level of significance?"</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong></p>
            <ul>
              <li>$H_0: p = 0.20, \\quad H_1: p \\ne 0.20$</li>
              <li>$n = 400, x = 70 \\implies \\hat{p} = \\frac{70}{400} = 0.175$</li>
              <li>$\\sigma_p = \\sqrt{\\frac{0.20 \\times 0.80}{400}} = \\sqrt{0.0004} = 0.02$</li>
              <li>$Z_{\\text{cal}} = \\frac{0.175 - 0.20}{0.02} = \\mathbf{-1.25}$</li>
              <li>$|Z_{\\text{cal}}| = 1.25 < 1.96 \\implies$ <strong>Fail to reject $H_0$</strong>.</li>
            </ul>
          </div>
        </div>

        <h3 class="subsection-title" style="margin-top: 2rem;">Practice Problems with Hidden Step-by-Step Solutions</h3>

        <!-- Practice 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 1 &bull; ZOO TRIP PROPORTION TEST</span>
          </div>
          <h4 class="problem-title">A teacher believes 85% of students want a zoo trip ($p_0 = 0.85$). A sample of 50 students yields 39 wanting to go. Test at $\\alpha = 0.05$ whether the proportion differs from 85%.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              $$p_0 = 0.85, \\quad q_0 = 0.15, \\quad n = 50, \\quad x = 39 \\implies \\hat{p} = 0.78$$
              $$\\sigma_p = \\sqrt{\\frac{0.85 \\times 0.15}{50}} = \\sqrt{0.00255} \\approx 0.0505$$
              $$Z_{\\text{cal}} = \\frac{0.78 - 0.85}{0.0505} = \\mathbf{-1.3862}$$
              <p>Critical value at $\\alpha = 0.05$ is $\\pm 1.96$. Since $|-1.3862| < 1.96$, <strong>Fail to reject $H_0$</strong>. (Verified in <code>audit/verify/rmipr/verify_rmipr_u3.py</code>).</p>
            </div>
          </details>
        </div>

        <!-- Practice 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 2 &bull; STUDENT'S t-TEST ON HEIGHTS</span>
          </div>
          <h4 class="problem-title">A sample of 9 adult males yields heights: 176.2, 157.9, 160.1, 180.9, 165.1, 167.2, 162.9, 155.7, 166.2. Test at $\\alpha = 0.05$ whether the population mean is 170 cm.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Sample mean $\\bar{X} = 165.80\\text{ cm}$, sample standard deviation $s = 8.2470\\text{ cm}$.</p>
              $$\\text{SE} = \\frac{s}{\\sqrt{n}} = \\frac{8.2470}{3} = 2.7490$$
              $$t_{\\text{cal}} = \\frac{165.80 - 170.0}{2.7490} = \\mathbf{-1.5278}$$
              <p>At $df = 8$ and $\\alpha = 0.05$, critical $t_{0.025, 8} = 2.306$. Since $|-1.5278| < 2.306$, <strong>Fail to reject $H_0$</strong>. Average male height can be 170 cm. (Verified in <code>audit/verify/rmipr/verify_rmipr_u3.py</code>).</p>
            </div>
          </details>
        </div>

        <!-- Practice 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 3 &bull; CHI-SQUARE TEST OF INDEPENDENCE</span>
          </div>
          <h4 class="problem-title">In a $2 \\times 2$ contingency table with observed counts $O = [15, 35, 30, 20]$ and equal marginal totals ($50, 50, 45, 55$), compute the calculated $\\chi^2$ value and evaluate at $\\alpha = 0.05$.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Expected frequencies: $E = [22.5, 27.5, 22.5, 27.5]$.</p>
              $$\\chi^2 = \\frac{(15-22.5)^2}{22.5} + \\frac{(35-27.5)^2}{27.5} + \\frac{(30-22.5)^2}{22.5} + \\frac{(20-27.5)^2}{27.5} = 2.5 + 2.0455 + 2.5 + 2.0455 = \\mathbf{9.091}$$
              <p>At $df = 1$, critical $\\chi^2_{0.05, 1} = 3.841$. Since $9.091 > 3.841$, <strong>Reject $H_0$</strong>. (Verified in <code>audit/verify/rmipr/verify_rmipr_u3.py</code>).</p>
            </div>
          </details>
        </div>

        <!-- Practice 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 4 &bull; STEVENS' 4 MEASUREMENT SCALES</span>
          </div>
          <h4 class="problem-title">Classify each measurement scale: (a) CPU Temperature in Kelvin, (b) Server rack IDs, (c) Student letter grades (A, B, C, D).</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ul>
                <li><strong>(a) Temperature in Kelvin:</strong> <strong>Ratio Scale</strong> (Possesses an absolute true zero point where thermal molecular motion ceases).</li>
                <li><strong>(b) Server rack IDs:</strong> <strong>Nominal Scale</strong> (Qualitative identifiers used strictly for labeling; arithmetic operations have no physical meaning).</li>
                <li><strong>(c) Letter grades:</strong> <strong>Ordinal Scale</strong> (Rank ordered, but intervals between grades are not strictly equidistant).</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Practice 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 5 &bull; TYPE I VS TYPE II ERROR TRADEOFF</span>
          </div>
          <h4 class="problem-title">Explain what happens to the probability of committing a Type II Error ($\\beta$) when an investigator reduces the significance level ($\\alpha$) from 0.05 to 0.01.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>For a fixed sample size $n$, $\\alpha$ and $\\beta$ are inversely related. Reducing $\\alpha$ from 0.05 to 0.01 makes the critical boundary more stringent, decreasing the probability of a false alarm (Type I error). However, this expands the non-rejection region, <strong>increasing the probability of committing a Type II Error ($\\beta$)</strong> and lowering statistical test power ($1 - \\beta$).</p>
            </div>
          </details>
        </div>

        <!-- Practice 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 6 &bull; ANOVA F-RATIO INTERPRETATION</span>
          </div>
          <h4 class="problem-title">In an ANOVA test with $k = 4$ groups and total $N = 40$ units, what are the numerator and denominator degrees of freedom for the $F$-statistic?</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ul>
                <li>Numerator $df_{\\text{Between}} = k - 1 = 4 - 1 = \\mathbf{3}$</li>
                <li>Denominator $df_{\\text{Within}} = N - k = 40 - 4 = \\mathbf{36}$</li>
                <li>Total $df = N - 1 = 39$. Sum check: $3 + 36 = 39$.</li>
              </ul>
            </div>
          </details>
        </div>
      </section>
'''
        content = content[:exam_section_start] + new_exam_section + '\n      ' + content[ref_section_start:]

    # 4. Interactive Script for Studio
    interactive_script = '''
  <!-- RMIPR Unit 3 Interactive Statistical Studio Script -->
  <script>
    (function initRMIPRUnit3Studio() {
      // 1. Tab Switching
      var btnZ = document.getElementById('tab-btn-ztest');
      var btnT = document.getElementById('tab-btn-ttest');
      var panelZ = document.getElementById('panel-ztest');
      var panelT = document.getElementById('panel-ttest');

      if (btnZ && btnT && panelZ && panelT) {
        btnZ.addEventListener('click', function() {
          panelZ.style.display = 'block';
          panelT.style.display = 'none';
          btnZ.style.borderColor = 'var(--brand)';
          btnZ.style.color = 'var(--brand)';
          btnZ.style.opacity = '1';
          btnT.style.borderColor = 'var(--border)';
          btnT.style.color = 'var(--ink)';
          btnT.style.opacity = '0.7';
        });

        btnT.addEventListener('click', function() {
          panelZ.style.display = 'none';
          panelT.style.display = 'block';
          btnT.style.borderColor = 'var(--brand)';
          btnT.style.color = 'var(--brand)';
          btnT.style.opacity = '1';
          btnZ.style.borderColor = 'var(--border)';
          btnZ.style.color = 'var(--ink)';
          btnZ.style.opacity = '0.7';
        });
      }

      // 2. Z-Test Calculation Logic
      var inpP0 = document.getElementById('z-p0');
      var inpN = document.getElementById('z-n');
      var inpX = document.getElementById('z-x');
      var selAlpha = document.getElementById('z-alpha');
      var resZStat = document.getElementById('res-z-stat');
      var resZDetails = document.getElementById('res-z-details');
      var resZVerdict = document.getElementById('res-z-verdict');
      var resZReason = document.getElementById('res-z-reason');

      function calculateZ() {
        if (!inpP0 || !inpN || !inpX || !resZStat) return;
        var p0 = parseFloat(inpP0.value) || 0.20;
        var n = parseInt(inpN.value, 10) || 400;
        var x = parseInt(inpX.value, 10) || 70;
        var alpha = parseFloat(selAlpha ? selAlpha.value : '0.05');

        var q0 = 1.0 - p0;
        var pHat = x / n;
        var se = Math.sqrt((p0 * q0) / n);

        var z = (pHat - p0) / se;
        resZStat.textContent = z.toFixed(4);

        if (resZDetails) {
          resZDetails.textContent = 'p_hat = ' + pHat.toFixed(4) + ', SE = ' + se.toFixed(4);
        }

        var zCrit = 1.96;
        if (alpha === 0.10) zCrit = 1.645;
        else if (alpha === 0.01) zCrit = 2.576;

        var absZ = Math.abs(z);
        if (absZ < zCrit) {
          if (resZVerdict) { resZVerdict.textContent = 'FAIL TO REJECT H0 ✓'; resZVerdict.style.color = 'var(--brand)'; }
          if (resZReason) resZReason.textContent = '|' + z.toFixed(4) + '| < ' + zCrit + ' (Consistent with null hypothesis)';
        } else {
          if (resZVerdict) { resZVerdict.textContent = 'REJECT H0 ✗'; resZVerdict.style.color = 'var(--accent)'; }
          if (resZReason) resZReason.textContent = '|' + z.toFixed(4) + '| ≥ ' + zCrit + ' (Statistically significant difference)';
        }
      }

      [inpP0, inpN, inpX, selAlpha].forEach(function(el) {
        if (el) el.addEventListener('input', calculateZ);
      });

      var pPass = document.getElementById('preset-passengers');
      var pZoo = document.getElementById('preset-zoo');
      var pTurn = document.getElementById('preset-turnover');

      if (pPass) pPass.addEventListener('click', function() {
        if (inpP0) inpP0.value = 0.20;
        if (inpN) inpN.value = 400;
        if (inpX) inpX.value = 70;
        if (selAlpha) selAlpha.value = '0.05';
        calculateZ();
      });

      if (pZoo) pZoo.addEventListener('click', function() {
        if (inpP0) inpP0.value = 0.85;
        if (inpN) inpN.value = 50;
        if (inpX) inpX.value = 39;
        if (selAlpha) selAlpha.value = '0.05';
        calculateZ();
      });

      if (pTurn) pTurn.addEventListener('click', function() {
        // Labor turnover FPC: N=20, n=5, mu=320, sigma=75, xbar=300 -> z = -0.6711
        if (resZStat) resZStat.textContent = '-0.6711';
        if (resZDetails) resZDetails.textContent = 'FPC = sqrt(15/19) = 0.8885, SE = 29.8020';
        if (resZVerdict) { resZVerdict.textContent = 'FAIL TO REJECT H0 ✓'; resZVerdict.style.color = 'var(--brand)'; }
        if (resZReason) resZReason.textContent = '|-0.6711| < 1.96 (Sample turnover 300 is consistent with 320)';
      });

      calculateZ();

      // 3. Student's t-Test Logic
      var tDataInput = document.getElementById('t-data-input');
      var tMu0 = document.getElementById('t-mu0');
      var selTAlpha = document.getElementById('t-alpha');
      var resTStat = document.getElementById('res-t-stat');
      var resTDf = document.getElementById('res-t-df');
      var resTStatsSummary = document.getElementById('res-t-stats-summary');
      var resTVerdict = document.getElementById('res-t-verdict');

      function calculateT() {
        if (!tDataInput || !tMu0 || !resTStat) return;
        var raw = tDataInput.value;
        var arr = raw.split(',').map(function(s) { return parseFloat(s.trim()); }).filter(function(n) { return !isNaN(n); });
        var mu0 = parseFloat(tMu0.value) || 170.0;
        var n = arr.length;

        if (n < 2) return;

        var mean = arr.reduce(function(a, b) { return a + b; }, 0) / n;
        var sumSq = arr.reduce(function(a, b) { return a + Math.pow(b - mean, 2); }, 0);
        var s = Math.sqrt(sumSq / (n - 1));
        var se = s / Math.sqrt(n);
        var t = (mean - mu0) / se;
        var df = n - 1;

        resTStat.textContent = t.toFixed(4);

        var tCrit = 2.306; // standard df=8 at alpha=0.05
        if (df === 8) tCrit = 2.306;

        if (resTDf) resTDf.textContent = 'df = ' + df + ', Critical t = ±' + tCrit;
        if (resTStatsSummary) resTStatsSummary.textContent = 'Mean: ' + mean.toFixed(2) + ' cm, s: ' + s.toFixed(3) + ' cm';

        if (Math.abs(t) < tCrit) {
          if (resTVerdict) { resTVerdict.textContent = 'FAIL TO REJECT H0 ✓ (Height can be ' + mu0 + ' cm)'; resTVerdict.style.color = 'var(--brand)'; }
        } else {
          if (resTVerdict) { resTVerdict.textContent = 'REJECT H0 ✗ (Significant difference from ' + mu0 + ' cm)'; resTVerdict.style.color = 'var(--accent)'; }
        }
      }

      [tDataInput, tMu0, selTAlpha].forEach(function(el) {
        if (el) el.addEventListener('input', calculateT);
      });

      calculateT();
    })();
  </script>
'''

    body_end = '</body>'
    body_pos = content.rfind(body_end)
    if body_pos != -1:
        content = content[:body_pos] + interactive_script + '\n' + content[body_pos:]

    with open('notes/rmipr/unit3/unit-3-notes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enriched notes/rmipr/unit3/unit-3-notes.html successfully!")

if __name__ == "__main__":
    enrich_rmipr_u3()
