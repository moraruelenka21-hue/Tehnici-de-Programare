# Exercițiul 44 — Crearea modulului webtools
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

# Funcțiile fetch, get_status, get_title și security_headers
# sunt definite în fișierul webtools.py.
import webtools
response = webtools.fetch(BASE_URL)
print("Titlul:", webtools.get_title(response.text))
print("Modul importat:", webtools.__name__)
