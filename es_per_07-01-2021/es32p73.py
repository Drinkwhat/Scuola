'''
Implemente l'algoritmo per il calcolo della
soluzione di un'equazione di primo grado 
(a * x + b = 0). Il processo risolutivo dipende
dai valori assunti dai coefficienti a e b secondo 
la tabella che segue.


se a = 0 e b = 0 è indeterminata
se a = 0 e b != 0 è impossibile
se a != 0 e b = 0 x = 0
se a != 0 e b != 0 x = -b/a
'''
try:
    a = float(input("Qual è il valore di a? "))
    b = float(input("Qual è il valore di b? "))

    if a    == 0 and b == 0:
        print("L'equazione è indeterminata")

    elif a == 0 and b != 0:
        print("L'equazione è impossibile")

    elif a != 0 and b == 0:
        print("x = 0")

    else:
        print("x = -b/a")
except:
    print('''scrivi un numero, se è razionale metta''',
    '''il "." al posto della "," e non metta nessun spazio ''')