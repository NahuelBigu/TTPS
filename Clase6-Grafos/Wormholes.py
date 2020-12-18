from sys import stdin, stdout , setrecursionlimit
#Wormholes UVA - 558 
#Accepted

inf=1e10
def Bellman_Ford(aristas,nodos) :
    dist=[inf for x in range(len(aristas))]
    cantidadNegativa=False
    for i in range(len(nodos)-1):
        for v in aristas:
            if (dist[v[0]] > (dist[v[1]] + v[2])):
                dist[v[0]]= dist[v[1]] + v[2]
    for v in aristas:
        if ( dist[v[0]] > dist[v[1]] + v[2]):
            cantidadNegativa=True
            break
    return cantidadNegativa

cases=int(stdin.readline().strip())
for case in range(cases):
    star,wormholes = stdin.readline().strip().split(' ')
    nodos={}
    for x in range(int(star)):
        nodos[x]=[]

    aristas = []
    for c in range(int(wormholes)):
        entrada= stdin.readline().strip().split(' ')
        aristas.append([int(entrada[0]),int(entrada[1]),int(entrada[2])])
        nodos[int(entrada[0])].append((int(entrada[1]),int(entrada[2])))
  
    print( "possible" if Bellman_Ford(aristas,nodos) else "not possible")