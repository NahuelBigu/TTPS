from copy import deepcopy
import os
from sys import stdin, stdout

class FordFulkersonAlgorithm:
    def __init__(self,s,d,g):
        self.src = []
        self.src.append(s)
        self.src.append(0)
        self.src.append(0)
        self.dest = d
        self.augPaths = []
        self.augPathsGraph = []
        self.graph = g
        

    def checkPath(self,path, graph3,mini):
        i = 0
        src = path[i][0]
        dest = path[-1][0]
        while src != dest:
            for n in range(1, len(graph3[src])):
                if graph3[src][n][0] == path[i+1][0]:
                    if graph3[src][n][2]+mini > graph3[src][n][1] or \
                    graph3[src][n][2] == graph3[src][n][1] : #n = node
                        return False
                    break
            i+=1
            src = path[i][0]
        return True

    def updateWeigth(self,s , d, mi):
        for i in range(1, len(self.graph[s])):
            if self.graph[s][i][0] == d:
                self.graph[s][i][2] += mi
                return 0

    def augumentedPaths(self, src, dest, graph, path=[]):
        graph[src[0]][0] = True
        path.append(src)
        src = src[0]
        if src == dest:
            temp = deepcopy(path)
            self.augPaths.append(temp)
        else:
            for i in range(1, len(graph[src])):
                if graph[graph[src][i][0]][0] == False:
                    self.augumentedPaths(graph[src][i], dest, graph , path)
        path.pop()
        graph[src][0] = False

    def maximumFlow(self):
        self.augumentedPaths(self.src, self.dest, self.graph)
        maxFlow = 0
        for p in self.augPaths:
            mini = []
            for j in range(1, len(p)):
                mini.append(p[j][1])
            mini = min(mini)
            if self.checkPath(p, self.graph, mini):
                maxFlow += mini
                for j in range(len(p)-1):
                    self.updateWeigth(p[j][0] , p[j+1][0],mini)
                #self.createGraph(self.graph, p)
        #self.createGraph(self.graph,None,1)
        return maxFlow



    
firstLine=stdin.readline().split()
while firstLine != ["0","0"]:
    #firstLine[0] es el numero de categorias firstLine[1] es el numero de problemas
    nCat=int(firstLine[0])
    nPro=int(firstLine[1])
    n=nCat+nPro+2 # El grafo va a tener tantos nodos como categorais + problemas + 2 nodos que serian el s y el t para el Ford Fulkerson
    s="s"    #Primer nodo
    t="t"  #Ultimo nodo
    graph={'s': [False],
           't': [False]} # Los primeros nCat numeros van a pertenecer a 

    # La segunda linea contiene nCat numeros que hacen referencia a cuantos problemas pueden ser incluidos en la categoria de la posicion i
    secondLine=stdin.readline().split() 
    cantidadMaxima=0    
    # Seteo las aristas que van desde la categoria a t para definir la cantidad de problemas que pueden tener.
    for x in range(1,nCat+1):
        graph["Cat-"+str(x)]=[False,['t',int(secondLine[x-1]),0]]
        cantidadMaxima+=int(secondLine[x-1])
   
    # Las siguientes nPro lineas contienen en primer lugar la cantidad de categorias a las que puede pertenecer y luego esa misma cantidad de numeros que hacen referencia a la categoria
    for iProblem in range(nPro):
        graph["s"].append(["Pro-"+str((iProblem+1)),1,0])

        graph["Pro-"+str(iProblem+1)]=[False]
        
        prob_cat=stdin.readline().split() 
        for x in range(int(prob_cat[0])):
            categoria=int(prob_cat[x+1])
            graph["Pro-"+str(iProblem+1)].append(["Cat-"+str(categoria),1,0])
            
    
    
    src = 's'
    dest = 't'
    obj = FordFulkersonAlgorithm(src, dest, graph)

    
    
    if (obj.maximumFlow() == cantidadMaxima):
        stdout.write("1\n")
        paraImpr={}
        for x in range(nCat):
            paraImpr[str(x+1)]=[]
        for key in obj.graph:
            if key.startswith("Pro"):
                categorias=obj.graph[key][1:]
                for c in categorias:
                    if (c[2]==1):
                        paraImpr[str(c[0][4:])].append(key[4:])
        for key in paraImpr:
            stdout.write(" ".join(paraImpr[key])+"\n")
    else:
        stdout.write("0\n")
    
    firstLine=stdin.readline().split()

   