# Forensics și steganografie

`decode.py` rezolvă partea A, iar `partea2.py` rezolvă partea B. Probele sunt incluse și se pot regenera cu `probe_pregateste.py`. Rezultatele generate sunt salvate în `arsenal/forensics`.

```sh
python -m pip install -r requirements.txt
python decode.py U2FsdXQ=
python partea2.py
python teste/test_decode.py
```

Cu `--pas A1` sau `--pas B1` se poate rula un singur exercițiu.
