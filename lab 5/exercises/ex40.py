# Exercițiul 40 — Amprenta SHA256 a paginii
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import hashlib
from webtools import fetch

def page_fingerprint(url: str) -> str:
    """Returnează SHA256 al octeților paginii."""
    return hashlib.sha256(fetch(url).content).hexdigest()

first = page_fingerprint(BASE_URL)
second = page_fingerprint(BASE_URL)
print(first)
print(second)
print("Egale:", first == second)
# Orice octet modificat produce o altă amprentă.
