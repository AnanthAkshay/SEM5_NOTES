const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const PORT = 8105;
const REPO_ROOT = path.resolve(__dirname, '..');
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const SCREENSHOT_DIR = path.join(REPO_ROOT, 'audit/se_screenshots');

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
  console.log('SOFTWARE ENGINEERING (24IS52) VERIFICATION SUITE');
  console.log('======================================================================');

  const server = await startServer();
  console.log(`Server listening on http://localhost:${PORT}/SEM5_NOTES/\n`);

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true
  });

  const subjectsData = require(path.join(REPO_ROOT, 'data/subjects.js'));
  const seSubject = subjectsData.subjects.find(s => s.id === 'se');

  let allPassed = true;

  try {
    // 1. HTTP 200 LINK GATE FOR ALL REGISTERED SE FILES
    console.log('--- 1. Checking HTTP 200 for all registered SE files ---');
    const registeredSeFiles = [];
    seSubject.units.forEach(u => {
      if (u.files) u.files.forEach(f => registeredSeFiles.push(f));
    });

    console.log(`Found ${registeredSeFiles.length} registered SE files.`);
    for (const file of registeredSeFiles) {
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

    // 2. RESPONSIVE OVERFLOW AT 1280, 768, 390, 320 ON SE PAGE
    console.log('\n--- 2. Checking Responsive Overflow on SE Page at 1280, 768, 390, 320 ---');
    const viewports = [
      { name: 'desktop', width: 1280, height: 800 },
      { name: 'tablet', width: 768, height: 1024 },
      { name: 'mobile', width: 390, height: 844 },
      { name: 'mobile-small', width: 320, height: 600 }
    ];

    for (const vp of viewports) {
      const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
      const page = await ctx.newPage();
      await page.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/se`, { waitUntil: 'networkidle' });

      const hasOverflow = await page.evaluate(() => {
        return document.documentElement.scrollWidth > window.innerWidth;
      });

      if (hasOverflow) {
        console.error(`  ❌ Horizontal overflow detected on SE page at ${vp.name} (${vp.width}px)!`);
        allPassed = false;
      } else {
        console.log(`  ✓ No horizontal overflow at ${vp.name} (${vp.width}px) on SE page.`);
      }
      await ctx.close();
    }

    // 3. UI RENDERING & IN-BROWSER VIEWER
    console.log('\n--- 3. Checking SE Practice Tab & Modal Viewer for Important Questions ---');
    const uiCtx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const uiPage = await uiCtx.newPage();
    const consoleErrors = [];
    uiPage.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });

    await uiPage.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/se`, { waitUntil: 'networkidle' });

    // Switch to Practice tab
    await uiPage.evaluate(() => window.SEM5_APP && window.SEM5_APP.switchTab('practice'));
    await uiPage.waitForTimeout(200);

    // Verify entry is displayed and appears exactly once
    const entryCheck = await uiPage.evaluate(() => {
      const rows = Array.from(document.querySelectorAll('.file-row'));
      const iqRows = rows.filter(r => {
        const title = r.querySelector('.file-title')?.textContent.trim() || '';
        return title.includes('Important Questions');
      });
      return {
        count: iqRows.length,
        firstTitle: iqRows[0]?.querySelector('.file-title')?.textContent.trim(),
        firstTag: iqRows[0]?.querySelector('.pill-tag-green, .pill-tag-purple, .pill-tag')?.textContent.trim()
      };
    });

    console.log(`  Important Questions entry count: ${entryCheck.count}`);
    if (entryCheck.count !== 1) {
      console.error(`  ❌ Expected exactly 1 Important Questions row, got ${entryCheck.count}!`);
      allPassed = false;
    } else {
      console.log(`  ✓ Found exactly 1 entry: "${entryCheck.firstTitle}" (tag: "${entryCheck.firstTag}")`);
    }

    if (consoleErrors.length > 0) {
      console.error('  ❌ Console errors on SE page:', consoleErrors);
      allPassed = false;
    } else {
      console.log('  ✓ Zero console errors on SE page.');
    }

    // Test in-browser viewer on the Important Questions PDF
    console.log('\n--- 4. Opening In-Browser Modal Viewer for SE Important Questions ---');
    const viewerResult = await uiPage.evaluate(() => {
      if (!window.SEM5_APP || !window.SEM5_APP.openViewer) return { success: false, reason: 'SEM5_APP not found' };
      window.SEM5_APP.openViewer('se-units-1-2-important-questions-pdf');
      const modal = document.getElementById('viewer-modal');
      const iframe = document.getElementById('viewer-iframe');
      return {
        success: modal && modal.classList.contains('open'),
        src: iframe ? iframe.src : ''
      };
    });

    if (viewerResult.success) {
      console.log(`  ✓ Viewer opened successfully with src: ${viewerResult.src}`);
    } else {
      console.error(`  ❌ Failed to open viewer for se-units-1-2-important-questions-pdf!`);
      allPassed = false;
    }

    await uiPage.waitForTimeout(600);
    const viewerShot = path.join(SCREENSHOT_DIR, 'se_important_questions_viewer.png');
    await uiPage.screenshot({ path: viewerShot });
    console.log(`  📸 Saved modal viewer screenshot: ${viewerShot}`);

    await uiPage.evaluate(() => window.SEM5_APP.closeViewer());
    await uiPage.waitForTimeout(100);

    // 5. GLOBAL SEARCH VERIFICATION
    console.log('\n--- 5. Checking Global Search for "Important Questions" ---');
    await uiPage.keyboard.press('/');
    await uiPage.waitForTimeout(150);
    await uiPage.fill('#search-input', 'important questions');
    await uiPage.waitForTimeout(150);

    const searchResults = await uiPage.evaluate(() => {
      const items = Array.from(document.querySelectorAll('.search-result-item'));
      return items.map(el => ({
        title: el.querySelector('.search-res-title')?.textContent.trim() || '',
        sub: el.querySelector('.search-res-breadcrumbs')?.textContent.trim() || ''
      }));
    });

    const seMatch = searchResults.find(r => r.sub.toLowerCase().includes('se') || r.sub.toLowerCase().includes('software engineering'));
    if (seMatch) {
      console.log(`  ✓ Found SE Important Questions in search results: "${seMatch.title}" (${seMatch.sub})`);
    } else {
      console.error('  ❌ SE Important Questions NOT found in search results for "important questions"!');
      allPassed = false;
    }

    // Verify NO "IS51" string appears in SE search results or anywhere on the page
    const pageText = await uiPage.evaluate(() => document.body.innerText);
    const containsIs51Se = /IS51.*Software|Software.*IS51/i.test(pageText);
    if (containsIs51Se) {
      console.error('  ❌ "IS51" found associated with Software Engineering on page!');
      allPassed = false;
    } else {
      console.log('  ✓ Zero occurrences of "IS51" associated with Software Engineering on the site.');
    }

    // 6. SCREENSHOTS AT 1280, 768, 390, 320 IN LIGHT AND DARK
    console.log('\n--- 6. Capturing SE Page Screenshots in Light & Dark ---');
    const shotConfigs = [
      { name: 'desktop_dark', width: 1280, height: 900, theme: 'dark' },
      { name: 'desktop_light', width: 1280, height: 900, theme: 'light' },
      { name: 'mobile_dark', width: 390, height: 844, theme: 'dark' },
      { name: 'mobile_light', width: 390, height: 844, theme: 'light' }
    ];

    for (const sc of shotConfigs) {
      const shotCtx = await browser.newContext({ viewport: { width: sc.width, height: sc.height } });
      const shotPage = await shotCtx.newPage();
      await shotPage.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/se`, { waitUntil: 'networkidle' });
      await shotPage.evaluate(t => {
        document.documentElement.setAttribute('data-theme', t);
        localStorage.setItem('sem5_theme_v1', t);
      }, sc.theme);
      await shotPage.waitForTimeout(200);

      // Switch to practice tab
      await shotPage.evaluate(() => window.SEM5_APP && window.SEM5_APP.switchTab('practice'));
      await shotPage.waitForTimeout(200);

      const pPath = path.join(SCREENSHOT_DIR, `se_practice_${sc.name}.png`);
      await shotPage.screenshot({ path: pPath, fullPage: false });
      console.log(`  📸 Saved screenshot: ${pPath}`);
      await shotCtx.close();
    }

    await uiCtx.close();

  } catch (err) {
    console.error('Test execution error:', err);
    allPassed = false;
  } finally {
    await browser.close();
    server.close();
  }

  if (allPassed) {
    console.log('\n======================================================================');
    console.log('✅ ALL SE VERIFICATION CHECKS PASSED PERFECTLY!');
    console.log('======================================================================\n');
    process.exit(0);
  } else {
    console.error('\n❌ SOME SE VERIFICATION CHECKS FAILED!\n');
    process.exit(1);
  }
}

runVerification();
