num = int(raw_input("Ingrese un numero decimal "))
binario = ""
if (num > 0):
    while(num > 0):
        if (num%2 == 0):
            binario = "0" + binario
        else:
            binario = "1" + binario
        num = int(num/2)
else:
    if (num == 0):
        binario = "0"

print("El numero Binario es : "+binario)