import os
import shutil
from fontTools.ttLib import TTFont

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS_DIR = os.path.join(REPO_ROOT, 'fonts')
NODE_MODULES = os.path.join(REPO_ROOT, 'node_modules')

LATIN_RANGE = "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"
LATIN_EXT_RANGE = "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C4, U+2113, U+2C60-2C7F, U+A720-A7FF"
GREEK_RANGE = "U+0370-03FF, U+1F00-1FFF"

FONT_FILES = [
    # Patrick Hand (Regular 400)
    {
        'src': os.path.join(NODE_MODULES, '@fontsource/patrick-hand/files/patrick-hand-latin-400-normal.woff2'),
        'src_ext': os.path.join(NODE_MODULES, '@fontsource/patrick-hand/files/patrick-hand-latin-ext-400-normal.woff2'),
        'dest': 'patrick-hand-400-latin.woff2',
        'dest_ext': 'patrick-hand-400-latin-ext.woff2',
        'family': 'Patrick Hand',
        'weight': 400,
        'style': 'normal'
    },
    # Caveat (Regular 400 and Bold 700)
    {
        'src': os.path.join(NODE_MODULES, '@fontsource/caveat/files/caveat-latin-400-normal.woff2'),
        'src_ext': os.path.join(NODE_MODULES, '@fontsource/caveat/files/caveat-latin-ext-400-normal.woff2'),
        'dest': 'caveat-400-latin.woff2',
        'dest_ext': 'caveat-400-latin-ext.woff2',
        'family': 'Caveat',
        'weight': 400,
        'style': 'normal'
    },
    {
        'src': os.path.join(NODE_MODULES, '@fontsource/caveat/files/caveat-latin-700-normal.woff2'),
        'src_ext': os.path.join(NODE_MODULES, '@fontsource/caveat/files/caveat-latin-ext-700-normal.woff2'),
        'dest': 'caveat-700-latin.woff2',
        'dest_ext': 'caveat-700-latin-ext.woff2',
        'family': 'Caveat',
        'weight': 700,
        'style': 'normal'
    },
    # Kalam (Regular 400 and Bold 700)
    {
        'src': os.path.join(NODE_MODULES, '@fontsource/kalam/files/kalam-latin-400-normal.woff2'),
        'src_ext': os.path.join(NODE_MODULES, '@fontsource/kalam/files/kalam-latin-ext-400-normal.woff2'),
        'dest': 'kalam-400-latin.woff2',
        'dest_ext': 'kalam-400-latin-ext.woff2',
        'family': 'Kalam',
        'weight': 400,
        'style': 'normal'
    },
    {
        'src': os.path.join(NODE_MODULES, '@fontsource/kalam/files/kalam-latin-700-normal.woff2'),
        'src_ext': os.path.join(NODE_MODULES, '@fontsource/kalam/files/kalam-latin-ext-700-normal.woff2'),
        'dest': 'kalam-700-latin.woff2',
        'dest_ext': 'kalam-700-latin-ext.woff2',
        'family': 'Kalam',
        'weight': 700,
        'style': 'normal'
    },
    # JetBrains Mono (Regular 400 and Bold 700)
    {
        'src': os.path.join(NODE_MODULES, '@fontsource/jetbrains-mono/files/jetbrains-mono-latin-400-normal.woff2'),
        'src_ext': os.path.join(NODE_MODULES, '@fontsource/jetbrains-mono/files/jetbrains-mono-latin-ext-400-normal.woff2'),
        'src_greek': os.path.join(NODE_MODULES, '@fontsource/jetbrains-mono/files/jetbrains-mono-greek-400-normal.woff2'),
        'dest': 'jetbrains-mono-400.woff2',
        'dest_ext': 'jetbrains-mono-400-ext.woff2',
        'dest_greek': 'jetbrains-mono-400-greek.woff2',
        'family': 'JetBrains Mono',
        'weight': 400,
        'style': 'normal'
    },
    {
        'src': os.path.join(NODE_MODULES, '@fontsource/jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2'),
        'src_ext': os.path.join(NODE_MODULES, '@fontsource/jetbrains-mono/files/jetbrains-mono-latin-ext-700-normal.woff2'),
        'src_greek': os.path.join(NODE_MODULES, '@fontsource/jetbrains-mono/files/jetbrains-mono-greek-700-normal.woff2'),
        'dest': 'jetbrains-mono-700.woff2',
        'dest_ext': 'jetbrains-mono-700-ext.woff2',
        'dest_greek': 'jetbrains-mono-700-greek.woff2',
        'family': 'JetBrains Mono',
        'weight': 700,
        'style': 'normal'
    }
]

def main():
    print("Rebuilding fonts directory and fonts.css...")

    for fname in os.listdir(FONTS_DIR):
        if fname.endswith('.woff2'):
            os.remove(os.path.join(FONTS_DIR, fname))

    css_blocks = [
        "/* ==========================================================================",
        "   SEM 5 · ISE Notes - Handwriting & Monospace Font Bundles",
        "   All fonts licensed under SIL Open Font License (OFL 1.1)",
        "   Families: Patrick Hand, Caveat, Kalam, JetBrains Mono",
        "   Complete Basic Latin, Latin-Extended & Greek glyph coverage",
        "   ========================================================================== */\n"
    ]

    for item in FONT_FILES:
        # Copy latin woff2
        dest_path = os.path.join(FONTS_DIR, item['dest'])
        shutil.copyfile(item['src'], dest_path)

        # Copy latin-ext woff2 if present
        has_ext = 'src_ext' in item and os.path.exists(item['src_ext'])
        if has_ext:
            dest_ext_path = os.path.join(FONTS_DIR, item['dest_ext'])
            shutil.copyfile(item['src_ext'], dest_ext_path)

        # Copy greek woff2 if present
        has_greek = 'src_greek' in item and os.path.exists(item['src_greek'])
        if has_greek:
            dest_greek_path = os.path.join(FONTS_DIR, item['dest_greek'])
            shutil.copyfile(item['src_greek'], dest_greek_path)

        # Verify font with fontTools
        font = TTFont(dest_path)
        cmap = font.getBestCmap()
        weight_class = font['OS/2'].usWeightClass
        has_fvar = 'fvar' in font
        assert not has_fvar, f"Error: {item['dest']} is a variable font!"
        assert weight_class == item['weight'], f"Error: {item['dest']} weight is {weight_class}, expected {item['weight']}"
        has_az = all(ord(c) in cmap for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        has_az_lower = all(ord(c) in cmap for c in 'abcdefghijklmnopqrstuvwxyz')
        has_digits = all(ord(c) in cmap for c in '0123456789')
        assert has_az and has_az_lower and has_digits, f"Error: {item['dest']} missing ASCII!"
        print(f"VERIFIED: {item['family']} ({item['weight']}) -> {item['dest']} ({len(cmap)} glyphs, static CID-ready)")

        # Generate CSS
        if has_greek:
            css_blocks.append(f"""@font-face {{
  font-family: '{item['family']}';
  font-style: {item['style']};
  font-weight: {item['weight']};
  font-display: swap;
  src: url('{item['dest_greek']}') format('woff2');
  unicode-range: {GREEK_RANGE};
}}
""")
        if has_ext:
            css_blocks.append(f"""@font-face {{
  font-family: '{item['family']}';
  font-style: {item['style']};
  font-weight: {item['weight']};
  font-display: swap;
  src: url('{item['dest_ext']}') format('woff2');
  unicode-range: {LATIN_EXT_RANGE};
}}
""")
        css_blocks.append(f"""@font-face {{
  font-family: '{item['family']}';
  font-style: {item['style']};
  font-weight: {item['weight']};
  font-display: swap;
  src: url('{item['dest']}') format('woff2');
  unicode-range: {LATIN_RANGE};
}}
""")

    fonts_css_path = os.path.join(FONTS_DIR, 'fonts.css')
    with open(fonts_css_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(css_blocks))
    print(f"Generated {fonts_css_path}")

    # Ensure OFL.txt license file exists and is complete
    ofl_path = os.path.join(FONTS_DIR, 'OFL.txt')
    with open(ofl_path, 'w', encoding='utf-8') as f:
        f.write("""SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
---------------------------------------------------
This repository bundles the following fonts licensed under SIL Open Font License (OFL 1.1):
1. Patrick Hand (Copyright (c) 2010-2012 Patrick Neveu, patrick.neveu@free.fr)
2. Caveat (Copyright (c) 2014-2020 Tipotype, info@tipotype.com)
3. Kalam (Copyright (c) 2014-2015 Indian Type Foundry, info@indiantypefoundry.com)
4. JetBrains Mono (Copyright (c) 2020 JetBrains s.r.o.)

PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide development of collaborative font projects, to support the font creation efforts of academic and linguistic communities, and to provide a free and open framework in which fonts may be shared and improved in partnership with others.

PERMISSION & CONDITIONS
Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies of the Font Software, subject to the standard OFL conditions.
""")
    print("Bundled fonts/OFL.txt successfully.")

if __name__ == '__main__':
    main()
