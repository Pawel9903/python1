from random import randint

rozmiar = int(input("Podaj rozmiar macierzy: "))


macierzA = []
print(range(rozmiar))
for element in range(rozmiar):
    wersA = []
    macierzA.append(wersA)
    for liczba in range(rozmiar):
        wersA.append(randint(1,100))

print(macierzA)

macierzB = []
for element in range(rozmiar):
    wersB = []
    macierzB.append(wersB)
    for liczba in range(rozmiar):
        wersB.append(randint(1,100))

print(macierzB)

macierzC = []
for i in range(rozmiar):
    for j in range(rozmiar):
        macierzC.append(macierzA[i][j]+macierzB[i][j])

print(macierzC)








