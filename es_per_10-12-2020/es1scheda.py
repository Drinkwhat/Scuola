parola = input("che parola vuoi scoprire se è un palidromo? ")

if parola == parola[::-1]:
    print("è un palindromo")
    
else:
    print("Non è un palindromo")