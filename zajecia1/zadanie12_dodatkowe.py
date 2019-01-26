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


def wyznacznik(macierzA, rozmiar):
    if rozmiar == 1:
        return macierzA[0][0]
    if rozmiar == 2:
        return macierzA[0][0] * macierzA[1][1] - macierzA[0][1] * macierzA[1][0]
    suma = 0
    for i in range(rozmiar):
        if i % 2 == 0:
            suma += macierzA[0][i] * wyznacznik([wiersz[:i] + wiersz[i + 1:] for wiersz in macierzA[1:]], rozmiar - 1)
        else:
            suma -= macierzA[0][i] * wyznacznik([wiersz[:i] + wiersz[i + 1:] for wiersz in macierzA[1:]], rozmiar - 1)
    return suma

wynik = wyznacznik(macierzA,rozmiar)

print(wynik)


