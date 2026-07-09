# BGW Doors — Sales Decline Diagnostic & Recovery Plan

**Prepared:** July 9, 2026  
**Client:** BGW Doors (Kevin, Paul)  
**Budget:** ~$8,500–$10,000/mo Google Ads + Microsoft + Amazon  
**Primary channel:** Performance Max (Shopping) — US (excl. CA) + California + Brand Search  

> **Data analysis complete (Jul 9, 2026):** See `Data/Analysis/summary.md`, `geo-reconciliation.md`, `feed-title-audit.md`, and `ga4-snapshot.md`. Key finding: **tracking must be fixed first** — GA4 shows 44 purchases YTD vs 566 checkouts; Ads likely optimizing on inflated conversions.

---

## Executive Summary

Kevin and Brent are right to suspect Google Ads is underperforming, but **the root cause is likely a stack of compounding problems**, not one broken lever. Spending more will not fix:

1. **Unverified conversion tracking** — Smart Bidding optimizes toward whatever signal it receives. If purchase values, deduplication, or micro-events are wrong, PMax will chase the wrong users.
2. **Feed-to-intent mismatch** — Product titles emphasize model numbers ("Solid Wood Exterior Door M580E") instead of how buyers search ("pre-hung wood front door," "exterior entry door with sidelights"). Slab doors may be cannibalizing pre-hung traffic.
3. **Geo waste** — Ads likely reach states/cities with clicks but no historical Shopify revenue. Without reconciling Shopify sales-by-location against Google spend-by-location, exclusions are guesswork.
4. **Weak audience signals** — Manual Customer Match uploads are stale. PMax has limited first-party data to find lookalikes of actual buyers.
5. **High-ticket CRO gap** — Cold Shopping traffic landing on variant-heavy product pages with shipping uncertainty on oversized freight.

**This plan follows MaaxGen's Google Ads Optimization Playbook order:** fix data → fix bleed → fix geo → fix assets/feed → then restructure bidding.

> **Data gap:** ~~Shopify customer-by-location export (720 days), `product_export_1.csv`, and GA4 YTD export were referenced but are not yet in `02-Clients/BGW-Doors/Data/`.~~ **Resolved** — exports merged. Analysis in `Data/Analysis/`.

---

## Phase 0 — Baseline & "Why Are Sales Down?" Framework

### Hypotheses to Test (ranked by likelihood)

| # | Hypothesis | How to confirm | If true, fix |
|---|-----------|----------------|--------------|
| H1 | Conversion tracking is inaccurate or thin | Tag Assistant, GA4 DebugView, Ads conversion diagnostics, Shopify order match | Phase 1 |
| H2 | PMax shows products to wrong geos | Shopify revenue-by-state/city vs Ads location report | Phase 2 |
| H3 | Feed titles/descriptions don't match search intent | Search terms insights + title audit vs queries | Phase 3 |
| H4 | Slab/low-intent products consume budget | Product performance by item ID + custom labels | Phase 3–4 |
| H5 | Product concentration — Google favors few SKUs | Top 10 products by impressions vs revenue | Phase 4 |
| H6 | Price/shipping competitiveness | Merchant Center price benchmarks + landing page shipping clarity | Phase 3 |
| H7 | Audience signals are stale/empty | Audience insights + Customer Match list age | Phase 4–5 |
| H8 | Site CVR dropped (not just ads) | GA4 funnel YTD vs prior year: sessions → ATC → checkout → purchase | Phase 6 |

### Data to Collect (first 7 days)

Place all exports in `02-Clients/BGW-Doors/Data/`:

**From Shopify (720 days)**
- [ ] Customers by billing/shipping state and city (already exported — add to Data folder)
- [ ] Orders with revenue, AOV, product SKU, discount code, shipping state
- [ ] Product conversion rate by SKU

**From Google Ads (last 90 days + YoY compare)**
- [ ] Campaign report (both PMax campaigns + Brand)
- [ ] Asset group report
- [ ] Product performance (Shopping) — item ID level
- [ ] Listing group report
- [ ] Location report (city + state)
- [ ] Search terms insights
- [ ] Audience insights
- [ ] Conversion action report
- [ ] Landing page report

**From Merchant Center**
- [ ] Product diagnostics / Needs attention
- [ ] Price competitiveness report
- [ ] Full product feed export
- [ ] Popular products report

**From GA4 (YTD + prior year same period)**
- [ ] Ecommerce funnel: view_item → add_to_cart → begin_checkout → purchase
- [ ] Revenue by source/medium (google/cpc vs organic vs direct)
- [ ] Landing page report
- [ ] Item revenue report
- [ ] Geo: city/region

### Year-over-Year Comparison Metrics

| Metric | Source | Why it matters |
|--------|--------|----------------|
| Shopify revenue & order count | Shopify | Ground truth |
| MER (total ad spend / Shopify revenue) | Shopify + ad platforms | Are ads profitable holistically? |
| Google Ads cost, conv value, ROAS | Google Ads | Platform view (may lie if tracking broken) |
| GA4 purchase rate by channel | GA4 | Is google/cpc CVR down or just volume? |
| AOV | Shopify | High-ticket mix shift? |
| ATC rate, checkout rate | GA4 | CRO vs traffic quality |
| Top states by revenue | Shopify | Geo truth |
| Top products by revenue | Shopify | Feed priority |
| Feed disapprovals / warnings | Merchant Center | Eligibility |

---

## Phase 1 — Conversion Tracking & Signal Health (DO THIS FIRST)

**Status per Conversion Tracking Playbook: NO-GO until verified.**

Current setup: purchase tracking via **Shopify Google & YouTube app**. Offline conversions (calls, emails, showroom) not measured.

### 1.1 Conversion Action Inventory

Audit every action in Google Ads → Goals → Conversions:

| Action | Primary? | Source | Count | Value | Keep / Fix / Remove |
|--------|----------|--------|-------|-------|---------------------|
| Purchase | ? | Shopify app | ? | Dynamic? | TBD |
| Add to cart | ? | ? | ? | ? | Likely secondary |
| Begin checkout | ? | ? | ? | ? | Likely secondary |
| Phone call | ? | ? | ? | ? | Not set up |
| Form submit | ? | ? | ? | ? | Not set up |
| Page view / engagement | ? | ? | ? | ? | Remove if primary |

**Rules for BGW (ecom national + local leads):**

- **Primary (national PMax):** Purchase only, with dynamic transaction values, count = Every
- **Primary (CA local PMax, if lead-focused):** Qualified phone call (≥90 sec) + form submission, count = One
- **Secondary:** Add to cart, begin checkout, page views, micro-engagements
- **Never** count the same event from both GA4 import AND Shopify app tag

### 1.2 Verification Checklist

- [ ] Tag Assistant: purchase fires on order confirmation with correct value and transaction ID
- [ ] GA4 DebugView: `purchase` event matches Shopify order (value, items, currency)
- [ ] Google Ads → Diagnostics: "Recording conversions" with recent timestamps
- [ ] Spot-check 10 orders: Shopify revenue vs Ads attributed revenue (±5%)
- [ ] Check for duplicate purchase counting (common with Shopify app + GA4 import)
- [ ] Enhanced Conversions for Web: enabled and verified
- [ ] Consent mode: confirm behavior if cookie banner affects tracking

### 1.3 New Events to Add (after purchase is verified)

| Event | Purpose | Priority |
|-------|---------|----------|
| `qualified_lead` | Form + call for CA installation | High |
| `high_value_cart` | ATC on wood doors >$3,500 | Medium |
| `checkout_started` | Secondary signal for PMax | Medium |
| Offline purchase upload | Showroom/in-store closes | Medium |

### 1.4 Attribution Settings

- **Model:** Data-driven (unless volume too low)
- **Click window:** 30 days for high-ticket doors (consider 60 if data supports)
- **Engaged-view conversions:** Review YouTube contribution

**Gate:** Do not change tROAS, budgets, geo exclusions, or major PMax restructure until Phase 1 shows **go**.

---

## Phase 2 — Geographic Optimization (Shopify Truth vs Google Spend)

### 2.1 Analysis Method

1. Export Shopify orders (720 days) → revenue by **shipping state** and **shipping city**
2. Export Google Ads location report (90 days) → cost, conversions, conv value by city/state
3. Build reconciliation table:

| State/City | Shopify Revenue | Shopify Orders | Ads Cost | Ads Conv Value | Ads ROAS | Action |
|------------|----------------|----------------|----------|----------------|----------|--------|
| ... | ... | ... | ... | ... | ... | TBD |

4. Classify each location:
   - **Tier A — Scale:** High Shopify revenue + acceptable Ads ROAS
   - **Tier B — Monitor:** Some revenue, mixed Ads performance
   - **Tier C — Exclude candidate:** High Ads spend, zero/low Shopify orders in 720 days
   - **Tier D — Local only:** CA metros with installation leads (separate from national)

### 2.2 Expected Patterns (to validate with data)

National freight shipping favors:
- Sun Belt, Texas, Southeast, Midwest suburbs (homeowners with renovation budget)
- States with high home values and owner-occupied housing

Likely waste:
- States with very low historical order volume despite high click volume
- Cities with high CTR but zero purchases (price shoppers, wrong intent)
- Rural areas where freight cost surprises kill conversion at checkout

### 2.3 Campaign Geo Strategy

**Current:** PMax US (excl. CA) + PMax CA

**Recommended evolution (after data review):**

| Campaign | Geo | Goal | Notes |
|----------|-----|------|-------|
| PMax — National Wood Heroes | Tier A states only (start with top 15–20 states by Shopify revenue) | Purchase tROAS | Wood = highest margin |
| PMax — National Full Catalog | Tier A + B states | Purchase tROAS | Broader feed once wood campaign stable |
| PMax — California Ecom | CA (excl. LA install radius if needed) | Purchase | Keep separate — already exists |
| PMax — LA Installation Leads | LA/Ontario radius (~50 mi) | Qualified leads | Different conversion actions |
| Brand Search | National | Purchase + leads | Protect brand |

**Important:** PMax does not use city bid adjustments. Levers are **location exclusions**, **separate campaigns with different geo targets**, and **audience signals**.

### 2.4 Location Exclusion Process

1. Only exclude cities/states with **statistical confidence** (e.g., >$200 spend and 0 orders in 720 days Shopify data)
2. Log every exclusion in Change-Log.md with reason
3. Re-review quarterly — don't permanently exclude a market that was never given a fair feed

---

## Phase 3 — Merchant Center & Shopify Feed Optimization

Merchant Center quality directly controls PMax Shopping performance. BGW's current titles (e.g., "Solid Wood Exterior Door M580E") under-index on high-intent keywords.

### 3.1 Title Formula (Google Best Practices)

Per [Google title guidelines](https://support.google.com/merchants/answer/6324415):

- 1–150 characters; front-load the most important details (truncation happens in ads)
- Include: material, door type, configuration, size, finish, brand
- Match landing page — **do not** put "pre-hung" in feed if the page doesn't say pre-hung
- No promo text in title ("free shipping," "20% off")
- Distinguish variants clearly

**Recommended BGW title structure:**

```
[Pre-Hung] [Material] [Front/Entry] Door [Model] | [Config] | [Size] | BGW Doors
```

### 3.2 Pre-Hung vs Slab — Strategic Decision

| Factor | Pre-Hung (recommended focus) | Slab |
|--------|------------------------------|------|
| BGW differentiator | Factory-direct pre-hung, in stock | Commodity, DIY buyer |
| Buyer intent | Ready to install, higher AOV | Price-sensitive, wrong fit often |
| Search demand | "pre hung wood front door," "entry door with frame" | "door slab," "replacement slab" |
| Feed strategy | **Push** — custom label `hero`, dedicated asset group | **Limit** — custom label `monitor` or separate low-budget group |

**Action:** Audit how many Shopify products are slab vs pre-hung. If Merchant Center feed pulls default product title (not SEO title), update **SEO title** in Shopify for Shopping intent. Confirm Google & YouTube app syncs SEO fields or configure supplemental feed.

### 3.3 Title Rewrite Examples

| Current (likely) | Optimized Shopping/SEO Title |
|------------------|------------------------------|
| Solid Wood Exterior Door M580E | Pre-Hung Wood Front Door M580E \| Single \| African Mahogany \| 36x80 |
| Fiberglass Exterior Door FD05 | Pre-Hung Fiberglass Entry Door FD05 \| Craftsman Style \| 36x80 |
| Iron Door Exterior # ID03 | Pre-Hung Iron Front Door ID03 \| Double \| Security Glass |
| Solid Wood Entry Door-M002 | Pre-Hung Wood Entry Door M002 \| Single With Sidelights |

*Verify exact sizes/configs on each product page before publishing.*

### 3.4 Description Optimization

Per [Google feed optimization tips](https://support.google.com/merchants/answer/7380908):

- Lead with material, pre-hung inclusion (frame, hinges, threshold), and sizing
- Include: African Mahogany / fiberglass / iron, single vs double, sidelight config
- Shipping: "Nationwide freight shipping in 5–8 business days" (if true on page)
- Installation: "Professional installation available in Los Angeles / Ontario, CA area"
- No competitor mentions, no promo codes in description
- Match landing page copy exactly

### 3.5 Custom Labels (implement in Shopify → feed)

Use Merchant Center custom labels for PMax listing group control:

| Label | Values | Use |
|-------|--------|-----|
| `custom_label_0` — Material | wood, fiberglass, iron | Asset group splits |
| `custom_label_1` — Margin tier | high, medium, low | Budget priority |
| `custom_label_2` — Performance | hero, stable, test, poor | Quarterly refresh from Ads data |
| `custom_label_3` — Door type | pre-hung, slab, double, sidelight | Intent control |
| `custom_label_4` — Inventory | in-stock, custom, clearance | Promo alignment (FREESHIP2026) |

**How to set in Shopify:** Use Google & YouTube app metafields, or a feed app (DataFeedWatch, Mulwi, etc.) if the native app doesn't support custom labels. Alternatively, supplemental feed via Google Sheets (short term) → n8n (long term).

### 3.6 Other Feed Fixes

- [ ] **Google product category:** `Hardware > Building Materials > Doors > Exterior Doors` (verify exact taxonomy ID)
- [ ] **Product type:** `Home & Garden > Doors > Exterior Entry Doors > Wood Front Doors` (3+ levels deep)
- [ ] **GTIN/MPN/brand:** Submit MPN = model number, brand = BGW Doors
- [ ] **Additional images:** Installed lifestyle shots, detail close-ups (up to 10)
- [ ] **Price accuracy:** Sale price + `sale_price_effective_date` for 20% warehouse sale
- [ ] **Shipping:** Free shipping annotation — configure in Shopify + Merchant Center per [Shopify delivery best practices](https://support.google.com/merchants/answer/14238138)
- [ ] **Transit time:** 5–8 business days as custom label or shipping settings
- [ ] **Product reviews:** Enable in Merchant Center if not active (trust for high-ticket)

### 3.7 Featured Collection Priority

For `product_export_1.csv` (featured collection): optimize these SKUs first — they are likely getting the most impressions. Sequence:

1. Fix disapprovals/warnings
2. Rewrite titles/descriptions (wood first — most profitable)
3. Add custom labels
4. Add lifestyle images
5. Verify price competitiveness in Merchant Center

---

## Phase 4 — Performance Max Strategy

### 4.1 Current State

- PMax Sales — US (excl. California)
- PMax Sales — California
- Brand Search

### 4.2 Recommended Target Structure (implement in waves after tracking verified)

**Wave 1 — Feed + labels (no campaign splits yet)**
- Single national PMax, but custom labels and improved titles
- Add audience signals (Phase 4.4)

**Wave 2 — Material splits (when budget supports ~$100+/day per campaign)**

| Campaign | Budget % | Listing Groups | tROAS Target |
|----------|----------|----------------|--------------|
| PMax — Wood Doors | 45% | custom_label_0 = wood | Start 15–20% below account avg, tighten monthly |
| PMax — Fiberglass Doors | 25% | custom_label_0 = fiberglass | Same |
| PMax — Iron Doors | 15% | custom_label_0 = iron | Same |
| PMax — Clearance/Sale | 10% | custom_label_4 = clearance OR sale items | Aggressive tROAS OK |
| PMax — California | 5% | Geo = CA | Separate goal mix if leads matter |

**Wave 3 — Hero product isolation (if concentration problem confirmed)**
- Dedicated asset group or campaign for top 10 wood SKUs by Shopify revenue
- Prevents Google from burying winners under long-tail slab SKUs

### 4.3 Asset Group Segmentation

Each asset group should have aligned: **products + creative + audience + search themes + URL**.

| Asset Group | Products | Search Themes | Final URL | Creative Angle |
|-------------|----------|---------------|-----------|----------------|
| Wood Pre-Hung Singles | Wood, single, pre-hung | pre hung wood front door, mahogany entry door, solid wood exterior door | /collections/wood-front-doors | Craftsmanship, African Mahogany, curb appeal |
| Wood Double + Sidelights | Wood, double, sidelight | double front wood doors, entry door with sidelights | /collections/wood-front-doors | Architectural, luxury renovation |
| Fiberglass Entry | Fiberglass, all configs | fiberglass front door, craftsman entry door | /collections/fiberglass-front-doors | Low maintenance, climate durability |
| Iron Security | Iron, all configs | iron front door, wrought iron entry door | /collections/iron-front-doors | Security, statement piece |
| In-Stock / Sale | custom_label_4 = in-stock | in stock entry doors, exterior door sale | Homepage or sale collection | 20% warehouse sale, factory direct |
| Slab (limited) | Slab only | wood door slab (only if keeping) | /collections/slab-doors | DIY — deprioritize budget |

**Per asset group, include:**
- 5+ headlines mentioning material + "Pre-Hung" + "Factory Direct"
- 5+ descriptions with shipping time + trust (since 1992, 1M doors sold)
- 15+ images: product on white + installed lifestyle
- Video if available (even 15-sec product spin)
- Audience signal (see 4.4)

### 4.4 Listing Group Segmentation

Inside each asset group, use listing groups to subdivide:

```
All products
├── Material (custom_label_0)
│   ├── Wood
│   │   ├── Pre-Hung (custom_label_3)
│   │   │   ├── Hero (custom_label_2 = hero) → bid boost via tROAS
│   │   │   └── Other
│   │   └── Slab → monitor/exclude if poor
│   ├── Fiberglass
│   └── Iron
└── Everything else → low priority
```

**Exclude from national PMax:**
- Out of stock (automatic)
- Slab doors (test exclusion if data shows waste)
- Products with >$500 spend and 0 conversions in 90 days (after tracking fixed)

### 4.5 Audience Signals

Audience signals guide PMax AI — they are not hard targeting.

**First-party lists (upload via Customer Match):**

| Audience | Source | Refresh | Use |
|----------|--------|---------|-----|
| Past purchasers (720 days) | Shopify | Weekly via n8n | Observation + similar audiences |
| High AOV purchasers (>$4,000) | Shopify | Weekly | Wood door lookalike signal |
| Cart abandoners (30 days) | Shopify/GA4 | Daily | Remarketing signal |
| Checkout abandoners (14 days) | Shopify/GA4 | Daily | Highest intent |
| Email subscribers (no purchase) | Shopify/Klaviyo | Weekly | Prospecting signal |
| California purchasers | Shopify | Weekly | CA campaign signal |

**Custom segments (search-based):**

- People who searched: "wood front door," "pre hung entry door," "fiberglass exterior door," "iron entry door," "double front door with sidelights"
- Competitor intent: "doors4home," "eto doors," "us door and more" (monitor lead quality)
- In-market: Home Improvement, Doors & Windows
- Home renovation / luxury homeowner affinities

**Exclusions:**
- Past purchasers from prospecting-only asset groups (if running separate remarketing)
- "Contractor wholesale" if lead quality is poor (validate with data)

### 4.6 Bidding & Budget (only after Phase 1 go)

- **National PMax:** Maximize conversion value → transition to tROAS once 30+ purchases/30 days per campaign
- **Initial tROAS:** Set 15–20% below trailing 30-day ROAS, adjust monthly in 10–15% steps
- **Brand Search:** Manual CPC or Target Impression Share (top of page)
- **Do not** increase budget until ROAS or CPA is stable for 2+ weeks

---

## Phase 5 — Customer List Automation (n8n)

Shopify plan may not include native Google audience sync. **n8n is the right path.**

### 5.1 Architecture

```
Shopify (orders/customers)
    → n8n workflow (scheduled daily)
        → Transform to Google Ads Customer Match format
            → Google Ads API upload (UserList)
                → Auto-apply to PMax audience signals
```

Reference: `13-Tools/API Connections.md`

### 5.2 Workflow: Purchaser List Sync

**Trigger:** Cron, daily at 2 AM PT

**Steps:**
1. Shopify Admin API: pull customers with orders in last 720 days (email, phone, address, order value)
2. Filter: `orders_count >= 1` and `total_spent > 0`
3. Hash PII (SHA-256): email, phone (E.164), first name, last name, zip
4. Upload to Google Ads Customer Match list: `BGW - Purchasers 720d`
5. Log execution in n8n; alert on failure

**Scopes needed:**
- Shopify: `read_customers`, `read_orders`
- Google Ads: Customer Match upload permission (account must meet eligibility: 90+ days, $50k+ spend lifetime — BGW likely qualifies)

### 5.3 Additional Workflows

| Workflow | Frequency | List Name |
|----------|-----------|-----------|
| High AOV purchasers (>$4K) | Weekly | BGW - High Value Buyers |
| Cart abandoners | Daily | BGW - Cart Abandon 30d |
| CA purchasers | Weekly | BGW - California Buyers |
| Offline leads → OCI | Real-time webhook | BGW - Qualified Leads |

### 5.4 Interim Manual Process (until n8n live)

1. Export Shopify customers CSV weekly
2. Upload to Google Ads Audience Manager → Customer Match
3. Apply as audience signal to all PMax asset groups
4. Document upload date in Change-Log.md (stale >14 days = degraded signal)

---

## Phase 6 — CRO & Landing Page Alignment

High-ticket doors need trust before purchase. Shopping sends cold traffic.

### 6.1 Product Page Checklist (per SKU)

- [ ] Title matches feed ("Pre-Hung Wood Front Door...")
- [ ] Price visible above fold with sale price if applicable
- [ ] Shipping cost/timeline visible before ATC (freight surprises = abandonment)
- [ ] "What's included" section: pre-hung frame, hinges, threshold, weatherstripping
- [ ] Size selector defaults to most popular (36x80)
- [ ] 6+ images including installed photo
- [ ] Reviews/testimonials
- [ ] Trust badges: Since 1992, 1M doors sold, factory direct
- [ ] Mobile: CTA sticky, images swipeable

### 6.2 Collection Page SEO (supports Shopping + organic)

- Wood, fiberglass, iron collection pages should use H1s with "Pre-Hung [Material] Front Doors"
- Add FAQ schema (already have good FAQ content on homepage — extend to collections)

---

## Phase 7 — Measurement & Reporting Cadence

### Weekly (Brent)

- Ads spend vs Shopify revenue (MER)
- Top 10 products by spend and by Shopify revenue (reconciliation)
- New feed disapprovals
- Conversion tracking health check

### Monthly (Kevin + Brent)

- Full geo reconciliation table update
- Asset group performance
- Feed title A/B results (measure CTR + CVR change)
- Test results logged to Test-Results.md

### KPI Targets (set after baseline — placeholders)

| KPI | Current (TBD) | 90-Day Target |
|-----|---------------|---------------|
| Shopify revenue (Google attributed) | TBD | +25% |
| MER | TBD | Improve 20% |
| Purchase CVR (google/cpc) | TBD | +0.3% absolute |
| Wood door ROAS | TBD | Profitable at margin |
| Feed approval rate | TBD | 98%+ |

---

## Implementation Sequence

```
Week 1–2:  Phase 0 (data collection) + Phase 1 (tracking audit)
Week 2–3:  Phase 2 (geo analysis) + Phase 3 (feed titles, labels — wood first)
Week 3–4:  Phase 5 (n8n MVP — purchaser list) + Phase 4 Wave 1 (audience signals)
Week 4–6:  Phase 4 Wave 2 (material campaign splits) if data supports
Week 6–8:  Phase 6 (CRO on top 10 SKUs) + Phase 4 Wave 3 (hero isolation)
Ongoing:   Phase 7 reporting + quarterly geo/feed refresh
```

**Nothing in Phases 2–6 goes live without explicit approval from Brent/Kevin.**

---

## Questions for Kevin / Paul

1. **Shopify plan level** — Which plan? Does Google & YouTube app support SEO title override for feed, or only default product title?
2. **Margin data** — Can we get COGS or margin by product category for true profit-based ROAS?
3. **Slab door strategy** — Keep advertising slabs nationally, or deprioritize to focus budget on pre-hung?
4. **California split** — Is the CA PMax campaign meant for ecom, installation leads, or both? Different conversion actions needed.
5. **Showroom/offline sales** — Rough % of revenue from phone/showroom vs online checkout? Critical for tracking scope.
6. **Freight shipping** — Flat rate or calculated? Any states with delivery restrictions or surcharge?
7. **Historical baseline** — What was monthly Shopify revenue at peak (~2 years ago) vs now? Same ad spend?
8. **Competitor intel** — Any known accounts outbidding on Shopping for wood doors?

---

## Data Request — Add to `02-Clients/BGW-Doors/Data/`

Please add these files so quantitative analysis can begin:

- [ ] `shopify-customers-by-location-720d.csv`
- [ ] `product_export_1.csv` (featured collection)
- [ ] `ga4-ytd-2026.csv` (or export key reports)
- [ ] Google Ads campaign export (90 day)
- [ ] Google Ads product performance export
- [ ] Google Ads location export
- [ ] Merchant Center product diagnostics export

---

## Related Vault Files

- [[Client-Brief]]
- [[Google-Ads]]
- [[Merchant-Center]]
- `04-Playbooks/Google Ads Optimization Playbook.md`
- `04-Playbooks/Conversion Tracking Playbook.md`
- `13-Tools/API Connections.md`
