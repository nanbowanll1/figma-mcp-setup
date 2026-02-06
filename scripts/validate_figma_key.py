#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate Figma API Key by calling the Figma API.
Usage: python validate_figma_key.py <API_KEY>
"""

import sys
import urllib.request
import urllib.error
import json


def validate_figma_api_key(api_key: str) -> dict:
    """
    Validate a Figma API key by calling GET /v1/me endpoint.

    Args:
        api_key: The Figma API key to validate

    Returns:
        dict with 'valid' (bool), 'message' (str), and optionally 'user' info
    """
    if not api_key or not api_key.strip():
        return {
            "valid": False,
            "message": "API Key is empty"
        }

    api_key = api_key.strip()
    url = "https://api.figma.com/v1/me"

    request = urllib.request.Request(
        url,
        headers={
            "X-Figma-Token": api_key,
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            return {
                "valid": True,
                "message": "API Key is valid",
                "user": {
                    "id": data.get("id"),
                    "email": data.get("email"),
                    "handle": data.get("handle")
                }
            }
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return {
                "valid": False,
                "message": "API Key is invalid or expired (403 Forbidden)"
            }
        elif e.code == 401:
            return {
                "valid": False,
                "message": "API Key is unauthorized (401 Unauthorized)"
            }
        else:
            return {
                "valid": False,
                "message": f"HTTP Error: {e.code} {e.reason}"
            }
    except urllib.error.URLError as e:
        return {
            "valid": False,
            "message": f"Network error: {e.reason}"
        }
    except Exception as e:
        return {
            "valid": False,
            "message": f"Unexpected error: {str(e)}"
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_figma_key.py <API_KEY>")
        print("Example: python validate_figma_key.py figd_xxxxx")
        sys.exit(1)

    api_key = sys.argv[1]
    result = validate_figma_api_key(api_key)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
