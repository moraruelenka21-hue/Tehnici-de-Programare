# Exercițiul 46 — Blocul de execuție main
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

import runpy
import webtools
# La import, blocul main din webtools nu se execută.
print("Numele modulului importat:", webtools.__name__)
print("Simulare a rulării directe python webtools.py:")
runpy.run_module("webtools", run_name="__main__")
# În webtools.py există:
# if __name__ == "__main__":
#     print("Autotest:", get_status(BASE_URL))
# Rularea directă folosește numele __main__, importul nu.
