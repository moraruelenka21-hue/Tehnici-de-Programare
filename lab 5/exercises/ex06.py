# Exercițiul 6 — Documentația funcției get
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
import time
help(requests.get)
time.sleep(1)
response = requests.get(BASE_URL, timeout=TIMEOUT)
print("Status:", response.status_code)
# timeout este transmis prin **kwargs.
# Limitează așteptarea de conectare și citire.
