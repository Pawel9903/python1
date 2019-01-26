import random
liczba = random.randint(1, 49)
#print('Wylosowana liczba: ', liczba)

for i in range(6):
    print('Zgadujesz po raz ', i+1)
    odp = input('Jaka liczbe od 1 do 49 wylosowano: ')
    if liczba == int(odp):
        print('Hura !!!!')
        break
    elif i==5:
        print('No niestety')
        print('Wylosowano: ', liczba)
    elif int(odp)>liczba:
        print('Podana liczba jest za duża.')
    elif int(odp)<liczba:
        print('Podana liczba jest za mała.')

