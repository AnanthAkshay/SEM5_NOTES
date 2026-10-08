const { chromium } = require('playwright');
const path = require('path');

const pagePath = process.argv[2] || 'notes/cn/unit1/unit-1-notes.html';
const BASE_URL = 'http://localhost:8088/SEM5_NOTES/' + pagePath;
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log(`Testing page: ${BASE_URL}`);
  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true
  });

  const page = await browser.newPage();
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });

  page.on('requestfailed', req => {
    console.log('Request failed:', req.url(), req.failure() ? req.failure().errorText : '');
  });
  const failedReqs = [];
  page.on('response', resp => {
    if (resp.status() >= 400) {
      console.log(`HTTP ${resp.status()}: ${resp.url()}`);
      failedReqs.push({ status: resp.status(), url: resp.url() });
    }
  });

  // Test desktop (1280px)
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  // Check horizontal overflow
  const desktopOverflow = await page.evaluate(() => {
    return document.documentElement.scrollWidth > window.innerWidth;
  });
  console.log(`Desktop 1280px overflow: ${desktopOverflow}`);

  // Test mobile viewports: 768px, 390px, 320px
  for (const w of [768, 390, 320]) {
    await page.setViewportSize({ width: w, height: 800 });
    await page.waitForTimeout(200);
    const overflow = await page.evaluate(() => {
      return document.documentElement.scrollWidth > window.innerWidth;
    });
    console.log(`Mobile ${w}px overflow: ${overflow}`);

    if (w === 320 && overflow) {
      const overElements = await page.evaluate(() => {
        const list = [];
        const winW = window.innerWidth;
        document.querySelectorAll('*').forEach(el => {
          const rect = el.getBoundingClientRect();
          if (rect.right > winW + 1) {
            list.push({
              tag: el.tagName,
              id: el.id,
              className: el.className,
              width: Math.round(rect.width),
              right: Math.round(rect.right)
            });
          }
        });
        return list.slice(0, 8);
      });
      console.log('Overflow elements at 320px:', overElements);
    }
  }

  if (failedReqs.length > 0) {
    console.log('Failed requests (>= 400):', failedReqs);
  }

  // Check KaTeX math rendered
  const katexCount = await page.evaluate(() => {
    return document.querySelectorAll('.katex').length;
  });
  console.log(`KaTeX elements rendered: ${katexCount}`);

  // Check SVG diagrams count
  const svgCount = await page.evaluate(() => {
    return document.querySelectorAll('svg').length;
  });
  console.log(`SVGs rendered: ${svgCount}`);

  // Check Interactive Explorer slider
  await page.setViewportSize({ width: 1280, height: 900 });
  const sliderExists = await page.evaluate(() => {
    const s = document.getElementById('slider-dist');
    return s !== null;
  });
  console.log(`Interactive slider exists: ${sliderExists}`);

  console.log(`Console errors: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    console.error('Console errors:', consoleErrors);
  }

  // Take screenshot of desktop and mobile
  await page.screenshot({ path: 'audit/scratch/cn_u1_desktop.png', fullPage: false });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: 'audit/scratch/cn_u1_mobile.png', fullPage: false });
  console.log('Screenshots saved to audit/scratch/');

  await browser.close();
  console.log('Single page test complete.');
})();
