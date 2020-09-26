#Spiderman and Jumping CodeChef - SPIDY2 

from sys import stdin,stdout


n=int(stdin.readline().strip())

building=[int(n) for n in stdin.readline().strip().split()]

DP=[-1]*n
for x in reversed(range(n)):
    DP[x]=[-1]*n
    #DP[n-x-1]=[-1]*(x+1)



def spiderman2(I,J,energyCost):
    if(DP[I][J] != -1 and DP[I][J]<energyCost):
        return DP[I][J]
    DP[I][J]=abs(building[I]-building[J])+energyCost
    if (J==n-1):
        return DP[I][J]
    aux=1
    energyCost+=DP[I][J]
    energyMin=spiderman2(J,J+aux,energyCost)
    aux*=2
    while(J+aux<=n-1):
        energyMin= min(energyMin,spiderman2(J,J+aux,energyCost))
        aux*=2
    return energyMin + energyCost

spiderman2(0,0,0)
minimo=999999999999999
for d in DP:
    if(minimo>d[n-1] and d[n-1]!= -1):
        minimo=d[n-1]
print(minimo)