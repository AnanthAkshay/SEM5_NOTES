const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/cn/unit3/unit-3-notes.html', { waitUntil: 'networkidle' });

  // 1. IPv4 Header
  const figHdr = page.locator('#fig-ipv4-header');
  await figHdr.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await figHdr.screenshot({ path: 'audit/scratch/cn_u3_ipv4_header_desktop.png' });

  // 2. CIDR Bit Breakdown & Subnet widget
  const figCidr = page.locator('#fig-cidr-breakdown');
  await figCidr.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await figCidr.screenshot({ path: 'audit/scratch/cn_u3_cidr_breakdown_desktop.png' });

  const widgetSubnet = page.locator('#subnet-calculator-widget');
  await widgetSubnet.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await widgetSubnet.screenshot({ path: 'audit/scratch/cn_u3_subnet_calculator_desktop.png' });

  // 3. NAT Flow
  const figNat = page.locator('#fig-nat-flow');
  await figNat.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await figNat.screenshot({ path: 'audit/scratch/cn_u3_nat_flow_desktop.png' });

  // 4. Dijkstra Graph
  const figDijk = page.locator('#fig-dijkstra-graph');
  await figDijk.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await figDijk.screenshot({ path: 'audit/scratch/cn_u3_dijkstra_graph_desktop.png' });

  // Mobile screenshot (390px)
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(300);
  await figHdr.scrollIntoViewIfNeeded();
  await page.waitForTimeout(200);
  await figHdr.screenshot({ path: 'audit/scratch/cn_u3_ipv4_header_mobile.png' });

  await browser.close();
  console.log('CN Unit 3 all screenshots captured successfully.');
})();
