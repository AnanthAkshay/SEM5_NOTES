"""
build_cn_u3_enriched.py - Programmatically enriches CN Unit 3 notes:
- Academic verification box (Forouzan 4th Ed, RFC 791, RFC 4632, RFC 1918, RFC 3022, RFC 792)
- 4 Theme-Aware SVG diagrams (IPv4 Header, CIDR Bit Breakdown, Dijkstra Graph, NAT Flow)
- Interactive IPv4 Subnet / CIDR Calculator in vanilla JS
- 7 Solved Exam Questions transcribed from Ramaiah CIE-2 (Term 2025)
- 6 Verified Practice Problems with step-by-step collapsible solutions
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_cn_u3_assets import (
    generate_ipv4_header_svg,
    generate_cidr_breakdown_svg,
    generate_dijkstra_graph_svg,
    generate_nat_flow_svg
)

def build():
    path = "notes/cn/unit3/unit-3-notes.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. VERIFICATION BOX
    verif_box = '''        <div class="verification-box">
          <div class="verif-header">
            <span class="verif-badge">ACADEMIC AUDIT &amp; SOURCES</span>
            <span class="verif-date">Audited: October 2026</span>
          </div>
          <p class="verif-text"><strong>Prescribed Textbook:</strong> Behrouz A. Forouzan &amp; Sophia Chung Fegan, <em>Data Communications and Networking</em>, McGraw-Hill (Chapters 19.1–19.3, 20.1–20.4, 21.1–21.3, 22.1–22.3).</p>
          <p class="verif-text"><strong>Verification Sources:</strong> Behrouz A. Forouzan 4th Edition (2007) local reference text, faculty lecture deck <code>is53-cn-unit2.pdf</code>, RFC 791 (IPv4 Protocol &amp; Header), RFC 4632 (Classless Inter-Domain Routing / CIDR), RFC 1918 (Private Address Allocation), RFC 3022 (Network Address Translation / NAT), RFC 792 (ICMPv4), and Ramaiah Autonomous CIE-2 Examination Papers (Term 2025). All numerical calculations, IP masks, fragment offsets, and Dijkstra path costs verified via automated test suite (<code>audit/verify/cn/verify_cn_u3.py</code>).</p>
          <p class="verif-note"><em>Note:</em> The local textbook copy is the 4th Edition (2007). All IP header bit structures, CIDR prefix mathematics, and routing shortest-path algorithms are standard across all networking curricula and RFC specifications.</p>
        </div>'''

    target = '</div>\n      </header>'
    if 'class="verification-box"' not in html:
        html = html.replace(target, '</div>\n' + verif_box + '\n      </header>', 1)

    # 2. FIGURE 3.2 & INTERACTIVE SUBNET CALCULATOR IN SECTION 3 (#sec-3)
    cidr_fig = f'''
        <!-- FIGURE 3.2: CIDR BIT ALLOCATION & SUBNET RANGES -->
        <figure class="diagram-card" id="fig-cidr-breakdown">
          {generate_cidr_breakdown_svg()}
          <figcaption class="diagram-title">Figure 3.2: CIDR Prefix Bit Partition &amp; Host Range for 200.16.70.82/27</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">As required in Ramaiah SEE Examination: 27 network prefix bits leave 5 host bits, yielding 30 assignable host addresses (200.16.70.65 to 200.16.70.94).</p>
        </figure>'''

    subnet_interactive = '''
        <!-- INTERACTIVE SUBNET & CIDR CALCULATOR -->
        <div class="interactive-card" id="subnet-calculator-widget">
          <div class="interactive-header">
            <div class="interactive-title">
              <span>🌐</span> Interactive IPv4 Subnet &amp; CIDR Calculator
            </div>
            <span class="interactive-badge">LIVE JS CALCULATOR</span>
          </div>

          <p style="font-size:14.5px; color:var(--ink-muted); margin-bottom:1.25rem;">
            Enter any IPv4 address and select a CIDR prefix (/16 to /30) to compute the network address, broadcast address, valid host range, and total usable host count in real time.
          </p>

          <div class="interactive-grid">
            <div class="control-group">
              <label for="input-ip" class="control-label">
                <span>IPv4 Address:</span>
                <span id="lbl-ip" class="control-val">200.16.70.82</span>
              </label>
              <input type="text" id="input-ip" class="slider-input" value="200.16.70.82" style="font-family:var(--font-mono); padding:6px 12px; border-radius:8px; border:1px solid var(--border); background:var(--surface); color:var(--ink);" aria-label="IPv4 Address">
            </div>

            <div class="control-group">
              <label for="slider-prefix" class="control-label">
                <span>CIDR Prefix (/n):</span>
                <span id="lbl-prefix" class="control-val">/27 (255.255.255.224)</span>
              </label>
              <input type="range" id="slider-prefix" min="16" max="30" value="27" step="1" class="slider-input" aria-label="CIDR Prefix">
            </div>
          </div>

          <div class="results-grid">
            <div class="res-card">
              <span class="res-label">Network Address</span>
              <span id="out-net" class="res-value" style="color:var(--green);">200.16.70.64</span>
            </div>
            <div class="res-card">
              <span class="res-label">Subnet Mask</span>
              <span id="out-mask" class="res-value">255.255.255.224</span>
            </div>
            <div class="res-card">
              <span class="res-label">Broadcast Address</span>
              <span id="out-bcast" class="res-value" style="color:#B91C1C;">200.16.70.95</span>
            </div>
            <div class="res-card">
              <span class="res-label">Usable Host Range</span>
              <span id="out-range" class="res-value">200.16.70.65 - .94</span>
            </div>
            <div class="res-card">
              <span class="res-label">Total Usable Hosts</span>
              <span id="out-hosts" class="res-value" style="color:var(--brand);">30 Hosts (2^5 - 2)</span>
            </div>
            <div class="res-card">
              <span class="res-label">Binary Mask Representation</span>
              <span id="out-binmask" class="res-value" style="font-size:11px; font-family:var(--font-mono);">11111111.11111111.11111111.11100000</span>
            </div>
          </div>
        </div>

        <script>
        (function() {
          function ipToInt(ip) {
            var parts = ip.trim().split('.');
            if (parts.length !== 4) return null;
            var num = 0;
            for (var i = 0; i < 4; i++) {
              var n = parseInt(parts[i], 10);
              if (isNaN(n) || n < 0 || n > 255) return null;
              num = (num << 8) | n;
            }
            return num >>> 0;
          }

          function intToIp(num) {
            return [
              (num >>> 24) & 255,
              (num >>> 16) & 255,
              (num >>> 8) & 255,
              num & 255
            ].join('.');
          }

          function getMask(p) {
            if (p === 0) return 0;
            return ((0xFFFFFFFF << (32 - p)) >>> 0);
          }

          function toBin8(n) {
            var s = n.toString(2);
            while (s.length < 8) s = '0' + s;
            return s;
          }

          function updateSubnet() {
            var ipStr = document.getElementById('input-ip').value.trim();
            var prefix = parseInt(document.getElementById('slider-prefix').value, 10);
            var ipInt = ipToInt(ipStr);

            if (ipInt === null) {
              document.getElementById('lbl-ip').textContent = 'Invalid IP';
              return;
            }

            var mask = getMask(prefix);
            var netInt = (ipInt & mask) >>> 0;
            var bcastInt = (netInt | (~mask >>> 0)) >>> 0;
            var hostBits = 32 - prefix;
            var numHosts = Math.pow(2, hostBits) - 2;

            var firstHost = netInt + 1;
            var lastHost = bcastInt - 1;

            var maskIp = intToIp(mask);
            var netIp = intToIp(netInt);
            var bcastIp = intToIp(bcastInt);

            document.getElementById('lbl-ip').textContent = ipStr;
            document.getElementById('lbl-prefix').textContent = '/' + prefix + ' (' + maskIp + ')';
            document.getElementById('out-net').textContent = netIp;
            document.getElementById('out-mask').textContent = maskIp;
            document.getElementById('out-bcast').textContent = bcastIp;
            document.getElementById('out-range').textContent = intToIp(firstHost) + ' - ' + intToIp(lastHost);
            document.getElementById('out-hosts').textContent = numHosts + ' Hosts (2^' + hostBits + ' - 2)';

            var maskParts = maskIp.split('.').map(function(n) { return toBin8(parseInt(n, 10)); });
            document.getElementById('out-binmask').textContent = maskParts.join('.');
          }

          var ipIn = document.getElementById('input-ip');
          var prefSl = document.getElementById('slider-prefix');
          if (ipIn && prefSl) {
            ipIn.addEventListener('input', updateSubnet);
            prefSl.addEventListener('input', updateSubnet);
            updateSubnet();
          }
        })();
        </script>'''

    sec3_m = re.search(r'(<section id="sec-3".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if sec3_m:
        html = html[:sec3_m.start(2)] + cidR_content(cidr_fig, subnet_interactive) + '\n\n        ' + html[sec3_m.start(2):]

    # 3. FIGURE 3.4: NAT FLOW IN SECTION 4 (#sec-4)
    nat_fig = f'''
        <!-- FIGURE 3.4: NAT PORT TRANSLATION ARCHITECTURE (CIE-2 Q2.a) -->
        <figure class="diagram-card" id="fig-nat-flow">
          {generate_nat_flow_svg()}
          <figcaption class="diagram-title">Figure 3.4: Network Address Translation (NAT / NAPT) Packet Rewriting (RFC 3022)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">As required in Ramaiah CIE-2 Exam Q2(a): Maps private socket (192.168.1.10:45000) to public gateway socket (203.0.113.1:50001).</p>
        </figure>'''

    sec4_m = re.search(r'(<section id="sec-4".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if sec4_m:
        html = html[:sec4_m.start(2)] + nat_fig + '\n\n        ' + html[sec4_m.start(2):]

    # 4. FIGURE 3.1: IPV4 HEADER IN SECTION 5 (#sec-5)
    ipv4_hdr_fig = f'''
        <!-- FIGURE 3.1: IPV4 20-BYTE HEADER GRID FORMAT (RFC 791) -->
        <figure class="diagram-card" id="fig-ipv4-header">
          {generate_ipv4_header_svg()}
          <figcaption class="diagram-title">Figure 3.1: IPv4 20-Byte Base Datagram Header Structure (RFC 791)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Five 32-bit rows defining 14 standard fields (IHL=5 means 5 x 4 = 20 bytes; Fragment Offset in 8-byte blocks; Checksum covers header only).</p>
        </figure>'''

    sec5_m = re.search(r'(<section id="sec-5".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if sec5_m:
        html = html[:sec5_m.start(2)] + ipv4_hdr_fig + '\n\n        ' + html[sec5_m.start(2):]

    # 5. FIGURE 3.3: DIJKSTRA GRAPH IN SECTION 7 (#sec-7)
    dijkstra_fig = f'''
        <!-- FIGURE 3.3: DIJKSTRA 6-NODE SHORTEST PATH GRAPH (CIE-2 Q3.a) -->
        <figure class="diagram-card" id="fig-dijkstra-graph">
          {generate_dijkstra_graph_svg()}
          <figcaption class="diagram-title">Figure 3.3: Dijkstra's Shortest Path Tree on 6-Node Network (Ramaiah CIE-2 Q3.a Solved)</figcaption>
          <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">Source Node A: Shortest tree paths highlighted in green (A&rarr;B: 2, A&rarr;C: 3 via B, A&rarr;E: 6 via C, A&rarr;D: 8 via E, A&rarr;F: 9 via D).</p>
        </figure>'''

    sec7_m = re.search(r'(<section id="sec-7".*?)(<div class="quick-recall-box">)', html, re.DOTALL)
    if sec7_m:
        html = html[:sec7_m.start(2)] + dijkstra_fig + '\n\n        ' + html[sec7_m.start(2):]

    # 6. SOLVED EXAM ARCHIVE (RAMAIAH CIE-2 PAPERS)
    archive_section = '''      <section id="questions-asked-before" class="note-section exam-archive">
        <div class="section-badge">&block; ARCHIVE</div>
        <h2 class="section-title">Solved Questions from Past CIE-2 Examination Papers</h2>
        <p class="section-lead">The following questions have been transcribed from the official Ramaiah CIE-2 examination paper (Term 2025) in <code>notes/cn/practice/cn-cie-1-and-2.pdf</code>, solved with complete intermediate steps:</p>

        <!-- CIE-2 Q1(a) -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (2025) &bull; Q 1(a)</span>
            <span class="archive-marks">[7 Marks &bull; Blooms L2, CO3]</span>
          </div>
          <p class="archive-q">"Differentiate between IPv4 and IPv6 packet formats. Explain the role of ICMP messages in IP communication."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Part 1: Key Differences between IPv4 and IPv6 Packets:</strong></p>
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr><th>Feature</th><th>IPv4 Header (RFC 791)</th><th>IPv6 Header (RFC 2460 / 8200)</th></tr>
                </thead>
                <tbody>
                  <tr><td><strong>Header Length</strong></td><td>Variable (20 to 60 bytes, depending on Options)</td><td>Fixed 40 bytes (Base header)</td></tr>
                  <tr><td><strong>Address Size</strong></td><td>32 bits (4 octets, $2^{32} \approx 4.29 \times 10^9$)</td><td>128 bits (16 octets, $2^{128} \approx 3.4 \times 10^{38}$)</td></tr>
                  <tr><td><strong>Checksum</strong></td><td>Included in header (recalculated at every hop)</td><td>Removed (integrity verified by L2 and L4)</td></tr>
                  <tr><td><strong>Fragmentation</strong></td><td>Handled by routers and sending host (ID, Flags, Offset)</td><td>Handled only by sending host using Extension Headers</td></tr>
                  <tr><td><strong>Flow Label</strong></td><td>Not available (only 8-bit TOS/DSCP)</td><td>20-bit dedicated Flow Label for QoS stream routing</td></tr>
                  <tr><td><strong>Next Header</strong></td><td>8-bit Protocol field</td><td>8-bit Next Header field (daisy-chains extension headers)</td></tr>
                </tbody>
              </table>
            </div>
            <p style="margin-top:0.6rem;"><strong>Part 2: Role of ICMP Messages in IP Communication:</strong></p>
            <p>Since IP is a best-effort, connectionless network layer protocol lacking built-in error reporting, <strong>ICMPv4 (RFC 792)</strong> operates alongside IP to provide:</p>
            <ul>
              <li><strong>Error Reporting:</strong> Informs the sending host when a packet cannot be delivered (e.g., <em>Type 3: Destination Unreachable</em>, <em>Type 11: Time to Live Exceeded</em> during routing loops/traceroute, <em>Type 12: Parameter Problem</em>, <em>Type 4: Source Quench</em>).</li>
              <li><strong>Diagnostic Queries:</strong> Enables reachability and latency testing via <em>Type 8: Echo Request</em> and <em>Type 0: Echo Reply</em> (ping utility), as well as timestamping for clock synchronization.</li>
            </ul>
          </div>
        </div>

        <!-- CIE-2 Q1(c) -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (2025) &bull; Q 1(c)</span>
            <span class="archive-marks">[5 Marks &bull; Blooms L2, CO3]</span>
          </div>
          <p class="archive-q">"What are well-known, registered, and dynamic port numbers? Explain with examples."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p>Port numbers are 16-bit integers ($0 \text{ to } 65,535$) used by transport-layer protocols (TCP and UDP) to identify specific application processes on an IP host. IANA divides the port number space into three distinct ranges:</p>
            <ul>
              <li><strong>1. Well-Known Ports ($0 \text{ to } 1023$):</strong> Assigned and controlled strictly by IANA for standard universal server services. Requires superuser/root privileges to bind on UNIX systems. <em>Examples:</em> Port 20/21 (FTP), Port 22 (SSH), Port 25 (SMTP), Port 53 (DNS), Port 80 (HTTP), Port 443 (HTTPS).</li>
              <li><strong>2. Registered Ports ($1024 \text{ to } 49,151$):</strong> Not strictly assigned for universal services, but registered with IANA to avoid duplicate usage by vendor applications. <em>Examples:</em> Port 1433 (Microsoft SQL Server), Port 3306 (MySQL), Port 5432 (PostgreSQL), Port 8080 (HTTP Alternate / Apache Tomcat).</li>
              <li><strong>3. Dynamic / Private / Ephemeral Ports ($49,152 \text{ to } 65,535$):</strong> Neither controlled nor registered by IANA. Automatically and temporarily allocated by the client operating system to initiate outbound client connections. Deallocated immediately once the socket connection terminates.</li>
            </ul>
          </div>
        </div>

        <!-- CIE-2 Q2(a) -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (2025) &bull; Q 2(a)</span>
            <span class="archive-marks">[7 Marks &bull; Blooms L2, CO3]</span>
          </div>
          <p class="archive-q">"Explain Network Address Translation (NAT). Illustrate address translation table with private and public IP mappings."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Network Address Translation (NAT, RFC 3022):</strong> A routing technique that modifies network address information in the IP packet header while in transit across a traffic routing device. It enables an entire private local network (using RFC 1918 blocks such as <code>192.168.0.0/16</code> or <code>10.0.0.0/8</code>) to share a single or small pool of globally unique public IPv4 addresses.</p>
            <p><strong>Network Address Port Translation (NAPT / IP Masquerading) Operation:</strong></p>
            <p>When multiple private hosts communicate concurrently with the outside Internet, the NAT gateway tracks connections using both the IP address and the transport layer port number:</p>
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr><th>Private Source (LAN)</th><th>NAT Public Source (WAN)</th><th>External Destination</th><th>Protocol</th></tr>
                </thead>
                <tbody>
                  <tr><td><code>192.168.1.10:45000</code></td><td><code>203.0.113.1:50001</code></td><td><code>198.51.100.2:80</code> (Web)</td><td>TCP</td></tr>
                  <tr><td><code>192.168.1.11:45000</code></td><td><code>203.0.113.1:50002</code></td><td><code>198.51.100.2:80</code> (Web)</td><td>TCP</td></tr>
                  <tr><td><code>192.168.1.10:52140</code></td><td><code>203.0.113.1:50003</code></td><td><code>8.8.8.8:53</code> (DNS)</td><td>UDP</td></tr>
                </tbody>
              </table>
            </div>
            <p style="margin-top:0.6rem;"><strong>Translation Steps:</strong></p>
            <ol>
              <li><strong>Outbound Packet:</strong> Host <code>192.168.1.10</code> sends packet to web server. Router replaces source IP <code>192.168.1.10</code> with public IP <code>203.0.113.1</code> and source port <code>45000</code> with temporary translation port <code>50001</code>, recalculating the IP header checksum.</li>
              <li><strong>Inbound Reply:</strong> Web server replies to <code>203.0.113.1:50001</code>. The router looks up port <code>50001</code> in its translation table, restores destination to <code>192.168.1.10:45000</code>, recalculates checksums, and forwards to the internal host.</li>
            </ol>
          </div>
        </div>

        <!-- CIE-2 Q2(b) -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (2025) &bull; Q 2(b)</span>
            <span class="archive-marks">[8 Marks &bull; Blooms L3, CO3]</span>
          </div>
          <p class="archive-q">"Contrast Distance Vector Routing with Link State Routing. Explain the count-to-infinity problem and its solutions (Split Horizon, Poison Reverse)."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Comparison Table:</strong></p>
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr><th>Dimension</th><th>Distance Vector Routing (e.g., RIP)</th><th>Link State Routing (e.g., OSPF)</th></tr>
                </thead>
                <tbody>
                  <tr><td><strong>Underlying Algorithm</strong></td><td>Distributed Bellman-Ford algorithm</td><td>Dijkstra's Shortest Path First (SPF) algorithm</td></tr>
                  <tr><td><strong>Knowledge Scope</strong></td><td>Knows only direct neighbors and their vectors ("routing by rumor")</td><td>Every router knows full global network topology</td></tr>
                  <tr><td><strong>Updates Sent</strong></td><td>Sends entire routing table periodically (e.g. 30s)</td><td>Sends Link-State Advertisements (LSAs) only when changes occur</td></tr>
                  <tr><td><strong>Convergence Speed</strong></td><td>Slow convergence; vulnerable to routing loops</td><td>Very fast convergence; loop-free SPF calculation</td></tr>
                  <tr><td><strong>Memory &amp; CPU</strong></td><td>Low memory and minimal computational overhead</td><td>High memory for LSDB link database; high CPU for Dijkstra run</td></tr>
                </tbody>
              </table>
            </div>
            <p style="margin-top:0.6rem;"><strong>The Count-to-Infinity Problem:</strong></p>
            <p>Occurs when a link fails (e.g., link A–B fails). Node B detects failure, but Node C still advertises that it can reach A with cost 2 (via B). Node B mistakenly updates its route to A via C with cost $1 + 2 = 3$. In the next round, C updates its cost to $1 + 3 = 4$, and this mutual reinforcement increments endlessly until metric reaches $\infty$ (in RIP, $\infty = 16$).</p>
            <p><strong>Solutions:</strong></p>
            <ul>
              <li><strong>Split Horizon:</strong> A router never advertises a route back out of the interface through which it learned that route. Since C learned the route to A from B, C never advertises A back to B.</li>
              <li><strong>Poison Reverse:</strong> Instead of omitting the route, C explicitly advertises the route back to B with a metric of $\infty$ ($16$), immediately breaking the loop.</li>
            </ul>
          </div>
        </div>

        <!-- CIE-2 Q2(c) -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (2025) &bull; Q 2(c)</span>
            <span class="archive-marks">[5 Marks &bull; Blooms L3, CO4]</span>
          </div>
          <p class="archive-q">"Explain TCP congestion control mechanisms: Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery (TCP Tahoe vs Reno)."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p>TCP maintains a congestion window ($\text{cwnd}$) and slow-start threshold ($\text{ssthresh}$) to prevent network collapse:</p>
            <ul>
              <li><strong>1. Slow Start:</strong> Begins with $\text{cwnd} = 1\text{ MSS}$. For every ACK received, $\text{cwnd}$ increments by 1 MSS, causing exponential growth ($\text{cwnd}$ doubles each RTT: $1 \to 2 \to 4 \to 8$). Continues until $\text{cwnd} \ge \text{ssthresh}$.</li>
              <li><strong>2. Congestion Avoidance:</strong> Once $\text{cwnd} \ge \text{ssthresh}$, growth switches to linear (Additive Increase: $+1\text{ MSS}$ per RTT) to probe channel capacity conservatively.</li>
              <li><strong>3. Fast Retransmit:</strong> When sender receives 3 duplicate ACKs for the same segment, it assumes the packet was lost and retransmits immediately without waiting for the retransmission timeout (RTO).</li>
              <li><strong>4. Fast Recovery (Tahoe vs Reno):</strong>
                <ul>
                  <li><strong>TCP Tahoe:</strong> On packet loss (timeout OR 3 dup ACKs), sets $\text{ssthresh} = \text{cwnd} / 2$ and resets $\text{cwnd} = 1\text{ MSS}$, falling back into Slow Start.</li>
                  <li><strong>TCP Reno:</strong> On 3 duplicate ACKs, sets $\text{ssthresh} = \text{cwnd} / 2$ and sets $\text{cwnd} = \text{ssthresh} + 3\text{ MSS}$ (Fast Recovery), avoiding the severe penalty of dropping back to 1 MSS. On timeout, Reno still drops to $\text{cwnd} = 1\text{ MSS}$.</li>
                </ul>
              </li>
            </ul>
          </div>
        </div>

        <!-- CIE-2 Q3(a) -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (2025) &bull; Q 3(a)</span>
            <span class="archive-marks">[10 Marks &bull; Blooms L3, CO3]</span>
          </div>
          <p class="archive-q">"Given the 6-node network graph (Nodes A, B, C, D, E, F with edge costs: A-B=2, A-C=4, B-C=1, B-D=7, C-E=3, D-E=2, D-F=1, E-F=5), execute Dijkstra's algorithm from source node A. Show the step-by-step permanent and temporary label updates and determine the shortest path tree."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p><strong>Step-by-Step Execution of Dijkstra's Algorithm (Source = A):</strong></p>
            <p>Let $N'$ be the set of nodes permanently resolved, and $D(v)$ be the current minimum path cost from source A to node $v$:</p>
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr><th>Step</th><th>$N'$ (Visited)</th><th>$D(B), p(B)$</th><th>$D(C), p(C)$</th><th>$D(D), p(D)$</th><th>$D(E), p(E)$</th><th>$D(F), p(F)$</th><th>Selected Min</th></tr>
                </thead>
                <tbody>
                  <tr><td>0 (Init)</td><td>{A}</td><td><strong>2, A</strong></td><td>4, A</td><td>&infin;</td><td>&infin;</td><td>&infin;</td><td>Select B ($D=2$)</td></tr>
                  <tr><td>1</td><td>{A, B}</td><td>2, A</td><td><strong>3, B</strong></td><td>9, B</td><td>&infin;</td><td>&infin;</td><td>Select C ($D=3$)</td></tr>
                  <tr><td>2</td><td>{A, B, C}</td><td>2, A</td><td>3, B</td><td>9, B</td><td><strong>6, C</strong></td><td>&infin;</td><td>Select E ($D=6$)</td></tr>
                  <tr><td>3</td><td>{A, B, C, E}</td><td>2, A</td><td>3, B</td><td><strong>8, E</strong></td><td>6, C</td><td>11, E</td><td>Select D ($D=8$)</td></tr>
                  <tr><td>4</td><td>{A, B, C, E, D}</td><td>2, A</td><td>3, B</td><td>8, E</td><td>6, C</td><td><strong>9, D</strong></td><td>Select F ($D=9$)</td></tr>
                  <tr><td>5 (Done)</td><td>{A, B, C, E, D, F}</td><td>2, A</td><td>3, B</td><td>8, E</td><td>6, C</td><td>9, D</td><td>All Resolved</td></tr>
                </tbody>
              </table>
            </div>
            <p style="margin-top:0.6rem;"><strong>Final Shortest Path Results from Source A:</strong></p>
            <ul>
              <li><strong>Node B:</strong> Path: $\text{A} \to \text{B}$, Total Cost = $\mathbf{2}$</li>
              <li><strong>Node C:</strong> Path: $\text{A} \to \text{B} \to \text{C}$, Total Cost = $2 + 1 = \mathbf{3}$ (beats direct link cost 4)</li>
              <li><strong>Node E:</strong> Path: $\text{A} \to \text{B} \to \text{C} \to \text{E}$, Total Cost = $3 + 3 = \mathbf{6}$</li>
              <li><strong>Node D:</strong> Path: $\text{A} \to \text{B} \to \text{C} \to \text{E} \to \text{D}$, Total Cost = $6 + 2 = \mathbf{8}$ (beats path via B with cost 9)</li>
              <li><strong>Node F:</strong> Path: $\text{A} \to \text{B} \to \text{C} \to \text{E} \to \text{D} \to \text{F}$, Total Cost = $8 + 1 = \mathbf{9}$ (beats path via E with cost 11)</li>
            </ul>
          </div>
        </div>

        <!-- CIE-2 Q3(b) -->
        <div class="archive-item">
          <div class="archive-header">
            <span class="archive-source">Ramaiah Internal Assessment - II (2025) &bull; Q 3(b)</span>
            <span class="archive-marks">[10 Marks &bull; Blooms L2, CO3]</span>
          </div>
          <p class="archive-q">"Discuss the transition mechanisms from IPv4 to IPv6: Dual Stack, Tunneling, and Header Translation."</p>
          <div class="archive-answer" style="margin-top:0.6rem; font-size:14.5px; line-height:1.6;">
            <p>Because the global Internet cannot be upgraded from IPv4 to IPv6 overnight, the IETF standardized three fundamental co-existence strategies:</p>
            <ol>
              <li><strong>1. Dual Stack (RFC 4213):</strong>
                <ul>
                  <li>Hosts and routers run both IPv4 and IPv6 protocol stacks simultaneously on the same physical interfaces.</li>
                  <li>When an application initiates communication, DNS queries return both an A record (IPv4) and an AAAA record (IPv6). If IPv6 is available, the client prioritizes the IPv6 stack; otherwise, it falls back seamlessly to IPv4.</li>
                  <li><em>Advantage:</em> Cleanest migration mechanism; no protocol translation overhead.</li>
                </ul>
              </li>
              <li><strong>2. Tunneling (e.g., 6to4, 6in4, Teredo):</strong>
                <ul>
                  <li>Used when two IPv6 nodes or networks must communicate across an intervening IPv4-only transit network.</li>
                  <li>The ingress border router encapsulates the entire IPv6 datagram as payload inside an IPv4 datagram (Protocol 41). The packet traverses the IPv4 network as normal traffic.</li>
                  <li>The egress border router decapsulates the packet, strips the IPv4 header, and forwards the native IPv6 packet to the destination.</li>
                </ul>
              </li>
              <li><strong>3. Header Translation (NAT-PT / SIIT / NAT64):</strong>
                <ul>
                  <li>Required when an IPv6-only host must communicate directly with an IPv4-only host that cannot be upgraded.</li>
                  <li>The translator device strips the IPv6 header and synthesizes an equivalent IPv4 header (mapping 128-bit addresses to 32-bit addresses and adjusting total length, TTL/Hop Limit, and checksums).</li>
                  <li><em>Limitation:</em> Information loss can occur because IPv6 lacks certain IPv4 header fields, and applications with embedded IP addresses (like FTP) require Application Layer Gateways (ALGs).</li>
                </ul>
              </li>
            </ol>
          </div>
        </div>
      </section>'''

    # 7. PRACTICE PROBLEMS SECTION
    practice_section = '''      <section id="practice-problems" class="note-section">
        <div class="section-badge">&nabla; PRACTICE</div>
        <h2 class="section-title">Practice Problems with Step-by-Step Solutions</h2>
        <p class="section-lead">Test your understanding with these exam-level numericals. Click each collapsible card to reveal the complete verified solution:</p>

        <!-- Problem 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PROBLEM 1 &bull; CIDR ADDRESSING</span>
          </div>
          <h4 class="problem-title">An organization is assigned the CIDR block <code>198.51.100.160/26</code>. Determine: (a) Subnet Mask in dotted decimal, (b) Network Address, (c) Broadcast Address, and (d) Range of usable host IP addresses.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>Step 1: Subnet Mask</strong></p>
              <p>Prefix length $n = 26$. First 3 octets are all 1s (24 bits). 4th octet has 2 ones ($11000000_2 = 192_{10}$).</p>
              $$\text{Subnet Mask} = \mathbf{255.255.255.192}$$
              <p><strong>Step 2: Network Address</strong></p>
              <p>Bitwise AND on 4th octet: $160_{10} = 10100000_2$. $10100000_2 \text{ AND } 11000000_2 = 10000000_2 = 128_{10}$.</p>
              $$\text{Network Address} = \mathbf{198.51.100.128}$$
              <p><strong>Step 3: Broadcast Address</strong></p>
              <p>Host bits $h = 32 - 26 = 6$. Total addresses in block $= 2^6 = 64$. Broadcast $= 128 + 64 - 1 = 191$.</p>
              $$\text{Broadcast Address} = \mathbf{198.51.100.191}$$
              <p><strong>Step 4: Usable Host Range</strong></p>
              $$\text{Usable Hosts} = \mathbf{198.51.100.129 \text{ to } 198.51.100.190} \quad (\text{Total: } 64 - 2 = \mathbf{62\text{ hosts}})$$
            </div>
          </details>
        </div>

        <!-- Problem 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PROBLEM 2 &bull; VLSM ALLOCATION</span>
          </div>
          <h4 class="problem-title">An enterprise base block is <code>192.168.10.0/24</code>. Allocate subnets for three departments: Dept A (60 hosts), Dept B (28 hosts), and Dept C (12 hosts). Specify network address, mask, and host range for each.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Always allocate starting from the largest requirement:</p>
              <ul>
                <li><strong>Dept A (60 hosts):</strong> Needs $60 + 2 = 62$ addresses. Nearest power of 2 is $2^6 = 64$ ($h=6$). Subnet prefix: $32 - 6 = \mathbf{/26}$ (Mask <code>255.255.255.192</code>).
                  <br>&bull; Network: <code>192.168.10.0/26</code>, Range: <code>192.168.10.1 - 192.168.10.62</code>, Broadcast: <code>192.168.10.63</code>.
                </li>
                <li><strong>Dept B (28 hosts):</strong> Needs $28 + 2 = 30$ addresses. Nearest power of 2 is $2^5 = 32$ ($h=5$). Subnet prefix: $32 - 5 = \mathbf{/27}$ (Mask <code>255.255.255.224</code>).
                  <br>&bull; Starts at next free boundary: <code>192.168.10.64/27</code>, Range: <code>192.168.10.65 - 192.168.10.94</code>, Broadcast: <code>192.168.10.95</code>.
                </li>
                <li><strong>Dept C (12 hosts):</strong> Needs $12 + 2 = 14$ addresses. Nearest power of 2 is $2^4 = 16$ ($h=4$). Subnet prefix: $32 - 4 = \mathbf{/28}$ (Mask <code>255.255.255.240</code>).
                  <br>&bull; Starts at next free boundary: <code>192.168.10.96/28</code>, Range: <code>192.168.10.97 - 192.168.10.110</code>, Broadcast: <code>192.168.10.111</code>.
                </li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PROBLEM 3 &bull; IP FRAGMENTATION</span>
          </div>
          <h4 class="problem-title">An IPv4 packet with Total Length = 4000 bytes (20 bytes header, 3980 bytes payload) arrives at an outgoing link with MTU = 1500 bytes. Calculate the parameters (Total Length, Data Size, Offset, DF, and MF) for all fragments.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Max payload per fragment $= 1500 - 20 = 1480$ bytes. Notice $1480$ is divisible by 8 ($1480 / 8 = 185$).</p>
              <ul>
                <li><strong>Fragment 1:</strong>
                  <br>&bull; Data: 1480 bytes (bytes 0 to 1479).
                  <br>&bull; Total Length: $1480 + 20 = \mathbf{1500\text{ bytes}}$.
                  <br>&bull; Fragment Offset: $0 / 8 = \mathbf{0}$.
                  <br>&bull; Flags: $\text{DF} = 0, \text{MF} = \mathbf{1}$.
                </li>
                <li><strong>Fragment 2:</strong>
                  <br>&bull; Data: 1480 bytes (bytes 1480 to 2959).
                  <br>&bull; Total Length: $1480 + 20 = \mathbf{1500\text{ bytes}}$.
                  <br>&bull; Fragment Offset: $1480 / 8 = \mathbf{185}$.
                  <br>&bull; Flags: $\text{DF} = 0, \text{MF} = \mathbf{1}$.
                </li>
                <li><strong>Fragment 3:</strong>
                  <br>&bull; Remaining Data: $3980 - (1480 + 1480) = 1020$ bytes (bytes 2960 to 3979).
                  <br>&bull; Total Length: $1020 + 20 = \mathbf{1040\text{ bytes}}$.
                  <br>&bull; Fragment Offset: $2960 / 8 = \mathbf{370}$.
                  <br>&bull; Flags: $\text{DF} = 0, \text{MF} = \mathbf{0}$ (Last fragment).
                </li>
              </ul>
            </div>
          </details>
        </div>

        <!-- Problem 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PROBLEM 4 &bull; TRANSMISSION VS PROPAGATION DELAY</span>
          </div>
          <h4 class="problem-title">A 1500-byte packet is sent over a 2500 km fiber-optic cable ($v = 2 \times 10^8\text{ m/s}$) at transmission rate $R = 1\text{ Gbps}$. Calculate $d_{trans}$, $d_{prop}$, and determine whether the link is latency-dominated or bandwidth-dominated.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>1. Transmission Delay:</strong></p>
              $$L = 1500 \times 8 = 12,000\text{ bits}$$
              $$d_{trans} = \frac{L}{R} = \frac{12,000\text{ bits}}{10^9\text{ bps}} = 1.2 \times 10^{-5}\text{ s} = \mathbf{12\text{ }\mu\text{s}}$$
              <p><strong>2. Propagation Delay:</strong></p>
              $$d = 2,500\text{ km} = 2.5 \times 10^6\text{ m}$$
              $$d_{prop} = \frac{d}{v} = \frac{2.5 \times 10^6}{2 \times 10^8} = 0.0125\text{ s} = \mathbf{12.5\text{ ms}} = \mathbf{12,500\text{ }\mu\text{s}}$$
              <p><strong>3. Latency Regime:</strong></p>
              $$d_{prop} / d_{trans} = 12,500 / 12 \approx \mathbf{1041.7}$$
              <p>Since propagation delay exceeds transmission delay by over $1000\times$, this long-haul link is heavily <strong>propagation/latency-dominated</strong>.</p>
            </div>
          </details>
        </div>

        <!-- Problem 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PROBLEM 5 &bull; DIJKSTRA SHORTEST PATH</span>
          </div>
          <h4 class="problem-title">In a diamond network with nodes W, X, Y, Z and bidirectional edge costs W-X=3, W-Y=5, X-Y=1, X-Z=6, Y-Z=2, determine the shortest path and cost from W to Z using Dijkstra's algorithm.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>Execution Trace from Source W:</strong></p>
              <ol>
                <li>Init: $D(X)=3, D(Y)=5, D(Z)=\infty$. Min is $X$ ($D=3$). Permanent: $\{W, X\}$.</li>
                <li>From X: update $D(Y) = \min(5, 3 + 1) = \mathbf{4}$ via X. Update $D(Z) = \min(\infty, 3 + 6) = 9$ via X. Min is $Y$ ($D=4$). Permanent: $\{W, X, Y\}$.</li>
                <li>From Y: update $D(Z) = \min(9, 4 + 2) = \mathbf{6}$ via Y. Min is $Z$ ($D=6$). Permanent: $\{W, X, Y, Z\}$.</li>
              </ol>
              $$\text{Shortest Path: } \mathbf{W \to X \to Y \to Z} \quad \text{with Cost} = 3 + 1 + 2 = \mathbf{6}$$
            </div>
          </details>
        </div>

        <!-- Problem 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PROBLEM 6 &bull; ICMP ERROR CODE ANALYSIS</span>
          </div>
          <h4 class="problem-title">A host runs traceroute to a target server. (a) What ICMP error message is generated by intermediate routers? (b) What ICMP error message is generated by the destination host when the probe reaches it?</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>(a) Intermediate Routers:</strong></p>
              <p>The host sends UDP probe packets with incrementally increasing TTL values ($TTL = 1, 2, 3 \dots$). When router hop $k$ decrements TTL to 0, it drops the packet and transmits back to the source:</p>
              $$\mathbf{\text{ICMP Type 11, Code 0: Time to Live Exceeded in Transit}}$$
              <p><strong>(b) Destination Host:</strong></p>
              <p>The packet reaches the final destination with TTL &gt; 0. Because the traceroute client targets an intentionally unused high UDP port (e.g., 33434+), the destination host's transport layer cannot deliver the datagram and returns:</p>
              $$\mathbf{\text{ICMP Type 3, Code 3: Destination Unreachable (Port Unreachable)}}$$
            </div>
          </details>
        </div>
      </section>'''

    # Replace questions-asked-before
    arch_m = re.search(r'(<section id="questions-asked-before".*?</section>)', html, re.DOTALL)
    if arch_m:
        html = html[:arch_m.start(1)] + archive_section + html[arch_m.end(1):]

    # Replace practice-problems
    prac_m = re.search(r'(<section id="practice-problems".*?</section>)', html, re.DOTALL)
    if prac_m:
        html = html[:prac_m.start(1)] + practice_section + html[prac_m.end(1):]

    html = html.replace('height="auto"', 'height="300"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"CN Unit 3 enriched successfully! File size: {len(html)} bytes")

def cidR_content(fig, interactive):
    return f"{fig}\n\n{interactive}"

if __name__ == "__main__":
    build()
