"""Comparatie SUID cu o imagine de referinta."""

import argparse
import json
from pathlib import Path
from arsenal.privesc.enum import citeste_linii, nume, GTFO


def cai(fisier):
    return set(citeste_linii(fisier))


def compara(baza, acum):
    noi = acum - baza
    risc = {nume(c): ("mare" if nume(c) in GTFO else "normal")
            for c in sorted(noi)}
    periculoase = [c for c in sorted(noi) if nume(c) in GTFO]
    return {"noi": sorted(noi), "risc": risc, "periculoase": periculoase}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("capturi", type=Path)
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    baza = cai(a.capturi / "baza_suid.txt")
    acum = cai(a.capturi / "suid.txt")
    rezultat = compara(baza, acum)
    if a.json:
        print(json.dumps(rezultat, indent=2, ensure_ascii=False))
        return
    print("baza:", len(baza), " acum:", len(acum))
    print(len(rezultat["noi"]), "SUID noi fata de sistemul curat")
    for c in rezultat["noi"]:
        print(" ", c)
    print("periculoase NOI:", rezultat["periculoase"])


if __name__ == "__main__":
    main()
