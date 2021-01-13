def risolvi_primo_grado():
    if b == 0:
        if c == 0:
            print("equazione indeterminata")
        else:
            print("equazione impossibile")
    else:
        print("x =", -c / b)


def calcola_delta():
    d = b ** 2 - 4 * a * c
    return d

def risolvi_secondo_grado():
    delta = calcola_delta()
    if delta < 0:
        print("Non esistono soluzioni reali")

    else:
        x1 = (-b + (delta) ** 1/2 / (2*a))
        x2 = (-b - (delta) ** 1/2 / (2*a))
        print("x1 =", x1)
        print("x2 =", x2)
try:
    a = float(input("1° coefficiente: "))
    b = float(input("2° coefficiente: "))
    c = float(input("3° coefficiente: "))
except:
    print('''Devi mettere solo numeri arabi e al posto della
     "," metti "." e riavvia il programma''')

if a != 0:
    risolvi_secondo_grado()
else:
    risolvi_primo_grado()