import matplotlib.pyplot as mat


def main():
    zrodlo = input("Wprowadz zrodlo danych (tekst lub plik): ").strip()
    if zrodlo == "tekst":
        tekst = input("Wprowadz tekst: ")
        dane = zlicz_litery(tekst)
        histogram(dane)
    elif zrodlo == "plik":
        path = input("Wprowadz sciezke do pliku tekstowego: ")
        tekst = Z_pliku(path)
        dane = zlicz_litery(tekst)
        histogram(dane)
    else:
        print("Nieprawidlowe zrodlo danych. Wybierz 'tekst' lub 'plik'.")


def zlicz_litery(tekst):
    dane = {}
    for char in tekst:
        if char.isalpha():
            char = char.lower()
            if char in dane:
                dane[char] += 1
            else:
                dane[char] = 1
    return dict(sorted(dane.items()))


def histogram(dane):
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


def Z_pliku(file):
    plik = open(file)
    dane = plik.read()
    plik.close()
    return dane


if __name__ == "__main__":
    main()
