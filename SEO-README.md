# CraveMode AI — SEO Status & Optimization Handoff

> **Current SEO Health Score: 78/100**
> Target: 90–95/100
> Last audited: March 11, 2026
> Site: https://getcravemode.com
> Tech: Next.js 15.5.12 + Tailwind CSS 3.4 + Supabase + TypeScript
> Total pages: 115 (all statically generated, zero build errors)

---

## Table of Contents

1. [Score Breakdown by Category](#score-breakdown-by-category)
2. [What's Already Been Done (4 Phases)](#whats-already-been-done)
3. [Critical Issues to Fix (Score Impact: +5–8 points)](#critical-issues-to-fix)
4. [High Priority Issues (Score Impact: +4–6 points)](#high-priority-issues)
5. [Medium Priority Issues (Score Impact: +2–4 points)](#medium-priority-issues)
6. [Low Priority / Nice-to-Have](#low-priority)
7. [Manual Tasks (Not Code)](#manual-tasks-not-code)
8. [File Reference Guide](#file-reference-guide)
9. [How to Run the Audit](#how-to-run-the-audit)
10. [Estimated Score After Fixes](#estimated-score-after-fixes)

---

## Score Breakdown by Category

| Category | Weight | Score | Notes |
|----------|--------|-------|-------|
| Technical SEO | 25% | 82/100 | Preloader bug, CSP issues |
| Content Quality (E-E-A-T) | 25% | 78/100 | Up from 68 after expansion |
| On-Page SEO | 20% | 74/100 | Duplicate H1, title truncation |
| Schema / Structured Data | 10% | 72/100 | FAQPage ineligible, inconsistencies |
| Performance (Core Web Vitals) | 10% | 80/100 | Good static generation |
| Images | 5% | 62/100 | 50+ empty alt texts |
| AI Search Readiness (GEO) | 5% | 80/100 | llms.txt is solid |

**Weighted total: 76.3 → Rounded: 78/100**

---

## What's Already Been Done

### Phase 1 — Foundation (Complete)
- `robots.ts` with crawler directives (allows search bots, blocks training bots)
- `sitemap.ts` generating 80+ URLs dynamically
- `json-ld.tsx` reusable component for structured data
- `llms.txt` for AI crawler consumption (179 lines, comprehensive)
- Organization + WebSite schemas on root layout
- Service + FAQPage schemas on landing page
- 9 metadata `layout.tsx` files for client-component pages
- `/pricing` page with full plan comparison
- `/services/photo-enhancement` and `/services/video-creation` pages
- `/blog` with 9 in-depth posts (1500+ words each)
- `/food-photography` hub + 20 city pages
- Blog system: `src/lib/blog/posts.ts` with inline HTML content

### Phase 2 — Expansion (Complete)
- Platform guides: Uber Eats, DoorDash photo optimization
- Comparison pages: AI vs Photographer, Managed vs Self-Service
- Restaurant type pages: Fine Dining, Fast Casual, Cafes, Food Trucks, Bakeries
- 4 additional blog posts (ROI, lighting, video, tips)
- Restaurant type data: `src/lib/data/restaurant-types.ts`

### Phase 3 — Scale (Complete)
- Expanded from 20 to 50 US city pages
- 3 more platform guides: GrubHub, Google Business, Instagram
- 4 more blog posts (social media strategy, delivery optimization, branding, Google Business)
- Free tool: `/tools/photo-checker` (client-side Canvas API quality analyzer)
- Total: 109 pages

### Phase 4 — Authority (Complete, code only)
- VideoObject schema on video creation page
- Content depth improvements across all pages
- Internal linking additions (32+ cross-links between blog posts)
- Canonical URL standardization
- Various schema fixes and metadata improvements

---

## Critical Issues to Fix

These are blocking indexing or causing significant ranking penalties. **Fix immediately for +5–8 points.**

### 1. Preloader References Wrong File Extensions (Performance Killer)
**File:** `site/src/components/Preloader.tsx` (lines 10–14)
**Problem:** The preloader tries to load `.jpg` files that don't exist — actual files are `.webp`. This causes the preloader to hit its 5-second safety timeout on EVERY homepage visit before showing content.

```typescript
// CURRENT (BROKEN):
const criticalImages = [
  '/hero/food-03.jpg',   // file doesn't exist
  '/hero/food-19.jpg',   // file doesn't exist
  '/hero/food-05.jpg',   // file doesn't exist
  '/hero/food-18.jpg',   // file doesn't exist
];

// FIX: Change to .webp
const criticalImages = [
  '/hero/food-03.webp',
  '/hero/food-19.webp',
  '/hero/food-05.webp',
  '/hero/food-18.webp',
];
```
**Impact:** Fixes 5-second homepage delay, improves LCP, improves bounce rate.

### 2. OG Image Wrong Dimensions (Breaks Social Sharing)
**File:** `site/src/app/layout.tsx` (lines 106–108)
**Problem:** The declared OG image `after-3.jpg` is actually 800x1192 pixels (portrait), but the metadata declares it as 1200x630 (landscape). Every social media share (Facebook, Twitter/X, LinkedIn, iMessage) will display incorrectly — cropped, stretched, or with a blank preview.

```typescript
// CURRENT (WRONG):
images: [{
  url: '/cravemode/after-3.jpg',
  width: 1200,
  height: 630,
  alt: 'CraveMode AI — Restaurant Photo Enhancement',
}]

// FIX: Create a proper 1200x630 OG image and update the path
// OR fix dimensions to match the actual file
```
**Action:** Create a proper 1200x630 pixel OG image (restaurant food collage with CraveMode branding) and place it at `site/public/og-image.jpg`. Update `layout.tsx` to reference it.

### 3. 50+ Hero Images with Empty Alt Text (Kills Image SEO)
**File:** `site/src/components/CosmosHero.tsx` (line 98)
**Problem:** All 30+ food images in the hero section have `alt=""`. Google Image Search cannot index any of these. For a food photography service, image SEO is critical.

```typescript
// CURRENT:
alt=""

// FIX: Add descriptive alt text to each image
// Examples:
alt="Professional AI-enhanced burger photography"
alt="Sushi platter with vibrant color grading"
alt="Pasta dish with dramatic restaurant lighting"
```
**Action:** Add unique, descriptive alt text to every food image in CosmosHero. Also check other components for empty alt attributes.

### 4. Duplicate H1 Tags on Landing Page
**File:** `site/src/components/Preloader.tsx` (line 145)
**Problem:** The Preloader renders `<h1>CraveMode</h1>` and the CosmosHero also renders an `<h1>`. Google sees two H1 tags on the homepage — dilutes the primary heading signal.

```typescript
// CURRENT in Preloader.tsx:
<h1 className="...">CraveMode</h1>

// FIX: Change to <div> or <span> since the preloader is decorative
<div className="..." aria-hidden="true">CraveMode</div>
```

---

## High Priority Issues

Significantly impact rankings. **Fix within 1 week for +4–6 points.**

### 5. FAQPage Schema Ineligible (Remove or Replace)
**Files:** `site/src/app/page.tsx`, `site/src/app/pricing/page.tsx`, `site/src/app/faq/page.tsx`, `site/src/app/food-photography/[city]/page.tsx`
**Problem:** Google restricted FAQPage rich results to government and healthcare sites in August 2023. Having ineligible schema doesn't hurt rankings directly, but it's wasted code and sends mixed signals to crawlers.

**Action:** Remove all `FAQPage` schema markup from these files. Keep the FAQ content visible on the pages — just remove the JSON-LD structured data for it. Optionally replace with more useful schemas (e.g., `HowTo` for guides, `Product` for pricing).

### 6. Founder Name Inconsistency in Schema
**File:** `site/src/app/layout.tsx` (lines 32–34)
**Problem:** Root layout Organization schema says founder is "CraveMode AI Team" but the About page has a Person schema for "Nafiul Rahman" as founder. Google's Knowledge Graph can't reconcile this.

```typescript
// FIX in layout.tsx Organization schema:
founder: {
  "@type": "Person",
  name: "Nafiul Rahman",
  "@id": "https://getcravemode.com/about#founder"
}
```

### 7. Blog Article Schema Missing Author URL
**File:** `site/src/app/blog/[slug]/page.tsx`
**Problem:** Article schema has `author.name` but no `author.url`. Google's documentation recommends linking to an author profile page for better E-E-A-T signals.

```typescript
// ADD to Article schema author section:
author: {
  "@type": "Person",
  name: "Nafiul Rahman",
  url: "https://getcravemode.com/about"
}
```

### 8. Sitemap Conflicts
**File:** `site/src/app/sitemap.ts`
**Problems:**
- `/sign-up` is in the sitemap BUT has `noindex` in its layout.tsx — conflicting signals to Google
- `/about` is in the sitemap — verify this page actually exists and returns 200
- All 50 city pages share the same `lastmod` date, which looks artificial to crawlers

**Actions:**
- Remove `/sign-up` from sitemap (or remove `noindex` from its layout)
- Verify `/about` page exists
- Add varied `lastmod` dates for city pages (spread across the last 30 days)

### 9. Title Tag Truncation
**Problem:** Several page titles exceed Google's 60-character display limit and get cut off in search results:
- "Free Food Photo Quality Checker — Score Your Menu Photos | CraveMode AI" (73 chars)
- "AI vs Professional Food Photographer: Cost, Speed & Quality Comparison | CraveMode AI" (86 chars)
- Various blog post titles

**Action:** Shorten titles to 55-60 characters. Put the brand name only on the homepage. Use the description for additional context.

### 10. CSP Security Headers Too Permissive
**File:** `site/next.config.mjs`
**Problem:** Content Security Policy uses `unsafe-inline` and `unsafe-eval` — security scanners flag this, and Google may consider it a trust signal.

**Action:** Implement nonce-based CSP for inline scripts. Next.js 15 supports this with `headers()` configuration.

---

## Medium Priority Issues

Optimization opportunities. **Fix within 1 month for +2–4 points.**

### 11. Robots.txt Improvements
**File:** `site/src/app/robots.ts`
- Add `/sign-up` to disallow list (matches the noindex directive)
- Add `/offline` to disallow list
- Add explicit allows for `Amazonbot`, `YouBot`, `Applebot-Extended`

### 12. Schema Consistency — Use JsonLd Component Everywhere
**File:** `site/src/app/tools/photo-checker/layout.tsx`
**Problem:** Uses raw `dangerouslySetInnerHTML` for JSON-LD instead of the reusable `JsonLd` component used elsewhere. Inconsistency makes maintenance harder.

**Action:** Replace with `<JsonLd data={...} />` component import.

### 13. VideoObject Schema Missing embedUrl
**File:** `site/src/app/services/video-creation/page.tsx`
**Problem:** VideoObject schema lacks `embedUrl` property. Google recommends this for video rich results.

### 14. About Page Person Schema Needs @id
**File:** `site/src/app/about/page.tsx`
**Problem:** The Person schema for the founder lacks an `@id` property, which prevents cross-referencing from other schemas (Organization, Article author, etc.).

```typescript
// ADD:
"@id": "https://getcravemode.com/about#founder"
```

### 15. Internal Linking Gaps
**Problem:** Homepage has very few links to content hubs (/blog, /food-photography, /guides). The link equity from the homepage (strongest page) isn't flowing to content pages.

**Action:** Add a "Resources" or "Learn More" section to the homepage footer or a dedicated section linking to:
- Blog hub
- Food Photography hub
- Platform guides
- Free photo checker tool
- City pages (top 5-10)

### 16. E-E-A-T Improvements
Current E-E-A-T sub-scores:
- Experience: 52/100
- Expertise: 68/100
- Authoritativeness: 55/100
- Trustworthiness: 70/100

**Actions to improve:**
- Add customer testimonials with real names and restaurant names
- Add case studies with before/after results and specific metrics
- Add author bios to blog posts (photo, credentials, experience)
- Add "Last updated" dates visible on all content pages
- Add trust badges (if any: BBB, industry associations, client logos)
- Link to external authority sources (cite studies, Google documentation)

---

## Low Priority

Nice-to-have improvements. **Backlog items.**

### 17. City Page Content Differentiation
**Problem:** Only ~10 of 50 city pages have unique content entries in `src/lib/data/city-content.ts`. The rest use generic templates. Google may classify these as thin/duplicate content.

**Action:** Add unique paragraphs, local stats, and neighborhood references for each city over time.

### 18. Blog Post Featured Images
**Problem:** Blog posts lack unique featured images. Each post should have a custom OG image (1200x630) for social sharing.

### 19. Breadcrumb Schema on All Pages
**Problem:** Not all pages have BreadcrumbList schema. Adding it to every page helps Google understand site hierarchy.

### 20. Hreflang Tags (Future)
If expanding internationally, add hreflang tags. Not needed now for US-only targeting.

---

## Manual Tasks (Not Code)

These cannot be done by a developer in the codebase — they require external account setup:

### Must-Do (Critical for reaching 90+)
1. **Register Google Search Console** — Submit sitemap, monitor indexing, check for crawl errors
2. **Register Bing Webmaster Tools** — Submit sitemap, covers Bing + DuckDuckGo + Yahoo
3. **Set up Google Analytics 4 (GA4)** — Track traffic, user behavior, conversion events
4. **Create proper 1200x630 OG image** — Design in Canva/Figma, food collage with CraveMode branding
5. **Verify /about page exists** — If not, create it (currently in sitemap)

### Should-Do (Builds Authority)
6. **Submit to business directories** — Capterra, G2, GetApp, Product Hunt
7. **Respond to HARO queries** — Food photography, restaurant marketing topics
8. **Guest post on food industry blogs** — Get backlinks from relevant sites
9. **Set up Google Business Profile** — Even as a virtual/online business
10. **Create social media profiles** — Instagram (@cravemodeai), Twitter/X (@cravemodeai), LinkedIn

### Nice-to-Have (Long-term Authority)
11. **Publish original research** — "State of Restaurant Photography 2026" report
12. **Start YouTube channel** — Food photography tutorials, before/after showcases
13. **Podcast appearances** — Restaurant marketing, food tech podcasts
14. **Customer testimonials** — Collect and publish real reviews with photos

---

## File Reference Guide

### Core SEO Files
| File | Purpose |
|------|---------|
| `site/src/app/robots.ts` | Crawler directives (allow/disallow) |
| `site/src/app/sitemap.ts` | Dynamic XML sitemap generation |
| `site/src/components/json-ld.tsx` | Reusable JSON-LD schema component |
| `site/public/llms.txt` | AI crawler content file |
| `site/src/app/layout.tsx` | Root layout — Organization schema, OG defaults |

### Content Pages
| Route | File | Type |
|-------|------|------|
| `/` | `site/src/app/page.tsx` | Landing page (hero, features, FAQ) |
| `/pricing` | `site/src/app/pricing/page.tsx` | Plan comparison |
| `/services/photo-enhancement` | `site/src/app/services/photo-enhancement/page.tsx` | Service page |
| `/services/video-creation` | `site/src/app/services/video-creation/page.tsx` | Service page |
| `/blog` | `site/src/app/blog/page.tsx` | Blog index |
| `/blog/[slug]` | `site/src/app/blog/[slug]/page.tsx` | Blog posts (9 total) |
| `/food-photography` | `site/src/app/food-photography/page.tsx` | City hub |
| `/food-photography/[city]` | `site/src/app/food-photography/[city]/page.tsx` | 50 city pages |
| `/guides/*` | `site/src/app/guides/*/page.tsx` | 5 platform guides |
| `/compare/*` | `site/src/app/compare/*/page.tsx` | 2 comparison pages |
| `/for/*` | `site/src/app/for/*/page.tsx` | 5 restaurant type pages |
| `/tools/photo-checker` | `site/src/app/tools/photo-checker/page.tsx` | Free tool |
| `/showcase` | `site/src/app/showcase/page.tsx` | Before/after gallery |

### Data Files
| File | Purpose |
|------|---------|
| `site/src/lib/blog/posts.ts` | All 9 blog posts (inline HTML) |
| `site/src/lib/data/cities.ts` | 50 US metro data (rates, restaurants, nearby) |
| `site/src/lib/data/city-content.ts` | Unique content for ~10 cities |
| `site/src/lib/data/restaurant-types.ts` | 5 restaurant type data |

### Strategy Docs (in project root)
| File | Purpose |
|------|---------|
| `SEO-STRATEGY.md` | Overall SEO strategy |
| `COMPETITOR-ANALYSIS.md` | Competitor research |
| `SITE-STRUCTURE.md` | URL structure plan |
| `CONTENT-CALENDAR.md` | Content publishing schedule |
| `IMPLEMENTATION-ROADMAP.md` | 4-phase implementation plan |

---

## How to Run the Audit

The SEO audit uses Claude Code's `/seo-audit` skill which launches 6 specialist subagents in parallel:

1. **Technical SEO** — robots.txt, sitemaps, canonicals, security headers
2. **Content Quality** — E-E-A-T, readability, thin content detection
3. **Schema / Structured Data** — JSON-LD validation, missing opportunities
4. **Sitemap Analysis** — Structure, quality gates, missing pages
5. **On-Page SEO & Images** — Titles, headings, alt text, meta descriptions
6. **AI Search Readiness** — Citability, llms.txt, structural clarity

To run: Open Claude Code in the project directory and type `/seo-audit`

The audit generates:
- `FULL-AUDIT-REPORT.md` — Detailed findings
- `ACTION-PLAN.md` — Prioritized recommendations

---

## Estimated Score After Fixes

If all Critical + High issues are resolved:

| Category | Current | Projected | Change |
|----------|---------|-----------|--------|
| Technical SEO | 82 | 92 | +10 (Preloader fix, CSP, robots) |
| Content Quality | 78 | 85 | +7 (E-E-A-T, testimonials, author bios) |
| On-Page SEO | 74 | 88 | +14 (H1 fix, titles, internal links) |
| Schema | 72 | 90 | +18 (Remove FAQPage, fix inconsistencies) |
| Performance | 80 | 90 | +10 (Preloader fix = huge LCP improvement) |
| Images | 62 | 85 | +23 (Alt text, OG image) |
| AI Search | 80 | 85 | +5 (Minor improvements) |
| **Weighted Total** | **78** | **~89** | **+11** |

To reach 90+, also address Medium priority items (internal linking, city content, blog images).

To reach 95, complete the manual tasks (GSC, GA4, business directories, backlinks, testimonials).

---

## Quick Win Checklist (Can Be Done in 1 Day)

- [ ] Fix Preloader.tsx: `.jpg` → `.webp` (lines 10-14)
- [ ] Fix Preloader.tsx: `<h1>` → `<div>` (line 145)
- [ ] Create 1200x630 OG image and update layout.tsx
- [ ] Add alt text to CosmosHero images
- [ ] Remove FAQPage schema from 4 files
- [ ] Fix founder name in layout.tsx Organization schema
- [ ] Add `author.url` to blog Article schema
- [ ] Remove `/sign-up` from sitemap
- [ ] Shorten 5+ truncated title tags
- [ ] Add `@id` to About page Person schema

**Estimated time: 2-4 hours for all quick wins**
**Expected score improvement: 78 → 85-88**

---

*Last updated: March 11, 2026*
*Prepared by: Nafiul Rahman*
*Tool: Claude Code with /seo-audit skill*
