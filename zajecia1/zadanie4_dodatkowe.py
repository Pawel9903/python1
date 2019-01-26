from PIL import Image
from os import listdir, path
from os.path import splitext

katalog = '/'
cel = '.png'

for plik in listdir(katalog):

    nazwa, rozszerzenie = splitext(plik)

    if rozszerzenie == '.jpeg':
        im = Image.open(path.join(katalog, plik))
        im.save(path.join(katalog, nazwa + cel))
        print('Dokonano konwersji pliku:  %s' % plik)
    else:
        print('Zły format pliku. Nie dokonano konwersji pliku:  %s' % plik)

