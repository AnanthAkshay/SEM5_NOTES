const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/toc/unit1/unit-1-notes.html', { waitUntil: 'networkidle' });

  // Scroll section 3 into view first
  await page.evaluate(() => {
    const sec = document.getElementById('sec-dfa-design');
    if (sec) sec.scrollIntoView();
  });
  await page.waitForTimeout(600);

  // 1. DFA ends in 01
  const fig1 = page.locator('#fig-dfa-ends-01');
  await fig1.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await fig1.screenshot({ path: 'audit/scratch/toc_u1_dfa_ends_01_desktop.png' });

  // 2. Parity DFA
  const fig2 = page.locator('#fig-parity-dfa');
  await fig2.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await fig2.screenshot({ path: 'audit/scratch/toc_u1_parity_dfa_desktop.png' });

  // 3. Interactive simulator
  const sim = page.locator('#dfa-simulator-widget');
  await sim.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await sim.screenshot({ path: 'audit/scratch/toc_u1_simulator_desktop.png' });

  await browser.close();
  console.log('TOC Unit 1 screenshots captured properly.');
})();
