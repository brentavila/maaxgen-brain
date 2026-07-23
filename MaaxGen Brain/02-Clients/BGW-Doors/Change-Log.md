# BGW Doors Change Log

## 2026-07-02 (offer relaunch)

### Change Made

Relaunched Summer Warehouse Sale with new offer architecture:

- Removed compare-at and sale price split in Shopify; single shelf price (compare-at = sell price)
- Added **20% off automatic discount at checkout** in Shopify (no manual coupon)
- Created/updated **Merchant Center promotion**
- Updated **website** copy to "20% Off In-Stock Doors — Auto Applied At Checkout"
- Retired **`FREESHIP2026`** model (compare-at + sale + free-shipping coupon)

### Reason For Change

Prior offer failed: 1 coupon redemption, conflicting site messaging, feed showed ~13% discount while ads claimed 20%, post–Jun 18 ROAS 0.22. Diagnostic recommended simplifying offer so ad promise matches checkout with no coupon friction.

### Expected Outcome

Higher checkout completion on ad traffic; clearer 20% savings story; improved trust vs old compare-at + hidden shipping math; lift in conversion rate and ROAS before re-scaling PMax.

### Result

Pending — monitor 30 days from 2026-07-02. Before metrics: account ROAS 1.36, CPA $963, PMax CPA ~$1,952.

### Notes

- Total customer savings intended to match prior offer; only the **delivery mechanism** changed
- Shelf prices now show full price (e.g. FD05 $2,360, M577 $3,120); discount visible at checkout
- Next: re-export MC feed, align PMax ad assets, pull GA4/Shopify funnel after change

---

## 2026-07-02 (diagnostic)

### Change Made

Root-cause diagnostic: Google Ads profitability investigation (last 30 days requested; live account data not yet available via MCP).

### Reason For Change

Sales and ad performance below target. Client hypothesis: trust vs pricing vs promo vs site CRO. June 18 Summer Warehouse Sale (`FREESHIP2026`) has only 1 coupon redemption in Shopify.

### Expected Outcome

Prioritized fix list before scaling or restructuring Google Ads spend.

### Result

30-day Google Ads + Merchant Center exports analyzed (2026-07-02). Account ROAS **1.36**, CPA **$963**. Post–Jun 18 sale ROAS **0.22**. See Google-Ads.md baseline and Test-Results.md.

### Notes

**Google Ads data (Jun 2–Jul 1, 2026):**

- Total spend **$9,623** → **~10 conversions** → **$13,128 conv. value** → ROAS **1.36**
- **PMax US** consumed 81% of budget ($7,772) at CPA **$1,952** (~0.03% click CVR)
- **Brand Search** best performer: 5 conv., CPA **$147**
- **Remarketing Display**: $303, **0 conversions** — pause candidate
- **PMax spend +114%** vs prior 30d while performance worsened
- **Post-sale (Jun 18+):** $5,014 spend → 4 conv. → $1,100 value → ROAS **0.22**
- Brand query **`bgw doors reviews`** active (trust research, 0 conv.)
- Mobile = 75% of spend

**Merchant Center feed (292 variants):**

- 66 out of stock still in feed; 78 missing condition
- Avg sale discount **12.8%**, not 20%
- Fiberglass in-stock avg **$3,331**; wood **$4,377**

**Findings (evidence-based, site + ads + feed):**

1. **Pricing likely primary blocker for cold Shopping/PMax traffic.** Comparable fiberglass speakeasy pre-hung singles: BGW ~$2,238 vs Doors4Home ~$1,170–$1,570. Wood entry doors: BGW from ~$2,846 vs Home Depot pre-hung mahogany ~$1,390–$1,528.
2. **Promo is structurally weak, not just a messaging problem.** The "20% off" is mostly free shipping via coupon on an already-modest compare-at discount (~5% on hero fiberglass SKUs). Coupon requires manual entry; only 1 use confirms it is not driving behavior.
3. **Conflicting offer copy on site** (15% auto-apply vs 20% coupon) creates confusion and erodes trust.
4. **Trust/CRO gaps on PDPs:** no live product reviews; placeholder review sections; harsh return policy (48 hr, 20% restocking); knocked-down pre-hung assembly requirement not surfaced until PDP.
5. **Google Ads API not connected for BGW** (`GOOGLE_ADS_CUSTOMER_ID_BGW` empty; account not under MAAXGEN MCC). Cannot validate campaign ROAS, product concentration, or wasted spend until connected.
6. **Conversion tracking unverified** (Shopify Google & YouTube app). Smart Bidding signal health unknown — step 1 of audit order-of-operations is blocked.

**Recommended sequence:** Fix offer/pricing clarity → CRO/trust on PDP + cart → verify tracking → then optimize PMax (product-level, geo, negatives, assets).

---

## 2026-06-30

### Change Made

Set up client folder.

### Reason For Change

Create source of truth for future AI analysis.

### Expected Outcome

Better consistency across ChatGPT, Claude, Cursor, and Gemini.

### Result

Pending.

### Notes

Initial setup.
