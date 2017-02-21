a=int(input("Ingrese el Primer Numero"))
b=int(input("Ingrese el Segundo Numero"))
c=int(input("Ingrese el Tercer Numero"))

def max_de_tres(a,b,c):

    if (a > b and a > c):
        print("El numero mayor es el  " + str(a))
    else:
        if (b > a and b > c):
            print("El numero mayor es el  " + str(b))
        else:
            print("El numero mayor es el " + str(c))

print max_de_tres(a,b,c)