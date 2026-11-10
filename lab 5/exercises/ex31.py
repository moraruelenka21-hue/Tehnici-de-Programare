# Exercițiul 31 — Funcții care apelează funcții
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import security_headers

def score_headers(results: dict) -> str:
    """Returnează raportul dintre numărul antetelor prezente și total."""
    return f"{sum(bool(value) for value in results.values())}/{len(results)}"

print("Scor:", score_headers(security_headers(BASE_URL)))
