from pylab import *

x = arange(-10, 10.5, 0.5)
a = int(input("Podaj współczynnik a: "))
x1 = []
x2 = []
y1 = []
y2 = []

for i in x:
    if i <= 0:
        x1.append(i)
        y1.append((i/(-3)) + a)
    if i >= 0:
        x2.append(i)
        y2.append((i*i)/3)

xlabel('x')
ylabel('y')
plot(x1, y1)
plot(x2, y2)
title('Wykres f(x)')
grid(True)
show()