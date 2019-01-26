liczba_poczatkowa = int(input("Podaj liczbę początkową: "))
liczba_koncowa = int(input("Podaj liczbę końcową: "))
skok = int(input("Podaj odstęp między liczbami: "))

for i in range(liczba_poczatkowa,liczba_koncowa,skok):
    print(i, end=" ")