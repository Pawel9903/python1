while True:
    klucz = int(input("Podaj przesunięcie szyfru cezara (1-10): "))
    if klucz in range(11): break
tekst = input("Podaj tekst do zaszyfrowania: ")

def szyfruj(tekst):
    zaszyfrowany_tekst = ""
    for litera in tekst:
        if ord(litera) > 122 - klucz:
            zaszyfrowany_tekst += chr(ord(litera) + klucz - 26)
        else:
            zaszyfrowany_tekst += chr(ord(litera) + klucz)
    return zaszyfrowany_tekst

deszyfrowany_tekst = szyfruj(tekst)

def deszyfruj(deszyfrowany_tekst):
    zdeszyfrowany_tekst = ""
    for litera in deszyfrowany_tekst:
        if (ord(litera) - klucz) > 96:
            zdeszyfrowany_tekst += chr(ord(litera) - klucz)
            zdeszyfrowany_tekst = zdeszyfrowany_tekst.replace(":",  " ")
        else:
            zdeszyfrowany_tekst += chr(ord(litera) - klucz + 26)
            zdeszyfrowany_tekst = zdeszyfrowany_tekst.replace(":",  " ")

    return zdeszyfrowany_tekst

print("\nTekst zaszyfrowany: ", szyfruj(tekst))
print("\nTekst zdeszyfrowany: ", deszyfruj(deszyfrowany_tekst))



