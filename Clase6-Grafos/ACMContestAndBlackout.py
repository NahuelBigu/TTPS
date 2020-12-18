from sys import stdin, stdout , setrecursionlimit
#ACM Contest and Blackout UVA - 10600 
#Accepted
def kruskalito(aristas,vertices):
    aristas.sort(key=lambda item: item[2])
    mst={}
    for cross in range(1,vertices+1):
        mst[cross]={}
    conocidos =[ {x} for x in range(0,vertices+1)]

    for ari in aristas:
        if not ari[1] in conocidos[ari[0]]:
            aux= conocidos[ari[0]].union(conocidos[ari[1]])
            for setnum in aux:
                conocidos[setnum]=aux
            mst[ari[0]][ari[1]]= ari[2]
            mst[ari[1]][ari[0]]= ari[2]

    return mst 

cases=int(stdin.readline().strip())
for case in range(cases):
    school,connections = stdin.readline().strip().split(' ')
    aristas = []
    for c in range(int(connections)):
        entrada= stdin.readline().strip().split(' ')
        aristas.append([int(entrada[0]),int(entrada[1]),int(entrada[2])])

    primer= kruskalito(aristas,int(school))  
    aristasPrimer=[]
    minPrimero=0
    for x in primer:
        for i in primer[x]:
            if not [i,x,primer[i][x]] in aristasPrimer:
                aristasPrimer.append([x,i,primer[x][i]])
                minPrimero+=primer[x][i]


    minSegundo=10e9
    for ar in aristasPrimer:
        aristaAux=aristas[:]    
        if ar in aristaAux: aristaAux.remove(ar)
        else: aristaAux.remove([ar[1],ar[0],ar[2]])
        
        segundo=kruskalito(aristaAux,int(school))
        aristasSegundo=[]
        minSegundoAux=0
        for x in segundo:
            for i in segundo[x]:
                if not [i,x,segundo[i][x]] in aristasSegundo:
                    aristasSegundo.append([x,i,segundo[x][i]])
                    minSegundoAux+=segundo[x][i]
        if(minSegundoAux>=minPrimero):
            minSegundo= min(minSegundoAux,minSegundo)
        
    print(str(minPrimero) + " " + str(minSegundo))