zamek_szyfrowy = 1234

proba=0

while proba<3:
    proba += 1
    kod = input('Wprowadź kod: ')
    kod = int(kod)
    if zamek_szyfrowy==kod:
        print('Sejf otwarty')
        break
    elif proba==3:
        print('Wprowadzono zły kod. Próba: ' + str(proba) + '/3')
        print('Sejf zablokowany.')
    else:
        print('Wprowadzono zły kod. Próba: ' + str(proba) + '/3')