nomi = []
voti = []

for x in range(2):
    p = input("come si chiama il canditato? (solo cognome e lettera maiuscola) ")
    v = int(input("quanti voti ha? "))
    nomi.append(p)
    voti.append(v)

nomi.sort()
voti.sort()
voti.reverse()

print(nomi)
print(voti)
