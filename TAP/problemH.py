
from sys import stdin, stdout
import itertools 

cajas,cant=[int(x) for x in stdin.readline().strip().split(' ')]  # 

cajasValores = [int(x) for x in stdin.readline().strip().split(' ')]
amin,bmax=[int(x) for x in stdin.readline().strip().split(' ')]  # 
result=0

for valor in itertools.combinations(cajasValores, cant): 
    a=sum(valor)
    if(a<=bmax and a>=amin):
        result+=1
print(result)