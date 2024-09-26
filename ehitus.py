# Muutujad töötajate ja nende ülesannete hoidmiseks
tootajad = {}
ulesanded = []

# Funktsioon töötajate lisamiseks
def lisa_tootaja(nimi, amet):
    if nimi in tootajad:
        print(f"Töötaja {nimi} on juba olemas.")
    else:
        tootajad[nimi] = {
            "amet": amet,
            "aktiivne_ylesanne": None
        }
        print(f"Töötaja {nimi} lisatud ametikohale '{amet}'.")

# Funktsioon ülesannete lisamiseks
def lisa_ulesanne(nimi, keerukus):
    ulesanne = {
        "nimi": nimi,
        "keerukus": keerukus,
        "staatus": "olemas"
    }
    ulesanded.append(ulesanne)
    print(f"Ülesanne '{nimi}' lisatud keerukusega {keerukus}.")

# Funktsioon ülesande määramiseks töötajale
def maarake_ylesanne(tootaja_nimi, ulesanne_nimi):
    if tootaja_nimi not in tootajad:
        print(f"Töötajat nimega {tootaja_nimi} ei ole olemas.")
        return

    # Kontrollime, kas töötaja on saadaval
    if tootajad[tootaja_nimi]["aktiivne_ylesanne"]:
        print(f"Töötaja {tootaja_nimi} on juba ülesandega '{tootajad[tootaja_nimi]['aktiivne_ylesanne']}' hõivatud.")
        return

    # Otsime ülesannet
    for ulesanne in ulesanded:
        if ulesanne["nimi"] == ulesanne_nimi and ulesanne["staatus"] == "olemas":
            tootajad[tootaja_nimi]["aktiivne_ylesanne"] = ulesanne_nimi
            ulesanne["staatus"] = "määratud"
            print(f"Ülesanne '{ulesanne_nimi}' määratud töötajale {tootaja_nimi}.")
            return
    
    print(f"Ülesannet nimega '{ulesanne_nimi}' ei leitud või see on juba määratud.")

# Funktsioon oleku kuvamiseks
def kuva_seis():
    print("\n--- Töötajad ja nende ülesanded ---")
    for nimi, andmed in tootajad.items():
        print(f"Töötaja: {nimi}, Amet: {andmed['amet']}, Aktiivne ülesanne: {andmed['aktiivne_ylesanne']}")
    
    print("\n--- Ülesanded ---")
    for ulesanne in ulesanded:
        print(f"Ülesanne: {ulesanne['nimi']}, Keerukus: {ulesanne['keerukus']}, Staatus: {ulesanne['staatus']}")

# Peamine tsükkel
while True:
    print("\n1. Lisa töötaja")
    print("2. Lisa ülesanne")
    print("3. Määra ülesanne töötajale")
    print("4. Kuva olek")
    print("5. Välju")
    valik = input("Vali toiming (1-5): ")

    if valik == "1":
        nimi = input("Sisesta töötaja nimi: ")
        amet = input(f"Sisesta töötaja {nimi} amet: ")
        lisa_tootaja(nimi, amet)
    elif valik == "2":
        nimi = input("Sisesta ülesande nimi: ")
        keerukus = input(f"Sisesta ülesande {nimi} keerukus (lihtne, keskmine, raske): ")
        lisa_ulesanne(nimi, keerukus)
    elif valik == "3":
        tootaja_nimi = input("Sisesta töötaja nimi, kellele määrata ülesanne: ")
        ulesanne_nimi = input("Sisesta ülesande nimi, mida määrata: ")
        maarake_ylesanne(tootaja_nimi, ulesanne_nimi)
    elif valik == "4":
        kuva_seis()
    elif valik == "5":
        print("Programmi lõpetamine.")
        break
    else:
        print("Vale valik, proovi uuesti.")
