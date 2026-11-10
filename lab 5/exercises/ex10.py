# Exercițiul 10 — Tratarea erorilor HTTP
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import requests
from webtools import fetch
for path in ("/", "/this-page-does-not-exist"):
    try:
        response = fetch(BASE_URL + path)
        response.raise_for_status()
        print(path, "fără eroare HTTP:", response.status_code)
    except requests.HTTPError as error:
        print("Pagina nu este disponibilă:", error.response.status_code)
# Site-ul poate răspunde 200 și pentru calea de test.
# HTTPError la 404 este verificat și printr-un test local.
