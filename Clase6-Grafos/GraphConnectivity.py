from sys import stdin, stdout , setrecursionlimit
#Graph Connectivity UVA - 459 
#Accepted
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

 

visited = []
def DFSUtil(x,grafo):
    global visited
    visited.append(x)   
    for vecino in grafo[x]:
        if not vecino in visited:
            DFSUtil(vecino,grafo)

def DFS(graph): 

    global visited
    cant=0
    visited = []
    for x in graph:
        if (not x in visited):
            cant+=1
            DFSUtil(x,graph)
    
    return cant


cases=int(stdin.readline().strip())
stdin.readline()
primera=True
for x in range(cases):
    if (primera):
        primera=False
    else:
        print()
    letra=stdin.readline().strip()
    nodos={}
    for c in char_range("A",letra):
        nodos[c]=[]

    coneccion=stdin.readline().strip()
    while(coneccion!=""):
        posA=coneccion[0]
        posB=coneccion[1]
        nodos[posA].append(posB)
        nodos[posB].append(posA)
        coneccion=stdin.readline().strip()
    print(DFS(nodos))
    