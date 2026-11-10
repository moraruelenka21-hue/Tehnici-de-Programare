# Exercițiul 37 — Extragerea legăturilor fără duplicate
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import re
from webtools import fetch

def extract_links(html: str) -> list:
    """Extrage href cu ghilimele duble și elimină duplicatele în ordine."""
    return list(dict.fromkeys(re.findall(r'href="([^"]+)"', html)))

links = extract_links(fetch(BASE_URL).text)
print("Număr:", len(links))
print(links)
