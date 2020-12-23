'''
Dato un elenco di studenti partecipanti a una gara sportiva
di lancio del peso (nome studente, lancio), visualizza il valore 
del lancio del vincitore (valore massimo).
'''

punti = []
print("per bloccare il programma prema -1")

while True:

    nome = input("Qual è il nome del giocatore? ")
    point = float(input("quanti metri ha fatto? " ))

    if point == -1:
        break

    punti.append(point)

print("il punteggio più alto è", max(punti))