# Exercițiul 48 — Argumente din linia de comandă
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import argparse
from webtools import fetch, get_title

def main():
    """Preia URL-ul din linia de comandă."""
    parser = argparse.ArgumentParser(description="Exemplu web")
    parser.add_argument("url", nargs="?", default=BASE_URL)
    args = parser.parse_args()
    response = fetch(args.url)
    print("URL primit:", args.url)
    print("Titlul:", get_title(response.text))

if __name__ == "__main__":
    main()
# Rulare: python main.py https://cybercor.org
