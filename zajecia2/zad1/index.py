import meidana
import avarage

stop = False
count = 1
array_rating = []
rating = 0

while stop == False:
	try:
		rating = int(input('podaj '+ str(count) +' ocene '))

		if int(rating) > 0 and int(rating) < 7:
			array_rating.append(rating)
			count += 1
		else:
			stop = True
	except ValueError:
                print("Podana wartość nie jest liczbą")
if array_rating == 0:
	print('Nie ma żadnych ocen')
else:
	print('wszystkie oceny:')
	print(*array_rating, sep=',')
	meidana.mediana(array_rating)
	avarage.avarage(array_rating)
