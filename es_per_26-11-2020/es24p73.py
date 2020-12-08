x = int(input("Quanti voti ha ricevuto il primo candidato? (in cifre arabe) "))
y = int(input("Quanti voti ha ricevuto il secondo candidato? (in cifre arabe) "))

pc = (x + y)/100

if x > y:
    print("ha vinto il primo con ", x/pc)

elif x < y:
    print("ha vinto il secondo con ",  y/pc)
    
else:
    print("sono pari")