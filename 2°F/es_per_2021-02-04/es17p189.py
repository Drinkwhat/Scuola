
'''
Costruisci un dizionario ottenuto da quello dell'esercizio precedente invertevendo oò ruolo di chiave e valore.
Usa il nuovo di dizionario per trovare il nome della nazione, noto il nome della capitale.
'''

cap_naz = {
    "Roma":"Italia"
}

print("per bloccare il programma scriva Stop")

while True:
    nome_cap = input("Inserisci nome della capitale: ")
    nome_cap = nome_cap.capitalize()

    nome_naz = input("Inserisci nome di una nazione: ")
    nome_naz = nome_naz.capitalize()

    if nome_naz or nome_cap == "Stop":
        break

    elif nome_cap in cap_naz:

        if cap_naz[nome_cap] == nome_naz:
            print("bravo")
        else:
            print("Riprova sarai più fortunato")

    else:
        cap_naz[nome_cap] = nome_naz