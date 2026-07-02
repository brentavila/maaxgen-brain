# New Client Onboarding Playbook

SOP for bringing a new client into the system so every skill and subagent has what it needs from day one.

## 1. Create The Client Folder

Copy the structure of an existing client folder in `02-Clients/` (or use [[10-Templates/Client Brief Template]], [[10-Templates/Change Log Template]], [[10-Templates/Test Results Template]]). Required files:

- Client-Brief.md (fill completely; this is what every skill reads first)
- Offers.md, Audience.md, Services-Products.md, Landing-Pages.md
- Google-Ads.md (account type: ecom ROAS or local TCPA, baseline, known problems)
- Change-Log.md, Test-Results.md, Winning-Copy.md, Rejected-Ideas.md, Next-Actions.md
- Data/ subfolder for exports

## 2. Add A Client Rule

Create `.cursor/rules/<client>.mdc` scoped to `02-Clients/<Client>/**` with the client's focus, KPIs, and copy constraints. Use `bgw-doors.mdc` as the pattern.

## 3. Register In The System

- Add the client to [[01-Dashboard/MaaxGen Command Center]]
- Add the client to the quick-reference table in the `gads-account-audit` skill (account type, constraint, tracking status)

## 4. Access And Tracking Baseline

- Request read-only access first: Google Ads, GA4, Merchant Center and Shopify (ecom), Search Console, GoHighLevel (lead gen)
- Connect via the pattern in [[13-Tools/API Connections]]; credentials never go in the vault
- Run the [[Conversion Tracking Playbook]] before any optimization work
- Capture a performance baseline in Test-Results.md (like King's Auto Test 1)

## 5. First 30 Days

1. Week 1: tracking audit and fixes, baseline capture
2. Week 2: search term hygiene and negative lists
3. Week 3-4: first test queue (from `gads-account-audit` diagnostic), report cadence agreed with client
