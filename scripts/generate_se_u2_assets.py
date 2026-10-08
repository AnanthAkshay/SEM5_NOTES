"""
generate_se_u2_assets.py - Generates theme-aware SVGs for SE Unit 2 notes:
- Figure 2.1: Library Management System Use Case Diagram (Ramaiah CIE-1 Q3.b)
- Figure 2.2: Sequence Diagram for Book Borrowing & Checkout Interaction
- Figure 2.3: Requirements Engineering Process Flow (Sommerville Ch. 4)
"""

def generate_library_use_case_svg():
    """Figure 2.1: Library Management System Use Case Diagram with Member & Librarian Actors (CIE-1 Q3.b)"""
    return '''<svg viewBox="0 0 780 420" width="100%" height="420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Use Case Diagram for Library Management System showing Member and Librarian actors">
  <defs>
    <marker id="uc-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="uc-arr-dash" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink-muted)" />
    </marker>
  </defs>

  <!-- Canvas Container -->
  <rect x="5" y="5" width="770" height="410" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">LIBRARY MANAGEMENT SYSTEM &bull; USE CASE DIAGRAM (RAMAIAH CIE-1 Q3.b)</text>

  <!-- Left Actor: Library Member -->
  <g transform="translate(60, 160)">
    <!-- Stick Figure: Member -->
    <circle cx="0" cy="-35" r="14" fill="none" stroke="var(--ink)" stroke-width="2.2" />
    <line x1="0" y1="-21" x2="0" y2="18" stroke="var(--ink)" stroke-width="2.2" />
    <line x1="-22" y1="-5" x2="22" y2="-5" stroke="var(--ink)" stroke-width="2.2" />
    <line x1="0" y1="18" x2="-18" y2="52" stroke="var(--ink)" stroke-width="2.2" />
    <line x1="0" y1="18" x2="18" y2="52" stroke="var(--ink)" stroke-width="2.2" />
    <rect x="-42" y="62" width="84" height="22" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="0" y="77" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">&laquo;Actor&raquo; Member</text>
  </g>

  <!-- Right Actor: Librarian -->
  <g transform="translate(720, 160)">
    <!-- Stick Figure: Librarian -->
    <circle cx="0" cy="-35" r="14" fill="none" stroke="var(--brand)" stroke-width="2.2" />
    <line x1="0" y1="-21" x2="0" y2="18" stroke="var(--brand)" stroke-width="2.2" />
    <line x1="-22" y1="-5" x2="22" y2="-5" stroke="var(--brand)" stroke-width="2.2" />
    <line x1="0" y1="18" x2="-18" y2="52" stroke="var(--brand)" stroke-width="2.2" />
    <line x1="0" y1="18" x2="18" y2="52" stroke="var(--brand)" stroke-width="2.2" />
    <rect x="-45" y="62" width="90" height="22" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="0" y="77" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">&laquo;Actor&raquo; Librarian</text>
  </g>

  <!-- System Boundary Box -->
  <rect x="145" y="48" width="490" height="350" rx="10" fill="none" stroke="var(--brand)" stroke-width="1.8" stroke-dasharray="6,4" />
  <rect x="155" y="55" width="220" height="20" rx="4" fill="var(--surface-alt)" />
  <text x="165" y="69" font-family="var(--font-mono)" font-size="10.5" font-weight="700" fill="var(--brand)">System: Library Management</text>

  <!-- Use Case 1: Search Books -->
  <g transform="translate(260, 105)">
    <ellipse cx="0" cy="0" rx="90" ry="24" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="4" font-family="var(--font-display)" font-size="11" font-weight="600" fill="var(--ink)" text-anchor="middle">Search &amp; Browse Catalog</text>
  </g>

  <!-- Use Case 2: Borrow Book -->
  <g transform="translate(260, 175)">
    <ellipse cx="0" cy="0" rx="90" ry="24" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="4" font-family="var(--font-display)" font-size="11" font-weight="600" fill="var(--ink)" text-anchor="middle">Borrow Book</text>
  </g>

  <!-- Use Case 3: Return Book -->
  <g transform="translate(260, 245)">
    <ellipse cx="0" cy="0" rx="90" ry="24" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="4" font-family="var(--font-display)" font-size="11" font-weight="600" fill="var(--ink)" text-anchor="middle">Return Book</text>
  </g>

  <!-- Use Case 4: Verify Member Eligibility (Included) -->
  <g transform="translate(490, 140)">
    <ellipse cx="0" cy="0" rx="95" ry="24" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="4" font-family="var(--font-display)" font-size="10.5" font-weight="600" fill="var(--ink)" text-anchor="middle">Validate Member Identity</text>
  </g>

  <!-- Use Case 5: Pay Overdue Fine (Extended) -->
  <g transform="translate(490, 220)">
    <ellipse cx="0" cy="0" rx="95" ry="24" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="4" font-family="var(--font-display)" font-size="10.5" font-weight="600" fill="var(--ink)" text-anchor="middle">Calculate &amp; Collect Fine</text>
  </g>

  <!-- Use Case 6: Manage Book Inventory (Librarian) -->
  <g transform="translate(490, 310)">
    <ellipse cx="0" cy="0" rx="95" ry="24" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="4" font-family="var(--font-display)" font-size="10.5" font-weight="600" fill="var(--ink)" text-anchor="middle">Manage Catalog &amp; Stock</text>
  </g>

  <!-- Use Case 7: Generate Circulation Reports -->
  <g transform="translate(260, 340)">
    <ellipse cx="0" cy="0" rx="90" ry="24" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="4" font-family="var(--font-display)" font-size="10.5" font-weight="600" fill="var(--ink)" text-anchor="middle">Generate Overdue Report</text>
  </g>

  <!-- Association Lines from Member -->
  <line x1="75" y1="145" x2="170" y2="105" stroke="var(--ink)" stroke-width="1.5" />
  <line x1="75" y1="160" x2="170" y2="175" stroke="var(--ink)" stroke-width="1.5" />
  <line x1="75" y1="175" x2="170" y2="245" stroke="var(--ink)" stroke-width="1.5" />

  <!-- Association Lines from Librarian -->
  <line x1="705" y1="145" x2="585" y2="140" stroke="var(--brand)" stroke-width="1.5" />
  <line x1="705" y1="160" x2="585" y2="220" stroke="var(--brand)" stroke-width="1.5" />
  <line x1="705" y1="180" x2="585" y2="310" stroke="var(--brand)" stroke-width="1.5" />
  <line x1="705" y1="195" x2="350" y2="340" stroke="var(--brand)" stroke-width="1.5" />

  <!-- Relationship: Borrow Book <<include>> Validate Member Identity -->
  <path d="M 345 162 L 400 148" fill="none" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#uc-arr-dash)" />
  <rect x="340" y="138" width="60" height="14" rx="3" fill="var(--surface)" />
  <text x="370" y="148" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">&laquo;include&raquo;</text>

  <!-- Relationship: Return Book <<extend>> Calculate & Collect Fine -->
  <path d="M 400 228 L 348 238" fill="none" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#uc-arr-dash)" />
  <rect x="350" y="222" width="60" height="14" rx="3" fill="var(--surface)" />
  <text x="380" y="232" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">&laquo;extend&raquo;</text>
</svg>'''

def generate_sequence_diagram_svg():
    """Figure 2.2: Sequence Diagram for Book Borrowing / Checkout Interaction"""
    return '''<svg viewBox="0 0 780 390" width="100%" height="390" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sequence Diagram for Book Borrowing interaction">
  <defs>
    <marker id="seq-sync" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="seq-reply" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink-muted)" />
    </marker>
  </defs>

  <!-- Background -->
  <rect x="5" y="5" width="770" height="380" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">SEQUENCE DIAGRAM &bull; BOOK BORROWING &amp; CHECKOUT INTERACTION</text>

  <!-- Lifeline 1: Member (Actor) -->
  <g transform="translate(90, 52)">
    <rect x="-55" y="0" width="110" height="30" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="19" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">:Member</text>
    <line x1="0" y1="30" x2="0" y2="300" stroke="var(--border)" stroke-width="1.5" stroke-dasharray="4,4" />
  </g>

  <!-- Lifeline 2: LibraryWebUI -->
  <g transform="translate(280, 52)">
    <rect x="-65" y="0" width="130" height="30" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="19" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">:LibraryWebUI</text>
    <line x1="0" y1="30" x2="0" y2="300" stroke="var(--border)" stroke-width="1.5" stroke-dasharray="4,4" />
  </g>

  <!-- Lifeline 3: BorrowController -->
  <g transform="translate(480, 52)">
    <rect x="-70" y="0" width="140" height="30" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="19" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">:BorrowController</text>
    <line x1="0" y1="30" x2="0" y2="300" stroke="var(--border)" stroke-width="1.5" stroke-dasharray="4,4" />
  </g>

  <!-- Lifeline 4: CatalogDB -->
  <g transform="translate(670, 52)">
    <rect x="-60" y="0" width="120" height="30" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="0" y="19" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">:CatalogDB</text>
    <line x1="0" y1="30" x2="0" y2="300" stroke="var(--border)" stroke-width="1.5" stroke-dasharray="4,4" />
  </g>

  <!-- Activation Bars -->
  <rect x="84" y="100" width="12" height="225" rx="2" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
  <rect x="274" y="105" width="12" height="215" rx="2" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
  <rect x="474" y="125" width="12" height="185" rx="2" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
  <rect x="664" y="150" width="12" height="135" rx="2" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />

  <!-- Message 1: Member -> UI -->
  <line x1="96" y1="110" x2="272" y2="110" stroke="var(--brand)" stroke-width="1.8" marker-end="url(#seq-sync)" />
  <text x="180" y="104" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">1: submitBorrowRequest(isbn, id)</text>

  <!-- Message 2: UI -> Controller -->
  <line x1="286" y1="130" x2="472" y2="130" stroke="var(--brand)" stroke-width="1.8" marker-end="url(#seq-sync)" />
  <text x="380" y="124" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">2: validateBorrower(id)</text>

  <!-- Message 3: Controller -> DB -->
  <line x1="486" y1="155" x2="662" y2="155" stroke="var(--brand)" stroke-width="1.8" marker-end="url(#seq-sync)" />
  <text x="575" y="149" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">3: queryMemberStatus(id)</text>

  <!-- Message 4: DB -> Controller (Return) -->
  <line x1="664" y1="180" x2="488" y2="180" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#seq-reply)" />
  <text x="575" y="174" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">4: return eligibility (0 fines, active)</text>

  <!-- Message 5: Controller -> DB -->
  <line x1="486" y1="210" x2="662" y2="210" stroke="var(--brand)" stroke-width="1.8" marker-end="url(#seq-sync)" />
  <text x="575" y="204" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">5: updateBookStatus(isbn, BORROWED)</text>

  <!-- Message 6: DB -> Controller (Return) -->
  <line x1="664" y1="235" x2="488" y2="235" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#seq-reply)" />
  <text x="575" y="229" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">6: recordCreated(loanId, due: 14d)</text>

  <!-- Message 7: Controller -> UI (Return) -->
  <line x1="474" y1="265" x2="288" y2="265" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#seq-reply)" />
  <text x="380" y="259" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">7: checkoutSuccess(loanId, dueDate)</text>

  <!-- Message 8: UI -> Member (Return) -->
  <line x1="274" y1="295" x2="98" y2="295" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#seq-reply)" />
  <text x="180" y="289" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">8: displayCheckoutReceipt(loanId)</text>
</svg>'''

def generate_requirements_process_svg():
    """Figure 2.3: Requirements Engineering Process Flow (Elicitation, Specification, Validation, Management)"""
    return '''<svg viewBox="0 0 780 320" width="100%" height="320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Requirements Engineering Process Flow with Feedback Loops">
  <defs>
    <marker id="re-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="re-arr-back" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink-muted)" />
    </marker>
  </defs>

  <!-- Canvas -->
  <rect x="5" y="5" width="770" height="310" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">THE REQUIREMENTS ENGINEERING SPIRAL PROCESS &bull; SOMMERVILLE CH. 4</text>

  <!-- Activity 1: Requirements Elicitation -->
  <g transform="translate(30, 60)">
    <rect width="165" height="100" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <rect width="165" height="26" rx="8" fill="var(--surface-alt)" />
    <text x="82" y="18" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">1. Elicitation &amp; Discovery</text>
    <line x1="0" y1="26" x2="165" y2="26" stroke="var(--border)" stroke-width="1" />
    <text x="12" y="44" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Stakeholder Interviews</text>
    <text x="12" y="60" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Use Cases &amp; Scenarios</text>
    <text x="12" y="76" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Ethnography / Observation</text>
    <text x="12" y="92" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Domain Document Analysis</text>
  </g>

  <!-- Arrow 1 to 2 -->
  <path d="M 195 110 L 220 110" fill="none" stroke="var(--brand)" stroke-width="2" marker-end="url(#re-arr)" />

  <!-- Activity 2: Requirements Analysis & Negotiation -->
  <g transform="translate(225, 60)">
    <rect width="165" height="100" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="82" y="18" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">2. Analysis &amp; Negotiation</text>
    <line x1="0" y1="26" x2="165" y2="26" stroke="var(--border)" stroke-width="1" />
    <text x="12" y="44" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Conflict Resolution</text>
    <text x="12" y="60" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Feasibility Assessment</text>
    <text x="12" y="76" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Prioritization (MoSCoW)</text>
    <text x="12" y="92" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Boundary Clarification</text>
  </g>

  <!-- Arrow 2 to 3 -->
  <path d="M 390 110 L 415 110" fill="none" stroke="var(--brand)" stroke-width="2" marker-end="url(#re-arr)" />

  <!-- Activity 3: Requirements Specification -->
  <g transform="translate(420, 60)">
    <rect width="165" height="100" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="82" y="18" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">3. Specification (SRS)</text>
    <line x1="0" y1="26" x2="165" y2="26" stroke="var(--border)" stroke-width="1" />
    <text x="12" y="44" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; User Requirements (FR/NFR)</text>
    <text x="12" y="60" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; System Architecture Specs</text>
    <text x="12" y="76" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; IEEE 830 Standard Format</text>
    <text x="12" y="92" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Mathematical Models / UML</text>
  </g>

  <!-- Arrow 3 to 4 -->
  <path d="M 585 110 L 610 110" fill="none" stroke="var(--brand)" stroke-width="2" marker-end="url(#re-arr)" />

  <!-- Activity 4: Requirements Validation -->
  <g transform="translate(615, 60)">
    <rect width="140" height="100" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="70" y="18" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">4. Validation</text>
    <line x1="0" y1="26" x2="140" y2="26" stroke="var(--border)" stroke-width="1" />
    <text x="10" y="44" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Formal Reviews</text>
    <text x="10" y="60" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Prototyping</text>
    <text x="10" y="76" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Test-Case Gen</text>
    <text x="10" y="92" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">&bull; Consistency Check</text>
  </g>

  <!-- Feedback loops from Validation back to Elicitation & Specification -->
  <path d="M 685 160 L 685 190 L 112 190 L 112 165" fill="none" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#re-arr-back)" />
  <rect x="330" y="182" width="160" height="16" rx="4" fill="var(--surface)" />
  <text x="410" y="194" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Feedback Loop &bull; Defects Discovered</text>

  <!-- Bottom Encompassing Layer: Requirements Management & RTM -->
  <g transform="translate(30, 225)">
    <rect width="725" height="70" rx="10" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="20" y="26" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--brand)">CROSS-CUTTING GOVERNANCE: REQUIREMENTS MANAGEMENT &amp; TRACEABILITY (RTM)</text>
    <text x="20" y="46" font-family="var(--font-mono)" font-size="9.5" fill="var(--ink)">1. Change Control Board (CCB) Impact Analysis &bull; 2. Forward &amp; Backward Traceability Matrix &bull; 3. Version Baselining</text>
    <text x="20" y="60" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)">Links initial user needs &rarr; SRS specification items &rarr; design modules &rarr; executable verification test cases.</text>
  </g>
</svg>'''

if __name__ == "__main__":
    print("Testing SE Unit 2 SVG generators...")
    uc = generate_library_use_case_svg()
    seq = generate_sequence_diagram_svg()
    re_proc = generate_requirements_process_svg()
    print(f"Generated Library Use Case: {len(uc)} bytes")
    print(f"Generated Sequence Diagram: {len(seq)} bytes")
    print(f"Generated RE Process: {len(re_proc)} bytes")
