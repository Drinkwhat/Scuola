'''Data la parabola y = ax² + bx + c, definisci due funzioni per calcolarne i punti significativi: vertice e fuoco.
Le due funzioni ricevono come parametri a, b, c e restituiscono il valore calcolato'''

def fuoco(a, b, c):
    delta = b**2 - 4*a*c
    x_fuoco = -b/2*a
    y_fuoco = (1-delta)/4*a
    return x_fuoco, y_fuoco

def vertice(a, b, c):
    delta = b**2 - 4*a*c
    x_vertice = -b/2*a
    y_vertice = -delta/4*a
    return x_vertice, y_vertice

try:
    def main():
        a = float(input("Definisci il valore di a: "))
        b = float(input("Definisci il valore di b: "))
        c = float(input("Definisci il valore di c: "))
        ris_fuoco = fuoco(a, b, c)
        ris_vertice = vertice(a, b, c)
        print("Le coordinate del vertice della parabola: ", ris_vertice)
        print("Le coordinate del fuoco della parabola: ", ris_fuoco)
except:
    print('''Devi mettere solo numeri arabi e al posto della
     "," metti "." e riavvia il programma''')

main()