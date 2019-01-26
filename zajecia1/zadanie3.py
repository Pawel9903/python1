cena_samochodu = input('Podaj cenę samochodu: ')
cena_samochodu = float(cena_samochodu)

podatek = 0.23
wartosc_podatku = cena_samochodu*podatek

oplata_rejestracyjna = 0.05
wartosc_oplaty_rejestracyjnej = cena_samochodu*oplata_rejestracyjna

prowizja_dealera = 2000

oplata_za_dostarczenie = 500

faktyczna_cena_samochodu = cena_samochodu+wartosc_podatku+wartosc_oplaty_rejestracyjnej+prowizja_dealera+oplata_za_dostarczenie
print('\nPodatek: ', wartosc_podatku)
print('Opłata rejestracyjne: ', wartosc_oplaty_rejestracyjnej)
print('Prowizja dealera: ', prowizja_dealera)
print('Opłata za dostarczenie: ', oplata_za_dostarczenie)
print('\nCałkowita cena samochodu', faktyczna_cena_samochodu)