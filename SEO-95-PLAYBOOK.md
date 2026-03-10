# CraveMode AI — SEO 95+ Playbook

> Comprehensive action plan to raise every SEO category from current scores to 95+.
> Based on RECON YouTube research (18 queries) + 4 deep web research agents (150+ sources).

**Current Score: 70/100 | Target: 95+/100**

| Category | Current | Target | Gap |
|----------|---------|--------|-----|
| Technical SEO | 72 | 95+ | Security headers, canonical tags, sitemap |
| Content Quality (E-E-A-T) | 52 | 95+ | Fabricated stats, no author pages, thin city pages |
| On-Page SEO | 82 | 95+ | Missing canonicals, internal linking gaps |
| Schema / Structured Data | 82 | 95+ | Organization gaps, missing VideoObject duration |
| Performance (CWV) | 70 | 95+ | Image formats, bundle size, LCP/INP |
| Images | 62 | 95+ | No AVIF, uncompressed heroes, missing alt/sizes |
| AI Search / GEO | 78 | 95+ | Sparse llms.txt, no AI bot differentiation |

---

## 1. Technical SEO (72 → 95+)

### 1.1 Security Headers — ADD TO `next.config.mjs`

**Impact: HIGH | Effort: LOW (1 file change)**

Zero security headers exist today. Add all 7 to `site/next.config.mjs`:

```javascript
const ContentSecurityPolicy = `
  default-src 'self';
  script-src 'self' 'unsafe-inline' 'unsafe-eval' https://www.googletagmanager.com https://*.google-analytics.com https://js.stripe.com https://va.vercel-scripts.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: blob: https://*.supabase.co https://*.google-analytics.com https://www.googletagmanager.com https://*.stripe.com;
  font-src 'self' data:;
  connect-src 'self' https://*.supabase.co wss://*.supabase.co https://*.google-analytics.com https://www.google-analytics.com https://region1.google-analytics.com https://analytics.google.com https://api.stripe.com https://errors.stripe.com;
  frame-src 'self' https://js.stripe.com https://hooks.stripe.com;
  frame-ancestors 'none';
  worker-src 'self' blob:;
  object-src 'none';
  base-uri 'self';
  form-action 'self';
  upgrade-insecure-requests;
`.replace(/\s{2,}/g, ' ').trim();

const securityHeaders = [
  { key: 'Content-Security-Policy', value: ContentSecurityPolicy },
  { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()' },
  { key: 'X-DNS-Prefetch-Control', value: 'on' },
];

// Add to nextConfig:
async headers() {
  return [{ source: '/(.*)', headers: securityHeaders }];
},
```

**Why `next.config.mjs` not middleware:** Static headers preserve CDN caching. Nonce-based CSP in middleware forces dynamic rendering on every page — kills static optimization.

**Why `'unsafe-inline'` is required:** Framer Motion injects inline `style` attributes for all animations. No workaround without nonces.

**Critical:** Verify Next.js version is 15.2.3+ to patch CVE-2025-29927 (middleware authorization bypass via `x-middleware-subrequest` header injection).

### 1.2 Canonical Tags — ADD TO 13+ MISSING PAGES

**Impact: HIGH | Effort: LOW (13 small edits)**

Pages WITH canonical tags (13): `/food-photography/[city]`, `/blog/[slug]`, `/tools/photo-checker`, `/compare/*`, `/guides/*`, `/for/[type]`

Pages MISSING canonical tags (~13-20):

| Page | Add to metadata |
|------|----------------|
| `/` (homepage) | `alternates: { canonical: '/' }` |
| `/pricing` | `alternates: { canonical: '/pricing' }` |
| `/showcase` | `alternates: { canonical: '/showcase' }` |
| `/services` | `alternates: { canonical: '/services' }` |
| `/services/photo-enhancement` | `alternates: { canonical: '/services/photo-enhancement' }` |
| `/services/video-creation` | `alternates: { canonical: '/services/video-creation' }` |
| `/blog` (index) | `alternates: { canonical: '/blog' }` |
| `/food-photography` (hub) | `alternates: { canonical: '/food-photography' }` |
| `/sign-in` | `alternates: { canonical: '/sign-in' }` |
| `/sign-up` | `alternates: { canonical: '/sign-up' }` |
| `/privacy` | `alternates: { canonical: '/privacy' }` |
| `/terms` | `alternates: { canonical: '/terms' }` |
| `/refund` | `alternates: { canonical: '/refund' }` |

Relative paths work because `metadataBase` is already set to `https://getcravemode.com` in root layout.

### 1.3 Sitemap Cleanup

**Impact: MEDIUM | Effort: MEDIUM**

Three problems with current `site/src/app/sitemap.ts`:

1. **`lastModified: new Date()`** on every page — Google sees "everything just changed" and ignores lastmod entirely
2. **`changeFrequency`** — Google ignores this completely
3. **`priority`** — Google ignores this completely

**Fix:** Create `src/lib/data/page-dates.ts` with real dates:

```typescript
export const PAGE_DATES: Record<string, string> = {
  '/': '2026-03-01',
  '/pricing': '2026-03-05',
  '/showcase': '2026-02-15',
  '/services': '2026-02-01',
  // ... etc — update when content actually changes
};
```

Remove all `changeFrequency` and `priority` fields. Use city data file's last-modified date for all 50 city pages.

**Automation option:** Add a `prebuild` script that extracts git commit dates per file:
```bash
git log -1 --format=%cI -- "src/app/pricing/page.tsx"
```

---

## 2. Content Quality / E-E-A-T (52 → 95+)

**This is the biggest gap.** Google's December 2025 core update expanded E-E-A-T evaluation to ALL competitive searches, not just YMYL.

### 2.1 REMOVE ALL FABRICATED STATISTICS — IMMEDIATE

**Impact: CRITICAL | Effort: LOW**

These claims have zero backing and actively damage trust:

| File | Claim | Action |
|------|-------|--------|
| `trusted-by.tsx:48` | "2,800+ Restaurants" | Replace: "Built for restaurants of every size" |
| `trusted-by.tsx:80` | "98.4% Satisfaction Rate" | Remove entirely |
| `trusted-by.tsx:69` | "3.2M+ Photos Enhanced" | Replace: "Upload any photo, get 6 formats back" |
| `trusted-by.tsx:58` | "47 Countries" | Remove — focus on US launch market |
| `numbers-speak.tsx:30-41` | "+340% Google Clicks" | Replace with cited stat: "Restaurants with photos get 35% more clicks — Google" |
| `numbers-speak.tsx` | "$4.2M Revenue Generated" | Remove entirely |
| `numbers-speak.tsx` | "+127% More Orders" | Replace: "Menu photos increase orders 30-70% — Grubhub data" |
| `numbers-speak.tsx` | "2,800+ Restaurants" | Remove (duplicate) |
| `numbers-speak.tsx` | "3.2M Photos Enhanced" | Remove (duplicate) |
| `numbers-speak.tsx` | "98.4% Satisfaction Rate" | Remove (duplicate) |

**Golden rule:** Every number on the site must either (a) come from verifiable data, or (b) be attributed to a specific third-party source with a link.

**Citable replacement statistics:**
- "Restaurants with menu photos receive up to 70% more orders" — Grubhub
- "82% of people order based purely on how food looks in photos" — IJIRT research
- "Menu photos increase sales 20-45%" — Multiple studies
- "Restaurants with photos get 35% more clicks on Google" — Google data

### 2.2 Create `/about` Page

**Impact: HIGH | Effort: MEDIUM**

Google's Experience signal requires proof that real humans built and run the service. Create `/about` with:

- Founder name, photo, background story (why food photography?)
- Team bios with relevant experience
- Company mission and origin story
- Contact details (physical address or at minimum city + state)
- LinkedIn links for team members

### 2.3 Add Author Bylines to All Blog Posts

**Impact: MEDIUM | Effort: LOW**

Each of the 9 blog posts needs:
- Author name + headshot
- One-line bio with credentials
- Link to `/about/[author]` page
- LinkedIn profile link

### 2.4 Add Inline Source Citations to Blog Posts

**Impact: HIGH | Effort: MEDIUM**

AI Overviews cite articles that cover 62% more facts than non-cited ones. Go through each blog post and add 2-3 inline citations:

| Blog Post | Statistics to Cite | Source |
|-----------|-------------------|--------|
| Food Photography Cost 2026 | Avg photographer rates | BLS.gov, Thumbtack |
| Food Photography ROI | "70% more orders with photos" | Grubhub data |
| Restaurant Video Content Guide | Video marketing stats | HubSpot, Wyzowl survey |
| Restaurant Social Media Strategy | Platform engagement rates | Sprout Social |
| Food Delivery Photo Optimization | Platform-specific requirements | Official platform help centers |
| Google Business Profile Photos | Google-specific statistics | Google Business help docs |

**Format:** Use inline links, NOT footnotes. Footnotes lose anchor text value and create mobile usability issues.

### 2.5 City Page Content Differentiation — CRITICAL

**Impact: CRITICAL | Effort: HIGH**

Current state: 50 city pages share identical FAQs, identical images, identical "How It Works" section. Only city name, restaurant count, and photographer rate change. This is the exact pattern Google penalized in December 2025.

**Minimum requirements per city page:**
- **500+ unique words** with **30-40% content differentiation**
- Under 300 unique words risks penalties

**What to add per city page:**

1. **One unique introductory paragraph (100-150 words)** about that city's food scene — cuisine types, notable food districts, seasonal trends
2. **City-specific cuisine breakdown** (what % of restaurants are each type)
3. **2-3 city-specific FAQ questions** replacing/supplementing the generic ones
4. **Local platform landscape** (which delivery apps dominate)
5. **One local insight/statistic** with proper citation (e.g., "[City] added 340 new restaurants in 2025")

**Data sources:** Google Maps API, census.gov (population, food service employment), BLS.gov (County Business Patterns), Yelp/TripAdvisor data.

### 2.6 Beta Testing Program

**Impact: HIGH (long-term) | Effort: MEDIUM**

Use BetaTesting.com (free for up to 50 testers) or recruit 5-10 restaurants manually. This generates:
- Real case studies with named restaurants, before/after photos, specific metrics
- Video testimonials (even 30-second iPhone videos)
- Attributed quotes: "CraveMode turned 8 phone photos into 48 ready-to-post images in 2 hours" — Maria Chen, Owner, Sakura Kitchen, Austin TX

---

## 3. On-Page SEO (82 → 95+)

### 3.1 Internal Linking Rules

1. Every spoke page links back to its hub page with keyword-rich anchor text
2. Hub pages link to all their spokes
3. Spokes cross-link to sibling spokes when contextually relevant
4. No page more than 3 clicks from homepage
5. City pages link to relevant restaurant type pages
6. Blog posts link to service pages and city pages

### 3.2 Content Cluster Architecture

**Hub 1:** `/food-photography` (exists) — 50 city spokes + 5 restaurant type spokes + blog posts
**Hub 2:** `/restaurant-marketing` (NEW) — social media, Google Business, Instagram, delivery, branding guides
**Hub 3:** `/food-delivery` (NEW) — Uber Eats, DoorDash, Grubhub, multi-platform optimization
**Hub 4:** `/restaurant-video` (NEW) — video service page + video guide + TikTok/Reels/Shorts guides

### 3.3 Answer-First Content Formatting

Start every section with a definition: "X is Y that does Z." Then expand with specifics. This format is 20-30% more likely to be cited by AI systems.

---

## 4. Schema / Structured Data (82 → 95+)

### 4.1 Organization Schema — ENHANCE in `layout.tsx`

**Current:** Basic Organization with name, url, logo
**Missing:** @id, sameAs, foundingDate, founder, knowsAbout, areaServed, numberOfEmployees

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://getcravemode.com/#organization",
  "name": "CraveMode AI",
  "url": "https://getcravemode.com",
  "logo": "https://getcravemode.com/logo.png",
  "foundingDate": "2026",
  "founder": {
    "@type": "Person",
    "name": "[Founder Name]"
  },
  "areaServed": {
    "@type": "Country",
    "name": "United States"
  },
  "knowsAbout": [
    "food photography",
    "restaurant marketing",
    "AI image enhancement",
    "food video production"
  ],
  "sameAs": [
    "https://www.linkedin.com/company/cravemode-ai",
    "https://www.instagram.com/cravemodeai",
    "https://twitter.com/cravemodeai",
    "https://www.youtube.com/@cravemodeai",
    "https://www.crunchbase.com/organization/cravemode-ai"
  ]
}
```

**Why sameAs matters:** Appears on 25-34% of AI-cited pages. Cross-validates entity identity.

### 4.2 VideoObject — ADD `duration`

In `/services/video-creation/page.tsx`, add `duration` property:

```json
{
  "@type": "VideoObject",
  "duration": "PT15S",
  "embedUrl": "https://getcravemode.com/services/video-creation"
}
```

### 4.3 Pricing Page — ADD `WebApplication` + `AggregateOffer`

Replace basic WebPage schema with:

```json
{
  "@type": "WebApplication",
  "name": "CraveMode AI",
  "applicationCategory": "BusinessApplication",
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": "297",
    "highPrice": "1497",
    "priceCurrency": "USD",
    "offerCount": 6
  }
}
```

### 4.4 Keep ALL FAQ Schema

FAQ schema no longer triggers rich result dropdowns for non-health/government sites. BUT: pages with FAQPage markup are **3.2x more likely to appear in AI Overviews**. Keep every FAQ schema intact.

### 4.5 Add ImageGallery Schema to `/showcase`

Currently has zero structured data. Add via layout.tsx:

```json
{
  "@type": "ImageGallery",
  "name": "CraveMode AI — Before & After Showcase",
  "description": "Real food photo transformations by CraveMode AI"
}
```

### 4.6 Use `@id` for Cross-Referencing

Every schema on the site should reference the Organization via `@id`:

```json
{
  "provider": { "@id": "https://getcravemode.com/#organization" }
}
```

---

## 5. Performance / CWV (70 → 95+)

### 5.1 Image Format Configuration — `next.config.mjs`

**Impact: +10-15 points | Effort: 5 minutes**

```javascript
images: {
  formats: ['image/avif', 'image/webp'],  // AVIF = 20-30% smaller than WebP
  deviceSizes: [640, 750, 828, 1080, 1200, 1920],
  imageSizes: [32, 48, 64, 96, 128, 256],
  minimumCacheTTL: 2678400,  // 31 days — food photos don't change
},
```

### 5.2 Remove Duplicate Animation Package

**Impact: -34KB bundle | Effort: 30 min**

`package.json` includes BOTH `framer-motion` (v11) and `motion` (v12). They do the same thing. Remove `framer-motion`, keep `motion`:

```bash
npm uninstall framer-motion
# Update imports: "framer-motion" → "motion/react"
```

### 5.3 Pre-Compress Hero Images to WebP

**Impact: -70% hero image weight | Effort: 1 hour**

Create `scripts/compress-images.mjs` using Sharp:

```javascript
import sharp from 'sharp';

// Hero images: render at 80-280px, serve at 400px (2x retina)
await sharp(inputPath)
  .resize({ width: 400, withoutEnlargement: true })
  .webp({ quality: 75, effort: 6 })
  .toFile(outputPath);

// Before/after images: serve at 1200px max
await sharp(inputPath)
  .resize({ width: 1200, withoutEnlargement: true })
  .webp({ quality: 80, effort: 6 })
  .toFile(outputPath);
```

Expected: Hero images 1.8MB → ~500KB. Before/after 2.5MB → ~700KB.

### 5.4 Dynamic Import Below-Fold Sections

**Impact: Major INP improvement | Effort: 1 hour**

Extend existing `dynamic()` pattern (FAQ + Contact) to all below-fold sections:

```typescript
const Problem = dynamic(
  () => import("@/components/sections/problem").then(mod => ({ default: mod.Problem })),
  { loading: () => <div className="min-h-screen bg-background" /> }
);
// Same for: HowItWorks, Formats, VideoSpotlight, NumbersSpeak, GlobalNetwork, TrustedBy, Pricing
```

### 5.5 LCP Optimization

1. Add `fetchpriority="high"` + `loading="eager"` to top 4 hero images in CosmosHero
2. Limit `<link rel="preload">` to 2-3 images max (not 6) — over-preloading competes for bandwidth
3. Keep Preloader disabled (`ENABLE_PRELOADER = false`)

### 5.6 CLS Prevention

1. Add `width` + `height` attributes to all `<img>` tags in hero/CosmosHero
2. Ensure `next/font` uses `display: 'swap'` with `adjustFontFallback: true`
3. Add `min-height` to typewriter effect container in `problem.tsx`

### 5.7 LazyMotion Migration (Longer-term)

**Impact: -30KB initial JS | Effort: 2-3 hours**

Switch from `motion.*` to `m.*` + `LazyMotion`:

```typescript
// Provider
import { LazyMotion } from 'motion/react';
const loadFeatures = () => import('@/lib/motion-features').then(mod => mod.default);

<LazyMotion features={loadFeatures} strict>
  {children}
</LazyMotion>

// Components: motion.div → m.div
import * as m from 'motion/react-m';
<m.div animate={{ opacity: 1 }} />
```

The `strict` prop throws errors if any file accidentally imports the full `motion` component.

### 5.8 Server/Client Component Split (Longest-term)

**Impact: -50%+ homepage JS | Effort: 4-6 hours**

Push `'use client'` boundaries down to leaf components. Sections like `footer.tsx`, `trusted-by.tsx`, `numbers-speak.tsx` can be mostly Server Components with tiny Client Component islands for animations.

---

## 6. Images (62 → 95+)

### 6.1 Use `next/image` for All Static Images

Replace raw `<img>` tags with `next/image` for all before/after and showcase images:

```tsx
import Image from 'next/image';
import afterPhoto from '@/public/cravemode/after-1.jpg';

<Image
  src={afterPhoto}
  alt="Enhanced restaurant food photo — grilled salmon with herbs"
  placeholder="blur"
  quality={80}
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
  className="h-full w-full object-cover"
/>
```

Static imports give automatic blur placeholder + dimensions.

### 6.2 Generate Blur Placeholders

For dynamically-referenced images, create `scripts/generate-blur-placeholders.mjs`:

```javascript
const buffer = await sharp(filePath).resize(10).blur().toBuffer();
const base64 = `data:image/jpeg;base64,${buffer.toString('base64')}`;
```

Save to `src/lib/blur-placeholders.json`, reference in components.

### 6.3 Descriptive Alt Text

Replace empty `alt=""` on hero images with descriptive text. For decorative images, `alt=""` is correct, but for content images (before/after gallery, showcase), use descriptive text:

- Good: `alt="Enhanced restaurant photo — grilled salmon with roasted vegetables"`
- Bad: `alt="photo"` or `alt=""`

### 6.4 Proper `sizes` Attribute

Every `next/image` should have a `sizes` attribute matching its responsive behavior:

```tsx
// Full-width mobile, half on tablet, third on desktop
sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"

// Fixed-width sidebar image
sizes="300px"
```

Without `sizes`, the browser downloads the largest srcset variant.

---

## 7. AI Search / GEO (78 → 95+)

### 7.1 Expand `llms.txt`

**Impact: MEDIUM | Effort: LOW**

Current llms.txt is ~30 lines. Expand to 100+ lines with:

- Key statistics (cost per photo, savings %, delivery speed)
- Links to all key pages with one-sentence descriptions
- Comparison table (AI vs. photographer)
- FAQ pairs matching natural query phrasing
- Pricing plan details

Full recommended content is in the Schema/GEO research output.

### 7.2 Update `robots.ts` — Differentiate AI Bots

**Impact: MEDIUM | Effort: LOW**

```typescript
rules: [
  { userAgent: "*", allow: "/", disallow: ["/api/", "/auth/", "/explore", "/image", "/video", "/gallery", "/queue", "/settings"] },
  // Allow AI SEARCH bots (real-time citation)
  { userAgent: "ChatGPT-User", allow: "/" },
  { userAgent: "Claude-SearchBot", allow: "/" },
  { userAgent: "PerplexityBot", allow: "/" },
  // Block AI TRAINING bots (prevent content in training data)
  { userAgent: "GPTBot", disallow: "/" },
  { userAgent: "Google-Extended", disallow: "/" },
  { userAgent: "CCBot", disallow: "/" },
  { userAgent: "anthropic-ai", disallow: "/" },
],
```

### 7.3 Add Statistics to ALL Content Pages

**Impact: +41% AI visibility (single most effective GEO technique)**

Every service page, guide, and blog post should include concrete numbers with sources:

- "CraveMode AI costs $8-$33 per photo compared to $75-$150 from traditional photographers — a 78-95% cost reduction"
- "Restaurants with menu photos receive up to 70% more orders (Grubhub)"
- "Delivery speed: 24-48 hours vs. 2-3 weeks from traditional photographers"

### 7.4 Self-Contained Answer Passages

AI systems score passages independently. Optimal: **134-167 words** that fully answer a query without surrounding context.

Rewrite key sections as standalone answer blocks. Each should:
- Open with a definition or direct answer
- Include 1-2 statistics with attribution
- Close with a conclusion or next step
- Be extractable from the page without losing meaning

### 7.5 Entity SEO — Build Brand Presence

Create profiles on these platforms (all with identical brand name "CraveMode AI"):
1. Crunchbase (free profile)
2. LinkedIn Company Page
3. YouTube Channel
4. Instagram Business
5. Product Hunt
6. G2 (free listing)
7. Capterra (free listing)
8. Wikidata entry (structured data seed for Knowledge Graph)

**Knowledge Panel requirements:** ~30+ sources consistently confirming entity information. Takes 3-6 months.

---

## Implementation Priority Matrix

### Week 1 — Quick Wins (72 → ~88)

| # | Task | Category | Impact | Effort |
|---|------|----------|--------|--------|
| 1 | Add security headers to `next.config.mjs` | Technical | HIGH | 15 min |
| 2 | Add canonical tags to 13 missing pages | Technical | HIGH | 1 hr |
| 3 | Add `formats: ['image/avif', 'image/webp']` to config | Images | HIGH | 5 min |
| 4 | Remove fabricated statistics from trusted-by.tsx + numbers-speak.tsx | E-E-A-T | CRITICAL | 1 hr |
| 5 | Add `duration` to VideoObject schema | Schema | HIGH | 10 min |
| 6 | Enhance Organization schema (@id, sameAs, foundingDate) | Schema | HIGH | 30 min |
| 7 | Update robots.ts to differentiate AI training vs search bots | GEO | MEDIUM | 15 min |
| 8 | Add `fetchpriority="high"` to top hero images | CWV | MEDIUM | 15 min |
| 9 | Add `width`/`height` to all `<img>` tags | CWV | MEDIUM | 30 min |

### Week 2 — Content Fixes (88 → ~92)

| # | Task | Category | Impact | Effort |
|---|------|----------|--------|--------|
| 10 | Remove sitemap `changeFrequency` + `priority`, fix `lastModified` | Technical | MEDIUM | 2 hr |
| 11 | Expand llms.txt to 100+ lines | GEO | MEDIUM | 1 hr |
| 12 | Add inline source citations to 9 blog posts | E-E-A-T | HIGH | 3 hr |
| 13 | Add WebApplication + AggregateOffer schema to pricing | Schema | HIGH | 1 hr |
| 14 | Add ImageGallery schema to /showcase | Schema | MEDIUM | 30 min |
| 15 | Add statistics + comparison tables to service pages | GEO | HIGH | 2 hr |
| 16 | Remove duplicate framer-motion package | CWV | HIGH | 30 min |
| 17 | Pre-compress hero images with Sharp script | Images | HIGH | 1 hr |

### Week 3-4 — Structural Improvements (92 → ~95)

| # | Task | Category | Impact | Effort |
|---|------|----------|--------|--------|
| 18 | Create `/about` page with founder story + team bios | E-E-A-T | HIGH | 3 hr |
| 19 | Add author bylines to all 9 blog posts | E-E-A-T | MEDIUM | 2 hr |
| 20 | Dynamic import all below-fold homepage sections | CWV | HIGH | 1 hr |
| 21 | Generate blur placeholders for all images | Images | MEDIUM | 1 hr |
| 22 | Migrate hero images to `next/image` where possible | Images | HIGH | 2 hr |
| 23 | Add self-contained 134-167 word answer passages | GEO | HIGH | 3 hr |
| 24 | Internal linking audit + cross-linking | On-Page | MEDIUM | 2 hr |
| 25 | Add definition-style openings to all service/tool pages | GEO | MEDIUM | 1 hr |

### Month 2-3 — Scale & Authority (95 → 98+)

| # | Task | Category | Impact | Effort |
|---|------|----------|--------|--------|
| 26 | Enrich 50 city pages with unique content (500+ words each) | E-E-A-T | CRITICAL | 20 hr |
| 27 | LazyMotion + `m` component migration | CWV | HIGH | 3 hr |
| 28 | Server/Client component split for sections | CWV | HIGH | 6 hr |
| 29 | Build hub pages (/restaurant-marketing, /restaurant-video) | On-Page | MEDIUM | 4 hr |
| 30 | Launch beta program + collect case studies | E-E-A-T | HIGH | Ongoing |
| 31 | Create Crunchbase, G2, Capterra, Wikidata profiles | GEO | MEDIUM | 2 hr |
| 32 | Publish 4-8 new deeply-researched blog posts/month | E-E-A-T | HIGH | Ongoing |
| 33 | Replace simple Framer Motion animations with CSS | CWV | MEDIUM | 3 hr |

---

## Key Research Sources

### Technical SEO
- Next.js Official: [headers()](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers), [CSP Guide](https://nextjs.org/docs/app/guides/content-security-policy)
- [CVE-2025-29927 Analysis](https://www.averlon.ai/blog/nextjs-cve-2025-29927-header-injection)
- Google: [Sitemaps Best Practices](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

### E-E-A-T & Content
- [E-E-A-T in 2026](https://ibrandstrategist.com/newsletter/google-e-e-a-t-in-2026-what-it-means-for-seo-and-your-rankings/)
- [December Core Update 2025](https://pamsalon.medium.com/december-core-update-2025-the-new-authority-signals-you-need-6dbcb5a7f602)
- [Programmatic SEO Without Traffic Loss](https://www.getpassionfruit.com/blog/programmatic-seo-traffic-cliff-guide)

### Performance & Images
- Next.js: [Image Component](https://nextjs.org/docs/app/api-reference/components/image), [Image Config](https://nextjs.org/docs/app/api-reference/config/next-config-js/images)
- Motion.dev: [Reduce Bundle Size](https://motion.dev/docs/react-reduce-bundle-size), [LazyMotion](https://motion.dev/docs/react-lazy-motion)
- [DebugBear: Next.js Image Optimization](https://www.debugbear.com/blog/nextjs-image-optimization)

### Schema & GEO
- [FAQ Schema for AI Search](https://www.frase.io/blog/faq-schema-ai-search-geo-aeo)
- [GEO vs SEO 2025](https://strapi.io/blog/generative-engine-optimization-vs-traditional-seo-guide)
- [AI Overview Ranking Factors 2026](https://wellows.com/blog/google-ai-overviews-ranking-factors/)
- [How to Get Cited by AI](https://searchengineland.com/how-to-get-cited-by-ai-seo-insights-from-8000-ai-citations-455284)
- [Entity SEO for Startups](https://blog.mean.ceo/entity-seo-for-startups/)

### Citable Statistics for CraveMode Content
- "Up to 70% more orders with menu photos" — Grubhub
- "82% order based on how food looks" — IJIRT research
- "Menu photos increase sales 20-45%" — Multiple studies
- "US fast food market: $658.85B in 2025" — ResearchAndMarkets
- "Online food delivery: $257.43B in 2025, projected $694.65B by 2035" — Precedence Research
- "DoorDash holds 56% of US delivery market" — OysterLink
