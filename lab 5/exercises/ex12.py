# Exercițiul 12 — Citirea antetelor cu get
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
response = fetch(BASE_URL)
print("Server:", response.headers.get("Server", "lipsește"))
print("Content-Type:", response.headers.get("Content-Type", "lipsește"))
print("content-type:", response.headers.get("content-type", "lipsește"))
# Numele antetelor nu disting majusculele de minuscule.
