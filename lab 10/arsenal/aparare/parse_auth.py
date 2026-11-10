"""Extrage și numără eșecurile de autentificare SSH."""

import argparse
import re
import sys
from collections import Counter

TIPAR = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+) port")


def esec(linie):
    potrivire = TIPAR.search(linie)
    if potrivire is None:
        return None
    return potrivire.group(1), potrivire.group(2)


def citeste_esecuri(cale):
    esecuri = []
    try:
        with open(cale, encoding="utf-8", errors="replace") as jurnal:
            for linie in jurnal:
                rezultat = esec(linie)
                if rezultat is not None:
                    user, ip = rezultat
                    esecuri.append({"user": user, "ip": ip})
    except FileNotFoundError:
        print(f"nu gasesc {cale}", file=sys.stderr)
        return []
    except OSError as eroare:
        print(f"nu pot citi {cale}: {eroare.strerror}", file=sys.stderr)
        return []
    return esecuri


def pe_ip(esecuri):
    return Counter(fisa["ip"] for fisa in esecuri)


def afiseaza_rezumat(total, counts):
    print(f"Esecuri de autentificare: {total}")
    for ip, numar in counts.most_common():
        print(f"  {ip}: {numar}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", help="Calea catre jurnalul de autentificare.")
    args = parser.parse_args()
    esecuri = citeste_esecuri(args.log)
    afiseaza_rezumat(len(esecuri), pe_ip(esecuri))


if __name__ == "__main__":
    main()
