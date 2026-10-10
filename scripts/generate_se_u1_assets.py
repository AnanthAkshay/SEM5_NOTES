"""
generate_se_u1_assets.py - Generates theme-aware SVGs for SE Unit 1 notes:
- Figure 1.1: Waterfall Process Model with Feedback Loops (Ramaiah CIE-1 Q2.a)
- Figure 1.2: Rational Unified Process (RUP) 4 Distinct Phases & Milestones (Ramaiah CIE-1 Q3.a)
- Figure 1.3: Scrum Agile Lifecycle Framework with Burndown & Sprints
"""

def generate_waterfall_model_svg():
    """Figure 1.1: Classical Waterfall Process Model with Downward Cascades"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Waterfall Process Model for Software Development">
  <defs>
    <marker id="wf-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="wf-arr-back" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink-muted)" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">THE CLASSICAL WATERFALL PROCESS MODEL &bull; CASCADING PHASES (RAMAIAH CIE-1 Q2.a)</text>

  <!-- Phase 1: Requirements Definition -->
  <g transform="translate(40, 55)">
    <rect width="170" height="42" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="85" y="22" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">1. Requirements Analysis</text>
    <text x="85" y="34" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">SRS Document Baseline</text>
  </g>

  <!-- Arrow 1 to 2 -->
  <path d="M 210 76 L 240 76 L 240 105" fill="none" stroke="var(--brand)" stroke-width="2" marker-end="url(#wf-arr)" />

  <!-- Phase 2: System & Software Design -->
  <g transform="translate(180, 105)">
    <rect width="170" height="42" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="85" y="22" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">2. System &amp; SW Design</text>
    <text x="85" y="34" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Architecture &amp; Data Models</text>
  </g>

  <!-- Arrow 2 to 3 -->
  <path d="M 350 126 L 380 126 L 380 155" fill="none" stroke="var(--brand)" stroke-width="2" marker-end="url(#wf-arr)" />

  <!-- Phase 3: Implementation & Unit Testing -->
  <g transform="translate(320, 155)">
    <rect width="170" height="42" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="85" y="22" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">3. Implementation &amp; Unit</text>
    <text x="85" y="34" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Source Code &amp; Module Tests</text>
  </g>

  <!-- Arrow 3 to 4 -->
  <path d="M 490 176 L 520 176 L 520 205" fill="none" stroke="var(--brand)" stroke-width="2" marker-end="url(#wf-arr)" />

  <!-- Phase 4: Integration & System Testing -->
  <g transform="translate(460, 205)">
    <rect width="170" height="42" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="85" y="22" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">4. Integration &amp; System</text>
    <text x="85" y="34" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">End-to-End System Tests</text>
  </g>

  <!-- Arrow 4 to 5 -->
  <path d="M 630 226 L 660 226 L 660 255" fill="none" stroke="var(--brand)" stroke-width="2" marker-end="url(#wf-arr)" />

  <!-- Phase 5: Operation & Maintenance -->
  <g transform="translate(570, 255)">
    <rect width="170" height="42" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="2" />
    <text x="85" y="22" font-family="var(--font-display)" font-size="11.5" font-weight="800" fill="var(--green)" text-anchor="middle">5. Operation &amp; Maint.</text>
    <text x="85" y="34" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="var(--green)" text-anchor="middle">Deployment &amp; Patches</text>
  </g>

  <!-- Theoretical Feedback Loops (Dotted gray curves) -->
  <path d="M 320 176 C 260 176, 260 97, 210 97" fill="none" stroke="var(--ink-muted)" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#wf-arr-back)" />
  <path d="M 460 226 C 400 226, 400 147, 350 147" fill="none" stroke="var(--ink-muted)" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#wf-arr-back)" />
  <text x="50" y="290" font-family="var(--font-mono)" font-size="10.5" fill="var(--ink-muted)">* Dotted arcs: Costly feedback loops in practice</text>
</svg>'''

def generate_rup_model_svg():
    """Figure 1.2: Rational Unified Process (RUP) 4 Distinct Phases & Milestones"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Rational Unified Process 4 Phases and Milestones">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">RATIONAL UNIFIED PROCESS (RUP) &bull; 4 DYNAMIC PHASES &amp; MILESTONES (RAMAIAH CIE-1 Q3.a)</text>

  <!-- Time Axis Bar across Top -->
  <g transform="translate(30, 55)">
    <rect width="720" height="26" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="75" y="18" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">INCEPTION (10%)</text>
    <text x="235" y="18" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">ELABORATION (30%)</text>
    <text x="475" y="18" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--green)" text-anchor="middle">CONSTRUCTION (50%)</text>
    <text x="665" y="18" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink-muted)" text-anchor="middle">TRANSITION (10%)</text>
    <line x1="150" y1="0" x2="150" y2="26" stroke="var(--border)" stroke-width="1.5" />
    <line x1="320" y1="0" x2="320" y2="26" stroke="var(--border)" stroke-width="1.5" />
    <line x1="630" y1="0" x2="630" y2="26" stroke="var(--border)" stroke-width="1.5" />
  </g>

  <!-- 4 Phase Cards -->
  <!-- Phase 1: Inception -->
  <g transform="translate(30, 95)">
    <rect width="165" height="155" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="82" y="24" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">1. Inception Phase</text>
    <line x1="15" y1="34" x2="150" y2="34" stroke="var(--border)" stroke-width="1" />
    <text x="12" y="55" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Business case &amp; scope</text>
    <text x="12" y="75" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Feasibility study</text>
    <text x="12" y="95" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Identify primary actors</text>
    <!-- Milestone -->
    <rect x="10" y="115" width="145" height="28" rx="6" fill="var(--surface)" stroke="var(--brand)" stroke-width="1" />
    <text x="82" y="132" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="var(--brand)" text-anchor="middle">Milestone: Lifecycle Obj.</text>
  </g>

  <!-- Phase 2: Elaboration -->
  <g transform="translate(205, 95)">
    <rect width="175" height="155" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="87" y="24" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">2. Elaboration Phase</text>
    <line x1="15" y1="34" x2="160" y2="34" stroke="var(--border)" stroke-width="1" />
    <text x="12" y="55" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Requirements capture</text>
    <text x="12" y="75" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Architecture baseline</text>
    <text x="12" y="95" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Mitigate high risks</text>
    <!-- Milestone -->
    <rect x="10" y="115" width="155" height="28" rx="6" fill="var(--surface)" stroke="var(--brand)" stroke-width="1" />
    <text x="87" y="132" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="var(--brand)" text-anchor="middle">Milestone: Lifecycle Arch.</text>
  </g>

  <!-- Phase 3: Construction -->
  <g transform="translate(390, 95)">
    <rect width="185" height="155" rx="10" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.5" />
    <text x="92" y="24" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">3. Construction Phase</text>
    <line x1="15" y1="34" x2="170" y2="34" stroke="var(--green)" stroke-width="1" />
    <text x="12" y="55" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Component coding</text>
    <text x="12" y="75" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; System integration</text>
    <text x="12" y="95" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Comprehensive tests</text>
    <!-- Milestone -->
    <rect x="10" y="115" width="165" height="28" rx="6" fill="var(--surface)" stroke="var(--green)" stroke-width="1" />
    <text x="92" y="132" font-family="var(--font-mono)" font-size="8.5" font-weight="800" fill="var(--green)" text-anchor="middle">Milestone: Initial Op. Cap.</text>
  </g>

  <!-- Phase 4: Transition -->
  <g transform="translate(585, 95)">
    <rect width="165" height="155" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="82" y="24" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--ink)" text-anchor="middle">4. Transition Phase</text>
    <line x1="15" y1="34" x2="150" y2="34" stroke="var(--border)" stroke-width="1" />
    <text x="12" y="55" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Beta test deployment</text>
    <text x="12" y="75" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; User training &amp; conversion</text>
    <text x="12" y="95" font-family="var(--font-body)" font-size="10" fill="var(--ink)">&bull; Bug patching</text>
    <!-- Milestone -->
    <rect x="10" y="115" width="145" height="28" rx="6" fill="var(--surface)" stroke="var(--border-strong)" stroke-width="1" />
    <text x="82" y="132" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="var(--ink-muted)" text-anchor="middle">Milestone: Product Release</text>
  </g>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(30, 265)">
    <rect width="720" height="50" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="360" y="20" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Core Workflows span all phases: Business Modeling, Requirements, Analysis &amp; Design, Implementation, Testing, Deployment.</text>
    <text x="360" y="38" font-family="var(--font-mono)" font-size="10" fill="var(--green)" text-anchor="middle">RUP unites plan-driven architecture discipline in Elaboration with Agile iterations in Construction.</text>
  </g>
</svg>'''

def generate_scrum_framework_svg():
    """Figure 1.3: Scrum Agile Lifecycle Framework with Sprint Loop & Burndown"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Scrum Framework with Product Backlog and Sprint Cycle">
  <defs>
    <marker id="scrum-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--green)" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">THE SCRUM AGILE FRAMEWORK &bull; SPRINT VELOCITY &amp; INCREMENT DELIVERY (SOMMERVILLE CH. 3)</text>

  <!-- 1. Product Backlog on Left -->
  <g transform="translate(30, 65)">
    <rect width="130" height="235" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="65" y="26" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">Product Backlog</text>
    <text x="65" y="42" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">(Product Owner)</text>
    <!-- Backlog items stack -->
    <rect x="15" y="55" width="100" height="24" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="71" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)" text-anchor="middle">Story #1 (13 SP)</text>
    <rect x="15" y="85" width="100" height="24" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="101" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)" text-anchor="middle">Story #2 (8 SP)</text>
    <rect x="15" y="115" width="100" height="24" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="131" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)" text-anchor="middle">Story #3 (8 SP)</text>
    <rect x="15" y="145" width="100" height="24" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="161" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Story #4 (5 SP)</text>
    <rect x="15" y="175" width="100" height="24" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="191" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Remaining: 180 SP</text>
  </g>

  <!-- Arrow from Product Backlog to Sprint Planning -->
  <line x1="160" y1="182" x2="200" y2="182" stroke="var(--green)" stroke-width="2" marker-end="url(#scrum-arr)" />

  <!-- 2. Sprint Planning & Sprint Backlog -->
  <g transform="translate(200, 105)">
    <rect width="130" height="155" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="65" y="24" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Sprint Planning</text>
    <text x="65" y="38" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">&amp; Sprint Backlog</text>
    <rect x="15" y="50" width="100" height="22" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="65" font-family="var(--font-mono)" font-size="8.5" fill="var(--brand)" text-anchor="middle">Task 1 (Design)</text>
    <rect x="15" y="78" width="100" height="22" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="93" font-family="var(--font-mono)" font-size="8.5" fill="var(--brand)" text-anchor="middle">Task 2 (Code)</text>
    <rect x="15" y="106" width="100" height="22" rx="4" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="65" y="121" font-family="var(--font-mono)" font-size="8.5" fill="var(--brand)" text-anchor="middle">Task 3 (Test)</text>
  </g>

  <!-- Arrow to Sprint Cycle -->
  <line x1="330" y1="182" x2="380" y2="182" stroke="var(--green)" stroke-width="2" marker-end="url(#scrum-arr)" />

  <!-- 3. Central Sprint Cycle Loop (2-4 Weeks) -->
  <g transform="translate(450, 182)">
    <circle cx="0" cy="0" r="62" fill="var(--green-tint)" stroke="var(--green)" stroke-width="2.5" />
    <text x="0" y="-12" font-family="var(--font-display)" font-size="13" font-weight="800" fill="var(--green)" text-anchor="middle">SPRINT</text>
    <text x="0" y="5" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">2 &ndash; 4 WEEKS</text>
    <text x="0" y="22" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Velocity: 44 SP</text>

    <!-- Daily Standup Satellite above -->
    <circle cx="0" cy="-80" r="24" fill="var(--surface)" stroke="var(--brand)" stroke-width="1.8" />
    <text x="0" y="-83" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="var(--brand)" text-anchor="middle">DAILY</text>
    <text x="0" y="-71" font-family="var(--font-mono)" font-size="8" fill="var(--ink)" text-anchor="middle">15 min</text>
    <line x1="0" y1="-56" x2="0" y2="-62" stroke="var(--brand)" stroke-width="1.5" />
  </g>

  <!-- Arrow to Output Increment -->
  <line x1="512" y1="182" x2="560" y2="182" stroke="var(--green)" stroke-width="2" marker-end="url(#scrum-arr)" />

  <!-- 4. Shippable Increment & Review -->
  <g transform="translate(560, 105)">
    <rect width="180" height="155" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.2" />
    <text x="90" y="24" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--green)" text-anchor="middle">Shippable Increment</text>
    <text x="90" y="40" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Potentially Deployable Code</text>

    <rect x="15" y="55" width="150" height="34" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="90" y="70" font-family="var(--font-mono)" font-size="9" font-weight="700" fill="var(--ink)" text-anchor="middle">Sprint Review</text>
    <text x="90" y="82" font-family="var(--font-body)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Demo to Stakeholders</text>

    <rect x="15" y="98" width="150" height="34" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="90" y="113" font-family="var(--font-mono)" font-size="9" font-weight="700" fill="var(--ink)" text-anchor="middle">Sprint Retrospective</text>
    <text x="90" y="125" font-family="var(--font-body)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Team Process Tuning</text>
  </g>
</svg>'''
