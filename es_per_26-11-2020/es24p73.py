'''
Alla fine della giornata di elezioni per il balottaggio tra due candidati, 
siacquisiscono i voti ottenuti dai candidati. Scrivi il programma che calcoli 
le percentuali ottenute da ciascun candidato e comunichi il nome del vincitore.
'''
x = int(input("Quanti voti ha ricevuto il primo candidato? (in cifre arabe) "))
y = int(input("Quanti voti ha ricevuto il secondo candidato? (in cifre arabe) "))

pc = (x + y)/100

if x > y:
    print("ha vinto il primo con ", x/pc)

elif x < y:
    print("ha vinto il secondo con ",  y/pc)
    
else:
    print("sono pari")