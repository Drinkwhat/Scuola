'''
Scrivi una programma che data in ingresso una lista A contenente n parole,
restituisca in output una lista B di interi che rappresentano la lunghezza delle parole
contenute in A.
'''
a = []
b = []
while True:
    nome = input("dimmi le parole che vuoi contare i caratteri (per fermare il programma 0) ")
    if nome == "0":
        break
    a.append(nome)
    b.append(len(nome))
      
    
print(b)