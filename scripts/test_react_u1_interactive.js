const { chromium } = require('playwright');
const path = require('path');

const BASE_URL = 'http://localhost:8088/SEM5_NOTES/notes/reactjs/unit1/unit-1-notes.html';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  console.log(`Starting ReactJS Unit 1 interactive test on: ${BASE_URL}`);
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

  // 2. Scroll to interactive widget
  await page.evaluate(() => {
    const el = document.getElementById('react-jsx-studio');
    if (el) el.scrollIntoView();
  });
  await page.waitForTimeout(300);

  // 3. Test Tab 1 Presets
  console.log('Testing Tab 1 Presets...');
  await page.click('#preset-cart');
  let jsxCode = await page.textContent('#view-jsx-source');
  console.log('Preset Cart JSX loaded:', jsxCode.includes('cart') || jsxCode.includes('Cart'));

  await page.click('#preset-list');
  jsxCode = await page.textContent('#view-jsx-source');
  console.log('Preset List JSX loaded:', jsxCode.includes('course.id'));

  await page.click('#preset-card');
  jsxCode = await page.textContent('#view-jsx-source');
  console.log('Preset Card JSX re-loaded:', jsxCode.includes('user.name'));

  // 4. Test Tab 2 Switching
  console.log('Testing Tab 2 Switching...');
  await page.click('#tab-btn-rendering');
  await page.waitForTimeout(200);

  // Check initial greeting
  let greeting = await page.textContent('#res-greeting-text');
  console.log('Initial greeting text:', greeting.trim());

  // Type new name
  await page.fill('#state-user-name', 'Rohan');
  greeting = await page.textContent('#res-greeting-text');
  console.log('Updated greeting with name Rohan:', greeting.trim());

  // Toggle logged in to false
  await page.click('#state-is-logged-in');
  greeting = await page.textContent('#res-greeting-text');
  console.log('Logged out greeting:', greeting.trim());

  // Toggle logged in back to true
  await page.click('#state-is-logged-in');
  greeting = await page.textContent('#res-greeting-text');
  console.log('Logged back in greeting:', greeting.trim());

  // Change filter to "high"
  await page.selectOption('#state-course-filter', 'high');
  let coursesCount = await page.textContent('#res-courses-count');
  console.log('Courses count after high filter:', coursesCount.trim());

  // 5. Test Exam Questions Details expansion
  const firstDetail = await page.$('details.exam-card');
  if (firstDetail) {
    await page.evaluate(el => el.setAttribute('open', 'true'), firstDetail);
    console.log('First exam card opened successfully');
  }

  // 6. Screenshot interactive studio
  const studio = await page.$('#react-jsx-studio');
  if (studio) {
    await studio.screenshot({ path: 'audit/scratch/react_u1_studio.png' });
    console.log('Saved studio screenshot to audit/scratch/react_u1_studio.png');
  }

  await browser.close();
  console.log('ReactJS Unit 1 interactive test completed successfully!');
})();
