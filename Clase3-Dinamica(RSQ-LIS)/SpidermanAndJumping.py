#Spiderman and Jumping CodeChef - SPIDY2 

from sys import stdin,stdout
import sys
sys.setrecursionlimit(200000)
n=int(stdin.readline().strip())

building=[int(n) for n in stdin.readline().strip().split()]
DP=[-1]*n

def spiderman(I):
    if(DP[I] != -1):
        return DP[I]
    if(I==n-1):#si es el ultimo
        return 0
    energyMin=999999999999
    aux=1 
    
    while(I+aux <= (n-1)):
        energyMin=min(energyMin, (abs(building[I]-building[I+aux])  + spiderman(I+aux)) )
        aux<<=1 ## mueve un bit a la izq
    DP[I]=energyMin
    return DP[I]


print(spiderman(0))
