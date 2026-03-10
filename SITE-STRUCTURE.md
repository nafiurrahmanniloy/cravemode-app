# CraveMode AI — Site Structure & URL Architecture

> Information architecture, URL hierarchy, internal linking, and content organization

---

## URL Hierarchy

```
getcravemode.com/
│
├── /                                    ← Landing page (exists)
├── /pricing                             ← Standalone pricing page
├── /showcase                            ← Before/after gallery (exists)
│
├── /services/                           ← Service hub
│   ├── /services/photo-enhancement      ← Photo enhancement details
│   ├── /services/video-creation         ← Video/Reels/TikTok creation
│   └── /services/social-media-kit       ← Social media content packages
│
├── /for/                                ← Restaurant type verticals
│   ├── /for/fine-dining
│   ├── /for/fast-casual
│   ├── /for/cafes-coffee-shops
│   ├── /for/food-trucks
│   ├── /for/bakeries
│   ├── /for/bars-cocktails
│   ├── /for/dark-kitchens
│   ├── /for/pizzerias
│   ├── /for/sushi-restaurants
│   └── /for/catering
│
├── /food-photography/                   ← Programmatic city pages
│   ├── /food-photography/new-york
│   ├── /food-photography/los-angeles
│   ├── /food-photography/chicago
│   ├── /food-photography/houston
│   ├── /food-photography/miami
│   ├── /food-photography/san-francisco
│   ├── /food-photography/dallas
│   ├── /food-photography/atlanta
│   ├── /food-photography/seattle
│   ├── /food-photography/boston
│   ├── /food-photography/phoenix
│   ├── /food-photography/denver
│   ├── /food-photography/san-diego
│   ├── /food-photography/austin
│   ├── /food-photography/nashville
│   ├── /food-photography/portland
│   ├── /food-photography/philadelphia
│   ├── /food-photography/las-vegas
│   ├── /food-photography/charlotte
│   ├── /food-photography/minneapolis
│   └── ... (50+ cities total)
│
├── /guides/                             ← Platform & how-to guides
│   ├── /guides/uber-eats-photos
│   ├── /guides/doordash-menu-photos
│   ├── /guides/grubhub-photo-requirements
│   ├── /guides/google-business-photos
│   └── /guides/instagram-restaurant-photos
│
├── /compare/                            ← Comparison pages
│   ├── /compare/ai-vs-photographer
│   ├── /compare/cravemode-vs-foodshot
│   ├── /compare/cravemode-vs-snappr
│   ├── /compare/cravemode-vs-diy
│   └── /compare/managed-vs-self-service
│
├── /case-studies/                       ← Client success stories
│   ├── /case-studies                    ← Index page
│   └── /case-studies/[slug]             ← Individual case study
│
├── /blog/                               ← Content hub
│   ├── /blog                            ← Blog index
│   ├── /blog/food-photography-cost      ← PILLAR: Cost guide 2026
│   ├── /blog/food-photography-tips
│   ├── /blog/food-photography-lighting
│   ├── /blog/restaurant-instagram-guide
│   ├── /blog/restaurant-video-content-guide
│   ├── /blog/food-photography-roi
│   ├── /blog/food-photography-equipment
│   ├── /blog/restaurant-social-media-strategy
│   ├── /blog/food-styling-tips
│   └── /blog/[slug]                     ← Individual posts
│
├── /alternatives/                       ← Alternative-to pages
│   └── /alternatives/food-photographer
│
├── /sign-in                             ← Auth (exists)
├── /sign-up                             ← Auth (exists)
├── /explore                             ← Dashboard (exists, auth-protected)
├── /image                               ← Photo tool (exists, auth-protected)
├── /video                               ← Video tool (exists, auth-protected)
├── /gallery                             ← Gallery (exists, auth-protected)
├── /queue                               ← Queue (exists, auth-protected)
├── /settings                            ← Settings (exists, auth-protected)
│
├── /privacy                             ← Privacy policy (exists)
├── /terms                               ← Terms of service (exists)
├── /refund                              ← Refund policy (exists)
│
├── /sitemap.xml                         ← Dynamic XML sitemap
├── /robots.txt                          ← Crawler directives
└── /llms.txt                            ← AI search optimization
```

---

## Internal Linking Strategy

### Hub & Spoke Model

Each content pillar has a hub page that links to spoke pages, and spokes link back to the hub.

```
                    ┌─────────────────┐
                    │    HOME (/)      │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────┴────┐        ┌────┴────┐        ┌────┴────┐
    │Services │        │  Blog   │        │Showcase │
    │  Hub    │        │  Hub    │        │  Hub    │
    └────┬────┘        └────┬────┘        └────┬────┘
         │                   │                   │
    ┌────┼────┐        ┌────┼────┐        ┌────┼────┐
    │    │    │        │    │    │        │    │    │
   Photo Video Kit   Cost Tips Light   Case1 Case2 Case3
```

### Cross-Linking Rules

| From | Links To |
|------|----------|
| Landing page | Services hub, Pricing, Showcase, Blog (top posts) |
| Service pages | Pricing, relevant case studies, relevant blog posts, showcase |
| City pages | Services hub, Pricing, nearby city pages, relevant guides |
| Blog posts | Services (contextual CTA), related blog posts, showcase |
| Case studies | Services used, pricing, related case studies |
| Comparison pages | Services, pricing, case studies as proof |
| Platform guides | Services, pricing, relevant city pages |
| Restaurant type pages | Services, pricing, relevant case studies, city pages |

### Breadcrumb Structure

Every page gets breadcrumbs for navigation + SEO:

```
Home > Services > Photo Enhancement
Home > Blog > Food Photography Cost in 2026
Home > Food Photography > New York
Home > For > Fine Dining Restaurants
Home > Compare > CraveMode AI vs FoodShot AI
Home > Case Studies > [Client Name]
```

---

## Page Templates

### City Page Template (`/food-photography/[city]`)

```
H1: Food Photography in [City] — Professional Results, AI Prices
├── Hero: City-specific stats (# restaurants, avg photo cost)
├── Section: What Local Restaurants Pay for Photography
│   ├── Traditional photographer rates in [City]
│   ├── Agency rates in [City]
│   └── CraveMode AI as alternative (CTA)
├── Section: Before/After Examples
│   └── 3-4 real before/after images
├── Section: How CraveMode AI Works
│   └── 3-step process
├── Section: Pricing Comparison Table
│   └── Local photographer vs CraveMode AI
├── Section: FAQ (city-specific)
│   └── 4-5 questions about food photography in [City]
├── Section: CTA
│   └── "Get Your First Batch Free — Money-Back Guarantee"
└── Schema: Service + areaServed: [City]
```

### Restaurant Type Template (`/for/[type]`)

```
H1: AI Food Photography for [Restaurant Type]
├── Hero: Type-specific pain points and imagery
├── Section: Why [Type] Restaurants Need Better Photos
├── Section: Before/After Examples (type-specific)
├── Section: What's Included
│   └── Photos, videos, formats specific to this type
├── Section: Pricing
├── Section: FAQ (type-specific)
├── Section: CTA
└── Schema: Service + serviceType specific
```

### Comparison Page Template (`/compare/[slug]`)

```
H1: CraveMode AI vs [Competitor] — Which Is Right for You?
├── Quick comparison table (features, pricing, delivery)
├── Section: Overview of each service
├── Section: Feature-by-feature breakdown
├── Section: Pricing comparison
├── Section: Who should choose which
├── Section: Verdict
├── Section: CTA
└── Schema: Article
```

### Blog Post Template (`/blog/[slug]`)

```
H1: [Title — Keyword-Optimized]
├── Meta: Author, date, reading time, category
├── Table of contents (for long posts)
├── Content with H2/H3 hierarchy
├── Internal links to related content
├── CTA banner (mid-article and end)
├── Related posts section
└── Schema: Article + Person (author)
```

---

## Sitemap Organization

### sitemap.xml structure

```xml
<!-- Main sitemap index -->
<sitemapindex>
  <sitemap><loc>/sitemap-core.xml</loc></sitemap>
  <sitemap><loc>/sitemap-services.xml</loc></sitemap>
  <sitemap><loc>/sitemap-cities.xml</loc></sitemap>
  <sitemap><loc>/sitemap-blog.xml</loc></sitemap>
  <sitemap><loc>/sitemap-guides.xml</loc></sitemap>
</sitemapindex>
```

| Sitemap | Pages | Priority | Change Freq |
|---------|-------|----------|-------------|
| Core | /, /pricing, /showcase, /sign-up | 1.0 | weekly |
| Services | /services/*, /for/*, /compare/*, /alternatives/* | 0.8 | monthly |
| Cities | /food-photography/* (50+ pages) | 0.7 | monthly |
| Blog | /blog/* | 0.6 | weekly |
| Guides | /guides/* | 0.7 | monthly |

### Pages Excluded from Sitemap
- `/explore`, `/image`, `/video`, `/gallery`, `/queue`, `/settings` (auth-protected)
- `/sign-in` (utility page)
- `/auth/callback` (API route)
- All `/api/*` routes

---

## robots.txt

```
User-agent: *
Allow: /
Disallow: /api/
Disallow: /auth/
Disallow: /explore
Disallow: /image
Disallow: /video
Disallow: /gallery
Disallow: /queue
Disallow: /settings
Disallow: /sign-in

# AI Crawlers — Allow for GEO
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: https://getcravemode.com/sitemap.xml
```

---

## Content Priority Matrix

| Page Group | Count | SEO Impact | Effort | Build Order |
|-----------|:-----:|:----------:|:------:|:-----------:|
| Technical SEO (robots, sitemap, schema) | — | High | Low | Phase 1, Week 1 |
| Page metadata (all existing pages) | 15 | Medium | Low | Phase 1, Week 1 |
| Services hub + 3 service pages | 4 | High | Medium | Phase 1, Weeks 2-3 |
| Pricing page (standalone) | 1 | High | Low | Phase 1, Week 2 |
| Blog pillar: Food Photography Cost | 1 | Very High | High | Phase 1, Week 3-4 |
| City pages (first 15) | 15 | High | Medium | Phase 2, Weeks 5-8 |
| Platform guides (5) | 5 | High | Medium | Phase 2, Weeks 6-8 |
| Comparison pages (5) | 5 | Medium | Medium | Phase 2, Weeks 8-10 |
| Restaurant type pages (10) | 10 | Medium | Medium | Phase 2, Weeks 9-12 |
| Blog posts (ongoing) | 2/month | Medium | Medium | Phase 2+, ongoing |
| City pages (remaining 35) | 35 | Medium | Low (template) | Phase 3, Weeks 13-20 |
| Case studies | 3-5 | High | High (needs clients) | Phase 3, as clients come |
| Alternatives page | 1 | Medium | Low | Phase 2, Week 10 |
