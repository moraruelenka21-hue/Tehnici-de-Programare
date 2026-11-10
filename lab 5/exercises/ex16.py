# Exercițiul 16 — Verificarea HTTPS
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
response = fetch(BASE_URL)
secure = response.url.startswith("https://")
print("Conexiune securizată" if secure else "Conexiune nesecurizată")
print("URL final:", response.url)
