"""
build_evs_u2_enriched.py - Enriches notes/evs/unit2/unit-2-notes.html with:
1. Academic Verification Box citing Erach Bharucha, Benny Joseph, and authentic CIE 1 (2024-2025) question paper (HS 510)
2. Interactive Ecological Conservation & Green Energy Studio:
   - Tab 1: Rainwater Harvesting Yield Calculator (V = A * R * C, live catchment area, rainfall, roof coefficient presets, liters output, domestic days supply)
   - Tab 2: Solar Rooftop PV Generation & Carbon Offset Calculator (capacity, daily yield, grid emission factor, annual kWh, metric tons CO2 offset)
3. Standardized Exam Archive & 6 Verified Practice Problems matching audit/verify/evs/verify_evs_u2.py
"""

import re

def enrich_evs_u2():
    with open('notes/evs/unit2/unit-2-notes.html', 'r', encoding='utf-8') as f:
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
            <strong>Prescribed References:</strong> Erach Bharucha, <em>Textbook of Environmental Studies for Undergraduate Courses</em>, Universities Press / UGC India (Chapter 2: Natural Resources); Benny Joseph, <em>Environmental Studies</em>, McGraw-Hill; R. Rajagopalan, <em>Environmental Studies: From Crisis to Cure</em>, Oxford University Press.
          </p>
          <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
            <strong>Authentic Examination Papers Solved:</strong> Transcribed directly from official department paper in <code>notes/evs/practice/evs-cie1-qp-2024.docx</code> (Ramaiah Continuous Internal Evaluation - I, Course Code <strong>HS 510: Environmental Studies</strong>):
          </p>
          <ul style="margin: 0 0 0.5rem 0; padding-left: 1.2rem; color: var(--ink-muted); font-size: 0.88rem;">
            <li><strong>Part A (1 Mark Each):</strong> Q4 Adverse impacts of mining; Q5 Types of soil erosion by wind (Saltation, creep, suspension); Q7 Afforestation; Q8 Resource sustainability criteria; Q9 Organic farming; Q10 Definition of minerals.</li>
            <li><strong>Part B (5 Marks Each):</strong> Q1.b Environmental effects of using fossil fuels ($CO_2$, acid rain, smog); Q2.b Effects of overuse of freshwater and water resource problems (Groundwater depletion, saltwater intrusion, subsidence, Cauvery dispute); Q3.b Conventional vs. Renewable energy sources.</li>
          </ul>
          <p style="margin: 0; color: var(--ink-muted); font-size: 0.88rem;">
            <strong>Mathematical &amp; Code Verification:</strong> Rooftop rainwater harvesting yield ($150\\text{ m}^2 \\times 0.9\\text{ m} \\times 0.85 = 114.75\\text{ m}^3 = 114,750\\text{ Litres}$) and solar PV carbon offset ($8,212.5\\text{ kWh} \\times 0.82 = 6,734.25\\text{ kg CO}_2 = 6.734\\text{ metric tons}$) verified via automated unit test suite (<code>audit/verify/evs/verify_evs_u2.py</code>).
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
      <!-- Interactive Ecological Conservation & Green Energy Studio -->
      <div id="evs-conservation-studio" class="interactive-widget-card" style="margin: 2.5rem 0; padding: 1.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--brand); font-weight: 700; letter-spacing: 0.05em;">Interactive Lab Explorer</div>
            <h3 style="margin: 0.2rem 0 0 0; font-family: var(--font-display); font-size: 1.25rem; color: var(--ink);">Water Harvesting &amp; Solar Carbon Offset Studio</h3>
          </div>
          <div style="display: flex; gap: 0.5rem;" id="conservation-tab-controls" role="tablist">
            <button id="tab-btn-rain" class="pill-action-btn" role="tab" aria-selected="true" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">Tab 1: Rainwater Harvesting</button>
            <button id="tab-btn-solar" class="pill-action-btn" role="tab" aria-selected="false" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; opacity: 0.7;">Tab 2: Solar PV &amp; Carbon Offset</button>
          </div>
        </div>

        <!-- Panel 1: Rainwater Harvesting Calculator -->
        <div id="panel-rain" role="tabpanel" style="display: block;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Calculate annual rooftop rainwater harvesting potential using the hydrological runoff equation:
            $$V = A \\times R \\times C$$
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
            <!-- Inputs Column -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="margin-bottom: 0.75rem;">
                <label for="input-roof-area" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">
                  Roof Catchment Area ($A$):
                </label>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                  <input type="number" id="input-roof-area" value="150" min="10" max="10000" style="width: 120px; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.95rem; font-weight: 700;">
                  <span style="font-size: 0.82rem; color: var(--ink-muted);">$\\text{m}^2$</span>
                </div>
              </div>

              <div style="margin-bottom: 0.75rem;">
                <label for="input-rainfall-mm" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">
                  Annual Rainfall ($R$):
                </label>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                  <input type="number" id="input-rainfall-mm" value="900" min="50" max="5000" style="width: 120px; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.95rem; font-weight: 700;">
                  <span style="font-size: 0.82rem; color: var(--ink-muted);">$\\text{mm/yr}$ ($0.90\\text{ m}$)</span>
                </div>
              </div>

              <div style="margin-bottom: 0.5rem;">
                <label for="select-roof-coeff" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">
                  Roof Surface / Runoff Coeff ($C$):
                </label>
                <select id="select-roof-coeff" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.85rem;">
                  <option value="0.85" selected>Reinforced Concrete Roof (C = 0.85 - Solved Example)</option>
                  <option value="0.90">Galvanized Corrugated Metal (C = 0.90)</option>
                  <option value="0.75">Terracotta Clay Tile (C = 0.75)</option>
                  <option value="0.25">Soil / Green Roof Garden (C = 0.25)</option>
                </select>
              </div>
            </div>

            <!-- Output Column -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border); display: flex; flex-direction: column; justify-content: center;">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">
                Harvested Water Yield
              </div>

              <div style="display: flex; align-items: baseline; gap: 0.75rem; margin: 0.25rem 0;">
                <span id="res-rain-litres" style="font-family: var(--font-display); font-size: 2.2rem; font-weight: 800; color: var(--brand);">114,750</span>
                <span style="font-size: 1rem; font-weight: 700; color: var(--ink);">Litres / year</span>
              </div>
              <div id="res-rain-m3" style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--ink-muted); margin-bottom: 0.75rem;">
                Volume: 114.75 m³ ($150 \\times 0.90 \\times 0.85$)
              </div>

              <div style="padding: 0.75rem; background: var(--surface); border-radius: 6px; border: 1px dashed var(--brand);">
                <div style="font-size: 0.8rem; font-weight: 700; color: var(--ink);">Domestic Water Security Index:</div>
                <div id="res-water-days" style="font-size: 0.82rem; color: var(--ink-muted); margin-top: 0.2rem;">
                  Supplies a 4-person household (at 135 L/capita/day = 540 L/day) for <strong>212.5 days</strong> of clean domestic use!
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Panel 2: Solar PV Generation & Carbon Offset -->
        <div id="panel-solar" role="tabpanel" style="display: none;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Calculate annual electrical generation and greenhouse gas carbon offset ($CO_2$) for rooftop Solar PV arrays:
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
            <!-- Inputs Column -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="margin-bottom: 0.75rem;">
                <label for="input-solar-cap" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">
                  PV System Capacity ($kW_p$):
                </label>
                <input type="number" id="input-solar-cap" value="5.0" step="0.5" min="0.5" max="1000" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.95rem;">
              </div>

              <div style="margin-bottom: 0.75rem;">
                <label for="input-solar-yield" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">
                  Daily Specific Yield (kWh/kWp/day):
                </label>
                <input type="number" id="input-solar-yield" value="4.5" step="0.1" min="1.0" max="8.0" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.95rem;">
              </div>

              <div>
                <label for="input-grid-factor" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">
                  Grid Emission Factor (kg $CO_2$/kWh):
                </label>
                <input type="number" id="input-grid-factor" value="0.82" step="0.01" min="0.1" max="1.5" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.95rem;">
              </div>
            </div>

            <!-- Output Column -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border); display: flex; flex-direction: column; justify-content: center;">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.35rem;">
                Annual Generation &amp; Carbon Abatement
              </div>

              <div style="margin-bottom: 0.75rem;">
                <div style="font-size: 0.75rem; color: var(--ink-muted); text-transform: uppercase; font-family: var(--font-mono);">Annual Solar Electricity</div>
                <div id="res-solar-kwh" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--ink); margin: 0.1rem 0;">8,212.5 kWh</div>
                <div id="res-solar-formula" style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted);">$5.0 \\times 4.5 \\times 365 = 8,212.5\\text{ kWh/yr}$</div>
              </div>

              <div style="padding: 0.75rem; background: var(--surface); border-radius: 6px; border: 1.5px solid var(--brand);">
                <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700;">Annual Carbon Offset</div>
                <div id="res-solar-offset-kg" style="font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; color: var(--brand); margin: 0.1rem 0;">6,734.25 kg CO₂</div>
                <div id="res-solar-offset-tons" style="font-size: 0.8rem; font-weight: 600; color: var(--ink);">Equivalent to 6.734 Metric Tons of CO₂ Abated</div>
                <div id="res-solar-trees" style="font-size: 0.75rem; color: var(--ink-muted); margin-top: 0.25rem;">Equivalent to planting ~306 mature tree seedlings!</div>
              </div>
            </div>
          </div>
        </div>
      </div>
'''

    # Insert interactive widget at the end of Section 8 (#sec-numericals)
    sec_8_pos = content.find('id="sec-numericals"')
    if sec_8_pos != -1:
        sec_8_end = content.find('</section>', sec_8_pos)
        if sec_8_end != -1:
            content = content[:sec_8_end] + '\n' + interactive_widget + '\n' + content[sec_8_end:]

    # 3. Standardize and enrich Section 10 with authentic CIE 1 questions and verified practice problems
    exam_start = content.find('<section id="exam-questions"')
    ref_start = content.find('<section id="sec-references"')

    if exam_start != -1 and ref_start != -1:
        new_exam_section = '''<section id="exam-questions" class="content-section exam-archive">
        <h2 class="section-title">10. Authentic Exam Archive &amp; Model Solutions</h2>
        <p class="section-lead">The following authentic questions have been transcribed directly from official department examination papers in <code>notes/evs/practice/evs-cie1-qp-2024.docx</code> (Ramaiah Continuous Internal Evaluation - I, Course Code <strong>HS 510: Environmental Studies</strong>):</p>

        <h3 class="subsection-title">Part A: 1-Mark Objective Questions (CIE-1 2024-2025)</h3>

        <!-- CIE-1 Q4 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q4 [1M]</span>
            <span class="q-title">These are some of the adverse effects of mining:</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Options:</strong> (a) Water pollution &bull; (b) Air pollution &bull; (c) Noise pollution &bull; (d) All of the above</p>
            <p><strong>Correct Answer: (d) All of the above.</strong></p>
            <p><strong>Academic Explanation:</strong> Mining activities induce multiple cross-media ecological damage:</p>
            <ul>
              <li><em>Water Pollution:</em> Acid Mine Drainage (oxidation of iron pyrite $FeS_2$), leaching of toxic heavy metals ($Pb, Cd, As$), and siltation of downstream rivers from tailings pond breaches.</li>
              <li><em>Air Pollution:</em> Fugitive particulate matter emissions ($PM_{10}$ and $PM_{2.5}$) generated by blasting, haul roads, and mineral processing crushers.</li>
              <li><em>Noise Pollution:</em> High-decibel emissions and ground vibrations caused by explosive blasting, heavy earth-moving equipment, and slurry transport pumps.</li>
            </ul>
          </div>
        </details>

        <!-- CIE-1 Q5 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q5 [1M]</span>
            <span class="q-title">Saltation, surface creep, and suspension are the types of soil erosion by:</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Options:</strong> (a) Wind &bull; (b) Water &bull; (c) Mining &bull; (d) None of the above</p>
            <p><strong>Correct Answer: (a) Wind.</strong></p>
            <p><strong>Physical Transport Mechanics:</strong></p>
            <ul>
              <li><strong>Saltation (50–70% of wind transport):</strong> Medium sand particles ($0.1 - 0.5\\text{ mm}$) bounce in short hops along the ground.</li>
              <li><strong>Surface Creep (5–25% of transport):</strong> Coarser soil grains ($0.5 - 2.0\\text{ mm}$) are pushed or rolled along the surface by colliding saltating particles.</li>
              <li><strong>Suspension (3–40% of transport):</strong> Very fine silt and clay particles ($< 0.1\\text{ mm}$) are lifted into turbulent upper atmospheric air currents and transported over thousands of kilometers.</li>
            </ul>
          </div>
        </details>

        <!-- CIE-1 Q7 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q7 [1M]</span>
            <span class="q-title">Extensive planting of trees to increase forest cover is called:</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Options:</strong> (a) Afforestation &bull; (b) Agro forestation &bull; (c) Deforestation &bull; (d) Social forestry</p>
            <p><strong>Correct Answer: (a) Afforestation.</strong></p>
            <p><strong>Explanation:</strong> Afforestation is the establishment of a forest or stand of trees in an area where there was no recent previous tree cover, serving as a carbon sink and halting desertification.</p>
          </div>
        </details>

        <!-- CIE-1 Q8 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q8 [1M]</span>
            <span class="q-title">Sustainability requires:</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Options:</strong> (a) Conservation of resources &bull; (b) Minimizing depletion of non-renewable resources &bull; (c) Using sustainable practices for managing renewable resources &bull; (d) All</p>
            <p><strong>Correct Answer: (d) All.</strong></p>
            <p><strong>Explanation:</strong> Ecological sustainability requires balancing consumption with regeneration rates so present societal needs are met without compromising future generations.</p>
          </div>
        </details>

        <!-- CIE-1 Q9 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q9 [1M]</span>
            <span class="q-title">Which of the following is the most environmentally friendly agriculture practice?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Options:</strong> (a) Using chemical fertilizers &bull; (b) Using insecticides &bull; (c) Organic farming &bull; (d) None of the above</p>
            <p><strong>Correct Answer: (c) Organic farming.</strong></p>
            <p><strong>Explanation:</strong> Organic farming eliminates synthetic agrochemicals, relying on biofertilizers (compost, vermicompost, <em>Rhizobium</em>), crop rotation, and biological pest control to preserve soil microbial biodiversity and prevent groundwater nitrate toxicity.</p>
          </div>
        </details>

        <!-- CIE-1 Q10 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q10 [1M]</span>
            <span class="q-title">A mineral is defined as a:</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Options:</strong> (a) Organic matter &bull; (b) Naturally occurring inorganic substance &bull; (c) Synthetic compound &bull; (d) None</p>
            <p><strong>Correct Answer: (b) Naturally occurring inorganic substance.</strong></p>
            <p><strong>Explanation:</strong> A mineral is a naturally occurring, homogeneous, inorganic solid having a definite chemical composition and an ordered internal crystalline structure.</p>
          </div>
        </details>

        <h3 class="subsection-title">Part B: 5-Mark Subjective Questions (CIE-1 2024-2025)</h3>

        <!-- CIE-1 Part B Q1.b -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q1.b [5M]</span>
            <span class="q-title">What are the environmental effects of using fossil fuels?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Model Solution:</strong> The combustion of fossil fuels (coal, petroleum, natural gas) generates severe multidimensional impacts:</p>
            <ol>
              <li><strong>Anthropogenic Greenhouse Effect &amp; Global Warming:</strong> Burning carbon yields massive $CO_2$ emissions (rising from pre-industrial $280\\text{ ppm}$ to over $420\\text{ ppm}$), driving global temperature rise, polar ice melt, and sea-level rise.</li>
              <li><strong>Acid Deposition (Acid Rain):</strong> High sulfur and nitrogen content in coal/petroleum combusts into $SO_2$ and $NO_x$, which oxidize into sulfuric acid ($H_2SO_4$) and nitric acid ($HNO_3$), dropping precipitation $pH < 5.6$ and corroding monuments and acidifying freshwater fisheries.</li>
              <li><strong>Photochemical Smog &amp; Respiratory Distress:</strong> Vehicle exhausts release volatile organic compounds (VOCs) and $NO_x$, reacting with sunlight to form ground-level ozone ($O_3$) and photochemical smog, triggering asthma and chronic bronchitis.</li>
              <li><strong>Thermal Pollution &amp; Ash Disposal:</strong> Coal-fired thermal power stations produce millions of tons of fly ash containing toxic heavy metals ($Pb, As, Hg$), contaminating groundwater aquifers and topsoils.</li>
            </ol>
          </div>
        </details>

        <!-- CIE-1 Part B Q2.b -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q2.b [5M]</span>
            <span class="q-title">Explain the effects of overuse of fresh water and problems related to water resources.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Model Solution:</strong> Over-exploitation of freshwater leads to critical hydrological crises:</p>
            <ol>
              <li><strong>Water Table Depletion:</strong> Intensive tube-well extraction for green-revolution agriculture exceeds natural monsoon recharge, causing regional aquifer water tables to fall by meters annually.</li>
              <li><strong>Saltwater Intrusion:</strong> Excessive drawdown in coastal areas reverses hydraulic gradients, pulling dense saline seawater into freshwater municipal aquifers and ruining drinking water supplies.</li>
              <li><strong>Land Subsidence:</strong> Over-extraction drains interstitial pore water from deep silt/clay strata, causing the overburden ground to compact and sink irreversibly (e.g., Mexico City, Jakarta, Venice).</li>
              <li><strong>Waterlogging and Soil Salinization:</strong> In canal-irrigated zones, excessive irrigation without adequate drainage raises the water table into the root zone, causing capillary action to evaporate water and leave a toxic crust of alkaline salts on arable soils.</li>
              <li><strong>Riparian &amp; Interstate Water Conflicts:</strong> Upstream impoundments restrict downstream flows during dry seasons, causing severe socio-economic disputes (e.g. Cauvery River dispute between Karnataka and Tamil Nadu).</li>
            </ol>
          </div>
        </details>

        <!-- CIE-1 Part B Q3.b -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">CIE-1 Q3.b [5M]</span>
            <span class="q-title">Write an explanatory note on energy sources (Conventional vs. Renewable Alternatives).</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Official Model Solution:</strong> Energy sources are categorized based on replenishment capability:</p>
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr>
                    <th>Dimension</th>
                    <th>Conventional / Non-Renewable</th>
                    <th>Non-Conventional / Renewable</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Sources</strong></td>
                    <td>Coal, Crude Oil, Natural Gas, Nuclear Fission ($U^{235}$).</td>
                    <td>Solar PV, Wind Turbines, Small Hydro, Biomass, Geothermal.</td>
                  </tr>
                  <tr>
                    <td><strong>Depletion Profile</strong></td>
                    <td>Finite geological deposits; exhausting within decades to centuries.</td>
                    <td>Naturally replenished continuously via solar and planetary cycles.</td>
                  </tr>
                  <tr>
                    <td><strong>Carbon Footprint</strong></td>
                    <td>High greenhouse gas and particulate emissions ($0.82 - 1.0\\text{ kg CO}_2/\\text{kWh}$).</td>
                    <td>Zero or near-zero operational greenhouse gas emissions.</td>
                  </tr>
                  <tr>
                    <td><strong>Ecological Hazards</strong></td>
                    <td>Acid rain, oil spills, radioactive nuclear waste storage.</td>
                    <td>Intermittent output, land requirement, bird strike risks (wind).</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </details>

        <h3 class="subsection-title">Verified Numerical &amp; Conceptual Practice Problems</h3>

        <!-- Practice 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 1 &bull; ROOFTOP RAINWATER HARVESTING YIELD</span>
          </div>
          <h4 class="problem-title">Calculate the annual harvested rainwater yield for a concrete rooftop of area $150\\text{ m}^2$ located in a region with $900\\text{ mm}$ annual rainfall and runoff coefficient $0.85$.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Applying the hydrological harvesting equation: $V = A \\times R \\times C$</p>
              <ul>
                <li>Catchment Area: $A = 150\\text{ m}^2$</li>
                <li>Rainfall: $R = 900\\text{ mm} = 0.90\\text{ m}$</li>
                <li>Runoff Coefficient: $C = 0.85$ (concrete roof)</li>
              </ul>
              $$V = 150\\text{ m}^2 \\times 0.90\\text{ m} \\times 0.85 = 135 \\times 0.85 = \\mathbf{114.75\\text{ m}^3}$$
              $$V_{\\text{litres}} = 114.75 \\times 1,000 = \\mathbf{114,750\\text{ Litres}}$$
              <p><em>Verification:</em> Verified by automated unit test in <code>audit/verify/evs/verify_evs_u2.py</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 2 &bull; SOLAR PV GENERATION &amp; CO2 OFFSET</span>
          </div>
          <h4 class="problem-title">A $5.0\\text{ kWp}$ solar PV rooftop system operates with an average yield of $4.5\\text{ kWh/kWp/day}$. If the grid emission factor is $0.82\\text{ kg CO}_2/\\text{kWh}$, calculate annual energy generated and metric tons of $CO_2$ offset.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ol>
                <li><strong>Annual Electricity Generation:</strong>
                  $$E_{\\text{annual}} = 5.0\\text{ kWp} \\times 4.5\\text{ kWh/kWp/day} \\times 365 = \\mathbf{8,212.5\\text{ kWh/year}}$$
                </li>
                <li><strong>Annual Carbon Dioxide Offset:</strong>
                  $$\\text{CO}_2\\text{ Offset} = 8,212.5\\text{ kWh} \\times 0.82\\text{ kg CO}_2/\\text{kWh} = \\mathbf{6,734.25\\text{ kg CO}_2}$$
                </li>
                <li><strong>Conversion to Metric Tons:</strong>
                  $$\\text{Offset}_{\\text{tons}} = \\frac{6,734.25}{1,000} = \\mathbf{6.734\\text{ Metric Tons}}$$
                </li>
              </ol>
              <p><em>Verification:</em> Verified by automated unit test in <code>audit/verify/evs/verify_evs_u2.py</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 3 &bull; ACID MINE DRAINAGE (AMD) REACTION</span>
          </div>
          <h4 class="problem-title">Write the stoichiometric chemical reaction for Acid Mine Drainage (AMD) formation and explain why it severely pollutes aquatic ecosystems.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>When sub-surface mining exposes iron pyrite ($FeS_2$) to atmospheric oxygen and groundwater, iron-oxidizing bacteria (<em>Acidithiobacillus ferrooxidans</em>) catalyze the reaction:</p>
              $$2\\text{FeS}_2 + 7\\text{O}_2 + 2\\text{H}_2\\text{O} \\longrightarrow 2\\text{Fe}^{2+} + 4\\text{SO}_4^{2-} + 4\\text{H}^+$$
              <p><strong>Ecological Impact:</strong> Generates concentrated sulfuric acid ($H_2SO_4$), driving stream $pH$ down to $2 - 3$, dissolving highly toxic heavy metals (aluminum, lead, cadmium), and suffocating aquatic gills with insoluble orange-brown ferric hydroxide precipitations ("yellow boy").</p>
            </div>
          </details>
        </div>

        <!-- Practice 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 4 &bull; WATERLOGGING VS SALINIZATION MECHANISMS</span>
          </div>
          <h4 class="problem-title">Differentiate between waterlogging and soil salinization in agricultural land management.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ul>
                <li><strong>Waterlogging:</strong> Physical condition where excessive irrigation water saturates soil pore spaces, pushing the water table into the plant root zone, displacing oxygen, and causing anaerobic root asphyxiation.</li>
                <li><strong>Soil Salinization:</strong> Chemical degradation where high water tables evaporate in arid/semi-arid climates, drawing dissolved minerals upward via capillary action and depositing a sterile white crust of alkaline sodium, calcium, and magnesium salts on topsoil.</li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Practice 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 5 &bull; WIND EROSION FRACTION SIZES</span>
          </div>
          <h4 class="problem-title">Tabulate the three physical modes of wind erosion with their respective particle diameter ranges and transport percentages.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <div class="table-container">
                <table class="notes-table">
                  <thead>
                    <tr>
                      <th>Mode of Erosion</th>
                      <th>Particle Diameter Range</th>
                      <th>Percentage of Total Wind Transport</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Saltation</strong> (Bouncing)</td>
                      <td>$0.1\\text{ mm}$ to $0.5\\text{ mm}$</td>
                      <td>$50\\%$ to $70\\%$ (Dominant mechanism)</td>
                    </tr>
                    <tr>
                      <td><strong>Surface Creep</strong> (Rolling)</td>
                      <td>$0.5\\text{ mm}$ to $2.0\\text{ mm}$</td>
                      <td>$5\\%$ to $25\\%$</td>
                    </tr>
                    <tr>
                      <td><strong>Suspension</strong> (Airborne)</td>
                      <td>$< 0.1\\text{ mm}$ (Fine silt/clay)</td>
                      <td>$3\\%$ to $40\\%$</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </details>
        </div>

        <!-- Practice 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 6 &bull; ECOLOGICAL CONFLICTS OF MEGA DAMS</span>
          </div>
          <h4 class="problem-title">Analyze the key environmental and social trade-offs of large river valley projects with reference to Sardar Sarovar and Tehri Dams.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>While multipurpose mega dams generate hydroelectricity and irrigation water, they incur severe ecological and socio-economic trade-offs:</p>
              <ul>
                <li><strong>Forest &amp; Biodiversity Submergence:</strong> Inundation of vast tracts of pristine riverine forests, destroying wildlife corridors and endemic habitats.</li>
                <li><strong>Tribal Displacement &amp; Resettlement Trauma:</strong> Uprooting indigenous tribal communities from ancestral lands without adequate rehabilitation (the core focus of Medha Patkar's <em>Narmada Bachao Andolan</em>).</li>
                <li><strong>Reservoir-Induced Seismicity (RIS):</strong> Massive concentrated water masses in seismic zones (e.g. Tehri Dam in the Central Himalayan seismic gap) create pore pressure lubrication along active fault lines.</li>
                <li><strong>Silt Trap &amp; Downstream Delta Erosion:</strong> Trapping fertile nutrient silts in reservoirs deprives downstream estuaries, starving agricultural deltas and triggering coastal erosion.</li>
              </ul>
            </div>
          </details>
        </div>
      </section>'''
        content = content[:exam_start] + new_exam_section + '\n\n      ' + content[ref_start:]

    # 4. Interactive Studio JavaScript Engine
    widget_script = '''
  <!-- Interactive EVS Unit 2 Water Harvesting & Solar Studio Engine -->
  <script>
  (function() {
    // Tab switching
    var tabRain = document.getElementById('tab-btn-rain');
    var tabSolar = document.getElementById('tab-btn-solar');
    var panelRain = document.getElementById('panel-rain');
    var panelSolar = document.getElementById('panel-solar');

    if (tabRain && tabSolar && panelRain && panelSolar) {
      tabRain.addEventListener('click', function() {
        tabRain.style.borderColor = 'var(--brand)';
        tabRain.style.color = 'var(--brand)';
        tabRain.style.opacity = '1';
        tabRain.setAttribute('aria-selected', 'true');

        tabSolar.style.borderColor = 'var(--border)';
        tabSolar.style.color = 'var(--ink)';
        tabSolar.style.opacity = '0.7';
        tabSolar.setAttribute('aria-selected', 'false');

        panelRain.style.display = 'block';
        panelSolar.style.display = 'none';
      });

      tabSolar.addEventListener('click', function() {
        tabSolar.style.borderColor = 'var(--brand)';
        tabSolar.style.color = 'var(--brand)';
        tabSolar.style.opacity = '1';
        tabSolar.setAttribute('aria-selected', 'true');

        tabRain.style.borderColor = 'var(--border)';
        tabRain.style.color = 'var(--ink)';
        tabRain.style.opacity = '0.7';
        tabRain.setAttribute('aria-selected', 'false');

        panelSolar.style.display = 'block';
        panelRain.style.display = 'none';
      });
    }

    // Panel 1: Rainwater Harvesting Engine
    var inpArea = document.getElementById('input-roof-area');
    var inpRain = document.getElementById('input-rainfall-mm');
    var selCoeff = document.getElementById('select-roof-coeff');
    var outLitres = document.getElementById('res-rain-litres');
    var outM3 = document.getElementById('res-rain-m3');
    var outDays = document.getElementById('res-water-days');

    function updateRain() {
      var a = parseFloat(inpArea ? inpArea.value : "150");
      var rMm = parseFloat(inpRain ? inpRain.value : "900");
      var c = parseFloat(selCoeff ? selCoeff.value : "0.85");

      if (Number.isNaN(a) || Number.isNaN(rMm) || Number.isNaN(c) || a <= 0 || rMm <= 0) return;

      var rM = rMm / 1000.0;
      var vM3 = a * rM * c;
      var vLitres = vM3 * 1000.0;

      if (outLitres) outLitres.textContent = Math.round(vLitres).toLocaleString('en-US');
      if (outM3) outM3.textContent = 'Volume: ' + vM3.toFixed(2) + ' m³ (' + a + ' × ' + rM.toFixed(2) + ' × ' + c + ')';

      if (outDays) {
        var dailyUse = 4 * 135; // 540 L/day
        var days = (vLitres / dailyUse).toFixed(1);
        outDays.innerHTML = 'Supplies a 4-person household (at 135 L/capita/day = 540 L/day) for <strong>' + days + ' days</strong> of clean domestic use!';
      }
    }

    if (inpArea) inpArea.addEventListener('input', updateRain);
    if (inpRain) inpRain.addEventListener('input', updateRain);
    if (selCoeff) selCoeff.addEventListener('change', updateRain);

    // Panel 2: Solar PV & Carbon Engine
    var inpCap = document.getElementById('input-solar-cap');
    var inpYield = document.getElementById('input-solar-yield');
    var inpGrid = document.getElementById('input-grid-factor');
    var outKwh = document.getElementById('res-solar-kwh');
    var outFormula = document.getElementById('res-solar-formula');
    var outOffsetKg = document.getElementById('res-solar-offset-kg');
    var outOffsetTons = document.getElementById('res-solar-offset-tons');
    var outTrees = document.getElementById('res-solar-trees');

    function updateSolar() {
      var cap = parseFloat(inpCap ? inpCap.value : "5.0");
      var y = parseFloat(inpYield ? inpYield.value : "4.5");
      var factor = parseFloat(inpGrid ? inpGrid.value : "0.82");

      if (Number.isNaN(cap) || Number.isNaN(y) || Number.isNaN(factor) || cap <= 0 || y <= 0) return;

      var kwh = cap * y * 365;
      var offsetKg = kwh * factor;
      var offsetTons = offsetKg / 1000.0;
      var trees = Math.round(offsetKg / 22.0);

      if (outKwh) outKwh.textContent = kwh.toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + ' kWh';
      if (outFormula) outFormula.textContent = cap.toFixed(1) + ' × ' + y.toFixed(1) + ' × 365 = ' + kwh.toFixed(1) + ' kWh/yr';
      if (outOffsetKg) outOffsetKg.textContent = offsetKg.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' kg CO₂';
      if (outOffsetTons) outOffsetTons.textContent = 'Equivalent to ' + offsetTons.toFixed(3) + ' Metric Tons of CO₂ Abated';
      if (outTrees) outTrees.textContent = 'Equivalent to planting ~' + trees + ' mature tree seedlings!';
    }

    if (inpCap) inpCap.addEventListener('input', updateSolar);
    if (inpYield) inpYield.addEventListener('input', updateSolar);
    if (inpGrid) inpGrid.addEventListener('input', updateSolar);
  })();
  </script>
'''

    # Insert script right before closing </body>
    body_end = '</body>'
    bpos = content.rfind(body_end)
    if bpos != -1:
        content = content[:bpos] + widget_script + '\n' + content[bpos:]

    with open('notes/evs/unit2/unit-2-notes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully enriched notes/evs/unit2/unit-2-notes.html!")

if __name__ == '__main__':
    enrich_evs_u2()
