# CraveMode AI — SEO Action Plan

**Current Score: 68/100**
**Target Score: 85/100**

Prioritized fixes organized by impact and effort. Completing Critical + High items would raise the score to approximately 82-88/100.

---

## CRITICAL — Fix Before Deployment

### 1. Remove all 52 FAQPage schemas
**Impact:** Removes restricted/invalid structured data from 52 pages
**Files:**
- `site/src/app/page.tsx` (landing page FAQPage JSON-LD)
- `site/src/app/pricing/page.tsx` (pricing FAQPage JSON-LD)
- `site/src/app/food-photography/[city]/page.tsx` (city pages FAQPage JSON-LD)
**Details:** Google restricted FAQ rich results to government/healthcare sites in August 2023. These 52 FAQPage schemas add page weight but will never generate rich results. Keep FAQ content on the page for users — just remove the JSON-LD wrapper.

### 2. Convert hero images to Next.js `<Image>` component
**Impact:** Fixes LCP on highest-traffic page, enables AVIF/WebP, responsive srcset
**File:** `site/src/components/CosmosHero.tsx`
**Details:** 20 food images use native `<img>` tags. Convert to `next/image` with `sizes` prop, `priority` on first 4 visible images, and `loading="lazy"` on the rest. This is the single biggest Core Web Vitals improvement.

### 3. Create verifiable author profiles OR remove individual bylines
**Impact:** Fixes critical E-E-A-T violation
**Files:** `site/src/lib/data/authors.ts`, `site/src/lib/blog/posts.ts`
**Details:** "Sarah Chen" and "Marcus Rivera" have no verifiable external presence. Either:
- **Option A:** Build `/blog/author/[slug]` pages with headshots, LinkedIn links, and verified credentials
- **Option B:** Remove individual bylines and attribute all content to "CraveMode AI Team"
Fabricated author personas are a direct Google QRG violation.

### 4. Add real case studies with named clients
**Impact:** Transforms Experience score from 28/100 to 60+/100
**Details:** Even 2-3 detailed case studies with real restaurant names, before/after photos, and measurable results (e.g., "Bella Trattoria in Austin saw a 28% increase in DoorDash orders") would be transformative. This is the #1 content gap.

---

## HIGH PRIORITY — Significant SEO Impact (Fix within 1-2 weeks)

### 5. Fix orphaned pages — add `/for/*` and `/compare/*` to navigation
**Impact:** 7 high-value pages gain internal link equity
**Files:**
- `site/src/components/sections/footer.tsx` — add "Restaurant Types" and "Compare" sections
- `site/src/app/services/page.tsx` — cross-link to restaurant type pages
- `site/src/app/pricing/page.tsx` — link to comparison pages
**Details:** 5 restaurant type pages and 2 comparison pages have zero internal navigation links. These are discoverable only via sitemap. Add footer links, cross-links from related pages.

### 6. Source all statistics with linked citations
**Impact:** E-E-A-T expertise + AI citation readiness (+5 points)
**Files:** `site/src/lib/blog/posts.ts`, `site/src/lib/data/city-content.ts`
**Details:** Every "X% of diners" claim needs a linked source:
- "30% more orders on delivery platforms" → Link to DoorDash/Uber Eats merchant resources
- "35% more clicks on Google Business Profile" → Link to Google study
- "77% of diners check social media" → Link to Toast/Square/Yelp survey
Zero external citations in 9 blog posts and 50 city pages is a major trust gap.

### 7. Fix footer anchor links for non-homepage pages
**Impact:** Fixes broken navigation on 80+ pages
**File:** `site/src/components/sections/footer.tsx`
**Details:** Quick Links use `#gallery`, `#pricing`, `#faq` — these only work on homepage. On city/blog/guide pages they do nothing. Change to `/#gallery`, `/#pricing`, `/#faq` (full paths).

### 8. Add inline images to blog posts
**Impact:** Image search traffic + engagement + content quality
**File:** `site/src/lib/blog/posts.ts`
**Details:** For food photography content, having zero images in blog posts is a glaring omission. Add 2-3 before/after examples, lighting setup diagrams, or annotated screenshots per post.

### 9. Server-render the Showcase page
**Impact:** Makes social proof visible to search engines
**File:** `site/src/app/showcase/page.tsx`
**Details:** Currently `"use client"` — content invisible without JS. Server-render the image grid and hydrate only the interactive slider on the client.

### 10. Add `dateModified` to all Article schemas
**Impact:** Freshness signals for 5+ pages
**Files:** Guide pages (5), comparison pages (2)
**Details:** Google uses `dateModified` for freshness ranking. Currently missing from all guide and comparison page Article schemas.

---

## MEDIUM PRIORITY — Quality Improvements (Fix within 1 month)

### 11. Expand restaurant type pages to 800+ words
**Files:** `site/src/lib/data/restaurant-types.ts`, `site/src/app/for/[type]/page.tsx`
**Details:** Currently 350-400 words (thin). Add 2-3 narrative paragraphs explaining photography challenges in depth with specific examples.

### 12. Differentiate city FAQ answers
**File:** `site/src/app/food-photography/[city]/page.tsx`
**Details:** Write 2-3 city-specific FAQ answers per page. Example for NYC: reference Brooklyn food scene, mention specific photographer pricing in Manhattan vs. outer boroughs.

### 13. Standardize schema provider/publisher references
**Files:** Restaurant type pages, blog posts, guide pages, comparison pages
**Details:** Some use `{ "@id": "${siteUrl}/#organization" }` (correct), others use inline Organization. Standardize on `@id` reference to build a connected entity graph.

### 14. Reconcile social media URLs
**Files:** `site/src/app/layout.tsx` (Organization sameAs), `site/src/components/sections/footer.tsx`
**Details:** Schema says `@cravemodeai`, footer says `@cravemode`. Must match actual social profiles.

### 15. Resolve `/sign-up` robots.txt/sitemap conflict
**Files:** `site/src/app/robots.ts`, `site/src/app/sitemap.ts`
**Details:** `/sign-up` is disallowed in robots.txt but included in sitemap. Either remove from sitemap or remove the disallow.

### 16. Enrich ImageGallery schema on Showcase
**File:** `site/src/app/showcase/layout.tsx`
**Details:** Current ImageGallery has no `image` array. Add ImageObject entries for showcase items. Also add missing BreadcrumbList.

### 17. Add `image` to managed-vs-self-service Article schema
**File:** `site/src/app/compare/managed-vs-self-service/page.tsx`
**Details:** Missing `image` property blocks Article rich results for this page.

### 18. Expand guide pages to 1,500+ words OR redirect to blog posts
**Files:** Guide page.tsx files
**Details:** Guide pages (600-700 words) cannibalize more comprehensive blog posts on same topics. Either expand guides to be standalone or redirect shorter guides to detailed blog posts.

### 19. Vary CTA format across blog posts
**File:** `site/src/lib/blog/posts.ts`
**Details:** Every post ends with identical CraveMode sales pitch. Vary: some end with tool recommendation, some with related post, some with downloadable resource.

### 20. Add external links to blog posts
**File:** `site/src/lib/blog/posts.ts`
**Details:** Each post should include 3-5 external links to authoritative sources. Signals editorial rigor to Google and AI citation systems.

### 21. Use real dates for synthetic sitemap entries
**File:** `site/src/app/sitemap.ts`
**Details:** City and type page `lastModified` dates use index-based formulas. Use real dates from `page-dates.ts` instead.

---

## LOW PRIORITY — Polish (Fix within 3 months)

### 22. Standardize canonical URL format (all relative or all absolute)
### 23. Add `redirects()` stub to next.config.mjs for post-launch URL changes
### 24. Expand "food-photography-tips" post to 1,500+ words
### 25. Change manifest `start_url` from `/explore` to `/`
### 26. Verify `/blog?q=` search functionality or remove WebSite SearchAction
### 27. Fix `offerCount` type on photo-enhancement page (number → string)
### 28. Use `<JsonLd>` component consistently (photo-checker uses raw `<script>` tag)
### 29. Add blog cross-links to city pages and city cross-links to blog posts
### 30. Add blog category/tag pages as content scales

---

## Manual Tasks (Non-Code)

These require action outside the codebase:

1. **Register Google Search Console** — Submit sitemap, monitor indexing
2. **Register Bing Webmaster Tools** — Submit sitemap
3. **Set up GA4** — Track traffic, conversions, Core Web Vitals
4. **Add physical business address** — To footer and Organization schema
5. **Add contact email/phone** — For high-intent prospects and trust signals
6. **Register on Trustpilot/G2/Capterra** — Third-party review signals
7. **Pursue press mentions** — Restaurant industry publications (Eater, FSR Magazine, Nation's Restaurant News)
8. **Create real case studies** — Named restaurants with specific metrics and before/after photos
9. **Build verifiable author presence** — LinkedIn profiles, headshots, external publications
10. **Add Google Business Profile** — If serving specific locations
11. **Submit to directories** — Capterra, G2, GetApp, Product Hunt

---

## Score Projection

| Action Group | Est. Score Impact |
|-------------|-------------------|
| Remove FAQPage schemas (#1) | +1 |
| Hero image optimization (#2) | +3-4 |
| Author/Case study fixes (#3-4) | +6-8 |
| Orphaned pages + internal links (#5, #7) | +3-4 |
| Source citations (#6) | +2-3 |
| Schema fixes (#10, #13, #16, #17) | +2-3 |
| Content expansion (#11, #12, #18) | +2-3 |
| **Total potential improvement** | **+19-26** |
| **Projected score** | **87-94/100** |

---

## Priority Matrix

```
         HIGH IMPACT
              │
    ┌─────────┼─────────┐
    │  #2 #3  │  #4 #6  │
    │  #5 #7  │  #8     │
    │         │         │
LOW ──────────┼──────────── HIGH
EFFORT        │         EFFORT
    │  #1 #10 │  #11#12 │
    │  #14#15 │  #18#19 │
    │         │         │
    └─────────┼─────────┘
              │
         LOW IMPACT
```

**Start with:** Top-left quadrant (high impact, low effort) — items #1, #2, #5, #7, #10

---

*Generated by CraveMode AI SEO Audit — 2026-03-11*
