
from sys import stdin, stdout

[a, b] = [int(x) for x in stdin.readline().strip().split()]

mapa = [[-1 for  in range(b)] for  in range(a)]

for i in range(a):
    mapa[i] = list(stdin.readline().strip())

cant_palabras = int(stdin.readline().strip())
palabras = []
for i in range(cant_palabras):
    palabras.append(stdin.readline().strip())

iteracion_de_palabras = []


for i in range(a):
    for j in range(b):
        for p in palabras:
            p=list(p)
            aux=[]
            if(len(p)+j > p):
                for x in range(len(p)):
                    if()
            if mapa[i][j] in p: