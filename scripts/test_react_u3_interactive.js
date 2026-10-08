const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/reactjs/unit3/unit-3-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log(`Starting ReactJS Unit 3 interactive test on: ${BASE_URL}`);
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
    const el = document.getElementById('react-forms-studio');
    if (el) el.scrollIntoView();
  });
  await page.waitForTimeout(300);

  // 3. Test Multi-Field Form
  console.log('Testing Multi-Field Form...');
  await page.fill('#form-input-name', 'Rohan Verma');
  let stateJson = await page.textContent('#view-form-state-json');
  console.log('State updated with Rohan Verma:', stateJson.includes('Rohan Verma'));

  await page.click('#btn-submit-form');
  let feedbackText = await page.textContent('#submit-feedback');
  console.log('Submit feedback visible:', feedbackText.includes('preventDefault'));

  // 4. Test Tab 2 Lifting State Up
  console.log('Testing Tab 2 Lifting State Up...');
  await page.click('#tab-btn-lifting');
  await page.waitForTimeout(200);

  // Click Boiling Point preset
  await page.click('#preset-boiling');
  let cVal = await page.inputValue('#temp-input-c');
  let fVal = await page.inputValue('#temp-input-f');
  let verdict = await page.textContent('#boiling-text');
  console.log(`Boiling preset values: ${cVal}°C, ${fVal}°F. Verdict: ${verdict.trim()}`);

  // Click Freezing Point preset
  await page.click('#preset-freezing');
  cVal = await page.inputValue('#temp-input-c');
  fVal = await page.inputValue('#temp-input-f');
  verdict = await page.textContent('#boiling-text');
  console.log(`Freezing preset values: ${cVal}°C, ${fVal}°F. Verdict: ${verdict.trim()}`);

  // 5. Screenshot interactive studio
  const studio = await page.$('#react-forms-studio');
  if (studio) {
    await studio.screenshot({ path: 'audit/scratch/react_u3_studio.png' });
    console.log('Saved studio screenshot to audit/scratch/react_u3_studio.png');
  }

  await browser.close();
  console.log('ReactJS Unit 3 interactive test completed successfully!');
})();
