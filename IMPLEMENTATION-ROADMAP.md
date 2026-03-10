# CraveMode AI — SEO Implementation Roadmap

> Phased execution plan with specific tasks, owners, and success criteria

---

## Phase 1 — Foundation (Weeks 1-4)

**Goal**: Get the technical SEO infrastructure right and launch core pages.

### Week 1: Technical SEO Setup

| # | Task | Type | Priority | Details |
|---|------|------|----------|---------|
| 1.1 | Create `robots.txt` | Code | P0 | Allow crawling of public pages, block `/api/`, `/auth/`, dashboard routes. Allow GPTBot, ClaudeBot, PerplexityBot. |
| 1.2 | Create `sitemap.ts` | Code | P0 | Next.js dynamic sitemap. Include all public pages, exclude auth-protected. Split into sitemap index with sub-sitemaps. |
| 1.3 | Add Organization schema | Code | P0 | JSON-LD on root layout — name, url, logo, sameAs (social profiles), contactPoint. |
| 1.4 | Add FAQPage schema | Code | P0 | JSON-LD on landing page FAQ section. Extract Q&A pairs from existing FAQ component. |
| 1.5 | Add Service schema | Code | P0 | JSON-LD on landing page — describe photo and video services. |
| 1.6 | Add page-level metadata | Code | P0 | Unique title + description for `/showcase`, `/sign-in`, `/sign-up`, `/explore`, `/image`, `/video`, `/gallery`, `/queue`, `/settings`. |
| 1.7 | Register Google Search Console | Setup | P0 | Verify domain ownership, submit sitemap. |
| 1.8 | Register Bing Webmaster Tools | Setup | P1 | Submit sitemap. |
| 1.9 | Set up GA4 | Setup | P0 | Install tracking, set up conversion events (sign-up, checkout). |
| 1.10 | Add `llms.txt` | Code | P1 | Describe site structure and services for AI crawlers. |

**Success Criteria**: All public pages indexed in Google within 2 weeks. Search Console showing zero errors.

### Week 2: Core Page Build

| # | Task | Type | Priority | Details |
|---|------|------|----------|---------|
| 2.1 | Build `/pricing` page | Code + Content | P0 | Standalone pricing page. All 6 plans (3 subscription + 3 one-time). Comparison table vs alternatives. FAQ. Product schema per plan. |
| 2.2 | Build `/services` hub | Code + Content | P0 | Overview page linking to photo, video, social media kit. Highlight the unique photo+video combo. |
| 2.3 | Add BreadcrumbList schema | Code | P1 | Dynamic breadcrumbs component with schema markup for all new pages. |
| 2.4 | Internal linking audit | Code | P1 | Ensure landing page links to /pricing, /showcase, /services. Footer links updated. |

### Week 3: Service Pages

| # | Task | Type | Priority | Details |
|---|------|------|----------|---------|
| 3.1 | Build `/services/photo-enhancement` | Code + Content | P0 | Before/after gallery, process walkthrough, formats, pricing link. Service schema. ~1,500 words. |
| 3.2 | Build `/services/video-creation` | Code + Content | P0 | Video samples, Reels/TikTok focus, turnaround times. Service schema. ~1,500 words. Emphasize: NO competitor offers this. |
| 3.3 | Optimize existing `/showcase` | Code | P1 | Add metadata, Schema (ImageGallery), filtering by cuisine/style. |

### Week 4: First Pillar Blog Post

| # | Task | Type | Priority | Details |
|---|------|------|----------|---------|
| 4.1 | Build `/blog` layout | Code | P0 | Blog index page with pagination. Blog post template with TOC, author, date, reading time, related posts. |
| 4.2 | Write "Food Photography Cost 2026" | Content | P0 | 3,000-4,000 word pillar post. City pricing data, photographer vs AI vs agency. Comparison tables. FAQ section. Internal links to pricing + services. |
| 4.3 | Add Article + Person schema | Code | P1 | Blog post template includes author bio and Article schema. |

**Phase 1 Deliverables**: 8 new pages, full technical SEO infrastructure, first blog post, analytics tracking.

---

## Phase 2 — Expansion (Weeks 5-12)

**Goal**: Build the content moat with city pages, platform guides, and comparison content.

### Weeks 5-6: City Pages (Batch 1)

| # | Task | Priority | Details |
|---|------|----------|---------|
| 5.1 | Build city page template | P0 | Reusable Next.js template with dynamic data. generateStaticParams or on-demand ISR. |
| 5.2 | Create city data file | P0 | JSON/TS file with 50 cities: name, slug, state, population, restaurant count, avg photographer cost, local stats. |
| 5.3 | Launch first 10 city pages | P0 | NYC, LA, Chicago, Miami, Houston, SF, Dallas, Atlanta, Seattle, Boston. Each ~1,500-2,000 words with city-specific content. |
| 5.4 | Add inter-city linking | P1 | "See also: Food photography in [nearby cities]" section. |

### Weeks 7-8: Platform Guides + Blog

| # | Task | Priority | Details |
|---|------|----------|---------|
| 7.1 | `/guides/uber-eats-photos` | P0 | Uber Eats photo specs, requirements, tips. High-intent keyword. ~2,000 words. |
| 7.2 | `/guides/doordash-menu-photos` | P0 | DoorDash requirements guide. ~2,000 words. |
| 7.3 | Blog: "Restaurant Video Content Guide" | P0 | OWN this keyword — no competitor has it. 2,500+ words. |
| 7.4 | Blog: "15 Food Photography Tips" | P1 | Educational top-of-funnel content. 2,000 words. |

### Weeks 9-10: Comparison Pages

| # | Task | Priority | Details |
|---|------|----------|---------|
| 9.1 | `/compare/ai-vs-photographer` | P0 | Feature/cost/time comparison. Balanced tone. 2,000 words. |
| 9.2 | `/compare/cravemode-vs-foodshot` | P0 | Honest comparison. Highlight video + managed service. 1,500 words. |
| 9.3 | `/compare/managed-vs-self-service` | P1 | Position the "done-for-you" advantage. 1,500 words. |
| 9.4 | More platform guides | P1 | GrubHub, Google Business, Instagram guides. |

### Weeks 11-12: Restaurant Type Pages + Blog

| # | Task | Priority | Details |
|---|------|----------|---------|
| 11.1 | Build restaurant type template | P0 | Reusable template for `/for/[type]` pages. |
| 11.2 | Launch first 5 type pages | P0 | Fine dining, fast casual, cafes, food trucks, bakeries. ~1,500 words each. |
| 11.3 | Blog: "Food Photography Lighting Guide" | P1 | Educational pillar content. 2,500 words. |
| 11.4 | Blog: "Food Photography ROI" | P1 | Data-driven commercial content. 2,000 words. |
| 11.5 | Launch 5 more city pages | P1 | Phoenix, Denver, San Diego, Austin, Nashville. |

**Phase 2 Deliverables**: 30+ new pages, programmatic template system, 4 blog posts, competitive content.

---

## Phase 3 — Scale (Weeks 13-24)

**Goal**: Scale content production, build authority signals, start link building.

### Monthly Recurring Tasks

| Task | Frequency | Details |
|------|-----------|---------|
| Blog posts | 4/month | Mix of educational, commercial, data-driven |
| City pages | 5/month | Remaining 35 cities from template |
| Content refresh | 1/month | Update top-performing posts with new data |
| Competitor monitoring | 1/month | Track new competitor content, adjust strategy |
| Technical SEO audit | 1/month | Check Core Web Vitals, crawl errors, index coverage |

### Key Milestones

| Week | Milestone | Success Metric |
|------|-----------|---------------|
| 13 | 50 total pages indexed | GSC index coverage |
| 16 | First page-1 ranking | Any target keyword |
| 18 | 100 organic sessions/week | GA4 |
| 20 | 75 total pages indexed | GSC index coverage |
| 24 | 500 organic sessions/week | GA4 |

### Authority Building Actions

| Action | Timeline | Expected Impact |
|--------|----------|----------------|
| Submit to Capterra | Week 13 | Review presence + backlink |
| Submit to G2 | Week 13 | Review presence + backlink |
| Submit to GetApp | Week 13 | Review presence + backlink |
| HARO / Connectively responses | Weekly from Week 14 | Expert quotes → backlinks |
| Guest post on restaurant industry blog | Week 16 | Domain authority boost |
| Create free tool (photo quality checker) | Week 20 | Link magnet |
| Publish original research | Week 22 | Citation source |

---

## Phase 4 — Authority (Months 7-12)

**Goal**: Establish CraveMode AI as the go-to resource for restaurant visual content.

### Content Maturity Actions

| Action | Details |
|--------|---------|
| Update all "2026" content to "2027" | Refresh titles, data, and stats before year-end |
| "State of Restaurant Visual Content" report | Original research based on client data |
| Video content (YouTube) | Tutorials, case studies, tips — embed in blog posts |
| Podcast guest appearances | Restaurant industry podcasts |
| Partner content | Co-authored content with restaurant associations |
| Advanced schema | Recipe schema for food blogs, VideoObject for video content |

### Expected Results (Month 12)

| Metric | Target |
|--------|--------|
| Organic sessions/month | 10,000-20,000 |
| Pages indexed | 150-200 |
| Keywords in top 10 | 80-150 |
| Domain Rating | 35-50 |
| Organic leads/month | 80-150 |
| Revenue from organic | Track via GA4 attribution |

---

## Resource Requirements

### Phase 1 (Weeks 1-4)
- **Developer**: 20-30 hours (technical SEO, page templates, schema)
- **Content writer**: 15-20 hours (pricing page, services, blog post)
- **Tools**: Google Search Console (free), GA4 (free)

### Phase 2 (Weeks 5-12)
- **Developer**: 15-20 hours (city template, blog template, comparison layout)
- **Content writer**: 40-50 hours (city pages, guides, blog posts, comparison content)
- **Tools**: Ahrefs or SEMrush ($99-$199/mo for keyword tracking)

### Phase 3 (Weeks 13-24)
- **Content writer**: 20-30 hours/month (blog posts, city pages, refreshes)
- **Link building**: 5-10 hours/month (outreach, HARO, guest posts)
- **Tools**: Same as Phase 2

### Phase 4 (Months 7-12)
- **Content writer**: 20-30 hours/month
- **Video production**: 10-15 hours/month (if pursuing YouTube)
- **PR/outreach**: 10 hours/month
- **Tools**: Same + PR tool (optional)

---

## Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|:-----------:|:------:|------------|
| Slow indexing (new domain) | High | Medium | Submit pages manually in GSC. Build initial backlinks from directories. |
| Competitor copies video content strategy | Medium | Low | First-mover advantage. Keep publishing. Build brand recognition. |
| Google algorithm update | Medium | Medium | Diversify traffic sources. Focus on genuine value, not gaming algorithms. |
| Thin content on city pages | Medium | High | Ensure each city page has 1,500+ unique words. Add real local data. |
| Content production slowdown | Medium | Medium | Build templates for easy replication. Batch-produce similar content types. |
| No clients for case studies | High (early) | Medium | Use demo before/after examples initially. Replace with real clients ASAP. |

---

## Quick Start Checklist

For the developer starting Phase 1 this week:

```
[ ] Create src/app/robots.ts
[ ] Create src/app/sitemap.ts
[ ] Add JSON-LD component (src/components/schema.tsx)
[ ] Add Organization schema to root layout
[ ] Add FAQPage schema to landing page
[ ] Add Service schema to landing page
[ ] Add unique metadata exports to all page.tsx files
[ ] Create src/app/pricing/page.tsx
[ ] Create src/app/services/page.tsx
[ ] Create src/app/services/photo-enhancement/page.tsx
[ ] Create src/app/services/video-creation/page.tsx
[ ] Create src/app/blog/page.tsx (index)
[ ] Create src/app/blog/[slug]/page.tsx (post template)
[ ] Create llms.txt in public/
[ ] Register Google Search Console
[ ] Set up GA4
```
