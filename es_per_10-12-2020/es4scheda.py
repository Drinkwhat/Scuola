pi = 3.14
poligono = input("Quale area di un poligono vuoi sapere? ")
if poligono == "quadrato" or "Quadrato":
    l = float(input("Qual è il lato del quadrato? (in cm) "))
    print("L'area è:", l**2, "cm^2")
elif poligono == "Cerchio" or "cerchio":
    linea = input ("cosa mi dai? (raggio o diametro) ")

    if linea == "raggio" or "Raggio":
        lunghezza = float(input ("quanto è lungo? (in centimetri) "))

    else:
        lunghezza = float(input ("quanto è lungo? (in centimetri) "))
        lunghezza /= 2
    print ("l'area è", lunghezza**2*pi, "cm^2")
elif poligono == "Rettangolo" or "rettangolo":
    l = float(input("Qual è la base? (in cm) "))
    l2 = float(input("Qual è l'altezza? (in cm) "))
    print(l * l2)