# Conversion Tracking Playbook

SOP for verifying that a client's conversion data can be trusted. This is the gate before any bidding, budget, or geo change. Skill: `gads-conversion-tracking`. For the offline half, skill: `gads-offline-conversions`.

## The Audit, In Order

1. **Inventory every conversion action.** Source (Ads tag, GA4 import, call, offline), category, primary vs secondary, count, value. Flag double-counting and "all conversions" inflation.
2. **Primary vs secondary.** Only primary actions drive Smart Bidding. Ecom: primary = purchase with dynamic value. Local: primary = qualified call (duration threshold) plus form. Micro-actions go secondary.
3. **Value tracking** (ecom). Dynamic transaction values, spot-check against Shopify orders.
4. **Counting setting.** Lead gen = One per click. Ecom = Every.
5. **Window and attribution.** Match the click window to the sales cycle. Data-driven attribution unless there is a reason not to.
6. **Dedup GA4 vs Ads tag.** One source of truth per event, never both.
7. **Enhanced Conversions.** Web EC on and verified in diagnostics. EC for Leads set up for any account with offline close-back.
8. **Both-directions check.** Tags fire on the real event (Tag Assistant / DebugView) and Google Ads shows "Recording conversions" with recent timestamps.

## Offline Close-Back (lead gen)

Pipeline: lead captured in GoHighLevel, outcome marked (qualified / closed-won), n8n or Data Manager uploads the conversion with gclid or hashed identifiers back to Google Ads. Architecture and credential handling in [[13-Tools/API Connections]].

## Output

A go/no-go verdict per account: is the signal trustworthy enough to optimize on? Record the verdict and any fixes in the client's Change-Log.md.

## Client Status

- **BGW Doors:** purchase tracking via Shopify Google & YouTube app; accuracy unverified. Offline conversions (calls, emails, showroom) not measured. No-go until verified.
- **King's Auto:** primary actions, call duration threshold, and GA4/Ads dedup unverified. No-go for tCPA changes until confirmed.
