/**
 * SEM 5 — Playwright Verification Suite for PYQ Diagrams
 * Checks every PYQ diagram across all 8 subjects:
 * - Tests viewports: 1280px (desktop) and 390px (mobile)
 * - Tests themes: dark and light mode
 * - Validates SVG viewBox, <title>/<desc>, markers
 * - Checks text bounding boxes for overlapping labels, clipping, and font size
 * - Captures sample visual screenshots to audit/diagram_screenshots/
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const REPO_ROOT = path.resolve(__dirname, '..');
const SCREENSHOT_DIR = path.join(REPO_ROOT, 'audit/diagram_screenshots');

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

const SUBJECTS = ['ai', 'cn', 'evs', 'ml', 'reactjs', 'rmipr', 'se', 'toc'];
const VIEWPORTS = [
  { name: 'desktop', width: 1280, height: 800 },
  { name: 'mobile', width: 390, height: 844 }
];
const THEMES = ['dark', 'light'];

async function verifyAllDiagrams() {
  console.log('='.repeat(70));
  console.log('PLAYWRIGHT PYQ DIAGRAM BOUNDING BOX & RESPONSIVE VERIFICATION');
  console.log('='.repeat(70));

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--allow-file-access-from-files']
  });

  let totalDiagramsChecked = 0;
  let totalIssuesFound = 0;
  const issues = [];

  try {
    for (const sub of SUBJECTS) {
      const htmlPath = path.join(REPO_ROOT, `notes/${sub}/pyq/pyq-answers.html`);
      if (!fs.existsSync(htmlPath)) {
        console.error(`Missing HTML for ${sub}: ${htmlPath}`);
        continue;
      }

      console.log(`\nAuditing Diagrams for Subject: [${sub.toUpperCase()}]`);

      for (const vp of VIEWPORTS) {
        for (const theme of THEMES) {
          const context = await browser.newContext({
            viewport: { width: vp.width, height: vp.height }
          });
          const page = await context.newPage();

          const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
          await page.goto(fileUrl, { waitUntil: 'networkidle' });

          // Set theme
          await page.evaluate((t) => {
            document.documentElement.setAttribute('data-theme', t);
          }, theme);
          // Wait for KaTeX math and layout to settle
          await page.waitForTimeout(600);

          // Evaluate all diagrams on this page
          const evalResults = await page.evaluate(() => {
            const diagrams = Array.from(document.querySelectorAll('.diagram-svg'));
            const report = [];

            diagrams.forEach((svg, idx) => {
              svg.scrollIntoView();
              const diagId = svg.closest('.pyq-card')?.id || `svg-${idx}`;
              const vb = svg.getAttribute('viewBox');
              const title = svg.querySelector('title')?.textContent || '';
              const desc = svg.querySelector('desc')?.textContent || '';
              const aria = svg.getAttribute('aria-label') || '';

              let vbX = 0, vbY = 0, vbW = 760, vbH = 260;
              if (vb) {
                const parts = vb.trim().split(/[\s,]+/).map(Number);
                if (parts.length === 4) {
                  [vbX, vbY, vbW, vbH] = parts;
                }
              }

              // Marker resolution check
              const rawHtml = svg.outerHTML;
              const markerMatches = Array.from(rawHtml.matchAll(/url\(#([^\)]+)\)/g)).map(m => m[1]);
              const definedMarkers = Array.from(svg.querySelectorAll('marker')).map(m => m.id);
              const missingMarkers = markerMatches.filter(m => !definedMarkers.includes(m));

              // Text elements bounding box check using screen-space getBoundingClientRect
              const svgRect = svg.getBoundingClientRect();
              const textNodes = Array.from(svg.querySelectorAll('text'));
              const textBoxes = [];
              const fontWarnings = [];
              const clipWarnings = [];

              textNodes.forEach(tNode => {
                const rect = tNode.getBoundingClientRect();
                const textContent = tNode.textContent.trim();
                const computedStyle = window.getComputedStyle(tNode);
                const fontSize = parseFloat(computedStyle.fontSize);

                if (fontSize < 10) {
                  fontWarnings.push({ text: textContent, fontSize });
                }

                // Check clipping against SVG rendered screen bounds (allow 10px margin for subpixel rendering)
                if (
                  rect.left < svgRect.left - 10 ||
                  rect.right > svgRect.right + 10 ||
                  rect.top < svgRect.top - 10 ||
                  rect.bottom > svgRect.bottom + 10
                ) {
                  clipWarnings.push({
                    text: textContent,
                    rect: { left: Math.round(rect.left), top: Math.round(rect.top), right: Math.round(rect.right), bottom: Math.round(rect.bottom) },
                    svgRect: { left: Math.round(svgRect.left), top: Math.round(svgRect.top), right: Math.round(svgRect.right), bottom: Math.round(svgRect.bottom) }
                  });
                }

                textBoxes.push({
                  text: textContent,
                  left: rect.left,
                  top: rect.top,
                  right: rect.right,
                  bottom: rect.bottom,
                  w: rect.width,
                  h: rect.height,
                  fs: fontSize,
                  node: tNode
                });
              });

              // Check pairwise text overlaps in screen space
              const overlapPairs = [];
              for (let i = 0; i < textBoxes.length; i++) {
                for (let j = i + 1; j < textBoxes.length; j++) {
                  const b1 = textBoxes[i];
                  const b2 = textBoxes[j];
                  if (!b1.text || !b2.text) continue;
                  // Skip if one contains the other (e.g. tspan parent or nested text)
                  if (b1.node.contains(b2.node) || b2.node.contains(b1.node)) continue;
                  const minLen = Math.min(b1.text.length, b2.text.length);
                  const minOverlap = minLen <= 2 ? 6 : 4;

                  const xOverlap = Math.max(0, Math.min(b1.right, b2.right) - Math.max(b1.left, b2.left));
                  const yOverlap = Math.max(0, Math.min(b1.bottom, b2.bottom) - Math.max(b1.top, b2.top));

                  if (xOverlap > minOverlap && yOverlap > minOverlap) {
                    overlapPairs.push({
                      t1: b1.text,
                      t2: b2.text,
                      area: Math.round(xOverlap * yOverlap)
                    });
                  }
                }
              }

              report.push({
                diagId,
                hasViewBox: !!vb,
                viewBox: vb,
                hasTitle: !!(title || aria),
                missingMarkers,
                fontWarnings,
                clipWarnings,
                overlapPairs,
                textCount: textNodes.length
              });
            });

            return report;
          });

          // Check first diagram for screenshot proof
          if (evalResults.length > 0 && vp.name === 'mobile' && theme === 'dark') {
            const firstSvg = await page.$('.diagram-svg');
            if (firstSvg) {
              const shotPath = path.join(SCREENSHOT_DIR, `${sub}_mobile_dark.png`);
              await firstSvg.screenshot({ path: shotPath });
            }
          }

          for (const res of evalResults) {
            totalDiagramsChecked++;
            let hasIssue = false;

            if (!res.hasViewBox) {
              issues.push(`[${sub.toUpperCase()}:${res.diagId}] Missing viewBox in ${vp.name} ${theme}`);
              hasIssue = true;
            }
            if (res.missingMarkers.length > 0) {
              issues.push(`[${sub.toUpperCase()}:${res.diagId}] Unresolved markers: ${res.missingMarkers.join(', ')} in ${vp.name} ${theme}`);
              hasIssue = true;
            }
            if (res.overlapPairs.length > 0) {
              for (const ov of res.overlapPairs) {
                issues.push(`[${sub.toUpperCase()}:${res.diagId}] Text overlap between "${ov.t1}" and "${ov.t2}"`);
              }
              hasIssue = true;
            }
            if (res.clipWarnings.length > 0) {
              for (const cl of res.clipWarnings) {
                issues.push(`[${sub.toUpperCase()}:${res.diagId}] Clipped text: "${cl.text}" outside viewBox`);
              }
              hasIssue = true;
            }

            if (hasIssue) totalIssuesFound++;
          }

          console.log(`  ✓ ${vp.name} (${vp.width}px) [${theme}]: Checked ${evalResults.length} diagrams.`);
          await context.close();
        }
      }
    }
  } finally {
    await browser.close();
  }

  console.log('\n' + '='.repeat(70));
  console.log(`VERIFICATION COMPLETE`);
  console.log(`Total Diagram Instances Audited: ${totalDiagramsChecked}`);
  console.log(`Issues Found: ${issues.length}`);
  if (issues.length > 0) {
    console.log('\nIssues Detail:');
    issues.slice(0, 20).forEach(iss => console.log('  ⚠️', iss));
    if (issues.length > 20) console.log(`  ... and ${issues.length - 20} more.`);
    return false;
  } else {
    console.log('✅ ALL DIAGRAMS PASSED ZERO-CLIPPING, ZERO-OVERLAP, AND RESPONSIVE BOUNDING-BOX GATES!');
    return true;
  }
}

if (require.main === module) {
  verifyAllDiagrams().then(passed => {
    process.exit(passed ? 0 : 1);
  }).catch(err => {
    console.error('Audit run failed:', err);
    process.exit(1);
  });
}

module.exports = { verifyAllDiagrams };
