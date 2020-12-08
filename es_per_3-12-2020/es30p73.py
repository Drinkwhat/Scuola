num = 0

lunghezza = int(input("Quanto è lungo il numero binario? "))

for l in range(lunghezza):

    cif = int(input("Scirvi la cifra da destra verso sinistra "))
    dec = cif*2**l
    num += dec 
    
print(num)