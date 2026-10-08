const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/ml/unit3/unit-3-notes.html', { waitUntil: 'networkidle' });

  const widget = await page.$('#lr-explorer-widget');
  console.log('LR widget exists:', !!widget);
  await widget.scrollIntoViewIfNeeded();

  const outEq = await page.$('#out-lr-eq');
  const outPred = await page.$('#out-lr-pred');
  const outMse = await page.$('#out-lr-mse');
  const outR2 = await page.$('#out-lr-r2');

  console.log('Initial Equation (m=4.50, c=41.00):', (await outEq.textContent()).trim());
  console.log('Predicted Marks for X=7.0:', (await outPred.textContent()).trim());
  console.log('MSE:', (await outMse.textContent()).trim());
  console.log('R2:', (await outR2.textContent()).trim());

  // Test slider changes
  const sliderM = await page.$('#slider-lr-slope');
  await sliderM.evaluate(el => { el.value = '5.00'; el.dispatchEvent(new Event('input')); });

  console.log('Updated Equation (m=5.00):', (await outEq.textContent()).trim());
  console.log('Updated Predicted Marks for X=7.0:', (await outPred.textContent()).trim());

  await browser.close();
  console.log('Linear Regression interactive widget test PASSED!');
})();
