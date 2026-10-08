const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/ai/unit1/unit-1-notes.html');

  console.log('Testing Agent Architecture Simulator (Tab 1)...');
  // Check initial state
  const initialTitle = await page.$eval('#out-agent-title', el => el.textContent.trim());
  const initialAction = await page.$eval('#out-agent-action', el => el.textContent.trim());
  console.log('Initial Agent State:', { initialTitle, initialAction });
  if (initialTitle !== 'Simple Reflex Agent') throw new Error(`Expected Simple Reflex Agent, got ${initialTitle}`);
  if (!initialAction.includes('SUCK')) throw new Error(`Expected SUCK, got ${initialAction}`);

  // Switch to Model-Based Agent
  await page.selectOption('#select-agent-type', 'model_based');
  const mbTitle = await page.$eval('#out-agent-title', el => el.textContent.trim());
  const mbState = await page.$eval('#out-agent-state', el => el.textContent.trim());
  console.log('After Model-Based Selection:', { mbTitle, mbState });
  if (!mbTitle.includes('Model-Based')) throw new Error(`Expected Model-Based, got ${mbTitle}`);
  if (!mbState.includes('Internal World Model')) throw new Error(`Expected Internal World Model in state, got ${mbState}`);

  // Switch to Utility-Based Agent
  await page.selectOption('#select-agent-type', 'utility_based');
  const utilTitle = await page.$eval('#out-agent-title', el => el.textContent.trim());
  console.log('After Utility-Based Selection:', { utilTitle });
  if (!utilTitle.includes('Utility-Based')) throw new Error(`Expected Utility-Based, got ${utilTitle}`);

  console.log('Testing PEAS & Environment Classifier (Tab 2)...');
  // Click Tab 2
  await page.click('#tab-btn-peas');
  await page.waitForTimeout(200);

  // Check initial system in Tab 2: Smart Traffic
  const pText = await page.$eval('#out-peas-p', el => el.textContent.trim());
  const pillsCount = await page.$$eval('#out-env-pills span', els => els.length);
  console.log('Traffic System PEAS:', { pText: pText.substring(0, 40) + '...', pillsCount });
  if (!pText.toLowerCase().includes('delay') && !pText.toLowerCase().includes('wait time')) {
    throw new Error(`Expected traffic delay/wait time in P, got ${pText}`);
  }
  if (pillsCount !== 7) throw new Error(`Expected 7 environmental dimension pills, got ${pillsCount}`);

  // Select Medical Diagnosis
  await page.selectOption('#select-peas-system', 'medical');
  const medPText = await page.$eval('#out-peas-p', el => el.textContent.trim());
  console.log('Medical System PEAS:', { medPText: medPText.substring(0, 40) + '...' });
  if (!medPText.toLowerCase().includes('diagnostic') && !medPText.toLowerCase().includes('precision')) {
    throw new Error(`Expected diagnostic in P, got ${medPText}`);
  }

  // Select Chess
  await page.selectOption('#select-peas-system', 'chess');
  const chessPText = await page.$eval('#out-peas-p', el => el.textContent.trim());
  const chessPill = await page.$eval('#out-env-pills span:first-child', el => el.textContent.trim());
  console.log('Chess System PEAS:', { chessPText, chessPill });
  if (!chessPill.includes('Fully Observable')) {
    throw new Error(`Expected Fully Observable for Chess, got ${chessPill}`);
  }

  await browser.close();
  console.log('All Agent Architecture & PEAS interactive tests PASSED successfully!');
})();
