# CraveMode AI

## What Is CraveMode AI?

CraveMode AI is a done-for-you photo and video enhancement service for restaurants. Owners send us their existing phone photos — dark, blurry, poorly lit, whatever they have — and our AI transforms them into professional, mouth-watering content that drives orders and fills tables.

This repo is the **complete business-in-a-box**: lead generation, cold outreach, sales funnel, payment processing, client delivery, retention, and analytics — all automated through n8n workflows, Instantly email campaigns, and an Airtable CRM.

---

## The Problem

Restaurants are bleeding customers because of bad food photos, and most don't even realize it.

- **75% of diners** look at food photos before deciding where to eat — not reviews, not the menu description, photos
- A professional food photoshoot costs **$500-$2,000 per session** and takes 2-3 weeks to schedule, shoot, edit, and deliver
- Menu changes, seasonal items, and social media content mean you'd need to hire a photographer **repeatedly**
- Restaurant owners are already drowning in staffing, suppliers, health inspections — learning photography or managing photoshoots isn't happening
- Restaurants with high-quality photos get up to **30% more clicks** on Google Maps — that's 30% more people who never even see the bad-photo restaurants
- The result: every restaurant with bad photos is losing real money, every day, to the competitor down the street who happens to have better pictures

Most restaurants know their photos are bad. They just don't have a realistic way to fix it.

---

## The Solution

Restaurants send us the photos they already have — iPhone camera roll, Google listing screenshots, whatever — and our AI pipeline transforms them into professional content ready for every platform.

**AI Enhancement Pipeline:**
- **WaveSpeed AI** (photo enhancement) — lighting correction, color grading, background cleanup, sharpening. Takes a dark phone photo and outputs magazine-quality shots
- **Kling 3.0** (video generation) — creates 5-15 second cinematic food clips from still photos: sizzling close-ups, smooth pans, steam effects, appetizing transitions. The kind of content that stops the scroll on Instagram/TikTok

**What gets delivered:**
- Enhanced photos in every format: Google Business (720x720), Instagram Square (1080x1080), Instagram Story (1080x1920), Facebook (1200x630), website banner (1920x600), original high-res for print menus
- Cinematic video clips in 9:16 vertical (Reels/TikTok), 1:1 square, and 16:9 landscape
- Everything organized in a shared folder with clear naming, ready to post

**Turnaround:** 24-48 hours for subscription plans, 5 days for one-time packs.

**No photographer, no studio, no lighting equipment, no scheduling.** Restaurant sends photos, we send back content that sells.

---

## Ideal Customer Profile

Not every restaurant is a good fit. Here's who we target and why:

### Best Customers

| Signal | Why It Matters |
|--------|----------------|
| **Independent, single-location restaurants** | They don't have a marketing team or budget for professional photography. They feel the pain the most. |
| **Google rating 3.5-4.5 stars** | Good enough food to benefit from better photos, but not already crushing it online. 5-star spots usually already have pro photos. |
| **20-200 Google reviews** | Established enough to have traffic, not so new they're still figuring out the menu. |
| **Bad existing photos on Google/website** | The more dramatic the before/after, the easier the sell. Restaurants with decent photos don't feel the urgency. |
| **Active on Google Business Profile** | They care about online presence — they'll actually use the enhanced content. |
| **Revenue $500K-$5M/year** | Can afford $297-$997/mo and will see ROI from one extra table per night. |

### Restaurant Types That Convert Best

Italian, Mexican, Asian fusion, BBQ, bakeries/dessert shops, craft cocktail bars, farm-to-table — any cuisine where food presentation matters and photos can look dramatically different after enhancement. Fast food and chains are not the target.

### Who We Filter Out

- Chains and franchises (corporate handles marketing)
- Restaurants with fewer than 10 reviews (too new, high churn risk)
- Restaurants that already have professional photography (no pain point)
- Ghost kitchens / delivery-only (no Google listing to optimize)

### Geographic Strategy

Start with one metro area. Saturate it before expanding. Restaurants talk to each other — social proof compounds locally. Target cities with dense restaurant scenes: Miami, Austin, Chicago, NYC, LA, Portland, Denver, Nashville.

---

## How Fulfillment Works

The gap between "customer pays" and "customer gets their content" — here's the actual enhancement workflow:

### Step 1: Customer Sends Photos

After onboarding, customers send photos through one of these channels:
- **Email** — reply to their welcome email with photos attached (simplest, lowest friction)
- **Shared Google Drive folder** — created during onboarding, customer drops photos in anytime
- **Airtable form** — direct upload with dish names and notes (for organized clients)

Any quality works. iPhone photos, screenshots from their Google listing, old camera roll shots. The worse the original, the more dramatic the transformation.

### Step 2: AI Enhancement (n8n Workflow)

When new photos land, the enhancement workflow kicks off:

1. **Intake** — Photos get logged in the Deliveries table (Airtable) with status "Queued"
2. **WaveSpeed AI processing** — Each photo gets sent to WaveSpeed for enhancement: lighting correction, color grading, background cleanup, sharpening, composition improvement. Status moves to "Processing"
3. **Format generation** — Enhanced originals get resized into all platform-specific versions:
   - Google Business (720x720)
   - Instagram Square (1080x1080)
   - Instagram Story (1080x1920)
   - Facebook (1200x630)
   - Website Banner (1920x600)
   - Original high-res (for print menus)
4. **Video generation** — Selected hero photos get sent to Kling 3.0 to create 5-15 second cinematic clips (sizzling effects, smooth pans, steam, appetizing transitions). Three formats: 9:16 vertical, 1:1 square, 16:9 landscape
5. **Quality check** — Status moves to "Enhanced", assets staged for delivery

### Step 3: Delivery

The **asset delivery pipeline** (n8n workflow) handles the rest automatically:
- All format versions uploaded to shared folder (Google Drive/S3/R2)
- Customer notified via email with thumbnails and download links
- Deliveries table updated with asset URLs for every format
- Quota counters incremented (photos used / videos used this month)
- If quota hits 80%, a notification goes to the customer
- Delivery notifications batch every 30 minutes (not per-photo spam)

### Step 4: Quota Management

- Each plan has monthly limits (Starter: 15 photos + 3 videos, Growth: 40 + 10, Pro: 100 + 25)
- Usage tracked in real-time in the Customers table
- Quota resets automatically on the 1st of each month via the `quota-monthly-reset` workflow
- Customers approaching their limit get a notification + upgrade prompt
- Customers who consistently max out trigger the upsell automation

---

## How We Get Clients

The entire client acquisition pipeline is automated — from finding restaurants to closing the sale to preventing churn. Here's exactly how it works:

### Step 1: Lead Discovery (Automated)

An existing n8n workflow scrapes Google Maps for restaurants by city/region. For each restaurant it pulls:
- Restaurant name, address, phone, website
- Google rating and review count
- Owner/contact info when available

We load 500-1,000 new restaurant leads per week, starting with one city and expanding.

### Step 2: Email Enrichment (Automated)

Apify scrapes each restaurant's website to find owner/manager email addresses. Fallback enrichment through Apollo.io or Hunter.io if Apify can't find it. Verified emails get tagged in Airtable, bounced emails get flagged.

### Step 3: Cold Outreach via Instantly (Automated)

Enriched leads get pushed into Instantly.ai for a 3-email cold outreach sequence:

| Email | Timing | Purpose |
|-------|--------|---------|
| Email 1 | Day 0 | Intro — "Quick question about {restaurant}'s photos" + link to before/after demo gallery |
| Email 2 | Day 3 | Follow-up — social proof, specific before/after example |
| Email 3 | Day 7 | Breakup — "Last call for {restaurant}", creates urgency |

**Volume target:** 600 cold emails/day across 5+ sending accounts (120/account/day). Sending domain is separate from the main domain to protect reputation. 2-3 week warmup period before sending at volume.

**Engagement tracking:** Opens, clicks, and replies flow back into Airtable via Instantly webhooks. Lead scores update automatically. Hot leads trigger Slack alerts.

### Step 4: Landing Page + Sales Funnel (Automated)

Interested leads land on the CraveMode landing page (`site/index.html`), which includes:
- Before/after photo gallery with drag sliders
- 3-step "how it works" walkthrough
- Pricing tiers with buy buttons
- Embedded 5-minute VSL (video sales letter)
- Testimonials and FAQ
- Inquiry form for questions

**Two conversion paths:**
1. **Buy directly** — FanBasis checkout handles payment. Webhook fires to n8n, which creates the customer in Airtable, triggers the 3-email onboarding sequence, and sends a Slack notification
2. **Submit inquiry** — Form data goes to Airtable + triggers a 4-email nurture sequence over 14 days, building trust and handling objections

**Abandoned cart recovery:** If someone starts checkout but doesn't finish, a 3-email recovery sequence fires (1 hour, 24 hours, 48 hours — the third email includes a discount code).

### Step 5: Onboarding + Delivery (Automated)

New customers get a 3-email welcome sequence over 2 days:
1. Welcome + what to expect
2. How to send your first photos
3. First delivery notification

When photos are enhanced, the **asset delivery pipeline** automatically:
- Generates all format versions (Instagram, Facebook, Google, etc.)
- Tracks quota usage against their plan limits
- Batches delivery notifications (every 30 minutes)
- Resets quotas on the 1st of each month

### Step 6: Retention + Growth (Automated)

**Churn risk detection** runs daily, scoring every customer 0-100 based on usage, portal access, payment status, and engagement. Risk-tiered emails fire automatically:
- Medium risk — check-in email
- High risk — value reminder + offer
- Critical risk — personal outreach + discount
- Failed payment — 4-email recovery sequence

**Upsell automation** runs weekly, detecting:
- Customers who maxed their photo/video quota → upgrade email
- High-usage customers for 3+ months → loyalty upgrade offer
- 3-month anniversary → milestone celebration + upgrade nudge

**Ghost lead revival** runs daily, pulling leads who opened emails but never replied and running them through a 5-email re-engagement sequence with escalating urgency and a flash discount.

**Anti-spam orchestrator** enforces max 2 emails per lead per day across ALL campaigns, with priority ordering so cart recovery always beats a cold outreach email.

---

## The Landing Page

The landing page (`site/index.html`) is a full conversion-optimized single page designed to do one thing: get restaurant owners to either buy the $497 Starter Pack or submit an inquiry. Built as static HTML/CSS/JS — no framework, deploys anywhere.

### Page Sections (Top to Bottom)

| Section | What's On It |
|---------|-------------|
| **Navigation** | Sticky nav with logo, section links, and "Get Started" CTA button |
| **Hero** | Headline ("Turn Your Food Photos Into Sales Machines"), subtitle, two CTA buttons (See Pricing / View Examples), animated stat counters (50+ restaurants, 12K+ photos enhanced, 34% avg order increase) |
| **Problem** | Three stat cards (75% check photos, $3,500+ photoshoot cost, 2-3 week turnaround) + side-by-side comparison (Without CraveMode vs With CraveMode AI) with negative/positive checklists |
| **How It Works** | 3-step walkthrough with icons and connector arrows: Send Photos → AI Works Its Magic → Download & Deploy |
| **Before/After Gallery** | 6 interactive drag-slider comparisons (burger, sushi, pasta, tacos, dessert, cocktails) with restaurant names and cities. Users drag to reveal the transformation |
| **Pricing** | 3 subscription tiers (Starter/Growth/Pro) with feature lists, "Most Popular" badge on Growth. Below: 3 one-time packs (Starter Pack/Menu Refresh/Grand Opening) for commitment-free entry |
| **Testimonials** | 3 owner testimonials with star ratings, quotes, names, and restaurant details. Trust bar with animated counters (50+ restaurants, 12K+ photos, 98% satisfaction, 34% revenue lift) |
| **FAQ** | 6 expandable accordion items: photo quality, turnaround, cancellation, formats, videos, money-back guarantee |
| **Contact/CTA** | Split layout — left side: headline + 4 benefit checkmarks + CTA button. Right side: inquiry form (restaurant name, email, phone, message) with success state |
| **Footer** | Logo, quick links, legal links, contact email, hours |

### Key Conversion Features

- **Fade-in animations** on scroll for every section
- **Animated number counters** that count up when they enter viewport
- **Interactive before/after sliders** — drag to reveal transformation (most engaging element)
- **Mobile responsive** — full hamburger menu, stacked layouts, touch-friendly sliders
- **Two CTAs visible at all times** — nav button + hero buttons + pricing buttons + bottom CTA
- **$497 Starter Pack** positioned as the low-risk entry point throughout
- **Form submission** handled via JavaScript — sends to n8n webhook, shows success state inline

---

## The VSL (Video Sales Letter)

The VSL is a 5-minute video that lives on the landing page and does the heavy lifting for warm leads who want to hear the pitch before buying. Full script with visual cues and B-roll directions in `vsl/script.md`.

### Script Structure

| Section | Time | What Happens |
|---------|------|-------------|
| **Hook** | 0:00-0:30 | Split screen: terrible food photo vs AI-enhanced version. "If your restaurant's food photos look like they were taken with a flip phone... you are losing customers every single day." |
| **Problem Agitation** | 0:30-1:30 | Stats (75% check photos), montage of bad Google Maps food photos, photographer costs ($500-$2K), restaurant owner chaos. "Those bad photos are costing you real money. Every day. Every scroll." |
| **Solution** | 1:30-2:30 | 3-step reveal with before/after transitions. "You send us your existing photos... our AI enhancement engine transforms them... you get back professional-grade photos ready for everywhere." Video clip reveal as kicker. |
| **Proof** | 2:30-3:30 | Rapid-fire before/after gallery (6-8 examples, 1.5 seconds each). "Restaurants with high-quality photos get up to 30% more clicks on Google Maps." Over 50 restaurants served. |
| **Offer** | 3:30-4:30 | Pricing overview — Growth tier highlighted ($597/mo). Pivot to Starter Pack ($497 one-time) as the risk-free entry. "25 enhanced photos. 3 cinematic videos. $497. That's less than a single photoshoot." |
| **CTA** | 4:30-5:00 | "Click the button below." Scarcity: "We can only take on about 20 new restaurants per month." Final montage of best transformations. |

### Recording Options

1. **Face-to-camera** — highest trust, most personal. Use iPhone 14+ or better, natural lighting, clean background
2. **Screen recording + voiceover** — faster production, lets you show the before/afters fullscreen
3. **AI avatar** (HeyGen/Synthesia) — fastest production, but less personal. Good for v1 to get launched fast, replace with real video later

### B-Roll Needed

- 6-8 before/after photo pairs (the more dramatic the better)
- Screenshots of bad Google Maps food photos (blur restaurant names)
- Screen recording scrolling through enhanced gallery
- 2-3 Kling 3.0 cinematic food video clips
- Simple pricing graphic (Canva)
- "Limited spots" graphic
- CraveMode logo + CTA end card

---

## The 7 Email Campaigns

| Campaign | Emails | Daily Volume | Trigger |
|----------|--------|-------------|---------|
| Cold Outreach | 3 | 600 (60%) | New enriched lead |
| Inquiry Nurture | 4 | 100 (10%) | Landing page form submission |
| Abandoned Cart | 3 | 30 (3%) | Checkout started but not completed |
| Ghost Revival | 5 | 50 (5%) | Lead opened 3+ emails but went silent |
| Re-engagement | 2 | 50 (5%) | No activity for 30+ days |
| Churn Prevention | 1-4 | 20 (2%) | Risk score threshold hit |
| Upsell | 1 | 20 (2%) | Quota maxed / high usage / anniversary |
| **Total** | **30+** | **1,000/day** | |

All email templates are in `emails/` as markdown files, ready to paste into Instantly.

---

## The 12 n8n Workflows

| Workflow | File | What It Does |
|----------|------|-------------|
| Instantly Lead Upload | `instantly-lead-upload.json` | Pushes enriched leads from Airtable into Instantly campaigns |
| Instantly Reply Handler | `instantly-reply-handler.json` | Processes opens, clicks, replies, bounces → updates Airtable + Slack alerts |
| Landing Page Form Handler | `landing-page-form-handler.json` | Captures inquiry form submissions → Airtable + nurture sequence |
| Payment Webhook Handler | `payment-webhook-handler.json` | Processes FanBasis payments → creates customer records + triggers onboarding |
| Onboarding Sequence | `onboarding-sequence.json` | 3-email welcome sequence over 2 days |
| Asset Delivery Pipeline | `asset-delivery-pipeline.json` | Multi-format photo/video delivery + quota tracking |
| Quota Monthly Reset | `quota-monthly-reset.json` | Resets all customer quotas on the 1st of each month |
| Ghost Lead Reviver | `ghost-lead-reviver.json` | Daily scan for silent leads → re-engagement campaign |
| Churn Risk Detector | `churn-risk-detector.json` | Daily customer scoring → triggers prevention emails |
| Upsell Automation | `upsell-automation.json` | Weekly scan for upgrade opportunities |
| Metrics Snapshot | `metrics-snapshot.json` | Daily business metrics capture (MRR, churn, LTV, conversions) |
| Cross-Campaign Orchestrator | `cross-campaign-orchestrator.json` | Anti-spam enforcement — max 2 emails/lead/day with priority |

---

## The Airtable CRM (7 Tables)

| Table | Records | Purpose |
|-------|---------|---------|
| **Leads** | Every restaurant discovered | Full CRM with lead scoring, pipeline stages, outreach status, objection tracking |
| **Customers** | Every paying client | Plan tier, quota tracking, churn risk score, payment status, LTV |
| **Deliveries** | Every photo/video delivered | Asset URLs, format versions, enhancement model, batch tracking |
| **Conversations** | Every email thread | Inbound/outbound, classification (interested/objection/question), sentiment |
| **Metrics** | Daily business snapshots | MRR, ARR, churn rate, conversion rates, LTV, CAC, emails sent, revenue |
| **A/B Tests** | Every experiment | Subject lines, CTAs, landing page variants, statistical significance tracking |
| **Optimization Log** | Weekly review journal | Findings, actions taken, expected vs actual impact |

Lead scoring formula auto-calculates based on email opens (+10), replies (+50), sample gallery views (+30), Google rating (+10-20), and review count (+5-15). Leads tier into Priority/Hot/Warm/Cold.

Full schema with all fields and formulas in `docs/airtable-schema.md`.

---

## Business Model

### Subscriptions (3-month commitment)

| Tier | Monthly | Photos | Videos | Turnaround |
|------|---------|--------|--------|------------|
| Starter | $297/mo | 15 | 3 | 48 hours |
| Growth | $597/mo | 40 | 10 | 24 hours (priority) |
| Pro | $997/mo | 100 | 25 | Same-day rush |

### One-Time Packs (no commitment)

| Pack | Price | Includes |
|------|-------|----------|
| Starter Pack | $497 | 25 photos + 3 videos |
| Menu Refresh | $997 | Full menu (up to 60 items) + print/digital formats |
| Grand Opening | $1,497 | 100 photos + 10 videos + social media launch kit + Google Business setup |

### Money-Back Guarantee

Every plan and pack comes with a quality guarantee: if the customer isn't satisfied with their first batch of enhanced content, we either redo it at no charge or issue a full refund — their choice. This is the key to making the $497 Starter Pack work as a low-risk entry point. The before/after difference is so dramatic that refund requests are effectively zero, but the guarantee removes the last objection standing between "interested" and "purchased."

For subscriptions, if a customer isn't seeing results after 30 days, we work with them to make it right before they consider canceling. This feeds into the churn prevention system — customers flagged as dissatisfied get personal outreach before they ever hit the cancel button.

### Revenue Projections

| Clients | Avg Revenue | MRR | ARR |
|---------|-------------|-----|-----|
| 10 | $597 | $5,970 | $71,640 |
| 50 | $597 | $29,850 | $358,200 |
| 100 | $597 | $59,700 | $716,400 |
| 500 | $597 | $298,500 | $3,582,000 |
| 1,000 | $597 | $597,000 | $7,164,000 |

---

## Tech Stack

| Tool | Role | Cost |
|------|------|------|
| n8n | Automation engine (12 workflows) | Self-hosted (free) |
| Instantly.ai | Cold email sending (7 campaigns, 1K/day) | $37/mo |
| Airtable | Database + CRM (7 tables) | Free tier |
| FanBasis | Payment processing (6 products) | Per-transaction |
| Apify | Email enrichment (scrape restaurant websites) | Pay-per-use |
| WaveSpeed AI | Photo enhancement | Pay-per-use |
| Kling 3.0 | Video generation | Pay-per-use |
| Vercel/Netlify | Landing page hosting | Free tier |
| Slack | Team notifications (leads, sales, alerts) | Free tier |

**Total monthly overhead: ~$45-75/mo.** AI enhancement and payment processing costs are per-transaction, covered by customer revenue.

---

## Project Structure

```
cravemode-ai/
├── site/                          # Landing page (deploy to Vercel/Netlify)
│   ├── index.html                 # Full landing page with pricing, gallery, FAQ
│   ├── styles.css                 # Modern responsive styles
│   └── script.js                  # Interactivity + form handling
│
├── workflows/                     # n8n workflow JSONs (import to n8n)
│   ├── instantly-lead-upload.json       # Upload leads to Instantly campaigns
│   ├── instantly-reply-handler.json     # Handle email opens/replies/bounces
│   ├── landing-page-form-handler.json   # Process landing page inquiries
│   ├── payment-webhook-handler.json     # Process payments → create customers
│   ├── onboarding-sequence.json         # 3-email welcome sequence
│   ├── asset-delivery-pipeline.json     # Auto-deliver enhanced photos/videos
│   ├── quota-monthly-reset.json         # Reset quotas on 1st of month
│   ├── ghost-lead-reviver.json          # Re-engage silent leads daily
│   ├── churn-risk-detector.json         # Calculate churn risk scores daily
│   ├── upsell-automation.json           # Detect upgrade opportunities weekly
│   ├── metrics-snapshot.json            # Daily business metrics snapshot
│   └── cross-campaign-orchestrator.json # Prevent over-emailing (max 2/lead/day)
│
├── emails/                        # All email templates (markdown)
│   ├── cold-outreach/             # 3-email Instantly campaign
│   ├── inquiry-nurture/           # 4-email nurture for landing page leads
│   ├── abandoned-cart/            # 3-email cart recovery
│   ├── onboarding/                # 3-email welcome sequence
│   ├── churn-prevention/          # Risk-tiered retention emails
│   ├── upsell/                    # Upgrade opportunity emails
│   └── re-engagement/             # Ghost revival + cold re-engagement
│
├── vsl/                           # Video Sales Letter
│   └── script.md                  # Full 5-minute VSL script with visual cues
│
└── docs/                          # Documentation
    ├── airtable-schema.md         # Complete Airtable table/field definitions
    ├── instantly-campaigns.md     # All 7 Instantly campaigns with settings
    ├── human-actions.md           # Manual setup checklist (23 tasks)
    └── deployment-guide.md        # Step-by-step deployment instructions
```

---

## Quick Start

### 1. Start Email Warmup (Do This First — 2-3 Week Lead Time)
1. Sign up for Instantly.ai ($37/mo Growth plan)
2. Purchase a separate sending domain (e.g., `getcravemode.com`) — never send cold emails from your main domain
3. Add sending domain to Instantly + configure DNS (SPF, DKIM, DMARC)
4. Enable warmup on all sending accounts — this takes 2-3 weeks before you can send at volume
5. Get your Instantly API key (Settings → Integrations → API)

### 2. Set Up Airtable
Follow `docs/airtable-schema.md` to create all 7 tables in order (Leads → Customers → Deliveries → Conversations → Metrics → A/B Tests → Optimization Log).

### 3. Deploy Landing Page
```bash
cd site/
# Option A: Vercel
npx vercel

# Option B: Netlify
npx netlify deploy --prod

# Option C: Any static host
# Just upload index.html, styles.css, script.js
```

### 4. Set Up Payments
1. Create 6 products in FanBasis (3 subscriptions + 3 one-time packs)
2. Configure webhook endpoint to point at your n8n payment handler
3. Update landing page buy buttons with real FanBasis checkout URLs

### 5. Import n8n Workflows
1. Open your n8n instance
2. Import each JSON from `workflows/` folder
3. Configure credentials: Instantly API, Airtable API, FanBasis webhook, Slack webhook, SMTP
4. Test each workflow individually before activating

### 6. Set Up Slack Notifications
Create 3 channels: `#cravemode-leads`, `#cravemode-sales`, `#cravemode-alerts`. Create incoming webhooks for each and add to n8n workflows.

### 7. Create Demo Gallery
Run your n8n enhancement workflow on sample restaurant photos. Curate 6-8 of the most dramatic before/after pairs. Include 2-3 Kling 3.0 video clips.

### 8. Record VSL
Use `vsl/script.md` as your teleprompter. Upload to YouTube (unlisted) or Vimeo. Embed on landing page.

### 9. Load First Leads + Go Live
1. Verify Instantly warmup is complete (80%+ score)
2. Load first 200-500 restaurant leads into Airtable
3. Activate n8n workflows one by one (10 min between each)
4. Start Instantly campaign at 25/day, monitor deliverability
5. Ramp to 100/day in week 2, 200+/day in week 3

---

## Launch Timeline

```
Week 0 (Day 1):
  START email warmup in Instantly ← Do this FIRST
  Sign up for Airtable, create tables
  Register sending domain + landing page domain

Week 0-1:
  Build landing page
  Set up FanBasis products
  Create demo gallery (run enhancement workflow on sample restaurants)
  Set up Slack channels + n8n credentials

Week 1-2:
  Record VSL video
  Upload and embed on landing page
  Import and configure all n8n workflows
  Test full purchase flow end-to-end
  Set up analytics

Week 2-3 (warmup complete):
  Load first 500 leads
  Send first 50 test emails (25/day)
  Monitor deliverability (target: 40%+ open rate, <5% bounce)
  Activate reply handling

Week 3-4:
  Ramp to 100 emails/day
  First customers coming in
  Activate delivery + onboarding workflows
  Collect first testimonials

Week 4+:
  Scale to 200-1,000 emails/day
  Activate nurture + ghost revival sequences
  Start A/B testing
  Weekly optimization reviews
```

---

## Monitoring + Ongoing

**Daily (5 min):** Check Slack channels, glance at Airtable pipeline, respond to hot leads.

**Weekly (30 min):** Review metrics dashboard (MRR, conversion rates, churn), check A/B test results, identify funnel bottlenecks.

**Monthly (1-2 hours):** Full funnel analysis, cohort analysis, LTV by channel, unit economics review. Refresh demo gallery with best new transformations. Run re-engagement on cold leads. Clean bounces and unsubscribes.

---

## Monthly Operating Costs

| Service | Cost | Required |
|---------|------|----------|
| Instantly.ai (Growth) | $37/mo | Yes |
| Sending domain | $10-15/year | Yes |
| Landing page (Carrd/Framer) | $5-19/mo | Yes |
| Airtable | Free tier | Yes |
| n8n | Self-hosted (free) or $20/mo cloud | Yes |
| Slack | Free tier | Yes |
| Analytics (Plausible) | $9/mo | Optional (GA4 is free) |
| Email enrichment (Apify) | Free tier | Yes |
| **Total minimum** | **~$45/mo** | |
| **Total comfortable** | **~$75/mo** | |

WaveSpeed AI, Kling 3.0, and FanBasis costs are per-transaction and covered by customer revenue.

---

## Full Documentation

| Doc | What's Inside |
|-----|---------------|
| `docs/human-actions.md` | Complete manual setup checklist — 23 tasks organized by phase with time estimates (12-18 hours total, spread across 2-3 weeks) |
| `docs/deployment-guide.md` | Step-by-step deployment instructions with day-by-day timeline, troubleshooting guide for deliverability issues |
| `docs/airtable-schema.md` | All 7 tables with every field, type, formula, and recommended views. Cross-table relationships and setup order |
| `docs/instantly-campaigns.md` | All 7 Instantly campaigns with email timing, daily volume allocation, sending account distribution, warmup schedule, and API reference |
| `vsl/script.md` | Full 5-minute VSL script with visual cues, B-roll shot list, recording tips, and editing guidance |