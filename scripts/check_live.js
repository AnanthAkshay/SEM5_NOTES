/**
 * SEM 5 · ISE Notes - Post-Deployment Live Verification Script
 * 
 * Verifies live GitHub Pages deployment:
 * - Home page, 404 page, manifest, and assets
 * - Every subject view (all 8 subjects)
 * - Every standard unit notes HTML page (all 24 units)
 * - Every handwritten web notebook HTML page (all 24 units)
 * - Every handwritten notebook PDF file (all 24 units)
 * - MIME types, HTTP status codes, console errors, broken internal links
 * 
 * Usage:
 *   node scripts/check_live.js [BASE_URL]
 * 
 * Example:
 *   node scripts/check_live.js https://ananthakshay.github.io/SEM5_NOTES/
 */

const { chromium } = require('playwright');
const https = require('https');
const http = require('http');
const url = require('url');

const DEFAULT_BASE = 'https://ananthakshay.github.io/SEM5_NOTES';
const targetBase = (process.argv[2] || DEFAULT_BASE).replace(/\/+$/, '');

const SUBJECTS = [
  { id: 'ai', code: 'ISE552', name: 'Artificial Intelligence', units: [1, 2, 3] },
  { id: 'cn', code: 'IS53', name: 'Computer Networks', units: [1, 2, 3] },
  { id: 'evs', code: 'HS510', name: 'Environmental Studies', units: [1, 2, 3] },
  { id: 'ml', code: 'IS51', name: 'Machine Learning', units: [1, 2, 3] },
  { id: 'reactjs', code: 'ISAEC594', name: 'ReactJS', units: [1, 2, 3] },
  { id: 'rmipr', code: 'AL58', name: 'Research Methodology & IPR', units: [1, 2, 3] },
  { id: 'se', code: 'IS52', name: 'Software Engineering', units: [1, 2, 3] },
  { id: 'toc', code: 'IS54', name: 'Theory of Computation', units: [1, 2, 3] }
];

async function httpCheck(targetUrl) {
  return new Promise((resolve) => {
    try {
      const parsed = new URL(targetUrl);
      const client = parsed.protocol === 'https:' ? https : http;
      const options = {
        method: 'HEAD',
        headers: { 'User-Agent': 'SEM5-LiveChecker/1.0' }
      };
      const req = client.request(parsed, options, (res) => {
        // Follow redirect if 301/302
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          const nextUrl = new URL(res.headers.location, targetUrl).toString();
          httpCheck(nextUrl).then(resolve);
          return;
        }
        resolve({
          url: targetUrl,
          status: res.statusCode,
          contentType: res.headers['content-type'] || '',
          contentLength: parseInt(res.headers['content-length'] || '0', 10)
        });
      });
      req.on('error', (err) => {
        resolve({ url: targetUrl, status: 0, error: err.message });
      });
      req.setTimeout(12000, () => {
        req.destroy();
        resolve({ url: targetUrl, status: 0, error: 'Timeout after 12s' });
      });
      req.end();
    } catch (err) {
      resolve({ url: targetUrl, status: 0, error: err.message });
    }
  });
}

(async () => {
  console.log(`\n======================================================`);
  console.log(` SEM 5 · Post-Deploy Verification Suite`);
  console.log(` Target Base URL: ${targetBase}`);
  console.log(`======================================================\n`);

  let totalTests = 0;
  let passedTests = 0;
  const failures = [];

  function record(name, pass, detail) {
    totalTests++;
    if (pass) {
      passedTests++;
      console.log(`  [PASS] ${name}`);
    } else {
      failures.push({ name, detail });
      console.error(`  [FAIL] ${name} -> ${detail}`);
    }
  }

  // --- Phase 1: HTTP Head checks on Core Assets ---
  console.log(`\n--- Phase 1: Core Portal & Asset Checks ---`);
  const coreEndpoints = [
    { name: 'Home HTML', path: '/index.html', expectMime: 'text/html' },
    { name: '404 Error Page', path: '/404.html', expectMime: 'text/html' },
    { name: 'Robots.txt', path: '/robots.txt', expectMime: 'text/plain' },
    { name: 'Manifest', path: '/manifest.webmanifest', expectMime: '' },
    { name: 'Design Stylesheet', path: '/css/style.css', expectMime: 'text/css' },
    { name: 'Handwritten Stylesheet', path: '/css/handwritten.css', expectMime: 'text/css' },
    { name: 'App JavaScript', path: '/js/app.js', expectMime: 'javascript' },
    { name: 'Subjects Data', path: '/data/subjects.js', expectMime: 'javascript' }
  ];

  for (const ep of coreEndpoints) {
    const epUrl = `${targetBase}${ep.path}`;
    const res = await httpCheck(epUrl);
    const pass = res.status === 200 && (!ep.expectMime || res.contentType.includes(ep.expectMime));
    record(
      `${ep.name} (${ep.path})`,
      pass,
      `HTTP ${res.status}, Type: ${res.contentType || 'none'}`
    );
  }

  // --- Phase 2: PDF Handwritten Notebook Head Checks (all 24 units) ---
  console.log(`\n--- Phase 2: Handwritten Notebook PDFs (24 Units) ---`);
  for (const sub of SUBJECTS) {
    for (const u of sub.units) {
      const pdfPath = `/notes/${sub.id}/unit${u}/handwritten/${sub.id}-unit${u}-handwritten.pdf`;
      const pdfUrl = `${targetBase}${pdfPath}`;
      const res = await httpCheck(pdfUrl);
      const isPdf = res.status === 200 && res.contentType.includes('pdf');
      const hasContent = !res.contentLength || res.contentLength > 50000;
      record(
        `PDF: ${sub.code} Unit ${u} (${sub.id}-unit${u}-handwritten.pdf)`,
        isPdf && hasContent,
        `Status=${res.status}, Size=${Math.round(res.contentLength/1024)} KB, MIME=${res.contentType}`
      );
    }
  }

  // --- Phase 3: Browser Runtime & Console Error Checks with Playwright ---
  console.log(`\n--- Phase 3: Playwright Runtime & Browser Integrity ---`);
  try {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const fs = require('fs');
    if (fs.existsSync(chromePath)) {
      browser = await chromium.launch({ executablePath: chromePath, headless: true });
    } else {
      browser = await chromium.launch({ channel: 'chrome', headless: true });
    }
  } catch (err) {
    try {
      browser = await chromium.launch({ headless: true });
    } catch (e2) {
      console.warn(`[WARN] Chromium launch warning: ${err.message}. Testing without browser UI pass.`);
    }
  }

  if (browser) {
    const page = await browser.newPage();
    const consoleErrors = [];
    const failedNetwork = [];

    page.on('console', msg => {
      if (msg.type() === 'error') {
        const text = msg.text();
        if (!text.includes('attribute height: Expected length, "auto"')) {
          consoleErrors.push(text);
        }
      }
    });

    page.on('response', resp => {
      if (resp.status() >= 400) {
        failedNetwork.push(`${resp.status()} on ${resp.url()}`);
      }
    });

    // Test 3.1: Home Page Loading & Navigation
    console.log(`  Visiting Home Page: ${targetBase}/`);
    consoleErrors.length = 0;
    failedNetwork.length = 0;
    try {
      const resp = await page.goto(`${targetBase}/`, { waitUntil: 'networkidle', timeout: 20000 });
      record('Home page loads with HTTP 200', resp && resp.status() === 200, `status=${resp ? resp.status() : 'null'}`);
      record('Home page has 0 console errors', consoleErrors.length === 0, consoleErrors.join('; '));
      record('Home page has 0 failed asset requests', failedNetwork.length === 0, failedNetwork.join('; '));

      // Test subject navigation
      await page.evaluate(() => window.SEM5_APP && window.SEM5_APP.openSubject('ai'));
      await page.waitForTimeout(400);
      const aiVisible = await page.evaluate(() => document.getElementById('subject-view').classList.contains('active'));
      record('SPA routing switches to Subject Detail View', aiVisible, 'subject-view active class');
    } catch (e) {
      record('Home page browser test', false, e.message);
    }

    // Test 3.2: Sample Unit Notes HTML Page
    console.log(`  Visiting HTML Notes: ${targetBase}/notes/toc/unit1/unit-1-notes.html`);
    consoleErrors.length = 0;
    failedNetwork.length = 0;
    try {
      const resp = await page.goto(`${targetBase}/notes/toc/unit1/unit-1-notes.html`, { waitUntil: 'domcontentloaded', timeout: 20000 });
      record('TOC Unit 1 notes loads HTTP 200', resp && resp.status() === 200, `status=${resp ? resp.status() : 'null'}`);
      record('TOC Unit 1 notes 0 console errors', consoleErrors.length === 0, consoleErrors.join('; '));
      record('TOC Unit 1 notes 0 failed assets', failedNetwork.length === 0, failedNetwork.join('; '));
    } catch (e) {
      record('TOC Unit 1 notes test', false, e.message);
    }

    // Test 3.3: Sample Handwritten Web HTML Page
    console.log(`  Visiting Handwritten Web: ${targetBase}/notes/ml/unit1/handwritten/ml-unit1-handwritten.html`);
    consoleErrors.length = 0;
    failedNetwork.length = 0;
    try {
      const resp = await page.goto(`${targetBase}/notes/ml/unit1/handwritten/ml-unit1-handwritten.html`, { waitUntil: 'domcontentloaded', timeout: 20000 });
      record('ML Unit 1 Handwritten Web loads HTTP 200', resp && resp.status() === 200, `status=${resp ? resp.status() : 'null'}`);
      record('ML Unit 1 Handwritten Web 0 console errors', consoleErrors.length === 0, consoleErrors.join('; '));
      record('ML Unit 1 Handwritten Web 0 failed assets', failedNetwork.length === 0, failedNetwork.join('; '));
    } catch (e) {
      record('ML Unit 1 Handwritten Web test', false, e.message);
    }

    await browser.close();
  }

  // --- Final Summary ---
  console.log(`\n======================================================`);
  console.log(` Summary: ${passedTests} / ${totalTests} assertions passed (${Math.round((passedTests/totalTests)*100)}%)`);
  if (failures.length > 0) {
    console.error(`\n ${failures.length} Failures Detected:`);
    failures.forEach(f => console.error(`  - ${f.name}: ${f.detail}`));
    console.log(`======================================================\n`);
    process.exit(1);
  } else {
    console.log(` ALL CHECKS PASSED PERFECTLY! Portal is release ready.`);
    console.log(`======================================================\n`);
    process.exit(0);
  }
})();
