# Exercițiul 9 — Atributele răspunsului
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
response = fetch(BASE_URL)
print("status_code:", response.status_code)  # atribut
print("ok:", response.ok)  # atribut
print("url:", response.url)  # atribut
print("encoding:", response.encoding)  # atribut
