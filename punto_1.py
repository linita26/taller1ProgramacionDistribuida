def maximo(a,b):

    if a > b:
        return "El numero mayor es "+str(a)
    else:
       return "El numero mayor es  "+str(b)
a = int(input("Ingrese  el primer numero: "))
b = int(input("Ingrese  el segundo numero: "))

print maximo(a,b)