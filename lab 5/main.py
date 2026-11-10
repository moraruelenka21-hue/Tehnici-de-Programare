"""Programul principal pentru exercițiile 44–50."""
import argparse
import webtools
from webtools import get_title, security_headers, DEFAULT_HEADERS

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

# Ex. 45: o definiție locală get_title ulterioară ar înlocui numele importat.
# Forma webtools.get_title rămâne neambiguă.


def main():
    """Citește URL-ul din CLI și produce rapoartele CSV și JSON."""
    parser = argparse.ArgumentParser(description="Raport web")
    parser.add_argument("url", nargs="?", default=BASE_URL)
    args = parser.parse_args()
    if webtools.urlparse(args.url).scheme not in ("http", "https") or not webtools.urlparse(args.url).hostname:
        parser.error("URL-ul trebuie să fie complet: https://cybercor.org")
    print("Ex. 47 DEFAULT_HEADERS:", DEFAULT_HEADERS)
    try:
        # Ex. 44: import de modul și apel cu nume calificat.
        response = webtools.fetch(args.url)
        print("Ex. 44 titlu:", webtools.get_title(response.text))
        print("Ex. 45 titlu:", get_title(response.text))
        print("Ex. 45 antete:", security_headers(args.url))
    except webtools.requests.RequestException as error:
        print("Pagina nu poate fi citită:", error)
    webtools.save_csv(webtools.check_paths(args.url, ["/", "/robots.txt", "/sitemap.xml"]))
    print("Ex. 49: salvat în report.csv")
    webtools.site_report(args.url)


if __name__ == "__main__":
    main()
