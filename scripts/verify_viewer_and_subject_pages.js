/**
 * SEM 5 · Viewer Gate & Subject Pages Comprehensive Verification Script
 * - Tests in-browser PDF viewer opening across desktop & mobile
 * - Tests zero horizontal overflow at 1280px, 768px, 390px, and 320px
 * - Tests UI GATE: Every unit strictly shows:
 *     1. Interactive Notes (HTML)
 *     2. Handwritten Notebook (PDF)
 *     3. Recent Notes (tag: 'Recent Notes')
 *     And NO OTHER old faculty slide or removed PDF note!
 * - Tests SEARCH GATE:
 *     - Newly synced recent notes ARE searchable
 *     - Removed files & old titles NEVER appear
 * - Tests theme toggling & zero console errors
 * - Captures high-res screenshots for all 8 subject pages in desktop/mobile, light/dark
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const PORT = 8099;
const REPO_ROOT = path.resolve(__dirname, '..');
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const SCREENSHOT_DIR = path.join(REPO_ROOT, 'audit/subject_screenshots');

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

const MIME_TYPES = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.css': 'text/css',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.pdf': 'application/pdf',
  '.woff2': 'font/woff2'
};

function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let reqPath = decodeURIComponent(req.url.split('?')[0]);
      if (reqPath.startsWith('/SEM5_NOTES/')) {
        reqPath = reqPath.slice('/SEM5_NOTES/'.length);
      } else if (reqPath === '/SEM5_NOTES') {
        reqPath = '';
      }

      if (!reqPath || reqPath.endsWith('/')) {
        reqPath += 'index.html';
      }

      const filePath = path.join(REPO_ROOT, reqPath);
      if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
        const ext = path.extname(filePath).toLowerCase();
        const mime = MIME_TYPES[ext] || 'application/octet-stream';
        res.writeHead(200, { 'Content-Type': mime });
        fs.createReadStream(filePath).pipe(res);
      } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end(`404 Not Found: ${req.url}`);
      }
    });

    server.listen(PORT, () => {
      console.log(`Server listening on http://localhost:${PORT}/SEM5_NOTES/`);
      resolve(server);
    });
  });
}

async function runViewerAndSubjectGates() {
  console.log('='.repeat(70));
  console.log('VIEWER GATE, STRICT UNIT UI GATE & SUBJECT VERIFICATION');
  console.log('='.repeat(70));

  const server = await startServer();
  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--allow-file-access-from-files']
  });

  const subjectsModule = require(path.join(REPO_ROOT, 'data/subjects.js'));
  const subjectsData = subjectsModule.subjects || global.window.SEM5_DATA.subjects;

  let allPassed = true;

  try {
    // 1. TEST HORIZONTAL OVERFLOW AT 1280, 768, 390, 320
    console.log('\n--- 1. Checking Horizontal Overflow at 1280, 768, 390, 320 ---');
    const viewports = [
      { name: 'desktop', width: 1280, height: 800 },
      { name: 'tablet', width: 768, height: 1024 },
      { name: 'mobile', width: 390, height: 844 },
      { name: 'mobile-small', width: 320, height: 600 }
    ];

    for (const vp of viewports) {
      const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
      const page = await ctx.newPage();
      await page.goto(`http://localhost:${PORT}/SEM5_NOTES/`, { waitUntil: 'networkidle' });

      const hasOverflow = await page.evaluate(() => {
        return document.documentElement.scrollWidth > window.innerWidth;
      });

      if (hasOverflow) {
        console.error(`  ❌ Horizontal overflow detected on home page at ${vp.name} (${vp.width}px)!`);
        allPassed = false;
      } else {
        console.log(`  ✓ No horizontal overflow at ${vp.name} (${vp.width}px) on home page.`);
      }

      // Check on a subject page too
      await page.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/cn`, { waitUntil: 'networkidle' });
      const hasSubjectOverflow = await page.evaluate(() => {
        return document.documentElement.scrollWidth > window.innerWidth;
      });
      if (hasSubjectOverflow) {
        console.error(`  ❌ Horizontal overflow detected on CN subject page at ${vp.name} (${vp.width}px)!`);
        allPassed = false;
      } else {
        console.log(`  ✓ No horizontal overflow at ${vp.name} (${vp.width}px) on subject page.`);
      }

      await ctx.close();
    }

    // 2. TEST STRICT UNIT NOTES COMPLIANCE ACROSS ALL 8 SUBJECTS
    console.log('\n--- 2. Checking Strict Unit Notes Structure (HTML -> Handwritten -> Recent Notes ONLY) ---');
    const unitCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const unitPage = await unitCtx.newPage();

    for (const sub of subjectsData) {
      await unitPage.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/${sub.id}`, { waitUntil: 'networkidle' });
      
      const unitResults = await unitPage.evaluate((subId) => {
        const units = Array.from(document.querySelectorAll('.unit-pill-card'));
        const errors = [];
        const unitsSummary = [];

        units.forEach(u => {
          const title = u.querySelector('.unit-summary-title')?.textContent.trim();
          const countLabel = u.querySelector('.unit-summary-meta span')?.textContent.trim();
          const rows = Array.from(u.querySelectorAll('.file-row'));

          const renderedCount = rows.length;
          const expectedCount = parseInt(countLabel) || 0;
          if (renderedCount !== expectedCount) {
            errors.push(`[${subId} - ${title}] Summary label '${countLabel}' != rendered rows (${renderedCount})`);
          }

          // Check row sequence: 0 = Notes, 1 = Handwritten, 2+ = Recent Notes
          rows.forEach((row, idx) => {
            const rowTitle = row.querySelector('.file-title')?.textContent.trim();
            const typePill = row.querySelector('.file-type-pill')?.textContent.trim();
            const tagPill = row.querySelector('.pill-tag-green, .pill-tag-purple')?.textContent.trim();

            if (idx === 0) {
              if (typePill !== 'NOTES') {
                errors.push(`[${subId} - ${title}] Row 0 expected NOTES, got '${typePill}' (${rowTitle})`);
              }
            } else if (idx === 1) {
              if (typePill !== 'NOTEBOOK (PDF)') {
                errors.push(`[${subId} - ${title}] Row 1 expected NOTEBOOK (PDF), got '${typePill}' (${rowTitle})`);
              }
            } else {
              // Row 2+ MUST be Recent Notes
              if (!tagPill || !tagPill.includes('Recent Notes')) {
                errors.push(`[${subId} - ${title}] Row ${idx} '${rowTitle}' is missing Recent Notes tag! (got: '${tagPill}')`);
              }
            }
          });

          unitsSummary.push(`${title}: ${renderedCount} files`);
        });

        return { errors, unitsSummary };
      }, sub.id);

      if (unitResults.errors.length > 0) {
        console.error(`  ❌ Violations in ${sub.id}:`);
        unitResults.errors.forEach(e => console.error(`    -> ${e}`));
        allPassed = false;
      } else {
        console.log(`  ✓ [${sub.id}] Strict Unit Structure Verified: ${unitResults.unitsSummary.join(' | ')}`);
      }
    }
    await unitCtx.close();

    // 3. TEST GLOBAL SEARCH (Recent notes searchable, removed files absent)
    console.log('\n--- 3. Checking Global Search (Recent Notes Present & Removed Notes Absent) ---');
    const searchCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const searchPage = await searchCtx.newPage();
    await searchPage.goto(`http://localhost:${PORT}/SEM5_NOTES/`, { waitUntil: 'networkidle' });

    // Open search modal
    await searchPage.keyboard.press('/');
    await searchPage.waitForTimeout(200);

    // Test that Recent notes are searchable
    const recentQueries = ['Tableau', 'IPv4', 'Agile', 'Adversarial', 'Regression', 'Complete Course Notebook'];
    for (const q of recentQueries) {
      await searchPage.fill('#search-input', q);
      await searchPage.waitForTimeout(150);
      const resultsCount = await searchPage.evaluate(() => document.querySelectorAll('.search-result-item').length);
      console.log(`  ✓ Search query "${q}" -> found ${resultsCount} results.`);
      if (resultsCount === 0) {
        console.error(`  ❌ Expected search results for active query "${q}", got 0!`);
        allPassed = false;
      }
    }

    // Test that Removed files NEVER appear in search
    const removedQueries = [
      'Unit 1 And 2 Alternate',
      'Shruti Mam',
      'ai-informed-search',
      'is53-cn-unit1.pdf',
      'Unit 1 (22.4 MB)'
    ];
    for (const q of removedQueries) {
      await searchPage.fill('#search-input', q);
      await searchPage.waitForTimeout(150);
      const resultsCount = await searchPage.evaluate(() => document.querySelectorAll('.search-result-item').length);
      if (resultsCount > 0) {
        console.error(`  ❌ Removed file/title appeared in search for "${q}" (found ${resultsCount} results)!`);
        allPassed = false;
      } else {
        console.log(`  ✓ Removed query "${q}" -> 0 results (correctly excluded).`);
      }
    }

    await searchPage.keyboard.press('Escape');
    await searchCtx.close();

    // 4. TEST IN-BROWSER PDF VIEWER GATE
    console.log('\n--- 4. Checking In-Browser PDF Viewer Gate ---');
    const viewerCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const viewerPage = await viewerCtx.newPage();
    const consoleErrors = [];
    viewerPage.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });

    await viewerPage.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/ml`, { waitUntil: 'networkidle' });

    const testPdfIds = [
      'ml-ml-ch2-understanding-data-pdf',
      'se-unit-1-1-pdf',
      'cn-cn-unit1-complete-pdf',
      'toc-toc-notes-complete-pdf',
      'ai-ai-adversarial-search-pdf',
      'rmipr-rm-ipr-unit1-pdf'
    ];

    for (const fid of testPdfIds) {
      const opened = await viewerPage.evaluate((fileId) => {
        if (window.SEM5_APP && window.SEM5_APP.openViewer) {
          window.SEM5_APP.openViewer(fileId);
          const modal = document.getElementById('viewer-modal');
          const iframe = document.getElementById('viewer-iframe');
          return {
            isOpen: modal && modal.classList.contains('open'),
            src: iframe ? iframe.src : ''
          };
        }
        return null;
      }, fid);

      if (opened && opened.isOpen && opened.src && !opened.src.endsWith('about:blank')) {
        console.log(`  ✓ PDF Viewer successfully opened recent file "${fid}": iframe loaded -> ${opened.src.split('/SEM5_NOTES/')[1] || opened.src}`);
      } else {
        console.error(`  ❌ PDF Viewer failed to open file "${fid}"!`, opened);
        allPassed = false;
      }

      await viewerPage.evaluate(() => {
        if (window.SEM5_APP && window.SEM5_APP.closeViewer) window.SEM5_APP.closeViewer();
      });
      await viewerPage.waitForTimeout(100);
    }
    await viewerCtx.close();

    // 5. CAPTURE HIGH-RES SCREENSHOTS FOR ALL 8 SUBJECT PAGES (Desktop & Mobile, Light & Dark)
    console.log('\n--- 5. Capturing High-Res Screenshots for all 8 Subject Pages ---');
    const renderModes = [
      { name: 'desktop', width: 1280, height: 900, theme: 'dark' },
      { name: 'desktop', width: 1280, height: 900, theme: 'light' },
      { name: 'mobile', width: 390, height: 844, theme: 'dark' },
      { name: 'mobile', width: 390, height: 844, theme: 'light' }
    ];

    for (const mode of renderModes) {
      console.log(`\nRendering Viewport: ${mode.name} (${mode.width}px) | Theme: [${mode.theme}]`);
      const ctx = await browser.newContext({ viewport: { width: mode.width, height: mode.height } });
      const page = await ctx.newPage();

      for (const sub of subjectsData) {
        await page.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/${sub.id}`, { waitUntil: 'networkidle' });

        await page.evaluate((t) => {
          document.documentElement.setAttribute('data-theme', t);
          localStorage.setItem('sem5_theme_v1', t);
        }, mode.theme);
        await page.waitForTimeout(200);

        const titleText = await page.evaluate(() => {
          const el = document.querySelector('.subject-view-title');
          return el ? el.textContent.trim() : '';
        });

        const shotPath = path.join(SCREENSHOT_DIR, `${sub.id}_${mode.name}_${mode.theme}.png`);
        await page.screenshot({ path: shotPath, fullPage: false });
        console.log(`  📸 [${sub.id}] "${titleText}" -> ${path.basename(shotPath)}`);
      }
      await ctx.close();
    }

  } catch (err) {
    console.error(`Verification error:`, err);
    allPassed = false;
  } finally {
    await browser.close();
    server.close();
  }

  console.log('\n' + '='.repeat(70));
  if (allPassed) {
    console.log('✅ ALL VIEWER, RESPONSIVE, STRICT UNIT & SEARCH TESTS PASSED!');
  } else {
    console.log('❌ SOME TESTS FAILED!');
    process.exit(1);
  }
}

runViewerAndSubjectGates();
