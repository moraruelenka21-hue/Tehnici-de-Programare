"""Enumerarea fisierelor SUID, regulilor sudo si sarcinilor cron."""

import argparse
import json
from pathlib import Path

GTFO = {"find", "vim.basic", "vim", "nmap", "cp", "bash",
        "less", "awk", "python3", "perl"}


def citeste_linii(cale):
    """Pastreaza ordinea si dublurile; elimina golurile si comentariile."""
    with open(cale, encoding="utf-8") as fisier:
        return [ln.strip() for ln in fisier
                if ln.strip() and not ln.lstrip().startswith("#")]


def nume(cale):
    """Extrage numele unei cai Linux, inclusiv cand rulam pe Windows."""
    return cale.rsplit("/", 1)[-1]


def suid_constatari(cale):
    """O fisa pentru fiecare cale unica, in ordine determinista."""
    return [{"cale": c, "nume": nume(c),
             "risc": "mare" if nume(c) in GTFO else "normal"}
            for c in sorted(set(citeste_linii(cale)))]


def sudo_constatari(cale):
    """Despacheteaza fiecare regula in utilizator si drept."""
    out = []
    for ln in citeste_linii(cale):
        user, drept = ln.split(" : ", 1)
        out.append({"user": user.strip(), "drept": drept.strip(),
                    "risc": "mare" if "NOPASSWD" in drept else "normal"})
    return out


def cron_constatari(cale):
    """Formatul furnizat: cinci campuri de timp, user, comanda."""
    out = []
    for ln in citeste_linii(cale):
        campuri = ln.split(maxsplit=6)
        if len(campuri) != 7:
            raise ValueError(f"Linie cron invalida: {ln}")
        out.append({"user": campuri[5], "comanda": campuri[6]})
    return out


def enumereaza(d):
    """Grupeaza constatarile pe sursa intr-un dictionar de liste."""
    d = Path(d)
    return {"suid": suid_constatari(d / "suid.txt"),
            "sudo": sudo_constatari(d / "sudo.txt"),
            "cron": cron_constatari(d / "crontab.txt")}


def utilizatori(raport):
    return ({c["user"] for c in raport["sudo"]}
            | {c["user"] for c in raport["cron"]})


def filtreaza_risc(raport, risc):
    """Extindere optionala: filtrare in toate categoriile."""
    return {cat: [c for c in lista if c.get("risc") == risc]
            for cat, lista in raport.items()}


def grupeaza_risc(raport):
    """Extindere optionala: campul absent devine neclasificat."""
    grupuri = {}
    for categorie, lista in raport.items():
        for c in lista:
            eticheta = c.get("nume", c.get("user", ""))
            grupuri.setdefault(c.get("risc", "neclasificat"), []).append(
                f"{categorie}: {eticheta}")
    return grupuri


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("capturi", type=Path)
    p.add_argument("--json", action="store_true")
    p.add_argument("--risc", choices=["mare", "normal"])
    p.add_argument("--output", type=Path, default=Path("enum.json"))
    a = p.parse_args()
    raport = enumereaza(a.capturi)
    if a.risc:
        raport = filtreaza_risc(raport, a.risc)
    if a.json:
        print(json.dumps(raport, indent=2, ensure_ascii=False))
        return
    for categorie, lista in raport.items():
        mari = [c for c in lista if c.get("risc") == "mare"]
        print(f"{categorie}: {len(lista)} gasite, {len(mari)} cu risc mare")
    print("utilizatori implicati:", ", ".join(sorted(utilizatori(raport))))
    with a.output.open("w", encoding="utf-8") as f:
        json.dump(raport, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Raport salvat in {a.output.as_posix()}")


if __name__ == "__main__":
    main()
