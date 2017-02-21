a = input("ingrese el numero del Ano: ")

def es_bisiesto(a):

    if a % 4 == 0 and (not(a % 100 == 0)):
        print "El ano", a, "es un ano bisiesto "
    elif a % 400 == 0:
        print "El ano", a, "es un ano bisiesto "
    else:
        print "El ano", a, "no es bisiesto"
es_bisiesto(a)