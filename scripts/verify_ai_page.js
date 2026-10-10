const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const PORT = 8098;
const REPO_ROOT = path.resolve(__dirname, '..');
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const SCREENSHOT_DIR = path.join(REPO_ROOT, 'audit/ai_screenshots');

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
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      let reqPath = req.url.split('?')[0];
      reqPath = decodeURIComponent(reqPath);

      if (reqPath.startsWith('/SEM5_NOTES/')) {
        reqPath = reqPath.replace('/SEM5_NOTES/', '/');
      }

      let filePath = path.join(REPO_ROOT, reqPath);
      if (reqPath === '/' || reqPath === '') {
        filePath = path.join(REPO_ROOT, 'index.html');
      }

      fs.stat(filePath, (err, stats) => {
        if (err || !stats.isFile()) {
          res.writeHead(404, { 'Content-Type': 'text/plain' });
          res.end(`404 Not Found: ${req.url}`);
          return;
        }

        const ext = path.extname(filePath).toLowerCase();
        const contentType = MIME_TYPES[ext] || 'application/octet-stream';
        res.writeHead(200, { 'Content-Type': contentType });
        fs.createReadStream(filePath).pipe(res);
      });
    });

    server.listen(PORT, () => {
      resolve(server);
    });
    server.on('error', reject);
  });
}

async function runVerification() {
  console.log('======================================================================');
  console.log('AI (ISE552) SPECIFIC VERIFICATION & REGRESSION SUITE');
  console.log('======================================================================');

  const server = await startServer();
  console.log(`Server listening on http://localhost:${PORT}/SEM5_NOTES/\n`);

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true
  });

  const subjectsData = require(path.join(REPO_ROOT, 'data/subjects.js'));
  const aiSubject = subjectsData.subjects.find(s => s.id === 'ai');

  let allPassed = true;

  try {
    // 1. HTTP 200 LINK GATE FOR ALL REGISTERED AI FILES
    console.log('--- 1. Checking HTTP 200 for all registered AI files ---');
    const registeredAiFiles = [];
    aiSubject.units.forEach(u => {
      u.files.forEach(f => registeredAiFiles.push(f));
    });

    console.log(`Found ${registeredAiFiles.length} registered AI files.`);
    for (const file of registeredAiFiles) {
      const fileUrl = `http://localhost:${PORT}/SEM5_NOTES/${file.path}`;
      const status = await new Promise(res => {
        http.get(fileUrl, r => {
          res(r.statusCode);
        }).on('error', () => res(500));
      });

      if (status !== 200) {
        console.error(`  ❌ [${file.id}] ${file.path} returned HTTP ${status}!`);
        allPassed = false;
      } else {
        console.log(`  ✓ [${file.id}] HTTP 200 -> ${file.path}`);
      }
    }

    // 2. RESPONSIVE OVERFLOW AT 1280, 768, 390, 320 ON AI PAGE
    console.log('\n--- 2. Checking Responsive Overflow on AI Page at 1280, 768, 390, 320 ---');
    const viewports = [
      { name: 'desktop', width: 1280, height: 800 },
      { name: 'tablet', width: 768, height: 1024 },
      { name: 'mobile', width: 390, height: 844 },
      { name: 'mobile-small', width: 320, height: 600 }
    ];

    for (const vp of viewports) {
      const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
      const page = await ctx.newPage();
      await page.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/ai`, { waitUntil: 'networkidle' });

      const hasOverflow = await page.evaluate(() => {
        return document.documentElement.scrollWidth > window.innerWidth;
      });

      if (hasOverflow) {
        console.error(`  ❌ Horizontal overflow detected on AI page at ${vp.name} (${vp.width}px)!`);
        allPassed = false;
      } else {
        console.log(`  ✓ No horizontal overflow at ${vp.name} (${vp.width}px) on AI page.`);
      }
      await ctx.close();
    }

    // 3. STRICT UNIT NOTES HIERARCHY GATE (HTML -> Handwritten -> Recent Notes ONLY)
    console.log('\n--- 3. Checking Strict AI Unit Notes Structure ---');
    const uiCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const uiPage = await uiCtx.newPage();
    const consoleErrors = [];
    uiPage.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });

    await uiPage.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/ai`, { waitUntil: 'networkidle' });

    const evalResult = await uiPage.evaluate(() => {
      const units = Array.from(document.querySelectorAll('.unit-pill-card'));
      const errors = [];
      const unitDetails = [];

      units.forEach(u => {
        const title = u.querySelector('.unit-summary-title')?.textContent.trim();
        const countLabel = u.querySelector('.unit-summary-meta span')?.textContent.trim();
        const rows = Array.from(u.querySelectorAll('.file-row'));

        const renderedCount = rows.length;
        const expectedCount = parseInt(countLabel) || 0;
        if (renderedCount !== expectedCount) {
          errors.push(`[${title}] Label '${countLabel}' != rendered rows (${renderedCount})`);
        }

        rows.forEach((row, idx) => {
          const rowTitle = row.querySelector('.file-title')?.textContent.trim();
          const typePill = row.querySelector('.file-type-pill')?.textContent.trim();
          const tagPill = row.querySelector('.pill-tag-green, .pill-tag-purple')?.textContent.trim();

          if (idx === 0) {
            if (typePill !== 'NOTES') {
              errors.push(`[${title}] Row 0 expected NOTES, got '${typePill}' (${rowTitle})`);
            }
          } else if (idx === 1) {
            if (typePill !== 'NOTEBOOK (PDF)') {
              errors.push(`[${title}] Row 1 expected NOTEBOOK (PDF), got '${typePill}' (${rowTitle})`);
            }
          } else {
            // Row 2+ MUST be Recent Notes
            if (!tagPill || !tagPill.includes('Recent Notes')) {
              errors.push(`[${title}] Row ${idx} '${rowTitle}' is missing Recent Notes tag!`);
            }
          }
        });

        unitDetails.push({ title, count: renderedCount });
      });

      return { errors, unitDetails };
    });

    if (evalResult.errors.length > 0) {
      console.error('  ❌ Strict Unit Structure Errors:');
      evalResult.errors.forEach(e => console.error(`    -> ${e}`));
      allPassed = false;
    } else {
      console.log('  ✓ Strict Unit Structure Verified:');
      evalResult.unitDetails.forEach(u => console.log(`    - ${u.title}: ${u.count} files`));
    }

    if (consoleErrors.length > 0) {
      console.error('  ❌ Console errors on AI page:', consoleErrors);
      allPassed = false;
    } else {
      console.log('  ✓ Zero console errors on AI page.');
    }

    // 4. IN-BROWSER PDF VIEWER GATE FOR ALL RECENT NOTES
    console.log('\n--- 4. Checking In-Browser PDF Viewer Gate for AI Recent Notes ---');
    const recentAiFiles = aiSubject.units.filter(u => typeof u.unitNumber === 'number').flatMap(u => u.files.slice(2));
    for (const f of recentAiFiles) {
      const opened = await uiPage.evaluate((fid) => {
        if (!window.SEM5_APP || !window.SEM5_APP.openViewer) return false;
        window.SEM5_APP.openViewer(fid);
        const modal = document.getElementById('viewer-modal');
        const iframe = document.getElementById('viewer-iframe');
        const imgWrap = document.getElementById('viewer-image-wrap');
        const isPdf = fid.endsWith('pdf');
        const isImg = fid.endsWith('jpg') || fid.endsWith('jpeg') || fid.endsWith('png');
        return {
          isOpen: modal && modal.classList.contains('open'),
          src: iframe ? iframe.src : '',
          imgSrc: imgWrap ? imgWrap.querySelector('img')?.src : ''
        };
      }, f.id);

      if (opened.isOpen) {
        console.log(`  ✓ Viewer opened "${f.id}": ${opened.src || opened.imgSrc}`);
      } else {
        console.error(`  ❌ Failed to open viewer for "${f.id}"!`);
        allPassed = false;
      }

      await uiPage.evaluate(() => {
        if (window.SEM5_APP && window.SEM5_APP.closeViewer) window.SEM5_APP.closeViewer();
      });
      await uiPage.waitForTimeout(50);
    }
    await uiCtx.close();

    // 5. GLOBAL SEARCH GATE (Search recent AI topics, removed files absent)
    console.log('\n--- 5. Checking Global Search for AI ---');
    const searchCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const searchPage = await searchCtx.newPage();
    await searchPage.goto(`http://localhost:${PORT}/SEM5_NOTES/`, { waitUntil: 'networkidle' });
    await searchPage.keyboard.press('/');
    await searchPage.waitForTimeout(150);

    const testQueries = ['Intelligent Agents', 'Informed Search', 'Uninformed Search', 'Local Search', 'Adversarial Search', 'PEAS'];
    for (const q of testQueries) {
      await searchPage.fill('#search-input', q);
      await searchPage.waitForTimeout(150);
      const count = await searchPage.evaluate(() => document.querySelectorAll('.search-result-item').length);
      console.log(`  ✓ Search query "${q}" -> ${count} results.`);
      if (count === 0) {
        console.error(`  ❌ Expected search results for active query "${q}", got 0!`);
        allPassed = false;
      }
    }
    await searchCtx.close();

    // 6. SCREENSHOTS OF AI SUBJECT PAGE
    console.log('\n--- 6. Capturing High-Res Screenshots of AI Subject Page ---');
    const shotModes = [
      { name: 'desktop_dark', width: 1280, height: 900, theme: 'dark' },
      { name: 'desktop_light', width: 1280, height: 900, theme: 'light' },
      { name: 'mobile_dark', width: 390, height: 844, theme: 'dark' },
      { name: 'mobile_light', width: 390, height: 844, theme: 'light' }
    ];

    for (const sm of shotModes) {
      const ctx = await browser.newContext({ viewport: { width: sm.width, height: sm.height } });
      const page = await ctx.newPage();
      await page.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/ai`, { waitUntil: 'networkidle' });
      await page.evaluate(t => {
        document.documentElement.setAttribute('data-theme', t);
        localStorage.setItem('sem5_theme_v1', t);
      }, sm.theme);
      await page.waitForTimeout(200);

      const shotPath = path.join(SCREENSHOT_DIR, `ai_${sm.name}.png`);
      await page.screenshot({ path: shotPath, fullPage: false });
      console.log(`  📸 Saved screenshot: ${shotPath}`);
      await ctx.close();
    }

  } catch (err) {
    console.error('Test execution error:', err);
    allPassed = false;
  } finally {
    await browser.close();
    server.close();
  }

  if (allPassed) {
    console.log('\n======================================================================');
    console.log('✅ ALL AI VERIFICATION CHECKS PASSED PERFECTLY!');
    console.log('======================================================================\n');
    process.exit(0);
  } else {
    console.error('\n❌ SOME AI VERIFICATION CHECKS FAILED!\n');
    process.exit(1);
  }
}

runVerification();
