plik = open("/Users/piotrglazer/Downloads/wyjscie.txt")
zawartosc_pliku = plik.read()
#print(zawartosc_pliku)

tekst = zawartosc_pliku.split(' ')

#print(tekst)

do_usuniecia = ["się", "i", "oraz", "nigdy", "dlaczego", "To", "jest", "A"]

for slowo in tekst:
    if slowo in do_usuniecia:
        tekst.remove(slowo)

nowy_tekst = " ".join(tekst)

#print(nowy_tekst)

wyjscie = open("/Users/piotrglazer/Downloads/wyjscie.txt", "a")
wyjscie.write(nowy_tekst)
plik.close()
wyjscie.close()

'''
tekst = "to się tak i tak zaczeło oraz nigdy nie skonczyło"
do_usuniecia = ["się", "i", "oraz", "nigdy", "dlaczego"]
tekst_zmieniony = []

for slowo in tekst.split(' '):
    tekst_zmieniony.append(slowo)

for slowo in tekst_zmieniony:
    if slowo in do_usuniecia:
        tekst_zmieniony.remove(slowo)

nowy_tekst = " ".join(tekst_zmieniony)

print(tekst)
print(nowy_tekst)
print(tekst_zmieniony)
'''