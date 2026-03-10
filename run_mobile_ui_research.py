#!/usr/bin/env python3
"""RECON research: Premium mobile food photography app UI/UX patterns 2025-2026"""

import sys
import json
import asyncio

sys.path.insert(0, '/Users/nafiurrahman/Desktop/Foodshot/recon-researcher')

from src.youtube_search import search_and_curate

async def main():
    print("Running RECON Mobile UI/UX Research...")
    print("=" * 60)

    all_results = {}

    # Query 1: Premium dark mode mobile app UI design
    print("\nQuery 1: Premium Dark Mode Mobile App UI Design 2025-2026")
    print("-" * 60)
    try:
        results1 = await search_and_curate(
            query="premium dark mode mobile app UI design 2025 2026 glassmorphism",
            num_videos=5,
            mode="expert",
            analyze_transcripts=False
        )
        all_results['dark_mode_ui'] = results1
        if results1.get('videos'):
            for i, v in enumerate(results1['videos'][:5], 1):
                print(f"{i}. {v.get('title', 'N/A')}")
                print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")
    except Exception as e:
        print(f"   Error: {e}")
        all_results['dark_mode_ui'] = {'error': str(e)}

    # Query 2: Food photography app UI/UX design
    print("\nQuery 2: Food Photography App UI/UX Design Patterns")
    print("-" * 60)
    try:
        results2 = await search_and_curate(
            query="food photography app UI UX design mobile best practices",
            num_videos=5,
            mode="expert",
            analyze_transcripts=False
        )
        all_results['food_app_ux'] = results2
        if results2.get('videos'):
            for i, v in enumerate(results2['videos'][:5], 1):
                print(f"{i}. {v.get('title', 'N/A')}")
                print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")
    except Exception as e:
        print(f"   Error: {e}")
        all_results['food_app_ux'] = {'error': str(e)}

    # Query 3: React Native animation patterns premium
    print("\nQuery 3: React Native Premium Animations & Micro-interactions")
    print("-" * 60)
    try:
        results3 = await search_and_curate(
            query="react native reanimated premium animations micro interactions 2025",
            num_videos=5,
            mode="expert",
            analyze_transcripts=False
        )
        all_results['rn_animations'] = results3
        if results3.get('videos'):
            for i, v in enumerate(results3['videos'][:5], 1):
                print(f"{i}. {v.get('title', 'N/A')}")
                print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")
    except Exception as e:
        print(f"   Error: {e}")
        all_results['rn_animations'] = {'error': str(e)}

    # Query 4: Mobile app glassmorphism implementation
    print("\nQuery 4: Glassmorphism & Liquid Glass Mobile Implementation")
    print("-" * 60)
    try:
        results4 = await search_and_curate(
            query="glassmorphism liquid glass mobile app design implementation iOS",
            num_videos=5,
            mode="expert",
            analyze_transcripts=False
        )
        all_results['glassmorphism'] = results4
        if results4.get('videos'):
            for i, v in enumerate(results4['videos'][:5], 1):
                print(f"{i}. {v.get('title', 'N/A')}")
                print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")
    except Exception as e:
        print(f"   Error: {e}")
        all_results['glassmorphism'] = {'error': str(e)}

    # Query 5: AI creative tools mobile app design
    print("\nQuery 5: AI Creative Tools Mobile App Design")
    print("-" * 60)
    try:
        results5 = await search_and_curate(
            query="AI photo editing app mobile design UX Remini Lensa VSCO 2025",
            num_videos=5,
            mode="expert",
            analyze_transcripts=False
        )
        all_results['ai_creative_apps'] = results5
        if results5.get('videos'):
            for i, v in enumerate(results5['videos'][:5], 1):
                print(f"{i}. {v.get('title', 'N/A')}")
                print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")
    except Exception as e:
        print(f"   Error: {e}")
        all_results['ai_creative_apps'] = {'error': str(e)}

    # Query 6: Mobile tab bar design patterns bottom navigation
    print("\nQuery 6: Bottom Tab Bar Design Patterns & Custom Navigation")
    print("-" * 60)
    try:
        results6 = await search_and_curate(
            query="mobile bottom tab bar custom design patterns animation 2025",
            num_videos=5,
            mode="expert",
            analyze_transcripts=False
        )
        all_results['tab_bar_design'] = results6
        if results6.get('videos'):
            for i, v in enumerate(results6['videos'][:5], 1):
                print(f"{i}. {v.get('title', 'N/A')}")
                print(f"   Channel: {v.get('channel', 'N/A')} | Views: {v.get('views', 0):,} | Score: {v.get('score', 0)}/100")
    except Exception as e:
        print(f"   Error: {e}")
        all_results['tab_bar_design'] = {'error': str(e)}

    # Save results
    output_path = '/Users/nafiurrahman/Desktop/Foodshot/recon_mobile_ui_research.json'
    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)

    print("\n" + "=" * 60)
    print(f"RECON research complete! Results saved to: recon_mobile_ui_research.json")
    total_videos = sum(len(r.get('videos', [])) for r in all_results.values() if isinstance(r, dict) and 'videos' in r)
    print(f"Total videos found across all queries: {total_videos}")

    return all_results

if __name__ == "__main__":
    asyncio.run(main())
