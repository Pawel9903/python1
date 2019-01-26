ile = int(input("Ile liczb chcesz dodać do listy? "))
lista = []
for i in range(0, ile):
    liczba = int(input("Podaj liczbę: "))
    lista.append(liczba)

print("\nZawartość listy: ([indeks] wartość):")
for i, v in enumerate(lista):
    print("[", i, "]", v)

print("\nElementy w odwrotnej kolejności:")
for element in reversed(lista):
    print(element, end=", ")

print("\n\nElementy posortowane rosnąco:")
for element in sorted(lista):
    print(element, end=", ")

usun = int(input("\n\nPodaj wartość liczby, którą chcesz usunąć?: "))
for i, v in enumerate(lista):
    if i==usun: lista.remove(v)
print(lista)

element = int(input("\nPodaj liczbę, której liczbę wystąpień chcesz sprawdzić: "))
print("Liczba wystąpień: ", lista.count(element))
print("Indeks pierwszego wystąpienia: ", end="")
if lista.count(element):
    print(lista.index(element))
else:
    print("Brak elementu w liście")

i = int(input("\nPodaj indeks początkowy: "))
j = int(input("Podaj indeks końcowy: "))
print(lista[i:j+1])
