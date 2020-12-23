'''
Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un
palindromo (parole che si leggono uguali anche al contrario) oppure meno.
'''
parola = input("che parola vuoi scoprire se è un palidromo? ")

if parola == parola[::-1]:
    print("è un palindromo")
    
else:
    print("Non è un palindromo")