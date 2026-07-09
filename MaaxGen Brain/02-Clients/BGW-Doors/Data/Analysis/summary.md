# BGW Data Analysis Summary

**Analysis date:** From merged GitHub exports

## Top Findings

1. **Tracking is the #1 blocker.** GA4 shows 44 purchases YTD vs 566 checkouts (92% checkout abandonment). Google Ads reports 711 conversions over 720 days — likely inflated by micro-conversions, not purchases. Verify purchase is the only Primary action.

2. **California dominates customers** — 260 of 640 (41%). National hot states: FL (41), NY (38), NJ (22), VA (18), TX (17). Use these for national PMax geo targeting.

3. **CA ads waste identified.** San Diego County: $2,182 spend, ~0 Shopify customers. Santa Clara County: $857. Ontario (10 customers): only $59 spend — under-invested in a proven market.

4. **Feed uses wrong titles.** Featured products have good SEO titles but default titles lack "Pre-Hung" and "Front Door." Zero custom labels set. Merchant Center is not getting optimized data.

5. **Slab doors outselling pre-hung in GA4.** Top item: "Slab Solid Wood Door - M300 Series" (10 units). PMax may be pushing wrong products.

## Recommended Immediate Actions

| Priority | Action | Owner |
|----------|--------|-------|
| P0 | Audit conversion actions — purchase only as Primary | Brent |
| P0 | Configure Google & YouTube app to sync SEO title/description | Brent/Kevin |
| P1 | Export **state-level** location report for US national PMax | Brent |
| P1 | Exclude CA counties: San Diego County, Santa Clara County, Fresno County (test) | Brent (after approval) |
| P1 | Add custom labels in Shopify feed | Brent |
| P2 | Investigate checkout abandonment (shipping cost surprise?) | Kevin |
| P2 | Import phone calls as secondary then primary conversion | Brent |
| P2 | n8n Customer Match sync from Shopify | Brent |

## Files Generated

- `Analysis/geo-reconciliation.md`
- `Analysis/feed-title-audit.md`
- `Analysis/ga4-snapshot.md`

## Data Gaps

- State-level Google Ads location report for national campaign ($119k in "Other locations")
- Shopify revenue by state (export has customer counts, not dollar revenue)
- Merchant Center diagnostics export
