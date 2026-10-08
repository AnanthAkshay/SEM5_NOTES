const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/se/unit2/unit-2-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log('Testing SE Unit 2 Interactive Explorer...');
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

  // 1. Initial Availability calculation
  const initAvail = await page.textContent('#res-avail-pct');
  const initDowntime = await page.textContent('#res-downtime');
  const initTier = await page.textContent('#res-sla-tier');

  console.log('Initial Availability state:', { initAvail, initDowntime, initTier });

  if (!initAvail.includes('99.602%')) {
    throw new Error(`Expected 99.602%, got ${initAvail}`);
  }

  // 2. Adjust MTBF to 1000 and MTTR to 1
  await page.$eval('#mtbf-slider', el => { el.value = 1000; el.dispatchEvent(new Event('input')); });
  await page.$eval('#mttr-slider', el => { el.value = 1; el.dispatchEvent(new Event('input')); });
  await page.waitForTimeout(100);

  const updatedAvail = await page.textContent('#res-avail-pct');
  const updatedDowntime = await page.textContent('#res-downtime');
  console.log('Updated Availability state (1000h / 1h):', { updatedAvail, updatedDowntime });

  if (!updatedAvail.includes('99.900%')) {
    throw new Error(`Expected 99.900%, got ${updatedAvail}`);
  }

  // 3. Reset button
  await page.click('#btn-reset-avail');
  await page.waitForTimeout(100);
  const resetAvail = await page.textContent('#res-avail-pct');
  console.log('Reset Availability state:', resetAvail);
  if (!resetAvail.includes('99.602%')) {
    throw new Error(`Reset failed, expected 99.602%, got ${resetAvail}`);
  }

  // 4. Tab switch to RTM
  await page.click('#tab-btn-rtm');
  await page.waitForTimeout(100);

  const rtmVisible = await page.isVisible('#panel-rtm');
  const availVisible = await page.isVisible('#panel-avail');
  console.log('Tab switch visibility:', { rtmVisible, availVisible });

  if (!rtmVisible || availVisible) {
    throw new Error('Tab switching failed');
  }

  // Check RTM rows
  const rowCount = await page.$$eval('#rtm-tbody tr', rows => rows.length);
  const initCoverage = await page.textContent('#rtm-coverage-badge');
  console.log('RTM initial table:', { rowCount, initCoverage });

  if (rowCount !== 6 || !initCoverage.includes('100.0%')) {
    throw new Error(`Expected 6 rows and 100.0% coverage, got ${rowCount} rows, ${initCoverage}`);
  }

  // Toggle first requirement
  await page.click('#rtm-tbody tr:first-child input[type="checkbox"]');
  await page.waitForTimeout(100);
  const toggledCoverage = await page.textContent('#rtm-coverage-badge');
  console.log('Toggled Coverage (1 unchecked):', toggledCoverage);
  if (!toggledCoverage.includes('83.3%')) {
    throw new Error(`Expected 83.3% coverage, got ${toggledCoverage}`);
  }

  // Check filter
  await page.click('#rtm-filter-support');
  await page.waitForTimeout(100);
  const supportRowCount = await page.$$eval('#rtm-tbody tr', rows => rows.length);
  console.log('Support filter row count:', supportRowCount);
  if (supportRowCount !== 2) {
    throw new Error(`Expected 2 support rows, got ${supportRowCount}`);
  }

  console.log('SE Unit 2 Interactive Explorer verification PASSED perfectly!');
  await browser.close();
})();
