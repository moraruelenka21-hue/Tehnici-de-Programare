"""Inventar de procese și evenimente Windows."""

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

CAI_SUSPECTE = ("\\temp\\", "\\roaming\\")
SUSPECTE_ID = {4625, 1102, 7045}


@dataclass
class Proces:
    pid: int
    nume: str
    user: str
    cale: str

    def e_suspect(self):
        cale = self.cale.casefold()
        return any(folder in cale for folder in CAI_SUSPECTE)


@dataclass
class Eveniment:
    id: int
    nivel: str
    sursa: str
    cont: str
    mesaj: str

    def e_suspect(self):
        return self.id in SUSPECTE_ID or self.nivel.casefold() == "critical"


def procese_din_json(cale):
    with open(cale, encoding="utf-8") as fisier:
        return [Proces(**date) for date in json.load(fisier)]


def evenimente_din_json(cale):
    with open(cale, encoding="utf-8") as fisier:
        return [Eveniment(**date) for date in json.load(fisier)]


@dataclass
class Inventar:
    procese: list[Proces]

    @classmethod
    def din_json(cls, cale):
        return cls(procese_din_json(cale))

    def __len__(self):
        return len(self.procese)

    def suspecte(self):
        return [proces for proces in self.procese if proces.e_suspect()]

    def pe_user(self):
        grupuri = {}
        for proces in self.procese:
            grupuri.setdefault(proces.user, []).append(proces.nume)
        return grupuri


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capturi", type=Path, help="Folderul cu cele doua fisiere JSON.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        inventar = Inventar.din_json(args.capturi / "procese.json")
        evenimente = evenimente_din_json(args.capturi / "evenimente.json")
    except (OSError, UnicodeError, ValueError, TypeError) as eroare:
        parser.error(f"nu pot incarca datele: {eroare}")

    suspecte = inventar.suspecte()
    alarma = [eveniment for eveniment in evenimente if eveniment.e_suspect()]

    if args.json:
        raport = {
            "procese_suspecte": [asdict(proces) for proces in suspecte],
            "evenimente_alarma": [asdict(eveniment) for eveniment in alarma],
        }
        print(json.dumps(raport, ensure_ascii=False, indent=2))
        return

    print(f"Procese: {len(inventar)} | suspecte: {len(suspecte)}")
    for proces in suspecte:
        print(f"  [{proces.pid}] {proces.nume}  ({proces.user})  {proces.cale}")
    print(f"Evenimente: {len(evenimente)} | alarma: {len(alarma)}")
    for eveniment in alarma:
        print(f"  {eveniment.id} [{eveniment.nivel}] {eveniment.cont}: {eveniment.mesaj}")


if __name__ == "__main__":
    main()
