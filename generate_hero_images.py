"""
Generate enhanced food images for FoodShot AI website hero section.
Uses Nano Banana via Kie.ai following prompt best practices.
"""

import sys
import json
import time
import requests
from pathlib import Path

sys.path.insert(0, '.')
from tools.config import KIE_API_KEY, KIE_CREATE_URL, KIE_STATUS_URL

# Reference URLs (already uploaded to Kie.ai)
REFERENCE_URLS = [
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557577964-gzgktc9jrfp.jpg",  # food-02
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557579381-e2mu5bzfipf.jpg",  # food-03
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557580567-s9aqvuwz1vf.jpg",  # food-04
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557582674-6t2myj03urw.jpg",  # food-05
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557583792-oyfqm2yqcm.jpg",   # food-07
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557584893-1dxovvm3ip1.jpg",  # food-08
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557585993-bg6rwelns8m.jpg",  # food-09
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557587033-ndu8wzbvugr.jpg",  # food-13
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557588174-bdzxpb3za5v.jpg",  # food-14
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557589209-p8971h3pwd.jpg",   # food-15
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557590594-0thbtzu8rv8.jpg",  # food-16
    "https://tempfile.redpandaai.co/kieai/512766/foodshot-hero/1772557591916-ogjfrwz42j9.jpg",  # food-17
]

# Food descriptions for each image (will be used in prompts)
FOOD_DESCRIPTIONS = [
    "gourmet burger with melted cheese and fresh toppings",
    "colorful fresh salad bowl with mixed greens and vegetables",
    "artisanal pizza with herbs and premium ingredients",
    "elegant plated dessert with chocolate and berries",
    "steaming bowl of ramen with perfectly cooked noodles",
    "fresh sushi platter with colorful rolls and garnish",
    "golden crispy fried chicken with herbs",
    "decadent chocolate cake slice with cream",
    "vibrant smoothie bowl with fresh fruits and toppings",
    "gourmet sandwich with layers of fresh ingredients",
    "aromatic coffee with latte art and pastries",
    "authentic tacos with colorful toppings and lime",
]

# Enhancement prompts following best practices (16:9 ratio for website hero)
def create_prompt(description, input_num):
    """Create enhancement prompt following Nano Banana Pro best practices"""
    return f"""16:9. Professional food photography enhancement of {description}.
Preserve the exact background, setting, and composition from the reference image.
Enhance only the food appearance: boost color vibrancy, improve lighting on the dish, add subtle steam or freshness cues where appropriate.
Make the food look more appetizing with better color saturation, sharper details, and enhanced textures.
Maintain the original camera angle, framing, and environment exactly as shown.
Keep all existing props, tableware, and background elements unchanged.
Shot on high-end cinema camera, 50mm prime lens, sharp focus on the food.
Natural textures visible, rich appetizing colors, photorealistic finish.
Using input image {input_num} for accurate food identity, plating, and background preservation."""

print("🎨 FoodShot AI - Hero Image Generation")
print("=" * 60)
print(f"Generating {len(REFERENCE_URLS)} enhanced food images")
print(f"Aspect Ratio: 16:9 (website hero)")
print(f"Model: Nano Banana Pro via Kie.ai")
print("=" * 60)

# Step 1: Submit all generation tasks
print("\n📤 Submitting generation tasks...")
tasks = []

for i, (ref_url, description) in enumerate(zip(REFERENCE_URLS, FOOD_DESCRIPTIONS), 1):
    prompt = create_prompt(description, i)

    payload = {
        "model": "nano-banana-pro",
        "input": {
            "prompt": prompt,
            "aspect_ratio": "16:9",
            "resolution": "2K",  # High quality for website
            "output_format": "png",
            "image_input": [ref_url],
        },
    }

    headers = {
        "Authorization": f"Bearer {KIE_API_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(KIE_CREATE_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        if result.get("code") == 200:
            task_id = result.get("data", {}).get("taskId")
            tasks.append({
                "task_id": task_id,
                "description": description,
                "number": i
            })
            print(f"  ✅ Task {i}/12: {task_id[:20]}... ({description[:40]}...)")
        else:
            print(f"  ❌ Task {i} failed: {result.get('msg')}")
    else:
        print(f"  ❌ Task {i} API error: {response.status_code}")

    time.sleep(0.5)  # Rate limiting

print(f"\n✅ Submitted {len(tasks)}/12 tasks")

# Step 2: Poll for completion
print("\n⏳ Waiting for generation to complete...")
print("This may take 2-5 minutes per image...")

completed_tasks = []
max_wait = 600  # 10 minutes total
start_time = time.time()

while len(completed_tasks) < len(tasks) and (time.time() - start_time) < max_wait:
    for task in tasks:
        if task["task_id"] in [t["task_id"] for t in completed_tasks]:
            continue  # Skip already completed

        response = requests.get(
            f"{KIE_STATUS_URL}?taskId={task['task_id']}",
            headers={"Authorization": f"Bearer {KIE_API_KEY}"}
        )

        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 200:
                data = result.get("data", {})
                status = data.get("status")

                if status == "completed":
                    output = data.get("output", {})
                    image_url = output.get("images", [{}])[0].get("url") if output.get("images") else None

                    if image_url:
                        task["image_url"] = image_url
                        completed_tasks.append(task)
                        print(f"  ✅ {task['number']}/12 completed: {task['description'][:40]}...")
                elif status == "failed":
                    print(f"  ❌ {task['number']}/12 failed: {data.get('error', 'Unknown error')}")
                    completed_tasks.append(task)  # Mark as done to move on

    if len(completed_tasks) < len(tasks):
        time.sleep(5)  # Poll every 5 seconds

print(f"\n✅ Completed {len(completed_tasks)}/{len(tasks)} generations")

# Step 3: Download images
print("\n📥 Downloading generated images...")
output_dir = Path("outputs/hero-enhanced")
output_dir.mkdir(parents=True, exist_ok=True)

downloaded = []
for task in completed_tasks:
    if "image_url" not in task:
        continue

    image_url = task["image_url"]
    filename = f"food-enhanced-{task['number']:02d}.png"
    output_path = output_dir / filename

    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            downloaded.append({
                "file": filename,
                "path": str(output_path),
                "description": task["description"]
            })
            print(f"  ✅ {filename}")
        else:
            print(f"  ❌ {filename} - Download failed: {response.status_code}")
    except Exception as e:
        print(f"  ❌ {filename} - Error: {e}")

print(f"\n✅ Downloaded {len(downloaded)}/12 images to outputs/hero-enhanced/")

# Step 4: Save metadata
metadata_path = output_dir / "generation-metadata.json"
with open(metadata_path, "w") as f:
    json.dump({
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_images": len(downloaded),
        "aspect_ratio": "16:9",
        "model": "nano-banana-pro",
        "provider": "kie.ai",
        "resolution": "2K",
        "images": downloaded
    }, f, indent=2)

print(f"✅ Saved metadata to {metadata_path}")

print("\n" + "=" * 60)
print("🎉 Generation complete!")
print(f"📁 Images saved to: outputs/hero-enhanced/")
print(f"📊 Total generated: {len(downloaded)}/12")
print("=" * 60)
