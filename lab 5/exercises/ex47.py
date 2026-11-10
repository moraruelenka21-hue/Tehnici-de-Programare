# Exercițiul 47 — Constantele de modul
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

from webtools import DEFAULT_HEADERS, fetch
print("Constanta:", DEFAULT_HEADERS)
response = fetch(ECHO_URL + "/headers")
print("User-Agent primit:", response.json()["headers"].get("User-Agent"))
# DEFAULT_HEADERS = {"User-Agent": "WebLab-Student"}
# fetch o folosește pentru httpbin.org.
# Pe cybercor păstrăm antetele standard, conform regulilor.
