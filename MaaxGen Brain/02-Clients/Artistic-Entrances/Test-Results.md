# Artistic Entrances Test Results

## Planned — Configurator Landing Experience

### Hypothesis

A mobile-first, guided door configurator will increase qualified quote requests compared with the current custom-door landing page because visitors can explore products, specify their preferences, and understand the next step before sharing contact information.

### Primary Metric

Cost per qualified custom-door lead.

### Secondary Metrics

- Landing-page to configurator-start rate
- Configurator completion rate
- Quote submission rate
- Appointment rate
- Closed-sale rate and revenue

### Baseline

Not yet established. Capture the current landing page's sessions, leads, qualified leads, cost, and conversion rate for a comparable pre-test window before launch.

### Test Design

- Validate the configurator on staging first
- Launch to a controlled traffic segment or use a time-based before/after test if campaign splitting would damage learning
- Preserve campaign intent, geography, bidding, and offer where possible
- Evaluate lead quality in GoHighLevel, not form count alone

### Status

Local pre-launch validation completed on 2026-07-22:

- Production build passed
- ESLint passed
- Browser flow passed from door selection through quote form
- Selection states and progress steps were exposed correctly to assistive technology
- GTM events are implemented without contact information in the data layer

The live test remains planned. Do not begin until real catalog assets, form delivery, conversion deduplication, analytics events, and owner approval are verified.

### Result

Pending.
