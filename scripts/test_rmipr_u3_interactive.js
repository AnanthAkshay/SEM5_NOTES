const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/rmipr/unit3/unit-3-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log('Testing RMIPR Unit 3 Interactive Statistical Studio...');
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

  // 1. Initial Z-test (Passenger first class: Z = -1.2500)
  const initZ = await page.textContent('#res-z-stat');
  const initVerdict = await page.textContent('#res-z-verdict');
  console.log('Initial Z-test state:', { initZ, initVerdict });

  if (initZ.trim() !== '-1.2500' || !initVerdict.includes('FAIL TO REJECT')) {
    throw new Error(`Expected Z = -1.2500 and Fail to Reject; got Z=${initZ}, verdict=${initVerdict}`);
  }

  // 2. Click Zoo trip preset
  await page.click('#preset-zoo');
  await page.waitForTimeout(100);

  const zooZ = await page.textContent('#res-z-stat');
  console.log('Zoo trip Z-stat:', zooZ);
  if (!zooZ.includes('-1.386')) {
    throw new Error(`Expected Z ~ -1.3862, got ${zooZ}`);
  }

  // 3. Click Labor turnover preset
  await page.click('#preset-turnover');
  await page.waitForTimeout(100);

  const turnoverZ = await page.textContent('#res-z-stat');
  console.log('Labor turnover Z-stat:', turnoverZ);
  if (!turnoverZ.includes('-0.6711')) {
    throw new Error(`Expected Z = -0.6711, got ${turnoverZ}`);
  }

  // 4. Tab switch to Student's t-test
  await page.click('#tab-btn-ttest');
  await page.waitForTimeout(100);

  const tVisible = await page.isVisible('#panel-ttest');
  const zVisible = await page.isVisible('#panel-ztest');
  console.log('Tab switch visibility:', { tVisible, zVisible });

  if (!tVisible || zVisible) {
    throw new Error('Tab switching failed');
  }

  // 5. Check Student's t-test result for 9 heights
  const tStat = await page.textContent('#res-t-stat');
  const tDf = await page.textContent('#res-t-df');
  const tVerdict = await page.textContent('#res-t-verdict');
  console.log('Student t-test result (9 heights):', { tStat, tDf, tVerdict });

  if (!tStat.includes('-1.5278') || !tDf.includes('8') || !tVerdict.includes('FAIL TO REJECT')) {
    throw new Error(`Expected t = -1.5278, df=8, and Fail to Reject; got t=${tStat}`);
  }

  console.log('RMIPR Unit 3 Interactive Statistical Studio verification PASSED perfectly!');
  await browser.close();
})();
