"""
generate_cn_u3_assets.py - Generates theme-aware SVG diagrams for CN Unit 3:
1. IPv4 20-Byte Datagram Header Layout (RFC 791)
2. CIDR Bit Breakdown & Subnet Address Space Diagram
3. Link State / Dijkstra's 6-Node Shortest Path Graph (Ramaiah CIE-2 Q3.a)
4. NAT Network Address Translation Flow Diagram (Ramaiah CIE-2 Q2.a)
"""

def generate_ipv4_header_svg():
    return '''<svg viewBox="0 0 800 360" width="100%" height="360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="IPv4 20-Byte Datagram Header Layout">
  <defs>
    <style>
      .hdr-bg { fill: var(--surface-alt); stroke: var(--border); stroke-width: 1.5; }
      .hdr-field { stroke: var(--border); stroke-width: 1.2; }
      .field-f1 { fill: rgba(46, 195, 107, 0.12); }
      .field-f2 { fill: rgba(59, 130, 246, 0.12); }
      .field-f3 { fill: rgba(245, 158, 11, 0.12); }
      .field-f4 { fill: rgba(139, 92, 246, 0.12); }
      .hdr-title { font-family: var(--font-sans); font-size: 13px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .hdr-sub { font-family: var(--font-mono); font-size: 11px; fill: var(--ink-muted); text-anchor: middle; dominant-baseline: middle; }
      .hdr-bit { font-family: var(--font-mono); font-size: 10.5px; font-weight: 600; fill: var(--ink-muted); text-anchor: middle; }
      .row-label { font-family: var(--font-mono); font-size: 11.5px; font-weight: 600; fill: var(--ink-muted); text-anchor: end; }
    </style>
  </defs>

  <!-- Bit number indicators 0 to 31 -->
  <g transform="translate(100, 24)">
    <text x="0" y="0" class="hdr-bit" text-anchor="start">Bit 0</text>
    <text x="85" y="0" class="hdr-bit">3</text>
    <text x="95" y="0" class="hdr-bit">4</text>
    <text x="175" y="0" class="hdr-bit">7</text>
    <text x="185" y="0" class="hdr-bit">8</text>
    <text x="350" y="0" class="hdr-bit">15</text>
    <text x="365" y="0" class="hdr-bit">16</text>
    <text x="425" y="0" class="hdr-bit">18</text>
    <text x="435" y="0" class="hdr-bit">19</text>
    <text x="670" y="0" class="hdr-bit" text-anchor="end">Bit 31</text>
  </g>

  <!-- Main grid table -->
  <g transform="translate(100, 36)">
    <!-- Row 0: Bytes 0-3 -->
    <text x="-12" y="32" class="row-label">Bytes 0-3</text>
    <rect x="0" y="0" width="90" height="56" class="hdr-field field-f1"/>
    <text x="45" y="22" class="hdr-title">VER</text>
    <text x="45" y="38" class="hdr-sub">4 bits (0100)</text>

    <rect x="90" y="0" width="90" height="56" class="hdr-field field-f1"/>
    <text x="135" y="22" class="hdr-title">IHL</text>
    <text x="135" y="38" class="hdr-sub">4 bits (5 = 20B)</text>

    <rect x="180" y="0" width="180" height="56" class="hdr-field field-f2"/>
    <text x="270" y="22" class="hdr-title">Type of Service</text>
    <text x="270" y="38" class="hdr-sub">8 bits (DSCP/ECN)</text>

    <rect x="360" y="0" width="310" height="56" class="hdr-field field-f3"/>
    <text x="515" y="22" class="hdr-title">Total Length</text>
    <text x="515" y="38" class="hdr-sub">16 bits (Header + Data, max 65,535 B)</text>

    <!-- Row 1: Bytes 4-7 -->
    <text x="-12" y="92" class="row-label">Bytes 4-7</text>
    <rect x="0" y="60" width="360" height="56" class="hdr-field field-f2"/>
    <text x="180" y="82" class="hdr-title">Identification</text>
    <text x="180" y="98" class="hdr-sub">16 bits (Reassembly Token)</text>

    <rect x="360" y="60" width="70" height="56" class="hdr-field field-f4"/>
    <text x="395" y="82" class="hdr-title">Flags</text>
    <text x="395" y="98" class="hdr-sub">3 b (0,DF,MF)</text>

    <rect x="430" y="60" width="240" height="56" class="hdr-field field-f4"/>
    <text x="550" y="82" class="hdr-title">Fragment Offset</text>
    <text x="550" y="98" class="hdr-sub">13 bits (Units of 8 bytes)</text>

    <!-- Row 2: Bytes 8-11 -->
    <text x="-12" y="152" class="row-label">Bytes 8-11</text>
    <rect x="0" y="120" width="180" height="56" class="hdr-field field-f3"/>
    <text x="90" y="142" class="hdr-title">Time to Live (TTL)</text>
    <text x="90" y="158" class="hdr-sub">8 bits (Max 255 hops)</text>

    <rect x="180" y="120" width="180" height="56" class="hdr-field field-f1"/>
    <text x="270" y="142" class="hdr-title">Protocol</text>
    <text x="270" y="158" class="hdr-sub">8 b (1=ICMP, 6=TCP, 17=UDP)</text>

    <rect x="360" y="120" width="310" height="56" class="hdr-field field-f2"/>
    <text x="515" y="142" class="hdr-title">Header Checksum</text>
    <text x="515" y="158" class="hdr-sub">16 bits (1s Complement Sum of Header Only)</text>

    <!-- Row 3: Bytes 12-15 -->
    <text x="-12" y="212" class="row-label">Bytes 12-15</text>
    <rect x="0" y="180" width="670" height="56" class="hdr-field field-f1"/>
    <text x="335" y="202" class="hdr-title">Source IPv4 Address</text>
    <text x="335" y="218" class="hdr-sub">32 bits (4 Octets: A.B.C.D)</text>

    <!-- Row 4: Bytes 16-19 -->
    <text x="-12" y="272" class="row-label">Bytes 16-19</text>
    <rect x="0" y="240" width="670" height="56" class="hdr-field field-f1"/>
    <text x="335" y="262" class="hdr-title">Destination IPv4 Address</text>
    <text x="335" y="278" class="hdr-sub">32 bits (4 Octets: A.B.C.D)</text>
  </g>
</svg>'''

def generate_cidr_breakdown_svg():
    return '''<svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CIDR Subnet Bit Allocation and Address Range">
  <defs>
    <style>
      .cidr-box { stroke: var(--border); stroke-width: 1.5; rx: 8px; }
      .net-bits { fill: rgba(46, 195, 107, 0.15); stroke: var(--green); }
      .host-bits { fill: rgba(245, 158, 11, 0.15); stroke: #F59E0B; }
      .t-title { font-family: var(--font-sans); font-size: 13.5px; font-weight: 700; fill: var(--ink); text-anchor: middle; }
      .t-code { font-family: var(--font-mono); font-size: 12px; fill: var(--ink); text-anchor: middle; }
      .t-desc { font-family: var(--font-sans); font-size: 11px; fill: var(--ink-muted); text-anchor: middle; }
      .bracket { stroke: var(--ink-muted); stroke-width: 1.5; fill: none; }
    </style>
  </defs>

  <!-- Block title & IP Example -->
  <g transform="translate(380, 25)">
    <text class="t-title" y="0">Example CIDR Block: 200.16.70.82 / 27 (Subnet Mask: 255.255.255.224)</text>
    <text class="t-desc" y="18">Total 32 Bits = 27 Network Prefix Bits + 5 Host Identifier Bits</text>
  </g>

  <!-- Octet Blocks -->
  <g transform="translate(40, 65)">
    <!-- Octet 1 -->
    <rect x="0" y="0" width="150" height="50" class="cidr-box net-bits"/>
    <text x="75" y="22" class="t-code">200 (11001000)</text>
    <text x="75" y="38" class="t-desc">Octet 1 (8 Prefix Bits)</text>

    <!-- Octet 2 -->
    <rect x="165" y="0" width="150" height="50" class="cidr-box net-bits"/>
    <text x="240" y="22" class="t-code">16 (00010000)</text>
    <text x="240" y="38" class="t-desc">Octet 2 (8 Prefix Bits)</text>

    <!-- Octet 3 -->
    <rect x="330" y="0" width="150" height="50" class="cidr-box net-bits"/>
    <text x="405" y="22" class="t-code">70 (01000110)</text>
    <text x="405" y="38" class="t-desc">Octet 3 (8 Prefix Bits)</text>

    <!-- Octet 4 Split (3 bits net, 5 bits host) -->
    <rect x="495" y="0" width="80" height="50" class="cidr-box net-bits"/>
    <text x="535" y="22" class="t-code">010</text>
    <text x="535" y="38" class="t-desc">3 Prefix b</text>

    <rect x="580" y="0" width="100" height="50" class="cidr-box host-bits"/>
    <text x="630" y="22" class="t-code">10010</text>
    <text x="630" y="38" class="t-desc">5 Host Bits</text>
  </g>

  <!-- Summary Cards -->
  <g transform="translate(40, 140)">
    <!-- Network Address -->
    <rect x="0" y="0" width="160" height="65" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2"/>
    <text x="80" y="20" class="t-title" font-size="12">Network Address</text>
    <text x="80" y="40" class="t-code" fill="var(--green)" font-weight="700">200.16.70.64</text>
    <text x="80" y="55" class="t-desc">Host bits = all 0s</text>

    <!-- First Usable -->
    <rect x="173" y="0" width="160" height="65" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2"/>
    <text x="253" y="20" class="t-title" font-size="12">First Usable Host</text>
    <text x="253" y="40" class="t-code" font-weight="700">200.16.70.65</text>
    <text x="253" y="55" class="t-desc">Network + 1</text>

    <!-- Last Usable -->
    <rect x="346" y="0" width="160" height="65" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2"/>
    <text x="426" y="20" class="t-title" font-size="12">Last Usable Host</text>
    <text x="426" y="40" class="t-code" font-weight="700">200.16.70.94</text>
    <text x="426" y="55" class="t-desc">Broadcast - 1</text>

    <!-- Broadcast -->
    <rect x="520" y="0" width="160" height="65" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2"/>
    <text x="600" y="20" class="t-title" font-size="12">Broadcast Address</text>
    <text x="600" y="40" class="t-code" fill="#B91C1C" font-weight="700">200.16.70.95</text>
    <text x="600" y="55" class="t-desc">Host bits = all 1s (30 Hosts)</text>
  </g>
</svg>'''

def generate_dijkstra_graph_svg():
    return '''<svg viewBox="0 0 740 320" width="100%" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dijkstra Shortest Path 6-Node Graph (Ramaiah CIE-2 Q3.a)">
  <defs>
    <style>
      .edge { stroke: var(--border); stroke-width: 2.2; }
      .shortest-edge { stroke: var(--green); stroke-width: 4; stroke-linecap: round; }
      .node-circle { fill: var(--surface); stroke: var(--border); stroke-width: 2.5; }
      .node-source { fill: rgba(46, 195, 107, 0.2); stroke: var(--green); stroke-width: 3.5; }
      .node-txt { font-family: var(--font-sans); font-size: 16px; font-weight: 800; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .cost-bg { fill: var(--surface); rx: 4px; stroke: var(--border); stroke-width: 1; }
      .cost-txt { font-family: var(--font-mono); font-size: 12px; font-weight: 700; fill: var(--ink); text-anchor: middle; dominant-baseline: middle; }
      .tree-cost { fill: var(--green); font-weight: 800; }
      .dist-tag { font-family: var(--font-mono); font-size: 11px; font-weight: 700; fill: var(--green); text-anchor: middle; }
    </style>
  </defs>

  <!-- Edges -->
  <line x1="100" y1="160" x2="250" y2="70" class="shortest-edge"/>
  <line x1="100" y1="160" x2="250" y2="250" class="edge"/>
  <line x1="250" y1="70" x2="250" y2="250" class="shortest-edge"/>
  <line x1="250" y1="70" x2="470" y2="70" class="edge"/>
  <line x1="250" y1="250" x2="470" y2="250" class="shortest-edge"/>
  <line x1="470" y1="250" x2="470" y2="70" class="shortest-edge"/>
  <line x1="470" y1="70" x2="640" y2="160" class="shortest-edge"/>
  <line x1="470" y1="250" x2="640" y2="160" class="edge"/>

  <!-- Cost Badges -->
  <rect x="160" y="103" width="24" height="18" class="cost-bg"/>
  <text x="172" y="112" class="cost-txt tree-cost">2</text>

  <rect x="160" y="193" width="24" height="18" class="cost-bg"/>
  <text x="172" y="202" class="cost-txt">4</text>

  <rect x="238" y="151" width="24" height="18" class="cost-bg"/>
  <text x="250" y="160" class="cost-txt tree-cost">1</text>

  <rect x="348" y="61" width="24" height="18" class="cost-bg"/>
  <text x="360" y="70" class="cost-txt">7</text>

  <rect x="348" y="241" width="24" height="18" class="cost-bg"/>
  <text x="360" y="250" class="cost-txt tree-cost">3</text>

  <rect x="458" y="151" width="24" height="18" class="cost-bg"/>
  <text x="470" y="160" class="cost-txt tree-cost">2</text>

  <rect x="543" y="103" width="24" height="18" class="cost-bg"/>
  <text x="555" y="112" class="cost-txt tree-cost">1</text>

  <rect x="543" y="193" width="24" height="18" class="cost-bg"/>
  <text x="555" y="202" class="cost-txt">5</text>

  <!-- Nodes -->
  <circle cx="100" cy="160" r="28" class="node-circle node-source"/>
  <text x="100" y="160" class="node-txt">A</text>
  <text x="100" y="205" class="dist-tag">[Dist: 0]</text>

  <circle cx="250" cy="70" r="28" class="node-circle"/>
  <text x="250" y="70" class="node-txt">B</text>
  <text x="250" y="32" class="dist-tag">[Dist: 2 via A]</text>

  <circle cx="250" cy="250" r="28" class="node-circle"/>
  <text x="250" y="250" class="node-txt">C</text>
  <text x="250" y="295" class="dist-tag">[Dist: 3 via B]</text>

  <circle cx="470" cy="70" r="28" class="node-circle"/>
  <text x="470" y="70" class="node-txt">D</text>
  <text x="470" y="32" class="dist-tag">[Dist: 8 via E]</text>

  <circle cx="470" cy="250" r="28" class="node-circle"/>
  <text x="470" y="250" class="node-txt">E</text>
  <text x="470" y="295" class="dist-tag">[Dist: 6 via C]</text>

  <circle cx="640" cy="160" r="28" class="node-circle"/>
  <text x="640" y="160" class="node-txt">F</text>
  <text x="640" y="205" class="dist-tag">[Dist: 9 via D]</text>
</svg>'''

def generate_nat_flow_svg():
    return '''<svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="NAT Network Address Translation Flow and Mapping Table (Ramaiah CIE-2 Q2.a)">
  <defs>
    <style>
      .nat-box { fill: var(--surface-alt); stroke: var(--border); stroke-width: 1.5; rx: 8px; }
      .nat-router { fill: rgba(46, 195, 107, 0.12); stroke: var(--green); stroke-width: 2; rx: 8px; }
      .flow-arrow { stroke: var(--ink); stroke-width: 1.8; marker-end: url(#nat-head); }
      .flow-txt { font-family: var(--font-mono); font-size: 10.5px; fill: var(--ink); text-anchor: middle; }
      .nat-title { font-family: var(--font-sans); font-size: 13px; font-weight: 700; fill: var(--ink); text-anchor: middle; }
      .nat-sub { font-family: var(--font-mono); font-size: 11px; fill: var(--ink-muted); text-anchor: middle; }
    </style>
    <marker id="nat-head" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink)"/>
    </marker>
  </defs>

  <!-- Private Host A (Left: x=15 to 145) -->
  <rect x="15" y="55" width="130" height="90" class="nat-box"/>
  <text x="80" y="85" class="nat-title">Private Host A</text>
  <text x="80" y="105" class="nat-sub">192.168.1.10</text>
  <text x="80" y="125" class="nat-sub" fill="var(--green)">Port: 45000</text>

  <!-- NAT Router in Center (x=275 to 485) -->
  <rect x="275" y="35" width="210" height="135" class="nat-router"/>
  <text x="380" y="60" class="nat-title">NAT Router / Gateway</text>
  <text x="380" y="78" class="nat-sub">LAN IP: 192.168.1.1</text>
  <text x="380" y="94" class="nat-sub" font-weight="700">WAN Public: 203.0.113.1</text>

  <!-- NAT Translation Table Box -->
  <rect x="288" y="105" width="184" height="50" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1"/>
  <text x="380" y="122" class="nat-sub" font-weight="700">Translation Entry</text>
  <text x="380" y="140" class="nat-sub" fill="var(--green)">192.168.1.10:45000 &harr; :50001</text>

  <!-- Public Web Server B (Right: x=615 to 745) -->
  <rect x="615" y="55" width="130" height="90" class="nat-box"/>
  <text x="680" y="85" class="nat-title">Web Server B</text>
  <text x="680" y="105" class="nat-sub">198.51.100.2</text>
  <text x="680" y="125" class="nat-sub">HTTP Port: 80</text>

  <!-- Outbound Arrow (Top) -->
  <path d="M 145 80 L 275 80" class="flow-arrow"/>
  <text x="210" y="68" class="flow-txt">Src: 192.168.1.10</text>
  <text x="210" y="78" class="flow-txt">Port: 45000</text>

  <path d="M 485 80 L 615 80" class="flow-arrow"/>
  <text x="550" y="68" class="flow-txt">Src: 203.0.113.1</text>
  <text x="550" y="78" class="flow-txt">Port: 50001</text>

  <!-- Inbound Arrow (Bottom) -->
  <path d="M 615 120 L 485 120" class="flow-arrow"/>
  <text x="550" y="135" class="flow-txt">Dst: 203.0.113.1</text>
  <text x="550" y="145" class="flow-txt">Port: 50001</text>

  <path d="M 275 120 L 145 120" class="flow-arrow"/>
  <text x="210" y="135" class="flow-txt">Dst: 192.168.1.10</text>
  <text x="210" y="145" class="flow-txt">Port: 45000</text>
</svg>'''
