import math

def wyswietl(przedmioty,opis):
    print(opis)
    for przedmiot in przedmioty:
        print(przedmiot, end=", ")

def srednia(oceny):
    suma = sum(oceny)
    return suma / float(len(oceny))

def mediana(oceny):
    oceny_posortowane = sorted(oceny)
    length = len(oceny_posortowane)
    if len(oceny_posortowane) % 2 == 0:
        half = int(len(oceny_posortowane) / 2)
        return float(sum(oceny_posortowane[half - 1:half + 1])) / 2.0
    else:
        indeks = len(oceny) // 2
        return oceny_posortowane[indeks]

def wariancja(oceny, srednia):
    sigma = 0.0
    for ocena in oceny:
        sigma += (ocena - srednia)**2
    return sigma / len(oceny)

def odchylenie(oceny, srednia):
    return math.sqrt(wariancja(oceny, srednia))