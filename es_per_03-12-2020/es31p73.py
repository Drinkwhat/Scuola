def convertitore (num):

    if num == 0:
        print(0)

    elif num == 1:
        print(1)

    else:
        dec_bin(num)

def dec_bin (num):
    
    if num > 1:
        dec_bin(num//2)
        
    print(num%2, end = "")

i = int(input("che numero vuoi convertire in codice binario? (solo numeri decimali) "))

convertitore(i)