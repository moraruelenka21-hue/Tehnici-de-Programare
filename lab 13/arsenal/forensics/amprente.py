import argparse
import hashlib
from pathlib import Path


MAGIC = {b"\x89PNG": "PNG", b"%PDF": "PDF", b"PK\x03\x04": "ZIP"}


def tip(head):
    for semnatura, nume in MAGIC.items():
        if head.startswith(semnatura):
            return nume
    return "necunoscut"


def amprenta_fisier(cale):
    cale = Path(cale)
    with cale.open("rb") as fisier:
        date = fisier.read()
    return {
        "nume": cale.name,
        "tip": tip(date[:8]),
        "sha256": hashlib.sha256(date).hexdigest()[:16],
    }


def scaneaza(folder):
    return [amprenta_fisier(cale) for cale in sorted(Path(folder).iterdir())
            if cale.is_file()]


def main():
    parser = argparse.ArgumentParser(description="Identifică și amprentează fișierele.")
    parser.add_argument("folder", help="folderul cu probe")
    for fisa in scaneaza(parser.parse_args().folder):
        print(f"{fisa['nume']:14} {fisa['tip']:11} {fisa['sha256']}")


if __name__ == "__main__":
    main()
