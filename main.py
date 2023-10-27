import matplotlib.pyplot as mat


def main():
    zrodlo = input("Wprowadz zrodlo danych (tekst lub plik): ").strip()
    if zrodlo == "tekst":
        tekst = input("Wprowadz tekst: ")
        dane = zLiCz_lItErY(tekst)
        hIsToGrAm(dane)
    elif zrodlo == "plik":
        path = input("Wprowadz sciezke do pliku tekstowego: ")
        tekst = z_PlIkU(path)
        dane = zLiCz_lItErY(tekst)
        hIsToGrAm(dane)
    else:
        print("Nieprawidlowe zrodlo danych. Wybierz 'tekst' lub 'plik'.")


def zLiCz_lItErY(tekst):
    dane = {}
    for char in tekst:
        if char.isalpha():
            char = char.lower()
            if char in dane:
                dane[char] += 1
            else:
                dane[char] = 1
    return dict(sorted(dane.items()))


def hIsToGrAm(dane):
    litery = list(dane.keys())
    ilosc = list(dane.values())

    mat.figure(figsize=(14, 7))
    mat.bar(litery, ilosc)
    mat.xlabel('Litera')
    mat.ylabel('Liczba wystapien')
    mat.title('Histogram liter')
    mat.grid(axis='y')
    mat.savefig("histogram")
    mat.show()


def z_PlIkU(file):
    plik = open(file)
    dane = plik.read()
    plik.close()
    return dane


if __name__ == "__main__":
    main()
