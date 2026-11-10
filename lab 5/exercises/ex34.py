# Exercițiul 34 — Argumente numite colectate
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

def log(message, **details):
    """Afișează mesajul și detaliile primite ca argumente cu nume."""
    print(" | ".join([str(message)] + [f"{key}={value}" for key, value in details.items()]))

log("verificat", url=BASE_URL, status=200)
# print afișează; return oferă o valoare apelantului.
