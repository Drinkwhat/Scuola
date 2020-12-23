'''
Dato un elenco di città, con l'indicazione per ciascuna di esse del nome
e delle temperature massima e minima registrate in un giorno, si devono 
contare quante città hanno superato nel giorno un valore prefissato 
per l'escursione termica, ottenuta per differenza tra temperatura massima e minima.
Organizza un programma che, dopo aver richiesto il valore da controllare dell'escursione termica,
per ogni città dell'elenco ripeta la richiesta dei dati (nome, temperatura massima e minima), 
calcoli l'escursione termica e controlli se l'escursione è maggiore del valore prefissato: 
in questo caso, incrementa il contatore delle città selezionate. Alla fine della ripetizione 
comunica il numero delle città registrato nel contatore.
'''
città1 = []
print("per bloccare il programma prema -1")

escurs = float(input("Qual è valore di escursione di riferimento? "))

while True:

    città = input("Qual è il nome della città? ")
    mi = float(input("Qual è la temperatura minima? "))
    ma = float(input("Qual è la temperatura massima? "))

    if   ma - mi > escurs:
        città1.append(città)
        
    elif ma - mi == -1:
        break

print(len(città1))