"""
build_react_u2_enriched.py - Enriches notes/reactjs/unit2/unit-2-notes.html with:
1. Academic Verification Box citing Chris Minnick (Wiley 2022), Fullstack React, and ISAEC594 Syllabus
2. Interactive React Component & useState Hook Studio:
   - Tab 1: Interactive State & Immutability Sandbox (Counter with batching simulation, object/array immutable updates)
   - Tab 2: Props & Container Composition (props.children) Studio (live modal container, child slot switcher, code trace)
3. Standardized Exam Archive & 6 Verified Practice Problems matching audit/verify/reactjs/verify_react_u2.js
"""

import re

def enrich_react_u2():
    with open('notes/reactjs/unit2/unit-2-notes.html', 'r', encoding='utf-8') as f:
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
            <strong>Prescribed References:</strong> Chris Minnick, <em>Beginning ReactJS Foundations: Building User Interfaces with ReactJS - An Approachable Guide</em>, Wiley, 2022 (Chapters 4, 5 &amp; 6); Anthony Accomazzo et al., <em>Fullstack React: The Complete Guide to ReactJS and Friends</em>, 2017; Official React 18 Docs (<a href="https://react.dev/reference/react/useState" target="_blank" rel="noopener">react.dev/useState</a>) and Component Composition Guides.
          </p>
          <p style="margin: 0 0 0.5rem 0; color: var(--ink);">
            <strong>Curriculum &amp; Examination Scope:</strong> Course Code <strong>ISAEC594</strong> (Ability Enhancement Course: Front End Development using ReactJS, 1 Credit). Covers functional components, prop passing and destructuring, props vs. state, React Fragments, <code>props.children</code> container composition, <code>useState</code> hook syntax, functional updates, and shallow reference equality immutability.
          </p>
          <p style="margin: 0; color: var(--ink-muted); font-size: 0.88rem;">
            <strong>Code &amp; Test Verification:</strong> Functional prop destructuring (<code>"Rohan [STUDENT] - 95 pts"</code>), container composition, and <code>useState</code> state transitions (Counter to 5, profile age update to 21, array length to 3) verified via automated test suite (<code>audit/verify/reactjs/verify_react_u2.js</code>).
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
      <!-- Interactive React Component & useState Hook Studio -->
      <div id="react-state-studio" class="interactive-widget-card" style="margin: 2.5rem 0; padding: 1.5rem; background: var(--surface); border: 1.5px solid var(--border); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; color: var(--brand); font-weight: 700; letter-spacing: 0.05em;">Interactive Lab Explorer</div>
            <h3 style="margin: 0.2rem 0 0 0; font-family: var(--font-display); font-size: 1.25rem; color: var(--ink);">Component State &amp; Composition Studio</h3>
          </div>
          <div style="display: flex; gap: 0.5rem;" id="state-tab-controls" role="tablist">
            <button id="tab-btn-state" class="pill-action-btn" role="tab" aria-selected="true" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; border-color: var(--brand); color: var(--brand);">Tab 1: useState &amp; Immutability</button>
            <button id="tab-btn-children" class="pill-action-btn" role="tab" aria-selected="false" style="padding: 0.35rem 0.8rem; font-size: 0.8rem; opacity: 0.7;">Tab 2: Props &amp; Children Container</button>
          </div>
        </div>

        <!-- Panel 1: useState & Immutability Sandbox -->
        <div id="panel-state" role="tabpanel" style="display: block;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            Explore state updates, the critical difference between direct vs. functional state updates, and immutable object modification:
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 1.25rem;">
            <!-- Sub-panel A: Counter & Batching -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">A. Counter State (Batching &amp; Functional Updates)</div>
              
              <div style="display: flex; align-items: baseline; gap: 0.75rem; margin: 0.75rem 0;">
                <span style="font-size: 0.85rem; color: var(--ink-muted);">Current Count:</span>
                <span id="counter-val" style="font-family: var(--font-display); font-size: 2.2rem; font-weight: 800; color: var(--brand);">0</span>
              </div>

              <!-- Controls -->
              <div style="display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 1rem;">
                <button id="btn-count-inc" class="pill-action-btn" style="padding: 0.3rem 0.65rem; font-size: 0.8rem;">+1 Inc</button>
                <button id="btn-count-dec" class="pill-action-btn" style="padding: 0.3rem 0.65rem; font-size: 0.8rem;">-1 Dec</button>
                <button id="btn-count-5" class="pill-action-btn" style="padding: 0.3rem 0.65rem; font-size: 0.8rem;">Set 5</button>
                <button id="btn-count-reset" class="pill-action-btn" style="padding: 0.3rem 0.65rem; font-size: 0.8rem;">Reset</button>
              </div>

              <!-- Rapid Triple Click Batching Test -->
              <div style="padding: 0.75rem; background: var(--surface); border-radius: 6px; border: 1px dashed var(--border);">
                <div style="font-size: 0.8rem; font-weight: 600; color: var(--ink); margin-bottom: 0.4rem;">Simulate 3 Rapid Increments in 1 Handler:</div>
                <div style="display: flex; gap: 0.5rem;">
                  <button id="btn-batch-direct" class="pill-action-btn" style="font-size: 0.75rem; padding: 0.25rem 0.5rem;" title="Calls setCount(count + 1) three times">3x Direct Call</button>
                  <button id="btn-batch-fn" class="pill-action-btn" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; border-color: var(--brand); color: var(--brand);" title="Calls setCount(prev => prev + 1) three times">3x Functional Call</button>
                </div>
                <div id="batch-explanation" style="font-size: 0.75rem; color: var(--ink-muted); margin-top: 0.4rem; font-family: var(--font-mono);">
                  Ready: Click either button to see batching behavior.
                </div>
              </div>
            </div>

            <!-- Sub-panel B: Object State Immutability -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">B. Immutable Object State (Spread Operator)</div>

              <div style="margin: 0.75rem 0;">
                <pre style="margin: 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); line-height: 1.45;"><code id="view-user-json">{
  "name": "Priya",
  "age": 20,
  "enrolled": true
}</code></pre>
              </div>

              <!-- Controls -->
              <div style="display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 0.75rem;">
                <button id="btn-user-bday" class="pill-action-btn" style="padding: 0.3rem 0.65rem; font-size: 0.8rem;">Birthday (+1 Age)</button>
                <button id="btn-user-enroll" class="pill-action-btn" style="padding: 0.3rem 0.65rem; font-size: 0.8rem;">Toggle Enrolled</button>
                <button id="btn-user-reset" class="pill-action-btn" style="padding: 0.3rem 0.65rem; font-size: 0.8rem;">Reset User</button>
              </div>

              <div id="ref-check-box" style="padding: 0.5rem 0.75rem; background: var(--surface); border-radius: 6px; border: 1px solid var(--border); font-size: 0.78rem; font-family: var(--font-mono); color: var(--brand);">
                Shallow Ref Check: prev !== next (New object created &rarr; Re-render triggered)
              </div>
            </div>
          </div>
        </div>

        <!-- Panel 2: Props & Children Container Pattern -->
        <div id="panel-children" role="tabpanel" style="display: none;">
          <p style="font-size: 0.9rem; color: var(--ink-muted); margin-top: 0;">
            The <code>props.children</code> pattern allows container components to wrap arbitrary JSX elements without knowing their specific structure ahead of time:
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
            <!-- Controls & Source -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">Parent Configuration</div>
              
              <div style="margin-bottom: 0.8rem;">
                <label for="input-modal-title" style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.3rem;">Container Title Prop:</label>
                <input type="text" id="input-modal-title" value="Confirmation" style="width: 100%; padding: 0.45rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--ink); font-family: var(--font-mono); font-size: 0.85rem;">
              </div>

              <div style="margin-bottom: 0.8rem;">
                <label style="display: block; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink); margin-bottom: 0.3rem;">Injected Child Content:</label>
                <div style="display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.85rem; color: var(--ink);">
                  <label style="cursor: pointer; display: flex; align-items: center; gap: 0.4rem;">
                    <input type="radio" name="modal-child-radio" value="warning" checked style="accent-color: var(--brand);">
                    <span>Delete Warning (2 paragraphs)</span>
                  </label>
                  <label style="cursor: pointer; display: flex; align-items: center; gap: 0.4rem;">
                    <input type="radio" name="modal-child-radio" value="badge" style="accent-color: var(--brand);">
                    <span>UserBadge Component (Rohan, 95 pts)</span>
                  </label>
                  <label style="cursor: pointer; display: flex; align-items: center; gap: 0.4rem;">
                    <input type="radio" name="modal-child-radio" value="reg" style="accent-color: var(--brand);">
                    <span>Registration Notice</span>
                  </label>
                </div>
              </div>

              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted); text-transform: uppercase; margin-bottom: 0.3rem;">Parent JSX Invocation:</div>
              <pre style="margin: 0; padding: 0.5rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.75rem; color: var(--ink); line-height: 1.4;"><code id="view-parent-jsx">&lt;ModalCard title="Confirmation"&gt;
  &lt;p&gt;Are you sure you want to delete this?&lt;/p&gt;
  &lt;p&gt;This action is irreversible.&lt;/p&gt;
&lt;/ModalCard&gt;</code></pre>
            </div>

            <!-- Rendered Output -->
            <div style="padding: 1.2rem; background: var(--surface-alt); border-radius: 8px; border: 1px solid var(--border);">
              <div style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem;">Rendered &lt;ModalCard&gt; Component</div>
              
              <div style="background: var(--surface); border: 1.5px solid var(--border); border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-top: 0.5rem;">
                <div style="padding: 0.75rem 1rem; background: var(--surface-alt); border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center;">
                  <strong id="modal-rendered-title" style="font-family: var(--font-display); font-size: 1rem; color: var(--ink);">Confirmation</strong>
                  <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--brand); font-weight: 700;">props.title</span>
                </div>
                
                <div id="modal-rendered-body" style="padding: 1rem; color: var(--ink); font-size: 0.88rem; line-height: 1.5;">
                  <p style="margin: 0 0 0.5rem 0;">Are you sure you want to delete this?</p>
                  <p style="margin: 0; color: #dc2626; font-size: 0.82rem; font-weight: 600;">This action is irreversible.</p>
                </div>

                <div style="padding: 0.6rem 1rem; background: var(--surface-alt); border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center;">
                  <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--ink-muted);">slot: props.children</span>
                  <div style="display: flex; gap: 0.4rem;">
                    <button class="pill-action-btn" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">Cancel</button>
                    <button class="pill-action-btn" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; border-color: var(--brand); color: var(--brand);">Proceed</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
'''

    # Insert interactive widget at the end of Section 8 (#sec-code-demos)
    sec_8_pos = content.find('id="sec-code-demos"')
    if sec_8_pos != -1:
        sec_8_end = content.find('</section>', sec_8_pos)
        if sec_8_end != -1:
            content = content[:sec_8_end] + '\n' + interactive_widget + '\n' + content[sec_8_end:]

    # 3. Standardize and enrich Section 10 with authentic questions and verified practice problems
    exam_start = content.find('<section id="exam-questions"')
    ref_start = content.find('<section id="sec-references"')

    if exam_start != -1 and ref_start != -1:
        new_exam_section = '''<section id="exam-questions" class="content-section exam-archive">
        <h2 class="section-title">10. Important Exam Questions &amp; Practice</h2>
        <p class="section-lead">The following conceptual questions and verified code tracing problems cover essential university examination patterns for <strong>ISAEC594 (Front End Development using ReactJS)</strong>:</p>

        <h3 class="subsection-title">2-Mark Conceptual Questions</h3>

        <!-- Q1 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">1. Differentiate between Props and State in React.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ul>
              <li><strong>Props (Properties):</strong> External, read-only configuration passed from a parent component downward to a child. They are immutable from the child component's perspective.</li>
              <li><strong>State:</strong> Internal, private data managed locally within a component via the <code>useState</code> hook. When state transitions occur via its setter function, React schedules a re-render of the component and its children.</li>
            </ul>
          </div>
        </details>

        <!-- Q2 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">2. What are React Fragments and why are they used?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>React Fragments (<code>&lt;&gt;...&lt;/&gt;</code> or <code>&lt;React.Fragment&gt;...&lt;/React.Fragment&gt;</code>) allow grouping a list of children elements without adding an extra wrapper node (such as an unwanted <code>&lt;div&gt;</code>) to the browser's real DOM tree.</p>
            <p><strong>Use Cases:</strong> Preserves semantic HTML layouts such as tables (e.g. returning multiple <code>&lt;td&gt;</code> elements inside a table row) and CSS Flexbox/Grid parent-child alignments.</p>
          </div>
        </details>

        <!-- Q3 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">3. Explain the purpose of `props.children` with a brief example.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p><code>props.children</code> is a special prop available in every React component that automatically captures any JSX elements or text passed between the component's opening and closing tags.</p>
            <p><strong>Example:</strong> In <code>&lt;Card&gt;&lt;h2&gt;Title&lt;/h2&gt;&lt;/Card&gt;</code>, the <code>Card</code> component receives the <code>&lt;h2&gt;</code> node inside <code>props.children</code>, enabling flexible container composition patterns.</p>
          </div>
        </details>

        <!-- Q4 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">4. State the two fundamental Rules of Hooks in React.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <ol>
              <li><strong>Only Call Hooks at the Top Level:</strong> Do not call hooks inside loops, conditional statements (<code>if</code>), or nested functions. This ensures hooks are invoked in the exact same sequential order on every render, allowing React to correctly preserve state associations.</li>
              <li><strong>Only Call Hooks from React Functions:</strong> Only invoke hooks from React functional components or custom hooks, never from regular JavaScript utility functions or class components.</li>
            </ol>
          </div>
        </details>

        <!-- Q5 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">2 MARKS</span>
            <span class="q-title">5. Why should functional state updates `setState(prev => prev + 1)` be used instead of direct updates `setState(state + 1)`?</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Answer:</strong></p>
            <p>React batches multiple state updates during event handlers and asynchronous operations for performance. Direct updates read the current render's stale closure snapshot of state. If multiple direct updates are executed in succession, subsequent calls overwrite previous ones. Passing an updater callback function <code>prev =&gt; prev + 1</code> guarantees React passes the most recent pending state to the calculation.</p>
          </div>
        </details>

        <h3 class="subsection-title">5-Mark &amp; 10-Mark Model Questions</h3>

        <!-- Q6 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">10 MARKS</span>
            <span class="q-title">6. Explain the `useState` hook in React with syntax, mechanics, and a complete working counter implementation.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Comprehensive Answer:</strong></p>
            <ol>
              <li>
                <strong>Hook Definition &amp; Signature:</strong> <code>const [state, setState] = useState(initialValue);</code><br>
                <code>useState</code> is a built-in React Hook enabling functional components to maintain private, local reactive state. It takes an optional initial value and returns an array of two items using ES6 array destructuring:
                <ul>
                  <li><code>state</code>: The current state variable.</li>
                  <li><code>setState</code>: The dispatcher function used to update the state and trigger a re-render.</li>
                </ul>
              </li>
              <li>
                <strong>Update Mechanics &amp; Batching:</strong> When <code>setState</code> is called, React does not mutate the variable immediately in place. Instead, it enqueues a re-render request with the new value. React compares the new value with the old value using <code>Object.is</code> equality; if unchanged, React bails out of re-rendering.
              </li>
              <li>
                <strong>Complete Working Implementation:</strong>
                <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>import React, { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    &lt;div className="counter-card"&gt;
      &lt;h2&gt;Current Count: {count}&lt;/h2&gt;
      &lt;button onClick={() =&gt; setCount(prev =&gt; prev + 1)}&gt;Increment&lt;/button&gt;
      &lt;button onClick={() =&gt; setCount(prev =&gt; Math.max(0, prev - 1))}&gt;Decrement&lt;/button&gt;
      &lt;button onClick={() =&gt; setCount(0)}&gt;Reset&lt;/button&gt;
    &lt;/div&gt;
  );
}</code></pre>
              </li>
            </ol>
          </div>
        </details>

        <!-- Q7 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">10 MARKS</span>
            <span class="q-title">7. Why is state immutability crucial in React? Explain how objects and arrays are immutably updated with clear code examples.</span>
          </summary>
          <div class="qa-answer">
            <p><strong>Crucial Nature of State Immutability:</strong></p>
            <p>React relies on <em>shallow reference comparison</em> (<code>Object.is</code>) to detect whether state has updated. If an object or array is mutated directly in-place (e.g. <code>user.age = 21</code> or <code>arr.push(item)</code>), the memory pointer/reference of the object remains identical. React perceives no change and will skip re-rendering the component, leading to silent UI synchronization failures.</p>
            <p><strong>Immutable Modification Patterns:</strong></p>
            <ul>
              <li>
                <strong>1. Updating Objects:</strong> Always copy the existing object using the ES6 object spread operator (<code>...</code>) and override specific fields:
                <pre style="margin: 0.4rem 0; padding: 0.5rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.78rem; color: var(--ink);"><code>// Correct: Creates a brand new object reference
setUser(prevUser =&gt; ({
  ...prevUser,
  age: prevUser.age + 1
}));</code></pre>
              </li>
              <li>
                <strong>2. Adding Items to Arrays:</strong> Use array spread syntax instead of <code>push()</code>:
                <pre style="margin: 0.4rem 0; padding: 0.5rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.78rem; color: var(--ink);"><code>setItems(prev =&gt; [...prev, newItem]);</code></pre>
              </li>
              <li>
                <strong>3. Deleting Items from Arrays:</strong> Use <code>Array.prototype.filter()</code> which returns a new filtered array:
                <pre style="margin: 0.4rem 0; padding: 0.5rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.78rem; color: var(--ink);"><code>setItems(prev =&gt; prev.filter(item =&gt; item.id !== idToDelete));</code></pre>
              </li>
              <li>
                <strong>4. Updating Items in Arrays:</strong> Use <code>Array.prototype.map()</code> to produce a transformed array copy:
                <pre style="margin: 0.4rem 0; padding: 0.5rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.78rem; color: var(--ink);"><code>setItems(prev =&gt; prev.map(item =&gt; 
  item.id === targetId ? { ...item, completed: true } : item
));</code></pre>
              </li>
            </ul>
          </div>
        </details>

        <!-- Q8 -->
        <details class="exam-card">
          <summary class="exam-summary">
            <span class="q-badge">5 MARKS</span>
            <span class="q-title">8. Contrast Functional Components with Class Components in terms of syntax, state management, and lifecycle.</span>
          </summary>
          <div class="qa-answer">
            <div class="table-container">
              <table class="notes-table">
                <thead>
                  <tr>
                    <th>Dimension</th>
                    <th>Functional Components (Modern)</th>
                    <th>Class Components (Legacy)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Declaration</strong></td>
                    <td>Plain JavaScript function returning JSX</td>
                    <td>ES6 class extending <code>React.Component</code> with a <code>render()</code> method</td>
                  </tr>
                  <tr>
                    <td><strong>`this` Keyword</strong></td>
                    <td>No <code>this</code> binding required; lexical scoping throughout</td>
                    <td>Requires explicit method binding in constructor or arrow functions</td>
                  </tr>
                  <tr>
                    <td><strong>State Management</strong></td>
                    <td><code>useState</code> and other Hooks</td>
                    <td><code>this.state = {...}</code> in constructor; <code>this.setState()</code></td>
                  </tr>
                  <tr>
                    <td><strong>Lifecycle Logic</strong></td>
                    <td>Unified <code>useEffect</code> hook</td>
                    <td>Partitioned methods: <code>componentDidMount</code>, <code>componentDidUpdate</code>, <code>componentWillUnmount</code></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </details>

        <h3 class="subsection-title">Verified Code Tracing &amp; Practice Problems</h3>

        <!-- Practice 1 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 1 &bull; PROPS DESTRUCTURING &amp; DEFAULTS</span>
          </div>
          <h4 class="problem-title">Trace the output of <code>UserBadge({ name: "Rohan", score: 95 })</code> when defined as: <code>function UserBadge({ name, role = "Student", score = 0 })</code>.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Consider the functional component with default parameter values:</p>
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>function UserBadge({ name, role = "Student", score = 0 }) {
  return {
    badgeText: `${name} [${role.toUpperCase()}] - ${score} pts`,
    isTopScorer: score >= 90
  };
}</code></pre>
              <ul>
                <li><code>name</code> is provided as <code>"Rohan"</code>.</li>
                <li><code>role</code> is omitted, so default value <code>"Student"</code> applies &rarr; <code>role.toUpperCase() = "STUDENT"</code>.</li>
                <li><code>score</code> is <code>95</code> &rarr; <code>score &gt;= 90</code> evaluates to <code>true</code>.</li>
                <li><strong>Result:</strong> <code>badgeText: "Rohan [STUDENT] - 95 pts"</code>, <code>isTopScorer: true</code>.</li>
              </ul>
              <p><em>Verification:</em> Verified by automated test in <code>audit/verify/reactjs/verify_react_u2.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 2 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 2 &bull; PROPS.CHILDREN CONTAINER TRACE</span>
          </div>
          <h4 class="problem-title">Trace the output structure of <code>ModalCard</code> when passed title "Confirmation" and an array of 2 string children.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <p>Function definition: <code>function ModalCard({ title, children }) { return { header: title, body: children }; }</code></p>
              <ul>
                <li><code>header = "Confirmation"</code></li>
                <li><code>body = ["Are you sure you want to delete this?", "This action is irreversible."]</code></li>
                <li><code>body.length = 2</code></li>
              </ul>
              <p><strong>Conclusion:</strong> The container successfully encapsulates arbitrary child items inside <code>props.children</code> without mutating them.</p>
              <p><em>Verification:</em> Verified in <code>audit/verify/reactjs/verify_react_u2.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 3 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 3 &bull; SEQUENTIAL USESTATE CALLS &amp; UPDATERS</span>
          </div>
          <h4 class="problem-title">Trace the state transitions: initial value 0 &rarr; <code>setCount(c =&gt; c + 1)</code> &rarr; <code>setCount(c =&gt; c + 1)</code> &rarr; <code>setCount(5)</code>.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ol>
                <li>Initial state: <code>count = 0</code>.</li>
                <li>First functional update: <code>c =&gt; c + 1</code> transforms <code>0 &rarr; 1</code>.</li>
                <li>Second functional update: <code>c =&gt; c + 1</code> transforms <code>1 &rarr; 2</code>.</li>
                <li>Direct assignment: <code>setCount(5)</code> replaces state with literal <code>5</code>.</li>
                <li><strong>Final state:</strong> <code>5</code>.</li>
              </ol>
              <p><em>Verification:</em> Verified in <code>audit/verify/reactjs/verify_react_u2.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 4 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 4 &bull; OBJECT STATE IMMUTABILITY TRACE</span>
          </div>
          <h4 class="problem-title">Given state <code>user = { name: "Priya", age: 20 }</code>, write the immutable update that increments age to 21 while preserving name.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>setUser(prev => ({
  ...prev,
  age: 21
}));</code></pre>
              <ul>
                <li>The spread operator <code>...prev</code> copies all existing properties (<code>name: "Priya"</code>).</li>
                <li><code>age: 21</code> overrides the old age property.</li>
                <li>Outer parentheses <code>({ ... })</code> ensure JavaScript parses the curly braces as an object literal return rather than a function block body.</li>
              </ul>
              <p><em>Verification:</em> Verified in <code>audit/verify/reactjs/verify_react_u2.js</code> (Confirms <code>user.age === 21</code> and <code>user.name === "Priya"</code>).</p>
            </div>
          </details>
        </div>

        <!-- Practice 5 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 5 &bull; ARRAY STATE IMMUTABLE APPEND</span>
          </div>
          <h4 class="problem-title">Given state <code>todos = ["Read syllabus", "Write pilot"]</code>, show how to append "Pass exam" without mutating the original array.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <pre style="margin: 0.5rem 0; padding: 0.6rem; background: var(--surface); border: 1px solid var(--border); border-radius: 6px; font-family: var(--font-mono); font-size: 0.8rem; color: var(--ink);"><code>// Correct: Spread syntax creates a new array reference
setTodos(prev => [...prev, "Pass exam"]);</code></pre>
              <p>Resulting state: <code>["Read syllabus", "Write pilot", "Pass exam"]</code> (length: 3).</p>
              <p><em>Anti-pattern to avoid:</em> <code>todos.push("Pass exam"); setTodos(todos);</code> (Mutates in place, fails React shallow comparison!).</p>
              <p><em>Verification:</em> Verified in <code>audit/verify/reactjs/verify_react_u2.js</code>.</p>
            </div>
          </details>
        </div>

        <!-- Practice 6 -->
        <div class="problem-card">
          <div class="problem-header">
            <span class="problem-tag">PRACTICE 6 &bull; IMMUTABLE DELETION &amp; TOGGLE IN ARRAYS</span>
          </div>
          <h4 class="problem-title">Given task array <code>tasks = [{id: 1, done: false}, {id: 2, done: false}]</code>, write expressions to (a) delete task 1 and (b) toggle task 2 to done.</h4>
          <details>
            <summary class="reveal-btn">Show Step-by-Step Solution</summary>
            <div class="qa-answer">
              <ul>
                <li><strong>(a) Immutable Deletion:</strong>
                  <pre style="margin: 0.3rem 0; padding: 0.4rem; background: var(--surface); border: 1px solid var(--border); border-radius: 4px; font-family: var(--font-mono); font-size: 0.78rem;"><code>setTasks(prev => prev.filter(t => t.id !== 1));</code></pre>
                </li>
                <li><strong>(b) Immutable Field Toggle:</strong>
                  <pre style="margin: 0.3rem 0; padding: 0.4rem; background: var(--surface); border: 1px solid var(--border); border-radius: 4px; font-family: var(--font-mono); font-size: 0.78rem;"><code>setTasks(prev => prev.map(t => 
  t.id === 2 ? { ...t, done: !t.done } : t
));</code></pre>
                </li>
              </ul>
            </div>
          </details>
        </div>
      </section>'''
        content = content[:exam_start] + new_exam_section + '\n\n      ' + content[ref_start:]

    # 4. Interactive Widget JavaScript Engine
    widget_script = '''
  <!-- Interactive React Component & useState Hook Studio Engine -->
  <script>
  (function() {
    // Tab switching
    var tabState = document.getElementById('tab-btn-state');
    var tabChildren = document.getElementById('tab-btn-children');
    var panelState = document.getElementById('panel-state');
    var panelChildren = document.getElementById('panel-children');

    if (tabState && tabChildren && panelState && panelChildren) {
      tabState.addEventListener('click', function() {
        tabState.style.borderColor = 'var(--brand)';
        tabState.style.color = 'var(--brand)';
        tabState.style.opacity = '1';
        tabState.setAttribute('aria-selected', 'true');

        tabChildren.style.borderColor = 'var(--border)';
        tabChildren.style.color = 'var(--ink)';
        tabChildren.style.opacity = '0.7';
        tabChildren.setAttribute('aria-selected', 'false');

        panelState.style.display = 'block';
        panelChildren.style.display = 'none';
      });

      tabChildren.addEventListener('click', function() {
        tabChildren.style.borderColor = 'var(--brand)';
        tabChildren.style.color = 'var(--brand)';
        tabChildren.style.opacity = '1';
        tabChildren.setAttribute('aria-selected', 'true');

        tabState.style.borderColor = 'var(--border)';
        tabState.style.color = 'var(--ink)';
        tabState.style.opacity = '0.7';
        tabState.setAttribute('aria-selected', 'false');

        panelChildren.style.display = 'block';
        panelState.style.display = 'none';
      });
    }

    // Panel 1A: Counter Engine
    var count = 0;
    var outCounter = document.getElementById('counter-val');
    var outBatchExpl = document.getElementById('batch-explanation');

    function renderCount() {
      if (outCounter) outCounter.textContent = count;
    }

    var btnInc = document.getElementById('btn-count-inc');
    var btnDec = document.getElementById('btn-count-dec');
    var btnSet5 = document.getElementById('btn-count-5');
    var btnReset = document.getElementById('btn-count-reset');

    if (btnInc) btnInc.addEventListener('click', function() { count++; renderCount(); });
    if (btnDec) btnDec.addEventListener('click', function() { count = Math.max(0, count - 1); renderCount(); });
    if (btnSet5) btnSet5.addEventListener('click', function() { count = 5; renderCount(); });
    if (btnReset) btnReset.addEventListener('click', function() { count = 0; renderCount(); });

    // Rapid batching test
    var btnBatchDirect = document.getElementById('btn-batch-direct');
    var btnBatchFn = document.getElementById('btn-batch-fn');

    if (btnBatchDirect) {
      btnBatchDirect.addEventListener('click', function() {
        // Direct simulation: read snapshot count
        var snap = count;
        // 3 calls to setCount(snap + 1)
        count = snap + 1;
        renderCount();
        if (outBatchExpl) {
          outBatchExpl.textContent = 'Direct result: ' + count + ' (+1 only! All 3 calls used stale snapshot: ' + snap + ' + 1)';
          outBatchExpl.style.color = '#ef4444';
        }
      });
    }

    if (btnBatchFn) {
      btnBatchFn.addEventListener('click', function() {
        // Functional simulation: queued updater functions
        var old = count;
        count = count + 1;
        count = count + 1;
        count = count + 1;
        renderCount();
        if (outBatchExpl) {
          outBatchExpl.textContent = 'Functional result: ' + count + ' (+3 correctly! Each updater received pending state: ' + old + ' -> ' + (old+1) + ' -> ' + (old+2) + ' -> ' + (old+3) + ')';
          outBatchExpl.style.color = 'var(--brand)';
        }
      });
    }

    // Panel 1B: Immutable Object State Engine
    var userProfile = { name: "Priya", age: 20, enrolled: true };
    var outUserJson = document.getElementById('view-user-json');
    var outRefCheck = document.getElementById('ref-check-box');

    function renderUser(isImmutableUpdate) {
      if (outUserJson) {
        outUserJson.textContent = JSON.stringify(userProfile, null, 2);
      }
      if (outRefCheck) {
        if (isImmutableUpdate) {
          outRefCheck.textContent = 'Shallow Ref Check: prev !== next (New object created -> Re-render triggered)';
          outRefCheck.style.color = 'var(--brand)';
        } else {
          outRefCheck.textContent = 'Initial profile loaded';
          outRefCheck.style.color = 'var(--ink-muted)';
        }
      }
    }

    var btnBday = document.getElementById('btn-user-bday');
    var btnEnroll = document.getElementById('btn-user-enroll');
    var btnUserReset = document.getElementById('btn-user-reset');

    if (btnBday) {
      btnBday.addEventListener('click', function() {
        userProfile = Object.assign({}, userProfile, { age: userProfile.age + 1 });
        renderUser(true);
      });
    }

    if (btnEnroll) {
      btnEnroll.addEventListener('click', function() {
        userProfile = Object.assign({}, userProfile, { enrolled: !userProfile.enrolled });
        renderUser(true);
      });
    }

    if (btnUserReset) {
      btnUserReset.addEventListener('click', function() {
        userProfile = { name: "Priya", age: 20, enrolled: true };
        renderUser(false);
      });
    }

    // Panel 2: Props & Children Engine
    var inpTitle = document.getElementById('input-modal-title');
    var outModalTitle = document.getElementById('modal-rendered-title');
    var outModalBody = document.getElementById('modal-rendered-body');
    var outParentJsx = document.getElementById('view-parent-jsx');
    var radios = document.querySelectorAll('input[name="modal-child-radio"]');

    var childTemplates = {
      warning: {
        bodyHtml: '<p style="margin: 0 0 0.5rem 0;">Are you sure you want to delete this?</p><p style="margin: 0; color: #dc2626; font-size: 0.82rem; font-weight: 600;">This action is irreversible.</p>',
        jsxContent: '  <p>Are you sure you want to delete this?</p>\\n  <p>This action is irreversible.</p>'
      },
      badge: {
        bodyHtml: '<div style="display: flex; align-items: center; justify-content: space-between; padding: 0.5rem; background: var(--surface-alt); border-radius: 6px;"><span style="font-weight: 700; color: var(--ink);">Rohan [STUDENT]</span><span style="background: var(--brand); color: #000; font-weight: 700; font-size: 0.75rem; padding: 0.15rem 0.5rem; border-radius: 999px;">95 pts (Top Scorer)</span></div>',
        jsxContent: '  <UserBadge name="Rohan" role="Student" score={95} />'
      },
      reg: {
        bodyHtml: '<p style="margin: 0 0 0.4rem 0;">Please confirm your semester elective registration before the deadline.</p><div style="font-size: 0.78rem; color: var(--brand); font-weight: 600;">Course Code: ISAEC594 (Front End Development using ReactJS)</div>',
        jsxContent: '  <p>Please confirm your semester elective registration...</p>\\n  <Badge code="ISAEC594" />'
      }
    };

    function updateModal() {
      var title = (inpTitle ? inpTitle.value : "Confirmation").trim() || "Notice";
      if (outModalTitle) outModalTitle.textContent = title;

      var selected = "warning";
      radios.forEach(function(r) {
        if (r.checked) selected = r.value;
      });

      var template = childTemplates[selected] || childTemplates.warning;
      if (outModalBody) outModalBody.innerHTML = template.bodyHtml;

      if (outParentJsx) {
        outParentJsx.textContent = '<ModalCard title="' + title + '">\\n' + template.jsxContent + '\\n</ModalCard>';
      }
    }

    if (inpTitle) inpTitle.addEventListener('input', updateModal);
    radios.forEach(function(r) {
      r.addEventListener('change', updateModal);
    });
  })();
  </script>
'''

    # Insert script right before closing </body>
    body_end = '</body>'
    bpos = content.rfind(body_end)
    if bpos != -1:
        content = content[:bpos] + widget_script + '\n' + content[bpos:]

    with open('notes/reactjs/unit2/unit-2-notes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully enriched notes/reactjs/unit2/unit-2-notes.html!")

if __name__ == '__main__':
    enrich_react_u2()
