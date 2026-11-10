"""Detectează adresele cu multe eșecuri de autentificare SSH."""

import argparse
import json

from arsenal.aparare.parse_auth import afiseaza_rezumat, citeste_esecuri, pe_ip

PRAG_IMPLICIT = 10


def suspecti(counts, prag=PRAG_IMPLICIT):
    if prag < 1:
        raise ValueError(f"prag invalid: {prag} (cel putin 1)")
    peste_prag = [(ip, numar) for ip, numar in counts.items() if numar >= prag]
    return sorted(peste_prag, key=lambda pereche: pereche[1], reverse=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", help="Calea catre jurnalul de autentificare.")
    parser.add_argument("--prag", type=int, default=PRAG_IMPLICIT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    esecuri = citeste_esecuri(args.log)
    counts = pe_ip(esecuri)
    try:
        adrese_suspecte = suspecti(counts, args.prag)
    except ValueError as eroare:
        parser.error(str(eroare))

    if args.json:
        raport = {
            "esecuri": len(esecuri),
            "pe_ip": dict(counts.most_common()),
            "suspecti": adrese_suspecte,
        }
        print(json.dumps(raport, indent=2))
        return

    afiseaza_rezumat(len(esecuri), counts)
    print(f"Suspecti (prag {args.prag}):")
    for ip, numar in adrese_suspecte:
        print(f"  {ip}  ({numar} incercari)  BRUTE FORCE")


if __name__ == "__main__":
    main()
