# BGW Doors Test Results

## Running Tests

### Summer Warehouse Sale — 20% Auto-Applied at Checkout (launched 2026-07-02)

| Metric | Before (Jun 2–Jul 1 baseline) | After | Verdict |
|---|---|---|---|
| Offer mechanism | Compare-at + sale + `FREESHIP2026` coupon | Single price + 20% auto at checkout | **Running** |
| Shopify coupon redemptions | 1 (`FREESHIP2026`) | TBD (auto discount) | **Running** |
| Promo clarity (site-wide) | Conflicting 15% vs 20% + coupon | Unified auto-applied messaging | **Running** |
| Google Ads ROAS / CPA | 1.36 ROAS / $963 CPA | TBD | **Running** |
| Merchant Center promo | Sale price avg ~13% off | MC promotion live (pending feed re-export) | **Running** |

**Hypothesis:** A true 20% auto-applied checkout discount on full shelf price removes coupon friction and aligns ad promise with checkout, lifting conversion rate vs the retired compare-at + shipping coupon model.

**Before metrics (2026-06-02 to 2026-07-01):** $9,623 spend, ~10 conv., 1.36 ROAS, PMax CPA ~$1,952, post–Jun 18 sale ROAS 0.22.

**Review date:** ~2026-08-02 (30 days).

---

## Queued Tests

### T3 — Product reviews on top 10 ad-driven SKUs

- **Hypothesis:** Social proof lifts CR on high-ticket cold traffic without changing price.
- **Before metrics needed:** PDP bounce rate, time on page, CR by landing page (GA4).

### T4 — Default variant = lowest-price single door on ad landing SKUs

- **Hypothesis:** Reducing price shock from "From" to default variant improves add-to-cart.
- **Before metrics needed:** Variant selection rate, cart abandonment on FD05-class products.

---

## Completed Tests

### Summer Warehouse Sale — FREESHIP2026 (2026-06-18 to 2026-07-02) — **FAILED**

| Metric | Result | Verdict |
|---|---|---|
| Shopify coupon redemptions | 1 | **Failed** |
| Promo clarity | Conflicting 15% vs 20% messaging | **Failed** |
| Google Ads ROAS (post-launch) | 0.22 (Jun 18–Jul 1) | **Failed** |

**Conclusion:** Retired 2026-07-02. Replaced with auto-applied 20% checkout discount. See Change-Log.md.

---

## Cancelled / Superseded

### T1 — Automatic free shipping (no coupon)

- **Status:** Superseded by 2026-07-02 offer (auto 20% at checkout replaces shipping-coupon model).

### T2 — True price reduction on hero SKUs

- **Status:** Partially addressed — 20% auto-applied at checkout on full shelf price achieves real discount vs old ~5% compare-at spread. Price vs competitors still TBD (benchmarking queued in Next-Actions.md).
