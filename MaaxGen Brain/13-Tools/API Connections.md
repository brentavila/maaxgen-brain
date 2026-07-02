# API Connections

Architecture for connecting Google Ads, GA4, Merchant Center, Search Console, GoHighLevel, n8n, and Shopify to the MaaxGen system.

**The one rule: no credential of any kind ever appears in this vault.** This vault syncs to Obsidian and other devices. API keys, OAuth tokens, refresh tokens, client secrets, webhook signing secrets, and account IDs paired with tokens all live outside the vault. This file documents the architecture only.

## Where Secrets Live

| Layer | Location | What goes there |
|---|---|---|
| Local secret store | `C:\Users\brent\.maaxgen\.env` (outside the vault, never synced) | API keys, OAuth client IDs and secrets, refresh tokens |
| Windows Credential Manager | OS-level | Anything long-lived you want encrypted at rest |
| n8n credential store | Inside n8n (encrypted with the n8n encryption key) | Credentials n8n workflows use at runtime |
| MCP server config | Claude/Cursor MCP config files, referencing environment variables | Never hardcode tokens in the config; use env var references |

See `C:\Users\brent\.maaxgen\README.md` for the setup checklist.

## Connection Pattern By Platform

Read paths go through MCP servers so Claude and Cursor can pull data directly with scoped, read-only access. Write paths go through n8n so every mutation is a logged, reviewable workflow instead of an agent improvising API calls.

| Platform | Auth | Access mode | Read path | Write path |
|---|---|---|---|---|
| Google Ads | OAuth 2.0 + developer token, per-client customer ID under the MCC | Read-only first; standard access only after read workflows proven | Google Ads MCP server (GAQL queries) | n8n workflow for offline conversion uploads and approved changes |
| GA4 | OAuth 2.0 or service account with viewer role per property | Viewer only | GA4 Data API MCP server | None (GA4 is read-only for us) |
| Merchant Center | Same Google Cloud project, Content API scope | Read-only first | Content API via MCP or scheduled n8n pull | Feed fixes via Shopify app, not direct API writes |
| Search Console | OAuth 2.0, restricted user per property | Read-only by nature | Search Console API MCP server | None |
| Shopify | Custom app per store, Admin API token with minimal scopes (`read_orders`, `read_products`, `read_reports`) | Read-only scopes only | Shopify Admin API MCP server or n8n pull | Never write; the client owns the store |
| GoHighLevel | Location-level API key (not agency-level) or OAuth app | Scoped to the one location | n8n pull for lead and pipeline data | n8n workflows (tagging, pipeline moves) with approval gates |
| n8n | Its own credential store, encrypted | Orchestrator | Exposes webhooks the agents can call | Runs all write-side automation |

## Google Cloud Setup (one project, four APIs)

One Google Cloud project (`maaxgen-agency`) with the Google Ads API, Analytics Data API, Content API for Shopping, and Search Console API enabled. One OAuth consent screen, one client ID/secret pair, per-client refresh tokens generated from accounts that have the minimum role (Viewer/read-only) on each property. Tokens go in `~/.maaxgen/.env`, referenced by MCP config as environment variables.

## The Offline Conversion Pipeline (GHL to Google Ads)

The one write path that matters most, per the `gads-offline-conversions` skill:

1. GHL captures the lead (email, phone, gclid custom field if present)
2. Opportunity stage change (qualified / closed-won) fires a GHL webhook to n8n
3. n8n maps stage to a Google Ads conversion action, hashes email/phone (SHA-256) for Enhanced Conversions for Leads
4. n8n uploads via the Google Ads API using credentials from its own store
5. Verification step confirms the upload landed and attributes

Every upload is logged in the n8n execution history, and conversion mapping changes get an entry in the client's Change-Log.md.

## Unsafe Patterns (do not do these)

- Credentials in any markdown file in this vault, including "temporarily"
- Credentials pasted into chat prompts or committed in `.cursor` or `.claude` config files that sync
- Agency-level GHL API key where a location-level key works
- Shopify token with write scopes when we only read
- Write access to any ad account before read-only workflows are proven (standing safety rule)
- A single shared refresh token across all clients; one token per client so revocation is surgical
- n8n webhook URLs without authentication (add a header token check on every inbound webhook)

## Status

| Platform | Status |
|---|---|
| Google Ads | Not connected; CSV exports in client Data folders in the meantime |
| GA4 | Not connected |
| Merchant Center | Not connected |
| Search Console | Not connected |
| GoHighLevel | Not connected |
| n8n | Not deployed |
| Shopify (BGW) | Not connected |

Update this table as connections go live. Never add IDs-plus-tokens here; account IDs alone are fine.
