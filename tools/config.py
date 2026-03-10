"""
Configuration loader for FoodShot AI.
Loads API keys from .claude/.env and provides centralized constants.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .claude/.env
PROJECT_ROOT = Path(__file__).parent.parent
ENV_PATH = PROJECT_ROOT / ".claude" / ".env"
load_dotenv(ENV_PATH)

# --- API Keys ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
KIE_API_KEY = os.getenv("KIE_API_KEY")
CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")
CLICKUP_WORKSPACE_ID = os.getenv("CLICKUP_WORKSPACE_ID")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
N8N_API_KEY = os.getenv("N8N_API_KEY")
N8N_API_URL = os.getenv("N8N_API_URL", "http://localhost:5678/api/v1")
FIGMA_API_KEY = os.getenv("FIGMA_API_KEY")
MIDJOURNEY_API_KEY = os.getenv("MIDJOURNEY_API_KEY")
REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")

# --- Kie AI Endpoints ---
KIE_FILE_UPLOAD_URL = "https://kieai.redpandaai.co/api/file-stream-upload"
KIE_CREATE_URL = "https://api.kie.ai/api/v1/jobs/createTask"
KIE_STATUS_URL = "https://api.kie.ai/api/v1/jobs/recordInfo"

# --- ClickUp ---
CLICKUP_API_URL = "https://api.clickup.com/api/v2"

# --- Cost Constants (per unit) ---
COSTS = {
    # Image models (per image)
    ("nano-banana", "google"): 0.04,
    ("nano-banana", "kie"): 0.09,
    ("nano-banana-pro", "google"): 0.13,
    ("nano-banana-pro", "kie"): 0.09,
    ("midjourney", "midjourney"): 0.04,  # Approximate
    # Video models (per video)
    ("veo-3.1", "google"): 0.50,
    ("kling-3.0", "kie"): 0.30,
    ("sora-2-pro", "kie"): 0.30,
}

# --- Default Models ---
DEFAULT_IMAGE_MODEL = "nano-banana-pro"
DEFAULT_VIDEO_MODEL = "kling-3.0"

# --- Directories ---
INPUTS_DIR = PROJECT_ROOT / "references" / "inputs"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
TEMPLATES_DIR = PROJECT_ROOT / "references" / "templates"

# Ensure directories exist
INPUTS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

# --- Image Generation Models ---
IMAGE_MODELS = {
    "nano-banana": "nano-banana",
    "nano-banana-pro": "nano-banana-pro",
    "midjourney": "midjourney",  # Optional
}

# --- Video Generation Models ---
VIDEO_MODELS = {
    "kling-3.0": "kling-3.0/video",
    "veo-3.1": "veo-3.1-generate-preview",
    "sora-2-pro": "sora-2-pro-image-to-video",
}

# --- FoodShot Business Constants ---
PACKAGES = {
    "basic": {
        "name": "Basic",
        "price": 297,
        "photos": 20,
        "videos": 0,
        "billing": "monthly"
    },
    "pro": {
        "name": "Pro",
        "price": 497,
        "photos": 50,
        "videos": 5,
        "billing": "monthly"
    },
    "premium": {
        "name": "Premium",
        "price": 997,
        "photos": 100,
        "videos": 10,
        "billing": "monthly"
    },
    "pack-20": {
        "name": "20 Photo Pack",
        "price": 497,
        "photos": 20,
        "videos": 0,
        "billing": "one-time"
    },
    "pack-50": {
        "name": "50 Photo Pack",
        "price": 997,
        "photos": 50,
        "videos": 0,
        "billing": "one-time"
    },
    "pack-100": {
        "name": "Premium Pack",
        "price": 1497,
        "photos": 100,
        "videos": 10,
        "billing": "one-time"
    }
}


def get_cost(model, provider=None):
    """
    Get the cost per generation for a model+provider combination.

    Args:
        model: Model name (e.g., "nano-banana-pro", "veo-3.1")
        provider: Provider name (e.g., "google", "kie"). If None, uses default.

    Returns:
        float: Cost per unit
    """
    if provider is None:
        # Import here to avoid circular imports
        from .providers import IMAGE_PROVIDERS, VIDEO_PROVIDERS
        if model in IMAGE_PROVIDERS:
            provider = IMAGE_PROVIDERS[model]["default"]
        elif model in VIDEO_PROVIDERS:
            provider = VIDEO_PROVIDERS[model]["default"]
        else:
            return 0.0
    return COSTS.get((model, provider), 0.0)


def check_credentials():
    """Verify required API keys are set. Returns list of missing keys."""
    required = {
        "CLICKUP_API_KEY": CLICKUP_API_KEY,
        "CLICKUP_WORKSPACE_ID": CLICKUP_WORKSPACE_ID,
        "N8N_WEBHOOK_URL": N8N_WEBHOOK_URL,
    }
    missing = [name for name, value in required.items() if not value]

    # At least one generation provider must be configured
    if not KIE_API_KEY and not GOOGLE_API_KEY:
        missing.append("KIE_API_KEY or GOOGLE_API_KEY (at least one required)")

    if missing:
        print("❌ Missing API keys:")
        for key in missing:
            print(f"  - {key}")
        print(f"\n📝 Add them to: {ENV_PATH}")
    else:
        print("✅ All required credentials configured!")

    return missing


def get_package_info(package_key):
    """Get package details by key."""
    return PACKAGES.get(package_key.lower())


def calculate_profit_margin(package_key, photos_generated, videos_generated):
    """
    Calculate profit margin for a client package.

    Args:
        package_key: Package identifier (e.g., "pro", "pack-50")
        photos_generated: Number of photos generated
        videos_generated: Number of videos generated

    Returns:
        dict: Revenue, cost, profit, margin percentage
    """
    package = get_package_info(package_key)
    if not package:
        return None

    revenue = package["price"]
    photo_cost = photos_generated * get_cost(DEFAULT_IMAGE_MODEL)
    video_cost = videos_generated * get_cost(DEFAULT_VIDEO_MODEL)
    total_cost = photo_cost + video_cost
    profit = revenue - total_cost
    margin = (profit / revenue) * 100 if revenue > 0 else 0

    return {
        "revenue": revenue,
        "cost": total_cost,
        "profit": profit,
        "margin": f"{margin:.1f}%",
        "breakdown": {
            "photo_cost": photo_cost,
            "video_cost": video_cost
        }
    }
