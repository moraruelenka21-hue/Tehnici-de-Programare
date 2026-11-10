Colecții în Python
Moraru Elena, SI-264

Fișiere principale
  arsenal/privesc/enum.py           Citire SUID, sudo și cron; raport JSON
  arsenal/privesc/diferenta.py      Comparație cu sistemul de referință
  arsenal/privesc/test_diferenta.py Testul de regresie
  arsenal/privesc/enum.json         Raport generat pe datele furnizate
  arsenal/privesc/start/            Cele patru fișiere de intrare
  tests/test_proiect.py             Verificări suplimentare
  evidence/run_*.py                 Exemple executabile pentru pașii individuali

Rulare din rădăcina proiectului, cu Python 3.10 sau mai nou:
  python -m pip install -r requirements.txt
  python -m arsenal.privesc.enum arsenal/privesc/start
  python -m arsenal.privesc.enum arsenal/privesc/start --json
  python -m arsenal.privesc.enum arsenal/privesc/start --output arsenal/privesc/enum.json
  python -m arsenal.privesc.diferenta arsenal/privesc/start
  python -m arsenal.privesc.diferenta arsenal/privesc/start --json
  python -m pytest -q arsenal/privesc/test_diferenta.py tests

Filtrare opțională:
  python -m arsenal.privesc.enum arsenal/privesc/start --risc mare --json

Exemple individuale:
  python -m evidence.run_A1
  python -m evidence.run_A2
  python -m evidence.run_A3
  python -m evidence.run_A4
  python -m evidence.run_B1
  python -m evidence.run_B2
  python -m evidence.run_B3
  python -m evidence.run_O1

Fără --json, enum.py afișează rezumatul și salvează enum.json în directorul
curent. --output stabilește altă destinație. Cu --json se scrie numai la stdout.
Programele folosesc biblioteca standard; pytest este necesar doar pentru teste.

Rezultate
14 linii SUID, 13 căi distincte, 4 SUID cu risc mare.
3 reguli sudo, dintre care 2 cu risc mare; 3 sarcini cron.
Utilizatori: ana, root, www-data. Referință: 9 căi; captura curentă: 13 căi.
Căi noi: /bin/cp, /usr/bin/find, /usr/bin/nmap, /usr/bin/vim.basic.
Toate cele 6 teste trec. Fișierele de intrare sunt identice cu cele furnizate.

Etichetele de risc urmează regula din cerință. Sarcinile cron nu au câmpul
risc; în gruparea opțională apar ca neclasificate.
