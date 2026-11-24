from pathlib import Path

from arsenal.forensics.amprente import amprenta_fisier, scaneaza, tip

PROBE = Path(__file__).with_name("probe")


def test_tip_din_magic():
    assert tip(b"\x89PNG\r\n") == "PNG"
    assert tip(b"%PDF-1.4") == "PDF"
    assert tip(b"PK\x03\x04") == "ZIP"
    assert tip(b"text") == "necunoscut"


def test_amprenta_png():
    assert amprenta_fisier(PROBE / "imagine.png") == {
        "nume": "imagine.png", "tip": "PNG", "sha256": "ea3a9848da7e6c1d"
    }


def test_scaneaza_toate():
    nume = [fisa["nume"] for fisa in scaneaza(PROBE)]
    assert nume == ["arhiva.zip", "imagine.png", "note.txt", "raport.pdf"]
