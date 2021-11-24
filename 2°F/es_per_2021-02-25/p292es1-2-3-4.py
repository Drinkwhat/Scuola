'''
Crea una classe Atleta attribuendogli un valore buleano visita_medica,
creando un metodo per assegnarli una squadra, per effettuare la visita medica
e per visualizzare i suoi dati.
'''
class Atleta:
    def __init__(self, name_team, visita_medica = False):
        self.name_team = name_team
        self.visita_medica = visita_medica

    def info(self):
        if self.visita_medica == True:
            print("Gioco per", self.name_team, "ho fatto la visita medica")
        else:
            print("Gioco per", self.name_team, "e non ho fatto la visita medica")
        
a1 = Atleta("juventus", True)
a1.info()