"""Exercițiile 21–34; implementările reutilizabile sunt în webtools."""
from webtools import (fetch, get_status, get_title, page_exists, check_paths,
                      get_header, security_headers, score_headers, fetch_robots,
                      disallowed_paths, response_times, log)
import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10


def demonstrate(label, function, *args, **kwargs):
    """Execută o demonstrație și afișează erorile fără a opri celelalte exerciții."""
    try:
        result = function(*args, **kwargs)
        print(label, result)
        return result
    except (requests.RequestException, TypeError, ValueError) as error:
        print(label, type(error).__name__, str(error))
        return None


def main():
    """Apelează fiecare funcție cerută cel puțin o dată."""
    response = demonstrate("Ex. 21 fetch:", fetch, BASE_URL)
    if response is not None:
        print("Status:", response.status_code)
    for path in ("/", "/robots.txt", "/sitemap.xml"):
        demonstrate("Ex. 22 " + path, get_status, BASE_URL + path)
    demonstrate("Ex. 23 implicit", fetch, BASE_URL)
    demonstrate("Ex. 23 explicit", fetch, BASE_URL, timeout=3)
    demonstrate("Ex. 24 titlu", get_title, response.text if response is not None else "")
    help(get_title)  # Ex. 25
    demonstrate("Ex. 26 tip incorect", get_status, 123)
    # Type hints nu validează la execuție. Requests respinge 123 ca URL invalid.
    demonstrate("Ex. 27 URL invalid", page_exists, "https://this-domain-does-not-exist.invalid")
    demonstrate("Ex. 28 căi", check_paths, BASE_URL, ["/", "/robots.txt", "/sitemap.xml"])
    demonstrate("Ex. 29 argument cu nume", get_header, BASE_URL, name="Server")
    headers = demonstrate("Ex. 30 antete", security_headers, BASE_URL)
    if headers is not None:
        demonstrate("Ex. 31 scor", score_headers, headers)
    robots = demonstrate("Ex. 32 robots", fetch_robots, BASE_URL)
    demonstrate("Ex. 32 Disallow", disallowed_paths, robots)
    demonstrate("Ex. 32 None", disallowed_paths, None)
    demonstrate("Ex. 33 timpi", response_times, BASE_URL, BASE_URL + "/robots.txt")
    log("Ex. 34 verificat", url=BASE_URL, status=response.status_code if response is not None else None)
    # print afișează; return oferă o valoare apelantului pentru reutilizare.


if __name__ == "__main__":
    main()
