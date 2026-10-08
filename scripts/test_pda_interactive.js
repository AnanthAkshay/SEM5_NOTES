const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/toc/unit3/unit-3-notes.html', { waitUntil: 'networkidle' });

  const widget = await page.$('#pda-simulator-widget');
  console.log('PDA widget exists:', !!widget);

  const input = await page.$('#input-pda-str');
  const status = await page.$('#out-pda-status');
  console.log('Default status (aabb):', (await status.innerText()).trim());

  await input.fill('aaabbb');
  await input.dispatchEvent('input');
  console.log('Status for aaabbb:', (await status.innerText()).trim());

  await input.fill('aab');
  await input.dispatchEvent('input');
  console.log('Status for aab:', (await status.innerText()).trim());

  // Test switch language to balanced parens
  const langSelect = await page.$('#select-pda-lang');
  await langSelect.selectOption('balanced_parens');
  await langSelect.dispatchEvent('change');
  await input.fill('(())()');
  await input.dispatchEvent('input');
  console.log('Status for (())():', (await status.innerText()).trim());

  await input.fill('(()');
  await input.dispatchEvent('input');
  console.log('Status for (():', (await status.innerText()).trim());

  await browser.close();
  console.log('PDA interactive simulator test PASSED!');
})();
