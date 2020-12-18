
from sys import stdin,stdout


snma="ff02:0000:0000:0000:0000:0001:ff"
direccion=input("Ingrese direccion destino completa IPV6: ")
snma+= direccion[-7:]
print("SNMA:"+snma)



MMA="33:33:"
i=0
for x in snma[-9:]:
    if(x != ":"):
        i+=1
        MMA+=x
        if(i==2):
            MMA+=":"
            i=0
print("MMA: "+MMA[:-1])