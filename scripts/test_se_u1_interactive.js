const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/se/unit1/unit-1-notes.html');

  console.log('Testing Scrum Velocity & Burndown Simulator...');
  // Initial state check
  const initCompleted = await page.$eval('#out-total-completed', el => el.textContent.trim());
  const initVelocity = await page.$eval('#out-avg-velocity', el => el.textContent.trim());
  const initRemaining = await page.$eval('#out-remaining-backlog', el => el.textContent.trim());
  const initSprints = await page.$eval('#out-sprints-remaining', el => el.textContent.trim());
  const initVerdict = await page.$eval('#out-release-verdict', el => el.textContent.trim());

  console.log('Initial Scrum State:', { initCompleted, initVelocity, initRemaining, initSprints, initVerdict });
  if (initCompleted !== '132 SP') throw new Error(`Expected 132 SP, got ${initCompleted}`);
  if (initVelocity !== '44.00 SP/sprint') throw new Error(`Expected 44.00 SP/sprint, got ${initVelocity}`);
  if (initRemaining !== '48 SP') throw new Error(`Expected 48 SP, got ${initRemaining}`);
  if (!initSprints.includes('1.09 sprints')) throw new Error(`Expected 1.09 sprints, got ${initSprints}`);
  if (!initVerdict.includes('ON TRACK')) throw new Error(`Expected ON TRACK, got ${initVerdict}`);

  // Test adjusting Sprint 1 to 50 SP
  const s1 = await page.$('#slider-sprint-1');
  await s1.evaluate(el => {
    el.value = '50';
    el.dispatchEvent(new Event('input'));
  });

  const updatedCompleted = await page.$eval('#out-total-completed', el => el.textContent.trim());
  const updatedVelocity = await page.$eval('#out-avg-velocity', el => el.textContent.trim());
  const updatedRemaining = await page.$eval('#out-remaining-backlog', el => el.textContent.trim());

  console.log('After Sprint 1 = 50 SP:', { updatedCompleted, updatedVelocity, updatedRemaining });
  if (updatedCompleted !== '142 SP') throw new Error(`Expected 142 SP, got ${updatedCompleted}`);
  if (updatedVelocity !== '47.33 SP/sprint') throw new Error(`Expected 47.33 SP/sprint, got ${updatedVelocity}`);
  if (updatedRemaining !== '38 SP') throw new Error(`Expected 38 SP, got ${updatedRemaining}`);

  // Verify SVG burndown chart has polyline and circles
  const hasPolyline = await page.$eval('#svg-burndown-chart polyline', el => !!el.getAttribute('points'));
  const circlesCount = await page.$$eval('#svg-burndown-chart circle', els => els.length);
  console.log('Burndown Chart Elements:', { hasPolyline, circlesCount });
  if (!hasPolyline) throw new Error('Expected polyline in burndown chart');
  if (circlesCount !== 4) throw new Error(`Expected 4 circles, got ${circlesCount}`);

  await browser.close();
  console.log('All SE Unit 1 interactive tests PASSED successfully!');
})();
