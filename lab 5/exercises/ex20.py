# Exercițiul 20 — Sesiune cu User Agent personalizat
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import PacedSession
agent = "WebLab-Student"
with PacedSession() as session:
    session.headers.update({"User-Agent": agent})
    response = session.get(ECHO_URL + "/headers", timeout=TIMEOUT)
    response.raise_for_status()
    actual = response.json()["headers"].get("User-Agent")
    print("User-Agent întors:", actual)
    print("Confirmat:", actual == agent)
# Antetele personalizate sunt verificate numai pe httpbin.
# text este atribut; json() este metodă de decodare.
