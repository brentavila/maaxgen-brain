# King's Auto Google Ads

## Account Type

Local lead gen. Constraint is TCPA on qualified calls and booked appointments, not raw conversions.

## Q2 2026 Baseline (2026-04-01 to 2026-06-29)

Full detail in [[Change-Log]] and [[Test-Results]]. Raw exports in [[Data/Raw|Data/Raw]].

| Metric | Value |
|---|---|
| Spend | $3,500 |
| Clicks | 645 |
| Conversions | 135 |
| Blended CPA | $25.93 |

**Campaign breakdown:**

- Search - Brand: $465 spend, ~94 conv, ~$5 CPA (carries ~70% of conversions)
- Search - Services: $2,133 spend, ~36 conv, ~$59 CPA (primary efficiency problem)
- Demand Gen - Retargeting: $453 spend, 0 conv
- PMax - Local Ads: $449 spend, 5 conv, ~$90 CPA

## Known Problems

- Brand Search masks blended CPA; judge Services on its own ~$59 CPA
- "Subaru mechanic near me" (Broad, $760) and "mechanic shop" (Phrase, $749) are the top keyword waste
- PMax matching competitor names and wrong-intent queries (meineke, dealer names, safelite)
- June spend roughly doubled vs April/May; cause not yet confirmed
- Mobile is 82% of clicks; call tracking and mobile landing page are critical
- Tracking not yet verified: Primary conversion actions, call duration threshold, GA4/Ads dedup

## Active Test Queue

Tests 2-5 in [[Test-Results]]: pause Demand Gen, broad-to-exact tightening, competitor negative list, Services RSA refresh. None implemented yet as of 2026-06-30.

## Rules For This Account

- Do not change tCPA targets until tracking flags above are resolved
- Prioritize call quality and bookings over conversion count
- Log every change in [[Change-Log]] and every test in [[Test-Results]]
