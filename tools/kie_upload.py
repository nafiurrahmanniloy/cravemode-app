"""
Kie.ai file upload utility for FoodShot AI.
Uploads reference images and gets hosted URLs (3-day expiry).
"""

import requests
from pathlib import Path
from .config import KIE_API_KEY, KIE_FILE_UPLOAD_URL


def upload_references(file_paths):
    """
    Upload reference images to Kie.ai and get hosted URLs.

    Args:
        file_paths: List of local file paths to upload

    Returns:
        list: Hosted image URLs from Kie.ai
    """
    if not KIE_API_KEY:
        raise ValueError("KIE_API_KEY not set in .claude/.env")

    uploaded_urls = []

    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue

        print(f"📤 Uploading {path.name}...")

        with open(path, "rb") as f:
            files = {"file": (path.name, f)}
            # CRITICAL: uploadPath must be included or request fails
            data = {"uploadPath": "foodshot-hero"}
            response = requests.post(
                KIE_FILE_UPLOAD_URL,
                files=files,
                data=data,
                headers={"Authorization": f"Bearer {KIE_API_KEY}"}
            )

        if response.status_code == 200:
            result = response.json()
            if result.get("success") or result.get("code") == 200:
                url = result.get("data", {}).get("downloadUrl")
                if url:
                    uploaded_urls.append(url)
                    print(f"✅ Uploaded: {url}")
                else:
                    print(f"❌ No downloadUrl in response for {path.name}")
            else:
                print(f"❌ Upload failed: {result.get('msg', result)}")
        else:
            print(f"❌ Upload failed: {response.status_code} - {response.text}")

    print(f"\n✅ Uploaded {len(uploaded_urls)}/{len(file_paths)} images")
    return uploaded_urls


def upload_single(file_path):
    """Upload a single file and return the URL."""
    urls = upload_references([file_path])
    return urls[0] if urls else None
