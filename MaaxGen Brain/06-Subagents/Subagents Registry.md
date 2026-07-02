# Subagents Registry

Index of Claude Code subagents installed for MaaxGen. The actual agent files live at `~/.claude/agents/` (outside this vault). This note is documentation only; editing it does not change behavior.

## Design Rule

Subagents exist for two reasons only: to isolate heavy data crunching from the main conversation, or to hold a distinct reviewer role. Method lives in skills; each data subagent is a thin wrapper that loads its matching skill. One source of truth, two entry points.

## Data-Platform Subagents (wrap the matching skill)

| Subagent | Wraps skill | Distinct job |
|---|---|---|
| `shopify-profit-analyst` | `shopify-profit-analyst` | Crunches raw Shopify orders into profit truth in isolated context |
| `ga4-analyst` | `ga4-analyst` | Diagnoses post-click behavior when CPA is high or conversion rate is low |
| `merchant-center-analyst` | `merchant-center-analyst` | Audits feed health for ecom accounts |
| `search-console-analyst` | `search-console-analyst` | Compares organic reality against paid spend |

## Specialist Subagents (distinct roles, no skill twin)

| Subagent | Distinct job | Boundary |
|---|---|---|
| `cro-specialist` | Landing page and product page conversion review; A/B test specs | Pages and forms only; does not touch campaign settings |
| `seo-analyst` | Local SEO, GBP, service pages, content opportunities | Organic only; paid query data comes in via search-console-analyst handoff |
| `creative-director` | Image/video/YouTube ad concepts and hooks from documented offers and winners | Concepts and scripts only; asset performance analysis belongs to `gads-asset-optimizer` |
| `client-report-writer` | Turns Change-Log, Test-Results, and platform data into the monthly client report | Follows [[04-Playbooks/Monthly Reporting Playbook]]; writes reports, never recommendations |

## Routing Map

- Google Ads question → `gads-account-audit` skill in the main thread routes to specialist skills, delegating data pulls to the data-platform subagents
- "Why is the page not converting" → `cro-specialist`
- "GBP ranking / organic growth" → `seo-analyst`
- "New ad creative / video scripts" → `creative-director`
- "Monthly report for X" → `client-report-writer`

## Retired

- PPC Strategist Subagent: replaced by the `gads-account-audit` skill and its routing (archived in `99-Archive`)
- Data Analyst Subagent: empty placeholder; role covered by the four data-platform subagents (archived)

## Planned, Not Built

- SMS/Email compliance reviewer (build when campaigns go live)
