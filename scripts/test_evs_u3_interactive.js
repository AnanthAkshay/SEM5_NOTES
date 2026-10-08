const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/evs/unit3/unit-3-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log(`Starting EVS Unit 3 interactive test on: ${BASE_URL}`);
  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);

  // 1. Verify Academic Box exists
  const academicBox = await page.$('.academic-verification-box');
  console.log('Academic Verification Box exists:', !!academicBox);

  // 2. Scroll to interactive studio
  await page.evaluate(() => {
    const el = document.getElementById('evs-diversity-studio');
    if (el) el.scrollIntoView();
  });
  await page.waitForTimeout(300);

  // 3. Test Tab 1 Simpson's Index
  console.log('Testing Tab 1 Simpson\'s Index...');
  let dVal = await page.textContent('#res-simpson-d');
  let divVal = await page.textContent('#res-simpson-1minusd');
  let recipVal = await page.textContent('#res-simpson-reciprocal');
  console.log(`Initial Simpson metrics: D = ${dVal.trim()}, 1-D = ${divVal.trim()}, 1/D = ${recipVal.trim()}`);

  await page.click('#preset-equitable');
  divVal = await page.textContent('#res-simpson-1minusd');
  console.log('Diversity after Equitable Canopy preset:', divVal.trim());

  await page.click('#preset-forest-a');
  divVal = await page.textContent('#res-simpson-1minusd');
  console.log('Diversity re-checked with Solved Forest A:', divVal.trim());

  // 4. Test Tab 2 Shannon-Wiener Index
  console.log('Testing Tab 2 Shannon-Wiener...');
  await page.click('#tab-btn-shannon');
  await page.waitForTimeout(200);

  let hVal = await page.textContent('#res-shannon-h');
  let hMaxVal = await page.textContent('#res-shannon-hmax');
  let jVal = await page.textContent('#res-shannon-j');
  console.log(`Shannon H' = ${hVal.trim()}, H_max = ${hMaxVal.trim()}, Evenness J' = ${jVal.trim()}`);

  // 5. Test Exam Questions Details expansion
  const firstDetail = await page.$('details.exam-card');
  if (firstDetail) {
    await page.evaluate(el => el.setAttribute('open', 'true'), firstDetail);
    console.log('First authentic exam card opened successfully');
  }

  // 6. Screenshot interactive studio
  const studio = await page.$('#evs-diversity-studio');
  if (studio) {
    await studio.screenshot({ path: 'audit/scratch/evs_u3_studio.png' });
    console.log('Saved studio screenshot to audit/scratch/evs_u3_studio.png');
  }

  await browser.close();
  console.log('EVS Unit 3 interactive test completed successfully!');
})();
