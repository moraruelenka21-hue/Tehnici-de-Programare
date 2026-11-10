# Exercițiul 7 — Cronometrarea unei cereri
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
import time
time.sleep(1)
start = time.perf_counter()
response = requests.get(BASE_URL, timeout=TIMEOUT)
duration = time.perf_counter() - start
print("Durata completă:", round(duration, 6))
print("Până la antete:", response.elapsed.total_seconds())
# perf_counter include și citirea corpului răspunsului.
# elapsed se oprește după primirea antetelor.
