#!/usr/bin/env python3
"""Generate GMC-optimized Shopify product import CSV for featured collection."""

from __future__ import annotations

import csv
import re
from html import unescape
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "products_export_1 (3).csv"
OUTPUT = BASE / "products_export_gmc_optimized.csv"

GMC_CATEGORY = "4634"  # Hardware > Building Materials > Doors (existing BGW taxonomy)
HERO_HANDLES = {
    "m-280a-mahogany-door",
    "fiberglass-exterior-door-fd05",
    "m-705-mahogany-door",
    "m580e-exterior-wood-double-doors",
    "m580e-white",
    "valencia-fiberglass-door-and-sidelights-fd04w",
    "francisco-iron-door",
}


def strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    text = unescape(re.sub(r"\s+", " ", text)).strip()
    return text


def material_from_row(row: dict) -> str:
    mat = (row.get("Door material (product.metafields.shopify.door-material)") or "").lower()
    title = (row.get("Title") or "").lower()
    if "fiberglass" in mat or "fiberglass" in title or re.search(r"\bfd\d", title):
        return "fiberglass"
    if "iron" in mat or "iron" in title or "steel" in title:
        return "iron"
    if "aluminum" in mat or "folding" in title:
        return "aluminum"
    return "wood"


def config_from_row(row: dict) -> str:
    cfg = (row.get("Door Configuration (product.metafields.custom.door_configuration)") or "").lower()
    title = (row.get("Title") or "").lower()
    if "single door with sidelight" in cfg or "sidelight" in title:
        return "sidelight"
    if "double" in cfg or "double" in title:
        return "double"
    if "folding" in title or "bi-fold" in title:
        return "folding"
    return "single"


def extract_model(title: str, handle: str) -> str:
    for pat in [r"\b(M\d+[A-Z]?|FD\d+[A-Z]?|ID\d+|M-\w+|300I)\b", r"\b([A-Z]\d{3,4}[A-Z]?)\b"]:
        m = re.search(pat, title, re.I)
        if m:
            return m.group(1).upper().replace("M-", "M")
    return handle.split("-")[0].upper()


def shopping_title(row: dict) -> str:
    title = row.get("Title") or ""
    handle = row.get("Handle") or ""
    mat = material_from_row(row)
    config = config_from_row(row)
    model = extract_model(title, handle)

    if config == "folding":
        return f"Bi-Fold Aluminum Patio Door | Interior Exterior | BGW Doors"[:150]

    mat_label = {"wood": "Wood", "fiberglass": "Fiberglass", "iron": "Iron", "aluminum": "Aluminum"}[mat]
    config_label = {
        "single": "Single",
        "double": "Double",
        "sidelight": "Single With Sidelights",
        "folding": "Bi-Fold",
    }[config]

    parts = [f"Pre-Hung {mat_label} Front Door"]
    if model and model not in ("FOLDING", "BROOKSIDE", "CASTLE"):
        parts.append(model)
    parts.append(config_label)
    parts.append("BGW Doors")
    result = " | ".join(parts[:3]) + " | " + parts[-1] if len(parts) > 3 else " | ".join(parts)
    return result[:150]


def shopping_description(row: dict, title: str) -> str:
    seo = (row.get("SEO Description") or "").strip()
    body = strip_html(row.get("Body (HTML)") or "")
    mat = material_from_row(row)
    config = config_from_row(row)

    if config == "folding":
        base = seo if seo else body[:400]
        extras = (
            " Aluminum bi-fold folding patio door for residential interiors and exteriors. "
            "Nationwide freight shipping in 5 to 8 business days. "
            "Factory-direct pricing from BGW Doors. Over 30 years in business."
        )
        return re.sub(r"\s+", " ", (base + extras).strip())[:5000]

    base = seo if seo else body[:400]
    if "pre-hung" not in base.lower() and "prehung" not in base.lower():
        base = (
            f"Factory-direct pre-hung {mat} exterior entry door from BGW Doors. "
            f"{base}"
        )
    extras = (
        " Includes pre-hung frame, hinges, and threshold. "
        "Nationwide freight shipping in 5 to 8 business days. "
        "Professional installation available in Los Angeles and Ontario, California. "
        "Over 30 years in business. Premium in-stock warehouse inventory."
    )
    if config == "double":
        extras = " Double door configuration." + extras
    if config == "sidelight":
        extras = " Single door with sidelights configuration." + extras

    desc = (base + extras).strip()
    desc = re.sub(r"\s+", " ", desc)
    return desc[:5000]


def labels_for(row: dict) -> tuple[str, str, str, str, str]:
    handle = row.get("Handle") or ""
    mat = material_from_row(row)
    config = config_from_row(row)

    label0 = mat
    label1 = "high" if mat == "wood" else "medium"
    label2 = "hero" if handle in HERO_HANDLES else "stable"
    label3 = "pre-hung" if config != "folding" else "folding"
    if config == "double":
        label3 = "pre-hung-double"
    elif config == "sidelight":
        label3 = "pre-hung-sidelight"
    label4 = "in-stock"
    return label0, label1, label2, label3, label4


def product_type(row: dict) -> str:
    mat = material_from_row(row)
    config = config_from_row(row)
    if config == "folding":
        return "Home & Garden > Doors > Patio Doors > Folding Doors"
    base = f"Home & Garden > Doors > Exterior Entry Doors > {mat.title()} Front Doors"
    if config == "double":
        return base + " > Double Doors"
    if config == "sidelight":
        return base + " > Doors With Sidelights"
    return base


def main() -> None:
    with SOURCE.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    for row in rows:
        title = shopping_title(row)
        desc = shopping_description(row, title)
        l0, l1, l2, l3, l4 = labels_for(row)
        model = extract_model(row.get("Title") or "", row.get("Handle") or "")

        row["Title"] = title
        row["SEO Title"] = title[:70]
        row["SEO Description"] = desc[:320]
        row["Google Shopping / Google Product Category"] = GMC_CATEGORY
        row["Google Shopping / MPN"] = model if model else row.get("Handle", "")[:70]
        row["Google Shopping / Condition"] = "new"
        row["Google Shopping / Custom Label 0"] = l0
        row["Google Shopping / Custom Label 1"] = l1
        row["Google Shopping / Custom Label 2"] = l2
        row["Google Shopping / Custom Label 3"] = l3
        row["Google Shopping / Custom Label 4"] = l4
        row["Type"] = row.get("Type") or "Front Door"
        row["Product Category"] = product_type(row)

        tags = set(t.strip() for t in (row.get("Tags") or "").split(",") if t.strip())
        tags.update(["pre-hung", "entry door", "exterior door", "BGW Doors", l0])
        row["Tags"] = ", ".join(sorted(tags))

    with OUTPUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUTPUT} ({len(rows)} variant rows)")


if __name__ == "__main__":
    main()
