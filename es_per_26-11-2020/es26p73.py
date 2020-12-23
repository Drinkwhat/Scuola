'''
Calcola la media degli stipendi dei dipendenti di un'azienda,
acquisiti con una ripetizione fino a quando si inserisce il 
valore -1 per segnalare la fine dell'input dei dati.
'''
stipendi1 = 0
count = 0

while True:
    stipendi = int(input("Quanto guadagna il dipendente? "))
    if stipendi == -1:
        break
    stipendi1 += stipendi
    count += 1
    
print(stipendi1 / count)