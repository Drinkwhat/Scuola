'''
Verifica se un numero è pari o dispari (un numero è pari quando il resto
della divisione intera per 2 è uguale a 0)
'''
try:
    num = int(input("qual è il numero che vuoi sapere se è pari o dispari? "))

    if num // 2 == num / 2:
        print("il numero è pari")
    
    else:
        print("il numero è dispari")
except:
    print('''scriva un numero e non metta nessun spazio ''')