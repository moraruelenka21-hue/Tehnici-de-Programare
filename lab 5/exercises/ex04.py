# Exercițiul 4 — Descărcare cu biblioteca standard
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import urllib.request
import time
time.sleep(1)
try:
    with urllib.request.urlopen(BASE_URL, timeout=TIMEOUT) as response:
        print("Status:", response.status)
        html = response.read().decode("utf-8", errors="replace")
        print(html[:200])
except OSError as error:
    print("Accesul prin urllib a eșuat:", error)
# read() întoarce bytes; decode() produce un șir str.
