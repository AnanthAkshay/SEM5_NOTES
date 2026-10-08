"""
build_react_u1_enriched.py - Enriches notes/reactjs/unit1/unit-1-notes.html with:
1. Academic Verification Box citing Chris Minnick (Wiley 2022), Fullstack React, and ISAEC594 Syllabus
2. Interactive JSX Compilation & Virtual DOM Diffing Studio:
   - Tab 1: JSX Babel Transpiler & Virtual DOM AST Inspector (live presets, createElement code, JSON AST, DOM output)
   - Tab 2: Conditional & List Rendering Sandbox (interactive name, auth toggle, message slider, live status & mapped list)
3. Standardized Exam Archive & 6 Verified Practice Problems matching audit/verify/reactjs/verify_react_u1.js
"""

import re

def enrich_react_u1():
    with open('notes/reactjs/unit1/unit-1-notes.html', 'r', encoding='utf-8') as f:
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
            <strong>Prescribed References:</strong> Chris Minnick, <em>Beginning ReactJS Foundations: Building User Interfaces with ReactJS - An Approachable Guide</em>, Wiley, 2022 (Chapters 1, 2 &amp; 3); Anthony Accomazzo et al., <em>Fullstack React: The Complete Guide to ReactJS and Friends</em>, 2017; Official React 18 Docs (<a href="https://react.dev" target="_blank" rel="noopener">react.dev</a>) and Vite Guides (<a href="https://vitejs.dev/guide/" target="_blank" rel="noopener">vitejs.dev</a>).
          </p>
          <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
            <strong>Curriculum &amp; Examination Scope:</strong> Course Code <strong>ISAEC594</strong> (Ability Enhancement Course: Front End Development using ReactJS, 1 Credit). Covers declarative UI philosophy, Virtual DOM and $O(n)$ heuristic reconciliation, Vite project structure, JSX compilation mechanics, and conditional/list rendering patterns.
          </p>
          <p style="margin: 0; color: var(--ink-muted); font-size: 0.88rem;">
            <strong>Code &amp; Test Verification:</strong> All JSX AST object hierarchies, conditional greeting traces (<code>"Welcome Back! (3 new)"</code> vs <code>"Please Sign In"</code>), and list key associations (<code>key="c1"</code>) verified via automated test suite (<code>audit/verify/reactjs/verify_react_u1.js</code>).
          </p>
        </div>'''

    # Insert academic box right after source-links-card inside header
    source_links_idx = content.find('</div>\n      </header>')
    if source_links_idx != -1:
        content = content[:source_links_idx + 6] + '\n' + academic_box + content[source_links_idx + 6:]
    else:
        # fallback
        header_end = '</header>'
        pos = content.find(header_end)
        if pos != -1:
            content = content[:pos] + academic_box + '\n      ' + content[pos:]

    # 2. Interactive Widget
    interactive_widget = '''
      <!-- Interactive JSX Compilation & Virtual DOM Diffing Studio -->
      <div id="react-jsx-studio" class="interactive-widget-card" style="margin: 2.5rem 0; padding: 1.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--brand); font-weight: 700; letter-spacing: 0.05em;">Interactive Lab Explorer</div>
            <h3 style="margin: 0.2rem 0 0 0; font-family: var(--font-display); font-size: 1.25rem; color: var(--ink);">JSX Compilation &amp; Virtual DOM Diffing Studio</h3>
          </div>
          <div style="display: flex; gap: 0.5rem;" id="studio-tab-controls" role="tablist">
            <button id="tab-btn-transpile" class="pill-action-btn" role="tab" aria-selected="true" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">Tab 1: JSX &amp; VDOM AST</button>
            <button id="tab-btn-rendering" class="pill-action-btn" role="tab" aria-selected="false" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; opacity: 0.7;">Tab 2: Conditional &amp; List Sandbox</button>
          </div>
        </div>

        <!-- Panel 1: JSX Transpiler & VDOM AST Inspector -->
        <div id="panel-transpile" role="tabpanel" style="display: block;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Select a JSX code pattern to inspect how the Babel compiler converts it into pure <code>React.createElement()</code> function calls, constructs the in-memory <strong>Virtual DOM Tree Object</strong>, and finally renders the real DOM nodes:
          </p>

          <!-- Preset selector buttons -->
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
            <span style="font-size: 0.8rem; color: var(--ink-muted); align-self: center;">Code Presets:</span>
            <button id="preset-card" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem; border-color: var(--brand); color: var(--brand);">1. User Profile Card</button>
            <button id="preset-cart" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">2. Conditional Cart Badge</button>
            <button id="preset-list" class="pill-action-btn" style="padding: 0.25rem 0.6rem; font-size: 0.75rem;">3. Course List Item with Key</button>
          </div>

          <!-- 3-Way Inspection Grid -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
            <!-- Column 1: JSX Source -->
            <div style="padding: 1rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">1. Author's JSX Source</div>
              <pre style="margin: 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; overflow-x: auto; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); line-height: 1.45;"><code id="view-jsx-source">&lt;div className="card"&gt;
  &lt;h1&gt;Hello {user.name}&lt;/h1&gt;
  &lt;p&gt;Active: {user.active ? "Yes" : "No"}&lt;/p&gt;
&lt;/div&gt;</code></pre>
            </div>

            <!-- Column 2: Compiled JavaScript -->
            <div style="padding: 1rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">2. Babel Transpiled Output</div>
              <pre style="margin: 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; overflow-x: auto; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); line-height: 1.45;"><code id="view-babel-output">React.createElement("div", { className: "card" },
  React.createElement("h1", null, "Hello " + user.name),
  React.createElement("p", null, "Active: " + (user.active ? "Yes" : "No"))
);</code></pre>
            </div>
          </div>

          <!-- Bottom Grid: VDOM AST & Real DOM Live Preview -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
            <!-- VDOM Object -->
            <div style="padding: 1rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">3. In-Memory Virtual DOM (AST Object)</div>
              <pre style="margin: 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; overflow-x: auto; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ink); max-height: 180px;"><code id="view-vdom-ast">{
  "type": "div",
  "props": {
    "className": "card",
    "children": [
      { "type": "h1", "props": { "children": "Hello Ananya" } },
      { "type": "p", "props": { "children": "Active: Yes" } }
    ]
  }
}</code></pre>
            </div>

            <!-- Real DOM Live Preview -->
            <div style="padding: 1rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">4. Browser DOM Output (Rendered Result)</div>
              <div id="view-dom-preview" style="padding: 0.75rem; background: var(--surface); border: 1px dashed var(--brand); border-radius: 6px; min-height: 120px; display: flex; flex-direction: column; justify-content: center;">
                <div style="font-weight: 700; font-size: 1.1rem; color: var(--ink);">Hello Ananya</div>
                <div style="font-size: 0.85rem; color: var(--ink-muted); margin-top: 0.25rem;">Active: <span style="color: var(--brand); font-weight: 600;">Yes</span></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Panel 2: Conditional & List Rendering Sandbox -->
        <div id="panel-rendering" role="tabpanel" style="display: none;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Adjust the application state below to see how JavaScript conditional expressions and array <code>.map()</code> transformations evaluate in real-time:
          </p>

          <!-- Interactive State Controls -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1.25rem; padding: 1rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
            <div>
              <label for="state-user-name" style="display: block; font-family: var(--font-mono); font-size: 0.82rem; color: var(--ink); margin-bottom: 0.35rem;">
                User Name:
              </label>
              <input type="text" id="state-user-name" value="Ananya" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.88rem;">
            </div>

            <div>
              <label style="display: block; font-family: var(--font-mono); font-size: 0.82rem; color: var(--ink); margin-bottom: 0.35rem;">
                Authentication State:
              </label>
              <label style="display: flex; align-items: center; gap: 0.5rem; margin-top: 0.45rem; cursor: pointer; font-size: 0.88rem; color: var(--ink);">
                <input type="checkbox" id="state-is-logged-in" checked style="accent-color: var(--brand); width: 16px; height: 16px;">
                <span><code>isLoggedIn = true</code></span>
              </label>
            </div>

            <div>
              <label for="state-unread-count" style="display: block; font-family: var(--font-mono); font-size: 0.82rem; color: var(--ink); margin-bottom: 0.35rem;">
                Unread Messages: <span id="val-unread-count" style="font-weight: 700; color: var(--brand);">3</span>
              </label>
              <input type="range" id="state-unread-count" min="0" max="10" value="3" style="width: 100%; accent-color: var(--brand); margin-top: 0.35rem;">
            </div>

            <div>
              <label for="state-course-filter" style="display: block; font-family: var(--font-mono); font-size: 0.82rem; color: var(--ink); margin-bottom: 0.35rem;">
                Filter Courses:
              </label>
              <select id="state-course-filter" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.85rem;">
                <option value="all">All Enrolled (3)</option>
                <option value="high">High Credits (&ge; 4 Credits)</option>
                <option value="low">AEC Course (&lt; 4 Credits)</option>
              </select>
            </div>
          </div>

          <!-- Dynamic Evaluation Outputs -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
            <!-- Greeting Card -->
            <div style="padding: 1.25rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Conditional Status Output</div>
              <div id="res-greeting-text" style="font-family: var(--font-display); font-size: 1.35rem; font-weight: 800; color: var(--brand); margin: 0.5rem 0;">
                Welcome Back! (3 new)
              </div>
              <div style="font-family: var(--font-mono); font-size: 0.78rem; color: var(--ink-muted);">
                Expression: <code>{isLoggedIn ? "Welcome Back!" : "Please Sign In"} {isLoggedIn &amp;&amp; unread &gt; 0 &amp;&amp; `(${unread} new)`}</code>
              </div>
            </div>

            <!-- List Card -->
            <div style="padding: 1.25rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase;">Mapped List Elements</span>
                <span id="res-courses-count" style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); font-weight: 700;">3 items rendered</span>
              </div>
              <ul id="res-course-ul" style="margin: 0; padding-left: 1.2rem; font-size: 0.85rem; color: var(--ink); line-height: 1.6;">
                <li><span style="background: rgba(46,195,107,0.15); color: var(--brand); padding: 0.1rem 0.35rem; border-radius: 4px; font-family: var(--font-mono); font-size: 0.75rem; margin-right: 0.3rem;">key="c1"</span> <strong>ReactJS Fundamentals</strong> (1 Credits)</li>
                <li><span style="background: rgba(46,195,107,0.15); color: var(--brand); padding: 0.1rem 0.35rem; border-radius: 4px; font-family: var(--font-mono); font-size: 0.75rem; margin-right: 0.3rem;">key="c2"</span> <strong>Machine Learning</strong> (4 Credits)</li>
                <li><span style="background: rgba(46,195,107,0.15); color: var(--brand); padding: 0.1rem 0.35rem; border-radius: 4px; font-family: var(--font-mono); font-size: 0.75rem; margin-right: 0.3rem;">key="c3"</span> <strong>Computer Networks</strong> (4 Credits)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
'''

    # Insert interactive widget at the end of Section 9 (#sec-jsx-compilation)
    sec_9_pos = content.find('id="sec-jsx-compilation"')
    if sec_9_pos != -1:
        sec_9_end = content.find('</section>', sec_9_pos)
        if sec_9_end != -1:
            content = content[:sec_9_end] + '\n' + interactive_widget + '\n' + content[sec_9_end:]

    # 3. Standardize and enrich Section 12 with authentic questions and verified practice problems
    exam_start = content.find('<section id="exam-questions"')
    ref_start = content.find('<section id="sec-references"')

    if exam_start != -1 and ref_start != -1:
        new_exam_section = '''<section id="exam-questions" class="content-section exam-archive">
        <h2 class="section-title">12. Important Exam Questions &amp; Practice</h2>
        <p class="section-lead">The following conceptual questions and verified code tracing problems cover key university examination patterns for <strong>ISAEC594 (Front End Development using ReactJS)</strong>:</p>

        <h3 class="subsection-title">2-Mark Conceptual Questions</h3>

        <!-- Q1 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">1. What is the Virtual DOM and how does React reconciliation improve application performance?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>The <strong>Virtual DOM</strong> is a lightweight, tree-structured JavaScript object representation of the browser's actual DOM kept in memory.</p>
            <ul>
              <li>When application state transitions occur, React re-renders the Virtual DOM tree in memory and compares it against the previous snapshot using an $O(n)$ heuristic diffing algorithm called <strong>reconciliation</strong>.</li>
              <li>Rather than causing expensive global page reflows and repaints in the browser, React calculates the minimal set of real DOM mutations required and applies them in a single optimized batch update.</li>
            </ul>
          </div>
        </details>

        <!-- Q2 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">2. State three fundamental syntax rules of JSX and explain why each is required.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ol>
              <li><strong>Single Root Element:</strong> Every component must return exactly one parent root element or a Fragment (<code>&lt;&gt;...&lt;/&gt;</code>). <em>Reason:</em> JSX compiles to a single function call (<code>React.createElement(...)</code>), which can only return a single JavaScript value.</li>
              <li><strong>Explicit Closing of All Tags:</strong> All tags must be explicitly closed, including void/self-closing elements (e.g. <code>&lt;img /&gt;</code>, <code>&lt;input /&gt;</code>, <code>&lt;br /&gt;</code>). <em>Reason:</em> JSX follows XML/XHTML well-formed syntax strictly.</li>
              <li><strong>camelCase Attribute Naming:</strong> HTML attributes must be written in camelCase (e.g. <code>className</code> instead of <code>class</code>, <code>htmlFor</code> instead of <code>for</code>, <code>tabIndex</code>). <em>Reason:</em> <code>class</code> and <code>for</code> are reserved keywords in JavaScript.</li>
            </ol>
          </div>
        </details>

        <!-- Q3 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">3. Why should array indices not be used as the 'key' prop when rendering dynamic lists in React?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>Using array index (e.g., <code>key={index}</code>) ties element identity to its sequential array position rather than its actual data identity.</p>
            <ul>
              <li>If items in the list are reordered, inserted at the beginning, or filtered out, their numerical index changes.</li>
              <li>React's reconciliation algorithm assumes the item at index 0 is the same node across renders, causing severe bugs such as uncontrolled component state retention (e.g., text remaining in swapped input fields), broken transitions, and performance degradation. Unique, persistent entity IDs (e.g., <code>key={item.id}</code>) must always be used.</li>
            </ul>
          </div>
        </details>

        <!-- Q4 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">4. Distinguish between JavaScript expressions and statements in JSX. Give an example of an invalid JSX embedding.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ul>
              <li><strong>Expressions:</strong> Code constructs that evaluate to a single value (e.g., variable references, ternaries <code>a ? b : c</code>, function calls, arithmetic). Expressions can be embedded inside curly braces <code>{expression}</code> in JSX.</li>
              <li><strong>Statements:</strong> Code constructs that perform an action or control flow but do not evaluate directly to a value (e.g., <code>if (...)</code>, <code>for (...)</code>, <code>while (...)</code>, <code>switch</code>).</li>
              <li><strong>Invalid JSX Example:</strong> <code>&lt;div&gt;{if (user.active) { "Active" }}&lt;/div&gt;</code> results in a JavaScript syntax error because an <code>if</code> statement cannot be passed as an argument to <code>React.createElement()</code>. The valid alternative is ternary: <code>&lt;div&gt;{user.active ? "Active" : "Inactive"}&lt;/div&gt;</code>.</li>
            </ul>
          </div>
        </details>

        <!-- Q5 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">5. What is meant by unidirectional (one-way) data flow, and why is it beneficial?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>In React, data strictly flows in one direction: from parent components down to child components via immutable <strong>props</strong>. Child components cannot directly modify the props they receive; they can only notify parents by invoking callback functions passed down as props.</p>
            <p><strong>Benefits:</strong> Eliminates hidden side-effects, guarantees deterministic application state, simplifies debugging through predictable top-down data cascades, and prevents cyclical state dependency cascades.</p>
          </div>
        </details>

        <h3 class="subsection-title">5-Mark &amp; 10-Mark Model Questions</h3>

        <!-- Q6 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">10 MARKS</span>
            <span class="q-title">6. Compare React with Angular and Vue.js across key architectural dimensions.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Comprehensive Architectural Comparison:</strong></p>
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr>
                    <th>Dimension</th>
                    <th>React (Meta)</th>
                    <th>Angular (Google)</th>
                    <th>Vue.js (Evan You)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Classification</strong></td>
                    <td>UI Library (unopinionated; routing and state managed by ecosystem)</td>
                    <td>Complete Framework (batteries-included: CLI, forms, router, HTTP, DI)</td>
                    <td>Progressive Framework (incrementally adoptable core + official ecosystem)</td>
                  </tr>
                  <tr>
                    <td><strong>Syntax / Templates</strong></td>
                    <td>JSX (JavaScript XML with pure JS logic)</td>
                    <td>HTML enhanced with directives (<code>*ngIf</code>, <code>*ngFor</code>)</td>
                    <td>SFC (Single File Components with <code>&lt;template&gt;</code>, <code>&lt;script&gt;</code>, <code>&lt;style&gt;</code>)</td>
                  </tr>
                  <tr>
                    <td><strong>Data Binding</strong></td>
                    <td>Strictly Unidirectional (one-way data flow via props)</td>
                    <td>Two-way data binding (<code>[(ngModel)]</code>) &amp; unidirectional</td>
                    <td>Two-way model binding (<code>v-model</code>) on top of one-way props</td>
                  </tr>
                  <tr>
                    <td><strong>DOM Abstraction</strong></td>
                    <td>Virtual DOM with Fiber reconciler</td>
                    <td>Incremental DOM (compiles templates into direct DOM instructions)</td>
                    <td>Optimized Virtual DOM with compile-time flag optimizations</td>
                  </tr>
                  <tr>
                    <td><strong>Language Primary</strong></td>
                    <td>JavaScript (ES6+) or TypeScript</td>
                    <td>TypeScript (enforced by default)</td>
                    <td>JavaScript or TypeScript</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </details>

        <!-- Q7 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">5 MARKS</span>
            <span class="q-title">7. Explain the reconciliation algorithm in React. How does React achieve $O(n)$ time complexity?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>Theoretical minimum algorithms for comparing two arbitrary trees require $O(n^3)$ operations (where $n$ is the total count of tree nodes). In a web application with 1,000 DOM nodes, an $O(n^3)$ algorithm would require one billion comparisons per render cycle, completely stalling the browser thread.</p>
            <p>React implements an $O(n)$ heuristic diffing algorithm based on two fundamental assumptions:</p>
            <ol>
              <li><strong>Elements of Different Types Produce Different Trees:</strong> Whenever the root element type changes (e.g. from <code>&lt;div&gt;</code> to <code>&lt;span&gt;</code>, or <code>&lt;Header&gt;</code> to <code>&lt;Nav&gt;</code>), React unmounts the entire old subtree and recreates the new DOM subtree from scratch without inspecting deeper children.</li>
              <li><strong>Keys Identify Stable Children Across Renders:</strong> For children lists, React uses the unique <code>key</code> prop to match children in the original tree with children in the subsequent tree. This allows React to detect insertions, deletions, and moves in linear $O(n)$ time rather than checking all permutations.</li>
            </ol>
          </div>
        </details>

        <!-- Q8 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">5 MARKS</span>
            <span class="q-title">8. Explain why modern React development replaced Create React App (CRA) with Vite. Contrast their architectural approaches.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ul>
              <li><strong>Create React App (CRA / Webpack Architecture):</strong> CRA relies on Webpack, which bundles the entire application source code and all node_modules into monolithic bundles before starting the development server. As the codebase expands to hundreds of modules, server startup takes 30-90 seconds, and Hot Module Replacement (HMR) experiences perceptible multi-second lag.</li>
              <li><strong>Vite Architecture (Native ESM + esbuild):</strong>
                <ul>
                  <li><strong>Instant Dev Server Startup:</strong> Vite serves source code over native browser ES Modules (<code>import</code> / <code>export</code>). The browser requests modules on-demand as they are needed, eliminating bundle wait time.</li>
                  <li><strong>Fast Dependency Pre-bundling:</strong> Dependencies written in CommonJS or UMD are pre-bundled using <strong>esbuild</strong> (written in Go), which executes 10&times; to 100&times; faster than JS-based bundlers.</li>
                  <li><strong>Instant Hot Module Replacement (HMR):</strong> When a file is edited, Vite invalidates and re-transpiles only that specific module over native ESM, keeping HMR speed constant regardless of total project size.</li>
                </ul>
              </li>
            </ul>
          </div>
        </details>

        <h3 class="subsection-title">Verified Code Tracing &amp; Practice Problems</h3>

        <!-- Practice 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 1 &bull; VIRTUAL DOM TREE CONSTRUCTION</span>
          </div>
          <h4 class="problem-title">Write the exact JavaScript object (AST) generated by React for the following JSX: <code>&lt;div className="card"&gt;&lt;h1&gt;Hello Ananya&lt;/h1&gt;&lt;p&gt;Active: Yes&lt;/p&gt;&lt;/div&gt;</code>.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>React compiles JSX into <code>React.createElement(type, props, ...children)</code> calls, which construct a plain JavaScript object tree:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>{
  type: "div",
  props: {
    className: "card",
    children: [
      {
        type: "h1",
        props: { children: "Hello Ananya" }
      },
      {
        type: "p",
        props: { children: "Active: Yes" }
      }
    ]
  }
}</code></pre>
              <p><em>Verification:</em> Verified by automated test in <code>audit/verify/reactjs/verify_react_u1.js</code> (Asserts <code>vdom.type === "div"</code> and <code>vdom.props.className === "card"</code>).</p>
            </div>
          </details>
        </div>

        <!-- Practice 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 2 &bull; CONDITIONAL GREETING &amp; BADGE TRACE</span>
          </div>
          <h4 class="problem-title">Trace the output of <code>renderStatus(isLoggedIn, unreadCount)</code> for (a) <code>isLoggedIn = true, unreadCount = 3</code> and (b) <code>isLoggedIn = false, unreadCount = 0</code>.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Consider the conditional rendering logic:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>function renderStatus(isLoggedIn, unreadCount) {
  const greeting = isLoggedIn ? "Welcome Back!" : "Please Sign In";
  const badge = isLoggedIn && unreadCount > 0 ? `(${unreadCount} new)` : "";
  return `${greeting} ${badge}`.trim();
}</code></pre>
              <ul>
                <li><strong>Case (a):</strong> <code>greeting = "Welcome Back!"</code>; <code>badge = "(3 new)"</code>. Concatenated output: <code>"Welcome Back! (3 new)"</code>.</li>
                <li><strong>Case (b):</strong> <code>greeting = "Please Sign In"</code>; <code>badge = ""</code>. Concatenated output: <code>"Please Sign In"</code>.</li>
              </ul>
              <p><em>Verification:</em> Verified by automated test in <code>audit/verify/reactjs/verify_react_u1.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 3 &bull; LIST TRANSFORMATION WITH KEYS</span>
          </div>
          <h4 class="problem-title">Given array <code>courses = [{id: "c1", title: "ReactJS", credits: 1}, {id: "c2", title: "ML", credits: 4}, {id: "c3", title: "CN", credits: 4}]</code>, trace the mapped elements and confirm the key property.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Mapped JSX expression: <code>courses.map(c =&gt; &lt;li key={c.id}&gt;{c.title} ({c.credits} Credits)&lt;/li&gt;)</code></p>
              <ul>
                <li>Element 0: <code>&lt;li key="c1"&gt;ReactJS (1 Credits)&lt;/li&gt;</code> &rarr; <code>props.key = "c1"</code></li>
                <li>Element 1: <code>&lt;li key="c2"&gt;ML (4 Credits)&lt;/li&gt;</code> &rarr; <code>props.key = "c2"</code></li>
                <li>Element 2: <code>&lt;li key="c3"&gt;CN (4 Credits)&lt;/li&gt;</code> &rarr; <code>props.key = "c3"</code></li>
              </ul>
              <p><strong>Total elements produced:</strong> 3. Each child possesses a unique, stable, persistent identifier adhering to React reconciliation requirements.</p>
            </div>
          </details>
        </div>

        <!-- Practice 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 4 &bull; FALSY VALUE SHORT-CIRCUIT TRAP</span>
          </div>
          <h4 class="problem-title">What gets rendered in the browser DOM for <code>&lt;div&gt;{unreadCount &amp;&amp; &lt;span&gt;New Items&lt;/span&gt;}&lt;/div&gt;</code> when <code>unreadCount = 0</code>? Explain why this happens and provide the fix.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>Unexpected Output:</strong> The browser renders <code>&lt;div&gt;0&lt;/div&gt;</code>!</p>
              <p><strong>Explanation:</strong> In JavaScript, the short-circuit operator <code>&amp;&amp;</code> evaluates the left-hand side. If it is falsy, it returns that falsy value immediately. Since <code>0</code> is falsy, the expression evaluates to the number <code>0</code>. While React does not render <code>false</code>, <code>null</code>, or <code>undefined</code>, it <strong>does render numbers</strong>, so the digit <code>0</code> is injected directly into the DOM.</p>
              <p><strong>Recommended Fix:</strong> Coerce to boolean or compare explicitly:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>{/* Fix 1: Explicit comparison */}
{unreadCount > 0 && <span>New Items</span>}

{/* Fix 2: Boolean conversion */}
{Boolean(unreadCount) && <span>New Items</span>}</code></pre>
            </div>
          </details>
        </div>

        <!-- Practice 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 5 &bull; BABEL TRANSPILATION OF NESTED JSX</span>
          </div>
          <h4 class="problem-title">Show the transpiled JavaScript function calls for: <code>&lt;nav id="main"&gt;&lt;a href="/home" className="active"&gt;Home&lt;/a&gt;&lt;/nav&gt;</code>.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>React.createElement(
  "nav",
  { id: "main" },
  React.createElement(
    "a",
    { href: "/home", className: "active" },
    "Home"
  )
);</code></pre>
              <p>The outer element passes type <code>"nav"</code>, props <code>{ id: "main" }</code>, and the nested element call as its child parameter.</p>
            </div>
          </details>
        </div>

        <!-- Practice 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 6 &bull; FRAGMENTS WITH KEY PROPS</span>
          </div>
          <h4 class="problem-title">When is the empty fragment shorthand <code>&lt;&gt;...&lt;/&gt;</code> invalid in React, and what syntax must be used instead?</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p><strong>Scenario:</strong> When mapping a list of items where each iteration requires grouping multiple sibling elements without adding an extra wrapper DOM element (like a <code>&lt;div&gt;</code>), a <code>key</code> prop must be supplied to the container.</p>
              <p>The shorthand syntax <code>&lt;&gt;...&lt;/&gt;</code> does not accept attributes or props, so <code>&lt; key={item.id}&gt;</code> is a syntax error.</p>
              <p><strong>Required Syntax:</strong> Use the explicit <code>&lt;React.Fragment&gt;</code> component:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>{items.map(item => (
  <React.Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.description}</dd>
  </React.Fragment>
))}</code></pre>
            </div>
          </details>
        </div>
      </section>'''
        content = content[:exam_start] + new_exam_section + '\n\n      ' + content[ref_start:]

    # 4. Interactive Widget JavaScript Engine
    widget_script = '''
  <!-- Interactive JSX Compilation Studio Client Engine -->
  <script>
  (function() {
    // Tab switching
    var tabTranspile = document.getElementById('tab-btn-transpile');
    var tabRendering = document.getElementById('tab-btn-rendering');
    var panelTranspile = document.getElementById('panel-transpile');
    var panelRendering = document.getElementById('panel-rendering');

    if (tabTranspile && tabRendering && panelTranspile && panelRendering) {
      tabTranspile.addEventListener('click', function() {
        tabTranspile.style.borderColor = 'var(--brand)';
        tabTranspile.style.color = 'var(--brand)';
        tabTranspile.style.opacity = '1';
        tabTranspile.setAttribute('aria-selected', 'true');

        tabRendering.style.borderColor = 'var(--border)';
        tabRendering.style.color = 'var(--ink)';
        tabRendering.style.opacity = '0.7';
        tabRendering.setAttribute('aria-selected', 'false');

        panelTranspile.style.display = 'block';
        panelRendering.style.display = 'none';
      });

      tabRendering.addEventListener('click', function() {
        tabRendering.style.borderColor = 'var(--brand)';
        tabRendering.style.color = 'var(--brand)';
        tabRendering.style.opacity = '1';
        tabRendering.setAttribute('aria-selected', 'true');

        tabTranspile.style.borderColor = 'var(--border)';
        tabTranspile.style.color = 'var(--ink)';
        tabTranspile.style.opacity = '0.7';
        tabTranspile.setAttribute('aria-selected', 'false');

        panelRendering.style.display = 'block';
        panelTranspile.style.display = 'none';
      });
    }

    // Panel 1: Presets
    var presetData = {
      card: {
        jsx: '<div className="card">\\n  <h1>Hello {user.name}</h1>\\n  <p>Active: {user.active ? "Yes" : "No"}</p>\\n</div>',
        babel: 'React.createElement("div", { className: "card" },\\n  React.createElement("h1", null, "Hello " + user.name),\\n  React.createElement("p", null, "Active: " + (user.active ? "Yes" : "No"))\\n);',
        ast: JSON.stringify({
          type: "div",
          props: {
            className: "card",
            children: [
              { type: "h1", props: { children: "Hello Ananya" } },
              { type: "p", props: { children: "Active: Yes" } }
            ]
          }
        }, null, 2),
        domHtml: '<div style="font-weight: 700; font-size: 1.1rem; color: var(--ink);">Hello Ananya</div><div style="font-size: 0.85rem; color: var(--ink-muted); margin-top: 0.25rem;">Active: <span style="color: var(--brand); font-weight: 600;">Yes</span></div>'
      },
      cart: {
        jsx: '<div className="badge">\\n  <span>Cart</span>\\n  {count > 0 && <span className="counter">{count} items</span>}\\n</div>',
        babel: 'React.createElement("div", { className: "badge" },\\n  React.createElement("span", null, "Cart"),\\n  count > 0 && React.createElement("span", { className: "counter" }, count + " items")\\n);',
        ast: JSON.stringify({
          type: "div",
          props: {
            className: "badge",
            children: [
              { type: "span", props: { children: "Cart" } },
              { type: "span", props: { className: "counter", children: "3 items" } }
            ]
          }
        }, null, 2),
        domHtml: '<div style="display: flex; align-items: center; gap: 0.5rem;"><span style="font-weight: 700; color: var(--ink);">Cart</span><span style="background: var(--brand); color: #000; font-weight: 700; font-size: 0.75rem; padding: 0.15rem 0.5rem; border-radius: 999px;">3 items</span></div>'
      },
      list: {
        jsx: '<li key={course.id}>\\n  <strong>{course.title}</strong>\\n  <span> ({course.credits} Credits)</span>\\n</li>',
        babel: 'React.createElement("li", { key: course.id },\\n  React.createElement("strong", null, course.title),\\n  React.createElement("span", null, " (" + course.credits + " Credits)")\\n);',
        ast: JSON.stringify({
          type: "li",
          props: {
            key: "c1",
            children: [
              { type: "strong", props: { children: "ReactJS Fundamentals" } },
              { type: "span", props: { children: " (1 Credits)" } }
            ]
          }
        }, null, 2),
        domHtml: '<div style="font-size: 0.9rem; color: var(--ink);"><span style="background: rgba(46,195,107,0.15); color: var(--brand); padding: 0.1rem 0.35rem; border-radius: 4px; font-family: var(--font-mono); font-size: 0.75rem; margin-right: 0.3rem;">key="c1"</span> <strong>ReactJS Fundamentals</strong> <span>(1 Credits)</span></div>'
      }
    };

    function applyPreset(key) {
      var d = presetData[key];
      if (!d) return;
      var srcEl = document.getElementById('view-jsx-source');
      var babelEl = document.getElementById('view-babel-output');
      var astEl = document.getElementById('view-vdom-ast');
      var domEl = document.getElementById('view-dom-preview');

      if (srcEl) srcEl.textContent = d.jsx;
      if (babelEl) babelEl.textContent = d.babel;
      if (astEl) astEl.textContent = d.ast;
      if (domEl) domEl.innerHTML = d.domHtml;

      ['preset-card', 'preset-cart', 'preset-list'].forEach(function(id) {
        var btn = document.getElementById(id);
        if (btn) {
          if (id === 'preset-' + key) {
            btn.style.borderColor = 'var(--brand)';
            btn.style.color = 'var(--brand)';
          } else {
            btn.style.borderColor = 'var(--border)';
            btn.style.color = 'var(--ink)';
          }
        }
      });
    }

    var btnCard = document.getElementById('preset-card');
    var btnCart = document.getElementById('preset-cart');
    var btnList = document.getElementById('preset-list');
    if (btnCard) btnCard.addEventListener('click', function() { applyPreset('card'); });
    if (btnCart) btnCart.addEventListener('click', function() { applyPreset('cart'); });
    if (btnList) btnList.addEventListener('click', function() { applyPreset('list'); });

    // Panel 2: Interactive Sandbox Engine
    var inpName = document.getElementById('state-user-name');
    var chkLoggedIn = document.getElementById('state-is-logged-in');
    var rngUnread = document.getElementById('state-unread-count');
    var selFilter = document.getElementById('state-course-filter');
    var txtUnreadVal = document.getElementById('val-unread-count');
    var outGreeting = document.getElementById('res-greeting-text');
    var outCoursesCount = document.getElementById('res-courses-count');
    var outCourseUl = document.getElementById('res-course-ul');

    var courseCatalog = [
      { id: "c1", title: "ReactJS Fundamentals", credits: 1 },
      { id: "c2", title: "Machine Learning", credits: 4 },
      { id: "c3", title: "Computer Networks", credits: 4 }
    ];

    function updateSandbox() {
      var name = (inpName ? inpName.value : "Ananya").trim() || "Student";
      var isLoggedIn = chkLoggedIn ? chkLoggedIn.checked : true;
      var unread = rngUnread ? parseInt(rngUnread.value, 10) : 3;
      var filter = selFilter ? selFilter.value : "all";

      if (txtUnreadVal) txtUnreadVal.textContent = unread;

      // Greeting logic
      if (outGreeting) {
        if (!isLoggedIn) {
          outGreeting.textContent = "Please Sign In";
          outGreeting.style.color = "var(--ink-muted)";
        } else {
          var badgeText = unread > 0 ? " (" + unread + " new)" : "";
          outGreeting.textContent = "Welcome Back, " + name + "!" + badgeText;
          outGreeting.style.color = "var(--brand)";
        }
      }

      // Course list filter logic
      var filtered = courseCatalog.filter(function(c) {
        if (filter === "high") return c.credits >= 4;
        if (filter === "low") return c.credits < 4;
        return true;
      });

      if (outCoursesCount) {
        outCoursesCount.textContent = filtered.length + " items rendered";
      }

      if (outCourseUl) {
        outCourseUl.innerHTML = "";
        filtered.forEach(function(c) {
          var li = document.createElement("li");
          li.innerHTML = '<span style="background: rgba(46,195,107,0.15); color: var(--brand); padding: 0.1rem 0.35rem; border-radius: 4px; font-family: var(--font-mono); font-size: 0.75rem; margin-right: 0.3rem;">key="' + c.id + '"</span> <strong>' + c.title + '</strong> (' + c.credits + ' Credits)';
          outCourseUl.appendChild(li);
        });
      }
    }

    if (inpName) inpName.addEventListener('input', updateSandbox);
    if (chkLoggedIn) chkLoggedIn.addEventListener('change', updateSandbox);
    if (rngUnread) rngUnread.addEventListener('input', updateSandbox);
    if (selFilter) selFilter.addEventListener('change', updateSandbox);
  })();
  </script>
'''

    # Insert script right before closing </body>
    body_end = '</body>'
    bpos = content.rfind(body_end)
    if bpos != -1:
        content = content[:bpos] + widget_script + '\n' + content[bpos:]

    with open('notes/reactjs/unit1/unit-1-notes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully enriched notes/reactjs/unit1/unit-1-notes.html!")

if __name__ == '__main__':
    enrich_react_u1()
