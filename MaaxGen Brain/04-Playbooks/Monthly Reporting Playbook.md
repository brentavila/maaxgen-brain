# Monthly Reporting Playbook

SOP for producing client monthly reports. Subagent: `client-report-writer` (Claude Code). Data comes from the client folder and connected tools, never from memory.

## Inputs

1. Client folder: Client-Brief (KPIs), Change-Log (what we did), Test-Results (what we learned)
2. Google Ads data for the month vs prior month and same month last year when available
3. GA4 landing page and channel data (`ga4-analyst`)
4. For ecom: Shopify revenue and MER (`shopify-profit-analyst`) so reported ROAS matches reality
5. For lead gen: qualified lead and closed-lead counts from GoHighLevel

## Report Structure

1. **Result vs the KPI that matters** (the client's main KPI from the brief, not vanity metrics)
2. **What we changed this month and why** (from Change-Log)
3. **What we learned** (tests concluded, from Test-Results)
4. **What we are doing next month** (top 3 actions, expected impact)
5. **Anything we need from the client**

## Writing Rules

- Grounded, plain language a busy owner can skim in two minutes
- No em dashes, no hype, no unexplained jargon
- Every claim backed by a number the client could verify
- Lead with the outcome, not the activity

## After Sending

Save the report to the client's Reports.md with the date. Add next month's committed actions to Next-Actions.md.
