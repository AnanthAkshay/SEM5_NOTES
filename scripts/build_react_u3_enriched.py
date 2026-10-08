"""
build_react_u3_enriched.py - Enriches notes/reactjs/unit3/unit-3-notes.html with:
1. Academic Verification Box citing Chris Minnick (Wiley 2022), Fullstack React, and ISAEC594 Syllabus
2. Interactive Controlled Form & State Lifting Studio:
   - Tab 1: Scalable Multi-Field Controlled Form Studio (live JSON form state, computed property names, preventDefault)
   - Tab 2: Synchronized Temperature Converter (Lifting State Up, presets for boiling/freezing/body temp, boiling verdict)
3. Standardized Exam Archive & 6 Verified Practice Problems matching audit/verify/reactjs/verify_react_u3.js
"""

import re

def enrich_react_u3():
    with open('notes/reactjs/unit3/unit-3-notes.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Academic Box
    academic_box = '''
        <!-- Academic Verification & Syllabus Mapping Card -->
        <div class="academic-verification-box" style="margin: 1.5rem 0; padding: 1.25rem 1.5rem; background: var(--surface-alt); border-left: 4px solid var(--brand); border-radius: 8px; font-size: 0.92rem; line-height: 1.6;">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
            <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: var(--brand);"></span>
            <strong style="color: var(--brand); font-family: var(--font-display); text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.82rem;">Academic Verification &amp; Syllabus Alignment</strong>
          </div>
          <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
            <strong>Prescribed References:</strong> Chris Minnick, <em>Beginning ReactJS Foundations: Building User Interfaces with ReactJS - An Approachable Guide</em>, Wiley, 2022 (Chapters 7 &amp; 8: Events and Forms); Anthony Accomazzo et al., <em>Fullstack React: The Complete Guide to ReactJS and Friends</em>, 2017; Official React 18 Docs (<a href="https://react.dev/learn/responding-to-events" target="_blank" rel="noopener">Responding to Events</a> and <a href="https://react.dev/learn/sharing-state-between-components" target="_blank" rel="noopener">Sharing State Between Components</a>).
          </p>
          <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
            <strong>Curriculum &amp; Examination Scope:</strong> Course Code <strong>ISAEC594</strong> (Ability Enhancement Course: Front End Development using ReactJS, 1 Credit). Covers the SyntheticEvent system, event delegation, <code>e.preventDefault()</code>, controlled vs. uncontrolled components, multi-field form state with ES6 computed property names, and the Lifting State Up architectural pattern.
          </p>
          <p style="margin: 0; color: var(--ink-muted); font-size: 0.88rem;">
            <strong>Code &amp; Test Verification:</strong> SyntheticEvent simulation, computed property state handler (<code>Aditi Rao</code>, Semester <code>6</code>, <code>agreedToTerms: true</code>), and bidirectional temperature converter ($100^\\circ\\text{C} = 212^\\circ\\text{F}, 32^\\circ\\text{F} = 0^\\circ\\text{C}, 98.6^\\circ\\text{F} = 37^\\circ\\text{C}$) verified via automated test suite (<code>audit/verify/reactjs/verify_react_u3.js</code>).
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
      <!-- Interactive Controlled Form & State Lifting Studio -->
      <div id="react-forms-studio" class="interactive-widget-card" style="margin: 2.5rem 0; padding: 1.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--brand); font-weight: 700; letter-spacing: 0.05em;">Interactive Lab Explorer</div>
            <h3 style="margin: 0.2rem 0 0 0; font-family: var(--font-display); font-size: 1.25rem; color: var(--ink);">Controlled Forms &amp; Lifting State Up Studio</h3>
          </div>
          <div style="display: flex; gap: 0.5rem;" id="forms-tab-controls" role="tablist">
            <button id="tab-btn-form" class="pill-action-btn" role="tab" aria-selected="true" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">Tab 1: Multi-Field Form</button>
            <button id="tab-btn-lifting" class="pill-action-btn" role="tab" aria-selected="false" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; opacity: 0.7;">Tab 2: Synchronized Temp Converter</button>
          </div>
        </div>

        <!-- Panel 1: Multi-Field Form Studio -->
        <div id="panel-form" role="tabpanel" style="display: block;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Type into the inputs below to see how a single controlled handler utilizes ES6 computed property names <code>[e.target.name]: value</code> to keep React state as the single source of truth:
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
            <!-- Interactive Form Column -->
            <form id="interactive-reg-form" style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);" onsubmit="return false;">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.8rem;">Registration Form (Controlled)</div>

              <div style="margin-bottom: 0.75rem;">
                <label for="form-input-name" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">Full Name:</label>
                <input type="text" id="form-input-name" name="fullName" value="Aditi Rao" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.85rem;">
              </div>

              <div style="margin-bottom: 0.75rem;">
                <label for="form-input-email" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">College Email:</label>
                <input type="email" id="form-input-email" name="email" value="aditi.rao@msrit.edu" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.85rem;">
              </div>

              <div style="margin-bottom: 0.75rem;">
                <label for="form-input-sem" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.25rem;">Semester:</label>
                <select id="form-input-sem" name="semester" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.85rem;">
                  <option value="5">Semester V</option>
                  <option value="6" selected>Semester VI</option>
                  <option value="7">Semester VII</option>
                </select>
              </div>

              <div style="margin-bottom: 0.75rem;">
                <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; font-size: 0.85rem; color: var(--ink);">
                  <input type="checkbox" id="form-input-terms" name="agreedToTerms" checked style="accent-color: var(--brand); width: 16px; height: 16px;">
                  <span>Agree to academic honor code</span>
                </label>
              </div>

              <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
                <button type="submit" id="btn-submit-form" class="pill-action-btn" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">Submit (e.preventDefault)</button>
                <button type="button" id="btn-reset-form" class="pill-action-btn" style="padding: 0.35rem 0.8rem; font-size: 0.8rem;">Reset</button>
              </div>
              <div id="submit-feedback" style="font-size: 0.75rem; color: var(--brand); margin-top: 0.5rem; font-family: var(--font-mono); display: none;">
                ✓ SyntheticEvent.preventDefault() intercepted submission successfully.
              </div>
            </form>

            <!-- State & Code Inspector Column -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">Live Form State (Single Source of Truth)</div>

              <pre style="margin: 0 0 1rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); line-height: 1.45;"><code id="view-form-state-json">{
  "fullName": "Aditi Rao",
  "email": "aditi.rao@msrit.edu",
  "semester": "6",
  "agreedToTerms": true
}</code></pre>

              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase; margin-bottom: 0.3rem;">Evaluated Computed Property Handler:</div>
              <pre style="margin: 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ink); line-height: 1.45;"><code id="view-computed-handler">const { name, value, type, checked } = e.target;
setFormData(prev => ({
  ...prev,
  [name]: type === "checkbox" ? checked : value
}));</code></pre>
            </div>
          </div>
        </div>

        <!-- Panel 2: Synchronized Temperature Converter (Lifting State Up) -->
        <div id="panel-lifting" role="tabpanel" style="display: none;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Two sibling inputs synchronized in real time because state is lifted to their common ancestor <code>&lt;Calculator&gt;</code>:
          </p>

          <!-- Presets -->
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
            <span style="font-size: 0.8rem; color: var(--ink-muted); align-self: center;">Benchmarks:</span>
            <button id="preset-boiling" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem; border-color: var(--brand); color: var(--brand);">Boiling Point (100°C = 212°F)</button>
            <button id="preset-freezing" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Freezing Point (0°C = 32°F)</button>
            <button id="preset-body" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">Body Temp (37°C = 98.6°F)</button>
          </div>

          <!-- Dual Sibling Input Cards -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
            <!-- Sibling 1: Celsius -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700;">Sibling A: CelsiusInput</span>
                <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted);">scale="c"</span>
              </div>
              <label for="temp-input-c" style="display: block; font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Enter temperature in Celsius:</label>
              <input type="number" id="temp-input-c" value="100" step="any" style="width: 100%; padding: 0.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 1.1rem; font-weight: 700;">
            </div>

            <!-- Sibling 2: Fahrenheit -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700;">Sibling B: FahrenheitInput</span>
                <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted);">scale="f"</span>
              </div>
              <label for="temp-input-f" style="display: block; font-size: 0.85rem; color: var(--ink); margin-bottom: 0.35rem;">Enter temperature in Fahrenheit:</label>
              <input type="number" id="temp-input-f" value="212" step="any" style="width: 100%; padding: 0.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 1.1rem; font-weight: 700;">
            </div>
          </div>

          <!-- Boiling Verdict Card -->
          <div id="boiling-verdict-box" style="padding: 1rem 1.25rem; background: rgba(46, 195, 107, 0.12); border: 1.5px solid var(--brand); border-radius: 8px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <div style="font-size: 0.75rem; font-family: var(--font-mono); text-transform: uppercase; color: var(--brand); font-weight: 700;">Boiling Verdict (Sibling C: BoilingVerdict)</div>
              <div id="boiling-text" style="font-size: 1.05rem; font-weight: 700; color: var(--ink); margin-top: 0.2rem;">
                The water would boil. (&ge; 100°C)
              </div>
            </div>
            <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink-muted);">
              Calculated from lifted state: <code>celsius = (fahrenheit - 32) &times; 5 / 9</code>
            </div>
          </div>
        </div>
      </div>
'''

    # Insert interactive widget at the end of Section 7 (#sec-code-demos)
    sec_7_pos = content.find('id="sec-code-demos"')
    if sec_7_pos != -1:
        sec_7_end = content.find('</section>', sec_7_pos)
        if sec_7_end != -1:
            content = content[:sec_7_end] + '\n' + interactive_widget + '\n' + content[sec_7_end:]

    # 3. Standardize and enrich Section 9 with authentic questions and verified practice problems
    exam_start = content.find('<section id="exam-questions"')
    ref_start = content.find('<section id="sec-references"')

    if exam_start != -1 and ref_start != -1:
        new_exam_section = '''<section id="exam-questions" class="content-section exam-archive">
        <h2 class="section-title">9. Important Exam Questions &amp; Practice</h2>
        <p class="section-lead">The following conceptual questions and verified code tracing problems cover essential university examination patterns for <strong>ISAEC594 (Front End Development using ReactJS)</strong>:</p>

        <h3 class="subsection-title">2-Mark Conceptual Questions</h3>

        <!-- Q1 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">1. What is a SyntheticEvent in React and why does React use it?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>A <strong>SyntheticEvent</strong> is a cross-browser wrapper object around the browser's native DOM event. It provides identical properties and methods (e.g. <code>e.stopPropagation()</code>, <code>e.preventDefault()</code>) across Chrome, Safari, Firefox, and Edge according to the W3C event specification.</p>
            <p><strong>Reason for Use:</strong> Ensures complete cross-browser consistency and allows React to implement efficient root-level event delegation without attaching thousands of individual listeners to DOM nodes.</p>
          </div>
        </details>

        <!-- Q2 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">2. Distinguish between Controlled and Uncontrolled components in React forms.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ul>
              <li><strong>Controlled Component:</strong> The input value is driven directly by React local state (via <code>value={state}</code> and <code>onChange={handler}</code>). React state serves as the single source of truth. Every keystroke updates state and re-renders the input.</li>
              <li><strong>Uncontrolled Component:</strong> Form data is maintained internally by the browser's real DOM. React pulls values on demand when needed using a reference (<code>ref</code>) or standard form submission, typically using <code>defaultValue</code> for initial setup.</li>
            </ul>
          </div>
        </details>

        <!-- Q3 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">3. Why must `e.preventDefault()` be called in a form submit handler in React?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>By default, browser HTML forms submit an HTTP POST/GET request and initiate a full page reload. In Single Page Applications (SPAs) built with React, calling <code>e.preventDefault()</code> cancels the default browser form navigation, allowing JavaScript to handle validation and asynchronous network requests (e.g. <code>fetch</code> / <code>axios</code>) without losing in-memory application state.</p>
          </div>
        </details>

        <!-- Q4 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">4. How do ES6 computed property names enable a single handler to manage multiple form inputs?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>ES6 computed property syntax <code>[expression]: value</code> evaluates the key dynamically at runtime. By assigning each input element a <code>name</code> attribute matching its respective key in state, the handler reads <code>e.target.name</code> and updates that specific property: <code>setForm(prev =&gt; ({ ...prev, [e.target.name]: e.target.value }))</code>.</p>
          </div>
        </details>

        <!-- Q5 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">5. Why can sibling components in React not share state directly with one another?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>React strictly enforces a <strong>unidirectional (top-down) data flow</strong>: props can only be passed downward from parent to child. Sibling components possess no direct communication link. To share or synchronize state between siblings, state must be lifted to their closest common ancestor.</p>
          </div>
        </details>

        <h3 class="subsection-title">5-Mark &amp; 10-Mark Model Questions</h3>

        <!-- Q6 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">10 MARKS</span>
            <span class="q-title">6. Explain the architectural pattern of 'Lifting State Up' in detail with a diagram and code walkthrough.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Architectural Principle:</strong></p>
            <p>Often, several components need to reflect the same changing data. In React, rather than trying to synchronize state between separate local components, the state is <strong>lifted up</strong> to their closest common parent component.</p>
            <ol>
              <li><strong>Common Ancestor Ownership:</strong> The parent component maintains the shared state (e.g. <code>temperature</code> and <code>scale</code>) as the single source of truth.</li>
              <li><strong>Downwards Props:</strong> The parent passes down the current state to children via props (e.g. <code>temperature={celsius}</code>).</li>
              <li><strong>Upwards Callbacks:</strong> The parent passes event callback functions down to the children (e.g. <code>onTemperatureChange={handleCelsiusChange}</code>) so children can notify the parent when a user types an input.</li>
              <li><strong>Re-render Cascade:</strong> When the parent's state updates, all child components re-render with the freshly calculated synchronized values simultaneously.</li>
            </ol>
            <p><em>(Refer to the complete working Temperature Calculator implementation in Section 7).</em></p>
          </div>
        </details>

        <!-- Q7 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">5 MARKS</span>
            <span class="q-title">7. Write a complete React controlled component handling multiple inputs (text, email, select, checkbox) using a single handleChange method.</span>
          </summary>
          <div class="qa-answer">
            <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>import React, { useState } from 'react';

export default function RegistrationForm() {
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    semester: "5",
    agree: false
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitted payload:", formData);
  };

  return (
    &lt;form onSubmit={handleSubmit}&gt;
      &lt;input name="fullName" value={formData.fullName} onChange={handleChange} /&gt;
      &lt;input name="email" value={formData.email} onChange={handleChange} /&gt;
      &lt;select name="semester" value={formData.semester} onChange={handleChange}&gt;
        &lt;option value="5"&gt;V&lt;/option&gt;
        &lt;option value="6"&gt;VI&lt;/option&gt;
      &lt;/select&gt;
      &lt;input type="checkbox" name="agree" checked={formData.agree} onChange={handleChange} /&gt;
      &lt;button type="submit"&gt;Register&lt;/button&gt;
    &lt;/form&gt;
  );
}</code></pre>
          </div>
        </details>

        <h3 class="subsection-title">Verified Code Tracing &amp; Practice Problems</h3>

        <!-- Practice 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 1 &bull; SYNTHETICEVENT PREVENTDEFAULT SIMULATION</span>
          </div>
          <h4 class="problem-title">Trace the execution of <code>submitEvent.preventDefault()</code> and explain how it prevents browser reload in Single Page Applications.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Consider the SyntheticEvent mock implementation:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>function createSyntheticEvent(targetData) {
  let defaultPrevented = false;
  return {
    target: targetData,
    preventDefault: () => { defaultPrevented = true; },
    isDefaultPrevented: () => defaultPrevented
  };
}</code></pre>
              <ul>
                <li>When <code>submitEvent.preventDefault()</code> is invoked, internal flag <code>defaultPrevented</code> becomes <code>true</code>.</li>
                <li>Browser navigation to the form target URL is canceled; execution continues in JavaScript memory without page unmount.</li>
              </ul>
              <p><em>Verification:</em> Verified by automated test in <code>audit/verify/reactjs/verify_react_u3.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 2 &bull; MULTI-FIELD STATE COMPUTED PROPERTY TRACE</span>
          </div>
          <h4 class="problem-title">Trace state transitions for initial state: <code>{ fullName: "", semester: "5", agreedToTerms: false }</code> when updating name to "Aditi Rao", semester to "6", and agreedToTerms to true.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>function updateFormState(prevState, event) {
  const { name, value, type, checked } = event.target;
  const fieldValue = type === "checkbox" ? checked : value;
  return { ...prevState, [name]: fieldValue };
}</code></pre>
              <ol>
                <li>Text input event: <code>[fullName]: "Aditi Rao"</code> &rarr; <code>{ fullName: "Aditi Rao", semester: "5", agreedToTerms: false }</code>.</li>
                <li>Select event: <code>[semester]: "6"</code> &rarr; <code>{ fullName: "Aditi Rao", semester: "6", agreedToTerms: false }</code>.</li>
                <li>Checkbox event: <code>[agreedToTerms]: true</code> &rarr; <code>{ fullName: "Aditi Rao", semester: "6", agreedToTerms: true }</code>.</li>
              </ol>
              <p><em>Verification:</em> Verified by automated test in <code>audit/verify/reactjs/verify_react_u3.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 3 &bull; TEMPERATURE CONVERSION FORMULAS</span>
          </div>
          <h4 class="problem-title">Verify conversion output: (a) 100°C to Fahrenheit, (b) 32°F to Celsius, and (c) 98.6°F to Celsius.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Using formulas: $F = (C \times 9 / 5) + 32$ and $C = (F - 32) \times 5 / 9$:</p>
              <ul>
                <li><strong>(a) 100°C &rarr; °F:</strong> $(100 \times 9 / 5) + 32 = 180 + 32 = \mathbf{212^\circ\text{F}}$.</li>
                <li><strong>(b) 32°F &rarr; °C:</strong> $(32 - 32) \times 5 / 9 = 0 \times 5 / 9 = \mathbf{0^\circ\text{C}}$.</li>
                <li><strong>(c) 98.6°F &rarr; °C:</strong> $(98.6 - 32) \times 5 / 9 = 66.6 \times 5 / 9 = 333 / 9 = \mathbf{37^\circ\text{C}}$.</li>
              </ul>
              <p><em>Verification:</em> Verified by automated unit test in <code>audit/verify/reactjs/verify_react_u3.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 4 &bull; CHECKBOX VALUE VS CHECKED ATTRIBUTE</span>
          </div>
          <h4 class="problem-title">Why does reading <code>e.target.value</code> from an HTML checkbox cause a bug in React? What is the correct property?</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>Bug:</strong> Standard HTML checkbox elements always return the string <code>"on"</code> for <code>e.target.value</code> regardless of whether the box is checked or unchecked!</p>
              <p><strong>Fix:</strong> Read the boolean property <code>e.target.checked</code>:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>const value = e.target.type === "checkbox" ? e.target.checked : e.target.value;</code></pre>
            </div>
          </details>
        </div>

        <!-- Practice 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 5 &bull; TRYCONVERT ROBUST ERROR HANDLING</span>
          </div>
          <h4 class="problem-title">Write the implementation of <code>tryConvert(temperature, convertFn)</code> that handles empty strings, non-numeric inputs, and rounds to 3 decimal places.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>function tryConvert(temperature, convertFn) {
  const input = parseFloat(temperature);
  if (Number.isNaN(input)) {
    return "";
  }
  const output = convertFn(input);
  const rounded = Math.round(output * 1000) / 1000;
  return rounded.toString();
}</code></pre>
              <p>If user clears an input field, <code>parseFloat("")</code> is <code>NaN</code>, returning empty string <code>""</code> to clear the sibling input cleanly.</p>
            </div>
          </details>
        </div>

        <!-- Practice 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 6 &bull; CONTROLLED COMPONENT WARNING FIX</span>
          </div>
          <h4 class="problem-title">Explain the console warning: <em>"A component is changing an uncontrolled input to be controlled"</em> and show how to fix it.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>Cause:</strong> The input was initially rendered with <code>value={undefined}</code> (e.g. state was initialized to <code>undefined</code>), which React interprets as an uncontrolled input. When state updates to a string, React detects a transition to controlled mode, which can cause subtle synchronization bugs.</p>
              <p><strong>Fix:</strong> Always initialize string form states with an empty string <code>""</code> rather than <code>undefined</code> or <code>null</code>:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>// WRONG: causes warning
const [name, setName] = useState();

// CORRECT: guaranteed controlled from mount
const [name, setName] = useState("");</code></pre>
            </div>
          </details>
        </div>
      </section>'''
        content = content[:exam_start] + new_exam_section + '\n\n      ' + content[ref_start:]

    # 4. Interactive Widget JavaScript Engine
    widget_script = '''
  <!-- Interactive Controlled Forms & State Lifting Studio Engine -->
  <script>
  (function() {
    // Tab switching
    var tabForm = document.getElementById('tab-btn-form');
    var tabLifting = document.getElementById('tab-btn-lifting');
    var panelForm = document.getElementById('panel-form');
    var panelLifting = document.getElementById('panel-lifting');

    if (tabForm && tabLifting && panelForm && panelLifting) {
      tabForm.addEventListener('click', function() {
        tabForm.style.borderColor = 'var(--brand)';
        tabForm.style.color = 'var(--brand)';
        tabForm.style.opacity = '1';
        tabForm.setAttribute('aria-selected', 'true');

        tabLifting.style.borderColor = 'var(--border)';
        tabLifting.style.color = 'var(--ink)';
        tabLifting.style.opacity = '0.7';
        tabLifting.setAttribute('aria-selected', 'false');

        panelForm.style.display = 'block';
        panelLifting.style.display = 'none';
      });

      tabLifting.addEventListener('click', function() {
        tabLifting.style.borderColor = 'var(--brand)';
        tabLifting.style.color = 'var(--brand)';
        tabLifting.style.opacity = '1';
        tabLifting.setAttribute('aria-selected', 'true');

        tabForm.style.borderColor = 'var(--border)';
        tabForm.style.color = 'var(--ink)';
        tabForm.style.opacity = '0.7';
        tabForm.setAttribute('aria-selected', 'false');

        panelLifting.style.display = 'block';
        panelForm.style.display = 'none';
      });
    }

    // Panel 1: Multi-field form engine
    var formState = {
      fullName: "Aditi Rao",
      email: "aditi.rao@msrit.edu",
      semester: "6",
      agreedToTerms: true
    };

    var inpName = document.getElementById('form-input-name');
    var inpEmail = document.getElementById('form-input-email');
    var selSem = document.getElementById('form-input-sem');
    var chkTerms = document.getElementById('form-input-terms');
    var outStateJson = document.getElementById('view-form-state-json');
    var outComputed = document.getElementById('view-computed-handler');
    var btnSubmit = document.getElementById('btn-submit-form');
    var btnReset = document.getElementById('btn-reset-form');
    var feedback = document.getElementById('submit-feedback');

    function syncFormState(lastField) {
      if (outStateJson) {
        outStateJson.textContent = JSON.stringify(formState, null, 2);
      }
      if (outComputed && lastField) {
        outComputed.textContent = '// Handled event for field: "' + lastField + '"\\nsetFormData(prev => ({\\n  ...prev,\\n  ["' + lastField + '"]: ' + JSON.stringify(formState[lastField]) + '\\n}));';
      }
    }

    if (inpName) {
      inpName.addEventListener('input', function() {
        formState.fullName = inpName.value;
        syncFormState('fullName');
      });
    }
    if (inpEmail) {
      inpEmail.addEventListener('input', function() {
        formState.email = inpEmail.value;
        syncFormState('email');
      });
    }
    if (selSem) {
      selSem.addEventListener('change', function() {
        formState.semester = selSem.value;
        syncFormState('semester');
      });
    }
    if (chkTerms) {
      chkTerms.addEventListener('change', function() {
        formState.agreedToTerms = chkTerms.checked;
        syncFormState('agreedToTerms');
      });
    }

    if (btnSubmit) {
      btnSubmit.addEventListener('click', function(e) {
        e.preventDefault();
        if (feedback) {
          feedback.style.display = 'block';
          feedback.textContent = '✓ SyntheticEvent.preventDefault() called for ' + formState.fullName + ' (' + formState.email + ')';
        }
      });
    }

    if (btnReset) {
      btnReset.addEventListener('click', function() {
        formState = {
          fullName: "Student",
          email: "student@msrit.edu",
          semester: "5",
          agreedToTerms: false
        };
        if (inpName) inpName.value = formState.fullName;
        if (inpEmail) inpEmail.value = formState.email;
        if (selSem) selSem.value = formState.semester;
        if (chkTerms) chkTerms.checked = formState.agreedToTerms;
        if (feedback) feedback.style.display = 'none';
        syncFormState('reset');
      });
    }

    // Panel 2: Temperature conversion engine (Lifting State Up)
    function toCelsius(f) {
      return (f - 32) * 5 / 9;
    }
    function toFahrenheit(c) {
      return (c * 9 / 5) + 32;
    }
    function tryConvert(temperature, convertFn) {
      var input = parseFloat(temperature);
      if (Number.isNaN(input)) {
        return "";
      }
      var output = convertFn(input);
      var rounded = Math.round(output * 1000) / 1000;
      return rounded.toString();
    }

    var inpC = document.getElementById('temp-input-c');
    var inpF = document.getElementById('temp-input-f');
    var verdictBox = document.getElementById('boiling-verdict-box');
    var verdictText = document.getElementById('boiling-text');

    function updateVerdict(celsiusVal) {
      var c = parseFloat(celsiusVal);
      if (!Number.isNaN(c) && c >= 100) {
        if (verdictBox) {
          verdictBox.style.background = 'rgba(46, 195, 107, 0.15)';
          verdictBox.style.borderColor = 'var(--brand)';
        }
        if (verdictText) {
          verdictText.textContent = 'The water would boil. (' + c + '°C >= 100°C)';
          verdictText.style.color = 'var(--brand)';
        }
      } else {
        if (verdictBox) {
          verdictBox.style.background = 'rgba(59, 130, 246, 0.1)';
          verdictBox.style.borderColor = 'rgba(59, 130, 246, 0.4)';
        }
        if (verdictText) {
          verdictText.textContent = 'The water would not boil. (' + (Number.isNaN(c) ? '0' : c) + '°C < 100°C)';
          verdictText.style.color = '#3b82f6';
        }
      }
    }

    if (inpC && inpF) {
      inpC.addEventListener('input', function() {
        var cVal = inpC.value;
        inpF.value = tryConvert(cVal, toFahrenheit);
        updateVerdict(cVal);
      });

      inpF.addEventListener('input', function() {
        var fVal = inpF.value;
        var cVal = tryConvert(fVal, toCelsius);
        inpC.value = cVal;
        updateVerdict(cVal);
      });
    }

    function applyTempBenchmark(cVal, fVal) {
      if (inpC) inpC.value = cVal;
      if (inpF) inpF.value = fVal;
      updateVerdict(cVal);
    }

    var btnBoil = document.getElementById('preset-boiling');
    var btnFreeze = document.getElementById('preset-freezing');
    var btnBody = document.getElementById('preset-body');

    if (btnBoil) btnBoil.addEventListener('click', function() { applyTempBenchmark("100", "212"); });
    if (btnFreeze) btnFreeze.addEventListener('click', function() { applyTempBenchmark("0", "32"); });
    if (btnBody) btnBody.addEventListener('click', function() { applyTempBenchmark("37", "98.6"); });
  })();
  </script>
'''

    # Insert script right before closing </body>
    body_end = '</body>'
    bpos = content.rfind(body_end)
    if bpos != -1:
        content = content[:bpos] + widget_script + '\n' + content[bpos:]

    with open('notes/reactjs/unit3/unit-3-notes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully enriched notes/reactjs/unit3/unit-3-notes.html!")

if __name__ == '__main__':
    enrich_react_u3()
