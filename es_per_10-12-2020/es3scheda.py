parola = input("Quale parola vuoi tradurre in rovarspraket? ")
parola = parola.lower()
rov = ""

for x in range(len(parola)):

    if parola[x] != "a" or "e" or "i" or "o" or "u":
        rov += parola[x] + "o" + parola[x]

    else:
        rov += parola[x]

print(rov)