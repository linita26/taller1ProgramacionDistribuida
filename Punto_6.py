t = raw_input("Ingrese el texto: ")
def inversa(cadena):
    ncadena = []
    cuenta=len(cadena)
    for i in range(0,len(cadena)):
         cuentas=cuenta-i
         cuentas=cuentas-1
         ncadena.append (cadena[cuentas])
    return ncadena

print inversa(t)