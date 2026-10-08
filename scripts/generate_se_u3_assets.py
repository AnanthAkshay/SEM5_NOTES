"""
generate_se_u3_assets.py - Generates theme-aware SVGs for SE Unit 3 notes:
- Figure 3.1: Layered & Repository Architectural Patterns Comparison (Ramaiah CIE-2 Q1.a)
- Figure 3.2: Architecture of a Language Processing System / Compiler Pipeline (Ramaiah CIE-2 Q2.a)
- Figure 3.3: UML Class Diagrams for Observer & Singleton Design Patterns (Ramaiah CIE-2 Q3.a)
"""

def generate_layered_repository_svg():
    """Figure 3.1: Layered Architecture vs Repository Architecture (CIE-2 Q1.a)"""
    return '''<svg viewBox="0 0 780 390" width="100%" height="390" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Layered Architecture vs Repository Architecture Comparison">
  <defs>
    <marker id="arch-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
  </defs>

  <!-- Background -->
  <rect x="5" y="5" width="770" height="380" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">ARCHITECTURAL DESIGN PATTERNS COMPARISON &bull; (RAMAIAH CIE-2 Q1.a)</text>

  <!-- Left: Layered Architecture (4 Tiers) -->
  <g transform="translate(25, 52)">
    <rect width="350" height="320" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="175" y="24" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">LAYERED ARCHITECTURE (4-TIER)</text>
    <text x="175" y="38" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Unidirectional Downward Dependency</text>

    <!-- Layer 1: Presentation -->
    <g transform="translate(20, 50)">
      <rect width="310" height="46" rx="6" fill="var(--surface)" stroke="var(--brand)" stroke-width="1.5" />
      <text x="155" y="22" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">1. User Interface (Presentation Layer)</text>
      <text x="155" y="36" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Web Views, Mobile Client UI, Templates</text>
    </g>

    <!-- Arrow 1 to 2 -->
    <line x1="175" y1="96" x2="175" y2="114" stroke="var(--brand)" stroke-width="2" marker-end="url(#arch-arr)" />

    <!-- Layer 2: UI Management -->
    <g transform="translate(20, 115)">
      <rect width="310" height="46" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
      <text x="155" y="22" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">2. Application / Controller Layer</text>
      <text x="155" y="36" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Form Validation, Session State, API Routing</text>
    </g>

    <!-- Arrow 2 to 3 -->
    <line x1="175" y1="161" x2="175" y2="179" stroke="var(--brand)" stroke-width="2" marker-end="url(#arch-arr)" />

    <!-- Layer 3: Core Domain Logic -->
    <g transform="translate(20, 180)">
      <rect width="310" height="46" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
      <text x="155" y="22" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">3. Core Business Logic (Domain Layer)</text>
      <text x="155" y="36" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Order Processing, Pricing Algorithms, Rules</text>
    </g>

    <!-- Arrow 3 to 4 -->
    <line x1="175" y1="226" x2="175" y2="244" stroke="var(--brand)" stroke-width="2" marker-end="url(#arch-arr)" />

    <!-- Layer 4: Data Access / Storage -->
    <g transform="translate(20, 245)">
      <rect width="310" height="46" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
      <text x="155" y="22" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">4. System Support &amp; Database Layer</text>
      <text x="155" y="36" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Relational DBMS, File Storage, OS Interfaces</text>
    </g>
  </g>

  <!-- Right: Repository Architecture -->
  <g transform="translate(405, 52)">
    <rect width="350" height="320" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="175" y="24" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">REPOSITORY ARCHITECTURE (IDE MODEL)</text>
    <text x="175" y="38" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Central Data Store &bull; Decoupled Tools</text>

    <!-- Central Repository Cylinder / Box -->
    <g transform="translate(95, 120)">
      <rect width="160" height="80" rx="10" fill="var(--surface)" stroke="var(--brand)" stroke-width="2" />
      <text x="80" y="32" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">CENTRAL</text>
      <text x="80" y="48" font-family="var(--font-display)" font-size="12" font-weight="700" fill="var(--brand)" text-anchor="middle">REPOSITORY</text>
      <text x="80" y="65" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">(Project Database / AST)</text>
    </g>

    <!-- Subsystem 1: Code Editor -->
    <rect x="25" y="55" width="105" height="36" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
    <text x="77" y="78" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">Code Editor</text>
    <line x1="90" y1="91" x2="125" y2="120" stroke="var(--brand)" stroke-width="1.5" />

    <!-- Subsystem 2: Compiler / Parser -->
    <rect x="220" y="55" width="105" height="36" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
    <text x="272" y="78" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">Syntax Parser</text>
    <line x1="260" y1="91" x2="225" y2="120" stroke="var(--brand)" stroke-width="1.5" />

    <!-- Subsystem 3: Debugger -->
    <rect x="20" y="235" width="105" height="36" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
    <text x="72" y="258" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">Debugger</text>
    <line x1="90" y1="235" x2="125" y2="200" stroke="var(--brand)" stroke-width="1.5" />

    <!-- Subsystem 4: Code Generator -->
    <rect x="225" y="235" width="105" height="36" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
    <text x="277" y="258" font-family="var(--font-mono)" font-size="9" font-weight="600" fill="var(--ink)" text-anchor="middle">Code Generator</text>
    <line x1="260" y1="235" x2="225" y2="200" stroke="var(--brand)" stroke-width="1.5" />

    <text x="175" y="300" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">All tools communicate strictly through shared repository</text>
  </g>
</svg>'''

def generate_compiler_pipeline_svg():
    """Figure 3.2: Architecture of a Language Processing System / Compiler Pipeline (CIE-2 Q2.a)"""
    return '''<svg viewBox="0 0 780 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Architecture of a Language Processing System">
  <defs>
    <marker id="comp-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="comp-sym" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--ink-muted)" />
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect x="5" y="5" width="770" height="330" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">ARCHITECTURE OF A LANGUAGE PROCESSING SYSTEM &bull; COMPILER PIPELINE (RAMAIAH CIE-2 Q2.a)</text>

  <!-- Input: Source Program -->
  <g transform="translate(20, 60)">
    <rect width="90" height="50" rx="6" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="45" y="24" font-family="var(--font-display)" font-size="10.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Source</text>
    <text x="45" y="38" font-family="var(--font-display)" font-size="10.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Program</text>
  </g>

  <!-- Arrow Source -> Lexer -->
  <line x1="110" y1="85" x2="132" y2="85" stroke="var(--brand)" stroke-width="2" marker-end="url(#comp-arr)" />

  <!-- Stage 1: Lexical Analyzer -->
  <g transform="translate(135, 60)">
    <rect width="105" height="50" rx="6" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="52" y="24" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Lexical</text>
    <text x="52" y="38" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Analyzer</text>
  </g>

  <!-- Arrow Lexer -> Syntax (Tokens) -->
  <line x1="240" y1="85" x2="265" y2="85" stroke="var(--brand)" stroke-width="2" marker-end="url(#comp-arr)" />
  <text x="252" y="78" font-family="var(--font-mono)" font-size="7.5" fill="var(--ink-muted)" text-anchor="middle">Tokens</text>

  <!-- Stage 2: Syntax Analyzer -->
  <g transform="translate(268, 60)">
    <rect width="105" height="50" rx="6" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="52" y="24" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Syntax</text>
    <text x="52" y="38" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Analyzer</text>
  </g>

  <!-- Arrow Syntax -> Semantic (Parse Tree) -->
  <line x1="373" y1="85" x2="398" y2="85" stroke="var(--brand)" stroke-width="2" marker-end="url(#comp-arr)" />
  <text x="385" y="78" font-family="var(--font-mono)" font-size="7.5" fill="var(--ink-muted)" text-anchor="middle">Parse Tree</text>

  <!-- Stage 3: Semantic Analyzer -->
  <g transform="translate(401, 60)">
    <rect width="105" height="50" rx="6" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="52" y="24" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Semantic</text>
    <text x="52" y="38" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Analyzer</text>
  </g>

  <!-- Arrow Semantic -> Optimizer (Syntax Tree) -->
  <line x1="506" y1="85" x2="531" y2="85" stroke="var(--brand)" stroke-width="2" marker-end="url(#comp-arr)" />

  <!-- Stage 4: Code Optimizer -->
  <g transform="translate(534, 60)">
    <rect width="105" height="50" rx="6" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="52" y="24" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Code</text>
    <text x="52" y="38" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Optimizer</text>
  </g>

  <!-- Arrow Optimizer -> Code Gen -->
  <line x1="639" y1="85" x2="664" y2="85" stroke="var(--brand)" stroke-width="2" marker-end="url(#comp-arr)" />

  <!-- Stage 5: Code Generator -->
  <g transform="translate(667, 60)">
    <rect width="90" height="50" rx="6" fill="var(--surface-alt)" stroke="var(--brand)" stroke-width="1.5" />
    <text x="45" y="24" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Code</text>
    <text x="45" y="38" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">Generator</text>
  </g>

  <!-- Central Shared Data Structures underneath -->
  <!-- Symbol Table -->
  <g transform="translate(135, 175)">
    <rect width="238" height="65" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="119" y="28" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">SYMBOL TABLE</text>
    <text x="119" y="46" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Identifiers, Types, Scopes, Addresses</text>
  </g>

  <!-- Error Handler -->
  <g transform="translate(401, 175)">
    <rect width="238" height="65" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="119" y="28" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--ink)" text-anchor="middle">ERROR HANDLER</text>
    <text x="119" y="46" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Lexical, Syntax, &amp; Semantic Error Recovery</text>
  </g>

  <!-- Target Machine Code Output -->
  <g transform="translate(667, 175)">
    <rect width="90" height="65" rx="8" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="45" y="28" font-family="var(--font-display)" font-size="10.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Target</text>
    <text x="45" y="44" font-family="var(--font-display)" font-size="10.5" font-weight="700" fill="var(--ink)" text-anchor="middle">Machine</text>
    <text x="45" y="58" font-family="var(--font-mono)" font-size="9" fill="var(--brand)" text-anchor="middle">Code</text>
  </g>

  <!-- Connecting Lines from Pipeline stages to Symbol Table & Error Handler -->
  <path d="M 187 110 L 187 170" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#comp-sym)" />
  <path d="M 320 110 L 320 170" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#comp-sym)" />
  <path d="M 453 110 L 453 170" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#comp-sym)" />
  <path d="M 586 110 L 586 170" stroke="var(--ink-muted)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#comp-sym)" />
  <path d="M 712 110 L 712 170" stroke="var(--brand)" stroke-width="2" marker-end="url(#comp-arr)" />

  <text x="390" y="285" font-family="var(--font-mono)" font-size="9" fill="var(--ink-muted)" text-anchor="middle">Pipes-and-Filters Architectural Style &bull; Each phase consumes intermediate representation and produces transformed output</text>
</svg>'''

def generate_design_patterns_svg():
    """Figure 3.3: UML Class Diagrams for Observer & Singleton Design Patterns (CIE-2 Q3.a)"""
    return '''<svg viewBox="0 0 780 380" width="100%" height="380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="UML Class Diagrams for Observer and Singleton Design Patterns">
  <defs>
    <marker id="dp-arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="var(--brand)" />
    </marker>
    <marker id="dp-inherit" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <polygon points="0,1 8,5 0,9" fill="var(--surface)" stroke="var(--ink)" stroke-width="1.5" />
    </marker>
  </defs>

  <!-- Canvas -->
  <rect x="5" y="5" width="770" height="370" rx="14" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
  <text x="25" y="32" font-family="var(--font-display)" font-size="13" font-weight="700" fill="var(--ink)" letter-spacing="0.5">GANG OF FOUR (GoF) DESIGN PATTERNS &bull; (RAMAIAH CIE-2 Q3.a)</text>

  <!-- Left: Singleton Pattern -->
  <g transform="translate(25, 52)">
    <rect width="270" height="305" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="135" y="24" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--brand)" text-anchor="middle">SINGLETON PATTERN (CREATIONAL)</text>

    <!-- Singleton UML Class Box -->
    <g transform="translate(15, 45)">
      <rect width="240" height="150" rx="6" fill="var(--surface)" stroke="var(--brand)" stroke-width="1.8" />
      <text x="120" y="20" font-family="var(--font-display)" font-size="11" font-weight="700" fill="var(--brand)" text-anchor="middle">DatabaseConnectionPool</text>
      <line x1="0" y1="28" x2="240" y2="28" stroke="var(--border)" stroke-width="1" />
      <text x="10" y="45" font-family="var(--font-mono)" font-size="9" fill="var(--ink)">- _instance: DatabaseConnectionPool</text>
      <text x="10" y="62" font-family="var(--font-mono)" font-size="9" fill="var(--ink)">- connections: int = 10</text>
      <line x1="0" y1="72" x2="240" y2="72" stroke="var(--border)" stroke-width="1" />
      <text x="10" y="90" font-family="var(--font-mono)" font-size="9" fill="var(--ink)">- DatabaseConnectionPool()</text>
      <text x="10" y="108" font-family="var(--font-mono)" font-size="9" font-weight="700" fill="var(--brand)">+ getInstance(): Pool</text>
      <text x="10" y="126" font-family="var(--font-mono)" font-size="9" fill="var(--ink)">+ getConnection(): Connection</text>
      <text x="10" y="142" font-family="var(--font-mono)" font-size="9" fill="var(--ink)">+ releaseConnection(c)</text>
    </g>

    <text x="135" y="225" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--ink)" text-anchor="middle">Key Invariant:</text>
    <text x="135" y="245" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Private constructor ensures no direct 'new'.</text>
    <text x="135" y="260" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Global static access point returns</text>
    <text x="135" y="275" font-family="var(--font-mono)" font-size="8.5" fill="var(--brand)" text-anchor="middle">exactly one shared instance.</text>
  </g>

  <!-- Right: Observer Pattern -->
  <g transform="translate(315, 52)">
    <rect width="440" height="305" rx="10" fill="var(--surface-alt)" stroke="var(--border)" stroke-width="1.5" />
    <text x="220" y="24" font-family="var(--font-display)" font-size="11.5" font-weight="700" fill="var(--brand)" text-anchor="middle">OBSERVER PATTERN (BEHAVIORAL &bull; PUB/SUB)</text>

    <!-- Subject Interface/Class -->
    <g transform="translate(15, 45)">
      <rect width="180" height="105" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
      <text x="90" y="18" font-family="var(--font-display)" font-size="10.5" font-weight="700" fill="var(--ink)" text-anchor="middle">&laquo;Subject&raquo;</text>
      <line x1="0" y1="26" x2="180" y2="26" stroke="var(--border)" stroke-width="1" />
      <text x="8" y="42" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">- observers: List&lt;Observer&gt;</text>
      <line x1="0" y1="50" x2="180" y2="50" stroke="var(--border)" stroke-width="1" />
      <text x="8" y="66" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">+ attach(o: Observer)</text>
      <text x="8" y="82" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">+ detach(o: Observer)</text>
      <text x="8" y="98" font-family="var(--font-mono)" font-size="8.5" font-weight="700" fill="var(--brand)">+ notifyAll()</text>
    </g>

    <!-- Observer Interface -->
    <g transform="translate(245, 45)">
      <rect width="180" height="70" rx="6" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5" />
      <text x="90" y="18" font-family="var(--font-display)" font-size="10.5" font-weight="700" fill="var(--ink)" text-anchor="middle">&laquo;interface&raquo; Observer</text>
      <line x1="0" y1="26" x2="180" y2="26" stroke="var(--border)" stroke-width="1" />
      <line x1="0" y1="36" x2="180" y2="36" stroke="var(--border)" stroke-width="1" />
      <text x="8" y="54" font-family="var(--font-mono)" font-size="9" font-weight="700" fill="var(--brand)">+ update(state: Object)</text>
    </g>

    <!-- Association: Subject has 0..* Observers -->
    <line x1="195" y1="80" x2="243" y2="80" stroke="var(--brand)" stroke-width="1.5" marker-end="url(#dp-arr)" />
    <text x="219" y="74" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)" text-anchor="middle">1..*</text>

    <!-- Concrete Subject: WeatherStation -->
    <g transform="translate(15, 175)">
      <rect width="180" height="85" rx="6" fill="var(--surface)" stroke="var(--brand)" stroke-width="1.5" />
      <text x="90" y="18" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">WeatherStation</text>
      <line x1="0" y1="26" x2="180" y2="26" stroke="var(--border)" stroke-width="1" />
      <text x="8" y="42" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">- state: WeatherData</text>
      <line x1="0" y1="50" x2="180" y2="50" stroke="var(--border)" stroke-width="1" />
      <text x="8" y="66" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">+ getState(): Data</text>
      <text x="8" y="80" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">+ setState(d: Data)</text>
    </g>
    <!-- Inheritance arrow up to Subject -->
    <line x1="105" y1="175" x2="105" y2="152" stroke="var(--ink)" stroke-width="1.5" marker-end="url(#dp-inherit)" />

    <!-- Concrete Observer: WeatherDisplay -->
    <g transform="translate(245, 175)">
      <rect width="180" height="85" rx="6" fill="var(--surface)" stroke="var(--brand)" stroke-width="1.5" />
      <text x="90" y="18" font-family="var(--font-display)" font-size="10" font-weight="700" fill="var(--brand)" text-anchor="middle">PhoneDisplay / WindowDisplay</text>
      <line x1="0" y1="26" x2="180" y2="26" stroke="var(--border)" stroke-width="1" />
      <text x="8" y="42" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">- currentReading: String</text>
      <line x1="0" y1="50" x2="180" y2="50" stroke="var(--border)" stroke-width="1" />
      <text x="8" y="66" font-family="var(--font-mono)" font-size="8.5" fill="var(--brand)">+ update(state: Object)</text>
      <text x="8" y="80" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink)">+ render()</text>
    </g>
    <!-- Inheritance arrow up to Observer -->
    <line x1="335" y1="175" x2="335" y2="117" stroke="var(--ink)" stroke-width="1.5" marker-end="url(#dp-inherit)" />

    <text x="220" y="285" font-family="var(--font-mono)" font-size="8.5" fill="var(--ink-muted)" text-anchor="middle">Decoupled 1-to-many dependency: Subject notifies all registered observers automatically.</text>
  </g>
</svg>'''

if __name__ == "__main__":
    print("Testing SE Unit 3 SVG generators...")
    lay = generate_layered_repository_svg()
    comp = generate_compiler_pipeline_svg()
    dp = generate_design_patterns_svg()
    print(f"Generated Layered vs Repo: {len(lay)} bytes")
    print(f"Generated Compiler Pipeline: {len(comp)} bytes")
    print(f"Generated Design Patterns: {len(dp)} bytes")
