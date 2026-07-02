import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parent


def parse_money(s):
    if pd.isna(s):
        return 0.0
    if isinstance(s, (int, float)):
        return float(s)
    s = str(s).replace("$", "").replace(",", "").replace("%", "").strip()
    if s in ("", "No data", "< 10%"):
        return 0.0
    try:
        return float(s)
    except ValueError:
        return 0.0


def parse_pct(s):
    if pd.isna(s):
        return 0.0
    s = str(s).replace("%", "").strip()
    try:
        return float(s)
    except ValueError:
        return 0.0


st_path = base / "Search terms report (1) 1.csv"
df_st = pd.read_csv(st_path, skiprows=2)

for col in ["Cost", "Avg. CPC", "Cost / conv."]:
    if col in df_st.columns:
        df_st[col + "_num"] = df_st[col].apply(parse_money)
df_st["Conv_rate_num"] = df_st["Conv. rate"].apply(parse_pct)
df_st["Conv_num"] = df_st["Conversions"].apply(parse_money)

total_cost = df_st["Cost_num"].sum()
total_clicks = int(df_st["Clicks"].sum())
total_conv = df_st["Conv_num"].sum()

print("=== SEARCH TERMS TOTALS ===")
print(f"Rows: {len(df_st)}")
print(f"Cost: ${total_cost:,.2f}")
print(f"Clicks: {total_clicks}")
print(f"Conversions: {total_conv}")
print(f"CPA: ${total_cost/total_conv if total_conv else 0:,.2f}")
print(f"Conv rate: {total_conv/total_clicks*100 if total_clicks else 0:.2f}%")

wasted = df_st[df_st["Conv_num"] == 0]
wasted_cost = wasted["Cost_num"].sum()
print(f"\nWasted spend (0 conv): ${wasted_cost:,.2f} ({wasted_cost/total_cost*100:.1f}% of total)")

print("\n=== TOP 25 SPEND, ZERO CONVERSIONS ===")
top_waste = wasted.nlargest(25, "Cost_num")
for _, r in top_waste.iterrows():
    term = str(r["Search term"])[:60]
    camp = str(r["Campaign"])[:40]
    print(f"  ${r['Cost_num']:7.2f} | {int(r['Clicks']):3d} clk | {term} | {camp}")

conv = df_st[df_st["Conv_num"] > 0].sort_values("Conv_num", ascending=False)
print(f"\n=== CONVERTING SEARCH TERMS ({len(conv)} terms, {conv['Conv_num'].sum():.0f} conv) ===")
for _, r in conv.head(30).iterrows():
    cpa = r["Cost_num"] / r["Conv_num"] if r["Conv_num"] else 0
    term = str(r["Search term"])[:50]
    camp = str(r["Campaign"])[:35]
    print(f"  {r['Conv_num']:5.1f} conv | ${cpa:6.2f} CPA | ${r['Cost_num']:7.2f} | {term} | {camp}")

print("\n=== BY CAMPAIGN (search terms) ===")
camp = (
    df_st.groupby("Campaign")
    .agg(cost=("Cost_num", "sum"), clicks=("Clicks", "sum"), conv=("Conv_num", "sum"))
    .sort_values("cost", ascending=False)
)
for c, r in camp.iterrows():
    cpa = r["cost"] / r["conv"] if r["conv"] else float("inf")
    cpa_str = f"${cpa:.2f}" if cpa != float("inf") else "N/A"
    print(f"  ${r['cost']:8.2f} | {int(r['clicks']):4d} clk | {r['conv']:5.1f} conv | CPA {cpa_str} | {c}")

kw = pd.read_csv(base / "Search_keywords(2026.04.01-2026.06.29).csv")
kw["Cost_num"] = kw["Cost"].apply(parse_money)
print("\n=== KEYWORDS BY SPEND ===")
for _, r in kw.sort_values("Cost_num", ascending=False).iterrows():
    print(
        f"  ${r['Cost_num']:8.2f} | {int(r['Clicks']):4d} clk | CTR {r['CTR']} | "
        f"{str(r['Match type'])[:20]:20} | {r['Search Keyword']}"
    )

competitor_patterns = [
    "meineke", "valvoline", "jiffy", "firestone", "midas", "brake plus", "brakes plus",
    "les schwab", "pep boys", "mavis", "goodyear", "discount tire", "friesen",
    "community auto", "mccormick", "alpine", "eagle auto", "ken garff", "dellenbach",
    "tynan", "houska", "seneff", "mason street", "weston", "campus repair",
    "707 automotive", "kennedy automotive", "loyola", "salta", "saving grace", "gearz",
    "chan's foreign", "prolube", "severance", "motorway", "super rupair", "asr fort",
    "pine dog", "longs auto", "final drive", "nelson auto", "westin", "dave's",
    "1up complete", "ams fort", "pat's vee", "caliber", "fast track", "autonation",
    "triple a", "h&r repair", "h&h automotive", "scoots automotive", "zach's transmission",
    "kens muffler", "kens auto", "flying wrenches", "matt parker mechanic",
]

comp_rows = df_st[
    df_st["Search term"].str.lower().apply(lambda x: any(p in x for p in competitor_patterns))
]
print("\n=== COMPETITOR-RELATED TERMS ===")
print(
    f"Cost: ${comp_rows['Cost_num'].sum():,.2f}, Clicks: {int(comp_rows['Clicks'].sum())}, "
    f"Conversions: {comp_rows['Conv_num'].sum()}"
)

diy_patterns = [
    "headlight", "how to", "diy", " parts", "amazon", "youtube", "manual", "recall",
    "subaru of america customer", "inspection service before buying",
]
diy = df_st[df_st["Search term"].str.lower().apply(lambda x: any(p in x for p in diy_patterns))]
print("\n=== DIY/PARTS/NON-SERVICE TERMS ===")
print(
    f"Cost: ${diy['Cost_num'].sum():,.2f}, Clicks: {int(diy['Clicks'].sum())}, "
    f"Conversions: {diy['Conv_num'].sum()}"
)

dealer_patterns = [
    "service department", "service center", "kia service", "nissan service",
    "toyota service", "honda service", "ford service", "chevrolet", "jeep service",
    "land rover service", "lexus fort", "audi service", "volkswagen repair near me",
    "ken garff", "dellenbach", "tynan nissan", "fort collins kia service department",
]
dealer = df_st[df_st["Search term"].str.lower().apply(lambda x: any(p in x for p in dealer_patterns))]
print("\n=== DEALER SERVICE DEPT QUERIES ===")
print(
    f"Cost: ${dealer['Cost_num'].sum():,.2f}, Clicks: {int(dealer['Clicks'].sum())}, "
    f"Conversions: {dealer['Conv_num'].sum()}"
)

print("\n=== MATCH TYPE PERFORMANCE ===")
mt = (
    df_st.groupby("Match type")
    .agg(cost=("Cost_num", "sum"), clicks=("Clicks", "sum"), conv=("Conv_num", "sum"))
    .sort_values("cost", ascending=False)
)
for m, r in mt.iterrows():
    print(f"  ${r['cost']:8.2f} | {int(r['clicks']):4d} clk | {r['conv']:5.1f} conv | {m}")

ai = df_st[df_st["Match type"].str.contains("AI Max", na=False)]
print("\n=== AI MAX ===")
print(
    f"Cost: ${ai['Cost_num'].sum():,.2f}, Clicks: {int(ai['Clicks'].sum())}, "
    f"Conv: {ai['Conv_num'].sum()}"
)

pmax = df_st[df_st["Campaign"].str.contains("Pmax", na=False)]
print("\n=== PMAX SEARCH TERMS ===")
print(
    f"Cost: ${pmax['Cost_num'].sum():,.2f}, Clicks: {int(pmax['Clicks'].sum())}, "
    f"Conv: {pmax['Conv_num'].sum()}"
)
pmax_waste = pmax[pmax["Conv_num"] == 0].nlargest(15, "Cost_num")
for _, r in pmax_waste.iterrows():
    if r["Cost_num"] > 0 or r["Clicks"] > 0:
        print(f"  ${r['Cost_num']:6.2f} | {str(r['Search term'])[:55]}")

svc = df_st[df_st["Campaign"].str.contains("Services", na=False)]
print("\n=== SEARCH SERVICES ===")
print(
    f"Cost: ${svc['Cost_num'].sum():,.2f}, Clicks: {int(svc['Clicks'].sum())}, "
    f"Conv: {svc['Conv_num'].sum()}"
)
print("Top waste in Services:")
svc_noconv = svc[svc["Conv_num"] == 0].nlargest(20, "Cost_num")
for _, r in svc_noconv.iterrows():
    if r["Cost_num"] > 0:
        print(f"  ${r['Cost_num']:7.2f} | {str(r['Search term'])[:55]}")

brand = df_st[df_st["Campaign"].str.contains("Brand", na=False)]
print("\n=== SEARCH BRAND ===")
print(
    f"Cost: ${brand['Cost_num'].sum():,.2f}, Clicks: {int(brand['Clicks'].sum())}, "
    f"Conv: {brand['Conv_num'].sum()}"
)
if brand["Conv_num"].sum():
    print(f"Brand CPA: ${brand['Cost_num'].sum()/brand['Conv_num'].sum():.2f}")

ts = pd.read_csv(base / "Time_series(2026.04.01-2026.06.29).csv")
ts["Cost_num"] = ts["Cost"].apply(parse_money)
ts["Date"] = pd.to_datetime(ts["Date"], format="%a, %b %d, %Y")
ts["Month"] = ts["Date"].dt.to_period("M")
monthly = ts.groupby("Month").agg(cost=("Cost_num", "sum"), clicks=("Clicks", "sum"))
print("\n=== MONTHLY SPEND ===")
print(monthly)

camp_df = pd.read_csv(base / "Campaigns(2026.04.01-2026.06.29).csv")
camp_df["Cost_num"] = camp_df["Cost"].apply(parse_money)
print("\n=== CAMPAIGNS FILE ===")
print(camp_df.to_string(index=False))
print(f"Total campaign cost: ${camp_df['Cost_num'].sum():,.2f}")
print(f"Total campaign clicks: {int(camp_df['Clicks'].sum())}")

for f in [
    "Demographics(Age_2026.04.01-2026.06.29).csv",
    "Demographics(Gender_2026.04.01-2026.06.29).csv",
    "Day_&_hour(Day_2026.04.01-2026.06.29).csv",
]:
    p = base / f
    if p.exists():
        d = pd.read_csv(p)
        if "Cost" in d.columns:
            d["Cost_num"] = d["Cost"].apply(parse_money)
        print(f"\n=== {f} ===")
        print(d.to_string(index=False))

# High intent local terms with impressions but no spend or conv
local_good = df_st[
    df_st["Search term"].str.lower().str.contains("fort collins|near me", na=False)
    & ~df_st["Search term"].str.lower().apply(lambda x: any(p in x for p in competitor_patterns))
]
print("\n=== LOCAL INTENT TERMS (fort collins / near me, non-competitor) ===")
print(
    f"Cost: ${local_good['Cost_num'].sum():,.2f}, Clicks: {int(local_good['Clicks'].sum())}, "
    f"Conv: {local_good['Conv_num'].sum()}"
)
local_conv = local_good[local_good["Conv_num"] > 0].sort_values("Conv_num", ascending=False)
for _, r in local_conv.head(15).iterrows():
    print(f"  {r['Conv_num']:.1f} conv | ${r['Cost_num']:.2f} | {r['Search term']}")

# Suburu terms
sub = df_st[df_st["Search term"].str.lower().str.contains("subaru", na=False)]
print("\n=== SUBARU TERMS ===")
print(
    f"Cost: ${sub['Cost_num'].sum():,.2f}, Clicks: {int(sub['Clicks'].sum())}, "
    f"Conv: {sub['Conv_num'].sum()}"
)
for _, r in sub.sort_values("Cost_num", ascending=False).head(15).iterrows():
    print(
        f"  ${r['Cost_num']:6.2f} | {r['Conv_num']:.1f} conv | "
        f"{int(r['Clicks'])} clk | {r['Search term']}"
    )
