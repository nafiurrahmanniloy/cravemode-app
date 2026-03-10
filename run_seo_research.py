"""
RECON SEO Research for CraveMode AI
Target: 95+ SEO score across all categories

Research queries organized by audit category:
1. Technical SEO (72→95): Security headers, canonical tags, JS rendering
2. Content Quality / E-E-A-T (52→95): Case studies, trust signals, thin content
3. On-Page SEO (82→95): Advanced on-page strategies
4. Schema / Structured Data (82→95): Advanced schema, rich results
5. Performance / CWV (70→95): Next.js image optimization, LCP, INP
6. Images (62→95): Next.js Image component, WebP/AVIF, compression
7. AI Search Readiness / GEO (78→95): AI Overviews, citations, GEO
"""

import sys
import json
import asyncio

sys.path.insert(0, '/Users/nafiurrahman/Desktop/Foodshot/recon-researcher')
from src.youtube_search import search_and_curate


async def main():
    all_results = {}

    queries = {
        # --- TECHNICAL SEO (72 → 95) ---
        "nextjs_security_headers": {
            "query": "Next.js security headers configuration HSTS CSP X-Frame-Options 2025 2026",
            "num_videos": 5,
            "mode": "expert",
        },
        "nextjs_canonical_tags": {
            "query": "Next.js canonical tags metadata API app router SEO best practices",
            "num_videos": 5,
            "mode": "expert",
        },
        "nextjs_seo_technical": {
            "query": "Next.js 14 15 technical SEO complete guide crawlability indexability 2025 2026",
            "num_videos": 5,
            "mode": "expert",
        },

        # --- CONTENT QUALITY / E-E-A-T (52 → 95) ---
        "eeat_signals_seo": {
            "query": "E-E-A-T signals SEO 2025 2026 experience expertise authority trust Google",
            "num_videos": 5,
            "mode": "expert",
        },
        "case_studies_trust_signals": {
            "query": "SaaS case studies trust signals social proof conversion SEO best practices",
            "num_videos": 5,
            "mode": "expert",
        },
        "thin_content_programmatic_seo": {
            "query": "programmatic SEO avoid thin content duplicate city pages template differentiation 2025",
            "num_videos": 5,
            "mode": "expert",
        },
        "topical_authority_content": {
            "query": "topical authority content strategy SEO 2025 2026 content clusters pillar pages",
            "num_videos": 5,
            "mode": "expert",
        },

        # --- SCHEMA / STRUCTURED DATA (82 → 95) ---
        "schema_markup_advanced": {
            "query": "advanced schema markup structured data JSON-LD rich results 2025 2026 SEO",
            "num_videos": 5,
            "mode": "expert",
        },
        "schema_service_pricing": {
            "query": "schema markup Service pricing page Offer AggregateOffer JSON-LD SEO",
            "num_videos": 5,
            "mode": "expert",
        },

        # --- PERFORMANCE / CWV (70 → 95) ---
        "nextjs_core_web_vitals": {
            "query": "Next.js Core Web Vitals optimization LCP INP CLS 2025 2026 performance",
            "num_videos": 5,
            "mode": "expert",
        },
        "nextjs_image_optimization": {
            "query": "Next.js Image component optimization WebP AVIF lazy loading blur placeholder performance",
            "num_videos": 5,
            "mode": "expert",
        },
        "framer_motion_performance": {
            "query": "Framer Motion performance optimization React reduce bundle size animation SEO",
            "num_videos": 5,
            "mode": "expert",
        },

        # --- IMAGES (62 → 95) ---
        "image_seo_optimization": {
            "query": "image SEO optimization alt text WebP AVIF compression responsive images 2025 2026",
            "num_videos": 5,
            "mode": "expert",
        },
        "nextjs_image_best_practices": {
            "query": "Next.js Image component best practices sizes priority placeholder quality",
            "num_videos": 5,
            "mode": "expert",
        },

        # --- AI SEARCH READINESS / GEO (78 → 95) ---
        "generative_engine_optimization": {
            "query": "Generative Engine Optimization GEO AI Overviews SEO 2025 2026 citations",
            "num_videos": 5,
            "mode": "expert",
        },
        "ai_search_optimization": {
            "query": "AI search optimization ChatGPT Perplexity Google AI Overviews llms.txt brand visibility",
            "num_videos": 5,
            "mode": "expert",
        },

        # --- OVERALL SEO STRATEGY ---
        "seo_95_score_strategy": {
            "query": "perfect SEO score 90 95 100 technical SEO audit checklist 2025 2026",
            "num_videos": 5,
            "mode": "expert",
        },
        "saas_seo_strategy": {
            "query": "SaaS SEO strategy B2B service business SEO 2025 2026 complete guide",
            "num_videos": 5,
            "mode": "expert",
        },
    }

    for key, params in queries.items():
        print(f"\n{'='*60}")
        print(f"Researching: {key}")
        print(f"Query: {params['query']}")
        print(f"{'='*60}")

        try:
            results = await search_and_curate(
                query=params["query"],
                num_videos=params["num_videos"],
                mode=params["mode"],
                analyze_transcripts=False,
            )
            all_results[key] = {
                "query": params["query"],
                "videos": results.get("videos", []),
                "total_candidates": results.get("total_candidates", 0),
                "filtered_out": results.get("filtered_out", 0),
            }
            video_count = len(results.get("videos", []))
            print(f"  Found {video_count} expert videos")
            for v in results.get("videos", [])[:3]:
                print(f"  - [{v.get('score', 0):.1f}] {v.get('title', 'N/A')[:70]}")
        except Exception as e:
            print(f"  ERROR: {e}")
            all_results[key] = {"query": params["query"], "error": str(e)}

    # Save results
    output_path = "/Users/nafiurrahman/Desktop/Foodshot/recon_seo_research.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n\n{'='*60}")
    print(f"RESEARCH COMPLETE — saved to {output_path}")
    print(f"Total queries: {len(queries)}")
    successful = sum(1 for v in all_results.values() if "error" not in v)
    print(f"Successful: {successful}/{len(queries)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main())
