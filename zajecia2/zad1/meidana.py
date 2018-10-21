def mediana(array):
	array.sort()
	lenght = len(array)
	print('Mediana: ' + str(array[int(lenght/2)]))
