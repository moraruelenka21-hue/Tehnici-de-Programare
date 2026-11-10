# Exercițiul 49 — Raportul CSV
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import csv
from datetime import datetime
from webtools import check_paths, OUTPUT_DIR

def save_csv(results: dict, filename=None):
    """Salvează path, status și checked_at într-un CSV UTF8."""
    filename = filename or OUTPUT_DIR / "report.csv"
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["path", "status", "checked_at"])
        writer.writeheader()
        for path, status in results.items():
            writer.writerow({"path": path, "status": status,
                             "checked_at": datetime.now().isoformat()})

results = check_paths(BASE_URL, ["/", "/robots.txt", "/sitemap.xml"])
save_csv(results)
print((OUTPUT_DIR / "report.csv").read_text(encoding="utf-8"))
