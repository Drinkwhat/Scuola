'''
Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore.
Successivamente interroga il dizionario pre visualizzare la capitale di una nazione.
'''

naz=["Italia", "Spagna", "Germania", "Regno unito", "Portogallo"]
cap=["Roma", "Madrid", "Berlino", "Londra", "Lisbona"]
print("Scriva Stop per fermare il programma")
while True:
    naz=input("Inserire una nazione ")
    naz=naz.capitalize()
    if naz=="Stop":
        break
    elif naz in naz:
        print("La capitale di", naz, "è", cap[naz.index(naz)])
    else:
        print("Inserire la capitale di", naz)
        cap=input()
        cap=cap.capitalize()
        naz.append(naz)
        cap.append(cap)
        print("Nazione e Capitale aggiunta correttamente")