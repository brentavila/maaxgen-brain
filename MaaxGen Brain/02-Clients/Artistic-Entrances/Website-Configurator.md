# Artistic Entrances Website Configurator

## Objective

Create a premium, mobile-first custom iron door experience that helps high-intent visitors choose a door and key options, then submit a complete request for a personalized quote. The configurator is a lead-generation tool and will not accept payments in version 1.

## Ownership Boundaries

| Item | Source of truth |
|---|---|
| Marketing strategy, offers, tests, and results | This Artistic Entrances vault folder |
| Application code and catalog schema | Dedicated `artistic-entrances-configurator` repository |
| Optimized product media | Cloud image CDN |
| Raw source media and catalog files | Local asset-staging folder outside MaaxGen Brain |
| Contacts and opportunities | GoHighLevel |
| Approved integration writes | n8n |
| Credentials and tokens | `C:\Users\brent\.maaxgen\` or platform credential stores |

Do not add product-image binaries, catalog PDFs, credentials, API keys, or tokens to MaaxGen Brain.

## Version 1 Scope

### Customer flow

1. Arrive on an SEO and paid-traffic landing page focused on custom iron doors.
2. Start the configurator.
3. Select a door style from searchable and filterable door photos.
4. Select configuration, glass, handle, and finish options.
5. Review a design summary.
6. Enter contact and project details and optionally upload a current-entry photo.
7. Submit a quote request.
8. See a confirmation page and enter the existing GoHighLevel follow-up flow.

### Hybrid preview

- The primary preview changes to the selected door photo.
- Handles, glass, and finishes appear as catalog thumbnails or swatches.
- The design summary clearly lists every selected option.
- Version 1 does not claim to show a photorealistic composite of every combination.

### Out of scope

- Payments and checkout
- Live inventory promises
- Automatic pricing
- Photorealistic real-time compositing
- Customer accounts
- Automatic discounts

## Catalog Schema

Each option requires a stable ID so links and saved configurations remain valid.

### Door

- `id`
- `name`
- `slug`
- `style`
- `configuration`
- `imageUrl`
- `thumbnailUrl`
- `alt`
- `availableGlassIds`
- `availableHandleIds`
- `availableFinishIds`
- `featured`

### Glass

- `id`
- `name`
- `thumbnailUrl`
- `description`

### Handle

- `id`
- `name`
- `thumbnailUrl`
- `description`

### Finish

- `id`
- `name`
- `hex`
- `textureUrl`
- `description`

Unknown compatibility should be treated as requiring confirmation, not assumed to be available.

## Lead Payload

The application sends the following fields to a server-side endpoint, which forwards approved data to n8n or GoHighLevel:

- First and last name
- Email
- Phone
- ZIP code
- Homeowner, contractor, or builder
- Project timeline
- Budget range, if approved for the form
- Notes
- SMS consent and timestamp
- Selected door ID and name
- Door configuration
- Glass ID and name
- Handle ID and name
- Finish ID and name
- Source URL, UTM values, GCLID, and session identifiers where available
- Entryway-photo URL, when uploads are enabled

The human-readable configuration summary should be stored on the contact or opportunity. The full JSON payload may be stored in a long-text custom field or an external record referenced by ID.

## GoHighLevel And n8n Flow

1. The Next.js server validates the request and consent.
2. The server posts to an n8n webhook using a secret stored outside the repository.
3. n8n creates or updates the GoHighLevel contact.
4. n8n creates or updates the custom-door opportunity and attaches the configuration summary.
5. GoHighLevel applies the configurator tag and starts the approved response workflow.
6. Qualified and closed outcomes can later be uploaded to Google Ads through the documented offline-conversion pipeline.

Do not expose a private GoHighLevel token or n8n production webhook secret in browser code.

## Analytics Events

Use GTM container `GTM-TPFGF2VM`.

| Event | Trigger | Important parameters |
|---|---|---|
| `configurator_start` | First intentional interaction | `source_page` |
| `configurator_step_view` | A step becomes active | `step_name`, `step_number` |
| `configurator_option_select` | An option is selected | `option_type`, `option_id` |
| `configurator_complete` | Customer reaches review | `door_id` |
| `generate_lead` | Valid quote request succeeds | `door_id`, `lead_type` |
| `entry_photo_upload` | Optional upload succeeds | `file_type` |

Do not send names, emails, phone numbers, street addresses, notes, or image filenames to Google Analytics or advertising pixels.

## SEO Requirements

- Primary page intent: custom iron doors
- Primary H1: “Design Your Custom Iron Door”
- Unique metadata and copy for important door categories
- Crawlable gallery and category links outside the JavaScript-only configurator
- LocalBusiness and appropriate service schema; do not create fake product prices or review data
- Responsive images, reserved image dimensions, and lazy loading below the fold
- Internal links from the current gallery and relevant service pages

## Performance And Accessibility

- Mobile-first layouts and touch targets
- Keyboard-operable selections and visible focus states
- Descriptive image alternative text
- Do not use color alone to communicate finish selection
- Target a fast Largest Contentful Paint on paid landing pages
- Use responsive CDN transformations and modern image formats
- Keep the quote form usable if optional media fails to load

## Asset Pipeline

1. Keep raw source files in a local staging folder outside the vault.
2. Inventory files and calculate hashes to identify duplicates.
3. Assign stable catalog IDs and human-reviewed names.
4. Create optimized WebP/AVIF variants and square thumbnails.
5. Extract one catalog thumbnail for each handle and glass option.
6. Create finish swatches from documented catalog values.
7. Upload processed assets to the selected CDN.
8. Save CDN public IDs and URLs in catalog data.

Recommended naming:

`door-{door-id}-{view-or-variant}.webp`

## Environment Variables

Expected names in the configurator deployment:

- `N8N_QUOTE_WEBHOOK_URL`
- `N8N_QUOTE_WEBHOOK_TOKEN`
- `NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

Only public CDN identifiers may use a `NEXT_PUBLIC_` prefix. Secrets must remain in local or hosting-provider secret stores.

## Launch Gates

- Product names and option compatibility reviewed by Artistic Entrances
- All public claims and active offers approved
- Responsive image performance tested on mobile
- Form validation, spam protection, and consent tested
- GoHighLevel contact, opportunity, tags, and workflow verified
- GTM events verified without personally identifiable information
- Thank-you page and error recovery tested
- Conversion action mapped and deduplicated
- Staging reviewed by the owners
- Paid traffic is not moved until Brent explicitly approves the live Google Ads change

## Success Metrics

- Landing-page to configurator-start rate
- Completion rate by configurator step
- Quote-form submission rate
- Cost per qualified quote request
- Appointment rate
- Close rate and closed revenue
- Median lead response time

## Future Enhancements

- Email a resumable design link
- Photo upload and human-generated digital rendering
- AI-assisted post-submit rendering with human approval
- Layered visual compositing for selected high-volume door models
- Saved configurations in GoHighLevel custom fields
- Separate in-stock purchasing flow if payments are approved later
