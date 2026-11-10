# Exercițiul 28 — Verificarea unei liste de căi
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from urllib.parse import urljoin
from webtools import get_status

def check_paths(base: str, paths: list) -> dict:
    """Verifică fiecare cale; None indică o eroare de rețea, nu un cod HTTP."""
    results = {}
    for path in paths:
        try:
            results[path] = get_status(urljoin(base.rstrip("/") + "/", path))
        except requests.RequestException:
            results[path] = None
    return results

print(check_paths(BASE_URL, ["/", "/robots.txt", "/sitemap.xml"]))
