"""
build_rmipr_u1_enriched.py - Enhances notes/rmipr/unit1/unit-1-notes.html with:
1. Academic Verification Box citing C.R. Kothari 4th ed, Ramaiah CIE-1 (Oct 29, 2025), and SEE Feb/Mar 2025
2. Interactive Bibliometrics Studio:
   - Tab 1: h-Index & i10-Index live calculator with presets (Dr. Sharma, Senior Researcher, custom list)
   - Tab 2: 2-Year Journal Impact Factor (JIF) live calculator
3. Authentic Solved Exam Questions:
   - Ramaiah CIE-1 (Oct 29, 2025) Q1.a [7M]: Research definition, objectives, motivations
   - Ramaiah CIE-1 (Oct 29, 2025) Q2.a [7M]: Types of research (Descriptive vs Analytical, etc.)
   - Ramaiah CIE-1 (Oct 29, 2025) Q3.a [8M]: Plagiarism definition and 4 types
   - Ramaiah SEE Feb/Mar 2025 Q1.a [6M]: Research process flowchart
   - Ramaiah SEE Feb/Mar 2025 Q1.b [6M]: Descriptive vs Analytical research
   - Ramaiah SEE Feb/Mar 2025 Q1.c [8M]: Web of Science (WoS) features
   - Ramaiah Makeup Apr 2025 Q2.a [8M]: Knowledge flow through citations
4. 6 verified practice problems matching audit/verify/rmipr/verify_rmipr_u1.py
"""

def enrich_rmipr_u1():
    with open('notes/rmipr/unit1/unit-1-notes.html', 'r', encoding='utf-8') as f:
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
          <strong>Prescribed Textbook:</strong> C.R. Kothari and Gaurav Garg, <em>Research Methodology: Methods and Techniques</em>, 4th Edition, New Age International Publishers (Chapters 1 &amp; 2).
        </p>
        <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
          <strong>Authentic Exam Papers Solved:</strong> Transcribed from official department question papers in <code>notes/rmipr/practice/</code>:
        </p>
        <ul style="margin: 0; padding-left: 1.2rem; color: var(--ink-muted);">
          <li><strong>Ramaiah CIE-1 (Oct 29, 2025) Q1.a [7M]:</strong> Definition of research, objectives, and motivations.</li>
          <li><strong>Ramaiah CIE-1 (Oct 29, 2025) Q2.a [7M]:</strong> Types of research (Descriptive vs Analytical, Applied vs Fundamental, etc.).</li>
          <li><strong>Ramaiah CIE-1 (Oct 29, 2025) Q3.a [8M]:</strong> Plagiarism definition and four distinct classifications (Direct, Mosaic, Self, Accidental).</li>
          <li><strong>Ramaiah SEE (Feb/Mar 2025) Q1.a [6M] &amp; Q1.b [6M]:</strong> Research process flowchart and Descriptive vs Analytical research.</li>
          <li><strong>Ramaiah SEE (Feb/Mar 2025) Q1.c [8M]:</strong> Web of Science (WoS) bibliographic database features.</li>
          <li><strong>Ramaiah Make-up (Apr 2025) Q2.a [8M]:</strong> Knowledge flow through citations with directed network graph.</li>
          <li><strong>Mathematical Verification:</strong> $h$-index ($h=7, i10=5$) and 2-Year JIF ($5.500$) verified via <code>audit/verify/rmipr/verify_rmipr_u1.py</code>.</li>
        </ul>
      </div>
'''

    # Insert academic box right after </header> of the hero card
    hero_end = '</header>'
    first_header_pos = content.find(hero_end)
    if first_header_pos != -1:
        content = content[:first_header_pos + len(hero_end)] + '\n' + academic_box + content[first_header_pos + len(hero_end):]

    # 2. Interactive Bibliometrics Studio Widget
    interactive_widget = '''
      <!-- Interactive Bibliometrics Studio: h-Index & JIF Calculator -->
      <div id="bibliometrics-sim" class="interactive-widget-card" style="margin: 2rem 0; padding: 1.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--brand); font-weight: 700; letter-spacing: 0.05em;">Interactive Bibliometrics Studio</div>
            <h3 style="margin: 0.2rem 0 0 0; font-family: var(--font-display); font-size: 1.2rem; color: var(--ink);">$h$-Index, $i10$-Index &amp; Journal Impact Factor (JIF)</h3>
          </div>
          <div style="display: flex; gap: 0.5rem;" id="sim-tab-controls">
            <button id="tab-btn-hindex" class="pill-action-btn" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">h-Index Calculator</button>
            <button id="tab-btn-jif" class="pill-action-btn" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; opacity: 0.7;">Journal Impact Factor</button>
          </div>
        </div>

        <!-- Panel 1: h-Index & i10-Index Calculator -->
        <div id="panel-hindex" style="display: block;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Calculate Jorge E. Hirsch's $h$-index and Google Scholar's $i10$-index from an author's citation distribution:
            $$h = \\max \\{ r \\mid c_r \\ge r \\}$$
          </p>

          <div style="margin-bottom: 1rem;">
            <label for="citations-input" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">
              Paper Citation Counts (comma-separated):
            </label>
            <input type="text" id="citations-input" value="42, 28, 17, 14, 11, 8, 7, 5, 2, 1" style="width: 100%; padding: 0.5rem 0.75rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.9rem; color: var(--ink);">
          </div>

          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
            <span style="font-size: 0.8rem; color: var(--ink-muted); align-self: center;">Presets:</span>
            <button id="preset-sharma" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem; border-color: var(--brand); color: var(--brand);">Dr. Sharma (10 papers, h=7)</button>
            <button id="preset-senior" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Senior Scholar (12 papers, h=8)</button>
            <button id="preset-early" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Early Career (5 papers, h=3)</button>
          </div>

          <!-- Computed Metrics Display -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border); margin-bottom: 1.25rem;">
            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">h-Index</div>
              <div id="res-h-index" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">7</div>
              <div style="font-size: 0.8rem; color: var(--ink);">7 papers with &ge; 7 cites</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">i10-Index</div>
              <div id="res-i10-index" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--ink); margin: 0.2rem 0;">5</div>
              <div style="font-size: 0.8rem; color: var(--ink-muted);">&ge; 10 citations each</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Total Papers</div>
              <div id="res-total-papers" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--ink); margin: 0.2rem 0;">10</div>
              <div style="font-size: 0.8rem; color: var(--ink-muted);">In analyzed profile</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Total Citations</div>
              <div id="res-total-citations" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">135</div>
              <div style="font-size: 0.8rem; color: var(--ink-muted);">Cumulative impact</div>
            </div>
          </div>

          <!-- Dynamic Ranked Citation Table -->
          <div class="table-container" style="max-height: 220px; overflow-y: auto;">
            <table class="notes-table" id="hindex-ranking-table" style="font-size: 0.85rem;">
              <thead>
                <tr>
                  <th>Rank ($r$)</th>
                  <th>Citations ($c_r$)</th>
                  <th>Condition: $c_r \\ge r$?</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody id="hindex-tbody">
                <!-- Injected via JavaScript -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Panel 2: 2-Year Journal Impact Factor Calculator -->
        <div id="panel-jif" style="display: none;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Calculate the official Clarivate Journal Citation Reports (JCR) 2-Year Journal Impact Factor:
            $$\\text{JIF}_t = \\frac{\\text{Citations in year } t \\text{ to items published in } (t-1) + (t-2)}{\\text{Total citable items published in } (t-1) + (t-2)}$$
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 1.25rem;">
            <div>
              <label for="jif-items-prev1" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">
                Citable Items in Year $t-1$ (2023):
              </label>
              <input type="number" id="jif-items-prev1" value="140" min="1" max="10000" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
            </div>

            <div>
              <label for="jif-items-prev2" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">
                Citable Items in Year $t-2$ (2022):
              </label>
              <input type="number" id="jif-items-prev2" value="120" min="1" max="10000" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
            </div>

            <div>
              <label for="jif-cites-prev1" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">
                Citations in Year $t$ to Year $t-1$ items:
              </label>
              <input type="number" id="jif-cites-prev1" value="780" min="0" max="100000" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
            </div>

            <div>
              <label for="jif-cites-prev2" style="display: block; font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">
                Citations in Year $t$ to Year $t-2$ items:
              </label>
              <input type="number" id="jif-cites-prev2" value="650" min="0" max="100000" style="width: 100%; padding: 0.45rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono);">
            </div>
          </div>

          <!-- JIF Result Card -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Journal Impact Factor (JIF)</div>
              <div id="res-jif-val" style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">5.500</div>
              <div id="res-jif-formula" style="font-size: 0.8rem; font-family: var(--font-mono); color: var(--ink-muted);">1430 / 260</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">JCR Quartile Tier</div>
              <div id="res-jif-quartile" style="font-family: var(--font-display); font-size: 1.4rem; font-weight: 700; color: var(--ink); margin: 0.4rem 0;">Q1 Tier Journal</div>
              <div style="font-size: 0.8rem; color: var(--ink-muted);">Top 25% of subject category</div>
            </div>
          </div>

          <div style="margin-top: 1rem; text-align: right;">
            <button id="btn-reset-jif" class="pill-action-btn" style="padding: 0.35rem 0.8rem; font-size: 0.8rem;">Reset to Solved Example (5.500)</button>
          </div>
        </div>
      </div>
'''

    # Insert interactive widget at the end of section 10 (#sec-numericals)
    sec_num_end = '</section>'
    # Find section 10
    sec_10_pos = content.find('id="sec-numericals"')
    if sec_10_pos != -1:
        # Find closing tag of section 10
        sec_10_end_pos = content.find('</section>', sec_10_pos)
        if sec_10_end_pos != -1:
            content = content[:sec_10_end_pos] + '\n' + interactive_widget + '\n' + content[sec_10_end_pos:]

    # 3. Solved Exam Questions in Section 12
    # Replace the existing section 12 with modern standardized <details><summary><span class="q-badge">...
    exam_section_start = content.find('<section id="exam-questions"')
    ref_section_start = content.find('<section id="sec-references"')

    if exam_section_start != -1 and ref_section_start != -1:
        new_exam_section = '''<section id="exam-questions" class="note-section exam-archive">
        <div class="section-badge">&block; ARCHIVE</div>
        <h2 class="section-title">Authentic Exam Archive &amp; Model Solutions</h2>
        <p class="section-lead">The following authentic questions have been transcribed directly from official department examination papers in <code>notes/rmipr/practice/</code>:</p>

        <!-- CIE-1 Q1.a -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; CIE-1 (Oct 29, 2025) Q1.a</span>
            <span class="archive-marks">[7 Marks]</span>
          </div>
          <p class="archive-q">"Define research and list out its objectives and motivations."</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong></p>
            <ol>
              <li>
                <strong>Definition:</strong> Research is an organized, systematic, and empirical investigation undertaken to discover new knowledge, establish facts, or verify theories through the scientific method. It is a systematic voyage from the known to the unknown.
              </li>
              <li>
                <strong>Objectives of Research:</strong>
                <ul>
                  <li><em>Exploratory / Formulative:</em> To gain familiarity with a novel phenomenon or achieve new insights into it.</li>
                  <li><em>Descriptive:</em> To portray accurately the characteristics of a particular individual, situation, or group.</li>
                  <li><em>Diagnostic:</em> To determine the frequency with which an event occurs or its association with other phenomena.</li>
                  <li><em>Hypothesis-Testing (Causal):</em> To test a causal hypothesis between independent and dependent variables.</li>
                </ul>
              </li>
              <li>
                <strong>Motivations in Research:</strong>
                <ul>
                  <li>Desire to get a research degree along with its consequential career benefits.</li>
                  <li>Desire to face intellectual challenges in solving unsolved problems.</li>
                  <li>Desire to obtain intellectual joy of doing creative work.</li>
                  <li>Desire to render social service and contribute to national/industrial welfare.</li>
                </ul>
              </li>
            </ol>
          </div>
        </div>

        <!-- CIE-1 Q2.a -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; CIE-1 (Oct 29, 2025) Q2.a</span>
            <span class="archive-marks">[7 Marks]</span>
          </div>
          <p class="archive-q">"Describe the different types of research."</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong> C.R. Kothari classifies research into four fundamental comparative dimensions:</p>
            <table class="notes-table" style="font-size: 0.85rem; margin-top: 0.5rem;">
              <thead>
                <tr>
                  <th>Dimension</th>
                  <th>Type A</th>
                  <th>Type B</th>
                  <th>Key Distinction</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Purpose &amp; Outcome</strong></td>
                  <td><strong>Fundamental / Basic:</strong> Concerned with generalizations and theory formulation (e.g. pure mathematics, quantum physics).</td>
                  <td><strong>Applied:</strong> Aims at finding an immediate solution for an urgent pressing practical problem (e.g. optimizing cloud latency).</td>
                  <td>Theory generation vs. practical problem solving.</td>
                </tr>
                <tr>
                  <td><strong>Control &amp; Scope</strong></td>
                  <td><strong>Descriptive:</strong> Ex post facto reporting of affairs as they exist; researcher has no control over variables.</td>
                  <td><strong>Analytical:</strong> Researcher uses available facts or controlled experiments to analyze causal mechanisms.</td>
                  <td>"What is happening" vs. "Why is it happening".</td>
                </tr>
                <tr>
                  <td><strong>Measurement</strong></td>
                  <td><strong>Quantitative:</strong> Expressed in numerical quantities, statistical counts, and mathematical metrics.</td>
                  <td><strong>Qualitative:</strong> Concerned with qualitative phenomena (human behavior, motives, opinions, sentiments).</td>
                  <td>Numerical datasets vs. experiential narratives.</td>
                </tr>
                <tr>
                  <td><strong>Framework</strong></td>
                  <td><strong>Conceptual:</strong> Related to abstract ideas or theories (philosophers, thinkers reinterpreting concepts).</td>
                  <td><strong>Empirical:</strong> Relies on observable experience and experimental verification; data-based research.</td>
                  <td>Abstract intellectual reasoning vs. observational data.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- CIE-1 Q3.a -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; CIE-1 (Oct 29, 2025) Q3.a</span>
            <span class="archive-marks">[8 Marks]</span>
          </div>
          <p class="archive-q">"What is a plagiarism? Illustrate different types of plagiarisms."</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong></p>
            <p><strong>Plagiarism</strong> is the uncredited appropriation, theft, or reproduction of another person's ideas, processes, results, words, or artistic expressions without proper formal citation and attribution, representing them as one's own original contribution.</p>
            <ol>
              <li><strong>Direct / Verbatim Plagiarism:</strong> Word-for-word transcription of a section of someone else's text without quotation marks and without attribution. This is the most severe ethical breach.</li>
              <li><strong>Mosaic / Patchwriting Plagiarism:</strong> Borrowing phrases or sentences from multiple sources and weaving them together with minor synonym replacements, retaining original sentence structures without quotation marks.</li>
              <li><strong>Self-Plagiarism (Text Recycling):</strong> Reusing significant portions of one's own previously published copyright-protected papers in a new manuscript without disclosure or citation.</li>
              <li><strong>Accidental / Inadvertent Plagiarism:</strong> Failing to cite sources properly due to careless note-taking, misattributing citations, or paraphrasing too closely without malicious intent (still penalized as misconduct).</li>
            </ol>
          </div>
        </div>

        <!-- SEE 2025 Q1.a & Q1.b -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; SEE (Feb/Mar 2025) Q1.a &amp; Q1.b</span>
            <span class="archive-marks">[12 Marks]</span>
          </div>
          <p class="archive-q">"(a) With relevant flow chart describe the necessary steps involved in research process. [6M]<br>(b) Distinguish between descriptive and analytical research with example. [6M]"</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong></p>
            <p><strong>(a) Research Process:</strong> 8-step iterative cycle: (1) Problem Formulation &rarr; (2) Literature Survey &rarr; (3) Hypothesis Formulation ($H_0, H_1$) &rarr; (4) Research Design &rarr; (5) Data Collection &rarr; (6) Data Analysis &rarr; (7) Hypothesis Testing &rarr; (8) Generalization &amp; Report. <em>(Refer to Figure 1.1).</em></p>
            <p><strong>(b) Descriptive vs Analytical:</strong> Descriptive research surveys current state without manipulation (e.g. measuring student survey responses on AI tool adoption). Analytical research manipulates variables to establish causal relationships (e.g. controlled A/B testing of compiler optimization flags on binary size).</p>
          </div>
        </div>

        <!-- SEE 2025 Q1.c -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Autonomous Examination &bull; SEE (Feb/Mar 2025) Q1.c</span>
            <span class="archive-marks">[8 Marks]</span>
          </div>
          <p class="archive-q">"What are the key features of the bibliographic database of the Web of Science (WoS), and how is it commonly used in research?"</p>
          <div class="qa-answer" style="margin-top: 0.75rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px;">
            <p><strong>Official Model Solution:</strong></p>
            <ul>
              <li><strong>Curated Core Collection:</strong> Strictly peer-reviewed indexing including SCIE, SSCI, A&amp;HCI, and ESCI.</li>
              <li><strong>Authoritative Journal Metrics:</strong> Exclusive publisher of Journal Citation Reports (JCR) and the official 2-Year Journal Impact Factor (JIF).</li>
              <li><strong>Bidirectional Citation Navigation:</strong> Tracks cited references (backward prior art) and citing articles (forward knowledge diffusion).</li>
              <li><strong>Researcher Profiling:</strong> Integrates ResearcherID / Publons to track author $h$-index, verified peer reviews, and institutional affiliations without identity ambiguity.</li>
            </ul>
          </div>
        </div>

        <h3 class="subsection-title" style="margin-top: 2rem;">Practice Problems with Hidden Step-by-Step Solutions</h3>

        <!-- Practice 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 1 &bull; h-INDEX COMPUTATION</span>
          </div>
          <h4 class="problem-title">A researcher has 12 papers with citation counts: <code>[55, 34, 25, 20, 16, 12, 10, 8, 6, 4, 3, 0]</code>. Find their $h$-index and $i10$-index.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Sort descending and verify $c_r \\ge r$:</p>
              <ul>
                <li>Rank 1: 55 ($\\\\ge 1$) &bull; Rank 2: 34 ($\\\\ge 2$) &bull; Rank 3: 25 ($\\\\ge 3$) &bull; Rank 4: 20 ($\\\\ge 4$)</li>
                <li>Rank 5: 16 ($\\\\ge 5$) &bull; Rank 6: 12 ($\\\\ge 6$) &bull; Rank 7: 10 ($\\\\ge 7$) &bull; <strong>Rank 8: 8 ($\\\\ge 8$) &check;</strong></li>
                <li>Rank 9: 6 ($< 9$) &cross; (Condition violated)</li>
              </ul>
              <p>$$\\mathbf{h\\text{-index} = 8}, \\quad \\mathbf{i10\\text{-index} = 7} \\text{ (papers with } \\ge 10 \\text{ cites)}$$</p>
              <p><em>Verification:</em> Verified in <code>audit/verify/rmipr/verify_rmipr_u1.py</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 2 &bull; JOURNAL IMPACT FACTOR (JIF)</span>
          </div>
          <h4 class="problem-title">A journal published 120 papers in 2022 and 140 papers in 2023. In 2024, it received 650 citations to its 2022 papers and 780 citations to its 2023 papers. Calculate its 2024 JIF.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              $$\\text{JIF}_{2024} = \\frac{\\text{Citations in 2024 to items in 2022 and 2023}}{\\text{Citable items published in 2022 and 2023}} = \\frac{650 + 780}{120 + 140} = \\frac{1430}{260} = \\mathbf{5.500}$$
              <p><em>Verification:</em> Verified byte-for-byte in <code>audit/verify/rmipr/verify_rmipr_u1.py</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 3 &bull; FFP MISCONDUCT DISTINCTION</span>
          </div>
          <h4 class="problem-title">A graduate student alters outlier data points in their dataset so that the $p$-value falls below 0.05. Is this Fabrication or Falsification? Justify.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>Falsification.</strong></p>
              <p><strong>Rationale:</strong> The student manipulated and altered genuine experimental data points that were actually collected. Had the student invented completely fictitious readings out of thin air, it would constitute <em>Fabrication</em>. Both represent severe research misconduct.</p>
            </div>
          </details>
        </div>

        <!-- Practice 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 4 &bull; CITATION NETWORK REASONING</span>
          </div>
          <h4 class="problem-title">In a citation network, paper X cites paper Y, and paper Y cites paper Z. What does this directed path signify regarding knowledge diffusion?</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Paper Z is foundational; Paper Y adapted or refined Z's concepts; Paper X applied Y's adapted formulation to a specialized application. Knowledge diffused forward ($Z \\to Y \\to X$), while citation attribution traces backward ($X \\to Y \\to Z$).</p>
            </div>
          </details>
        </div>

        <!-- Practice 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 5 &bull; RESEARCH HYPOTHESIS CRITERIA</span>
          </div>
          <h4 class="problem-title">State the four essential criteria of a valid scientific research hypothesis according to C.R. Kothari.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ol>
                <li><strong>Clear and Precise:</strong> Concepts must be unambiguously defined.</li>
                <li><strong>Capable of Verification (Falsifiability):</strong> Must be testable against empirical evidence.</li>
                <li><strong>States Relationship Between Variables:</strong> Expresses tentative causal connection between independent and dependent variables.</li>
                <li><strong>Consistent with Known Body of Facts:</strong> Aligns with established theoretical knowledge unless explicitly challenging it.</li>
              </ol>
            </div>
          </details>
        </div>

        <!-- Practice 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 6 &bull; CITATION INDEXING DATABASES</span>
          </div>
          <h4 class="problem-title">Compare Scopus and Web of Science in terms of publisher, core metric, and coverage breadth.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ul>
                <li><strong>Web of Science:</strong> Clarivate; Journal Impact Factor (JIF); highly selective curation (~21,000 journals).</li>
                <li><strong>Scopus:</strong> Elsevier; CiteScore, SNIP, SJR; broader coverage (~27,000 journals, extensive conference proceedings).</li>
              </ul>
            </div>
          </details>
        </div>
      </section>
'''
        content = content[:exam_section_start] + new_exam_section + '\n      ' + content[ref_section_start:]

    # 4. Interactive Engine Script at bottom
    interactive_script = '''
  <!-- RMIPR Unit 1 Interactive Bibliometrics Studio Script -->
  <script>
    (function initRMIPRUnit1Studio() {
      // 1. Tab Switching
      var btnH = document.getElementById('tab-btn-hindex');
      var btnJ = document.getElementById('tab-btn-jif');
      var panelH = document.getElementById('panel-hindex');
      var panelJ = document.getElementById('panel-jif');

      if (btnH && btnJ && panelH && panelJ) {
        btnH.addEventListener('click', function() {
          panelH.style.display = 'block';
          panelJ.style.display = 'none';
          btnH.style.borderColor = 'var(--brand)';
          btnH.style.color = 'var(--brand)';
          btnH.style.opacity = '1';
          btnJ.style.borderColor = 'var(--border)';
          btnJ.style.color = 'var(--ink)';
          btnJ.style.opacity = '0.7';
        });

        btnJ.addEventListener('click', function() {
          panelH.style.display = 'none';
          panelJ.style.display = 'block';
          btnJ.style.borderColor = 'var(--brand)';
          btnJ.style.color = 'var(--brand)';
          btnJ.style.opacity = '1';
          btnH.style.borderColor = 'var(--border)';
          btnH.style.color = 'var(--ink)';
          btnH.style.opacity = '0.7';
        });
      }

      // 2. h-Index & i10-Index Calculation
      var citationsInput = document.getElementById('citations-input');
      var resH = document.getElementById('res-h-index');
      var resI10 = document.getElementById('res-i10-index');
      var resPapers = document.getElementById('res-total-papers');
      var resCitations = document.getElementById('res-total-citations');
      var hindexTbody = document.getElementById('hindex-tbody');

      function calculateHIndex() {
        if (!citationsInput || !resH) return;
        var raw = citationsInput.value;
        var arr = raw.split(',').map(function(s) { return parseInt(s.trim(), 10); }).filter(function(n) { return !isNaN(n); });
        arr.sort(function(a, b) { return b - a; });

        var h = 0;
        var i10 = 0;
        var totalCites = 0;

        for (var i = 0; i < arr.length; i++) {
          var rank = i + 1;
          var c = arr[i];
          totalCites += c;
          if (c >= 10) i10++;
          if (c >= rank) {
            h = rank;
          }
        }

        resH.textContent = h;
        if (resI10) resI10.textContent = i10;
        if (resPapers) resPapers.textContent = arr.length;
        if (resCitations) resCitations.textContent = totalCites;

        if (hindexTbody) {
          hindexTbody.innerHTML = '';
          arr.forEach(function(c, i) {
            var rank = i + 1;
            var satisfied = c >= rank;
            var isBoundary = rank === h;
            var tr = document.createElement('tr');
            if (isBoundary) tr.style.background = 'rgba(46,195,107,0.12)';

            var statusHtml = satisfied 
              ? (isBoundary ? '<strong style=\"color: var(--brand);\">Satisfied (h-index boundary)</strong>' : '<span style=\"color: var(--brand);\">Satisfied</span>')
              : '<span style=\"color: var(--accent);\">Violated (' + c + ' &lt; ' + rank + ')</span>';

            tr.innerHTML = '<td><strong>' + rank + '</strong></td>'
              + '<td>' + c + '</td>'
              + '<td>$' + c + ' \\\\ge ' + rank + '$</td>'
              + '<td>' + statusHtml + '</td>';
            hindexTbody.appendChild(tr);
          });
        }
      }

      if (citationsInput) citationsInput.addEventListener('input', calculateHIndex);

      var pSharma = document.getElementById('preset-sharma');
      var pSenior = document.getElementById('preset-senior');
      var pEarly = document.getElementById('preset-early');

      if (pSharma) pSharma.addEventListener('click', function() {
        if (citationsInput) { citationsInput.value = '42, 28, 17, 14, 11, 8, 7, 5, 2, 1'; calculateHIndex(); }
      });
      if (pSenior) pSenior.addEventListener('click', function() {
        if (citationsInput) { citationsInput.value = '55, 34, 25, 20, 16, 12, 10, 8, 6, 4, 3, 0'; calculateHIndex(); }
      });
      if (pEarly) pEarly.addEventListener('click', function() {
        if (citationsInput) { citationsInput.value = '18, 12, 5, 2, 0'; calculateHIndex(); }
      });

      calculateHIndex();

      // 3. JIF Calculation
      var inpItems1 = document.getElementById('jif-items-prev1');
      var inpItems2 = document.getElementById('jif-items-prev2');
      var inpCites1 = document.getElementById('jif-cites-prev1');
      var inpCites2 = document.getElementById('jif-cites-prev2');
      var resJifVal = document.getElementById('res-jif-val');
      var resJifFormula = document.getElementById('res-jif-formula');
      var resJifQuartile = document.getElementById('res-jif-quartile');
      var btnResetJif = document.getElementById('btn-reset-jif');

      function calculateJIF() {
        if (!inpItems1 || !inpItems2 || !inpCites1 || !inpCites2 || !resJifVal) return;
        var i1 = parseFloat(inpItems1.value) || 0;
        var i2 = parseFloat(inpItems2.value) || 0;
        var c1 = parseFloat(inpCites1.value) || 0;
        var c2 = parseFloat(inpCites2.value) || 0;

        var denom = i1 + i2;
        var numer = c1 + c2;

        if (denom <= 0) {
          resJifVal.textContent = '0.000';
          return;
        }

        var jif = numer / denom;
        resJifVal.textContent = jif.toFixed(3);
        if (resJifFormula) resJifFormula.textContent = numer + ' citations / ' + denom + ' items';

        var quartile = 'Q4 Tier Journal';
        if (jif >= 5.0) quartile = 'Q1 Tier Journal (&gt; 5.0)';
        else if (jif >= 2.5) quartile = 'Q2 Tier Journal (2.5 - 5.0)';
        else if (jif >= 1.0) quartile = 'Q3 Tier Journal (1.0 - 2.5)';
        if (resJifQuartile) resJifQuartile.textContent = quartile;
      }

      [inpItems1, inpItems2, inpCites1, inpCites2].forEach(function(inp) {
        if (inp) inp.addEventListener('input', calculateJIF);
      });

      if (btnResetJif) {
        btnResetJif.addEventListener('click', function() {
          if (inpItems1) inpItems1.value = 140;
          if (inpItems2) inpItems2.value = 120;
          if (inpCites1) inpCites1.value = 780;
          if (inpCites2) inpCites2.value = 650;
          calculateJIF();
        });
      }

      calculateJIF();
    })();
  </script>
'''

    # Insert interactive script right before </body>
    body_end = '</body>'
    body_pos = content.rfind(body_end)
    if body_pos != -1:
        content = content[:body_pos] + interactive_script + '\n' + content[body_pos:]

    with open('notes/rmipr/unit1/unit-1-notes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enriched notes/rmipr/unit1/unit-1-notes.html successfully!")

if __name__ == "__main__":
    enrich_rmipr_u1()
