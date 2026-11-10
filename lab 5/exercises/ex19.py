# Exercițiul 19 — Cookie-urile răspunsului
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
response = fetch(BASE_URL)
if not response.cookies:
    print("Niciun cookie setat")
for cookie in response.cookies:
    print("Nume:", cookie.name, "Secure:", cookie.secure)
