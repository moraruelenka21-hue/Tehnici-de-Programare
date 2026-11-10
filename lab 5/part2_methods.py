"""Exercițiile 9–20: metode și atribute."""
import requests
from webtools import fetch, get_title, PacedSession

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10


def main():
    """Analizează răspunsul și demonstrează HEAD, redirecturi și sesiuni."""
    try:
        response = fetch(BASE_URL)
        print("Ex. 9 status:", response.status_code)  # atribut
        print("ok:", response.ok)  # atribut; True și la unele coduri 3xx
        print("url:", response.url)  # atribut
        print("encoding:", response.encoding)  # atribut
        response.raise_for_status()  # Ex. 10, metodă
        for name, value in response.headers.items():  # Ex. 11
            print(f"{name}: {value}")
        print("Ex. 12 Server:", response.headers.get("Server", "lipsește"))
        print("Content-Type:", response.headers.get("Content-Type", "lipsește"))
        print("content-type:", response.headers.get("content-type", "lipsește"))
        # Antetele Requests nu disting majusculele de minuscule.
        print("Ex. 13 cyber:", response.text.lower().count("cyber"))
        # lower returnează str, care are la rândul lui metoda count.
        print("Ex. 14 titlu:", get_title(response.text))
        lines = response.text.splitlines()
        print("Ex. 15 linii:", len(lines), "maxim:", len(max(lines, key=len, default="")))
        print("Ex. 16:", "Conexiune securizată" if response.url.startswith("https://") else "Conexiune nesecurizată")
        print("Ex. 19 cookie-uri:")
        if not response.cookies:
            print("Niciun cookie setat")
        for cookie in response.cookies:
            print(cookie.name, cookie.secure)
    except requests.RequestException as error:
        print("Ex. 9–16,19 eroare:", error)
    try:
        response = fetch(BASE_URL + "/this-page-does-not-exist")
        response.raise_for_status()
        print("Ex. 10 calea inexistentă a răspuns fără eroare HTTP:", response.status_code)
    except requests.HTTPError as error:
        print("Ex. 10 pagina nu este disponibilă:", error.response.status_code)
    except requests.RequestException as error:
        print("Ex. 10 eroare de rețea:", error)
    try:
        response = fetch("http://cybercor.org")
        print("Ex. 17:")
        for hop in response.history:
            print(hop.status_code, hop.url)
        print("Final:", response.status_code, response.url)
    except requests.RequestException as error:
        print("Ex. 17 eroare:", error)
    try:
        with PacedSession() as session:
            head = session.head(BASE_URL, timeout=TIMEOUT)
            get_response = session.get(BASE_URL, timeout=TIMEOUT)
        print("Ex. 18 HEAD:", len(head.content), "GET:", len(get_response.content))
        # HEAD transmite antete fără corp; GET transmite și corpul resursei.
    except requests.RequestException as error:
        print("Ex. 18 eroare:", error)
    try:
        with PacedSession() as session:
            agent = "WebLab-Student"
            session.headers.update({"User-Agent": agent})
            response = session.get(ECHO_URL + "/headers", timeout=TIMEOUT)
            response.raise_for_status()
            actual = response.json()["headers"].get("User-Agent")
            print("Ex. 20 User-Agent:", actual, "confirmat:", actual == agent)
    except (requests.RequestException, ValueError, KeyError) as error:
        print("Ex. 20 eroare:", error)
    # text este un atribut calculat; json() este o metodă care decodează JSON.


if __name__ == "__main__":
    main()
