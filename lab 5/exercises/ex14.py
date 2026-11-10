# Exercițiul 14 — Extragerea titlului cu find
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import fetch
html = fetch(BASE_URL).text
start = html.lower().find("<title>")
if start != -1:
    start += len("<title>")
    end = html.lower().find("</title>", start)
    title = html[start:end].strip() if end != -1 else ""
else:
    title = ""
print("Titlul:", title)
