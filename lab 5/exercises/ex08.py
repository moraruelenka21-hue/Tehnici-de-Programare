# Exercițiul 8 — Tratarea unui import absent
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

try:
    import bs4
    print("BeautifulSoup disponibil:", bs4.__version__)
except ImportError:
    print("Instalați modulul cu: pip install beautifulsoup4")
# Modul: o unitate importabilă.
# Pachet: organizează module și subpachete.
# Bibliotecă: o colecție de cod reutilizabil.
