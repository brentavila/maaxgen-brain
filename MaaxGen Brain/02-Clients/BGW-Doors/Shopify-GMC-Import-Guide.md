# BGW Doors — Shopify GMC Import Guide

**File to import:** `Data/products_export_gmc_optimized.csv`  
**Products:** 30 featured collection handles, 320 variant rows  
**Regenerate:** `python3 Data/generate_gmc_import.py`

---

## What Was Optimized (Google Merchant Center Best Practices)

Per [Google title guidelines](https://support.google.com/merchants/answer/6324415) and BGW feed strategy:

| Field | Before | After |
|-------|--------|-------|
| **Title** | `Solid Wood Exterior Door M580E` | `Pre-Hung Wood Front Door \| M580E \| Double \| BGW Doors` |
| **SEO Title** | Good but not in feed | Matches optimized Title |
| **SEO Description** | Short | Pre-hung, material, shipping, install note (landing-page aligned) |
| **Google Product Category** | Empty on most | `4634` (Doors) |
| **MPN** | Empty | Model number (M580E, FD05, ID03, etc.) |
| **Condition** | Empty | `new` |
| **Custom Label 0** | Empty | `wood` / `fiberglass` / `iron` |
| **Custom Label 1** | Empty | `high` (wood) / `medium` |
| **Custom Label 2** | Empty | `hero` (top sellers) / `stable` |
| **Custom Label 3** | Empty | `pre-hung-double` / `pre-hung-sidelight` / `pre-hung` |
| **Custom Label 4** | Empty | `in-stock` |
| **Product Category** | Sparse | `Home & Garden > Doors > Exterior Entry Doors > ...` |
| **Tags** | Partial | Added `pre-hung`, `entry door`, `exterior door` |

### Hero products (custom_label_2 = hero)

- M580E, M580E-White, M280, M705A, FD05, FD04W, ID03

---

## Before You Import

### 1. Align product pages with new titles

Google requires feed titles to **match the landing page**. After import, verify each product page shows:
- "Pre-Hung" in the visible product name or prominent H1
- Material (Wood / Fiberglass / Iron)
- Configuration (Single, Double, With Sidelights)

If the theme displays only the old title, update the product page template or add "Pre-Hung" to the product description header.

### 2. Backup

Shopify Admin → Products → Export → Current export (backup).

### 3. Google & YouTube app feed settings

After import, confirm in **Shopify → Google & YouTube**:
- Feed uses **product title** from Shopify (will now be optimized)
- Or configure to use **SEO title** if you prefer keeping display title separate
- Trigger manual sync to Merchant Center
- Check **Merchant Center → Products** within 24–48 hours

---

## Import Steps (Shopify Admin)

1. Go to **Products → Import**
2. Click **Add file** → select `products_export_gmc_optimized.csv`
3. Check **"Overwrite products with matching handles"**
4. Click **Import products**
5. Wait for processing email (320 rows may take a few minutes)

### Columns updated on import

The CSV contains all original columns. Shopify updates any column present. Key changed columns:

- Title
- SEO Title
- SEO Description
- Type
- Tags
- Product Category
- Google Shopping / Google Product Category
- Google Shopping / MPN
- Google Shopping / Condition
- Google Shopping / Custom Label 0–4

**Not changed:** Price, inventory, images, variants structure, Body HTML.

---

## After Import Checklist

- [ ] Spot-check 5 products on site — title shows "Pre-Hung"
- [ ] Google & YouTube app → sync feed
- [ ] Merchant Center → Diagnostics → 0 new errors
- [ ] Merchant Center → Products → spot-check title matches live page
- [ ] Google Ads → PMax listing groups → filter by custom_label_0 (wood/fiberglass/iron)
- [ ] Log change in `Change-Log.md`

---

## PMax Listing Group Setup (after labels sync)

Use custom labels in **Sales-Performance Max-19** and **Performance Max: California**:

| Listing group | Filter |
|---------------|--------|
| Wood Pre-Hung | `custom_label_0` = wood AND `custom_label_3` contains pre-hung |
| Wood Double | `custom_label_3` = pre-hung-double |
| Fiberglass | `custom_label_0` = fiberglass |
| Iron | `custom_label_0` = iron |
| Heroes only | `custom_label_2` = hero |

---

## Sample Optimized Titles

| Handle | New Title |
|--------|-----------|
| m580e-exterior-wood-double-doors | Pre-Hung Wood Front Door \| M580E \| Double \| BGW Doors |
| m-280a-mahogany-door | Pre-Hung Wood Front Door \| M280 \| Single With Sidelights \| BGW Doors |
| fiberglass-exterior-door-fd05 | Pre-Hung Fiberglass Front Door \| FD05 \| Single With Sidelights \| BGW Doors |
| francisco-iron-door | Pre-Hung Iron Front Door \| ID03 \| Double \| BGW Doors |
| folding-door | Bi-Fold Aluminum Patio Door \| Interior Exterior \| BGW Doors |

---

## Regenerating the File

If you add products to the featured collection:

1. Export new CSV from Shopify
2. Save as `products_export_1 (3).csv` (or update path in script)
3. Run: `python3 "MaaxGen Brain/02-Clients/BGW-Doors/Data/generate_gmc_import.py"`
4. Import `products_export_gmc_optimized.csv`

---

## Related

- [[Google-Ads-Location-Targeting]]
- [[Merchant-Center]]
- [[Data/Analysis/feed-title-audit.md]]
