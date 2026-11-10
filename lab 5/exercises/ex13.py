# Exercițiul 13 — Înlănțuirea metodelor de șir
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
response = fetch(BASE_URL)
count = response.text.lower().count("cyber")
print("Apariții cyber:", count)
# lower() întoarce un str; acesta are metoda count().
