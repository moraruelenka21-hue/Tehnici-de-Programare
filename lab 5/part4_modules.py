"""Exercițiile 35–43: module standard și parser HTML."""
import json
from urllib.parse import urlparse, urljoin
from webtools import (fetch, extract_links, split_links, ImageFinder,
                      page_fingerprint, resolve, cert_days_left, OUTPUT_DIR)
from part3_functions import demonstrate

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10


def parse_url(url):
    """Ex. 35: afișează cele cinci componente ale URL-ului."""
    parsed = urlparse(url)
    for name in ("scheme", "netloc", "path", "query", "fragment"):
        print(name, getattr(parsed, name))


def join_urls(base, links):
    """Ex. 36: compune URL-uri fără a accesa resursele respective."""
    return [urljoin(base, link) for link in links]


def test_images():
    """Ex. 39: verifică exact parserul pe HTML cunoscut înaintea site-ului real."""
    html = '''<html><body>
    <img src="/logo.png" alt="Logo"><IMG SRC="poza.jpg">
    <img alt="imagine fără src">
    <img src="https://cdn.example.com/banner.webp" />
    <a href="/despre">Aceasta nu este o imagine</a></body></html>'''
    finder = ImageFinder()
    finder.feed(html)
    print(finder.images)
    assert finder.images == ["/logo.png", "poza.jpg", "https://cdn.example.com/banner.webp"]
    print("Testul a trecut!")


def save_headers(headers):
    """Ex. 41: salvează și recitește antetele în JSON."""
    path = OUTPUT_DIR / "headers.json"
    with path.open("w", encoding="utf-8") as file:
        json.dump(dict(headers), file, indent=2)
    with path.open(encoding="utf-8") as file:
        restored = json.load(file)
    print("Ex. 41:", next((v for k, v in restored.items() if k.lower() == "content-type"), "lipsește"))


def main():
    """Execută funcțiile tuturor exercițiilor din Partea 4."""
    parse_url("https://cybercor.org/path?x=1#top")
    print("Ex. 36:", join_urls(BASE_URL, ["/about", "contact.html", "../index.html"]))
    test_images()
    response = demonstrate("Pagina reală", fetch, BASE_URL)
    if response is not None:
        links = extract_links(response.text)
        print("Ex. 37 legături unice:", len(links), links)
        internal, external = split_links(links, BASE_URL)
        print("Ex. 38 interne:", len(internal), "externe:", len(external))
        finder = ImageFinder()
        finder.feed(response.text)
        print("Ex. 39 imagini:", len(finder.images), finder.images)
        print("Verificare count <img:", response.text.lower().count("<img"))
        save_headers(response.headers)
    first = demonstrate("Ex. 40 amprenta 1", page_fingerprint, BASE_URL)
    second = demonstrate("Ex. 40 amprenta 2", page_fingerprint, BASE_URL)
    print("Amprente egale:", first == second if first and second else "nu se poate compara")
    # Amprente diferite dacă se schimbă orice octet, inclusiv conținut dinamic.
    try:
        print("Ex. 42 IP:", resolve("cybercor.org"))
    except OSError as error:
        print("Ex. 42 eroare:", error)
    try:
        print("Ex. 43 zile certificat:", cert_days_left("cybercor.org"))
    except (OSError, ValueError, KeyError) as error:
        print("Ex. 43 eroare:", error)
    # HTMLParser.feed apelează handle_starttag în timpul analizei HTML.


if __name__ == "__main__":
    main()
