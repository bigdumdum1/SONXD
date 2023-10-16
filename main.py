def Z_pliku(file):
    plik = open(file)
    dane = plik.read()
    plik.close()
    return dane

print(Z_pliku("plik.txt"))
