from random import choice, randrange

slowa = ("Krzysztof", "Stodoła", "Cegła", "Kolor", "Samochód")
wylosowane_slowo = choice(slowa)
losowane_slowo = wylosowane_slowo
#print(wylosowane_slowo)
sukces = wylosowane_slowo
pomieszane = ""
while wylosowane_slowo:
    pozycja = randrange(len(wylosowane_slowo))
    pomieszane += wylosowane_slowo[pozycja]
    wylosowane_slowo = wylosowane_slowo[:pozycja] + wylosowane_slowo[(pozycja+1):]
print(
    """
            Gra 'Wymieszane litery'!!!
    Uporządkuj litery, odgadnij prawidłowe słowo.
    """
)
print("Zgadnij słowo: ", pomieszane)

zgaduj = input("\n Twoja odpowiedź: \n")
krok = 0
strata = 0
print(losowane_slowo[:krok])
while zgaduj != sukces and zgaduj != "":
    print("Niestety to nie to słowo.")
    krok +=1
    strata += 1
    print(losowane_slowo[:krok])
    zgaduj = input("Twoja odpowiedź:")
if zgaduj == sukces:
    print("Zgadza się. Prawidłowa odpowiedź.\n")
punkty = len(losowane_slowo)-strata
print(f"Zdobyłeś {punkty} punkty/ów")
print("\nDziękuję za udział w grze")