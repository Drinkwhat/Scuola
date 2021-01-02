'''
A un concorso pubblico hanno partecipato due candidati 
prima in ordine alfabetico e poi in ordine decrescente 
di punteggio.
'''
nomi = []
voti = []
try:
    for x in range(2):
        p = input("come si chiama il canditato? (solo cognome) ")
        p.lower()
        v = int(input("quanti voti ha? "))
        nomi.append(p)
        voti.append(v)

    nomi.sort()
    voti.sort()
    voti.reverse()

    print(nomi)
    print(voti)
except:
    print('''scriva un numero senza nessun spazio''')
