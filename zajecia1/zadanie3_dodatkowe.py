from os import listdir, path

start = '/'


def przegladaj(katalog):
    for element in listdir(katalog):

        sciezka = path.join(katalog, element);

        print(sciezka)

        if path.isdir(sciezka):
            przegladaj(sciezka)


przegladaj(start)