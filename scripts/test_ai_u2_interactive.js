const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/ai/unit2/unit-2-notes.html');

  console.log('Testing Graph Search Strategy Comparator (Tab 1)...');
  // Initial state: A* search
  const astarPath = await page.$eval('#out-search-path', el => el.textContent.trim());
  const astarCost = await page.$eval('#out-search-cost', el => el.textContent.trim());
  const astarOpt = await page.$eval('#out-search-opt', el => el.textContent.trim());
  console.log('A* Search Initial State:', { astarPath, astarCost, astarOpt });
  if (!astarPath.includes('S → A → B → C → D → G')) throw new Error(`Expected S → A → B → C → D → G, got ${astarPath}`);
  if (astarCost !== '8.0') throw new Error(`Expected 8.0, got ${astarCost}`);
  if (!astarOpt.includes('Optimal')) throw new Error(`Expected Optimal, got ${astarOpt}`);

  // Test Greedy Best-First Search
  await page.selectOption('#select-search-algo', 'greedy');
  const greedyCost = await page.$eval('#out-search-cost', el => el.textContent.trim());
  const greedyOpt = await page.$eval('#out-search-opt', el => el.textContent.trim());
  console.log('After Greedy Selection:', { greedyCost, greedyOpt });
  if (greedyCost !== '10.0 (Suboptimal!)') throw new Error(`Expected 10.0 (Suboptimal!), got ${greedyCost}`);
  if (!greedyOpt.includes('Not Optimal')) throw new Error(`Expected Not Optimal, got ${greedyOpt}`);

  // Test UCS
  await page.selectOption('#select-search-algo', 'ucs');
  const ucsCost = await page.$eval('#out-search-cost', el => el.textContent.trim());
  console.log('After UCS Selection:', { ucsCost });
  if (ucsCost !== '8.0') throw new Error(`Expected 8.0 for UCS, got ${ucsCost}`);

  // Test DFS
  await page.selectOption('#select-search-algo', 'dfs');
  const dfsCost = await page.$eval('#out-search-cost', el => el.textContent.trim());
  console.log('After DFS Selection:', { dfsCost });
  if (dfsCost !== '14.0 (Suboptimal!)') throw new Error(`Expected 14.0 for DFS, got ${dfsCost}`);

  console.log('Testing Simulated Annealing Boltzmann Calculator (Tab 2)...');
  // Click Tab 2
  await page.click('#tab-btn-anneal');
  await page.waitForTimeout(200);

  // Check initial state: dE = -5, T = 100
  const initialProb = await page.$eval('#out-anneal-prob', el => el.textContent.trim());
  const initialRegime = await page.$eval('#out-anneal-regime', el => el.textContent.trim());
  console.log('Initial Annealing State:', { initialProb, initialRegime });
  if (initialProb !== '95.12 %') throw new Error(`Expected 95.12 %, got ${initialProb}`);

  // Move Temperature slider to 1000 K
  const sliderTemp = await page.$('#slider-temperature');
  await sliderTemp.evaluate(el => {
    el.value = '1000';
    el.dispatchEvent(new Event('input'));
  });
  const hotProb = await page.$eval('#out-anneal-prob', el => el.textContent.trim());
  console.log('After T = 1000 K:', { hotProb });
  if (hotProb !== '99.50 %') throw new Error(`Expected 99.50 %, got ${hotProb}`);

  // Move Temperature slider to 1 K
  await sliderTemp.evaluate(el => {
    el.value = '1';
    el.dispatchEvent(new Event('input'));
  });
  const coldProb = await page.$eval('#out-anneal-prob', el => el.textContent.trim());
  const coldRegime = await page.$eval('#out-anneal-regime', el => el.textContent.trim());
  console.log('After T = 1 K:', { coldProb, coldRegime });
  if (coldProb !== '0.67 %') throw new Error(`Expected 0.67 %, got ${coldProb}`);
  if (!coldRegime.includes('Greedy')) throw new Error(`Expected Greedy regime, got ${coldRegime}`);

  await browser.close();
  console.log('All AI Unit 2 interactive tests PASSED successfully!');
})();
