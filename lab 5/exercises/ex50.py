# Exercițiul 50 — Proiectul final site_report
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import site_report, OUTPUT_DIR
import json
# Implementarea completă se află în webtools.py.
# Funcția colectează:
#   status și URL final, titlu, IP, redirecturi HTTP,
#   scor antete, expirare TLS, href interne/externe,
#   directive Disallow din robots.txt.
report = site_report(BASE_URL)
with (OUTPUT_DIR / "report.json").open(encoding="utf-8") as file:
    saved = json.load(file)
print("Fișier JSON valid:", saved == report)
print("Raport salvat:", OUTPUT_DIR / "report.json")
