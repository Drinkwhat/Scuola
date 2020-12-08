a = []
b = []
while True:
    nome = input("dimmi le parole che vuoi contare (per fermare il programma 0) ")
    a.append(nome)
    if nome == "0":
        break
    b.append(len(nome))
      
    
print(b)