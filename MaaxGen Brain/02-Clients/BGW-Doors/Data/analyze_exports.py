#!/usr/bin/env python3
"""Analyze BGW Doors exports: geo reconciliation, feed titles, GA4 snapshot."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
EXPORTS = BASE / "Exports"
ANALYSIS = BASE / "Analysis"
SEARCH_DIRS = (EXPORTS, BASE)  # CSVs may live in Data/ or Data/Exports/


def find_file(patterns: list[str]) -> Path | None:
    candidates: list[Path] = []
    for directory in SEARCH_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.iterdir()):
            if path.is_file() and path.suffix.lower() in {".csv", ".tsv"}:
                candidates.append(path)

    for path in candidates:
        name = path.name.lower()
        for pat in patterns:
            if re.search(pat, name, re.I):
                return path
    return None


def list_data_files() -> list[str]:
    files: list[str] = []
    for directory in SEARCH_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.iterdir()):
            if path.is_file() and path.suffix.lower() in {".csv", ".tsv"}:
                files.append(str(path.relative_to(BASE)))
    return files


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return (reader.fieldnames or [], rows)


def norm_state(val: str) -> str:
    val = (val or "").strip()
    if not val:
        return ""
    # Common US state abbreviations
    return val.upper() if len(val) <= 3 else val.title()


def col_match(fields: list[str], candidates: list[str]) -> str | None:
    lower = {f.lower(): f for f in fields}
    for c in candidates:
        if c.lower() in lower:
            return lower[c.lower()]
    for f in fields:
        fl = f.lower()
        for c in candidates:
            if c.lower() in fl:
                return f
    return None


def parse_money(val: str) -> float:
    if not val:
        return 0.0
    val = re.sub(r"[^\d.\-]", "", str(val))
    try:
        return float(val)
    except ValueError:
        return 0.0


def analyze_shopify_customers(path: Path) -> dict[str, dict]:
    fields, rows = read_csv(path)
    state_col = col_match(fields, ["shipping province", "shipping state", "province", "state", "billing province"])
    city_col = col_match(fields, ["shipping city", "city", "billing city"])
    rev_col = col_match(fields, ["total spent", "total_spent", "total revenue", "amount spent"])
    orders_col = col_match(fields, ["orders count", "orders_count", "total orders", "number of orders"])

    by_state: dict[str, dict] = defaultdict(lambda: {"revenue": 0.0, "orders": 0, "customers": 0})
    by_city: dict[str, dict] = defaultdict(lambda: {"revenue": 0.0, "orders": 0, "customers": 0})

    for row in rows:
        state = norm_state(row.get(state_col or "", ""))
        city = (row.get(city_col or "", "") or "").strip().title()
        rev = parse_money(row.get(rev_col or "", "0"))
        orders = int(parse_money(row.get(orders_col or "", "1")) or 1)

        if state:
            by_state[state]["revenue"] += rev
            by_state[state]["orders"] += orders
            by_state[state]["customers"] += 1
        if state and city:
            key = f"{city}, {state}"
            by_city[key]["revenue"] += rev
            by_city[key]["orders"] += orders
            by_city[key]["customers"] += 1

    return {"by_state": dict(by_state), "by_city": dict(by_city)}


def analyze_google_locations(path: Path) -> dict[str, dict]:
    fields, rows = read_csv(path)
    # Google Ads location reports vary; try common column names
    loc_col = col_match(fields, ["location", "city", "most specific location", "targeted location"])
    state_col = col_match(fields, ["state", "region", "province"])
    cost_col = col_match(fields, ["cost", "spend"])
    conv_col = col_match(fields, ["conversions", "all conv.", "all conversions"])
    value_col = col_match(fields, ["conv. value", "conversion value", "all conv. value"])
    clicks_col = col_match(fields, ["clicks"])

    by_state: dict[str, dict] = defaultdict(lambda: {"cost": 0.0, "conversions": 0.0, "value": 0.0, "clicks": 0})
    by_city: dict[str, dict] = defaultdict(lambda: {"cost": 0.0, "conversions": 0.0, "value": 0.0, "clicks": 0})

    for row in rows:
        loc = (row.get(loc_col or "", "") or "").strip()
        state = norm_state(row.get(state_col or "", ""))
        if not state and loc:
            # Often "City, State" or "State"
            parts = [p.strip() for p in loc.split(",")]
            if len(parts) >= 2:
                city = parts[0].title()
                state = norm_state(parts[-1])
            else:
                state = norm_state(parts[0])
                city = ""
        else:
            city = loc.split(",")[0].title() if loc and "," in loc else (loc.title() if loc else "")

        cost = parse_money(row.get(cost_col or "", "0"))
        conv = parse_money(row.get(conv_col or "", "0"))
        value = parse_money(row.get(value_col or "", "0"))
        clicks = int(parse_money(row.get(clicks_col or "", "0")))

        if state:
            by_state[state]["cost"] += cost
            by_state[state]["conversions"] += conv
            by_state[state]["value"] += value
            by_state[state]["clicks"] += clicks
        if state and city:
            key = f"{city}, {state}"
            by_city[key]["cost"] += cost
            by_city[key]["conversions"] += conv
            by_city[key]["value"] += value
            by_city[key]["clicks"] += clicks

    return {"by_state": dict(by_state), "by_city": dict(by_city)}


def build_geo_reconciliation(shopify: dict, ads: dict) -> str:
    lines = ["# Geo Reconciliation — Shopify vs Google Ads (720 days)\n"]
    all_states = set(shopify["by_state"]) | set(ads["by_state"])

    rows = []
    for state in all_states:
        s = shopify["by_state"].get(state, {"revenue": 0, "orders": 0, "customers": 0})
        a = ads["by_state"].get(state, {"cost": 0, "conversions": 0, "value": 0, "clicks": 0})
        roas = a["value"] / a["cost"] if a["cost"] > 0 else 0
        tier = classify_geo(s["revenue"], s["orders"], a["cost"], a["value"])
        rows.append((s["revenue"], state, s, a, roas, tier))

    rows.sort(key=lambda x: -x[0])

    lines.append("## By State\n")
    lines.append("| State | Shopify Revenue | Orders | Ads Cost | Ads Conv Value | Ads ROAS | Tier | Recommendation |")
    lines.append("|-------|----------------:|-------:|---------:|---------------:|---------:|------|----------------|")
    for rev, state, s, a, roas, tier in rows[:60]:
        rec = geo_recommendation(tier, a["cost"], s["revenue"])
        lines.append(
            f"| {state} | ${s['revenue']:,.0f} | {s['orders']} | ${a['cost']:,.0f} | ${a['value']:,.0f} | {roas:.2f} | {tier} | {rec} |"
        )

    # Waste: high spend, no shopify revenue
    waste = [
        (state, ads["by_state"][state])
        for state in ads["by_state"]
        if ads["by_state"][state]["cost"] >= 200
        and shopify["by_state"].get(state, {}).get("revenue", 0) == 0
    ]
    waste.sort(key=lambda x: -x[1]["cost"])

    lines.append("\n## Exclude Candidates (Ads cost ≥ $200, $0 Shopify revenue)\n")
    if waste:
        lines.append("| State | Ads Cost | Ads Conv Value | Clicks |")
        lines.append("|-------|----------:|---------------:|-------:|")
        for state, a in waste[:25]:
            lines.append(f"| {state} | ${a['cost']:,.0f} | ${a['value']:,.0f} | {a['clicks']} |")
    else:
        lines.append("_None meeting threshold, or data needs review._\n")

    # Top shopify states with poor ads ROAS
    lines.append("\n## Top Revenue States — Ads Efficiency\n")
    for rev, state, s, a, roas, tier in rows[:15]:
        if s["revenue"] > 0:
            lines.append(f"- **{state}**: ${s['revenue']:,.0f} Shopify revenue, ${a['cost']:,.0f} ad spend, ROAS {roas:.2f} ({tier})")

    return "\n".join(lines) + "\n"


def classify_geo(revenue: float, orders: int, cost: float, conv_value: float) -> str:
    if revenue >= 10000 and (cost == 0 or conv_value / max(cost, 1) >= 2):
        return "A — Scale"
    if revenue >= 2000 or orders >= 3:
        return "B — Monitor"
    if cost >= 200 and revenue == 0:
        return "C — Exclude candidate"
    if revenue > 0:
        return "B — Monitor"
    return "D — Low volume"


def geo_recommendation(tier: str, cost: float, revenue: float) -> str:
    if tier.startswith("A"):
        return "Protect; consider dedicated wood campaign"
    if tier.startswith("C"):
        return "Test exclusion after tracking verified"
    if cost > 500 and revenue < 1000:
        return "Reduce exposure; review search terms"
    return "Monitor"


def analyze_product_export(path: Path) -> str:
    fields, rows = read_csv(path)
    title_col = col_match(fields, ["title", "product title", "name"])
    seo_title_col = col_match(fields, ["seo title", "metafield", "google shopping title"])
    type_col = col_match(fields, ["type", "product type", "product category"])
    handle_col = col_match(fields, ["handle", "url handle"])
    body_col = col_match(fields, ["body", "description", "body html"])

    lines = ["# Feed Title Audit — Featured Collection\n"]
    lines.append("| Current Title | Suggested Shopping Title | Notes |")
    lines.append("|---------------|---------------------------|-------|")

    for row in rows[:50]:
        title = (row.get(title_col or "", "") or "").strip()
        if not title:
            continue
        suggested = suggest_title(title, row.get(type_col or "", ""), row.get(body_col or "", ""))
        notes = []
        tl = title.lower()
        if "slab" in tl:
            notes.append("Slab — deprioritize in PMax")
        if "pre-hung" not in tl and "pre hung" not in tl:
            notes.append("Add Pre-Hung if product includes frame")
        if "front door" not in tl and "entry door" not in tl:
            notes.append("Add front/entry door keyword")
        lines.append(f"| {title[:60]} | {suggested[:70]} | {', '.join(notes) or 'OK'} |")

    return "\n".join(lines) + "\n"


def suggest_title(title: str, product_type: str, body: str) -> str:
    t = title
    material = "Wood"
    if "fiberglass" in t.lower() or "fiberglass" in (product_type or "").lower():
        material = "Fiberglass"
    elif "iron" in t.lower():
        material = "Iron"

    config = "Single"
    if "double" in t.lower():
        config = "Double"
    if "sidelight" in t.lower() or "sidelite" in t.lower():
        config += " With Sidelights"

    model = re.search(r"\b([A-Z]?\d{2,4}[A-Z]?|[A-Z]\d+[A-Z]?|M\d+[A-Z]?|FD\d+[A-Z]?|ID\d+)\b", t)
    model_str = model.group(1) if model else ""

    if "slab" in t.lower():
        return f"{material} Door Slab {model_str}".strip()

    base = f"Pre-Hung {material} Front Door"
    if model_str:
        base += f" {model_str}"
    return f"{base} | {config}"


def main() -> None:
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    missing = []

    shopify_path = find_file([r"customer", r"shopify.*export", r"customers"])
    ads_path = find_file([r"location", r"720"])
    product_path = find_file([r"product_export"])
    ga4_path = find_file([r"ga4", r"analytics"])

    summary_lines = ["# BGW Exports Analysis Summary\n"]
    found = list_data_files()
    if found:
        summary_lines.append("## CSV Files Found\n")
        for f in found:
            summary_lines.append(f"- `{f}`")
        summary_lines.append("")

    if shopify_path and ads_path:
        shopify = analyze_shopify_customers(shopify_path)
        ads = analyze_google_locations(ads_path)
        geo_md = build_geo_reconciliation(shopify, ads)
        (ANALYSIS / "geo-reconciliation.md").write_text(geo_md, encoding="utf-8")
        summary_lines.append(f"- Geo reconciliation: `Analysis/geo-reconciliation.md`")
        top_states = sorted(shopify["by_state"].items(), key=lambda x: -x[1]["revenue"])[:5]
        summary_lines.append("\n## Top 5 States by Shopify Revenue\n")
        for state, data in top_states:
            summary_lines.append(f"- {state}: ${data['revenue']:,.0f} ({data['orders']} orders)")
    else:
        if not shopify_path:
            missing.append("Shopify customer export")
        if not ads_path:
            missing.append("Google Ads location report (720 days)")

    if product_path:
        feed_md = analyze_product_export(product_path)
        (ANALYSIS / "feed-title-audit.md").write_text(feed_md, encoding="utf-8")
        summary_lines.append(f"- Feed title audit: `Analysis/feed-title-audit.md`")
    else:
        missing.append("product_export_1.csv")

    if ga4_path:
        summary_lines.append(f"- GA4 file found: `{ga4_path.name}` (manual review recommended)")
    else:
        missing.append("GA4 YTD export")

    if missing:
        summary_lines.append("\n## Missing Files\n")
        for m in missing:
            summary_lines.append(f"- {m}")
        summary_lines.append(f"\nPlace files in: `{BASE}` or `{EXPORTS}` and commit to GitHub.")

    (ANALYSIS / "summary.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print((ANALYSIS / "summary.md").read_text())


if __name__ == "__main__":
    main()
