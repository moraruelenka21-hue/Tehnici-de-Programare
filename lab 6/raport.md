# Laboratorul 6 — Informații invizibile

## A. Decodare

- `mesaj.txt` are trei straturi, în ordinea Base64 → Base64 → hex. Mesajul decodat este `FLAG{straturi_de_encoding}`.
- Cheia XOR găsită este `128` (`0x80`). Textul obținut conține `FLAG{xor_un_octet}`.
- Primul hash MD5 are 32 de caractere hexazecimale. În dicționarul probei corespunde parolei `password`.
- `decode.py U2FsdXQ= --pas A7` scrie în `fisa.json` stratul `base64` și rezultatul `Salut`. Pentru `/w==`, rezultatul este `ff`, cu formatul `hex`. La citirea probei binare cu octeții `ff 0a`, rezultatul păstrează ambii octeți.
- `test_base64` și `test_binar` au trecut.

## B. Forensics și steganografie

- `foto.jpg` are semnătură JPEG (`FF D8 FF`), iar `ascuns.png` are semnătură PNG (`89 50 4E 47 0D 0A 1A 0A`).
- Șirurile tipăribile din PNG includ `IHDR`, `IEND` și `secret.txt`.
- EXIF indică Apple iPhone 13 și data `2026:09:14 10:30:00`. Coordonatele GPS sunt 47,0166667° N și 28,8575° E.
- Arhiva ZIP începe la octetul 782 din `ascuns.png`. Fișierul extras, `secret.txt`, conține `FLAG{ascuns_prin_carving}`.
- În `stego.png` au fost scriși 184 de biți. La citirea biților LSB s-a obținut `FLAG{ascuns_in_pixeli}`.
