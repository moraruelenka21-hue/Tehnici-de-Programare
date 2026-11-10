"""Funcții reutilizabile pentru exercițiile 21–50."""
import csv
import hashlib
import json
import re
import socket
import ssl
import time
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10
DEFAULT_HEADERS = {"User-Agent": "WebLab-Student"}
SECURITY_HEADERS = (
    "Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options",
    "X-Content-Type-Options", "Referrer-Policy",
)
OUTPUT_DIR = Path(__file__).resolve().parent


class PacedSession(requests.Session):
    """Pune o pauză de o secundă înaintea fiecărei cereri, inclusiv redirecturi."""

    def send(self, request, **kwargs):
        """Trimite cererea după pauză, cu timeout și cel mult 10 redirecționări."""
        time.sleep(1)
        kwargs.setdefault("timeout", TIMEOUT)
        return super().send(request, **kwargs)


def fetch(url: str, timeout: float = 10) -> requests.Response:
    """Descarcă URL-ul și returnează răspunsul; erorile sunt tratate de apelant."""
    with PacedSession() as session:
        session.max_redirects = 10
        # Ex. 47: constanta este folosită pe httpbin, unde verificăm antete
        # personalizate. Pe cybercor păstrăm antetele standard, conform regulilor.
        if urlparse(str(url)).hostname == "httpbin.org":
            session.headers.update(DEFAULT_HEADERS)
        return session.get(url, timeout=timeout)


def get_status(url: str) -> int:
    """Returnează codul HTTP al URL-ului."""
    return fetch(url).status_code


def get_title(html: str) -> str:
    """Extrage titlul prin find și slicing; returnează șir gol dacă lipsește."""
    lower = html.lower()
    start = lower.find("<title>")
    if start == -1:
        return ""
    start += len("<title>")
    end = lower.find("</title>", start)
    return unescape(html[start:end].strip()) if end != -1 else ""


def page_exists(url: str) -> bool:
    """Întoarce True pentru un răspuns 2xx și False la erori sau alte coduri."""
    try:
        return 200 <= get_status(url) < 300
    except requests.RequestException:
        return False


def check_paths(base: str, paths: list) -> dict:
    """Verifică fiecare cale; None indică o eroare de rețea, nu un cod HTTP."""
    results = {}
    for path in paths:
        try:
            results[path] = get_status(urljoin(base.rstrip("/") + "/", path))
        except requests.RequestException:
            results[path] = None
    return results


def get_header(url: str, name: str, default: str = "lipsește") -> str:
    """Returnează antetul cerut sau valoarea implicită."""
    return fetch(url).headers.get(name, default)


def security_headers(url: str) -> dict:
    """Verifică prezența celor cinci antete; nu evaluează politicile lor."""
    return headers_presence(fetch(url).headers)


def headers_presence(headers) -> dict:
    """Analizează antetele unui răspuns deja descărcat, fără cereri suplimentare."""
    names = {name.lower() for name in headers}
    return {name: name.lower() in names for name in SECURITY_HEADERS}


def score_headers(results: dict) -> str:
    """Returnează raportul dintre numărul antetelor prezente și total."""
    return f"{sum(bool(value) for value in results.values())}/{len(results)}"


def fetch_robots(base: str):
    """Returnează robots.txt la status 200 sau None când nu poate fi citit."""
    try:
        response = fetch(urljoin(base.rstrip("/") + "/", "/robots.txt"))
        return response.text if response.status_code == 200 else None
    except requests.RequestException:
        return None


def disallowed_paths(robots_text) -> list:
    """Colectează valorile Disallow nevidе, fără comentarii, din toate grupurile."""
    paths = []
    for line in (robots_text or "").splitlines():
        key, sep, value = line.split("#", 1)[0].partition(":")
        if sep and key.strip().lower() == "disallow" and value.strip():
            paths.append(value.strip())
    return paths


def response_times(*urls) -> dict:
    """Returnează timpii Requests elapsed în secunde; None la eroare."""
    results = {}
    for url in urls:
        try:
            results[url] = fetch(url).elapsed.total_seconds()
        except requests.RequestException:
            results[url] = None
    return results


def log(message, **details):
    """Afișează mesajul și detaliile primite ca argumente cu nume."""
    print(" | ".join([str(message)] + [f"{key}={value}" for key, value in details.items()]))


def extract_links(html: str) -> list:
    """Extrage href cu ghilimele duble și elimină duplicatele în ordine."""
    return list(dict.fromkeys(re.findall(r'href="([^"]+)"', html)))


def split_links(links: list, domain: str) -> tuple:
    """Separă URL-urile HTTP/HTTPS interne și externe după domeniu."""
    base = domain if "://" in domain else "https://" + domain
    hostname = urlparse(base).hostname
    internal, external = [], []
    for link in links:
        absolute = urljoin(base.rstrip("/") + "/", unescape(link))
        parsed = urlparse(absolute)
        if parsed.scheme not in ("http", "https"):
            continue  # mailto:, tel: și javascript: nu sunt pagini web.
        target = internal if parsed.hostname == hostname else external
        if absolute not in target:
            target.append(absolute)
    return internal, external


class ImageFinder(HTMLParser):
    """Colectează atributele src ale imaginilor în ordinea din HTML."""

    def __init__(self):
        """Inițializează parserul și lista imaginilor."""
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        """Este apelată de feed pentru fiecare tag de început."""
        if tag == "img":
            src = dict(attrs).get("src")
            if src:
                self.images.append(src)


def page_fingerprint(url: str) -> str:
    """Returnează SHA256 al octeților paginii."""
    return hashlib.sha256(fetch(url).content).hexdigest()


def resolve(hostname: str) -> str:
    """Rezolvă numele domeniului la o adresă IPv4."""
    return socket.gethostbyname(hostname)


def cert_days_left(hostname: str) -> int:
    """Verifică TLS și calculează zilele întregi până la expirarea certificatului."""
    time.sleep(1)
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure:
            expires = ssl.cert_time_to_seconds(secure.getpeercert()["notAfter"])
    return int((expires - datetime.now(timezone.utc).timestamp()) // 86400)


def save_csv(results: dict, filename=None):
    """Salvează path, status și checked_at într-un CSV UTF8."""
    filename = filename or OUTPUT_DIR / "report.csv"
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["path", "status", "checked_at"])
        writer.writeheader()
        for path, status in results.items():
            writer.writerow({"path": path, "status": status,
                             "checked_at": datetime.now().isoformat()})


def site_report(url: str) -> dict:
    """Colectează și afișează raportul complet; salvează report.json și erorile."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Introduceți un URL complet HTTP sau HTTPS.")
    result = {"url": url, "checked_at": datetime.now().isoformat(), "errors": {}}
    try:
        response = fetch(url)
        internal, external = split_links(extract_links(response.text), response.url)
        result.update(status=response.status_code, final_url=response.url,
                      title=get_title(response.text),
                      security_headers=headers_presence(response.headers),
                      internal_links=len(internal), external_links=len(external))
        result["security_score"] = score_headers(result["security_headers"])
    except requests.RequestException as error:
        result.update(status=None, final_url=None, title=None, security_score=None,
                      security_headers=None, internal_links=None, external_links=None)
        result["errors"]["page"] = str(error)
    for key, function in (("ip", resolve), ("certificate_days_left", cert_days_left)):
        try:
            result[key] = function(parsed.hostname)
        except (OSError, ValueError, KeyError) as error:
            result[key] = None
            result["errors"][key] = str(error)
    try:
        redirect = fetch("http://" + parsed.netloc + "/")
        result["redirects"] = [{"status": r.status_code, "url": r.url,
                                "location": r.headers.get("Location")}
                               for r in redirect.history]
        result["http_final_url"] = redirect.url
        result["http_final_status"] = redirect.status_code
    except requests.RequestException as error:
        result["redirects"] = None
        result["errors"]["redirects"] = str(error)
    robots = fetch_robots(url)
    result["robots_available"] = robots is not None
    result["disallowed_paths"] = disallowed_paths(robots)
    with open(OUTPUT_DIR / "report.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    print(f"=== Raport site: {url} ===")
    for key, value in result.items():
        print(f"{key}: {value}")
    print("Salvat în report.json")
    return result


if __name__ == "__main__":
    # Ex. 46: la import __name__ este webtools, deci acest bloc nu se execută.
    try:
        print("Autotest:", get_status(BASE_URL))
    except requests.RequestException as error:
        print("Autotest indisponibil:", error)
