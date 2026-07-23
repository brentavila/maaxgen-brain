# BGW Doors — Next Actions

From data analysis (Jul 9, 2026). Full reports in `Data/Analysis/`.

## Completed (2026-07-02)

- [x] **Decide offer architecture** — Auto-applied 20% at checkout on single shelf price (replaces compare-at + `FREESHIP2026`)
- [x] **Fix conflicting promo copy** — Website updated to unified "20% Off — Auto Applied At Checkout"
- [x] **Merchant Center promotion** — Created/updated
- [x] **Shopify pricing model** — Compare-at/sale split removed; single price = former compare-at
- [x] Last 30d campaign ROAS by campaign (CA PMax, US PMax, Brand) — see Google-Ads.md

## P0 — Do Before Any Budget or Geo Changes

- [ ] **Conversion tracking audit** — Confirm purchase is the only Primary action. GA4 shows 44 purchases YTD; Ads shows 711 conversions over 720 days (likely micro-conversion inflation).
- [ ] **Switch Merchant Center feed to SEO title + SEO description** in Shopify Google & YouTube app. Default titles lack "Pre-Hung" and "Front Door"; SEO titles are already written.
- [ ] **Re-export Merchant Center feed** — Confirm single-price model; verify MC promotion approved and visible
- [ ] **Update PMax ad assets** — Headlines/descriptions to match auto-applied 20% offer (no coupon, no strikethrough)

## P1 — Geo (after tracking verified)

- [ ] **Restrict Sales-Performance Max-19** to Tier A states: FL, NY, NJ, VA, TX, NC, PA, WA, GA, MD, AZ, MI, NV, AL, IL (331 customers, 52% of base outside CA)
- [ ] **Deprioritize/exclude** states with <5 Shopify customers (OR, HI, OH, KS, ID, MO, etc.)
- [ ] **Protect Brand Search** — $16,527 spend, 167 conv ($99 CPA); best campaign in location report
- [ ] **CA exclude test:** San Diego County ($2,182), Santa Clara County ($857), Fresno County ($319)
- [ ] **CA scale:** Ontario (10 customers, $59 spend), San Jose (15 customers, $538 spend)
- [ ] Optional: Export state-level report filtered to **Sales-Performance Max-19 only** ($119k still in "Other locations")

## P1 — Feed & PMax

- [ ] **Import** `Data/products_export_gmc_optimized.csv` into Shopify (see [[Shopify-GMC-Import-Guide]])
- [ ] Align product pages so visible titles include "Pre-Hung" (Google feed match requirement)
- [ ] Populate **custom labels** via import (wood/fiberglass/iron, hero, pre-hung config)
- [ ] Apply **location targeting** per [[Google-Ads-Location-Targeting]] (after tracking verified)
- [ ] Segment PMax asset groups: Wood / Fiberglass / Iron (wood gets 45% budget)
- [ ] Review why **slab doors** are top GA4 purchase item — limit slab in listing groups if margin is lower
- [ ] **Reduce PMax US budget** toward ~$3,600/mo until post-offer metrics prove out (was $7,772 at 0.22 post-sale ROAS). Do not cut Brand Search.
- [ ] **Pause Remarketing - Display** ($303, 0 conversions last 30d)
- [ ] **Exclude out-of-stock variants** from Merchant Center / PMax
- [ ] **Fix missing `condition` attributes** in feed

## P2 — CRO & Tracking Expansion

- [ ] Investigate **checkout abandonment** — 566 checkouts → 44 purchases (7.8%) YTD
- [ ] Import **phone clicks** (255 YTD) as conversion action
- [ ] Deploy **n8n Customer Match** sync (640 purchasers, weekly refresh)
- [ ] Add real product reviews on top 10 ad SKUs (remove placeholder blocks)
- [ ] Set default variant to lowest-price single door on Shopping landing products
- [ ] Cart/checkout: show 20% discount preview before checkout (if Shopify theme allows)

## P2 — Pricing (needs Paul/Kevin input)

- [ ] Benchmark top 15 SKUs vs Doors4Home, Home Depot, US Door on identical configs (36x80 single pre-hung) **at post-discount price** (20% off shelf)
- [ ] Identify SKUs where BGW is >25% above market even after 20% discount
- [ ] Consider pushing wood (highest margin) only where price is defensible

## Monitoring (2026-07-02 → ~2026-08-02)

- [ ] Shopify orders and revenue vs same period pre-change
- [ ] Google Ads ROAS, CPA, conv. rate (weekly) — baseline: 1.36 ROAS, $963 CPA
- [ ] MC promotion approval status

## Data Still Needed

- [ ] Product-level wasted spend list (PMax by SKU)
- [ ] Shopify **revenue** by state (current export is customer counts only)
- [ ] Merchant Center diagnostics / price competitiveness export
- [ ] MER reconciliation (total Shopify revenue vs total ad spend)
