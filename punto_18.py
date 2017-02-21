

palabras=raw_input("Ingrese La  Palabra ")
mayuscula=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cont = 0

for i in palabras:
        if i in mayuscula:
            cont = cont+1
            print "La cadena tiene", cont, "mayuscula/s"

