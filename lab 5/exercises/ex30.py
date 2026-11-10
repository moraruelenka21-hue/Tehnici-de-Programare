# Exercițiul 30 — Antete de securitate
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
SECURITY_HEADERS = (
    "Strict-Transport-Security", "Content-Security-Policy",
    "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy",
)

def security_headers(url):
    """Returnează prezența celor cinci antete, fără alte evaluări."""
    headers = fetch(url).headers
    return {name: name in headers for name in SECURITY_HEADERS}

for name, present in security_headers(BASE_URL).items():
    print(name, present)
