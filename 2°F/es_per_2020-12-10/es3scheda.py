'''
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto
"rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni
consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola
"mangiare" diventa "momanongogiarore".
Scrivi una programma in grado di tradurre una parola o frase passata tramite input in
"rövarspråket".
Dopo aver tradotto una frase, il programma dovrå chiedere all'utente se intende
tradume un'altra, e in caso di risposta positiva, dovrå attendere Ilinserimento di una
nuova parola da parte dell'utente.
'''
parola = input("Quale parola vuoi tradurre in rovarspraket? ")
parola = parola.lower()
rov = ""

for x in range(len(parola)):

    if parola[x] != "a" or "e" or "i" or "o" or "u":
        rov += parola[x] + "o" + parola[x]

    else:
        rov += parola[x]

print(rov)