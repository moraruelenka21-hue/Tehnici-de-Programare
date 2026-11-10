import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from arsenal.forensics.decode import desfa

def test_base64():
    strat, rezultat = desfa("U2FsdXQ=")
    assert strat == "base64"
    assert rezultat == b"Salut"

if __name__ == "__main__":
    test_base64()
    print("test_base64: OK")
