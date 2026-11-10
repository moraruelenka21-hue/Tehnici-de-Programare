# Exercițiul 3 — Alias pentru modul
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests as rq
import time
time.sleep(1)
response = rq.get(BASE_URL, timeout=TIMEOUT)
print("Cod HTTP:", response.status_code)
# Un alias cunoscut scurtează numele folosit repetat.
# Un alias arbitrar poate face codul mai greu de urmărit.
