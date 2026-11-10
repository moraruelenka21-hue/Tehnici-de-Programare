# Exercițiul 21 — Prima funcție fetch
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
import time

def fetch(url):
    """Returnează obiectul răspuns pentru adresa dată."""
    time.sleep(1)
    return requests.get(url, timeout=TIMEOUT)

response = fetch(BASE_URL)
print("Status:", response.status_code)
