def main():
    data = []
    text = input("Wprowadz tekst: ")
    for i in range(len(text)):
        if text[i].isalpha():
            if any(text[i] in d for d in data):
                #do naprawy data[][text[i]] += 1
            else:
                data.append({text[i]: 1})
    print(data)


if __name__ == "__main__":
    main()
