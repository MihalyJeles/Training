import requests

def fajl_letoltes(url, cel_fajlnev):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Hibát dob, ha nem sikerült a letöltés
        with open(cel_fajlnev, 'wb') as f:
            f.write(response.content)
        print(f"Sikeresen letöltve: {cel_fajlnev}")
    except requests.exceptions.RequestException as e:
        print(f"Hiba történt a letöltés során: {e}")
# Példa használat:
url = "https://example.com/fajl.pdf"  # Cseréld ki a kívánt URL-re
cel_fajlnev = "letoltott_fajl.pdf"     # Cseréld ki a kívánt fájlnévre
fajl_letoltes(url, cel_fajlnev)
/