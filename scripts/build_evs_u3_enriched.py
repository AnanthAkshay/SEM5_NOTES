"""
build_evs_u3_enriched.py - Enriches notes/evs/unit3/unit-3-notes.html with:
1. Academic Verification Box citing Erach Bharucha, Benny Joseph, and HS510 Syllabus
2. Interactive Ecological Diversity Index Studio:
   - Tab 1: Simpson's Diversity Index Calculator (D and 1 - D, live inputs, presets, dynamic step table)
   - Tab 2: Shannon-Wiener Index (H') & Pielou's Evenness (J') Calculator (H', H_max = ln(S), J' equitability)
3. Standardized Exam Archive & 6 Verified Practice Problems matching audit/verify/evs/verify_evs_u3.py
"""

import re

def enrich_evs_u3():
    with open('notes/evs/unit3/unit-3-notes.html', 'r', encoding='utf-8') as f:
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
            <strong>Prescribed References:</strong> Erach Bharucha, <em>Textbook of Environmental Studies for Undergraduate Courses</em>, Universities Press / UGC India (Chapter 4: Biodiversity); Benny Joseph, <em>Environmental Studies</em>, McGraw-Hill; R. Rajagopalan, <em>Environmental Studies: From Crisis to Cure</em>, Oxford University Press.
          </p>
          <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
            <strong>Curriculum &amp; Examination Scope:</strong> Course Code <strong>HS 510: Environmental Studies</strong>. Covers genetic, species, and community ($\alpha, \beta, \gamma$) diversity; 10 biogeographical zones of India; Norman Myers biodiversity hotspots (Western Ghats, Eastern Himalayas, Indo-Burma, Sundaland); the Evil Quartet threats to biodiversity; In-situ vs. Ex-situ conservation; and mathematical diversity metrics.
          </p>
          <p style="margin: 0; color: var(--ink-muted); font-size: 0.88rem;">
            <strong>Mathematical &amp; Code Verification:</strong> Simpson's Index of Diversity ($D = 0.2584, 1 - D = 0.7416, 1/D = 3.87$), Shannon-Wiener Diversity Index ($H' = 1.4541$), and species evenness ($J' = 0.9035$) verified via automated unit test suite (<code>audit/verify/evs/verify_evs_u3.py</code>).
          </p>
        </div>'''

    # Insert academic box right after source-links-card
    source_links_idx = content.find('</div>\n      </header>')
    if source_links_idx != -1:
        content = content[:source_links_idx + 6] + '\n' + academic_box + content[source_links_idx + 6:]
    else:
        header_end = '</header>'
        pos = content.find(header_end)
        if pos != -1:
            content = content[:pos] + academic_box + '\n      ' + content[pos:]

    # 2. Interactive Widget
    interactive_widget = '''
      <!-- Interactive Ecological Diversity Index Studio -->
      <div id="evs-diversity-studio" class="interactive-widget-card" style="margin: 2.5rem 0; padding: 1.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--brand); font-weight: 700; letter-spacing: 0.05em;">Interactive Lab Explorer</div>
            <h3 style="margin: 0.2rem 0 0 0; font-family: var(--font-display); font-size: 1.25rem; color: var(--ink);">Biodiversity Indices: Simpson's &amp; Shannon-Wiener Studio</h3>
          </div>
          <div style="display: flex; gap: 0.5rem;" id="diversity-tab-controls" role="tablist">
            <button id="tab-btn-simpson" class="pill-action-btn" role="tab" aria-selected="true" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">Tab 1: Simpson's Diversity (1 - D)</button>
            <button id="tab-btn-shannon" class="pill-action-btn" role="tab" aria-selected="false" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; opacity: 0.7;">Tab 2: Shannon-Wiener (H') &amp; Evenness (J')</button>
          </div>
        </div>

        <!-- Panel 1: Simpson's Index Calculator -->
        <div id="panel-simpson" role="tabpanel" style="display: block;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Calculate Simpson's Index of Dominance ($D$) and Simpson's Index of Diversity ($1 - D$):
            $$D = \\frac{\\sum n_i(n_i - 1)}{N(N - 1)}, \\quad \\text{Diversity} = 1 - D$$
          </p>

          <!-- Presets -->
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
            <span style="font-size: 0.8rem; color: var(--ink-muted); align-self: center;">Community Presets:</span>
            <button id="preset-forest-a" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem; border-color: var(--brand); color: var(--brand);">Forest Community A (40, 25, 15, 12, 8 - Solved)</button>
            <button id="preset-equitable" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Equitable Canopy (20, 20, 20, 20, 20)</button>
            <button id="preset-monoculture" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Disturbed Monoculture (90, 4, 3, 2, 1)</button>
          </div>

          <div style="margin-bottom: 1rem;">
            <label for="input-species-counts" style="display: block; font-family: var(--font-mono); font-size: 0.82rem; color: var(--ink); margin-bottom: 0.35rem;">
              Species Abundance Counts (comma-separated):
            </label>
            <input type="text" id="input-species-counts" value="40, 25, 15, 12, 8" style="width: 100%; padding: 0.5rem 0.75rem; background: var(--surface-alt); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.9rem; color: var(--ink);">
          </div>

          <!-- Computed Metrics Grid -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border); margin-bottom: 1.25rem;">
            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Total Individuals ($N$)</div>
              <div id="res-total-n" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--ink); margin: 0.2rem 0;">100</div>
              <div id="res-total-s" style="font-size: 0.78rem; color: var(--ink-muted);">Species Richness $S = 5$</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Dominance ($D$)</div>
              <div id="res-simpson-d" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--ink); margin: 0.2rem 0;">0.2584</div>
              <div id="res-d-ratio" style="font-size: 0.78rem; font-family: var(--font-mono); color: var(--ink-muted);">2558 / 9900</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Diversity ($1 - D$)</div>
              <div id="res-simpson-1minusd" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">0.7416</div>
              <div style="font-size: 0.78rem; color: var(--ink-muted);">74.16% diversity chance</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Reciprocal ($1 / D$)</div>
              <div id="res-simpson-reciprocal" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">3.870</div>
              <div style="font-size: 0.78rem; color: var(--ink-muted);">Effective species</div>
            </div>
          </div>

          <!-- Dynamic Species Breakdown Table -->
          <div class="table-container" style="max-height: 200px; overflow-y: auto;">
            <table class="notes-table" style="font-size: 0.85rem;">
              <thead>
                <tr>
                  <th>Species Tag</th>
                  <th>Abundance ($n_i$)</th>
                  <th>Proportion ($p_i$)</th>
                  <th>$n_i(n_i - 1)$</th>
                  <th>Contribution</th>
                </tr>
              </thead>
              <tbody id="simpson-breakdown-tbody">
                <!-- Injected via JavaScript -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Panel 2: Shannon-Wiener Calculator -->
        <div id="panel-shannon" role="tabpanel" style="display: none;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Calculate the Shannon-Wiener Diversity Index ($H'$) and Pielou's Species Evenness ($J'$):
            $$H' = -\\sum_{i=1}^S p_i \\ln(p_i), \\quad J' = \\frac{H'}{\\ln(S)}$$
          </p>

          <!-- Computed Metrics Grid -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border); margin-bottom: 1.25rem;">
            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Shannon Index ($H'$)</div>
              <div id="res-shannon-h" style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">1.4541</div>
              <div style="font-size: 0.78rem; color: var(--ink-muted);">Typical biological range: 1.5 - 3.5</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Max Diversity ($H_{\\text{max}} = \\ln(S)$)</div>
              <div id="res-shannon-hmax" style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--ink); margin: 0.2rem 0;">1.6094</div>
              <div style="font-size: 0.78rem; color: var(--ink-muted);">$\\ln(5) = 1.6094$</div>
            </div>

            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Pielou's Evenness ($J'$)</div>
              <div id="res-shannon-j" style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--brand); margin: 0.2rem 0;">0.9035</div>
              <div style="font-size: 0.78rem; color: var(--ink-muted);">90.35% equitable canopy distribution</div>
            </div>
          </div>

          <div style="padding: 0.75rem 1rem; background: var(--surface-alt); border-radius: 6px; border: 1px dashed var(--brand); font-size: 0.85rem; color: var(--ink);">
            <strong>Ecological Takeaway:</strong> High evenness ($J' = 0.9035$) proves that individuals are well apportioned across all 5 species without any single taxon totally overwhelming the forest canopy.
          </div>
        </div>
      </div>
'''

    # Insert interactive widget at the end of Section 9 (#sec-numericals)
    sec_9_pos = content.find('id="sec-numericals"')
    if sec_9_pos != -1:
        sec_9_end = content.find('</section>', sec_9_pos)
        if sec_9_end != -1:
            content = content[:sec_9_end] + '\n' + interactive_widget + '\n' + content[sec_9_end:]

    # 3. Standardize and enrich Section 11 with authentic questions and verified practice problems
    exam_start = content.find('<section id="exam-questions"')
    ref_start = content.find('<section id="sec-references"')

    if exam_start != -1 and ref_start != -1:
        new_exam_section = '''<section id="exam-questions" class="content-section exam-archive">
        <h2 class="section-title">11. Authentic Exam Archive &amp; Model Solutions</h2>
        <p class="section-lead">The following conceptual questions and verified diversity metric calculations cover key university examination patterns for <strong>HS 510: Environmental Studies</strong>:</p>

        <h3 class="subsection-title">2-Mark Conceptual Questions</h3>

        <!-- Q1 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">1. Define the term 'Endemic Species' with an authentic example from India.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p><strong>Endemic Species</strong> are plants or animals whose natural wild geographic distribution is strictly confined to a specific geographic region or habitat, and found nowhere else globally.</p>
            <p><strong>Authentic Indian Example:</strong> The <strong>Lion-tailed Macaque</strong> (<em>Macaca silenus</em>) and the <strong>Nilgiri Tahr</strong> (<em>Nilgiritragus hylocrius</em>), both endemic exclusively to the tropical evergreen rainforests of the Western Ghats.</p>
          </div>
        </details>

        <!-- Q2 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">2. State the two essential criteria proposed by Norman Myers to designate a global Biodiversity Hotspot.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ol>
              <li><strong>High Endemism Criterion:</strong> The region must contain at least <strong>1,500 species of endemic vascular plants</strong> ($>0.5\\%$ of the world's total plant species).</li>
              <li><strong>High Threat / Habitat Loss Criterion:</strong> The region must have lost at least <strong>$70\\%$ of its original native primary vegetation</strong> (i.e., retaining $\\le 30\\%$ of its pristine natural habitat).</li>
            </ol>
          </div>
        </details>

        <!-- Q3 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">3. What are the four global Biodiversity Hotspots that cover regions of India?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ol>
              <li><strong>Western Ghats and Sri Lanka</strong> (Southwestern India).</li>
              <li><strong>Eastern Himalayas</strong> (Covering Arunachal Pradesh, Sikkim, and adjacent sub-Himalayan tracts).</li>
              <li><strong>Indo-Burma</strong> (Covering North-Eastern states including Manipur, Mizoram, Nagaland).</li>
              <li><strong>Sundaland</strong> (Covering the Nicobar Islands group).</li>
            </ol>
          </div>
        </details>

        <!-- Q4 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">4. Differentiate between Alpha, Beta, and Gamma diversity in landscape ecology.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ul>
              <li><strong>Alpha ($\\alpha$) Diversity:</strong> Species diversity within a particular local community or single habitat.</li>
              <li><strong>Beta ($\\beta$) Diversity:</strong> The rate of species turnover between two distinct adjacent communities or habitats along an environmental gradient.</li>
              <li><strong>Gamma ($\\gamma$) Diversity:</strong> The overall total species richness across an entire landscape, biome, or geographic region ($\gamma = \alpha \times \beta$).</li>
            </ul>
          </div>
        </details>

        <h3 class="subsection-title">5-Mark &amp; 10-Mark Model Questions</h3>

        <!-- Q5 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">10 MARKS</span>
            <span class="q-title">5. Differentiate comprehensively between In-Situ and Ex-Situ conservation strategies.</span>
          </summary>
          <div class="qa-answer">
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr>
                    <th>Dimension</th>
                    <th>In-Situ Conservation (On-Site)</th>
                    <th>Ex-Situ Conservation (Off-Site)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Definition</strong></td>
                    <td>Conservation of species within their natural native habitats where evolutionary processes continue.</td>
                    <td>Conservation of endangered organisms in artificial, human-controlled environments outside native habitats.</td>
                  </tr>
                  <tr>
                    <td><strong>Examples</strong></td>
                    <td>National Parks (Bandipur, Kaziranga), Wildlife Sanctuaries, Biosphere Reserves (Nilgiri), Sacred Groves.</td>
                    <td>Zoological Parks, Botanical Gardens, Seed Banks (NBPGR, New Delhi), Cryopreservation facilities.</td>
                  </tr>
                  <tr>
                    <td><strong>Human Intervention</strong></td>
                    <td>Minimal; National Parks prohibit all human settlement, grazing, and resource extraction.</td>
                    <td>Intensive; organisms depend upon artificial feeding, veterinary care, and controlled temperature regimes.</td>
                  </tr>
                  <tr>
                    <td><strong>Evolutionary Value</strong></td>
                    <td>High; populations continue natural adaptation, predator-prey dynamics, and speciation.</td>
                    <td>Low; natural selection halted; vulnerability to genetic bottlenecks and inbreeding depression.</td>
                  </tr>
                  <tr>
                    <td><strong>Scope &amp; Cost</strong></td>
                    <td>Protects entire ecosystems, thousands of species, and trophic pyramids cost-effectively.</td>
                    <td>Focuses on select high-profile endangered taxa; requires high capital and maintenance expenditures.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </details>

        <!-- Q6 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">8 MARKS</span>
            <span class="q-title">6. Explain the four major drivers of biodiversity loss under Edward O. Wilson's 'Evil Quartet'.</span>
          </summary>
          <div class="qa-answer">
            <ol>
              <li><strong>Habitat Loss &amp; Fragmentation (Primary Cause):</strong> Clearing pristine tropical rainforests for commercial monocultures (palm oil, soy) and infrastructure fractures contiguous habitats into tiny isolated forest islands, causing edge effects and local population extinctions.</li>
              <li><strong>Over-Exploitation:</strong> Excessive harvesting exceeding biological reproduction rates. Driven by greed rather than need (e.g. historical extinction of the Passenger Pigeon, Steller's Sea Cow, and poaching of One-horned Rhinos for horn keratin).</li>
              <li><strong>Invasion of Alien Species:</strong> Accidental or intentional introduction of non-native exotic species that aggressively outcompete native taxa. Examples: <em>Parthenium hysterophorus</em> (congress grass), <em>Lantana camara</em>, and <em>Eichhornia crassipes</em> (water hyacinth / "Terror of Bengal") choking aquatic ecosystems.</li>
              <li><strong>Co-Extinctions:</strong> When an obligate mutualistic relationship exists, the extinction of a host species unavoidably triggers the co-extinction of its obligate pollinator or parasite (e.g. co-evolved fig-wasp mutualisms).</li>
            </ol>
          </div>
        </details>

        <h3 class="subsection-title">Verified Numerical &amp; Computational Practice Problems</h3>

        <!-- Practice 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 1 &bull; SIMPSON'S INDEX OF DIVERSITY</span>
          </div>
          <h4 class="problem-title">A sample of 100 trees from a forest plot contains 5 species with abundances: 40, 25, 15, 12, and 8. Calculate Simpson's Index ($D$), Simpson's Index of Diversity ($1 - D$), and Reciprocal Index ($1/D$).</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ol>
                <li>Total individuals: $N = 40 + 25 + 15 + 12 + 8 = 100$.</li>
                <li>Denominator: $N(N - 1) = 100 \times 99 = 9,900$.</li>
                <li>Numerator: $\sum n_i(n_i - 1) = (40 \times 39) + (25 \times 24) + (15 \times 14) + (12 \times 11) + (8 \times 7) = 1560 + 600 + 210 + 132 + 56 = \mathbf{2,558}$.</li>
                <li>Simpson's Dominance: $D = \frac{2,558}{9,900} \approx \mathbf{0.2584}$.</li>
                <li><strong>Simpson's Diversity:</strong> $1 - D = 1 - 0.2584 = \mathbf{0.7416}$.</li>
                <li><strong>Reciprocal Index:</strong> $\frac{1}{D} = \frac{1}{0.2584} \approx \mathbf{3.870}$.</li>
              </ol>
              <p><em>Verification:</em> Verified by automated unit test in <code>audit/verify/evs/verify_evs_u3.py</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 2 &bull; SHANNON-WIENER DIVERSITY &amp; EVENNESS</span>
          </div>
          <h4 class="problem-title">For the identical tree community ($N = 100, S = 5$, counts: $40, 25, 15, 12, 8$), calculate the Shannon-Wiener Diversity Index ($H'$) and Pielou's Evenness ($J'$).</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Proportions: $p_i = [0.40, 0.25, 0.15, 0.12, 0.08]$</p>
              <ul>
                <li>$0.40 \ln(0.40) = 0.40 \times (-0.9163) = -0.3665$</li>
                <li>$0.25 \ln(0.25) = 0.25 \times (-1.3863) = -0.3466$</li>
                <li>$0.15 \ln(0.15) = 0.15 \times (-1.8971) = -0.2846$</li>
                <li>$0.12 \ln(0.12) = 0.12 \times (-2.1203) = -0.2544$</li>
                <li>$0.08 \ln(0.08) = 0.08 \times (-2.5257) = -0.2021$</li>
                <li>Sum $= -1.4541 \implies \mathbf{H' = 1.4541}$.</li>
              </ul>
              <p>Maximum possible diversity: $H_{\text{max}} = \ln(S) = \ln(5) = \mathbf{1.6094}$.</p>
              <p><strong>Species Evenness:</strong> $J' = \frac{H'}{H_{\text{max}}} = \frac{1.4541}{1.6094} \approx \mathbf{0.9035}$ (90.35% equitable distribution).</p>
              <p><em>Verification:</em> Verified by automated unit test in <code>audit/verify/evs/verify_evs_u3.py</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 3 &bull; THEORETICAL MAXIMUM DIVERSITY</span>
          </div>
          <h4 class="problem-title">Under what ecological condition does Shannon-Wiener Diversity ($H'$) reach its absolute theoretical maximum $H_{\text{max}}$?</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Shannon-Wiener diversity reaches $H_{\text{max}} = \ln(S)$ when all $S$ species have <strong>strictly equal abundances</strong> (i.e. $p_i = \frac{1}{S}$ for all $i$). Under this condition, Pielou's evenness $J' = \frac{\ln(S)}{\ln(S)} = \mathbf{1.00}$ (100% perfect community equitability).</p>
            </div>
          </details>
        </div>

        <!-- Practice 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 4 &bull; CRYOPRESERVATION MECHANISMS</span>
          </div>
          <h4 class="problem-title">Explain the thermodynamic principle and storage temperature utilized in cryopreservation for ex-situ biodiversity conservation.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Cryopreservation preserves plant germplasm (pollen, seeds, meristems) and animal gametes/embryos in <strong>liquid nitrogen at $-196^\circ\text{C}$ ($77\text{ K}$)</strong>.</p>
              <p><strong>Principle:</strong> At $-196^\circ\text{C}$, all chemical kinetic activity and cellular metabolic respiration cease completely. Biological tissues remain in metabolic suspended animation for decades to centuries without genetic degradation or senescence.</p>
            </div>
          </details>
        </div>

        <!-- Practice 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 5 &bull; BIOGEOGRAPHIC ZONES OF INDIA</span>
          </div>
          <h4 class="problem-title">Enumerate the 10 Biogeographic Zones of India designated by the Wildlife Institute of India (WII).</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ol>
                <li>1. Trans-Himalayan Zone (Ladakh, Lahaul-Spiti)</li>
                <li>2. Himalayan Zone (Northwest, West, Central, and East Himalayas)</li>
                <li>3. Desert Zone (Thar and Kutch)</li>
                <li>4. Semi-Arid Zone (Punjab plains to Gujarat)</li>
                <li>5. Western Ghats (Malabar plains and Sahyadri ranges)</li>
                <li>6. Deccan Peninsula (Central highlands, Chhota Nagpur, Eastern ghats)</li>
                <li>7. Gangetic Plain (Upper and Lower Gangetic alluvial plains)</li>
                <li>8. Coastal Zone (West and East coasts, Lakshadweep)</li>
                <li>9. North-East Zone (Brahmaputra valley and Assam hills)</li>
                <li>10. Islands (Andaman and Nicobar archipelago)</li>
              </ol>
            </div>
          </details>
        </div>

        <!-- Practice 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 6 &bull; INVASIVE ALIEN SPECIES (IAS) DISRUPTION</span>
          </div>
          <h4 class="problem-title">Describe how *Eichhornia crassipes* (Water Hyacinth) alters aquatic ecology and drives local extinctions.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><em>Eichhornia crassipes</em> (Water Hyacinth), introduced as an ornamental aquatic plant, forms dense impenetrable floating vegetative mats over freshwater lakes and rivers:</p>
              <ul>
                <li><strong>Sunlight Blockade:</strong> Blocks solar penetration, killing submerged photosynthesizing aquatic macrophytes and phytoplankton.</li>
                <li><strong>Dissolved Oxygen (DO) Depletion:</strong> High biomass decay exerts massive Biochemical Oxygen Demand (BOD), causing severe hypoxia/anoxia that asphyxiates native fish fauna.</li>
                <li><strong>Ecosystem Succession Acceleration:</strong> Accelerated sediment buildup converts open water bodies into shallow marshes prematurely.</li>
              </ul>
            </div>
          </details>
        </div>
      </section>'''
        content = content[:exam_start] + new_exam_section + '\n\n      ' + content[ref_start:]

    # 4. Interactive Studio JavaScript Engine
    widget_script = '''
  <!-- Interactive EVS Unit 3 Biodiversity Index Studio Engine -->
  <script>
  (function() {
    // Tab switching
    var tabSimpson = document.getElementById('tab-btn-simpson');
    var tabShannon = document.getElementById('tab-btn-shannon');
    var panelSimpson = document.getElementById('panel-simpson');
    var panelShannon = document.getElementById('panel-shannon');

    if (tabSimpson && tabShannon && panelSimpson && panelShannon) {
      tabSimpson.addEventListener('click', function() {
        tabSimpson.style.borderColor = 'var(--brand)';
        tabSimpson.style.color = 'var(--brand)';
        tabSimpson.style.opacity = '1';
        tabSimpson.setAttribute('aria-selected', 'true');

        tabShannon.style.borderColor = 'var(--border)';
        tabShannon.style.color = 'var(--ink)';
        tabShannon.style.opacity = '0.7';
        tabShannon.setAttribute('aria-selected', 'false');

        panelSimpson.style.display = 'block';
        panelShannon.style.display = 'none';
      });

      tabShannon.addEventListener('click', function() {
        tabShannon.style.borderColor = 'var(--brand)';
        tabShannon.style.color = 'var(--brand)';
        tabShannon.style.opacity = '1';
        tabShannon.setAttribute('aria-selected', 'true');

        tabSimpson.style.borderColor = 'var(--border)';
        tabSimpson.style.color = 'var(--ink)';
        tabSimpson.style.opacity = '0.7';
        tabSimpson.setAttribute('aria-selected', 'false');

        panelShannon.style.display = 'block';
        panelSimpson.style.display = 'none';
      });
    }

    // Interactive Engine
    var inpCounts = document.getElementById('input-species-counts');
    var outN = document.getElementById('res-total-n');
    var outS = document.getElementById('res-total-s');
    var outD = document.getElementById('res-simpson-d');
    var outDRatio = document.getElementById('res-d-ratio');
    var outDiv = document.getElementById('res-simpson-1minusd');
    var outRecip = document.getElementById('res-simpson-reciprocal');
    var tbodySimpson = document.getElementById('simpson-breakdown-tbody');

    var outShannonH = document.getElementById('res-shannon-h');
    var outShannonHmax = document.getElementById('res-shannon-hmax');
    var outShannonJ = document.getElementById('res-shannon-j');

    function calculateMetrics() {
      var raw = (inpCounts ? inpCounts.value : "40, 25, 15, 12, 8");
      var parts = raw.split(',').map(function(s) { return parseFloat(s.trim()); }).filter(function(n) { return !Number.isNaN(n) && n > 0; });
      if (parts.length < 2) return;

      var N = parts.reduce(function(a, b) { return a + b; }, 0);
      var S = parts.length;
      var denom = N * (N - 1);
      var num = 0;
      var shannonSum = 0;

      if (tbodySimpson) tbodySimpson.innerHTML = '';

      var tags = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];

      parts.forEach(function(n, idx) {
        var term = n * (n - 1);
        num += term;
        var p = n / N;
        shannonSum += (p * Math.log(p));

        if (tbodySimpson) {
          var tr = document.createElement('tr');
          var tag = tags[idx] || ('Sp ' + (idx + 1));
          tr.innerHTML = '<td><strong>Species ' + tag + '</strong></td><td>' + n + '</td><td>' + p.toFixed(4) + '</td><td>' + term + '</td><td>' + ((term/denom)*100).toFixed(1) + '%</td>';
          tbodySimpson.appendChild(tr);
        }
      });

      var D = denom > 0 ? (num / denom) : 0;
      var div = 1.0 - D;
      var recip = D > 0 ? (1.0 / D) : 0;

      var H = -shannonSum;
      var Hmax = Math.log(S);
      var J = Hmax > 0 ? (H / Hmax) : 0;

      // Update Simpson DOM
      if (outN) outN.textContent = N;
      if (outS) outS.textContent = 'Species Richness S = ' + S;
      if (outD) outD.textContent = D.toFixed(4);
      if (outDRatio) outDRatio.textContent = num + ' / ' + denom;
      if (outDiv) outDiv.textContent = div.toFixed(4);
      if (outRecip) outRecip.textContent = recip.toFixed(3);

      // Update Shannon DOM
      if (outShannonH) outShannonH.textContent = H.toFixed(4);
      if (outShannonHmax) outShannonHmax.textContent = Hmax.toFixed(4);
      if (outShannonJ) outShannonJ.textContent = J.toFixed(4);
    }

    if (inpCounts) inpCounts.addEventListener('input', calculateMetrics);

    function applyCommunityPreset(countsStr, activeId) {
      if (inpCounts) inpCounts.value = countsStr;
      calculateMetrics();
      ['preset-forest-a', 'preset-equitable', 'preset-monoculture'].forEach(function(id) {
        var btn = document.getElementById(id);
        if (btn) {
          if (id === activeId) {
            btn.style.borderColor = 'var(--brand)';
            btn.style.color = 'var(--brand)';
          } else {
            btn.style.borderColor = 'var(--border)';
            btn.style.color = 'var(--ink)';
          }
        }
      });
    }

    var btnForest = document.getElementById('preset-forest-a');
    var btnEquit = document.getElementById('preset-equitable');
    var btnMono = document.getElementById('preset-monoculture');

    if (btnForest) btnForest.addEventListener('click', function() { applyCommunityPreset("40, 25, 15, 12, 8", 'preset-forest-a'); });
    if (btnEquit) btnEquit.addEventListener('click', function() { applyCommunityPreset("20, 20, 20, 20, 20", 'preset-equitable'); });
    if (btnMono) btnMono.addEventListener('click', function() { applyCommunityPreset("90, 4, 3, 2, 1", 'preset-monoculture'); });

    // Initial calculation
    calculateMetrics();
  })();
  </script>
'''

    # Insert script right before closing </body>
    body_end = '</body>'
    bpos = content.rfind(body_end)
    if bpos != -1:
        content = content[:bpos] + widget_script + '\n' + content[bpos:]

    with open('notes/evs/unit3/unit-3-notes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully enriched notes/evs/unit3/unit-3-notes.html!")

if __name__ == '__main__':
    enrich_evs_u3()
