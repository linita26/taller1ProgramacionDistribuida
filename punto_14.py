factor=int(raw_input("ingrese el numero a multiplicar:"))
rango=range(1,11)

for elemento in rango :
    producto=factor * elemento
    print factor, " X ",elemento, " = ", producto
