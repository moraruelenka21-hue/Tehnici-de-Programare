# Exercițiul 11 — Afișarea tuturor antetelor
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
response = fetch(BASE_URL)
for name, value in response.headers.items():
    print(f"{name}: {value}")
