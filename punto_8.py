elementos= int(input("Introduce cantidad de elementos: "))
lista1=[]
lista2=[]
for i in range(0,elementos):
    lista1.append(raw_input("lista 1 posicion ["+str(i+1)+str("] ")))

for i in range(0,elementos):
    lista2.append(raw_input("lista 2 posicion ["+str(i+1)+str("] ")))
igual=0;
for i in range(0, elementos):
    for y in range(0, elementos):
        if(lista1[i]==lista2[y]):
            igual=igual+1

if igual>=1:
    print "true"
else:
    print "false"