# Artistic Entrances Assets

Product images and catalog source files do **not** live in this Obsidian vault. They are stored locally for staging and upload to CDN.

## Local paths

| Purpose | Path |
|---|---|
| Raw door photos | `C:\Users\brent\projects\artistic-entrances-assets\raw\doors\` |
| Catalog PDF and option crops | `C:\Users\brent\projects\artistic-entrances-assets\raw\catalog\` |
| Optimized files before CDN upload | `C:\Users\brent\projects\artistic-entrances-assets\processed\` |
| Configurator app code | `C:\Users\brent\projects\artistic-entrances-configurator\` |

## What to do

1. Copy the client door image folder into `raw\doors\`
2. Copy the product catalog PDF into `raw\catalog\`
3. From the configurator repo, run `npm run audit:assets`
4. After review, optimize files into `processed\` and run `npm run cdn:upload`

See [[Website-Configurator]] for the full launch workflow.
