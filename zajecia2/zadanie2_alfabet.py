print("Alfabet:")
x = 0
for i in range(65, 91):
    litera = chr(i)
    x += 1
    print(litera + litera.lower(), end="")

print("")
for i in range(65, 91):
    litera = chr(i)
    x += 1
    print(litera.lower() + litera, end="")
x = -1
print("\n\nAlfabet od końca:")
for i in range(122, 96, -1):
    litera = chr(i)
    x += 1
    print(litera.upper() + litera, end="")

print("")
for i in range(122, 96, -1):
    litera = chr(i)
    x += 1
    print(litera + litera.upper(), end="")