from pylab import *

a = 1
b = -3
c = 1
x = arange(-10,11,1)
y = []

for i in x:
    y.append((a*i*i)+(b*i)+c)

plot(x,y)
title('Wykres f(x) = a*x^2 + b*x + c')
grid(True)
plt.show()