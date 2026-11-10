# Exercițiul 15 — Numărarea liniilor HTML
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
lines = fetch(BASE_URL).text.splitlines()
longest = max(lines, key=len, default="")
print("Număr de linii:", len(lines))
print("Lungimea maximă:", len(longest))
