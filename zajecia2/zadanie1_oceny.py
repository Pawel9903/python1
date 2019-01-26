from zadanie1_ocenydef import wyswietl, srednia, mediana, odchylenie

def main(args):
    przedmioty = set(['polski', 'angielski', 'matematyka', 'historia', 'geografia'])
    przedmioty_posortowane = sorted(przedmioty)
    wyswietl(przedmioty_posortowane, "Lista przedmiotów: ")
    print("\n\nWprowadź brakujące przedmioty. Aby przerwać wprowadzanie przedmiotów, naciśnij Enter.")
    while True:
        przedmiot = input("Podaj nazwę przedmiotu, który chcesz dodać: ")
        if len(przedmiot):
            if przedmiot in przedmioty:
                print("Ten przedmiot już jest dodany!")
            przedmioty.add(przedmiot)
        else:
            przedmioty_uaktualnione = sorted(przedmioty)
            wyswietl(przedmioty_uaktualnione, "\nTwoje przedmioty:")
            przedmiot = input("\n\nZ którego przedmiotu wprowadzisz oceny? ")
            if przedmiot not in przedmioty:
                print("Brak przedmiotu, wprowadź przedmiot by go dodać do listy, naciśnij Enter by wyjść.")
            else:
                break
    oceny = []
    ocena = None
    print("\nAby przerwać wprowadzanie ocen, podaj 0 (zero).")
    while not ocena:
        try:
            ocena = int(input("Wprowadź ocenę (1-6): "))
            if (ocena > 0 and ocena < 7):
                oceny.append(float(ocena))
            elif ocena == 0:
                break
            else:
                print("Błędna ocena.")
            ocena = None
        except ValueError:
            print("Błędne dane!")

    oceny_posortowane = sorted(oceny)
    wyswietl(oceny_posortowane, "\n" + przedmiot.capitalize() + " - wprowadzone oceny: ")

    s = srednia(oceny)
    m = mediana(oceny)
    o = odchylenie(oceny, s)
    print("\n\nŚrednia: {0:5.2f}".format(s))
    print("Mediana: {0:5.2f}\nOdchylenie: {1:5.2f}".format(m, o))
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
