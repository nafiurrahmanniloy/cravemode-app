# CraveMode AI — Full SEO Audit Report

**Domain:** https://getcravemode.com
**Framework:** Next.js 15.5.12 (App Router) + Tailwind CSS + Framer Motion
**Audit Date:** 2026-03-11
**Total Indexable Pages:** ~87 URLs across 9 content categories
**Deployment Status:** NOT YET DEPLOYED (local dev only)

---

## Executive Summary

### Overall SEO Health Score: 68/100

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Technical SEO | 25% | 82/100 | 20.5 |
| Content Quality | 25% | 58/100 | 14.5 |
| On-Page SEO | 20% | 78/100 | 15.6 |
| Schema / Structured Data | 10% | 72/100 | 7.2 |
| Performance (CWV) | 10% | 60/100 | 6.0 |
| Images | 5% | 55/100 | 2.75 |
| AI Search Readiness | 5% | 48/100 | 2.4 |
| **TOTAL** | **100%** | | **68.95** |

### Business Type Detected
**SaaS / Professional Service** — AI-powered food photography enhancement for restaurants. B2B service with subscription + one-time pricing model.

### Top 5 Critical Issues
1. **Hero images use native `<img>` tags** — 20 images without Next.js optimization (LCP impact)
2. **Fabricated/unverifiable author profiles** — E-E-A-T violation per Google QRG
3. **Zero real client case studies** — No evidence of experience delivering the service
4. **52 FAQPage schemas are restricted** — Google restricted FAQ rich results in Aug 2023 to gov/healthcare only
5. **`/for/*` and `/compare/*` pages are orphaned** — 7 high-value pages with zero internal navigation links

### Top 5 Quick Wins
1. Remove all 52 FAQPage JSON-LD schemas (reduces page weight, removes invalid markup)
2. Add `/for/*` and `/compare/*` links to footer navigation
3. Add `dateModified` to all Article schemas missing it (5 pages)
4. Fix footer anchor links to use full paths (`/#pricing` instead of `#pricing`)
5. Standardize canonical URL format (all relative or all absolute)

---

## 1. Technical SEO (82/100)

### 1.1 Crawlability — PASS

**robots.ts** is well-configured:
- Allows all public marketing pages
- Blocks app-only routes: `/api/`, `/auth/`, `/explore`, `/image`, `/video`, `/gallery`, `/queue`, `/settings`
- AI search bots (`ChatGPT-User`, `Claude-SearchBot`, `PerplexityBot`) explicitly allowed
- AI training bots (`GPTBot`, `anthropic-ai`, `Google-Extended`) blocked
- Sitemap reference included

**Issues:**
- [Medium] `/sign-up` is disallowed in robots.txt but included in sitemap — conflicting signals. Either remove from sitemap or allow crawling.
- [Low] No `crawl-delay` directive (minor, not needed pre-launch).

### 1.2 Indexability — PASS

- Canonical tags present on every public page via `alternates.canonical`
- No accidental `noindex` on public pages (only 404 page has `noindex`)
- `metadataBase` correctly set to `https://getcravemode.com`

**Issues:**
- [Medium] Canonical format inconsistency — some pages use relative paths (`/pricing`), others use absolute URLs (`${siteUrl}/food-photography/${slug}`). Functional but inconsistent.

### 1.3 Security Headers — PASS (Strong)

| Header | Value | Status |
|--------|-------|--------|
| Content-Security-Policy | Comprehensive (self, Supabase, GA4, Stripe) | PASS |
| Strict-Transport-Security | max-age=63072000; includeSubDomains; preload | PASS |
| X-Frame-Options | DENY | PASS |
| X-Content-Type-Options | nosniff | PASS |
| Referrer-Policy | strict-origin-when-cross-origin | PASS |
| Permissions-Policy | camera=(), microphone=(), geolocation=() | PASS |
| X-Powered-By | Suppressed | PASS |

### 1.4 URL Structure — PASS

All URLs use lowercase, hyphenated slugs. Clean hierarchy. No special characters or trailing slashes.

**Issues:**
- [Medium] No `redirects()` configuration in `next.config.mjs`. Need this post-launch for any URL changes.
- [Low] `/for/fine-dining` URL pattern is semantically weak — `/food-photography-for/fine-dining` would be more descriptive.

### 1.5 Mobile Optimization — PASS

- Viewport configured correctly: `width: device-width`, `initialScale: 1`, `maximumScale: 5`
- PWA manifest with icons (192/512px), screenshots, shortcuts
- Tailwind responsive classes throughout (`sm:`, `md:`, `lg:`)
- `MobileBottomNavServer` for mobile navigation

**Issues:**
- [Low] Manifest `start_url` points to `/explore` (protected route). Should be `/` for unauthenticated PWA installs.

### 1.6 JavaScript Rendering — PASS (with caveats)

All SEO-critical pages are React Server Components with `generateStaticParams()`.

**Issues:**
- [High] `/showcase` page is `"use client"` but publicly indexed — content invisible without JS execution.
- [Medium] Homepage 11 below-fold sections use `next/dynamic` — SEO content not in initial HTML response.

---

## 2. Content Quality (58/100)

### 2.1 E-E-A-T Assessment — 37.6/100 (Weighted)

| Factor | Score | Weight | Weighted |
|--------|-------|--------|----------|
| Experience | 28/100 | 20% | 5.6 |
| Expertise | 52/100 | 25% | 13.0 |
| Authoritativeness | 22/100 | 25% | 5.5 |
| Trustworthiness | 45/100 | 30% | 13.5 |
| **Weighted Total** | | | **37.6/100** |

**Experience (28/100) — CRITICAL:**
- Zero real client case studies or before/after results with named restaurants
- Statistics cited without links or sources ("30% more orders", "35% more clicks")
- Showcase page uses generic sample images, no actual client work
- No founder operational evidence, no "restaurants served" count backed by data

**Expertise (52/100) — HIGH:**
- Author profiles appear fabricated — "Sarah Chen" and "Marcus Rivera" have no external presence, no photos (only initials), no LinkedIn profiles, no author pages
- Blog content demonstrates reasonable industry knowledge but is widely available general information

**Authoritativeness (22/100) — CRITICAL:**
- Zero external citations, press mentions, or "as featured in" section
- No third-party reviews (Trustpilot, G2, Capterra)
- No industry partnerships or guest contributions
- No original research or unique data

**Trustworthiness (45/100) — HIGH:**
- Legal pages exist (privacy, terms, refund)
- Pricing is transparent ($297/$597/$997)
- Money-back guarantee mentioned consistently
- Missing: phone number, physical address, email in footer, company registration info

### 2.2 Blog Content Analysis (9 posts)

| Post | Est. Words | Quality | Key Issue |
|------|-----------|---------|-----------|
| restaurant-social-media-strategy | ~2,200 | 65/100 | Generic advice, no original data |
| food-delivery-photo-optimization | ~2,000 | 70/100 | Good specifics, some unverified claims |
| restaurant-branding-visual-identity | ~1,600 | 62/100 | Relies on well-known brand examples |
| google-business-profile-photos | ~2,200 | 72/100 | Best post — specific and actionable |
| food-photography-roi | ~1,500 | 55/100 | Hypothetical ROI, no real data |
| food-photography-lighting-guide | ~1,400 | 68/100 | Practical, slightly under 1,500w minimum |
| restaurant-video-content-guide | ~1,800 | 65/100 | Good structure, generic advice |
| food-photography-tips | ~1,200 | 60/100 | Below 1,500-word minimum |
| food-photography-cost | ~1,800 | 58/100 | Competitor names may be fabricated |

**Strengths:** Proper heading hierarchy, internal cross-links between posts, tables, published dates, author attribution.

**Weaknesses:**
- Every post ends with identical CraveMode AI sales pitch CTA
- Zero external citations in any blog post
- No inline images in any post (for food photography content, this is glaring)
- AI-generated content markers: uniform structure, consistent paragraph length, generic phrasing
- No comments/engagement mechanism

### 2.3 City Pages (50 pages) — 68/100

**Positive:** All 50 cities have unique content in `city-content.ts` — food scene descriptions, neighborhoods, specialties, local insights. Genuinely differentiated content.

**Issues:**
- [High] FAQ section uses identical questions across all 50 cities with only name substituted — 250 near-duplicate FAQ answers
- [Medium] "How It Works" and cost comparison table are identical template across all pages
- Unique content per city: ~500-800 words unique + ~400 words template

### 2.4 Restaurant Type Pages (5 pages) — 52/100

- Well-differentiated per type but thin at ~350-400 words each
- Below 500-word minimum for service/location pages
- No narrative paragraphs — entirely structured bullet lists

### 2.5 Guide Pages (5 pages) — 55/100

- Thin at ~600-700 words vs. competing content at 1,500-3,000 words
- Blog posts covering same topics are more comprehensive — content cannibalization risk

### 2.6 Comparison Pages (2 pages) — 61/100

- AI vs Photographer: AI wins 8/12 rows with biased visual highlighting
- Managed vs Self-Service: All rows favor CraveMode

---

## 3. On-Page SEO (78/100)

### 3.1 Meta Tags — PASS
- All pages have unique, descriptive titles under 70 characters
- Meta descriptions present on all marketing pages (120-160 chars)
- Complete OG and Twitter card markup with images

### 3.2 Heading Structure — PASS
Proper H1 > H2 > H3 hierarchy across all pages. Blog posts use HTML anchor IDs for deep linking.

### 3.3 Internal Linking — NEEDS IMPROVEMENT

**Positive:**
- Footer links to About, Blog, Pricing, Services, Food Photography, Guides
- City pages cross-link to nearby cities (2-3 each)
- Blog posts link to 2 related articles
- Restaurant type pages link to related types

**Issues:**
- [High] `/for/*` restaurant type pages (5 pages) have zero navigation/footer links — orphaned
- [High] `/compare/*` comparison pages (2 pages) have zero navigation/footer links — orphaned
- [Medium] Footer "Quick Links" use anchor links (`#gallery`, `#pricing`) that only work on homepage — broken on all other pages
- [Medium] No cross-linking between blog posts and related city/guide/service pages
- [Low] No blog category/tag pages for topical organization

---

## 4. Schema / Structured Data (72/100)

### Schemas Detected

| Page | Schema Types | Status |
|------|-------------|--------|
| Root layout | Organization, WebSite (SearchAction) | PASS |
| Landing page | Service (OfferCatalog), ~~FAQPage~~ | Service PASS, FAQ REMOVE |
| Pricing | BreadcrumbList, Service (OfferCatalog), ~~FAQPage~~ | PASS except FAQ |
| Blog index | BreadcrumbList, CollectionPage, ItemList | PASS |
| Blog posts | BreadcrumbList, Article | PASS |
| City pages (x50) | Service (areaServed), BreadcrumbList, ~~FAQPage~~ | PASS except FAQ |
| Type pages (x5) | Service, BreadcrumbList | PASS |
| Services hub | BreadcrumbList | PASS |
| Photo enhancement | BreadcrumbList, Service | PASS |
| Video creation | BreadcrumbList, Service, VideoObject | PASS |
| Photo checker | BreadcrumbList, SoftwareApplication | PASS |
| Showcase | ImageGallery | PASS (minimal) |
| Guides (x5) | BreadcrumbList, Article | PASS |
| Comparisons (x2) | BreadcrumbList, Article | PASS |

### Critical: FAQPage Schema Restricted (52 pages)

Google restricted FAQ rich results to government/healthcare sites in August 2023. **52 pages** have FAQPage JSON-LD that will never generate rich results:
- Landing page (1)
- Pricing page (1)
- All 50 city pages

**Action:** Remove all FAQPage JSON-LD to reduce page weight.

### Other Schema Issues

- [Medium] ImageGallery on showcase has no actual `image` array
- [Medium] 5 pages have Article schema without `dateModified` (guides + comparisons)
- [Medium] Managed-vs-self-service Article missing `image` property (blocks rich results)
- [Low] Inconsistent provider/publisher — some use `@id` reference, others use inline Organization
- [Low] Photo enhancement `offerCount` is number instead of string
- [Low] WebSite SearchAction points to `/blog?q=` which may not have search functionality
- [Low] Dead breadcrumb parent links (`/tools`, `/compare` may not exist as pages)

### Missing Schema Opportunities

1. **Product schema** on pricing page — can trigger price display in search
2. **ProfessionalService** — helps with "near me" queries
3. **AggregateRating/Review** on showcase (when real reviews exist)
4. **BreadcrumbList** on showcase page (currently missing)
5. **Do NOT add HowTo or FAQ** — both removed from rich results by Google

---

## 5. Performance / Core Web Vitals (60/100)

### LCP Risks
- [Critical] `CosmosHero.tsx` uses 20 native `<img>` tags — no responsive srcset, no AVIF/WebP, no lazy loading. LCP depends on client JS.
- [Medium] 3 hero images preloaded with `fetchPriority="high"` (partial mitigation)
- [Medium] 11 homepage sections use `next/dynamic` — content not in initial server response

### INP Risks
- [Medium] Footer has 20+ Framer Motion `<motion.*>` elements with spring physics on every page
- [Low] `content-visibility: auto` applied to below-fold sections (positive)

### CLS Risks
- [Medium] Hero images use absolute positioning with fixed dimensions (mitigates flow impact)
- [Low] Variable fonts (Inter, Playfair) prevent FOIT/FOUT

### Build Config — PASS
- AVIF/WebP image optimization, responsive sizes, 31-day cache TTL
- ISR configured (dynamic: 180s, static: 300s)
- View transitions, optimized package imports

---

## 6. Images (55/100)

- [Critical] Hero uses native `<img>` tags — no Next.js optimization
- [High] Blog posts have zero inline images — food photography content with no photos
- [Medium] Showcase ImageGallery schema has no image data
- [Low] `/cosmos` page generic alt text ("Food 1", "Food 2") — blocked by robots.txt

**Positive:** next.config.mjs properly configured for AVIF/WebP, responsive sizes, 31-day cache.

---

## 7. AI Search Readiness (48/100)

| Factor | Score | Finding |
|--------|-------|---------|
| llms.txt | 85/100 | Comprehensive file with services, pricing, FAQ, contact |
| Schema markup | 82/100 | Excellent structured data layer |
| Heading hierarchy | 85/100 | Well-structured across all pages |
| Quotable statistics | 35/100 | Present but unsourced |
| Unique insights | 25/100 | No original research or proprietary data |
| Source attribution | 15/100 | Zero external links in blog content |
| Content freshness | 70/100 | All dated 2026, `updatedAt` used on some posts |

**AI Bot Policy (Smart):**
- ALLOWED: ChatGPT-User, Claude-SearchBot, PerplexityBot (citation/retrieval)
- BLOCKED: GPTBot, anthropic-ai, Google-Extended, CCBot (training)

---

## 8. Sitemap Analysis (90/100)

87 total URLs generated dynamically from shared data sources.

| Category | Count |
|----------|-------|
| Core marketing | 5 |
| Service pages | 3 |
| Guide pages | 6 |
| Compare pages | 2 |
| Restaurant types | 5 |
| Blog (hub + 9 posts) | 10 |
| City (hub + 50 cities) | 51 |
| Tool pages | 2 |
| Legal pages | 3 |
| **Total** | **87** |

- No phantom URLs, no missing indexable pages
- Protected routes correctly excluded
- Data sources synchronized between sitemap and page routes

**Issues:**
- [Low] Synthetic `lastModified` dates for city and type pages (index-based formula)
- [Low] Identical dates on guide/compare/legal page batches

---

## 9. Social Link Inconsistency

Organization schema `sameAs` uses `cravemodeai` handles but footer links use `cravemode` (without `ai`). Must be reconciled.

---

## What Is Working Well

1. Canonical tags on every page
2. Rich structured data — 10+ schema types
3. Security headers — full suite with HSTS preload
4. Static generation for all SEO pages via `generateStaticParams()`
5. Unique city content — 50 cities with hand-written differentiated prose
6. Smart AI bot management in robots.txt
7. Comprehensive llms.txt for AI discoverability
8. Custom 404 page with noindex
9. Breadcrumb schemas on nearly every page
10. AVIF/WebP image optimization config
11. PWA manifest with icons, screenshots, shortcuts
12. Skip-to-content accessibility link
13. Flat, clean URL structure
14. Data-synchronized sitemap (eliminates URL drift)
15. Blog Article schema with author, dates, publisher

---

## Key Statistics

| Metric | Value |
|--------|-------|
| Total indexable pages | ~87 |
| Pages with structured data | 80+ |
| Blog posts | 9 |
| City pages | 50 |
| Restaurant type pages | 5 |
| Guide pages | 5 |
| Comparison pages | 2 |
| Pages with FAQPage (to remove) | 52 |
| Orphaned high-value pages | 7 |
| Blog posts with external citations | 0 |
| Named case studies/testimonials | 0 |

---

*Generated by CraveMode AI SEO Audit — 2026-03-11*
