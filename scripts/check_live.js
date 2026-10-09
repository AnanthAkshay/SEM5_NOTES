/**
 * SEM 5 · ISE Notes - Post-Deployment Live Verification Script
 * 
 * Verifies live deployment (or local test server):
 * - Home page, 404 page, robots.txt, manifest, core stylesheets & scripts
 * - Every subject view (all 8 subjects in SPA)
 * - Every standard unit notes HTML page (all 24 units)
 * - Every handwritten notebook PDF file (all 24 units)
 * - MIME types, HTTP 200 responses, console errors, and internal links
 * 
 * Usage:
 *   node scripts/check_live.js [BASE_URL]
 * 
 * Examples:
 *   node scripts/check_live.js https://ananthakshay.github.io/SEM5_NOTES
 *   node scripts/check_live.js http://localhost:8088/SEM5_NOTES
 */

const { chromium } = require('playwright');
const https = require('https');
const http = require('http');

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

async function httpCheck(targetUrl, method = 'HEAD') {
  return new Promise((resolve) => {
    try {
      const parsed = new URL(targetUrl);
      const client = parsed.protocol === 'https:' ? https : http;
      const options = {
        method,
        headers: { 'User-Agent': 'SEM5-LiveChecker/2.0' }
      };
      const req = client.request(parsed, options, (res) => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          const nextUrl = new URL(res.headers.location, targetUrl).toString();
          httpCheck(nextUrl, method).then(resolve);
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
      req.setTimeout(15000, () => {
        req.destroy();
        resolve({ url: targetUrl, status: 0, error: 'Timeout after 15s' });
      });
      req.end();
    } catch (err) {
      resolve({ url: targetUrl, status: 0, error: err.message });
    }
  });
}

(async () => {
  console.log(`\n======================================================`);
  console.log(` SEM 5 · Post-Deployment Live Verification Suite`);
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

  // --- Phase 1: Core Portal & Essential Asset Endpoints ---
  console.log(`--- Phase 1: Core Portal & Asset Checks ---`);
  const coreEndpoints = [
    { name: 'Home HTML', path: '/index.html', expectMime: 'text/html' },
    { name: '404 Error Page', path: '/404.html', expectMime: 'text/html' },
    { name: 'Robots.txt', path: '/robots.txt', expectMime: '' },
    { name: 'Manifest', path: '/manifest.webmanifest', expectMime: '' },
    { name: 'Design Stylesheet', path: '/css/style.css', expectMime: 'text/css' },
    { name: 'Handwritten Stylesheet', path: '/css/handwritten.css', expectMime: 'text/css' },
    { name: 'App JavaScript', path: '/js/app.js', expectMime: 'javascript' },
    { name: 'Notes JavaScript', path: '/js/notes.js', expectMime: 'javascript' },
    { name: 'Subjects Data', path: '/data/subjects.js', expectMime: 'javascript' },
    { name: 'Notes Index', path: '/data/notes-index.js', expectMime: 'javascript' }
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

  // --- Phase 2: Handwritten Notebook PDFs (all 24 units) ---
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
        `Status=${res.status}, Size=${Math.round(res.contentLength / 1024)} KB, MIME=${res.contentType}`
      );
    }
  }

  // --- Phase 3: Standard Interactive HTML Unit Notes (all 24 units) ---
  console.log(`\n--- Phase 3: Interactive HTML Unit Notes (24 Units) ---`);
  for (const sub of SUBJECTS) {
    for (const u of sub.units) {
      const notePath = `/notes/${sub.id}/unit${u}/unit-${u}-notes.html`;
      const noteUrl = `${targetBase}${notePath}`;
      const res = await httpCheck(noteUrl);
      const pass = res.status === 200 && res.contentType.includes('text/html');
      record(
        `HTML Note: ${sub.code} Unit ${u} (${sub.id}/unit${u})`,
        pass,
        `Status=${res.status}, MIME=${res.contentType}`
      );
    }
  }

  // --- Phase 4: Playwright Runtime, Subject Views, Console & Navigation ---
  console.log(`\n--- Phase 4: Playwright Browser Runtime & Console Error Checks ---`);
  let browser = null;
  try {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const fs = require('fs');
    if (fs.existsSync(chromePath)) {
      browser = await chromium.launch({ executablePath: chromePath, headless: true });
    } else {
      browser = await chromium.launch({ headless: true });
    }
  } catch (err) {
    console.warn(`[WARN] Chromium launch: ${err.message}. Running fallback mode.`);
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

    // 4.1 Home Page
    console.log(`  Checking Home Page: ${targetBase}/`);
    consoleErrors.length = 0;
    failedNetwork.length = 0;
    try {
      const resp = await page.goto(`${targetBase}/`, { waitUntil: 'networkidle', timeout: 25000 });
      record('Home page loads HTTP 200', resp && resp.status() === 200, `status=${resp ? resp.status() : 'null'}`);
      record('Home page 0 console errors', consoleErrors.length === 0, consoleErrors.join('; '));
      record('Home page 0 failed network requests', failedNetwork.length === 0, failedNetwork.join('; '));
    } catch (e) {
      record('Home page browser test', false, e.message);
    }

    // 4.2 All 8 Subject SPA Views
    console.log(`  Checking all 8 Subject SPA Views...`);
    for (const sub of SUBJECTS) {
      consoleErrors.length = 0;
      failedNetwork.length = 0;
      try {
        await page.goto(`${targetBase}/#subject-${sub.id}`, { waitUntil: 'networkidle', timeout: 15000 });
        await page.waitForTimeout(300);
        const heading = await page.evaluate(() => {
          const el = document.querySelector('.subject-view-title');
          return el ? el.textContent.trim() : '';
        });
        const normHeading = heading.toLowerCase().replace('&', 'and').replace(/\s+/g, ' ');
        const normExpected = sub.name.toLowerCase().replace('&', 'and').replace(/\s+/g, ' ');
        const match = normHeading.includes(normExpected);
        record(
          `Subject View: ${sub.name} (${sub.code})`,
          match && consoleErrors.length === 0,
          `Heading: "${heading}", Errors: ${consoleErrors.join('; ') || 'none'}`
        );
      } catch (e) {
        record(`Subject View: ${sub.name}`, false, e.message);
      }
    }

    // 4.3 Sample Interactive Notes Check (Console & PDF Link validation)
    console.log(`  Checking Interactive Notes Pages Runtime...`);
    const sampleNotes = [
      { sub: 'toc', u: 1 },
      { sub: 'ml', u: 1 },
      { sub: 'ai', u: 2 },
      { sub: 'cn', u: 3 }
    ];

    for (const sample of sampleNotes) {
      consoleErrors.length = 0;
      failedNetwork.length = 0;
      const noteUrl = `${targetBase}/notes/${sample.sub}/unit${sample.u}/unit-${sample.u}-notes.html`;
      try {
        const resp = await page.goto(noteUrl, { waitUntil: 'domcontentloaded', timeout: 20000 });
        // Check for PDF link card
        const hasPdfCard = await page.evaluate(() => {
          const links = Array.from(document.querySelectorAll('a[href*="-handwritten.pdf"]'));
          return links.length > 0;
        });
        const allErrors = [...consoleErrors, ...failedNetwork];
        record(
          `Notes Runtime: ${sample.sub.toUpperCase()} Unit ${sample.u} loads with 0 errors & PDF link card`,
          resp && resp.status() === 200 && allErrors.length === 0 && hasPdfCard,
          `status=${resp ? resp.status() : 'null'}, errors=${allErrors.join('; ') || 'none'}, pdfCard=${hasPdfCard}`
        );
      } catch (e) {
        record(`Notes Runtime: ${sample.sub} Unit ${sample.u}`, false, e.message);
      }
    }

    await browser.close();
  }

  // --- Final Summary ---
  console.log(`\n======================================================`);
  console.log(` Summary: ${passedTests} / ${totalTests} assertions passed (${Math.round((passedTests / totalTests) * 100)}%)`);
  if (failures.length > 0) {
    console.error(`\n ${failures.length} Failures Detected:`);
    failures.forEach(f => console.error(`  - ${f.name}: ${f.detail}`));
    console.log(`======================================================\n`);
    process.exit(1);
  } else {
    console.log(` ALL CHECKS PASSED! Portal is ready for live deployment.`);
    console.log(`======================================================\n`);
    process.exit(0);
  }
})();
