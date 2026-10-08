const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/ml/unit1/unit-1-notes.html', { waitUntil: 'networkidle' });

  const widget = await page.$('#cm-explorer-widget');
  console.log('CM widget exists:', !!widget);
  await widget.scrollIntoViewIfNeeded();

  const acc = await page.$('#out-cm-acc');
  const prec = await page.$('#out-cm-prec');
  const rec = await page.$('#out-cm-rec');
  const f1 = await page.$('#out-cm-f1');
  console.log('Default Accuracy (CIE-1):', (await acc.textContent()).trim());
  console.log('Default Precision:', (await prec.textContent()).trim());
  console.log('Default Recall:', (await rec.textContent()).trim());
  console.log('Default F1-Score:', (await f1.textContent()).trim());

  // Test switching to SEE 2026 preset
  const preset = await page.$('#select-cm-preset');
  await preset.selectOption('see2026');
  await preset.dispatchEvent('change');
  console.log('SEE 2026 Accuracy:', (await acc.textContent()).trim());
  console.log('SEE 2026 Precision:', (await prec.textContent()).trim());
  console.log('SEE 2026 Recall:', (await rec.textContent()).trim());
  console.log('SEE 2026 F1-Score:', (await f1.textContent()).trim());

  // Test custom input
  const inTP = await page.$('#input-cm-tp');
  await inTP.fill('100');
  await inTP.dispatchEvent('input');
  console.log('Custom (TP=100) Accuracy:', (await acc.textContent()).trim());

  await browser.close();
  console.log('Confusion Matrix interactive widget test PASSED!');
})();
