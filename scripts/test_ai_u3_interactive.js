const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/ai/unit3/unit-3-notes.html');

  console.log('Testing Minimax & Alpha-Beta Game Tree Simulator (Tab 1)...');
  // Initial state: exam_default preset with Alpha-Beta active
  const rootVal = await page.$eval('#out-game-root', el => el.textContent.trim());
  const bestMove = await page.$eval('#out-game-move', el => el.textContent.trim());
  const evalsText = await page.$eval('#out-game-evals', el => el.textContent.trim());
  const prunedText = await page.$eval('#out-game-pruned', el => el.textContent.trim());

  console.log('Initial Game Tree State:', { rootVal, bestMove, evalsText, prunedText });
  if (rootVal !== '3') throw new Error(`Expected root value 3, got ${rootVal}`);
  if (!bestMove.includes('Branch B')) throw new Error(`Expected Branch B, got ${bestMove}`);
  if (!evalsText.includes('7 of 9 leaves')) throw new Error(`Expected 7 of 9 leaves, got ${evalsText}`);
  if (!prunedText.includes('Leaves 4, 6 under Node C')) throw new Error(`Expected pruned leaves 4, 6 under C, got ${prunedText}`);

  // Test switching to Pure Minimax (all 9 leaves evaluated)
  await page.selectOption('#select-prune-mode', 'pure_minimax');
  const mmEvals = await page.$eval('#out-game-evals', el => el.textContent.trim());
  const mmPruned = await page.$eval('#out-game-pruned', el => el.textContent.trim());
  console.log('After Pure Minimax Selection:', { mmEvals, mmPruned });
  if (!mmEvals.includes('9 of 9 leaves')) throw new Error(`Expected 9 of 9 leaves for pure Minimax, got ${mmEvals}`);
  if (!mmPruned.includes('Pruning Disabled')) throw new Error(`Expected Pruning Disabled, got ${mmPruned}`);

  console.log('Testing Australia Map CSP & AC-3 Explorer (Tab 2)...');
  // Click Tab 2
  await page.click('#tab-btn-ac3');
  await page.waitForTimeout(200);

  // Check initial state: WA = Red
  const domWA = await page.$eval('#out-dom-wa', el => el.textContent.trim());
  const domNT = await page.$eval('#out-dom-nt', el => el.textContent.trim());
  const domSA = await page.$eval('#out-dom-sa', el => el.textContent.trim());
  console.log('Initial AC-3 State (WA=Red):', { domWA, domNT, domSA });
  if (!domWA.includes('Red')) throw new Error(`Expected Red for WA, got ${domWA}`);
  if (!domNT.includes('G, B')) throw new Error(`Expected {G, B} for NT, got ${domNT}`);
  if (!domSA.includes('G, B')) throw new Error(`Expected {G, B} for SA, got ${domSA}`);

  // Select SA = Green (dual assignment)
  await page.selectOption('#select-sa-color', 'G');
  const dualNT = await page.$eval('#out-dom-nt', el => el.textContent.trim());
  const dualSA = await page.$eval('#out-dom-sa', el => el.textContent.trim());
  console.log('After WA=Red and SA=Green:', { dualNT, dualSA });
  if (!dualNT.includes('Blue')) throw new Error(`Expected NT to be uniquely Blue, got ${dualNT}`);
  if (!dualSA.includes('Green')) throw new Error(`Expected SA to be Green, got ${dualSA}`);

  // Select WA = unassigned
  await page.selectOption('#select-wa-color', 'unassigned');
  const resetNT = await page.$eval('#out-dom-nt', el => el.textContent.trim());
  console.log('After Reset:', { resetNT });
  if (!resetNT.includes('R, G, B')) throw new Error(`Expected {R, G, B} for reset, got ${resetNT}`);

  await browser.close();
  console.log('All AI Unit 3 interactive tests PASSED successfully!');
})();
