# MaaxGen Brain - Operating Instructions

You are helping Brent build and operate MaaxGen, an AI-powered marketing and advertising agency for small businesses. This repo contains the Obsidian vault `MaaxGen Brain/` (the agency's second brain) plus automation config.

## Brent's Skill Level

Strong: advertising strategy, Google Ads, Meta Ads, client communication, marketing.
Learning: technical workflows, Cursor, Claude Code, agents, APIs, automation. Explain technical steps clearly and practically.

## Map Of The Vault

- `MaaxGen Brain/00-Inbox/` - unprocessed capture
- `MaaxGen Brain/01-Dashboard/` - command center
- `MaaxGen Brain/02-Clients/<Client>/` - source of truth per client (brief, offers, change log, test results, winning copy, rejected ideas, data exports)
- `MaaxGen Brain/03-Services/` - service knowledge (checklists, copy rules)
- `MaaxGen Brain/04-Playbooks/` - SOPs. Follow these when doing client work.
- `MaaxGen Brain/05-Skills/Skills Registry.md` - index of installed Claude skills
- `MaaxGen Brain/06-Subagents/Subagents Registry.md` - index of installed subagents
- `MaaxGen Brain/13-Tools/API Connections.md` - integration architecture (never put credentials here)

## Skills And Subagents

Google Ads skills are installed at `~/.claude/skills/maaxgen-google-ads-skills/`. Entry point for any account work is the `gads-account-audit` skill. Subagents live in `~/.claude/agents/`. The vault registries document what exists and when each fires.

## Client Work Rules

Before making recommendations for a client:

1. Load the `maaxgen-client-context` skill (reads the client folder in the right order)
2. Read Client-Brief.md, Offers.md, Change-Log.md, Test-Results.md, Rejected-Ideas.md
3. Do not repeat failed tests unless there is a clear reason
4. Prioritize actions by expected impact on revenue, leads, CPA, ROAS, and lead quality
5. After work: log changes in Change-Log.md, tests in Test-Results.md, winners in Winning-Copy.md, failures in Rejected-Ideas.md

## Safety Rules

- Never make live changes to ad accounts, websites, automations, emails, or SMS without explicit approval. Read-only analysis and drafts are always allowed.
- Never assume live account data unless provided or pulled through a connected tool.
- Never write credentials, API keys, tokens, or client secrets into any file inside `MaaxGen Brain/` (it syncs to Obsidian and other devices). Secrets live in `~/.maaxgen/` or the OS credential store only. See `MaaxGen Brain/13-Tools/API Connections.md`.

## Google Ads Copy Rules

- 10 headlines when requested, 30 characters max including spaces
- Start Case, include the keyword when possible, include a CTA
- No exclamation points
- Long headlines up to 90 characters when requested
- No em dashes in any client-facing copy; keep copy grounded, not salesy

## SEO Preference

Include SEO tips and opportunities when relevant.
