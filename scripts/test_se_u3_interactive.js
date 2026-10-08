const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/se/unit3/unit-3-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log('Testing SE Unit 3 Interactive Patterns Studio...');
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

  // 1. Observer Pattern publish
  await page.click('#btn-publish-weather');
  await page.waitForTimeout(100);

  let logText = await page.textContent('#observer-log');
  console.log('Initial broadcast log contains PhoneDisplay:', logText.includes('PhoneDisplay'));
  if (!logText.includes('PhoneDisplay') || !logText.includes('WindowDisplay')) {
    throw new Error('Observer publish failed to notify attached observers');
  }

  // 2. Heat wave emergency alert test
  await page.check('#obs-alert');
  await page.$eval('#temp-slider', el => { el.value = 40; el.dispatchEvent(new Event('input')); });
  await page.click('#btn-publish-weather');
  await page.waitForTimeout(100);

  logText = await page.textContent('#observer-log');
  console.log('Emergency alert triggered in log:', logText.includes('Heat wave alert'));
  if (!logText.includes('Heat wave alert')) {
    throw new Error('Emergency alert failed to trigger on >=38C');
  }

  // 3. Tab switch to Singleton
  await page.click('#tab-btn-singleton');
  await page.waitForTimeout(100);

  const singleVisible = await page.isVisible('#panel-singleton');
  const obsVisible = await page.isVisible('#panel-observer');
  console.log('Tab switch visibility:', { singleVisible, obsVisible });
  if (!singleVisible || obsVisible) {
    throw new Error('Tab switching failed');
  }

  // 4. Acquire Connection
  await page.click('#btn-borrow-conn');
  await page.waitForTimeout(100);
  let poolState = await page.textContent('#pool-active-count');
  console.log('Pool state after 1 acquire:', poolState);
  if (!poolState.includes('9 / 10 Free')) {
    throw new Error(`Expected '9 / 10 Free', got ${poolState}`);
  }

  // 5. Release Connection
  await page.click('#btn-release-conn');
  await page.waitForTimeout(100);
  poolState = await page.textContent('#pool-active-count');
  console.log('Pool state after release:', poolState);
  if (!poolState.includes('10 / 10 Free')) {
    throw new Error(`Expected '10 / 10 Free', got ${poolState}`);
  }

  // 6. Assert poolA === poolB
  await page.click('#btn-verify-singleton');
  await page.waitForTimeout(100);
  const singleLog = await page.textContent('#singleton-log');
  console.log('Singleton assert logged:', singleLog.includes('assert (poolA === poolB) is TRUE'));
  if (!singleLog.includes('assert (poolA === poolB) is TRUE')) {
    throw new Error('Singleton identity assertion failed');
  }

  console.log('SE Unit 3 Interactive Patterns Studio verification PASSED perfectly!');
  await browser.close();
})();
