from sys import stdin, stdout , setrecursionlimit
setrecursionlimit(110)
class Graph:
    def __init__(self,pos,dirigido=True):
            self.adyacentes = []
            self.pesos = []
            self.dirigido=dirigido
            self.pos=pos

    def agregarAdyacente(self,adyacente,peso=1):
        self.adyacentes.append(adyacente)
        self.pesos.append(peso)
        if (self.dirigido):
            adyacente.adyacentes.append(self)
            adyacente.pesos.append(peso)
    
    def adyacentes(self):
        return self.adyacentes
    def pesos(self):
        return self.pesos

    def pos(self):
        return self.pos
    

def dijkstra(G,s,t):
    vis=[False]* (len(G)+2)
    coladeprioridad=[]
    coladeprioridad.insert(0,(0,s))
    mini=1e10
    while(len(coladeprioridad) != 0):
        arc=coladeprioridad.pop()
        v= arc[1]
        p= arc[0]
       
        if(v == t): 
            mini= min(mini,p)
            vis[v.pos]= False
            
        if (not vis[v.pos]):
            vis[v.pos]= True
            for i in range(len(v.adyacentes)):
                u=v.adyacentes[i]
                w=v.pesos[i]

                coladeprioridad.insert(0,(max(p,w),u))
        

    return mini
"""
def BFS(graph, s, t): 

    # Mark all the vertices as not visited 
    visited = [False] * (len(graph)+1) 

    # Create a queue for BFS 
    queue = [] 

    # Mark the source node as  
    # visited and enqueue it 
    queue.append(s) 
    visited[s] = True
    maximoD=-1
    decibeles=0
    while queue: 

        # Dequeue a vertex from  
        # queue and print it 
        s = queue.pop(0) 
    
        # Get all adjacent vertices of the 
        # dequeued vertex s. If a adjacent 
        # has not been visited, then mark it 
        # visited and enqueue it 
        for i in s.adyacentes: 
            if visited[i.pos] == False: 
                queue.append(i)
                
                visited[i.pos] = True


maximoReturn=1e9
visited = set()
def DFSUtil( v, peso,maximo , t):
    global maximoReturn
    global visited
    
    maximo=max(maximo,peso)
  
    if(v == t):
        maximoReturn=min(maximo,maximoReturn)
    else:  
        visited[v.pos] =True   
        for i,neighbour in enumerate(v.adyacentes):
            if not visited[neighbour.pos]:
                DFSUtil(neighbour,v.pesos[i],maximo,t)
                visited[neighbour.pos]=False

def DFS(s,t): # s = nodo inicial , t = nodo destino
    global maximoReturn
    global visited
    maximoReturn=1e9

    visited = [False] * (len(streets)+1) 
    visited[s.pos] =True
    DFSUtil(s,0,0,t)
    return maximoReturn
"""
def kruskal(s,t):
    listaAristas=sorted(self.connections.items(),key=lambda item: item[1])
    nuevasAristas={}
    for e in listaAristas:
        if self.ufds.find(e[0][0])!=self.ufds.find(e[0][1]):
            nuevasAristas[e[0]]=e[1]
            self.ufds.union(e[0][0],e[0][1])
    self.connections=nuevasAristas
    """ for k in self.g.keys():
        self.g[k]=set()
    for k in self.connections.keys():
        self.g[k[0]].add(k[1])
        self.g[k[1]].add(k[0])"""

streets={}
conections=0
querys=0
cases=0
primera=True
for line in stdin:
    line=line.strip().split(' ')
    if(line[0]=="0" and line[1]=="0" and line[2]=="0"): break
    if(conections==0 and querys==0):
        #Case first input
        cases+=1
        conections=int(line[1])
        querys=int(line[2])
        for x in range(int(line[0])):
            streets[x+1]=Graph(x+1)
        if (primera):
            primera=False
        else:
            print() 
        print("Case #"+str(cases))
    elif(conections>0):
        # Leo conecciones
        conections-=1
        streets[int(line[0])].agregarAdyacente(streets[int(line[1])],int(line[2]))
    else:
        #query
        querys-=1
        #res=DFS(streets[int(line[0])],streets[int(line[1])])
        res=dijkstra(streets,streets[int(line[0])],streets[int(line[1])])
        print(res if (res!=1e10) else "no path")
