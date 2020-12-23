'''
I dati relativi al numero di veicoli transitati in entrata 
a un casello autostradale sono inseriti, giorno per giorno,
con una ripetizione che termina quando si inserisce 0 come 
segnalazione della fine dell'input dei dati. 
Comunica il totale dei veicoli transitati nel periodo considerato.
'''

veicoli_entrati = 0

while True:
    veicoli = int(input("Quante veicoli sono entrati oggi? "))

    if veicoli == 0:
        break
    
    veicoli_entrati += veicoli

print("sono passati ", veicoli_entrati, "veicoli ")