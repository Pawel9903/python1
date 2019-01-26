from math import sqrt

wyjscie = "t"
while wyjscie != "n":
    dane = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")
    lista = []
    for x in dane.split(","):
        lista.append(int(x))
    a, b, c = lista
    print(f"Podano boki: a={a} ; b={b} ; c={c}" )
    if a + b > c and a + c > b and b + c > a:
        print("Z podanych boków można utworzyć trójkąt.")
        if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
            print("Może to być również trójkąt prostokątny!")
            print("Obwód trójkąta prostokątnego wynosi: ", (a+b+c))
            print("Pole trójkąta prostokątnego wynosi: ", round((0.5*a*b),2))
            break
        else:
            print("Z podanych odcinków nie można utworzyć trójkąta prostokątnego.")
        print("Obwód wynosi:", (a + b + c))
        p = 0.5 * (a + b + c)
        P = round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)
        print("Pole wynosi:", P)
        wyjscie = "n"
    else:
        print("Z podanych odcinków nie można utworzyć trójkąta.")
        wyjscie = input("Spróbujesz jeszcze raz (t/n): ")