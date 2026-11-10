# Exercițiul 23 — Parametri cu valori implicite
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from webtools import PacedSession

def fetch(url, timeout=10):
    """Descarcă pagina cu timeout implicit sau explicit."""
    with PacedSession() as session:
        return session.get(url, timeout=timeout)

print("Implicit:", fetch(BASE_URL).status_code)
print("Explicit 3 secunde:", fetch(BASE_URL, timeout=3).status_code)
