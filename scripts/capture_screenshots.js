const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/cn/unit1/unit-1-notes.html', { waitUntil: 'networkidle' });

  // 1. Hero & Verification box
  const hero = page.locator('#hero');
  await hero.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await hero.screenshot({ path: 'audit/scratch/cn_u1_verif_box.png' });

  // 2. Cascaded DB diagram
  const figCascaded = page.locator('#fig-cascaded-db');
  if (await figCascaded.count() > 0) {
    await figCascaded.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await figCascaded.screenshot({ path: 'audit/scratch/cn_u1_cascaded_db.png' });
  }

  // 3. Latency breakdown diagram
  const figLatency = page.locator('#fig-latency-breakdown');
  if (await figLatency.count() > 0) {
    await figLatency.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await figLatency.screenshot({ path: 'audit/scratch/cn_u1_latency_fig.png' });
  }

  // 4. Interactive explorer
  const explorer = page.locator('#latency-explorer-widget');
  if (await explorer.count() > 0) {
    await explorer.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await explorer.screenshot({ path: 'audit/scratch/cn_u1_interactive.png' });
  }

  await browser.close();
  console.log('Targeted screenshots captured successfully.');
})();
