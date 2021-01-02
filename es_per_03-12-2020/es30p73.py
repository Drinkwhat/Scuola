'''
Fornisci una rappresentazione in decimale di un numeri binario. 
All'inizio si richiede il numero di cifre di cui è composto il 
numero binario (lunghezza); si esegue poi una ripetizione 
che richiedere le cifre del numero binario una a una a partire 
da destra e per ciascuna calcola il prodotto della cifra binaria
per la potenza di 2 corrispondente alla posizione della cifra binaria
e aggiunge il risultato alla somma; la ripetizione viene eseguita per
il contatore che va dal valore 0 al valore di lunghezza diminuito di 1.
Confronta poi il risultato con il valore ottenuto dalla funzione predefinita
del linguaggio per convertire un numero binario in decimale.
'''

num = 0
try:

    lunghezza = int(input("Quanto è lungo il numero binario? "))

    for l in range(lunghezza):

        cif = int(input("Scirvi la cifra da destra verso sinistra "))
        dec = cif*2**l
        num += dec 
    
    print(num)
except:
    print('''scriva un numero senza nessun spazio''')