# projekt_4.py: čtvrtý projekt do Engeto Online Python Akademie

# author: Pavel Nováček
# email: gippel@seznam.cz


def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu",
              "1. Přidat nový úkol",
              "2. Zobrazit všechny úkoly",
              "3. Odstranit úkol",
              "4. Konec programu",
              sep="\n"
              )
        try:
            vstup = int(input("Vyberte možnost (1-4): "))
            if vstup not in (1, 2, 3, 4):
                print("Volba mimo rozsah. Zadejte číslo 1-4.\n")
                continue
            return vstup
        except ValueError:
            print("Neplatná volba.\n")
            continue


def pridat_ukol():
    while True:
        print("Pro návrat do hlavního menu napište 'z'")
        nazev = input("Zadejte název úkolu: ")
        if nazev == "":
            print("Zadali jste prázdný vstup.\n")
            continue
        elif nazev == "z":
            print()
            break
        popis = input("Zadejte popis úkolu: ")
        if popis == "":
            print("Zadali jste prázdný vstup.\n")
            continue
        elif popis == "z":
            print()
            break
        print(f"Úkol {nazev} byl přidán.")
        return {nazev: popis}


def zobrazit_ukoly(seznam):
    if len(seznam) == 0:
        print("Seznam úkolů je prázdný.",
              "\n", end=""
              )
    else:
        for pozice_seznamu, ukol in enumerate(seznam, start=1):
            for klic, hodnota in ukol.items():
                print(f"{pozice_seznamu}. {klic} - {hodnota}")
    print()


def odstranit_ukol(seznam):
    zobrazit_ukoly(seznam)

    while True:
        print("Pro návrat do hlavního menu napište 'z'")
        try:
            vstup = input("Zadejte číslo úkolu, který chcete vymazat: ")
            if vstup == "z":
                print()
                break
            elif len(seznam) == 0:
                break
            elif int(vstup) not in range(1, len(seznam) + 1):
                print("Úkol není v seznamu.")
                continue
            else:
                seznam.pop(int(vstup) - 1)
                print(f"Úkol {vstup} byl vymazán.\n")
                break
        except ValueError:
            print("Zadali jste prázdný vstup.\n")
            continue


def main():
    while True:
        volba = hlavni_menu()
        print()
        if volba == 1:
            ukol = pridat_ukol()
            if ukol:
                ukoly.append(ukol)
                print()
        elif volba == 2:
            zobrazit_ukoly(ukoly)
        elif volba == 3:
            odstranit_ukol(ukoly)
        elif volba == 4:
            print("Konec programu.")
            exit()


ukoly = []

if __name__ == "__main__":
    main()
