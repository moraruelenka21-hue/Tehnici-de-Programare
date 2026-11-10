# Exercițiul 45 — Importul unor nume din modul
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
from webtools import get_title, security_headers
response = fetch(BASE_URL)
print("Titlul:", get_title(response.text))
print("Antete:", security_headers(BASE_URL))
# O funcție locală get_title definită ulterior înlocuiește
# numele importat. webtools.get_title rămâne neambiguă.
