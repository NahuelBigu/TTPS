import itertools 
from sys import stdin, stdout


INFINITO = 1e1000
def calcSlope(a, b):
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    if dx == 0:
        return INFINITO
    return dy/dx


def point_in_line(points):
    
    n = len(points)
    for i in range(n):
        slopes = -1
        for j in range(i+1, n):
            slope = calcSlope(points[i], points[j])
            if (slope == -1):
                slopes=slope
            else:
                if(slope!=slopes):
                    return False
    return True

casos=int(stdin.readline())
numeros=[int(x) for x in stdin.readline().strip().split(' ')]
i=0
arr=[]
puntaje=0
for valor in itertools.permutations(numeros,casos): 
    for _ in range(int(len(valor)/2)-1):
        t=(valor[i],valor[i+1])
        i+=2
        arr.append(t)
    puntaje += 1 if point_in_line(arr) else 0
print(puntaje)