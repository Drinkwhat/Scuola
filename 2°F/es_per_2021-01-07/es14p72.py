'''
Crea un programma che scriva la differenza 
di due numeri a e b se il loro prodotto è maggiore di 10,
oppure la loro somma se il prodotto è minore o uguale a 10.
Esegui poi il programma con diverse coppie di valori per a e b:
(-5; 2), (5; -5), (10; 2), (-4; -5), (5; 4), (-3; -2).
'''
try:
    a = float(input("Quanto vale a? "))
    b = float(input("Quanto vale b? "))

    c = a * b

    if c > 10:
        print(a - b)

    else:
        print(a + b)
except:
    print('''scrivi un numero, se è razionale metta''',
    '''il "." al posto della "," e non metta nessun spazio ''')