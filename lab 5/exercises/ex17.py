# Exercițiul 17 — Lanțul de redirecționări
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
response = fetch("http://cybercor.org")
for hop in response.history:
    print("Redirecționare:", hop.status_code, hop.url)
print("URL final:", response.url)
print("Status final:", response.status_code)
