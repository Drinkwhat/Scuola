veicoli_entrati = 0

while True:
    veicoli = int(input("Quante veicoli sono entrati oggi? (in cifre arabe) "))

    if veicoli == 0:
        break
    
    veicoli_entrati += veicoli

print("sono passati ", veicoli_entrati, "veicoli ")