const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/evs/unit1/unit-1-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log(`Starting EVS Unit 1 interactive test on: ${BASE_URL}`);
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
    const el = document.getElementById('evs-energy-studio');
    if (el) el.scrollIntoView();
  });
  await page.waitForTimeout(300);

  // 3. Test Tab 1 Presets
  console.log('Testing Tab 1 Presets...');
  await page.click('#preset-forest');
  let t1Val = await page.textContent('#tier-1-val');
  let t4Val = await page.textContent('#tier-4-val');
  console.log(`Forest preset T1: ${t1Val.trim()}, T4: ${t4Val.trim()}`);

  await page.click('#preset-desert');
  t1Val = await page.textContent('#tier-1-val');
  t4Val = await page.textContent('#tier-4-val');
  console.log(`Desert preset T1: ${t1Val.trim()}, T4: ${t4Val.trim()}`);

  await page.click('#preset-grassland');
  t1Val = await page.textContent('#tier-1-val');
  t4Val = await page.textContent('#tier-4-val');
  console.log(`Grassland preset T1: ${t1Val.trim()}, T4: ${t4Val.trim()}`);

  // 4. Test Tab 2 Switching & Calculations
  console.log('Testing Tab 2 Rule of 70 & Efficiency...');
  await page.click('#tab-btn-calc');
  await page.waitForTimeout(200);

  let doublingYears = await page.textContent('#res-doubling-years');
  console.log('Doubling years at r=1.75%:', doublingYears.trim());

  let trophicEff = await page.textContent('#res-trophic-eff');
  console.log('Trophic efficiency (132/1200):', trophicEff.trim());

  // 5. Test Exam Questions Details expansion
  const firstDetail = await page.$('details.exam-card');
  if (firstDetail) {
    await page.evaluate(el => el.setAttribute('open', 'true'), firstDetail);
    console.log('First authentic exam card opened successfully');
  }

  // 6. Screenshot interactive studio
  const studio = await page.$('#evs-energy-studio');
  if (studio) {
    await studio.screenshot({ path: 'audit/scratch/evs_u1_studio.png' });
    console.log('Saved studio screenshot to audit/scratch/evs_u1_studio.png');
  }

  await browser.close();
  console.log('EVS Unit 1 interactive test completed successfully!');
})();
