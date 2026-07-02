# Google Ads Optimization Prompt

Portable prompt for tools that do not have the MaaxGen skills installed (ChatGPT, Gemini, Claude web without skills). In Claude Code or Cursor, do not use this; just ask for an audit and the `gads-account-audit` skill takes over with the full [[04-Playbooks/Google Ads Optimization Playbook]].

---

We are improving Google Ads performance for this client. I will provide the client files and campaign data.

Read the client files first, in this order: Client-Brief.md, Offers.md, Google-Ads.md, Change-Log.md, Test-Results.md, Rejected-Ideas.md, Winning-Copy.md. Do not propose anything listed in Rejected-Ideas.md, and do not repeat tests already in Test-Results.md.

Follow this order of operations and do not skip ahead: 1) conversion tracking health, 2) offline conversion feedback for lead gen, 3) search terms and negatives, 4) geographic performance, 5) ads and assets, 6) bidding and structure. If tracking health is unknown, flag it before recommending bid or budget changes.

Goal: more conversions, with ROAS as the constraint for ecommerce or cost per qualified lead as the constraint for local lead gen.

Provide:

1. Executive summary
2. Top 5 problems and top 5 opportunities, highest leverage first
3. Tracking concerns and a go/no-go verdict on the data
4. Campaign, keyword, search term, and negative keyword recommendations (exact terms, not categories)
5. Ad copy recommendations (10 headlines, 30 characters max, Start Case, keyword plus CTA, no exclamation points)
6. Landing page recommendations
7. Budget recommendations with risk noted
8. 7-day action plan and 30-day testing plan
9. Notes to add to Change-Log.md and Test-Results.md

Do not invent data, pricing, or offers. List any data you still need.
