# BGW Doors — Next Actions

From data analysis (Jul 9, 2026). Full reports in `Data/Analysis/`.

## P0 — Do Before Any Budget or Geo Changes

- [ ] **Conversion tracking audit** — Confirm purchase is the only Primary action. GA4 shows 44 purchases YTD; Ads shows 711 conversions over 720 days (likely micro-conversion inflation).
- [ ] **Switch Merchant Center feed to SEO title + SEO description** in Shopify Google & YouTube app. Default titles lack "Pre-Hung" and "Front Door"; SEO titles are already written.

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

## P2 — CRO & Tracking Expansion

- [ ] Investigate **checkout abandonment** — 566 checkouts → 44 purchases (7.8%) YTD
- [ ] Import **phone clicks** (255 YTD) as conversion action
- [ ] Deploy **n8n Customer Match** sync (640 purchasers, weekly refresh)

## Data Still Needed

- [ ] Google Ads state-level location report (national campaign)
- [ ] Shopify **revenue** by state (current export is customer counts only)
- [ ] Merchant Center diagnostics / price competitiveness export
