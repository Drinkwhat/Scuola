'''
Risolvi il problema precedente partendo da due liste
che generano un dizionario con la nazione come chiave
e la capitale come valore.

Successivamente interroga il dizionario per visualizzare
la capitale di una nazione
'''


naz_cap = {
    "Italia":"Roma"
}

print("per bloccare il programma scriva Stop")

while True:
    nome_naz = input("Inserisci nome di una nazione: ")
    nome_naz = nome_naz.capitalize()

    nome_cap = input("Inserisci nome della capitale: ")
    nome_cap = nome_cap.capitalize()

    if nome_naz or nome_cap == "Stop":
        break

    elif nome_naz in naz_cap:

        if naz_cap[nome_naz] == nome_cap:
            print("bravo")
        else:
            print("Riprova sarai più fortunato")

    else:
        naz_cap[nome_naz] = nome_cap