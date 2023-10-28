import matplotlib.pyplot as mat
from sys import exit


def main():
    zrodlo = input("Wprowadz zrodlo danych (tekst lub plik): ").strip()
    znak = input("Czy chcesz zliczyc tylko dany znak (y/n): ").strip()
    if zrodlo == "tekst":
        tekst = input("Wprowadz tekst: ")
        if znak == 'n':
            dane = zLiCz_lItErY(tekst)
        elif znak == 'y':
            dane = Znak(tekst)
        hIsToGrAm(dane)

    elif zrodlo == "plik":
        path = input("Wprowadz sciezke do pliku tekstowego: ")
        tekst = z_PlIkU(path)
        if znak == 'n':
            dane = zLiCz_lItErY(tekst)
        elif znak == 'y':
            dane = Znak(tekst)
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


def Znak(tekst):
    danyZnak = input("Podaj znak, ktory chcesz zliczyc: ")
    dane = {}
    for char in tekst:
        if char == danyZnak:
            if char.isalpha():
                char = char.lower()
                if char in dane:
                    dane[char] += 1
                else:
                    dane[char] = 1
    return dict(sorted(dane.items()))

def z_PlIkU(file):
    plik = open(file)
    dane = plik.read()
    plik.close()
    return dane


def menu1():
    while True:
        print("Menu:")
        print("1. Chce stworzyc histogram z pliku tekstowego.")
        print("2. Chce stworzyc histogram wprowadzajac tekst.")
        print("3. Wyjscie")

        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            zrodlo = "plik"
            break
        elif wybor == "2":
            zrodlo = "tekst"
            break
        elif wybor == "3":
            exit("Koniec programu")
        else:
            print("Nieprawidlowy wybor. Wybierz opcje 1, 2 lub 3")
    return zrodlo


def menu2():
    while True:
        print("Menu:")
        print("1. Chce zliczyc wszystkie litery")
        print("2. Chce zliczyc wybrane litery.")
        print("3. Wyjscie")

        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            znak = "n"
            break
        elif wybor == "2":
            znak = "y"
            break
        elif wybor == "3":
            exit("Koniec programu")
        else:
            print("Nieprawidlowy wybor. Wybierz opcje 1, 2 lub 3")
    return znak


if __name__ == "__main__":
    main()
