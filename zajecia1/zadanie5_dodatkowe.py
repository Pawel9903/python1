from math import sqrt
a = int(input("y=ax^2+bx+c Podaj a: "))
b = int(input("y=ax^2+bx+c Podaj b: "))
c = int(input("y=ax^2+bx+c Podaj c: "))

delta = b*b-(4*a*c)

if delta >= 0:
    pierwiastek_delta = float(sqrt(delta))
    if delta>0:
        x1 = (-b-pierwiastek_delta)/(2*a)
        x2 = (-b+pierwiastek_delta)/(2*a)
        print(f"Delta > 0 równanie kwadratowe y = ""{0:+}x^2".format(a), "{0:+}x".format(b), "{0:+}".format(c),
              "posiada dwa rozwiązania.")
        print(f"x1 = {x1} \t\t x2 = {x2}")
    else:
        x0 = -b / (2*a)
        print(f"Delta > 0 równanie kwadratowe y = ""{0:+}x^2".format(a), "{0:+}x".format(b), "{0:+}".format(c),
              "posiada jedno rozwiązanie.")
        print(f"x0 = {x0}")
else:
    print(f"Delta<0 równanie kwadratowe y = ""{0:+}x^2".format(a),"{0:+}x".format(b),"{0:+}".format(c),
          "nie posiada rozwiązań.")
    print(f"Delta wynosi {delta} ")

