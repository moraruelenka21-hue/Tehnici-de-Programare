# Exercițiul 29 — Argumente cu nume
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch

def get_header(url: str, name: str, default: str = "lipsește") -> str:
    """Returnează antetul cerut sau valoarea implicită."""
    return fetch(url).headers.get(name, default)

print(get_header(BASE_URL, name="Server"))
