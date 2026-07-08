# Google Drive Meeting Notes Playbook

Connect Google Meet summaries to the MaaxGen Brain client folders so meeting context improves task management, recommendations, and agent memory.

## Goal

After every client Google Meet, meeting notes land in the right `02-Clients/<Client>/` folder, get structured, and update [[Next-Actions]], [[Change-Log]], and other client files as needed.

## Vault layout (per client)

| File / folder | Purpose |
|---|---|
| `Meeting-Notes.md` | Processed meeting log, index, and agent routing rules |
| `Data/Meetings/*.txt` | Raw plain-text exports from Google Drive (manual for now) |
| `Data/Meetings/Raw.md` | Index note for the raw folder in Obsidian |

## Phase 1 — Manual (current)

1. **Export from Drive:** Open the Meet notes Doc → File → Download → Plain text (.txt).
2. **Save:** `MaaxGen Brain/02-Clients/<Client>/Data/Meetings/YYYY-MM-DD-title.txt`
3. **Process in Cursor:** Prompt example:
   > Process `<Client>` meeting notes from `Data/Meetings/<file>.txt`. Add a structured entry to `Meeting-Notes.md`. Extract action items to `Next-Actions.md`, decisions to `Change-Log.md`, and offer changes to `Offers.md` where relevant.
4. **Verify:** Check the meeting index row in `Meeting-Notes.md` and linked vault files.

## Phase 2 — Semi-automated (next)

Pick one path (do not build all at once):

### Option A — Google Drive folder watch (recommended)

- Dedicated Drive folder: `MaaxGen / Meet Notes /` with subfolders per client.
- n8n workflow (or local script on a schedule):
  1. Google Drive API lists new Docs modified since last run.
  2. Export each Doc as plain text via Drive API (`files.export` with `text/plain`).
  3. Write to `Data/Meetings/` in the vault (Obsidian sync or git pull on the machine that runs the script).
  4. Optional: webhook or Cursor automation to trigger "process latest meeting for BGW."

**Auth:** Same Google Cloud project as other MaaxGen integrations. Scope: `drive.readonly` (read + export only). Token in `C:\Users\brent\.maaxgen\.env` — never in the vault. See [[API Connections]].

### Option B — Gmail trigger

If Meet summaries arrive by email with a Doc link, n8n can parse the link, fetch the Doc ID, export text, and file it. Less reliable if Google changes email format.

### Option C — Zapier / Make

Fastest to prototype: New file in Drive folder → export text → append to a Google Sheet or webhook → script writes to vault. Migrate to n8n when stable.

## Phase 3 — Full loop

1. **Ingest** — Drive → `Data/Meetings/*.txt` (automated).
2. **Process** — Agent reads raw file + client context; writes structured block to `Meeting-Notes.md`.
3. **Route** — Action items → `Next-Actions.md`; approved changes → `Change-Log.md`; tests → `Test-Results.md`; rejections → `Rejected-Ideas.md`.
4. **Notify** — Optional: summary posted to Command Center or a daily digest.

## Client matching

Map Meet notes to client folders by:

- **Drive subfolder name** (e.g. `Meet Notes/BGW-Doors/`) — simplest.
- **Calendar event title** prefix (e.g. `[BGW]` in the meeting name).
- **Manual tag** in the Doc title until automation is tuned.

Document the rule in each client's `Meeting-Notes.md` once chosen.

## Agent read order update

When doing client work, read `Meeting-Notes.md` after `Change-Log.md` and `Test-Results.md` so live conversation context is not lost. The `maaxgen-client-context` skill should include this file in a future update.

## Safety

- Drive integration is **read-only** until processing workflow is proven.
- Do not store OAuth tokens or Doc IDs with secrets in the vault.
- Raw `.txt` files are snapshots; do not overwrite after processing.

## Related

- [[API Connections]] — Google Cloud project and secret locations
- [[Meeting Notes Template]] — per-meeting entry format
- Branch: `Google-Drive` — meeting notes infrastructure and future automation work
