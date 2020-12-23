'''

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