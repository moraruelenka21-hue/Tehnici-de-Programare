import re
import base64
import hashlib
import argparse
import json
from pathlib import Path
from urllib.parse import unquote

BAZA = Path(__file__).resolve().parents[2]
AICI = Path(__file__).resolve().parent

# A2. Recunoașterea codării
def ghici_strat(s):
    if re.search(r"%[0-9a-fA-F]{2}", s):
        return "url"
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/]+={0,2}", s) and len(s) % 4 == 0:
        return "base64"
    return "necunoscut"

# A3. Desfacerea unui strat
def desfa(s):
    strat = ghici_strat(s)
    if strat == "url":
        return strat, unquote(s).encode()
    if strat == "hex":
        return strat, bytes.fromhex(s)
    if strat == "base64":
        return strat, base64.b64decode(s, validate=True)
    return strat, s.encode()

# A4. Desfacerea straturilor succesive
def decodeaza(text):
    straturi = []
    for _ in range(8):
        strat, date = desfa(text)
        if strat == "necunoscut":
            break
        text = date.decode()
        straturi.append(strat)
    return straturi, text

def citibil(date):
    return all(32 <= c < 127 for c in date)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("intrare", nargs="?", default="U2FsdXQ=")
    p.add_argument("--fisier", action="store_true")
    p.add_argument("--pas", default="toate")
    a = p.parse_args()

    # A1. Text și octeți
    if a.pas in ("toate", "A1"):
        print("A1")
        s = "Salut"
        b = s.encode()
        print(b, b[0])
        print(b.hex())
        print(bytes.fromhex(b.hex()))

    if a.pas in ("toate", "A2"):
        print("A2")
        print(ghici_strat("%2Fetc"))
        print(ghici_strat("48656c6c6f"))

    if a.pas in ("toate", "A3"):
        print("A3")
        print(desfa("%2Fetc"))
        print(desfa("48656c6c6f"))

    if a.pas in ("toate", "A4"):
        print("A4")
        text = (BAZA / "mesaj.txt").read_text().strip()
        straturi, rezultat = decodeaza(text)
        print("Straturi:", straturi)
        print("Mesaj:", rezultat)

    # A5. XOR cu o cheie de un octet
    if a.pas in ("toate", "A5"):
        print("A5")
        date = (BAZA / "xor.bin").read_bytes()
        for k in range(256):
            clar = bytes(b ^ k for b in date)
            if citibil(clar):
                print("Cheie:", k)
                print(clar.decode())
                break

    # A6. Hash MD5 și dicționar
    if a.pas in ("toate", "A6"):
        print("A6")
        tinta = (BAZA / "hashuri.txt").read_text().splitlines()[0]
        print("Lungime hash:", len(tinta))
        for cuv in (BAZA / "wordlist.txt").read_text().splitlines():
            if hashlib.md5(cuv.encode()).hexdigest() == tinta:
                print("Parola:", cuv)
                break

    # A7. Intrare din linia de comandă și fișa JSON
    if a.pas in ("toate", "A7"):
        print("A7")
        text = a.intrare
        if a.fisier:
            text = Path(a.intrare).read_text().strip()
        straturi, rezultat = decodeaza(text)
        fisa = {"strat": straturi, "rezultat": rezultat}
        with open(AICI / "fisa.json", "w", encoding="utf-8") as f:
            json.dump(fisa, f, ensure_ascii=False, indent=4)
        print(json.dumps(fisa, ensure_ascii=False, indent=4))
        print("Salvat: arsenal/forensics/fisa.json")

if __name__ == "__main__":
    main()
