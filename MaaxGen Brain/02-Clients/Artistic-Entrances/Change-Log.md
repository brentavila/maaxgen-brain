# Artistic Entrances Change Log

Use this file to document meaningful marketing, website, tracking, and automation changes.

## 2026-07-22 — Door Configurator Project Started

### Change Made

- Documented the client brief and website configurator requirements
- Separated application code, product assets, CRM data, and MaaxGen strategy documentation
- Began a dedicated Next.js configurator project outside the Obsidian vault
- Defined the hybrid preview, lead payload, analytics events, and launch gates

### Reason For Change

High-intent custom iron door traffic needs a clearer, more engaging path from product discovery to a qualified quote request. Large product-image libraries also require purpose-built storage rather than the synced MaaxGen Brain vault.

### Expected Outcome

- Higher landing-page engagement and quote completion
- Better lead context for the Artistic Entrances sales team
- Cleaner performance measurement from configurator start through closed sale
- Faster and safer product-asset delivery

### Result

Local implementation completed and verified:

- Production Next.js build passes
- ESLint passes
- Door, option, review, and quote steps were browser-tested
- Quote API validates the complete configuration, SMS consent, and optional entry photo
- Asset audit and Cloudinary upload tooling are ready

The client source image folder, catalog PDF, Cloudinary credentials, n8n production webhook, deployment account, and live-ad write access were not available. No live ad, website, CRM, CDN, or automation changes have been made.

### Notes

Paid traffic must not be moved until staging, tracking, form delivery, and owner approval are complete.
