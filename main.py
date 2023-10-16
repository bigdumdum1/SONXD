def main():
    data = []
    text = input("Wprowadz tekst: ")
    # do poprawy
    for i in range(len(text)):
        if text[i].isalpha():
            if (text[i] in d for d in data):
                data[0][text[i]]
            else:
                data.append({text[i]: 1})

def Z_pliku(file):
    plik = open(file)
    dane = plik.read()
    plik.close()
    return dane

print(Z_pliku("plik.txt"))

if __name__ == "__main__":
    main()
