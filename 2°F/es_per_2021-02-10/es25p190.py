'''
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario che ha per chiave matricola, mentre il valore associato è il voto.
Elenca i risultati in ordine crescente di voto e succesivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali.
'''

giudizi = {
    "Pippo": 30,
    "Pluto": 22,
    "Paperino": 22
}

voti = list(giudizi.values())
voti_tot = []

for i in range(len(giudizi)):

    if voti[i] not in voti_tot:
        voti_tot.append(voti[i])
        
print(voti_tot)