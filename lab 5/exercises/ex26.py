# Exercițiul 26 — Adnotări de tip
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from webtools import fetch

def get_status(url: str) -> int:
    """Returnează codul HTTP al URL-ului."""
    return fetch(url).status_code

try:
    print(get_status(123))
except requests.RequestException as error:
    print(type(error).__name__, str(error))
# Type hints nu validează automat valorile la execuție.
# Requests respinge 123 ca URL invalid.
