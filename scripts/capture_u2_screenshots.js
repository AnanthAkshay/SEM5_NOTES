const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/cn/unit2/unit-2-notes.html', { waitUntil: 'networkidle' });

  // 1. Sliding window
  const figSliding = page.locator('#fig-sliding-window');
  if (await figSliding.count() > 0) {
    await figSliding.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await figSliding.screenshot({ path: 'audit/scratch/cn_u2_sliding.png' });
  }

  // 2. CRC division
  const figCrc = page.locator('#fig-crc-division');
  if (await figCrc.count() > 0) {
    await figCrc.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await figCrc.screenshot({ path: 'audit/scratch/cn_u2_crc_fig.png' });
  }

  // 3. CRC explorer widget
  const crcExp = page.locator('#crc-explorer-widget');
  if (await crcExp.count() > 0) {
    await crcExp.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await crcExp.screenshot({ path: 'audit/scratch/cn_u2_crc_widget.png' });
  }

  await browser.close();
  console.log('CN Unit 2 all screenshots captured.');
})();
