# Exercițiul 18 — Comparația HEAD cu GET
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import PacedSession
with PacedSession() as session:
    head = session.head(BASE_URL, timeout=TIMEOUT)
    response = session.get(BASE_URL, timeout=TIMEOUT)
print("HEAD corp:", len(head.content), "octeți")
print("GET corp:", len(response.content), "octeți")
# HEAD returnează antete fără corpul resursei.
# GET transmite și corpul paginii.
