# BGW Doors — Next Actions

From data analysis (Jul 9, 2026). Full reports in `Data/Analysis/`.

## P0 — Do Before Any Budget or Geo Changes

- [ ] **Conversion tracking audit** — Confirm purchase is the only Primary action. GA4 shows 44 purchases YTD; Ads shows 711 conversions over 720 days (likely micro-conversion inflation).
- [ ] **Switch Merchant Center feed to SEO title + SEO description** in Shopify Google & YouTube app. Default titles lack "Pre-Hung" and "Front Door"; SEO titles are already written.

## P1 — Geo (after tracking verified)

- [ ] Export **state-level** Google Ads location report for national PMax (US excl. CA). Current report hides ~$119k in "Other locations."
- [ ] **National Tier A states** to prioritize (≥10 Shopify customers): FL, NY, NJ, VA, TX, NC, PA, WA, GA, MD, AZ, MI, NV, AL, IL
- [ ] **CA exclude test** (≥$100 spend, ≤1 customer): San Diego County, Santa Clara County, Fresno County
- [ ] **CA scale** (proven customers, under-spent): Ontario (10 customers, $59 spend), Inland Empire cities (Fontana, Rancho Cucamonga, Chino)

## P1 — Feed & PMax

- [ ] Populate **custom labels** in Shopify (material, margin, pre-hung vs slab, in-stock)
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
