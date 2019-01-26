from random import choice, randrange

slowa = ("pompka", "stodoła", "cegła", "kolor", "samochód")
wylosowane_slowo = choice(slowa)
print(wylosowane_slowo)
ile_liter = len(wylosowane_slowo)
print(f"Wylosowane słowo posiada {ile_liter} liter")
print("\nMasz 5 szans zadania pytania czy dana litera jest zwarta w słowie.")
krok = 0
while krok<5:
    krok += 1
    print(f"Próba {krok}/5.")
    litera = input("\nPodaj literę: ")
    ile=0
    for i in wylosowane_slowo:
        if i == litera:
            ile +=1
    if ile:
        print("Tak")
    else:
        print("Nie")
zgaduj = input("Podaj odpowiednie słowo: ")
if zgaduj == wylosowane_slowo:
    print("\nBrawo. Prawidłowa odpowiedź!!!")
else:
    print("\nBardzo mi przykro. Zła odpowiedź")
