# Artistic Entrances Meeting Notes

Google Meet generates a meeting summary in Google Drive (Google Doc). Until Drive automation is connected, import notes manually and process them here so they feed [[Next-Actions]], [[Change-Log]], [[Client-Brief]], and [[Offers]].

## Manual import (now)

1. Open the Meet notes Google Doc in Drive.
2. **File → Download → Plain text (.txt)**.
3. Save to `Data/Meetings/YYYY-MM-DD-short-title.txt` in this client folder.
4. In Cursor, ask: *"Process the Artistic Entrances meeting notes from Data/Meetings/[filename] into Meeting-Notes.md and update Next-Actions."*

Raw exports live in [[Data/Meetings/Raw]].

## Meeting index

| Date | Title | Attendees | Source | Processed |
|---|---|---|---|---|
| 2026-06-27 | Automation Strategy and AI Guardrails | Brent Avila, Jose Espinoza, John Rodriguez, Homeinnovate LLC | [[Data/Meetings/2026-06-27-automation-strategy.txt]] | Yes |

## Meetings

### 2026-06-27 — Automation Strategy and AI Guardrails

**Attendees:** Brent Avila (MaaxGen), Jose Espinoza, John Rodriguez, Homeinnovate LLC

**Source:** [[Data/Meetings/2026-06-27-automation-strategy.txt]]

**Summary**

The team reviewed the fully built AI automation stack: a GHL-integrated chatbot (Claude, ChatGPT, Gemini) with 60-second SMS response, 14-day nurture sequences, and lead scoring. Close rate is 3–4%; the strategic shift is from increasing lead volume to optimizing follow-up and conversion. Key decisions locked down AI discount guardrails after discussing real-world losses from unsupervised bot discounting. Nationwide Google Shopping ads were approved to launch once the next door shipment arrives (~July 25). Next meeting scheduled for July 13.

**Decisions**

- Implement automated SMS + email blast for all "attempting contact" pipeline opportunities
- AI bot discount policy: max $1,000, valid 24 hours only, human escalation required for unresolved objections
- Prohibit AI from issuing independent discounts without guardrails
- Shift focus from lead volume to conversion rate optimization (current close rate: 3–4%)
- Launch nationwide Google Shopping ads after shipment arrives on the 25th
- Plan larger budget allocation in January for new channel expansion
- Next meeting: **2026-07-13**

**Client requests / constraints**

- SMS marketing requires explicit opt-in; transactional messages only without consent
- Bot must respect "Do Not Disturb" statuses to avoid carrier blacklisting
- AI cannot check live inventory yet; pricing from knowledge base with manual team follow-up
- Photo collection strategy: offer free digital rendering in exchange for door photos (attach to CRM)
- John Rodriguez shared BGW retrospective as cautionary tale: inconsistent budget, impulsive spending, band-aid fixes — team committed to financial discipline and long-term strategy

**Action items**

| Owner | Action | Due | Routed to |
|---|---|---|---|
| Brent Avila | Develop non-spammy stale-lead revival plan | Before blast | [[Next-Actions]] #4 |
| Brent Avila | Build "attempting contact" automation (mass SMS + email) | 2026-07-13 | [[Next-Actions]] #2 |
| Brent Avila | Execute email/text blast for past Facebook and form leads | After opt-in audit | [[Next-Actions]] #3 |
| Brent Avila | Configure AI discount guardrails ($1K max, 24hr, human escalation) | Before deployment | [[Next-Actions]] #8 |
| Brent Avila | Clean up CRM opportunities and workflows | 2026-07-13 | [[Next-Actions]] #5 |
| Brent Avila | Test AI agents for business task delegation | Ongoing | [[Next-Actions]] #11 |
| Brent Avila | Launch nationwide Google Shopping once shipment active | ~2026-07-25 | [[Next-Actions]] #13 |
| Brent Avila | Present CRM opportunity updates at next meeting | 2026-07-13 | [[Next-Actions]] #7 |
| Homeinnovate LLC | Test AI chatbot via provided link | This week | [[Next-Actions]] #1 |
| Homeinnovate LLC | Plan January budget increase for new channel | Q4 2026 | [[Next-Actions]] #18 |
| Jose Espinoza | Develop Instagram course on doors/windows | Ongoing | [[Next-Actions]] #15 |
| John Rodriguez | Contact measurement contact about failed appointment | ASAP | [[Next-Actions]] #6 |

**Recommendations discussed**

- AI video generation (Kling, C-Dance 2.5) for 30-second door promo ads from still images
- Obsidian "Second Brain" + local Mac Mini for secure AI agent ops (financial data stays off cloud)
- Government backlink / AEO service ($30K/yr via usmayor.org) — discussed, not approved
- Facebook Marketplace automation — uncertain feasibility due to platform restrictions
- $500 Amazon gift card campaign to revive month-old stale leads (connects to April promo)

**Continuity from prior meetings**

| Prior meeting | Thread | Status in June 27 |
|---|---|---|
| 2026-03-17 | Follow-up system was critical gap; only 5 FB leads vs 21 prior month | **Addressed** — 60-sec SMS, 14-day nurture, attempting-contact automation approved |
| 2026-03-17 | $500 Amazon gift card for custom doors | **Revisited** — proposed for stale-lead revival blast |
| 2026-04-08 | Shift focus to custom doors; GHL funnel site + chatbot | **Delivered** — bot live with Claude/Gemini/GHL integration; live demo successful |
| 2026-04-08 | $500 gift card promo reinstated | **Carried forward** — now part of lead revival strategy |
| 2026-04-11 | Bot install for testing; revert to successful lead form | **Partially done** — bot mature and tested; form revert status unclear |
| 2026-04-11 | YouTube channel + cross-post from Facebook | **Open** — not mentioned; still on carry-forward list |
| 2026-04-11 | Mini ballistic door samples for influencers | **Open** — not mentioned; still on carry-forward list |
| 2026-04-11 | Marketplace generating strong leads ($6,500 sale) | **Confirmed ongoing** — team still closing via marketplace |
| 2026-04-17 | FB budget +$5/day ($25.80/day) | **Baseline held** — January increase planned for new channel |
| 2026-04-17 | Deploy custom door site; point Google Ads to new page | **Evolved** — now planning nationwide Shopping ads post-shipment |
| 2026-04-17 | East Coast market expansion after logistics dialed | **Aligned** — nationwide Shopping supports this direction |

**Open questions**

- Has the lead form been reverted to the February version that converted at ~1 lead/day?
- Is SMS opt-in captured on all existing Facebook and form leads before the blast?
- Shopify/Stripe direct purchase through bot — timeline and inventory sync approach?
- Facebook Marketplace automation — feasible or blocked by platform ToS?

**Raw notes**

<details>
<summary>Full import</summary>

See [[Data/Meetings/2026-06-27-automation-strategy.txt]]

</details>

---

## How agents use this file

When loading Artistic Entrances context, read this file after [[Change-Log]] and [[Test-Results]] to capture client voice, priorities, and commitments from live conversations. Route outcomes as follows:

| Extract | Write to |
|---|---|
| Tasks for Brent / MaaxGen | [[Next-Actions]] |
| Account or site changes made or approved | [[Change-Log]] |
| Offer, pricing, or promo changes | [[Offers]] + [[Client-Brief]] if strategic |
| Tests agreed in the meeting | [[Test-Results]] |
| Ideas ruled out | [[Rejected-Ideas]] |
