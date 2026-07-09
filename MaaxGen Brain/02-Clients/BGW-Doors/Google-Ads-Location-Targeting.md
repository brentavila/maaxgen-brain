# BGW Doors — Google Ads Location Targeting

**Draft for Brent/Kevin approval. Do not apply until conversion tracking audit is complete (P0).**

Campaigns covered:
- **Sales-Performance Max-19** (national freight / US excl. CA)
- **Performance Max: California** (California ecom + local overlap)

Brand Search (`Search - Brand`) is **not** restricted by this plan. It is performing at ~$99 CPA and should remain **United States** broad.

---

## Global Settings (Both Campaigns)

Apply these before changing locations:

| Setting | Value | Why |
|---------|-------|-----|
| **Location options** | **Presence: People in or regularly in your targeted locations** | Avoids "interest in California" clicks from other states |
| **NOT** | Presence or interest | That option wastes national budget on researchers, not buyers |
| **Goal** | Purchases (after tracking verified) | One Primary purchase action with dynamic value |
| **Bid strategy** | Maximize conversion value → tROAS later | Only after 30+ purchases/month per campaign |

**Where to set:** Campaign → Settings → Locations → Location options → Edit → Select **Presence**.

---

## Campaign 1: Sales-Performance Max-19 (Nationwide)

### Strategy

Use **positive targeting** (include only proven states). Do not target all United States and hope exclusions work.

**Exclude California entirely** — it has its own campaign (`Performance Max: California`).

### Step-by-Step in Google Ads

1. Open campaign **Sales-Performance Max-19**
2. Go to **Settings → Locations**
3. Remove **United States** if it is the only target (if present)
4. Click **Enter another location** → search and **Include** each state below
5. Confirm **California is NOT included**
6. Set location option to **Presence** (see global settings)
7. Save

### States to INCLUDE (15 states — Tier 1 + Tier 2)

Based on 720-day Shopify customer data (≥10 customers each):

| # | State | Shopify Customers | Tier |
|---|-------|------------------:|------|
| 1 | Florida | 41 | Scale |
| 2 | New York | 38 | Scale |
| 3 | New Jersey | 22 | Scale |
| 4 | Virginia | 18 | Scale |
| 5 | Texas | 17 | Scale |
| 6 | North Carolina | 15 | Scale |
| 7 | Pennsylvania | 15 | Scale |
| 8 | Washington | 15 | Scale |
| 9 | Georgia | 15 | Scale |
| 10 | Maryland | 13 | Tier A |
| 11 | Arizona | 11 | Tier A |
| 12 | Michigan | 11 | Tier A |
| 13 | Nevada | 10 | Tier A |
| 14 | Alabama | 10 | Tier A |
| 15 | Illinois | 10 | Tier A |

**Copy-paste list for Google Ads location search:**

```
Florida
New York
New Jersey
Virginia
Texas
North Carolina
Pennsylvania
Washington
Georgia
Maryland
Arizona
Michigan
Nevada
Alabama
Illinois
```

### Optional Wave 2 Includes (monitor tier — 5–9 customers)

Add only after Wave 1 is stable for 30 days:

```
Colorado
Massachusetts
Tennessee
Connecticut
Indiana
```

### States to EXCLUDE (if any remain from a prior "United States" target)

If the campaign previously targeted all US, explicitly **exclude** these low-volume states:

```
California
Oregon
Hawaii
Ohio
Kansas
Idaho
Missouri
New Hampshire
Wisconsin
Kentucky
Arkansas
Oklahoma
New Mexico
Mississippi
Utah
South Dakota
South Carolina
Delaware
Alaska
Vermont
Wyoming
Montana
Rhode Island
North Dakota
Nebraska
West Virginia
Iowa
Minnesota
Louisiana
Maine
```

### Expected Impact

- Reallocates ~$5,500/mo national spend toward states with **331 proven customers** (52% of base)
- Stops spend in states with 0–4 customers and no sales history
- Current visible performance: **7 conversions on $12,325** at country level — geo tightening is critical

### PMax Listing Group Tie-In (after custom labels import)

| Asset group | Listing group filter | Geo |
|-------------|---------------------|-----|
| Wood Doors | `custom_label_0 = wood` | 15 states above |
| Fiberglass Doors | `custom_label_0 = fiberglass` | 15 states above |
| Iron Doors | `custom_label_0 = iron` | 15 states above |

---

## Campaign 2: Performance Max — California

### Strategy

Target **California** statewide, then **exclude waste counties** identified in the 720-day location + Shopify reconciliation.

### Step-by-Step in Google Ads

1. Open campaign **Performance Max: California**
2. Go to **Settings → Locations**
3. Ensure **California, United States** is **Included**
4. Click **Enter another location** → search each exclusion below → set to **Exclude**
5. Set location option to **Presence**
6. Save

### Location to INCLUDE

| Location | Type |
|----------|------|
| California, United States | State |

### Locations to EXCLUDE (county level)

| Location | Ads Spend (720d) | Shopify Customers | Reason |
|----------|-----------------:|------------------:|--------|
| San Diego County, California, United States | $2,182 | 0 | Highest waste; exclude first |
| Santa Clara County, California, United States | $857 | 0 | Zero customer match |
| Fresno County, California, United States | $319 | 0 | Zero customer match |

**Copy-paste for Google Ads exclusion search:**

```
San Diego County, California
Santa Clara County, California
Fresno County, California
```

### Optional Wave 2 CA Exclusions (review after 30 days)

Lower priority — borderline data:

| Location | Spend | Customers | Note |
|----------|------:|----------:|------|
| San Francisco, California | $68 | 2 | Monitor; exclude if no improvement |
| San Bernardino County, California | $86 | 0* | County-level; city Fontana has 4 customers |

*Shopify city data does not map cleanly to county — validate before excluding San Bernardino County.

### CA Markets to PROTECT (do not exclude)

These have proven Shopify customers and should continue receiving spend:

| City | Customers | Current Spend |
|------|----------:|--------------:|
| San Jose | 15 | $538 |
| Ontario | 10 | $59 |
| San Diego (city) | 8 | $0 |
| Yorba Linda | 7 | $8 |
| Rancho Cucamonga | 6 | $38 |
| Fremont | 6 | $33 |
| Fontana | 4 | $79 |

**Note:** San Diego **County** is excluded, not San Diego **city**. Google may still serve the city depending on how geo boundaries resolve — monitor after launch.

### Local Installation Radius (optional, separate campaign)

If you split installation leads later, create a **third** PMax or Search campaign:

| Setting | Value |
|---------|-------|
| Target | 50-mile radius around Ontario, CA 91761 |
| Goal | Qualified calls + form submissions |
| Exclude | National freight messaging |

Keep this separate from the California ecom PMax to avoid mixed signals.

---

## Campaign Comparison Summary

| Campaign | Include | Exclude | Location option |
|----------|---------|---------|-----------------|
| Sales-Performance Max-19 | 15 US states (list above) | California + all non-listed states | Presence |
| Performance Max: California | California (state) | San Diego, Santa Clara, Fresno counties | Presence |
| Search - Brand | United States | None (keep broad) | Presence |

---

## Change Log Template

When approved and applied, log in `Change-Log.md`:

```markdown
## YYYY-MM-DD — Location targeting (BGW)

**Campaign:** Sales-Performance Max-19
**Change:** Restricted to 15 Tier A states; removed broad US targeting
**Reason:** 331 of 640 Shopify customers outside CA; $119k spend in unlisted geos with 7 visible conv
**Expected:** Lower wasted spend; higher concentration in FL, NY, NJ, TX, etc.

**Campaign:** Performance Max: California
**Change:** Excluded San Diego County, Santa Clara County, Fresno County
**Reason:** $3,358 combined spend with 0 matched Shopify customers
**Expected:** Reallocate to San Jose, Ontario, Inland Empire
```

---

## Verification Checklist (7 days after launch)

- [ ] Location report shows spend shifting into Tier A states (national)
- [ ] San Diego / Santa Clara / Fresno counties show $0 spend (CA)
- [ ] Shopify orders by state tracked weekly
- [ ] No drop in Brand Search conversions
- [ ] Purchase conversion volume in Google Ads aligns with Shopify orders (±10%)

---

## Related Files

- [[Data/Analysis/geo-reconciliation.md]]
- [[Next-Actions]]
- [[Diagnostic-Plan]]
- [[Google-Ads]]
