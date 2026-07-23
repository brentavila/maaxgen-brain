# Change Log

Use this file to document every meaningful change.

## Format

### Date

## Change Made

## Reason For Change

## Expected Outcome

## Result

## Notes

---

# Change Entries

## 2026-06-30

### Change Made

Set up client folder.

### Reason For Change

Create source of truth for future AI analysis.

### Expected Outcome

Better consistency across ChatGPT, Claude, Cursor, and Gemini.

### Result

Pending.

### Notes

Initial setup.

---

## 2026-06-30

### Change Made

Completed Q2 2026 Google Ads baseline analysis (Apr 1 – Jun 29 CSV export).

### Reason For Change

Establish performance baseline before optimization changes.

### Expected Outcome

Clear priorities for CPA reduction and conversion quality improvement.

### Result

Baseline captured. Pending optimization implementation.

### Notes

**Account baseline:** $3,500 spend | 645 clicks | 135 conversions | $25.93 CPA.

**Key findings:**

- Brand Search (~$465, ~94 conv, ~$5 CPA) drives ~70% of conversions.
- Services Search (~$2,133, ~36 conv, ~$59 CPA) is primary efficiency problem.
- Demand Gen Retargeting ($453, 0 conv) and PMax ($449, 5 conv, $90 CPA) underperform.
- Top keyword waste: "Subaru mechanic near me" (Broad, $760) and "mechanic shop" (Phrase, $749).
- Subaru Specialist ad group spend up 70% QoQ without proportional conversion lift.
- June spend ~2× Apr/May; investigate budget/bid/match type changes.
- PMax triggering competitor names and wrong-intent queries (meineke, dealer names, safelite, etc.).
- Mobile = 82% of clicks; call tracking and mobile LP critical.

**Planned tests (see Test-Results.md):**

1. Pause Demand Gen — measure call/booking impact over 14 days.
2. Broad-to-exact match tightening on top 2 service keywords.
3. Competitor negative keyword list (account level).
4. Services RSA copy refresh with coupon + Subaru positioning.

**Tracking flags:** Confirm Primary conversion actions, call duration threshold, and GA4/Ads dedup before tCPA changes.

---

## 2026-07-02

### Change Made

GTM conversion tag audit via local read-only MCP (`gtm_audit_conversion_tags`).

Container: **GTM-MSC76CJB** (kingsautocenter.net) | Account `6207634803` | Default Workspace.

### Reason For Change

Cross-check GTM setup against Google Ads conversion actions before Primary/Secondary cleanup or tCPA changes.

### Expected Outcome

Clear map of which tags fire which conversions; flag duplicates and gaps.

### Result

Audit complete. No GTM changes made (read-only).

### Notes

**GTM tags that affect Google Ads / GA4 conversions:**

| Tag | Type | Fires on | Ads / GA4 role |
|---|---|---|---|
| Google Ads Dynamic Call Tracking | awcc | All Pages | Website call swap on (970) 695-9360; label `cR4SCO3OwvwYEIHtycsq` → Ads **Dynamic Call Tracking** (Primary) |
| Google Ads - Text Optin Signup | awct | Text opt-in confirmation visible | Label `aFO5CNKixPwYEIHtycsq`; no matching enabled Ads action found |
| GA4 Call Click Event | gaawe | `tel:` link clicks | Event `call_click` → GA4 import (Ads action **Hidden**) |
| Google Tag AW-11432785537 | googtag | Init | Base Ads tag |
| Google Tag + GA4 (tags 8 and 10) | googtag | Init + All Pages | Both load **G-WEQSQCEZ6Y** — likely duplicate GA4 config |

**Appointment booking:** Triggers exist for AutoOps confirmation (`Element Visibility - Appointment Booked Confirmation`), but only **FB Schedule** fires there. No GTM Google Ads or GA4 event tag on booking. Ads **AutoOps - ao-appointment-booked** (Primary) is GA4-import only — AutoOps must send the event to GA4 directly, not via GTM.

**Not in GTM (Ads-side only):** Calls from ads (forwarding number), Clicks to call, Directions, Store visits.

**Issues to fix (approval required before publish):**

1. **Six Primary actions in Ads, only two GTM-fired conversion paths** — demote Clicks to call, Directions, Store visits to Secondary before bidding changes.
2. **Duplicate GA4 load** — tags 8 and 10 both configure G-WEQSQCEZ6Y; consolidate to one Google tag.
3. **No Consent Mode v2** — no consent tags or variables in container.
4. **Text Optin Ads tag** — GTM fires a conversion label with no active Ads action; remove tag or create/match action intentionally.
5. **call_click is Hidden in Ads (correct)** — do not promote; Dynamic Call Tracking + Calls from ads are the call Primary pair.

**Cross-reference Ads Primary actions:** Calls from ads, Dynamic Call Tracking, Clicks to call, AutoOps ao-appointment-booked, Local actions Directions, Store visits — all Primary; only Dynamic Call Tracking and GA4 appointment import trace cleanly from this GTM container.
