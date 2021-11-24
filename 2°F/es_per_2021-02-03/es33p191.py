'''
In un laboratorio di analisi i pazienti sono sottoposti a un esame specialistico
secondo l'ordine di arrivo:scrivi il programma che consenta di registrare i nomi
dei pazienti man mano che arrivano.
Visualizza poi il nome del paziente che deve essere sottoposto all'esame perchè è
il primo della coda in attesa.
'''
coda = []
print("per bloccare il programma scriva stop")
while True:
    nome = input("inserire i pazienti in ordine di arrivo: ")
   
    if  nome != "stop":
        coda.append (nome)
        
    else:
        break

for i in range(len(coda)):
    print ("il paziente n°", i + 1, "da sottoporre all'esame è", coda [i])