"""
api_helper.py
Fetches a motivational quote from a free public API.
Demonstrates: requests library, JSON parsing, exception handling.
"""

import requests

QUOTE_API_URL = "https://api.quotable.io/random?tags=inspirational"

def fetch_motivational_quote():
    """
    Hit the Quotable API and return a formatted quote string.
    Falls back gracefully if there's no internet connection.
    """
    try:
        response = requests.get(QUOTE_API_URL, timeout=5)
        response.raise_for_status()  # raises exception for 4xx/5xx

        data = response.json()
        quote = data.get("content", "Keep going!")
        author = data.get("author", "Unknown")
        
        return f'"{quote}"\n                  — {author}'

    except requests.exceptions.ConnectionError:
        return '"Stay focused and never give up."\n                  — Hardik Sharma'
    
    except requests.exceptions.Timeout:
        return '"Great things take time."\n                  — Hardik Sharma'
    
    except requests.exceptions.RequestException:
        # Catch-all for any other request issues
        return '"Keep pushing forward."\n                  — Hardik Sharma'