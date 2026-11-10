# Exercițiul 32 — Fișierul robots și directivele Disallow
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from urllib.parse import urljoin
from webtools import fetch

def fetch_robots(base: str):
    """Returnează robots.txt la status 200 sau None când nu poate fi citit."""
    try:
        response = fetch(urljoin(base.rstrip("/") + "/", "/robots.txt"))
        return response.text if response.status_code == 200 else None
    except requests.RequestException:
        return None

def disallowed_paths(robots_text) -> list:
    """Colectează valorile Disallow nevidе, fără comentarii, din toate grupurile."""
    paths = []
    for line in (robots_text or "").splitlines():
        key, sep, value = line.split("#", 1)[0].partition(":")
        if sep and key.strip().lower() == "disallow" and value.strip():
            paths.append(value.strip())
    return paths

robots = fetch_robots(BASE_URL)
print("Disallow:", disallowed_paths(robots))
print("Test None:", disallowed_paths(None))
