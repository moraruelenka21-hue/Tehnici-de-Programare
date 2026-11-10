# Exercițiul 25 — Docstring și help
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from html import unescape

def get_title(html: str) -> str:
    """Extrage titlul prin find și slicing; returnează șir gol dacă lipsește."""
    lower = html.lower()
    start = lower.find("<title>")
    if start == -1:
        return ""
    start += len("<title>")
    end = lower.find("</title>", start)
    return unescape(html[start:end].strip()) if end != -1 else ""

help(get_title)
print("Exemplu:", get_title("<title>Exemplu web</title>"))
