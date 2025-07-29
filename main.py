# projekt_04.py: čtvrtý projekt do Engeto Online Python Akademie

# author: Pavel Nováček
# email: gippel@seznam.cz


def hlavni_menu():
    """
    Zobrazí hlavní menu a umožní spustit funkci dle volby 1-4.
    """
    while True:
        print("Správce úkolů - hlavní menu",
              "1. Přidat úkol",
              "2. Zobrazit všechny úkoly",
              "3. Vymazat úkol",
              "4. Konec programu",
              sep="\n"
              )
        try:
            vstup = int(input("Zvolte 1-4: "))
            if vstup not in (1, 2, 3, 4):
                print("Volba mimo rozsah. Napište číslo 1-4.\n")
                continue
            return vstup
        except ValueError:
            print("Neplatný vstup. Napište číslo 1-4.\n")
            continue


def pridat_ukol_input():
    """
    Umožní přidat úkol ve formátu: název a popis.

    Příklad:
    Zadejte název úkolu: Test1
    Zadejte popis úkolu: Toto je test.
    """
    while True:
        print("Pro návrat do hlavního menu napište 'z'")
        nazev = input("Zadejte název úkolu: ")
        if nazev == "":
            print("Zadali jste prázdný vstup. Zadejte název úkolu.\n")
            continue
        elif nazev == "z":
            print()
            return None
        popis = input("Zadejte popis úkolu: ")
        if popis == "":
            print("Zadali jste prázdný vstup. Zadejte popis úkolu.\n")
            continue
        elif popis == "z":
            print()
            return None
        return nazev, popis


def pridat_ukol(nazev, popis):
    if nazev and popis:
        print(f"Úkol {nazev} byl přidán.")
        return {nazev: popis}


def zobrazit_ukoly(seznam):
    """
    Zobrazí uložené úkoly.

    Příklad:
    1. Test1 - Toto je test.
    """
    if len(seznam) == 0:
        print("Seznam úkolů je prázdný.\n")
        return True
    else:
        for pozice_seznamu, ukol in enumerate(seznam, start=1):
            for klic, hodnota in ukol.items():
                print(f"{pozice_seznamu}. {klic} - {hodnota}")
    print()
    return False


def odstranit_ukol(seznam):
    """
    Umožní odstranit úkol ze seznamu.
    """
    if zobrazit_ukoly(seznam):
        return

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
            print("Zadali jste prázdný vstup. Zadejte číslo.\n")
            continue


def main():
    """
    Hlavní běh programu, který spouští funkci dle volby.
    """
    while True:
        volba = hlavni_menu()
        print()
        if volba == 1:
            ukol = pridat_ukol_input()
            if ukol:
                ukoly.append(pridat_ukol(ukol[0], ukol[1]))
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
