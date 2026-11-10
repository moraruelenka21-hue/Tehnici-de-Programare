# Exercițiul 43 — Zile până la expirarea certificatului
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import socket, ssl, time
from datetime import datetime, timezone

def cert_days_left(hostname: str) -> int:
    """Verifică TLS și calculează zilele întregi până la expirarea certificatului."""
    time.sleep(1)
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure:
            expires = ssl.cert_time_to_seconds(secure.getpeercert()["notAfter"])
    return int((expires - datetime.now(timezone.utc).timestamp()) // 86400)

print("Zile rămase:", cert_days_left("cybercor.org"))
