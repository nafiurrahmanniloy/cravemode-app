# CraveMode AI — SEO Strategy

> **Business**: CraveMode AI — Done-for-you restaurant photo & video enhancement service
> **Domain**: getcravemode.com
> **Market**: US nationwide (restaurant owners, managers, marketers)
> **Starting Point**: Zero organic traffic, new domain
> **Date**: March 2026

---

## Executive Summary

CraveMode AI has **two massive competitive advantages** that no competitor currently claims in SEO:

1. **Photo + Video** — Every competitor is photo-only. CraveMode is the only service offering AI-generated Reels/TikToks alongside enhanced photos.
2. **Done-For-You managed service** — Competitors sell self-service SaaS tools ($9-$99/mo). CraveMode is a premium managed service ($297-$997/mo) where restaurant owners just upload and receive finished content.

The SEO strategy exploits these gaps while building a scalable content engine targeting the 1M+ restaurants in the US.

---

## 1. Target Audience Segments

| Segment | Search Behavior | Intent Level |
|---------|----------------|-------------|
| **Restaurant owners** actively looking for photo/video help | "restaurant food photography service", "food photo editing for restaurants" | High (ready to buy) |
| **Restaurant owners** researching costs | "food photography cost 2026", "how much does food photography cost" | Medium-high (comparing options) |
| **Restaurant owners** needing delivery platform photos | "Uber Eats photo requirements", "DoorDash menu photos" | High (specific need) |
| **Restaurant marketers** planning content | "restaurant Instagram content strategy", "food video for social media" | Medium (building awareness) |
| **Restaurant owners** frustrated with DIY | "how to take better food photos", "food photography tips for restaurants" | Low-medium (top of funnel) |

---

## 2. Keyword Strategy

### Tier 1 — Money Keywords (Bottom of Funnel)

These drive direct conversions. Build dedicated landing pages.

| Keyword Cluster | Est. Monthly Volume | Competition | Priority |
|----------------|--------------------|-----------:|---------|
| "restaurant food photography service" | 1,200 | Medium | P0 |
| "food photography for restaurants" | 2,400 | High | P0 |
| "AI food photo editing" / "AI food photography" | 1,800 | Medium | P0 |
| "restaurant content creation service" | 800 | Low | P0 |
| "food video for restaurants" | 600 | Very Low | P0 |
| "restaurant social media content service" | 900 | Low | P0 |
| "done for you restaurant content" | 300 | Very Low | P0 |
| "restaurant photo and video package" | 200 | Very Low | P0 |

### Tier 2 — Commercial Investigation Keywords

These capture prospects comparing options. Build comparison and guide pages.

| Keyword Cluster | Est. Monthly Volume | Competition | Priority |
|----------------|--------------------|-----------:|---------|
| "food photography cost [2026]" | 6,600 | High | P1 |
| "food photography pricing" | 3,200 | High | P1 |
| "AI vs traditional food photography" | 500 | Low | P1 |
| "best food photography service for restaurants" | 400 | Medium | P1 |
| "food photographer alternative" | 300 | Low | P1 |
| "restaurant Reels creation service" | 200 | Very Low | P1 |
| "food photography before and after" | 400 | Very Low | P1 |

### Tier 3 — Programmatic / Location Keywords

Scalable city-specific pages. Build templates, generate at scale.

| Keyword Pattern | Cities to Target | Est. Combined Volume |
|----------------|-----------------|---------------------|
| "food photography [city]" | 50 US metros | 15,000+ |
| "food photography cost [city]" | 50 US metros | 8,000+ |
| "restaurant photographer [city]" | 50 US metros | 12,000+ |
| "restaurant content creation [city]" | 25 US metros | 3,000+ |

### Tier 4 — Platform-Specific Keywords

Capture restaurant owners needing specific delivery platform photos.

| Keyword | Est. Monthly Volume | Competition |
|---------|--------------------|-----------:|
| "Uber Eats photo requirements" / "Uber Eats menu photos" | 2,400 | Low |
| "DoorDash menu photo guide" / "DoorDash food photos" | 1,600 | Low |
| "GrubHub photo requirements" | 600 | Very Low |
| "Google Business restaurant photos" | 1,200 | Low |
| "Instagram food photography for restaurants" | 1,800 | Medium |

### Tier 5 — Educational / Top of Funnel

Blog content to build domain authority and capture early-stage prospects.

| Keyword Cluster | Est. Monthly Volume | Competition |
|----------------|--------------------|-----------:|
| "food photography tips" | 8,100 | High |
| "food photography lighting" | 4,400 | High |
| "food styling tips" | 3,600 | High |
| "restaurant Instagram tips" | 2,900 | Medium |
| "restaurant social media strategy" | 2,400 | Medium |
| "how to photograph food with iPhone" | 5,400 | Medium |
| "food photography equipment" | 1,900 | Medium |

---

## 3. Content Pillars

### Pillar 1: "Restaurant Visual Content" (Primary)
Core service pages explaining CraveMode AI's photo + video enhancement.
- Home page, service pages, pricing, how it works
- **Goal**: Convert high-intent visitors

### Pillar 2: "Food Photography Cost & Comparison" (Commercial)
Cost guides, competitor comparisons, AI vs traditional content.
- Pillar page: "Food Photography Cost Guide 2026"
- Supporting: city-specific pages, platform guides, comparison pages
- **Goal**: Capture commercial investigation traffic

### Pillar 3: "Restaurant Marketing Content" (Educational)
Blog content on restaurant social media, food photography tips, content strategy.
- Blog posts, tutorials, case studies
- **Goal**: Build authority, capture top-of-funnel traffic

### Pillar 4: "Results & Proof" (Trust)
Before/after showcases, case studies, ROI data.
- Showcase gallery, case study pages, data-driven content
- **Goal**: Build E-E-A-T signals, convert skeptics

---

## 4. Technical SEO Foundation

### Immediate (Week 1)

| Task | Status | Details |
|------|--------|---------|
| Add `robots.txt` | Missing | Allow all crawlers, block `/api/`, `/auth/`, authenticated pages |
| Add `sitemap.xml` | Missing | Dynamic sitemap via Next.js `sitemap.ts` |
| Add Schema.org (Organization) | Missing | JSON-LD on all pages |
| Add Schema.org (FAQPage) | Missing | FAQ section on landing page |
| Add Schema.org (Service) | Missing | Service description markup |
| Add Schema.org (Product) | Missing | Pricing/package markup |
| Add page-level metadata | Missing | Unique title/description for every public page |
| Add canonical URLs | Partial | Verify metadataBase works correctly |

### Week 2-4

| Task | Details |
|------|---------|
| Core Web Vitals audit | Target LCP < 2.5s, CLS < 0.1, INP < 200ms |
| Image optimization | WebP/AVIF, proper `sizes` attributes, lazy loading |
| Internal linking | Cross-link between service pages, blog, showcase |
| Analytics setup | Google Search Console + GA4 + conversion tracking |
| `llms.txt` | AI search optimization (GEO) |

---

## 5. Page Architecture

### Service Pages (New)
```
/                           → Landing page (exists)
/services                   → Overview of all services
/services/photo-enhancement → Photo enhancement details
/services/video-creation    → Video/Reels creation details
/services/social-media-kit  → Social media content packages
/pricing                    → Dedicated pricing page (extract from landing)
/showcase                   → Before/after gallery (exists)
/case-studies               → Client success stories
/case-studies/[slug]        → Individual case study
```

### Comparison Pages (New)
```
/compare/ai-vs-photographer         → AI vs hiring a photographer
/compare/cravemode-vs-foodshot       → vs FoodShot AI
/compare/cravemode-vs-snappr         → vs Snappr
/compare/cravemode-vs-diy            → vs doing it yourself
/alternatives/food-photographer      → Alternative to hiring photographers
```

### Location Pages (Programmatic — New)
```
/food-photography/[city]             → City-specific landing pages
  e.g., /food-photography/new-york
        /food-photography/los-angeles
        /food-photography/miami
        ... (50+ cities)
```

### Platform Guide Pages (New)
```
/guides/uber-eats-photos             → Uber Eats photo requirements
/guides/doordash-menu-photos         → DoorDash photo guide
/guides/grubhub-photo-requirements   → GrubHub guide
/guides/google-business-photos       → Google Business Profile photos
/guides/instagram-restaurant-photos  → Instagram content guide
```

### Restaurant Type Pages (New)
```
/for/fine-dining                     → Fine dining restaurants
/for/fast-casual                     → Fast casual
/for/cafes-coffee-shops              → Cafes & coffee shops
/for/food-trucks                     → Food trucks
/for/bakeries                        → Bakeries
/for/bars-cocktails                  → Bars & cocktail lounges
/for/dark-kitchens                   → Dark/ghost kitchens
```

### Blog (New)
```
/blog                               → Blog index
/blog/food-photography-cost          → Pillar: Cost guide 2026
/blog/food-photography-tips          → Tips listicle
/blog/food-photography-lighting      → Lighting guide
/blog/restaurant-instagram-guide     → Instagram strategy
/blog/restaurant-video-content       → Video content guide
/blog/food-photography-roi           → ROI data
/blog/[slug]                         → Individual posts
```

### Legal / Utility (Exists)
```
/privacy                            → Privacy policy (exists)
/terms                              → Terms of service (exists)
/refund                             → Refund policy (exists)
```

---

## 6. Schema Markup Plan

| Page Type | Schema Types |
|-----------|-------------|
| All pages | `Organization`, `WebSite`, `BreadcrumbList` |
| Landing page | `Service`, `FAQPage`, `Review` (testimonials) |
| Pricing page | `Product` (one per plan), `Offer` |
| Service pages | `Service`, `HowTo` |
| Blog posts | `Article`, `Person` (author) |
| Case studies | `Article`, `Review` |
| Showcase | `ImageGallery`, `ImageObject` |
| Location pages | `Service` + `areaServed` |
| Comparison pages | `Article` |

---

## 7. E-E-A-T Strategy

### Experience
- Before/after showcase with real client photos
- Case studies with specific metrics (% increase in orders, engagement)
- Video testimonials from restaurant owners

### Expertise
- Blog content demonstrating deep knowledge of food photography
- Platform-specific guides showing insider knowledge
- Industry data and original research

### Authoritativeness
- Press mentions and media coverage
- Listings on review sites (Capterra, G2, GetApp)
- Social proof (client count, photos enhanced count)

### Trustworthiness
- Clear pricing (no hidden fees)
- Money-back guarantee prominent in schema + content
- Transparent process documentation
- SSL, privacy policy, terms of service (already exist)

---

## 8. GEO (Generative Engine Optimization)

To appear in AI Overviews, ChatGPT search, and Perplexity:

| Action | Purpose |
|--------|---------|
| Add `llms.txt` to root | Describe site purpose, key pages, services for AI crawlers |
| Passage-level citability | Write clear, quotable paragraphs with data points |
| Structured FAQ content | AI models love pulling from well-structured Q&A |
| Claim brand mentions | Ensure "CraveMode AI" appears in list posts, comparisons |
| Data-driven content | Original statistics AI models can cite |
| Allow AI crawlers | GPTBot, ClaudeBot, PerplexityBot in robots.txt |

---

## 9. KPI Targets

| Metric | Baseline (Now) | 3 Months | 6 Months | 12 Months |
|--------|:-----------:|:--------:|:--------:|:---------:|
| Organic Sessions/mo | 0 | 500-1,000 | 3,000-5,000 | 10,000-20,000 |
| Indexed Pages | 0 | 30-40 | 80-100 | 150-200 |
| Keywords Ranking (Top 100) | 0 | 50-100 | 200-400 | 500-1,000 |
| Keywords Ranking (Top 10) | 0 | 5-10 | 20-40 | 80-150 |
| Domain Rating (Ahrefs) | 0 | 10-15 | 20-30 | 35-50 |
| Organic Leads/mo | 0 | 5-10 | 20-40 | 80-150 |
| Core Web Vitals | Unknown | All Green | All Green | All Green |

---

## 10. Competitive Positioning Matrix

| Competitor | Photos | Videos | Managed | Pricing | SEO Maturity |
|-----------|:------:|:------:|:-------:|:-------:|:------------:|
| **CraveMode AI** | Yes | **Yes** | **Yes** | $297-$997/mo | Starting |
| FoodShot AI | Yes | No | No | $9-$99/mo | Strong |
| MenuPhotoAI | Yes | No | No | $39+/mo | Growing |
| PlatePhoto | Yes | No | No | $10-$99/mo | Weak |
| Snappr | Yes | No | Partial | $100+/session | Strong |
| MenuCapture | Yes | No | No | $0.24/photo | Weak |

**Key Takeaway**: CraveMode AI's "Photo + Video + Done-For-You" positioning is completely uncontested in SEO. No competitor targets restaurant video content or managed service keywords.

---

## Next Steps

See companion documents:
- **[COMPETITOR-ANALYSIS.md](COMPETITOR-ANALYSIS.md)** — Deep competitor breakdown
- **[SITE-STRUCTURE.md](SITE-STRUCTURE.md)** — Full URL hierarchy and internal linking plan
- **[CONTENT-CALENDAR.md](CONTENT-CALENDAR.md)** — 12-month content roadmap with priorities
- **[IMPLEMENTATION-ROADMAP.md](IMPLEMENTATION-ROADMAP.md)** — Phased execution plan (weeks 1-52)
