"""Teste locale pentru cazurile limită; nu trimit cereri web."""
import unittest
from unittest.mock import patch
import requests
import webtools

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10


class WebToolsTests(unittest.TestCase):
    """Verifică parsarea, clasificarea și tratarea erorilor."""

    def test_title(self):
        """Titlu normal, majuscule, entități și tag absent sau incomplet."""
        self.assertEqual(webtools.get_title("<TITLE> A &amp; B </TITLE>"), "A & B")
        self.assertEqual(webtools.get_title("<p>fără titlu</p>"), "")
        self.assertEqual(webtools.get_title("<title>neterminat"), "")

    def test_robots(self):
        """None și directive fără valoare nu produc căi fictive."""
        self.assertEqual(webtools.disallowed_paths(None), [])
        self.assertEqual(webtools.disallowed_paths("Disallow:\nDisallow: /admin # text\ndisallow: /private"), ["/admin", "/private"])

    def test_links(self):
        """Clasificarea exclude protocoalele fără pagini HTTP."""
        inside, outside = webtools.split_links(["/about", "/about", "https://other.invalid/x", "mailto:a@b.com"], BASE_URL)
        self.assertEqual(inside, [BASE_URL + "/about"])
        self.assertEqual(outside, ["https://other.invalid/x"])

    def test_security(self):
        """Antetele nu disting majusculele; scorul numără numai prezența."""
        presence = webtools.headers_presence({"x-frame-options": "DENY"})
        self.assertEqual(webtools.score_headers(presence), "1/5")

    def test_images(self):
        """Parserul recunoaște majuscule și ignoră imaginile fără src."""
        parser = webtools.ImageFinder()
        parser.feed('<IMG SRC="a.png"><img alt="x"><img src="b.png"/>')
        self.assertEqual(parser.images, ["a.png", "b.png"])

    def test_network_error(self):
        """page_exists returnează False când cererea eșuează."""
        with patch("webtools.fetch", side_effect=requests.ConnectionError("test")):
            self.assertFalse(webtools.page_exists(BASE_URL))

    def test_http_error(self):
        """Demonstrează HTTPError pe un răspuns 404 construit local."""
        response = requests.Response()
        response.status_code = 404
        response.url = BASE_URL + "/this-page-does-not-exist"
        with self.assertRaises(requests.HTTPError):
            response.raise_for_status()


if __name__ == "__main__":
    unittest.main(verbosity=2)
