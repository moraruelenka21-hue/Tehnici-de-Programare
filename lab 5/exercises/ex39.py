# Exercițiul 39 — Parserul de imagini
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from html.parser import HTMLParser
from webtools import fetch

class ImageFinder(HTMLParser):
    """Colectează atributele src ale imaginilor în ordinea din HTML."""

    def __init__(self):
        """Inițializează parserul și lista imaginilor."""
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        """Este apelată de feed pentru fiecare tag de început."""
        if tag == "img":
            src = dict(attrs).get("src")
            if src:
                self.images.append(src)

test_html = '<img src="/logo.png"><IMG SRC="poza.jpg">' \
    '<img alt="fără src"><img src="https://cdn.example.com/banner.webp" />'
finder = ImageFinder()
finder.feed(test_html)
assert finder.images == ["/logo.png", "poza.jpg", "https://cdn.example.com/banner.webp"]
print("Testul a trecut!", finder.images)
response = fetch(BASE_URL)
finder = ImageFinder()
finder.feed(response.text)
print("Site real:", len(finder.images), finder.images)
print("Verificare <img:", response.text.lower().count("<img"))
# feed() apelează handle_starttag în timpul parsării.
