from pylab import *

a = int(input("Funkcja a*x-b. Podaj a:"))
b = int(input("Funkcja a*x-b. Podaj b:"))
x = arange(-10, 11)
y = []
for i in x:
    y.append(a * i - b)
plot(x, y)
title('Wykres f(x) = a*x - b')
grid(True)
show()