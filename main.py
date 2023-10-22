def main():
    zrodlo = input("Wprowadz zrodlo danych (tekst lub plik): ").strip()
    if zrodlo == "tekst":
        tekst = input("Wprowadz tekst: ")
        dane = zlicz_litery(tekst)
    elif zrodlo == "plik":
        path = input("Wprowadz sciezke do pliku tekstowego: ")
        tekst = Z_pliku(path)
        dane = zlicz_litery(tekst)
    else:
        print("Nieprawidłowe źródło danych. Wybierz 'tekst' lub 'plik'.")


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


def Z_pliku(file):
    plik = open(file)
    dane = plik.read()
    plik.close()
    return dane


if __name__ == "__main__":
    main()
