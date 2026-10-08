const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/reactjs/unit2/unit-2-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log(`Starting ReactJS Unit 2 interactive test on: ${BASE_URL}`);
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
    const el = document.getElementById('react-state-studio');
    if (el) el.scrollIntoView();
  });
  await page.waitForTimeout(300);

  // 3. Test Counter Controls
  console.log('Testing Counter Controls...');
  await page.click('#btn-count-inc');
  await page.click('#btn-count-inc');
  let countVal = await page.textContent('#counter-val');
  console.log('Count after two increments:', countVal.trim());

  await page.click('#btn-batch-fn');
  countVal = await page.textContent('#counter-val');
  console.log('Count after functional 3x batch:', countVal.trim());

  await page.click('#btn-count-5');
  countVal = await page.textContent('#counter-val');
  console.log('Count after Set 5:', countVal.trim());

  // 4. Test Immutable Object State
  console.log('Testing Object Immutability...');
  await page.click('#btn-user-bday');
  let userJson = await page.textContent('#view-user-json');
  console.log('User JSON after birthday:', userJson.includes('"age": 21'));

  // 5. Test Tab 2 Children Composition
  console.log('Testing Tab 2 Children Composition...');
  await page.click('#tab-btn-children');
  await page.waitForTimeout(200);

  await page.fill('#input-modal-title', 'Elective Choice');
  let renderedTitle = await page.textContent('#modal-rendered-title');
  console.log('Rendered modal title:', renderedTitle.trim());

  await page.click('input[value="badge"]');
  let renderedBody = await page.textContent('#modal-rendered-body');
  console.log('Rendered modal body with badge:', renderedBody.includes('Rohan'));

  // 6. Screenshot interactive studio
  const studio = await page.$('#react-state-studio');
  if (studio) {
    await studio.screenshot({ path: 'audit/scratch/react_u2_studio.png' });
    console.log('Saved studio screenshot to audit/scratch/react_u2_studio.png');
  }

  await browser.close();
  console.log('ReactJS Unit 2 interactive test completed successfully!');
})();
