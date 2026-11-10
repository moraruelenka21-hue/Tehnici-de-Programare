# Exercițiul 2 — Două stiluri de import
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from requests import get
import time
time.sleep(1)
print("import requests:", requests.get(BASE_URL, timeout=TIMEOUT).status_code)
time.sleep(1)
print("from requests import get:", get(BASE_URL, timeout=TIMEOUT).status_code)
# requests.get arată originea funcției.
# Importul direct get face apelul mai scurt.
