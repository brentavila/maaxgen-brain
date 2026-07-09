# BGW Doors — Data Exports

Index of analysis exports. Place CSV files in this folder (`02-Clients/BGW-Doors/Data/Exports/`).

## Files

| File | Status | Used for |
|------|--------|----------|
| Shopify customer export (720 days) | Pending sync | Revenue by state/city — geo truth |
| `product_export_1.csv` | Pending sync | Featured collection feed title audit |
| GA4 YTD export | Pending sync | Funnel CVR, channel performance |
| BGW Doors Location report Last 720 Days | Pending sync | Google Ads spend/conversions by location |

## Run Analysis

From repo root:

```bash
python3 "MaaxGen Brain/02-Clients/BGW-Doors/Data/analyze_exports.py"
```

Outputs: `Data/Analysis/geo-reconciliation.md`, `Data/Analysis/feed-title-audit.md`, `Data/Analysis/summary.md`
