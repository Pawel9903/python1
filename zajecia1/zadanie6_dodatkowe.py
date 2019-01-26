from random import randint

nieposortowane = []
posortowane_malejaco = []

for liczba in range(50):
    nieposortowane.append(randint(1,10000))

for liczba in sorted(nieposortowane, reverse=True):
    posortowane_malejaco.append(liczba)

print(posortowane_malejaco)
