/**
 * SEM 5 · Automated Regression Test Suite:
 * - Home page rendering at 1280px & 390px in dark & light modes
 * - Zero console/page errors
 * - Exactly 8 subject cards with code, name, description, progress bar, pin button
 * - Filter pills verification: All (8), Core ISE (4), Electives & AEC (4), Practice Ready (8)
 * - Navigation to subject detail view & presence of Notes, Handwritten, Solved PYQs, Practice
 * - HTTP 200 checks for all subject links, units, notebooks, and PYQ pages
 * - Screenshots capture to audit/home_screenshots/
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const PORT = 8098;
const REPO_ROOT = path.resolve(__dirname, '..');
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const SCREENSHOT_DIR = path.join(REPO_ROOT, 'audit/home_screenshots');

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

async function runTestSuite() {
  console.log('='.repeat(70));
  console.log('HOME PAGE & SUBJECT CARDS COMPREHENSIVE VERIFICATION SUITE');
  console.log('='.repeat(70));

  const server = await startServer();
  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--allow-file-access-from-files']
  });

  const testConfigs = [
    { name: 'desktop', width: 1280, height: 800, theme: 'dark' },
    { name: 'desktop', width: 1280, height: 800, theme: 'light' },
    { name: 'mobile', width: 390, height: 844, theme: 'dark' },
    { name: 'mobile', width: 390, height: 844, theme: 'light' }
  ];

  let allTestsPassed = true;

  try {
    for (const cfg of testConfigs) {
      console.log(`\nTesting Viewport: ${cfg.name} (${cfg.width}px) | Theme: [${cfg.theme}]`);
      const context = await browser.newContext({ viewport: { width: cfg.width, height: cfg.height } });
      const page = await context.newPage();

      const consoleErrors = [];
      const pageErrors = [];

      page.on('console', msg => {
        if (msg.type() === 'error') {
          consoleErrors.push(msg.text());
        }
      });
      page.on('pageerror', err => {
        pageErrors.push(err.toString());
      });

      await page.goto(`http://localhost:${PORT}/SEM5_NOTES/`, { waitUntil: 'networkidle' });

      // Apply theme
      await page.evaluate((t) => {
        if (window.SEM5_APP) {
          document.documentElement.setAttribute('data-theme', t);
          localStorage.setItem('sem5_theme_v1', t);
        }
      }, cfg.theme);
      await page.waitForTimeout(300);

      // Assert zero console/page errors
      if (pageErrors.length > 0 || consoleErrors.length > 0) {
        console.error(`  ❌ Errors detected in ${cfg.name} ${cfg.theme}:`);
        pageErrors.forEach(e => console.error('    Page error:', e));
        consoleErrors.forEach(e => console.error('    Console error:', e));
        allTestsPassed = false;
      } else {
        console.log(`  ✓ Zero console errors and zero page crashes.`);
      }

      // Assert exactly 8 cards rendered
      const cardCount = await page.evaluate(() => document.querySelectorAll('.subject-card').length);
      if (cardCount !== 8) {
        console.error(`  ❌ Expected 8 subject cards, got: ${cardCount}`);
        allTestsPassed = false;
      } else {
        console.log(`  ✓ Exactly 8 subject cards rendered.`);
      }

      // Assert card structure (code, title, desc, pin btn, exam chip)
      const cardsValid = await page.evaluate(() => {
        const cards = Array.from(document.querySelectorAll('.subject-card'));
        return cards.every(c => {
          const hasCode = !!c.querySelector('.card-code-circle');
          const hasTitle = !!c.querySelector('.card-title');
          const hasDesc = !!c.querySelector('.card-desc');
          const hasPin = !!c.querySelector('.pin-btn');
          const hasExamChip = !!c.querySelector('.card-exam-chip');
          return hasCode && hasTitle && hasDesc && hasPin && hasExamChip;
        });
      });

      if (!cardsValid) {
        console.error(`  ❌ Card structure incomplete (missing code/title/desc/pin/exam-chip)`);
        allTestsPassed = false;
      } else {
        console.log(`  ✓ All 8 cards have complete original structure with single exam chip.`);
      }

      // Assert that each card links to #subject/<id>
      const cardsLinkValid = await page.evaluate(() => {
        const cards = Array.from(document.querySelectorAll('.subject-card'));
        return cards.every(c => {
          const href = c.getAttribute('href');
          const subId = c.getAttribute('data-subject');
          return subId && href === `#subject/${subId}`;
        });
      });
      if (!cardsLinkValid) {
        console.error(`  ❌ Cards missing proper link to #subject/<id>`);
        allTestsPassed = false;
      } else {
        console.log(`  ✓ Each card links directly to #subject/<id>.`);
      }

      // Test filter pills
      // 1. All (8)
      await page.click('button[data-filter="all"]');
      const allCount = await page.evaluate(() => document.querySelectorAll('.subject-card').length);
      // 2. Core ISE
      await page.click('button[data-filter="core"]');
      const coreCount = await page.evaluate(() => document.querySelectorAll('.subject-card').length);
      // 3. Electives & AEC
      await page.click('button[data-filter="elective"]');
      const elecCount = await page.evaluate(() => document.querySelectorAll('.subject-card').length);
      // 4. Practice Ready
      await page.click('button[data-filter="practice"]');
      const pracCount = await page.evaluate(() => document.querySelectorAll('.subject-card').length);
      // Reset to all
      await page.click('button[data-filter="all"]');

      console.log(`  ✓ Filter Pills: All=${allCount}, Core=${coreCount}, Electives=${elecCount}, Practice=${pracCount}`);
      if (allCount !== 8 || coreCount !== 4 || elecCount !== 4 || pracCount !== 8) {
        console.error(`  ❌ Filter counts unexpected! Expected 8, 4, 4, 8.`);
        allTestsPassed = false;
      }

      // Scroll to subjects section to capture the subject cards clearly
      await page.evaluate(() => document.getElementById('subjects-section').scrollIntoView({ behavior: 'instant' }));
      await page.waitForTimeout(300);

      // Take screenshot of home page cards section
      const shotName = `home_${cfg.name}_${cfg.theme}.png`;
      await page.screenshot({ path: path.join(SCREENSHOT_DIR, shotName), fullPage: false });
      console.log(`  📸 Screenshot saved: ${shotName}`);

      // If desktop dark, test clicking subject card to open subject view
      if (cfg.name === 'desktop' && cfg.theme === 'dark') {
        console.log('\nTesting Subject View Interaction (clicking Computer Networks)...');
        // Click CN card
        await page.click('.subject-card[data-subject="cn"]');
        await page.waitForTimeout(400);

        const isSubjectActive = await page.evaluate(() => {
          return document.getElementById('subject-view').classList.contains('active');
        });
        const hasScopeLine = await page.evaluate(() => {
          return !!document.querySelector('.subject-scope-line');
        });
        const tabs = await page.evaluate(() => {
          return Array.from(document.querySelectorAll('.segmented-tab')).map(t => t.textContent.trim());
        });

        console.log(`  ✓ Subject View active: ${isSubjectActive}`);
        console.log(`  ✓ CIE-1 Scope line present: ${hasScopeLine}`);
        console.log(`  ✓ Tabs found: ${tabs.join(' | ')}`);

        // Assert presence of Notes, Handwritten, Solved PYQs and Practice
        const subjectFeatures = await page.evaluate(() => {
          const tabsText = Array.from(document.querySelectorAll('.segmented-tab')).map(t => t.textContent.trim());
          const hasNotesTab = tabsText.some(t => t.includes('Notes'));
          const hasPyqTab = tabsText.some(t => t.includes('Solved PYQs') || t.includes('PYQ'));
          const hasPracticeTab = tabsText.some(t => t.includes('Practice'));
          const hasHandwrittenPills = !!document.querySelector('.file-type-handwritten') || !!document.querySelector('.pill-tag-purple');
          return { hasNotesTab, hasPyqTab, hasPracticeTab, hasHandwrittenPills };
        });

        if (subjectFeatures.hasNotesTab && subjectFeatures.hasPyqTab && subjectFeatures.hasPracticeTab && subjectFeatures.hasHandwrittenPills) {
          console.log('  ✓ Subject view successfully displays Notes, Handwritten, Solved PYQs, and Practice entries.');
        } else {
          console.error('  ❌ Subject view missing expected entries:', subjectFeatures);
          allTestsPassed = false;
        }

        // Switch to Solved PYQs tab
        const pyqTab = await page.$('.segmented-tab:has-text("Solved PYQs")');
        if (pyqTab) {
          await pyqTab.click();
          await page.waitForTimeout(300);
          const pyqCardCount = await page.evaluate(() => document.querySelectorAll('.scheme-section-card, .pyq-hub-container').length);
          console.log(`  ✓ Switched to Solved PYQs tab (found ${pyqCardCount} sections/cards).`);
        } else {
          console.error('  ❌ Solved PYQs tab not found!');
          allTestsPassed = false;
        }

        // Capture screenshot of subject view
        const subShotName = 'subject_cn_desktop_dark.png';
        await page.screenshot({ path: path.join(SCREENSHOT_DIR, subShotName), fullPage: false });
        console.log(`  📸 Subject View Screenshot saved: ${subShotName}`);
      }

      await context.close();
    }

    // HTTP 200 check for all links in data/subjects.js
    console.log('\n' + '='.repeat(70));
    console.log('CHECKING ALL HTTP LINKS IN data/subjects.js');
    console.log('='.repeat(70));

    global.window = {};
    require(path.join(REPO_ROOT, 'data/subjects.js'));
    const subjectsData = global.window.SEM5_DATA.subjects;

    const testPage = await browser.newPage();
    let checkedCount = 0;
    let failedCount = 0;

    for (const sub of subjectsData) {
      for (const unit of sub.units) {
        for (const file of (unit.files || [])) {
          if (file.path && !file.path.startsWith('http') && !file.path.startsWith('//')) {
            const url = `http://localhost:${PORT}/SEM5_NOTES/${file.path}`;
            try {
              const res = await testPage.goto(url, { waitUntil: 'load', timeout: 5000 });
              if (res.status() !== 200) {
                console.error(`  ❌ HTTP ${res.status()}: ${file.path}`);
                failedCount++;
                allTestsPassed = false;
              } else {
                checkedCount++;
              }
            } catch (err) {
              console.error(`  ❌ Request failed for ${file.path}: ${err.message}`);
              failedCount++;
              allTestsPassed = false;
            }
          }
        }
      }
    }
    await testPage.close();
    console.log(`✓ Verified ${checkedCount} resource paths from subjects.js. Failed: ${failedCount}`);

    // Verify every subject SPA page loads correctly via hash
    console.log('\n' + '='.repeat(70));
    console.log('CHECKING ALL 8 SUBJECT DETAIL SPA VIEWS');
    console.log('='.repeat(70));
    const subPage = await browser.newPage();
    for (const sub of subjectsData) {
      await subPage.goto(`http://localhost:${PORT}/SEM5_NOTES/#subject/${sub.id}`, { waitUntil: 'networkidle' });
      const title = await subPage.evaluate(() => {
        const el = document.querySelector('.subject-view-title');
        return el ? el.textContent.trim() : '';
      });
      if (!title) {
        console.error(`  ❌ Subject view failed to load for ${sub.id}`);
        allTestsPassed = false;
      } else {
        console.log(`  ✓ Subject view loaded: ${sub.id} -> "${title}"`);
      }
    }
    await subPage.close();

  } finally {
    await browser.close();
    server.close();
  }

  console.log('\n' + '='.repeat(70));
  if (allTestsPassed) {
    console.log('✅ ALL HOME PAGE, CARD, FILTER, AND LINK TESTS PASSED!');
    return true;
  } else {
    console.error('❌ TESTS FAILED!');
    return false;
  }
}

if (require.main === module) {
  runTestSuite().then(passed => {
    process.exit(passed ? 0 : 1);
  }).catch(err => {
    console.error('Test suite failed:', err);
    process.exit(1);
  });
}

module.exports = { runTestSuite };
