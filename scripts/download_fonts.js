const fs = require('fs');
const https = require('https');
const path = require('path');

const fontsDir = path.join(__dirname, '..', 'fonts');
if (!fs.existsSync(fontsDir)) fs.mkdirSync(fontsDir, { recursive: true });

async function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return downloadFile(res.headers.location, dest).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        return reject(new Error(`Failed to get '${url}' (${res.statusCode})`));
      }
      const file = fs.createWriteStream(dest);
      res.pipe(file);
      file.on('finish', () => file.close(resolve));
    }).on('error', reject);
  });
}

const fontFamilies = [
  'Patrick+Hand',
  'Caveat:wght@400;600;700',
  'Kalam:wght@400;700',
  'Indie+Flower',
  'Architects+Daughter',
  'Gaegu:wght@400;700',
  'Shadows+Into+Light',
  'JetBrains+Mono:ital,wght@0,400;0,600;1,400'
];

async function fetchGoogleFontCss(family) {
  const url = `https://fonts.googleapis.com/css2?family=${family}&display=swap`;
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
  });
  return await res.text();
}

async function main() {
  console.log('Downloading fonts into:', fontsDir);
  let localCssRules = [];
  let fileIndex = 0;

  for (const family of fontFamilies) {
    console.log(`Fetching CSS for ${family}...`);
    const css = await fetchGoogleFontCss(family);
    
    // Parse each @font-face block
    const blocks = css.split('@font-face');
    for (const b of blocks) {
      if (!b.includes('font-family')) continue;
      
      const familyMatch = b.match(/font-family:\s*['"]?([^'";]+)['"]?;/);
      const styleMatch = b.match(/font-style:\s*([^;]+);/);
      const weightMatch = b.match(/font-weight:\s*([^;]+);/);
      const srcMatch = b.match(/src:\s*url\((https:[^)]+)\)\s*format\(['"]?woff2['"]?\);/);
      const unicodeMatch = b.match(/unicode-range:\s*([^;]+);/);

      if (!familyMatch || !srcMatch) continue;

      const fontFam = familyMatch[1].trim();
      const fontStyle = styleMatch ? styleMatch[1].trim() : 'normal';
      const fontWeight = weightMatch ? weightMatch[1].trim() : '400';
      const fontUrl = srcMatch[1].trim();
      const unicodeRange = unicodeMatch ? unicodeMatch[1].trim() : null;

      // Only download latin / primary subsets to keep file size small and fast
      const commentMatch = b.match(/\/\*\s*([^*]+)\s*\*\//);
      const subset = commentMatch ? commentMatch[1].trim() : 'subset';

      // We need latin subset primarily
      if (subset !== 'latin' && !family.includes('Kalam') && subset !== 'latin-ext') {
        // If it's another script and not latin, skip unless needed
        if (!subset.includes('latin') && !subset.includes('devanagari')) continue;
      }

      fileIndex++;
      const cleanName = fontFam.toLowerCase().replace(/[^a-z0-9]/g, '_');
      const filename = `${cleanName}-${fontWeight}-${fontStyle}-${subset}-${fileIndex}.woff2`;
      const destPath = path.join(fontsDir, filename);

      console.log(`  Downloading ${filename} from ${fontUrl}...`);
      await downloadFile(fontUrl, destPath);

      let rule = `@font-face {\n  font-family: '${fontFam}';\n  font-style: ${fontStyle};\n  font-weight: ${fontWeight};\n  font-display: swap;\n  src: url('${filename}') format('woff2');`;
      if (unicodeRange) {
        rule += `\n  unicode-range: ${unicodeRange};`;
      }
      rule += '\n}';
      localCssRules.push(rule);
    }
  }

  const cssPath = path.join(fontsDir, 'fonts.css');
  fs.writeFileSync(cssPath, localCssRules.join('\n\n') + '\n', 'utf8');
  console.log(`Successfully written fonts.css with ${localCssRules.length} font-faces.`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
