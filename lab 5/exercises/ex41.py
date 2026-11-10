# Exercițiul 41 — Salvarea și încărcarea JSON
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import json
from pathlib import Path
from webtools import fetch, OUTPUT_DIR

def save_headers(headers):
    """Salvează antetele și le citește înapoi din JSON."""
    path = OUTPUT_DIR / "headers.json"
    with path.open("w", encoding="utf-8") as file:
        json.dump(dict(headers), file, indent=2)
    with path.open(encoding="utf-8") as file:
        loaded = json.load(file)
    print(loaded.get("Content-Type", loaded.get("content-type")))

save_headers(fetch(BASE_URL).headers)
