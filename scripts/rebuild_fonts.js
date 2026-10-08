const fs = require('fs');
const path = require('path');
const https = require('https');

const fontsDir = path.resolve(__dirname, '..', 'fonts');

function download(url, dest) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return download(res.headers.location, dest).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        return reject(new Error(`Failed ${url}: status ${res.statusCode}`));
      }
      const file = fs.createWriteStream(dest);
      res.pipe(file);
      file.on('finish', () => file.close(resolve));
    }).on('error', reject);
  });
}

const FONTS_TO_DOWNLOAD = [
  { name: 'Patrick Hand', query: 'Patrick+Hand:wght@400', slug: 'patrick-hand' },
  { name: 'Caveat', query: 'Caveat:wght@400;700', slug: 'caveat' },
  { name: 'Kalam', query: 'Kalam:wght@400;700', slug: 'kalam' },
  { name: 'JetBrains Mono', query: 'JetBrains+Mono:wght@400;700', slug: 'jetbrains-mono' }
];

async function main() {
  console.log('Rebuilding fonts in:', fontsDir);
  
  // 1. Remove old woff2 files in fonts directory
  const existingFiles = fs.readdirSync(fontsDir);
  for (const f of existingFiles) {
    if (f.endsWith('.woff2')) {
      fs.unlinkSync(path.join(fontsDir, f));
      console.log('Deleted old font file:', f);
    }
  }

  let generatedCssRules = [];

  for (const item of FONTS_TO_DOWNLOAD) {
    console.log(`\nFetching CSS for ${item.name}...`);
    const cssUrl = `https://fonts.googleapis.com/css2?family=${item.query}&display=swap`;
    const res = await fetch(cssUrl, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });
    const css = await res.text();

    // Regex to accurately match: /* [subset] */ @font-face { [body] }
    const blockRegex = /\/\*\s*([^*]+?)\s*\*\/\s*@font-face\s*\{([\s\S]*?)\}/g;
    let match;

    while ((match = blockRegex.exec(css)) !== null) {
      const subset = match[1].trim();
      const body = match[2];

      // We only need 'latin' and 'latin-ext' (and devanagari for Kalam if desired)
      if (subset !== 'latin' && subset !== 'latin-ext') {
        continue;
      }

      const famMatch = body.match(/font-family:\s*['"]?([^'";]+)/);
      const weightMatch = body.match(/font-weight:\s*([^;]+)/);
      const styleMatch = body.match(/font-style:\s*([^;]+)/);
      const urlMatch = body.match(/src:\s*url\((https:[^)]+)\)/);
      const rangeMatch = body.match(/unicode-range:\s*([^;]+)/);

      if (!famMatch || !urlMatch) continue;

      const family = famMatch[1].trim();
      const weight = weightMatch ? weightMatch[1].trim() : '400';
      const style = styleMatch ? styleMatch[1].trim() : 'normal';
      const fontUrl = urlMatch[1].trim();
      const unicodeRange = rangeMatch ? rangeMatch[1].trim() : 'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD';

      const filename = `${item.slug}-${weight}-${subset}.woff2`;
      const destPath = path.join(fontsDir, filename);

      console.log(`  Downloading ${filename} (${subset}, weight ${weight}) from ${fontUrl}...`);
      await download(fontUrl, destPath);

      const rule = `@font-face {\n  font-family: '${family}';\n  font-style: ${style};\n  font-weight: ${weight};\n  font-display: swap;\n  src: url('${filename}') format('woff2');\n  unicode-range: ${unicodeRange};\n}`;
      generatedCssRules.push(rule);
    }
  }

  const cssPath = path.join(fontsDir, 'fonts.css');
  const finalCssContent = `/* ==========================================================================
   SEM 5 · ISE Notes - Handwriting & Monospace Font Bundles
   All fonts licensed under SIL Open Font License (OFL 1.1)
   Families: Patrick Hand, Caveat, Kalam, JetBrains Mono
   ========================================================================== */

${generatedCssRules.join('\n\n')}
`;

  fs.writeFileSync(cssPath, finalCssContent, 'utf8');
  console.log(`\nSuccessfully wrote ${generatedCssRules.length} @font-face rules into ${cssPath}`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
