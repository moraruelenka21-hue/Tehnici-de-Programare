import re
import argparse
import zipfile
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

BAZA = Path(__file__).resolve().parents[2] / "probe"
AICI = Path(__file__).resolve().parent

# B1. Tipul real al fișierului
def tip_real(cale):
    cap = Path(cale).read_bytes()[:8]
    if cap.startswith(b"%PDF"):
        return "pdf"
    if cap.startswith(b"\x89PNG"):
        return "png"
    if cap.startswith(b"\xff\xd8"):
        return "jpg"
    if cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    return cap.hex()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pas", default="toate")
    a = p.parse_args()

    if a.pas in ("toate", "B1"):
        print("B1")
        print("foto.jpg:", tip_real(BAZA / "foto.jpg"))
        print("ascuns.png:", tip_real(BAZA / "ascuns.png"))

    # B2. Secvențe de text din fișierul binar
    if a.pas in ("toate", "B2"):
        print("B2")
        date = (BAZA / "ascuns.png").read_bytes()
        for m in re.findall(rb"[ -~]{4,}", date):
            print(m.decode())

    # B3. Metadate EXIF și coordonate GPS
    if a.pas in ("toate", "B3"):
        print("B3")
        exif = Image.open(BAZA / "foto.jpg").getexif()
        for tag, val in exif.items():
            if tag != 34853:
                print(TAGS.get(tag, tag), "=", val)
        gps = exif.get_ifd(34853)
        lat = gps[2]
        lon = gps[4]
        latitudine = float(lat[0] + lat[1] / 60 + lat[2] / 3600)
        longitudine = float(lon[0] + lon[1] / 60 + lon[2] / 3600)
        if gps[1] == "S":
            latitudine = -latitudine
        if gps[3] == "W":
            longitudine = -longitudine
        print("Latitudine:", latitudine)
        print("Longitudine:", longitudine)

    # B4. Extragerea arhivei ZIP
    if a.pas in ("toate", "B4"):
        print("B4")
        date = (BAZA / "ascuns.png").read_bytes()
        i = date.find(b"PK\x03\x04")
        if i != -1:
            (AICI / "gasit.zip").write_bytes(date[i:])
            print("Arhiva extrasă de la octetul", i)
            with zipfile.ZipFile(AICI / "gasit.zip") as z:
                print("Fișiere:", z.namelist())
                print(z.read("secret.txt").decode().strip())

    # B5. Ascunderea mesajului în ultimul bit al canalului roșu
    if a.pas in ("toate", "B5"):
        print("B5")
        img = Image.open(BAZA / "foto.jpg").convert("RGB")
        px = list(img.get_flattened_data())
        mesaj = b"FLAG{ascuns_in_pixeli}" + b"\0"
        biti = "".join(f"{x:08b}" for x in mesaj)
        px_nou = []
        for i, (r, g, b) in enumerate(px):
            if i < len(biti):
                r = (r & ~1) | int(biti[i])
            px_nou.append((r, g, b))
        img.putdata(px_nou)
        img.save(AICI / "stego.png")
        print("Salvat: arsenal/forensics/stego.png")
        print("Biți scriși:", len(biti))

    # B6. Recuperarea mesajului din canalul roșu
    if a.pas in ("toate", "B6"):
        print("B6")
        img = Image.open(AICI / "stego.png").convert("RGB")
        biti = ""
        for r, g, b in img.get_flattened_data():
            biti += str(r & 1)
        octeti = []
        for i in range(0, len(biti), 8):
            octet = biti[i:i + 8]
            if len(octet) < 8:
                break
            valoare = int(octet, 2)
            if valoare == 0:
                break
            octeti.append(valoare)
        print(bytes(octeti).decode())

if __name__ == "__main__":
    main()
