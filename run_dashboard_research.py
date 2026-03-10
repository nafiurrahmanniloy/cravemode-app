#!/usr/bin/env python3
"""Dashboard research using RECON - AI generation platform UX patterns"""

import sys
import json
import asyncio

sys.path.insert(0, '/Users/nafiurrahman/Desktop/Foodshot/recon-researcher')

from src.youtube_search import search_and_curate

async def main():
    print("Running RECON Dashboard Research...")
    print("=" * 60)

    all_results = {}

    # Query 1: AI Image/Video Generation Dashboard Design
    print("\nQuery 1: AI Generation Platform Dashboard UX")
    print("-" * 60)
    results1 = await search_and_curate(
        query="AI image video generation platform dashboard UI UX design 2025 2026",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['ai_gen_dashboard_ux'] = results1
    if results1.get('videos'):
        for i, v in enumerate(results1['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 2: SaaS Dashboard Best Practices
    print("\nQuery 2: SaaS Dashboard Design Best Practices")
    print("-" * 60)
    results2 = await search_and_curate(
        query="SaaS dashboard design best practices dark theme Next.js 2025",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['saas_dashboard_design'] = results2
    if results2.get('videos'):
        for i, v in enumerate(results2['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 3: Runway Midjourney Leonardo Dashboard Walkthrough
    print("\nQuery 3: AI Tool Dashboard Walkthroughs")
    print("-" * 60)
    results3 = await search_and_curate(
        query="Runway ML Leonardo AI Midjourney dashboard walkthrough interface tutorial 2025",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['ai_tool_walkthroughs'] = results3
    if results3.get('videos'):
        for i, v in enumerate(results3['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 4: Food Photography AI Tool / Restaurant SaaS
    print("\nQuery 4: Food Photography AI Platform Design")
    print("-" * 60)
    results4 = await search_and_curate(
        query="food photography AI platform restaurant SaaS tool design UX",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['food_ai_platform'] = results4
    if results4.get('videos'):
        for i, v in enumerate(results4['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 5: Authentication & User Dashboard Next.js
    print("\nQuery 5: Next.js Authentication Dashboard Build")
    print("-" * 60)
    results5 = await search_and_curate(
        query="Next.js 14 authentication dashboard build tutorial clerk auth 2025",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['nextjs_auth_dashboard'] = results5
    if results5.get('videos'):
        for i, v in enumerate(results5['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Query 6: Higgsfield Kie AI Platform Review
    print("\nQuery 6: Higgsfield & Kie AI Platform Reviews")
    print("-" * 60)
    results6 = await search_and_curate(
        query="Higgsfield AI review walkthrough Kie AI Kling video generation platform 2025",
        num_videos=5,
        mode="expert",
        analyze_transcripts=False
    )
    all_results['higgsfield_kie_reviews'] = results6
    if results6.get('videos'):
        for i, v in enumerate(results6['videos'][:5], 1):
            print(f"{i}. {v.get('title', 'N/A')}")
            print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")

    # Save results
    output_path = '/Users/nafiurrahman/Desktop/Foodshot/recon_dashboard_research.json'
    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2)

    print("\n" + "=" * 60)
    print(f"Research complete! Results saved to: recon_dashboard_research.json")
    print(f"Total videos found: {sum(len(r.get('videos', [])) for r in all_results.values())}")

    return all_results

if __name__ == "__main__":
    asyncio.run(main())
