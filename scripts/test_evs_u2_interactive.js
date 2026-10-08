const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/evs/unit2/unit-2-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log(`Starting EVS Unit 2 interactive test on: ${BASE_URL}`);
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
    const el = document.getElementById('evs-conservation-studio');
    if (el) el.scrollIntoView();
  });
  await page.waitForTimeout(300);

  // 3. Test Tab 1 Rainwater Harvesting
  console.log('Testing Tab 1 Rainwater Harvesting...');
  let litresVal = await page.textContent('#res-rain-litres');
  console.log('Initial harvested litres:', litresVal.trim());

  await page.fill('#input-roof-area', '200');
  litresVal = await page.textContent('#res-rain-litres');
  console.log('Litres after increasing area to 200 m²:', litresVal.trim());

  await page.selectOption('#select-roof-coeff', '0.90');
  litresVal = await page.textContent('#res-rain-litres');
  console.log('Litres with metal roof (C = 0.90):', litresVal.trim());

  // 4. Test Tab 2 Solar PV & Carbon Offset
  console.log('Testing Tab 2 Solar PV & Carbon...');
  await page.click('#tab-btn-solar');
  await page.waitForTimeout(200);

  let solarKwh = await page.textContent('#res-solar-kwh');
  let offsetKg = await page.textContent('#res-solar-offset-kg');
  console.log(`Solar generation: ${solarKwh.trim()}, Carbon offset: ${offsetKg.trim()}`);

  // 5. Test Exam Questions Details expansion
  const firstDetail = await page.$('details.exam-card');
  if (firstDetail) {
    await page.evaluate(el => el.setAttribute('open', 'true'), firstDetail);
    console.log('First authentic exam card opened successfully');
  }

  // 6. Screenshot interactive studio
  const studio = await page.$('#evs-conservation-studio');
  if (studio) {
    await studio.screenshot({ path: 'audit/scratch/evs_u2_studio.png' });
    console.log('Saved studio screenshot to audit/scratch/evs_u2_studio.png');
  }

  await browser.close();
  console.log('EVS Unit 2 interactive test completed successfully!');
})();
