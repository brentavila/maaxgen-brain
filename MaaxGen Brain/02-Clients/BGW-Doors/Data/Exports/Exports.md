# BGW Doors — Data Exports

Place CSV exports in **`Data/`** or **`Data/Exports/`** (either works).

## Required Files

| File | Used for | Status |
|------|----------|--------|
| Shopify customer export (720 days) | Revenue by state/city | Check GitHub |
| `product_export_1.csv` | Featured collection feed audit | Check GitHub |
| GA4 YTD export | Funnel / channel CVR | Check GitHub |
| BGW Doors Location report Last 720 Days | Google Ads geo spend | Check GitHub |

## Verify Files Are on GitHub

Adding files in Obsidian does **not** automatically commit them to git. After copying CSVs locally, run:

```bash
cd /path/to/maaxgen-brain
git status
git add "MaaxGen Brain/02-Clients/BGW-Doors/Data/"*.csv
git add "MaaxGen Brain/02-Clients/BGW-Doors/Data/Exports/"*.csv
git commit -m "Add BGW Doors data exports"
git push origin main
```

Confirm on GitHub:  
https://github.com/brentavila/maaxgen-brain/tree/main/MaaxGen%20Brain/02-Clients/BGW-Doors/Data

You should see `.csv` files listed, not only `.md` and `.py`.

## Run Analysis

```bash
python3 "MaaxGen Brain/02-Clients/BGW-Doors/Data/analyze_exports.py"
```

Outputs: `Data/Analysis/geo-reconciliation.md`, `feed-title-audit.md`, `summary.md`
