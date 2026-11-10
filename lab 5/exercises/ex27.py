# Exercițiul 27 — Funcția page_exists
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from webtools import get_status

def page_exists(url: str) -> bool:
    """Întoarce True pentru un răspuns 2xx și False la erori sau alte coduri."""
    try:
        return 200 <= get_status(url) < 300
    except requests.RequestException:
        return False

print("Pagina principală:", page_exists(BASE_URL))
print("Domeniu invalid:", page_exists("https://this-domain-does-not-exist.invalid"))
