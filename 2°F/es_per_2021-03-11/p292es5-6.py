'''
Elenca le proprietà e metodi della classe Prodotto.
Definisci il metodo assegna_prezzo della classe prodotto.
'''
class Prodotto:
    def __init__(self, name, prezzi, quantita = 1):
        self.name = name
        self.prezzi = prezzi
        self.quantita = quantita
    
    def info(self):
        print("hai comprato",self.quantita, "di", self.name, "ad un totale di", self.quantita * self.prezzi,"euro.")

prodotto = input("Cosa vuoi comprare? ")
quanti = float(input("Quanti ne vuoi? "))
prezzo = float(input("Quanto costa? "))
p1 = Prodotto(prodotto, prezzo, quanti)
p1.info()