const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/rmipr/unit2/unit-2-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log('Testing RMIPR Unit 2 Interactive Experimental Studio...');
  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true
  });

  const page = await browser.newPage();
  const consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });

  await page.goto(BASE_URL, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  // 1. Initial Sample Size check (Proportion: n = 385)
  const initN = await page.textContent('#res-sample-n');
  const initFormula = await page.textContent('#res-sample-formula');
  console.log('Initial Proportion Sample Size:', { initN, initFormula });

  if (initN.trim() !== '385') {
    throw new Error(`Expected n=385, got ${initN}`);
  }

  // 2. Switch to Mean Mode
  await page.click('#subtab-mean');
  await page.waitForTimeout(100);

  const meanN = await page.textContent('#res-sample-n');
  const meanFormula = await page.textContent('#res-sample-formula');
  console.log('Mean Mode Sample Size (sigma=15, E=3, 99%):', { meanN, meanFormula });

  if (meanN.trim() !== '166') {
    throw new Error(`Expected n=166, got ${meanN}`);
  }

  // 3. Tab switch to Latin Square
  await page.click('#tab-btn-lsd');
  await page.waitForTimeout(100);

  const lsdVisible = await page.isVisible('#panel-lsd');
  const sampleVisible = await page.isVisible('#panel-samplesize');
  console.log('Tab switch visibility:', { lsdVisible, sampleVisible });

  if (!lsdVisible || sampleVisible) {
    throw new Error('Tab switching failed');
  }

  // Check 4x4 initial LSD cells
  let cellCount = await page.$$eval('#lsd-matrix-grid div', cells => cells.length);
  let dfRows = await page.textContent('#lsd-df-tbody');
  console.log('4x4 LSD cells:', cellCount, 'df contents:', dfRows.includes('6'));

  if (cellCount !== 16 || !dfRows.includes('6') || !dfRows.includes('15')) {
    throw new Error(`Expected 16 cells and df_error=6, got ${cellCount} cells`);
  }

  // Switch to 5x5
  await page.click('#lsd-m-5');
  await page.waitForTimeout(100);
  cellCount = await page.$$eval('#lsd-matrix-grid div', cells => cells.length);
  dfRows = await page.textContent('#lsd-df-tbody');
  console.log('5x5 LSD cells:', cellCount, 'df_error=12:', dfRows.includes('12'));

  if (cellCount !== 25 || !dfRows.includes('12') || !dfRows.includes('24')) {
    throw new Error(`Expected 25 cells and df_error=12, got ${cellCount} cells`);
  }

  console.log('RMIPR Unit 2 Interactive Experimental Studio verification PASSED perfectly!');
  await browser.close();
})();
