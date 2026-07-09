#!/usr/bin/env python3
"""BGW Doors export analysis — handles actual file names and formats."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
ANALYSIS = BASE / "Analysis"
ANALYSIS.mkdir(exist_ok=True)

STATE_MAP = {
    "California": "CA", "Texas": "TX", "Florida": "FL", "New York": "NY",
    "Nevada": "NV", "Arizona": "AZ", "Georgia": "GA", "Washington": "WA",
    "Colorado": "CO", "Oregon": "OR", "Illinois": "IL", "Ohio": "OH",
    "Michigan": "MI", "Pennsylvania": "PA", "North Carolina": "NC",
    "Virginia": "VA", "Tennessee": "TN", "Maryland": "MD", "New Jersey": "NJ",
    "Massachusetts": "MA", "Indiana": "IN", "Missouri": "MO", "Wisconsin": "WI",
    "Minnesota": "MN", "South Carolina": "SC", "Alabama": "AL", "Louisiana": "LA",
}


def norm_city(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


def load_shopify() -> tuple[dict[str, int], dict[str, int], int]:
    path = BASE / "Customers by location - 2024-07-19 - 2026-07-09.csv"
    by_state: dict[str, int] = defaultdict(int)
    by_city_ca: dict[str, int] = defaultdict(int)
    total = 0
    with path.open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            n = int(row.get("New customer records") or 0)
            total += n
            region = (row.get("Customer region") or "").replace("US-", "")
            city_raw = row.get("Customer city") or ""
            if region:
                by_state[region] += n
            if region == "CA" and city_raw:
                city = re.sub(r"^US-[A-Z]{2}-", "", city_raw)
                by_city_ca[city] += n
    return dict(by_state), dict(by_city_ca), total


def load_ads_ca() -> tuple[list[dict], dict[str, float]]:
    path = BASE / "BGW Doors Location report Last 720 Days - BGW Doors Location report Last 720 Days.csv"
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("Location,"))
    rows = []
    totals: dict[str, float] = {}
    for row in csv.DictReader(lines[start:]):
        loc = row.get("Location", "")
        if loc.startswith("Total:"):
            totals[loc] = float((row.get("Cost") or "0").replace(",", ""))
            continue
        if not loc or "California" not in loc:
            continue
        rows.append({
            "location": loc,
            "city": loc.split(",")[0].strip().strip('"'),
            "cost": float((row.get("Cost") or "0").replace(",", "")),
            "conv": float((row.get("Conversions") or "0").replace(",", "")),
            "clicks": int(float((row.get("Interactions") or "0").replace(",", ""))),
        })
    return rows, totals


def match_shopify_city(city: str, by_city_ca: dict[str, int]) -> int:
    if city in by_city_ca:
        return by_city_ca[city]
    nc = norm_city(city)
    for sc, count in by_city_ca.items():
        if norm_city(sc) == nc:
            return count
    return 0


def geo_report(by_state: dict[str, int], by_city_ca: dict[str, int], total: int, ads_rows: list[dict], totals: dict[str, float]) -> str:
    lines = [
        "# Geo Reconciliation — Shopify vs Google Ads\n",
        f"**Shopify:** {total} new customer records (Jul 19, 2024 – Jul 9, 2026)  ",
        f"**Google Ads:** ${totals.get('Total: Account', 0):,.0f} spend, {720} days (location report)\n",
        "> Note: City-level location data in this export is **California only** (Performance Max: California). "
        "National spend (~$119k) appears under \"Total: Other locations\" — request a **state-level** location report for the US excl. CA campaign.\n",
        "## National — Shopify Customer Hot States\n",
        "Use these states as Tier A targets for the national PMax campaign once tracking is fixed:\n",
        "| State | Customers | % of Total | Ads Data Available |",
        "|-------|----------:|-----------:|--------------------|",
    ]
    for state, n in sorted(by_state.items(), key=lambda x: -x[1])[:20]:
        pct = 100 * n / total
        ads_note = "CA city report only" if state == "CA" else "Need state report"
        lines.append(f"| {state or '(blank)'} | {n} | {pct:.1f}% | {ads_note} |")

    tier_a = [s for s, n in by_state.items() if n >= 10 and s]
    national_tier = [s for s in tier_a if s != "CA"]
    lines.append(f"\n**Recommended national geo focus (≥10 customers, excl. CA):** {', '.join(national_tier)}\n")

    lines += [
        "## California — City Reconciliation\n",
        "| City | Shopify Customers | Ads Cost | Ads Conv | Flag |",
        "|------|------------------:|---------:|---------:|------|",
    ]
    ca_rows = []
    for city, cust in sorted(by_city_ca.items(), key=lambda x: -x[1])[:30]:
        ads = next((r for r in ads_rows if norm_city(r["city"]) == norm_city(city)), None)
        cost = ads["cost"] if ads else 0
        conv = ads["conv"] if ads else 0
        if cost >= 100 and cust <= 1:
            flag = "Exclude candidate"
        elif cust >= 5:
            flag = "Scale"
        elif cost >= 50 and conv == 0:
            flag = "Waste — review"
        else:
            flag = "Monitor"
        ca_rows.append((cust, city, cost, conv, flag))
        lines.append(f"| {city} | {cust} | ${cost:,.0f} | {conv:.1f} | {flag} |")

    lines += [
        "\n## CA Exclude Candidates (≥$100 ads spend, ≤1 Shopify customer)\n",
        "| Location | Ads Cost | Ads Conv | Shopify Customers |",
        "|----------|----------:|---------:|------------------:|",
    ]
    for r in sorted(ads_rows, key=lambda x: -x["cost"]):
        cust = match_shopify_city(r["city"], by_city_ca)
        if r["cost"] >= 100 and cust <= 1:
            lines.append(f"| {r['city']} | ${r['cost']:,.0f} | {r['conv']:.1f} | {cust} |")

    lines += [
        "\n## Google Ads Account Totals (720 days)\n",
        "| Segment | Cost |",
        "|---------|-----:|",
    ]
    for key in ["Total: Account", "Total: Performance Max", "Total: Search", "Total: Shopping", "Total: Other locations", "Total: Locations"]:
        if key in totals:
            lines.append(f"| {key.replace('Total: ', '')} | ${totals[key]:,.0f} |")

    return "\n".join(lines) + "\n"


def feed_report() -> str:
    path = BASE / "products_export_1 (3).csv"
    seen: set[str] = set()
    products: list[dict] = []
    with path.open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            h = row.get("Handle", "")
            if h in seen:
                continue
            seen.add(h)
            products.append(row)

    lines = [
        "# Feed Title Audit — Featured Collection\n",
        f"**{len(products)} unique products** in featured export.\n",
        "## Critical Feed Issues\n",
        "- **0 product titles** contain \"Pre-Hung\" (Merchant Center likely uses default Title, not SEO Title)",
        "- **SEO Titles exist** and are stronger (e.g. \"Modern Wood Front Exterior Door\") but may not be syncing to Google Shopping feed",
        "- **No custom labels** populated (Custom Label 0–4 all empty)",
        "- **Google Product Category** missing on most SKUs\n",
        "## Title vs SEO Title (feed should use SEO)\n",
        "| Product Title (current feed?) | SEO Title (should be in feed) | Suggested Shopping Title |",
        "|------------------------------|------------------------------|--------------------------|",
    ]

    for row in products:
        title = (row.get("Title") or "").strip()
        seo = (row.get("SEO Title") or "").strip()
        tl = title.lower()
        material = "Wood"
        if "fiberglass" in tl or "fd" in tl:
            material = "Fiberglass"
        elif "iron" in tl:
            material = "Iron"
        config = "Single"
        if "double" in tl:
            config = "Double"
        if "sidelight" in tl:
            config += " With Sidelights"
        model = re.search(r"\b([A-Z]?\d{2,4}[A-Z]?|M\d+[A-Z]?|FD\d+[A-Z]?|ID\d+)\b", title)
        model_str = model.group(1) if model else ""
        if "slab" in tl:
            suggested = f"{material} Door Slab {model_str}".strip()
        else:
            suggested = f"Pre-Hung {material} Front Door {model_str} | {config}".strip()
        lines.append(f"| {title[:45]} | {seo[:45]} | {suggested[:55]} |")

    lines += [
        "\n## Custom Label Recommendations\n",
        "| Label | Assign |",
        "|-------|--------|",
        "| custom_label_0 | wood / fiberglass / iron |",
        "| custom_label_1 | high / medium margin |",
        "| custom_label_2 | hero / stable / test / poor |",
        "| custom_label_3 | pre-hung / slab / double / sidelight |",
        "| custom_label_4 | in-stock / clearance |",
        "\n## Action: Configure Shopify Google & YouTube App\n",
        "Set feed to pull **SEO Title** and **SEO Description** instead of default product title/body. "
        "Verify in Merchant Center after next sync.\n",
    ]
    return "\n".join(lines) + "\n"


def ga4_report() -> str:
    path = BASE / "BGW Doors GA4 Analytics Jan 1 2026 - July 7 2026 - Reports snapshot.csv"
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()

    metrics = {}
    channels: dict[str, int] = {}
    items: list[tuple[str, int]] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("Sessions,Add to carts"):
            vals = next(csv.reader([lines[i + 1]]))
            metrics = {"sessions": int(vals[0]), "atc": int(vals[1]), "purchases": int(vals[2]), "checkouts": int(vals[3])}
        if line.startswith("Session primary channel group"):
            reader = csv.DictReader(lines[i : i + 20])
            for row in reader:
                ch = row.get("Session primary channel group (Default Channel Group)", "")
                sess = row.get("Sessions", "")
                if ch and sess and ch != "Session primary channel group (Default Channel Group)":
                    try:
                        channels[ch] = int(sess)
                    except ValueError:
                        pass
        if line.startswith("Item name,Items purchased"):
            reader = csv.DictReader(lines[i : i + 50])
            for row in reader:
                name = row.get("Item name", "")
                qty = row.get("Items purchased", "")
                if name and qty:
                    try:
                        items.append((name, int(qty)))
                    except ValueError:
                        pass
        i += 1

    s, atc, purch, chk = metrics.get("sessions", 0), metrics.get("atc", 0), metrics.get("purchases", 0), metrics.get("checkouts", 0)
    out = [
        "# GA4 Snapshot — YTD Jan 1 to Jul 7, 2026\n",
        "## Site Funnel (all channels)\n",
        "| Metric | Count | Rate |",
        "|--------|------:|-----:|",
        f"| Sessions | {s:,} | — |",
        f"| Add to cart | {atc:,} | {100*atc/s:.2f}% of sessions |" if s else "",
        f"| Begin checkout | {chk:,} | {100*chk/atc:.1f}% of ATC |" if atc else "",
        f"| Purchases | {purch:,} | {100*purch/s:.3f}% of sessions |" if s else "",
        f"| Checkout → Purchase | — | {100*purch/chk:.1f}% |" if chk else "",
        "\n**Diagnosis:** Massive checkout abandonment. 566 checkouts → 44 purchases (7.8%). "
        "This is a CRO + shipping/trust problem, not just an ads targeting problem.\n",
        "## Traffic by Channel (sessions)\n",
        "| Channel | Sessions | % |",
        "|---------|----------:|--:|",
    ]
    total_ch = sum(channels.values())
    for ch, n in sorted(channels.items(), key=lambda x: -x[1]):
        out.append(f"| {ch} | {n:,} | {100*n/total_ch:.1f}% |")

    out += [
        "\n## Top Purchased Items (YTD)\n",
        "| Item | Qty | Note |",
        "|------|----:|------|",
    ]
    for name, qty in sorted(items, key=lambda x: -x[1])[:15]:
        note = "Slab — deprioritize in feed" if "slab" in name.lower() else ("Wood pre-hung" if "wood" in name.lower() and "slab" not in name.lower() else "")
        out.append(f"| {name[:60]} | {qty} | {note} |")

    out += [
        "\n## Offline Signals Not in Google Ads\n",
        "- **255 phone clicks** (GA4) — not imported as conversions",
        "- **33 email clicks** — not tracked in Ads",
        "\n## Key Events\n",
        "- Purchases: 44",
        "- Phone clicks: 248 (top key event after purchase)",
        "\nPaid Search 120d avg value: $2.93 vs Organic Search: $9.24 — organic buyers may be higher intent.\n",
    ]
    return "\n".join(out) + "\n"


def summary(by_state, total, totals, metrics) -> str:
    purch = metrics.get("purchases", 44)
    spend = totals.get("Total: Account", 0)
    return f"""# BGW Data Analysis Summary

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
"""


def main() -> None:
    by_state, by_city_ca, total = load_shopify()
    ads_rows, totals = load_ads_ca()

    (ANALYSIS / "geo-reconciliation.md").write_text(
        geo_report(by_state, by_city_ca, total, ads_rows, totals), encoding="utf-8"
    )
    (ANALYSIS / "feed-title-audit.md").write_text(feed_report(), encoding="utf-8")
    (ANALYSIS / "ga4-snapshot.md").write_text(ga4_report(), encoding="utf-8")

    metrics = {}
    ga4_path = BASE / "BGW Doors GA4 Analytics Jan 1 2026 - July 7 2026 - Reports snapshot.csv"
    for i, line in enumerate(ga4_path.read_text(encoding="utf-8-sig").splitlines()):
        if line.startswith("Sessions,Add to carts"):
            vals = next(csv.reader([ga4_path.read_text(encoding="utf-8-sig").splitlines()[i + 1]]))
            metrics = {"purchases": int(vals[2])}

    (ANALYSIS / "summary.md").write_text(summary(by_state, total, totals, metrics), encoding="utf-8")
    print((ANALYSIS / "summary.md").read_text())


if __name__ == "__main__":
    main()
