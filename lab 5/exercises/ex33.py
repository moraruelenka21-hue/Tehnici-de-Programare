# Exercițiul 33 — Număr variabil de argumente
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from webtools import fetch

def response_times(*urls) -> dict:
    """Returnează timpii Requests elapsed în secunde; None la eroare."""
    results = {}
    for url in urls:
        try:
            results[url] = fetch(url).elapsed.total_seconds()
        except requests.RequestException:
            results[url] = None
    return results

print(response_times(BASE_URL, BASE_URL + "/robots.txt"))
