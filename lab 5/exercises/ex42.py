# Exercițiul 42 — Rezolvarea DNS
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import socket

def resolve(hostname: str) -> str:
    """Rezolvă numele domeniului la o adresă IPv4."""
    return socket.gethostbyname(hostname)

print("Adresă IPv4:", resolve("cybercor.org"))
