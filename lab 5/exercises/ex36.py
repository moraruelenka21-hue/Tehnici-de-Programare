# Exercițiul 36 — Compunerea URL-urilor
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from urllib.parse import urljoin

def join_urls(base, links):
    """Transformă legăturile relative în URL-uri complete."""
    return [urljoin(base, link) for link in links]

for url in join_urls(BASE_URL, ["/about", "contact.html", "../index.html"]):
    print(url)
# URL-urile rezultate sunt afișate, fără cereri către aceste căi.
