# Google Ads Optimization Playbook

The SOP for optimizing any MaaxGen Google Ads account. The `gads-account-audit` skill automates this order; this note is the human-readable version and the source the skill defers to.

## Order Of Operations (do not reorder)

Fix the data before touching the levers. Smart Bidding optimizes toward whatever signal it is fed.

1. **Conversion tracking and signal health.** Skill: `gads-conversion-tracking`. Primary vs secondary actions, value tracking, dedup GA4 vs Ads tag, Enhanced Conversions, counting setting, window and attribution. If this is broken, stop; everything downstream is invalid.
2. **Offline conversion feedback** (lead gen accounts). Skill: `gads-offline-conversions`. Calls and CRM closed-won fed back via Enhanced Conversions for Leads or OCI. The GHL and n8n pipeline is documented in [[13-Tools/API Connections]].
3. **Search term and negative keyword hygiene.** Skill: `gads-search-terms-negatives`. Stop the bleed first; it is the fastest reversible win.
4. **Geographic optimization.** Skill: `gads-geo-optimizer`. For ecom, reconcile against Shopify profit-by-city (`shopify-profit-analyst`), not platform ROAS. For local, reconcile against closed leads.
5. **Asset and Ad Strength optimization.** Skill: `gads-asset-optimizer`. RSA assets, PMax asset groups, audience signals, images and video coverage.
6. **Structure and bidding review.** Only after 1-5. tROAS for ecom with reliable values, tCPA for lead gen with close-back. Move targets 15-20% at a time.

## Account Type Branch

- **E-commerce** (BGW Doors): constraint is ROAS reconciled to profit and MER. Merchant Center feed health (`merchant-center-analyst`) is part of step 5.
- **Local lead gen** (King's Auto, Sajack, Artistic Entrances lead side): constraint is TCPA on qualified leads. Step 2 matters more than anywhere.

## Before Any Recommendation

1. Read the client folder: Client-Brief, Offers, Google-Ads, Change-Log, Test-Results, Rejected-Ideas
2. Never repeat a failed test without a stated reason
3. Never assume tracking works unless documented

## After Any Change

- Log it in the client's Change-Log.md (date, change, reason, expected outcome)
- If it is a test, add it to Test-Results.md with hypothesis and before-metrics
- Winning copy goes to Winning-Copy.md; failed ideas to Rejected-Ideas.md

## Approval Gate

No live changes to campaigns, budgets, or bidding without Brent's explicit approval. Analysis and drafts are always allowed.
