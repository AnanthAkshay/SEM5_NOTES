const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/toc/unit1/unit-1-notes.html');

  // Initial State: DFA ends_01, string 10101 -> ACCEPTED
  const autoVal = await page.$eval('#select-automaton', el => el.value);
  const strVal = await page.$eval('#input-test-string', el => el.value);
  const statusVal = await page.$eval('#out-status', el => el.textContent.trim());
  const finalVal = await page.$eval('#out-final-st', el => el.textContent.trim());

  console.log('DFA Simulator Initial State:', { autoVal, strVal, finalVal, statusVal });
  if (!statusVal.includes('ACCEPTED')) throw new Error(`Expected ACCEPTED for '10101', got ${statusVal}`);
  if (finalVal !== 'q₂') throw new Error(`Expected final state q₂, got ${finalVal}`);

  // Test typing a rejected string: 10100
  await page.fill('#input-test-string', '10100');
  await page.dispatchEvent('#input-test-string', 'input');
  const rejStatus = await page.$eval('#out-status', el => el.textContent.trim());
  const rejFinal = await page.$eval('#out-final-st', el => el.textContent.trim());
  console.log('After typing 10100:', { rejFinal, rejStatus });
  if (!rejStatus.includes('REJECTED')) throw new Error(`Expected REJECTED for '10100', got ${rejStatus}`);
  if (rejFinal !== 'q₁') throw new Error(`Expected final state q₁, got ${rejFinal}`);

  // Test selecting div_3 automaton
  await page.selectOption('#select-automaton', 'div_3');
  const div3Str = await page.$eval('#input-test-string', el => el.value);
  const div3Status = await page.$eval('#out-status', el => el.textContent.trim());
  console.log('After selecting div_3:', { div3Str, div3Status });
  if (!div3Status.includes('ACCEPTED')) throw new Error(`Expected ACCEPTED for '110' (6 mod 3 = 0), got ${div3Status}`);

  await browser.close();
  console.log('DFA interactive test passed 100%!');
})();
