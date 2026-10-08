"""
generate_cn_u2_assets.py - Generates inline SVGs for CN Unit 2.
"""

def generate_crc_division_svg():
    return '''<svg viewBox="0 0 720 280" width="100%" height="280" role="img" aria-label="CRC Modulo-2 Polynomial Long Division Diagram">
  <title>CRC Modulo-2 Binary Division (Dataword: 101011, Divisor: 10011)</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />

  <text x="360" y="28" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">CRC Modulo-2 Binary Long Division (Sender FCS Generation)</text>
  <text x="360" y="48" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Dataword: 101011 &bull; Divisor G(x): 10011 (x^4 + x + 1) &bull; Appended: 101011 0000</text>

  <!-- Modulo-2 Division Box -->
  <g transform="translate(140, 70)" font-family="var(--font-mono)" font-size="13">
    <!-- Divisor -->
    <text x="0" y="20" fill="var(--green)" font-weight="700">10011</text>
    <!-- Division line / bracket -->
    <line x1="55" y1="5" x2="55" y2="180" stroke="var(--ink)" stroke-width="1.8" />
    <line x1="55" y1="5" x2="320" y2="5" stroke="var(--ink)" stroke-width="1.8" />

    <!-- Dividend -->
    <text x="65" y="20" fill="var(--ink)" font-weight="700">1010110000</text>
    <text x="235" y="20" fill="var(--ink-muted)">(Quotient: 101101)</text>

    <!-- Step 1 -->
    <text x="65" y="40" fill="var(--ink-muted)">10011</text>
    <line x1="65" y1="45" x2="150" y2="45" stroke="var(--border)" stroke-width="1" />
    <text x="95" y="60" fill="var(--ink)">01101</text>
    <text x="65" y="60" fill="var(--ink)">---&gt; 011011</text>

    <!-- Step 2 -->
    <text x="95" y="80" fill="var(--ink-muted)">10011</text>
    <line x1="95" y1="85" x2="180" y2="85" stroke="var(--border)" stroke-width="1" />
    <text x="125" y="100" fill="var(--ink)">010000</text>

    <!-- Step 3 -->
    <text x="125" y="120" fill="var(--ink-muted)">10011</text>
    <line x1="125" y1="125" x2="210" y2="125" stroke="var(--border)" stroke-width="1" />
    <text x="155" y="140" fill="var(--ink)">0001100</text>

    <!-- Final Remainder -->
    <text x="155" y="165" fill="#B91C1C" font-weight="700">Remainder (FCS) = 0100</text>
  </g>

  <!-- Codeword Box -->
  <g transform="translate(480, 85)">
    <rect x="0" y="0" width="200" height="130" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" rx="8" />
    <text x="100" y="24" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">Transmitted Codeword</text>
    
    <rect x="15" y="38" width="105" height="32" fill="rgba(46,195,107,0.15)" stroke="var(--green)" stroke-width="1.2" rx="4" />
    <text x="67" y="58" fill="var(--ink)" font-family="var(--font-mono)" font-size="12" font-weight="700" text-anchor="middle">101011</text>
    <text x="67" y="82" fill="var(--green)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Dataword (k=6)</text>

    <rect x="125" y="38" width="60" height="32" fill="rgba(185,28,28,0.15)" stroke="#B91C1C" stroke-width="1.2" rx="4" />
    <text x="155" y="58" fill="#B91C1C" font-family="var(--font-mono)" font-size="12" font-weight="700" text-anchor="middle">0100</text>
    <text x="155" y="82" fill="#B91C1C" font-family="var(--font-mono)" font-size="10" text-anchor="middle">FCS (r=4)</text>

    <text x="100" y="112" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">Receiver remainder: 0000 &check;</text>
  </g>

  <text x="360" y="262" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Ramaiah CIE-1 Q1(c) Solved: Codeword = 101011 0100 &bull; Modulo-2 polynomial division with degree 4 divisor</text>
</svg>'''

def generate_arp_packet_svg():
    return '''<svg viewBox="0 0 720 250" width="100%" height="250" role="img" aria-label="ARP Packet Format Diagram (28 Bytes Header)">
  <title>ARP Packet Layout (RFC 826)</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />

  <text x="360" y="26" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">ARP Packet Format (28 Octets for IPv4 over Ethernet)</text>

  <!-- Ruler (32 bits) -->
  <g font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)">
    <text x="40" y="44">bit 0</text>
    <text x="195" y="44">bit 8</text>
    <text x="360" y="44">bit 16</text>
    <text x="680" y="44" text-anchor="end">bit 31</text>
  </g>

  <!-- Row 1: Hardware Type (16) + Protocol Type (16) -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="315" height="32" fill="rgba(46,195,107,0.12)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="157" y="16" fill="var(--ink)" font-family="var(--font-display)" font-size="11.5" font-weight="700" text-anchor="middle">Hardware Type (HTYPE: 16 bits)</text>
    <text x="157" y="27" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="9.5" text-anchor="middle">Ethernet = 0x0001</text>

    <rect x="325" y="0" width="315" height="32" fill="rgba(37,99,235,0.12)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="482" y="16" fill="var(--ink)" font-family="var(--font-display)" font-size="11.5" font-weight="700" text-anchor="middle">Protocol Type (PTYPE: 16 bits)</text>
    <text x="482" y="27" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="9.5" text-anchor="middle">IPv4 = 0x0800</text>
  </g>

  <!-- Row 2: HLEN (8) + PLEN (8) + Operation (16) -->
  <g transform="translate(40, 86)">
    <rect x="0" y="0" width="155" height="32" fill="rgba(217,119,6,0.12)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="77" y="16" fill="var(--ink)" font-family="var(--font-display)" font-size="11" font-weight="700" text-anchor="middle">Hardware Len (8b)</text>
    <text x="77" y="27" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="9.5" text-anchor="middle">6 bytes (MAC)</text>

    <rect x="160" y="0" width="155" height="32" fill="rgba(124,58,237,0.12)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="237" y="16" fill="var(--ink)" font-family="var(--font-display)" font-size="11" font-weight="700" text-anchor="middle">Protocol Len (8b)</text>
    <text x="237" y="27" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="9.5" text-anchor="middle">4 bytes (IPv4)</text>

    <rect x="325" y="0" width="315" height="32" fill="rgba(46,195,107,0.12)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="482" y="16" fill="var(--ink)" font-family="var(--font-display)" font-size="11.5" font-weight="700" text-anchor="middle">Operation (OPER: 16 bits)</text>
    <text x="482" y="27" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="9.5" text-anchor="middle">1 = Request &bull; 2 = Reply</text>
  </g>

  <!-- Row 3: Sender Hardware Address (48 bits MAC: upper 32 bits + lower 16 bits in row 4) -->
  <g transform="translate(40, 122)">
    <rect x="0" y="0" width="640" height="32" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="320" y="20" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">Sender Hardware Address (SHA: bytes 0–3 of 6-byte MAC)</text>
  </g>

  <!-- Row 4: SHA remaining 16b + Sender IP upper 16b -->
  <g transform="translate(40, 158)">
    <rect x="0" y="0" width="315" height="32" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="157" y="20" fill="var(--ink)" font-family="var(--font-display)" font-size="11.5" font-weight="700" text-anchor="middle">SHA (bytes 4–5 of MAC)</text>

    <rect x="325" y="0" width="315" height="32" fill="rgba(37,99,235,0.12)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="482" y="20" fill="var(--ink)" font-family="var(--font-display)" font-size="11.5" font-weight="700" text-anchor="middle">Sender IP Address (SPA: 32 bits)</text>
  </g>

  <!-- Row 5: Target Hardware Address (48b) & Target IP Address (32b) -->
  <g transform="translate(40, 194)">
    <rect x="0" y="0" width="315" height="32" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="157" y="16" fill="var(--ink)" font-family="var(--font-display)" font-size="11.5" font-weight="700" text-anchor="middle">Target Hardware (THA: 48 bits)</text>
    <text x="157" y="27" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">All 0s in Request; Filled in Reply</text>

    <rect x="325" y="0" width="315" height="32" fill="rgba(37,99,235,0.12)" stroke="var(--border)" stroke-width="1.2" rx="3" />
    <text x="482" y="20" fill="var(--ink)" font-family="var(--font-display)" font-size="11.5" font-weight="700" text-anchor="middle">Target IP Address (TPA: 32 bits)</text>
  </g>

  <text x="360" y="242" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10.5" text-anchor="middle">Ramaiah CIE-1 Q2(c) Solved: Encapsulated directly into Ethernet Frame (Type 0x0806)</text>
</svg>'''

def generate_sliding_window_svg():
    return '''<svg viewBox="0 0 720 400" width="100%" height="400" role="img" aria-label="Selective Repeat ARQ Sliding Window Protocol Timing Diagram">
  <title>Selective Repeat ARQ Protocol (Sender Window Sw = 2^(m-1))</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />

  <text x="360" y="28" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">Selective Repeat ARQ (m = 2, Sw = 2, Rw = 2) with Lost Frame Retransmission</text>

  <!-- Timelines -->
  <line x1="150" y1="55" x2="150" y2="355" stroke="var(--ink)" stroke-width="2" />
  <line x1="570" y1="55" x2="570" y2="355" stroke="var(--ink)" stroke-width="2" />
  <polygon points="146,355 154,355 150,363" fill="var(--ink)" />
  <polygon points="566,355 574,355 570,363" fill="var(--ink)" />

  <text x="150" y="48" fill="var(--ink)" font-family="var(--font-display)" font-size="13" font-weight="700" text-anchor="middle">Sender (TX)</text>
  <text x="570" y="48" fill="var(--ink)" font-family="var(--font-display)" font-size="13" font-weight="700" text-anchor="middle">Receiver (RX)</text>

  <!-- Window status boxes -->
  <text x="40" y="80" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11">Win: [0, 1]</text>
  <text x="600" y="80" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11">Win: [0, 1]</text>

  <!-- Frame 0 sent -->
  <line x1="150" y1="75" x2="570" y2="105" stroke="var(--green)" stroke-width="2" />
  <polygon points="562,101 570,105 562,109" fill="var(--green)" />
  <text x="240" y="82" fill="var(--ink)" font-family="var(--font-mono)" font-size="11" font-weight="600" text-anchor="middle">Frame 0</text>

  <!-- Frame 1 sent (LOST) -->
  <line x1="150" y1="110" x2="420" y2="135" stroke="#B91C1C" stroke-width="2" />
  <text x="428" y="139" fill="#B91C1C" font-family="var(--font-display)" font-size="13" font-weight="bold">✕ [Lost]</text>
  <text x="240" y="115" fill="#B91C1C" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Frame 1</text>

  <!-- ACK 0 returned -->
  <line x1="570" y1="105" x2="150" y2="155" stroke="#1E4E79" stroke-width="1.8" stroke-dasharray="4,2" />
  <polygon points="158,151 150,155 158,159" fill="#1E4E79" />
  <text x="470" y="145" fill="#1E4E79" font-family="var(--font-mono)" font-size="11" font-weight="600" text-anchor="middle">ACK 0 (Rx slides to [1, 2])</text>

  <!-- Frame 2 sent -->
  <text x="40" y="165" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11">Win: [1, 2]</text>
  <line x1="150" y1="165" x2="570" y2="205" stroke="var(--green)" stroke-width="2" />
  <polygon points="562,201 570,205 562,209" fill="var(--green)" />
  <text x="240" y="178" fill="var(--ink)" font-family="var(--font-mono)" font-size="11" font-weight="600" text-anchor="middle">Frame 2</text>
  <text x="600" y="210" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10.5">Buffer Frame 2</text>

  <!-- NAK 1 returned -->
  <line x1="570" y1="205" x2="150" y2="255" stroke="#B91C1C" stroke-width="1.8" stroke-dasharray="4,2" />
  <polygon points="158,251 150,255 158,259" fill="#B91C1C" />
  <text x="470" y="245" fill="#B91C1C" font-family="var(--font-mono)" font-size="11" font-weight="600" text-anchor="middle">NAK 1 (Selective NAK)</text>

  <!-- Selective Retransmission of Frame 1 ONLY -->
  <line x1="150" y1="265" x2="570" y2="305" stroke="var(--green)" stroke-width="2" />
  <polygon points="562,301 570,305 562,309" fill="var(--green)" />
  <text x="270" y="278" fill="var(--green)" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">Retransmit Frame 1 ONLY</text>

  <!-- ACK 3 (Cumulative ACK up to 2) -->
  <line x1="570" y1="305" x2="150" y2="345" stroke="#1E4E79" stroke-width="1.8" stroke-dasharray="4,2" />
  <polygon points="158,341 150,345 158,349" fill="#1E4E79" />
  <text x="470" y="340" fill="#1E4E79" font-family="var(--font-mono)" font-size="11" font-weight="600" text-anchor="middle">ACK 3 (Rx slides to [3, 0])</text>

  <text x="360" y="380" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">Ramaiah CIE-2 Q1(b) Justified: Sw = 2^(m-1) = 2 ensures unacknowledged frames never overlap with next cycle window</text>
</svg>'''

if __name__ == '__main__':
    print("CN Unit 2 assets generated.")
