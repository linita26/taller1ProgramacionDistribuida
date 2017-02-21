
def vocal(letra):

    

     if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":

        print "Es una vocal"
     else:
        print "No es una vocal"

letra = raw_input("Ingrese el caracter: ")
print vocal(letra)
