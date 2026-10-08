const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/rmipr/unit1/unit-1-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log('Testing RMIPR Unit 1 Interactive Bibliometrics Studio...');
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

  // 1. Initial h-index check (Dr. Sharma)
  const initH = await page.textContent('#res-h-index');
  const initI10 = await page.textContent('#res-i10-index');
  const initTotal = await page.textContent('#res-total-papers');
  console.log('Initial h-index state:', { initH, initI10, initTotal });

  if (initH.trim() !== '7' || initI10.trim() !== '5' || initTotal.trim() !== '10') {
    throw new Error(`Expected h=7, i10=5, papers=10; got h=${initH}, i10=${initI10}, papers=${initTotal}`);
  }

  // 2. Click preset: Senior Scholar (12 papers, h=8)
  await page.click('#preset-senior');
  await page.waitForTimeout(100);

  const seniorH = await page.textContent('#res-h-index');
  const seniorI10 = await page.textContent('#res-i10-index');
  const seniorTotal = await page.textContent('#res-total-papers');
  console.log('Senior Scholar preset:', { seniorH, seniorI10, seniorTotal });

  if (seniorH.trim() !== '8' || seniorI10.trim() !== '7' || seniorTotal.trim() !== '12') {
    throw new Error(`Expected h=8, i10=7, papers=12; got h=${seniorH}, i10=${seniorI10}`);
  }

  // 3. Tab switch to JIF
  await page.click('#tab-btn-jif');
  await page.waitForTimeout(100);

  const jifVisible = await page.isVisible('#panel-jif');
  const hindexVisible = await page.isVisible('#panel-hindex');
  console.log('Tab switch visibility:', { jifVisible, hindexVisible });

  if (!jifVisible || hindexVisible) {
    throw new Error('Tab switching failed');
  }

  const initJIF = await page.textContent('#res-jif-val');
  const initQuartile = await page.textContent('#res-jif-quartile');
  console.log('Initial JIF state:', { initJIF, initQuartile });

  if (initJIF.trim() !== '5.500') {
    throw new Error(`Expected JIF 5.500, got ${initJIF}`);
  }

  // 4. Modify JIF inputs
  await page.$eval('#jif-cites-prev1', el => { el.value = 800; el.dispatchEvent(new Event('input')); });
  await page.waitForTimeout(100);
  const updatedJIF = await page.textContent('#res-jif-val');
  console.log('Updated JIF (cites 800+650 / 260):', updatedJIF);

  // 5. Reset JIF
  await page.click('#btn-reset-jif');
  await page.waitForTimeout(100);
  const resetJIF = await page.textContent('#res-jif-val');
  console.log('Reset JIF:', resetJIF);
  if (resetJIF.trim() !== '5.500') {
    throw new Error(`Expected reset JIF 5.500, got ${resetJIF}`);
  }

  console.log('RMIPR Unit 1 Interactive Bibliometrics Studio verification PASSED perfectly!');
  await browser.close();
})();
