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
try:
    bin = input("che numero binario vuoi convertire in decimale? ")

    dec = int(bin, 2)

    print(dec)
except:
    print('''scriva un numero senza nessun spazio''',
    ''' e rispetta l'ordine binario''')