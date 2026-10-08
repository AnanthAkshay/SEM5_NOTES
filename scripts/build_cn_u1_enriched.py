"""
build_cn_u1_enriched.py - Programmatically builds enriched CN Unit 1 notes.
All additions are strictly verified against audit/verify/cn/verify_cn_u1.py.
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_cn_u1_assets import (
    generate_cascaded_db_svg,
    generate_bdp_pipe_svg,
    generate_hybrid_star_bus_svg
)
import scripts.chart_helper as ch

def build():
    path = "notes/cn/unit1/unit-1-notes.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. VERIFICATION BOX
    verif_box = '''        <div class="verification-box">
          <div class="verif-header">
            <span class="verif-badge">ACADEMIC AUDIT &amp; SOURCES</span>
            <span class="verif-date">Audited: October 2026</span>
          </div>
          <p class="verif-text"><strong>Prescribed Textbook:</strong> Behrouz A. Forouzan &amp; Sophia Chung Fegan, <em>Data Communications and Networking</em>, McGraw-Hill (Chapters 1.1–1.5, 2.1–2.5, 3.1–3.6).</p>
          <p class="verif-text"><strong>Verification Sources:</strong> Behrouz A. Forouzan 4th Edition (2007) local reference text, faculty lecture deck <code>is53-cn-unit1.pdf</code>, RFC 1122 (Internet Host Requirements), and ITU-T V.90/V.92 recommendations. All numerical values and formulas recomputed and verified via automated test suite (<code>audit/verify/cn/verify_cn_u1.py</code>).</p>
          <p class="verif-note"><em>Note:</em> The local textbook copy is the 4th Edition (2007). While syllabus mentions 5th Edition, core mathematical theorems (Fourier analysis, decibels, Nyquist, Shannon) and OSI/TCP-IP models are identical. Always verify specific schemes with your faculty before exams.</p>
        </div>'''

    if 'class="verification-box"' not in html:
        # Insert after source-links-card
        target = '</div>\n      </header>'
        repl = '</div>\n' + verif_box + '\n      </header>'
        html = html.replace(target, repl, 1)

    # 2. HYBRID TOPOLOGY IN SECTION 1
    hybrid_fig = f'''
        <!-- FIGURE 1.2: HYBRID TOPOLOGY (CIE-1 QUESTION) -->
        <figure class="diagram-card" id="fig-hybrid-topology">
          {generate_hybrid_star_bus_svg()}
          <figcaption class="diagram-title">Figure 1.2: Hybrid Topology — Central Star Backbone with Three Bus Branches</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">As requested in Ramaiah CIE-1 Exam: combines star resilience with bus cabling efficiency for departmental workgroups.</p>
        </figure>'''

    if 'id="fig-hybrid-topology"' not in html:
        target = '</div>\n\n        <div class="quick-recall-box">'
        repl = '</div>\n' + hybrid_fig + '\n\n        <div class="quick-recall-box">'
        html = html.replace(target, repl, 1)

    # 3. SECTION 4: CASCADED DB DIAGRAM + 3 SOLVED NUMERICALS
    cascaded_fig = f'''
        <!-- FIGURE 1.3: CASCADED DECIBEL TRANSMISSION -->
        <figure class="diagram-card" id="fig-cascaded-db">
          {generate_cascaded_db_svg()}
          <figcaption class="diagram-title">Figure 1.3: Signal Power Evolution across Cascaded Cable &amp; Amplifier Stages</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Net decibels are additive: -3 dB + 7 dB - 3 dB = +1 dB. Input 10 mW yields 12.589 mW output.</p>
        </figure>'''

    # Ensure 3 fully solved worked numericals in Section 4:
    # 4.1: Half power and double power
    # 4.2: Cascaded stages
    # 4.3: Cable attenuation over distance and amplifier spacing
    solved_num_sec4 = f'''{cascaded_fig}

        <!-- SOLVED WORKED NUMERICAL 4.1: HALVED & DOUBLED POWER -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge easy">WORKED NUMERICAL 4.1 &bull; EASY / FOUNDATION</span>
            <span class="problem-points">[3 MARKS]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Decibel Rating for Halved and Doubled Signal Power</h4>
            <p>Compute the decibel ($dB$) rating of a transmission link when:</p>
            <ol>
              <li>The signal power drops to exactly half of its initial value ($P_2 / P_1 = 0.5$).</li>
              <li>The signal power is doubled by an active repeater ($P_2 / P_1 = 2.0$).</li>
            </ol>
            <p><strong>Solution:</strong></p>
            <p><strong>Case 1: Power Halved:</strong></p>
            $$dB = 10 \log_{{10}}\\left(\\frac{{P_2}}{{P_1}}\\right) = 10 \\log_{{10}}(0.5) = 10 \\times (-0.30103) \\approx -3.010\\text{{ dB}}$$
            <div class="final-answer-box">
              <span class="final-answer-label">Result:</span>
              <span class="final-answer-value">A 3 dB loss (-3.01 dB) represents a 50% drop in signal power</span>
            </div>

            <p style="margin-top:1rem;"><strong>Case 2: Power Doubled:</strong></p>
            $$dB = 10 \\log_{{10}}(2.0) = 10 \\times (+0.30103) \\approx +3.010\\text{{ dB}}$$
            <div class="final-answer-box">
              <span class="final-answer-label">Result:</span>
              <span class="final-answer-value">A 3 dB gain (+3.01 dB) doubles the signal power</span>
            </div>
          </div>
        </div>

        <!-- SOLVED WORKED NUMERICAL 4.2: CASCADED TRANSMISSION -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">WORKED NUMERICAL 4.2 &bull; MEDIUM / EXAM STANDARD</span>
            <span class="problem-points">[5 MARKS]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Signal Power through Cascaded Transmission Stages</h4>
            <p>A signal with an input power of $P_{{in}} = 10\\text{{ mW}}$ passes through three cascaded transmission segments:</p>
            <ul>
              <li>Segment 1: Transmission cable with an attenuation of $-3\\text{{ dB}}$</li>
              <li>Segment 2: In-line amplifier with a gain of $+7\\text{{ dB}}$</li>
              <li>Segment 3: Secondary cable section with an attenuation of $-3\\text{{ dB}}$</li>
            </ul>
            <p>Compute: (a) The net decibel rating of the link, and (b) The final output power $P_{{out}}$.</p>

            <p><strong>Part (a): Net decibel rating:</strong></p>
            <p>Decibels are additive across cascaded stages:</p>
            $$dB_{{total}} = dB_1 + dB_2 + dB_3 = (-3) + (+7) + (-3) = +1\\text{{ dB}}$$

            <p><strong>Part (b): Output power $P_{{out}}$:</strong></p>
            $$dB_{{total}} = 10 \\log_{{10}}\\left(\\frac{{P_{{out}}}}{{P_{{in}}}}\\right) \\implies 1 = 10 \\log_{{10}}\\left(\\frac{{P_{{out}}}}{{10}}\\right)$$
            $$\\log_{{10}}\\left(\\frac{{P_{{out}}}}{{10}}\\right) = \\frac{{1}}{{10}} = 0.1 \\implies \\frac{{P_{{out}}}}{{10}} = 10^{{0.1}} \\approx 1.2589$$
            <div class="final-answer-box">
              <span class="final-answer-label">Final Output Power:</span>
              <span class="final-answer-value">P_out = 10 &times; 1.2589 = 12.589 mW (+1 dB net gain)</span>
            </div>
          </div>
        </div>

        <!-- SOLVED WORKED NUMERICAL 4.3: CABLE LOSS OVER DISTANCE & REPEATERS -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">WORKED NUMERICAL 4.3 &bull; EXAM-LEVEL / SYSTEM DESIGN</span>
            <span class="problem-points">[6 MARKS]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Cable Loss over Distance and Repeater Spacing</h4>
            <p>A coaxial cable exhibits an attenuation rate of $0.3\\text{{ dB/km}}$. An input signal with power $P_{{in}} = 200\\text{{ mW}}$ is injected at the transmitter.</p>
            <ol>
              <li>Calculate the signal power at a distance of $10\\text{{ km}}$.</li>
              <li>If the link extends to $100\\text{{ km}}$ and repeaters offering $15\\text{{ dB}}$ gain each are inserted, calculate the minimum number of repeaters required to fully compensate for cable attenuation.</li>
            </ol>

            <p><strong>Part 1: Signal power at 10 km:</strong></p>
            $$\\text{{Total loss}} = 10\\text{{ km}} \\times 0.3\\text{{ dB/km}} = 3.0\\text{{ dB}}$$
            $$dB = -3.0 = 10 \\log_{{10}}\\left(\\frac{{P_{{out}}}}{{200}}\\right) \\implies \\log_{{10}}\\left(\\frac{{P_{{out}}}}{{200}}\\right) = -0.30$$
            $$\\frac{{P_{{out}}}}{{200}} = 10^{{-0.30}} \\approx 0.50119$$
            <div class="final-answer-box">
              <span class="final-answer-label">Power at 10 km:</span>
              <span class="final-answer-value">P_out = 200 &times; 0.50119 = 100.24 mW</span>
            </div>

            <p style="margin-top:1rem;"><strong>Part 2: Repeaters required over 100 km:</strong></p>
            $$\\text{{Total link loss over 100 km}} = 100\\text{{ km}} \\times 0.3\\text{{ dB/km}} = 30.0\\text{{ dB}}$$
            $$\\text{{Number of 15 dB repeaters}} = \\frac{{\\text{{Total Loss}}}}{{\\text{{Gain per Repeater}}}} = \\frac{{30.0\\text{{ dB}}}}{{15.0\\text{{ dB}}}} = 2$$
            <div class="final-answer-box">
              <span class="final-answer-label">Repeaters Required:</span>
              <span class="final-answer-value">Exactly 2 in-line amplifiers (spaced at 33.3 km and 66.7 km)</span>
            </div>
          </div>
        </div>'''

    # Replace the single worked numerical in sec-4 with solved_num_sec4
    sec4_pattern = re.compile(r'<!-- SOLVED WORKED NUMERICAL: CASCADED TRANSMISSION -->.*?<div class="quick-recall-box">', re.DOTALL)
    html = sec4_pattern.sub(lambda m: f'{solved_num_sec4}\n\n        <div class="quick-recall-box">', html, count=1)

    # 4. SECTION 5: EXPAND WITH NYQUIST, SHANNON, CIE-1 QUESTION, LATENCY, BDP, CHARTS, AND INTERACTIVE
    components = [
        {'name': 'Transmission Delay', 'value': 0.008, 'unit': 'ms', 'color': 'var(--green)', 'desc': 'Time to push 1000B packet onto 1 Gbps link (L/R)'},
        {'name': 'Propagation Delay', 'value': 5.000, 'unit': 'ms', 'color': '#2563EB', 'desc': 'Time for bit to traverse 1000 km fiber link (d/v)'},
        {'name': 'Queuing Delay', 'value': 1.500, 'unit': 'ms', 'color': '#D97706', 'desc': 'Average wait time in intermediate switch buffer queues'},
        {'name': 'Processing Delay', 'value': 0.020, 'unit': 'ms', 'color': '#7C3AED', 'desc': 'Router header inspection & routing lookup time'}
    ]
    svg_delay_breakdown = ch.delay_breakdown_bar(components, width=720, height=240, title="Packet Latency Component Breakdown (1000 km Fiber Link)")
    svg_bdp_pipe = generate_bdp_pipe_svg()

    sec5_expansion = f'''
        <!-- SOLVED WORKED NUMERICAL 5.1: SHANNON CAPACITY -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge easy">WORKED NUMERICAL 5.1 &bull; STANDARD EXAM PROBLEM</span>
            <span class="problem-points">[5 MARKS]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Shannon Capacity of a Noisy Telephone Channel</h4>
            <p>A standard analog telephone line has a bandwidth of $B = 3000\\text{{ Hz}}$ ($3\\text{{ kHz}}$) and a Signal-to-Noise Ratio of $\\text{{SNR}}_{{dB}} = 35\\text{{ dB}}$. Compute the theoretical channel capacity.</p>

            <p><strong>Step 1: Convert $\\text{{SNR}}_{{dB}}$ to linear $\\text{{SNR}}$:</strong></p>
            $$\\text{{SNR}}_{{dB}} = 10 \\log_{{10}}(\\text{{SNR}}) \\implies 35 = 10 \\log_{{10}}(\\text{{SNR}}) \\implies \\log_{{10}}(\\text{{SNR}}) = 3.5$$
            $$\\text{{SNR}} = 10^{{3.5}} \\approx 3162.28$$

            <p><strong>Step 2: Apply Shannon Capacity Formula:</strong></p>
            $$C = B \\log_2(1 + \\text{{SNR}}) = 3000 \\times \\log_2(1 + 3162.28) = 3000 \\times \\log_2(3163.28)$$
            $$\\log_2(3163.28) = \\frac{{\\ln(3163.28)}}{{\\ln(2)}} \\approx 11.6272$$
            <div class="final-answer-box">
              <span class="final-answer-label">Shannon Capacity:</span>
              <span class="final-answer-value">C = 3000 &times; 11.6272 = 34,881.6 bps &approx; 34.88 kbps</span>
            </div>
            <p style="margin-top:0.75rem; font-size:14px; color:var(--ink-muted);"><em>Exam Comparison:</em> At $\\text{{SNR}}_{{dB}} = 30\\text{{ dB}}$ ($\\text{{SNR}} = 1000$), $C = 3000 \\times \\log_2(1001) = 29.902\\text{{ kbps}}$. The $35\\text{{ dB}}$ rating yields $34.88\\text{{ kbps}}$.</p>
          </div>
        </div>

        <!-- SOLVED WORKED NUMERICAL 5.2: COMBINED NYQUIST & SHANNON -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">WORKED NUMERICAL 5.2 &bull; COMBINED DESIGN PROBLEM</span>
            <span class="problem-points">[8 MARKS &bull; HIGH OCCURRENCE]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Signal Levels Required to Attain Shannon Limit</h4>
            <p>A channel has a bandwidth of $B = 1\\text{{ MHz}}$ and a linear $\\text{{SNR}} = 63$.</p>
            <ol>
              <li>Find the Shannon theoretical capacity of the channel.</li>
              <li>How many discrete signal voltage levels $L$ must the transmitter employ to achieve this data rate under Nyquist's theorem?</li>
            </ol>

            <p><strong>Part 1: Shannon Capacity:</strong></p>
            $$C = B \\log_2(1 + \\text{{SNR}}) = 10^6 \\times \\log_2(1 + 63) = 10^6 \\times \\log_2(64)$$
            <p>Since $64 = 2^6$, $\\log_2(64) = 6$:</p>
            <div class="final-answer-box">
              <span class="final-answer-label">Shannon Capacity:</span>
              <span class="final-answer-value">C = 10^6 &times; 6 = 6.000 Mbps</span>
            </div>

            <p style="margin-top:1rem;"><strong>Part 2: Finding Required Signal Levels $L$:</strong></p>
            <p>Equate the Nyquist formula to the Shannon limit:</p>
            $$C_{{Nyquist}} = 2 B \\log_2(L) \\implies 6 \\times 10^6 = 2 \\times (10^6) \\times \\log_2(L)$$
            $$\\log_2(L) = \\frac{{6 \\times 10^6}}{{2 \\times 10^6}} = 3 \\implies L = 2^3 = 8\\text{{ levels}}$$
            <div class="final-answer-box">
              <span class="final-answer-label">Signal Levels:</span>
              <span class="final-answer-value">L = 8 discrete voltage levels (3 bits/signal element)</span>
            </div>
          </div>
        </div>

        <!-- SOLVED WORKED NUMERICAL 5.3: CIE-1 PAST PAPER QUESTION -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">WORKED NUMERICAL 5.3 &bull; RAMAIAH CIE-1 (2025) SOLVED</span>
            <span class="problem-points">[4 MARKS &bull; QUESTION 1(a)]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Channel with Reduced Bit Rate below Shannon Limit</h4>
            <p><em>(Past Paper Question 1.a):</em> "We have a channel with a $2\\text{{-MHz}}$ bandwidth. The SNR for this channel is $63$. What are the appropriate bit rate and signal level? (To calculate signal level, consider the bit rate to be $4\\text{{ Mbps}}$ less than the upper limit)."</p>

            <p><strong>Step 1: Compute the Shannon Upper Limit:</strong></p>
            $$B = 2\\text{{ MHz}} = 2 \\times 10^6\\text{{ Hz}}, \\quad \\text{{SNR}} = 63$$
            $$C_{{upper}} = B \\log_2(1 + \\text{{SNR}}) = 2 \\times 10^6 \\times \\log_2(1 + 63) = 2 \\times 10^6 \\times \\log_2(64) = 2 \\times 10^6 \\times 6 = 12\\text{{ Mbps}}$$

            <p><strong>Step 2: Determine Specified Operating Bit Rate:</strong></p>
            $$R = C_{{upper}} - 4\\text{{ Mbps}} = 12\\text{{ Mbps}} - 4\\text{{ Mbps}} = \\mathbf{{8\\text{{ Mbps}}}}$$

            <p><strong>Step 3: Determine Signal Level $L$ using Nyquist formula:</strong></p>
            $$R = 2 B \\log_2(L) \\implies 8 \\times 10^6 = 2 \\times (2 \\times 10^6) \\times \\log_2(L) = 4 \\times 10^6 \\times \\log_2(L)$$
            $$\\log_2(L) = \\frac{{8 \\times 10^6}}{{4 \\times 10^6}} = 2 \\implies L = 2^2 = \\mathbf{{4\\text{{ levels}}}}$$
            <div class="final-answer-box">
              <span class="final-answer-label">CIE-1 Solution:</span>
              <span class="final-answer-value">Bit Rate R = 8 Mbps &bull; Signal Level L = 4 levels</span>
            </div>
          </div>
        </div>

        <h3>3. Network Performance: Latency &amp; Bandwidth-Delay Product (BDP)</h3>
        <p>In addition to data rate limits, two metrics govern network performance: <strong>latency (delay)</strong> and the <strong>Bandwidth-Delay Product</strong>.</p>

        <div class="callout callout-formula">
          <span class="callout-label">LATENCY COMPONENTS</span>
          <p>The total latency (one-way delay) for a packet traversing a transmission link is the sum of four distinct delays:</p>
          $$\\text{{Total Latency}} = T_{{trans}} + T_{{prop}} + T_{{queue}} + T_{{proc}}$$
          <ul>
            <li><strong>Transmission Delay ($T_{{trans}}$):</strong> Time needed to push all packet bits onto the wire:
              $$T_{{trans}} = \\frac{{\\text{{Packet Length }} (L) \\text{{ [bits]}}}}{{\\text{{Transmission Rate }} (R) \\text{{ [bps]}}}}$$
            </li>
            <li><strong>Propagation Delay ($T_{{prop}}$):</strong> Time for a single bit to travel from sender to receiver:
              $$T_{{prop}} = \\frac{{\\text{{Distance }} (d) \\text{{ [m]}}}}{{\\text{{Propagation Speed }} (v) \\text{{ [m/s]}}}}$$
              <em>Typical speeds:</em> $v \\approx 2 \\times 10^8\\text{{ m/s}}$ in copper/fiber; $v \\approx 3 \\times 10^8\\text{{ m/s}}$ in air/vacuum.
            </li>
            <li><strong>Queuing Delay ($T_{{queue}}$):</strong> Time the packet waits in intermediate router buffers before transmission.</li>
            <li><strong>Processing Delay ($T_{{proc}}$):</strong> Time required for routers to examine packet headers, verify checksums, and determine outgoing interface.</li>
          </ul>
        </div>

        <!-- FIGURE 1.4: LATENCY COMPONENT BREAKDOWN -->
        <figure class="diagram-card" id="fig-latency-breakdown">
          {svg_delay_breakdown}
          <figcaption class="diagram-title">Figure 1.4: Packet Latency Component Breakdown for a 1000 km Optical Fiber Link</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">On high-speed links, propagation delay (5 ms) and queuing dominate over packet transmission time (8 &mu;s).</p>
        </figure>

        <div class="callout callout-def">
          <span class="callout-label">BANDWIDTH-DELAY PRODUCT (BDP)</span>
          <p>The <strong>Bandwidth-Delay Product (BDP)</strong> defines the maximum number of bits that can fill the transmission link at any given instant ("bits in flight"):</p>
          $$\\mathbf{{\\text{{BDP}} = \\text{{Bandwidth }} (R) \\times \\text{{Propagation Delay }} (T_{{prop}})}}$$
          <p>Conceptually, envision the link as an empty water pipe connecting sender and receiver. The cross-sectional area of the pipe is the bandwidth ($R$), and its length is the propagation delay ($T_{{prop}}$). The volume of the pipe represents the BDP.</p>
        </div>

        <!-- FIGURE 1.5: BDP PIPE DIAGRAM -->
        <figure class="diagram-card" id="fig-bdp-pipe">
          {svg_bdp_pipe}
          <figcaption class="diagram-title">Figure 1.5: Conceptual Representation of Bandwidth-Delay Product as a Pipe</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Volume of pipe = R &times; T_prop. Critical for sizing sliding window buffers in TCP and ARQ protocols.</p>
        </figure>

        <!-- SOLVED WORKED NUMERICAL 5.4: STORE AND FORWARD LATENCY -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">WORKED NUMERICAL 5.4 &bull; STORE-AND-FORWARD MULTI-HOP LATENCY</span>
            <span class="problem-points">[5 MARKS]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Store-and-Forward Packet Transmission across Multiple Routers</h4>
            <p>A host transmits a $1000\\text{{-Byte}}$ ($8000\\text{{-bit}}$) packet to a destination host across $N = 3$ identical links separated by $2$ intermediate store-and-forward routers. Each link has a bandwidth of $R = 10\\text{{ Mbps}}$, distance $d = 100\\text{{ km}}$, and propagation speed $v = 2 \\times 10^8\\text{{ m/s}}$. Each router has a processing delay of $100\\text{{ }}\\mu\\text{{s}}$. Queuing delay is negligible ($0$). Calculate total end-to-end latency.</p>

            <p><strong>Step 1: Transmission delay per hop ($T_{{trans}}$):</strong></p>
            $$T_{{trans}} = \\frac{{8000\\text{{ bits}}}}{{10 \\times 10^6\\text{{ bps}}}} = 0.0008\\text{{ s}} = 0.800\\text{{ ms}} = 800\\text{{ }}\\mu\\text{{s}}$$

            <p><strong>Step 2: Propagation delay per hop ($T_{{prop}}$):</strong></p>
            $$T_{{prop}} = \\frac{{100 \\times 10^3\\text{{ m}}}}{{2 \\times 10^8\\text{{ m/s}}}} = 0.0005\\text{{ s}} = 0.500\\text{{ ms}} = 500\\text{{ }}\\mu\\text{{s}}$$

            <p><strong>Step 3: Total End-to-End Latency:</strong></p>
            <p>In store-and-forward switching, each router must completely receive the packet before forwarding it. Thus, the packet is transmitted $3$ times, propagates across $3$ links, and is processed at $2$ routers:</p>
            $$T_{{total}} = 3 \\times T_{{trans}} + 3 \\times T_{{prop}} + 2 \\times T_{{proc}}$$
            $$T_{{total}} = 3 \\times (0.8\\text{{ ms}}) + 3 \\times (0.5\\text{{ ms}}) + 2 \\times (0.1\\text{{ ms}}) = 2.4 + 1.5 + 0.2 = \\mathbf{{4.100\\text{{ ms}}}}$$
            <div class="final-answer-box">
              <span class="final-answer-label">Total Multi-Hop Latency:</span>
              <span class="final-answer-value">T_total = 4.100 ms (4100 &mu;s)</span>
            </div>
          </div>
        </div>

        <!-- SOLVED WORKED NUMERICAL 5.5: GEO SATELLITE BDP & EFFICIENCY -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">WORKED NUMERICAL 5.5 &bull; GEO SATELLITE BDP &amp; PROTOCOL EFFICIENCY</span>
            <span class="problem-points">[6 MARKS]</span>
          </div>
          <div class="problem-statement">
            <h4 class="problem-title">Bandwidth-Delay Product and Efficiency of Satellite Link</h4>
            <p>A geostationary earth orbit (GEO) satellite communication link operates at a data rate of $R = 10\\text{{ Mbps}}$. The one-way propagation delay is $T_{{prop}} = 250\\text{{ ms}}$ ($0.25\\text{{ s}}$).</p>
            <ol>
              <li>Calculate the Bandwidth-Delay Product in bits and in Kilobytes.</li>
              <li>If a Stop-and-Wait protocol is used with a frame size of $L = 1500\\text{{ Bytes}}$ ($12,000\\text{{ bits}}$) and negligible ACK transmission time, calculate the channel efficiency (utilization $\\eta$).</li>
            </ol>

            <p><strong>Part 1: Bandwidth-Delay Product:</strong></p>
            $$\\text{{BDP}} = R \\times T_{{prop}} = (10 \\times 10^6\\text{{ bps}}) \\times 0.25\\text{{ s}} = 2,500,000\\text{{ bits}} = 2.5\\text{{ Mbits}}$$
            $$\\text{{BDP in Bytes}} = \\frac{{2,500,000\\text{{ bits}}}}{{8}} = 312,500\\text{{ Bytes}} \\approx 312.5\\text{{ KB}}$$
            <div class="final-answer-box">
              <span class="final-answer-label">Satellite BDP:</span>
              <span class="final-answer-value">2,500,000 bits (312.5 KB in flight)</span>
            </div>

            <p style="margin-top:1rem;"><strong>Part 2: Stop-and-Wait Channel Efficiency:</strong></p>
            $$T_{{trans}} = \\frac{{12,000\\text{{ bits}}}}{{10 \\times 10^6\\text{{ bps}}}} = 0.0012\\text{{ s}} = 1.2\\text{{ ms}}$$
            $$\\text{{Round Trip Time (RTT)}} = 2 \\times T_{{prop}} = 2 \\times 250\\text{{ ms}} = 500\\text{{ ms}}$$
            $$\\text{{Total cycle time}} = T_{{trans}} + \\text{{RTT}} = 1.2\\text{{ ms}} + 500\\text{{ ms}} = 501.2\\text{{ ms}}$$
            $$\\eta = \\frac{{T_{{trans}}}}{{T_{{trans}} + 2 T_{{prop}}}} = \\frac{{1.2}}{{501.2}} \\approx 0.00239 = \\mathbf{{0.24\\%}}$$
            <div class="final-answer-box">
              <span class="final-answer-label">Channel Utilization:</span>
              <span class="final-answer-value">&eta; = 0.24% (Extremely wasteful; explains why sliding windows are mandatory)</span>
            </div>
          </div>
        </div>

        <!-- INTERACTIVE LATENCY & BDP EXPLORER WIDGET -->
        <div class="interactive-card" id="latency-explorer-widget">
          <div class="interactive-header">
            <div class="interactive-title">
              <span>⚡</span> Interactive Latency &amp; Bandwidth-Delay Explorer
            </div>
            <span class="interactive-badge">LIVE JS SIMULATOR</span>
          </div>

          <p style="font-size:14.5px; color:var(--ink-muted); margin-bottom:1.25rem;">
            Experiment with link distance, channel capacity, and packet size to observe propagation vs transmission delay tradeoffs and the resulting Bandwidth-Delay Product (pipe volume).
          </p>

          <div class="interactive-grid">
            <div class="control-group">
              <label for="slider-dist" class="control-label">
                <span>Link Distance ($d$):</span>
                <span id="val-dist" class="control-val">1000 km</span>
              </label>
              <input type="range" id="slider-dist" class="slider-input" min="10" max="36000" step="10" value="1000" aria-label="Distance in km">
            </div>

            <div class="control-group">
              <label for="slider-rate" class="control-label">
                <span>Bandwidth ($R$):</span>
                <span id="val-rate" class="control-val">100 Mbps</span>
              </label>
              <input type="range" id="slider-rate" class="slider-input" min="1" max="10000" step="10" value="100" aria-label="Bandwidth in Mbps">
            </div>

            <div class="control-group">
              <label for="slider-size" class="control-label">
                <span>Packet Size ($L$):</span>
                <span id="val-size" class="control-val">1500 Bytes</span>
              </label>
              <input type="range" id="slider-size" class="slider-input" min="64" max="65535" step="64" value="1500" aria-label="Packet Size in Bytes">
            </div>

            <div class="control-group">
              <label for="slider-speed" class="control-label">
                <span>Propagation Speed ($v$):</span>
                <span id="val-speed" class="control-val">200,000 km/s (Fiber)</span>
              </label>
              <select id="slider-speed" class="slider-input" style="height:36px; padding:0 8px; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:var(--ink);" aria-label="Propagation speed">
                <option value="200000" selected>200,000 km/s (Optical Fiber / Copper Cable)</option>
                <option value="300000">300,000 km/s (Wireless Radio / Satellite)</option>
              </select>
            </div>
          </div>

          <div class="results-grid">
            <div class="res-card">
              <span class="res-label">Propagation Delay (T_prop)</span>
              <span id="out-tprop" class="res-value">5.000 ms</span>
            </div>
            <div class="res-card">
              <span class="res-label">Transmission Delay (T_trans)</span>
              <span id="out-ttrans" class="res-value">0.120 ms</span>
            </div>
            <div class="res-card">
              <span class="res-label">Round Trip Time (RTT)</span>
              <span id="out-rtt" class="res-value">10.000 ms</span>
            </div>
            <div class="res-card">
              <span class="res-label">Bandwidth-Delay Product (BDP)</span>
              <span id="out-bdp" class="res-value" style="color:var(--green);">500,000 bits (62.5 KB)</span>
            </div>
            <div class="res-card">
              <span class="res-label">Stop-and-Wait Efficiency (&eta;)</span>
              <span id="out-eff" class="res-value">1.19 %</span>
            </div>
          </div>
        </div>'''

    sec5_script = '''
        <script>
        (function() {
          function updateCalc() {
            var d = parseFloat(document.getElementById('slider-dist').value);
            var r = parseFloat(document.getElementById('slider-rate').value);
            var l = parseFloat(document.getElementById('slider-size').value);
            var v = parseFloat(document.getElementById('slider-speed').value);

            document.getElementById('val-dist').textContent = d >= 1000 ? (d/1000).toFixed(1) + 'k km' : d + ' km';
            document.getElementById('val-rate').textContent = r >= 1000 ? (r/1000).toFixed(1) + ' Gbps' : r + ' Mbps';
            document.getElementById('val-size').textContent = l >= 1000 ? (l/1000).toFixed(2) + ' KB' : l + ' B';

            // Calculations
            var t_prop_sec = d / v;
            var t_prop_ms = t_prop_sec * 1000;
            var t_trans_sec = (l * 8) / (r * 1e6);
            var t_trans_ms = t_trans_sec * 1000;
            var rtt_ms = 2 * t_prop_ms;

            var bdp_bits = (r * 1e6) * t_prop_sec;
            var bdp_bytes = bdp_bits / 8;
            var bdp_str = bdp_bits >= 1e6 ? (bdp_bits/1e6).toFixed(2) + ' Mbits (' + (bdp_bytes/1024).toFixed(1) + ' KB)' : (bdp_bits/1e3).toFixed(1) + ' kbits (' + (bdp_bytes/1024).toFixed(1) + ' KB)';

            var eff = (t_trans_ms / (t_trans_ms + 2 * t_prop_ms)) * 100;

            document.getElementById('out-tprop').textContent = t_prop_ms >= 10 ? t_prop_ms.toFixed(1) + ' ms' : t_prop_ms.toFixed(3) + ' ms';
            document.getElementById('out-ttrans').textContent = t_trans_ms < 0.01 ? (t_trans_ms*1000).toFixed(1) + ' μs' : t_trans_ms.toFixed(3) + ' ms';
            document.getElementById('out-rtt').textContent = rtt_ms >= 10 ? rtt_ms.toFixed(1) + ' ms' : rtt_ms.toFixed(3) + ' ms';
            document.getElementById('out-bdp').textContent = bdp_str;
            document.getElementById('out-eff').textContent = eff.toFixed(2) + ' %';
          }

          ['slider-dist', 'slider-rate', 'slider-size', 'slider-speed'].forEach(function(id) {
            var el = document.getElementById(id);
            if (el) {
              el.addEventListener('input', updateCalc);
              el.addEventListener('change', updateCalc);
            }
          });
          updateCalc();
        })();
        </script>'''

    sec5_expansion = sec5_expansion + sec5_script

    # Replace Section 5's problem cards and add performance subsection
    sec5_pattern = re.compile(r'<!-- SOLVED WORKED NUMERICAL 1: SHANNON CAPACITY -->.*?<div class="quick-recall-box">', re.DOTALL)
    html = sec5_pattern.sub(lambda m: f'{sec5_expansion}\n\n        <div class="quick-recall-box">', html, count=1)

    # 5. EXAM ARCHIVE (PAST CIE QUESTIONS)
    archive_section = '''      <section id="questions-asked-before" class="note-section exam-archive">
        <div class="section-badge">&block; ARCHIVE</div>
        <h2 class="section-title">Solved Questions from Past CIE &amp; Model Papers</h2>
        <p class="section-lead">The following questions have been transcribed from the official Ramaiah CIE-1 test paper (Term 2025) and SEE archives in <code>notes/cn/practice/cn-cie-1-and-2.pdf</code>, solved with complete steps:</p>

        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (2025) &bull; Q 1(a)</span>
            <span class="archive-marks">[4 Marks &bull; Blooms L3, CO1]</span>
          </div>
          <p class="archive-q">"We have a channel with a 2-MHz bandwidth. The SNR for this channel is 63. What are the appropriate bit rate and signal level? (To calculate signal level consider the bit rate to be 4Mbps less than the upper limit)."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Step 1: Compute Shannon upper limit:</strong></p>
            $$C = B \log_2(1 + \text{SNR}) = 2 \times 10^6 \times \log_2(1 + 63) = 2 \times 10^6 \times 6 = \mathbf{12\text{ Mbps}}$$
            <p><strong>Step 2: Operating bit rate:</strong></p>
            $$R = 12\text{ Mbps} - 4\text{ Mbps} = \mathbf{8\text{ Mbps}}$$
            <p><strong>Step 3: Signal levels via Nyquist formula:</strong></p>
            $$R = 2 B \log_2(L) \implies 8 \times 10^6 = 2 \times (2 \times 10^6) \times \log_2(L) = 4 \times 10^6 \times \log_2(L)$$
            $$\log_2(L) = 2 \implies L = 2^2 = \mathbf{4\text{ discrete signal levels}}.$$
          </div>
        </div>

        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (2025) &bull; Q 2(a)</span>
            <span class="archive-marks">[4 Marks &bull; Blooms L4, CO1]</span>
          </div>
          <p class="archive-q">"Compare mesh topology with star topology. Draw a hybrid topology with a star backbone and three bus networks."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <ul>
              <li><strong>Mesh vs Star Comparison:</strong> Mesh requires $n(n-1)/2$ dedicated physical links and $n-1$ I/O ports per device, ensuring zero traffic congestion and maximum privacy, but at immense cabling expense. Star requires only $n$ links and $1$ port per host connected to a central hub/switch, offering simpler installation, but suffers from a single point of failure at the hub.</li>
              <li><strong>Hybrid Topology Sketch:</strong> See <a href="#fig-hybrid-topology">Figure 1.2</a> above illustrating a central star switch linking three terminated bus segments (e.g. Finance, Engineering, Admin).</li>
            </ul>
          </div>
        </div>

        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (2025) &bull; Q 2(b)</span>
            <span class="archive-marks">[4 Marks &bull; Blooms L3, CO1]</span>
          </div>
          <p class="archive-q">"Convert the digital data 11001010 to digital signal by applying AMI and differential Manchester line coding schemes."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Given Bit Sequence:</strong> <code>1  1  0  0  1  0  1  0</code></p>
            <ul>
              <li><strong>AMI (Alternate Mark Inversion):</strong> Binary <code>0</code> is represented by $0\text{ V}$. Binary <code>1</code> alternates between $+V$ and $-V$:
                <br><code>Bit 1: +V &bull; Bit 1: -V &bull; Bit 0: 0V &bull; Bit 0: 0V &bull; Bit 1: +V &bull; Bit 0: 0V &bull; Bit 1: -V &bull; Bit 0: 0V</code>
              </li>
              <li><strong>Differential Manchester:</strong> Always has a mid-bit transition for synchronization. Binary <code>0</code> causes an inversion at the start of the bit interval; binary <code>1</code> has no transition at the start.
                <br><em>Bit trace:</em> Assuming initial high state: Bit 1 (no transition at start, mid-bit drop to low); Bit 1 (no start transition, mid-bit rise to high); Bit 0 (inversion at start to low, mid-bit rise to high); Bit 0 (inversion at start to low, mid-bit rise to high); Bit 1 (no start transition, mid-bit drop to low); Bit 0 (inversion at start to high, mid-bit drop to low); Bit 1 (no start transition, mid-bit rise to high); Bit 0 (inversion at start to low, mid-bit rise to high).
              </li>
            </ul>
          </div>
        </div>

        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - I (2025) &bull; Q 3(c)</span>
            <span class="archive-marks">[7 Marks &bull; Blooms L2, CO1]</span>
          </div>
          <p class="archive-q">"What is transmission impairment? Briefly explain its causes with necessary diagrams."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p>Transmission impairment occurs when an analog or digital signal travels across an imperfect physical transmission medium, causing the received signal at the destination to differ from the injected signal at the source. The three primary causes are:</p>
            <ol>
              <li><strong>Attenuation:</strong> Loss of signal energy as heat due to conductor resistance; compensated via amplifiers (<a href="#fig-cascaded-db">Figure 1.3</a>).</li>
              <li><strong>Distortion:</strong> Occurs in composite signals because different frequency components propagate at different velocities (delay distortion), shifting arrival phases and altering waveform shape.</li>
              <li><strong>Noise:</strong> Spurious external electrical energy added to the signal (thermal noise, induced noise, crosstalk between adjacent wires, and impulse spikes).</li>
            </ol>
          </div>
        </div>
      </section>'''

    # Replace questions-asked-before section
    archive_pattern = re.compile(r'<section id="questions-asked-before".*?</section>', re.DOTALL)
    html = archive_pattern.sub(lambda m: archive_section, html, count=1)

    # 6. PRACTICE PROBLEMS (6 VERIFIED PROBLEMS WITH HIDDEN SOLUTIONS)
    practice_section = '''      <section id="practice-problems" class="note-section">
        <div class="section-badge">&nabla; PRACTICE</div>
        <h2 class="section-title">Verified Practice Problems with Hidden Answers</h2>
        <p class="section-lead">Test your problem-solving speed on these 6 exam-pattern numericals. Click each card to reveal the complete step-by-step verified solution:</p>

        <!-- PRACTICE 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge easy">PRACTICE 1 &bull; NYQUIST BIT RATE</span>
            <span class="problem-points">[3 MARKS]</span>
          </div>
          <h4 class="problem-title">Calculate the Nyquist maximum bit rate for a noiseless channel with bandwidth $B = 4\text{ kHz}$ using $L = 4$ signal levels.</h4>
          <details class="model-answer">
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="answer-body">
              <p>Formula: $C = 2 B \log_2(L)$</p>
              $$C = 2 \times 4000 \times \log_2(4) = 8000 \times 2 = \mathbf{16,000\text{ bps}} = \mathbf{16\text{ kbps}}$$
              <div class="final-answer-box">
                <span class="final-answer-label">Result:</span>
                <span class="final-answer-value">C = 16 kbps</span>
              </div>
            </div>
          </details>
        </div>

        <!-- PRACTICE 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge easy">PRACTICE 2 &bull; MESH TOPOLOGY LINKS</span>
            <span class="problem-points">[3 MARKS]</span>
          </div>
          <h4 class="problem-title">In a fully connected mesh network of $10$ computers, how many physical cables and I/O ports per device are required?</h4>
          <details class="model-answer">
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="answer-body">
              <ul>
                <li>Number of duplex links: $\frac{n(n-1)}{2} = \frac{10 \times 9}{2} = \mathbf{45\text{ physical links}}$.</li>
                <li>I/O ports per computer: $n - 1 = 10 - 1 = \mathbf{9\text{ ports}}$.</li>
              </ul>
              <div class="final-answer-box">
                <span class="final-answer-label">Result:</span>
                <span class="final-answer-value">45 Links &bull; 9 Ports per node</span>
              </div>
            </div>
          </details>
        </div>

        <!-- PRACTICE 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">PRACTICE 3 &bull; CASCADED AMPLIFIER & CABLE</span>
            <span class="problem-points">[4 MARKS]</span>
          </div>
          <h4 class="problem-title">A signal with $P_{in} = 50\text{ mW}$ enters a cable with $-6\text{ dB}$ loss, followed by an amplifier with $+12\text{ dB}$ gain. Find the final output power $P_{out}$.</h4>
          <details class="model-answer">
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="answer-body">
              <p>Net gain: $dB_{total} = -6\text{ dB} + 12\text{ dB} = +6\text{ dB}$.</p>
              $$6 = 10 \log_{10}\left(\frac{P_{out}}{50}\right) \implies \frac{P_{out}}{50} = 10^{0.6} \approx 3.98107$$
              $$P_{out} = 50 \times 3.98107 = \mathbf{199.05\text{ mW}}$$
              <div class="final-answer-box">
                <span class="final-answer-label">Result:</span>
                <span class="final-answer-value">P_out = 199.05 mW</span>
              </div>
            </div>
          </details>
        </div>

        <!-- PRACTICE 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">PRACTICE 4 &bull; SHANNON CHANNEL CAPACITY</span>
            <span class="problem-points">[5 MARKS]</span>
          </div>
          <h4 class="problem-title">Find the Shannon capacity of a telephone line with bandwidth $B = 3.1\text{ kHz}$ and $\text{SNR}_{dB} = 35\text{ dB}$.</h4>
          <details class="model-answer">
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="answer-body">
              <p>Linear $\text{SNR} = 10^{3.5} \approx 3162.28$.</p>
              $$C = 3100 \times \log_2(1 + 3162.28) = 3100 \times 11.6272 = \mathbf{36,044.4\text{ bps}} \approx \mathbf{36.04\text{ kbps}}$$
              <div class="final-answer-box">
                <span class="final-answer-label">Result:</span>
                <span class="final-answer-value">C = 36.04 kbps</span>
              </div>
            </div>
          </details>
        </div>

        <!-- PRACTICE 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">PRACTICE 5 &bull; BANDWIDTH ENGINEERING</span>
            <span class="problem-points">[5 MARKS]</span>
          </div>
          <h4 class="problem-title">What bandwidth $B$ is required to transmit $56\text{ kbps}$ over a noiseless channel using 16-QAM ($L = 16$)?</h4>
          <details class="model-answer">
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="answer-body">
              <p>Bits per signal element: $r = \log_2(16) = 4\text{ bits}$.</p>
              $$C = 2 B \log_2(L) \implies 56,000 = 2 \times B \times 4 = 8 B$$
              $$B = \frac{56,000}{8} = \mathbf{7000\text{ Hz}} = \mathbf{7\text{ kHz}}$$
              <div class="final-answer-box">
                <span class="final-answer-label">Result:</span>
                <span class="final-answer-value">Required Bandwidth B = 7.000 kHz</span>
              </div>
            </div>
          </details>
        </div>

        <!-- PRACTICE 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-badge exam">PRACTICE 6 &bull; BANDWIDTH-DELAY PRODUCT</span>
            <span class="problem-points">[5 MARKS]</span>
          </div>
          <h4 class="problem-title">A $100\text{ Mbps}$ link connects two routers across a $2000\text{ km}$ optical fiber link ($v = 2 \times 10^8\text{ m/s}$). Compute the Bandwidth-Delay Product in bits and in Kilobytes.</h4>
          <details class="model-answer">
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="answer-body">
              $$T_{prop} = \frac{2000 \times 10^3\text{ m}}{2 \times 10^8\text{ m/s}} = 0.01\text{ s} = 10\text{ ms}$$
              $$\text{BDP} = (100 \times 10^6\text{ bps}) \times 0.01\text{ s} = \mathbf{1,000,000\text{ bits}} = \mathbf{1\text{ Mbit}}$$
              $$\text{BDP in Bytes} = \frac{1,000,000}{8} = \mathbf{125,000\text{ Bytes}} = \mathbf{125\text{ KB}}$$
              <div class="final-answer-box">
                <span class="final-answer-label">Result:</span>
                <span class="final-answer-value">BDP = 1,000,000 bits (125 KB in flight)</span>
              </div>
            </div>
          </details>
        </div>
      </section>'''

    # Replace practice-problems section
    practice_pattern = re.compile(r'<section id="practice-problems".*?</section>', re.DOTALL)
    html = practice_pattern.sub(lambda m: practice_section, html, count=1)

    # Clean legacy height="auto" attribute on any SVG
    html = html.replace('width="100%" height="auto"', 'width="100%"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print("CN Unit 1 enriched successfully! File size:", os.path.getsize(path), "bytes")

if __name__ == '__main__':
    build()
