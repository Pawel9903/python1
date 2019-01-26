from os import path

slownik = {}
plik = "slownik.txt"

def otworz(plik):
    if path.isfile(plik):
        with open(plik, "r") as pliktxt:
            for line in pliktxt:
                linia = line.split(":")
                j_obcy = linia[0]
                tlumaczenie = linia[1].rstrip()
                tlumaczenie = tlumaczenie.split(",")
                slownik[j_obcy] = tlumaczenie
    return len(slownik)

def zapisz(slownik):
    pliktxt = open(plik, "w")
    for j_obcy in slownik:
        znaczenia = ",".join(slownik[j_obcy])
        linia = ":".join([j_obcy, znaczenia])
        pliktxt.write(linia+"\n")
    pliktxt.close()

def zamiana(str):
    str = str.strip()
    str = str.lower()
    return str

print("""Podaj dane w formacie:
'wyraz obcy: znaczenie1, znaczenie2'
Aby zakończyć wprowadzanie danych, wpisz 'koniec'.
""")

nowy = False
ileWyrazow = otworz(plik)
print("Liczba słów w bazie:", ileWyrazow)

while True:
    dane = input("Wprowadź dane: ")
    linia = dane.split(":")
    j_obcy = linia[0].strip().lower()
    if j_obcy == 'koniec':
        break
    elif dane.count(":") == 1:
        if j_obcy in slownik:
            print("Wyraz", j_obcy, " i jego znaczenia są już w słowniku.")
            czy_zamienic = input("Zastąpić wpis (t/n)? ")
        if j_obcy not in slownik or czy_zamienic == "t":
            znaczenia = linia[1].split(",")
            znaczenia = list(map(zamiana, znaczenia))
            slownik[j_obcy] = znaczenia
            nowy = True
    else:
        print("Błędny format!")

if nowy:
    zapisz(slownik)

print(slownik)

print("=" * 50)
print("{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia"))
print("=" * 50)
for j_obcy in slownik:
    print("{0: <15}{1: <40}".format(j_obcy, ",".join(slownik[j_obcy])))
