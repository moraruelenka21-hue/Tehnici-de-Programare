import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login."""
    if not host.startswith(("http://", "https://")):
        host = "https://" + host

    return host.rstrip("/") + "/" + path.lstrip("/")


def is_https(url):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    return url.lower().startswith("https://")


def show_response(url):
    """Trimite un GET la url și afișează statusul și Content-Type."""
    try:
        response = requests.get(url, timeout=3)
        print(f"Status: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'indisponibil')}")
    except requests.RequestException as error:
        print(f"Eroare la accesarea site-ului: {error}")


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    try:
        response = requests.get(url, timeout=3)
        return {
            "status": response.status_code,
            "content_type": response.headers.get("Content-Type", ""),
            "length": len(response.content),
            "server": response.headers.get("Server", ""),
        }
    except requests.RequestException:
        return {
            "status": None,
            "content_type": "",
            "length": 0,
            "server": "",
        }


def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
    working = 0
    failed = 0

    for url in SITES:
        result = check_site(url)

        if result["status"] is not None and result["status"] < 400:
            working += 1
            print(f"{url} - OK ({result['status']})")
        else:
            failed += 1
            print(f"{url} - Eroare ({result['status']})")

    print(f"\nSite-uri functionale: {working}")
    print(f"Site-uri cu erori: {failed}")


def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
    try:
        response = requests.get(url, timeout=3)
        present = [
            header
            for header in SECURITY_HEADERS
            if header in response.headers
        ]
    except requests.RequestException as error:
        print(f"Eroare la verificarea antetelor: {error}")
        present = []

    missing = [
        header
        for header in SECURITY_HEADERS
        if header not in present
    ]
    score = round(len(present) / len(SECURITY_HEADERS) * 100)

    return {
        "present": present,
        "missing": missing,
        "score": score,
    }


def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
    status = None
    attempts_made = 0

    for attempt in range(attempts):
        attempts_made += 1

        try:
            response = requests.get(url, timeout=3)
            status = response.status_code

            if status < 400:
                break
        except requests.RequestException as error:
            status = None
            print(f"Eroare la incercarea {attempts_made}: {error}")

    return {
        "status": status,
        "attempts": attempts_made,
    }
