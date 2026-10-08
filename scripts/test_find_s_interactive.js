const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/ml/unit2/unit-2-notes.html', { waitUntil: 'networkidle' });

  const widget = await page.$('#find-s-simulator-widget');
  console.log('Find-S widget exists:', !!widget);
  await widget.scrollIntoViewIfNeeded();

  const outS = await page.$('#out-cl-s');
  const btnNext = await page.$('#btn-cl-next');
  console.log('Initial S0:', (await outS.textContent()).trim());

  // Step 1: Sample 1 (No)
  await btnNext.click();
  console.log('After Step 1 (Sample 1 No):', (await outS.textContent()).trim());

  // Step 2: Sample 2 (No)
  await btnNext.click();
  console.log('After Step 2 (Sample 2 No):', (await outS.textContent()).trim());

  // Step 3: Sample 3 (Yes) -> S1
  await btnNext.click();
  console.log('After Step 3 (Sample 3 Yes):', (await outS.textContent()).trim());

  // Step 4: Sample 4 (Yes) -> S2
  await btnNext.click();
  console.log('After Step 4 (Sample 4 Yes):', (await outS.textContent()).trim());

  // Step through remaining samples to final S
  for (let i = 5; i <= 10; i++) {
    await btnNext.click();
  }
  console.log('Final S after 10 samples:', (await outS.textContent()).trim());

  await browser.close();
  console.log('Find-S interactive stepper test PASSED!');
})();
