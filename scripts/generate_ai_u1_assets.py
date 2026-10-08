"""
generate_ai_u1_assets.py - Generates theme-aware SVGs for AI Unit 1 notes:
- Figure 1.1: 4 Approaches to AI Matrix (Ramaiah CIE-1 Oct 2025 Q1.a)
- Figure 1.2: Model-Based Reflex Agent Architecture (Ramaiah CIE-1 Oct 2025 Q2.a)
- Figure 1.3: PEAS Task Environment Breakdown (Ramaiah CIE-1 Oct 2025 Q3.a)
"""

def generate_four_approaches_svg():
    """Figure 1.1: 2x2 Grid of the Four Historical Definitions of AI"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Four Approaches to Defining Artificial Intelligence">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">THE FOUR APPROACHES TO DEFINING AI (RUSSELL &amp; NORVIG &bull; CIE-1 Q1.a)</text>

  <!-- Column Headers -->
  <text x="260" y="65" font-family="var(--font-display)" font-size="13" font-weight="800" fill="var(--brand)" text-anchor="middle">HUMAN-CENTRIC STANDARD</text>
  <text x="580" y="65" font-family="var(--font-display)" font-size="13" font-weight="800" fill="var(--green)" text-anchor="middle">RATIONAL (IDEAL) STANDARD</text>

  <!-- Row Headers -->
  <text x="35" y="140" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--ink)" text-anchor="start">THINKING</text>
  <text x="35" y="156" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="start">(Internal Cognition)</text>

  <text x="35" y="245" font-family="var(--font-display)" font-size="12" font-weight="800" fill="var(--ink)" text-anchor="start">ACTING</text>
  <text x="35" y="261" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="start">(External Behavior)</text>

  <!-- Quadrant 1: Thinking Humanly (Top-Left) -->
  <g transform="translate(130, 85)">
    <rect width="260" height="105" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="130" y="28" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" text-anchor="middle">1. Thinking Humanly</text>
    <text x="130" y="48" font-family="var(--font-mono)" font-size="10" font-weight="600" fill="var(--brand)" text-anchor="middle">The Cognitive Modeling Approach</text>
    <text x="130" y="70" font-family="var(--font-body)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">Validates internal algorithmic steps against</text>
    <text x="130" y="86" font-family="var(--font-body)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">human psychological &amp; fMRI neuro-traces.</text>
  </g>

  <!-- Quadrant 2: Thinking Rationally (Top-Right) -->
  <g transform="translate(450, 85)">
    <rect width="260" height="105" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="130" y="28" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" text-anchor="middle">2. Thinking Rationally</text>
    <text x="130" y="48" font-family="var(--font-mono)" font-size="10" font-weight="600" fill="var(--green)" text-anchor="middle">The "Laws of Thought" Approach</text>
    <text x="130" y="70" font-family="var(--font-body)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">Aristotelian syllogisms and deductive logic.</text>
    <text x="130" y="86" font-family="var(--font-body)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">Struggles with uncertain, informal data.</text>
  </g>

  <!-- Quadrant 3: Acting Humanly (Bottom-Left) -->
  <g transform="translate(130, 205)">
    <rect width="260" height="105" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="130" y="28" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" text-anchor="middle">3. Acting Humanly</text>
    <text x="130" y="48" font-family="var(--font-mono)" font-size="10" font-weight="600" fill="var(--brand)" text-anchor="middle">The Turing Test Approach (1950)</text>
    <text x="130" y="70" font-family="var(--font-body)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">Passes if human interrogator cannot distinguish</text>
    <text x="130" y="86" font-family="var(--font-body)" font-size="11" fill="var(--ink-muted)" text-anchor="middle">machine responses from human responses.</text>
  </g>

  <!-- Quadrant 4: Acting Rationally (Bottom-Right - MODERN GOLD STANDARD) -->
  <g transform="translate(450, 205)">
    <rect width="260" height="105" rx="10" fill="var(--green-tint)" stroke="var(--green)" stroke-width="2" />
    <text x="130" y="28" font-family="var(--font-display)" font-size="13" font-weight="800" fill="var(--green)" text-anchor="middle">4. Acting Rationally &starf;</text>
    <text x="130" y="48" font-family="var(--font-mono)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">The Rational Agent Approach (Standard)</text>
    <text x="130" y="70" font-family="var(--font-body)" font-size="11" fill="var(--ink)" text-anchor="middle">Acts to maximize expected performance metric</text>
    <text x="130" y="86" font-family="var(--font-body)" font-size="11" fill="var(--ink)" text-anchor="middle">given available percepts and built-in knowledge.</text>
  </g>
</svg>'''

def generate_model_based_reflex_agent_svg():
    """Figure 1.2: Model-Based Reflex Agent Architectural Schematic"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Model-Based Reflex Agent Internal Architecture">
  <defs>
    <marker id="agent-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">MODEL-BASED REFLEX AGENT ARCHITECTURE (RAMAIAH CIE-1 Q2.a)</text>

  <!-- Environment Box on Left -->
  <g transform="translate(30, 70)">
    <rect width="130" height="235" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="2" />
    <text x="65" y="40" font-family="var(--font-display)" font-size="14" font-weight="800" fill="var(--ink)" text-anchor="middle">ENVIRONMENT</text>
    <text x="65" y="60" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">(Physical World)</text>
    <!-- Sensory Stream Icon -->
    <circle cx="65" cy="115" r="22" fill="var(--border)" />
    <text x="65" y="120" font-size="16" text-anchor="middle">&#x1f441;&#xfe0f;</text>
    <text x="65" y="150" font-family="var(--font-mono)" font-size="10" fill="var(--ink-muted)" text-anchor="middle">Sensory Percepts</text>
    <!-- Actuator effect Icon -->
    <circle cx="65" cy="195" r="22" fill="var(--brand-tint)" />
    <text x="65" y="200" font-size="16" text-anchor="middle">&#x2699;&#xfe0f;</text>
    <text x="65" y="230" font-family="var(--font-mono)" font-size="10" fill="var(--brand)" text-anchor="middle">Action Effects</text>
  </g>

  <!-- Percept Arrow: Environment to Sensors -->
  <line x1="160" y1="120" x2="230" y2="120" stroke="var(--brand)" stroke-width="2" marker-end="url(#agent-arr)" />
  <text x="195" y="112" font-family="var(--font-mono)" font-size="10" font-weight="600" fill="var(--brand)" text-anchor="middle">Percepts</text>

  <!-- Agent Outer Boundary -->
  <rect x="235" y="55" width="510" height="260" rx="14" fill="var(--surface)" stroke="var(--brand)" stroke-width="2" stroke-dasharray="6 3" />
  <text x="255" y="78" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)">INTERNAL AGENT BOUNDARY</text>

  <!-- Sensors Box -->
  <g transform="translate(250, 100)">
    <rect width="90" height="42" rx="8" fill="var(--brand-tint)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="45" y="26" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">SENSORS</text>
  </g>

  <!-- State Component (What the world is like now) -->
  <g transform="translate(380, 85)">
    <rect width="180" height="50" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="90" y="22" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">STATE</text>
    <text x="90" y="38" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Internal Memory of World</text>
  </g>

  <line x1="340" y1="121" x2="380" y2="110" stroke="var(--ink-muted)" stroke-width="1.5" marker-end="url(#agent-arr)" />

  <!-- Transition Model Knowledge Components on Right -->
  <g transform="translate(590, 75)">
    <rect width="140" height="42" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="70" y="18" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="var(--ink)" text-anchor="middle">How world evolves</text>
    <text x="70" y="32" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">(Physics / dynamics)</text>
  </g>
  <line x1="560" y1="98" x2="590" y2="96" stroke="var(--ink-muted)" stroke-width="1.2" />

  <g transform="translate(590, 125)">
    <rect width="140" height="42" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1" />
    <text x="70" y="18" font-family="var(--font-mono)" font-size="9.5" font-weight="700" fill="var(--ink)" text-anchor="middle">What my actions do</text>
    <text x="70" y="32" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">(Transition model)</text>
  </g>
  <line x1="560" y1="122" x2="590" y2="136" stroke="var(--ink-muted)" stroke-width="1.2" />

  <!-- Condition-Action Rules Box -->
  <g transform="translate(380, 160)">
    <rect width="180" height="50" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="90" y="22" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Condition-Action Rules</text>
    <text x="90" y="38" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">"If state = S then Action A"</text>
  </g>
  <line x1="470" y1="135" x2="470" y2="160" stroke="var(--brand)" stroke-width="1.8" marker-end="url(#agent-arr)" />

  <!-- Action Selector Box -->
  <g transform="translate(380, 235)">
    <rect width="180" height="45" rx="8" fill="var(--green-tint)" stroke="var(--green)" stroke-width="1.8" />
    <text x="90" y="20" font-family="var(--font-body)" font-size="11.5" font-weight="700" fill="var(--green)" text-anchor="middle">What action I should do</text>
    <text x="90" y="35" font-family="var(--font-mono)" font-size="9" fill="var(--green)" text-anchor="middle">Selected Action a</text>
  </g>
  <line x1="470" y1="210" x2="470" y2="235" stroke="var(--brand)" stroke-width="1.8" marker-end="url(#agent-arr)" />

  <!-- Actuators Box -->
  <g transform="translate(250, 235)">
    <rect width="90" height="45" rx="8" fill="var(--brand-tint)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="45" y="28" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">ACTUATORS</text>
  </g>
  <line x1="380" y1="257" x2="340" y2="257" stroke="var(--brand)" stroke-width="2" marker-end="url(#agent-arr)" />

  <!-- Action Arrow: Actuators to Environment -->
  <line x1="250" y1="257" x2="160" y2="257" stroke="var(--brand)" stroke-width="2" marker-end="url(#agent-arr)" />
  <text x="205" y="250" font-family="var(--font-mono)" font-size="10" font-weight="600" fill="var(--brand)" text-anchor="middle">Action</text>
</svg>'''

def generate_peas_task_env_svg():
    """Figure 1.3: PEAS 4-Quadrant Framework Breakdown for Smart Traffic & Medical Systems"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="PEAS Framework Breakdown for Intelligent Systems">
  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">PEAS SPECIFICATION ARCHITECTURE (RAMAIAH CIE-1 Q3.a)</text>

  <!-- Left Card: Smart Traffic Control System -->
  <g transform="translate(25, 55)">
    <rect width="350" height="260" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <rect width="350" height="38" rx="12" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="175" y="25" font-family="var(--font-display)" font-size="12.5" font-weight="800" fill="var(--brand)" text-anchor="middle">SYSTEM 1: SMART TRAFFIC CONTROL (CIE-1 Q3.a.i)</text>

    <!-- P -->
    <text x="20" y="65" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--green)">[P] Performance:</text>
    <text x="20" y="82" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Minimize vehicle wait time, eliminate gridlock,</text>
    <text x="20" y="97" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">prioritize emergency vehicles (ambulances), fuel economy.</text>

    <!-- E -->
    <text x="20" y="125" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)">[E] Environment:</text>
    <text x="20" y="142" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Urban intersection roads, vehicles, pedestrians,</text>
    <text x="20" y="157" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">weather conditions (rain/fog), time-of-day traffic flow.</text>

    <!-- A -->
    <text x="20" y="185" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="#3B82F6">[A] Actuators:</text>
    <text x="20" y="202" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Signal light controllers (Red/Yellow/Green timers),</text>
    <text x="20" y="217" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">variable electronic sign boards, barrier gates.</text>

    <!-- S -->
    <text x="20" y="245" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="#EF4444">[S] Sensors:</text>
    <text x="20" y="262" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">CCTV intersection cameras, inductive road loop sensors,</text>
    <text x="20" y="277" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">infrared pedestrian detectors, GPS fleet telemetry.</text>
  </g>

  <!-- Right Card: Intelligent Medical Diagnosis System -->
  <g transform="translate(405, 55)">
    <rect width="350" height="260" rx="12" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <rect width="350" height="38" rx="12" fill="var(--surface)" stroke="var(--border)" stroke-width="1" />
    <text x="175" y="25" font-family="var(--font-display)" font-size="12.5" font-weight="800" fill="var(--green)" text-anchor="middle">SYSTEM 2: MEDICAL DIAGNOSIS (CIE-1 Q3.a.ii)</text>

    <!-- P -->
    <text x="20" y="65" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--green)">[P] Performance:</text>
    <text x="20" y="82" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Diagnostic accuracy, near-zero false negatives,</text>
    <text x="20" y="97" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">minimal testing cost, patient survival rate, quick triage.</text>

    <!-- E -->
    <text x="20" y="125" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="var(--brand)">[E] Environment:</text>
    <text x="20" y="142" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Hospital ward / clinic, patients, medical staff,</text>
    <text x="20" y="157" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">symptom histories, laboratory testing equipment.</text>

    <!-- A -->
    <text x="20" y="185" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="#3B82F6">[A] Actuators:</text>
    <text x="20" y="202" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Screen display of diagnosis report, treatment plan,</text>
    <text x="20" y="217" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">prescription recommendations, follow-up test orders.</text>

    <!-- S -->
    <text x="20" y="245" font-family="var(--font-mono)" font-size="11" font-weight="800" fill="#EF4444">[S] Sensors:</text>
    <text x="20" y="262" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">Keyboard entry of symptoms, vitals monitors (ECG/BP),</text>
    <text x="20" y="277" font-family="var(--font-body)" font-size="10.5" fill="var(--ink)">digital lab test feeds (blood/urine), radiology DICOM scans.</text>
  </g>
</svg>'''
