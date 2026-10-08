const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/toc/unit2/unit-2-notes.html', { waitUntil: 'networkidle' });

  // 1. Thompson NFA in Section 2
  await page.evaluate(() => {
    const s = document.getElementById('sec-2');
    if (s) s.scrollIntoView();
  });
  await page.waitForTimeout(500);
  const figThomp = page.locator('#fig-thompson-nfa');
  await figThomp.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await figThomp.screenshot({ path: 'audit/scratch/toc_u2_thompson_desktop.png' });

  // 2. 6-State Minimized DFA in Section 7
  await page.evaluate(() => {
    const s = document.getElementById('sec-7');
    if (s) s.scrollIntoView();
  });
  await page.waitForTimeout(500);
  const figMin = page.locator('#fig-cie1-min-dfa');
  await figMin.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await figMin.screenshot({ path: 'audit/scratch/toc_u2_min_dfa_desktop.png' });

  // 3. Interactive Minimizer Widget
  const widget = page.locator('#dfa-minimizer-widget');
  await widget.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await widget.screenshot({ path: 'audit/scratch/toc_u2_widget_desktop.png' });

  await browser.close();
  console.log('TOC Unit 2 screenshots captured.');
})();
