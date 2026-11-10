# Exercițiul 35 — Descompunerea URL-ului
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from urllib.parse import urlparse

def parse_url(url):
    """Afișează cele cinci componente cerute."""
    parsed = urlparse(url)
    for name in ("scheme", "netloc", "path", "query", "fragment"):
        print(name, getattr(parsed, name))

parse_url("https://cybercor.org/path?x=1#top")
