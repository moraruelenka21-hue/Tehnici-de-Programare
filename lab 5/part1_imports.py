"""Exercițiile 1–8: moduri de import și biblioteca standard."""
import requests
import urllib.request
import time
from requests import get
import requests as rq

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10


def main():
    """Execută cele opt exerciții și tratează erorile de rețea."""
    print("Ex. 1 requests:", requests.__version__)
    # requests este extern: pip install requests; urllib este inclus în Python.
    # Ex. 2: requests.get arată originea; from requests import get este mai scurt.
    # Ex. 3: un alias cunoscut scurtează codul; unul arbitrar ascunde semnificația.
    for label, getter in (("Ex. 2 import", requests.get),
                          ("Ex. 2 from", get), ("Ex. 3 alias", rq.get)):
        try:
            time.sleep(1)
            print(label, getter(BASE_URL, timeout=TIMEOUT).status_code)
        except requests.RequestException as error:
            print(label, "eroare:", error)
    try:
        time.sleep(1)
        with urllib.request.urlopen(BASE_URL, timeout=TIMEOUT) as response:
            print("Ex. 4 status:", response.status)
            print(response.read().decode("utf-8", errors="replace")[:200])
    except (OSError, ValueError) as error:
        print("Ex. 4 eroare:", error)
    print("Ex. 5:", dir(requests))
    # get = funcție; Session = clasă; exceptions = modul.
    print("Ex. 6 documentație:")
    help(requests.get)
    # timeout se transmite prin **kwargs; limitează așteptarea de conectare/citire,
    # nu este un termen absolut pentru întreaga descărcare.
    try:
        time.sleep(1)
        start = time.perf_counter()
        response = requests.get(BASE_URL, timeout=TIMEOUT)
        elapsed = time.perf_counter() - start
        print("Ex. 6 status:", response.status_code)
        print("Ex. 7 perf_counter:", elapsed, "elapsed:", response.elapsed.total_seconds())
        # perf_counter include citirea corpului; elapsed se oprește la antete.
    except requests.RequestException as error:
        print("Ex. 6–7 eroare:", error)
    try:
        import bs4
        print("Ex. 8 bs4 disponibil:", bs4.__version__)
    except ImportError:
        print("Instalați modulul cu: pip install beautifulsoup4")
    # Modul = unitate importabilă; pachet = structură de module/subpachete;
    # bibliotecă = colecție de cod care poate cuprinde unul sau mai multe pachete.


if __name__ == "__main__":
    main()
