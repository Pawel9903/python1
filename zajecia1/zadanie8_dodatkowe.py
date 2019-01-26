
plik = open("/")
zawartosc_pliku = plik.read()
#print(zawartosc_pliku)

tekst = zawartosc_pliku.split(' ')

print(tekst)

do_podmiany = {"to":"jo","i":"oraz", "oraz":"i","nigdy":"prawie nigdy","dlaczego":"czemu","jest":"było"}

for slowo in tekst:
    if slowo in do_podmiany.keys():
        #print(tekst.index(slowo))
        pozycja = tekst.index(slowo)
        tekst[pozycja] = do_podmiany[slowo]

nowy_tekst = " ".join(tekst)

print(nowy_tekst)

wyjscie = open("/", "a")
wyjscie.write(nowy_tekst)
plik.close()
wyjscie.close()
