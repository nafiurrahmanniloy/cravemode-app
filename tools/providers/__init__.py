"""
Multi-provider abstraction layer for FoodShot AI.
Supports Google AI Studio, Kie AI, and optional providers like Midjourney.
"""

# Provider registry for image generation
IMAGE_PROVIDERS = {
    "nano-banana": {
        "default": "google",
        "providers": ["google", "kie"]
    },
    "nano-banana-pro": {
        "default": "google",
        "providers": ["google", "kie"]
    },
    "midjourney": {
        "default": "midjourney",
        "providers": ["midjourney"]
    }
}

# Provider registry for video generation
VIDEO_PROVIDERS = {
    "veo-3.1": {
        "default": "google",
        "providers": ["google"]
    },
    "kling-3.0": {
        "default": "kie",
        "providers": ["kie"]
    },
    "sora-2-pro": {
        "default": "kie",
        "providers": ["kie"]
    }
}


def get_image_provider(model, provider=None):
    """
    Get the provider for image generation.

    Args:
        model: Model name
        provider: Specific provider to use (optional)

    Returns:
        str: Provider name
    """
    if model not in IMAGE_PROVIDERS:
        raise ValueError(f"Unknown image model: {model}")

    if provider is None:
        return IMAGE_PROVIDERS[model]["default"]

    if provider not in IMAGE_PROVIDERS[model]["providers"]:
        raise ValueError(f"Provider {provider} not available for model {model}")

    return provider


def get_video_provider(model, provider=None):
    """
    Get the provider for video generation.

    Args:
        model: Model name
        provider: Specific provider to use (optional)

    Returns:
        str: Provider name
    """
    if model not in VIDEO_PROVIDERS:
        raise ValueError(f"Unknown video model: {model}")

    if provider is None:
        return VIDEO_PROVIDERS[model]["default"]

    if provider not in VIDEO_PROVIDERS[model]["providers"]:
        raise ValueError(f"Provider {provider} not available for model {model}")

    return provider
