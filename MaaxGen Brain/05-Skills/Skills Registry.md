# Skills Registry

Index of Claude skills installed for MaaxGen. The actual skill files live at `~/.claude/skills/` (outside this vault) so they load in Claude Code and Cursor. This note is documentation only; editing it does not change behavior.

## How Skills And This Vault Fit Together

Skills hold the *method* (how to audit, how to mine search terms). The vault holds the *state* (client briefs, baselines, change logs). Skills read the vault through the `maaxgen-client-context` skill and the playbooks in `04-Playbooks`, and write results back to client folders.

## Google Ads Optimization Skills

Location: `~/.claude/skills/maaxgen-google-ads-skills/`

| Skill | Job | When it fires |
|---|---|---|
| `gads-account-audit` | Orchestrator. Diagnoses the account, enforces order of operations, routes to specialists | Any "audit / review / optimize / improve" request, or a single symptom like "CPA too high" |
| `gads-conversion-tracking` | Signal health: primary/secondary actions, values, dedup, Enhanced Conversions | Anything about tracking, conversion actions, attribution, GTM/gtag; always before bidding changes |
| `gads-offline-conversions` | Feed calls and CRM closed-won back to Google (EC for Leads, OCI, Data Manager) | Offline conversions, call tracking, gclid, CRM close-back; every lead-gen account |
| `gads-search-terms-negatives` | Query mining, n-grams, negative keyword lists | Search terms, wasted spend, negatives, irrelevant clicks |
| `gads-geo-optimizer` | Location performance, exclusions, budget by geography | Geo, cities, regions, location bid adjustments |
| `gads-asset-optimizer` | Ad Strength, RSA and PMax assets, audience signals, pinning | Headlines, creative, assets, asset groups, Ad Strength |

## Data-Platform Skills (the truth layers)

Same location. These feed the Ads skills real numbers instead of platform-reported ones.

| Skill | Job | Feeds |
|---|---|---|
| `shopify-profit-analyst` | True profit by city/product, MER, margin, customer-match lists | geo-optimizer, asset-optimizer, account-audit |
| `ga4-analyst` | Post-click behavior: landing pages, funnels, attribution, audiences | account-audit, CRO work |
| `merchant-center-analyst` | Feed health, disapprovals, title optimization, competitiveness | PMax/Shopping eligibility |
| `search-console-analyst` | Organic vs paid overlap, query gaps, brand defense sizing | search-terms-negatives |

## Support Skills

| Skill | Job | When it fires |
|---|---|---|
| `maaxgen-client-context` | Loads a client's vault folder in the right order before any client work | Any request naming a client |

## Standing Order Of Operations

Enforced by `gads-account-audit` and documented in [[04-Playbooks/Google Ads Optimization Playbook]]:

1. Conversion tracking → 2. Offline close-back → 3. Search terms and negatives → 4. Geo → 5. Assets → 6. Bidding and structure

## Planned, Not Built

- Meta Ads optimizer (no active Meta spend documented yet)
- Email/SMS compliance checker (build when email/SMS campaigns go live)
