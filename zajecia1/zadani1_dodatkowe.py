from os import listdir, path, scandir, walk


lista = listdir('/dev')
lista2 = '/dev'


print(len(lista))
print(lista)

print(len([1 for x in list(scandir(lista2)) if x.is_file()]))
print([x for x in list(scandir(lista2)) if x.is_file()])

print(sum(len(files) for _, _, files in walk(lista2)))
print(files for _,_, files in walk(lista2))


