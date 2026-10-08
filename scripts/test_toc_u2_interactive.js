const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/toc/unit2/unit-2-notes.html');

  // Verify initial state: Step 0
  const initDesc = await page.$eval('#lbl-min-step-desc', el => el.textContent.trim());
  const initClasses = await page.$eval('#out-min-classes', el => el.textContent.trim());
  console.log('Minimizer Initial State:', { initDesc, initClasses });

  // Step 1: Base mark
  await page.click('#btn-min-step');
  const baseDesc = await page.$eval('#lbl-min-step-desc', el => el.textContent.trim());
  const basePairs = await page.$eval('#out-base-pairs', el => el.textContent.trim());
  console.log('After Step 1:', { baseDesc, basePairs });
  if (!basePairs.includes('(A,D)')) throw new Error(`Expected (A,D) in base pairs, got ${basePairs}`);

  // Step 2: Inductive iteration
  await page.click('#btn-min-step');
  const indDesc = await page.$eval('#lbl-min-step-desc', el => el.textContent.trim());
  const indPairs = await page.$eval('#out-ind-pairs', el => el.textContent.trim());
  console.log('After Step 2:', { indDesc, indPairs });
  if (!indPairs.includes('(A,B)')) throw new Error(`Expected (A,B) in inductive pairs, got ${indPairs}`);

  // Step 3: Fixed point
  await page.click('#btn-min-step');
  const finalDesc = await page.$eval('#lbl-min-step-desc', el => el.textContent.trim());
  const finalClasses = await page.$eval('#out-min-classes', el => el.textContent.trim());
  console.log('After Step 3:', { finalDesc, finalClasses });
  if (!finalClasses.includes('{A,C,E}')) throw new Error(`Expected {A,C,E} in final classes, got ${finalClasses}`);

  // Reset
  await page.click('#btn-min-reset');
  const resetDesc = await page.$eval('#lbl-min-step-desc', el => el.textContent.trim());
  console.log('After Reset:', { resetDesc });
  if (!resetDesc.includes('Step 0')) throw new Error(`Expected Step 0 after reset, got ${resetDesc}`);

  await browser.close();
  console.log('TOC Unit 2 interactive test passed 100%!');
})();
