"""Bonus: extragerea titlului și legăturilor cu BeautifulSoup."""
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10
from bs4 import BeautifulSoup
from webtools import fetch, get_title, extract_links
import requests


def get_title_bs4(html):
    """Extrage titlul, inclusiv când tag-ul are atribute."""
    title = BeautifulSoup(html, "html.parser").title
    return title.get_text(strip=True) if title else ""


def extract_links_bs4(html):
    """Extrage href indiferent de tipul ghilimelelor și elimină duplicatele."""
    soup = BeautifulSoup(html, "html.parser")
    return list(dict.fromkeys(tag["href"] for tag in soup.find_all(href=True)))


def main():
    """Compară metodele de bază cu parserul BeautifulSoup."""
    sample = '<title class="x">Exemplu web</title><a href=\'/about\'>Despre</a>'
    print("HTML cunoscut:", get_title(sample), get_title_bs4(sample))
    print("Legături:", extract_links(sample), extract_links_bs4(sample))
    try:
        response = fetch(BASE_URL)
        print("Titlu find / bs4:", get_title(response.text), get_title_bs4(response.text))
        print("Legături regex / bs4:", len(extract_links(response.text)), len(extract_links_bs4(response.text)))
    except requests.RequestException as error:
        print("Eroare:", error)
    # BeautifulSoup acceptă atribute și ghilimele simple; regex-ul cerut este
    # limitat la href cu ghilimele duble. În ambele cazuri avem funcții scurte.


if __name__ == "__main__":
    main()
