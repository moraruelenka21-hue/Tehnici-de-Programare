# Exercițiul 22 — Returnarea codului HTTP
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
from urllib.parse import urljoin

def get_status(url: str) -> int:
    """Returnează codul HTTP al URL-ului."""
    return fetch(url).status_code

for path in ("/", "/robots.txt", "/sitemap.xml"):
    print(path, get_status(urljoin(BASE_URL, path)))
