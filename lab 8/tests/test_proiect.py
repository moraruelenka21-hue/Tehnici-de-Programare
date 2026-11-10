import json
import subprocess
import sys
from pathlib import Path
from arsenal.privesc.enum import (
    citeste_linii, enumereaza, filtreaza_risc, grupeaza_risc, utilizatori,
)
from arsenal.privesc.diferenta import cai, compara

ROOT = Path(__file__).resolve().parents[1]
START = ROOT / "arsenal/privesc/start"


def test_date_furnizate():
    r = enumereaza(START)
    assert len(citeste_linii(START / "suid.txt")) == 14
    assert [len(r[c]) for c in ("suid", "sudo", "cron")] == [13, 3, 3]
    assert [len(v) for v in filtreaza_risc(r, "mare").values()] == [4, 2, 0]
    assert utilizatori(r) == {"ana", "root", "www-data"}
    assert r["cron"][0]["comanda"] == "cd / && run-parts --report /etc/cron.hourly"
    assert r["cron"][2]["user"] == "www-data"
    assert len(grupeaza_risc(r)["neclasificat"]) == 3


def test_diferenta_furnizata():
    rezultat = compara(cai(START / "baza_suid.txt"), cai(START / "suid.txt"))
    expected = ["/bin/cp", "/usr/bin/find", "/usr/bin/nmap", "/usr/bin/vim.basic"]
    assert rezultat["noi"] == expected
    assert rezultat["periculoase"] == expected


def test_elimina_goluri_comentarii_pastreaza_dubluri(tmp_path):
    p = tmp_path / "intrare.txt"
    p.write_text("  # comentariu\n\n /bin/cp \n/bin/cp\n", encoding="utf-8")
    assert citeste_linii(p) == ["/bin/cp", "/bin/cp"]


def test_diferenta_directie_si_filtrare():
    r = compara({"/bin/vechi", "/bin/cp"}, {"/bin/cp", "/usr/bin/find", "/bin/nou"})
    assert r["noi"] == ["/bin/nou", "/usr/bin/find"]
    assert r["periculoase"] == ["/usr/bin/find"]
    assert r["risc"]["nou"] == "normal"
    assert compara(set(), set())["noi"] == []


def test_json_curat_fara_scriere(tmp_path):
    cmd = [sys.executable, "-m", "arsenal.privesc.enum", str(START), "--json"]
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True)
    assert set(json.loads(p.stdout)) == {"suid", "sudo", "cron"}
    out = tmp_path / "raport.json"
    subprocess.run(cmd[:-1] + ["--output", str(out)], cwd=ROOT, check=True,
                   capture_output=True)
    assert json.loads(out.read_text(encoding="utf-8")) == enumereaza(START)
