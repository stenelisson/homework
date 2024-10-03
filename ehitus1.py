# Materjalide loetelu
materjalid = {
    "betoon": 500,  # kg
    "tellised": 1000,  # tk
    "teras": 300,  # kg
    "puit": 200  # m3
}

# Ülesannete loetelu
ulesanded = []

# Funktsioon materjalide lisamiseks
def lisa_materjal(nimi, kogus):
    if nimi in materjalid:
        materjalid[nimi] += kogus
    else:
        materjalid[nimi] = kogus
    print(f"Lisatud {kogus} {nimi}. Kokku: {materjalid[nimi]}.")

# Funktsioon ülesannete lisamiseks
def lisa_ulesanne(nimi, vajalikud_materjalid):
    # Kontrollime, kas kõik vajalikud materjalid on saadaval
    for materjal, kogus in vajalikud_materjalid.items():
        if materjal not in materjalid or materjalid[materjal] < kogus:
            print(f"Ülesannet '{nimi}' ei saa lisada. Puudub {materjal} või kogus ei ole piisav.")
            return
    
    # Kui kõik materjalid on saadaval, lisame ülesande
    ulesanded.append(nimi)
    for materjal, kogus in vajalikud_materjalid.items():
        materjalid[materjal] -= kogus
    
    print(f"Ülesanne '{nimi}' on lisatud ja vajalikud materjalid vähendatud.")

# Funktsioon, mis kuvab hetke seisuga ülesandeid ja materjale
def kuva_seis():
    print("\nMaterjalid hetkel:")
    for materjal, kogus in materjalid.items():
        print(f"{materjal}: {kogus}")
    
    print("\nÜlesanded hetkel:")
    for idx, ulesanne in enumerate(ulesanded, start=1):
        print(f"{idx}. {ulesanne}")

# Peamine programmi tsükkel
while True:
    print("\n1. Lisa materjal")
    print("2. Lisa ülesanne")
    print("3. Kuva seis")
    print("4. Välju")
    valik = input("Vali toiming (1-4): ")

    if valik == "1":
        nimi = input("Sisesta materjali nimi: ")
        kogus = int(input(f"Sisesta kogus materjalile {nimi}: "))
        lisa_materjal(nimi, kogus)
    elif valik == "2":
        nimi = input("Sisesta ülesande nimi: ")
        vajalikud_materjalid = {}
        while True:
            materjal = input("Sisesta vajalik materjal (või 'valmis' lõpetamiseks): ")
            if materjal == "valmis":
                break
            kogus = int(input(f"Sisesta vajalik kogus materjalile {materjal}: "))
            vajalikud_materjalid[materjal] = kogus
        lisa_ulesanne(nimi, vajalikud_materjalid)
    elif valik == "3":
        kuva_seis()
    elif valik == "4":
        print("Programmi lõpetamine.")
        break
    else:
        print("Vale valik, proovi uuesti.")
