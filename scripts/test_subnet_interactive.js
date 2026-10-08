const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
  });
  const page = await browser.newPage();
  await page.goto('http://localhost:8088/SEM5_NOTES/notes/cn/unit3/unit-3-notes.html');

  // Initial State: 200.16.70.82 / 27
  const ipVal = await page.$eval('#input-ip', el => el.value);
  const prefVal = await page.$eval('#slider-prefix', el => el.value);
  const netVal = await page.$eval('#out-net', el => el.textContent.trim());
  const maskVal = await page.$eval('#out-mask', el => el.textContent.trim());
  const bcastVal = await page.$eval('#out-bcast', el => el.textContent.trim());
  const rangeVal = await page.$eval('#out-range', el => el.textContent.trim());
  const hostsVal = await page.$eval('#out-hosts', el => el.textContent.trim());

  console.log('Subnet Initial State:');
  console.log({ ipVal, prefVal, netVal, maskVal, bcastVal, rangeVal, hostsVal });

  if (netVal !== '200.16.70.64') throw new Error(`Expected Network 200.16.70.64, got ${netVal}`);
  if (maskVal !== '255.255.255.224') throw new Error(`Expected Mask 255.255.255.224, got ${maskVal}`);
  if (bcastVal !== '200.16.70.95') throw new Error(`Expected Broadcast 200.16.70.95, got ${bcastVal}`);
  if (!hostsVal.includes('30 Hosts')) throw new Error(`Expected 30 Hosts, got ${hostsVal}`);

  // Test updating prefix to /24
  await page.fill('#slider-prefix', '24');
  await page.dispatchEvent('#slider-prefix', 'input');
  const net24 = await page.$eval('#out-net', el => el.textContent.trim());
  const mask24 = await page.$eval('#out-mask', el => el.textContent.trim());
  const hosts24 = await page.$eval('#out-hosts', el => el.textContent.trim());
  console.log('/24 update:', { net24, mask24, hosts24 });
  if (net24 !== '200.16.70.0') throw new Error(`Expected 200.16.70.0 for /24, got ${net24}`);
  if (mask24 !== '255.255.255.0') throw new Error(`Expected 255.255.255.0 for /24, got ${mask24}`);

  await browser.close();
  console.log('Subnet interactive test passed 100%!');
})();
