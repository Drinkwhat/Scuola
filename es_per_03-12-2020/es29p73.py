città1 = []
print("per bloccare il programma prema -1")

escurs = float(input("Qual è valore di escursione di riferimento? "))

while True:

    città = input("Qual è il nome della città? ")
    mi = float(input("Qual è la temperatura minima? "))
    ma = float(input("Qual è la temperatura massima? "))

    if   ma - mi > escurs:
        città1.append(città)
        
    elif ma - mi == -1:
        break

print(len(città1))