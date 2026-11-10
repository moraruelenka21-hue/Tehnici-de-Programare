import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from arsenal.forensics.decode import decodeaza, desfa

def test_base64():
    strat, rezultat = desfa("U2FsdXQ=")
    assert strat == "base64"
    assert rezultat == b"Salut"

def test_binar():
    assert decodeaza("/w==") == (["base64"], b"\xff")
    assert decodeaza("%FF") == (["url"], b"\xff")
    assert decodeaza(b"\xff\n") == ([], b"\xff\n")

if __name__ == "__main__":
    test_base64()
    print("test_base64: OK")
    test_binar()
    print("test_binar: OK")
