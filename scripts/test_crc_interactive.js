const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/cn/unit2/unit-2-notes.html');

  // Verify elements exist
  const dataVal = await page.$eval('#input-dataword', el => el.value);
  const divVal = await page.$eval('#select-divisor', el => el.value);
  const fcsVal = await page.$eval('#out-fcs', el => el.textContent.trim());
  const codewordVal = await page.$eval('#out-codeword', el => el.textContent.trim());
  const synVal = await page.$eval('#out-syndrome', el => el.textContent.trim());

  console.log('CRC Initial State:');
  console.log({ dataVal, divVal, fcsVal, codewordVal, synVal });

  if (fcsVal !== '0100') {
    throw new Error(`Expected FCS 0100 for 101011 / 10011, got ${fcsVal}`);
  }

  // Test typing a different binary dataword
  await page.fill('#input-dataword', '1100');
  await page.dispatchEvent('#input-dataword', 'input');
  const newFcs = await page.$eval('#out-fcs', el => el.textContent.trim());
  console.log('New FCS for 1100 with 10011:', newFcs);

  await browser.close();
  console.log('CRC interactive test passed 100%!');
})();
