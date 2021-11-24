'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure un messaggio nel caso la persona non sia presente rubrica.
'''

rubrica = {
    "Pippo": 353556596   
}
print("per bloccare il programma scriva Stop")

while True:
    persona = input("Inserisci nome della persona che vuoi chiamare: ")
    persona = persona.capitalize()

    if persona == "Stop":
        break

    elif persona in rubrica:
        print("Il numero di", persona, "è","\n", rubrica[persona])

    else:
        numero = int(input("Non c'è, inserisci il suo numero: "))
        rubrica[persona] = numero