"""
Utility functions for FoodShot AI generation pipeline.
Polling, downloads, status printing, etc.
"""

import time
import requests
from pathlib import Path


def poll_job_status(status_url, headers, max_wait=300, interval=10):
    """
    Poll a job status endpoint until completion or timeout.

    Args:
        status_url: URL to check job status
        headers: Request headers (with API key)
        max_wait: Maximum seconds to wait (default: 300 = 5 minutes)
        interval: Seconds between checks (default: 10)

    Returns:
        dict: Final job status response
    """
    elapsed = 0
    while elapsed < max_wait:
        response = requests.get(status_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            status = data.get("data", {}).get("status")

            if status in ["completed", "success"]:
                return data
            elif status in ["failed", "error"]:
                error_msg = data.get("data", {}).get("error", "Unknown error")
                raise Exception(f"Job failed: {error_msg}")

            # Still processing
            print(f"⏳ Status: {status}... ({elapsed}s elapsed)")
        else:
            print(f"⚠️  Status check failed: {response.status_code}")

        time.sleep(interval)
        elapsed += interval

    raise TimeoutError(f"Job did not complete within {max_wait} seconds")


def download_asset(url, output_path):
    """
    Download an asset from URL to local path.

    Args:
        url: Asset URL
        output_path: Local file path to save to

    Returns:
        Path: Path to downloaded file
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    print(f"📥 Downloading {path.name}...")
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Downloaded: {path}")
        return path
    else:
        raise Exception(f"Download failed: {response.status_code}")


def print_cost_breakdown(model, count, provider=None):
    """
    Print cost breakdown for generation batch.

    Args:
        model: Model name
        count: Number of assets to generate
        provider: Provider name (optional)
    """
    from .config import get_cost

    unit_cost = get_cost(model, provider)
    total_cost = unit_cost * count

    print("\n💰 Cost Breakdown")
    print(f"   Model: {model}")
    if provider:
        print(f"   Provider: {provider}")
    print(f"   Quantity: {count}")
    print(f"   Unit Cost: ${unit_cost:.2f}")
    print(f"   Total Cost: ${total_cost:.2f}")
    print()


def confirm_generation(prompt_message="Proceed with generation?"):
    """
    Ask user for confirmation before proceeding.

    Args:
        prompt_message: Confirmation prompt

    Returns:
        bool: True if user confirms, False otherwise
    """
    response = input(f"{prompt_message} (yes/no): ").strip().lower()
    return response in ["yes", "y"]
