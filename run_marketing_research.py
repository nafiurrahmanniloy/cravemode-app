#!/usr/bin/env python3
"""Marketing research using RECON"""

import sys
import json
import asyncio

sys.path.insert(0, '/Users/nafiurrahman/Desktop/Foodshot/recon-researcher')

from src.youtube_search import search_and_curate
from src.paper_search import search_papers

async def main():
    print("🔍 Running RECON Marketing Research...")
    print("=" * 60)

    all_results = {}

    # Query 1: Restaurant B2B Marketing
    print("\n📊 Query 1: Restaurant B2B Marketing Strategies")
    print("-" * 60)
    results1 = await search_and_curate(
        query="restaurant marketing strategy B2B food service 2025",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False  # Faster without transcript analysis
    )
    all_results['restaurant_marketing'] = results1
    if results1.get('videos'):
        for i, v in enumerate(results1['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 2: Landing Page Conversion
    print("\n🎯 Query 2: Landing Page Conversion Optimization")
    print("-" * 60)
    results2 = await search_and_curate(
        query="landing page conversion optimization best practices SaaS",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['landing_page_conversion'] = results2
    if results2.get('videos'):
        for i, v in enumerate(results2['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 3: Portfolio Design
    print("\n🖼️  Query 3: Portfolio Showcase Design & UX")
    print("-" * 60)
    results3 = await search_and_curate(
        query="portfolio showcase design UX how many examples optimal",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['portfolio_design'] = results3
    if results3.get('videos'):
        for i, v in enumerate(results3['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 4: Social Proof Placement
    print("\n✅ Query 4: Social Proof Placement Strategies")
    print("-" * 60)
    results4 = await search_and_curate(
        query="social proof placement landing page testimonials conversion",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['social_proof_placement'] = results4
    if results4.get('videos'):
        for i, v in enumerate(results4['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Save results
    output_path = '/Users/nafiurrahman/Desktop/Foodshot/recon_marketing_research.json'
    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2)

    print("\n" + "=" * 60)
    print(f"✅ Research complete! Results saved to: recon_marketing_research.json")
    print(f"📊 Total videos found across all queries: {sum(len(r.get('videos', [])) for r in all_results.values())}")

    return all_results

if __name__ == "__main__":
    asyncio.run(main())
