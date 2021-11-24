'''
Con riferimento al dizionario del problema precedente, 
elenca i numeri di matricola degli studenti che hanno ottenuto
una votazione superiore alla media di tutte le votazioni
'''

giudizi = {
    "Pippo": 30,
    "Pluto": 22,
    "Paperino": 22,
    "Ciao": 0
}

voti = list(giudizi.values())
media  = sum(voti) / len(giudizi)
print(media)
alunni_sopra_media = []

for i in range(len(giudizi)):
    if voti[i] > media:
        pass   