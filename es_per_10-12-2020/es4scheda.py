from math import pi

poligono = input("Quale area di un poligono vuoi sapere? ")

if poligono == "quadrato" or "Quarato":

    linea = input("Cosa mi dai? (perimetro o diagonale o lato) ")

    if linea == "Perimetro" or "perimetro":
        
        l = float(input("Qual è il perimetro? "))
        l /= 4
        l **= 2
        
    elif linea == "lato" or "Lato":  
        l = float(input("Qual è il lato del quadrato? (in cm) "))
        l **= 2

    else:
        l = float(input("Qual è la diagonale? (in cm) "))

        l = (l**2)/2

    print("L'area è:", l, "cm^2")

elif poligono == "Cerchio" or "cerchio":

    linea = input ("Cosa mi dai? (raggio o diametro) ")

    if linea == "raggio" or "Raggio":
        lunghezza = float(input ("quanto è lungo? (in centimetri) "))

    else:
        lunghezza = float(input ("quanto è lungo? (in centimetri) "))
        lunghezza /= 2
    
    print ("l'area è", lunghezza**2*pi, "cm^2")

else:

    l = float(input("Qual è la base? (in cm) "))
    l2 = float(input("Qual è l'altezza? (in cm) "))
    print(l * l2)