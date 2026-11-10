# Exercițiul 38 — Legături interne și externe
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from html import unescape
from urllib.parse import urljoin, urlparse
from webtools import fetch, extract_links

def split_links(links: list, domain: str) -> tuple:
    """Separă URL-urile HTTP/HTTPS interne și externe după domeniu."""
    base = domain if "://" in domain else "https://" + domain
    hostname = urlparse(base).hostname
    internal, external = [], []
    for link in links:
        absolute = urljoin(base.rstrip("/") + "/", unescape(link))
        parsed = urlparse(absolute)
        if parsed.scheme not in ("http", "https"):
            continue  # mailto:, tel: și javascript: nu sunt pagini web.
        target = internal if parsed.hostname == hostname else external
        if absolute not in target:
            target.append(absolute)
    return internal, external

inside, outside = split_links(extract_links(fetch(BASE_URL).text), BASE_URL)
print("Interne:", len(inside), inside)
print("Externe:", len(outside), outside)
